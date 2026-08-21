#!/usr/bin/env python3
"""Compile individual JD chapters to PDF, optionally also to DOCX."""

from __future__ import annotations

import argparse
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence


ROOT = Path(__file__).resolve().parent
REPOSITORY_ROOT = ROOT.parent
SRC_DIR = ROOT / "src"
PDF_DIR = ROOT / "pdf"
DOCX_DIR = ROOT / "docx"
COMMON_TEX = REPOSITORY_ROOT / "odisea_common.tex"
DRIVER_TEMPLATE = ROOT / "odisea_single_driver.tex"

SOURCE_RE = re.compile(r"^odisea(?P<number>[1-9][0-9]*)_(?P<slug>.+)\.tex$")
HEADING_RE = re.compile(
    r"^\s*\\odiseachapter\{(?P<part>[^{}]+)\}\{(?P<title>[^{}]+)\}",
    re.MULTILINE,
)


class BuildError(RuntimeError):
    """A user-facing build error."""


@dataclass(frozen=True)
class Chapter:
    number: int
    slug: str
    source: Path

    @property
    def short_name(self) -> str:
        return f"odisea{self.number}"

    @property
    def source_stem(self) -> str:
        return self.source.stem

    @property
    def legacy_driver_stem(self) -> str:
        return f"odisea{self.number}d_{self.slug}"

    @property
    def aliases(self) -> Sequence[str]:
        return (self.short_name, self.source_stem, self.legacy_driver_stem)

    @property
    def output_stem(self) -> str:
        return self.source_stem

    @property
    def relative_source_without_suffix(self) -> str:
        return self.source.relative_to(ROOT).with_suffix("").as_posix()


def discover_chapters() -> List[Chapter]:
    if not SRC_DIR.is_dir():
        raise BuildError(f"source directory not found: {SRC_DIR}")
    if not COMMON_TEX.is_file():
        raise BuildError(f"shared LaTeX file not found: {COMMON_TEX}")
    if not DRIVER_TEMPLATE.is_file():
        raise BuildError(f"driver template not found: {DRIVER_TEMPLATE}")

    chapters: List[Chapter] = []
    numbers: Dict[int, Path] = {}
    for source in sorted(SRC_DIR.glob("odisea*_*.tex")):
        match = SOURCE_RE.fullmatch(source.name)
        if not match:
            continue
        number = int(match.group("number"))
        if number in numbers:
            raise BuildError(
                f"chapter {number} is ambiguous: {numbers[number].name}, {source.name}"
            )
        numbers[number] = source
        chapters.append(Chapter(number, match.group("slug"), source))

    if not chapters:
        raise BuildError(f"no chapter sources found in {SRC_DIR}")
    return sorted(chapters, key=lambda chapter: chapter.number)


def normalize_selector(selector: str) -> str:
    if Path(selector).name != selector:
        raise BuildError("chapter selectors must be names, not paths")
    if selector.endswith(".tex"):
        selector = selector[:-4]
    return selector


def resolve_chapter(selector: str, chapters: Sequence[Chapter]) -> Chapter:
    normalized = normalize_selector(selector)
    aliases: Dict[str, Chapter] = {}
    for chapter in chapters:
        for alias in chapter.aliases:
            if alias in aliases:
                raise BuildError(f"ambiguous chapter alias: {alias}")
            aliases[alias] = chapter

    try:
        return aliases[normalized]
    except KeyError as exc:
        valid = ", ".join(chapter.short_name for chapter in chapters)
        raise BuildError(f"unknown chapter {selector!r}; valid short names: {valid}") from exc


def chapter_title(chapter: Chapter) -> str:
    text = chapter.source.read_text(encoding="utf-8")
    match = HEADING_RE.search(text)
    if not match:
        raise BuildError(
            f"{chapter.source.name} has no simple \\odiseachapter{{part}}{{title}} heading"
        )
    return (
        "Leer la Odisea en tiempos iletrados. "
        f"{match.group('part')}: {match.group('title')}"
    )


def wrapper_text(chapter: Chapter) -> str:
    return (
        f"\\def\\odiseacontent{{{chapter.relative_source_without_suffix}}}\n"
        "\\input{odisea_single_driver}\n"
    )


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
    return environment


