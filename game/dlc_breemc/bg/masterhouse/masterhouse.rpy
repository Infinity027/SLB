init 1:
    layeredimage bg masterhouse:
        attribute_function Pickers([DayNightPicker, SeasonPicker])
        group season auto variant "day" if_any "day"
        group season auto variant "night" if_any "night"
        always:
            "snow"

init python:
    Room(**{
    "name": "masterhouse",
    "exits": ["beach", "ramenshop"],
    "display_name": "Master House",
    "conditions":[
        IsDone("master_female_event_01"),
        IsHour(8, 20),
        ],
    "outfit": "swimsuit",
    "tags": ["beach"],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
