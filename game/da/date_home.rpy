layeredimage bg date_livingroom:
    always:
        "bg livingroom"

init -2 python:
    Room(
    **{
        "name": "date_livingroom",
        "exits": ["map"],
        "display_name": "Home",
        "music": house_music(),
        "outfit": "casual",
        "tags": ["dateroom"],
    }
)

    Date(
    "livingroom",
    display_name="Home",
    clothes="casual",
    conditions=[ValidRooms("date_livingroom")],
    love_gain=0,
)

    Activity(
    **{
        "name": "date_play_console",
        "icon": "videogame",
        "rooms": "date_livingroom",
        "conditions": [
            InInventory("zbox_360"),
        ],
        "display_name": "Play console",
        "label": "date_play_console",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_play_boardgame",
        "icon": "boardgame",
        "rooms": "date_livingroom",
        "display_name": "Play boardgame",
        "label": "date_play_boardgame",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_snacks",
        "hunger": 2,
        "icon": "eat",
        "rooms": "date_livingroom",
        "conditions": [
            HeroTarget(
                MinStat("energy", 0),
                MinStat("hunger", 0),
                MinStat("grooming", 0),
                MinStat("fun", 0),
                Not(MaxStat("hunger")),
            ),
        ],
        "display_name": "Make some snacks",
        "label": "date_snacks",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_watch_tv",
        "icon": "tv",
        "rooms": "date_livingroom",
        "display_name": "Watch TV",
        "label": "date_watch_tv",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_chat_couch",
        "icon": "talk",
        "rooms": "date_livingroom",
        "display_name": "Chat on the couch",
        "label": "date_chat_couch",
    }
)

    Activity(
    **{
        "name": "date_play_guitar",
        "icon": "guitar",
        "rooms": "date_livingroom",
        "conditions": [
            HeroTarget(
                IsGender("male"),
            ),
            HasSkill("guitar"),
        ],
        "display_name": "Play guitar",
        "label": "date_play_guitar",
    }
)

    Activity(
    **{
        "name": "date_swim_pool_home",
        "fun": 1,
        "rooms": "date_livingroom",
        "conditions": [
            IsSeason(0, 1),
            HeroTarget(
                MinStat("energy", 3),
                MinStat("hunger", 3),
                MinStat("grooming", 0),
                MinStat("fun", 3),
            ),
            InInventory("swimsuit"),
        ],
        "display_name": "Go for a swim",
        "label": "date_swim_pool_home",
        "once_day": True,
        "icon": "swim",
    }
)

    Activity(
    **{
        "name": "date_hot_tub_home",
        "charm": 1,
        "fun": 1,
        "energy": 1,
        "grooming": 1,
        "rooms": "date_livingroom",
        "conditions": [
            HeroTarget(
                MinStat("energy", 0),
                MinStat("hunger", 3),
                MinStat("grooming", 0),
                MinStat("fun", 0),
                IsFlag("hottubrepaired"),
            ),
            InInventory("swimsuit"),
        ],
        "display_name": "Dip in the hot tub",
        "label": "date_hot_tub_home",
        "once_day": True,
        "icon": "hottub",
    }
)

    Activity(
    **{
        "name": "date_pool_suntan",
        "energy": 2,
        "icon": "tan",
        "rooms": "date_livingroom",
        "conditions": [
            IsHour(9, 19),
            InInventory("lotion"),
            IsSeason(0, 1),
        ],
        "display_name": "Apply sunscreen",
        "label": "date_suntan",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_walk_outside",
        "energy": 2,
        "icon": "leash",
        "rooms": "date_livingroom",
        "conditions": [
            IsTimeOfDay("evening"),
            DateTarget(
                IsGender("female"),
                IsFlag("collared"),
                IsFlag("walk_outside"),
                MinStat("sub", 100),
            ),
        ],
        "display_name": "Take her for a walk",
        "label": "date_walk_outside",
        "once_day": True,
    }
)

label date_chat_couch:
    $ renpy.show(f"chatting {active_girl.id} livingroom")
    "We sit on the couch to chat."
    call expression active_girl.get_chat from _call_expression_7
    $ renpy.hide("chatting")
    return

