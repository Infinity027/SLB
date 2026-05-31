label kat_desire_0_male:
    kat.say "I'm glad we managed to get to know each other properly, [hero.name]."
    kat.say "After what happened at the gaming tournament..."
    kat.say "Well...let's just say it's great you could put that behind you."
    kat.say "Because I think we have a lot in common."
    menu:
        "Be confident" if hero.charm >= 25:
            mike.say "Don't worry about it, Kat."
            mike.say "I always knew all that aggression was just an act."
            mike.say "And I can guess all the insecurities you're hiding under it too."
            mike.say "Remember, I know what makes you tick!"
            $ kat.sub += 1
        "Be reassured":
            mike.say "Yeah, that was a little crazy, Kat!"
            mike.say "I think we were all too caught up in the moment."
            mike.say "Getting to know the real you is kind of a relief!"
            mike.say "Because you're actually okay."
            $ kat.love += 1
        "Be careful":
            mike.say "Yeah, well..."
            mike.say "We'll have to see about that, Kat."
            mike.say "You were pretty mean to us back then."
            mike.say "So you're going to have to earn my trust."
            $ kat.love -= 1
    return

label kat_desire_1_male:
    kat.say "You know what, [hero.name]..."
    kat.say "I think it'd be cool if we were to hang-out together."
    kat.say "Just you and me, yeah?"
    kat.say "We could play some games, maybe order a pizza?"
    kat.say "Nothing heavy, just friends having fun together."
    menu:
        "Good idea" if not bree.hidden:
            mike.say "I was going to ask you the same thing, Kat!"
            mike.say "I know that [bree.name]'s busy all the time at the moment."
            mike.say "So she couldn't come along anyway."
            mike.say "Just you and me sounds great!"
            $ kat.love += 1
        "[bree.name] is my gaming partner" if not bree.hidden:
            mike.say "I dunno, Kat..."
            mike.say "[bree.name]'s always in on my gaming nights."
            mike.say "And she's tied up at the moment."
            mike.say "If we got together, I'd feel like we were going behind her back."
            $ kat.love -= 1
        "I'd love that":
            mike.say "You'd be up for that?"
            mike.say "Spending time just with me?!?"
            mike.say "I'd love that."
            mike.say "How soon can we do it?"
            $ kat.sub -= 1
    return

label kat_desire_2_male:
    kat.say "I love the way you make me laugh, [hero.name]!"
    kat.say "Most guys don't seem to get me in that way."
    kat.say "But since we've been hanging-out more, I don't know..."
    kat.say "I feel like something's just clicked between us."
    menu:
        "Really?":
            mike.say "Huh?"
            mike.say "You do?!?"
            mike.say "That's weird, Kat."
            mike.say "Because I hadn't noticed that at all!"
            $ kat.love -= 1
        "That's cute":
            mike.say "I guess that means I'm a rare find, huh?"
            mike.say "Sounds like you don't click with men a lot."
            mike.say "Someone like that's worth making an effort to keep."
            mike.say "You know, doing anything to keep them around?"
            $ kat.sub += 1
        "That's great":
            mike.say "I can't explain it in words, Kat."
            mike.say "It just feels natural, that's all."
            mike.say "Like I know what'll make you smile."
            mike.say "I guess that means we're becoming good friends."
            $ kat.love += 1
    return

label kat_desire_3_male:
    kat.say "I love it when we play games together, [hero.name]."
    kat.say "We seem to connect on a level I've never known before."
    kat.say "It kinda makes me wonder..."
    kat.say "What else would we do that well together?"
    menu:
        "I am touched":
            mike.say "Whoa, Kat..."
            mike.say "That's a pretty big compliment!"
            mike.say "And I hope I'm reading you right..."
            mike.say "You mean doing things together that aren't gaming?"
            mike.say "Right?"
            $ kat.love += 1
        "I'm not so sure":
            mike.say "Meh..."
            mike.say "We work together okay, Kat."
            mike.say "But it's nothing like the connection I had with [bree.name]."
            mike.say "I mean, remember how badly we kicked your ass!"
            $ kat.love -= 1
        "I do well thanks to you":
            mike.say "If I'm playing well, Kat..."
            mike.say "It has to be because I have such a great partner!"
            mike.say "Sometimes, I feel like I can't play alone anymore."
            mike.say "Like I need to have you there to be able to perform!"
            $ kat.sub -= 1
    return

