init python:
    Room(**{
    "name": "gymmachine",
    "hours": (6, 22),
    "conditions": [
        IsHour(6, 22),
        InInventory("sport_clothes"),
        ],
    "display_name": "Gym weight room",
    "exits": ["map", "gymlockers", "gymreception", "gym", "mma"],
    "music": "music/roa_music/higher.ogg",
    "outfit": "sport",
    "tags": ["gym"],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
