init python:
    SpecificTalkSubject(**{
    "name": "kylie_talk_stalking",
    "display_name": "About stalking",
    "label": "kylie_talk_stalking_male",
    "duration": 0,
    "icon": "button_kylie",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(kylie,
            IsActive(),
            IsFlag("policestation")
            ),
        ],
    "do_once": True,
    })

label kylie_talk_stalking_male:
    show kylie normal
    "The moment that I lay eyes on Kylie, it's all that I can do to keep myself from storming straight over and confronting her."
    "But somehow I manage to control my anger long enough to close the distance between us looking like I suspect nothing."
    "All the time I can feel my teeth grinding together behind sealed lips and my nails digging into my palms."
    "For her own part, Kylie seems to be her normal, saccharine self."
    show kylie smile
    "She smiles sweetly as I approach, giving me what would otherwise look like a friendly wave of greeting."
    kylie.say "[hero.name]."
    show kylie happy
    kylie.say "It's SO great to see you!"
    mike.say "Save that crap for some other sap, Kylie."
    mike.say "Because it's not going to wash with me anymore!"
    show kylie surprised
    "At this, Kylie reels backwards a little."
    "Clearly my unexpected outburst has caught her off-guard."
    "But she's not so green as to drop the pretense of innocence just yet."
    kylie.say "I...I don't understand, [hero.name]."
    show kylie sad
    kylie.say "Are you accusing me of something?"
    kylie.say "Because I would never..."
    "Not interested in hearing whatever bullshit she cooks up, I shake my head."
    "And then I hold up my mobile phone, hitting play on the incriminating footage."
    show kylie surprised
    "I see Kylie's eyes go wide a moment later, and I know that she knows what it is."
    "And she knows that I know that she knows too!"
    "I wait in silence, intrigued to hear what's going to come out of her mouth next."
    "From the extended amount of time Kylie takes to respond, I can guess that it'll be good too..."
    show kylie sad
    kylie.say "Oh, [hero.name]..."
    kylie.say "I'm SO SO sorry!"
    kylie.say "You must HATE me!"
    "The speed with which Kylie collapses into a flood of tears is simply shocking."
    "She literally becomes a weeping mess in the blink of an eye."
    "Maybe this incredible speed should have set off alarm bells in my mind."
    "But as it is, I'm simply overwhelmed by her sudden show of emotion."
    mike.say "What?!?"
    mike.say "Yes...I mean no..."
    mike.say "I mean I just want to know what's going on, Kylie!"
    "I glance around as I say this, beginning to worry what anyone watching us will think."
    "I guess my judgment is pretty clouded by the fear of being accused of something as I accuse Kylie of something!"
    show kylie annoyed
    kylie.say "I didn't mean to, [hero.name] - you have to believe me!"
    show kylie sad
    kylie.say "I was just passing one night, that's all."
    kylie.say "I happened to walk past your place, and I thought I'd see if you were awake."
    mike.say "At three in the morning?!?"
    show kylie annoyed
    kylie.say "I know how it sounds, [hero.name], I really do!"
    kylie.say "At first I was going to knock or ring the bell."
    kylie.say "But then I got scared you'd be mad at me waking you."
    show kylie sad
    kylie.say "So...so I just stood there, hoping you might come to the door anyway."
    kylie.say "And then I started taking a walk almost every night..."
    "Kylie looks down at her feet, wringing her hands as the tears run down her cheeks."
    kylie.say "I'll stop, [hero.name]."
    kylie.say "I promise you I will!"
    "As much as I know that I should tell her that a promise is not enough, I hesitate before saying as much."
    "Sure, the explanation Kylie just gave me sounds crazier than a box of frogs."
    "But then she's never been the most average or ordinary of girls either."
    "Maybe she just let herself get carried away, and it got to where she couldn't stop herself?"
    "At least she's acknowledged that what she did was wrong."
    "That has to count for something, right?"
    mike.say "Urgh..."
    mike.say "Okay, don't make me regret this, Kylie."
    mike.say "But if you really mean that, then I suppose we can put it behind us."
    show kylie smile
    "Kylie all but throws herself at me then, smiling and batting her eyelids."
    show kylie happy
    kylie.say "Oh, thank you, [hero.name]!"
    kylie.say "I'll be good, you'll see."
    kylie.say "I'll make sure you know just how much I love you."
    kylie.say "I promise you..."
    show kylie smile
    "All I can do is nod and smile in return as she presses herself against me."
    "God help me - this girl scares me and turns me on in equal measures."
    "I just hope that I've done the right thing..."
    $ kylie.love += 5
    $ kylie.flags.policestation = False
    $ kylie.flags.nostalking = True
    return

label kylie_talk_love_male:
    show kylie
    kylie.say "Love is the deep feeling of needing someone else more than air."
    $ kylie.love += 1
    hide kylie
    return

