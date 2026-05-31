init python:
    Activity(**{
    "name": "ask_for_a_job_church_female",
    "duration": 0,
    "icon": "askforjob",
    "rooms": "church",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("morality", 90),
            IsFlag("job_day", False)),
        ],
    "display_name": "Ask for a job",
    "label": "ask_for_a_job_day",
})

    Activity(**{
    "name": "work_church_female",
    "label": "work_church",
    "money_gain": {"attributes": ["charm", "fitness", "knowledge"], "mult": (2,)},
    "duration": 4,
    "rooms": "church",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_day", "church"),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })

    Activity(**{
    "name": "ask_for_a_job_female_homelessshelter",
    "duration": 0,
    "icon": "askforjob",
    "rooms": "alley",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("morality", 70),
            Or(
                And(IsFlag("job_day", False),
                    Not(IsFlag("job_night", "homelessshelter")),
                    ),
                And(IsFlag("job_night", False),
                    Not(IsFlag("job_day", "homelessshelter")),
                    ),
                ),
            ),
        ],
    "display_name": "Ask for a job",
    "label": "ask_for_a_job_homelessshelter",
})

    Activity(**{
    "name": "work_homelessshelter_female",
    "label": "work_homelessshelter",
    "money_gain": {"attributes": ["charm", "fitness"], "mult": (1.8,)},
    "duration": 4,
    "rooms": "alley",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            Or(
                And(IsFlag("job_day", "homelessshelter"),
                    IsTimeOfDay("morning", "afternoon"),
                    ),
                And(IsFlag("job_night", "homelessshelter"),
                    IsTimeOfDay("evening", "night"),
                    ),
                ),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })

    Activity(**{
    "name": "ask_for_a_job_bookstore_female",
    "duration": 0,
    "icon": "askforjob",
    "rooms": "bookstore",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("morality", 50),
            IsFlag("job_day", False),
            ),
        ],
    "display_name": "Ask for a job",
    "label": "ask_for_a_job_day",
})

    Activity(**{
    "name": "work_bookstore_female",
    "label": "work_bookstore",
    "money_gain": {"attributes": ["fitness", "knowledge"], "mult": (1.6,)},
    "duration": 4,
    "rooms": "bookstore",
    "conditions": [
        HeroTarget(
            IsGender("female"),
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

    Activity(**{
    "name": "ask_for_a_job_flowershop_female",
    "duration": 0,
    "icon": "askforjob",
    "rooms": "flowershop",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("morality", 30),
            IsFlag("job_day", False)),
        ],
    "display_name": "Ask for a job",
    "label": "ask_for_a_job_day",
})

    Activity(**{
    "name": "work_flowershop_female",
    "label": "work_flowershop",
    "money_gain": {"attributes": ["charm", "knowledge"], "mult": (1.3,)},
    "duration": 4,
    "rooms": "flowershop",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_day", "flowershop"),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })


    Activity(**{
    "name": "ask_for_a_job_electronic_female",
    "duration": 0,
    "icon": "askforjob",
    "rooms": "electronic",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("morality", 10),
            IsFlag("job_day", False)),
        ],
    "display_name": "Ask for a job",
    "label": "ask_for_a_job_day",
})

    Activity(**{
    "name": "work_electronic_female",
    "label": "work_electronic",
    "money_gain": {"attributes": ["knowledge"], "mult": (1.1,)},
    "duration": 4,
    "rooms": "electronic",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_day", "electronic"),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })

    Activity(**{
    "name": "ask_for_a_job_female",
    "duration": 0,
    "icon": "askforjob",
    "rooms": ("bakery", "clothesshop", "coffeeshop", "jewelrystore"),
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsFlag("job_day", False)),
        ],
    "display_name": "Ask for a job",
    "label": "ask_for_a_job_day",
})

    Activity(**{
    "name": "work_bakery_female",
    "label": "work_bakery",
    "money_gain": {"attributes": ["charm"]},
    "duration": 4,
    "rooms": "bakery",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_day", "bakery"),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })

    Activity(**{
    "name": "work_clothesshop_female",
    "label": "work_clothesshop",
    "money_gain": {"attributes": ["charm"]},
    "duration": 4,
    "rooms": "clothesshop",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_day", "clothesshop"),
            ),
        Not(
            Or(
                And(
                    IsNotDone("sasha_clothesshop_coworker_01"),
                    HeroTarget(MinFlag("worked_clothesshop", 3)),
                    ),
                And(
                    IsNotDone("sasha_clothesshop_coworker_02"),
                    HeroTarget(MinFlag("worked_clothesshop", 6)),
                    ),
                And(
                    IsNotDone("sasha_clothesshop_coworker_03"),
                    HeroTarget(MinFlag("worked_clothesshop", 9)),
                    ),
                And(
                    IsNotDone("sasha_clothesshop_friend_01"),
                    HeroTarget(MinFlag("worked_clothesshop", 12)),
                    ),
                And(
                    IsNotDone("sasha_clothesshop_friend_02"),
                    HeroTarget(MinFlag("worked_clothesshop", 15)),
                    ),
                And(
                    IsNotDone("sasha_clothesshop_friend_03"),
                    HeroTarget(MinFlag("worked_clothesshop", 18)),
                    ),
                And(
                    IsNotDone("sasha_clothesshop_friend_04"),
                    HeroTarget(MinFlag("worked_clothesshop", 21)),
                    ),
                And(
                    Or(
                        And(
                            IsNotDone("sasha_clothesshop_lover_01"),
                            HeroTarget(MinFlag("worked_clothesshop", 24)),
                            ),
                        And(
                            IsNotDone("sasha_clothesshop_lover_02"),
                            HeroTarget(MinFlag("worked_clothesshop", 27)),
                            ),
                        And(
                            IsNotDone("sasha_clothesshop_lover_03"),
                            HeroTarget(MinFlag("worked_clothesshop", 30)),
                            ),
                        ),
                    PersonTarget(sasha, MinStat("love", 160)),
                    ),
                ),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })

    Activity(**{
    "name": "work_coffeeshop_female",
    "label": "work_coffeeshop",
    "money_gain": {"attributes": ["charm"]},
    "duration": 4,
    "rooms": "coffeeshop",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_day", "coffeeshop"),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })

    Activity(**{
    "name": "ask_for_a_job_gym_female",
    "duration": 0,
    "icon": "askforjob",
    "rooms": "gymreception",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Or(
                And(IsFlag("job_day", False),
                    Not(IsFlag("job_night", "gym")),
                    ),
                And(IsFlag("job_night", False),
                    Not(IsFlag("job_day", "gym")),
                    ),
                ),
            ),
        ],
    "display_name": "Ask for a job",
    "label": "ask_for_a_job",
})

    Activity(**{
    "name": "work_gym_female",
    "label": "work_gym",
    "money_gain": {"attributes": ["fitness"]},
    "duration": 4,
    "rooms": ("gym", "gymmachine"),
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            Or(
                And(IsFlag("job_day", "gym"),
                    IsTimeOfDay("morning", "afternoon"),
                    ),
                And(IsFlag("job_night", "gym"),
                    IsTimeOfDay("evening", "night"),
                    ),
                ),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })

    Activity(**{
    "name": "work_jewelrystore_female",
    "label": "work_jewelrystore",
    "money_gain": {"attributes": ["knowledge"]},
    "duration": 4,
    "rooms": "jewelrystore",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_day", "jewelrystore"),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })

    Activity(**{
    "name": "ask_for_a_job_pub_female",
    "duration": 0,
    "icon": "askforjob",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            HasRoomTag("pub"),
            MaxStat("morality", -10),
            IsFlag("job_night", False)),
        ],
    "display_name": "Ask for a job",
    "label": "ask_for_a_job_night",
})

    Activity(**{
    "name": "work_pub_female",
    "label": "work_pub",
    "money_gain": {"attributes": ["fitness"], "mult": (1.1,)},
    "duration": 4,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            HasRoomTag("pub"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_night", ("pub", "pubplay", "pubseat", "pubexterior")),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })

    Activity(**{
    "name": "ask_for_a_job_university_female",
    "duration": 0,
    "icon": "askforjob",
    "rooms": "university",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("knowledge", 100),
            IsFlag("job_day", False)),
        ],
    "display_name": "Ask for a job",
    "label": "ask_for_a_job_day",
})

    Activity(**{
    "name": "work_university_female",
    "label": "work_university",
    "money_gain": {"attributes": ["knowledge","charm"], "mult": (1.5,)},
    "duration": 4,
    "rooms": "classroom",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_day", "university"),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })

    Activity(**{
    "name": "ask_for_a_job_nightclub_female",
    "duration": 0,
    "icon": "askforjob",
    "rooms": "nightclub",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MaxStat("morality", -20),
            IsFlag("job_night", False)),
        ],
    "display_name": "Ask for a job",
    "label": "ask_for_a_job_night",
})

    Activity(**{
    "name": "work_nightclub_female",
    "label": "work_nightclub",
    "money_gain": {"attributes": ["charm"], "mult": (1.2,)},
    "duration": 4,
    "rooms": "nightclub",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_night", "nightclub"),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })

    Activity(**{
    "name": "ask_for_a_job_maidcafe_female",
    "duration": 0,
    "icon": "askforjob",
    "rooms": "maidcafe",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MaxStat("morality", -30),
            IsFlag("job_day", False),
            ),
        ],
    "display_name": "Ask for a job",
    "once_month": True,
    "label": "ask_for_a_job_day",
    })

    Activity(**{
    "name": "work_maidcafe_female",
    "label": "work_maidcafe",
    "money_gain": {"attributes": ["charm", "fitness"], "mult": (1.4,)},
    "duration": 4,
    "rooms": "maidcafe",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 4),
            MinStat("hunger", 4),
            MinStat("grooming", 4),
            MinStat("fun", 4),
            IsFlag("job_day", "maidcafe"),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })

    Activity(**{
    "name": "ask_for_a_job_sexshop_female",
    "duration": 0,
    "icon": "askforjob",
    "rooms": "sexshop",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MaxStat("morality", -40),
            IsFlag("job_night", False)),
        ],
    "display_name": "Ask for a job",
    "label": "ask_for_a_job_night",
})

    Activity(**{
    "name": "work_sexshop_female",
    "label": "work_sexshop",
    "money_gain": {"attributes": ["charm", "knowledge"], "mult": (1.5,)},
    "duration": 4,
    "rooms": "sexshop",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_night", "sexshop"),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })

    Activity(**{
    "name": "ask_for_a_job_stripper_female",
    "duration": 0,
    "icon": "askforjob",
    "rooms": ["stripclub"],
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MaxStat("morality", -50),
            IsFlag("job_night", False)),
        ],
    "display_name": "Ask for a job",
    "label": "ask_for_a_job_night",
})

    Activity(**{
    "name": "work_stripclub_female",
    "label": "work_stripclub",
    "money_gain": {"attributes": ["charm", "fitness"], "mult": (1.6,)},
    "duration": 4,
    "rooms": ["stripclub"],
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_night", "stripclub"),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })

    Activity(**{
    "name": "ask_for_a_job_model_female",
    "duration": 0,
    "icon": "askforjob",
    "rooms": "photostudio",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MaxStat("morality", -60),
            Or(
                And(IsFlag("job_day", False),
                    Not(IsFlag("job_night", "model")),
                    ),
                And(IsFlag("job_night", False),
                    Not(IsFlag("job_day", "model")),
                    ),
                ),
            ),
        ],
    "display_name": "Ask for a job as a model",
    "label": "ask_for_a_job_model",
})

    Activity(**{
    "name": "work_model_female",
    "label": "work_model",
    "money_gain": {"attributes": ["charm", "fitness"], "mult": (1.7,)},
    "duration": 4,
    "rooms": "photostudio",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            Or(
                And(IsFlag("job_day", "model"),
                    IsTimeOfDay("morning", "afternoon"),
                    ),
                And(IsFlag("job_night", "model"),
                    IsTimeOfDay("evening", "night"),
                    ),
                ),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })

    Activity(**{
    "name": "ask_for_a_job_camgirl_female",
    "duration": 0,
    "icon": "askforjob",
    "rooms": "bedroom4",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MaxStat("morality", -70),
            Or(
                And(IsFlag("job_day", False),
                    Not(IsFlag("job_night", "bedroom4")),
                    ),
                And(IsFlag("job_night", False),
                    Not(IsFlag("job_day", "bedroom4")),
                    ),
                ),
            ),
        ],
    "display_name": "Work as a camgirl",
    "label": "ask_for_a_job_camgirl",
})

    Activity(**{
    "name": "work_camgirl_female",
    "label": "work_camgirl",
    "money_gain": {"attributes": ["charm", "knowledge"], "mult": (1.8,)},
    "duration": 4,
    "rooms": "bedroom4",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            Or(
                And(IsFlag("job_day", "bedroom4"),
                    IsTimeOfDay("morning", "afternoon"),
                    ),
                And(IsFlag("job_night", "bedroom4"),
                    IsTimeOfDay("evening", "night"),
                    ),
                ),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })

    Activity(**{
    "name": "quit_job_camgirl",
    "duration": 0,
    "icon": "quitjob",
    "rooms": "bedroom4",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Or(
                IsFlag("job_day", "bedroom4"),
                IsFlag("job_night", "bedroom4"),
                ),
            ),
        ],
    "display_name": "Quit your camgirl job",
    "once_day": True,
    "label": "quit_camgirl_job",
    })

    Activity(**{
    "name": "ask_for_a_job_pornstar_female",
    "duration": 0,
    "icon": "askforjob",
    "rooms": "photostudio",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MaxStat("morality", -80),
            Or(
                And(IsFlag("job_day", False),
                    Not(IsFlag("job_night", "pornstar")),
                    ),
                And(IsFlag("job_night", False),
                    Not(IsFlag("job_day", "pornstar")),
                    ),
                ),
            ),
        ],
    "display_name": "Ask for a job as a pornstar",
    "label": "ask_for_a_job_pornstar",
})

    Activity(**{
    "name": "work_pornstar_female",
    "label": "work_pornstar",
    "money_gain": {"attributes": ["charm", "fitness", "knowledge"], "mult": (1.9,)},
    "duration": 4,
    "rooms": "photostudio",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            Or(
                And(IsFlag("job_day", "pornstar"),
                    IsTimeOfDay("morning", "afternoon"),
                    ),
                And(IsFlag("job_night", "pornstar"),
                    IsTimeOfDay("evening", "night"),
                    ),
                ),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })

    Activity(**{
    "name": "ask_for_a_job_prostitute_female",
    "duration": 0,
    "icon": "askforjob",
    "rooms": "alley",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MaxStat("morality", -90),
            Or(
                And(IsFlag("job_day", False),
                    Not(IsFlag("job_night", "prostitute")),
                    ),
                And(IsFlag("job_night", False),
                    Not(IsFlag("job_day", "prostitute")),
                    ),
                ),
            ),
        ],
    "display_name": "Ask for a job",
    "label": "ask_for_a_job_prostitute",
})

    Activity(**{
    "name": "work_prostitute_female",
    "label": "work_prostitute",
    "money_gain": {"attributes": ["charm", "fitness", "knowledge"], "mult": (2,)},
    "duration": 4,
    "rooms": "alley",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            Or(
                And(IsFlag("job_day", "prostitute"),
                    IsTimeOfDay("morning", "afternoon"),
                    ),
                And(IsFlag("job_night", "prostitute"),
                    IsTimeOfDay("evening", "night"),
                    ),
                ),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })


    Event(**{
    "name": "random_work_events_female",
    "label": "random_work_events_female",
    "priority": 0,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsActivity("work_bakery_female",
                       "work_bookstore_female",
                       "work_camgirl_female",
                       "work_church_female",
                       "work_clothesshop_female",
                       "work_coffeeshop_female",
                       "work_electronic_female",
                       "work_flowershop_female",
                       "work_gym_female",
                       "work_homelessshelter_female",
                       "work_jewelrystore_female",
                       "work_maidcafe_female",
                       "work_model_female",
                       "work_nightclub_female",
                       "work_pornstar_female",
                       "work_prostitute_female",
                       "work_pub_female",
                       "work_sexshop_female",
                       "work_stripclub_female",)),
        ],
    "chances": 20,
    "do_once": False,
    "once_week": True,
    "quit": False
    })

    Activity(**{
    "name": "ask_for_a_job_office_female",
    "duration": 0,
    "icon": "askforjob",
    "rooms": "office",
    "conditions": [
        Or(
            IsDone("dwayne_female_event_05"),
            IsDone("dwayne_female_event_05_alt"),
            IsDone("mike_job_offer_female")
            ),
        HeroTarget(
            IsGender("female"),
            IsFlag("job_day", False),
            ),
        ],
    "display_name": "Ask for a job",
    "once_month": True,
    "label": "ask_for_a_job_day_office",
    })

    Activity(**{
    "name": "work_office_female",
    "label": "work_office",
    "money_gain": {"attributes": ["charm", "knowledge"], "mult": (1.3,)},
    "duration": 4,
    "rooms": "office",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_day", "office"),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })

    Activity(**{
    "name": "quit_job_office",
    "duration": 0,
    "icon": "quitjob",
    "rooms": "office",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsFlag("job_day", "office"),
            ),
        ],
    "display_name": "Quit your office job",
    "once_day": True,
    "label": "quit_office_job",
    })

label ask_for_a_job_day_office:
    if (("dwayne_female_event_05" in DONE or "dwayne_female_event_05_alt" in DONE) and not hero.flags.office_fired_dwayne) and ("mike_job_offer_female" in DONE and not hero.flags.office_fired_mike):
        menu:
            "Work for Dwayne":
                bree.say "Dwayne, I thought about your job proposition and I'd like to apply."
                dwayne.say "Sure, the job is yours."
                $ hero.flags.office_boss = "dwayne"
                $ hero.flags.dwayne_office_job_delay = TemporaryFlag(True, 5)
            "Work for [mike.name]":
                bree.say "[mike.name], I thought about your job proposition and I'd like to apply."
                mike.say "Sure, the job is yours."
                $ hero.flags.office_boss = "mike"
    elif ("dwayne_female_event_05" in DONE or "dwayne_female_event_05_alt" in DONE) and not hero.flags.office_fired_dwayne:
        bree.say "Dwayne, I thought about your job proposition and I'd like to apply."
        dwayne.say "Sure, the job is yours."
        $ hero.flags.office_boss = "dwayne"
        $ hero.flags.dwayne_office_job_delay = TemporaryFlag(True, 5)
    elif "mike_job_offer_female" in DONE and not hero.flags.office_fired_mike:
        bree.say "[mike.name], I thought about your job proposition and I'd like to apply."
        mike.say "Sure, the job is yours."
        $ hero.flags.office_boss = "mike"
    $ game.flags.job_day = game.room
    return

label work_office:
    show chibi work
    "I work on a few minor contracts."
    hide chibi
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    return

label quit_office_job:
    if hero.flags.office_boss == "dwayne":
        bree.say "Dwayne, I wanna quit my job!"
        dwayne.say "Ha! You're loss!"
    elif hero.flags.office_boss == "mike":
        bree.say "[mike.name], I wanna quit my job!"
        mike.say "Alright [hero.name]..."
    $ hero.flags.office_boss = None
    $ game.flags.job_day = False
    return

label work_camgirl:
    show chibi camgirl
    "I love feeling all those eyes on me..."
    hide chibi
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    return

label quit_camgirl_job:
    "I don't want to expose myself anymore."
    if game.flags.job_day == "bedroom4":
        $ game.flags.job_day = False
    if game.flags.job_night == "bedroom4":
        $ game.flags.job_night = False
    return

label work_church:
    show chibi church
    "It feels so good to work in the house of god."
    hide chibi
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    return

label work_clothesshop:
    show chibi clothesshop
    "I feel like I am bringing those people's souls out by helping them choose their style."
    hide chibi
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    $ game.flags.worked_clothesshop += 1
    return

label work_flowershop:
    show chibi flowershop
    "The flowers are so beautiful and give everyone so much joy."
    hide chibi
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    return

label work_homelessshelter:
    show chibi homelessshelter
    "It feels so good to help those lost souls."
    hide chibi
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    return

label work_jewelrystore:
    show chibi jewelrystore
    "I feel so blessed working surrounded by all those beautiful things."
    hide chibi
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    return

label work_model:
    show chibi model
    "Thanks to my beautiful body I can make some money easy."
    hide chibi
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    return

label work_nightclub:
    show chibi nightclub
    "That job is like being paid to party!"
    hide chibi
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    return

label work_pornstar:
    show chibi pornstar
    "I get to fuck studs with big cocks and be paid to do it?!"
    "Hell yeah!"
    hide chibi
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    return

label work_prostitute:
    show chibi prostitute
    "I hope the next one will be cute & clean at least..."
    hide chibi
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    return

label work_pub:
    show chibi pub
    "That job is like being paid to party!"
    hide chibi
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    return

label work_university:
    show chibi teaching
    "I teach and mold some young minds like putty!"
    hide chibi
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    return

label work_stripclub:
    if Room.find(game.room).get_present_npcs():
        call give_lapdance_female from _call_give_lapdance_female
        if _return != "canceled":
            $ game.flags.story_hasworked = True
            $ game.flags.hasworked = TemporaryFlag(True, "day")
            return
    show chibi stripper
    "Thanks to my beautiful body I can make some money easy."
    hide chibi
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    return


label random_work_events_female:
    if renpy.has_label(f"random_work_events_{game.room}"):
        call expression f"random_work_events_{game.room}" from _call_expression_376
    return

