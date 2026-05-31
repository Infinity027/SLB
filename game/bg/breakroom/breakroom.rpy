init python:
    Room(**{
    "name": "breakroom",
    "hours": (8, 20),
    "conditions": [
        IsDayOfWeek("123456"),
        IsHour(8, 20),
        ],
    "display_name": "Breakroom",
    "exits": ["map", "personal","ceo", "alettaoffice", "office"],
    "music": "music/roa_music/fly_high.ogg",
    "outfit": "work",
    "tags": ["work"],
    })

    Activity(**{
    "name": "eat_a_snack",
    "label": "eat_a_snack",
    "duration": 0,
    "hunger": 2,
    "money_cost": 5,
    "rooms": "breakroom",
    "conditions": [
        HeroTarget(MinStat("hunger", 0)),
        ],
    "display_name": "Eat a snack",
    "icon": "hotdog",
    "once_day": True,
    })

    Activity(**{
    "name": "coffee_break",
    "fun": 1,
    "energy": 1,
    "duration": 0,
    "rooms": "breakroom",
    "conditions": [
        HeroTarget(
            MinStat("energy", 0),
            MinStat("hunger", 0),
            MinStat("grooming", 0),
            MinStat("fun", 0),
            IsFlag("hasworked"),
            IsFlag("suspended", False),
            IsFlag("coffee", False),
            ),
        ],
    "display_name": "Take a coffee break",
    "icon": "coffee",
    "label": "coffee_break",
    "once_day": True,
    })

label eat_a_snack:
    show chibi hotdog
    "I eat a snack."
    return

label coffee_break:
    scene bg breakroom
    $ coffee_girls = [
        p for p in ['aletta', 'audrey', 'lavish', 'shiori', 'cassidy']
        if Person.is_not_hidden(p) and Room.has_tag(Person.find(p).room, "work")
    ]
    if coffee_girls and hero.charm >= 20:
        $ g = randchoice(coffee_girls)
        if g == "cassidy":
            show cassidy casual
            call expression cassidy.get_chat from _call_expression_coffee_break_cassidy
            hide cassidy casual
        else:
            $ renpy.show(g + " work")
            call expression Person.find(g).get_chat from _call_expression_coffee_break
            $ renpy.hide(g + " work")
    else:
        show chibi coffeebreak
        "I take a coffee break..."
    $ game.flags.coffee = TemporaryFlag(True, "day")
    hide bg
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
