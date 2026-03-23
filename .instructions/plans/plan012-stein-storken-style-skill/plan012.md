---
type: plan
description: "Plan 012 — Create a reusable Stein Storken style skill focused on Norwegian writing patterns and Excel workbook conventions"
---
# Plan 012: Stein Storken Style Skill

**Status:** `active`

**Branch:** `plan/012-stein-storken-style-skill`

**Created:** 2026-03-23T03:13:41+00:00

**Updated:** 2026-03-23T03:32:25+00:00

## Goal

Create a reusable self-contained skill named `stein-storken-style` that helps agents emulate the Stein Storken communication style in Norwegian and produce Excel workbooks in the same recognizable style, using the plan011 corpus as the primary evidence base.

## Context / Why

Plan011 already extracted a curated set of email fragments and candidate attachments suitable for style analysis. The next step is to turn that evidence into a reusable skill package that can guide future agents in two practical areas only:

1. **Text** — Norwegian writing style, sentence habits, bullet structure, repeated wording, delivery phrasing, and decision-support framing.
2. **Excel** — workbook organization, sheet naming tendencies where observable, summary-first workbook architecture, text/comment-heavy first-sheet delivery, three-alternative decision-support structure, visual conventions, likely older Office-era formatting cues, and ready-to-use templates.

The focus at this stage is intentionally narrow. Other document types such as Word or PDF may appear in the source corpus, but they are not important to parse for this plan except where they provide minor contextual evidence. The main evidence sources should therefore be:
- extracted email fragments from plan011
- Excel attachments from plan011 output

The shipped skill must never mention the real person name and must use only the alias `Stein Storken`. All templates, examples, and generated user-facing artifacts should be in Norwegian. The skill should also teach the characteristic habit of calling even large spreadsheet workbooks "en enkel modell" and of presenting three alternatives to support a decision instead of making the decision outright.

## Scope

### In scope
- Build a new skill named `stein-storken-style`
- Analyze plan011 text fragments for recurring Norwegian communication patterns
- Analyze plan011 Excel attachments for recurring workbook and formatting conventions
- Document the style as actionable rules, examples, and reusable guidance
- Include one or more Excel templates in the skill
- Make the skill self-contained and aligned with skill-file standards
- Prefer deterministic local parsing and summarization of corpus data before any optional LLM-assisted synthesis

### Out of scope
- Deep parsing or style extraction from non-Excel attachments such as Word or PDF files
- Claims of exact historical Office version unless directly supported by inspected workbook evidence
- Broader persona simulation beyond communication and Excel deliverables

## Output Structure

- `repo/skills/stein-storken-style/SKILL.md` — primary skill instructions
- `repo/skills/stein-storken-style/references/style-analysis.md` — observed writing and communication patterns with provenance
- `repo/skills/stein-storken-style/references/excel-style-guide.md` — observed Excel conventions, workbook architecture, and template usage guidance
- `repo/skills/stein-storken-style/references/examples.md` — Norwegian examples of style usage, phrasing, bullets, and delivery language
- `repo/skills/stein-storken-style/templates/` — Excel template assets in Stein Storken style
- `repo/skills/stein-storken-style/data/` or `references/` notes as needed for provenance snapshots used during authoring
- `.instructions/plans/plan012-stein-storken-style-skill/data/source-inventory.md` — selected primary evidence sources from plan011 with rationale
- `.instructions/plans/plan012-stein-storken-style-skill/data/text-style-summary.md` or `.json` — compact extracted language patterns, counts, examples, and provenance
- `.instructions/plans/plan012-stein-storken-style-skill/data/excel-workbook-inventory.md` or `.json` — compact workbook-by-workbook structural and formatting summaries
- `.instructions/plans/plan012-stein-storken-style-skill/data/template-spec.md` — mapping from observed conventions to shipped template design decisions

## Style Expectations

- All examples, templates, and generated output guidance should default to Norwegian.
- The skill should emphasize concise, practical, decision-support communication.
- The skill should teach a tendency to present **three alternatives** when recommending a course of action.
- When delivering large or complex spreadsheets, the skill should normalize the phrase pattern: **"Her er en enkel modell som viser ..."**
- The skill should teach that **"en enkel modell"** is often a rhetorical framing device rather than a literal statement of workbook simplicity.
- The skill should teach a recurring workbook pattern where the first sheet functions as a summary/overview sheet with explanatory text and comments, followed by supporting detail sheets.
- The skill should avoid overclaiming certainty and should support decisions rather than making them for the user.

## Evidence Expectations

- Treat plan011 extracted fragments as the primary text corpus.
- Treat plan011 `.xlsx` attachments as the primary spreadsheet corpus.
- Build compact intermediate summaries before writing the shipped skill: source inventory, text-style summary, workbook inventory, and template spec.
- Use weaker sources only for context, not as the main basis for rules.
- Distinguish strong repeated patterns from soft tendencies and uncertain inference.
- Hard rules should be reserved for patterns repeated across multiple independent fragments or workbooks; softer tendencies should be labeled accordingly.
- Where evidence is incomplete, describe conventions as likely or observed rather than certain.
- LLM use, if any, should operate on compact summaries or representative excerpts rather than raw corpus dumps.