label random_work_events_camgirl:
label random_work_events_bedroom4:
    $ r = randint(1, 5)
    if r == 1:

        "I'm well into my streaming session today, and the numbers are looking good."
        "And I'm more than happy with the donations that have been trickling in too!"
        "In fact, I'm thinking about wrapping things up for the day and going offline."
        "But then I see that a message has popped up in my chat window."
        "And it's a message that has dollar symbols in it too!"
        bree.say "Oh..."
        bree.say "Hello there..."
        bree.say "What's this?"
        "Old man" "Hello there, my dear!"
        "Old man" "You want to earn some serious cash?"
        "I chuckle and shake my head at the message."
        "I have no idea how he wants me to earn the money."
        "But I need to play nice if I want to find out."
        bree.say "Oh, really?"
        bree.say "You got a nice, big wad for me, huh?"
        "I make a point of winking a the webcam."
        "Old man" "Oh yes, my dear!"
        "Old man" "Two hundred big ones!"
        "Old man" "But first you have to do something for me."
        "I can't keep my eyes from lighting up at the mention of the money."
        "That amount would make today a very profitable one!"
        "All I have to do is keep him sweet and find out what he wants."
        bree.say "And what would that be?"
        "I smile as I wait for his response."
        "And all the time I'm hoping it's something easy."
        "Old man" "That bottle behind you, my dear."
        "Old man" "Do you see it?"
        "A little puzzled, I turn and see the bottle he's referring to."
        bree.say "Erm..."
        bree.say "Yeah, I see it."
        "Old man" "The neck looks nice and long - wide too."
        "Old man" "I'll pay you two hundred dollars to use it like a dildo!"
        "I can't help my eyes going wide at the mere suggestion."
        "And the chat box goes pretty crazy too."
        "Seems like it's an equal split in there."
        "Half of the watchers are encouraging me to do it."
        "And the other half are calling the guy asking a pervert!"
        menu:
            "Use the bottle":
                "Urgh..."
                "The last thing I want to do right now is use a bottle to do..."
                "Well, to do that!"
                "But the whole idea of this job is to please the people watching."
                "And to do that, I have to be prepared to do the stuff they want to see."
                "So I force a smile onto my face and nod."
                "Then I reach out for the bottle..."
                bree.say "Hmm..."
                bree.say "Now that you mention it..."
                bree.say "That bottle does look pretty good!"
                "What follows is not the proudest moment of my life."
                "In fact I'd pay more then two hundred dollars to have it erased from my memory!"
                "But somehow I manage to get through it."
                "The whole time thinking about the money it's making for me."
                $ hero.money += 200
                $ hero.fun -= 5
            "Don't do it":
                "Eww!"
                "There's no way I'm doing what that creep wants."
                "I might be a camgirl, but that's just gross!"
                "But I have to style it out for the sake of my image."
                "So I smile and shake my head."
                "At the same time I wag my finger at the camera."
                bree.say "Uh-uh..."
                bree.say "What kind of a girl do you think I am?"
                bree.say "I don't use anything down there that's not made for it."
                bree.say "And I don't use cheap shit either."
                bree.say "But maybe if some kind person were to buy me something expensive..."
                "The teasing and hinting seems to have the desired effect."
                "Pretty soon I have more than a few watchers promising to by me a real sex-toy."
                "I guess that's what they mean about life giving you lemons!"
                $ hero.money += 50
                $ hero.charm += 2
    elif r == 2:

        "I'm just chatting away with the watchers as usual."
        "Trying to make myself laugh at their lame jokes."
        "And passing the time by thinking about other things."
        "When I notice that one of them is more active than the others."
        "It's a username that I think I recognise from other streaming sessions."
        "One of the watchers that's almost always online when I stream."
        bree.say "Hey, Edgelord1991..."
        bree.say "Always good to see you in my chat!"
        "The guy must be right there and watching me."
        "Because he responds almost before I'm done speaking!"
        "Edgelord1991" "Hey, [hero.name]..."
        "Edgelord1991" "I never miss a stream that you do."
        "Edgelord1991" "I'm legit your number one fan."
        bree.say "Aw!"
        bree.say "That's so sweet of you to say!"
        bree.say "I love all my fans!"
        "Edgelord1991" "None of them love you as much as I do!"
        "Edgelord1991" "And I want to prove it to you as well."
        "Hmm..."
        "That's starting to sound a little worrying."
        "But I guess I should indulge him a little longer."
        bree.say "Oh really?"
        bree.say "And how would you go about doing that?"
        "Again the guy responds in an instant."
        "Edgelord1991" "Agree to meet me in person."
        "Edgelord1991" "Do that and I'll show you!"
        "Oh dear - this guy just crossed a line."
        "There's no way I'm going to meet up with him."
        "Not in public, private or anywhere!"
        "And I need to let him know that."
        menu:
            "Shoot the guy down":
                "I have to send a clear message to this guy."
                "And I need to make sure that he understands it."
                "Him and everyone else on that watches my streams."
                bree.say "Ha!"
                bree.say "You're joking, right?"
                bree.say "I'm a camgirl, not a prostitute, buddy!"
                bree.say "You watch me."
                bree.say "We chat about fun stuff."
                bree.say "And if you're generous, you send me donations."
                bree.say "But that's as far as it goes."
                bree.say "You either remember that, or else I block your ass!"
                "And with that, I make a point of chatting with other watchers instead."
                "Hopefully the guy will get the message."
                $ hero.charm -= 4
            "Let the guy down gently":
                "I have to send a clear message to this guy."
                "And I need to make sure that he understands it."
                "But I have to let him down gently too."
                bree.say "Now, now..."
                bree.say "You know that's not fair!"
                bree.say "You have to share me with everyone else."
                bree.say "I'm a camgirl, remember?"
                bree.say "You watch me."
                bree.say "We chat about fun stuff."
                bree.say "And if you're generous, you send me donations."
                bree.say "But what happens in stream stays on stream!"
                "I smile and make a point of chatting to some of my other watchers."
                "Hopefully the guy will get the message."
                $ hero.charm += 2
                $ hero.fun += 2
    elif r == 3:

        "I'm trying my best to make today's stream as fun as possible."
        "And for the most part, it's working out really well."
        "But there's someone in the chat-window that keeps distracting me."
        "One watcher that seems to be trying to throw a spanner in the works."
        "They keep asking me dumb questions and mocking other watchers."
        "But trolls are nothing new to me, and I've mostly been ignoring them."
        bree.say "So..."
        bree.say "I think a change of clothes is what I need."
        bree.say "I want to relax a little, yeah?"
        bree.say "Maybe even take a nap after I'm done streaming."
        bree.say "So what should I wear?"
        "I have a bunch of outfits strewn around my room."
        "All of them carefully chosen and all of them in view of the webcam."
        "And at first I get the usual kind of suggestions from my watchers."
        "Some of them want me to wear a cute set of pyjamas."
        "Some of them want to see me in more revealing night-wear."
        "But then the troublesome watcher chimes in with their suggestion."
        "Guy" "I hear you look good in really slobby stuff."
        "Guy" "Like sweatpants with a busted waistband."
        "Guy" "And a t-shirt that has ketchup stains on it!"
        "I open my mouth to tell the watcher off."
        "But then my gaze falls on the laundry hamper in the corner."
        "It's well out of shot of the webcam, I made sure of that."
        "And yet I can see a pair of sweatpants and a T-shirt."
        "They match the description the watcher used."
        "And I was only wearing them around the house last night!"
        "That watcher must be [mike.name] and Sasha!"
        menu:
            "Call [mike.name] and Sasha out":
                "I'm not going to let those jerks get away with this!"
                "I'm onto a good thing here, and I'm making money too."
                "So I raise an eyebrow and shake my head."
                bree.say "Oh, what?"
                bree.say "Like the ones I wear around the house, [mike.name!u]?"
                bree.say "Or the ones that I just put in the washing machine, SASHA?"
                "I let out a laugh and shake my head."
                bree.say "Don't worry, guys."
                bree.say "It's just my loser housemates trying to be clever."
                bree.say "And you know what we do to trolls, don't you?"
                bree.say "We splat them with the ban-hammer!"
                "I follow this up by banning the offending profile."
                "And then I do my best to get back on with the stream."
                $ hero.fun += 1
            "Fight fire with fire":
                "I'm not going to let those jerks get away with this!"
                "I'm onto a good thing here, and I'm making money too."
                "So I raise an eyebrow and shake my head."
                bree.say "Oh, you know who wears REALLY gross stuff?"
                bree.say "My housemates, that's who!"
                bree.say "Like, I live with this guy called [mike.name]."
                bree.say "And he never, literally never, changes his underwear."
                bree.say "You can smell him coming halfway across the house!"
                bree.say "Oh, and don't forget Sasha too."
                bree.say "She wears the same dirty, stinky T-shirts home from band practice."
                bree.say "And she leaves her panties around the bathroom when she's done with them too!"
                "I watch as the offending profile goes quiet, then disappears from my chat."
                "So I smile a little more sincerely."
                "And then I do my best to get back on with the stream."
                $ mike.love -= 5
                $ sasha.love -= 5
    elif r == 4:

        "I'm having a great time on my stream today, really enjoying the chat."
        "My watchers are being a lot of fun, and not too creepy for a change!"
        "In fact, most of them seem happy to chat about my hobbies and interests."
        "So we've been chatting about books, movies and TV shows most of the time."
        "But then one of them seems to spot all the gaming stuff I have in my room."
        "Gamerdude2020" "Hey, those are some cool posters!"
        "Gamerdude2020" "And I can see a couple of rare action figures on your shelf too!"
        "I take a look back over my shoulder."
        "And then I turn my head back to the webcam with a smile."
        bree.say "Aw!"
        bree.say "Thank you."
        bree.say "I'm pretty proud of my collection!"
        "Gamerdude2020" "Oh yeah?"
        "Gamerdude2020" "Did one of your boyfriends buy you that stuff?"
        "The question kind of catches me off guard."
        "So much so that I can't help frowning."
        bree.say "Erm...no."
        bree.say "Why would you think that?"
        bree.say "I collected them myself."
        "Gamerdude2020" "No way."
        "Gamerdude2020" "Videogames aren't for girls."
        "Gamerdude2020" "They just pretend to like them to impress guys!"
        "I can feel myself getting really annoyed with this guy."
        "He actually thinks that I only pretend to be into games to impress men?!?"
        "What a jerk!"
        menu:
            "Put the guy in his place":
                "I'm not going to let him talk to me like that."
                "Especially not when he's on MY stream!"
                bree.say "Urgh..."
                bree.say "How are there still guys like you around?"
                bree.say "I thought this was the twenty-first century!"
                bree.say "Don't worry, guys."
                bree.say "It's just some loser trying to be clever."
                bree.say "And you know what we do to trolls, don't you?"
                bree.say "We splat them with the ban-hammer!"
                "I follow this up by banning the offending profile."
                "And then I do my best to get back on with the stream."
            "Make the guy look stupid":
                "I'm not going to let him talk to me like that."
                "Especially not when he's on MY stream!"
                bree.say "Tell me something..."
                bree.say "Have you ever played a videogame with a girl?"
                bree.say "In fact, have you ever played with a girl at all?"
                bree.say "No - I bet you just play with your own joystick, huh?"
                "I pause for a minute as a thought occurs to me."
                bree.say "You know I AM a real gamer girl."
                bree.say "And I just thought of a way to prove it."
                bree.say "So donate if you want me to play games live on here."
                bree.say "Oh, and one more thing..."
                bree.say "If I get enough donations, I'll be playing in my underwear!"
                $ hero.money += 50
                $ hero.morality -= 2
    elif r == 5:

        "I tend to assume that most of my watchers are going to be guys."
        "I mean, they often have silly, macho usernames that kind of give it away."
        "But almost as many of those names are kind of less than specific."
        "So when I get asked a question, I tend to assume the one asking is a guy."
        "Punky" "Hey, [hero.name]..."
        "Punky" "Do you like girls?"
        "I lean in closer to read the question in the chat-window."
        "And I'm already putting on my best alluring giggle."
        bree.say "Hi there, Punky..."
        bree.say "I dunno..."
        bree.say "I have a lot of girls that are friends."
        bree.say "But I don't think that's the kind of girlfriend you mean!"
        "Punky" "Hell no!"
        "Punky" "I wanna know if you're a girl into girls."
        "Punky" "Maybe one that's into girls like me?"
        "I chuckle as I consider my answer."
        menu:
            "Maintain an air of mystery":
                "I want to keep the watcher's interest."
                "But at the same time, I have to do that for everyone else too."
                "I have no problem flirting with girls."
                "But it always pays to keep up an air of mystery."
                bree.say "Oh well..."
                bree.say "I guess that would depend on the girl in question."
                bree.say "That and how nicely she'd be if I let her play with me!"
                "I smile as I see my chat-window light up in response to this."
                "Half of the guys in there are jealous of any girl I'd mess around with."
                "And the other half are desperate to see me messing around with her!"
                $ hero.fun += 2
                $ hero.charm += 2
            "Flirt with the watcher":
                "What have I got to hide here?"
                "Sure, of course I like the idea of being with another girl."
                "This is the twenty first century and I'm one hundred percent liberated."
                "And if anyone watching doesn't like that, they can shove it."
                "I don't want them watching my stream!"
                bree.say "Oh yeah!"
                bree.say "I just LOVE playing with other girls."
                bree.say "They're just as much fun as boys."
                bree.say "Sometimes even more fun!"
                "I smile as I see my chat-window light up in response to this."
                "Half of the guys in there are jealous of any girl I'd mess around with."
                "And the other half are desperate to see me messing around with her!"
                $ hero.fun += 2
                $ hero.morality -= 2
    return

