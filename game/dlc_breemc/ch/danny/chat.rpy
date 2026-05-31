label danny_desire_0_female:
    danny.say "Whoa, [hero.name]..."
    danny.say "You should dress like that more often."
    bree.say "Huh?"
    bree.say "Like what, Danny?"
    danny.say "Like you're almost naked!"
    danny.say "That's a good look for you!"
    if hero.morality > 0:
        bree.say "Oh, Danny..."
        bree.say "You're such a bad boy!"
        bree.say "But I do kinda love it when you talk like that."
        danny.say "You know it's the truth!"
        $ danny.love += 1
    else:
        bree.say "Hey!"
        bree.say "You shouldn't talk to me like that, Danny."
        bree.say "I'm a modern woman, and I deserve respect!"
        danny.say "Wha...what did I do?"
        danny.say "That was supposed to be a compliment!"
        $ danny.love -= 1
    return

label danny_desire_1_female:
    bree.say "Danny..."
    bree.say "Why are you hanging back like that?"
    bree.say "Why don't you want to walk beside me?"
    danny.say "Isn't it obvious, [hero.name]?"
    danny.say "I can't check out your ass from there."
    danny.say "Back here I can see it wiggling while you walk!"
    if hero.morality > 0:
        bree.say "Danny!"
        bree.say "Are you saying this outfit makes my butt look huge?!?"
        danny.say "What?"
        danny.say "Your butt looks great!"
        danny.say "I mean, yeah - it's big."
        danny.say "But like, big in a good way, you know?"
        $ danny.love += 1
    else:
        bree.say "You can't follow me round like that all day!"
        bree.say "Just come here and walk by me, okay?"
        bree.say "If you do, I promise to make it up to you later..."
        danny.say "Well, when you put it like that..."
        danny.say "I'm gonna be right by your side!"
        $ danny.sub += 1
    return

label danny_desire_2_female:
    if not hero.flags.haircut:
        danny.say "I was gonna ask, [hero.name]..."
        danny.say "What colour do you dye your hair?"
        bree.say "Oh, I don't dye it, Danny..."
        bree.say "This is my natural colour."
        danny.say "You're serious?"
        danny.say "Wow..."
        danny.say "I like that kind of slutty blonde colour."
        danny.say "But I thought it only came out of a bottle!"
        if danny.sub >= 20:
            bree.say "Slutty blonde, huh?"
            bree.say "You really can't hide it, can you?"
            danny.say "Huh..."
            danny.say "What do you mean?"
            bree.say "Oh come on, Danny - you're horny twenty-four seven!"
            bree.say "Even looking at my hair turns you on, doesn't it?"
            danny.say "Yeah, yeah..."
            danny.say "You got me, [hero.name] - I'm kind of an old romantic like that!"
            $ danny.sub += 1
        else:
            bree.say "Slutty blonde?!?"
            bree.say "What's that supposed to mean?"
            bree.say "Blonde's put out more?"
            danny.say "Geez, [hero.name]..."
            danny.say "I didn't invent the name."
            danny.say "It's just something they call it."
            danny.say "I always thought it was a compliment!"
            $ danny.love -= 1
    return

label danny_desire_3_female:
    danny.say "Hey, [hero.name]..."
    danny.say "What's brown and sticky?"
    bree.say "I heard that one already!"
    bree.say "It's a stick."
    danny.say "Nah, it's a piece of shit!"
    bree.say "Eww!"
    bree.say "What's with the crappy jokes?"
    danny.say "I was trying to make you laugh so hard you had a wardrobe malfunction, [hero.name]."
    danny.say "Then I could watch you change your panties!"
    if hero.morality <= -25:
        bree.say "You can stop with the lame attempts at humour, Danny."
        bree.say "Because they're never going to help you get into a girl's underwear!"
        danny.say "Ouch!"
        danny.say "You're a harsh critic, [hero.name]."
        bree.say "Not if you just ask me politely."
        bree.say "Then I might actually let you have what you want..."
        $ danny.sub += 1
    else:
        bree.say "Double eww!"
        bree.say "You're a disgusting animal, Danny!"
        danny.say "Ah, my jokes are wasted on you, [hero.name]."
        danny.say "You just don't have a sense of humour."
        $ danny.love -= 1
    return

