Trace expected rejection, configuration failure, dependency failure, and unexpected exceptions through their handling boundaries.

Check whether stable error semantics, field paths, and recoverability survive conversion, and whether one clear owner records the root cause with suitable correlation and redaction. Trace exception conversion to the serving boundary and verify the actual root-cause record.

For retries or partial success, identify the fact owner and successful checkpoints. Favor specific, proportional context that explains what failed with a clear logging owner and appropriately redacted fields.