label kat_desire_4_male:
    kat.say "To think that all we used to do was play games together!"
    kat.say "Sometimes it amazes me how far we've come, [hero.name]."
    kat.say "Now I can't think of anyone else I'd rather have as my partner."
    kat.say "We make a great team, don't we?"
    menu:
        "Sure":
            mike.say "We sure do, Kat!"
            mike.say "And I do still love playing games with you."
            mike.say "It's just...well, you know..."
            mike.say "There are other fun things to do together too!"
            $ kat.love += 1
        "If you follow my lead":
            mike.say "Yeah, you could say that, Kat."
            mike.say "But a team needs a leader, doesn't it?"
            mike.say "One person to give orders and another to take them."
            mike.say "And I think we both know who fill what role, don't we?"
            $ kat.sub += 1
        "If you let me free":
            mike.say "I don't know, Kat..."
            mike.say "Sometimes I miss those simpler times."
            mike.say "Back then I could always just quit the game."
            mike.say "I could walk away anytime I wanted."
            $ kat.love -= 1
    return

label kat_desire_5_male:
    kat.say "I'm tired of playing video-games all the time, [hero.name]."
    kat.say "I want to do something different for a change."
    kat.say "And I want it to be something real too."
    kat.say "I want you to play with me!"
    menu:
        "Help me on this one":
            mike.say "Of course, Kat!"
            mike.say "Whatever you say."
            mike.say "But I don't know how to play that game."
            mike.say "So you're going to have to teach me..."
            $ kat.sub -= 1
        "I have a game in mind" if hero.charm >= 25:
            mike.say "You read my mind, Kat!"
            mike.say "And I have just the game in mind."
            mike.say "So hold on tight."
            mike.say "Because you're in for a hell of a ride!"
            $ kat.love += 1
        "No more games":
            mike.say "Yeah, well don't count on that happening, Kat."
            mike.say "I'm tired of playing games too."

            mike.say "So you're going to have to play with yourself!"
            $ kat.love -= 1
    return

label kat_love_0_male:
    kat.say "I have to confess something, [hero.name]..."
    kat.say "Back when we first met, I thought you were such a jerk!"
    kat.say "But now that I've actually got to know you..."
    kat.say "Well, I've realised how wrong I was!"
    menu:
        "Confess":
            mike.say "I'm so happy to hear you say that, Kat!"
            mike.say "I have a confession to make too."
            mike.say "But mine's that I liked you even when we were competing against each other!"
            mike.say "I had to hide it around [bree.name], just to keep the peace!"
            $ kat.sub -= 1
        "Agree":
            mike.say "Of course you feel like that about me, Kat."
            mike.say "That's because I really am a great guy!"
            mike.say "Can't say the same for you though."
            mike.say "You've got some work to do before I'm convinced you're not a bitch!"
            $ kat.love -= 1
        "Reciprocate":
            mike.say "If it helps, Kat..."
            mike.say "I used to feel the same way about you."
            mike.say "I'm just glad we could get past that."
            mike.say "Because I think you're pretty cool too."
            $ kat.love += 1
    return

label kat_love_1_male:
    kat.say "I just wanted to say thanks, [hero.name]."
    kat.say "Hanging-out with you and your friends is really fun."
    kat.say "And I know we didn't get off to a good start."
    kat.say "But you've really made me feel like I belong."
    menu:
        "That was an effort":
            mike.say "Yeah, I know..."
            mike.say "I made sure they all knew to be nice to you."
            mike.say "But I don't know how long that'll last."
            mike.say "I mean, it's not like you're one of my real friends or anything!"
            $ kat.love -= 1
        "That was easy":
            mike.say "That's because you do belong, Kat!"
            mike.say "And I didn't have to make anyone do that either."
            mike.say "You fit in with us really well."
            mike.say "It kind of feels like you've always been there."
            $ kat.love += 1
        "That was the plan" if hero.charm >= 50:
            mike.say "I think they really do like you, Kat."
            mike.say "But that's probably because of what I didn't tell them about you."
            mike.say "And I'm willing to keep it that way."
            mike.say "So long as you prove to me that you're grateful..."
            $ kat.sub += 1
    return

