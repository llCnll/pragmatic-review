# 架构方向 Workflow

## 适用场景

- 当前改动引入了新层、共享 helper、跨模块依赖或基础模式
- 希望从长期演进和边界控制角度看这次改动

## 推荐组合

- `pragmatic-review + scope-uncommitted + lens-architecture`

## 重点关注

1. boundary drift
2. ownership confusion
3. fake abstraction
4. helper / base-layer explosion
5. future diff complexity

## 不值得浪费时间的点

- clean architecture 教条
- 没有实际收益的新层级
