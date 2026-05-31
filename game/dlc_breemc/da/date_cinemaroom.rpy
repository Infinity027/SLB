init python:
    Activity(**{
    "name": "date_put_hand_on_leg_female",
    "display_name": "Put [date_girl.possessive_adjective] hand on your leg",
    "label": "date_put_hand_on_leg_female",
    "icon": "caress",
    "rooms": "date_cinemaroom",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MaxStat("morality", 25)
            ),
        ActiveTarget(
            IsFlag("datehand", False)
            ),
        ],
    "once_day": True,
    "duration": 0,
    })

    Activity(**{
    "name": "date_put_hand_between_legs_female",
    "display_name": "Put [date_girl.possessive_adjective] hand between your legs",
    "label": "date_put_hand_between_legs_female",
    "icon": "between",
    "once_day": True,
    "rooms": "date_cinemaroom",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MaxStat("morality", 15)
            ),
        ActiveTarget(
            IsFlag("datehand", "leg"),
            ),
        ],
    "duration": 0,
    })

    Activity(**{
    "name": "date_put_hand_in_panties_female",
    "display_name": "Make [date_girl.personal_pronoun] finger you",
    "label": "date_put_hand_in_panties_female",
    "icon": "finger",
    "rooms": "date_cinemaroom",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MaxStat("morality", -15)
            ),
        ActiveTarget(
            IsFlag("datehand", "between"),
            ),
        ],
    "once_day": True,
    "duration": 0,
    })

    Activity(**{
    "name": "date_caress_boobs_female",
    "display_name": "Put [date_girl.possessive_adjective] hand over your chest",
    "label": "date_caress_boobs_female",
    "icon": "caressboobs",
    "rooms": "date_cinemaroom",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MaxStat("morality", -5)
            ),
        ActiveTarget(
            IsFlag("datehand", False),
            ),
        ],
    "once_day": True,
    "duration": 0,
    })

    Activity(**{
    "name": "date_caress_boobs_inside_female",
    "display_name": "Put [date_girl.possessive_adjective] hand inside your top",
    "label": "date_caress_boobs_inside_female",
    "icon": "handinbra",
    "rooms": "date_cinemaroom",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MaxStat("morality", -10)
            ),
        ActiveTarget(
            IsFlag("datehand", "breasts"),
            ),
        ],
    "once_day": True,
    "duration": 0,
    })






















    Activity(**{
    "name": "date_put_hand_in_pants_female",
    "display_name": "Put [date_girl.possessive_adjective] hand in your pants",
    "label": "date_put_hand_in_pants_female",
    "icon": "pants",
    "rooms": "date_cinemaroom",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MaxStat("morality", 0)
            ),
        ActiveTarget(
            IsFlag("datehand", "finger"),
            ),
        ],
    "once_day": True,
    "duration": 0,
    })

    Activity(**{
    "name": "date_jerk_off_female",
    "display_name": "Jerk him off",
    "label": "date_jerk_off_female",
    "icon": "handjob",
    "rooms": "date_cinemaroom",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MaxStat("morality", -20)
            ),
        ActiveTarget(
            IsFlag("datehand", "finger"),
            IsGender("male"),
            ),
        ],
    "once_day": True,
    "duration": 0,
    })

    Activity(**{
    "name": "date_blow_him_female",
    "display_name": "Blow him",
    "label": "date_blow_female",
    "icon": "blowjob",
    "rooms": "date_cinemaroom",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MaxStat("morality", -50)
            ),
        ActiveTarget(
            IsFlag("datehand", "jerk"),
            IsGender("male"),
            ),
        ],
    "once_day": True,
    "duration": 0,
    })

label date_caress_boobs_female:
    $ renpy.show(f"watch movie grab outside happy {active_girl.id}")
    "I slowly put [active_girl.possessive_adjective] hand over my chest."
    if active_girl.love <= 75 - hero.charm:
        active_girl.say "What do you think you are doing?"
        $ renpy.show("watch movie normal")
        $ game.active_date.score -= 10
    else:
        "[active_girl.subject_pronoun!c] starts caressing my breasts above the clothes."
        $ active_girl.flags.datehand = TemporaryFlag("breasts", 1)
        if "slutty" in active_girl.traits:
            $ game.active_date.score += 5
    hide watch movie
    return

