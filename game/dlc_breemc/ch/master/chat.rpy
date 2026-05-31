label master_desire_0_female:
    master.say "We should be spending more time together, my dear."
    master.say "Not as master and pupil, but just as friends."
    master.say "That way our bond will only become stronger!"
    if master.love >= 25:
        bree.say "You really think that would help, master?"
        bree.say "If you do, then I'm all for it."
        $ master.love += 1
    else:
        bree.say "Hmm...I don't think that's a good idea."
        bree.say "I like to keep a clear barrier between the professional and the personal."
        $ master.sub += 1
    return

label master_desire_1_female:
    master.say "You're really growing in my estimation, my dear."
    master.say "In fact, I feel you are fast becoming more than a mere pupil to me."
    if master.love >= 50:
        bree.say "You really think so, master?"
        bree.say "That sounds like a really positive sign."
        bree.say "Maybe we should spend even more time together?"
        $ master.love += 1
    else:
        bree.say "Erm...I'm not sure how I feel about that."
        bree.say "Maybe we should have another chat about boundaries?"
        bree.say "You know, refresh your memory?"
        $ master.sub += 1
    return

label master_desire_2_female:
    master.say "My dear..."
    master.say "Are you easily taken in by the flower of youth?"
    master.say "Or do you look deeper, maybe for the sign of wisdom and experience?"
    if master.love >= 100:
        bree.say "Oh yes, master!"
        bree.say "I used to be seduced by such frivolous things."
        bree.say "But thanks to you, I now look deeper."
        $ master.love += 1
    else:
        bree.say "What's that supposed to mean, master?"
        bree.say "There's nothing wrong with liking a hottie!"
        bree.say "I mean...you like young girls, don't you?"
        $ master.sub += 1
    return

label master_desire_3_female:
    master.say "We've come a long way together, my dear."
    master.say "So much so that I feel like we are now more than simply master and pupil."
    master.say "Wouldn't you agree?"
    if master.love >= 100:
        bree.say "I do, master, I really do!"
        bree.say "Your teachings have changed who I am."
        bree.say "You're more like an inspiration to me than just a teacher!"
        $ master.love += 1
    else:
        bree.say "I don't know if I'd put it that way, master."
        bree.say "Sure, you're full of wisdom and all that."
        bree.say "But it's not like I need your advice for everything, is it?"
        $ master.sub += 1
    return

label master_desire_4_female:
    master.say "My dear, my dear!"
    master.say "My teachings are clearly having an effect on your physiology."
    master.say "Because your body is a breath-taking sight!"
    if hero.fitness >= 50:
        bree.say "Thank you for the compliment, master."
        bree.say "But none of it would have been possible without you."
        bree.say "Maybe that means I should offer you a reward?"
        $ master.love += 1
    else:
        bree.say "Hmm...it might have helped, a little."
        bree.say "But I like work out at the gym all the time, and I eat right too."
        bree.say "So you can't take all the credit."
        $ master.sub += 1
    return

label master_desire_5_female:
    master.say "My dear, you have become so much more than simply a pupil."
    master.say "You are my most devoted disciple, the vessel into which I pour myself."
    master.say "I must be with you always!"
    if hero.morality <= -25:
        bree.say "It makes me so happy to hear you say that, Master."
        bree.say "I can feel your wisdom growing inside of me."
        bree.say "And I'd like to feel something else growing in there too..."
        $ master.love += 1
    else:
        bree.say "Really?"
        bree.say "Like you don't have any other pupils apart from me?"
        bree.say "Because I'm thinking of expanding my horizons with a new teacher."
        $ master.sub += 1
    return

label master_love_0_female:
    master.say "Ah..."
    master.say "Being a master of the mystical arts is such a burden."
    master.say "Every day is a struggle for me!"
    if master.love >= 25:
        bree.say "Oh, master!"
        bree.say "I can only imagine the burdens you have to bear."
        bree.say "You want to unburden yourself by telling me all about it?"
        $ master.love += 1
    else:
        bree.say "Really, master?!?"
        bree.say "Because you don't seem to actually DO much."
        bree.say "You just spend your time perving around the beach!"
        $ master.sub += 1
    return

label master_love_1_female:
    master.say "Hello, my dear!"
    master.say "How does this day find my favourite pupil?"
    master.say "I hope it finds you well!"
    if hero.fun < 5:
        bree.say "My day was going badly until now, master."
        bree.say "But just seeing you has strengthened my resolve!"
        $ master.love += 1
    else:
        bree.say "It did until you came creeping up to me!"
        bree.say "Why don't you crawl back under a stone, yeah?"
        $ master.sub += 1
    return

label master_love_2_female:
    master.say "Hmm...you look exceptionally good today, my dear!"
    master.say "Have you been putting in extra time on the exercises I taught you?"
    master.say "Because that would certainly explain it."
    if hero.fitness >= 25:
        bree.say "Thank you for noticing, master!"
        bree.say "I always put in one hundred and ten percent effort."
        bree.say "Especially when it comes to your teachings!"
        $ master.love += 1
    else:
        bree.say "If anything, I've been easing off on your stuff, master."
        bree.say "Because it doesn't seem to be doing all that much."
        bree.say "I've had more results from just doing basic yoga!"
        $ master.sub += 1
    return

label master_love_3_female:
    master.say "We should get together tomorrow, my dear - over lunch."
    master.say "Nutrition is of the upmost importance."
    master.say "And I'd like to watch you eat...I mean watch WHAT you eat!"
    if master.love >= 100:
        bree.say "That sounds like a very good idea, master."
        bree.say "Plus it'd be nice to spend more time together."
        bree.say "Wouldn't it?"
        $ master.love += 1
    else:
        bree.say "I don't think I want to do that, master."
        bree.say "Eating with you would probably upset my digestion."
        bree.say "And just the thought of it is spoiling my appetite..."
        $ master.sub += 1
    return

label master_love_4_female:
    master.say "The time has come for us to spend more time together, my dear."
    master.say "Your studies have progressed to the point where it is necessary."
    master.say "We will need to become closer than ever in order for you to reach the next level!"
    if master.love >= 125:
        bree.say "I totally understand, master."
        bree.say "And I'm willing to do whatever is needed."
        bree.say "Even if it means being with you twenty-four seven!"
        $ master.love += 1
    else:
        bree.say "I don't think so, master."
        bree.say "In fact I think there's nothing more I can learn from you."
        bree.say "Maybe it's even time for me to find a new master..."
        $ master.sub += 1
    return

label master_love_5_female:
    master.say "I feel the need to be honest with you, my dear."
    master.say "You have become more than just a pupil to me, much more."
    master.say "In fact, I have come to love you in a very real, very physical sense!"
    if master.love >= 150:
        bree.say "Oh, master!"
        bree.say "You've taught me so much already."
        bree.say "But the greatest lesson of all was teaching me to love you!"
        $ master.love += 1
    else:
        bree.say "Erm...this is kind of awkward!"
        bree.say "I feel like you're reading my signals all wrong."
        bree.say "Because I am NOT interested in you like that - not at all!"
        $ master.sub += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
