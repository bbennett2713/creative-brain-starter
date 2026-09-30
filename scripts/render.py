#!/usr/bin/env python3
"""Turn an ad written in HTML into PNG images.

Usage:
    python3 scripts/render.py output/batch-01/ad-01.html
    python3 scripts/render.py output/batch-01/*.html --sizes 1080x1080,1080x1350
    python3 scripts/render.py templates/branded.html --out output/test

Each HTML file becomes one PNG per size, saved next to the HTML file
(or in --out), named like ad-01-1080x1080.png.

The HTML should size itself to the window (use vw / vh / % units),
so one file works for both square and 4:5.

It warns when an image or a font fails to load, so a wrong path never
slips through as a silent fallback.
"""

import argparse
import sys
from pathlib import Path

INSTALL_HELP = """
The renderer needs Playwright (a free tool that drives a hidden browser).
Install it once with:

    python3 -m pip install playwright

If you don't have Google Chrome installed, also run:

    python3 -m playwright install chromium

If pip says "externally managed environment", use a local environment instead:

    python3 -m venv .venv
    .venv/bin/python -m pip install playwright
    .venv/bin/python scripts/render.py <your files>

(Inside Claude Code, just say "install the renderer for me".)
"""

DEFAULT_SIZES = "1080x1080,1080x1350"

FAILED_FONTS_JS = """
async () => {
  await document.fonts.ready;
  const bad = [];
  for (const f of document.fonts) {
    if (f.status === "unloaded") { try { await f.load(); } catch (e) {} }
    if (f.status === "error") bad.push(f.family + " " + f.weight);
  }
  return bad;
}
"""


def parse_sizes(text):
    sizes = []
    for part in text.split(","):
        part = part.strip().lower()
        if not part:
            continue
        try:
            w, h = part.split("x")
            sizes.append((int(w), int(h)))
        except ValueError:
            sys.exit(f"Could not read size '{part}'. Use WIDTHxHEIGHT, like 1080x1350.")
    return sizes


def launch_browser(p):
    """Try the Chrome already on the computer first, then Playwright's own."""
    errors = []
    for kwargs in ({"channel": "chrome"}, {}):
        try:
            return p.chromium.launch(**kwargs)
        except Exception as e:
            errors.append(str(e).splitlines()[0])
    print(INSTALL_HELP)
    print("Details: " + " | ".join(errors))
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Render HTML ads to PNG.")
    parser.add_argument("html", nargs="+", help="One or more HTML files")
    parser.add_argument("--sizes", default=DEFAULT_SIZES,
                        help=f"Comma-separated sizes (default {DEFAULT_SIZES})")
    parser.add_argument("--out", default=None,
                        help="Folder for the PNGs (default: next to each HTML file)")
    args = parser.parse_args()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print(INSTALL_HELP)
        sys.exit(1)

    sizes = parse_sizes(args.sizes)
    files = [Path(p).resolve() for p in args.html]
    missing = [str(f) for f in files if not f.is_file()]
    if missing:
        sys.exit("Can't find: " + ", ".join(missing))

    made, warnings = [], 0
    with sync_playwright() as p:
        browser = launch_browser(p)
        for f in files:
            out_dir = Path(args.out).resolve() if args.out else f.parent
            out_dir.mkdir(parents=True, exist_ok=True)
            for (w, h) in sizes:
                page = browser.new_page(viewport={"width": w, "height": h},
                                        device_scale_factor=1)
                page.goto(f.as_uri())
                page.wait_for_load_state("networkidle")
                bad_fonts = page.evaluate(FAILED_FONTS_JS)
                broken = page.evaluate(
                    "[...document.images].filter(i => !i.complete || i.naturalWidth === 0)"
                    ".map(i => i.getAttribute('src'))")
                if (w, h) == sizes[0]:  # report once per file, not once per size
                    for src in broken:
                        print(f"  warning: image did not load in {f.name}: {src}")
                        warnings += 1
                    for fam in bad_fonts:
                        print(f"  warning: font did not load in {f.name}: {fam} "
                              "(a fallback font was used; check the @font-face path)")
                        warnings += 1
                target = out_dir / f"{f.stem}-{w}x{h}.png"
                page.screenshot(path=str(target), clip={"x": 0, "y": 0, "width": w, "height": h})
                page.close()
                made.append(target)
        browser.close()

    for m in made:
        print(f"made {m}")
    if warnings:
        print(f"{warnings} warning(s) above. Fix them before showing these ads.")


if __name__ == "__main__":
    main()
