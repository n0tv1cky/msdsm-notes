#!/usr/bin/env python3
"""GitHub-safe maths for lecture notes (stdlib only).

The notes are read on github.com, whose markdown pass runs BEFORE MathJax and
mangles plain $...$ / $$...$$ LaTeX: it strips backslash escapes (\\, -> ",",
\\{ \\} vanish, \\% comments out the rest), reads * as emphasis, ignores $$
blocks inside paragraphs, skips $...$ right after a quote or "/", shows
indented ```math fences inside list items as plain code, and rejects
\\phantom. The format that survives (fixed on all notes in 8db2fd0/dd186e6):

  * top-level display maths      -> a ```math fence
  * display maths in a list item -> $`\\displaystyle ...`$ on its own line
  * inline maths                 -> GitHub verbatim $`...`$ (LaTeX unchanged)
  * no \\phantom
  * in table rows, | inside maths -> \\vert{} and \\| -> \\Vert{}
  * unescaped currency $ (spans holding prose) and anything inside code
    spans/blocks are left byte-identical

to_github(text) applies all of that and is idempotent. from_github(text)
undoes the GitHub-only syntax (back to $...$ and multi-line $$ blocks) for
consumers that expect plain LaTeX delimiters, e.g. notion_body.py.

Usage:
  github_math.py FILE...          convert notes in place (prints "fixed FILE")
  github_math.py --check FILE...  exit 1 if any file is not in GitHub form
"""
import re
import sys

# ---- pass 1: $..$/$$..$$ -> ```math fences / one-line $$ in list items ----
# (from ~/.msdsm-study/github-math-fix/mathfix.py, logic unchanged)
FENCE = re.compile(r"^(\s*)(```|~~~)")
DISALLOWED = re.compile(r"\\[hv]?phantom\s*\{")

def strip_disallowed(s):
    out, i = [], 0
    while (k := DISALLOWED.search(s, i)):
        out.append(s[i:k.start()])
        depth, j = 1, k.end()
        while depth and j < len(s):
            depth += {"{": 1, "}": -1}.get(s[j], 0); j += 1
        i = j
    out.append(s[i:])
    return "".join(out)

# inline: $x$ not preceded by \ or $ or `, content not starting/ending with space
INLINE = re.compile(r"(?<![\\$`])\$(?![\s$`])((?:[^$\\\n]|\\.)+?)(?<![\s\\`])\$(?![$`\d])")
DISPLAY_INLINE = re.compile(r"(?<!\\)\$\$(.+?)(?<!\\)\$\$")


def escfree(t):
    return strip_disallowed(t)


def _prose(body):
    b = re.sub(r"\\(text|mathrm|textbf|texttt|operatorname)\{[^}]*\}", "", body)
    return '**' in body or '"' in body or re.search(r"[A-Za-z]{2,}[ ,.;]+[A-Za-z]{2,}[ ,.;]+[A-Za-z]{2,}", b)

def conv_inline_text(seg, table_row):
    def disp(m):
        body = m.group(1).strip()
        if "`" in body or (table_row and "|" in body): return m.group(0)
        return "$\\displaystyle " + escfree(body) + "$"
    def inl(m):
        body = m.group(1)
        if "`" in body or (table_row and "|" in body) or _prose(body): return m.group(0)
        return "$" + escfree(body) + "$"
    parts = re.split(r"((?<!\\)\$\$.+?(?<!\\)\$\$)", seg)
    for i in range(len(parts)):
        parts[i] = disp(DISPLAY_INLINE.match(parts[i])) if i % 2 else INLINE.sub(inl, parts[i])
    return "".join(parts)

def conv_line(line):
    table_row = line.lstrip().startswith("|")
    # earlier pass wrote GitHub-only $`..`$; turn those back into plain $..$
    # skip code spans
    out, i = [], 0
    for m in re.finditer(r"(`+).+?\1", line):
        out.append(conv_inline_text(line[i:m.start()], table_row)); out.append(m.group(0)); i = m.end()
    out.append(conv_inline_text(line[i:], table_row))
    return "".join(out)

