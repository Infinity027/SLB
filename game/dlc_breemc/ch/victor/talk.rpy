label victor_talk_love_female:
    victor.say "It's hard when you do what I do, [hero.name]..."
    victor.say "You're exposed to so much fear and hatred, you know?"
    victor.say "It makes you even more desperate to find love and cling onto it."
    menu:
        "Compliment him":

            if hero.morality >= 25:
                bree.say "That's so beautiful, Victor - you're like a knight in a romantic fantasy!"
            elif hero.morality <= -25:
                bree.say "I love it when you talk like that, Victor - it really gets my blood pumping!"
            else:
                bree.say "I don't know how you do it, Victor - to still be able to love after all that suffering."
            $ victor.love += 2
        "Tease him":

            if hero.morality >= 25:
                bree.say "Eww...what you do is SO scary and noisy, Victor - it's a total turn-off!"
            elif hero.morality <= -25:
                bree.say "Ah, come on, Victor - I know that you get hard doing what you do for a living!"
            else:
                bree.say "Yeah, unless you accidentally shoot the person you love, along with everyone else!"
            $ victor.love -= 2
        "Reassure him":

            if hero.morality >= 25:
                bree.say "Oh, Victor - I'm so lucky to have someone like you to protect me!"
            elif hero.morality <= -25:
                bree.say "Keep talking like that, Victor, and you're going to make me melt!"
            else:
                bree.say "You're so romantic, Victor - and you make me feel so safe too!"
            $ victor.sub -= 1
    return

label victor_talk_sex_female:
    victor.say "Ah, I...I've got to say, [hero.name]..."
    victor.say "After my wife passed, I kind of stopped doing anything...intimate, you know?"
    victor.say "So I gotta say that I'm a little worried about going there again...with you!"
    menu:
        "Show compassion":

            if hero.morality >= 25:
                bree.say "Don't worry about a thing, Victor - we can take it one step at a time."
            elif hero.morality <= -25:
                bree.say "Don't you worry about a thing, Victor - I can handle you, no problem!"
            else:
                bree.say "I get it, Victor - we can go as slow, or as fast as you need to."
            $ victor.love += 2
        "Be impatient":

            if hero.morality >= 25:
                bree.say "Oh...I see - I thought you were way more masterful than that!"
            elif hero.morality <= -25:
                bree.say "Oh cut it with the sob-story, Victor - a girl's got needs!"
            else:
                bree.say "Don't take too long about it, Victor - I can't wait forever!"
            $ victor.love -= 2
        "'I'll show you'":

            if hero.morality >= 25:
                bree.say "Don't worry, Victor - I'll take good care of you."
            elif hero.morality <= -25:
                bree.say "Just leave it to me, Victor - you won't regret it!"
            else:
                bree.say "It's okay, Victor - I'll show you the way."
            $ victor.sub += 1
    return

label victor_talk_politics_female:
    victor.say "I don't do politics, [hero.name] - never have, never will."
    victor.say "In my time, I've taken out men on both sides of the spectrum."
    victor.say "Because they were so corrupt that someone wanted them gone!"
    menu:
        "Agree with him":

            if hero.morality >= 25:
                bree.say "I know what you mean, Victor - all politicians seem the same to me."
            elif hero.morality <= -25:
                bree.say "Power, money and sex - that's what it's all really about."
            else:
                bree.say "Left, right or centre, they're all just out for themselves."
            $ victor.love += 2
        "Teach him":

            if hero.morality >= 25:
                bree.say "That's probably because you've never been educated on it, Victor - let me enlighten you."
            elif hero.morality <= -25:
                bree.say "Oh, Victor, you're so naive - let me teach you a little about the real world!"
            else:
                bree.say "Of course they sound the same, Victor - because you need to be better informed!"
            $ victor.sub += 1
        "Show admiration":

            if hero.morality >= 25:
                bree.say "Ah...I wish I could see things as clearly as you do, Victor!"
            elif hero.morality <= -25:
                bree.say "Oh, Victor, there's so much I want you to educate me on!"
            else:
                bree.say "I guess you do have a unique perspective - wanna tell me all about it?"
            $ victor.sub -= 1
    return

