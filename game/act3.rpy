# act 3 - 3am
# descartes bit, then diogenes, schopenhauer, camus, kierkegaard

# purple-ish blur for the 3am stuff
transform haze:
    matrixcolor TintMatrix("#9d8cff") * BrightnessMatrix(-0.12)
    blur 3


label act3:
    $ fix_took()

    # Scene 1: The Descartes gag
    play music night fadein 2.0
    scene bg haven_venue at haze with fade
    show aarav neutral at pos_left
    show shwetank neutral at pos_right
    with dissolve

    "3:07am. Twenty-four hours into the project."
    "Aarav and Shwetank had stopped blinking about an hour ago."

    shw "Okay, if this build fails one more time, I'm going to walk into the sea."
    a "We're in Delhi."
    shw "I'll find one."

    "Nobody said anything for a while."

    a confused "...Dude."
    shw "What."
    stop music
    a "Are you real?"
    shw "..."
    shw confused "I think I am."

    show descartes happy at pos_mid with dissolve
    des "That's actually quite profound evidenc--"

    play sound scratch
    everyone "{size=+20}RENÉ DESCARTES!!{/size}" with vpunch

    hide descartes with dissolve
    show aarav shocked
    show shwetank shocked

    "..."
    shw neutral "...We should sleep."
    a neutral "We should drink more coffee."
    shw "...Yeah, we should drink more coffee."

    # Scene 2: The Guy in the haze
    play music night fadein 2.0
    scene bg haven_venue at haze with fade
    show theguy neutral at pos_mid with dissolve

    "You were still awake too."
    "Around 3:30am, dead philosophers started showing up. You weren't even that surprised."

    # Diogenes: the Cynic
    show theguy at pos_left with move
    "There was a suitcase in the corner. A familiar 28-inch suitcase."
    "Someone was living in it."

    show diogenes happy at pos_right with dissolve
    dio "Best barrel I've ever had. Wheels and everything."
    ng confused "...Who are you?"
    dio "Diogenes. I used to live in a jar in Athens. Now I live in this."
    dio neutral "You're carrying a whole planet. Why?"
    ng "Because it's mine?"
    dio "Is it? Or did someone hand it to you?"
    dio "Expectations. Rankings. What people will think. Most of that weight was never yours."
    dio "I once saw a kid drink water with his bare hands, and threw away my cup. Didn't need it."
    dio "Alexander the Great once asked me what he could do for me. I told him to stand out of my sunlight."
    dio happy "Drop what you don't need. You'll be amazed how light you get."

    menu:
        "Take it: \"Maybe some of this weight isn't even mine.\"":
            $ took["cynic"] += 1
            ng neutral "Maybe some of this weight isn't even mine."
            dio "Now you're thinking like a dog. That's a compliment, by the way."

        "Leave it: \"I can't just throw everything away.\"":
            ng neutral "I can't just throw everything away."
            dio neutral "Not everything. Just the cup."
            dio "Think about it. Now move, you're in my sunlight."

    hide diogenes with dissolve

    # Schopenhauer: the pessimist
    "Near the speakers, someone was glaring at the music."
    show schopenhauer angry at pos_right with dissolve

    scho "Noise. Noise everywhere. I wrote an entire essay about how much I hate noise."
    ng "...Hi?"
    scho neutral "You look miserable."
    ng sad "Thanks."
    scho "It wasn't an insult. Everyone is miserable. Life swings like a pendulum between suffering and boredom."
    scho "You want something, it hurts. You get it, you're bored. Then you want something else."
    ng "That's... the most depressing thing anyone's said to me tonight."
    scho "Yes. But listen."
    scho "If everyone is suffering, then the person next to you is too. Every single one of them."
    scho "So I always thought we should greet each other not as 'sir' or 'madam,' but as 'fellow sufferer.'"
    scho "It makes you kinder. And kindness is the only real relief there is."
    scho "That, and music. Good music. Not... whatever this is."

    menu:
        "Take it: \"So I'm not the only one carrying something.\"":
            $ took["pessimist"] += 1
            ng neutral "So I'm not the only one carrying something."
            scho "No one is the only one. That's the one good thing about suffering. It's crowded."

        "Leave it: \"That's too bleak for me.\"":
            ng neutral "That's too bleak for me."
            scho "It's 3am at a hackathon. Everything is bleak."
            scho happy "Goodnight, fellow sufferer."

    hide schopenhauer with dissolve

    # Camus: the absurd
    play sound bounce
    "A football rolled across the floor and bounced off your foot."
    show camus happy at pos_right with dissolve

    cam "Sorry! Old habit. I was a goalkeeper, you know."
    cam "Everything I know about life, I learned from football. The ball never comes the way you expect."
    cam neutral "You're holding the world."
    ng "It's heavy."
    cam "There was a man named Sisyphus. The gods made him push a rock up a hill forever. Every time he reached the top, it rolled back down."
    cam "Pointless. Absurd. Forever."

    if feeling == "empty":
        ng sad "Like nothing really matters."
        cam "Exactly! Nothing has a meaning built in. Good. That means you get to decide."
    else:
        ng sad "That sounds like my week."

    cam "But the moment he walks back down to the rock? That's his. Nobody can take that from him."
    cam happy "One must imagine Sisyphus happy."
    cam "Not because the rock stops. Because he decides to keep going anyway."
    cam "The ball always bounces back. So do you."

    menu:
        "Take it: \"Then I'll push it anyway.\"":
            $ took["absurd"] += 1
            ng neutral "Then I'll push it anyway."
            cam happy "There it is. Revolt! At 3am! Beautiful."

        "Leave it: \"That sounds exhausting.\"":
            ng neutral "That sounds exhausting."
            cam neutral "It is. So is everything worth doing."
            cam "Here. Keep the ball. Just in case."

    hide camus with dissolve

    # Kierkegaard: the leap
    "The last one was sitting alone, writing furiously in a notebook."
    show kierkegaard neutral at pos_right with dissolve

    kie "Ah. You're the one with the planet."
    ng "Who are you?"
    kie "Depends on the book. Johannes Climacus. Victor Eremita. Johannes de Silentio. Kierkegaard, if you insist."
    ng confused "...That's a lot of names."
    kie happy "I had a lot to say and very few friends."

    kie neutral "You're afraid, aren't you? Not of one thing. Of all the things that could happen next."
    ng "...Yeah."
    kie "I called that 'the dizziness of freedom.' You feel sick because you're standing at the edge of every possible choice."
    kie "That's not a bad sign. It means you're free."
    kie "Here's the cruel joke: life can only be understood backwards. But it has to be lived forwards."
    kie "You won't understand this fall until much later. You don't have to understand it to keep walking."
    kie "At some point, you just leap."

    menu:
        "Take it: \"I don't need it to make sense yet.\"":
            $ took["leap"] += 1
            ng neutral "I don't need it to make sense yet."
            kie happy "Then you're already mid-air. Congratulations."

        "Leave it: \"I need to understand it first.\"":
            ng neutral "I need to understand it first."
            kie neutral "Then you'll be standing at the edge for a very long time."
            kie "But the edge isn't going anywhere. Neither are you."

    hide kierkegaard with dissolve

    # End of Act 3
    show theguy at pos_mid with move
    "Then they were gone."
    "You were still holding the world. It felt a bit lighter though."

    jump act4
