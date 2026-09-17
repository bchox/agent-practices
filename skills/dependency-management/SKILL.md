---
name: dependency-management
description: Add, remove, or update software dependencies with compatibility, supply-chain, lockfile, and migration checks.
---

# Dependency management

Confirm the dependency is necessary and compatible with the project's runtime and license policy. Prefer a maintained, narrowly scoped package over duplicating a large framework or adding an unmaintained convenience dependency.

Use the repository's package manager, update the lockfile in the same change, and review install scripts and major transitive changes. Read the upstream release and migration notes for major upgrades. Run the focused tests, full required suite, and a production build when the dependency affects bundling or deployment.

Never expose registry credentials or weaken integrity checks to complete an installation.
