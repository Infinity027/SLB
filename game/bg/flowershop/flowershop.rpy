init python:
    Gift("flowers", price=50, tooltip="A bouquet of flowers to express affection", tags=["flowers"], label="flowers", love_bonus=1, bonus_traits=["artsy"])
    Gift("lots_of_flowers", price=100, tooltip="An abundance of flowers for a grand gesture", tags=["flowers"], label="flowers", love_bonus=2, bonus_traits=["princess", "artsy"])

    Room(**{
    "name": "flowershop",
    "exits": ["mall2","coffeeshop","electronic", "drugstore", "jewelrystore", "mallmap"],
    "hours": (9, 18),
    "conditions": [
        IsHour(9, 18),
        ],
    "display_name": "Flower Shop",
    "music": "music/roa_music/blue.ogg",
    "outfit": "casual",
    "tags": ["mall_southside", "mall_northside"],
    "inventory": (
        "flowers",
        "lots_of_flowers",
        ),
    })

    Activity(**{
    "name": "flowershop_shop",
    "duration": 0,
    "display_name": "Shop",
    "icon": "shop",
    "rooms": "flowershop",
    "label": "flowershop_shop",
    })

label flowershop_shop:
    $ Room.find("flowershop").shop("jessica teaser")
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
