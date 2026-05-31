label lexi_give_female:
    lexi.say "TADA!"
    lexi.say "There ya go, [hero.name]!"
    bree.say "Erm...thanks, Lexi."
    bree.say "But what's the special occasion?"
    lexi.say "No special occasion, [hero.name]."
    lexi.say "I just wanted to get you something nice is all!"
    bree.say "Oh...okay, Lexi."
    bree.say "Thank you for thinking of me!"
    return

label lexi_give_birthday_female:
    lexi.say "Happy birthday, [hero.name]!"
    lexi.say "Here's your present too."
    bree.say "Oh, Lexi - thank you so much!"
    bree.say "But how did you know it was my birthday today?"
    lexi.say "No big deal, [hero.name]."
    lexi.say "I asked [mike.name] and Sasha when it was."
    lexi.say "I just didn't want to miss it, you know?"
    bree.say "Wow...that's kind of amazing, Lexi!"

    $ hero.gain_item("box_of_condoms")
    return

label lexi_give_christmas_female:
    lexi.say "Merry Christmas, [hero.name]!"
    lexi.say "Here's your present from me."
    bree.say "Thank you, Lexi."
    bree.say "It's so nice that you thought of me."
    bree.say "Should I wait until Christmas morning?"
    bree.say "Or do you want me to open it now?"
    lexi.say "I dunno, [hero.name]..."
    lexi.say "What am I, the Christmas Police?!?"

    $ hero.gain_item("box_of_condoms")
    return

label lexi_give_valentine_female:
    lexi.say "Thanks for being my valentine, [hero.name]!"
    lexi.say "Here's a little something I got you too..."
    bree.say "Aw, Lexi - you didn't have to get me a valentine's gift!"
    lexi.say "Yeah, yeah...I know that, [hero.name]."
    lexi.say "But it ain't against the law, is it?"
    bree.say "I guess not, Lexi!"
    $ hero.gain_item("valentine_chocolates")
    return

label lexi_birthday_gift_female:
    show lexi
    if lexi.flags.birthdayknown:
        bree.say "Happy birthday Lexi."
        lexi.say "How sweet, you remembered my birthday!"
    else:
        lexi.say "How do you know my birthday?"
        bree.say "I didn't, it's just pure luck."
        $ lexi.flags.birthdayknown = True
    return


label lexi_gift_collar_female:
    if lexi.sub >= 90:
        "Lexi seems to enjoy the gift."
        $ lexi.love += 5
        $ lexi.set_sex_slave()
    else:
        "Lexi seems to dislike the gift."
        $ lexi.love -= 20
        $ lexi.sub -= 10
        $ hero.cancel_activity()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
