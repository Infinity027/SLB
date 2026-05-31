init 1:
    image bg date_maidcafe = LayeredImageProxy("bg maidcafe")


init -2 python:
    Room(
    **{
        "name": "date_maidcafe",
        "exits": ["map"],
        "display_name": "Maid Cafe",
        "hours": (14, 17),
        "conditions": [
            IsHour(14, 17),
        ],
        "music": "music/roa_music/chillaxing_waves.ogg",
        "outfit": "casual",
        "tags": ["dateroom"],
    }
)

    Date(
    **{
        "name": "maidcafe",
        "display_name": "Maid Cafe",
        "conditions": [
            ValidRooms("date_maidcafe"),
            HeroTarget(
                IsGender("male")
            ),
            Not(IsDone("reona_redemption_03")),
            PersonTarget(
                "reona",
                OnDate(),
                MinStat("purity", 40),
                MinStat("love", 60),
            ),
        ],
        "clothes": "casual",
        "bypass_greetings": True,
    }
)

label date_maidcafe:
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
