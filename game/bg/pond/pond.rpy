init 1:
    layeredimage bg pond:
        attribute_function Pickers([DayNightPicker, SeasonPicker])
        group season auto variant "day" if_any "day"
        group season auto variant "night" if_any "night"
        always:
            "snow"

init python:
    Room(**{
    "name": "pond",
    "exits": ["map", "park"],
    "music": season_music(),
    "random_music": True,
    "tags": ["park"],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
