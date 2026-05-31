label ayesha_talk_love_male:
    show ayesha
    mike.say "Ayesha, do you think true love is a real thing?"
    mike.say "Or is it just something fictional, you know - made up?"
    show ayesha sad
    "Ayesha glances away for a moment, a sad look in her eyes."
    ayesha.say "I used to think that it was."
    ayesha.say "But life kinda beats that way of thinking out of you..."
    $ ayesha.love -= 1
    hide ayesha
    return

label ayesha_talk_sex_male:
    show ayesha
    mike.say "You keep yourself in such great shape, Ayesha."
    mike.say "Do you even have time to think about stuff like, I don't know...sex?"
    show ayesha annoyed
    "Ayesha looks at me as though what I just said struck a nerve."
    ayesha.say "What?!?"
    ayesha.say "Just because I can bench press more than most guys, it doesn't mean I'm not a real woman!"
    $ ayesha.love -= 1
    $ ayesha.sub += 1
    hide ayesha
    return

label ayesha_talk_politics_male:
    show ayesha
    mike.say "It seems like there's a new thing to be outraged about in the news every day."
    mike.say "Do you keep up on all of that stuff, Ayesha?"
    "Ayesha rolls her eyes and shakes her head."
    ayesha.say "I don't have time for most of it."
    ayesha.say "And I like to listen to music while I work out, not the news."
    hide ayesha
    return

label ayesha_talk_food_male:
    show ayesha
    mike.say "Wow, you sure do have a healthy appetite, Ayesha!"
    show ayesha annoyed
    "Ayesha's eyes go wide and she instantly looks embarrassed."
    ayesha.say "Wha...what are you trying to say?!?"
    ayesha.say "I...I need to eat a lot of protein, that's all!"
    ayesha.say "I don't eat like a cow because I want to!"
    $ ayesha.love -= 1
    hide ayesha
    return

label ayesha_talk_travels_male:
    show ayesha
    mike.say "I'd like to travel the world one day, Ayesha."
    mike.say "How about you?"
    "Ayesha's eyes become wide and almost starry."
    ayesha.say "I'd be too lonely to travel all that way."
    ayesha.say "Unless I had someone to keep me company..."
    hide ayesha
    return

label ayesha_talk_tv_male:
    show ayesha
    mike.say "You seen anything good on TV recently, Ayesha?"
    show ayesha annoyed
    "Ayesha frowns and shakes her head."
    ayesha.say "Can't say that I have."
    show ayesha angry
    ayesha.say "Most stuff I see on TV is just vacant shit anyway."
    $ ayesha.love -= 1
    hide ayesha
    return

label ayesha_talk_sports_male:
    show ayesha
    mike.say "You're always sparring at the gym, Ayesha."
    mike.say "Apart from wrestling, are you into any REAL sports?"
    show ayesha annoyed
    "Ayesha fixes me with a hard stare, crossing her arms over her chest."
    show ayesha angry
    ayesha.say "I'm going to pretend you didn't say that, [hero.name]."
    ayesha.say "Most wrestlers are better athletes than those creampuffs in other sports!"
    $ ayesha.love -= 5
    hide ayesha
    return

label ayesha_talk_fashion_male:
    show ayesha
    mike.say "I know some of the shorter girls I know have a hard time buying nice clothes."
    mike.say "So, is it the same story for you too, Ayesha?"
    show ayesha blush
    "Ayesha looks instantly embarrassed and self-conscious."
    "Her head darts this way and that, as if she's convinced people are staring at her."
    ayesha.say "Wha...what are you trying to say, [hero.name]?"
    ayesha.say "Of course not!"
    ayesha.say "It's not like I ever had to buy men's clothes to get something in my size..."
    $ ayesha.sub += 1
    hide ayesha
    return

label ayesha_talk_books_male:
    show ayesha
    mike.say "Do you have much time for reading, Ayesha?"
    mike.say "You seem to spend so much time in the gym!"
    show ayesha annoyed
    "Ayesha narrows her eyes at me, shaking her head a little."
    ayesha.say "I can actually read, you know."
    ayesha.say "And you might be surprised to know that I like books without pictures too!"
    $ ayesha.love -= 1
    hide ayesha
    return

