label sasha_desire_0_male:
    $ result = randint(1, 5)
    if result == 1:
        sasha.say "What makes big boobs and perkiness so attractive to boys?"
        sasha.say "I mean, really. Two round, mounds of fat and a fake smile."
        sasha.say "Yeah, winning attributes."
    elif result == 2:
        sasha.say "I'm not afraid of death."
        sasha.say "I just don't want to be there when it happens."
    elif result == 3:
        mike.say "Don't you think it's a little sad to be as mean to everybody as you are?"
        sasha.say "I'm the one that's got to die when it's time for me to die, so let me live my life the way I want to."
    elif result == 4:
        mike.say "The only activity a cynic will find contagious is yawning, that is, with other people, at other people."
        sasha.say "Did you talk to me?"
    else:
        mike.say "Sasha do you have a moment?"
        sasha.say "Yeah, sure, what do you want?"
        mike.say "I chat with Sasha for a while."
    $ sasha.love += 1
    return

label sasha_desire_1_male:
    $ result = randint(1, 5)
    if result == 1:
        mike.say "Sasha looks like she wants to say something."
        $ result = renpy.display_menu([("Talk to her", 1), ("Don't talk to her", 2)])
        if result == 1:
            $ result2 = renpy.display_menu([("Tease her", 1), ("Don't tease her", 2)])
            if result2 == 1:
                if hero.charm >= 20:
                    mike.say "Someone has her panties in a twist."
                    if sasha.love < 120 - hero.charm/2:
                        sasha.say "Don't, for one minute, think that you had any effect whatsoever on my panties."
                        mike.say "Then what did I have an effect on?"
                        sasha.say "Other than my upchuck reflex, nothing."
                    else:
                        sasha.say "I am not wearing any."
                        $ sasha.sub += 2
                    $ sasha.love += 1
                else:
                    python:
                        result = randchoice(male_bad_pickup_lines)
                        for l in result:
                            if l[0] == "mc":
                                mike.say(l[1])
                            else:
                                sasha.say(l[1])
                    mike.say "She looks disgusted by my comment and leaves."
                    $ sasha.love -= 1
            else:
                mike.say "Did you see the last episode of Game of Thrones?"
                mike.say "With the sound of my voice Sasha seems to regain her composure."
                sasha.say "Not yet, but I will watch it tonight I think."
                $ sasha.love += 1
        else:
            mike.say "I just act as if I didn't notice and leave her alone."
            mike.say "For an instant it looks like she will say it, but in the end she stays silent."
            $ sasha.love += 1
    elif result == 2:
        mike.say "You know, most psychologists agree that hostility is really just sublimated sexual attraction."
        sasha.say "You wish."
        $ sasha.love += 1
    elif result == 3:
        sasha.say "You know what I don't like about you?"
        mike.say "No."
        sasha.say "You flirt with everything."
        sasha.say "You flirt with old people and babies and everybody in between."
        $ sasha.love += 1
    elif result == 4:
        sasha.say "If they substituted the word 'Lust' for 'Love' in the popular songs it would come nearer to the truth."
    else:
        sasha.say "There is a correlation between the number of days since a man last had sex, and, the number of things that he is willing to do for a woman."
    return

label sasha_desire_2_male:
    $ result = randint(1, 6)
    if result == 1:
        sasha.say "Would you say you're completely full of shit or just 50 percent?"
        mike.say "I hope just 50 but who knows."
    elif result == 2:
        sasha.say "The fear of death follows from the fear of life."
        sasha.say "A man who lives fully is prepared to die at any time."
        mike.say "You know, sometimes you are a little bit creepy."
        sasha.say "Thanks."
    elif result == 3:
        mike.say "You always talk about death..."
        sasha.say "I mean what is there in this world that truly makes living worthwhile?"
        "Sasha thinks about it."
        sasha.say "Cats, cats are nice."
    elif result == 4:
        sasha.say "Each night, when I go to sleep, I die."
        sasha.say "And the next morning, when I wake up, I am reborn."
    elif result == 5:
        mike.say "What the hell makes you smart?"
        sasha.say "I wouldn't go for coffee with you."
        mike.say "Listen - I wouldn't ask you."
        sasha.say "That, is what makes you stupid."
    else:
        mike.say "Everything in the world is about sex."
        sasha.say "Except sex."
        sasha.say "Sex is about power."
        $ sasha.sub += 1
    $ sasha.love += 1
    return

label sasha_desire_3_male:
    $ result = randint(1, 2)
    if result == 1:
        mike.say "Sasha is looking at me in an ambiguous way."
        if hero.charm >= 20:
            mike.say "Hey, Sasha looking hot today!"
            sasha.say "Well [hero.name], I am just trying very hard to attract the attention of a special someone."
            mike.say "Do I know him?"
            sasha.say "You could say that."
            $ sasha.love += 1
        else:
            python:
                result = randchoice(male_bad_pickup_lines)
                for l in result:
                    if l[0] == "mc":
                        mike.say(l[1])
                    else:
                        sasha.say(l[1])
            sasha.say "Sometimes you really know how to ruin the mood."
            mike.say "I'm not perfect, but who are we kidding, neither are you."
            $ sasha.love -= 1
    else:
        sasha.say "To answer your question, you want me because I'm made of awesome."
        mike.say "What am I going to do with you?"
        sasha.say "I have suggestions, but this might not be the place for them."
        $ sasha.love += 1

    return

