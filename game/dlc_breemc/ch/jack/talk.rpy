label jack_talk_love_female:
    show jack
    jack.say "Ah, [hero.name]..."
    jack.say "This is going to sound a little lame..."
    jack.say "But do you believe in love - you know, like true love?"
    menu:
        "I do":
            bree.say "Aw, Jack - that's not lame at all!"
            bree.say "I could believe in a guy that believes in true love."
            bree.say "Probably fall in love with him too!"
            "Jack smiles and blushes, suddenly coming over all bashful."
            $ jack.love += 1
        "There's no such thing as \"true love\"":
            bree.say "Urgh...Jack, that's SO predictable!"
            bree.say "That kind of thing's just made up for Hollywood movies!"
            jack.say "Oh...okay, [hero.name] - sure!"
            "Jack tries to brush it off, like he doesn't care."
            "But he looks more than a little disappointed with my answer."
            $ jack.love -= 1
        "I'll teach you what's \"true love\"":
            bree.say "I believe you need to know who's in charge, Jack."
            bree.say "Men love to know their place!"
            "Jack nods eagerly at this, his cheeks flushing red."
            $ jack.sub += 1
        "If you do so do I":
            bree.say "I believe in it if that's what you believe, Jack!"
            bree.say "If it'll make you happy, yeah?"
            "Jack nods and smiles at this, a confident look on his face."
            $ jack.sub -= 1
    hide jack
    return

label jack_talk_sex_female:
    show jack
    jack.say "People are always telling me that I should join a gym, [hero.name]."
    jack.say "But I think a guy can get enough exercise doing other things."
    jack.say "Like things that happen in the bedroom, yeah?"
    menu:
        "That's right!":
            bree.say "You got that right, Jack!"
            bree.say "It's the most fun two people can have together."
            bree.say "And you don't have to pay a fee either!"
            "I add a sly wink to emphasize my point."
            "And Jack cracks a smile of his own too."
            $ jack.love += 1
        "Working out is a better option":
            bree.say "Hmm...I don't agree, Jack."
            bree.say "Working out gives a guy more stamina, you know?"
            bree.say "Keeps him harder and makes him go faster too."
            "Jack gives me an awkward smile and then gazes down at his gut."
            "I don't think that was the answer he wanted."
            $ jack.love -= 1
        "You'll be out of breath with me":
            bree.say "Don't worry about needing a workout, Jack."
            bree.say "I'll make sure that you sweat enough!"
            "Jack's eyes go wide, and he looks delighted with my answer."
            $ jack.sub += 1
        "I might help you exercise then":
            bree.say "Oh, I don't know where I'd even begin, Jack!"
            bree.say "But I'm sure that you could show me, right?"
            "Jack nods and smiles at this, a confident look on his face."
            $ jack.sub -= 1
    hide jack
    return

label jack_talk_politics_female:
    show jack
    jack.say "I don't really do right or left when it comes to politics, [hero.name]."
    jack.say "I like to take good ideas from both sides."
    jack.say "That way you can have the best of both worlds, right?"
    menu:
        "Same mind set applies to me":
            bree.say "Me too, Jack, me too."
            bree.say "People at the extremes never see the whole picture."
            bree.say "They're just so blinkered!"
            "Jack nods, clearly pleased to hear me agree with him."
            $ jack.love += 1
        "You're just a ignorant then":
            bree.say "No way, Jack!"
            bree.say "That's just what stupid people say."
            bree.say "People too ignorant to understand important issues!"
            "Jack looks surprised and even a little embarrassed."
            "And he quickly tries to change the subject."
            $ jack.love -= 1
        "What do I care?":
            bree.say "Did I ask you for your opinion on politics, Jack?!?"
            jack.say "Erm...no, [hero.name] - I guess not!"
            bree.say "Then shut up until I do!"
            "Jack nods at this, his cheeks flushing red."
            $ jack.sub += 1
        "I guess...":
            bree.say "If you say so, Jack."
            bree.say "I don't know too much about politics."
            bree.say "Sounds like you could educate me though!"
            "Jack nods and smiles at this, a confident look on his face."
            $ jack.sub -= 1
    hide jack
    return

