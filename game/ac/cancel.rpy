init python:
    InteractActivity(**{
    "name": "cancel",
    "label": "cancel",
    "display_name": "Cancel",
    "icon": "cancel",
    "order":1,
    "conditions": [
        HeroTarget(
            MinStat("energy", 0),
            MinStat("hunger", 0),
            MinStat("grooming", 0),
            MinStat("fun", 0),
            ),
        ],
    "duration": 0,
    })

label cancel:
    $ do_activity.flags.end_event = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
