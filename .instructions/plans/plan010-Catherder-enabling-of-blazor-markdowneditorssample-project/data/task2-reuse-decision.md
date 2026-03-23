# Task 2 — Reuse decision note

Created: 2026-03-22T00:40:39+00:00

## Compared sources

- Canonical source of truth: `/workspace/catherder-instructions`
- Reference enabled project: `/workspace/tmp-catherder-dev`
- Target project: `/workspace/tmp-blazor-markdowneditorssample`

## Safe reuse from `tmp-catherder-dev`

### Reuse / adapt
- Concise `.NET / C#` and `ASP.NET Blazor` stack description style
- Simple repository-layout section format in `project.instructions.md`
- Practical build/run command section structure
- Lightweight development conventions appropriate to a prototype-stage software project
- Minimal `AGENTS.md` bootstrap model already aligned with current standards

### Reuse with modification
- Testing guidance should be simplified for a sandbox/sample project rather than a larger application with tests and provider integrations
- Project layout should reflect the sample repo's actual structure (`src/`, solution file, README, optional `data/` scope) rather than catherder-dev's multi-project layout
- Scratchpad and roadmap should reflect editor-evaluation work rather than orchestration-product development

## Exclusions from reuse

Do not copy these from `tmp-catherder-dev`:
- Microsoft Agent Framework (MAF) guidance
- AI agent orchestration architecture notes
- provider/model abstraction principles
- vendor/provider testing strategy for live integrations
- references to `CatHerder.Core`, `CatHerder.Web`, or related app-specific layout
- domain-specific coding conventions that do not apply to the sample project

## Decision summary

- Canonical process files come from `catherder-instructions`
- Project-specific files should be freshly authored for the markdown editor sample
- `tmp-catherder-dev` serves only as a wording/style reference for compatible software-project guidance, not as a copy source for domain content
