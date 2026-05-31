init python:
    InteractActivity(**{
    "name": "tickle",
    "display_name": "Tickle [active_girl.personal_pronoun]",
    "duration": 0,
    "icon": "tickle",
    "conditions": [
        HeroTarget(
            Or(
                IsGender("male"),
                MaxStat("morality", 75)
                )
            ),
        ActiveTarget(),
        ],
    "label": "tickle",
    "once_day": "ACTIVE",
    })

label tickle:
    call expression f"{active_girl.id}_greet" from _call_expression_156
    $ renpy.show(active_girl.id)
    if renpy.has_label(f"{active_girl.id}_tickle_activity"):
        call expression f"{active_girl.id}_tickle_activity" from _call_expression_157
    else:
        "I tickle [active_girl.name]."
        $ gain = 0
        if "playful" in active_girl.traits:
            $ gain += 1
        elif "not_playful" in active_girl.traits:
            $ gain -= 1
        if "dominant" in active_girl.traits:
            $ gain -= 1
        if "princess" in active_girl.traits:
            $ gain -= 1
        $ active_girl.love += gain
    if hero.is_female and hero.morality >= 50:
        $ hero.morality -= 1
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
