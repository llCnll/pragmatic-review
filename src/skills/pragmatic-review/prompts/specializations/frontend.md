Focus:
- duplicated derived state
- effect complexity
- hidden lifecycle coupling
- rerender cascades
- prop and state synchronization risk
- UI logic that is hard to debug

Check:
- whether state has one clear source of truth
- whether effects are doing coordination that should be modeled directly
- whether component boundaries reduce or increase mental load

