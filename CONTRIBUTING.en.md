# Contribution Guide

[简体中文](CONTRIBUTING.md) | **English**

[Back to the directory](README.en.md)

Contributions can add useful resources, update project status, improve translations, or report broken links.

## Adding a Resource

1. Search existing entries and choose the category matching the primary use case. Cross-link other categories instead of duplicating descriptions.
2. Prefer the original website or repository and remove referral and tracking parameters.
3. Describe the purpose in one sentence, then include requirements that affect selection: clients, runtimes, authorization, deployment, or commercial terms.
4. Distinguish official projects, community tools, paid services, and historical resources. A public repository does not mean the product is free.
5. Record the review date, source evidence, and scope. Reading a README, reaching a website, and testing functionality are different results. A proxy denial does not establish that a website is offline.

Suggested entry format:

```markdown
| [Project name](https://example.com) | One-sentence purpose. | Key requirements, source, or pricing notes. |
```

## Languages and Document Structure

| 中文 | English | Content |
| :---- | :---- | :---- |
| [README.md](README.md) | [README.en.md](README.en.md) | Resource directory and selection guide |
| [Notion Skills](docs/notion-skills.md) | [Notion Skills](docs/notion-skills.en.md) | Skill details and Clipno setup and usage |
| [核验记录](docs/resource-checks.md) | [Verification record](docs/resource-checks.en.md) | Sources, verification scope, and reasons for deferring candidates |
| [贡献指南](CONTRIBUTING.md) | [Contribution guide](CONTRIBUTING.en.md) | Selection and maintenance conventions |

Update links, dependencies, and verification status in both languages when changing resources. Keep navigation in the current language except for explicit language-switch links; preserve project names, package names, and executable commands.

## Before Submitting

- Check local files, images, section anchors, and language-switch links.
- Compare resource lists and command examples across languages to catch omissions or altered commands.
- Run `python3 scripts/check_docs.py` to check local links, table structure, language switches, resource parity, and shell examples; then run `git diff --check`.
- Claim only checks that were completed; a reachable link does not establish that a tool works.

Keep detailed verification notes in the verification record and decision-relevant information in the directory. Label discontinued or unavailable resources and move them to historical listings when appropriate.

The checker uses only the Python 3 standard library and works offline. GitHub Actions runs it when documentation changes are pushed or proposed in a pull request. It does not check external website availability or execute listed tools. `.editorconfig` standardizes encoding, indentation, and line endings.
