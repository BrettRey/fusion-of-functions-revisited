#!/usr/bin/env python3
"""Ledger of every quotation in the paper, checked against the page it cites.

The house checker (.house-style/check-quotes.py) only treats a quotation as
sourced when a \\cite command with a page sits beside it. This paper mostly
attributes in prose ("CGEL ... (p. 420)", "PHP (p. 571)"), so the house checker
skips most of its quotations as scare quotes. This script borrows the house
checker's text handling (normalizing, the page map read off the running heads)
and adds two things:

  1. Prose attribution. A quotation's page is the nearest "(p. N)" or
     "(pp. N--M)" in its sentence, preferring one after the quotation. Its source
     is a label or citation inside that parenthesis or, failing that, the nearest
     source named before the quotation in the text (CGEL, PHP, or a cited key).
  2. Ellipses and brackets. "\\ldots" and "[...]" split a quotation into pieces,
     which must all occur, in order, on the cited page.

Verdicts:
  PASS          every piece is on the cited page (or the page after, for a
                quotation that crosses a page break)
  WRONG PAGE    every piece is in the source, but not on the cited page
  MISSING       some piece isn't found in the source; read the page before
                concluding anything (extraction can garble a passage)
  UNCHECKABLE   no usable local copy, or no page map for it
  NO PAGE       the source is identified but no page is cited
Quotations with no page cite in their sentence are listed separately as
probable scare quotes or terms; nothing is claimed about them.

Usage (from the repository root):
    python3 tools/quote_ledger.py [--out notes/passes/DATE-quote-audit.md]
"""

import argparse
import datetime
import importlib.util
import json
import re
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PORTFOLIO = REPO.parents[2]
LIT = PORTFOLIO / "literature"
MAIN = REPO / "fusion-of-functions-revisited.tex"

spec = importlib.util.spec_from_file_location("cq", PORTFOLIO / ".house-style/check-quotes.py")
cq = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cq)

CONF = json.loads((REPO / "tools/quote-sources.json").read_text())
LABELS = {name: (re.compile(v["pattern"]), v["key"]) for name, v in CONF["labels"].items()}
FILES = CONF["files"]
OFFSETS = {k: v for k, v in CONF.get("offsets", {}).items() if not k.startswith("_")}

PAGE_RE = re.compile(r"\b(pp?)\.~?\s*(\d{1,4}(?:\s*--\s*\d{1,4})?(?:,\s*\d{1,4}(?:\s*--\s*\d{1,4})?)*)")
CITE_RE = re.compile(r"\\(?:[Tt]extcite|[Cc]itep|citealp|citet|parencite)\s*(?:\[([^\]]*)\])?\s*(?:\[([^\]]*)\])?\s*\{([^}]+)\}")


def inputs():
    """Section files in the order the main file inputs them."""
    t = MAIN.read_text()
    return [REPO / (m.group(1) if m.group(1).endswith(".tex") else m.group(1) + ".tex")
            for m in re.finditer(r"^\\input\{(drafts/[^}]+)\}", t, re.M)]


LIGATURES = str.maketrans({"\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl", "\ufb03": "ffi", "\ufb04": "ffl"})


def norm(s):
    """The house normalization, plus ligature folding (PHP's PDF prints 'eﬀect')."""
    return cq.normalize(s.translate(LIGATURES))


def footnote_spans(text):
    """(start, end) of every \\footnote{...} body."""
    out, i = [], 0
    while True:
        j = text.find("\\footnote{", i)
        if j < 0:
            return out
        k, depth = j + len("\\footnote{"), 1
        while k < len(text) and depth:
            if text[k] == "{" and text[k - 1] != "\\":
                depth += 1
            elif text[k] == "}" and text[k - 1] != "\\":
                depth -= 1
            k += 1
        out.append((j, k))
        i = j + 1


def strip_comments(text):
    """Blank out LaTeX comments, keeping offsets and line numbers."""
    return re.sub(r"(?<!\\)%[^\n]*", lambda m: " " * len(m.group(0)), text)


def sentence_bounds(text, start, end):
    """Rough sentence around a quotation: back to '. ' or a blank line, forward likewise."""
    lo = max(text.rfind(". ", 0, start), text.rfind("\n\n", 0, start), text.rfind("{", 0, start) if False else -1)
    hi_dot = text.find(". ", end)
    hi_par = text.find("\n\n", end)
    hi = min([h for h in (hi_dot, hi_par) if h >= 0] or [len(text)])
    return (lo + 1 if lo >= 0 else 0), hi + 1


def label_in(s):
    """A source named inside a string: a citation key or a prose label."""
    m = CITE_RE.search(s)
    if m:
        return m.group(3).split(",")[0].strip()
    for name, (rx, key) in LABELS.items():
        if rx.search(s):
            return key
    return None


