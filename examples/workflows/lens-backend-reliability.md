# 后端 + 可靠性组合 Workflow

## 适用场景

- 当前改动既是后端流程改动，又明显涉及可靠性风险
- 比如写路径、异步任务、外部系统调用、失败恢复逻辑

## 推荐组合

- `pragmatic-review + scope-uncommitted + lens-backend + lens-reliability`

## 重点关注

1. broken or partial failure path
2. hidden side-effect ordering
3. rollback 或 retry weakness
4. observability gap
5. workflow complexity growth

## 约束

- 没有具体失败路径，不要泛泛地报可靠性问题
