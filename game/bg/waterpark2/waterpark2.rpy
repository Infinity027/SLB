init python:
    Room(**{
    "name": "waterpark2",
    "hours": (10, 18),
    "conditions": [
        IsHour(10, 18),
        IsSeason(0, 1),
        InInventory("swimsuit"),
        ],
    "display_name": "Small pool",
    "exits": ["map", "waterpark"],
    "music": "music/roa_music/endless_summer.ogg",
    "outfit": "swimsuit",
    "tags": ["waterpark"],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
