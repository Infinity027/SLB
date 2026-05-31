label ayesha_desire_0_female:
    ayesha.say "Would...would you mind if I came over here more often, [hero.name]?"
    ayesha.say "It's kind of nice, with a casual vibe, you know?"
    if ayesha.love >= 50:
        bree.say "Sure thing, Ayesha."
        bree.say "It's always nice to have new faces around the place."
        bree.say "And someone new to talk to."
        $ ayesha.love += 1
    else:
        bree.say "Do you have to be around here so much, Ayesha?"
        bree.say "It's pretty crowded with the three of us already."
        bree.say "And you kind of take up a lot of space, you know?"
        $ ayesha.sub += 1
    return

label ayesha_desire_1_female:
    ayesha.say "I really like it when we get the chance to talk, [hero.name]."
    ayesha.say "I mean, [mike.name] and Sasha are great too."
    ayesha.say "But I feel like we kind of connect more?"
    if ayesha.love >= mike.love and ayesha.love >= sasha.love:
        bree.say "I hear you, Ayesha."
        bree.say "I enjoy talking with you too."
        bree.say "You're pretty smart."
        bree.say "And pretty pretty too!"
        $ ayesha.love += 1
    else:
        bree.say "Hmm...maybe, Ayesha."
        bree.say "But why do you always want to talk about boring stuff?"
        bree.say "Like books and things - SO boring!"
        $ ayesha.sub += 1
    return

label ayesha_desire_2_female:
    ayesha.say "[hero.name]..."
    ayesha.say "Do you like Sasha?"
    ayesha.say "Oh my...that didn't come out sounding right!"
    ayesha.say "I mean...do you think she's...well...pretty?"
    if ayesha.love >= sasha.love:
        bree.say "Eww, no way, Ayesha!"
        bree.say "I'm not into the whole rock chick thing!"
        bree.say "I much prefer girls that are active."
        bree.say "You know, kind of physically fit?"
        $ ayesha.love += 1
    else:
        bree.say "Oh, sure I do, Ayesha!"
        bree.say "I just love the whole dark vibe she's got going on too!"
        bree.say "Rather that than some kind of sporty girl jock thing..."
        $ ayesha.sub += 1
    return

label ayesha_desire_3_female:
    ayesha.say "You want me to come over and just hang out, [hero.name]?"
    ayesha.say "I really liked it the last time we got to do that."
    ayesha.say "And I was wondering if you wanted to do it again?"
    if ayesha.love >= 50:
        bree.say "That sounds great, Ayesha!"
        bree.say "I had a great time too."
        bree.say "I was hoping we could do just that."
        $ ayesha.love += 1
    else:
        bree.say "Really, Ayesha?"
        bree.say "Because that's not how I remember it at all!"
        bree.say "I was bored senseless the whole time."
        $ ayesha.sub += 1
    return

label ayesha_desire_4_female:
    ayesha.say "I love the way you dress, [hero.name]."
    ayesha.say "It's like you know just what to pick every day."
    ayesha.say "I guess you know your own style, right?"
    if hero.charm >= 20:
        bree.say "Thanks for the compliment, Ayesha!"
        bree.say "But I like the way you dress too."
        bree.say "And the way things look on that amazing figure of yours!"
        bree.say "Wow, just, wow!"
        $ ayesha.love += 1
    else:
        bree.say "I try to make an effort, Ayesha."
        bree.say "But it must be so hard for you."
        bree.say "Do you like, have to buy men's clothes or something?"
        $ ayesha.sub += 1
    return

label ayesha_desire_5_female:
    ayesha.say "I feel like I've grown really close to you, [hero.name]."
    ayesha.say "When we're apart, you're often all I can think about."
    ayesha.say "That and when I can get to see you next!"
    if ayesha.love >= 75:
        bree.say "Oh god, Ayesha - that's so weird!"
        bree.say "I've been feeling the same way too."
        bree.say "There must be something behind it."
        $ ayesha.love += 1
    else:
        bree.say "Eww...that's kind of creepy, Ayesha!"
        bree.say "So you're like what, stalking me or something?"
        $ ayesha.sub += 1
    return

