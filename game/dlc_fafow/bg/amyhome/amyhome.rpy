init 1:
    layeredimage bg amyhome:
        attribute_function DayNightPicker()
        attribute day null
        attribute night null
        always:
            if_any "day"
            "amyhome_day"
        always:
            if_any "night"
            "amyhome_night"

init python:
    Room(**{
    "name": "amyhome",
    "display_name": "Amy's home",
    "exits": ["map"],
    "music": "music/roa_music/reflection.ogg",
    "outfit": "casual",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget("amy",
            Not(IsHidden()),
            IsRoom("amyhome"),
            Not(IsActivity("sleep")),
            ),
        Or(
            IsDone("amy_event_08"),
            PersonTarget("amy",
                IsFlag("addressknown", True),
                ),
            ),
        ],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
