# Resource Verification Record

[简体中文](resource-checks.md) | **English**

Review date: 2026-11-09. [Back to the resource directory](../README.en.md)

“Upstream documentation reviewed” means the original README was retrieved and its described purpose and links checked. It does not establish successful installation, login, functional testing, or active maintenance. “External site unverified” means the environment's proxy returned 403 before a response from the destination website was obtained; it does not establish that the site is offline.

## Open-source Project Sources

| Project | Upstream documentation reviewed | Changes and scope |
| :---- | :---- | :---- |
| Notion Avatar Maker | [README](https://github.com/Mayandev/notion-avatar/blob/main/README.md) | Replaced the old Vercel address with the upstream `notion-avatar.app` website, using `/zh` in Chinese and `/en` in English. The website itself is unverified. |
| notion-enhancer | [README](https://github.com/notion-enhancer/notion-enhancer/blob/main/README.md) | Added interface enhancement purpose and documentation link; no claim about current client compatibility or maintenance activity. |
| NotionNext | [README](https://github.com/notionnext-org/NotionNext/blob/main/README.md) | Used the current organization repository and described website publishing use cases. |
| React Notion X | [README](https://github.com/NotionX/react-notion-x/blob/master/readme.md) | Identified it as a React rendering library, distinct from an official API SDK. |
| notion-sdk-js | [README](https://github.com/makenotion/notion-sdk-js/blob/main/README.md) | Identified the official JS/TS SDK and package name `@notionhq/client`. |
| notion-sdk-py | [README](https://github.com/ramnes/notion-sdk-py/blob/main/README.md) | Identified the community Python SDK and package name `notion-client`. |

## Websites, Documentation, and Service Directories

The environment's network policy prevented access to these external sites during this review. Availability, login, paid features, and embedding have not been tested. Descriptions serve as directory summaries, not guarantees of functionality or plan features.

| Entry | Source URL | Verification status |
| :---- | :---- | :---- |
| Notion Avatar Maker | <https://notion-avatar.app/en> · <https://notion-avatar.app/zh> | Addresses cross-checked against the upstream README; external site unverified. |
| notion-enhancer documentation | <https://notion-enhancer.github.io/> | Address cross-checked against the upstream README; external site unverified. |
| Notion Themes | <https://notionthemes.yudax.me> | Existing repository entry with unknown current status. Retained as historical; unverified browser support and installation instructions removed. |
| Indify | <https://indify.co/> | Third-party widget service; external site unverified. |
| Apption | <https://apption.co/> | Third-party directory and tools; external site unverified. |
| WidgetBox | <https://widgetbox.app/> | Third-party widget service; external site unverified. |
| API Getting started | <https://developers.notion.com/docs/getting-started> | Official entry point, also linked from SDK documentation; external site unverified. |
| API Reference | <https://developers.notion.com/reference/intro> | Official API reference entry point; external site unverified. |
| Notion Help Center | <https://www.notion.com/help> | Official entry point; external site unverified. |
| Notion Academy | <https://www.notion.com/help/notion-academy> | Official course entry point; exact route and course availability await browser verification. |
| Notion Marketplace | <https://www.notion.com/templates> | Official platform; individual template authors, prices, and licenses require separate checks. |
| Notion Everything | <https://www.notioneverything.com/> | Third-party directory awaiting online verification; its individual templates have not been reviewed. |

For skill and Clipno sources, prerequisites, and verification scope, see the [Notion Skills collection](notion-skills.en.md).

## Additions Inspired by spencerpauly/awesome-notion

The [reference directory](https://github.com/spencerpauly/awesome-notion/blob/master/README.md) was read to identify candidates, followed by each original project's documentation. This update adds the following eight distinct resources and moves the existing React Notion X entry into the rendering tools category. Both language versions were updated. Checks cover sources and described purposes only; nothing was installed, deployed, or executed, so current runtime compatibility is not guaranteed.

| New resource | Original documentation reviewed | Selection rationale and limits |
| :---- | :---- | :---- |
| Simple Icons CDN | [README](https://github.com/LitoMore/simple-icons-cdn/blob/main/README.md) | General-purpose brand icon service, listed for icon links and assets rather than as a Notion plugin. |
| Next.js Notion Starter Kit | [README](https://github.com/transitive-bullshit/nextjs-notion-starter-kit/blob/main/readme.md) | Upstream explicitly uses Notion as a CMS; verified its Node.js >= 22 and public root page requirements. |
| NoteHost | [README](https://github.com/velsa/notehost/blob/main/README.md) | Listed its Cloudflare Workers proxy, custom domains, and styling; did not carry over unconditional free-hosting claims. |
| Ultimate Notion | [README](https://github.com/ultimate-notion/ultimate-notion/blob/main/README.md) | Verified higher-level Python interfaces and exports built on notion-sdk-py; labeled as a community project. |
| Notion Helper | [README](https://github.com/TomFrankly/notion-helper/blob/main/README.md) | Verified its ESM library, object builders, and large-request splitting; distinguished it from the official SDK. |
| Mk Notes | [README](https://github.com/Myastr0/mk-notes/blob/master/README.md) | Verified Markdown-to-Notion sync and the CLI package name; did not infer two-way sync. |
| notion4ever | [README](https://github.com/MerkulovDaniil/notion4ever/blob/main/README.md) | Verified exports of Markdown, HTML, and subpages through the official API; no claim of complete backup or all block types. |
| Indie Hacker Toolkit | [README](https://github.com/Wittlesus/indie-hacker-toolkit/blob/master/README.md) | Verified its commercial template pack, purchase requirement, and Markdown import workflow; omitted marketing metrics and did not call it a free open-source template. |

### Content Not Copied Directly

| Candidate or claim | Reason |
| :---- | :---- |
| The official Notion API is “still in private beta” | Outdated claim in the reference directory; not carried over. |
| `4ier/notion-cli` | README.md/readme.md requests against main/master all returned 404 in this check. Documentation was not confirmed, so it was not listed; this does not prove the project is permanently unavailable. |
| `yannbolliger/notion-exporter` | Its documentation relies on the web app's internal export interface and browser cookies. This update prioritizes notion4ever, which uses the official API. |
| `janniks/vue-notion` | Upstream flags unfinished Vue 3 documentation, potentially outdated docs, and private-API fetching methods. Not added to the main directory in this update. |
| `5am-code/laravel-notion-api` | Its README lists Laravel 8–10 compatibility. Compatibility with newer versions was not investigated further, so it was not added in this update. |
| Hosted services such as Engine.so, Feather, and Super.so | They illustrate the knowledge-base, blog, and website use cases, but their current service status and features were not individually verified. This update uses existing or source-checked tools to explain the use cases instead of repeating plan and feature promises. |

The “Notion as …” explanation and selection guidance are integrated into [Notion use cases in the README](../README.en.md#notion-as), without a separate duplicate tool list.
