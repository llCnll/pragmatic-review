Only output high-signal findings.

Default language:
- respond in Chinese unless the user explicitly asks for another language

Default finding cap:
- report at most 3 findings in normal review mode
- if additional P0 or P1 findings exist, allow them to exceed the cap
- in deep review mode, allow up to 5 findings before using the same severity override
- if nothing meets the threshold, output none

For each finding include:
1. Severity
2. Category
3. Location
4. Problem
5. Why it matters
6. Suggested improvement
7. Tradeoff
8. Estimated value: high / medium / low
9. Estimated impact

Rules:
- be concrete
- cite the changed location
- explain the failure mode or maintenance cost
- avoid vague warnings
- avoid speculative advice without evidence
- rank findings before truncating
- prefer dropping lower-value findings over compressing them into noise
- if nothing meets the threshold, say so clearly
