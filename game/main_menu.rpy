# main menu
# title letters fall and bounce
# old default menu is still in screens.rpy (main_menu_default)

define MENU_FONT = "fonts/Rubik.ttf"
define MENU_INK = "#1b1530"
define MENU_ACCENT = "#ffd84d"

# Letter animations
transform letter_fall(delay, height=60, hop_every=6.0):
    yoffset -900 alpha 0.0
    pause delay
    alpha 1.0
    easeout .42 yoffset 0
    easein .16 yoffset -height
    easeout .16 yoffset 0
    easein .09 yoffset -(height * .3)
    easeout .09 yoffset 0
    block:
        pause hop_every
        easein .14 yoffset -18
        easeout .14 yoffset 0
        repeat

transform fade_in_late(delay):
    alpha 0.0 yoffset 20
    pause delay
    ease .6 alpha 1.0 yoffset 0

transform menu_button:
    on idle:
        ease .15 zoom 1.0 xoffset 0
    on hover:
        easein .08 zoom 1.12 xoffset 12
        easeout .08 zoom 1.06

transform menu_bob(delay=0.0):
    yoffset 0
    pause delay
    block:
        ease 1.6 yoffset -14
        ease 1.6 yoffset 0
        repeat

transform menu_slide_in(delay):
    xoffset 500 alpha 0.0
    pause delay
    easein .5 xoffset 0 alpha 1.0

# Styles
style menu_title_small is text:
    font MENU_FONT
    instance "Black"
    size 92
    color "#ffffff"
    outlines [(7, MENU_INK, 0, 0), (7, "#00000055", 6, 8)]
    kerning 2

style menu_title_big is menu_title_small:
    size 230
    color MENU_ACCENT
    outlines [(10, MENU_INK, 0, 0), (10, "#00000066", 8, 12)]

style menu_tagline is text:
    font MENU_FONT
    instance "Medium"
    size 34
    color "#e9e6ff"
    italic True
    outlines [(3, MENU_INK, 0, 0)]

style menu_btn is button:
    padding (0, 4)

style menu_btn_text is text:
    font MENU_FONT
    instance "Bold"
    size 54
    idle_color "#ffffff"
    hover_color MENU_ACCENT
    outlines [(5, MENU_INK, 0, 0)]

# Screen
screen main_menu():
    tag menu

    add "bg aarav_room" at Transform(blur=6, matrixcolor=BrightnessMatrix(-0.08))
    add "ui/menu_gradient.png"

    # FALL hitting the floor
    timer 1.37 action Play("sound", audio.bounce)

    # characters on the right
    add "aarav neutral" at menu_slide_in(1.6), menu_bob(0.0):
        xalign .98 yalign 1.0 yoffset 40
    add "oreek neutral" at menu_slide_in(1.8), menu_bob(0.8):
        xalign .70 yalign 1.0 yoffset 70

    # title
    vbox:
        xpos 110 ypos 90
        spacing -30

        hbox:
            for i, ch in enumerate("THE EXAMINED"):
                text ch style "menu_title_small" at letter_fall(0.15 + i * 0.05, 40, 7.0 + i * 0.13)

        hbox:
            xoffset -6
            for i, ch in enumerate("FALL"):
                text ch style "menu_title_big" at letter_fall(0.95 + i * 0.12, 110, 5.0 + i * 0.25)

        text "a game about bouncing back" style "menu_tagline" at fade_in_late(1.9):
            xoffset 10
            yoffset 40

    # Buttons
    vbox:
        xpos 120 ypos 610
        spacing 0

        textbutton _("Start") style "menu_btn" action Start() at menu_button, fade_in_late(2.1)
        textbutton _("Load") style "menu_btn" action ShowMenu("load") at menu_button, fade_in_late(2.2)
        textbutton _("Preferences") style "menu_btn" action ShowMenu("preferences") at menu_button, fade_in_late(2.3)
        textbutton _("About") style "menu_btn" action ShowMenu("about") at menu_button, fade_in_late(2.4)
        if renpy.variant("pc"):
            textbutton _("Quit") style "menu_btn" action Quit(confirm=False) at menu_button, fade_in_late(2.5)
