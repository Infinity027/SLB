init python:
    Room(**{
    "name": "bedroom2",
    "exits": ["secondfloor", "housemap"],
    "display_name": "[bree.name]'s Bedroom",
    "music": "music/roa_music/juice.ogg",
    "conditions": [
        PersonTarget(bree,
            Not(IsHidden()),
        ),
        ],
    "outfit": "casual",
    "tags": ["home"],
    })