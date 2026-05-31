label emma_desire_0_female:
label emma_desire_1_female:
label emma_desire_2_female:
label emma_desire_3_female:
label emma_desire_4_female:
label emma_desire_5_female:
label emma_love_0_female:
label emma_love_1_female:
label emma_love_2_female:
label emma_love_3_female:
label emma_love_4_female:
label emma_love_5_female:
    call expression conditional_choice_picker(EMMA_CHATS_FEMALE) from _call_expression_391
    return

define EMMA_CHATS_FEMALE = {
                            "emma_chat_manga_female": (True, 1),
                            "emma_chat_family_female": ("emma.love > 75", 1),
                            "emma_chat_clouds_female": (True, 2),
                            "emma_chat_notwork_female": (True, 1),
                            "emma_chat_school_female": ("emma.love >= 75", 1),
                            "emma_chat_favoritefood_female": (True, 1),
                            "emma_chat_rp_female": ("emma.love > 120", 1),
                            "emma_chat_hugs_female": ("emma.love > 60", 1),
                            "emma_chat_japan_female": (True, 1)
                            }


label emma_chat_manga_female:
    emma.say "Do you read any manga?"
    bree.say "Not really."
    emma.say "Oh, that's too bad. I really like it."
    bree.say "What are your favorites?"
    emma.say "Orange Highway, No Need for Benji, Mariko-hime. Oh, Boku ni Hana no Sadness!"
    bree.say "I've heard of a couple of those."
    emma.say "Maybe you should read more!"
    menu:
        "I will":
            bree.say "I'll look some of those up!"
            $ emma.love += 1
        "I'm not really interested":
            bree.say "That doesn't sound very interesting to me."
            $ emma.love -= 1
    return

label emma_chat_family_female:
    emma.say "I miss my sisters."
    if not emma.flags.toldsisters:
        bree.say "You never did tell me that story."
        emma.say "Oh, I...I don't want to depress you."
        menu:
            "It's okay, I'm here for you":
                if emma.love < 100:
                    show emma sad
                    emma.say "I don't think I'm ready to talk about it with you yet."
                    emma.say "But I appreciate the sentiment."
                else:
                    $ emma.flags.toldsisters = True
                    emma.say "Growing up, I was the oldest of three. All girls. Mom and Dad both worked. Mom worked a lot actually, and had to travel."
                    emma.say "So a lot of times it was just Dad, and when I got old enough, I started doing a lot of things Mom would do."
                    bree.say "That's what makes you sad?"
                    emma.say "No. I loved it, honestly. I loved my family so much. It's the next part."
                    "She takes a deep breath."
                    emma.say "About a month after I left home for school, they, uh. They..."
                    "Her voice starts to crack."
                    emma.say "Krissa had a recital, you see, and they were all on their way and a drunk hit them head on, on the freeway."
                    emma.say "The cop on the phone said they all died instantly."
                    bree.say "Oh no, I'm so...I'm sorry!"
                    emma.say "No no, don't be sorry. Life happens. But now you see why I don't like to talk about it."
                    bree.say "Well, I'm sorry anyway."
                    emma.say "You're a good man, [hero.name]."
            "Then let's talk about something else":
                bree.say "Then let's talk about something else. How's work been?"
                emma.say "Oh, you know. Work's good."
    else:
        bree.say "I didn't know them, but I'm glad they had you."
        emma.say "I'm sorry, I'm getting maudlin, aren't I?"
        bree.say "It's okay."
    $ emma.love += 1
    return

label emma_chat_clouds_female:
    emma.say "When you look at the clouds, do you see shapes? Or just clouds?"
    bree.say "Um. Sometimes, I guess, if one is really particularly shaped, but usually just clouds."
    emma.say "Oh. I see shapes all the time. I see faces, places, animals, buildings, bridges."
    emma.say "Sometimes I see mecha fighting. Is that weird?"
    menu:
        "Yes, it's weird":
            bree.say "Yes, that's weird."
            emma.say "I thought so."
        "No, it's adorable":
            bree.say "No, it's adorable. It just shows you have a very active imagination."
            $ emma.love += 1
    return

label emma_chat_notwork_female:
    emma.say "What do you do when you're not working?"
    bree.say "Um. Go out on dates, hang out at the beach, stuff like that."
    emma.say "Oh, you date a lot?"
    $ renpy.dynamic("girls")
    $ girls = len(list(Girl.filter(lambda x: x.flags.dates)))
    if girls > 5:
        bree.say "I have."
    elif girls > 2:
        bree.say "A few."
    else:
        bree.say "Not a lot, I guess."
        $ emma.love += 1
    emma.say "Oh. I've not really dated much. I don't know what it's like to date a lot of people."
    bree.say "It's good to figure out what it is you really want."
    return

label emma_chat_school_female:
    emma.say "One of the kids I teach at school, he's so cute. He flirts with {b}all{/b} the girls, though most of them don't quite realize it."
    emma.say "The other boys don't get it, they're not really ready for that."
    bree.say "Maturing a little fast, is he?"
    emma.say "Maybe. But he reminds me of you."
    bree.say "I'm glad you said you think he's cute, then!"
    $ emma.flags.love += 1
    return

label emma_chat_favoritefood_female:
    emma.say "What's your favorite food?"
    menu:
        "Pizza":
            bree.say "I like pizza a lot."
            emma.say "Pizza is good. Crust, sauce, cheese. Maybe meat, maybe veggies. Kind of a bit of everything!"
            $ emma.love += 1
        "Burgers":
            bree.say "I guess I eat a lot of burgers."
            emma.say "You should eat healthier. Of course, I should eat healthier too, so that makes us even."
        "Pasta":
            bree.say "I love pasta. A little too much!"
            emma.say "Oh I especially love pasta when it's fresh!"
            if hero.has_skill("cooking"):
                bree.say "I should make some for you sometime, then. It's one of my specialties!"
            else:
                bree.say "Me too, but it's too hard to get at home."
            $ emma.love += 1
    return

label emma_chat_rp_female:
    emma.say "Do you like to roleplay?"
    bree.say "You mean like Dungeons and Dragons?"
    emma.say "Oh. Yeah that too, I guess."
    bree.say "Sure. Unless you meant something else?"
    emma.say "I meant, um. I guess, more...um. Intimate, maybe?"
    bree.say "Oh. I've never tried it."
    emma.say "Would you try it, if you were asked?"
    bree.say "Probably!"
    $ emma.love += 1
    return

label emma_chat_hugs_female:
    emma.say "Have you ever just seen someone and wanted to hug them as hard as you can for as long as you can?"
    bree.say "Did you have someone specific in mind?"
    emma.say "M-maybe!"
    $ emma.love += 1
    return

label emma_chat_japan_female:
    emma.say "Have you ever been to Japan?"
    bree.say "No."
    emma.say "Me either. I'd like to go someday."
    $ emma.love += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
