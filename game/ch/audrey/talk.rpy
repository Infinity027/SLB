label audrey_talk_love_male:
    show audrey
    mike.say "What's your take on love, Audrey?"
    if audrey.is_visibly_pregnant:
        audrey.say "I know that I love having your baby inside of me."
        show audrey joke
        audrey.say "Almost as much as I like having you inside of me..."
    else:
        audrey.say "Love?"
        audrey.say "Hah - it's just a longer, more boring word for sex..."
        mike.say "Well, it's only one letter longer..."
        show audrey joke
        audrey.say "Yeah, but it's whole lot more boring."
    $ audrey.love += 1
    hide audrey
    return

label audrey_talk_sex_male:
    show audrey
    mike.say "You have any words of wisdom when it comes to sex, Audrey?"
    if audrey.is_visibly_pregnant:
        audrey.say "I can't say that being pregnant has affected my sex-drive."
        show audrey joke
        audrey.say "If anything, it's made me want it all the more..."
    else:
        audrey.say "Hmm...I always say that sex is the best way to spend an afternoon."
        show audrey joke
        audrey.say "But kinky sex...that's the best way to spend an entire weekend."
    $ audrey.love += 1
    hide audrey
    return

label audrey_talk_politics_male:
    show audrey
    mike.say "What about you, Audrey - what are your personal politics?"
    show audrey annoyed
    if audrey.is_visibly_pregnant:
        audrey.say "I couldn't care less about politics, except for when it comes to my rights and my body."
        audrey.say "There's only one man that I want having any say over what happens to my body..."
    else:
        audrey.say "I'm not that interested in politics."
        audrey.say "Well, except for office politics, especially when it involves the occasional blowjob."
    $ audrey.love -= 1
    hide audrey
    return

label audrey_talk_food_male:
    show audrey
    mike.say "I'm thinking of slipping out to grab some lunch - what's your preference, Audrey?"
    if audrey.is_visibly_pregnant:
        audrey.say "Everything's gotten screwed up with my appetite since I got pregnant."
        show audrey flirt
        audrey.say "I got my cravings pretty bad, and all I want to eat is cock!"
    else:
        audrey.say "Well, I love my food as fresh from the source as I can get it."
        show audrey flirt
        audrey.say "That's one of the reasons that I just love blowjobs."
    $ audrey.love += 1
    hide audrey
    return

label audrey_talk_travels_male:
    show audrey
    mike.say "Where's that one dream trip to, Audrey - the one you've been planning your entire life?"
    if audrey.is_visibly_pregnant:
        audrey.say "You better have a good babysitter lined up for when this kid arrives."
        show audrey happy
        audrey.say "As I still want to achieve my ambition for each and every continent..."
    else:
        show audrey happy
        audrey.say "I'd love to travel around the globe."
        audrey.say "That way I could finally achieve my ambition of being fucked at least once on every continent."
    $ audrey.love += 1
    hide audrey
    return

label audrey_talk_tv_male:
    show audrey
    mike.say "Seen anything decent on TV recently, Audrey?"
    show audrey annoyed
    if audrey.is_visibly_pregnant:
        audrey.say "I keep falling asleep on the couch in the evenings - maybe you could help me stay awake?"
    else:
        audrey.say "I don't really care about TV, at least when it comes to actually watching it."
        audrey.say "There's far better things to do on a couch..."
    $ audrey.love -= 1
    hide audrey
    return

label audrey_talk_sports_male:
    show audrey
    mike.say "You always struck me as the sporty type, Audrey."
    show audrey happy
    if audrey.is_visibly_pregnant:
        audrey.say "The bump might mean that I can't do some of the vertical exercises that I used to like so much."
        audrey.say "But I can still do a whole lot of stuff when I'm horizontal..."
    else:
        $ result = randint(1, 2)
        if result == 1:
            audrey.say "Well, it's important to have a good stamina."
            audrey.say "If you want to be able to enjoy every night to the full."
        else:
            audrey.say "I've always loved being able to exercise - I think I like martial arts training the most of all."
    $ audrey.love += 1
    hide audrey
    return

label audrey_talk_fashion_male:
    show audrey
    mike.say "You look pretty glamorous today, Audrey - you ever consider becoming a model?"
    if audrey.is_visibly_pregnant:
        show audrey happy
        audrey.say "I wouldn't mind modelling some maternity wear for you."
        audrey.say "The modern stuff is pretty nice, especially the lingerie..."
    else:
        show audrey joke
        $ result = randint(1, 2)
        if result == 1:
            audrey.say "Ew, no - those girls are so skinny it's freaky."
        else:
            audrey.say "No, I'm more of a purse kind of girl."
    $ audrey.love += 1
    hide audrey
    return

label audrey_talk_books_male:
    show audrey
    mike.say "Read any good books lately, Audrey?"
    show audrey annoyed
    if audrey.is_visibly_pregnant:
        audrey.say "Have you read that Fifty Shades book?"
        audrey.say "Is there anything in there about kinky sex when you're pregnant?"
    else:
        audrey.say "Yeah, like I'm really going to go out of my way to do something that boring!"
    $ audrey.love -= 1
    hide audrey
    return

