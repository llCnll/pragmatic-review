Prioritize findings by severity:

- P0: likely broken behavior, data loss, or race
- P1: clear maintainability risk with future cost
- P2: cognitive complexity that materially impairs reasoning
- P3: evolution or architecture drift
- P4: observability or debugging weakness
- P5: obvious, practical performance waste
- P6: low-value cleanup

Report P0–P4 by default. Report P5 when the waste is obvious; report P6 only when cleanup feedback is requested.

Rank by user or operational risk, maintenance cost, strength of evidence, and correction cost, in that order.
