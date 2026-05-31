label date_stay_coffee_female:
    if renpy.has_label(f"{date_girl.id}_ask_fuck_date_{hero.gender}"):
        call expression f"{date_girl.id}_ask_fuck_date_{hero.gender}" from _call_expression_525
    else:
        call date_ask_fuck_date_female from _call_date_ask_fuck_date_female
    if _return:
        $ renpy.hide(date_girl.id)
        call expression f"{date_girl.id}_fuck_date_{hero.gender}" pass (_return) from _call_expression_403
    return


label date_ask_fuck_date_female:
    if date.score >= 80:
        $ date_girl.flags.datenumber += 1
    if renpy.has_label(f"{date_girl.id}_fuck_date_{hero.gender}") and (
            date.score >= (100 - date_girl.flags.drinks * 5) or
            date_girl.love >= 150 or
            date_girl.sexperience):
        if renpy.has_label(f"{date_girl.id}_ask_hot_coffee_{hero.gender}"):
            call expression f"{date_girl.id}_ask_hot_coffee_{hero.gender}" from _call_expression_535
        elif date_girl.id in ["mike", "sasha"]:
            date_girl.say "What do you say we end this at home?"
        else:
            date_girl.say "What do you say we end this at your place?"
        menu:
            "Yes" if hero.stamina and (not date_girl.flags.addressknown or date_girl.id not in []) and (
                    hero.morality <= -50
                    or (hero.morality <= -25 and date_girl.flags.datenumber >= 1)
                    or (hero.morality <= 0 and date_girl.flags.datenumber >= 2)
                    or (hero.morality <= 25 and date_girl.flags.datenumber >= 3)
                    or (hero.morality <= 50 and date_girl.flags.datenumber >= 4)
                    or (hero.morality <= 75 and date_girl.flags.datenumber >= 5)
                ):
                call expression f"date_ask_fuck_date_dialogues_1_{hero.gender}" from _call_expression_526
                return "hero"
            "My place" if hero.stamina and date_girl.flags.addressknown and date_girl.id in [] and (
                    hero.morality <= -50
                    or (hero.morality <= -25 and date_girl.flags.datenumber >= 1)
                    or (hero.morality <= 0 and date_girl.flags.datenumber >= 2)
                    or (hero.morality <= 25 and date_girl.flags.datenumber >= 3)
                    or (hero.morality <= 50 and date_girl.flags.datenumber >= 4)
                    or (hero.morality <= 75 and date_girl.flags.datenumber >= 5)
                ):
                call expression f"date_ask_fuck_date_dialogues_1_{hero.gender}" from _call_expression_536
                return "hero"
            "Your place" if hero.stamina and date_girl.flags.addressknown and date_girl.id in [] and (
                    hero.morality <= -50
                    or (hero.morality <= -25 and date_girl.flags.datenumber >= 1)
                    or (hero.morality <= 0 and date_girl.flags.datenumber >= 2)
                    or (hero.morality <= 25 and date_girl.flags.datenumber >= 3)
                    or (hero.morality <= 50 and date_girl.flags.datenumber >= 4)
                    or (hero.morality <= 75 and date_girl.flags.datenumber >= 5)
                ):
                call expression f"date_ask_fuck_date_dialogues_1_{hero.gender}" from _call_expression_537
                return date_girl.id
            "No" if hero.stamina:
                call expression f"date_ask_fuck_date_dialogues_2_{hero.gender}" from _call_expression_527
                $ date_girl.love -= 5
                return False
            "No. I'm exhausted." if not hero.stamina:
                "I had too much 'hot coffee' lately, I should rest."
                call expression f"date_ask_fuck_date_dialogues_3_{hero.gender}" from _call_expression_528
                $ date_girl.love -= 5
                return False
    else:
        date_girl.say "See you around."
    return False
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
