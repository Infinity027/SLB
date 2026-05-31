init python:
    InteractActivity(**{
    "name": "propose",
    "display_name": "Propose",
    "icon": "askmarry",
    "conditions": [
        InInventory("wedding_ring"),
        ActiveTarget(
            Not(IsActivity("sleep")),
            IsFlag("nopropose", False),
            MinStat("love", 160),
            ),
        Or(
            And(
                HeroTarget(
                    IsGender("male"),
                    ),
                ActiveTarget(
                    And(
                        IsFlag("engagedmike", False),
                        IsFlag("engagedmc", False),
                        )
                    ),
            ),
            And(
                HeroTarget(
                    IsGender("female"),
                    ),
                ActiveTarget(
                    IsFlag("engagedmc", False),
                    ),
            ),
        ),
        ],
    "label": "common_propose",
    })

    InteractActivity(**{
    "name": "cancel_propose",
    "display_name": "Cancel engagement",
    "icon": "abortmarry",
    "duration": 0,
    "conditions": [
        ActiveTarget(
            Not(IsActivity("sleep")),
            ),
        Or(
            And(
                HeroTarget(
                    IsGender("male"),
                    ),
                ActiveTarget(
                    And(
                        IsFlag("engagedmike", True),
                        IsFlag("engagedmc", True),
                        )
                    ),
            ),
            And(
                HeroTarget(
                    IsGender("female"),
                    ),
                ActiveTarget(
                    IsFlag("engagedmc", True),
                    ),
            ),
        ),
        ],
    "label": "common_cancel_propose",
    })

label common_propose(from_girl=None):

    if not from_girl:
        $ from_girl = active_girl
    $ girl_harems = Harem.find(from_girl)
    if girl_harems:
        $ unengaged_active_harem_girls = dict()
        $ propose_choices = list()
        python:

            for harem in girl_harems:
                harem_active_members = [Person.find(person) for person in harem.active_members_in_room]
                harem_unengaged_members = [p.id for p in harem_active_members if not p.flags.engagedmike]
                if harem_unengaged_members and hero.has_item("wedding_ring") >= len(harem_unengaged_members):
                    unengaged_active_harem_girls[harem.id] = sorted(harem_unengaged_members)

            if unengaged_active_harem_girls:
                
                
                propose_choices.extend([(f"Propose to {h_id.capitalize()} harem", h_members) for h_id, h_members in unengaged_active_harem_girls.items() if len(h_members) > 1 and renpy.has_label(f"{'_'.join(h_members)}_propose_{hero.gender}")])
            if renpy.has_label(f"{from_girl.id}_propose_{hero.gender}"):
                propose_choices.append((f"Propose to {from_girl.name}", [from_girl.id]))
            propose_choices.append(("Cancel", "canceled"))
        if len(propose_choices) > 2:
            $ narrator("Who should I propose to?", interact=False)
            $ propose_choice = renpy.display_menu(propose_choices)
        else:
            $ propose_choice = propose_choices[0][1]
        if propose_choice == "canceled":
            "I will try again later."
            $ hero.cancel_activity()
            return
        call expression f"{'_'.join(propose_choice)}_propose_{hero.gender}" from _call_expression_446
    else:
        if renpy.has_label(f"{from_girl.id}_propose_{hero.gender}"):
            call expression f"{from_girl.id}_propose_{hero.gender}" from _call_expression_447
        else:
            "I should try again later."
            $ hero.cancel_activity()
    return

label common_cancel_propose(from_girl=None):
    if not from_girl:
        $ from_girl = active_girl
    if renpy.has_label(f"{from_girl.id}_cancel_propose_{hero.gender}"):
        call expression f"{from_girl.id}_cancel_propose_{hero.gender}" from _call_expression_523
    else:
        $ renpy.show(f"{from_girl.id} surprised")
        if hero.is_male:
            mike.say "I think we shouldn't get married right away..."
            mike.say "I... I just need more time..."
            mike.say "To reflect on myself, you know?"
        else:
            bree.say "I think we shouldn't get married right away..."
            bree.say "I... I just need more time..."
            bree.say "To reflect on myself, you know?"
        $ renpy.show(f"{from_girl.id} angry")
        $ renpy.say(from_girl.name, "Yeah.")
        $ renpy.say(from_girl.name, "I see very well what you mean [hero.name]!")
        $ from_girl.cancel_fiance()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
