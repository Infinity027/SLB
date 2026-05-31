label lexi_desire_0_female:
    lexi.say "I should spend more time over here, [hero.name]."
    lexi.say "Everyone's pretty laid back and cool."
    if lexi.love >= 50:
        bree.say "They're not always so chilled, Lexi."
        bree.say "But you are - so you're always welcome around here!"
        $ lexi.love += 1
    else:
        bree.say "Urgh...that's the last thing I need."
        bree.say "Another person getting under my feet!"
        $ lexi.sub += 1
    return

label lexi_desire_1_female:
    lexi.say "Hey, [hero.name]..."
    lexi.say "You wanna come hang out?"
    lexi.say "Like, just you and me?"
    if lexi.love >= 50:
        bree.say "Why not, Lexi."
        bree.say "We've been getting on pretty well, haven't we?"
        bree.say "Spending more time with you sounds like fun!"
        $ lexi.love += 1
    else:
        bree.say "Hmm...maybe not, Lexi."
        bree.say "I kinda feel like we work when we're part of a group."
        bree.say "But when it's just us...I'm not feeling it."
        $ lexi.sub += 1
    return

label lexi_desire_2_female:
    lexi.say "[hero.name]..."
    lexi.say "Do you like just guys?"
    lexi.say "Or do you like girls as well?"
    lexi.say "You know...like in that special kind of way?"
    if lexi.love >= 75:
        bree.say "I can go either way, Lexi."
        bree.say "But the girl has to be really special."
        bree.say "She has to be special for me to even tell her that!"
        $ lexi.love += 1
    else:
        bree.say "Whoa!"
        bree.say "That's a pretty personal question, Lexi."
        bree.say "How about you keep your nose out of my business, okay?"
        $ lexi.sub += 1
    return

label lexi_desire_3_female:
    lexi.say "I got a confession to make, [hero.name]..."
    lexi.say "Sasha and [mike.name] are pretty cool, you know."
    lexi.say "But I kinda like you better than them!"
    if lexi.love >= mike.love and lexi.love >= sasha.love:
        bree.say "Don't let them hear about this, Lexi..."
        bree.say "But I know what you mean!"
        bree.say "You're WAY more fun than those guys!"
        $ lexi.love += 1
    else:
        bree.say "You know what's not cool, Lexi?"
        bree.say "Talking about people behind their backs!"
        bree.say "Wait until [mike.name] and Sasha hear about this..."
        $ lexi.sub += 1
    return

label lexi_desire_4_female:
    lexi.say "Mmm...[hero.name]!"
    lexi.say "Your tits and ass look amazing in that!"
    lexi.say "You could make a fortune on a street corner..."
    if hero.morality <= -25:
        bree.say "Lexi...I...I don't know what to say!"
        bree.say "That's such a wicked thing to suggest."
        bree.say "But I kind of like it..."
        $ lexi.love += 1
    else:
        bree.say "So you're saying that look like a prostitute?"
        bree.say "That's about the size of it, right?"
        bree.say "Disgusting!"
        $ lexi.sub += 1
    return

label lexi_desire_5_female:
    lexi.say "I...I keep coming up with excuses to see you, [hero.name]."
    lexi.say "It's weird...but I can't stop thinking about you too!"
    lexi.say "If I'm not with you, then you're always on my mind."
    if lexi.love >= 100:
        bree.say "If it's weird, Lexi, then we're both weird!"
        bree.say "Because I've been feeling the same way too."
        bree.say "I think we might be turning into more than just friends!"
        $ lexi.love += 1
    else:
        bree.say "Yeah, Lexi...that is pretty weird."
        bree.say "Maybe you should try to think about other stuff?"
        bree.say "Or at least think about other people..."
        $ lexi.sub += 1
    return

label lexi_love_0_female:
    lexi.say "WOW...!"
    lexi.say "Today was really tough, [hero.name]."
    lexi.say "Work kind of beat me up!"
    if game.flags.hasworked and lexi.love >= 75:
        bree.say "My day was pretty hard too, Lexi."
        bree.say "You wanna tell me all about it?"
        bree.say "I find talking it through often helps."
        $ lexi.love += 1
    else:
        bree.say "Erm...aren't you some kind of prostitute, Lexi?"
        bree.say "Hard to see how you can be so tired."
        bree.say "Don't you do most of your work lying down?"
        $ lexi.sub += 1
    return

label lexi_love_1_female:
    lexi.say "Hey, [hero.name]!"
    lexi.say "You look pretty down in the dumps!"
    lexi.say "Who's been upsetting you?"
    if hero.fun >= 5:
        bree.say "Ah, it's nothing, Lexi."
        bree.say "But thanks for asking."
        bree.say "It's nice to know that you care."
        $ lexi.love += 1
    else:
        bree.say "Oh what do you care, Lexi?"
        bree.say "I mean, we hardly know each other."
        bree.say "So who are you trying to kid?"
        $ lexi.sub += 1
    return

label lexi_love_2_female:
    lexi.say "Hey, [hero.name]...we are looking SERIOUSLY sexy today!"
    lexi.say "That outfit makes everything about you pop."
    lexi.say "I gotta get me some fashion tips from you, girl!"
    if hero.charm >= 20:
        bree.say "You...you really think so, Lexi?"
        bree.say "Thanks!"
        bree.say "I wish I had the confidence to dress like you."
        bree.say "You always look so...well...so sexy!"
        $ lexi.love += 1
    else:
        bree.say "You mean I look like a hooker?"
        bree.say "I knew this outfit was a mistake!"
        bree.say "I should go change before I get propositioned..."
        $ lexi.sub += 1
    return

label lexi_love_3_female:
    lexi.say "Let's go grab a drink, [hero.name]!"
    lexi.say "Just you and me - screw the others."
    lexi.say "It'll be more fun that way!"
    if lexi.love >= mike.love and lexi.love >= sasha.love:
        bree.say "Oh yeah, Lexi!"
        bree.say "Let's go right now, okay?"
        bree.say "Before [mike.name] and Sasha figure it out!"
        $ lexi.love += 1
    else:
        bree.say "Nah...I'll pass, Lexi."
        bree.say "I'd feel like I was going behind their backs."
        bree.say "And you're turning into a bad influence..."
        $ lexi.sub += 1
    return

label lexi_love_4_female:
    lexi.say "We need to hang out together whenever we can, [hero.name]."
    lexi.say "I feel like we connect on a whole different level."
    lexi.say "Like we're becoming more than friends, yeah?"
    if lexi.love >= 75:
        bree.say "That's so weird, Lexi!"
        bree.say "I feel just like that too."
        bree.say "And I was about to say the same thing!"
        $ lexi.love += 1
    else:
        bree.say "I'm not so sure, Lexi."
        bree.say "I kind of more feel like we're a package."
        bree.say "Like you can't have me without [mike.name] and Sasha."
        $ lexi.sub += 1
    return

label lexi_love_5_female:
    lexi.say "I don't normally admit this kind of thing, [hero.name]."
    lexi.say "But...I kind of have feelings for you."
    lexi.say "You know...like romantic feelings?"
    if lexi.love >= 100:
        bree.say "I'm SO glad you said that, Lexi!"
        bree.say "I feel like I'm falling in love with you too!"
        bree.say "Hearing you say that is such a relief."
        $ lexi.love += 1
    else:
        bree.say "I can see why you wouldn't admit that, Lexi."
        bree.say "It's kind of dangerous to open yourself up."
        bree.say "Especially when the other person might not feel the same way!"
        bree.say "Which I don't, by the way..."
        $ lexi.sub += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
