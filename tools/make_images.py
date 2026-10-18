"""Make the web-ready images the site publishes from the originals in references/.

Run from the repo root:  python3 tools/make_images.py
Needs Pillow (pip install pillow). Re-running overwrites the outputs in assets/img/.
To add a game's art, add entries to JOBS below and run it again.
"""
from pathlib import Path

from PIL import Image, ImageEnhance, ImageOps

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / "references"
OUT = ROOT / "assets" / "img"

# name -> source, optional crop box (in source pixels), widths to export.
# Each width is written as <name>-<width>.webp and <name>-<width>.jpg.
JOBS = {
    "bumperblock/keyart": dict(src="keyart_stadium.jpg", widths=[640, 1280, 1920]),
    "bumperblock/driver-rabbit": dict(src="keyart_stadium.jpg", crop=(290, 740, 830, 1280), widths=[360]),
    "bumperblock/driver-raccoon": dict(src="keyart_stadium.jpg", crop=(870, 840, 1440, 1410), widths=[360]),
    "bumperblock/driver-cat": dict(src="keyart_stadium.jpg", crop=(1440, 830, 1970, 1360), widths=[360]),
    "bumperblock/driver-dog": dict(src="keyart_stadium.jpg", crop=(2010, 850, 2600, 1440), widths=[360]),
}

# The app icon is the two mountains and the wave from the logo, without the text.
FAVICON_CROP = (290, 230, 1730, 1250)


def export(name, src, widths, crop=None):
    img = Image.open(REF / src).convert("RGB")
    if crop:
        img = img.crop(crop)
    dest = OUT / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    for w in widths:
        w = min(w, img.width)
        h = round(img.height * w / img.width)
        small = img.resize((w, h), Image.LANCZOS)
        small.save(f"{dest}-{w}.webp", quality=82, method=6)
        small.save(f"{dest}-{w}.jpg", quality=84, optimize=True, progressive=True)


def ink_logo(widths):
    """The full logo as black ink on a transparent background, so it sits on any page color."""
    gray = Image.open(REF / "logo.jpg").convert("L")
    alpha = ImageOps.invert(gray).point(lambda v: 0 if v < 28 else min(255, int((v - 28) * 1.25)))
    dest = OUT / "mountain-wave" / "logo-ink"
    dest.parent.mkdir(parents=True, exist_ok=True)
    for w in widths:
        h = round(gray.height * w / gray.width)
        img = Image.new("RGBA", (w, h), (26, 23, 20, 0))
        img.putalpha(alpha.resize((w, h), Image.LANCZOS))
        img.save(f"{dest}-{w}.webp", quality=85, method=6)
        img.save(f"{dest}-{w}.png", optimize=True)


def favicons():
    """apple-touch-icon.png from the logo, and favicon.ico from favicon-32.png.

    favicon.svg is drawn by hand (the logo's detail turns to mush at tab size) and
    favicon-32.png is a 32px render of it; re-render that if you change the SVG.
    """
    mark = Image.open(REF / "logo.jpg").convert("L").crop(FAVICON_CROP)
    # Paper to transparent, ink to opaque.
    ink = ImageOps.invert(ImageEnhance.Contrast(mark).enhance(2.2))
    ink = ink.point(lambda v: 0 if v < 40 else min(255, int(v * 1.4)))
    side = max(ink.size)
    square = Image.new("L", (side, side), 0)
    square.paste(ink, ((side - ink.width) // 2, (side - ink.height) // 2))
    # iOS shows transparency as black, so put the mark on the logo's paper color.
    size, pad = 180, 18
    icon = Image.new("RGB", (size, size), (252, 247, 234))
    icon.paste((20, 18, 16), (pad, pad), square.resize((size - 2 * pad, size - 2 * pad), Image.LANCZOS))
    icon.save(ROOT / "apple-touch-icon.png", optimize=True)
    Image.open(ROOT / "favicon-32.png").save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32)])


if __name__ == "__main__":
    for name, job in JOBS.items():
        export(name, **job)
    ink_logo([480, 960])
    favicons()
    print("done")
