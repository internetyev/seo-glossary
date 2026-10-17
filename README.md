# SEO dictionary

An English - Ukrainian dictionary of SEO terms, kept so that people and AI agents writing SEO documents use one standard vocabulary and never coin their own.

The dictionary is in [seo-dictionary.md](seo-dictionary.md). Nine term sections (keywords and search demand, topical map and site structure, on-page, link-building, technical SEO, data and reporting, abbreviations, rejected terms, Ukrainian loanwords) and a change log.

How it is used:

- An agent reads the file before writing any SEO deliverable and uses only the terms in it, in the listed English or Ukrainian form.
- A term that is not in the file is checked with the owner before use, then added with the date.
- A Ukrainian form marked `*` is a proposal not yet confirmed in practice.
- The rejected-terms table lists words that were ruled out; they never come back.

Terms of the semantic SEO framework follow Koray Tugberk Gubur's vocabulary (topical map, central entity, Core and Outer sections, macro and micro context, and the rest).

## Checker

`tools/check_terms.py` scans a document against the dictionary and reports rejected terms, unlisted abbreviations, working-document loanwords in reader copy, and candidate coined labels (quoted, Title Case or hyphenated phrases not in the dictionary), with line numbers:

```bash
python3 tools/check_terms.py path/to/document.md
```

Add `--reader-facing` for article copy, `--json` for machine-readable output.
