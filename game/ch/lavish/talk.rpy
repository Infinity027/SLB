label lavish_talk_love_male:
    show lavish flirt
    if lavish.love <= 100:
        lavish.say "I hope to fall in love someday..."
    elif lavish.love <= 150:
        lavish.say "I think I am in love with someone."
    else:
        lavish.say "I love you so much..."
    $ lavish.love += 1
    hide lavish
    return

label lavish_talk_sex_male:
    show lavish flirt
    if not lavish.sexperience:
        lavish.say "Never been so interested in sex."
    else:
        lavish.say "Sex with you is so fantastic I think I'll end up addicted."
        $ lavish.sub += 1
    hide lavish
    return

label lavish_talk_politics_male:
    show lavish
    lavish.say "It's our responsibility as citizens to be aware of that!"
    $ lavish.love += 1
    hide lavish
    return

label lavish_talk_food_male:
    show lavish happy
    lavish.say "I do love a good meal in a nice restaurant."
    $ lavish.love += 1
    hide lavish
    return

label lavish_talk_travels_male:
    show lavish happy
    lavish.say "I wanna see Europe one day."
    $ lavish.love += 1
    hide lavish
    return

label lavish_talk_tv_male:
    show lavish
    lavish.say "I don't really care about TV, but I love going to the cinema."
    $ lavish.love += 1
    hide lavish
    return

label lavish_talk_sports_male:
    show lavish
    lavish.say "Not so interested in sports, well except for health reasons."
    hide lavish
    return

label lavish_talk_fashion_male:
    show lavish flirt
    if not lavish.sub >= 75:
        lavish.say "I love to always look classy."
    else:
        if lavish.flags.sexyswimsuit:
            lavish.say "I kind of start liking those slutty clothes you bought me."
            $ lavish.sub += 1
        else:
            lavish.say "I love to always look classy."
    $ lavish.love += 1
    hide lavish
    return

label lavish_talk_books_male:
    show lavish bored
    lavish.say "I am not really a bookish girl."
    $ lavish.love -= 1
    hide lavish
    return

label lavish_talk_people_male:
    show lavish
    lavish.say "Humanity is wonderful."
    hide lavish
    return

label lavish_talk_computers_male:
    show lavish bored
    lavish.say "Not interested."
    $ lavish.love -= 1
    hide lavish
    return

label lavish_talk_music_male:
    show lavish
    lavish.say "A little bit of this, a little bit of that."
    hide lavish
    return

label lavish_talk_birthday_male:
    show lavish
    mike.say "Happy birthday Lavish."
    show lavish happy
    lavish.say "Thank you [hero.name]."
    $ lavish.love += 3
    hide lavish
    return

init python:
    SpecificTalkSubject(**{
    "name": "lavish_talk_investigation",
    "display_name": "About the investigation",
    "label": "lavish_talk_investigation_male",
    "duration": 0,
    "icon": "button_investigate",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsFlag("underinvestigation"),
            MaxFlag("workinvestigation", 99)
            ),
        PersonTarget(lavish,
            IsActive(),
            ),
        ],
    "do_once": True,
    })

label lavish_talk_investigation_male:
    show lavish
    mike.say "Lavish, do you know anything about this investigation?"
    show lavish annoyed
    lavish.say "I'm sorry, I'm just an intern, that's way above my pay grade."
    lavish.say "So, did you do it?"
    mike.say "Steal the money? No! I'd never do anything like that."
    show lavish normal
    lavish.say "What's going on, then?"
    if 'cassidy_hold_meeting' in DONE:
        mike.say "Someone set me up, and I think the CEO's daughter and someone in accounting is involved."
        if game.flags.toldjeff:
            mike.say "There's a guy over there named Jeff, I think he helped change the numbers."
        mike.say "Someone set me up. I don't know who, but whoever it is can make changes in our accounting systems."
    lavish.say "Hmm. I'll do some digging, maybe someone over there knows something. Some of the other interns and I go for drinks."
    mike.say "Okay, but be careful, Lavish. Whatever's going on is serious, and if you aren't careful you could be implicated too."
    show lavish angry
    lavish.say "Whatever, [hero.name]. I can find a new job -- I don't want to work at a place that does this to their employees."
    mike.say "Thank you, Lavish. I really appreciate it."
    show lavish normal
    lavish.say "Sure. I'll get in touch."
    $ lavish.set_counter("investigationcallback")
    hide lavish
    return

