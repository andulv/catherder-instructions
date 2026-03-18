---
type: plan
description: "Plan 006 — CatHerder-enable catherder-dev following current standards, preserving experimental skills as reference only"
---
# Plan 006: CatHerder-Enable Catherder-Dev

**Status:** `draft`

**Branch:** `plan/006-catherder-enable-catherder-dev`

**Created:** 2026-03-06T09:00:00+01:00

**Updated:** 2026-03-06T09:00:00+01:00

## Goal

Bootstrap the catherder-dev project as a properly CatHerder-enabled project
following current standards, while preserving valuable legacy experimental
skills and guidance as reference material (not auto-migrated into `.instructions/`).

## Context / Why

Catherder-dev has a mature but outdated `.instructions/` setup (now moved to
`.instructions-legacy-outdated-but-may-contain-useful-info-instructions-experiments-to-build-on/`).
It contains sophisticated experimental skills (format validation, reference integrity checks)
that should be kept as reference/prototypes for future iteration, but not directly
carried into the new standards-compliant `.instructions/`.

Unlike Omnitrade (which had limited legacy content), catherder-dev's legacy
folder is complex and most of its specialized skills are prototypes/experiments,
not yet polished for reuse.

## What We Want To Achieve (Outcomes)

A standards-compliant CatHerder-enabled catherder-dev project with:

- `.instructions/` matching canonical minimum structure (with some project-specific extensions)
- `.agents/` directory (empty initially; experimental skills stay as reference, not migrated)
- All CatHerder process rules via standard instruction files
- Legacy experimental skills preserved as reference in a safe location (not `.instructions/`)
- Clear separation: "live" `.instructions/` vs "reference" legacy folder

End state — these files exist and are correct:

```
.instructions/
  SCRATCHPAD.md
  catherder.instructions.md          ← exact copy from repo/instructions/
  catherder-git.instructions.md      ← exact copy from repo/instructions/
  project-status-roadmap.md          ← new, based on current state
  project.instructions.md            ← new, project-specific only
  plans/                             ← directory exists
.agents/
  skills/                            ← directory exists (empty initially)
AGENTS.md                            ← minimal entry point
```

Legacy reference material:

- `.instructions-legacy-outdated-but-may-contain-useful-info-instructions-experiments-to-build-on/`
  - Skills remain here as prototypes/reference (not migrated)
  - May be pruned later after extraction of useful insight

## Summary Of Work Needed

**1. Scout legacy folder for useful project-level guidance**

Skim `.instructions-legacy-outdated-but-may-contain-useful-info-instructions-experiments-to-build-on/`
and extract any genuinely project-specific information (team structure, architectural
decisions, dev workflow preferences) that should go into new `.instructions/`.

Note: Skills folders are experimental — mark them as reference-only in scoping.

**2. Clarify project-specific architectural decisions and workflow**

Review legacy `project.INSTRUCTIONS.md`, `team.md`, and architecture notes to extract
project-specific guidance (what makes catherder-dev different from a standard setup?).
Document findings — this will inform `project.instructions.md`.

**3. Create `.instructions/` scaffold**

Standard minimal structure matching plan005 + this project's needs.

**4. Copy canonical instruction files**

Copy `catherder.instructions.md` and `catherder-git.instructions.md` verbatim
from `repo/instructions/`.

**5. Create project-specific instruction files**

- `project.instructions.md` — Identity, tech stack, dev workflow, architecture notes (no process duplication)
- `project-status-roadmap.md` — Phases, current focus, priorities (project phase: **Prototype**)
- `SCRATCHPAD.md` — Fresh current-session context

**6. Document legacy reference location**

Ensure `project.instructions.md` and/or SCRATCHPAD note that experimental
skills live in the legacy folder and how they might be revisited later.

**7. Review and scope legacy experimental skills**

Decide: keep legacy skills folder as-is, extract specific insights into docs,
or mark for eventual cleanup.

## Key Principles / Constraints

- Canonical instruction files are **exact copies** from `repo/instructions/` — no edits.
- Project-specific info goes in dedicated files; no duplication of process rules.
- Experimental skills (validation, audit, etc.) stay in legacy folder; don't auto-migrate.
- Legacy folder is a **reference**, not an active part of the new `.instructions/`.

## Open Questions

**Resolved:**
- ✓ Project phase: **Prototype** (experimental skills in legacy folder; focus on core catherder-dev work)
- ✓ Legacy plans/tasks: **Can be discarded** (start fresh with new plan/task numbering in `.instructions/plans/`)

**To resolve during execution:**
- Task 2: Extract project-specific architectural decisions/workflow practices from legacy folder → feed into `project.instructions.md`
- Task 7: Review legacy experimental skills; decide on reference strategy (keep as-is, extract insights, or prune)

## Notes

- Source prompt: `plan006-prompt.md`
- Legacy content: `.instructions-legacy-outdated-but-may-contain-useful-info-instructions-experiments-to-build-on/`
