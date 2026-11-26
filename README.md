# Name identifier claim audit

This offline static tool audits documented name-identifier claims against Python source calls. It never executes the inspected code or contacts a network. It examines root README prose and Markdown under docs, excluding fenced blocks; inline code counts. It normalises case, whitespace, hyphens and contractions, and removes negative matches before searching for positive matches.

Install from a local distribution with `python3 -m pip install PATH`, then run:

```sh
isni-validation-claim-audit audit .
python3 -m isni_validation_claim_audit audit . --json
isni-validation-claim-audit --version
```

Use `--ignore PREFIX` repeatedly to omit path prefixes, `--fail-on medium` to include test-only findings in the exit threshold, and `--verbose` for the audited path. Exit status is 0 for pass, 2 for a finding at or above the threshold, and 1 for usage or I/O errors. The default threshold is high.

Positive claims without production evidence yield the following finding, with medium severity when evidence exists only in tests and high otherwise:

```
documented-isni-validation-claim-false
```

Negative claims with production evidence yield this high severity finding:

```
documented-no-isni-validation-claim-false
```

Evidence consists of statically recognised calls to the three supported library routes or explicitly named generic calls. Aliases are resolved and local shadows excluded. Tests count separately; fixtures, examples, docs, symlinks and syntax-invalid files do not supply production evidence. This is a heuristic, not proof that a call executes or that a claim is accurate.

## Differentiation

This audit does not cover generic input validation.
This audit does not cover ISBN book numbers.
This audit does not cover ISSN serial numbers.
This audit does not cover IBAN bank accounts.
This audit does not cover UUID strings.
This audit does not cover semantic versions.
This audit does not cover MAC addresses.
This audit does not cover BIC bank identifiers.
This audit does not cover cron expression validation.
This audit does not cover cron expression description.
This audit does not cover scheduled execution.
This audit does not cover calendar dates.
This audit does not cover timeouts.
This audit does not cover payment processing.
This audit does not cover credit card extraction.
This audit does not cover account authentication.
This audit does not cover password verification.
This audit does not cover password hashing.
This audit does not cover password generation.
This audit does not cover PDF encryption.
This audit does not cover email delivery.
This audit does not cover SMS delivery.
This audit does not cover document extraction.
This audit does not cover barcode decoding.
This audit does not cover email address validation.
This audit does not cover phone number validation.
This audit does not cover password strength.
This audit does not cover JSON Schema validation.
This audit does not cover credit card validation.
This audit does not cover domain validation.
This audit does not cover URL validation.
This audit does not cover IP address validation.
This audit does not cover JSON parsing.
This audit does not cover regular expression matching.
This audit does not cover URL parsing.
This audit does not cover web fetching.
This audit does not cover DNS lookup.
This audit does not cover barcode generation.
This audit does not cover account number extraction.
This audit does not cover vehicle number extraction.
This audit does not cover vehicle number decoding.
This audit does not cover vehicle history lookup.
This audit does not cover hex colour validation.
This audit does not cover ORCID researcher identifiers.
This audit does not cover DOI validation and resolution.
This audit does not cover CAS Registry Numbers.
This audit does not cover CUSIP security identifiers.
This audit does not cover SEDOL security identifiers.
This audit does not cover ISIN security identifiers.
This audit does not cover security record lookup.
This audit does not cover security identifier extraction.
This audit does not cover IMEI identifiers.
This audit does not cover MEID identifiers.
This audit does not cover ESN identifiers.
This audit does not cover ISMN music publications.
This audit does not cover ISAN audiovisual works.
This audit does not cover GRid releases.
This audit does not cover EAN trade items.
This audit does not cover generic serial numbers.
This audit does not cover FIGI financial instruments.
This audit does not cover financial instrument lookup.
This audit does not cover financial instrument extraction.
This audit does not cover ISRC recordings.
This audit does not cover Ethereum addresses.
This audit does not cover Binance Smart Chain addresses.
This audit does not cover Tron addresses.
This audit does not cover Litecoin addresses.
This audit does not cover Dogecoin addresses.
This audit does not cover bitcoin addresses.
This audit does not cover transaction hashes.
This audit does not cover private keys.
This audit does not cover block explorer lookup.
This audit does not cover address generation.
This audit does not cover address extraction.
This audit does not cover payment receipt confirmation.
This audit does not cover spreadsheet reading.
This audit does not cover spreadsheet generation.
This audit does not cover word document reading.
This audit does not cover word document generation.
This audit does not cover presentation reading.
This audit does not cover presentation generation.
This audit does not cover PDF extraction.
This audit does not cover PDF generation.
This audit does not cover PDF merging.
This audit does not cover PDF splitting.
This audit does not cover PDF rotation.
This audit does not cover PDF form filling.
This audit does not cover PDF watermarking.
This audit does not cover PDF redaction.
This audit does not cover PDF compression.
This audit does not cover PDF annotation.
This audit does not cover table extraction.
This audit does not cover OCR.
This audit does not cover document data extraction.
This audit does not cover electronic signatures.
This audit does not cover screen recording.
This audit does not cover video generation.
This audit does not cover QR code generation.
This audit does not cover barcode scanning.
This audit does not cover audio mixing.
This audit does not cover audio generation.
This audit does not cover audio editing.
This audit does not cover audio source separation.
This audit does not cover speech recognition.
This audit does not cover text to speech.
This audit does not cover noise suppression.
This audit does not cover music generation.
This audit does not cover music transcription.
This audit does not cover InChI structures.
This audit does not cover SMILES molecular notation.
This audit does not cover EC inventory numbers.
This audit does not cover UN transport numbers.
This audit does not cover PubChem lookup.
This audit does not cover chemical structure validation.
This audit does not cover other chemical identifiers.

