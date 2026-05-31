label hanna_desire_0_male:
    if hero.fitness >= 10:
        hanna.say "I like how you take care of your body."
        $ hanna.love += 1
    else:
        hanna.say "You should work out more."
    return

label hanna_desire_1_male:
    if hero.fitness >= 20:
        hanna.say "Those abs looks good on you."
        $ hanna.love += 1
    elif hero.fitness < 10:
        hanna.say "I don't like men who don't take care of their body."
        $ hanna.love -= 1
    else:
        hanna.say "You should work out more."
    return

label hanna_desire_2_male:
    if hero.fitness >= 30:
        hanna.say "You look good today."
        $ hanna.love += 1
    elif hero.fitness < 20:
        hanna.say "I don't like men who don't take care of their body."
        $ hanna.love -= 1
    else:
        hanna.say "You should work out more."
    return

label hanna_desire_3_male:
    if hero.fitness >= 40:
        hanna.say "Sometimes I wanna rip your shirt off."
        $ hanna.love += 1
    elif hero.fitness < 30:
        hanna.say "I don't like men who don't take care of their body."
        $ hanna.love -= 1
    else:
        hanna.say "You should work out more."
    return

label hanna_desire_4_male:
    if hero.fitness >= 50:
        hanna.say "Can I see you naked?"
        $ hanna.love += 1
    elif hero.fitness < 40:
        hanna.say "I don't like men who don't take care of their body."
        $ hanna.love -= 1
    else:
        hanna.say "You should work out more."
    return

label hanna_desire_5_male:
    if hero.fitness >= 50:
        hanna.say "Can I see you naked?"
        $ hanna.love += 1
    elif hero.fitness < 40:
        hanna.say "I don't like men who don't take care of their body."
        $ hanna.love -= 1
    else:
        hanna.say "You should work out more."
    return

label hanna_love_0_male:
    hanna.say "I kind of like your smile."
    $ hanna.sub += 1
    return

label hanna_love_1_male:
    hanna.say "You look great in that shirt."
    $ hanna.sub += 1
    return

label hanna_love_2_male:
    hanna.say "You should go topless."
    $ hanna.sub += 1
    return

label hanna_love_3_male:
    hanna.say "I love your pecs."
    $ hanna.sub += 1
    return

label hanna_love_4_male:
    hanna.say "Your abs are so sexy."
    $ hanna.sub += 1
    return

label hanna_love_5_male:
    hanna.say "I wanna eat you alive."
    $ hanna.sub += 1
    return

label hanna_good_sweet_talk_male:
    show hanna
    if hanna.love > 133:
        mike.say "Wow...you're SO fit, Hanna!"
        mike.say "You have so much stamina too."
        mike.say "It's...well, it's so sexy!"
        show hanna flirt
        hanna.say "Mmm...I like to work out."
        hanna.say "But making love is the BEST kind of exercise!"
    elif hanna.love > 66:
        mike.say "People just can't keep their eyes off you, Hanna!"
        mike.say "I'm so lucky to be seen with someone as gorgeous as you."
        show hanna flirt
        hanna.say "You're terrible, [hero.name], such a flatterer!"
        hanna.say "But I'd be lying if I said I didn't like it!"
    else:
        mike.say "You take such good care of yourself, Hanna."
        mike.say "And it shows too - you look amazing!"
        show hanna happy
        hanna.say "Aww...thanks for the compliment!"
        hanna.say "But I DO work hard to keep in shape."
    hide hanna
    return

label hanna_bad_sweet_talk_male:
    show hanna
    mike.say "It's great that a girl can have a ripped body these days."
    mike.say "Right, Hanna?"
    show hanna angry
    hanna.say "Y...you think I look like a guy?"
    hanna.say "Be honest - have you ever mistaken me for a guy?!?"
    mike.say "No, Hanna, no!"
    hide hanna
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
