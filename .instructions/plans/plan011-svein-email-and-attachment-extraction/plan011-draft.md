---
type: plan
description: "Plan 011 draft — Prepare a non-destructive workflow to find Svein-authored emails and likely Svein-authored attachments in reference archives"
---
# Plan 011 Draft: Svein Email and Attachment Extraction

**Status:** `draft`

**Created:** 2026-03-23T00:00:00+00:00

**Updated:** 2026-03-23T00:00:00+00:00

## Goal

Prepare a safe, efficient extraction plan for the `reference/` folder that produces a good, extensive sample of text written by Svein Skorpen and collects attachments likely created by him.

## Context / Why

The `reference/` folder contains an archive of emails and attachments. Initial inspection shows a Maildir-style mailbox under `reference/mailbox-anders-plantedamp/`, with standard folders such as `Inbox`, `Archive`, `Sent`, and `Trash`, each containing `cur` / `new` / `tmp`. This means the archive is directly accessible with Python standard-library email parsing and does not currently require PST-specific tooling.

A light probe also confirmed multiple exact `From:` matches for `Svein Skorpen <svein@byrknes.no>`, so the archive definitely contains relevant material.

The user wants a broader extraction target than sender matching alone: find mail text written by Svein regardless of who sent, received, or forwarded the message, and filter out surrounding text written by others when practical. This is a sampling workflow rather than a full recall workflow: it is acceptable to miss some Svein-authored material, but retained text should be likely to have been written by Svein rather than by others. For attachments, the working goal is to collect documents likely created by him based on clues in mail text, filename patterns, and other practical signals.

This requires separating archive inventory, text attribution within messages, output design, and document clue collection so the later execution can be audited and tuned without losing provenance.

## Intended Outputs

- A confirmed Maildir-based archive handling approach for the contents in `reference/`
- A text-attribution approach for extracting only the parts of email text likely written by Svein
- A proposed export structure for readable Svein-authored text fragments and associated attachments
- A clue-based approach for collecting Excel, Word, PDF, and other documents likely created by Svein based on mail references and filename patterns
- Auditable manifests capturing source, extracted text scope, match reason, and confidence

## Candidate Workflow Shape

### Phase 1: Inventory
- Confirm and document the Maildir folder structure under `reference/`
- Enumerate mail folders and estimate where relevant material is concentrated
- Separate message files from any standalone documents or compressed material

### Phase 2: Svein text detection
- Match direct sender hits for `svein@byrknes.no` and `Svein Skorpen`
- Expand to forwarded, quoted, or embedded mail text likely written by Svein even when another person sent the containing message
- Heuristically isolate fragments likely written by Svein and filter out surrounding text written by others
- Keep ambiguous extractions in a review bucket rather than retaining obvious non-Svein text

### Phase 3: Text and attachment export
- Export Svein-authored text fragments into a readable text-first format that remains human- and LLM-friendly
- Preserve provenance to the containing message and relevant headers
- Save attachments linked to retained relevant messages with original filenames preserved through collision-safe naming

### Phase 4: Document clue collection
- Look for references in mail text that suggest a document was written by Svein
- Use filename patterns, naming habits, and surrounding mail context as practical authorship clues
- Collect candidate files permissively while still recording why they were included
- Record confidence and evidence for each candidate document

## Risks / Questions

- The archive format is now partially confirmed as Maildir, but there may still be standalone documents or nested material elsewhere under `reference/` that need separate handling.
- Extracting only the text written by Svein inside forwarded or quoted threads is heuristic and may occasionally miss valid Svein-authored text.
- The workflow should favor retaining text likely written by Svein over maximizing total text volume.
- Document authorship is to be inferred from mail references, filename style, and surrounding context rather than metadata, so evidence quality will vary.
- Formatting preservation is best approximated through a text-first export of the extracted Svein-authored fragments.

## Proposed Tooling

- `python3` for Maildir parsing, heuristic text extraction, attachment collection, and manifest generation
- shell tools such as `find` and `grep` for quick inventory support
- optional Python HTML/text helpers if richer email-body normalization is needed
- optional LLM review later only on compact extracted records, not raw mailbox data

## Notes

- Prompt: `plan011-prompt.md`
- Planning-only session. No extraction or file copying should start until an active plan exists.
- The execution plan should stay non-destructive and preserve source-to-output traceability.
