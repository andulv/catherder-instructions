---
type: plan
description: "Plan 012 draft — Prepare a self-contained skill that emulates Stein Storken writing and Excel style from plan011 corpus outputs"
---
# Plan 012 Draft: Stein Storken Style Skill

**Status:** `draft`

**Created:** 2026-03-23T03:13:41+00:00

**Updated:** 2026-03-23T03:13:41+00:00

## Goal

Prepare a plan for creating a new reusable skill named `stein-storken-style` that captures the communication style, writing habits, document structure patterns, and Excel presentation conventions associated with the Stein Storken alias, using plan011 extraction outputs as the main evidence base.

## Context / Why

Plan011 produced a curated corpus of email fragments and candidate attachments that can be used to infer recurring communication patterns and document habits. The user now wants that material turned into a reusable skill so future agents can write in the same style and generate spreadsheets with the same recognizable look and delivery phrasing.

The requested skill is not just a writing-style prompt. It needs to be a self-contained skill package that can guide:
- Norwegian-language written communication
- document structure, bullets, and sentence rhythm
- decision-support framing with three alternatives rather than direct prescription
- delivery phrasing such as "her er en enkel modell som viser ..."
- spreadsheet styling and templates in the visual idiom associated with black, yellow, and white formatting and likely older Office-era conventions

Because this repository is the source of truth for CatHerder conventions, the resulting skill should follow repository skill standards and preserve evidence/provenance from the plan011 corpus in authoring references. It also needs to avoid the original personal name inside the shipped skill and instead use only the alias `Stein Storken`.

## Intended Outputs

- A new skill folder for `stein-storken-style`
- A Norwegian-first `SKILL.md` describing when and how to apply the style
- Reference material summarizing observed writing patterns, phrase habits, structure conventions, and Excel conventions derived from plan011 outputs
- One or more Excel templates that embody the Stein Storken style
- Validation notes showing the skill meets skill-file standards

## Key Planning Questions

- Which parts of the plan011 corpus are strong enough to treat as stable style signals versus only anecdotal examples?
- How should the skill separate hard rules from softer tendencies so agents imitate the style without overfitting noisy mail fragments?
- What is the safest way to represent likely Office-2007-era Excel conventions without claiming unsupported historical certainty?
- Where should binary spreadsheet templates live so the skill remains self-contained and easy to use?
- How should provenance be captured when the shipped skill must avoid the real name but the authoring evidence comes from plan011 outputs that contain it?

## Candidate Workflow Shape

### Phase 1: Corpus review and style extraction
- Inspect representative plan011 fragments and candidate Excel/document attachments
- Record recurring words, sentence forms, greeting/closing habits, bullet structures, and recommendation framing
- Distinguish strong repeated patterns from weaker or uncertain observations

### Phase 2: Skill design
- Define the skill trigger description and scope
- Decide what belongs in `SKILL.md` versus `references/` versus template assets
- Specify Norwegian-only expectations for user-facing outputs and examples

### Phase 3: Excel-style specification
- Analyze relevant workbook candidates from plan011 output
- Document recurring visual conventions such as fonts, fills, borders, sheet organization, naming, and delivery wording
- Define one or more templates suitable as starting points for future workbook generation

### Phase 4: Packaging and validation plan
- Prepare how the skill should be laid out under the repository skill structure
- Include validation steps for upstream skill format and CatHerder reference conventions
- Record any limitations or confidence notes where evidence is incomplete

## Risks / Questions

- Some attachment files in plan011 may be PDFs or Office documents that require additional tooling to inspect deeply.
- Style signals from email fragments may include context-specific wording that should not be overgeneralized.
- The user suspects older Office-era visual patterns, but this may need to be framed as an evidence-based approximation unless confirmed from workbook inspection.
- Excel templates are binary assets, so the execution plan should clearly define naming, location, and how they are referenced from the skill.
- The skill must not ship the real name, so authoring artifacts need careful wording and alias handling.

## Proposed Tooling

- Shell tools for inventorying plan011 outputs and candidate attachment types
- Python for corpus summarization and spreadsheet inspection where needed
- Spreadsheet-capable tooling for generating `.xlsx` template assets
- Skill validation tooling and local reference validation scripts if available in-repo

## Notes

- Prompt: `plan012-prompt.md`
- Planning-only session. No skill files or template assets should be created until the plan becomes active and execution is explicitly requested.
- The skill should likely be published under `repo/skills/` if it is intended as a reusable canonical artifact, but this should be confirmed during execution planning.
