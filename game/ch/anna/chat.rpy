label anna_desire_0_male:
    if hero.has_skill("guitar"):
        anna.say "Oh, I'm so happy you joined the band."
        menu:
            "I just hope I will not screw up":
                mike.say "Same here - I just hope that I don't screw it up!"
                anna.say "Don't worry - I'm sure you'll be great."
            "It was on a whim":
                mike.say "I kind of did it on a whim."
                anna.say "Erm...okay."
                $ anna.love -= 1
            "We will make great music":
                mike.say "I think we're gonna make some great music together, Anna."
                anna.say "Aw, thank you [hero.name]!"
                $ anna.love += 1
            "I'll take us to legendary status":
                mike.say "I'm going to take us all the way to being rock legends!"
                anna.say "Wow!"
                $ anna.sub += 1
    else:
        anna.say "So, did you like our music?"
        menu:
            "It was shitty":
                mike.say "Nah - it was pretty shitty."
                anna.say "Erm...okay."
            "I prefer pop music":
                mike.say "To be honest, it wasn't my kind of thing."
                mike.say "I normally listen to pop music."
                anna.say "Jesus wept..."
                $ anna.love -= 1
            "Yes":
                mike.say "Of course I did - you guys are great."
                anna.say "Oh, thank you!"
                $ anna.love += 1
            "You should practice more":
                mike.say "You sound pretty raw - practice some more and you'll be great."
                $ anna.sub += 1
    return

label anna_desire_1_male:
    if not hero.has_skill("guitar"):
        anna.say "[hero.name]...what do you think of Sasha."
        menu:
            "She's mean":
                mike.say "She's pretty mean - I don't think she should talk to you like that."
                $ anna.love += 1
            "She's hot":
                mike.say "Phew - she's hot as fuck!"
                $ anna.love -= 1
            "She's fun":
                mike.say "She's pretty fun to be around - I really like snarky women."
                $ anna.love -= 1
            "Not much":
                mike.say "Ah...I don't really like her all that much."
                mike.say "Confession time - I like you a lot better."
                $ anna.sub += 1
    else:
        anna.say "So, what is it you like to do for fun?"
        menu:
            "Working out":
                mike.say "I like to work out mostly - you know, trying to keep in shape?"
                $ anna.love -= 1
            "Picking up chicks":
                mike.say "I like to cruise round the local bars, picking up babes."
                $ anna.love -= 1
            "Reading":
                mike.say "I tend to find that I read, often for hours at a time."
                $ anna.love += 1
            "Watching T.V.":
                mike.say "I tend to just vegetate in front of the TV."
    return

label anna_desire_2_male:
    if not hero.has_skill("guitar"):
        anna.say "[hero.name]...what do you think of Kleio?"
        menu:
            "She's annoying":
                mike.say "Christ the girl's annoying as hell!"
                $ anna.love -= 1
            "She's hot":
                mike.say "Wow - she is just as hot as hell!"
                $ anna.love -= 1
            "She's fun":
                mike.say "She's pretty fun to hang around with."
                $ anna.love += 1
            "Not much":
                mike.say "To be honest, I don't like her all that much."
                mike.say "I much prefer hanging around with you."
                $ anna.sub += 1
    else:
        anna.say "You wanna listen to the new album I just got?"
        menu:
            "Be Intrigued":
                mike.say "Yeah, Anna - you have great taste in music, so it should be interesting."
                $ anna.love += 1
            "Don't Care":
                mike.say "Nah...not interested."
                $ anna.love -= 1
            "Maybe later":
                mike.say "I'm busy right now, Anna - but I'd love for you to show me later."
                $ anna.love += 1
    return

label anna_desire_3_male:
    if not hero.has_skill("guitar"):
        anna.say "I just love metal - no other music comes close to that feeling of sheer raw power!"
        menu:
            "It's just noise":
                mike.say "It's just noise, not music - makes my ears bleed."
                $ anna.love -= 1
            "What crap":
                mike.say "What load of crap!"
                $ anna.love -= 2
            "Me too":
                mike.say "Me too - I agree with you one hundred percent."
                $ anna.love += 1
            "Power metal is the metal of metal":
                mike.say "Power metal is the shit - metal turned all the way up to eleven!"
                $ anna.sub += 1
    else:
        anna.say "Erm, [hero.name]...are you seeing someone right now?"
        menu:
            "No":
                mike.say "No, not really - I never seem to get many dates."
            "A lot":
                mike.say "Hell yeah - who I want and when I want to see them!"
                $ anna.love += 1
            "It's not your business":
                mike.say "Is that really any of your business, Anna?"
                $ anna.love -= 1
            "I can date you":
                mike.say "Don't worry, Anna - I can always make time for you..."
                $ anna.sub += 1
    return

label anna_desire_4_male:
    anna.say "Can I ask how many women you've slept with?"
    menu:
        "That's too personal":
            mike.say "Wow - that's kind of a personal question, don't you think?"
        "Dozens":
            mike.say "There were dozens before I met you, and there'll be dozens more after you."
            $ anna.love -= 1
        "Tell me about you":
            mike.say "I'll show you mine if you'll show me yours - tell me how many men you've been with, and I'll spill my guts."
            $ anna.love += 1
        "Enough":
            mike.say "Don't worry, I've been with enough to know what'll make you scream..."
            $ anna.sub += 1
    $ anna.love += 1
    return

