label dwayne_desire_0_female:
    dwayne.say "Your pad's pretty nice, [hero.name]."
    dwayne.say "I mean sure, it's kind of quaint."
    dwayne.say "But I like visiting you here."
    if dwayne.love >= 50:
        bree.say "It works for me, Dwayne!"
        bree.say "But I guess you're used to penthouse apartments, huh?"
        bree.say "I'm more of a homebody!"
        $ dwayne.love += 1
    else:
        bree.say "You can just come out and say that it's small, Dwayne."
        bree.say "You're not going to score any points with me for slumming it!"
        $ dwayne.sub += 1
    return

label dwayne_desire_1_female:
    dwayne.say "I should thank [mike.name] for introducing us, [hero.name]."
    dwayne.say "It's been a real blast getting to know you!"
    dwayne.say "So should I just thank him, or does he deserve a bonus?"
    if dwayne.love >= mike.love:
        bree.say "I'd say he deserves that bonus, Dwayne."
        bree.say "Because he did good when he hooked us up!"
        $ dwayne.love += 1
    else:
        bree.say "Geez, Dwayne - just tell [mike.name] he did good."
        bree.say "You don't have to throw money at everything!"
        $ dwayne.sub += 1
    return

label dwayne_desire_2_female:
    dwayne.say "I overheard some of the girls at the office talking about [mike.name] the other day."
    dwayne.say "And you know what - one of them actually said that he was good-looking!"
    dwayne.say "Which is strange, because he always looked kind of gawky and weird to me."
    if dwayne.love >= mike.love:
        bree.say "Hmm..."
        bree.say "I guess he's kind of cute, in a geeky sort of way."
        bree.say "But I prefer a more manly kind of man - like you!"
        $ dwayne.love += 1
    else:
        bree.say "Maybe they like a more sensitive kind of guy?"
        bree.say "You know what I mean, Dwayne?"
        bree.say "The kind that doesn't have to rely on flashing his money around?"
        $ dwayne.sub += 1
    return

label dwayne_desire_3_female:
    dwayne.say "You feel it too, right, [hero.name]?"
    dwayne.say "That spark that we have between us?"
    dwayne.say "It's there whenever we're spending time together!"
    if dwayne.love >= 75:
        bree.say "I kinda do, Dwayne."
        bree.say "It's like we're not just hanging out."
        bree.say "Like we're actually connecting on another level."
        $ dwayne.love += 1
    else:
        bree.say "Yeah...whatever it is you're talking about, I'm not feeling it!"
        bree.say "I think you're reading WAY more into this than is really there, Dwayne."
        $ dwayne.sub += 1
    return

label dwayne_desire_4_female:
    dwayne.say "Mmm..."
    dwayne.say "You are really wearing that outfit, [hero.name]!"
    dwayne.say "I don't know how you do it."
    dwayne.say "But you always look damn good!"
    if hero.charm >= 20:
        bree.say "Oh...thank you, Dwayne!"
        bree.say "I always try extra hard for you."
        bree.say "Because I know that you appreciate it!"
        $ dwayne.love += 1
    else:
        bree.say "I have to put in the work to look this good, Dwayne."
        bree.say "Some of us don't have the money to just buy their look."
        bree.say "But you can always spot someone that does..."
        $ dwayne.sub += 1
    return

label dwayne_desire_5_female:
    dwayne.say "I can't hide my feelings any longer, [hero.name]."
    dwayne.say "I have to have you in my life."
    dwayne.say "And I want to have you by my side every single day!"
    if dwayne.love >= 100:
        bree.say "I feel the same way, Dwayne!"
        bree.say "I want to be on your arm wherever you go!"
        bree.say "Promise me that's how it's going to be?"
        $ dwayne.love += 1
    else:
        bree.say "Urgh..."
        bree.say "I'm not for sale, Dwayne!"
        bree.say "And no amount of money is going to buy me!"
        $ dwayne.sub += 1
    return

