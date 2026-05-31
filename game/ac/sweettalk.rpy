init python:
    InteractActivity(**{
    "name": "sweet_talk",
    "display_name": "Compliment",
    "fun": 1,
    "label": "sweet_talk",
    "conditions": [
        HeroTarget(
            Or(
                IsGender("male"),
                MaxStat("morality", 75)
                )
            ),
        ActiveTarget(
            Not(IsActivity("sleep")),
            IsFlag("breakup", False),
            IsFlag("nosweettalk", False),
            ),
        ],
    "duration": 0,
    "icon": "compliment",
    "once_day": "ACTIVE",
    })

label sweet_talk:
    call expression f"{active_girl.id}_greet" from _call_expression_24
    $ renpy.show(active_girl.id)
    $ res = randint(1, 100)
    if res <= 50 + hero.charm:
        if renpy.has_label(f"{active_girl.id}_good_sweet_talk_{hero.gender}"):
            call expression f"{active_girl.id}_good_sweet_talk_{hero.gender}" from _call_expression_167
        else:
            call expression f"good_pickup_lines_{hero.gender}" pass (active_girl.is_male) from _call_expression_182
            $ result = randchoice(_return)
            while result:
                $ line = result.pop(0)
                if line[0] == "mc":
                    call expression f"say_sentence_{hero.gender}" pass (sentence=line[1].replace("[girlname]", active_girl.name)) from _call_expression_179
                elif line[0] == "game":
                    $ renpy.say("", line[1].replace("[girlname]", active_girl.name))
                else:
                    $ active_girl.say(line[1].replace("[girlname]", active_girl.name))
        $ active_girl.love += 2
        if active_girl.is_female and active_girl.lesbian > MAX_LES_GUY_DATE and hero.is_male:
            $ active_girl.lesbian -= 1
        elif active_girl.is_female and active_girl.lesbian < MIN_LES_GIRL_DATE and hero.is_female:
            $ active_girl.lesbian += 1
    elif res <= 80 + hero.charm:
        call expression f"sweet_talk_dialogues_1_{hero.gender}" from _call_expression_180
    else:
        if renpy.has_label(f"{active_girl.id}_bad_sweet_talk_{hero.gender}"):
            call expression f"{active_girl.id}_bad_sweet_talk_{hero.gender}" from _call_expression_181
        else:
            call expression f"bad_pickup_lines_{hero.gender}" pass (active_girl.is_male) from _call_expression_492
            $ result = randchoice(_return)
            while result:
                $ line = result.pop(0)
                if line[0] == "mc":
                    call expression f"say_sentence_{hero.gender}" pass (sentence=line[1].replace("[girlname]", active_girl.name)) from _call_expression_183
                elif line[0] == "game":
                    $ renpy.say("", line[1].replace("[girlname]", active_girl.name))
                else:
                    $ active_girl.say(line[1].replace("[girlname]", active_girl.name))
        call expression f"sweet_talk_dialogues_2_{hero.gender}" from _call_expression_184
        $ active_girl.love -= 1
    if hero.is_female and hero.morality >= 50:
        $ hero.morality -= 1
    $ active_girl.set_flag("interact", 1, 1, "+")
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