label sasha_desire_4_male:
    $ result = randint(1, 4)
    if sasha.flags.mikeNickname and sasha.love >= 150:
        sasha.say "I want you to fuck me [hero.name]."
    elif result == 1:
        sasha.say "It is nothing to die."
        sasha.say "It is frightful not to live."
    elif result == 2:
        mike.say "You look beautiful sitting there spitting at me like a she-cat."
        mike.say "All I have to do is look at you, and I lust."
        mike.say "I'm going to take you to a bed and take off your clothes and fuck you until you don't have the energy to be mad at me anymore."
    elif result == 3:
        mike.say "Nice butt!"
        sasha.say "I can't believe what I'm hearing here."
        mike.say "What? I-I said you had a-"
        sasha.say "My butt is not just nice! It's great."
        mike.say "I said that you had a nice butt, it's just not a great butt."
        sasha.say "Oh, you wouldn't know a great butt if it came up and bit ya."
        mike.say "There's an image."
    else:
        sasha.say "Oh no."
        sasha.say "Don't smile."
        sasha.say "You'll kill me."
        sasha.say "I stop breathing when you smile."
    $ sasha.love += 1
    return

label sasha_desire_5_male:
    if sasha.flags.mikeNickname and sasha.love >= 150:
        sasha.say "I need your cock [hero.name]."
    elif hero.fitness > 20:
        sasha.say "Fuck, you are hot..."
        mike.say "Well, thank you."
        if hero.knowledge < 19:
            sasha.say "But yor brain is rotten."
            if hero.charm < 19:
                sasha.say "And you really don't know how to talk to a woman."
            mike.say "Oookay..."
        else:
            sasha.say "And smart too."
            if hero.charm < 19:
                sasha.say "And you really don't know how to talk to a woman."
                mike.say "Oookay..."
            else:
                sasha.say "And you really know how to talk to a woman."
                mike.say "Thanks I guess..."
    else:
        sasha.say "I really have no idea why I want to fuck you so much..."
        if hero.fitness < 19:
            sasha.say "You are a slob..."
        if hero.knowledge < 19:
            sasha.say "You are stupid."
        if hero.charm < 19:
            sasha.say "And you really don't know how to talk to a woman."
        mike.say "Oookay...maybe we just have good chemistry."
        sasha.say "Or I am becoming increasingly crazy."
    $ sasha.love += 1
    return

label sasha_love_0_male:
    $ result = randint(1, 5)
    if result == 1:
        sasha.say "Never trust people who smile constantly."
        sasha.say "They're either selling something or not very bright."
    elif result == 2:
        sasha.say "I want to scream sometimes, because I hate when people refer to a dead person as the 'late' so and so."
        sasha.say "I'm sorry to break that bad news, but that person isn't just late—they're not even coming!"
    elif result == 3:
        mike.say "Love is a circular emotion that surrounds you, like a hug."
        sasha.say "Or a noose."
    elif result == 4:
        sasha.say "My goal in life is to have a psychiatric disorder named after me."
        mike.say "You are on the right path."
    else:
        sasha.say "I can't decide whether I'm a good girl wrapped up in a bad girl, or if I'm a bad girl wrapped up in a good girl."
        sasha.say "And that's how I know I'm a woman!"
    $ sasha.love += 1
    return

