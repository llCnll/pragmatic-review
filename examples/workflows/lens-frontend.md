# 前端方向 Workflow

## 适用场景

- 当前改动主要是 UI、hooks、组件或状态管理逻辑
- 希望从前端可维护性视角看这次改动

## 推荐组合

- `pragmatic-review + scope-uncommitted + lens-frontend`

## 重点关注

1. source of truth 是否清晰
2. effect 是否过度复杂
3. 生命周期耦合是否隐蔽
4. 调试成本是否偏高
5. 是否存在明显 rerender 浪费

## 不值得浪费时间的点

- 纯格式问题
- CSS 审美偏好
- 没有实质收益的组件拆分建议