label danny_desire_4_female:
    danny.say "You wanna come for a ride, [hero.name]?"
    danny.say "It's all rev'd up and ready to go!"
    bree.say "Ooh..."
    bree.say "Are you talking about your motorbike, Danny?"
    danny.say "Heh, heh..."
    danny.say "Nah, [hero.name] - I mean my manhood!"
    danny.say "It's getting hard with me just thinking about you!"
    if danny.sexperience >= 5:
        bree.say "Oh, Danny..."
        bree.say "You're so predictable."
        bree.say "But that's one of the things I love about you."
        danny.say "And my cock, right?"
        danny.say "You love that too?"
        bree.say "Yeah, yeah - that too."
        $ danny.love += 1
    else:
        bree.say "Urgh..."
        bree.say "You really do have a one-track mind."
        bree.say "You know that?"
        danny.say "So what if I do, [hero.name]?"
        danny.say "What else should a red-blooded guy have on his mind?"
        $ danny.love -= 1
    return

label danny_desire_5_female:
    danny.say "I can't deny it any longer, [hero.name]..."
    danny.say "I need yah bad."
    bree.say "That's hardly news to me, Danny."
    bree.say "You've always got sex on your mind!"
    danny.say "It's different this time."
    danny.say "I'll die if I don't get into your panties!"
    danny.say "I swear it's true!"
    if danny.sexperience >= 8 and hero.morality <= -25:
        bree.say "Oh, Danny..."
        bree.say "You really know how to treat a lady!"
        danny.say "Huh?"
        danny.say "I do?!?"
        bree.say "Nah, you're totally clueless."
        bree.say "But lucky for you, you're also hot."
    else:
        bree.say "I don't think so, Danny..."
        bree.say "I already have one asshole in there."
        bree.say "And I don't think there's room for another!"
        danny.say "Ouch, [hero.name]..."
        danny.say "That was seriously savage!"
    return

label danny_love_0_female:
    danny.say "Say, [hero.name]..."
    danny.say "Are you like, doing anything?"
    danny.say "Or going anywhere right now?"
    bree.say "Erm..."
    bree.say "No, Danny..."
    bree.say "I was going to hang around here."
    bree.say "Why do you ask?"
    danny.say "Oh...no reason."
    danny.say "I was just going to hang around here too, that's all."
    if danny.love >= 20 or hero.morality >= 50:
        bree.say "That's cool then."
        bree.say "We'll just hang out together then."
        bree.say "You and me, yeah?"
        danny.say "Sure we will, [hero.name]."
        danny.say "Just the two of us."
        $ danny.love += 1
    else:
        bree.say "Oh..."
        bree.say "You're just saying that to be nice, aren't you?"
        danny.say "No, [hero.name] - I'm not!"
        bree.say "It's okay, Danny."
        bree.say "I'll get out of here."
        bree.say "Sorry again for making it awkward."
        danny.say "Well fuck my life!"
        $ danny.love -= 1
    return

label danny_love_1_female:
    danny.say "Over here, [hero.name]!"
    danny.say "I saved a spot for you!"
    bree.say "Oh, you didn't have to do that, Danny."
    danny.say "I know, I know..."
    danny.say "But...well..."
    danny.say "We're friends, right?"
    danny.say "And that's the kind of shit friends do..."
    danny.say "Am I right?"
    if danny.sub >= 20:
        bree.say "Of course we are, Danny!"
        bree.say "I mean, I assume we are."
        bree.say "You think we're friends, don't you?"
        danny.say "Oh sure, [hero.name]..."
        danny.say "I think we're friends."
        danny.say "Like, we're real good friends!"
        $ danny.love += 1
    else:
        bree.say "Erm..."
        bree.say "I think what we are is acquaintances."
        bree.say "But friends?"
        bree.say "I don't think we're quite there yet!"
        danny.say "Geez..."
        danny.say "Now I wish I hadn't bothered!"
        $ danny.love -= 1
    return

