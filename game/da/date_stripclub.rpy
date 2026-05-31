layeredimage bg date_stripclub:
    always:
        "stripclub"

init python:
    Room(**{
    "name": "date_stripclub",
    "exits": ["map"],
    "display_name": "Strip Club",
    "hours": (18, 4),
    "conditions": [
        IsHour(18, 4),
        ],
    "money_cost": 30,
    "music": "music/darren_curtis/feel_it_in_your_feet.ogg",
    "outfit": "date",
    "tags": ["dateroom"],
    })

    Date(
    "stripclub",
    display_name = "Strip Club",
    conditions=[IsDone("hanna_event_08"),
                ValidRooms("date_stripclub"),
                PersonTarget("hanna",
                            OnDate(),
                            Or(
                                IsFlag("sexydate"),
                                IsFlag("sluttydate"),
                                ),
                ),
                ],
    clothes = "sexydate",
    )

    InteractActivity(**{
    "name": "dance_on_stage",
    "fun": 2,
    "grooming": 0,
    "conditions": [
        HeroTarget(
            IsRoom("date_stripclub"),
            MinStat("energy", 2),
            MinStat("hunger", 3),
            MinStat("grooming", 3),
            MinStat("fun", 1),
            ),
        ActiveTarget(),
        ],
    "display_name": "Ask [date_girl.possessive_adjective] to dance on stage",
    "icon": "dance",
    "label": "date_stripclub_dance_on_stage",
    })

label date_stripclub:
    if active_girl.id == 'hanna':
        call hanna_event_09_intro from _call_hanna_event_09_intro
        return
    else:
        $ renpy.show(active_girl.id)
        "We go to the stripclub."
        $ renpy.hide(active_girl.id)
    return

label date_stripclub_dance_on_stage:
    $ active_girl.set_flag("interact", 1, 1, "+")
    call expression f"{active_girl.id}_greet" from _call_expression_374
    $ renpy.show(active_girl.id)
    call expression f"date_stripclub_dance_on_stage_dialogues_1_{hero.gender}" from _call_expression_375
    if hero.charm >= 40 - active_girl.love or date_girl == active_girl:
        active_girl.say "Sure, why not?"
        $ renpy.hide(active_girl.id)
        show expression f"poledance {active_girl.id}"
        "I watch [active_girl.name] dancing."
        $ bonus = 3
        $ active_girl.love += bonus
        $ hero.fun += 2
        hide expression f"poledance {active_girl.id}"
    else:
        active_girl.say "Sorry, I don't feel it."
        $ hero.cancel_activity()
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
