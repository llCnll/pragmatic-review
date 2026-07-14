# Pragmatic Review

`pragmatic-review` 是一个面向 AI coding agents 的务实代码审查 skill。

它的目标不是输出更长的 checklist，而是让 AI review 更接近务实的 senior engineer：高信号、低噪音、少废话、少 nitpick，优先关注长期可维护性、认知复杂度、未来 bug 风险和演进风险。

## 谁应该看

如果你只是使用这个 skill：
- 只需要安装 `pragmatic-review`
- 不需要理解仓库内部的 `scope-*` 或 `lens-*`
- 用自然语言告诉 AI 要审查什么范围、按什么方向审查即可

如果你要维护或发布这个 skill：
- 修改源码目录 `src/skills/pragmatic-review`
- 通过脚本生成发布目录 `publish/pragmatic-review`
- 上传或发布 `publish/pragmatic-review` 对应的运行时包

## 安装使用

通过 SkillHub / ClawHub 安装：

```bash
npx clawhub install pragmatic-review --registry <registry-url>
```

如果你的环境已经配置了默认 registry，也可以省略 `--registry`：

```bash
npx clawhub install pragmatic-review
```

安装后，在 Codex 或支持 skills 的 AI coding agent 中直接这样说：

```text
审查当前未提交改动
```

```text
审查暂存区代码
```

```text
按前端方向 review
```

```text
按后端方向 review
```

```text
按可靠性方向 review
```

```text
按架构方向审查暂存区代码
```

更明确的写法：

```text
使用 pragmatic-review 按架构方向审查暂存区代码，输出中文。
```

## 范围和方向

默认范围是“当前未提交改动”。

当前未提交改动包括：
- 已暂存改动
- 未暂存的 tracked 文件改动
- 和当前工作相关、可直接读取的 untracked 文件

明确说“暂存区代码”时，只审查暂存区：

```bash
git diff --cached
```

审查方向可以自然语言指定：
- 前端方向：状态、effect、生命周期、渲染链路、组件边界
- 后端方向：副作用顺序、失败路径、事务边界、服务耦合
- 可靠性方向：幂等、重试、回滚、部分失败、可观测性
- 架构方向：边界漂移、ownership、依赖方向、假抽象、过度设计

内部模型里这些方向叫 `lens-*`，范围叫 `scope-*`。它们只是内部路由概念，不是需要用户单独安装或记忆的 skill。

## 输出风格

默认输出中文。

审查原则：
- 只输出真正值得修的问题
- 优先 bug 风险、维护风险、认知复杂度和演进风险
- 不做低价值样式评论
- 不建议为了抽象而抽象
- 不做微优化
- 宁可少说，也不要输出低信号建议

普通模式默认最多输出最值得修的 3 条问题；如果存在额外 P0/P1 问题，可以超过这个上限。需要更完整审查时，可以明确说：

```text
做一次 deep review
```

## 仓库结构

```text
.
├── src/
│   ├── skills/pragmatic-review/
│   ├── model/
│   └── profiles/
├── publish/
│   └── pragmatic-review/
├── adapters/
├── docs/
├── examples/
├── scripts/
└── dist/
```

关键目录：
- `src/skills/pragmatic-review/`：源码真相，维护时改这里
- `publish/pragmatic-review/`：生成后的运行时 skill 包，发布时用这里
- `dist/pragmatic-review-0.1.0.zip`：可上传到 SkillHub 页面的 zip 包
- `adapters/`：不同平台的适配参考
- `examples/`：中文自然语言用法示例
- `docs/`：框架设计、平台说明、扩展策略

## 发布方式

如果只是普通使用者，不需要看这一节。

维护者发布前先构建并校验：

```bash
python scripts/build-publish-package.py
python scripts/validate-preset-parity.py
```

验证发布包内容：

```bash
cd publish/pragmatic-review
npm pack --dry-run --json
```

发布目录是：

```text
publish/pragmatic-review
```

SkillHub 页面要求上传 zip 时，应上传：

```text
dist/pragmatic-review-0.1.0.zip
```

这个 zip 的根目录应直接包含：

```text
SKILL.md
package.json
agents/openai.yaml
prompts/
```

不要把整个仓库打包上传，也不要把外层 `publish/pragmatic-review` 文件夹再包一层。

## 维护约束

这个仓库遵循：
- 对外只暴露一个 skill：`pragmatic-review`
- `scope-*` 和 `lens-*` 只作为内部组合模型
- 源码和发布物分离
- 发布物由脚本生成，不手工维护
- 文档和规格优先于实现
- 高风险能力必须有最小验证方式

常用文档：
- [框架概览](docs/framework-overview.md)
- [审查框架规格](docs/review-framework-spec.md)
- [平台适配说明](docs/platform-matrix.md)
- [目录结构](docs/directory-structure.md)
- [自然语言速查表](examples/workflows/natural-language-cheatsheet.md)
