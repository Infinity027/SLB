init python:
    Consumable("cake", effects=[("fun", 1), ("hunger", 1)], frequency_limit="day")
    Consumable("valentine_chocolates", effects=[("fun", 1), ("hunger", 1)], frequency_limit="day")

    InteractActivity(**{
    "name": "gift",
    "display_name": "Offer a gift",
    "label": "give_a_gift",
    "conditions": [
        HeroTarget(Not(IsRoom("jail"))),
        "hero.has_gifts",
        ActiveTarget(
            Not(IsActivity("work")),
            Or(
                MinStat("love", 40),
                And(
                    IsBirthday(),
                    MinStat("love", 20),
                    ),
                ),
            ),
        ],
    "icon": "gift",
    "once_day": "ACTIVE",
    "duration": 0,
    })

label give_a_gift(from_birthday_date=False):
    $ renpy.dynamic("result", difficulty=75, gift_reaction="neutral", has_specific_reaction=False)

    if not from_birthday_date:
        $ active_girl.set_flag("interact", 1, 1, "+")
        call expression f"{active_girl.id}_greet" from _call_expression_18

    $ renpy.show(active_girl.id, at_list=[reset, default])
    $ renpy.show(active_girl.id, at_list=[left4])
    $ result = renpy.call_screen("choose_gift")
    $ renpy.show(active_girl.id, at_list=[center])

    if result != "None" and result != "exit":
        if any([game.calendar.is_today(*active_girl.birthday), game.calendar.is_today("valentine"), game.calendar.is_today("christmas")]):
            $ difficulty -= 25
        if (hero.charm >= difficulty - active_girl.love) or from_birthday_date:
            if result.once and active_girl.flags[f"gift{result.name}"] is True:
                active_girl.say "I already have one of those."
                active_girl.say "What would I need a second one for?"
                if from_birthday_date:
                    $ renpy.show(active_girl.id, at_list=[reset, default])
                    return "done"
                $ hero.cancel_activity()
            if (hero.activity and not hero.activity.flags.canceled) or not hero.activity:
                if not from_birthday_date:
                    if game.calendar.is_today(*active_girl.birthday) and renpy.has_label(f"{active_girl.id}_birthday_gift_{hero.gender}"):
                        call expression f"{active_girl.id}_birthday_gift_{hero.gender}" from _call_expression_19
                    elif game.calendar.is_today("valentine") and renpy.has_label(f"{active_girl.id}_valentine_gift_{hero.gender}"):
                        call expression f"{active_girl.id}_valentine_gift_{hero.gender}" from _call_expression_40
                    elif game.calendar.is_today("christmas") and renpy.has_label(f"{active_girl.id}_christmas_gift_{hero.gender}"):
                        call expression f"{active_girl.id}_christmas_gift_{hero.gender}" from _call_expression_41
                if isinstance(result.label, tuple) and renpy.has_label(f"{active_girl.id}_gift_{result.label[0]}_{hero.gender}"):
                    call expression f"{active_girl.id}_gift_{result.label[0]}_{hero.gender}" pass (*result.label[1:]) from _call_expression_159
                    if from_birthday_date:
                        $ renpy.show(active_girl.id, at_list=[reset, default])
                        return "done"
                elif isinstance(result.label, basestring) and renpy.has_label(f"{active_girl.id}_gift_{result.label}_{hero.gender}"):
                    call expression f"{active_girl.id}_gift_{result.label}_{hero.gender}" from _call_expression_160
                    if from_birthday_date:
                        $ renpy.show(active_girl.id, at_list=[reset, default])
                        return "done"
                elif isinstance(result.label, basestring) and result.once and {'clothes', 'swimsuit', 'underwear'} & set(result.tags) and not renpy.has_label(f"{active_girl.id}_gift_{result.label}"):
                    "I don't think it's something I should give [active_girl.personal_pronoun]... At least not right now..."
                    if from_birthday_date:
                        $ renpy.show(active_girl.id, at_list=[reset, default])
                        return False

                    $ hero.cancel_activity()
                    $ renpy.hide(active_girl.id)
                    return
                if from_birthday_date:
                    $ renpy.show(active_girl.id, at_list=[reset, default])
                    $ gift_reaction = result.use(active_girl)
                    return gift_reaction
                if hero.activity and not hero.activity.flags.canceled:
                    $ gift_reaction = result.use(active_girl)
                    call give_a_gift_reaction (active_girl, gift_reaction) from _call_give_a_gift_reaction
        else:
            $ renpy.show(active_girl.id)
            $ hero.cancel_activity()
            active_girl.say "No thanks."
    else:
        if from_birthday_date:
            $ renpy.show(active_girl.id, at_list=[reset, default])
            return result
        $ hero.cancel_activity()
    $ renpy.hide(active_girl.id)
    return

label give_a_gift_reaction(active_npc, reaction_result):


    if reaction_result == "neutral":
        if renpy.has_label(f"{active_npc.id}_give_a_gift_reaction_neutral_{hero.gender}") and not active_npc.flags.neutral_gift_reaction:
            call expression f"{active_npc.id}_give_a_gift_reaction_neutral_{hero.gender}" from _call_expression_36
            $ active_npc.flags.neutral_gift_reaction = TemporaryFlag(True, "week")
        else:
            "[active_girl.name] seems indifferent to the gift."
    elif reaction_result:
        if renpy.has_label(f"{active_npc.id}_give_a_gift_reaction_positive_{hero.gender}") and not active_npc.flags.positive_gift_reaction:
            call expression f"{active_npc.id}_give_a_gift_reaction_positive_{hero.gender}" from _call_expression_55
            $ active_npc.flags.positive_gift_reaction = TemporaryFlag(True, "week")
        else:
            "[active_girl.name] seems to enjoy the gift."
    else:
        if renpy.has_label(f"{active_npc.id}_give_a_gift_reaction_negative_{hero.gender}") and not active_npc.flags.negative_gift_reaction:
            call expression f"{active_npc.id}_give_a_gift_reaction_negative_{hero.gender}" from _call_expression_56
            $ active_npc.flags.negative_gift_reaction = TemporaryFlag(True, "week")
        else:
            "[active_girl.name] seems to dislike the gift."
    return

label npc_give_a_gift:
    $ renpy.show(active_girl.id)
    $ active_girl.set_flag("interact", 1, 1, "+")

    if game.calendar.is_today(*hero.birthday) and active_girl.love >= 40 and renpy.has_label(f"{active_girl.id}_give_birthday_{hero.gender}"):
        call expression f"{active_girl.id}_give_birthday_{hero.gender}" from _call_expression_69
    elif game.calendar.is_today("valentine") and active_girl.love >= 100 and renpy.has_label(f"{active_girl.id}_give_valentine_{hero.gender}"):
        call expression f"{active_girl.id}_give_valentine_{hero.gender}" from _call_expression_71
    elif game.calendar.is_today("christmas") and active_girl.love >= 50 and renpy.has_label(f"{active_girl.id}_give_christmas_{hero.gender}"):
        call expression f"{active_girl.id}_give_christmas_{hero.gender}" from _call_expression_73

    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
