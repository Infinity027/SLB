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







label bree_warn_condom:
    $ result = randint(1, 3)
    if result == 1:
        bree.say "Wait a minute..."
        bree.say "We need to use a condom!"
    elif result == 2:
        bree.say "You'd better put something on that thing."
        bree.say "Or else you're not coming any closer to me with it!"
    else:
        bree.say "Wait a minute, [hero.name]!"
        bree.say "We should use some protection."
        mike.say "Like what?"
        mike.say "A safety harness?!?"
        bree.say "No, dumbass!"
        bree.say "Like a condom!"
    return

label bree_force_condom:
    $ result = randint(1, 3)
    if result == 1 and game.room == "bedroom3":
        bree.say "Sasha keeps them in that drawer."
        bree.say "The one over there!"
        "I follow [bree.name]'s directions and hastily grab a condom."
        "Then I slide it on and clamber back onto the bed."
    elif result == 2:
        bree.say "It's okay..."
        bree.say "I got one in my pocket."
        "[bree.name] shuffles over to her clothes."
        "Then she shuffles back with the condom."
        "And once it's on, we're ready to go."
    else:
        bree.say "Don't worry, I brought one myself."
        "[bree.name] hops off the bed and rummages around in her clothes."
        "Then she hops back on with the condom in hand."
        "I wait patiently as she opens the packet and slides it on."
        "And then we're straight back into the action."
    return

label bree_mad_condom:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Aw, come on, [bree.name]!"
        mike.say "Stop trying to put the brakes on this thing!"
        bree.say "Hey!"
        bree.say "The deal was that I let you fuck me."
        bree.say "Not let you knock me up!"
        "[bree.name] rolls over and grabs her clothes."
        bree.say "That's it, [hero.name]."
        bree.say "The deal's off."
        bree.say "Go jerk your own joystick!"
    elif result == 2:
        "I shake my head and scowl at [bree.name]."
        mike.say "What the hell, [bree.name]?"
        mike.say "I thought you wanted to live dangerously?"
        bree.say "Dangerously, [hero.name]."
        bree.say "Not stupidly!"
        "[bree.name] pushes me off her."
        "And then she climbs off the bed and starts to get dressed."
        bree.say "You might as well put that thing away."
        bree.say "Because I'm not in the mood anymore!"
    else:
        mike.say "Really, [bree.name]?"
        mike.say "I thought we were getting crazy tonight?"
        mike.say "You know, living dangerously?"
        "[bree.name] rolls her eyes and sighs in disgust."
        "She climbs off me and then off the bed too."
        bree.say "Yeah well..."
        bree.say "There's a difference between crazy and stupid."
        bree.say "And you just crossed over the into stupid."
        bree.say "I think I'll sleep in my own room tonight, okay?"
        "By now [bree.name] has most of her clothes on and she's headed for the door."
        "I can tell from the tone of her voice that there's no point in arguing."
        "Once she's gone and I'm on my own, all I can do is curse my own stupidity."
        "Looks like I went and ruined what could have been a perfect night."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