label jack_talk_food_female:
    show jack
    jack.say "Mmm...I'm hungry, [hero.name]!"
    jack.say "How about you?"
    "As he says this, Jack glances down at his belly."
    "It's obvious that he's feeling self-conscious about it."
    menu:
        "Me too":
            bree.say "Me too, Jack - I could eat a horse!"
            bree.say "Times like this, I can't help it."
            bree.say "All I want to do is pig-out!"
            "Jack smiles at this, relieved at my answer."
            $ jack.love += 1
        "Don't you think you've ate enough?":
            "Which he really should be with a gut like that!"
            bree.say "Ah, maybe you should cut down a little, Jack?"
            bree.say "Maybe eat a bit more salad?"
            "I poke a finger into his belly, just to drive home the point."
            "Jack looks ashamed of himself, letting me know he gets the message."
            $ jack.love -= 1
        "We'll go eat only if you behave":
            bree.say "If you want a snack, then you'll have to earn it, Jack!"
            bree.say "Be a good boy, and you just might deserve it!"
            "I can almost hear the sound of Jack's stomach rumbling."
            "But he nods all the same, eager to agree to my terms."
            $ jack.sub += 1
        "Let's go grab you something":
            bree.say "Then we really should get you something to eat, Jack!"
            bree.say "We can't have you passing out!"
            bree.say "You need to keep your strength up!"
            "Jack nods and smiles at this, a confident look on his face."
            $ jack.sub -= 1
    hide jack
    return

label jack_talk_travels_female:
    show jack
    jack.say "I know where I'd go if I had the cash, [hero.name]."
    jack.say "I'd do Tokyo - stay as long as I possibly could!"
    jack.say "That'd be pretty cool, right?"
    menu:
        "Totally!":
            bree.say "You read my mind, Jack!"
            bree.say "Just think of all the cool Japanese arcades we could visit!"
            bree.say "The stores full of anime stuff we can't get over here too!"
            "Every word I say makes Jack nod faster than ever."
            "He seems delighted that I agree with him."
            $ jack.love += 1
        "So obvious of you":
            "I shake my head and laugh."
            bree.say "Oh, Jack - you're such a nerd!"
            bree.say "Don't you ever want to do adult stuff for a change?"
            bree.say "You can play videogames and watch cartoons here at home!"
            "Jack nods and laughs weakly."
            "But it's clear that wasn't the answer he was looking for."
            $ jack.love -= 1
        "Don't you dare leave me":
            bree.say "You're not going anywhere without my saying so, Jack!"
            bree.say "Not even to the end of the street - never mind Japan!"
            "Jack nods at this, his cheeks flushing red."
            jack.say "Ah...yeah, [hero.name]...you're the boss!"
            $ jack.sub += 1
        "Bring me with you please":
            bree.say "You wouldn't go without me - would you, Jack?"
            bree.say "And I couldn't go on my own."
            bree.say "I'd need you to be my special tour-guide!"
            "Jack nods and smiles at this, a confident look on his face."
            $ jack.sub -= 1
    hide jack
    return

label jack_talk_tv_female:
    show jack
    jack.say "Isn't this a great time to be alive, [hero.name]?"
    jack.say "There's so much good stuff to binge on TV."
    jack.say "I just wish I had time to watch it all!"
    menu:
        "Best moment to be alive indeed":
            bree.say "You said it, Jack!"
            bree.say "I feel like I should just take a month off to catch up."
            bree.say "Hell, maybe even a year!"
            "Jack smiles and nods eagerly, happy to have me agree with him."
            $ jack.love += 1
        "That's nothing more than a distraction to me":
            bree.say "Nah, I don't have room for TV, Jack."
            bree.say "It's just wasting time I could have spent gaming!"
            "Jack nods at this, but he looks a little disappointed."
            "I don't think that was the answer he wanted to hear."
            $ jack.love -= 1
        "Don't tell me you've watched series I'm into...":
            bree.say "What have you been binging, Jack?!?"
            bree.say "It'd better not be the series I'm into!"
            bree.say "You know I don't like you seeing them before I do!"
            jack.say "O...okay, [hero.name]!"
            jack.say "How about you tell me what I can watch in future?"
            $ jack.sub += 1
        "As long as I can watch series with you":
            bree.say "You know I love the same things that you do, Jack."
            bree.say "So how about we get together to watch?"
            bree.say "And you can pick the shows, yeah?"
            "Jack nods and smiles at this, a confident look on his face."
            $ jack.sub -= 1
    hide jack
    return

