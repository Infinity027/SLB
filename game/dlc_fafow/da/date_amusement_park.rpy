init 2:
    layeredimage bg amusement:
        attribute_function Pickers([DayNightPicker, SeasonPicker])
        group season auto variant "day" if_any "day"
        group season auto variant "night" if_any "night"
        always:
            "snow"

    image bg date_amusement = LayeredImageProxy("bg amusement")

init -2 python:
    Room(
    **{
        "name": "date_amusement",
        "exits": ["map"],
        "display_name": "Amusement Park",
        "hours": (14, 17),
        "conditions": [
            IsHour(14, 17),
        ],
        "music": "music/roa_music/summer_air.ogg",
        "outfit": "casual",
        "tags": ["dateroom"],
    }
)

    Date(
    "amusement",
    display_name="Amusement Park",
    conditions=[ValidRooms("date_amusement")],
    love_gain=3,
)

    Activity(
    **{
        "name": "date_icecream_amusement",
        "money_cost": 10,
        "hunger": 1,
        "icon": "icecream",
        "rooms": "date_amusement",
        "display_name": "Have an ice cream",
        "label": "date_icecream_amusement",
        "conditions": [
            IsSeason(0, 1),
        ],
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_ferris_wheel",
        "icon": "ferriswheel",
        "rooms": "date_amusement",
        "display_name": "Ride the ferris wheel",
        "label": "date_ferris_wheel",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_merry_go_round",
        "icon": "merrygoround",
        "rooms": "date_amusement",
        "display_name": "Ride the merry go round",
        "label": "date_merry_go_round",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_haunted_house",
        "icon": "hauntedhouse",
        "rooms": "date_amusement",
        "display_name": "Go to the haunted house",
        "label": "date_haunted_house",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_love_boat",
        "icon": "loveboat",
        "rooms": "date_amusement",
        "display_name": "Ride a love boat",
        "label": "date_love_boat",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_hedge_maze",
        "icon": "hedgemaze",
        "rooms": "date_amusement",
        "display_name": "Try the hedge maze",
        "label": "date_hedge_maze",
        "once_day": True,
    }
)

label date_hedge_maze:
    show expression "hedge maze " + date_girl.id
    if renpy.has_label(f"{active_girl.id}_hedge_maze_reaction_{hero.gender}"):
        call expression f"{active_girl.id}_hedge_maze_reaction_{hero.gender}" from _call_expression_482
    else:
        "We try out the hedge maze together."
    call expression date_girl.get_chat from _call_expression_483
    hide expression "hedge maze " + date_girl.id
    return


label date_love_boat:
    show expression "love boat " + date_girl.id
    if renpy.has_label(f"{active_girl.id}_love_boat_reaction_{hero.gender}"):
        call expression f"{active_girl.id}_love_boat_reaction_{hero.gender}" from _call_expression_484
    else:
        "We ride a love boat together."
    call expression date_girl.get_chat from _call_expression_485
    hide expression "love boat " + date_girl.id
    return

label date_haunted_house:
    show expression "haunted house " + date_girl.id
    if renpy.has_label(f"{active_girl.id}_haunted_house_reaction_{hero.gender}"):
        call expression f"{active_girl.id}_haunted_house_reaction_{hero.gender}" from _call_expression_486
    else:
        "We go to the haunted house together."
    call expression date_girl.get_chat from _call_expression_487
    hide expression "haunted house " + date_girl.id
    return

label date_merry_go_round:
    show expression "merry go round " + date_girl.id
    if renpy.has_label(f"{active_girl.id}_merry_go_round_reaction_{hero.gender}"):
        call expression f"{active_girl.id}_merry_go_round_reaction_{hero.gender}" from _call_expression_488
    else:
        "We ride the merry go round together."
    call expression date_girl.get_chat from _call_expression_489
    hide expression "merry go round " + date_girl.id
    return

label date_ferris_wheel:
    show expression f"ferris wheel {date_girl.id}"
    if renpy.has_label(f"{active_girl.id}_ferris_wheel_reaction_{hero.gender}"):
        call expression f"{active_girl.id}_ferris_wheel_reaction_{hero.gender}" from _call_expression_490
    else:
        "We ride the ferris wheel together."
    call expression date_girl.get_chat from _call_expression_491
    hide expression f"ferris wheel {date_girl.id}"
    return

label date_icecream_amusement:
    show expression f"amusement icecream {date_girl.id}"
    if renpy.has_label(f"{active_girl.id}_date_amusement_ice_cream_{hero.gender}"):
        call expression f"{active_girl.id}_date_amusement_ice_cream_{hero.gender}" from _call_expression_519
    else:
        "We eat an ice cream together."
    call expression date_girl.get_chat from _call_expression_493
    if "gourmand" in date_girl.traits:
        $ game.active_date.score += 5
    hide expression f"amusement icecream {date_girl.id}"
    return

label date_amusement:
    $ renpy.show(date_girl.id)
    if renpy.has_label(active_girl.id + "_date_amusement_park_" + hero.gender):
        call expression active_girl.id + "_date_amusement_park_" + hero.gender from _call_expression_509
    else:
        "We go to the amusement park."
    $ renpy.hide(date_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
