label sasha_desire_0_female:
    sasha.say "You okay with me inviting the girls from the band over here, [hero.name]?"
    sasha.say "They're pretty cool, and I think you'll get on with them too."
    if sasha.love >= 50 and mike.love >= 50:
        bree.say "No need to ask my permission, Sasha - this is your house too!"
        bree.say "But yeah, I'd love to meet the girls in your band."
        $ sasha.love += 1
    else:
        bree.say "Urgh...do you have to bring them back here, Sasha?"
        bree.say "It's noisy enough with you and [mike.name] stomping around the place!"
        $ sasha.sub += 1
    return

label sasha_desire_1_female:
    sasha.say "I'm pretty happy with the fact I got to move in here with you and [mike.name]."
    sasha.say "I've lived with some real pieces of work in my time, [hero.name]!"
    sasha.say "I just feel like you two are good people - like we could all be friends, you know?"
    if sasha.love >= 50:
        bree.say "I know exactly what you mean, Sasha."
        bree.say "And for the record, I think I got pretty lucky too!"
        $ sasha.love += 1
    else:
        bree.say "It's nice to be living with nice people, Sasha."
        bree.say "But you don't have to try so hard to get on with me."
        bree.say "It's not going to impress me."
        $ sasha.sub += 1
    return

label sasha_desire_2_female:
    sasha.say "[hero.name]..."
    sasha.say "I was just wondering..."
    sasha.say "[mike.name] kinda likes the look of himself, doesn't he?"
    if mike.love < 75:
        bree.say "I know exactly what you mean, Sasha!"
        bree.say "It's like he spends more time in the bathroom on a morning than a girl."
        bree.say "Not that it seems to make much of a difference!"
        $ sasha.love += 1
    else:
        bree.say "Of course he does, Sasha!"
        bree.say "And why the hell not?"
        bree.say "After all, it's great we get to live with such a hottie!"
        $ sasha.sub += 1
    return

label sasha_desire_3_female:
    sasha.say "You want to just hang out with me today, [hero.name]?"
    sasha.say "I could have made plans...but I just kinda wanted to do whatever."
    sasha.say "Well...so long as we can do it together?"
    if sasha.love >= 75:
        bree.say "You know, it's pretty weird, Sasha."
        bree.say "But I was just thinking the same thing!"
        bree.say "It's like we're always on the same wavelength or something."
        bree.say "Like we have a real connection."
        $ sasha.love += 1
    else:
        bree.say "Wow, Sasha - way to make a girl feel special!"
        bree.say "'Like...duh...you wanna hang out and do like nothing at all?'"
        bree.say "Did you even need to engage your brain to think of that one?"
        $ sasha.love += 1
    return

label sasha_desire_4_female:
    sasha.say "Erm, [hero.name]..."
    sasha.say "You're gonna think this is pretty weird."
    sasha.say "But you look SO hot today - like you're totally owning that look!"
    if hero.charm >= 20:
        bree.say "Thanks, Sasha!"
        bree.say "Is it weird that I kinda like it when you say that too?"
        bree.say "Like it makes me feel...well, even hotter!"
        $ sasha.love += 1
    else:
        bree.say "Well, Sasha, that's kind of the thing..."
        bree.say "Not all of us are happy just to wear black all the time!"
        $ sasha.sub += 1
    return

label sasha_desire_5_female:
    sasha.say "[hero.name]..."
    sasha.say "You wouldn't like...move out without telling me, would you?"
    sasha.say "Because I really feel like I need you in my life!"
    if sasha.love >= 100:
        bree.say "Of course not, Sasha!"
        bree.say "I'm not going anywhere, I promise."
        bree.say "And if I ever do, I'm taking you with me!"
        $ sasha.love += 1
    else:
        bree.say "Where is all of this needy shit coming from, Sasha?"
        bree.say "After all, we're housemates, not soulmates!"
        bree.say "And I'm not going to be living with you forever."
        $ sasha.sub += 1
    return

