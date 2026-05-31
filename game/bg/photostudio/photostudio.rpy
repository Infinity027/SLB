init python:
    Room(**{
    "name": "photostudio",
    "hours": (9, 22),
    "conditions": [
        IsHour(9, 22),
        HeroTarget(
                IsGender("female"),
                MaxStat("morality", -60)
                )
        ],
    "display_name": "Photo Studio",
    "exits": ["map"],
    "music": "music/darren_curtis/feel_it_in_your_feet.ogg",
    "outfit": "casual",
    })

    Event(**{
    "name": "about_photostudio",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsRoom("map"),
            MaxStat("morality", -60)
            ),
        ],
    "label": "about_photostudio",
    "do_once": True,
    "once_day": True,
    })


label about_photostudio:
    "A photo studio has opened in town. Maybe I can find a job here."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
