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
