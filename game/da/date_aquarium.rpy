layeredimage bg date_aquarium:
    always:
        "aquarium"

init -2 python:
    Room(
    **{
        "name": "date_aquarium",
        "exits": ["map"],
        "display_name": "Aquarium",
        "hours": (14, 17),
        "conditions": [
            IsHour(14, 17),
        ],
        "music": "music/roa_music/summer_air.ogg",
        "outfit": "casual",
        "tags": ["dateroom"],
    }
)