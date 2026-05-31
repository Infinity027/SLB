label cassidy_talk_love_female:
    bree.say "I hope you don't mind me saying this, Cassidy..."
    bree.say "But you're SO pretty!"
    bree.say "You must have guys falling in love with you all the time!"
    cassidy.say "Aw, thanks so sweet of you to say, [hero.name]!"
    cassidy.say "I mean, you're right, of course!"
    cassidy.say "But if someone falls for me, that's their problem."
    cassidy.say "I'm not even sure love's for real!"
    return

label cassidy_talk_sex_female:
    bree.say "You're dad's the boss at [mike.name]'s company, right, Cassidy?"
    bree.say "And I bet he's super protective of his little girl, right?"
    cassidy.say "Urgh...he sure is, [hero.name]!"
    cassidy.say "And it's the bane of my social life!"
    bree.say "Yeah, my dad's a cop and he's like that too!"
    bree.say "Makes sneaking out to get it on with a guy that much better, right?"
    cassidy.say "It sure does, [hero.name]!"
    cassidy.say "Feels like you're getting one over on him!"
    $ cassidy.love += 1
    return

label cassidy_talk_politics_female:
    bree.say "You're family are pretty rich, right, Cassidy?"
    bree.say "I mean they must move in high-up circles?"
    cassidy.say "Oh yeah - mom and dad are always going to important events."
    bree.say "So they must be into good causes too?"
    bree.say "Charity events and political fund-raisers?"
    cassidy.say "Huh?"
    cassidy.say "I don't know what the hell goes on there, [hero.name]!"
    cassidy.say "It's all boring - no fun at all!"
    return

label cassidy_talk_food_female:
    bree.say "I was just going to grab something to eat, Cassidy."
    bree.say "You want me to get you some too?"
    bree.say "I'm thinking maybe pizza or sushi?"
    if cassidy.love >= 25:
        $ cassidy.love += 1
        cassidy.say "You bet, [hero.name]!"
        cassidy.say "I love junk food - it's the best!"
        cassidy.say "But mom and dad are too snobby to let me order it!"
    else:
        $ cassidy.love -= 1
        cassidy.say "Urgh...no way, [hero.name]!"
        cassidy.say "Have you seen some of the people that work in take-out restaurants?"
        cassidy.say "No way am I eating something that they've touched with their hands!"
    return

label cassidy_talk_travels_female:
    bree.say "I keep on saving and saving."
    bree.say "One day I'll have enough squirreled away."
    bree.say "And then I'll take that trip!"
    cassidy.say "Why do that, [hero.name]?"
    cassidy.say "Just ask your daddy to pay for it."
    cassidy.say "That's what I always do!"
    bree.say "Gee, Cassidy...why didn't I think of that!"
    return

label cassidy_talk_sports_female:
    bree.say "I think my dad wanted a boy!"
    bree.say "I mean, he was always trying to push me into playing sports."
    bree.say "You know, like he was making up for me being a girl?"
    cassidy.say "Urgh...I know what you mean, [hero.name]!"
    cassidy.say "Daddy bought me SO MANY ponies!"
    cassidy.say "But I never wanted to do dressage!"
    bree.say "Wow, Cassidy...that must have been a living hell!"
    $ cassidy.love -= 1
    return

label cassidy_talk_fashion_female:
    bree.say "I guess you don't have much trouble keeping up with fashions, Cassidy?"
    bree.say "With a dad as rich as yours, you must have a wardrobe like an aircraft hanger!"
    if cassidy.love >= 25:
        cassidy.say "It's one of the best things about being rich, [hero.name]!"
        cassidy.say "I even have some outfits that I've worn once."
        cassidy.say "And I get lost inside of my closet it's so big!"
        $ cassidy.love += 1
    else:
        cassidy.say "Hey - are you being mean to me?"
        cassidy.say "Because if you are, that's not fair, [hero.name]!"
        cassidy.say "It's hard being rich - you have to live up to everyone's expectations!"
    return

label cassidy_talk_books_female:
    bree.say "I read a really good book last week, Cassidy."
    bree.say "Would you like to borrow it?"
    bree.say "I think you might enjoy it."
    cassidy.say "Two things, [hero.name]..."
    cassidy.say "Number one, I'm rich."
    cassidy.say "So I don't need to read anything I don't want to."
    cassidy.say "Number two, I don't borrow things."
    cassidy.say "I buy them new and untouched by the hands of the poor!"
    return

label cassidy_talk_people_female:
    bree.say "You must get to meet a lot of interesting people, Cassidy."
    bree.say "You know, what with the circles your mom and dad move in?"
    bree.say "There must be some interesting stories you could tell!"
    cassidy.say "Oh no, [hero.name]...almost none at all."
    cassidy.say "Most people are SO boring!"
    cassidy.say "I just forget everything they say to me."
    cassidy.say "Like I delete it, and poof - it's gone!"
    return

label cassidy_talk_computers_female:
    bree.say "I bet you can afford a top-of-the-range computer, Cassidy!"
    bree.say "And keep up with all the upgrades in the tech too!"
    bree.say "What kind of computer are you using at the moment?"
    cassidy.say "Oh, [hero.name]...you're so funny!"
    cassidy.say "I don't need to use a computer."
    cassidy.say "I just use my phone, like a normal person!"
    return

label cassidy_talk_music_female:
    cassidy.say "Eww...what is that awful sound?"
    bree.say "Oh...it's Sasha's band 'The Deathless Harpies'."
    bree.say "This is a track off their new album, Cassidy."
    cassidy.say "Well, it sounds more like somebody being tortured!"
    bree.say "So it's not your cup of tea, Cassidy."
    bree.say "What kind of music do you like?"
    cassidy.say "I don't know, [hero.name]."
    cassidy.say "I don't really do music..."
    return

label cassidy_talk_birthday_female:
    bree.say "Happy Birthday, Cassidy!"
    cassidy.say "Oh, [hero.name]...you remembered!"
    cassidy.say "Maybe I was wrong about you!"
    bree.say "Wait...what?!?"
    $ cassidy.love += 3
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