label ayesha_love_0_female:
    ayesha.say "Urgh!"
    ayesha.say "I covered somebody else's classes at the gym today."
    ayesha.say "And on top of my own, they really kicked my ass!"
    if ayesha.love >= 50:
        bree.say "Ouch!"
        bree.say "I don't know how you do it, Ayesha."
        bree.say "You're like a dynamo or something."
        $ ayesha.love += 1
    else:
        bree.say "Seriously, Ayesha - how hard can it be?"
        bree.say "Don't you just mess around in lycra all day?"
        $ ayesha.sub += 1
    return

label ayesha_love_1_female:
    ayesha.say "Hey, [hero.name]."
    ayesha.say "Are you keeping well today?"
    ayesha.say "I'm feeling pretty good myself!"
    if hero.fun >= 5:
        bree.say "Ah, I was feeling pretty lousy, Ayesha."
        bree.say "But you're just so positive today."
        bree.say "In feel like you're picking me up too!"
        $ ayesha.love += 1
    else:
        bree.say "Urgh..."
        bree.say "Enough with the bland motivational speeches, Ayesha."
        bree.say "I'm not in the mood."
        $ ayesha.sub += 1
    return

label ayesha_love_2_female:
    ayesha.say "[hero.name], you're looking so healthy - you're practically glowing!"
    ayesha.say "But I haven't seen you down the gym that much."
    ayesha.say "Have you been working out behind my back?"
    if hero.fitness >= 20:
        bree.say "No, Ayesha...I swear I haven't."
        bree.say "But maybe I should?"
        bree.say "You seem to think I look pretty fit."
        $ ayesha.love += 1
    else:
        bree.say "Wait a minute, Ayesha..."
        bree.say "Are you trying to sign me up for more classes at the gym?"
        bree.say "Do you get some kind of bonus for that?"
        $ ayesha.sub += 1
    return

label ayesha_love_3_female:
    ayesha.say "Would you like to meet up for lunch tomorrow, [hero.name]?"
    ayesha.say "Just the two of us, maybe?"
    ayesha.say "Kind of like a date and not a date!"
    if ayesha.love >= 50:
        bree.say "That sounds like a great idea."
        bree.say "I've been meaning to ask you for some healthy eating tips, Ayesha."
        bree.say "Plus it'd be nice to have some time together too."
        $ ayesha.love += 1
    else:
        bree.say "Is that really such a good idea, Ayesha?"
        bree.say "I mean, you probably disapprove of the stuff I like to eat, right?"
        bree.say "And I don't want lunch to turn into a lecture."
        $ ayesha.sub += 1
    return

label ayesha_love_4_female:
    ayesha.say "I have to be honest, [hero.name]."
    ayesha.say "I want to see more of you - a lot more of you."
    ayesha.say "Just the two of us, if you know what I mean?"
    if ayesha.love >= 75:
        bree.say "I think I do, Ayesha."
        bree.say "And I'd like that very much."
        bree.say "It'd give us a chance to get even closer..."
    else:
        bree.say "Really, Ayesha?"
        bree.say "I'd kind of feel uncomfortable with that."
        bree.say "In fact, I think you need to back off a little."
        $ ayesha.sub += 1
    return

label ayesha_love_5_female:
    ayesha.say "This is really hard for me to say, [hero.name]."
    ayesha.say "But I can't hide it any longer."
    ayesha.say "I think I've fallen in love with you!"
    ayesha.say "Do you feel the same way about me?"
    if ayesha.love >= 100:
        bree.say "Oh my god, Ayesha - are you serious?!?"
        bree.say "I feel the same way about you - I mean, I love you!"
        bree.say "I just didn't know how to say it!"
        $ ayesha.love += 1
    else:
        bree.say "I get it, Ayesha, really I do."
        bree.say "I mean, you're obviously going to feel that way about me."
        bree.say "But how could you even think that I'd feel the same way about you?"
        bree.say "It's just never going to happen!"
        $ ayesha.sub += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
