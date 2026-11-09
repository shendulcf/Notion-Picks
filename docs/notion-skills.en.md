# Notion Skills Collection

[简体中文](notion-skills.md) | **English**

A skill is a set of instructions for an AI agent, usually stored in `SKILL.md` and supporting files. It can teach an agent to run a command-line tool (CLI) or connect to a service through MCP. After installing a skill, you still need the tools and accounts it uses.

[Back to README](../README.en.md#notion-skills)

- [OpenAI Notion Plugin](#openai-notion-plugin)
- [Community Skills (Unofficial)](#community-skills-unofficial)
- [Clipno CLI Companion Skill](#clipno-cli-companion-skill)
- [Usage and Submission Guidelines](#usage-and-submission-guidelines)

## OpenAI Notion Plugin

The [Notion plugin in openai/plugins](https://github.com/openai/plugins/tree/main/plugins/notion) includes these four skills. Connect and authorize Notion in a client that supports the plugin before using them.

| Skill | Use case | Purpose |
| :---- | :---- | :---- |
| [notion-knowledge-capture](https://github.com/openai/plugins/tree/main/plugins/notion/skills/notion-knowledge-capture) | Knowledge capture | Turn conversations and notes into Notion wiki entries, guides, FAQs, or decision records, linked to existing pages. |
| [notion-meeting-intelligence](https://github.com/openai/plugins/tree/main/plugins/notion/skills/notion-meeting-intelligence) | Meeting preparation | Use Notion context to prepare agendas, pre-reads, and decisions to discuss. |
| [notion-research-documentation](https://github.com/openai/plugins/tree/main/plugins/notion/skills/notion-research-documentation) | Research and documentation | Synthesize multiple Notion sources into cited briefs, comparisons, or research reports. |
| [notion-spec-to-implementation](https://github.com/openai/plugins/tree/main/plugins/notion/skills/notion-spec-to-implementation) | Implementation planning | Turn PRDs or feature specifications in Notion into implementation plans, tasks, and progress updates. |

[openai/skills](https://github.com/openai/skills) is deprecated; its replacement is `openai/plugins`. The links above point to the new directories. The old ones remain useful for reference, but follow the [plugin repository instructions](https://github.com/openai/plugins#readme) and your client’s documentation when installing. Older MCP configuration commands may no longer apply.

## Community Skills (Unofficial)

These skills are maintained by third parties. Client and dependency details come from their project documentation and have not been tested individually.

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

See the [community repository instructions](https://github.com/sickn33/antigravity-awesome-skills#readme) to install the first two skills. `notion-automation` needs Rube MCP. `notion-template-business` gives design and sales advice; it does not read or write Notion data.

## Clipno CLI Companion Skill

- [Repository](https://github.com/EwingYangs/clipno-cli) · [Website](https://clipno.app)
- [Original skill](https://github.com/EwingYangs/clipno-cli/blob/main/skills/clipno/SKILL.md)
- Category: third-party web clipping tool with both a CLI and an agent skill. Uses the Clipno service; Notion MCP is not required.

### Install the Skill

Run this in an environment supported by your client, then choose the installation target when prompted:

```bash
npx skills add EwingYangs/clipno-cli
```

This step installs the skill only. Set up the `clipno` CLI and account authorization separately. The project README also covers the Claude Code plugin marketplace and manual installation.

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

`extract` needs Clipno login but no linked Notion workspace. `save` also supports tags, notes, titles, transcription, OCR, and AI summaries. Enrichment may appear on the page later and depends on account settings and quotas. Check the website for current limits.

## Usage and Submission Guidelines

- Choose resources according to their dependencies: the OpenAI plugin uses its Notion integration; the community automation skill uses Rube MCP; Clipno uses its CLI and service; the template business skill provides strategic guidance.
- Verify tool availability and permission scope after installation. Installing a skill, connecting a service, and granting page or database access are separate steps.
- New entries should include original project and `SKILL.md` links, maintainer, purpose, supported clients, runtime and service dependencies, installation, and authorization instructions. For entries hosted in third-party collections, identify both the collection and its declared upstream source.
- These descriptions come from project documentation and accessible skill files. The tools have not been installed or run, and authorization, extraction quality, and Notion writes remain untested.

Sources reviewed on 2026-11-09. Installation instructions, directories, and plans can change; check the original project before setting up a tool.
