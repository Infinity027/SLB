init python:
    Room(**{
    "name": "tattooshop",
    "hours": (9, 18),
    "conditions": [
        IsHour(9, 18),
        HeroTarget(IsGender("female"))
        ],
    "display_name": "Piercings Shop",
    "exits": ["mall1", "bakery", "bookstore", "clothesshop", "arcade", "mallmap"],
    "outfit": "casual",
    "tags": ["mall_southside"],
    })

    Activity(**{
    "name": "piercing_shop_mc",
    "icon": "piercing",
    "rooms": "tattooshop",
    "conditions": [
        HeroTarget(IsGender("female"),
            MinStat("money", 50)),
        ],
    "display_name": "Buy a new piercing",
    "label": "piercing_shop_mc",
    "once_day": True,
    })



label piercing_shop_mc:
    scene bg tattooshop
    "What piercing should I buy?"
    show tattooparlormc
    python:
        piercings = hero.piercings
        while True:
            choices = []
            
            for piercing, cost in sorted(Piercings.all_piercings.items(), key=lambda x: x[1]):
                if piercing in piercings and not piercings[piercing].pierced and hero.money >= cost:
                    choices.append(("{} ({}{{image=gui/icons/icon_money.png}})".format(piercing.capitalize(), cost), (piercing, cost)))
            choices.append(("Cancel", (None, 0)))
            piercing, cost = renpy.display_menu(choices)
            if piercing is None:
                break
            hero.money -= cost
            renpy.call("piercings_reactions_mc", piercing, True, from_current=True)
    "That's enough for today."
    hide tattooparlormc
    return


label piercings_reactions_mc(chosen_piercing, piercing_state):
    if chosen_piercing in ["nipples"]:
        show tattooparlormc topless focused
        pause 1
        $ piercings[chosen_piercing].pierced = piercing_state
        $ piercings[chosen_piercing].worn = piercing_state
        $ renpy.show("tattooparlormc topless focused")
        if renpy.has_label(f"mc_piercing_nipples_reaction_{hero.gender}"):
            call expression f"mc_piercing_nipples_reaction_{hero.gender}" from _call_expression_381
        else:
            pause 2
    elif chosen_piercing in ["navel"]:
        $ renpy.show("tattooparlormc notop focused belly")
        pause 1
        $ piercings[chosen_piercing].pierced = piercing_state
        $ piercings[chosen_piercing].worn = piercing_state
        $ renpy.show("tattooparlormc notop focused belly")
        if renpy.has_label(f"mc_piercing_navel_reaction_{hero.gender}"):
            call expression f"mc_piercing_navel_reaction_{hero.gender}" from _call_expression_382
        else:
            pause 2
    elif chosen_piercing in ["clit"]:
        $ renpy.show("tattooparlormc bottomless focused")
        pause 1
        $ piercings[chosen_piercing].pierced = piercing_state
        $ piercings[chosen_piercing].worn = piercing_state
        $ renpy.show("tattooparlormc bottomless focused")
        if renpy.has_label(f"mc_piercing_clit_reaction_{hero.gender}"):
            call expression f"mc_piercing_clit_reaction_{hero.gender}" from _call_expression_383
        else:
            pause 2
    elif chosen_piercing in ["tongue", "lips"]:
        $ renpy.show("tattooparlormc head focused")
        pause 1
        $ piercings[chosen_piercing].pierced = piercing_state
        $ piercings[chosen_piercing].worn = piercing_state
        $ renpy.show("tattooparlormc head focused")
        if renpy.has_label(f"mc_piercing_head_reaction_{hero.gender}"):
            call expression f"mc_piercing_head_reaction_{hero.gender}" from _call_expression_384
        else:
            pause 2
    else:
        $ renpy.show("tattooparlormc ")
        pause 1
        $ piercings[chosen_piercing].pierced = piercing_state
        $ piercings[chosen_piercing].worn = piercing_state
        $ renpy.show("tattooparlormc ")
        if renpy.has_label(f"mc_piercing_nose_reaction_{hero.gender}"):
            call expression f"mc_piercing_nose_reaction_{hero.gender}" from _call_expression_385
        else:
            pause 2
    scene bg black
    $ renpy.show("tattooparlormc ")
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
