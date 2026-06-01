
label ayesha_intro_condom:
    $ result = randint(1, 2)
    if result == 1:
        "My mind is so caught up with the need to make Ayesha comfortable, that I forget almost everything else."
    else:
        "I want Ayesha's pussy, and there's nothing else on my mind as I pull her towards me."
    return

label ayesha_warn_condom:
    $ result = randint(1, 4)
    if result == 1:
        "But the same can't be said for Ayesha, who fixes me with a serious look, stopping me in my tracks."
        ayesha.say "Ah, [hero.name] - aren't you forgetting something?"
    elif result == 2:
        "But the I feel her resist for the first time that night."
        "Ayesha turns her head to regard me over her shoulder."
        ayesha.say "[hero.name] - don't you go forgetting that one little thing, okay?"
    elif result == 3:
        "Suddenly, Ayesha stops and shakes her head."
        ayesha.say "Wait a minute, baby."
        ayesha.say "We should use some protection!"
    else:
        "Ayesha stops me dead in my tracks."
        ayesha.say "Ah, [hero.name] - aren't you forgetting something?"
    return

label ayesha_force_condom:
    $ result = randint(1, 4)
    if result == 1:
        "I'm puzzled by this at first, but nod as soon as Ayesha holds up a condom."
        "I nod hastily, taking it and wasting no time in putting it on."
        "So a couple of seconds later, everything is sorted and ready to go."
    elif result == 2:
        "Ayesha's right - first things first though - can't forget the basics!"
        "I reach out and just manage to grab a condom from the bedside table."
        "She glances back over her shoulder, nodding in approval."
        "All it takes is a couple more seconds, and we're ready to go."
    elif result == 3:
        "I wait patiently as Ayesha retrieves a condom from her things."
        "And then I watch with baited breath as she opens the packet and slips it onto my cock."
        "A moment later it's done, and Ayesha nods happily."
        ayesha.say "There you go."
        ayesha.say "Now, where were we..."
    else:
        "I'm a little thrown off at first, but nod as soon as she proffers a condom."
        "Taking it from her, I don't even bother to say a word as I put it on."
        "In no time at all I'm ready to go."
    return

label ayesha_mad_condom:
    $ result = randint(1, 3)
    if result == 1:
        "But the same can't be said for Ayesha, who fixes me with a serious look, stopping me in my tracks."
        ayesha.say "Ah, [hero.name] - aren't you forgetting something?"
        mike.say "No...I don't think so!"
        "Ayesha makes a snorting sound of disapproval."
        ayesha.say "What about the condom, genius?!?"
        ayesha.say "I don't believe it - you were going to do me without one!"
        "She shoves me in the middle of the chest with the flat of her hand."
        "And for the first time tonight, I'm reminded of just how strong she actually is."
        "I gasp as the air is blown out of my lungs and fall on my back atop the bed."
        "I'm still thrashing about, trying to catch my breath as Ayesha gets up and grabs her clothes."
        "Then I hear the sound of the door opening and slamming closed as she leaves."
        play sound door_slam
    elif result == 2:
        mike.say "What little thing would that be?"
        "Ayesha shakes her head, amazed at my answer."
        ayesha.say "Erm, the condom, moron!"
        ayesha.say "You're not putting that thing inside me without one."
        "Ayesha clambers off me, and isn't too gentle in doing so either."
        "I groan in pain, already feeling too ashamed to protest."
        "And so I end up watching in silence as gets dressed."
        "Then she storms out of the door, slamming it behind her."
        play sound door_slam
    elif result == 3:
        mike.say "Really, Ayesha?"
        mike.say "That's just going to kill the mood!"
        mike.say "I'll pull out before the end, trust me."
        ayesha.say "Yeah..."
        ayesha.say "I think you just killed the mood yourself!"
        "With that, she climbs off me and then off the bed."
        "Ayesha starts pulling on her clothes as I watch in disbelief."
        mike.say "You can't seriously be leaving!"
        ayesha.say "Well that's what I'm doing."
        ayesha.say "So you'd better deal with it!"
        "All I can do is watch in silence as Ayesha makes good on her promise."
        "Looks like I really blew it this time - and all over a damn condom!"
    else:
        mike.say "What the hell are you talking about?!?"
        "Ayesha fixes me with a look that's equal parts disbelief and disgust."
        ayesha.say "Protection, you stupid bastard!"
        ayesha.say "We're not going any further without one."
        "Ayesha shoves me off of her, tossing me aside with little effort."
        "The blow is painful, but the shock is what hits me hardest."
        "I wince in discomfort, not daring to say a word for fear of what she might do to me."
        "Which means that I end up watching in silence as she pulls on her clothes."
        "And the only sound that follows is that of the door slamming closed behind her."
        play sound door_slam
    $ LEAVE = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
