# Changelog

All notable changes are documented here. The project follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.4.0] - 2026-09-17

### Added

- Selective skill installation and discoverable template/skill listing
- Documentation, infrastructure, and monorepo project profiles
- Database-change and release-management skills
- A generated, versioned JSON catalog and schema for tooling
- A layered monorepo example showing scoped `AGENTS.md` contracts
- Public governance, support boundaries, CODEOWNERS, and adoption reports

### Changed

- Template discovery is dynamic, so new profiles do not require installer code changes
- CI pins third-party actions to immutable commits

## [0.3.0] - 2026-09-17

### Added

- `scripts/placeholders.sh` to list or fail on leftover `<placeholder>` tokens
- `Done when` lines and `Use when` descriptions on every skill
- Skills pointer in templates and the filled example

### Changed

- README leads with the failure mode this kit is for
- Adoption helper prints next steps and remaining placeholders
- Getting started requires a strict placeholder check before commit

## [0.2.0] - 2026-09-17

### Added

- A safe adoption helper with template selection and dry-run support
- Debugging and dependency-management skills
- Getting-started, compatibility, and skill-authoring guides
- A complete sample `AGENTS.md`

### Changed

- All skills now include discoverable YAML metadata
- Repository checks now validate skill structure and template placeholders

## [0.1.0] - 2026-09-17

### Added

- Initial repository contract, six skills, four templates, examples, community files, and CI

[Unreleased]: https://github.com/bchox/agent-practices/compare/v0.4.0...HEAD
[0.4.0]: https://github.com/bchox/agent-practices/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/bchox/agent-practices/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/bchox/agent-practices/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/bchox/agent-practices/releases/tag/v0.1.0
