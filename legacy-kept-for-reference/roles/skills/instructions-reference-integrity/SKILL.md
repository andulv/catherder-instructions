---
name: instructions-reference-integrity
description: "Checks links, anchors, and path references inside .instructions files. Use when asked to verify references, find broken links, validate reading-order paths, or audit entry-point link health."
---
# Instructions Reference Integrity

Validate internal references in `.instructions/` content: markdown links,
anchor fragments, and inline path mentions.

Use the deterministic script for all checks — do not perform these checks
manually. All script paths below are relative to this skill's directory.

## Procedure

### Step 1: Run the script

```skill-run
script: scripts/validate_references.py
python: any        # no external deps; any Python 3 in PATH works
args:
  target:
    description: file or directory to scan (recursively checks *.md)
    default: .instructions
  --workspace-root:
    description: repo root for resolving workspace-relative inline paths
    default: .
  --no-inline-paths:
    description: skip backtick inline path checks; only check link targets and anchors
    default: false
output: json
exit-nonzero-on-findings: true
```

### Step 2: Interpret results

JSON output contains a `findings` array and a `summary`. Each finding has:
- `file`, `line` — source location
- `target` — the reference that failed
- `code` — `FILE_NOT_FOUND` | `ANCHOR_NOT_FOUND` | `INLINE_PATH_NOT_FOUND`

Zero findings = clean. Non-zero exit code = broken references found.

### Step 3: Report findings

```
## Reference Integrity: [scope]

### Broken links
- [source-file:line] -> [target] — FILE_NOT_FOUND
- [source-file:line] -> [target#anchor] — ANCHOR_NOT_FOUND

### Summary
- Files scanned: N, links checked: N, broken: N
```

## Finding Codes

- `FILE_NOT_FOUND` — link target path does not exist on disk.
- `ANCHOR_NOT_FOUND` — file exists but the `#fragment` is not a heading in it.
- `INLINE_PATH_NOT_FOUND` — backtick-quoted path-like string does not resolve.

## Scope Limits

- Focuses on instruction references, not semantic policy conflicts.
- For contradictions and policy drift, use `instructions-consistency-analysis`.
- For format/schema checks, use `instructions-format-validation`.
