label aletta_use_condom:
    $ result = randint(1, 4)
    if result == 1 and game.room == "bedroom1":
        "But let's not get ahead of ourselves here - safety first!"
        "I grab a condom from the bedside table before going any further."
        "The temporary delay doesn't seem to bother Aletta in the slightest."
        "Instead she eyes my cock almost wantonly as I slide the thing on."
    elif result == 2 and game.room == "bedroom1":
        "At the last moment, I remember to reach out and grab a condom from the ashtray on the bedside table."
        "I hand it to Aletta, and she nods without saying a word as she tears open the packet."
        "I can't see what she's doing as she reaches down to slip it over my cock."
    elif result == 3 and game.room == "bedroom1":
        "I use the moment of exposing Aletta's pussy to reach out and grab a condom from the bedside table."
        "She's so wrapped up in waiting to see just what I'll do next that she doesn't even notice the pause."
        "Which means that I have it out of the packet and on my cock before Aletta's any the wiser."
    else:
        "But I have to make sure we play it safe."
        "So I hold up a hand to stop Aletta in her tracks."
        mike.say "Wait a minute, Aletta."
        mike.say "We should use some protection."
        "Aletta looks at me and blinks, like it'd totally slipped her mind."
        "Then she nods, urging me to take care of it as soon as I can."
        "I take the hint, grabbing a condom and slipping it on in record time."
        "That done, we're ready to go."
    return

label aletta_intro_condom:
    $ result = randint(1, 5)
    if result == 1:
        "And I can't resist the siren call of a pussy the likes of this one!"
        "I lean in as quickly as I can, angling my cock towards Aletta's lips."
    elif result == 2:
        "My mind's not able to focus on anything apart from the amazing feeling of Aletta's slick crotch as she slithers around atop me."
        "All it takes is one or two subtle moves on her part, and she has me just where she wants me."
        "I suppose it's a happy coincidence that's right where I want to be right now too."
    elif result == 3:
        "It's at that very second that Aletta looks at me."
        "From the look in her eyes, she's clearly expecting me to do something right now."
        "But for the life of me, I'm just not sure what it is."
    elif result == 4:
        "Aletta seems to know exactly what she wants."
        "And it looks like she knows how to get it too!"
    else:
        "It seems like I'm the one in charge here, and so I step up and take control."
        "I grab Aletta by the haunches and pull her suddenly backwards."
        "She yelps in surprise and then in delight as my cock pushes between her thighs."
        "And in that moment, both of us know just where this is going!"
    return

label aletta_warn_condom:
    $ result = randint(1, 3)
    if result == 1:
        aletta.say "Hold on there, [hero.name]."
        aletta.say "Aren't you forgetting a little something?"
        "Aletta holds up a condom in its wrapper and offers it to me."
    elif result == 2:
        aletta.say "I see you got carried away and forgot to take precautions, [hero.name]."
        aletta.say "Don't worry about it, I'm kind of flattered!"
    else:
        "But then she pauses, as if remembering something important."
        aletta.say "Wait a minute, [hero.name]."
        aletta.say "We really should use a condom."
    return

label aletta_force_condom:
    $ result = randint(1, 3)
    if result == 1:
        "Let's not get ahead of ourselves here - safety first!"
        "I grab a condom from Aletta before going any further."
        "The temporary delay doesn't seem to bother her in the slightest."
        "Instead she eyes my cock almost wantonly as I slide the thing on."
    elif result == 2:
        aletta.say "Just grab one from my purse and let's get on with it, okay?"
        "I hurry to do as I'm told, ashamed to have forgotten something so important."
        "But at the same time feeling relieved that Aletta could see the funny side of it too!"
    else:
        "I look at Aletta and blink, because it totally slipped my mind."
        "She smiles knowingly, then waves a condom in front of my eyes."
        "I take the hint, grabbing the condom and slipping it on in record time."
        "That done, we're ready to go."
    return

label aletta_mad_condom:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Geez, Aletta - that's a real mood-killer!"
        "Aletta frowns at this, and I can already sense I've said the wrong thing."
        aletta.say "Not as much of a mood-killer as a positive pregnancy test!"
        aletta.say "No condom, no sex - it's as simple as that."
        mike.say "You're joking, right?!?"
        "Aletta rolls her eyes in disgust as she shoves me off of her."
        "I watch as she gets up and starts to pull on her clothes."
        "The best signal there is to say that this thing is well and truly over."
    elif result == 2:
        "Aletta offers me a cold stare."
        mike.say "What the hell, Aletta?"
        mike.say "One minute you're practically begging for it."
        mike.say "And then the next, you're going frigid on me!"
        aletta.say "Huh, is that so?"
        aletta.say "Well, I'm not so cock-hungry that I'm going to let you fuck me without protection!"
        mike.say "Aletta, you're killing the mood!"
        aletta.say "No, [hero.name] - you've already done that yourself!"
        "As she says this, Aletta climbs off of the bed and begins to hunt for her clothes."
        "All I can do is watch as my cock withers in bitter disappointment."
    else:
        mike.say "Aw, who has time for that, Aletta?"
        mike.say "Let's just have some fun, yeah?"
        mike.say "You can always get the morning-after pill!"
        "Aletta shakes her head and rolls her eyes at this."
        "Then she climbs off me and starts to get dressed."
        aletta.say "Well done, [hero.name]."
        aletta.say "You really killed the mood there!"
        "With that, she strides out of my office."
        "Leaving me with only my sexual frustration for company."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