label random_work_events_church:
    $ r = randint(1, 5)
    if r == 1:

        "Oh god...I know this is kind of a cliche."
        "And it's totally wrong to be thinking like this in a church."
        "But Father McGuire is hot."
        "And I mean like SO hot!"
        "I don't know if it's that thing that some older guys have."
        "Like they're a little bit fatherly - but not at all like your actual Dad."
        "But they make you feel like they could really take care of everything, you know?"
        "And the worst thing us that Father McGuire definitely knows it too!"
        "Like, he keeps coming over and smiling at me."
        "But he does it in a really charming way too!"
        "Father McGuire" "Good morning, [hero.name]."
        "Father McGuire" "You look positively radiant this morning."
        "Father McGuire" "Always a good thing to see you around the church."
        "I fumble with what I'm doing, almost dropping things on the floor."
        bree.say "Ah..."
        bree.say "Oh..."
        bree.say "Good morning, Father..."
        bree.say "I was...I was just..."
        "Without saying a word, Father McGuire steps forwards."
        "He catches what I was about to drop, saving it from hitting the floor."
        "But he's also pressed up against me, his chest against my back."
        bree.say "F...Father!"
        bree.say "What are you doing?!?"
        "Father McGuire" "Ah, [hero.name]..."
        "Father McGuire" "Will you relax a little?"
        "Father McGuire" "I'm just helping you out, that's all."
        "Helping me out?"
        "How does pressing his dick against my ass help me out?!?"
        "I mean...any other time I wouldn't mind a guy like him hitting on me."
        "But isn't he supposed to be a priest?"
        "Like with a vow of celibacy or something?"
        menu:
            "Tell the priest off":
                "I have to put a stop to this, here and now!"
                "How many times have you heard stories about pervert priests?"
                "And they get away with it because nobody stands up or speaks out."
                "So I take a step forwards and turn around."
                "At the same time, I hold up a hand, looking him in the eye."
                bree.say "Father..."
                bree.say "You need to stop right there."
                bree.say "And don't even think about coming any closer!"
                "Father McGuire looks a little shocked at my reaction."
                "I guess he's used to his looks and position getting him his way."
                "But then his face breaks into a charming smile."
                "And I can see that he's trying to smooth things over."
                "Father McGuire" "What are you talking about, [hero.name]?"
                "Father McGuire" "I was only trying to help."
                "Father McGuire" "I think what we have here is a simple misunderstanding."
                "I narrow my eyes, not taking them off him for a second."
                bree.say "Yeah, Father..."
                bree.say "Someone's definitely misunderstood things here!"
                "Father McGuire gives me another one of his charming smiles."
                "But as he turns to go, it doesn't have the same effect on me as before."
                $ hero.morality += 1
            "Flirt with the priest":
                "What the hell am I even complaining about?"
                "I like the look of the guy and he's only doing what comes naturally."
                "And working here in the church is pretty boring."
                "Having his attention could really spice up the job!"
                bree.say "Oh, Father..."
                bree.say "You have such quick reflexes."
                bree.say "And such strong hands too!"
                "As I say this, I push my ass backwards."
                "And I can instantly tell that he's pretty excited right now!"
                "Father McGuire lets out a low, knowing laugh."
                "And the sound of it is enough to start melting me inside."
                "Father McGuire" "Ah, [hero.name]..."
                "Father McGuire" "I'm always happy to help."
                "Father McGuire" "All you have to do is ask..."
                "I can feel his hands moving over my body as he says all of this."
                "Don't get me wrong, he's not groping me or anything like that."
                "Instead he's stroking and caressing me in a gentle, suggestive manner."
                "And then he steps backwards, beginning to walk away."
                "Which leaves me standing there, my heart beating at double-speed."
                "And the memory of his touch still making my body tingle."
                $ hero.morality -= 1
    elif r == 2:

        "Turns out working in a church is a little like working in retail."
        "Yeah, I know - sounds like a weird thing to say, right?"
        "But you spend a lot of time going around the place straightening it up."
        "And you soon realise that you have to keep an eye on the valuables too."
        "Like they have a donation plate in the church, right out in the open."
        "Anyone that wants to can come along and drop cash onto it."
        "And the idea is that it's for a good cause."
        "So nobody should be inclined to steal it."
        "But we all know that humans are going to be human, don't we?"
        "Sure enough, as I walk past the donation plate, I spot something."
        "Or to be more specific, I spot someone."
        "There's a kind of edgy-looking guy hanging around it."
        "He keeps looking around, like he's checking for any witnesses."
        "Right now he's in that period of grace where he could be perfectly innocent."
        "Like he might be pausing to say a prayer before dropping in his donation."
        "I keep as quiet as I can, watching him intently."
        "And when I see his hand reach out, I notice that it's empty."
        "Oh yeah, he's definitely taking, rather than giving."
        "And it looks like I'm the only one that's spotted him doing it too."
        "Urgh...damn it."
        "Why couldn't the priest have caught him in the act?"
        "This kind of thing is beneath my pay-grade!"
        "I glance around for a moment, sizing up the situation."
        "The door to the church is open, as always."
        "And the guy has a clear path to run out of here right now."
        "But then I look back at him and notice how desperate he looks."
        "His clothes are pretty dirty, hanging off him."
        "Plus he looks like he hasn't showered in quite a while."
        "What am I going to do about this guy?"
        menu:
            "Step in and challenge the man":
                "I can't just let him steal from the church."
                "That money should be going to a good cause."
                "But maybe there's another way to help the guy?"
                "I take a step towards him."
                "And I cough to catch his attention."
                bree.say "Ahem..."
                bree.say "You really shouldn't be doing that."
                "At the sound of my voice, the man drops the money."
                "And he turns around to see who's caught him in the act."
                "Oddly, I don't feel frightened as he does so."
                "The man looks so tired and desperate that I actually feel sorry for him."
                "Shady guy" "I...I..."
                "Shady guy" "Please..."
                "Shady guy" "I need this!"
                "The sound of our conversation draws the attention of the priest."
                "Father McGuire walks over, his face friendly and his voice calm."
                "Father McGuire" "What's the matter, [hero.name]?"
                bree.say "It's this man, Father..."
                "As I pause, the man looks at me, desperation in his eyes."
                "I guess he's expecting me to tell the priest he was stealing."
                bree.say "I think he could really use someone to talk to."
                bree.say "Someone to listen to his problems and help him."
                "Father McGuire nods kindly and puts a hand on the man's shoulder."
                "Instantly he seems to sag and I can see tears in his eyes."
                "As the priest leads him away, I feel like I did the right thing."
                "Father McGuire should be able to help the man."
                "And far more than a handful of stolen money ever could."
                $ hero.morality += 2
            "Let the man steal from the donation plate":
                "I know that the money on the plate is destined for good causes."
                "The church helps out all kinds of charities in the city."
                "But what is this guy if he's not a charity case?"
                "And why shouldn't some of that money help him out?"
                "With that in mind, I turn my back and walk away."
                "I make sure to keep my distance from the donation plate for a while."
                "And when I finally pass that way again, the man is gone."
                "But so is most of the money that was on the plate."
                "Now the priest is standing over it, stroking his chin."
                "At the sound of me approaching, he turns to regard me."
                "Father McGuire" "Oh, [hero.name]..."
                "Father McGuire" "I'm afraid we've been the victims of a minor theft."
                "Trying to look surprised, I walk over to the priest."
                bree.say "Oh really, Father?"
                "Father McGuire" "I'm afraid so."
                "Father McGuire" "Someone told me they saw a man run out of the church."
                "Father McGuire" "And when I came to check, money had been taken from the donation plate."
                bree.say "That's terrible, Father!"
                bree.say "But I'm sure I didn't see anything myself."
                "The priest nods a little sadly."
                "Father McGuire" "It's not the money that bothers me, [hero.name]."
                "Father McGuire" "If the man was desperate, then he's welcome to it."
                "Father McGuire" "After all, it is meant to help those in need."
                "Father McGuire" "But I would have liked the chance to talk to him."
                "Father McGuire" "Because often the problems a person has are deeper than you know."
                "Father McGuire" "And money is not going to solve them."
                "I watch as the priest walks away shaking his head."
                "And I can't help thinking..."
                "I might have done the right thing in the short-term."
                "But the wrong thing in the long-term."
                $ hero.morality -= 2
    elif r == 3:

        "I'm really starting to feel like I'm settling in at the church."
        "I get on with most of the people here pretty well."
        "And the work is just on the right side of boring to for time to pass quickly."
        "But one thing that does take me by surprise is the way people like to gossip here!"
        "I mean, when I started, I was kind of worried that everyone would be uptight."
        "I thought that they'd all be sticking to the rules in the good book."
        "But they talk behind each other's backs all the time!"
        "And it seems everything is fair game for gossip too."
        harmony.say "[hero.name]..."
        harmony.say "Did you hear about Father McGuire?"
        "I look up at the sound of Harmony's voice."
        "She's a girl that volunteers here, a real pillar of the community type."
        "But it sounds like she's a sucker for gossip too!"
        bree.say "Ah...no, Harmony."
        bree.say "I don't think I did."
        "Harmony waves me closer, looking this way and that as she does so."
        harmony.say "Okay, [hero.name]..."
        harmony.say "You have to swear on your favourite bible, yeah?"
        harmony.say "Not to tell a soul that you heard this from me, right?"
        "I nod slowly for the sake of hearing what she has to say."
        "I don't actually think I own a copy of the bible myself."
        "But that's not going to stop me hearing some juicy gossip."
        bree.say "You got it, Harmony."
        bree.say "I won't tell a soul."
        harmony.say "Well..."
        harmony.say "One of the female parishioners was telling me..."
        harmony.say "That during her confession, she admitted to adultery."
        harmony.say "And Father McGuire asked for...details!"
        bree.say "Of who she was cheating with?"
        harmony.say "No, [hero.name] - of what position they did it in!"
        "Now, look - I'm no prude myself."
        "But even I find that more than a little shocking."
        "And it could mean serious trouble if that news gets out."
        "So what should I do?"
        menu:
            "Tell Harmony off for gossiping":
                "I guess this is the very reason that you're not supposed to spread rumours and gossip."
                "And isn't there a lot of stuff about that in the bible too?"
                "Harmony's always telling people how they should be good and moral."
                "But right now, she sounds like a total hypocrite!"
                bree.say "Hmm..."
                bree.say "The woman that told you all this, Harmony..."
                bree.say "Did she give you any proof that it went down that way?"
                "Harmony looks surprised by my question."
                "She blinks and then shakes her head."
                harmony.say "Well...no, [hero.name]."
                harmony.say "Not really."
                "I nod at this and then press Harmony further."
                bree.say "And did you confront Father McGuire?"
                bree.say "You know, ask for his side of the story?"
                "Harmony shakes her head again."
                harmony.say "N...no!"
                harmony.say "Of course not!"
                bree.say "Hmm..."
                bree.say "So you're just spreading rumours about him?"
                bree.say "Do you think that's what Jesus would do?"
                "Harmony stares down at her feet and her cheeks flush red."
                harmony.say "I...I guess not."
                harmony.say "I should go, [hero.name]."
                harmony.say "I have a lot of stuff to think about."
                "I watch as Harmony hurries away."
                "And I hope that I just did the right thing."
                $ hero.morality += 1
            "Thank Harmony for the gossip":
                "Ah, what am I even worrying about?"
                "Everyone gossips and they do it all the time too."
                "Why should a church be any different?"
                "And it's not like Father McGuire was breaking the law or anything."
                "I mean, that vow of celibacy must be pretty tough to live with!"
                bree.say "Oh my!"
                bree.say "Who'd have thought he'd do that?"
                bree.say "And in the confessional as well!"
                "Harmony nods eagerly at my amazement."
                "And I can see the delight in her eyes at my reaction."
                harmony.say "I know, I know..."
                harmony.say "To think that we might have a scandal our hands."
                harmony.say "Right here in our own church!"
                "Part of me feels like it's wrong to be gossiping like this."
                "But another part of me is kind of relieved that it's happening."
                "Because it makes me feel like I'm being accepted as part of the church."
                harmony.say "Now you keep an eye out, [hero.name]."
                harmony.say "And don't let Father McGuire get you on your own either!"
                bree.say "Don't worry, Harmony - I won't!"
                bree.say "And thanks again for warning me."
                "Harmony nods and smiles."
                "Then she hurries off, presumably to pass on the gossip to someone else."
    elif r == 4:

        "I'm just pottering about the church, trying to look busy."
        "And that's when Father McGuire appears out of nowhere."
        "He looks more than a little flustered, which is unusual for him."
        "And as soon as he spots me, he hurries over."
        "Father McGuire" "Ah, [hero.name]..."
        "Father McGuire" "I'm glad I found you!"
        bree.say "Oh..."
        bree.say "Hello, Father..."
        bree.say "Did you need me for something?"
        "The priest nods and begins to explain himself."
        "Father McGuire" "Yes, [hero.name]..."
        "Father McGuire" "It's almost time for mass, you see."
        "Father McGuire" "And we're all out of wine for the communion!"
        bree.say "Oh dear - that doesn't sound good."
        "Father McGuire" "No, [hero.name] - it's a disaster!"
        "Father McGuire" "That's why I need you to go buy some more wine for me, okay?"
        "The request catches me totally off-guard."
        "I always thought they got the wine from somewhere special."
        "I never expected to be able to just go out and buy it."
        bree.say "But, Father..."
        bree.say "How will I know what kind to buy?"
        bree.say "Does it have to be expensive?"
        bree.say "Or come from a specific place?"
        "The priest shakes his head."
        "Father McGuire" "Oh no, [hero.name]!"
        "Father McGuire" "It can be any kind of wine."
        "Father McGuire" "It only becomes special once I've blessed it."
        "I nod and hurry out of the church, headed for the nearest liquor store."
        "And when I burst in there, I grab the first bottle of wine I see."
        "I mean, he did say any wine would do."
        "So what does it matter?"
        menu:
            "Choose red wine":
                "As soon as I get back to the church, I hand over the bottle."
                "The priest doesn't look at the label for as much as a second."
                "Instead he holds it up to the light, studying the contents."
                bree.say "Erm..."
                bree.say "You said any wine was okay, Father."
                bree.say "Why are you looking at it like that?"
                "Father McGuire" "Oh, it's fine, [hero.name]."
                "Father McGuire" "After you left, something struck me."
                "Father McGuire" "I assumed you'd know I wanted red wine and not white."
                "Father McGuire" "And luckily for me, I was right!"
                "I can't help smiling as the priest hurries off with the wine."
                "Now that he mentioned it, I did kinda know that the wine should be red."
                "But I was in such a hurry when I went to the store that I just grabbed anything."
                "Lucky for me that I chose the right one!"
                $ hero.knowledge += 1
            "Choose white wine":
                "As soon as I get back to the church, I hand over the bottle."
                "The priest doesn't look at the label for as much as a second."
                "Instead he holds it up to the light, studying the contents."
                bree.say "Erm..."
                bree.say "You said any wine was okay, Father."
                bree.say "Why are you looking at it like that?"
                "Father McGuire" "Erm...it's my fault, [hero.name]."
                "Father McGuire" "After you left, something struck me."
                "Father McGuire" "I assumed you'd know I wanted red wine and not white."
                "Father McGuire" "And this definitely isn't red!"
                "Father McGuire" "But don't worry - I can still make it to the liquor store myself."
                "Father McGuire" "Maybe I can bless the wine in the car or something..."
                "I have a nervous grin on my face as the Priest hurries off."
                "Now that he mentioned it, I did kinda know that the wine should be red."
                "But I was in such a hurry when I went to the store that I just grabbed anything."
                "And it looks like I really screwed up!"
                $ hero.money -= 5
    elif r == 5:

        "I'm just minding my business in the church, pretending to work as usual."
        "But the sound of a commotion on the other side of the building catches my attention."
        "And I can't help being drawn towards the source of the hubbub with genuine interest."
        "As I get closer I can see Father McGuire and various other members of the staff."
        "They're all crowded around one of the statues of saints that are dotted around the place."
        "I'm just about to ask what all the fuss is about."
        "But the priest speaks up before the question is out of my mouth."
        "Father McGuire" "Praise be to the almighty!"
        "Father McGuire" "It's a genuine miracle!"
        "At this, everyone else stars shouting and praising the almighty too."
        "And they throw their arms up in the air at the same time."
        "Which allows me to see the object of their attention."
        "At first I can't see what all the fuss is about."
        "It's just another one of the statues that I must have dusted, like a hundred times over."
        "It's of a pretty grumpy-looking old man who looks like he's pointing at someone in disapproval."
        "But as I look closer, I can see something new."
        "There's a couple of streams running down the cheeks of the statue."
        "And they pretty much make it look like the thing's been crying."
        bree.say "Ooh..."
        bree.say "That's weird!"
        bree.say "It looks like the statue's been..."
        "Father McGuire" "CRYING!"
        "Father McGuire" "Yes, [hero.name] - it's a miracle!"
        "Father McGuire" "The statue of Saint Lupercus is weeping!"
        "Father McGuire" "Our humble church has been blessed with a miracle!"
        "I don't know what it is that makes me look up at that exact moment."
        "Maybe it's everyone throwing their hands in the air."
        "Or maybe I just have an unconscious hunch about all of this."
        "And that's when I see the air-conditioning unit on the wall above the statue."
        "It looks pretty beat-up, and I see water dripping from the bottom."
        "And right onto the head of the statue."
        "What's going on here?"
        "How come nobody else noticed that?"
        menu:
            "Point out the dripping above the statue":
                "Urgh...I really don't want to do this."
                "But there's never going to be a better time than right now."
                "So here goes..."
                bree.say "Erm..."
                bree.say "I don't suppose anyone looked up there, did they?"
                bree.say "You know, where there's that dripping A/C unit?"
                "Everyone stops dead, and all eyes fall on me."
                "For a moment I honestly think they're going to riot."
                "I don't know, maybe burn me at the stake for being a non-believer."
                "But then Father McGuire looks up at where I'm pointing."
                "Father McGuire" "Oh..."
                "Father McGuire" "Oh I see..."
                "Father McGuire" "Thank you, [hero.name]."
                "Father McGuire" "I was just about to go and call the Bishop."
                "Father McGuire" "And that would have been very embarrassing."
                "Everyone looks disappointed, but they can see the A/C unit too."
                "And I'm sure they're as relieved as the priest under it all."
                $ hero.money += 2
                $ hero.morality += 1
            "Do not point out the dripping above the statue":
                "Hmm...this is a bit of a sticky situation."
                "One of them's bound to notice the drip sooner or later."
                "But they all seem so happy about the supposed miracle."
                "It feels really wrong to burst their bubble."
                "So I just nod and smile."
                bree.say "Erm..."
                bree.say "Yay?"
                bree.say "I guess?"
                "Father McGuire" "You guess right, [hero.name]!"
                "Father McGuire" "This will really put us on the map!"
                "Father McGuire" "I'm off to call the Bishop!"
                "Oh dear - that doesn't sound good."
                "But it's too late for me to change my mind now."
                "All I can do is sit back and watch."
                $ hero.morality -= 1
    return

label random_work_events_clothesshop:
    $ r = randint(1, 5)
    if r == 1:

        "I'm doing my turn looking after the changing booths at the back of the store."
        "It mainly just involves counting the clothes going in and giving the customer a tag."
        "The tag has the same number as the amount of clothes they take in there."
        "Then you check the two numbers still match when they come out again."
        "You see - easy!"
        "And if someone is trying to steal something, you don't tackle them yourself."
        "You just hit the alarm and call for security, then let them handle it."
        "Today things are going pretty smoothly for me, no incidents or issues."
        "I'm just folding up some clothes to be taken back onto the shop floor."
        harmony.say "Hey!"
        "At the sound of someone's voice, I look up from what I'm doing."
        "And then I see a girl's face, peeking out from behind one of the curtains."
        bree.say "Erm..."
        bree.say "Are you talking to me?"
        "The girl nods and beckons me over with a roll of her eyes."
        harmony.say "Sorry to be a pain."
        harmony.say "But I wondered if you could help me out?"
        "I walk over with a smile on my face, trying to look helpful."
        "She probably wants whatever she's trying on in a different size."
        "That's the most common request that you get in this part of the store."
        bree.say "No problem, madam."
        bree.say "What can I do for you?"
        "The girl glances to the left and right, like she's checking we're alone."
        "And I can see that she's already blushing as she asks the question."
        harmony.say "Look...I don't normally ask anyone to do this..."
        harmony.say "But could you maybe...give me an honest opinion?"
        harmony.say "I'm buying an outfit for a date."
        harmony.say "And I REALLY want to make a good impression!"
        "Hmm...that doesn't sound too bad."
        bree.say "Sure thing!"
        bree.say "Let me see what you're thinking, okay?"
        "The girl nods and slowly draws back the curtain."
        show harmony date embarrassed with dissolve
        "And the first thing that hits me is a smack of jealousy!"
        "She's one of those girls with a naturally curvaceous figure."
        "You could never say she was thin, but she's certainly not overweight."
        "Actually, she'd look right at home in one of those classical paintings you see!"
        "But the dress that she has on - oh my!"
        "It's covering up everything she has to show off."
        harmony.say "So?"
        harmony.say "What do you think?"
        menu:
            "Compliment Harmony":
                "I keep the smile on my face as I answer the question."
                "And I also decide to keep my opinions to myself."
                "I'm just a sales assistant here, not a style consultant."
                bree.say "I think that looks good on you."
                bree.say "It's stylish without showing off too much."
                show harmony happy
                "I can almost feel the sense of relief from the girl."
                "She lets out a long sigh and nods her head."
                harmony.say "Oh, thank you!"
                show harmony normal
                harmony.say "I thought it was the right choice."
                harmony.say "But I have no idea about these kind of things!"
                hide harmony with dissolve
                "I keep on smiling as the girl closes the curtain on me."
                "If she's happy with the way she looks, then that's all that matters."
                "And if her date doesn't appreciate that, then he doesn't deserve her."
                $ hero.money += 5
                $ hero.fun += 1
            "Suggest Harmony to show off more flesh":
                "I purse my mouth and make a point of studying her closely."
                "I could just smile and tell her that she looks fine in that dress."
                "But I hate to see a figure like that going to waste!"
                bree.say "Don't take this the wrong way, yeah?"
                bree.say "But you've got a body to die for!"
                show harmony surprised
                "The girl's eyes go wide at this."
                "And soon her cheeks are burning red."
                show harmony embarrassed
                harmony.say "Oh...oh my!"
                harmony.say "You think I should wear less?"
                bree.say "Trust me, girl - you don't need to wear next to nothing."
                bree.say "Just something that shows off what you've got a little better."
                hide harmony with dissolve
                "The girl nods and then closes the curtain."
                "It feels good to have boosted her confidence in herself."
                "And I hope her date, whoever he is, appreciates what I just did for him!"
                $ hero.morality -= 2
    elif r == 2:

        "I'm working the till, ringing up customer's purchases and taking their payments."
        "And thanks to the fact the store is busy means that I hardly have the chance to catch a breath!"
        "This is supposed to be one of the parts of the job that's boring but simple."
        "All I should have to do is keep right on smiling and scanning the purchases."
        "And that's exactly how it goes, for a short while at least..."
        "Girl" "HEY!"
        "Girl" "What are you doing?!?"
        palla.say "Excuse me?"
        palla.say "Did I ASK you to talk to me?"
        "I look up to see two women in the queue locking glances."
        "The first is glaring at the second, who seems more amused than anything else."
        bree.say "Erm..."
        bree.say "Is there a problem here?"
        "Both of the women look around at me."
        "And just like that, I'm right in the middle of their argument."
        "Girl" "You bet there is!"
        "Girl" "She just pushed her way into the damn queue!"
        "The second girl scoffs at this and shakes her head."
        palla.say "Oh please!"
        palla.say "I have important places to be."
        palla.say "I can't be expected to wait behind all these people!"
        "One of them's supposed to be getting served next."
        "And that means their argument is holding up the entire queue."
        "People behind them are starting to mutter and stare too."
        "I need to do something to defuse the situation."
        menu:
            "Send Palla to the back of the queue":
                "I hate people that think they're better than everyone else."
                "And they only reason they get away with it is because people let them!"
                bree.say "We have a strict policy in this store."
                bree.say "No cutting the line, okay?"
                "The first girl nods and crosses her arms over her chest."
                "But the second shoots me an icy glare."
                palla.say "I don't think I like your tone!"
                palla.say "And I think I'd like to speak to your manager too!"
                "I can't help letting out a chuckle of laughter."
                bree.say "Wait a minute..."
                bree.say "You said you were in too much of a hurry to queue."
                bree.say "But now you have time to hang around and complain to my manager?"
                bree.say "I wish you'd make up your mind!"
                "The rude girl blinks as she realises that I've got her."
                "And I can hear the people behind her starting to laugh too."
                "She shakes her head, trying to recover a measure of dignity."
                palla.say "I...I..."
                palla.say "I don't have time for this!"
                "As if to make the point, she throws the clothes she was buying on the ground."
                "And then she storms straight out of the store without looking back."
                "I can't help smiling as she leaves, feeling a warm glow inside of me."
                $ hero.morality += 1
                $ hero.fun += 1
            "Serve Palla quickly to get rid of her":
                "I hate people that think they're better than everyone else."
                "But I'm at work right now, so I have to bite down on my anger."
                "What's best is to just get rid of her as soon as possible."
                bree.say "You don't seem to be buying much, madam."
                bree.say "Let me just ring them up for you - super quick, okay?"
                "She gives me a superior smile and hands over her purchases."
                "After which I hurry to get her served and out of my hair."
                "Once she's gone, the other woman lets out a sigh."
                "Girl" "You really shouldn't have done that, you know?"
                "Girl" "All you did there was validate her privilege!"
                "I feel the disapproval being directed my way."
                "But all I can do is nod my head and apologise."
                bree.say "I'm sorry, madam."
                bree.say "I hope the rest of your day goes well."
                $ hero.fun -= 3
    elif r == 3:

        "When I started working here they were very specific about dealing with shop-lifters."
        "Keep an eye out for anything suspicious, but don't confront anyone you suspect."
        "The place is full of cameras and there are security guards around too."
        "Which is exactly what I keep telling myself when I see a shifty guy in the store."
        "He's hanging around, trying a little too hard to look like he's just browsing."
        "Plus, whenever I look up, he's always in the women's section of the store."
        "I could just assume that he's looking for a gift to surprise his girlfriend."
        "Or that he's secretly trying to pick something out for himself."
        "But part of me just knows that he's up to something."
        "Suddenly I see him turn and start to make for the door."
        "I make to follow, but then I remember my training."
        "What I really should be doing is alerting security."
        "That and leaving the whole thing alone myself."
        "But he's about to make it out of the door."
        "There's no way that security's going to be able to catch him!"
        "Do I tackle the guy, or let him go?"
        menu:
            "Tackle the suspicious man":
                "Oh hell - screw waiting for security!"
                "I wait until the guy's about to pass me."
                "And then I leap towards him."
                "He's much bigger than me, but I take him by surprise."
                "Maybe that's the only reason that I manage to knock him off his feet."
                "Together we tumble onto the floor in a tangle of limbs."
                "Shady guy" "Hey!"
                "Shady guy" "What are you doing?!?"
                bree.say "I saw what you were doing, buddy!"
                bree.say "You're not going anywhere until security shows up!"
                "The guy looks at me in amazement."
                "But then he laughs and pulls something out of his pocket."
                "When he holds it up, I see that it's his ID."
                "Shady guy" "I am security!"
                "Shady guy" "I'm an undercover store detective."
                bree.say "Oh..."
                bree.say "Oh my god!"
                bree.say "I'm so sorry!"
                "As we both get to our feet, the detective waves it off."
                "Shady guy" "Don't worry about it."
                "Shady guy" "Happens all the time."
                "Shady guy" "Now if you'll excuse me..."
                "He points towards the door."
                "And I nod, stepping aside."
                "The he runs off, probably chasing a real shoplifter!"
            "Do nothing":
                "Screw getting involved in that!"
                "Security are paid to deal with it, not me."
                "I watch as the guy rushes out of the store and disappears."
                "And after a little time passes, I think about calling security."
                "But then I see him walking back into the store, bold as you like!"
                "Shady guy" "Excuse me..."
                "The man pulls something out of his pocket."
                "When he holds it up, I see that it's his ID."
                "Shady guy" "I'm an undercover store detective."
                "Shady guy" "And I just chased down a shoplifter."
                "Shady guy" "Looks like she'd been stealing from your store."
                "I feel a sudden rush of relief."
                "Because I'd have looked like a complete moron tackling the actual store detective!"
                bree.say "Really?"
                bree.say "Wow..."
                bree.say "Sorry I just stood back and didn't help!"
                "The man shakes his head at this."
                "Shady guy" "Oh no, you did just the right thing."
                "Shady guy" "I always get people grabbing me, mistaking me for a thief myself!"
                "Shady guy" "Just let your manager know we'll be getting in contact, yeah?"
                "I nod and smile, then watch as he leaves the store."
                "Once he's gone, I let out a sigh of relief."
                "Because I'm thankful for being spared public embarrassment."
                $ hero.money += 5
    elif r == 4:

        "One of the weird little quirks of this job is that they give you an actual pay cheque."
        "I mean, it's not an actual cheque, just a piece of paper that says what you've earned."
        "But it still feels strange in an age where you do everything else online using your phone."
        "One thing it has done though it make me actually take the time to read the thing."
        "I know roughly what I make an hour here, and how long I've been working every month."
        "So I also have a pretty good handle on what I should be getting after taxes."
        "Which is why my jaw drops when I check out the bottom line of the latest pay cheque."
        "How in the hell can it be that low?!?"
        "It should be way higher than that!"
        "I know my mental arithmetic isn't the best."
        "But there's no way I could have got it that wrong."
        "I start scrutinising every line of the pay cheque, looking for any mistakes."
        "I can see that there are quite a lot of deductions at the bottom."
        "And most of them seem to have names that make no sense to me at all."
        "Manager" "[hero.name]..."
        "Manager" "Are you okay?"
        "At the sound of the manager's voice I jump a little."
        "I was so engrossed that I didn't even spot them walking over."
        bree.say "Ah..."
        bree.say "Sorry!"
        bree.say "I was just checking out my pay cheque for last month."
        "Manager" "Oh?"
        "Manager" "Is there something wrong with it?"
        "I'm about to tell the manager about my suspicions."
        "But then I find myself pausing."
        "What if I'm just reading this thing wrong?"
        "I'll make myself look like I think I'm being underpaid."
        "And an idiot if I really have made a mistake."
        "But on the other hand, I'm down a serious chunk of money here."
        "If there is an error, I can't afford to let it slide."
        menu:
            "Explain your concerns to the manager":
                "What's the problem with asking about my concerns?"
                "It's not like they can fire me for being clued up on what I'm earning."
                bree.say "Well..."
                bree.say "You see, I thought I knew roughly what I was earning every month."
                bree.say "But there's a lot of deductions on here that I don't understand."
                "The manager frowns and leans in to take a closer look."
                "Manager" "Hmm..."
                "Manager" "What's going on here?"
                "Manager" "Do you mind?"
                "I shake my head and hand over the pay cheque."
                "And I can already see the manager's head shaking."
                "Manager" "No..."
                "Manager" "This doesn't look right at all."
                "Manager" "Leave it with me, [hero.name]."
                "Manager" "I'll sort this out with head-office."
                "I nod and watch as they walk away."
                "Hopefully I just made the right decision."
                "And I'll see the results in an amended pay cheque pretty soon."
                $ hero.money += 25
            "Say nothing":
                "Sure, I need the money."
                "But I need the job too!"
                "Maybe I can sort this out by calling someone?"
                "I doubt the store manager handles this kind of thing anyway."
                bree.say "No..."
                bree.say "It's okay, really."
                bree.say "Just going through it, that's all."
                "The manager nods and smiles at this."
                "Manager" "Okay, [hero.name]..."
                "Manager" "But you be sure to tell me if there's something amiss."
                "Manager" "Everything's done on computers these days."
                "Manager" "But that doesn't mean mistakes aren't made."
                "With that, the manager walks off again."
                "Which leaves me alone and wondering if I did the right thing after all."
                $ hero.fun -= 2
                $ hero.money -= 5
    elif r == 5:

        "I'm back on the till again, putting in my shift."
        "And everything seems to be going well for once."
        "It's not too busy and most of the customers are being nice."
        "That means my mind's already starting to wander."
        "I'm thinking about what I'm going to do when I get off work."
        "And of course that means I'm not really paying attention to reality."
        "Working on auto-pilot, I take the money, open the till and hand over the change."
        "All of which seems to work until I hear an impatient coughing sound."
        "Customer" "Ahem!"
        bree.say "Huh?"
        "Customer" "Excuse me..."
        "Customer" "But you seem to have made a mistake!"
        "I blink and shake my head, snapping back to reality."
        "The only problem is that it doesn't help me understand what's actually going on."
        "Customer" "Are you even listening to me?"
        "Customer" "I paid with a fifty just now."
        "Customer" "But you gave me change for a twenty."
        bree.say "I did?"
        "Customer" "Yes, you did!"
        "I glance down at the notes in the customer's hand."
        "And then I look back at the till again."
        "It certainly looks like I rang it up as a twenty."
        "But there is a fifty in the till, so I could have made that mistake."
        "Plus I was distracted at the time."
        "The customer obviously wants me to give her the money."
        "But I feel a little trepidation about doing that."
        "Because what if she's trying to rip me off?"
        menu:
            "Reimburse the customer":
                "I glance around the customer to see the state of the queue."
                "And unfortunately for me, it's starting to get pretty long."
                "I need to get this sorted out and the queue moving again."
                "And the easiest way to do that is to just bite the bullet."
                bree.say "Okay, okay..."
                "I reach into the till and make up the difference."
                "Then I hand the money over to the customer with a forced smile."
                "She doesn't return the gesture, just grabs the money and leaves."
                "Which I suppose is something that I should be thankful for."
                "I try to push the whole thing out of my mind as I serve the next customer."
                "But I can't help thinking about how quickly that customer was out the door."
                "Almost like she wanted to get away before anyone questioned what was happening..."
                "Ah well, it's done now."
                "I guess the worse they can do is dock my wages if the till is down."
                $ hero.fun -= 2
            "Tell her to see with the manager":
                "I glance around the customer to see the state of the queue."
                "And unfortunately for me, it's starting to get pretty long."
                "I need to get this sorted out and the queue moving again."
                "And the easiest way to do that is to send it on up the chain."
                bree.say "Would you mind waiting a moment, madam?"
                "As I say this, I press a button on the counter."
                "Customer" "Why?"
                "Customer" "What are you doing?"
                bree.say "Just calling my manager over."
                "Customer" "Don't do that!"
                "Customer" "Can't you just take it out of the till?"
                "I shake my head as I scan the store for the manager."
                bree.say "No, madam..."
                bree.say "Only my manager has the authority to do that."
                "The customer's starting to look nervous now."
                "She glances at the door and then shakes her head."
                "Customer" "You know what...forget about it."
                "Customer" "I don't have time for this!"
                "I watch as she hurries out of the store before the manager arrives."
                "All I can do is shake my head and start to serve the next customer."
                "Maybe she was trying to rip me off after all."
                $ hero.money += 5
    return

