label mike_talk_love_female:
    show mike
    if randint(0, 1) == 0:
        bree.say "What about you, [mike.name] - got any good war stories about your past conquests?"
        mike.say "Ah, geez...not really - I've never been all that lucky in love..."
    else:
        bree.say "[mike.name]..."
        bree.say "I was just wondering..."
        bree.say "What do you think about...love?"
        mike.say "Whoa, that's a bid random, [hero.name]!"
        mike.say "You know one thing I think?"
        mike.say "I think you shouldn't spring questions like that on me!"
    $ mike.love -= 1
    hide mike
    return

label mike_talk_sex_female:
    show mike
    if randint(0, 1) == 0:
        bree.say "I love the fact that we're becoming more liberated these days, that we can talk about sex whenever we want."
        mike.say "Yeah, it's pretty neat - I mean, I love having sex!"
        "I have to chuckle at his two-dimensional response."
        bree.say "Yeah, [mike.name] - I already got that!"
    else:
        bree.say "One thing I love about being alive right now is sex!"
        mike.say "HUH?!?"
        bree.say "I mean, it's great that we can actually talk about it, right?"
        bree.say "Like in the past, nobody talked about it and everyone was unhappy - and that was bad!"
        mike.say "Y...yeah, [hero.name]!"
        mike.say "You're totally right!"
        mike.say "We can talk about sex anytime you want to!"
    $ mike.love += 1
    hide mike
    return

label mike_talk_politics_female:
    show mike
    if randint(0, 1) == 0:
        bree.say "It's not long until the campaigning starts for the local elections."
        bree.say "But I'm still not sure which of the candidates I trust the most."
        mike.say "Huh - candidates for what now?"
    else:
        bree.say "Urgh..."
        bree.say "I have NO idea who to vote for this time around, [mike.name]!"
        bree.say "These guys have great policies, but the candidate's a scumbag."
        bree.say "And these guys have terrible policies, but their candidate's great!"
        mike.say "Ah...don't ask me, [hero.name]!"
        mike.say "You have no idea how much I hate politics!"
        mike.say "In fact, don't talk to me about it again!"
    $ mike.love -= 1
    hide mike
    return

label mike_talk_food_female:
    show mike
    if randint(0, 1) == 0:
        bree.say "It's like I WANT to eat healthy, but there are only so many hours in the day."
        bree.say "What about you, [mike.name]?"
        mike.say "It's all about convenience for me - junk food all the way."
    else:
        bree.say "Ooh...I think I hear my stomach rumbling!"
        bree.say "That means it's time for a snack!"
        bree.say "You want one too, [mike.name]?"
        mike.say "But, [hero.name], we just ate a meal like twenty minutes ago!"
        bree.say "So what?"
        bree.say "If I want a snack, I get a snack!"
        mike.say "[hero.name]...I think I love you!"
        mike.say "I...I mean I think I love your snacking habits!"
    $ mike.love += 1
    hide mike
    return

label mike_talk_travels_female:
    show mike
    if randint(0, 1) == 0:
        bree.say "Sometimes I feel like a failure when I look at how many of my friends have gone off and travelled the world."
        mike.say "It's no big deal."
        mike.say "Hell, I've never even been outside the country."
    else:
        bree.say "I'm thinking of starting up one of those picture-boards."
        bree.say "You know what I mean, [mike.name]?"
        bree.say "Somewhere I can pin-up pictures of all the places I want to go one day!"
        mike.say "That's a great idea, [hero.name]!"
        mike.say "I'm always dreaming about just packing it all in and going travelling too."
    $ mike.love += 1
    hide mike
    return

label mike_talk_tv_female:
    show mike
    if randint(0, 1) == 0:
        bree.say "Urrgh...everyone keeps on telling me about what new series I need to watch when I'm only halfway through the last one!"
        mike.say "I know, I know - so many decent TV shows out there and so little time."
    else:
        bree.say "There'd better be plenty of room in the DVR's memory."
        bree.say "Because the new season of Weirder Shit is starting soon!"
        mike.say "You're kidding?!?"
        mike.say "How in the hell did I miss that?"
        bree.say "Don't worry, [mike.name] - I already programmed it to record."
        bree.say "You want to watch it with me?"
        mike.say "Sure I do, [hero.name]!"
    $ mike.love += 1
    hide mike
    return

