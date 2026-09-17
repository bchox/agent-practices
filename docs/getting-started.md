# Getting started

Adopt the smallest useful subset and make it **true** for your repository. Empty placeholders are worse than no contract.

## 1. Choose a template

- `generic` — any repo
- `kotlin-android` — Android / Kotlin
- `typescript` — Node/TS apps and libraries
- `python` — Python apps and packages

Git Bash or WSL on Windows. Native `cmd.exe` is untested.

```sh
./scripts/adopt.sh --target /path/to/project --template typescript --dry-run
./scripts/adopt.sh --target /path/to/project --template typescript
```

## 2. Kill the placeholders

Replace every `<placeholder>` with commands that work from a **fresh checkout**. Document directories agents must not touch.

```sh
./scripts/placeholders.sh --strict /path/to/project
```

That command should exit 0 before you commit `AGENTS.md`.

## 3. Cut skills you will not use

The helper copies all skills into `.agents/skills/`. Delete the ones that never change a decision. Keep the rest short.

## 4. Prove it with one task

Ask the agent for a small, reviewable change. Check:

- Did it find `AGENTS.md`?
- Did it run the real commands?
- Did it stay in bounds?
- Did the PR report what actually ran?

Fix the contract from that failure. Do not add hypothetical rules.

See [Compatibility](compatibility.md) if the tool did not load the files.
