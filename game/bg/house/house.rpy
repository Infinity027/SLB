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

    # Activity(**{
    # "name": "house_place_spy_camera",
    # "display_name": "Place spy camera",
    # "max_girls": 0,
    # "rooms": "house",
    # "conditions": [
    #     IsDone("kylie_run"),
    #     HeroTarget(IsFlag("kyliecameraplaced", False)),
    #     InInventory("spy_camera"),
    #     PersonTarget("kylie",
    #         Not(IsHidden()),
    #         Not(IsFlag("schedule", "jail")),
    #         ),
    #     ],
    # "label": "house_place_spy_camera",
    # "icon": "spycamera",
    # "once_day": True,
    # })

    # Activity(**{
    # "name": "house_remove_spy_camera",
    # "display_name": "Check spy camera",
    # "max_girls": 0,
    # "rooms": "house",
    # "conditions": [
    #     HeroTarget(
    #         IsFlag("kyliecameraplaced"),
    #         IsFlag("kyliecameradelay", False),
    #         ),
    #     PersonTarget("kylie",
    #         Not(IsHidden()),
    #         Not(IsFlag("schedule", "jail")),
    #         ),
    #     ],
    # "label": "house_remove_spy_camera",
    # "icon": "spycamera",
    # "once_day": True,
    # })

# label house_remove_spy_camera:
#     show chibi spy
#     $ game.flags.kyliecameraplaced = False
#     if Person.is_not_hidden("kylie") and kylie.yandere >= 25:
#         $ kylie.flags.policestation = True
#         call kylie_investigation_1 from _call_kylie_investigation_1
#     else:
#         "As soon as I get a spare moment to myself, I pull up the footage for the previous night."
#         "Sifting through it, there's nothing to explain the mystery at first."
#         "The only sign of life that I see is actually someone walking their dog in the middle of the night."
#         "Weird, but I guess that's not exactly illegal or anti-social behavior."
#         "The footage ends, and I now fully understand the meaning of boring."
#         $ game.pass_time(2, needs=True)
#     return

# label house_place_spy_camera:
#     show chibi spy
#     "I don't honestly recall if I got the idea to buy a camera and install it out on the front porch because of Kylie."
#     "Or if I'd always been toying with the idea of getting one anyway, and the business with her just spurred me into action."
#     "But either way, I got my hands on one and spent a frustrating couple of hours trying to put it somewhere discreet out on the front porch."
#     "It's a good spot for the camera that can see the entire front yard, and is nearly impossible to see if you're not looking for it."
#     "Yeah, I know it's not the most challenging of tasks on paper - but I'm a tech guy, not the hands-on type - okay?"
#     "And after that was done, it took only a couple of minutes to set up the feed from the camera to my laptop and mobile."
#     "I guess that I was finished, just having done it kind of made me feel that much more secure."
#     $ game.flags.kyliecameraplaced = True
#     $ game.flags.kyliecameradelay = TemporaryFlag(True, 7)
#     $ hero.lose_item("spy_camera")
#     return

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
