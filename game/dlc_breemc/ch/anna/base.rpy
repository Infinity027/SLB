label anna_greet_dialogues_female:
    $ result = randint(1, 3)
    if result == 1:
        bree.say "Hello, Anna."
    elif result == 2:
        bree.say "Hi."
    else:
        if game.hour < 6:
            bree.say "Hello Anna."
        elif game.hour < 12:
            bree.say "Good morning Anna."
        elif game.hour < 19:
            bree.say "Good afternoon Anna."
        else:
            bree.say "Good evening Anna."
    return

label anna_ask_date_female:



    call anna_ask_date_alone_female from _call_anna_ask_date_alone_female
    return _return

label anna_ask_date_alone_female:
    bree.say "Anna..."
    anna.say "Yeah, [hero.name]?"
    bree.say "I...erm..."
    bree.say "I wanted to ask you something..."
    "Anna turns to me and smiles sweetly."
    "Which of course only serves to make things even worse."
    anna.say "Go ahead, [hero.name]."
    anna.say "You can ask me anything at all!"
    bree.say "Ah...okay..."
    bree.say "I was going to ask if you'd go on a date with me?"
    bree.say "You know, like a real date?"
    if anna.love < 50 or anna.flags.nodate:
        "Anna giggles and shakes her head at the notion."
        anna.say "Oh, [hero.name]..."
        anna.say "I do date girls when I meet one I like."
        anna.say "But I just don't like you that way."
        anna.say "At least not yet..."
        $ date_choice = False
    else:
        "Anna giggles and claps her hands with glee."
        anna.say "Oh, [hero.name]..."
        anna.say "I thought you'd never ask!"
        anna.say "That's a great idea."
        anna.say "I'd love to go on a date with you!"
        $ date_choice = True
    return date_choice
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
