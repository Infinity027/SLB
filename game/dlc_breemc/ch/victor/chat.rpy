label victor_desire_0_female:
    if victor.sub >= 50:
        victor.say "It's so hard being a hitman, [hero.name]- nobody ever thinks about your feelings, you know?"
    elif victor.sub <= -50:
        victor.say "There's no down-time as a hitman, [hero.name]- it's like, constant stress and struggle."
    else:
        victor.say "Being a hitman is tough, [hero.name]- you're always struggling with your mental health."
    menu:
        "I can't imagine how hard that must be":
            if hero.morality >= 25:
                bree.say "Oh, Victor - you must really suffer!"
            elif hero.morality <= -25:
                bree.say "What you need is a way to release all of that stress, Victor!"
            else:
                bree.say "It's tough in normal jobs - so I can't imagine how bad you have it!"
            $ victor.love += 1
        "Aren't you just, like, a thug?":
            if hero.morality >= 25:
                bree.say "Huh...I thought you just shot people for a living?"
            elif hero.morality <= -25:
                bree.say "Oh please, Victor - you just shoot your load, right?"
            else:
                bree.say "Don't you just point the gun and squeeze the trigger?"
            $ victor.love += 1
        "You need to connect with your feminine side":
            if hero.morality >= 25:
                bree.say "I think you need to relax more, Victor - get in touch with your feelings."
            elif hero.morality <= -25:
                bree.say "You need someone to take control of your life, Victor - and that includes your sex life!"
            else:
                bree.say "Have you ever considered trying stuff like meditation or yoga?"
            $ victor.sub += 1
    return

label victor_desire_1_female:
    if victor.sub >= 50:
        victor.say "I like that you don't want to talk about the killing part of my job, [hero.name]- it's so hard sometimes!"
    elif victor.sub <= -50:
        victor.say "I like that we don't talk about my work much, [hero.name]- so I think we're going to keep it that way."
    else:
        victor.say "Thanks for not always wanting to hear about my job, [hero.name]- it really helps me stay grounded."
    menu:
        "You're more than your job":
            if hero.morality >= 25:
                bree.say "There's more to you than your job, Victor, much more!"
            elif hero.morality <= -25:
                bree.say "Oh, there's so many more fun things I want to hear about, Victor!"
            else:
                bree.say "You're not defined by your job, Victor, not at all."
            $ victor.love += 1
        "Yeah, about that...":
            if hero.morality >= 25:
                bree.say "That's only because it scares me, Victor - we have to confront it sooner or later."
            elif hero.morality <= -25:
                bree.say "Oh yeah, the old elephant in the room - it is kind of a passion killer!"
            else:
                bree.say "Yeah, about that - I've just been putting off having a serious talk about it."
            $ victor.sub += 1
        "Your job makes me feel safe":
            if hero.morality >= 25:
                bree.say "If I'm honest, Victor, what you do makes me feel safe and protected!"
            elif hero.morality <= -25:
                bree.say "I love what you do, Victor - knowing you can protect me is such a turn-on!"
            else:
                bree.say "I don't like to admit it, Victor - but what you do makes me feel safe."
            $ victor.sub -= 1

label victor_desire_2_female:
    if victor.sub >= 50:
        victor.say "Sometimes I want to give up what I do, [hero.name], and just be a normal guy."
    elif victor.sub <= -50:
        victor.say "I always wonder what my life would be like if I turned my back on what I do."
    else:
        victor.say "I often wonder what life would be like if I were just an average dude."
    menu:
        "I think you would still be you":
            if hero.morality >= 25:
                bree.say "Oh, you could never be just an average guy, Victor - you're special!"
            elif hero.morality <= -25:
                bree.say "You'd still remember all of the tricks that you learned, Victor - all the spiciness too!"
            else:
                bree.say "I think what makes you unique would endure, Victor, because it's a part of who you are."
            $ victor.love += 1
        "Maybe you need someone to help find the real you?":
            if hero.morality >= 25:
                bree.say "I'm here for you if you decide to do that, Victor - I'll help you find a new identity."
            elif hero.morality <= -25:
                bree.say "Just put yourself in my hands, Victor - I'll shape you into a new man!"
            else:
                bree.say "You sound like you need some help finding yourself, Victor - I'd be happy to give it to you."
            $ victor.sub += 1
        "I'm the one that should be learning from you!":
            if hero.morality >= 25:
                bree.say "With all of your experiences, Victor, I'm the one who should be learning from you!"
            elif hero.morality <= -25:
                bree.say "Oh come on, Victor - you could teach me something new every night!"
            else:
                bree.say "That's funny, Victor, because I always thought you'd be amazing, what with all the stuff you know!"
            $ victor.sub -= 1
    return