def sources_before(text, pos, limit=6000):
    """Sources named before pos, nearest first: cite keys and prose labels."""
    lo = max(0, pos - limit)
    notes = footnote_spans(text)
    mine = [s for s in notes if s[0] <= pos < s[1]]

    def visible(at):
        # A source named inside a footnote doesn't govern text outside that footnote.
        inside = [s for s in notes if s[0] <= at < s[1]]
        return not inside or inside == mine

    seen = []
    for m in CITE_RE.finditer(text, lo, pos):
        if visible(m.start()):
            seen.append((m.start(), m.group(3).split(",")[0].strip()))
    for name, (rx, key) in LABELS.items():
        for m in rx.finditer(text, lo, pos):
            if visible(m.start()):
                seen.append((m.start(), key))
    out = []
    for _, k in sorted(seen, reverse=True):
        if k not in out:
            out.append(k)
    return out


def plausible(key, page_spec):
    """True when the cited pages fall inside the source's page range, or it can't be told."""
    pages = source_pages(key)
    want = cq.parse_pages(page_spec or "")
    if not pages or not want:
        return True
    lo, hi = min(pages), max(pages)
    return all(lo <= p <= hi for p in want)


def enclosing_paren(text, i):
    """The parenthetical containing position i, if any."""
    lo = text.rfind("(", 0, i)
    if lo < 0 or text.find(")", lo) < i:
        return None
    hi = text.find(")", i)
    return text[lo:hi + 1] if hi >= 0 else None


def attribute(text, qs, qe):
    """(source_key, page_spec) for the quotation spanning text[qs:qe], or (None, None)."""
    s0, s1 = sentence_bounds(text, qs, qe)
    notes = footnote_spans(text)
    mine = [s for s in notes if s[0] <= qs < s[1]]

    def visible(at):
        inside = [s for s in notes if s[0] <= at < s[1]]
        return not inside or inside == mine

    cands = []  # (distance, key, pages)
    for m in CITE_RE.finditer(text, s0, s1):
        if not visible(m.start()):
            continue
        pages = (m.group(2) or m.group(1) or "").strip()
        if re.search(r"\d", pages):
            d = m.start() - qe if m.start() >= qe else (qs - m.end()) + 10000
            cands.append((d, m.group(3).split(",")[0].strip(), pages))
    for m in PAGE_RE.finditer(text, s0, s1):
        if not visible(m.start()):
            continue
        if m.start() >= qs and m.end() <= qe:
            continue  # a page reference inside the quotation itself
        d = m.start() - qe if m.start() >= qe else (qs - m.end()) + 10000
        paren = enclosing_paren(text, m.start()) or ""
        key = label_in(paren)
        if not key:
            # Nearest source named before the quotation whose pages could include this one.
            before = sources_before(text, qs)
            known = [k for k in before if source_pages(k) and plausible(k, m.group(2))]
            unknown = [k for k in before if not source_pages(k)]
            key = (known or unknown or before or [None])[0]
        cands.append((d, key, m.group(2)))
    if not cands:
        return None, None
    d, key, pages = min(cands)
    return key, pages


def pieces(body):
    """The plain-text pieces a quotation must contain, split at ellipses and brackets."""
    s = body.replace("\\ldots{}", " ... ").replace("\\ldots", " ... ")
    s = re.sub(r"\\textup\{\[\}|\\textup\{\]\}", "", s)
    s = re.sub(r"\\enquote\*?\{([^{}]*)\}", r"'\1'", s)
    plain = cq.strip_markup(s).translate(LIGATURES)
    parts = re.split(r"\s*(?:\.\.\.|\[[^\]]*\])\s*", plain)
    parts = [p.strip(" ,;:") for p in parts if len(p.strip(" ,;:")) >= 4]
    return parts or [plain]


_SRC, _WHOLE = {}, {}


def page_map(raw, offset=None):
    """{printed page: normalized text}. Uses a known offset, else votes on folios
    in each page's first and last non-blank lines (the house checker's first and
    last 80 characters miss CGEL's right-aligned running heads)."""
    pages = raw.split("\f")
    if offset is None:
        from collections import Counter
        votes = Counter()
        for i, p in enumerate(pages, 1):
            ls = [l.strip() for l in p.splitlines() if l.strip()]
            if not ls:
                continue
            for edge in (ls[0], ls[-1]):
                for m in re.finditer(r"(?:^|\s)(\d{1,4})(?:\s|$)", edge):
                    n = int(m.group(1))
                    if 1 <= n <= 4000 and n >= i - 1:
                        votes[n - i] += 1
        if not votes:
            return None
        offset, support = votes.most_common(1)[0]
        if support < 3 or support < len(pages) * 0.25:
            return None
    def body(p):
        ls = p.splitlines()
        nb = [k for k, l in enumerate(ls) if l.strip()]
        if nb and re.search(r"\d", ls[nb[0]]) and len(ls[nb[0]].strip()) < 110:
            ls[nb[0]] = ""          # running head with folio
        if nb and re.fullmatch(r"\s*\d{1,4}\s*", ls[nb[-1]]):
            ls[nb[-1]] = ""         # footer folio
        return "\n".join(ls)
    return {i + offset: norm(body(p)) for i, p in enumerate(pages, 1)}


