# Authoring a skill

Each skill is a directory containing `SKILL.md`. Its YAML frontmatter makes discovery cheap:

```yaml
---
name: focused-skill-name
description: Use when <the request that should load this skill>.
---
```

Start the description with `Use when`. End the body with a `Done when` line. The rest is numbered steps that change decisions. Assume ordinary software skill.

Use `references/` for substantial detail needed only in certain modes, `scripts/` for deterministic repeated operations, and `assets/` for material copied into outputs. Do not add empty scaffolding.

Run `./scripts/check.sh` after adding or changing a skill.
