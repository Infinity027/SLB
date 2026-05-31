init python:
    InteractActivity(**{
    "name": "dance_with",
    "label": "dance_with",
    "display_name": "Ask to dance",
    "icon": "dance",
    "fun": 2,
    "grooming": 0,
    "conditions": [
        HeroTarget(
            IsRoom("nightclub", "nightclubbar", "date_nightclub", "vip"),
            MinStat("energy", 2),
            MinStat("hunger", 3),
            MinStat("grooming", 3),
            MinStat("fun", 1),
            Or(
                IsGender("male"),
                MaxStat("morality", 90)
                ),
            ),
        ActiveTarget(),
        ],
    })

    InteractActivity(**{
    "name": "dance_girl",
    "label": "dance_girl",
    "display_name": "Have her dance with a girl",
    "icon": "dancegirl",
    "fun": 2,
    "grooming": 0,
    "conditions": [
        HeroTarget(
            IsRoom("nightclub", "nightclubbar", "date_nightclub", "vip"),
            IsGender("male"),
            MinStat("energy", 2),
            MinStat("hunger", 3),
            MinStat("grooming", 3),
            MinStat("fun", 1),
            Or(
                IsGender("male"),
                MaxStat("morality", 90)
                ),
            ),
        ActiveTarget(
            IsGender("female"),
            MinStat("sub", 25),
            ),
        ],
    })

label dance_girl:
    $ active_girl.set_flag("interact", 1, 1, "+")
    call expression f"{active_girl.id}_greet" from _call_expression_54
    $ renpy.show(active_girl.id)
    mike.say "[active_girl.name], you should dance with that cute girl here."
    if hero.charm >= 60 - active_girl.sub or active_girl.lesbian >= 15:
        active_girl.say "Sure, why not?"
        $ active_girl.lesbian += 1
        "[active_girl.name] dances with a cute girl."
    else:
        active_girl.say "I don't think so."
        $ hero.cancel_activity()
    if hero.is_female and hero.morality >= 75:
        $ hero.morality -= 1
    $ renpy.hide(active_girl.id)
    return

label dance_with:
    $ active_girl.set_flag("interact", 1, 1, "+")
    call expression f"{active_girl.id}_greet" from _call_expression_21
    $ renpy.show(active_girl.id)
    if renpy.has_label(f"{active_girl.id}_dance_with_replace_{hero.gender}"):
        call expression f"{active_girl.id}_dance_with_replace_{hero.gender}" from _call_expression_22
    else:
        call expression f"dance_with_dialogues_1_{hero.gender}" from _call_expression_61
        if hero.charm >= 40 - active_girl.love or date_girl == active_girl:
            active_girl.say "Sure, why not?"
            $ renpy.hide(active_girl.id)
            $ renpy.show(f"dance {active_girl.id}")
            if renpy.has_label(f"{active_girl.id}_dance_with"):
                call expression f"{active_girl.id}_dance_with" from _call_expression_145
            else:
                "I dance with [active_girl.name]."
            $ bonus = 1
            if hero.has_skill("dance"):
                $ bonus += 1
            $ active_girl.love += bonus
            $ hero.fun += 2
            $ renpy.hide(f"dance {active_girl.id}")
            if hero.is_female:
                if renpy.has_label(f"{active_girl.id}_after_dance_success_with_{hero.gender}") and (hero.has_skill("dance") or hero.fitness >= 50):
                    call expression f"{active_girl.id}_after_dance_success_with_{hero.gender}" from _call_expression_83
                elif renpy.has_label(f"{active_girl.id}_after_dance_failure_with_{hero.gender}"):
                    call expression f"{active_girl.id}_after_dance_failure_with_{hero.gender}" from _call_expression_169
        else:
            active_girl.say "Sorry, I don't feel like dancing."
            $ hero.cancel_activity()
    if hero.is_female and hero.morality >= 75:
        $ hero.morality -= 1
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
