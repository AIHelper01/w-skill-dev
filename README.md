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

| Skill | skill name | 说明 |
|---|---|---|
| [w-weather](w-skill/w-weather/SKILL.md) | `w-weather` | 免费天气查询：wttr.in 为主、Open-Meteo 兜底，无需 API key，仅依赖 `curl`。在 ClawHub [`@steipete/weather`](https://docs.clawhub.ai/steipete/skills/weather) v1.0.0 基础上整理，已去除上游分发元数据 |
| [w-slide-lecturer](w-skill/w-slide-lecturer/SKILL.md) | `slide-teaching-guide` | PPT/PDF 逐模块英文授课讲稿：原文提取、英文讲稿、中文指图提示与截图打包，可按需产出 Word。含 `scripts/`（extract/build/validate）与 `references/`。目录名为仓库名 `w-slide-lecturer`，skill name 沿用历史名 |
| [w-arxiv-paper-brief](w-skill/w-arxiv-paper-brief/SKILL.md) | `w-arxiv-paper-brief` | 把 arXiv 论文写成忠于原文的中文精简解读，含核心思路、实测收益、首版日期与少量原文插图 |

三个 skill 原先各为独立仓库（`AIHelper01/w-slide-lecturer`、`AIHelper01/w-arxiv-paper-brief`），
已迁入本仓库统一管理；`agents/openai.yaml` 为 Codex/Agent 界面元数据，一并保留。

## 第三方 skill（third-party/）

暂无。下载后按 `third-party/<skill-name>/` 放置并在此登记。

官方 ClawHub 安装方式示例：`npx clawhub@latest install weather`。

## 安装到 Codex

把 skill 目录复制到 `$CODEX_HOME/skills/`（默认 `~/.codex/skills/`）即可被识别：

```bash
cp -R w-skill/w-weather            ~/.codex/skills/w-weather
cp -R w-skill/w-slide-lecturer     ~/.codex/skills/w-slide-lecturer
cp -R w-skill/w-arxiv-paper-brief  ~/.codex/skills/w-arxiv-paper-brief
```

自研 skill 建议直接在 `w-skill/<name>/` 开发调试，验证后再复制或安装。
