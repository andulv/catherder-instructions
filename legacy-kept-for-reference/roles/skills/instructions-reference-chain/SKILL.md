---
name: instructions-reference-chain
description: "Simulates how an agent traverses references from an entry file and maps the resulting context graph. Use to trace reading paths, estimate context size, detect cycles, and find unreachable instruction files."
---
# Instructions Reference Chain

Simulate agent context discovery by traversing references from a chosen
entry-point file.

## Entry Points

Default entry points when none are provided:
- `.github/copilot-instructions.md`
- `AGENTS.md`
- root Claude instruction file (tool convention)
- `.instructions/README.md`

## Simulation Procedure

### 1) Select Start Node

Pick the specified entry file. If omitted, start with known entry points.

### 2) Traverse References Depth-First

For each visited file:
- Parse markdown links and inline path references.
- Resolve and enqueue referenced files.
- Track depth and avoid revisiting already-seen files.

### 3) Build Context Graph

Capture:
- traversal order,
- edge relationships (A -> B),
- rough token estimate per file,
- cumulative tokens,
- max depth.

### 4) Detect Problems

Flag:
- **CIRCULAR**: cycle in reference chain.
- **ORPHAN**: file unreachable from any standard entry point.
- **DEAD END**: referenced file has no onward references.
- **BLOAT**: reachable content likely exceeds practical context budget.

## Output Format

```
## Reference Chain: [entry-point]

### Traversal
1. [entry-point] (N tokens)
   -> 2. [file-A] (N tokens)
      -> 3. [file-B] (N tokens)
   -> 2. [file-C] (N tokens)

### Summary
- Files reachable: N
- Total estimated tokens: N
- Max depth: N
- Circular references: none / [list]

### Issues
- ORPHAN: [file] — not reachable from standard entry points
- BLOAT: context from [entry] exceeds ~N tokens
- DEAD END: [file] — no onward references
- CIRCULAR: [file-A -> file-B -> file-A]
```

## Guardrails

- Never recurse indefinitely; maintain a visited set.
- Prefer report-first behavior; do not edit files unless asked.
- Treat unresolved references as input quality issues, not traversal failures.

## Scope Limits

- This skill maps discovery paths; it does not validate semantics.
- Pair with `instructions-reference-integrity` for link correctness.
- Pair with `instructions-consistency-analysis` for policy conflicts.
