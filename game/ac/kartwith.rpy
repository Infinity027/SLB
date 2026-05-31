init python:
    InteractActivity(**{
    "name": "kart_with",
    "fun": 2,
    "grooming": 0,
    "money_cost": 25,
    "conditions": [
        HeroTarget(
            IsRoom("kart"),
            MinStat("energy", 2),
            MinStat("hunger", 3),
            MinStat("grooming", 3),
            MinStat("fun", 1),
            ),
        ],
    "icon": "duokart",
    "display_name": "Invite to a race",
    "label": "kart_with",
    })

label kart_with:
    $ active_girl.set_flag("interact", 1, 1, "+")
    call expression f"{active_girl.id}_greet" from _call_expression_170
    $ renpy.show(active_girl.id)
    if renpy.has_label(f"{active_girl.id}_kart_with_{hero.gender}"):
        call expression f"{active_girl.id}_kart_with_{hero.gender}" from _call_expression_171
    else:
        call expression f"kart_with_dialogues_1_{hero.gender}" from _call_expression_115
        if hero.charm >= 40 - active_girl.love:
            active_girl.say "Sure, why not?"
            "I race [active_girl.name]."
            $ active_girl.love += hero.charm // 20
            $ hero.fun += 2
        else:
            active_girl.say "Sorry, I don't feel like it."
            $ hero.cancel_activity()
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
