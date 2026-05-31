label sasha_talk_love_male:
    show sasha
    $ result = randint(1, 5)
    if sasha.flags.mikeNickname and sasha.love >= 150:
        show sasha blush
        sasha.say "I love you [hero.name]."
    elif result == 1:
        mike.say "Why don't they ever a make a movie about what happens after they kiss?"
        show sasha joke
        sasha.say "They do, it's called porn."
    elif result == 2 and sasha.love > 80 - hero.charm/2:
        sasha.say "Have you ever been in love?"
        mike.say "Sure."
        show sasha annoyed
        sasha.say "Horrible isn't it?"
        mike.say "Why?"
        sasha.say "It makes you so vulnerable."
        sasha.say "It opens your chest and it opens up your heart and it means that someone can get inside you and mess you up."
        $ sasha.sub += 1
        $ sasha.love += 1
    elif result == 3:
        show sasha joke
        sasha.say "There is only one thing worse than a boy who hates you: a boy that loves you."
    elif result == 4:
        sasha.say "You're not gay, are you?"
        mike.say "If I were, I would dress better."
    else:
        mike.say "Why do women think the only way to get men to do what they want is to manipulate them?"
        sasha.say "Lot's of reason, really : "
        show sasha annoyed
        sasha.say "History, personal experience, romantic comedies."
    $ sasha.love += 1
    hide sasha
    return

label sasha_talk_sex_male:
    show sasha
    $ result = randint(1, 5)
    if sasha.flags.mikeNickname and sasha.love >= 150:
        show sasha blush
        sasha.say "Please use me anyway you want [hero.name]."
    elif result == 1:
        mike.say "Why did God give men penises?"
        show sasha happy
        sasha.say "So they'd have at least one way to shut a woman up."
    elif result == 2:
        sasha.say "Which of the following words does not belong: meat, eggs, wife, blowjob."
        mike.say "Blowjob. You can beat your meat, eggs, and wife; but you can't beat a blowjob."
    elif result == 3:
        sasha.say "How do you circumcise a hillbilly?"
        mike.say "I don't know."
        show sasha happy
        sasha.say "Kick his sister in the jaw."
    elif result == 4:
        sasha.say "I don't know the question, but sex is definitely the answer."
    else:
        mike.say "What is the difference between oral and anal sex?"
        sasha.say "Dunno..."
        mike.say "Oral sex makes your day and Anal sex makes your whole week."
        $ sasha.sub += 1
    $ sasha.love += 1
    hide sasha
    return

label sasha_talk_politics_male:
    show sasha angry
    sasha.say "You're not to be so blind with patriotism that you can't face reality."
    sasha.say "Wrong is wrong, no matter who does it or says it."
    $ sasha.love -= 1
    hide sasha
    return

label sasha_talk_food_male:
    show sasha
    sasha.say "I don't understand dieting."
    sasha.say "Seize the moment."
    show sasha happy
    sasha.say "Remember all those women on the 'Titanic' who waved off the dessert cart."
    $ sasha.love += 1
    hide sasha
    return

label sasha_talk_travels_male:
    show sasha
    sasha.say "Not all journeys seek an end."
    sasha.say "Some are their own purpose."
    $ sasha.love += 2
    hide sasha
    return

label sasha_talk_tv_male:
    show sasha
    sasha.say "To attract a lover, you need to craft the perfect Craigslist ad."
    show sasha joke
    sasha.say "Here's mine: Free TV with purchase of potato chips and couch."
    if hero.charm >= 25:
        $ sasha.sub += 1
    $ sasha.love += 1
    hide sasha
    return

label sasha_talk_sports_male:
    show sasha joke
    mike.say "The problem with winter sports is that -- follow me closely here -- they generally take place in winter."
    $ sasha.love += 2
    hide sasha
    return

label sasha_talk_fashion_male:
    show sasha happy
    $ result = randint(1, 10)
    if result == 1:
        sasha.say "You can never be overdressed or over educated."
    elif result == 2:
        sasha.say "A girl should be two things: classy and fabulous."
    elif result == 3:
        sasha.say "I don't know who invented high heels, but all women owe him a lot!"
    elif result == 4:
        sasha.say "Dress shabbily and they remember the dress; dress impeccably and they remember the woman."
    elif result == 5:
        sasha.say "The most beautiful makeup of a woman is passion. But cosmetics are easier to buy."
    elif result == 6:
        sasha.say "I love new clothes."
        sasha.say "If everyone could just wear new clothes everyday, I reckon depression wouldn't exist anymore."
    elif result == 7:
        sasha.say "A woman who doesn't wear perfume has no future."
    elif result == 8:
        sasha.say "Whoever said that money can't buy happiness, simply didn't know where to go shopping."
    elif result == 9:
        sasha.say "A woman's dress should be like a barbed-wire fence: serving its purpose without obstructing the view."
    elif result == 10:
        sasha.say "It's a good thing I was born a girl, otherwise I'd be a drag queen."
    $ sasha.love += 1
    hide sasha
    return

label sasha_talk_books_male:
    show sasha annoyed
    if hero.knowledge > 20 and sasha.love > 40:
        sasha.say "You get a little moody sometimes but I think that's because you like to read."
        sasha.say "People that like to read are always a little fucked up."
    else:
        mike.say "If you go home with somebody, and they don't have books, don't fuck 'em!"
    $ sasha.love -= 1
    hide sasha
    return