label lavish_investigation_callback:
    play sound cell_vibrate loop
    "My phone buzzes. It's Lavish. She said she'd get in touch, maybe she's got some good news?"
    stop sound
    $ result = renpy.call_screen("smartphone_choice", "Lavish")
    if not result:
        $ hero.cancel_event()
        $ lavish.love -= 5
        return
    mike.say "Lavish!"
    lavish.say "Hey, [hero.name]. I did some asking around, like you asked. I may have something useful for you."
    mike.say "Spill it!"
    lavish.say "Everyone in accounting has been on edge the last few weeks. A lot of strange requests have come down from the top. Multiple audits, but also some secret budget changes."
    lavish.say "And apparently Dwayne himself has been taking meetings with an accountant named Jeff."
    lavish.say "Word is, Jeff used to be considered a bad employee, and everyone thought he was going to be fired."
    lavish.say "Then, all of a sudden, he ends up promoted. He's a director now, has his own office, and nobody knows who he actually reports to. It's hidden in the system."
    lavish.say "I'll send you some more details my friend dug up too. I hope it helps."
    mike.say "That is really helpful, Lavish! Thank you!"
    lavish.say "No problem, [hero.name]. I really hope you don't get fired. I'll miss you here."
    if lavish.love > 120:
        lavish.say "I mean, REALLY miss you."
    mike.say "Aw, that's sweet! Thanks! And I owe you one, Lavish!"
    lavish.say "Good luck!"
    call investigation_points (10 + max(lavish_love // 7, 5)) from _call_investigation_points_2
    return

init:
    define nickname_boss = ["Boss", "boss"]
    define nickname_perv = ["Perv", "perv"]

label command_nickname_lavish:
    menu:

        "Call me Boss" if active_girl.flags.mikeNickname not in nickname_boss and hero.flags.office_boss == "mike":
            $ active_girl.flags.mikeNickname = "Boss"
        "Stop calling me Boss" if active_girl.flags.mikeNickname in nickname_boss:
            $ active_girl.flags.mikeNickname = None


        "Call me Perv" if active_girl.flags.mikeNickname not in nickname_perv and active_girl.flags.peeped_count >= 1:
            $ active_girl.flags.mikeNickname = "Perv"
        "Stop calling me Perv" if active_girl.flags.mikeNickname in nickname_perv:
            $ active_girl.flags.mikeNickname = None
        "Cancel":


            jump command_girl

label submissive_interact_lavish_male:
    mike.say "Hey, Lavish..."
    mike.say "I wanted to ask you something."
    show lavish talkative
    lavish.say "Oh, okay - what was it?"
    show lavish normal
    mike.say "Well, I was wondering if, when you say hi to me..."
    mike.say "You could maybe work in a compliment too?"
    mike.say "Maybe about how much you're into me?"
    if lavish.sub >= 70 or lavish.is_sex_slave:
        show lavish surprised
        lavish.say "Oh...that's not what I was expecting you to say!"
        show lavish flirt
        lavish.say "But if that's what you really want, [hero.name]..."
        lavish.say "Then I'll be sure to think something up."
        $ lavish.flags.submissive_interact = True
    else:
        show lavish angry
        lavish.say "Oh, come on, [hero.name] - you can't be serious?"
        lavish.say "We might be seeing each other outside of work."
        lavish.say "But I still have standards to maintain!"
        show lavish upset
        mike.say "Ah...okay, Lavish - let's forget about it..."
        $ lavish.love -= 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
