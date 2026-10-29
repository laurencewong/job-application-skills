---
name: remove-ai-tells
description: Find and remove AI-writing tells from the user's job-application materials (resume, cover letter, free-text form answers, recruiter replies) so they read like a person wrote them. Mechanical scan + judgment pass + rewrite, facts unchanged. Use before anything in an application goes out, and as the required "human check" step inside tailor-resume, write-cover-letter and answer-job-questions.
---

# remove-ai-tells

**Rule zero: change the voice, never the facts.** Every number, title, date and claim stays exactly as verified in `career/career-facts.md`. If a fix would change meaning, leave it and flag it.

## 1. Mechanical scan
`python3 .claude/skills/remove-ai-tells/scripts/check.py <file.md>`
It checks only the RESUME block, or the body after the front matter, and flags:
- buzzwords (spearheaded, leveraged, passionate, results-driven…)
- AI words (delve, landscape, navigate, elevate, foster, pivotal…)
- intensifiers (genuinely, truly, deeply)
- stock enthusiasm and stock closes
- em-dash pauses
- "not X, but Y" mirrors
- colon reveals
- "here's the thing" openers
- clever framing
- arrows and emoji
- too many groups of three
- repeated sentence openers

Date ranges ("8/2026 – Present") are not flagged.

## 2. Judgment pass (the scan can't see these)
- **Uniform skeletons.** Every bullet shaped "**Label:** verb … metric" reads as generated. Vary the shapes and drop most bold labels.
- **Symmetry.** Paired sentences with the same rhythm ("A discount that X is Y. One that Z is W.") are a tell. One is fine; two in a row is not.
- **Semicolon chains.** Three clauses joined by semicolons is machine rhythm. Split them into sentences.
- **Over-tidy closers.** A final sentence that sums up or "lands" the paragraph should be cut.
- **Abstraction drift.** "Drove alignment", "owned the vision". Replace with what actually happened.
- **Read aloud.** Would the user say this sentence to a hiring manager across a table? If not, rewrite it plainer and shorter.

Prefer a fresh-context reviewer (a separate agent) for this pass: give it the text and this checklist only, not your reasoning.

## 3. Rewrite
- Fix each flag in the user's voice: flat, specific, short sentences (see `career/voice-profile.md`).
- Keep real lists of three when they really are lists. Remove the reflexive ones.
- Re-run the scan once. Zero flags is not required; every remaining flag needs a reason ("real list", "date range").

## 4. Output
Write a new file and keep the original, or give the fixed text inline for form answers. Then send the user a 3-line summary:
- how many tells you found
- the 2–3 biggest fixes, as before → after
- anything you left on purpose

## Where it plugs in
- `tailor-resume`: run it before export.
- `write-cover-letter`: this IS the human check.
- `answer-job-questions`: run it on every free-text answer.
- `apply-for-job`: nothing gets uploaded until it has passed.
