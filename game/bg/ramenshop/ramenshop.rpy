init python:
    Room(**{
    "name": "ramenshop",
    "exits": ["beach", "masterhouse"],
    "display_name": "Japanese Ramen Restaurant",
    "ambience": "sd/SFX/ambiences/cooking.ogg",
    "conditions":[
        IsHour(11, 23),
        ],
    "outfit": "casual",
    "tags": ["beach"],
    })

    Activity(**{
    "name": "eat_a_ramen",
    "label": "eat_a_ramen",
    "duration": 0,
    "hunger": 7,
    "money_cost": 25,
    "rooms": "ramenshop",
    "conditions": [
        HeroTarget(
            MinStat("energy", 0),
            MinStat("hunger", 0),
            MinStat("grooming", 0),
            MinStat("fun", 0),
            Not(MaxStat("hunger")),
            Not(OnDate()),
            ),
        ],
    "display_name": "Eat a Ramen",
    "icon": "eat",
    })

label eat_a_ramen:
    show chibi ramen
    "Slupr, slurp...\nslurp..."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