label mike_talk_sports_female:
    show mike
    if randint(0, 1) == 0:
        bree.say "Hey, the new football season's starting this weekend - wanna catch a game?"
        mike.say "Nah...not really my cup of tea."
    else:
        bree.say "[mike.name]..."
        bree.say "You're a guy, right?"
        mike.say "Sort of, [hero.name]..."
        mike.say "I..I mean of course I am!"
        bree.say "So explain sports to me?"
        bree.say "You guys seem to love it."
        bree.say "But I just don't see the appeal."
        mike.say "Oh...erm..."
        mike.say "I can't, [hero.name] - I'm not that kind of guy!"
    $ mike.love -= 1
    hide mike
    return

label mike_talk_fashion_female:
    show mike
    if randint(0, 1) == 0:
        bree.say "What do you think of this outfit, [mike.name]?"
        mike.say "Whatever...less is more, I guess..."
    else:
        bree.say "What look are you trying to pull off this season, [mike.name]?"
        bree.say "No, let me guess - it's some kind of computer nerd chic, right?"
        mike.say "Hey!"
        mike.say "What the hell is that supposed to mean?"
        bree.say "Oh...oh dear - you actually meant to dress like that?"
        mike.say "[hero.name] - these are my nicest things!"
    $ mike.love -= 1
    hide mike
    return

label mike_talk_books_female:
    show mike
    if randint(0, 1) == 0:
        bree.say "I just finished this book that my friend recommended."
        bree.say "I swear that I could not put it down!"
        mike.say "What's it called?"
        mike.say "Maybe I could borrow it?"
        mike.say "I love books."
    else:
        bree.say "Ooh..."
        bree.say "Who's been leaving piles of books around the house?"
        mike.say "I'm sorry, [hero.name]!"
        mike.say "Those are mine - but I did mean to clean them up, I promise."
        bree.say "Oh no, [mike.name] - I wanted to ask if I could borrow some of them!"
        bree.say "They look really interesting!"
        mike.say "You're serious?"
        mike.say "Sure, [hero.name], of course you can!"
    $ mike.love += 1
    hide mike
    return

label mike_talk_people_female:
    show mike
    if randint(0, 1) == 0:
        bree.say "It's so important to get out and meet new people every now and again."
        bree.say "People that'll actually listen to what you have to say."
        mike.say "Who's listening to who say what now?"
    else:
        bree.say "It's starting to smell like ass around the house, [mike.name]."
        bree.say "I really think we should get out more, you know?"
        bree.say "Maybe go to the pub and socialise with other people?"
        mike.say "Urgh..."
        mike.say "Do we HAVE to, [hero.name]?"
        mike.say "People suck!"
    $ mike.love -= 1
    hide mike
    return

label mike_talk_computers_female:
    show mike
    if randint(0, 1) == 0:
        bree.say "My laptop's been playing up recently."
        bree.say "You work with computers, don't you, [mike.name]?"
        mike.say "Please, [hero.name] - I don't want to talk about work."
        mike.say "I'd rather talk about you."
    else:
        bree.say "[mike.name]..."
        bree.say "Is the router on the blink again?"
        mike.say "Yeah, but I already rebooted it."
        bree.say "That thing sucks, and it's ancient."
        bree.say "We should get one of those new home-hubs with all the lights on them."
        mike.say "Ooh...I know just the one you mean!"
        mike.say "And my buddy Shawn works at the electrical store too."
        mike.say "I bet he can get us a discount!"
    $ mike.love += 1
    hide mike
    return

label mike_talk_music_female:
    show mike
    if randint(0, 1) == 0:
        bree.say "Sasha always seems to be playing heavy metal as loud as she can!"
        mike.say "I know, [hero.name] - I do have ears, and she's going to make them bleed!"
    else:
        bree.say "Who in the hell's playing that song?!?"
        mike.say "Sorry, [hero.name] - it was me."
        mike.say "Don't worry, I'm used to people telling me to turn it off!"
        bree.say "Turn it off?"
        bree.say "I love this track!"
        mike.say "Y...you do?"
        mike.say "I thought I was the only one!"
    $ mike.love += 1
    hide mike
    return

label mike_talk_birthday_female:
    show mike
    if randint(0, 1) == 0:
        bree.say "Happy birthday, [mike.name]!"
        mike.say "Aw, thanks, [hero.name] - feels like you're the only one that thinks about me around here."
    else:
        bree.say "Happy Birthday, [mike.name]!"
        bree.say "Hope you have a good one!"
        mike.say "Aw, thanks, [hero.name]!"
        mike.say "You remembered my birthday!"
    $ mike.love += 1
    hide mike
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
