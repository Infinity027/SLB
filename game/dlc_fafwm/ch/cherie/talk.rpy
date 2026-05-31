label cherie_talk_love_male:
    show cherie normal
    show cherie talkative
    cherie.say "When you come from the country that I do, {i}mon ami{/i}, everyone expects you to be an expert on the subject of love."
    cherie.say "But the truth is that we are the same as anyone else the world over when it comes to affairs of the heart."
    show cherie happy
    cherie.say "We do what our hearts tell us is the best thing, that which makes us feel the happiest in the moment."
    cherie.say "This is the best way to be, don't you agree?"
    show cherie flirt
    menu:
        "That's very irresponsible":
            mike.say "How can you even begin to think like that about something as important as love?!?"
            show cherie annoyed
            mike.say "It's like, the most important thing in the world, Cherie!"
            mike.say "Aren't you supposed to get wiser as you get older?"
            $ cherie.love -= 1
        "My thoughts exactly":
            mike.say "That sounds totally right to me, Cherie."
            show cherie smile
            mike.say "Like it's the only thing you can do with any honesty."
            mike.say "And at least that way you know that you were acting out of genuine love."
            $ cherie.love += 1
        "You don't need to be an expert if you leave it to me":
            mike.say "Seems like you have a lot of unanswered questions about love, Cherie."
            mike.say "But don't you worry about that, because it's not a problem anymore."
            show cherie stuned blush
            mike.say "Because now you have me to make all of those choices for you."
            $ cherie.sub += 1
    show cherie normal -blush
    return

label cherie_talk_sex_male:
    show cherie talkative
    cherie.say "Ah, I have seen so many lovers come and go, {i}mon ami{/i}."
    show cherie happy
    cherie.say "And it is good to be like this, is it not?"
    cherie.say "To have experienced many different things and to make all of that part of who you are in the bedroom?"
    show cherie flirt
    menu:
        "You're right, Cherie - and I want you to teach me!":
            mike.say "You don't know how much I love hearing you talk like that, Cherie!"
            show cherie b stuned blush
            mike.say "I want to benefit from all of the experience that you've had in the bedroom."
            mike.say "To learn everything that you can teach me!"
            $ cherie.sub -= 1
        "What about faithfulness?":
            mike.say "I'm sorry, Cherie, but isn't that just an excuse to sleep around?"
            show cherie annoyed
            mike.say "Wouldn't you rather be with just one person for the rest of your life?"
            mike.say "I mean, is boring sex really that bad if you know the other person really loves you?"
            $ cherie.love -= 1
        "Variety is the spice of life":
            mike.say "I think you're right, Cherie - sex is just like anything else in life."
            show cherie smile
            mike.say "You don't get good at it by doing the same things with the same people all the time."
            mike.say "And I don't think you ever stop learning new things either."
            $ cherie.love += 1
    show cherie a normal -blush
    return

label cherie_talk_politics_male:
    show cherie whining
    cherie.say "Politicians bore me so much, {i}mon ami{/i} - they are all the same, I think."
    show cherie talkative
    cherie.say "And no matter what they say or the things they promise to do, nothing changes."
    cherie.say "I wonder if, were they all to suddenly disappear, would we not just get on without them?"
    show cherie annoyed
    menu:
        "You really don't know what you're talking about":
            mike.say "Sounds to me like you really don't know much about politics, Cherie."
            show cherie upset
            mike.say "Because that's the kind of thing someone really ignorant would come out with."
            mike.say "Maybe if you paid attention to the news a little more, you'd be at least a little clued up?"
            $ cherie.love -= 1
        "You don't need to worry about things like that":
            show cherie flirt
            mike.say "Well you're a beautiful woman, Cherie - so you can get away with not worrying about that kind of thing."
            mike.say "All you need to do is make sure that you everyone sees how stunning you look, and you'll be fine."
            mike.say "Trust me, there'll always be someone willing to take care of you and chase away the bad guys."
            $ cherie.sub += 1
        "You really see to the heart of the matter":
            mike.say "You know what, I never really looked at it that way, Cherie."
            show cherie smile
            mike.say "But now that you mention it, they are all the same, aren't they?"
            mike.say "Thanks for opening my eyes to the truth on that one!"
            $ cherie.sub -= 1
    show cherie normal
    return

