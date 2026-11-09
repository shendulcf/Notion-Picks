# Notion Skills Collection

[简体中文](notion-skills.md) | **English**

Workflows for AI agents using Notion. A skill typically consists of `SKILL.md` and supporting resources; a CLI executes commands; MCP is a protocol for connecting external services. A project can provide both a CLI and a skill. Installing a skill does not mean its tools are installed or accounts authorized.

[Back to README](../README.en.md#notion-skills)

- [OpenAI Notion Plugin](#openai-notion-plugin)
- [Community Skills (Unofficial)](#community-skills-unofficial)
- [Clipno CLI Companion Skill](#clipno-cli-companion-skill)
- [Usage and Submission Guidelines](#usage-and-submission-guidelines)

## OpenAI Notion Plugin

Source: [Notion plugin in openai/plugins](https://github.com/openai/plugins/tree/main/plugins/notion). The plugin includes the following four skills. The project describes them as using a connected Notion integration; connect and authorize Notion in a client that supports the plugin.

| Skill | Use case | Purpose |
| :---- | :---- | :---- |
| [notion-knowledge-capture](https://github.com/openai/plugins/tree/main/plugins/notion/skills/notion-knowledge-capture) | Knowledge capture | Turn conversations and notes into Notion wiki entries, guides, FAQs, or decision records, linked to existing pages. |
| [notion-meeting-intelligence](https://github.com/openai/plugins/tree/main/plugins/notion/skills/notion-meeting-intelligence) | Meeting preparation | Use Notion context to prepare agendas, pre-reads, and decisions to discuss. |
| [notion-research-documentation](https://github.com/openai/plugins/tree/main/plugins/notion/skills/notion-research-documentation) | Research and documentation | Synthesize multiple Notion sources into cited briefs, comparisons, or research reports. |
| [notion-spec-to-implementation](https://github.com/openai/plugins/tree/main/plugins/notion/skills/notion-spec-to-implementation) | Implementation planning | Turn PRDs or feature specifications in Notion into implementation plans, tasks, and progress updates. |

The previously listed [openai/skills](https://github.com/openai/skills) repository is marked deprecated in its README and points to `openai/plugins`. The table now links to the current plugin directories. Old directories remain historical references rather than preferred installation entry points. Follow the [plugin repository instructions](https://github.com/openai/plugins#readme) and your client's documentation for installation and activation, rather than copying older MCP configuration commands.

## Community Skills (Unofficial)

These resources are maintained by third parties and are not official Notion or OpenAI skills. Client compatibility and dependencies reflect the projects' documentation and have not been individually tested.

### [notion-automation](https://github.com/sickn33/antigravity-awesome-skills/tree/main/skills/notion-automation)

Search and manage Notion pages, databases, blocks, and comments.

- Source: sickn33/antigravity-awesome-skills
- Clients and dependencies: A client supporting skills and MCP; requires Rube MCP (Composio) and an authorized Notion connection.

### [notion-template-business](https://github.com/sickn33/antigravity-awesome-skills/tree/main/skills/notion-template-business)

Plan Notion template design, pricing, sales channels, and marketing.

- Source: sickn33/antigravity-awesome-skills; credits vibeship-spawner-skills as its source
- Clients and dependencies: The project provides setup instructions for Claude Code, Codex, and other clients. Strategic guidance; no Notion MCP connection required.

### [clipno](https://github.com/EwingYangs/clipno-cli/tree/main/skills/clipno)

Guide an agent to use the Clipno CLI to save links to Notion or extract web content.

- Source: EwingYangs/clipno-cli
- Clients and dependencies: The project explicitly documents Claude Code skill usage; other clients depend on their skill support. Requires Node.js >= 18, the Clipno CLI or npx, and Clipno login. Saving also requires a linked Notion workspace.

For the first two entries, see the [community repository instructions](https://github.com/sickn33/antigravity-awesome-skills#readme). `notion-automation` uses third-party Rube MCP, a different connection method from the OpenAI plugin. `notion-template-business` provides business guidance rather than Notion data operations.

## Clipno CLI Companion Skill

- [Repository](https://github.com/EwingYangs/clipno-cli) · [Website](https://clipno.app)
- [Original skill](https://github.com/EwingYangs/clipno-cli/blob/main/skills/clipno/SKILL.md)
- Category: third-party web clipping tool with both a CLI and an agent skill. Uses the Clipno service; Notion MCP is not required.

### Install the Skill

Run the following in an environment supported by your client and select the installation target when prompted:

```bash
npx skills add EwingYangs/clipno-cli
```

This adds a workflow for the agent. It does not globally install the `clipno` CLI or automatically authorize accounts. The project also documents Claude Code plugin marketplace and manual installation methods in its README.

### Use the CLI

Requires Node.js >= 18. Install globally, log in, and verify the login:

```bash
npm i -g clipno
clipno login
clipno whoami
```

Before saving links, connect a workspace in [Clipno's Notion settings](https://clipno.app/dashboard/notion). Replace the example URL below with your own:

```bash
# Save to the linked Notion database
clipno save https://example.com --json

# Extract page content without writing to Notion
clipno extract https://example.com --markdown
```

You can use `npx clipno` instead of the globally installed `clipno` command. The original skill uses `npx -y clipno@latest` when the CLI is not installed.

`extract` does not require a linked Notion workspace, but still runs through the Clipno service; complete Clipno login as described by the project. `save` supports tags, notes, titles, transcription, OCR, and AI summaries. Some enrichment is added asynchronously and depends on account settings and quotas. Check the website for current plans and limits.

## Usage and Submission Guidelines

- Choose resources according to their dependencies: the OpenAI plugin uses its Notion integration; the community automation skill uses Rube MCP; Clipno uses its CLI and service; the template business skill provides strategic guidance.
- Verify tool availability and permission scope after installation. Installing a skill, connecting a service, and granting page or database access are separate steps.
- New entries should include original project and `SKILL.md` links, maintainer, purpose, supported clients, runtime and service dependencies, installation, and authorization instructions. For entries hosted in third-party collections, identify both the collection and its declared upstream source.
- Verification scope: upstream documentation, skill file availability, and described purposes have been checked. These skills and CLIs have not been installed or executed; account authorization, extraction quality, and Notion writes have not been tested.

Review date: 2026-11-09. Upstream directories, installation methods, and service plans may change; refer to the original projects for current instructions.