label date_watch_tv:
    show expression f"watch date tv {active_girl.id}"
    $ renpy.dynamic("genre")
    $ renpy.dynamic("reactions")
    $ genre = renpy.call_screen("select", [(movie.description, movie.id) for movie in Movie.all_movies()], "movies", None)
    if genre != "porn":
        "We watch some TV."
        call apply_movie_gain (genre, active_girl) from _call_apply_movie_gain_2
        $ reactions = _return
        call movie_reactions (genre, reactions[0], reactions[1], reactions[2]) from _call_movie_reactions_2
    else:
        if hero.charm >= 100 - active_girl.love:
            "We watch some porn."
            call apply_movie_gain (genre, active_girl) from _call_apply_movie_gain_3
            $ reactions = _return
            $ renpy.dynamic("subgenre")
            menu:
                "SM porn":
                    $ subgenre = "sm"
                "Femdom porn":
                    $ subgenre = "femdom"
                "Gonzo porn":
                    $ subgenre = "gonzo"
                "Lesbian porn":
                    $ subgenre = "lesbian"
            call apply_porn_extra_gains (subgenre, active_girl) from _call_apply_porn_extra_gains_1
            call movie_reactions (genre, reactions[0], reactions[1], reactions[2]) from _call_movie_reactions_3
        else:
            hide expression f"watch date tv {active_girl.id}"
            $ renpy.show(active_girl.id)
            active_girl.say "Sorry, I don't want to watch this sort of thing."
            $ game.active_date.score -= 5
            $ renpy.hide(active_girl.id)
    hide expression f"watch date tv {active_girl.id}"
    return

label date_swim_pool_home:
    scene bg pool
    if renpy.has_label(f"{active_girl.id}_date_swim_pool_home_{hero.gender}"):
        call expression f"{active_girl.id}_date_swim_pool_home_{hero.gender}" from _call_expression_286
    else:
        $ game.active_date.clothes = "swimsuit"
        show expression "playing water pool " + date_girl.id
        "We go to the pool and play in the water."
        hide expression "playing water pool " + date_girl.id
    if "playful" in date_girl.traits or "sporty" in date_girl.traits:
        $ game.active_date.score += 5
    if "not_playful" in date_girl.traits or "not_sporty" in date_girl.traits:
        $ game.active_date.score -= 5
    $ game.active_date.clothes = None
    return

label date_hot_tub_home:
    $ game.active_date.clothes = "swimsuit"
    if active_girl.sub >= 25 and active_girl.sexperience >= 1:
        $ renpy.show(f"hottub {active_girl.id} naked")
    else:
        $ renpy.show(f"hottub {active_girl.id}")
    if renpy.has_label(f"{active_girl.id}_hottub"):
        call expression f"{active_girl.id}_hottub" from _call_expression_172
    else:
        "We spend a relaxing time in the hot tub."
    $ game.active_date.score += 5
    $ game.active_date.clothes = None
    hide hottub
    return

label date_snacks:
    $ renpy.show(f"eat snacks {active_girl.id}")
    "We go to the kitchen and eat some snacks."
    call expression active_girl.get_chat from _call_expression_4
    $ game.active_date.score += 5
    $ renpy.hide(f"eat snacks {active_girl.id}")
    return

label date_play_console:
    $ renpy.dynamic(difficulty=0)
    $ renpy.show(active_girl.id)
    show expression f"play console {active_girl.id}"
    "I play some video games with [active_girl.name]."
    if "geek" in active_girl.traits:
        $ difficulty += 1
    if "playful" in active_girl.traits:
        $ difficulty += 1
    if "not_geek" in active_girl.traits:
        $ difficulty -= 1
    if "not_playful" in active_girl.traits:
        $ difficulty -= 1
    $ game.active_date.score += difficulty * 5
    if hero.has_skill("video_games") or hero.knowledge >= date_girl.sub:
        $ date_girl.sub += 2
        "I won!"
    else:
        $ date_girl.sub -= 2
        "I lose."
    hide expression f"play console {active_girl.id}"
    $ renpy.hide(active_girl.id)
    return

label date_play_guitar:
    $ renpy.dynamic(difficulty=1)
    $ renpy.show(f"play guitar {active_girl.id}")
    "I play some guitar for [active_girl.name]."
    if "music" in active_girl.traits:
        $ difficulty += 1
    $ game.active_date.score += difficulty * 5
    $ renpy.hide(f"play guitar {active_girl.id}")
    return

label date_play_boardgame:
    $ renpy.dynamic(difficulty=0)
    $ renpy.show(f"board games {active_girl.id}")
    "I play some boardgames with [active_girl.name]."
    if "geek" in active_girl.traits:
        $ difficulty += 1
    if "playful" in active_girl.traits:
        $ difficulty += 1
    if "not_geek" in active_girl.traits:
        $ difficulty -= 1
    if "not_playful" in active_girl.traits:
        $ difficulty -= 1
    $ game.active_date.score += difficulty * 5
    if hero.knowledge >= date_girl.sub:
        $ date_girl.sub += 2
        "I won!"
    else:
        $ date_girl.sub -= 2
        "I lose."
    $ renpy.hide(f"board games {active_girl.id}")
    return

label date_livingroom:
    $ renpy.show(active_girl.id)
    "We decide to hang out at the house."
    $ renpy.hide(active_girl.id)
    return

label date_walk_outside:
    $ game.active_date.score += 5
    $ renpy.show(active_girl.id)
    if renpy.has_label(f"{active_girl.id}_walk_outside"):
        call expression f"{active_girl.id}_walk_outside" from _call_expression_287
    else:
        "I take her for a walk."
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
