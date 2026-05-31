init python:
    Gift("teddy_bear", price=100, tooltip="A cuddly teddy bear", tags=["teddybear"], love_bonus=1, bonus_traits=["artsy", "innocent", "playful"])
    Item("bear_bell", price=1000, tooltip="A bear repelling bell... I wonder if it works or call the bear for dinner...")
    Item("luxury_bed", price=200, tooltip="Be rested with less sleep")
    Item("baseball_bat", price=50, tooltip="A wooden baseball bat")

    Room(**{
    "name": "mall1",
    "display_name": "Mall Southside",
    "exits": ["map", "mall2", "bakery", "bookstore", "clothesshop", "arcade", "tattooshop", "mallmap"],
    "hours": (7, 18),
    "conditions": [
        IsHour(7, 18),
        ],
    "music": season_music(),
    "random_music": True,
    "tags": [],
    "outfit": "casual",
    "tags": ["mall_southside"],
    "inventory": (
        "teddy_bear",
        "bear_bell",
        "luxury_bed",
        "baseball_bat",
        ),
    })

    Activity(**{
    "name": "mall_shop",
    "duration": 0,
    "icon": "shop",
    "display_name": "Shop",
    "rooms": ("mall1", "mall2"),
    "label": "mall_shop",
    })

    Activity(**{
    "name": "eat_a_hotdog",
    "label": "hotdog",
    "duration": 0,
    "hunger": 2,
    "money_cost": 5,
    "rooms": ("mall1", "date_mall1", "mall2"),
    "conditions": [
        HeroTarget(MinStat("hunger", 0)),
        ],
    "display_name": "Eat a hot dog",
    "icon": "hotdog",
    "once_day": True,
    })

    Activity(**{
    "name": "get_a_haircut",
    "label": "haircut",
    "rooms": ("mall1", "mall2"),
    "conditions": [
        HeroTarget(
            MinStat("energy", 5),
            MinStat("hunger", 5),
            MinStat("grooming", 5),
            MinStat("fun", 5),
            ),
        ],
    "display_name": "Get a haircut",
    "once_week": True,
    "icon": "haircut",
    "money_cost": 50,
    })

label mall_shop:
    $ Room.find("mall1").shop()
    return

label haircut:
    show chibi haircut
    if hero.is_female and hero.morality <= -50:
        if hero.flags.first_dye:
            menu:
                "Dye my hair in pink" if not hero.flags.haircut:
                    "I get my hair cut and dyed."
                    $ hero.flags.haircut = True
                "Use my natural color" if hero.flags.haircut:
                    "I like my natural color."
                    $ hero.flags.haircut = False
                "Just a little hair care":
                    "I just need to cut the tips."
        else:
            "I need change. I will dye my hair."
            $ hero.flags.haircut = True
            $ hero.flags.first_dye = True
    else:
        "I get my hair cut."
    "..."
    if hero.charm < 50:
        "I already feel better like this."
        $ hero.charm += 3
    elif hero.charm < 75:
        "It slightly better but nothing life changer."
        $ hero.charm += 1
    else:
        "I don't think a little haircut would change much in the charisma I give off though..."
    return

label hotdog:
    show chibi hotdog
    "I eat a snack."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
