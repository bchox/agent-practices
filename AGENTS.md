# Repository operating contract

## Purpose

Maintain portable, high-signal guidance for humans and coding agents. This repository contains documentation and templates, not a product runtime.

## Working rules

- Read the relevant `docs/`, template, and skill before editing it.
- Preserve vendor neutrality. Describe capabilities, not endorsements.
- Prefer small, independently reviewable changes. Do not reformat unrelated files.
- Never add secrets, private repositories, customer data, or instructions to defeat safeguards.
- Update examples when a convention changes.

## Validation

Run `./scripts/check.sh` before proposing a change. It checks required files, skill metadata, template coverage, executable helpers, and trailing whitespace. If a check cannot run, say why in the pull request.

## Review bar

Every contribution needs a clear user problem, copy-pasteable guidance, and a safe default. Claims about a tool's behavior should link to its official documentation or be phrased as tool-agnostic advice.
