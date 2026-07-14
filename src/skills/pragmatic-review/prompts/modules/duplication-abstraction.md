Focus:
- duplicated business logic
- repeated condition trees
- copy-paste branches drifting apart
- fake abstractions that add navigation cost

Prioritize:
- reuse only when it reduces complexity
- duplication tolerance when the abstraction would be harder to understand

Avoid:
- generic helpers that hide business meaning
- DRY for its own sake
- premature generalization from two simple call sites

