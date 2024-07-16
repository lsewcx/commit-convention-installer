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

## 错误排查

遇到问题时，请首先查看以下常见错误及其解决方案。如果你的问题未在此列出，或者提供的解决方案无效，请通过[Issue](https://github.com/lsewcx/commit-convention-installer/issues)报告新问题。

### 常见错误及解决方案

#### 1. npm 或 pnpm 未安装

**错误信息**：`npm: command not found` 或 `pnpm: command not found`

**解决方案**：确保你的电脑上已安装npm或pnpm。你可以访问[npm官网](https://www.npmjs.com/get-npm)或[pnpm官网](https://pnpm.io/installation)获取安装指南。

#### 2. git cz 启动失败

**错误信息**：`git: 'cz' is not a git command`

**解决方案**：查看安装时是否有库没有安装成功，可以尝试手动安装或者是再次运行脚本。
#### 3. 如果提示初始化失败或者是package.json没有
怀疑是npm并没有安装成功，npm出现了问题，目录下查看是否有package.json文件如果没有则是npm出现问题

### 报告新问题

如果你遇到了未列出的问题，或者提供的解决方案无效，请通过创建新的[Issue](https://github.com/lsewcx/commit-convention-installer/issues)来报告问题。在报告问题时，请尽可能详细地描述你遇到的问题，包括错误信息、你尝试过的解决方案，以及问题出现的上下文信息。这将帮助我们更快地诊断并解决问题。

## TODO
- [ ] **python代码打包(Linux,MacOS,Windows)**
- [ ] **?可视化界面**

## 感谢以下开源项目
- husky
- cz-customizable

## 许可证

本项目采用 [MIT 许可证](https://opensource.org/licenses/MIT)。您可以自由地使用、复制、修改、合并、发布、分发、再授权和/或出售此软件及其文档的副本。

请尊重原作者的劳动成果，并在分发时保留版权声明和许可证声明。

