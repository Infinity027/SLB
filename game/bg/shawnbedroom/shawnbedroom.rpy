init 1:
    layeredimage bg shawnbedroom:
        attribute_function DayNightPicker()
        attribute day "shawnbedroom_day"
        attribute night "shawnbedroom_night"

init python:
    Room(**{
    "name": "shawnbedroom",
    "display_name": "Shawn's Bedroom",
    "outfit": "casual",
    "tags": ["pallahome"],
    "exits": ["pallalivingroom"],
    "music": house_music(),
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