def convert(text):
    lines = text.split("\n")
    res, i, in_code, fence = [], 0, False, None
    while i < len(lines):
        ln = lines[i]
        fm = FENCE.match(ln)
        if in_code:
            res.append(ln)
            if fm and fm.group(2) == fence: in_code = False
            i += 1; continue
        if fm:
            in_code, fence = True, fm.group(2); res.append(ln); i += 1; continue
        s = ln.strip()
        indent = ln[: len(ln) - len(ln.lstrip())]
        bullet = re.match(r"^(\s*(?:[-*+]|\d+\.)\s+)\$\$", ln)
        # display block: line is (optionally a list bullet +) $$... possibly spanning lines
        if s.startswith("$$") or bullet:
            lead = bullet.group(1) if bullet else indent
            body_start = ln[len(lead):] if bullet else s
            body = body_start[2:]
            j = i
            if "$$" in body:
                inner, rest = body.split("$$", 1)
                if rest.strip():  # $$..$$ followed by text on same line -> inline display
                    res.append(conv_line(ln)); i += 1; continue
                block = [inner]
            else:
                block = [body]
                j = i + 1
                while j < len(lines) and "$$" not in lines[j]:
                    block.append(lines[j]); j += 1
                if j == len(lines):
                    res.append(ln); i += 1; continue  # unmatched; leave
                last = lines[j]
                before, after = last.split("$$", 1)
                if after.strip():
                    res.append(ln); i += 1; continue
                block.append(before)
            pad = " " * len(lead) if bullet else indent
            content = [strip_disallowed(b.strip()) if False else b for b in block]
            content = strip_disallowed("\n".join(content)).split("\n")
            content = [c[len(indent):] if c.startswith(indent) else c.lstrip() for c in content]
            content = [c for c in content if c.strip() != ""] or [""]
            # a fence can't start mid-paragraph inside a list cleanly; ensure blank line before
            if res and res[-1].strip() != "" and not bullet:
                res.append("")
            if bullet:
                res.append(lead + "```math")
            else:
                res.append(pad + "```math")
            res.extend(pad + c for c in content)
            res.append(pad + "```")
            i = j + 1
            continue
        res.append(conv_line(ln))
        i += 1
    return "\n".join(res)

def unindent_fences(text):
    """GitHub shows ```math as plain code when it is indented inside a list item.
    Turn indented math fences into a one-line $$...$$ paragraph (blank-line separated)."""
    lines, res, i = text.split("\n"), [], 0
    while i < len(lines):
        m = re.match(r"^(\s+|\s*(?:[-*+]|\d+\.)\s+)```math\s*$", lines[i])
        if m:
            lead = m.group(1)
            pad = " " * len(lead)
            j, body = i + 1, []
            while j < len(lines) and lines[j].strip() != "```":
                body.append(lines[j].strip()); j += 1
            expr = escfree(" ".join(b for b in body if b))
            if lead.strip():          # was on a bullet line
                res.append(lead + "$$" + expr + "$$")
            else:
                if res and res[-1].strip(): res.append("")
                res.append(pad + "$$" + expr + "$$")
                if j + 1 < len(lines) and lines[j + 1].strip(): res.append("")
            i = j + 1; continue
        res.append(lines[i]); i += 1
    return "\n".join(res)

# ---- pass 2: GitHub verbatim inline maths ----
# (from ~/.msdsm-study/github-math-fix/ghmath.py, logic unchanged)
FENCE2 = re.compile(r"^\s*(```|~~~)")
# A closing $ must not precede a digit, else "$29 / $79" pairs two prices
# into one maths span (as pass 1 already requires).
INL = re.compile(r"(?<![\\$`])\$(?![\s$`])((?:[^$\\\n`]|\\.)+?)(?<!\\)\$(?![$`\d])")
DISP = re.compile(r"^(\s+)\$\$(.+?)\$\$\s*$")

def _prose2(body):
    b = re.sub(r"\\(text|mathrm|textbf|texttt|operatorname)\{[^}]*\}", "", body)
    return '**' in body or '"' in body or re.search(r"[A-Za-z]{2,}[ ,.;]+[A-Za-z]{2,}[ ,.;]+[A-Za-z]{2,}", b)

def wrap(k):
    return k.group(0) if _prose2(k.group(1)) else "$`" + k.group(1).strip() + "`$"

def inline_line(line):
    out, i = [], 0
    for m in re.finditer(r"\$`.*?`\$|(`+).+?\1", line):
        out.append(INL.sub(wrap, line[i:m.start()]))
        out.append(m.group(0)); i = m.end()
    out.append(INL.sub(wrap, line[i:]))
    return "".join(out)

def verbatim_pass(text):
    res, in_code, fence = [], False, None
    for ln in text.split("\n"):
        f = FENCE2.match(ln)
        if in_code:
            res.append(ln)
            if f and f.group(1) == fence: in_code = False
            continue
        if f:
            in_code, fence = True, f.group(1); res.append(ln); continue
        d = DISP.match(ln)
        if d:
            res.append(d.group(1) + "$`\\displaystyle " + d.group(2).strip() + "`$"); continue
        res.append(inline_line(ln))
    return "\n".join(res)


# ---- pass 3: table rows -- a bare | inside maths would split the cell ----
VERB = re.compile(r"\$`(.*?)`\$")


def _vert(m):
    s = m.group(1)
    s = re.sub(r"\\\|", r"\\Vert{}", s)
    s = re.sub(r"(?<!\\)\|", r"\\vert{}", s)
    return "$`" + s + "`$"


def table_pass(text):
    res, in_code, fence = [], False, None
    for ln in text.split("\n"):
        f = FENCE2.match(ln)
        if in_code:
            res.append(ln)
            if f and f.group(1) == fence:
                in_code = False
            continue
        if f:
            in_code, fence = True, f.group(1)
            res.append(ln)
            continue
        if ln.lstrip().startswith("|"):
            ln = VERB.sub(_vert, ln)
        res.append(ln)
    return "\n".join(res)


