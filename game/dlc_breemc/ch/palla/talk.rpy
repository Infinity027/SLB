label palla_talk_love_female:
    bree.say "You must have guys falling for you all the time, Palla!"
    bree.say "I mean, you walk around like a model on a catwalk."
    bree.say "You're so confident you act like you own the place!"
    $ renpy.dynamic("result")
    $ result = randint(1, 3)
    if result == 1:
        palla.say "Oh yeah, I know what you mean, [hero.name]!"
        palla.say "Most of them just aren't prepared for a girl like me."
        palla.say "What hope do they have of resisting?"
    elif result == 2:
        palla.say "Frankly, [hero.name], I don't care what effect I have on them."
        palla.say "I don't have time to worry about anything like that."
        palla.say "I'm above such paltry concerns as other people's feelings!"
    else:
        palla.say "Urgh...don't remind me, [hero.name]!"
        palla.say "Do you know what it's like to turn men into salivating dogs?"
        palla.say "You can't get anything done, let alone hold a conversation."
        palla.say "All people want to do is tell me how beautiful I am!"
    $ palla.love += 1
    return

label palla_talk_sex_female:
    bree.say "All of this isn't for show, right, Palla?"
    bree.say "You're not just flashing the goods and then refusing to deliver?"
    bree.say "I mean...you actually like doing the deed, right?"
    if randint(0, 1) == 0:
        palla.say "Oh dear, [hero.name]...let me explain something to you."
        palla.say "It's all about selling an image to people, you see."
        palla.say "You make them think they want something like crazy."
        palla.say "But you never actually let them have it - that's the trick!"
    else:
        palla.say "Of course I do, [hero.name]!"
        palla.say "I just like to make sure they earn it before they get it."
        palla.say "People are so much more eager to please if they had to work for it!"
        palla.say "And I enjoy reaping that reward..."
    $ palla.love += 1
    return

label palla_talk_politics_female:
    bree.say "I don't get the impression you're interested in politics, Palla!"
    palla.say "What makes you say that, [hero.name]?"
    bree.say "Well...you're more about making a fashion statement than a political statement, Palla!"
    palla.say "There's politics in fashion too, [hero.name]!"
    palla.say "I boycott labels that use sweatshops all the time."
    palla.say "And I also know who uses ethical and ecologically sustainable materials too!"
    palla.say "I'm not just a brainless mannequin, [hero.name]!"
    bree.say "Wow, Palla...I stand corrected!"
    $ palla.love += 1
    return

label palla_talk_food_female:
    bree.say "I guess you're pretty keen on watching what you eat, Palla?"
    bree.say "Don't want to go crazy and find nothing fits anymore, right?"
    palla.say "I wish, [hero.name]!"
    palla.say "The truth is that I LOVE my food!"
    palla.say "I just wish I could eat whatever I want without worrying!"
    bree.say "Oh, Palla...now I feel kind of sorry for you!"
    $ palla.love += 1
    return

label palla_talk_travels_female:
    bree.say "You get to do much travelling, Palla?"
    bree.say "Want to see the world?"
    palla.say "Hmm...I so do, [hero.name]!"
    palla.say "That's one of the reasons I want to make a name for myself in fashion."
    palla.say "That way I can get invited to the big events in places like France and Italy."
    palla.say "See the world and the world of fashion at the same time!"
    $ palla.love += 1
    return

label palla_talk_tv_female:
    bree.say "Watch much TV, Palla?"
    bree.say "Sometimes I feel like I'm an addict!"
    palla.say "Not really, [hero.name]."
    palla.say "There's nothing that appeals to me on there."
    palla.say "So it'd just be a waste of my time."
    return

label palla_talk_sports_female:
    bree.say "Are sports a thing you're into, Palla?"
    bree.say "I don't see there being much of a connection with fashion!"
    palla.say "Are you kidding, [hero.name]?!?"
    palla.say "Major sporting events attract the beautiful people."
    palla.say "And the beautiful people need beautiful clothes to wear."
    palla.say "When I watch sports, it's to see who's wearing who!"
    $ palla.love += 1
    return

label palla_talk_fashion_female:
    bree.say "I think my wardrobe's past its sell-by-date, Palla!"
    bree.say "You mind if I pick your brains for some tips?"
    palla.say "I'd really rather not if it's all the same to you, [hero.name]."
    palla.say "It's not that I don't have my finger on the pulse, you understand?"
    palla.say "More that I don't trust you to be able to pull off what I'd suggest."
    palla.say "No offence..."
    bree.say "Geez, Palla...you could have just said no!"
    $ palla.love -= 1
    return

label palla_talk_books_female:
    bree.say "You come across as pretty smart, Palla."
    bree.say "Are you a reader, or is it all natural?"
    palla.say "I actually read a lot, [hero.name]."
    palla.say "But it's fashion magazines, not stuffy old books!"
    palla.say "What does somebody with time to sit down and write all that know about haute couture?"
    $ palla.love -= 1
    return

label palla_talk_people_female:
    bree.say "You're pretty haughty, Palla!"
    bree.say "I get the impression you don't like people in general..."
    palla.say "That is simply not true, [hero.name]!"
    palla.say "I like the idea of people."
    palla.say "In fact, I prefer it to the reality of most human beings!"
    $ palla.love += 1
    return

label palla_talk_computers_female:
    bree.say "How are you with computers, Palla?"
    bree.say "There's something up with my laptop."
    bree.say "And I'm damned if I can figure it out!"
    palla.say "Sure, [hero.name], why not?"
    palla.say "Maybe I can look at your leaky pipes next?"
    palla.say "Or maybe fix [mike.name]'s car, huh?"
    bree.say "Erm...you're being sarcastic, aren't you, Palla?"
    bree.say "Very good, [hero.name], very observant!"
    $ palla.love -= 1
    return

label palla_talk_music_female:
    bree.say "What kind of music to the elite of the fashion world listen to, Palla?"
    bree.say "Opera?"
    bree.say "Classical music?"
    bree.say "Or is your taste as cutting edge as your clothes?"
    palla.say "Ha, ha, [hero.name]...very funny."
    palla.say "Actually I don't much care for music."
    palla.say "I find it a distraction from the fashion."
    return

label palla_talk_birthday_female:
    bree.say "Happy Birthday, Palla!"
    bree.say "I hope it's a stylish one!"
    palla.say "You...you remembered my birthday?"
    palla.say "[hero.name]...I'm really touched!"
    $ palla.love += 3
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
