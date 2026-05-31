label bree_talk_love_male:
    show bree
    $ result = randint(1, 8)
    if bree.is_collared and bree.love >= 150:
        show bree flirt
        bree.say "I love you [hero.name]."
        bree.say "Will you have the time to fuck your little pet today?"
    elif result == 1:
        show bree sad
        bree.say "I am ugly."
        if hero.charm >= 20:
            $ result = renpy.display_menu([("Agree", 1), ("Disagree", 2), ("Joke", 3)])
        else:
            $ result = 1
        if result == 1:
            mike.say "On that we agree."
            show bree angry
            "[bree.name] looks hurt by my answer."
            bree.say "Jackass."
            $ bree.love -= 2
        elif result == 2:
            mike.say "I am pregnant."
            show bree surprised
            bree.say "What???"
            mike.say "I thought we were stating impossible things."
            show bree happy
            "[bree.name] smiles at my pathetic joke."
            bree.say "Thx."
            $ bree.love += 1
        else:
            mike.say "You are insulting my tastes."
            show bree surprised
            bree.say "?"
            mike.say "I wouldn't have an ugly sex slave."
            show bree happy
            bree.say "LOL!"
            $ bree.sub += 1
    elif result == 2:
        bree.say "It's very easy to be cynical about love until you've had that instant connection. If you're lucky, it happens once in a lifetime."
        if hero.charm >= 20:
            $ result = renpy.display_menu([("Agree", 1), ("Disagree", 2), ("Joke", 3)])
        else:
            $ result = 2
        if result == 1:
            mike.say "I hope it will happen to me sometime."
            $ bree.love += 1
        elif result == 2:
            mike.say "What a load of crap."
            show bree sad
            "[bree.name] looks very sad at my answer."
            $ bree.love -= 1
        else:
            mike.say "Your describing a sex slave's relationship to her master."
            show bree blush
            "[bree.name] blushes madly."
            $ bree.sub += 1
    elif result == 3:
        bree.say "Can't you say something deep and meaningful for once?"
        if hero.knowledge >= 10:
            $ result = renpy.display_menu([("Joke", 2), ("Be serious", 1)])
        else:
            $ result = 2
        if result == 1:
            mike.say "You've gotta dance like there's nobody watching,\nLove like you'll never be hurt."
            mike.say "Sing like there's nobody listening,\nAnd live like it's heaven on earth."
            show bree flirt
            bree.say "Okay, that will do."
            $ bree.love += 1
        else:
            mike.say "Bet you 100 quid you can't turn me hetero."
            show bree annoyed
            "[bree.name] looks pissed and leave me there."
            $ bree.love -= 1
    elif result == 4:
        bree.say "What is true love?"
        if hero.charm >= 20:
            if bree.love >= 50:
                mike.say "True love is finding someone who matches you kink for kink."
                mike.say "I for once want to find a woman that I can slap and choke in bed but still cuddle in the morning."
                show bree flirt
                bree.say "It's oddly hot."
                $ bree.sub += 1
            else:
                mike.say "True love is your soul's recognition of its counterpoint in another."
                show bree happy
                bree.say "It's a little cheesy but I like it."
                mike.say "I read it on a bumper sticker!"
                $ bree.love += 2
        else:
            mike.say "I really don't know."
    elif result == 5:
        show bree blush
        bree.say "You know you're in love when you can't fall asleep because reality is finally better than your dreams."
        $ bree.love += 1
    elif result == 6:
        mike.say "If you can make a woman laugh, you can make her do anything."
        $ bree.love += 1
    elif result == 7:
        bree.say "Do you want a happy ending?"
        mike.say "True love stories don't have endings."
        $ bree.love += 1
    else:
        show bree sad
        bree.say "I know what's in store for me. No one will ever have passion for me."
        bree.say "People all around me will be falling in love, and making love, and getting married and having kids."
        bree.say "The closest thing I'll ever have to that is someone inviting me to their Christmas dinner because they feel guilty I might be spending the holiday alone."
        bree.say "Or if I'm lucky, my male counterpart, an obese man or a guy with a harelip, will invite me to coffee; and we'll pretend to love each other and tie the knot because we're so desperately afraid of growing old alone."
        if hero.charm >= 20:
            show bree normal
            mike.say "I better get to eating more pizza then..."
            show bree blush
            mike.say "I need to get fat quick."
            $ bree.love += 1
        else:
            mike.say "..."
            $ bree.love -= 1
    hide bree
    return

