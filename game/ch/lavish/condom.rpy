label lavish_use_condom:
    $ result = randint(1, 2)
    if result == 1 and game.room == "bedroom1":
        "All I need to do is slip a little something on first."
        "I take a moment to grab a condom from the bedside table."
        "And as soon as she sees what I'm doing, Lavish nods in agreement."
        "A few moments later it's on and we're ready to go."
    else:
        "It's hard to focus on anything but the flower before me, flushed bright pink and gleaming."
        "My eyes stay locked on it as I strip out of my clothes, a man in a daze."
        "It takes me two seconds flat to retrieve a condom and slide it on."
        "I'm not wasting any time."
    return






label lavish_warn_condom:
    $ result = randint(1, 2)
    if result == 1:
        lavish.say "Aren't you forgetting something?"
        "Lavish's question stops me in my tracks."
        "And for a moment I can't think what she means."
        lavish.say "Shouldn't we be using some protection?"
    else:
        "But as I take my cock into my hand and step toward her, her lips curl into a wolfish smirk, and she lifts one finger from her wet folds and wags it back and forth."
        "Nuh uh."
    return

label lavish_force_condom:
    $ result = randint(1, 2)
    if result == 1:
        "Lavish leans off the edge of the bed and fumbles around in her pockets."
        "She returns a moment later, waving a condom under my nose."
        mike.say "Oh, I see!"
        "I take the condom from her and hurry to put it on."
        "Now we really are all ready to go!"
    else:
        lavish.say "Not yet."
        "She throws me a condom while saying that."
        "I almost groan out loud, but I respect the boundary, quickly catching the condom and sliding it on."
    return

label lavish_mad_condom:
    mike.say "Can't we just forget about it this one time?"
    "Lavish lets out a snort of derision and shakes her head."
    "She climbs off the bed and begins to get dressed."
    lavish.say "You know what, [hero.name]..."
    lavish.say "Maybe we can forget about the sex too!"
    "It doesn't take long for her to dress and storm out on me."
    "And all of my apologies and pleas fall on deaf ears."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
