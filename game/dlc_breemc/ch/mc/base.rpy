init python:
    InteractEvent(**{
    "name": "pregnancy_congratulations",
    "label": "pregnancy_congratulations",
    "priority": 1500,
    "duration": 0,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(OnDate()),
            MinCounter("pregnant", 30),
            CounterChanceChecker("pregnant", 90),
            ),
        ActiveTarget(),
        ],
    "do_once": "ACTIVE",
    "once_hour": False,
    "quit": False,
    })

label pregnancy_congratulations:
    if renpy.has_label(f"{active_girl.id}_pregnancy_congratulations"):
        call expression f"{active_girl.id}_pregnancy_congratulations" from _call_expression_454
    $ hero.pregnancy_congratulations.add(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
