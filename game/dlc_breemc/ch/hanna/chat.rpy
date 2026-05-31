label hanna_desire_0_female:
    if hero.fitness >= 10:
        hanna.say "I like how you take care of your body."
        $ hanna.love += 1
    else:
        hanna.say "You should work out more."
    return

label hanna_desire_1_female:
    if hero.fitness >= 20:
        hanna.say "Those abs looks good on you."
        $ hanna.love += 1
    elif hero.fitness < 10:
        hanna.say "I don't like men who don't take care of their body."
        $ hanna.love -= 1
    else:
        hanna.say "You should work out more."
    return

label hanna_desire_2_female:
    if hero.fitness >= 30:
        hanna.say "You look good today."
        $ hanna.love += 1
    elif hero.fitness < 20:
        hanna.say "I don't like men who don't take care of their body."
        $ hanna.love -= 1
    else:
        hanna.say "You should work out more."
    return

label hanna_desire_3_female:
    if hero.fitness >= 40:
        hanna.say "Sometimes I wanna rip your shirt off."
        $ hanna.love += 1
    elif hero.fitness < 30:
        hanna.say "I don't like men who don't take care of their body."
        $ hanna.love -= 1
    else:
        hanna.say "You should work out more."
    return

label hanna_desire_4_female:
    if hero.fitness >= 50:
        hanna.say "Can I see you naked?"
        $ hanna.love += 1
    elif hero.fitness < 40:
        hanna.say "I don't like men who don't take care of their body."
        $ hanna.love -= 1
    else:
        hanna.say "You should work out more."
    return

label hanna_desire_5_female:
    if hero.fitness >= 50:
        hanna.say "Can I see you naked?"
        $ hanna.love += 1
    elif hero.fitness < 40:
        hanna.say "I don't like men who don't take care of their body."
        $ hanna.love -= 1
    else:
        hanna.say "You should work out more."
    return

label hanna_love_0_female:
    hanna.say "I kind of like your smile."
    $ hanna.sub += 1
    return

label hanna_love_1_female:
    hanna.say "You look great in that shirt."
    $ hanna.sub += 1
    return

label hanna_love_2_female:
    hanna.say "You should go topless."
    $ hanna.sub += 1
    return

label hanna_love_3_female:
    hanna.say "I love your pecs."
    $ hanna.sub += 1
    return

label hanna_love_4_female:
    hanna.say "Your abs are so sexy."
    $ hanna.sub += 1
    return

label hanna_love_5_female:
    hanna.say "I wanna eat you alive."
    $ hanna.sub += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
