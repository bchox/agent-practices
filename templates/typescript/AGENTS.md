# <project-name> TypeScript guide

Preserve strict typing; do not introduce `any` to bypass an error. Keep runtime validation at external boundaries and use the project's package manager and formatter. Add unit tests beside the affected behavior when that is the local convention.

Run `<typecheck-command>`, `<lint-command>`, and `<test-command>` before review. Do not change lockfiles unless dependencies changed.
