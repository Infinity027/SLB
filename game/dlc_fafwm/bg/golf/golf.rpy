init python:
    Room(**{
    "name": "golf",
    "display_name": "Golf Course",
    "exits": ["map"],
    "music": "music/roa_music/reflection.ogg",
    "outfit": "casual",
    "conditions": [
        IsHour(9, 19),
        ],
    })