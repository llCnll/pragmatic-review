# Codex 使用说明

## 模型

当前仓库内部仍然使用三层模型：

1. 核心能力
- `pragmatic-review`

2. 范围模型
- `scope-uncommitted`
- `scope-staged`

3. 审查方向模型
- `lens-frontend`
- `lens-backend`
- `lens-reliability`
- `lens-architecture`

但是：
- **通过 clawhub/skillhub 安装后，对用户暴露的公开 skill 只保留一个：`pragmatic-review`**

也就是说：
- `scope-*` 和 `lens-*` 是内部模型、仓库文档和引用模式中的概念
- 不是公开并列 skill 产品

## 用户应该怎么用

如果已经通过 clawhub/skillhub 正确安装 `pragmatic-review`，直接使用自然语言指定：
- 范围
- 审查方向

推荐说法：

```text
使用 pragmatic-review 审查当前未提交改动，输出中文。
```

```text
使用 pragmatic-review 审查暂存区代码，输出中文。
```

```text
使用 pragmatic-review 按前端方向审查当前未提交改动，输出中文。
```

```text
使用 pragmatic-review 按后端方向审查当前未提交改动，输出中文。
```

```text
使用 pragmatic-review 按可靠性方向审查当前未提交改动，输出中文。
```

```text
使用 pragmatic-review 按架构方向审查当前未提交改动，输出中文。
```

## 为什么只保留一个公开 skill

因为更合理的产品形态是：
- 用户只需要记住一个 skill 名称
- 范围和方向通过自然语言指定
- 系统内部再做 scope / lens 路由

这样可以避免：
- 公开 skill 列表膨胀
- 用户记忆多个 skill 名
- 把内部模型错误暴露成外部操作面

## 零安装引用模式

如果你不想安装，仍然可以按仓库内的引用模型使用：
- core: `src/skills/pragmatic-review/SKILL.md`
- scope: `adapters/codex/scope-uncommitted.md`
- scope: `adapters/codex/scope-staged.md`
- lens: `adapters/codex/lens-frontend.md`
- lens: `adapters/codex/lens-backend.md`
- lens: `adapters/codex/lens-reliability.md`
- lens: `adapters/codex/lens-architecture.md`
- helper: `adapters/codex/reference-mode.md`

## 安装方式

后续以 clawhub/skillhub 安装为主。

发布到你的 registry 后：

```bash
npx clawhub install pragmatic-review --registry <registry-url>
```

如果本机已经配置默认 registry，也可以省略 `--registry`：

```bash
npx clawhub install pragmatic-review
```

`clawhub` 负责从 configured registry 安装 skill，并写入 Codex 可发现的 skill 目录。

当前仓库不再维护本地手工复制安装路径，避免它和 `publish/pragmatic-review` 发布包产生行为漂移。

发布包：
- `publish/pragmatic-review`

## 常用 Git 行为

```powershell
git status --short
git diff --cached
git diff
```

`git diff --cached` 只代表暂存区，不代表全部提交前改动。

