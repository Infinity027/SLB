label kylie_desire_0_female:
    kylie.say "I started coming over here to hang out with [mike.name]."
    kylie.say "But I feel like it's you I end up talking to more, [hero.name]."
    kylie.say "How weird is that?"
    if kylie.love >= 25:
        bree.say "It's not weird at all, Kylie."
        bree.say "I guess we just have a lot in common!"
        $ kylie.love += 1
    else:
        bree.say "Yeah...I had noticed that, Kylie."
        bree.say "And it's kind of making me feel a little uncomfortable..."
        $ kylie.sub += 1
    return

label kylie_desire_1_female:
    kylie.say "I'm glad we're getting the chance to hang-out together, [hero.name]."
    kylie.say "Because I'm not just one of [mike.name]'s friends, you know?"
    kylie.say "I'm your friend too, right?"
    if kylie.love >= mike.love:
        bree.say "Me too, Kylie."
        bree.say "I like spending time with you."
        bree.say "And who needs [mike.name] anyway!"
        $ kylie.love += 1
    else:
        bree.say "I don't see it that way, Kylie."
        bree.say "I kind of feel forced into it."
        $ kylie.sub += 1
    return

label kylie_desire_2_female:
    kylie.say "[hero.name]..."
    kylie.say "Do you like girls as well as guys?"
    kylie.say "No reason...I just wanted to ask."
    if kylie.love >= 50:
        bree.say "I like both, Kylie."
        bree.say "But it has to be the right guy or girl."
        bree.say "You know what I mean, right?"
        $ kylie.love += 1
    else:
        bree.say "That's kind of a personal question, Kylie."
        bree.say "Stuff I don't feel like sharing with you."
        $ kylie.sub += 1
    return

label kylie_desire_3_female:
    kylie.say "I really want to start hanging out with you more, [hero.name]."
    kylie.say "I feel like we're really making a connection, you know?"
    kylie.say "And we should build on that."
    if kylie.love >= 25:
        bree.say "You're right, Kylie!"
        bree.say "We're getting on great, aren't we?"
        bree.say "Spending more time together makes sense."
        $ kylie.love += 1
    else:
        bree.say "I kind of feel that's too much, Kylie."
        bree.say "I mean, we're like good friends."
        bree.say "But are we anything more than that?"
        $ kylie.sub += 1
    return

label kylie_desire_4_female:
    kylie.say "I love you in that outfit, [hero.name]."
    kylie.say "It totally suits you."
    kylie.say "Fits your figure so well!"
    if hero.charm >= 20:
        bree.say "Thanks for the compliment, Kylie!"
        bree.say "I was kind of hoping you'd like it..."
        $ kylie.love += 1
    else:
        bree.say "It's important to make an effort, Kylie."
        bree.say "I was kind of hoping to inspire you to do the same!"
        $ kylie.sub += 1
    return

label kylie_desire_5_female:
    kylie.say "[hero.name], I can't think of going a day without seeing you!"
    kylie.say "How crazy is that?"
    kylie.say "You feel the same way, right?"
    if kylie.love >= 100:
        bree.say "It's not crazy at all, Kylie!"
        bree.say "I feel the same way about you too."
        bree.say "I want to see you every single day."
        $ kylie.love += 1
    else:
        bree.say "No, Kylie - it is crazy."
        bree.say "And so are you!"
        bree.say "I don't want you around me all the time!"
        $ kylie.sub += 1
    return

label kylie_love_0_female:
    kylie.say "Oh, [hero.name]!"
    kylie.say "I had such a hard day at college..."
    kylie.say "How about you, [hero.name]?"
    if kylie.love >= 50:
        bree.say "Oh, I remember being a student, Kylie!"
        bree.say "People don't realise how tough it can be."
        bree.say "You want to talk about it?"
        $ kylie.love += 1
    else:
        bree.say "Wait a minute, Kylie - you're a student!"
        bree.say "I just bummed around and went drinking when I was at college!"
        $ kylie.sub += 1
    return

label kylie_love_1_female:
    kylie.say "Hey, [hero.name]."
    kylie.say "How are you doing today?"
    kylie.say "I hope you're feeling well?"
    if hero.fun >= 5:
        bree.say "Ah, I was feeling pretty lousy, Kylie."
        bree.say "But seeing you had really cheered me up!"
        bree.say "I don't know why, but it always seems to."
        $ kylie.love += 1
    else:
        bree.say "Yeah well, hope away, Kylie!"
        bree.say "I'm in a pretty shitty mood."
        bree.say "And a few words from you aren't going to change that."
        $ kylie.sub += 1
    return

label kylie_love_2_female:
    kylie.say "You're looking really fit today, [hero.name]."
    kylie.say "More toned...even a little more buff!"
    kylie.say "Have you been working out more than usual?"
    if hero.fitness >= 25:
        bree.say "I have been doing a little more at the gym, Kylie."
        bree.say "Thanks for noticing."
        bree.say "I guess it must be paying off."
        $ kylie.love += 1
    else:
        bree.say "What do you care how fit I'm looking, Kylie?"
        bree.say "Are you like thinking of fighting me or something?"
        bree.say "That is SO weird!"
        $ kylie.sub += 1
    return

label kylie_love_3_female:
    kylie.say "We should have some lunch together, [hero.name]."
    kylie.say "Just you and me, nice and intimate."
    kylie.say "If you're up for it?"
    if kylie.love >= 75:
        bree.say "Ooh...that sounds like a great idea, Kylie!"
        bree.say "When can you make it?"
        bree.say "I'll have a look in my diary too..."
        $ kylie.love += 1
    else:
        bree.say "Is that really such a good idea, Kylie?"
        bree.say "I kind of feel like that would kill my appetite."
        bree.say "There's just something about you that puts me on edge..."
        $ kylie.sub += 1
    return

label kylie_love_4_female:
    kylie.say "I really want to see more of you, [hero.name]."
    kylie.say "I...I mean...I NEED to see more if you!"
    kylie.say "I feel like I need to keep you really close to me!"
    if kylie.love >= 100:
        bree.say "Me too, Kylie."
        bree.say "I feel like we're getting so close."
        bree.say "Almost like it's becoming an obsession!"
        $ kylie.love += 1
    else:
        bree.say "Really, Kylie?"
        bree.say "That's coming on strong."
        bree.say "Maybe too strong, yeah?"
        $ kylie.sub += 1
    return

label kylie_love_5_female:
    kylie.say "I have to tell you this, [hero.name]."
    kylie.say "It's been eating me up inside!"
    kylie.say "I'm in love with you, madly in love with you!"
    if kylie.love >= 150:
        bree.say "Oh my god, Kylie - are you serious?!?"
        bree.say "I feel the same way about you - I mean, I love you!"
        bree.say "I was just waiting for the right time to say it."
        $ kylie.love += 1
    else:
        bree.say "Erm, Kylie..."
        bree.say "I hate to have to say this..."
        bree.say "But you're giving off serious psycho vibes right now!"
        bree.say "Like, totally bunny-boiler!"
        $ kylie.sub += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
