---
name: instructions-format-validation
description: "Validates .instructions/ files for structural correctness: YAML front-matter, markdown structure, naming conventions, and timestamp format. Use when asked to review, audit, validate, or check instruction files for format compliance. Also use when creating new instruction files to ensure they follow conventions."
---
# Instructions Format Validation

Validate `.instructions/` files against the project's format conventions.
This skill uses a deterministic script for mechanical checks. Manual judgment
is only needed for `UNCERTAIN` results.

> **Requires:** `python-frontmatter` installed in `.venv`  
> First-time setup: `.venv/bin/pip install -r .claude/skills/instructions-format-validation/scripts/requirements.txt`

## Validation Procedure

### Step 1: Run deterministic validator

```
.venv/bin/python .claude/skills/instructions-format-validation/scripts/validate.py <target-path>
```

`<target-path>` is a single `.instructions/` markdown file or a directory
(recursively validates all `*.md` files). Script is read-only, outputs JSON.

### Step 2: Resolve `UNCERTAIN` findings manually

For each `UNCERTAIN` result (e.g. synonym section names like "Success Criteria"
vs required "Acceptance Criteria"), consult `references/expected-structures.md`
to decide PASS or FAIL. Authoritative source:
`.instructions/plans/TEMPLATE.md` and `.instructions/plans/tasks/TEMPLATE.md`

### Step 3: Report in standard format

Convert JSON output plus any manual judgments into the report format below.

## Output Format

Report findings per file using this structure:

```
## Findings: [filename]

- **[PASS]** Front-matter: valid, type=plan, description present
- **[FAIL]** Structure: missing required section "Acceptance Criteria"
- **[FAIL]** Naming: file uses underscore (expected kebab-case)
- **[WARN]** Timestamp: Updated field uses bare date without time
- **[PASS]** Headings: sequential hierarchy, one H1

### Summary: N passed, N failed, N warnings
```

Severity levels:
- **FAIL** — must fix, violates a required convention
- **UNCERTAIN** — ambiguous; apply manual judgment (see Step 2)
- **PASS** — correct

## Scope

This skill checks files under `.instructions/` only. It does not validate:
- Source code files
- Non-instruction markdown (README.md at repo root, AGENTS.md, and tool-specific instruction files)
- Files in `.github/skills/` or `.claude/skills/` (those follow the Agent
  Skills spec, not .instructions/ conventions)

## When NOT to Use

- For checking links or references → use `instructions-reference-integrity`
- For finding contradictions across files → use `instructions-consistency-analysis`
- For tracing what an agent sees → use `instructions-reference-chain`
