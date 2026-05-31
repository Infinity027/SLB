label camila_desire_0_female:
    camila.say "I'm glad I was on duty when you came to the station, [hero.name]."
    camila.say "How about you?"
    menu:
        "Agree":
            bree.say "Me too, Camila."
            bree.say "I can't imagine another cop tackling my case!"
            $ camila.love += 1
        "Disagree":
            bree.say "Whatever, Camila."
            bree.say "I'm sure another cop would have done the same."
            $ camila.love -= 1
    return

label camila_desire_1_female:
    camila.say "It's good that we decided to hang out together, [hero.name]."
    camila.say "You know, get together as friends?"
    menu:
        "Agree":
            bree.say "That's how I feel too, Camila."
            bree.say "There's so much more to you than just being a cop!"
            $ camila.love += 1
        "Disagree":
            bree.say "I don't know about that, Camila."
            bree.say "It kind of makes you seem more ordinary."
            $ camila.sub += 1
    return

label camila_desire_2_female:
    camila.say "[hero.name]..."
    camila.say "Those hookers I busted the other day..."
    camila.say "You weren't checking them out, were you?"
    menu:
        "Of course not":
            bree.say "No, Camila, no way!"
            bree.say "I was just feeling sorry for them, that's all."
            $ camila.love += 1
        "That's exactly what I was doing":
            bree.say "Of course I was, Camila."
            bree.say "They were some seriously hot trash!"
            $ camila.sub += 1
    return

label camila_desire_3_female:
    camila.say "I have such a great time when we're together, [hero.name]."
    camila.say "You think we should take it to the next level?"
    camila.say "You know, make it official between us?"
    menu:
        "Agree":
            bree.say "I'd love that, Camila."
            bree.say "Anything to spend more time with you!"
            $ camila.love += 1
        "Disagree":
            bree.say "I don't like the sound of that, Camila!"
            bree.say "Can't we just stay buddies?"
            $ camila.love -= 1
    return

label camila_desire_4_female:
    camila.say "I gotta say it, [hero.name]."
    camila.say "You're making me hot right now!"
    menu:
        "Agree":
            bree.say "You always make me hot, Camila!"
            bree.say "And you're the only one that can put out the fire too!"
            $ camila.love += 1
        "Disagree":
            bree.say "Geez, Camila - what's got you so worked up?"
            bree.say "Did you shoot someone at work again?"
            $ camila.love -= 1
    return

label camila_desire_5_female:
    camila.say "I...I used to feel like I was married to the force, [hero.name]."
    camila.say "But just recently, I realised you matter more to me these days!"
    camila.say "In fact, sometimes you're all I can think about."
    menu:
        "Agree":
            bree.say "Wow, Camila - I know what being a cop means to you."
            bree.say "So if you loved me half as much as the job, I'd be a lucky guy."
            bree.say "That you love me more must mean I'm the luckiest guy in the world!"
            $ camila.love += 1
        "Disagree":
            bree.say "You mean that I'm making you lose your edge, Camila?"
            bree.say "That since we got together you've gotten sloppy?"
            bree.say "Geez, you're basically admitting to being a bad cop!"
            $ camila.love -= 1
    return

label camila_love_0_female:
    camila.say "Urgh..."
    camila.say "I'm so beat."
    camila.say "That was some crazy shift!"
    menu:
        "Agree":
            bree.say "Well, you're off duty now, Camila."
            bree.say "So let's forget all about it and relax, yeah?"
            $ camila.love += 1
        "Disagree":
            bree.say "Geez, Camila, what's with all the complaining?"
            bree.say "Aren't you cops always telling us your job's tough?"
            $ camila.sub += 1
    return

label camila_love_1_female:
    camila.say "Hey, [hero.name]!"
    camila.say "How's things with you, huh?"
    menu:
        "Be nice":
            bree.say "Thanks for asking, Camila."
            bree.say "It means a lot to know you care."
            $ camila.love += 1
        "Scold her":
            bree.say "Huh, why are you asking me that?"
            bree.say "You cops are always snooping in people's business!"
            $ camila.sub += 1
    return

label camila_love_2_female:
    camila.say "I gotta say it, [hero.name]."
    camila.say "You're looking happier than I've seen you in a while!"
    menu:
        "Agree":
            bree.say "Well, that's down to you, Camila."
            bree.say "I know you've got my case in hand."
            bree.say "But more importantly, you're a good friend too!"
            $ camila.love += 1
        "Disagree":
            bree.say "Yeah well, it's not thanks to you and your fellow cops."
            bree.say "So don't go looking for a positive review from me!"
            $ camila.love -= 1
    return

label camila_love_3_female:
    camila.say "Hey, [hero.name]!"
    camila.say "You wanna come score a beer with me?"
    camila.say "I just got off of work, and I have a hankering for a cold one!"
    menu:
        "Agree":
            bree.say "I'm right there, Camila."
            bree.say "Can't wait to hear all about your day."
            bree.say "About all the bad guys you busted!"
            $ camila.love += 1
        "Disagree":
            bree.say "Ah, is that such a good idea, Camila?"
            bree.say "Booze isn't the answer to everything."
            bree.say "You know that, right?"
            $ camila.love -= 1
    return

label camila_love_4_female:
    camila.say "Spending time with you is so much fun, [hero.name]."
    camila.say "I feel like I can't get enough of you!"
    menu:
        "Agree":
            bree.say "I know exactly what you mean, Camila."
            bree.say "Whenever we have to go our separate ways..."
            bree.say "Well, all I can think about is when I can see you next!"
            $ camila.love += 1
        "Disagree":
            bree.say "Yeah, Camila, the thing is..."
            bree.say "I've been feeling a little claustrophobic around you lately."
            bree.say "And I think I need less time around you, not more!"
            $ camila.love -= 1
    return

label camila_love_5_female:
    camila.say "I never thought I'd be saying this about anyone, [hero.name]."
    camila.say "But since we met, you're really gotten under my skin!"
    camila.say "I think I'm in love with you!"
    menu:
        "Agree":
            bree.say "I feel the same way, Camila!"
            bree.say "Like you're a part of me now."
            $ camila.love += 1
        "Disagree":
            bree.say "Urgh!"
            bree.say "You're talking about me like I'm ringworm, Camila!"
            bree.say "Way to let me know how you actually feel."
            $ camila.sub += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
