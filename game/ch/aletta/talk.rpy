label aletta_talk_love_male:
    mike.say "How about you, Aletta - do you believe in true love and all that stuff?"
    show aletta
    if aletta.is_visibly_pregnant:
        show aletta happy
        "Aletta rubs her swelling belly, smiling as she does so."
        aletta.say "I used to think it was all just chemicals screwing with the brain."
        aletta.say "That was before I had a symbol of our love growing, right here inside of me!"
        $ aletta.love += 1
    else:
        aletta.say "Love is an outdated concept, nothing more than a chemical reaction in the most primitive parts of the human brain."
        aletta.say "Passion, now there's something much more interesting to me!"
        menu:
            "Agree":
                mike.say "Couldn't have said it better myself."
                mike.say "Who wants to be a slave to a chemical reaction when you could be one to passion instead!"
                show aletta flirt
                "Aletta eyes me like a satisfied cat, seeming to know I'm trying to impress her, yet intrigued all the same."
                $ aletta.love += 1
            "Disagree":
                mike.say "That's not very romantic, now is it?"
                mike.say "I like to think that there's always the one out there, just waiting to sweep you off of your feet."
                show aletta annoyed
                aletta.say "Well, I hope you find the man of your dreams one day soon!"
    hide aletta
    return

label aletta_talk_sex_male:
    mike.say "We're all modern, emotionally mature adults here - so what do you say to us talking about sex?"
    show aletta
    if aletta.love < 40:
        "Aletta pulls down her glasses to regard me with one raised eyebrow."
        aletta.say "You really think that's something you want to chat to your boss about?"
        aletta.say "Because you could be opening up a whole new can of worms there."

    elif aletta.love < 80:
        show aletta happy
        "Aletta chuckles, shaking her head in amusement before she'll look me in the eye and answer the question."
        show aletta flirt
        aletta.say "You should be careful what you ask, for [hero.name]."
        aletta.say "I really don't think you'd be able to handle a woman like me!"
    elif aletta.love < 120:
        show aletta flirt
        "Aletta looks me up and down for a moment, like I'm a piece of meat that's been offered up to her."
        aletta.say "I like my men to be savage and strong, able to handle a woman of my calibre."
        show aletta dreamy
        aletta.say "I don't normally go for little shrimps like you!"
    else:
        show aletta flirt
        "Aletta removes her glasses, chewing on one of the arms as she looks me up and down."
        aletta.say "You might be worth a try at some point...if I'm ever in genuine need."
        $ aletta.love += 1
    hide aletta
    return

label aletta_talk_politics_male:
    mike.say "Hey, Aletta - did you see what that jackass in the White House said this time!"
    show aletta
    if aletta.sub >= 75:
        aletta.say "If you say so, [hero.name] - you know more about that kind of thing that me!"
        $ aletta.sub += 1
    else:
        aletta.say "Politics doesn't interest me the slightest - it's just a pissing contest for impotent, middle-aged white men."
        menu:
            "Agree":
                mike.say "Yeah, it's a bit of a pasty sausage party all right!"
                show aletta annoyed
                aletta.say "Urgh...are you just saying that to try and impress me?"
                $ aletta.love -= 1
            "Disagree":
                mike.say "That's just the kind of thing a reactionary femi-Nazi would say!"
                show aletta surprised
                aletta.say "Femi-what?!?"
    hide aletta
    return

label aletta_talk_food_male:
    show aletta talkative
    aletta.say "Let's say I like to get my food directly from the source."
    hide aletta
    return

label aletta_talk_travels_male:
    show aletta wink
    aletta.say "I don't think that I need to travel very far to find what I crave."
    $ aletta.love += 1
    hide aletta
    return

label aletta_talk_tv_male:
    show aletta annoyed
    aletta.say "I am bored, goodbye."
    hide aletta
    return

label aletta_talk_sports_male:
    show aletta talkative
    aletta.say "Speaking about sports, maybe you should work out a little more."
    hide aletta
    return

label aletta_talk_fashion_male:
    show aletta talkative
    aletta.say "I could spend my whole life trying clothes on."
    hide aletta
    return

label aletta_talk_books_male:
    show aletta talkative
    aletta.say "I don't read that much - print is a dead medium."
    hide aletta
    return

label aletta_talk_people_male:
    show aletta talkative
    aletta.say "Don't you have something interesting to say?"
    hide aletta
    return

label aletta_talk_computers_male:
    show aletta talkative
    aletta.say "Not interested."
    hide aletta
    return

label aletta_talk_music_male:
    show aletta annoyed
    aletta.say "Go away now."
    hide aletta
    return

label aletta_talk_birthday_male:
    show aletta
    mike.say "Happy birthday Aletta."
    show aletta happy
    aletta.say "Thank you [hero.name]."
    $ aletta.love += 1
    hide aletta
    return

