label morgan_talk_love_female:
    bree.say "Hey, Morgan...I heard that you've always had a massive crush on [mike.name]!"
    bree.say "I just wanted to say, that's so romantic!"
    bree.say "You must really be a believer in true love to hold a torch that long, huh?"
    if morgan.male >= 75:
        morgan.say "Who told you that?!?"
        morgan.say "If it was [mike.name], I'll kill him!"
        morgan.say "True love's just something dumb people make up to keep from going crazy!"
    elif morgan.male >= 25:
        morgan.say "I don't know if I'd say it was massive, [hero.name]!"
        morgan.say "More like I admired him from afar."
        morgan.say "True love makes it sound like a fairy tale."
        morgan.say "And that's not how I see it!"
        $ morgan.love += 1
    elif morgan.sub > 75:
        morgan.say "If that's what [mike.name] told you, then that's what happened, [hero.name]."
        morgan.say "And I don't know if it's true love between us."
        morgan.say "But he's finally helped me to discover my true calling in life!"
        $ morgan.love += 1
    else:
        morgan.say "Oh yeah, [hero.name] - that's just the way it happened!"
        morgan.say "I thought we'd never be reunited, but in the end we got there."
        morgan.say "So maybe there is an element of true love involved!"
        $ morgan.love += 1
    if morgan.love >= 50:
        $ morgan.male -= 1
    return

label morgan_talk_sex_female:
    bree.say "Oh, this is such an embarrassing thing to admit, Morgan..."
    bree.say "But I feel like I haven't had any real action in forever!"
    bree.say "If you know what I mean?"
    if morgan.male >= 75:
        morgan.say "Well what'd you expect me to do about it, [hero.name]?"
        morgan.say "You need to stop feeling sorry for yourself and get out there!"
        morgan.say "Get off your ass and go catch a dick!"
        $ morgan.male += 1
    elif morgan.male >= 25:
        morgan.say "Geez, [hero.name]...we've all been there!"
        morgan.say "Just don't let it get to you, okay?"
        morgan.say "It'll pass, and you'll forget you ever hit a dry patch."
    elif morgan.sub > 75:
        morgan.say "I'm not the kind to speak up and complain, [hero.name]."
        morgan.say "I'm happy to take what I'm given."
        morgan.say "But maybe you should just ask somebody you like?"
        morgan.say "You never know - they might take pity on you..."
    else:
        morgan.say "Oh, you're talking about sex, aren't you, [hero.name]?"
        morgan.say "I'm not really comfortable sharing that kind of personal information."
        morgan.say "So if you wouldn't mind, I'd rather we dropped the subject."
        $ morgan.love += 1
    if morgan.sub <= 25:
        $ morgan.sub += 1
    return

label morgan_talk_politics_female:
    bree.say "I always think that I should be more politically active, Morgan."
    bree.say "[mike.name] was telling me that you're a pretty radical thinker."
    bree.say "Got any advice on how I can get started?"
    if morgan.male >= 75:
        morgan.say "Nah, I kind of lost interest in the politics recently."
        morgan.say "You bust your ass protesting and waving banners."
        morgan.say "But nothing ever really changes, so it's a waste of time."
        $ morgan.love += 1
    elif morgan.male >= 25:
        morgan.say "Of course I can, [hero.name]!"
        morgan.say "And it's great that you're doing this!"
        morgan.say "I've got some books I can lend you."
        morgan.say "And there are some websites that'll be useful too..."
    else:
        morgan.say "Oh no, [hero.name]...no, no, no!"
        morgan.say "I gave up all of that stuff when I got in touch with my feminine side!"
        morgan.say "It's too raucous and violent for me now!"
        $ morgan.love -= 1
    return

label morgan_talk_food_female:
    bree.say "Are you hungry, Morgan?"
    bree.say "I already ate a meal."
    bree.say "But I never ignore my stomach!"
    bree.say "How about you?"
    if morgan.male >= 75:
        morgan.say "Then you really need to work on your willpower, [hero.name]!"
        morgan.say "Giving in to your appetite like that, it's not good."
        morgan.say "Before you know it, you won't be able to control yourself."
    elif morgan.male >= 25:
        morgan.say "Nah, [hero.name] - I'm fine, really."
        morgan.say "But you go ahead and do you."
        morgan.say "I promise I won't judge."
    elif morgan.sub > 75:
        morgan.say "If you want me to have a snack, then okay, [hero.name]."
        morgan.say "It'd be rude of me to say no, wouldn't it?"
        $ morgan.love += 1
    else:
        morgan.say "Well, I have already eaten..."
        morgan.say "But if you're going to grab a snack, then what the hell!"
        morgan.say "I might as well be naughty too!"
        $ morgan.love += 1
    return

