label minami_desire_0_female:
    minami.say "I'm so glad that I could move in here, rather than into a hall of residence with all of those strange guys."
    minami.say "You're the only strange guy that I want to be around, big bro!"
    if minami.siscon >= 15:
        bree.say "Hah, you have NO idea how strange I am, Minami!"
    else:
        bree.say "Ah, I'm sure you'd have gotten used to it in the end, Minami..."
        $ minami.siscon += 2
    return

label minami_desire_1_female:
    minami.say "I just love living here with you, [hero.name] and Sasha."
    minami.say "One guy and two girls - I bet you have all kinds of fun together!"
    if minami.siscon >= 30:
        bree.say "Minami, you have NO idea!"
    else:
        bree.say "Erm...we play boardgames sometimes, if that's what you mean?"
        $ minami.siscon += 2
    return

label minami_desire_2_female:
    minami.say "Big bro..."
    minami.say "Be honest - do you think [hero.name] and Sasha are prettier than me?"
    if minami.siscon >= 45:
        bree.say "Don't tell them I said so, Minami."
        bree.say "But they both wish they were as cute as you!"
    else:
        bree.say "I...I don't know, Minami."
        bree.say "I don't see them in that way - or you!"
        $ minami.siscon += 2
    return

label minami_desire_3_female:
    minami.say "I know we've always been pretty close, big bro."
    minami.say "But now that we're living together I want to get to know you in a whole new way..."
    if minami.siscon >= 60:
        bree.say "Me too, Minami."
        bree.say "Having you here with me's made me see you in a whole new light..."
    else:
        bree.say "I think we're good enough friends already, Minami - don't you?!?"
        $ minami.siscon += 2
    return

label minami_desire_4_female:
    minami.say "Wow - you look SO good today, big bro."
    minami.say "Almost good enough to eat!"
    if minami.siscon >= 75:
        bree.say "Well, you'd better have a healthy appetite, Minami."
        bree.say "Because I always fill a girl right up!"
    else:
        bree.say "I...I look just the same as I did yesterday!"
        bree.say "And the day before that too..."
        $ minami.siscon += 2
    return

label minami_desire_5_female:
    minami.say "I don't think I could get out of bed without knowing I'd see you every day, big bro!"
    if minami.siscon >= 90:
        bree.say "With the right sleeping arrangements, you could see me before you have to..."
    else:
        bree.say "Ah...maybe you should invest in an alarm clock?"
        $ minami.siscon += 2
    return

label minami_love_0_female:
    minami.say "Hey, big bro."
    minami.say "What's up with you?"
    menu:
        "Be nice":
            bree.say "Nothing, now that you're here, Minami!"
            if minami.love >= 200:
                $ minami.siscon += 1
            else:
                $ minami.love += 1
        "Scold her":
            bree.say "I like to be the one asking the questions, Minami."
            $ minami.sub += 1
        "Tease her" if minami.siscon >= 50:
            bree.say "I was just thinking about your girlfriends back home, Minami..."
            $ minami.lesbian += 1
    return

label minami_love_1_female:
    minami.say "Phew!"
    minami.say "I had such a hard day at college."
    minami.say "And now I'm pooped!"
    menu:
        "Be nice":
            bree.say "Come and sit down, Minami - tell me all about it."
            if minami.love >= 200:
                $ minami.siscon += 1
            else:
                $ minami.love += 1
        "Scold her":
            bree.say "I think my day at the office might have been harder, Minami!"
            $ minami.sub += 1
        "Tease her" if minami.siscon >= 50:
            bree.say "Maybe you could ask [hero.name] or Sasha for a massage?"
            $ minami.lesbian += 1
    return

label minami_love_2_female:
    minami.say "All I do is talk about me, big bro!"
    minami.say "How are you doing, you know?"
    minami.say "College and work not getting you down?"
    menu:
        "Be nice":
            bree.say "Thanks for taking the time to ask, Minami."
            bree.say "It means a lot to know that you care."
            if minami.love >= 200:
                $ minami.siscon += 1
            else:
                $ minami.love += 1
        "Scold her":
            bree.say "If I wanted you to know that, Minami, I'd have told you already!"
            $ minami.sub += 1
        "Tease her" if minami.siscon >= 50:
            bree.say "Yeah, sometimes it does."
            bree.say "But thinking of [hero.name], Sasha and you all under one roof always helps."
            $ minami.lesbian += 1
    return

label minami_love_3_female:
    minami.say "Would you like a little treat tomorrow morning, big bro?"
    minami.say "Maybe breakfast in bed?"
    menu:
        "Be nice":
            bree.say "If I could see you first thing every morning, Minami - that'd be enough of a treat for me!"
            if minami.love >= 200:
                $ minami.siscon += 1
            else:
                $ minami.love += 1
        "Scold her":
            bree.say "Hmm...that'd be nice, Minami."
            bree.say "Maybe you could wear that cute maid outfit you have too..."
            $ minami.sub += 1
        "Tease her" if minami.siscon >= 50:
            bree.say "Only if you do the same for [hero.name] and Sasha too."
            bree.say "And you shouldn't worry about walking in on them, either..."
            $ minami.lesbian += 1
    return

label minami_love_4_female:
    minami.say "I...want to spend more time with you, big bro."
    minami.say "Not around [hero.name] or Sasha either."
    minami.say "Just you and me..."
    menu:
        "Be nice":
            bree.say "I've been wanting the same thing, Minami."
            bree.say "I just didn't know how to say it!"
            if minami.love >= 200:
                $ minami.siscon += 1
            else:
                $ minami.love += 1
        "Scold her":
            bree.say "We could do that, Minami."
            bree.say "But you'd have to be VERY obedient..."
            $ minami.sub += 1
        "Tease her" if minami.siscon >= 50:
            bree.say "I think we could let [hero.name] and Sasha in on it, Minami."
            bree.say "Especially if we spent the time VERY close together..."
            $ minami.lesbian += 1
    return

label minami_love_5_female:
    minami.say "I...I'm scared to say this, big bro."
    minami.say "But...but...I think I'm in love with you!"
    menu:
        "Be nice" if minami.siscon >= 90:
            bree.say "I...I feel the exact same way, Minami!"
            bree.say "I was scared to admit it too!"
            if minami.love >= 200:
                $ minami.siscon += 1
            else:
                $ minami.love += 1
        "Scold her":
            bree.say "That's great to hear, Minami."
            bree.say "So long as you always remember your place..."
            $ minami.sub += 1
        "Tease her" if minami.siscon >= 90:
            bree.say "I feel the same way, Minami."
            bree.say "But I think we both have enough love to share with someone else..."
            $ minami.lesbian += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
