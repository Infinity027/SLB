init python:
    Room(**{
    "name": "ceo",
    "hours": (8, 20),
    "conditions": [
        IsDayOfWeek("123456"),
        Or(
            IsHour(8, 20),
            And(
                IsDone("cherie_event_06"),
                IsNotDone("cherie_event_07_1"),
                IsTimeOfDay("evening", "night"),
                ),
            ),
        Or(
            And(
                HeroTarget(
                    IsGender("male"),
                    IsFlag("isceo")
                    ),
                ),
            And(
                HeroTarget(
                    IsGender("female"),
                    ),
                PersonTarget("dwayne",
                    Not(IsHidden()),
                    IsRoom("ceo"),
                    ),
                ),
            ),
        ],
    "display_name": {
        "hero.is_male": "My Office",
        "hero.is_female": "Dwayne's office"
        },
    "exits": ["office", "alettaoffice", "breakroom", "map"],
    "music": "music/roa_music/fly_high.ogg",
    "outfit": "work",
    "tags": ["work", "mcoffice"],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
