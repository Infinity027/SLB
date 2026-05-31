init python:

    Room(**{
    "name": "pallalivingroom",
    "display_name": "Palla's home",
    "exits": ["balcony", "shawnbedroom", "pallabedroom", "map"],
    "outfit": "casual",
    "music": "music/roa_music/juice.ogg",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget("palla",
            Not(IsHidden()),
            IsFlag("addressknown", True),
            ),
        Or(
            HeroTarget(
                HasRoomTag("pallahome"),
                ),
            PersonTarget("palla",
                HasRoomTag("pallahome"),
                Not(IsActivity("sleep")),
                ),
            ),
        ],
    "tags": ["pallahome"],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
