# the chart at the end
# x = let go <-> push through, y = heart <-> head
# you land on the average of what you took, the planet choice nudges it a bit

init python:
    # key, who, school, max score, (x, y), head crop in their pfp
    IDEAS = [
        ("tao",       "jassi",        "Jassi",        "Taoism",         2, (-0.85, -0.30), (176, 8, 200, 200)),
        ("stoic",     "edvance",      "Edvance",      "Stoicism",       2, ( 0.20,  0.88), (131, 76, 166, 166)),
        ("nietzsche", "shwetank",     "Shwetank",     "Nietzsche",      2, ( 0.88, -0.58), (120, 10, 140, 140)),
        ("cynic",     "diogenes",     "Diogenes",     "Cynicism",       1, (-0.72,  0.50), (91, 42, 176, 176)),
        ("pessimist", "schopenhauer", "Schopenhauer", "Pessimism",      1, (-0.40, -0.82), (93, 54, 219, 219)),
        ("absurd",    "camus",        "Camus",        "Absurdism",      1, ( 0.75,  0.55), (113, 95, 120, 120)),
        ("leap",      "kierkegaard",  "Kierkegaard",  "Existentialism", 1, ( 0.42, -0.86), (91, 46, 193, 193)),
    ]

    PLANET_NUDGE = {
        "down":  (-0.25, 0.0),
        "carry": (0.25, 0.0),
        "share": (0.0, -0.25),
        "look":  (0.0, 0.25),
    }

    RESULTS = {
        "unbothered": ("The Unbothered", "you think it through, then you let it go. it's honestly a little annoying how calm you are."),
        "stubborn": ("The Stubborn One", "you did the math, the odds are bad, and you're doing it anyway."),
        "soft": ("The Soft Landing", "you don't fight the fall. you feel it, and you let people catch you."),
        "main": ("The Main Character", "you feel all of it and run straight at it. CHARACTER DEVELOPMENT."),
        "everyone": ("A Bit of Everyone", "you took bits from all over and somehow made it work."),
        "unconvinced": ("The Unconvinced", "you heard everyone out and bought none of it. Socrates would've liked you."),
    }

    def compass_result(took, planet):
        levels = {}
        for key, tag, who, school, top, pos, crop in IDEAS:
            levels[key] = min(1.0, float(took.get(key, 0)) / top)
        total = sum(levels.values())

        x, y = PLANET_NUDGE.get(planet, (0.0, 0.0))
        if total:
            # averages bunch up in the middle, so spread them out
            x += 1.4 * sum(levels[i[0]] * i[5][0] for i in IDEAS) / total
            y += 1.4 * sum(levels[i[0]] * i[5][1] for i in IDEAS) / total
        x = max(-0.92, min(0.92, x))
        y = max(-0.92, min(0.92, y))

        if not total:
            kind = "unconvinced"
        elif total >= 2 and x * x + y * y < 0.07:
            kind = "everyone"
        elif y >= 0:
            kind = "stubborn" if x >= 0 else "unbothered"
        else:
            kind = "main" if x >= 0 else "soft"

        closest = None
        picked = [i for i in IDEAS if levels[i[0]]]
        if picked:
            closest = min(picked, key=lambda i: (i[5][0] - x) ** 2 + (i[5][1] - y) ** 2)[2]

        return dict(
            x=x,
            y=y,
            kind=kind,
            closest=closest,
            share={k: (v / total if total else 0.0) for k, v in levels.items()},
        )


define COMPASS_SIZE = 840
define COMPASS_R = 345

transform compass_drop:
    yoffset -1000 alpha 0.0
    pause .5
    alpha 1.0
    easeout .45 yoffset 0
    easein .16 yoffset -90
    easeout .16 yoffset 0
    easein .09 yoffset -25
    easeout .09 yoffset 0

style compass_text is text:
    font MENU_FONT
    instance "Bold"
    size 26
    color "#ece8ff"

style compass_axis is compass_text:
    instance "Black"
    size 30
    color "#ffffff"

style compass_title is compass_text:
    instance "Black"
    size 76
    color MENU_ACCENT

style compass_body is compass_text:
    instance "Medium"
    size 32

style compass_button is menu_btn
style compass_button_text is menu_btn_text


