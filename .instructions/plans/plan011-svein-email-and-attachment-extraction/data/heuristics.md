# Plan 011 Heuristics

**Created:** 2026-03-23T00:00:00+00:00
**Updated:** 2026-03-23T01:00:00+00:00

## Purpose

Document the first-pass local heuristic rules for extracting text likely written by Svein Skorpen and for flagging candidate documents likely created by him.

This workflow is sampling-oriented. It is acceptable to miss some Svein-authored material, but retained primary text should be likely to have been written by Svein rather than by others. Clearly bounded quoted context by others may be kept when useful for understanding what triggered Svein's response, but it must be explicitly marked as context.

## Extraction priorities

1. Retain high-confidence text likely written by Svein as primary sample text.
2. Avoid retaining text clearly written by other people as if it were Svein-authored.
3. Preserve clearly bounded quoted context by others only when it helps explain Svein's response and can be explicitly marked as context.
4. Keep ambiguous text only when it has useful supporting evidence and can be clearly marked for review.
5. Favor local deterministic parsing over LLM inference during the main extraction pass.

## Identity clues

Primary direct identity clues:
- exact email: `svein@byrknes.no`
- exact display name: `Svein Skorpen`

Secondary supporting clues:
- quoted or forwarded `From:` lines containing the exact name or email
- signature blocks containing the exact name or email together with bounded Svein-authored content
- surrounding mail text explicitly referring to Svein as author of an attached or discussed document

## Fragment types

Use one of these fragment types in the fragment manifest:
- `direct_primary` — primary authored text from a direct high-confidence Svein-sent message
- `quoted_context` — clearly bounded quoted context from another person retained for response context
- `quoted_svein` — quoted text block attributed to Svein inside another message
- `forwarded_svein` — forwarded message block attributed to Svein inside another message
- `review_block` — ambiguous retained block kept for review

## Evidence codes

Use short evidence codes in manifests and notes:
- `FROM_EXACT` — top-level `From:` exactly matches Svein name or email
- `FROM_EMAIL_MATCH` — top-level `From:` contains `svein@byrknes.no`
- `FROM_NAME_MATCH` — top-level `From:` contains `Svein Skorpen`
- `QUOTED_FROM_MATCH` — quoted block includes a matching `From:` line for Svein
- `FORWARDED_FROM_MATCH` — forwarded block includes a matching `From:` line for Svein
- `QUOTED_CONTEXT_PRESENT` — retained quoted context is present and explicitly marked as non-Svein context
- `MAIL_TEXT_REFERENCE` — surrounding mail text refers to Svein as author or sender of the relevant content
- `FILENAME_MATCH` — attachment filename supports likely Svein authorship or work-product relevance
- `THREAD_CONTEXT_MATCH` — subject/thread context supports Svein relevance but is not sufficient alone

## Confidence bands

- `high` — strong direct evidence that the retained text or document is by Svein
- `medium` — useful supporting evidence, acceptable for sampling, but not fully direct
- `review` — ambiguous material retained for later inspection; should be limited

## Text retention rules

### Direct Svein messages

When top-level `From:` is a high-confidence Svein match:
- retain the leading authored portion as `direct_primary`
- stop primary retention at clear quoted-history markers such as reply headers, forwarded-message separators, or inline header runs
- optionally retain the following bounded quoted material as `quoted_context` when it appears to be the prompt or context for Svein's reply
- never merge quoted context into the same fragment as if it were authored by Svein

### Embedded Svein text

Retain embedded text only when there is stronger bounded evidence such as:
- explicit quoted `From:` line matching Svein
- explicit forwarded block matching Svein

Use:
- `quoted_svein` for quoted Svein-authored blocks
- `forwarded_svein` for forwarded Svein-authored blocks

### Exclude text when

Do not retain text when:
- the visible author is clearly another person and there is no bounded Svein-authored sub-block
- the text only mentions Svein or includes him in recipient lists
- authorship depends mainly on broad thread context rather than local fragment evidence
- the block is too poorly bounded to separate Svein text from non-Svein text
- the only signal would previously have been `SIGNATURE_MATCH`-style address or name presence without stronger authorship evidence

### Review bucket rules

Retain as `review_block` only when:
- there is useful evidence pointing toward Svein authorship, and
- the fragment is bounded enough to inspect later, and
- retaining it does not obviously include substantial text by someone else as if authored by Svein

## Block segmentation rules

During body parsing, segment candidate text using practical local markers such as:
- quoted reply prefixes like `>`
- forwarded-message separators
- inline header runs such as `From:`, `Sent:`, `To:`, `Subject:`
- signature boundaries
- blank-line paragraph grouping

For direct Svein messages, treat everything before the first strong quoted-history marker as candidate primary text.
For retained context, prefer one bounded quoted block rather than long thread dumps.
For embedded material, prefer smaller bounded blocks over large thread dumps.

## Attachment and document-candidate rules

### Save attachments from retained relevant messages

Save attachments from messages that produced retained text fragments when:
- the message itself is a direct high-confidence Svein message, or
- the message contains a retained high- or medium-confidence Svein fragment and the attachment is relevant to that message context

Preserve original filenames via collision-safe naming in the output path.

### Candidate-document inclusion rules

Classify saved attachments into two semantic buckets:
- `likely_svein_created`
- `relevant_svein_related`

Use `likely_svein_created` when one or more of these apply with good evidence:
- attached to a direct high-confidence Svein message and content context suggests it is his work product
- referenced in mail text as something Svein wrote, prepared, revised, or attached
- filename pattern and surrounding context together support likely Svein authorship

Use `relevant_svein_related` when:
- the attachment is useful sampling material from a Svein-related message
- it is relevant to understanding Svein's communications or document patterns
- authorship is uncertain

### Candidate-document exclusion rules

Do not classify as likely Svein-created when:
- attachment is merely present in a thread mentioning Svein
- evidence only shows he received the file
- context points more strongly to another author

## LLM-use guidance

Primary extraction should stay local and deterministic.

If later review needs LLM help, send only compact staged records such as:
- one extracted primary fragment with optional marked quoted context
- one embedded Svein fragment with its evidence codes and nearby context
- one candidate document record with filename and short evidence note

Do not send full raw mailbox dumps or large MIME payloads unless explicitly needed.

## Verification focus

During review, pay special attention to:
- false positives where retained primary text is clearly by someone else
- whether quoted context is clearly marked as non-Svein context
- missed obvious direct Svein content
- forwarded/quoted boundary quality
- whether candidate documents have meaningful evidence rather than weak co-occurrence

## Notes

These are first-pass heuristics intended to support sampling and later tuning, not final authorship proof.
