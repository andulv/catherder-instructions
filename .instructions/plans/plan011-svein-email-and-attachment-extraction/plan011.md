---
type: plan
description: "Plan 011 — Extract Svein-authored mail text and likely Svein-created documents from reference mail archives"
---
# Plan 011: Svein Email and Attachment Extraction

**Status:** `completed`

**Branch:** `plan/011-svein-email-and-attachment-extraction`

**Created:** 2026-03-23T00:00:00+00:00

**Updated:** 2026-03-23T01:20:00+00:00

## Goal

Extract a good, extensive sample of text written by Svein Skorpen from the `reference/` mail archive, even when that text appears inside forwarded or quoted messages, and collect documents likely created by him based on permissive context clues.

## Context / Why

The `reference/` folder contains a Maildir-style mailbox under `reference/mailbox-anders-plantedamp/`, with standard mail folders such as `Inbox`, `Archive`, `Sent`, and `Trash`. Initial probing confirmed multiple exact `From:` matches for `Svein Skorpen <svein@byrknes.no>`, so the archive definitely contains relevant material and can be parsed directly with Python standard-library tooling.

The target is broader than sender matching alone. The user wants the mail text written by Svein regardless of who sent, received, or forwarded the containing message, with surrounding non-Svein text filtered out where practical. This is a sampling workflow, not a full forensic extraction: recall does not need to be perfect, but retained text should be text likely written by Svein rather than by others. The user also wants candidate documents likely created by him, inferred primarily from mail references, filename patterns, and contextual clues rather than strict metadata proof.

## Output Structure

- `data/inventory.md` — confirmed archive structure, tool availability, and initial direct-match findings
- `data/heuristics.md` — heuristic rules, evidence codes, fragment types, and confidence meanings
- `data/verification.md` — sample-review findings, false-positive observations, and follow-up tuning notes
- `output/fragments/` — readable extracted Svein-authored text fragments
- `output/attachments/` — saved attachments from retained relevant messages with collision-safe naming
- `output/manifests/fragments.jsonl` — auditable text-fragment manifest
- `output/manifests/candidate-documents.jsonl` — auditable candidate-document manifest

## Heuristic Expectations

- Prefer precision over completeness for retained text fragments: it is acceptable to miss some Svein-authored text if that helps avoid retaining text clearly written by others.
- Use local deterministic heuristics first; LLM use, if any, should be limited to later review of compact extracted records rather than raw mailbox data.
- Normalize evidence into short codes such as `FROM_EXACT`, `QUOTED_FROM_MATCH`, `FORWARDED_FROM_MATCH`, `SIGNATURE_MATCH`, `FILENAME_MATCH`, and `MAIL_TEXT_REFERENCE`.
- Use simple confidence bands such as `high`, `medium`, and `review`.
- Export whole-body text only for direct high-confidence Svein messages; for forwarded or quoted material, export only segmented blocks likely written by Svein.
- Keep ambiguous fragments only when clearly marked for review; do not retain obvious non-Svein text just to increase sample volume.

## Manifest Minimum Fields

### Fragment manifest

Each fragment record should include at least:
- `message_id`
- `source_path`
- `mailbox_folder`
- `top_level_from`
- `fragment_id`
- `fragment_type`
- `confidence`
- `evidence_codes`
- `text`

### Candidate-document manifest

Each candidate document record should include at least:
- `message_id`
- `attachment_filename`
- `saved_path`
- `sha256`
- `confidence`
- `evidence_codes`
- `evidence_note`

## Tasks

- [x] Task 1: Record the confirmed archive structure, available tooling, and known direct Svein matches in `data/inventory.md`.
- [x] Task 2: Design and document the heuristic rules in `data/heuristics.md`, including evidence codes, fragment types, confidence bands, and rules for excluding obvious non-Svein text.
- [x] Task 3: Implement the export structure, manifest formats, and non-destructive extraction script so it writes auditable fragment records and readable text outputs under `output/`.
- [x] Task 4: Implement attachment export for retained relevant messages with original filenames preserved through collision-safe naming and provenance captured in manifests.
- [x] Task 5: Implement a permissive document-candidate pass that flags attachments likely created by Svein using mail-text references, filename patterns, and surrounding context, with evidence notes recorded in `output/manifests/candidate-documents.jsonl`.
- [x] Task 6: Verify results by reviewing at least 5 direct matches, 5 quoted/forwarded matches, and 5 candidate documents, then record quality observations and tuning needs in `data/verification.md`.
- [x] Task 7: Tighten fragment extraction so direct Svein messages separate likely Svein-authored primary text from clearly bounded quoted context by others when useful. Output: updated extraction rules, script changes, and regenerated fragment outputs with explicit authorship/context marking.
- [x] Task 8: Tighten embedded-fragment retention by removing `SIGNATURE_MATCH`-only captures, requiring stronger bounded evidence such as explicit quoted or forwarded Svein sender lines, and preserving non-Svein context only when clearly marked as context. Output: updated heuristic rules, script changes, and regenerated fragment outputs.
- [x] Task 9: Refine candidate-document classification to distinguish between likely Svein-created documents and generally relevant Svein-related attachments, then regenerate candidate manifest records. Output: updated candidate-document manifest semantics and regenerated manifest.

## Acceptance Criteria

- [x] The plan records the confirmed Maildir structure and currently available/missing tooling relevant to the workflow.
- [x] The workflow can identify direct `From:` matches for `Svein Skorpen <svein@byrknes.no>` and expand beyond them using documented heuristics.
- [x] The extraction approach targets text written by Svein even when embedded in forwarded or quoted threads.
- [x] Retained text is sampling-oriented but avoids retaining text clearly written by others.
- [x] Direct-message extraction separates likely Svein-authored primary text from clearly marked quoted context by others where useful.
- [x] Embedded-fragment extraction does not retain recipient-list/header-only blocks that merely mention or include Svein, and any retained non-Svein context is explicitly marked as context.
- [x] Output files are text-first, human-friendly, LLM-friendly, and preserve traceability back to the containing message.
- [x] Fragment and candidate-document manifests use documented minimum fields and evidence codes.
- [x] Attachments associated with retained relevant messages are saved with original filenames preserved through collision-safe naming.
- [x] Candidate documents are collected using permissive contextual clues, with reasons recorded for later review.
- [x] Original source files under `reference/` remain unchanged.

## Notes

- Prompt: `plan011-prompt.md`
- Draft: `plan011-draft.md`
- The plan is sampling-oriented: it should produce good and extensive material for learning Svein's communication style and likely document patterns without requiring exhaustive recall.
- Execution should remain non-destructive, mostly local, and focused on preserving source-to-output traceability.
- Verification in `data/verification.md` found that the first-pass pipeline works but needs stricter fragment filtering and explicit context marking before the corpus is treated as clean Svein-style sample text.
