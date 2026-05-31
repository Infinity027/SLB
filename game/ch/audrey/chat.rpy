label audrey_desire_0_male:
    audrey.say "Oh god, but I'm bored."
    return

label audrey_desire_1_male:
    if audrey.love > 75:
        $ result = randint(1, 3)
        if result == 1:
            audrey.say "You really are quite hot, aren't you?"
        elif result == 2:
            audrey.say "Be honest with me - what do you think of my ass?"
        else:
            audrey.say "You know what's better than sex in the morning?"
            if audrey.flags.nickname == "toy":
                mike.say "No little Toy, what's better than sex in the morning?"
            else:
                mike.say "No Audrey, what's better than sex in the morning?"
            audrey.say "Butt!"
            mike.say "But what?"
            audrey.say "Butt sex in the morning!"
            $ audrey.love += 2
    else:
        audrey.say "I sometimes wish you had something interesting to say..."
        mike.say "Well, I'm sorry, but I don't do wishes."
        $ audrey.love += 1
    return

label audrey_desire_2_male:
    audrey.say "Is it my imagination, or have you been working out recently?"
    $ audrey.love += 1
    return

label audrey_desire_3_male:
    audrey.say "You know it's kinda hard for me to work when we're in the same room."
    audrey.say "You really sorta distract me."
    $ audrey.love += 1
    return

label audrey_desire_4_male:
    $ result = randint(2, 4)
    if result == 2:
        audrey.say "Spanking is one hand clapping in appreciation of a magnificent ass."
    elif result == 3:
        audrey.say "When I woke up this morning, it felt like something was missing..."
        audrey.say "It was the taste of your cum on my lips..."
    else:
        mike.say "God...I just have to have you."
        audrey.say "Take me...own me...use me."
        audrey.say "Pick a verb, but just please...do it!"
        mike.say "Fuck you."
        mike.say "I'm going to fuck you."
        mike.say "There, that's my verb."
        $ audrey.love += 1
    return

label audrey_desire_5_male:
    $ result = randint(1, 2)
    if result == 1:
        audrey.say "It's hard for an educated woman, to turn her brain off, that is."
        audrey.say "That's probably the largest part of the pleasure I find in being a sub."
        audrey.say "None of the decisions are yours, none of the responsibilities either."
        audrey.say "When you can't refuse any request, when you sometimes can't even move - then those voices finally fall silent."
        audrey.say "All that you can do, all you're allowed to do, is just to feel."
    else:
        mike.say "I like the idea of marooning you on an island."
        audrey.say "Oh...why is that?"
        "She's squinting up at me now, her dark eyes like the sea on a moonless night."
        mike.say "So I could keep you trapped there, where only I could reach you."
        mike.say "You'd be my hostage, totally at my mercy..."
        mike.say "I'd be your Odysseus, you'd be my Circe..."
        "She laughs and reaches her hand out to me."
        audrey.say "You already have that kind of power over me...without a sea and an island!"
    $ audrey.love += 1
    return

label audrey_love_0_male:
    if randint(1, 2) == 1 and Person.is_not_hidden("aletta"):
        audrey.say "Fucking hell - Aletta is such a bitch..."
        $ audrey.love += 1
    else:
        audrey.say "Oh god, but I'm bored."
    return

label audrey_love_1_male:
    audrey.say "All men love a submissive woman."
    audrey.say "Those that say they don't are just lying to themselves."
    audrey.say "There's just something about a beautiful, vulnerable woman."
    audrey.say "Especially one looking to them for protection and to be taken care of."
    audrey.say "It can inspire a man to greatness."
    $ audrey.love += 1
    return

label audrey_love_2_male:
    if not audrey.flags.birthdayknown:
        if audrey.flags.nickname == "toy":
            mike.say "Hey Toy - just when is your birthday?"
        else:
            mike.say "Hey Audrey - just when is your birthday?"
        audrey.say "It's on the [audrey.birthday[1]] of [audrey.birthday[0]]."
        audrey.say "Why - are you thinking of getting me a gift?"
        mike.say "Maybe...just wait and see..."
        $ audrey.flags.birthdayknown = True
    else:
        audrey.say "Jesus Christ - I hate my work."
        audrey.say "When I was little, I always dreamed about being a pornstar."
        mike.say "Wow, your childhood dreams sure are cute!"
    $ audrey.love += 1
    return

label audrey_love_3_male:
    audrey.say "I truly hate that job - without you it'd be intolerable."
    $ audrey.love += 1

    return

label audrey_love_4_male:
    audrey.say "Why don't we both tell them to go shove their shitty jobs at the same time?"
    $ audrey.love += 1
    return

label audrey_love_5_male:
    audrey.say "You know, you're probably the best co-worker I've ever had."
    $ audrey.love += 1
    return

label audrey_good_sweet_talk_male:
    show audrey
    if audrey.love > 133:
        mike.say "Wow, Audrey!"
        mike.say "You look good, you're great in bed too!"
        mike.say "Is there anything you can't do?"
        show audrey flirt
        audrey.say "No, I'm pretty much perfect!"
    elif audrey.love > 66:
        mike.say "You look SO hot, Audrey!"
        mike.say "And I'm so lucky to be out with you!"
        audrey.say "Aw, thanks!"
        show audrey flirt
        audrey.say "But you're right on both counts..."
    else:
        mike.say "Your pranks make me crazy, Audrey."
        mike.say "But in a good kind of way, you know?"
        show audrey joke
        audrey.say "Yeah, I think I get what you mean!"
    hide audrey
    return

label audrey_bad_sweet_talk_male:
    show audrey
    mike.say "You know, Audrey, once a person gets to know you, you're a lot of fun!"
    show audrey annoyed
    audrey.say "Oh, I heard that one before!"
    audrey.say "Everyone starts out thinking I'm just a bitch."
    audrey.say "Seem you did too!"
    mike.say "That's not exactly what I meant!"
    hide audrey
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