label morgan_talk_travels_female:
    bree.say "Have you seen anything of the world, Morgan?"
    bree.say "I'm always dreaming about going off on a big adventure."
    bree.say "But that's all I ever seem to do - just dream!"
    if morgan.male >= 75:
        morgan.say "Nah, [hero.name] - I've never been anywhere special."
        morgan.say "Most places are just like here, ordinary and boring."
        morgan.say "Anywhere special they make sure you can't get to!"
        $ morgan.male += 1
    elif morgan.male >= 25:
        morgan.say "No, [hero.name] - I can't say that I have."
        morgan.say "But I keep dreaming about it too."
        morgan.say "And it's good to know that I'm not the only one!"
        $ morgan.love += 1
    else:
        morgan.say "I used to think about travelling and seeing the world."
        morgan.say "But now I realise what a big place it really is!"
        morgan.say "And the thought of that kind of scares me!"
        $ morgan.love += 1
    return

label morgan_talk_tv_female:
    bree.say "You watch much TV, Morgan?"
    bree.say "In our house, we've worn holes in the sofa cushions!"
    bree.say "And the DVR's always full to bursting!"
    if morgan.male >= 75:
        morgan.say "Meh..."
        morgan.say "I don't really catch much on the TV, [hero.name]."
        morgan.say "I'm too busy doing other shit."
        $ morgan.love -= 1
    elif morgan.male >= 25:
        morgan.say "Oh no, [hero.name] - no way!"
        morgan.say "I've got too much to get done in the time I've got left!"
        morgan.say "And I'm not going to spend it comatose in front of the TV!"
    elif morgan.sub > 75:
        morgan.say "I'll watch the TV if somebody else wants me to, [hero.name]."
        morgan.say "Just don't ask me to choose what we watch!"
        morgan.say "I'd rather have somebody else choose for me..."
        $ morgan.sub += 1
    else:
        morgan.say "I know that I shouldn't, [hero.name]..."
        morgan.say "But once I start watching, it's like I can't stop!"
        morgan.say "Is getting addicted to the TV an actual thing?"
        $ morgan.love += 1
    return

label morgan_talk_sports_female:
    bree.say "Why is there always so much sports on all year round?"
    bree.say "Spring sports, Summer sports, Autumn sports, Winter sports!"
    bree.say "I mean who actually watches all of this stuff?"
    if morgan.male >= 75:
        morgan.say "Well, for one thing it's because sports are awesome, [hero.name]!"
        morgan.say "But I guess they help people to escape from the banality of life too."
        morgan.say "A little breath of fresh air and distraction."
        $ morgan.love -= 1
    elif morgan.male >= 25:
        morgan.say "I dunno, [hero.name]!"
        morgan.say "I guess it's just always been that way."
        morgan.say "People like sports and like inventing new ones!"
        $ morgan.love += 1
    elif morgan.sub > 75:
        morgan.say "I don't really have an opinion on sports, [hero.name]."
        morgan.say "But I'll watch them if I'm told to."
        morgan.say "I'll even pretend to enjoy it."
        $ morgan.love += 1
    else:
        morgan.say "I know what you mean, [hero.name]!"
        morgan.say "It's so dumb it's unreal!"
        morgan.say "Just a load of high-school jocks that never grew up!"
        $ morgan.sub += 1
    return

label morgan_talk_fashion_female:
    bree.say "You've got a pretty strong look there, Morgan!"
    bree.say "Are you following any particular fashion?"
    bree.say "Or did you come up with it yourself?"
    if morgan.male >= 75:
        morgan.say "No and no, [hero.name]!"
        morgan.say "This is just the way I like to dress."
        morgan.say "People can take it or leave it."
        morgan.say "I don't care either way."
        $ morgan.love -= 1
        $ morgan.sub -= 1
        $ morgan.male += 1
    elif morgan.male >= 25:
        morgan.say "I don't know if I'd call it a fashion statement, [hero.name]!"
        morgan.say "I've always just gone with what I like and what feels like it fits."
        morgan.say "And I guess I managed to put some of my personality into it along the way!"
        $ morgan.love += 1
    elif morgan.sub > 75:
        morgan.say "Oh no, [hero.name]..."
        morgan.say "I should probably tone it down in that case!"
        morgan.say "Maybe I should start dressing like somebody else?"
        $ morgan.love += 1
    elif morgan.sub < 25:
        morgan.say "Y...you're right, [hero.name]!"
        morgan.say "I do have a look that's all me, don't I!"
        morgan.say "Maybe I should start having more confidence in myself?"
        $ morgan.male -= 1
    else:
        morgan.say "Thanks for noticing, [hero.name]!"
        morgan.say "I've been trying to think of a name for it too."
        morgan.say "How does 'Morganwave' sound?"
        $ morgan.love += 1
        $ morgan.sub += 1
        $ morgan.male -= 1
    return

