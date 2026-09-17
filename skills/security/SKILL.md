---
name: security
description: Review or implement changes involving trust boundaries, authentication, authorization, secrets, dependencies, or sensitive data.
---

# Security

Treat all external input as untrusted. Avoid logging secrets or personal data, validate authorization at the server boundary, and use least privilege. Do not commit credentials, tokens, production exports, or private URLs.

For dependency, authentication, data-handling, or permission changes, identify the threat model and include targeted tests or review notes. Escalate suspected vulnerabilities through the project's private reporting channel.

Never weaken authentication, authorization, transport security, input validation, or auditability merely to make a failing test pass.
