label minami_talk_love_female:
    bree.say "You're young and carefree, right, Minami?"
    bree.say "That means you practically have to believe in love!"
    bree.say "It's like a staple of being young and naive!"
    minami.say "No way, [hero.name]!"
    minami.say "Love's too serious - it's for old people, like you!"
    minami.say "I wanna have fun while I'm young!"
    $ minami.love -= 1
    return

label minami_talk_sex_female:
    bree.say "You're old enough to have done it, right, Minami?"
    bree.say "I mean, it's not gone out of fashion since I was your age, has it?"
    minami.say "What are you talking about, [hero.name]?"
    minami.say "Oh...you mean SEX!"
    minami.say "Of course not!"
    minami.say "I like it whenever I can get it!"
    minami.say "I just wish I could get it more often..."
    $ minami.sub += 1
    return

label minami_talk_politics_female:
    bree.say "Where do you come down in terms of politics, Minami?"
    bree.say "I know that most people of your age are kind of left-leaning."
    bree.say "But if you're more central or even on the right, I'd like to hear your reasons."
    minami.say "Boo...boring!"
    minami.say "Politics makes me yawn, [hero.name]!"
    minami.say "Shut up before you put me in a boredom-induced coma!"
    $ minami.love -= 1
    return

label minami_talk_food_female:
    bree.say "I'm going to do the online shop for the house, Minami."
    bree.say "Is there anything you want adding to the list?"
    minami.say "Huh?!?"
    minami.say "You mean I get to order stuff I want?"
    minami.say "Mom never let me do that back home!"
    bree.say "Well you're one of us now, Minami."
    bree.say "So you get a say in how we do things around here too!"
    minami.say "Thanks, [hero.name] - you rock!"
    $ minami.love += 1
    return

label minami_talk_travels_female:
    bree.say "I always wanted to see the world, Minami."
    bree.say "And I keep the hope alive that I'll be able to one day."
    bree.say "How about you?"
    bree.say "Have you travelled the globe yet?"
    minami.say "Oh hell no, [hero.name]!"
    minami.say "I'm just like you - I wanna, but I can't!"
    minami.say "Mom and Dad never took us on many holidays either."
    minami.say "Almost like they wanted to keep big bro and me as sheltered as possible..."
    $ minami.love += 1
    return

label minami_talk_tv_female:
    bree.say "Hey, Minami - it's TV time!"
    bree.say "Last one down has to sit next to [mike.name]!"
    minami.say "Ooh, TV!"
    minami.say "I'm coming, so you'd better get out of my way!"
    minami.say "I'm not sitting next to my stinky big bro!"
    $ minami.love += 1
    return

label minami_talk_sports_female:
    bree.say "Hmm..."
    bree.say "Looks like there's some serious sports on TV today!"
    bree.say "Any of it take your fancy, Minami?"
    minami.say "Oh god no!"
    minami.say "Sports are the suckiest thing in the world, [hero.name]!"
    minami.say "Everyone knows that!"
    $ minami.love -= 1
    return

label minami_talk_fashion_female:
    bree.say "I've tried my hand at cosplay in the past, Minami."
    bree.say "But I was never able to come up with anything like your stuff!"
    bree.say "You really have a talent there."
    minami.say "Thanks, [hero.name]!"
    minami.say "Most people don't appreciate the work that goes into it!"
    minami.say "Hey, I know - you should try some of them on!"
    bree.say "Oh no, I couldn't!"
    bree.say "Well, maybe just a couple..."
    $ minami.love += 1
    return

label minami_talk_books_female:
    bree.say "Erm, Minami..."
    bree.say "Yeah, [hero.name]...what's up?"
    bree.say "Those manga you're reading...they look really interesting."
    bree.say "Could I maybe borrow one when you're done reading them?"
    minami.say "Sure thing, [hero.name]!"
    minami.say "I've got more in my room too."
    minami.say "Would you like to see them?"
    $ minami.love += 1
    return

label minami_talk_people_female:
    bree.say "You seem to get on well with everyone, Minami."
    bree.say "In fact, I've only ever seen you have a cross word with [mike.name]!"
    bree.say "How on earth do you manage it?"
    minami.say "Oh, well...I guess I just look for the best in people, [hero.name]."
    minami.say "Sometimes it's hard, but it kinda pays off in the end."
    minami.say "Apart from with big bro - he's hopeless!"
    $ minami.love += 1
    return

label minami_talk_computers_female:
    bree.say "The latest update makes Discordant so much easier to use!"
    bree.say "It's like the programmers are finally listening!"
    minami.say "I know what you mean, [hero.name]."
    minami.say "I was thinking of moving to another platform."
    minami.say "But this changes everything!"
    $ minami.love += 1
    return

label minami_talk_music_female:
    bree.say "Hmm..."
    bree.say "Have you seen my Y-Pod, Minami?"
    bree.say "I thought I left it somewhere around here!"
    minami.say "Is that thing your's, [hero.name]?!?"
    minami.say "I thought it was something you found buried in the garden!"
    minami.say "Those things are so old I thought they were all in museums!"
    $ minami.love -= 1
    return

label minami_talk_birthday_female:
    bree.say "Happy Birthday, Minami!"
    bree.say "Many happy returns to the little sister of the house!"
    minami.say "Oh, [hero.name]...you remembered my birthday!"
    minami.say "That's so cool!"
    minami.say "You really are like my big sister!"
    $ minami.love += 5
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
