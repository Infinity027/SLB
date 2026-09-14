init python:
    InteractActivity(**{
    "name": "pet",
    "display_name": "Pet her head",
    "duration": 0,
    "icon": "pettinggirl",
    "conditions": [
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
    if renpy.has_label(f"{active_girl.id}_pet_activity_male"):
        call expression f"{active_girl.id}_pet_activity_male" from _call_expression_99
    else:
        if renpy.has_label(f"{active_girl.id}_pet_intro_male"):
            call expression f"{active_girl.id}_pet_intro_male" from _call_expression_125
        else:
            "I pet [active_girl.name]'s head."
        if "dominant" in active_girl.traits:
            show expression f"{active_girl.id} close annoyed"
            if renpy.has_label(f"{active_girl.id}_pet_annoyed_male"):
                call expression f"{active_girl.id}_pet_annoyed_male" from _call_expression_126
            $ active_girl.love -= 1
        else:
            if "submissive" in active_girl.traits:
                $ active_girl.love += 1
            if active_girl.sub < 75:
                $ active_girl.sub += 1
            if renpy.has_label(f"{active_girl.id}_pet_happy_male"):
                call expression f"{active_girl.id}_pet_happy_male" from _call_expression_128
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
