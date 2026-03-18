---
type: plan
description: "Plan 009 draft — Upstream reusable instruction/process improvements from catherder-dev into this repository, canonical docs, and published artifacts"
---
# Plan 009 Draft: Upstream catherder-dev Instruction Improvements

**Status:** `draft`

**Created:** 2026-03-15T00:00:00+00:00

**Updated:** 2026-03-15T00:00:00+00:00

## Goal

Prepare a safe, coordinated upstreaming pass that adopts reusable instruction and process improvements from `catherder-dev` into this repository's operational files, the canonical CatHerder source docs under `docs/catherder/`, and derived reusable artifacts under `repo/`.

## Context / Why

`catherder-dev` has evolved its instruction files and process wording in ways that may improve CatHerder broadly: clearer startup guidance, cleaner wording, better git-policy phrasing, and potentially leaner instruction surfaces for agents. Some of those changes appear reusable, while others remain project-specific.

This repository is both:
- an operational CatHerder-enabled repository with its own `.instructions/`, and
- the source of truth for reusable CatHerder documentation and published artifacts.

Because of that dual role, upstreaming should be done intentionally:
- preserve local-vs-canonical distinctions
- avoid blindly copying project-specific wording
- reduce duplication between `project.instructions.md` and `catherder.instructions.md`
- improve reliability and concision for agents with minimal context cost

## Intended Outputs

- A reviewed sync decision for each compared file
- Proposed local updates for this repository's `AGENTS.md`, `README.md`, and `.instructions/` files where appropriate
- Proposed canonical doc updates in `docs/catherder/`
- Proposed derived artifact updates in `repo/`
- Recorded rationale for accepted, rejected, and deferred upstream candidates

## Candidate Upstream Directions

### Strong candidates
- Adopt clearer, more neutral wording from `catherder-dev` for `catherder-git.instructions.md`
- Simplify `catherder.instructions.md` where local reading-order content duplicates document-map guidance in `project.instructions.md`
- Tighten bootstrap and startup wording for `AGENTS.md` and `README.md`

### Manual-merge candidates
- `README.md` framing and startup guidance
- `project.instructions.md` top-level framing and structure wording
- Canonical documentation that should encode the sharper split between entry guidance and process rules

### Likely non-sync / caution areas
- Any project-specific architecture or technology guidance from `catherder-dev`
- `SCRATCHPAD.md`, plans, and other operational state
- Any change that increases startup context without improving compliance or clarity

## Risks / Questions

- Some current canonical guidance may already partially cover these improvements; avoid creating drift or redundant wording.
- The repo currently lacks a reusable `project.instructions.md` template/artifact in `repo/instructions/`; decide whether to introduce one or document the pattern elsewhere.
- Need to preserve the distinction between this repo's local `.instructions/` and cross-project standards in `docs/` and `repo/`.
- Must avoid making `catherder.instructions.md` into a second entry/navigation file.

## Proposed Execution Shape

1. Capture file-by-file sync decisions and rationale in plan data.
2. Refine this repository's local operational files where approved.
3. Update canonical source docs in `docs/catherder/` to encode approved patterns.
4. Propagate those approved patterns into derived artifacts under `repo/`.
5. Verify consistency and record remaining gaps or decisions for follow-up.

## Notes

- Prompt: `plan009-prompt.md`
- Planning-only session. No execution tasks should start until an active plan exists.
- Input comparison used `tmp-symlink-to-catherder-dev` as the downstream reference project.
