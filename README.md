# Awesome-Notion

**简体中文** | [English](README.en.md)

收集 Notion 工具、Skills、模板与内容发布方案的双语目录，附项目来源和使用前提。

[Skills 详细指南](docs/notion-skills.md) · [资源核验记录](docs/resource-checks.md) · [贡献指南](CONTRIBUTING.md)

条目介绍上游声明的用途；来源核验与待验证服务见[核验记录](docs/resource-checks.md)。

## 从这里开始

| 我想做什么 | 推荐入口 |
| :---- | :---- |
| 个性化工作区 | [美化](#notion-beautify)与[小组件](#notion-widgets) |
| 搭博客、知识库或网站 | [Notion 应用场景](#notion-as) |
| 使用 AI Agent 或剪藏链接 | [Skills](#notion-skills) 与 [Clipno](#notion-cli) |
| 用代码集成或迁移内容 | [API 工具](#notion-api)与[同步导出](#notion-sync-export) |
| 学习 Notion 或寻找起步模板 | [教程](#notion-tutorials)与[模板](#notion-templates) |

## 目录

- [Notion 美化](#notion-beautify)
- [Notion 小组件](#notion-widgets)
- [Notion 应用场景：博客、知识库与网站](#notion-as)
- [Notion API 与开发工具](#notion-api)
- [Notion 技能（Skills）](#notion-skills)
- [Notion 命令行工具](#notion-cli)
- [同步与导出](#notion-sync-export)
- [Notion 教程](#notion-tutorials)
- [Notion 模板](#notion-templates)
- [收录与核验说明](#收录与核验说明)
- [参与贡献](#参与贡献)
- [许可证](#许可证)

---

<a id="notion-beautify"></a>

## Notion 美化

| 资源 | 用途 | 来源与说明 |
| :---- | :---- | :---- |
| [Notion Avatar Maker](https://notion-avatar.app/zh) | 生成 Notion 风格头像，支持部件组合及 AI 头像功能。 | [开源仓库](https://github.com/Mayandev/notion-avatar)；AI 功能以实际服务为准。 |
| [Simple Icons CDN](https://github.com/LitoMore/simple-icons-cdn) | 获取可调颜色、尺寸的品牌图标，用于 Notion 图标或图片链接。 | 通用图标 CDN；使用前查看图标的商标与许可说明。 |
| [notion-enhancer](https://github.com/notion-enhancer/notion-enhancer) | Notion 界面定制与增强。 | [文档](https://notion-enhancer.github.io/)；安装方式和适配客户端应以项目当前说明为准。 |

<details>
<summary>历史截图与主题收录</summary>

### Notion 风格头像

![Notion 风格头像历史截图](README.assets/image-20220704131006302.png)

### Notion Themes（历史收录）

[原网站](https://notionthemes.yudax.me)用于 Notion 配色与主题定制。当前未确认服务可用性及浏览器兼容性，保留作历史参考；以下为旧版截图。

![Notion Themes 历史截图](README.assets/image-20220704132023438.png)

</details>

<a id="notion-widgets"></a>

## Notion 小组件

将组件服务生成的链接通过 Notion 的嵌入功能加入页面。账号要求、可嵌入内容及免费或付费范围以各服务说明为准。

| 资源 | 用途 | 来源 |
| :---- | :---- | :---- |
| [Indify](https://indify.co/) | 时钟、天气、倒计时等页面组件。 | 第三方服务 |
| [Apption](https://apption.co/) | 查找适合嵌入 Notion 的工具和组件。 | 第三方目录与工具服务 |
| [WidgetBox](https://widgetbox.app/) | 日历、时钟等可定制组件。 | 第三方服务 |

<a id="notion-as"></a>
<a id="notion建站与内容发布"></a>

## Notion 应用场景：博客、知识库与网站

“Notion as …” 表示用 Notion 编辑和管理内容，再由外部工具发布为博客、知识库或网站。下表按使用目标选择工具。

### 按场景选择

| 场景 | Notion 承担什么 | 如何选 |
| :---- | :---- | :---- |
| Notion as Blog CMS（博客内容管理） | 编辑文章、分类和页面内容。 | 希望搭完整站点可看 NotionNext；偏好 Next.js 开发模板可看 Next.js Notion Starter Kit。 |
| Notion as Public Knowledge Base（公开知识库） | 维护帮助文档、指南和知识内容。 | NotionNext 声明支持知识库；若需要站内搜索、版本、访问控制或客服集成，应另行核实工具是否支持。 |
| Notion as Website（网站内容后台） | 编辑用于作品集、个人站或产品介绍页的内容。 | NotionNext 适合站点系统；NoteHost 适合通过 Cloudflare 为 Notion 页面配置自己的域名与页面样式。 |

### 工具与前提

| 项目 | 用途 | 适合人群与前提 |
| :---- | :---- | :---- |
| [NotionNext](https://github.com/notionnext-org/NotionNext) | 以 Notion 管理内容，发布博客、作品集、知识库等网站。 | 希望自行部署站点的用户；配置和部署要求见项目 README。 |
| [Next.js Notion Starter Kit](https://github.com/transitive-bullshit/nextjs-notion-starter-kit) | 基于 Next.js 和 React Notion X 的网站、博客开发模板。 | 当前 README 要求 Node.js >= 22，配置公开的根 Notion 页面，并自行部署。 |
| [NoteHost](https://github.com/velsa/notehost) | 用 Cloudflare Workers 代理 Notion 站点，配置自定义域名、页面路径及样式。 | 需要自己的域名、Cloudflare 账号和部署配置；它是代理方案，不是独立内容管理系统。 |

这些工具主要解决内容展示和发布，不能据此推断它们提供完整的会员、支付、订单或业务数据库能力。公开站点只应包含计划对外发布的内容；API 集成授权与将页面发布到互联网是不同操作。需要嵌入自有 React 应用时，见下方[页面渲染工具](#notion-renderers)。

<a id="notion-api"></a>

## Notion API 与开发工具

| 资源 | 用途 | 来源与使用前提 |
| :---- | :---- | :---- |
| [Getting started](https://developers.notion.com/docs/getting-started) | 创建集成并开始调用 API。 | Notion 官方文档；按集成类型配置凭据并授予内容访问权限。 |
| [API Reference](https://developers.notion.com/reference/intro) | 查询端点、对象和请求格式。 | Notion 官方参考；注意 API 版本及数据库、数据源等对象的区别。 |
| [notion-sdk-js](https://github.com/makenotion/notion-sdk-js) | 在 JavaScript / TypeScript 中调用 Notion API。 | 官方 SDK；npm 包名为 `@notionhq/client`。 |
| [notion-sdk-py](https://github.com/ramnes/notion-sdk-py) | 在 Python 中调用 Notion API。 | 社区 SDK；PyPI 包名为 `notion-client`。 |
| [Ultimate Notion](https://github.com/ultimate-notion/ultimate-notion) | 在 Python 中以更高层接口操作页面和数据库，并导出内容。 | 社区项目，基于 notion-sdk-py；需要 Notion 集成令牌及内容授权。 |
| [Notion Helper](https://github.com/TomFrankly/notion-helper) | 构建页面与内容块对象，并拆分大型 API 请求。 | 社区 ESM 工具库，搭配官方 JS SDK 使用。 |

<a id="notion-renderers"></a>

### 页面渲染工具

| 项目 | 用途 | 使用前提 |
| :---- | :---- | :---- |
| [React Notion X](https://github.com/NotionX/react-notion-x) | 在 React 项目中渲染 Notion 页面。 | 面向开发者；它是渲染组件库，不是官方 API SDK，取数方式及支持内容应按项目说明确认。 |

<a id="notion-skills"></a>

## Notion 技能（Skills）

收集用于 Notion 的 AI Agent Skills，按来源及连接方式分类。完整条目、安装方法和使用前提见 [Notion Skills 收集](docs/notion-skills.md)。

- [OpenAI Notion 插件及四个 Skills](docs/notion-skills.md#openai-notion-插件)：知识整理、会议准备、研究文档和需求实施规划；原 `openai/skills` 仓库已弃用，已更新到当前插件路径。
- [社区 Skills](docs/notion-skills.md#社区-skills非官方)：Notion 自动化、模板经营指导，以及基于 Clipno CLI 的网页剪藏。
- [Clipno Skill 安装与使用](docs/notion-skills.md#clipno-cli-配套-skill)：区分 Skill 安装、CLI 安装及账号授权。

<a id="notion-cli"></a>

## Notion 命令行工具

| 工具 | 主要用途 | 使用前提与安装 |
| :---- | :---- | :---- |
| [Clipno](https://github.com/EwingYangs/clipno-cli) · [官网](https://clipno.app) | 将链接剪藏到 Notion；将网页提取为结构化 JSON 或 Markdown，按选项进行转录、OCR 和摘要。 | Node.js >= 18；登录 Clipno。保存到 Notion 还需在 Clipno 中关联 Notion 工作区。[安装与说明](docs/notion-skills.md#clipno-cli-配套-skill) |

Clipno 是附带 Agent Skill 的命令行工具，使用 Clipno 服务，不依赖 Notion MCP。以上为项目声明能力，尚未安装实测。

<a id="notion-sync-export"></a>

## 同步与导出

| 项目 | 用途 | 使用前提与边界 |
| :---- | :---- | :---- |
| [Mk Notes](https://github.com/Myastr0/mk-notes) | 使用命令行将本地 Markdown 文档同步到 Notion。 | 社区 CLI；npm 包为 `@mk-notes/cli`，需配置 Notion 访问。同步方向：Markdown → Notion。 |
| [notion4ever](https://github.com/MerkulovDaniil/notion4ever) | 通过官方 Notion API 将页面及子页面导出为 Markdown、HTML 等内容。 | Python 工具，需要集成令牌及目标页面访问权限；导出能力受 API 与工具支持的内容类型限制，不等同于完整工作区备份。 |

<a id="notion-tutorials"></a>

## Notion 教程

| 资源 | 适用场景 | 来源 |
| :---- | :---- | :---- |
| [Notion 帮助中心](https://www.notion.com/help) | 入门、页面编辑、数据库、共享与权限等功能查询。 | 官方 |
| [Notion Academy](https://www.notion.com/help/notion-academy) | 按课程学习 Notion。 | 官方；课程与语言支持以网站为准。 |
| [Notion API 入门](https://developers.notion.com/docs/getting-started) | 开发集成或自动化工具。 | 官方；配套 SDK 见 [Notion API 与开发工具](#notion-api)。 |

<a id="notion-templates"></a>

## Notion 模板

| 资源 | 用途 | 来源与说明 |
| :---- | :---- | :---- |
| [Notion 模板市场](https://www.notion.com/templates) | 按工作、学习、生活及项目管理等场景查找模板。 | 官方平台，包含官方及社区创作者内容；具体模板可能免费或付费。 |
| [Notion Everything](https://www.notioneverything.com/) | 查找第三方 Notion 模板及相关资源。 | 第三方目录；以创作者的价格、授权及交付说明为准。 |
| [Indie Hacker Toolkit](https://github.com/Wittlesus/indie-hacker-toolkit) | 面向独立开发者的发布清单、收入追踪、内容日历等模板包。 | 付费模板包，以 Markdown 导入；价格、交付和再分发许可见原项目。 |

选择模板时，优先核对预览、数据库结构、所需功能及是否适合自己的工作流程。模板经营相关的 Agent Skill 见 [社区 Skills](docs/notion-skills.md#社区-skills非官方)。

## 收录与核验说明

优先收录官方入口、可追溯的开源项目和用途明确的第三方资源；区分官方 SDK、社区工具、服务目录和历史项目。

感谢 [spencerpauly/awesome-notion](https://github.com/spencerpauly/awesome-notion) 提供分类与资源线索。条目按原项目说明重新核对，具体取舍见核验记录。

本轮核验日期：2026-11-09。已读取所列开源项目的上游 README，未安装或测试其功能。部分官网及文档站受当前环境网络策略限制，未验证在线可用性；不代表这些网站已失效。逐项来源与核验范围见 [资源核验记录](docs/resource-checks.md)。

## 参与贡献

欢迎补充资源、修正说明或反馈失效链接。请阅读[贡献指南](CONTRIBUTING.md)，并同步维护中英文版本。

## 许可证

本仓库采用 [MIT License](LICENSE)。外链项目、图标和模板仍遵循各自的许可证及使用条款。
