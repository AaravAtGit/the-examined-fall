# makes the emote pngs + placeholder silhouettes
# run from project root: python3 tools/make_ui_assets.py
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent / "game"
UI = ROOT / "ui"
EMOTES = UI / "emotes"
PLACEHOLDER = UI / "placeholder"
PFP = ROOT / "pfp"
for d in (UI, EMOTES, PLACEHOLDER, PFP):
    d.mkdir(parents=True, exist_ok=True)

SS = 4  # supersampling factor for smooth edges
FONT = "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf"
INK = (30, 30, 40, 255)


def down(img, size):
    return img.resize(size, Image.LANCZOS)


def dilate(mask, px):
    # grow mask by ~px (blur + threshold)
    return mask.filter(ImageFilter.GaussianBlur(px / 2)).point(lambda v: 255 if v > 8 else 0)


def outlined(mask, fill, outline=INK, thickness=36):
    w, h = mask.size
    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    out.paste(Image.new("RGBA", (w, h), outline), (0, 0), dilate(mask, thickness))
    out.paste(Image.new("RGBA", (w, h), fill), (0, 0), mask)
    return out


def new_mask(n=800):
    m = Image.new("L", (n, n), 0)
    return m, ImageDraw.Draw(m)


def text_mask(ch, size=640, n=800):
    m, d = new_mask(n)
    font = ImageFont.truetype(FONT, size)
    d.text((n / 2, n / 2), ch, font=font, fill=255, anchor="mm")
    return m


def save_emote(img, name):
    down(img, (200, 200)).save(EMOTES / f"{name}.png")


# Emotes
# Sweat drop
m, d = new_mask()
d.ellipse((230, 360, 570, 700), fill=255)
d.polygon([(400, 90), (240, 470), (560, 470)], fill=255)
img = outlined(m, (120, 200, 255, 255))
ImageDraw.Draw(img).ellipse((300, 450, 370, 560), fill=(255, 255, 255, 230))
save_emote(img, "sweat")

# Exclamation / question
save_emote(outlined(text_mask("!"), (255, 80, 80, 255), thickness=44), "exclaim")
save_emote(outlined(text_mask("?"), (255, 215, 80, 255), thickness=44), "question")

# Anger vein
m, d = new_mask()
r, off, wdt = 190, 195, 95
for (cx, cy, a0, a1) in [
    (400 - off, 400 - off, 0, 90),
    (400 + off, 400 - off, 90, 180),
    (400 - off, 400 + off, 270, 360),
    (400 + off, 400 + off, 180, 270),
]:
    d.arc((cx - r, cy - r, cx + r, cy + r), a0, a1, fill=255, width=wdt)
save_emote(outlined(m, (240, 50, 60, 255), thickness=28), "anger")


# Sparkles
def star(d, cx, cy, R, r):
    pts = []
    for i in range(8):
        rad = R if i % 2 == 0 else r
        import math
        ang = math.pi / 4 * i - math.pi / 2
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    d.polygon(pts, fill=255)


m, d = new_mask()
star(d, 360, 420, 300, 70)
star(d, 640, 180, 130, 32)
star(d, 640, 650, 95, 24)
save_emote(outlined(m, (255, 230, 100, 255), thickness=30), "sparkle")

# Rain cloud
m, d = new_mask()
for box in [(120, 230, 400, 510), (300, 140, 620, 460), (480, 260, 720, 500), (160, 330, 680, 520)]:
    d.ellipse(box, fill=255)
img = outlined(m, (150, 160, 180, 255))
drops, dd = new_mask()
for x in (240, 400, 560):
    dd.ellipse((x - 35, 620, x + 35, 700), fill=255)
    dd.polygon([(x, 550), (x - 33, 650), (x + 33, 650)], fill=255)
img.alpha_composite(outlined(drops, (100, 170, 255, 255), thickness=24))
save_emote(img, "cloud")

# Light bulb (idea / scheming)
m, d = new_mask()
d.ellipse((220, 130, 580, 490), fill=255)
d.rectangle((310, 440, 490, 600), fill=255)
img = outlined(m, (255, 225, 90, 255))
base, bd = new_mask()
bd.rounded_rectangle((300, 560, 500, 690), 30, fill=255)
img.alpha_composite(outlined(base, (170, 170, 185, 255), thickness=24))
rays = Image.new("RGBA", (800, 800), (0, 0, 0, 0))
rd = ImageDraw.Draw(rays)
for (x0, y0, x1, y1) in [(400, 20, 400, 90), (130, 130, 180, 180), (670, 130, 620, 180), (60, 330, 130, 330), (740, 330, 670, 330)]:
    rd.line((x0, y0, x1, y1), fill=INK, width=34)
img.alpha_composite(rays)
save_emote(img, "bulb")

# "..." speech bubble
m, d = new_mask()
d.rounded_rectangle((90, 200, 710, 560), 160, fill=255)
d.polygon([(220, 520), (160, 690), (360, 540)], fill=255)
img = outlined(m, (255, 255, 255, 255))
dots = ImageDraw.Draw(img)
for x in (260, 400, 540):
    dots.ellipse((x - 45, 335, x + 45, 425), fill=INK)
save_emote(img, "dots")

# Silhouette helper (transparent cutout: head + shoulders)
def silhouette(color, letter=None, size=600):
    N = size * SS
    img = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.ellipse((N * .32, N * .06, N * .68, N * .42), fill=color)
    d.rectangle((N * .44, N * .36, N * .56, N * .5), fill=color)  # neck          # head
    d.rounded_rectangle((N * .14, N * .46, N * .86, N * 1.3), N * .25, fill=color)  # shoulders
    if letter:
        font = ImageFont.truetype(FONT, int(N * .28))
        d.text((N * .5, N * .6), letter, font=font, fill="white", anchor="mm")
    return down(img, (size, size))


# Placeholder pfps (used until you add a real one)
COLORS = {
    "aarav": (245, 185, 66),
    "oreek": (111, 195, 255),
    "shrey": (155, 227, 122),
    "dsp": (255, 122, 122),
    "theguy": (60, 60, 70),
    "jassi": (255, 179, 217),
    "edvance": (201, 167, 255),
    "shwetank": (126, 224, 208),
    "descartes": (200, 180, 120),
    "diogenes": (190, 150, 100),
    "schopenhauer": (130, 140, 170),
    "camus": (230, 140, 100),
    "kierkegaard": (150, 175, 120),
}
for name, col in COLORS.items():
    silhouette(col + (255,), name[0].upper()).save(PLACEHOLDER / f"{name}.png")

print("UI assets written to", UI)
