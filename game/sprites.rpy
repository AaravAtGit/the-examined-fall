# sprites
# one image per person in game/pfp/ (name.png / .jpg / .webp)
# every expression gets built from that one image + an emote + a little motion
# usage: show oreek nervous / o shocked "..."
# new character -> add to CAST, new expression -> add to EXPRESSIONS

init -1 python:

    CAST = ["aarav", "oreek", "dsp", "shrey", "theguy", "jassi", "edvance",
            "shwetank", "descartes", "diogenes", "schopenhauer", "camus", "kierkegaard"]

    # Horizontal squash per character (1.0 = untouched, 0.85 = 15% slimmer).
    SLIM = {
        "aarav": 0.85,
    }

    # Size multiplier per character (1.0 = normal, 1.25 = 25% bigger).
    SIZE = {
        "kierkegaard": 1.25,
    }

    # Characters whose image is mirrored left-to-right.
    FLIP = {"aarav"}

    # Sprites are scaled to fit inside this box (keeps aspect ratio).
    SPRITE_MAX_W = 760
    SPRITE_MAX_H = 760

    # expression: (emote, colour tint, motion)
    EXPRESSIONS = {
        "neutral":    (None,       None,     "idle"),
        "happy":      ("sparkle",  None,     "bounce"),
        "shocked":    ("exclaim",  None,     "shake"),
        "sad":        ("cloud",    "sad",    "sink"),
        "scheming":   ("bulb",     "scheme", "lean"),
        "sheepish":   ("sweat",    None,     "shrink"),
        "suspicious": ("dots",     None,     "lean"),
        "nervous":    ("sweat",    None,     "jitter"),
        "angry":      ("anger",    "angry",  "shake"),
        "confused":   ("question", None,     "sway"),
    }

    TINTS = {
        "sad":    SaturationMatrix(0.35) * TintMatrix("#c4ceff"),
        "scheme": TintMatrix("#e2d2ff"),
        "angry":  TintMatrix("#ffbdbd"),
    }

    PFP_EXTS = (".png", ".jpg", ".jpeg", ".webp")

    def find_pfp(name):
        for ext in PFP_EXTS:
            path = "pfp/" + name + ext
            if renpy.loadable(path):
                return path
        return "ui/placeholder/" + name + ".png"

    # Tall images (full-body) get cropped to the upper body so they match busts.
    MAX_ASPECT = 1.6      # max height / width before cropping
    HEAD_ZONE = 0.22      # top fraction of the visible character treated as the head

    def main_blob_edges(path, flip=False):
        # finds the biggest solid blob (the character, skips stars etc)
        # returns {row_y: rightmost_x}
        import pygame_sdl2
        with renpy.open_file(path) as f:
            surf = pygame_sdl2.image.load(f, path)
        w, h = surf.get_size()
        step = max(1, min(w, h) // 160)
        gw, gh = w // step, h // step

        solid = [[surf.get_at((gx * step, gy * step))[3] > 100 for gx in range(gw)]
                 for gy in range(gh)]

        seen = [[False] * gw for _ in range(gh)]
        best = []
        for sy in range(gh):
            for sx in range(gw):
                if not solid[sy][sx] or seen[sy][sx]:
                    continue
                blob, stack = [], [(sx, sy)]
                seen[sy][sx] = True
                while stack:
                    cx, cy = stack.pop()
                    blob.append((cx, cy))
                    for nx, ny in ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)):
                        if 0 <= nx < gw and 0 <= ny < gh and solid[ny][nx] and not seen[ny][nx]:
                            seen[ny][nx] = True
                            stack.append((nx, ny))
                if len(blob) > len(best):
                    best = blob

        edges = {}
        for gx, gy in best:
            y, x = gy * step, gx * step
            if flip:
                x = w - 1 - x  # mirror, so "right-most" is measured on the flipped image
            if x > edges.get(y, -1):
                edges[y] = x
        return edges


