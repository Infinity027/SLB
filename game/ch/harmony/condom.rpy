label harmony_use_condom:
    $ result = randint(1, 2)
    if result == 1 and game.room == "bedroom1":
        "With the stakes being this high, I'm not about to go taking any chances."
        "So I pause long enough to grab a condom from the pile on the bedside table."
        "Harmony makes no objection to the delay, and seems happy to wait."
        "A couple of seconds later, I'm all ready to go."
    else:
        "But I have to make sure we play it safe."
        "So I hold up a hand to stop Harmony in her tracks."
        mike.say "Wait a minute, Harmony."
        mike.say "We should use some protection."
        "Harmony looks at me and blinks, like it'd totally slipped her mind."
        "Then she nods, urging me to take care of it as soon as I can."
        "I take the hint, grabbing a condom and slipping it on in record time."
        "That done, we're ready to go."
    return

label harmony_intro_condom:
    "Pulling my shorts down, I prepare myself for the more than pleasant task ahead."
    return

label harmony_warn_condom:
    "But then I hear a quiet but insistent cough from Harmony below me."
    return

label harmony_force_condom:
    "Harmony holds up a condom, and I take it from her sheepishly."
    "It feels bad to have been reminded of such a basic precaution."
    "And doubly so from someone as innocent as Harmony!"
    "But a couple of seconds later, it's on and I'm ready to go."
    return

label harmony_mad_condom:
    harmony.say "[hero.name], whatever are you thinking?"
    harmony.say "You know how sensitive I am about this kind of thing!"
    harmony.say "Where's the condom?"
    mike.say "Oh come on, Harmony!"
    mike.say "What are the chances of you getting pregnant anyway?"
    "At this, Harmony's eyes become wide with disbelief and anger."
    "She pushes me off of her and roll to the edge of the bed."
    "Grabbing her clothes, she storms out of the room, leaving me alone and frustrated."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
