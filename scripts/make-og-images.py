#!/usr/bin/env python3
"""Regenerate the five social preview images in assets/img/.

Each image is 1200x630: cream ground, the triangle M from assets/img/mark.svg
inset at 72,60, a headline in the display face (Unbounded 900 at the tracking
assets/css/style.css sets) and an Archivo label along the bottom left.

The page is laid out as HTML and shot by headless Chrome, so the type is set by
the same engine and the same font files the live site uses. Every image is then
measured back off its own pixels - mark box, headline cap top, label cap top,
margins - and a run that misses the grid fails instead of writing.

Usage:
    python3 scripts/make-og-images.py            # write assets/img/og-*.png
    python3 scripts/make-og-images.py --check    # render and verify, write nothing

Needs Google Chrome, and Pillow (pip install pillow) for the measuring. The two
webfonts are pulled from Google Fonts once and cached in scripts/.cache/.
"""

from __future__ import annotations

import argparse
import base64
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

try:
    from PIL import Image, ImageChops
except ImportError:  # pragma: no cover - a missing install, not a code path
    sys.exit("Pillow is required: pip install pillow")

ROOT = Path(__file__).resolve().parent.parent
IMG_DIR = ROOT / "assets" / "img"
CACHE = Path(__file__).resolve().parent / ".cache"

# ---------------------------------------------------------------- brand tokens
# These mirror :root and .display / .label in assets/css/style.css.
CREAM = (0xF5, 0xF2, 0xEF)
INK = "#1a120b"
DISPLAY_TRACKING = "-0.04em"
DISPLAY_LEADING = 0.98
LABEL_TRACKING = "0.18em"

# ------------------------------------------------------------------- geometry
WIDTH, HEIGHT = 1200, 630
MARGIN = 72
MARK_BOX = (72, 60, 106, 103)  # left, top, width, height
HEADLINE_TOP = 237  # cap top of the first headline line
HEADLINE_MAX_BOTTOM = 505  # headline ink has to clear the label
LABEL_TOP = 542  # cap top of the label
LABEL_SIZE = 25
HEADLINE_MAX_SIZE = 84
HEADLINE_MIN_SIZE = 40
TEXT_MAX_WIDTH = WIDTH - 2 * MARGIN

# ---------------------------------------------------------------------- pages
# Copy carries over from the images these replace. Lines are broken by hand
# rather than wrapped, so each one reads as a written line in a face that runs
# much wider than the serif it succeeds.
PAGES = [
    {
        "file": "og-default.png",
        "headline": ["Life is what", "happens while", "you're in the", "meantime."],
        "label": "Lager bar  //  3409 Cass Ave, Detroit",
    },
    {
        "file": "og-about.png",
        "headline": ["The meantime", "is the good part."],
        "label": "About  //  Meantime, Detroit",
    },
    {
        "file": "og-menu.png",
        "headline": ["What's", "pouring."],
        "label": "Live tap list  //  Meantime, Detroit",
    },
    {
        "file": "og-pals.png",
        "headline": ["Be a pal."],
        "label": "Pal membership  //  Meantime, Detroit",
    },
    {
        "file": "og-visit.png",
        "headline": ["3409 Cass Ave,", "Detroit."],
        "label": "Visit  //  Open six days",
    },
]

# ----------------------------------------------------------------------- fonts
FONT_CSS_URL = (
    "https://fonts.googleapis.com/css2?family=Unbounded:wght@900&family=Archivo:wght@700"
)
# A browser UA, so Google Fonts answers with woff2 split by subset.
UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "google-chrome",
    "chromium",
]


