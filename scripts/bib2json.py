#!/usr/bin/env python3
"""
bib2json.py  —  Turn your BibTeX files into the site's publications data.

WHAT IT DOES
    Reads  journals.bib  and  conferences.bib  (in the repo root),
    parses every entry, cleans up the LaTeX, and writes a single file:

        _data/publications.json

    Jekyll reads that file automatically, so the Publications page
    (and the "Selected publications" on the home page) rebuild themselves.

HOW TO USE
    You normally never run this by hand. The GitHub Action runs it for you
    on every push. But if you want to preview locally:

        python3 scripts/bib2json.py

    Pure standard library — no `pip install` needed. Works on Python 3.7+.

ADDING A PAPER
    Just add a normal @article / @inproceedings entry to journals.bib or
    conferences.bib and push. Optional extra fields you can add to any entry:

        url    = {https://...}     ->  adds a "PDF" / "Link" button
        doi    = {10.1109/...}     ->  adds a "DOI" button
        award  = {Best Paper}      ->  shows a small award badge

    To feature a paper on the home page, put its citation key in the
    `selected_publications` list in _data/profile.yml.
"""

import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# (source file, publication type) — order controls nothing; year sorting does.
SOURCES = [
    ("journals.bib", "journal"),
    ("conferences.bib", "conference"),
]

TYPE_FROM_ENTRY = {
    "article": "journal",
    "inproceedings": "conference",
    "conference": "conference",
    "incollection": "chapter",
    "inbook": "chapter",
    "book": "book",
    "phdthesis": "thesis",
    "mastersthesis": "thesis",
    "techreport": "report",
    "misc": "other",
    "unpublished": "other",
}

TYPE_LABEL = {
    "journal": "Journal Article",
    "conference": "Conference Paper",
    "chapter": "Book Chapter",
    "book": "Book",
    "thesis": "Thesis",
    "report": "Technical Report",
    "other": "Preprint / Other",
}

# ---------------------------------------------------------------------------
# LaTeX -> Unicode cleanup
# ---------------------------------------------------------------------------

_COMBINING = {
    "'": "́", "`": "̀", '"': "̈", "^": "̂",
    "~": "̃", "=": "̄", ".": "̇", "c": "̧",
    "v": "̌", "u": "̆", "H": "̋", "k": "̨",
    "r": "̊", "b": "̱", "d": "̣",
}

_SPECIAL = {
    r"\ss": "ß", r"\SS": "SS", r"\o": "ø", r"\O": "Ø",
    r"\l": "ł", r"\L": "Ł", r"\aa": "å", r"\AA": "Å",
    r"\ae": "æ", r"\AE": "Æ", r"\oe": "œ", r"\OE": "Œ",
    r"\i": "i", r"\j": "j",
}

_ACCENT_RE = re.compile(r"\\([`'\"^~=.cvuHkrbd])\s*\{?\\?([a-zA-Z])\}?")


def _accent(match):
    acc, letter = match.group(1), match.group(2)
    comb = _COMBINING.get(acc)
    if not comb:
        return letter
    return unicodedata.normalize("NFC", letter + comb)


def delatex(text):
    """Best-effort conversion of BibTeX/LaTeX snippets to clean Unicode text."""
    if not text:
        return ""
    s = text
    # Escaped specials
    for a, b in ((r"\&", "&"), (r"\%", "%"), (r"\_", "_"),
                 (r"\$", "$"), (r"\#", "#"), (r"\{", "{"), (r"\}", "}")):
        s = s.replace(a, b)
    # Special standalone glyphs (longest first so \SS beats \S etc.)
    for cmd in sorted(_SPECIAL, key=len, reverse=True):
        s = re.sub(re.escape(cmd) + r"(?![a-zA-Z])", _SPECIAL[cmd], s)
    # Accents: \'e  \'{e}  \"{u}  \c{s}  \v{z} ...
    s = _ACCENT_RE.sub(_accent, s)
    # Ties / non-breaking spaces
    s = s.replace("~", " ")
    # Dashes
    s = s.replace("---", "—").replace("--", "–")
    # Drop any leftover control sequences but keep their letters
    s = re.sub(r"\\[a-zA-Z]+", "", s)
    # Strip braces
    s = s.replace("{", "").replace("}", "")
    # Collapse whitespace
    s = re.sub(r"\s+", " ", s).strip()
    return s


# ---------------------------------------------------------------------------
# BibTeX parsing (dependency-free)
# ---------------------------------------------------------------------------

def find_entries(text):
    """Yield (entry_type, body, raw_text) for each @entry{...} block."""
    entries = []
    i, n = 0, len(text)
    while i < n:
        if text[i] != "@":
            i += 1
            continue
        brace = text.find("{", i)
        if brace == -1:
            break
        etype = text[i + 1:brace].strip().lower()
        depth, k = 0, brace
        while k < n:
            c = text[k]
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    break
            k += 1
        raw = text[i:k + 1]
        body = text[brace + 1:k]
        if etype not in ("comment", "string", "preamble"):
            entries.append((etype, body, raw))
        i = k + 1
    return entries


_FIELD_RE = re.compile(r"([a-zA-Z][a-zA-Z0-9_\-]*)\s*=\s*")


