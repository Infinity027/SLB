init python:
    Gift("romance_novel", price=30, tooltip="A novel that gives love", tags=["books"], love_bonus=1, purity_bonus=-1, bonus_traits=["dreamer", "bookworm"])
    Gift("mistress_amanda", display_name="Mistress Amanda", price=50, tooltip="A book about the dominant Mistress Amanda", tags=["books"], sub_bonus=-1, bonus_traits=["not_religious", "not_innocent", "bookworm", "dominant"])
    Gift("yuri_manga", price=50, tooltip="A manga that represents lesbian scenes", tags=["books", "manga"], les_bonus=1, bonus_traits=["not_religious", "bookworm"])
    Gift("porn_magazine", price=50, tooltip="A magazine with mostly heterosexual picture", tags=["books"], les_bonus=-1, bonus_traits=["slutty", "not_religious", "not_innocent", "bookworm"])
    Gift("a_sex_slave_story", display_name="A sex slave's story", price=50, tooltip="A tale of surrender and passion in the journey of a sex slave", tags=["books"], sub_bonus=1, bonus_traits=["not_religious", "not_innocent", "bookworm", "submissive"])
    Gift("leather_bound_bible", price=100, tooltip="The holy book", tags=["books"], love_bonus=1, purity_bonus=1, bonus_traits=["religious", "not_slutty", "bookworm"])
    Consumable("knowledge_book", price=100, tooltip="An encyclopedia of everything", effects=[("knowledge", 2), ("time", 4)], frequency_limit="week", conditions=[HeroTarget(MinStat("energy", 2), MinStat("hunger", 2), MinStat("grooming", 2), MinStat("fun", 2))])
    Consumable("fitness_book", price=100, tooltip="A book listing training and fitness exercises", effects=[("fitness", 2), ("time", 4)], frequency_limit="week", conditions=[HeroTarget(MinStat("energy", 2), MinStat("hunger", 2), MinStat("grooming", 2), MinStat("fun", 2))])
    Consumable("charm_book", price=100, tooltip="A book about charm techniques", effects=[("charm", 2), ("time", 4)], frequency_limit="week", conditions=[HeroTarget(MinStat("energy", 2), MinStat("hunger", 2), MinStat("grooming", 2), MinStat("fun", 2))])
    Consumable("fun_book", price=25, tooltip="A book with many joke and funny tricks", effects=[("fun", 4), ("time", 2)], frequency_limit="day", conditions=[HeroTarget(MinStat("energy", 2), MinStat("hunger", 2), MinStat("grooming", 2), MinStat("fun", 2))])
    Consumable("skill_book_massage", display_name="Skill book: massage", price=200, label="massage_skill_book", uses=10, tooltip="A book to learn how to give massages", conditions=[HeroTarget(MinStat("energy", 2), MinStat("hunger", 2), MinStat("grooming", 2), MinStat("fun", 2))], one_only=True)
    Consumable("skill_book_guitar", display_name="Skill book: guitar", price=200, label="guitar_skill_book", uses=10, tooltip="A book to learn how to play the guitar", conditions=[HeroTarget(MinStat("energy", 2), MinStat("hunger", 2), MinStat("grooming", 2), MinStat("fun", 2))], one_only=True)
    Consumable("skill_book_cooking", display_name="Skill book: cooking", price=200, label="cooking_skill_book", uses=10, tooltip="A book to learn how to cook", conditions=[HeroTarget(MinStat("energy", 2), MinStat("hunger", 2), MinStat("grooming", 2), MinStat("fun", 2))], one_only=True)
    Consumable("sexperience_book", price=100, label="sexperience_book", uses=10, tooltip="A book to learn how to fuck like a god", conditions=[HeroTarget(MinStat("energy", 2), MinStat("hunger", 2), MinStat("grooming", 2), MinStat("fun", 2))], one_only=True)
    Consumable("skill_book_shibari", display_name="Skill book: shibari", price=200, label="shibari_skill_book", uses=20, tooltip="A book to learn how to play with ropes", conditions=[HeroTarget(MinStat("energy", 2), MinStat("hunger", 2), MinStat("grooming", 2), MinStat("fun", 2))], one_only=True)
    Consumable("skill_book_sm", display_name="Skill book: SM", price=200, label="sm_skill_book", uses=20, tooltip="A book to learn SM techniques", conditions=[HeroTarget(MinStat("energy", 2), MinStat("hunger", 2), MinStat("grooming", 2), MinStat("fun", 2))], one_only=True)
    Consumable("skill_book_fertility", display_name="Skill book: fertility", price=200, label="fertility_skill_book", uses=10, tooltip="A book to learn how to know if a girl is fertile", conditions=[HeroTarget(MinStat("energy", 2), MinStat("hunger", 2), MinStat("grooming", 2), MinStat("fun", 2))], one_only=True)
    Consumable("skill_book_investigation", display_name="How to get away with murder", price=400, label="investigation_skill_book", uses=4, tooltip="A rare compilation of archived police files talking about murder and the methods used to solve them", conditions=[HeroTarget(MinStat("energy", 2), MinStat("hunger", 2), MinStat("grooming", 2), MinStat("fun", 2))], one_only=True)
    Gift("fantasy_book_signed", display_name="Fantasy book (signed)", price=50, tags=["books"], label="signed_fantasy_book", love_bonus=0)
    Item("shark_training", display_name="How to train your shark", price=1000, tooltip="A book about shark training... Might be a parody of a well known movie.")


    Room(**{
    "name": "bookstore",
    "exits": ["mall1", "bakery", "clothesshop", "arcade", "tattooshop", "mallmap"],
    "hours": (9, 18),
    "conditions": [
        IsHour(9, 18),
        ],
    "display_name": "Book Store",
    "music": "music/roa_music/good_morning.ogg",
    "outfit": "casual",
    "tags": ["mall_southside"],
    "inventory": (
        "romance_novel",
        "mistress_amanda",
        "yuri_manga",
        "porn_magazine",
        "a_sex_slave_story",
        "leather_bound_bible",
        "knowledge_book",
        "charm_book",
        "fun_book",
        "shark_training",
        {"id": "skill_book_massage", "conditions": ("game.days_played % 7 == 0", 'not hero.has_skill("massage")')},
        {"id": "skill_book_guitar", "conditions": ("game.days_played % 7 == 1", 'not hero.has_skill("guitar")')},
        {"id": "skill_book_cooking", "conditions": ("game.days_played % 7 == 2", 'not hero.has_skill("cooking")')},
        {"id": "sexperience_book", "conditions": ("game.days_played % 7 == 3",)},
        {"id": "skill_book_shibari", "conditions": ("game.days_played % 7 == 4", 'not hero.has_skill("shibari")')},
        {"id": "skill_book_sm", "conditions": ("game.days_played % 7 == 5", 'not hero.has_skill("sm")')},
        {"id": "skill_book_fertility", "conditions": ("game.days_played % 7 == 6", 'not hero.has_skill("fertility_assessment")')},
        {"id": "skill_book_investigation", "conditions": ('not hero.has_skill("investigator")',)},
        ),
    })

    Activity(**{
    "name": "bookstore_shop",
    "label": "bookstore_shop",
    "duration": 0,
    "icon": "shop",
    "rooms": "bookstore",
    "display_name": "Shop",
    })

    Activity(**{
    "name": "work_bookstore",
    "label": "work_bookstore",
    "money_gain": {"attributes": ["charm"], "bonus": (1,)},
    "duration": 4,
    "rooms": "bookstore",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_day", "bookstore"),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })

    Event(**{
    "name": "book_signing",
    "label": "book_signing",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("bookstore")),
        PersonTarget(bree,
            Not(IsHidden()),
            Not(IsRoom("bookstore")),
            MinStat("love", 25),
            ),
        ],
    "chances": 5,
    "do_once": False,
    })