def find_chrome() -> str:
    for candidate in CHROME_CANDIDATES:
        path = candidate if Path(candidate).exists() else shutil.which(candidate)
        if path:
            return path
    sys.exit("Google Chrome not found; install it or put it on PATH.")


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def font_faces() -> str:
    """@font-face rules with the latin woff2 files inlined as data URIs.

    Inlined rather than linked so the render needs no network once the files are
    cached, and so Chrome can load them from a file:// page.
    """
    CACHE.mkdir(exist_ok=True)
    css_file = CACHE / "google-fonts.css"
    if not css_file.exists():
        css_file.write_bytes(fetch(FONT_CSS_URL))
    css = css_file.read_text()

    rules, families = [], set()
    for block in re.findall(r"@font-face\s*\{[^}]*\}", css):
        # Google ships a block per subset; the copy here is all latin.
        if "U+0000-00FF" not in block:
            continue
        family = re.search(r"font-family:\s*'([^']+)'", block).group(1)
        weight = re.search(r"font-weight:\s*(\d+)", block).group(1)
        url = re.search(r"url\((https://[^)]+\.woff2)\)", block).group(1)
        cached = CACHE / f"{family.lower()}-{weight}.woff2"
        if not cached.exists():
            cached.write_bytes(fetch(url))
        data = base64.b64encode(cached.read_bytes()).decode()
        families.add(family)
        rules.append(
            f"@font-face{{font-family:'{family}';font-style:normal;"
            f"font-weight:{weight};font-display:block;"
            f"src:url(data:font/woff2;base64,{data}) format('woff2');}}"
        )

    missing = {"Unbounded", "Archivo"} - families
    if missing:
        sys.exit(f"Google Fonts served no latin woff2 for: {', '.join(sorted(missing))}")
    return "".join(rules)


# ------------------------------------------------------------------- rendering
# The page starts on a red ground and only turns cream once the webfonts have
# loaded and the headline has been sized and placed. A render that fails part
# way through therefore comes back obviously wrong, and verify() stops the run
# rather than shipping type set in a fallback face.
PAGE = """<!doctype html>
<meta charset="utf-8">
<style>
{faces}
html, body {{ margin: 0; padding: 0; }}
body {{
  width: {width}px; height: {height}px; overflow: hidden;
  background: #ff0000; color: {ink};
  -webkit-font-smoothing: antialiased;
}}
#mark {{ position: absolute; left: {mark_left}px; top: {mark_top}px;
         width: {mark_width}px; height: {mark_height}px; }}
#headline {{
  position: absolute; left: {margin}px; top: {headline_top}px;
  font-family: Unbounded, sans-serif; font-weight: 900;
  letter-spacing: {display_tracking}; line-height: {display_leading};
  white-space: pre; margin: 0;
}}
#label {{
  position: absolute; left: {margin}px; top: {label_top}px;
  font-family: Archivo, sans-serif; font-weight: 700;
  font-size: {label_size}px; letter-spacing: {label_tracking};
  text-transform: uppercase; white-space: pre; margin: 0;
}}
</style>
{mark}
<h1 id="headline">{headline}</h1>
<p id="label">{label}</p>
<script>
const headline = document.getElementById('headline');
const lines = {lines};

// The largest size at which every line clears the side margins and the block
// clears the label. Deterministic, so the calibration pass and the final pass
// settle on the same number.
function fit() {{
  for (let size = {max_size}; size >= {min_size}; size--) {{
    headline.style.fontSize = size + 'px';
    let widest = 0;
    for (const line of lines) {{
      headline.textContent = line;
      widest = Math.max(widest, headline.getBoundingClientRect().width);
    }}
    headline.textContent = lines.join('\\n');
    if (widest <= {max_width} && lines.length * size * {display_leading} <= {max_height}) {{
      return size;
    }}
  }}
  return {min_size};
}}

// document.fonts.check() answers true for a family that was never declared,
// so ask the only question that cannot be faked: does the text measure the
// same as it does in the fallback it would drop to?
function loaded(family, weight) {{
  const probe = document.createElement('span');
  probe.textContent = 'meantime 3409 WHAT';
  probe.style.cssText = 'position:absolute;visibility:hidden;white-space:pre;'
    + 'font-size:80px;font-weight:' + weight;
  document.body.appendChild(probe);
  const widths = ['monospace', 'serif'].map(fallback => {{
    probe.style.fontFamily = fallback;
    const plain = probe.getBoundingClientRect().width;
    probe.style.fontFamily = family + ',' + fallback;
    return [plain, probe.getBoundingClientRect().width];
  }});
  probe.remove();
  return widths.every(([plain, styled]) => Math.abs(plain - styled) > 0.5);
}}

Promise.all([
  document.fonts.load('900 80px Unbounded'),
  document.fonts.load('700 {label_size}px Archivo'),
]).then(() => {{
  if (!loaded('Unbounded', 900) || !loaded('Archivo', 700)) {{
    return;  // leave the ground red: the run stops at verify()
  }}
  headline.style.fontSize = fit() + 'px';
  // Nudge both blocks so measured ink, not the line box, lands on the grid.
  headline.style.top = ({headline_top} + {headline_nudge}) + 'px';
  document.getElementById('label').style.top = ({label_top} + {label_nudge}) + 'px';
  document.body.style.background = '{cream}';
}});
</script>
"""


