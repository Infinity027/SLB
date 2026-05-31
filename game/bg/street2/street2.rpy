init 1:
    layeredimage bg street2:
        attribute_function Pickers([DayNightPicker, SeasonPicker])
        group season auto variant "day" if_any "day"
        group season auto variant "night" if_any "night"
        always:
            "snow"

init python:
    Room(**{
    "name": "street2",
    "display_name": "Downtown",
    "exits": ["map", "street"],
    "music": season_music(),
    "random_music": True,
    "outfit": "casual",
    "tags": ["street"],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