label kat_love_2_male:
    kat.say "I like spending time with your friends, [hero.name]."
    kat.say "But I always seem to end up talking to you the most."
    kat.say "And I was wondering..."
    kat.say "Could we maybe hang-out together, just you and me?"
    menu:
        "Of course" if hero.charm >= 40:
            mike.say "I think I'd like that, Kat."
            mike.say "Having you all to myself sounds kinda nice."
            mike.say "And we can talk about whatever we want."
            mike.say "Not have to worry about entertaining other people too!"
            $ kat.love += 1
        "Of course!!!":
            mike.say "That'd be amazing, Kat!"
            mike.say "I hate it when people cut into our conversations."
            mike.say "If it were just us, there'd be nobody to interrupt."
            mike.say "I could listen to you talk all night!"
            $ kat.sub -= 1
        "I don't think so":
            mike.say "I don't think that's a good idea, Kat."
            mike.say "Because I was going to talk to you about that."
            mike.say "I feel like you've been smothering me recently."

            $ kat.love -= 1
    return

label kat_love_3_male:
    kat.say "When was the last time we did anything with other people?"
    kat.say "I feel like we're almost an exclusive thing, you and me."
    kat.say "And I gotta say - I'M LOVING IT!"
    kat.say "I don't miss the others one little bit!"
    menu:
        "That's what I want":
            mike.say "That's right, Kat..."
            mike.say "You don't need other people to be happy."
            mike.say "We just need each other."
            mike.say "Other people just complicate things."
            $ kat.sub += 1
        "That's not healthy":
            mike.say "That's it!"
            mike.say "That's what's been bugging me!"
            mike.say "This can't be healthy, Kat."
            mike.say "I think we need to mix with a wider circle of people!"
            $ kat.love -= 1
        "That's amazing" if hero.charm >= 40:
            mike.say "Wow...I hadn't noticed, Kat!"
            mike.say "But now you come to mention it, you're right."
            mike.say "I guess I've been having such a good time with you."
            mike.say "I just kind of forgot about everyone else!"
            $ kat.love += 1
    return

label kat_love_4_male:
    kat.say "You feel it too, don't you, [hero.name]?"
    kat.say "Like, we're not just friends anymore, are we?"
    kat.say "I can't go on wondering if you feel the same way!"
    kat.say "You do feel the same way about me, right?"
    menu:
        "Of course we are still friends":
            mike.say "Huh?"
            mike.say "What are you talking about, Kat?"
            mike.say "Sure we're pretty good friends."
            mike.say "But what else is there you want me to say?"
            $ kat.love -= 1
        "Of course we are more than friends":
            mike.say "Sure we're more than friends, Kat!"
            mike.say "I thought that went without saying!"
            mike.say "But if you need me to say it, I will."
            mike.say "We're more than friends - MUCH more than friends!"
            $ kat.love += 1
        "Of course we are what you want us to be":
            mike.say "Why didn't you ask me to say it before, Kat!"
            mike.say "Of course we're more then friends."
            mike.say "We're a couple, lovers, friends with benefits even!"
            mike.say "We're whatever you want us to be!"
            $ kat.sub -= 1
    return

label kat_love_5_male:
    kat.say "I can't hold back any longer, [hero.name]..."
    kat.say "I have to say it before I lose my mind!"
    kat.say "I'm in love with you, totally and crazily!"
    kat.say "And I want to spend the rest of my life with you too."
    menu:
        "Be over the moon":
            mike.say "WOW!"
            mike.say "You put my feelings into words, Kat!"
            mike.say "It's like you read my mind."
            mike.say "Because I feel the same way too."
            $ kat.love += 1
        "Be over her" if hero.charm >= 50:
            mike.say "That's what I want too, Kat."
            mike.say "Exactly what I want."
            mike.say "And it's what'll happen too."
            mike.say "So long as you remember who's in charge..."
            $ kat.sub += 1
        "Be overwhelmed":
            mike.say "Whoa, whoa, whoa..."
            mike.say "Slow down there, Kat!"
            mike.say "All you mentioned there is what YOU feel and YOU want!"
            mike.say "You ever think that I might want to take things a little slower?"
            $ kat.love -= 1
    return

