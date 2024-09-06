import subprocess
import json
import logging
from rich.console import Console
import platform
import sys  # 导入sys模块以支持退出功能

__AUTHOR__ = 'liushien'

class __VERSION__:
    def __init__(self) -> None:
        self.__version = (0, 0, 0)
    
    def __str__(self):
        return 'v'+'.'.join(map(str, self.__version))

CONSOLE = Console()
logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)

PACKAGE_MANAGERS = {
    'Windows': {'npm': 'npm.cmd', 'pnpm': 'pnpm.cmd'},
    'default': {'npm': 'npm', 'pnpm': 'pnpm'}
}
SUPPORT_PLATFORM=['Windows',"Darwin"]

def check_package_manager_installed(manager:str,os_system='default') -> bool:
    cmd = PACKAGE_MANAGERS.get(os_system, PACKAGE_MANAGERS['default']).get(manager, manager)
    try:
        subprocess.run([cmd, '--version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        CONSOLE.print(f"[red]{cmd} 未安装或找不到路径[/red]")
        return False

def modify_package_json() -> None:
    CONSOLE.log("[bold green]开始读取并修改package.json文件[/bold green]")
    try:
        with open('package.json', 'r') as file:
            data = json.load(file)
        data['config'] = {"commitizen": {"path": "node_modules/cz-customizable"}}
        with open('package.json', 'w') as file:
            json.dump(data, file, indent=4)
        CONSOLE.log("[bold green]package.json文件更新完成[/bold green]")
    except Exception as e:
        LOG.error(f"修改package.json时出错: {e}")
        config_content = "..."  # 这里填写你的config_content
        with open('.cz-config.js', 'w', encoding='utf-8') as file:  # 指定编码为utf-8
            file.write(config_content)
        CONSOLE.log("[bold green].cz-config.js文件创建完成[/bold green]")

def run_command(command:str, success_message:str, failure_message:str) -> None:
    try:
        subprocess.run(command, check=True, shell=True)
        CONSOLE.print(success_message, style="green")
    except subprocess.CalledProcessError:
        CONSOLE.print(failure_message, style="red")

def install_dependencies_and_setup_hooks(package_manager:str) -> None:
    dependencies = "commitizen cz-customizable conventional-changelog-cli cz-conventional-changelog --save-dev"
    husky_init_command = f"{package_manager} exec husky init" if package_manager != "npm" else "npx husky init"
    commit_msg_hook_command = f'echo "npx --no -- commitlint --edit $1" > .husky/commit-msg'
    
    run_command(f"{package_manager} add {dependencies}", f"{dependencies} 安装成功", f"{dependencies} 安装失败")
    if(package_manager == "pnpm"):
        run_command('pnpm add --save-dev husky', 'husky 安装成功', 'husky 安装失败')
        run_command('pnpm add --save-dev @commitlint/config-conventional', '@commitlint/config-conventional 安装成功', '@commitlint/config-conventional 安装失败')
    else:
      run_command('npm install --save-dev husky', 'husky 安装成功', 'husky 安装失败')
      run_command('npm install --save-dev @commitlint/config-conventional', '@commitlint/config-conventional 安装成功', '@commitlint/config-conventional 安装失败')
    run_command(husky_init_command, 'husky init成功', 'husky init失败')
    run_command(commit_msg_hook_command, "pre-commit 钩子设置成功", "pre-commit 钩子设置失败")

def create_cz_config_js() ->None:
    CONSOLE.log("[bold green]开始创建.cz-config.js文件[/bold green]")
    config_content = """

module.exports = {
    // type 类型
    types: [
      { value: 'feat', name: '✨ feat:     新增产品功能' },
      { value: 'fix', name: '🐛 fix:      修复 bug' },
      { value: 'docs', name: '📚 docs:     文档的变更' },
      {
        value: 'style',
        name: '💅 style:    不改变代码功能的变动(如删除空格、格式化、去掉末尾分号等)',
      },
      {
        value: 'refactor',
        name: '🛠 refactor: 重构代码。不包括 bug 修复、功能新增',
      },
      {
        value: 'perf',
        name: '⚡️ perf:     性能优化',
      },
      { value: 'test', name: '🚨 test:     添加、修改测试用例' },
      {
        value: 'build',
        name: '📦️ build:    构建流程、外部依赖变更，比如升级 npm 包、修改 webpack 配置',
      },
      { value: 'ci', name: '👷 ci:       修改了 CI 配置、脚本' },
      {
        value: 'chore',
        name: '🔨 chore:    对构建过程或辅助工具和库的更改,不影响源文件、测试用例的其他操作',
      },
      { value: 'revert', name: '⏪ revert:   回滚 commit' },
      { value: 'workflow', name: '🔁 workflow: 工作流程变动' },
      { value: 'mod', name: '🔧 mod:      不确定分类的修改' },
      { value: 'wip', name: '🚧 wip:      开发中' },
      { value: 'types', name: '🏷️ types:    类型修改' },
      { value: 'release', name: '🚀 release:  版本发布' },
    ],
    scopes: [
      ['new', '新增功能'],
      ['components', '组件相关'],
      ['hooks', 'hook 相关'],
      ['hoc', 'HOC'],
      ['utils', 'utils 相关'],
      ['antd', '对 antd 主题的调整'],
      ['styles', '样式相关'],
      ['deps', '项目依赖'],
      ['auth', '对 auth 修改'],
      ['other', '其他修改'],
      ['doc', '文档修改'],
      ['test', '测试用例'],
      ['build', '构建过程'],
      ['release', '发布版本'],
      ['workflow', '工作流相关'],
      ['ci', '持续集成'],
      ['types', '类型定义文件更改'],
      ['lint', '代码风格'],
      ['i18n', '国际化'],
      ['revert', '回退'],
      ['custom', '以上都不是？我要自定义'],
    ].map(([value, description]) => {
      return {
        value,
        name: `${value.padEnd(30)} (${description})`
      };
    }),
    messages: {
      type: "请确保你的提交遵循了原子提交规范！选择你要提交的类型:",
      scope: '选择一个 scope (可选):',
      customScope: '请输入自定义的 scope:',
      subject: '填写一个简短精炼的描述语句:',
      body: '添加一个更加详细的描述，可以附上新增功能的描述或 bug 链接、截图链接 (可选)。使用 "|" 换行:',
      breaking: '列举非兼容性重大的变更 (可选):',
      footer: '列举出所有变更的 ISSUES CLOSED  (可选)。 例如.: #31, #34:',
      confirmCommit: '确认提交?',
    },
    allowBreakingChanges: ['feat', 'fix'],
    subjectLimit: 100,
  };
    """
    try:
        with open('.cz-config.js', 'w') as file:
            file.write(config_content)
        CONSOLE.log("[bold green].cz-config.js文件创建完成[/bold green]")
    except Exception as e:
        LOG.error(f"创建.cz-config.js文件时出错,尝试使用utf-8写入")
        CONSOLE.print(f"[red]{e}[/red]")
        with open('.cz-config.js', 'w',encoding='utf-8') as file:
            file.write(config_content)
        CONSOLE.log("[bold green].cz-config.js文件创建完成[/bold green]")

def write_commitlint_config() -> None:
    CONSOLE.log("[bold green]开始创建commitlint.config.js文件[/bold green]")
    config_content = """
module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'type-enum': [
      2,
      'always',
      [
        'feat', // 新功能(feature)
        'fix', // 修补bug
        'docs', // 文档(documentation)
        'style', // 格式、样式(不影响代码运行的变动)
        'refactor', // 重构(即不是新增功能，也不是修改BUG的代码)
        'perf', // 优化相关，比如提升性能、体验
        'test', // 添加测试
        'ci', // 持续集成修改
        'chore', // 构建过程或辅助工具的变动
        'revert', // 回滚到上一个版本
        'workflow', // 工作流改进
        'mod', // 不确定分类的修改
        'wip', // 开发中
        'types', // 类型修改
        'release' // 版本发布
      ]
    ],
    'subject-full-stop': [0, 'never'],
    'subject-case': [0, 'never']
  }
}
"""

    with open('commitlint.config.js', 'w') as file:
        file.write(config_content)
    CONSOLE.log("[bold green]commitlint.config.js文件创建完成[/bold green]")

def clear_pre_commit_hook() -> None:
    try:
        # 打开文件并清空内容
        with open('.husky/pre-commit', 'w') as file:
            file.write('')  # 写入空字符串以清空文件
        CONSOLE.log("[bold green].husky/pre-commit 文件内容已清空[/bold green]")
    except Exception as e:
        LOG.error(f"清空 .husky/pre-commit 文件时出错:")
        CONSOLE.print(f"[red]{e}[/red]")

def main():
    if platform.system() not in SUPPORT_PLATFORM:
        CONSOLE.print("[red]不支持的操作系统[/red]")
        CONSOLE.print("不清楚是否支持你的操作系统？可以尝试运行脚本")
        system='default'
    else:
        system=platform.system()
    CONSOLE.print(f"检测到你的操作系统为[bold green]{system}[/bold green]")
    CONSOLE.print(f"版本: [bold magenta]{__VERSION__()}[/bold magenta], 作者: [bold cyan]{__AUTHOR__}[/bold cyan]")
    package_manager = CONSOLE.input('[bold green]选择你使用的包管理器(npm/pnpm): [/bold green]')
    if check_package_manager_installed(package_manager,os_system=system):
        install_dependencies_and_setup_hooks(package_manager)
        modify_package_json()
        write_commitlint_config()
        create_cz_config_js()
        clear_pre_commit_hook()
        CONSOLE.log("[bold green]脚本执行结束[/bold green]")
        CONSOLE.input("[bold green]按任意键退出...[/bold green]")  # 添加等待用户输入以暂停
        sys.exit(0)  # 正常退出程序
    else:
        LOG.error('输入错误或包管理器未安装')

if __name__ == '__main__':
    main()
