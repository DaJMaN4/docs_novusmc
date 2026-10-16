"""Media slots for the docs.

python tools/media.py   (from the repo root)

- inserts a <figure> for every slot in tools/media_plan.py under its heading (once; existing figures are kept),
- creates a labelled placeholder in .gitbook/assets/ for every slot whose file does not exist yet,
- writes tools/MEDIA.md: checklist of all slots, placeholders vs real images.

Replace a placeholder by saving the real screenshot / GIF under the same file name, then run the script again.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont, PngImagePlugin

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, ".gitbook", "assets")
MARK = "novusmc-placeholder"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from media_plan import PLAN  # noqa: E402

FONT = "C:/Windows/Fonts/arialbd.ttf"
FONT_REG = "C:/Windows/Fonts/arial.ttf"


def font(size, bold=False):
    try:
        return ImageFont.truetype(FONT if bold else FONT_REG, size)
    except OSError:
        return ImageFont.load_default()


def wrap(draw, text, fnt, width):
    lines, line = [], ""
    for word in text.split():
        test = (line + " " + word).strip()
        if draw.textlength(test, font=fnt) <= width:
            line = test
        else:
            lines.append(line)
            line = word
    lines.append(line)
    return lines


def frame(size, kind, caption, capture, name, phase):
    w, h = size
    img = Image.new("RGB", size, (30, 32, 40))
    d = ImageDraw.Draw(img)
    # stripes so the placeholder is obvious
    for x in range(-h, w, 40):
        d.line([(x + phase * 20, 0), (x + h + phase * 20, h)], fill=(38, 41, 52), width=14)
    accent = (255, 170, 0) if kind == "gif" else (85, 200, 255)
    d.rectangle([8, 8, w - 9, h - 9], outline=accent, width=4)
    s = w / 1280
    label = ("GIF — DO NAGRANIA" if kind == "gif" else "ZRZUT EKRANU — DO ZROBIENIA")
    d.text((w / 2, h * 0.2), label, font=font(int(44 * s), True), fill=accent, anchor="mm")
    y = h * 0.38
    for ln in wrap(d, caption, font(int(56 * s), True), w * 0.85):
        d.text((w / 2, y), ln, font=font(int(56 * s), True), fill=(240, 240, 240), anchor="mm")
        y += 66 * s
    y += 10 * s
    for ln in wrap(d, capture, font(int(30 * s)), w * 0.8):
        d.text((w / 2, y), ln, font=font(int(30 * s)), fill=(180, 184, 196), anchor="mm")
        y += 38 * s
    d.text((w / 2, h - 40 * s), name, font=font(int(24 * s)), fill=(120, 124, 140), anchor="mm")
    return img


def make_placeholder(path, caption, capture, name):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if path.endswith(".gif"):
        frames = [frame((800, 450), "gif", caption, capture, name, p).convert("P", palette=Image.ADAPTIVE, colors=32)
                  for p in (0, 1)]
        frames[0].save(path, save_all=True, append_images=frames[1:], duration=600, loop=0, comment=MARK.encode())
    else:
        info = PngImagePlugin.PngInfo()
        info.add_text(MARK, "1")
        frame((1280, 720), "png", caption, capture, name, 0).quantize(64).save(path, pnginfo=info, optimize=True)


def is_placeholder(path):
    try:
        with Image.open(path) as im:
            return MARK in getattr(im, "text", {}) or im.info.get("comment") == MARK.encode()
    except OSError:
        return False


def figure(src, caption):
    return f'<figure><img src="{src}" alt="{caption}"><figcaption><p>{caption}</p></figcaption></figure>'


def main():
    rows = []
    for page, headings in PLAN.items():
        path = os.path.join(ROOT, page)
        with open(path, encoding="utf8") as f:
            lines = f.read().split("\n")
        changed = False
        for heading, slots in headings.items():
            try:
                idx = next(i for i, ln in enumerate(lines) if ln.strip() == heading)
            except StopIteration:
                print(f"! {page}: heading not found: {heading}")
                continue
            new = []
            for file, caption, capture in slots:
                asset = os.path.join(ASSETS, file)
                src = os.path.relpath(asset, os.path.dirname(path)).replace(os.sep, "/")
                if not os.path.exists(asset):
                    make_placeholder(asset, caption, capture, file)
                rows.append((page, heading, file, caption, capture, is_placeholder(asset)))
                if not any(src in ln for ln in lines):
                    new += [figure(src, caption), ""]
            if new:
                lines[idx + 1:idx + 1] = [""] + new[:-1] if lines[idx + 1].strip() == "" else [""] + new
                changed = True
        if changed:
            with open(path, "w", encoding="utf8", newline="\n") as f:
                f.write("\n".join(lines))

    todo = sum(1 for r in rows if r[5])
    out = [
        "# Zdjęcia i GIF-y do dokumentacji",
        "",
        f"Gotowe: **{len(rows) - todo} / {len(rows)}** (PNG: {sum(1 for r in rows if r[2].endswith('.png'))}, "
        f"GIF: {sum(1 for r in rows if r[2].endswith('.gif'))}).",
        "",
        "Każde miejsce na obrazek ma już plik-zaślepkę w `.gitbook/assets/`. Aby dodać prawdziwy obrazek, "
        "zapisz go **pod tą samą nazwą** (nadpisz zaślepkę) i uruchom `python tools/media.py`, żeby odświeżyć tę listę.",
        "",
        "* **Zrzuty ekranu (.png):** 1280×720 lub większe, bez interfejsu czatu (F1 ukrywa HUD, gdy niepotrzebny).",
        "* **GIF-y (.gif):** 3–8 s, szerokość ok. 800 px, do ~10 MB.",
        "* Nowe miejsca dodajesz w `tools/media_plan.py` (strona → nagłówek → plik, podpis, co nagrać).",
        "",
    ]
    last = None
    for page, heading, file, caption, capture, ph in rows:
        if page != last:
            out += ["", f"## {page}", "", "| | Plik | Podpis | Co pokazać |", "| --- | --- | --- | --- |"]
            last = page
        out.append(f"| {'⬜' if ph else '✅'} | `{file}` | {caption} | {capture} |")
    with open(os.path.join(ROOT, "tools", "MEDIA.md"), "w", encoding="utf8", newline="\n") as f:
        f.write("\n".join(out) + "\n")
    print(f"{len(rows)} slots, {todo} placeholders")


if __name__ == "__main__":
    main()
