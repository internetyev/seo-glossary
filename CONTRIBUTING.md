# Contributing to the SEO glossary

Thank you for helping keep the vocabulary straight. This guide covers what a good contribution looks like and how it is reviewed.

## What to contribute

- **A missing term** that SEO practitioners actually use. Include where you have seen it used (a tool's interface, a vendor's documentation, a conference talk, a client's own words).
- **A Ukrainian form** for a row that has none or carries a `*`. The best evidence is usage by Ukrainian practitioners: an industry article, a tool localisation, a job post, a community thread. A dictionary translation on its own is not evidence; the glossary records the living form, which is often a loanword.
- **A correction** to a meaning that is wrong or too narrow.
- **A rejected term**: a word that is being used for something the glossary already names, or an invented label that keeps appearing in AI-written text. Give the replacement.
- **Another language pair**, as a new file built on the same ten-section structure.

Not wanted: terms coined for one company's product, marketing names for ordinary things, or rows without a meaning.

## Row format

Sections 1 to 6:

```
| English term | Ukrainian form | one line of meaning | words not to use instead |
```

- English: lowercase unless it is a proper name or an established abbreviation. Several accepted forms are separated by commas (`interlinking, internal linking`).
- Ukrainian: the form used in practice. Append `*` to a proposal that nobody has confirmed. Loanwords allowed only in working documents also go to section 9.
- Meaning: one sentence, no definition-of-a-definition, no marketing.
- Do not use: leave empty when nothing was ruled out.

Section 8 (rejected terms):

```
| rejected term | use instead | date or short reason |
```

Section 7 (abbreviations) and section 9 (loanwords) are comma-separated lists.

Every change adds one line to section 10 (change log) with the date.

## Style

- ASCII hyphen-minus only; no em dash, en dash, smart quotes or arrows.
- No client, company, project or person names in rows or examples; describe the case generically (`a marketplace of local events`, not the marketplace's name).
- Keep the row where its section puts it; do not reorder existing rows.
- A term that already exists under another name is a rejected-terms row, not a second term row.

## How changes are reviewed

1. Does the term exist in use, or only in the proposal? Usage wins.
2. Does the glossary already name the thing? Then the new word is either a synonym to add to the English column or a rejected term.
3. Is the Ukrainian form the one practitioners use? Two independent usage examples remove the `*`.
4. Does the meaning read correctly to someone outside SEO?

Small pull requests (one to five rows) are merged fastest. For anything structural, open an issue first.

## Running the checker on your own documents

```bash
python3 tools/check_terms.py your-document.md
```

If the checker flags something in a document that you believe is correct usage, that is often a sign of a missing row: propose it.
