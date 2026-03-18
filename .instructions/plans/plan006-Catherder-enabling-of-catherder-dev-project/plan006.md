---
type: plan
description: "Plan 006 — CatHerder-enable catherder-dev, preserving experimental skills as reference"
---
# Plan 006: CatHerder-Enable Catherder-Dev

**Status:** `completed`

**Branch:** `plan/006-catherder-enable-catherder-dev`

**Created:** 2026-03-06T09:30:00+01:00

**Updated:** 2026-03-06T10:58:00+01:00

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

Project phase: **Prototype** (experimental skills in legacy folder; focus on core catherder-dev work).

## Tasks

- [x] Task 1: Inventory legacy content; list keep/ignore candidates (project, roadmap, team, plans, skills). Output: short list in plan notes or data file.
- [x] Task 2: Extract project-specific guidance from legacy `project.INSTRUCTIONS.md` + `team.md` into notes for `project.instructions.md`. Output: bullet list ready to paste.
- [x] Task 3: Create scaffold (`AGENTS.md`, `.instructions/`, `.agents/`, `.instructions/plans/`). Output: folders + entrypoint present.
- [x] Task 4: Copy canonical `catherder.instructions.md` + `catherder-git.instructions.md` verbatim into `.instructions/`. Output: byte-for-byte match.
- [x] Task 5: Create new project files: `project.instructions.md`, `project-status-roadmap.md`, `SCRATCHPAD.md` (phase = Prototype). Output: new files populated.
- [x] Task 6: Document legacy folder usage (reference-only) in /home/anders/source/agent/catherder-dev/.instructions/legacy-folder-usage.md. Output: explicit reference note.
- [x] Task 7: Write a short decision note on legacy skills (keep as reference, extract insights, or prune later). Output: a single paragraph decision.

## Acceptance Criteria

- [x] Catherder-dev contains `.instructions/` with: `SCRATCHPAD.md`, `catherder.instructions.md`, `project-status-roadmap.md`, `plans/`, and project-specific files
- [x] Catherder-dev contains `.agents/` (skills folder, initially empty)
- [x] Catherder-dev contains `AGENTS.md` entry point pointing to `.instructions/`
- [x] Canonical files are copied verbatim from `repo/instructions/`
- [x] Project-specific instructions include project-extracted guidance; no process duplication
- [x] Legacy experimental skills remain in legacy folder, not migrated; reference strategy documented
- [x] Project phase clearly set to **Prototype** in `.instructions/project-status-roadmap.md`

## Notes

- Prompt: `plan006-prompt.md`
- Draft: `plan006-draft.md`
- Task 1 output: `data/legacy-inventory.md`
- Task 2 output: `data/project-guidance-extract.md`
- Task 6 output: `/home/anders/source/agent/catherder-dev/.instructions/legacy-folder-usage.md`
- Task 7 output: `/home/anders/source/agent/catherder-dev/.instructions/legacy-skills-decision.md`
