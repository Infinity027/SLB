init python:
    InteractActivity(**{
    "name": "apologize",
    "label": "apologize",
    "display_name": "Apologize for breaking up",
    "icon": "heart",
    "duration": 0,
    "conditions": [
        ActiveTarget(
            Not(IsActivity("sleep")),
            IsFlag("breakup"),
            ),
        ],
    "once_day": "ACTIVE",
    })

    InteractActivity(**{
    "name": "apologize_friendzone",
    "label": "apologize",
    "display_name": "Ask for a second chance",
    "icon": "heart",
    "duration": 0,
    "conditions": [
        ActiveTarget(
            Not(IsActivity("sleep")),
            IsFlag("friendzone"),
            IsFlag("breakup", False),
            ),
        ],
    "once_day": "ACTIVE",
    })

label apologize:
    call expression f"{active_girl.id}_greet" from _call_expression_82
    $ renpy.show(active_girl.id)
    call expression f"apologize_dialogues_1_{hero.gender}" from _call_expression_20
    active_girl.say "Alright, but don't ever do this again."
    $ active_girl.flags.breakup = False
    $ active_girl.flags.friendzone = False
    $ active_girl.status = "friend"
    if hero.is_female and hero.morality <= -25:
        $ hero.morality += 1
    $ renpy.hide(active_girl.id)
    python:
        for harem in Harem.find(active_girl, is_active=False):
            harem.apologize(active_girl)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
