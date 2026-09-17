# Authoring a skill

Each skill is a directory containing `SKILL.md`. Its YAML frontmatter makes discovery cheap:

```yaml
---
name: focused-skill-name
description: What the skill does and the concrete requests that should activate it.
---
```

The body should contain only guidance that changes decisions: important constraints, a useful workflow, and links to conditional references. Assume the agent already understands ordinary software development.

Use `references/` for substantial detail needed only in certain modes, `scripts/` for deterministic repeated operations, and `assets/` for material copied into outputs. Do not add empty scaffolding.

Run `./scripts/check.sh` after adding or changing a skill.
