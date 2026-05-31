init python:
    Event(**{
    "name": "scottie_auto_greet",
    "label": "auto_greet",
    "girl": "scottie",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsActivity("None")
            ),
        PersonTarget(scottie,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            IsFlag("greeted", False),
            MinStat("love", 50),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

label scottie_greet:
    if renpy.has_label(f"scottie_greet_dialogues_{hero.gender}") and not scottie.flags.greeted:
        scene expression f"bg {game.room}"
        $ scottie.flags.greeted = TemporaryFlag(True, 1)
        show scottie
        $ result = randint(1, 3)
        if result == 1:
            scottie.say "Hello, babe."
        elif result == 2:
            scottie.say "Hi, baby."
        elif result == 3:
            scottie.say "Hi, babe."
        else:
            if game.hour < 12:
                scottie.say "Good morning babe."
            elif game.hour < 19:
                scottie.say "Good afternoon baby."
            else:
                scottie.say "Good evening babe."
        call expression f"scottie_greet_dialogues_{hero.gender}" from _call_expression_268
        hide scottie
    return

label scottie_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello, Scottie."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            mike.say "Hello Scottie."
        elif game.hour < 12:
            mike.say "Good morning Scottie."
        elif game.hour < 19:
            mike.say "Good afternoon Scottie."
        else:
            mike.say "Good evening Scottie."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
