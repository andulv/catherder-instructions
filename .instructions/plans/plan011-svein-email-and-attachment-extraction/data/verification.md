# Plan 011 Verification

**Created:** 2026-03-23T00:00:00+00:00
**Updated:** 2026-03-23T01:00:00+00:00

## Verification scope

Reviewed:
- 5 direct-match extracted fragments from the first pass
- 5 quoted/forwarded/signature-adjacent extracted fragments from the first pass
- 5 candidate-document records from the first pass
- spot-checked regenerated outputs after heuristic tightening and context marking

This verification now includes both the first-pass findings and the follow-up tuning pass.

## First-pass findings

### Direct-match fragment review

- All 5 direct-match samples clearly contained at least some authentic Svein-authored text.
- 4 of 5 direct-match samples also included substantial quoted or forwarded text written by others.
- The original whole-body rule for direct Svein messages was too permissive.

### Embedded fragment review

- 1 of 5 embedded samples was clearly useful and well aligned with the goal.
- 4 of 5 embedded samples were weak or false-positive-like because they only showed Svein as recipient/cc or mentioned him without showing his authored text.
- `SIGNATURE_MATCH` alone was too weak for retention.

### Candidate-document review

- All 5 reviewed candidate documents were plausible as relevant documents.
- Evidence for “likely created by Svein” was often too weak when based only on “attachment on a direct Svein message” plus file extension.

## Tuning changes applied

The follow-up execution applied these changes:
- direct Svein messages are now split into `direct_primary` and optional `quoted_context`
- non-Svein quoted text is no longer mixed into the same fragment as if it were authored by Svein
- `SIGNATURE_MATCH`-only embedded captures were removed
- embedded retention now requires stronger quoted/forwarded evidence
- candidate documents are now classified as either:
  - `likely_svein_created`
  - `relevant_svein_related`

## Regenerated output snapshot

Current regenerated output counts:
- fragment records: `116`
  - `direct_primary`: `64`
  - `quoted_context`: `47`
  - `quoted_svein`: `3`
  - `forwarded_svein`: `2`
- candidate-document records: `66`
  - `likely_svein_created`: `31`
  - `relevant_svein_related`: `35`

## Regenerated-output assessment

### What improved

1. The dataset is much cleaner for primary Svein-style sampling.
2. Useful non-Svein context can still be preserved, but is now explicitly marked as `quoted_context`.
3. Header-only and recipient-list noise has been removed from embedded extraction.
4. Candidate-document semantics now better reflect certainty levels.

### Remaining limitations

1. Some direct-message samples still contain inline history markers that were not fully split before quoted context begins.
2. Quoted/forwarded embedded extraction is now precise but sparse; this is acceptable for sampling.
3. Candidate-document classification is still heuristic and should be treated as reviewable, not final proof.

## Overall verdict

The first pass successfully established a local non-destructive extraction pipeline. After the tuning pass, the outputs are substantially better aligned with the real goal: learning Svein's communication style while optionally preserving clearly marked context from others. The current corpus is usable as a sampling set, with the main caveat that some direct-primary fragments may still contain a small amount of inline quoted material.
