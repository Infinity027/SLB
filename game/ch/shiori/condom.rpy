label shiori_use_condom:
    $ result = randint(1, 5)
    if result == 1 and game.room == "bedroom1":
        "I pause just long enough to grab a condom from the bedside table and slide it over my cock."
        "Shiori already has one kid, and there's no way I want to become father to her second by accident."
        "Whether or not she approves of me wearing it, she makes no sound of protest."
    elif result == 2 and game.room == "bedroom1":
        "I'm about to press on, when I happen to glance at the condoms on the bedside table."
        "It only takes a moment to release Shiori grab one and slip it on, which is far better than the potential alternative."
        "I tie her up in my arms once more, and prepare to get down to business."
    elif result == 3 and game.room == "bedroom1":
        "It's just then that I remember something pretty important."
        "I hold up a hand, asking Shiori to wait a moment."
        "She looks puzzled, but nods all the same."
        "But when she sees me grab a condom from the bedside table, she nods again."
        "I hastily put the thing on, and we're all set to go."
    elif result == 4 and game.room == "bedroom1":
        mike.say "Just a second, Shiori."
        "Huh - what's the matter, [hero.name]?"
        "Shiori watches as I reach for a condom from the bedside table."
        "Her question answered, she nods as I put it on."
        "And a moment later we're ready to go."
    else:
        mike.say "Shiori..."
        mike.say "Just wait a moment."
        "At the mere mention of a delay, Shiori looks worried."
        shiori.say "What's the matter, [hero.name]?"
        mike.say "Don't worry, Shiori."
        mike.say "I just want to get a condom, that's all."
        "The look of relief on Shiori's face is instant."
        "And her smile is genuine too."
        shiori.say "Of course!"
        shiori.say "You go grab one."
        "It only takes me a few moments to find a condom."
        "And in a few seconds I have it on."
        "Then we're ready to go."
    return
