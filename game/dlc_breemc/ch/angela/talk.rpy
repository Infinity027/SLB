label angela_talk_love_female:
    bree.say "I sometimes wonder if there's such a thing as true love, Angela."
    bree.say "But I suppose you'd know better than me, wouldn't you?"
    bree.say "After all, you've been married and raised kids."
    angela.say "I don't know, [hero.name]."
    angela.say "I used to think that I knew what love was, that I had it in spades."
    angela.say "But it turns out it was all a lie - so I don't have a clue!"
    return

label angela_talk_sex_female:
    bree.say "I feel weird asking you about stuff like this, Angela..."
    bree.say "But I want to know what a more experienced woman thinks."
    bree.say "You don't stop enjoying sex, do you?"
    bree.say "I mean when you get a little bit...older!"
    angela.say "Hey, [hero.name]...I'm not that old!"
    angela.say "And for the record - no, you don't stop enjoying it at all!"
    $ angela.love += 1
    return

label angela_talk_politics_female:
    bree.say "I don't know why more young people aren't into politics, Angela."
    bree.say "It's really important stuff and it affects all of us."
    bree.say "How can they be soi cynical?"
    angela.say "I can't throw stones on that issue, [hero.name]."
    angela.say "I totally lost touch with politics when I started a family."
    angela.say "I was so tied up with raising [mike.name] and Minami, you know?"
    $ angela.love -= 1
    return

label angela_talk_food_female:
    bree.say "Ooh...I can feel my stomach growling!"
    bree.say "Time to feed the ravenous beast!"
    bree.say "I'm going to call for a pizza."
    bree.say "You want some, Angela?"
    angela.say "Take-out pizza?!?"
    angela.say "That's no good for you, [hero.name]!"
    angela.say "Let me cook you a good, home-made meal instead."
    $ angela.love += 1
    return

label angela_talk_travels_female:
    bree.say "I really want to see the world some day, Angela."
    bree.say "But I guess that's something everyone wants."
    bree.say "Have you ever managed to do any travelling?"
    angela.say "[mike.name]'s dad and I actually took our act to a lot of different places."
    angela.say "Sure, we were always working."
    angela.say "But we took time out to see the sights whenever we could."
    return

label angela_talk_tv_female:
    bree.say "I know that I should cut down on how much TV I watch, Angela."
    bree.say "But I just love the chance to sit down and tune the world out."
    bree.say "I suppose you've got more discipline than me, right?"
    angela.say "Erm, no, [hero.name]...I'm addicted to my soap operas!"
    angela.say "When the kids were at home, I never had the time."
    angela.say "But since [mike.name] and Minami both moved out, I've had more time on my hands."
    angela.say "And I filled it up watching the TV!"
    $ angela.love += 1
    return

label angela_talk_sports_female:
    bree.say "I'm not into sports in general, Angela."
    bree.say "I just don't get the appeal."
    bree.say "You know what I mean, right?"
    angela.say "I didn't like sports until [mike.name] and Minami started playing them."
    angela.say "But then I really got into cheering them on from the side-lines."
    angela.say "And I kind of miss that, you know?"
    return

label angela_talk_fashion_female:
    bree.say "Do you keep up with the latest fashions, Angela?"
    bree.say "My Mom's always saying that she's too busy!"
    bree.say "How about you?"
    angela.say "I know what she means, [hero.name]!"
    angela.say "I wouldn't have a clue what's on trend right now!"
    angela.say "But who knows, what with the kids flying the nest."
    angela.say "Maybe I'll have a bit more time for myself."
    $ angela.love -= 1
    return

label angela_talk_books_female:
    bree.say "I keep trying to spend a little time reading every day."
    bree.say "It's hard sometimes, but I almost always manage to squeeze it in."
    bree.say "How about you, Angela?"
    angela.say "Oh, [hero.name]...this is really embarrassing!"
    angela.say "But I'm not a big reader."
    angela.say "I normally only read trashy romance novels!"
    return

label angela_talk_people_female:
    bree.say "I try to keep an open mind, Angela."
    bree.say "But people are like...I dunno, such massive jerks!"
    bree.say "Sometimes I wonder why I bother."
    angela.say "Oh no, [hero.name]...you can't think like that!"
    angela.say "Not everyone in the world can be a jerk."
    angela.say "You just have to look for the good in people."
    return

label angela_talk_computers_female:
    bree.say "Did they have computers when you were young, Angela?"
    bree.say "I mean, like...my generation grew up with them being a thing."
    bree.say "I can't imagine them not being a part of life!"
    angela.say "I'm not that old, [hero.name]!"
    angela.say "And yes, there were computers around back then too!"
    angela.say "But they weren't as fancy and powerful as they are now."
    angela.say "Maybe that's why I'm not a computer person..."
    $ angela.love += 1
    return

label angela_talk_music_female:
    bree.say "[mike.name] and Minami are always playing music and going to gigs."
    bree.say "Did you have a musical thing going on when they were growing up?"
    bree.say "You know, Angela - did they get it from you?"
    angela.say "Not really, [hero.name]!"
    angela.say "That was more their father's thing."
    angela.say "I just like to hum along to the radio once in a while."
    return

label angela_talk_birthday_female:
    bree.say "Happy Birthday, Angela!"
    bree.say "Hope you have a good one!"
    angela.say "Oh, [hero.name]..."
    angela.say "Aren't you sweet to think of me!"
    $ angela.love += 2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
