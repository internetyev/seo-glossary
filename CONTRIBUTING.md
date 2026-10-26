# Contributing to the SEO glossary

Thank you for helping keep the vocabulary straight. This guide covers what a good contribution looks like and how it is reviewed.

## What to contribute

- **A missing term** that SEO practitioners actually use. Include where you have seen it used (a tool's interface, a vendor's documentation, a conference talk, a client's own words).
- **A correction** to a meaning that is wrong or too narrow.
- **A rejected term**: a word that is being used for something the glossary already names, or an invented label that keeps appearing in AI-written text. Give the replacement.
- **A translation of the glossary into another language**, as a separate file with the same section structure.

Not wanted: terms coined for one company's product, marketing names for ordinary things, or rows without a meaning.

## Row format

Sections 1 to 6:

```
| English term | one line of meaning | words not to use instead |
```

- English: lowercase unless it is a proper name or an established abbreviation. Several accepted forms are separated by commas (`interlinking, internal linking`).
- Meaning: one sentence, no definition-of-a-definition, no marketing.
- Do not use: leave empty when nothing was ruled out.

Section 8 (rejected terms):

```
| rejected term | use instead | date or short reason |
```

Section 7 (abbreviations) is a comma-separated list.

Every change adds one line to section 9 (change log) with the date.

## Style

- ASCII hyphen-minus only; no em dash, en dash, smart quotes or arrows.
- No client, company, project or person names in rows or examples, and no example that names an industry or a niche; describe the case with a generic noun (`a marketplace`, `a publisher`).
- Keep the row where its section puts it; do not reorder existing rows.
- A term that already exists under another name is a rejected-terms row, not a second term row.

## How changes are reviewed

1. Does the term exist in use, or only in the proposal? Usage wins.
2. Does the glossary already name the thing? Then the new word is either a synonym to add to the English column or a rejected term.
3. Does the meaning read correctly to someone outside SEO?

Small pull requests (one to five rows) are merged fastest. For anything structural, open an issue first.

## Running the checker on your own documents

```bash
python3 tools/check_terms.py your-document.md
```

If the checker flags something in a document that you believe is correct usage, that is often a sign of a missing row: propose it.
