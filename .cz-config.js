

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
    