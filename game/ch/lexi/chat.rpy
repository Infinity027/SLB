label lexi_desire_0_male:

    if lexi.love < 30:
        lexi.say "What do you want dumbass?"
    else:
        lexi.say "What's up [hero.name]?"

    return

label lexi_desire_1_male:

    if lexi.love < 60:
        lexi.say "You think because you're not half bad looking you deserve something special?"
    else:
        lexi.say "You know, I think you're not half bad looking..."

    return

label lexi_desire_2_male:

    if lexi.love < 90:
        lexi.say "Don't go thinking I'll fall for you just because you know how to smile."
    else:
        lexi.say "Stop smiling like that, it's embarrassing."
    $ lexi.love += 1

    return

label lexi_desire_3_male:

    if lexi.love < 120:
        lexi.say "I love Disrupted, such a great band..."
    else:
        lexi.say "You should take me to a Disrupted concert sometime."
    $ lexi.love += 1

    return

label lexi_desire_4_male:

    if lexi.love < 150:
        lexi.say "I feel nervous around you sometimes."
    else:
        lexi.say "Why isn't your dick in my pussy right now?"
    $ lexi.love += 1

    return

label lexi_desire_5_male:

    if lexi.love < 180:
        lexi.say "What do you say we go somewhere quiet?"
    else:
        lexi.say "I miss the feeling of you fucking me."
    $ lexi.love += 1

    return

label lexi_love_0_male:

    if lexi.love < 30:
        lexi.say "Get the hell away from me."
    else:
        lexi.say "What are you listening to these days?"
    $ lexi.love += 1

    return

label lexi_love_1_male:

    if lexi.love < 60:
        lexi.say "Fuck off."
    else:
        lexi.say "I am glad I met you, you're quite the nice guy for a dork."
    $ lexi.love += 1

    return

label lexi_love_2_male:

    if lexi.love < 90:
        lexi.say "So you play World of Warcraft or what?"
    else:
        lexi.say "Fuck I am bored."
    $ lexi.love += 1

    return

label lexi_love_3_male:

    if lexi.love < 120:
        lexi.say "Is there a school for guys like you to learn how to talk to girls like me?"
    else:
        lexi.say "I know I am too good for you, but I might make an exception."
    $ lexi.love += 1

    return

label lexi_love_4_male:

    if lexi.love < 150:
        lexi.say "So are we a couple?"
    else:
        lexi.say "I think I might be falling for you..."
    $ lexi.love += 1

    return

label lexi_love_5_male:

    if lexi.love < 180:
        lexi.say "Yeah, yeah, I am in love, so what?"
    else:
        lexi.say "Please fuck me as soon as we are alone..."
    $ lexi.love += 1

    return

label lexi_good_sweet_talk_male:
    show lexi
    if lexi.love > 133:
        mike.say "Lexi, if I ever tell you put more clothes on, do something for me."
        mike.say "Shoot me in the head, okay?"
        mike.say "You look perfect just as you are!"
        show lexi happy
        lexi.say "Aw...I love you too, [hero.name]!"
    elif lexi.love > 66:
        mike.say "I love the way you're not ashamed to be who you really are, Lexi."
        mike.say "It's pretty liberating, you know?"
        show lexi wink
        lexi.say "I'm just trying to be the best I can at being me!"
        lexi.say "I can't help it if I'm good at it!"
    else:
        mike.say "You really know how to have a good time, Lexi!"
        mike.say "It's like you figured out what's really important in life."
        lexi.say "Huh?!?"
        lexi.say "I'm no philosopher for sure - but thanks for the compliment!"
    hide lexi
    return

label lexi_bad_sweet_talk_male:
    show lexi
    mike.say "You're so laid back and easy, Lexi."
    mike.say "That's what I love about you!"
    show lexi angry
    lexi.say "Oh, so you like that I'm easy, huh?"
    lexi.say "You think I'm a whore - is that it?!?"
    mike.say "Erm...I don't think that's what I said..."
    hide lexi
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
