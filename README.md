# SEO glossary (English - Ukrainian)

A working glossary of SEO terms: English, the Ukrainian form used in practice, one line of meaning, and the words that were ruled out. It exists so that people and AI agents writing SEO documents use one standard vocabulary and never coin their own.

The glossary itself is one file: [seo-glossary.md](seo-glossary.md).

## Why

Every AI-written SEO document tends to invent a label or two: a "spine" for a site architecture, a "slate" for a content plan, a "token" for an anchor. Each invented word costs the reader a question and the author a correction. A shared glossary removes the question: the agent reads it before writing, uses only what is in it, and asks before adding anything.

The same applies across languages. The Ukrainian SEO vocabulary mixes loanwords that practitioners use (анкор, донор, лінкбілдинг) with calques nobody uses (перелінкування), and only usage decides which is right. The glossary records the forms that are actually used.

## What is inside

| Section | Content |
|---|---|
| 1. Keywords and search demand | keyword, search volume, intent, SERP, impressions, clicks |
| 2. Topical map and site structure | the semantic SEO framework of Koray Tugberk Gubur: topical map, central entity, Core and Outer sections, macro and micro context, nodes, bridges; plus pillar, cluster, hub, page template, query template |
| 3. On-page | title, meta description, headings, internal links, anchors, structured data |
| 4. Link-building and off-page | backlink, referring domain, donor, placement, anchor types, link velocity, digital PR |
| 5. Technical SEO | crawl, indexing, canonical, redirects, hreflang, rendering, Core Web Vitals, and the vocabulary of a technical audit |
| 6. Data, tools and reporting | Search Console, crawlers, keyword and backlink indexes, report conventions |
| 7. Abbreviations | the short forms that may appear without expansion |
| 8. Rejected terms | words that were ruled out, with the replacement and the date |
| 9. Ukrainian loanwords | industry loanwords allowed in working documents but not in copy that readers see |
| 10. Change log | dated entries |

Each term row has four columns: English, Ukrainian, Meaning, Do not use. A Ukrainian form marked `*` is a proposal that has not yet been confirmed in practice; confirming or correcting those is the most useful contribution.

## How to use it

**As a writer or editor:** keep the file open; when a term is in the rejected table, use the replacement; when a term is missing, propose it (see Contributing).

**As an AI agent:** read `seo-glossary.md` before writing any SEO deliverable, use only its terms in the listed form, and check any term that is not in it with the person you work for before using it. Ready-made skills for three agents are in [skills/](skills/): one each for Claude Code, OpenAI Codex and Gemini CLI. Each is a folder with a `SKILL.md`; copy it into the agent's skills directory as its README explains.

**With the checker:** `tools/check_terms.py` scans a document against the glossary and reports, with line numbers, rejected terms, unlisted abbreviations, working-document loanwords in reader copy, and candidate coined labels (quoted, Title Case or hyphenated phrases that are not in the glossary).

```bash
python3 tools/check_terms.py path/to/document.md
```

Add `--reader-facing` for article copy and `--json` for machine-readable output. Candidates are questions for a reader, not verdicts.

## Contributing

Contributions are welcome: a missing term, a better Ukrainian form, a correction to a meaning, a term that should be rejected, or a glossary in another language pair built on the same structure. The short version:

1. Open an issue for a question or a disputed form, or a pull request for a ready row.
2. One term per row, in the section where it belongs, with all four columns filled. A Ukrainian form you have seen used in practice goes in without `*`; a proposal goes in with `*`.
3. Rejected terms go to section 8 with the replacement and the date.
4. Plain ASCII hyphens, no em or en dashes, no smart quotes. No client, company or project names.
5. Add a line to the change log.

[CONTRIBUTING.md](CONTRIBUTING.md) has the full guide, including the row format and how usage evidence is weighed.

## License

The glossary and the tools are released under the [Creative Commons Attribution 4.0](LICENSE) license: use, copy and adapt them freely, with attribution.
