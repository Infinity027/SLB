label kiara_use_condom:
    $ result = randint(1, 2)
    if result == 1:
        "But then I remember that there's something else I need to take care of first."
        "And so I quickly make to roll out from under Kiara and retrieve it from my bedside table."
        "Though I only manage to wriggle once before she pins me down with all of her weight."
        if kiara.sub >= 25:
            kiara.say "Wait..."
            kiara.say "What are you doing?"
        elif kiara.sub < -25:
            kiara.say "Oh no, no, no..."
            kiara.say "I did not give you permission to go anywhere!"
        else:
            kiara.say "[hero.name]…"
            kiara.say "What could be more important than this?"
        "I smile and shake, my head, trying to assure her there's nothing wrong."
        mike.say "Whoa..."
        mike.say "Calm down, Kiara - I just want to get a condom!"
        "I gesture the bedside table to make my point."
        "And that seems to be more than enough to reassure her."
        "Because her mood seems to improve and she nods her head eagerly, letting me up."
        "Hell, she even helps me to open the packet and get the thing on."
        "And with that done, we're back in business."
    else:
        "I'm all ready to go, fixated on my target and not about to let anything get in my way."
        "But then I stop in my tracks, as I suddenly remember something important that I've forgotten."
        "Kiara seems to notice this instant change in mood, and waves to get my attention."
        kiara.say "What is it, [hero.name]?"
        kiara.say "Is there something wrong?"
        "I shake my head as I make to get up, trying to reassure Kiara everything's fine."
        mike.say "Nothing to worry about, Kiara..."
        mike.say "I just need to take care of something."
        mike.say "Won't take a minute, I promise."
        "Kiara looks like she's about to say more, but I'm already up and off."
        "But true to my word, it only takes me a moment to find what I'm looking for."
        mike.say "Ta da!"
        kiara.say "A condom?"
        kiara.say "Oh yes, that is a good idea."
        "Kiara nods as I hurry back to her and hand it over."
        "She tears open the packet and helps me to get it on."
        "Then we're all set, back in position and ready to go."
    return
