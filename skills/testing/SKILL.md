---
name: testing
description: Design, add, repair, or run software tests with coverage proportional to the behavior and regression risk.
---

# Testing

Start with the smallest test that exercises the changed behavior, then run the project's required suite. Include normal behavior, failure behavior, and boundary cases appropriate to the risk. Prefer deterministic tests; do not hide failures by loosening assertions or skipping tests without a documented reason.

Report the commands run and their results in the pull request.

## Test selection

- Unit-test deterministic logic and error handling.
- Use integration tests for boundaries such as storage, networking, and process interaction.
- Add end-to-end coverage only for critical user journeys that lower-level tests cannot prove.
- Reproduce a bug with a failing test before fixing it when practical.
