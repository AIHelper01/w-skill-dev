---
name: w-ppt-lecture-script
description: Create or revise a slide-by-slide English teaching script from PPT/PPTX materials, delivered as editable Word documents with a full screenshot of each original slide, complete source wording preserved in bold, Chinese module headings, English narration for substantive figures, natural transitions, and source-coverage/visual QA. Use when asked to 生成讲解稿、英文讲稿、逐页授课解说稿、PPT截图配套Word讲稿、保留原文加粗、原文串联为主, or to revise an existing lecture script to this style.
---

# PPT → Word English Lecture Script (原文为主，串联为辅)

## Goal
Generate **editable .docx teaching notes** for the exact provided presentation, not a PPT-text dump and not a loose summary. Each slide starts with a **full, unaltered screenshot of that slide**, followed by **Chinese organizational headings** and **spoken English narration**. Preserve **all source wording in the spoken/explained content** and make reproduced source text **bold**. Use brief natural transitions and explanations to connect that source text into a teachable sequence. The balance is **source content first, linking second**.

## Required inputs
- For a new script, user-supplied finalized PowerPoint file(s) (.pptx preferred) and, when available, an example lecture script .docx that establishes the user's format.
- If an existing teaching-script Word file is supplied, use it as the layout and voice benchmark while treating the **latest PPT** as the authority for content.
- For an image-only revision, use the existing Word file and the latest matching PPT when available. Readable embedded slide screenshots can serve as the visual source. Insert the missing narration at the relevant module or caption and revise only existing figure narration within scope. Preserve the rest of the wording, order, formatting, and screenshots.
- Work with all slides in PPT order, including cover, section dividers, tables, figures, setup steps, and conclusions. If the PPT explicitly marks a slide for deletion, omit only as explicitly requested.

## Non-negotiable priorities
1. **Faithful source coverage**: every meaningful editable source text item must be represented in the corresponding slide's Word narration, not hidden solely inside the embedded screenshot. Preserve the original English wording when expressing original text. Original sentences, definitions, points, command names, parameters, captions, labels, and conclusions must not silently disappear or be rewritten into different sentences. For diagrams, account for key legible text and flow labels, adding a guided explanation.
2. **Source text bold**: source wording reproduced verbatim in the Word prose must be bold. For long sentences, bold the *entire original sentence or original segment*; original lists/steps may be separate bold units woven into spoken sentences. Newly authored transitions and explanatory sentences remain normal weight. Do not bold non-source explanatory sentences simply to fill space.
3. **A real lecture**: not a raw list, transcription, or a second pasted-original-text section. Introduce each module naturally, weave the bold original into the narrative, then explain just enough to make it understandable. Avoid duplication, filler, and repetitive “This slide shows...”. Keep language short, natural, and easy to read aloud for an international classroom.
4. **Visual sequencing**: finish one area before moving to the next. E.g. 页面衔接 → 左侧：... → 右上：... → 右下：... → 底部：... → 页面总结与过渡. Chinese is for the headings / brief presenter notes only; all prose the instructor reads aloud is English.
5. **Slide screenshot**: one complete, readable PPT slide screenshot per logical slide entry. Never substitute a crop, missing image placeholder, or an unrelated illustration. Screenshot comes before narration.
6. **Exact tech material**: preserve code blocks, commands, API fields, numbers, quoted phrases and product names literally (code in monospace, with surrounding original explanation bold). Never invent unavailable features. Distinguish PPT's claims from verified current facts; unless the user asks for research, do not silently rewrite the source.
7. **Delivery**: one editable Word document per source deck by default, in original order. Place images *inside the Word document* (no missing external image dependency). Use consistent styles, readable typography, and logical paragraph breaks. It is fine and expected that some slides need multiple Word pages; do not force one-slide-per-Word-page if it makes text too small or clips content.

## End-to-end workflow

### Step 1 — Inspect source and benchmark
- Open the finalized deck; enumerate all slide numbers and titles.
- Extract all text from *every* editable shape, text box, table cell, grouped shape, speaker note when explicitly requested, and relevant chart labels; do not assume `shape.text` alone captures tables/group shapes.
- Inspect every rendered slide visually, including raster images and grouped drawings. For each substantive visual, note its slide, position, type, readable labels, and where it belongs in the narration. Use the original PPT or a larger render to check fine text when available. Flag unreadable details. Skip decorative imagery.
- If an example Word is supplied, inspect heading structure, screenshot placement, bolding, sentence rhythm, and slide transitions. Match the quality and style, not only its outline.

