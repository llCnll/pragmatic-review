# 暂存区 Workflow

## 适用场景

- 只想审查已经 `git add` 的改动
- 希望把 review 范围严格限制在暂存区
- 想把“准备提交”的那部分改动单独过一遍

## 推荐组合

- `pragmatic-review + scope-staged`

## 路由行为

1. 用 `git diff --cached` 获取暂存区改动
2. 明确忽略未暂存改动
3. 如果暂存区为空，明确停止
4. 如果这批暂存改动需要额外关注点，再叠加某个 `lens-*`

## 可叠加的审查方向

- `lens-frontend`
- `lens-backend`
- `lens-reliability`
- `lens-architecture`
