# Titanium protocol — comments and feedback

The public titanium MOPA protocol page is alpha, not a validated recipe:
https://muse.ai/s/titanium-mopa-deep-engraving-protocol-oxh6yxwtpn714/ezs7cy2fiGCRXlLrD6V_QAO0MurEBLCtcnKo8S3Kk5A

## How to comment

Comments go via GitHub Issues in this repo — use “New issue”, then pick a template:

- **Protocol feedback** — a correction or a test result for the titanium protocol.
- **Titanium data** — a new data point, with source, machine, settings and measured result.
- **Question / general comment** — anything else about the protocol or the lab work.

Do not put credentials, passwords, API keys or personal data in an issue.
Do not attach executables. Links and attachments are checked before anything
is used — never run or open an attachment blindly.

## What happens next

1. Every issue is security-checked first: links, scripts, executables,
   credentials and personal data are stripped or flagged. Suspicious
   submissions get the `security-review` label and are not published.
2. Each issue is labelled before it touches the protocol:
   - `unverified` — user-submitted, not yet reviewed
   - `plausible` — looks consistent, still needs a test
   - `verified` — checked against a source or a repeatable test
   - `tribal-anecdotal` — forum / group / chat experience, cited as group + forum only unless a quality link exists
   - `needs-test` — worth a coupon test (see the T1–T8 validation tests on the protocol page)
   - `security-review` — needs a security check before any use
3. A daily ingest summarises new and updated issues for James. Nothing is
auto-edited into the protocol page, auto-merged or auto-published.
James approves additions first.

## Intended labels

The label set above is the intended set. The GitHub tool available here
does not create labels, so if a label does not exist yet in the repo, create
it in GitHub (Issues → Labels) with the meanings above before relying on it.

## Provenance

Titanium data in the protocol is accredited to Laser Everything, as collected
from lexical analysis of keywords over the course of member discussions on
Discord, as well as the JPT guidelines. JPT cut-off tables in
`jpt-mopa-cutoff/` are JPT only — match the whole model code, do not scale
between wattages or series, and vendors lock lasers to their bounds.

The underlying personal-collection source files are not published or
redistributed here. Only the public synthesis page linked above is public.
