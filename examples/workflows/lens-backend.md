# 后端方向 Workflow

## 适用场景

- 当前改动主要是 service、handler、job、持久化或业务流程代码
- 希望从后端流程稳定性和副作用控制角度看这次改动

## 推荐组合

- `pragmatic-review + scope-uncommitted + lens-backend`

## 重点关注

1. 副作用顺序是否合理
2. partial failure 路径是否清晰
3. transaction boundary 是否明确
4. observability 是否足够
5. workflow ownership 是否分散

## 不值得浪费时间的点

- 纯命名口味
- 没有维护收益的大改
- 没有证据支撑的抽象建议
