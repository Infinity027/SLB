label camila_desire_0_male:
    camila.say "I'm glad I was on duty when you came to the station, [hero.name]."
    camila.say "How about you?"
    menu:
        "Agree":
            mike.say "Me too, Camila."
            mike.say "I can't imagine another cop tackling my case!"
            $ camila.love += 1
        "Disagree":
            mike.say "Whatever, Camila."
            mike.say "I'm sure another cop would have done the same."
            $ camila.love -= 1
    return

label camila_desire_1_male:
    camila.say "It's good that we decided to hang out together, [hero.name]."
    camila.say "You know, get together as friends?"
    menu:
        "Agree":
            mike.say "That's how I feel too, Camila."
            mike.say "There's so much more to you than just being a cop!"
            $ camila.love += 1
        "Disagree":
            mike.say "I don't know about that, Camila."
            mike.say "It kind of makes you seem more ordinary."
            $ camila.sub += 1
    return

label camila_desire_2_male:
    camila.say "[hero.name]..."
    camila.say "Those hookers I busted the other day..."
    camila.say "You weren't checking them out, were you?"
    menu:
        "Of course not":
            mike.say "No, Camila, no way!"
            mike.say "I was just feeling sorry for them, that's all."
            $ camila.love += 1
        "That's exactly what I was doing":
            mike.say "Of course I was, Camila."
            mike.say "They were some seriously hot trash!"
            $ camila.sub += 1
    return

label camila_desire_3_male:
    camila.say "I have such a great time when we're together, [hero.name]."
    camila.say "You think we should take it to the next level?"
    camila.say "You know, make it official between us?"
    menu:
        "Agree":
            mike.say "I'd love that, Camila."
            mike.say "Anything to spend more time with you!"
            $ camila.love += 1
        "Disagree":
            mike.say "I don't like the sound of that, Camila!"
            mike.say "Can't we just stay buddies?"
            $ camila.love -= 1
    return

label camila_desire_4_male:
    camila.say "I gotta say it, [hero.name]."
    camila.say "You're making me hot right now!"
    menu:
        "Agree":
            mike.say "You always make me hot, Camila!"
            mike.say "And you're the only one that can put out the fire too!"
            $ camila.love += 1
        "Disagree":
            mike.say "Geez, Camila - what's got you so worked up?"
            mike.say "Did you shoot someone at work again?"
            $ camila.love -= 1
    return

label camila_desire_5_male:
    camila.say "I...I used to feel like I was married to the force, [hero.name]."
    camila.say "But just recently, I realised you matter more to me these days!"
    camila.say "In fact, sometimes you're all I can think about."
    menu:
        "Agree":
            mike.say "Wow, Camila - I know what being a cop means to you."
            mike.say "So if you loved me half as much as the job, I'd be a lucky guy."
            mike.say "That you love me more must mean I'm the luckiest guy in the world!"
            $ camila.love += 1
        "Disagree":
            mike.say "You mean that I'm making you lose your edge, Camila?"
            mike.say "That since we got together you've gotten sloppy?"
            mike.say "Geez, you're basically admitting to being a bad cop!"
            $ camila.love -= 1
    return

label camila_love_0_male:
    camila.say "Urgh..."
    camila.say "I'm so beat."
    camila.say "That was some crazy shift!"
    menu:
        "Agree":
            mike.say "Well, you're off duty now, Camila."
            mike.say "So let's forget all about it and relax, yeah?"
            $ camila.love += 1
        "Disagree":
            mike.say "Geez, Camila, what's with all the complaining?"
            mike.say "Aren't you cops always telling us your job's tough?"
            $ camila.sub += 1
    return

label camila_love_1_male:
    camila.say "Hey, [hero.name]!"
    camila.say "How's things with you, huh?"
    menu:
        "Be nice":
            mike.say "Thanks for asking, Camila."
            mike.say "It means a lot to know you care."
            $ camila.love += 1
        "Scold her":
            mike.say "Huh, why are you asking me that?"
            mike.say "You cops are always snooping in people's business!"
            $ camila.sub += 1
    return

label camila_love_2_male:
    camila.say "I gotta say it, [hero.name]."
    camila.say "You're looking happier than I've seen you in a while!"
    menu:
        "Agree":
            mike.say "Well, that's down to you, Camila."
            mike.say "I know you've got my case in hand."
            mike.say "But more importantly, you're a good friend too!"
            $ camila.love += 1
        "Disagree":
            mike.say "Yeah well, it's not thanks to you and your fellow cops."
            mike.say "So don't go looking for a positive review from me!"
            $ camila.love -= 1
    return

label camila_love_3_male:
    camila.say "Hey, [hero.name]!"
    camila.say "You wanna come score a beer with me?"
    camila.say "I just got off of work, and I have a hankering for a cold one!"
    menu:
        "Agree":
            mike.say "I'm right there, Camila."
            mike.say "Can't wait to hear all about your day."
            mike.say "About all the bad guys you busted!"
            $ camila.love += 1
        "Disagree":
            mike.say "Ah, is that such a good idea, Camila?"
            mike.say "Booze isn't the answer to everything."
            mike.say "You know that, right?"
            $ camila.love -= 1
    return

label camila_love_4_male:
    camila.say "Spending time with you is so much fun, [hero.name]."
    camila.say "I feel like I can't get enough of you!"
    menu:
        "Agree":
            mike.say "I know exactly what you mean, Camila."
            mike.say "Whenever we have to go our separate ways..."
            mike.say "Well, all I can think about is when I can see you next!"
            $ camila.love += 1
        "Disagree":
            mike.say "Yeah, Camila, the thing is..."
            mike.say "I've been feeling a little claustrophobic around you lately."
            mike.say "And I think I need less time around you, not more!"
            $ camila.love -= 1
    return

label camila_love_5_male:
    camila.say "I never thought I'd be saying this about anyone, [hero.name]."
    camila.say "But since we met, you're really gotten under my skin!"
    camila.say "I think I'm in love with you!"
    menu:
        "Agree":
            mike.say "I feel the same way, Camila!"
            mike.say "Like you're a part of me now."
            $ camila.love += 1
        "Disagree":
            mike.say "Urgh!"
            mike.say "You're talking about me like I'm ringworm, Camila!"
            mike.say "Way to let me know how you actually feel."
            $ camila.sub += 1
    return

label camila_good_sweet_talk_male:
    show camila
    if camila.love > 133:
        mike.say "Do you have your handcuff on you, Camila?"
        mike.say "I...I was wondering if you'd...maybe interrogate me?"
        show camila flirt
        camila.say "Sure thing, [hero.name]."
        camila.say "I'll break you, but you'll love every moment!"
    elif camila.love > 66:
        mike.say "I love hearing stories about your work, Camila."
        mike.say "It's great knowing that I'm dating a tough cop!"
        show camila flirt
        camila.say "I'm just doing my job, [hero.name]!"
        camila.say "But I DO like that you like it..."
    else:
        mike.say "You're so tough and streetwise, Camila."
        mike.say "I feel safe whenever you're around!"
        show camila happy
        camila.say "Thanks, [hero.name]!"
        camila.say "Protect and serve - that's my duty!"
    hide camila
    return

label camila_bad_sweet_talk_male:
    show camila
    mike.say "I don't think I've ever met a girl as tough as you, Camila."
    mike.say "You're tougher than any guy I know!"
    show camila angry
    camila.say "You think I like hearing stuff like that, huh?"
    camila.say "I am actually a woman, you know?"
    mike.say "Uh...yeah, Camila...please don't hurt me!"
    hide camila
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
