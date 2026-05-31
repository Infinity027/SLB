label minami_desire_0_male:
    minami.say "I'm so glad that I could move in here, rather than into a hall of residence with all of those strange guys."
    minami.say "You're the only strange guy that I want to be around, big bro!"
    if minami.siscon >= 15:
        mike.say "Hah, you have NO idea how strange I am, Minami!"
    else:
        mike.say "Ah, I'm sure you'd have gotten used to it in the end, Minami..."
        $ minami.siscon += 2
    return

label minami_desire_1_male:
    if bree.is_gone_forever and sasha.is_gone_forever:
        minami.say "I just love living here with you."
        minami.say "You all alone - I bet you feel lonely sometimes..."
    elif bree.is_gone_forever:
        minami.say "I just love living here with you and Sasha."
        minami.say "One guy and one girl - I bet you have all kinds of fun together!"
    elif sasha.is_gone_forever:
        minami.say "I just love living here with you and [bree.name]."
        minami.say "One guy and a girl - I bet you have all kinds of fun together!"
    else:
        minami.say "I just love living here with you, [bree.name] and Sasha."
        minami.say "One guy and two girls - I bet you have all kinds of fun together!"
    if minami.siscon >= 30:
        mike.say "Minami, you have NO idea!"
    else:
        if bree.is_gone_forever and sasha.is_gone_forever:
            mike.say "Erm...I watch TV... A lot?"
        else:
            mike.say "Erm...we play boardgames sometimes, if that's what you mean?"
        $ minami.siscon += 2
    return

label minami_desire_2_male:
    minami.say "Big bro..."
    if bree.is_gone_forever and sasha.is_gone_forever:
        minami.say "Be honest - do you think I'm pretty?"
        if minami.siscon >= 45:
            mike.say "Well, Minami."
            mike.say "No one I know is as cute as you!"
        else:
            mike.say "I...I don't know, Minami."
            mike.say "I don't see you in that way!"
            $ minami.siscon += 2
    elif bree.is_gone_forever:
        minami.say "Be honest - do you think Sasha is prettier than me?"
        if minami.siscon >= 45:
            mike.say "Don't tell her I said so, Minami."
            mike.say "But she wishes she was as cute as you!"
        else:
            mike.say "I...I don't know, Minami."
            mike.say "I don't see her in that way - or you!"
            $ minami.siscon += 2
    elif sasha.is_gone_forever:
        minami.say "Be honest - do you think [bree.name] is prettier than me?"
        if minami.siscon >= 45:
            mike.say "Don't tell her I said so, Minami."
            mike.say "But she wishes she was as cute as you!"
        else:
            mike.say "I...I don't know, Minami."
            mike.say "I don't see her in that way - or you!"
            $ minami.siscon += 2
    else:
        minami.say "Be honest - do you think [bree.name] and Sasha are prettier than me?"
        if minami.siscon >= 45:
            mike.say "Don't tell them I said so, Minami."
            mike.say "But they both wish they were as cute as you!"
        else:
            mike.say "I...I don't know, Minami."
            mike.say "I don't see them in that way - or you!"
            $ minami.siscon += 2
    return

label minami_desire_3_male:
    minami.say "I know we've always been pretty close, big bro."
    minami.say "But now that we're living together I want to get to know you in a whole new way..."
    if minami.siscon >= 60:
        mike.say "Me too, Minami."
        mike.say "Having you here with me's made me see you in a whole new light..."
    else:
        mike.say "I think we're good enough friends already, Minami - don't you?!?"
        $ minami.siscon += 2
    return

label minami_desire_4_male:
    minami.say "Wow - you look SO good today, big bro."
    minami.say "Almost good enough to eat!"
    if minami.siscon >= 75:
        mike.say "Well, you'd better have a healthy appetite, Minami."
        mike.say "Because I always fill a girl right up!"
    else:
        mike.say "I...I look just the same as I did yesterday!"
        mike.say "And the day before that too..."
        $ minami.siscon += 2
    return

label minami_desire_5_male:
    minami.say "I don't think I could get out of bed without knowing I'd see you every day, big bro!"
    if minami.siscon >= 90:
        mike.say "With the right sleeping arrangements, you could see me before you have to..."
    else:
        mike.say "Ah...maybe you should invest in an alarm clock?"
        $ minami.siscon += 2
    return