label kylie_talk_sex_male:
    show kylie
    kylie.say "Sex..."
    kylie.say "Can we do it?"
    show kylie blush
    kylie.say "Do you want to do it?"
    kylie.say "You can fuck me here and now if you want..."
    $ kylie.love += 1
    hide kylie
    return

label kylie_talk_politics_male:
    show kylie annoyed
    kylie.say "I am not that interested in politics."
    $ kylie.love -= 1
    hide kylie
    return

label kylie_talk_food_male:
    show kylie smile
    kylie.say "I like whatever you like."
    $ kylie.love += 1
    hide kylie
    return

label kylie_talk_travels_male:
    show kylie smile
    kylie.say "The only place I wanna go is where you are."
    $ kylie.love += 1
    hide kylie
    return

label kylie_talk_tv_male:
    show kylie annoyed
    kylie.say "I don't really care about TV..."
    $ kylie.love -= 1
    hide kylie
    return

label kylie_talk_sports_male:
    show kylie
    $ result = randint(1, 2)
    if result == 1:
        show kylie smile
        kylie.say "It's important to take care of your health."
    else:
        show kylie annoyed
        kylie.say "Do you want me to exercise more?"
        show kylie blush
        kylie.say "Do you like sporty chicks?"
    $ kylie.love += 1
    hide kylie
    return

label kylie_talk_fashion_male:
    show kylie blush
    $ result = randint(1, 2)
    if result == 1:
        kylie.say "Should I dress slutty?"
    else:
        kylie.say "Should I dress less slutty?"
    $ kylie.love += 1
    hide kylie
    return

label kylie_talk_books_male:
    show kylie annoyed
    kylie.say "Boring."
    $ kylie.love -= 1
    hide kylie
    return

label kylie_talk_people_male:
    show kylie
    kylie.say "You are the only one I need."
    kylie.say "And I am the only girl you'll need."
    hide kylie
    return

label kylie_talk_computers_male:
    show kylie annoyed
    kylie.say "Not interested."
    $ kylie.love -= 1
    hide kylie
    return

label kylie_talk_music_male:
    show kylie
    kylie.say "A little bit of this, a little bit of that."
    hide kylie
    return

label kylie_talk_birthday_male:
    show kylie
    mike.say "Happy birthday Kylie."
    show kylie happy
    kylie.say "Thank you [hero.name]."
    $ kylie.love += 3
    hide kylie
    return

init:
    define nickname_my_one_and_only = ["My One and Only", "my one and only"]
    define nickname_my_heart = ["My Heart", "my heart"]
    define nickname_my_ball_and_chain = ["My ball and chain", "my ball and chain"]

label command_nickname_kylie:
    menu:

        "Call me My One and Only" if active_girl.flags.mikeNickname not in nickname_my_one_and_only:
            $ active_girl.flags.mikeNickname = "My One and Only"
        "Stop calling me My One and Only" if active_girl.flags.mikeNickname in nickname_my_one_and_only:
            $ active_girl.flags.mikeNickname = None


        "Call me My Heart" if active_girl.flags.mikeNickname not in nickname_my_heart:
            $ active_girl.flags.mikeNickname = "My Heart"
        "Stop calling me My Heart" if active_girl.flags.mikeNickname in nickname_my_heart:
            $ active_girl.flags.mikeNickname = None


        "Call me My ball and chain" if active_girl.flags.mikeNickname not in nickname_my_ball_and_chain:
            $ active_girl.flags.mikeNickname = "My ball and chain"
        "Stop calling me My ball and chain" if active_girl.flags.mikeNickname in nickname_my_ball_and_chain:
            $ active_girl.flags.mikeNickname = None
        "Cancel":


            jump command_girl

label submissive_interact_kylie_male:
    mike.say "Hey, Kylie..."
    mike.say "You know how you always say you're crazy about me?"
    show kylie surprised
    kylie.say "What?!?"
    kylie.say "Who says I'm crazy?!"
    show kylie talkative
    kylie.say "Oh...right, I see what you mean."
    show kylie normal
    mike.say "Well...maybe you could tell me that when you say hi?"
    if kylie.sub >= 70 or kylie.is_sex_slave:
        show kylie happy
        kylie.say "Of course, [hero.name] - that sounds like a great idea."
        show kylie talkative
        kylie.say "Anything that makes people know that I'm yours and you're mine."
        show kylie shout
        kylie.say "And warns them what'll happen if they come between us too!"
        $ kylie.flags.submissive_interact = True
    else:
        show kylie whining
        kylie.say "Oh no, [hero.name] - that would make me sound all needy and pathetic."
        kylie.say "I can't have people thinking that I'm some kind of crazy girl!"
        show kylie sad
        mike.say "Of course not, Kylie - who'd believe a thing like that?"
        $ kylie.love -= 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
