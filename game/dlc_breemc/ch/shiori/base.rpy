label shiori_greet_dialogues_female:
    $ result = randint(1, 3)
    if result == 1:
        bree.say "Hello, Shiori."
    elif result == 2:
        bree.say "Hi."
    else:
        if game.hour < 6:
            bree.say "Hello."
        elif game.hour < 12:
            bree.say "Good morning Shiori."
        elif game.hour < 19:
            bree.say "Good afternoon Shiori."
        else:
            bree.say "Good evening Shiori."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
