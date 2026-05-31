init python:
    Room(**{
    "name": "classroom",
    "exits": ["university","library","dininghall"],
    "display_name": "Classroom",
    "hours": (8, 18),
    "conditions": [
        IsDayOfWeek("123456"),
        IsHour(8, 18),
        ],
    "music": season_music(),
    "random_music": True,
    "outfit": "casual",
    "tags": ["uni"],
    })

    Activity(**{
    "name": "study",
    "label": "study_classroom",
    "fun": -1,
    "knowledge": 3,
    "money_cost": 25,
    "duration": 2,
    "rooms": "classroom",
    "conditions": [
        HeroTarget(
            Or(
                IsGender("male"),
                And(
                    IsGender("female"),
                    IsFlag("graduated", True),
                    ),
                ),
            MinStat("energy", 3),
            MinStat("hunger", 3),
            MinStat("grooming", 3),
            MinStat("fun", 4),
            ),
        ],
    "display_name": "Study",
    "icon": "study",
    })

label study_classroom:
    show chibi study
    $ s = randchoice([
            "I take a boring (and way too long) English class.",
            "I sit almost lost in an half-empty classroom.",
            "A little Chinese man is teaching the basics of Spanish.",
            "I listen to a guy talking about space, stars, suns and planets.",
            "I never knew that a hot teacher could make economy interesting.",
            "Luckily, this class is very short.",
            "ZzZzZzZz.",
            "I stare blankly at the walls.",
            "Economy 101, that's something I'll tell my grandchildren about.",
            "Do they teach anything useful here?",
            "The history of German porn...now there's a topic I won't get bored with."
            ])
    "[s]"
    hide chibi
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