label sasha_love_0_female:
    sasha.say "Oh man, [hero.name]!"
    sasha.say "Band practice was goddamn awful tonight!"
    sasha.say "None of us could get it together and we sounded like shit!"
    if sasha.love >= 50:
        bree.say "That sounds awful, Sasha!"
        bree.say "And you usually sound so good."
        bree.say "You want to tell me all about it?"
        $ sasha.love += 1
    else:
        bree.say "Whoa - you mean you guys actually practice?"
        bree.say "I thought you just made it up as you went along!"
        $ sasha.sub += 1
    return

label sasha_love_1_female:
    sasha.say "Hey, [hero.name]."
    sasha.say "You don't look too hot today."
    sasha.say "What's eating you?"
    if hero.fun >= 5:
        bree.say "Oh, thank you, Sasha!"
        bree.say "I could really use someone to talk to."
        bree.say "Everyone else just seems to be ignoring me!"
        $ sasha.love += 1
    else:
        bree.say "Like it's any of YOUR business, Sasha!"
        bree.say "I'm not sharing my problems with you."
        bree.say "Because I know you're just fishing for gossip."
        $ sasha.sub += 1
    return

label sasha_love_2_female:
    sasha.say "You're really making those pants work for you, [hero.name]!"
    sasha.say "Since when did you have a butt that went on all day long?"
    if sasha.love >= 75:
        bree.say "Oh these old things?"
        bree.say "I've had them for ages."
        bree.say "But I never realised they did so much for me!"
        bree.say "Maybe I should wear them more often?"
        $ sasha.love += 1
    else:
        bree.say "It's a little thing called style, Sasha."
        bree.say "I don't like wearing slutty little leather numbers and band T-shirts."
        bree.say "Unlike some people I could name..."
        $ sasha.sub += 1
    return

label sasha_love_3_female:
    sasha.say "We should go out and have a drink together, [hero.name]."
    sasha.say "You know, just you and me - no [mike.name]!"
    sasha.say "I think it'd be fun, don't you?"
    if mike.love < 75:
        bree.say "I've been waiting for you to say that, Sasha!"
        bree.say "We can go do it the very first chance we get."
        bree.say "Let's make it when [mike.name]'s fallen asleep and started snoring!"
        $ sasha.love += 1
    else:
        bree.say "Oh no, Sasha, no way is that happening!"
        bree.say "I've seen the kind of places you like to drink in."
        bree.say "I wouldn't feel safe there, not without [mike.name] to protect me!"
        $ sasha.sub += 1
    return

label sasha_love_4_female:
    sasha.say "I feel like I have to say this, [hero.name]."
    sasha.say "Like if I don't then I might never manage to get it out!"
    sasha.say "You've become like my best friend, [hero.name] - maybe even more than that!"
    if sasha.love >= 100:
        bree.say "That's uncanny, Sasha!"
        bree.say "It's like you're reading my mind right now!"
        bree.say "I feel the exact same way."
        $ sasha.love += 1
    else:
        bree.say "Erm...maybe you shouldn't have said that at all, Sasha!"
        bree.say "We're like, casual friends at best, at least in my mind."
        bree.say "Nothing more than that."
        $ sasha.sub += 1
    return

label sasha_love_5_female:
    sasha.say "I'm just gonna say whatever comes into my head, [hero.name]."
    sasha.say "I'm gonna be totally honest, and fuck the consequences."
    sasha.say "I love you, [hero.name] - I just frikin love you, okay?"
    if sasha.love >= 150:
        bree.say "Me too, Sasha, me too!"
        bree.say "I...I mean I love you too - not me!"
        bree.say "You know what I mean, right?"
        $ sasha.love += 1
    else:
        bree.say "Whoa...way to over-share, Sasha!"
        bree.say "You know next time, maybe keep it to yourself?"
        bree.say "Because that love you're talking about is just in your head!"
        $ sasha.sub += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
