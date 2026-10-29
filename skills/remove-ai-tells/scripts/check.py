#!/usr/bin/env python3
"""Flag AI-writing tells in job-application text (resume, cover letter, form answers).

Usage: check.py <file.md> [--block START END]
Only text between <!-- RESUME START --> / <!-- RESUME END --> is checked if those
markers exist; front matter and "Tailoring notes" are skipped. Prints one line per
hit with the line number, the tell, and the offending text. Mechanical only: a
human-voice judgment pass still has to follow (see SKILL.md).
"""
import re
import sys

WORDS = {
    # resume/cover-letter buzzwords that read as generated
    "spearheaded": "buzzword", "orchestrated": "buzzword", "leveraged": "buzzword",
    "leverage": "buzzword", "utilize": "buzzword", "utilized": "buzzword",
    "passionate": "buzzword", "results-driven": "buzzword", "dynamic": "buzzword",
    "fast-paced": "buzzword", "proven track record": "buzzword", "thrive": "buzzword",
    "seamless": "buzzword", "seamlessly": "buzzword", "robust": "buzzword",
    "holistic": "buzzword", "synergy": "buzzword", "impactful": "buzzword",
    "cutting-edge": "buzzword", "best-in-class": "buzzword", "world-class": "buzzword",
    "delve": "AI word", "tapestry": "AI word", "testament": "AI word",
    "landscape": "AI word", "ever-evolving": "AI word", "navigate": "AI word",
    "elevate": "AI word", "unlock": "AI word", "empower": "AI word", "foster": "AI word",
    "harness": "AI word", "pivotal": "AI word", "crucial": "AI word", "realm": "AI word",
    "genuinely": "intensifier", "truly": "intensifier", "deeply": "intensifier",
    "incredibly": "intensifier", "honestly": "intensifier",
    "excited to": "stock enthusiasm", "thrilled": "stock enthusiasm",
    "i look forward to": "stock close", "at your earliest convenience": "stock close",
    "i am confident": "stock close", "i believe i would be": "stock close",
}
PATTERNS = [
    (r"(?<![\d])\s[—–]\s(?![\d]|present)|[a-z]—[a-z]", "em/en dash used as a pause; use a period or a comma"),
    (r"\b(isn't|is not|wasn't|not)\b[^.]{0,60}[,;.]\s*(it's|it is|but)\b", "\"not X, but Y\" / \"isn't X. It's Y\" mirror"),
    (r"\bnot (just|only|merely)\b", "\"not just X\" framing"),
    (r"(?<!\*)(?<!\*\*)\b[a-z][^.:*]{8,60}:\s+[a-z$\d]", "colon reveal mid-sentence; consider two sentences"),
    (r"\b(here's|here is) (the|what|why|how)\b", "\"here's the thing\" opener"),
    (r"\b(in short|simply put|put simply|at its core|the bottom line)\b", "summarizing tic"),
    (r"\b(in pieces|the job i've been preparing for|everything i've)\b", "clever framing; say it plainly"),
    (r"→|➜|⇒", "arrow glyph"),
    (r"[🚀✨🔥💡👇✅]", "emoji"),
]
TRIPLET = r"\b[\w$&-]+, [\w$&-]+,? (and|or) [\w$&-]+\b"


def body(text: str) -> list[tuple[int, str]]:
    lines = text.split("\n")
    start, end = 0, len(lines)
    for i, l in enumerate(lines):
        if "RESUME START" in l:
            start = i + 1
        if "RESUME END" in l:
            end = i
    if start == 0 and lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                start = i + 1
                break
    out = []
    for i in range(start, end):
        if re.match(r"^#+\s*(tailoring notes|notes)\b", lines[i], re.I):
            break
        out.append((i + 1, lines[i]))
    return out


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    text = open(sys.argv[1], encoding="utf-8").read()
    hits = 0
    openers: dict[str, list[int]] = {}
    for n, line in body(text):
        low = line.lower()
        for w, label in WORDS.items():
            if re.search(r"(?<![\w-])" + re.escape(w) + r"(?![\w-])", low):
                print(f"L{n}: {label}: \"{w}\"  | {line.strip()[:110]}")
                hits += 1
        for pat, label in PATTERNS:
            if re.search(pat, line, re.I):
                print(f"L{n}: {label}  | {line.strip()[:110]}")
                hits += 1
        for sent in re.split(r"(?<=[.!?])\s+", line.strip()):
            w = re.sub(r"[^a-z' ]", "", sent.lower()).split()[:2]
            if len(w) == 2:
                openers.setdefault(" ".join(w), []).append(n)
    trip = [n for n, line in body(text) if re.search(TRIPLET, line, re.I)]
    if len(trip) > 3:
        print(f"L{','.join(map(str, trip))}: {len(trip)} lines with groups of three; vary the rhythm (keep the ones that are real lists)")
        hits += 1
    for o, ns in openers.items():
        if len(ns) >= 3 and o not in ("i run", "i built"):
            print(f"L{','.join(map(str, ns))}: repeated sentence opener \"{o} …\" x{len(ns)}")
            hits += 1
    print(f"--- {hits} flag(s). Mechanical only: now do the judgment pass in SKILL.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
