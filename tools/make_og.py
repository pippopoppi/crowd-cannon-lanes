#!/usr/bin/env python3
"""Render og.png (1200x630 Twitter/OpenGraph card) and icon-180.png with Pillow."""
import math
import os
import random

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
random.seed(7)


def font(size, bold=True):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
    ]
    for c in candidates:
        if os.path.exists(c):
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()


def soldier(d, x, y, r, body, light, dark="#1e3a8a", facing_right=True):
    """Tiny soldier seen from the side, marching to the right (blue) or left (red)."""
    f = 1 if facing_right else -1
    d.rectangle((x - r * 0.7, y + r * 0.5, x - r * 0.2, y + r * 1.4), fill=dark)
    d.rectangle((x + r * 0.2, y + r * 0.5, x + r * 0.7, y + r * 1.4), fill=dark)
    d.rounded_rectangle((x - r, y - r * 0.45, x + r, y + r * 1.0), int(r * 0.45), fill=body)
    gx0, gx1 = sorted((x + f * r * 0.75, x + f * r * 1.9))
    d.rectangle((gx0, y - r * 0.2, gx1, y + r * 0.1), fill="#1f2937")
    d.ellipse((x - r * 0.7, y - r * 1.75, x + r * 0.7, y - r * 0.35), fill="#fcd9b6")
    d.pieslice((x - r * 0.78, y - r * 1.9, x + r * 0.78, y - r * 0.35), 180, 360, fill=dark)
    ex = x + f * r * 0.28
    d.ellipse((ex - r * 0.12, y - r * 1.05, ex + r * 0.12, y - r * 0.8), fill="#111827")


def card():
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), "#72b96c")
    d = ImageDraw.Draw(img, "RGBA")
    for y in range(0, H, 80):
        d.rectangle((0, y, W, y + 40), fill=(255, 255, 255, 14))
    # red zone (right) and blue zone (left): battlefield rotated to landscape
    d.rectangle((W - 200, 0, W, H), fill=(190, 24, 60, 56))
    d.rectangle((0, 0, 190, H), fill=(37, 99, 235, 46))

    # gates (vertical in landscape)
    gates = [(430, 110, 120, "×2", (59, 130, 246)), (430, 300, 120, "×3", (34, 197, 94)), (690, 200, 200, "×4", (168, 85, 247))]
    for gx, gy, gh, label, col in gates:
        d.rounded_rectangle((gx, gy, gx + 34, gy + gh), 8, fill=col + (110,), outline=col + (255,), width=4)
        d.rectangle((gx - 5, gy - 6, gx + 39, gy), fill="#f8fafc")
        d.rectangle((gx - 5, gy + gh, gx + 39, gy + gh + 6), fill="#f8fafc")
    d.rounded_rectangle((430, 236, 464, 294), 6, fill="#e2e8f0")
    d.rounded_rectangle((430, 265, 464, 294), 6, fill="#cbd5e1")

    # army: thin stream left, thick crowd right
    for i in range(60):
        x = 230 + random.random() * 190
        y = 300 + (random.random() - 0.5) * 60
        soldier(d, x, y, 9, "#3b82f6", "#bfdbfe")
    for i in range(380):
        x = 480 + random.random() * 480
        spread = 60 + (x - 480) * 0.55
        y = 315 + (random.random() - 0.5) * spread
        soldier(d, x, y, 9, "#3b82f6", "#bfdbfe")
    for i in range(90):
        x = 930 + random.random() * 240
        y = 60 + random.random() * 510
        soldier(d, x, y, 9, "#ef4444", "#fca5a5", dark="#7f1d1d", facing_right=False)

    for gx, gy, gh, label, col in gates:
        f = font(34)
        tw = d.textlength(label, font=f)
        d.rounded_rectangle((gx + 17 - tw / 2 - 6, gy + gh / 2 - 22, gx + 17 + tw / 2 + 6, gy + gh / 2 + 22), 10, fill=col + (230,))
        d.text((gx + 17 - tw / 2, gy + gh / 2 - 22), label, font=f, fill="white")

    # base
    bx, by = 1060, 240
    d.rounded_rectangle((bx, by + 10, bx + 110, by + 90), 10, fill="#7f1d1d")
    d.rounded_rectangle((bx, by, bx + 110, by + 80), 10, fill="#dc2626")
    for x in range(bx + 6, bx + 104, 22):
        d.rectangle((x, by - 12, x + 14, by + 4), fill="#b91c1c")
    d.rounded_rectangle((bx + 40, by + 28, bx + 70, by + 80), 6, fill="#fecaca")
    d.rounded_rectangle((bx + 46, by + 40, bx + 64, by + 80), 4, fill="#1f2937")

    # cannon on the left, pointing right
    cx, cy = 150, 310
    d.ellipse((cx - 30, cy - 36, cx + 30, cy + 36), fill="#1e40af")
    d.ellipse((cx - 22, cy - 26, cx + 22, cy + 26), fill="#3b82f6")
    d.rounded_rectangle((cx, cy - 16, cx + 70, cy + 16), 8, fill="#334155")
    d.rounded_rectangle((cx + 60, cy - 12, cx + 74, cy + 12), 5, fill="#0f172a")

    # title banner
    banner = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    bd = ImageDraw.Draw(banner)
    bd.rounded_rectangle((40, 440, 760, 590), 26, fill=(8, 12, 30, 215))
    img.paste(banner, (0, 0), banner)
    d = ImageDraw.Draw(img, "RGBA")
    d.text((70, 455), "CROWD CANNON: LANES", font=font(60), fill="#93c5fd")
    d.text((72, 540), "Fight the lane. Grab the cards. Crack the crates.", font=font(26, bold=False), fill="#e2e8f0")

    img.save(os.path.join(ROOT, "og.png"), optimize=True)
    print("wrote og.png")


def icon():
    S = 180
    img = Image.new("RGB", (S, S), "#0f172a")
    d = ImageDraw.Draw(img, "RGBA")
    d.rounded_rectangle((22, 56, 158, 84), 8, fill=(34, 197, 94, 220))
    f = font(24)
    d.text((90 - d.textlength("×3", font=f) / 2, 56), "×3", font=f, fill="white")
    for x, y in [(56, 34), (78, 28), (102, 34), (124, 28), (66, 108), (114, 108)]:
        soldier(d, x, y, 9, "#3b82f6", "#bfdbfe")
    d.pieslice((62, 120, 118, 176), 180, 360, fill="#1e40af")
    d.rounded_rectangle((80, 104, 100, 146), 5, fill="#334155")
    img.save(os.path.join(ROOT, "icon-180.png"), optimize=True)
    print("wrote icon-180.png")


if __name__ == "__main__":
    card()
    icon()
