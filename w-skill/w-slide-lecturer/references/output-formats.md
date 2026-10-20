# Output formats

## Default one-slide script
- `### Slide XX — Title`
- `### 页面衔接：[topic] → [topic]` — short English bridge
- Sequential spatial sections: `### 左上 ...`, `### 中间 ...`, `### 右侧 ...`, `### 底部 ...`
- Key slide-original text in **bold**; speaker bridges/explanations in plain English
- `### 页面总结与过渡` — one-sentence takeaway and next slide when known

## Optional A1 / A2 / B / C full extraction
When requested by the user, produce FOUR sections for each slide:
- **A1 PPT original text:** group by visible module; preserve verbatim wording and order, repair only extraction-related broken line wraps.
- **A2 Diagram/image text:** grouped by the same original modules; capture image labels, formulas, arrows, examples (indicate illegible words).
- **B English Teaching Script:** module-by-module spoken script, same module order as A1/A2, retain original words in bold with minimal additions.
- **C 中文指图提示:** concise guidance on which visual area to point at and when; do not substitute for the script.

## Multi-slide compiled file
Use chronological slide numbers as the user currently has them, keep one complete slide section at a time, and optionally add a compact slide-level completeness checklist. Never silently drop slides.
