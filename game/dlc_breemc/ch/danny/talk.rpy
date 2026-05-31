label danny_talk_love_female:
    show danny
    bree.say "You've got a reputation for being a bad guy, Danny."
    bree.say "So I suppose your heart's as hard and black as slate, huh?"
    bree.say "No way that you could learn to love someone?"
    danny.say "Wh...what did you just say?"
    danny.say "That's not fair - nobody ever gave me a chance!"
    danny.say "Who says I can't learn to love somebody!"
    $ danny.love -= 1
    hide danny
    return

label danny_talk_sex_female:
    show danny
    bree.say "I've got to be honest with you, Danny."
    bree.say "I know you're from the wrong side of the tracks."
    bree.say "But the idea of being with a guy like you..."
    bree.say "It's kind of exciting in a scary way!"
    danny.say "Hey, you know it is, baby!"
    danny.say "This bad boy'll make a bad girl out of you!"
    $ danny.love += 1
    hide danny
    return

label danny_talk_politics_female:
    show danny
    bree.say "What side of the political debate does a bad guy come down on, Danny?"
    bree.say "Surely you can't be on the side of anyone that wants more police on the beat?"
    danny.say "Hey, I leave politics to the politicians, babe!"
    danny.say "You think I'm bad, huh?"
    danny.say "You ain't seen nobody as sick as those motherfuckers!"
    $ danny.love -= 1
    hide danny
    return

label danny_talk_food_female:
    show danny
    bree.say "You're a pretty build guy, Danny."
    bree.say "Nobody gets to look like that eating a salad!"
    bree.say "What kind of stuff do you like eating anyway?"
    danny.say "Food's the fuel for Danny's engine, [hero.name]!"
    danny.say "Feed him burgers and foot-long's."
    danny.say "With those in his tank, he'll go all night!"
    hide danny
    return

label danny_talk_travels_female:
    show danny
    bree.say "You're a biker, right, Danny?"
    bree.say "Does that mean you love the open road?"
    bree.say "The feel of the wind in your hair and the freedom to go anywhere?"
    danny.say "Whoa...you'd better believe it, girl!"
    danny.say "Take a ride on the back of my bike and come see for yourself."
    danny.say "I guarantee you'll want to ride forever!"
    $ danny.love += 1
    hide danny
    return

label danny_talk_tv_female:
    show danny
    bree.say "You know, you remind me of the villains in cop shows, Danny."
    bree.say "Did you watch those when you were coming up with your look?"
    bree.say "Or is it just a coincidence?"
    danny.say "Aw...I hate those kind of shows!"
    danny.say "They always show it from the cop's point of view."
    danny.say "Nobody ever gets to hear the other guy's side of it!"
    hide danny
    return

label danny_talk_sports_female:
    show danny
    bree.say "You like sports, right, Danny?"
    bree.say "A big, macho biker like you - it's a no-brainer!"
    danny.say "Nah...I never much liked competitive sports."
    danny.say "Too many rules for my taste - and the umpire's basically a rules cop!"
    danny.say "I'm really more of a knife-fighting kind of guy..."
    hide danny
    return

label danny_talk_fashion_female:
    show danny
    bree.say "So who started wearing all the leather first, Danny?"
    bree.say "Was it you bikers?"
    bree.say "Or those guys that sing the song about the YMCA?"
    danny.say "Hey, sister...you shouldn't joke about those cats!"
    danny.say "They're a tough bunch of guys!"
    danny.say "And they'll kick your ass!"
    $ danny.love -= 1
    hide danny
    return

label danny_talk_books_female:
    show danny
    bree.say "I don't see you as the type of guy that reads much, Danny."
    bree.say "In fact, can you actually read at all?"
    bree.say "I've never seen you actually do it!"
    danny.say "Hey - that's an unfounded and prejudiced assumption!"
    danny.say "Actually I just finished reading a book by Charles Dickens!"
    danny.say "I just gotta leave it at home."
    danny.say "Because...well, there's no pockets in this vest that's big enough for it!"
    $ danny.love -= 1
    hide danny
    return

label danny_talk_people_female:
    show danny
    bree.say "You don't strike me as a 'people person', Danny."
    bree.say "You know what I mean?"
    bree.say "You're a bit crazy and intimidating!"
    danny.say "Nah, [hero.name] - I LOVE people!"
    danny.say "It's people that buy the stuff I'm selling."
    danny.say "So why wouldn't I love 'em?"
    $ danny.love += 1
    hide danny
    return

label danny_talk_computers_female:
    show danny
    bree.say "You have much to do with computers, Danny?"
    bree.say "I mean, you can't carry one with you down a dodgy alleyway!"
    bree.say "And they're not going to help you out in a fight either!"
    danny.say "Nope, I like to rely on the old grey matter!"
    danny.say "It's never let me down yet, Dee!"
    bree.say "Erm...it's '[hero.name]', Danny!"
    hide danny
    return

label danny_talk_music_female:
    show danny
    bree.say "This might be a bit of a cliche, Danny."
    bree.say "But are you by any chance into Metallikea?"
    danny.say "Are you kidding, [hero.name]?!?"
    danny.say "I've loved those guys since 'Thrill Em All'!"
    danny.say "They're the greatest band in the world!"
    $ danny.love += 1
    hide danny
    return

label danny_talk_birthday_female:
    show danny
    bree.say "Happy Birthday, Danny!"
    bree.say "Hope you have a great day."
    danny.say "Thanks, [hero.name]!"
    danny.say "I couldn't remember if it was you I told today was my birthday!"
    bree.say "You tell different people a different date?"
    danny.say "Yeah, well...my momma could never remember it either."
    danny.say "So I just choose a date I like the sound of whenever anybody asks me..."
    $ danny.love += 1
    hide danny
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
