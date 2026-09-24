#!/usr/bin/env python3
"""Generate AI study notes from lecture transcripts using the Anthropic API
key from masters/.env (see the anthropic-api-key-location / drive-asr-transcripts
memories). Single shared script, course-specific guidance keyed by DSM code,
so new lectures/courses only need a dict entry, not a new script.

Lives in this repo (projects/msdsm-notes, standalone git repo, remote
github.com/n0tv1cky/msdsm-notes) and writes ITS OWN output here --
<this-repo>/<TERM>/<course-dir-name>/lectures/<name>.md -- not back into
subjects/. Raw transcripts stay private under subjects/<course>/transcripts/
(gitignored, not redistributable); only the derived notes this script
produces are published in this repo.

TERM is a single hardcoded constant below (all courses in COURSE_GUIDANCE
today are Batch 6 Term 1) -- bump it by hand when a new term's courses
start, there's no way to infer it from the transcripts path.

Usage: python3 generate_notes.py <transcripts_dir> [file1.txt file2.txt ...]
  <transcripts_dir> is still subjects/<dsm-code>-<short-title>/transcripts
  (files default to every *.txt in that dir; already-generated .md files
   in this repo's <TERM>/<course-dir-name>/lectures/ are skipped)
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

ENV_PATH = Path("/Users/n0tv1cky/Documents/Personal/masters/.env")
NOTES_REPO_DIR = Path(__file__).resolve().parent
TERM = "term1"
MODEL = "claude-opus-5"
MAX_TOKENS = 16000

COURSE_GUIDANCE = {
    "101": (
        "DSM-101 (Probability & Statistics)",
        "Capture named theorems/distributions precisely (e.g. CLT, Bayes' "
        "theorem, Gaussian/Poisson/Binomial), formulas written out exactly "
        "(e.g. standard error = sigma/sqrt(n)), and worked numerical "
        "examples with their actual numbers.",
    ),
    "102": (
        "DSM-102 (Programming Fundamentals for Data Science, likely Python)",
        "This content is code-heavy. Speech-to-text mangles programming "
        "syntax badly -- reconstruct it correctly using context (e.g. "
        "'four loop' -> for loop, 'dot append' -> .append(), 'i plus plus' "
        "-> i++, 'equals equals' -> ==, variable/function names as spoken). "
        "When the instructor writes or traces through code live, reproduce "
        "it as an actual fenced code block (best-effort reconstruction from "
        "the spoken walkthrough -- explicitly note where you had to infer "
        "exact syntax/values rather than presenting a guess as certain). "
        "List every function, keyword, operator, or built-in introduced "
        "with a one-line explanation. Call out any syntax rules, common "
        "mistakes, or debugging tips mentioned.",
    ),
    "103": (
        "DSM-103 (Data Structures)",
        "Correct ASR errors on CS terminology (e.g. 'big O', 'array', "
        "'pointer', 'recursion', 'stack', 'queue', 'linked list', "
        "'traversal'). For each algorithm discussed, give its steps/logic "
        "(as pseudocode or numbered steps) and time/space complexity if "
        "mentioned. Describe any diagrams or visual structures (trees, "
        "pointer diagrams, 2D array memory layouts) in words, since the "
        "transcript has no visuals. Call out indexing/addressing formulas "
        "explicitly (e.g. row-major vs column-major addressing) with the "
        "exact formula given.",
    ),
    "104": (
        "DSM-104 (Managerial Communication)",
        "Capture any communication frameworks, models, or rubrics "
        "discussed (e.g. audience-analysis dimensions, structuring a "
        "pitch, dos/don'ts of a presentation). Note any case examples, "
        "videos, or in-class exercises referenced and the lesson drawn "
        "from each -- summarize their content rather than quoting at "
        "length. Include any presentation/assignment guidelines or "
        "evaluation criteria mentioned.",
    ),
    "106": (
        "DSM-106 (Business Research)",
        "Sessions often work through a real company case study to teach "
        "a research/analytical framework. Capture the case's concrete "
        "details relevant to the analysis (company, product, numbers/"
        "prices/data used), the research question being addressed, and "
        "the methodology or framework applied (e.g. segmentation, "
        "regression, hypothesis testing, survey design, sampling). "
        "Include any statistical formulas, terms (validity, reliability, "
        "significance), or analytical steps explicitly mentioned, with "
        "the actual numbers used in any worked example.",
    ),
    "107": (
        "DSM-107 (Managerial Economics)",
        "Capture named economic models/curves (e.g. isocost, isoquant, "
        "demand/supply, MRS, MRT, opportunity cost, comparative "
        "advantage), any graphs described verbally (describe the axes "
        "and the shape/movement of the curve), and worked numerical "
        "examples with their actual numbers.",
    ),
}


def infer_course_code(transcripts_dir: Path) -> str:
    # transcripts dir's parent is like "dsm102-programming-fundamentals"
    m = re.match(r"dsm(\d+)", transcripts_dir.parent.name, re.IGNORECASE)
    if not m:
        raise RuntimeError(f"Can't infer DSM course code from {transcripts_dir.parent.name}")
    return m.group(1)


def load_api_key():
    for line in ENV_PATH.read_text().splitlines():
        line = line.strip()
        if line.startswith("ANTHROPIC_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise RuntimeError("ANTHROPIC_API_KEY not found in .env")


def build_prompt(course_name, guidance, name, transcript):
    return (
        f"This is an ASR transcript of a {course_name} graduate lecture, "
        f"session file '{name}'. Speech-to-text errors, filler words, and "
        "classroom chatter are expected -- work around them.\n\n"
        "Produce study notes in Markdown, detailed enough that someone who "
        "didn't attend the lecture can write their own handwritten notes "
        "from this alone. Include:\n"
        "1. A one-paragraph overview of what the session covers.\n"
        "2. A bulleted list of the specific topics/concepts covered, "
        "roughly in the order taught -- include any named theorems, "
        "formulas/equations (written out precisely), definitions, and "
        "worked examples (with the actual numbers/steps used).\n"
        "3. Anything flagged as important for exams/assignments, if "
        "mentioned.\n\n"
        "Formatting rule for any mathematical notation: always use proper "
        "LaTeX delimited with $...$ (inline) or $$...$$ (display), e.g. "
        "$\\int_{-\\infty}^{\\infty} P(x)\\,dx = 1$ or $E[X^2]$. Never use "
        "bare Unicode superscript/subscript characters (e.g. x², ₓᵢ) or "
        "unescaped ^/_ outside a $...$ block -- those don't render "
        "consistently. Apply this to every formula in the notes, not just "
        "the formula-sheet section.\n\n"
        f"{guidance}\n\n"
        f"Transcript:\n{transcript}"
    )


def call_api(api_key, prompt):
    body = json.dumps({
        "model": MODEL,
        "max_tokens": MAX_TOKENS,
        "messages": [{"role": "user", "content": prompt}],
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=body,
        headers={
            "content-type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=300) as resp:
        return json.loads(resp.read())


def main():
    transcripts_dir = Path(sys.argv[1]).resolve()
    course_code = infer_course_code(transcripts_dir)
    course_name, guidance = COURSE_GUIDANCE[course_code]
    course_dir_name = transcripts_dir.parent.name  # e.g. "dsm107-managerial-economics"

    api_key = load_api_key()
    notes_dir = NOTES_REPO_DIR / TERM / course_dir_name / "lectures"
    notes_dir.mkdir(parents=True, exist_ok=True)

    txt_files = sorted(transcripts_dir.glob("*.txt"))
    targets = sys.argv[2:] if len(sys.argv) > 2 else [p.name for p in txt_files]

    for fname in targets:
        p = transcripts_dir / fname
        out_path = notes_dir / (p.stem + ".md")
        if out_path.exists():
            print("SKIP (exists):", out_path.name)
            continue
        transcript = p.read_text(encoding="utf-8")
        word_count = len(transcript.split())
        if word_count == 0:
            print("SKIP (empty transcript, no ASR available):", p.name)
            continue
        print(f"Generating notes: {p.name} ({word_count} words, course {course_code})")
        try:
            data = call_api(api_key, build_prompt(course_name, guidance, p.stem, transcript))
        except Exception as e:
            print("  ERROR (API call):", e)
            continue
        stop_reason = data.get("stop_reason")
        text = "".join(block.get("text", "") for block in data.get("content", []))
        if stop_reason != "end_turn":
            print(f"  TRUNCATED (stop_reason={stop_reason}) -- NOT saving. "
                  f"Got {len(text.split())} words; raise MAX_TOKENS or split the transcript.")
            continue
        out_path.write_text(text, encoding="utf-8")
        print(f"  saved {out_path.name} ({len(text.split())} words, stop_reason={stop_reason})")


if __name__ == "__main__":
    main()