def run_command(
    command: Sequence[str], environment: dict[str, str] | None = None
) -> None:
    completed = subprocess.run(
        command,
        cwd=str(ROOT),
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


def build_chapter(
    chapter: Chapter,
    staging_dir: Path,
    latexmk: str,
    pandoc: str | None,
) -> None:
    print(f"Compiling {chapter.short_name} ({chapter.source.name})")

    wrapper_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            prefix=".compile_jd_",
            suffix=".tex",
            dir=str(ROOT),
            delete=False,
        ) as wrapper:
            wrapper.write(wrapper_text(chapter))
            wrapper_path = Path(wrapper.name)

        run_command(
            [
                latexmk,
                "-lualatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                "-file-line-error",
                f"-outdir={staging_dir}",
                f"-jobname={chapter.output_stem}",
                str(wrapper_path),
            ],
            tex_environment(),
        )
    finally:
        if wrapper_path is not None:
            wrapper_path.unlink(missing_ok=True)

    pdf_path = staging_dir / f"{chapter.output_stem}.pdf"
    if not pdf_path.is_file():
        raise BuildError(f"latexmk did not create {pdf_path.name}")

    if pandoc is not None:
        docx_path = staging_dir / f"{chapter.output_stem}.docx"
        run_command(
            [
                pandoc,
                str(COMMON_TEX),
                str(chapter.source),
                "--from=latex",
                "--to=docx",
                "--metadata",
                f"title={chapter_title(chapter)}",
                "--metadata",
                "author=Juan José Gómez Cadenas",
                "--output",
                str(docx_path),
            ]
        )
        if not docx_path.is_file():
            raise BuildError(f"pandoc did not create {docx_path.name}")


def publish_outputs(
    chapters: Iterable[Chapter], staging_dir: Path, publish_docx: bool
) -> None:
    PDF_DIR.mkdir(exist_ok=True)
    if publish_docx:
        DOCX_DIR.mkdir(exist_ok=True)
    for chapter in chapters:
        staged_pdf = staging_dir / f"{chapter.output_stem}.pdf"
        os.replace(staged_pdf, PDF_DIR / staged_pdf.name)
        print(f"  PDF:  {PDF_DIR.relative_to(ROOT) / staged_pdf.name}")
        if publish_docx:
            staged_docx = staging_dir / f"{chapter.output_stem}.docx"
            os.replace(staged_docx, DOCX_DIR / staged_docx.name)
            print(f"  DOCX: {DOCX_DIR.relative_to(ROOT) / staged_docx.name}")


def show_chapters(chapters: Sequence[Chapter]) -> None:
    for chapter in chapters:
        print(
            f"{chapter.short_name:<9} "
            f"{chapter.source.relative_to(ROOT)} "
            f"(full name: {chapter.output_stem})"
        )


def show_dry_run(chapters: Sequence[Chapter], build_docx: bool) -> None:
    for chapter in chapters:
        print(f"{chapter.short_name}: {chapter.source.relative_to(ROOT)}")
        print("  temporary driver:")
        for line in wrapper_text(chapter).splitlines():
            print(f"    {line}")
        print(f"  PDF:  pdf/{chapter.output_stem}.pdf")
        if build_docx:
            print(f"  DOCX: docx/{chapter.output_stem}.docx")


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compile JD chapter sources to clean PDF outputs."
    )
    parser.add_argument(
        "chapter",
        nargs="?",
        help="short or full chapter name, for example odisea1 or odisea1d_nolan.tex",
    )
    parser.add_argument("--all", action="store_true", help="compile every chapter")
    parser.add_argument(
        "--docx",
        action="store_true",
        help="also generate DOCX output",
    )
    parser.add_argument("--list", action="store_true", help="list discovered chapters")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="show resolved inputs and outputs without compiling",
    )
    args = parser.parse_args(argv)

    if args.list:
        if args.chapter or args.all or args.dry_run or args.docx:
            parser.error(
                "--list cannot be combined with a chapter, --all, --dry-run, or --docx"
            )
    elif bool(args.chapter) == bool(args.all):
        parser.error("choose exactly one chapter or --all")
    return args


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        chapters = discover_chapters()
        if args.list:
            show_chapters(chapters)
            return 0

        selected = chapters if args.all else [resolve_chapter(args.chapter, chapters)]
        if args.dry_run:
            show_dry_run(selected, args.docx)
            return 0

        latexmk = require_tool("latexmk")
        pandoc = require_tool("pandoc") if args.docx else None
        PDF_DIR.mkdir(exist_ok=True)
        if args.docx:
            DOCX_DIR.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(
            prefix=".compile_jd_build_", dir=str(ROOT)
        ) as temporary_dir:
            staging_dir = Path(temporary_dir)
            for chapter in selected:
                build_chapter(chapter, staging_dir, latexmk, pandoc)
            publish_outputs(selected, staging_dir, args.docx)
        return 0
    except BuildError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("\nBuild interrupted; temporary files cleaned.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
