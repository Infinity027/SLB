init python:
    Item("bike", price=500, tooltip="Go to far-away places (slowly)")
    Item("car", price=5000, tooltip="Go to far-away places (fast)")
    Item("sports_car", price=20000, tooltip="Go to far-away places (fast) with style", replace_items=["car"])

    Room(**{
    "name": "garage",
    "hours": (9, 18),
    "conditions": [
        IsHour(9, 18),
        ],
    "display_name": "Car workshop",
    "exits": ["map"],
    "music": season_music(),
    "random_music": True,
    "outfit": "casual",
    "inventory": (
        "bike",
        "car",
        "sports_car",
        ),
    })

    Activity(**{
    "name": "garage_shop",
    "duration": 0,
    "display_name": "Shop",
    "icon": "shop",
    "rooms": "garage",
    "label": "garage_shop",
    })

label garage_shop:
    $ Room.find("garage").shop("kleio" if Person.is_not_hidden("kleio") and kleio.present else None)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
