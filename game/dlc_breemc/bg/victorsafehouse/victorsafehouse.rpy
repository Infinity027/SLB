init python:
    Room(**{
    "name": "victorsafehouse",
    "display_name": "Victor's Safehouse",
    "exits": ["map"],
    "conditions": [
        'not Room.find("victorsafehouse").hidden',
        HeroTarget(
            IsGender("female"),
            ),
        PersonTarget("victor",
            Not(IsHidden()),
            IsRoom("victorsafehouse"),
            Not(IsActivity("sleep")),
            ),
        ],
    "music": "music/TeknoAXE/simple_metal.ogg",
    "valid": False,
    "outfit": "casual",
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
