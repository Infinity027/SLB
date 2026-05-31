init python:
    Room(**{
    "name": "pubplay",
    "exits": ["map", "pub", "pubexterior", "pubseat"],
    "display_name": "Play Room",
    "hours": (19, 3),
    "conditions": [
        IsHour(19, 3),
        ],
    "music": "music/roa_music/can_you_hear_me.ogg",
    "outfit": "casual",
    "tags": ["pub"],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
