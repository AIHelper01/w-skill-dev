---
name: w-ppt-lecture-script
description: Create or revise a slide-by-slide English teaching script from PPT/PPTX materials, delivered as editable Word documents with a full screenshot of each original slide, complete source wording preserved in bold, Chinese module headings, natural spoken English, semantic teaching order, selective technical explanations, and source-coverage/visual QA. Use when asked to 生成讲解稿、英文讲稿、逐页授课解说稿、PPT截图配套Word讲稿、保留原文加粗、原文串联为主, or to revise an existing lecture script to this style.
metadata:
  version: "3.1.0"
---

# PPT → Word English Lecture Script (原文为主，串联为辅)

## Goal
Generate **editable .docx teaching notes** for the exact provided presentation, not a PPT-text dump and not a loose summary. Each slide starts with a **full, unaltered screenshot of that slide**, followed by **Chinese organizational headings** and **spoken English narration**. Preserve **all meaningful source wording in the spoken/explained content, with the explicit repeated-contents exception below** and make reproduced source text **bold**. Use brief natural transitions and explanations to connect that source text into a teachable sequence. The balance is **source content first, linking second**.

## Required inputs
- User-supplied finalized PowerPoint file(s) (.pptx preferred) and, when available, an example lecture script .docx that establishes the user's format.
- If an existing teaching-script Word file is supplied, use it as the layout and voice benchmark while treating the **latest PPT** as the authority for content.
- Work with all slides in PPT order, including cover, section dividers, tables, figures, setup steps, and conclusions. If the PPT explicitly marks a slide for deletion, omit only as explicitly requested.

## Non-negotiable priorities
1. **Faithful source coverage**: every meaningful editable source text item must be represented in the corresponding slide's Word narration, not hidden solely inside the embedded screenshot. Preserve the original English wording when expressing original text. Original sentences, definitions, points, command names, parameters, captions, labels, and conclusions must not silently disappear or be rewritten into different sentences. For diagrams, account for key legible text and flow labels, adding a guided explanation.
2. **Source text bold**: source wording reproduced verbatim in the Word prose must be bold. For long sentences, bold the *entire original sentence or original segment*; original lists/steps may be separate bold units woven into spoken sentences. Newly authored transitions and explanatory sentences remain normal weight. Do not bold non-source explanatory sentences simply to fill space.
3. **A real lecture**: not a raw list, transcription, or a second pasted-original-text section. Introduce each module naturally, weave the bold original into the narrative, then explain just enough to make it understandable. Avoid duplication, filler, and repetitive “This slide shows...”. Keep language short, natural, and easy to read aloud for an international classroom.
4. **Semantic sequencing**: identify knowledge modules and their relationships before writing. Finish one module before moving to the next. Visual position is a cue, not the governing rule. Keep headings, products, numbers, labels, illustrations and explanations belonging to one module together even when they occupy different heights. Chinese is for headings / brief presenter notes only; all spoken prose is English. Follow the specialized routing rules below.
5. **Slide screenshot**: one complete, readable PPT slide screenshot per logical slide entry. Never substitute a crop, missing image placeholder, or an unrelated illustration. Screenshot comes before narration.
6. **Exact tech material**: preserve code blocks, commands, API fields, numbers, quoted phrases and product names literally (code in monospace, with surrounding original explanation bold). Never invent unavailable features. Distinguish PPT's claims from verified current facts; unless the user asks for research, do not silently rewrite the source.
7. **Delivery**: one editable Word document per source deck by default, in original order. Place images *inside the Word document* (no missing external image dependency). Use consistent styles, readable typography, and logical paragraph breaks. It is fine and expected that some slides need multiple Word pages; do not force one-slide-per-Word-page if it makes text too small or clips content.

## Teaching design rules (V3.0)

### Contents pages
- First contents page: introduce the course, then read each original chapter title in bold in order. Add one or two simple English sentences explaining what learners will study. For key chapters, add why the topic matters. For comparison chapters, explicitly say what approaches will be compared. For product chapters, name representative products when supplied by the user or supported by the deck; explain practical value without unsupported popularity claims.
- Optional chapters: retain `(optional)` and say “This is an optional part of today's course, so I will only give a brief introduction.” Do not skip or overdevelop them.
- Repeated contents page used as a section divider: briefly connect the previous topic, introduce the highlighted current chapter title and what comes next. Do not reread inactive chapters; their text is retained in the screenshot and may be recorded as an intentional coverage exception. Verify which chapter is active from the slide, never guess.

### Semantic reading order
Before drafting, inspect the complete slide image and source text, identify the slide type, map each module and its constituent items, and choose a reading route. Do not rely on extraction order, shape insertion order, or global x/y sorting. Follow explicit user-approved routes over defaults.