## Tasks

- [x] Task 1: Inventory the plan011 corpus relevant to this skill in `.instructions/plans/plan012-stein-storken-style-skill/data/source-inventory.md`, explicitly separating text-fragment sources from Excel attachment sources, identifying which files are primary evidence, and recording why weaker sources are excluded or treated as context only.
- [x] Task 2: Produce a compact text-analysis staging artifact in `.instructions/plans/plan012-stein-storken-style-skill/data/text-style-summary.md` or `.json` using local parsing first, documenting recurring Norwegian language patterns, repeated wording, sentence structure, bullet usage, greeting/closing habits, decision-support framing, frequency indicators, representative examples, and provenance.
- [x] Task 3: Produce a compact workbook-analysis staging artifact in `.instructions/plans/plan012-stein-storken-style-skill/data/excel-workbook-inventory.md` or `.json` using deterministic local workbook parsing first, documenting for each relevant `.xlsx` workbook: filename, confidence/source, sheet names and order, sheet count, whether the first sheet is a summary/overview sheet, whether it contains explanatory text/comments, whether three-option decision structure is present, recurring labels/headings, and notable formatting signals such as fills/colors, borders, fonts, merged cells, frozen panes, and emphasis patterns.
- [x] Task 4: Synthesize the staged text and workbook evidence into authoring references that distinguish hard rules, soft tendencies, and uncertain inference, including explicit documentation that "en enkel modell" often describes a large multi-sheet decision-support workbook rather than a literally simple file.
- [x] Task 5: Define the skill package structure and write a self-contained Norwegian-first `SKILL.md` for `stein-storken-style`, including trigger conditions, defaults, hard rules, soft tendencies, guidance for producing text and Excel outputs in style, and explicit instruction that any optional LLM use should rely on compact summaries rather than raw corpus material.
- [x] Task 6: Create Norwegian example material showing Stein Storken style for short email replies, structured bullet summaries, summary-sheet wording, and workbook handoff phrasing, including three-alternative decision-support patterns and the rhetorical use of "en enkel modell" for large supporting workbooks.
- [x] Task 7: Create one or more `.xlsx` templates and a supporting `.instructions/plans/plan012-stein-storken-style-skill/data/template-spec.md` that map observed evidence to the shipped design, including black/yellow/white conventions where evidenced, a summary-first sheet with explanatory text/comments, a three-alternative decision structure, and multiple supporting sheets suitable for a practical "en enkel modell" starting point.
- [x] Task 8: Validate the skill structure and references against skill-file standards, confirm the shipped skill never uses the real name, confirm the shipped skill is self-contained and not runtime-dependent on plan011 files, and record any evidence gaps or confidence limitations in the references. (validation report: .instructions/plans/plan012-stein-storken-style-skill/data/validation-task8-report.md)

## Acceptance Criteria

- [ ] A new skill folder exists for `repo/skills/stein-storken-style`.
- [ ] The shipped skill uses only the alias `Stein Storken` and does not use the real name.
- [ ] The skill is focused on text and Excel, with non-Excel document parsing explicitly treated as out of scope at this stage.
- [ ] The skill is self-contained and does not require runtime dependency on plan011 files.
- [ ] `SKILL.md` clearly explains when to use the skill and how to write in the Stein Storken style.
- [ ] The skill guidance and examples are Norwegian-first, and all included templates/examples intended for users are in Norwegian.
- [ ] The skill teaches the recurring delivery pattern of calling even large workbooks "en enkel modell".
- [ ] The skill teaches that "en enkel modell" may describe a large multi-sheet decision-support workbook rather than a literally simple file.
- [ ] The skill teaches a decision-support pattern centered on presenting three alternatives rather than making the final decision.
- [ ] The Excel guidance documents whether the first sheet is typically a summary/overview sheet with explanatory text/comments and carries that pattern into the templates where supported by evidence.
- [ ] At least one Excel template is included and reflects the observed black/yellow/white style conventions.
- [ ] At least one Excel template includes a summary-first multi-sheet structure suitable for a large supporting workbook with three alternatives.
- [ ] The Excel guidance distinguishes observed conventions from uncertain inferences, especially around older Office-era formatting assumptions.
- [ ] References include provenance notes showing that plan011 extracted fragments and Excel outputs were the main evidence base.
- [ ] The plan produces compact staging artifacts for text patterns, workbook inventory, and template design decisions so local parsing remains primary and any LLM use stays efficient.
- [ ] The skill passes relevant structural validation or, if validation tooling is unavailable, includes a documented manual validation check.

## Notes

- Prompt: `plan012-prompt.md`
- Draft: `plan012-draft.md`
- This plan is active for execution planning, but execution should still follow CatHerder task discipline: one task at a time, with immediate checkbox updates when tasks are completed.
- If the user later wants broader document-style emulation, that should likely be handled as a follow-up plan after the text-and-Excel foundation is complete.