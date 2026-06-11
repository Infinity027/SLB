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

#     Date(
#     **{
#         "name": "aquarium",
#         "display_name": "Aquarium",
#         "conditions": [
#             HeroTarget(
#                 IsGender("male")
#             ),
#             Not(IsDone("ayesha_date_aquarium")),
#             ValidRooms("date_aquarium"),
#             PersonTarget(
#                 "ayesha",
#                 OnDate(),
#                 MinStat("love", 60),
#             ),
#         ],
#         "clothes": "casual",
#         "love_gain": 1,
#     }
# )