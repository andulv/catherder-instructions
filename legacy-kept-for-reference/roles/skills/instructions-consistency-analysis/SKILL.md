---
name: instructions-consistency-analysis
description: "Detects contradictions, duplicated policy statements, and precedence ambiguities across .instructions files. Use for consistency reviews, conflict detection, and policy deduplication audits."
---
# Instructions Consistency Analysis

Analyze `.instructions/` content for policy consistency problems that format and
link checks do not catch.

## Method

### 1) Identify Policy Domains

Start with domain definitions in:
- `references/known-policy-domains.md`

### 2) Gather Claims Per Domain

For each domain, list files that make explicit claims or rules.

### 3) Compare Claims

Compare statements pairwise and classify each relationship as:
- **CONFLICT**: claims cannot both be true.
- **DUPLICATE**: same policy repeated without reference.
- **AMBIGUOUS**: both claims may apply, but precedence is unclear.
- **CONSISTENT**: aligned and non-conflicting.

### 4) Recommend Reconciliation

For each issue, propose the minimal corrective action:
- pick canonical source,
- delete duplicate text and cross-reference, or
- add explicit scope/precedence wording.

## What to Check

1. Contradicting rules across files.
2. Duplicated policies with drift risk.
3. Role and skill scope overlap.
4. Org-vs-project precedence ambiguity.

## Output Format

```
## Consistency Analysis: [scope]

### Conflicts
- CONFLICT: [topic] — [file-A] says X, [file-B] says Y
  Recommendation: [how to reconcile]

### Duplicates
- DUPLICATE: [topic] — restated in [file-A] and [file-B]
  Recommendation: consolidate into [canonical-file]

### Ambiguities
- AMBIGUOUS: [topic] — both [file-A] and [file-B] apply
  Recommendation: add explicit precedence

### Clean
- N policy domains checked, N consistent
```

## Scope Limits

- This is analysis-only by default; do not auto-edit unless asked.
- Use `instructions-format-validation` for structural checks.
- Use `instructions-reference-integrity` for broken links and anchors.