label victor_talk_food_female:
    victor.say "I know there's so much exotic cuisine around right now."
    victor.say "But I kinda like home-made stuff, you know?"
    victor.say "Like real, basic comfort foods, yeah?"
    menu:
        "'That's boring !'":

            if hero.morality >= 25:
                bree.say "Eww...that sounds so boring and stodgy!"
            elif hero.morality <= -25:
                bree.say "BORING...variety is the spice of life!"
            else:
                bree.say "Geez, Victor...that's pretty disappointing to hear!"
            $ victor.love += 2
        "'I'll show you'":

            if hero.morality >= 25:
                bree.say "Oh, that's just because you've been sheltered, Victor - but don't worry, I'll help you expand your palette."
            elif hero.morality <= -25:
                bree.say "Oh boy, Victor - open wide, because am I going to enjoy expanding your horizons!"
            else:
                bree.say "Nah, you're just stuck in your ways - we'll soon fix that."
            $ victor.sub += 1
        "'I'd love to taste them'":

            if hero.morality >= 25:
                bree.say "That sounds wonderful, Victor - will you share them with me?"
            elif hero.morality <= -25:
                bree.say "You know me, Victor - I'll let you put anything you want in my mouth!"
            else:
                bree.say "That sounds interesting, Victor - I'd love to try them."
            $ victor.sub -= 1
    $ victor.love += 2
    return

label victor_talk_travels_female:
    bree.say "Doing what you do, Victor, you must have seen a lot of the world?"
    victor.say "I've been to a lot of different places, if that's what you mean."
    victor.say "But it's not the same when you're there to carry out a hit, [hero.name]!"
    menu:
        "Be positive":

            if hero.morality >= 25:
                bree.say "Oh, Victor, that sounds so terrible - we'll go back there together, and put it right!"
            elif hero.morality <= -25:
                bree.say "Oh baby, if you go back with me, I guarantee it'll be different!"
            else:
                bree.say "No time like the present to change that, Victor - let's go there together, yeah?"
            $ victor.love += 2
        "Show disgust":

            if hero.morality >= 25:
                bree.say "Eww...the idea of shooting people really does spoil it for me!"
            elif hero.morality <= -25:
                bree.say "Yeah, I can see how that's be a total downer!"
            else:
                bree.say "Everything being spattered with blood and guts would be a turn-off!"
            $ victor.love -= 2
        "Support him":

            if hero.morality >= 25:
                bree.say "What you need is someone to take you back there, Victor - someone to hold your hand."
            elif hero.morality <= -25:
                bree.say "You just worry about getting freaky in the bedroom, Victor - I'll handle being normal for both of us!"
            else:
                bree.say "Don't worry, Victor - I'll show you how to behave like a normal person!"
            $ victor.sub += 1
    return

label victor_talk_tv_female:
    bree.say "You watch any decent shows on TV recently, Victor?"
    bree.say "I'm looking for something new to binge."
    victor.say "Ah, I don't watch much TV, [hero.name]..."
    victor.say "All those apps and streaming services - they confuse the hell out of me!"
    menu:
        "Be positive":

            if hero.morality >= 25:
                bree.say "Don't fret about it, Victor - I'll pick something for us to watch together."
            elif hero.morality <= -25:
                bree.say "Don't worry about it, Victor - I'll keep you distracted while we're on the sofa together!"
            else:
                bree.say "It can be a bit confusing, can't it?"
            $ victor.love += 2
        "Make fun of him":

            if hero.morality >= 25:
                bree.say "Aww...the big nasty hitman can't word the TV - that is so cute!"
            elif hero.morality <= -25:
                bree.say "If you can't turn on the TV, then what chance have you got of doing the same to me?!?"
            else:
                bree.say "Geez, Victor, you're a hitman, not a damn caveman!"
            $ victor.love -= 2
        "Agree with him":

            if hero.morality >= 25:
                bree.say "Maybe I watch too much TV anyway - you think so, Victor?"
            elif hero.morality <= -25:
                bree.say "Ah, who wants to watch TV when we can have more fun with just the two of us?"
            else:
                bree.say "We could try reading instead - if you can recommend a decent book?"
            $ victor.sub -= 1
    return

