label samantha_use_condom:
    $ result = randint(1, 4)
    if result == 1 and game.room == "bedroom1":
        "But eager as we both are, that's no excuse to take risks."
        if samantha.flags.nickname == "cupcake":
            mike.say "On the table by the bed, Cupcake..."
        else:
            mike.say "On the table by the bed, Sam..."
        samantha.say "Huh?"
        mike.say "The condoms, they're on the bedside table!"
        samantha.say "Oh yeah - good thinking!"
        "Sam leans over and grabs a condom."
        "Then she opens the packet and slides it onto my cock."
        "That done, we're ready to go."
    elif result == 2:
        "Suddenly I stop in my tracks, slapping my forehead."
        samantha.say "What's the matter, [hero.name]?"
        samantha.say "You get a cramp or something?"
        if samantha.flags.nickname == "cupcake":
            mike.say "No, Cupcake..."
        else:
            mike.say "No, Sam..."
        mike.say "I just remembered we need to use a condom."
        samantha.say "Oh yeah."
        samantha.say "Good thinking!"
        "It only takes me a couple of seconds to grab a condom."
        "And as soon as it's on, we're good to go."
    elif result == 3:
        mike.say "Uh..."
        mike.say "We should..."
        mike.say "We should use a condom!"
        "Sam stops in her tracks, like she'd totally forgotten."
        "And then she nods in agreement."
        samantha.say "Sure, sure - let's get one on there."
        samantha.say "I never had that problem when this was all just in my head!"
        "Sam waits patiently while I grab a condom and tear open the packet."
        "Then she helps me to roll it down over my cock."
        "That done, we're ready to go!"
    else:
        "But first I need to make sure that we take the appropriate precautions."
        "So I hold up a hand as I climb off the bed, heading for the bedside table."
        mike.say "Just a second, Sam..."
        mike.say "I need to grab something."
        "Sam looks up with genuine surprise written all over her face."
        "And who can blame her, as I'm sure no guy ever lost interest in her at this point before."
        if samantha.sub >= 50:
            samantha.say "Where are you going, [hero.name]?"
            samantha.say "Did I do something wrong?"
        else:
            samantha.say "What are you doing?"
            samantha.say "Is something wrong?"
        "By the time Sam's said all of this, I've found what I was looking for."
        "And when I hold up the condom, I see her expression turn into one of relief."
        "She nods eagerly as I return, already tearing open the packet."
        "Then she helps me to get it on, and we're good to go."
    return
