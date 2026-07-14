# 可靠性方向 Workflow

## 适用场景

- 当前改动涉及重试、异步任务、外部集成、hotfix 或显式副作用
- 希望从故障恢复和运行稳定性角度看这次改动

## 推荐组合

- `pragmatic-review + scope-uncommitted + lens-reliability`

## 重点关注

1. 幂等风险
2. retry safety
3. rollback safety
4. timeout / cancellation handling
5. operator visibility

## 约束

- 没有具体失败路径，不要轻易报可靠性问题
