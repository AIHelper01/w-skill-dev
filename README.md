# w-skill-dev

自研 Codex Skills 的开发与分发仓库。

A development and distribution repository for custom Codex Skills.

[中文](#中文) | [English](#english)

## 中文

### 项目简介

本仓库用于集中开发和维护自研 Skill：

- `w-skill/`：本仓库开发的 Skill，每个 Skill 使用独立目录。
- `third-party/`：从外部来源下载并保留上游信息的第三方 Skill。
- `SKILL.md`：每个 Skill 的必需入口，包含 YAML frontmatter 和使用说明。
- `scripts/`、`references/`、`examples/`、`assets/`：按需存放脚本、参考规则、示例和输出资源。

### 目录结构

```text
w-skill-dev/
├── w-skill/
│   └── w-<name>/
│       ├── SKILL.md
│       ├── scripts/       # 可选
│       ├── references/    # 可选
│       ├── examples/      # 可选
│       └── assets/        # 可选
└── third-party/
    └── <skill-name>/
        └── SKILL.md
```

自研 Skill 目录统一使用 `w-` 前缀。`SKILL.md` frontmatter 中的 `name` 应与目录名一致。第三方 Skill 应保留原始分发元数据，并在 README 中登记来源和版本。

### 自研 Skills

| Skill | 功能 |
|---|---|
| [w-weather](w-skill/w-weather/SKILL.md) | 免费天气查询。优先使用 wttr.in，Open-Meteo 作为备用，无需 API key。 |
| [w-ppt-lecture-script](w-skill/w-ppt-lecture-script/SKILL.md) | 把 PPT/PPTX 转换为可编辑的逐页 Word 英文讲稿；保留完整幻灯片截图、加粗原文，并按视觉顺序使用简单英语讲解流程图、架构图、时间线、表格和界面截图。也支持修订已有讲稿。 |
| [w-arxiv-paper-brief](w-skill/w-arxiv-paper-brief/SKILL.md) | 将 arXiv 论文整理为忠于原文的中文精简解读，包含核心思路、实测收益、首版日期和少量原文插图。 |
| [w-interactive-demo](w-skill/w-interactive-demo/SKILL.md) | 从网页提取指定交互演示并离线打包，或新建可调参数、图表与指标联动的教学演示。 |
| [w-mcp-server-builder](w-skill/w-mcp-server-builder/SKILL.md) | 构建、改进或审查 Python FastMCP 服务，重点覆盖 Streamable HTTP、安全防护、优雅退出和文档。 |
| [w-md2nb](w-skill/w-md2nb/SKILL.md) | 将 Markdown 教程目录批量转换为 Jupyter Notebook，保留清晰的单元格结构和本地图片资源。 |

### 安装到 Codex

安装全部自研 Skill：

```bash
for skill in \
  w-weather \
  w-ppt-lecture-script \
  w-arxiv-paper-brief \
  w-interactive-demo \
  w-mcp-server-builder \
  w-md2nb; do
  cp -R "w-skill/$skill" "${CODEX_HOME:-$HOME/.codex}/skills/$skill"
done
```

安装单个 Skill：

```bash
cp -R "w-skill/w-ppt-lecture-script" \
  "${CODEX_HOME:-$HOME/.codex}/skills/w-ppt-lecture-script"
```

也可以使用 Codex 的 Skill 安装工具直接从 GitHub 仓库路径安装。

### 开发约定

1. 在 `w-skill/<name>/` 中修改源文件。
2. 保持 `SKILL.md` 的 `name`、目录名和 README 登记一致。
3. 只添加任务真正需要的脚本、参考文件和示例。
4. 使用 Skill Creator 的 `quick_validate.py` 验证 Skill。
5. 测试通过后再提交仓库，并同步到本机安装目录。

`~/.codex/skills/` 是安装副本；本仓库应作为自研 Skill 的源代码来源。

### 第三方 Skills

当前没有收录第三方 Skill。新增时放入 `third-party/<skill-name>/`，保留上游许可证和分发元数据，并在本节登记来源与版本。

---

## English

### Overview

This repository is the source of truth for custom Codex Skills:

- `w-skill/` contains Skills developed and maintained in this repository.
- `third-party/` is reserved for externally sourced Skills with upstream metadata preserved.
- `SKILL.md` is the required entry point for every Skill. It contains YAML frontmatter and operating instructions.
- `scripts/`, `references/`, `examples/`, and `assets/` are optional supporting resources.

### Repository layout

```text
w-skill-dev/
├── w-skill/
│   └── w-<name>/
│       ├── SKILL.md
│       ├── scripts/       # optional
│       ├── references/    # optional
│       ├── examples/      # optional
│       └── assets/        # optional
└── third-party/
    └── <skill-name>/
        └── SKILL.md
```

Custom Skill directories use the `w-` prefix. The `name` in the `SKILL.md` frontmatter should match the directory name. Third-party Skills should retain their original distribution metadata, source, version, and license information.

### Custom Skills

| Skill | Purpose |
|---|---|
| [w-weather](w-skill/w-weather/SKILL.md) | Get weather information without an API key, using wttr.in first and Open-Meteo as a fallback. |
| [w-ppt-lecture-script](w-skill/w-ppt-lecture-script/SKILL.md) | Turn a PPT/PPTX into an editable, slide-by-slide English Word lecture script. It embeds each full slide, preserves source wording in bold, and explains flowcharts, architectures, timelines, tables, and interface screenshots in simple spoken English and visual order. It can also revise an existing script. |
| [w-arxiv-paper-brief](w-skill/w-arxiv-paper-brief/SKILL.md) | Create a concise Chinese brief of an arXiv paper with its core idea, measured benefits, first-submission date, and selected original figures. |
| [w-interactive-demo](w-skill/w-interactive-demo/SKILL.md) | Extract a selected interactive web demo for offline use or build a new teaching demo with linked controls, charts, and metrics. |
| [w-mcp-server-builder](w-skill/w-mcp-server-builder/SKILL.md) | Build, improve, or review Python FastMCP servers, with emphasis on Streamable HTTP, security controls, graceful shutdown, and documentation. |
| [w-md2nb](w-skill/w-md2nb/SKILL.md) | Convert Markdown tutorial directories into Jupyter notebooks while preserving readable cell boundaries and local image assets. |

### Install in Codex

Install all custom Skills:

```bash
for skill in \
  w-weather \
  w-ppt-lecture-script \
  w-arxiv-paper-brief \
  w-interactive-demo \
  w-mcp-server-builder \
  w-md2nb; do
  cp -R "w-skill/$skill" "${CODEX_HOME:-$HOME/.codex}/skills/$skill"
done
```

Install one Skill:

```bash
cp -R "w-skill/w-ppt-lecture-script" \
  "${CODEX_HOME:-$HOME/.codex}/skills/w-ppt-lecture-script"
```

You can also use the Codex Skill installer with a GitHub repository path.

### Development workflow

1. Edit the source under `w-skill/<name>/`.
2. Keep the directory name, `SKILL.md` frontmatter name, and README entry consistent.
3. Add only the scripts, references, examples, and assets required by the workflow.
4. Validate the Skill with Skill Creator's `quick_validate.py`.
5. Commit the tested source, then synchronize it to the local installation directory.

Treat `~/.codex/skills/` as an installed copy. This repository should remain the source of truth for custom Skills.

### Third-party Skills

No third-party Skills are currently included. Add future packages under `third-party/<skill-name>/`, preserve upstream license and distribution metadata, and record the source and version in this section.
