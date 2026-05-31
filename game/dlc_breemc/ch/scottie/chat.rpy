label scottie_desire_0_female:
    scottie.say "I should hang out at your place more, [hero.name]."
    scottie.say "You need a real manly man to keep you entertained."
    scottie.say "Not that dweeb [mike.name]!"
    if scottie.love >= mike.love:
        bree.say "Oh, Scottie!"
        bree.say "Don't be mean to poor [mike.name]!"
        bree.say "But I would like you to hang out here more often..."
        $ scottie.love += 1
    else:
        bree.say "Urgh...you're such a jerk, Scottie!"
        bree.say "At least [mike.name] HAS a brain between his ears."
        bree.say "All you have there is cotton wool!"
        $ scottie.sub += 1
    return

label scottie_desire_1_female:
    scottie.say "Hanging with you is great, [hero.name]."
    scottie.say "You're a really great chick."
    scottie.say "And you're super-hot too!"
    if hero.charm < 19:
        bree.say "Aww...thank you, Scottie!"
        bree.say "I like hanging out with you too."
        bree.say "And a compliment like that is never a bad thing either!"
        $ scottie.love += 1
    else:
        bree.say "Yeah, but it's not like that for me, Scottie."
        bree.say "Because I have to make all the conversation and be interesting for the two of us."
        bree.say "I mean, you're not exactly Mr Charisma, are you?"
        $ scottie.sub += 1
    return

label scottie_desire_2_female:
    scottie.say "[hero.name]..."
    scottie.say "Why do you do stuff like hanging out and playing video-games with [mike.name]?"
    scottie.say "The guy's a total dork - you should be spending time with me instead!"
    if scottie.love >= mike.love:
        bree.say "There's no reason to be jealous, Scottie."
        bree.say "[mike.name]'s just a friend, I promise."
        bree.say "And I always save the REALLY fun games to play with you!"
        $ scottie.love += 1
    else:
        bree.say "Maybe because [mike.name]'s not a pumped up Jerk, Scottie?"
        bree.say "And maybe because he likes me for me."
        bree.say "Rather than for the size of my rack!"
        $ scottie.sub += 1
    return

label scottie_desire_3_female:
    scottie.say "You know that we like...hang out a lot, [hero.name]?"
    scottie.say "And it's a really good time, right?"
    scottie.say "Like maybe we should hang out more seriously?"
    if scottie.love >= 120 - hero.charm/2:
        bree.say "Scottie, are you asking me on a date?"
        bree.say "Because that's what I translated it as!"
        bree.say "And yeah, that sounds like fun!"
        $ scottie.love += 1
    else:
        bree.say "Scottie, you REALLY need to think before you speak."
        bree.say "Because I have no idea what you're babbling about!"
        bree.say "Like, did you even go to school at all?"
        $ scottie.sub += 1
    return

label scottie_desire_4_female:
    scottie.say "WHOA...[hero.name]!"
    scottie.say "You are looking mega hot today!"
    scottie.say "Like they could put you in an art gallery or something!"
    if scottie.love > 100:
        bree.say "You mean I'm like a work of art?"
        bree.say "Oh, Scottie - that's so kind of you to say."
        bree.say "And you didn't mention my ass once!"
        $ scottie.love += 1
    else:
        bree.say "Yeah well, that makes one of us, Scottie."
        bree.say "You'd be more at home in the Zoo!"
        bree.say "Or maybe a museum as a specimen of Neanderthal Man!"
        $ scottie.sub += 1
    return

label scottie_desire_5_female:
    scottie.say "I...I never felt this way about a girl before, [hero.name]!"
    scottie.say "It's like, you're super hot and sexy."
    scottie.say "But that's not all I love about you."
    scottie.say "I like...love all the stuff you say and do too!"
    if hero.knowledge < 19:
        bree.say "Aw, Scottie - you're such a big dope!"
        bree.say "But I love you too, you know that?"
        bree.say "I really do!"
        $ scottie.love += 1
    else:
        bree.say "Watch out using all of those big words, Scottie."
        bree.say "You don't want to go overheating your brain."
        bree.say "You know, burn out that one last brain cell?"
        $ scottie.sub += 1
    return

