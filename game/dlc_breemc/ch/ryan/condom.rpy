label ryan_use_condom:
    "We're just about ready to go, all lined up and about to do it."
    "But that's when I realise that I've gone and forgotten something."
    if hero.morality >= 25:
        bree.say "Whoops...wait a second, Ryan!"
    elif hero.morality <= -25:
        bree.say "We'll get it on, Ryan - in just a second!"
    else:
        bree.say "Oh...hang on, Ryan!"
    "Ryan looks puzzled by my sudden change of course."
    "And he frowns as I hurry away from him."
    if ryan.sub >= 50:
        ryan.say "What's the matter - did I do something wrong?"
    elif ryan.sub <= -50:
        ryan.say "[hero.name], get back here, right now!"
    else:
        ryan.say "Hey - where are you going?"
    "I kind of choose to ignore what Ryan's saying."
    "Because I've already found what I was looking for."
    "When I hold up the condom, the look on his face changes to one of recognition."
    "And he's nodding eagerly as I make my way back over to him."
    "Once there, I don't waste any time in tearing open the wrapper."
    "As soon as it's on, we're back in business and ready to go!"
    return

label ryan_intro_condom:
    "We're all ready to go, everything lined up and in place."
    "And I can honestly say that all of my attention is on the task ahead of me."
    "There's nothing that I want more than to get things underway."
    "And I'm hoping that Ryan's on the same page too."
    "Because I don't know what I'll do if I don't get what I want in the next couple of minutes!"
    return

label ryan_warn_condom:
    "But before I can leap on him, Ryan holds up a hand."
    "Which has the frustrating effect of stopping me in my tracks."
    if ryan.sub >= 50:
        ryan.say "Wait, [hero.name]..."
        ryan.say "We should really use some protection."
    elif ryan.sub <= -50:
        ryan.say "Stop right there, [hero.name]..."
        ryan.say "We're not doing it without a condom!"
    else:
        ryan.say "Hold on, [hero.name]..."
        ryan.say "What about the condom?"
    "And from the look on his face, I can tell he's totally serious."
    return

label ryan_force_condom:
    "I'm about to object when Ryan leaps up and hurries over to his clothes."
    "Then I watch as he rummages in his pockets until he finds something."
    "And when he finally holds up a condom, I feel a genuine sense of relief."
    "Ryan hurries back with it in his hand, and we're soon tearing the packet open."
    "As soon as it's on, we're back in business and ready to go!"
    return

label ryan_mad_condom:
    if hero.morality >= 25:
        bree.say "Can't we just forget it this one time?"
    elif hero.morality <= -25:
        bree.say "Forget it, Ryan - I promise you it'll feel a hundred times better!"
    else:
        bree.say "Ah, just forget it this once, Ryan!"
    "Ryan looks at me like he can't believe what he's hearing."
    "And then he starts to move away from me, shaking his head."
    if ryan.sub >= 50:
        ryan.say "I can't believe you'd be so reckless, [hero.name]!"
    elif ryan.sub <= -50:
        ryan.say "Well that's me soured on this whole deal!"
    else:
        ryan.say "I'm not taking any chances, [hero.name]!"
    "I watch in helpless silence as Ryan pulls on his clothes."
    "And then let out a tortured groan as he walks out of the door too."
    "Realising that I just cheated myself out of some serious fun."
    "And all for the sake of one lousy condom!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