label morgan_talk_books_female:
    bree.say "What's that you were reading just now, Morgan?"
    bree.say "It looked really interesting from what I could see of the cover."
    bree.say "And I'm looking for a recommendation as to what I should read next!"
    if morgan.male >= 75:
        morgan.say "Meh...whatever, [hero.name]."
        morgan.say "It's just some trash I picked up somewhere."
        morgan.say "Hell, I don't even remember where I got it!"
        $ morgan.love -= 1
        $ morgan.sub -= 1
        $ morgan.male += 1
    elif morgan.male >= 25:
        morgan.say "Sure, [hero.name]...here you go."
        morgan.say "It's been a great read so far."
        morgan.say "I'm sure you'll love it too."
        $ morgan.love += 1
        $ morgan.male -= 1
    elif morgan.sub > 75:
        morgan.say "Oh no, [hero.name]...don't be silly!"
        morgan.say "You don't want my advice."
        morgan.say "I should be the one asking you what I need to read next!"
        $ morgan.sub += 1
    elif morgan.sub < 25:
        morgan.say "You know what, [hero.name]...I will give you a recommendation!"
        morgan.say "Maybe I should have more confidence in my choice of books."
        morgan.say "I am a grown woman, after all!"
        $ morgan.sub -= 1
    else:
        morgan.say "Don't you think that's a bit rude, [hero.name]?"
        morgan.say "I haven't even finished the book yet."
        morgan.say "And you were snooping on me while I was reading too!"
        $ morgan.love -= 1
        $ morgan.sub += 1
        $ morgan.male -= 1
    return

label morgan_talk_people_female:
    bree.say "Part of me always wants to go out of my way to please people, Morgan."
    bree.say "But another part of me thinks that I try too hard as well!"
    bree.say "I never know which side I should be listening to!"
    if morgan.male >= 75:
        morgan.say "Don't as me, [hero.name]."
        morgan.say "Sounds like you need to talk to a therapist."
        morgan.say "And god knows that's not me!"
        $ morgan.love += 1
    elif morgan.male >= 25:
        morgan.say "You shouldn't change yourself to please others, [hero.name]."
        morgan.say "I did that for a long time, and look where it got me!"
        morgan.say "Be true to yourself, okay."
        morgan.say "That way anyone worth bothering with will get to know the real you."
    elif morgan.sub > 75:
        morgan.say "I find that if you let people have their way, that makes them happy, [hero.name]."
        morgan.say "So I always listen carefully so that I can figure out what they want."
        $ morgan.sub += 1
    else:
        morgan.say "You should always try to make people happy, [hero.name]!"
        morgan.say "If they're happy, then they'll treat you nicely."
        morgan.say "And we all want to be treated nicely, don't we?"
        $ morgan.love += 1
        $ morgan.male -= 1
    return

label morgan_talk_computers_female:
    bree.say "I just can't seem to figure out this problem with my laptop!"
    bree.say "Maybe what it needs is a fresh pair of eyes..."
    bree.say "Morgan, would you help me out with it?"
    if morgan.male >= 75:
        morgan.say "Nah, [hero.name]...computers aren't my strong suit!"
        morgan.say "You'd be better off asking an egg-head like [mike.name]."
        morgan.say "He knows all about that kind of stuff."
        $ morgan.male += 1
    elif morgan.male >= 25:
        morgan.say "Sure, [hero.name]...I'm no expert mind you!"
        morgan.say "But for what it's worth, I'll take a look."
        morgan.say "Who knows, I might spot something you missed!"
        $ morgan.love += 1
    elif morgan.sub > 75:
        morgan.say "No, [hero.name]...you don't want my help!"
        morgan.say "I'd only make it worse!"
        $ morgan.sub += 1
    elif morgan.sub < 25:
        morgan.say "You know what, [hero.name]...maybe I will take a look."
        morgan.say "After all, I'm not stupid, am I?"
        morgan.say "And I can hardly make it worse!"
    else:
        morgan.say "Oh no, [hero.name]!"
        morgan.say "I don't want to get involved."
        morgan.say "I might end up making it worse!"
        $ morgan.love -= 1
        $ morgan.sub += 1
        $ morgan.male += 1
    return

label morgan_talk_music_female:
    bree.say "What's that track you're listening to, Morgan?"
    bree.say "It sounds really interesting!"
    if morgan.male >= 75:
        morgan.say "I dunno, [hero.name]."
        morgan.say "It's just some random playlist I found."
        $ morgan.love += 1
        $ morgan.sub -= 1
        $ morgan.male += 1
    elif morgan.male >= 25:
        morgan.say "Oh, it's great, [hero.name]...really cool!"
        morgan.say "Come and have a listen for yourself."
        $ morgan.love += 1
    elif morgan.sub < 25:
        morgan.say "You know what, [hero.name]...you're right!"
        morgan.say "I wasn't so sure myself."
        morgan.say "But you convinced me!"
        $ morgan.love += 1
    else:
        morgan.say "That's pretty rude of you, [hero.name]!"
        morgan.say "I was losing myself in the music."
        morgan.say "And you just killed the mood!"
        $ morgan.love += 1
        $ morgan.male -= 1
    return

label morgan_talk_birthday_female:
    bree.say "Happy Birthday, Morgan!"
    morgan.say "Aw...thanks, [hero.name]!"
    $ morgan.love += 2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