label victor_desire_3_female:
    if victor.sub >= 50:
        victor.say "Sometimes I want to quit what I do, [hero.name]- but I'm scared of the consequences."
    elif victor.sub <= -50:
        victor.say "I could turn my back on what I do, but I'd need to know it was for something worth the cost."
    else:
        victor.say "I keep thinking about walking away from what I do, but there's always a price to pay."
    menu:
        "I'm here for you whatever you choose":
            if hero.morality >= 25:
                bree.say "That sounds scary, Victor - but I'd do whatever I could to help."
            elif hero.morality <= -25:
                bree.say "Whatever you do, I'm here for you - in a very real, physical sense!"
            else:
                bree.say "I'm here for you if you need me, Victor - I want you to know that."
            $ victor.love += 1
        "Whatever, just keep me out of it":
            if hero.morality >= 25:
                bree.say "That world really scares me, Victor - just keep it away from me!"
            elif hero.morality <= -25:
                bree.say "Yeah, Victor, you make sure you leave all of that shit at the bedroom door!"
            else:
                bree.say "You do you, Victor - just keep that whole world separate from mine!"
            $ victor.sub += 1
        "You need to be integrated into the real world":
            if hero.morality >= 25:
                bree.say "When you do leave it all behind, I'm here to teach you how to be normal."
            elif hero.morality <= -25:
                bree.say "When that happens, I'll make sure the only craziness happens in the bedroom!"
            else:
                bree.say "If you choose to quit, Victor, I'll make life as normal for you as I can."
            $ victor.sub -= 1
    return

label victor_desire_4_female:
    if victor.sub >= 50:
        victor.say "I almost missed a shot today, [hero.name]- because I was thinking of you!"
    elif victor.sub <= -50:
        victor.say "Damn it, [hero.name]- my feelings for you are threatening to take away my edge!"
    else:
        victor.say "Work was tough today, [hero.name]- because you were on my mind the whole time!"
    menu:
        "I really mean that much to you?":
            if hero.morality >= 25:
                bree.say "Victor, are you serious - I really mean that much to you?!?"
            elif hero.morality <= -25:
                bree.say "Oh man, I want to know what you were picturing me doing to you!"
            else:
                bree.say "Wow, if I can get into a hitman's head, then this really is serious!"
            $ victor.love += 1
        "Anything to stop you from killing!":
            if hero.morality >= 25:
                bree.say "I'm glad that I made it harder for you to shoot someone!"
            elif hero.morality <= -25:
                bree.say "You know it's better to make love than war, Victor!"
            else:
                bree.say "Huh...maybe your conscience is trying to tell you something?"
            $ victor.sub += 1
        "Is there room for me in that head of yours?":
            if hero.morality >= 25:
                bree.say "Oh, Victor - I hope there's room for me and your work in there?"
            elif hero.morality <= -25:
                bree.say "Let your work keep the professional bit of your brain - I want to live in the pleasure centre!"
            else:
                bree.say "You can fit both things in there, right - me and your work?"
            $ victor.sub -= 1
    return

label victor_desire_5_female:
    if victor.sub >= 50:
        victor.say "[hero.name], I'm just gonna throw down my guns and come running to you!"
    elif victor.sub <= -50:
        victor.say "[hero.name], all I want to do is empty my clip and then be with you!"
    else:
        victor.say "[hero.name], the moment that I'm done with my current job, I'll be with you!"
    menu:
        "I'm ready and waiting for you!":
            if hero.morality >= 25:
                bree.say "Whenever you're ready, Victor - I'll be waiting for you!"
            elif hero.morality <= -25:
                bree.say "You can 'empty your clip into me' anytime, Victor!"
            else:
                bree.say "You know where to find me when you're done, Victor!"
        "You can have it on my terms":
            if hero.morality >= 25:
                bree.say "If you make sure to call ahead, I'll be ready for you."
            elif hero.morality <= -25:
                bree.say "You need to learn to be a bit more obedient, Victor!"
            else:
                bree.say "Not unless you give me ample warning!"
        "Take me, I'm yours!":
            if hero.morality >= 25:
                bree.say "I can't resist you, Victor - come and find me!"
            elif hero.morality <= -25:
                bree.say "Oh boy, you'd better be ready to back up all that big talk, mister!"
            else:
                bree.say "I'll be ready and waiting for you!"
    return

