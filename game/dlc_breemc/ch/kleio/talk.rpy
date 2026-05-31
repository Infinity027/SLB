label kleio_talk_love_female:
    show kleio
    bree.say "I know you like to act all tough and cynical, Kleio."
    bree.say "But I get the feeling you're really an old romantic at heart!"
    if kleio.love >= 50:
        kleio.say "Shhh!"
        kleio.say "Shut up, [hero.name]!"
        kleio.say "Okay, okay...you found me out - but you'd better not tell another soul!"
        $ kleio.love += 1
    else:
        kleio.say "Geez, [hero.name]!"
        kleio.say "I'd say a penny for your thoughts - but I'd be getting ripped off!"
        kleio.say "You really don't get me at all, do you?"
        $ kleio.love -= 1
    hide kleio
    return

label kleio_talk_sex_female:
    show kleio
    bree.say "Okay, Kleio, okay - you're a hard-assed sister, I get it!"
    bree.say "But I figured out one thing you have to like."
    bree.say "And that's sex - everyone likes sex, right?"
    if kleio.love >= 50:
        kleio.say "What kind of a goof are you, [hero.name]?"
        kleio.say "Of course I like doing it - I'm only human!"
        kleio.say "Just keep it down, yeah?"
    else:
        kleio.say "Whoa...hold it right there, [hero.name]!"
        kleio.say "You just crossed over the line into private and personal."
        kleio.say "Now you need to take a step back - a big one!"
        $ kleio.love -= 1
    hide kleio
    return

label kleio_talk_politics_female:
    show kleio
    bree.say "Ooh...you're political and stuff, aren't you, Kleio?"
    bree.say "I bet you have all sorts of interesting opinions on politics, right?"
    bree.say "And you're pretty loud too, so you must like sharing them too!"
    if kleio.love >= 50:
        kleio.say "Of course I do, [hero.name]!"
        kleio.say "Anybody that doesn't is a fucking moron!"
        kleio.say "Oh, and most people who disagree with me are too!"
        $ kleio.love += 1
    else:
        kleio.say "Ha...I don't have opinions, [hero.name] - I have principles!"
        kleio.say "And save your breath asking me to explain them to you."
        kleio.say "I don't think you'd be able to keep up for a minute!"
        $ kleio.sub -= 1
    hide kleio
    return

label kleio_talk_food_female:
    show kleio
    bree.say "Mmm...I'm hungry, Kleio."
    bree.say "Looks like it's time for a snack!"
    bree.say "I know you're angry, but are you hungry too?"
    bree.say "Ooh...maybe you're hangry!"
    if kleio.love >= 75:
        kleio.say "For your information, [hero.name] - I am not hungry or angry."
        kleio.say "And as far as food goes, you do you."
        $ kleio.love += 1
    else:
        kleio.say "Urgh..."
        kleio.say "Okay, [hero.name], okay - you got me!"
        kleio.say "I am hungry, so let's grab something to eat already!"
        $ kleio.love -= 1
    hide kleio
    return

label kleio_talk_travels_female:
    show kleio
    bree.say "It sucks when you want to see the world and you're broke!"
    bree.say "You know what I mean, Kleio?"
    bree.say "I'd love to travel, but I can barely make the rent!"
    kleio.say "Ahh...I know just what you mean, [hero.name]!"
    kleio.say "There are so many cool places out there..."
    kleio.say "I just keep hoping the band makes it big, you know?"
    kleio.say "That way we could go on tour and see the world!"
    $ kleio.love += 1
    hide kleio
    return

label kleio_talk_tv_female:
    show kleio
    bree.say "I need to keep off the videogames tonight, Kleio."
    bree.say "If I don't, I won't be able to get my TV hit!"
    bree.say "So many shows, so little time!"
    kleio.say "Urgh..."
    kleio.say "There's a real world all around you, [hero.name]."
    kleio.say "Maybe you should try getting into that for a change?"
    $ kleio.love -= 1
    hide kleio
    return

label kleio_talk_sports_female:
    show kleio
    bree.say "All the guys I know get so worked up about their sports, Kleio!"
    bree.say "I just don't get how they can be so passionate about a game."
    bree.say "What do you think?"
    kleio.say "I couldn't care less, [hero.name]."
    kleio.say "There's only one thing more boring than watching sports."
    kleio.say "And that's talking about sports!"
    hide kleio
    return

label kleio_talk_fashion_female:
    show kleio
    bree.say "I love your look, Kleio."
    bree.say "Punk never really seems to go out of fashion."
    bree.say "And you wear it so well!"
    if kleio.love >= 50:
        kleio.say "I don't really think of it as a 'look', [hero.name]."
        kleio.say "It's more a way of life for me, you know?"
        kleio.say "But thanks for the compliment all the same!"
        $ kleio.love += 1
    else:
        kleio.say "Hah...shows what you know, [hero.name]!"
        kleio.say "Punk's not a look, it's a fucking mindset - a way of life!"
        kleio.say "But I wouldn't expect you to understand that."
        $ kleio.love -= 1
    hide kleio
    return

label kleio_talk_books_female:
    show kleio
    bree.say "You read, right, Kleio?"
    bree.say "I mean, you're pretty smart - or at least you sound like you are."
    bree.say "So you must read, right?"
    if hero.knowledge >= 25:
        kleio.say "Of course I read, [hero.name]!"
        kleio.say "Everybody should read, as much as they can!"
        kleio.say "Feeding your brain's as important as feeding your body."
        $ kleio.love += 1
    else:
        kleio.say "Of course I read, [hero.name]!"
        kleio.say "Does that come as a surprise to you?"
        kleio.say "Because it wouldn't surprise me if you couldn't!"
        $ kleio.love -= 1
    hide kleio
    return

label kleio_talk_people_female:
    show kleio
    bree.say "You must meet a lot of interesting people, Kleio."
    bree.say "You know, being in a band and playing all those gigs?"
    kleio.say "Meh..."
    kleio.say "People are just people, [hero.name]."
    kleio.say "Most of them are nothing special."
    hide kleio
    return

label kleio_talk_computers_female:
    show kleio
    bree.say "Do you use computers when you're making music, Kleio?"
    bree.say "You know, like sampling and mixing, that kind of thing?"
    kleio.say "Are you kidding, [hero.name]?!?"
    kleio.say "Music's a form of art - pure and unfettered!"
    kleio.say "It shouldn't be polluted with stuff like computers!"
    $ kleio.love -= 1
    hide kleio
    return

label kleio_talk_music_female:
    show kleio
    bree.say "Ooh...ooh!"
    bree.say "You're into your music, right, Kleio?"
    bree.say "Can you recommend something for me to listen to?"
    if kleio.love >= 50:
        kleio.say "You've come to the right person, [hero.name]!"
        kleio.say "I've got the knowledge you need to save your record collection!"
        $ kleio.love += 1
    else:
        kleio.say "Forget about it, [hero.name]."
        kleio.say "I don't think we're in the same wave-length."
        $ kleio.love -= 1
    hide kleio
    return

label kleio_talk_birthday_female:
    show kleio
    bree.say "Oh, I meant to say..."
    bree.say "Happy Birthday, Kleio!"
    kleio.say "Huh?!?"
    kleio.say "You...you remembered my birthday?"
    kleio.say "Thanks, [hero.name]!"
    $ kleio.love += 3
    hide kleio
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
