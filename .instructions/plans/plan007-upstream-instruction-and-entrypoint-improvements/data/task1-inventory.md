# Task 1 Inventory — Instruction and Entrypoint Improvements

Date: 2026-03-09T00:00:00+00:00
Plan: `plan007`

## Canonical Defaults

These improvements should become default guidance for CatHerder-enabled projects:

- Use a single authoritative source for repository-specific document entry guidance.
- Keep `AGENTS.md` as a minimal bootstrap/entry file; do not duplicate workflow rules there.
- Use markdown links for referenced instruction files.
- Replace blanket startup read-order lists with a document map that states what each file is and when to read it.
- Distinguish reading guidance as:
  - required
  - operational
  - conditional
- Treat `project-status-roadmap.md` as conditional context, not universally required startup reading.
- Treat `SCRATCHPAD.md` as resume/continue context and session-end handoff memory.
- State clearly that `catherder.instructions.md` is workflow authority.
- State clearly that `catherder-git.instructions.md` is mandatory when present and git/repository-change work is involved.
- Add ignore-by-default search/scan guidance for noise-heavy paths such as `.git/`, `.venv/`, and generated/cache directories.
- Improve repository-structure guidance so agents can distinguish operational files, canonical reusable artifacts, and legacy/reference areas.
- Prefer concise, imperative, low-ambiguity wording optimized for agent execution.

## Optional Guidance

These are useful patterns but should be framed as optional or adaptable by repository:

- Exact section labels for document maps (`Required`, `Operational`, `Conditional`).
- Exact ignore-by-default examples beyond core defaults (`node_modules/`, `.idea/`, `.vs/`, `bin/`, `obj/`).
- Exact wording for repository-structure examples beyond the canonical enabled-project baseline.
- Whether `project.instructions.md` contains a full repository tree or a shorter orientation block.

## Repository-Local Only

These improvements are local to this repository and should not be upstreamed as defaults:

- Structure descriptions that reference this repository’s specific folders such as `repo/`, `docs/catherder/`, or `legacy-kept-for-reference/`.
- This repository’s distinction between editing `.instructions/` versus editing canonical docs under `docs/catherder/`.
- This repository’s local plan numbers, branch names, and session notes.
- This repository’s exact local agent/runtime layout under `.agents/`.

## Notes

- Existing catalog templates still use a rigid reading-order model and should be updated.
- Canonical docs currently do not describe minimal `AGENTS.md` bootstrap behavior.
- Canonical docs and reusable templates should align on when roadmap and scratchpad are read.
