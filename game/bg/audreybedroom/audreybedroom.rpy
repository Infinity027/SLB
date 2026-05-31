init 1:
    layeredimage bg audreybedroom:
        attribute_function DayNightPicker()
        attribute day "audreybedroom_day"
        attribute night "audreybedroom_night"

init python:
    Room(**{
    "name": "audreybedroom",
    "display_name": "Audrey's bedroom",
    "exits": ["audreylivingroom"],
    "outfit": "casual",
    "music": "music/roa_music/esperanza.ogg",
    "tags": ["audreyhome"],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
