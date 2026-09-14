init python:
    InteractActivity(**{
    "name": "askbirthday",
    "label": "ask_birthday",
    "display_name": "Ask birthday",
    "icon": "birthday",
    "duration": 0,
    "conditions": [
        ActiveTarget(
            IsFlag("birthdayknown", False),
            MinStat("love", 5),
            ),
        ],
    "once_day": "ACTIVE",
    })

label ask_birthday:
    call expression f"{active_girl.id}_greet" from _call_expression_28
    $ renpy.show(active_girl.id)
    if renpy.has_label(f"{active_girl.id}_ask_birthday_male"):
        call expression f"{active_girl.id}_ask_birthday_male" from _call_expression_23
    else:
        call ask_birthday_dialogues_1_male from _call_expression_30
        if hero.charm < 40 - active_girl.love:
            active_girl.say "I don't think that's any of your business."
        else:
            active_girl.say "It's on the [active_girl.birthday[1]] of [active_girl.birthday[0]]."
            active_girl.say "Are you planning on getting me a gift?"
            call ask_birthday_dialogues_2_male from _call_expression_42
            $ active_girl.flags.birthdayknown = True
            $ active_girl.love += 1
    $ renpy.hide(active_girl.id)
    return
return