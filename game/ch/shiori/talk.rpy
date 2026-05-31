label shiori_talk_love_male:
    show shiori
    mike.say "Shiori, what do you think true love actually is?"
    show shiori embarrassed
    if shiori.is_visibly_pregnant:
        shiori.say "I think that true love is having someone's child growing inside of you, nurturing it and bringing it into the world!"
    else:
        shiori.say "I think that love is being able to do anything for your man, no matter what he asks."
        shiori.say "It's having him dictate every aspect of your life..."
        $ shiori.sub += 1
    hide shiori
    return

label shiori_talk_sex_male:
    show shiori
    mike.say "What's your preference when it comes to sex, Shiori?"
    show shiori embarrassed
    if shiori.is_visibly_pregnant:
        "I hear that you can still have sex while you're pregnant..."
    else:
        shiori.say "Well...I can't imagine pleasure without at least a touch of pain..."
    $ shiori.sub += 1
    hide shiori
    return

label shiori_talk_politics_male:
    show shiori
    mike.say "Opinions on politics are like assholes everyone's got one - what are your politics, Shiori?"
    show shiori annoyed
    if shiori.is_visibly_pregnant:
        shiori.say "I don't know anything about politics."
        shiori.say "But you won't vote for anyone that'd hurt our baby, would you, [hero.name]?"
    else:
        shiori.say "Oh, I wouldn't know anything about all of that!"
        shiori.say "I just nod and smile when people start talking about politics."
    hide shiori
    return

label shiori_talk_food_male:
    show shiori
    mike.say "Most people tend to eat out these days - how about you, Shiori?"
    show shiori
    if shiori.is_visibly_pregnant:
        shiori.say "Since I got pregnant, I just can't stop eating!"
        shiori.say "If this keeps up, I'll be the size of a whale by the time the baby's due!"
    else:
        shiori.say "Oh no, I love making food!"
        shiori.say "I think that a woman should be able to cook a hearty meal for her man at the end of the working day."
    hide shiori
    return

label shiori_talk_travels_male:
    show shiori
    mike.say "I've always wanted to be able to take a year off and travel, you know - see the world."
    show shiori happy
    shiori.say "Not me, I'm happy as can be right were I am."
    $ shiori.love += 1
    hide shiori
    return

label shiori_talk_tv_male:
    show shiori
    mike.say "I need to start watching that new series on Netflix that everyone's talking about, tonight if I can."
    mike.say "You've heard about it, right, Shiori?"
    if shiori.is_visibly_pregnant:
        shiori.say "I'm usually so tired by the time I flop down on the sofa, I'm asleep in just a couple of minutes!"
    else:
        shiori.say "Nope - I mainly watch soaps, sometimes Reality TV shows."
    hide shiori
    return

label shiori_talk_sports_male:
    show shiori
    mike.say "All anyone's talking about in the office is the big game that's going to be on TV tonight."
    mike.say "Will you be watching it too, Shiori?"
    if shiori.is_visibly_pregnant:
        shiori.say "I'm usually so worn out by the time I collapse on the sofa, I'm snoring away in just a few minutes!"
    else:
        shiori.say "Oh no, I don't watch sports on TV, sorry."
    hide shiori
    return

label shiori_talk_fashion_male:
    show shiori
    mike.say "You're always pretty well dressed when you walk into the office, Shiori."
    if shiori.is_visibly_pregnant:
        shiori.say "Erm...nothing really fits me anymore, and I need to buy some maternity clothes, real soon!"
    else:
        shiori.say "Aw, thank you for saying so - I just love clothes and shopping!"
    hide shiori
    return

label shiori_talk_books_male:
    show shiori
    mike.say "I heard about this pretty hardcore new adult novel that apparently everyone's reading."
    mike.say "Have you heard of it...or read it?"
    if shiori.is_visibly_pregnant:
        shiori.say "No...but I did pick up this adorable book of baby names!"
    else:
        "Shiori giggles and shakes her head."
        shiori.say "Oh no...I don't read all that much."
        shiori.say "I think I might be too dumb to understand it!"
    hide shiori
    return