screen philosophy_compass(res):
    modal True
    zorder 100

    $ mid = COMPASS_SIZE // 2

    add Solid(MENU_INK)

    timer 0.95 action Play("sound", audio.bounce)

    fixed:
        xysize (COMPASS_SIZE, COMPASS_SIZE)
        xpos 100 ypos 120

        # quadrants, yours lights up
        for kind, qx, qy, col, tx, ty in [
                ("unbothered", 0, 0, "#3b3470", 0.03, 0.02),
                ("stubborn", 1, 0, "#6b5524", 0.97, 0.02),
                ("soft", 0, 1, "#27535a", 0.03, 0.98),
                ("main", 1, 1, "#6b2d4b", 0.97, 0.98)]:
            add Solid(col):
                xysize (mid, mid)
                xpos qx * mid ypos qy * mid
                alpha (1.0 if res["kind"] in (kind, "everyone") else 0.5)
            text RESULTS[kind][0]:
                style "compass_text"
                size 24
                color (MENU_ACCENT if res["kind"] == kind else "#ffffff88")
                xalign tx yalign ty

        add Solid("#ffffff99"):
            xysize (4, COMPASS_SIZE)
            xalign 0.5
        add Solid("#ffffff99"):
            xysize (COMPASS_SIZE, 4)
            yalign 0.5


        for key, tag, who, school, top, pos, crop in IDEAS:
            $ px = mid + int(pos[0] * COMPASS_R)
            $ py = mid - int(pos[1] * COMPASS_R)
            $ on = res["share"][key] > 0
            add Transform("pfp/%s.png" % tag, crop=crop, xysize=(92, 92), matrixcolor=SaturationMatrix(1.0 if on else 0.0), alpha=(1.0 if on else 0.35)):
                pos (px, py) anchor (0.5, 0.5)
            text who:
                style "compass_text"
                size 20
                color ("#ffffff" if on else "#ffffff66")
                xpos px xanchor 0.5 ypos (py + 45)

        fixed at compass_drop:
            xysize (110, 136)
            xpos mid + int(res["x"] * COMPASS_R) xanchor 0.5
            ypos mid - int(res["y"] * COMPASS_R) yanchor 1.0

            add Transform("pfp/theguy.png", crop=(43, 2, 315, 315), xysize=(86, 86)):
                xalign 0.5
            text "YOU" style "compass_axis" color MENU_ACCENT outlines [(4, MENU_INK, 0, 0)] xalign 0.5 ypos 78
            add Solid(MENU_ACCENT):
                xysize (16, 16)
                xalign 0.5 yalign 1.0

    text "HEAD" style "compass_axis" xpos (100 + mid) xanchor 0.5 ypos 72
    text "HEART" style "compass_axis" xpos (100 + mid) xanchor 0.5 ypos 972
    text "LET GO" style "compass_axis" at Transform(rotate=-90):
        pos (70, 120 + mid) anchor (0.5, 0.5)
    text "PUSH THROUGH" style "compass_axis" at Transform(rotate=90):
        pos (972, 120 + mid) anchor (0.5, 0.5)

    vbox at fade_in_late(1.4):
        xpos 1040 ypos 120
        xsize 800
        spacing 14

        text "you are" style "compass_body"
        text RESULTS[res["kind"]][0] style "compass_title"
        text RESULTS[res["kind"]][1] style "compass_body"
        if res["closest"]:
            text "closest to: {}".format(res["closest"]) style "compass_body" color MENU_ACCENT

        null height 14

        for key, tag, who, school, top, pos, crop in IDEAS:
            $ share = res["share"][key]
            fixed:
                xysize (800, 44)
                text school:
                    style "compass_text"
                    color ("#ffffff" if share else "#ffffff66")
                    yalign 0.5
                bar:
                    value StaticValue(share, 1.0)
                    xpos 260 yalign 0.5
                    xysize (420, 22)
                    left_bar Solid(MENU_ACCENT)
                    right_bar Solid("#ffffff22")
                    thumb None
                text "{}%".format(int(round(share * 100))):
                    style "compass_text"
                    xalign 1.0 yalign 0.5

        null height 10
        textbutton "Continue" style "compass_button" action Return() at menu_button
