label ayesha_talk_love_female:
    show ayesha
    bree.say "Wow, Ayesha...I mean, just...WOW!"
    bree.say "You're like the biggest girl I've ever seen!"
    bree.say "Guys must be fighting to get with you!"
    ayesha.say "Hmmph..."
    ayesha.say "You might think that's the case, [hero.name]."
    ayesha.say "But the truth is it's not much fun being me!"
    $ ayesha.love -= 1
    hide ayesha
    return

label ayesha_talk_sex_female:
    show ayesha
    bree.say "You're so fit and in such great shape, Ayesha."
    bree.say "And you're so strong too!"
    bree.say "You must be able to do like...well...like crazy things..."
    bree.say "You know...in bed?"
    if ayesha.sub >= 50:
        ayesha.say "Oh, I do whatever my partner tells me, [hero.name]!"
        ayesha.say "Whatever his heart most desires - that's what makes me happy!"
        ayesha.say "The more...interesting... the better I like it!"
        $ ayesha.sub += 1
    else:
        ayesha.say "That's a very personal subject, [hero.name]."
        ayesha.say "One that I'd really rather not talk about!"
        $ ayesha.love -= 1
    hide ayesha
    return

label ayesha_talk_politics_female:
    show ayesha
    bree.say "Which side of the debate are you on, Ayesha?"
    bree.say "I mean, what are your political beliefs?"
    ayesha.say "Religion and politics, [hero.name]!"
    ayesha.say "Those are the two things you should never talk about!"
    ayesha.say "And I always keep them to myself."
    hide ayesha
    return

label ayesha_talk_food_female:
    show ayesha
    bree.say "Ooh..."
    bree.say "I can already feel my stomach rumbling, Ayesha!"
    bree.say "Are you hungry too?"
    bree.say "After all, you are a big girl!"
    ayesha.say "No, [hero.name] - I'm a built girl."
    ayesha.say "And I have to keep to a strict diet to achieve that."
    ayesha.say "I eat to train, not train to eat!"
    $ ayesha.love -= 1
    hide ayesha
    return

label ayesha_talk_travels_female:
    show ayesha
    bree.say "Oh, I really want to get away somewhere this summer, Ayesha!"
    bree.say "It feels like an age since I went somewhere decent on holiday."
    ayesha.say "Ah...."
    ayesha.say "I know what you mean, [hero.name]!"
    ayesha.say "Seeing another part of the world, experiencing another culture."
    ayesha.say "There's really nothing like it!"
    hide ayesha
    return

label ayesha_talk_tv_female:
    show ayesha
    bree.say "Hey, Ayesha - what are you watching on TV right now?"
    bree.say "Anything apart from old wrestling reruns?"
    ayesha.say "No, [hero.name], I'm not watching anything at all."
    ayesha.say "In fact, I don't make a habit of watching TV."
    ayesha.say "I'm the kind of person that likes to do, not watch!"
    $ ayesha.love -= 1
    hide ayesha
    return

label ayesha_talk_sports_female:
    show ayesha
    bree.say "So...you're a wrestler, right, Ayesha?"
    ayesha.say "I was the last time I checked, [hero.name]."
    bree.say "But you're into other sports too, yeah?"
    bree.say "I mean, it's all the same in the end, isn't it?"
    ayesha.say "It most certainly is not!"
    ayesha.say "People in other sports are a bunch of snobs!"
    ayesha.say "They look down on professional wrestling."
    ayesha.say "But they're a bunch of wimps!"
    ayesha.say "Weaklings that wouldn't last a minute in a wrestling ring!"
    $ ayesha.love -= 5
    hide ayesha
    return

label ayesha_talk_fashion_female:
    show ayesha
    bree.say "Oh my, Ayesha - where'd you get that outfit?!?"
    bree.say "It's so flattering - and so feminine too!"
    ayesha.say "Oh...I...well..."
    ayesha.say "It DID take me a lot of effort to pull it together!"
    ayesha.say "Do you really think it looks that good on me?"
    $ ayesha.sub += 1
    hide ayesha
    return

label ayesha_talk_books_female:
    show ayesha
    bree.say "Ayesha, I just finished this great book."
    bree.say "You have to read it yourself."
    bree.say "It's all about..."
    ayesha.say "Erm...no, [hero.name]..."
    ayesha.say "I don't need book recommendations from you."
    ayesha.say "It's probably more trashy than the stuff I like to read anyway..."
    $ ayesha.love -= 1
    hide ayesha
    return

label ayesha_talk_people_female:
    show ayesha
    bree.say "Urgh..."
    bree.say "People - what are they like, Ayesha?!?"
    bree.say "No...wait...I'm generalising."
    bree.say "People are generally good - right?"
    ayesha.say "I think so too, [hero.name]."
    ayesha.say "It's just that the bad ones are louder than the good ones!"
    $ ayesha.sub += 1
    hide ayesha
    return

label ayesha_talk_computers_female:
    show ayesha
    bree.say "I found this great new program for my laptop and..."
    bree.say "Oh, sorry, Ayesha - I'm just assuming you're a tech-head too!"
    ayesha.say "Well...I kind of am, [hero.name]!"
    ayesha.say "So if you want to tell me all about it, then go ahead!"
    $ ayesha.love += 1
    hide ayesha
    return

label ayesha_talk_music_female:
    show ayesha
    bree.say "How are you when it comes to music, Ayesha?"
    bree.say "Are you into all that heavy stuff they play at the wrestling shows?"
    ayesha.say "Well...I don't mind it, [hero.name]."
    ayesha.say "But the truth is that I like all kind of music."
    ayesha.say "And here's a secret..."
    ayesha.say "I sometimes listen to boy bands while I work-out and spar!"
    $ ayesha.love += 2
    hide ayesha
    return

label ayesha_talk_birthday_female:
    show ayesha close
    bree.say "Happy Birthday, Ayesha!"
    bree.say "I hope you have a great day!"
    if ayesha.love >= 50:
        ayesha.say "How..."
        ayesha.say "How did you know?"
        ayesha.say "That's so kind of you to find out!"
        $ ayesha.love += 5
    else:
        ayesha.say "What..."
        ayesha.say "How did you find out it was my birthday?"
        ayesha.say "Have you been spying on me?!?"
        $ ayesha.love -= 1
    hide ayesha
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
