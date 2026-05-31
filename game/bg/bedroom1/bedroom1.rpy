init python:
    Room(**{
    "name": "bedroom1",
    "exits": ["livingroom", "housemap"],
    "display_name": "My Bedroom",
    "music": house_music(),
    "conditions": [
        HeroTarget(IsGender("male")),
        ],
    "outfit": "casual",
    "tags": ["home"],
    })

    Activity(**{
    "name": "clean_my_bedroom",
    "rooms": ("bedroom1", "bedroom4"),
    "conditions": [
        HeroTarget(
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("cleaningservices", False),
            Not(OnDate()),
            ),
        ],
    "icon": "vacuum",
    "display_name": "Clean my bedroom",
    "label": "clean_my_bedroom",
    "every_two_days": True,
    })

    Activity(**{
    "name": "dopushups",
    "label": "dopushups",
    "fitness": 0.5,
    "rooms": ("bedroom1", "bedroom4"),
    "conditions": [
        HeroTarget(
            MinStat("energy", 5),
            MinStat("hunger", 5),
            MinStat("grooming", 5),
            MinStat("fun", 5),
            MaxStat("fitness", 25),
            Not(OnDate()),
            ),
        ],
    "display_name": "Do some push-ups",
    "once_day": True,
    "icon": "push",
    })

label dopushups:
    show chibi pushups
    $ renpy.say("",randchoice( [
            "1, 2, 3, 4...",
            "10, 11, 12, 13, 14...",
            "100, 101, 102, 103, 104...",
            "1000, 1001, 1002, 1003, 1004...",
            "10000, 10001, 10002, 10003, 10004...",
            ]))
    return

label clean_my_bedroom:
    play sound vacuum
    show chibi vacuum
    $ game.set_flag("chores",25,"week","+")
    python:
        if game.flags.chores > 100:
            for p in Person.get_housemates():
                p.love += 1
    "I clean my bedroom."
    stop sound
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
