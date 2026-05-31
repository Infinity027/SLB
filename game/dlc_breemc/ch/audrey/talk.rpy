label audrey_talk_love_female:
    show audrey
    bree.say "Oh, it's SO hard to hold down a relationship these days, Audrey."
    bree.say "It's like the world of dating's gone mad - like it's chaos!"
    audrey.say "Yeah, [hero.name] - isn't it great?"
    audrey.say "I don't want to cry over it."
    audrey.say "I want to watch the world of dating burn!"
    $ audrey.love += 1
    hide audrey
    return

label audrey_talk_sex_female:
    show audrey
    bree.say "I hear people say stuff like 'sex is over-rated', Audrey."
    bree.say "And, like...they sound really serious and clever."
    bree.say "But they have to be wrong - right?"
    audrey.say "Of course they're wrong, [hero.name]."
    audrey.say "And fuck those guys too!"
    audrey.say "They probably never had any great sex anyway!"
    $ audrey.love += 1
    hide audrey
    return

label audrey_talk_politics_female:
    show audrey
    bree.say "I know it's not sexy or fun, Audrey."
    bree.say "But I really think more people our age should be into politics."
    bree.say "I mean, it effects us all!"
    audrey.say "Yawn...boring!"
    audrey.say "Politicians are all the same, [hero.name]!"
    audrey.say "And voting's a waste of my precious time!"
    $ audrey.love -= 1
    hide audrey
    return

label audrey_talk_food_female:
    show audrey
    bree.say "I feel so hungry, Audrey!"
    bree.say "And I can't stop talking about it!"
    bree.say "You must think I'm such a little pig!"
    audrey.say "Don't be silly, [hero.name]!"
    audrey.say "Food's the most important thing to give your body."
    audrey.say "Well...after sex, of course!"
    $ audrey.love += 1
    hide audrey
    return

label audrey_talk_travels_female:
    show audrey
    bree.say "I keep making a list of all the places I've been and all the places I want to go."
    bree.say "But the first list is never going to be as long as the second one!"
    audrey.say "I know just what you mean, [hero.name]."
    audrey.say "I've got a list like that myself."
    audrey.say "It's more like a list of guys I've fucked from different places..."
    audrey.say "But the principle is the same, right?"
    $ audrey.love += 1
    hide audrey
    return

label audrey_talk_tv_female:
    show audrey
    bree.say "I have to see the next episode of this series I'm binging, Audrey."
    bree.say "The male lead's SO hot, and he's about to get it on with the female lead too!"
    audrey.say "Urgh..."
    audrey.say "Hard pass from me on that one, [hero.name]!"
    audrey.say "I'm not watching actors pretend to fuck."
    audrey.say "I'd rather be the one being watched when I actually fuck!"
    $ audrey.love -= 1
    hide audrey
    return

label audrey_talk_sports_female:
    show audrey
    bree.say "I don't get sports, Audrey."
    bree.say "And I don't get why people watch them either!"
    audrey.say "Your loss, [hero.name]!"
    audrey.say "Because it's basically all repressed sexual desire, you know?"
    audrey.say "All those people want to fuck, but they can't."
    audrey.say "So they channel it into the shouting and screaming instead!"
    $ audrey.love += 1
    hide audrey
    return

label audrey_talk_fashion_female:
    show audrey
    bree.say "You like to dress to impress, right, Audrey?"
    bree.say "The right outfit for the right occasion?"
    audrey.say "Of course, [hero.name]!"
    audrey.say "It's no different to bringing the right weapon to a hunt."
    audrey.say "You need a specific kind of tool to slaughter your prey!"
    $ audrey.love += 1
    hide audrey
    return

label audrey_talk_books_female:
    show audrey
    bree.say "Read any good books lately, Audrey?"
    bree.say "Yeah, I know it's a cliche!"
    bree.say "But I'd still like to know."
    audrey.say "Oh yeah?"
    audrey.say "Well, the answer is no!"
    audrey.say "Print's dead, [hero.name]!"
    audrey.say "And I prefer to live in the real world!"
    $ audrey.love -= 1
    hide audrey
    return

label audrey_talk_people_female:
    show audrey
    bree.say "This is going to sound so naive, Audrey."
    bree.say "But I still believe in the basic goodness of people."
    audrey.say "It's naive, [hero.name], but I get it."
    audrey.say "I believe in something similar."
    audrey.say "But I believe in the basic naivety of people!"
    hide audrey
    return

label audrey_talk_computers_female:
    show audrey
    bree.say "Computers are SO useful!"
    bree.say "Seriously, Audrey - where would we be without them?"
    audrey.say "Ah, we'd get by somehow, [hero.name]."
    audrey.say "There was somebody saying that about bricks made of shit a thousand years ago."
    audrey.say "But you don't hear much from him now, do you?"
    $ audrey.love -= 1
    hide audrey
    return

label audrey_talk_music_female:
    show audrey
    bree.say "Ooh...you HAVE to hear this song, Audrey!"
    bree.say "It's a real ear-worm - everyone's listening to it!"
    audrey.say "Nah, I'll pass, [hero.name]."
    audrey.say "It looks like that worm got all the way to your brain!"
    hide audrey
    return

label audrey_talk_birthday_female:
    show audrey
    bree.say "Hey, Audrey..."
    bree.say "Surprise - HAPPY BIRTHDAY!"
    audrey.say "Wha...how..."
    audrey.say "No...no way..."
    audrey.say "I'm not crying!"
    $ audrey.love += 3
    hide audrey
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
