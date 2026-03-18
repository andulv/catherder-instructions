---
type: plan
description: "Plan 005 — CatHerder-enable the Omnitrade project following current standards"
---
# Plan 005: CatHerder-Enable Omnitrade

**Status:** `draft`

**Created:** 2026-03-05T13:00:00+01:00

**Updated:** 2026-03-05T13:00:00+01:00

## Goal

Bootstrap the Omnitrade project as a properly CatHerder-enabled project following
current standards, incorporating relevant project-specific content from the old
`.instructions-old-invalid-but-parts-might-be-useful/` folder.

## Context / Why

Omnitrade has an older, non-standard `.instructions/` setup (now moved to
`.instructions-old-invalid-but-parts-might-be-useful/`). The CatHerder standards
have evolved significantly since that setup was created. We need a clean
`.instructions/` that follows the current canonical structure while preserving
Omnitrade-specific technical knowledge.

## What We Want To Achieve (Outcomes)

A standard CatHerder-enabled Omnitrade project with:

- `.instructions/` directory matching canonical minimum structure
- `.agents/` directory (even if initially empty)
- All CatHerder process rules via standard instruction files
- Project-specific knowledge preserved in appropriate locations
- Old `.instructions-old-invalid-but-parts-might-be-useful/` safely superseded (can be deleted afterward)

End state — these files exist and are correct:

```
.instructions/
  SCRATCHPAD.md
  catherder.instructions.md          ← exact copy from repo/instructions/
  catherder-git.instructions.md      ← exact copy from repo/instructions/
  project-status-roadmap.md          ← new, based on old roadmap + current state
  project.instructions.md            ← new, project-specific only
  plans/                             ← directory exists (migrate old plans later if needed)
.agents/
  skills/                            ← directory exists (empty initially)
AGENTS.md                            ← minimal entry point
```

## Summary Of Work Needed

**1. Create scaffold (`AGENTS.md`, `.instructions/`, `.agents/`)**

Standard minimal entry point and directory structure.

**2. Copy canonical instruction files**

Copy `catherder.instructions.md` and `catherder-git.instructions.md` verbatim
from `repo/instructions/` in catherder-instructions-repo.

**3. Create `project.instructions.md` — project identity and tech stack**

Omnitrade-specific content only (no process duplication). Incorporate useful
content from the old files:

- From old `project/project.instructions.md`: identity, stack table, layout table,
  development rules (code-first, migration-first, snake_case convention).
- Keep it focused: what the project is, tech choices, repo layout, dev conventions.
- Reference `catherder.instructions.md` for all process rules.

**4. Create `project-status-roadmap.md` — phases and status**

Based on old `project/project-status-roadmap.md` but updated to reflect current
state. The old file has good structure — phase table, current focus, open
questions, needs-work backlog. Update statuses (many plans completed since then).

**5. Create domain-specific instruction files (optional, from old rules/)**

The old setup had two valuable rule files:
- `rules/database-migrations.instructions.md` — EF Core migration commands and workflow
- `rules/entity-design.instructions.md` — naming, EF config, and design principles

These contain genuinely useful, project-specific technical rules. Options:
- Include as separate files in `.instructions/` (e.g. `database.instructions.md`,
  `entity-design.instructions.md`)
- Or fold the critical rules into `project.instructions.md`

**6. Create `SCRATCHPAD.md`**

Fresh scratchpad reflecting current state. The old SCRATCHPAD has extensive
history — extract only what's relevant as current context (recent plan status,
current branch state, pending work).

**7. Verify and clean up**

- Confirm all files match CatHerder standards
- Confirm old `.instructions-old-invalid-but-parts-might-be-useful/` is fully
  superseded and can be deleted

## Key Principles / Constraints

- `catherder.instructions.md` and `catherder-git.instructions.md` are **exact
  copies** from `repo/instructions/` — no project-specific edits.
- `project.instructions.md` contains **only project-specific** content. All
  CatHerder process rules are already in `catherder.instructions.md`.
- Don't duplicate content between files. Cross-reference instead.
- Domain rule files (database, entity design) should use the `.instructions.md`
  extension and proper frontmatter.
- Old plans (002–012) are NOT migrated into `.instructions/plans/` in this plan.
  That's a separate decision.

## Open Questions

- [ ] Should old plans (002–012 from the previous setup) be migrated into
  `.instructions/plans/`? Or start fresh with new plan numbering?
- [ ] Should domain-specific rules (database migrations, entity design) be
  separate instruction files or folded into `project.instructions.md`?
- [ ] What is the current state of the Omnitrade git repo? (branch, last commit,
  pending changes) — needed for accurate SCRATCHPAD.

## Notes

- Source prompt: `plan005-prompt.md`
- Old instructions location: `/home/anders/source/omnitrade/.instructions-old-invalid-but-parts-might-be-useful/`
- Key content to preserve from old files:
  - Tech stack (.NET 10, EF Core 10, PostgreSQL, Npgsql, MudBlazor)
  - Entity naming rules (snake_case via convention, PK always `Id`, etc.)
  - Migration-first workflow with specific `dotnet-ef` commands
  - Phase definitions and current prototype status
  - Plan 008 context (nopCommerce import nuances — don't lose this)
