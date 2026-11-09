# Notion Skills 收集

**简体中文** | [English](notion-skills.en.md)

收集可供 AI Agent 使用的 Notion 工作流程。Skill 通常由 `SKILL.md` 和配套资源组成；CLI 是执行命令的工具；MCP 是连接外部服务的协议。一个项目可以同时提供 CLI 和 Skill，安装 Skill 不代表已经安装工具或完成账号授权。

[返回 README](../README.md#notion-skills)

- [OpenAI Notion 插件](#openai-notion-插件)
- [社区 Skills（非官方）](#社区-skills非官方)
- [Clipno CLI 配套 Skill](#clipno-cli-配套-skill)
- [使用与收录说明](#使用与收录说明)

## OpenAI Notion 插件

来源：[openai/plugins 的 Notion 插件](https://github.com/openai/plugins/tree/main/plugins/notion)。插件包含以下四个 Skills，项目说明其通过已连接的 Notion 集成提供能力；使用时需在支持该插件的客户端完成 Notion 连接与授权。

| Skill | 适用场景 | 主要用途 |
| :---- | :---- | :---- |
| [notion-knowledge-capture](https://github.com/openai/plugins/tree/main/plugins/notion/skills/notion-knowledge-capture) | 知识沉淀 | 将对话和笔记整理为 Notion Wiki、操作指南、FAQ 或决策记录，并关联已有页面。 |
| [notion-meeting-intelligence](https://github.com/openai/plugins/tree/main/plugins/notion/skills/notion-meeting-intelligence) | 会议准备 | 结合 Notion 中的背景资料，整理议程、会前阅读材料和待决策事项。 |
| [notion-research-documentation](https://github.com/openai/plugins/tree/main/plugins/notion/skills/notion-research-documentation) | 研究与文档 | 检索多个 Notion 来源，汇总为带有引用的简报、对比分析或研究报告。 |
| [notion-spec-to-implementation](https://github.com/openai/plugins/tree/main/plugins/notion/skills/notion-spec-to-implementation) | 需求落地 | 将 Notion 中的 PRD 或功能规格拆解为实施计划、任务和进度记录。 |

原先收录的 [openai/skills](https://github.com/openai/skills) 已在 README 标记弃用，并指向 `openai/plugins`。上表已更新为当前插件中的目录；旧目录仍可作为历史参考，不再作为首选安装入口。安装与启用以[插件项目说明](https://github.com/openai/plugins#readme)及客户端文档为准，不应直接套用旧版 MCP 配置命令。

## 社区 Skills（非官方）

以下资源由第三方维护，不属于 Notion 或 OpenAI 官方发布的 Skills。客户端兼容性与依赖按各项目说明列出，未逐一实测。

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

前两个条目的安装方法见[社区项目说明](https://github.com/sickn33/antigravity-awesome-skills#readme)。`notion-automation` 使用第三方 Rube MCP，与 OpenAI 插件的集成方式不同。`notion-template-business` 是经营策略类 Skill，不是 Notion 数据操作工具。

## Clipno CLI 配套 Skill

- [项目仓库](https://github.com/EwingYangs/clipno-cli) · [官网](https://clipno.app)
- [Skill 原文](https://github.com/EwingYangs/clipno-cli/blob/main/skills/clipno/SKILL.md)
- 分类：第三方网页剪藏工具，同时提供 CLI 与 Agent Skill。通过 Clipno 服务执行，不需要 Notion MCP。

### 安装 Skill

在所用客户端支持的环境中运行以下命令，并按提示选择安装目标：

```bash
npx skills add EwingYangs/clipno-cli
```

该命令添加的是供 Agent 使用的工作流程，不等同于全局安装 `clipno` CLI，也不会自动完成账号授权。项目还提供 Claude Code 插件市场和手动复制安装方式，见其 README。

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

`extract` 不要求关联 Notion，但仍通过 Clipno 服务执行，应按项目说明完成 Clipno 登录。`save` 支持标签、备注、标题，以及转录、OCR 和 AI 摘要等选项；部分增强结果异步写入，并受账号设置和配额限制。套餐与额度以官网当前说明为准。

## 使用与收录说明

- 根据实际依赖选择资源：OpenAI 插件使用其 Notion 集成，社区自动化 Skill 使用 Rube MCP，Clipno 使用 CLI 与 Clipno 服务，模板经营 Skill 主要提供策略指导。
- 安装后核对工具可用性和授权范围；安装 Skill、连接服务、授予页面或数据库访问权限是不同步骤。
- 新条目应提供项目及 `SKILL.md` 原始链接、维护者、用途、适用客户端、运行时与服务依赖，以及安装和授权说明。第三方收集仓库中的条目应注明所在仓库和其声明的上游来源。
- 核验分层记录：本页已核实上游说明、Skill 文件可访问性及其声明用途；尚未安装或执行这些 Skills、CLI，也未验证账号授权、网页提取质量或 Notion 写入行为。

核实日期：2026-11-09。上游目录、安装方式和服务套餐可能更新，请以原项目说明为准。
