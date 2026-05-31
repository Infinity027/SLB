init python:
    InteractActivity(**{
    "name": "kiss",
    "display_name": "Kiss",
    "label": "kiss_her",
    "duration": 0,
    "icon": "kiss",
    "conditions": [
        HeroTarget(MinStat("grooming", 2)),
        ActiveTarget(
            Not(IsActivity("sleep")),
            IsFlag("nokiss", False),
            MinStat("love", 40),
            ),
        ],
    "once_day": "ACTIVE",
    })

label kiss_her:
    $ active_girl.flags.greeted = TemporaryFlag(True, "day")
    $ active_girl.set_flag("interact", 1, 1, "+")
    if renpy.has_label(f"{active_girl.id}_kiss_{hero.gender}"):
        call expression f"{active_girl.id}_kiss_{hero.gender}" from _call_expression_12
        call check_cheated ("kissing") from _call_check_cheated
    elif renpy.has_label(f"{active_girl.id}_kiss"):
        call expression f"{active_girl.id}_kiss" from _call_expression_32
        call check_cheated ("kissing") from _kiss_her
    elif active_girl.love + hero.charm < 120 and not active_girl.is_girlfriend or active_girl.flags.nokiss or not game.active_date.score >= 75:
        $ renpy.show(active_girl.id)
        "[active_girl.name] pushes me away."
        active_girl.say "Don't ever do that again."
        $ active_girl.love -= 2
        $ hero.cancel_activity()
        $ renpy.hide(active_girl.id)
    elif active_girl.love + hero.charm < 140 or game.active_date.score >= 75:
        show expression f"{active_girl.id} kiss"
        if not active_girl.flags.kiss:
            "When our lips come into contact with each other, it sends shivers down my back..."
            "The intoxicating smell of flowers and the taste of blueberry give a different vibe to that first kiss..."
            "As I look at her, I can see surprise and pleasure mixed together."
        else:
            "[active_girl.name] kisses me softly."
        $ active_girl.flags.kiss += 1
        $ active_girl.love += 1
        hide expression f"{active_girl.id} kiss"
        call check_cheated ("kissing") from _kiss_her_2
    else:
        show expression f"{active_girl.id} kiss"
        if not active_girl.flags.kiss:
            "[active_girl.name] grips my neck and sticks her wet tongue in my mouth."
            "After what feels like an eternity, we part, breathless..."
            active_girl.say "It feels like I waited for that kiss for far too long.\nI hope there's more coming my way."
            "After that line she turns around and leaves."
        else:
            "[active_girl.name] kisses me passionately."
        $ active_girl.flags.kiss += 1
        $ active_girl.love += 2
        hide expression f"{active_girl.id} kiss"
        call check_cheated ("kissing") from _kiss_her_3
    return

label check_cheated(action, cheat_npc=None):
    if cheat_npc or active_girl:
        if not cheat_npc:
            $ cheat_npc = active_girl
        $ cheat_npc = Person.find(cheat_npc)
        if not cheat_npc:
            return False
        $ cheated_girls = game.get_cheated_girls(cheat_npc)
        if cheated_girls:
            $ cheated_girl = renpy.random.choice(cheated_girls)
            if cheated_girl and renpy.has_label(f"{cheated_girl.id}_beats_{cheat_npc.id}_{hero.gender}"):
                call expression f"{cheated_girl.id}_beats_{cheat_npc.id}_{hero.gender}" from _call_expression_467
                if _return is None or _return == False:
                    call expression f"postfight_{hero.gender}" from _call_expression_468
                    return True
            if cheated_girl and renpy.has_label(cheated_girl.id + "_cheated"):
                call expression cheated_girl.id + "_cheated" pass (action, cheat_npc) from _call_expression_34
                return True
    return False
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
