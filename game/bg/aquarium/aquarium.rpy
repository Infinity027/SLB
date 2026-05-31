init python:
    Room(**{
    "name": "aquarium",
    "display_name": "Aquarium",
    "hours": (9, 18),
    "conditions": [
        IsHour(9, 18),
        ],
    "exits": ["map"],
    "music": "music/roa_music/blue.ogg",
    "outfit": "casual",
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
