label sasha_use_condom:
    $ result = randint(0, 2)
    if result == 0 and game.room == "bedroom1":
        "But keen as I am to get something going between us, I still need to be careful."
        "And so I hold a hand up to halt Sasha while I reach for a condom on the bedside table."
        "At first she seems puzzled, even a little insulted by the delay in the proceedings."
        "Though this changes pretty quickly when she sees what I put it off for."
        "After that, Sasha waits patiently while I make myself ready down there."
    elif result == 2:
        "But that's when I remember something important."
        "And so I hold up a hand, wanting Sasha to wait a moment."
        if sasha.sub >= 25:
            if sasha.flags.mikeNickname:
                sasha.say "[hero.name], where are you going?!?"
            else:
                sasha.say "Master, where are you going?!?"
        elif sasha.sub <= -25:
            sasha.say "Hey, you're not going anywhere until you've done your duty!"
        else:
            sasha.say "Hey, [hero.name] - now you're taking the cock away!"
        mike.say "It's okay, Sasha..."
        mike.say "I just need to grab a condom, okay?"
        "I'm already rummaging around for the aforementioned condom as I say this."
        "And the revelation of what I'm doing seems to change Sasha's tune too."
        if sasha.sub >= 25:
            sasha.say "Ooh...good idea!"
        elif sasha.sub <= -25:
            sasha.say "Ah, I was just about to say that myself!"
        else:
            sasha.say "Oh yeah, I should have thought of that myself!"
        "I nod as I hurry back to the dresser with the condom in hand."
        "And as soon as I have the packet open, I slide it on."
        "Once that's done, we're ready to go."
    else:
        "But I have to make sure we play it safe."
        "So I hold up a hand to stop Sasha in her tracks."
        mike.say "Wait a minute, Sasha."
        mike.say "We should use some protection."
        "Sasha looks at me and blinks, like it'd totally slipped her mind."
        "Then she nods, urging me to take care of it as soon as I can."
        "I take the hint, grabbing a condom and slipping it on in record time."
        "That done, we're ready to go."
    return







label sasha_warn_condom:
    $ result = randint(0, 1)
    if result == 0:
        "Before I can pull Sasha down onto my cock, she wriggles out of my grasp."
        "Then I find a finger wagging in front of my face, as she scolds me."
        if sasha.sub < 25:
            sasha.say "Aren't we forgetting a little something?"
        else:
            sasha.say "Stop it, you silly goose!"
            sasha.say "You don't want to be a daddy, do you?"
    else:
        "But that's when Sasha holds up a hand to stop me."
        mike.say "What's up, Sasha?"
        mike.say "I thought you were desperate for it?"
        if sasha.sub >= 25:
            if sasha.flags.mikeNickname:
                sasha.say "Sorry, [hero.name]..."
            else:
                sasha.say "Sorry, Master..."
            sasha.say "But I just remembered that we need to use protection."
        elif sasha.sub <= -25:
            sasha.say "Yeah, but you're not getting anything without a condom."
        else:
            sasha.say "I know, but we really should use a condom."
    return

label sasha_force_condom:
    $ result = randint(0, 1)
    if result == 0:
        "At first I'm puzzled, even a little insulted by the delay in the proceedings."
        "Though this changes pretty quickly when I see Sasha holding up a condom."
        "After that, I wait patiently while she slips it on down there."
    else:
        sasha.say "Don't worry, I came prepared!"
        "I watch as Sasha slips out from in front of me."
        "And then she hurries to find the condom."
        "It doesn't take her long, and as returns as soon as she has it."
        "I tear the packet open and slide it on."
        "Once that's done, we're ready to go."
    return

label sasha_mad_condom:
    $ result = randint(0, 1)
    if result == 0:
        sasha.say "No protection, no sex."
        sasha.say "It's that simple, [hero.name]!"
        "I look at her in askance, unable to believe what she's saying."
        mike.say "Oh, come on, Sasha!"
        mike.say "Don't ruin the whole night being a prude."
        "Sasha snorts derisively at this, climbing off of me while shaking her head."
        "I try to make a grab for her, but she slaps my hands away and then she's gone."
    else:
        mike.say "What are you talking about, Sasha?"
        mike.say "Let's just forget about it and fuck!"
        mike.say "I promise I can pull out before I lose it, okay?"
        "Sasha looks at me in horror and she jerks herself away."
        "Shaking her head and putting some distance between us."
        if sasha.sub >= 25:
            if sasha.flags.mikeNickname:
                sasha.say "Oh no, [hero.name]..."
            else:
                sasha.say "Oh no, Master..."
            sasha.say "That's too much, even for me!"
        elif sasha.sub <= -25:
            sasha.say "I don't know where you get off telling me what to do!"
            sasha.say "Seems like you need to be taught some basic obedience!"
        else:
            sasha.say "You must have lost your mind!"
            sasha.say "So I'll come back once you find it again."
        "I watch in helpless silence as Sasha puts on enough of her clothes to be considered decent."
        "And then she storms out of the room, leaving me alone and frustrated."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
