label dwayne_talk_love_female:
    show dwayne
    bree.say "You and Cherie make quite power-couple, Dwayne!"
    bree.say "Is it the fact that you're in love that makes it work?"
    bree.say "Because you really can't fake a love like that!"
    dwayne.say "HA!"
    dwayne.say "How little you know, [hero.name]!"
    dwayne.say "Cherie and I have been living a lie for years now!"
    dwayne.say "We don't love each other - it's just an act."
    $ dwayne.love -= 1
    hide dwayne
    return

label dwayne_talk_sex_female:
    show dwayne
    bree.say "They say power and money are an aphrodisiac, Dwayne."
    bree.say "And since you've got both of those things, I have to ask..."
    bree.say "Is it actually true?"
    dwayne.say "What a charming question, [hero.name]!"
    dwayne.say "Well, I have to say that I'm blessed with success when it comes to the ladies."
    dwayne.say "But I prefer to think that's on account of my natural charms and winning personality!"
    $ dwayne.love += 1
    hide dwayne
    return

label dwayne_talk_politics_female:
    show dwayne
    bree.say "I was going to ask you about politics, Dwayne."
    bree.say "But everyone gets defensive when you talk about that kind of thing."
    bree.say "I guess they're worried they might offend somebody!"
    dwayne.say "Not me, [hero.name] - I couldn't give a rat's ass about offending anyone!"
    dwayne.say "And as for my politics, I'm one hundred percent capitalist and conservative, baby!"
    dwayne.say "Both of them with a capital C too!"
    $ dwayne.love += 1
    hide dwayne
    return

label dwayne_talk_food_female:
    show dwayne
    bree.say "You must be used to the finer things in life, Dwayne."
    bree.say "I bet you even have your own chef on call, twenty-four seven!"
    bree.say "One that can whip up all sorts of exotic dishes too."
    dwayne.say "I don't care for extravagant food, [hero.name]."
    dwayne.say "It's all just empty calories."
    dwayne.say "A distraction from getting work done and then reaping the rewards!"
    hide dwayne
    return

label dwayne_talk_travels_female:
    show dwayne
    bree.say "What's it like flying in first class and going on fancy cruises, Dwayne?"
    bree.say "[mike.name]'s always telling me you work really hard."
    bree.say "So you must take decent holidays to recover, right?"
    dwayne.say "Why would I want to laze around and let the competition catch me up, [hero.name]?"
    dwayne.say "When I fly anywhere, it's to a close a deal."
    dwayne.say "Oh, and it's executive class, not humble first class for me!"
    hide dwayne
    return

label dwayne_talk_tv_female:
    show dwayne
    bree.say "I used to watch that show with the Billionaire on it, Dwayne."
    bree.say "You know the one, where he shouts a lot and fires people every week?"
    bree.say "Is that the kind of shows that big-shots like you watch?"
    dwayne.say "I don't have time to watch TV, [hero.name]."
    dwayne.say "I'm too busy being out there, making things happen."
    dwayne.say "Ha - they should make a show about me, not that orange buffoon!"
    $ dwayne.love -= 1
    hide dwayne
    return

label dwayne_talk_sports_female:
    show dwayne
    bree.say "Wow - you're almost as big as [mike.name] said you were!"
    bree.say "Do you work out, Dwayne?"
    bree.say "No, wait...you play sports, don't you?"
    dwayne.say "Ha, ha, ha..."
    dwayne.say "I was quite the athlete in college, [hero.name]."
    dwayne.say "Played American Football - coach said I could have turned pro!"
    dwayne.say "A guy should play competitive sports, it makes him tough and hungry!"
    $ dwayne.love += 1
    hide dwayne
    return

label dwayne_talk_fashion_female:
    show dwayne
    bree.say "What on earth is that suit made of, Dwayne?"
    bree.say "It's so shiny - I swear I can see my face in it!"
    dwayne.say "Yeah, you like it, don't you, [hero.name]?"
    dwayne.say "I love to look good, make the right impression."
    dwayne.say "So I have all of my suits hand-made in Italy!"
    $ dwayne.love += 1
    hide dwayne
    return

label dwayne_talk_books_female:
    show dwayne
    bree.say "I bet you have one of those offices that's full of bookshelves, Dwayne."
    bree.say "But think it's all just for decoration and you've not read one of them!"
    bree.say "I'm right, aren't I?"
    dwayne.say "Oh, [hero.name], [hero.name], [hero.name]..."
    dwayne.say "They're all bestselling books on winning at business and in life."
    dwayne.say "And I've read every single one, cover to cover!"
    hide dwayne
    return

label dwayne_talk_people_female:
    show dwayne
    bree.say "Guys like you know how to sound positive, Dwayne."
    bree.say "But I think that's all just part of your charm offensive."
    bree.say "I don't think you really like people at all!"
    dwayne.say "You couldn't be more wrong, [hero.name]."
    dwayne.say "I love people, because they're the greatest natural resource in the world."
    dwayne.say "Not only that, they're renewable too!"
    dwayne.say "You can squeeze everything out of them one day."
    dwayne.say "And then do it all over again the next!"
    $ dwayne.love += 1
    hide dwayne
    return

label dwayne_talk_computers_female:
    show dwayne
    bree.say "Hard to imagine businesses without computers, huh, Dwayne?"
    bree.say "I bet your company relies on them almost totally, right?"
    bree.say "It'd grind to a halt without them!"
    dwayne.say "Computers are just tools, [hero.name]."
    dwayne.say "Once we had flint and fire."
    dwayne.say "And then we had steel and coal."
    dwayne.say "Now we have silicon and software!"
    dwayne.say "And one day we'll have something else, something better!"
    hide dwayne
    return

label dwayne_talk_music_female:
    show dwayne
    bree.say "What kind of music does a corporate titan listen to, Dwayne?"
    bree.say "Classical, opera or something that nobody would expect?"
    dwayne.say "Nah...I don't really care for music, [hero.name]."
    dwayne.say "It all sounds the same to me anyway!"
    $ dwayne.love -= 1
    hide dwayne
    return

label dwayne_talk_birthday_female:
    show dwayne
    bree.say "Happy Birthday, Dwayne."
    bree.say "[mike.name] told me it was today."
    dwayne.say "Oh, he did, did he?"
    dwayne.say "He'd better not have told you how old I am too!"
    $ dwayne.love += 1
    hide dwayne
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