label shiori_talk_people_male:
    show shiori
    shiori.say "[hero.name], what do you think about children?"
    menu:
        "I hate them":
            mike.say "I really don't have much time for children."
            $ shiori.love -= 1
        "I love them":
            mike.say "I love them, Shiori - who doesn't?"
            show shiori happy
            $ shiori.love += 1
            if shiori.love >= 195:
                shiori.say "You know, I would love to have yours [hero.name]."
    hide shiori
    return

label shiori_talk_computers_male:
    show shiori
    mike.say "How are you coping with the latest software upgrades on your work computer, Shiori?"
    show shiori annoyed
    if shiori.is_visibly_pregnant:
        shiori.say "I can't even think about computers, not when I already have babies on the brain!"
    else:
        shiori.say "I'm not really very good with computers, they make my brain hurt!"
    hide shiori
    return

label shiori_talk_music_male:
    show shiori
    mike.say "I was going to play some music - do you have any preferences, Shiori?"
    show shiori
    if shiori.is_visibly_pregnant:
        shiori.say "Could you play some classical music?"
        shiori.say "It's supposed to be good for the baby!"
    else:
        shiori.say "Not really - I don't listen to music all that much."
    hide shiori
    return

label shiori_talk_birthday_male:
    show shiori
    mike.say "Happy birthday, Shiori!"
    show shiori happy
    shiori.say "Ah you remembered - that makes me feel so special!"
    $ shiori.love += 1
    hide shiori
    return

init python:
    SpecificTalkSubject(**{
    "name": "shiori_talk_investigation",
    "display_name": "About the investigation",
    "label": "shiori_talk_investigation_male",
    "duration": 0,
    "icon": "button_investigate",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsFlag("underinvestigation"),
            MaxFlag("workinvestigation", 99)
            ),
        PersonTarget(shiori,
            IsActive(),
            ),
        ],
    "do_once": True,
    })

label shiori_talk_investigation_male:
    show shiori
    mike.say "Shiori, do you know anything about this investigation?"
    show shiori annoyed
    shiori.say "I'm sorry, [hero.name], nobody talks to me about things like that."
    show shiori normal
    shiori.say "I'm sure it's just some kind of mistake and everything will be fine."
    mike.say "No, Shiori. Somebody set me up, and if I don't find out who and how, I'm going to get fired, and maybe go to jail!"
    show shiori surprised
    shiori.say "Oh no, that's terrible, [hero.name]! Is there anything I can do to help?"
    "I could ask Shiori to ask around, but she's about as subtle as those giant, milky melons she has. Maybe she could trade favors or something."
    show shiori sad
    "But on the other hand, I can't remember her ever getting anything right. Do I trust her to do this?"
    menu:
        "Ask her to help":
            $ shiori.set_counter("investigationcallback")
            mike.say "Maybe you could ask around the accountants and see if you can find anything out? Maybe if you...show off your assets."
            show shiori normal
            shiori.say "Whatever do you mean, [hero.name]?"
            mike.say "I mean...ugh, never mind. Just ask around?"
            show shiori happy
            shiori.say "Sure, I'll ask around, sir. People like me!"
            mike.say "Thanks for the help. Let me know what you find out."
        "She would only mess it up":
            mike.say "I don't think there's anything you can do, Shiori. But thank you very much for the offer."
            shiori.say "Okay, sir. If you think of anything I can do, you'll let me know?"
            mike.say "I will."
    hide shiori
    return

