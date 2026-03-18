---
type: reference
description: "Plan 009 Task 1 comparison decisions for requested files between catherder-instructions-repo and tmp-symlink-to-catherder-dev"
---
# Plan 009 Task 1 — Comparison Decisions

## Scope

Compared these files between this repository and `tmp-symlink-to-catherder-dev`:

- `AGENTS.md`
- `README.md`
- `.instructions/project.instructions.md`
- `.instructions/catherder.instructions.md`
- `.instructions/catherder-git.instructions.md`

Also reviewed implications for canonical and published materials under:

- `docs/catherder/`
- `repo/`

## File-by-file Decisions

### `AGENTS.md`
- **Classification:** canonical/shared bootstrap file
- **Current repo status:** already follows the preferred minimal bootstrap pattern
- **Difference summary:** `catherder-dev` adds stronger trigger wording: "Before doing work or planning to do work on this project, read ..."
- **Recommended sync direction:** `merge manually`
- **Rationale:** This repository's version is slightly shorter and already aligns with CatHerder's preferred minimal bootstrap role. The `catherder-dev` wording is a useful refinement because it explicitly covers both planning and execution startup.
- **Cautions:** Do not expand `AGENTS.md` into a second workflow document. Keep it minimal and avoid duplicating process rules.
- **Suggested reusable takeaway:** strengthen startup trigger wording while preserving a one-link bootstrap model.

### `README.md`
- **Classification:** locally adaptable with reusable orientation patterns
- **Current repo status:** broader and more methodology-focused; includes some legacy/transitional references
- **Difference summary:** `catherder-dev` README is more direct about project purpose, startup point, and repository layout
- **Recommended sync direction:** `merge manually`
- **Rationale:** The `catherder-dev` README demonstrates a more focused orientation style that could improve this repository's README. However, this repository has a dual role (operate + publish) and cannot simply copy a project README model.
- **Cautions:** Avoid using README as a second instruction file. Keep it high-signal and orienting. Remove or de-emphasize stale transitional references if no longer needed.
- **Suggested reusable takeaway:** tighten opening purpose statement, highlight repository role distinctions sooner, and keep startup guidance short.

### `.instructions/project.instructions.md`
- **Classification:** locally adaptable repository-entry guidance
- **Current repo status:** structurally stronger than `catherder-dev`; already uses required / operational / conditional reading model and clearly distinguishes local operation from canonical publishing
- **Difference summary:** `catherder-dev` version is more compact and direct, but is more project-specific and less operationally expressive
- **Recommended sync direction:** `sync this repo's structural model outward`; for this repo itself, `merge manually` for wording refinements only
- **Rationale:** This repository's document-map structure is a stronger reusable pattern. The `catherder-dev` version offers useful tone/compactness cues, but not a better overall repository-entry model for this repo.
- **Cautions:** Keep project-specific architecture and tech details out of reusable patterns. Avoid repeating process rules that belong in `catherder.instructions.md`.
- **Suggested reusable takeaway:** preserve document-map-first entry guidance, but tighten top framing and reduce wording where possible.

### `.instructions/catherder.instructions.md`
- **Classification:** canonical/shared process rules
- **Current repo status:** good coverage of core process rules, but still contains a `Reading Order` section that overlaps with `project.instructions.md`
- **Difference summary:** `catherder-dev` version is leaner and omits local reading-order guidance while preserving the core process model
- **Recommended sync direction:** `merge manually`, leaning toward the leaner `catherder-dev` formulation
- **Rationale:** The best reusable improvement is not the whole file but the sharper separation of responsibilities: `project.instructions.md` should govern entry/navigation; `catherder.instructions.md` should remain focused on invariant process rules.
- **Cautions:** Do not remove process-critical material while simplifying. Avoid introducing repository navigation guidance here that duplicates `project.instructions.md`.
- **Suggested reusable takeaway:** remove redundant read-order/navigation content and keep this file process-only.

### `.instructions/catherder-git.instructions.md`
- **Classification:** canonical/shared git module
- **Current repo status:** policy intent is sound, but wording is less grammatical, less neutral, and more anthropomorphic
- **Difference summary:** `catherder-dev` version expresses the same policy more clearly, with better grammar, clearer refusal criteria, and more neutral language
- **Recommended sync direction:** `sync from catherder-dev into this repo` and propagate into canonical/derived artifacts
- **Rationale:** This is the clearest high-confidence upstream candidate. Better wording here directly improves agent reliability and reduces ambiguity in plan/branch/commit behavior.
- **Cautions:** Ensure canonical docs and derived artifacts are updated alongside any local file changes to avoid drift.
- **Suggested reusable takeaway:** use precise, neutral policy language; remove phrasing such as "complain and nag" and other personality-based instructions.

## Issues Identified During Review

### README.md startup path inconsistency
This repository's README says: *"Start here for working on this repo: `.instructions/SCRATCHPAD.md`, then `.instructions/catherder.instructions.md`."*

This contradicts both `AGENTS.md` (which points to `project.instructions.md`) and the Task 2 approved guidance model (which designates `project.instructions.md` as the repository entry authority). Task 3 should fix this.

### Markdown syntax bug in catherder-dev `catherder.instructions.md`
Prompt Precedence item 6 reads: `` **Task file(s)` referenced by the plan `` — the bold marker is unclosed and the backtick placement is wrong. The instructions-repo version is correct: `**Task file(s)** referenced by the plan`. This is a catherder-dev local bug, not an upstream concern, but worth noting to avoid propagating it.

## Cross-cutting Findings

### Reusable improvements identified
- Stronger bootstrap trigger wording can improve compliance without materially increasing context size.
- README files should orient, not duplicate repository instructions.
- `project.instructions.md` should own entry/navigation and reading guidance.
- `catherder.instructions.md` should own process rules only.
- Git rules benefit from neutral, explicit, testable wording.

### README startup path fix needed
- This repository's README must be updated to point to `project.instructions.md` as the entry point, aligning with AGENTS.md and the approved guidance model.

### Differences intentionally not treated as upstream candidates
- `catherder-dev` architecture, stack, and project-specific development guidance
- `SCRATCHPAD.md`, plans, and other operational state
- Any wording that increases startup context without improving clarity or compliance

## Implications for Canonical and Published Materials

### `docs/catherder/`
The comparison suggests updates should reinforce:
- minimal bootstrap role for `AGENTS.md`
- separation of entry/navigation from process rules
- concise README/orientation patterns
- neutral git-policy wording
- explicit low-context / low-duplication instruction design principles

### `repo/`
The comparison suggests updates should likely reach:
- `repo/instructions/catherder.instructions.md`
- `repo/instructions/catherder-git.instructions.md`
- possibly a new reusable `project.instructions.md` template/example, or a clearer published pattern if that artifact is intentionally omitted
