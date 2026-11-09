# 资源核验记录

**简体中文** | [English](resource-checks.en.md)

核验日期：2026-11-09。[返回资源目录](../README.md)

“上游说明已读取”表示已获取原项目 README 并核对用途和相关地址，不代表安装、登录、功能测试或维护状态评估已完成。“外站未验证”表示当前环境的代理返回 403，未获得目标网站的 HTTP 响应，不能据此判定网站失效。

## 开源项目来源

| 项目 | 已读取的上游说明 | 本轮处理 |
| :---- | :---- | :---- |
| Notion Avatar Maker | [README](https://github.com/Mayandev/notion-avatar/blob/main/README.md) | 将旧 Vercel 地址更新为 README 提供的 `notion-avatar.app`；中文版使用 `/zh`，英文版使用 `/en`；官网本身未验证。 |
| notion-enhancer | [README](https://github.com/notion-enhancer/notion-enhancer/blob/main/README.md) | 收录界面增强用途及文档地址；不推断当前客户端兼容性或维护活跃度。 |
| NotionNext | [README](https://github.com/notionnext-org/NotionNext/blob/main/README.md) | 使用当前组织仓库路径，收录建站与内容发布用途。 |
| React Notion X | [README](https://github.com/NotionX/react-notion-x/blob/master/readme.md) | 标明 React 渲染组件库身份，避免与官方 API SDK 混淆。 |
| notion-sdk-js | [README](https://github.com/makenotion/notion-sdk-js/blob/main/README.md) | 标明官方 JS/TS SDK 及包名 `@notionhq/client`。 |
| notion-sdk-py | [README](https://github.com/ramnes/notion-sdk-py/blob/main/README.md) | 标明社区 Python SDK 及包名 `notion-client`。 |

## 官网、文档与服务目录

以下外站入口本轮未能通过网络策略，未作在线可用性、登录、付费功能或嵌入测试。用途为目录简介，不构成功能或套餐保证。

| 条目 | 来源地址 | 核验状态 |
| :---- | :---- | :---- |
| Notion Avatar Maker | <https://notion-avatar.app/zh> · <https://notion-avatar.app/en> | 地址由上游 README 交叉确认；外站未验证。 |
| notion-enhancer 文档 | <https://notion-enhancer.github.io/> | 地址由上游 README 交叉确认；外站未验证。 |
| Notion Themes | <https://notionthemes.yudax.me> | 原仓库已有条目；当前状态不明，保留为历史收录，移除未经核实的浏览器支持与安装步骤。 |
| Indify | <https://indify.co/> | 第三方组件服务；外站未验证。 |
| Apption | <https://apption.co/> | 第三方目录与工具服务；外站未验证。 |
| WidgetBox | <https://widgetbox.app/> | 第三方组件服务；外站未验证。 |
| API Getting started | <https://developers.notion.com/docs/getting-started> | 官方入口，亦由 SDK README 引用；外站未验证。 |
| API Reference | <https://developers.notion.com/reference/intro> | 官方 API 参考入口；外站未验证。 |
| Notion 帮助中心 | <https://www.notion.com/help> | 官方入口；外站未验证。 |
| Notion Academy | <https://www.notion.com/help/notion-academy> | 官方课程入口；具体路径与课程可用性待浏览器复核。 |
| Notion 模板市场 | <https://www.notion.com/templates> | 官方平台；具体模板作者、价格与授权需逐项核对。 |
| Notion Everything | <https://www.notioneverything.com/> | 第三方目录，待在线复核；不代表其中每个模板均已核验。 |

Skills 与 Clipno 的来源、安装前提及核验范围见 [Notion Skills 收集](notion-skills.md)。

## 参考 spencerpauly/awesome-notion 的增补

已读取[参考目录](https://github.com/spencerpauly/awesome-notion/blob/master/README.md)，据此筛选候选，再逐一读取原项目说明。本轮增加以下八个不同资源，并将原有 React Notion X 移至渲染工具分类；中英文版本同步更新。以下均为来源与声明用途核验，未安装、部署或执行，不能据此保证当前运行兼容性。

| 新增资源 | 已读取的原项目说明 | 收录依据与边界 |
| :---- | :---- | :---- |
| Simple Icons CDN | [README](https://github.com/LitoMore/simple-icons-cdn/blob/main/README.md) | 通用品牌图标服务，按图标链接与素材用途收录，不描述成 Notion 插件。 |
| Next.js Notion Starter Kit | [README](https://github.com/transitive-bullshit/nextjs-notion-starter-kit/blob/main/readme.md) | 上游明确使用 Notion 作为 CMS；核对到 Node.js >= 22 和公开根页面要求。 |
| NoteHost | [README](https://github.com/velsa/notehost/blob/main/README.md) | 收录 Cloudflare Workers 代理、自定义域名和样式用途；不沿用无条件免费托管的表述。 |
| Ultimate Notion | [README](https://github.com/ultimate-notion/ultimate-notion/blob/main/README.md) | 核对到基于 notion-sdk-py 的 Python 高层接口及导出能力，标为社区项目。 |
| Notion Helper | [README](https://github.com/TomFrankly/notion-helper/blob/main/README.md) | 核对到 ESM 工具库、对象构建与大请求拆分用途，区分于官方 SDK。 |
| Mk Notes | [README](https://github.com/Myastr0/mk-notes/blob/master/README.md) | 核对到 Markdown 到 Notion 的同步及 CLI 包名，不推断双向同步。 |
| notion4ever | [README](https://github.com/MerkulovDaniil/notion4ever/blob/main/README.md) | 核对到通过官方 API 导出 Markdown、HTML 和子页面；不保证完整备份或所有块类型。 |
| Indie Hacker Toolkit | [README](https://github.com/Wittlesus/indie-hacker-toolkit/blob/master/README.md) | 核对到商业模板包、购买和 Markdown 导入要求；不复制营销指标，不称其为免费开源模板。 |

### 未直接照搬的内容

| 候选或表述 | 处理原因 |
| :---- | :---- |
| 官方 Notion API “仍在私测” | 参考目录中的过时描述，不沿用。 |
| `4ier/notion-cli` | 本次尝试 main/master 分支的 README.md/readme.md 均返回 404；未确认项目文档，不加入正式目录，也不据此断定项目永久失效。 |
| `yannbolliger/notion-exporter` | 上游说明依赖 Web App 内部导出接口及浏览器 Cookie；本轮优先收录通过官方 API 导出的 notion4ever。 |
| `janniks/vue-notion` | 上游提示 Vue 3 文档尚在完善、部分文档可能过时，取数方法依赖私有 API；暂不扩充到主目录。 |
| `5am-code/laravel-notion-api` | README 的兼容性说明列出 Laravel 8–10，未进一步确认新版本兼容性，本轮暂不收录。 |
| Engine.so、Feather、Super.so 等托管服务 | 可体现公开知识库、博客和网站三种场景，但当前未逐一验证服务状态与功能；本轮先用已有或已核对上游的工具说明场景，不照搬套餐和功能承诺。 |

“Notion as …” 的场景说明及选型建议已并入 [README 的 Notion 应用场景](../README.md#notion-as)，不另设重复工具清单。
