label shawn_talk_love_female:
    bree.say "What do you think about love, Shawn?"
    bree.say "Do you believe in it?"
    bree.say "Or are you one of those guys that thinks it's just a chemical reaction?"
    shawn.say "The first one, [hero.name]!"
    shawn.say "I could really get into the idea of true love."
    shawn.say "If anyone would actually give me the chance!"
    $ shawn.love += 1
    return

label shawn_talk_sex_female:
    bree.say "I see you as one of those sexy, repressed geeks, Shawn!"
    bree.say "Like everybody thinks you're all talk and movie quotes."
    bree.say "But the real, passionate you is trying to break out!"
    shawn.say "Yeah, [hero.name] - that's right!"
    shawn.say "Just because I love cool stuff doesn't mean I'm not a sexual being!"
    shawn.say "I'm like an undiscovered world in a sci-fi novel!"
    $ shawn.love += 1
    return

label shawn_talk_politics_female:
    bree.say "Do you do politics, Shawn?"
    bree.say "I mean, you're a bit of a lock-in."
    bree.say "So I get it if you're not interested."
    shawn.say "Meh...I try to avoid politics at all costs, [hero.name]."
    shawn.say "Both sides just sound the same to me."
    shawn.say "Unless someone from one of my favourite sci-fi shows were to run for office..."
    $ shawn.love -= 1
    return

label shawn_talk_food_female:
    bree.say "I'm getting pretty hungry, Shawn."
    bree.say "How about you?"
    bree.say "We could maybe order a pizza?"
    shawn.say "Wow, [hero.name] - that's amazing!"
    shawn.say "It's like you read my mind or something!"
    shawn.say "I'm starving, and I LOVE pizza!"
    $ shawn.love += 1
    return

label shawn_talk_travels_female:
    bree.say "There's like a million places that I want to travel to, Shawn."
    bree.say "But Tokyo's always been right up there, at the top of my list!"
    shawn.say "Whoa...that's such a crazy coincidence, [hero.name]!"
    shawn.say "Tokyo's top of my bucket-list too!"
    shawn.say "The stores full of manga, all those cutting edge electronics!"
    shawn.say "It always looks like geek heaven to me!"
    $ shawn.love += 1
    return

label shawn_talk_tv_female:
    bree.say "Ooh...I hate it when this happens!"
    bree.say "The DVR is almost full up with my stuff already."
    bree.say "But there are SO MANY cool new shows about to start streaming!"
    shawn.say "I know, [hero.name], I know - it's an all too familiar pain!"
    shawn.say "You should come down to the store ASAP."
    shawn.say "What you need is a memory upgrade on that DVR of yours!"
    $ shawn.love += 1
    return

label shawn_talk_sports_female:
    bree.say "I don't get the feeling that you're a sporty type, Shawn."
    bree.say "But don't worry - I'll let you into a little secret."
    bree.say "I'm not sporty either!"
    shawn.say "Oh god, [hero.name] - that's such a relief for me to hear!"
    shawn.say "I actually have a doctor's note excusing me from any kind of strenuous physical activity."
    shawn.say "Even sports videogames make me break out in a rash!"
    return

label shawn_talk_fashion_female:
    bree.say "Not really into the whole fashion thing, are you Shawn?"
    bree.say "In fact, I don't think I've ever seen you in anything but your work clothes!"
    shawn.say "Hey - that's a pretty low blow, [hero.name]!"
    shawn.say "I just think fashion's a pretty pointless thing."
    shawn.say "It's what's inside that counts, not what I'm wearing!"
    return

label shawn_talk_books_female:
    bree.say "I'm gonna go out on a limb and guess you're a reader, Shawn."
    bree.say "You just have that look of a guy that always has his nose in a book!"
    shawn.say "Of course I am, [hero.name]!"
    shawn.say "Who needs people when you can read a great book instead?"
    shawn.say "Plus, the real world kind of sucks..."
    $ shawn.love += 1
    return

label shawn_talk_people_female:
    bree.say "You're a tough one to figure out in some ways, Shawn."
    bree.say "Like, you work in an electronics store, serving customers all day."
    bree.say "But something tells me that you're not really a people person."
    shawn.say "You got it, [hero.name] - that's me in a nutshell!"
    shawn.say "It's like I love the stuff I sell, but I hate the people I sell it to!"
    shawn.say "Nobody else seems to understand that - but you do!"
    return

label shawn_talk_computers_female:
    bree.say "I'm pretty clued-up when it comes to computers, Shawn."
    bree.say "But I've heard you and [mike.name] talking about them."
    bree.say "And what you were talking about really blew me away!"
    shawn.say "That's kind of my thing, [hero.name]!"
    shawn.say "I'm the daddy when it comes to computers."
    shawn.say "Anything you need, just come to me!"
    $ shawn.love += 1
    return

label shawn_talk_music_female:
    bree.say "You like music, right, Shawn?"
    bree.say "Of course you do - everybody does!"
    bree.say "How about retro videogame themes?"
    shawn.say "Oh man...did you sneak a look at my playlist?"
    shawn.say "Those things are playing in my head all the time!"
    return

label shawn_talk_birthday_female:
    bree.say "Happy Birthday, Shawn!"
    bree.say "Have a geeky birthday!"
    shawn.say "Y...you remembered?!?"
    shawn.say "Wow, [hero.name] - that's amazing!"
    $ shawn.love += 2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