label shiori_investigation_callback:
    play sound cell_vibrate
    "My phone buzzes. It's Shiori. She said she'd get in touch, maybe she's got some good news?"
    $ result = renpy.call_screen("smartphone_choice", "Shiori")
    if not result:
        $ hero.cancel_event()
        $ shiori.love -= 5
        return
    mike.say "Shiori!"
    shiori.say "Hello, [hero.name]."
    "I asked around the accountants, like you asked. Can you believe one of them asked to see my boobs in exchange for information?"
    mike.say "No. I can't believe anyone would ask you that."
    "What I can't believe is that it was only one."
    mike.say "I hope you...well, did you get anything?"
    shiori.say "Yes, [hero.name]! I got a whole bunch of information! I sent it to you in an email."
    "Huh, she really got something? That's great!"
    mike.say "Thanks, Shiori! I really owe you one!"
    shiori.say "I'm here to serve, [hero.name]! Anything I can do for you makes me happy!"
    mike.say "Great! I'm going to look into this information now."
    "After I hang up, I look in my email. It's a dizzying array of accounting information, and none of it matches anything I already have."
    "It's really interesting, and it's going to take me hours to sort through it."
    "Unfortunately, as I will find out later, it's all fake, and it actually sets my investigation back."
    call investigation_points (-10) from _call_investigation_points_7
    return

init:
    define nickname_hero = ["Hero", "hero"]
    define nickname_owner = ["Owner", "owner"]
    define nickname_koibito = ["Koibito", "koibito"]
    define nickname_hanata = ["Hanata", "hanata"]
    define nickname_mr_boss_sir = ["Mr.Boss sir", "mr.boss sir"]

label command_nickname_shiori:
    menu:

        "Call me Hero" if active_girl.flags.mikeNickname not in nickname_hero and hero.fitness > 90 and hero.charm > 90 and hero.knowledge > 90:
            $ active_girl.flags.mikeNickname = "Hero"
        "Stop calling me Hero" if active_girl.flags.mikeNickname in nickname_hero:
            $ active_girl.flags.mikeNickname = None


        "Call me Owner" if active_girl.flags.mikeNickname not in nickname_owner and active_girl.status == "sex slave":
            $ active_girl.flags.mikeNickname = "Owner"
        "Stop calling me Owner" if active_girl.flags.mikeNickname in nickname_owner:
            $ active_girl.flags.mikeNickname = None


        "Call me Koibito" if active_girl.flags.mikeNickname not in nickname_koibito and active_girl.status in ["girlfriend"]:
            $ active_girl.flags.mikeNickname = "Koibito"
        "Stop calling me Koibito" if active_girl.flags.mikeNickname in nickname_koibito:
            $ active_girl.flags.mikeNickname = None


        "Call me Hanata" if active_girl.flags.mikeNickname not in nickname_hanata and active_girl.love > 120:
            $ active_girl.flags.mikeNickname = "Hanata"
        "Stop calling me Hanata" if active_girl.flags.mikeNickname in nickname_hanata:
            $ active_girl.flags.mikeNickname = None


        "Call me Mr.Boss sir" if active_girl.flags.mikeNickname not in nickname_mr_boss_sir and hero.flags.office_boss == "mike":
            $ active_girl.flags.mikeNickname = "Mr.Boss sir"
        "Stop calling me Mr.Boss sir" if active_girl.flags.mikeNickname in nickname_mr_boss_sir:
            $ active_girl.flags.mikeNickname = None
        "Cancel":


            jump command_girl

label submissive_interact_shiori_male:
    mike.say "Hey, Shiori..."
    mike.say "I got an idea!"
    show shiori surprised
    shiori.say "Huh..."
    shiori.say "What was it?"
    show shiori stuned
    mike.say "I loved milking you so much the other day."
    mike.say "I want you to ask me to do it again whenever you say hi to me!"
    if shiori.sub >= 70 or shiori.is_sex_slave:
        show shiori talkative blush
        shiori.say "I...I liked it too - a lot!"
        shiori.say "Just the thought of it makes me feel...horny!"
        shiori.say "Of course I'll do it."
        $ shiori.flags.submissive_interact = True
    else:
        show shiori whining
        shiori.say "B...but that was supposed to be just between us!"
        shiori.say "I couldn't live with people knowing you milked me like a cow!"
        show shiori sad
        mike.say "Okay, Shiori, okay - calm down!"
        mike.say "We'll forget all about it, I promise."
        $ shiori.love -= 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