## Limitations

```
validate isni
```

The bare phrase above can denote a manual runbook step; context requires human review.

```
isni validation
```

The bare phrase above can denote a roadmap item; context requires human review.

```
isni validator
```

The bare phrase above can denote a hosted page; context requires human review.

```
isni check
```

The bare phrase above can denote a presence-only lint rule; context requires human review.

```
check isni
```

The bare phrase above can denote a manual runbook step; context requires human review.

```
verify isni
```

The bare phrase above can denote visually confirming a contributor; context requires human review.

```
isni verification
```

The bare phrase above can denote an external service result; context requires human review.

```
validate isni number
```

The bare phrase above can denote a manual runbook step; context requires human review.

```
isni number validation
```

The bare phrase above can denote a specification section without code; context requires human review.

```
valid isni
```

The bare phrase above can denote example output; context requires human review.

```
isni is valid
```

The bare phrase above can denote example output; context requires human review.

```
isni is invalid
```

The bare phrase above can denote example error text; context requires human review.

```
isni validity
```

The bare phrase above can denote a configuration flag or column name; context requires human review.

```
isni format validation
```

The bare phrase above can denote a format description; context requires human review.

```
validate isni format
```

The bare phrase above can denote a format description; context requires human review.

```
isni number check
```

The bare phrase above can denote a metadata checklist item; context requires human review.

```
check isni number
```

The bare phrase above can denote a manual runbook step; context requires human review.

```
verify isni number
```

The bare phrase above can denote visually confirming a contributor; context requires human review.

```
validate isni number format
```

The bare phrase above can denote a format description; context requires human review.

```
isni number is valid
```

The bare phrase above can denote example output; context requires human review.

```
isni
```

The bare phrase above can denote an abbreviation alone; context requires human review.

```
isni number
```

The bare phrase above can denote a number alone; context requires human review.

```
name identifier
```

The bare phrase above can denote a general identifier alone; context requires human review.

```
contributor identifier
```

The bare phrase above can denote a general identifier alone; context requires human review.

```
isni.org
```

The bare phrase above can denote a registry address alone; context requires human review.

```
check digit
```

The bare phrase above can denote a checksum alone; context requires human review.

```
orcid
```

The bare phrase above can denote a researcher identifier alone; context requires human review.

A compact call only reformats its input.

A format call only regroups its input.

A checksum digit calculation does not judge a complete number.

A generic MOD 11-2 validation call does not enforce the identifier length or alphabet.

A registry lookup retrieves a record rather than judging a string.

A generation call does not judge an input.

An ORCID-specific call judges a narrower range.

A regular expression match alone does not establish the checksum.

A length check alone does not establish the checksum.

A separator-position check alone does not establish the checksum.

A digit-only check alone does not establish the checksum.

Identifier scheme detection classifies schemes rather than judging this particular one.

The check digit cannot catch a wrong but well-formed identifier.

The stdnum route accepts spaces, hyphens, and a lowercase x.

The idutils route accepts an identifier URI.

Shared library routes can over-count projects limited to ORCID identifiers.

Library calls do not establish assignment or the identity of a contributor.

The validators package supplies no second route for cross-checking.

A bare import alone is not evidence.

A string or comment alone is not evidence.

A bare name reference without a call is not evidence.

An external command alone is not evidence.

A claim in a roadmap, changelog, or TODO without code is not evidence.

Evidence split across two modules is not evidence.

A route call on a locally shadowed name is not evidence.

A syntax-invalid file supplies no evidence.

Static analysis cannot establish whether a call runs.
