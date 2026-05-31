label ayesha_desire_0_male:
    ayesha.say "I'm so happy that you're a member of the same gym where I work, [hero.name]."
    ayesha.say "It's great to see you around there so often."
    if hero.charm >= 10:
        mike.say "Me too, Ayesha."
        mike.say "You're one of the reasons I keep going there."
        $ ayesha.love += 1
    else:
        mike.say "Meh - I only keep going there because it's a short drive from home."
        $ ayesha.love -= 1
    return

label ayesha_desire_1_male:
    ayesha.say "I love the chance to hang out with you away from the gym, [hero.name]."
    ayesha.say "I don't want you to think I'm just some dumb muscle-freak!"
    if hero.charm >= 20:
        mike.say "That makes two of us, Ayesha."
        mike.say "I really like getting to know more about you too."
        $ ayesha.love += 1
    else:
        mike.say "I don't know, Ayesha."
        mike.say "Apart from the gym, it's not like we actually have much in common!"
        $ ayesha.love -= 1
    return

label ayesha_desire_2_male:
    ayesha.say "[hero.name]..."
    ayesha.say "What do you think of Hanna?"
    ayesha.say "Do you think she's...pretty?"
    if hero.charm >= 40:
        mike.say "I guess so - if you like that kind of thing."
        mike.say "Don't tell her I said so - but I always thought she was a little bit of a bimbo."
        $ ayesha.love += 1
    else:
        mike.say "Oh, hell yeah!"
        mike.say "She's so hot it makes working out at the gym really hard!"
        $ ayesha.love -= 1
    return

label ayesha_desire_3_male:
    ayesha.say "I've really enjoyed hanging out with you, [hero.name]."
    ayesha.say "But I feel like I want more out of our friendship - if you know what I mean?"
    if hero.charm >= 60:
        mike.say "I'm so glad you said that, Ayesha."
        mike.say "Because I was thinking of how best to say the same thing to you too!"
        $ ayesha.love += 1
    else:
        mike.say "Geez, Ayesha - way to get super clingy and ruin a perfectly good friendship!"
        $ ayesha.love -= 1
    return

label ayesha_desire_4_male:
    ayesha.say "I...I just wanted to say..."
    ayesha.say "You look SO good to me right now, [hero.name]!"
    if hero.charm >= 80:
        mike.say "Thanks for the compliment, Ayesha."
        mike.say "But I was kind of hoping I'd look good enough for you want to touch me too!"
        $ ayesha.love += 1
    else:
        mike.say "Well, at least one of us has got to make an effort, Ayesha."
        $ ayesha.love -= 1
    return

label ayesha_desire_5_male:
    ayesha.say "It's weird, you know - but I can't seem to imagine a day without you."
    ayesha.say "How crazy is that, [hero.name]?"
    if hero.charm >= 90:
        mike.say "It's not so strange, Ayesha."
        mike.say "And I don't want you to have to imagine that."
        mike.say "Because I don't want to go a day without you either."
        $ ayesha.love += 1
    else:
        mike.say "So you're saying you don't have much in the way of imagination?"
        mike.say "Am I right, Ayesha?"
        $ ayesha.love -= 1
    return

label ayesha_love_0_male:
    ayesha.say "Urgh!"
    ayesha.say "I had such a hard day at the gym..."
    if hero.charm >= 10:
        mike.say "Really - would you like to tell me all about it, Ayesha?"
        $ ayesha.love += 1
    else:
        mike.say "Boring!"
        mike.say "That's the last thing I want to hear about!"
        $ ayesha.love -= 1
    return

label ayesha_love_1_male:
    ayesha.say "Hey, [hero.name]."
    ayesha.say "How are you feeling today?"
    if hero.charm >= 20:
        mike.say "I was feeling pretty awful, Ayesha."
        mike.say "But seeing you is a real shot in the arm."
        $ ayesha.love += 1
    else:
        mike.say "Too bad to answer lame questions, Ayesha..."
        $ ayesha.love -= 1
    return

label ayesha_love_2_male:
    ayesha.say "You're looking better than ever, [hero.name]."
    ayesha.say "Those sessions at the gym are really paying off!"
    if hero.charm >= 40:
        mike.say "Aw, I don't know about that, Ayesha!"
        mike.say "And even if I am, it's mainly down to your coaching."
        $ ayesha.love += 1
    else:
        mike.say "Oh god, Ayesha!"
        mike.say "Stop fishing for a compliment already."
        $ ayesha.love -= 1
    return

label ayesha_love_3_male:
    ayesha.say "Would you like to meet up for lunch someday, [hero.name]?"
    ayesha.say "You know - just you and me?"
    if hero.charm >= 60:
        mike.say "Really, Ayesha?"
        mike.say "That sounds perfect!"
        $ ayesha.love += 1
    else:
        mike.say "Is that really such a good idea, Ayesha?"
        mike.say "I mean, aren't you on some kind of complicated diet or something?"
        $ ayesha.love -= 1
    return

label ayesha_love_4_male:
    ayesha.say "I really want to see more of you, [hero.name]."
    ayesha.say "A LOT more..."
    if hero.charm >= 80:
        mike.say "Me too, Ayesha."
        mike.say "And not in the gym either!"
        $ ayesha.love += 1
    else:
        mike.say "Really, Ayesha?"
        mike.say "Well, maybe I could put in more time at the gym..."
        $ ayesha.love -= 1
    return

label ayesha_love_5_male:
    ayesha.say "Th...this...this is really hard for me to say, [hero.name]."
    ayesha.say "But...I think...I think I've fallen in love with you!"
    if hero.charm >= 90:
        mike.say "Oh my god, Ayesha - you do?!?"
        mike.say "I feel the same way about you - I mean, I love you!"
        $ ayesha.love += 1
    else:
        mike.say "That's understandable, Ayesha."
        mike.say "I mean, you don't have much experience with guys..."
        $ ayesha.love -= 10
    return

label ayesha_good_sweet_talk_male:
    show ayesha
    if ayesha.love > 133:
        mike.say "I don't know how you do it, Ayesha."
        mike.say "You're strong and gentle at the same time."
        mike.say "And...well, you're smoking hot too!"
        show ayesha happy
        ayesha.say "Oh, I love it when you talk about me like that!"
    elif ayesha.love > 66:
        mike.say "I love to see you in a dress, Ayesha."
        mike.say "You're so strong and yet so sexy too!"
        mike.say "I'm a one lucky guy!"
        show ayesha blush
        ayesha.say "You really mean that?"
        ayesha.say "I guess I'm pretty lucky too!"
    else:
        mike.say "Wow, Ayesha - you're so smart!"
        mike.say "And funny too!"
        mike.say "There's so much more to you than meets the eye."
        ayesha.say "Aww...you're making me blush!"
    hide ayesha
    return

label ayesha_bad_sweet_talk_male:
    show ayesha
    mike.say "It's great that you can get sexy clothes in your size these days, Ayesha!"
    show ayesha angry
    ayesha.say "What are you trying to say?"
    ayesha.say "That I'm some kind of gigantic freak?!?"
    mike.say "No...no way, Ayesha!"
    hide ayesha
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