label jack_talk_sports_female:
    show jack
    jack.say "Yeah...I'm not one of those stereotypical guys."
    jack.say "You know - the kind that are into sports?"
    jack.say "Like, that's all they can even talk about!"
    menu:
        "Yeah, the classic \"I'm the alpha male\" type of guy":
            bree.say "Urgh...don't get me started on those assholes!"
            bree.say "They're just a bunch of dumb jocks that never grew up."
            bree.say "I'm more of E-Sports kind of girl!"
            "Jack smiles and nods eagerly, happy to have me agree with him."
            $ jack.love += 1
        "What a surprise!":
            "I can't help letting out a snigger at this."
            bree.say "Ah, yeah, Jack - I kind of noticed that!"
            bree.say "You're more of a classic nerd, right?"
            "Jack nods at this, but he looks more than a little disappointed."
            "I don't think that was the answer he wanted to hear."
            $ jack.love -= 1
        "Trust me, you will love sport with me":
            bree.say "You don't need to worry about sports, Jack."
            bree.say "I'll make sure your energy gets put to good use!"
            "Jack nods at this, his cheeks flushing red."
            jack.say "You got it, [hero.name]!"
            $ jack.sub += 1
        "I can't stand any kind of physical activity":
            bree.say "Eww...I HATE sports, Jack!"
            bree.say "I'm just so glad that you do too!"
            "Jack nods and smiles at this, a confident look on his face."
            $ jack.sub -= 1
    hide jack
    return

label jack_talk_fashion_female:
    show jack
    jack.say "I think people are just being conned with fashion, [hero.name]."
    jack.say "It's another way to make money, you see?"
    jack.say "You should just find your own style and go with it."
    menu:
        "There's shallow people everywhere":
            bree.say "Yeah, I feel the same way, Jack."
            bree.say "People are too hung up on the way they look."
            bree.say "It's what's on the inside that counts, right?"
            "Jack nods eagerly, pleased to find that I agree with him."
            $ jack.love += 1
        "It's probably just you not taking care of your style":
            bree.say "I don't think band T-shirts and jeans counts as a style, Jack!"
            bree.say "And what's wrong with taking pride in your appearance?"
            bree.say "Maybe if you updated your wardrobe you'd change your mind?"
            "Jack nods at this, but he looks more than a little hurt."
            "I don't think that was the answer he wanted to hear."
            $ jack.love -= 1
        "Don't get too attached to yours though":
            bree.say "Hmm...you can dress like that for now, Jack."
            bree.say "But you'll have to change it up if I get tired of it."
            bree.say "Okay?"
            jack.say "Uh...okay, [hero.name]!"
            $ jack.sub += 1
        "You look perfect the way you are":
            bree.say "Oh, you're SO right, Jack!"
            bree.say "I'd never ask you to change how you look."
            bree.say "That'd be so shallow of me!"
            "Jack nods and smiles at this, a confident look on his face."
            $ jack.sub -= 1
    hide jack
    return

label jack_talk_books_female:
    show jack
    jack.say "I know that I should read more adult stuff, [hero.name]."
    jack.say "But every time I see a shiny new comic-book..."
    jack.say "It's like I turn into a kid all over again!"
    menu:
        "You should only read things that you like":
            bree.say "There's no shame in that, Jack."
            bree.say "Reading should be something you do because you love it."
            bree.say "Not something that's a chore!"
            "Jack nods eagerly, pleased to find that I agree with him."
            $ jack.love += 1
        "That's kinda sad to still read comics at your age":
            bree.say "Oh, Jack - you really are a big kid!"
            bree.say "Are you ever going to get serious and grow up?"
            "Jack nods at this, but he looks more than a little hurt."
            "I don't think that was the answer he wanted to hear."
            $ jack.love -= 1
        "I'll knock some motivation into you":
            bree.say "Maybe you just need the right motivation, Jack?"
            bree.say "Someone to discipline you and punish you when you slack off?"
            "Jack nods at this, his cheeks flushing red."
            jack.say "You got it, [hero.name]!"
            $ jack.sub += 1
        "I'd like to discover what's so cool about comics":
            bree.say "I'm out of touch with comic-books, Jack."
            bree.say "Maybe you could give me a crash-course?"
            bree.say "If you did, then you'd be my hero!"
            "Jack nods and smiles at this, a confident look on his face."
            $ jack.sub -= 1
    hide jack
    return

