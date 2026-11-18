#!/usr/bin/env python3
"""Draft a course recap page module-by-module with the Anthropic API, then
assemble the drafts into one self-contained HTML page.

This does the bulk writing of a recap (cheat cards, analogies, widget code).
It does NOT replace the verification steps in the building-course-recaps
skill: every drafted number is still recomputed in Python and every widget
stepped through in a browser before anything is committed.

Key: ANTHROPIC_API_KEY from masters/.env (same as generate_notes.py).

Usage (from the repo root):
  python3 scripts/build_recap.py plan     <course-dir> <example-plan.json>  # draft plan.json from all notes
  python3 scripts/build_recap.py plan-extend <course-dir> <example-plan.json> <next-module-no> "<existing module titles>" [note-glob ...]
                                                                    # plan only new lectures -> recap/plan-ext.json
  python3 scripts/build_recap.py draft    <plan.json> [m1 m3 ...]   # one API call per module
  python3 scripts/build_recap.py assemble <plan.json>               # stitch drafts -> page
  python3 scripts/build_recap.py extend   <plan-ext.json> ["kicker"] [before-id]  # merge drafts into an existing page

plan.json:
{
  "course_dir": "term1/dsm109-mathematical-programming",
  "title": "DSM-109 Full Course Recap",
  "kicker": "DSM-109 Mathematical Programming · full course recap · S1–S9 (Vatsa)",
  "legend": [["amber", "..."], ["teal", "..."]],
  "katex": true,
  "footer": "one paragraph",
  "course_notes": "course-wide guidance for the drafter (contrast colours, quiz format...)",
  "modules": [
    {"id": "m1", "nav": "1 · Why OR", "sessions": ["DSM-109-1_2026-10-22_Amit-Kumar-Vatsa", ...],
     "plan": "the approved plan row, in prose",
     "facts": "numbers already verified in Python -- the drafter must use these exactly"}
  ]
}
Drafts land in .recap-build/<course-dir-name>/ (gitignored): <id>.html, <id>.js,
<id>.raw.txt (full response) and usage.json (tokens + cost per call).
"""
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ENV_PATH = Path("/Users/n0tv1cky/Documents/Personal/masters/.env")
KIT = REPO / ".claude/skills/building-course-recaps/kit"
MODEL = "claude-opus-5-5"
EFFORT = "high"
MAX_TOKENS = 128000
PRICE_IN, PRICE_OUT, PRICE_CACHE_READ, PRICE_CACHE_WRITE = 4.0, 20.0, 0.20, 5.0  # $/MTok (5-min cache write = 1.25x)


