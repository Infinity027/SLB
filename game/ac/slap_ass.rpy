init python:
    InteractActivity(**{
    "name": "slap",
    "display_name": "Slap ass",
    "duration": 0,
    "icon": "slap",
    "conditions": [
        ActiveTarget(
            Not(IsActivity("sleep")),
            IsFlag("breakup", False),
            IsFlag("noslap", False),
            ),
        HeroTarget(
            Or(
                IsGender("male"),
                MaxStat("morality", 50)
                ),
            ),
        ],
    "label": "slap",
    "once_day": "ACTIVE",
    })

label slap:
    call expression f"{active_girl.id}_greet" from _call_expression_131
    $ renpy.hide(active_girl.id)
    $ renpy.show(f"slap {active_girl.id} happy waiting")
    if renpy.has_label(f"{active_girl.id}_slap_ass_intro_{hero.gender}"):
        call expression f"{active_girl.id}_slap_ass_intro_{hero.gender}" from _call_expression_133
    else:
        "I slap [active_girl.name] on the ass."
    if active_girl.sub >= 10 - active_girl.flags.slapassmod:
        $ renpy.show(f"slap {active_girl.id} slapping")
        if active_girl.sub < 15 + active_girl.flags.slapassmod:
            $ active_girl.sub += 1
        elif active_girl.sub < 25 + active_girl.flags.slapassmod:
            $ active_girl.sub += randint(0, 1)
        elif active_girl.sub < 35 + active_girl.flags.slapassmod:
            $ active_girl.sub += randchoice([0, 0, 1])
        elif active_girl.sub < 45 + active_girl.flags.slapassmod:
            $ active_girl.sub += randchoice([0, 0, 0, 1])
        elif active_girl.sub < 50 + active_girl.flags.slapassmod:
            $ active_girl.sub += randchoice([0, 0, 0, 0, 1])
        if renpy.has_label(f"{active_girl.id}_slap_ass_happy_{hero.gender}"):
            call expression f"{active_girl.id}_slap_ass_happy_{hero.gender}" from _call_expression_134
        else:

            "She smiles and blushes..."
    else:
        $ renpy.show(f"slap {active_girl.id} angry slapping")
        $ active_girl.love -= 1
        $ active_girl.sub -= 1
        if renpy.has_label(f"{active_girl.id}_slap_ass_angry_{hero.gender}"):
            call expression f"{active_girl.id}_slap_ass_angry_{hero.gender}" from _call_expression_136
        else:
            active_girl.say "What are you doing?"
    if hero.is_female and hero.morality >= 25:
        $ hero.morality -= 1
    hide slap
    $ renpy.show(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