label sasha_love_1_male:
    $ result = randint(1, 5)
    if result ==1:
        "I smile to Sasha."
        mike.say "If you weren't so psychotic, you'd be fun to hang around."
        sasha.say "Funny, I feel that way about you too."
        "She doesn't say anything else, but walks away with a grin on her face."
        $ sasha.love += 1
    elif result == 2:
        if bree.love >= 120 - hero.charm/2 and sasha.love >= 120 - hero.charm/2:
            sasha.say "So, I have seen how [bree.name] looks at you."
            mike.say "How?"
            sasha.say "Come on, you bask in the light of her smile like it's the sun."
            mike.say "Well, maybe I enjoy it a little."
            sasha.say "She's cute, You know, in a little girl or motherly kind of way."
            sasha.say "But you don't need to like a girl who treats you like you're ten: You've already got a mom."
            sasha.say "Just saying..."
            $ sasha.love += 1
        else:
            sasha.say "You know what?"
            mike.say "What?"
            sasha.say "Sex without love is a meaningless experience, but as far as meaningless experiences go its pretty damn good."
            mike.say "Should I take that as an invitation?"
            if sasha.love > 120 - hero.charm/2:
                sasha.say "More like an order."
            elif sasha.love > 80 - hero.charm/2:
                sasha.say "Maybe."
                $ sasha.sub += 1
            else:
                sasha.say "You wish."
            $ sasha.love += 1
    elif result == 3:
        sasha.say "I consider conversations with people to be mind exercises but I don't want to pull a muscle, so I stretch a lot."
        sasha.say "That's why I'm constantly either rolling my eyes or yawning."
        $ sasha.love += 1
    elif result == 4:
        sasha.say "I am free of all prejudice."
        sasha.say "I hate everyone equally."
        $ sasha.love += 1
    else:
        if sasha.love > 80 - hero.charm/2:
            sasha.say "So, we should talk about the complex issues of our times."
            sasha.say "Can men and women really be friends or do you secretly want to bang Samantha?"
            $ result = renpy.display_menu([("Yes", 1), ("Maybe", 2), ("No", 3)])
            if result == 1:
                mike.say "Is it that obvious?"
                sasha.say "I can't blame you, with that ass even I have a boner."
                $ sasha.love += 1
            elif result == 2:
                mike.say "She has a boyfriend."
                $ sasha.love -= 1
            elif result == 3:
                mike.say "We are just friends."
                sasha.say "Maybe you have someone else in mind."
                $ sasha.love += 1
        else:
            mike.say "If you could have any super power what would it be?"
            sasha.say "The power to make you interesting."
            $ sasha.love += 1
    return

label sasha_love_2_male:
    if hero.fun < 5:
        sasha.say "You look depressed."
        mike.say "Yeah, I am a little..."
        sasha.say "...Cheer up?"
        mike.say "Thx, but you really are no good at this..."
        $ sasha.love -= 1
    elif not sasha.flags.birthdayknown:
        mike.say "Hey Sasha, when is your birthday?"
        sasha.say "It's on the [sasha.birthday[1]] of [sasha.birthday[0]]."
        sasha.say "Are you planning on getting me a gift?"
        mike.say "Maybe..."
        $ sasha.flags.birthdayknown = True
        $ sasha.love += 1
    else:
        mike.say "So what's your excuse?"
        sasha.say "For?"
        mike.say "Acting the way we do."
        sasha.say "I don't like to do what people expect."
        sasha.say "Why should I live up to other people's expectations instead of my own?"
        mike.say "So you disappoint them from the start and then you're covered, right?"
        sasha.say "Something like that."
        mike.say "Then you screwed up!"
        sasha.say "How?"
        mike.say "You never disappointed me."
        $ sasha.love += 1
    return

label sasha_love_3_male:
    if hero.grooming < 3:
        sasha.say "You could, you know..."
        sasha.say "Shower a little?"
        $ sasha.love -= 1
    else:
        if randint(1, 2) == 1:
            sasha.say "You know, I lost my mother at a young age."
            mike.say "Sorry to hear that."
            sasha.say "Yeah, she went out to get cigarettes and I never found her again."
        else:
            sasha.say "I have chosen the path of the black sheep rather than that of the unicorns and puppies."
            mike.say "If you are talking about those flesh eating sheep, then yes it does seem a lot like you."
        $ sasha.love += 1

    return

label sasha_love_4_male:
    mike.say "Sasha, I barely seem to see you smile..."
    sasha.say "It's because you are barely funny."
    mike.say "I'll take that verbal abuse as a token of our friendship."
    sasha.say "You should, I don't bother abusing people I am not interested in."
    mike.say "Maybe I should abuse you then?"
    if sasha.flags.mikeNickname and sasha.love >= 150:
        sasha.say "Please do [hero.name]."
    $ sasha.love += 1
    return

label sasha_love_5_male:
    sasha.say "I never thought we could become that good friends."
    if sasha.is_collared and sasha.love >= 150:
        mike.say "You're not my friend you are my prized sex slave."
    else:
        mike.say "Or would you say, if you were capable of feelings."
    $ sasha.love += 1
    return

label sasha_good_sweet_talk_male:
    show sasha
    if sasha.love > 133:
        mike.say "Hey, Sasha - you rock!"
        mike.say "And you make me hard as one too!"
        show sasha blush
        sasha.say "Oh, man - that's really cringe!"
        sasha.say "But I love you all the same!"
    elif sasha.love > 66:
        mike.say "You look so good in that outfit, Sasha."
        mike.say "I love being seen with you."
        show sasha happy
        sasha.say "Thanks for the compliment!"
    else:
        mike.say "You're so cool, Sasha."
        mike.say "Always turning me onto new music."
        mike.say "And well, just being great in general!"
        sasha.say "Thanks, man!"
        sasha.say "You're pretty cool too."
    hide sasha
    return

label sasha_bad_sweet_talk_male:
    show sasha
    mike.say "You might wear black and mope about, Sasha."
    mike.say "But you're actually a lot of fun underneath it all!"
    show sasha angry
    sasha.say "It's not moping around, you jerk!"
    sasha.say "It's called being deep and in touch with your inner self!"
    mike.say "Erm...okay, Sasha..."
    hide sasha
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
