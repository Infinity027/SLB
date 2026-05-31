label shiori_talk_love_female:
    bree.say "You've got so much more experience of love than I do, Shiori."
    bree.say "I mean, you've already been married and started a family."
    bree.say "All I've done is fool around with some short-term relationships!"
    if shiori.sub >= 50:
        shiori.say "Oh, I don't know about that..."
        shiori.say "I think that I have a lot to learn."
        shiori.say "If only someone were willing to teach me..."
    else:
        shiori.say "Oh, those are different things, [hero.name]."
        shiori.say "Believe me, you can be married to someone for what feels like forever."
        shiori.say "But that doesn't mean that they love you."
    $ shiori.sub += 1
    return

label shiori_talk_sex_female:
    bree.say "I'm so envious of your figure, Shiori!"
    bree.say "I'd need to have surgery to get a chest like yours!"
    bree.say "You must have fun in the bedroom, right?"
    if shiori.sub >= 50:
        shiori.say "Oh...thank you, [hero.name]!"
        shiori.say "Look, you're making me blush!"
        shiori.say "Would you like to know what else you're doing to me?"
        shiori.say "And where?"
    else:
        shiori.say "Oh, [hero.name] - you're so naughty!"
        shiori.say "I couldn't possibly tell you about that..."
        shiori.say "Well...maybe just a little!"
        shiori.say "And I do so enjoy it when I get to be intimate with someone I like in that way!"
    $ shiori.sub += 1
    return

label shiori_talk_politics_female:
    bree.say "I do my best to keep up with politics, Shiori."
    bree.say "But you must be more clued-up, right?"
    bree.say "I mean, you have a son - so even if it's just for his sake?"
    shiori.say "Oh goodness no, [hero.name]!"
    shiori.say "That's way too complicated for me to understand."
    shiori.say "I just used to leave that to my husband."
    shiori.say "He'd always tell me who to vote for."
    shiori.say "And now that he's gone, I just don't bother with it!"
    return

label shiori_talk_food_female:
    bree.say "Do you know any good recipes, Shiori?"
    bree.say "I imagine you like to cook for your son?"
    bree.say "I see you as that kind of mom."
    shiori.say "Not really, [hero.name]."
    shiori.say "I have so little time between my jobs!"
    shiori.say "Normally I open a can or stick something in the microwave."
    return

label shiori_talk_travels_female:
    bree.say "Sometimes I feel like I've never been further than the city limits."
    bree.say "How about you, Shiori?"
    bree.say "Have you ever been anywhere cool?"
    shiori.say "No, [hero.name], I haven't."
    shiori.say "I always wanted to, but life sort of got in the way."
    shiori.say "Maybe I will some time in the future."
    shiori.say "And it'll be like a dream come true!"
    $ shiori.love += 1
    return

label shiori_talk_tv_female:
    bree.say "Ooh, Shiori - before I forget!"
    bree.say "There's this great new anime that just started streaming."
    bree.say "Let me tell you the name, because I'm sure your son will love it!"
    shiori.say "[hero.name], I'm surprised at you!"
    shiori.say "Television rots your brain!"
    shiori.say "And Kanta should be spending his free time studying."
    shiori.say "Not watching garbage!"
    return

label shiori_talk_sports_female:
    bree.say "Shiori, are you into basket-ball?"
    bree.say "Because somebody at uni had some tickets going spare."
    bree.say "Nobody else is free, so I wondered if you wanted to come with me?"
    shiori.say "Oh no, [hero.name]!"
    shiori.say "No, no, no!"
    shiori.say "I hate sports and I don't like crowds either."
    shiori.say "You're so packed in and helpless - what if somebody touches my boobs?"
    return

label shiori_talk_fashion_female:
    bree.say "With a body like yours, Shiori, you must love summer!"
    bree.say "All those warm days and time at the beach."
    bree.say "Your curves must be on show twenty-four seven!"
    shiori.say "Oh no, [hero.name]!"
    shiori.say "I could never do that!"
    shiori.say "I don't want everybody looking at me."
    shiori.say "Just one person in particular..."
    return

label shiori_talk_books_female:
    bree.say "Read any good books lately, Shiori?"
    bree.say "I'm always on the lookout for a hot tip!"
    shiori.say "Erm...no, not really."
    shiori.say "I don't have time to read."
    shiori.say "You know, what with my family and my two jobs!"
    return

label shiori_talk_people_female:
    bree.say "I suppose you have to try to see the best in people."
    bree.say "Don't you think, Shiori?"
    bree.say "Otherwise it'd be all bleak and hopeless."
    if shiori.love >= 125:
        shiori.say "That's what I always say to Kanta, [hero.name]."
        shiori.say "I tell him to look for the good in people."
        shiori.say "Especially when it's hardest to find."
        $ shiori.love += 1
    else:
        shiori.say "On no, [hero.name] - some people are just bad through and through!"
        shiori.say "Like my ex-husband."
        shiori.say "There was nothing good about that man!"
        $ shiori.love -= 1
    return

label shiori_talk_computers_female:
    bree.say "You must spend a lot of time working with computers, Shiori."
    bree.say "Everyone that works in an office does, don't they?"
    bree.say "That's just how things are, right?"
    shiori.say "I don't think I'm an expert, [hero.name]!"
    shiori.say "The basics I can handle."
    shiori.say "But I'm always afraid that I'm going to break the one I have at work!"
    return

label shiori_talk_music_female:
    bree.say "What's your taste in music, Shiori?"
    bree.say "I like to ask people the question when I remember to."
    bree.say "Because it tells you a lot about them."
    shiori.say "Oh, I don't know, [hero.name]."
    shiori.say "I don't really have a taste in music."
    shiori.say "There's not much time for it in my life!"
    return

label shiori_talk_birthday_female:
    bree.say "I meant to say, Happy Birthday, Shiori!"
    bree.say "Hope you have a good one too!"
    shiori.say "Oh, [hero.name] - that's so kind of you to say!"
    shiori.say "But why would you remember my birthday?"
    shiori.say "I'm nobody important!"
    $ shiori.love += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
