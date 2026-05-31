init 1:
    layeredimage bg audreylivingroom:
        attribute_function DayNightPicker()
        attribute day "audreylivingroom_day"
        attribute night "audreylivingroom_night"

init python:
    Room(**{
    "name": "audreylivingroom",
    "display_name": "Audrey's home",
    "exits": ["audreybedroom", "map"],
    "outfit": "casual",
    "music": "music/roa_music/esperanza.ogg",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget("audrey",
            Not(IsHidden()),
            IsFlag("addressknown", True),
            ),
        Or(
            HeroTarget(
                HasRoomTag("audreyhome"),
                ),
            PersonTarget("audrey",
                HasRoomTag("audreyhome"),
                Not(IsActivity("sleep")),
                ),
            ),
        ],
    "tags": ["audreyhome"],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
