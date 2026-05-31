label hanna_greet_dialogues_female:
    $ result = randint(1, 3)
    if result == 1:
        bree.say "Hello, Hanna."
    elif result == 2:
        bree.say "Hi."
    else:
        if game.hour < 6:
            bree.say "Hello Hanna."
        elif game.hour < 12:
            bree.say "Good morning Hanna."
        elif game.hour < 19:
            bree.say "Good afternoon Hanna."
        else:
            bree.say "Good evening Hanna."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
