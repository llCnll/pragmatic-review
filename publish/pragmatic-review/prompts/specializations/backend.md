Focus:
- partial failure paths
- transaction boundary confusion
- hidden write ordering assumptions
- API contract drift
- business logic split across layers without clear ownership

Check:
- what happens after the first side effect succeeds and the next one fails
- whether the diff increases debugging difficulty
- whether responsibilities stay in the right layer

