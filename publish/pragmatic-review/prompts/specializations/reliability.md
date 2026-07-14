Focus:
- idempotency
- retry safety
- rollback safety
- timeout and cancellation handling
- sequencing of external side effects

Check:
- whether the change is safe under duplicate execution
- whether failure leaves the system in a confusing partial state
- whether operators can tell what happened

