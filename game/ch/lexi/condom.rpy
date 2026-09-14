label lexi_use_condom:
    $ result = randint(1, 4)
    if result == 1 and game.room == "bedroom1":
        "My cock's more than ready to go right now."
        "But I need to take a moment, just to be safe."
        "I grab a condom from the bedside table, and slip it on."
        if lexi.flags.drugs:
            "Lexi's glazed eyes hardly seem to register the momentary delay anyway."
        else:
            "Lexi seems impatient for me to get started, but doesn't complain at the delay."
    elif result == 2 and game.room == "bedroom1":
        lexi.say "Mmm..."
        lexi.say "I want this in me so bad!"
        mike.say "Yeah, but wait a minute..."
        mike.say "We should use a condom!"
        "Lexi nods in agreement."
        "But I know that I've got to do this quickly."
        "Luckily for me I have a stash in a nearby drawer."
        "And I can grab one really fast."
        "As soon as it's on, we're ready to go."
    elif result == 3 and game.room == "bedroom1":
        mike.say "Hold on a minute, Lexi."
        lexi.say "Huh..."
        lexi.say "What's the hold-up?!?"
        "I reach over to the bedside table and snatch up a condom."
        "As soon as she sees it in my hand, Lexi nods and lets me get on with it."
        "A second or two later, it's on and we're ready to go for real."
    else:
        "But I have to make sure we play it safe."
        "So I hold up a hand to stop Lexi in her tracks."
        mike.say "Wait a minute, Lexi."
        mike.say "We should use some protection."
        "Lexi looks at me and blinks, like it'd totally slipped her mind."
        "Then she nods, urging me to take care of it as soon as I can."
        "I take the hint, grabbing a condom and slipping it on in record time."
        "That done, we're ready to go."
    return

label lexi_drugs_condom:
    "Lexi's eyes are glazed over by now, meaning she's hardly aware of what's going on."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
