# act 2 - the guy
# his problem is never named, player just picks how it feels
# jassi = tao, edvance = stoic, shwetank = nietzsche

default feeling = None
default took = {}

init python:
    TOOK_KEYS = ("tao", "stoic", "nietzsche", "cynic", "pessimist", "absurd", "leap")
    OLD_KEYS = {"patience": "tao", "embrace": "nietzsche"}  # renamed keys

    def fix_took():
        # old saves might be missing some keys
        store.took = dict(store.took or {})
        for old, new in OLD_KEYS.items():
            if old in store.took:
                store.took[new] = store.took.get(new, 0) + store.took.pop(old)
        for k in TOOK_KEYS:
            store.took.setdefault(k, 0)

    config.after_load_callbacks.append(fix_took)


label act2:
    $ fix_took()

    # Scene 1: The corner
    scene bg haven_venue with fade
    show aarav sad at pos_left

    a "Everyone here got in the normal way."
    a "I got in as checked luggage."

    "Then he noticed someone in the far corner."
    "Just sitting there."

    show theguy neutral at pos_right with dissolve

    "And holding... the Earth?"

    a shocked "...Is that a globe?"
    ng "It's heavy."
    a neutral "Right. Okay. Sure."
    a "Mind if I sit?"
    ng "..."
    ng "It's a free corner."

    a "You're not building anything?"
    ng "Was going to."
    ng "Then I didn't feel like it."
    ng "Then I didn't feel like anything."

    show aarav neutral
    a "Did something happen?"

    ng sad "Yeah."
    ng "Something happened."

    a "You don't have to tell me what."
    ng neutral "..."

    menu:
        "What does it feel like?"

        "\"Like everyone's moving forward, and I'm stuck.\"":
            $ feeling = "stuck"
            ng sad "Like everyone's moving forward, and I'm stuck."

        "\"Like I gave it everything, and it wasn't enough.\"":
            $ feeling = "not_enough"
            ng sad "Like I gave it everything, and it wasn't enough."

        "\"Like I'm letting everyone down.\"":
            $ feeling = "letdown"
            ng sad "Like I'm letting everyone down."

        "\"Like nothing really matters anymore.\"":
            $ feeling = "empty"
            ng sad "Like nothing really matters anymore."

    a "..."
    a "That sounds really heavy."
    ng "That's what I said."

    # Aarav's confession
    a sheepish "Can I tell you something embarrassing?"
    ng neutral "..."
    a "I wasn't supposed to be here. I missed registration."
    a "So I came in a suitcase. And bribed my way in with chocolates that were meant for the volunteers."
    ng confused "...You came in a suitcase."
    a "A 28-inch suitcase."
    ng "..."
    "He almost laughed."

    a neutral "My point is, I'm not exactly the guy with answers."
    a "But this room is full of people who've crashed. Hard. All of them got back up somehow."
    a happy "Go ask them how."
    ng "And if they don't have answers either?"
    a "Then at least you'll have company while not having answers."

    ng neutral "..."
    "He got up. The Earth came with him."

    # POV shift
    scene black with fade
    "{i}From here, you're him.{/i}"
    "{i}Take what helps. Leave what doesn't.{/i}"

    # Scene 2: Jassi, patience
    scene bg haven_venue with fade
    show theguy neutral at pos_left
    show jassi neutral at pos_right
    with dissolve

    j "Hey. You're the one Aarav sent?"
    ng "Apparently."
    j "He said you were sitting in a corner holding the planet."
    ng "It's heavy."
    j happy "Looks heavy."

    j neutral "Can I tell you what I do when everything falls apart?"
    j "Nothing."
    ng confused "...Nothing?"
    j "Not forever. But at first, nothing."
    j "When there's a storm, you don't sail out into it to prove you're brave. You'd just sink faster."
    j "You wait. Let the storm settle into a calm sea."
    j "Then you sail."
    j "Patience isn't giving up. It's waiting until you can actually see where you're going."
    j "Lao Tzu had a thing about water. It's the softest thing there is, and it still wears down mountains."
    j "It doesn't fight. It just keeps flowing. Be like water."

    menu:
        "\"That actually helps.\"":
            $ took["tao"] += 2
            ng neutral "That actually helps."
            j happy "Told you. Two-thousand-year-old advice is old for a reason."

        "\"But what if the storm never stops?\"":
            $ took["tao"] += 1
            ng sad "But what if the storm never stops?"
            j "Then you learn to sail in rain."
            j "But they always stop. Even the long ones."

        "\"I've been waiting. It's not working.\"":
            ng sad "I've been waiting. It's not working."
            j neutral "Then maybe you need different advice than mine."
            j "Edvance is over there. Talk to him. He's... intense, but he means well."

    # Scene 3: Edvance vs Shwetank, Stoic vs anti-Stoic
    scene bg haven_venue with dissolve
    show edvance neutral at pos_left
    show theguy neutral at pos_mid
    with dissolve

    ed "Let me guess. Something went wrong, and now it's all you can think about."
    ng "...Yeah."
    ed "Here's the thing. You can't control what happened."
    ed "You can't control what people think of you. You can't control the storm."
    ed "You control exactly one thing: how you respond."
    ed "That's Stoicism. Epictetus figured it out two thousand years ago, and he was a slave. If he could do it, so can you."
    ed "Don't let it {i}feel{/i} like the end of the world, and it won't be."

    show shwetank angry at pos_right with dissolve
    shw "Oh, here we go."
    ed suspicious "Shwetank."
    shw "\"Don't let your emotions affect you.\" Do you hear yourself?"
    shw "Stoicism is a coping mechanism, man."
    shw "People don't pick it up because it's logical. They pick it up because it's {i}comforting.{/i}"
    shw "It's for people who've been beaten down by fate so badly that pretending not to feel is easier than feeling."
    shw "It's avoidance. You're just hiding from the suffering."

    ed angry "That's not what it--"
    shw "You have to {i}accept{/i} the suffering. Walk straight into it."
    shw happy "That's how you grow! That's how you become a better, higher version of yourself!"
    shw "It's called CHARACTER DEVELOPMENT!" with vpunch

    ed neutral "You know \"love your fate\" is basically a Stoic idea, right? Nietzsche borrowed it."
    shw shocked "..."
    shw "...That's not the point."
    ed "It's a little bit the point."

    "They both turned to you."

    menu:
        "Side with Edvance: \"I can't control what happened. Only what I do next.\"":
            $ took["stoic"] += 2
            ng neutral "I can't control what happened. Only what I do next."
            ed happy "Exactly."
            shw suspicious "Fine. But feel it first, at least. Promise me."

        "Side with Shwetank: \"I don't want to pretend it doesn't hurt.\"":
            $ took["nietzsche"] += 2
            ng sad "I don't want to pretend it doesn't hurt."
            shw happy "THANK you."
            ed neutral "Nobody said pretend. But okay. Feel it. Then decide what to do with it."

        "\"Honestly? You both sound kind of right.\"":
            $ took["stoic"] += 1
            $ took["nietzsche"] += 1
            ng confused "Honestly? You both sound kind of right."
            shw "..."
            ed "..."
            shw "...I hate that he's right."
            ed "Feel it. Then don't let it steer. Fine. Truce."

    # Scene 4: Night falls
    scene bg haven_venue with fade
    show aarav neutral at pos_left
    show theguy neutral at pos_right
    with dissolve

    "By 3am half of Haven was asleep on beanbags. The other half was on 420mg of caffeine."

    a "So? Did they fix you?"
    ng "No."
    ng "But..."

    if took["tao"] >= 2:
        ng "Jassi said to wait for the storm to settle. I think I can do that."
    elif took["tao"] == 1:
        ng "Jassi says storms always stop. I'm not sure I believe him yet."

    if took["stoic"] >= 2:
        ng "Edvance said I only control what I do next. That's... less than everything. Which is easier to carry."
    elif took["nietzsche"] >= 2:
        ng "Shwetank said to feel it instead of hiding from it. So I'm going to stop hiding."
    else:
        ng "Edvance and Shwetank argued about it for twenty minutes. Weirdly, that helped the most."

    a happy "That's not nothing."
    ng "It's not nothing."

    "He was still holding the Earth."
    "But he wasn't staring at it anymore."

    a neutral "Okay. I'm going to get my fifth coffee."
    a "I'm sure nothing weird will happen to us after five coffees at 3am."

    jump act3