label minami_love_0_male:
    minami.say "Hey, big bro."
    minami.say "What's up with you?"
    menu:
        "Be nice":
            mike.say "Nothing, now that you're here, Minami!"
            if minami.love >= 200:
                $ minami.siscon += 1
            else:
                $ minami.love += 1
        "Scold her":
            mike.say "I like to be the one asking the questions, Minami."
            $ minami.sub += 1
        "Tease her" if minami.siscon >= 50:
            if bree.is_gone_forever and sasha.is_gone_forever:
                mike.say "I was just thinking about what we'll do back home, Minami..."
                $ minami.sub += 1
            elif bree.is_gone_forever or sasha.is_gone_forever:
                mike.say "I was just thinking about your girlfriend back home, Minami..."
                $ minami.lesbian += 1
            else:
                mike.say "I was just thinking about your girlfriends back home, Minami..."
                $ minami.lesbian += 1
    return

label minami_love_1_male:
    minami.say "Phew!"
    minami.say "I had such a hard day at college."
    minami.say "And now I'm pooped!"
    menu:
        "Be nice":
            mike.say "Come and sit down, Minami - tell me all about it."
            if minami.love >= 200:
                $ minami.siscon += 1
            else:
                $ minami.love += 1
        "Scold her":
            mike.say "I think my day at the office might have been harder, Minami!"
            $ minami.sub += 1
        "Tease her" if minami.siscon >= 50:
            if bree.is_gone_forever and sasha.is_gone_forever:
                mike.say "I think there's a massage parlor in town, maybe you could go there?"
                $ minami.sub += 1
            elif bree.is_gone_forever:
                mike.say "Maybe you could ask Sasha for a massage?"
                $ minami.lesbian += 1
            elif sasha.is_gone_forever:
                mike.say "Maybe you could ask [bree.name] for a massage?"
                $ minami.lesbian += 1
            else:
                mike.say "Maybe you could ask [bree.name] or Sasha for a massage?"
                $ minami.lesbian += 1
    return

label minami_love_2_male:
    minami.say "All I do is talk about me, big bro!"
    minami.say "How are you doing, you know?"
    minami.say "College and work not getting you down?"
    menu:
        "Be nice":
            mike.say "Thanks for taking the time to ask, Minami."
            mike.say "It means a lot to know that you care."
            if minami.love >= 200:
                $ minami.siscon += 1
            else:
                $ minami.love += 1
        "Scold her":
            mike.say "If I wanted you to know that, Minami, I'd have told you already!"
            $ minami.sub += 1
        "Tease her" if minami.siscon >= 50:
            mike.say "Yeah, sometimes it does."
            if bree.is_gone_forever and sasha.is_gone_forever:
                mike.say "But thinking of you living here always helps."
                $ minami.sub += 1
            elif bree.is_gone_forever:
                mike.say "But thinking of Sasha and you all under one roof always helps."
                $ minami.lesbian += 1
            elif sasha.is_gone_forever:
                mike.say "But thinking of [bree.name] and you all under one roof always helps."
                $ minami.lesbian += 1
            else:
                mike.say "But thinking of [bree.name], Sasha and you all under one roof always helps."
                $ minami.lesbian += 1
    return

label minami_love_3_male:
    minami.say "Would you like a little treat tomorrow morning, big bro?"
    minami.say "Maybe breakfast in bed?"
    menu:
        "Be nice":
            mike.say "If I could see you first thing every morning, Minami - that'd be enough of a treat for me!"
            if minami.love >= 200:
                $ minami.siscon += 1
            else:
                $ minami.love += 1
        "Scold her":
            mike.say "Hmm...that'd be nice, Minami."
            mike.say "Maybe you could wear that cute maid outfit you have too..."
            $ minami.sub += 1
        "Tease her" if minami.siscon >= 50:
            if bree.is_gone_forever and sasha.is_gone_forever:
                mike.say "Only if you do the same for [bree.name] and Sasha too."
                mike.say "And you shouldn't worry about walking in on them, either..."
            if bree.is_gone_forever:
                mike.say "Only if you do the same for Sasha too."
                mike.say "And you shouldn't worry about walking in on her, either..."
            elif sasha.is_gone_forever:
                mike.say "Only if you do the same for [bree.name] too."
                mike.say "And you shouldn't worry about walking in on her, either..."
            else:
                mike.say "Only if you do the same for [bree.name] and Sasha too."
                mike.say "And you shouldn't worry about walking in on them, either..."
            $ minami.lesbian += 1
    return

