# Agent Practices

Practical, portable repository guidance for AI-assisted software development.

Agent Practices gives a project a clear operating contract: human maintainers retain ownership, coding agents get focused instructions, and contributions are verified before they land. It is intentionally vendor-neutral and works with Codex, OpenCode, Claude Code, and similar tools that can read repository files.

## What is included

- A root `AGENTS.md` contract and reusable task-focused skills
- Architecture and convention guides that scale from a small project to a team
- Starter templates for generic, Kotlin/Android, TypeScript, and Python repositories
- An example repository and GitHub issue, pull request, and CI defaults

## Quick start

Copy the parts that fit your project; do not blindly adopt every rule.

```sh
git clone https://github.com/bchox/agent-practices.git
cp agent-practices/templates/generic/AGENTS.md ./AGENTS.md
cp -R agent-practices/skills ./.agents/skills
```

Then tailor `AGENTS.md` with your commands, architecture, scope boundaries, and review expectations. Keep it short enough to remain useful and link to deeper documentation.

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

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), and [SECURITY.md](SECURITY.md). Released under the [MIT License](LICENSE).
