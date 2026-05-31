init 1:
    layeredimage bg date_cinema:
        attribute_function Pickers([DayNightPicker, SeasonPicker])
        group season auto variant "day" if_any "day"
        group season auto variant "night" if_any "night"
        always:
            "snow"

init python:
    Room(**{
    "name": "date_cinema",
    "exits": ["map"],
    "display_name": "Movie Theater",
    "hours": (14, 23),
    "conditions": [
        IsHour(14, 23),
        ],
    "money_cost": 30,
    "music": season_music(),
    "random_music": True,
    "outfit": "casual",
    "tags": ["dateroom"],
    })

    Date(
    "cinema",
    display_name = "Cinema",
    money_cost=30,
    conditions=[ValidRooms("date_cinema")],
    clothes = "casual",
    )

    Activity(**{
    "name": "date_watch_a_movie",
    "duration": 0,
    "rooms": "date_cinema",
    "display_name": "Watch a movie",
    "icon": "cinema",
    "label": "date_watch_movie",
    "once_day": True,
    })

    Activity(**{
    "name": "date_buy_popcorn",
    "duration": 0,
    "rooms": ("date_cinema", "date_cinemaroom"),
    "hunger": 1,
    "icon": "buypopcorn",
    "money_cost": 10,
    "display_name": "Buy popcorn",
    "label": "date_buy_popcorn",
    "once_day": True,
    })

    Event(**{
    "name": "date_no_seat_left",
    "label": "date_no_seat_left",
    "conditions": [
        HeroTarget(IsActivity("date_watch_a_movie")),
        ],
    "chances": 5,
    "once_day": True,
    })

label date_buy_popcorn:
    $ renpy.show(active_girl.id)
    show expression "buy popcorn " + date_girl.id
    "We buy some popcorn."
    call expression active_girl.get_chat from _call_expression_86
    if "gourmand" in active_girl.traits:
        $ game.active_date.score += 5
    show expression "buy popcorn " + date_girl.id
    $ renpy.hide(active_girl.id)
    return

label date_no_seat_left:
    "When we reach the cinema, an employee tells us that it's full."
    $ renpy.show(active_girl.id)
    "[active_girl.name] looks a little disappointed."
    $ renpy.hide(active_girl.id)
    $ choices = [("Leave", 1), ("Convince the employee", 2), ("Try to sneak in", 4)]
    if hero.money >= 10:
        $ choices.append(("Bribe the employee", 3))
    $ result = renpy.display_menu(choices)
    if result == 1:
        call expression f"date_no_seat_left_dialogues_1_{hero.gender}" from _call_expression_283
        $ game.active_date.score += 5
        $ game.pass_time(2, needs=True)
    elif result ==2:
        call expression f"date_no_seat_left_dialogues_2_{hero.gender}" from _call_expression_284
        if hero.charm >= 20:
            $ renpy.say("Employee", "Ok, but just this time.")
            $ game.active_date.score += 5
        else:
            $ renpy.say("Employee", "Absolutely not.")
            $ game.active_date.score += 5
            $ game.pass_time(2, needs=True)
    elif result ==3:
        call expression f"date_no_seat_left_dialogues_3_{hero.gender}" from _call_expression_285
        $ hero.money -= 10
        $ renpy.say("Employee", "Ok, but just this time.")
        $ game.active_date.score += 5
    else:
        "We sneak into the movie theater from the back door."
        if "rebel" in active_girl.traits:
            $ game.active_date.score += 10
        elif "not_rebel" in active_girl.traits:
            $ renpy.show(active_girl.id)
            $ game.active_date.score -= 10
            active_girl.say "We shouldn't be doing that."
            $ renpy.hide(active_girl.id)
    return

label date_cinema:
    if active_girl:
        $ renpy.show(active_girl.id)
        "We go to the cinema."
        $ renpy.hide(active_girl.id)
    return

label date_watch_movie:
    $ renpy.show(active_girl.id)
    active_girl.say "What kind of movie should we go see?"
    $ renpy.dynamic("genre")
    $ genre = renpy.call_screen("select", [(movie.description, movie.id) for movie in Movie.all_movies() if movie.cinema], "movies")
    $ game.room = "date_cinemaroom"
    call enter_room (room_present_girls=[active_girl.id], max_time=2) from _call_enter_room_1
    $ active_girl.object = date_girl
    call apply_movie_gain (genre, active_girl) from _call_apply_movie_gain_1
    $ renpy.dynamic("reactions")
    $ reactions = _return
    call movie_reactions (genre, reactions[0], reactions[1], reactions[2]) from _call_movie_reactions_1
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
