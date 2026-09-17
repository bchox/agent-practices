---
name: release-management
description: Use when preparing a version, changelog, tag, release artifact, or public software release.
---

# Release management

1. Confirm the intended version and included commits from repository history; do not infer approval to publish from approval to prepare.
2. Update version sources and changelog together. Describe user-visible changes, migrations, and known limitations without marketing claims.
3. Run the documented release checks and inspect generated artifacts for secrets, unexpected files, and reproducibility.
4. Create tags, releases, or uploads only when explicitly authorized. Verify the published version and links after release.

Done when version metadata agrees everywhere, checks pass, and any external publication is verified at its destination.
