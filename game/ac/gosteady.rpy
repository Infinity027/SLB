init python:
    InteractActivity(**{
    "name": "gosteady",
    "display_name": "Go steady",
    "icon": "gosteady",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            ),
        ActiveTarget(
            Not(IsActivity("sleep")),
            IsFlag("engagedmike", False),
            IsFlag("girlfriend", False),
            MinStat("love", 120),
            MinStat("sexperience", 1),
            ),
        ],
    "label": "go_steady",
    })

label go_steady:
    call expression f"{active_girl.id}_greet" from _call_expression_60
    $ renpy.show(active_girl.id)
    if renpy.has_label(f"{active_girl.id}_go_steady_intro_{hero.gender}"):
        call expression f"{active_girl.id}_go_steady_intro_{hero.gender}" from _call_expression_75
    else:
        call expression f"go_steady_dialogues_1_{hero.gender}" from _call_expression_89
    if active_girl.love >= 150:
        $ renpy.show(f"{active_girl.id} happy")
        if renpy.has_label(f"{active_girl.id}_go_steady_yes_{hero.gender}"):
            call expression f"{active_girl.id}_go_steady_yes_{hero.gender}" from _call_expression_91
        else:
            active_girl.say "Of course I want that!"
        $ active_girl.love += 10
        if active_girl.is_male:
            $ active_girl.set_boyfriend()
        else:
            $ active_girl.set_girlfriend()
        $ active_girl.flags.nobreakup = False
    else:
        $ renpy.show(f"{active_girl.id} annoyed")
        if renpy.has_label(f"{active_girl.id}_go_steady_no_{hero.gender}"):
            call expression f"{active_girl.id}_go_steady_no_{hero.gender}" from _call_expression_93
        else:
            active_girl.say "No thank you..."
        $ active_girl.love -= 10
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
