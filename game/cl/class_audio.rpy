
init -15 python:



    def season_music():
        music = [
        ("music/roa_music/spring.ogg", "game.season == 0"),
        ("music/roa_music/feel_better.ogg", "game.season == 0"),
        ("music/roa_music/walk_around.ogg", "game.season == 1"),
        ("music/roa_music/coastline.ogg", "game.season == 1"),
        ("music/roa_music/leaves.ogg", "game.season == 2"),
        ("music/roa_music/something_special.ogg", "game.season == 2"),
        ("music/roa_music/winter_magic.ogg", "game.season == 3"),
        ("music/darren_curtis/just_the_right_pace.ogg", "game.season == 3"),
    ]
        return music


    def house_music():
        music = [
        (
            "music/roa_music/memories.ogg",
            "(game.day % 2 == 0) and (game.hour % 3 != 0)",
        ),
        ("music/roa_music/journey.ogg", "(game.day % 2 != 0) and (game.hour % 3 != 0)"),
        ("music/roa_music/sunny.ogg", "(game.hour % 3 == 0)"),
    ]
        return music
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
