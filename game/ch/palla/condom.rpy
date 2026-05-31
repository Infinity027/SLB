label palla_use_condom:
    $ result = randint(1, 2)
    if result == 1:
        "I only pause long enough to slip a condom on, before lining myself up with Palla's exposed pussy. And then I thrust it in."
        "I want to take it slow, but I'm so turned on I just can't, and I go all the way in on the first try."
    else:
        "I only pause long enough to slip a condom on, before lining myself up with Palla's exposed pussy."
        palla.say "What's going on back there?"
        "Without explaining a single thing to her, I thrust forwards and force myself into her with some considerable urgency."
        palla.say "Wha...aaa...aaah!"
    return

label palla_intro_condom:


    "But it's in the very next moment that I remember I forgot something."
    "And it's something important too."
    mike.say "Hold that thought, Palla!"
    "As I leap off the bed, Palla props herself up on her elbows."
    "And she doesn't look too impressed with me as she does so either."
    palla.say "[hero.name]..."
    palla.say "What are you doing?!?"
    palla.say "Get back here this instant!"
    "Already back to where I dropped my pants, I hold up a hand to calm Palla."
    mike.say "I'll be right there, Palla..."
    mike.say "Just needed to grab this."
    "As I hold up my other hand, Palla sees the condom for the first time."
    "And in turn, I see an instant change in her demeanour."
    palla.say "Oh..."
    palla.say "Well why didn't you just say so?"
    "Ignoring Palla's attempts to save face, I jump back onto the bed."
    "All it takes is a couple of seconds, and the condom is on."
    "And then we can get right back to it."

    return

label palla_warn_condom:


    "But then Palla puts up a hand to stop me."
    mike.say "What the..."
    mike.say "What's the matter now?"
    show palla vangry at startle(0.1, 5)
    palla.say "Aren't you forgetting something?"
    palla.say "What about the condom?"

    if palla.love >= 80:
        palla.say "After all, it doesn't matter"

    return

label palla_force_condom:


    "Before I can say another word, Palla slides out from under me."
    "Then she hurries to one of the bedside drawers."
    show palla talkative at startle(0.5, 1)
    palla.say "Don't worry..."
    if game.room == "shawnbedroom":
        palla.say "I know where Shawn keeps his stash."
        palla.say "And he's not likely to run out any time soon!"
    else:
        palla.say "I have some right here!"
    "Palla grabs a condom and then hops back onto the bed."
    "All it takes is a couple of seconds, and the thing on."
    "And then we can get right back to it."

    return

label palla_mad_condom:


    "I can't actually believe that Palla's putting the breaks on right now."
    "Not after she's been leading me on in the way she has."
    "And all for the sake of a damn condom!"
    mike.say "Oh come on, Palla..."
    mike.say "You can't be serious, can you?"
    mike.say "Just forget about it this one time, yeah?"
    mike.say "I mean, this can't be the first time you've been ridden bare-back!"
    show palla angry
    "I watch as Palla's expression darkens and she narrows her eyes."
    "Then she thrusts her hand upwards, shoving me aside and off of her."
    mike.say "WHOA!"
    show palla at center, traveling(1, 0.5, (640, 720))
    show palla underwear topless with dissolve
    "I go tumbling off the bed and onto the floor, landing in a heap."
    hide palla
    show palla underwear with dissolve
    "At the same time, Palla leaps up and begins to snatch up her clothes."
    show palla vangry
    palla.say "You really see me that way, [hero.name]?"
    palla.say "As some kind of cheap slut?"
    palla.say "One that you can just shoot your load into whenever you fancy it?!?"
    show palla angry
    mike.say "Palla..."
    mike.say "No I..."
    mike.say "I didn't mean to..."
    show palla vangry
    palla.say "Oh shut the fuck up."
    palla.say "And let yourself out."
    hide palla with easeoutleft
    pause 1
    play sound door_close
    "Palla storms out of the room, leaving me sitting naked on the floor."
    "Naked and painfully aware of the fact that I just blew it, big time."

    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
