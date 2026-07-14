Prioritize what is worth saying.

Severity order:
- P0: likely bug, data loss, race, broken behavior
- P1: maintainability risk with clear future cost
- P2: cognitive complexity that materially hurts reasoning
- P3: evolution risk or architecture drift
- P4: observability or debugging weakness
- P5: obvious performance issue
- P6: low-value cleanup

Default threshold:
- report P0 to P4
- report P5 only when the waste is obvious
- suppress P6 unless the user explicitly asked for cleanup feedback

Tie-breakers:
1. user-visible or operational risk
2. long-term maintenance burden
3. ease of proving the issue from the diff
4. cost of the suggested change

