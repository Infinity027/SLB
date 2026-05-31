init python:
    InteractActivity(**{
    "name": "pet",
    "display_name": "Pet her head",
    "duration": 0,
    "icon": "pettinggirl",
    "conditions": [
        HeroTarget(IsGender("male")),
        ActiveTarget(
            Not(IsActivity("sleep")),
            IsGender("female"),
            MinStat("love", 25),
            MinStat("sub", 50),
            ),
        ],
    "label": "pet",
    "once_day": "ACTIVE",
    })

label pet:
    call expression f"{active_girl.id}_greet" from _call_expression_98
    $ renpy.hide(active_girl.id)
    show expression f"{active_girl.id} close pat"
    if renpy.has_label(f"{active_girl.id}_pet_activity_{hero.gender}"):
        call expression f"{active_girl.id}_pet_activity_{hero.gender}" from _call_expression_99
    else:
        if renpy.has_label(f"{active_girl.id}_pet_intro_{hero.gender}"):
            call expression f"{active_girl.id}_pet_intro_{hero.gender}" from _call_expression_125
        else:
            "I pet [active_girl.name]'s head."
        if "dominant" in active_girl.traits:
            show expression f"{active_girl.id} close annoyed"
            if renpy.has_label(f"{active_girl.id}_pet_annoyed_{hero.gender}"):
                call expression f"{active_girl.id}_pet_annoyed_{hero.gender}" from _call_expression_126
            $ active_girl.love -= 1
        else:
            if "submissive" in active_girl.traits:
                $ active_girl.love += 1
            if active_girl.sub < 75:
                $ active_girl.sub += 1
            if renpy.has_label(f"{active_girl.id}_pet_happy_{hero.gender}"):
                call expression f"{active_girl.id}_pet_happy_{hero.gender}" from _call_expression_128
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
