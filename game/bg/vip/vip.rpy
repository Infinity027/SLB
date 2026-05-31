init python:
    Room(**{
    "name": "vip",
    "hours": (22, 5),
    "conditions": [
        IsHour(22, 5),
        ],
    "display_name": "VIP",
    "exits": ["nightclub", "nightclubbar", "restroom"],
    "music": "music/darren_curtis/feel_it_in_your_feet.ogg",
    "outfit": "date",
    "tags": ["club"],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
