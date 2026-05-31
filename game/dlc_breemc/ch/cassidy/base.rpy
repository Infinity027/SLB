label cassidy_greet_dialogues_1_female:
    bree.say "Hello, my pet!"
    return

label cassidy_greet_dialogues_2_female:
    bree.say "My sweet pet!"
    return

label cassidy_greet_dialogues_3_female:
    bree.say "Hello, Mistress."
    return

label cassidy_greet_dialogues_4_female:
    $ result = randint(1, 3)
    if result == 1:
        bree.say "Hello, Cassidy."
    elif result == 2:
        bree.say "Hi."
    else:
        if game.hour < 6:
            bree.say "Hello Cassidy."
        elif game.hour < 12:
            bree.say "Good morning Cassidy."
        elif game.hour < 19:
            bree.say "Good afternoon Cassidy."
        else:
            bree.say "Good evening Cassidy."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
