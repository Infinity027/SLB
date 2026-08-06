init python:
    Room(**{
    "name": "restaurant",
    "exits": ["map"],
    "conditions":[
        IsHour(18, 23),
        HeroTarget(Not(OnDate())),
        PersonTarget("cherie",
            ),
        ],
    "display_name": "Restaurant",
    "outfit": "date",
    })