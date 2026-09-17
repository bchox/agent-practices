# API package guidance

Run package tests with `pnpm --filter @atlas/api test`. Database integration tests require the repository's documented test container.

Keep transport validation in `src/http/` and business rules in `src/domain/`. Schema changes require the `database-changes` skill, an upgrade test, and deployment-order notes in the pull request.

Do not run migrations against shared or production databases from an agent task.
