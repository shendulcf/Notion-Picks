# Notion Picks

[简体中文](README.md) | **English**

A selection of Notion tools, skills, and templates, with notes on what they do, how to get started, and what to watch for. The aim is to help you find a few tools that fit your work without having to sift through a huge list.

[Skills guide](docs/notion-skills.en.md) · [Verification record](docs/resource-checks.en.md) · [Contribute](CONTRIBUTING.en.md)

Descriptions are based on project documentation. The [verification record](docs/resource-checks.en.md) tracks which sources were read and which services still need testing.

## Start Here

| I want to… | Start with |
| :---- | :---- |
| Personalize my workspace | [Appearance](#notion-beautify) and [widgets](#notion-widgets) |
| Build a blog, knowledge base, or website | [Notion use cases](#notion-as) |
| Use an AI agent or clip links | [Skills](#notion-skills) and [Clipno](#notion-cli) |
| Connect code or move content | [API tools](#notion-api) and [sync/export](#notion-sync-export) |
| Learn Notion or find a starting template | [Tutorials](#notion-tutorials) and [templates](#notion-templates) |

## Contents

- [Notion Beautify](#notion-beautify)
- [Notion Widgets](#notion-widgets)
- [Notion Use Cases: Blogs, Knowledge Bases, and Websites](#notion-as)
- [Notion API](#notion-api)
- [Notion Skills](#notion-skills)
- [Notion CLI](#notion-cli)
- [Sync and Export](#notion-sync-export)
- [Notion Tutorials](#notion-tutorials)
- [Notion Templates](#notion-templates)
- [Selection and Verification](#selection-and-verification)
- [Contributing](#contributing)
- [License](#license)

---

## Notion Beautify

| Resource | Purpose | Source and notes |
| :---- | :---- | :---- |
| [Notion Avatar Maker](https://notion-avatar.app/en) | Create Notion-style avatars with configurable parts and AI features. | [Source](https://github.com/Mayandev/notion-avatar); AI features depend on the live service. |
| [Simple Icons CDN](https://github.com/LitoMore/simple-icons-cdn) | Get brand icons with customizable colors and sizes for Notion icons or image links. | General-purpose icon CDN; check trademark and license guidance before use. |
| [notion-enhancer](https://github.com/notion-enhancer/notion-enhancer) | Customize and enhance the Notion interface. | [Documentation](https://notion-enhancer.github.io/); consult the current project instructions for installation and supported clients. |

<details>
<summary>Historical screenshots and theme listing</summary>

### Notion-style Avatar

![Historical screenshot of Notion-style avatars](README.assets/image-20220704131006302.png)

### Notion Themes (Historical Listing)

The [original website](https://notionthemes.yudax.me) offered Notion color schemes and themes. Current availability and browser compatibility have not been confirmed. Retained for historical reference; the screenshot below shows an older version.

![Historical screenshot of Notion Themes](README.assets/image-20220704132023438.png)

</details>

## Notion Widgets

Add a widget to a Notion page by embedding the link its service generates. Some widgets require an account or a paid plan.

| Resource | Purpose | Source |
| :---- | :---- | :---- |
| [Indify](https://indify.co/) | Page widgets such as clocks, weather, and countdowns. | Third-party service |
| [Apption](https://apption.co/) | Discover tools and widgets for embedding in Notion. | Third-party directory and tools |
| [WidgetBox](https://widgetbox.app/) | Customizable calendars, clocks, and other widgets. | Third-party service |

<a id="notion-as"></a>
<a id="notion-websites-and-publishing"></a>

## Notion Use Cases: Blogs, Knowledge Bases, and Websites

“Notion as …” means writing content in Notion and publishing it as a blog, knowledge base, or website through another tool. Your choice depends on what you want to build and whether you want to handle deployment yourself.

### Choose by Use Case

| Use case | Notion’s role | How to choose |
| :---- | :---- | :---- |
| Notion as Blog CMS | Edit articles, categories, and page content. | Consider NotionNext for a website system, or Next.js Notion Starter Kit for a Next.js development template. |
| Notion as Public Knowledge Base | Maintain help articles, guides, and other knowledge content. | NotionNext describes knowledge-base support. Separately verify search, versioning, access control, or customer-support integrations if you need them. |
| Notion as Website | Edit content for portfolios, personal websites, or product pages. | NotionNext provides a website system; NoteHost uses Cloudflare to add your own domain and page styling to Notion pages. |

### Tools and Requirements

| Project | Purpose | Audience and requirements |
| :---- | :---- | :---- |
| [NotionNext](https://github.com/notionnext-org/NotionNext) | Manage content in Notion and publish blogs, portfolios, knowledge bases, and other websites. | Users who want to deploy their own sites; see the project README for configuration and deployment requirements. |
| [Next.js Notion Starter Kit](https://github.com/transitive-bullshit/nextjs-notion-starter-kit) | A website and blog development template using Next.js and React Notion X. | The current README requires Node.js >= 22, a public root Notion page, and your own deployment. |
| [NoteHost](https://github.com/velsa/notehost) | Proxy Notion sites through Cloudflare Workers with custom domains, page paths, and styling. | Requires your own domain, a Cloudflare account, and deployment configuration. A proxy solution rather than an independent CMS. |

These tools handle content presentation and publishing. Check separately for membership, payment, or order features, and choose carefully which pages to publish. API authorization does not make a page public. To display Notion content inside your own React app, see [page rendering tools](#notion-renderers).

## Notion API

| Resource | Purpose | Source and requirements |
| :---- | :---- | :---- |
| [Getting started](https://developers.notion.com/docs/getting-started) | Create an integration and start making API requests. | Official Notion documentation; configure credentials and grant content access for your integration type. |
| [API Reference](https://developers.notion.com/reference/intro) | Look up endpoints, objects, and request formats. | Official reference; check API versions and distinctions between databases, data sources, and other objects. |
| [notion-sdk-js](https://github.com/makenotion/notion-sdk-js) | Call the Notion API from JavaScript or TypeScript. | Official SDK; npm package: `@notionhq/client`. |
| [notion-sdk-py](https://github.com/ramnes/notion-sdk-py) | Call the Notion API from Python. | Community SDK; PyPI package: `notion-client`. |
| [Ultimate Notion](https://github.com/ultimate-notion/ultimate-notion) | Use higher-level Python interfaces for pages and databases, with content exports. | Community project built on notion-sdk-py; requires a Notion integration token and content access. |
| [Notion Helper](https://github.com/TomFrankly/notion-helper) | Build page and block objects and split large API requests. | Community ESM library used with the official JS SDK. |

<a id="notion-renderers"></a>

### Page Rendering Tools

| Project | Purpose | Requirements |
| :---- | :---- | :---- |
| [React Notion X](https://github.com/NotionX/react-notion-x) | Render Notion pages in React applications. | For developers; a rendering library rather than an official API SDK. Check its documentation for data fetching and supported content. |

## Notion Skills

These skills help an AI agent organize Notion content, prepare meetings, or save links. See the [Notion Skills collection](docs/notion-skills.en.md) for setup instructions.

- [OpenAI Notion plugin and four skills](docs/notion-skills.en.md#openai-notion-plugin): knowledge capture, meeting preparation, research documentation, and implementation planning. The deprecated `openai/skills` links have been updated to the current plugin paths.
- [Community skills](docs/notion-skills.en.md#community-skills-unofficial): Notion automation, template business guidance, and web clipping through the Clipno CLI.
- [Clipno skill installation and usage](docs/notion-skills.en.md#clipno-cli-companion-skill): skill installation, CLI installation, and account authorization are separate steps.

## Notion CLI

| Tool | Purpose | Requirements and setup |
| :---- | :---- | :---- |
| [Clipno](https://github.com/EwingYangs/clipno-cli) · [Website](https://clipno.app) | Save links to Notion; extract pages as structured JSON or Markdown, with optional transcription, OCR, and summaries. | Node.js >= 18 and Clipno login. Saving to Notion also requires linking a Notion workspace in Clipno. [Installation and usage](docs/notion-skills.en.md#clipno-cli-companion-skill) |

Clipno saves and extracts links through its own service. Its companion skill teaches an agent to use the CLI, without Notion MCP. This description follows the project documentation; the tool has not been tested here.

<a id="notion-sync-export"></a>

## Sync and Export

| Project | Purpose | Requirements and limits |
| :---- | :---- | :---- |
| [Mk Notes](https://github.com/Myastr0/mk-notes) | Sync local Markdown documents to Notion from the command line. | Community CLI; npm package: `@mk-notes/cli`. Requires Notion access. Sync direction: Markdown → Notion. |
| [notion4ever](https://github.com/MerkulovDaniil/notion4ever) | Export pages and subpages as Markdown, HTML, and other content through the official Notion API. | Python tool requiring an integration token and target page access. Export coverage depends on the API and supported content types; not a complete workspace backup. |

## Notion Tutorials

| Resource | Use case | Source |
| :---- | :---- | :---- |
| [Notion Help Center](https://www.notion.com/help) | Getting started, page editing, databases, sharing, and permissions. | Official |
| [Notion Academy](https://www.notion.com/help/notion-academy) | Learn Notion through courses. | Official; check the website for courses and supported languages. |
| [Notion API getting started](https://developers.notion.com/docs/getting-started) | Build integrations and automation tools. | Official; see [Notion API](#notion-api) for SDKs. |

## Notion Templates

| Resource | Purpose | Source and notes |
| :---- | :---- | :---- |
| [Notion Marketplace](https://www.notion.com/templates) | Find templates for work, study, personal life, and project management. | Official platform with templates from Notion and community creators; individual templates may be free or paid. |
| [Notion Everything](https://www.notioneverything.com/) | Discover third-party Notion templates and related resources. | Third-party directory; check each creator's pricing, license, and delivery terms. |
| [Indie Hacker Toolkit](https://github.com/Wittlesus/indie-hacker-toolkit) | Template pack for solo founders, including launch checklists, revenue tracking, and content calendars. | Paid template pack imported as Markdown; see the project for pricing, delivery, and redistribution terms. |

Look at a template’s preview and database structure before deciding whether it fits the way you work. For help designing and selling templates, see [Community skills](docs/notion-skills.en.md#community-skills-unofficial).

## Selection and Verification

Resources are chosen for the problems they solve, who they suit, and what it takes to use them. Both official and community projects are included, with paid products labeled.

Thanks to [spencerpauly/awesome-notion](https://github.com/spencerpauly/awesome-notion) for leads on some of these resources.

Sources were last reviewed on 2026-11-09. The listed open-source projects’ READMEs were read, but the tools have not been installed and tested individually. Network restrictions prevented access to some websites. Details are in the [resource verification record](docs/resource-checks.en.md).

## Contributing

Contributions from people who have used these tools are welcome, as are corrections and broken-link reports. The [contribution guide](CONTRIBUTING.en.md) covers entry format and keeping both languages up to date.

## License

This repository uses the [MIT License](LICENSE). Linked projects, icons, and templates retain their own licenses and terms.
