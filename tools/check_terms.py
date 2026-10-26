#!/usr/bin/env python3
"""Check one or more documents against the SEO dictionary.

Reports, with line numbers:
  rejected      a term from the rejected-terms table or a "Do not use" cell
  abbreviation  an all-caps token that the abbreviations section does not list
  candidate     a quoted, Title Case or hyphenated multi-word phrase that is not in
                the dictionary - a possible coined label, to be judged by a reader

Usage:
  check_terms.py [--dictionary PATH] [--json] FILE [FILE ...]
"""
import argparse
import json
import re
import sys
from pathlib import Path

DEFAULT_DICT = Path(__file__).resolve().parent.parent / "seo-glossary.md"

# all-caps tokens that are ordinary technical words, not SEO abbreviations
CAPS_WHITELIST = {
    "URL", "URLS", "HTML", "CSS", "JS", "JSON", "CSV", "XML", "API", "APIS", "HTTP", "HTTPS",
    "PDF", "PNG", "JPG", "SVG", "ID", "IDS", "UI", "UX", "OK", "TODO", "FAQ", "FAQS", "TLDR",
    "CTA", "CTAS", "H1", "H2", "H3", "H4", "H5", "H6", "US", "UK", "EU", "USA", "DE", "ES",
    "FR", "IT", "PL", "UA", "RU", "EN", "GB", "AI", "LLM", "LLMS", "MCP", "CLI", "SDK", "CMS",
    "SQL", "DNS", "CDN", "SSL", "TLS", "IP", "KPI", "KPIS", "ROI", "B2B", "B2C", "SAAS",
    "GA4", "GTM", "CRM", "ERP", "IT", "HR", "PR", "QA", "QC", "NGO", "GOV",
    "EDU", "USD", "EUR", "UAH", "GBP", "MB", "KB", "GB", "AM", "PM", "A", "I", "Q", "N",
    "NA", "WHO", "OECD", "UNICEF", "CCD", "MVP", "SOP", "SERPS", "KD", "UTM", "YOY", "MOM",
}


def parse_dictionary(path):
    """Return terms, rejected, abbreviations from the markdown tables."""
    text = Path(path).read_text(encoding="utf-8")
    terms = {}        # lowercase English term -> row dict
    rejected = []     # (rejected phrase, use instead, source section)
    abbreviations = set()
    section = ""
    for line in text.splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        if section.startswith("7.") and line.strip() and not line.startswith("#"):
            for token in re.split(r",\s*", line.strip().rstrip(".")):
                token = re.sub(r"\s*\(.*?\)", "", token).strip()
                if token:
                    abbreviations.add(token.upper())
            continue
        if not line.startswith("| ") or line.startswith("|---") or line.startswith("| English") \
                or line.startswith("| Rejected"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if section.startswith("8.") and len(cells) >= 2:
            rejected.append((cells[0], cells[1], "rejected terms"))
            continue
        if len(cells) >= 3:
            english, meaning, do_not_use = cells[:3]
            for name in re.split(r",\s*|\s*/\s*", english):
                name = re.sub(r"\s*\(.*?\)", "", name).strip().lower()
                if name:
                    terms[name] = {"english": english, "meaning": meaning}
            if do_not_use:
                for bad in re.split(r",\s*", do_not_use):
                    bad = re.sub(r"\s*\(.*?\)", "", bad).strip()
                    if bad and len(bad) > 1:
                        rejected.append((bad, english, "do not use"))
    return terms, rejected, abbreviations


def rejected_regex(phrase, replacement):
    """Build a regex for one rejected phrase."""
    phrase = phrase.strip().strip('"')
    if not phrase:
        return None, None
    rx = re.compile(r"(?<![\w-])" + re.escape(phrase) + r"(?:s|es)?(?![\w-])", re.I | re.U)
    return rx, None


def scan(path, terms, rejected, abbreviations):
    findings = []
    lines = Path(path).read_text(encoding="utf-8", errors="replace").splitlines()
    known = set(terms.keys())
    compiled = []
    for phrase, use, source in rejected:
        rx, skip = rejected_regex(phrase, use)
        if rx:
            compiled.append((phrase, use, source, rx, skip))
    for number, line in enumerate(lines, 1):
        if line.startswith("|---"):
            continue
        for phrase, use, source, rx, skip in compiled:
            for m in rx.finditer(line):
                word = m.group(0)
                if skip and word.lower().startswith(skip):
                    continue
                findings.append({"line": number, "type": "rejected", "found": word,
                                 "dictionary": use, "note": source})
        for m in re.finditer(r"(?<![\w-])[A-Z][A-Z0-9-]{1,7}(?![\w])", line):
            token = m.group(0).replace("-", "")
            if token in abbreviations or token in CAPS_WHITELIST or token.isdigit():
                continue
            findings.append({"line": number, "type": "abbreviation", "found": m.group(0),
                             "dictionary": "not in section 7", "note": "expand or add"})
        for m in re.finditer(r"[\"“«]([^\"”»]{3,60})[\"”»]", line):
            phrase = m.group(1).strip().lower()
            if 2 <= len(phrase.split()) <= 4 and phrase not in known:
                findings.append({"line": number, "type": "candidate", "found": m.group(1),
                                 "dictionary": "not in dictionary",
                                 "note": "quoted phrase used as a term"})
        for m in re.finditer(r"(?<![\w])([A-Z][a-z]+(?: [A-Z][a-z]+){1,3})(?![\w])", line):
            if m.start() == 0 or line.lstrip().startswith(("#", "|", "-", "*", "1", "2", "3")):
                continue
            phrase = m.group(1).lower()
            if phrase not in known:
                findings.append({"line": number, "type": "candidate", "found": m.group(1),
                                 "dictionary": "not in dictionary",
                                 "note": "Title Case phrase mid-sentence"})
        for m in re.finditer(r"(?<![\w])([A-Za-zА-Яа-яіїєґІЇЄҐ]{4,}-[A-Za-zА-Яа-яіїєґІЇЄҐ]{4,})(?![\w-])", line):
            phrase = m.group(1).lower()
            if phrase not in known and phrase.replace("-", " ") not in known:
                findings.append({"line": number, "type": "candidate", "found": m.group(1),
                                 "dictionary": "not in dictionary",
                                 "note": "hyphenated compound"})
    unique, seen = [], set()
    for x in findings:
        key = (x["line"], x["type"], x["found"].lower())
        if key not in seen:
            seen.add(key)
            unique.append(x)
    return unique


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+")
    ap.add_argument("--dictionary", default=str(DEFAULT_DICT))
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    terms, rejected, abbreviations = parse_dictionary(args.dictionary)
    report = {}
    for f in args.files:
        report[f] = scan(f, terms, rejected, abbreviations)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=1))
        return
    total = 0
    for f, findings in report.items():
        print(f"\n## {f} - {len(findings)} finding(s)\n")
        if not findings:
            continue
        print("| Line | Type | Found | Dictionary | Note |")
        print("|---|---|---|---|---|")
        for x in findings:
            print(f"| {x['line']} | {x['type']} | {x['found']} | {x['dictionary']} | {x['note']} |")
        total += len(findings)
    print(f"\nTotal: {total} finding(s) across {len(report)} file(s); "
          f"dictionary: {len(terms)} terms, {len(rejected)} rejected forms, {len(abbreviations)} abbreviations.")


if __name__ == "__main__":
    sys.exit(main())
