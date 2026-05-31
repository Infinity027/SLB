label lavish_desire_0_female:
    "Lavish is happily humming."
    $ lavish.love += 1
    return

label lavish_desire_1_female:
    if lavish.love > 75:
        $ result = randint(1, 3)
        if result == 1:
            lavish.say "I love your smile."
        elif result == 2:
            lavish.say "I think someone on the second floor is watching my ass when I pass by..."
            lavish.say "What a creep."
        else:
            lavish.say "I wish we worked together more."
        $ lavish.love += 2
    else:
        lavish.say "How are you doing today?"
        bree.say "Fine."
        $ lavish.love += 1
    return

label lavish_desire_2_female:
    lavish.say "I love working with you."
    $ lavish.love += 1
    return

label lavish_desire_3_female:
    lavish.say "Do you think you will be promoted soon?"
    $ lavish.love += 1
    return

label lavish_desire_4_female:
    $ result = randint(1, 4)
    if result == 1:
        lavish.say "It's crazy how good you are at your job."
    elif result == 2:
        lavish.say "Do you think I should let my hair grow?"
    elif result == 3:
        lavish.say "What do you think about office relationships?"
    else:
        bree.say "How are you doing today Lavish?"
        lavish.say "Fine, thanks for asking."
    $ lavish.love += 1
    return

label lavish_desire_5_female:
    lavish.say "I think I am in love with you."
    $ lavish.love += 1
    return

label lavish_love_0_female:
    lavish.say "Aletta is such a great boss."
    $ lavish.love += 1
    return

label lavish_love_1_female:
    lavish.say "What do you think about Shiori?"
    menu:
        "She's cute":
            $ lavish.love -= 1
            bree.say "I think she's cute."
        "She's very professional":
            $ lavish.love += 1
            bree.say "She's very good at her job and has a very professional attitude."
    return

label lavish_love_2_female:
    $ nbr = randint(1, 2)
    if not lavish.flags.birthdayknown and nbr == 1:
        bree.say "Hey Lavish, when is your birthday?"
        lavish.say "It's on the [lavish.birthday[1]] of [lavish.birthday[0]]."
        lavish.say "Are you planning on getting me a gift?"
        bree.say "Maybe..."
        $ lavish.flags.birthdayknown = True
    else:
        lavish.say "I love my work, but when I was little I dreamed about being a princess."
        bree.say "Your childhood dreams are so cute."
    $ lavish.love += 1
    return

label lavish_love_3_female:
    lavish.say "You only make that job better and more fun."
    $ lavish.love += 1

    return

label lavish_love_4_female:
    lavish.say "I hope one day we will work together 24/7."
    $ lavish.love += 1

    return

label lavish_love_5_female:
    lavish.say "You are probably the best coworker ever."
    $ lavish.love += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