label random_work_events_flowershop:
    $ r = randint(1, 5)
    if r == 1:

        "I smile as a new customer walks into the store and heads towards the counter."
        "Being all happy and helpful to anyone that comes in here is kind of a cliche."
        "But I'm feeling pretty upbeat today, so I don't even have to force it."
        bree.say "Good day, Sir..."
        bree.say "How can I help you?"
        "The man looks at me with what I can now see are red-rimmed and watery eyes."
        "Then he opens his mouth like he's trying to say something in response."
        "But what comes out isn't actual words."
        with vpunch
        "Customer" "Achoo!"
        "I can't help jumping backwards at the sound of his sneeze."
        "It's just so loud and unexpected, and it catches me off-guard."
        bree.say "Oh my!"
        bree.say "Erm...bless you?"
        with hpunch
        "Customer" "Achoo...achoo...achoo!"
        "I watch helplessly as the man sneezes again and again."
        "And even when he seems to have stopped, he still looks pretty awful."
        "His eyes are streaming and I can see that he's struggling to breathe."
        bree.say "Erm..."
        bree.say "Are you okay?"
        "Customer" "No...allergies...pollen!"
        "Customer" "Very...very bad!"
        bree.say "Maybe you should step outside then?"
        "Customer" "No...need flowers...anniversary!"
        "Customer" "Wife...loves them!"
        "Oh my god - that's so romantic!"
        "He's buying his wife flowers despite his allergies!"
        menu:
            "Show me what you want, I'll be quick":
                "I nod and begin to pull together all the stuff I need."
                bree.say "Point to what you want, Sir."
                bree.say "And I'll try to be as quick as I can!"
                "The man nods, trying as best he can to cover his face with a hand."
                "He points and then I point to confirm what he wants."
                "And a nod or shake of the head lets me know if I'm right."
                "Soon enough we've put together a pretty decent bouquet."
                "I put a wrapping of clear cellophane around it to keep in the pollen."
                "Then he pays as fast as humanly possible, leaving me a small tip, and ducks out the door."
                $ hero.money += 2
            "Show me what you want from outside":
                "I nod and begin to pull together all the stuff I need."
                bree.say "Go wait outside, Sir."
                bree.say "Then point to what you want in the window, okay?"
                "The man nods, trying as best he can to cover his face with a hand."
                "Then he ducks out of the door and stands in front of the window."
                "He points and then I point to confirm what he wants."
                "And a nod or shake of the head lets me know if I'm right."
                "Soon enough we've put together a pretty decent bouquet."
                "I put a wrapping of clear cellophane around it to keep in the pollen."
                "I take his payment, along with a decent tip, at the door, and then he hurries away with his flowers."
                $ hero.money += 5
    elif r == 2:

        "My nose twitches as a familiar smell wafts into the store."
        "I can't quite place it until I look up and around for the source."
        "And then I see a guy's just walked into the shop."
        "I know you shouldn't stereotype people, but the smell has to be from him."
        "Because he looks like the kind of guy to smoke 'herbal' cigarettes."
        "If you know what I mean?"
        "I watch as he spends a good few minutes shuffling around the place."
        "And it looks like he's trying to find something specific."
        "But at the same time, he's also trying not to look suspicious."
        "Which obviously has the exact opposite effect."
        "In the end I walk over to see if I can help."
        bree.say "Ahem..."
        "Customer" "Whoa!"
        "Customer" "Don't sneak up on a guy like that!"
        bree.say "Oh..."
        bree.say "Sorry, Sir."
        bree.say "I just wondered if you needed any help?"
        "The guy takes a quick look around."
        "As if he's worried somebody might overhear our conversation."
        "Customer" "Um...okay..."
        "Customer" "I wanted to buy...like..."
        "Customer" "Some poppies!"
        bree.say "Huh?"
        bree.say "You want poppies?"
        "The guy nods eagerly."
        "And as he does so, I realise what he's trying to do."
        "He must think that he can get high on the seeds!"
        "Like, make opium out of it or something!"
        menu:
            "Here's what you ask for":
                "I try as best I can to keep from laughing."
                "And at the same time, I wave for him to follow me."
                bree.say "Here, Sir..."
                bree.say "Are these the kind you're looking for?"
                "Customer" "I dunno..."
                "Customer" "Are they real poppies?"
                bree.say "One hundred percent the genuine article."
                "Customer" "Then they're what I want!"
                "I don't say another word about it."
                "I just wrap up as many poppies as the guy can afford."
                "Then he hurries out, trying to hide them from sight."
                "I watch him go, wondering if he can actually do it."
                "And if I just became an accessory to an actual crime."
                "But I kind of doubt it!"
                $ hero.morality -= 1
            "That's not how it works":
                "I try as best I can to keep from laughing."
                bree.say "You know..."
                bree.say "I don't think you can actually do it!"
                "Customer" "Wha...what do you mean?"
                "Customer" "Do what?"
                bree.say "I don't think you can get opium from the seeds."
                bree.say "I mean, when you see that kind of thing in the movies..."
                bree.say "They have like whole fields full of the stuff."
                "The guy's eyes go wide with amazement."
                "Like he can't believe I'm onto him."
                "Customer" "Erm..."
                "Customer" "That's not what they're for!"
                "I shrug, and don't say another word about it."
                "I just wrap up as many poppies as the guy can afford."
                "Then he hurries out, trying to hide them from sight."
                "I watch him go, wondering if he can actually do it."
                "And if I just became an accessory to an actual crime."
                "But I kind of doubt it!"
                $ hero.morality += 1
    elif r == 3:

        "I look up and smile as a girl walks over to the counter."
        show cassidy casual normal
        "She's pretty well-dressed, and looks more than a little lost."
        "So this could be a good chance to offer a customer some help."
        "Not to mention getting a decent sale under my belt."
        bree.say "Hello there..."
        bree.say "How can I help you?"
        "The girl's head spins around at the sound of my voice."
        "And the look on her face is instantly surly."
        cassidy.say "Urgh..."
        cassidy.say "I guess so."
        cassidy.say "I just need some flowers for my mother."
        "I nod and gesture towards the nearest flowers."
        bree.say "As you can see, we have a lot of choice."
        bree.say "But if you tell me what the occasion is..."
        bree.say "Then I can suggest something that might be appropriate."
        cassidy.say "Like...is that ANY of your business?"
        show cassidy annoyed
        cassidy.say "Just sell me some stupid flowers already!"
        cassidy.say "What about those?"
        "I do the best I can to ignore how rude the girl is being."
        "And instead I walk over to the flowers she's pointing at."
        bree.say "Good choice."
        bree.say "You can see the price right there."
        cassidy.say "You have to be kidding!"
        show cassidy angry
        cassidy.say "How can you charge so much?"
        cassidy.say "I could just go outside and pick flowers for free!"
        menu:
            "Take a deep breath":
                "I force a smile onto my face."
                "And I push down the urge to slap the girl's face too."
                bree.say "You could do that."
                bree.say "But then you'd have to go wading through the dirt and mud."
                bree.say "And picking them would be no good for your nails either."
                "The girl's face contorts into an expression of disgust."
                cassidy.say "Eww!"
                show cassidy annoyed
                cassidy.say "That sounds disgusting!"
                bree.say "Exactly!"
                bree.say "That's what we're here for."
                bree.say "Like, you could make yourself a coffee."
                bree.say "But why do that when you can pay a barista, right?"
                cassidy.say "Right!"
                show cassidy normal
                "The girl's mood improves as I wrap up her flowers and scan her card."
                "And she strides out of the shop like she was the one that made the point, not me!"
                $ hero.energy += 1
            "Do it yourself then":
                "I let out a snort of annoyance with the girl."
                "And I plant my balled fists on my thighs."
                bree.say "You could do that."
                bree.say "But you'd just end up with a bunch of weeds."
                bree.say "And your mother would be less than impressed."
                "The girl's face changes, her expression becoming thoughtful."
                cassidy.say "Hmm..."
                show cassidy normal
                cassidy.say "I guess I would be pretty mad if that happened to me."
                cassidy.say "There's nothing worse than a cheap gift!"
                bree.say "Exactly!"
                bree.say "That's what we're here for."
                "The girl's mood improves as I wrap up her flowers and scan her card."
                "And she strides out of the shop like she was the one that made the point, not me!"
                $ hero.fun += 1
    elif r == 4:


        aletta.say "Excuse me..."
        show aletta casual normal
        "The tone of the voice is confident and demanding."
        "So much so that it makes me sit up and pay attention."
        bree.say "Huh?"
        aletta.say "Oh, you are awake after all!"
        aletta.say "I'm looking for some plants to decorate my office."
        aletta.say "This one looks the part, very impressive."
        aletta.say "But I need to know how to care for it."
        "I glance at the plant she's talking about."
        "But then I realise it's one of the more exotic ones we stock."
        "I know all about the common ones in the place."
        "But I'm still learning about the rare and expensive ones."
        bree.say "Ooh..."
        bree.say "I'm not sure."
        bree.say "I'm pretty new here, so I'll have to get the manager."
        "This doesn't seem to go down well with the uppity woman."
        show aletta annoyed
        aletta.say "So you're basically admitting you're incompetent?"
        bree.say "HEY!"
        "Manager" "What's going on here, [hero.name]?"
        "Manager" "Do you need a hand?"
        "Before I can say anything, the woman cuts in."
        show aletta angry
        aletta.say "The problem is that your employee knows nothing!"
        menu:
            "Screw you bitch!":
                bree.say "Excuse me!" with vpunch
                bree.say "I already explained that I'm new here."
                bree.say "And I offered to fetch the manager for you!"
                "The manager holds up a hand to defuse the situation."
                "Manager" "Don't worry about it, [hero.name]."
                "Manager" "I'll handle this."
                hide aletta
                "I walk away, fuming at the way I've been treated."
                "And a little later, the manager finds me for a chat."
                "Manager" "That's one of our more difficult customers right there!"
                "Manager" "I understand how she can make you mad, [hero.name]."
                "Manager" "But it's best to just leave her to me in future, okay?"
                "All I can do is nod in agreement."
                "At least the manager was understanding."
                "Another person might have told me off for speaking to a customer like that."
                "They might even have fired me for it!"
            "Let the manager handle it":
                "I open my mouth to say something in response."
                "But then I realise how angry I'm feeling right now."
                "Whatever comes out of my mouth is likely to land me in trouble."
                "So I close it again and stay silent."
                "The manager holds up a hand to defuse the situation."
                "Manager" "Don't worry about it, [hero.name]."
                "Manager" "I'll handle this."
                "I walk away, fuming at the way I've been treated."
                hide aletta
                "And a little later, the manager finds me for a chat."
                "Manager" "That's one of our more difficult customers right there!"
                "Manager" "I understand how she can make you mad, [hero.name]."
                "Manager" "So well done for walking away."
                "I nod and smile, feeling vindicated by the manager's words."
                "Looks like I managed to avoid doing the wrong thing back there."
        $ hero.knowledge += 1
    elif r == 5:

        "Feeling like I'm being watched, I glance up from what I'm doing."
        "And I literally jump backwards when I see a guy staring at me."
        "He's pressed up against the window, hands by his eyes to see inside."
        "And the worst part is that he looks like some kind of criminal too!"
        show danny
        "I mean seriously, this guy looks like an extra from an action movie."
        "The sleazy guy in the sleazy bar who gets his ass kicked by the hero."
        "Before I can do a thing, he's opening the door and stepping inside."
        danny.say "Ah..."
        danny.say "Like..."
        danny.say "Hey there!"
        "I force a smile onto my face and try on to look scared."
        "If he wants the contents of the till, then he can have them!"
        bree.say "Erm..."
        bree.say "Hello, Sir!"
        "But rather than demanding money, the guy looks around the store."
        danny.say "So..."
        danny.say "You guys sell flowers, right?"
        bree.say "That's right - we're a florist!"
        danny.say "Good, good...because I need some."
        danny.say "For my girl, you see - not for me!"
        "I can't help starting to smile a little."
        "The big, scary tough guy wants to buy flowers!"
        "It's actually quite sweet!"
        bree.say "How about some roses, Sir?"
        bree.say "They're fifty dollars for a dozen right now."
        danny.say "HOW MUCH?!?" with vpunch
        menu:
            "We have other flowers":
                bree.say "It doesn't have to be roses, Sir."
                bree.say "We have some carnations right over here."
                bree.say "They're less expensive."
                bree.say "But they're just as pretty."
                "The scary man looks at the prices."
                "And I see relief on his face."
                danny.say "Yeah..."
                danny.say "My bitch'll love those!"
                danny.say "Not that I'm cheap, you know?"
                "I shake my head as I wrap up his order."
                bree.say "Of course not, Sir."
                bree.say "I'm sure these are for a very lucky lady..."
            "There's this other shop":
                bree.say "Hmm..."
                bree.say "There is an all-night garage around the corner."
                bree.say "They have bunches of flowers for sale too."
                bree.say "And I shouldn't say this..."
                bree.say "But they ARE a lot cheaper than ours..."
                "And I see relief on his face."
                danny.say "Yeah..."
                danny.say "That sounds better."
                danny.say "My bitch'll never know the difference!"
                "I nod my head as he hurries out of the door."
                bree.say "Of course, Sir."
                bree.say "I'm sure she's a very lucky lady..."
        $ hero.charm += 1
    return

label random_work_events_alley:
    $ r = randint(1, 5)
    if r == 1:

        "I'm just going about finishing up the last task I got given."
        "When I see one of the regulars at the shelter shuffling over."
        "He's a sorry case, even compared to the others we help out."
        "And that's why I can't help feeling particularly sorry for him."
        bree.say "Hey there..."
        bree.say "Are you okay?"
        bree.say "Do you need some help?"
        "The man looks around, like he's afraid of being overheard."
        "But eventually he finds the courage to speak up."
        "Shady guy" "I..."
        "Shady guy" "I don't like doing this..."
        "Shady guy" "But could you spare me some cash?"
        "Shady guy" "Not much!"
        "Shady guy" "Whatever change you have would be enough."
        "He looks at me with pleading eyes."
        "And I guess he knows what an awkward position he just put me in too."
        menu:
            "Give the man your change":
                "Urgh..."
                "They told me not to do this when I started working here."
                "I had the whole lecture about what these guys will spend it on."
                "But all the people we help here know about that stuff."
                "So he must be desperate to even ask."
                "Now it's my turn to look around as I pull out my change."
                bree.say "Here you go."
                bree.say "Just don't tell anyone I did this, okay?"
                "The man gratefully takes the money, nodding profusely."
                "Then he hurries away, leaving me to wonder if I made the right decision."
                $ hero.morality += 1
                $ hero.money -= 5
            "Refuse to give":
                "Is this guy for real?"
                "They told me not to do this when I started working here."
                "I had the whole lecture about what these guys will spend it on."
                "And I'll be in big trouble if they find out I gave him a penny!"
                bree.say "Oh come on!"
                bree.say "You know what the policy is here."
                bree.say "And you know it'll be my ass if I break it!"
                "The man looks disappointed."
                "But he nods and hurries away all the same."
                "And I'm left to wonder if I did the right thing after all."
                $ hero.morality -= 1
    elif r == 2:

        "It must be getting towards the end of my shift by now."
        "At least I hope it is, as I'm tired and my feet are aching!"
        "I got to pull out my phone, intending to check the time."
        "But then I start to panic as I can't feel it in my pocket!"
        "And that's because it's not there."
        "Trying to keep calm, I check every pocket I have."
        "But it's nowhere to be found."
        "I glance around, wondering if I could have left it anywhere."
        "And that's when I remember how dodgy some of the people in here look."
        "I kind of feel like I'm jumping to conclusions."
        "But what if one of them stole it?"
        "I mean, what if one of them is a pick-pocket?"
        menu:
            "Keep your suspicions to yourself":
                "No, no, no - I can't think like that."
                "I need to give these people a fair chance."
                "So I keep my suspicions to myself and say nothing."
                "I'll just have to report the phone missing."
                "Who knows, maybe it'll turn up in the lost and found?"
                "A moment later, I see someone dash out of the door."
                "And part of me can't help wondering."
                "Was that they guy who took my damn phone?"
                $ hero.morality += 1
                $ hero.fun -= 1
            "Demand to know who stole your phone":
                "I feel so mad right now."
                "This place is a charity for god's sake."
                "We're all trying to help these people."
                "And this is how they repay that kindness?!?"
                bree.say "HEY!"
                bree.say "Which one of you low-lives stole my phone?!?"
                "Everyone turns to look in my direction."
                "Save for one guy who drops something and runs out the door."
                "I hurry over and pick it up, seeing that it's my phone."
                "Then I shoot a glare at the rest of them."
                "Which seems to do the trick."
                $ hero.morality -= 1
    elif r == 3:

        "I'm on duty at the soup kitchen today, ladling out bowl after bowl."
        "I do the best I can to keep smiling as the people shuffle past me."
        "But there's so many of them that it's starting to become a blur!"
        "I'm not saying all homeless people look the same."
        "But I could swear I've seen some of these guys in the line before."
        "In fact, I'm pretty sure some of them have soup in their beards!"
        "And breadcrumbs too!"
        "One or two of the guys in the queue seems to notice my expression."
        "And they share a sly laugh as they shuffle towards the front of the queue."
        "That all but confirms it for me."
        "They're sneaking back into the queue for seconds!"
        menu:
            "Call them out":
                "I know these guys are hungry."
                "But we're trying to help as many people as possible."
                "What if someone has to go without because of this?"
                bree.say "HEY!"
                bree.say "No coming back for another bowl!"
                bree.say "That way there won't be enough to go around!"
                "The sniggering guys suddenly look pretty guilty."
                "And everyone else is staring at them too."
                "Being called out seems to work."
                "As they leave the queue with their heads hung low."
                $ hero.morality += 1
            "Let it go":
                "I should probably call those guys out."
                "But what if they're still hungry?"
                "I mean, they are only getting a bowl of soup each!"
                "So I shake my head and ignore the situation."
                "Soon enough the last of the soup is gone."
                "In the end, we have to turn some people away."
                "Which makes me feel a little guilty."
                "And I wonder if I made the right decision after all."
                $ hero.morality -= 1
    elif r == 4:

        "I keep seeing this creepy-looking guys hanging around the shelter."
        "He doesn't look like one of the homeless people we get in here."
        "In fact, he looks more like a stereotypical bad guy from a movie."
        "You know the kind - they hang around in scummy bars and ride big motorbikes, yeah?"
        "I try to keep an eye on him without being noticed."
        "But this time I see him handing a little plastic bag over to one of the regulars."
        "And then he gets handed a wad of used notes in return."
        "Is that...are those..."
        "Oh god, he's a drug-dealer!"
        "And what's worse, he's noticed me watching him!"
        danny.say "Hey!"
        danny.say "What are you lookin at, huh?"
        "The guy starts walking towards me."
        "And he doesn't look friendly at all!"
        menu:
            "Stand up to Danny":
                "I stand my ground as the guy comes towards me."
                "And I plant my hands firmly on my hips."
                bree.say "I saw what you were doing just now."
                bree.say "You were selling that man drugs!"
                "The fact that I've come right out and said it seems to affect the guy."
                "He stops in his tracks and looks around, noting that people are staring."
                danny.say "Whu...what are you talkin about?"
                danny.say "I didn't do nothin!"
                bree.say "Then you won't mind me calling the cops, will you?"
                bree.say "They can sort out what you are and aren't doing here!"
                "The man shakes his head, and then makes a dash for the door."
                "Leaving me to breath a sigh of relief."
                "Hopefully he won't be back if he thinks we're onto him."
                $ hero.charm += 1
                $ hero.morality += 1
            "Try to placate Danny":
                "I start backing up as soon as he comes towards me."
                "That and shaking my head as well."
                bree.say "N... nothing..."
                bree.say "Nothing at all!"
                "The man lets out a nasty laugh and nods his head."
                danny.say "Damn right you weren't!"
                danny.say "And don't let me catch you lookin at me again!"
                danny.say "You hear?"
                "I nod and then hurry away as fast as I dare."
                "All the time hoping never to see that guy again."
                $ hero.charm -= 2
    elif r == 5:

        "I'm serving up the soup for a long line of hungry homeless guys."
        "But when I look up to see who's next, I stop lifting the ladle."
        "And that's because I swear I recognise the next guy in line."
        bree.say "Hey..."
        bree.say "Wait a minute..."
        bree.say "Don't I know you?"
        "The guy's starting to look nervous."
        "Glancing this way and that while visibly sweating."
        jack.say "Erm..."
        jack.say "No, I don't think so!"
        bree.say "I think I do!"
        bree.say "Aren't you [mike.name]'s friend?"
        bree.say "Jack, isn't it?"
        jack.say "No, no, no!"
        jack.say "My name's...KYLE!"
        jack.say "That's it - Kyle, definitely not Jack!"
        menu:
            "Shrug it off":
                "I shrug and shake my head."
                bree.say "Huh!"
                bree.say "That's weird..."
                bree.say "You look just like him!"
                "I ladle the guy some soup and he hurries away."
                "And I make a mental note to ask [mike.name] about it when I get home."
                "That is if I don't get distracted and forget all about it."
            "Call Jack out":
                "I lean in closer and glare at him."
                bree.say "Quit it, Jack!"
                bree.say "I know it's you!"
                "Jack shakes his head, panic in his eyes."
                jack.say "Okay, okay - it's me!"
                jack.say "Just promise not to tell anyone about this, please?"
                bree.say "What are you doing here, Jack?"
                bree.say "Last time I checked, you weren't on the streets!"
                jack.say "No, [hero.name] - but I AM poor!"
                jack.say "I was just trying to save money, that's all!"
                bree.say "That's SO wrong, Jack!"
                bree.say "I'll promise to keep quiet on one condition."
                bree.say "That you never show your face in here again."
                bree.say "Got it?!?"
                "Jack nods, then turns and runs out of the place."
                "Leaving me shaking my head in sheer amazement."
                $ hero.morality += 1
    return

