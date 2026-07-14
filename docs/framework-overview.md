# AI Review Framework

This repository contains a modular, maintainability-first AI code review framework.

Default behavior:
- Review current uncommitted changes when the user does not explicitly specify another range.
- Use two orthogonal internal axes: scope and optional review lens.
- Prefer silence over low-value feedback.
- Optimize for maintainability, debuggability, and future change safety.

Framework layers:
1. `src/skills/pragmatic-review/prompts/core/`: stable worldview, scope model, prioritization, output contract
2. `src/skills/pragmatic-review/prompts/routing/`: select modules based on change shape, domain, and risk
3. `src/skills/pragmatic-review/prompts/modules/`: focused review lenses by problem type
4. `src/skills/pragmatic-review/prompts/specializations/`: reusable frontend, backend, reliability, architecture, performance overlays
5. `src/skills/pragmatic-review/` and `src/model/`: self-contained source skill plus internal scope/lens model
6. `adapters/`: platform-specific wrappers and reference files

Mental model:
- `pragmatic-review` = the only public skill product
- `scope-*` = internal label for which changes to review
- `lens-*` = internal label for how to bias the review
- `publish/pragmatic-review/` = generated installable package, not the source of truth

Public usage should normally be natural language, for example:
- `使用 pragmatic-review 审查当前未提交改动，输出中文。`
- `使用 pragmatic-review 按架构方向审查暂存区代码，输出中文。`

Start here:
- Spec: [review-framework-spec.md](review-framework-spec.md)
- Routing: [../src/skills/pragmatic-review/prompts/routing/review-router.md](../src/skills/pragmatic-review/prompts/routing/review-router.md)
- Profile registry: [../src/profiles/review-profiles.yaml](../src/profiles/review-profiles.yaml)
- Scope model: [../src/model/scopes.md](../src/model/scopes.md)
- Lens model: [../src/model/lenses.md](../src/model/lenses.md)
- Platform notes: [platform-matrix.md](platform-matrix.md)

