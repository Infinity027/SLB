init python:
    Room(**{
    "name": "mall2",
    "display_name": "Mall Northside",
    "exits": ["map", "mall1", "flowershop","coffeeshop","electronic", "drugstore", "jewelrystore", "mallmap"],
    "hours": (7, 18),
    "conditions": [
        IsHour(7, 18),
        ],
    "music": season_music(),
    "random_music": True,
    "outfit": "casual",
    "tags": ["mall_southside", "mall_northside"],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
