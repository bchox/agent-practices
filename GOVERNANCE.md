# Governance

Agent Practices is maintained in public by [@bchox](https://github.com/bchox). Maintainers are responsible for issue triage, review quality, releases, security coordination, and the long-term coherence of the project.

## Decisions

Small, reversible changes are decided through pull-request review. Changes to the catalog schema, project direction, compatibility promises, or security posture should begin with an issue so tradeoffs are visible before implementation.

Decisions favor observed repository needs, vendor neutrality, safe defaults, and instructions that can be verified. Popularity alone does not justify adding a rule or integration.

## Maintainers

Regular contributors may be invited as maintainers after demonstrating sound judgment across multiple contributions. Maintainers disclose relevant conflicts, do not approve their own security-sensitive changes without another reviewer when one is available, and may step down at any time.

If the sole maintainer becomes inactive for 90 days, established contributors may open a public stewardship issue proposing a new maintainer or an orderly archival plan.

## Releases

Releases follow semantic versioning. A release must have a changelog entry, matching `VERSION` and catalog metadata, a passing default-branch CI run, and a signed or annotated Git tag.
