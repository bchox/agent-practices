---
name: dependency-management
description: Use when adding, removing, upgrading, or pinning a package or lockfile.
---

# Dependency management

1. Confirm the package is necessary, maintained, and compatible with runtime and license rules.
2. Use this repo's package manager. Update the lockfile in the same change.
3. Read migration notes for major upgrades. Review install scripts and surprising transitive jumps.
4. Run focused tests, the required suite, and a production build if bundling or deploy is affected.

Done when the lockfile matches the manifest and no registry credentials leaked.