label kat_desire_0_female:
    kat.say "I'm glad we managed to get to know each other properly, [hero.name]."
    kat.say "After what happened at the gaming tournament..."
    kat.say "Well...let's just say it's great you could put that behind you."
    kat.say "Because I think we have a lot in common."
    menu:
        "Be confident" if hero.charm >= 25:
            bree.say "Don't worry about it, Kat."
            bree.say "I always knew all that aggression was just an act."
            bree.say "And I can guess all the insecurities you're hiding under it too."
            bree.say "Remember, I know what makes you tick!"
            $ kat.sub += 1
        "Be reassured":
            bree.say "Yeah, that was a little crazy, Kat!"
            bree.say "I think we were all too caught up in the moment."
            bree.say "Getting to know the real you is kind of a relief!"
            bree.say "Because you're actually okay."
            $ kat.love += 1
        "Be careful":
            bree.say "Yeah, well..."
            bree.say "We'll have to see about that, Kat."
            bree.say "You were pretty mean to us back then."
            bree.say "So you're going to have to earn my trust."
            $ kat.love -= 1
    return

label kat_desire_1_female:
    kat.say "You know what, [hero.name]..."
    kat.say "I think it'd be cool if we were to hang-out together."
    kat.say "Just you and me, yeah?"
    kat.say "We could play some games, maybe order a pizza?"
    kat.say "Nothing heavy, just friends having fun together."
    menu:
        "Good idea" if not mike.hidden:
            bree.say "I was going to ask you the same thing, Kat!"
            bree.say "I know that [mike.name]'s busy all the time at the moment."
            bree.say "So he couldn't come along anyway."
            bree.say "Just you and me sounds great!"
            $ kat.love += 1
        "[mike.name] is my gaming partner" if not mike.hidden:
            bree.say "I dunno, Kat..."
            bree.say "[mike.name]'s always in on my gaming nights."
            bree.say "And he's tied up at the moment."
            bree.say "If we got together, I'd feel like we were going behind his back."
            $ kat.love -= 1
        "I'd love that":
            bree.say "You'd be up for that?"
            bree.say "Spending time just with me?!?"
            bree.say "I'd love that."
            bree.say "How soon can we do it?"
            $ kat.sub -= 1
    return

label kat_desire_2_female:
    kat.say "I love the way you make me laugh, [hero.name]!"
    kat.say "Most guys don't seem to get me in that way."
    kat.say "But since we've been hanging-out more, I don't know..."
    kat.say "I feel like something's just clicked between us."
    menu:
        "Really?":
            bree.say "Huh?"
            bree.say "You do?!?"
            bree.say "That's weird, Kat."
            bree.say "Because I hadn't noticed that at all!"
            $ kat.love -= 1
        "That's cute":
            bree.say "I guess that means I'm a rare find, huh?"
            bree.say "Sounds like you don't click with men a lot."
            bree.say "Someone like that's worth making an effort to keep."
            bree.say "You know, doing anything to keep them around?"
            $ kat.sub += 1
        "That's great":
            bree.say "I can't explain it in words, Kat."
            bree.say "It just feels natural, that's all."
            bree.say "Like I know what'll make you smile."
            bree.say "I guess that means we're becoming good friends."
            $ kat.love += 1
    return

label kat_desire_3_female:
    kat.say "I love it when we play games together, [hero.name]."
    kat.say "We seem to connect on a level I've never known before."
    kat.say "It kinda makes me wonder..."
    kat.say "What else would we do that well together?"
    menu:
        "I am touched":
            bree.say "Whoa, Kat..."
            bree.say "That's a pretty big compliment!"
            bree.say "And I hope I'm reading you right..."
            bree.say "You mean doing things together that aren't gaming?"
            bree.say "Right?"
            $ kat.love += 1
        "I'm not so sure":
            bree.say "Meh..."
            bree.say "We work together okay, Kat."
            bree.say "But it's nothing like the connection I had with [bree.name]."
            bree.say "I mean, remember how badly we kicked your ass!"
            $ kat.love -= 1
        "I do well thanks to you":
            bree.say "If I'm playing well, Kat..."
            bree.say "It has to be because I have such a great partner!"
            bree.say "Sometimes, I feel like I can't play alone anymore."
            bree.say "Like I need to have you there to be able to perform!"
            $ kat.sub -= 1
    return

