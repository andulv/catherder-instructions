# Plan 011 Prompt

Prepare and execute a non-destructive workflow for the `reference/` folder to identify text written by Svein Skorpen and documents likely created by him.

Known direct identity clue:
- `svein@byrknes.no`

This is a sampling workflow. The goal is to build good and extensive samples of Svein's communication style and likely document formats and contents. It is acceptable to miss some relevant material, but retained text should be likely written by Svein rather than by others.

Goals:
- use the confirmed Maildir mailbox structure in `reference/` as the primary source format
- identify text fragments likely written by Svein using sender metadata, forwarded/quoted mail structure, and practical heuristics
- filter out surrounding email text written by others when practical
- export extracted Svein-authored text into human-friendly, LLM-friendly text files
- save attachments associated with retained relevant messages using original filenames with collision-safe naming
- identify documents likely created by Svein using clues from mail text, filenames, and surrounding context
- produce auditable manifests showing what matched and why

Constraints:
- do not modify original source files under `reference/`
- prefer retaining text likely written by Svein over maximizing recall
- keep provenance from extracted text and documents back to the containing message
- keep the main workflow mostly local and deterministic; if LLM help is needed, use compact staged records rather than raw mailbox data
