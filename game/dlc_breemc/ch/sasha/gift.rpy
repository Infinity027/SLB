label sasha_give_female:









    if "skill_book_guitar" not in hero.inventory and not hero.has_skill("guitar"):
        $ gift = "skill_book_guitar"
        "She hands me a pretty large book."
        bree.say "Wow!\nIs that a book with guitar tricks?"
        sasha.say "It sure is..."
        bree.say "Thank you so much."
    elif "dildo" not in hero.inventory and sasha.love >= 50:
        $ gift = "dildo"
        "She hands me a small box."
        bree.say "A dildo?"
        sasha.say "I am pretty sure you know how to use it."
        bree.say "Thank you I guess."
    else:
        $ gift = "flowers"
        "She hands me some flowers."
        bree.say "Thanks."
    $ hero.gain_item(gift)
    return

label sasha_give_birthday_female:
    sasha.say "Happy birthday, [hero.name]!"
    sasha.say "And here's your present too."
    bree.say "Aw...thanks, Sasha!"
    bree.say "Oh wow - how did you know?"
    sasha.say "Well, I do listen to you when you're talking, [hero.name]!"
    sasha.say "I remember you saying you liked that kind of stuff..."
    call sasha_give_female from _call_sasha_give_female
    return

label sasha_give_christmas_female:
    sasha.say "Merry Christmas, [hero.name]!"
    sasha.say "I hope you like what I got you."
    bree.say "You got me a present?"
    bree.say "Sasha, that's so thoughtful of you!"
    sasha.say "Ah, don't rub it in, [hero.name]!"
    sasha.say "Isn't that what people are supposed to do at Christmas?"
    bree.say "Oh stop it, Sasha!"
    bree.say "We both know you're not really a grinch!"
    call sasha_give_female from _call_sasha_give_female_1
    return

label sasha_give_valentine_female:
    sasha.say "Happy valentine's day, [hero.name]."
    sasha.say "I got you a little something too."
    sasha.say "Just to say thanks for being my valentine."
    bree.say "Sasha - that's so sweet of you!"
    bree.say "I'm glad you're my valentine too."
    sasha.say "Yeah, [hero.name] - we both rock."
    $ hero.gain_item("valentine_chocolates")
    return


label sasha_birthday_gift_female:
    show sasha
    if sasha.flags.birthdayknown:
        bree.say "Happy birthday Sasha."
        sasha.say "How sweet, you remembered my birthday!"
    else:
        sasha.say "How do you know my birthday?"
        bree.say "I didn't, it's just pure luck."
        $ sasha.flags.birthdayknown = True
    return

label sasha_christmas_gift_female:
    show sasha
    bree.say "Merry Christmas Sasha."
    sasha.say "Thanks!"
    $ sasha.love += 2
    return

label sasha_valentine_gift_female:
    show sasha
    bree.say "Happy valentine's day Sasha."
    sasha.say "Thank you."
    $ sasha.love += 2
    return


label sasha_gift_collar_female:
    if sasha.sub >= 90:
        "Sasha seems to enjoy the gift."
        $ sasha.love += 5
        $ sasha.set_sex_slave()
    else:
        "Sasha seems to dislike the gift."
        $ sasha.love -= 20
        $ sasha.sub -= 10
        $ hero.cancel_activity()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
