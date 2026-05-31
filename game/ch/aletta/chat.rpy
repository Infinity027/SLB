label aletta_desire_0_male:
    if randint(1, 2) == 1:
        aletta.say "You should try harder at work."
        menu:
            "Yes boss":
                mike.say "Yes boss."
                aletta.say "Good boy."
                $ aletta.sub -= 1
            "I work enough":
                mike.say "I work hard enough."
                aletta.say "Lazy ass..."
                $ aletta.love -= 1
            "You can trust me":
                mike.say "You can trust me Aletta."
                aletta.say "Thank you [hero.name]."
                $ aletta.love += 1
            "Let me handle things":
                mike.say "You should step back and let me handle things."
                aletta.say "..."
                $ aletta.sub += 1
    else:
        aletta.say "Did you get the reports done?"
        menu:
            "Yes boss":
                mike.say "Yes boss."
                aletta.say "Good boy."
                $ aletta.sub -= 1
            "I'll do them later":
                mike.say "I'll get them done when I get them done."
                aletta.say "..."
                $ aletta.love -= 1
            "Of course":
                mike.say "Of course I did Aletta."
                aletta.say "Great."
                $ aletta.love += 1
            "Don't worry":
                mike.say "You should mind your own business and not worry about me."
                $ aletta.sub += 1
    return

label aletta_desire_1_male:
    if randint(1, 2) == 1 and Person.is_not_hidden("audrey"):
        aletta.say "What do you think of Audrey?"
        menu:
            "She's lazy":
                mike.say "She's too lazy, not doing her share of work if I can say so."
                $ aletta.love += 1
            "She's hot":
                mike.say "She's hot as fuck."
                $ aletta.love -= 1
            "I prefer older women":
                mike.say "She's too young to know what a woman should be."
                $ aletta.love += 1
            "I prefer willful women":
                mike.say "She's too meek for my tastes."
                $ aletta.sub -= 1
    else:
        aletta.say "What do you like to do for fun?"
        menu:
            "Working out":
                mike.say "Working out mostly. I like to stay fit."
                $ aletta.love += 1
            "Picking up chicks":
                mike.say "Picking up chicks at the local bar."
                $ aletta.love -= 1
            "Reading":
                mike.say "I love to read for hours."
                $ aletta.love += 1
            "Watching T.V.":
                mike.say "Watching T.V. and being lazy."
                $ aletta.sub -= 1
    return

label aletta_desire_2_male:
    if randint(1, 2) == 1:
        aletta.say "Why don't you try being more manly."
        menu:
            "Yes":
                mike.say "Yes ma'am."
                $ aletta.sub -= 1
            "Fuck off":
                mike.say "Fuck off."
                $ aletta.love -= 1
            "I am manly already":
                mike.say "I am manly enough."
                $ aletta.love += 1
            "Let me show you":
                mike.say "Why don't you get on my lap so that I can show you manly."
                $ aletta.sub += 1
    else:
        aletta.say "Would you like to see the new gun I just got?"
        menu:
            "Be Intrigued":
                mike.say "That sounds interesting."
                $ aletta.sub -= 1
            "Don't Care":
                mike.say "Not interested."
                $ aletta.love -= 1
            "Maybe later":
                mike.say "I'm busy right now, but you can show me later."
                $ aletta.love += 1
            "I'll protect you":
                mike.say "You don't need a gun as long as you have me to protect you."
                $ aletta.sub += 1
    return

label aletta_desire_3_male:
    if randint(1, 2):
        aletta.say "Men are such pussies."
        menu:
            "Women are our leaders":
                mike.say "We need women to lead us."
                $ aletta.sub -= 1
            "What crap":
                mike.say "What crap."
                $ aletta.love -= 1
            "Some maybe":
                mike.say "Some more than others."
                $ aletta.love += 1
            "Not me":
                mike.say "I am no pussy Aletta, want me to show you?"
                $ aletta.sub += 1
    else:
        aletta.say "Are you seeing someone?"
        menu:
            "No":
                mike.say "No, I don't get many dates."
                $ aletta.sub -= 1
            "A lot":
                mike.say "Yeah, anyone I want, when I want."
                $ aletta.love -= 1
            "It's not your business":
                mike.say "I don't see how that is any of your business."
                $ aletta.love += 1
            "I can date you":
                mike.say "I still have some time for you."
                $ aletta.sub += 1
    return

label aletta_desire_4_male:
    if randint(1, 2) == 1:
        aletta.say "Why don't you try being more manly."
        menu:
            "Sure":
                mike.say "Yes ma'am."
                $ aletta.sub -= 1
            "Fuck off":
                mike.say "Fuck off."
                $ aletta.love -= 1
            "I am more than enough":
                mike.say "I am manly enough."
                $ aletta.love += 1
            "On your knees, bitch":
                mike.say "Why don't you get on your knees so that I can show you manly."
                $ aletta.sub += 1
    else:
        aletta.say "How many women have you slept with?"
        menu:
            "That's too personal":
                mike.say "Oh that's too personal."
                $ aletta.sub -= 1
            "Dozens":
                mike.say "Dozens before you, and dozens after you."
                $ aletta.love -= 1
            "Tell me about you":
                mike.say "I'll tell you if you tell me how many men you have been with."
                $ aletta.love += 1
            "Enough":
                mike.say "Enough to know how to make you scream..."
                $ aletta.sub += 1
                $ aletta.love += 1
    return

