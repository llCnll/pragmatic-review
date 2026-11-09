Focus:
- partial failure paths
- transaction boundary confusion
- hidden write ordering assumptions
- API contract drift
- ownership of business logic spanning layer boundaries

Check:
- what happens after the first side effect succeeds and the next one fails
- whether the diff increases debugging difficulty
- whether responsibilities stay in the right layer
