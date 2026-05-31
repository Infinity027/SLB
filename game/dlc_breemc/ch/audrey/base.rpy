label audrey_greet_dialogues_female:
    $ result = randint(1, 3)
    if result == 1:
        if audrey.flags.nickname == "toy":
            bree.say "Hello, my little Toy."
        else:
            bree.say "Hello, Audrey."
    elif result == 2:
        bree.say "Hi."
    else:
        if game.hour < 6:
            if audrey.flags.nickname == "toy":
                bree.say "Hello, my little Toy."
            else:
                bree.say "Hello Audrey."
        elif game.hour < 12:
            if audrey.flags.nickname == "toy":
                bree.say "Good morning my little Toy."
            else:
                bree.say "Good morning Audrey."
        elif game.hour < 19:
            if audrey.flags.nickname == "toy":
                bree.say "Good afternoon my little Toy."
            else:
                bree.say "Good afternoon Audrey."
        else:
            if audrey.flags.nickname == "toy":
                bree.say "Good evening my little Toy."
            else:
                bree.say "Good evening Audrey."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
