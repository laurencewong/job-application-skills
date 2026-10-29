---
name: tailor-resume
description: Tailor the user's resume to one specific job posting (reorder, re-emphasize, rewrite bullets in their voice) using ONLY verified facts from career/career-facts.md, then export a one-page PDF. Use when the user shares a job link or description and asks to update or tailor their resume, or as step 1 of apply-for-job.
---

# tailor-resume

**Rule zero: no lying.** Every claim, number, title and date comes from `career/career-facts.md` (or a file it links). Never invent, inflate, round up, merge roles, or imply scope the user didn't have. If the posting wants something the user hasn't confirmed (for example "managed managers"), leave a `[FILL]` and ask. Don't paper over it.

## Steps
1. **Read the posting.** Extract the title, level, must-haves, nice-to-haves, the 5–8 phrases it repeats, the pay band and the location.
2. **Read** `career/career-facts.md`, the newest base resume (`career/resume-*.md`) and `career/voice-profile.md`.
3. **Map posting to evidence.** For each must-have, name the fact that proves it, or mark it GAP. Show the GAPs to the user; never fill them with adjectives.
4. **Tailor.**
   - Summary: three lines aimed at this role.
   - Reorder sections and bullets so the most relevant proof comes first.
   - Mirror the posting's nouns where they're true (applicant-tracking systems match on them).
   - Bullets start with a verb and put the number up front.
   - One page. Cut what doesn't serve this role.
5. **Write** `career/resume-<company>-<yyyy-mm>.md`.
   - Front matter: the target role, a status, and any open `[FILL]` or `[CONFIRM]` items.
   - Wrap the resume in `<!-- RESUME START -->` / `<!-- RESUME END -->`.
   - End with a short "Tailoring notes" section: what moved, why, and the GAPs.
6. **Export** with `python3 scripts/render_resume.py career/resume-<company>-<yyyy-mm>.md`. Confirm it's one page. Markdown lists need a blank line before them or they render as run-on paragraphs.
7. **Send the user** the GAP list, any `[FILL]` questions and the PDF path. The resume is done only when they approve it.

## Never
- Unverified numbers.
- Titles they didn't hold.
- Employer internals they haven't cleared for external use.
- Pay history.
- Filler: "results-driven", "passionate", "leveraged", or "10+ years" unless it's literally true.
