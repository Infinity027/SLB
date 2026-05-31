init python:
    InteractActivity(**{
    "name": "gosteady_female",
    "display_name": "Go steady",
    "icon": "gosteady",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            ),
        ActiveTarget(
            Not(IsActivity("sleep")),
            IsFlag("engagedmc", False),
            Or(
                And(
                    IsGender("female"),
                    IsFlag("girlfriend", False),
                ),
                And(
                    IsGender("male"),
                    IsFlag("boyfriend", False),
                ),
            ),
            MinStat("love", 120),
            MinStat("sexperience", 1),
            ),
        ],
    "label": "go_steady",
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
