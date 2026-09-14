label claire_use_condom:
    $ result = randint(1, 2)
    if result == 1:
        "I don't know how, but by some minor miracle, my brain manages to function for a second."
        "And in that moment I remember that there's something I've forgotten."
        "Which makes me stop what I'm doing and start to climb off the bed."
        "But as I do so, Claire reaches out with one hand, grabbing hold of my wrist."
        if claire.sub >= 25:
            claire.say "What's the matter?"
            claire.say "Where are you going?!?"
        else:
            claire.say "Hold it right there, mister..."
            claire.say "I thought you were about to deliver?"
        "I shake my head and give Claire what I hope is a reassuring smile."
        mike.say "I'm just grabbing a condom, Claire..."
        mike.say "Can't forget something as important as that!"
        "As soon as I've explained myself, Claire nods and lets me go."
        "Which means that I can hop off the bed and grab a condom."
        "Then together we open the packet and put the thing on."
    else:
        "We're just about ready to go, all lined up and about to do it."
        "But that's when I realise that I've gone and forgotten something."
        mike.say "Oh...hang on, Claire!"
        "Claire looks puzzled by my sudden change of course."
        "And she frowns as I hurry away from her."
        "Clearly not happy with this new turn of events."
        claire.say "Hey - where are you going?"
        "I kind of choose to ignore what Claire's saying."
        "Because I've already found what I was looking for."
        "When I hold up the condom, the look on her face changes to one of recognition."
        "And she's nodding eagerly as I make my way back over to her."
        "Once there, I don't waste any time in tearing open the wrapper."
        "As soon as it's on, we're back in business and ready to go!"
    return
