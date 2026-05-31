layeredimage bg date_mall1:
    always:
        "mall1"

init -2 python:
    Room(
    **{
        "name": "date_mall1",
        "exits": ["map"],
        "display_name": "Mall",
        "hours": (14, 18),
        "conditions": [
            IsHour(14, 18),
        ],
        "music": season_music(),
        "random_music": True,
        "outfit": "casual",
        "tags": ["dateroom"],
    }
)

    Date(
    "mall1",
    display_name="Mall",
    clothes="casual",
    conditions=[ValidRooms("date_mall1")],
    love_gain=0,
)

    Activity(
    **{
        "name": "date_go_shopping",
        "icon": "shop",
        "rooms": "date_mall1",
        "conditions": [
            HeroTarget(MinStat("money", 50)),
        ],
        "display_name": "Go shopping",
        "label": "date_go_shopping",
    }
)

    Activity(
    **{
        "name": "date_steal_shit",
        "icon": "steal",
        "rooms": "date_mall1",
        "display_name": "Steal shit",
        "label": "date_steal_shit",
    }
)

    Activity(
    **{
        "name": "date_play_arcade",
        "rooms": "date_mall1",
        "fun": 2,
        "icon": "playarcade",
        "money_cost": 25,
        "display_name": "Play at the arcade",
        "label": "date_play_arcade",
        "conditions": [
            Or(
                "'fafow' not in DLCS",
                InvalidActivities("challenge_kat"),
            ),
        ],
    }
)

    Activity(
    **{
        "name": "date_piercing_shop",
        "icon": "piercing",
        "rooms": "date_mall1",
        "conditions": [
            HeroTarget(MinStat("money", 50)),
            DateTarget(MinStat("sub", 30)),
        ],
        "display_name": "Visit the piercing shop",
        "label": "date_piercing_shop",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_coffee",
        "money_cost": 20,
        "energy": 1,
        "icon": "coffee",
        "rooms": "date_mall1",
        "display_name": "Have a coffee",
        "label": "date_coffee",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_photobooth",
        "duration": 0,
        "money_cost": 5,
        "icon": "picture",
        "rooms": "date_mall1",
        "display_name": "Take a pic together",
        "label": "date_photobooth",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_bakery",
        "money_cost": 20,
        "hunger": 1,
        "icon": "pastry",
        "rooms": "date_mall1",
        "display_name": "Have a pastry",
        "label": "date_bakery",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_kart",
        "money_cost": 25,
        "icon": "solokart",
        "rooms": "date_mall1",
        "display_name": "Go karting",
        "label": "date_kart",
        "once_day": True,
    }
)


    def get_piercings_menu(piercings):
        choices = []
        
        for piercing, cost in sorted(Piercings.all_piercings.items(), key=lambda x: x[1]):
            if (
            piercing in piercings
            and not piercings[piercing].pierced
            and hero.money >= cost
        ):
                choices.append(
                (
                    "{} ({}{{image=gui/icons/icon_money.png}})".format(
                        piercing.capitalize(), cost
                    ),
                    (piercing, cost),
                )
            )
        choices.append(("Cancel", (None, 0)))
        return choices

label date_kart:
    $ date_girl.set_flag("interact", 1, 1, "+")
    call expression date_girl.id + "_greet" from _call_expression_288
    $ renpy.show(date_girl.id)
    if renpy.has_label(date_girl.id + "_kart_with"):
        call expression date_girl.id + "_kart_with" from _call_expression_289
    else:
        call expression f"date_kart_dialogues_1_{hero.gender}" from _call_expression_290
        if hero.charm >= 40 - date_girl.love:
            date_girl.say "Sure, why not?"
            "I race [active_girl.name]."
            $ game.active_date.score += 5
            $ hero.fun += 2
        else:
            date_girl.say "Sorry, I don't feel like it."
            $ hero.cancel_activity()
    $ renpy.hide(date_girl.id)
    return

label date_photobooth:
    $ renpy.hide(date_girl.id)
    $ renpy.show("photobooth " + date_girl.id, at_list=[photo_pos(randint(-5, 5))])
    "We go to a photo booth and have our pictures taken."
    hide photobooth
    $ renpy.show(date_girl.id)
    $ game.active_date.score += 5
    return

