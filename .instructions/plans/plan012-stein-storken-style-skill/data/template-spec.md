# Plan 012 Template Specification

Maps observed workbook evidence to shipped Stein Storken-style template assets.

## Evidence-informed decisions

- Summary-first workbook structure is based primarily on the analysed `Analyse PD AS og GRO PRO AS ...` workbooks.
- Explanatory text on the first sheet is carried into both templates.
- Yellow fill is used selectively because direct yellow-fill evidence appears in multiple inspected workbooks.
- Three-alternative structure is made explicit in one template because the user requirement is strong and workbook evidence supports comparison framing, even when labels are not always written exactly as `Alternativ 1/2/3`.
- Multi-sheet supporting structure is included to match the observed pattern that an "enkel modell" may still be a substantial workbook.

## Shipped templates

### 1. `stein-storken-enkel-modell-template.xlsx`
- `Oppsummering` first sheet
- supporting sheets: `Alternativ 1`, `Alternativ 2`, `Alternativ 3`, `Forutsetninger`
- first sheet contains explanatory wording, comparison table, and comment area
- intended as the default decision-support workbook starter

### 2. `stein-storken-tre-alternativer-template.xlsx`
- `Oppsummering` first sheet
- supporting sheets: `Underlag A`, `Underlag B`, `Underlag C`
- more compact comparison layout, still clearly three-part
- intended for simpler side-by-side structured recommendation cases

## Deliberate safe inference

- Exact historical font defaults are not treated as hard evidence; Arial is used as a clean, practical default.
- Exact office theme colors beyond direct yellow evidence are simplified into black / yellow / white conventions.
- The templates are starting structures, not claims of exact historical reconstruction.