def parse_fields(body):
    comma = body.find(",")
    if comma == -1:
        return body.strip(), {}
    key = body[:comma].strip()
    rest = body[comma + 1:]
    fields = {}
    i, n = 0, len(rest)
    while i < n:
        while i < n and rest[i] in " \t\r\n,":
            i += 1
        m = _FIELD_RE.match(rest, i)
        if not m:
            break
        name = m.group(1).lower()
        i = m.end()
        if i < n and rest[i] == "{":
            depth, s = 0, i
            while i < n:
                if rest[i] == "{":
                    depth += 1
                elif rest[i] == "}":
                    depth -= 1
                    if depth == 0:
                        i += 1
                        break
                i += 1
            val = rest[s + 1:i - 1]
        elif i < n and rest[i] == '"':
            s = i
            i += 1
            while i < n and rest[i] != '"':
                i += 1
            val = rest[s + 1:i]
            i += 1
        else:
            s = i
            while i < n and rest[i] != ",":
                i += 1
            val = rest[s:i].strip()
        fields[name] = val
    return key, fields


def _is_me(name, surname, first):
    nl = name.strip().lower()
    if nl in ("abhishek", "abhishek gupta", "a. gupta", "a gupta"):
        return True
    return surname.strip().lower() == "gupta" and first.strip().lower().startswith("abhishek")


def parse_authors(field):
    field = delatex(field.replace("\n", " ")) if False else field  # keep raw for splitting
    parts = re.split(r"\s+and\s+", field.strip())
    authors = []
    for raw in parts:
        raw = raw.strip()
        if not raw:
            continue
        if raw.lower() in ("others", "et al", "et al."):
            authors.append({"name": "et al.", "is_me": False, "et_al": True})
            continue
        if "," in raw:
            last, first = raw.split(",", 1)
        else:
            toks = raw.split()
            last = toks[-1] if toks else raw
            first = " ".join(toks[:-1])
        name = delatex(("%s %s" % (first.strip(), last.strip())).strip())
        authors.append({
            "name": name,
            "is_me": _is_me(name, delatex(last), delatex(first)),
            "et_al": False,
        })
    return authors


def year_of(fields):
    y = fields.get("year", "").strip()
    m = re.search(r"\d{4}", y)
    return int(m.group(0)) if m else 0


def build_record(etype, fields, raw, default_type):
    ptype = TYPE_FROM_ENTRY.get(etype, default_type)
    authors = parse_authors(fields.get("author", ""))
    venue = fields.get("journal") or fields.get("booktitle") or fields.get("school") \
        or fields.get("institution") or fields.get("publisher") or ""
    rec = {
        "id": fields.get("_key", ""),
        "type": ptype,
        "type_label": TYPE_LABEL.get(ptype, "Publication"),
        "title": delatex(fields.get("title", "")),
        "authors": authors,
        "authors_plain": ", ".join(a["name"] for a in authors),
        "venue": delatex(venue),
        "volume": delatex(fields.get("volume", "")),
        "number": delatex(fields.get("number", "")),
        "pages": delatex(fields.get("pages", "")),
        "year": year_of(fields),
        "publisher": delatex(fields.get("publisher", "")),
        "doi": fields.get("doi", "").strip(),
        "url": fields.get("url", "").strip(),
        "award": delatex(fields.get("award", "")),
        "note": delatex(fields.get("note", "")),
        "bibtex": raw.strip(),
    }
    # Drop empty optional fields. In Liquid an empty string "" is TRUTHY, so
    # leaving them in makes {% if p.number %} etc. render stray ", no. " and
    # phantom PDF/DOI/award badges. Omitting the key makes it nil → falsy.
    for k in ("venue", "volume", "number", "pages", "publisher",
              "doi", "url", "award", "note"):
        if not rec.get(k):
            rec.pop(k, None)
    return rec


def main():
    records = []
    seen = set()
    for filename, default_type in SOURCES:
        path = os.path.join(ROOT, filename)
        if not os.path.exists(path):
            sys.stderr.write("  (skipped, not found: %s)\n" % filename)
            continue
        with open(path, "r", encoding="utf-8") as fh:
            text = fh.read()
        count = 0
        for etype, body, raw in find_entries(text):
            key, fields = parse_fields(body)
            if not key:
                continue
            if key in seen:
                key = key + "_dup"
            seen.add(key)
            fields["_key"] = key
            records.append(build_record(etype, fields, raw, default_type))
            count += 1
        print("  %-18s %3d entries" % (filename, count))

    # Newest first; stable secondary sort by title.
    records.sort(key=lambda r: (-r["year"], r["title"].lower()))

    out_path = os.path.join(ROOT, "_data", "publications.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(records, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    j = sum(1 for r in records if r["type"] == "journal")
    c = sum(1 for r in records if r["type"] == "conference")
    o = len(records) - j - c
    print("  -> %s" % os.path.relpath(out_path, ROOT))
    print("  total: %d publications  (%d journal, %d conference, %d other)"
          % (len(records), j, c, o))


if __name__ == "__main__":
    print("Generating publications from BibTeX ...")
    main()
