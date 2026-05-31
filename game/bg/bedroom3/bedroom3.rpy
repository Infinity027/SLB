init python:
    Room(**{
    "name": "bedroom3",
    "exits": ["secondfloor", "housemap"],
    "display_name": "Sasha's Bedroom",
    "conditions": [
                    PersonTarget(sasha,
                        Not(IsHidden()),
                    ),
                  ],
    "music": "music/roa_music/smile_for_me.ogg",
    "outfit": "casual",
    "tags": ["home"],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
