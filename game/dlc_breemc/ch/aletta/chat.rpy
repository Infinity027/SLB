label aletta_desire_0_female:
    if randint(1, 2) == 1:
        aletta.say "You should try harder at work."
        menu:
            "Yes boss":
                bree.say "Yes boss."
                aletta.say "Good boy."
                $ aletta.sub -= 1
            "I work enough":
                bree.say "I work hard enough."
                aletta.say "Lazy ass..."
                $ aletta.love -= 1
            "You can trust me":
                bree.say "You can trust me Aletta."
                aletta.say "Thank you [hero.name]."
                $ aletta.love += 1
            "Let me handle things":
                bree.say "You should step back and let me handle things."
                aletta.say "..."
                $ aletta.sub += 1
    else:
        aletta.say "Did you get the reports done?"
        menu:
            "Yes boss":
                bree.say "Yes boss."
                aletta.say "Good boy."
                $ aletta.sub -= 1
            "I'll do them later":
                bree.say "I'll get them done when I get them done."
                aletta.say "..."
                $ aletta.love -= 1
            "Of course":
                bree.say "Of course I did Aletta."
                aletta.say "Great."
                $ aletta.love += 1
            "Don't worry":
                bree.say "You should mind your own business and not worry about me."
                $ aletta.sub += 1
    return

label aletta_desire_1_female:
    if randint(1, 2) == 1:
        aletta.say "What do you think of Audrey?"
        menu:
            "She's lazy":
                bree.say "She's too lazy, not doing her share of work if I can say so."
                $ aletta.love += 1
            "She's hot":
                bree.say "She's hot as fuck."
                $ aletta.love -= 1
            "I prefer older women":
                bree.say "She's too young to know what a woman should be."
                $ aletta.love += 1
            "I prefer willful women":
                bree.say "She's too meek for my tastes."
                $ aletta.sub -= 1
    else:
        aletta.say "What do you like to do for fun?"
        menu:
            "Working out":
                bree.say "Working out mostly. I like to stay fit."
                $ aletta.love += 1
            "Picking up chicks":
                bree.say "Picking up chicks at the local bar."
                $ aletta.love -= 1
            "Reading":
                bree.say "I love to read for hours."
                $ aletta.love += 1
            "Watching T.V.":
                bree.say "Watching T.V. and being lazy."
                $ aletta.sub -= 1
    return

label aletta_desire_2_female:
    if randint(1, 2) == 1:
        aletta.say "Why don't you try being more manly."
        menu:
            "Yes":
                bree.say "Yes ma'am."
                $ aletta.sub -= 1
            "Fuck off":
                bree.say "Fuck off."
                $ aletta.love -= 1
            "I am manly already":
                bree.say "I am manly enough."
                $ aletta.love += 1
            "Let me show you":
                bree.say "Why don't you get on my lap so that I can show you manly."
                $ aletta.sub += 1
    else:
        aletta.say "Would you like to see the new gun I just got?"
        menu:
            "Be Intrigued":
                bree.say "That sounds interesting."
                $ aletta.sub -= 1
            "Don't Care":
                bree.say "Not interested."
                $ aletta.love -= 1
            "Maybe later":
                bree.say "I'm busy right now, but you can show me later."
                $ aletta.love += 1
            "I'll protect you":
                bree.say "You don't need a gun as long as you have me to protect you."
                $ aletta.sub += 1
    return

label aletta_desire_3_female:
    if randint(1, 2):
        aletta.say "Men are such pussies."
        menu:
            "Women are our leaders":
                bree.say "We need women to lead us."
                $ aletta.sub -= 1
            "What crap":
                bree.say "What crap."
                $ aletta.love -= 1
            "Some maybe":
                bree.say "Some more than others."
                $ aletta.love += 1
            "Not me":
                bree.say "I am no pussy Aletta, want me to show you?"
                $ aletta.sub += 1
    else:
        aletta.say "Are you seeing someone?"
        menu:
            "No":
                bree.say "No, I don't get many dates."
                $ aletta.sub -= 1
            "A lot":
                bree.say "Yeah, anyone I want, when I want."
                $ aletta.love -= 1
            "It's not your business":
                bree.say "I don't see how that is any of your business."
                $ aletta.love += 1
            "I can date you":
                bree.say "I still have some time for you."
                $ aletta.sub += 1
    return

