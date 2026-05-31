init python:
    InteractActivity(**{
    "name": "cinema_with",
    "label": "cinema_with",
    "display_name": "Invite to movie",
    "icon": "cinema",
    "duration": 2,
    "fun": 2,
    "grooming": 0,
    "conditions": [
        HeroTarget(
            IsRoom("cinema"),
            MinStat("energy", 2),
            MinStat("hunger", 3),
            MinStat("grooming", 3),
            MinStat("fun", 1),
            ),
        ],
    })

label cinema_with:
    $ active_girl.set_flag("interact", 1, 1, "+")
    call expression f"{active_girl.id}_greet" from _call_expression_35
    $ renpy.show(active_girl.id)
    call expression f"cinema_with_dialogues_1_{hero.gender}" from _call_expression_53
    if hero.charm >= 40 - active_girl.love:
        active_girl.say "Sure, why not?"
        "I watch a movie with [active_girl.name]."
        $ active_girl.love += hero.charm // 20
        $ hero.fun += 2
    else:
        active_girl.say "Sorry, I don't feel like it."
        $ hero.cancel_activity()
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