label book_signing:

    "[bree.name]'s favorite author is here, signing books."
    "Maybe I should get his latest book and get it signed."
    $ result = renpy.display_menu([("Do it", 1), ("Don't do it", 2)])
    if result == 1:
        if hero.money >= 50:
            $ hero.money -= 50
            $ hero.gain_item("fantasy_book_signed")
            "I'm pretty sure she will be thrilled."
            $ game.pass_time(needs=True)
        else:
            "Too bad I don't have enough money."
    else:
        "It's not worth my time."

    return

label work_bookstore:
    show chibi bookstore
    "If I can sell a hundred books I get a one dollar bonus!"
    hide chibi
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    return

label bookstore_shop:
    $ Room.find("bookstore").shop("natalie casual")
    return

label sexperience_book:
    if hero.has_skill("bookworm"):
        $ game.pass_time(1, True)
    else:
        $ game.pass_time(2, True)
    $ hero.flags.sexperience += 2
    return

label massage_skill_book:
    if hero.has_skill("massage"):
        "I know everything I need to about massages."
    else:
        if hero.has_skill("bookworm"):
            $ game.pass_time(1, True)
        else:
            $ game.pass_time(2, True)
        $ hero.gain_skill("massage", 10)
        $ skill = hero.skills.massage.value
        "I read about massages in the book. ([skill]%%)"
    return

