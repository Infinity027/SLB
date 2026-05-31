label jack_desire_0_female:
    jack.say "It's great that [mike.name] has you as a housemate, [hero.name]."
    jack.say "It means I have two cool people to hang-out with when I'm over here!"
    if jack.love < 30:
        bree.say "I don't know about that, Jack."
        bree.say "I think we already have enough nerds around here!"
    else:
        bree.say "I know what you mean, Jack."
        bree.say "It's nice to have someone else I can talk to."
    return

label jack_desire_1_female:
    jack.say "I'm glad we're getting the chance to hang-out together, [hero.name]."
    jack.say "I hope you think of me as more than just one of [mike.name]'s friends too!"
    if jack.love < 60:
        bree.say "I don't know, Jack."
        bree.say "I kind of like to pick and choose my own friends, you know?"
    else:
        bree.say "That makes two of us, Jack."
        bree.say "I really like getting to know more about you too."
    return

label jack_desire_2_female:
    jack.say "[hero.name]..."
    jack.say "Do you like [mike.name]?"
    jack.say "I...I mean...do you think he's handsome?"
    if jack.love < 90:
        bree.say "I guess so - if you like that kind of thing."
        bree.say "Don't tell him, but I think he's a little vain!"
        bree.say "Like he works out a likes the look of himself too much!"
    else:
        bree.say "Oh, sure I do, Jack!"
        bree.say "I mean, [mike.name]'s pretty good looking."
        bree.say "And he works out at the gym, so he's pretty ripped too!"
    return

label jack_desire_3_female:
    jack.say "I love getting the chance to just hang out with you, [hero.name]."
    jack.say "But...I feel like there's more to it than that, yeah?"
    jack.say "Like maybe we could be a little more than just friends?"
    if jack.love < 120:
        bree.say "Geez, Jack - way to ruin a perfectly good friendship!"
        bree.say "We were getting on just fine."
        bree.say "But you had to go and make it weird!"
    else:
        bree.say "I'm so glad you said that, Jack!"
        bree.say "I've been wanting to say the same thing too."
        bree.say "I just didn't know how to do it!"
    $ jack.love += 1
    return

label jack_desire_4_female:
    jack.say "Erm...[hero.name]...I just have to tell you this..."
    jack.say "You look REALLY good today!"
    jack.say "And you look pretty amazing the rest of the time too!"
    if jack.love < 150:
        bree.say "I try to make an effort, Jack."
        bree.say "You might want to think about doing that too!"
    else:
        bree.say "Thanks for the compliment, Jack!"
        bree.say "But do I look good enough that you want to touch me too?"
    $ jack.love += 1
    return

label jack_desire_5_female:
    jack.say "It's weird, [hero.name], but I can't think of going a day without seeing you!"
    jack.say "How crazy is that?"
    jack.say "You feel the same way, right?"
    if jack.love < 180:
        bree.say "Maybe you need to expand your social circle, Jack?"
        bree.say "They do say that absence makes the heart grow fonder!"
    else:
        bree.say "It's not crazy at all, Jack!"
        bree.say "I can't imagine not seeing you around here either!"
        bree.say "I mean...I don't want to go a day without seeing you!"
    $ jack.love += 1
    return

label jack_love_0_female:
    jack.say "Urgh!"
    jack.say "I had such a hard day at work..."
    jack.say "How about you, [hero.name]?"
    if jack.love < 30:
        bree.say "Wait a minute - you have a job?"
        bree.say "I thought you just bummed around other people's houses!"
    else:
        bree.say "Oh, don't worry about my day, Jack."
        bree.say "You sound like you need to vent."
        bree.say "So tell me all about your day!"
    $ jack.love += 1
    return

label jack_love_1_female:
    jack.say "Hey, [hero.name]."
    jack.say "How are you feeling today?"
    jack.say "Life treating you well?"
    if jack.love < 60:
        bree.say "Urgh..."
        bree.say "Enough with the bland platitudes, Jack!"
        bree.say "My life sucks enough already!"
    else:
        bree.say "Ah, I was feeling pretty lousy, Jack."
        bree.say "But seeing you had really cheered me up!"
    $ jack.love += 1
    return

label jack_love_2_female:
    jack.say "Wow - you're looking really great!"
    jack.say "Have you been working out more than usual?"
    if jack.love < 90:
        bree.say "What's that supposed to mean?"
        bree.say "That I look like a mess the rest of the time?!?"
    else:
        bree.say "Aw...thank you for saying so, Jack!"
        bree.say "I haven't - but maybe I should?"
        bree.say "Especially if it gets me such nice compliments!"
    $ jack.love += 1
    return

label jack_love_3_female:
    jack.say "Would you like to meet up for lunch tomorrow, [hero.name]?"
    jack.say "You know - just you and me?"
    jack.say "Kind of like a date - but not a date!"
    if jack.love < 120:
        bree.say "Is that really such a good idea, jack?"
        bree.say "I mean, you probably live in junk-food or something, right?"
        bree.say "And I'm trying to watch what I eat!"
    else:
        bree.say "You don't have to sound so nervous, Jack!"
        bree.say "That sounds great - I'd love to have lunch with you."
    $ jack.love += 1
    return

label jack_love_4_female:
    jack.say "I really want to see more of you, [hero.name]."
    jack.say "I...I mean...A LOT more..."
    jack.say "I feel like we're getting really close!"
    if jack.love < 150:
        bree.say "Really, jack?"
        bree.say "Well, maybe if you come round to hang-out with [mike.name] more?"
        bree.say "I mean, you'd see me then, right?"
    else:
        bree.say "Me too, jack."
        bree.say "And I don't mean with [mike.name] around either!"
        bree.say "We could get even closer..."
    $ jack.love += 1
    return

label jack_love_5_female:
    jack.say "Th...this...this is really hard for me to say, [hero.name]."
    jack.say "But...I think...I think I've fallen in love with you!"
    jack.say "Do you feel the same way about me?"
    if jack.love < 180:
        bree.say "I get it, Jack, really I do."
        bree.say "I mean, you're going to feel that way about me."
        bree.say "But you really think I feel the same way about you?!?"
    else:
        bree.say "Oh my god, Jack - are you serious?!?"
        bree.say "I feel the same way about you - I mean, I love you!"
        bree.say "I just didn't know how to say it!"
    $ jack.love += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
