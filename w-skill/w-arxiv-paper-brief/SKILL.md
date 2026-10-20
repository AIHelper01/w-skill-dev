---
name: w-arxiv-paper-brief
description: "Create concise Chinese Markdown briefs for arXiv papers, covering core ideas, measured benefits, the first-submission date, and a small number of original figures. Use when a user provides an arXiv paper or URL and wants a source-grounded Chinese explanation."
---

# W Arxiv Paper Brief

Create a self-contained Chinese Markdown interpretation for the requested arXiv paper.

## Requirements

Use an environment that can access arXiv, download and inspect PDFs, render PDF pages, crop images, and write local files. If a required capability is unavailable, explain what is missing instead of producing an incomplete brief.

## Deliverable

Create the output at the workspace root:

```text
arXiv-<paper-id>/
├── arXiv-<paper-id>.md
└── assets/
    └── arXiv-<paper-id>-figure-<number>.png
```

Use relative image paths in the Markdown. If `arXiv-<paper-id>/` already exists, do not overwrite or reuse it. Create the next available versioned folder by appending `-v2.0`, then `-v3.0`, `-v4.0`, and so on. Treat the selected folder name as `<output-name>` and use it consistently for the Markdown file and figure filenames: `<output-name>/<output-name>.md` and `<output-name>/assets/<output-name>-figure-<number>.png`. When versioned folders already exist, inspect them and choose one greater than the highest existing whole-number major version.

## Content

- Start with the title, then put `## 来源` first. Include a compact source-list item with the paper citation and official abstract/PDF links.
- Directly below that list, put all metadata in one Markdown blockquote: `> **模型：** <模型名>   **模型厂家：** <开发机构>   **论文 ID：** arXiv:<id>   **论文名称：** <title>   **作者：** <authors>   **发布时间：** <first submission date>   **原文：** [arXiv](...)｜[PDF](...)`. When the paper clearly concerns an identifiable model and its developer, include the model and maker fields first; otherwise omit just those two fields. Use the official arXiv version history for the first-submission date.
- Write in Chinese. After the source and metadata block, use `## 核心观点` to explain what the paper changes and how it works, followed by `## 带来的收益` to explain measured gains, practical implications, and material boundaries. Place selected original figures under the section they support.
- Prefer concise explanation over a course-style survey. Preserve essential equations when central to the contribution. Use no other top-level sections, and do not repeat `## 来源` at the end.
- Include caveats only when they materially change how the paper's central claim should be understood.
- End with a compact takeaway in `## 带来的收益`; source links appear only in the opening `## 来源` section.

## Figures

- Inspect the PDF and select the fewest original figures that materially explain the contribution. Prefer one by default, but include multiple figures whenever each is needed to explain a distinct key mechanism, architectural stage, or indispensable result; do not omit a necessary figure merely to keep the count to one.
- Extract figures at readable resolution. Crop only after visually locating the full figure boundary; retain a small safety margin on all four sides, especially below plots, legends, arrows, and axis labels. Do not crop a figure merely to remove surrounding prose if that risks cutting a visual element. Crop out unrelated page text and partial captions; provide a Chinese caption and the original Figure number with a direct PDF-page source link.
- Name every image `<output-name>-figure-<number>.png` under `assets/`, using the same versioned or unversioned `<output-name>` selected for the folder.
- Preserve the original figure number and attribution. If the paper's license or access conditions do not permit redistributing a figure, link to the source instead of extracting it.

## Accuracy and verification

- Ground claims, formulas, figure numbers, and reported results in the paper PDF. Obtain the first-submission date from the official arXiv version history.
- Clearly label later work as subsequent background, and include it only when requested.
- Before delivery, verify that the Markdown file and all linked images exist, paths resolve relative to the Markdown file, and selected figures are readable. Visually inspect each final crop at its saved dimensions and confirm that no diagram component, chart edge, axis, label, legend, arrow, or intended caption is clipped; re-crop with more margin when uncertain.
