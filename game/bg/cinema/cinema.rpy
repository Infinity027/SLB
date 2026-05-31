init 1:
    layeredimage bg cinema:
        attribute_function Pickers([DayNightPicker, SeasonPicker])
        group season auto variant "day" if_any "day"
        group season auto variant "night" if_any "night"
        always:
            "snow"

init python:
    Room(**{
    "name": "cinema",
    "exits": ["map"],
    "display_name": "Movie theater",
    "hours": (14, 23),
    "conditions": [
        IsHour(14, 23),
        ],
    "music": season_music(),
    "random_music": True,
    "outfit": "casual",
    })

    Activity(**{
    "name": "watch_a_movie",
    "duration": 2,
    "fun": 5,
    "icon": "cinema",
    "money_cost": 10,
    "display_name": "Watch a movie",
    "rooms": "cinema",
    "label": "watch_movie",
    })

label watch_movie:
    show bg cinemaroom
    show chibi theater
    "I watch a movie."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