def build_html(page: dict, faces: str, mark: str, nudges: tuple[int, int]) -> str:
    headline_nudge, label_nudge = nudges
    return PAGE.format(
        faces=faces,
        mark=mark,
        headline="\n".join(page["headline"]),
        label=page["label"],
        lines=json.dumps(page["headline"]),
        width=WIDTH,
        height=HEIGHT,
        margin=MARGIN,
        cream="#%02x%02x%02x" % CREAM,
        ink=INK,
        mark_left=MARK_BOX[0],
        mark_top=MARK_BOX[1],
        mark_width=MARK_BOX[2],
        mark_height=MARK_BOX[3],
        headline_top=HEADLINE_TOP,
        headline_nudge=headline_nudge,
        label_top=LABEL_TOP,
        label_nudge=label_nudge,
        label_size=LABEL_SIZE,
        display_tracking=DISPLAY_TRACKING,
        display_leading=DISPLAY_LEADING,
        label_tracking=LABEL_TRACKING,
        max_size=HEADLINE_MAX_SIZE,
        min_size=HEADLINE_MIN_SIZE,
        max_width=TEXT_MAX_WIDTH,
        max_height=HEADLINE_MAX_BOTTOM - HEADLINE_TOP,
    )


def screenshot(chrome: str, html: str, out_png: Path, timeout: float = 60) -> None:
    """Shoot the page at exactly 1200x630.

    Chrome writes the file and then sits there rather than exiting, so wait for
    the PNG to stop growing and close it down.
    """
    if out_png.exists():
        out_png.unlink()
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "page.html"
        page.write_text(html)
        process = subprocess.Popen(
            [
                chrome,
                "--headless=new",
                f"--user-data-dir={Path(tmp) / 'profile'}",
                "--no-first-run",
                "--no-default-browser-check",
                "--disable-gpu",
                "--disable-background-networking",
                "--disable-component-update",
                "--hide-scrollbars",
                "--force-device-scale-factor=1",
                f"--window-size={WIDTH},{HEIGHT}",
                "--virtual-time-budget=5000",
                f"--screenshot={out_png}",
                page.as_uri(),
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        try:
            deadline, size = time.time() + timeout, -1
            while time.time() < deadline:
                if out_png.exists():
                    current = out_png.stat().st_size
                    if current and current == size:
                        return
                    size = current
                if process.poll() is not None and out_png.exists():
                    return
                time.sleep(0.15)
            sys.exit(f"{out_png.name}: Chrome produced no screenshot within {timeout:.0f}s.")
        finally:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()


# ----------------------------------------------------------------- measurement
def ink_bands(png: Path) -> list[dict]:
    """Bands of rows carrying ink or mark color, with each band's extents."""
    image = Image.open(png).convert("RGB")
    if image.size != (WIDTH, HEIGHT):
        sys.exit(f"{png.name}: rendered {image.size}, expected {(WIDTH, HEIGHT)}.")
    if image.getpixel((2, 2)) != CREAM:
        sys.exit(
            f"{png.name}: the ground is {image.getpixel((2, 2))}, not cream - the page "
            "never finished, most likely because Unbounded or Archivo did not load."
        )

    ground = Image.new("RGB", image.size, CREAM)
    mask = ImageChops.difference(image, ground).convert("L").point(
        lambda value: 255 if value > 12 else 0
    )

    rows = []
    for y in range(HEIGHT):
        box = mask.crop((0, y, WIDTH, y + 1)).getbbox()
        rows.append((box[0], box[2] - 1) if box else None)

    bands, start = [], None
    for y, row in enumerate(rows + [None]):
        if row and start is None:
            start = y
        elif not row and start is not None:
            extents = [r for r in rows[start:y] if r]
            bands.append(
                {
                    "top": start,
                    "bottom": y - 1,
                    "left": min(e[0] for e in extents),
                    "right": max(e[1] for e in extents),
                }
            )
            start = None
    return bands


def verify(png: Path, bands: list[dict]) -> None:
    """The mark, the headline and the label all have to sit on the grid."""
    if len(bands) < 3:
        sys.exit(f"{png.name}: wanted a mark, a headline and a label, found {len(bands)} bands.")

    mark, *rest = bands
    headline, label = rest[:-1], rest[-1]
    left, top, width, height = MARK_BOX
    drawn = (mark["right"] - mark["left"] + 1, mark["bottom"] - mark["top"] + 1)

    problems = []
    if abs(mark["left"] - left) > 1 or abs(mark["top"] - top) > 1:
        problems.append(f"mark starts at {mark['left']},{mark['top']} not {left},{top}")
    if abs(drawn[0] - width) > 2 or abs(drawn[1] - height) > 2:
        problems.append(f"mark measures {drawn[0]}x{drawn[1]} not {width}x{height}")
    if abs(headline[0]["top"] - HEADLINE_TOP) > 1:
        problems.append(f"headline cap top at {headline[0]['top']} not {HEADLINE_TOP}")
    if headline[-1]["bottom"] > HEADLINE_MAX_BOTTOM:
        problems.append(f"headline runs to {headline[-1]['bottom']}, past {HEADLINE_MAX_BOTTOM}")
    if abs(label["top"] - LABEL_TOP) > 1:
        problems.append(f"label cap top at {label['top']} not {LABEL_TOP}")
    for band in headline + [label]:
        if band["left"] < MARGIN - 4 or band["right"] > WIDTH - MARGIN:
            problems.append(f"a line runs {band['left']}-{band['right']}, outside the margins")
            break
    if problems:
        sys.exit(f"{png.name}: " + "; ".join(problems))


def main() -> None:
    parser = argparse.ArgumentParser(description="Rebuild the og:image set.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="render and verify without writing to assets/img/",
    )
    args = parser.parse_args()

    chrome = find_chrome()
    faces = font_faces()
    mark = (IMG_DIR / "mark.svg").read_text().strip().replace("<svg ", '<svg id="mark" ', 1)

    with tempfile.TemporaryDirectory() as tmp:
        for page in PAGES:
            work = Path(tmp) / page["file"]

            # Pass one places the blocks by line box. Ink sits a little inside
            # that box, by an amount that depends on the face and the size the
            # fit lands on, so measure the miss.
            screenshot(chrome, build_html(page, faces, mark, (0, 0)), work)
            bands = ink_bands(work)
            if len(bands) < 3:
                sys.exit(f"{page['file']}: nothing rendered to measure.")
            nudges = (HEADLINE_TOP - bands[1]["top"], LABEL_TOP - bands[-1]["top"])

            # Pass two applies the correction, and is the image we keep.
            screenshot(chrome, build_html(page, faces, mark, nudges), work)
            bands = ink_bands(work)
            verify(work, bands)

            if not args.check:
                shutil.copyfile(work, IMG_DIR / page["file"])
            headline = bands[1:-1]
            print(
                f"{page['file']}: {len(page['headline'])} lines, cap height "
                f"{headline[0]['bottom'] - headline[0]['top'] + 1}px, ink to "
                f"{headline[-1]['bottom']}" + (" (check only)" if args.check else "")
            )


if __name__ == "__main__":
    main()
