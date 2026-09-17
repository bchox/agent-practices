---
name: code-review
description: Review a proposed code change for concrete correctness, security, regression, maintainability, testing, and documentation risks.
---

# Code review

Review for correctness, security, regressions, maintainability, test coverage, and documentation—not style preferences alone. Read the surrounding code and confirm that the change's stated outcome is actually achieved.

Prioritize findings by impact. Each finding should name the concrete risk, affected location, and a practical remedy. If no blocking issue exists, summarize residual risks and validation gaps.

Do not report hypothetical style concerns as defects. Verify that a reported issue is introduced or exposed by the change and is actionable for the author.
