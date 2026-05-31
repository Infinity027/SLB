label minami_greet_dialogues_female:
    $ result = randint(1, 3)
    if result == 1:
        bree.say "Hello."
    elif result == 2:
        bree.say "Hi."
    else:
        if game.hour < 6:
            bree.say "Hello Minami."
        elif game.hour < 12:
            bree.say "Good morning Minami."
        elif game.hour < 19:
            bree.say "Good afternoon Minami."
        else:
            bree.say "Good evening Minami."
    return

label minami_ask_date_female:



    call minami_ask_date_alone_female from _call_minami_ask_date_alone_female
    return _return

label minami_ask_date_alone_female:
    "I must have tried to say this almost a dozen time by now."
    "But this time is different, as I finally manage to get the words out."
    bree.say "Minami..."
    bree.say "Can I ask you something?"
    minami.say "Oh..."
    minami.say "Sure, [hero.name] - what's up?"
    bree.say "I was just wondering..."
    bree.say "Would you maybe want to go out with me?"
    bree.say "You know, like on an actual date?"
    if kleio.love < 50 or kleio.flags.nodate:
        minami.say "Oh, that's so sweet of you to ask, [hero.name]!"
        minami.say "But I just don't think we should do that."
        minami.say "At least not yet - we're not there, you know?"
        "I feel a surge of disappointment as Minami says no."
        "But I nod all the same, accepting her answer."
        $ date_choice = False
    else:
        minami.say "Are you serious, [hero.name]?"
        minami.say "That's a great idea!"
        minami.say "When can we do it?"
        "I feel a surge of relief as Minami says yes."
        "And then I realise, I have no idea about the actual details!"
        $ date_choice = True
    return date_choice
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
