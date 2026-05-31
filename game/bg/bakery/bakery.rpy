init python:
    Gift("cake_gift", display_name="Cake", price=10, tooltip="A delightful cake", tags=["sweets"], label="sweets", love_bonus=2, bonus_traits=["gourmand"])
    Gift("candies", price=5, tooltip="Sweet candies", tags=["sweets"], label="sweets", love_bonus=1, bonus_traits=["gourmand"])
    Consumable("minty_candies", price=25, tooltip="Refreshing minty candies", effects=[("grooming", 1)], frequency_limit="day")
    Consumable("energy_drink", price=25, tooltip="An energy drink to boost energy", effects=[("energy", 1)], frequency_limit="day")
    Consumable("pastry", price=25, tooltip="A tasty pastry to satisfy little hunger", effects=[("hunger", 1)], frequency_limit="day")

    Room(**{
    "name": "bakery",
    "exits": ["mall1", "bookstore", "clothesshop", "arcade", "tattooshop", "mallmap"],
    "display_name": "Bakery",
    "hours": (7, 18),
    "conditions": [
        IsHour(7, 18),
        ],
    "music": "music/roa_music/good_morning.ogg",
    "outfit": "casual",
    "tags": ["mall_southside"],
    "inventory": (
        "cake_gift",
        "candies",
        "minty_candies",
        "energy_drink",
        "pastry",
        ),
    })

    Activity(**{
    "name": "bakery_shop",
    "duration": 0,
    "icon": "shop",
    "rooms": "bakery",
    "display_name": "Shop",
    "label": "bakery_shop",
    "conditions": [
        HeroTarget(MinStat("hunger", 0)),
        HeroTarget(MinStat("energy", 0)),
        ],
    })

    Activity(**{
    "name": "work_bakery",
    "label": "work_bakery",
    "money_gain": {"attributes": ["charm"], "bonus": (0.5,)},
    "duration": 4,
    "rooms": "bakery",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_day", "bakery"),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })

label work_bakery:
    show chibi bakery
    "Making bread, making sandwiches, selling sandwiches. Boring but pays the bills, right?"
    hide chibi
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    return

label bakery_shop:
    $ Room.find("bakery").shop("samantha" if samantha.present or hero.is_female else None)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
