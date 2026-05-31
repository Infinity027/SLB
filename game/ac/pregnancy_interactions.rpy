init python:
    
    InteractActivity(**{
        "name": "belly_interactions_male",
        "display_name": "About your belly",
        "label": "belly_interactions_male",
        "conditions": [
            HeroTarget(
                IsGender("male"),

                ),
            ActiveTarget(
                IsActive(),
                MinStat("love", 120),
                Not(IsActivity("sleep")),
                IsVisiblyPregnant(),
                "active_girl not in [cherie, claire, kiara]",
                ),
            ],
        "icon": "belly",
        "priority": 600,
        "do_once": False,
        "once_day": "ACTIVE",
        "duration": 0,
        })

label belly_interactions_male:
    $ renpy.show(f"{active_girl.id} normal", at_list=[center, zoomAt(1.5, (640, 1040))])
    menu:
        "Kiss her belly":
            call expression f"{active_girl.id}_belly_kiss_male" from _call_expression_520
        "Caress her belly":
            call expression f"{active_girl.id}_belly_caress_male" from _call_expression_521
        "Listen to the baby":
            call expression f"{active_girl.id}_belly_listen_male" from _call_expression_522
        "Never mind":
            $ hero.cancel_activity()
            return
    $ active_girl.set_flag("interact", 1, 1, "+")
    $ active_girl.love += 2
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
