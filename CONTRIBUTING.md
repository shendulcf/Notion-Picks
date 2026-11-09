# 贡献指南

**简体中文** | [English](CONTRIBUTING.en.md)

[返回目录](README.md)

欢迎分享用得顺手的工具，也欢迎纠错、补充翻译或报告失效链接。

## 新增资源

1. 先看看是否已经收录，再按主要用途选一个分类。其他分类需要提及时，链接到已有条目即可。
2. 链接到官网或原始仓库，去掉推广和追踪参数。
3. 写清楚它能做什么，再补充读者需要准备的东西，如客户端、运行环境、账号或部署。付费项目也请注明。
4. 标明官方或社区来源。历史项目要注明状态；仓库公开但产品收费的，也照实写。
5. 留下查阅日期和来源，并说明有没有试用。网页打不开时，先分清是网站问题还是自己的网络限制。

建议条目格式：

```markdown
| [项目名](https://example.com) | 一句话说明用途。 | 关键使用前提、来源或费用说明。 |
```

## 双语与文档结构

| 中文 | English | 内容 |
| :---- | :---- | :---- |
| [README.md](README.md) | [README.en.md](README.en.md) | 资源目录及选型入口 |
| [Notion Skills](docs/notion-skills.md) | [Notion Skills](docs/notion-skills.en.md) | Skills 详情、Clipno 安装与使用 |
| [核验记录](docs/resource-checks.md) | [Verification record](docs/resource-checks.en.md) | 来源、核验范围及暂未收录的原因 |
| [贡献指南](CONTRIBUTING.md) | [Contribution guide](CONTRIBUTING.en.md) | 收录与维护约定 |

新增或修改资源时同步两种语言的链接、依赖及核验状态。正文导航应留在当前语言，仅语言切换链接跳到另一版；项目名称、包名和可执行命令保持原文。

## 提交前检查

- 检查本地文件、图片、目录锚点和语言切换链接。
- 比对两种语言的资源列表与命令示例，避免漏译条目或改变命令。
- 运行 `python3 scripts/check_docs.py` 检查本地链接、表格、语言切换、双语资源与命令示例，再运行 `git diff --check`。
- 仅声明实际完成的核验；链接访问成功不等于工具可正常运行。

首页写用途和使用条件，查资料的细节放到核验记录。停更或失效的项目注明状态，需要时归入历史条目。

检查脚本仅使用 Python 3 标准库，可离线运行。文档变更推送或发起 Pull Request 后，GitHub Actions 会执行检查；它不会验证外站可用性或运行收录工具。`.editorconfig` 统一编码、缩进与换行。
