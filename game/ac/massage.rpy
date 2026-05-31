init python:
    InteractActivity(**{
    "name": "massage",
    "display_name": "Offer a massage",
    "conditions": [
        HasSkill("massage"),
        ActiveTarget(),
        ],
    "icon": "massage",
    "label": "massage",
    "once_day": "ACTIVE",
    })

label massage:
    call expression f"{active_girl.id}_greet" from _call_expression_154
    $ renpy.show(active_girl.id)
    if renpy.has_label(f"{active_girl.id}_massage_activity_{hero.gender}"):
        call expression f"{active_girl.id}_massage_activity_{hero.gender}" from _call_expression_118
    else:
        if renpy.has_label(f"{active_girl.id}_massage_intro_{hero.gender}"):
            call expression f"{active_girl.id}_massage_intro_{hero.gender}" from _call_expression_121
        else:
            "I massage [active_girl.name]."
        if hero.fitness + hero.charm >= active_girl.love:
            $ renpy.show(f"{active_girl.id} happy")
            if renpy.has_label(f"{active_girl.id}_massage_accept_{hero.gender}"):
                call expression f"{active_girl.id}_massage_accept_{hero.gender}" from _call_expression_122
            $ gain = 1
            if "dominant" in active_girl.traits:
                $ gain += 1
            if "princess" in active_girl.traits:
                $ gain += 1
            $ active_girl.love += gain
        else:
            $ renpy.show(f"{active_girl.id} annoyed")
            if renpy.has_label(f"{active_girl.id}_massage_refuse_{hero.gender}"):
                call expression f"{active_girl.id}_massage_refuse_{hero.gender}" from _call_expression_123
        if active_girl.sub >= 50 or active_girl.sub < 0:
            $ active_girl.sub -= 1
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
