#!/usr/bin/env python3
"""Build the complete Odisea book as PDF, optionally also as DOCX."""

from __future__ import annotations

import argparse
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import List, Sequence
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parent
BOOK_TEX = ROOT / "odisea_book.tex"
COMMON_TEX = ROOT / "odisea_common.tex"
PDF_OUTPUT = ROOT / "odisea_book.pdf"
DOCX_OUTPUT = ROOT / "odisea_book.docx"

SOURCE_INPUT_RE = re.compile(r"\\input\{(src/odisea[^{}]+)\}")
PANDOC_CHAPTER_MACRO = (
    r"\newcommand{\odiseachapter}[2]{\chapter{#2}}"
    "\n"
    r"\renewenvironment{versopropio}"
    r"{\begin{verse}\itshape"
    r"\renewcommand{\stanzabreak}{\par\itshape}}"
    r"{\end{verse}}"
    "\n"
)
PANDOC_PAGE_BREAK = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n'
PANDOC_STRUCTURE_FILTER = r'''
local chapter_numbers = {}
local page_break = pandoc.RawBlock(
  "openxml",
  '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'
)

local function roman(number)
  local numerals = {
    {1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"},
    {100, "C"}, {90, "XC"}, {50, "L"}, {40, "XL"},
    {10, "X"}, {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"}
  }
  local result = ""
  for _, numeral in ipairs(numerals) do
    while number >= numeral[1] do
      result = result .. numeral[2]
      number = number - numeral[1]
    end
  end
  return result
end

function Pandoc(document)
  local chapter = 0
  for _, block in ipairs(document.blocks) do
    if block.t == "Header" and block.level == 1 then
      chapter = chapter + 1
      local number = roman(chapter)
      chapter_numbers["#" .. block.identifier] = number
      block.content:insert(1, pandoc.Space())
      block.content:insert(1, pandoc.Str(number .. "."))
    end
  end

  document = document:walk {
    Link = function(link)
      local number = chapter_numbers[link.target]
      if number and link.attributes["reference-type"] == "ref" then
        link.content = pandoc.Inlines {pandoc.Str(number)}
      end
      return link
    end
  }

  local blocks = pandoc.Blocks {}
  for _, block in ipairs(document.blocks) do
    if block.t == "Header" and block.level == 1 then
      blocks:insert(page_break)
    end
    blocks:insert(block)
  end
  document.blocks = blocks
  return document
end
'''

WORDPROCESSINGML = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
OFFICE_RELATIONSHIPS = (
    "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
)
PACKAGE_RELATIONSHIPS = (
    "http://schemas.openxmlformats.org/package/2006/relationships"
)
CONTENT_TYPES = "http://schemas.openxmlformats.org/package/2006/content-types"
ElementTree.register_namespace("w", WORDPROCESSINGML)
ElementTree.register_namespace("r", OFFICE_RELATIONSHIPS)


def word_tag(name: str) -> str:
    return f"{{{WORDPROCESSINGML}}}{name}"


def relationship_tag(name: str) -> str:
    return f"{{{PACKAGE_RELATIONSHIPS}}}{name}"


def content_type_tag(name: str) -> str:
    return f"{{{CONTENT_TYPES}}}{name}"


def paragraph_properties(style: ElementTree.Element) -> ElementTree.Element:
    properties = style.find(word_tag("pPr"))
    if properties is None:
        properties = ElementTree.SubElement(style, word_tag("pPr"))
    return properties


def set_word_value(element: ElementTree.Element, name: str, value: str) -> None:
    element.set(word_tag(name), value)


