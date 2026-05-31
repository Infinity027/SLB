init 1:
    layeredimage bg trailer:
        attribute_function Pickers([DayNightPicker, SeasonPicker])
        attribute burned null
        group season auto variant "day_burned" if_all ["day", "burned"]
        group season auto variant "night_burned" if_all ["night", "burned"]
        group season auto variant "day" if_any "day" if_not "burned"
        group season auto variant "night" if_any "night" if_not "burned"
        always:
            "snow"

init python:
    Room(**{
    "name": "trailer",
    "hours": (0, 23),
    "conditions": [
        IsHour(0, 23),
        HasVehicle(),
        PersonTarget("lexi",
                Not(IsHidden()),
                IsFlag("trailer")
                )
        ],
    "display_name": "Trailer Park",
    "exits": ["map", "trailerinside"],
    "linked_rooms": ["trailerinside"],
    "required_item": ["vehicle"],
    "travel_time": 1,
    "outfit": "casual",
    "tags": ["trailer"],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