### Step 2 — Design a slide-by-slide script plan
- Pick module headings based on what is visually *actually* on that page. Avoid boilerplate headings that do not match the slide.
- Assign every source item to exactly one meaningful spot in the module order. Keep the slide title and subtitles visible and represented. Tables: first state the headings, then explain the rows in reasonable groups, using source wording for each item. Commands: present exact commands with a short explanation of what they do and when to run them.
- Place each visual's explanation under its existing module or next to its caption in the slide's reading order. Use readable labels, step names, and callouts verbatim in **bold**. Connect them with short, normal-weight spoken English that guides the audience's eyes. If the existing script already covers the visual, add only the missing part.
  - **Flowcharts and sequence diagrams:** start at the entry point and follow the arrows. Connect each meaningful step to the next and explain decision branches, returns, and loops where shown.
  - **Architecture diagrams:** name the main layers or components, briefly state what they do, and explain how they connect. Cover internal detail when it is needed to understand the slide.
  - **Charts, examples, and interface screenshots:** point to the relevant axis, series, comparison, highlighted control, or visible result. Reuse the figure's wording and explain what the audience should notice.
- Produce **one or two** concise English linking lines before each chunk and explanatory lines only when needed. Source text is the center of attention; do not over-expand simple pages.

### Step 3 — Write the actual English lecture
For each slide write:

`Slide NN — [original slide title]`

`[full slide screenshot]`

`原 PPT · Slide NN`

`页面衔接：[previous topic] → [current topic]`
Short and natural spoken transition in English.

`左侧/右侧/顶部/底部：[PPT's actual module]`
Natural spoken lead-in (regular). Then **exact original PPT sentences/fragments in bold**, followed by a short plain-English elaboration where useful. Continue in the page's visual order. A presenter must be able to read the text as speech, without reading metadata or explanatory drafting notes.

`页面总结与过渡`
Two or three clear sentences that capture the key message and lead naturally to the next slide; avoid needlessly repeating all source lines.

If there are substantial original English items (including tables) that sound unnatural as direct speech, connect them with short prompts (“Let's look at the three modes.”) and retain each original label/phrase in **bold**, making them easy to read in sequence. Do **not** append a separate full-page bold source dump to satisfy coverage.

### Step 4 — Build Word with screenshots
- Render the supplied PPT to images at a readable size, using the *exact latest upload*.
- Create .docx using Word paragraphs and runs; original source runs bold, added bridging text normal; Chinese module labels as headings. Put one slide image at the start of each slide section.
- Respect natural slide-length variation. Intro and chapter-divider slides may be short; multi-module technical slides require more substantial narration.

### Step 5 — Verify before delivery
- Run `scripts/check_source_coverage.py --pptx INPUT.pptx --docx OUTPUT.docx --json REPORT.json` as a **heuristic** omission scan (not a proof of full fidelity; shape order and image text need manual review). Resolve or justify all substantive misses.
- Compare each Word section with the slide and the visual notes from Step 1. Confirm that every substantive visual has an English explanation in the right module, exact labels are bold, and the narration follows the visible path or layout. An embedded screenshot, caption, or text-coverage scan alone cannot confirm this. Use the [acceptance checklist](references/quality-checklist.md).
- Render the final `.docx` to PNG/PDF using the document skill's `render_docx.py`. Review pages for image fit, line breaks, font substitution, orphaned headings, cut-off screenshots, empty gaps, and overflow. Fix and re-render.
- Verify slide count/sequence, original coverage, original bold formatting, Word embedded screenshot count, and chapter transitions. If anything cannot be read or preserved, explicitly report the limitation.

## Failures to avoid
- Short generic summaries instead of module-by-module explanation.
- Copying all original PPT text into one bold block after an unrelated short narration.
- A verbose explanation that crowds out the source's own sentences.
- Claiming that a screenshot alone counts as source-text coverage.
- Missing original table cells, footnotes, chart labels, step numbers, or callout captions.
- Rephrasing source wording while claiming it is an exact original quotation.
- Splitting screenshot from its slide heading without careful pagination.
- Forcing 37 slides into exactly 37 Word pages when text needs more space.

## Package files
- `references/quality-checklist.md` — acceptance checks and practical definition of complete.
- `examples/one-slide-example.md` — sample showing source-first narration with natural links.
- `scripts/check_source_coverage.py` — basic source/docx match report; does not replace visual inspection.
