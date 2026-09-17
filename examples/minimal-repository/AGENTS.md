# Tiny Notes contributor and agent guide

## Commands

- Install: `npm ci`
- Lint and type-check: `npm run check`
- Test: `npm test`
- Build: `npm run build`

## Project map

- `src/domain/` contains framework-independent note behavior.
- `src/web/` contains HTTP routes and presentation code.
- `tests/` mirrors `src/` and contains integration fixtures.

## Rules

- Keep domain code independent of the web framework.
- Validate request data at the route boundary.
- Add a regression test for every bug fix.
- Do not commit `.env`, build output, or fixture data copied from production.

## Definition of done

Run the focused test while developing, then `npm run check && npm test && npm run build` before review. Report any command that could not run and why.
