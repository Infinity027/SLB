init python:
    Event(**{
    "name": "jack_auto_greet",
    "label": "auto_greet",
    "girl": "jack",
    "priority": 100,
    "conditions": [
        HeroTarget(IsActivity("None")),
        PersonTarget(jack,
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

label jack_greet:
    if renpy.has_label(f"jack_greet_dialogues_{hero.gender}") and not jack.flags.greeted:
        scene expression f"bg {game.room}"
        $ jack.flags.greeted = TemporaryFlag(True, 1)
        show jack
        $ result = randint(1, 3)
        if result == 1:
            jack.say "Hello, [hero.name]."
        elif result == 2:
            jack.say "Hi, [hero.name]."
        elif result == 3:
            jack.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                jack.say "Good morning [hero.name]."
            elif game.hour < 19:
                jack.say "Good afternoon [hero.name]."
            else:
                jack.say "Good evening [hero.name]."
        call expression f"jack_greet_dialogues_{hero.gender}" from _call_expression_241
        hide jack
    return

label jack_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello, Jack."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            mike.say "Hello Jack."
        elif game.hour < 12:
            mike.say "Good morning Jack."
        elif game.hour < 19:
            mike.say "Good afternoon Jack."
        else:
            mike.say "Good evening Jack."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