init python:
    SpecificTalkSubject(**{
    "name": "aletta_talk_investigation",
    "display_name": "About the investigation",
    "label": "aletta_talk_investigation",
    "duration": 0,
    "icon": "button_investigate",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsFlag("underinvestigation"),
            MaxFlag("workinvestigation", 99)
            ),
        PersonTarget(aletta,
            IsActive(),
            ),
        ],
    "do_once": True,
    })

label aletta_talk_investigation:
    show aletta
    mike.say "Can we talk about this investigation?"
    show aletta embarrassed
    aletta.say "[hero.name], I really should not be talking to you about it."
    show aletta sad
    mike.say "But I'm being set up! And aren't I a good employee? Don't you want to get to the truth here?"
    show aletta annoyed
    "Aletta sighs."
    show aletta whining
    aletta.say "Look, [hero.name], there are rules. I have to follow those rules. We cannot discuss this."
    show aletta sad
    "Damn it."
    mike.say "Fine, but remember that I could go to jail over this. And I didn't steal the money."
    show aletta whining
    aletta.say "I know. I'm sorry this is happening."
    $ aletta.set_counter("investigationcallback")
    hide aletta
    return

label aletta_investigation_callback:
    play sound cell_vibrate loop
    "My phone buzzes. It's Aletta. I should answer it quickly, this could be important."
    stop sound
    $ result = renpy.call_screen("smartphone_choice", "Aletta")
    if not result:
        $ hero.cancel_event()
        $ aletta.love -= 5
        return
    aletta.say "Hi, [hero.name]. I'm sorry we couldn't talk earlier."
    mike.say "Thanks for calling. I really need some help here."
    aletta.say "I may have found something. Look into a subsidiary named Deewah Holdings, Limited. I think that has something to do with the money."
    aletta.say "And most important, that has nothing to do with you. If you can prove the money went through there and you didn't have any control, it might help."
    mike.say "Oh my God, Aletta! That's brilliant! Amazing! Thank you so much for the help! I love you for this!"
    if aletta.love > 160:
        aletta.say "I love you too!"
    mike.say "I owe you for this. If this all works out, anything you want."
    if aletta.love > 120 and aletta.sub < 5:
        aletta.say "Anything, really? I just might take you up on that..."
    else:
        aletta.say "Of course, [hero.name]. Happy to help."
    call investigation_points (max(aletta.love // 7, 5)) from _call_investigation_points_6
    return

init:
    define nickname_young_man = ["Young man", "young man"]
    define nickname_boss_buck = ["Boss Buck", "boss buck"]
    define nickname_cow_boy = ["Cow-boy, cow-boy"]

label command_nickname_aletta:
    menu:

        "Call me Young man" if active_girl.flags.mikeNickname not in nickname_young_man and active_girl.love > 100:
            $ active_girl.flags.mikeNickname = "Young man"
        "Stop calling me Young man" if active_girl.flags.mikeNickname in nickname_young_man:
            $ active_girl.flags.mikeNickname = None


        "Call me Boss Buck" if active_girl.flags.mikeNickname not in nickname_boss_buck and hero.flags.office_boss == "mike":
            $ active_girl.flags.mikeNickname = "Boss Buck"
        "Stop calling me Boss Buck" if active_girl.flags.mikeNickname in nickname_boss_buck:
            $ active_girl.flags.mikeNickname = None


        "Call me Cow-boy" if active_girl.flags.mikeNickname not in nickname_cow_boy and "aletta_event_04b" in DONE:
            $ active_girl.flags.mikeNickname = "Cow-boy"
        "Stop calling me Cow-boy" if active_girl.flags.mikeNickname in nickname_cow_boy:
            $ active_girl.flags.mikeNickname = None
        "Cancel":


            jump command_girl

label submissive_interact_aletta_male:
    show aletta
    mike.say "Ah, Aletta..."
    mike.say "I know that you're into your guns, ammo and all that."
    aletta.say "Hmm?"
    show aletta talkative
    aletta.say "Oh, yes - I suppose that I am."
    show aletta normal
    mike.say "Well, I was thinking that you could ask me to use you for target practice."
    mike.say "You know - when I shoot my load at you?"
    if aletta.sub >= 70 or aletta.is_sex_slave:
        show aletta talkative
        aletta.say "Oh, I see what you did there, [hero.name]."
        aletta.say "How clever of you!"
        show aletta happy
        aletta.say "Of course I will - anything to please you."
        show aletta normal
        $ aletta.flags.submissive_interact = True
    else:
        show aletta embarrassed
        aletta.say "Firstly, that is the weakest attempt at humour I've ever heard."
        show aletta angry
        aletta.say "And secondly, why would I humiliate myself by doing something like that?"
        show aletta upset
        mike.say "Ah...okay, Aletta."
        mike.say "It was a crazy idea anyway!"
        $ aletta.love -= 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
