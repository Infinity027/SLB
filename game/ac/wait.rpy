init python:
    Activity(**{
    "name": "wait",
    "conditions": [
        HeroTarget(
            MinStat("energy", 0),
            MinStat("hunger", 0),
            MinStat("grooming", 0),
            MinStat("fun", 0),
            ),
        ],
    "display_name": "Wait",
    "icon": "wait",
    "label": "wait",
    "order": 1,
    })

    Event(**{
    "name": "wait_bored",
    "fun": -1,
    "quit": False,
    "conditions": [
        HeroTarget(IsActivity("wait")),
        ],
    "chances": 5,
    "label": "wait_bored",
    })

label wait_bored:
    "I'm bored..."
    return

label wait:
    scene bg black with dissolve
    pause 0.1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
