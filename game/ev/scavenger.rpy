init python:
    Activity(**{
    "name": "scavenger_get_clue",
    "duration": 0,
    "display_name": "Get scavenger hunt clue",
    "conditions": [
        "isinstance(game.active_date, ScavengerHuntAppointment)",
        ],
    "label": "scavenger_get_clue",
    "icon": "cheat",
    })

    Activity(**{
    "name": "scavenger_guess",
    "duration": 0,
    "display_name": "Guess scavenger hunt",
    "conditions": [
        "isinstance(game.active_date, ScavengerHuntAppointment)",
        ],
    "label": "scavenger_guess",
    "icon": "investigate",
    })

label scavenger_do_date(date):
    $ active_girl.object = date.participants[0]
    $ scavenger_girl = active_girl.object
    $ game.active_date = date
    $ game.room = date.start_location
    $ date.stay = True
    scene expression f"bg {game.room}"
    call expression f"{date.base}_start" from _scavenger_do_date_start
    call scavenger_get_clue from _scavenger_do_date_start2
    while date.stay:
        $ active_girl.object = scavenger_girl
        call enter_room (room_present_girls=[scavenger_girl.id], max_time=1) from _scavenger_do_date_enter_room


    call expression f"{date.base}_finish" from _scavenger_do_date_finish
    $ scavenger_girl.love += int((date.score * 0.2) - 10)
    $ game.active_date = NoDateEvent()
    $ active_girl.object = None
    $ scavenger_girl.object = None
    return

label scavenger_get_clue:
    call expression f"{game.active_date.base}_clue_{game.active_date.current_clue}" from _call_expression_72
    return

label scavenger_guess:
    call expression f"{game.active_date.base}_guess_{game.active_date.current_clue}" from _call_expression_74
    if _return:

        "The app makes a triumphant dinging noise. That was the correct answer!"
        $ game.active_date.total += (game.active_date.max_attempts - game.active_date.current_attempts) * game.active_date.points_per_attempt
        $ game.active_date.score += (game.active_date.max_attempts - game.active_date.current_attempts) * game.active_date.points_per_attempt
        call scavenger_next_clue from _scavenger_guess
    else:

        "The app makes a buzzing noise. That is incorrect."
        $ game.active_date.current_attempts += 1
        if game.active_date.current_attempts >= game.active_date.max_attempts:
            "It looks like we ran out of guesses for that clue."
            call scavenger_next_clue from _scavenger_guess2

    return

label scavenger_next_clue:
    $ game.active_date.current_clue += 1
    $ game.active_date.current_attempts = 0
    $ game.active_date.tried = set()
    if renpy.has_label(f"{game.active_date.base}_clue_{game.active_date.current_clue}"):
        call scavenger_get_clue from _scavenger_hunt_next_clue
    else:
        $ game.active_date.stay = False
        $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
