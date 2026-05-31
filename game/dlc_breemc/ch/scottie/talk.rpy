label scottie_talk_love_female:
    show scottie
    if randint(0, 1) == 0:
        bree.say "You believe in love, right Scottie?"
        scottie.say "Love...seriously?"
        if scottie.sub <= 25:
            $ scottie.sub -= 1
            scottie.say "The only thing you should worry about loving is having my cock inside of you!"
            menu:
                "I like that idea" if hero.morality <= 25:
                    "Sounds like a plan!"
                    $ scottie.love += 1
                    $ scottie.sub -= 1
                "Just fuck off":
                    "You really are a pig, asshole..."
                    $ scottie.sub += 1
                    $ scottie.love -= 1
        elif scottie.sub >= 75:
            scottie.say "I know that I love it when you give me an order!"
            $ scottie.sub += 1
    else:
        bree.say "I think it's important for a guy to be deep, Scottie."
        bree.say "That's how a girl really knows that she can believe in him."
        bree.say "And...maybe...even fall in love with him!"
        scottie.say "Urgh...boring!"
        scottie.say "I know what a girl wants, [hero.name]."
        scottie.say "And it's length, not depth!"
        $ scottie.love -= 1
    hide scottie
    return

label scottie_talk_sex_female:
    show scottie
    if randint(0, 1) == 0:
        bree.say "What about sex, Scottie - are you spontaneous, or do you like to plan ahead?"
        if scottie.love <= 25:
            scottie.say "You better put out when and where I say, bitch!"
            menu:
                "Of course!" if hero.morality <= 25:
                    "Of course love!"
                    $ scottie.love += 1
                    $ scottie.sub -= 1
                "Just fuck off":
                    "You really are a pig, asshole..."
                    $ scottie.sub += 1
                    $ scottie.love -= 1
        elif scottie.sub >= 75:
            scottie.say "Yes...ready and willing to please."
            $ scottie.sub += 1
        else:
            scottie.say "I'm cool with whenever and wherever you want babe."
    else:
        bree.say "I love that you're so upbeat, Scottie."
        bree.say "It's like I could talk to you about anything."
        bree.say "Music, movies...even sex!"
        scottie.say "Especially the sex, babe, especially the sex!"
        scottie.say "In fact, what else is there to talk about?"
        $ scottie.love += 1
    hide scottie
    return

label scottie_talk_politics_female:
    show scottie
    if randint(0, 1) == 0:
        bree.say "I'm not sure who to vote for in the local elections this year."
        if scottie.love <= 25:
            scottie.say "What are you wasting your time on that stuff for?"
            scottie.say "If I wanted you to have an opinion on politics, I'd have told you what it should be already!"
            menu:
                "Of course!" if hero.morality <= 25:
                    "Of course love!"
                    $ scottie.love += 1
                    $ scottie.sub -= 1
                "Just fuck off":
                    "You really are a pig, asshole..."
                    $ scottie.sub += 1
                    $ scottie.love -= 1
        elif scottie.sub >= 75:
            scottie.say "I wouldn't know about any of that...would you like to tell me who to vote for?"
            $ scottie.sub += 1
        else:
            scottie.say "Meh, I'm not that interested in politics and all that kind of stuff."
    else:
        bree.say "Did you see what that scumbag politician did today?"
        bree.say "And it looks like he's going to get away with it again!"
        scottie.say "Erm, no, [hero.name]."
        scottie.say "I don't DO politics, not at all!"
        bree.say "Don't you think that's a little irresponsible, Scottie?"
        scottie.say "I try not to think at all, [hero.name]."
        scottie.say "That usually does the trick!"
        $ scottie.love -= 1
    hide scottie
    return

