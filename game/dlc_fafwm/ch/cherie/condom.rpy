label cherie_use_condom:
    $ result = randint(1, 2)
    if result == 1:
        "I'm all set and ready to go, raring to get it on with Cherie."
        "But then I remember something important, and I hold up a hand."
        if cherie.sub >= 66:
            cherie.say "[hero.name]..."
            cherie.say "What is wrong?"
        else:
            cherie.say "What..."
            cherie.say "What is the matter, [hero.name]?"
        "I give Cherie a reassuring smile as I reach for what I need."
        mike.say "No need to panic, Cherie..."
        mike.say "I just remembered that we need a condom, that's all."
        "Cherie nods as I explain myself to her, and in a moment I've grabbed to condom."
        "And as soon as it's on, we get right back down to business."
    else:
        "But then, at the last possible moment, I remember something important."
        "And so I hold a hand up to Cherie as I back off a little way."
        cherie.say "What is the matter, mon ami?"
        cherie.say "Is there something wrong?"
        "By the time Cherie's asked her questions, I'm already at the bedside table."
        "So by way of an answer, I pluck the condom I was looking for off the surface."
        "Then I wave it in the air for her to see as I hurry back to my former position."
        cherie.say "Oh, but of course..."
        cherie.say "We should be using protection!"
        "It doesn't take me long to get the condom out of the packet."
        "Then I slide it on and get back down to business."
    return