label danny_love_2_female:
    danny.say "You know something, [hero.name]..."
    bree.say "I know a lot of things, Danny."
    bree.say "What was the one you're thinking of?"
    danny.say "Okay, smart-ass..."
    danny.say "I was just gonna say I never much hang-out with chicks."
    danny.say "But I like doing it with you - you're okay."
    if hero.fun >= 4:
        bree.say "You mean I'm more like a guy?"
        danny.say "No, [hero.name] - that's not what I meant!"
        bree.say "It's okay, Danny..."
        bree.say "I'm just fucking with you."
        bree.say "I like hanging-out with you too."
        bree.say "You're kind of my first biker!"
        $ danny.love += 1
        $ danny.sub += 1
    else:
        bree.say "Yeah, Danny..."
        bree.say "I could have guessed you don't have many female friends."
        bree.say "Calling them chicks probably doesn't help!"
        danny.say "Why are you being like that, [hero.name]?"
        danny.say "I was just trying to be nice!"
        bree.say "Well maybe try a little harder next time."
        $ danny.love -= 1
        $ danny.sub -= 1
    return

label danny_love_3_female:
    danny.say "I don't want to just hang-out today, [hero.name]."
    danny.say "We do shit like that all the time."
    bree.say "Huh?"
    bree.say "Isn't that what friends do, Danny?"
    bree.say "They hang-out and talk about random shit."
    danny.say "Yeah, but we're more than friends!"
    bree.say "We are?"
    danny.say "Sure we are!"
    danny.say "Aren't we?"
    if danny.sexperience >= 3:
        bree.say "I hope we are, Danny!"
        bree.say "It's kind of hard to admit stuff like that."
        danny.say "Fuck!"
        danny.say "Ain't that the truth!"
        bree.say "I really feel like we are more than friends."
        bree.say "I might not know what we are instead."
        bree.say "But we're definitely more than friends."
        $ danny.love += 1
    else:
        bree.say "Yeah..."
        bree.say "I think you might have skipped ahead a couple of levels there."
        bree.say "Might be time to back up and see where the other person's at, Danny!"
        danny.say "Erm..."
        danny.say "I dunno what most of that meant, [hero.name]..."
        danny.say "But I'm guessing it wasn't good?"
        $ danny.love -= 1
    return

label danny_love_4_female:
    danny.say "Hey, [hero.name]..."
    danny.say "I got a bone to pick with you!"
    bree.say "What's the matter, Danny?"
    bree.say "Did I do something to piss you off?"
    danny.say "Yeah, [hero.name]..."
    danny.say "You like bewitched me with your feminine powers or something!"
    danny.say "I can't stop thinking about you!"
    bree.say "Are you..."
    bree.say "Are you trying to say that you love me?!?"
    danny.say "Whoa..."
    danny.say "I think I am!"
    if danny.love >= 190:
        bree.say "That's okay, Danny..."
        bree.say "Because I've been feeling the same way too!"
        danny.say "Holy shit!"
        danny.say "You mean that..."
        bree.say "Yes, Danny..."
        bree.say "I think I love you too!"
        danny.say "Oh man..."
        danny.say "This is like something out of a fucking movie!"
        $ danny.love += 1
    else:
        bree.say "Well how is any of that my fault, Danny?"
        bree.say "You're a grown man, a big scary biker."
        bree.say "You're supposed to be in control of your own shit!"
        danny.say "Oh man..."
        danny.say "This isn't how it goes in the movies!"
        danny.say "I got totally lied to by Hollywood!"
        $ danny.love -= 1
    return

label danny_love_5_female:
    danny.say "Gurgh..."
    danny.say "Argh..."
    danny.say "It's no good..."
    danny.say "I can't fight it no more!"
    bree.say "Bloody hell, Danny..."
    bree.say "Are you okay?"
    danny.say "No, [hero.name], I ain't okay!"
    danny.say "I can't keep it in any longer..."
    danny.say "I love ya, [hero.name]!"
    danny.say "I love ya like crazy!"
    if danny.love >= 190 and hero.fun >= 6:
        bree.say "You do?"
        bree.say "Because I do too!"
        bree.say "I mean I love you!"
        bree.say "Not me, obviously..."
        danny.say "Shit..."
        danny.say "That's a relief."
        danny.say "So we're both on the same page!"
        $ danny.love += 1
    else:
        bree.say "Whoa!"
        bree.say "Way to overshare, Danny!"
        danny.say "Wha..."
        danny.say "Wadda ya mean, [hero.name]?"
        danny.say "Don't you feel the same way?"
        bree.say "I was getting there."
        bree.say "Until you dropped all that on me."
        bree.say "But now I think we need to slow down a little."
        danny.say "Well shit..."
        $ danny.love -= 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