label cherie_talk_food_male:
    show cherie talkative
    cherie.say "You must think that it's such a stereotype for me to lecture you on food, coming from my country."
    show cherie whining
    cherie.say "But it is the truth, {i}mon ami{/i} - you eat such bland and unhealthy garbage here yet still call it food!"
    show cherie talkative
    cherie.say "They say that you are what you eat, so what are you when you fill yourself with such rubbish every day?"
    show cherie sadsmile
    menu:
        "Don't be such a total snob":
            show cherie annoyed
            mike.say "Urgh...change the record, Cherie - that's such a predictable thing to say."
            mike.say "So you have good food back home, so what?"
            mike.say "I think you guys are just obsessed with it because everything else in your country sucks."
            $ cherie.love -= 1
        "If it's so good then you should cook more":
            mike.say "If your food is so good, Cherie, then why don't you prove it?"
            show cherie stuned
            mike.say "Like, get your ass in the kitchen and cook me a meal every day."
            mike.say "That way you can show me how good the stuff is, and make yourself useful at the same time."
            $ cherie.sub += 1
        "I'm tired of eating rubbish":
            mike.say "You're right, Cherie, food here is bad for you on so many levels."
            show cherie amused
            mike.say "And another thing - how come it's so damn expensive too?"
            mike.say "It's like I'm being served slop, and asked to pay for nouvelle cuisine!"
            $ cherie.love += 1
    show cherie normal
    return

label cherie_talk_travels_male:
    show cherie talkative
    cherie.say "One of the things that I will never regret about being with a man like Dwayne is the freedom to travel."
    show cherie happy
    cherie.say "Oh my, the places I have been, the things I have seen and done in my lifetime!"
    show cherie talkative
    cherie.say "It is something that I would almost thank that awful man for allowing me to experience."
    show cherie sadsmile
    menu:
        "The world's a big and very scary place":
            mike.say "I'm glad to have someone like you around, Cherie - someone with so much experience."
            show cherie amused
            mike.say "I've never really travelled that far from home, and the idea of it kind of scares me."
            mike.say "Maybe with someone like you, I could finally conquer that fear?"
            $ cherie.sub -= 1
        "I hope we can see new places together":
            show cherie flirt
            mike.say "I want to feel that same thrill too, Cherie - and do it with you."
            mike.say "And the world's a big place, so big you can't have seen it all."
            mike.say "So there must be places out there that we can discover together."
            $ cherie.love += 1
        "You don't need the world when you have me":
            show cherie stuned
            mike.say "That was just Dwayne trying to buy you with his piles of money, Cherie."
            show cherie flirt
            mike.say "I'm going to show you what a real man can mean in your life, trust me."
            mike.say "Once I'm done, I'll be the whole of your world."
            $ cherie.sub += 1
    show cherie normal
    return

label cherie_talk_tv_male:
    show cherie talkative
    cherie.say "I have never really been interested in television, {i}mon ami{/i}."
    show cherie happy
    cherie.say "The cinema was always the place to be entertained for me."
    show cherie talkative
    cherie.say "In comparison, television always seemed so small, so limited."
    show cherie sadsmile
    menu:
        "You just haven't seen the right shit on TV":
            show cherie stuned
            mike.say "Okay, Cherie, I'm calling bullshit on that one, right now!"
            mike.say "The only reason you're saying that is because you haven't watched the right stuff - but that ends now."
            mike.say "Starting tonight, we're binging series until you see the error of your ways."
            $ cherie.sub += 1
        "I guess cinema will always have that sense of romance":
            mike.say "They're always saying that TV and rentals and streaming will kill of the movies."
            show cherie smile
            mike.say "But I don't think that's ever going to really happen, Cherie."
            mike.say "Cinema's always going to have that air of romance that TV can never copy."
            $ cherie.love += 1
        "Urgh...that's just ignorance and snobbery":
            show cherie annoyed
            mike.say "That's what people say when they want to sound superior, Cherie."
            mike.say "Looking down their noses at people who just want to binge a decent series at home of an evening."
            mike.say "Plus I bet those same people have never watched half of the so-called classic movies they claim to love!"
            $ cherie.love -= 1
    show cherie normal
    return

