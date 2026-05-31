init python:
    Room(**{
    "name": "bedroom6",
    "exits": ["livingroom","housemap"],
    "display_name": "[mike.name]'s Bedroom",
    "music": house_music(),
    "conditions": [
        HeroTarget(IsGender("female")),
        ],
    "outfit": "casual",
    "tags": ["home"],
    })

layeredimage button bg bedroom6:
    if game.hour >= 20 or game.hour <= 5:
        "button_bedroom6_night"
    else:
        "button_bedroom6_day"
    group fg:
        attribute hover:
            "gui/location_button_fg_hover.png"
        attribute idle:
            "gui/location_button_fg_idle.png"
        attribute insensitive:
            "gui/location_button_fg_insensitive.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
