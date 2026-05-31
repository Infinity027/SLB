init python:
    InteractActivity(**{
    "name": "asknumber",
    "label": "ask_number",
    "display_name": "Ask number",
    "icon": "number",
    "duration": 0,
    "conditions": [
        ActiveTarget(
            Not(ContactKnown())
            ),
        ],
    "once_day": "ACTIVE",
    })

label ask_number:
    call expression f"{active_girl.id}_greet" from _call_expression_17
    $ renpy.show(active_girl.id)
    if renpy.has_label(f"{active_girl.id}_ask_phone_{hero.gender}"):
        call expression f"{active_girl.id}_ask_phone_{hero.gender}" from _call_expression_43
    else:
        call expression f"ask_number_dialogues_1_{hero.gender}" from _call_expression_44
        if hero.charm < 20 - active_girl.love:
            active_girl.say "I don't think so."
        else:
            $ hero.smartphone_contacts.append(active_girl.id)
            active_girl.say "Sure."
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
