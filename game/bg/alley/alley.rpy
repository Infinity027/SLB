init 1:
    layeredimage bg alley:
        attribute_function Pickers([DayNightPicker, SeasonPicker])
        group season auto variant "day" if_any "day"
        group season auto variant "night" if_any "night"
        always:
            "snow"

init python:
    Consumable("drugs", label="use_drugs", price=200, effects=[("fun", 10), ("energy", 5)], frequency_limit="day")
    Consumable("weed", label="use_drugs", price=100, effects=[("fun", 5), ("energy", 2)], frequency_limit="day")

    Room(**{
    "name": "alley",
    "display_name": "Dark alley",
    "exits": ["map"],
    "music": season_music(),
    "random_music": True,
    "outfit": "casual",
    "inventory": (
        {"id": "drugs", "conditions": ("hero.is_male or (hero.is_female and hero.morality <= -70)",)},
        {"id": "weed", "conditions": ("hero.is_male or (hero.is_female and hero.morality <= -30)",)},
        ),
    })

    Activity(**{
    "name": "buy_drugs",
    "label": "buy_drugs",
    "rooms": "alley",
    "duration": 0,
    "display_name": "Buy some illegal stuff",
    "icon": "shop",
    "conditions": [
        HeroTarget(
            Or(
                IsGender("male"),
                MaxStat("morality", 25)
                ),
            )
        ]
    })

label buy_drugs:
    $ Room.find("alley").shop("lexi" if lexi.present else None)
    return

label use_drugs:
    if renpy.has_label(f"use_drugs_{hero.gender}"):
        call expression f"use_drugs_{hero.gender}" from _call_expression_194
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
