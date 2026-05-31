label cherie_talk_love_female:
    bree.say "Don't take this the wrong way, Cherie..."
    bree.say "But you're a mature woman, right?"
    cherie.say "I won't, [hero.name] - so long as you don't call me old!"
    bree.say "Ah...okay, Cherie!"
    bree.say "But you've got some experience, haven't you?"
    bree.say "So tell me...do you still believe in true love?"
    cherie.say "Oh, [hero.name]...I don't think I've found it."
    cherie.say "But that doesn't mean I've stopped looking!"
    if Person.find("cherie"):
        $ cherie.love += 1
    return

label cherie_talk_sex_female:
    bree.say "I hope I look as good as you when I'm older, Cherie!"
    cherie.say "Why, [hero.name] - you cheeky little thing, you!"
    bree.say "And...well...you still..."
    bree.say "You know...want to do fun stuff when you're older, right?"
    bree.say "Like sexy stuff?"
    cherie.say "Ha, ha..."
    cherie.say "I want to do more sexy stuff now than ever, [hero.name]!"
    cherie.say "Certainly more than I did when I was your age..."
    if Person.find("cherie"):
        $ cherie.love += 1
    return

label cherie_talk_politics_female:
    bree.say "Do you do politics, Cherie?"
    bree.say "Most young people don't seem to care all that much."
    bree.say "But you must care more when you get older!"
    cherie.say "Urgh...I spent years holding my tongue around people, [hero.name]!"
    cherie.say "Smiling and pretending to agree with assholes for the sake of Dwayne's career."
    cherie.say "The experience put me off talking politics forever!"
    if Person.find("cherie"):
        $ cherie.love -= 1
    return

label cherie_talk_food_female:
    bree.say "You have an amazing figure, Cherie!"
    bree.say "Better than some of the girls I go to uni with!"
    bree.say "What's your secret?"
    bree.say "You have to tell me!"
    cherie.say "Oh, [hero.name]...it's a constant battle!"
    cherie.say "I love my food so much."
    cherie.say "But it's like anything I eat that I shouldn't..."
    cherie.say "It goes straight to my hips and my ass!"
    return

label cherie_talk_travels_female:
    bree.say "You've travelled, right, Cherie?"
    bree.say "You've seen some of the world?"
    cherie.say "You could say that, [hero.name]."
    cherie.say "But we always tended to go where Dwayne wanted to."
    cherie.say "The kind of places that would impress his friends and where he could network, you know?"
    cherie.say "I never got to go to the places that I wanted to visit..."
    if Person.find("cherie"):
        $ cherie.sub += 1
    return

label cherie_talk_tv_female:
    bree.say "Do you watch much TV, Cherie?"
    bree.say "Or is that a little lacking in sophistication?"
    cherie.say "Oh no, [hero.name]...don't be silly!"
    cherie.say "I'd die if I ever missed my soap operas."
    cherie.say "Sometimes I feel like the characters in them are the best friends I have!"
    if Person.find("cherie"):
        $ cherie.love += 1
    return

label cherie_talk_sports_female:
    bree.say "I don't see sports as being your kind of thing, Cherie."
    bree.say "You know - too much shouting and cheering!"
    bree.say "It just doesn't seem to fit!"
    cherie.say "Oh no, [hero.name]...I love watching sports!"
    cherie.say "Especially the ones that are played by strapping young men!"
    cherie.say "If you know what I mean..."
    if Person.find("cherie"):
        $ cherie.love += 1
    return

label cherie_talk_fashion_female:
    bree.say "You dress pretty stylish, Cherie!"
    bree.say "I keep meaning to ask you for some tips."
    bree.say "But I'm kind of afraid of the price-tag!"
    cherie.say "Oh, thank you so much, [hero.name]!"
    cherie.say "I do try my best to look good."
    cherie.say "Maybe we could go shopping together some time?"
    return

label cherie_talk_books_female:
    bree.say "I never see you reading a book, Cherie."
    bree.say "So I guess that means you read when you're alone?"
    cherie.say "Oh no, [hero.name]...I've never been a big reader!"
    cherie.say "The most I can manage is to flick through a fashion magazine."
    cherie.say "Or maybe a romance novel, if I'm feeling really brave!"
    if Person.find("cherie"):
        $ cherie.love -= 1
    return

label cherie_talk_people_female:
    bree.say "Sounds like you host a lot of parties, Cherie."
    bree.say "And that you attend your fair share too."
    bree.say "Does that mean you're a people-person?"
    cherie.say "Ah...I wish that I was, [hero.name]!"
    cherie.say "The truth is that I'm kind of putting on a show."
    cherie.say "I don't like spending time with lots of people I don't really like."
    cherie.say "I'd much rather spend time with one person that I really do like..."
    if Person.find("cherie"):
        $ cherie.love -= 1
    return

label cherie_talk_computers_female:
    cherie.say "What's the matter, [hero.name]?"
    cherie.say "You look cross."
    cherie.say "And that's not like you at all!"
    bree.say "It's my laptop, Cherie - it's playing up!"
    bree.say "You want to take a look?"
    bree.say "See if you can figure it out?"
    cherie.say "Oh no, [hero.name]...I don't understand computers."
    cherie.say "I'm sure I'd only make it worse!"
    if Person.find("cherie"):
        $ cherie.love -= 1
    return

label cherie_talk_music_female:
    bree.say "What's your favourite kind of music, Cherie?"
    bree.say "Do you like retro stuff?"
    bree.say "Or are you into the latest sounds?"
    cherie.say "I don't know, [hero.name]!"
    cherie.say "I used to be clued-up on music."
    cherie.say "But when Cassidy came along, I kind of lost touch!"
    return

label cherie_talk_birthday_female:
    bree.say "Happy Birthday, Cherie!"
    bree.say "And many happy returns too!"
    cherie.say "Oh, [hero.name]...however did you remember?!?"
    cherie.say "Dwayne and Cassidy never remembered my birthday - not ever!"
    if Person.find("cherie"):
        $ cherie.love += 2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
