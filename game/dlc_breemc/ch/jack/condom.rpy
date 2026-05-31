label jack_use_condom:
    $ result = randint(0, 3)
    if result == 0:
        "At the last moment I remember something that's more than a little important."
        bree.say "Whoa..."
        bree.say "We should really use a condom!"
        bree.say "I think I have one in my purse..."
        "For a couple of seconds we fumble around, looking for a condom."
        "But one soon appears, and it's hastily torn from the package."
        "A moment later it's on his cock, and we're good to go!"
    elif result == 1:
        "It's about then that something hits me."
        "And I hold up a hand to halt proceedings."
        jack.say "What's up, [hero.name]?"
        jack.say "Did I do something wrong already?"
        bree.say "Don't be silly, Jack!"
        bree.say "I just remembered we need a condom, that's all!"
        jack.say "Oh!"
        jack.say "Okay..."
        "I hop off Jack's lap and hurry to grab a condom."
        "Then I get straight down to putting it on him."
        "With that taken care of, we're ready to go."
    elif result == 2:
        "But then I remember something else."
        "And I hurry to call a temporary halt to the proceedings."
        bree.say "Wait a minute, Jack..."
        bree.say "We forgot something!"
        jack.say "Huh?"
        jack.say "What's that, [hero.name]?"
        bree.say "A condom, that's what."
        bree.say "Don't worry, I got one right over here."
        "Quick as a flash, I jump off the bed"
        "Then I grab a condom from where I keep them in a drawer."
        "Hopping back onto the bed, I hand it to Jack and then get back into position."
        "He fiddles around a little, getting it on."
        "That done, we're good to go."
    else:
        "But before Jack can get there, I hold up a hand to stop him."
        jack.say "Huh?"
        jack.say "What's up, [hero.name]?"
        jack.say "Did you change your mind already?"
        bree.say "No, Jack..."
        bree.say "I just remembered that we should take precautions."
        bree.say "I have some condoms right over here."
        "I reach over to the other side of the bed."
        "And I grab one of the condoms I have stashed there."
        "Then I hand it over to Jack."
        bree.say "There you go - put it on!"
        "Jack nods and hurries to do as he's told."
        "Once he's wearing the condom, we're ready to go."
    return

label jack_intro_condom:
    "I watch him sliding his fingers up and down the shaft intently."
    "And I can almost feel my pussy twitching in anticipation."
    "My heart beating a little faster the close it gets to me!"
    return

label jack_warn_condom:
    $ result = randint(0, 3)
    if result == 0:
        "At the last moment I remember something that's more than a little important."
        bree.say "Whoa..."
        bree.say "We should really use a condom!"
    elif result == 1:
        "It's about then that Jack seems to find his voice."
        jack.say "Ah, [hero.name]..."
        jack.say "I don't mean to be a buzz-kill..."
        jack.say "But we should really use a condom!"
    elif result == 2:
        "But then I hear Jack speaking up again."
        jack.say "Wait a minute, [hero.name]..."
        jack.say "We forgot to use protection!"
    else:
        "But before he makes it all the way to me, Jack stops."
        "And he holds up a hand in front of me."
        bree.say "Huh?"
        bree.say "What gives, Jack?"
        bree.say "Don't tell me you're getting cold feet!"
        jack.say "No, [hero.name]..."
        jack.say "I was just thinking that we should use a condom."
    return

label jack_force_condom:
    $ result = randint(0, 3)
    if result == 0:
        "Before I can protest, Jack hops off me."
        "And then he's hunting around for a condom."
        "I can't help feeling a little slighted as he does this."
        "But I do the best I can to hide my feelings as he returns."
        jack.say "Phew..."
        jack.say "Lucky I remembered one of these!"
        jack.say "Just let me get it on there..."
        jack.say "Then we're good to go!"
    elif result == 1:
        bree.say "Yeah, you're right..."
        bree.say "We really should!"
        bree.say "I can't believe I forgot."
        jack.say "It's okay, [hero.name]..."
        jack.say "I've got one right over there..."
        jack.say "In the pocket of my pants!"
        "I hop off Jack's lap and hurry to grab a condom."
        "Then I get straight down to putting it on him."
        "With that taken care of, we're ready to go."
    elif result == 2:
        "Before I can say a word, Jack's already hopping off the bed."
        jack.say "Don't worry..."
        jack.say "I have one in my pocket."
        jack.say "Right here!"
        with vpunch
        "He jumps back onto the bed and fiddles around putting it on."
        "That done, we're good to go."
    else:
        jack.say "It's okay..."
        jack.say "I have one in my pocket."
        jack.say "Right over there."
        "I watch as Jack gets up and hunts for his pants."
        "As soon as he retrieves it, he starts putting it on."
        "Once he's wearing the condom, we're ready to go."
    return

