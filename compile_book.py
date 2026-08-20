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
from pathlib import Path
from typing import List, Sequence


ROOT = Path(__file__).resolve().parent
BOOK_TEX = ROOT / "odisea_book.tex"
COMMON_TEX = ROOT / "odisea_common.tex"
PDF_OUTPUT = ROOT / "odisea_book.pdf"
DOCX_OUTPUT = ROOT / "odisea_book.docx"

SOURCE_INPUT_RE = re.compile(r"\\input\{(src/odisea[^{}]+)\}")
PANDOC_CHAPTER_MACRO = r"\newcommand{\odiseachapter}[2]{\chapter{#2}}" + "\n"


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


def run_command(command: Sequence[str]) -> None:
    completed = subprocess.run(
        command,
        cwd=str(ROOT),
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
                "-pdf",
                "-interaction=nonstopmode",
                "-halt-on-error",
                "-file-line-error",
                f"-outdir={staging_dir}",
                "-jobname=odisea_book",
                str(BOOK_TEX),
            ]
        )
        if not staged_pdf.is_file():
            raise BuildError(f"latexmk did not create {staged_pdf.name}")

        if build_docx:
            staged_docx = staging_dir / DOCX_OUTPUT.name
            pandoc_macros = staging_dir / "pandoc_book_macros.tex"
            pandoc_macros.write_text(PANDOC_CHAPTER_MACRO, encoding="utf-8")
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
                    "--metadata",
                    "title=Leer la Odisea en tiempos iletrados",
                    "--metadata",
                    "author=Juan José Gómez Cadenas",
                    "--output",
                    str(staged_docx),
                ]
            )
            if not staged_docx.is_file():
                raise BuildError(f"pandoc did not create {staged_docx.name}")

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
