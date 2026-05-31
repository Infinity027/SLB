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

label shiori_intro_condom:
    $ result = randint(1, 4)
    if result == 1:
        "I might have been talking up the erection that I have right now for the sake of getting Shiori excited."
        "But I wasn't making that shit up just for her sake either."
        "I want my cock inside of her so badly right now, and I don't want anything to come between us when it's in there either!"
    elif result == 2:
        "Shiori's the only thing on my mind at that moment, and I just can't wait a second longer to have her."
        "Without stopping to do as much as draw breath, I thrust my cock upwards."

    return

label shiori_warn_condom:
    $ result = randint(1, 3)
    if result == 1:
        shiori.say "Oh, wait..."
        shiori.say "We should really use a condom!"
    elif result == 2:
        shiori.say "Oh, [hero.name], wait!"
        shiori.say "What about protection?"
        "I stop dead in my tracks as Shiori asks the question."
        "The thought really hadn't occurred to me!"
    else:
        shiori.say "[hero.name], wait!"
        shiori.say "Aren't you going to use a condom?"
        "Shiori's question puts a stop to everything."
        "And I need to answer it in order to get them moving again!"
        mike.say "Ah, no Shiori."
        mike.say "I guess not!"
        "Shiori looks surprised and also a little hurt."
    return

label shiori_force_condom:



    shiori.say "Don't worry..."
    shiori.say "I have one in my bag."
    shiori.say "Over there!"
    "It only takes me a few moments to find a condom."
    "And in a few seconds I have it on."
    "Then we're ready to go."
    return

label shiori_mad_condom:



    mike.say "Forget about that, Shiori!"
    mike.say "Let's just have some fun, okay?"
    "Shiori looks at me with a shocked expression."
    "Then she pushes me away and rolls off the bed."
    mike.say "Shiori!"
    mike.say "What are you doing?!?"
    "Shiori doesn't turn to look at me."
    "She just starts to get herself dressed."
    shiori.say "I...I thought you were different, [hero.name]."
    shiori.say "But you're just like all men."
    shiori.say "You're a selfish beast!"
    "Half-dressed, Shiori storms out of the room."
    "Leaving me alone and cursing myself."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