label victor_talk_sports_female:
    bree.say "You're a tough, athletic kind of guy, Victor - bet you're totally into sports, right?"
    victor.say "Ah, not really, [hero.name]..."
    victor.say "I was always too much of a loner, at least for team sports."
    menu:
        "Agree with him":

            if hero.morality >= 25:
                bree.say "Me neither - it is so refreshing to hear a guy say that!"
            elif hero.morality <= -25:
                bree.say "So, you prefer it one-on-one, right?"
            else:
                bree.say "Huh...it's kind of nice to know you're different, Victor."
            $ victor.love += 2
        "Tease him":

            if hero.morality >= 25:
                bree.say "Ooh...remind me not to introduce you to my dad - he's a total sports-freak!"
            elif hero.morality <= -25:
                bree.say "I get it, Victor - you're scared of performing in public!"
            else:
                bree.say "So what, Victor - you always found big groups of guys intimidating?"
            $ victor.sub += 1
        "Joke":

            if hero.morality >= 25:
                bree.say "I hope you can still loner with me around, Victor?"
            elif hero.morality <= -25:
                bree.say "That's fine, Victor - most of the stuff I want to do with you needs us to be alone!"
            else:
                bree.say "I'm cool with the loner thing - so long as you make an exception for me!"
            $ victor.sub -= 1
    return

label victor_talk_fashion_female:
    bree.say "I was wondering, Victor - do you, like, own any clothes that aren't...well, black?"
    "Victor looks down at what he's wearing, as if he's never seen it before in his life."
    if victor.sub >= 50:
        victor.say "Ah...I never really noticed before, [hero.name]!"
    elif victor.sub <= -50:
        victor.say "I can't change the way I dress, [hero.name] - it's part of my identity."
    else:
        victor.say "Ah, it's kind of a hitman thing, [hero.name] - like a uniform, I guess."
    menu:
        "Complain":

            if hero.morality >= 25:
                bree.say "Yeah, it's just that it's...you know, kind of boring!"
            elif hero.morality <= -25:
                bree.say "Hard for a girl to get excited on a constant diet of blah black!"
            else:
                bree.say "You're not on a hit all the time, Victor - so why not mix it up a little?"
            $ victor.love -= 2
        "Take the lead":

            if hero.morality >= 25:
                bree.say "You should let me pick you out some clothes when you're not on a job, Victor."
            elif hero.morality <= -25:
                bree.say "Yeah, you're not getting anything out of me in the bedroom if you keep painting everything black!"
            else:
                bree.say "Man, I'm gonna need to start styling you when you're off work!"
            $ victor.sub += 1
        "Be positive":

            if hero.morality >= 25:
                bree.say "Well, I suppose that it is a strong look - very manly."
            elif hero.morality <= -25:
                bree.say "I guess there's a thrill to a classic!"
            else:
                bree.say "I have to admit it's iconic, Victor - very memorable."
            $ victor.sub -= 1
    return

label victor_talk_books_female:
    victor.say "Ah, you're always reading a book, [hero.name]."
    victor.say "I never get the chance to read anything for the pleasure of it."
    victor.say "Mostly I read manuals on martial arts and gun maintenance!"
    menu:
        "Compliment him":

            if hero.morality >= 25:
                bree.say "That's nothing to be ashamed of, Victor - you're still expanding your mind."
            elif hero.morality <= -25:
                bree.say "I bet you know all sorts of things about the human body!"
            else:
                bree.say "That's interesting, Victor - you must be a mine of information."
            $ victor.love += 2
        "Tease him":

            if hero.morality >= 25:
                bree.say "You really should try to read some fiction, Victor - it'd expand your mind."
            elif hero.morality <= -25:
                bree.say "Urgh...you must have, like, zero imagination!"
            else:
                bree.say "Sounds like you're just absorbing facts for their own sake."
            $ victor.love -= 2
        "Give help":

            if hero.morality >= 25:
                bree.say "Sounds like you need someone to recommend a good book to begin with!"
            elif hero.morality <= -25:
                bree.say "Don't worry, Victor - I'm used to showing you how it's done!"
            else:
                bree.say "It's okay to admit you're clueless, Victor - I can recommend a book or two."
            $ victor.sub += 1
    return

