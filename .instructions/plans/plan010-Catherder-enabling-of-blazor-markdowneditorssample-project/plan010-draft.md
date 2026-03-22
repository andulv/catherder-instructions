---
type: plan
description: "Plan 010 draft — CatHerder-enable tmp-blazor-markdowneditorssample following current standards with selective reuse from tmp-catherder-dev"
---
# Plan 010 Draft: CatHerder-Enable Blazor MarkdownEditorsSample

**Status:** `draft`

**Created:** 2026-03-22T00:40:39+00:00

**Updated:** 2026-03-22T00:40:39+00:00

## Goal

Prepare a safe, standards-compliant CatHerder enablement for `tmp-blazor-markdowneditorssample`, using `catherder-instructions` as the canonical source and selectively reusing compatible .NET / Blazor instruction patterns from `tmp-catherder-dev`.

## Context / Why

`tmp-blazor-markdowneditorssample` is a Blazor sandbox project for evaluating multiple markdown editors and related integration patterns. It is not currently CatHerder-enabled.

This repository, `catherder-instructions`, is the source of truth for CatHerder standards and reusable enablement patterns. `tmp-catherder-dev` is already CatHerder-enabled and uses a similar .NET / ASP.NET Blazor stack, making it a useful reference for project-specific phrasing and development guidance.

The target project should gain the standard CatHerder bootstrap and process structure without importing catherder-dev-specific domain content such as agent orchestration, MAF guidance, or unrelated architecture rules.

## Intended Outputs

- A short inventory of the target project's relevant structure and technical characteristics
- A list of reusable guidance candidates from `tmp-catherder-dev`
- A standards-compliant CatHerder scaffold plan for the target project
- Proposed project-specific instruction content tailored to the Blazor markdown editor sample
- A verification checklist for end-state CatHerder compliance

## Candidate Enablement Strategy

### Canonical/shared content
- Copy `catherder.instructions.md` from `catherder-instructions`
- Copy `catherder-git.instructions.md` from `catherder-instructions`
- Use the minimal `AGENTS.md` bootstrap model already established in CatHerder-enabled repos

### Project-specific content to author
- `project.instructions.md`
- `project-status-roadmap.md`
- `SCRATCHPAD.md`

### Selective reuse from `tmp-catherder-dev`
- .NET / C# and Blazor-oriented build/run conventions
- concise repository layout description style
- practical testing/build expectations suitable for a prototype-stage software project

### Non-reuse / caution areas
- Microsoft Agent Framework guidance
- AI agent orchestration architecture details
- provider/model abstraction rules
- any content not relevant to a markdown-editor sample sandbox

## Risks / Questions

- Need to choose the appropriate project phase; current evidence suggests `Prototype`, but that should be confirmed during execution.
- Must keep project-specific instructions concise and avoid duplicating process rules from canonical files.
- Should verify whether `.agents/` needs only the standard empty scaffold or any project-local agent/runtime assets.
- The target project may later want editor-specific technical notes beyond the initial CatHerder bootstrap; those should be kept in project-specific docs only.

## Proposed Execution Shape

1. Inventory the target project and capture reusable guidance candidates from `tmp-catherder-dev`.
2. Create the CatHerder scaffold in the target project (`AGENTS.md`, `.instructions/`, `.instructions/plans/`, `.agents/`).
3. Copy canonical process files from `catherder-instructions`.
4. Author project-specific files for the target project's purpose, layout, commands, and phase.
5. Verify the end state against CatHerder entry and structure expectations.

## Notes

- Prompt: `plan010-prompt.md`
- Planning-only session. No execution tasks should start until an active plan exists.
- Target project: `/workspace/tmp-blazor-markdowneditorssample`
- Reference enabled project: `/workspace/tmp-catherder-dev`
