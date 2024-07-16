# Commit Convention Installer

这是一个一键运行的脚本，旨在自动生成规范化的 GitHub Commit 消息。
> [!IMPORTANT]
> 你的电脑里面必须有npm or pnpm 才能运行

## 特性

- **简化流程**：通过自动化配置，简化 commit 规范的实施过程。
- **灵活性**：支持 `git cz` 进行选项式提交，也支持 `git commit -m` 进行手动提交，增加了提交的灵活性。
- **规范化提交**：确保所有提交消息都符合预设的规范，有助于维护项目的清晰度和可追溯性。

## 快速开始

1. **克隆仓库**

   ```bash
   git clone https://github.com/lsewcx/commit-convention-installer.git
   pip install -r requirements.txt

   或者直接下载release包进行使用
2. **进行提交**
    使用 git cz 启动交互式提交界面。或者直接使用 git commit -m "你的提交信息"，提交信息需要符合预设的规范。


## 提交规范
### 提交类型

以下是我们项目中使用的一些常用的提交类型：

- **feat**：新增功能
- **fix**：修复问题
- **docs**：文档变更
- **style**：代码格式（不影响代码运行的变动）
- **refactor**：代码重构
- **perf**：性能优化
- **test**：添加或修改测试代码
- **chore**：对构建过程或辅助工具和库的更改

## 贡献指南

我们非常欢迎并鼓励社区的贡献！无论是功能请求、bug 修复还是文档改进，我们都欢迎您通过以下方式与我们分享：

- **Issue**：报告问题或提出新的想法
- **Pull Request**：提交您的代码更改

## TODO
- [ ] **python代码打包(Linux,MacOS,Windows)**
- [ ] **?可视化界面**

## 感谢以下开源项目
- husky
- cz-customizable

## 许可证

本项目采用 [MIT 许可证](https://opensource.org/licenses/MIT)。您可以自由地使用、复制、修改、合并、发布、分发、再授权和/或出售此软件及其文档的副本。

请尊重原作者的劳动成果，并在分发时保留版权声明和许可证声明。

