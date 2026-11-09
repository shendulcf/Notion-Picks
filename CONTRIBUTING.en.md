# Contribution Guide

[简体中文](CONTRIBUTING.md) | **English**

[Back to the directory](README.en.md)

Share tools you have found useful, correct an entry, improve a translation, or report a broken link.

## Adding a Resource

1. Check whether the resource is already listed, then choose a category for its main use. Link to that entry from other categories when needed.
2. Prefer the original website or repository and remove referral and tracking parameters.
3. Say what the tool does and what the reader needs to use it: a client, runtime, account, or deployment. Mention any payment requirement.
4. Identify official or community sources and label historical projects. If a product is paid despite having a public repository, say so.
5. Include the date and sources you checked, and say whether you tried the tool. If a page will not open, check whether the problem is the site or your network.

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

Keep purposes and requirements on the homepage and source details in the verification record. Label discontinued or unavailable resources, moving them to historical listings when needed.

The checker uses only the Python 3 standard library and works offline. GitHub Actions runs it when documentation changes are pushed or proposed in a pull request. It does not check external website availability or execute listed tools. `.editorconfig` standardizes encoding, indentation, and line endings.
