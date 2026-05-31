init python:
    InteractActivity(**{
    "name": "shop_with",
    "duration": 2,
    "fun": 2,
    "money_cost": 50,
    "conditions": [
        HeroTarget(
            IsRoom("mall1", "mall2"),
            MinStat("energy", 2),
            MinStat("hunger", 3),
            MinStat("grooming", 3),
            MinStat("fun", 1),
            ),
        ActiveTarget(MinStat("love", 20)),
        ],
    "display_name": "Go shopping together",
    "icon": "shop",
    "label": "shop_with",
    })

label shop_with:
    $ active_girl.set_flag("interact", 1, 1, "+")
    call expression f"{active_girl.id}_greet" from _call_expression_146
    $ renpy.show(active_girl.id)
    if renpy.has_label(f"{active_girl.id}_shop_with_replace_{hero.gender}"):
        call expression f"{active_girl.id}_shop_with_replace_{hero.gender}" from _call_expression_147
    else:
        call expression f"shop_with_dialogues_1_{hero.gender}" from _call_expression_130
        if hero.fitness >= 40 - active_girl.love:
            active_girl.say "Sure, why not?"
            if renpy.has_label(f"{active_girl.id}_shop_with_{hero.gender}"):
                call expression f"{active_girl.id}_shop_with_{hero.gender}" from _call_expression_148
            else:
                "I go shopping with [active_girl.name]."
            $ bonus = 1
            $ hero.fitness += 1
            if hero.charm >= 75:
                $ bonus += 1
            if "princess" in active_girl.traits:
                $ bonus += 1
            $ active_girl.love += bonus
        else:
            active_girl.say "Sorry, I don't feel like it."
            $ hero.cancel_activity()
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
