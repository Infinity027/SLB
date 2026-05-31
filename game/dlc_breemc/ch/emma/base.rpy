label emma_greet_dialogues_female:
    $ result = randint(1, 3)
    if result == 1:
        bree.say "Hello, Emma."
    elif result == 2:
        bree.say "Hi."
    else:
        if game.hour < 12:
            bree.say "Good morning Emma."
        elif game.hour < 19:
            bree.say "Good afternoon Emma."
        else:
            bree.say "Good evening Emma."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