### Text–visual pairing and interleaving
Before drafting a slide that contains both explanatory text and substantive visuals, create a slide-local pairing map:

| Text or concept module | Related visual region | Relationship | Narration position |
|---|---|---|---|
| Definition, claim, step, or example | Diagram, screenshot, chart, table, or callout | Explains, compares, proves, continues, or shows the result | Immediately before or after the related source text |

Use the map to write in the pattern `source idea → related visual path → short takeaway → next module`.

- Finish one text–visual pair before starting the next. Do not explain all text first and collect all image explanations at the end.
- Keep the complete slide screenshot once at the beginning. Pairing controls the spoken order; it does not require cropping or repeating the screenshot.
- Use a dedicated diagram heading only when the visual is an independent knowledge module. Never add a catch-all `图片解读` section merely because a slide contains images.
- In revisions, move useful visual explanation into its related module, remove the old generic tail block, and delete any duplicated wording.
- A mixed slide might require this route: definition → related upper figure → reason or implication → process steps → related lower loop → summary. The route follows knowledge relationships, not a default “all text, then all images” sequence.

| Slide type | Default teaching route |
|---|---|
| Multi-column / cards | Left to right, one complete knowledge module at a time; title → representative example → short callouts → detailed explanation when the diagram supports that relationship. A larger explanation box may be above the small boxes yet still be explained after them. |
| Timeline | Earliest to latest; time → stage → representative technologies → representative applications → brief explanation. Never separate all dates from their technologies. |
| Capability hierarchy | Basic to advanced when teaching progression; may be bottom to top. Pair every number with its own label and explanation. |
| Flow / loop | Follow arrows and actual execution sequence; start at the task/input and complete one loop. Explain each action and what happens next. |
| Architecture | Overall purpose → components by layer or data/control flow → relationships → key takeaway. |
| Comparison | Complete each compared object or each meaningful comparison dimension; explicitly summarize differences. |
| Table | Group by row or column according to comparison purpose; keep each value with its correct header. |
| Software / code | Explain purpose → actual operation order → exact commands/settings → expected result; never invent a UI control or output. |
| Case study | Context → problem → action/permission → result → lesson, following the source. |

Complete a module before introducing the next. Do not mechanically generate “top/left/middle/right/bottom” sections when they break semantic units. Use meaningful Chinese headings such as `第二阶段：2022 — Algorithm-led`.

### Spoken English and selective enrichment
- Use short, natural sentences suitable for an international technical classroom. Prefer use, help, show, improve, complete, find, choose. Avoid unnecessarily formal vocabulary; retain precise technical terminology. Example: “The Agent identified the problem, asked for permission, and took action.” Use “looked into” instead if the intended meaning is investigation rather than finding the cause.
- On the first meaningful occurrence of a technical abbreviation, give its expansion or short form when it helps learners: “ReAct stands for Reasoning and Acting.” “Support Vector Machines, or SVM for short, were widely used at that time.” Do not invent expansions or repeat them every slide. Preserve user-approved wording and add accurate context only.
- Explain why a technology matters, its historical role, or how it differs from another approach in one short sentence when helpful. Use qualified factual wording (e.g. “one of the most widely used” rather than an unsupported “the best”). Use examples from the slide or user-approved examples; mark hypothetical examples as such. Do not silently update the source or fabricate product claims.
- For key concepts or actions, explain each separately in the same order as the source rather than compressing them into one dense paragraph. Example: HIRE IT → DIRECT IT → APPROVE IT → STOP IT; explain each, then emphasize human control.
- Add concise natural connections that express cause, contrast, progression or purpose. Do not insert generic filler before every box, and do not turn an introduction into a full lesson. Use emphasis and additional depth selectively on the course's actual focal topics.
- In revision tasks, retain the user's previously approved sentences and unaffected sections. Apply later explicit corrections only to the relevant portions. Do not regenerate approved content from scratch. If prior wording is unavailable, say so instead of pretending to reproduce it verbatim.
- Use regular weight for added narration, including newly added acronym expansions and examples, unless explicitly requested otherwise. Preserve source wording in bold; don't mix up source and supplemental claims.

Read `references/teaching-patterns.md` for concrete routing and narration examples, and `references/quality-checklist.md` for final acceptance criteria.

## End-to-end workflow

### Step 1 — Inspect source and benchmark
- Open the finalized deck; enumerate all slide numbers and titles.
- Extract all text from *every* editable shape, text box, table cell, grouped shape, speaker note when explicitly requested, and relevant chart labels; do not assume `shape.text` alone captures tables/group shapes.
- Review the screenshot of each slide for text inside raster images or diagrams, heading hierarchy, and intended narration order. When embedded text cannot be confidently read, flag it rather than guess or pretend it was reproduced.
- If an example Word is supplied, inspect heading structure, screenshot placement, bolding, sentence rhythm, and slide transitions. Match the quality and style, not only its outline.

