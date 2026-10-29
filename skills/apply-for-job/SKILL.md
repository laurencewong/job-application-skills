---
name: apply-for-job
description: End-to-end job application. Read the posting, tailor the resume, write the cover letter, answer the form, fill the applicant-tracking form (Greenhouse, Lever, Ashby, Workday) in the browser, and submit ONLY after the user's explicit "submit". Use when the user sends a job link and says "apply" or "apply for me".
---

# apply-for-job

**Rules**
- No lying: all content comes from `career/career-facts.md` and `career/application-answers.md`.
- Nothing is submitted without the user's explicit "submit" for THIS job.
- Never create accounts or set passwords on job sites. Hand that step to the user.
- Never enter government ID or bank numbers.

## Flow
1. **Fit check (2 minutes).** Summarize the role, level, pay band, location and must-haves. Flag hard gaps honestly (e.g. "requires managing managers"). If it's a poor fit, say so before doing the work.
2. **Resume.** Run `tailor-resume`.
3. **Cover letter.** Run `write-cover-letter`, but only if the form has the field or the company clearly values one.
4. **Answers.** Run `answer-job-questions`, and send its one message of questions.
5. **Approval package** (one message to the user):
   - the role and fit summary
   - where the resume PDF is
   - the cover letter text
   - every form answer
   - anything still open
6. **Fill.**
   - Open the posting in a browser. Upload the PDFs and fill each field from the package.
   - For custom dropdowns (react-select and similar), type into the field and press Enter rather than synthesizing clicks.
   - Screenshot the whole filled form, and re-check every field against the package.
   - Wait for "submit".
7. **Submit and confirm.**
   - Click Submit only after the user says "submit."
   - If a CAPTCHA challenge appears, stop and hand it to the user.
   - Capture the confirmation page, and log the application (company, role, band, date, files) in `career/pipeline.md`.