label aletta_desire_5_male:
    aletta.say "What's your favorite sex toy?"
    menu:
        "Anything you like":
            mike.say "Anything you want to use on me."
            $ aletta.sub -= 1
        "You":
            mike.say "You."
            if aletta.sub >= 125:
                $ aletta.love += 2
            elif aletta.sub >= 75:
                $ aletta.love += 1
            else:
                $ aletta.love -= 1
        "Let me show you":
            mike.say "How about I show you instead?"
            $ aletta.love += 1
        "Whatever keeps you in line":
            mike.say "Whatever keeps you in line the best."
            $ aletta.sub += 1
            $ aletta.love += 1
    return

label aletta_love_0_male:
    aletta.say "How do you feel about smoking?"
    menu:
        "It's your choice":
            mike.say "If you enjoy it I don't have a problem with it."
            $ aletta.sub -= 1
        "I only smoke while drunk":
            mike.say "I only smoke when I get drunk."
            $ aletta.love -= 1
        "It's bad for the health":
            mike.say "You should care more about your health if you smoke."
            $ aletta.love += 1
        "You shouldn't smoke":
            mike.say "Smoking isn't lady like at all."
            $ aletta.sub += 1
    return

label aletta_love_1_male:
    aletta.say "What do you think of career minded women?"
    menu:
        "We need women to lead us":
            mike.say "Men need women to lead us."
            $ aletta.sub -= 1
        "I am better than any woman":
            mike.say "I could probably do a better job than her and earn more money either way."
            $ aletta.love -= 1
        "She's flawed":
            mike.say "I think she would be someone who hasn't been cared for properly."
            $ aletta.love += 1
        "It's not her place":
            mike.say "If she was with me she would have to become a housewife."
            $ aletta.sub += 1
    return

label aletta_love_2_male:
    aletta.say "How do you feel about women who date married men?"
    menu:
        "I don't judge":
            mike.say "It isn't my place to judge."
            $ aletta.sub -= 1
        "She's a slut":
            mike.say "She sounds slutty."
            $ aletta.love -= 1
        "The man is at fault":
            mike.say "A better question is why is a married man dating someone else?"
            $ aletta.love += 1
        "She would be better with me":
            mike.say "If she were mine she wouldn't need anyone else."
            $ aletta.sub += 1
    return

label aletta_love_3_male:
    if randint(1, 2) == 1 and Person.is_not_hidden("audrey"):
        aletta.say "What do you think of Audrey?"
        menu:
            "She's lazy":
                mike.say "She's too lazy, not doing her share of work if I can say so."
                $ aletta.love += 1
            "She's hot":
                mike.say "She's hot as fuck."
                $ aletta.love -= 1
            "I prefer older women":
                mike.say "She's too young to know what a woman should be."
                $ aletta.love += 1
            "I prefer willful women":
                mike.say "She's too meek for my tastes."
                $ aletta.sub -= 1
    else:
        aletta.say "What do you like to do for fun?"
        menu:
            "Working out":
                mike.say "Working out mostly. I like to stay fit."
                $ aletta.love += 1
            "Picking up chicks":
                mike.say "Picking up chicks at the local bar."
                $ aletta.love -= 1
            "Reading":
                mike.say "I love to read for hours."
                $ aletta.love += 1
            "Watching T.V.":
                mike.say "Watching T.V. and being lazy."
                $ aletta.sub -= 1
    return

label aletta_love_4_male:
    aletta.say "When are you going to ask me out?"
    menu:
        "You should ask me":
            mike.say "I was waiting for you to ask me."
            $ aletta.sub -= 1
        "When I do":
            mike.say "When I feel like it."
            $ aletta.love -= 1
        "Be patient":
            mike.say "Be patient Aletta."
            $ aletta.love += 1
        "When you are ready":
            mike.say "When I feel you are ready for a date."
            $ aletta.sub += 1
    return

label aletta_love_5_male:
    aletta.say "How would you feel if I asked you over for drinks?"
    menu:
        "I would obey":
            mike.say "I would come if it would make you happy."
            $ aletta.sub -= 1
        "I'd check my schedule":
            mike.say "I would have to make sure I don't have something better to do."
            $ aletta.love -= 1
        "I am the one who would ask":
            mike.say "Isn't it my job to ask you over for drinks?"
            $ aletta.love += 1
        "It would be the best night for you":
            mike.say "I would come over to show you the best night of your life."
            $ aletta.sub += 1
    return

label aletta_good_sweet_talk_male:
    show aletta
    if aletta.love > 133:
        mike.say "I liked having you as a colleague, Aletta."
        mike.say "But it's SO much better having you as a partner."
        show aletta blush
        aletta.say "I...I don't know what to say!"
        show aletta happy
        aletta.say "Thank you!"
    elif aletta.love > 66:
        mike.say "I'm so glad we started dating, Aletta."
        mike.say "It's shown me a whole different side to you."
        mike.say "And it's a side I wish I'd seen sooner too."
        show aletta happy
        aletta.say "That's so nice of you to say!"
    else:
        mike.say "I don't know how you do it, Aletta!"
        aletta.say "Do what?"
        mike.say "You're so professional and efficient in the office."
        mike.say "But away from it, you're a lot of fun too!"
        aletta.say "Oh...thank you!"
    hide aletta
    return

label aletta_bad_sweet_talk_male:
    show aletta
    mike.say "Wow, Aletta - you look so good with your hair down and your glasses off!"
    show aletta angry
    aletta.say "What's that supposed to mean?"
    aletta.say "That I look awful with my hair up and my glasses on?!?"
    mike.say "Erm...no...sorry, Aletta!"
    hide aletta
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
