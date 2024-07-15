import subprocess
import json
import logging
from rich.console import Console

__VERSION__=(0,0,0)
__AUTHOR__='liushien'

# 创建Rich的Console实例
console = Console()

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)

def check_package_managers():
    managers = {
        'npm': False,
        'pnpm': False
    }
    
    try:
        subprocess.run(['npm', '--version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        managers['npm'] = True
    except subprocess.CalledProcessError:
        pass
    
    try:
        subprocess.run(['pnpm', '--version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        managers['pnpm'] = True
    except subprocess.CalledProcessError:
        pass
    
    return managers


def add_config_to_package_json():
    console.log("[bold green]开始读取并修改package.json文件[/bold green]")
    # 读取package.json文件
    with open('package.json', 'r') as file:
        data = json.load(file)
    
    # 添加或更新config部分
    data['config'] = {
        "commitizen": {
            "path": "node_modules/cz-customizable"
        }
    }

    
    # 写回修改后的数据到package.json
    with open('package.json', 'w') as file:
        json.dump(data, file, indent=4)
    console.log("[bold green]package.json文件更新完成[/bold green]")

def create_cz_config_js():
    console.log("[bold green]开始创建.cz-config.js文件[/bold green]")
    config_content = """
module.exports = {
  // type 类型
  types: [
    { value: 'feat', name: 'feat:     新增产品功能' },
    { value: 'fix', name: 'fix:      修复 bug' },
    { value: 'docs', name: 'docs:     文档的变更' },
    {
      value: 'style',
      name:
        'style:    不改变代码功能的变动(如删除空格、格式化、去掉末尾分号等)',
    },
    {
      value: 'refactor',
      name: 'refactor: 重构代码。不包括 bug 修复、功能新增',
    },
    {
      value: 'perf',
      name: 'perf:     性能优化',
    },
    { value: 'test', name: 'test:     添加、修改测试用例' },
    {
      value: 'build',
      name: 'build:    构建流程、外部依赖变更，比如升级 npm 包、修改 webpack 配置'
    },
    { value: 'ci', name: 'ci:       修改了 CI 配置、脚本' },
    {
      value: 'chore',
      name: 'chore:    对构建过程或辅助工具和库的更改,不影响源文件、测试用例的其他操作',
    },
    { value: 'revert', name: 'revert:   回滚 commit' },
  ],
  scopes: [
    ['components', '组件相关'],
    ['hooks', 'hook 相关'],
    ['hoc', 'HOC'],
    ['utils', 'utils 相关'],
    ['antd', '对 antd 主题的调整'],
    ['styles', '样式相关'],
    ['deps', '项目依赖'],
    ['auth', '对 auth 修改'],
    ['other', '其他修改'],
    ['custom', '以上都不是？我要自定义'],
  ].map(([value, description]) => {
    return {
      value,
      name: `${value.padEnd(30)} (${description})`
    };
  }),
  messages: {
    type: "请确保你的提交遵循了原子提交规范！\\n选择你要提交的类型:",
    scope: '\\n选择一个 scope (可选):',
    customScope: '请输入自定义的 scope:',
    subject: '填写一个简短精炼的描述语句:\\n',
    body: '添加一个更加详细的描述，可以附上新增功能的描述或 bug 链接、截图链接 (可选)。使用 "|" 换行:\\n',
    breaking: '列举非兼容性重大的变更 (可选):\\n',
    footer: '列举出所有变更的 ISSUES CLOSED  (可选)。 例如.: #31, #34:\\n',
    confirmCommit: '确认提交?',
  },
  allowBreakingChanges: ['feat', 'fix'],
  subjectLimit: 100,
};
"""
    with open('.cz-config.js', 'w') as file:
        file.write(config_content)
    console.log("[bold green].cz-config.js文件创建完成[/bold green]")

def write_commitlint_config():
    console.log("[bold green]开始创建commitlint.config.js文件[/bold green]")
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
    console.log("[bold green]commitlint.config.js文件创建完成[/bold green]")

def install_dependencies(package_manager):
    console = Console()

    # 定义一个辅助函数来运行命令并打印结果
    def run_command(command, success_message, failure_message):
        try:
            subprocess.run(command, check=True,shell=True)
            console.print(success_message, style="green")
        except subprocess.CalledProcessError:
            console.print(failure_message, style="red")

    # 安装commitizen和commitlint
    run_command(package_manager + " install cz-customizable", "cz-customizable 安装成功", "cz-customizable 安装失败")
    run_command(package_manager + " install --save-dev @commitlint/cli @commitlint/config-conventional", "@commitlint/cli 和 @commitlint/config-conventional 安装成功", "@commitlint/cli 和 @commitlint/config-conventional 安装失败")
  
    
    # 根据包管理器设置husky pre-commit钩子
    if package_manager == "pnpm":
        run_command('pnpm add --save-dev husky', 'husky 安装成功', 'husky 安装失败')
        run_command('pnpm exec husky init','husky init成功','husky init失败')
        command = 'echo "pnpm dlx commitlint --edit \\$1" > .husky/commit-msg'
        run_command(command, "pnpm pre-commit 钩子设置成功", "pnpm pre-commit 钩子设置失败")
    elif package_manager == "npm":
        run_command('npm install --save-dev husky', 'husky 安装成功', 'husky 安装失败')
        run_command('npx husky init', 'husky init成功', 'husky init失败')
        command = 'echo "npx --no -- commitlint --edit \\$1" > .husky/commit-msg'
        run_command(command, "npm pre-commit 钩子设置成功", "npm pre-commit 钩子设置失败")
    with open('.husky/pre-commit', 'w') as file:
      file.write('')
    


if __name__ == '__main__':
    console.print(f"版本: [bold magenta]{__VERSION__}[/bold magenta], 作者: [bold cyan]{__AUTHOR__}[/bold cyan]")
    managers = check_package_managers()
    for manager, installed in managers.items():
      if installed:
          console.print(f"[green]{manager} 已安装[/green]")
      else:
          console.print(f"[red]{manager} 未安装[/red]")
    package = console.input('[bold green]选择你使用的包管理器(npm/pnpm): [/bold green]')
    if package in ['npm', 'pnpm']:
        install_dependencies(package)
    else:
        LOG.error('输入错误')
    add_config_to_package_json()
    create_cz_config_js()
    write_commitlint_config()
    console.log("[bold green]脚本执行结束[/bold green]")

