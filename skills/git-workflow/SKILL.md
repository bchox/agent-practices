---
name: git-workflow
description: Use when branching, committing, or opening a pull request for this change.
---

# Git workflow

1. Inspect the working tree first. Do not clobber unrelated user edits.
2. Use a focused branch. Commits are coherent; subject is imperative and true.
3. Review the diff for secrets, generated junk, and drive-by formatting.
4. Do not force-push shared branches, rewrite published history, push, merge, or tag unless asked.

Done when the PR diff matches the requested scope and nothing private is in it.