label jack_mad_condom:
    show jack angry at center, zoomAt(1.5, (640, 1040)) with fade
    $ result = randint(0, 4)
    if result == 0:
        jack.say "What?!?"
        jack.say "Oh come on, [hero.name]!"
        jack.say "Forget about it just this once!"
        "For a moment I can't actually believe what I'm hearing."
        "Is he really trying to convince me not to use protection?!?"
        bree.say "No way, Jack!"
        bree.say "There's not a chance of that happening!"
        bree.say "How can you be so irresponsible?"
        "I can already feel the desire cooling off inside of me."
        "Talk about a passion-killer!"
    elif result == 1:
        jack.say "[hero.name]..."
        jack.say "Aw, come on!"
        jack.say "Don't you think you're making a big deal out of nothing?"
        "I don't answer Jack, instead letting my actions speak for themselves."
        scene bg bedroom4
        show jack sad naked at center, zoomAt(1.5, (640, 1040))
        with fade
        "Hopping up, I start to gather up my clothes and get ready."
        jack.say "[hero.name] - aren't you even going to answer me?!?"
        "I'm almost dressed by now, so I do as he asks."
        "Turning to face Jack, I give him a piece of my mind."
        bree.say "It's nothing to you, Jack."
        bree.say "But it's something to me."
        bree.say "I'm not winding up pregnant, buddy."
        bree.say "Not for the sake of you having a little fun!"
        scene bg secondfloor with fade
        "Before Jack can say another word, I storm out."
        "Sure, I'm leaving him with his dick in his hand."
        "But he deserves it."
        "And he could use the time to think about what he's just done too."
    elif result == 2:
        bree.say "Well you are being a buzz-kill, Jack!"
        bree.say "Just forget about it, okay?"
        "I feel Jack getting to his feet."
        "As I'm sitting on his lap, that's not good news for me."
        scene bg bedroom4
        show jack sad naked at center, zoomAt(1.5, (640, 1040))
        with vpunch
        "And sure enough, I find myself tumbling into the floor!"
        bree.say "Hey!"
        jack.say "Sorry, [hero.name]..."
        jack.say "But I just can't be the irresponsible."
        jack.say "And if you're not going to use protection..."
        jack.say "Then I think I should leave."
        "No matter what I say, nothing seems to work."
        show jack date with dissolve
        pause 0.3
        hide jack with easeoutright
        "And Jack keeps his word, getting dressed and walking out."
        "Which leaves me alone, frustrated and even a little bruised from the fall!"
    elif result == 3:
        bree.say "Don't be such a pussy, Jack!"
        bree.say "Forget about it, just this once, yeah?"
        "I feel jack getting off the bed behind me."
        scene bg bedroom4
        show jack sad naked at center, zoomAt(1.5, (640, 1040))
        with fade
        "And I turn around, surprised to see him picking up his clothes."
        bree.say "Hey!"
        bree.say "Where are you going?"
        jack.say "Home, [hero.name]..."
        jack.say "I'm going home."
        bree.say "But why?"
        show jack angry
        jack.say "I can't believe you don't want to use protection!"
        jack.say "That's a massive turn-off, [hero.name] - a total mood-killer!"
        "I keep on trying to argue with Jack, to convince him to stay."
        show jack date with dissolve
        pause 0.3
        hide jack with easeoutright
        "But he sticks to his convictions, and soon he's dressed and gone."
        "Leaving me alone and frustrated in my room."
    else:
        bree.say "Oh come on, Jack!"
        bree.say "Don't be a boring prick."
        bree.say "Forget about the condom and let's fuck already!"
        "Jack looks shocked at what I just said."
        scene bg bedroom4
        show jack sad naked at center, zoomAt(1.5, (640, 1040))
        with fade
        "So much so that he's already backing away from me."
        show jack angry
        jack.say "I can't believe you'd be so irresponsible, [hero.name]."
        jack.say "Or that you'd call me a boring prick."
        jack.say "I do happen to have feelings, you know!"
        "No matter what I say or do from that point on, it doesn't matter."
        "Nothing can persuade Jack to stay or even that I'm sorry."
        show jack date with dissolve
        pause 0.3
        hide jack with easeoutright
        "Instead he storms out of my room once he's dressed."
        "Which leaves me alone, unfulfilled and feeling pretty stupid."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
