label kylie_use_condom:
    if not kylie.sexperience:
        "If I'm going to be the guy of her dreams and take her virginity as she's always dreamed, the least I can do is not knock her up in the act!"
    if game.room == 'bedroom1':
        "I reach over and pluck one of the condoms off of the bedside table."
    else:
        "I pull a condom out of my secret compartment like a magician pulls a rabbit out of a hat."
    if kylie.yandere < 50 or kylie.love < 180:
        $ result = randint(1, 2)
        if result == 1:
            "Kylie stops for a moment, watching as I roll the condom over my fast rising cock."
            "While she doesn't applaud me for taking the time to do so, she doesn't complain about it either."
        if result == 2:
            "Just a thought occurs to me."
            "I hold up a hand to Kylie, asking her to wait a moment."
            "At first she looks puzzled, but then she sees the condom in my hand."
            "Kylie nods and waits patiently as I put it on."
        else:
            "But first things first - we need to take precautions."
            mike.say "Wait a second, Kylie."
            mike.say "We should really grab a condom!"
            "Kylie looks surprised at this, like it slipped her mind too."
            "But then she nods her head, watching me find one on the bedside table."
            "All it takes is a couple of seconds to get the thing on."
            "Then we're all set!"
    else:
        kylie.say "No - no protection!"
        "I look at her in askance, totally astounded by a girl refusing to let me use protection."
        if kylie.flags.unpilled:
            kylie.say "I am on the pill remember..."
        elif not kylie.sexperience:
            kylie.say "That was never part of how this is supposed to happen, [hero.name]."
            kylie.say "It has to be just how I imagined it!"
        menu:
            "Insist":
                if not kylie.sexperience and not kylie.flags.unpilled:
                    mike.say "I don't care how you imagined it, Kylie."
                mike.say "I'm not fucking you without it!"
                kylie.say "Then I guess you're not fucking me at all!"
                "With that, she begins to gather up her clothes and pull them on while making for the door."
                $ kylie.love -= 10
                return "leave_without_gain"
            "Accept":
                "I'm not going to be denied now, not when I'm this close!"
                "So I just shrug and toss the condom away."
                "Which sees a wicked smile spreads across Kylie's face in response."
                return False
    return

label kylie_intro_condom:
    "I know that I should be taking precautions, but I'm also getting swept along in Kylie's whole dream scenario at the same time."
    "I want this to be as perfect as possible, to live up to her expectations."
    "And so I reason that doing it without a condom would come closest to how she's imagined this whole thing playing out."
    return

label kylie_warn_condom:
    $ result = randint(1, 2)
    if result == 1:
        kylie.say "Okay..."
        kylie.say "Let's just break character for a moment."
        kylie.say "We need to use some protection, yeah?"
    else:
        kylie.say "Hold on, [hero.name]..."
        kylie.say "We should really use a condom!"
        "Kylie pulls away from me as she says this."
        "Enough to let me know that she's serious."
        "She's not going to give me anything until I put one on!"
    return

label kylie_force_condom:
    $ result = randint(1, 2)
    if result == 1:
        kylie.say "There's a condom in my purse over there."
        "Kylie nods in the direction of her clothes."
        "I leap off the bed in search of the condom."
        "Kylie nods and waits patiently as I put it on."
    else:
        kylie.say "Don't worry, I have one on me."
        "Kylie hops off the bed and retrieves the condom."
        "Then she hands it over to me."
        "All it takes is a couple of seconds to get the thing on."
        "Then we're all set!"
    return

label kylie_mad_condom:
    $ result = randint(1, 2)
    if result == 1:
        mike.say "Seriously, Kylie?"
        mike.say "I thought you were more adventurous than that!"
        kylie.say "Adventurous, yes."
        kylie.say "Stupid, no."
        kylie.say "I think I'd like you to untie me now."
        kylie.say "Something just killed the mood."
        "I think about protesting, but the look on Kylie's face stops me dead."
        "Instead I find myself doing as I'm told, and then watching as she gets dressed."
        "Kylie leaves me with one last, withering look before she walks out of the door."
        "And that's more than enough to put out the fire of my own lust."
    else:
        mike.say "Don't worry about it, Kylie."
        mike.say "Just this once, we won't use one!"
        "Kylie looks at me in amazement, shaking her head."
        "Then she hops off the bed and starts getting dressed."
        kylie.say "That's not adventurous, [hero.name]."
        kylie.say "It's just plain irresponsible."
        kylie.say "Call me when you're ready to apologise!"
        "And with that, she storms out of the room."
        "Which leaves me all alone for the sake of a single condom!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