label jack_talk_people_female:
    show jack
    jack.say "It's not like I'm anti-social or anything, [hero.name]."
    jack.say "I just feel like, people in general, they don't get me."
    jack.say "You know what I mean when I say that?"
    menu:
        "I don't like people either":
            bree.say "Oh, totally, Jack, totally!"
            bree.say "People in general are the worst!"
            bree.say "That's why I like more quirky types - quirky's my normal!"
            "Jack nods eagerly, pleased to find that I agree with him."
            $ jack.love += 1
        "I know why they don't get you...":
            bree.say "Well, of course they don't get you, Jack!"
            bree.say "You're a bit of a freak, aren't you?"
            bree.say "So normal people are never going to understand you!"
            "Jack nods at this, but he looks more than a little hurt."
            "I don't think that was the answer he wanted to hear."
            $ jack.love -= 1
        "Who cares about the others?!":
            bree.say "The only person you have to worry about getting you is me, Jack!"
            bree.say "Everyone else you can pretty much ignore - you hear me?"
            "Jack nods, eager to show that he does."
            jack.say "Sure thing, [hero.name] - whatever you say!"
            $ jack.sub += 1
        "No one gets you as much as I do":
            bree.say "Oh, forget about normal people, Jack!"
            bree.say "They'll never understand you."
            bree.say "Not like I do!"
            "Jack nods and smiles at this, a confident look on his face."
            $ jack.sub -= 1
    hide jack
    return

label jack_talk_computers_female:
    show jack
    jack.say "I can't imagine living in a time before computers existed, [hero.name]!"
    jack.say "I mean just think of all the things we use them for in the space of a day."
    jack.say "It's scary how lost we'd be without them!"
    menu:
        "That's surrealist how true it is":
            bree.say "Yeah, Jack - it's pretty mind-blowing!"
            bree.say "Kind of like living in the Matrix for real, right?"
            "Jack nods eagerly, pleased to find that I agree with him."
            jack.say "Exactly, [hero.name] - I knew you'd get it!"
            $ jack.love += 1
        "Like you know anything on that topic...":
            bree.say "You don't need to talk to me about computers, Jack!"
            bree.say "I live and breathe technology - twenty-four seven!"
            bree.say "In fact, I probably know WAY more than you do!"
            "Jack nods at this, but he looks more than a little hurt."
            "I don't think that was the answer he wanted to hear."
            $ jack.love -= 1
        "You are alike":
            bree.say "You're like a computer, Jack."
            bree.say "You're easy to turn on and follow basic instructions!"
            bree.say "Which is just the way I like it!"
            "Jack nods at this, his cheeks flushing red."
            jack.say "You got it, [hero.name]!"
            $ jack.sub += 1
        "You seem so knowledgeable on that topic!":
            bree.say "Wow...you sound like you know your stuff, Jack!"
            bree.say "How about to give me some private IT lessons?"
            "Jack nods and smiles at this, a confident look on his face."
            $ jack.sub -= 1
    hide jack
    return

label jack_talk_music_female:
    show jack
    jack.say "You gotta admit it, [hero.name] - heavy metal's music at it's best!"
    jack.say "The power, the passion, the sheer bad-assery!"
    jack.say "Nothing kicks it like metal!"
    menu:
        "It's the best for games":
            bree.say "It sure makes a game kick ass, Jack!"
            bree.say "Metal on the soundtrack makes it better."
            bree.say "Anything else is lame!"
            "Jack nods eagerly, pleased to find that I agree with him."
            $ jack.love += 1
        "It only fits for a specific type of person":
            bree.say "Oh, Jack - you're so silly!"
            bree.say "Metal's for sad guys that never had girlfriends."
            bree.say "That's why it's all about repressed, adolescent sexuality!"
            "Jack nods at this, but he looks more than a little hurt."
            "I don't think that was the answer he wanted to hear."
            $ jack.love -= 1
        "Metal is nothing compare to me":
            bree.say "Never mind heavy metal, Jack."
            bree.say "I'm the biggest bad-ass in your life - right?!?"
            "Jack nods at this, his cheeks flushing red."
            jack.say "You got it, [hero.name]!"
            $ jack.sub += 1
        "If you say so then it must be true":
            bree.say "Whatever you say, Jack."
            bree.say "You're the expert, not me!"
            "Jack nods and smiles at this, a confident look on his face."
            $ jack.sub -= 1
    hide jack
    return

label jack_talk_birthday_female:
    show jack happy
    bree.say "Hey, Jack..."
    bree.say "Happy Birthday!"
    jack.say "Wow...[hero.name]...you remembered!"
    jack.say "That's so cool!"
    $ jack.love += 3
    hide jack
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
