init 1:
    layeredimage bg housemap:
        attribute_function Pickers([DayNightPicker, SeasonPicker])
        attribute first null
        group ground_season auto variant "day" if_any "day"
        group ground_season auto variant "night" if_any "night"
        group first_season auto variant "day" if_all ["day", "first"]
        group first_season auto variant "night" if_all ["night", "first"]
        always:
            "snow"

init python:
    Room(**{
    "name":"housemap",
    "exits": [
        "livingroom",
        "bedroom1",
        "bedroom2",
        "bedroom3",
        "bedroom4",
        "bedroom5",
        "bedroom6",
        "kitchen",
        "pool",
        "bathroom",
        "secondfloor",
        "house",
        "map",
        "attic",
        "firstfloorbathroom",
        "houselibrary"
        ],
    "display_name": "Home",
    "music": house_music(),
    "outfit": "casual",
    "tags": ["home"],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
