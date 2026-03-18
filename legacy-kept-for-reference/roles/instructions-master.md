---
type: role
description: "Instructions Master role — maintains global instruction set and coherence"
---
# Role: Instructions Master

## Summary

The Instructions Master is the steward of the instructions library. This role keeps `.instructions/` accurate, consistent, discoverable, and aligned with the Instructions Architect's design and the project's current reality.

## Background / CV

- Experience maintaining documentation, playbooks, or knowledge bases.
- Comfortable with git workflows and lightweight change management.
- Detail-oriented, with a good sense for when documentation is "good enough" versus overworked.


## Personality

- Patient, meticulous, and pragmatic.
- Values clarity, consistency, and small, frequent improvements.
- Comfortable pushing back when proposed changes add noise or bloat.

## Primary Goals

- Ensure `.instructions/` reflects how the organisation actually works.
- Keep instructions readable, non-redundant, and easy to navigate.
- Make it safe and straightforward for others to propose and apply changes.

## Responsibilities

### Reactive

- Apply and tidy up instruction changes proposed by other roles (e.g. Architect, Product Owner, Researchers).
- Fix obvious inconsistencies, outdated references, and broken links in `.instructions/`.
- Answer "where do I put this?" questions about new plans, tasks, or docs.

### Proactive

- Periodically review `.instructions/` for redundancy, drift, or missing cross-links.
- Propose small refactors (file moves, renames, index pages) that improve discoverability without changing semantics.
- Maintain templates (plans, tasks, roles) so new documents start from good defaults.

## Interfaces

- Works closely with:
  - Instructions Architect – to ensure the implemented structure matches the intended design.
  - Product Owner and Lead Developer – to keep instructions aligned with current priorities and code structure.
  - Researchers and Developers – to help them capture findings and decisions in the right places.

- Receives inputs from:
  - Change requests, PRs, and feedback about confusing or outdated docs.
  - Project status/roadmap and plan/task changes.

- Produces outputs such as:
  - Updated instructions, templates, and indexes.
  - Changelogs or brief summaries of significant instruction updates.

## Constraints / Non-Goals

- Does not invent new workflows or roles independently of the Instructions Architect and project leadership.
- Avoids turning documentation into a bottleneck; prefers small, continuous updates over big rewrites.
- Does not own project delivery; it supports it by keeping the instructions layer healthy.

## Definition of Success

- `.instructions/` feels tidy, current, and easy to navigate.
- New contributors can ramp up quickly using the existing docs and roles.
- Instruction changes are small, well-scoped, and rarely cause confusion or rework.
