Look for nested or interleaved decisions, repeated mode checks, hidden ordering assumptions, and state that requires broad file-by-file simulation.

Classify the decisions as type dispatch, business policy, state aggregation, fixed mapping, or protection guards. Consult [branch structure](../../references/patterns/branch-complexity-patterns.md) when a demonstrated variation point needs redesign.

Favor direct flow, explicit state, and fewer simultaneous concepts. Verify unknown-value behavior, priority, errors, calls, and side effects when recommending structural changes. Use branch count as a measurement clue and substantiate findings with the decisions' actual complexity.
