init 1:
    layeredimage bg balcony:
        attribute_function DayNightPicker()
        attribute day "balcony_day"
        attribute night "balcony_night"

init python:

    Room(**{
    "name": "balcony",
    "display_name": "Balcony",
    "exits": ["pallalivingroom"],
    "music": house_music(),
    "outfit": "casual",
    "tags": ["pallahome"],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
