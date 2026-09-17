---
name: debugging
description: Use when diagnosing a failure, crash, regression, or wrong result before fixing.
---

# Debugging

1. Reproduce the smallest failing case. Write actual vs expected.
2. Trace evidence (logs, tests, recent diffs). Separate root cause from symptoms.
3. Change one variable at a time. Add temporary logs only if you lack evidence; remove them unless they belong in ops.
4. If the request is diagnosis-only, stop at the cause. If a fix is in scope, add a regression test first.

Done when the cause is named with evidence, not a guess.
