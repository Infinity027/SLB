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
