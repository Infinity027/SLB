init python:
    InteractActivity(**{
    "name": "breakup_her",
    "display_name": "Break up with her",
    "label": "break_up",
    "duration": 0,
    "conditions": [
        ActiveTarget(
            Not(IsActivity("sleep")),
            IsFlag("breakup", False),
            IsFlag("friendzone", False),
            IsFlag("nobreakup", False),
            IsGender("female"),
            Or(
                IsFlag("girlfriend"),
                IsFlag("engagedmike"),
                IsFlag("engagedmc"),
                ),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "breakup",
    })

    InteractActivity(**{
    "name": "breakup_him",
    "display_name": "Break up with him",
    "label": "break_up",
    "duration": 0,
    "conditions": [
        ActiveTarget(
            Not(IsActivity("sleep")),
            IsFlag("breakup", False),
            IsFlag("friendzone", False),
            IsFlag("nobreakup", False),
            IsGender("male"),
            Or(
                IsFlag("boyfriend"),
                IsFlag("engagedmike"),
                IsFlag("engagedmc"),
                ),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "breakup",
    })

    InteractActivity(**{
    "name": "friendzone_her",
    "display_name": "Friendzone her",
    "label": "friendzone",
    "duration": 0,
    "conditions": [
        ActiveTarget(
            Not(IsActivity("sleep")),
            MinStat("love", 25),
            IsFlag("breakup", False),
            IsFlag("friendzone", False),
            IsFlag("nobreakup", False),
            IsGender("female")
            ),
        InvalidActivities("breakup_him", "breakup_her"),
        ],
    "once_day": "ACTIVE",
    "icon": "breakup",
    })

    InteractActivity(**{
    "name": "friendzone_him",
    "display_name": "Friendzone him",
    "label": "friendzone",
    "duration": 0,
    "conditions": [
        ActiveTarget(
            Not(IsActivity("sleep")),
            MinStat("love", 25),
            IsFlag("breakup", False),
            IsFlag("friendzone", False),
            IsFlag("nobreakup", False),
            IsGender("male")
            ),
        InvalidActivities("breakup_him", "breakup_her"),
        ],
    "once_day": "ACTIVE",
    "icon": "breakup",
    })

label break_up:
    call expression f"{active_girl.id}_greet" from _call_expression_58
    $ renpy.show(active_girl.id)
    if renpy.has_label(f"{active_girl.id}_breakup_{hero.gender}"):
        call expression f"{active_girl.id}_breakup_{hero.gender}" from _call_expression_59
        if _return == "denied":
            return
    else:
        if active_girl.love >= 100:
            if active_girl.is_girlfriend:
                call expression f"break_up_dialogues_1_{hero.gender}" from _call_expression_45
            else:
                call expression f"break_up_dialogues_2_{hero.gender}" from _call_expression_46
            $ renpy.show(f"{active_girl.id} sad")
            call expression f"break_up_dialogues_3_{hero.gender}" from _call_expression_47
        else:
            call expression f"break_up_dialogues_4_{hero.gender}" from _call_expression_48
    $ active_girl.breakup()
    $ active_girl.flags.breakupDelay = TemporaryFlag(True, 3)
    $ active_girl.collared = False
    $ active_girl.status = YAML[active_girl.id]["status"]
    $ active_girl.flags.giftslave_collar = False
    $ renpy.hide(active_girl.id)
    return

label friendzone:
    call expression f"{active_girl.id}_greet" from _call_expression_168
    $ renpy.show(active_girl.id)
    if active_girl.love >= 100:
        call expression f"friendzone_dialogues_1_{hero.gender}" from _call_expression_49
    else:
        call expression f"friendzone_dialogues_2_{hero.gender}" from _call_expression_51
    $ active_girl.friendzone()
    $ active_girl.flags.breakupDelay = TemporaryFlag(True, 3)
    $ active_girl.collared = False
    $ active_girl.status = YAML[active_girl.id]["status"]
    $ active_girl.flags.giftslave_collar = False
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