label random_work_events_jewelrystore:
    $ r = randint(1, 5)
    if r == 1:

        "I'm always being told that you have to be discreet in this job."
        "It's like, sure, they want you to be nice and encourage people to buy stuff."
        "But the stuff in here is so expensive that you can't do the hard sell thing."
        "They say that when people are spending so much money, pressure doesn't help."
        "So you kind of have to use your judgement as to when and when not to offer advice."
        "But right now I think I can see a guy that definitely needs my help."
        "He's younger than our average customer, not as well-dressed either."
        "In fact, he looks like he's ready to bolt out of the store any moment!"
        bree.say "Good day, Sir..."
        bree.say "Is there anything that I can help you with?"
        "The guy jumps at the sound of my voice."
        "And for a moment I think I did the wrong thing coming over."
        "Customer" "Oh..."
        "Customer" "Please don't sneak up on me like that!"
        "I didn't think I had."
        "But I choose to ignore the statement."
        bree.say "Sorry, Sir."
        bree.say "Were you looking for anything in particular?"
        "Customer" "Y...yeah..."
        "Customer" "I need something to impress a girl, you know?"
        "Customer" "Problem is, I don't have much money."
        "Customer" "And everything in here is so expensive!"
        "Hmm...I can sympathise with being broke."
        "But this is a jewellery store, so what did he expect?"
        menu:
            "Price is not that important":
                bree.say "Okay, Sir..."
                bree.say "I'm going to let you in on a little secret."
                "The guy looks at me in genuine surprise."
                "Customer" "A secret?"
                "Customer" "What do you mean?"
                "I smile as I begin to explain myself."
                bree.say "You can spend all the money you have on jewellery."
                bree.say "But if this girl is worth your time, that won't really impress her."
                "The guy blinks and shakes his head."
                "Customer" "It won't?!?"
                "Customer" "But I thought girls liked that kind of thing!"
                bree.say "Oh, we do, we do..."
                bree.say "But it won't make a girl like YOU."
                bree.say "If she's nice, then the jewellery won't change her impression of you."
                bree.say "And if she's not, then she'll likely see what else she can squeeze you for."
                "Customer" "Really?!?"
                "Customer" "That's terrible!"
                bree.say "I'm afraid that's just how it is."
                bree.say "So come over here and let me show you some of the cheaper stuff we sell."
                bree.say "Trust me, she'll know it's not the best."
                bree.say "But if she likes it, that'll be because she likes you."
                bree.say "And if she doesn't..."
                "Customer" "Okay, okay!"
                "Customer" "I think I'm starting to get it."
                "I can see that huge boost to my sales targets disappearing into the distance."
                "But at least I know that I'm doing the right thing."
                $ hero.morality += 1
            "The more expensive, the better":
                bree.say "You do know that jewellery is like an investment, right?"
                "The guy looks at me in genuine surprise."
                "Customer" "An investment?"
                "Customer" "What does that mean?"
                "I smile as I begin my pitch."
                bree.say "It's like anything in life, Sir."
                bree.say "You get what you pay for."
                bree.say "Take the hit in your wallet and the girl you mentioned is going to be impressed."
                bree.say "Skimp on the expense and she's going to think that you're cheap."
                bree.say "Spend the money and then you'll reap the profits of your investment."
                "The guy looks nervous, and more than a little sweaty."
                "But he nods his head."
                "Customer" "I get it."
                "Customer" "The more money I spend, the more she'll be into me."
                "Customer" "Right?"
                bree.say "I wouldn't use those exact words, Sir."
                bree.say "But pretty much."
                "The guy nods and begins to study the more expensive items on sale again."
                "For a moment I wonder if I did the right thing."
                "But then I think of the effect the sale will have on my sales targets."
                "And all of my misgivings seem to fade away."
                $ hero.morality -= 1
                $ hero.money += 5
    elif r == 2:


        "I'm working the till towards the end of my shift and it's pretty quiet."
        "My mind's already wandering as I think of what I'm going to do when I get off work."
        "There's only a couple of customers in the store and most of them seem to be browsing."
        "Only one of them is actually asking to see something from out of a cabinet."
        "And as a colleague is dealing with them, I see no reason to pay any serious attention."
        "A few minutes later, I hear the sound of someone coughing."
        "And I look up to see a customer standing on the other side of the counter."
        bree.say "Oh..."
        bree.say "Sorry, madam!"
        bree.say "I didn't see you there."
        "The woman waves away my apology and gives me a smile."
        "Customer" "Oh don't be silly, dear!"
        "Customer" "There's no need to apologise."
        "Customer" "I just have something that I need you to sort out for me."
        "I nod eagerly, happy to have been let off the hook."
        bree.say "Of course."
        bree.say "How can I help?"
        "The woman pulls out a bag with the store's branding on it."
        "Customer" "I purchased this for a friend a while back."
        "Customer" "But she already has one just like it."
        "Customer" "So I would like a refund, please."
        "I take the bag and check the contents."
        "Inside is a piece of jewellery that I know we sell."
        "And there's even a receipt for the original sale."
        "Problem is, we're not supposed to give refunds."
        bree.say "I'm sorry, madam."
        bree.say "But our store policy is credit or exchange."
        "At this, I see the woman's expression change."
        "Before it was friendly, but now it's becoming irritated."
        "Customer" "I don't think I like your tone, girl!"
        "Customer" "I want a refund, and I want it now!"
        menu:
            "Let see what I can do":
                "I glance around the store as the woman starts to raise her voice."
                "The last thing that I want is to have her cause a scene."
                "That could be enough to get me fired!"
                bree.say "Ah..."
                bree.say "Did I say it was store policy?"
                bree.say "I meant to say refunds are a matter of staff discretion!"
                "The woman smiles as I open the till and take out the money."
                "But then she surprises me by almost snatching the notes out of my hand."
                "I thought she'd at least want to count it, but she just hurries out the door."
                "As I watch her go, I begin to realise that I've seen her before."
                "She looks just like the customer being shown stuff from the cabinet earlier."
                "Suddenly I get a sinking feeling in the pit of my stomach."
                "Oh shit - she must have palmed the item when the cabinet was open."
                "And she had the bag, as well as the fake receipt, ready for it!"
                "This is bad!"
                "How am I going to explain all of this to my manager?!?"
                $ hero.money -= 5
            "I can call the manager":
                "I raise an eyebrow as the woman starts to raise her voice."
                "This is weird, because if she's shopped here before, she should know the policy."
                "And I'd have expected her to be asking to see my manager by now."
                bree.say "I already said I was sorry, madam."
                bree.say "But I don't have the power to give you a refund."
                bree.say "Wait a minute - I'll call the store manager..."
                "Customer" "NO!" with vpunch
                "Customer" "I mean, no..."
                "Customer" "I don't have time for that."
                "Customer" "Just give it to me and I'll come back another time."
                "Now it all makes sense!"
                "She looks just like the customer being shown stuff from the cabinet earlier."
                "Oh shit - she must have palmed the item when the cabinet was open."
                "And she had the bag, as well as the fake receipt, ready for it!"
                "As I lean forwards to hand it over, I press the silent alarm button with my other hand."
                "Luckily for me, the woman doesn't seem to notice, and she hurries towards the exit."
                "Which is when security pounces on her!"
                "Phew - that was lucky."
                "I almost helped someone rob the store!"
                $ hero.morality += 1
    elif r == 3:


        "I'm in the middle of showing a customer what we have on offer in the way of pendants."
        "And that's when he asks me something that I don't think I've ever heard before."
        "Customer" "There are all great, I guess..."
        "Customer" "But do you have anything with an Aquamarine stone?"
        bree.say "Huh?"
        bree.say "You mean the colour?"
        "The man looks up and shakes his head."
        "And I can see his expression is a little frustrated."
        "Customer" "No, no, no!"
        "Customer" "I mean like the stone!"
        bree.say "Oh, I see!"
        bree.say "Sorry, it's just that I've never been asked that before."
        bree.say "People usually want stones like diamonds and rubies, you know?"
        bree.say "Or pearls and stuff like that."
        "Customer" "Well, Aquamarine's my wife's birthstone."
        "Customer" "And I wanted to get her a gift, a personal one."
        "I smile and nod."
        bree.say "Aw!"
        bree.say "That's so sweet!"
        bree.say "We have that kind of thing right over here..."
        "But when I show the man our stock, he doesn't look pleased at all."
        "In fact, he starts shaking his head and muttering."
        "Customer" "Oh no, this is wrong."
        "Customer" "This is all wrong!"
        bree.say "What's the matter, Sir?"
        "Customer" "The months and the stones - they're all messed up!"
        "Customer" "My wife's birthday is in February."
        "Customer" "But it says Amethyst here, not Aquamarine!"
        menu:
            "That's a mistake indeed":
                "I shrug and shake my head."
                "I have no idea if the customer's right or not."
                "But either way, what does it matter to me?"
                bree.say "Oh, really?"
                bree.say "I'll let someone know about the mistake."
                bree.say "Shall I ring up the Aquamarine pendant for you, Sir?"
                "The man nods, looking happy to have been taken at his word."
                "And he keeps right on smiling as I wrap up his purchase then take his money."
                "Once he's gone, I pull out my phone and quickly check it out online."
                "Oops - looks like he was wrong!"
                "It's Amethyst for February."
                "Aquamarine is for March!"
                "Well, he can always come back and change it."
                "I just hope his wife doesn't get too mad!"
                $ hero.money += 5
            "Let me check":
                "I shrug and shake my head."
                "I have no idea if the customer's right or not."
                "So I pull out my phone and quickly check it out online."
                bree.say "Erm..."
                bree.say "Says here it's Amethyst for February."
                bree.say "Aquamarine is for March."
                "The man frowns and leans over to look."
                "Customer" "Well...that must be wrong too!"
                "I chuckle as I proceed to pull up one source after another."
                "And every last one says that he's wrong."
                bree.say "You still want to buy the wrong stone, Sir?"
                "For a moment, I think he's going to ask to see the manager."
                "But then he shakes his head and turns to leave."
                "Customer" "No thank you."
                "Customer" "I think I'll take my custom elsewhere!"
                "With that he storms out of the store."
                $ hero.knowledge += 1
    elif r == 4:


        "A customer comes up to me while I'm cleaning one of the cabinets."
        "He looks a little harassed, so I put on my best smile as I greet him."
        "Maybe I can calm him down if I help him out quickly enough."
        bree.say "Good day, sir."
        bree.say "How can I help you?"
        "The man nods as soon as I speak to him."
        "But he still looks as harassed as ever."
        "Customer" "Yes, yes, yes..."
        "Customer" "I want to look at a watch in the window."
        "Now it's my turn to nod, and I wave for him to follow me."
        "As I walk towards the window, I ask the inevitable question."
        bree.say "Which watch were you wanting to take a look at, sir?"
        "The man frowns at this, like it's a dumb question to ask."
        "Customer" "I already said - the one in the window!"
        bree.say "Erm..."
        bree.say "There are quite a few different watches in there, sir."
        bree.say "It'd help if you could tell me the make?"
        "Customer" "I don't know!"
        bree.say "Or the colour?"
        "Customer" "I have no idea!"
        bree.say "Or where it is in the window - like, which row?"
        "Customer" "I already said - it's the one in the window!"
        bree.say "Well...would you come outside and point at it for me?"
        "Customer" "Urgh..."
        "Customer" "Why are you making this so difficult?"
        "Customer" "The one in the damn window!"
        menu:
            "Let me get it for you":
                "All I can think to do is reach into the window and start showing him watches."
                "And what follows is pretty much like a really bad comedy."
                bree.say "This one?"
                "Customer" "No!"
                bree.say "How about this one?"
                "Customer" "No!"
                bree.say "Is it this one?"
                "Customer" "No!"
                bree.say "Maybe this one?"
                "Customer" "No!"
                "After what feels like forever, the man shakes his head."
                "Customer" "This is ridiculous!"
                "Customer" "Why is it so hard for you to do your job?!?"
                "With that, he turns on his heel and walks out of the store."
                "Leaving me to wonder just what the hell happened."
            "A little help would be great":
                "I know that it's very important to do all I can for the customers."
                "But there's got to be a limit on what I have to put up with."
                "And this is simply ridiculous!"
                bree.say "I'm very sorry, sir."
                bree.say "But I don't know which watch you're talking about."
                bree.say "We sell literally hundreds of different items in this store."
                bree.say "So please, just step outside with me and we can find it together."
                "I'm expecting the customer to admit that he's being stupid."
                "But instead he shakes his head."
                "Customer" "This is ridiculous!"
                "Customer" "Why is it so hard for you to do your job?!?"
                "With that, he turns on his heel and walks out of the store."
                "Leaving me to wonder just what the hell happened."
        $ hero.energy -= 1
    elif r == 5:

        "I'm showing a female customer the rings that we sell."
        "And she seems really keen on dropping a large wad of cash too."
        "So all I should really have to do is smile and let her pick one out."
        "Customer" "Oooh..."
        "Customer" "I REALLY like this one!"
        "I watch as the woman plucks one of the rings from the tray."
        bree.say "Excellent, madam!"
        bree.say "Let me just check if we have that in your size."
        "The woman laughs at this and shakes her head."
        "Customer" "Oh no!"
        "Customer" "Don't be so silly!"
        "Customer" "I'm sure this one will be just fine..."
        "The woman tries to prove her point right away."
        "And I can see that she's already having trouble!"
        menu:
            "Let me do it for you":
                "I reach out and put a gentle hand on the customers own."
                bree.say "I'd rather just check, madam."
                bree.say "I'd be devastated if it got stuck on your finger."
                bree.say "Getting it off could be quite painful!"
                "The woman looks at me in consternation for a moment."
                "But then realisation seems to dawn on her."
                "Customer" "Oh, I suppose you're right."
                "I nod and smile as I proceed to measure the woman's finger."
                "And soon enough she's walking out of the store with her purchase."
                $ hero.morality += 1
            "It fits perfectly":
                "I nod and smile, remembering that the customer is always right."
                "And I watch in silence as the woman proceeds to jam the ring on."
                "Customer" "Oh..."
                "Customer" "Oh dear..."
                "Customer" "I think...I think it's stuck!"
                "The smile on my face is totally fake."
                "Forced on there as I try not to say I told you so."
                bree.say "Oh no, madam!"
                bree.say "Let's see what we can do with that..."
                "As I hurry off to find some liquid soap, I remind myself of something."
                "And that's the fact the customer isn't always right."
                "More often than not, they're one hundred percent wrong!"
                $ hero.morality -= 1
    return


label random_work_events_photostudio:
    $ renpy.dynamic("job")
    $ job = hero.flags.job_day if game.calendar.get_time_of_day() in {"morning", "afternoon"} else hero.flags.job_night
    call expression f"random_work_events_{job}" from _call_expression_510
    return