def source_pages(key):
    """{printed page: normalized text} for a source, or None (no file, or no page map)."""
    if key in _SRC:
        return _SRC[key]
    f = FILES.get(key)
    out = None
    if f and (LIT / f).exists():
        raw = subprocess.run(["pdftotext", "-layout", str(LIT / f), "-"],
                             capture_output=True, text=True, timeout=300).stdout
        _WHOLE[key] = norm(raw)
        out = page_map(raw, OFFSETS.get(key))
    _SRC[key] = out
    return out


def found(page_text, parts):
    """All parts occur, in order, in page_text."""
    low = page_text.lower()
    low2 = cq.FOOTNOTE_TOKEN_RE.sub(" ", low)
    for hay in (low, low2):
        i, ok = 0, True
        for p in parts:
            j = hay.find(p.lower(), i)
            if j < 0:
                ok = False
                break
            i = j + len(p)
        if ok:
            return True
    return False


def split_across(piece, a, b):
    """piece begins on page a and ends on page b, with other text between."""
    ws = [k for k, ch in enumerate(piece) if ch == " "]
    return any(len(piece[:k]) >= 8 and len(piece[k + 1:]) >= 8 and piece[:k] in a and piece[k + 1:] in b
               for k in ws)


def check(key, page_spec, parts):
    if not key:
        return "UNCHECKABLE", "source not identified", ""
    pages = source_pages(key)
    if pages is None:
        if key in _WHOLE:
            ok = found(_WHOLE[key], parts)
            return ("PASS" if ok else "MISSING"), "wording only: no page map for this PDF, so the page isn't checked", ""
        return "UNCHECKABLE", f"no local copy of {key}", ""
    if not page_spec:
        return "NO PAGE", "", ""
    want = cq.parse_pages(page_spec)
    for p in sorted(want):
        txt = pages.get(p, "") + " " + pages.get(p + 1, "")
        if found(txt, parts):
            return "PASS", "", str(p)
    for p in sorted(want):
        a, b = pages.get(p, "").lower(), pages.get(p + 1, "").lower()
        if all(split_across(x.lower(), a, b) or x.lower() in a for x in parts):
            return "PASS", "split across a page break (footnote or heading between)", str(p)
    hits = [p for p, t in pages.items() if found(t + " " + pages.get(p + 1, ""), parts)]
    if hits:
        return "WRONG PAGE", f"found on p. {', '.join(map(str, hits[:3]))}", ""
    return "MISSING", "not found in the source; read the page", ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=f"notes/passes/{datetime.date.today()}-quote-audit.md")
    args = ap.parse_args()

    rows, loose = [], []
    for f in inputs():
        raw = f.read_text()
        text = strip_comments(raw)
        for line, body, qs, qe in cq.extract_quotes(text):
            key, pages = attribute(text, qs, qe)
            short = cq.strip_markup(body.replace("\\ldots{}", "...").replace("\\ldots", "..."))
            short = short if len(short) <= 80 else short[:77] + "..."
            loc = f"{f.relative_to(REPO)}:{line}"
            if key is None and pages is None:
                loose.append((loc, short))
                continue
            verdict, note, _ = check(key, pages, pieces(body))
            rows.append((loc, short, key or "?", pages or "", verdict, note))

    counts = {}
    for r in rows:
        counts[r[4]] = counts.get(r[4], 0) + 1
    out = REPO / args.out
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# Quotation ledger, {datetime.date.today()}",
        f"<!-- SUMMARY: every quotation in the paper with its source, cited page and verdict, from tools/quote_ledger.py · status: generated · updated: {datetime.date.today()} -->",
        "",
        "Generated by `tools/quote_ledger.py` from the section files the main file inputs. "
        "Sources are local PDFs listed in `tools/quote-sources.json`; pages come from each PDF's running heads. "
        "A PASS means the words were found on the cited page of the local copy; it says nothing about the edition. "
        "MISSING and WRONG PAGE mean read the page before concluding anything.",
        "",
        "**Totals:** " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) +
        f"; {len(loose)} quoted spans with no page cite in their sentence (listed at the end).",
        "",
        "| Where | Quotation | Source | Page | Verdict | Note |",
        "|---|---|---|---|---|---|",
    ]
    order = {"MISSING": 0, "WRONG PAGE": 1, "UNCHECKABLE": 2, "NO PAGE": 3, "PASS": 4}
    for r in sorted(rows, key=lambda r: (order.get(r[4], 9), r[0])):
        q = r[1].replace("|", "\\|")
        lines.append(f"| {r[0]} | {q} | {r[2]} | {r[3]} | {r[4]} | {r[5]} |")
    lines += ["", "## Quoted spans with no page cite in their sentence", "",
              "Probable scare quotes, terms, or quotations attributed elsewhere in the paragraph. Not checked.", ""]
    lines += [f"- {loc}: {q}" for loc, q in loose]
    out.write_text("\n".join(lines) + "\n")
    print(out.relative_to(REPO), counts, f"unattributed {len(loose)}")


if __name__ == "__main__":
    main()