def customize_reference_doc(reference_doc: Path) -> None:
    """Match the DOCX body more closely to the typeset PDF."""
    with zipfile.ZipFile(reference_doc, "r") as archive:
        members = [(info, archive.read(info.filename)) for info in archive.infolist()]

    customized = []
    for info, data in members:
        if info.filename == "word/styles.xml":
            root = ElementTree.fromstring(data)
            styles = {
                style.get(word_tag("styleId")): style
                for style in root.findall(word_tag("style"))
            }

            body_properties = paragraph_properties(styles["BodyText"])
            spacing = body_properties.find(word_tag("spacing"))
            if spacing is None:
                spacing = ElementTree.SubElement(body_properties, word_tag("spacing"))
            set_word_value(spacing, "line", "288")
            set_word_value(spacing, "lineRule", "auto")
            justification = body_properties.find(word_tag("jc"))
            if justification is None:
                justification = ElementTree.SubElement(body_properties, word_tag("jc"))
            set_word_value(justification, "val", "both")

            verse_properties = paragraph_properties(styles["BlockText"])
            verse_justification = verse_properties.find(word_tag("jc"))
            if verse_justification is None:
                verse_justification = ElementTree.SubElement(
                    verse_properties, word_tag("jc")
                )
            set_word_value(verse_justification, "val", "left")

            toc_style = styles.get("TOC1")
            if toc_style is None:
                toc_style = ElementTree.SubElement(
                    root,
                    word_tag("style"),
                    {
                        word_tag("type"): "paragraph",
                        word_tag("styleId"): "TOC1",
                    },
                )
                name = ElementTree.SubElement(toc_style, word_tag("name"))
                set_word_value(name, "val", "toc 1")
                based_on = ElementTree.SubElement(toc_style, word_tag("basedOn"))
                set_word_value(based_on, "val", "Normal")
                next_style = ElementTree.SubElement(toc_style, word_tag("next"))
                set_word_value(next_style, "val", "Normal")
                priority = ElementTree.SubElement(toc_style, word_tag("uiPriority"))
                set_word_value(priority, "val", "39")
                ElementTree.SubElement(toc_style, word_tag("semiHidden"))
                ElementTree.SubElement(toc_style, word_tag("unhideWhenUsed"))

            toc_properties = paragraph_properties(toc_style)
            tabs = toc_properties.find(word_tag("tabs"))
            if tabs is None:
                tabs = ElementTree.SubElement(toc_properties, word_tag("tabs"))
            for old_tab in list(tabs):
                tabs.remove(old_tab)
            tab = ElementTree.SubElement(tabs, word_tag("tab"))
            set_word_value(tab, "val", "right")
            set_word_value(tab, "leader", "none")
            set_word_value(tab, "pos", "8278")
            toc_spacing = toc_properties.find(word_tag("spacing"))
            if toc_spacing is None:
                toc_spacing = ElementTree.SubElement(
                    toc_properties, word_tag("spacing")
                )
            set_word_value(toc_spacing, "before", "0")
            set_word_value(toc_spacing, "after", "0")
            set_word_value(toc_spacing, "line", "240")
            set_word_value(toc_spacing, "lineRule", "auto")
            toc_justification = toc_properties.find(word_tag("jc"))
            if toc_justification is None:
                toc_justification = ElementTree.SubElement(
                    toc_properties, word_tag("jc")
                )
            set_word_value(toc_justification, "val", "left")
            data = ElementTree.tostring(root, encoding="utf-8", xml_declaration=True)

        elif info.filename == "word/settings.xml":
            root = ElementTree.fromstring(data)
            update_fields = root.find(word_tag("updateFields"))
            if update_fields is None:
                update_fields = ElementTree.SubElement(root, word_tag("updateFields"))
            set_word_value(update_fields, "val", "true")
            data = ElementTree.tostring(root, encoding="utf-8", xml_declaration=True)

        customized.append((info, data))

    temporary_doc = reference_doc.with_suffix(".customized.docx")
    with zipfile.ZipFile(temporary_doc, "w") as archive:
        for info, data in customized:
            archive.writestr(info, data)
    os.replace(temporary_doc, reference_doc)


