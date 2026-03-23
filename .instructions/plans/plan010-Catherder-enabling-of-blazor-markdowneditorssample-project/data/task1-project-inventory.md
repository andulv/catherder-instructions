# Task 1 — Target project inventory

Created: 2026-03-22T00:40:39+00:00

## Repository identity

- Project: `tmp-blazor-markdowneditorssample`
- Type: ASP.NET Blazor sandbox / sample application
- Purpose: evaluate and compare multiple markdown editors in one Blazor app
- Current CatHerder state: not enabled at start of execution

## Relevant structure observed

- `README.md` — project overview, integration notes, and run instructions
- `Blazor-MarkdownEditorsSample.slnx` — solution entry
- `src/MarkdownEditorsSample.Blazor/` — application project
- `.vscode/` — local editor configuration
- No `AGENTS.md`
- No `.instructions/`
- No `.agents/`

## Technical characteristics

- Language/runtime: .NET / C#
- Frontend framework: ASP.NET Blazor
- Editor integrations include MudMarkdown, Cherry, Toast UI, Vditor, Milkdown, and Tiptap
- Uses JavaScript interop for browser-first editors
- App configuration via `appsettings.json` and `appsettings.Development.json`
- File browser root points to local `data/` directory according to README

## Development / execution commands from README

From repository root:

- `dotnet build src/MarkdownEditorsSample.Blazor/MarkdownEditorsSample.Blazor.csproj`
- `dotnet run --project src/MarkdownEditorsSample.Blazor/MarkdownEditorsSample.Blazor.csproj`

## Technical concerns likely relevant to project instructions

- Blazor component lifecycle and JS interop coordination
- editor initialization and disposal
- content synchronization between JS editors and C# state
- script and stylesheet load ordering
- deterministic local test data scope via `data/`

## Enablement implications

- Project is a good fit for standard CatHerder software-project bootstrap
- Similar enough to `tmp-catherder-dev` to reuse concise .NET / Blazor project guidance patterns
- Must avoid catherder-dev-specific content related to agent orchestration, MAF, and provider abstractions
- Likely project phase for roadmap: `Prototype`
