init python:
    Consumable("arnold_braunschweiger_method", price=100, effects=[("fitness", 2), ("time", 4)], frequency_limit="week", conditions=[HeroTarget(MinStat("energy", 2), MinStat("hunger", 2), MinStat("grooming", 2), MinStat("fun", 2))])

label ayesha_give_female:








    if "arnold_braunschweiger_method" not in hero.inventory:
        $ gift = "arnold_braunschweiger_method"
        "She hands me a pretty large book."
        bree.say "What is this Ayesha?"
        ayesha.say "A book that'll help you get stronger faster."
        bree.say "Thanks! I love that more than ever."
    else:
        $ gift = "flowers"
        "She hands me some flowers."
        bree.say "Thanks."
    $ hero.gain_item(gift)
    return

label ayesha_give_birthday_female:
    ayesha.say "Happy birthday, [hero.name]!"
    ayesha.say "I...I got you a gift too!"
    bree.say "Oh wow!"
    bree.say "Thanks, Ayesha."
    ayesha.say "I...I picked it myself, obviously!"
    bree.say "You did?"
    bree.say "That makes it even more special, Ayesha!"
    call ayesha_give_female from _call_ayesha_give_female
    return

label ayesha_give_christmas_female:
    ayesha.say "Merry Christmas, [hero.name]!"
    ayesha.say "And here's your present from me."
    ayesha.say "No need to wait for Christmas morning."
    ayesha.say "You can open it now, if you like?"
    bree.say "Oh, Ayesha..."
    bree.say "Thank you so much!"
    call ayesha_give_female from _call_ayesha_give_female_1
    return

label ayesha_give_valentine_female:
    bree.say "Oh, Ayesha..."
    bree.say "What's that you've got there?"
    ayesha.say "Oh...that..."
    ayesha.say "It's a valentine's gift..."
    ayesha.say "For you, [hero.name] - obviously it's for you!"
    bree.say "That's so sweet of you, Ayesha!"
    bree.say "I'm lucky to have you as my valentine."
    $ hero.gain_item("valentine_chocolates")
    return

label ayesha_valentine_gift_female:
    show ayesha
    bree.say "Happy valentine's day Ayesha."
    ayesha.say "Thank you."
    $ ayesha.love += 2
    return

label ayesha_birthday_gift_female:
    show ayesha
    if ayesha.flags.birthdayknown:
        bree.say "Happy birthday Ayesha."
        ayesha.say "How sweet, you remembered my birthday!"
    else:
        ayesha.say "How do you know my birthday?"
        bree.say "I didn't, it's just pure luck."
        $ ayesha.flags.birthdayknown = True
    return

label ayesha_christmas_gift_female:
    show ayesha
    bree.say "Merry Christmas Ayesha."
    ayesha.say "Thanks!"
    $ ayesha.love += 2
    return


label ayesha_gift_collar_female:
    if ayesha.sub >= 90:
        "Ayesha seems to enjoy the gift."
        $ ayesha.love += 5
        $ ayesha.set_sex_slave()
    else:
        "Ayesha seems to dislike the gift."
        $ ayesha.love -= 20
        $ ayesha.sub -= 10
        $ hero.cancel_activity()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