label bree_talk_sex_male:
    show bree
    $ result = randint(1, 5)
    if bree.is_collared and bree.love >= 150:
        show bree blush
        bree.say "I need your cock in my mouth [hero.name]."
        bree.say "Pretty please..."
    elif result == 1:
        bree.say "What do you think about kids?"
        mike.say "I think about makin' 'em all the time."
        if hero.charm >= 20:
            $ bree.love += 1
        else:
            $ bree.love -= 1
    elif result == 2:
        mike.say "What's the definition of a Yankee?"
        show bree evil
        bree.say "Oh! I know that one!"
        show bree happy
        bree.say "Same thing as a 'quickie', only you do it yourself."
        $ bree.love += 1
    elif result == 3:
        mike.say "Give me a blow job!"
        show bree annoyed
        bree.say "Can you be more romantic?"
        show bree blush
        mike.say "Fine, give me a blow job in the rain."
        if bree.love > 20 - hero.charm/2:
            $ bree.love += 1
            $ bree.sub += 1
    elif result == 4:
        if not bree.flags.anal:
            mike.say "Have you ever tried to... You know... Take it up the ass?"
            if bree.love > 120 - hero.charm/2:
                show bree flirt
                bree.say "No, but do tell me when you get the urge, I'll be delighted."
                $ bree.sub += 1
                $ bree.love += 2
            elif bree.love > 80 - hero.charm/2:
                show bree blush
                bree.say "That's pretty personal [hero.name]..."
                $ bree.love += 1
            else:
                show bree angry
                bree.say "Keep these kinds of questions to yourself..."
                $ bree.love -= 1
        else:
            mike.say "Hi, I'm Andy. Wanna play with my Woody?"
            if bree.love > 80 - hero.charm/2:
                show bree happy
                "[bree.name] giggles and gently slaps my hand."
                $ bree.love += 1
            elif not hero.charm >= 80 - bree.love:
                show bree angry
                bree.say "Keep these kinds of jokes to yourself please..."
                $ bree.love -= 1
    else:
        bree.say "It's not always about sex, sometimes the best type of intimacy is where you just lay back."
        bree.say "Laugh together at the stupidest things, hold each other, and enjoy each others' company."
        if bree.love > 80 - hero.charm/2:
            show bree happy
            bree.say "But who am I kidding, I love sex."
            "She says that with a bright and playful smile on her face."
            $ bree.love += 1
        elif not hero.charm >= 20:
            show bree sad
            mike.say "What a load of crap."
            $ bree.love -= 1
    hide bree
    return

label bree_talk_politics_male:
    show bree
    $ result = randint(1, 4)
    if result == 1:
        show bree evil
        bree.say "Whats Michelle Obamas favorite vegetable?"
        show bree happy
        bree.say "Barackoli!"
        $ bree.love += 1
    elif result == 2:
        mike.say "Political language... is designed to make lies sound truthful and murder respectable."
        mike.say "And to give an appearance of solidity to pure wind."
        bree.say "That's so true, who said that?"
        if not hero.knowledge >= 10:
            mike.say "I don't remember."
            $ bree.love += 1
        else:
            mike.say "George Orwell."
            show bree happy
            bree.say "I love that writer."
            $ bree.love += 2
    elif result == 3:
        bree.say "What is Barack Obamas favorite TV show?"
        show bree happy
        bree.say "Game of Drones!"
        $ bree.love += 1
    else:
        bree.say "How is Barack Obama going to get Republicans to cross party lines and support health care reform?"
        show bree happy
        bree.say "By giving their mistresses free breast implants!"
        $ bree.love += 1
    hide bree
    return

