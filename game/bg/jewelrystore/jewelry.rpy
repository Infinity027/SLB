init python:
    Gift("silver_bracelet", price=50, tooltip="A delicate silver bracelet to show affection", tags=["jewelry"], love_bonus=1, bonus_traits=["not_princess", "innocent", "not_rebel"])
    Gift("silver_necklace", price=100, tooltip="A beautiful silver necklace to express love", tags=["jewelry"], love_bonus=2, bonus_traits=["not_princess", "innocent", "not_rebel"])
    Gift("gold_bracelet", price=500, tooltip="An elegant gold bracelet fit for a princess", tags=["jewelry"], love_bonus=3, bonus_traits=["princess", "not_rebel"])
    Gift("gold_necklace", price=750, tooltip="A luxurious gold necklace fit for royalty", tags=["jewelry"], love_bonus=4, bonus_traits=["princess", "not_rebel"])
    Gift("diamond_necklace", price=1000, tooltip="A dazzling diamond necklace for the ultimate expression of love", tags=["jewelry"], love_bonus=5, bonus_traits=["princess", "not_rebel"])
    Item("wedding_ring", price=5000, one_only=False, tooltip="Ask a girl to marry you")

    Room(**{
    "name": "jewelrystore",
    "exits": ["mall2", "flowershop", "electronic", "drugstore", "coffeeshop", "mallmap"],
    "hours": (9, 18),
    "conditions": [
        IsHour(9, 18),
        ],
    "display_name": "Jewelry Store",
    "music": "music/roa_music/higher.ogg",
    "outfit": "casual",
    "tags": ["mall_southside", "mall_northside"],
    "inventory": (
        "silver_bracelet",
        "silver_necklace",
        "gold_bracelet",
        "gold_necklace",
        "diamond_necklace",
        "wedding_ring",
        ),
    })

    Activity(**{
    "name": "jewelrystore_shop",
    "label": "jewelrystore_shop",
    "duration": 0,
    "icon": "shop",
    "rooms": "jewelrystore",
    "display_name": "Shop",
    })

label jewelrystore_shop:
    $ Room.find("jewelrystore").shop("valentina teaser")
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
