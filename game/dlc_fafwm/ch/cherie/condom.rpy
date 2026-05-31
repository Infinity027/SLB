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

label cherie_intro_condom:
    "Everything seems to be in place, and we're all ready to go."
    "I'm finally right where I want to be, with Cherie on the same page."
    "I feel like I've been waiting for this moment so long it's unreal."
    "And there's part of me that wants to pinch myself to make sure I'm not dreaming."
    "Though another part of me is too wary to even risk as much as that."
    return

label cherie_warn_condom:
    $ result = randint(1, 2)
    if result == 1:
        "But before I can make my first move, Cherie holds up a hand to stop me."
        if cherie.sub >= 66:
            cherie.say "I am sorry, [hero.name]..."
            cherie.say "But I think there is something that you have forgotten!"
        else:
            cherie.say "Wait a second, [hero.name]..."
            cherie.say "There is something that we have forgotten!"
        mike.say "Huh..."
        mike.say "What are you talking about?"
        cherie.say "A condom, {i}mon ami{/i} - we need to use a condom!"
    else:
        "But then, at the last possible moment, Cherie raises a hand in the air."
        "And she waves it about frantically, clearly trying to get my attention."
        mike.say "What's the matter, Cherie?"
        mike.say "Did we forget something important?"
        "Cherie nods her head at this."
        cherie.say "But of course, mon ami…"
        cherie.say "We have not remembered to use a condom!"
    return

label cherie_force_condom:
    $ result = randint(1, 2)
    if result == 1:
        "Before I can protest, Cherie extricates herself from my grasp."
        "And then she hops out of reach, rummaging around in her things."
        show cherie normal
        if cherie.sub >= 66:
            cherie.say "Sorry for the delay, [hero.name]..."
        else:
            cherie.say "Here we are!"
        cherie.say "But now I have what we need!"
        "Cherie hurries back over to me, already opening the packet."
        "And as soon as it's on, we get right back down to business."
    else:
        cherie.say "Do not worry..."
        cherie.say "I have one right here."
        "Cherie proceeds to crawl on her hands and knees to the pile of clothes she's discarded."
        "And the sight of that alone is more than enough to keep me quiet while she hunts for the condom."
        "But as soon as she finds it, Cherie retraces her steps and gets herself back into position."
        "Then she hands it over to me and it doesn't take me long to get the condom out of the packet."
        "That done, I slide it on and get back down to business."
    return

label cherie_mad_condom:
    $ result = randint(1, 2)
    if result == 1:
        mike.say "Are you actually serious, Cherie?"
        mike.say "Just forget about the damn condom..."
        mike.say "And let's get on with it already!"
        scene expression f"bg {game.room}"
        show cherie stuned naked at center, zoomAt(1.25, (640, 880))
        with hpunch
        "Cherie looks at me in horror, and then she shoves me away from her."
        if cherie.sub >= 66:
            show cherie whining
            cherie.say "I am sorry, {i}mon ami{/i}..."
            show cherie talkative
            cherie.say "I would do anything that you asked of me - except for that!"
            show cherie normal
        else:
            show cherie angry
            cherie.say "I cannot believe what I am hearing!"
            show cherie annoyed
            cherie.say "If you will not use protection, then there will be no sexy-time!"
            show cherie upset
        mike.say "Cherie, please!"
        show cherie upset
        "I do the best I can to plead with Cherie."
        "But my words fall on deaf ears as she gets up and pulls on her clothes."
        hide cherie with easeoutright
        "And then she storms out, leaving me alone and unfulfilled."
    else:
        mike.say "There's no time for that now, Cherie..."
        mike.say "Not if you want me to fuck you senseless!"
        "The moment the words are out of my mouth, I know that I've made a big mistake."
        scene expression f"bg {game.room}"
        show cherie upset naked at center, zoomAt(1.25, (640, 880))
        with hpunch
        "Because the expression on Cherie's face becomes one of anger and annoyance."
        "And she takes advantage of me looking her in the eye a moment later."
        with vpunch
        "As she aims a pretty vicious kick right at my groin."
        mike.say "Urgh!"
        mike.say "What the fuck?!?"
        with vpunch
        "Cherie doesn't catch me square in the balls, instead clipping them and hitting me in the stomach instead."
        "But the effect is more than enough to make me collapse onto my ass, groaning in pain."
        "And she instantly uses the distraction to get up and start pulling on her clothes."
        show cherie angry underwear
        cherie.say "No, no, no..."
        cherie.say "You will not be doing anything to me tonight, mon ami…"
        cherie.say "Not without protection!"
        show cherie upset
        "I hold out a hand, trying to appeal to Cherie to stop."
        "Hoping that we can maybe talk about it and sort something out."
        "But she seems to be set on making a dramatic exit."
        hide cherie with easeoutright
        "As she storms out of the door as soon as she's half-way decent."
        "Leaving me to roll around on the floor, still clutching at my aching gut."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
