label kleio_greet_dialogues_female:
    $ result = randint(1, 3)
    if result == 1:
        bree.say "Hello, Kleio."
    elif result == 2:
        bree.say "Hi."
    else:
        if game.hour < 6:
            bree.say "Hello Kleio."
        elif game.hour < 12:
            bree.say "Good morning Kleio."
        elif game.hour < 19:
            bree.say "Good afternoon Kleio."
        else:
            bree.say "Good evening Kleio."
    return

label kleio_ask_date_female:



    call kleio_ask_date_alone_female from _call_kleio_ask_date_alone_female
    return _return

label kleio_ask_date_alone_female:
    bree.say "Kleio..."
    bree.say "I was wondering about something..."
    kleio.say "Huh?"
    kleio.say "What's that, [hero.name]?"
    bree.say "Well..."
    bree.say "We get on pretty well, don't we?"
    kleio.say "Sure we do!"
    bree.say "So maybe we could do more than just hang out?"
    bree.say "We could go somewhere and do something together - just the two of us?"
    kleio.say "[hero.name]..."
    kleio.say "Are you asking me out?"
    kleio.say "Like on an actual date?"
    bree.say "Erm..."
    bree.say "I guess so!"
    if kleio.love < 50 or kleio.flags.nodate:
        kleio.say "Wow...that took you like forever!"
        kleio.say "And it was kind of a waste of time too."
        kleio.say "Because we're not there yet, [hero.name]!"
        kleio.say "I'm not ready to go on a date with you."
        $ date_choice = False
    else:
        kleio.say "Sure we can, [hero.name]."
        kleio.say "That sounds like a great idea!"
        kleio.say "I dunno why you didn't ask me before now."
        $ date_choice = True
    return date_choice
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