label date_caress_boobs_inside_female:
    $ renpy.show(f"watch movie grab inside happy {active_girl.id}")
    "I move my top aside so [active_girl.subject_pronoun] can caress my skin directly."
    if active_girl.love <= 100 - hero.charm:
        active_girl.say "What do you think you are doing?"
        $ renpy.show("watch movie normal")
        $ active_girl.flags.datehand = TemporaryFlag(False, 1)
        $ game.active_date.score -= 10
    else:
        $ renpy.show("watch movie blush")
        "I blush a little when [active_girl.possessive_adjective] fingers reach my nipples."
        $ renpy.show("watch movie normal")
        "After a while [active_girl.subject_pronoun] removes [active_girl.possessive_adjective] hand..."
        "And I'm a little disappointed."
        $ active_girl.flags.datehand = TemporaryFlag(False, 1)
        if "slutty" in active_girl.traits:
            $ game.active_date.score += 20
        else:
            $ game.active_date.score += 5
    hide watch movie
    return

label date_put_hand_on_leg_female:
    $ renpy.show(f"watch movie happy {active_girl.id}")
    "I slowly put [active_girl.possessive_adjective] hand on my leg."
    if active_girl.love <= 75 - hero.charm:
        active_girl.say "What do you think you are doing?"
        $ game.active_date.score -= 10
    else:
        $ renpy.show("watch movie leg")
        "It feels good."
        "I smile at [active_girl.personal_pronoun]"
        $ active_girl.flags.datehand = TemporaryFlag("leg", 1)
        if "slutty" in active_girl.traits:
            $ game.active_date.score += 5
    hide watch movie
    return

label date_put_hand_between_legs_female:
    $ renpy.show(f"watch movie finger outside happy {active_girl.id}")
    "I move [active_girl.possessive_adjective] hand up toward my panties."
    if active_girl.love <= 100 - hero.charm:
        active_girl.say "What do you think you are doing?"
        $ renpy.show("watch movie normal")
        $ active_girl.flags.datehand = TemporaryFlag(False, 1)
        $ game.active_date.score -= 10
    else:
        "I moan a little when [active_girl.subject_pronoun] reach my underwear."
        $ active_girl.flags.datehand = TemporaryFlag("between", 1)
        if "slutty" in active_girl.traits:
            $ game.active_date.score += 5
    hide watch movie
    return

label date_put_hand_in_panties_female:
    $ renpy.show(f"watch movie finger outside happy {active_girl.id}")
    "I push my underwear aside and try to put [active_girl.possessive_adjective] finger inside me."
    if active_girl.love <= 125 - hero.charm:
        active_girl.say "What do you think you are doing?"
        $ renpy.show("watch movie normal")
        $ active_girl.flags.datehand = TemporaryFlag(False, 1)
        $ game.active_date.score -= 10
    else:
        $ renpy.show("watch movie finger inside blush")
        "My breath starts to get heavy as [active_girl.subject_pronoun] fingers me."
        active_girl.say "Mmmmmmh."
        "I slowly reach to climax, while watching the movie."
        if active_girl.is_female:
            $ active_girl.flags.datehand = TemporaryFlag(False, 1)
        else:
            $ active_girl.flags.datehand = TemporaryFlag("finger", 1)
        if "slutty" in active_girl.traits:
            $ game.active_date.score += 20
        else:
            $ game.active_date.score += 5
    hide watch movie
    return











label date_jerk_off_female:
    $ renpy.show(f"watch movie happy handjob {active_girl.id}")
    "I jerk him off until he comes in my hand."
    $ active_girl.flags.datehand = TemporaryFlag("jerk", 1)
    if "sluts" in active_girl.desire_factors:
        $ game.active_date.score += 5
    $ renpy.hide(active_girl.id)
    return

label date_blow_female:
    $ renpy.show(f"watch movie happy blowjob {active_girl.id}")
    "I get on my knees and blow him."
    $ active_girl.flags.datehand = TemporaryFlag("blow", 1)
    if "sluts" in active_girl.desire_factors:
        $ game.active_date.score += 5
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
