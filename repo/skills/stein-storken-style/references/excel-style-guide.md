---
type: reference
description: "Observed Excel workbook conventions, layout tendencies, and template design guidance for Stein Storken style, derived from plan011 workbook inspection."
snapshot_date: 2026-03-23
sources:
  - .instructions/plans/plan012-stein-storken-style-skill/data/source-inventory.md
  - .instructions/plans/plan012-stein-storken-style-skill/data/excel-workbook-inventory.json
  - .instructions/plans/plan011-svein-email-and-attachment-extraction/output/manifests/candidate-documents.jsonl
---
# Stein Storken Excel Style Guide

Condensed workbook-style reference derived from deterministic inspection of `.xlsx` files from the authoring corpus snapshot used for this skill.

## Scope

- Covers workbook architecture, first-sheet patterns, visible formatting signals, headings, and template implications.
- Does not claim exact historical Office version.
- Distinguishes observed signals from safe inference.

## Evidence basis

- Workbook candidates inspected locally: 5 `.xlsx` files from the authoring corpus snapshot.
- Strongest workbook-architecture signals come from the two `Analyse PD AS og GRO PRO AS ...` workbooks.
- Yellow fill and black/default styling recur across multiple files.

## Hard rules

- Deliver workbook outputs in **Norwegian**.
- Prefer a **summary-first workbook structure** when the workbook supports a decision or comparison.
- The first sheet should usually tell the receiver **what the model shows**, not only contain raw numbers.
- When the workbook supports a strategic choice, present **three alternatives** or an equivalent three-part comparison structure.
- It is acceptable to introduce a large workbook as **"en enkel modell"** even when the file contains several supporting sheets; this is a recurring rhetorical framing device.
- Keep workbook sections purposeful and label-driven.

## Strong repeated patterns

### Workbook architecture

Observed:
- single-sheet operational files exist (`Salgsrapport ...`, `Vedlegg2 ...`)
- multi-sheet analysis files also exist and are especially important for this skill
- analysis workbooks include a first-sheet framing layer before deeper supporting sheets

Practical guidance:
- Do not assume "simple" means one sheet.
- For decision-support workbooks, prefer:
  1. a summary/overview sheet first
  2. supporting calculation or detail sheets after that

### First-sheet summary / explanation pattern

Observed strongest in:
- `090126 Analyse PD AS og GRO PRO AS fra 2022 til 2025 oppdatert.xlsx`
- `060126 Analyse PD AS og GRO PRO AS fra 2022 til 2025.xlsx`

Observed signals:
- first sheet contains headings and explanatory text
- numbered comments / issue notes appear directly on the first sheet
- first sheet frames comparison before detailed sheets are read

Practical guidance:
- Put explanatory text, assumptions, comments, or decision framing on the first sheet.
- Let the first sheet answer: **what is this, what should be compared, and what matters most?**

### Three-part comparison structure

Observed / inferred from workbook evidence:
- explicit `1/3 PD`, `1/3 GP`, `1/3 TOTALT` headings in one workbook
- comparison-oriented column groups and overordnet nøkkeltall framing
- strong user requirement that large workbooks often present three options

Practical guidance:
- Use three alternatives as the default decision-support structure when applicable.
- Alternatives may be labelled directly as `Alternativ 1/2/3` or represented through three comparison blocks when that reads more naturally.

### Formatting signals

Observed:
- black/default text dominates
- yellow fill is present in multiple workbooks
- merged heading ranges are common in analysis-style sheets
- header blocks and label sections are more important than decorative styling

Practical guidance:
- Use black text as the default.
- Use yellow fill selectively to highlight assumptions, key values, or areas needing attention.
- Use white/neutral background elsewhere.
- Prefer bold section headings and merged label areas when they improve readability.

## Soft tendencies

- Tab names are functional, often tied to company/entity names or topic names.
- The first sheet may have broad headings rather than polished presentation language.
- Commentary can sit in cells on the right side of a sheet, not only in formal Excel comments.
- The workbook may mix summary, assumptions, and comparison logic in a pragmatic rather than elegant way.

## Uncertain / use with caution

- Exact font family and exact Office-era defaults were not established strongly enough to make them hard rules.
- Not every workbook shows an explicit `Alternativ 1/2/3` label set.
- Color-theme codes suggest style consistency, but exact RGB interpretation of themed colors is less certain than direct yellow fill evidence.

## Template guidance

For a reusable Stein Storken-style workbook template, prefer:

1. **First sheet: `Oppsummering`**
   - short explanatory text near the top
   - purpose statement using `en enkel modell`
   - three alternative blocks
   - comment / vurdering area

2. **Supporting sheets** such as:
   - `Alternativ 1`
   - `Alternativ 2`
   - `Alternativ 3`
   - `Forutsetninger`

3. Visual conventions:
   - black text default
   - yellow fill for assumptions / attention points
   - white/neutral general canvas
   - bold headings and simple borders

## Notes

- The style signal is primarily architectural and rhetorical, not merely cosmetic.
- A workbook can be introduced as modest while still containing extensive supporting detail.