label kat_desire_4_female:
    kat.say "To think that all we used to do was play games together!"
    kat.say "Sometimes it amazes me how far we've come, [hero.name]."
    kat.say "Now I can't think of anyone else I'd rather have as my partner."
    kat.say "We make a great team, don't we?"
    menu:
        "Sure":
            bree.say "We sure do, Kat!"
            bree.say "And I do still love playing games with you."
            bree.say "It's just...well, you know..."
            bree.say "There are other fun things to do together too!"
            $ kat.love += 1
        "If you follow my lead":
            bree.say "Yeah, you could say that, Kat."
            bree.say "But a team needs a leader, doesn't it?"
            bree.say "One person to give orders and another to take them."
            bree.say "And I think we both know who fill what role, don't we?"
            $ kat.sub += 1
        "If you let me free":
            bree.say "I don't know, Kat..."
            bree.say "Sometimes I miss those simpler times."
            bree.say "Back then I could always just quit the game."
            bree.say "I could walk away anytime I wanted."
            $ kat.love -= 1
    return

label kat_desire_5_female:
    kat.say "I'm tired of playing video-games all the time, [hero.name]."
    kat.say "I want to do something different for a change."
    kat.say "And I want it to be something real too."
    kat.say "I want you to play with me!"
    menu:
        "Help me on this one":
            bree.say "Of course, Kat!"
            bree.say "Whatever you say."
            bree.say "But I don't know how to play that game."
            bree.say "So you're going to have to teach me..."
            $ kat.sub -= 1
        "I have a game in mind":
            bree.say "You read my mind, Kat!"
            bree.say "And I have just the game in mind."
            bree.say "So hold on tight."
            bree.say "Because you're in for a hell of a ride!"
            $ kat.love += 1
        "No more games":
            bree.say "Yeah, well don't count on that happening, Kat."
            bree.say "I'm tired of playing games too."

            bree.say "So you're going to have to play with yourself!"
            $ kat.love -= 1
    return

label kat_love_0_female:
    kat.say "I have to confess something, [hero.name]..."
    kat.say "Back when we first met, I thought you were such a jerk!"
    kat.say "But now that I've actually got to know you..."
    kat.say "Well, I've realised how wrong I was!"
    menu:
        "Confess":
            bree.say "I'm so happy to hear you say that, Kat!"
            bree.say "I have a confession to make too."
            bree.say "But mine's that I liked you even when we were competing against each other!"
            bree.say "I had to hide it around [mike.name], just to keep the peace!"
            $ kat.sub -= 1
        "Agree":
            bree.say "Of course you feel like that about me, Kat."
            bree.say "That's because I really am a great guy!"
            bree.say "Can't say the same for you though."
            bree.say "You've got some work to do before I'm convinced you're not a bitch!"
            $ kat.love -= 1
        "Reciprocate":
            bree.say "If it helps, Kat..."
            bree.say "I used to feel the same way about you."
            bree.say "I'm just glad we could get past that."
            bree.say "Because I think you're pretty cool too."
            $ kat.love += 1
    return

label kat_love_1_female:
    kat.say "I just wanted to say thanks, [hero.name]."
    kat.say "Hanging-out with you and your friends is really fun."
    kat.say "And I know we didn't get off to a good start."
    kat.say "But you've really made me feel like I belong."
    menu:
        "That was an effort":
            bree.say "Yeah, I know..."
            bree.say "I made sure they all knew to be nice to you."
            bree.say "But I don't know how long that'll last."
            bree.say "I mean, it's not like you're one of my real friends or anything!"
            $ kat.love -= 1
        "That was easy":
            bree.say "That's because you do belong, Kat!"
            bree.say "And I didn't have to make anyone do that either."
            bree.say "You fit in with us really well."
            bree.say "It kind of feels like you've always been there."
            $ kat.love += 1
        "That was the plan" if hero.charm >= 50:
            bree.say "I think they really do like you, Kat."
            bree.say "But that's probably because of what I didn't tell them about you."
            bree.say "And I'm willing to keep it that way."
            bree.say "So long as you prove to me that you're grateful..."
            $ kat.love += 1
    return

