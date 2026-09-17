---
name: database-changes
description: Use when changing a database schema, migration, query contract, index, or persisted data shape.
---

# Database changes

1. Identify supported database versions, data volume, deployment order, and whether old and new application versions overlap.
2. Prefer backward-compatible expand-and-contract changes. Separate destructive cleanup from the change that stops using old data.
3. Make migrations deterministic, restartable where practical, and observable. Avoid long locks; explain backfill and rollback behavior.
4. Test both a fresh database and an upgrade from the last supported schema. Review query plans for index-sensitive changes.

Done when deployment order is safe, existing data has a defined path, and recovery does not depend on guesswork.
