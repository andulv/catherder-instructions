# PR Summary — CatHerder-enable Omnitrade (plan005)

## Overview

This change CatHerder-enables the Omnitrade repository by adding the current
standard `.instructions/` structure + minimal `AGENTS.md` entry point, and by
migrating the useful project-specific technical guidance from the legacy
`.instructions-old-invalid-but-parts-might-be-useful/` folder.

Work was performed on Omnitrade branch: `plan/005-catherder-enable-omnitrade`.

## What Changed

### Added (Omnitrade)

- `AGENTS.md` — entry point stating the repo is CatHerder-enabled and the reading order.
- `.instructions/` (new)
  - `catherder.instructions.md` — canonical template (verbatim copy)
  - `catherder-git.instructions.md` — canonical template (verbatim copy)
  - `project.instructions.md` — Omnitrade-specific identity/stack/layout (no process duplication)
  - `project-status-roadmap.md` — Omnitrade phases + current focus
  - `SCRATCHPAD.md` — minimal current-session notes
  - `database-migrations.instructions.md` — migrations-first workflow + `dotnet-ef` commands
  - `entity-design.instructions.md` — naming + EF config rules
  - `plans/` — created (tracked via `.gitkeep`)
- `.agents/skills/` — created (tracked via `.gitkeep`)

### Preserved (Omnitrade)

- Legacy folder retained as source material:
  - `.instructions-old-invalid-but-parts-might-be-useful/`

## Canonical Compliance

- `catherder.instructions.md` and `catherder-git.instructions.md` are copied
  verbatim from catherder-instructions-repo `repo/instructions/`.
- Project-specific information is concentrated in `project.instructions.md` and
  the two domain rules files; process rules remain in `catherder.instructions.md`.

## Commits (Omnitrade)

1. `task005-01: add CatHerder scaffold`
   - Added `AGENTS.md`
   - Added `.instructions/` canonical rule files

2. `task005-02: add Omnitrade instruction set`
   - Added project-specific instruction files + domain rules + `.gitkeep` markers

3. `task005-03: align AGENTS reading order`
   - Adjusted reading order to match canonical guidance (`SCRATCHPAD → catherder → roadmap → project`)

## How To Review

- Start at `AGENTS.md`.
- Confirm `.instructions/` contains the required minimum structure.
- Spot-check:
  - `project.instructions.md` contains only Omnitrade specifics.
  - `database-migrations.instructions.md` and `entity-design.instructions.md` match the intended technical rules.
- Confirm legacy folder is not referenced as the active instruction source.

## Follow-ups / Not Done Here

- Decide what to do with `.instructions-old-invalid-but-parts-might-be-useful/`:
  - keep for reference, or delete once the new `.instructions/` is trusted.
- Decide whether to migrate historical plans from the old folder into the new `.instructions/plans/`.
