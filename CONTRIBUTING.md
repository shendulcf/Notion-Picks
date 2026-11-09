# 贡献指南

**简体中文** | [English](CONTRIBUTING.en.md)

[返回目录](README.md)

欢迎新增实用资源、更新项目状态、修正翻译和反馈失效链接。

## 新增资源

1. 搜索现有条目，选择最符合主要用途的分类；跨分类时使用内部链接，避免重复描述。
2. 优先链接项目官网或原始仓库，移除推广和追踪参数。
3. 用一句话说明用途，补充会影响选择的前提：适用客户端、运行时、授权、部署要求或商业属性。
4. 区分官方项目、社区工具、付费服务和历史资源；公开仓库不代表产品免费。
5. 记录核验日期、证据来源与范围。读过 README、官网可访问和实际功能测试是不同结果；不能把代理拒绝访问当成网站失效。

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

详细核验说明放在核验记录中，目录保留影响选型的关键信息。停更或失效资源应标注状态，必要时移入历史条目。

检查脚本仅使用 Python 3 标准库，可离线运行。文档变更推送或发起 Pull Request 后，GitHub Actions 会执行检查；它不会验证外站可用性或运行收录工具。`.editorconfig` 统一编码、缩进与换行。
