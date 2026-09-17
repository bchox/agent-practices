# Getting started

Adopt the smallest useful subset and make it true for your repository.

## 1. Choose a template

- `generic` for any repository
- `kotlin-android` for Android projects
- `typescript` for TypeScript applications and libraries
- `python` for Python applications and packages

Run the helper from this repository:

```sh
./scripts/adopt.sh --target /path/to/project --template typescript --dry-run
./scripts/adopt.sh --target /path/to/project --template typescript
```

## 2. Customize the contract

Replace every `<placeholder>`. Document commands that work from a fresh checkout, the directories that define architectural boundaries, and any files that agents must not modify.

## 3. Select skills

The helper installs all skills under `.agents/skills/`. Remove skills that do not affect decisions in your project. Add repository-specific references only when they prevent repeated rediscovery.

## 4. Verify with a real task

Ask your coding agent to make a small, reviewable change. Check whether it found the contract, ran the correct commands, respected boundaries, and reported validation clearly. Improve the guidance based on observed gaps rather than hypothetical ones.
