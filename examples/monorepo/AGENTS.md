# Atlas workspace guide

## Commands

- Install: `pnpm install --frozen-lockfile`
- Check affected packages: `pnpm turbo run lint test --filter=...[HEAD^1]`
- Test all: `pnpm turbo run lint test build`

## Repository map

- `apps/` contains deployable products.
- `packages/` contains versioned workspace libraries and services.
- `tooling/` contains shared build and lint configuration.

Nested `AGENTS.md` files add package-specific commands. Root rules always apply.

## Rules

- Import other workspaces through their public package exports.
- Keep lockfile changes tied to manifest changes.
- Update affected consumers when a shared contract changes.
- Do not commit environment files, generated build output, or production data.

## Definition of done

Affected checks pass during development; the full workspace build passes before merge.