# GitHub's maths renderer rejects some macros outright ("The following macros
# are not allowed: operatorname") and shows an error box instead of the maths.
# Map each to an allowed equivalent; \mathrm only loses operator spacing.
GH_MACROS = re.compile(r"\\operatorname\*?(?=\s*\{)")
GH_MACRO_SUB = r"\\mathrm"
CODESPAN = re.compile(r"\$`.*?`\$|(`+).+?\1")


def _macros_line(ln):
    # rewrite prose and $`...`$ maths spans; leave plain code spans alone
    out, i = [], 0
    for m in CODESPAN.finditer(ln):
        out.append(GH_MACROS.sub(GH_MACRO_SUB, ln[i:m.start()]))
        tok = m.group(0)
        out.append(tok if m.group(1) else GH_MACROS.sub(GH_MACRO_SUB, tok))
        i = m.end()
    out.append(GH_MACROS.sub(GH_MACRO_SUB, ln[i:]))
    return "".join(out)


def macro_pass(text):
    """Replace macros GitHub refuses to render. Skips non-maths code blocks.
    (github_issues catches leftovers via the to_github(text) != text check.)"""
    res, fence, is_math = [], None, False
    for ln in text.split("\n"):
        f = FENCE2.match(ln)
        if fence:
            if f and ln.strip() == fence:
                fence = None
            elif is_math:
                ln = GH_MACROS.sub(GH_MACRO_SUB, ln)
            res.append(ln)
            continue
        if f:
            fence, is_math = f.group(1), ln.strip() == "```math"
            res.append(ln)
            continue
        res.append(_macros_line(ln))
    return "\n".join(res)


def to_github(text):
    """Plain-$ LaTeX notes -> GitHub-safe maths. Idempotent."""
    return macro_pass(table_pass(verbatim_pass(unindent_fences(convert(text)))))


# ---- reverse, for consumers that want plain $ delimiters (Notion) ----
MATH_FENCE = re.compile(r"^(\s*)```math\s*$")
# GitHub verbatim maths or a code span, leftmost first, so `$` in code is kept.
TOKEN = re.compile(r"\$`(.*?)`\$|(`+).+?\2")
DISP_VERB = re.compile(r"^(\s*(?:(?:[-*+]|\d+\.)\s+)?)\$`\\displaystyle (.*)`\$\s*$")


def from_github(text):
    """```math fences -> multi-line $$ blocks; own-line $`\\displaystyle X`$ ->
    one-line $$X$$ (notion_body blockifies it); $`X`$ -> $X$. Code untouched."""
    lines, res, i = text.split("\n"), [], 0
    in_code, fence = False, None
    while i < len(lines):
        ln = lines[i]
        m = MATH_FENCE.match(ln)
        if not in_code and m:
            ind = m.group(1)
            j = i + 1
            body = []
            while j < len(lines) and lines[j].strip() != "```":
                body.append(lines[j])
                j += 1
            res.append(ind + "$$")
            res.extend(body)
            res.append(ind + "$$")
            i = j + 1
            continue
        f = FENCE2.match(ln)
        if in_code:
            res.append(ln)
            if f and f.group(1) == fence:
                in_code = False
            i += 1
            continue
        if f:
            in_code, fence = True, f.group(1)
            res.append(ln)
            i += 1
            continue
        d = DISP_VERB.match(ln)
        if d:
            res.append(d.group(1) + "$$" + d.group(2).strip() + "$$")
        else:
            res.append(TOKEN.sub(lambda k: k.group(0) if k.group(1) is None
                                 else "$" + k.group(1) + "$", ln))
        i += 1
    return "\n".join(res)


def github_issues(text):
    """Problems GitHub would render wrongly (empty list = clean)."""
    issues = []
    if to_github(text) != text:
        issues.append("not in GitHub maths form (run scripts/github_math.py on it)")
    in_code = False
    for n, ln in enumerate(text.split("\n"), 1):
        if re.match(r"^\s*(```|~~~)", ln):
            if re.match(r"^\s+```math", ln) and not in_code:
                issues.append(f"line {n}: indented ```math fence (GitHub shows it as code)")
            in_code = not in_code
            continue
        if not in_code and DISALLOWED.search(ln):
            issues.append(f"line {n}: \\phantom (not allowed on GitHub)")
    return issues


def main(argv):
    if argv and argv[0] == "--check":
        bad = 0
        for p in argv[1:]:
            for issue in github_issues(open(p, encoding="utf-8").read()):
                print(f"{p}: {issue}")
                bad += 1
        return 1 if bad else 0
    for p in argv:
        old = open(p, encoding="utf-8").read()
        new = to_github(old)
        if new != old:
            open(p, "w", encoding="utf-8").write(new)
            print("fixed", p)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
