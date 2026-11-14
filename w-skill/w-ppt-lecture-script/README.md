# w-ppt-lecture-script V3.1

用于将英文技术 PPT 转成可直接朗读的 Word 授课讲稿。保留原名，便于覆盖旧版本。

## 安装
解压 ZIP，将整个 `w-ppt-lecture-script/` 文件夹放入你的 Agent 已配置的 Skills 搜索目录，替换旧版本。Codex 可使用 `$w-ppt-lecture-script` 调用（以实际环境支持的路径和语法为准）。此包不会自动安装到你的设备或账户。

## 调用示例
```
使用 $w-ppt-lecture-script 为附件 PPT 生成完整英文授课讲稿，输出 Word。
保留每页原图、原文加粗，按知识模块与教学逻辑逐页解读。
```

## 版本变化
- 先建立“文字／概念模块 ↔ 相关图片区域”的配对关系，再交错生成讲稿；不再先讲完文字、最后统一追加图片解读。
- 一个页面有多组文字与图示时，完成一组再进入下一组；整合后删除重复的 `图片解读` 尾块。
- 首次目录逐章介绍、重点价值、选学范围；重复目录仅引出当前章节。
- 按语义模块规划讲解顺序，支持纵向模块、时间线、能力层级、流程与架构。
- 专业术语首现补全称/简称，适当补充历史地位、技术差异和实际例子。
- 简单自然的英语；保留已确认的讲稿内容。
- 覆盖检查脚本从全局匹配改为逐页匹配；仍需人工核对模块顺序、截图和例外项。

## 文件
- `SKILL.md` 主规则
- `references/teaching-patterns.md` 教学路线与回归示例
- `references/quality-checklist.md` 质量检查
- `examples/one-slide-example.md` 单页讲稿示例
- `scripts/check_source_coverage.py` 原文覆盖启发式检查（依赖 python-pptx、python-docx）
