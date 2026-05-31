label aletta_talk_love_female:
    show aletta
    bree.say "You seem like a real career woman, Aletta."
    bree.say "But you still find time for other stuff, right?"
    bree.say "Important stuff like love?"
    if aletta.is_visibly_pregnant:
        aletta.say "Of course I do, [hero.name]!"
        aletta.say "How else would I have found the time to have a baby?"
        $ aletta.love += 2
    else:
        aletta.say "Of course I do, [hero.name]!"
        aletta.say "And I'm as serious about it as I am my career!"
        $ aletta.love += 1
    hide aletta
    return

label aletta_talk_sex_female:
    show aletta
    bree.say "You always seem to get what you want, Aletta."
    bree.say "Does that include....well...sex?"
    if aletta.love < 120:
        aletta.say "Oh dear, [hero.name]!"
        aletta.say "You're so obvious."
        aletta.say "I could never open up to you about something that intimate!"
        $ aletta.love -= 1
    else:
        aletta.say "How sweet of you to ask, [hero.name]!"
        aletta.say "And yes - I ALWAYS get what I want."
        aletta.say "Especially when it comes to sex!"
        $ aletta.love += 1
    hide aletta
    return

label aletta_talk_politics_female:
    show aletta
    bree.say "Politics always confuses me, Aletta."
    bree.say "It's just people shouting at each other all the time!"
    bree.say "It's so confusing."
    if aletta.love >= 100:
        aletta.say "Oh dear, [hero.name]!"
        aletta.say "Is it too much for your sweet little head to understand?"
        aletta.say "Don't worry, a little discipline might help you to grasp it..."
        $ aletta.sub -= 1
    else:
        aletta.say "Ignorance is no excuse, [hero.name]!"
        aletta.say "This is the twenty-first century."
        aletta.say "A woman should educate herself!"
        $ aletta.love -= 1
    hide aletta
    return

label aletta_talk_food_female:
    show aletta
    bree.say "Ooh, I can smell something good cooking somewhere around here!"
    bree.say "Doesn't it make your mouth water, Aletta?"
    aletta.say "Hmm..."
    if aletta.love >= 100:
        $ aletta.love += 1
    aletta.say "Food is fuel, [hero.name]."
    aletta.say "You shouldn't let it take control of you like that!"
    hide aletta
    return

label aletta_talk_travels_female:
    show aletta
    bree.say "Urgh..."
    bree.say "I never seem to go anywhere, Aletta!"
    bree.say "I wish I could just jet off somewhere - see the world!"
    $ aletta.love += 1
    aletta.say "I know just what you mean, [hero.name]."
    aletta.say "Travel broadens the mind, makes you a better person."
    aletta.say "The one thing I hate about my career is not having more paid vacation time!"
    hide aletta
    return

label aletta_talk_tv_female:
    show aletta
    bree.say "I can't wait to get home tonight, Aletta."
    bree.say "I'm gonna binge the entire new series of the 'Weirder Shit'!"
    bree.say "Everyone's raving about it on social media!"
    aletta.say "I can honestly say that I've never heard of it."
    if aletta.love >= 100:
        $ aletta.love += 1
    aletta.say "Television is just chewing-gum for the eyes!"
    hide aletta
    return

label aletta_talk_sports_female:
    show aletta
    bree.say "I don't get sports, Aletta."
    bree.say "And I don't get why people are so crazy about them either!"
    bree.say "Unless it's E-Sports - now that I DO understand!"
    aletta.say "Hmm..."
    aletta.say "I certainly disapprove of the loutish behaviour."
    aletta.say "But I do appreciate the effort involved on the part of the athletes."
    aletta.say "Maybe if you focused on that you'd get it?"
    hide aletta
    return

label aletta_talk_fashion_female:
    show aletta
    bree.say "I'm not up to speed on power-dressing, Aletta."
    bree.say "But I guess you've got to be clued-up in your position?"
    aletta.say "Oh dear, [hero.name] - it's not all shoulder-pads and stuff like that!"
    aletta.say "But yes, it does pay off to know how to dress in the office."
    aletta.say "I must give you the basics some time soon!"
    hide aletta
    return

label aletta_talk_books_female:
    show aletta
    bree.say "I always feel like I should read more, Aletta."
    bree.say "But there's just so much good stuff on TV."
    bree.say "And so many cool new games I want to play too!"
    bree.say "I can never find the time."
    if aletta.love >= 100:
        $ aletta.sub -= 1
    aletta.say "Well you never will while you keep making excuses, [hero.name]!"
    aletta.say "And you should be feeding your head."
    aletta.say "Not just indulging yourself with that kind of junk all the time!"
    hide aletta
    return

label aletta_talk_people_female:
    show aletta
    bree.say "People are always saying I'm anti-social."
    bree.say "But I don't think that I am, Aletta."
    bree.say "I think it's more that I'm not user-friendly!"
    if aletta.love >= 100:
        $ aletta.sub -= 1
    aletta.say "You don't owe anybody anything, [hero.name]."
    aletta.say "If somebody doesn't appreciate you, that's their problem - not yours!"
    hide aletta
    return

label aletta_talk_computers_female:
    show aletta
    bree.say "You're a wizard when it comes to computers, right, Aletta?"
    bree.say "I mean, you have to be to be good at your job, don't you?"
    if aletta.love >= 100:
        $ aletta.love -= 1
    aletta.say "Hmm..."
    aletta.say "I see computers as a tool, [hero.name]."
    aletta.say "A necessary tool, but still no more than a tool."
    aletta.say "You can't do every job with just one tool."
    hide aletta
    return

label aletta_talk_music_female:
    show aletta
    bree.say "Do you have time to listen to music, Aletta?"
    bree.say "You always seem so busy!"
    bree.say "Do you even have time?"
    aletta.say "I'll let you into a little secret, [hero.name]..."
    aletta.say "I sometimes wear REALLY discreet ear-pods in the office!"
    aletta.say "But don't tell anyone - it'd ruin my image."
    hide aletta
    return

label aletta_talk_birthday_female:
    show aletta
    bree.say "Happy birthday Aletta."
    aletta.say "Thank you [hero.name]."
    $ aletta.love += 1
    hide aletta
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
