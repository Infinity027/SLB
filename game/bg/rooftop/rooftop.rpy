init python:
    Room(**{
    "name": "rooftop",
    "hours": (18, 20),
    "conditions": [
        IsHour(18, 20),
        PersonTarget("kleio",
                Not(IsHidden()),
                IsDone("kleio_event_10"),
                Not(IsDone("kleio_event_11"))
                )
        ],
    "display_name": "Rooftop",
    "exits": ["map"],
    "outfit":"casual",
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