label aletta_desire_4_female:
    if randint(1, 2) == 1:
        aletta.say "Why don't you try being more manly."
        menu:
            "Sure":
                bree.say "Yes ma'am."
                $ aletta.sub -= 1
            "Fuck off":
                bree.say "Fuck off."
                $ aletta.love -= 1
            "I am more than enough":
                bree.say "I am manly enough."
                $ aletta.love += 1
            "On your knees, bitch":
                bree.say "Why don't you get on your knees so that I can show you manly."
                $ aletta.sub += 1
    else:
        aletta.say "How many women have you slept with?"
        menu:
            "That's too personal":
                bree.say "Oh that's too personal."
                $ aletta.sub -= 1
            "Dozens":
                bree.say "Dozens before you, and dozens after you."
                $ aletta.love -= 1
            "Tell me about you":
                bree.say "I'll tell you if you tell me how many men you have been with."
                $ aletta.love += 1
            "Enough":
                bree.say "Enough to know how to make you scream..."
                $ aletta.sub += 1
                $ aletta.love += 1
    return

label aletta_desire_5_female:
    aletta.say "What's your favorite sex toy?"
    menu:
        "Anything you like":
            bree.say "Anything you want to use on me."
            $ aletta.sub -= 1
        "You":
            bree.say "You."
            if aletta.sub >= 125:
                $ aletta.love += 2
            elif aletta.sub >= 75:
                $ aletta.love += 1
            else:
                $ aletta.love -= 1
        "Let me show you":
            bree.say "How about I show you instead?"
            $ aletta.love += 1
        "Whatever keeps you in line":
            bree.say "Whatever keeps you in line the best."
            $ aletta.sub += 1
            $ aletta.love += 1
    return

label aletta_love_0_female:
    aletta.say "How do you feel about smoking?"
    menu:
        "It's your choice":
            bree.say "If you enjoy it I don't have a problem with it."
            $ aletta.sub -= 1
        "I only smoke while drunk":
            bree.say "I only smoke when I get drunk."
            $ aletta.love -= 1
        "It's bad for the health":
            bree.say "You should care more about your health if you smoke."
            $ aletta.love += 1
        "You shouldn't smoke":
            bree.say "Smoking isn't lady like at all."
            $ aletta.sub += 1
    return

label aletta_love_1_female:
    aletta.say "What do you think of career minded women?"
    menu:
        "We need women to lead us":
            bree.say "Men need women to lead us."
            $ aletta.sub -= 1
        "I am better than any woman":
            bree.say "I could probably do a better job than her and earn more money either way."
            $ aletta.love -= 1
        "She's flawed":
            bree.say "I think she would be someone who hasn't been cared for properly."
            $ aletta.love += 1
        "It's not her place":
            bree.say "If she was with me she would have to become a housewife."
            $ aletta.sub += 1
    return

label aletta_love_2_female:
    aletta.say "How do you feel about women who date married men?"
    menu:
        "I don't judge":
            bree.say "It isn't my place to judge."
            $ aletta.sub -= 1
        "She's a slut":
            bree.say "She sounds slutty."
            $ aletta.love -= 1
        "The man is at fault":
            bree.say "A better question is why is a married man dating someone else?"
            $ aletta.love += 1
        "She would be better with me":
            bree.say "If she were mine she wouldn't need anyone else."
            $ aletta.sub += 1
    return

label aletta_love_3_female:
    aletta.say "What do you think of Audrey?"
    menu:
        "She's lazy":
            bree.say "She's too lazy, not doing her share of work if I can say so."
            $ aletta.love += 1
        "She's hot":
            bree.say "She's hot as fuck."
            $ aletta.love -= 1
        "I prefer older women":
            bree.say "She's too young to know what a woman should be."
            $ aletta.love += 1
        "I prefer willful women":
            bree.say "She's too meek for my tastes."
            $ aletta.sub -= 1
    return

label aletta_love_4_female:
    aletta.say "When are you going to ask me out?"
    menu:
        "You should ask me":
            bree.say "I was waiting for you to ask me."
            $ aletta.sub -= 1
        "When I do":
            bree.say "When I feel like it."
            $ aletta.love -= 1
        "Be patient":
            bree.say "Be patient Aletta."
            $ aletta.love += 1
        "When you are ready":
            bree.say "When I feel you are ready for a date."
            $ aletta.sub += 1
    return

label aletta_love_5_female:
    aletta.say "How would you feel if I asked you over for drinks?"
    menu:
        "I would obey":
            bree.say "I would come if it would make you happy."
            $ aletta.sub -= 1
        "I'd check my schedule":
            bree.say "I would have to make sure I don't have something better to do."
            $ aletta.love -= 1
        "I am the one who would ask":
            bree.say "Isn't it my job to ask you over for drinks?"
            $ aletta.love += 1
        "It would be the best night for you":
            bree.say "I would come over to show you the best night of your life."
            $ aletta.sub += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
