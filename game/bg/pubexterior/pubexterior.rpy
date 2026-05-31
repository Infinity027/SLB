init 1:
    layeredimage bg pubexterior:
        attribute_function Pickers([DayNightPicker, SeasonPicker])
        group season auto variant "day" if_any "day"
        group season auto variant "night" if_any "night"
        always:
            "snow"

init python:
    Room(**{
    "name": "pubexterior",
    "exits": ["map", "pub", "pubplay", "pubseat"],
    "display_name": "Exterior",
    "hours": (19, 3),
    "conditions": [
        IsHour(19, 3),
        ],
    "music": "music/roa_music/can_you_hear_me.ogg",
    "outfit": "casual",
    "tags": ["pub"],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