label bree_talk_food_male:
    show bree
    $ result = randint(1, 3)
    if bree.is_collared and bree.love >= 150:
        show bree flirt
        bree.say "Your cum is the most tasty food in the world [hero.name]."
        bree.say "Give me some please..."
    elif result == 1:
        show bree happy
        bree.say "If more of us valued food and cheer and song above hoarded gold, it would be a merrier world."
        $ bree.love += 2
    elif result == 2:
        show bree happy
        bree.say "Ask not what you can do for your country. Ask what's for lunch."
        $ bree.love += 1
    else:
        bree.say "All you need is love."
        show bree wink
        bree.say "But a little chocolate now and then doesn't hurt."
        mike.say "LOL!"
        $ bree.love += 1
    hide bree
    return

label bree_talk_travels_male:
    show bree
    $ result = randint(1, 4)
    if result == 1:
        bree.say "The world is a book and those who do not travel read only one page."
    elif result == 2:
        bree.say "To travel is to live."
    elif result == 3:
        bree.say "It can hardly be a coincidence that no language on earth has ever produced the expression, 'As pretty as an airport."
    else:
        bree.say "Not all those who wander are lost."
        if hero.knowledge >= 10:
            mike.say "Oh, My God!\nDid you just quote the lord of the ring?"
            show bree wink
            bree.say "Dare I say yes?"
            mike.say "Marry me!"
            if bree.love >= 120 - hero.charm/2:
                bree.say "Be careful, I could say yes again."
                if bree.sexperience:
                    mike.say "As long as I can fuck and slap your ass for the rest of my life please do."
                $ bree.sub += 1
            show bree happy
            "She giggles and walks away."
            $ bree.love += 2
    hide bree
    return

label bree_talk_tv_male:
    show bree
    bree.say "I don't watch tv that much."
    if bree.flags.porn:
        show bree blush
        bree.say "But I do love watching porn with you."
        $ bree.sub += 1
    hide bree
    return

label bree_talk_sports_male:
    show bree
    bree.say "You know, I work out a little, a girl has to."
    if bree.love >= 25:
        show bree flirt
        bree.say "It's not that easy to keep that hourglass figure you seem to like so much, you weasel man."
    hide bree
    return

label bree_talk_fashion_male:
    show bree
    if bree.is_collared and bree.love >= 150:
        if bree.flags.mikeNickname:
            bree.say "I'll wear whatever you want [hero.name]."
    else:
        show bree annoyed
        bree.say "I prefer to wear comfortable clothes than fashionable ones."
    $ bree.love -= 1
    hide bree
    return

label bree_talk_books_male:
    show bree
    $ result = randint(1, 5)
    if result == 1:
        bree.say "A room without books is like a body without a soul."
    elif result == 2:
        bree.say "Books are a uniquely portable magic."
    elif result == 3:
        bree.say "I can never read all the books I want; I can never be all the people I want and live all the lives I want."
        bree.say "I can never train myself in all the skills I want."
        bree.say "And why do I want?"
        bree.say "I want to live and feel all the shades, tones and variations of mental and physical experience possible in my life."
        bree.say "And I am horribly limited."
    elif result == 4:
        bree.say "I'm a book lover."
        show bree blush
        bree.say "I've probably already fucked a whole library."
        $ bree.sub += 1
    else:
        mike.say "Have you red HG2G?"
        show bree wink
        bree.say "Don't Panic."
    $ bree.love += 1
    hide bree
    return

label bree_talk_people_male:
    show bree
    if bree.is_collared and bree.love >= 150:
        show bree blush
        if bree.flags.mikeNickname:
            bree.say "If you really want me to fuck one of your friends I guess I'll do it [hero.name]."
        $ bree.sub -= 1
    else:
        show bree annoyed
        bree.say "Sorry, I have things to do."
    $ bree.love -= 1
    hide bree
    return

