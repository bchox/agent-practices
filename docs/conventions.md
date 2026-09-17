# Conventions

Use direct language, stable headings, and examples that work when copied. Keep root instructions under roughly 250 lines; put detailed material in linked files. State commands exactly, including working directory when relevant.

Rules should explain *why* when the reason affects a decision. Prefer "run the focused test, then the full suite before merge" over blanket, unverifiable instructions. Templates use placeholders in angle brackets, such as `<package-name>`.

Project profiles live at `templates/<name>/AGENTS.md`; the adoption helper discovers them automatically. Skill directories and their frontmatter names must match. Regenerate `catalog.json` after changing the version, a skill description, or the available skills and templates.
