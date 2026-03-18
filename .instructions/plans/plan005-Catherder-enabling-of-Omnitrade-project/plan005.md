---
type: plan
description: "Plan 005 — CatHerder-enable Omnitrade following current standards"
---
# Plan 005: CatHerder-Enable Omnitrade

**Status:** `completed`

**Branch:** `plan/005-catherder-enable-omnitrade`

**Created:** 2026-03-05T13:10:00+01:00

**Updated:** 2026-03-05T23:55:00+01:00

## Goal

Create a clean, standards-compliant CatHerder enablement for the Omnitrade project
at `/home/anders/source/omnitrade`, incorporating relevant project-specific and
tech-specific guidance from `.instructions-old-invalid-but-parts-might-be-useful`.

## Context / Why

Omnitrade has older instruction artifacts that don’t follow the current CatHerder
conventions. We want a minimal `.instructions/` + `.agents/` setup that matches
current standards, without losing valuable Omnitrade-specific guidance.

## Tasks

- [x] Task 1: Verify Omnitrade repo state (git clean, identify old instruction content)
- [x] Task 2: Create Omnitrade CatHerder scaffold (`AGENTS.md`, `.instructions/`, `.agents/`)
- [x] Task 3: Copy canonical instruction files into Omnitrade `.instructions/`
- [x] Task 4: Create Omnitrade project-specific instruction files (project, roadmap, scratchpad)
- [x] Task 5: Carry over Omnitrade-specific technical rules from old instructions
- [x] Task 6: Verify end state (minimum structure present; no process duplication)

## Acceptance Criteria

- [x] Omnitrade contains `.instructions/` with: `SCRATCHPAD.md`, `catherder.instructions.md`, `project-status-roadmap.md`, and `plans/`
- [x] Omnitrade contains `.agents/` (skills folder may be empty)
- [x] Omnitrade contains `AGENTS.md` entry point pointing to `.instructions/`
- [x] Canonical files are copied verbatim from `repo/instructions/`
- [x] Project-specific instructions include only Omnitrade-specific info; process rules remain in `catherder.instructions.md`

## Notes

- Prompt: `plan005-prompt.md`
- Draft: `plan005-draft.md`
- PR summary: `data/pr-summary.md`