label random_work_events_model:
    $ r = randint(1, 5)
    if r == 1:

        "I'm flicking through the outfits on the rack for this shoot."
        "And most of it is pretty average stuff, at least nothing noteworthy."
        "But then I come across a shirt and shirt combo, with a tie and knee-socks."
        "The skirt is dangerously short, the shirt sure to show off my midriff."
        "All in all it looks worryingly like a school-girl's uniform..."
        "Photographer" "You like the look of that one, huh?"
        bree.say "Erm..."
        bree.say "It's daring!"
        "Photographer" "Isn't it though?"
        "Photographer" "Great that you like it, [hero.name]."
        "Photographer" "We'll go with that one first today!"
        "Photographer" "Oh, and one more thing..."
        "Photographer" "I need your hair up in bunches, okay?"
        bree.say "Whoa!"
        bree.say "Wait a minute!"
        bree.say "Are you trying to dress me up as a school-girl?!?"
        "Photographer" "What?"
        "Photographer" "No, no, no, [hero.name]!"
        "Photographer" "I'm just trying to capture the youthful energy of that concept."
        "I narrow my eyes at the photographer as they smile and nod."
        menu:
            "Wear the outfit":
                "I let out a sigh and nod my head."
                bree.say "Okay, okay..."
                bree.say "So long as I'm not supposed to be an actual school-girl."
                "I hurry to get into the outfit and fix my hair as requested."
                "And then I do the best I can to get through the next hour of my life."
                "Which involves making sure that I keep things strictly non-sexual."
                "Of course the photographer keeps on urging me to spice things up."
                "But I make a point of refusing to pout or pose in any suggestive way."
                "By the end of the shoot, I can tell they're getting pretty annoyed."
                "But that doesn't stop me sticking to my principles."
                "After all, I'm a fashion model, not a porn star!"
                $ hero.morality += 1
                $ hero.energy -= 1
                $ hero.money += 20
            "Do not wear the outfit":
                "I make a huffing sound and shake my head."
                bree.say "Yeah, well..."
                bree.say "That's not going to work for me."
                "Photographer" "What are you talking about, [hero.name]?"
                bree.say "I have principles and standards, you know!"
                bree.say "Nobody's going to get that I'm not actually supposed to be a school-girl."
                bree.say "All they'll see is me posing in what looks like a school-uniform!"
                "For a moment it looks like the photographer's going to argue with me."
                "That or put their foot down and kick me off the shoot."
                "But then they nod and give in."
                "Photographer" "Okay, Okay..."
                "Photographer" "Forget all about it, [hero.name]!"
    elif r == 2:

        "I've been told that there's going to be a new girl on the shoot today."
        "So I make sure to look out for her so that I can say hi and introduce myself."
        "I remember just how scary my first day in this job was all too well!"
        "That's why I want to be able to meet the new girl and help her settle in."
        "When I finally spot her, she definitely looks the part."
        "She's tall and very pretty, dressed in really stylish clothes too!"
        "Without a second thought, I walk straight up to her."
        bree.say "Hi there..."
        bree.say "I'm [hero.name]..."
        "Without even looking in my direction, the girl holds out her coat."
        palla.say "I don't need to know your name."
        palla.say "Just take my coat and remember my coffee order, and we'll be fine."
        "I make a point of not taking the coat."
        "And I laugh like the whole thing is a joke."
        bree.say "Erm...no!"
        bree.say "I'm not the girl that gets the coffee."
        bree.say "I'm one of the models."
        "The girl looks at me in sheer amazement."
        palla.say "You're kidding?"
        palla.say "They let someone with THAT face be a model?!?"
        menu:
            "Laugh off the insult":
                "I force a smile onto my face and shake my head."
                "After all, I need to be able to get on with this girl."
                "Otherwise the shoot won't go ahead and I won't get paid!"
                bree.say "Ha, ha!"
                bree.say "That's a wicked sense of humour you got there!"
                bree.say "I hope you work as hard as your jokes hit."
                "That said, I turn on my heel and walk away."
                "Because I seriously don't want to hear her response."
                "Maybe if I ignore her insults, we can get through this shoot."
                $ hero.fun -= 1
            "Put Palla in her place":
                "I can't keep my expression from turning mean as I stare at her."
                "And I instantly feel like I need to put my foot down with this girl."
                "Otherwise she's going to think she can walk all over me."
                bree.say "It's your face you should be worrying about."
                bree.say "Because if you talk to me like that again..."
                bree.say "Then I'm going to break your nose, you rude bitch!"
                "That said, I turn on my heel and walk away."
                "Because I seriously don't want to hear her response."
                "If I managed to put her in her place, then we can get through this shoot."
                $ hero.fun += 1
    elif r == 3:

        bree.say "Ooh..."
        bree.say "Who's that girl over there?"
        bree.say "Did someone bring their kid to work with them?"
        "As soon as I say this, the photographer almost jumps out of his skin."
        "Photographer" "Didn't I tell you, [hero.name]?"
        "Photographer" "That's the designer for today's shoot."
        "Photographer" "Her name's Cassidy."
        "Photographer" "Daddy's putting up the money for all of this."
        "Photographer" "But for god's sake, don't mention that!"
        "I find myself frowning at all of this."
        "But I nod all the same and try to remain professional."
        "Photographer" "Oh shit...here she comes!"
        "Photographer" "Hi, Cassidy, darling - is everything okay?"
        cassidy.say "So far, so good!"
        cassidy.say "Who's this?"
        cassidy.say "Is she one of my models?"
        "I can't help bristling a little as the girl totally ignores me."
        "But the photographer seems to be in full-on grovelling mode."
        menu:
            "Stay polite to Cassidy":
                "Urgh..."
                "Someone really should put this spoilt little brat in her place!"
                "But right now her daddy's money is paying my wages."
                "So it looks like I'm going to have to suck it up."
                bree.say "That's right - my name's [hero.name]."
                bree.say "And I'm really looking forward to wearing your designs."
                bree.say "They look so fresh and original."
                "The photographer's face lights up as I verbally kiss Cassidy's ass."
                "And she seems to be pretty pleased with what I have to say too."
                cassidy.say "Thank you, [hero.name]."
                cassidy.say "Sounds like you get it."
                cassidy.say "Like you can see what I'm trying to achieve with my designs."
                $ hero.fun -= 1
            "Put Cassidy in her place":
                "Hmm..."
                "So daddy's little princess wants to play designer, does she?"
                "Then maybe somebody should give her a taste of the real thing."
                bree.say "Ahem!"
                bree.say "Firstly, I have a name."
                bree.say "And secondly, don't act like I'm not here, okay?"
                "Cassidy takes a step backwards in surprise."
                "She's clearly not used to being spoken to like that."
                "But the photographer leaps in, trying to make the save."
                "Photographer" "This is [hero.name]."
                "Photographer" "And yes, she is going to be modelling for you."
                cassidy.say "Is she allowed to be so rude to me?"
                "Photographer" "She's a strong-willed, free-spirited professional, Cassidy."
                "Photographer" "The prefect type of person to bring your designs to life!"
                "Cassidy frowns, but then she nods."
                cassidy.say "I guess so..."
                cassidy.say "But she'd better do all of that stuff you said just now!"
        $ hero.money += 25
    elif r == 4:

        "I'm getting ready to put on the first outfit for the shoot."
        "And yeah, I know that my mind is elsewhere as I'm doing it."
        "But I snap right back to reality when I realise people are staring at me."
        "First one, then another and finally all of the other models are doing it."
        "They're pointing at me like they can't believe what they're seeing."
        bree.say "Uh..."
        bree.say "What's the matter?"
        bree.say "Seriously, guys - you're creeping me out!"
        bree.say "what is it?!?"
        "The photographer comes over to see what all the fuss is about."
        "He leans in and then frowns at what he sees, shaking his head."
        "Photographer" "It's a pimple, [hero.name]."
        "Photographer" "You have a pimple on your nose."
        bree.say "What?"
        bree.say "How did I not see that?"
        "Photographer" "Don't worry, [hero.name]."
        "Photographer" "I always touch up your shots on my laptop."
        "Photographer" "I can edit that out, no problem."
        menu:
            "Be grateful":
                "I feel a wave of relief sweep over me."
                "And I nod eagerly, ready to get on with the shoot."
                bree.say "That's great!"
                bree.say "Maybe I can put something on it in the meantime..."
                "With that problem sorted, I return to getting ready."
                "I need to concentrate on getting through the shoot."
                "And I can do that because someone else is handling the zit."
                "If only I could edit out the blemishes in real life too!"
                $ hero.energy += 1
            "Be annoyed":
                bree.say "Hey - wait a minute!"
                bree.say "What do you mean you always touch up my shots?"
                bree.say "What's wrong with them?"
                "The photographer holds up his hands, fending off my questions."
                "At the same time he's shaking his head and backing off too."
                "Photographer" "Nothing, [hero.name], nothing!"
                "Photographer" "That's just part of the editing process, you know?"
                "Photographer" "I do the same thing to everyone's shots."
                "I narrow my eyes as I watch him hurry away."
                "And that's because I'm sure he's not telling me the truth."
                $ hero.charm -= 1
    elif r == 5:

        "I walk into the studio and see the racks of clothes for today's shoot."
        "There's one that's filled with pretty casual stuff, like jeans and sweatpants."
        "But the next has some really nice-looking dresses and evening gowns on it."
        "I can't help stopping by the latter and inspecting them a little more closely."
        "Photographer" "Hey, [hero.name]!"
        "Photographer" "Like what you see, huh?"
        bree.say "Oh yeah!"
        bree.say "These are really pretty."
        bree.say "Which of them am I going to be wearing for the shoot?"
        "The photographer chuckles and shakes his head."
        "Photographer" "Oh no, [hero.name]!"
        "Photographer" "Palla's doing the evening-wear section of the shoot."
        "Photographer" "You're modelling the that rack over there."
        "My heart sinks as he points to the jeans and sweatpants."
        bree.say "But why?"
        "Photographer" "You gotta go with your strengths, [hero.name]."
        "Photographer" "And you...well, you're more sweatpants than evening-wear!"
        menu:
            "Suck it up":
                "I want to protest at being pigeon-holed like this."
                "To ask why a bony bitch like Palla gets to be glamorous and I don't."
                "But then I remember that I'm not doing this to get famous."
                "I'm doing it to earn a living."
                bree.say "Urgh..."
                bree.say "Okay, okay..."
                bree.say "So long as I get paid at the end of it all."
                "Photographer" "That's great, [hero.name]!"
                "Photographer" "And what are you even worried about?"
                "Photographer" "You look great in sweatpants!"
                $ hero.charm -= 1
            "Complains":
                "This is bullshit!"
                "I refuse to be pigeon-holed!"
                bree.say "And why is that, huh?"
                bree.say "Because I have a figure?"
                bree.say "Because I'm not a bony bitch, like Palla?"
                "The photographer holds up his hands and backs away."
                "Photographer" "What's the matter, [hero.name]?"
                "Photographer" "You look great in sweatpants!"
                bree.say "I look great in a pretty dress too!"
                "Photographer" "Erm..."
                "Photographer" "Okay, okay..."
                "Photographer" "I'll see what I can do!"
    return

label random_work_events_nightclub:
    $ r = randint(1, 5)
    if r == 1:

        "It's been a fairly typical night working behind the bar at the club."
        "But now I'm getting to the point where I really want my shift to be over."
        "I'm tired and my feet are sore, but I'm still doing my best to keep smiling."
        "But as I serve this one guy, he keeps winking at me the whole time."
        bree.say "Erm..."
        bree.say "Are you okay?"
        bree.say "Looks like you got something in your eye!"
        "Guy" "What?"
        "Guy" "Oh no!"
        "Guy" "I was just wondering - is this one of those places where you guys dance?"
        "Guy" "You know, like get up on the bar and dance?"
        "Guy" "Because I'd give you a massive tip to see that!"
        "It takes me a moment to get my head around what the guy's saying."
        "But when I do, I shake my head."
        menu:
            "Laugh it off":
                "I laugh and wave the guy's question away."
                bree.say "I think you've been watching too many movies, buddy!"
                bree.say "You think we can actually get up on here and dance?"
                bree.say "The health and safety regulations are there for a reason."
                bree.say "And no tips big enough to risk breaking your neck for!"
                "The guy looks disappointed and more than a little embarrassed."
                "Guy" "Oh..."
                "Guy" "Okay..."
                "Guy" "Sorry I asked."
            "Tell the guy off":
                "I fix the guy with a hard stare."
                bree.say "Really?"
                bree.say "Have you seen how narrow this bar is?"
                bree.say "And we've got morons slobbering over it all the time!"
                bree.say "What you're saying is you want to see me fall and break something?!?"
                "The guy starts to back off, beating a hasty retreat."
                "Guy" "I..."
                "Guy" "No..."
                "Guy" "Look...I'm sorry I asked!"
    elif r == 2:

        "I'm just doing whatever behind the bar when the manager walks over."
        "He looks harassed as usual, and waves at me to get my attention."
        "Manager" "[hero.name]..."
        "Manager" "Somebody blocked one of the toilets in the ladies bathroom."
        "Manager" "I can't go in there myself, because I'm a guy."
        "Manager" "So I need you to grab a plunger and sort it out."
        "My eyes go wide at the idea of doing what he just asked."
        "And I shake my head, already starting to back away."
        bree.say "Eww!"
        bree.say "No way!"
        bree.say "That sounds disgusting!"
        "Manager" "Come on, [hero.name]!"
        "Manager" "Help me out here."
        "Manager" "There's nobody else that can do it!"
        menu:
            "Do it":
                bree.say "Okay, okay..."
                bree.say "But you owe me for this - big time!"
                "The manager looks genuinely relieved at my answer."
                "And he nods as he hands over a plunger and some rubber gloves."
                "Manager" "That's great, [hero.name]."
                "Manager" "I always knew you were a team player!"
                "I mutter something insulting as I storm off towards the ladies bathroom."
                "And what follows is one of the most unpleasant experiences of my life."
                $ hero.fun -= 2
                $ hero.money += 20
            "Refuse":
                bree.say "No way!"
                bree.say "I'm a bar-tender, not a plumber!"
                bree.say "Get on the phone and call someone."
                "The manager looks frustrated at my answer."
                "But there's really nothing that he can do."
                "Unblocking toilets simply isn't a part of my job-description."
                "Manager" "Really, [hero.name]?"
                "Manager" "I thought you were a team-player."
                "Manager" "But obviously I was wrong!"
    elif r == 3:

        "I'm serving a guy that's all smiles and winks."
        "You know the kind - thinks he's a real ladies man."
        "And I'm doing the best I can to keep things professional."
        bree.say "There you go!"
        bree.say "Will that be card or cash?"
        "Guy" "I always pay cash, babe."
        "Guy" "And here's a little something extra."
        "Guy" "So that you can buy one for yourself too."
        "The guy's handed over the extra cash before I can object."
        "And I can see from the look on his face that he's pleased with himself."
        "Guy" "I don't suppose your shift ends anytime soon?"
        "Guy" "Because I sure could use some company..."
        menu:
            "Accept the tip and gently let the guy down":
                "I put on my best fake smile and shake my head."
                bree.say "Thank you very much."
                bree.say "But I should let you know..."
                bree.say "We have a strict policy of non-fraternisation here."
                bree.say "So I can't take you up on that offer."
                "Guy" "Oh..."
                "Guy" "Okay..."
                "Guy" "If that's your policy."
                "The guy looks disappointed and more than a little deflated."
                "But my guess is that he'll soon find someone else to sleaze over."
                $ hero.money += 5
            "Refuse the tip and tell the guy off":
                "I frown at the guy and toss his tip onto the bar."
                "Then I plant my balled fists firmly on my hips."
                bree.say "No thank you."
                bree.say "We have a strict policy on tips here."
                bree.say "And just for the record, I'm not a prostitute."
                bree.say "So you can't buy my services!"
                "The guy backs off, waving his hands in the air."
                "Guy" "No..."
                "Guy" "No, that's not what I..."
                "Guy" "Sorry, I have to go now!"
                "And with that, he hurries away from the bar."
    elif r == 4:

        "I've pulled the short straw tonight, ending up in the VIP section."
        "This sucks because the kind of people that use it are almost always assholes."
        "Like the guy that's striding up to me right now, with his date on his arm."
        dwayne.say "Hey there, little lady!"
        dwayne.say "Would you show me to my usual booth?"
        bree.say "Just a second, sir..."
        bree.say "What name was that booked under?"
        "The guy reels off his full name, and I look down the list."
        bree.say "Huh..."
        bree.say "I don't see you down here!"
        cherie.say "What's the matter, Dwayne?"
        cherie.say "Is there a problem?"
        "The guy smiles and tries to brush the situation aside."
        dwayne.say "No problem, Cherie!"
        dwayne.say "Look, my name should be on the list."
        dwayne.say "And even if it isn't, I'm a valued patron."
        dwayne.say "So just step aside and let me through, okay?"
        menu:
            "Stand your ground":
                "I could just let this privileged prick through."
                "But he's the kind of guy that really hacks me off."
                "So I shake my head and tap the guest list."
                bree.say "I'm afraid I can't do that."
                bree.say "But I can ask the manager to come over, if you'd like?"
                "The man looks at me in genuine surprise."
                "I guess he's not used to people standing up to him."
                dwayne.say "I..."
                dwayne.say "Do you know who I am?!?"
                "The moment he says those words, I know that he's lost."
                "It's like an admission of his arrogance."
                bree.say "Yes, sir, I do."
                bree.say "You're someone who's name isn't on the list!"
                "I hear the man's date snigger at this."
                "And then he storms off with her following close behind."
                $ hero.charm += 1
                $ dwayne.love -= 2
            "Let Dwayne have his way":
                "I glance over at the VIP section, seeing that it's half-empty."
                "Then I look back at the guy towering over me, noting his size and expression."
                "I shrug and step aside, because what's the point in causing a scene?"
                bree.say "Whatever..."
                bree.say "Just don't blame me if someone says you stole their reservation."
                "The guy's suddenly all smiles, laughing at my warning as if it's a joke."
                "He strides past me with his date in tow."
                "And I get back to what I was doing before he showed up."
                $ dwayne.love += 2
    elif r == 5:

        "I somehow manage to hear the sound of breaking glass over the music."
        "And I'm out from behind the bar with the dustpan and brush a moment later."
        "Looks like someone's dropped a glass in the middle of the dance-floor."
        "So I need to get out there as quickly as I can to clean it up."
        "Or else somebody's going to get hurt!"
        "But I soon see that the place is still heaving with bodies."
        "How in the hell am I supposed to get out there?"
        "I'm likely to get trampled to death before I even reach the glass!"
        menu:
            "Make the DJ stop the music":
                "Then an idea pops into my head."
                "And I make straight for the DJ booth."
                bree.say "Hey!"
                bree.say "Kill the music!"
                "DJ" "Huh?"
                bree.say "Just do it!"
                "Shocked at being bossed around, the DJ does as he's told."
                "Then I use the mass confusion that follows to reach my goal."
                "I elbow my way onto the dance-floor and soon find the glass."
                "And once it's safely swept up, I nod to the DJ."
                "Soon enough the music is back on and everything returns to normal."
            "Fight your way onto the dance-floor":
                "Urgh..."
                "Looks like I'm going to have to brave the crowd!"
                "Steeling myself, I begin to elbow my way through."
                bree.say "Excuse me..."
                bree.say "Coming through..."
                bree.say "Could you just..."
                bree.say "Aaargh!"
                "By the time I'm done, I feel like I've been beaten up."
                "I emerge from the crowd, bruised and dishevelled."
                "But at least I know the glass has been taken care of."
                $ hero.fun -= 1
                $ hero.energy -= 2
        $ hero.morality += 1
    return

