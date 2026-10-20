# w-skill-dev — Skill 开发基地

与 `mcpserver-dev` 平行的技能（Skill）开发目录。
自研 skill 放 `w-skill/`，下载的第三方 skill 源码放 `third-party/`。

## 目录约定

```
w-skill-dev/
├── w-skill/          # 自研 skill，每个 skill 一个子目录
│   └── <skill-name>/SKILL.md
└── third-party/      # 公网下载的第三方 skill（非本仓库开发）
    └── <skill-name>/SKILL.md
```

- 每个 skill 一个目录，目录名即 skill 的 `name`（frontmatter 中的 `name`）。
- `SKILL.md` 是必需入口：YAML frontmatter（`name` / `description` / 可选
  `homepage`、`metadata`）+ 正文使用说明。
- 有脚本、模板等附属资源时，放在同一 skill 目录内（如 `scripts/`、`assets/`）。
- 第三方 skill 保留原始 `_meta.json` 等文件，并在下表登记来源与版本；
  官方安装方式：`npx clawhub@latest install weather`。

## 已收录

| Skill | 位置 | 来源 | 说明 |
|---|---|---|---|
| weather | `third-party/weather/` | ClawHub [`@steipete/weather`](https://docs.clawhub.ai/steipete/skills/weather) v1.0.0（Peter Steinberger） | 免费天气查询：wttr.in 为主、Open-Meteo 兜底，无需 API key，仅依赖 `curl` |

## 安装到 Codex

把 skill 目录复制到 `$CODEX_HOME/skills/`（默认 `~/.codex/skills/`）即可被识别：

```bash
cp -R third-party/weather ~/.codex/skills/weather
```

自研 skill 建议直接在 `w-skill/<name>/` 开发调试，验证后再复制或安装。
