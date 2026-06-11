init python:
    Room(**{
    "name": "policestation",
    "hours": (0, 23),
    "conditions": [
        IsHour(0, 23),
        Or(
            PersonTarget("alexis",
                Not(IsHidden()),
                IsFlag("policestation")
                ),
            PersonTarget("camila",
                Not(IsHidden()),
                ),
            And(
                IsDone("camila_event_01_alt"),
                IsNotDone("camila_event_02_alt"),
                HeroTarget(
                    IsGender("male"),
                    IsFlag("undercover", True),
                    ),
                ),
            And(
                IsDone("camila_event_02_alt"),
                IsNotDone("camila_event_04_alt"),
                HeroTarget(
                    IsGender("male"),
                    ),
                ),
            And(
                PersonTarget("amy",
                    IsFlag("police_ticket", True),
                    ),
                IsNotDone("amy_kink_03_police"),
                ),
            And(
                IsDone("angela_female_event_10"),
                IsNotDone("angela_female_event_11"),
                HeroTarget(
                    IsGender("female")
                    ),
                PersonTarget("angela",
                    Not(IsHidden()),
                    IsFlag("angela_choice", "police"),
                    )
                ),
            And(
                IsDone("angela_female_event_13a"),
                IsNotDone("angela_female_event_14a"),
                HeroTarget(
                    IsGender("female")
                    ),
                PersonTarget("angela",
                    Not(IsHidden()),
                    )
                ),
        )
        ],
    "display_name": "Police Station",
    "exits": ["map", "jail"],
    "music": season_music(),
    "random_music": True,
    "outfit": "casual",
    "tags": ["policestation"],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
