label lavish_greet_dialogues_female:
    $ result = randint(1, 3)
    if result == 1:
        bree.say "Hello, Lavish."
    elif result == 2:
        bree.say "Hi."
    else:
        if game.hour < 6:
            bree.say "Hello Lavish."
        elif game.hour < 12:
            bree.say "Good morning Lavish."
        elif game.hour < 19:
            bree.say "Good afternoon Lavish."
        else:
            bree.say "Good evening Lavish."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
