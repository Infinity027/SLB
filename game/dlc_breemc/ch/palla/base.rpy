label palla_greet_dialogues_female:
    $ renpy.dynamic("greeting", "timeofday")
    $ greeting = randint(1, 3)
    if game.hour < 6:
        $ timeofday = "Hello"
    elif game.hour < 12:
        $ timeofday = "Good morning"
    elif game.hour < 19:
        $ timeofday = "Good afternoon"
    else:
        $ timeofday = "Good evening"
    if palla_love < 40:
        if greeting == 1:
            palla.say "Oh, it's you, asshole."
            bree.say "Yeah, hi to you too, bitch."
        elif greeting == 2 and hero.grooming < 6:
            palla.say "Ugh, you stink, [hero.name], go shower!"
            bree.say "Join me?"
            palla.say "Gross!"
        else:
            palla.say "Hi, I guess."
            bree.say "You guess?"
            palla.say "Fine, I take it back."
    elif palla_love < 120:
        if greeting == 1:
            palla.say "[timeofday], [hero.name]."
            bree.say "Wait you said hello without being mean."
            palla.say "Yeah? Sorry, I meant \"Hi there, fuckface\""
        elif greeting == 2 and hero.grooming < 6:
            palla.say "Ugh, you stink, [hero.name], go shower!"
            bree.say "Join me?"
            palla.say "You'd have to force me."
        else:
            palla.say "'Sup, asshole?"
            bree.say "Nothing much, bitch!"
            "She smiles sweetly."
    elif palla_love < 199:
        if greeting == 1:
            "Palla stares at me hungrily. When I look her way our eyes meet for a split second, then she looks away and pretends not to see me."
        else:
            palla.say "[timeofday], Handsome!"
            bree.say "Hey sexy!"
    else:
        palla.say "[timeofday], Handsome!"
        bree.say "Hey sexy!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
