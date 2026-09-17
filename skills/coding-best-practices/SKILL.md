---
name: coding-best-practices
description: Use when implementing or refactoring application code in this repo.
---

# Coding best practices

1. Read the local architecture and neighboring files. Copy existing patterns; do not invent a second style.
2. Make the smallest change that satisfies the agreed requirement. Do not guess product behavior—stop and ask.
3. Preserve public interfaces unless the request changes them. Prefer existing dependencies.
4. Delete dead paths you created. Add focused tests. Run the commands in `AGENTS.md`.

Done when the behavior change is covered by a test and the documented checks pass.