label scottie_talk_food_female:
    show scottie
    if randint(0, 1) == 0:
        if scottie.love <= 25:
            scottie.say "Well don't be a dumbass - make us something or else order it in!"
            scottie.say "God, I have to tell you to do every damn thing."
            menu:
                "Of course!" if hero.morality <= 25:
                    "Of course love!"
                    $ scottie.love += 1
                    $ scottie.sub -= 1
                "Just fuck off":
                    "You really are a pig, asshole..."
                    $ scottie.sub += 1
                    $ scottie.love -= 1
        elif scottie.sub >= 75:
            scottie.say "You should have told me earlier!"
            scottie.say "I could knock you something up myself, or should I order you take-out?"
            $ scottie.sub += 1
        else:
            bree.say "I'm getting kinda hungry."
            scottie.say "Me too - say, you wanna cook something for me?"
    else:
        bree.say "Hmm..."
        bree.say "I think my stomach is rumbling."
        bree.say "Time for a snack!"
        bree.say "You want something too, Scottie?"
        scottie.say "You mean food, [hero.name]?"
        scottie.say "You're offering to make me food?"
        bree.say "Erm...yeah!"
        scottie.say "[hero.name], did I ever tell you that I love you?"
    hide scottie
    return

label scottie_talk_travels_female:
    show scottie
    if randint(0, 1) == 0:
        bree.say "I really wonder if I'm missing out by not travelling more..."
        if scottie.love <= 25 and scottie.sub <= 25:
            scottie.say "You're going nowhere without me or my say so!"
            menu:
                "Of course!" if hero.morality <= 25:
                    "Of course love!"
                    $ scottie.love += 1
                    $ scottie.sub -= 1
                "Just fuck off":
                    "You really are a pig, asshole..."
                    $ scottie.sub += 1
                    $ scottie.love -= 1
        elif scottie.sub >= 75:
            scottie.say "Are you planning to go away?!?"
            scottie.say "Please, take me with you - don't leave me!"
            $ scottie.sub += 1
        else:
            scottie.say "Hey, baby - I can take you someplace fun without leaving the room!"
    else:
        bree.say "I want a holiday this year."
        bree.say "But I want to go somewhere special."
        bree.say "Any ideas, Scottie?"
        scottie.say "The beach?"
        bree.say "Erm...the beach is right here, doofus!"
        scottie.say "That's why I said it, [hero.name]."
        scottie.say "You could save money by having a holiday at home."
        bree.say "Forget it, Scottie..."
    $ scottie.love += 1
    hide scottie
    return

label scottie_talk_tv_female:
    show scottie
    if randint(0, 1) == 0:
        bree.say "I fancy watching a documentary tonight - how about you?"
        if scottie.sub <= 25:
            scottie.say "If by that you mean a show where guys buy a car, fix it and then sell to other guys, then okay."
            scottie.say "Anything else and you can forget it."
            menu:
                "Of course!" if hero.morality <= 25:
                    "Of course love!"
                    $ scottie.love += 1
                    $ scottie.sub -= 1
                "Just fuck off":
                    "You really are a pig, asshole..."
                    $ scottie.sub += 1
                    $ scottie.love -= 1
        elif scottie.sub >= 75:
            scottie.say "Whatever you want."
            scottie.say "If I like your choice, then great."
            scottie.say "If not, then I can just keep my mouth shut the whole time."
            $ scottie.sub += 1
        else:
            scottie.say "I love that show where they fix cars."
            scottie.say "You know, the one with the guy that's got the beard and the other with the hair?"
    else:
        bree.say "You want to watch some TV, Scottie?"
        scottie.say "Ah...no, [hero.name], I'll pass."
        scottie.say "Your shows are always kinda boring!"
        bree.say "What do you mean?"
        bree.say "I like to watch crime dramas and sci-fi!"
        scottie.say "Yeah, but would it hurt them to blow more stuff up?"
        scottie.say "And maybe have one little monster truck race?"
    hide scottie
    return

