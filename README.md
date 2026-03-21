# CatHerder Instructions Repository

CatHerder is an experimental lightweight operating model for **human + agent** software teams.

This repository is the source of truth for CatHerder conventions, templates, and reusable guidance.

CatHerder started as an attempt to create a set of instructions, documentation, and skills for GitHub Copilot in VS Code.
After some success, some weird LLM behavior, and much confusion, I discovered the system prompt for GitHub Copilot
in VS Code (see
[request-auto-gpt-5.3-Codex.md](docs/gh-copilot-prompts/request-auto-gpt-5.3-Codex.md),
[request-gemini-3.1-pro-preview.md](docs/gh-copilot-prompts/request-gemini-3.1-pro-preview.md),
[request-gpt-5.4.md](docs/gh-copilot-prompts/request-gpt-5.4.md),
[request-opus-4.6.md](docs/gh-copilot-prompts/request-opus-4.6.md)).

The next step was to test instructions with custom standalone agents, free from the VS Code / Copilot context. This has now evolved into the CatHerder application.

Current goals for catherder-instructions:
- Can be used with GitHub Copilot (VS Code, CLI, Cloud)
- Can be used with the CatHerder application
- Can be used with Claude Code, Cursor, and Codex

This probably cannot be achieved with a common directory structure or file format that fits all agents. We must either supply configuration settings for the various clients or have a script that initializes for different clients.

Projects using the CatHerder instructions process and methodology can be simultaneously developed across the different coding agents and frameworks listed above.


## What is here

- `.instructions/` — operational instructions for working in this repository
- `docs/catherder` — canonical source documentation for the CatHerder methodology
- `repo/` — published reusable artifacts consumed by CatHerder-enabled projects

## This repo is CatHerder-enabled

This repository uses CatHerder to operate on itself:

- use `.instructions/` to plan and execute work in this repo
- use `repo/` to publish reusable instructions, skills, templates, and related artifacts

For repository work, start with [`AGENTS.md`](AGENTS.md) or [`.instructions/project.instructions.md`](.instructions/project.instructions.md).
If resuming work, also read [`.instructions/SCRATCHPAD.md`](.instructions/SCRATCHPAD.md).

## Status

This repository is evolving as CatHerder conventions are refined and validated across different agents and editors.