label cherie_talk_sports_male:
    show cherie talkative
    cherie.say "Ah...I'm never sure that I understand the appeal of sports, you know?"
    show cherie happy
    cherie.say "But I wonder if there is some essential truth buried beneath the act of playing the game."
    show cherie talkative
    cherie.say "Maybe what speaks to us is not the mundane things going on with the players, but the universal truths their struggles represent?"
    show cherie normal
    menu:
        "Geez, it's just a game":
            show cherie annoyed
            mike.say "Ouch, Cherie - you're starting to make my head hurt!"
            mike.say "Do you think about everything in such painful detail?"
            mike.say "Because you know, sometimes a game is just a game."
            $ cherie.love -= 1
        "You need to pay more attention to the rules":
            show cherie stuned blush
            mike.say "Why didn't you just say that you don't get the rules, Cherie?"
            mike.say "Next chance we get, we're sitting down and watching a game from start to finish."
            mike.say "Then you can be quiet and listen as I explain it all to you."
            $ cherie.sub += 1
        "That's way more interesting than the actual sports":
            show cherie amused
            mike.say "I never thought about it like that before, Cherie."
            mike.say "Funny how you always see things more deeply than I do."
            mike.say "So...do you want to tell me more about your insights?"
            $ cherie.sub -= 1
    show cherie normal -blush
    return

label cherie_talk_fashion_male:
    show cherie talkative
    cherie.say "Fashion is not the same in my home country as it is over here, {i}mon ami{/i}."
    show cherie whining
    cherie.say "Here you treat it like something that must be studied, or worse, a talent that you must be born with."
    show cherie happy
    cherie.say "At home it is a natural thing, an instinct that is as much a part of us as the words we speak and the air we breathe."
    show cherie smile
    menu:
        "You guys dress weird":
            show cherie annoyed
            mike.say "I don't know about that, Cherie..."
            mike.say "The exchange students I study with that come from your country don't seem all that stylish."
            mike.say "I mean, white denim jeans - what's up with that anyway?"
            $ cherie.love -= 1
        "You sure could do something to perk up my wardrobe":
            show cherie amused
            mike.say "I always struggle to know what to wear, Cherie."
            mike.say "Does your expertise in fashion extend to awkward guys?"
            mike.say "Because I wouldn't turn down any advice you could give me."
            $ cherie.sub -= 1
        "You certainly seem to have a natural style":
            mike.say "I don't know where it comes from, Cherie."
            mike.say "But you definitely have a style all of your own."
            mike.say "I've never seen you look anything but sharp and on-trend!"
            $ cherie.love += 1
    show cherie normal
    return

label cherie_talk_books_male:
    show cherie happy
    cherie.say "Ah, when I was younger, I would read all the time, always devouring books."
    show cherie whining
    cherie.say "But now I find that I do not have enough time to devote to my passion of reading."
    show cherie talkative
    cherie.say "Maybe some day I will find the time again, as I do miss it so!"
    show cherie normal
    menu:
        "I doubt you'd get what I'm reading":
            mike.say "I don't have that problem, Cherie -I always make time to read every day."
            mike.say "I mean, I'd recommend some titles to you..."
            show cherie annoyed
            mike.say "But I think they'd probably be too involved and complicated for you."
            $ cherie.love -= 1
        "I bet you have the best taste in books":
            mike.say "You're so smart and sophisticated, Cherie..."
            show cherie amused
            mike.say "I bet you have the best taste in books too - really smart ones."
            mike.say "Would you mind recommending me some titles you like?"
            $ cherie.sub -= 1
        "Maybe we could start swapping recommendations":
            mike.say "I love to read too, Cherie - I can't get hold of books quickly enough."
            show cherie smile
            mike.say "Maybe we could start helping each other out, like a little book-club, just you and me?"
            mike.say "We can recommend each other books and then share our thoughts on them."
            $ cherie.love += 1
    show cherie normal
    return

