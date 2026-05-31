init python:
    Item("anal_beads", price=200)
    Item("vibrator", price=200)
    Item("dildo", price=400)
    Item("double_dildo", price=600)
    Item("large_dildo", price=800)
    Item("blindfold", price=200)
    Item("bondage_ropes", price=200)
    Item("handcuffs", price=200)
    Gift("butt_plug", price=200, tags=["butt_plug"], label="butt_plug", once=True, bonus_traits=["submissive"])
    Gift("slave_collar", price=100, label="collar", love_bonus=2, once=True, bonus_traits=["submissive"])
    Gift("cosplay_outfit", price=500, label="cosplay", love_bonus=2, once=True, bonus_traits=["submissive"])

    Room(**{
    "name": "sexshop",
    "exits": ["map"],
    "display_name": "Sex shop",
    "hours": (20, 2),
    "conditions": [
        IsHour(20, 2),
        ],
    "music": "music/roa_music/can_you_hear_me.ogg",
    "outfit": "casual",
    "inventory": (
        "anal_beads",
        "vibrator",
        "dildo",
        "large_dildo",
        "double_dildo",
        "blindfold",
        "bondage_ropes",
        "handcuffs",
        "box_of_condoms",
        "butt_plug",
        "slave_collar",
        "cosplay_outfit",
        ),
    })

    Activity(**{
    "name": "sexshop_shop",
    "duration": 0,
    "rooms": "sexshop",
    "display_name": "Shop",
    "icon": "shop",
    "label": "sexshop_shop",
    })

    Activity(**{
    "name": "work_sexshop",
    "label": "work_sexshop",
    "money_gain": {"attributes": ["charm"], "bonus": (5,)},
    "duration": 4,
    "rooms": "sexshop",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_night", "sexshop"),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })

label work_sexshop:
    show chibi sexshop
    "I'm gonna be honest, I like selling dildos."
    hide chibi
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    return

label sexshop_shop:
    $ Room.find("sexshop").shop("reona casual" if reona.present else None)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
