init python:
    DayTransitionEvent(**{
    "name": "pay_bills",
    "label": "pay_bills",
    "priority": 1000,
    "conditions": [
        MinDaysPlayed(1),
        IsDayOfWeek("1"),
        ],
    "once_day": False,
    "once_week": True,
    })

    DayTransitionEvent(**{
    "name": "sick",
    "label": "sick",
    "conditions": [
        HeroTarget(IsFlag("sick", False)),
        ],
    "chances": 5,
    "once_day": False,
    "once_week": True,
    })

    Event(**{
    "name": "low_energy",
    "label": "low_energy",
    "priority": 100,
    "conditions": [
        HeroTarget(MaxStat("energy", 3)),
        ],
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "low_hunger",
    "label": "low_hunger",
    "priority": 100,
    "conditions": [
        HeroTarget(MaxStat("hunger", 3)),
        ],
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "low_grooming",
    "label": "low_grooming",
    "priority": 100,
    "conditions": [
        HeroTarget(MaxStat("grooming", 3)),
        ],
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "low_fun",
    "label": "low_fun",
    "priority": 100,
    "conditions": [
        HeroTarget(MaxStat("fun", 3)),
        ],
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

label low_fun:
    "I am so bored."
    return

label low_grooming:
    "I smell like something died in my pants."
    return

label low_hunger:
    "I am so hungry."
    return

label low_energy:
    "I am so tired."
    return

label sick:

    call expression f"sick_dialogues_1_{hero.gender}" from _call_expression_405
    "I think I might be sick."
    $ game.flags.sick = TemporaryFlag(True, randint(1, 3), hook="clear_sickness_penalties")
    $ hero.energy.decay_penalty = True
    $ hero.energy.gain_penalty = True
    $ hero.fun.gain_penalty = True
    $ hero.grooming.gain_penalty = True
    $ hero.hunger.gain_penalty = True
    return

label clear_sickness_penalties:
    $ hero.energy.decay_penalty = False
    $ hero.energy.gain_penalty = False
    $ hero.fun.gain_penalty = False
    $ hero.grooming.gain_penalty = False
    $ hero.hunger.gain_penalty = False
    return

label cured:
    call expression f"cured_dialogues_1_{hero.gender}" from _call_expression_406
    $ game.flags.sick = False
    $ hero.energy.decay_penalty = False
    $ hero.energy.gain_penalty = False
    $ hero.fun.gain_penalty = False
    $ hero.grooming.gain_penalty = False
    $ hero.hunger.gain_penalty = False
    if FLAGS.get("HERO!sick") and FLAGS["HERO!sick"].duration != 0:
        $ FLAGS.pop("HERO!sick")
    return

label injured:



    $ game.flags.injured = TemporaryFlag(True, randint(1, 3), hook="clear_injury_penalties")
    $ hero.fun.decay_penalty = True
    $ hero.grooming.decay_penalty = True
    $ hero.hunger.decay_penalty = True
    return

label clear_injury_penalties:
    $ hero.fun.decay_penalty = False
    $ hero.grooming.decay_penalty = False
    $ hero.hunger.decay_penalty = False
    return

label healed:
    call expression f"healed_dialogues_1_{hero.gender}" from _call_expression_542
    $ game.flags.injured = False
    $ hero.fun.decay_penalty = False
    $ hero.grooming.decay_penalty = False
    $ hero.hunger.decay_penalty = False
    if FLAGS.get("HERO!injured") and FLAGS["HERO!injured"].duration != 0:
        $ FLAGS.pop("HERO!injured")
    return

label enhance_penis:
    if hero.has_skill("hung"):
        mike.say "One more and I won't be able to find any underwear at my size."
        return
    elif hero.has_skill("smalldick"):
        $ hero.gain_skill("smalldick", False)
    else:
        $ hero.gain_skill("hung")
    mike.say "I can feel my underwear being tighter."
    return

label diminish_penis:
    if hero.has_skill("smalldick"):
        mike.say "I won't be able to see it if I take one more."
        return
    elif hero.has_skill("hung"):
        $ hero.gain_skill("hung", False)
    else:
        $ hero.gain_skill("smalldick")
    mike.say "I can feel my underwear being larger."
    return

label pay_bills:
    $ rent = game.get_rent_amount()
    if game.flags.debt > 0:
        $ payment = game.flags.debt if game.flags.debt < 200 else 200
        "Time to pay my weekly debt due... ([payment]{image=gui/icons/icon_money.png})"
        if hero.money >= payment:
            $ hero.money -= payment
            $ payment = payment * 0.9 if payment < game.flags.debt else game.flags.debt
            $ game.flags.debt -= payment
        else:
            "I don't have enough money..."
            "I should at least give what I have..."
            $ game.flags.debt -= hero.money - 50
            $ hero.money.val = 0
        if game.flags.debt <= 0:
            "I have finally paid my debt off!"
            $ game.flags.debt = 0
    if hero.money >= rent:
        "Time to pay the rent... ([rent]{image=gui/icons/icon_money.png})"
        $ hero.money -= rent
    else:
        "I don't have enough money to pay the rent..."
        "I should at least give what I have..."
        python:
            for p in Person.get_housemates():
                p.love -= 10
            hero.money.val = 0
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