label minami_love_4_male:
    minami.say "I...want to spend more time with you, big bro."
    if bree.is_gone_forever and sasha.is_gone_forever:
        minami.say "Just you and me..."
    elif bree.is_gone_forever:
        minami.say "Not around Sasha."
        minami.say "Just you and me..."
    elif sasha.is_gone_forever:
        minami.say "Not around [bree.name]."
        minami.say "Just you and me..."
    else:
        minami.say "Not around [bree.name] or Sasha either."
        minami.say "Just you and me..."
    menu:
        "Be nice":
            mike.say "I've been wanting the same thing, Minami."
            mike.say "I just didn't know how to say it!"
            if minami.love >= 200:
                $ minami.siscon += 1
            else:
                $ minami.love += 1
        "Scold her":
            mike.say "We could do that, Minami."
            mike.say "But you'd have to be VERY obedient..."
            $ minami.sub += 1
        "Tease her" if minami.siscon >= 50:
            if bree.is_gone_forever and sasha.is_gone_forever:
                mike.say "We could do that, Minami."
                mike.say "But you'd have to be VERY obedient..."
                $ minami.sub += 1
            elif bree.is_gone_forever:
                mike.say "I think we could let Sasha in on it, Minami."
                mike.say "Especially if we spent the time VERY close together..."
                $ minami.lesbian += 1
            elif sasha.is_gone_forever:
                mike.say "I think we could let [bree.name] in on it, Minami."
                mike.say "Especially if we spent the time VERY close together..."
                $ minami.lesbian += 1
            else:
                mike.say "I think we could let [bree.name] and Sasha in on it, Minami."
                mike.say "Especially if we spent the time VERY close together..."
                $ minami.lesbian += 1
    return

label minami_love_5_male:
    minami.say "I...I'm scared to say this, big bro."
    minami.say "But...but...I think I'm in love with you!"
    menu:
        "Be nice" if minami.siscon >= 90:
            mike.say "I...I feel the exact same way, Minami!"
            mike.say "I was scared to admit it too!"
            if minami.love >= 200:
                $ minami.siscon += 1
            else:
                $ minami.love += 1
        "Scold her":
            mike.say "That's great to hear, Minami."
            mike.say "So long as you always remember your place..."
            $ minami.sub += 1
        "Tease her" if minami.siscon >= 90:
            mike.say "I feel the same way, Minami."
            mike.say "But I think we both have enough love to share with someone else..."
            $ minami.lesbian += 1
    return

label minami_good_sweet_talk_male:
    show minami
    if minami.love > 133:
        mike.say "You're so hot and sexy, Minami!"
        mike.say "You're the best thing to happen to me - ever!"
        show minami tehe blush
        minami.say "Aww, thank you, big bro!"
        minami.say "You're all I ever wanted too!"
    elif minami.love > 66:
        mike.say "Things just feel so much easier now we're together, Minami."
        mike.say "So much more natural, you know?"
        minami.say "Yeah, big bro, I do."
        minami.say "We can finally be honest about how we feel."
    else:
        mike.say "You look so good in those short skirts, Minami."
        mike.say "Sometimes I wish you'd wear them and nothing else!"
        show minami happy
        minami.say "I DO like the way I look in them, big bro."
        minami.say "Thanks for the compliment!"
    hide minami
    return

label minami_bad_sweet_talk_male:
    show minami
    mike.say "Wow, Minami - I can't believe you grew up to be so hot!"
    show minami scared
    minami.say "Eww, big bro!"
    minami.say "You think about how I was when we were kids?!?"
    minami.say "That's gross!"
    mike.say "No, Minami...that's not what I meant!"
    hide minami
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
