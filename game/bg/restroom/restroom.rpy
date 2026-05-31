init python:
    Room(**{
    "name": "restroom",
    "hours": (22, 5),
    "conditions": [
        IsHour(22, 5),
        ],
    "display_name": "Restroom",
    "exits": ["nightclub", "vip"],
    "music": "music/darren_curtis/feel_it_in_your_feet.ogg",
    "outfit": "date",
    "tags": ["club"],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
