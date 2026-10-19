---
name: seo-glossary
description: Use the SEO glossary before writing or reviewing any SEO document - load the term list, use only its terms, never coin a term, run the checker on the output, and propose missing terms as glossary rows. Trigger on "/seo-glossary", "check the SEO terms in {file}", "which term should I use for ...", or whenever the task produces an SEO deliverable (audit, brief, strategy, content plan, report).
---

# seo-glossary

## 1. Locate the glossary

Use the first that exists: the folder named by `$SEO_GLOSSARY_DIR`; a `seo-glossary.md` in the current repository; `~/seo-glossary/seo-glossary.md`. If none exists, say so and offer to run:

```bash
git clone https://github.com/internetyev/seo-glossary ~/seo-glossary
```

## 2. Before writing

Read `seo-glossary.md`: sections 1-6 are term tables (English | Meaning | Do not use), 7 abbreviations, 8 rejected terms, 9 change log. Use only listed terms, in the listed form. A word in a "Do not use" cell or in the rejected table is never used. A term the document needs that is not in the glossary: ask the user, never coin one; after their answer, propose it as a row.

## 3. Before delivering

Run the checker on the written output:

```bash
python3 {glossary folder from step 1}/tools/check_terms.py path/to/output.md
```

Report the findings as one table: line, found, glossary term, action. A `candidate` is a question, not a verdict: drop candidates that are ordinary prose, proper names, product names or the user's own vocabulary. Apply only the fixes the user approves.

## 4. Contributing back

A confirmed new term becomes a row in the format from CONTRIBUTING.md (English, one-line meaning, do-not-use) in the section where it belongs, plus a dated change-log line. Offer to open a pull request.

## Rules

- ASCII hyphens only; no em or en dashes.
- No verbatim copying from other glossaries; meanings are written in your own words.
- No client, company or person names in glossary rows.
