init python:
    Item("dionaea")

label kylie_give_female:







    if "dionaea" not in hero.inventory:
        $ gift = "dionaea"
        "She hands me a plant."
        bree.say "Wow! Is that a carnivorous plant?"
        kylie.say "Sure is! So you can always remember me when you look at it."
        bree.say "Yeeesss... Thanks Kylie, I'll be careful to not let it bite me."
    else:
        $ gift = "flowers"
        "She hands me some flowers."
        bree.say "Thanks."
    $ hero.gain_item(gift)
    return

label kylie_give_birthday_female:
    kylie.say "Happy birthday, [hero.name]!"
    kylie.say "And look, I didn't forget - here's your present!"
    bree.say "Oh wow!"
    bree.say "Thanks, Kylie..."
    bree.say "Wait a minute...what are these red stains on the box?"
    kylie.say "Oh, they're nothing, [hero.name]."
    kylie.say "Probably red paint, or tomato ketchup, you know?"
    call kylie_give_female from _call_kylie_give_female
    return

label kylie_give_christmas_female:
    kylie.say "Merry Christmas, [hero.name]!"
    kylie.say "Here's your present too."
    bree.say "Oh, thank you, Kylie!"
    bree.say "You want me to open it now?"
    bree.say "You know, so you can see me do it?"
    kylie.say "Oh no, [hero.name], that's okay."
    kylie.say "Open it when I'm not there if you like."
    kylie.say "I'll be watching...I mean in spirit - I'll be watching in spirit!"
    call kylie_give_female from _call_kylie_give_female_1
    return

label kylie_give_valentine_female:
    kylie.say "Hey there, valentine!"
    kylie.say "Here's your gift!"
    bree.say "Aw, thanks, Kylie!"
    bree.say "It's a heart, that's so..."
    bree.say "Wait a minute...it's all wet and sticky!"
    kylie.say "Oh yeah...that's...erm..."
    kylie.say "That's because the paint is still a little wet, that's all!"
    $ hero.gain_item("valentine_chocolates")
    return

label kylie_birthday_gift_female:
    show kylie
    if kylie.flags.birthdayknown:
        bree.say "Happy birthday Kylie."
        kylie.say "How sweet, you remembered my birthday!"
    else:
        kylie.say "How do you know my birthday?"
        bree.say "I didn't, it's just pure luck."
        $ kylie.flags.birthdayknown = True
    return


label kylie_gift_collar_female:
    if kylie.sub >= 90:
        "Kylie seems to enjoy the gift."
        $ kylie.love += 5
        $ kylie.set_sex_slave()
    else:
        "Kylie seems to dislike the gift."
        $ kylie.love -= 20
        $ kylie.sub -= 10
        $ hero.cancel_activity()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
