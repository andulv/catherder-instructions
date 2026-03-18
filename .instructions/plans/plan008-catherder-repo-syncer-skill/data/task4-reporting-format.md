# Task 4 Reporting Format — Comparison and Sync Recommendation Output

Date: 2026-03-11T01:30:00+00:00
Plan: `plan008`

## Default Output Structure

### 1. Scope Summary
- repo A
- repo B
- compared surfaces
- exclusions or user-requested scope adjustments

### 2. Inventory Table
For each compared item include:
- path
- present in A? (`yes`/`no`)
- present in B? (`yes`/`no`)
- classification
- quick note

### 3. Findings by Item
For each material difference include:
- path
- difference summary
- why it matters
- likely status:
  - canonical improvement
  - local customization
  - operational/local-only
  - unresolved ambiguity

### 4. Recommendation Block
For each compared item include:
- recommendation: `sync A → B` / `sync B → A` / `merge manually` / `do not sync` / `needs canonical decision`
- confidence: `high` / `medium` / `low`
- rationale
- cautions

### 5. Directional Sync Summary
Provide a compact grouped summary:
- suggested A → B sync candidates
- suggested B → A sync candidates
- manual merge candidates
- do-not-sync items
- unresolved decisions

## Required Style Rules

- Keep the report concise and sortable by path.
- Explain *why* a recommendation exists, not just *what* differs.
- Call out risky items explicitly.
- Avoid overstating certainty when canonical status is unclear.
- If the user asks for a diff list only, the recommendation sections may be abbreviated but unresolved/risky items should still be flagged.

## Optional Follow-On Section

If the user wants execution planning, add:
- proposed sync order
- files to back up or review manually first
- patch sequencing notes
- explicit reminder that edits need user approval