label kat_love_2_female:
    kat.say "I like spending time with your friends, [hero.name]."
    kat.say "But I always seem to end up talking to you the most."
    kat.say "And I was wondering..."
    kat.say "Could we maybe hang-out together, just you and me?"
    menu:
        "Of course":
            bree.say "I think I'd like that, Kat."
            bree.say "Having you all to myself sounds kinda nice."
            bree.say "And we can talk about whatever we want."
            bree.say "Not have to worry about entertaining other people too!"
            $ kat.love += 1
        "Of course!!!":
            bree.say "That'd be amazing, Kat!"
            bree.say "I hate it when people cut into our conversations."
            bree.say "If it were just us, there'd be nobody to interrupt."
            bree.say "I could listen to you talk all night!"
            $ kat.sub -= 1
        "I don't think so":
            bree.say "I don't think that's a good idea, Kat."
            bree.say "Because I was going to talk to you about that."
            bree.say "I feel like you've been smothering me recently."

            $ kat.love -= 1
    return

label kat_love_3_female:
    kat.say "When was the last time we did anything with other people?"
    kat.say "I feel like we're almost an exclusive thing, you and me."
    kat.say "And I gotta say - I'M LOVING IT!"
    kat.say "I don't miss the others one little bit!"
    menu:
        "That's what I want":
            bree.say "That's right, Kat..."
            bree.say "You don't need other people to be happy."
            bree.say "We just need each other."
            bree.say "Other people just complicate things."
            $ kat.sub += 1
        "That's not healthy":
            bree.say "That's it!"
            bree.say "That's what's been bugging me!"
            bree.say "This can't be healthy, Kat."
            bree.say "I think we need to mix with a wider circle of people!"
            $ kat.love -= 1
        "That's amazing":
            bree.say "Wow...I hadn't noticed, Kat!"
            bree.say "But now you come to mention it, you're right."
            bree.say "I guess I've been having such a good time with you."
            bree.say "I just kind of forgot about everyone else!"
            $ kat.love += 1
    return

label kat_love_4_female:
    kat.say "You feel it too, don't you, [hero.name]?"
    kat.say "Like, we're not just friends anymore, are we?"
    kat.say "I can't go on wondering if you feel the same way!"
    kat.say "You do feel the same way about me, right?"
    menu:
        "Of course we are still friends":
            bree.say "Huh?"
            bree.say "What are you talking about, Kat?"
            bree.say "Sure we're pretty good friends."
            bree.say "But what else is there you want me to say?"
            $ kat.love -= 1
        "Of course we are more than friends":
            bree.say "Sure we're more than friends, Kat!"
            bree.say "I thought that went without saying!"
            bree.say "But if you need me to say it, I will."
            bree.say "We're more than friends - MUCH more than friends!"
            $ kat.love += 1
        "Of course we are what you want us to be":
            bree.say "Why didn't you ask me to say it before, Kat!"
            bree.say "Of course we're more then friends."
            bree.say "We're a couple, lovers, friends with benefits even!"
            bree.say "We're whatever you want us to be!"
            $ kat.sub -= 1
    return

label kat_love_5_female:
    kat.say "I can't hold back any longer, [hero.name]..."
    kat.say "I have to say it before I lose my mind!"
    kat.say "I'm in love with you, totally and crazily!"
    kat.say "And I want to spend the rest of my life with you too."
    menu:
        "Be over the moon":
            bree.say "WOW!"
            bree.say "You put my feelings into words, Kat!"
            bree.say "It's like you read my mind."
            bree.say "Because I feel the same way too."
            $ kat.love += 1
        "Be over her" if hero.charm >= 50:
            bree.say "That's what I want too, Kat."
            bree.say "Exactly what I want."
            bree.say "And it's what'll happen too."
            bree.say "So long as you remember who's in charge..."
            $ kat.sub += 1
        "Be overwhelmed":
            bree.say "Whoa, whoa, whoa..."
            bree.say "Slow down there, Kat!"
            bree.say "All you mentioned there is what YOU feel and YOU want!"
            bree.say "You ever think that I might want to take things a little slower?"
            $ kat.love -= 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