label scottie_love_0_female:
    scottie.say "You know, [hero.name] - I've had it!"
    scottie.say "Why is everyone in the world dumber than me?"
    scottie.say "It makes my life SO frikin hard!"
    if hero.knowledge < 19:
        bree.say "Oh, Scottie!"
        bree.say "You're such a big dope!"
        bree.say "You wanna talk about it?"
        $ scottie.love += 1
    else:
        bree.say "Yeah, Scottie, that's right."
        bree.say "It's the world that's dumb and not you!"
        bree.say "Geez you're a moron!"
        $ scottie.sub += 1
    return

label scottie_love_1_female:
    scottie.say "Hey, [hero.name]!"
    scottie.say "How's my favourite girl?"
    scottie.say "Things going your way today, I hope?"
    if scottie.love > 100:
        bree.say "I wish I could be as positive as you, Scottie."
        bree.say "I don't know how you do it!"
        bree.say "Honestly, it's like you can just turn your brain off!"
        $ scottie.love += 1
    else:
        bree.say "Well, things were picking up."
        bree.say "Until you showed up that is."
        bree.say "Now it's all going downhill again..."
        $ scottie.sub += 1
    return

label scottie_love_2_female:
    scottie.say "Hey, [hero.name] - looking good there!"
    scottie.say "Someone's been hitting the gym."
    scottie.say "And it's paying off big time!"
    if hero.fitness > 20:
        bree.say "Erm...no, Scottie!"
        bree.say "No more than usual..."
        bree.say "You really think I look that good?"
        $ scottie.love += 1
    else:
        bree.say "Scottie, what have I told you about ogling me?"
        bree.say "I'm a human being, you need to look me in the eye."
        bree.say "Not stare at my chest and objectivise me!"
        $ scottie.sub += 1
    return

label scottie_love_3_female:
    scottie.say "Hey, [hero.name] - you free tomorrow, around lunch?"
    scottie.say "I was thinking we could go grab a bite to eat."
    scottie.say "You know...just you and me...alone?"
    if scottie.love > 100:
        bree.say "Ooh...that kind of sounds like a date, Scottie!"
        bree.say "But no worries, I'd love to do that."
        bree.say "Don't tell me where we're going - keep it a surprise!"
        $ scottie.love += 1
    else:
        bree.say "Yeah, Scottie, let me guess..."
        bree.say "You want to go somewhere they just serve red meat, right?"
        bree.say "The kind of place where they say rude things about vegans?"
        $ scottie.sub += 1
    return

label scottie_love_4_female:
    scottie.say "I want to hang out with you more, [hero.name]."
    scottie.say "I mean I REALLY want to spend more time with you!"
    scottie.say "I dunno why - but I can't stop thinking about you!"
    if scottie.love > 100:
        bree.say "Aww, Scottie - you have a crush on me, don't you?"
        bree.say "That's so cute!"
        bree.say "Sure thing, of course we can hang out more."
        $ scottie.love += 1
    else:
        bree.say "Urgh...I'm not feeling it, Scottie."
        bree.say "I mean, like if you want to hang out with me and my friends, maybe."
        bree.say "But not just the two of us - no way!"
        $ scottie.sub += 1
    return

label scottie_love_5_female:
    scottie.say "[hero.name], I need your help!"
    scottie.say "I keep feeling all funny when I'm around you."
    scottie.say "And when I'm not, it's even worse!"
    scottie.say "All I think about then is being with you as soon as I can!"
    if scottie.love > 150:
        bree.say "Oh, Scottie - you're in love with me, aren't you?"
        bree.say "It's okay, it's okay, because..."
        bree.say "Well...because I love you too!"
        $ scottie.love += 1
    else:
        bree.say "Sounds like you're losing your tiny mind, Scottie!"
        bree.say "Seriously, go see a doctor and get some pills or something."
        bree.say "Because you're not getting anything from me!"
        $ scottie.sub += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
