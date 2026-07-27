# SKILL.md 说明文档

## 什么是 SKILL.md？

SKILL.md 是 Anthropic 于 2025 年底推出、2026 年迅速普及的 **AI Agent 技能协议标准文件**。它本质上是一份结构化的 Markdown 文件，用于向 AI 编码助手注入特定领域的专业知识、工作流程和操作规范。

## 核心特点

### 1. 跨工具通用

一份 SKILL.md 能被 32+ 主流 AI Agent 工具自动读取（截至 2026 年 3 月），包括：

- Claude Code
- Cursor
- OpenAI Codex
- Gemini CLI
- JetBrains Junie
- AWS Kiro
- Block Goose
- 以及其他兼容工具

解决了长期以来 prompt 无法在不同 AI 编码工具间复用的问题。

### 2. 渐进式加载（Progressive Disclosure）

- 会话启动时：只读取 skill 的名称和简介（约 100 tokens）
- 匹配到具体任务时：加载完整的指令和参考文件
- 效果：100 个 skill 共存也不会撑爆上下文窗口

### 3. 官方标准

- 规范地址：`agentskills.io/specification`
- 发布方：Anthropic（2025-12-18）
- 校验工具：`skills-ref validate`

## 与 AGENTS.md 的区别

| 文件 | 作用 | 类比 |
|------|------|------|
| AGENTS.md | 描述项目本身的信息 | 项目 README for agents |
| SKILL.md | 描述 agent 怎么做某类工作 | 能力包 / 插件 |

两者互补：AGENTS.md 说"这个项目长什么样"，SKILL.md 说"agent 怎么干某类活"。

## 生态现状

### 官方仓库

- **anthropics/skills**（~128k stars）— 官方技能集合
  - 文档处理：pdf / docx / xlsx / pptx
  - 开发工具：web-artifacts-builder / mcp-builder
  - 测试：webapp-testing

### 社区热门

| 项目 | 说明 |
|------|------|
| obra/superpowers（~177k stars） | TDD、调试、代码审查等工作流框架 |
| nuwa-skill（~28k stars） | 将历史人物思维方式蒸馏为 SKILL.md |
| awesome-claude-skills（~57k stars） | 社区技能目录合集 |
| darwin-skill（~5k stars） | 自动优化 SKILL.md 的进化系统 |

## 安全注意事项

SKILL.md 本质上是可执行指令，拥有文件系统和 Shell 访问权限。Snyk 在 2026 年 2 月的审计中发现：

- 3984 个 skill 中 36% 存在至少一个安全缺陷
- 13.4% 存在严重问题
- 76 个被确认包含恶意载荷（凭据窃取、后门、数据外泄）

建议：安装前阅读 SKILL.md 内容，来源不明的不使用。

## 总结

SKILL.md 是 2026 年 AI 开发工具生态中最重要的标准化进展之一。它比 MCP 知名度低，但渗透率更高——写一份 skill，32+ 工具都能读。正在成为 AI Agent 时代的"配置文件标准"。
