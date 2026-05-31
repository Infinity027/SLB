init python:
    Room(**{
    "name": "waterpark",
    "hours": (10, 18),
    "conditions": [
        IsHour(10, 18),
        IsSeason(0, 1),
        InInventory("swimsuit"),
        ],
    "display_name": "Big slide",
    "exits": ["map", "waterpark2"],
    "money_cost": 10,
    "music": "music/roa_music/endless_summer.ogg",
    "outfit": "swimsuit",
    "tags": ["waterpark"],
    })

    Activity(**{
    "name": "swim_waterpark",
    "label": "swim",
    "fun": 1,
    "fitness": 1,
    "duration": 2,
    "rooms": ("waterpark", "waterpark2"),
    "conditions": [
        HeroTarget(
            MinStat("energy", 3),
            MinStat("hunger", 3),
            MinStat("grooming", 3),
            MinStat("fun", 3),
            ),
        ],
    "display_name": "Swim",
    "icon": "swim",
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
