label kylie_talk_love_female:
    show kylie
    bree.say "It feels kind of funny to admit this, Kylie - you know, as a modern girl."
    bree.say "But a big part of me still believes in true love, just like I did as a kid!"
    bree.say "I bet you think that's silly, right?"
    kylie.say "Oh no, [hero.name]!"
    kylie.say "No way!"
    kylie.say "I believe everybody has a soulmate out there somewhere."
    kylie.say "You just have to figure who they are."
    kylie.say "And then spend the rest of your life trying to win their heart!"
    $ kylie.love += 1
    hide kylie
    return

label kylie_talk_sex_female:
    show kylie
    bree.say "We're modern, liberated women, right, Kylie?"
    bree.say "So we should be able to talk about sex without feeling guilty."
    bree.say "I mean, it's not like we don't enjoy it!"
    kylie.say "You're right, [hero.name]!"
    kylie.say "We shouldn't be ashamed to admit that we like it as much as guys."
    kylie.say "Slut-shaming's a crime against the sexual sisterhood!"
    $ kylie.love += 1
    hide kylie
    return

label kylie_talk_politics_female:
    show kylie
    bree.say "You never mentioned your political beliefs, Kylie."
    bree.say "You can't be an adult and not even have an opinion!"
    bree.say "That's like opting out of life!"
    kylie.say "I'm not left or right on any issue, [hero.name]."
    kylie.say "I have one of those brains that's...different."
    kylie.say "And none of the politicians really speak to me."
    kylie.say "Not like the voices in my head..."
    $ kylie.love -= 1
    hide kylie
    return

label kylie_talk_food_female:
    show kylie
    bree.say "You've got one of those...erm...classical figures, Kylie!"
    bree.say "You know, curves that go on forever!"
    bree.say "I don't know how you do it - I have to starve myself to keep my figure!"
    kylie.say "Oh, you mentioned starving yourself, [hero.name]!"
    kylie.say "And that's making me think of food!"
    kylie.say "The only thing that comes close to sex!"
    $ kylie.love += 1
    hide kylie
    return

label kylie_talk_travels_female:
    show kylie
    bree.say "Seems like everyone wants to travel the world, Kylie."
    bree.say "I guess you're one of them too, right?"
    kylie.say "I can't deny it, [hero.name] - I would love to travel."
    kylie.say "But I could only do it with the right companion."
    kylie.say "Seeing all of those sights and sharing those memories with them..."
    kylie.say "Now that would be perfect!"
    $ kylie.love += 1
    hide kylie
    return

label kylie_talk_tv_female:
    show kylie
    bree.say "I hope I remembered to set the DVR."
    bree.say "There's a new drama I want to catch."
    bree.say "One where detectives are hunting a serial-killer!"
    kylie.say "Urgh!"
    kylie.say "I hate those kind of shows!"
    kylie.say "They always try to demonise the killer."
    kylie.say "Nobody ever tries to see it from their point of view!"
    $ kylie.love -= 1
    hide kylie
    return

label kylie_talk_sports_female:
    show kylie
    bree.say "[mike.name]'s claimed the TV tonight, which sucks!"
    bree.say "He says that he wants to watch some dumb soccer game."
    bree.say "Can you believe that?!?"
    kylie.say "You shouldn't dump on sports like that, [hero.name]."
    kylie.say "They're a great way to get closer to a guy."
    kylie.say "Better to be snuggled up to him watching sports than not at all!"
    $ kylie.love += 1
    hide kylie
    return

label kylie_talk_fashion_female:
    show kylie
    bree.say "Ah..."
    bree.say "I wish I had a figure like your's, Kylie!"
    bree.say "It's so full and feminine."
    bree.say "It makes everything you wear look amazing!"
    kylie.say "Aw, thank you, [hero.name]!"
    kylie.say "That's so sweet of you to say!"
    kylie.say "I'm glad some people appreciate my curves!"
    hide kylie
    $ kylie.love += 1
    return

label kylie_talk_books_female:
    show kylie
    bree.say "You always seem to have your nose in a text-book, Kylie."
    bree.say "What do you read when you're not studying?"
    bree.say "I mean, what do you read for pleasure?"
    kylie.say "I don't, [hero.name] - read anything, that is."
    kylie.say "I spend most of my spare time doing...other things..."
    $ kylie.love -= 1
    hide kylie
    return

label kylie_talk_people_female:
    show kylie
    bree.say "Do you have many friends apart from me and [mike.name], Kylie?"
    bree.say "I never seem to see you hanging around with anyone else on campus."
    kylie.say "I've never really had what you'd call friends, [hero.name]."
    kylie.say "To be honest, most people just don't interest me."
    kylie.say "I tend to focus all my attention on just a few people."
    kylie.say "Or even just the one..."
    hide kylie
    return

label kylie_talk_computers_female:
    show kylie
    bree.say "How's your laptop holding up this term, Kylie?"
    bree.say "I need to get mine serviced, make sure it doesn't die on me!"
    kylie.say "It's not alive, [hero.name] - so it can't actually die."
    kylie.say "You shouldn't talk about inanimate objects like that."
    kylie.say "Not when living things are so frail!"
    $ kylie.love -= 1
    hide kylie
    return

label kylie_talk_music_female:
    show kylie
    bree.say "Listen to this track, Kylie - it's a real ear-worm!"
    bree.say "I've been playing it non-stop since I heard it."
    kylie.say "Number one, no thank you."
    kylie.say "And number two, that's a horrible mental image!"
    kylie.say "An ear-worm - really?"
    hide kylie
    return

label kylie_talk_birthday_female:
    show kylie
    bree.say "Happy Birthday, Kylie!"
    bree.say "It...it is today, isn't it?"
    kylie.say "O...M...G!"
    kylie.say "Yes, [hero.name], it's today!"
    kylie.say "I can't believe you found out!"
    kylie.say "I must have underestimated you..."
    $ kylie.love += 3
    hide kylie
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
