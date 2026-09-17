---
name: security
description: Use when the change touches auth, secrets, trust boundaries, or sensitive data.
---

# Security

1. Treat all external input as untrusted. Authorize on the server, not the client.
2. Never commit credentials, tokens, production dumps, or private URLs. Do not log secrets.
3. For auth, permission, or data-handling changes, name the threat and add a targeted test or review note.
4. Report suspected vulns privately per `SECURITY.md`. Do not weaken controls to green a test.

Done when new trust-boundary behavior is explicit and untrusted input cannot skip checks.