def add_page_layout(
    section: ElementTree.Element,
    footer_relationship: str,
    number_format: str,
    first_number: int,
    *,
    next_page: bool = False,
    hide_first_page_number: bool = False,
) -> None:
    footer_reference = ElementTree.Element(word_tag("footerReference"))
    set_word_value(footer_reference, "type", "default")
    footer_reference.set(
        f"{{{OFFICE_RELATIONSHIPS}}}id", footer_relationship
    )
    section.insert(0, footer_reference)
    if next_page:
        section_type = ElementTree.SubElement(section, word_tag("type"))
        set_word_value(section_type, "val", "nextPage")
    page_size = ElementTree.SubElement(section, word_tag("pgSz"))
    set_word_value(page_size, "w", "11906")
    set_word_value(page_size, "h", "16838")
    page_margins = ElementTree.SubElement(section, word_tag("pgMar"))
    for side in ("top", "right", "bottom", "left"):
        set_word_value(page_margins, side, "1814")
    set_word_value(page_margins, "header", "720")
    set_word_value(page_margins, "footer", "720")
    set_word_value(page_margins, "gutter", "0")
    page_numbering = ElementTree.SubElement(section, word_tag("pgNumType"))
    set_word_value(page_numbering, "fmt", number_format)
    set_word_value(page_numbering, "start", str(first_number))
    if hide_first_page_number:
        ElementTree.SubElement(section, word_tag("titlePg"))


def page_number_footer() -> bytes:
    footer = ElementTree.Element(word_tag("ftr"))
    paragraph = ElementTree.SubElement(footer, word_tag("p"))
    properties = ElementTree.SubElement(paragraph, word_tag("pPr"))
    justification = ElementTree.SubElement(properties, word_tag("jc"))
    set_word_value(justification, "val", "center")

    begin_run = ElementTree.SubElement(paragraph, word_tag("r"))
    begin = ElementTree.SubElement(begin_run, word_tag("fldChar"))
    set_word_value(begin, "fldCharType", "begin")
    set_word_value(begin, "dirty", "true")
    instruction_run = ElementTree.SubElement(paragraph, word_tag("r"))
    instruction = ElementTree.SubElement(instruction_run, word_tag("instrText"))
    instruction.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    instruction.text = " PAGE "
    separate_run = ElementTree.SubElement(paragraph, word_tag("r"))
    separate = ElementTree.SubElement(separate_run, word_tag("fldChar"))
    set_word_value(separate, "fldCharType", "separate")
    result_run = ElementTree.SubElement(paragraph, word_tag("r"))
    result = ElementTree.SubElement(result_run, word_tag("t"))
    result.text = "1"
    end_run = ElementTree.SubElement(paragraph, word_tag("r"))
    end = ElementTree.SubElement(end_run, word_tag("fldChar"))
    set_word_value(end, "fldCharType", "end")
    return ElementTree.tostring(footer, encoding="utf-8", xml_declaration=True)