label victor_talk_people_female:
    bree.say "You must meet a lot of people in your line of work, Victor."
    victor.say "Oh yeah, [hero.name] - I've met literally hundreds of them."
    victor.say "But the problem is that I have to whack most people I meet."
    victor.say "And it's usually the interesting ones too!"
    menu:
        "Show compassion":

            if hero.morality >= 25:
                bree.say "Oh no, Victor - that must be so hard for you to process!"
            elif hero.morality <= -25:
                bree.say "And yet you're still alive and kicking - that's kind of hot!"
            else:
                bree.say "Ouch - that's pretty tough, and it must make you tough in turn."
            $ victor.love += 2
        "Tease him":

            if hero.morality >= 25:
                bree.say "Oh, I see - that must be why you can be so cold."
            elif hero.morality <= -25:
                bree.say "Urgh - I hate to think what that's doing to your kinks and quirks!"
            else:
                bree.say "Geez - that's got to be doing you some serious damage!"
            $ victor.love -= 2
        "Show admiration":

            if hero.morality >= 25:
                bree.say "Oh, Victor - you can be so strong and manly!"
            elif hero.morality <= -25:
                bree.say "You are just SO mysterious - and it's a total turn-on!"
            else:
                bree.say "Man, I just don't know how you keep going!"
            $ victor.sub -= 1
    return

label victor_talk_computers_female:
    victor.say "I know that everyone's into their computers and totally tech-savvy."
    victor.say "But I was taught to trust in more simple things, [hero.name]."
    victor.say "Tried and tested things that are totally reliable."
    menu:
        "Compliment him":

            if hero.morality >= 25:
                bree.say "I get that, Victor - you have a poetic simplicity about you."
            elif hero.morality <= -25:
                bree.say "Simple and straight to the point - that's what I like about you!"
            else:
                bree.say "Yeah, Victor, I get that - you have a real zen quality."
            $ victor.love += 2
        "Propose some help":

            if hero.morality >= 25:
                bree.say "Are you trying to say that you want me to teach you how to send an email?"
            elif hero.morality <= -25:
                bree.say "I get it, Victor - you want me to take you by the hand and show you the way!"
            else:
                bree.say "I can clue you in on stuff, Victor - no need to be a technophobe!"
            $ victor.sub += 1
        "Ask for help":

            if hero.morality >= 25:
                bree.say "I want to be like that too, Victor - will you teach me?"
            elif hero.morality <= -25:
                bree.say "Teach me, Victor - take me back to basics!"
            else:
                bree.say "My life could do with a techno-detox!"
            $ victor.sub -= 1
    return

label victor_talk_music_female:
    victor.say "I really don't get modern music, [hero.name]."
    victor.say "I prefer classical stuff, you know?"
    victor.say "It helps to focus my mind."
    menu:
        "Make fun of him":

            if hero.morality >= 25:
                bree.say "You mean it makes it easier to shoot people?!?"
            elif hero.morality <= -25:
                bree.say "I've seen what you do for a living, Victor - and it doesn't sell your taste in music!"
            else:
                bree.say "Geez, Victor - it helps you wipe out a room full of people?"
            $ victor.love -= 2
        "Take the lead":

            if hero.morality >= 25:
                bree.say "Don't be silly, Victor - you just need to listen to a more varied playlist!"
            elif hero.morality <= -25:
                bree.say "Oh, we are SO making love to my choice of music now - that'll soon change your mind!"
            else:
                bree.say "Okay, challenge accepted - you're obviously telling me that because you want help!"
            $ victor.sub += 1
        "Show interest":

            if hero.morality >= 25:
                bree.say "I'd love for you to educate me when it comes to classical music!"
            elif hero.morality <= -25:
                bree.say "Maybe we could listen to classical stuff while we're getting it on?"
            else:
                bree.say "I never got classical stuff before - but maybe if you explained it to me I would?"
            $ victor.sub -= 1
    return

label victor_talk_birthday_female:
    if hero.morality >= 25:
        bree.say "Hey, Victor - happy birthday!"
    elif hero.morality <= -25:
        bree.say "Happy birthday, big boy!"
    else:
        bree.say "Happy birthday, Victor!"
    if victor.sub >= 50:
        victor.say "Oh...thank you so much, [hero.name]!"
    elif victor.sub <= -50:
        victor.say "Well done for remembering, [hero.name]!"
    else:
        victor.say "Oh, thanks, [hero.name]!"
    $ victor.love += 5
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
