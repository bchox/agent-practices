# <project-name> infrastructure guide

## Commands

- Format: `<format-command>`
- Validate: `<validate-command>`
- Plan: `<plan-command>`
- Test: `<test-command>`

## Environment boundaries

List modules, environments, state backends, deployment order, and the owners who approve production changes.

## Rules

- Treat plans as evidence, not authorization to apply.
- Never commit state, credentials, private keys, production exports, or decrypted secrets.
- Pin providers and actions according to repository policy; review destructive replacements and permission expansion.
- Do not apply, deploy, rotate credentials, or change remote state unless explicitly requested and authorized.

## Skills

Task skills live in `.agents/skills/`. Prefer `security`, `code-review`, `testing`, and `dependency-management` for this profile.

## Definition of done

Formatting and validation pass, the plan is reviewed for destructive or privilege changes, and no remote mutation occurred outside the requested scope.
