---
name: testing
description: Use when adding, repairing, selecting, or running tests for a behavior change.
---

# Testing

1. Write the smallest test that fails for the new or broken behavior, then make it pass.
2. Cover the happy path, one real failure path, and a boundary if the risk warrants it.
3. Prefer deterministic tests. Do not skip or loosen assertions to hide flakes without a written reason.
4. Run the commands in `AGENTS.md` and paste what actually ran.

Done when the required suite passed on this change, not on memory.
