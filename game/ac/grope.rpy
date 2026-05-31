init python:
    InteractActivity(**{
    "name": "grope",
    "display_name": "Cop a feel",
    "duration": 0,
    "icon": "caressboobs",
    "conditions": [
        HeroTarget(
            Or(
                IsGender("male"),
                MaxStat("morality", 25)
                ),
            ),
        ActiveTarget(
            Not(IsActivity("sleep")),
            IsGender("female"),
            MinStat("love", 10),
            ),
        ],
    "label": "grope",
    "once_day": "ACTIVE",
    })

label grope:
    call expression f"{active_girl.id}_greet" from _call_expression_94
    $ renpy.hide(active_girl.id)
    show expression f"{active_girl.id} close grope" at truecenter
    if renpy.has_label(f"{active_girl.id}_grope_{hero.gender}"):
        call expression f"{active_girl.id}_grope_{hero.gender}" from _call_expression_97
    else:
        if renpy.has_label(f"{active_girl.id}_grope_intro_{hero.gender}"):
            call expression f"{active_girl.id}_grope_intro_{hero.gender}" from _call_expression_101
        else:
            "I grope [active_girl.name]'s boobs."
        if (active_girl.traits and {"innocent", "dominant"} & active_girl.traits) or active_girl.love < 25 or active_girl.sub < 25:
            show expression f"{active_girl.id} close annoyed"
            $ active_girl.love -= 2
            if renpy.has_label(f"{active_girl.id}_grope_annoyed_{hero.gender}"):
                call expression f"{active_girl.id}_grope_annoyed_{hero.gender}" from _call_expression_102
            else:
                "She does not seem to enjoy it..."
        else:
            if active_girl.traits and "slutty" in active_girl.traits:
                $ active_girl.love += 2
            else:
                $ active_girl.love += 1
            if active_girl.sub < 50:
                $ active_girl.sub += 1
            if renpy.has_label(f"{active_girl.id}_grope_happy_{hero.gender}"):
                call expression f"{active_girl.id}_grope_happy_{hero.gender}" from _call_expression_103
            else:
                "She seems to enjoy it!"
    if hero.is_female and hero.morality >= 0:
        $ hero.morality -= 1
    $ renpy.hide(active_girl.id)
    call check_cheated ("groping") from _grope_check_cheat
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