label victor_love_0_female:
    if victor.sub >= 50:
        victor.say "It's so weird, [hero.name], that you'd just happen to be there when I was doing a hit!"
    elif victor.sub <= -50:
        victor.say "You know, [hero.name], I sometimes think about how random us meeting actually was!"
    else:
        victor.say "You do realise how totally random us meeting each other was, right?"
    menu:
        "Maybe it was meant to be?":
            if hero.morality >= 25:
                bree.say "I totally get that, Victor - and I'm just glad that we did meet."
            elif hero.morality <= -25:
                bree.say "I always think fate has a way of serving up hot guys!"
            else:
                bree.say "Oh totally, Victor - but how lucky does that make us, right?"
        "It's a wonder you didn't shoot me!":
            if hero.morality >= 25:
                bree.say "To be honest, Victor, I was terrified you might shoot me!"
            elif hero.morality <= -25:
                bree.say "Yeah, I thought you were going to stick one in me - and not in the fun way either!"
            else:
                bree.say "Never mind the chances of us meeting - what about the chance of you shooting me when we did?!?"
        "Maybe I was meant to find you?":
            if hero.morality >= 25:
                bree.say "Hmm...maybe fate wanted you to have someone to guide you, Victor?"
            elif hero.morality <= -25:
                bree.say "Maybe the cosmos decided you weren't getting enough action, Victor?"
            else:
                bree.say "I think I was meant to find you, Victor, like, to show you the way."
    return

label victor_love_1_female:
    if victor.sub >= 50:
        victor.say "Ah, you've been hanging around with me a lot, [hero.name]- is there a reason why?"
    elif victor.sub <= -50:
        victor.say "Seems like you can't get enough of me lately, [hero.name]!"
    else:
        victor.say "We seem to be spending a lot of time together at the moment, [hero.name]!"
    menu:
        "Well, you are kind of exciting":
            if hero.morality >= 25:
                bree.say "What can I say, Victor - you're a pretty exciting guy!"
            elif hero.morality <= -25:
                bree.say "And I intend to spend a lot more with you too!"
            else:
                bree.say "What do you expect - you're an interesting guy!"
            $ victor.love += 1
        "The novelty will wear off eventually":
            if hero.morality >= 25:
                bree.say "That'll be the novelty, Victor - the thrill of the new!"
            elif hero.morality <= -25:
                bree.say "Yeah, tends to be that way until I get someone new into the sack!"
            else:
                bree.say "Nah, I always get kind of obsessive over new people - it'll pass."
            $ victor.sub += 1
        "You're just so darn interesting!":
            if hero.morality >= 25:
                bree.say "I can't explain it, Victor - I just love being with you!"
            elif hero.morality <= -25:
                bree.say "Yeah, Victor - you just really excite me, if you know what I mean?"
            else:
                bree.say "I know, it's weird, Victor - I'm not normally this into new people!"
    return

label victor_love_2_female:
    if victor.sub >= 50:
        victor.say "I don't make friends easily, [hero.name]- but with you, it's like I don't have a choice!"
    elif victor.sub <= -50:
        victor.say "Normally it's hard for me to connect with people, [hero.name]- but with you it's different."
    else:
        victor.say "I really feel like we're connecting, [hero.name]- you know, getting on really well?"
    menu:
        "I feel the same way too":
            if hero.morality >= 25:
                bree.say "I can't lie, Victor - I feel the same way too."
            elif hero.morality <= -25:
                bree.say "Oh, I want to connect with you, Victor - in a very literal sense!"
            else:
                bree.say "Me too, Victor - we've really hit it off, haven't we?"
        "I think you're being drawn to me":
            if hero.morality >= 25:
                bree.say "Hmm...I've noticed you gravitating towards me, if that's what you mean?"
            elif hero.morality <= -25:
                bree.say "I've seen the signs before, Victor - you want me like crazy!"
            else:
                bree.say "I feel like you're drawn to me, Victor - like you need me in your life."
        "I can't help being drawn to you":
            if hero.morality >= 25:
                bree.say "I can't help it, Victor - you're a magnetic kind of guy!"
            elif hero.morality <= -25:
                bree.say "Oh, Victor - you can ask me to do anything for you...anything at all!"
            else:
                bree.say "Well, you're an interesting guy, Victor, really fascinating."
    return

