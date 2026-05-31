init python:
    InteractActivity(**{
    "name": "study_with",
    "duration": 2,
    "conditions": [
        HeroTarget(
            IsRoom("classroom"),
            MinStat("energy", 2),
            MinStat("hunger", 3),
            MinStat("grooming", 3),
            MinStat("fun", 1),
            MinStat("knowledge", 20),
            ),
        ActiveTarget(MinStat("love", 20)),
        ],
    "display_name": "Study together",
    "icon": "study",
    "label": "study_with",
    })

label study_with:
    $ active_girl.set_flag("interact", 1, 1, "+")
    call expression f"{active_girl.id}_greet" from _call_expression_85
    $ renpy.show(active_girl.id)
    call expression f"study_with_dialogues_1_{hero.gender}" from _call_expression_164
    if hero.knowledge * 2 >= 40 - active_girl.love:
        if renpy.has_label(f"{active_girl.id}_study_with_intro_{hero.gender}"):
            show expression f"studywith {active_girl.id}"
            call expression f"{active_girl.id}_study_with_intro_{hero.gender}" from _call_expression_95
        else:
            active_girl.say "In fact, yes!"
            $ renpy.hide(active_girl.id)
            show expression f"studywith {active_girl.id}"
            "I help out [active_girl.name] with her studies."
        $ bonus = 1
        $ hero.knowledge += 1
        if hero.knowledge * 2 >= active_girl.love:
            $ bonus += 1
            if "bookworm" in active_girl.traits:
                $ bonus += 1
            $ active_girl.love += bonus
            if renpy.has_label(f"{active_girl.id}_study_with_success_{hero.gender}"):
                call expression f"{active_girl.id}_study_with_success_{hero.gender}" from _call_expression_165
            if hero.knowledge >= active_girl.sub:
                $ active_girl.sub += 1
            elif "bookworm" in active_girl.traits:
                $ active_girl.sub -= 1
        elif renpy.has_label(f"{active_girl.id}_study_with_failure_{hero.gender}"):
            call expression f"{active_girl.id}_study_with_failure_{hero.gender}" from _call_expression_166
        hide expression f"studywith {active_girl.id}"
    else:
        active_girl.say "I'm fine."
        $ hero.cancel_activity()
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
