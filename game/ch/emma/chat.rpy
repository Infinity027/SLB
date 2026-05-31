label emma_desire_0_male:
label emma_desire_1_male:
label emma_desire_2_male:
label emma_desire_3_male:
label emma_desire_4_male:
label emma_desire_5_male:
label emma_love_0_male:
label emma_love_1_male:
label emma_love_2_male:
label emma_love_3_male:
label emma_love_4_male:
label emma_love_5_male:
    call expression conditional_choice_picker(EMMA_CHATS_MALE) from _call_expression_226
    return

define EMMA_CHATS_MALE = {
                            "emma_chat_manga_male": (True, 1),
                            "emma_chat_family_male": ("emma.love > 75", 1),
                            "emma_chat_clouds_male": (True, 2),
                            "emma_chat_notwork_male": (True, 1),
                            "emma_chat_school_male": ("emma.love >= 75", 1),
                            "emma_chat_favoritefood_male": (True, 1),
                            "emma_chat_rp_male": ("emma.love > 120", 1),
                            "emma_chat_hugs_male": ("emma.love > 60", 1),
                            "emma_chat_japan_male": (True, 1)
                        }

label emma_chat_manga_male:
    emma.say "Do you read any manga?"
    mike.say "Not really."
    emma.say "Oh, that's too bad. I really like it."
    mike.say "What are your favorites?"
    emma.say "Orange Highway, No Need for Benji, Mariko-hime. Oh, Boku ni Hana no Sadness!"
    mike.say "I've heard of a couple of those."
    emma.say "Maybe you should read more!"
    menu:
        "I will":
            mike.say "I'll look some of those up!"
            $ emma.love += 1
        "I'm not really interested":
            mike.say "That doesn't sound very interesting to me."
            $ emma.love -= 1
    return


label emma_chat_family_male:
    emma.say "I miss my sisters."
    if not emma.flags.toldsisters:
        mike.say "You never did tell me that story."
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
                    mike.say "That's what makes you sad?"
                    emma.say "No. I loved it, honestly. I loved my family so much. It's the next part."
                    "She takes a deep breath."
                    emma.say "About a month after I left home for school, they, uh. They..."
                    "Her voice starts to crack."
                    emma.say "Krissa had a recital, you see, and they were all on their way and a drunk hit them head on, on the freeway."
                    emma.say "The cop on the phone said they all died instantly."
                    mike.say "Oh no, I'm so...I'm sorry!"
                    emma.say "No no, don't be sorry. Life happens. But now you see why I don't like to talk about it."
                    mike.say "Well, I'm sorry anyway."
                    emma.say "You're a good man, [hero.name]."
            "Then let's talk about something else":
                mike.say "Then let's talk about something else. How's work been?"
                emma.say "Oh, you know. Work's good."
    else:
        mike.say "I didn't know them, but I'm glad they had you."
        emma.say "I'm sorry, I'm getting maudlin, aren't I?"
        mike.say "It's okay."
    $ emma.love += 1
    return


label emma_chat_clouds_male:
    emma.say "When you look at the clouds, do you see shapes? Or just clouds?"
    mike.say "Um. Sometimes, I guess, if one is really particularly shaped, but usually just clouds."
    emma.say "Oh. I see shapes all the time. I see faces, places, animals, buildings, bridges."
    emma.say "Sometimes I see mecha fighting. Is that weird?"
    menu:
        "Yes, it's weird":
            mike.say "Yes, that's weird."
            emma.say "I thought so."
        "No, it's adorable":
            mike.say "No, it's adorable. It just shows you have a very active imagination."
            $ emma.love += 1
    return


label emma_chat_notwork_male:
    emma.say "What do you do when you're not working?"
    mike.say "Um. Go out on dates, hang out at the beach, stuff like that."
    emma.say "Oh, you date a lot?"
    $ renpy.dynamic("girls")
    $ girls = len(list(Girl.filter(lambda x: x.flags.dates)))
    if girls > 5:
        mike.say "I have."
    elif girls > 2:
        mike.say "A few."
    else:
        mike.say "Not a lot, I guess."
        $ emma.love += 1
    emma.say "Oh. I've not really dated much. I don't know what it's like to date a lot of people."
    mike.say "It's good to figure out what it is you really want."
    return


label emma_chat_school_male:
    emma.say "One of the kids I teach at school, he's so cute. He flirts with {b}all{/b} the girls, though most of them don't quite realize it."
    emma.say "The other boys don't get it, they're not really ready for that."
    mike.say "Maturing a little fast, is he?"
    emma.say "Maybe. But he reminds me of you."
    mike.say "I'm glad you said you think he's cute, then!"
    $ emma.flags.love += 1
    return

label emma_chat_favoritefood_male:
    emma.say "What's your favorite food?"
    menu:
        "Pizza":
            mike.say "I like pizza a lot."
            emma.say "Pizza is good. Crust, sauce, cheese. Maybe meat, maybe veggies. Kind of a bit of everything!"
            $ emma.love += 1
        "Burgers":
            mike.say "I guess I eat a lot of burgers."
            emma.say "You should eat healthier. Of course, I should eat healthier too, so that makes us even."
        "Pasta":
            mike.say "I love pasta. A little too much!"
            emma.say "Oh I especially love pasta when it's fresh!"
            if hero.has_skill("cooking"):
                mike.say "I should make some for you sometime, then. It's one of my specialties!"
            else:
                mike.say "Me too, but it's too hard to get at home."
            $ emma.love += 1
    return

label emma_chat_rp_male:
    emma.say "Do you like to roleplay?"
    mike.say "You mean like Dungeons and Dragons?"
    emma.say "Oh. Yeah that too, I guess."
    mike.say "Sure. Unless you meant something else?"
    emma.say "I meant, um. I guess, more...um. Intimate, maybe?"
    mike.say "Oh. I've never tried it."
    emma.say "Would you try it, if you were asked?"
    mike.say "Probably!"
    $ emma.love += 1
    return

label emma_chat_hugs_male:
    emma.say "Have you ever just seen someone and wanted to hug them as hard as you can for as long as you can?"
    mike.say "Did you have someone specific in mind?"
    emma.say "M-maybe!"
    $ emma.love += 1
    return

label emma_chat_japan_male:
    emma.say "Have you ever been to Japan?"
    mike.say "No."
    emma.say "Me either. I'd like to go someday."
    $ emma.love += 1
    return

label emma_good_sweet_talk_male:
    show emma
    if emma.love > 133:
        mike.say "When we make love, I don't know if I'm awake or dreaming."
        mike.say "It's so good to be with you, Emma!"
        show emma happy
        emma.say "I feel that way too!"
        emma.say "I love you, [hero.name]!"
    elif emma.love > 66:
        mike.say "I'm so happy that we got together, Emma."
        mike.say "What other guy can say he's dating the girl of his dreams - literally!"
        show emma happy
        emma.say "Oh, [hero.name]!"
        emma.say "You always know just what to say!"
    else:
        mike.say "I'm glad you weren't just a figment of my imagination, Emma."
        mike.say "Because you're a better friend than anything I could have imagined!"
        show emma blush
        emma.say "Oh...that's so sweet!"
    hide emma
    return

label emma_bad_sweet_talk_male:
    show emma
    mike.say "You're so quiet, Emma - sometimes I forget you're there at all!"
    show emma angry
    emma.say "That's really not a nice thing to say!"
    emma.say "It makes me think you don't notice me!"
    mike.say "Oh...when you put it like that..."
    mike.say "Sorry, Emma!"
    hide emma
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
