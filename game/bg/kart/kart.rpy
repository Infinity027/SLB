init python:
    Room(**{
    "name": "kart",
    "display_name": "Karting track",
    "exits": ["map"],
    "hours": (12, 23),
    "conditions": [
        IsHour(12, 23),
        ],
    "music": "music/roa_music/clouds.ogg",
    "outfit": "casual",
    })

    Activity(**{
    "name": "karting_solo",
    "fun": 2,
    "money_cost": 25,
    "rooms": "kart",
    "conditions": [
        HeroTarget(
            MinStat("energy", 3),
            MinStat("hunger", 3),
            MinStat("fun", 3),
            ),
        ],
    "display_name": "Drive a kart",
    "icon": "solokart",
    "label": "karting_solo",
    })

label karting_solo:
    show chibi kart
    if not hero.has_skill("racing"):
        $ hero.gain_skill("racing", 10)
        $ skill = hero.skills.racing.value
    "I have a lot of fun racing around!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
