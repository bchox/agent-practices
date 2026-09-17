# <project-name> contributor and agent guide

## Commands

- Install: `<install-command>`
- Lint: `<lint-command>`
- Test: `<test-command>`
- Build: `<build-command>`

## Project map

Describe the main directories, public interfaces, and where tests live.

## Rules

- Make focused changes and preserve existing patterns.
- Add or update tests for behavior changes.
- Do not add secrets or unrelated generated files.
- Update documentation when interfaces, setup, or behavior changes.

## Skills

Task skills live in `.agents/skills/`. Delete any skill that does not change decisions here. Agents should load the matching skill for the current task.

## Definition of done

State the validation commands actually run and any remaining limitation in the pull request.
