init python:
    Room(**{
    "name": "bedroom2",
    "exits": ["secondfloor", "housemap"],
    "display_name": "[bree.name]'s Bedroom",
    "music": "music/roa_music/juice.ogg",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(bree,
            Not(IsHidden()),
        ),
        ],
    "outfit": "casual",
    "tags": ["home"],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
