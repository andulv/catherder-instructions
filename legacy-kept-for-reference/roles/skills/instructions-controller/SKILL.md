---
name: instructions-controller
description: >
  Orchestrates .instructions/ quality checks across repos. Use when asked to
  review, audit, or validate instruction files, check overall health of the
  instructions structure, find broken links, detect contradictions, trace
  context graphs, or verify compliance with file format conventions. Routes
  requests to specialized skills and produces a unified report.
---
# Instructions Controller

This is a **routing adapter**. The full agent specification lives at:

> `.instructions/agents/instructions-controller.agent.md`

Read that file for the complete definition including:
- Skill dispatch table (which skill handles which request)
- Output format specification
- Stop rules and escalation policy
- Configuration options
- Composite request handling (full audit, health check, deep review)

## Quick Reference

| Request | Routed to |
|---|---|
| Format / front-matter / structure | `instructions-format-validation` |
| Links / references / anchors | `instructions-reference-integrity` |
| Contradictions / duplicates / policy | `instructions-consistency-analysis` |
| Context graph / traversal / reachability | `instructions-reference-chain` |
| Standards / conventions / spec | `agent-file-standards` |

## Default Behavior

- **Report-only** — never edit unless explicitly asked.
- **Auto-route** — infer which skills to invoke from the request.
- **Stop on ambiguity** — flag uncertain findings, escalate structural changes.
