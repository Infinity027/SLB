init 1:
    layeredimage bg pallabedroom:
        attribute_function DayNightPicker()
        attribute day "pallabedroom_day"
        attribute night "pallabedroom_night"

init python:
    Room(**{
    "name": "pallabedroom",
    "display_name": "Palla's bedroom",
    "exits": ["pallalivingroom"],
    "outfit": "casual",
    "music": "music/roa_music/juice.ogg",
    "tags": ["pallahome"],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