def finalize_docx(docx_path: Path) -> None:
    """Add book-style sections, page numbers, and a real Word footer."""
    with zipfile.ZipFile(docx_path, "r") as archive:
        members = {info.filename: (info, archive.read(info.filename)) for info in archive.infolist()}

    document_info, document_data = members["word/document.xml"]
    document = ElementTree.fromstring(document_data)
    body = document.find(word_tag("body"))
    if body is None:
        raise BuildError("DOCX body not found")

    children = list(body)
    first_heading = None
    for index, child in enumerate(children):
        if child.tag != word_tag("p"):
            continue
        style = child.find(f"{word_tag('pPr')}/{word_tag('pStyle')}")
        if style is not None and style.get(word_tag("val")) == "Heading1":
            first_heading = index
            break
    if first_heading is None:
        raise BuildError("DOCX chapter headings not found")

    section_break_index = None
    for index in range(first_heading - 1, -1, -1):
        child = children[index]
        page_break = child.find(
            f".//{word_tag('br')}[@{word_tag('type')}='page']"
        )
        if page_break is not None:
            section_break_index = index
            body.remove(child)
            break
    if section_break_index is None:
        raise BuildError("DOCX front-matter page break not found")

    relationships_info, relationships_data = members[
        "word/_rels/document.xml.rels"
    ]
    relationships = ElementTree.fromstring(relationships_data)
    relationship_ids = {
        relationship.get("Id") for relationship in list(relationships)
    }
    footer_relationship = "rIdPageFooter"
    suffix = 1
    while footer_relationship in relationship_ids:
        footer_relationship = f"rIdPageFooter{suffix}"
        suffix += 1
    ElementTree.SubElement(
        relationships,
        relationship_tag("Relationship"),
        {
            "Id": footer_relationship,
            "Type": f"{OFFICE_RELATIONSHIPS}/footer",
            "Target": "footer1.xml",
        },
    )

    front_paragraph = ElementTree.Element(word_tag("p"))
    front_properties = ElementTree.SubElement(front_paragraph, word_tag("pPr"))
    front_section = ElementTree.SubElement(front_properties, word_tag("sectPr"))
    add_page_layout(
        front_section,
        footer_relationship,
        "lowerRoman",
        1,
        next_page=True,
        hide_first_page_number=True,
    )
    body.insert(section_break_index, front_paragraph)

    main_section = body.find(word_tag("sectPr"))
    if main_section is None:
        raise BuildError("DOCX final section properties not found")
    for child in list(main_section):
        if child.tag in {
            word_tag("footerReference"),
            word_tag("pgSz"),
            word_tag("pgMar"),
            word_tag("pgNumType"),
            word_tag("titlePg"),
        }:
            main_section.remove(child)
    add_page_layout(main_section, footer_relationship, "decimal", 1)

    content_types_info, content_types_data = members["[Content_Types].xml"]
    content_types = ElementTree.fromstring(content_types_data)
    if not any(
        override.get("PartName") == "/word/footer1.xml"
        for override in content_types.findall(content_type_tag("Override"))
    ):
        ElementTree.SubElement(
            content_types,
            content_type_tag("Override"),
            {
                "PartName": "/word/footer1.xml",
                "ContentType": (
                    "application/vnd.openxmlformats-officedocument."
                    "wordprocessingml.footer+xml"
                ),
            },
        )

    members["word/document.xml"] = (
        document_info,
        ElementTree.tostring(document, encoding="utf-8", xml_declaration=True),
    )
    members["word/_rels/document.xml.rels"] = (
        relationships_info,
        ElementTree.tostring(
            relationships, encoding="utf-8", xml_declaration=True
        ),
    )
    members["[Content_Types].xml"] = (
        content_types_info,
        ElementTree.tostring(
            content_types, encoding="utf-8", xml_declaration=True
        ),
    )

    temporary_doc = docx_path.with_suffix(".finalized.docx")
    with zipfile.ZipFile(temporary_doc, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for info, data in members.values():
            archive.writestr(info, data)
        archive.writestr("word/footer1.xml", page_number_footer())
    os.replace(temporary_doc, docx_path)


class BuildError(RuntimeError):
    """A user-facing build error."""


def discover_sources() -> List[Path]:
    if not BOOK_TEX.is_file():
        raise BuildError(f"book driver not found: {BOOK_TEX}")
    if not COMMON_TEX.is_file():
        raise BuildError(f"shared LaTeX file not found: {COMMON_TEX}")

    book_text = BOOK_TEX.read_text(encoding="utf-8")
    uncommented = "\n".join(line.split("%", 1)[0] for line in book_text.splitlines())
    sources: List[Path] = []
    seen = set()
    for relative_name in SOURCE_INPUT_RE.findall(uncommented):
        relative_path = Path(relative_name)
        if relative_path.suffix != ".tex":
            relative_path = relative_path.with_suffix(".tex")
        source = ROOT / relative_path
        if source in seen:
            raise BuildError(f"duplicate chapter input in {BOOK_TEX.name}: {relative_path}")
        if not source.is_file():
            raise BuildError(f"chapter source not found: {relative_path}")
        seen.add(source)
        sources.append(source)

    if not sources:
        raise BuildError(f"no src/odisea chapter inputs found in {BOOK_TEX.name}")
    return sources


def require_tool(name: str) -> str:
    executable = shutil.which(name)
    if executable is None:
        raise BuildError(f"required command not found on PATH: {name}")
    return executable


def tex_environment() -> dict[str, str]:
    environment = os.environ.copy()
    if "TEXMFVAR" not in environment:
        cache_dir = Path(tempfile.gettempdir()) / "leerlaodisea-texmf-var"
        cache_dir.mkdir(parents=True, exist_ok=True)
        environment["TEXMFVAR"] = str(cache_dir)
    existing_inputs = environment.get("TEXINPUTS", "")
    environment["TEXINPUTS"] = f"{ROOT}//{os.pathsep}{existing_inputs}"
    return environment


def run_command(
    command: Sequence[str],
    environment: dict[str, str] | None = None,
    working_directory: Path = ROOT,
) -> None:
    completed = subprocess.run(
        command,
        cwd=str(working_directory),
        env=environment,
        text=True,
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if completed.returncode != 0:
        output = completed.stdout.rstrip()
        message = f"command failed ({completed.returncode}): {shlex.join(command)}"
        if output:
            message = f"{message}\n\n{output}"
        raise BuildError(message)


def show_dry_run(sources: Sequence[Path], build_docx: bool) -> None:
    print(f"Book driver: {BOOK_TEX.relative_to(ROOT)}")
    print("Chapter order:")
    for source in sources:
        print(f"  {source.relative_to(ROOT)}")
    print(f"PDF:  {PDF_OUTPUT.name}")
    if build_docx:
        print(f"DOCX: {DOCX_OUTPUT.name}")
    print("All intermediate files will be built in a temporary directory.")


def build_book(sources: Sequence[Path], build_docx: bool) -> None:
    latexmk = require_tool("latexmk")
    pandoc = require_tool("pandoc") if build_docx else None

    with tempfile.TemporaryDirectory(
        prefix=".compile_book_build_", dir=str(ROOT)
    ) as temporary_dir:
        staging_dir = Path(temporary_dir)
        staged_pdf = staging_dir / PDF_OUTPUT.name
        print(f"Compiling {BOOK_TEX.name} to PDF")
        run_command(
            [
                latexmk,
                "-lualatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                "-file-line-error",
                f"-outdir={staging_dir}",
                "-jobname=odisea_book",
                str(BOOK_TEX),
            ],
            tex_environment(),
            staging_dir,
        )
        if not staged_pdf.is_file():
            raise BuildError(f"latexmk did not create {staged_pdf.name}")

        if build_docx:
            staged_docx = staging_dir / DOCX_OUTPUT.name
            pandoc_macros = staging_dir / "pandoc_book_macros.tex"
            pandoc_filter = staging_dir / "pandoc_book_structure.lua"
            frontmatter_break = staging_dir / "pandoc_frontmatter_break.xml"
            reference_doc = staging_dir / "pandoc_reference.docx"
            pandoc_macros.write_text(PANDOC_CHAPTER_MACRO, encoding="utf-8")
            pandoc_filter.write_text(PANDOC_STRUCTURE_FILTER, encoding="utf-8")
            frontmatter_break.write_text(PANDOC_PAGE_BREAK, encoding="utf-8")
            run_command(
                [
                    pandoc,
                    "--output",
                    str(reference_doc),
                    "--print-default-data-file",
                    "reference.docx",
                ]
            )
            customize_reference_doc(reference_doc)
            print("Converting root src/ chapters to DOCX")
            run_command(
                [
                    pandoc,
                    str(COMMON_TEX),
                    str(pandoc_macros),
                    *(str(source) for source in sources),
                    "--from=latex",
                    "--to=docx",
                    "--toc",
                    "--toc-depth=1",
                    "--lua-filter",
                    str(pandoc_filter),
                    "--include-before-body",
                    str(frontmatter_break),
                    "--reference-doc",
                    str(reference_doc),
                    "--metadata",
                    "title=Leer la Odisea en tiempos iletrados",
                    "--metadata",
                    "author=Juan José Gómez Cadenas",
                    "--metadata",
                    "toc-title=Índice",
                    "--output",
                    str(staged_docx),
                ]
            )
            if not staged_docx.is_file():
                raise BuildError(f"pandoc did not create {staged_docx.name}")
            finalize_docx(staged_docx)

        os.replace(staged_pdf, PDF_OUTPUT)
        if build_docx:
            os.replace(staged_docx, DOCX_OUTPUT)

    print(f"PDF:  {PDF_OUTPUT.name}")
    if build_docx:
        print(f"DOCX: {DOCX_OUTPUT.name}")


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build odisea_book.pdf from root src/."
    )
    parser.add_argument(
        "--docx",
        action="store_true",
        help="also generate odisea_book.docx",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="show chapter order and outputs without compiling",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        sources = discover_sources()
        if args.dry_run:
            show_dry_run(sources, args.docx)
        else:
            build_book(sources, args.docx)
        return 0
    except BuildError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("\nBuild interrupted; temporary files cleaned.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
