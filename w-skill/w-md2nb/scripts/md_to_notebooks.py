#!/usr/bin/env python3
"""Convert Markdown tutorials into Jupyter notebooks and copy local assets."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path


FENCE_RE = re.compile(r"^(\s*)(```+|~~~+)\s*([A-Za-z0-9_+.#-]*)?.*$")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+")
MARKDOWN_IMAGE_LINE_RE = re.compile(r"^\s+(!\[[^\]]*\]\([^)]+\)\s*)$")
HTML_IMAGE_LINE_RE = re.compile(r"^\s+(<img\b[^>]*>\s*)$", re.IGNORECASE)


def split_markdown_blocks(lines: list[str]) -> list[str]:
    """Split prose so each paragraph or heading becomes one markdown cell."""
    blocks: list[str] = []
    current: list[str] = []

    def flush() -> None:
        nonlocal current
        while current and not current[0].strip():
            current.pop(0)
        while current and not current[-1].strip():
            current.pop()
        if current:
            blocks.append(normalize_markdown_block("".join(current)))
        current = []

    for line in lines:
        if not line.strip():
            flush()
            continue

        if HEADING_RE.match(line):
            flush()
            blocks.append(line.rstrip("\n"))
            continue

        current.append(line)

    flush()
    return blocks


def normalize_markdown_block(source: str) -> str:
    """Remove indentation from standalone image lines so notebooks render them as images."""
    normalized_lines: list[str] = []
    for line in source.splitlines(keepends=True):
        newline = "\n" if line.endswith("\n") else ""
        content = line[:-1] if newline else line
        markdown_match = MARKDOWN_IMAGE_LINE_RE.match(content)
        html_match = HTML_IMAGE_LINE_RE.match(content)
        if markdown_match:
            normalized_lines.append(markdown_match.group(1) + newline)
        elif html_match:
            normalized_lines.append(html_match.group(1) + newline)
        else:
            normalized_lines.append(line)
    return "".join(normalized_lines)


def make_markdown_cell(source: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": source.splitlines(keepends=True),
    }


def make_code_cell(source: str, language: str) -> dict:
    metadata = {}
    if language:
        metadata["language"] = language
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": metadata,
        "outputs": [],
        "source": source.splitlines(keepends=True),
    }


def markdown_to_cells(markdown: str) -> list[dict]:
    cells: list[dict] = []
    md_buffer: list[str] = []
    code_buffer: list[str] = []
    in_code = False
    fence_marker = ""
    fence_indent = ""
    code_language = ""

    def flush_markdown() -> None:
        nonlocal md_buffer
        for block in split_markdown_blocks(md_buffer):
            cells.append(make_markdown_cell(block))
        md_buffer = []

    for line in markdown.splitlines(keepends=True):
        fence_match = FENCE_RE.match(line)

        if in_code:
            if fence_match and line.lstrip().startswith(fence_marker):
                cells.append(make_code_cell("".join(code_buffer).rstrip("\n"), code_language))
                code_buffer = []
                in_code = False
                fence_marker = ""
                fence_indent = ""
                code_language = ""
            else:
                if fence_indent and line.startswith(fence_indent):
                    code_buffer.append(line[len(fence_indent) :])
                else:
                    code_buffer.append(line)
            continue

        if fence_match:
            flush_markdown()
            fence_indent = fence_match.group(1)
            fence_marker = fence_match.group(2)
            code_language = fence_match.group(3) or ""
            code_buffer = []
            in_code = True
            continue

        md_buffer.append(line)

    if in_code:
        md_buffer.append(f"```{code_language}\n")
        md_buffer.extend(code_buffer)

    flush_markdown()
    return cells


def make_notebook(cells: list[dict]) -> dict:
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "pygments_lexer": "ipython3",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def iter_markdown_files(source_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in source_dir.rglob("*.md")
        if ".ipynb_checkpoints" not in path.parts
    )


def iter_asset_files(source_dir: Path) -> list[Path]:
    ignored_suffixes = {".md", ".html"}
    return sorted(
        path
        for path in source_dir.rglob("*")
        if path.is_file()
        and ".ipynb_checkpoints" not in path.parts
        and path.suffix.lower() not in ignored_suffixes
    )


def copy_assets(source_dir: Path, output_dir: Path) -> int:
    copied = 0
    for source_file in iter_asset_files(source_dir):
        relative = source_file.relative_to(source_dir)
        output_file = output_dir / relative
        output_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_file, output_file)
        copied += 1
    return copied


def convert_file(source_file: Path, source_dir: Path, output_dir: Path) -> tuple[Path, int]:
    relative = source_file.relative_to(source_dir)
    output_file = output_dir / relative.with_suffix(".ipynb")
    output_file.parent.mkdir(parents=True, exist_ok=True)

    markdown = source_file.read_text(encoding="utf-8")
    cells = markdown_to_cells(markdown)
    notebook = make_notebook(cells)
    output_file.write_text(
        json.dumps(notebook, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return output_file, len(cells)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", default="docs", type=Path)
    parser.add_argument("--output-dir", default="notebooks", type=Path)
    parser.add_argument("--no-copy-assets", action="store_true")
    args = parser.parse_args()

    source_dir = args.source_dir
    output_dir = args.output_dir
    converted: list[tuple[Path, int]] = []

    for source_file in iter_markdown_files(source_dir):
        converted.append(convert_file(source_file, source_dir, output_dir))

    print(f"Converted {len(converted)} Markdown files to {output_dir}")
    for output_file, cell_count in converted:
        print(f"{output_file} ({cell_count} cells)")

    if not args.no_copy_assets:
        asset_count = copy_assets(source_dir, output_dir)
        print(f"Copied {asset_count} asset files to {output_dir}")


if __name__ == "__main__":
    main()
