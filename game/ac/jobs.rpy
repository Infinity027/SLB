init python:
    Activity(**{
    "name": "ask_for_a_job_male",
    "duration": 0,
    "icon": "askforjob",
    "rooms": ("bakery", "bookstore", "coffeeshop", "electronic", "gymreception", "sexshop"),
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsFlag("job_day", False),
            IsFlag("fired"),
            ),
        ],
    "display_name": "Ask for a job",
    "label": "ask_for_a_job_day",
    })

    Activity(**{
    "name": "quit_job_day",
    "duration": 0,
    "icon": "quitjob",
    "rooms": ("alley", "church", "bakery", "bookstore", "clothesshop", "coffeeshop", "electronic", "flowershop", "gymreception", "jewelrystore", "maidcafe", "photostudio", "university"),
    "conditions": [
        HeroTarget(
            IsFlag("job_day", "church", "bakery", "bookstore", "clothesshop", "coffeeshop", "electronic", "flowershop", "gym", "homelessshelter", "jewelrystore", "maidcafe", "model", "pornstar", "prostitute", "university"),
            ),
        'game.flags.job_day == game.room or (game.room == "alley" and game.flags.job_day in ["homelessshelter", "prostitute"]) or (game.room == "photostudio" and game.flags.job_day in ["model", "pornstar"])',
        ],
    "display_name": "Quit your day job",
    "once_day": True,
    "label": "quit_a_job_day",
    })

    Activity(**{
    "name": "quit_job_night",
    "duration": 0,
    "icon": "quitjob",
    "rooms": ("alley", "gymreception", "nightclub", "photostudio", "pub", "sexshop", "stripclub"),
    "conditions": [
        HeroTarget(
            IsFlag("job_night", "gym", "homelessshelter", "model", "nightclub", "pub", "pornstar", "prostitute", "sexshop", "stripclub"),
            ),
        'game.flags.job_night == game.room or (game.room == "alley" and game.flags.job_night in ["homelessshelter", "prostitute"]) or (game.room == "photostudio" and game.flags.job_night in ["model", "pornstar"])',
        ],
    "display_name": "Quit your night job",
    "once_day": True,
    "label": "quit_a_job_night",
    })

label ask_for_a_job:
    call expression f"ask_for_a_job_dialogues_1_{hero.gender}" from _call_expression_113
    "Shop owner" "Sure, the job is yours."
    if not game.flags.job_day:
        $ game.flags.job_day = game.room
    elif not game.flags.job_night:
        $ game.flags.job_night = game.room
    return

label ask_for_a_job_day:
    call expression f"ask_for_a_job_dialogues_1_{hero.gender}" from _call_expression_249
    "Shop owner" "Sure, the job is yours."
    $ game.flags.job_day = game.room
    return

label ask_for_a_job_night:
    call expression f"ask_for_a_job_dialogues_1_{hero.gender}" from _call_expression_250
    "Shop owner" "Sure, the job is yours."
    $ game.flags.job_night = game.room
    return

label quit_a_job_day:
    call expression f"quit_a_job_dialogues_1_{hero.gender}" from _call_expression_114
    "Shop owner" "That's a shame..."
    $ game.flags.job_day = False
    return

label quit_a_job_night:
    call expression f"quit_a_job_dialogues_1_{hero.gender}" from _call_expression_251
    "Shop owner" "That's a shame..."
    $ game.flags.job_night = False
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
