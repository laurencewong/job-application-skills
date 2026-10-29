#!/usr/bin/env python3
"""Render the RESUME block of a markdown file to a one-page Letter PDF.

Usage: render_resume.py career/resume-<company>.md [--css templates/resume-print.css] [--scale 0.96]
Needs: pandoc on PATH, and Playwright for Python (`pip install playwright && playwright install chromium`).
Writes <input>.pdf next to the markdown and prints the page count.
"""
import argparse, pathlib, re, subprocess, tempfile

ap = argparse.ArgumentParser()
ap.add_argument("md")
ap.add_argument("--css", default=str(pathlib.Path(__file__).resolve().parent.parent / "templates/resume-print.css"))
ap.add_argument("--scale", type=float, default=1.0)
a = ap.parse_args()

src = pathlib.Path(a.md).read_text()
m = re.search(r"<!-- RESUME START -->(.*)<!-- RESUME END -->", src, re.S)
body = m.group(1) if m else src
with tempfile.TemporaryDirectory() as d:
    md, html = pathlib.Path(d) / "r.md", pathlib.Path(d) / "r.html"
    md.write_text(body)
    subprocess.run(["pandoc", str(md), "-s", "--embed-resources", "--css", a.css,
                    "--metadata", "pagetitle=Resume", "-o", str(html)], check=True)
    from playwright.sync_api import sync_playwright
    out = pathlib.Path(a.md).with_suffix(".pdf")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto(html.as_uri())
        pg.pdf(path=str(out), format="Letter", print_background=True, scale=a.scale)
        b.close()
pages = len(re.findall(rb"/Type\s*/Page[^s]", out.read_bytes()))
print(f"{out} ({pages} page{'s' if pages != 1 else ''})" + ("  <- over one page: trim, or try --scale 0.96" if pages > 1 else ""))
