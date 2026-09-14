label bree_use_condom:
    $ result = randint(1, 2)
    if result == 1:
        if game.room == 'bedroom3':
            bree.say "You'd better put something on that thing."
            bree.say "Or else you're not coming any closer to me with it!"
            mike.say "You're right, [bree.name]."
            mike.say "Just one problem."
            "I look around and shrug."
            mike.say "Erm..."
            mike.say "This isn't my room, [bree.name]."
            mike.say "I have no idea where Sasha keeps her stuff!"
            "[bree.name] shakes her head and smiles."
            bree.say "No - but I do!"
            bree.say "She keeps them in that drawer."
            bree.say "The one over there!"
            "I follow [bree.name]'s directions and hastily grab a condom."
            "Then I slide it on and clamber back onto the bed."
        else:
            "But then I remember something important."
            mike.say "Wait a minute, [bree.name]..."
            mike.say "I just need to grab a condom."
            "[bree.name] nods as soon as she hears this."
            bree.say "Oh..."
            bree.say "Okay - good thinking."
            "I know that I have one in my wallet."
            "So it only takes me a moment to grab it."
            "And once it's on, we're ready to go."
    else:
        "But first things first."
        mike.say "[bree.name]..."
        mike.say "We need some protection first."
        bree.say "You mean like a safety harness?!?"
        mike.say "No, I mean like a condom!"
        bree.say "Oops...sorry!"
        "[bree.name] waits patiently while I grab a condom from the beside table."
        "It only takes me a couple of seconds to get it out and slide it on."
        "And then we're straight back into the action."
    return
