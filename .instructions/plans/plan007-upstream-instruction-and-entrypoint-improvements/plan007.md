---
type: plan
description: "Plan 007 — Upstream improved instruction-entry and repository-guidance patterns into canonical CatHerder artifacts"
---
# Plan 007: Upstream Instruction and Entrypoint Improvements

**Status:** `completed`

**Branch:** `plan/007-upstream-instruction-and-entrypoint-improvements`

**Created:** 2026-03-09T00:00:00+00:00

**Updated:** 2026-03-09T01:35:00+00:00

## Goal

Update the canonical CatHerder source materials so the improvements proven in this repository's `.instructions/` and `AGENTS.md` become reusable defaults for downstream CatHerder-enabled projects.

## Context / Why

While improving this repository's own operational instructions, we identified several generalizable patterns that make CatHerder instructions easier for agents to follow:

- one authoritative source per instruction topic
- document maps instead of blanket "read everything" startup lists
- explicit required / operational / conditional reading guidance
- markdown links for instruction references
- clearer distinction between entry guidance, workflow authority, and git-specific rules
- ignore-by-default guidance for search/scan hygiene
- more accurate repository structure guidance and clearer handling of legacy/reference areas

This repository is both an operational repository and the source of truth for CatHerder templates and conventions. Those proven improvements should be upstreamed into canonical docs and reusable artifacts so new CatHerder-enabled projects start with better defaults.

## Tasks

- [x] Task 1: Inventory this repository's instruction and entrypoint improvements; classify each as canonical default, optional guidance, or repository-local only. Output: short candidate list in a data note.
- [x] Task 2: Trace canonical source-of-truth and derived artifacts for instruction entry guidance, workflow rules, git rules, and project scaffolding. Output: affected-file map.
- [x] Task 3: Define the upstream guidance model for `AGENTS.md`, `project.instructions.md`, `catherder.instructions.md`, `catherder-git.instructions.md`, `SCRATCHPAD.md`, roadmap usage, and ignore-by-default guidance. Output: concise decision note.
- [x] Task 4: Update canonical documentation under `docs/catherder/` to reflect the approved model, including single-source authority for entry guidance, document-map/conditional-reading guidance, and ignore-by-default search/scan guidance. Output: canonical docs updated.
- [x] Task 5: Update reusable artifacts under `repo/` so approved canonical changes propagate into templates and other derived materials. Output: reusable artifacts updated.
- [x] Task 6: Verify consistency across canonical docs, reusable artifacts, and this repository's operational instructions; record any follow-up gaps. Output: verification note.

## Acceptance Criteria

- [ ] Canonical documentation defines a single-source-of-truth model for instruction entry guidance and workflow authority.
- [ ] Canonical guidance distinguishes required, operational, and conditional reading where appropriate.
- [ ] `project-status-roadmap.md` is not described as universally mandatory startup reading.
- [ ] `SCRATCHPAD.md` guidance clearly states resume/continue usage and session-end update expectations.
- [ ] `AGENTS.md` guidance supports a minimal bootstrap role without duplicating repository workflow instructions.
- [ ] Ignore-by-default search/scan guidance is represented where it belongs in the canonical model.
- [ ] Repository structure guidance clearly distinguishes operational, canonical, and legacy/reference areas.
- [ ] Affected reusable artifacts in `repo/` are updated to stay in sync with canonical documentation.
- [x] Any remaining ambiguities or deferred decisions are recorded in plan notes or verification output.

## Notes

- Prompt: `plan007-prompt.md`
- Draft: `plan007-draft.md`
- Start by checking [`../README.md`](../README.md) and [`../../../docs/catherder/README.md`](../../../docs/catherder/README.md) before editing canonical source materials.
- Recent repository-local improvements are summarized in [`../../SCRATCHPAD.md`](../../SCRATCHPAD.md).