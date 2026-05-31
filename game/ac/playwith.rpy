init python:
    InteractActivity(**{
    "name": "play_with",
    "duration": 2,
    "fun": 2,
    "money_cost": 50,
    "conditions": [
        HeroTarget(
            IsRoom("arcade"),
            MinStat("energy", 2),
            MinStat("hunger", 3),
            MinStat("grooming", 3),
            MinStat("fun", 1),
            ),
        ActiveTarget(MinStat("love", 20)),
        ],
    "display_name": "Play a game together",
    "icon": "playarcade",
    "label": "play_with",
    })

label play_with:
    $ active_girl.set_flag("interact", 1, 1, "+")
    call expression f"{active_girl.id}_greet" from _call_expression_173
    $ renpy.show(active_girl.id)
    if renpy.has_label(f"{active_girl.id}_play_with_replace_{hero.gender}"):
        call expression f"{active_girl.id}_play_with_replace_{hero.gender}" from _call_expression_174
    else:
        call expression f"play_with_dialogues_1_{hero.gender}" from _call_expression_129
        if hero.fitness >= 40 - active_girl.love:
            active_girl.say "Sure, why not?"
            if renpy.has_label(f"{active_girl.id}_play_with_{hero.gender}"):
                call expression f"{active_girl.id}_play_with_{hero.gender}" from _call_expression_175
            else:
                "I play a game with [active_girl.name]."
            $ bonus = 1
            $ sub_bonus = 0
            if hero.knowledge * 2 >= active_girl.love:
                $ bonus += 1
            if hero.has_skill("video_games") or hero.knowledge >= active_girl.sub:
                $ sub_bonus += 1
            if "geek" in active_girl.traits:
                $ bonus += 1
            if "playful" in active_girl.traits:
                $ bonus += 1
            if "not_geek" in active_girl.traits:
                $ bonus -= 1
            if "not_playful" in active_girl.traits:
                $ bonus -= 1
            $ active_girl.love += bonus
            $ active_girl.sub += sub_bonus
        else:
            active_girl.say "Sorry, I don't feel like it."
            $ hero.cancel_activity()
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
