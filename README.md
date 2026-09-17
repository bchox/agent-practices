# Agent Practices

Practical, portable repository guidance for AI-assisted software development.

[![CI](https://github.com/bchox/agent-practices/actions/workflows/ci.yml/badge.svg)](https://github.com/bchox/agent-practices/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Agent Practices gives a project a clear operating contract: human maintainers retain ownership, coding agents get focused instructions, and contributions are verified before they land. It is intentionally vendor-neutral and works with Codex, OpenCode, Claude Code, and similar tools that can read repository files.

## What is included

- A root `AGENTS.md` contract and eight reusable task-focused skills
- Architecture and convention guides that scale from a small project to a team
- Starter templates for generic, Kotlin/Android, TypeScript, and Python repositories
- An example repository and GitHub issue, pull request, and CI defaults

## Quick start

Preview an installation into another repository:

```sh
git clone https://github.com/bchox/agent-practices.git
cd agent-practices
./scripts/adopt.sh --target ../your-project --template generic --dry-run
./scripts/adopt.sh --target ../your-project --template generic
```

The helper never overwrites an existing `AGENTS.md` unless you pass `--force`. You can also copy files manually. Then replace template placeholders with your real commands, architecture, scope boundaries, and review expectations.

See [Getting started](docs/getting-started.md) for a short adoption path and [Compatibility](docs/compatibility.md) for tool-specific discovery notes.

## Layout

```text
AGENTS.md                 shared contributor and agent contract
skills/                   reusable, task-specific guidance
templates/                starting points by ecosystem
examples/minimal-repository/  small, complete integration example
docs/                     principles and architecture
```

## Principles

1. Instructions are versioned alongside the code.
2. Agents make narrow, reviewable changes and never invent product requirements.
3. Tests, linting, and documentation are part of the change—not cleanup work.
4. Secrets, private data, and generated credentials never enter prompts or commits.
5. Human reviewers remain accountable for merge decisions.

## Compatibility

This project uses plain Markdown and conventional repository files. Some tools discover `AGENTS.md` automatically; others may need it referenced in their own configuration. The guidance remains useful in either case.

## Project status

Agent Practices is early but usable. The current focus is stable skill packaging, realistic examples, and lightweight validation. See the [roadmap](ROADMAP.md) and [changelog](CHANGELOG.md).

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), and [SECURITY.md](SECURITY.md). Released under the [MIT License](LICENSE).
