label sasha_talk_love_female:
    bree.say "People are so cynical these days, Sasha."
    bree.say "It's like they don't believe in true love!"
    bree.say "But deep down, they have to, right?"
    if sasha.love > 80 - hero.charm/2:
        sasha.say "That's so true, [hero.name]!"
        sasha.say "I know that I'm desperate for somebody to love me!"
        sasha.say "Someone to tell me how to live my life too!"
        $ sasha.sub += 1
    else:
        sasha.say "I don't know about true love like in a fairy tale, [hero.name]!"
        sasha.say "But I for sure think that love's a real thing."
        sasha.say "You just have to put in the effort to find it."
        sasha.say "That and be able to take the hit when you don't..."
    $ sasha.love += 1
    return

label sasha_talk_sex_female:
    bree.say "I hate when people are so uptight about sex, Sasha!"
    bree.say "I mean, who are they even trying to kid?"
    bree.say "Everyone's got sex on the brain all the time!"
    if sasha.love > 80 - hero.charm/2:
        sasha.say "People should be more honest, [hero.name]!"
        sasha.say "It makes life much more simple."
        sasha.say "Like in my case - I could never hide the fact that I want sex!"
        sasha.say "I'm far too good of a girl to do something like that!"
        $ sasha.sub += 1
    else:
        sasha.say "People are just uptight and repressed, [hero.name]!"
        sasha.say "They think they have to say they're not obsessed with fucking!"
        sasha.say "We both know that's bullshit."
        sasha.say "Everyone's thinking about sex all the time!"
        $ sasha.love += 1
    return

label sasha_talk_politics_female:
    bree.say "Ooh...did you remember to vote already, Sasha?"
    bree.say "You don't want to leave it too late."
    bree.say "The polling station will be closed soon!"
    sasha.say "Ahh...why'd you have to go and bring up politics, [hero.name]?"
    sasha.say "Just thinking about all those lying scumbags makes me sick!"
    sasha.say "I'm not turning out to vote for any of them!"
    $ sasha.love -= 1
    return

label sasha_talk_food_female:
    bree.say "Hmm...my stomach's starting to rumble!"
    bree.say "I really should think about getting some food..."
    bree.say "Sasha, are you hungry too?"
    sasha.say "Of course I am, [hero.name]!"
    sasha.say "I'm always hungry!"
    sasha.say "Thanks for thinking about me too."
    $ sasha.love += 1
    return

label sasha_talk_travels_female:
    bree.say "It sucks being stuck in a job like mine, Sasha."
    bree.say "I don't want to take a holiday at home, mooching around the house."
    bree.say "I wanna go somewhere exotic and exciting!"
    sasha.say "I hear you, [hero.name]!"
    sasha.say "We're in the same boat."
    sasha.say "Dreaming about tropical beaches with our feet in a bucket of water!"
    $ sasha.love += 2
    return

label sasha_talk_tv_female:
    bree.say "Hey, Sasha, [mike.name]'s out tonight."
    bree.say "And you know what that means, right?"
    bree.say "We're the one's in control of the TV for once!"
    if hero.charm >= 25:
        sasha.say "Oh yeah, [hero.name]!"
        sasha.say "That sounds like so much fun!"
        sasha.say "So, what are we going to watch?"
        sasha.say "I'm sure you'll pick something great!"
        $ sasha.sub += 1
    else:
        sasha.say "Oh yeah, I forgot about that!"
        sasha.say "Bags I get to choose what we watch though."
        sasha.say "You chose the last time - and I have better taste!"
        $ sasha.love += 1
    return

label sasha_talk_sports_female:
    bree.say "Hmm...sports or sci-fi?"
    bree.say "I got to choose last time we watched TV."
    bree.say "So I guess it's up to you, Sasha."
    sasha.say "Oh, I thought it was your turn!"
    sasha.say "But thanks for being honest, [hero.name]."
    sasha.say "Sports it is then!"
    $ sasha.love += 2
    return

label sasha_talk_fashion_female:
    bree.say "You have to take me shopping sometime, Sasha."
    bree.say "I'm really liking the whole dark vibe of your wardrobe!"
    bree.say "I kinda want to see what I'd look like in that style too!"
    sasha.say "Aw...thanks, [hero.name]!"
    sasha.say "Sure thing we can go shopping together."
    sasha.say "And I'm sure you'll make a super-cute goth too!"
    $ sasha.love += 1
    return

label sasha_talk_books_female:
    bree.say "Oh, Sasha, I just finished this great book."
    bree.say "It's got action, romance, everything!"
    bree.say "You really should read it."
    sasha.say "Erm...no thanks, [hero.name]."
    sasha.say "I don't like people recommending books for me."
    sasha.say "When I do read, it's kind of a personal thing..."
    $ sasha.love -= 1
    return

label sasha_talk_people_female:
    bree.say "You must see a lot of new faces playing in a band, Sasha."
    bree.say "But I can't imagine what it's like when they're your fans too!"
    bree.say "That must be weird, right?"
    sasha.say "Well, you kind of get used to it..."
    sasha.say "Ah, who am I kidding!"
    sasha.say "It's weird, but a good kind of weird, you know?"
    $ sasha.love += 1
    return

label sasha_talk_computers_female:
    bree.say "Ooh, Sasha...I just downloaded this great new program on my laptop."
    bree.say "It's so good - you should get it too!"
    bree.say "Come see!"
    sasha.say "No thanks, [hero.name]."
    sasha.say "My laptop's more of necessary evil."
    sasha.say "I only use it when I really have to."
    $ sasha.love -= 1
    return

label sasha_talk_music_female:
    bree.say "Sasha...Sasha!"
    bree.say "I just listened to that Deathless Harpies track you sent me."
    sasha.say "Oh yeah?"
    sasha.say "What did you think?"
    bree.say "Well...I'm no metal-head..."
    bree.say "But it was amazing!"
    bree.say "You guys are SO good!"
    sasha.say "Th...thanks, [hero.name]!"
    sasha.say "That means a lot!"
    sasha.say "I think I have something in my eye..."
    $ sasha.love += 1
    return

label sasha_talk_birthday_female:
    bree.say "Happy Birthday, Sasha!"
    bree.say "Many happy returns to the best housemate in the world!"
    sasha.say "Th...thanks, [hero.name]!"
    sasha.say "That means a lot!"
    sasha.say "I think I have something in my eye..."
    $ sasha.love += 5
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