label victor_love_3_female:
    if victor.sub >= 50:
        victor.say "I'm really glad you gave me a chance, [hero.name], that we've become more than friends."
    elif victor.sub <= -50:
        victor.say "I think it's time we admitted the truth, [hero.name]- we're meant to be more than just friends!"
    else:
        victor.say "Your friendship means so much to me, [hero.name]- but maybe we could be even more?"
    menu:
        "I think we already are more than friends":
            if hero.morality >= 25:
                bree.say "Oh yeah, Victor - we're so much more than just friends!"
            elif hero.morality <= -25:
                bree.say "Of course we are - we're even more than friends with benefits!"
            else:
                bree.say "I've been thinking the same thing, Victor, the exact same thing!"
        "Slow down there, cowboy!":
            if hero.morality >= 25:
                bree.say "We're friends for sure, Victor - but I'm not sure we're anything more just yet."
            elif hero.morality <= -25:
                bree.say "Whoa...wait a minute, Victor - just because I'm liberated doesn't mean I'm easy!"
            else:
                bree.say "I like you a lot, Victor - but I want to take things slowly, okay?"
        "I think that you really need me":
            if hero.morality >= 25:
                bree.say "Well, I kind of see you as a project, Victor - someone that needs me to fix them."
            elif hero.morality <= -25:
                bree.say "You'd better stick around, Victor - because do I have things to teach you!"
            else:
                bree.say "You're a definite fixer-upper, Victor - but I like a challenge!"
    return

label victor_love_4_female:
    if victor.sub >= 50:
        victor.say "I used to think my heart was cold and dead, [hero.name]- but then you brought me back to life!"
    elif victor.sub <= -50:
        victor.say "I thought my personal life was dead and gone, [hero.name]- but you went and changed all that."
    else:
        victor.say "I thought all I had was my job, [hero.name]- but now I have you to look after too."
    menu:
        "I feel the same way too":
            if hero.morality >= 25:
                bree.say "I can't imagine my life without you, Victor!"
            elif hero.morality <= -25:
                bree.say "I can't imagine life without you - or a certain specific part of you!"
            else:
                bree.say "Aww...that's so sweet of you to say - I feel the same way too!"
        "Things change":
            if hero.morality >= 25:
                bree.say "Don't get too emotional, Victor - things can always change."
            elif hero.morality <= -25:
                bree.say "Ah well...I can get really bored of a guy, if he's not flexible in the bedroom!"
            else:
                bree.say "This all happened really quickly, so it could change just as fast."
        "It's like you walked in and took over my life!":
            if hero.morality >= 25:
                bree.say "I know, Victor - it feels like you were destined to meet me, to steer my destiny!"
            elif hero.morality <= -25:
                bree.say "I am SO ready to get down on my knees and obey your every command!"
            else:
                bree.say "Tell me about it - I sometimes think you were always meant to be the one!"
    return

label victor_love_5_female:
    if victor.sub >= 50:
        victor.say "I used to think my heart was cold and dead, [hero.name]- but then you brought me back to life!"
    elif victor.sub <= -50:
        victor.say "I thought my personal life was dead and gone, [hero.name]- but you went and changed all that."
    else:
        victor.say "I thought all I had was my job, [hero.name]- but now I have you to look after too."
    menu:
        "I feel the same way too":
            if hero.morality >= 25:
                bree.say "I can't imagine my life without you, Victor!"
            elif hero.morality <= -25:
                bree.say "I can't imagine life without you - or a certain specific part of you!"
            else:
                bree.say "Aww...that's so sweet of you to say - I feel the same way too!"
        "Things change":
            if hero.morality >= 25:
                bree.say "Don't get too emotional, Victor - things can always change."
            elif hero.morality <= -25:
                bree.say "Ah well...I can get really bored of a guy, if he's not flexible in the bedroom!"
            else:
                bree.say "This all happened really quickly, so it could change just as fast."
        "It's like you walked in and took over my life!":
            if hero.morality >= 25:
                bree.say "I know, Victor - it feels like you were destined to meet me, to steer my destiny!"
            elif hero.morality <= -25:
                bree.say "I am SO ready to get down on my knees and obey your every command!"
            else:
                bree.say "Tell me about it - I sometimes think you were always meant to be the one!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
