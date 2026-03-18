---
name: agent-file-standards
description: "Provides a dated offline summary of AGENTS.md, Agent Skills, Copilot, and Claude skill/file conventions. Use when defining skill layout, resolving standards questions, or checking cross-tool compatibility assumptions."
---
# Agent File Standards (Snapshot Reference)

Use this skill when you need a quick, offline standards baseline for agent
entry points and skill packaging across tools.

This skill is intentionally concise. The detailed snapshot lives in:

- `references/snapshot-2026-03.md`

## How to Use

1. Read the snapshot section relevant to your question (AGENTS.md, Agent Skills,
   Copilot, Claude, or local `.instructions/` conventions).
2. Treat the snapshot as orientation, not absolute truth.
3. Re-verify important details against the linked canonical sources before
   making final implementation decisions.

## Scope

- Focuses on file placement, discovery behavior, and skill structure.
- Does not replace project-specific workflow contracts.
- Does not enforce or validate files directly; use dedicated validation skills
  for checks.