label fertility_skill_book:
    if hero.has_skill("fertility_assessment"):
        "I know everything I need to about fertility."
    else:
        if hero.has_skill("bookworm"):
            $ game.pass_time(1, True)
        else:
            $ game.pass_time(2, True)
        $ hero.gain_skill("fertility_assessment", 10)
        $ skill = hero.skills.fertility_assessment.value
        "I read about fertility and how to spot it in the book. ([skill]%%)"
    return

label investigation_skill_book:
    if hero.has_skill("investigator"):
        "I know everything I need to about investigation."
    else:
        if hero.has_skill("bookworm"):
            $ game.pass_time(1, True)
        else:
            $ game.pass_time(2, True)
        $ hero.gain_skill("investigator", 25)
        $ skill = hero.skills.investigator.value
        "I read the investigation advices in the book. ([skill]%%)"
        if skill <= 25:
            "{i}\"When we found a corpse the first thing to do is to search everywhere around its location to retrieve the murder weapon.\"{/i}"
            "{i}\"It doesn't matter if the place is big, it will eventually be found.\"{/i}"
            "Pfff, like I'm gonna believe that!"
            "It's not possible to find something as small as a knife or a gun in a forest or in the sea."
        elif skill <= 50:
            "{i}\"It's complex police work to unravel the true from the false when all suspects gives us the same version.\"{/i}"
            "That make sense."
        elif skill <= 75:
            "{i}\"It's easier to get info from the suspects when they're isolated for a long time.\"{/i}"
            "{i}\"Their mind will play trick on them, thinking the others will rat about them.\"{/i}"
            "{i}\"Then we just have to press a little more to get the first flaws in their story.\"{/i}"
            "It's not surprising that people want to get out of such situation, even if that means throwing their accomplice under the bus."
            "It would be much more complex for the police though if they could just blindly trust in each other."
        else:
            "{i}\"It's rare, but a case can be especially complex when we start to trust someone we shouldn't.\"{/i}"
            "{i}\"There was this one guy who was a suspect, like the others...\"{/i}"
            "{i}\"But he offered so much help through the investigation that we unwittingly stop being suspicious of him.\"{/i}"
            "{i}\"Fortunately, this psychopath was always wandering around with a backpack containing a jar of his victims' big toes.\"{/i}"
            "{i}\"The smell betrayed him the day he didn't close it properly.\"{/i}"
            "Who the fuck carry such thing!?"
            "Wait... I remember this affair!"
            "It was some old filmmaker that always had a thing for feet!"
            "I think he's the one that made Zest Fiction."
            "We really live in a sick world..."
    return

label guitar_skill_book:
    if hero.has_skill("guitar"):
        "I know everything I need to about playing guitar."
    else:
        if hero.has_skill("bookworm"):
            $ game.pass_time(1, True)
        else:
            $ game.pass_time(2, True)
        $ hero.gain_skill("guitar", 10)
        $ skill = hero.skills.guitar.value
        "I practice guitar. ([skill]%%)"
    return

label cooking_skill_book:
    if hero.has_skill("cooking"):
        "I know everything I need to about cooking."
    else:
        if hero.has_skill("bookworm"):
            $ game.pass_time(1, True)
        else:
            $ game.pass_time(2, True)
        $ hero.gain_skill("cooking", 10)
        $ skill = hero.skills.cooking.value
        "I learn cooking. ([skill]%%)"
    return

label shibari_skill_book:
    if hero.has_skill("shibari"):
        "I know everything I need to about shibari."
    else:
        if hero.has_skill("bookworm"):
            $ game.pass_time(1, True)
        else:
            $ game.pass_time(2, True)
        $ hero.gain_skill("shibari", 5)
        $ skill = hero.skills.shibari.value
        "I learn shibari. ([skill]%%)"
    return

label sm_skill_book:
    if hero.has_skill("sm"):
        "I know everything I need to about SM."
    else:
        if hero.has_skill("bookworm"):
            $ game.pass_time(1, True)
        else:
            $ game.pass_time(2, True)
        $ hero.gain_skill("sm", 5)
        $ skill = hero.skills.sm.value
        "I learn S&M. ([skill]%%)"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
