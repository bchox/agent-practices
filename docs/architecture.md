# Architecture

Agent Practices is a documentation-first toolkit with four layers:

1. **Contract** — `AGENTS.md` sets project-wide scope, safety boundaries, commands, and review expectations.
2. **Skills** — discoverable, focused guidance for a specific activity such as testing or security.
3. **Templates** — ecosystem-aware starting points that teams customize.
4. **Examples** — complete, small combinations proving the pieces work together.

The layers intentionally depend only on Markdown conventions. A coding agent may load all or selected files; human contributors can use the same material without an agent.

`scripts/adopt.sh` is a convenience layer, not a package manager. It copies a selected contract and the current skills into a target repository, makes no network requests, and refuses to replace an existing contract by default.