label sasha_talk_people_male:
    show sasha
    mike.say "I love women, but I feel like you can't trust some of them. Some of them are liars, you know?"
    mike.say "Like I was in the park and I met this girl, she was cute and she had a dog."
    mike.say "And I went up to her, we started talking. She told me her dog's name."
    show sasha happy
    mike.say "Then I said, 'Does he bite?' She said, 'No.' And I said, 'Oh yeah? Then how does he eat?' Liar."
    $ sasha.love += 1
    hide sasha
    return

label sasha_talk_computers_male:
    show sasha annoyed
    sasha.say "I think computer viruses should count as life ..."
    sasha.say "I think it says something about human nature that the only form of life we have created so far is purely destructive."
    sasha.say "We've created life in our own image."
    $ sasha.love -= 1
    hide sasha
    return

label sasha_talk_music_male:
    show sasha
    if randint(1, 2) == 1:
        sasha.say "Pop and metal aren't friends."
        sasha.say "Each knows exactly where the other lives and tries to keep its distance."
        sasha.say "They choose different streets, neighborhoods, zip codes."
    else:
        sasha.say "Heavy Metal would not exist without Led Zeppelin, and if it did, it would suck."
    $ sasha.love += 1
    hide sasha
    return

label sasha_talk_birthday_male:
    show sasha
    mike.say "Happy birthday Sasha."
    show sasha happy
    sasha.say "Thank you!"
    $ sasha.love += 5
    hide sasha
    return

init:
    define nickname_dumbass = ["Dumbass", "dumbass"]
    define nickname_idiot = ["Idiot", "idiot"]
    define nickname_chad = ["Chad", "chad"]
    define nickname_boo = ["Boo", "boo"]
    define nickname_fuck_face = ["Fuck Face", "fuck face"]
    define nickname_my_big_bear = ["My Big Bear", "my big bear"]

label command_nickname_sasha:
    menu:

        "Call me Dumbass" if active_girl.flags.mikeNickname not in nickname_dumbass and active_girl.love > 100:
            $ active_girl.flags.mikeNickname = "Dumbass"
        "Stop calling me Dumbass" if active_girl.flags.mikeNickname in nickname_dumbass:
            $ active_girl.flags.mikeNickname = None


        "Call me Idiot" if active_girl.flags.mikeNickname not in nickname_idiot and active_girl.love > 100:
            $ active_girl.flags.mikeNickname = "Idiot"
        "Stop calling me Idiot" if active_girl.flags.mikeNickname in nickname_idiot:
            $ active_girl.flags.mikeNickname = None


        "Call me Chad" if active_girl.flags.mikeNickname not in nickname_chad and hero.fitness > 70:
            $ active_girl.flags.mikeNickname = "Chad"
        "Stop calling me Chad" if active_girl.flags.mikeNickname in nickname_chad:
            $ active_girl.flags.mikeNickname = None


        "Call me Boo" if active_girl.flags.mikeNickname not in nickname_boo:
            $ active_girl.flags.mikeNickname = "Boo"
        "Stop calling me Boo" if active_girl.flags.mikeNickname in nickname_boo:
            $ active_girl.flags.mikeNickname = None


        "Call me Fuck Face" if active_girl.flags.mikeNickname not in nickname_fuck_face and active_girl.sub > 80:
            $ active_girl.flags.mikeNickname = "Fuck Face"
        "Stop calling me Fuck Face" if active_girl.flags.mikeNickname in nickname_fuck_face:
            $ active_girl.flags.mikeNickname = None


        "Call me My Big Bear" if active_girl.flags.mikeNickname not in nickname_my_big_bear and active_girl.love > 120:
            $ active_girl.flags.mikeNickname = "My Big Bear"
        "Stop calling me My Big Bear" if active_girl.flags.mikeNickname in nickname_my_big_bear:
            $ active_girl.flags.mikeNickname = None
        "Cancel":


            jump command_girl

label submissive_interact_sasha_male:
    mike.say "Hey, Sasha..."
    mike.say "I was thinking - maybe we should have a special way of saying hi?"
    show sasha surprised
    sasha.say "Huh?!?"
    show sasha shout
    sasha.say "You mean like say it in a different language or something?"
    show sasha normal
    mike.say "No, I was meaning something personal, that's unique to us."
    mike.say "Like you could say that I rock you harder than heavy metal, yeah?"
    if sasha.sub >= 70 or sasha.is_sex_slave:
        show sasha happy
        sasha.say "Whoa...that's SO cheesy, [hero.name]!"
        show sasha shout blush
        sasha.say "But it is kind of cute too."
        sasha.say "Okay, okay - I'll try to think of something."
        $ sasha.flags.submissive_interact = True
    else:
        show sasha vangry
        sasha.say "Wow...that is SO lame, [hero.name]!"
        sasha.say "You want me to get your name tattooed on my ass too?!?"
        show sasha annoyed
        mike.say "Well...when you put it like that, Sasha..."
        mike.say "Maybe we forget about it, okay?"
        $ sasha.love -= 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
