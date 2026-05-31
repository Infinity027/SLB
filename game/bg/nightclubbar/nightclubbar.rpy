init python:
    Room(**{
    "name": "nightclubbar",
    "hours": (22, 5),
    "conditions": [
        IsHour(22, 5),
        Or(
            InInventory("fancy_clothes"),
            InInventory("fancy_dress"),
            ),
        ],
    "display_name": "Nightclub Bar",
    "exits": ["map", "nightclub", "vip", "restroom"],
    "music": "music/darren_curtis/feel_it_in_your_feet.ogg",
    "outfit": "date",
    "tags": ["club"],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
