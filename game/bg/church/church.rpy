init 1:
    layeredimage bg church wedding:
        always:
            "church_wedding"

init python:
    Room(**{
    "name": "church",
    "hours": (9, 19),
    "conditions": [
        Or(
            IsDayOfWeek("7"),
            HeroTarget(
                IsGender("female"),
                Or(
                    IsFlag("job_day", False),
                    IsFlag("job_day", "church"),
                ),
            ),
        ),
        IsHour(9, 19),
        ],
    "display_name": "Church",
    "exits": ["map"],
    "music": "music/darren_curtis/camelot_monastery.ogg",
    "outfit": "casual",
    })

    Activity(**{
    "name": "attend_mass",
    "rooms": "church",
    "conditions": [
        IsHour(9, 11),
        IsDayOfWeek("7"),
        HeroTarget(
            MinStat("energy", 1),
            MinStat("hunger", 1),
            MinStat("grooming", 5),
            MinStat("fun", 1),
            ),
        ],
    "fun": -2,
    "icon": "mass",
    "display_name": "Attend mass",
    "label": "attend_mass",
    "once_day": True,
    })

    Activity(**{
    "name": "bible_study",
    "duration": 3,
    "rooms": "church",
    "conditions": [
        IsHour(14, 19),
        IsDayOfWeek("7"),
        HeroTarget(
            MinStat("energy", 1),
            MinStat("hunger", 1),
            MinStat("grooming", 5),
            MinStat("fun", 1),
            ),
        ],
    "fun": -2,
    "icon": "mass",
    "display_name": "Bible study",
    "label": "bible_study",
    "once_day": True,
    })

label attend_mass:
    show chibi mass
    "I attend a service."
    if renpy.has_label(f"attend_mass_{hero.gender}"):
        call expression f"attend_mass_{hero.gender}" from _call_expression_197
    return

label bible_study:
    show chibi bible
    if Person.is_not_hidden("harmony"):
        $ harmony.love += 1
    "I do some bible study at church..."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
