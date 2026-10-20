---
name: w-md2nb
description: Convert Markdown tutorial directories into Jupyter notebooks while preserving readable cell boundaries and local image/static asset rendering. Use when Codex needs to batch convert docs/**/*.md or similar Markdown course material into .ipynb files, split headings and paragraphs into separate markdown cells, convert fenced code blocks into code cells, copy images/assets alongside notebooks, and validate notebook structure plus local image references.
---

# W Md2nb

## Workflow

Use the bundled script for deterministic conversion:

```bash
SKILL_DIR="${CODEX_HOME:-$HOME/.codex}/skills/w-md2nb"
python3 "$SKILL_DIR/scripts/md_to_notebooks.py" --source-dir docs --output-dir notebooks
```

Adjust `--source-dir` and `--output-dir` for other projects. Run from the repository root unless the user specifies absolute paths.

## Conversion Rules

- Convert every `*.md` under the source directory into a matching `.ipynb` path under the output directory.
- Skip `.ipynb_checkpoints`.
- Split headings into their own markdown cells so multiple headings are not merged.
- Split normal prose by blank lines so each paragraph becomes one markdown cell.
- Remove leading whitespace from standalone Markdown image lines and HTML `<img>` lines so Jupyter renders them as images instead of indented text/code.
- Convert fenced code blocks using backticks or tildes into code cells.
- Recognize indented fenced code blocks inside Markdown lists and remove only the common fence indentation from the code cell.
- Copy non-Markdown, non-HTML source files into the output tree so local images and static assets keep working.
- Preserve remote image URLs as-is.

## Validation

After conversion, run checks before reporting completion:

1. Load all generated `.ipynb` files with `json.loads`.
2. Count notebooks, total cells, markdown cells, and code cells.
3. Ensure no markdown cell contains more than one heading.
4. Ensure fenced code markers did not remain in markdown cells.
5. Parse Markdown image syntax and HTML `<img src="...">` references, ignore remote/data URLs, and verify local paths exist relative to each notebook.

If validation fails because source Markdown has broken local image paths, prefer narrow repair logic in the conversion script over broad text rewrites. Preserve the original Markdown unless the user explicitly asks to edit it.

## Script

The reusable converter lives at:

```text
scripts/md_to_notebooks.py
```

If using this skill outside this machine, copy that script into the target workspace or run it from the skill path. The script has no third-party Python dependencies.