### Step 2 — Design a slide-by-slide script plan
- Pick module headings based on what is visually *actually* on that page. Avoid boilerplate headings that do not match the slide.
- Assign every substantive source item to its correct module and slide; repeated labels may be spoken once per slide when the relationship remains clear. Keep the slide title and subtitles visible and represented. Tables: first state the headings, then explain the rows in reasonable groups, using source wording for each item. Diagrams: talk through their direction/flow and include labels. Commands: present exact commands with a short explanation of what they do and when to run them.
- For every slide containing both text and visuals, complete the text–visual pairing map before drafting. Every substantive visual must have a named related module and an intended narration position.
- Use concise English linking lines where they help; no mandatory filler before every chunk. Add explanatory lines only when needed. Source text is the center of attention; do not over-expand simple pages.

### Step 3 — Write the actual English lecture
For each slide write:

`Slide NN — [original slide title]`

`[full slide screenshot]`

`原 PPT · Slide NN`

`页面衔接：[previous topic] → [current topic]`
Short and natural spoken transition in English.

`左侧/右侧/顶部/底部：[PPT's actual module]`
Natural spoken lead-in (regular). Then **exact original PPT sentences/fragments in bold**, followed by a short plain-English elaboration where useful. Continue in the planned semantic teaching order. A presenter must be able to read the text as speech, without reading metadata or explanatory drafting notes.

`页面总结与过渡`
Two or three clear sentences that capture the key message and lead naturally to the next slide; avoid needlessly repeating all source lines.

If there are substantial original English items (including tables) that sound unnatural as direct speech, connect them with short prompts (“Let's look at the three modes.”) and retain each original label/phrase in **bold**, making them easy to read in sequence. Do **not** append a separate full-page bold source dump to satisfy coverage.

Interleave related text and visuals while writing. After explaining a source concept, immediately guide the audience through the figure, screenshot, table, or diagram that supports it. Do not finish the slide's textual narration and then append a generic page-level image explanation.

### Step 4 — Build Word with screenshots
- Render the supplied PPT to images at a readable size, using the *exact latest upload*.
- Create .docx using Word paragraphs and runs; original source runs bold, added bridging text normal; Chinese module labels as headings. Put one slide image at the start of each slide section.
- Respect natural slide-length variation. Intro and chapter-divider slides may be short; multi-module technical slides require more substantial narration.

### Step 5 — Verify before delivery
- Run `scripts/check_source_coverage.py --pptx INPUT.pptx --docx OUTPUT.docx --json REPORT.json` as a **heuristic** omission scan (not a proof of full fidelity; shape order and image text need manual review). Resolve or justify all substantive misses.
- Visually compare every Word slide section with the corresponding slide image: **all required original text represented and bold**, semantic sequencing correct, no duplicate-source dump, narrator's explanation subordinate to source.
- Audit every substantive visual against the text–visual pairing map. If a visual can only be located in a generic image-reading block at the end, the slide is not complete: move that explanation beside its related concept and remove duplicates.
- Render the final `.docx` to PNG/PDF using the document skill's `render_docx.py`. Review pages for image fit, line breaks, font substitution, orphaned headings, cut-off screenshots, empty gaps, and overflow. Fix and re-render.
- Verify slide count/sequence, original coverage and bold formatting within each slide (not globally), module association and teaching route, Word embedded screenshot count, and chapter transitions. Review the actual spoken flow aloud or simulate reading it. Record intentional exceptions, including inactive repeated directory entries, and preserve user-approved wording. If anything cannot be read or preserved, explicitly report the limitation.

## Failures to avoid
- Short generic summaries instead of module-by-module explanation.
- Copying all original PPT text into one bold block after an unrelated short narration.
- A verbose explanation that crowds out the source's own sentences.
- Claiming that a screenshot alone counts as source-text coverage.
- Missing original table cells, footnotes, chart labels, step numbers, or callout captions.
- Rephrasing source wording while claiming it is an exact original quotation.
- Explaining all text first and all visuals later when clear text–visual relationships exist.
- Keeping an integrated visual explanation and a duplicate catch-all `图片解读` tail block.
- Splitting screenshot from its slide heading without careful pagination.
- Forcing 37 slides into exactly 37 Word pages when text needs more space.

## Package files
- `references/teaching-patterns.md` — semantic routes, contents, and approved-style examples.
- `references/quality-checklist.md` — acceptance checks and practical definition of complete.
- `examples/one-slide-example.md` — sample showing source-first narration with natural links.
- `scripts/check_source_coverage.py` — basic source/docx match report; does not replace visual inspection.
