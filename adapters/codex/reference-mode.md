# Codex 引用模式

在不安装的情况下，仓库内部仍然按 `core + scope + optional lens` 工作：

- core: `src/skills/pragmatic-review/SKILL.md`
- scope: `adapters/codex/scope-uncommitted.md`
- scope: `adapters/codex/scope-staged.md`
- lens: `adapters/codex/lens-frontend.md`
- lens: `adapters/codex/lens-backend.md`
- lens: `adapters/codex/lens-reliability.md`
- lens: `adapters/codex/lens-architecture.md`

## 自然语言命中原则

最稳的句式：
- `按<方向>审查<范围>`

例如：
- `按后端方向审查当前未提交改动`
- `按架构方向审查暂存区代码`
- `按可靠性方向审查整个仓库代码`

## 默认审查

```text
请以 <repo-root>/src/skills/pragmatic-review/SKILL.md 作为核心 review 能力，
并使用 <repo-root>/adapters/codex/scope-uncommitted.md 作为范围模型，
审查当前工作区未提交改动。
输出中文。
```

## 只审查暂存区

```text
请以 <repo-root>/src/skills/pragmatic-review/SKILL.md 作为核心 review 能力，
并使用 <repo-root>/adapters/codex/scope-staged.md 作为范围模型，
只审查当前暂存区改动。
输出中文。
```

## 前端视角

```text
请以 <repo-root>/src/skills/pragmatic-review/SKILL.md 作为核心 review 能力，
并使用 <repo-root>/adapters/codex/scope-uncommitted.md 作为范围模型，
再叠加 <repo-root>/adapters/codex/lens-frontend.md 作为审查方向，
审查当前工作区未提交改动。
输出中文。
```

## 后端视角

```text
请以 <repo-root>/src/skills/pragmatic-review/SKILL.md 作为核心 review 能力，
并使用 <repo-root>/adapters/codex/scope-uncommitted.md 作为范围模型，
再叠加 <repo-root>/adapters/codex/lens-backend.md 作为审查方向，
审查当前工作区未提交改动。
输出中文。
```

## 可靠性视角

```text
请以 <repo-root>/src/skills/pragmatic-review/SKILL.md 作为核心 review 能力，
并使用 <repo-root>/adapters/codex/scope-uncommitted.md 作为范围模型，
再叠加 <repo-root>/adapters/codex/lens-reliability.md 作为审查方向，
审查当前工作区未提交改动。
输出中文。
```

## 架构视角

```text
请以 <repo-root>/src/skills/pragmatic-review/SKILL.md 作为核心 review 能力，
并使用 <repo-root>/adapters/codex/scope-uncommitted.md 作为范围模型，
再叠加 <repo-root>/adapters/codex/lens-architecture.md 作为审查方向，
审查当前工作区未提交改动。
输出中文。
```