label cherie_talk_people_male:
    show cherie talkative
    cherie.say "I know that I should not say such things, {i}mon ami{/i}..."
    cherie.say "That they say there is good in the hearts of all human beings."
    show cherie whining
    cherie.say "But I find that most of the people I meet, I do not like at all!"
    show cherie sadsmile
    menu:
        "That's a very negative attitude":
            mike.say "How can you be so dismissive of people, Cherie?"
            show cherie sad
            mike.say "It's not fair to judge someone before you know them."
            mike.say "That way you're setting them up to dislike you too!"
            $ cherie.love -= 1
        "You don't need to worry about people anymore":
            show cherie stuned
            mike.say "You're right, Cherie - most people are scum, total shits!"
            mike.say "That's why you need a guy like me to look out for you."
            mike.say "Without me, you'd be totally at their mercy."
            $ cherie.sub += 1
        "The world's a scary place and it scares the hell out of me":
            mike.say "You don't have to tell me that, Cherie - people scare the living shit out of me!"
            show cherie amused
            mike.say "I'm just glad I've met someone that can see how it is too."
            mike.say "And you sound like you know what to do about it as well!"
            $ cherie.sub -= 1
    show cherie normal
    return

label cherie_talk_computers_male:
    show cherie whining
    cherie.say "This is going to make me sound so old - but computers baffle me so!"
    show cherie talkative
    cherie.say "I can use them to do the most basic of things, you know?"
    show cherie whining
    cherie.say "But I have no idea how they actually work, none at all."
    show cherie sadsmile
    menu:
        "They really baffle me too":
            mike.say "I'll be honest with you, Cherie - they downright terrify me!"
            show cherie amused
            mike.say "Sometimes I wish we could just go back to how things were in the past."
            mike.say "Like, your generation were the ones that had the right idea."
            $ cherie.sub -= 1
        "That's no strange thing":
            mike.say "You're not alone there, Cherie - lots of people are unsure of computers."
            show cherie smile
            mike.say "But I'm sure that you can learn to understand them better."
            mike.say "Because you're a smart person, and you have me to help you too."
            $ cherie.love += 1
        "I expected as much":
            mike.say "They're complicated, cutting-edge machines, Cherie."
            mike.say "So of course you're going to find them confusing!"
            show cherie flirt
            mike.say "Best to let me handle them for you in the future - in case the break something, yeah?"
            $ cherie.sub += 1
    show cherie normal
    return

label cherie_talk_music_male:
    show cherie whining
    cherie.say "I feel so old when I say this, but I do not understand modern music, {i}mon ami{/i}."
    cherie.say "Maybe I am not supposed to appreciate it, maybe it is only for the very young."
    show cherie talkative
    cherie.say "But it does so very much sound like a cat being minced while it is still alive and conscious."
    show cherie sadsmile
    menu:
        "Oh that's so typical":
            show cherie annoyed
            mike.say "Why do people of your age always do that, Cherie?"
            mike.say "As soon as something new comes along, you just dump on it straight away."
            mike.say "Your generation didn't write all the greatest songs, no matter what you think."
            $ cherie.love -= 1
        "I really want to learn about decent music":
            mike.say "There are so many songs from back in the day, Cherie."
            show cherie amused
            mike.say "They really knew how to write a classic back then."
            mike.say "You want to tell me all about hearing them for the first time?"
            $ cherie.sub -= 1
        "The classics are classics for a reason":
            show cherie smile
            mike.say "I think there's definitely something to that, Cherie."
            mike.say "Like, there's songs that endure because they're just that damn good."
            mike.say "And most of this modern stuff seems to disappear as soon as something new comes along."
            $ cherie.love += 1
    show cherie normal
    return

label cherie_talk_birthday_male:
    mike.say "Happy birthday, Cherie!"
    mike.say "And many happy returns too."
    show cherie b surprised
    cherie.say "Oh my goodness!"
    show cherie b happy
    cherie.say "How sweet of you to remember."
    show cherie a normal
    return


init:
    define nickname_amour = ["Amour", "amour"]
    define nickname_cochonet = ["Cochonet", "cochonet"]

label command_nickname_cherie:
    menu:
        "Call me Amour" if active_girl.flags.mikeNickname not in nickname_amour and active_girl.love > 100:
            $ active_girl.flags.mikeNickname = "Amour"
        "Stop calling me Amour" if active_girl.flags.mikeNickname in nickname_amour:
            $ active_girl.flags.mikeNickname = None
        "Call me Cochonet" if active_girl.flags.mikeNickname not in nickname_cochonet and active_girl.sexperience > 5:
            $ active_girl.flags.mikeNickname = "Cochonet"
        "Stop calling me Cochonet" if active_girl.flags.mikeNickname in nickname_cochonet:
            $ active_girl.flags.mikeNickname = None
        "Cancel":
            jump command_girl
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
