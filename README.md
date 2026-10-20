# w-skill-dev — Skill 开发基地

与 `mcpserver-dev` 平行的技能（Skill）开发目录。
自研 skill 放 `w-skill/`，下载的第三方 skill 源码放 `third-party/`。

## 目录约定

```
w-skill-dev/
├── w-skill/          # 自研 skill，每个 skill 一个子目录
│   └── w-<name>/SKILL.md
└── third-party/      # 公网下载的第三方 skill（非本仓库开发）
    └── <skill-name>/SKILL.md
```

- 自研 skill 目录以 `w-` 前缀命名；`SKILL.md` frontmatter 的 `name` 默认与目录名一致，
  历史 skill 若已有对外使用的名字则保留原名（见下表备注）。
- `SKILL.md` 是必需入口：YAML frontmatter（`name` / `description` / 可选
  `homepage`、`metadata`）+ 正文使用说明。
- 有脚本、模板等附属资源时，放在同一 skill 目录内（如 `scripts/`、`assets/`）。
- 第三方 skill 保留原始 `_meta.json` 等分发元数据，并在下表登记来源与版本。

## 自研 skill（w-skill/）

| Skill | 说明 |
|---|---|
| [w-weather](w-skill/w-weather/SKILL.md) | 免费天气查询：wttr.in 为主、Open-Meteo 兜底，无需 API key，仅依赖 `curl`。在 ClawHub [`@steipete/weather`](https://docs.clawhub.ai/steipete/skills/weather) v1.0.0 基础上整理，已去除上游分发元数据 |
| [w-slide-lecturer](w-skill/w-slide-lecturer/SKILL.md) | PPT/PDF 逐模块英文授课讲稿：原文提取、英文讲稿、中文指图提示与截图打包，按需产出 Word。含 `scripts/`（extract/build/validate）与 `references/` |
| [w-arxiv-paper-brief](w-skill/w-arxiv-paper-brief/SKILL.md) | 把 arXiv 论文写成忠于原文的中文精简解读，含核心思路、实测收益、首版日期与少量原文插图 |
| [w-interactive-demo](w-skill/w-interactive-demo/SKILL.md) | 从网页链接提取指定交互演示并离线打包；或按浅色教学风格新建可调参数、图表与指标联动的演示工具 |
| [w-mcp-server-builder](w-skill/w-mcp-server-builder/SKILL.md) | 构建/改进/审查 Python FastMCP（MCP）服务，重点 Streamable HTTP、Host/Origin 防护、优雅退出与文档 |
| [w-md2nb](w-skill/w-md2nb/SKILL.md) | 把 Markdown 教程目录批量转成 Jupyter Notebook，保留可读单元格边界与本地图片渲染，附转换脚本 |

所有 skill 的 frontmatter `name` 与目录名一致。
`agents/openai.yaml` 是 Codex/Agent 界面元数据（展示名与默认提示词），一并维护。

> 沿革：`w-slide-lecturer`、`w-arxiv-paper-brief` 原为独立仓库（已删除，内容全量迁入本仓库）；
> `w-interactive-demo`、`w-mcp-server-builder`、`w-md2nb` 原先只存在于本机
> `~/.codex/skills/`，现以本仓库为唯一来源；`w-slide-lecturer` 的 skill name
> 原为 `slide-teaching-guide`，已统一为 `w-slide-lecturer`。

## 第三方 skill（third-party/）

暂无。下载后按 `third-party/<skill-name>/` 放置并在此登记。

官方 ClawHub 安装方式示例：`npx clawhub@latest install weather`。

## 安装到 Codex

把 skill 目录复制到 `$CODEX_HOME/skills/`（默认 `~/.codex/skills/`）即可被识别：

```bash
for s in w-weather w-slide-lecturer w-arxiv-paper-brief \
         w-interactive-demo w-mcp-server-builder w-md2nb; do
  cp -R "w-skill/$s" "$HOME/.codex/skills/$s"
done
```

更新单个 skill 同理；`~/.codex/skills/` 是安装副本，改动请先落在本仓库再复制过去。

自研 skill 建议直接在 `w-skill/<name>/` 开发调试，验证后再复制或安装。
