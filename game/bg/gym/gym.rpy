init python:
    Room(**{
    "name": "gym",
    "hours": (6, 22),
    "conditions": [
        IsHour(6, 22),
        InInventory("sport_clothes"),
        ],
    "display_name": "Gym fitness room",
    "exits": ["map", "gymreception", "gymmachine", "gymlockers", "mma"],
    "music": "music/roa_music/higher.ogg",
    "outfit": "sport",
    "tags": ["gym"],
    })

    Activity(**{
    "name": "train",
    "energy": -1,
    "grooming": -1,
    "fitness": 2,
    "icon": "workout",
    "duration": 2,
    "rooms": ("gym", "gymmachine"),
    "conditions": [
        HeroTarget(
            MinStat("energy", 3),
            MinStat("hunger", 3),
            MinStat("fun", 3),
            IsFlag("gymmember"),
            ),
        ],
    "display_name": "Light training",
    "label": "training",
    "say": [
        "Well, I'm hanging out here more than I am training...",
        "Time for a sweat.",
        ],
    })

    Activity(**{
    "name": "train_hard",
    "energy": -2,
    "grooming": -2,
    "fitness": 4,
    "icon": "workout_hard",
    "duration": 3,
    "rooms": ("gym", "gymmachine"),
    "conditions": [
        HeroTarget(
            MinStat("energy", 5),
            MinStat("hunger", 5),
            MinStat("fun", 5),
            IsFlag("gymmember"),
            ),
        ],
    "display_name": "Heavy training",
    "label": "training_hard",
    "say": [
        "Lifting lead... as long as it increases my chances to get laid!",
        "34... 35... 36... 37... 38...\nOh shit!",
        "I love watching women train while I do my own training, it's like the smell when you are cooking.",
        ],
    })

    Activity(**{
    "name": "work_gym",
    "label": "work_gym",
    "money_gain": {"attributes": ["fitness"], "bonus": (0.5,)},
    "duration": 4,
    "rooms": ("gym", "gymmachine", "gymreception"),
    "conditions": [
        HeroTarget(
            IsGender("male"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            Or(
                And(IsFlag("job_day", "gymreception"),
                    IsTimeOfDay("morning", "afternoon"),
                    ),
                And(IsFlag("job_night", "gymreception"),
                    IsTimeOfDay("evening", "night"),
                    ),
                ),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })

label training:
    show chibi train
    python:
        hero.flags.dirty = TemporaryFlag(True, "day")
        hero.fun += hero.fitness // 20 - 1
        successes = []
        for girl in Room.find(game.room).get_present_girls():
            if hero.fitness * 2 > girl.love:
                successes.append(girl)
                girl.love += 1
    if successes and hero.fitness >= 10:
        if len(successes) == 1:
            if isinstance(successes[0], Guy):
                "[successes[0].name] can't take his eyes off me while I work out."
            else:
                "[successes[0].name] can't take her eyes off me while I work out."
        else:
            if all([isinstance(i, Girl) for i in successes]):
                "The girls can't take their eyes off me while I work out."
            else:
                "They can't take their eyes off me while I work out."
    else:
        "I spend some time training at the gym."
    hide chibi
    return

label training_hard:
    show chibi trainhard
    python:
        hero.flags.dirty = TemporaryFlag(True, "day")
        hero.fun += hero.fitness // 20 - 1
        successes = []
        for girl in Room.find(game.room).get_present_girls():
            if hero.fitness * 2 > girl.love:
                successes.append(girl)
                girl.love += 1
    if successes and hero.fitness >= 10:
        if len(successes) == 1:
            if isinstance(successes[0], Guy):
                "[successes[0].name] can't take his eyes off me while I work out."
            else:
                "[successes[0].name] can't take her eyes off me while I work out."
        else:
            if all([isinstance(i, Girl) for i in successes]):
                "The girls can't take their eyes off me while I work out."
            else:
                "They can't take their eyes off me while I work out."
    else:
        "I push myself through a tough workout at the gym."
    hide chibi
    return

label work_gym:
    show chibi gym
    "Working the desk at the gym is nowhere near as much fun as working out at the gym."
    hide chibi
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