label random_work_events_pornstar:
    $ r = randint(1, 5)
    if r == 1:

        "I'm just getting into the costume that I've been given for the shoot and preparing myself."
        "But then I look up to see the guy that I'm going to be shooting with today walking onto set."
        "We've never worked together before and I've never even spoken to him before now."
        "But that's one of the quirks of a job like this."
        "You've gotta be able to handle getting intimate with a stranger at short notice."
        "Because after all, that is what we're getting paid for."
        "I know it's not a good way to judge the guy, but he does look pretty cute."
        "And when he sees me looking in his direction, he gives me a nice smile too."
        "Pornstar" "Oh..."
        "Pornstar" "Hey there!"
        "Pornstar" "You must be [hero.name], right?"
        "I nod and return the smile, trying to ignore the fact he's already stripping off too."
        bree.say "Yeah, that's me!"
        "Pornstar" "I'm Jamie - great to be working with you, [hero.name]."
        "We shake hands, and it's just about then I catch sight of it."
        "Even with his shorts still on, there's no way to hide something that size!"
        "Jamie must see my eyes go wide, because he chuckles a little."
        "It's not a mean laugh or a disgusting macho one."
        "More like he's used to that kind of reaction and trying to play it down."
        "Pornstar" "Yeah..."
        "Pornstar" "I get people staring at it a LOT!"
        "Pornstar" "But it's opened a lot of doors for me in the industry."
        bree.say "I bet it has!"
        bree.say "And if not, you could probably use it to batter them down!"
        "Jamie laughs again and nods."
        "But then he becomes a little more serious."
        "Pornstar" "Seriously though, [hero.name]..."
        "Pornstar" "Are you going to be okay with..."
        "Pornstar" "Well, you know...the size of it?"
        "Oh great - way to put me on the spot!"
        "Do I admit to being intimidated by the size of his cock?"
        "Or do I just wave it off and act like a professional?"
        "At least the professional I want him to think I am!"
        menu:
            "Laugh it off":
                "I'm not going to earn anyone's respect by showing fear."
                "And I want everyone watching to know that I can handle it."
                "Otherwise they'll not think of me when similar roles come up."
                "Plus I'm supposed to be an actor, right?"
                "So I should be able to pull this one off."
                bree.say "Don't worry about me, Jamie."
                bree.say "I've handled big parts before."
                bree.say "And I want to get bigger parts of the other kind too."
                "Pornstar" "Nicely put, [hero.name]!"
                "Pornstar" "So...let's go make this thing happen."
                "I nod and smile as I follow him to where we're supposed to do it."
                "And I get ready for a real test of my acting skills."
                "That and my physical stamina too!"
                $ hero.charm += 1
            "Admit that you're a little intimidated":
                "I'm not going to start lying about stuff like this."
                "Doing a sex scene requires a serious amount of trust."
                "And I'd be letting myself down if I wasn't honest with him."
                bree.say "Honestly, Jamie..."
                bree.say "Nobody warned me you be so..."
                bree.say "So big!"
                bree.say "I'd kind of like to have been able to prepare!"
                "Jamie nods as I say all of this."
                "And I can see that he's genuinely listening to my concerns."
                "Pornstar" "You don't have to go through with this, [hero.name]."
                "Pornstar" "Not if you feel like it's something so serious."
                "Pornstar" "But if it helps, I promise I'll be gentle."
                "The look on his face looks genuine, and I feel like I can trust him."
                "So I nod and give him what I hope is a sincere smile."
                bree.say "Okay, Jamie..."
                bree.say "Let's give it a try."
                "Oh god, I hope I can handle this!"
        $ hero.energy -= 1
    elif r == 2:

        "I'm looking at what passes for the script."
        "Specifically the scene we're shooting today."
        "I notice that I'm supposed to be using several toys and devices at various points."
        "But when I glance around the set, almost none of them can be seen to hand."
        "I frown at this, and then walk over to where the director is standing."
        bree.say "Hey, Steven..."
        bree.say "You got a minute?"
        "Harassed and impatient as usual, the director spins around to face me."
        "Director" "Huh?"
        "Director" "What is it now, [hero.name]?"
        "Director" "And hurry up already - time is money!"
        "I do the best I can to ignore his rude and unprofessional manner."
        "Holding up the script, I point to the lines that are concerning me."
        bree.say "Says right here that I'm supposed to use all these sex toys."
        "Director" "Yeah, so what?"
        "Director" "You got a problem with that?"
        bree.say "The only problem is that I don't see half of them on the set!"
        bree.say "Is someone from props bringing them before we start shooting?"
        "Director" "WHAT?!?"
        "Director" "Those useless assholes!"
        "Director" "I should fire the whole goddamn lot of them!"
        bree.say "Whatever, Steven, whatever."
        bree.say "But that doesn't help me out a whole lot, does it?"
        "Director" "Fucking hell, [hero.name] - you're an actor, so improvise!"
        "Director" "Use what we have and shove whatever else you can get up there, okay?"
        "I can't actually believe what I'm hearing."
        "He wants me to use props off the set to get myself off?!?"
        menu:
            "Refuse to work without the proper equipment":
                "So he wants to remind me that I'm an actress, does he?"
                "Well maybe he needs to be reminded of what that really means!"
                bree.say "No way, Steven!"
                bree.say "Don't try to play the actress card on me."
                bree.say "Not when you know that's an unsafe working environment!"
                "Director" "You what?"
                "Director" "You know how easily I can replace you?!?"
                bree.say "Not quickly enough to get this scene in the can."
                bree.say "And you'd have to reshoot all the stuff we already did too!"
                bree.say "Be much quicker to send someone out to grab all the stuff I need..."
                "Director" "Urgh.."
                "Director" "Okay, okay..."
                "Director" "Geez...and I thought I was a manipulative shit!"
                $ hero.charm += 1
            "Improvise":
                "I guess he does have a point."
                "Improvisation is an important skill to cultivate."
                "So I nod and start trying to look around the set."
                bree.say "I'd rather have the real thing, Steven!"
                bree.say "But when life gives you lemons..."
                "The director smiles and nods, happy with my reaction."
                "Director" "That's my girl, [hero.name]."
                "Director" "I knew you wouldn't let me down!"
                "Director" "Let's get making some lemonade - SEXY lemonade!"
                "I nod, still trying to scan the set for inspiration."
                "I'm hoping that I've made the right decision here."
                "And wondering whether I can sue if things go wrong..."
                $ hero.fun -= 1
    elif r == 3:

        "I'm all dressed and ready to get on with the shoot."
        "And I'm not the only one, as the entire crew are ready too."
        "But it looks like my co-star's running more than a little late!"
        "Where in the hell are they?"
        "I'm trying to be professional about all of this."
        "But I can't help rolling my eyes and looking at the director."
        bree.say "I thought you said this Charlie was a pro?"
        bree.say "Wouldn't a pro have been here on time?"
        "Director" "Don't worry, [hero.name]."
        "Director" "Charlie and I go way back."
        "Director" "One hundred percent a class-act."
        "Director" "Just be patient and you'll see."
        lexi.say "Hey guys!"
        lexi.say "Sorry I'm late."
        lexi.say "Had a heavy session last night, and I overslept!"
        "I look up to see a pretty, but slutty-looking girl walking onto the set."
        "For a moment I wonder what she's doing there, but then it hits me."
        bree.say "THAT'S CHARLIE?!?"
        lexi.say "Oh yeah, that's my stage-name."
        lexi.say "Charlie - you know, with an I?"
        "Director" "Oops...must have been a spelling error in the script!"
        "Director" "There isn't going to be a problem, is there?"
        menu:
            "No problem":
                "I take a deep breath to steel myself."
                "And then I put a professional smile on my face."
                bree.say "No problem at all, Steve."
                bree.say "I just want to get on with the shoot, that's all."
                "He nods and smiles right back at me."
                "Director" "That's the spirit, [hero.name]."
                "Director" "Okay everyone, let's get this show on the road!"
                "The tardy girl shoots me a smile and then hurries off."
                "And that leaves me to wait for her to be ready to shoot."
                "Urgh...she'd better be worth the wait!"
            "Complains that Lexi was late":
                "I feel like I have to make a point here."
                "I'm always as professional as I can be."
                "And I expect other people to be professional too."
                bree.say "I just think it's disrespectful, that's all."
                bree.say "Keeping us all here waiting like that!"
                "Charli doesn't seem to let my complaints get to her."
                "Instead she just laughs and smiles."
                lexi.say "Ah, I used to be just like you, [hero.name]."
                lexi.say "But don't worry, you'll get over it!"
                "Director" "That's the spirit, Charlie."
                "Director" "Okay everyone, let's get this show on the road!"
                "The tardy girl shoots me a smile and then hurries off."
                "And that leaves me to wait for her to be ready to shoot."
                "Urgh...she'd better be worth the wait!"
        $ hero.fun -= 1
    elif r == 4:

        "Director" "Hey, [hero.name]..."
        "Director" "You got a minute to chat?"
        "I look up from what I'm doing and see the director hurrying towards me."
        "He has the look on his face that usually means he wants something."
        "But I supposed that I should hear him out before I tell him to get lost."
        bree.say "Hi, Steve..."
        bree.say "What's up?"
        "The director smiles and holds up his hands."
        "And I know that means he's going to try to sell something to me."
        "Director" "I've been thinking about the sex scene, [hero.name]."
        "Director" "The one that we're shooting today."
        "Director" "And I think it needs a little something extra."
        "Director" "A little more oomph, you know?"
        bree.say "Hmm..."
        bree.say "I can't say I do, Steve."
        bree.say "What would that entail, exactly?"
        "Director" "How about...now hear me out, okay?"
        "Director" "We do the scene without using protection?"
        "Director" "It'll make everything so much more real and passionate!"
        "Director" "And don't worry about anything going wrong - because I'll pay to fix it!"
        "I'm stunned that he'd even ask me to do something like that."
        "So much so that it takes me a few moments to blurt out an answer."
        menu:
            "Agree to do the scene without protection":
                "My instincts are screaming at me to say no."
                "But then I think about how enthusiastic the director looks."
                "If I put my reservations aside, just this once."
                "I'm sure that I could really impress him."
                bree.say "Okay, okay..."
                bree.say "But this is a one-off, Steve."
                bree.say "You understand that?"
                "The director nods his head eagerly."
                "But somehow I get the impression he's not really listening to me."
                "Director" "Great, [hero.name], Great!"
                "Director" "I'll go make all the arrangements..."
                "He hurries off, leaving me alone with my thoughts."
                "And all I can do is hope that I didn't just make a huge mistake."

                $ random_npc_impregnate("Pornstar")
                $ hero.morality -= 2
            "Refuse to do the scene without protection":
                "This is one of those times when I know that I have to listen to my instincts."
                "Sure, doing what the director wants would probably endear me to him in the future."
                "But it could just as easily get me a bad reputation in the industry too."
                "Not to mention the dangers of having unprotected sex!"
                bree.say "No way, Steve."
                bree.say "That's a rule I'm not going to break."
                bree.say "Either we use protection, or I don't do the scene."
                "Director" "Please, [hero.name]!"
                "Director" "Think about it seriously!"
                bree.say "That's what I am doing, Steve!"
                bree.say "And you're not talking me out of it."
                "Director" "Okay, [hero.name], okay..."
                "Director" "I'll go and tell them the bad news."
                "He hurries off, leaving me alone with my thoughts."
                "And all I can do is hope that I didn't just make a huge mistake."
                $ hero.money -= 25
    elif r == 5:

        "It's the first morning of the shoot, and everyone's getting ready on the set."
        "I'm all smiles and trying to look like I'm one hundred percent ready to go."
        "But the truth is that I was up late last night, working on an essay for uni."
        "Which means that I didn't get enough sleep and I've only scanned the script."
        "Hopefully I can bluff for a while and then read it in more depth later."
        "Director" "Right..."
        "Director" "Is everyone ready to get started?"
        "There's a chorus of affirmative responses from around the set."
        "And I'm sure to add my own voice to them, just to keep up the illusion."
        bree.say "Yeah, Steve..."
        bree.say "I'm totally ready to go!"
        "The director nods and waves me over."
        "Director" "Okay, [hero.name]..."
        "Director" "I've arranged for you to talk to Calvin before we get started."
        bree.say "Huh?"
        bree.say "Who's Calvin?"
        "Director" "The animal handler, [hero.name]."
        "Director" "You know?"
        "Director" "For the scene with the dog?"
        "Scene with a dog?"
        "What in the hell is he talking about?"
        "Oh no - I must have missed that when I scanned the script!"
        "How on earth can they expect me to do something with a dog?!?"
        "Isn't that illegal?"
        menu:
            "Refuse":
                "There's no way that I'd have signed on for this shoot if I'd known."
                "And even so, I'd have thought the director would know I wasn't up for that!"
                "Hell, how could he even want to make a film with such perversion in it?"
                "Whatever the case, I need to put my foot down."
                "And I need to do it now!"
                bree.say "No, Steve..."
                bree.say "I'm not ready for that."
                bree.say "In fact, I'll never be ready for that!"
                "The director's face becomes puzzled."
                "And he shakes his head."
                "Director" "I don't get it, [hero.name]."
                "Director" "Are you allergic to dogs or something?"
                bree.say "No - I just won't do...things with them!"
                bree.say "Things that are just wrong!"
                "Director" "Walking a dog is wrong?"
                bree.say "You want me to WALK the dog?"
                "Director" "Erm..."
                "Director" "You didn't read the script, did you, [hero.name]?"
                bree.say "No..."
                bree.say "No, I didn't..."
                $ hero.morality += 1
            "Do the best you can":
                "Oh god..."
                "Can I really do something like this?"
                "Am I expected to be cool with it as a professional?"
                bree.say "I...I'll do my best, Steve."
                bree.say "But I never did anything like this before."
                bree.say "And it's kinda scary, you know?"
                "The director's face becomes puzzled."
                "And he shakes his head."
                "Director" "I don't get it, [hero.name]."
                "Director" "Are you afraid of dogs or something?"
                bree.say "No - I just thought it was wrong do...things with them!"
                bree.say "Things that are just weird and icky!"
                "Director" "Walking a dog is wrong?"
                bree.say "You want me to WALK the dog?"
                "Director" "Erm..."
                "Director" "You didn't read the script, did you, [hero.name]?"
                bree.say "No..."
                bree.say "No, I didn't..."
                $ hero.morality -= 1
        $ hero.knowledge -= 1
    return

label random_work_events_pub:
    $ r = randint(1, 5)
    if r == 1:

        "I'm just filling the glass-washer behind the bar, when I hear a familiar noise."
        "Drunk" "Hey..."
        "Drunk" "Urgh..."
        "Drunk" "Can I PLEASE get some service around here?"
        "By now I'm used to the sound of someone hammering on the bar to get my attention."
        "But the way surly drunks talk to whoever's tending the bar is always annoying."
        "I pop up and take a look at the guy who's demanding to be served."
        "Urgh...this doesn't look good at all!"
        "He's clearly had too much to drink already."
        "But just as I think about ducking back down, he sees me."
        "Drunk" "Hey..."
        "Drunk" "Hey, you!"
        "Drunk" "I want another of the same!"
        "I hate this part of the job - it's the absolute worst."
        "I know that I'm supposed to cut someone off if they look like they've had too much."
        "But that's never something that a drunk is going to take well, quite the opposite."
        "On the other hand, I could just serve the guy in the hope of shutting him up."
        "But then he might still hang around and demand more booze."
        "Or worse, he could start trouble!"
        "I have to decide what I'm going to do - and fast..."
        menu:
            "Cut the drunk off":
                "This is going to suck."
                "But I have to do it."
                "Pulling myself up to my full height, I stick out my chest."
                "And then I stride over to where the drunk is still hammering on the bar."
                bree.say "I think you've had enough for tonight, buddy."
                bree.say "Time to go home and sleep it off."
                "The drunk stares at me for a second."
                "His eyes are blank, like he doesn't understand."
                "Then he shakes his head, and the look in his eyes turns mean."
                "Drunk" "What the hell?!?"
                "Drunk" "Don't tell me I've had enough, girlie!"
                "Drunk" "I'll tell you when I'm ready to quit - you got that?"
                "I don't like this one bit."
                "This guy's much bigger than me."
                "And the booze is giving him all the confidence in the world."
                "But I already started this fight."
                "Now I have to finish it."
                bree.say "Don't talk to me like that, buddy!"
                bree.say "We don't tolerate people abusing our staff around here."
                bree.say "Either you get lost right now, or else I call the cops!"
                "The drunk seems genuinely surprised at the tone of my voice."
                "So much so that he lurches back from the bar."
                "Then he turns and sways towards the door."
                "I can hear him muttering and swearing under his breath."
                "But at least he's finally leaving."
                "I wait until he's out of the door before I breathe a sigh of relief."
                "Now all I need to do is find a way to stop my heart hammering in my chest!"
                $ hero.charm += 1
            "Serve the drunk more booze":
                "If I were on shift with someone else it'd be different."
                "They could back me up and help out if things turned ugly."
                "But I'm stuck here on my own until the end of my shift."
                "So I put on my best fake-friendly face and walk over."
                bree.say "Sorry about the wait, sir."
                bree.say "Now what can I get you?"
                "The drunk narrows an eye at me."
                "Drunk" "Didn't you hear me?"
                "Drunk" "I said I wanted the same again!"
                "Why do they always assume I know what they had last time?"
                "Or that I know what they think is their 'usual'?"
                "Luckily for me, the drunk is still clutching his empty glass."
                "And we only serve one brand of booze in those."
                "So I can easily figure it out without letting on."
                bree.say "Okay, sir."
                bree.say "Coming right up..."
                "I pull the drink and hand it over as he pays for it."
                "And I keep the fake smile on my face the whole time."
                "The drunk seems satisfied with the outcome."
                "So much so that he lurches back from the bar."
                "Then he turns and sways towards the corner he came from."
                "I can hear him muttering and swearing under his breath."
                "But luckily for me, my shift is almost over."
                "So I can get the hell out of here before he wants another."
                "It's not my problem anymore."
                "The next person on shift can deal with it instead."
                $ hero.charm -= 1
    elif r == 2:

        "I'm just pottering around behind the bar, doing this and that."
        "When I look up to see a guy shuffling over from the direction of the bathrooms."
        "He seems to be glancing around, like he thinks everyone in the place is staring at him."
        "And they're starting to, just because of how weird he's being."
        "By the time he finally makes it over to the bar, he's almost sweating!"
        "I give him what I hope is a friendly smile and walk over."
        bree.say "Hey there!"
        bree.say "How can I help you?"
        "The guy's eyes are darting this way and that."
        "It's like he can't concentrate on talking to me."
        "I guess because he's too busy worrying about being overheard."
        "Patron" "I..."
        "Patron" "Erm..."
        "Patron" "I just..."
        "I raise my eyebrows, still not sure what he wants."
        bree.say "You want a drink, huh?"
        bree.say "Maybe something to eat?"
        "Patron" "N...no..."
        bree.say "Hmm..."
        bree.say "Cues for the pool table?"
        "Patron" "No."
        bree.say "Darts then?"
        bree.say "Or something putting on the TV?"
        bree.say "Is the music too loud maybe?"
        "Patron" "No, no, no..."
        "I'm fast running out of ideas."
        "So all I can do is shrug and press him for an answer."
        bree.say "Then you'd better tell me what it is, buddy!"
        "The guy leans in closer, almost all the way over the bar."
        "Patron" "C...c...condoms!"
        bree.say "What?"
        bree.say "We don't sell those over the bar!"
        bree.say "Try the machine in the guy's bathroom, yeah?"
        "Patron" "No...I already did that!"
        "Patron" "The machine ate my money."
        "Patron" "And it didn't give me my condoms!"
        "Patron" "Please, you have to help me."
        "Patron" "I need the money back so I can try some place else!"
        "Wow...he must need those things pretty badly!"
        "Urgh...I feel for the guy."
        "But I'm not supposed to open the till for stuff like that."
        "Hmm...decisions, decisions..."
        menu:
            "Reimburse the patron from the till":
                "I know that I'm going to get into trouble for doing this."
                "But I've been in a similar situation myself and I know how much it sucks."
                "So I just tell myself that I'm helping the guy out."
                "And I pray that it's worth the effort for whoever he's going to use them with!"
                bree.say "Look, buddy..."
                bree.say "I really shouldn't do this, you know?"
                bree.say "So if it happens again, don't ask me a second time."
                "The guy nods eagerly as I turn to open the till."
                "Quick as I can, I grab enough coinage to reimburse him."
                "Patron" "Thank you, thank you, thank you!"
                "Patron" "You just saved my life!"
                "Nod and let out a sigh."
                bree.say "Whatever."
                bree.say "Just don't tell anyone it was me."
                "The guy nods and grins as he turns towards the door."
                "As I watch him go, I just hope he has more luck somewhere else."
                "Because it'd suck if he went to another pub and had the same thing happen again."
                $ hero.money -= 5
                $ hero.morality += 1
            "Tell the patron to call the vending machine company":
                "I know that I could really help this guy out by just opening the till."
                "But I really need this job, and it's that kind of stuff that'll get me the sack."
                "And anyway, can't this guy afford to buy another back of condoms somewhere else?"
                bree.say "Look, buddy..."
                bree.say "If it were up to me, I'd give you the money back."
                bree.say "But the policy here is the till only opens for a sale."
                "The guy starts to look frantic."
                "He shakes his head at me."
                "And he seems to forget all about his previous need to be discreet."
                "Patron" "WHAT?!?"
                "Patron" "NO!"
                "Patron" "I need those things!"
                "I cross my arms over my chest."
                "And I give the guy what I hope is a stern look."
                bree.say "Look, man..."
                bree.say "What do you want from me, huh?"
                bree.say "I already told you I can't open the till."
                bree.say "Call the number on the side of the machine about a refund."
                bree.say "Then either go someplace else and get the condoms."
                bree.say "Or else take a cold fucking shower!"
                "The guy looks at me in surprise."
                "And then he seems to realise I'm serious."
                "He shakes his head as he makes for the door."
                "But at least he's gone, so he's not my problem anymore."
                $ hero.morality -= 1
    elif r == 3:

        "Patron 1" "Whoa..."
        "Patron 1" "What the hell?!?"
        "Patron 2" "You're done playing, man!"
        "Patron 2" "Move over and let us have a game already!"
        "I can hear the sound of raised voices coming from the other side of the tap-room."
        "Then there's the scraping of furniture being pushed across the floor too."
        "All of which can only mean that trouble's about to kick off."
        "I hurry out from behind the bar and towards the source of the commotion."
        "And it doesn't take me long to find a pair of guys squaring up to each other."
        bree.say "Hey!"
        bree.say "Break it up!"
        "At the sound of my voice, they both take a step backwards."
        "It's like the tone I'm using is just right to catch them off-guard."
        "Patron 1" "Erm..."
        "Patron 1" "This guy here..."
        "He points at the other guy to make his point."
        "Patron 1" "He's trying to muscle me off the pool-table!"
        "As soon as the accusation is made, the second guy shakes his head."
        "Patron 2" "The fuck I am!"
        "Patron 2" "His game's over, so he needs to get off the thing!"
        "Patron 1" "Says who, dick-head?"
        "Patron 2" "What's that, huh?"
        "The second guy points at a pile of loose change on the edge of the table."
        "Patron 2" "I already put the money down for the next game."
        "Patron 2" "Those are the rules of pool - everyone knows that!"
        "The first guy responds by dashing the coins onto the floor."
        "Patron 1" "You're making that shit up!"
        "Patron 1" "I stay on here until I want to quit!"
        bree.say "Can't you guys sort this out without getting into a fight?"
        "All of a sudden, they're both staring at me."
        "And I get the impression they expect me to settle this."
        "Hmm...they both have a point."
        "I've seen people put coins on a pool-table for the next game in the past."
        "But I always thought that was just so they got on when the current players quit."
        "Though now I think about it, this guy has been on the table most of my shift."
        "So maybe it's time he got off it and let someone else play?"
        "Urgh..."
        "There's no way I can solve this without pissing someone off."
        menu:
            "Side with the first patron":
                "I take a deep breath and turn to face the second guy."
                "And I'm sure to look him straight in the eye as I speak too."
                bree.say "Look, buddy..."
                bree.say "I don't know about any rules for pool."
                bree.say "But this isn't kindergarten, you know?"
                bree.say "People don't have to take turns here!"
                "The guy opens his mouth to protest."
                "But I hold up a hand to silence him."
                bree.say "Ah, ah, ah!"
                bree.say "I'm the one calling the shots here!"
                bree.say "And I say your time on the table's over."
                "Patron 2" "But, but..."
                "Patron 2" "You can't do that!"
                bree.say "I damn well can."
                bree.say "And I can throw you out too."
                bree.say "So stop whining and leave this guy to play in peace."
                bree.say "Or you'll find yourself barred!"
                "The guy looks like he's going to protest again."
                "But then he grunts and shoots a mean look at the first guy."
                "He wanders off, muttering something under his breath."
                "But at least the situation's been defused."
                "Patron 1" "Thanks for the help, babe!"
                bree.say "Don't babe me, buddy!"
                bree.say "How about you solve your own problems in the future, huh?"
            "Side with the second patron":
                "I take a deep breath and turn to face the first guy."
                "And I'm sure to look him straight in the eye as I speak too."
                bree.say "Look, buddy..."
                bree.say "I don't know about any rules for pool."
                bree.say "But you've been on there since my shift started."
                "The guy opens his mouth to protest."
                "But I hold up a hand to silence him."
                bree.say "Ah, ah, ah!"
                bree.say "I'm the one calling the shots here!"
                bree.say "And I say your time on the table's over."
                "Patron 1" "But, but..."
                "Patron 1" "You can't do that!"
                bree.say "I damn well can."
                bree.say "And I can throw you out too."
                bree.say "So hand over the cues and shut up."
                bree.say "Or you'll find yourself barred!"
                "The guy looks like he's going to protest again."
                "But then he grunts and tosses his cue to the second guy."
                "He wanders off, muttering something under his breath."
                "But at least the situation's been defused."
                "Patron 2" "Thanks for the help, babe!"
                bree.say "Don't babe me, buddy!"
                bree.say "How about you solve your own problems in the future, huh?"
        $ hero.charm += 1
    elif r == 4:

        "It's another one of those times when my shift feels like it's never going to end."
        "And there's not enough for me to do to be able to keep my mind occupied either."
        "Sure, there are a few tables full of customers to make sure I can't get away with looking at my phone."
        "But not enough for there to be a constant stream or orders to keep me busy."
        "Soon I find my mind wandering onto morbid subjects, like how shitty my wage is here."
        "It's better than nothing, yet still so low as to make me feel like a genuine wage-slave."
        "I'm starting to wonder how long I need to stick it out here in order to get a raise."
        "Or if I could find a better job elsewhere doing less for more money."
        "But then I see a table full of customers getting up and leaving the pub."
        "Yeah, I know - it sounds boring as hell."
        "Thing is it means I can go over there to collect their empty glasses."
        "And, wait for it, wipe down the table too!"
        "Oh god...kill me now!"
        "Why couldn't I have been born into a life of idle wealth and privilege?"
        "I think I could really make a career out of doing nothing in the lap of luxury."
        "Anyway, I hurry over and begin to gather up the glasses on the empty table."
        "That's when I see something in-between some of the empties."
        "Oh my..."
        "It looks like..."
        "Is it really what I think it is?"
        "I pluck the thing up from the table and examine it closely."
        "It is - it's a wad of bills!"
        "Someone must have been counting it on the table and forgotten it."
        "I quickly flick through the wad, making a guess at how much is there."
        "I mean, it's not a fortune by any means."
        "But it's probably more than I'll make for my shift today."
        "I look up at the door and I can see the customers from the table through the glass."
        "They're hanging about on the street outside, probably talking about something."
        "If I hurry now, I should be able to catch then before they walk away."
        "That way I can return the bills."
        "But...I was just thinking about how much I could use an injection of cash."
        "And minutes later I find a pile of used bills, just left on a table."
        "Could it be that fate's throwing me a life-line here?"
        "Did I finally earn some decent Karma?"
        menu:
            "Return the wad of notes":
                "Urgh..."
                "I could SO have used this money!"
                "But it's not mine, and I can't keep it."
                "My conscience would never let me sleep again!"
                "So I dash out through the doors, the notes in my hand."
                "Outside I see a group of girls in designer clothes."
                "They're the ones I'm looking for, I just know it."
                "Then I see that one of them is rummaging through her handbag."
                palla.say "Where in the hell is it?!?"
                palla.say "I know that I put it back in my purse!"
                bree.say "Erm..."
                bree.say "Is this what you're looking for?"
                "At the sound of my voice, the girl glares at me."
                "She's giving me one of those looks."
                "You know the kind - like someone's demanding you prove your right to breath the same air as them?"
                "But as soon as she sees the notes, she practically lunges at me, snatching them out of my hand."
                palla.say "GIVE ME THAT, YOU BITCH!"
                palla.say "What are you doing with my money?!?"
                "I instinctively leap backwards as soon as she has the cash."
                bree.say "HEY!"
                bree.say "I found it on your table, that's all!"
                palla.say "Well...it'd better all be here!"
                "I shake my head in sheer amazement."
                "And I can see her friends are looking on in amazement too."
                "Girl" "Ah, Palla..."
                "Girl" "All she did was bring you your money back!"
                "I hold up my hands and start to walk back inside."
                bree.say "Whatever..."
                bree.say "Geez - I was just trying to help!"
                "I walk back inside, amazed at how ungrateful some people can be."
                "But I guess I shouldn't have expected anything at all."
                "Because you should do the right thing for it's own sake."
                "Not for the sake of getting praised."
                $ hero.fun -= 1
                $ hero.morality += 1
            "Keep it":
                "Ah hell - I really need the money!"
                "Without looking up, I shove the notes into my pocket."
                "Then I grab the empty glasses and hurry back behind the bar."
                "I'm just stuffing the notes into my bag when I hear the door open."
                palla.say "OKAY..."
                palla.say "WHERE IS IT?!?"
                "I feel my heart lurch in my chest."
                "How did the know it was me that took the money?"
                "But then reality hits me, and I feel my panic subside a little."
                "Of course there's no way she could have seen me take it."
                "She's obviously just an entitled bitch that's used to shouting and getting her way."
                "And as soon as I stick my head around the corner, I see that I was right."
                "This girl looks like a total bitch!"
                bree.say "Uh..."
                bree.say "Can I help you?"
                palla.say "My money, you dumb little cow!"
                palla.say "Where is it?"
                palla.say "You cleared our table, so you must have found it?"
                "I try to look innocent as I shake my head."
                bree.say "Sorry...but no."
                bree.say "I didn't find anything but empty glasses."
                "The rude girl's eyes narrow and the points a finger at me."
                palla.say "Yeah, right - I bet you stole it!"
                bree.say "I did not!"
                bree.say "But...if anyone turns it in, we'll be sure to let you know."
                "One of the rude girl's friends takes hold of her arm."
                "Girl" "Ah, Palla..."
                "Girl" "She said she'd call you if it turns up."
                "Girl" "So let's get out of here, yeah?"
                "I get one last evil stare from the rude girl."
                "And then they're gone, leaving me alone with my conscience."
                "Oh, and the money - which should at least be some comfort."
                $ hero.money += 75
                $ hero.morality -= 2
    elif r == 5:

        "As soon as I see the manager looking at the rota, I know what's coming."
        "And so I decide that it's better to take the bull by the horns for once."
        "With a sigh, I walk over and try to sound positive as I strike up a conversation."
        bree.say "Ah..."
        bree.say "Hi there!"
        "The manager looks at me with the usual expression of tiredness and depression."
        "Manager" "Oh..."
        "Manager" "Hey, [hero.name]..."
        "Manager" "Erm...you're not wanting to complain about something, are you?"
        "I shake my head and try to seem as innocent as possible."
        bree.say "What?"
        bree.say "Me, complain?"
        bree.say "God, no!"
        bree.say "You just looked a little stressed, that's all."
        "The manager's face seems to light up a little at this."
        "I guess nobody else notices their moods much around here."
        "Manager" "Funny you should say that, [hero.name]!"
        "Manager" "I was just looking at the rota."
        "Manager" "And I have a shift I need to fill...right here."
        "Manager" "Hey...would you be able to cover it?"
        "Manager" "It'd show you're a real team player!"
        "I look at the shift they're pointing out."
        "And I instantly know I have something planned for that date."
        "But then I remember how totally broke I am right now."
        "I sure could use the money the shift would earn me."
        menu:
            "Take the extra shift":
                "Ah, screw it - I need the money more than I need a social life."
                "And if I'm broke, I guess I shouldn't be going out partying anyway."
                "I nod and force a smile as I blow a massive hole in my own plans."
                bree.say "You know what..."
                bree.say "I will take that shift."
                bree.say "I won't lie - I could use the money."
                "The manager's face lights up for the first time in as long as I can remember."
                "Manager" "That's great, [hero.name]!"
                "Manager" "I knew you were a team player."
                "Manager" "I'll put you on the rota right now."
                "Manager" "And I'll keep you in mind for any more that pop up too, okay?"
                bree.say "Ah..."
                bree.say "Okay, I guess."
                "I can't help letting my shoulders sag as I walk away."
                "I keep telling myself how much the extra money is going to help."
                "After all, who needs a social life when you're trying to pay off student loans?"
                $ hero.energy -= 2
                $ hero.money += 25
            "Don't do it":
                "No, I'm not going to do it!"
                "I work really hard here as it is."
                "And then I have my studies on top of that too."
                "If I don't take time out to relax and unwind, I'm going to lose it!"
                bree.say "Oh..."
                bree.say "If it'd been any other date, I'd have taken it."
                bree.say "But I already have something SUPER important going on then."
                bree.say "So important that I can't possibly cancel it."
                "The manager's face sinks, making them look even worse than before."
                "Manager" "You're sure, [hero.name]?"
                "Manager" "Ah, that's too bad."
                "Manager" "I guess I'll just have to find someone else to cover it."
                "I shrug and offer up a helpless smile."
                "Then I turn and walk away to start my shift."
                "And once I'm out of hearing range, I let out a sigh of relief."
                "I might be broke."
                "But at least I'm not trapped here working for peanuts."
    return