init 1 python:

    MOTIONS = {
        "idle": m_idle,
        "bounce": m_bounce,
        "shake": m_shake,
        "sink": m_sink,
        "lean": m_lean,
        "shrink": m_shrink,
        "jitter": m_jitter,
        "sway": m_sway,
    }

    def build_sprites(name):
        path = find_pfp(name)
        w, h = cached_size(path)
        flip = name in FLIP
        raw = cached("edges|%s|%s" % (path, flip), path,
                     lambda: {str(k): v for k, v in main_blob_edges(path, flip).items()})
        edges = {int(k): v for k, v in raw.items()} or {0: w}
        top, bottom = min(edges), max(edges)

        # Crop full-body images to the upper body.
        crop_y, crop_h = 0, h
        if h > w * MAX_ASPECT:
            crop_y = max(0, top - int(0.03 * h))
            crop_h = min(h - crop_y, int(w * MAX_ASPECT))
        # Trim empty space below the character, so feet/body sit on the screen edge.
        crop_h = min(crop_h, bottom + 4 - crop_y)
        visible_bottom = min(bottom, crop_y + crop_h)

        # Emote goes at the top-right of the head.
        head_limit = top + HEAD_ZONE * (visible_bottom - top)
        ex = max(x for y, x in edges.items() if y <= head_limit)
        ey = top + 0.08 * (visible_bottom - top) - crop_y

        scale = min(float(SPRITE_MAX_W) / w, float(SPRITE_MAX_H) / crop_h) * SIZE.get(name, 1.0)
        slim = SLIM.get(name, 1.0)
        size = (int(w * scale * slim), int(crop_h * scale))
        body = Transform(path, crop=(0, crop_y, w, crop_h), zoom=scale, xzoom=-slim if flip else slim)

        for expr, (emote, tint, motion) in EXPRESSIONS.items():
            layers = [body if tint is None else Transform(body, matrixcolor=TINTS[tint])]
            if emote:
                layers.append(At("ui/emotes/" + emote + ".png",
                                 emote_pop(int(ex * scale * slim) + 20, int(ey * scale))))
            sprite = Fixed(*layers, xysize=size)
            renpy.image((name, expr), At(sprite, MOTIONS[motion]))

    for _name in CAST:
        build_sprites(_name)


# Motions (played once each time the expression changes)
transform m_idle:
    xoffset 0

transform m_bounce:
    yoffset 0
    easein .12 yoffset -45
    easeout .14 yoffset 0
    easein .10 yoffset -20
    easeout .12 yoffset 0

transform m_shake:
    easein .08 zoom 1.04
    block:
        linear .04 xoffset -14
        linear .04 xoffset 14
        repeat 4
    linear .04 xoffset 0

transform m_sink:
    ease .7 yoffset 30 zoom .96

transform m_lean:
    ease .4 xoffset -25

transform m_shrink:
    ease .3 zoom .92

transform m_jitter:
    block:
        linear .05 xoffset -4
        linear .05 xoffset 4
        linear .05 xoffset 0
        pause 1.2
        repeat

transform m_sway:
    ease .25 xoffset 14
    ease .25 xoffset -8
    ease .2 xoffset 0

# Emote pops in at (x, y) inside the sprite, then bobs gently.
transform emote_pop(x, y):
    pos (x, y) anchor (.5, .5)
    zoom 0.0 alpha 0.0
    easein .18 zoom 1.2 alpha 1.0
    easeout .10 zoom 1.0
    block:
        ease 1.0 yoffset -6
        ease 1.0 yoffset 0
        repeat


# Screen positions (feet on the bottom edge, behind the textbox)
transform pos_left:
    xpos .25 xanchor .5 ypos 1.0 yanchor 1.0

transform pos_mid:
    xpos .5 xanchor .5 ypos 1.0 yanchor 1.0

transform pos_right:
    xpos .75 xanchor .5 ypos 1.0 yanchor 1.0
