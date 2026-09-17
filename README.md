# Agent Practices

Stop coding agents from freestyling your repo.

One `AGENTS.md` contract plus short task skills. Humans own merge. Agents get commands, boundaries, and a definition of done. Vendor-neutral: Codex, Claude Code, OpenCode, or anything that can read Markdown.

[![CI](https://github.com/bchox/agent-practices/actions/workflows/ci.yml/badge.svg)](https://github.com/bchox/agent-practices/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## You know it worked when

An agent finds `AGENTS.md`, runs **your** lint/test commands, stays out of the wrong directories, and the PR is reviewable without a second rewrite.

## Install into a project

```sh
git clone --depth 1 https://github.com/bchox/agent-practices.git
cd agent-practices
./scripts/adopt.sh --target /path/to/your-project --template typescript --dry-run
./scripts/adopt.sh --target /path/to/your-project --template typescript
```

Templates: `generic` · `typescript` · `python` · `kotlin-android`

The helper will not overwrite an existing `AGENTS.md` unless you pass `--force`. After copy it lists leftover `<placeholders>`. Fill those before you commit. Drop unused skills under `.agents/skills/`.

Filled example: [`examples/minimal-repository/AGENTS.md`](examples/minimal-repository/AGENTS.md).

## What you get

| Piece | Job |
| --- | --- |
| `AGENTS.md` | Commands, map, rules, done criteria |
| `skills/` | Eight task skills with **Use when** + **Done when** |
| `templates/` | Starting contracts per stack |
| `scripts/adopt.sh` | Safe copy + dry-run |
| `scripts/placeholders.sh` | Fail CI if you still shipped `<lint-command>` |

## Principles

1. Instructions live next to the code, versioned.
2. Agents make narrow changes. They do not invent product requirements.
3. Tests, lint, and docs ship in the same change.
4. Secrets never enter prompts or commits.
5. A human still merges.

## Compatibility

Plain Markdown. Some tools auto-load `AGENTS.md`; others need a one-line pointer. See [Compatibility](docs/compatibility.md).

## Status

Early, usable. Next: real adopted repos, Windows notes, link checks. [Roadmap](ROADMAP.md) · [Changelog](CHANGELOG.md)

## Contributing

[CONTRIBUTING.md](CONTRIBUTING.md) · [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) · [SECURITY.md](SECURITY.md) · [MIT](LICENSE)