label date_steal_shit:
    $ renpy.show(date_girl.id)
    "We go and steal some stuff in various shops."
    $ bonus = 0
    if "not_rebel" in date_girl.traits:
        $ bonus -= 5
    if "rebel" not in date_girl.traits:
        $ bonus -= 5
    if "poor" not in date_girl.traits:
        $ bonus -= 5
    if "rebel" in date_girl.traits:
        $ bonus += 5
    if "poor" in date_girl.traits:
        $ bonus += 5
    $ game.active_date.score += bonus
    $ renpy.hide(date_girl.id)
    return

label date_bakery:
    scene bg bakery
    $ renpy.show(date_girl.id)
    "We go to the bakery to eat a pastry."
    call expression date_girl.get_chat from _call_expression_5
    if "gourmand" in date_girl.traits:
        $ game.active_date.score += 5
    $ renpy.hide(date_girl.id)
    return

label date_coffee:
    scene bg coffeeshop
    $ renpy.show(date_girl.id)
    "We go to the coffeeshop to have a coffee."
    call expression date_girl.get_chat from _call_expression_6
    $ renpy.hide(date_girl.id)
    return

label date_piercing_shop:
    scene bg tattooshop
    $ renpy.show(date_girl.id)
    "I take [date_girl.name] to the piercing shop."
    "What piercing should I ask her to get?"
    $ renpy.show("tattooparlor " + date_girl.id)
    $ bought_piercing = False
    label date_piercing_shop_loop:
    $ renpy.dynamic("piercing", "cost")
    $ piercing, cost = renpy.display_menu(get_piercings_menu(date_girl.piercings))
    if piercing is None:
        if bought_piercing == False:
            $ hero.cancel_activity()
        else:
            date_girl.say "Thank you [hero.name]."
        return
    call piercings_reactions (date_girl.id, piercing, piercing_state=True) from _call_piercings_reactions
    $ hero.money -= cost
    if piercing in {"ears", "nose", "navel"}:
        $ date_girl.sub += 1
    elif piercing in {"tongue", "lips", "eyebrow"}:
        $ date_girl.sub += 2
    elif piercing in {"nipples"}:
        $ date_girl.sub += 3
    elif piercing in {"clit", "dick"}:
        $ date_girl.sub += 4
    $ bought_piercing = True
    call date_piercing_shop_loop from date_piercing_shop_loop_internal
    hide tattooparlor
    return

label piercings_reactions(current_girl, chosen_piercing, piercing_state):
    $ renpy.dynamic("piercings")
    $ piercings = Person.find(current_girl).piercings
    if chosen_piercing in ["nipples"]:
        $ renpy.show("tattooparlor " + current_girl + " topless focused")
        pause 1
        $ piercings[chosen_piercing].pierced = piercing_state
        $ piercings[chosen_piercing].worn = piercing_state
        $ renpy.show("tattooparlor " + current_girl + " topless focused")
        if renpy.has_label(f"{current_girl}_piercing_nipples_reaction_{hero.gender}"):
            call expression f"{current_girl}_piercing_nipples_reaction_{hero.gender}" from _call_expression_291
        else:
            pause 2
    elif chosen_piercing in ["navel"]:
        $ renpy.show("tattooparlor " + current_girl + " notop focused belly")
        pause 1
        $ piercings[chosen_piercing].pierced = piercing_state
        $ piercings[chosen_piercing].worn = piercing_state
        $ renpy.show("tattooparlor " + current_girl + " notop focused belly")
        if renpy.has_label(f"{current_girl}_piercing_navel_reaction_{hero.gender}"):
            call expression f"{current_girl}_piercing_navel_reaction_{hero.gender}" from _call_expression_292
        else:
            pause 2
    elif chosen_piercing in ["clit", "dick"]:
        $ renpy.show("tattooparlor " + current_girl + " bottomless focused")
        pause 1
        $ piercings[chosen_piercing].pierced = piercing_state
        $ piercings[chosen_piercing].worn = piercing_state
        $ renpy.show("tattooparlor " + current_girl + " bottomless focused")
        if renpy.has_label(f"{current_girl}_piercing_clit_reaction_{hero.gender}"):
            call expression f"{current_girl}_piercing_clit_reaction_{hero.gender}" from _call_expression_293
        else:
            pause 2
    elif chosen_piercing in ["tongue", "lips"]:
        $ renpy.show("tattooparlor " + current_girl + " head focused")
        pause 1
        $ piercings[chosen_piercing].pierced = piercing_state
        $ piercings[chosen_piercing].worn = piercing_state
        $ renpy.show("tattooparlor " + current_girl + " head focused")
        if renpy.has_label(f"{current_girl}_piercing_head_reaction_{hero.gender}"):
            call expression f"{current_girl}_piercing_head_reaction_{hero.gender}" from _call_expression_294
        else:
            pause 2
    elif chosen_piercing in ["ears"]:
        $ renpy.show("tattooparlor " + current_girl + " head focused")
        pause 1
        $ piercings[chosen_piercing].pierced = piercing_state
        $ piercings[chosen_piercing].worn = piercing_state
        $ renpy.show("tattooparlor " + current_girl + " head focused")
        if renpy.has_label(f"{current_girl}_piercing_ears_reaction_{hero.gender}"):
            call expression f"{current_girl}_piercing_ears_reaction_{hero.gender}" from _call_expression_402
        else:
            pause 2
    else:
        $ renpy.show("tattooparlor " + current_girl)
        pause 1
        $ piercings[chosen_piercing].pierced = piercing_state
        $ piercings[chosen_piercing].worn = piercing_state
        $ renpy.show("tattooparlor " + current_girl)
        if renpy.has_label(f"{current_girl}_piercing_nose_reaction_{hero.gender}"):
            call expression f"{current_girl}_piercing_nose_reaction_{hero.gender}" from _call_expression_295
        else:
            pause 2
    scene bg black
    $ renpy.show("tattooparlor " + current_girl)
    return

