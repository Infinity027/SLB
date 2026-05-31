init python:
    InteractActivity(**{
    "name": "train_with",
    "energy": -1,
    "grooming": -1,
    "fitness": 2,
    "duration": 2,
    "conditions": [
        HeroTarget(
            HasRoomTag("gym"),
            MinStat("energy", 2),
            MinStat("hunger", 3),
            MinStat("grooming", 3),
            MinStat("fun", 1),
            MinStat("fitness", 20),
            IsFlag("gymmember"),
            ),
        ActiveTarget(
            MinStat("love", 20),
            IsFlag("notrain", False)
            ),
        ],
    "display_name": "Train together",
    "icon": "workout",
    "label": "train_with",
    })

label train_with:
    $ active_girl.set_flag("interact", 1, 1, "+")
    call expression f"{active_girl.id}_greet" from _call_expression_149
    $ renpy.show(active_girl.id)
    if renpy.has_label(f"{active_girl.id}_train_with_replace_{hero.gender}"):
        call expression f"{active_girl.id}_train_with_replace_{hero.gender}" from _call_expression_150
    else:
        call expression f"train_with_dialogues_1_{hero.gender}" from _call_expression_187
        if hero.fitness * 2 >= 40 - active_girl.love:
            $ hero.flags.dirty = TemporaryFlag(True, "day")
            active_girl.say "Why not."
            if renpy.has_label(f"{active_girl.id}_train_with_{hero.gender}"):
                call expression f"{active_girl.id}_train_with_{hero.gender}" from _call_expression_151
            else:
                "I work out with [active_girl.name]."
            $ bonus = 1
            $ hero.fitness += 1
            $ hero.fun += 2
            if hero.fitness >= 75:
                $ bonus += 1
            if "sporty" in active_girl.traits:
                $ bonus += 1
            $ active_girl.love += bonus
            if hero.fitness >= active_girl.sub:
                $ active_girl.sub += 1
            elif "sporty" in active_girl.traits:
                $ active_girl.sub -= 1
        else:
            active_girl.say "Sorry, I don't feel like working out with you."
            $ hero.cancel_activity()
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
