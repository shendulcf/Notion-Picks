# Notion Skills 收集

**简体中文** | [English](notion-skills.en.md)

Skill 是写给 AI Agent 的操作指南，通常放在 `SKILL.md` 及配套文件里。它可以教 Agent 调用命令行工具（CLI），也可以通过 MCP 连接服务。装好 Skill 后，还需要准备它用到的工具和账号。

[返回 README](../README.md#notion-skills)

- [OpenAI Notion 插件](#openai-notion-插件)
- [社区 Skills（非官方）](#社区-skills非官方)
- [Clipno CLI 配套 Skill](#clipno-cli-配套-skill)
- [使用与收录说明](#使用与收录说明)

## OpenAI Notion 插件

[openai/plugins 的 Notion 插件](https://github.com/openai/plugins/tree/main/plugins/notion)包含下面四个 Skills。使用前，需要在支持该插件的客户端中连接并授权 Notion。

| Skill | 适用场景 | 主要用途 |
| :---- | :---- | :---- |
| [notion-knowledge-capture](https://github.com/openai/plugins/tree/main/plugins/notion/skills/notion-knowledge-capture) | 知识沉淀 | 将对话和笔记整理为 Notion Wiki、操作指南、FAQ 或决策记录，并关联已有页面。 |
| [notion-meeting-intelligence](https://github.com/openai/plugins/tree/main/plugins/notion/skills/notion-meeting-intelligence) | 会议准备 | 结合 Notion 中的背景资料，整理议程、会前阅读材料和待决策事项。 |
| [notion-research-documentation](https://github.com/openai/plugins/tree/main/plugins/notion/skills/notion-research-documentation) | 研究与文档 | 检索多个 Notion 来源，汇总为带有引用的简报、对比分析或研究报告。 |
| [notion-spec-to-implementation](https://github.com/openai/plugins/tree/main/plugins/notion/skills/notion-spec-to-implementation) | 需求落地 | 将 Notion 中的 PRD 或功能规格拆解为实施计划、任务和进度记录。 |

[openai/skills](https://github.com/openai/skills) 已标记弃用，新入口是 `openai/plugins`。上面的链接指向新目录；旧目录可供参考。安装时跟随[插件项目说明](https://github.com/openai/plugins#readme)和客户端文档，旧版 MCP 配置命令可能已经不适用。

## 社区 Skills（非官方）

下面是第三方维护的 Skills。客户端和依赖信息来自各自的项目文档，尚未逐一试用。

### [notion-automation](https://github.com/sickn33/antigravity-awesome-skills/tree/main/skills/notion-automation)

搜索及管理 Notion 页面、数据库、内容块和评论。

- 来源：sickn33/antigravity-awesome-skills
- 客户端与依赖：支持 Skills 与 MCP 的客户端；需连接 Rube MCP（Composio），并授权 Notion 连接。

### [notion-template-business](https://github.com/sickn33/antigravity-awesome-skills/tree/main/skills/notion-template-business)

Notion 模板的设计、定价、销售渠道和营销规划。

- 来源：sickn33/antigravity-awesome-skills；标注来源为 vibeship-spawner-skills
- 客户端与依赖：项目提供 Claude Code、Codex 等客户端的安装说明；属于策略指导，不要求连接 Notion MCP。

### [clipno](https://github.com/EwingYangs/clipno-cli/tree/main/skills/clipno)

指导 Agent 调用 Clipno CLI，将链接保存到 Notion，或提取网页内容。

- 来源：EwingYangs/clipno-cli
- 客户端与依赖：项目明确提供 Claude Code Skill 用法；其他客户端按其 Skills 支持情况选择。需要 Node.js >= 18、Clipno CLI 或 npx，以及 Clipno 登录；保存还需关联 Notion。

前两个 Skill 的安装方法见[社区项目说明](https://github.com/sickn33/antigravity-awesome-skills#readme)。`notion-automation` 需要 Rube MCP；`notion-template-business` 提供设计和销售建议，不负责读写 Notion 数据。

## Clipno CLI 配套 Skill

- [项目仓库](https://github.com/EwingYangs/clipno-cli) · [官网](https://clipno.app)
- [Skill 原文](https://github.com/EwingYangs/clipno-cli/blob/main/skills/clipno/SKILL.md)
- 分类：第三方网页剪藏工具，同时提供 CLI 与 Agent Skill。通过 Clipno 服务执行，不需要 Notion MCP。

### 安装 Skill

在支持 Skills 的客户端环境中运行，按提示选择安装位置：

```bash
npx skills add EwingYangs/clipno-cli
```

这一步只安装 Skill。`clipno` CLI 和账号授权仍需单独准备。项目 README 也列出了 Claude Code 插件市场和手动复制的安装方法。

### 使用 CLI

需要 Node.js >= 18。全局安装后登录，并验证登录状态：

```bash
npm i -g clipno
clipno login
clipno whoami
```

保存链接前，在 [Clipno 的 Notion 设置](https://clipno.app/dashboard/notion)中关联工作区。以下命令中的 URL 请替换为实际链接：

```bash
# 保存到已关联的 Notion 数据库
clipno save https://example.com --json

# 仅提取网页内容，不写入 Notion
clipno extract https://example.com --markdown
```

也可以使用 `npx clipno` 代替全局安装后的 `clipno` 命令。Skill 原文使用 `npx -y clipno@latest` 作为 CLI 未安装时的替代方式。

`extract` 只需要 Clipno 登录，不用关联 Notion 工作区。`save` 还支持标签、备注、标题、转录、OCR 和 AI 摘要。增强内容有时会稍后出现在页面上，并受账号设置和配额影响；具体额度请看官网。

## 使用与收录说明

- 准备连接时先看对应项目：OpenAI 插件使用 Notion 集成，社区自动化 Skill 用 Rube MCP，Clipno 用自己的 CLI 和服务；模板经营 Skill 则提供设计与销售建议。
- 安装后核对工具可用性和授权范围；安装 Skill、连接服务、授予页面或数据库访问权限是不同步骤。
- 新条目应提供项目及 `SKILL.md` 原始链接、维护者、用途、适用客户端、运行时与服务依赖，以及安装和授权说明。第三方收集仓库中的条目应注明所在仓库和其声明的上游来源。
- 这些介绍来自项目说明和可读取的 Skill 文件。尚未安装或运行工具，授权、提取效果和 Notion 写入也还没测试。

资料查阅于 2026-11-09。安装方法、目录和套餐可能变化，使用时请再看一眼原项目的说明。
