# credits
# the music bit is required by CC BY 4.0, don't remove it

define MUSIC_CREDIT = """\"Carefree\", \"Sneaky Snitch\", \"Gymnopedie No. 1\", \"Deliberate Thought\", \"Dreamy Flashback\"
Kevin MacLeod ({a=https://incompetech.com}incompetech.com{/a})
Licensed under Creative Commons: By Attribution 4.0
{a=https://creativecommons.org/licenses/by/4.0/}creativecommons.org/licenses/by/4.0{/a}
(trimmed and volume adjusted)"""

style credits_text is compass_body:
    xalign 0.5
    textalign 0.5

style credits_head is compass_title:
    xalign 0.5

screen end_credits():
    modal True
    zorder 100

    add Solid(MENU_INK)

    vbox at fade_in_late(0.2):
        align (0.5, 0.5)
        xsize 1600
        spacing 18

        text "The Examined Fall" style "credits_head"
        text "a game about bouncing back" style "credits_text" italic True
        null height 20

        text "made by Aarav" style "credits_text"
        text "with Oreek, Shrey, DSP, Jassi, Edvance, Shwetank and Nitik" style "credits_text"
        text "thanks to everyone who kept Haven running" style "credits_text"
        null height 20

        text "music" style "credits_text" color MENU_ACCENT
        text MUSIC_CREDIT style "credits_text" size 26
        null height 30

        textbutton "Back to menu":
            style "compass_button"
            xalign 0.5
            action Return()
            at menu_button
