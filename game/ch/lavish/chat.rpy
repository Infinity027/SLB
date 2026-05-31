label lavish_desire_0_male:
    "Lavish is happily humming."
    $ lavish.love += 1
    return

label lavish_desire_1_male:
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
        mike.say "Fine."
        $ lavish.love += 1
    return

label lavish_desire_2_male:
    lavish.say "I love working with you."
    $ lavish.love += 1
    return

label lavish_desire_3_male:
    lavish.say "Do you think you will be promoted soon?"
    $ lavish.love += 1
    return

label lavish_desire_4_male:
    $ result = randint(1, 4)
    if result == 1:
        lavish.say "It's crazy how good you are at your job."
    elif result == 2:
        lavish.say "Do you think I should let my hair grow?"
    elif result == 3:
        lavish.say "What do you think about office relationships?"
    else:
        mike.say "How are you doing today Lavish?"
        lavish.say "Fine, thanks for asking."
    $ lavish.love += 1
    return

label lavish_desire_5_male:
    lavish.say "I think I am in love with you."
    $ lavish.love += 1
    return

label lavish_love_0_male:
    if randint(1, 2) == 1 and Person.is_not_hidden("aletta"):
        lavish.say "Aletta is such a great boss."
    else:
        "Lavish is happily humming."
    $ lavish.love += 1
    return

label lavish_love_1_male:
    if randint(1, 2) == 1 and Person.is_not_hidden("shiori"):
        lavish.say "What do you think about Shiori?"
        menu:
            "She's cute":
                $ lavish.love -= 1
                mike.say "I think she's cute."
            "She's very professional":
                $ lavish.love += 1
                mike.say "She's very good at her job and has a very professional attitude."
    else:
        lavish.say "I love working with you."
        $ lavish.love += 1
    return

label lavish_love_2_male:
    $ nbr = randint(1, 2)
    if not lavish.flags.birthdayknown and nbr == 1:
        mike.say "Hey Lavish, when is your birthday?"
        lavish.say "It's on the [lavish.birthday[1]] of [lavish.birthday[0]]."
        lavish.say "Are you planning on getting me a gift?"
        mike.say "Maybe..."
        $ lavish.flags.birthdayknown = True
    else:
        lavish.say "I love my work, but when I was little I dreamed about being a princess."
        mike.say "Your childhood dreams are so cute."
    $ lavish.love += 1
    return

label lavish_love_3_male:
    lavish.say "You only make that job better and more fun."
    $ lavish.love += 1

    return

label lavish_love_4_male:
    lavish.say "I hope one day we will work together 24/7."
    $ lavish.love += 1

    return

label lavish_love_5_male:
    lavish.say "You are probably the best coworker ever."
    $ lavish.love += 1
    return

label lavish_good_sweet_talk_male:
    show lavish
    if lavish.love > 133:
        mike.say "You're a professional at work, Lavish."
        mike.say "But you're kind of a wild animal in the bedroom!"
        show lavish surprised blush
        lavish.say "Sssh...someone might hear you!"
        lavish.say "What happens in the bedroom's just for the two of us!"
    elif lavish.love > 66:
        mike.say "You always look SO good, Lavish."
        mike.say "I don't know how you do it!"
        show lavish flirt
        lavish.say "Thank you for noticing, [hero.name]!"
        lavish.say "I do try hard to make the right impression."
    else:
        mike.say "You work hard at the office, Lavish."
        mike.say "But you really know how to relax away from it too."
        show lavish happy
        lavish.say "Thank you!"
        lavish.say "It's good to know when to change gear."
    hide lavish
    return

label lavish_bad_sweet_talk_male:
    show lavish
    mike.say "Wow, Lavish - you sure do work hard!"
    show lavish angry
    lavish.say "Of course I do - I don't have any other choice!"
    lavish.say "You have no idea how hard it is to be a woman in a man's world!"
    mike.say "Ouch...maybe we should forget I mentioned it?"
    hide lavish
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