label audrey_talk_people_male:
    mike.say "What are you up to this weekend, Audrey - catching up with your girlfriends?"
    show audrey
    if audrey.is_visibly_pregnant:
        audrey.say "I was supposed to be going to one of those pregnant mother's groups."
        audrey.say "But after I asked the other mothers-to-be how good of a fuck the guy that got them pregnant was..."
        audrey.say "I get the impression I won't be welcome back there any time soon."
    else:
        audrey.say "I don't really have a lot of female friends...girls kind of avoid me."
        audrey.say "Especially if they've got a boyfriend..."
    hide audrey
    return

label audrey_talk_computers_male:
    show audrey
    mike.say "Know much about computers, Audrey?"
    show audrey annoyed
    audrey.say "Nah, nope, nada - not interested."
    $ audrey.love -= 1
    hide audrey
    return

label audrey_talk_music_male:
    show audrey
    mike.say "What's your thing when it comes to music, Audrey?"
    audrey.say "I'm quite eclectic - I like a little bit of this, little bit of that."
    hide audrey
    return

label audrey_talk_birthday_male:
    show audrey
    mike.say "Happy birthday, Audrey - hope you have a good one."
    show audrey happy
    audrey.say "Thank you, - you're the only one in the office that remembered."
    $ audrey.love += 3
    hide audrey
    return

init python:
    SpecificTalkSubject(**{
    "name": "audrey_talk_investigation",
    "display_name": "About the investigation",
    "label": "audrey_talk_investigation",
    "duration": 0,
    "icon": "button_investigate",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsFlag("underinvestigation"),
            MaxFlag("workinvestigation", 99)
            ),
        PersonTarget(audrey,
            IsActive(),
            ),
        ],
    "do_once": True,
    })

label audrey_talk_investigation:
    show audrey
    mike.say "Audrey, do you know anything about this investigation?"
    show audrey sad
    audrey.say "I'm sorry, [hero.name]. Everyone is talking about it but nobody knows anything about it."
    audrey.say "Just that everyone says you stole a lot of money."
    mike.say "Steal the money? No! I'd never do anything like that."
    show audrey surprised
    audrey.say "Then what happened?"
    if 'cassidy_hold_meeting' in DONE:
        mike.say "Someone set me up, and I think the CEO's daughter and someone in accounting is involved."
        if game.flags.toldjeff:
            mike.say "There's a guy over there named Jeff, I think he helped change the numbers."
        mike.say "Someone set me up. I don't know who, but whoever it is can make changes in our accounting systems."
    show audrey normal
    audrey.say "I wish I could help!"
    mike.say "Maybe you can. I bet there are people in accounting who know what's going on. Maybe you could be charming and dig up some information?"
    audrey.say "Sure, [hero.name], I'll try."
    mike.say "Thanks, Audrey! I owe you!"
    $ audrey.set_counter("investigationcallback")
    hide audrey
    return

label audrey_investigation_callback:
    play sound cell_vibrate loop
    "My phone buzzes. It's Audrey. She said she'd get in touch, maybe she's got some good news?"
    stop sound
    $ result = renpy.call_screen("smartphone_choice", "Audrey")
    if not result:
        $ hero.cancel_event()
        $ audrey.love -= 5
        return
    mike.say "Audrey!"
    audrey.say "Hey, [hero.name]. I did some asking around, like you asked. But I got yelled at and they told me if I don't stay out of it I could be fired too."
    mike.say "Oh no! I'm so sorry, Audrey. I didn't mean for you to get in trouble."
    audrey.say "It's okay, [hero.name]. I just wish I could help, but...I need this job."
    mike.say "Okay. Thanks for trying!"
    audrey.say "Good luck!"
    return

init:
    define nickname_chief = ["Chief", "chief"]
    define nickname_dick = ["Dick", "dick"]

label command_nickname_audrey:
    menu:

        "Call me Chief" if active_girl.flags.mikeNickname not in nickname_chief and hero.flags.office_boss == "mike":
            $ active_girl.flags.mikeNickname = "Chief"
        "Stop calling me Chief" if active_girl.flags.mikeNickname in nickname_chief:
            $ active_girl.flags.mikeNickname = None


        "Call me Dick" if active_girl.flags.mikeNickname not in nickname_dick and active_girl.sub > 70:
            $ active_girl.flags.mikeNickname = "Dick"
        "Stop calling me Dick" if active_girl.flags.mikeNickname in nickname_dick:
            $ active_girl.flags.mikeNickname = None
        "Cancel":


            jump command_girl

label submissive_interact_audrey_male:
    mike.say "Audrey..."
    mike.say "I've been thinking..."
    show audrey joke
    audrey.say "Oh-oh..."
    audrey.say "That's never a good sign!"
    show audrey normal
    mike.say "Hey - I'm being serious here!"
    mike.say "I wondered if you'd say how much you like to be played with?"
    mike.say "Like whenever you see me, you'd beg me to play with you?"
    if audrey.sub >= 70 or audrey.is_sex_slave:
        show audrey flirt
        audrey.say "Okay, okay..."
        audrey.say "Joking aside, that does sound kind of hot."
        audrey.say "Fine, I'll do it!"
        $ audrey.flags.submissive_interact = True
    else:
        show audrey whining
        audrey.say "You should go have your brain examined, [hero.name]."
        audrey.say "Because you'd have to me mental to think I'd do a thing like that!"
        show audrey sadsmile
        mike.say "Ah, maybe you're right, Audrey..."
        $ audrey.love -= 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
