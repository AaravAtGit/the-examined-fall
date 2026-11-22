# act 1 - missed registration, suitcase, chocolates

default packed = None


label act1:

    # Scene 1: Registration closed
    scene bg aarav_room with fade
    play music home fadein 1.0 if_changed

    show aarav neutral at pos_mid
    a "Okay. Haven Delhi. The flagship hackclub event."
    a happy "This is it. Let me just open the registration form and..."

    stop music
    play sound error
    show aarav shocked
    "{b}Registrations are now closed.{/b}"

    a "..."
    a "Closed?"
    a "CLOSED?!" with vpunch
    a "It was open, like, yesterday. Right?"

    "It had closed four days ago."
    "He had set a reminder. He had snoozed that reminder eleven times."

    # Scene 2: The group chat mourns
    show aarav sad
    play music heavy fadein 1.0
    a "I have to tell the GC."

    gc "{b}Aarav:{/b} guys i missed haven registration"
    gc "{b}Jassi:{/b} NOOOOO"
    gc "{b}Shwetank:{/b} bro how"
    gc "{b}Edvance:{/b} F"
    gc "{b}Oreek:{/b} wait you're actually not coming??"
    gc "{b}Nitik:{/b} haven without aarav is just... a building"

    a "They're right. It's just a building."
    a "A building I am {i}not allowed inside.{/i}"

    "Aarav stared at the ceiling for a long time."
    "Then he stared at the cupboard."
    "Then, very slowly, he thought about luggage."

    play music sneaky fadeout 0.5
    show aarav scheming
    a "If I can't walk in as a person..."
    a "I'll go in as cargo."

    # Scene 3: Oreek's suitcase
    scene bg oreek_room with dissolve
    show oreek neutral at pos_right
    show aarav neutral at pos_left
    with dissolve

    a "Oreek. Quick question. Purely hypothetical."
    o suspicious "Every time you say 'purely hypothetical', something illegal happens."
    a "How big is your suitcase?"
    o "...Why."
    a "Is it big enough to fit a human being?"
    o shocked "WHY would you need it to fit a--"
    o "No."
    o "NO. Absolutely not."

    a scheming "Hear me out."
    o "I'm not hearing you out."
    a "You hear me out every time."
    o neutral "...Fine. Go."

    a "You're going to Haven. You're taking a suitcase anyway."
    a "Clothes go in the suitcase. I am wearing clothes."
    a "So technically I'm just a very dense layer of clothes."
    o "That is the worst logic I have ever heard."
    o "...It's a 28-inch suitcase."
    a happy "I'll fold."

    o "If we're doing this, what are you packing in there with you?"

    menu:
        "Chocolates. A lot of chocolates.":
            $ packed = "chocolates"
            a "Chocolates. Trust me, it's strategic."
            o "Strategic how?"
            a "You'll see."

        "A water bottle. I'm a responsible stowaway.":
            $ packed = "water"
            a "A water bottle. Hydration matters, even in a suitcase."
            o "Okay, that's actually reasonable."
            o "I'm throwing in some chocolates too. You'll get hungry."

        "Nothing. I AM the luggage.":
            $ packed = "nothing"
            a "Nothing. I am the luggage."
            o "You're impossible."
            o "I'm throwing in some chocolates. If you pass out in there, it's on me."

    # Scene 3b: Sanity check with Shrey (separate call)
    # Shrey and Oreek barely know each other, so Aarav runs it past Shrey alone.

    scene bg aarav_room with dissolve
    show aarav neutral at pos_mid

    "That night, Aarav called Shrey. Somebody had to tell him if this was a bad idea."
    "Ideally somebody who would say it wasn't."

    play sound phone_ring
    s_call "Hello?"
    a "Shrey. I've found a way into Haven."
    s_call "Registrations are closed."
    a "Not the way I'm going in."
    a scheming "I'm going in a suitcase."
    s_call "..."
    s_call "Whose suitcase?"
    a "Oreek's."
    a "He's going anyway. It's a 28-inch suitcase."

    s_call "This is the most insane idea I've heard in my life."
    s_call "What about airflow? What about security? What about your DIGNITY?"
    a "My dignity left when I snoozed that reminder eleven times."
    s_call "Okay, fair, but you'll get crushed."
    a "I'll be crushed if I {i}don't{/i} go."
    s_call "...That was way too dramatic for something this stupid."
    s_call "Also, I'm literally volunteering at Haven. I did not hear any of this."
    a happy "Hear what?"
    s_call "Exactly."
    s_call "...Send pics."

    # Scene 4: In the suitcase
    scene black with fade
    play sound zip_sfx
    "{i}ZZZZZIIIP.{/i}"

    a "It's fine. It's cozy. It's like a sleeping bag with trust issues."
    play sound thud
    "{i}THUD.{/i}" with vpunch
    a "Ow."
    o_muffled "Sorry. Stairs."
    play sound thuds
    "{i}THUD. THUD. THUD.{/i}" with vpunch
    a "How many stairs do you HAVE?"
    o_muffled "Stop talking, the auto driver is looking at the bag."

    "Forty minutes, one auto, a metro ride and a lot of wheels later..."

    o_muffled "We're here. Don't. Make. A sound."

    # Scene 5: DSP at the gate
    scene bg haven_venue with fade
    show dsp neutral at pos_right
    show oreek nervous at pos_left
    with dissolve

    dsp "Name?"
    o "Oreek."
    dsp "Got you. And the suitcase?"
    o "...Clothes."
    dsp "Big suitcase for two nights."
    o "I have a lot of... feelings. About clothes."

    "Somewhere inside the suitcase, a nose itched."
    stop music
    play sound sneeze
    "{i}ACHOO.{/i}" with vpunch

    dsp suspicious "..."
    dsp "Your clothes just sneezed."
    o "Allergies. The clothes have allergies."

    play sound zip_sfx
    "The zip slid open. A head popped out."

    hide oreek
    show aarav sheepish at pos_left
    with dissolve

    a "Hi DSP."
    dsp "Aarav. You're not registered."
    a "I'm aware."
    dsp "You came in a {i}suitcase.{/i}"
    a "Also aware."

    play music sneaky
    a scheming "But consider this."
    "Aarav pulled out the chocolates."

    "They had been meant for the volunteers and organizers. Aditya, Shrey, Aryan, Whis, DSP, and everyone else keeping Haven running."

    dsp "...Is that a Five Star?"
    a "A whole bag of Five Stars. Milkybars. And a Dairy Milk Silk."
    a "Enough for every volunteer at Haven."
    dsp neutral "..."
    "DSP looked at the chocolates."
    "Then at Aarav."
    "Then at the chocolates again."
    dsp happy "I didn't see anything."
    dsp "Go. Before I change my mind. And put that suitcase back in one piece."

    # Scene 6: The guilt seed
    scene bg haven_venue with dissolve
    play music home fadeout 1.0
    show aarav happy at pos_mid

    a "I'm in."
    a "I actually did it. I'm at Haven!"

    show aarav neutral
    "Everyone else here filled the form on time."
    "He had followed a suitcase."

    show aarav sad
    play music heavy fadeout 1.0
    a "...So why does this feel like I just copied on an exam?"

    "The chocolates were gone in a minute."
    "The guilt wasn't."

    jump act2
