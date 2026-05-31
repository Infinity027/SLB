init python:
    InteractActivity(**{
    "name": "work_with",
    "duration": 2,
    "conditions": [
        'active_girl.id not in ["cassidy", "cherie"]',
        HeroTarget(
            IsGender("male"),
            IsRoom("office", "personal", "ceo", "alettaoffice"),
            MinStat("energy", 2),
            MinStat("hunger", 3),
            MinStat("grooming", 3),
            MinStat("fun", 1),
            IsFlag("suspended", False),
            ),
        ActiveTarget(
            MinStat("love", 20)
            ),
        ],
    "money_gain": {"attributes": ["charm", "knowledge"]},
    "display_name": "Work together",
    "icon": "work",
    "label": "work_with",
    "once_day": True,
    })

label work_with:
    $ active_girl.set_flag("interact", 1, 1, "+")
    call expression f"{active_girl.id}_greet" from _call_expression_100
    $ renpy.show(active_girl.id)
    if renpy.has_label(f"{active_girl.id}_work_with_replace"):
        call expression f"{active_girl.id}_work_with_replace" from _call_expression_112
    else:
        mike.say "[active_girl.name], do you want some help?"
        if hero.knowledge >= 40 - active_girl.love:
            active_girl.say "Sure, why not?"
            if renpy.has_label(f"{active_girl.id}_work_with"):
                call expression f"{active_girl.id}_work_with" from _call_expression_117
            else:
                scene expression f"workingwith {active_girl.id}"
                "I help out [active_girl.name] with her work."
            $ bonus = 1
            if active_girl.flags.career:
                $ active_girl.career += 5
            if hero.has_skill("work"):
                $ game.flags.worksatisfaction += 5
                $ bonus += 1
            if "workaholic" in active_girl.traits:
                $ bonus += 1
            $ active_girl.love += bonus
            $ game.flags.worksatisfaction += 5
        else:
            active_girl.say "Sorry, I don't need your help."
            $ hero.cancel_activity()
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
