# Agent compatibility

Agent Practices stores guidance as plain Markdown so it remains portable. Discovery behavior varies by tool and version; consult the tool's current official documentation when configuring automatic loading.

| Tool | Recommended entry point |
| --- | --- |
| Codex | Root `AGENTS.md`; reusable skills in a configured skills location |
| OpenCode | Reference the root contract from the project's instruction configuration when it is not discovered automatically |
| Claude Code | Keep `AGENTS.md` as the shared source and point tool-specific project guidance to it |
| Other agents | Load `AGENTS.md` as project context and select task skills from `.agents/skills/` |

Avoid maintaining divergent copies of the same rules. A small tool-specific pointer is preferable to duplicating the full contract.
