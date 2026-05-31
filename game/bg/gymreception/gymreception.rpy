init python:
    Room(**{
    "name": "gymreception",
    "hours": (6, 22),
    "conditions": [
        IsHour(6, 22),
        InInventory("sport_clothes"),
        ],
    "display_name": "Gym reception",
    "exits": ["map", "gymlockers", "gym", "gymmachine", "mma"],
    "music": "music/roa_music/higher.ogg",
    "outfit": "sport",
    "tags": ["gym"],
    })

    Activity(**{
    "name": "buymembership",
    "duration": 0,
    "money_cost": 20,
    "icon": "membershipcard",
    "rooms": "gymreception",
    "conditions": [
        HeroTarget(IsFlag("gymmember", False)),
        ],
    "display_name": "Buy a membership",
    "label": "buymembership",
    })

    Event(**{
    "name": "gym_out",
    "label": "gym_out",
    "priority": 1000,
    "conditions": [
        HeroTarget(HasRoomTag("gym")),
        Not(InInventory("sport_clothes")),
        ],
    "do_once": False,
    "once_hour": False,
    })

    Event(**{
    "name": "gym_need_membership",
    "label": "gym_need_membership",
    "priority": 1000,
    "conditions": [
        HeroTarget(
            IsRoom("gym", "gymlockers", "gymmachine"),
            IsFlag("gymmember", False),
            Not(IsFlag("job_day", "gymreception")),
            Not(IsFlag("job_night", "gymreception")),
            ),
        ],
    "do_once": False,
    "once_hour": False,
    })

label buymembership:
    $ game.flags.gymmember = TemporaryFlag(True, 7)
    return

label gym_out:
    "I'll need to buy a training outfit to be able to come here."
    $ game.room = "map"
    return

label gym_need_membership:
    "I need a membership to access this room."
    $ game.room = "gymreception"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