label scottie_talk_sports_female:
    show scottie
    if randint(0, 1) == 0:
        bree.say "I'm thinking of taking up some sports classes at the gym."
        if scottie.sub <= 25:
            scottie.say "You can exercise here, in front of me."
            scottie.say "It's cheaper, and plus, I get a free floor-show."
            menu:
                "Of course!" if hero.morality <= 25:
                    "Of course love!"
                    $ scottie.love += 1
                    $ scottie.sub -= 1
                "Just fuck off":
                    "You really are a pig, asshole..."
                    $ scottie.sub += 1
                    $ scottie.love -= 1
        elif scottie.sub >= 75:
            scottie.say "You don't need to shape up - you're perfect, just as you are."
            $ scottie.sub += 1
        else:
            scottie.say "Good idea - you need to stay in shape, can't let that body of your go getting all flabby now."
    else:
        bree.say "Oh, I heard that the local sports team won last night."
        bree.say "Sorry, but I don't know which one it was."
        bree.say "Or who they were playing..."
        bree.say "Or what the score was!"
        scottie.say "Who cares - we won, that's what counts!"
        scottie.say "Take that, you fucking losers!"
    hide scottie
    return

label scottie_talk_fashion_female:
    show scottie
    if randint(0, 1) == 0:
        bree.say "What do you think of this season's trends, Scottie?"
        if scottie.sub <= 25:
            scottie.say "What do you care?"
            scottie.say "If I like something, then you wear it."
            scottie.say "If not, then you don't."
            scottie.say "Simple as."
            menu:
                "Of course!" if hero.morality <= 25:
                    "Of course love!"
                    $ scottie.love += 1
                    $ scottie.sub -= 1
                "Just fuck off":
                    "You really are a pig, asshole..."
                    $ scottie.sub += 1
                    $ scottie.love -= 1
        elif scottie.sub >= 75:
            scottie.say "You look great in whatever you wear!"
            $ scottie.sub += 1
        else:
            scottie.say "Don't care - as far as I'm concerned, the less a girl wears the better."
    else:
        bree.say "Do you ever think about expanding your wardrobe, Scottie?"
        bree.say "You know, like maybe buying a shirt that's not a band T-shirt?"
        bree.say "Even wearing something with sleeves once in a while?"
        scottie.say "No way, baby!"
        scottie.say "I've been rocking this style since I was in high-school."
        scottie.say "And there's no way I'm stopping now!"
    $ scottie.love += 1
    hide scottie
    return

label scottie_talk_books_female:
    show scottie
    if randint(0, 1) == 0:
        bree.say "What's your favourite book, Scottie?"
        if scottie.sub <= 25:
            scottie.say "I don't want you reading anything without my say so from now on."
            scottie.say "Can't have you getting any crazy ideas into your head."
            menu:
                "Of course!" if hero.morality <= 25:
                    "Of course love!"
                    $ scottie.love += 1
                    $ scottie.sub -= 1
                "Just fuck off":
                    "You really are a pig, asshole..."
                    $ scottie.sub += 1
                    $ scottie.love -= 1
        elif scottie.sub >= 75:
            scottie.say "I don't read because big words always confuse me..."
            $ scottie.sub += 1
        else:
            scottie.say "Never read one in my life - books are so boring it's unreal."
    else:
        bree.say "I read a really great book about rock in the eighties, Scottie."
        bree.say "It was full of stories about bands like Metallikea and ByJovi."
        bree.say "Would you like to read it?"
        scottie.say "Erm...is there a comic-book version out yet?"
        scottie.say "Because that's really more my kind of thing!"
    $ scottie.love -= 1
    hide scottie
    return

label scottie_talk_people_female:
    show scottie
    if randint(0, 1) == 0:
        bree.say "What's your philosophy for getting on with people, Scottie?"
        if scottie.sub <= 25:
            scottie.say "Fuck other people - and you shouldn't be talking to anyone, unless I say you can!"
            menu:
                "Of course!" if hero.morality <= 25:
                    "Of course love!"
                    $ scottie.love += 1
                    $ scottie.sub -= 1
                "Just fuck off":
                    "You really are a pig, asshole..."
                    $ scottie.sub += 1
                    $ scottie.love -= 1
        elif scottie.sub >= 75:
            scottie.say "I'm scared that people will see through my bravado and say mean things that I won't understand."
            $ scottie.sub += 1
        else:
            scottie.say "I don't have one."
            scottie.say "Fuck them all, that's what I say!"
    else:
        bree.say "A customer was a real jerk to me at work today, Scottie."
        bree.say "You know, sometimes I really hate the human race!"
        scottie.say "Whoa...that's a little heavy, [hero.name]!"
        bree.say "I...I suppose you're right."
        scottie.say "Of course I am, babe."
        scottie.say "You just got to put out positive vibes, yeah?"
        scottie.say "People are more positive when you're positive!"
        bree.say "Wow...that actually makes sense!"
        bree.say "Thanks, Scottie."
    hide scottie
    return

