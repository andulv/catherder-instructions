---
type: plan
description: "Plan 007 — Upstream improved instruction-entry and repository-guidance patterns into canonical CatHerder artifacts"
---
# Plan 007: Upstream Instruction and Entrypoint Improvements

**Status:** `draft`

**Created:** 2026-03-09T00:00:00+00:00

**Updated:** 2026-03-09T00:00:00+00:00

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

## What We Want To Achieve (Outcomes)

A reviewed and intentionally updated set of canonical CatHerder artifacts such that:

- Canonical guidance clearly defines the relationship between `AGENTS.md`, `project.instructions.md`, `catherder.instructions.md`, and `catherder-git.instructions.md`
- Reusable instruction templates reflect agent-optimized document-entry guidance
- Guidance distinguishes required, operational, and conditional reads where appropriate
- `project-status-roadmap.md` is not presented as universally mandatory context
- `SCRATCHPAD.md` usage is described as resume/continue + session-end update behaviour
- Search/scan ignore-by-default guidance is represented where it belongs
- Repository structure guidance reflects intended CatHerder structure and clearly separates operational, canonical, and legacy/reference areas
- Any affected derived artifacts are identified and updated to remain in sync

## Summary Of Work Needed

**1. Inventory upstream candidates**

Review the changes made in this repository's `.instructions/` and `AGENTS.md`, and classify which are:
- repository-local only
- suitable as canonical defaults
- suitable as optional guidance only

**2. Identify canonical source files to change**

Use the derivation/publishing map to determine which source-of-truth materials govern:
- instruction entry guidance
- CatHerder workflow rules
- git workflow guidance
- reusable project scaffolding/templates
- agent entrypoint conventions

Likely areas include `docs/catherder/`, `repo/instructions/`, `repo/agents/`, and related READMEs/templates.

**3. Define the upstream guidance model**

Decide the canonical wording and boundaries for:
- minimal `AGENTS.md`
- authoritative repository document map in `project.instructions.md`
- workflow authority in `catherder.instructions.md`
- mandatory git guidance when `catherder-git.instructions.md` is present
- conditional use of roadmap and scratchpad files
- ignore-by-default guidance scope

**4. Draft canonical changes**

Prepare standards-compliant edits to the identified source files, keeping one authoritative source per topic and avoiding drift-prone duplication.

**5. Update derived reusable artifacts**

Propagate approved canonical changes into reusable templates/artifacts under `repo/` that downstream projects consume.

**6. Verify consistency**

Check that canonical docs, reusable artifacts, and repository-local instructions are aligned, and note any remaining follow-up work.

## Key Principles / Constraints

- Prefer one authoritative source per instruction topic.
- Optimize for agent execution: low ambiguity, low context overhead, explicit read conditions.
- Prefer markdown links over bare filenames.
- Do not force always-read startup lists when conditional reading is sufficient.
- Keep repository-local operational details separate from reusable canonical guidance.
- When changing canonical docs, update derived reusable artifacts that depend on them.

## Open Questions

- Which of the improved patterns belong in canonical CatHerder defaults vs repository-specific usage examples?
- Should ignore-by-default guidance live in canonical `project.instructions.md` templates, broader methodology docs, or both?
- Should `AGENTS.md` conventions be documented primarily in docs, templates, or both?

## Notes

- Source prompt: `plan007-prompt.md`
- Recent repository-local improvements are recorded in [`../../SCRATCHPAD.md`](../../SCRATCHPAD.md)
- Check [`docs/catherder/README.md`](../../../docs/catherder/README.md) before changing canonical docs to understand derivation/downstream sync requirements
