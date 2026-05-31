init python:
    Item("zbox_360", price=200, tooltip="Play video games at home")
    Item("fitness_machine", price=600, tooltip="Gain Fitness while sleeping")
    Item("knowledge_machine", price=600, tooltip="Gain Knowledge while sleeping")
    Item("charm_machine", price=600, tooltip="Gain Charm while sleeping")
    Item("spy_camera", price=100, tooltip="Micro camera for secretly recording things")
    Item("electric_guitar", price=1000, tooltip="An axe shaped electric guitar... METAL!")

    Room(**{
    "name": "electronic",
    "exits": ["mall2", "flowershop", "coffeeshop", "drugstore", "jewelrystore", "mallmap"],
    "display_name": "Electronic Store",
    "hours": (9, 18),
    "conditions": [
        IsHour(9, 18),
        ],
    "music": "music/roa_music/clouds.ogg",
    "outfit": "casual",
    "tags": ["mall_southside", "mall_northside"],
    "inventory": (
        "zbox_360",
        "fitness_machine",
        "knowledge_machine",
        "charm_machine",
        "spy_camera",
        "electric_guitar",
        ),
    })

    Activity(**{
    "name": "electronic_shop",
    "duration": 0,
    "icon": "shop",
    "display_name": "Shop",
    "rooms": "electronic",
    "label": "electronic_shop",
    })

    Activity(**{
    "name": "work_electronic",
    "label": "work_electronic",
    "money_gain": {"attributes": ["knowledge"], "bonus": (0.5,)},
    "duration": 4,
    "rooms": "electronic",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_day", "electronic"),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })

label work_electronic:
    show chibi electronic
    "Workin' hard or hardly workin'? That's what the customers ask. The answer is always hardly workin'."
    hide chibi
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    return

label electronic_shop:
    $ clerk = randchoice(["shawn work", "amy work"]) if Person.find("amy") and amy.present else "shawn work"
    $ Room.find("electronic").shop(clerk, discount=Room.find("electronic").flags.discount)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
