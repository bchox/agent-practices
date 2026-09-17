---
name: code-review
description: Use when reviewing a PR, diff, or proposed patch for merge risk.
---

# Code review

1. Read the stated intent, then the full diff and surrounding call sites. Confirm the change actually does what it claims.
2. Rank findings: correctness, security, regressions, missing tests, docs that now lie. Skip style nits that a formatter owns.
3. Each finding names file, risk, and a fix the author can apply. If nothing blocks merge, say so and list residual gaps.

Done when every blocking issue is concrete and you have either approved or requested specific changes.