label ayesha_talk_people_male:
    show ayesha
    mike.say "You're in such great shape, Ayesha."
    mike.say "It must make meeting people pretty easy, huh?"
    "Ayesha smiles, but the look in her eyes is oddly sad."
    ayesha.say "You'd think that, wouldn't you?"
    ayesha.say "But the attention you get isn't always the kind you want..."
    $ ayesha.sub += 1
    hide ayesha
    return

label ayesha_talk_computers_male:
    show ayesha
    mike.say "I'm pretty into my gaming, you know?"
    mike.say "What about you, Ayesha?"
    "Ayesha frowns and shakes her head."
    ayesha.say "Ah, I played Fire Pro Wrestling a couple of times."
    ayesha.say "But I prefer the real thing!"
    hide ayesha
    return

label ayesha_talk_music_male:
    show ayesha
    mike.say "What's your choice in music, Ayesha?"
    mike.say "No, let me guess - something thumping so you can work out to it, right?"
    show ayesha annoyed
    "Ayesha shakes her head and gives me a rueful look."
    ayesha.say "You really think I'm that one-dimensional, [hero.name]?"
    show ayesha normal
    ayesha.say "Actually, I like a lot of different stuff."
    show ayesha happy
    ayesha.say "Even some classical music and the occasional bit of Opera too!"
    $ ayesha.love += 2
    hide ayesha
    return

label ayesha_talk_birthday_male:
    show ayesha
    mike.say "Happy birthday, Ayesha."
    mike.say "I've been aching to say that to you since you told me the date!"
    show ayesha blush
    ayesha.say "Oh...wow..."
    ayesha.say "I don't know what to say, [hero.name]!"
    ayesha.say "You just made me feel SO special..."
    $ ayesha.love += 5
    hide ayesha
    return

init:
    define nickname_little_man = ["Little man", "little man"]
    define nickname_boi = ["Boi", "boi"]
    define nickname_coach = ["Coach", "coach"]

label command_nickname_ayesha:
    menu:

        "Call me Little man" if active_girl.flags.mikeNickname not in nickname_little_man and active_girl.love >= 20:
            $ active_girl.flags.mikeNickname = "Little man"
        "Stop calling me Little man" if active_girl.flags.mikeNickname in nickname_little_man:
            $ active_girl.flags.mikeNickname = None


        "Call me Boi" if active_girl.flags.mikeNickname not in nickname_boi and active_girl.love >= 70:
            $ active_girl.flags.mikeNickname = "Boi"
        "Stop calling me Boi" if active_girl.flags.mikeNickname in nickname_boi:
            $ active_girl.flags.mikeNickname = None


        "Call me Coach" if active_girl.flags.mikeNickname not in nickname_coach and active_girl.flags.manager:
            $ active_girl.flags.mikeNickname = "Coach"
        "Stop calling me Coach" if active_girl.flags.mikeNickname in nickname_coach:
            $ active_girl.flags.mikeNickname = None
        "Cancel":


            jump command_girl


label submissive_interact_ayesha_male:
    mike.say "Ayesha..."
    mike.say "I wondered if you'd do something for me?"
    show ayesha talkative
    ayesha.say "That kind of depends what that something is!"
    show ayesha normal
    mike.say "Well, as we're like an item, I was thinking you could greet me a certain way."
    mike.say "Maybe even say that you're mine and you want to get it on with me?"
    if ayesha.sub >= 70 or ayesha.is_sex_slave:
        show ayesha blush
        ayesha.say "I guess that I could do that, [hero.name]."
        ayesha.say "I wouldn't be lying if I said that."
        ayesha.say "And if it'll make you happy, all the better!"
        $ ayesha.flags.submissive_interact = True
    else:
        show ayesha angry
        ayesha.say "We're in a relationship, [hero.name]."
        ayesha.say "But you don't own me!"
        show ayesha upset
        mike.say "Ah, I get what you're saying, Ayesha."
        mike.say "Let's just forget about it..."
        $ ayesha.love -= 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
