init 1:
    image bg date_forest = LayeredImageProxy("bg forest")


init -2 python:
    Room(
    **{
        "name": "date_forest",
        "exits": ["map"],
        "display_name": "Forest",
        "hours": (14, 17),
        "conditions": [
            IsHour(14, 17),
        ],
        "music": "music/roa_music/summer_air.ogg",
        "outfit": "casual",
        "tags": ["dateroom"],
    }
)
