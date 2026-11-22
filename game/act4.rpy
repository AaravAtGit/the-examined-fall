# act 4 - 6am, the ending

default planet = None

# morning light
transform dawn:
    matrixcolor TintMatrix("#ffd7ad") * BrightnessMatrix(0.03)


label act4:
    $ fix_took()
    play music heavy fadeout 1.0 fadein 1.0 if_changed

    scene bg haven_venue at dawn with fade
    show aarav sad at pos_left
    show theguy neutral at pos_right
    with dissolve

    "6am."

    ng "You look worse than me."
    a "I keep seeing the volunteers. They've been up all night running this thing."
    a "And I spent their chocolates on getting myself in."
    ng "You told me to go ask people how they get back up."
    ng "So I asked. Some of them were even alive."
    a confused "Some of them?"
    ng "Don't worry about it."

    # he hands back whatever the player took
    if not any(took[k] for k in TOOK_KEYS):
        ng "I didn't buy any of it, honestly. So this one's just from me."
    if took["tao"]:
        ng "Breathe first. Don't go running over there in a panic."
    if took["stoic"]:
        ng "You can't un-suitcase yourself. You can pick what you do next."
    if took["nietzsche"]:
        ng "It's supposed to feel bad. So feel bad, and walk over anyway."
    if took["cynic"]:
        ng "You don't need them to think you're cool. Drop that part."
    if took["pessimist"]:
        ng "They're as tired as you are. They'll get it."
    if took["absurd"]:
        ng "It might go horribly. Do it anyway."
    if took["leap"]:
        ng "You won't know how it goes till you've done it."
    ng "Go tell them."

    a neutral "...When did you get good at this?"
    ng "About three hours ago."

    # confession
    stop music fadeout 1.5
    scene bg haven_venue at dawn with dissolve
    show aarav sheepish at pos_left
    show theguy neutral at pos_mid
    show dsp neutral at pos_right
    with dissolve

    a "DSP. I have to confess something."
    dsp "Is it the suitcase?"
    a "It's the suitcase. And the chocolates. Those were meant for all of you."
    dsp "I know. I handed them out."
    a shocked "You what?"
    dsp "You thought I ate a whole bag of chocolates?"
    dsp "..."
    dsp happy "I ate the Silk."

    play music home fadein 1.0
    a sad "So I felt horrible all night for nothing?"
    if took["nietzsche"]:
        ng happy "Not for nothing. CHARACTER DEVELOPMENT."
    else:
        ng "Not for nothing. You still came and said it."

    dsp suspicious "You're still not registered though."
    a sheepish "...Yeah."
    dsp neutral "And I'm short on volunteers."
    dsp happy "So grab a trash bag. You're staff now."
    a happy "I'm allowed in?"
    dsp "You're allowed to clean."

    if packed == "nothing":
        a "Yesterday I was luggage. Today I'm staff."
    elif packed == "water":
        a "I'll do it. I'm hydrated."
    else:
        a "I told Oreek the chocolates were strategic."

    hide dsp with dissolve
    show theguy at pos_right with move

    # the planet
    a neutral "What about you?"

    if feeling == "stuck":
        a "Still feel stuck?"
        ng "A bit. But I did walk all the way over here."
    elif feeling == "not_enough":
        a "Still feel like it wasn't enough?"
        ng "Maybe it wasn't. I can be sad about that and still try again."
    elif feeling == "letdown":
        a "Still feel like you're letting everyone down?"
        ng "Nobody here asked me for anything. They just talked to me."
    elif feeling == "empty":
        a "Does anything matter yet?"
        ng "This kind of did."
    else:
        ng "Not fixed. Better though."

    a "And the planet?"

    menu:
        "What do you do with it?"

        "Put it down.":
            $ planet = "down"
            ng neutral "I think I'm done holding it."
            play sound bounce
            "He let go." with vpunch
            ng shocked "...It bounces?"
            a "It bounces."

        "Keep carrying it. It's yours.":
            $ planet = "carry"
            ng happy "I'm keeping it. It's still heavy."
            ng "I think I just got stronger."

        "Get Aarav to hold the other side.":
            $ planet = "share"
            ng neutral "Can you grab the other side?"
            a shocked "Oh god. That IS heavy."
            ng happy "That's what I said."

        "Take a proper look at it first.":
            $ planet = "look"
            ng confused "I held it all night and never actually looked at it."
            a "And?"
            ng happy "It's smaller than I thought."

    a happy "Come on. I've got a hall to clean."
    ng happy "Yeah. I'm coming."

    scene black with fade
    "{i}\"The unexamined life is not worth living.\"{/i}\n- Socrates"
    "{i}So let's examine yours.{/i}"

    window hide
    $ quick_menu = False
    call screen philosophy_compass(compass_result(took, planet))
    with dissolve
    call screen end_credits
    with dissolve
    $ quick_menu = True
    return
