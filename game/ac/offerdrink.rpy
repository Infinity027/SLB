init python:
    InteractActivity(**{
    "name": "offer_a_drink",
    "money_cost": 10,
    "duration": 0,
    "conditions": [
        IsHour(19, 5),
        HeroTarget(
            Or(
                IsRoom("punkbar", "nightclub", "nightclubbar", "stripclub", "date_pub", "lounge", "date_nightclub", "vip", "date_stripclub"),
                HasRoomTag("pub"),
               ),
            MinStat("energy", 3),
            MinStat("hunger", 0),
            MinStat("grooming", 3),
            MinStat("fun", 3),
            Or(
                IsGender("male"),
                MaxStat("morality", 50)
                ),
            ),
        ActiveTarget(),
        ],
    "icon": "buydrink",
    "display_name": "Offer a drink",
    "label": "offer_a_drink",
    "once_hour": "ACTIVE",
    })

label offer_a_drink:
    call expression f"{active_girl.id}_greet" from _call_expression_37
    $ renpy.show(active_girl.id)
    if renpy.has_label(f"{active_girl.id}_offer_a_drink_{hero.gender}"):
        call expression f"{active_girl.id}_offer_a_drink_{hero.gender}" from _call_expression_38
    else:
        call expression f"offer_a_drink_dialogues_1_{hero.gender}" from _call_expression_124
        if active_girl.is_visibly_pregnant:
            $ renpy.show(f"{active_girl.id} angry")
            $ active_girl.love -= 10
            active_girl.say "Are you serious?!?"
            active_girl.say "I can't drink when I'm pregnant!"
            active_girl.say "What are you thinking?!?"
            $ hero.cancel_activity()
        elif (hero.charm >= 60 - active_girl.love and active_girl.flags.drinks < 2) or date_girl == active_girl:
            active_girl.say "Sure!"
            $ renpy.hide(active_girl.id)
            show expression f"drink {active_girl.id}"
            call expression active_girl.get_chat from _call_expression_39
            if active_girl.love <= 25:
                $ active_girl.love += 1
            elif date_girl == active_girl and game.active_date:
                $ game.active_date.score += 5
            hide expression f"drink {active_girl.id}"
            $ active_girl.set_flag("drinks", 1, "day", mod="+")
            if hero.is_female and hero.morality >= -25:
                $ hero.morality -= 1
        else:
            active_girl.say "Sorry, I don't feel like drinking."
            $ hero.cancel_activity()
    $ active_girl.set_flag("interact", 1, 1, "+")
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
