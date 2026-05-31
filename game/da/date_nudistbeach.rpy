layeredimage bg date_nudistbeach:
    if game.hour >= 20 or game.hour <= 5:
        "beach_night"
    else:
        "beach_day"

init python:
    Room(**{
    "name": "date_nudistbeach",
    "exits": ["map"],
    "display_name": "Nudist beach",
    "hours": (14, 17),
    "conditions": [
        IsHour(14, 17),
        IsSeason(0, 1),
        HasVehicle(motor=True),
        ],
    "music": "music/roa_music/summer_air.ogg",
    "outfit": "naked",
    "tags": ["dateroom"],
    })

    Date(
    "nudistbeach",
    display_name = "Nudist beach",
    conditions=[
        ValidRooms("date_nudistbeach"),
        GameTarget(
            IsFlag("nudistBeach", True),
            ),
        ],
    clothes = "naked",
    love_gain = 3,
    )

label date_nudistbeach:
    $ renpy.show(date_girl.id)
    "We go to the beach."
    if "sports_car" in hero.inventory:
        $ game.active_date.score += 5
    $ renpy.hide(date_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