label dwayne_love_0_female:
    dwayne.say "Phew..."
    dwayne.say "Another day steering the ship of corporate enterprise!"
    dwayne.say "A job like mine requires constant effort and endless stamina, [hero.name]!"
    if dwayne.love >= 50:
        bree.say "I have no idea how you run such a big company, Dwayne."
        bree.say "You must have so many people to worry about."
        bree.say "Let's talk about something else to get your mind of it, okay?"
        $ dwayne.love += 1
    else:
        bree.say "What do you want me to do, Dwayne - organise a parade for you?"
        bree.say "It's not like you're forced to do the job you do, is it?"
        bree.say "And I'm sure the huge amount of money you make is some comfort!"
        $ dwayne.sub += 1
    return

label dwayne_love_1_female:
    dwayne.say "Hey there, [hero.name]!"
    dwayne.say "How's my favourite girl doing today?"
    dwayne.say "Apart from looking as good as ever?"
    if hero.fun >= 5:
        bree.say "Oh...thank you, Dwayne!"
        bree.say "I was feeling pretty down in the dumps."
        bree.say "But you just cheered me up!"
        $ dwayne.love += 1
    else:
        bree.say "Oh give me a break, Dwayne."
        bree.say "Like you really care what I think or feel!"
        bree.say "You're just flattering me to make yourself look good."
        $ dwayne.sub += 1
    return

label dwayne_love_2_female:
    dwayne.say "[hero.name]...[hero.name]...[hero.name]..."
    dwayne.say "You are looking SO good today!"
    dwayne.say "I don't know where to start telling you how good you look!"
    if dwayne.love >= 75:
        bree.say "I...well...I..."
        bree.say "Oh hell...I'm blushing!"
        bree.say "Look what you made me do!"
        $ dwayne.love += 1
    else:
        bree.say "Erm...didn't you already do that, Dwayne?"
        bree.say "Urgh...your lines are so corny."
        bree.say "Like they're out of a book or something!"
        $ dwayne.sub += 1
    return

label dwayne_love_3_female:
    dwayne.say "We should do lunch tomorrow, [hero.name]."
    dwayne.say "Just you and me in some place really nice."
    dwayne.say "Kind of intimate, but not too formal, yeah?"
    if dwayne.love >= 75:
        bree.say "So long as it's just the two of us, Dwayne."
        bree.say "I'd love the chance to get to know you a little better."
        bree.say "If you know what I mean..."
        $ dwayne.love += 1
    else:
        bree.say "Nah...I don't think that'd work, Dwayne."
        bree.say "You probably wanna eat in some fancy place."
        bree.say "And all I want for lunch is a peanut butter and jelly sandwich!"
        $ dwayne.sub += 1
    return

label dwayne_love_4_female:
    dwayne.say "We've become really close these past few weeks, [hero.name]."
    dwayne.say "All the time we've spent together has been very meaningful for me."
    dwayne.say "And I feel like we should make a serious commitment to each other."
    if dwayne.love >= 75:
        bree.say "I was hoping you'd say that, Dwayne."
        bree.say "Because I feel the same way too."
        bree.say "I want to get seriously serious with you!"
        $ dwayne.love += 1
    else:
        bree.say "Is that the way you talk when you're trying to seal a business deal, Dwayne?"
        bree.say "Because to me, it just sounds so fake and false!"
        bree.say "Like, you REALLY can't read the room, can you?"
        $ dwayne.sub += 1
    return

label dwayne_love_5_female:
    dwayne.say "It's never easy for a man of my status to be this honest, [hero.name]."
    dwayne.say "But I feel that, with you, I have no other choice."
    dwayne.say "I'm in love with you, [hero.name], totally and hopelessly!"
    if dwayne.love >= 100:
        bree.say "Wow...that's amazing, Dwayne!"
        bree.say "Because I feel the same way about you too."
        bree.say "I love you like crazy!"
        $ dwayne.love += 1
    else:
        bree.say "Ooh...this is kind of awkward!"
        bree.say "Because I'm just not feeling it, Dwayne."
        bree.say "I mean, you're a nice guy and all that."
        bree.say "But I don't feel the same way about you."
        $ dwayne.sub += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