label random_work_events_stripclub:
    $ r = randint(1, 5)
    if r == 1:

        "I'm going through my usual routine, almost zoning out as I take off my clothes."
        "I've got this thing down to a point where I can be thinking about something else entirely."
        "Like, I can be thinking about what I need to pick from the store on the way home."
        "Or be running through the coursework I have to do for college."
        "But suddenly something happens that snaps me right back to reality."
        bree.say "HEY!"
        bree.say "What the hell!"
        bree.say "Did one of you creeps just touch me?!?"
        "Most of the guys watching burst out laughing as I ask the question."
        "And the guy that's guilty of the offence just kind of shrugs and smiles."
        "Guy" "What's the matter, babe?"
        "Guy" "All I did was have a little squeeze!"
        menu:
            "Slap the guy":
                "I can't let guys like this take liberties whenever they want."
                "That's the easiest way to make people think they can do whatever."
                "The slap catches the guy totally off-guard, spinning his head around."
                bree.say "No touching, asshole!"
                "Luckily for me, most of the guys buddies seem to think this is hilarious."
                "And they add to his humiliation by laughing at his sorry ass."
                $ hero.charm += 1
            "Let it go":
                "I narrow my eyes at the guy, letting him know what I think."
                "And I seriously think about slapping him for good measure."
                "But then I stop myself, remembering that I need the money."
                "So I go back to my routine, trying to forget all about it."
                "But at the same time I keep a close eye on the guy."
                "And every time I see him laughing, I feel anger leaping up in my gut."
                $ hero.fun -= 1
    elif r == 2:

        "I'm doing my best to make the people watching me happy."
        "But there's this one guy that's just not feeling it."
        "No matter what I do, he just looks miserable as hell!"
        "So once I'm done, I make a point of talking to him."
        bree.say "Hey buddy..."
        bree.say "What's up?"
        bree.say "Did you not like the show?"
        "The guy looks up at me, surprised by the question."
        "Guy" "Wha...what?"
        "Guy" "Oh...oh no!"
        "Guy" "It was great, really great!"
        bree.say "Then what's the problem?"
        bree.say "You look like you just got some bad news!"
        "Guy" "I...I'm just depressed, I guess."
        "Guy" "And I thought coming here might cheer me up."
        menu:
            "Be sympathetic":
                "I give the guy a sympathetic smile."
                bree.say "Aw..."
                bree.say "That's too bad!"
                bree.say "Tell you what..."
                bree.say "Hang around for my next set, okay?"
                bree.say "And I'll see what I can do to cheer you up."
                "The guy seems to pick up a little at this."
                "Guy" "Okay, I'll be here!"
                "I nod and smile, walking away to get changed."
                "And I'm already thinking of what I can do for the guy."
                $ hero.charm += 1
                $ hero.energy += 1
            "Not my problem":
                "I frown at this and shake my head."
                bree.say "What do you think I am, huh?"
                bree.say "A therapist?"
                bree.say "Or a fucking clown?"
                "Guy" "No!"
                "Guy" "Of course not!"
                bree.say "Then do me a favour and cheer up or get lost!"
                "And with that, I storm off, leaving the guy to his misery."
    elif r == 3:

        "I've just finished my routine and gotten myself dressed."
        "Then I see the guy that booked me walking over with his wallet out."
        "I do the best I can to put a friendly smile on my face."
        "Because this part of the job can get really awkward."
        "The guy's just watched you taking your clothes off in front of him."
        "And now you have to make small-talk while he counts out the money!"
        "Guy" "Hey there..."
        "Guy" "I got your money here."
        "He hands over a bunch of notes and turns to leave."
        "But not before I flick through them and note something."
        bree.say "Whoa!"
        bree.say "Where'd you think you're going?"
        bree.say "This is fifty bucks short!"
        "Guy" "Bullshit!"
        "Guy" "That's what we agreed to!"
        "Guy" "Like you can even count that high too!"
        menu:
            "Stand up to the guy":
                "This guy's got to be twice my size, with his buddies to back him up too."
                "But you have to be tough to make it in this job, able to stand up for yourself."
                bree.say "Just fucking pay me what we agreed, okay?"
                bree.say "If not, your buddies are going to see a girl kick your ass!"
                "The guy chuckles and shakes his head."
                "Guy" "Sure, like you could take me!"
                bree.say "And how's that going to look, huh?"
                bree.say "Either you get your ass kicked by a girl."
                bree.say "Or else everyone sees you beating a woman!"
                "Realisation dawns on the guy's face."
                "And he curses under his breath as he pulls out the rest of the money."
                "I can't help smiling as he shoves it into my hand and hurries away."
                $ hero.money += 50
            "Let it go":
                "I think about arguing."
                "But the guy's twice my size."
                "Plus he has his buddies to back him up."
                bree.say "Fuck you, man!"
                bree.say "And good luck hiring another stripper in this town."
                bree.say "Because word of you pulling shit like this will spread real fast."
                "With that, I grab my stuff and storm off."
                $ hero.fun -= 2
    elif r == 4:

        "I'm about to start my usual routine, beginning to unbutton myself."
        "But almost as soon as I do, the guy that's hired me holds up his hand."
        "Guy" "Ah..."
        "Guy" "You don't have to do that!"
        "Puzzled I give him an awkward smile."
        bree.say "Erm..."
        bree.say "Yeah, you see..."
        bree.say "I kind do have to."
        bree.say "Otherwise it's technically not stripping."
        bree.say "And that's what you paid for!"
        "The guy shakes his head."
        "Guy" "I...I know."
        "Guy" "But I'd rather you danced with your clothes on."
        "Guy" "I like it better that way!"
        menu:
            "Keep your clothes on":
                bree.say "Whatever, buddy..."
                bree.say "You're the one paying for all this!"
                "I restart my routine, but this time I keep my clothes on."
                "Sure, it feels a little weird and not everything works this way."
                "But the guy seems to be very happy with the end result."
                "And once I'm finished, he's smiling from ear-to-ear."
                "What's more, when I check my money, I see he slipped me a little extra too!"
                $ hero.energy -= 1
                $ hero.money += 20
            "Insist on stripping":
                bree.say "Look, buddy..."
                bree.say "I'm a stripper."
                bree.say "So I'm gonna strip!"
                bree.say "Close your eyes if you don't like it!"
                "I start up my routine again, doing it just how I always do."
                "And I don't pay the guy too much attention until it's over."
                "So what if he didn't like it."
                "All that matters is that I got paid!"
    elif r == 5:

        "I'm getting ready to go when the guy that hired me walks up."
        "He looks a little nervous, and I see he has something behind his back."
        "Guy" "Erm..."
        "Guy" "I was wondering if..."
        "Guy" "Well...if you could maybe wear this?"
        "He pulls out what looks like a school-girl's uniform."
        "And I can see that he's really embarrassed to be asking."
        bree.say "You want me to dress as a school-girl?"
        "Guy" "Yes!"
        "Guy" "It's always been a fantasy of mine!"
        "Guy" "I know it's a little weird..."
        "Guy" "But I'd be willing to pay extra."
        menu:
            "Agree":
                "I shrug as I take the uniform from him."
                bree.say "You know what they say?"
                bree.say "The customer is always right."
                "What difference does it make what I'm wearing?"
                "The whole point is just to take it off anyway."
                "As soon as I have the uniform on, I start my routine."
                "The guy watches me from start to finish."
                "In fact, he never takes his eyes off me the whole time."
                "And when I'm done, he seems totally satisfied."
            "Refuse":
                "I shake my head as I shove the uniform back towards him."
                bree.say "I don't do personal fetishes, buddy."
                bree.say "I turn up, I take my clothes off, I get paid."
                bree.say "That's how this works."
                "The guy looks more than a little disappointed."
                "And he really doesn't pay much attention as I perform my act."
                "But he still pays me at the end, which makes it all worthwhile."
                "Maybe next time he'll get the message and not ask me for weird shit."
    return


label ask_for_a_job_homelessshelter:
    call expression f"ask_for_a_job_dialogues_1_{hero.gender}" from _call_expression_377
    "Shop owner" "Sure, the job is yours."
    if not game.flags.job_day:
        $ game.flags.job_day = "homelessshelter"
    elif not game.flags.job_night:
        $ game.flags.job_night = "homelessshelter"
    return

label ask_for_a_job_camgirl:
    "I heard about girl filming themselves for money. Maybe I can try."
    if not game.flags.job_day:
        $ game.flags.job_day = "bedroom4"
    elif not game.flags.job_night:
        $ game.flags.job_night = "bedroom4"
    return

label ask_for_a_job_model:
    call expression f"ask_for_a_job_dialogues_1_{hero.gender}" from _call_expression_378
    "Shop owner" "Sure, the job is yours."
    if not game.flags.job_day:
        $ game.flags.job_day = "model"
    elif not game.flags.job_night:
        $ game.flags.job_night = "model"
    return

label ask_for_a_job_pornstar:
    call expression f"ask_for_a_job_dialogues_1_{hero.gender}" from _call_expression_379
    "Shop owner" "Sure, the job is yours."
    if not game.flags.job_day:
        $ game.flags.job_day = "pornstar"
    elif not game.flags.job_night:
        $ game.flags.job_night = "pornstar"
    return

label ask_for_a_job_prostitute:
    call expression f"ask_for_a_job_dialogues_1_{hero.gender}" from _call_expression_380
    "Shop owner" "Sure, the job is yours."
    if not game.flags.job_day:
        $ game.flags.job_day = "prostitute"
    elif not game.flags.job_night:
        $ game.flags.job_night = "prostitute"
    return

label random_work_events_sexshop:

    scene bg sexshop
    "I've been trying to gear myself up for this moment ever since I started working at the sex shop."
    "Preparing my body and mind for the gruelling challenge of what lies ahead on this particular shift."
    "Because today it's my turn to handle the glory hole booth."
    "And from what I hear, it's going to be a busy one!"
    "By now I'm more than used to being naked at work, and it's not something I even notice."
    show breemc gloryhole nomc at center, zoomAt(1.5, (640, 1080))
    "So when I walk in through the door to the booth, I'm surprised by the coolness of the tiles beneath my bare feet."
    "And it's not just the floor that's covered in them either, the walls of the booth are tiled too."
    "I guess that's the only sensible thing to cover them with, based on what goes on in here."
    "Turning around slowly, I can see that there are four holes around the booth."
    "One in each of the walls to the side of the door and two in the one opposite."
    "They're obviously located at roughly the height of an average guy's junk."
    "And right now they just look like four circles of black as I wait for the customers to arrive."
    "I don't know if I'm supposed to be posing in some certain kind of way right now."
    "Or maybe I should be doing a little dance of some sort?"
    "You know, kind of as a preview to what the clients can expect when the show gets started?"
    "But just as I'm thinking it over, I swear I hear a sound on the other side of one wall."
    "Then I can't help taking a leap backwards and letting out a yelp of surprise."
    show breemc gloryhole rightman stand nomc with fade
    "Because a cock is suddenly and without ceremony, thrust through one of the holes."
    "It's the one on the left side of the booth from my point of view."
    "So naturally I leap to the right, flattening myself against the wall on the other side."
    bree.say "Argh!"
    bree.say "Oh..."
    bree.say "Erm..."
    bree.say "Hello there, I guess!"
    "I'm still staring at the first dick to appear as I feel an unexpected prick in my ribs."
    "Sorry, sorry...I know, I know!"
    "But you're just going to have to put up with awful puns like that."
    "The sensation sends me leaping back the other way as a second cock appears behind me."
    "But in moving back, I almost run into the first one."
    "For a moment I stop, looking one way and then the other."
    "Then I take a deep breath, close my eyes, and try to focus."
    "I can't be afraid of these things."
    "They're part of the job, and that's all there is to it."
    "So with my eyes still closed and controlling my breathing, I crouch down."
    show breemc gloryhole leftman nomc
    "Then I reach out my hands to the left and right, trying to guess where the cocks are located."
    "I feel one brush against the tips of my fingers, so I grab it without thinking."
    "My reward is to hear a grunt from the other side of the wall."
    "But the cock doesn't retreat, so I take that as a good omen."
    "Though reaching for the second one, I'm sure to take more care."
    scene breemc gloryhole
    show breemc gloryhole rightstand stand rightman leftman
    with fade
    "Pretty soon I have a cock in each hand, and I'm starting to stroke them both."
    "I know my way around a guy's equipment quite well, and so I don't open my eyes."
    "And I take the lack of grunts as well as the occasional gasp I hear as positives."
    "Maybe this isn't going to be so hard after all?"
    "It's while I'm thinking this that I hear a disgruntled cough."
    "No, wait...not one, but two!"
    "Huh...I wonder what could be the reason for that?"
    "I thought I was handling both of these guys pretty well."
    show breemc gloryhole rightstand rightman leftman dickright dickleft with fade
    "Opening my eyes to see what's wrong, I'm greeted with an unexpected sight."
    "There are another two cocks in the booth, just an inch from my face!"
    "Two more customers must have started using the holes while I had my eyes shut."
    "At least that would explain the sounds they were making."
    "I can't attend to someone if I don't know they're there in the first place!"
    "Now this is going to complicate things somewhat."
    show breemc gloryhole rightblowjob bj
    "I instantly open my mouth and start to lick at the tip of one newcomer."
    "But I only have one mouth and two hands."
    "So how am I supposed to keep four guys happy at once?"
    "As if to underline my dilemma, the unattended cock waggles in the air."
    "And it's owner thrusts it forward as far as possible."
    "Obviously he's getting pissed at being the only one left out of the action!"
    "Instantly I drop the cock to my right and take hold of the protesting member."
    "But a moment later the one that I just abandoned starts waggling around in protest."
    show breemc gloryhole rightstand stand
    "Urgh...if only I had an mouth or pair of hands!"
    "I feel like one of those guys you see spinning plates."
    show breemc gloryhole left leftstand
    "Running this way and that to keep them all going."
    "Maybe that's it?"
    "I can't service all four cocks at once."
    "But I can make sure they spend as little time as possible unattended."
    "With that in mind, I start moving around the booth with a plan."
    show breemc gloryhole left leftblowjob rightman leftman dickright dickleft
    "Going clockwise, I pass the cocks from hand to mouth and back to the other hand."
    "So each of them goes from one to the other with a small amount of time left alone."
    "Pretty soon it seems to be working out well."
    "The change from hand to mouth to hand keeps things fresh."
    "While there's not really enough time left unattended for it to really sink in."
    "I also find that I can begin to note different things about the cocks too."
    "I remember which ones seem to prefer the hand to the mouth."
    "And I even recall where they like to be touched and how hard or soft."
    "But what I'm not ready for is when they're going to go off."
    "I have no idea who these cocks belong to or how much stamina they possess."
    show breemc gloryhole cumdickleft
    "So when the first one shoots his load, it comes as a total surprise."
    "It just so happens to be the one that's not getting any attention."
    "I have my back turned to it, so the cum hits the back of my head."
    "Then it spatters all the way down my back."
    "I comfort myself with the thought that it's just the one."
    show breemc gloryhole cumdickright
    "But a moment later, the one in my left hand goes off too!"
    "What's going on here?"
    "Are they telepathically linked?"
    show breemc gloryhole left leftstand
    "Or has the sight of the one going off triggered all the others too?"
    "There are peepholes in the booth, so that seems the most likely explanation."
    show breemc gloryhole left leftstand leftcumshot with hpunch
    "The next moment the one in my right hand explodes too."
    show breemc gloryhole left leftstand -leftcumshot breeleftcum lwall
    "So I've been splattered from two sides in quick succession."
    show breemc gloryhole left leftstand
    pause 0.25
    show breemc gloryhole right rightstand breast
    pause 0.25
    show breemc gloryhole right rightblowjob bj
    "Then a thought occurs to me, and I look down at the cock still in my mouth!"
    "Quick as a flash, I pull my head back."
    "I'm just in time to keep it from going off in my mouth."
    "But not to keep it from hitting me in the face!"
    show breemc gloryhole right rightstand stand rightcumshot with hpunch
    "I take this last shot squarely between the eyes."
    "And it's a big one too, painting my face as it hits me."
    show breemc gloryhole -rightcumshot breerightcum rwall
    "All I can do is squat there, totally covered in fast-cooling cum."
    "I watch as the cocks begin to sag, and then retreat back into the holes."
    "Only when they're gone does it hit me."
    scene breemc gloryhole at center, zoomAt(1.5, (640, 1080))
    show breemc gloryhole nomc lwall rwall
    with fade
    "No, not more cum!"
    "I mean the realisation that I actually did it."
    "I took on four cocks at once and came out on top."
    "But a few seconds later I realise something else."
    "Something far more pressing."
    "I need a shower, and I need one now!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
