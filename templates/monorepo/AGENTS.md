# <project-name> monorepo guide

## Commands

- Install: `<install-command>`
- Check affected packages: `<affected-check-command>`
- Test all: `<full-test-command>`

## Repository map

List workspace roots, shared packages, ownership boundaries, generated outputs, and how dependency direction is enforced.

## Instruction scope

This root file defines shared rules. A nested `AGENTS.md` may add commands and constraints for its subtree. Read the root and the closest nested file before editing; the more specific instruction applies within its scope unless it weakens a root safety boundary.

## Rules

- Limit changes and checks to affected packages while developing; run the required integration suite before review.
- Do not introduce cross-package imports that bypass public package interfaces.
- Update consumers when a shared contract changes.

## Skills

Task skills live in `.agents/skills/`. Delete any skill that does not change decisions here.

## Definition of done

Affected-package checks pass, integration impact is documented, and the diff contains no unrelated workspace or lockfile churn.
