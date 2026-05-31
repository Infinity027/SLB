label harmony_talk_love_female:
    show harmony
    bree.say "You always seem so positive and full of hope, Harmony."
    bree.say "I'm kind of jealous of that..."
    bree.say "Because it must mean you believe in things like the power of love, right?"
    harmony.say "Oh, [hero.name] - of course I do!"
    harmony.say "Love is the most powerful force in the universe!"
    harmony.say "All you have to do is believe!"
    $ harmony.love += 1
    hide harmony
    return

label harmony_talk_sex_female:
    show harmony
    bree.say "[mike.name] tells me you're pretty...spiritual, Harmony."
    bree.say "I was kinda wondering about something..."
    bree.say "How does that work with the old S...E...X?"
    if harmony.purity >= VHP:
        harmony.say "I'm going to pretend that I didn't hear you say that, [hero.name]."
        harmony.say "And I'm going to have to have a chat with [mike.name] too!"
        harmony.say "Somebody's suffering from loose lips!"
        $ harmony.love -= 1
    elif harmony.purity >= HP:
        harmony.say "Oh, [hero.name]...that's not really an appropriate subject!"
        harmony.say "I can see we need to have a little chat about boundaries!"
        harmony.say "And [mike.name] needs a slap on the hand too!"
        $ harmony.love -= 1
    elif harmony.purity < VLP:
        harmony.say "Ah, fuck the spiritual side of things, [hero.name]!"
        harmony.say "Life's too short to be hung up on all that."
        harmony.say "I like it up me whenever I can get it!"
        $ harmony.love += 1
    elif harmony.purity < LP:
        harmony.say "Oh, [hero.name]...you can say the word sex if you want to!"
        harmony.say "It's not like I'm going to burst into flames!"
        harmony.say "And for the record, it doesn't seem to get in the way..."
        $ harmony.love += 1
    else:
        harmony.say "Oh...sorry, [hero.name] - you caught me off guard with that one!"
        harmony.say "I guess I'm not as comfortable discussing that kind of thing as I thought..."
        harmony.say "Don't worry, it's not your fault."
        harmony.say "I just had kind of a sheltered life...until I met [mike.name]!"
        $ harmony.love += 1
    hide harmony
    return

label harmony_talk_politics_female:
    show harmony
    bree.say "Being spiritual must mean you have a handle on what's right and wrong, Harmony."
    bree.say "Does it help when you have to do something like vote?"
    bree.say "Because I sometimes find it hard to tell if those guys are sincere or not!"
    harmony.say "Ooh...politicians make me SO mad, [hero.name]!"
    harmony.say "They all pretend to be good people in front of the camera."
    harmony.say "But they're really a bunch of fakes with no morals!"
    $ harmony.love -= 1
    hide harmony
    return

label harmony_talk_food_female:
    show harmony
    bree.say "Don't take this the wrong way, Harmony."
    bree.say "But you really seem to enjoy your food!"
    bree.say "It's kind of cool that you're not trying to starve yourself, you know?"
    harmony.say "I know what you mean, [hero.name] - I'm never going to be stick-thin!"
    harmony.say "And people are always telling me that over-indulgence is a sin..."
    harmony.say "But the way I see it, I was made this way, so I should just embrace it!"
    $ harmony.sub += 1
    hide harmony
    return

label harmony_talk_travels_female:
    show harmony
    bree.say "Do you like the idea of travelling, Harmony?"
    bree.say "I know it's kind of a cliche - like everyone wants to do it."
    bree.say "But that's no reason not to, right?"
    harmony.say "You're right, [hero.name] - I would love to travel."
    harmony.say "I want to got to Europe and see all the history there."
    harmony.say "All those ancient churches and cathedrals."
    harmony.say "Seeing those would be so cool!"
    $ harmony.love += 1
    hide harmony
    return

label harmony_talk_tv_female:
    show harmony
    bree.say "I know some religious people think TV's evil, Harmony."
    bree.say "Like it's a tool of the devil or something like that."
    bree.say "But there must be some stuff on there that's okay, right?"
    harmony.say "I don't think the television is evil, [hero.name]!"
    harmony.say "It's like most things - some of it's bad and some of it's good."
    harmony.say "I really like watching the good stuff too!"
    $ harmony.love += 1
    hide harmony
    return

label harmony_talk_sports_female:
    show harmony
    bree.say "Sports, sports, sports!"
    bree.say "Everyone's into sports, apparently!"
    bree.say "What about you, Harmony?"
    bree.say "Are you one of the sports zombies?"
    harmony.say "Oh no, [hero.name] - I hate sports!"
    harmony.say "I always got picked last in gym class."
    harmony.say "And ever since then I've despised all sports!"
    $ harmony.love -= 1
    hide harmony
    return

label harmony_talk_fashion_female:
    show harmony
    bree.say "I hear it used to be hard to get clothes in plus sizes, Harmony."
    bree.say "But now it seems to be getting easier to find nice stuff."
    bree.say "What's following fashions like for you, Harmony?"
    harmony.say "I don't really do that, [hero.name]."
    harmony.say "When you're brought up religious, you see things differently."
    harmony.say "So to me, fashion's kind of a sin - like vanity."
    hide harmony
    return

label harmony_talk_books_female:
    show harmony
    bree.say "Religious people always seem to like burning books, Harmony."
    bree.say "So how does that work for you?"
    bree.say "Is there like a list of stuff you're allowed to read?"
    bree.say "Or is it the good book and nothing else?"
    harmony.say "Oh no, [hero.name]...you're thinking of the really hardcore crazies!"
    harmony.say "Actually, I love reading."
    harmony.say "And I read all kinds of different stuff too!"
    harmony.say "We should compare notes some time."
    $ harmony.love += 1
    hide harmony
    return

label harmony_talk_people_female:
    show harmony
    bree.say "Your spirituality helps you see the good in people, right, Harmony?"
    bree.say "I mean that's one of the things that they teach you, isn't it?"
    harmony.say "Hmm..."
    harmony.say "It is one of the things you're supposed to take to heart, [hero.name]."
    harmony.say "But I've never found that it works out in reality."
    harmony.say "Some people are good and some are bad."
    harmony.say "Others are just a mix of both."
    hide harmony
    return

label harmony_talk_computers_female:
    show harmony
    bree.say "You have a computer, right, Harmony?"
    bree.say "I mean, I know you're spiritual and all that."
    bree.say "But owning technology's not a sin - is it?"
    harmony.say "No, [hero.name] - of course not!"
    harmony.say "I just find that computers don't agree with me."
    harmony.say "They seem to go wrong whenever I touch them!"
    $ harmony.love -= 1
    hide harmony
    return

label harmony_talk_music_female:
    show harmony
    bree.say "What's your take on music, Harmony?"
    bree.say "You don't just listen to religious stuff, do you?"
    harmony.say "Hmm..."
    harmony.say "Sometimes I hear stuff I like on the radio."
    harmony.say "But it's weird, [hero.name]..."
    harmony.say "Nothing really seems to stick in my head!"
    hide harmony
    return

label harmony_talk_birthday_female:
    show harmony
    bree.say "Happy Birthday, Harmony!"
    bree.say "Many happy returns!"
    harmony.say "Oh, bless you, [hero.name]!"
    harmony.say "It's so touching that you remembered!"
    $ harmony.love += 3
    hide harmony
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
