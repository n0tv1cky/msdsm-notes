#!/usr/bin/env python3
"""Notion-safe body builder + math verifier for lecture notes.

Why this exists: Notion's markdown import (notion-create-pages /
notion-update-page) mangles a ONE-LINE display equation `$$X$$` into a
literal `\\$` followed by a broken inline equation, which renders as
"Invalid equation" (hit on all 36 pages created 2026-11-17). Multi-line
blocks

    $$
    X
    $$

import as proper block equations.

The repo notes are in GitHub-safe form (```math fences, $`...`$ inline; see
github_math.py), which Notion would show as code. So the body is first put
back to plain $...$ / $$ delimiters with github_math.from_github, then
display maths is rewritten to multi-line blocks.

Usage:
  notion_body.py <note.md>            print the body to send to Notion
                                      (front matter, <!-- nav --> blocks and
                                      the first H1 stripped; display math
                                      rewritten to multi-line blocks)
  notion_body.py --check <note.md>... report math problems; exit 1 if any

After writing a page to Notion, fetch it back once: the stored content must
contain no `\\$$` (that is the signature of a mangled equation).
"""
import re
import sys

from github_math import from_github

DISPLAY = re.compile(r"\$\$(.+?)\$\$")
LIST_MARKER = re.compile(r"^([-*+]|\d+\.)\s+")


def strip_for_notion(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            text = text[end + 5:]
    text = re.sub(r"<!-- nav -->.*?<!-- /nav -->\n?", "", text, flags=re.S)
    lines = text.split("\n")
    for i, ln in enumerate(lines):
        if ln.startswith("# "):
            del lines[i]
            break
    return "\n".join(lines)


def blockify_display_math(text: str) -> str:
    """Rewrite one-line `$$X$$` into multi-line blocks with blank lines around."""
    out = []
    in_code = False
    for ln in text.split("\n"):
        if ln.lstrip().startswith("```"):
            in_code = not in_code
        m = re.match(r"^(\s*)(.*)$", ln)
        indent, rest = m.group(1), m.group(2)
        pieces = DISPLAY.split(rest)
        if in_code or len(pieces) == 1:
            out.append(ln)
            continue
        texts, maths = pieces[0::2], pieces[1::2]
        lead = texts[0].strip()
        if rest.startswith("|") or any(t.strip() for t in texts[1:]):
            # inside a table row or mid-sentence: make it inline math
            out.append(DISPLAY.sub(lambda mm: "$" + mm.group(1).strip() + "$", ln))
            continue
        cont = indent
        lm = LIST_MARKER.match(lead)
        if lead:
            out.append(indent + lead)
            if lm:
                cont = indent + " " * len(lm.group(0))
        for mth in maths:
            out += ["", cont + "$$", cont + mth.strip(), cont + "$$", ""]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"


def notion_body(text: str) -> str:
    return blockify_display_math(strip_for_notion(from_github(text)))


PROSE = re.compile(r"(?:\b[A-Za-z]{2,}\b[ ,;.]+){4}")


def scan_math(s: str) -> tuple[list[str], list[int]]:
    """Pandoc-style pairing of single $ delimiters. An opener has a non-space
    after it; a closer has a non-space before it and no digit after it.
    Returns (span contents, unclosed opener positions). Only openers followed
    by LaTeX-looking text count as unclosed, so currency like "$29 / $79" is
    not flagged."""
    spans, bad = [], []
    i = 0
    while True:
        i = s.find("$", i)
        if i == -1:
            return spans, bad
        if i + 1 >= len(s) or s[i + 1].isspace():
            i += 1
            continue
        j = i + 1
        closed = False
        while True:
            j = s.find("$", j)
            if j == -1:
                break
            if not s[j - 1].isspace() and not (j + 1 < len(s) and s[j + 1].isdigit()):
                closed = True
                break
            j += 1
        if closed:
            spans.append(s[i + 1:j])
            i = j + 1
            continue
        if re.match(r"[^\s$]*[\\^_{]", s[i + 1:i + 30]):
            bad.append(i)
        i += 1


def looks_like_prose(span: str) -> bool:
    """A math span holding 4+ plain words in a row means a stray $ paired
    with the wrong partner and swallowed a sentence (e.g. `$\\le 0; and the
    price is ... x$`)."""
    span = re.sub(r"\\(text|mathrm|mathbf|textbf|operatorname|mbox)\{[^}]*\}", "", span)
    span = re.sub(r"\\[A-Za-z]+", "", span)
    return bool(PROSE.search(span))


def check(text: str) -> list[str]:
    """Return human-readable math problems (empty list = clean). Accepts
    plain-$ text or GitHub-form notes (converted back first)."""
    text = from_github(text)
    issues = []
    in_code = False
    for n, ln in enumerate(text.split("\n"), 1):
        if ln.lstrip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        bare = re.sub(r"`[^`]*`", "", ln).replace("\\$", "  ")
        bare = re.sub(r"\$\$.*?\$\$", "", bare)
        if bare.strip() == "$$":
            continue
        spans, unclosed = scan_math(bare)
        if unclosed:
            issues.append(f"line {n}: unclosed inline $ (LaTeX follows): {ln.strip()[:90]}")
        elif any(looks_like_prose(sp) for sp in spans):
            issues.append(f"line {n}: math span contains prose (mis-paired $?): {ln.strip()[:90]}")
    body = notion_body(text)
    if DISPLAY.search(body):
        issues.append("one-line $$...$$ survived blockify (bug in notion_body.py)")
    return issues


def main(argv):
    if argv and argv[0] == "--check":
        bad = 0
        for path in argv[1:]:
            for issue in check(open(path, encoding="utf-8").read()):
                print(f"{path}: {issue}")
                bad += 1
        return 1 if bad else 0
    if len(argv) != 1:
        print(__doc__)
        return 2
    sys.stdout.write(notion_body(open(argv[0], encoding="utf-8").read()))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