label date_play_arcade:
    scene bg arcade
    $ renpy.show(date_girl.id)
    "I take [date_girl.name] to the arcade."
    $ d = 0
    if "geek" in date_girl.traits:
        $ d += 1
    if "playful" in date_girl.traits:
        $ d += 1
    if "not_geek" in date_girl.traits:
        $ d -= 1
    if "not_playful" in date_girl.traits:
        $ d -= 1
    $ game.active_date.score += d * 5
    if renpy.has_label(f"{date_girl.id}_date_play_arcade_intro_{hero.gender}"):
        call expression f"{date_girl.id}_date_play_arcade_intro_{hero.gender}" from _call_expression_296
    else:
        "We played some games."
    $ renpy.hide(date_girl.id)
    show expression "game arcade " + date_girl.id
    if hero.has_skill("video_games") or hero.knowledge >= date_girl.sub:
        if renpy.has_label(f"{date_girl.id}_date_play_arcade_win_{hero.gender}"):
            call expression f"{date_girl.id}_date_play_arcade_win_{hero.gender}" from _call_expression_297
        else:
            "I won!"
        $ date_girl.sub += 2
    else:
        if renpy.has_label(f"{date_girl.id}_date_play_arcade_lose_{hero.gender}"):
            call expression f"{date_girl.id}_date_play_arcade_lose_{hero.gender}" from _call_expression_298
        else:
            "I lost..."
        $ date_girl.sub -= 2
    hide expression "game arcade " + date_girl.id
    return

label date_go_shopping:
    $ renpy.show(date_girl.id)
    "I take [date_girl.name] on a shopping spree."
    menu:
        "Spend 50{image=gui/icons/icon_money.png}":
            $ game.active_date.score += 5
            $ hero.money -= 50
        "Spend 100{image=gui/icons/icon_money.png}" if hero.money >= 100:
            $ game.active_date.score += 10
            $ hero.money -= 100
        "Spend 200{image=gui/icons/icon_money.png}" if hero.money >= 200:
            $ game.active_date.score += 15
            $ hero.money -= 200
        "Spend 400{image=gui/icons/icon_money.png}" if hero.money >= 400:
            $ game.active_date.score += 20
            $ hero.money -= 400
        "Spend 800{image=gui/icons/icon_money.png}" if hero.money >= 800:
            $ game.active_date.score += 25
            $ hero.money -= 800
        "Spend 1600{image=gui/icons/icon_money.png}" if hero.money >= 1600:
            $ game.active_date.score += 30
            $ hero.money -= 1600
    $ renpy.hide(date_girl.id)
    return

label date_mall1:
    $ renpy.show(date_girl.id)
    "We go to the mall."
    $ renpy.hide(date_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
