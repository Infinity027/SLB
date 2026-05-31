init 1:
    layeredimage bg hospital:
        attribute_function DayNightPicker()
        attribute day null
        attribute night null
        always:
            if_any "day"
            "hospital_day"
        always:
            if_any "night"
            "hospital_night"
init python:
    Room(**{
    "name": "hospital",
    "conditions": [
        Or(
            HeroTarget(
                IsFlag("injured")
                ),
            HeroTarget(
                IsGender("female"),
                Not(OnDate()),
                ),
            HeroTarget(
                IsGender("female"),
                IsFlag("foundpreg")
                ),
            And(IsDone("camila_event_08"),
                Not(IsDone("camila_event_09")),
                PersonTarget("camila",
                    Not(IsHidden()),
                    IsFlag("camiladelay", False)
                    ),
                ),
            And(
                IsDone("angela_female_event_07"),
                HeroTarget(
                    IsGender("female"),
                    Not(IsFlag("angela_test_results")),
                    ),
                PersonTarget("angela",
                    Not(IsHidden()),
                    ),
                ),
            )
        ],
    "display_name": "Hospital",
    "exits": ["map"],
    "music":season_music(),
    "random_music": True,
    "outfit": "casual",
    })

    Activity(**{
    "name": "Treat injury",
    "display_name": "Treat your injuries",
    "duration": 12,
    "rooms": "hospital",
    "money_cost": 250,
    "conditions": [
        HeroTarget(
                IsFlag("injured"),
                ),
        ],
    "label": "healed",
    "icon": "heal",
    "do_once": False,
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
