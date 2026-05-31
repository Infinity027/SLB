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

label claire_intro_condom:
    "We're all ready to go, everything lined up and in place."
    "And I can honestly say that all of my attention is on the task ahead of me."
    "There's nothing that I want more than to get things underway."
    "And I'm hoping that Claire's on the same page too."
    "Because I don't know what I'll do if I don't get what I want in the next couple of minutes!"
    return

label claire_warn_condom:
    $ result = randint(1, 2)
    if result == 1:
        "That's when Claire holds up a hand to stop me."
        mike.say "Huh?"
        mike.say "What's the matter, Claire?"
        mike.say "I hope you're not getting cold feet!"
    else:
        "But before I can leap on her, Claire holds up a hand."
        "Which has the frustrating effect of stopping me in my tracks."
        claire.say "Wait, [hero.name]..."
        claire.say "We should really use some protection."
        "And from the look on her face, I can tell she's totally serious."
        "I'm not getting on inch further without using one."
    return

label claire_force_condom:
    $ result = randint(1, 2)
    if result == 1:
        "Claire shakes her head as she manoeuvres out from under me."
        claire.say "Of course not."
        claire.say "I just remembered that we need some protection."
        "I watch as Claire slides off the bed and heads over to the pile of her clothes on the floor."
        "She quickly locates the condom that she's looking for and hurries back over to me."
        "Then together we open the packet and put the thing on."
    else:
        "I'm about to object when Claire leaps up and hurries over to her clothes."
        "Then I watch as she rummages in her purse until she finds something."
        "And when she finally holds up a condom, I feel a genuine sense of relief."
        "Claire hurries back with it in her hand, and we're soon tearing the packet open."
        "As soon as it's on, we're back in business and ready to go!"
    return

label claire_mad_condom:
    $ result = randint(1, 2)
    if result == 1:
        "Claire shakes her head."
        claire.say "No, of course not!"
        claire.say "But we should use a condom."
        "I can't help but sigh and roll my eyes at the suggestion."
        "Seeing it as a barrier between me and what I so desperately want."
        mike.say "Nah..."
        mike.say "Forget about the condom, Claire."
        mike.say "Let's just go for it, yeah?"
        scene expression f"bg {game.room}"
        show claire stuned naked at center, zoomAt(1.25, (640, 880))
        with hpunch
        "Claire looks at me like I've taken leave of my senses."
        "And then she quickly wriggles her way out from under me."
        show claire angry
        claire.say "I honestly can't believe what I'm hearing."
        claire.say "I thought you were more responsible than this."
        show claire upset
        "By now she's already made it to her clothes and started to get dressed."
        mike.say "Oh come on, Claire..."
        mike.say "I thought that we were making fantasy into reality!"
        show claire angry
        claire.say "Well you'll have to talk to your right hand about that, won't you."
        claire.say "Because I'm leaving, at least until you learn how to behave!"
        show claire upset
        pause 0.3
        hide claire with easeoutright
        "With that, Claire storms out, leaving me alone and extremely frustrated."
    else:
        mike.say "Ah, just forget it this once, claire!"
        scene expression f"bg {game.room}"
        show claire stuned naked at center, zoomAt(1.25, (640, 880))
        with hpunch
        "Claire looks at me like she can't believe what she's hearing."
        "And then she starts to move away from me, shaking her head."
        show claire angry
        claire.say "Well that's me soured on this whole deal!"
        claire.say "You've gone and totally spoiled my mood."
        claire.say "So I think I'll be on my way home."
        show claire upset
        "I watch in helpless silence as Claire pulls on her clothes."
        hide claire with easeoutright
        "And then let out a tortured groan as she walks out of the door too."
        "Realising that I just cheated myself out of some serious fun."
        "And all for the sake of one lousy condom!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
