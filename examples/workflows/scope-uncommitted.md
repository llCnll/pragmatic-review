# 工作区未提交改动 Workflow

## 适用场景

- 提交前审查当前工作区里的未提交改动
- 希望覆盖已暂存和未暂存的改动
- 需要一个默认、通用、低心智负担的入口

## 推荐组合

- `pragmatic-review + scope-uncommitted`

## 路由行为

1. 用 `git status --short` 确认当前有改动
2. 用 `git diff --cached` 看已暂存部分
3. 用 `git diff` 看未暂存部分
4. 如果当前改动需要额外关注点，再叠加某个 `lens-*`
5. 如果没有值得说的问题，就明确不输出低价值反馈

## 可叠加的审查方向

- `lens-frontend`
- `lens-backend`
- `lens-reliability`
- `lens-architecture`

## 相关示例

- `scope-staged`
- `lens-frontend`
- `lens-backend`
- `lens-reliability`
- `lens-architecture`
- `lens-backend-reliability`
