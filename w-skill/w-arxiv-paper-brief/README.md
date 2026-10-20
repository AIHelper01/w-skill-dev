# w-arxiv-paper-brief

An Agent Skill that turns an arXiv paper into a concise, source-grounded Chinese Markdown brief with selected original figures.

## What it produces

Each brief contains paper metadata, `核心观点`, `带来的收益`, selected figures, and source links. Existing output folders are preserved by creating `-v2.0`, `-v3.0`, and later versions.

## Requirements

The host agent must be able to access arXiv, download and inspect PDFs, render and crop PDF pages, and write local files.

## Install

Clone the repository into your agent's skills directory, or copy the repository folder there. For Codex on Windows, the default personal location is:

```text
C:\Users\<you>\.codex\skills\w-arxiv-paper-brief
```

Restart or begin a new agent turn after installation.

## Use

Invoke the skill with an arXiv URL or paper ID:

```text
Use $w-arxiv-paper-brief to explain https://arxiv.org/abs/1706.03762
```

## Files

- `SKILL.md` — portable Agent Skills instructions
- `agents/openai.yaml` — optional OpenAI/Codex interface metadata

## License

MIT. Extracted paper figures remain subject to the source paper's license and attribution requirements.
