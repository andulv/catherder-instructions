---
type: plan
description: "Plan 010 — CatHerder-enable tmp-blazor-markdowneditorssample following current standards with selective reuse from tmp-catherder-dev"
---
# Plan 010: CatHerder-Enable Blazor MarkdownEditorsSample

**Status:** `active`

**Branch:** `plan/010-catherder-enable-blazor-markdowneditorssample`

**Created:** 2026-03-22T00:40:39+00:00

**Updated:** 2026-03-22T00:40:39+00:00

## Goal

CatHerder-enable `tmp-blazor-markdowneditorssample` as a standards-compliant CatHerder project, using `catherder-instructions` as the canonical source and selectively reusing only the `tmp-catherder-dev` guidance that fits a .NET / ASP.NET Blazor software project.

## Context / Why

`tmp-blazor-markdowneditorssample` is a software project and technology-wise is similar enough to `tmp-catherder-dev` that some repository-specific guidance patterns can be reused. However, it is a markdown-editor sandbox/sample project, not an agent-orchestration application, so reuse must be selective and intentional.

This repository is the source of truth for CatHerder standards. The enablement work should therefore:
- preserve canonical process files from `catherder-instructions`
- create minimal, accurate project-specific instructions for the target project
- avoid copying catherder-dev-specific domain and architecture content

## Tasks

- [ ] Task 1: Inventory `tmp-blazor-markdowneditorssample` structure, commands, and technical concerns relevant to CatHerder enablement. Output: short inventory note under `data/`.
- [ ] Task 2: Compare `tmp-catherder-dev` CatHerder surface against the target project and record which project-specific guidance can be safely reused versus excluded. Output: reuse decision note under `data/`.
- [ ] Task 3: Create the CatHerder scaffold in `tmp-blazor-markdowneditorssample` (`AGENTS.md`, `.instructions/`, `.instructions/plans/`, `.agents/`). Output: folders and bootstrap file present.
- [ ] Task 4: Copy canonical `catherder.instructions.md` and `catherder-git.instructions.md` from `catherder-instructions` into the target project's `.instructions/`. Output: canonical process files present.
- [ ] Task 5: Create project-specific files in the target project: `project.instructions.md`, `project-status-roadmap.md`, and `SCRATCHPAD.md`, tailored to the markdown editor sample and appropriate project phase. Output: project-specific CatHerder files present.
- [ ] Task 6: Verify the target project's CatHerder-enabled end state against standards and record any follow-up gaps or deferred improvements. Output: verification note under `data/`.

## Acceptance Criteria

- [ ] `tmp-blazor-markdowneditorssample` contains `AGENTS.md` with the standard CatHerder bootstrap role.
- [ ] `tmp-blazor-markdowneditorssample` contains `.instructions/` with at least `project.instructions.md`, `catherder.instructions.md`, `catherder-git.instructions.md`, `project-status-roadmap.md`, `SCRATCHPAD.md`, and `plans/`.
- [ ] `tmp-blazor-markdowneditorssample` contains `.agents/`.
- [ ] Canonical process files in the target project are copied from `catherder-instructions` rather than improvised.
- [ ] Project-specific files accurately describe the markdown editor sample project, its layout, commands, and prototype-style workflow.
- [ ] No catherder-dev-specific agent-orchestration or MAF content is copied into the target project's project-specific instructions.
- [ ] A verification note records whether the final scaffold meets CatHerder entry and structure expectations.

## Notes

- Prompt: `plan010-prompt.md`
- Draft: `plan010-draft.md`
- Target project: `/workspace/tmp-blazor-markdowneditorssample`
- Reference enabled project: `/workspace/tmp-catherder-dev`
- This plan authorizes future execution work on the target project, but the current session only created planning artifacts.
