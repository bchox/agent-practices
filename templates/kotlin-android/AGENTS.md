# <app-name> Android guide

Use Kotlin and follow the module boundaries documented in this repository. Keep UI, domain, and data responsibilities separate; avoid placing business logic in Activities, Fragments, or Composables. Use existing dependency injection and state-management patterns.

Run `./gradlew test lint` and the focused Android instrumentation tests when applicable. Do not commit signing keys, `local.properties`, service configuration containing secrets, or device-specific files.

Task skills live in `.agents/skills/`.
