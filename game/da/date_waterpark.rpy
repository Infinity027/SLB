layeredimage bg date_waterpark:
    always:
        "waterpark"

init -2 python:
    Room(
    **{
        "name": "date_waterpark",
        "exits": ["map"],
        "display_name": "Waterpark",
        "hours": (14, 17),
        "conditions": [
            IsHour(14, 17),
            IsSeason(0, 1),
            InInventory("swimsuit"),
        ],
        "money_cost": 10,
        "required_item": "swimsuit",
        "music": "music/roa_music/endless_summer.ogg",
        "outfit": "swimsuit",
        "tags": ["dateroom"],
    }
)

    Date(
    "waterpark",
    display_name="Water park",
    money_cost=100,
    conditions=[ValidRooms("date_waterpark")],
    clothes="swimsuit",
    love_gain=2,
)

    Activity(
    **{
        "name": "date_try_the_waterslide",
        "icon": "waterslide",
        "display_name": "Waterslide",
        "rooms": "date_waterpark",
        "fun": 2,
        "label": "date_try_the_waterslide",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_icecream",
        "money_cost": 10,
        "hunger": 1,
        "icon": "icecream",
        "rooms": "date_waterpark",
        "display_name": "Have an ice cream",
        "label": "date_icecream",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_spa",
        "money_cost": 50,
        "energy": 2,
        "icon": "spa",
        "rooms": "date_waterpark",
        "display_name": "Go to the spa",
        "label": "date_spa",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_swimmingrace",
        "energy": -2,
        "icon": "swim",
        "rooms": "date_waterpark",
        "display_name": "Swim with [date_girl.possessive_adjective] in the pool",
        "label": "date_swimmingrace",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_play_waterpark",
        "icon": "playinsea",
        "rooms": "date_waterpark",
        "display_name": "Play in the pool",
        "label": "date_play_waterpark",
        "once_day": True,
    }
)

label date_play_waterpark:
    show expression "playing water waterpark " + date_girl.id
    "I play with [date_girl.name] in the pool."
    call expression date_girl.get_chat from _call_expression_67
    $ bonus = 0
    if "playful" in date_girl.traits:
        $ bonus += 5
    if "sporty" in date_girl.traits:
        $ bonus += 5
    if "not_playful" in date_girl.traits:
        $ bonus -= 5
    if "not_sporty" in date_girl.traits:
        $ bonus -= 5
    $ game.active_date.score += bonus
    hide expression "playing water waterpark " + date_girl.id
    return

label date_swimmingrace:
    $ renpy.show(active_girl.id)
    show expression "swimmingrace " + date_girl.id
    "I swim with [active_girl.name] in the pool."
    $ game.active_date.score += 5
    call expression active_girl.get_chat from _call_expression_2
    if "sporty" in active_girl.traits:
        $ game.active_date.score += 5
    if hero.fitness >= date_girl.sub:
        $ date_girl.sub += 2
        "I won!"
    else:
        $ date_girl.sub -= 2
        "I lose."
    hide expression "swimmingrace " + date_girl.id
    return

label date_spa:
    $ renpy.show(active_girl.id)
    "We have a relaxing time in the spa."
    $ game.active_date.score += 5
    call expression active_girl.get_chat from _call_expression_3
    if "princess" in active_girl.traits:
        $ game.active_date.score += 5
    $ renpy.hide(active_girl.id)
    return

label date_icecream:
    show expression f"beach icecream waterpark {active_girl.id}"
    "We eat an ice cream together."
    call expression active_girl.get_chat from _call_expression_31
    if "gourmand" in active_girl.traits:
        $ game.active_date.score += 5
    hide expression f"beach icecream waterpark {active_girl.id}"
    return

label date_try_the_waterslide:
    "We go to the waterslide."
    if renpy.has_label(f"{active_girl.id}_date_try_the_waterslide"):
        call expression f"{active_girl.id}_date_try_the_waterslide" from _call_expression_26
    else:
        show expression "waterslide " + date_girl.id
        if "not_playful" in active_girl.traits:
            active_girl.say "Urgh..."
            $ game.active_date.score -= 5
        elif "playful" not in active_girl.traits:
            active_girl.say "Why not..."
            $ game.active_date.score += 5
        else:
            active_girl.say "Yes, sure."
            $ game.active_date.score += 10
        hide expression "waterslide " + date_girl.id
    return

label date_waterpark:
    $ renpy.show(active_girl.id)
    "We go to a water park."
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
