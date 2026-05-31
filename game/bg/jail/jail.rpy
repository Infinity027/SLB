init python:
    Room(**{
    "name": "jail",
    "exits": ["policestation"],
    "display_name": "Jail",
    "hours": (0, 23),
    "conditions": [
        IsHour(0, 23),
        ],
    "music": season_music(),
    "random_music": True,
    "outfit": "casual",
    "tags": ["policestation"],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
