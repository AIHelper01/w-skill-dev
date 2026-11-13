---
name: w-ppt-lecture-script
description: Turn a PPT/PPTX into an editable slide-by-slide Word lecture script, or revise an existing script to match the slides. Use for PPT讲稿、英文讲解稿、逐页授课稿、PPT截图配套Word、图片或流程图解读. The output keeps the original slide screenshot, preserves source wording in bold, and adds simple spoken English in visual order.
---

# PPT to Word Lecture Script

## Task

Create or revise an editable `.docx` lecture script based on a PowerPoint deck.

The Word document is a teaching aid, not a slide transcript and not an independent essay. For every slide, it should let the instructor see the original slide and read a clear English explanation in the same order the audience sees the content.

The core balance is:

- the PPT supplies the facts, wording, labels, and visual structure;
- the script preserves that source material;
- short spoken English connects and explains it;
- Word provides the editable teaching format.

## Inputs and authority

Use the latest finalized PPT/PPTX as the content authority.

- If an existing lecture-script Word file is provided, preserve its layout, voice, slide order, screenshots, and unaffected text. Revise only the requested scope.
- If no PPT is available for a revision, readable full-slide screenshots embedded in the Word file may serve as the visual source. Do not guess unreadable text.
- Use a supplied example Word file as a style benchmark, not as a content source.
- Include all required slides in PPT order. Omit a slide only when the user explicitly asks.

## Required Word structure

Use this structure for each logical slide:

1. `Slide NN — [original slide title]`
2. one complete, readable screenshot of the original slide
3. `原 PPT · Slide NN`
4. `页面衔接` with a short English bridge from the previous slide
5. Chinese headings for the actual visual regions or modules on the slide
6. spoken English narration under those headings
7. `页面总结与过渡` with the key message and a natural lead to the next slide

Choose headings from the real layout, such as `左侧`, `右上`, `流程图`, `时间线`, or the module name. Do not force the same heading pattern onto every slide.

Simple cover, contents, divider, and closing slides may use a shorter structure. Dense technical slides may continue across multiple Word pages. Never shrink or clip content to force one slide onto one Word page.

## Source fidelity and formatting

Account for every meaningful source item outside the screenshot:

- title and subtitle;
- original sentences and bullet points;
- table headers and substantive cells;
- diagram labels, arrow labels, branches, captions, and conclusions;
- commands, code, filenames, API fields, parameters, numbers, quotations, and product names.

When original PPT wording appears in the narration, reproduce it exactly and make that source run **bold**. Keep newly written transitions and explanations in normal weight.

Do not silently paraphrase original wording and present it as source text. Do not paste all source text into a separate bold block merely to satisfy coverage. Weave each item into the module where it belongs.

Preserve technical material literally. Use monospace for code and commands where the Word format supports it. Do not invent features, facts, or labels that are not in the source. Unless the user requests research, explain the PPT rather than silently correcting or updating it.

## Spoken English

Write for an international classroom:

- use common words and short sentences;
- keep one main idea per sentence;
- preserve necessary technical terms, then explain them in simple language;
- write natural speech that an instructor can read aloud;
- avoid long abstract phrases, filler, and repeated formulas such as “This slide shows”;
- use examples only when they clarify the source and clearly remain additional explanation.

A useful pattern is: introduce the area, read or state the bold source item, explain it briefly, and connect it to the next area.

## Visual narration

Treat every substantive visual as content. Decorative images need no explanation.

Integrate the visual explanation into the relevant module. Do not append a generic “image interpretation” block after the page has already been explained.

The narration must follow the audience's eyes:

- finish one region before moving to the next;
- add a natural spoken bridge before changing regions;
- connect the final visual point to the page summary;
- avoid repeating text that the existing script already explains well.

Use the visual type to decide the path:

- **Flowchart or sequence:** start at the entry point, follow every meaningful arrow, explain decisions, branches, returns, errors, and stopping conditions.
- **Architecture:** identify the central or entry component, explain each main component, and follow the data, control, feedback, or execution connections between them.
- **Timeline:** move in the displayed direction, complete one milestone before the next, and explain what changes across time.
- **Comparison or table:** state the comparison dimensions, then complete one row or column at a time using the same criteria.
- **Chart:** identify the axes, series, values, or highlighted evidence and state what the audience should notice. Do not claim more than the chart supports.
- **Interface screenshot:** follow the real task order; point to the control, input, action, and visible result. Explain only controls relevant to the lesson.
- **Case trace or code example:** read from the starting condition through each step to the result; connect outputs from one step to inputs of the next.

For a visual revision, add only the missing explanation at the correct location. Preserve the rest of the slide section.

## Workflow

### 1. Inspect

- Enumerate slide numbers and titles.
- Extract editable text from shapes, grouped shapes, tables, charts, and notes when requested.
- Render and inspect every slide. Record substantive visuals, readable labels, visual order, and fine text that needs a larger view.
- Inspect any existing Word script for style, screenshot placement, heading levels, bolding, and speaking rhythm.

### 2. Plan

- Divide each slide by its actual visual regions or logical modules.
- Assign every source item to one location; avoid omission and duplication.
- Choose the visual path and the transition into and out of each region.
- Keep simple slides short and give complex diagrams enough space.

### 3. Write and build

- Write the narration in visual order using simple spoken English.
- Bold exact PPT source wording; keep connectors normal.
- Render the exact source slides and embed one full-slide screenshot at the start of each section.
- Build one editable Word document per source deck unless the user requests another grouping.

### 4. Verify

- Run `scripts/check_source_coverage.py --pptx INPUT.pptx --docx OUTPUT.docx --json REPORT.json` when the PPT is available. Treat the report as an omission hint, not proof of quality.
- Manually compare every slide with its Word section. Use [references/quality-checklist.md](references/quality-checklist.md).
- Confirm that visual narration is placed beside the relevant module and that the transitions make it sound like one continuous lecture.
- Render the final Word document to page images with the document workflow. Inspect every page for readable screenshots, correct fonts, bold source text, clean pagination, orphan headings, clipping, overlap, and large accidental gaps.
- Verify slide count, order, embedded image count, source coverage, and final file integrity. Report any unreadable or unverifiable source detail.

## Failure conditions

Do not deliver a result that:

- summarizes a complex slide in a few generic sentences;
- treats the embedded screenshot as sufficient source coverage;
- appends a mechanical visual-reading paragraph instead of integrating it;
- repeats the same generic transition on every slide;
- lists boxes without explaining their connections;
- misses table cells, captions, arrow labels, branches, errors, or stopping conditions;
- rewrites original source wording while presenting it as exact;
- separates a screenshot from its slide section or leaves external image dependencies;
- has not been rendered and visually inspected.

## Resources

- [references/quality-checklist.md](references/quality-checklist.md) — final content, teaching, visual, and Word checks.
- [examples/one-slide-example.md](examples/one-slide-example.md) — example of source-led narration with an integrated flowchart explanation.
- `scripts/check_source_coverage.py` — heuristic PPT-to-Word text coverage report.
