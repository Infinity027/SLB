init 1:
    layeredimage bg house:
        attribute_function Pickers([DayNightPicker, VehiclePicker, SeasonPicker])
        attribute night null
        attribute day null
        attribute sportscar null
        attribute car null
        attribute bike null

        group season auto variant "night" if_any "night" if_not ["sportscar", "car", "bike"]
        group season auto variant "day" if_any "day" if_not ["sportscar", "car", "bike"]

        group season auto variant "night_sportscar" if_all ["night", "sportscar"] if_not ["car", "bike"]
        group season auto variant "day_sportscar" if_all ["day", "sportscar"] if_not ["car", "bike"]

        group season auto variant "night_car" if_all ["night", "car"] if_not ["sportscar", "bike"]
        group season auto variant "day_car" if_all ["day", "car"] if_not ["sportscar", "bike"]

        group season auto variant "night_bike" if_all ["night", "bike"] if_not ["car", "sportscar"]
        group season auto variant "day_bike" if_all ["day", "bike"] if_not ["night", "car", "sportscar"]

        always:
            "snow"
        group season_fg auto variant "day" if_any "day"
        group season_fg auto variant "night" if_any "night"

init python:
    Room(**{
    "name": "house",
    "exits": ["map", "livingroom", "housemap"],
    "display_name": "Front Porch",
    "music": house_music(),
    "outfit": "casual",
    "tags": ["home"],
    })

    Activity(**{
    "name": "mow_the_lawn",
    "rooms": "house",
    "conditions": [
        IsSeason(0, 1),
        IsHour(10, 20),
        HeroTarget(
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("cleaningservices", False),
            Not(OnDate()),
            ),
        ],
    "icon": "mow_lawn",
    "display_name": "Mow the lawn",
    "label": "mow_the_lawn",
    "every_two_days": True,
    })

    Activity(**{
    "name": "shovel_snow",
    "rooms": "house",
    "conditions": [
        IsSeason(3),
        IsHour(10, 20),
        HeroTarget(
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("cleaningservices", False),
            Not(OnDate()),
            ),
        ],
    "icon": "shovelsnow",
    "display_name": "Shovel the snow",
    "label": "shovel_snow",
    "every_two_days": True,
    })

    Activity(**{
    "name": "sweep_leaves",
    "label": "sweep_leaves",
    "rooms": "house",
    "conditions": [
        IsSeason(2),
        IsHour(10, 20),
        HeroTarget(
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("cleaningservices", False),
            Not(OnDate()),
            ),
        ],
    "icon": "sweepyard",
    "display_name": "Sweep the leaves",
    "every_two_days": True,
    })

label mow_the_lawn:
    show chibi maw
    $ game.set_flag("chores", 25, "week", "+")
    python:
        if game.flags.chores > 100:
            for p in Person.get_housemates():
                p.love += 1
    "I mow the lawn."
    return

label sweep_leaves:
    show chibi leaves
    $ game.set_flag("chores", 25, "week", "+")
    python:
        if game.flags.chores > 100:
            for p in Person.get_housemates():
                p.love += 1
    "I sweep the leaves."
    return

label shovel_snow:
    show chibi shovel
    $ game.set_flag("chores", 25, "week", "+")
    python:
        if game.flags.chores > 100:
            for p in Person.get_housemates():
                p.love += 1
    "I shovel the snow."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
