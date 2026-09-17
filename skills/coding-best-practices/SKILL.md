---
name: coding-best-practices
description: Implement or refactor application code with focused scope, local architectural consistency, and proportional validation.
---

# Coding best practices

Use this skill when implementing or refactoring code. First identify the local architecture, public interfaces, and existing patterns. Make the smallest change that satisfies the agreed requirement. Keep behavior, types, error handling, and observability consistent with adjacent code.

Before finishing, remove dead paths created by the change, add focused tests, and run the repository's documented checks. Flag ambiguity instead of guessing about product behavior.

## Decision points

- Preserve public behavior unless the request explicitly changes it.
- Prefer existing dependencies and abstractions unless they are the source of the problem.
- Treat generated files as outputs: change their source and regenerate them.
- Document migrations and compatibility breaks where consumers will see them.
