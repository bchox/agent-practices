---
name: git-workflow
description: Prepare focused Git changes, commits, branches, and pull requests while preserving unrelated work and shared history.
---

# Git workflow

Use a focused branch and keep commits coherent. Inspect the working tree before editing; preserve unrelated user changes. Never force-push shared branches, rewrite history, or run destructive Git commands without explicit approval.

Before opening a pull request, review the diff for scope, generated files, secrets, and accidental formatting changes. Use an imperative commit subject that states the change.

Do not create remote branches, push, merge, tag, or publish a release unless the user requested the corresponding external action.
