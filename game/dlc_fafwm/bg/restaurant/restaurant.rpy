init python:
    Room(**{
    "name": "restaurant",
    "exits": ["map"],
    "conditions":[
        IsHour(18, 23),
        HeroTarget(
            Not(OnDate()),
            IsGender("male"),
            ),
        PersonTarget("cherie",
            ),
        ],
    "display_name": "Restaurant",
    "outfit": "date",
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
