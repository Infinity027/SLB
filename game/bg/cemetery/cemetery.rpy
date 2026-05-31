init python:
    Room(**{
    "name": "cemetery",
    "hours": (22, 3),
    "conditions": [
        'not Room.find("cemetery").hidden',
        IsHour(22, 3),
        ],
    "display_name": "Cemetery",
    "exits": ["map"],
    "music": "music/TeknoAXE/simple_metal.ogg",
    "valid": False,
    "outfit": "casual",
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
