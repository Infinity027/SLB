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

#     Date(
#     **{
#         "name": "forest",
#         "display_name": "Forest",
#         "conditions": [
#             ValidRooms("date_forest"),
#             Or(
#                 And(
#                     HeroTarget(
#                         IsGender("male")
#                     ),
#                     Not(IsDone("ayesha_date_forest")),
#                     PersonTarget(
#                         "ayesha",
#                         OnDate(),
#                         MinStat("love", 60),
#                     ),
#                 ),
#                 And(
#                     Not(IsDone("amy_date_forest")),
#                     HeroTarget(
#                         IsGender("male"),
#                         HasStamina()
#                     ),
#                     PersonTarget(
#                         "amy",
#                         OnDate(),
#                         MinStat("love", 120),
#                         MinStat("sexperience", 1),
#                     ),
#                 ),
#                 And(
#                     Not(IsDone("reona_date_forest")),
#                     HeroTarget(
#                         IsGender("male"),
#                         HasStamina()
#                     ),
#                     PersonTarget(
#                         "reona",
#                         OnDate(),
#                         MinStat("purity", 80),
#                         MinStat("love", 150),
#                     ),
#                 ),
#             ),
#         ],
#         "clothes": "casual",
#         "bypass_greetings": True,
#     }
# )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
