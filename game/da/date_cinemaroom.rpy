layeredimage bg date_cinemaroom:
    always:
        "cinemaroom"

init -2 python:
    Room(
    **{
        "name": "date_cinemaroom",
        "exits": ["date_cinema"],
        "display_name": "Movie Theater",
        "hours": (14, 23),
        "conditions": [
            IsHour(14, 23),
        ],
        "music": season_music(),
        "random_music": True,
        "outfit": "casual",
        "tags": ["dateroom"],
    }
)

    Activity(
    **{
        "name": "date_put_hand_on_leg",
        "display_name": "Hand on leg",
        "icon": "caress",
        "label": "date_put_hand_on_leg",
        "rooms": "date_cinemaroom",
        "conditions": [
            HeroTarget(IsGender("male")),
            ActiveTarget(
                IsFlag("datehand", False)
                ),
        ],
        "once_day": True,
        "duration": 0,
    }
)

    Activity(
    **{
        "name": "date_put_hand_between_legs",
        "display_name": "Hand between [date_girl.possessive_adjective] legs",
        "icon": "between",
        "label": "date_put_hand_between_legs",
        "once_day": True,
        "rooms": "date_cinemaroom",
        "conditions": [
            HeroTarget(IsGender("male")),
            ActiveTarget(
                IsFlag("datehand", "leg")
                ),
        ],
        "duration": 0,
    }
)

    Activity(
    **{
        "name": "date_put_hand_in_panties",
        "display_name": "Finger her",
        "icon": "finger",
        "rooms": "date_cinemaroom",
        "conditions": [
            HeroTarget(IsGender("male")),
            ActiveTarget(
                IsFlag("datehand", "between"),
                IsGender("female"),
            ),
        ],
        "label": "date_put_hand_in_panties",
        "once_day": True,
        "duration": 0,
    }
)

    Activity(
    **{
        "name": "date_caress_boobs",
        "display_name": "Caress her boobs",
        "rooms": "date_cinemaroom",
        "conditions": [
            HeroTarget(IsGender("male")),
            ActiveTarget(
                IsFlag("datehand", False),
                IsGender("female"),
            ),
        ],
        "label": "date_caress_boobs",
        "icon": "caressboobs",
        "once_day": True,
        "duration": 0,
    }
)

    Activity(
    **{
        "name": "date_caress_boobs_inside",
        "display_name": "Put your hand inside",
        "label": "date_caress_boobs_inside",
        "rooms": "date_cinemaroom",
        "conditions": [
            HeroTarget(IsGender("male")),
            ActiveTarget(
                IsFlag("datehand", "breasts"),
                IsGender("female"),
            ),
        ],
        "icon": "handinbra",
        "once_day": True,
        "duration": 0,
    }
)

    Activity(
    **{
        "name": "date_watch_the_movie",
        "display_name": "Watch the movie",
        "fun": 2,
        "icon": "cinema",
        "label": "date_watch_the_movie",
        "rooms": "date_cinemaroom",
    }
)

label date_watch_the_movie:
    $ renpy.show(f"watch movie happy {active_girl.id}")
    "I watch the movie with [active_girl.name]."
    hide watch movie
    return

label date_caress_boobs_inside:
    $ renpy.show(f"watch movie grab inside happy {active_girl.id}")
    "I move my hand inside her top to caress her skin directly."
    if active_girl.love <= 100 - hero.charm:
        active_girl.say "What do you think you are doing?"
        $ renpy.show("watch movie normal")
        $ active_girl.flags.datehand = TemporaryFlag(False, 1)
        $ game.active_date.score -= 10
    else:
        $ renpy.show("watch movie blush")
        "She blushes a little when my fingers reach her nipples."
        $ renpy.show("watch movie normal")
        "After a while I remove my hand..."
        "She looks a little disappointed."
        $ active_girl.flags.datehand = TemporaryFlag(False, 1)
        if "slutty" in active_girl.traits:
            $ game.active_date.score += 20
        else:
            $ game.active_date.score += 5
    hide watch movie
    return

label date_caress_boobs:
    $ renpy.show(f"watch movie grab outside happy {active_girl.id}")
    "I start caressing her breasts above her clothes."
    if active_girl.love <= 75 - hero.charm:
        active_girl.say "What do you think you are doing?"
        $ renpy.show("watch movie normal")
        $ game.active_date.score -= 10
    else:
        "She looks a little anxious but let my hand caress her."
        $ active_girl.flags.datehand = TemporaryFlag("breasts", 1)
        if "slutty" in active_girl.traits:
            $ game.active_date.score += 5
    hide watch movie
    return

label date_put_hand_in_panties:
    $ renpy.show(f"watch movie finger outside happy {active_girl.id}")
    "I push her underwear aside and try to put my finger inside her."
    if active_girl.love <= 125 - hero.charm:
        active_girl.say "What do you think you are doing?"
        $ renpy.show("watch movie normal")
        $ active_girl.flags.datehand = TemporaryFlag(False, 1)
        $ game.active_date.score -= 10
    else:
        $ renpy.show("watch movie finger inside blush")
        "Her breath starts to get heavy as I finger her."
        active_girl.say "Mmmmmmh."
        "She slowly reaches her climax, while watching the movie."
        $ active_girl.flags.datehand = TemporaryFlag(False, 1)
        if "slutty" in active_girl.traits:
            $ game.active_date.score += 20
        else:
            $ game.active_date.score += 5
    hide watch movie
    return

label date_put_hand_between_legs:
    $ renpy.show(f"watch movie finger outside happy {active_girl.id}")
    "I move my hand up toward [active_girl.name]'s panties."
    if active_girl.love <= 100 - hero.charm:
        active_girl.say "What do you think you are doing?"
        $ renpy.show("watch movie normal")
        $ active_girl.flags.datehand = TemporaryFlag(False, 1)
        $ game.active_date.score -= 10
    else:
        "She moans a little when I reach her underwear."
        $ active_girl.flags.datehand = TemporaryFlag("between", 1)
        if "slutty" in active_girl.traits:
            $ game.active_date.score += 5
    hide watch movie
    return

label date_put_hand_on_leg:
    $ renpy.show(f"watch movie happy {active_girl.id}")
    "I slowly move my hand to [active_girl.name]'s leg."
    if active_girl.love <= 75 - hero.charm:
        active_girl.say "What do you think you are doing?"
        $ game.active_date.score -= 10
    else:
        if active_girl.is_female:
            $ renpy.show("watch movie leg")
            "Her skin is soft under my fingers."
            "She looks at my hand but doesn't say anything."
        else:
            "I put my hand on his leg."
        $ active_girl.flags.datehand = TemporaryFlag("leg", 1)
        if "slutty" in active_girl.traits:
            $ game.active_date.score += 5
    hide watch movie
    return

label date_put_hand_on_crotch:
    $ renpy.show(f"watch movie leg happy {active_girl.id}")
    "I slowly move my hand to [active_girl.name]'s crotch."
    $ active_girl.flags.datehand = TemporaryFlag("crotch", 1)
    if "sluts" in active_girl.desire_factors:
        $ game.active_date.score += 5
    hide watch movie
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
