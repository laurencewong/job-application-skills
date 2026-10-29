---
name: write-cover-letter
description: Write a short, human-sounding cover letter for one job in the user's real voice, grounded only in verified facts, then check it for AI tells. Use when an application has a cover letter field, or the user asks for one.
---

# write-cover-letter

**No lying.** Facts come only from `career/career-facts.md`. No invented stories, metrics, mutual connections, or enthusiasm for things the user hasn't said.

## Shape
250 words max, in 3–4 short paragraphs of plain text.
1. **Why this role, specifically.** One concrete thing about the company or product, taken from the posting or the company's public site, tied to the user's actual experience. No "I'm excited to apply."
2. **The proof.** Two or three results that match the posting's must-haves, using the resume's exact numbers.
3. **How they work.** One honest line on their approach, in their voice from `career/voice-profile.md`.
4. **Close.** A plain line. No begging, no "at your earliest convenience."

## Human check (required)
- Run a fresh-context reviewer (a separate agent with no access to your draft's reasoning) to look for AI tells:
  - mirrored "not X but Y" lines
  - stacked groups of three
  - generic praise
  - colon reveals
  - em-dash asides
- Fix what it finds, then check once more.
- Read-aloud test: would the user say each sentence to a hiring manager? If not, rewrite it.

Save as `career/cover-<company>-<yyyy-mm>.md`. The user approves it before it's used.
