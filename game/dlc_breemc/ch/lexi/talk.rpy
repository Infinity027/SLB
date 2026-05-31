label lexi_talk_love_female:
    show lexi
    bree.say "A girl like you must have some crazy stories to tell about love, Lexi!"
    bree.say "I bet you could write a whole book about your amorous adventures, right?"
    if lexi.love >= 50:
        lexi.say "You have no fucking idea, [hero.name]!"
        lexi.say "I'd need more than one book though!"
        lexi.say "Oh, and for some of the people involved to be dead too..."
        $ lexi.love += 1
    else:
        lexi.say "What in the hell's that supposed to mean, [hero.name]?"
        lexi.say "Sure, I've been around the block a couple of times."
        lexi.say "But you make it sound like I've been ridden more times than a roller-coaster!"
        $ lexi.love -= 1
    hide lexi
    return

label lexi_talk_sex_female:
    show lexi
    bree.say "You know, I really admire the way you handle sex, Lexi."
    bree.say "It's like you're an intensely sexual being, sure."
    bree.say "But you're okay with that, and you own it."
    lexi.say "Hah!"
    lexi.say "That sounds like something a therapist would say, [hero.name]!"
    lexi.say "Let's just say I like it up me and leave it at that!"
    $ lexi.love += 1
    hide lexi
    return

label lexi_talk_politics_female:
    show lexi
    bree.say "There's a deeper side to everyone, right, Lexi?"
    bree.say "Like, I mean take politics for example."
    bree.say "You don't talk about stuff like that."
    bree.say "But I bet you have opinions on it."
    lexi.say "The only opinion I have on politics is that they're all scumbags!"
    lexi.say "They're bigger criminals than anyone I ever knew on the streets."
    lexi.say "But because they've got money and fancy things, they get away with it!"
    $ lexi.love -= 2
    hide lexi
    return

label lexi_talk_food_female:
    show lexi
    bree.say "Ooh...I need to think of something to eat for supper!"
    bree.say "Sorry if that sounds boring, Lexi."
    bree.say "I guess you have better things to talk about?"
    lexi.say "Nothing's more important than food, [hero.name]!"
    lexi.say "I'm a girl that likes to feel something warm inside of me..."
    lexi.say "Well...you know what I mean!"
    $ lexi.sub += 1
    hide lexi
    return

label lexi_talk_travels_female:
    show lexi
    bree.say "I keep meaning to start putting some money away, Lexi."
    bree.say "I want to save up to go travelling sometime soon."
    bree.say "Everyone wants to see the world, right?"
    lexi.say "Nah, I'll take a hard pass on that one!"
    lexi.say "It always sounds like so much hassle."
    lexi.say "And why go all that way when I can see it all on TV?"
    $ lexi.love -= 1
    hide lexi
    return

label lexi_talk_tv_female:
    show lexi
    bree.say "I'm worried that I watch too much TV, Lexi."
    bree.say "I have so much stuff recorded on the DVR."
    bree.say "Maybe we should try turning it off and talking instead?"
    lexi.say "You do you, [hero.name] - I'm happy laid on the sofa!"
    lexi.say "You couldn't pry my ass off of it with a crowbar!"
    $ lexi.love += 1
    hide lexi
    return

label lexi_talk_sports_female:
    show lexi
    bree.say "I think I might actually be getting into team sports, Lexi!"
    bree.say "I managed to watch a whole half of a soccer game the other day."
    bree.say "And I didn't fall asleep once - can you believe that?"
    lexi.say "Boo!"
    lexi.say "Sports are a waste of time and energy."
    lexi.say "The only time I want to be that hot and sweaty is while I'm fucking!"
    hide lexi
    return

label lexi_talk_fashion_female:
    show lexi
    bree.say "I love the look that you have going on, Lexi."
    bree.say "It's trashy, but really feisty at the same time."
    bree.say "I didn't know you could say so much while wearing so little!"
    lexi.say "Thanks, [hero.name] - I do my best to be a trend-setter."
    lexi.say "Trust me, as soon as the weather gets warmer, I'll be wearing even less!"
    $ lexi.love += 1
    hide lexi
    return

label lexi_talk_books_female:
    show lexi
    bree.say "You read any good books lately, Lexi?"
    bree.say "I just finished off the last one in my pile."
    bree.say "So I'm looking for any hot tips!"
    lexi.say "Boring!"
    lexi.say "I only read stuff with pictures."
    lexi.say "Oh, and sexy stuff - I like to look at sexy pictures!"
    $ lexi.love -= 2
    hide lexi
    return

label lexi_talk_people_female:
    show lexi
    bree.say "You must have seen a lot of humanity in your line of work, Lexi."
    bree.say "How's it shaped your view of people?"
    bree.say "Do you think they're basically good or bad?"
    lexi.say "Ah, people are just people."
    lexi.say "I never cared if they were good or bad."
    lexi.say "I only wanted to know what I could get out of them!"
    hide lexi
    return

label lexi_talk_computers_female:
    show lexi
    bree.say "Oh, I got those links you asked for, Lexi."
    bree.say "But I need your email address so I can send them to you, okay?"
    lexi.say "I dunno, [hero.name]..."
    lexi.say "Can't you just scribble it down on a piece of paper or something?"
    lexi.say "I don't trust computers!"
    $ lexi.love -= 2
    hide lexi
    return

label lexi_talk_music_female:
    show lexi
    bree.say "I might play some music on my phone."
    bree.say "You got any preferences, Lexi?"
    lexi.say "Nah, you go ahead and play whatever, [hero.name]."
    lexi.say "Music's just music, right?"
    hide lexi
    return

label lexi_talk_birthday_female:
    show lexi
    bree.say "Happy Birthday, Lexi!"
    bree.say "Many happy returns!"
    lexi.say "Wow...you remembered my birthday?"
    lexi.say "My own Mom never remembers my birthday!"
    $ lexi.love += 3
    hide lexi
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