def load_api_key():
    for line in ENV_PATH.read_text().splitlines():
        line = line.strip()
        if line.startswith("ANTHROPIC_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise RuntimeError("ANTHROPIC_API_KEY not found in .env")


RULES = """You draft ONE module of a self-contained HTML revision page ("course recap") for a
graduate MSDSM course. The student reads it before exams on desktop and phone. The page
already exists around your module: head, CSS, jump-nav, hero, footer, and a shared JS
core are supplied by the assembler. You write only your module's <section> and, if the
plan asks for one, its widget script.

OUTPUT FORMAT (strict):
1. One ```html fenced block containing exactly one
   <section class="module" id="{ID}"> ... </section>.
2. One ```js fenced block with the widget code: zero or more IIFEs, each starting with
   `(function(){ const panel = document.getElementById('...'); if (!panel) return;`.
   If the module has no widget, output an empty ```js block.
Nothing else outside the two blocks except at most three short lines of notes for the
reviewer (e.g. a number you could not find in the notes).

CONTENT RULES
- Concise: cheat-card entries are fragments, not paragraphs. No hero blurb. The module
  head is: <p class="module-tag">sessions (dates) — instructor</p>, <h2>, one-sentence <p class="lede">.
- Order inside a module: module-head, cheat-grid (2 or 3 cards; use .cheat-grid.two for 2),
  optional table-wrap tables, .note callouts for the professor's analogies/stories/repeated
  points (cite the session, e.g. "S03"), then interactive panel(s), then 1-3
  <details class="worked"> problems taken from the lecture with the lecture's own numbers
  and a final <div class="answer">.
- Any callout with more than one idea is a bulleted .note (<p> lead-in, then <ul><li>).
- The professor's analogies, stories and repeated warnings are the most valued content.
  Keep every one the plan lists, attributed to its session.
- Use ONLY numbers that appear in the supplied lecture notes or in the VERIFIED FACTS
  block. VERIFIED FACTS override the notes when they differ. Never invent data. If the
  notes flag something as inferred/ASR-garbled, either use the verified value or say
  "(reconstructed)".
- Leave out admin (grading weights, logistics, quiz rules) unless the plan says otherwise.
- NEVER name students. The notes sometimes name a student ("<name>'s solution",
  "suggested by <name>"): write "a student". Faculty names are fine.
- Colour thread: amber (var(--amber), <code>, dt) = one side of the course's central
  contrast; teal (var(--teal), <code class="t">, dt.t) = the other. The course notes
  say which is which. Rust (var(--rust)) = errors / wrong answers / infeasible.
- Maths: if KaTeX is on, write $...$ inline and $$...$$ display. Widget panels must carry
  class "nomath" so KaTeX skips them. Inside JS strings never use $ delimiters.
- Use only CSS classes that exist in the supplied stylesheet. Inline style only for
  one-off colours via the CSS variables. No new <style> blocks.
- No external libraries, fonts, images or network requests.

WIDGET RULES (the plan says which widgets; zero is a valid answer)
- Prefix every element id with the module id (e.g. m3Chart, m3Slider) so ids never clash.
- Use the shared helpers already in scope: el(tag, attrs) for SVG, h(tag, cls, txt) for
  HTML, clear(node), esc(s), ns(s) (minus sign), frame({x0,y0,w,h}), ticks(min,max,step),
  drawAxes(svg,f,xTicks,yTicks,xLabel,yLabel,xFmt,yFmt), COLORS {amber,teal,ink,dim,faint,
  line,rust}, REDUCED (prefers-reduced-motion), Player(panel, render, opts) for step-through
  animations (see the example: .viz-body, pre.pcode, .vars, .caption, .transport with
  data-act=reset|back|play|next, states [{line, vars:[[k,v]], cap, ...}]), presets(row, cb),
  Pool/place/fit/follow for moving DOM pieces.
- Charts: <svg class="chart" viewBox=...>; re-render on input and on window resize; when the
  container is narrower than 560px switch to a narrower viewBox with larger text (see the
  Big-O example). One scale places marks, ticks and labels. Clip curves to the frame with a
  clipPath instead of clamping y values. Every slider sweep from min to max must keep marks
  inside the frame.
- Every widget opens in a meaningful resting state (a lecture example already loaded), so
  print and thumbnails show something real. A .readout and a .verdict line state the
  result in words.
- Expose pure calculation functions on window.__recap.<moduleId> = {...} so the reviewer
  can check them against Python (e.g. corner points, objective values, ranges).
- Captions explain in plain words what just changed and why, using the lecture's terms.
- Must work at 360px width: no fixed widths wider than the screen; wide drawings go in
  .stage-scroll or a responsive viewBox.
"""


def kit_text():
    parts = [
        ("STYLESHEET (already on the page)", "css", (KIT / "style.css").read_text()),
        ("SHARED JS CORE (already in scope; your code is appended inside the same IIFE)", "js", (KIT / "core.js").read_text()),
        ("EXAMPLE MODULE (DSM-103, for structure and tone)", "html", (KIT / "example-module.html").read_text()),
        ("EXAMPLE SLIDER PANEL MARKUP (DSM-103 Big-O)", "html", (KIT / "example-slider-panel.html").read_text()),
        ("EXAMPLE WIDGETS (DSM-103: a Player step-through, then a slider chart)", "js", (KIT / "example-widgets.js").read_text()),
    ]
    return "\n\n".join(f"### {t}\n```{lang}\n{body}\n```" for t, lang, body in parts)


def module_prompt(plan, mod):
    notes_dir = REPO / plan["course_dir"] / "lectures"
    notes = []
    for stem in mod["sessions"]:
        p = notes_dir / (stem + ".md")
        notes.append(f"=== {p.name} ===\n{p.read_text(encoding='utf-8')}")
    return (
        f"COURSE: {plan['kicker']}\n"
        f"KaTeX: {'on' if plan.get('katex') else 'off (use <code> for formulas)'}\n"
        f"COURSE-WIDE NOTES: {plan.get('course_notes', '')}\n\n"
        f"YOUR MODULE: id={mod['id']}, nav label \"{mod['nav']}\"\n"
        f"APPROVED PLAN FOR THIS MODULE:\n{mod['plan']}\n\n"
        f"VERIFIED FACTS (computed in Python; use exactly):\n{mod.get('facts', '(none)')}\n\n"
        f"LECTURE NOTES FOR THIS MODULE:\n\n" + "\n\n".join(notes)
    )


def call_stream(api_key, system_blocks, user_text):
    body = json.dumps({
        "model": MODEL,
        "max_tokens": MAX_TOKENS,
        "stream": True,
        "output_config": {"effort": EFFORT},
        "fallbacks": "default",
        "system": system_blocks,
        "messages": [{"role": "user", "content": user_text}],
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages", data=body, method="POST",
        headers={
            "content-type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2026-10-21",
            "anthropic-beta": "server-side-fallback-2026-07-01",
        })
    text, usage, stop, served = [], {}, None, MODEL
    with urllib.request.urlopen(req, timeout=1800) as resp:
        for raw in resp:
            line = raw.decode("utf-8").rstrip("\n")
            if not line.startswith("data: "):
                continue
            ev = json.loads(line[6:])
            t = ev.get("type")
            if t == "message_start":
                usage.update(ev["message"].get("usage", {}))
                served = ev["message"].get("model", served)
            elif t == "content_block_delta" and ev["delta"].get("type") == "text_delta":
                text.append(ev["delta"]["text"])
            elif t == "message_delta":
                stop = ev["delta"].get("stop_reason") or stop
                usage.update({k: v for k, v in ev.get("usage", {}).items() if v is not None})
            elif t == "error":
                raise RuntimeError(f"stream error: {ev}")
    return "".join(text), usage, stop, served


def cost(u):
    return (u.get("input_tokens", 0) * PRICE_IN + u.get("output_tokens", 0) * PRICE_OUT
            + u.get("cache_read_input_tokens", 0) * PRICE_CACHE_READ
            + u.get("cache_creation_input_tokens", 0) * PRICE_CACHE_WRITE) / 1e6


def build_dir(plan):
    d = REPO / ".recap-build" / Path(plan["course_dir"]).name
    d.mkdir(parents=True, exist_ok=True)
    return d


def draft(plan, only):
    api_key = load_api_key()
    out = build_dir(plan)
    system = [
        {"type": "text", "text": RULES},
        {"type": "text", "text": kit_text(), "cache_control": {"type": "ephemeral"}},
    ]
    log_path = out / "usage.json"
    log = json.loads(log_path.read_text()) if log_path.exists() else []
    for mod in plan["modules"]:
        if only and mod["id"] not in only:
            continue
        print(f"[{mod['id']}] drafting ({len(mod['sessions'])} notes)...", flush=True)
        t0 = time.time()
        for attempt in range(3):
            try:
                text, usage, stop, served = call_stream(api_key, system, module_prompt(plan, mod))
                break
            except Exception as e:  # network / 5xx / overloaded: back off and retry
                print(f"  attempt {attempt + 1} failed: {e}", flush=True)
                if attempt == 2:
                    raise
                time.sleep(30 * (attempt + 1))
        (out / f"{mod['id']}.raw.txt").write_text(text)
        html_m = re.search(r"```html\s*\n(.*?)```", text, re.S)
        js_m = re.search(r"```js\s*\n(.*?)```", text, re.S)
        if stop != "end_turn" or not html_m:
            print(f"  WARNING stop_reason={stop}, html block found={bool(html_m)}; see {mod['id']}.raw.txt")
        if html_m:
            (out / f"{mod['id']}.html").write_text(html_m.group(1).strip() + "\n")
        (out / f"{mod['id']}.js").write_text((js_m.group(1).strip() + "\n") if js_m else "")
        tail = text[text.rfind("```") + 3:].strip() if "```" in text else ""
        c = cost(usage)
        log.append({"module": mod["id"], "model": served, "stop": stop, "usage": usage,
                    "cost_usd": round(c, 4), "seconds": round(time.time() - t0), "when": time.strftime("%F %T")})
        log_path.write_text(json.dumps(log, indent=1))
        print(f"  done in {time.time() - t0:.0f}s · {usage.get('output_tokens')} out · ${c:.2f} · served by {served}")
        if tail:
            print("  reviewer notes:", tail[:600])
    print(f"Total logged spend for this course: ${sum(x['cost_usd'] for x in log):.2f}")


def assemble(plan):
    out = build_dir(plan)
    css = (KIT / "style.css").read_text()
    katex = ""
    if plan.get("katex"):
        katex = ('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">\n'
                 '<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>\n'
                 '<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"\n'
                 "  onload=\"renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},"
                 "{left:'$',right:'$',display:false}],ignoredClasses:['nomath'],throwOnError:false})\"></script>\n")
    nav = "\n".join(f'  <a href="#{m["id"]}">{m["nav"]}</a>' for m in plan["modules"])
    legend = "\n".join(f'      <span><i class="swatch" style="background:var(--{c})"></i>{t}</span>'
                       for c, t in plan.get("legend", []))
    sections, scripts = [], []
    for m in plan["modules"]:
        sections.append(f"<!-- ============ {m['id']}: {m['nav']} ============ -->\n" + (out / f"{m['id']}.html").read_text())
        js = (out / f"{m['id']}.js").read_text() if (out / f"{m['id']}.js").exists() else ""
        if js.strip():
            scripts.append(f"  // ================= {m['id']}: {m['nav']} =================\n" + js)
    core = (KIT / "core.js").read_text().replace("window.__ds = {};", "window.__ds = {}; window.__recap = {};")
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{plan['title']}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,500&family=Source+Sans+3:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
{katex}<style>
{css}
</style>
</head>
<body>

<div class="progress" id="progress"></div>

<nav class="jumpnav">
{nav}
</nav>

<header class="hero">
  <div class="wrap-wide">
    <p class="kicker">{plan['kicker']}</p>
    <div class="legend">
{legend}
    </div>
  </div>
</header>

{chr(10).join(sections)}
<footer>
  <div class="wrap-wide"><p>{plan.get('footer', '')}</p></div>
</footer>
<script>
{core}
{chr(10).join(scripts)}
{(KIT / 'chrome.js').read_text()}
</script>
</body>
</html>
"""
    dest = REPO / plan["course_dir"] / "recap" / "course-recap.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(page)
    print("wrote", dest.relative_to(REPO), f"({len(page) // 1024} KB)")


PLAN_RULES = """You plan an interactive revision page ("course recap") for one graduate MSDSM
course, from its lecture notes. Read EVERY note. Output one ```json block holding a plan
in exactly the format of the example plan you are given (same keys), then at most ten
short lines for the reviewer: duplicate/missing sessions, sessions that are admin-only or
quiz-only (exclude them from modules), garbled or contradictory numbers you noticed.

Planning rules (from the building-course-recaps skill):
- Group sessions into 4-8 modules (topic clusters) in recording-date order. A note may
  belong to two modules if a session spans topics.
- Classify each module's content type: numerical / derivation (sliders + recomputed
  numbers), algorithmic (step-through animation with highlighted pseudocode and live
  variables), code (runnable-looking snippets with outputs), framework / conceptual (cards
  and tables; ZERO widgets is the right answer for pure frameworks), case (decision tables).
  Never add a chart to framework content just to look interactive. At most 1-2 widgets per
  module; each widget must teach something a card can't, and must replay the lecture's own
  example with its own numbers.
- For each module the "plan" text lists: the cheat cards (formulas, definitions, rules,
  procedures) as fragments; EVERY professor analogy, story, joke-with-a-point and repeated
  warning, each with its session (these are the most valued content); the widget(s) with
  exactly what they show, their presets from the lecture, readouts and verdicts; and 1-3
  worked problems taken from the lecture.
- "facts" lists every number the module will show, copied exactly from the notes, with the
  arithmetic written out so a reviewer can recompute it in Python. Mark values the notes
  flag as inferred/ASR-garbled. Do not invent data.
- Never name students; faculty names are fine.
- "course_notes" states the central contrast and which side is amber vs teal, the
  instructors, currencies/units, and any exam-format statements in the notes.
- "katex": true only if the course is formula-heavy.
- "sessions" entries are note filename stems exactly as given (no .md).
"""


def plan_course(course_dir, example_plan, globs=(), extend=None):
    """extend = {"start": 8, "existing": "titles of modules already on the page", "out": "plan-ext.json"}"""
    api_key = load_api_key()
    notes_dir = REPO / course_dir / "lectures"
    files = sorted(p for p in notes_dir.glob("*.md") if p.name.lower() != "readme.md")
    if globs:
        files = sorted({p for g in globs for p in notes_dir.glob(g + ".md")})
    notes = "\n\n".join(f"=== {p.stem} ===\n{p.read_text(encoding='utf-8')}" for p in files)
    ext = ""
    if extend:
        ext = (f"EXTENSION MODE: these notes are the NEW lectures of a course whose recap page already has "
               f"modules covering earlier sessions: {extend['existing']}. Plan only modules for the new notes, "
               f"with ids starting at m{extend['start']} (m{extend['start']}, m{extend['start'] + 1}, ...) and nav "
               f"labels numbered from {extend['start']}. Do not repeat material the existing modules already cover; "
               f"you may refer back to them. Keep title/kicker/legend/footer consistent with an existing page "
               f"(the assembler will not use them).\n\n")
    user = (ext + f"COURSE DIR: {course_dir}\nNOTE FILES: {', '.join(p.stem for p in files)}\n\n"
            f"EXAMPLE PLAN (another course, for format and depth):\n```json\n{Path(example_plan).read_text()}\n```\n\n"
            f"ALL LECTURE NOTES:\n\n{notes}")
    out = REPO / ".recap-build" / Path(course_dir).name
    out.mkdir(parents=True, exist_ok=True)
    print(f"planning {course_dir} ({len(files)} notes)...", flush=True)
    t0 = time.time()
    text, usage, stop, served = call_stream(api_key, [{"type": "text", "text": PLAN_RULES}], user)
    (out / "plan.raw.txt").write_text(text)
    m = re.search(r"```json\s*\n(.*?)```", text, re.S)
    dest = REPO / course_dir / "recap" / ((extend or {}).get("out") or "plan.json")
    dest.parent.mkdir(parents=True, exist_ok=True)
    if m:
        json.loads(m.group(1))  # fail loudly on malformed JSON
        dest.write_text(m.group(1).strip() + "\n")
    c = cost(usage)
    log_path = out / "usage.json"
    log = json.loads(log_path.read_text()) if log_path.exists() else []
    log.append({"module": "plan", "model": served, "stop": stop, "usage": usage, "cost_usd": round(c, 4),
                "seconds": round(time.time() - t0), "when": time.strftime("%F %T")})
    log_path.write_text(json.dumps(log, indent=1))
    print(f"  stop={stop} · {usage.get('output_tokens')} out · ${c:.2f} · wrote {dest.relative_to(REPO) if m else 'NOTHING'}")
    print("  reviewer notes:", text[text.rfind('```') + 3:].strip()[:1500])


def extend(plan, kicker=None, before_id=None):
    """Insert drafted extension modules into an existing course-recap.html:
    sections go before the footer (or before section id=before_id), nav links are
    appended, the kit CSS is prepended to <head> (existing rules still win), and the
    widgets run in their own <script> with a fresh copy of the kit core."""
    out = build_dir(plan)
    page_path = REPO / plan["course_dir"] / "recap" / "course-recap.html"
    page = page_path.read_text()
    mods = plan["modules"]
    sections = "\n".join(f"<!-- ============ {m['id']}: {m['nav']} ============ -->\n" + (out / f"{m['id']}.html").read_text()
                         for m in mods)
    js = "\n".join((out / f"{m['id']}.js").read_text() for m in mods if (out / f"{m['id']}.js").exists())
    if before_id:
        anchor = page.index(f'<section class="module" id="{before_id}"')
        anchor = page.rfind("\n", 0, anchor) + 1
        prev = page.rfind("<!--", 0, anchor)  # keep a banner comment with its section
        if prev != -1 and page[prev:anchor].strip().endswith("-->") and "\n" not in page[prev:anchor].strip():
            anchor = prev
    else:
        anchor = page.index("<footer")
    page = page[:anchor] + sections + "\n\n" + page[anchor:]
    nav_end = page.index("</nav>")
    links = "".join(f'  <a href="#{m["id"]}">{m["nav"]}</a>\n' for m in mods)
    if before_id:  # keep the trailing reference link (e.g. the complexity sheet) last
        ref = page.rfind(f'<a href="#{before_id}">', 0, nav_end)
        line_start = page.rfind("\n", 0, ref) + 1
        page = page[:line_start] + links + page[line_start:]
    else:
        page = page[:nav_end] + links + page[nav_end:]
    if "/* recap kit */" not in page:
        head_style = page.index("<style>")
        page = page[:head_style] + "<style>/* recap kit */\n" + (KIT / "style.css").read_text() + "\n</style>\n" + page[head_style:]
    core = (KIT / "core.js").read_text().replace("window.__ds = {};", "window.__ds = window.__ds || {}; window.__recap = window.__recap || {};")
    script = f"<script>\n{core}\n{js}\n}})();\n</script>\n"
    body_end = page.rindex("</body>")
    page = page[:body_end] + script + page[body_end:]
    if kicker:
        page = re.sub(r'(<p class="kicker">)[^<]*(</p>)', lambda m_: m_.group(1) + kicker + m_.group(2), page, count=1)
    page_path.write_text(page)
    print("extended", page_path.relative_to(REPO), f"with {len(mods)} modules ({len(page) // 1024} KB)")


def main():
    if len(sys.argv) >= 3 and sys.argv[1] == "extend":
        # extend <plan-ext.json> ["new kicker"] [insert-before-section-id]
        extend(json.loads(Path(sys.argv[2]).read_text()), sys.argv[3] if len(sys.argv) > 3 else None,
               sys.argv[4] if len(sys.argv) > 4 else None)
        return
    if len(sys.argv) >= 4 and sys.argv[1] == "plan":
        plan_course(sys.argv[2], sys.argv[3])
        return
    if len(sys.argv) >= 6 and sys.argv[1] == "plan-extend":
        # plan-extend <course-dir> <example-plan> <start-module-number> <existing-titles> [glob ...]
        plan_course(sys.argv[2], sys.argv[3], sys.argv[6:],
                    {"start": int(sys.argv[4]), "existing": sys.argv[5], "out": "plan-ext.json"})
        return
    if len(sys.argv) < 3 or sys.argv[1] not in ("draft", "assemble"):
        print(__doc__)
        sys.exit(1)
    plan = json.loads(Path(sys.argv[2]).read_text())
    if sys.argv[1] == "draft":
        draft(plan, set(sys.argv[3:]))
    else:
        assemble(plan)


if __name__ == "__main__":
    main()