label scottie_talk_computers_female:
    show scottie
    if randint(0, 1) == 0:
        bree.say "You much into computers, Scottie?"
        if scottie.sub <= 25:
            scottie.say "What the hell are you doing on the internet, anyway?"
            scottie.say "There are other guys on there - so you keep off of it, you hear?"
            menu:
                "Of course!" if hero.morality <= 25:
                    "Of course love!"
                    $ scottie.love += 1
                    $ scottie.sub -= 1
                "Just fuck off":
                    "You really are a pig, asshole..."
                    $ scottie.sub += 1
                    $ scottie.love -= 1
        elif scottie.sub >= 75:
            scottie.say "Computers scare me, because I'm afraid that I'll break them..."
            $ scottie.sub += 1
        else:
            scottie.say "Nah...not interested."
    else:
        bree.say "How are you getting on with that old laptop I gave you, Scottie?"
        bree.say "I know it's not the best you can get, but it's better than nothing, right?"
        scottie.say "No, [hero.name] - it's a fucking nightmare!"
        scottie.say "I swear that thing's cursed!"
        scottie.say "Why do computers have to be so complicated?"
        scottie.say "Just thinking about them makes my head hurt!"
    $ scottie.love -= 1
    hide scottie
    return

label scottie_talk_music_female:
    show scottie
    if randint(0, 1) == 0:
        bree.say "What's on your playlist, Scottie?"
        if scottie.sub <= 25:
            scottie.say "Metal, metal and more metal - so you'd better get to like it!"
            menu:
                "Of course!" if hero.morality <= 25:
                    "Of course love!"
                    $ scottie.love += 1
                    $ scottie.sub -= 1
                "Just fuck off":
                    "You really are a pig, asshole..."
                    $ scottie.sub += 1
                    $ scottie.love -= 1
        elif scottie.sub >= 75:
            scottie.say "I like K-Pop, but I always say metal, because I'm scared people will call me a pussy..."
            $ scottie.sub += 1
        else:
            scottie.say "Gotta be metal, all the way baby!"
    else:
        bree.say "I hate to say it, Scottie - but you were right!"
        bree.say "That album you lent me was amazing!"
        bree.say "How have I gone this long without discovering it?"
        scottie.say "This is how things are when you know, Scottie!"
        scottie.say "Magical things start to happen for you, [hero.name]!"
    hide scottie
    return

label scottie_talk_birthday_female:
    show scottie
    if randint(0, 1) == 0:
        bree.say "Happy birthday, Scottie."
        scottie.say "Hey, thanks babe!"
        if scottie.sub <= -25:
            scottie.say "I am gonna fuck your ass then your mouth to celebrate!"
        elif scottie.sub <= 25:
            scottie.say "Can I get a blowjob as my present?"
        if scottie.sub <= 25:
            menu:
                "Of course!" if hero.morality <= 25:
                    "Of course love!"
                    $ scottie.love += 1
                    $ scottie.sub -= 1
                "Just fuck off":
                    "You really are a pig, asshole..."
                    $ scottie.sub += 1
                    $ scottie.love -= 1
    else:
        bree.say "Happy Birthday, Scottie!"
        bree.say "Hope you have a good one!"
        scottie.say "Wait...what?!?"
        scottie.say "It's not my birthday!"
        bree.say "Erm...you told me it was today."
        scottie.say "Did I?"
        scottie.say "Oh yeah - sometimes I forget the date myself!"
    $ scottie.love += 3
    hide scottie
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
