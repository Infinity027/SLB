init 1:
    layeredimage bg kathome:
        attribute_function DayNightPicker()
        attribute day null
        attribute night null
        always:
            if_any "day"
            "kathome_day"
        always:
            if_any "night"
            "kathome_night"

init python:
    Room(**{
    "name": "kathome",
    "display_name": "Kat's home",
    "exits": ["map"],
    "music": "music/roa_music/buddy.ogg",
    "outfit": "casual",
    "conditions": [
        PersonTarget("kat",
                Not(IsHidden()),
                IsRoom("kathome"),
                Not(IsActivity("sleep")),
                IsDone("kat_event_07")
                )
        ],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
