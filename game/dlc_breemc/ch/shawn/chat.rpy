label shawn_desire_0_female:
    shawn.say "I'll confess something, [hero.name]..."
    shawn.say "I'm supposed to be over here to hang-out with [mike.name]."
    shawn.say "But I'm kind of using it as an excuse to see you too!"
    if shawn.love >= mike.love:
        bree.say "You're kidding, Shawn?"
        bree.say "That's pretty bad of you!"
        bree.say "But I kind like hearing it..."
        $ shawn.love += 1
    else:
        bree.say "That's an awful thing to admit, Shawn!"
        bree.say "[mike.name]'s your friend."
        bree.say "But it sounds like you're just using him to get to me!"
        $ shawn.sub += 1
    return

label shawn_desire_1_female:
    shawn.say "I'm getting a lot out of hanging-out with you, [hero.name]."
    shawn.say "I know we're both friends of [mike.name], which is cool."
    shawn.say "But we're becoming friends in our own right, yeah?"
    if shawn.love >= mike.love:
        bree.say "Of course we are, Shawn!"
        bree.say "And that friendship is really important to me."
        bree.say "[mike.name] or no [mike.name]!"
        $ shawn.love += 1
    else:
        bree.say "You're reading WAY too much into this, Shawn."
        bree.say "Sure, I like seeing you around the house."
        bree.say "But without [mike.name] there, it'd be super-awkward!"
        $ shawn.sub += 1
    return

label shawn_desire_2_female:
    shawn.say "[hero.name]..."
    shawn.say "Do you think [mike.name]'s a...well..."
    shawn.say "Do you think he's handsome, you know - good looking?"
    if shawn.love >= mike.love:
        bree.say "I know that [mike.name] thinks [mike.name]'s good looking!"
        bree.say "But to be honest, Shawn, he's not really my type."
        bree.say "I'm much more into blonde guys."
        $ shawn.love += 1
    else:
        bree.say "Yeah, Shawn!"
        bree.say "He's a real hottie!"
        bree.say "Don't you think?"
        $ shawn.sub += 1
    return

label shawn_desire_3_female:
    shawn.say "Hanging out with you is great, [hero.name]."
    shawn.say "But I feel like there's more to it, you know?"
    shawn.say "Like we're supposed to be more than just friends, yeah?"
    if shawn.love >= 100:
        bree.say "Wow..."
        bree.say "That's exactly how I feel, Shawn!"
        bree.say "How weird is that?"
        $ shawn.love += 1
    else:
        bree.say "I think you're getting confused, Shawn."
        bree.say "Sure, I like you and we're good friends."
        bree.say "But that doesn't mean I want anything more from you!"
        $ shawn.sub += 1
    return

label shawn_desire_4_female:
    shawn.say "I really like your outfit, [hero.name]."
    shawn.say "You always know just how to dress."
    shawn.say "And it never fails to turn my head!"
    if hero.charm >= 25:
        bree.say "I'm so glad you notice things like that, Shawn."
        bree.say "I try pretty hard to look good."
        bree.say "And you're one of the people I make the effort for too..."
        $ shawn.love += 1
    else:
        bree.say "Of course I try to dress well, Shawn."
        bree.say "Doesn't everyone?"
        bree.say "I'm not just trying to attract your attention, you know?"
        $ shawn.sub += 1
    return

label shawn_desire_5_female:
    shawn.say "I can't keep this to myself any more, [hero.name]."
    shawn.say "I want to spend more time with you, a LOT more time!"
    shawn.say "In fact, I want to be with you all the time!"
    if shawn.love >= 150:
        bree.say "You really mean that, Shawn?"
        bree.say "Oh wow, I wish you'd told me sooner."
        bree.say "Because I feel exactly the same way!"
        $ shawn.love += 1
    else:
        bree.say "Yeah well, you'll have to keep on wanting, Shawn."
        bree.say "Because I don't feel the same way about you!"
        bree.say "In fact, I could stand to spend a lot less time in your company..."
        $ shawn.sub += 1
    return

label shawn_love_0_female:
    shawn.say "Oh man!"
    shawn.say "Work was crazy today, [hero.name]!"
    shawn.say "Like super stressful, you know?"
    if shawn.love >= 25:
        bree.say "Oh no, Shawn!"
        bree.say "Sounds like you had a super tough day, huh?"
        bree.say "Want to tell me all about it?"
        $ shawn.love += 1
    else:
        bree.say "Don't be silly, Shawn."
        bree.say "[mike.name] told me about your job."
        bree.say "You basically work a counter and stack shelves!"
        $ shawn.sub += 1
    return

label shawn_love_1_female:
    shawn.say "I'm feeling pretty good today, [hero.name]."
    shawn.say "How about you?"
    shawn.say "Hope you're feeling the same way too!"
    if shawn.love >= 50:
        bree.say "It was turning out pretty meh, Shawn."
        bree.say "That was until you showed up!"
        $ shawn.love += 1
    else:
        bree.say "So you're having a great day."
        bree.say "And that means I have to be in a good mood too, huh?"
        bree.say "Urgh...get over yourself, Shawn!"
        $ shawn.sub += 1
    return

label shawn_love_2_female:
    shawn.say "I love the way you're looking today, [hero.name]."
    shawn.say "You're looking '[hero.name]liant'!"
    shawn.say "You get it?"
    if hero.fun >= 5:
        bree.say "Oh, Shawn..."
        bree.say "You're so corny!"
        bree.say "But you always make me laugh!"
        $ shawn.love += 1
    else:
        bree.say "Ouch..."
        bree.say "That was SO lame, Shawn."
        bree.say "Just like you!"
        $ shawn.sub += 1
    return

label shawn_love_3_female:
    shawn.say "We could go get some lunch, yeah?"
    shawn.say "Just you and me, [hero.name]."
    shawn.say "You know, like...if you wanted to?"
    if shawn.love >= 75:
        bree.say "Of course I want to, Shawn!"
        bree.say "That sounds like a great idea."
        bree.say "I can't wait!"
        $ shawn.love += 1
    else:
        bree.say "Nah, I think I'll pass, Shawn."
        bree.say "I'm on a pretty strict diet right now."
        bree.say "And you probably like want to eat junk-food or something, right?"
        $ shawn.sub += 1
    return

label shawn_love_4_female:
    shawn.say "I feel like we're getting really close, [hero.name]."
    shawn.say "Like we're good friends, but we're more than friends."
    shawn.say "You know what I mean, yeah?"
    if shawn.love >= 100:
        bree.say "I know exactly what you mean, Shawn!"
        bree.say "We're getting on so well, aren't we?"
        bree.say "I feel like we're already much more than just friends!"
        $ shawn.love += 1
    else:
        bree.say "Hmm..."
        bree.say "I think you're reading too much into this, Shawn."
        bree.say "Like, I like you - but not like that!"
        $ shawn.sub += 1
    return

label shawn_love_5_female:
    shawn.say "I...I think I have feelings for you, [hero.name]!"
    shawn.say "Like, I REALLY love you, with all my heart!"
    shawn.say "You feel the same way about me, right?"
    if shawn.love >= 150:
        bree.say "Yes, Shawn!"
        bree.say "One hundred percent yes!"
        bree.say "I wanted to say something, but I didn't know how."
        $ shawn.love += 1
    else:
        bree.say "Erm...no, Shawn."
        bree.say "I really like you, but not in that way."
        bree.say "Which makes this situation SO awkward..."
        $ shawn.sub += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
