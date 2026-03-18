---
type: plan
description: "Plan 008 — Create the catherder-repo-syncer skill for comparing and recommending sync of CatHerder instruction assets between repositories"
---
# Plan 008: Create catherder-repo-syncer Skill

**Status:** `completed`

**Branch:** `plan/008-catherder-repo-syncer-skill`

**Created:** 2026-03-11T00:00:00+00:00

**Updated:** 2026-03-11T02:15:00+00:00

## Goal

Create a reusable `catherder-repo-syncer` skill that helps agents compare CatHerder instruction assets across repositories, classify differences safely, and recommend intentional sync actions without assuming every difference should be copied.

## Context / Why

CatHerder instruction assets evolve in both directions:

- downstream projects often improve local instructions, skills, or agents that should be considered for upstreaming into `catherder-instructions-repo`
- the central `catherder-instructions-repo` also evolves and those improvements often need to be evaluated for propagation into downstream CatHerder-enabled projects
- some files are canonical defaults, some are expected local adaptations, and some are operational/local-only and should not be blindly synchronized

This comparison work is currently ad hoc. A dedicated skill should make it repeatable, scoped, and agent-safe by defining exactly what files are in scope, how to compare them, how to classify file roles, how to judge canonical vs local improvements, and how to present sync recommendations without making unsafe assumptions.

Plan 007 established useful upstreaming patterns that should shape this work:

- inventory first
- distinguish canonical defaults from optional or repository-local artifacts
- trace source-of-truth versus derived artifacts
- record unresolved policy gaps instead of guessing
- separate comparison/reporting from modification

## Tasks

- [x] Task 1: Inventory existing repository guidance, relevant canonical docs, and current skill patterns that should shape `catherder-repo-syncer`. Classify what is directly reusable versus repo-local context. Output: short inventory note in the plan folder.
- [x] Task 2: Define the sync-surface model for root `AGENTS.md`, `.instructions/`, and `.agents/`, including file-role classifications such as canonical/shared, locally adaptable, local-only/operational, and unresolved/needs-human-decision. Output: sync-surface classification note.
- [x] Task 3: Define the skill contract and decision model: triggers/non-triggers, supported repo-pair scenarios, comparison workflow, evaluation heuristics for newer/better/canonical/project-specific, recommendation categories, and compare-vs-sync safety boundaries. Output: decision note.
- [x] Task 4: Define the recommended reporting format for comparison output, including diff inventory, directional sync recommendations, ambiguity flags, and rationale fields. Output: reporting-format note or embedded reference content.
- [x] Task 5: Author `repo/skills/catherder-repo-syncer/SKILL.md` and any self-contained supporting references needed by the skill. Output: skill files created.
- [x] Task 6: Review the new skill against repository skill standards and fix any issues found. Output: review results recorded and skill adjusted if needed.
- [ ] Task 7: Verify that the final skill reflects Plan 007 lessons and known ambiguity areas, then record completion notes, limitations, and follow-up recommendations. Output: verification/completion note.

## Acceptance Criteria

- [x] A standards-compliant skill exists under `repo/skills/catherder-repo-syncer/`.
- [x] The skill explicitly supports both comparison modes:
  - `catherder-instructions-repo` ↔ one CatHerder-enabled project
  - one CatHerder-enabled project ↔ another CatHerder-enabled project
- [x] The skill scope explicitly covers only root `AGENTS.md`, `.instructions/`, and `.agents/` unless the user requests otherwise.
- [x] The skill instructs agents to begin with inventory and sync-surface classification before making sync recommendations.
- [x] The skill distinguishes at least these decision classes: `sync A → B`, `sync B → A`, `merge manually`, `do not sync`, and `needs canonical decision`.
- [x] The skill defines practical heuristics for judging whether a difference is likely canonical improvement, local customization, operational/local-only content, or unresolved ambiguity.
- [x] The skill explicitly treats `SCRATCHPAD.md` as local/operational and warns against blindly syncing it.
- [x] The skill explicitly identifies `.agents/agents/agents.yaml` as unresolved/needs-human-decision unless canonical guidance later changes.
- [x] The skill separates compare/report mode from actual sync/edit mode and requires explicit user intent before editing target repositories.
- [x] The skill provides a consistent output structure for findings, rationale, and suggested sync direction.
- [ ] Validation script execution is still pending in this environment; standards review is complete and any remaining limitations or follow-up gaps must be recorded.

## Notes

- Prompt: `plan008-prompt.md`
- Draft: `plan008-draft.md`
- Skill target location: `repo/skills/catherder-repo-syncer/`
- This plan intentionally inherits Plan 007 lessons about source-of-truth mapping, ambiguity handling, and cautious sync classification.
- Begin execution only on a dedicated branch created from a clean `main`, per `catherder-git.instructions.md`.
