# Layered monorepo example

This example shows scope without duplicating every rule:

```text
AGENTS.md
packages/
└── api/
    └── AGENTS.md
```

The root contract applies everywhere. The nested contract adds commands and boundaries for `packages/api/`. It does not weaken root safety rules.
