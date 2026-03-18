---
type: plan
description: "Plan 009 — Upstream reusable instruction/process improvements from catherder-dev into this repository, canonical docs, and published artifacts"
---
# Plan 009: Upstream catherder-dev Instruction Improvements

**Status:** `completed`

**Branch:** `plan/009-upstream-catherder-dev-instruction-improvements`

**Created:** 2026-03-15T00:00:00+00:00

**Updated:** 2026-03-15T02:00:00+00:00

## Goal

Upstream the reusable instruction and process improvements identified in `tmp-symlink-to-catherder-dev` into this repository in a controlled way: improve local operational instructions where appropriate, update canonical CatHerder source documentation under `docs/catherder/`, and propagate approved changes into reusable artifacts under `repo/`.

## Context / Why

A comparison of `catherder-dev` against this repository found a mix of reusable improvements and project-specific differences:

- `AGENTS.md` contains a slightly stronger bootstrap trigger for planning/work startup
- `README.md` is more direct and focused, suggesting this repository's README can be tightened
- `catherder.instructions.md` in `catherder-dev` is leaner and avoids local reading-order duplication
- `catherder-git.instructions.md` in `catherder-dev` is clearly better worded: more grammatical, more neutral, and more reliable for agent interpretation
- `project.instructions.md` in this repository remains structurally stronger, but could be tightened further for concision

The desired outcome is not blind sync. This repository must preserve the distinction between:
- local operational guidance in `.instructions/`
- canonical CatHerder documentation in `docs/catherder/`
- published reusable artifacts in `repo/`

The work should favor concise, low-bloat instructions that improve agent reliability, reduce duplicate guidance, and keep each file focused on a single role.

## Tasks

- [x] Task 1: Record the comparison decisions for all requested files (`AGENTS.md`, `README.md`, and selected `.instructions/*`) including classification, recommended sync direction, rationale, and caution areas. Output: comparison decision note under `data/`.
- [x] Task 2: Record the approved upstream guidance model for bootstrap files, repository READMEs, `project.instructions.md`, `catherder.instructions.md`, and `catherder-git.instructions.md`, emphasizing concision, single-purpose files, and low-context startup. Output: guidance decision note under `data/`.
- [x] Task 3: Refine this repository's local `AGENTS.md`, `README.md`, `.instructions/project.instructions.md`, `.instructions/catherder.instructions.md`, and `.instructions/catherder-git.instructions.md` according to the approved model. Output: local operational files updated.
- [x] Task 4: Update canonical documentation under `docs/catherder/` so the approved model is explicitly documented, including minimal bootstrap guidance, separation of entry/navigation from process rules, and clearer git-policy wording. Output: canonical docs updated.
- [x] Task 5: Update derived reusable artifacts under `repo/` to reflect the approved canonical model, including instruction templates and any README or agent-template guidance affected by the changes. Output: reusable artifacts updated.
- [x] Task 6: Decide whether `repo/instructions/` should gain a reusable `project.instructions.md` template/example or whether the pattern should remain documented only in canonical docs; record and implement the approved choice. Output: decision note and artifact update if approved.
- [x] Task 7: Verify consistency across local operational files, canonical docs, and reusable artifacts; record follow-up gaps, deferred decisions, and any intentionally non-upstreamed differences. Output: verification note.

## Acceptance Criteria

- [x] A file-by-file decision record exists for all user-requested comparison targets.
- [x] Approved guidance clearly distinguishes bootstrap, entry/navigation, process, and git-specific instruction roles.
- [x] This repository's local instruction files are more concise and do not duplicate startup/read-order guidance unnecessarily.
- [x] `catherder-git.instructions.md` uses neutral, precise wording without anthropomorphic or vague policy language.
- [x] Canonical docs under `docs/catherder/` explicitly support the approved concise instruction model.
- [x] Derived artifacts under `repo/` are updated to match canonical guidance and avoid drift.
- [x] The treatment of `project.instructions.md` as a reusable template/example versus documented pattern is explicitly decided and recorded.
- [x] Any differences intentionally left local to `catherder-dev` are documented rather than silently omitted.

## Notes

- Prompt: `plan009-prompt.md`
- Draft: `plan009-draft.md`
- Source comparison repo: `tmp-symlink-to-catherder-dev`
- Relevant prior work: Plan 007 (upstream instruction-entry improvements) and Plan 008 (`catherder-repo-syncer` skill) established useful comparison and source-of-truth patterns for this effort.
- 2026-03-15T00:30:00+00:00: Executed Tasks 1-2. Added `data/task1-comparison-decisions.md` with file-by-file sync decisions and `data/task2-guidance-model.md` with the approved concise instruction model for bootstrap, README, project-entry, process, and git-policy files.
- 2026-03-15T01:00:00+00:00: Executed Task 3. Refined local `AGENTS.md`, `README.md`, `.instructions/project.instructions.md`, `.instructions/catherder.instructions.md`, and `.instructions/catherder-git.instructions.md` to align with the approved concise, single-purpose instruction model.
- 2026-03-15T01:30:00+00:00: Executed Tasks 4-5. Updated canonical docs in `docs/catherder/` to codify minimal bootstrap guidance, clearer entry-versus-process separation, and improved git-policy wording. Propagated those changes into `repo/instructions/` and tightened `repo/agents/README.md` to preserve the minimal `AGENTS.md` bootstrap model.
- 2026-03-15T01:45:00+00:00: Executed Task 6. Recorded the decision to keep `project.instructions.md` as a documented repository-specific pattern rather than publishing a copy-ready template in `repo/instructions/`. Added decision note under `plan009/data/`; no new `repo/instructions/project.instructions.md` artifact was created.
- 2026-03-15T02:00:00+00:00: Executed Task 7. Verified consistency across local operational files, canonical docs, and derived artifacts. Recorded accepted outcomes, intentionally non-upstreamed differences, and deferred follow-up gaps in `data/task7-verification-note.md`.
