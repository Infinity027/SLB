init python:
    Room(**{
    "name": "nightclub",
    "hours": (22, 5),
    "conditions": [
        IsHour(22, 5),
        Or(
            InInventory("fancy_clothes"),
            InInventory("fancy_dress"),
            ),
        ],
    "display_name": "Night Club",
    "exits": ["map", "nightclubbar", "vip", "restroom"],
    "money_cost": 15,
    "music": "music/darren_curtis/feel_it_in_your_feet.ogg",
    "outfit": "date",
    "tags": ["club"],
    })

    Activity(**{
    "name": "party",
    "label": "nightclub_party",
    "duration": 2,
    "fun": 6,
    "charm": 3,
    "money_cost": 50,
    "rooms": "nightclub",
    "conditions": [
        HeroTarget(
            MinStat("energy", 3),
            MinStat("hunger", 3),
            MinStat("grooming", 4),
            MinStat("fun", 2),
            MinStat("charm", 10),
            Or(
                IsGender("male"),
                MaxStat("morality", 50)
                ),
            )
        ],
    "display_name": "Party",
    "icon": "party",
    "once_day": True,
    })

label nightclub_party:
    show chibi party
    $ s = randchoice(["I have a couple drinks with some friends.",
            "I have a few too many then go home.",
            "I wonder if I'm an alcoholic...",
            "Let's party!!",
            "Whoa, that beer is fucking great."])
    "[s]"
    if hero.is_female and hero.morality >= 0:
        $ hero.morality -= 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