label anna_desire_5_male:
    anna.say "Hey, [hero.name] - what's your favorite sex toy?"
    menu:
        "Anything you like":
            mike.say "I'm cool with anything that you want to use on me."
            $ anna.sub -= 1
        "You":
            mike.say "I have this cute little sex-doll that I like to call 'Anna'!"
            if anna.sub >= 75:
                $ anna.love += 2
            elif anna.sub >= 40:
                $ anna.love += 1
            else:
                $ anna.love -= 1
        "Let me show you":
            mike.say "Let me give you a practical demonstration..."
            $ anna.love += 1
        "Whatever keeps you in line":
            mike.say "Whatever the hell keeps your little ass in line."
            $ anna.sub += 1
    $ anna.love += 1
    return

label anna_love_0_male:
    anna.say "What do you think of girls that like to sleep with...girls?"
    menu:
        "It's your choice":
            mike.say "Hey, you do you - if that's what you like, that's what you like."
        "That's hot":
            mike.say "Oh yeah - I think it's fucking hot!"
            $ anna.love -= 1
        "Love is love":
            mike.say "Love is love, you can't keep it from taking whatever form it needs to in order to flourish."
            $ anna.love += 1
    return

label anna_love_1_male:
    anna.say "Erm...do you like piercings?"
    menu:
        "Not much":
            mike.say "Ah...they're not really my kind of thing."
        "You shouldn't defile your body":
            mike.say "The almighty shaped you in his own image, so you shouldn't defile his creation."
            $ anna.love -= 1
        "It's hot":
            mike.say "Yeah, very much so - piercings look really hot on a girl."
            $ anna.love += 1
        "The more the better":
            mike.say "Oh yes indeed - the more the better!"
            $ anna.sub += 1
    return

label anna_love_2_male:
    anna.say "[hero.name], what do you think of girls that date a lot of different guys?"
    menu:
        "I don't judge":
            mike.say "Nobody would judge a guy for dating a lot of different girls - and it's not really for me to judge, either."
            $ anna.love += 1
        "They're sluts":
            mike.say "Huh...sounds like you're talking about some real big slut right there!"
            $ anna.love -= 1
        "They would be better with me":
            mike.say "Trust me, if the girl you're talking about had been with me, then she wouldn't need another man."
            $ anna.sub += 1
    return

label anna_love_3_male:
    anna.say "Ah...sometimes I wish I was so much smarter..."
    menu:
        "You are plenty smart":
            mike.say "You might not be joining MENSA anytime soon, Anna - but you're smart enough for me."
            $ anna.love += 1
        "Me too":
            mike.say "Yeah, I know where you're coming from there - I wish you were smarter too!"
            $ anna.love -= 1
    return

label anna_love_4_male:
    anna.say "Hey, [hero.name] - when are you going to get your act together and ask me out?"
    menu:
        "You should ask me":
            mike.say "Well, I was kinda waiting for you to ask me!"
        "When I do":
            mike.say "I'll ask you out when I feel like it, and not before."
            $ anna.love -= 1
        "Be patient":
            mike.say "Hey, Anna - you just be patient now!"
            $ anna.love += 1
        "When you are ready":
            mike.say "I'll ask you out on a date just as soon as I think you're ready for one."
            $ anna.sub += 1
    return

label anna_love_5_male:
    anna.say "[hero.name] - what would you say if I...I don't know, maybe asked you over for drinks?"
    menu:
        "I would accept":
            mike.say "I'd make sure to be there, Anna - if that'd make you happy."
        "I'd check my schedule":
            mike.say "Ah...I'd need to check my diary first, make sure I didn't have someplace better to be."
            $ anna.love -= 1
        "I am the one who would ask":
            mike.say "Hey, are you calling me a bad friend?"
            mike.say "Isn't it me that's supposed to be the one asking you over?"
            $ anna.love += 1
        "It would be the best night for you":
            mike.say "I'd use the excuse of drinks to come over, sure."
            mike.say "But what I'd really want is to show you the night of your life!"
            $ anna.sub += 1
    return

label anna_good_sweet_talk_male:
    show anna
    if anna.love > 133:
        mike.say "Oh wow...your ass, Anna!"
        mike.say "It just hypnotises me - I can't keep my hands off it!"
        show anna blush
        anna.say "That's no problem - I love your hands on it!"
    elif anna.love > 66:
        mike.say "You're a lot of fun, Anna!"
        mike.say "And I love spending time with you."
        show anna wink
        anna.say "You're fun too - so we make a great pair!"
    else:
        mike.say "I love your hair, Anna."
        mike.say "The colour's so wild!"
        show anna happy
        anna.say "Aww...thank you!"
    hide anna
    return

label anna_bad_sweet_talk_male:
    show anna
    mike.say "Huh..."
    mike.say "Anna, I think your breasts are actually bigger than your head!"
    show anna angry
    anna.say "What's that supposed to mean?!?"
    anna.say "That I'm dumb, but it's okay because I have big tits?!?"
    mike.say "That's not what I meant!"
    hide anna
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