label bree_talk_computers_male:
    show bree
    if not bree.is_visibly_pregnant:
        $ result = randint(1, 4)
        if result == 1:
            bree.say "Computers are like Old Testament gods; lots of rules and no mercy."
        elif result == 2:
            mike.say "I think it's fair to say that personal computers have become the most empowering tool we've ever created."
            mike.say "They're tools of communication, they're tools of creativity, and they can be shaped by their user."
            bree.say "Yes but, man is still the most extraordinary computer of all."
            show bree happy
            bree.say "Or should I say woman?\nBecause a computer that freezes when it sees boobies is worth nothing."
            $ bree.love += 1
            if hero.knowledge >= 10:
                mike.say "Well, women don't have our transfer rate..."
                bree.say "Transfer rate?"
                mike.say "A single sperm has ~37.5MB of DNA information in it."
                mike.say "That means a normal ejaculation represents a data transfer of 1587GB in about 3 seconds."
                show bree happy
                mike.say "I must have accidentally uploaded an insane amount of data to my laptop over the years."
                $ bree.love += 2
        elif result == 3:
            show bree wink
            bree.say "Don't explain computers to laymen. Simpler to explain sex to a virgin."
            $ bree.love += 2
        else:
            show bree happy
            bree.say "No one messes around with a nerd's computer and escapes unscathed."
            $ bree.love += 2
    else:
        bree.say "Hey [hero.name], I discovered this great website to find advices on pregnancy."
        mike.say "What is it called?"
        bree.say "Preger-net"
    hide bree
    return

label bree_talk_music_male:
    show bree
    bree.say "You know, I listen to whatever is on the radio..."
    hide bree
    return

label bree_talk_birthday_male:
    show bree
    mike.say "Happy birthday [bree.name]."
    show bree happy
    bree.say "Thank you [hero.name]."
    $ bree.love += 5
    hide bree
    return

init:
    define nickname_roomie = ["Roomie", "roomie"]
    define nickname_hotshot = ["Hotshot", "hotshot"]
    define nickname_cutie = ["Cutie", "cutie"]
    define nickname_player_one = ["Player One", "player one"]

label command_nickname_bree:
    menu:

        "Call me Roomie" if active_girl.flags.mikeNickname not in nickname_roomie and active_girl.love > 50:
            $ active_girl.flags.mikeNickname = "Roomie"
        "Stop calling me Roomie" if active_girl.flags.mikeNickname in nickname_roomie:
            $ active_girl.flags.mikeNickname = None


        "Call me Hotshot" if active_girl.flags.mikeNickname not in nickname_hotshot and active_girl.love > 140 and active_girl.sub < 60:
            $ active_girl.flags.mikeNickname = "Hotshot"
        "Stop calling me Hotshot" if active_girl.flags.mikeNickname in nickname_hotshot:
            $ active_girl.flags.mikeNickname = None


        "Call me Cutie" if active_girl.flags.mikeNickname not in nickname_cutie and active_girl.love > 140 and active_girl.sub < 60:
            $ active_girl.flags.mikeNickname = "Cutie"
        "Stop calling me Cutie" if active_girl.flags.mikeNickname in nickname_cutie:
            $ active_girl.flags.mikeNickname = None


        "Call me Player One" if active_girl.flags.mikeNickname not in nickname_player_one and active_girl.sub > 80:
            $ active_girl.flags.mikeNickname = "Player One"
        "Stop calling me Player One" if active_girl.flags.mikeNickname in nickname_player_one:
            $ active_girl.flags.mikeNickname = None
        "Cancel":


            jump command_girl

label submissive_interact_bree_male:
    mike.say "[bree.name]..."
    mike.say "I know how much you like to play videogames..."
    show bree happy
    bree.say "I sure do, [hero.name]."
    show bree normal
    mike.say "And you like to play with me too, right?"
    show bree happy at startle
    "[bree.name] giggles at the question, shaking her head."
    show bree smile
    bree.say "Yeah, [hero.name], I like that too!"
    show bree normal
    mike.say "Well...would you say so when you see me?"
    if bree.sub >= 70 or bree.is_sex_slave:
        show bree smile blush
        bree.say "Of course I will, [hero.name]."
        bree.say "It sounds like fun!"
        bree.say "I'll make it clever and funny too, I promise!"
        $ bree.flags.submissive_interact = True
    else:
        show bree talkative
        bree.say "What are you even talking about, [hero.name]?"
        bree.say "That sounds SO cheesy it's unreal!"
        show bree annoyed
        mike.say "Ah, now that you say so, [bree.name]..."
        mike.say "Let's just forget about it, okay?"
        $ bree.love -= 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
