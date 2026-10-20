---
name: w-slide-lecturer
description: Create faithful, natural, easy-to-deliver English lecture scripts from training PPT slides, screenshots, or extracted slide text. Preserve all original modules and substantive content, teach in visual reading order, add concise transitions and grounded explanations, and maintain cross-slide narrative and a recurring case study. Use for slide-by-slide teaching scripts, revisions, and Chinese instructor cues.
---

# w-slide-lecturer — Slide-faithful English teaching scripts

## Mission
Turn a training slide (PPT/PPTX, screenshot, or extracted content) into an **English script suitable for speaking aloud**. Maintain the source's facts, module organization, and teaching intent. Add just enough scaffolding to make the ideas teachable; do not replace the slide with a new essay.

## Non-negotiable priorities
1. **Source fidelity first.** Do not silently omit, compress, merge, reorder, or paraphrase away original claims, list entries, examples, labels, figure details, numerical values, formulas, or caveats. Keep meaningful original English wording intact; correct only clear grammar or unnatural phrasing. The length should normally remain comparable to the substantive source material plus short explanations.
2. **One visual module at a time.** Follow the actual spatial reading order (typically top/left → middle → bottom/right, but adapt to the slide). Finish each module's original words, diagram, equation, and example before moving to another. Never hop back and forth between modules merely to group related ideas.
3. **Short, speakable English.** Prefer common vocabulary, short sentences, clear transitions and standard technical terms. Avoid artificial academic prose, hype, and repetitive meta-comments such as “the slide says”.
4. **Bold original PPT text.** In the teaching script, render key verbatim source lines in **bold**. Put added spoken connective/explanatory language in ordinary text; preserve the distinction. Do not bold invented text as if it were original.
5. **Continuity.** Begin with a natural bridge from the previous slide and end with a factual, short lead-in to the next slide when its topic is known. Reuse one recurring example where useful (default only if supplied by the course: Shanghai trip planning), while never claiming illustrative weather, prices or bookings are real data.
6. **Accuracy and uncertainty.** Technical terms must be correct. If the slide makes an overstrong assertion, retain and clearly attribute its wording to the slide while adding a concise qualification if necessary. Never invent figures, sources, product timelines, URLs, citations, or unseen text. Distinguish source content from optional domain commentary. Verify externally only if asked or if a time-sensitive claim materially requires checking; do not replace the provided source with web content.
7. **Teacher-friendly Chinese structure.** Use short Chinese section headers such as `页面衔接`, `左上 ...`, `右侧 ...`, `底部 ...`, while keeping the teaching narration in English. No Chinese inside the spoken script unless requested.

## Workflow

### 1. Read and map the slide
- Inspect ALL visible text, figure labels, arrows, charts, tables, footnotes, and any user-provided notes.
- When PPTX text is extractable, use it, but still inspect the visual layout to recover module order and image text.
- If a slide screenshot is low-resolution, mark uncertain words instead of filling them in by guesswork.
- Create an internal ordered module map: `module name | placement | source text | diagram/formula/figure details | intended teaching point`.
- For multiple slides, keep their actual slide numbers (including deletions or renumbering the user explicitly specified).

### 2. Preserve then explain each module
For every module, in the slide's visual order:
1. Introduce it with one natural spoken transition: “First, let's look at ...”, “Now let's follow the diagram ...”.
2. Reproduce the key original content, especially all original list items, terms, numbers, and examples, in **bold**, keeping its order and meaning.
3. Explain with one to three clear, easy-to-speak sentences only where explanation helps.
4. When a diagram is present, guide the teacher to point through the exact nodes/arrows in sequence. For tables, read rows by their original order; for equations, name variables and explain their purpose without altering math.
5. Do not interrupt this module to talk about another part of the slide.

### 3. Bridge the narrative
- Opening: connect to previous page's main learning outcome without repeating the entire previous lecture.
- Recurrent example: connect only where pedagogically relevant. For the Shanghai trip, distinguish planning (next step), action (API/tool), memory (current budget vs lasting preference), harness (execution and controls), safety (sandbox/permissions).
- Closing: summarize the **one central idea** and introduce the known next subject; for chapter divider and thank-you slides, use a shorter structure.
- If previous/next slide is unavailable, avoid guessing its contents; give a general bridge or omit.

### 4. Adapt depth to slide type
- **Content-heavy explanatory slides:** cover all substantive content in visual order.
- **Architecture slides:** identify roles and trace one representative request/response, keep conceptual vs official architecture clear.
- **Case-study slides:** preserve steps, sample outputs and constraints; connect each step to the core concept.
- **Chapter Contents slides:** short recap, transition, main question, upcoming chapter; do not narrate every item unless the user requests it.
- **Product timelines:** if the user requests milestones only, select only user-approved milestones; keep slide-provided dates attributed and avoid implying the illustrated curve is a measured benchmark.
- **Closing slides:** concise course recap and one memorable takeaway.
- **User asks for a shorter version:** compress connective explanations first, not original slide facts; if requested to skip details, respect the explicitly named items.

### 5. Deliver in a predictable format
Default response:
```
### Slide XX — [original slide title]

### 页面衔接：[previous] → [current]
[short English introduction]

### [方位] [Original module title]
[brief teacher pointer]

**[Slide's original wording or faithful minimally corrected excerpt]**
[short spoken explanation]
...

### 页面总结与过渡
[one key idea + one transition]
```
When the user gives a screenshot of both the slide and a draft transcript, use that transcript as source too and improve *without deleting original content*. If explicitly asked for A1/A2/B/C, use the extended extraction output in `references/output-formats.md`.

## Special technical guidance
- Function Calling = model expresses structured tool requests; the host/runtime executes them.
- MCP = protocol enabling standardized application–server tool discovery and calls; it does not itself supply data.
- Skill = reusable instructions and optional scripts/references; tools or runtimes perform actions. Metadata → SKILL.md instructions → resources accessed as needed.
- Short-term memory is broader than a context window; long-term memory is not necessarily a vector database.
- Harness = broader system coordinating model, tools, context, state, execution, approvals and feedback; a sandbox helps isolate execution, not guarantee security alone.
- ReAct / Plan-and-Solve / Reflection are useful patterns and may be combined, not mutually exclusive rules.
- Mark hypothetical weather forecasts, prices, and reservations as examples; do not claim live availability without tools.

## Final quality gate (mandatory, internal)
- Did I cover every source module, row, stage, list item and important figure/formula without omissions?
- Does the lecture follow the exact *visual* module order? Are modules completed before moving on?
- Did I preserve source wording and highlight slide-original statements distinctly?
- Is the English understandable, idiomatic and easy to say aloud, with standard terminology?
- Are transitions coherent and cases consistent with prior slides?
- Did I refrain from inventing slide text, facts, timestamps, numerical results or future slides?
- Did I avoid overexplaining a divider or summary page?
- Are source-driven statements separated from newly added analogies, clarifications and qualifications?

See `references/style-guide.md`, `references/output-formats.md`, and `examples/sample-slide.md` for more.
