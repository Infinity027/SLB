init python:
    Event(**{
    "name": "reona_event_01",
    "label": "reona_event_01",
    "display_name": "Can you help me with my homework?",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 1,
    "conditions": [
        IsDone("reona_teaser"),
        HeroTarget(
            IsGender("male"),
            IsRoom("university"),
            "hero.sexperience >= 10",
            MinStat("knowledge", 50),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_event_02",
    "label": "reona_event_02",
    "display_name": "Sex shop meeting",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 1,
    "conditions": [
        IsDone("reona_event_01"),
        HeroTarget(
            IsGender("male"),
            IsRoom("sexshop"),
            "hero.sexperience >= 20",
            Not(OnDate()),
            ),
        PersonTarget(reona,
            IsPresent(),
            MinStat("love", 20),
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_event_03",
    "label": "reona_event_03",
    "display_name": "I got my exams! Let's celebrate",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 2,
    "conditions": [
        IsDone("reona_event_02"),
        IsHour(22, 5),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom", "bedroom1", "houselibrary"),
            "hero.sexperience >= 30",
            Not(OnDate()),
            ),
        PersonTarget(reona,
            Not(IsHidden()),
            Not(IsPresent()),
            MinStat("love", 60),
            MinFlag("study_help_count", 5),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_event_04",
    "label": "reona_event_04",
    "display_name": "Caught cheating!",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 1,
    "conditions": [
        IsDone("reona_event_03"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("pub"),
            "hero.sexperience >= 40",
            Not(OnDate()),
            ),
        PersonTarget(reona,
            Not(IsHidden()),
            IsPresent(),
            MinStat("love", 80),
            ),
        ],
    "do_once": True,
    })

    InteractEvent(**{
    "name": "reona_event_04b",
    "label": "reona_event_04b",
    "display_name": "Reverse caught cheating!",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 0,
    "conditions": [
        IsDone("reona_event_03"),
        HeroTarget(
            IsGender("male"),
            "hero.sexperience >= 40",
            ),
        PersonTarget(reona,
            IsActive(),
            MinStat("love", 80),
            ),
        ],
    "do_once": True,
    })

    InteractEvent(**{
    "name": "reona_event_05",
    "label": "reona_event_05",
    "display_name": "Let's have a real relationship",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 1,
    "conditions": [
        IsDone("reona_event_04", "reona_event_04b"),
        HeroTarget(
            IsGender("male"),
            "hero.sexperience >= 50",
            ),
        PersonTarget(reona,
            IsActive(),
            MinStat("love", 100),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_event_06",
    "label": "reona_event_06",
    "display_name": "Cinema and restaurant date",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 0,
    "conditions": [
        IsDone("reona_event_05"),
        HeroTarget(
            IsGender("male"),
            OnDate(),
            IsRoom("date_restaurant"),
            "hero.sexperience >= 60",
            ),
        PersonTarget(reona,
            OnDate(),
            MinStat("love", 120),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_event_07",
    "label": "reona_event_07",
    "display_name": "Angela's visit",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 1,
    "conditions": [
        IsDone("reona_event_06"),
        IsTimeOfDay("afternoon"),
        IsDayOfWeek("6"),
        HeroTarget(
            IsGender("male"),
            "hero.sexperience >= 70",
            IsRoom("date_livingroom"),
            ),
        PersonTarget(reona,
            OnDate(),
            MinStat("love", 140),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_event_08",
    "label": "reona_event_08",
    "display_name": "Date at the park",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 1,
    "conditions": [
        IsDone("reona_event_07"),
        HeroTarget(
            IsGender("male"),
            "hero.sexperience >= 80",
            IsRoom("date_park"),
            ),
        PersonTarget(reona,
            OnDate(),
            MinStat("love", 160),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_event_09",
    "label": "reona_event_09",
    "display_name": "Unworthy",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 1,
    "conditions": [
        IsDone("reona_event_08"),
        HeroTarget(
            IsGender("male"),
            "hero.sexperience >= 90",
            ),
        PersonTarget(reona,
            OnDate(),
            MinStat("love", 180),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_event_10",
    "label": "reona_event_10",
    "display_name": "Worthy",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 1,
    "conditions": [
        IsDone("reona_event_09"),
        HeroTarget(
            IsGender("male"),
            "hero.sexperience >= 100",
            IsRoom("date_livingroom"),
            ),
        PersonTarget(reona,
            OnDate(),
            MinStat("love", 200),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_kink_01",
    "label": "reona_kink_01",
    "display_name": "I love men with experience",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 0,
    "conditions": [
        IsDone("reona_event_04", "reona_event_04b"),
        MinDateScore(40),
        HeroTarget(
            IsGender("male"),
            "hero.sexperience >= 50",
            "len(hero.get_partners()) >= 4",
            OnDate(),
            ),
        PersonTarget(reona,
            MinStat("love", 100),
            MinStat("sub", 10),
            Or(
                IsFlag("cheating_agreement", "mc"),
                IsFlag("cheating_agreement", "both"),
                ),
            OnDate(),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_kink_02",
    "label": "reona_kink_02",
    "display_name": "Caught you",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 0,
    "conditions": [
        IsDone("reona_kink_01"),
        HeroTarget(
            IsGender("male"),
            "hero.sexperience >= 60",
            "len(hero.get_partners()) >= 8",
            ),
        PersonTarget(reona,
            MinStat("love", 120),
            MinStat("sub", 20),
            IsPresent(),
            Or(
                IsFlag("cheating_agreement", "mc"),
                IsFlag("cheating_agreement", "both"),
                ),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_kink_03",
    "label": "reona_kink_03",
    "display_name": "Tell me about her",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 0,
    "conditions": [
        IsDone("reona_kink_02"),
        HeroTarget(
            IsGender("male"),
            "hero.sexperience >= 60",
            "len(hero.get_partners()) >= 12",
            OnDate(),
            ),
        PersonTarget(reona,
            MinStat("love", 120),
            MinStat("sub", 40),
            IsPresent(),
            OnDate(),
            ),
        Or(
            PersonTarget(samantha,
                MinFlag("last_date_day", 1),
                MinStat("sexperience", 1),
                ),
            PersonTarget(sasha,
                MinFlag("last_date_day", 1),
                MinStat("sexperience", 1),
                ),
            PersonTarget(bree,
                MinFlag("last_date_day", 1),
                MinStat("sexperience", 1),
                ),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_kink_04",
    "label": "reona_kink_04",
    "display_name": "How many?",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 0,
    "conditions": [
        IsDone("reona_kink_03"),
        HeroTarget(
            IsGender("male"),
            "hero.sexperience >= 70",
            "len(hero.get_partners()) >= 16",
            ),
        PersonTarget(reona,
            MinStat("love", 130),
            MinStat("sub", 60),
            IsPresent(),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_kink_05",
    "label": "reona_kink_05",
    "display_name": "I wannna be your slave",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 0,
    "conditions": [
        IsDone("reona_kink_04"),
        HeroTarget(
            IsGender("male"),
            "hero.sexperience >= 80",
            "len(hero.get_partners()) >= 18",
            ),
        PersonTarget(reona,
            MinStat("love", 150),
            MinStat("sub", 80),
            IsPresent(),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_kink_06",
    "label": "reona_kink_06",
    "display_name": "I love being your slave",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 0,
    "conditions": [
        IsDone("reona_kink_05"),
        HeroTarget(
            IsGender("male"),
            "hero.sexperience >= 110",
            "len(hero.get_partners()) >= 20",
            ),
        PersonTarget(reona,
            MinStat("love", 200),
            MinStat("sub", 100),
            IsPresent(),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_redemption_01",
    "label": "reona_redemption_01",
    "display_name": "I want you to value yourself",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 1,
    "conditions": [
        IsDone("reona_event_01"),
        HeroTarget(
            IsGender("male"),
            IsRoom("university"),
            ),
        PersonTarget(reona,
            MinFlag("study_help_count", 1),
            IsFlag("study_blow", False),
            IsRoom("classroom"),
            MinStat("love", 80),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_redemption_02",
    "label": "reona_redemption_02",
    "display_name": "The Deep Conversation",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 1,
    "conditions": [
        IsDone("reona_redemption_01"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            ),
        PersonTarget(reona,
            IsPresent(),
            MinStat("purity", 20),
            MinStat("love", 100),
            Not(IsFlag("redemptiondelay")),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_redemption_03",
    "label": "reona_redemption_03",
    "display_name": "Meeting Mrs. Chen",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 1,
    "conditions": [
        IsDone("reona_redemption_02"),
        HeroTarget(
            IsGender("male"),
            OnDate(),
            IsRoom("date_maidcafe"),
            ),
        PersonTarget(reona,
            OnDate(),
            MinStat("purity", 40),
            MinStat("love", 120),
            Not(IsFlag("redemptiondelay")),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_redemption_04",
    "label": "reona_redemption_04",
    "display_name": "The Volunteer Experience",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 1,
    "conditions": [
        IsDone("reona_redemption_03"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("street"),
            ),
        PersonTarget(reona,
            IsPresent(),
            MinStat("purity", 60),
            MinStat("love", 130),
            Not(IsFlag("redemptiondelay")),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_redemption_05",
    "label": "reona_redemption_05",
    "display_name": "The Mirror Moment",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 1,
    "conditions": [
        IsDone("reona_redemption_04"),
        HeroTarget(
            IsGender("male"),
            OnDate(),
            ),
        PersonTarget(reona,
            OnDate(),
            MinStat("purity", 70),
            MinStat("love", 140),
            Not(IsFlag("redemptiondelay")),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_redemption_07",
    "label": "reona_redemption_07",
    "display_name": "The Commitment",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 1,
    "conditions": [
        IsDone("reona_date_forest"),
        HeroTarget(
            IsGender("male"),
            IsActivity("None"),
            ),
        PersonTarget(reona,
            IsActive(),
            MinStat("purity", 100),
            MinStat("love", 180),
            Not(IsFlag("redemptiondelay")),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_jack_01",
    "label": "reona_jack_01",
    "display_name": "Reona/Jack meeting",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 0,
    "conditions": [
        IsDone("reona_event_01"),
        HeroTarget(
            IsGender("male"),
            IsRoom("university"),
            ),
        PersonTarget(reona,
            Not(IsHidden()),
            IsRoom("classroom"),
            MinStat("love", 40),
            MaxStat("sexperience", 0),
            ),
        ],
    "do_once": True,
    })


    Event(**{
    "name": "reona_jack_01a",
    "label": "reona_jack_01a",
    "display_name": "The Campaign Invitation",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 0,
    "conditions": [
        IsDone("jack_event_04"),
        IsDone("reona_jack_01"),
        IsNotDone("reona_jack_01b"),
        IsDayOfWeek(6, 7),
        IsHour(14, 17),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            ),
        PersonTarget(reona,
            Not(IsHidden()),
            MinStat("love", 100),
            MaxStat("sexperience", 0),
            MinStat("purity", 10),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            HasRoomTag("home"),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            HasRoomTag("home"),
            ),
        PersonTarget(minami,
            Or(
                IsGone(),
                And(
                    Not(IsGone()),
                    Not(IsHidden()),
                    HasRoomTag("home"),
                    )
                ),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_jack_02a",
    "label": "reona_jack_02a",
    "display_name": "The Character Development Session",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 0,
    "conditions": [
        IsDone("reona_jack_01a"),
        IsNotDone("reona_jack_01b"),
        IsTimeOfDay("afternoon", "evening"),
        HeroTarget(
            HasRoomTag("home"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(reona,
            Not(IsHidden()),
            MinStat("love", 130),
            MaxStat("sexperience", 0),
            MinStat("purity", 30),
            IsFlag("campaign_delay", False),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_jack_03a",
    "label": "reona_jack_03a",
    "display_name": "The Emotional Campaign",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 0,
    "conditions": [
        IsDone("reona_jack_02a"),
        IsNotDone("reona_jack_01b"),
        IsTimeOfDay("afternoon", "evening"),
        HeroTarget(
            HasRoomTag("home"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(reona,
            Not(IsHidden()),
            MinStat("love", 170),
            MaxStat("sexperience", 0),
            MinStat("purity", 50),
            IsFlag("campaign_delay", False),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_jack_04a",
    "label": "reona_jack_04a",
    "display_name": "The Garden Day",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 0,
    "conditions": [
        IsDone("reona_jack_03a"),
        IsNotDone("reona_jack_01b"),
        IsTimeOfDay("afternoon"),
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(reona,
            Not(IsHidden()),
            MinStat("love", 190),
            MaxStat("sexperience", 0),
            MinStat("purity", 70),
            IsFlag("campaign_delay", False),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_jack_05a",
    "label": "reona_jack_05a",
    "display_name": "The Victory Celebration",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 0,
    "conditions": [
        IsDone("reona_jack_04a"),
        IsNotDone("reona_jack_01b"),
        IsDayOfWeek(6, 7),
        IsTimeOfDay("afternoon"),
        HeroTarget(
            HasRoomTag("home"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(reona,
            Not(IsHidden()),
            MinStat("love", 200),
            MaxStat("sexperience", 0),
            MinStat("purity", 90),
            IsFlag("campaign_delay", False),
            ),
        ],
    "do_once": True,
    })



    InteractEvent(**{
    "name": "reona_jack_01b",
    "label": "reona_jack_01b",
    "display_name": "Why don't you like Jack?",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 0,
    "conditions": [
        IsDone("reona_jack_01"),
        IsNotDone("reona_jack_01a"),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(reona,
            MinStat("love", 80),
            IsActive(),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_jack_02b",
    "label": "reona_jack_02b",
    "display_name": "Would you like to have fun with Reona?",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 0,
    "conditions": [
        IsDone("reona_jack_01b"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(HasRoomTag("work")),
            Not(HasRoomTag("home")),
            ),
        PersonTarget(reona,
            Not(IsHidden()),
            MinStat("love", 120),
            Not(OnDate()),
            Not(IsPresent()),
            IsFlag("help_virgin_jack", True),
            ),
        ],
    "chances": 25,
    "do_once": True,
    })

    Event(**{
    "name": "reona_jack_05b",
    "label": "reona_jack_05b",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 2,
    "conditions": [
        IsDone("reona_jack_04b"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            HasRoomTag("home"),
            ),
        PersonTarget(reona,
            Not(IsHidden()),
            MinStat("sub", 80),
            Not(OnDate()),
            IsFlag("help_virgin_jack", True),
            ),
        ],
    "do_once": True,
    })

    InteractActivity(**{
    "name": "date_study_with_reona",
    "rooms": "date_livingroom",
    "display_name": "Helping out & reward",
    "duration": 2,
    "conditions": [
        IsDone("reona_event_01"),
        IsNotDone("reona_enough_study"),
        IsHour(8, 22),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_livingroom"),
            MinStat("energy", 2),
            MinStat("hunger", 3),
            MinStat("grooming", 3),
            MinStat("fun", 1),
            MinStat("knowledge", 50),
            "hero.sexperience >= 20",
            ),
        PersonTarget(reona,
            IsActive(),
            OnDate(),
            MinStat("love", 20),
            ),
        ],
    "once_day": True,
    "display_name": "Help Reona study",
    "icon": "study",
    "label": "reona_study_help",
    })

    Event(**{
    "name": "reona_enough_study",
    "label": "reona_enough_study",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("reona_event_02"),
        PersonTarget(reona,
            MinStat("love", 40),
            MinFlag("study_help_count", 5),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "reona_preg_talk",
    "max_girls": 1,
    "label": "reona_preg_talk",
    "do_once": False,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(reona,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("toldpreg", False),
            MinCounter("pregnant", 6),
            ),
        ],
    })

    Event(**{
    "name": "reona_lose_nodate",
    "label": "reona_lose_nodate",
    "priority": 1500,
    "conditions": [
        PersonTarget(reona,
            IsFlag("nodate", True),
            MinStat("love", 200),
            ),
        ],
    "quit": False,
    "do_once": True,
    })

    Event(**{
    "name": "reona_gain_haircut",
    "label": "reona_gain_haircut",
    "priority": 1500,
    "conditions": [
        PersonTarget(reona,
            IsFlag("haircut", False),
            MinStat("purity", 50),
            ),
        ],
    "quit": False,
    "do_once": True,
    })

    Event(**{
    "name": "reona_gain_pure_casual",
    "label": "reona_gain_pure_casual",
    "priority": 1500,
    "conditions": [
        PersonTarget(reona,
            IsFlag("purecasual", False),
            MinStat("purity", 50),
            ),
        ],
    "quit": False,
    "do_once": True,
    })

    Event(**{
    "name": "reona_gain_pure_date",
    "label": "reona_gain_pure_date",
    "priority": 1500,
    "conditions": [
        PersonTarget(reona,
            IsFlag("puredate", False),
            MinStat("purity", 60),
            ),
        ],
    "quit": False,
    "do_once": True,
    })

label reona_lose_nodate:
    $ reona.flags.nodate = False
    return

label reona_gain_haircut:
    $ reona.flags.haircut = True
    return

label reona_gain_pure_casual:
    $ reona.flags.purecasual = True
    return

label reona_gain_pure_date:
    $ reona.flags.puredate = True
    return

label reona_enough_study:
    if reona.love.max < 60:
        $ reona.love.max = 60
    return

label reona_study_help:
    show reona
    mike.say "I'm all ready for the session, Reona..."
    mike.say "So we can jump straight in."
    mike.say "If you're ready, yeah?"
    "Rather than answering me, Reona scoots over."
    show reona at center, zoomAt(1.5, (640, 1040))
    "And she doesn't stop until she's pressed right up against me!"
    show reona happy leftback rightok
    reona.say "Okay, [hero.name]..."
    reona.say "Let's do it!"
    reona.say "Let's study!"
    show reona normal leftnormal rightnormal
    "I nod and smile, trying to ignore the fact Reona's leaning into me."
    "Which is pretty hard, as I can feel every curve on that side of her body!"
    "But nevertheless, I make a massive effort to keep my mind on the task at hand."
    "And I feel like I manage to do a pretty good job as a makeshift tutor."
    "I've decided to slow everything down for Reona's sake."
    "Not because I think she's dumb, but rather so I can get a handle on her abilities."
    "That way I can then figure out how to pace the lesson to suit her."
    "The odd thing is that I find it benefits me too."
    "Walking Reona through things I already know reaffirms them for me."
    "And she actually asks more than a few insightful questions too."
    with fade
    "So by the time we come to the end of the session, I'm feeling pretty positive."
    mike.say "That about wraps it up, Reona."
    mike.say "How did you feel that went?"
    mike.say "Because I found it really useful."
    "Reona doesn't hesitate to nod in agreement."
    show reona happy
    reona.say "Me too, [hero.name]."
    reona.say "I have to say, you're a great teacher!"
    "Reona pauses for a moment."
    "And she lets out a breathy sigh before going on."
    show reona normal righthold
    reona.say "Now then..."
    reona.say "How about you let me do something for you?"
    reona.say "Something nice so that I can return the favour?"
    "It's about now that I realise Reona has her hand on my crotch."
    "I swallow audibly and look down to confirm my suspicions."
    "And Reona seems to take this as encouragement."
    "Because she gives my cock a firm squeeze as I do so."
    reona.say "You did the written part of the test."
    show reona flirt
    reona.say "Why not leave the oral exam to me?"
    menu:
        "Alright, even though I'm sure you {b}suck{/b} at orals" if not "reona_redemption_01" in DONE:
            "Part of me can't believe this is actually happening right now."
            "I mean sure, I kind of hoped that it would go this way."
            "But you kind of have to manage your expectations, don't you?"
            "Otherwise you'd go insane waiting for a moment like this."
            mike.say "When you put it that way, Reona..."
            mike.say "I guess it's only fair!"
            show reona normal
            "Reona giggles at this, nodding eagerly."
            "At the same time she reaches over with her other hand too."
            "Then she begins to unzip my flies and reach inside."
            "I feel a genuine thrill at the sensation of her fingers touching my cock."
            "So much so that I can't keep a shiver from spreading through my entire body."
            $ reona.purity -= 2
            show reona flirt
            reona.say "Don't worry, [hero.name]..."
            reona.say "I promise that I'll be gentle!"
            hide reona
            show reona bj livingroom handjob squeeze mouth_lick mike
            with fade
            "Reona slides onto the floor as she says this."
            "And she parts my legs, kneeling between them."
            "She has my cock in one hand, massaging it gently."
            "But it's her lips that I'm watching as she lowers her head."
            show reona bj mouth_open tongueout
            "They part, beginning to kiss and caress the tip."
            "Then Reona licks it with her tongue, making me shiver all over again."
            "The difference is that this time she doesn't stop to offer me any reassurance."
            show reona bj suck -handjob -squeeze
            "Instead she opens her mouth wide, and swallows it without hesitation or warning."
            "She's using lips, tongue and teeth to great effect."
            "And I'm beginning to wonder just how deep she can take me."
            "I swear that I can feel the muscles of Reona's throat around my cock."
            show reona bj eyes_close
            "Her head is bobbing up and down too, ensuring my own pleasure rises."
            "I feel like I won't be able to take much more of this."
            "Like I'm going to explode any moment."
            "But still Reona keeps right on going, pushing me further all the time."
            mike.say "Urgh..."
            mike.say "Reona..."
            mike.say "I'm going to..."
            "I can't get the rest of my words out."
            "But Reona seems to get my meaning all the same."
            menu:
                "Cum on her face":
                    show reona bj eyes_open leftpeace rightpeace
                    "Reona looks up at me, then points to her face."
                    "Luckily that makes her intentions very clear."
                    "And I nod for her to go right ahead."
                    show reona bj out up
                    "Quick as a flash, Reona pulls my cock out of her mouth."
                    "Then she waits patiently for the inevitable to happen."
                    show reona bj cum eyes_close with vpunch
                    $ reona.sub += 2
                    "Seconds later I shoot my load straight into her face."
                    with vpunch
                    "Reona smiles happily as sticky white streaks paint her cheeks."

                    hide reona
                    show reona bj livingroom mouth_lick facecum mike leftpeace rightpeace
                    "And she licks up whatever lands on her lips too."
                "Cum in her mouth":
                    show reona bj eyes_open
                    "Reona looks up at me, then points to her throat."
                    "Luckily that makes her intentions very clear."
                    "And I nod for her to go right ahead."
                    show reona bj eyes_close
                    "Reona obliges me by closing her eyes and waiting for the inevitable too happen."
                    show reona bj cum with vpunch
                    $ reona.love += 4
                    "Seconds later I shoot my load straight into her mouth and down her throat."
                    with vpunch
                    "She takes it all in her stride, swallowing every drop without issue."
            $ game.active_date.score += 20
            $ reona.flags.study_blow = True
        "No need for oral practice today":
            "It's one hell of a tempting offer."
            "And I have to fight hard to find the strength to resist."
            "But in the end I manage to put a hand atop Reona's."
            "And, much to her evident surprise, I lift it off my groin."
            mike.say "It's okay, Reona..."
            mike.say "This session's on me, okay?"
            show reona leftback rightnormal annoyed at center, zoomAt(1.25, (640, 900))
            $ reona.love -= 2
            $ reona.purity += 1
            $ hero.knowledge += 1
            $ game.active_date.score -= 10
            "Reona pulls back her hand, still looking confused."
            "I get the distinct impression she's not often turned down like that."
            "But to her credit, she doesn't sulk or get upset with me."
            "Instead she just shrugs and shakes her head."
            reona.say "Whatever you say, [hero.name]."
            show reona leftnormal normal
            reona.say "But I think you're crazy just giving it away for free!"
    $ reona.flags.study_help_count += 1
    return

label reona_event_01:
    scene bg university with fade
    "I've been waiting for the results of the last test I sat to be released for what feels like forever."
    "So when I see that they've finally been posted on the results board, I can't help rushing straight over."
    "After double-checking I have the right list, I scan for my name."
    "Then I say a silent player to whatever God is listening, and I trace the line across to see my grade."
    "And when I do, I can't contain myself any longer."
    mike.say "Oh yeah!"
    mike.say "Now that's what I'm talking about!"
    mike.say "Hail to the king, baby!"
    "Suddenly I realise that I'm in a public place and surrounded by dozens of other students."
    "And so I instantly shut up, staring at my feet as I shuffle away from the results board."
    "I can still feel the sense of embarrassment burning away inside of me when there's a tap on my shoulder."
    "I turn slowly, fully expecting to be told off by a fellow student that got a worse grade than me."
    "But instead I'm surprised to see a familiar face, and it's actually smiling at me."
    show reona casual happy leftback rightopen with dissolve
    reona.say "Hey, [hero.name]..."
    reona.say "Fancy bumping into you here!"
    "I recognise the girl standing in front of me."
    "But for a moment her name seems to escape me."
    mike.say "Oh..."
    mike.say "Hey...Reona?"
    "I smile as the name pops into my head."
    "And I'm hoping the whole time I've got it right."
    show reona leftpeace rightpeace
    reona.say "That's me..."
    reona.say "The one and only!"
    "Reona adds a giggle afterwards, and then a gentle shove on the shoulder."
    "All of which only serves to make me smile all the more."
    "Because it reminds me of just how hot Reona is."
    mike.say "So, Reona..."
    mike.say "You go here too?"
    mike.say "I mean, you're studying here?"
    show reona leftnormal rightnormal
    "Reona nods, and giggles again."
    reona.say "Yeah, I am."
    reona.say "It's crazy, you know?"
    reona.say "I thought I'd be done with all this stuff once I left highschool."
    show reona annoyed leftback
    reona.say "But here I am, still fucking studying!"
    "Reona rolls her eyes, like it's all a massive pain in the ass."
    "And all I can do in return is nod and smile."
    show reona normal leftnormal
    reona.say "You're a pretty smart guy, right?"
    reona.say "I mean, like..."
    reona.say "You looked like you aced that test on the board?"
    "Suddenly I feel like I'm being put on the spot."
    "But there's no way I can deny what just happened."
    mike.say "Well..."
    mike.say "I did okay, I guess."
    show reona happy
    reona.say "Oh come on, don't be so modest."
    reona.say "You totally passed with honours!"
    "It's hard to deny something like that at the best of times."
    "Especially when you're being praised by a girl as cute as Reona."
    mike.say "I suppose I am doing pretty well on my course."
    reona.say "I bet you are, [hero.name]."
    show reona normal
    reona.say "But the thing is...I'm not."
    reona.say "And I was wondering if you'd help me out?"
    reona.say "You know, like help me study some time?"
    menu:
        "Agree to help Reona study":
            "Is she actually serious?"
            "I'd have paid her for the chance to spend time in the same room!"
            "Sure, I'm more than a little pressed for time at the moment."
            "But I'm sure I can squeeze her in somewhere."
            mike.say "Are you kidding, Reona?"
            mike.say "It'd be my pleasure to help you study!"
            show reona happy
            "Reona's eyes light up as she hears me agree to her request."
            show reona leftback righthold at center, zoomAt(1.5, (640, 1040))
            "She's smiling seductively as she leans in closer too."
            reona.say "Oh, you won't regret spending your time with me, [hero.name]."
            reona.say "And I'll make sure you're very well rewarded for your efforts too."
            show reona flirt
            reona.say "Very well rewarded indeed..."
            "Reona looks straight into my eyes as she says all of this."
            "And just by doing that I can somehow tell what she's implying."
            "All of this means I know that I just made the right decision."
            mike.say "Ah..."
            mike.say "Y...yeah, Reona..."
            mike.say "I'm sure we can come to some kind of arrangement!"
            show reona normal
            "Reona nods happily, still close enough for our lips to touch."
            show reona casual rightnormal at center, traveling(1.0, 1.0, (640, 720))
            "Then she pulls back slowly."
            "As if letting me drink in the sight of her one more time."
            reona.say "Okay then..."
            show reona happy rightopen
            reona.say "I'll drop you a line when I'm free."
            reona.say "And we can hook up at your place."
            show reona at center, zoomAt(1.0, (840, 720)) with ease
            "With that, Reona turns on her heel and walks away."
            hide reona with easeoutright
            "I stand and watch her go, only snapping out of it once she's gone."
            "Seriously, it's like a spell's broken or something."
            "And I hurry off to my next lecture."
            "Part of me still unable to believe all that really just happened."
            $ reona.unhide()
        "Refuse to help Reona study (Never meet Reona again)":
            "Is she actually serious?"
            "I'm not a tutor."
            "And I have my own studies to think about."
            "Not to mention my job and all my other commitments!"
            mike.say "Ah..."
            mike.say "I'd love to help, Reona..."
            mike.say "But I have too much on my plate right now."
            "Reona doesn't seem discouraged by my refusal at first."
            show reona leftback righthold at center, zoomAt(1.5, (640, 1040))
            "Instead she keeps right on smiling, and leans in closer."
            reona.say "Oh, you wouldn't need to spend too much time on me, [hero.name]."
            reona.say "And I'd make sure you got very well rewarded for it too."
            show reona flirt
            reona.say "Very well rewarded indeed..."
            "Reona looks straight into my eyes as she says all of this."
            "And just by doing that I can somehow tell what she's implying."
            "Which is almost enough for me to change my mind on the spot."
            "But then I remember how important my studies are."
            "And how little time I already have to devote to them."
            mike.say "Sorry, Reona..."
            mike.say "But the answer is still no."
            mike.say "Check out the college website."
            mike.say "There are always ads for tutors on there."
            show reona angry
            "Reona opens her mouth to protest."
            hide reona with dissolve
            "But I walk away before she can speak."
            "And boy, is that ever a hard thing to do!"
            "Because I can't get that image out of my head."
            "The one of her all but offering herself to me."
            "And only in return for a little coaching too!"
    return

label reona_event_02:
    if reona.love.max < 40:
        $ reona.love.max = 40
    scene bg sexshop
    "I'm just minding my own business, browsing the aisles of the local sex shop."
    "Okay, okay...I know how that sounds!"
    "But seriously, this is the twenty-first century and I'm a sexually-liberated modern guy."
    "So if I want to walk into a sex shop and buy something to pleasure myself, then I will!"
    "Now that we've got that sorted out, let's get back to the matter at hand."
    "The only problem is that I have no idea what most of this stuff is supposed to actually do!"
    "Everything that I look at either baffles me or leaves me outright terrified to even try."
    "Pausing for a moment, I take a step back and looking at the rack upon rack of dildos."
    "Part of me feels kind of jealous of girls in that instant."
    "Because for them, picking something like that must be so much more interesting."
    "I mean, you can choose size, colour, material and whether or not it takes batteries."
    "Or you could just go for literally the biggest damn dildo in the place."
    "Which is what the girl I happen to see start browsing seems to be doing!"
    "Seriously, I do the best I can to tear my eyes away from her."
    "Because I know the last thing she needs is some guy staring at her in a place like this."
    "But the sheer size of the toys that she has in her hands is making my eyes water."
    "Good gods - she must never be able to get enough!"
    "That's about the time she just so happens to look up and see me watching her."
    "And just as my head is about to spin in the opposite direction, I recognise the girl."
    show reona happy leftback rightopen with dissolve
    reona.say "Hey, [hero.name]..."
    reona.say "Fancy seeing you here!"
    mike.say "Oh..."
    mike.say "Hi, Reona..."
    "My eyes can't help but wander down to the dildos she's holding."
    "And then they rise back up to meet Reona's own eyes."
    mike.say "I see you're doing a little bit of shopping?"
    show reona normal rightnormal
    "Reona's face breaks into a knowing smile."
    "And she kind of shakes her head from side to side."
    "Not denying the accusation, but more revelling in its implications."
    reona.say "I sure am."
    show reona leftnormal
    reona.say "You know how it is, yeah?"
    reona.say "No matter how many of these things you buy..."
    show reona flirt rightok
    reona.say "You always want a bigger one."
    reona.say "Am I right?"
    with vpunch
    "All I can do is laugh and nod at the question."
    mike.say "Oh yeah, Reona..."
    mike.say "It's always that way!"
    "Reona doesn't seem to notice the nervous tone in my voice."
    "Instead she appears to take it as my complete and total agreement."
    show reona normal rightnormal at center, zoomAt (1.5, (640, 1040))
    reona.say "Yeah, [hero.name]..."
    reona.say "You know how it is."
    "It's right about now that I see Reona's gaze fall on the racks in front of me."
    show reona happy
    "And a look of knowing amusement spreads over her face as she does so."
    reona.say "Looks like you're shopping for a thrill too."
    reona.say "Am I right?"
    "I think about denying it and trying to come up with an excuse."
    "But then I realise that would be a pretty stupid thing to do."
    "Maybe it would have worked with a more pure and innocent girl."
    "But Reona seems to be totally at ease with this kind of thing."
    "So she'd be sure to see through me in an instant."
    mike.say "Ah..."
    mike.say "Yeah, Reona..."
    mike.say "I was just looking at the stuff they have here for guys."
    mike.say "But the problem is that I'm not exactly up on this sort of stuff."
    mike.say "I mean, a lot of it looks like torture devices to me!"
    show reona interested
    "Suddenly Reona has a different look on her face."
    "And it's one that I'm really not used to seeing."
    "Instead of totally lascivious, she seems almost contemplative."
    reona.say "Hmm..."
    show reona happy
    reona.say "Well, some of that stuff is definitely meant for sado-masochistic play."
    "I can't help flinching at the mere mention of the subject."
    "And to my surprise, Reona appears to notice and change her tone."
    show reona normal rightopen
    reona.say "But if you're not into that kind of thing..."
    reona.say "There's a lot of stuff that's more vanilla."
    mike.say "I hope you don't mind me saying, Reona..."
    mike.say "You seem to know an awful lot about this stuff!"
    show reona happy rightnormal leftpeace
    reona.say "Well I do work here."
    reona.say "So I have to know my stuff."
    "All I can do is nod, guessing that it figures."
    "But I don't have much time to mull the information over."
    "As without being asked, Reona starts to show me different devices."
    show reona righthold leftback
    reona.say "This is kind of like a robot pussy, [hero.name]..."
    reona.say "It has a ton of different settings too."
    show reona normal
    reona.say "You know, depending on how rough or gentle you want it?"
    mike.say "Oh..."
    mike.say "That's...fascinating..."
    show reona happy rightok
    reona.say "We just got these really sweet fake assholes in too."
    reona.say "Nice and tight!"
    mike.say "You don't say?"
    reona.say "We also have some pretty nice penis pumps over here."
    show reona devious rightnormal leftnormal
    reona.say "Or there are extenders, if that's more your kind of thing?"
    mike.say "Erm..."
    mike.say "I think I'm okay with the size and length I already have."
    mike.say "I'm more interested in stimulation than enhancement."
    show reona happy
    reona.say "Suit yourself..."
    "I take a second look at all the dildos Reona's clutching."
    "And she seems to take note of my interest."
    show reona normal righthold dildo
    reona.say "You like dildos and vibrators?"
    mike.say "Kind of, Reona..."
    mike.say "But those aren't meant for guys like me!"
    show reona devious leftback at startle
    "Reona giggles and shakes her head, like I said something stupid or cute."
    reona.say "You're kidding, right?"
    reona.say "All kinds of guys use dildos..."
    reona.say "Gay, straight and everything in between!"
    show reona normal
    reona.say "In fact, we have some really cool prostate massagers right here."
    with fade
    "The conversation goes on like this for some time."
    "And once it's winding down, I feel like I need to push my eyes back into their sockets."
    scene bg sexshop
    show reona
    with fade
    "Reona leads me over to the counter with my purchases, where the cashier rings them up."
    "I take out my loyalty card and let the cashier scan it."
    "Which is when Reona leans over my shoulder and whispers into my ear."
    show reona happy
    reona.say "I see you're a member of the loyalty program?"
    mike.say "Y...yeah, Reona..."
    mike.say "I have my card right here!"
    show reona normal
    reona.say "In that case, I have a special offer for you."
    reona.say "Come in the back with me right now."
    show reona flirt rightok leftback
    reona.say "And I'll give you some oral validation!"
    menu:
        "I'd like that very much":
            "I don't need to have Reona's true meaning explained to me."
            "Because I always seem to have that kind of thing on my mind around her anyway."
            "Taking a moment to glance around the store, I see that it's pretty empty right now."
            "So there doesn't seem to be any danger in accepting the offer."
            mike.say "Sounds good to me, Reona..."
            mike.say "Lead the way."
            show reona rightnormal
            "Reona nods eagerly and takes my hand."
            "She gives the girl behind the till a nod."
            "And when she gets one in return, I realise she must be in on it too!"
            "But I tell myself that just means we'll have someone sympathetic watching our backs."
            "I also make a point of trying not to wonder just how often this kind of thing happens around here."
            "Reona leads me straight into the back of the shop, amongst shelves and racks of stock."
            "And as soon as we're in there, she kneels straight down in front of me."
            scene bg black
            show reona bj sexshop mike
            with fade
            "I kind of appreciate the way Reona gets on with business."
            "She unzips my flies and reaches inside with one hand."
            "I can't help gasping as I feel her grab hold of my cock."
            "And I really do mean that she grabs hold of it."
            "The same no nonsense attitude applying to this part of the task too."
            "My cock is already getting hard by the time Reona pulls it out."
            "So all she has to do is keep on stroking the shaft to finish off the job."
            "Even before it's fully hard, she's already leaning in and parting her lips."
            show reona bj suck
            "I'm able to keep watching right up until Reona actually takes it into her mouth."
            "But from that point on the sensation is so intense that my eyes close as a matter of course."
            "The way that Reona goes about giving me head is the same as the way she pulled out my cock."
            "She simply goes for it, without any complications or embellishments."
            "Lips and tongue wrap themselves around it with astonishing dexterity."
            "But not everything that Reona brings into play is as soft."
            "More than once I feel her bring her teeth into play too."
            "Nibbling and biting when it's least expected, so that I twitch and flinch."
            "Of course that only serves to add to the excitement that I'm feeling."
            "Not knowing when she might choose to bite instead of lick."
            "I can't see Reona's head moving, but I can certainly feel it."
            "It's bobbing back and forth the whole time, steady as can be."
            "But now I can feel her beginning to pick up speed."
            "And it's not just the movements of her head that effects either."
            "The same thing seems to be happening to all of the part of her body Reona's using too."
            "Her teeth bite harder and more often."
            "Her tongue is almost lashing the length of my cock."
            "Her lips are massaging anywhere her tongue doesn't touch."
            "The overall effect is that I feel like I'm being overwhelmed."
            "And I know that I won't be able to go on like this much longer."
            mike.say "Reona..."
            mike.say "Hey, Reona..."
            "I open my eyes and look down for the first time in what feels like ages."
            "And I'm relieved to see that Reona's eyes are open too."
            "She's looking up at me, evidently having heard me just now."
            mike.say "I think..."
            mike.say "I think I'm going to..."
            "I don't even have to finish what I was going to say."
            "Because Reona gives me a thumbs up, to show that she understands."
            "The next moment she points to her mouth."
            "Then she gestures to her face."
            "In an instant I get that she wants to know how to finish me off."
            "Whether I want her to swallow or take it in the face."
            menu:
                "Ask her to swallow":
                    mike.say "Can you swallow?"
                    "Reona nods as soon as I ask the question."
                    "And within moments I feel the inevitable happening."
                    show reona bj cum eyes_close with vpunch
                    "I gasp and moan as I start to cum, losing it in her mouth."
                    with vpunch
                    "But Reona's more than prepared and takes it all in her stride."
                    show reona bj cum eyes_open with vpunch
                    "She swallows every last drop without fail, not gagging even once."
                "Ask her to take it on her face":
                    mike.say "F...facial?"
                    "Reona nods as soon as I ask the question."
                    "And within moments I feel the inevitable happening."
                    "But Reona's more than prepared and takes it all in her stride."
                    show reona bj -suck
                    "She pulls my cock out of her mouth, as I lose it."
                    show reona bj cum
                    with vpunch
                    "And when I shoot my load into her face, she doesn't flinch once."
            scene bg sexshop at blur(16), dark with dissolve
            "Afterwards, we quickly clean ourselves up and check the coast is clear."
            scene bg sexshop
            show reona
            with dissolve
            "Then Reona leads me to the exit and hands me my purchases in a bag."
            reona.say "Thanks for being such a good customer, [hero.name]."
            show reona flirt
            reona.say "I hope you come back soon!"
            "I nod and smile, still more than a little high on what she just did to me."
            hide reona with dissolve
            "Then I wander out of the door and off down the street."
            "Already wondering what excuse I can dream up to go back there real soon."
            $ reona.purity -= 2
        "I'm kinda in a hurry, maybe next time?":
            "I'm already feeling more than a little flustered."
            "And so the offer from Reona kind of pushes me over the edge."
            "I take a very deliberate step away from her and shake my head."
            show reona surprised righthold
            mike.say "Thanks for the offer, Reona."
            mike.say "But there's somewhere else I really have to be."
            mike.say "Maybe next time, okay?"
            "Reona looks more than a little shocked at being turned down."
            show reona normal
            "But she seems to recover pretty quickly, regaining her composure."
            reona.say "Whatever you say, [hero.name]."
            reona.say "No pressure from me."
            show reona rightnormal
            reona.say "But there might not be a next time."
            reona.say "Just keep that in mind."
            "With that, Reona thrusts the bag containing my purchases into my hands."
            "And from the look on her face, I get the impression that it's time for me to leave."
            hide reona with dissolve
            "I nod and hurry towards the exit."
            "Not pausing to look back before I'm out of there."
            $ reona.purity += 1
    $ game.room = "alley"
    return

label reona_event_03:
    if reona.love.max < 80:
        $ reona.love.max = 80
    "I really wasn't planning to go out tonight, in fact I was just going to stay in and study."
    play sound cell_vibrate loop
    "But the very moment that I put down the pile of books I need to work my way through, my phone rings."
    "Muttering to myself, I pull it out and check the caller ID."
    "I'm fully expecting it to be someone that I have no desire to talk to."
    if "reona" in hero.smartphone_contacts:
        "But then I see that the call is from Reona, and my interest is instantly piqued."
        $ result = renpy.call_screen("smartphone_choice", "Reona")
        stop sound
        if not result:
            $ hero.cancel_event()
            $ reona.love -= 5
            return
        mike.say "Hey, Reona..."
    else:
        $ result = renpy.call_screen("smartphone_choice")
        stop sound
        if not result:
            $ hero.cancel_event()
            return
        mike.say "[hero.name] speaking."
        $ hero.smartphone_contacts.append("reona")
    reona.say "Hi, [hero.name]..."
    mike.say "This is a surprise!"
    mike.say "I wasn't expecting to hear from you tonight."
    reona.say "Oh, I'm full of surprises!"
    reona.say "You should have figured that out by now."
    mike.say "Erm..."
    mike.say "So what can I do for you?"
    mike.say "Is it time for another study session already?"
    reona.say "That's what I'm calling about."
    reona.say "I just got my exam results."
    mike.say "You did?"
    mike.say "Come on, Reona, don't leave me in suspense!"
    reona.say "I totally passed!"
    reona.say "And it's all thanks to you, [hero.name]."
    "I can feel my head starting to swell almost as soon as Reona says those words."
    "But I do the best I can to sound self-deprecating, even if it's only for the sake of appearances."
    mike.say "Oh, I don't know about that..."
    reona.say "Ah, stop trying to be all like humble and that, [hero.name]!"
    reona.say "I was so going to fail before you came along."
    mike.say "Well..."
    mike.say "Maybe I did help out more than a little."
    "All of a sudden, Reona's tone changes."
    "And I can almost picture her waving her hands in the air."
    "Like she's trying to change the subject."
    reona.say "Okay, okay..."
    reona.say "Enough about the boring part."
    reona.say "Now it's time to celebrate, just you and me."
    reona.say "I'm taking you to a club - tonight!"
    menu:
        "Tonight's not the night, sorry...":
            "I shake my head, even though I know Reona can't see me doing so."
            mike.say "Oh no, Reona..."
            mike.say "I couldn't possibly go out tonight."
            reona.say "WHAT?!?"
            reona.say "Why's that?"
            mike.say "I just sat down to start studying."
            mike.say "And I have a lot to get through."
            reona.say "Aw, come on..."
            reona.say "All work and no play, you know?"
            "It's more than a little tempting."
            "But I resolve to stay true to my plans."
            mike.say "I can't, Reona..."
            mike.say "And this is how I helped you out in the first place, remember?"
            mike.say "If I start slacking-off, then who's going to help you next time?"
            "There's a pause on the other end of the line."
            "And that can only be on account of Reona thinking it over."
            "Then she lets out a groan of surrender."
            $ reona.love -= 4
            reona.say "Urgh..."
            reona.say "You're one smart guy, [hero.name]."
            reona.say "But just don't get too clever for your own good."
            "With that, Reona ends the call."
            "Which leaves me to get back to my studies."
            "Though I can't help wondering what she meant by that last comment."
            "And as the night goes on, it starts to bug me more and more."
        "You're right, let's celebrate this together!":
            "I look at the stack of books as I mull it over."
            "And it occurs to me that I did put in a lot of work on Reona."
            "Plus all of that had to count as me studying too, right?"
            "So I can afford to ease off a little, and I do deserve a reward too."
            mike.say "You're on, Reona..."
            mike.say "Just tell me where and when."
            reona.say "Yay!"
            reona.say "I knew you were smart, [hero.name]."
            reona.say "And I promise you won't regret it too!"
            "Reona quickly fills me in on the details."
            "Then I head out of the door and hurry to meet her."
            scene bg nightclub
            show reona date happy leftback
            with fade
            "And within what feels like mere minutes, we're inside of the club."
            "It's kind of bewildering, what with all the noise and the lights."
            "Plus I feel like I was staring at my books a few seconds ago."
            "So everything has an almost unreal quality to it."
            show reona date happy leftback at center, zoomAt(1.5, (640, 1040)) with fade
            "But for all of my confusion, Reona's totally focused."
            "She has a tight hold of my hand, squeezing it the whole time."
            "Like she's determined not to let go of me for as much as a second."
            "I'm about to make a comment about the place."
            "Not to complain about the noise, but to say it looks exciting."
            "But I don't get the chance, as Reona jerks me straight onto the dance-floor."
            hide reona
            show dance reona date
            with hpunch
            mike.say "Whoa..."
            mike.say "Slow down, Reona!"
            reona.say "Huh?"
            reona.say "Why would I do that?"
            reona.say "We're here to party, [hero.name]..."
            reona.say "So let's fucking party already!"
            "I shrug as I find myself dragged into the crowd of moving bodies."
            "Reona's right - why am I even thinking of holding back?"
            "So I just forget about everything else and let her take the lead."
            "And is that ever something that I don't regret!"
            "Reona doesn't hesitate to take charge."
            "And she doesn't seem to move more than an inch from me too."
            "Seriously, the crowd is pressing in on us the whole time."
            "But I get the impression Reona would still be wrapped around me without them."
            "Sure, I've been close to her on more than one occasion in the past."
            "But it was never like this before, never this sensual and arousing."
            "If this is Reona's way of thanking me for helping her study, then I like it!"
            "I just wish more of the girls that I've helped out over the years paid me in the same way."
            "Oh, and don't think that I'm standing there like a statue either."
            "There's no way I can help but put my hands all over Reona too."
            "And the more I do, the more she seems to like it as well!"
            "In fact, we're so close together and things are getting so intimate..."
            "I'm starting to think that she's going to make me cum in my shorts!"
            "That's when I feel one of Reona's hands on my groin."
            "At first she's only stroking it, but then she starts to squeeze it too."
            mike.say "Uh..."
            mike.say "Reona..."
            mike.say "You're gonna make me..."
            hide dance
            show reona date devious righthold leftback at center, zoomAt(1.5, (640, 1040))
            "As if reading my mind, Reona puts a finger to my lips."
            reona.say "Oh no, [hero.name]..."
            reona.say "Not here!"
            "I feel Reona take hold of my hand again, pulling me off the dance-floor."
            show reona date devious righthold leftback at center, zoomAt(1.5, (540, 1040)) with ease
            "It looks like she's headed towards the bathrooms."
            "And from the look in her eye, I think I know what she has planned!"
            menu:
                "Let her guide you there":
                    "I do the best I can to make it look like I'm not hurrying after her."
                    "At least a little like Reona has to drag me into the bathroom."
                    "But the truth is that I want to shove her straight through the door myself!"
                    "All the emotions and desires that have built up on the dance-floor need releasing."
                    "And I just know that Reona has to be the one to release them for me."

                    scene bg publicbathroom with fade
                    "As soon as the door closes behind us, Reona hustles me into one of the cubicles."
                    "I slam the door and shoot the bolt as quickly as I possibly can."
                    "Then I turn around, sure that I'm ready for what's coming next."
                    "But what I see stops me dead in my tracks."
                    show reona doggy publicbathroom with fade
                    "Reona has her back to me, bending over so her ass is thrust out."
                    "She's already managed to hitch up her skirt."
                    "And as I turn, I see that she's starting to pull down her panties too!"
                    "Reona looks back over her shoulders, a knowing smile on her face."
                    reona.say "This is your real reward, [hero.name]."
                    reona.say "You know you want it."
                    reona.say "All you gotta do is come and take it!"
                    "I can feel my head nodding as I take a step forwards."
                    "I can feel my hands unzipping my flies too."
                    "But all the time I'm still staring right between Reona's thighs."
                    "By now she has her panties down to her knees."
                    "Which means that I can see my ultimate goal."
                    show reona doggy mike
                    "It's right there, pink, soft and already glistening under the harsh lighting."
                    "I don't need to hold my cock in order to guide it home."
                    "The sight of Reona's pussy has already made me hard as an iron rod."
                    "All I need to do is grab hold of her waist and thrust myself forwards."
                    show reona doggy eyes_closed mouth_pleasure vaginal
                    "And as it's shoved between her thighs, Reona let's out a gasp of approval."
                    "In that moment she sends me an important message about what she wants."
                    "Reona lets me know that she doesn't want me to hold back."
                    "And that's more than okay with me."
                    show reona doggy mouth_normal
                    "Reona's wriggling backwards and I'm pushing forwards."
                    "Which means that we meet in the middle and it just happens."
                    "I'm hard enough and she's slick enough that it just squeezes right in there."
                    reona.say "Mmm..."
                    reona.say "Oh yeah..."
                    show reona doggy eyes_normal mouth_teeth
                    reona.say "Oh fuck yeah!"
                    "Reona pretty much sums up what I'm feeling too."
                    "But for me there's no time to put it into words."
                    show reona doggy smash eyes_pleasure
                    "Instead I begin to move back and forth, not pausing for a moment."
                    "And I don't mean that I start slowly and build up either."
                    show reona doggy -smash
                    pause .35
                    show reona doggy smash mouth_pleasure
                    pause 0.1
                    show reona doggy bounce
                    pause 0.15
                    show reona doggy rest
                    pause 0.35
                    show reona doggy -smash
                    pause 0.35
                    show reona doggy smash
                    pause 0.1
                    show reona doggy bounce
                    pause 0.15
                    show reona doggy rest
                    "Right from the word go, I'm thrusting in and out of her."
                    "Pounding away at Reona as if my life depends on it."
                    "And all that seems to do is make her like it all the more."

                    "Rather than trying to see what I'm doing, she simply surrenders to it."
                    "By now all the sounds that she's making are animalistic in nature."
                    "And she's making me feel the same way too, like there's nothing else on my mind."
                    "You can say what you like about taking your time and making things romantic."
                    "But right now there's nothing I can think of that could be better than this."
                    "Fucking a girl that wants it so badly as hard as I possibly can."
                    show reona doggy -smash
                    pause 0.3
                    show reona doggy smash eyes_closed
                    pause 0.1
                    show reona doggy bounce
                    pause 0.15
                    show reona doggy rest
                    pause 0.3
                    show reona doggy -smash
                    pause 0.3
                    show reona doggy smash
                    pause 0.1
                    show reona doggy bounce
                    pause 0.15
                    show reona doggy rest
                    pause 0.3
                    show reona doggy -smash
                    pause 0.3
                    show reona doggy smash
                    pause 0.1
                    show reona doggy bounce
                    pause 0.15
                    show reona doggy rest
                    "Every ounce of effort I put in, Reona devours it with a ravenous hunger."
                    "For a time, I actually think that I'm not going to be able to satisfy her."
                    "That her desire is going to prove to be too much for me to handle."
                    show reona doggy -smash
                    pause 0.25
                    show reona doggy smash
                    pause 0.1
                    show reona doggy bounce
                    pause 0.15
                    show reona doggy rest
                    pause 0.25
                    show reona doggy -smash
                    pause 0.25
                    show reona doggy smash
                    pause 0.1
                    show reona doggy bounce
                    pause 0.15
                    show reona doggy rest
                    pause 0.25
                    show reona doggy -smash
                    pause 0.25
                    show reona doggy smash eyes_ahegao mouth_teeth
                    pause 0.1
                    show reona doggy bounce
                    pause 0.15
                    show reona doggy rest
                    "Suddenly I feel Reona beginning to shake, to twitch from head to toe."
                    "And it's with a genuine sense of relief that I realise she's starting to cum."
                    show reona doggy -smash
                    pause 0.2
                    show reona doggy smash
                    pause 0.1
                    show reona doggy bounce with vpunch
                    pause 0.15
                    show reona doggy rest
                    pause 0.2
                    show reona doggy -smash
                    "As if that was the cue my body had been waiting for, the same thing happens to me."
                    show reona doggy smash
                    pause 0.1
                    show reona doggy bounce
                    pause 0.15
                    show reona doggy rest
                    pause 0.15
                    show reona doggy -smash
                    pause 0.15
                    show reona doggy smash mouth_ahegao cum
                    pause 0.1
                    show reona doggy bounce with vpunch
                    pause 0.15
                    show reona doggy rest
                    $ reona.purity -= 2
                    $ reona.sub += 2
                    pause 0.35
                    show reona doggy -smash
                    pause 0.7
                    show reona doggy smash eyes_closed
                    pause 0.1
                    show reona doggy bounce with vpunch
                    pause 0.15
                    show reona doggy rest
                    "I shoot my load into Reona when I'm as deep as possible."
                    with vpunch
                    "And when I do so, the sounds that she makes are totally feral in nature!"
                    show reona doggy -smash mouth_pleasure
                    "Before I know what's happening, I can feel her standing up."
                    "The motion pulls my cock out of her a moment later."
                    "So I take that as my cue to make myself as decent as possible."
                    scene bg publicbathroom
                    show reona date flirt rightok leftpeace
                    with fade
                    "Reona doesn't say a word as she pull her panties back up."
                    "Instead she takes my hand again, then leads me out of the bathroom."
                    scene bg nightclub
                    with fade
                    "The rest of the night passes in a blur for me."
                    "And I don't think that I actually come down until hours later."
                    "But the memory of what we did together doesn't fade at all."
                    $ game.room = "nightclub"
                "Stop her":
                    "That's when I begin to seriously put on the breaks."
                    "Reona's putting all of her strength into it."
                    show reona surprised at center, zoomAt(1.5, (640, 1040)) with hpunch
                    "But once I really start resisting, she has to admit defeat."
                    "So instead she turns to confront me, a confused look on her face."
                    show reona embarrassed leftnormal
                    reona.say "What's the problem, [hero.name]?"
                    reona.say "Aren't you having a good time?"
                    mike.say "Of course I am, Reona!"
                    show reona angry rightnormal leftback
                    reona.say "Then why are you holding back?"
                    reona.say "I just want to make it even better!"
                    mike.say "It's not that I don't want to."
                    mike.say "It's just that this doesn't feel like the right place."
                    show reona embarrassed
                    "Reona stares at me for a moment."
                    "Almost like she doesn't understand what I mean."
                    show reona annoyed
                    $ reona.purity += 1
                    $ reona.sub -= 2
                    "Then she shakes her head."
                    reona.say "Okay, okay..."
                    reona.say "I'm not going to force you."
                    show reona happy leftpeace
                    reona.say "Let's get back to dancing instead."
                    "With that we head back onto the dance-floor."
                    "But I note that Reona's not taking me by the hand this time."
                    "And though we dance together, her mood seems to have cooled off too."
                    "All of which leaves me hoping that I just made the right decision."
    return

label reona_event_04:
    scene bg pub
    "The past few days have been pretty much all go for me."
    "College and work seem to have both gone crazy at the same time."
    "And so the first chance I get, I head down to the pub for a break."
    "I'm not meeting anyone else down there or hoping to bump into anyone either."
    "All I want is a genuinely quiet couple of drinks in the Winchester."
    "And I'm pleasantly surprised to find that's exactly what I get."
    "Sure, I say hi to the bartender and a couple of other familiar faces."
    "But everyone seems to get the message when I find a quiet corner."
    "And then they just leave me alone to enjoy my drink and my own company."
    "Finally I can feel myself starting to relax."
    "My muscles are beginning to unwind too."
    "In fact, I feel like I'm letting everything go."
    "No...wait..."
    "That's my bladder I can feel wanting to let go!"
    "Leaping up from my seat, I hurry over to the bathroom."
    "And I only just make it to the urinals before it's too late."
    scene bg publicbathroom with fade
    "As I empty my bladder, I can't help letting out a sigh of relief."
    mike.say "Aah..."
    "???" "♥ Aaah... ♥"
    mike.say "Mmm..."
    "???" "♥ Mmmm... ♥"
    "Wait a minute..."
    "Since when was there an echo in here?"
    "I'm finishing up and putting things back into my pants by now."
    "So I can pay more attention to the sounds I'm hearing."
    "It doesn't take long for me to realise they're coming from one of the cubicles."
    "And then I see the walls shaking, like someone's pounding away at them."
    "My eyes move downwards until I see two pairs of feet under the door."
    "So it's a very specific kind of pounding going on in there!"
    "Well, one thing I do know is that it's none of my business."
    "I'm not about to hang around in here when someone's getting lucky in a cubicle."
    "And I'm not going to tell anyone about it, because I'm not a killjoy either!"
    "Instead I hurry out of the bathroom, trying not to make too much noise."
    scene bg pub with fade
    "But all that being said, I turn around once I'm back in my seat."
    "And I make sure to keep an eye on the bathroom door too."
    "Hey, I may not be a killjoy, but I am a human being!"
    "Of course I want to see who was fucking in there just now."
    "A few minutes later, I get what I wished for."
    show ryan casual at blacker, left4 with easeinleft
    "The door opens and a guy walks out of the bathroom."
    "And I have to say that he's a bit of a disappointment."
    "Because he's nothing special, just a guy you'd walk past in the street."
    hide ryan with easeoutright
    "So forget about him, because the girl he was with might be much hotter."
    "Hell, he could have been with a guy that was much hotter than him."
    "Who am I to judge?"
    "But when I finally see the girl, my jaw almost hits the floor."
    show reona casual flirt leftback at left with easeinleft
    "For a moment I think I must be mistaken."
    "That it must just be someone that looks like her from a distance."
    "But it's not, and I'm clutching at straws - because that's Reona!"
    show reona surprised leftnormal
    "And as if on cue, just to make it obvious what I'm seeing, she puts a hand to her mouth."
    "Because she just realised that she still has a line of cum on her lips!"
    menu:
        "Confront her":
            show reona normal
            "My head's telling me to stay right where I am."
            "That it's a bad idea to walk straight over there."
            "An even worse one to just confront Reona in the middle of the pub."
            "But all the same, I feel myself rising from my seat."
            "And before I know it, I'm striding towards Reona."
            show reona leftback at center with ease
            "I catch her as she's just about to walk out of the door."
            "So I make a point of putting myself between her and the exit."
            show reona surprised rightopen at center, zoomAt(1.5, (640, 1040)), vshake
            "She jumps at the sight of me, clearly surprised by my sudden appearance."
            reona.say "Wha..."
            show reona happy
            reona.say "Oh..."
            show reona rightnormal
            reona.say "[hero.name], I didn't know you were in here too!"
            mike.say "I could say the same thing about you, Reona."
            mike.say "That was until I walked into the bathroom just now!"
            show reona normal
            show fx question
            "Reona looks confused for a moment."
            hide fx
            show reona embarrassed
            show fx exclamation
            "But then reality dawns on her, and I expect her to look guilty."
            "Or at the very least to look pissed that I caught her with another guy."
            "Instead she gives me a knowing smile and shakes her head."
            hide fx
            show reona normal
            reona.say "Oh no!"
            reona.say "We weren't that noisy, were we?"
            "Now it's my turn to shake my head."
            mike.say "What difference does that make, Reona?!?"
            mike.say "Quiet as a mouse or loud enough to raise the fucking dead."
            mike.say "I still just caught you having sex with another guy!"
            mike.say "What are you doing sleeping around behind my back?"
            show reona annoyed
            $ reona.love -= 10
            "Reona looks at me like I'm speaking a foreign language."
            show reona happy at center, zoomAt(1.5, (640, 1040)), vshake
            "Then she lets out a burst of laughter."
            show reona devious
            reona.say "Are you for real?"
            reona.say "You don't own me, [hero.name]."
            show reona normal
            $ reona.sub -= 5
            reona.say "And you can't tell me what to do."
            "I'm about to fire back at Reona, to lay it on the line."
            show reona annoyed rightopen
            "But she holds up a hand to my face and then slips past me out of the door."
            hide reona with easeoutright
            "The gesture catches to totally unprepared, all but frozen with shock."
            "And by the time I snap out of it, Reona is long gone."
            $ reona.flags.confronted_cheat = True
        "Avoid her":
            show reona normal
            "I actually start to get up from my seat, to take a step towards Reona."
            "But then something makes me stop, makes me sit back down and look away."
            "I don't know if it's the embarrassment at knowing she's going behind my back."
            "Or maybe it has more to do with the fear of making a scene in my local."
            hide reona with dissolve
            "Whatever the reason, I make sure not to look up or in her direction."
            "In fact I keep my head down until I hear the sound of the someone walking out the door."
            "And when I take a gamble, looking up again, Reona and the guy are nowhere to be seen."
            "Safe in the knowledge they're gone, I find myself leaning back in my seat."
            "A sigh of what feels like relief escapes me, as though I just dodged a bullet."
            "But I still have no idea what to make of it all."
            "Or how I should react the next time I see Reona."
    return

label reona_event_04b:
    if reona.love.max < 100:
        $ reona.love.max = 100
    hide reona
    show reona shy rightopen at center, zoomAt(1.5, (640, 1040))
    reona.say "[hero.name]..."
    reona.say "There's something I have to ask you..."
    "As soon as I hear those words, it feels like my guts are dropping out of my ass."
    "Seriously, my stomach starts churning and I feel like I'm going to pass out, vomit or both!"
    "Because no guy in his right mind wants to hear a girl tell him something like that."
    "But all the same, I do the best I can to pretend that I'm not worried."
    mike.say "Oh?"
    mike.say "What would that be, Reona?"
    show reona leftback
    reona.say "Don't freak out, okay..."
    reona.say "But I wanna know if you're fucking any other girls right now?"
    "Oh no, it's every bit as bad as I thought it was going to be!"
    "I can't help glancing around, like I don't want anyone else to hear us."
    "And I swear that I can already feel myself starting to sweat too."
    mike.say "Wha..."
    mike.say "What's that, Reona?"
    mike.say "Me...sleeping with other girls?"
    "Reona shakes her head at my reaction."
    show reona happy rightnormal
    reona.say "Hey, I told you not to freak out!"
    reona.say "It's a perfectly simple question."
    show reona normal leftnormal
    reona.say "Are you fucking anyone else besides me?"
    "I always knew that Reona was a pretty forward kind of girl."
    "But I never thought she was this bold."
    reona.say "And if not..."
    show reona devious
    reona.say "Then why not?!?"
    "I'm already opening my mouth to say something the way of an answer."
    "Because I figure that I have to offer one, no matter how bad it sounds."
    "But I find myself stopping in my tracks as her words actually sink in."
    mike.say "Wait a minute, Reona..."
    mike.say "Did you..."
    mike.say "Did you just say 'why not'?"
    show reona happy
    reona.say "Of course I did!"
    reona.say "Why?"
    show reona normal
    reona.say "Did you think I was some kind of prude?"
    "I'm still struggling to get my head around what Reona just said."
    "And the implications of it are still eluding me even now."
    mike.say "But I..."
    mike.say "Normally girls are mad when I..."
    mike.say "When I even look at another girl!"
    "Reona makes a scoffing sound and waves away my concerns."
    show reona happy righthold leftback
    reona.say "Pfft..."
    reona.say "What the fuck do they know?"
    reona.say "Nobody died and made them queen of the world!"
    mike.say "So you'd be okay with me doing something like that?"
    mike.say "I mean, in theory...if the chance came up..."
    mike.say "To like...be with another girl?"
    show reona devious rightnormal
    reona.say "Hell yeah!"
    reona.say "I love the idea of you bedding all the ladies, [hero.name]."
    reona.say "Like, if my man's such an unstoppable stud, a lady-killer..."
    show reona flirt leftnormal
    reona.say "Oooh...that's so hot!"
    "I'm starting to like what Reona's suggesting here."
    "Really warming to the notion of being able to play the field."
    "But there's still a part of me that think's it's too good to be true."
    show reona surprised
    mike.say "So..."
    mike.say "Say I slept with my housemate [bree.name]?"
    reona.say "The blonde?"
    show reona flirt
    reona.say "Mmm...I'd want to know everything you did to her!"
    mike.say "Or how about Sasha?"
    show reona normal
    reona.say "The rock-chick?"
    show reona flirt
    reona.say "Now with her, I'd want you to film it for me!"
    "I'm getting the impression that there's no trap being set for me here."
    "That Reona really is giving me her blessing to sleep around as much as I like."
    show reona devious rightok leftback
    reona.say "I just want you to have fun, [hero.name]."
    reona.say "Life's too short to be wasted, yeah?"
    mike.say "Oh...yeah, Reona..."
    mike.say "I totally get where you're coming from."
    show reona happy
    "Reona nods and smiles, pleased to have finally got her message through."
    "But at the same time my mind is already starting to turn all of this over and over."
    "Sure, it's great to know that I can do what I want with who I want."
    "The only problem is that I'm not exactly an international playboy."
    "I have to have other offers on the table before I can take advantage of that freedom."
    "So I guess that means I'll need to be on the lookout for any chances that present themselves."
    return

label reona_event_05:
    if reona.love.max < 120:
        $ reona.love.max = 120
    show reona
    "I've been wrestling with the revelation of just how liberated Reona is when it comes to sex."
    "Trying as best I can to just be cool with it and not allow the issue to become a big deal."
    "But no matter how hard I try, I don't seem to be able to just accept it and move on."
    "And my efforts to do so haven't escaped Reona's notice either, as I keep trying to avoid the subject."
    "So in the end, I guess she feels like she just has to have it out with me."
    "Which is a relief, as I'd just have had to raise it with her myself otherwise."
    show reona annoyed
    reona.say "[hero.name]..."
    reona.say "You're not cool with me sleeping with other people..."
    reona.say "Are you?"
    show reona normal
    "I feel a great sense of relief almost as soon as Reona says the words."
    "So much so that I can't help letting out a sigh before answering her."
    mike.say "Urgh..."
    mike.say "It's that obvious, huh?"
    show reona leftback rightopen
    reona.say "Yeah..."
    reona.say "It kind of is!"
    show reona normal
    mike.say "I thought that it'd help me being able to do it too."
    mike.say "But somehow it doesn't!"
    show reona pensive leftnormal rightnormal
    "Reona goes quiet for a moment, and in that time she almost looks thoughtful."
    "Which for her is a rare thing."
    "And that makes me doubly aware of just how seriously she's taking this thing."
    show reona interested
    reona.say "Hmm..."
    show reona pensive
    reona.say "I guess I did kind of spring it on you, [hero.name]."
    show reona annoyed
    reona.say "Most guys are super stoked when I tell them that."
    show reona leftback
    reona.say "And I thought you'd feel the same way too."
    show reona normal
    mike.say "I think that's part of the problem, Reona."
    mike.say "It's not that you want to have that freedom for yourself."
    mike.say "Or that you're willing to let me have the same."
    show reona embarrassed
    mike.say "I think the issue is that we didn't make that decision together."
    show reona shock
    "Reona blinks, as if that's something she never thought of before now."
    show reona devious
    "But then she nods her head."
    show reona embarrassed rightok
    reona.say "Okay, [hero.name]..."
    reona.say "Let's do that."
    reona.say "Let's decide what we want from each other."
    show reona normal
    mike.say "You..."
    mike.say "You mean right here and now?"
    show reona happy leftnormal rightnormal
    reona.say "Uh-huh..."
    reona.say "Let's do it!"
    "I nod my head too."
    "Finally feeling ready to sort this thing out once and for all."
    menu:
        "I'll keep sleeping around, but you can't do the same!":
            mike.say "The thing is, Reona..."
            mike.say "I like the idea of my being able to sleep around."
            mike.say "But the idea of you doing the same..."
            show reona shock
            show fx exclamation
            $ reona.love -= 2
            mike.say "That's something I don't like at all."
            "Reona blinks and shakes her head."
            reona.say "What?!?"
            hide fx
            show reona angry leftback rightopen
            reona.say "Don't you think that's kind of unfair?"
            reona.say "Why can't we both do it?"
            mike.say "Look, if you're fine with me sleeping around, that's one thing."
            mike.say "But I'm just not willing to share you with anyone."
            show reona surprised
            $ reona.love += 2
            mike.say "It's selfish, but I want you all to myself!"
            "Reona looks genuinely surprised at my explanation."
            show reona shy blush leftnormal rightnormal
            reona.say "You really mean that?"
            reona.say "You like me that much?"
            mike.say "Well, yeah, Reona..."
            show reona embarrassed
            $ reona.love += 2
            mike.say "In fact, I think I'm falling for you!"
            "That last admission is the thing that does it."
            "Reona puts a hand on her chest."
            "Almost like her heart's beating faster."
            show reona normal
            reona.say "Oh..."
            reona.say "Okay, [hero.name]."
            reona.say "It's a little different to what I'm used to."
            reona.say "But we can give that a try."
            $ reona.flags.cheating_agreement = "mc"
        "You can do what you want, but I have only eyes for you" if reona.sexperience > 0 and sum([npc.sexperience for npc in Person.all_people(ignore_hidden=False)]) == reona.sexperience:
            mike.say "The thing is, Reona..."
            mike.say "I'm fine with the idea of you being able to sleep around."
            mike.say "But the idea of me doing the same..."
            show reona surprised
            mike.say "Nah, that's not what I want at all."
            "Reona blinks and shakes her head."
            reona.say "Are you serious?!?"
            show reona embarrassed
            reona.say "Don't you think that's kind of unfair?"
            reona.say "Why can't we both do it?"
            mike.say "Look, it's not what I'm used to, but I think I can handle you doing it."
            mike.say "But I'm just not interested in any other girls, Reona."
            $ reona.love += 2
            mike.say "It's selfish, but I want you to be the only one."
            "Reona looks genuinely surprised at my explanation."
            show reona leftback righthold
            reona.say "You really mean that?"
            reona.say "You like me that much?"
            mike.say "Well, yeah, Reona..."
            show reona blush
            $ reona.love += 2
            mike.say "In fact, I think I'm falling for you!"
            "That last admission is the thing that does it."
            "Reona puts a hand on her chest."
            "Almost like her heart's beating faster."
            show reona normal leftnormal rightnormal
            reona.say "Oh..."
            reona.say "Okay, [hero.name]."
            reona.say "It's a little different to what I'm used to."
            reona.say "But we can give that a try."
            $ reona.flags.cheating_agreement = "reona"
        "As long as we can both have fun everything is fine":
            mike.say "This isn't what I'm used to."
            mike.say "But I think I can handle it."
            mike.say "So long as we're both on the same page, Reona."
            mike.say "We can't get jealous of each other sleeping with someone else."
            mike.say "It'll be hard for sure, but worth it."
            show reona happy
            "Reona looks genuinely pleased with my explanation."
            reona.say "You really mean that?"
            reona.say "You're going to give it a go?"
            mike.say "Well, yeah, Reona..."
            mike.say "I have a feeling that we're strong enough."
            mike.say "Because what we have is more than just a physical connection."
            show reona embarrassed blush
            $ reona.love += 2
            mike.say "In fact, I kind of think I'm falling for you!"
            "That last admission is the thing that does it."
            "Reona puts a hand on her chest."
            "Almost like her heart's beating faster."
            show reona normal
            reona.say "Oh..."
            reona.say "Okay, [hero.name]."
            reona.say "It's a little different to what I'm used to."
            reona.say "But we can give that a try."
            $ reona.flags.cheating_agreement = "both"
        "I want an exclusive relationship. You, me and no others.":
            mike.say "I know that this is kind of the way you role, Reona."
            mike.say "But I'd like you to try things my way, okay?"
            show reona sad
            reona.say "You mean..."
            mike.say "I mean that for as long as we're together..."
            mike.say "We only sleep with each other."
            mike.say "No fucking other people, yeah?"
            "Reona doesn't look convinced."
            show reona angry leftback rightopen
            reona.say "But why would I want to do that, [hero.name]?"
            reona.say "My way's a whole lot more fun."
            reona.say "And it's always worked out just fine for me."
            mike.say "Reona, I'm just not willing to share you with anyone."
            show reona surprised righthold
            mike.say "It's selfish, but I want you all to myself!"
            "Reona looks genuinely surprised at my explanation."
            show reona shy blush
            reona.say "You really mean that?"
            reona.say "You like me that much?"
            mike.say "Well, yeah, Reona..."
            show reona embarrassed
            $ reona.love += 2
            mike.say "In fact, I think I'm falling for you!"
            "That last admission is the thing that does it."
            "Reona puts a hand on her chest."
            "Almost like her heart's beating faster."
            show reona normal leftnormal rightnormal
            reona.say "Oh..."
            reona.say "Okay, [hero.name]."
            reona.say "It's a little different to what I'm used to."
            reona.say "But we can give that a try."
            $ reona.flags.cheating_agreement = "neither"
    return

label reona_event_06:
    if reona.love.max < 140:
        $ reona.love.max = 140
    scene bg restaurant
    "The problem with dating Reona is that I always find myself torn between two extremes with her."
    "Take tonight for example, when we've agreed to meet up for a date."
    "We're booked into a pretty nice restaurant for a meal."
    "Then the plan is to go see a movie at the local cinema."
    "Nothing out of the normal there, right?"
    "But the first issue comes while I'm waiting for Reona to turn up at the restaurant."
    "And no, she's not late or calling me to say that she's got to cancel at the last minute."
    "Because I look up to see her walking towards me at the exact time we arranged to meet."
    show reona sexydate at center, zoomAt(1.0, (940, 720)) with easeinright
    "The problem, if you want to call it that, is what Reona's chosen to wear."
    "More specifically the fact that she seems to have forgotten more than half of it!"
    "And this is what I mean about the extremes when it comes to dating Reona."
    show reona rightopen at center, traveling(1.5, 2.0, (640, 1040))
    "On the one hand she's getting stares from everyone that can see her."
    "Which is making me feel kind of awkward."
    "But on the other hand, she looks totally amazing in the outfit."
    "Which is making me feel seriously horny!"
    show reona flirt rightpeace
    reona.say "Hey, [hero.name]..."
    reona.say "You getting enough of an eyeful?"
    show reona happy rightnormal at startle
    "Reona giggles as she does a little twirl for my benefit."
    "Though all eyes seem to be on her as she does so too."
    mike.say "H...hi, Reona..."
    mike.say "You could say that."
    show reona devious
    reona.say "Don't worry, this isn't going to get weird."
    reona.say "We're just going to have a regular date, like two regular people."
    show reona interested
    reona.say "But tell me, what do you think?"
    reona.say "You like what I'm wearing, right?"
    menu:
        "It's...too much...":
            "I just can't lie to Reona and tell her I approve of what she's wearing."
            "There are too many people staring at us for a start."
            "Plus she really seems to want us to start behaving like a normal couple."
            "So dressing in such a provocative manner just isn't appropriate."
            mike.say "To be honest, Reona..."
            mike.say "You're showing a little too much skin."
            show reona shock
            "Reona looks instantly surprised by my reaction."
            "So much so that she even takes a step backwards and away from me."
            "I guess she's just not used to guys saying they disapprove of her wardrobe."
            reona.say "Oh..."
            reona.say "You..."
            reona.say "You really think so?"
            "I nod at this."
            mike.say "I kinda do, Reona."
            mike.say "And it's making people stare at us too."
            mike.say "So maybe tone it down next time?"
            show reona sad
            $ reona.love -= 2
            "Reona doesn't say anything more."
            "She just lowers her head a little and nods."
            $ game.active_date.score -= 20
        "Sure I do!":
            "I know that Reona said she wanted this to be like a normal date."
            "And so I should tell her that she's showing too much skin for that."
            "But the truth is that I don't want to start the date by upsetting her."
            "Plus it'd make me a hypocrite, as I'm liking what I see!"
            "So I decide to let it slide this time."
            mike.say "I sure do, Reona..."
            mike.say "You look incredible tonight!"
            show reona happy
            $ reona.love += 2
            "This seems to be exactly what Reona wanted to hear."
            "Because she smiles and grabs hold of my hand."
            reona.say "Aww..."
            reona.say "Thanks, [hero.name]."
            reona.say "Well tonight I'm all yours."
            reona.say "So you can look at me all you like!"
            hide reona
            show reona kiss sexydate
            with fade
            $ reona.flags.kiss += 1
            "Reona leans in and plants a long, lingering kiss on my lips."
            "All the while she's doing so, I know all eyes must be on us."
            "But the truth is that I don't really care."
            "Because the thrill that she's making me feel is incredible."
            "Not to mention how hard she's getting me down below too!"
            $ game.active_date.score += 20
            hide reona
    show reona sexydate at center, zoomAt(1.5, (640, 1040))
    with fade
    "After a few minutes to wait standing , we're shown to the table we reserved."
    scene bg black
    show restaurant meal reona sexydate nomeals
    with fade
    "And it's a relief that once we've sat down, Reona's not on show anymore."
    "That means we can get on with the business of actually having a nice meal."
    show restaurant_meal_waiter_pose01 as man zorder 1 at center, zoomAt(1.0, (200, 720)) with easeinleft
    "The waiter hands us both a menu and waits patiently as we peruse them."
    mike.say "What do you like the look of, Reona?"
    show restaurant meal reona sexydate bored nomeals
    reona.say "Hmm..."
    reona.say "This is all really fancy, you know?"
    mike.say "I guess it is a little."
    show restaurant meal reona sexydate -bored nomeals
    reona.say "You know what..."
    show restaurant meal reona sexydate happy nomeals
    reona.say "I'll have a cheeseburger."
    reona.say "Because you have to try real hard to fuck one of those up!"
    "I can't help glancing up as Reona drops an F-bomb."
    show restaurant_meal_waiter_pose01 as man zorder 1 at stepback(0.1, -10, 0)
    "And I see the waiter wince, like the sound of it caused him physical pain too."
    show restaurant meal reona sexydate -happy nomeals
    menu:
        "Order a fancy steak":
            "I feel like I have to do something to balance out Reona's faux pas."
            "And so I point at one of the most fancy and expensive steaks on the menu."
            mike.say "I think I'll have the T-bone, please."
            mike.say "And make sure that it's on the rare side of medium."
            "The waiter nods at this."
            "Waiter" "Very good sir."
            "Waiter" "One steak and one..."
            "He pauses to stare at Reona."
            "Waiter" "Cheeseburger!"
            "The waiter walks away, shaking his head."
        "Order a cheeseburger too":
            "Where does this guy get off acting like such a snob?"
            "The restaurant was happy to give us a table tonight."
            "And I'm sure they're going to be just as happy to take our money."
            "So what does it matter that Reona wants a cheeseburger?!?"
            mike.say "You know what, Reona..."
            mike.say "That sounds like a great idea."
            "I make a point of clicking my fingers to get the waiter's attention."
            "Because I once heard that's a sure-fire way to get them mad."
            mike.say "Hey, buddy..."
            mike.say "Two fucking cheeseburgers..."
            mike.say "And make it quick!"
            "The waiter looks at me like I just took a piss on his shoes."
            "But he bustles off without a word all the same."
    hide restaurant_meal_waiter_pose01 as man with easeoutleft
    show restaurant meal reona sexydate bored nomeals
    reona.say "Huh!"
    reona.say "I don't think that guy likes us."
    mike.say "Really, Reona?"
    mike.say "I can't imagine why..."
    $ game.active_date.score += 10
    show restaurant meal reona sexydate -nomeals -bored with fade
    "When the food arrives we seem to forget everything else around us."
    "Because it just looks and smells so good all we can think about is eating."
    "Up until that moment I had no idea that I was so damn hungry."
    "So I don't hesitate to get stuck into the meal on the plate before me."
    "Reona seems to feel the same way too, and I note she has a very healthy appetite."
    show restaurant meal reona sexydate happy
    "Pretty soon we're chatting away happily, the food putting us both in a good mood."
    "I watch as Reona swallows the last mouthful from her plate and then pushes it away."
    reona.say "Phew..."
    reona.say "I'm stuffed!"
    mike.say "Me too, Reona..."
    mike.say "I don't think I could eat another bite!"
    "As soon as we've settled the bill, Reona and I leave the restaurant."
    scene bg cinema
    show reona sexydate at center, zoomAt(1.5, (640, 1040))
    with fade
    "And we head straight over to the cinema, still talking all the way."
    "Walking into the foyer, we're greeted by the sight of a wall filled with posters."
    "All of them are eye-catching, some of them serious and many of them exciting."
    reona.say "Hey..."
    reona.say "Did we agree on what we were going to see?"
    mike.say "No, Reona..."
    mike.say "I don't think we did."
    "This seems to be the answer that Reona was hoping for."
    show reona happy
    "Because she instantly smiles and points to one of the posters."
    reona.say "Then we gotta see 'Fifty Shades of Beige'!"
    reona.say "It looks SO hot!"
    "I take a look at the poster and instantly see what Reona means."
    "It's one of those films that's kind of kinky in a conventional kind of way."
    "But to me it looks more like boil-in-the-bag perversion."
    mike.say "I kind of wanted to see this one, Reona..."
    mike.say "It's called 'Sand' and it's based on a classic sci-fi novel!"
    "Reona takes one look at the poster in question."
    show reona annoyed
    "And then she screws her face up in an expression of disapproval."
    reona.say "I don't like sand, [hero.name]..."
    reona.say "It's dry, scratchy and it gets in all of your cracks!"
    "Well it looks like we're not going to agree on a film anytime soon."
    "So one of us is going to have to let the other have their way."
    menu:
        "Accept to see Reona's film":
            "I really don't want to sit through an hour or more of crap."
            "But on the other hand I want the date to go as smoothly as possible."
            "So I guess I'm going to have to be the one that gives in this time."
            mike.say "Okay, Reona..."
            mike.say "We'll watch the beige film."
            mike.say "But you owe me one!"
            show reona happy
            $ reona.love += 4
            "Reona looks delighted to be getting her own way."
            "But mercifully she doesn't make a point of rubbing it in."
            reona.say "Thanks, [hero.name]..."
            reona.say "And you never know..."
            reona.say "You might actually end up liking it."
            mike.say "I seriously doubt that."
            $ game.active_date.score += 25
        "Force to see the film you want":
            "And there's non way I'm sitting through an hour or more of crap."
            "So Reona's just going to have to be the one to give in this time."
            mike.say "I'm not watching the beige film, Reona."
            mike.say "It's got really bad reviews and it's hours long!"
            mike.say "We either watch me choice or we call it a night."
            show reona shock
            "Reona looks at me with genuine surprise on her face."
            "Because I guess she was expecting me to give in to her."
            "And for a moment I think she's going to argue."
            "But then she nods and lets out a sigh."
            $ reona.love -= 2
            reona.say "Urgh..."
            reona.say "Okay, okay..."
            reona.say "Have it your way."
            $ game.active_date.score -= 20
    scene bg cinemaroom
    show reona sexydate at center, zoomAt(1.5, (640, 1040))
    with fade
    "Once we have the tickets in our hands, Reona and I find the screen we need."
    "And then we hurry to find our seats, getting into them just as the lights go down."
    "As the film begins, I feel Reona leaning her head on my shoulder."
    "The sensation is very nice, easing me into a state of total relaxation."
    "It only gets better once she leans her body against me too."
    "So much so that I hardly notice her hand creeping over my thigh."
    "By the time I realise what's going on and look down, Reona's already got my flies half-open!"
    show reona flirt
    "She seems to notice that I'm onto her, looking up at me with a smile on her face."
    "Then she lifts a finger to her lips, letting me know that she wants me to keep quiet."
    menu:
        "Let her play with you":
            scene bg black
            show reona double hj jack mikenpc cinema down mouth_lick onmike casual at center, zoomAt(1.25, (800, 840))
            with fade
            "I daren't try to stop Reona for fear of someone hearing the commotion it would make."
            "So instead I just lie back in my seat and leave her to it."
            "What follows is one of the most tense and yet exciting moments of my life."
            show reona double hj jack mikenpc cinema speed_mike with vpunch
            "Reona's technique is rough, fast and often more than a little painful!"
            "But the danger of getting caught is more than enough to make up for that."
            "All the time I'm fighting to keep myself from crying out."
            show reona double hj jack mike_close
            "My heart pounding away in my chest as Reona tugs at my manhood."
            "More than once I think that I'm going to shout something at random."
            "And maybe it's that fear which serves to speed things up."
            "Because it isn't long before I feel myself starting to lose it."
            "Fingers digging into the arms of my seat, I grind my teeth together."
            show reona double hj jack mike_close cum_hand_mike with vpunch
            "And somehow I manage to keep quiet as I shoot my load."
            with vpunch
            "Reona catches it in her hand, keeping it from spurting up and into the air."
            show reona double hj jack mikenpc cinema -speed_mike with vpunch
            "Then she adds to the sense of shame I'm feeling by wiping her hand on the chair beside her!"
            show reona double hj jack mike_open
            "As soon as I regain control of myself, I hurry to push my cock back into my pants."
            "Then I settle down to watch the rest of the film."
            "All the time praying that nobody saw what Reona just did to me."
            $ reona.purity -= 2
            $ game.active_date.score += 25
        "Stop her":
            "I reach down and grab hold of Reona's wrist."
            "And then I pull her hand away from my groin."
            show reona shock
            "She looks up at me in genuine surprise."
            "And I shake my head, making it plain that I want her to stop."
            "Reona shakes her own head in response, pulling her hand away."
            "Then she leans back in her chair, putting a little distance between us."
            "It looks to me like she's sulking, but there's nothing I can do about it."
            "Reona needs to learn about boundaries and what constitutes unacceptable behaviour."
            "This is just another step in the learning process for her."
            $ reona.purity += 2
            $ game.active_date.score -= 10
    scene bg cinema
    show reona happy sexydate at center, zoomAt(1.5, (640, 1040))
    with fade
    "When the film is over, we walk out into the cool night air."
    "Reona seems pleased with herself, happily hanging off my arm."
    reona.say "You see, [hero.name]..."
    reona.say "I can do normal dates!"
    mike.say "Erm..."
    mike.say "Yeah, Reona..."
    mike.say "I guess so!"
    "Reona doesn't seem to pick up on the hesitation in my voice."
    "And I choose not to shatter her illusions as well."
    "I mean, she's getting better at that kind of thing."
    "But maybe there's a little more work to be done in some areas?"
    "Though I'm not going to be the one to tell Reona that."
    $ game.hour = 0
    return

label reona_event_07:
    if reona.love.max < 160:
        $ reona.love.max = 160
    scene bg street
    show reona casual
    "I figured that if I want to get Reona to truly understand normal dating, then we need to do normal as much as possible."
    "Which is why I took the step of inviting her over to my place on a Saturday afternoon."
    "No big plans, no ulterior motives and most of all no hints at having the place to ourselves."
    "I mean sure, my housemates aren't going to be in when Reona gets over here."
    "But the fact I haven't told her as much means she can't come over expecting to be able to get up to any mischief."
    "And you know the kind of thing that I mean!"
    "You might also think that sounds crazy - that I'd pass up the chance to have Reona pounce on me."
    "But this is kind of like that film where the classy guy bets he can teach the low-class girl to be like him."
    "Only in this case it's me trying to prove to Reona that everything doesn't have to lead to sex."
    "And I figure that once I've managed to do that, the actual chance to fool around with her will be that much better."
    "All of this is running through my head when I hear the sound of a knock at the door."
    "But that instantly turns my thoughts into a crazy jumble as I rush to answer it."
    "It's all I can do to keep from flinging the door open once I get there."
    "So much so that the person on the other side takes a step back in genuine surprise."
    scene bg house
    show reona righthold leftback
    with fade
    reona.say "Oh..."
    reona.say "Hey, [hero.name]…"
    reona.say "Is everything okay?"
    "It takes me a few seconds to collect myself and get my thoughts back in order."
    "And not least because I wasn't prepared for just how good Reona looks right now."
    "Seriously, she's making me regret my decision to keep things clean already."
    "It'd be so easy just to go back on all that, to reach out for her and..."
    "No, no...show a little restraint!"
    mike.say "Hey, Reona..."
    mike.say "Everything's fine, just fine..."
    mike.say "I'm just a little flustered from cleaning up around the house."
    show reona happy rightnormal at startle
    "Reona covers her mouth to stifle a giggle as I step aside and let her in."
    reona.say "Ha..."
    reona.say "That's such a funny image, [hero.name]…"
    reona.say "You running around in an apron with a feather duster!"
    "I can feel the sensation of my cheeks flushing as Reona says all of this."
    show bg livingroom with fade
    "And so I do the best I can to shake it off while closing the door behind her."
    "But maybe I'm trying a little too hard."
    "Because my voice sounds comically gruff."
    mike.say "No way, Reona..."
    mike.say "Ahem..."
    mike.say "I mean, no way - I was just doing a little picking up around the place!"
    "Reona gives this a quick nod."
    "As though she's not really interested in my excuses."
    "And instead she walks straight through to the sitting room."
    "I follow on her heels, wondering why she's just letting herself in."
    "But then she sits down on the sofa and pats the spot beside her."
    "That's enough to remind me of all the times she's been over here to study in the past."
    "So is it really any wonder she feels comfortable just walking in?"
    reona.say "Why are you hovering in the doorway, [hero.name]?"
    reona.say "We can talk much more easily if you come sit by me!"
    show reona flirt leftnormal
    "Reona adds a wink as she keeps on patting the cushion at her side."
    "And I get the distinct feeling there's more being promised than mere conversation!"
    mike.say "Sure, Reona..."
    mike.say "Of course..."
    "I hurry over and plant my ass on the exact spot Reona's picked out for me."
    "And as soon as I'm sat down, I can feel my pulse starting to race."
    "Seriously, it's hard to be this close to Reona and stay in control."
    "From here I can see every curve of her body."
    "I can see her breast rising as she takes a breath."
    "And I can smell the scent of her on the air too."
    "I don't think I've ever caught the scent of a woman that was so sexy before."
    "Seriously, if human pheromones are really a thing, then Reona has them in spades!"
    reona.say "So..."
    show reona rightpeace:
        yalign 1
        ease 0.5 zoom 1.5
    reona.say "Here we are, [hero.name]."
    show reona:
        yalign 1
        ease 0.5 zoom 1.6
    reona.say "Just you and me, with the whole place to ourselves."
    show reona:
        yalign 1
        ease 0.5 zoom 1.7
    mike.say "Y...yeah, Reona..."
    mike.say "It sure seems that way!"
    "Urgh...what kind of a dumb line was that?!?"
    "Reona seems to be able to reduce me to the level of a total moron."
    "So much so that all I can do is nod and state the blindingly obvious."
    "But luckily for me it seems that she's not in a judgemental mood right now."
    reona.say "It does, doesn't it!"
    show reona:
        yalign 1
        ease 0.5 zoom 1.8
    reona.say "Just think of all the things we could get up to."
    "Of course Reona doesn't choose to leave imagining those things to my imagination."
    show reona:
        yalign 1
        ease 0.5 zoom 1.9
    "As she's saying this, she leans in as close as possible, pressing herself against me."
    "And I can feel her hands roaming all over my body too."
    "Paying particular attention to the sensitive part below the waist!"
    mike.say "Trust me, Reona..."
    mike.say "There's nothing else on my mind right now!"
    show reona happy
    "Reona lets out a chuckle that I sense is a signal she's ready to go."
    "I feel the muscles of her body tense as she prepares herself."
    "And my own body does the same with no need for a conscious thought."
    play sound door_knock
    "All of which is a shame, because that's the exact moment there's a knock at the door."
    show reona surprised:
        yalign 1
        ease 0.5 zoom 1
    "As one, Reona and I are snapped back to reality."
    "We sit up, heads turning towards the front door."
    "But it's me that makes to get up first."
    show reona shock rightopen leftnormal
    reona.say "You're not going to answer that, are you?!?"
    "I look back at Reona, surprised by her question."
    mike.say "I have to see who it is, Reona."
    mike.say "There might be someone important at the door."
    show reona angry leftback righthold
    reona.say "More important than me?"
    reona.say "More important than what we were about to do?!?"
    "I wave a hand in Reona's general direction, trying to play it down."
    mike.say "I'll only be a couple of seconds, okay?"
    mike.say "I'm just going to see who it is and get rid of them."
    "Reona sits back on the sofa, her arms crossed over her chest."
    "All of which sends me mixed messages, because it's obvious she's pissed."
    "But she also looks really hot when she pouts!"
    show reona annoyed
    reona.say "Okay, [hero.name]."
    reona.say "But you really had better get rid of them."
    reona.say "Because being interrupted like this really ruins my mood!"
    scene bg house with fade
    "With that in mind, I practically race to the front door."
    "I don't bother looking through the peephole to see who's there."
    "Instead I fling it open and prepare to tell them to get lost."
    mike.say "What the hell do you..."
    show angela with dissolve
    angela.say "Well goodness me..."
    angela.say "Is that how you choose to greet your mother these days?"
    "I stop dead in my tracks, jaw hanging open."
    "The last person I expected to find on the doorstep was my mom!"
    mike.say "I..."
    mike.say "I'm sorry, mom..."
    mike.say "I thought you were someone else!"
    "My mom raises an eyebrow at this."
    angela.say "Is that so?"
    mike.say "Erm...yeah..."
    mike.say "We've been getting a lot of nuisance callers recently."
    mike.say "Door-to-door salesmen and that kind of thing!"
    "My mom doesn't look too convinced by that hasty explanation."
    "But she seems to be willing to let it go, much to my relief."
    angela.say "Well?"
    mike.say "Well what?"
    angela.say "Are you going to let me in or not?"
    angela.say "I'm not used to being kept waiting on the doorstep like this!"
    "I glance over my shoulder and back again."
    "My mind racing as I try to think up a way to get rid of my mom."
    "Worse still, it has to be quick and yet something that won't piss her off."
    mike.say "It's not a good time right now, mom."
    mike.say "I kind of have company, you know?"
    "As soon as the words are out of my mouth, I know I screwed up."
    "Because if there's one thing my mom likes, it's interfering in my life."
    "Especially in my personal life!"
    "Instantly she starts straining to see past me."
    "Like she's hoping to catch a glimpse of whoever's inside the house."
    angela.say "All the more reason for me to come inside then."
    angela.say "Because you'll obviously want to introduce them to me, won't you?"
    mike.say "I..."
    mike.say "I don't think that's a good idea, mom!"
    "I'm right in the middle of trying to keep mom out of the house."
    "But at the same time doing the best I can to make out like I'm not."
    "And that's just when I hear the sound of someone walking up behind me."
    show angela at left with ease
    show reona rightopen leftback at right with easeinright
    reona.say "Oh..."
    reona.say "Hi there!"
    reona.say "You must be [hero.name]'s mom, right?"
    show angela happy
    angela.say "And you must be his 'company'!"
    show reona happy
    "I turn with a look of horror etched deep into my face."
    "And sure enough, there's Reona, standing in the hallway."
    "The shock means that I forget what I was supposed to be doing."
    scene bg livingroom with fade
    "Which gives my mom the chance she needs to push past me and get into the house."
    "All I can do is stand there and watch as mom and Reona look each other up and down."
    "And I'm not kidding, they're actually circling as they do so, like caged beasts!"
    "But the reality is that they have to at least try and behave like civilised human beings."
    "So there are smiles fixed on their faces the whole time."
    "Though they do seem to be showing off a little too much of their teeth."
    "And that makes the sight quite unnerving."
    "Stepping between them, I do all that I can to calm things down."
    mike.say "Okay, mom..."
    mike.say "This is Reona."
    mike.say "Reona, this is my mom..."
    mike.say "She just dropped in for a surprise visit!"
    show reona devious at right with easeinright
    reona.say "Why'd she do that, [hero.name]?"
    reona.say "Aren't you all grown-up by now?"
    reona.say "Because you sure look like a big boy to me!"
    show angela at left with easeinleft
    angela.say "Ha!"
    angela.say "When you have a son, you never stop looking out for him."
    angela.say "Because he's a man, and men are blind to some threats in life."
    reona.say "Oh yeah?"
    reona.say "And what kind of threat is that?"
    reona.say "I think the worst thing for a guy would be someone making him into a mummy's boy!"
    show angela grudge
    "Before now it seemed to me that mom and Reona were just jabbing at each other."
    "Testing the opposition's armour for weak spots with punches pulled before impact."
    "But I can see from the look on my mom's face, that one hit home."
    "And it looks like it hurt too!"
    angela.say "Better a mummy's boy than deadbeat."
    angela.say "The kind that would be seen in the company of a slut!"
    show reona angry righthold leftback
    "Ouch!"
    "Now the gloves are really coming off."
    "I can see the anger flare in Reona's eyes as my mom insults her."
    "And I just know that she's going to give back as good as she's getting."
    "Which is why I have to step in and stop this thing escalating."
    mike.say "OKAY..."
    mike.say "Okay..."
    mike.say "Time out, you two!"
    "I put myself between mom and Reona, asserting myself as best I can."
    mike.say "Reona..."
    mike.say "You go back into the sitting room and wait for me there."
    reona.say "But..."
    mike.say "No buts!"
    mike.say "Just do it!"
    show reona surprised
    "I see surprise replace the anger in Reona's eyes."
    "And that seems to be enough to make her do as she's told."
    hide reona with easeoutright
    show angela at center with ease
    "But once she's gone, I turn to see a victorious smile on my mom's face."
    show angela happy
    angela.say "Ha!"
    angela.say "Well done - you really told her!"
    mike.say "Knock it off, mom!"
    mike.say "In the kitchen, now!"
    scene bg kitchen
    show angela surprised
    with fade
    "I figure that's far enough away from the sitting room for us not to be overheard."
    "And luckily for me, my assertive tone has the exact same effect on my mom as it did Reona."
    "She hurriedly scuttles in there, with me close on her heels."
    "And then my mom puts the kitchen island between us, as if she's still intimidated."
    mike.say "Urgh..."
    mike.say "Look, mom..."
    mike.say "I don't know what you have against Reona."
    mike.say "But you can't just come barging in here and starting fights!"
    "Now that we're on my own, I'm already starting to feel sorry for my mom."
    "I know that she's in the wrong here, but it's hard to stay mad at one of my parents."
    "And the change of setting seems to be having an effect on her too."
    show angela normal
    "Rekindling her confidence and making her reassert herself once more."
    angela.say "Oh, [hero.name]..."
    angela.say "Can you really blame me?"
    angela.say "I've seen a hundred, no a thousand girls like that one."
    angela.say "And every one of them was bad news!"
    angela.say "I can tell that you like this Reona."
    angela.say "And I know that she's very pretty."
    angela.say "But she'll end up hurting you before it's all over!"
    "I take a deep breath and shake my head."
    mike.say "Mom..."
    mike.say "You can't control my life like you did when I was a kid."
    mike.say "And you don't know Reona nearly as well as I do."
    mike.say "You're just judging her on appearance, not character."
    mike.say "She's not the way you think she is, I swear!"
    "I feel like I'm making a pretty impassioned speech on Reona's behalf here."
    "But then I feel something nudging me in the thigh."
    "So naturally, I look down to see what it is."
    show angela at right with ease
    show reona flirt leftpeace rightok at left with easeinleft
    "And I find Reona's face, smiling up at me from below!"
    "She's down on all fours, holding a finger to her lips."
    "What the fuck?!?"
    "She must have crawled in here on all fours while I was talking with mom!"
    angela.say "Oh, [hero.name]..."
    angela.say "I suppose that you're right."
    "I look up to see that my mom's not noticed a thing."
    "She must have been looking away just now when I was glancing down at Reona."
    "It's then that I feel Reona reaching up and opening my flies!"
    hide reona
    hide angela
    show reona bj mike kitchen
    with fade
    "Fuck sake - she's proving me wrong even as I'm pleading her case!"
    "And the worst thing is that there's nothing I can do to stop her."
    "That is unless I want to give my mom all the proof she'll ever need."
    show reona bj handjob
    "Reona's not wasting any time either, unzipping me as quickly as she can."
    "Then she reaches straight in there, pulling my cock out just as fast."
    "The combination of embarrassment and excitement is hard to describe."
    "But it's very real, making my cock begin to stiffen as soon as it's in her hands."
    mike.say "Mmm..."
    mike.say "Ungh..."
    "I can't help making grunting sounds as Reona puts it in her mouth."
    "But the sound catches mom's attention, making her turn her head towards me again."
    show bg kitchen zorder 2
    show angela zorder 3
    with fade
    angela.say "Honey?"
    angela.say "Are you okay?"
    "I nod my head hastily, trying to dismiss her concern."
    mike.say "I'm fine, honestly..."
    mike.say "I just...pulled a muscle at the gym, that's all."
    angela.say "Oh dear!"
    angela.say "Do you want me to take a look at it?"
    angela.say "The last thing I want for you is to go all stiff!"
    hide bg
    hide angela
    show reona bj suck
    with fade
    "I hear Reona snigger, her lips still around my cock."
    "And the worst thing is that it somehow makes the feeling even more intense!"
    mike.say "No..."
    mike.say "I'll be fine."
    "By now Reona's well into it, her head bobbing up and down."
    "And despite my misgivings, I have to admit that it feels really good."
    "Even so, I do the best I can to downplay the sensations."
    show bg kitchen zorder 2
    show angela zorder 3
    with fade
    angela.say "Are you sure?"
    angela.say "I could give you my Chiropractor's number?"
    angela.say "You remember him, right?"
    angela.say "The one with the foreign name that's a real mouthful?"
    hide bg
    hide angela
    with fade
    "This time Reona almost gags on my cock as she tries to keep from laughing."
    "I don't know how this is even happening."
    "It's like I'm being cursed by the god of puns and double entendres!"
    show reona bj finger eyes_close
    "But the difference is that this time the joke's not just on me."
    "By now my cock is as deep in Reona's mouth as I expected she could get it."
    "Yet when she laughs, it somehow opens her throat up even more."
    "The head must be actually have ended up in her throat."
    "Because all of a sudden she's gagging and gasping."
    "The problem is that I can't see what's going on."
    "So I just assume that she's putting in a bit of extra effort."
    with vpunch
    "And why not?"
    show reona bj cum with vpunch
    "As it's more than enough to finish me off."
    show reona bj out -cum down eyes_ahegao squirt mouth_pleasure with vpunch
    "The moment I shoot my load into Reona's mouth, she drags herself off of me."
    "I have to watch out of the corner of my eye as she pretty much crawls out of the kitchen."
    scene bg kitchen with fade
    show angela
    "And somehow I manage to make myself decent without my mom seeing a thing."
    angela.say "Oh well..."
    angela.say "If I can't convince you, then there's no point in me stay."
    scene bg house with fade
    show angela
    "With that, she strides into the hallway and towards the door."
    "Which leaves me to run after her in an effort to get there first."
    mike.say "Don't be like that, mom..."
    mike.say "All I'm asking is that you give Reona a fair chance."
    mike.say "Let her prove herself to you, okay?"
    "My mom turns on the doorstep, shaking her head."
    angela.say "Oh, honey..."
    angela.say "You always were too kind and forgiving!"
    angela.say "But that's what makes you my special boy."
    angela.say "So I'll try my best, for you - not her!"
    "I wave as she walks off down the street."
    "And once she's out of sight, I close the door and lock it for good measure."
    scene bg livingroom
    show reona sad
    with fade
    reona.say "Your mom hates me!"
    "I jump at the sound of Reona's voice."
    "But to my relief, this time she's at least on her feet."
    mike.say "Reona!"
    mike.say "I'm doing all I can to make her change her mind."
    mike.say "But pulling stunts like that doesn't help!"
    show reona happy leftpeace rightpeace
    "Reona smiles and shakes her head at this."
    reona.say "I'll stop doing it when you start telling me to!"
    "Now it's my turn to shake my head."
    "Because I know that she's got me there."
    "And even worse, she knows that I know it too."
    $ game.active_date.score = 100
    return

label reona_event_08:
    if reona.love.max < 180:
        $ reona.love.max = 180
    scene bg park
    show reona leftpeace rightopen
    with fade
    "I'm still determined to stick to my plan of exposing Reona to normal dates."
    "That and proving to her that we can have clean, wholesome fun as a couple."
    "And while I admit the plan's had it's ups and downs recently, I'm not going to give up yet."
    "Which is why I convinced Reona to come along to the park with me today."
    "It's free, fun and the perfect chance for her to get in touch with nature."
    "And by that I do mean nature and not naturism!"
    show reona surprised
    reona.say "Shit..."
    reona.say "I knew that I remembered this place!"
    mike.say "You do?"
    show reona normal
    reona.say "Yeah, I do."
    reona.say "I used to come here all the time when I was younger."
    mike.say "Well that's great, Reona."
    mike.say "This'll be like a trip down memory lane for you."
    show reona happy rightok at startle
    "Reona nods and lets out a sniggering laugh."
    reona.say "Ha!"
    reona.say "It's all coming back to me now."
    reona.say "We used to smoke over there, by the restrooms."
    show reona flirt
    reona.say "Then we'd go into those woods and..."
    "I can already sense where this is going."
    show reona shy
    "So I step in, throwing my hands up to stop Reona."
    mike.say "Okay, okay..."
    mike.say "I get the picture."
    mike.say "But that's not what we're here for today."
    show reona normal leftback rightnormal
    "Reona shrugs and drops the subject."
    show reona interested
    "But I note that she keeps on looking around as we walk deeper into the park."
    "Her eyes settling on different spots as we go on, like she's still remembering the past."
    "I can't help feeling more than a little guilty at stopping Reona telling me about it too."
    "Sure, I want to get her away from the bad habits she's gotten into when it comes to kinky stuff."
    "But I can't help thinking that just ignoring that side of her isn't going to work either."
    show reona normal righthold
    mike.say "Reona..."
    reona.say "Yeah?"
    mike.say "I'm sorry I stopped you talking about your past just now."
    mike.say "That wasn't a very fair thing to do."
    show reona surprised
    "Reona looks genuinely surprised to hear my apology."
    show reona embarrassed
    "She blinks at me, then stares in silence for a moment."
    "Then she glances away, as though she's unable to look me in the eye."
    reona.say "No, [hero.name]…"
    reona.say "It's me that should be saying sorry to you."
    reona.say "You're trying so hard to make things nice for me."
    reona.say "But I find it so difficult to be like that."
    reona.say "I always have, ever since..."
    show reona sad
    "Reona almost winces as she stumbles over her words."
    "Whatever she was going to say, it's clearly a painful subject for her."
    mike.say "Ever since what, Reona?"
    mike.say "I mean, you don't have to tell me, not if you don't want to."
    mike.say "But it sounds to me like you really do..."
    "Reona takes a deep breath, and holds it for a moment."
    "Then she lets it out in one long sigh."
    reona.say "Urgh..."
    reona.say "The truth is that I wasn't always like..."
    reona.say "Well, like this, you know?"
    "I nod, keen to let Reona know that I understand her."
    "That she doesn't have to go into any more detail."
    show reona sadsmile rightopen
    reona.say "There was this guy, you see..."
    reona.say "And I was in love with him."
    reona.say "Or I thought I was in love with him."
    reona.say "You know how confusing it can be when your head's all messed up like that."
    "I nod again."
    mike.say "Oh yeah, I know what you mean."
    reona.say "Okay, so I thought he loved me too."
    reona.say "And he said that he did."
    reona.say "But it was like me saying I loved him just wasn't enough."
    reona.say "He said that he needed me to prove it to him."
    "I'm still nodding as Reona explains all of this to me."
    "But I'm beginning to think I know where this is going."
    reona.say "At first he was just asking me to do regular stuff."
    reona.say "Like, things that wouldn't freak you out to hear."
    reona.say "Then it started to get crazier and crazier."
    reona.say "But it wasn't like I noticed it at the time."
    reona.say "I dunno if I was just in denial, or if it happened so slowly it passed me by."
    reona.say "Whatever it was, by the end I was doing whatever he wanted me to do."
    reona.say "And...and it was really heavy stuff, [hero.name]."
    "By now I've stopped nodding along as Reona tells her story."
    "Because her eyes are looking straight ahead, rather than at me."
    "Like she's staring into the same past she's telling me about."
    reona.say "Anyway, it didn't last between us."
    reona.say "I think he dumped me when he'd got all of what he wanted."
    mike.say "At least it was over, Reona."
    mike.say "He couldn't hurt you anymore, right?"
    show reona sadshock righthold at startle
    "Reona lets out a rueful laugh and shakes her head."
    reona.say "You think?!?"
    show reona sadsmile
    reona.say "Let's just say he didn't keep it to himself."
    reona.say "So not only did he make me behave like a slut..."
    reona.say "He told everyone that we knew I was one too."
    reona.say "So he turned me into one, whether I liked it or not."
    mike.say "But surely you could have told your side of the story?"
    mike.say "Why would people believe him and not you?"
    show reona angry
    reona.say "It's easy for you to say that, [hero.name]."
    reona.say "For one thing, you're a guy."
    reona.say "People think it's cool for you to be fucking all the time."
    reona.say "But if a girl does the same thing, she's automatically a slut."
    reona.say "Plus you don't know how messed up I was in the head back then."
    reona.say "The guy totally screwed me up, destroyed my self-esteem."
    reona.say "I needed something that could take its place, and quickly."
    reona.say "So when I found there were guys queuing up to take their turn with the local slut..."
    show reona sadsmile
    "Reona doesn't bother to finish off what she might have been about to say."
    "Possibly because I can fill in the picture for myself."
    "Or possibly because she can't stand to dredge up any more of the past."
    "Either way the effect is the same."
    "Because now I can clearly see the vicious circle in which she's trapped."
    "Unsure of what to do next, I try something simple."
    show reona leftback at center, traveling(1.5, 1.0, (640, 1040))
    "I reach out and take hold of Reona's hand."
    "And when she doesn't pull away, I tighten my grip a little."
    mike.say "I'm sorry, Reona..."
    mike.say "Maybe I was wrong to try to do this."
    mike.say "I've been trying to change you, rather than understand you."
    mike.say "I feel like I'm as bad as they guy that hurt you in the past!"
    show reona surprised
    "Reona's head snaps around at this."
    "And she looks at me with amazement in her eyes."
    reona.say "Are you kidding me?!?"
    reona.say "For such a smart guy, you sure can be dumb sometimes!"
    mike.say "Huh?"
    mike.say "What do you mean?"
    show reona normal
    reona.say "You're the first guy in like forever that's treated me nice."
    reona.say "You've done stuff for me and not wanted sex in return."
    reona.say "This is hard because I'm a mess, not because you're doing something wrong."
    show reona devious
    reona.say "So don't be a pussy, and keep on being nice to me, you moron!"
    "As if to underline the point she's making, Reona leans in close."
    hide reona
    show reona kiss
    with fade
    $ reona.flags.kiss += 1
    "Then she plants a kiss on my lips, full of genuine passion and intensity."
    "The initial surprise passes in an instant, and I return the gesture."
    "It lasts for quite a long time, with tongues getting involved towards the end."
    "And once it's over, I find my heart is still racing."
    hide reona
    show reona normal at center, zoomAt(1.5, (640, 1040))
    with fade
    mike.say "Whoa..."
    mike.say "Reona..."
    mike.say "That was amazing!"
    reona.say "You see what I mean?"
    reona.say "You didn't make a dirty joke or ask for oral."
    reona.say "And you never tried to feel me up either!"
    show reona flirt
    reona.say "Though I'd probably have let you..."
    show reona normal
    reona.say "But the point is that I'm buzzing right now."
    reona.say "I'm excited and up for it - but I can wait for the right moment."
    reona.say "Before you came along, I'd have been begging any guy to fuck me!"
    mike.say "So you're saying I'm a turn-off?"


    show reona angry
    with hpunch
    "Reona gives me a punch in the ribs for my trouble."
    reona.say "Don't be a jerk!"
    show reona normal rightnormal
    reona.say "You know what I mean, [hero.name]."
    reona.say "I want it as bad as ever."
    reona.say "But I only want it from you!"
    "I nod, letting Reona know that I really do understand what she's saying."
    "Part of me is still trying to process all the information she just gave me."
    "To make sense of the fact that she just opened up to me for the first time."
    "I feel like this has to be a good thing, a positive thing for our relationship."
    "But that's going to take some time to do, and right now we're still on a date."
    mike.say "Come on, Reona..."
    mike.say "I want you to show me all the places you remember in the park."
    mike.say "And I want to know what you got up to there as well."
    show reona shock
    reona.say "Huh?"
    reona.say "Are you sure?"
    show reona normal
    reona.say "I thought we didn't talk about that kind of stuff?"
    mike.say "I think it's time we started to talk about every side of your personality, Reona."
    mike.say "The good, the bad and the dirty!"


    show reona happy
    with hpunch
    "Reona aims another punch at my ribs for that."
    "But I note she's smiling as she does so."
    "A sign that I hope will set the tone for the rest of our time in the park today."
    $ game.active_date.score = 100
    return

label reona_event_09:
    if reona.love.max < 200:
        $ reona.love.max = 200
    show reona embarrassed leftback
    "Almost from the first moment we met up today, I could tell that Reona had something on her mind."
    "She seems distracted and unable to concentrate on anything, which is really unusual for her."
    show reona guilty
    "Plus every time that I look in Reona's direction, I catch her looking away as if she won't meet my eye."
    mike.say "Reona..."
    mike.say "Is there something you wanted to say to me?"
    mike.say "Maybe something that's been bothering you?"
    "At first I think that Reona's going to just flat-out deny that there's anything wrong."
    "That she'll refuse to speak to me in the same way she's avoiding eye-contact."
    "But much to my surprise, the question seems to have the opposite effect."
    show reona normal at center, traveling(1.5, 1.0, (640, 1040))
    "Reona stops in her tracks, then turns to face me, looking totally resolute."
    reona.say "Okay, [hero.name]…"
    reona.say "You got me."
    reona.say "There is something on my mind."
    reona.say "Something that I really need to say to you!"
    "I was hoping to be able to get to the bottom of what's bugging Reona."
    "But not to be confronted in such a dramatic fashion as that!"
    "So I can't help taking an involuntary step backwards."
    mike.say "Oh..."
    mike.say "Okay, Reona..."
    mike.say "And what would that be?"
    "I see Reona's confidence waver for a moment, like she's going to lose her nerve."
    "But then she seems to reach down into her gut and find a new reserve of willpower."
    reona.say "I like you a lot, [hero.name]…"
    reona.say "Like, a hell of a lot!"
    "I nod at this, feeling a little puzzled."
    "Because it's not the revelation I was expecting."
    mike.say "I feel the exact same way about you, Reona."
    show reona sadsmile
    "Almost as soon as she's done speaking, Reona creases up her face."
    "She frowns and shakes her head, like she's done something wrong."
    reona.say "No, no, no..."
    reona.say "That's not what I mean!"
    reona.say "Why did I say it like that?"
    "Now I'm feeling more puzzled than ever."
    "Because if that's not what Reona means, I can't guess what she was actually trying to say."
    mike.say "You mean you don't like me?"
    mike.say "Or you just don't like me that much?"
    show reona sadshock
    reona.say "I don't like you, [hero.name]…"
    reona.say "I LOVE YOU!"
    "Now I really am feeling stunned, like I've just been slapped in the face."
    "I mean, you always hope the hot girl you're dating is going to admit she loves you."
    "But you don't really imagine it happening like this."
    mike.say "Reona, that's great!"
    mike.say "But what's the problem?"
    show reona sadfrustrated
    "Reona runs her hands through her hair and shakes her head at this."
    "And it's really one of the most dramatic performances I've seen from her!"
    reona.say "What's the problem?!?"
    with vpunch
    play sound punch_hard
    reona.say "I'm not good enough for you, [hero.name]!"
    show reona sadshock
    with vpunch
    play sound punch_hard
    reona.say "What else would it be?"
    with vpunch
    play sound punch_hard
    reona.say "I don't deserve a guy as great as you!"
    with vpunch
    play sound punch_hard
    show reona sadsmile
    "Reona keeps hitting me with these verbal and emotional body blows."
    "And one after another, they're all landing."
    "As soon as I feel like I've shaken the effects of one off, another one comes along after it."
    mike.say "What do you mean, Reona?"
    mike.say "Of course you do!"
    mike.say "We've been getting on great recently."
    mike.say "Spending time with you is the highlight of my day!"
    "I'm reaching out to take Reona's hand as I say all of this."
    show reona at center, traveling(1.25, 1.0, (640, 880))
    "But I can see that she's already starting to back away."
    show reona at center, traveling(1.0, 1.0, (640, 720))
    "Like she won't let me get close enough to actually touch her."
    show reona sadshock
    reona.say "No..."
    reona.say "I can't let you waste yourself on me, [hero.name]…"
    reona.say "You deserve someone better, someone that's not damaged goods!"
    hide reona with easeoutright
    "With that, Reona turns on her heel and hurries away from me."
    "Which leaves me standing alone, and calling after her."
    mike.say "Reona..."
    mike.say "Reona, please..."
    mike.say "Come back!"
    "Nothing I say seems to have any effect on Reona."
    "And before too long she's out of earshot anyway."
    "So I find myself all alone and confused as hell."
    "What does she mean by that?"
    "How can she even think she's not good enough for me?"
    "And what in the world am I supposed to do to change her mind?"
    $ game.active_date.stay = False
    $ hero.cancel_activity()
    if reona.love < 200:
        $ reona.flags.nodate = True
    return

label reona_event_10:
    "What Reona said to me the last time we were together has been playing on my mind ever since."
    "Hell, it was more of a confession than just something the idly tossed into the conversation!"
    "And why wouldn't it?"
    "Reona basically told me that she loved me in one breath and that she couldn't be with me in the next."
    "Plus I got a swift education on just how low her opinion of herself is in the same instant."
    "That's more than enough too give anyone pause for thought, isn't it?"
    "But it's not enough to make me want to keep my distance from Reona, no matter what she says."
    "Which is why I keep on calling and messaging her until she finally answers and agrees to meet me."
    "I've been practising what I'm going to say to her when we see each other in the flesh."
    show reona leftback with easeinleft
    "Yet the moment I lay eyes on Reona, all of that goes out of the window."
    with vpunch
    mike.say "REONA!"
    mike.say "I LOVE YOU!"
    show reona shock at startle
    "Reona's totally caught off-guard by me shouting that at her as an opening line."
    "So much so that she just stops in her tracks and stares at me in a stunned silence."
    "But I note that at least she isn't running away."
    mike.say "Sorry, sorry..."
    mike.say "That just came out, like I couldn't stop it!"
    mike.say "But I do mean that, Reona - I do love you."
    show reona normal righthold
    "Reona holds up a hand to wave in front of me."
    "And at the same time she shakes her head."
    show reona sadangry rightopen
    reona.say "Oh no, [hero.name]..."
    reona.say "I know what you're trying to do here."
    reona.say "You're trying to be my knight in shining armour, to save me."
    reona.say "And you don't need to, really you don't."
    "By now I'm shaking my head too, which makes two of us."
    "But I'm more than determined to get my message through."
    mike.say "Will you stop saying that, Reona?"
    mike.say "I'm not saying that I love you for your sake."
    mike.say "I'm being selfish and saying it for mine!"
    mike.say "And more than that, I don't want you to chance either."
    "Reona shoots me a sideways glance."
    "And I see suspicion flash in her eyes as she does so."
    show reona sadsmile
    reona.say "Huh?"
    reona.say "What's that supposed to mean?"
    reona.say "Aren't you the one that was supposed to be teaching me to be less slutty?"
    mike.say "Erm..."
    mike.say "I'd use the term 'sexually liberated', Reona..."
    mike.say "But I've realised I was wrong to do that."
    mike.say "I was wrong to try to change you."
    mike.say "The one that changes should be me."
    mike.say "And I should change to accept you just as you are."
    "I'm doing the best that I can to open myself up to Reona here."
    "To bear my heart to her in the hope of showing her I'm serious."
    "But she still doesn't seem convinced."
    show reona sadshock righthold
    reona.say "But I already told you about how that guy ruined me."
    reona.say "How he made me like this!"
    reona.say "How can you love me knowing that?"
    show reona sadsmile
    mike.say "Reona, I started falling for you almost as soon as we met."
    mike.say "Sure, I was a little intimidated by how forward you were."
    mike.say "But that was my issue, not yours."
    mike.say "And I think we wanting to do something about it was because of that."
    mike.say "I felt like I could only handle it if I was trying to correct it."
    mike.say "Really, it was me that needed fixing, not you!"
    show reona surprised
    "Reona looks at me with confusion on her face."
    reona.say "Whoa..."
    show reona shock
    reona.say "So you were the one that was fucked up the whole time?"
    reona.say "And you needed me to fix you with my super-sexy ways?"
    show reona pensive
    mike.say "Ah..."
    mike.say "I don't think that's exactly what I said, Reona!"
    mike.say "You want me to go over it again?"
    show reona normal rightnormal
    "Reona shakes her head as a smile starts to spread across her face."
    reona.say "Ah, who the hell cares!"
    show reona happy leftnormal
    reona.say "You just said you love me."
    reona.say "And that I don't have to change for you either."
    reona.say "So I'm gonna jump on that before you change your mind!"
    show reona at center, traveling(2.0, 0.5, (640, 1340))
    "With that, Reona grabs hold of me and pulls me into a tight embrace."
    hide reona
    show reona kiss
    with fade
    $ reona.flags.kiss += 1
    "Before I know what's happening, she's kissing me too."
    "Somehow I manage to regain enough of my sense to return the gesture."
    "At the same time hoping that I've managed to sort out some small part of our issues."
    $ game.active_date.score = 100
    return

label reona_kink_01:
    if reona.sub.max < 20:
        $ reona.sub.max = 20
    "Reona's one of those girls that you never expect to ask you a profound question."
    "Or to say something that's really going to make you stop and think about stuff from a new perspective."
    "Don't get me wrong, I'm not saying that she's dumb."
    "Just that she's not exactly the cerebral type, if you know what I mean?"
    "So it's usually down to me to think of the deeper things to talk about when we're together."
    "And there are always the tried and tested subjects that a guy can fall back on."
    show reona annoyed with dissolve
    reona.say "Urgh..."
    reona.say "I'm kinda bored, [hero.name]."
    show reona normal leftback righthold
    reona.say "So come on..."
    reona.say "Entertain me already!"
    show reona at center, traveling(1.5, 0.25, (640, 1040))
    pause 0.25
    with hpunch
    "Reona makes a point of poking me in the ribs to emphasize her demand."
    mike.say "Ouch!"
    mike.say "Okay, Reona, okay..."
    mike.say "You don't need to attack me!"
    show reona pensive rightnormal
    "Reona rolls her eyes at this."
    "Letting me know that she thinks I'm being dramatic."
    "But I'm still determined to complete the challenge she's set for me."
    mike.say "Erm..."
    mike.say "How about I ask you a question?"
    mike.say "How does that sound?"
    show reona annoyed rightopen
    reona.say "Like a disappointment!"
    mike.say "Hey!"
    mike.say "You haven't even heard the question yet!"
    mike.say "Okay, here goes - what's your biggest turn on?"
    show reona surprised
    mike.say "What is it that you really look for in a guy?"
    "I can see that I've surprised Reona as soon as she hears the question."
    show reona pensive leftnormal rightnormal
    "Her expression becomes instantly thoughtful as she turns it over in her head."
    "And at the same time, I'm already thinking of all the possible answers."
    reona.say "Ooh..."
    reona.say "That's a tough one."
    reona.say "You know, I don't think anyone ever asked me that before..."
    "I'm nodding my head as Reona says all of this."
    "And I'm expecting her to say something like looks, or cock size."
    "At least something that I can be pretty sure I have well covered."
    show reona normal
    reona.say "Okay..."
    show reona leftback
    reona.say "I got it!"
    reona.say "What I really like, is for a guy to have...experience."
    "I'm about to say something, but no words come out of my mouth."
    "Because Reona just took me by complete surprise."
    mike.say "Huh?"
    mike.say "What does that mean?"
    mike.say "That you like older guys?"
    "Reona shakes her head."
    show reona happy rightopen
    reona.say "No, no, no..."
    reona.say "I mean I like a guy with experience in the bedroom."
    mike.say "Oh, I see..."
    mike.say "But how do you compare one guy to another?"
    mike.say "Does he have to know certain positions?"
    mike.say "Or is it more about knowledge of the female anatomy?"
    show reona sad leftnormal rightnormal
    "Reona frowns as she thinks over my questions."
    reona.say "It's kind of hard to say."
    reona.say "Like, it doesn't make sense in a way you can turn into words."
    show reona happy leftback rightok
    reona.say "So instead, I rate all the guys that I've been with out of ten."
    reona.say "One is totally clueless."
    reona.say "And ten is a god in the sack!"
    "It's just then that something occurs to me."
    mike.say "Wait..."
    mike.say "You rate every guy you've been with?"
    show reona flirt
    reona.say "Oh yeah."
    mike.say "So you've already rated me?"
    show reona happy rightnormal
    reona.say "Well, of course..."
    mike.say "So what did I score?"
    show reona pensive
    reona.say "Erm..."
    show reona rightopen
    reona.say "You really think you can handle it?"
    "I can't help feeling more than a little insulted by the question."
    "Because I'm more than confident in my own capabilities."
    mike.say "Sure I can, Reona..."
    mike.say "So tell me - where do I rank?"
    show reona rightnormal leftnormal
    if len(hero.get_partners()) >= 20 or hero.sexperience >= 300:
        reona.say "Okay, [hero.name]..."
        reona.say "I know I'm gonna regret this..."
        show reona blush
        $ reona.sub += 5
        reona.say "I gotta be honest and say you're a ten!"
        "I was all prepared to be humble if Reona ranked me highly."
        "Likewise I was planning on being okay with it if I came somewhere in the middle."
        "But it's hard to stop a huge smile from quickly spreading across my face."
        "Because not only did Reona just rate me a perfect ten."
        "She also admitted that I'm pretty much her perfect guy!"
        mike.say "Whoa..."
        mike.say "Ten out of ten!"
        mike.say "Hail to the king, baby!"
        "I can see that Reona's beginning to look a little embarrassed."
        "Which is a pretty rare thing for her."
        "And she does the best she can to downplay the implications."
        show reona leftback rightopen
        reona.say "That doesn't mean you're the best guy in bed that ever lived!"
        reona.say "But yeah...it does mean you seem to have seen it all and done it all."
        show reona leftnormal righthold
        reona.say "Which I suppose is even better."
        mike.say "Don't worry, Reona..."
        mike.say "I promise that I won't let it go to my head."
        mike.say "I'll still be as humble as ever."
        show reona normal rightnormal
        reona.say "Who are you trying to kid, [hero.name]?!?"
        reona.say "We both know it's already swollen your head to the size of a watermelon!"
    elif len(hero.get_partners()) >= 14 or hero.sexperience >= 210:
        reona.say "Okay, [hero.name]..."
        show reona happy leftpeace
        $ reona.sub += 3
        reona.say "I gotta be honest and say you're a seven!"
        "I was all prepared to be humble if Reona ranked me highly."
        "Likewise I was planning on being okay with it if I came somewhere in the middle."
        "But it's hard to hide my relief when she rates me a seven out of ten."
        mike.say "Whoa..."
        mike.say "I've got to admit, Reona - I didn't expect to rank so high!"
        mike.say "So that means I'm pretty damn good, right?"
        "Reona nods her head."
        show reona normal leftback
        reona.say "This is all about experience, remember?"
        reona.say "Not just about how good you are in the sack."
        show reona happy
        reona.say "But yeah, you know some really nice tricks."
        reona.say "I mean, you don't know it all - not yet."
        show reona rightok
        reona.say "But I don't have any complaints!"
        "Like I already said, I'm trying my best not to seem smug."
        "But it's pretty hard when a girl like Reona bigs you up."
        "And I can't keep a huge smile from spreading across my face."
    elif len(hero.get_partners()) >= 10 or hero.sexperience >= 150:
        reona.say "Okay, [hero.name]..."
        show reona happy rightpeace
        $ reona.sub += 1
        reona.say "I gotta be honest and say you're a five!"
        "I was all prepared to be humble if Reona ranked me highly."
        "Likewise I was planning on being okay with it if I came somewhere in the middle."
        "Because there's always room for improvement, right?"
        "So being rated a five out of ten doesn't seem like too bad of a thing."
        mike.say "Oh..."
        mike.say "So..."
        mike.say "That's kind of in the middle, right?"
        mike.say "Not too good, but not too bad?"
        "Reona shakes her head at this."
        show reona normal rightopen
        reona.say "It doesn't mean you're mediocre, [hero.name]."
        reona.say "In fact, it means you get it right most of the time."
        show reona pensive rightnormal
        reona.say "But if you take your eyes off the prize..."
        reona.say "Then it can be a bit...meh!"
        "There's no way a guy likes to hear that he can be so-so."
        "But I do the best I can to ignore the negatives and focus on the positives."
        "Like the dad-rock song says, I'm halfway there."
        "Now I just need to make it the rest of the way."
        "If I can do that, then I've got it made."
    elif len(hero.get_partners()) >= 6 or hero.sexperience >= 90:
        reona.say "Okay, [hero.name]..."
        reona.say "I gotta be honest and say you're a three!"
        "I was all prepared to be humble if Reona ranked me highly."
        "Likewise I was planning on being okay with it if I came somewhere in the middle."
        "Because there's always room for improvement, right?"
        "But to be honest, I was expecting higher than a three."
        mike.say "Oh..."
        mike.say "Erm..."
        mike.say "Okay, I guess..."
        show reona normal
        reona.say "Well, [hero.name]..."
        reona.say "You said you could handle it!"
        "I nod and do the best I can to look like my ego's not been bruised."
        mike.say "No, no..."
        mike.say "It could have been worse."
        mike.say "I guess I just need to work on my technique, right?"
        "Reona nods at this, eager to put a positive spin on things."
        show reona happy rightopen
        reona.say "It doesn't mean you're bad in bed, [hero.name]."
        reona.say "Just that you could do with more experience."
        show reona normal leftback rightok
        reona.say "Sometimes you get it right, and it's amazing."
        reona.say "You just need to make sure it's more amazing."
        reona.say "And that it stays that way for longer."
    else:
        reona.say "Okay, [hero.name]..."
        show reona annoyed
        $ reona.sub -= 3
        reona.say "I gotta be honest and say you're a one!"
        "I was all prepared to be humble if Reona ranked me highly."
        "Likewise I was planning on being okay with it if I came somewhere in the middle."
        "Because there's always room for improvement, right?"
        "But the last thing that I expected was for her to give me the lowest score possible!"
        mike.say "What?!?"
        mike.say "That's as in the worst, right?"
        mike.say "We're doing it that way round?"
        show reona angry rightopen
        reona.say "Geez, [hero.name]..."
        reona.say "You said you could handle it!"
        mike.say "Well what do you expect?"
        mike.say "That was before you said I was the worst ever!"
        "Reona frowns and shakes her head at this."
        show reona leftback
        reona.say "It doesn't mean you're bad in bed, [hero.name]."
        reona.say "Just that you could do with more experience."
        show reona rightnormal
        reona.say "Like, you're eager enough to please."
        reona.say "But you just need to work on your technique..."
        reona.say "Quite a lot!"
    return

label reona_kink_02:
    if reona.sub.max < 40:
        $ reona.sub.max = 40
    reona.say "HEY!"
    reona.say "Hey, [hero.name]!"
    "At the sound of a familiar voice, I look up from what I'm doing."
    show reona leftpeace rightopen with easeinright
    "And the moment that I do, I see Reona hurrying towards me."
    "At the same time I can't keep a smile from spreading across my face."
    "Because what right-minded guy wouldn't grin at the sight of a pretty girl calling out for him?"
    "Especially a guy that knows just how much fun Reona is to be around!"
    mike.say "Oh...hey, Reona!"
    mike.say "What's with all the running and shouting?"
    show reona at center, traveling(1.5, 0.5, (640, 1040))
    "By the time I manage to get all of this out, Reona's already reached me."
    "And she's not panting or gasping for breath after sprinting over."
    "Which I guess means that she's in better shape than I gave her credit for."
    reona.say "I wanted to catch you and let you know..."
    reona.say "Let you know that I saw you the other night, yeah?"
    "I can't help frowning as Reona says all of this."
    "Because I'm not really sure what she's getting at."
    mike.say "Huh?"
    mike.say "You saw me and you didn't think to say hello?"
    show reona happy leftnormal rightpeace
    "Reona smiles and shakes her head."
    "It's like she thinks my question is a pretty silly one."
    reona.say "Of course not."
    reona.say "I could see that you were busy."
    reona.say "And I didn't want to interrupt."
    reona.say "I thought it'd be much better to talk to you about it when you were alone, am I right?"
    "Reona adds a knowing wink to underline her point."
    "But unfortunately it makes me worried that there's something wrong with her."
    "Because I'm still none the wiser as to what this is all about."
    mike.say "Interrupt what exactly?"
    show reona devious
    reona.say "Oh come on, [hero.name]..."
    reona.say "Stop acting all humble about it."
    reona.say "I saw you with that girl!"
    reona.say "I know that you were on a date with her!"
    show reona normal
    "Suddenly I feel the pit of my stomach twist and churn."
    "Panic threatens to take hold of me too."
    "And it's all I can do to keep from turning on my heel and running away."
    mike.say "Okay, Reona, okay..."
    mike.say "I'm going to need you to listen to me very carefully."
    mike.say "Because I can explain everything, yeah?"
    mike.say "You might think what you saw was me on a date with another girl..."
    mike.say "But there's a perfectly innocent explanation."
    mike.say "I just need to remember what it is!"
    show reona sad leftback righthold
    "Reona looks at me with an odd expression on her face."
    "I'm pretty sure it's not anger or spite."
    "But the odd thing is that it looks a lot like disappointment."
    show reona shock
    reona.say "An innocent explanation?!?"
    reona.say "I fucking hope not!"
    show reona sad
    mike.say "Wait..."
    mike.say "What?!?"
    show reona normal
    reona.say "I said I hope there isn't an innocent explanation."
    reona.say "Because that'd be such a downer!"
    mike.say "It...it would?"
    show reona devious
    reona.say "Of course it would!"
    reona.say "I came over here to gush about the fact I saw you with another girl."
    show reona flirt rightnormal
    reona.say "And that is SO hot!"
    reona.say "But if that's not what it was, then I guess I underestimated you."
    "By now my head is spinning from listening to Reona and trying to figure her out."
    "I've gone from being pleased to see her to making excuses for myself."
    "And now I'm doing all that I can to wrap my head around this latest declaration."
    mike.say "Wait, wait, wait..."
    mike.say "You think that catching me cheating on you is hot?!?"
    show reona annoyed
    "Reona shakes her head and rolls her eyes at this."
    reona.say "Oh, [hero.name]..."
    reona.say "What kind of selfish girls were you dating before I came along?"
    reona.say "I bet they were the kind that don't understand a real man's needs!"
    show reona normal
    reona.say "If you're seeing more than one girl, that doesn't mean you're cheating."
    mike.say "It..."
    mike.say "It doesn't?"
    show reona pensive
    reona.say "Of course not, silly!"
    reona.say "All that means is that your masculine appetites are above average."
    reona.say "That it takes more than one girl to be able to satisfy them."
    show reona normal
    "There's no doubt that I'm liking the sound of this explanation more and more."
    "But there's still a part of me that thinks it might be an elaborate trap."
    mike.say "So..."
    mike.say "Let me see if I've got this right."
    mike.say "You're not mad at me for seeing other girls?"
    mike.say "And me doing that isn't cheating on you either?"
    show reona devious
    reona.say "No, it's not!"
    reona.say "You have needs, [hero.name]."
    reona.say "Needs that have to be met!"
    "I'm starting to nod along with all that Reona's saying."
    "But then something else occurs to me."
    mike.say "And..."
    mike.say "Well..."
    mike.say "Correct me if I'm wrong, Reona..."
    mike.say "But didn't you also say something about it being...hot?"
    show reona flirt leftnormal rightok at center, traveling(2.0, 0.5, (640, 1340))
    "Reona leans in closer before she answers the question."
    "And she makes a point of draping herself over me as she does so."
    reona.say "Oh yeah!"
    reona.say "My man's too manly for one girl to be enough!"
    reona.say "And that's something that makes me feel pretty horny too!"
    "Part of me can't actually believe this is all happening."
    "My super-hot girlfriend thinks it's super-hot that I'm seeing other women."
    "And it sounds like she's more than keen for me to keep right on doing it too!"
    mike.say "You know what, Reona..."
    mike.say "Now that you mention it, I never did feel totally satisfied with one woman."
    mike.say "I mean, if I was, I wouldn't find myself looking at other girls, right?"
    "Reona's running her hands all over me as I say this."
    "And she starts nodding in agreement too."
    reona.say "Now you're getting it, [hero.name]."
    reona.say "You've got nothing to feel guilty about."
    reona.say "After all, you're just doing what comes naturally."
    reona.say "And trust me, I always cum naturally when you do me!"
    return

label reona_kink_03:
    if reona.sub.max < 60:
        $ reona.sub.max = 60
    show reona leftback
    reona.say "[hero.name]…"
    reona.say "Can I ask you something?"
    "At the sound of Reona's voice, I look up and straight at her."
    "And it's only a few seconds later that I actually realise she asked me a question."
    "Of course that's not a strange thing in of itself."
    "She's obviously asked me questions before."
    "But this time there's a certain something in the tone of voice Reona's using."
    "I can't quite put my finger on it."
    "But I get the feeling this is going to be an interesting question."
    mike.say "Sure, Reona..."
    mike.say "Ask away!"
    "Reona doesn't pause or hesitate."
    show reona devious leftnormal
    reona.say "The last girl you dated before me..."
    reona.say "What was she like?"
    "I was all ready to answer Reona's question."
    "But as soon as she brings up the subject of my most recent ex, that changes."
    "Now my head is filled with the ringing of mental alarm bells."
    "Because it's never a good thing when your current girlfriend starts asking about the one that came before them!"
    mike.say "Erm..."
    mike.say "Why would you want to know about that, Reona?"
    mike.say "I mean, she obviously couldn't hold a torch to you!"
    show reona pensive
    "Reona rolls her eyes at this makes a dismissive gesture."
    reona.say "Oh come on, [hero.name]!"
    reona.say "You know me better than that."
    reona.say "I'm not paranoid and fishing for compliments."
    show reona interested
    reona.say "I'm genuinely interested in hearing about this girl."
    show reona normal rightok
    "I study Reona in silence for what feels like a long time."
    "All the while I'm turning over what she just said inside of my head."
    "Reona's definitely not kidding when she says she's different to most girls."
    "She doesn't seem as uptight or jealous when it comes to relationships either."
    "So maybe she's telling the truth on this score too."
    mike.say "Okay, Reona..."
    mike.say "But remember, you asked for this!"
    show reona at center, traveling(1.5, 1.0, (640, 1040))
    "Reona nods eagerly, leaning in closer to hear what I have to say."
    "So I guess I really am doing this, so here goes nothing!"
    $ valid_girls = [npc for npc in [bree, sasha, samantha] if npc.sexperience > 0 and npc.flags.last_date_day > 0]
    $ sorted_valid_girls = sorted(valid_girls, key=lambda npc: npc.flags.last_date_day, reverse=True)
    if sorted_valid_girls[0] == samantha:
        mike.say "The last girl I dated was called Samantha..."
        mike.say "But I always called her Sam."
        "Reona's still nodding as she begins to hear the actual details."
        reona.say "You knew her by a nickname."
        reona.say "That's pretty cute!"
        "I can't help smiling and letting out a little chuckle."
        "Because just starting to talk about Sam is reminding me of her."
        "And all the little things I loved are coming back to me."
        mike.say "So was she..."
        mike.say "I mean so IS she!"
        "I shake my head and chuckle again."
        mike.say "Why am I talking about her in the past tense?"
        mike.say "We just broke up, and it's not like she's dead!"
        show reona happy at startle
        "Reona chuckles too."
        reona.say "Weird isn't it, how you do that?"
        reona.say "When you could bump into them on the street tomorrow!"
        show reona normal
        mike.say "Anyway..."
        mike.say "I met Sam when I moved into the house."
        mike.say "She was already living there with Ryan."
        show reona shock leftback righthold
        "At the mere mention of that name, Reona's smile changes."
        "It becomes knowing, as does the look in her eyes."
        reona.say "Don't tell me..."
        reona.say "She was with this Ryan guy."
        show reona angry
        reona.say "And he was a piece of shit?"
        "I look at Reona in amazement."
        mike.say "How did you know that?!?"
        show reona sad
        "Reona offers me a shrug."
        show reona annoyed
        reona.say "Ah, it's a classic scenario, as old as time itself."
        reona.say "Nice guy meets nice girl, but nice girl is dating douchebag!"
        show reona sad
        mike.say "Pretty much..."
        mike.say "I kind of held a torch for Sam all the time she was with Ryan."
        mike.say "Hell, they even got married for a while, but that didn't last."
        mike.say "He was cheating on Sam and eventually she found out."
        mike.say "She moved out and came back to the house for a while."
        show reona pensive
        reona.say "And then nature took it's course?"
        reona.say "Or did you sense that this was your chance, huh?"
        "I can feel my cheeks flushing at the mere suggestion."
        mike.say "Hey!"
        mike.say "It wasn't like that at all."
        mike.say "Sam needed someone to open up to."
        mike.say "And I couldn't help my feelings coming out."
        show reona normal
        "Reona nods."
        reona.say "Makes sense to me."
        reona.say "So what happened to ruin it?"
        reona.say "Why aren't you still together and planning to settle down?"
        "All I can do in response to that is shrug my shoulders."
        mike.say "Honestly, Reona?"
        mike.say "I wish I knew the answer to that!"
        mike.say "I always thought that Sam and I were supposed to be."
        mike.say "But I guess things don't always work out the way you hoped."
        show reona interested
        "Reona's nodding, clearly expecting me to say more."
        reona.say "But you had fun while it lasted, right?"
        reona.say "This Sam, did she live up to your hopes in the bedroom, or what?"
        mike.say "Hey!"
        mike.say "What are you trying to say?"
        show reona flirt
        reona.say "Oh come on, [hero.name]!"
        reona.say "No guy worships a girl like that and doesn't want to do her."
        show reona interested
        reona.say "So come on and spill - what was she like in the sack?!?"
        "I can see that Reona's not going to let it drop."
        "And so I decide to open up about that side of things."
        mike.say "She turned out to be pretty amazing, Reona."
        mike.say "Let's just say that I'd spent a lot of time imagining what it'd be like to be with her."
        mike.say "And nothing I imagined prepared me for how good it was in reality!"
        show reona happy leftnormal rightnormal
        with hpunch
        play sound punch_hard
        "Reona gives me a playful jab in the ribs."
        reona.say "You see, [hero.name]?"
        reona.say "You told me all about her, even the screwing."
        reona.say "And I'm still here, aren't I?"
        "I nod and begin to smile myself."
        "Because Reona's right, nothing bad happened at all."
        "In fact I kind of feel better for having opened up about Sam to her."
        "It's like she helped me to start drawing a line under the whole thing."
        show reona at center, traveling(1.0, 1.0, (640, 720))
        "And even though it didn't work out, I'm starting to see what I gained from the relationship."
        "Which is pretty awesome, especially when you think most girls would have just gotten jealous."
    elif sorted_valid_girls[0] == sasha:
        mike.say "The last girl that I actually officially dated was Sasha."
        mike.say "And yeah, she's one of my current housemates."
        mike.say "So it can get a bit awkward!"
        show reona normal rightopen
        "Reona's still nodding as she begins to hear the actual details."
        reona.say "Yeah, I get that."
        reona.say "But you must have really been into her."
        reona.say "Because you still dated her knowing that, right?"
        "I have to nod in agreement."
        "Because Reona's got me bang to rights."
        mike.say "You're right."
        mike.say "I knew it was a risk when we got together."
        mike.say "Dating a person you have to see almost every day."
        show reona interested
        reona.say "And was she worth it?"
        "I think about the question for a moment, thinking that it should be hard to answer."
        "But much to my surprise, I find that I'm already answering it, almost without thinking."
        mike.say "It sure was!"
        show reona happy rightok
        "Reona seems to be pleased with my spontaneous answer."
        "But it leaves me feeling more than a little embarrassed."
        "Because I've just been reminded of how much I wanted Sasha back then."
        "And here I am talking about it to my current girlfriend!"
        mike.say "I'm sorry, Reona..."
        mike.say "I didn't mean to..."
        show reona devious leftback rightnormal
        reona.say "Ah, shut up, [hero.name]!"
        reona.say "You existed before we met, and so did your cock!"
        reona.say "Don't apologise for your previous conquests."
        reona.say "I already told you, I think it's hot you've got some notches on your bedpost!"
        "I give Reona a nervous nod and a smile as I try to press on."
        "No matter how many times she reassures me on that front, it still feels strange."
        "Most girls are crazily jealous of a guy's previous girlfriends."
        show reona normal
        "But Reona just doesn't seem to see them as a threat."
        mike.say "Okay, okay..."
        mike.say "At first Sasha and I started getting on just as friends."
        mike.say "She's a rock-chick, which is pretty hot to begin with."
        mike.say "But she also plays guitar in a band, and she's seriously good!"
        mike.say "So that instantly made her even more amazing."
        mike.say "We found that we had a lot in common and we started hanging out."
        show reona devious
        reona.say "Then one thing led to another?"
        mike.say "You could say that."
        mike.say "It just felt natural, you know?"
        if sasha.flags.breakup:
            mike.say "But I guess it just wasn't meant to be a long-term thing."
        show reona flirt leftnormal
        "Reona nods."
        reona.say "But you had fun while it lasted, right?"
        reona.say "This Sasha, did she live up to your hopes in the bedroom, or what?"
        mike.say "Hey!"
        mike.say "What are you trying to say?"
        reona.say "Oh come on, [hero.name]!"
        reona.say "No guy talks about a hot rock-chick like that and doesn't want to do her."
        show reona interested
        reona.say "So come on and spill - what was she like in the sack?!?"
        "I can see that Reona's not going to let it drop."
        "And so I decide to open up about that side of things."
        mike.say "She turned out to be pretty amazing, Reona."
        mike.say "Sasha was wild and crazy, she introduced me to some kinky stuff too."
        mike.say "She was way more fun to be with than I could have imagined!"
        show reona happy leftnormal rightnormal
        with hpunch
        play sound punch_hard
        "Reona gives me a playful jab in the ribs."
        reona.say "You see, [hero.name]?"
        reona.say "You told me all about her, even the screwing."
        reona.say "And I'm still here, aren't I?"
        "I nod and begin to smile myself."
        "Because Reona's right, nothing bad happened at all."
        "In fact I kind of feel better for having opened up about Sasha to her."
        "It's like she helped me to start drawing a line under the whole thing."
        show reona at center, traveling(1.0, 1.0, (640, 720))
        "And even though it didn't work out, I'm starting to see what I gained from the relationship."
        "Which is pretty awesome, especially when you think most girls would have just gotten jealous."
    elif sorted_valid_girls[0] == bree:
        mike.say "The last girl that I actually officially dated was [bree.name]."
        mike.say "And yeah, she's one of my current housemates."
        mike.say "So it can get a bit awkward!"
        show reona normal rightopen
        "Reona's still nodding as she begins to hear the actual details."
        reona.say "Yeah, I get that."
        reona.say "But you must have really been into her."
        reona.say "Because you still dated her knowing that, right?"
        "I have to nod in agreement."
        "Because Reona's got me bang to rights."
        mike.say "You're right."
        mike.say "I knew it was a risk when we got together."
        mike.say "Dating a person you have to see almost every day."
        show reona interested
        reona.say "And was she worth it?"
        "I think about the question for a moment, thinking that it should be hard to answer."
        "But much to my surprise, I find that I'm already answering it, almost without thinking."
        mike.say "It sure was!"
        show reona happy rightok
        "Reona seems to be pleased with my spontaneous answer."
        "But it leaves me feeling more than a little embarrassed."
        "Because I've just been reminded of how much I wanted [bree.name] back then."
        "And here I am talking about it to my current girlfriend!"
        mike.say "I'm sorry, Reona..."
        mike.say "I didn't mean to..."
        show reona devious leftback rightnormal
        reona.say "Ah, shut up, [hero.name]!"
        reona.say "You existed before we met, and so did your cock!"
        reona.say "Don't apologise for your previous conquests."
        reona.say "I already told you, I think it's hot you've got some notches on your bedpost!"
        "I give Reona a nervous nod and a smile as I try to press on."
        "No matter how many times she reassures me on that front, it still feels strange."
        "Most girls are crazily jealous of a guy's previous girlfriends."
        show reona normal
        "But Reona just doesn't seem to see them as a threat."
        mike.say "Okay, okay..."
        mike.say "At first [bree.name] and I started getting on just as friends."
        mike.say "She's a gamer-girl, totally in the zone when she's playing."
        mike.say "So right from the start we had a lot in common."
        mike.say "But [bree.name]'s also totally talented, to the point she can kick ass in tournaments and stuff."
        mike.say "So that instantly made her even more amazing."
        mike.say "We found that we liked playing together and we started hanging out."
        show reona devious
        reona.say "Then one thing led to another?"
        mike.say "You could say that."
        mike.say "It just felt natural, you know?"
        mike.say "But I guess it just wasn't meant to be a long-term thing."
        show reona flirt leftnormal
        "Reona nods."
        reona.say "But you had fun while it lasted, right?"
        reona.say "This [bree.name], did she live up to your hopes in the bedroom, or what?"
        mike.say "Hey!"
        mike.say "What are you trying to say?"
        reona.say "Oh come on, [hero.name]!"
        reona.say "No guy talks about a hot gamer-girl like that and doesn't want to do her."
        show reona interested
        reona.say "So come on and spill - what was she like in the sack?!?"
        "I can see that Reona's not going to let it drop."
        "And so I decide to open up about that side of things."
        mike.say "She turned out to be pretty amazing, Reona."
        mike.say "[bree.name] was sweet and sensual, as well as loving to fool around."
        mike.say "She was way more fun to be with than I could have imagined!"
        show reona happy leftnormal rightnormal
        with hpunch
        play sound punch_hard
        "Reona gives me a playful jab in the ribs."
        reona.say "You see, [hero.name]?"
        reona.say "You told me all about her, even the screwing."
        reona.say "And I'm still here, aren't I?"
        "I nod and begin to smile myself."
        "Because Reona's right, nothing bad happened at all."
        "In fact I kind of feel better for having opened up about [bree.name] to her."
        "It's like she helped me to start drawing a line under the whole thing."
        show reona at center, traveling(1.0, 1.0, (640, 720))
        "And even though it didn't work out, I'm starting to see what I gained from the relationship."
        "Which is pretty awesome, especially when you think most girls would have just gotten jealous."
    return

label reona_kink_04:
    if reona.sub.max < 80:
        $ reona.sub.max = 80
    show reona
    reona.say "So..."
    reona.say "You remember we talked about you seeing other girls?"
    "At first I'm just vaguely turning my attention away from what I'm doing and towards Reona."
    "But the moment I hear her bring up that particular topic, my head snaps straight around."
    "And within a fraction of a second, I'm totally focussed on Reona and what she's got to say."
    mike.say "Erm..."
    mike.say "Yeah, Reona..."
    mike.say "I'm not going to forget something like that in a hurry!"
    show reona interested
    "Reona looks at me expectantly, like she's waiting for me to say something more."
    "And the silence between us soon becomes so awkward that I feel like I have to break it."
    mike.say "Was there something else I was meant to say just now?"
    mike.say "Because it seems like you're hanging in there to hear me say more!"
    show reona annoyed leftback
    "Reona's expression becomes a little exasperated at this."
    "And she nods her head vigorously too, underlining the point."
    reona.say "Of course there is, [hero.name]!"
    show reona devious rightpeace
    reona.say "Aren't you going to tell me how many girls you're dating?"
    reona.say "Like seeing right now?!?"
    "I feel more than a little ambushed by the question."
    "Before now I just thought Reona was cool with me seeing other girls."
    "I had no idea she expected me to report back to her on my efforts!"
    "But from the way she's looking at me right now, I can tell that's exactly what Reona wants."
    if len(hero.get_girlfriends()) <= 0:
        "I suppose that the best thing here is to be honest."
        "So I just shrug and shake my head."
        mike.say "I'm not dating anyone apart from you right now, Reona."
        mike.say "Sorry to disappoint you."
        show reona surprised righthold
        "I can see that Reona wasn't expecting that answer."
        "But it's not like she can come out and complain to me about it either."
        "So she seems to do the best she can to hide her disappointment."
        show reona embarrassed
        reona.say "Oh, it's okay, [hero.name]."
        reona.say "You just need some time to work on it, that's all!"
        show reona guilty
        "Reona seems to think about the situation for a moment."
        "Then she shares her thoughts with me."
        show reona sadangry
        reona.say "I hate to pry..."
        reona.say "But are you really trying to attract other girls?"
        reona.say "I mean, you need to be looking for all the signs."
        reona.say "And I know guys can be really bad at spotting them."
        show reona normal
        mike.say "Thanks for the advice, Reona."
        mike.say "I'll be sure to try harder in future."
        show reona happy
        reona.say "You do that, [hero.name]."
        reona.say "And be sure to keep me in the loop!"
    elif len(hero.get_girlfriends()) <= 4:
        "I suppose that the best thing here is to be honest."
        "So I just shrug, shake my head and tell it how it is."
        mike.say "I won't lie, Reona..."
        mike.say "I've been seeing a couple of other girls."
        show reona surprised righthold
        "Reona's eyes go wide at the casual admission."
        "It looks like that was the kind of answer she was hoping for."
        show reona interested at center, traveling(1.5, 1.0, (640, 1040))
        "She leans in closer, eager to get more details."
        reona.say "How many is a couple?"
        reona.say "Is that like, two?"
        reona.say "Or three?"
        reona.say "Or maybe even four?"
        mike.say "Believe it or not, Reona..."
        mike.say "It's pretty hard keeping track!"
        show reona devious
        reona.say "I get that, [hero.name]…"
        show reona interested
        reona.say "But still, try to be specific!"
        "I can see that I'm not getting out of this one."
        "So I do the best I can to give Reona a number."
        mike.say "Maybe three?"
        mike.say "Let's go with that."
        show reona normal
        "Reona's nodding all the time I'm saying this."
        "And I can see that she's loving every moment."
        show reona blush
        "It seems to be seriously turning her on too!"
        show reona flirt
        reona.say "Oh yeah..."
        reona.say "My man needs three girls to satisfy him!"
        "All I can do is nod and smile at this."
        show reona at center, traveling(1.0, 1.0, (640, 720))
        "Relieved to know that she approves of what I'm doing."
    elif len(hero.get_girlfriends()) <= 9:
        "I suppose that the best thing here is to be honest."
        "So I just shrug, shake my head and tell it how it is."
        mike.say "I won't lie, Reona..."
        mike.say "I've been seeing quite a few other girls!"
        show reona surprised leftnormal rightopen
        "Reona's eyes go wide at the casual admission."
        "It looks like that was the kind of answer she was hoping for."
        show reona interested at center, traveling(1.5, 1.0, (640, 1040))
        "She leans in closer, eager to get more details."
        reona.say "How many is a quite a few?"
        reona.say "Because like, half-a-dozen would be impressive."
        reona.say "But more than that and I'd be really impressed."
        mike.say "Believe it or not, Reona..."
        mike.say "It's pretty hard keeping track!"
        show reona devious
        reona.say "I get that, [hero.name]…"
        show reona interested
        reona.say "But still, try to be specific!"
        "I can see that I'm not getting out of this one."
        "So I do the best I can to give Reona a number."
        mike.say "Maybe seven?"
        mike.say "Or more like eight?"
        mike.say "Let's go with that."
        show reona happy rightok
        "Reona's nodding all the time I'm saying this."
        "And I can see that she's loving every moment."
        show reona blush
        "It seems to be seriously turning her on too!"
        show reona at center, traveling(1.75, 0.3, (640, 1200))
        "She wraps her arm around mine, pulling me close."
        show reona flirt
        reona.say "Oh yeah..."
        reona.say "My man needs eight girls to satisfy him!"
        reona.say "More girls than there are days of the week!"
        "All I can do is nod and smile at this."
        show reona at center, traveling(1.0, 1.0, (640, 720))
        "Relieved to know that she approves of what I'm doing."
    elif len(hero.get_girlfriends()) <= 19:
        "I suppose that the best thing here is to be honest."
        "So I just shrug, shake my head and tell it how it is."
        mike.say "I won't lie, Reona..."
        mike.say "I've been seeing a hell of a lot of other girls!"
        show reona shock
        "Reona's eyes go wide at the casual admission."
        "It looks like that was the kind of answer she was hoping for."
        show reona interested at center, traveling(1.5, 1.0, (640, 1040))
        "She leans in closer, eager to get more details."
        show reona happy leftnormal
        reona.say "That's what I wanted to hear!"
        reona.say "How many is a hell of a lot?"
        reona.say "Because like, ten would be impressive."
        reona.say "But if you got all the way up into the teens..."
        reona.say "Then that would be really impressive!"
        mike.say "Believe it or not, Reona..."
        mike.say "It's pretty hard keeping track!"
        show reona devious
        reona.say "I get that, [hero.name]…"
        show reona interested
        reona.say "But still, try to be specific!"
        "I can see that I'm not getting out of this one."
        "So I do the best I can to give Reona a number."
        mike.say "Maybe sixteen?"
        mike.say "Or more like seventeen?"
        mike.say "Let's go with that."
        show reona devious rightok
        "Reona's nodding all the time I'm saying this."
        "And I can see that she's loving every moment."
        show reona blush
        "It seems to be seriously turning her on too!"
        "Because she can't keep her hands off me."
        show reona at center, traveling(1.75, 0.3, (640, 1200))
        "She wraps her arm around mine, pulling me close."
        show reona flirt
        reona.say "Oh yeah..."
        reona.say "My man needs seventeen girls to satisfy him!"
        reona.say "More girls than there are days in a fortnight!"
        "All I can do is nod and smile at this."
        show reona at center, traveling(1.0, 1.0, (640, 720))
        "Relieved to know that she approves of what I'm doing."
    else:
        "I suppose that the best thing here is to be honest."
        "So I just shrug, shake my head and tell it how it is."
        mike.say "I won't lie, Reona..."
        mike.say "I've been seeing a totally insane number of girls!"
        mike.say "So many in fact, that I'm completely knackered!"
        show reona shock
        "Reona's eyes go wide at the casual admission."
        "It looks like that was the kind of answer she was hoping for."
        show reona interested at center, traveling(1.5, 1.0, (640, 1040))
        "She leans in closer, eager to get more details."
        show reona leftnormal
        reona.say "That's what I wanted to hear!"
        reona.say "How many is a totally insane number?"
        reona.say "Because like, twenty would be impressive."
        reona.say "But if it was even more than that..."
        reona.say "Then you be completely blowing my mind!"
        mike.say "Believe it or not, Reona..."
        mike.say "It's pretty hard keeping track!"
        mike.say "My brain's as tired as my body right now."
        mike.say "And I can't even think straight anymore!"
        show reona devious
        reona.say "I get that, [hero.name]…"
        show reona interested
        reona.say "But still, try to be specific!"
        "I can see that I'm not getting out of this one."
        "So I do the best I can to give Reona a number."
        mike.say "Maybe twenty?"
        show reona happy righthold
        mike.say "Or maybe it was more than that?"
        mike.say "Let's say that it was...that it was more than twenty."
        "Reona's nodding all the time I'm saying this."
        "And I can see that she's loving every moment."
        show reona blush
        "It seems to be seriously turning her on too!"
        "Because she can't keep her hands off me."
        "Or herself, as I swear I see one of them disappear below her skirt!"
        show reona at center, traveling(1.75, 0.3, (640, 1200))
        "She wraps her arm around mine, pulling me close."
        show reona flirt
        reona.say "Oh yeah..."
        reona.say "My man needs more than twenty girls to satisfy him!"
        reona.say "At this rate, we're going to have to bring them in by the bus-load!"
        "All I can do is nod and smile at this."
        show reona at center, traveling(1.0, 1.0, (640, 720))
        "Relieved to know that she approves of what I'm doing."
    return

label reona_kink_05:
    if reona.sub.max < 100:
        $ reona.sub.max = 100
    show reona leftback
    "It's been hard not to notice how keen Reona's been on the idea of me seeing other girls recently."
    "In fact, every time we meet up, she seems to find an excuse to bring up the subject."
    "Then I find myself being aggressively pumped for details on how it's all progressing."
    "At first I was over the moon that my girlfriend was cool with me seeing other women as the same time."
    "But now I'm starting to feel like it's some kind of weird sociological experiment."
    "You know, rather than just a chance to sleep around without any consequences?"
    "So when Reona brings it up again, can you really blame me for trying to change the subject?"
    show reona devious blush
    reona.say "You know what, [hero.name]…"
    reona.say "It's such a thrill knowing that you're totally in demand."
    reona.say "That there's a string of women you've satisfied and left in your wake!"
    show reona normal
    "I can't help my face creasing into a pretty painful frown at this."
    mike.say "You think we could talk about something else for a while, Reona?"
    mike.say "All of this stuff is very flattering to my ego."
    mike.say "But you do kind of make me sound like some kind of rampaging barbarian."
    mike.say "Like I'm leaving a series of pillaged villages in my wake!"
    show reona annoyed
    "Reona puts on a frown of her own in response to this."
    "But I can see that hers is one of amusement, rather than frustration."
    show reona devious righthold
    reona.say "Oh don't be silly, [hero.name]..."
    reona.say "The way I see things, you're more like Santa Claus."
    reona.say "Visiting good girls with a surprise for them in your sack!"
    mike.say "Okay, Reona..."
    mike.say "I'm going to have to stop you right there."
    mike.say "That and ask you never to compare me to Santa in that way again!"
    "No matter what I say on the subject, Reona doesn't seem to change her tune."
    show reona happy leftnormal rightnormal at startle
    "She just laughs off my response."
    "And then she carries on as though we're both on the same page."
    show reona normal
    reona.say "Ah..."
    show reona devious
    reona.say "But seriously, though..."
    show reona flirt
    reona.say "I am loving the thought of you spreading yourself about."
    reona.say "I'm thinking about it all the time - even fantasising about it too!"
    show reona normal
    "I know that I should try as best I can to shut this kind of thing down."
    "But the problem is that, underneath all of my smarts, I'm still a guy."
    "And what guy wouldn't get an ego-rub from hearing something like that?"
    mike.say "You..."
    mike.say "You are?"
    "Reona doesn't pause for a moment before nodding her head."
    "I can see this is a subject she's desperate to talk about."
    "And it seems like all she needed to gush about it was my permission too!"
    show reona pensive rightok
    reona.say "Of course I am, silly!"
    reona.say "Just the thought of you with one, two or three girls..."
    show reona devious rightpeace
    reona.say "Oooh..."
    reona.say "I'm getting hot just thinking about it now!"
    reona.say "All of those hot, feminine bodies, writhing away atop each other."
    reona.say "And all of them are doing it in the hope of getting to my man!"
    show reona leftback
    "I can see one of Reona's hands starting to move as she says all of this."
    "And I watch in silent amazement as it travels down the length of her body."
    "The hand makes it all the way down to Reona's waist."
    "And I swear that it was going to go further down too."
    "But that's when she sees me watching her, and pulls it back again."
    mike.say "So..."
    mike.say "You've been fantasising about me with other girls?"
    mike.say "That's...interesting!"
    show reona sadsmile
    "Reona shakes her head at this."
    reona.say "Oh no, [hero.name]..."
    show reona flirt righthold
    reona.say "Not just you and other girls."
    reona.say "You, other girls AND me!"
    reona.say "I can't stop thinking about how hot that would be."
    reona.say "To belong to a whole harem of girls, all wanting to serve you!"
    "I have to admit that Reona's painting a very vivid picture with her words."
    "From the tone of her voice and the look in her eyes, I can almost visualise it."
    "And she's selling the idea to me more with each passing moment too!"
    mike.say "Yeah, Reona..."
    mike.say "That's one hot fantasy!"
    "I'm gazing into the distance, thinking of the possibilities."
    show reona at center, traveling(1.5, 0.3, (640, 1040))
    "And that's exactly when Reona chooses to grab hold of me."
    "The sensation shocks me back to reality, and I find her staring straight into my eyes."
    show reona devious
    reona.say "It doesn't have to be, [hero.name]..."
    reona.say "A fantasy, that is."
    reona.say "If we wish hard enough, I'm certain it could come true!"
    "Reona doesn't say anything more on the subject."
    show reona at center, traveling(1.0, 0.6, (640, 720))
    "But I can tell from the look in her eyes that this isn't the end of it."
    "Not by any means."
    return

label reona_kink_06:
    show reona
    reona.say "[hero.name]…"
    show reona happy leftpeace rightopen
    reona.say "Hey, [hero.name]!"
    show reona at center, traveling(1.5, 2.0, (640, 1040))
    "At the sound of Reona's voice, I look up and see her hurrying towards me."
    "Of course my face instantly breaks into a smile at the mere sight of her."
    "And at the same time I can feel my mood getting better and better."
    "All of this while my heart is starting to beat faster too."
    "And why shouldn't any of that be true?"
    "I'm watching the girl that I love come running towards me."
    "The incredibly hot and sexually liberated girl that I love, I might add!"
    mike.say "Reona..."
    mike.say "Great to see you!"
    mike.say "And might I say that you're looking amazing, as usual!"
    show reona devious leftnormal
    "Reona's already smiling and even blushing a little as she reaches me."
    "The compliments that I'm giving her having a visible effect."
    "An effect that only serves to make her look better than ever."
    reona.say "Oh, you charming devil, you!"
    reona.say "How come you always know exactly what to say?"
    "I'm about to offer whatever answer I can think of to Reona."
    "But then she cuts me off by answering her own question."
    show reona happy
    reona.say "Because you're the perfect man, that's how."
    reona.say "And I'm the luckiest girl in the world to have you."
    reona.say "Which is something I'll never stop reminding myself of too!"
    "I can feel myself starting to get embarrassed by the way Reona's talking."
    "It's one thing when I'm the person heaping saccharine compliments onto a girl."
    "But another thing altogether when she's the one doing the same thing to me."
    "And yeah, I know that's hypocritical of me."
    "But it's just the way I am."
    mike.say "Aw..."
    mike.say "Quit it, Reona!"
    mike.say "I'm not that great really."
    "I intended the comment as a throwaway response."
    "Something that would serve to defuse the awkwardness I'm feeling."
    show reona normal leftback righthold
    "But the moment she hears what I have to say, Reona's mood changes."
    show reona annoyed
    "She suddenly becomes serious, shaking her head at me."
    reona.say "No, [hero.name]…"
    reona.say "Oh hell no!"
    reona.say "I won't let you talk about yourself like that."
    reona.say "Not when I've got to say to you what..."
    reona.say "Well, what I've got to say to you!"
    show reona devious
    "The truth is that this sudden surge of seriousness catches me totally off-guard."
    "And not only that, it kind of makes me a little worried to hear what Reona's talking about."
    "But I also get the impression that she's deadly serious right now."
    "So I do the best I can to steel myself and hear her out."
    mike.say "Okay, Reona..."
    mike.say "I guess you'd better say your piece."
    show reona happy
    "Reona gives me a little smile and a nod."
    reona.say "Okay..."
    reona.say "Here goes nothing..."
    show reona happy leftnormal rightnormal
    reona.say "I just wanted to say that I've never been as happy as I am right now."
    reona.say "And I totally mean that my life has gotten one hundred percent better since I met you."
    reona.say "It's not just like I love you either, you've like, given me a new purpose to live!"
    reona.say "Being with you and devoting myself to the task of fulfilling you sexually..."
    reona.say "I now know that's my calling in life, my reason for being here!"
    "I'm doing the best I can to keep my promise to Reona."
    "And it sounds like she's opening up her heart to me."
    "It's just that I never expected that to sound like what I'm hearing."
    "This is more like she's offering herself up as a living sacrifice to me!"
    show reona blush
    reona.say "And I want to keep on doing that, [hero.name]…"
    reona.say "I want to serve you..."
    reona.say "In a sexual capacity, that is..."
    reona.say "And for the rest of my life!"
    "I'm about to ask Reona if she's serious."
    "To check that she's actually thought all of this through."
    "But then I see the look in her eyes and realise there's no point."
    "Because all the proof I need is right there, and it's plain to see."
    "So instead, I open my arms wide and beckon for her to come closer."
    "Reona reacts in just the way I hoped she would."
    "She flings her own arms wide too."
    show reona at center, traveling(2.0, 0.1, (640, 1300))
    "And then she practically throws herself at me!"
    "The embrace that follows is long and intense."
    "I feel that it also allows us to communicate on an unconscious level too."
    "That the act of squeezing each other tightly underscores everything that's been said."
    "It takes a long time for me to want to let Reona go."
    show reona normal at center, traveling(1.0, 1.0, (640, 720))
    "But when I do, I'm secure in the feeling that she won't be going anywhere I'm not."
    return

label reona_redemption_01:
    if reona.purity.max < 20:
        $ reona.purity.max = 20
    "It's been a couple of days since my last study session with Reona."
    "Or to be more accurate, since she tried to give me oral in return for it."
    "And though the surprise I felt is long gone, it's still playing on my mind."
    "Of course part of that is on account of the fact it was a hard thing to refuse."
    "But the more I think about it, the more it makes me worry about Reona herself."
    "I mean, if she's in the habit of making such an offer just for help with her studies..."
    "Then what else is she going to be doing it for as well?"
    "And how long is it going to be before someone takes advantage of her?"
    "Hell, something like that could already have happened!"
    "That's why I head straight over to Reona the next time I see her at college."
    "I feel like I have to say something to her."
    "Whether she'll listen or not, I still have to try."
    scene bg classroom
    show reona leftback at center, zoomAt(1.0, (940, 720))
    with fade
    mike.say "Reona..."
    mike.say "Hey, Reona..."
    show reona surprised leftnormal at center, traveling(1.25, 1.0, (740, 820)) with ease
    "Reona turns at the sound of someone calling her name."
    "And when she sees that it's me, she walks in my direction."
    "Which is a relief, as I was worried she might blank me or something."
    show reona happy rightopen leftback at center, zoomAt(1.25, (640, 820)) with ease
    reona.say "Hey, [hero.name]..."
    reona.say "Have you come to talk to me about my offer?"
    mike.say "Ah, yeah..."
    mike.say "That's kind of it..."
    show reona rightnormal leftnormal
    "Suddenly I see a knowing smile spread across Reona's face."
    "And she nods her head, like she's been here before."
    reona.say "I knew it!"
    reona.say "You guys are all the same."
    show reona normal righthold
    reona.say "Once I'm in there..."
    "She taps the side of my head as she says this."
    reona.say "Then there's no way of getting me out!"
    show reona leftback rightnormal annoyed
    reona.say "So..."
    reona.say "You got anywhere in mind?"
    reona.say "There's a bathroom round the corner with a busted crapper."
    show reona normal rightok
    reona.say "So nobody goes in there."
    show reona normal rightok at center, traveling(1.0, 0.2, (640, 720))
    "I hold up my hands and take a step backwards."
    "Because Reona's going way too fast and in the wrong direction."
    show reona surprised
    mike.say "Whoa..."
    mike.say "Slow down, Reona!"
    mike.say "I want to talk to you about your offer, that's all."
    mike.say "I don't want to take you up on it."
    show reona pensive leftnormal righthold
    "Reona crosses her arms over her chest and frowns."
    "Then she hits me with a serious stare."
    reona.say "Oh yeah?"
    reona.say "Is that so?"
    show reona annoyed rightnormal
    reona.say "And just what about it do you want to discuss?"
    show reona pensive
    "I swallow audibly as I prepare to say my piece."
    "But then I just launch into it, consequences be damned."
    mike.say "I think I know why you do that, Reona..."
    mike.say "Why you offer to do sexual things for people."
    show reona normal leftback at startle(0.05,-10)
    "Reona gives this a derisive snort."
    show reona devious
    reona.say "Ha..."
    reona.say "So do I..."
    reona.say "It's because I like doing shit like that!"
    mike.say "I don't think that's the real reason, Reona."
    show reona embarrassed
    mike.say "I think it's because you don't put enough value in yourself."
    mike.say "You think the only way people will like you is if you please them."
    "I'm expecting Reona to fire straight back at me."
    "But instead she pauses for a moment."
    "Almost as if my words have affected her."
    reona.say "That..."
    show reona angry rightopen
    reona.say "That's bullshit!"
    mike.say "Is it though?"
    mike.say "I think you should value yourself more, Reona."
    mike.say "That you'd be a lot happier if you stopped putting it about so much."
    mike.say "Have you thought about finding yourself a good man?"
    mike.say "Hell, this is the twenty-first century - so even a good woman?"
    show reona sad rightnormal
    mike.say "You know, someone you can actually love and cherish?"
    mike.say "Someone that will do the same for you in return?"
    "Reona seems to have been gathering her strength as I say all of this."
    "Because I can see that the same hesitation is still there in her eyes."
    "Yet she manages to shake her head and let out a loud laugh of derision."
    show reona devious at startle
    reona.say "HA!"
    reona.say "You've got to be joking!"
    show reona rightok leftpeace
    reona.say "I do what I want with who I want, period."
    reona.say "Not because I'm down on myself."
    reona.say "Because I want to do it and I love it!"
    show reona leftback rightnormal
    reona.say "And I can get anyone I want too."
    "I can't help raising my eyebrows at this last boast."
    mike.say "Oh really?"
    mike.say "I seem to remember turning you down not long ago!"
    show reona sad
    "Reona's eyes narrow as I throw that back in her face."
    "And she cocks her head on one side as she stares into my own eyes."
    show reona devious rightopen
    reona.say "That was just a fluke!"
    reona.say "And I'll prove it too."
    reona.say "I'll bet I can make you mine, [hero.name], that you'll sleep with me."
    "The idea of making such a bet sounds crazy to me."
    "But now Reona's managed to get my blood up too."
    "So there's no chance of me being the level-headed one here."
    mike.say "You're on, Reona!"
    reona.say "If I win, you back off telling me to change my ways."
    mike.say "And if I win, you stop sleeping around."
    show reona at center, traveling(1.5, 1.0, (640, 1040))
    "I hold out my hand, and Reona takes it."
    show reona at startle
    "Then we shake hands to seal the deal."
    show reona rightok
    reona.say "This is going to be easy, [hero.name]."
    reona.say "And trust me, you'll never enjoy losing a bet as much as this one!"
    hide reona with easeoutleft
    "With that, she releases my hand and turns on her heel."
    "And I'm left to watch her walking away, wondering what the hell I was thinking."
    "Did I really just agree to let a girl the likes of Reona do her best to seduce me?!?"
    "Oh man...how do I get myself into situations like this?"
    $ reona.flags.redemptiondelay = TemporaryFlag(True, 3)
    return

label reona_redemption_02:
    if reona.purity.max < 40:
        $ reona.purity.max = 40
    "I've kind of been avoiding Reona since we had the conversation about relationships."
    "Well, if you can call me not calling her since then and hoping that she wouldn't call me avoiding someone."
    "I guess it'd be more truthful to say that I've been waiting for her to pop up and have it out with me."
    "But I'm under no illusion that Reona's the kind of girl that's just going to be able to let it go."
    show reona upset leftback at center, zoomAt(1.25, (640, 880)) with dissolve
    "So it comes as no surprise when I see her standing in front of me, balled hands on her hips."
    show reona angry
    reona.say "[hero.name]."
    show reona upset
    mike.say "Reona."
    show reona angry
    reona.say "Well, isn't there something you should be saying to me right about now?"
    show reona upset
    "I feel myself cringing inwardly as Reona puts me on the spot."
    "And for a moment I actually think about giving her the apology she wants."
    "But then the entirety of the conversation that started all of this flashes through my mind."
    "And I find my resolve strengthening, so much so that I shake my head."
    mike.say "If you're fishing for an apology, you won't get a bite from me."
    mike.say "Look, I'm sorry if what I said hurt you, Reona..."
    mike.say "But I can't change the way I feel just to please you."
    show reona surprised
    "Reona looks oddly surprised by my statement, like she wasn't expecting it."
    "And my guess is that she's used to guys giving in to her when she puts her foot down."
    "Or else that they just tell her whatever she wants to hear to her face."
    "Then they likely carry on regardless once her back is turned."
    reona.say "Huh..."
    show reona angry
    reona.say "Where do you get off acting like that, [hero.name]?"
    reona.say "Strutting around like you're better than me, like your shit don't stink!"
    show reona upset
    "Now it's my turn to look surprised, as I turn to stare at Reona."
    mike.say "Is..."
    mike.say "Is that what you think this is?"
    mike.say "That I think I'm better than you?"
    mike.say "Bloody hell, Reona!"
    show reona embarrassed
    "Reona recoils a little as I raise my voice."
    "Like she's poked the bear and now she's afraid to hear it roar."
    show reona shock
    reona.say "Well, that's what it looks like to me!"
    show reona sad
    reona.say "I say I like you, and I try to be nice to you..."
    reona.say "And you reject me, like I'm not good enough."
    reona.say "Like you think I'm...dirty, or something."
    show reona guilty
    "Reona looks down at her feet as she says this."
    "And her voice becomes quiet, like she's finding it hard to admit."
    "All in all, there's a look about her that's enough to start my heart breaking for her."
    "It also means that all of my annoyance drains away in that moment too."
    mike.say "Reona..."
    mike.say "It's not like that, not at all."
    show reona sadsmile
    "Reona looks up at me, still reluctant to meet my eye."
    show reona surprised
    reona.say "Oh yeah?"
    show reona angry
    reona.say "Then how is it, [hero.name]?"
    reona.say "You're supposed to be the smart one, right?"
    reona.say "Helping poor, dumb little me with my studies."
    reona.say "So put it in words that even I can understand, why don't you?"
    show reona upset
    "I hold my hands up in a gesture intended to calm Reona down."
    mike.say "Okay, Reona - I'll do my best."
    mike.say "You learn from experience, right?"
    mike.say "But you can also learn from example too."
    show reona pensive
    "Reona frowns, but she keeps on listening."
    mike.say "I've had a load of friends fall in love just like that."
    "I snap my fingers to emphasize my point."
    mike.say "They meet someone and there's instant chemistry."
    mike.say "Everything feels so right, they jump right into a relationship."
    mike.say "And for a while, everything seems to be fine for them."
    show reona interested
    "Reona nods."
    show reona talkative
    reona.say "That sounds great, [hero.name]…"
    reona.say "Like they're following their hearts."
    reona.say "Isn't love supposed to be like that?"
    show reona sadsmile
    mike.say "It always starts out like that, sure..."
    mike.say "But then they hit a bump in the road, something that challenges them."
    mike.say "And that's where the trouble starts, because you need more than infatuation to handle that."
    mike.say "That's when they find that they need the other person to be strong, to support them."
    mike.say "But for that you need to know someone, you need to be a friend, as well as a lover."
    mike.say "If all you have is the fact that you fancy each other, the relationship falls apart."
    mike.say "And then everyone involved ends up getting hurt."
    show reona interested
    "Reona's been listening to all that I've said."
    "And I'm amazed that she's not cut me off along the way."
    "But I can see that she's not about to admit defeat either."
    show reona annoyed
    reona.say "You make it sound so dull, [hero.name]…"
    reona.say "Like we should be taking personality tests and comparing the results!"
    show reona sadsmile
    "All I can do is shrug at Reona's comments."
    "That and stick to my guns."
    mike.say "I just think you need to build trust in a relationship, Reona..."
    mike.say "That and take the time to find someone you're emotionally compatible with."
    mike.say "If you want to have a fling, then be my guest."
    mike.say "But make sure both parties know that's what it is."
    mike.say "Otherwise someone's going to get hurt."
    show reona pensive
    "Reona crosses her arms over her chest, frowning at me again."
    "And for a moment I think she's going to make another attempt to argue her point."
    show reona normal
    "But instead she narrows her eyes and curls her lips."
    "I have no idea what's going on inside of her head right now."
    "Well, at least in terms of what conclusions she's forming."
    "But I'm sure she's thinking over everything that I've said."
    "So I decide to let the matter drop and give her some head-space."
    "Hopefully I've managed to get through to Reona this time."
    "Or at least make her understand where I'm coming from."
    "Even if she doesn't see things my way in the end."
    $ reona.flags.redemptiondelay = TemporaryFlag(True, 3)
    return

label reona_redemption_03:
    "I've been raving to Reona about just how good the local coffee shop I get my hit of caffeine from is for ages now."
    "And today I finally have the chance to take her in there with me and prove that I'm not making any of it up."
    "But the moment we walk in through the door, I start to think that I've made a mistake."
    "Because the place is heaving with people, the queue almost stretching out of the door and into the street."
    mike.say "Oh man..."
    mike.say "Of all the days this could have happened!"
    "Reona's looking down at her phone as we walk into the coffee shop."
    "So she only sees what I'm talking about when she glances up a moment later."
    show reona surprised
    reona.say "What's up, [hero.name]?"
    reona.say "Oops..."
    reona.say "This place does look kind of busy!"
    show reona normal
    "I shake my head, already seeing my plans going up in smoke."
    mike.say "It's not usually this crazy in here at this time, Reona."
    show reona happy
    reona.say "Well, at least I know you weren't making it up now."
    reona.say "This place looks every bit as popular as you said it was."
    show reona normal
    "I glance around, seeing that most of the tables are already full."
    "Even the usually unpopular seats at the window bench are all taken."
    mike.say "I'm sorry, Reona..."
    mike.say "I know that I promised you a coffee the likes of which you've never known."
    mike.say "But it doesn't look like that's going to happen now."
    show reona surprised at hshake
    "Reona wrinkles her nose at me."
    show reona talkative
    reona.say "But this is a coffee shop, [hero.name]…"
    reona.say "Can't we just get a couple to go?"
    show reona normal
    menu:
        "A takeaway coffee is fine":
            if reona.purity.max < 60:
                $ reona.purity.max = 60
            "I shrug and then nod."
            mike.say "I guess that's a decent backup plan."
            mike.say "Let's join the queue before it gets any longer."
            "Reona and I hurry to join the back of the line."
            "And while we wait for our turn, we both scan the coffee shop."
            "But there still doesn't seem to be any sign of a table coming free."
            "Even if there was, there's still more than half-a-dozen people ahead of us in the queue."
            "So every one of them technically has a better claim on a vacated table than we do."
            "Oddly the attention we're paying to the table situation seems to have an upside."
            "Which is that it feels like no time at all before we reach the front of the line."
            "The barista is working like a total machine, and we have our order quickly too."
            mike.say "Okay, Reona..."
            mike.say "Let's hit the road!"
            "Reona takes one last look around the coffee shop."
            "And then she lets out a sigh."
            show reona embarrassed
            reona.say "Hmm..."
            reona.say "It's such a shame - this place looks real nice."
            show reona normal
            "Elderly" "Excuse me..."
            "Reona and I turn around as one, locating the source of the voice."
            show mrschen at left
            show reona at right
            with fade
            "Which happens to be a rather small and elderly woman."
            "She's sitting alone at a table for four, and smiling up at us pleasantly."
            "Elderly" "I hope you don't think I'm being rude..."
            "Elderly" "But I couldn't help overhearing that you wanted to sit down."
            "My eyebrows rise as I start to tune into what she's hinting at."
            show mrschen with hpunch
            mike.say "Oh..."
            mike.say "Were you about to leave?"
            mike.say "Because we'd be really grateful for the table."
            "The elderly woman's smile doesn't change in the slightest."
            "But she shakes her head all the same."
            "Elderly" "Oh no, I still have plenty of tea left in the pot!"
            "She pats the lid of the teapot in front of her to make the point."
            "Elderly" "But you're more than welcome to join me."
            "Elderly" "If you don't mind sharing the table, that is?"
            menu:
                "That's very kind":
                    hide mrschen
                    hide reona
                    show bg maidcafe at center, blur(3), zoomAt(2, (140, 1220))
                    show reona surprised at center, zoomAt(2.5, (800, 1650))
                    show mrschen at center, zoomAt(2.5, (-320, 1650))
                    with fade
                    "I turn to Reona..."
                    show reona pensive
                    pause 0.1
                    show reona normal at stepback(1, 0, 5)
                    pause 1
                    show reona interested
                    "...and she gives me a shrug."
                    "Which I choose to take as her leaving the decision to me."
                    show bg maidcafe at center, traveling(2, 0.5, (960, 1220))
                    show reona at center, traveling(2.5, 0.5, (1800, 1650))
                    show mrschen at center, traveling(2.5, 0.5, (540, 1650))
                    pause 0.5
                    mike.say "Sure, we'll join you."
                    mike.say "I'm [hero.name]…"
                    show bg maidcafe at center, blur(0), traveling(1, 0.3, (640, 720))
                    show reona happy at center, traveling(1, 0.3, (960, 720))
                    show mrschen at center, traveling(1, 0.3, (320, 720))
                    pause 0.3
                    mike.say "And this is Reona."
                    "The elderly woman practically beams at us as we sit down."
                    "Elderly" "I'm Mrs Chen..."
                    "Mrs. Chen" "So pleased to make your acquaintance."
                    "Mrs. Chen" "Now, [hero.name]…"
                    "Mrs. Chen" "I know that you're a regular in here, as I see you all the time."
                    "Mrs. Chen" "And I have a very good memory when it comes to faces."
                    "Mrs. Chen" "But as for your pretty companion..."
                    show reona embarrassed at startle (0.05, -10)
                    show reona blush with dissolve
                    "Reona blushes as Mrs Chen compliments her."
                    "Mrs. Chen" "I can't recall ever having seen you in here before, my dear."
                    show reona talkative
                    reona.say "Oh, I've never gotten coffee here before now."
                    reona.say "[hero.name] raves about this place, so he brought me."
                    show reona normal -blush
                    "Reona's not saying anything out of the ordinary."
                    "But still Mrs Chen nods and smiles, like she's telling an enchanting tale."
                    "Mrs. Chen" "So is this a date then?"
                    "Mrs. Chen" "Or whatever you youngsters are calling them nowadays!"
                    show reona embarrassed
                    "Reona and I exchange a quick glance."
                    show reona normal
                    "And I realise that Mrs Chen is absolutely right."
                    "We are on a date right now, even if we're just getting coffee."
                    mike.say "That's right, Mrs Chen..."
                    mike.say "I know that just buying a girl coffee isn't very lavish..."
                    "Before I can finish, Mrs Chen waves away my explanation with a hand."
                    "Mrs. Chen" "Don't be silly, young man."
                    "Mrs. Chen" "You can't judge a date by the amount of money it costs."
                    "Mrs. Chen" "The important things in life don't have a price in dollars."
                    "Mrs. Chen" "Why, my late husband and I were what you'd call poor, by modern standards."
                    "Mrs. Chen" "But we were rich in what really mattered - time and love!"
                    "I'm nodding, doing the best I can to be respectful and listen to her words."
                    "I know it's a cliché, but sometimes old people really are pretty wise."
                    "But I make a point of glancing over to Reona, worried she might not feel the same way."
                    "Which is why I'm amazed to see her hanging on Mrs Chen's every word."
                    show reona shock
                    reona.say "You...you mean that your husband...passed away?"
                    mike.say "Reona - that's not a polite thing to ask!"
                    show reona guilty
                    "To my surprise, Mrs Chen chuckles and shakes her head."
                    show mrschen at stepback(0.05, 3,0)
                    pause 0.05
                    show mrschen at stepback(0.05,-3,0)
                    "Mrs. Chen" "Oh don't be silly, young man!"
                    "Mrs. Chen" "Of course she can ask me that."
                    "Mrs. Chen" "I love talking about my husband, even though he's gone now."
                    "Mrs. Chen" "And talking about a person helps them to live on in our memories."
                    show reona pensive
                    reona.say "Wow..."
                    reona.say "Sounds like you two were really in love."
                    show reona talkative
                    reona.say "Was it like, a whirlwind romance?"
                    reona.say "Did you meet one day and elope the next?"
                    show reona normal
                    "Mrs. Chen" "Now you're the one being silly, dear!"
                    "Mrs. Chen" "Whatever would we do something like that for?"
                    "Mrs. Chen" "Why, we must have been courting for almost two years before we married."
                    show reona surprised
                    reona.say "So you chose to wait?"
                    show reona interested
                    show mrschen at startle(0.05, -10)
                    "Mrs Chen nods happily."
                    "No doubt partly from he pleasant memories she's reliving in her mind right now."
                    "Mrs. Chen" "Oh yes - the waiting made it all the sweeter!"
                    "Reona and I keep on chatting with Mrs Chen until we've drunk our coffees."
                    "And then we make our apologies and get up to leave."
                    "Mrs. Chen" "Have a lovely day, the both of you."
                    "Mrs. Chen" "And be sure to say hello the next time we meet!"
                    scene bg street
                    show reona pensive
                    with fade
                    "Outside the coffee shop, I can see that Reona's looking thoughtful."
                    mike.say "Hey, Reona..."
                    mike.say "Penny for your thoughts?"
                    show reona talkative
                    reona.say "Oh..."
                    reona.say "Oh yeah..."
                    reona.say "You didn't set that up, did you?"
                    "The question catches me totally off-guard."
                    show reona normal with hpunch
                    mike.say "WHAT?!?"
                    mike.say "No, of course not - I never spoke that woman before in my life!"
                    show reona devious
                    pause 0.1
                    show reona talkative
                    reona.say "Well it just seems so convenient, what with your lectures on commitment and taking it slow."
                    reona.say "But I have to admit that she really made me think about it."
                    show reona normal
                    pause 1
                    show reona talkative
                    reona.say "Like, her husband's dead and she's on her own, you know?"
                    reona.say "On paper, that's so sad - but she's happy just to remember the dude!"
                    show reona pensive
                    "It sounds to me like Reona's processing all of this stuff for herself."
                    "And I don't want to sound like I'm trying to force any conclusions on her."
                    "So I just nod in agreement, leaving her to ponder things for herself."
                    "Hopefully that way the place she ends up will be the right one for her."
                    $ reona.love += 2
                    $ reona.purity += 5
                    $ game.active_date.score = 75
                "We'll wait":
                    "I put on what I hope is a kindly smile."
                    "But a the same time I shake my head too."
                    mike.say "That's a kind offer, mam."
                    mike.say "But we were hoping to have some private time together."
                    mike.say "No offence intended."
                    "If anything, the elderly woman's smile becomes wider still."
                    "The wrinkles on her face unable to hide the delight in her expression."
                    "Elderly" "None taken, young man."
                    "Elderly" "And might I say, you have such nice manners?"
                    "Elderly" "So much so that you remind me of my dear, departed husband!"
                    "I can already feel my cheeks starting to flush with colour."
                    "But I manage to nod and smile, even as Reona chuckles beside me."
                    "Outside the coffee shop, her laughter becomes more open."
                    scene bg street
                    show reona happy
                    with fade
                    pause 0.1
                    show reona talkative
                    reona.say "Oh wow..."
                    show reona normal at center, traveling(1.75, 1.5, (640, 1120))
                    pause 1.5
                    show reona talkative
                    reona.say "The look on your face!"
                    show reona normal
                    mike.say "Alright, Reona - laugh it up if you like."
                    mike.say "But I was just trying to be nice to a sweet old lady, that's all!"
                    show reona flirt
                    pause 1
                    show reona talkative
                    reona.say "Lighten up, [hero.name]…"
                    reona.say "I wasn't trying to be mean either."
                    reona.say "That was really nice, seeing you two being polite to each other."
                    reona.say "If you can even charm little old ladies like that, you must be a catch!"
                    $ game.active_date.score = 75
                    $ hero.cancel_event()
                    $ game.room = "street"
            $ reona.flags.redemptiondelay = TemporaryFlag(True, 3)
        "We'll come back another day":
            "I shake my head, dismissing the idea out of hand."
            mike.say "No way, Reona."
            mike.say "To really appreciate the coffee, you need to savour it."
            mike.say "And you just can't do that out of a cheap paper cup."
            mike.say "Not while you're dodging pedestrians on the sidewalk too!"
            show reona normal at startle(0.05, 5)
            "Reona shrugs and then turns on her heel."
            reona.say "If you say so."
            reona.say "Just make sure we try this again soon, okay?"
            show reona happy at startle(0.05,-10)
            pause 0.1
            hide reona with easeoutleft
            $ hero.cancel_event()
            $ hero.cancel_activity()
            $ game.room = "street"
            $ game.active_date.stay = False
    return

label reona_redemption_04:
    if reona.purity.max < 70:
        $ reona.purity.max = 70
    scene expression f"bg {game.room}"
    "I know that I'm taking a big risk in doing what I'm about to do."
    "But recent events have made me think that it might just be what's needed."
    "I'm waiting outside the front of a small, pretty humble-looking building."
    "I've sent the same location to Reona, along with a message to meet me here."
    "And that's it, the grand total of all the information that I've given her."
    "Part of me wonders if she's going to show up at all."
    "Never mind how she'll react when she finds out what this is really all about."
    "But I've started the ball rolling, and now I'm determined to see it through."
    reona.say "Ah..."
    reona.say "Hi, [hero.name]."
    "Damn it - Reona managed to walk up on me without me noticing!"
    "And I can tell from the tone of her voice that she's more than a little nervous."
    show reona embarrassed casual with easeinleft
    "So as I spin around to face her, I do the best I can to make her more comfortable."
    mike.say "Hey, Reona..."
    mike.say "Thanks for coming at such short notice."
    show reona at startle(0.05, 5)
    "Reona nods at this, but I note that she still looks awkward."
    reona.say "Yeah, well..."
    show reona talkative
    reona.say "When someone asks you to come to a mysterious rendezvous, you know?"
    reona.say "How are you going to be able to say no!"
    show reona normal
    "Now I'm the one that's starting to feel awkward and nervous."
    "But I need to focus if there's any chance of pulling this thing off."
    "So I put a smile on my face as I rub the back of my neck."
    mike.say "Yeah..."
    mike.say "About that, Reona..."
    mike.say "I'm taking a bit of a gamble here, you know?"
    mike.say "That's why I wanted to keep it secret."
    mike.say "That and so you'd have an open mind."
    "Reona looks over my shoulder at the building behind me."
    show reona pensive
    "And I feel like she's starting to realise what's going on here."
    show reona sadshock
    reona.say "This is like what, a charity place?"
    reona.say "I've driven past it a bunch of times, but I never knew what it was for sure."
    reona.say "There's always people coming and going - and some of them look really down on their luck."
    show reona pensive
    "I step to one side and turn so that we're both looking at the building."
    mike.say "Yes and no, Reona."
    mike.say "This is the local community center."
    mike.say "A place where people can come for help."
    show reona interested at startle(0.05, 5)
    "Reona nods, looking more solemn and attentive than I've seen her in a long time."
    show reona talkative
    reona.say "So they do what, exactly?"
    reona.say "Do they hand out money and stuff here?"
    show reona normal
    mike.say "No, Reona..."
    mike.say "It's more like they offer advice and counselling."
    mike.say "Like if you need someone to talk to about your problems."
    mike.say "Someone that's not going to judge you either."
    "Reona's still nodding as I explain all of this to her."
    "As though it's slowly sinking in more with each passing moment."
    show reona pensive
    "But then she turns to look at me, a serious expression on her face."
    show reona sad
    reona.say "So what?"
    reona.say "You think that's what I need?"
    show reona sadangry
    reona.say "That I'm one of those people who should be coming here?"
    menu:
        "Some of the people here really need help":
            "I can't help holding up my hands as Reona asks the question."
            "Making a gesture that shows my alarm at the very idea."
            show reona sadfrustrated with hpunch
            mike.say "WHOA!"
            mike.say "No way, Reona..."
            mike.say "The kind of people that come here are in real dire straits."
            mike.say "There's no way that you're in the same position as them."
            "I take a deep breath as I recover from the initial shock of the question."
            mike.say "No, the way I see it is that you're on journey of your own."
            mike.say "And it's more like you could see maybe a little of what you're going through in them."
        "You might find similarities with some people here":
            "I feel a little like I'm wincing as Reona poses the question."
            "Because while I don't think she's there just yet, she definitely could end up in the same place."
            mike.say "Not exactly, Reona..."
            mike.say "More like you're on a similar path, yeah?"
            mike.say "But you've realised it way, way earlier."
            mike.say "And you can use that knowledge to keep from making the same mistakes."
        "I'm kind of worried about you":
            "I grit my teeth as Reona poses the question."
            "Because I don't see any way to avoid telling her the truth."
            mike.say "Okay, Reona..."
            mike.say "Here's the thing..."
            mike.say "I don't think you're there yet."
            mike.say "But it's one of those slippery slope kind of situations."
            mike.say "But you've realised it way, way earlier."
            mike.say "And you can use that knowledge to keep from making the same mistakes."
    $ reona.love += 2
    show reona pensive
    "Luckily for me, Reona seems to take my explanation the way it was intended."
    "As she nods while I relate them to her and looks thoughtful afterwards."
    "But then she suddenly looks thoughtful and cocks her head on one side."
    reona.say "Wait a minute, [hero.name]…"
    show reona normal
    reona.say "I get all of that..."
    reona.say "But what are you doing here?"
    reona.say "I mean, like, how do you know about this place?"
    "By now I'm already walking towards the front doors."
    "And Reona's naturally following close behind me."
    mike.say "Oh, I volunteer here."
    mike.say "Not as often as I probably should."
    mike.say "And it's not like I'm a trained counsellor or anything."
    mike.say "But I like to help out where I can, you know?"
    mike.say "It makes me feel like I'm giving a little back to the community."
    show reona pensive
    "Reona's nodding as I hold the door open for us to step inside."
    "And I can see that she's looking at me in a subtly different way to before."
    "Kind of like she's surprised and impressed at the same time."
    scene bg communitycenter
    show reona normal casual at center
    show scottie b casual at blacker, right
    with fade
    "Once we're inside, I find one of the organisers in charge of the place."
    "And I introduce Reona to him, explaining why we're here."
    "Though I do all that I can to keep from making Reona look like she's the one in need of help."
    "But the people that run the community center are pretty savvy when it comes to that kind of thing."
    "And they seem to catch on to what I'm trying to do without needing it spelled out to them."
    "Once I'm sure that Reona's in safe hands, I find out what I can do to help today."
    scene bg communitycenter with fade
    "Which means that I'm soon swept up in the chaotic experience of doing this and that."
    "One moment I'm making coffee for a dozen or so people."
    "The next I'm trying to fix a laptop that's not cooperating."
    "And then it's on to the next little problem that pops up."
    "Which is how it always seems to be when I come along and help out here."
    "There's a thousand and one tiny problems getting in the way of actually helping people."
    "So the best I can do is tackle as many as I can so the counsellors can do the real work."
    show reona normal at center, zoomAt(1, (720, 720)) with easeinright
    "It's while I'm changing the toner cartridge on the photocopier that Reona reappears."
    show reona talkative
    reona.say "Hey, [hero.name]!"
    show reona normal
    mike.say "Oh..."
    mike.say "Hi, Reona - just let me handle this..."
    mike.say "There, all done!"
    "I stand up and manage to get a good look at Reona for the first time since her return."
    "And I can instantly see the thoughtful expression is still fixed on her face."
    "Whatever she's been doing and whoever she talked to, it's clearly had an effect on her."
    mike.say "Are you okay?"
    show reona at startle(0.05, 5)
    pause 0.3
    show reona guilty
    "Reona nods, but I can see that she's looking towards the door."
    "This seems like as good a time as any to leave, so I lead her in that direction."
    hide reona with easeoutleft
    show expression f"bg {game.room}" with slideawayright
    show reona happy
    "And it's only once we're outside and walking away that she finally opens up to me."
    show reona surprised
    reona.say "So that was kind of an eye-opener!"
    show reona happy
    mike.say "Yeah..."
    mike.say "There are some real messy cases that come here."
    show reona talkative
    reona.say "But I think I get why you brought me here now."
    reona.say "I can see myself in some of those girls."
    reona.say "And I realise that it's only luck that's kept me from being one of them."
    show reona happy
    "I nod as I listen to Reona recounting her conclusions."
    "This is pretty much what I hoped she'd take from the experience."
    "But it's important that she makes up her own mind on the subject."
    "Because that'll be far more impactful than me just lecturing her."
    show reona talkative
    reona.say "But it's more than that, [hero.name]..."
    show reona pensive
    reona.say "It makes me look at the things I've done in the past."
    reona.say "Things that I don't want to do again, not ever."
    show reona embarrassed
    reona.say "It makes me want to be a good person, a positive influence, you know?"
    show reona happy
    "I keep on nodding as we walk, letting Reona speak her mind."
    "And at the same time I'm relieved that this turned out how I hoped it would."
    "That it's the chance to turn a negative into a positive."
    "And that things for Reona are looking better from this point on."
    $ reona.flags.redemptiondelay = TemporaryFlag(True, 2)
    return

label reona_redemption_05:
    if reona.purity.max < 80:
        $ reona.purity.max = 80
    "The moment I lay eyes on Reona, I can tell that there's something amiss."
    "Normally she's the epitome of confidence and totally sure of herself."
    "Even now that there's a new, more contemplative side to her nature emerging."
    "She still looks like she could walk into any room and be the centre of attention."
    "But today Reona's walking with her shoulders hunched, almost staring at her feet."
    "And as she comes closer, I swear she's trying to avoid being looked at as she does so."
    mike.say "Reona..."
    mike.say "Are you okay?"
    "At the sound of my voice, Reona looks up, a startled expression on her face."
    "But I feel a sense of relief when she seems to regain her composure at seeing me."
    show reona surprised at center, hshake
    reona.say "Oh..."
    show reona sad
    reona.say "Oh, hi, [hero.name]."
    reona.say "No, I'm not okay - but I will be, in time."
    show reona pensive
    "Of course even such a measured admission fills me with concern for Reona."
    "And my first instinct is to demand that she explain just what the problem is."
    "But then I realise that would be pretty insensitive of me."
    "So I force myself to take a mental step backwards."
    "Which I hope will give her the space she needs to open up."
    mike.say "Okay, Reona..."
    mike.say "Do you want to talk about it?"
    show reona sadsmile
    "Reona takes a deep breath and then I'm relieved to see her smile."
    "She's not beaming with happiness, just showing a slight upturn in her mood."
    "But all the same, that small gesture makes me feel more hopeful."
    reona.say "You know, not too long ago, I'd have said no."
    reona.say "I'd have just bottled it all up and tried to forget about it."
    reona.say "But since I met you, I feel like I can do that - like I can talk about it."
    "Of course I'm pleased to hear Reona admit as much."
    "But I don't want to lose the thread of her current discomfort."
    "Especially not to simply wallow in the praise she's just given me."
    mike.say "So let's talk, Reona."
    mike.say "At your own speed, yeah?"
    mike.say "Tell me all about it."
    "Reona takes another deep breath, and then lets it out."
    show reona normal
    "But this time I can tell that she's getting ready to share her story."
    $ renpy.scene()
    $ renpy.show(f"bg {game.room}", at_list=[center, zoomAt(1, (640, 720))])
    show reona at center, zoomAt(1, (640, 720))
    $ renpy.show(f"bg {game.room}", at_list=[center, traveling(1.75 , 0.8, (640, 1160))])
    show reona talkative at center, traveling(1.75 , 0.8, (640, 1160))
    pause 0.8
    reona.say "Okay, so I bumped into an ex earlier today."
    reona.say "And yeah, that's not such a rare thing for me."
    reona.say "I probably have more of them than most girls!"
    reona.say "This guy was everything that I used to go for, you know?"
    reona.say "And when we were together, it was ALL about the sex."
    reona.say "Like, he would struggle to even remember my name sometimes."
    show reona annoyed
    reona.say "So he launches into the usual kind of talk..."
    reona.say "Wow, girl, you look so good!"
    reona.say "I always remember riding your ass..."
    reona.say "I still get hard just thinking about you..."
    "I hold up a hand to stop Reona's quoting the guy."
    show reona pensive
    mike.say "Yeah, Reona - I get the picture."
    show reona talkative
    reona.say "Well the thing is that once I'd have been totally fine with that."
    reona.say "In fact, I'd have been doing the same damn thing too."
    show reona upset
    reona.say "But this time it just made me feel...dirty."
    reona.say "Like this guy and me were together for a while."
    reona.say "And all he remembers from back then is the sex."
    show reona whining
    reona.say "I was just an object to him - a piece of meat!"
    show reona sadshock
    menu:
        "You're way more than that!":
            "I nod in agreement, looking Reona in the eye as I do so."
            mike.say "That guy sounds like a total jerk, Reona."
            mike.say "But you have to remember that what he said is on him."
            show reona sad
            mike.say "You might have been cool with it in the past."
            mike.say "But I've seen how much you've grown as a person recently."
            mike.say "And the way he made you feel is just a reflection of that."
            mike.say "It's because you know that you've become more than you were."
            "Reona shakes her head as she listens to my answer."
            show reona sadsmile
            reona.say "You're so different to those lousy guys, [hero.name]."
            reona.say "And it makes me wish I'd met you a whole lot sooner!"
        "My point exactly!":
            "I nod in agreement."
            mike.say "You see what I mean, Reona?"
            mike.say "This is exactly what I've been trying to tell you."
            mike.say "If you don't respect yourself, then others won't respect you either."
            show reona sad at startle(0.2, 5)
            pause 0.2
            show reona sadshock
            "Reona nods at this, listening to what I'm saying."
            show reona pensive
            "But I can see that she was maybe expecting something more from me."
            "And it's then I realise that my answer was pretty much a mini-lecture."
            mike.say "Oh..."
            mike.say "Sorry, Reona."
            mike.say "But that's not cool."
            mike.say "There's so much to you that this guy's missing."
            mike.say "But that's on him, not you."
            show reona sadsmile
        "I'll teach him respect":
            "I know that I should be comforting Reona right now."
            "But just the thought of what that guy did makes me so mad!"
            mike.say "That guy's lucky he's not here right now, Reona."
            mike.say "Because there's no way I'd let him talk to you like that!"
            show reona sad at startle(0.2, 5)
            pause 0.2
            show reona sadshock
            "Reona nods at this, but she doesn't look totally pleased."
            show reona pensive
            reona.say "That's sweet, [hero.name]..."
            reona.say "But you don't have to beat up my exes for me."
            mike.say "Oh..."
            mike.say "Sorry, Reona."
            mike.say "But that's not cool."
            mike.say "There's so much to you that this guy's missing."
            mike.say "But that's on him, not you."
            show reona sadsmile
    "Reona lets out a sigh."
    show reona talkative
    reona.say "You always do that, [hero.name]..."
    reona.say "You always ask me what I'm thinking and how I feel."
    reona.say "Like it matters to you as much as everything else does."
    "For the first time since we met up, Reona's smile begins to broaden."
    "And her whole mood starts to become more upbeat."
    show reona happy
    reona.say "I mean, don't get me wrong - you like the physical stuff too."
    reona.say "But you seem to care about how I feel about myself."
    reona.say "Guys in the past always seemed to put me down."
    reona.say "Like it made them feel better about themselves."
    show reona flirt
    reona.say "But you like me when I like myself!"
    "The way that Reona's looking at me right now is starting to make me blush."
    "So I do the best I can to wave away her compliments."
    mike.say "I just want you to realise your own worth, Reona."
    mike.say "Not for my sake, but for your's."
    show reona normal
    "Reona doesn't respond to my statement with words."
    "Instead she takes my hand, twining her fingers with mine."
    "And the gesture feels like it's worth a thousand words."
    $ reona.love += 5
    $ reona.flags.redemptiondelay = TemporaryFlag(True, 2)
    return


label reona_date_forest_male:
    if reona.purity.max < 100:
        $ reona.purity.max = 100
    show reona talkative
    reona.say "Come on, [hero.name]…"
    reona.say "What are you slowing down for now?"
    reona.say "We're never going to make it back before dark at this rate!"
    show reona normal
    mike.say "Urgh..."
    mike.say "I...I'm going as fast...as I can, Reona!"
    mike.say "Why don't you...slow down?!?"
    "I'm panting and gasping as I do the best I can to make it to the top of the hill."
    "And little by little, more of Reona comes into view as I battle towards the summit."
    "But no matter how much effort I put into it, nothing seems to impress my companion on the hike."
    show reona talkative
    reona.say "Man, you are so out of shape!"
    reona.say "I suppose we could take a quick break."
    reona.say "I don't want you collapsing on me or anything."
    show reona normal
    "I nod my head, genuinely thankful for this brief moment of mercy."
    "And I sit down on the first rock I find big enough for my butt."
    mike.say "It's okay, Reona..."
    mike.say "You don't...have to keep trying so hard!"
    "By now Reona's perched herself on a rock next to mine."
    "But even now she's only half sitting on the thing."
    "Like she's ready to leap up and keep going in the blink of an eye."
    show reona surprised at startle(0.05,-10)
    reona.say "Huh?"
    show reona embarrassed
    reona.say "What's that supposed to mean?"
    show reona normal
    mike.say "I know that hiking's not really your thing."
    mike.say "So it's not like you need to pretend you're having the best time."
    mike.say "I appreciate you coming along though, Reona - doing stuff outside your comfort zone."
    "Reona frowns a little, shaking her head."
    show reona annoyed
    reona.say "Is that really what you think?"
    show reona talkative
    reona.say "That I'm only here to impress you?"
    show reona normal
    "Now I feel like I'm the one that's been caught on the back-foot."
    "As though Reona's turned the tables on me and started to probe deeper."
    mike.say "No!"
    mike.say "Not at all."
    mike.say "Well...maybe a tiny bit."
    mike.say "But you have to admit that it wasn't your thing when we first met!"
    show reona happy
    "Reona raises an eyebrow as I begin to spill my guts."
    "Though I get the impression that last comment might have saved my ass."
    show reona normal
    reona.say "Okay, [hero.name], I'll give you that one."
    show reona talkative
    reona.say "But I feel like it kind of always was my thing."
    reona.say "The problem was that back then, I just didn't know it."
    show reona pensive
    reona.say "If that makes any kind of sense at all!"
    show reona interested
    "I'm nodding as Reona says this, because it really rings true."
    "She's been on a voyage of discovery since we first met."
    "And by that I mean self-discovery, an exploration of just who she is."
    menu:
        "Yeah of course":
            "I don't even need to think about it."
            "What Reona's saying makes total sense to me."
            mike.say "Oh, totally, Reona..."
            mike.say "I feel like you've been discovering new things the whole time I've known you."
            mike.say "And the weird thing is that I've known this new you longer than the old you!"
            show reona normal at startle(0.2, 5)
            pause 0.2
            show reona interested
            "Reona nods eagerly at this, like I've hit the nail on the head."
            reona.say "It's like you read my mind, [hero.name]."
            show reona talkative
            reona.say "And you've been helping me discover myself too."
            reona.say "Showing me that there's different way to be."
            reona.say "Encouraging me to try new things, to think in new ways."
            show reona interested
            "I really wanted this to be a conversation about Reona and her personal growth."
            "But all the same, I can't help smiling as she heaps praise onto my shoulders."
        "I think I understand":
            "I've been watching Reona examine herself closely for a while now."
            "Trying as best I can to help her out when she's needed it."
            "But that doesn't mean I'm qualified to be her therapist!"
            mike.say "Yeah, Reona..."
            mike.say "It makes sense that you're on a journey right now."
            mike.say "Maybe one on which you don't really know where you're going?"
            mike.say "Just that you have to see it through to the end, yeah?"
            show reona normal at startle(0.2, 5)
            pause 0.2
            show reona interested
            "Reona nods at this."
            "But I get the feeling that she wanted me to say more."
            show reona talkative
            reona.say "That's kind of it, [hero.name]."
            reona.say "I'm going somewhere without a map to help me."
            show reona interested
            reona.say "But I think I'll know when I get there."
        "Well...":
            "I feel like I kind of get where Reona's going with all of this stuff."
            "But at the same time I don't want to put my own stamp onto what she's going through."
            "So I do the best I can to be supportive while not totally agreeing with her."
            mike.say "Kind of, Reona..."
            mike.say "It sounds like you've been doing a lot of soul-searching."
            mike.say "Really getting to the bottom of who you really are?"
            show reona normal at startle(0.2, 5)
            pause 0.2
            show reona interested
            "Reona nods at this."
            "But I get the feeling that she wanted me to say more."
            show reona talkative
            reona.say "That's kind of it, [hero.name]."
            reona.say "But I'm not sure I've found out for sure."
            reona.say "At least not yet."
    $ reona.love += 2
    "By now I'm talking in a perfectly normal tone of voice, not gasping for breath."
    "And I'm just starting to feel like I'm regaining a little of my stamina."
    "But unfortunately, Reona seems to interpret that as me being back to full strength."
    "Because she leaps up from her rock, grabbing my hand and pulling me up with her."
    show reona happy
    pause 0.5
    show reona talkative
    reona.say "Come on, [hero.name]…"
    reona.say "Move your lazy ass!"
    show reona happy
    "There's nothing I can do so resist save for pulling in the opposite direction."
    "And as the walk should literally be downhill from here, I decide not to fight it."
    "Reona and I continue on the route of our hike, chatting about art and literature."
    "And again I'm struck by how far she's come in such a short space of time."
    "When I first bumped into her, Reona was an intellectually lazy girl."
    "Always looking for someone to do the work for her when it came to her studies."
    "And more than willing to shake her assets in order to get what she wanted too."
    "Now she's telling me what she thought of this book and that film without any prompting."
    "And she seems much happier for the changes in her character too."
    show reona zorder 2
    show scottie b naked at center, blacker, zoomAt(0.75, (1140, 720)) with easeinright
    show dwayne naked at center, blacker, zoomAt(0.85, (940, 720)) with easeinright
    show danny naked at center, blacker, zoomAt(0.75, (840, 720)) with easeinright
    pause 0.3
    show dwayne at blacker, startle(0.05, -10), zoomAt(0.85, (940, 720))
    "Some guy" "WOW!"
    show scottie at blacker, startle(0.05, -10), zoomAt(0.75, (1140, 720))
    "Other guy" "Hey, baby - where've you been all my life?"
    show danny at blacker, startle(0.05, -10), zoomAt(0.75, (840, 720))
    "Other guy" "Oh man - what a total babe!"
    "The sound of raised male voices makes both of us look round in surprise."
    "We've been so lost in nature and our conversation that it's a shock to hear another person speak."
    "Let alone suddenly being shouted at by the group of jocks I can see down by the creek up ahead."
    "My gaze goes from the cat-calling guys to Reona, remembering the things she's told me about her past."
    "From what I recall, those are exactly the kind of men she used to gravitate towards."
    "But much to my surprise, and undisguised delight, Reona rolls her eyes in disgust."
    show reona guilty
    pause 0.5
    show reona annoyed
    reona.say "Urgh..."
    show reona angry
    reona.say "What a total bunch of apes!"
    show reona normal
    "Without even looking in their direction, she strides on down the trail."
    "And I hurry to follow in her wake, all the time trying keep from smirking."
    "Because the more I learn about the new Reona, the more I seem to like her."
    show scottie at blacker, startle(0.05, -10), zoomAt(0.75, (1140, 720))
    pause 0.05
    hide scottie with easeoutright
    show dwayne at blacker, startle(0.05, -10), zoomAt(0.85, (940, 720))
    pause 0.05
    hide dwayne with easeoutright
    show danny at blacker, startle(0.05, -10), zoomAt(0.75, (840, 720))
    pause 0.05
    hide danny with easeoutright
    $ game.active_date.stay = False
    $ DONE["reona_date_forest"] = game.days_played
    $ reona.flags.redemptiondelay = TemporaryFlag(True, 2)
    $ game.pass_time(4)
    return

label reona_redemption_07:
    "I've been watching Reona's personal journey with interest ever since it became obvious she was on one."
    "And for the main part I've been more than happy to give her all the space that she's needed for that too."
    "But it's kind of ironic that one of the side-effects of it all has been the way we've kind of stalled on the physical side of things."
    "And yeah, I know how that sounds, coming from the same guy that encouraged her to change her promiscuous ways."
    "The problem is that I'm only human, you know?"
    "And Reona..."
    "Well, she's one of the hottest girls I've ever met."
    "Even with all of this wholesome stuff going on in her life right now, I still have the hots for her!"
    "And no matter how hard I try, I can't keep that from coming to the surface on occasion."
    "Like right now, for instance - we're just hanging out, all casual and innocent."
    hide reona
    show reona kiss with fade
    "But then Reona leans in to plant a kiss on my lips, taking me totally by surprise."
    "Naturally I return the gesture, leaning into the kiss for all I'm worth."
    "At the same time I can feel the natural progression of the whole thing."
    "Every passing second sees it becoming more intense in nature."
    "Soon enough there are tongues involved, and hands touching each others bodies."
    "This is the point where there's no way for me to put on the breaks."
    "No way for me to stop being a red-blooded guy that's dating a totally stunning girl."
    "I can feel myself pulling Reona ever closer, wanting to go further still."
    "And I can only guess that she's as aware of the feeling as I am."
    "That she's feeling the same thing too."
    hide reona kiss
    show reona sadsmile at center, zoomAt(1.5, (640, 1050))
    with fade
    "But that's the moment that I feel her begin to pull away from me."
    "Breaking the connection between us and bringing everything to a halt."
    "Of course I don't fight it, I just go along with what Reona seems to want in the moment."
    "And once we're apart, there's a whole lot of blushing and apologising on both sides."
    mike.say "Are..."
    mike.say "Are you okay, Reona?"
    show reona embarrassed
    reona.say "Yeah..."
    reona.say "I..."
    reona.say "I'm sorry, I just..."
    show reona guilty
    mike.say "Oh no..."
    mike.say "There's no need to apologise!"
    mike.say "I was just..."
    show reona normal blush
    "As one, Reona and I stop talking and just look each other in the eye."
    "And much to my relief, she begins to chuckle, which starts me off doing the same."
    show reona shout
    reona.say "Oh, [hero.name]…"
    reona.say "Will you listen to the two of us?"
    reona.say "This is so dumb."
    show reona normal
    mike.say "You said it, Reona..."
    mike.say "I mean, I don't want to sound like I'm desperate to jump on you or anything."
    mike.say "But sometimes I just can't help myself - I really am that crazy about you!"
    "Reona listens to what I have to say with genuine patience."
    "But I can see that she's still blushing."
    "And this time it's because of my admitting that I want her."
    "Wow...she really has changed a lot since we first met."
    "The old Reona would have just taken such a compliment in her stride."
    "Hell, she'd probably have flirted right back - raised the stakes too."
    show reona talkative
    reona.say "I get it, [hero.name], I do."
    reona.say "And I feel the same way about you."
    show reona flirt
    reona.say "The old me wouldn't have hesitated for a second!"
    show reona normal
    "Oh man - I think that was supposed to help me out."
    "But the reality is that it just makes me want to be ravished by the old Reona!"
    mike.say "But the new Reona?"
    mike.say "I'm guessing she's a different girl altogether?"
    show reona talkative
    reona.say "You could say that."
    show reona pensive
    reona.say "It's hard for me to put this stuff into words, you know?"
    reona.say "But I kind of feel like I can't indulge myself while I'm discovering the new me."
    reona.say "Or at least I can't indulge myself in that particular way..."
    show reona normal
    "There's no need for Reona to use the actual word."
    "Because what else could she be talking about but sex?"
    "And even though it makes me feel like I've been punched in the gut, I nod."
    show reona talkative
    reona.say "I hope you can understand, [hero.name]?"
    show reona whining
    reona.say "I've had to change so much and those old habits are so hard to break."
    reona.say "I feel like if I don't stop indulging myself in all the ways I used to..."
    reona.say "Well, like I'll just slip back to where I was before."
    show reona sadsmile
    reona.say "So I guess what I'm saying is that I want to wait."
    reona.say "To hold off on being intimate until we make some kind of real commitment to each other."
    show reona talkative
    reona.say "How does that sound to you, [hero.name]?"
    reona.say "Do you think that's something you could handle?"
    show reona normal
    "Reona's looking me straight in the eye as she's telling me all of this."
    "And once she's done explaining herself, she waits for me to give her an answer."
    menu:
        "That's fine, I'll wait" if reona.love >= 190:
            "Part of me wants to tell Reona that I don't think this is fair."
            "That I meant to help her get some much-needed respect for herself."
            "Not to make her turn herself into some kind of nun!"
            "But that would be a totally selfish way to react."
            "And it'd make a mockery of the bond that's grown between us."
            "Because if I really believe in what Reona's doing, the least I can do is see it through on her terms."
            mike.say "I won't lie, Reona - it sounds like it could be tough."
            mike.say "But it also sounds like this is something that you need."
            mike.say "So I'll do my very best to make sure it happens."
            "Reona looks at me in silence for a moment."
            "And the longer the silence endures, the more worried I become."
            "Worried that she's seen through me, sensed an insincerity that I didn't know was there."
            "But then she throws her arms around me and pulls me into a crazily tight hug."
            show reona happy
            reona.say "Oh, [hero.name]..."
            reona.say "You are just too good to be true!"
            reona.say "And I promise that you won't regret this."
            reona.say "Because the me you're getting is gonna be the best one ever!"
            show reona normal
            "I'm really enjoying the sensation of Reona's embrace."
            "Not to mention the glow of her affection for me."
            "But even so I can feel the familiar desires beginning to build up inside of me again."
            "So I gently ease things off, doing all that I can to abide by my promise to her."
            "Oh man, this is going to be one of the hardest things I've ever done."
            "But if I can pull it off, the potential reward is going to be epic."
            $ reona.love += 5
            $ game.active_date.score += 100
        "I've been patient enough":
            "I suddenly feel a surge of frustration well up in the middle of my chest."
            "Like all of this is coming to a head with Reona making such a demand of me."
            "And before I know it the words come tumbling out of my mouth."
            mike.say "Don't you think you're taking this whole thing a little too far, Reona?"
            show reona surprised
            "Reona looks at me in genuine surprise."
            show reona shock
            reona.say "What's that supposed to mean?"
            show reona sad
            reona.say "You know how important this journey's become to me."
            reona.say "And you were the one that started me down this path in the first place."
            show reona normal
            "I know that all of what Reona's saying is true."
            "But I'm not speaking from a logical place right now."
            "What's pouring out of me is pure emotion."
            "And none of it is rational or reasoned."
            mike.say "It just kind of feels like I'm being punished, Reona."
            mike.say "Like, you were throwing yourself at guys before I came along."
            mike.say "And sure, it's great that you've started to get some self-respect."
            mike.say "But did you have to go and turn yourself into some kind of nun?!?"
            show reona sad
            "Reona's expression is turning darker by the moment."
            "And I can see that I'm digging myself into a hole here."
            show reona angry
            reona.say "So what, [hero.name]?"
            reona.say "You're pissed that I didn't put out for you?"
            reona.say "You think that you deserve a ride because you were a nice guy?"
            show reona sad
            mike.say "No, Reona - of course not!"
            show reona shout
            reona.say "Well that's what it sounds like from where I'm standing."
            show reona normal at center, traveling (1.25, 0.3, (740, 880))
            "Reona turns on her heel and starts to walk away from me."
            mike.say "Reona..."
            mike.say "Where are you going?"
            show reona normal at center, traveling (1.0, 1.0, (940, 720))
            "Reona looks back over her shoulder, but she doesn't stop."
            show reona sadangry
            reona.say "I don't know where..."
            reona.say "Just that it has to be somewhere you're not."
            reona.say "I need some time to myself, time to think - about everything."
            hide reona with easeoutright
            "All I can do is stand there and watch as Reona storms away."
            "Hoping that I haven't gone and done irreparable damage to our relationship."
            $ reona.love -= 10
            $ reona.hide()
            $ reona.flags.temporary_hidden = TemporaryFlag(True, 7, hook=Person.find("reona").unhide)
            $ hero.cancel_activity()
            $ game.room = "street"
            $ game.active_date.stay = False
    return

label reona_jack_01:
    reona.say "Hey, [hero.name]!"
    show reona happy leftback rightopen with dissolve
    "I look up at the sound of a familiar voice and straight into Reona's smiling face."
    "She's standing right in front of me as the crowd of students part like a river around us."
    "And there's no way I can keep my own face from breaking into a smile too."
    "I can't explain it - Reona's just one of those girls who has that effect on me."
    mike.say "Oh..."
    mike.say "Hi, Reona..."
    mike.say "Are you on a break period?"
    "Reona shakes her head, and I instantly feel my mood go down as a result."
    show reona normal rightnormal
    reona.say "Sorry, [hero.name]..."
    reona.say "I'm on my way to my next lecture."
    reona.say "I was just stopping to say hi."
    mike.say "Ah, I see..."
    mike.say "Okay, Reona..."
    show reona at center, traveling(1.5, 0.25, (640, 1040))
    "Noticing the change in my mood, Reona reaches out and puts her hand atop mine."
    "The mere sensation of her touching me seems to reverse the effect on my mood."
    "And I feel suddenly uplifted once again."
    show reona happy righthold
    reona.say "Don't worry, [hero.name]..."
    reona.say "Maybe we can meet up for some lunch, yeah?"
    mike.say "Sure thing, Reona!"
    mike.say "I'll be in the refectory, okay?"
    show reona normal rightopen at center, traveling(1.0, 0.5, (640, 720))
    pause 1
    hide reona with easeoutleft
    "Reona nods and hurries away to her lecture."
    "But as I watch her go, I see someone else is doing the same thing."
    show jack sad at mostright5, dark with easeinright
    "It's Jack, standing just far enough away for Reona not to have seen him."
    "And from the look on his face, he doesn't seem pleased."
    show jack at center, traveling(1.5, 0.5, (640, 1040)), brighter with ease
    "As soon as Reona's gone, he hurries over to where I'm standing."
    mike.say "Hi, Jack..."
    "At first Jack doesn't greet me in return."
    "Instead he looks furtively over my shoulder."
    "And I realise he's staring in the direction that Reona just went."
    jack.say "Is she gone?"
    jack.say "She didn't see me, did she?"
    mike.say "Are you talking about Reona?"
    "Jack nods, still looking in the same direction."
    show jack angry
    jack.say "Of course I am!"
    mike.say "Erm..."
    mike.say "Yeah, Jack..."
    mike.say "She's gone."
    show jack sad
    "Jack's acting pretty weird, even for him."
    "So I do the best I can to ground the conversation."
    mike.say "You should have come over earlier."
    mike.say "Then I could have introduced the two of you."
    "Jack shakes his head at this, dismissing the idea."
    jack.say "No need for that..."
    jack.say "I already know her."
    mike.say "Isn't that all the more reason to come over and chat?"
    mike.say "I had no idea you two knew each other."
    mike.say "We could have made plans to study together or hang out."
    "It's only now that Jack finally looks me in the face."
    "And I can see that his expression is one of ironic amusement."
    show jack angry
    jack.say "Oh yeah, [hero.name]..."
    jack.say "Because she'd want to be seen with me!"
    show jack sad
    "Now Jack really is starting to bug me."
    "So I resolve to get more information out of him."
    mike.say "What are you talking about, Jack?"
    mike.say "I thought you said you knew Reona?"
    show jack angry
    jack.say "Sure I did."
    jack.say "But that doesn't mean she wants to hang out with me."
    show jack sad
    jack.say "..."
    jack.say "It's like this..."
    jack.say "I met Reona when we both started our courses here."
    jack.say "We both didn't know anyone, so we kind of became friends out of necessity."
    jack.say "Which was great for me, because I had the biggest crush on her back then."
    "All of that makes sense to me."
    "Jack's always falling for some girl he's met."
    "Usually one that's also way out of his league too."
    mike.say "So what changed between now and then?"
    show jack angry
    jack.say "What do you think changed?"
    jack.say "The same thing that always happens to me - she got popular!"
    jack.say "The next thing I know, she's seeing every guy that she meets."
    jack.say "And it turns out she's a massive slut too."
    show jack sad
    jack.say "Since then she won't speak to me, or even look me in the eye."
    "I raise my eyebrows and take a deep breath."
    "Then I let it out as a sigh of amazement as I shake my head."
    mike.say "Wow..."
    mike.say "That's pretty harsh."
    mike.say "Thanks for the warning, buddy."
    show jack normal
    jack.say "Any time, man!"
    hide jack with easeoutright
    "Jack hurries off to wherever he need to be next."
    "Which leaves me standing alone, thinking about what he just told me."
    "If he's to be believed, Reona used him when it suited her and then tossed him aside."
    "But on the other hand, I know that Jack can be way too sensitive about this kind of thing."
    "It's also perfectly possible that his feelings for Reona are colouring everything he said."
    "Maybe their relationship was way more casual and brief from her point of view than his."
    "Perhaps she just thought that they naturally grew apart?"
    "Whatever the truth might be, I'll try to keep both possibilities in mind."
    "Though I wouldn't be surprised to find the truth lies somewhere in the middle."
    return


label reona_jack_01a:
    if reona.purity.max < 30:
        $ reona.purity.max = 30
    "One of the things about sharing a house and having groups of friends that cross-over is unexpected dynamics."
    "Like, you never know who's going to be around whenever you have people over, so you get odd combinations hanging out together."
    "Take today for example - I have vague plans to hang out with Jack, maybe start planning a new Deities and Demigods campaign."
    play sound cell_vibrate
    play sfx1 door_knock
    "But at the very moment I hear the sound of him knocking at the door, I feel my phone vibrating in my pocket too."
    "I pull it out just as I make it into the hallway and open the front-door, noting that it's a call from Reona."
    scene bg house
    show jack at left5
    $ renpy.show_screen("smartphone_choice", "Reona", show_mc=False, accept_only=True)
    with fade
    "This means that I'm putting the thing to my ear the very same moment that I'm greeted by Jack standing on the porch."
    show jack happy
    jack.say "Hey, buddy!"
    jack.say "Here I am..."
    show jack surprised
    "Jack's words are cut off abruptly as I hold up a hand to silence him."
    show jack blank
    mike.say "Hey, Reona..."
    mike.say "What can I do for you?"
    "I'm looking straight at Jack as I wait to hear Reona's response on the other end of the line."
    "But the moment that he hears me say her name, Jack's eyes almost pop out of his head."
    show jack surprised
    jack.say "Is that Reona calling you?"
    jack.say "[hero.name], is that Reona?!?"
    show jack guilty
    "I make the 'cut-throat' gesture while staring Jack in the eye."
    reona.say "Oh..."
    reona.say "Hey, [hero.name]…"
    reona.say "Hope I didn't catch you at a bad time?"
    mike.say "No, Reona - I'm just letting someone into the house, that's all."
    mike.say "Anyway...what's up?"
    reona.say "Nothing too heavy..."
    reona.say "I was just out and about and I wondered if I could come over there?"
    reona.say "You know, like hang-out or something?"
    "I turn my gaze away from Jack for a moment, trying to concentrate on what Reona's saying."
    show jack at center, zoomAt(1.5, (440, 1090)) with fade
    "But when I turn back around, he's closed the distance between us, and is an inch from my face."
    show jack surprised
    jack.say "What's she saying?"
    jack.say "Did I just hear her ask if she can hang-out?!?"
    show jack blank
    mike.say "Aargh!"
    mike.say "Personal space, Jack, personal space!"
    show jack at center, traveling(1.75, 0.3, (440, 1240))
    "Jack doesn't seem to be listening to me, as he keeps on leaning in closer."
    reona.say "[hero.name]…"
    reona.say "Who's there with you?"
    reona.say "Is that Jack?"
    "Jack seems to take the mere mention of his name as an invitation to jump into the conversation."
    show jack at center, zoomAt(1.85, (440, 1320)) with hpunch
    "So much so that he almost tears the phone out of my hand in his eagerness to answer."
    show jack smile
    jack.say "Yeah, Reona - it's me, it's Jack!"
    jack.say "And of course you should come hang-out with us!"
    show jack normal
    reona.say "Oh..."
    reona.say "I was kinda asking, [hero.name]…"
    reona.say "But if he's cool with that..."
    show jack happy
    jack.say "Of course he is - he's nodding at me right now!"
    show jack normal
    "The reality is that I'm grimacing while looking daggers at Jack."
    "All while I'm trying to push him away and regain control of the phone."
    reona.say "Well if that's how it is - I'll be there ASAP!"
    show jack happy at center, zoomAt(1.5, (440, 1090)) with hpunch
    "Giving Jack an almighty shove, I finally manage to dislodge him from my person."
    "And then I raise the phone to my ear, hoping to catch Reona."
    mike.say "Reona?"
    mike.say "Hey, Reona?"
    $ renpy.hide_screen("smartphone_choice")
    mike.say "Fuck sake, Jack - she hung up already!"
    show jack blank
    "Jack looks at me like I'm talking absolute nonsense."
    "And he does so while casually waltzing in through the open door too."
    show jack smile at center, zoomAt(1.5, (640, 1090)) with ease
    jack.say "Why so tense, [hero.name]?"
    jack.say "She was asking to come hang-out with us."
    jack.say "I just told her it was okay."
    show jack normal
    "I stalk into the house on Jack's heels, slamming the door behind me."
    mike.say "Correction, Jack..."
    mike.say "Reona was asking if she could hang-out with ME!"
    mike.say "But you just had to go and insert yourself into the situation."
    scene bg livingroom with fade
    pause 0.2
    show jack at center, zoomAt(1.25, (540, 900)) with easeinright
    "Jack's already walked into the dining-room and put his bag down on the table."
    "Then he turns and plants his hands on his hips, shaking his head at me."
    show jack smile
    jack.say "But you'd already agreed to hang-out with me, buddy."
    jack.say "That means you'd have had to turn Reona down."
    jack.say "This way you get the best of both worlds - to hang-out with us together!"
    show jack normal
    "The sound of us talking seems to have caught the attention of my housemates."
    show jack at center, zoomAt(1.25, (440, 900))
    show bree zorder 3 at center, zoomAt(1.0, (840, 720))
    show sasha zorder 2 at center, zoomAt(1.0, (1040, 720))
    with easeinright
    "As I see Bree and Sasha appear in the doorway."
    if Harem.find(minami, name='home'):
        show minami zorder 1 at center, zoomAt(1.0, (1240, 720))
        with easeinright
        "And as if sensing the potential drama, Minami is close on their heels."
    show bree talkative
    bree.say "Aww..."
    bree.say "You're so innocent sometimes, Jack..."
    bree.say "It's kinda cute!"
    show bree normal
    "Jack was looking more than pleased to see the girls enter the room a moment ago."
    "But as soon as Bree makes her observation, a puzzled look settles on his face."
    show jack surprised
    jack.say "Huh?"
    jack.say "What are you talking about, Bree?"
    show jack blank
    show sasha shout
    sasha.say "She means that [hero.name] was going to blow you off for this Reona chick, dumbass!"
    sasha.say "But you're too naive to read the room."
    show sasha normal
    if Harem.find(minami, name='home'):
        show minami talkative
        minami.say "Yeah, Jack..."
        minami.say "[hero.name] thinks you're cock-blocking him!"
        show minami normal
    "Sasha's summing up of the situation is much more to the point."
    "But Jack still has that uncomprehending look on his face."
    "The one he always gets when he's waiting for me to reassure him of something."
    menu:
        "I'm fine":
            "I shoot what I hope is a disapproving look at the girls."
            "And then I turn to face Jack, shaking my head as I do so."
            mike.say "Ah, don't fall for that old trick, Jack..."
            mike.say "They're just trying to fuck with you, that's all."
            mike.say "Of course I'm okay with Reona joining us."
            show jack normal
            "Jack's expression changes almost the same moment I start to reassure him."
            "His confidence growing as he starts feeling like we're both on the same page."
            "He turns to point at the girls, gesturing to each of them in turn."
            show jack smile
            jack.say "Nice try, guys."
            jack.say "But you'll have to do better if you want to fool me!"
        "They're right you know":
            "I can't help shrugging and shaking my head at Jack."
            mike.say "Given the choice, I might have preferred to spend some time alone with Reona."
            mike.say "But it looks like you made that decision for me, Jack."
            show jack sad
            "Jack's face falls visibly as I make it plain to him."
            "And he can't help looking down at his feet, rather than at me."
            show jack whining
            jack.say "Oh..."
            jack.say "Sorry, buddy!"
            show jack sad
            "Oh man, he's doing that thing again."
            "Where he looks like a puppy someone just kicked up the butt!"
            mike.say "It's okay, man..."
            mike.say "What's done is done."
            $ reona.love += 2
        "I miss old times, just the two of us playing":
            "I can't help shrugging and shaking my head at Jack."
            mike.say "Given the choice, I might have preferred to have some quality time with my buddy."
            mike.say "But it looks like you made that decision for me, Jack."
            show jack sad
            "Jack's face falls visibly as I make it plain to him."
            "And he can't help looking down at his feet, rather than at me."
            show jack whining
            jack.say "Oh..."
            jack.say "Sorry, buddy!"
            show jack sad
            "Oh man, he's doing that thing again."
            "Where he looks like a puppy someone just kicked up the butt!"
            mike.say "It's okay, man..."
            mike.say "What's done is done."
            $ reona.sub += 1
    "Luckily for me, the girls seem to be more on the ball than Jack."
    "And they step in to smooth things over, before I really get pissed with him."
    scene bg livingroom
    show rpg livingroom nomc
    if Harem.find(minami, name='home'):
        show rpg minami
    with fade
    "As Jack's pulling the rulebooks out of his bag, they descend on him like a swarm of locusts."
    bree.say "Ooh..."
    bree.say "Is that the new set of core books for Deities and Demigods?"
    "Bree snatches the player's guidebook out of Jack's hands."
    "And before he can do anything about it, she begins sniffing it and letting out sighs of pleasure."
    bree.say "Mmm..."
    bree.say "Don't you just love that new book smell?"
    jack.say "Be...be careful with that, Bree!"
    jack.say "I haven't had a chance to handle it much myself."
    "But while Jack's attention is all on Bree, Sasha's already taken advantage."
    sasha.say "Whoa..."
    sasha.say "Cool demons!"
    "Jack turns his gaze away from Bree just in time to see Sasha scoop up the monster compendium."
    "She has it open and is thumbing through the glossy pages in the blink of an eye."
    "And I just know that to Jack, it must look like she's deliberately trying to smudge the fresh ink."
    jack.say "[hero.name]..."
    jack.say "Help me!"
    play sound door_knock
    "As if fate's doing all it can to punish Jack, the very next moment I hear a knock at the door."
    mike.say "Sorry, buddy..."
    mike.say "But I'm guessing that's Reona at the door."
    mike.say "Don't worry, I'll be right back."
    scene bg livingroom with fade
    "Trying not to let the smile on my face show, I turn my back on the scene."
    "Leaving Jack to struggle as he tries to protect his precious rulebooks."
    "I pretty much dash to the front-door once I'm in the hall and out of sight."
    "My mind racing to figure out how I'm going to sell this to Reona."
    "Because for all I know, she's never even heard of Demons and Demigods."
    scene bg black with dissolve
    pause 0.1
    scene bg house
    show reona at center, zoomAt(1.25, (640, 880))
    with wiperight
    "Opening the door, I'm greeted by the sight of her standing on the porch."
    show reona talkative
    reona.say "Hey, [hero.name]..."
    reona.say "I know that you kind of said this was okay on the phone."
    reona.say "But then your buddy was being so loud and talking over you."
    reona.say "Are you sure you're cool with me being here too?"
    hide reona with easeoutleft
    "I do the best I can to look nonchalant as Reona steps through the door."
    "Shrugging as I close it behind her, like it's nothing at all."
    scene bg livingroom with fade
    pause 0.2
    show reona at center, zoomAt(1.25, (640, 880)) with easeinright
    mike.say "Nah, it's fine, Reona..."
    mike.say "I'm sure we can make it work."
    mike.say "But you should probably know that we're doing roleplaying stuff today."
    mike.say "And it looks like my housemates are hanging around too."
    show reona interested
    "Reona's eyebrows shoot up her forehead as she hears what I'm saying."
    show reona surprised
    reona.say "Really?!?"
    reona.say "You sound pretty casual about that, [hero.name]."
    reona.say "Especially seeing as how you're doing it with another guy!"
    reona.say "Not to mention in front of your housemates - that's pretty wild."
    show reona normal
    "I look at Reona in obvious confusion for a moment, not sure what she means."
    "But then I slap myself on the forehead as realisation dawns on me."
    "My brain's still in 'Jack Mode', and I haven't switched it over to 'Reona Mode'."
    "So roleplaying means something very different to the two of us right now."
    "I pause with my hand on the dining-room door, waving the other in the air."
    mike.say "No, no, no..."
    mike.say "You're thinking I mean roleplaying, like, in the kinky sense."
    mike.say "When I mean roleplaying in the dragons and halflings sense."
    show reona interested
    "Reona's eyes go wide as she realises what I mean."
    show reona happy
    "And she nods to let me know we're finally on the same page."
    "But I note that she's giggling as we walk into the room."
    scene bg livingroom
    show reona normal at center, zoomAt(1.0, (1100, 720))
    show jack at center, zoomAt(1.0, (200, 760))
    if Harem.find(minami, name='home'):
        show minami normal at center, zoomAt(1.0, (880, 720))
    show sasha at center, zoomAt(1.0, (500, 720))
    show bree at center, zoomAt(1.0, (700, 720))
    with fade
    "As soon as we're in there, Jack's head pops up."
    "I swear it's almost like he can smell Reona even before he sees her."
    show jack happy
    jack.say "Hey, Reona!"
    show jack smile
    jack.say "It's so good to see you, yeah?"
    jack.say "So cool you wanted to some and hang-out with me!"
    show jack lying
    jack.say "I...I mean with us - hang-out with all of us!"
    show jack smile
    jack.say "This is Bree."
    jack.say "This is Sasha."
    show jack normal
    if Harem.find(minami, name='home'):
        jack.say "And this is Minami, [hero.name]'s kid sister."
        show jack normal
        show minami talkative
        minami.say "Hey - who are you calling a kid?!?"
        show minami normal
    show jack normal
    show reona rightopen happy
    "Reona gives Jack a wave and a smile as she walks over to look at the Demons and Demigods books."
    "And at the same time I can see the other girls looking at her, sizing her up like all women do to each other."
    show bree talkative
    bree.say "So that's why Jack was so eager to get her over here!"
    show bree normal
    show sasha shout
    sasha.say "Yeah, you nerdy guys are so fucking transparent."
    show sasha normal
    if Harem.find(minami, name='home'):
        show minami talkative
        minami.say "Hey, you two - don't be so mean!"
        minami.say "Like you never had a crush on someone special."
        show minami normal
    "I shrug as I walk past the other girls."
    "I totally get where they're coming from."
    "But I guess I have to play host today, so that means being fair to everyone."
    mike.say "Look, just be as nice as you can manage, okay?"
    mike.say "Reona's not been exposed to this kind of stuff that much in the past."
    mike.say "So she probably won't want to involved in rolling up characters and all that."
    "But once I make it to the table, I see that Reona's already sat down."
    "And that Jack's placed a blank character sheet in front of her."
    show reona talkative
    reona.say "You're really not kidding me, Jack?"
    reona.say "All we need to play is a pencil and some paper?!?"
    reona.say "Don't you need like, VR headsets and all that stuff to play games these days?"
    show reona normal
    "Jack's rubbing the back of his head and chuckling at all of this."
    "Like one of those awkward, nerdy guys in an anime that's talking to their cute crush."
    "Hell, I wouldn't be surprised if he got a nosebleed any time soon."
    show jack smile
    jack.say "Well, you do need dice - lots and lots of dice!"
    show jack normal
    "Jack makes his point by pouring out the contents of his dice-bag."


    "A myriad of six, eight, ten and twenty-sided dice cascade onto the table in front of Reona."
    "They're cast in various colours of resin and eye-catching effects."
    "And I can't help noticing that Reona looks a little dazzled by the sight of them."
    show reona surprised
    reona.say "Ooh..."
    reona.say "So pretty..."
    reona.say "Like precious jewels!"
    show reona normal
    mike.say "Demons and Demigods is a game where everyone plays a character, Reona."
    mike.say "And one person is the Gamesmaster, who runs everything else."
    "Reona looks thoughtful for a moment, then nods."
    show reona talkative
    reona.say "So it's like a play, yeah?"
    reona.say "We're the actors and this...this Gamesmaster is the director?"
    show reona normal
    "I can't help blinking in surprise as Reona gets it straight away."
    mike.say "That's pretty much it, Reona."
    mike.say "Only there's no script, so we're all improvising."
    "Reona's nodding as she looks up from the book in front of her."
    "Then she gestures to everyone else in the room."
    show reona talkative
    reona.say "And you all play this game?"
    reona.say "Like, the girls as well as the guys?"
    show reona normal
    show bree talkative
    bree.say "Oh yeah, totally, Reona."
    bree.say "Like, it used to be a guy nerd thing."
    show bree normal
    show sasha shout
    sasha.say "But loads of girls play it now."
    sasha.say "And not all of them are nerds like Bree here!"
    show sasha normal
    show bree vangry at startle
    bree.say "SASHA!"
    show bree angry
    show sasha shout
    sasha.say "What's the problem, Bree - you are a nerd!"
    show sasha normal
    "As Bree and Sasha start to squabble, I see my chance."
    "I nip in and sit down next to Reona while everyone else is distracted."
    mike.say "You sound pretty interested in the game, Reona."
    mike.say "I don't suppose that...well, you'd want to get involved?"
    "Reona surprises me by nodding without a moment's hesitation."
    show reona talkative
    reona.say "You know what, [hero.name] - I think I'd like to try it out."
    reona.say "I don't know if I totally get it yet."
    reona.say "But I know you and Jack, and your friends seem cool too."
    reona.say "So why the hell not?"
    show reona normal
    "I feel an unexpected rush of excitement as Reona agrees to join the campaign we're planning."
    "And for all that I've been trying to keep a level head, I can feel myself beginning to emulate Jack."
    "That is until the real Jack overhears what Reona just said."
    show jack happy
    jack.say "Are you frikin serious, Reona?!?"
    jack.say "Of course you can join the game."
    jack.say "What class do you want to play?"
    show jack normal
    "Reona looks at me with confusion on her face."
    show reona annoyed
    reona.say "Class?"
    reona.say "Are we going to be at school in the game?"
    show reona normal
    mike.say "No, no, no..."
    mike.say "Class is just a word for what your character does in the game."
    mike.say "Like their job, yeah?"
    show reona talkative
    reona.say "Oh, I see!"
    reona.say "But you don't have to like, work in a cafe, right?"
    reona.say "Because that's be pretty dumb, wouldn't it?"
    show reona normal
    mike.say "Of course not, Reona..."
    mike.say "You play as a hero in the game."
    show bree talkative
    bree.say "This time I want to be an elf priestess or a ranger!"
    show bree normal
    show sasha shout
    sasha.say "You'd better let me be an assassin in this game."
    sasha.say "You guys promised me I could the next one we played!"
    show sasha normal
    if Harem.find(minami, name='home'):
        show minami talkative
        minami.say "Can I be a rogue?"
        minami.say "But like, not a ninja - because that's SO obvious!"
        show minami normal
    "Reona seems to become thoughtful for a moment."
    "Like she's trying to remember something."
    show reona talkative
    reona.say "Hmm..."
    reona.say "I always liked those stories with the princesses and the knights when I was a little girl."
    reona.say "So maybe I could be something like that?"
    show reona normal
    "Jack can't seem to help himself as soon as he hears Reona's question."
    "He lets out a guffaw that makes him sound weirdly like a donkey."
    show jack worried
    jack.say "Hurgh..."
    jack.say "Fnarr, fnarr!"
    show jack whining
    jack.say "There's no princess class, Reona!"
    jack.say "And noble is an NPC only class too."
    show jack sadsmile
    "Reona frowns and narrows her eyes at Jack, clearly annoyed with what he just said."
    show reona angry
    reona.say "I didn't want to play some dumb princess, Jack..."
    reona.say "I wanted to play a knight!"
    show reona normal
    "Reona turns to me as she says this, as if looking for reassurance."
    show reona talkative
    reona.say "I can do that, right?"
    reona.say "A girl can be a knight?"
    show reona normal
    mike.say "You can be almost anything you like, Reona."
    mike.say "So you'd probably want to be a warrior..."
    mike.say "Or maybe a paladin?"
    show reona annoyed
    reona.say "Huh?"
    reona.say "What's the difference?"
    show reona normal
    mike.say "Well, a fighter is someone that does just that - they fight."
    mike.say "But they can be anything from a swashbuckler with a rapier to a massive guy with a sword the size of a surfboard."
    mike.say "A paladin's more like a knight, in fact, like a holy warrior in shining plate-armour."
    show reona happy
    reona.say "Then that's what I want to be - a female paladin!"
    show reona normal
    "Jack and I exchange a meaningful glance."
    "Both of us seemingly surprised at Reona."
    "Not just that she's getting into the idea of the game."
    "But also her choice of character too."
    "Back when I met her, a paladin was the last thing I'd have expected her to choose."
    "Jack and I begin to talk Reona through the rules and generating her character."
    "We take it slowly, but she still seems to get it without too much trouble."
    "The other girls chime in at various points, offering advice or asking questions of their own."
    "And just like that we're laying the foundations for a new game of Demons and Demigods."
    "Not just that, one that will be Reona's first venture into the wonderful world of table-top roleplaying games."
    "I don't think I've felt this excited about a game in years - maybe even since my own first time."
    "I just hope that everything goes well once we get started, and that Reona has a great time too."
    $ reona.flags.campaign_delay = TemporaryFlag(True, 2)
    return

label reona_jack_02a:
    show bg livingroom at center, blur(3), zoomAt(1.4, (640, 1020))
    show reona at center, zoomAt(2.2, (1740, 1620))
    show jack happy at center, zoomAt(2.2, (640, 1320))
    with fade
    "I'm beginning to change my mind about the whole business with Jack inviting Reona in on our Demons and Demigods game."
    "Back when it happened I was still kind of pissed at him for doing so without my permission."
    "Which meant I couldn't both have fun with my roleplaying buddies and then enjoy having Reona all to myself as well."
    "But what really changed my mind on the subject was seeing how she started to get into the idea."
    "I have to admit that I assumed Reona would be totally turned-off by the idea of a table-top roleplaying game."
    "Or even worse that she'd want to play, but then not really be able to grasp the rules and mechanics."
    "But so far she's proved me wrong on both counts, throwing herself into it and quickly picking up the basics."
    "And needless to say, both Jack and I are curious to see where this thing goes."
    "Which is why we've arranged to meet up with Reona today, along with a pile of Demons and Demigods rulebooks."
    "So we can finalise the details of her character and make sure everything is ready to start the campaign."
    menu:
        "Let's dive in the rulebooks":
            pass
        "Report the character development":
            $ hero.cancel_event()
            return
    if reona.purity.max < 50:
        $ reona.purity.max = 50
    reona.say "Greetings, fellow adventurers..."
    reona.say "How doth this fine morrow find you?"
    show jack whining
    "Jack and I exchange a puzzled glance."
    show jack worried
    "Then we look around as one."
    show bg livingroom at center, blur(0), traveling(1, 0.3, (640, 720))
    show reona guilty leftback righthold at center, traveling(1, 0.3, (960, 720))
    show jack at center, traveling(1, 0.3, (320, 720))
    pause 0.3
    "And I'm even more surprised when I see Reona standing behind us."
    show reona normal
    show jack blank
    mike.say "Reona?"
    mike.say "Are you feeling okay?"
    show jack worried
    jack.say "Yeah, Reona..."
    show reona guilty
    jack.say "You didn't hit your head on the way over here, or anything like that?"
    show jack blank
    show reona sadfrustrated
    "Reona frowns as she sits down at the table with us."
    show reona annoyed
    reona.say "What the hell are you two twerps talking about?!?"
    reona.say "I'm just trying to get into character, yeah?"
    show reona normal
    "My eyes meet Jack's as realisation dawns on us at the same moment."
    mike.say "Oh..."
    mike.say "I see what you mean, Reona."
    show jack smile
    jack.say "Oh yeah..."
    jack.say "That was totally convincing, Reona..."
    jack.say "I completely bought that you were a heroic paladin!"
    show jack worried
    show jack blank
    "I shoot a frown and an annoyed glance at Jack as saves himself and throws me under the bus in the act."
    "But as usual, he's too busy mooning at Reona to even notice the disapproval on my face."
    show reona happy
    pause 0.2
    show reona talkative
    reona.say "Thank you, Jack..."
    show reona leftpeace
    reona.say "At least someone appreciates the effort I'm putting in!"
    show reona leftback rightnormal
    reona.say "Seriously though, I've been binging fantasy films and TV series ever since we last met up."
    reona.say "Totally losing myself in them so that I can win when we play the game."
    show reona normal
    show jack surprised
    "I feel myself prickle a little as Reona mentions winning."
    "Because as anyone that plays Demons and Demigods knows, it's not that type of game."
    menu:
        "This game is not about winning":
            show jack annoyed
            mike.say "It's not exactly that type of game, Reona."
            "Reona looks more than a little puzzled at that statement."
            show reona surprised
            reona.say "Wha...what do you mean?"
            reona.say "Isn't this a game?"
            reona.say "All the games I played before, the idea was to win."
            show reona normal
            show jack smile
            "It looks like Jack's about to say something."
            "But as Reona's looking straight at me, she doesn't notice."
            show jack embarrassed
            "Sure, I feel a little guilty keeping Jack from saying his piece."
            "But I don't want to lose the chance to endear myself to Reona a little more."
            mike.say "This game is a little different to those, Reona."
            mike.say "In this one you work together with the other players, as a team."
            mike.say "You win by helping each other complete the quest."
            mike.say "That and playing your character well."
            show reona rightok at startle(0.2, 5)
            pause 0.2
            show reona rightnormal
            "Reona nods, like she's understanding my explanation."
            $ reona.love += 2
        "It's like you're not even trying!":
            mike.say "You'd better forget about winning before you get started, Reona!"
            show jack annoyed
            show reona sadshock
            "As soon as the words are out of my mouth, I regret them and the tone I used."
            "Because Reona looks at me as though I just cursed her out."
            show reona surprised
            reona.say "Wha...what do you mean?"
            reona.say "Isn't this a game?"
            reona.say "All the games I played before, the idea was to win."
            show reona sadshock
            "Jack cuts in before I can say another word."
            "And he makes sure to give me a disapproving look as he does so."
            show jack smile
            show reona guilty
            jack.say "He means it's not exactly that kind of game, Reona."
            jack.say "In this one you work together with the other players, as a team."
            jack.say "You win by helping each other complete the quest."
            jack.say "That and playing your character well."
            show jack blank
            show reona rightok at startle(0.2, 5)
            pause 0.2
            show reona rightnormal
            "Reona nods, like she's understanding Jack's explanation."
            "And I feel like kicking myself for not being more sensitive to a rookie player's needs."
            $ reona.sub += 1
        "...":
            "I decide to keep my mouth shut, not wanting to put Reona off by correcting her."
            "But it seems that Jack's not feeling the same about the situation."
            show jack annoyed
            pause 0.2
            show jack smile
            jack.say "You'd better forget about winning before you get started, Reona!"
            show jack blank
            "Reona looks more than a little stung by Jack's words."
            show reona surprised
            show jack annoyed
            reona.say "Wha...what do you mean?"
            reona.say "Isn't this a game?"
            reona.say "All the games I played before, the idea was to win."
            show reona normal
            show jack smile
            "I feel the need to step in before Jack puts his foot in it again."
            mike.say "He means it's not exactly that kind of game, Reona."
            mike.say "In this one you work together with the other players, as a team."
            mike.say "You win by helping each other complete the quest."
            mike.say "That and playing your character well."
            show reona rightok at startle(0.2, 5)
            pause 0.2
            show reona rightnormal
            "Reona nods, like she's understanding my explanation."
            "And I notice that Jack looks like he's kicking himself for not being more sensitive to a rookie player's needs."
    show reona interested
    reona.say "Oh yeah..."
    reona.say "I remember you saying it was more like a play!"
    reona.say "So that makes sense, I guess."
    show reona normal
    "Jack nods as he pulls out the character sheet Reona filled in last time."
    "And then he slides it in front of her, making sure she sees him do do."
    show jack smile
    jack.say "You remember this, Reona?"
    show jack blank
    show reona talkative
    reona.say "Sure I do."
    reona.say "But I thought we were done making my character."
    reona.say "Didn't we roll a bunch of those weird-looking dice?"
    reona.say "And we filled all of the boxes on the character sheet already."
    show reona normal
    "Sensing a chance to explain another aspect of the game to Reona, I lean in closer."
    mike.say "We did, Reona..."
    mike.say "But those are all the numbers behind your character."
    mike.say "They're like her vital statistics, yeah?"
    mike.say "What we're doing today is putting some skin on the bones."
    mike.say "Creating your character's back-story."
    mike.say "Working out who she is and where she comes from."
    show reona pensive
    "Reona looks thoughtful."
    show reona talkative
    reona.say "Is that important?"
    reona.say "Like, it's not going to help me killing stuff, is it?"
    show reona normal
    mike.say "No, but remember what we said about the play."
    mike.say "Imagine if a character in one of those didn't have a back-story."
    show reona interested
    "Reona nods as she absorbs what I'm saying."
    show reona talkative
    reona.say "I see..."
    reona.say "Like, the hero's not as cool if he's just a dummy with a sword?"
    reona.say "Hmm..."
    show reona normal
    pause 0.3
    show reona talkative
    reona.say "So why would my character want to be a paladin?"
    show reona normal
    "Jack chimes up, doing the best he can to help."
    show jack smile
    jack.say "Maybe she's got a good heart, Reona?"
    jack.say "Or she was raised by nuns that worship a benevolent god?"
    show jack blank
    "I watch with growing interest as Reona screws up her face at Jack's suggestions."
    "I mean, they're not bad for a start - but they are pretty basic."
    "And they're definitely vanilla in nature too!"
    "Thinking I could probably do better in my sleep, I open my mouth to offer an alternative."
    "But to my surprise, Reona beats me to it."
    show reona pensive
    reona.say "Hmm..."
    show reona talkative
    reona.say "I don't think my character was always good and pure."
    reona.say "Because if she was, why'd she ever become a paladin?"
    show jack annoyed
    reona.say "People only do that for a reason, like they're making up for something they did in the past."
    reona.say "So maybe my character was was bad, and then something happened to her that made her change?"
    show reona normal
    show jack wink at startle(0.2, 5)
    pause 0.2
    show jack smile
    "Jack's nodding his head eagerly as Reona says all of this."
    "Encouraging her to say more because it really is good stuff."
    "But I'm just left there staring at Reona in amazement."
    "As I realise that she's kind of inventing a fantasy version of herself."
    "Sure, it's not an exact match, as the real Reona isn't turning into a religious zealot."
    "But is is eerily reminiscent of the path that she's been on since she and I first met."
    show jack happy
    jack.say "That's great, Reona..."
    jack.say "The bad girl turned good trope is always gonna sell!"
    show jack blank
    show reona interested
    reona.say "What do you think, [hero.name]?"
    show reona normal
    "I blink in surprise as I realise that Reona's looking straight at me."
    "Almost like she's more interested in hearing my take on it than Jack's gushing praise."
    mike.say "I think you're onto something, Reona."
    mike.say "You've clearly thought about it and chosen something that speaks to you."
    mike.say "And I like it on a personal level too."
    mike.say "I like the idea that a person can change..."
    mike.say "That they can atone and bring out the goodness hidden inside of them."
    show reona happy
    "Reona smiles as I say all of this, letting me know that she approves."
    "And I also flatter myself by thinking that we're communicating on a different level too."
    "That she's aware of the fact I know that character is so close to the girl who's creating it too."
    show reona normal
    "The thought remains lodged in my head as we start to jot down notes for Reona's character."
    "And it doesn't disappear, even when we get down to the really intricate details later either."
    $ reona.flags.campaign_delay = TemporaryFlag(True, 2)
    return

label reona_jack_03a:
    if reona.purity.max < 70:
        $ reona.purity.max = 70
    scene bg livingroom with fade
    "The day has finally come when we're supposed to be starting the new Demons and Demigods campaign."
    "I've got the table all set up with the dice, paper and pens that we'll need - not to mention all the sourcebooks!"
    "And the rest of the space on the tabletop is almost totally taken up with snacks and bottles of water."
    "Because when you're as serious as we are about roleplaying, things tend to get very intense and take a lot of time."
    "So you have to be every bit as serious about feeding and hydration as you do about the game itself!"
    "Jack's the first person to turn up, as befitting the station of games master."
    "And once I show him into the room, he plants his hands on his hips."
    "I watch as he scans the table, sizing up what is to be his temporary domain."
    show jack casual smile with dissolve
    jack.say "Very good, very good..."
    jack.say "You have done well, my loyal minion!"
    show jack blank
    "I shoot Jack a disapproving look."
    mike.say "The praise is welcome, Jack - the corny title is most definitely not."
    mike.say "I am not, nor will I ever be, your minion!"
    "Jack waves away my objections as he scuttles over to the chair at the head of the table."
    "He pulls it out and deposits his bag on the floor beside him, pulling out his stuff."
    "As he piles up his notes, annotated rulebooks and a ton of dice, she lets out a sigh."
    show jack smile
    jack.say "Ah..."
    jack.say "There's nothing like the feeling of starting a new campaign."
    jack.say "Makes me wish I still had my special games master's hat."
    jack.say "Makes me wish SOMEONE hadn't thrown it onto the barbeque!"
    show jack blank
    "I roll my eyes as Jack throws the accusation at me."
    with hpunch
    mike.say "Not this again, Jack?"
    mike.say "It was a crappy wizard's hat you bought for a couple of bucks."
    mike.say "And you wrote 'kiss the GM for plus one to your saving throws' on it in marker-pen!"
    mike.say "What I did to that thing was an act of mercy."
    show jack whining
    "Jack opens his mouth to protest."
    play sound door_banging
    "But not for the first time, the sound of Reona knocking at the door saves me."
    show jack sad
    mike.say "Oops..."
    mike.say "That'll be Reona, so hold that thought."
    mike.say "Actually don't - toss that onto the fire too!"
    "Leaving Jack to splutter and gasp in protest, I hurry into the hallway."
    "And I manage to make it just in time, before Reona knocks a second time."
    "I know this because the door opens on her with a balled fist raised in the air."
    play sound door_open
    pause 0.2
    scene bg black with fade
    scene bg house with wiperight
    show reona casual surprised righthold
    reona.say "Oh..."
    show reona talkative rightpeace leftback
    reona.say "Hi, [hero.name]…"
    reona.say "I hope I'm not late?"
    show reona normal -rightpeace
    "I smile and shake my head, genuinely happy to see Reona."
    mike.say "Hey, Reona..."
    mike.say "No worries about the timing."
    mike.say "We're pretty casual about that when it comes to roleplaying."
    show reona happy
    mike.say "Well...at least I am - Jack can be a bit of an old woman!"
    show reona normal at startle(0.2, 5)
    "Reona nods as she steps into the hallway and I close the door behind us."
    show reona at traveling(3, 1.5, (640, 1720))
    pause 1
    show reona at blacker, zoomAt(3, (640, 1720)) with dissolve
    pause 0.3
    scene bg livingroom with fade
    play sound door_close
    queue sound door_lock
    show reona casual talkative
    reona.say "Are the others already here?"
    reona.say "It'd be hard for them to be late."
    reona.say "You know, because they live here too?"
    show reona normal
    mike.say "Oh no, it's just the three of us today, Reona."
    mike.say "Jack thought it'd be better if we eased you into it."
    mike.say "Kind of taster session with another experienced player."
    mike.say "Before we throw you in with the rest of the group, yeah?"
    show reona normal at startle(0.2, 5)
    "Reona's listening to every word I'm saying and nodding along."
    show reona talkative
    reona.say "So who's the experienced player?"
    show reona normal
    mike.say "Me, of course!"
    show reona embarrassed
    "Reona looks a little flustered as I answer the question."
    "And I suddenly remember that this is her first time playing the game."
    "So maybe I should be assuming less and explaining more."
    mike.say "Don't worry, Reona - you're in good hands."
    show reona talkative
    reona.say "Okay, okay..."
    reona.say "Just go easy on me!"
    show reona flirt
    "I can almost feel the irony hanging in the air as Reona makes the request."
    "Because as soon as she walks into the dining-room, Jack leaps out of his chair."
    "He's up and waving his arms in the air, a mock-serious look on his normally goofy face."
    show jack smile at left with easeinleft
    show reona guilty at right with ease
    jack.say "Welcome, weary traveller, to the world of ADVENTURE!"
    jack.say "Are you prepared for your journey into realms of magic and wonder?"
    show jack embarrassed
    "Reona takes a step backwards and shoots me a sideways glance."
    show reona whining
    reona.say "What...the...fuck?"
    mike.say "Just say yes, Reona..."
    show reona normal
    mike.say "Trust me, it's quicker that way."
    show reona talkative
    reona.say "If you say so..."
    show reona guilty
    "She turns her attention back to Jack, who's still capering in front of us."
    show reona talkative
    reona.say "Yeah, I guess so."
    show reona normal
    show jack smile
    jack.say "Excellent, excellent..."
    jack.say "I will be your guide on this journey, your portal into another world!"
    scene rpg
    show rpg nomc nosasha nobree
    show reona guilty leftback at center, zoomAt(1, (980, 820))
    show rpg_table_livingroom
    with fade
    "With an overly dramatic gesture, Jack shows Reona to her seat."
    "At the same time I pull out a chair close by, so that I can offer support."
    "And once we're seated, Jack finally seems satisfied and returns to his own chair."
    scene bg black
    show rpg_village_map at center, zoomAt(1, (640, 720))
    show rpg_village_map at center, traveling(3, 5, (640, 1220))
    jack.say "Okay, here we go..."
    show rpg_village_night with timelaps
    jack.say "Night has fallen over the small village of Trick Hollow."
    jack.say "And all of the souls living there have flocked to the inn for ale and good company."
    show rpg_bg_tavern with wiperight
    jack.say "But what is this?"
    jack.say "The place is alight with gossip, as they find there are two strangers in their midst."
    jack.say "One of them is a noble paladin, clad in shining plate-armour."
    $ renpy.music.set_pan(1, 0, "sound")
    pause 0.1
    $ renpy.music.set_pan(0, 0.3, "sound")
    play sound woosh_punch
    show reona rpg at right5 with easeinright
    pause 0.3
    show reona happy
    pause 0.2
    show reona normal
    "Jack makes a point of nodding to Reona as he introduces her character."
    jack.say "And the other is a heavily armored cleric, almost radiating an aura of calm wisdom."
    $ renpy.music.set_pan(-1, 0, "sound")
    pause 0.1
    $ renpy.music.set_pan(0, 0.3, "sound")
    play sound woosh_punch
    show mike rpg at left5 with easeinleft
    "Now Jack cocks his head in my direction for the same purpose."
    "And just like that, we're into the first scene of the game."
    "Obviously Reona's nervous and hesitant to speak up."
    "But this is where I really do have to give Jack his flowers."
    "Because for all of his over the top mannerisms, he really is a pretty good games-master."
    "And he uses all of those skills to immerse Reona in the scene that we're creating."
    "Plus his willingness to play the fool means she's soon put at ease."
    jack.say "You look up to see the serving wench placing another round of foaming ales on your table."
    show reona talkative
    reona.say "What's she doing that for?"
    reona.say "Did we already pay for them?"
    jack.say "The wench frowns and shakes her head."
    jack.say "'Pardon me, mistress,' she says, 'but I cannot fathom the nature of your speech.'"
    scene rpg
    show rpg nomc nosasha nobree
    show reona guilty leftback at center, zoomAt(1, (980, 820))
    show rpg_table_livingroom
    with fade
    "I lean in close enough to whisper into Reona's ear."
    mike.say "He wants you to talk in character."
    mike.say "To say it the way you think your paladin would."
    show reona surprised at startle()
    "Reona blinks in surprise, but she nods all the same."
    scene
    show rpg_bg_tavern
    show reona rpg talkative at right5
    show mike rpg at left5
    with fade
    reona.say "Erm..."
    reona.say "Good...good wench..."
    reona.say "From where did these fine ales come?"
    reona.say "I do not recall demanding another round!"
    show reona normal
    mike.say "Well done, Reona - that was perfect!"
    show reona happy
    "Reona smiles at the praise, but Jack's already moving on."
    jack.say "'They are from the man at the table yonder' says the wench as she gestures to the man inn question."
    jack.say "Following her hand, you see a small, meek-looking man at a table on the other side of the taproom."
    jack.say "He's fingering the brim of his hat and getting up to walk over, but he looks very nervous as he does so."
    show reona talkative
    reona.say "Wait a minute..."
    reona.say "I've had this happen to me in bars, like, a million times!"
    show reona normal
    show mike talkative
    mike.say "I don't think he's trying to hit on you, Reona!"
    mike.say "Maybe wait until he's said his piece to decide what's behind all of this?"
    "Reona nods and we both turn back to Jack."
    jack.say "Seeming to take your attention as an invitation to come over, the man gets up."
    jack.say "He shuffles over, becoming aware of the fact that all eyes in the inn are now on him."
    show master zorder 9 at blacker, center, zoomAt(1.3, (640, 940)) with dissolve
    show mike at left with ease
    show reona guilty at right with ease
    jack.say "'Beg pardon, noble adventurers,' he says, almost bowing before you."
    jack.say "'May I borrow a moment of your time?'."
    "I open my mouth to speak, but Reona beats me to it."
    reona.say "Of course, my good man."
    reona.say "Say your piece."
    jack.say "Tis my daughter, masters..."
    jack.say "She has been stolen away by the bandits that haunt the lonely forest roads in these parts."
    "I can see Reona beginning to nod, like she's getting into it now."
    reona.say "And you would have us rescue her?"
    reona.say "Maybe slay the bandits while we're at it?"
    jack.say "The man hesitates, like he's getting what he wants."
    jack.say "But there's something still bothering him."
    "Sensing my chance to get involved, I pick up one of my dice."
    mike.say "Can I make a Insight check to see if I can guess what's up?"
    scene rpg
    show rpg nomc nosasha nobree
    show reona guilty leftback at center, zoomAt(1, (980, 820))
    show rpg_table_livingroom
    with fade
    show reona interested
    "Jack nods, and I note that Reona's watching me with interest."
    show reona rightok
    "So I make a point of checking my character sheet."
    "I don't need to, but it'll help walk Reona through the process."
    show reona normal -rightok
    mike.say "So I have Insight of seventeen..."
    mike.say "That means I need to roll below that on a d20?"
    "Jack nods again, and I roll the dice."


    pause 0.3
    mike.say "Yes - I rolled a nine!"
    show reona guilty
    jack.say "You intuit that the man is holding something back."
    jack.say "Like, he's telling you the truth, but not the whole truth."
    show reona interested
    mike.say "When did he start doing that exactly?"
    show reona guilty
    jack.say "Hmm..."
    jack.say "You made the check easily, so I'll tell you."
    jack.say "He hesitated when Reona suggested slaying the bandits."
    show reona whining
    reona.say "Was...was that the wrong thing to do?"
    show reona interested
    mike.say "No, Reona - you were totally in character."
    mike.say "You couldn't have known he was holding something back."
    mike.say "I address him directly"
    scene
    show rpg_bg_tavern
    show master zorder 9 at blacker, center, zoomAt(1.3, (640, 940))
    show reona rpg guilty at right
    show mike rpg at left
    with fade
    mike.say "'Sir, there is something more, yes?'"
    mike.say "'Something that makes you hesitate to want the bandits dead?"
    jack.say "For a moment the man looks like he's going to deny it."
    jack.say "But then it's like you see something inside of him crack."
    jack.say "'Masters,' he says, 'I must confess that my daughter was not kidnapped, exactly...'."
    jack.say "'Her heart was stollen by one of the bandits, he seduced her and she fled to be with him!'."
    "Now I'm beginning to see where this story arc is going."
    "And I can also see that Jack's beginning to reel Reona in with it too."
    "I'm not sure if he's aware of just how close it is to her own story."
    "But it seems to be striking a chord with her all the same."
    "Pretty soon we're signed up to go to the haunted forest in search of the bandits."
    "And of course there's the complication of the daughter and her outlaw lover."
    show reona talkative
    reona.say "We should try to sneak in there and talk to them both, yeah?"
    reona.say "Like, they should have the chance to tell us their side of the story."
    mike.say "Is that your opinion, Reona?"
    scene rpg
    show rpg nomc nosasha nobree
    show reona pensive leftback at center, zoomAt(1, (980, 820))
    show rpg_table_livingroom
    with fade
    mike.say "Or is that how your character sees it?"
    show reona surprised
    reona.say "What's the difference?"
    reona.say "I am my character, aren't I?"
    show reona normal
    mike.say "Sure you are, but you're also playing a part, remember?"
    mike.say "That's part of the challenge of roleplaying, Reona."
    mike.say "Being able to see how someone different to you might handle a situation."
    "By the time the end of the session comes around, we've made good progress."
    "And by that I don't mean we've rushed through everything that Jack has planned."
    "I mean we've got our teeth into the roleplaying aspect of the game."
    "And more importantly, Reona's been enjoying herself too."
    "As I'm beginning to collect up my dice, I notice Reona chatting to Jack."
    "And as we're the only people in the room, I can't help listening in on the conversation."
    scene
    show bg livingroom
    show jack smile at center
    show reona guilty at right
    with fade
    jack.say "You really seemed to get into that once we got started, Reona."
    reona.say "Yeah, I guess it got easier as we got into it."
    jack.say "The quest seemed to get you thinking too, yeah?"
    reona.say "I know, right?"
    reona.say "Like, the more I started to think about it, the more I could imagine how it went down."
    reona.say "The girl's dad is in pieces, worried shitless about her."
    reona.say "But she's too much in love with a bad guy to see it."
    reona.say "Classic story of love with the guys from the wrong side of the tracks!"
    jack.say "It's always great when an adventure really makes the players think."
    jack.say "So I like to use things that people can relate to, you know?"
    "As soon as Jack mentions real-life experiences, the penny seems to drop for Reona."
    "Like she really hadn't related it to her own life until that moment."
    "I think about saying something to her, getting involved in the discussion."
    "But then I dismiss the thought, thinking it's better to let Reona think it over for herself."
    "That way the conclusions that she reaches will be her own."
    $ reona.flags.campaign_delay = TemporaryFlag(True, 2)
    return

label reona_jack_04a:
    if reona.purity.max < 90:
        $ reona.purity.max = 90
    $ result = renpy.call_screen("smartphone_choice", "Jack")
    if not result:
        $ hero.cancel_event()
        $ reona.love -= 5
        return
    jack.say "Hi bro. Want to hang out?"
    jack.say "Reona is joining me."
    mike.say "Sure, I'll meet you at the mall."
    scene bg mall1
    show jack casual at center, zoomAt(1, (320, 720))
    show reona casual zorder 7 at center, zoomAt(1, (960, 720))
    with fade
    "Jack, Reona and I have been hanging out on a pretty regular basis recently."
    "So I've had the chance to really see how they are together and what makes them tick."
    "But the big surprise for me was realising that it's each other - that Jack and Reona are totally compatible."
    "I mean, don't get me wrong - I could never have said that about the person Reona was when we first met."
    "And I know all about their shared history, which, to be frank sounds like a totally toxic mess."
    "But the person that Reona seems to be turning into more each time I see her?"
    "Well that's a totally different story."
    show jack lying at center, traveling(1, 2, (640, 720))
    "She's turning out to be kind, considerate and deeply sensitive."
    show reona lying with dissolve
    "In short, the perfect girl to bring the best out in Jack as well."
    show jack happy with dissolve
    "So yeah, I kind of realised that I'm the third wheel in this relationship!"
    "That Reona's the girl for my best friend and not for me."
    "Am I jealous of him for that?"
    "You know, the weird thing is that I'm not."
    "When I really try to imagine being with Reona, it just doesn't happen, it doesn't feel right."
    "And the more I see her and Jack starting to click, the more I want to see them go further."
    "It's like when we were playing Demons and Demigods the other day."
    "I might have been the one helping Reona to master the mechanics of the game and roleplaying her character."
    "But Jack was the games-master, the one spinning the story and creating the world she was connecting with."
    "So now I'm resolved that I know what my role is in this whole thing."
    "I'm going to make sure they have the time together they need for it to grow."
    "And don't worry, I'm going to be subtle about it too."
    "I just have to wait for the proper chance to present itself."
    "Luckily for me, I don't have to wait that long."
    "Because as we're walking along together, Jack reaches into his pocket."
    jack.say "Wait up, guys..."
    "Looking around, I see that he has his phone in his hand."
    show jack embarrassed
    jack.say "Oh..."
    jack.say "It's my mom!"
    jack.say "I gotta take this..."
    "He turns around as he puts the phone to his ear."
    show screen expression "smartphone_calling" pass ("MoM")
    show jack normal zorder 9 at center, zoomAt (3, (940, 2020))
    show mike smile at center, zoomAt(1, (500, 720))
    show reona lying zorder 7 at center, zoomAt(1, (700, 720))
    with fade
    "Which leaves Reona and I to exchange amused glances."
    show jack whining
    jack.say "Hey, mom..."
    jack.say "No..."
    jack.say "No, I haven't forgotten."
    jack.say "Yes, I know that I promised."
    jack.say "But I'm out with my friends."
    show jack angry
    jack.say "Oh come on - you know that I do have real friends!"
    "Jack slaps his hand over the phone and turns to face Reona and I."
    scene bg mall1
    hide screen expression "smartphone_calling"
    show jack whining at center
    show reona lying at right
    with fade
    jack.say "Look, guys..."
    jack.say "I might have promised my mom I'd help out in her rose garden."
    jack.say "And then I might have gone and forgotten all about it."
    show jack annoyed
    "I raise my eyebrows and let out an amused snort."
    show reona normal
    mike.say "Huh..."
    mike.say "And let me guess..."
    mike.say "She might have just said she'll have your ass on a plate if you don't make good on that promise, yeah?"
    show jack guilty blush with dissolve
    "Jack's cheeks are starting to turn a deep shade of red by now."
    "And I can see that he's not coming up with a way out of this for himself."
    "Now normally I'd be more than happy to watch him twist in the wind."
    "But I have to factor Reona into the equation."
    "Specifically how this makes Jack look in her eyes."
    mike.say "Well, three pairs of hands would be better than one, right?"
    mike.say "And we're just hanging around without anything to do, yeah?"
    "I make sure to turn and look Reona in the eye as I say all of this."
    "And it doesn't take long for her to figure out where I'm going."
    show jack -blush
    show reona shock
    reona.say "Wait..."
    reona.say "Are you suggesting we go over there and help out in his mom's garden?"
    reona.say "Like, prune the rose and stuff?"
    show reona stuned
    mike.say "Why not?"
    mike.say "We've got nothing else to do."
    mike.say "And it just might get Jack off his mom's shit-list."
    "Reona shrugs."
    show reona talkative
    reona.say "What the hell - count me in."
    show reona normal
    show jack surprised
    "With Reona on board, we both look over at Jack."
    "He blinks a couple of times, like he's trying to make sense of it all."
    "And then he starts jabbering into the phone all over again."
    show screen expression "smartphone_calling" pass ("MoM")
    show jack whining zorder 9 at center, zoomAt (3, (940, 2020))
    show mike smile at center, zoomAt(1, (500, 720))
    show reona lying zorder 7 at center, zoomAt(1, (700, 720))
    with fade
    jack.say "Okay, mom, okay..."
    jack.say "I'm coming over right now."
    jack.say "My friends?"
    jack.say "They're coming with me."
    scene bg mall1
    hide screen expression "smartphone_calling"
    show jack casual at left
    show reona casual at right
    with fade
    "Jack ends the call and waves for Reona and I to follow him."
    scene bg street
    show jack casual at left
    show reona casual at right
    with timelaps
    "I'm not too concerned about making the journey from here on foot."
    "Because I remember Jack telling me that his folks live not far from here."
    "And it soon becomes apparent that he knows all of the shortcuts on the way too."
    "All of which means that we arrive in what feels like record time."
    jack.say "MOM..."
    jack.say "We're here!"
    scene bg black
    show cassidy_ending_bg
    show jack at center
    show reona at right
    with fade
    "Jack bellows the words out as he lets us into the garden and looks around."
    "But it's when he leads us towards the roses that he gets an answer."
    show mrswhite at mostleft4 with moveinleft
    "Mrs White" "Quieten down, Jack!"
    "Mrs White" "I could have heard you from three streets over."
    "All three of us look over to see Mrs White emerge from behind a wall."
    "She's one of those mothers that you could imagine from an eighties movie."
    "And there's always part of me that thinks I'd find her really hot."
    "That is if she didn't look so much like Jack!"
    jack.say "Mom..."
    jack.say "You remember [hero.name]?"
    jack.say "And this is Reona."
    show mrswhite at startle(0.2, 5)
    "Mrs White gives me a smile and a little nod."
    "Then she does the same to Reona."
    show mrswhite at center with move
    pause 0.3
    show jack at left4 with move
    "But a second later, she shakes her head, like she's trying to clear her vision."
    "And then she turns back to take a second look at Reona, studying her closer this time."
    show mrswhite at startle(0.05,-10)
    "Mrs White" "Are you..."
    "Mrs White" "Are you really a girl?!?"
    show reona stuned
    "Reona looks more than a little put on the spot by the question."
    show jack embarrassed blush with dissolve
    "And I can see that Jack's already blushing as his mom embarrasses him."
    "But I can't resist stepping in and adding to his discomfort."
    mike.say "Well, Reona?"
    mike.say "Aren't you going to answer the nice lady?"
    mike.say "Are you a girl or not?"
    show reona normal
    "Before Reona can say a word, Jack bustles his way between all of us."
    show jack whining
    jack.say "Mom!"
    jack.say "Are you trying to make me die of embarrassment?!?"
    show jack smile -blush with dissolve
    jack.say "Of course Reona's a girl."
    show jack angry at startle(0.05,-10)
    jack.say "And you..."
    "He rounds on me, trying to look like he's seriously angry."
    "But only managing to make me want to chuckle out loud."
    show jack whining
    jack.say "Why are you encouraging her?"
    jack.say "You never had me do this in front of your mom!"
    show jack normal
    "I can't help remembering the last time Jack met my own mother."
    "Specifically the way his tongue was hanging out the whole time."
    "But I guess this isn't the time or place to remind him of that."
    mike.say "Okay, Jack..."
    mike.say "I'll cut it out."
    "I make a point of turning to Mrs White as soon as I've said this."
    mike.say "So, Mrs White..."
    mike.say "How can we help you with your roses?"
    "The mere mention of her beloved flowers seems to reset the poor woman's brain."
    "And in the space of a few seconds, she's forgotten all about the novelty of Jack turning up with an actual girl in town."
    show mrswhite at startle(0.05,-10)
    "Mrs White" "Oh, all I need is a few more hands to prune them really."
    "Mrs White" "Just let me give you the basic pointers, and some secateurs..."
    "Mrs White" "Then we'll make gardeners out of all three of you!"
    "Mrs White is as good as her word, furnishing us all with what I assume are secateurs."
    "And then she throws in a pair of gardening gloves each too."
    "Which it doesn't take me long to realise are a damn good idea."
    "Because the thorns on those roses are bloody sharp!"
    show reona at mostright5
    show jack at right5
    show mrswhite at mostleft5
    with move
    mike.say "Ouch!"
    "I wave the hand that I just impaled on a thorn in the air."
    "Hoping that the motion will do something to lessen the pain."
    "But all it seems to do is attract the attention of our host."
    "Mrs White" "Oh dear - did you get to close to the thorns?"
    "I look up to see Mrs White smiling at me."
    "And as I do so, I notice that Reona and Jack are working close together."
    "They're kneeling down, leaning over the same rose-bush."
    "So it strikes me that they should really be left alone."
    "Which means someone is going to have to distract Mrs White."
    mike.say "Yeah, I guess so!"
    mike.say "I never knew they could be so sharp...Mrs White!"
    mike.say "I'm sorry, I know that sounds like a dumb thing to call you."
    mike.say "But Jack's never told me what your actual name is."
    show mrswhite at startle(0.05,-10)
    "Mrs White rolls her eyes, as if she's not surprised in the slightest."
    "Mrs White" "Typical, Jack!"
    "Mrs White" "Sometimes I wonder if he remembers it himself."
    "Mrs White" "My name is Fanny, [hero.name] - Fanny White."
    mike.say "Hi, Fanny - nice to meet you."
    mike.say "And I should probably tell you that I know absolutely zero about roses!"
    show mrswhite at startle(0.05,-10)
    "Mrs White" "Well don't you worry about that, young man."
    "Mrs White" "Because I'm going to give you a crash-course on the subject!"
    "For what feels like a couple of hours, I do all that I can to indulge Mrs White."
    "Whenever I get the chance, stealing a glance over her shoulder at Jack and Reona."
    "And feeling vindicated as I see them getting ever closer together each time."
    hide mrswhite
    "Eventually Mrs White gets drawn away to handle some problem that I can't fathom in the garden."
    "But I see that there's no need to keep up the act, as Jack's walking over to me by now."
    show jack normal at center with move
    pause 0.5
    show reona leftback righthold
    show jack at center, traveling(2, 2, (320, 1370))
    mike.say "How's it going, buddy?"
    mike.say "You and Reona seem to make a great team."
    "Jack gazes over at Reona, who's still fiddling with a rose-bush."
    show jack smile
    jack.say "Yeah, [hero.name] - about that..."
    jack.say "What did you do with the old Reona?"
    jack.say "Because the change in her since you two met..."
    jack.say "It's like she's a totally different person or something!"
    show jack normal
    mike.say "Well she can't be that different, Jack."
    mike.say "Because you told me that you had the hots for her back then."
    mike.say "And it's pretty obvious that you still do now."
    show jack surprised
    "Jack looks at me like I've just caught him in the act of doing something shameful."
    show jack guilty
    "He blinks and works his lips, like he's about to start denying it for all he's worth."
    "But then his gaze drops to the ground and he shakes his head."
    show jack whining
    jack.say "It's that obvious, huh?"
    show jack sadsmile
    mike.say "Oh yeah, it is!"
    mike.say "So, I ask again - what are you waiting for?"
    mike.say "If you feel that way about Reona, then tell her!"
    show jack whining
    jack.say "But..."
    show jack worried
    jack.say "But what if she tells me to get lost again?"
    show jack sadsmile
    mike.say "What if she doesn't, you dummy?!?"
    mike.say "And even if she does, which I seriously doubt, so what?"
    show jack annoyed
    mike.say "The last time she did it wasn't the end of the world, was it?"
    show jack sadsmile
    "Jack's looking more like he's coming round to my way of thinking."
    "So I decide to back off a bit and try something more subtle."
    mike.say "Look at it this way, Jack..."
    mike.say "You don't want to end up stuck in the friendzone, do you?"
    mike.say "Struggling to hide your boner every time she's around?"
    show jack perv
    "Jack instantly tries to cover his groin with both hands."
    "All the while looking at me with pleading in his eyes."
    show jack surprised
    jack.say "No?"
    show jack guilty
    pause 0.7
    show jack sad with dissolve
    mike.say "Oh yes!"
    mike.say "Looks like a goddamn tent pole every single time."
    show jack at center, traveling(1, 2, (640, 720))
    pause 2
    "Jack scurries off to rejoin Reona, and I follow a little way behind."
    show jack annoyed with dissolve
    "Then I watch with interest as he kneels down beside her."
    show jack at center, traveling(1, 1, (840, 720))
    pause 1
    show reona guilty
    reona.say "Where did you get to, Jack?"
    reona.say "You ran off and left me with all the work to finish!"
    show jack worried
    jack.say "Reona..."
    jack.say "I..."
    jack.say "I had to get something straight in my head."
    jack.say "Something that I need to say to you."
    "Reona frowns, her expression becoming concerned."
    show reona annoyed
    reona.say "Oh no..."
    show reona guilty
    reona.say "This isn't about what happened before, is it?"
    reona.say "Because I know I was a bitch to you, okay?"
    reona.say "But I've changed, Jack, honestly I have!"
    show jack smile
    jack.say "You haven't changed, Reona..."
    jack.say "I always knew you were a good person, with a good heart."
    show reona embarrassed
    jack.say "All that's happened is that's come out from inside of you now."
    jack.say "You've just proved to me that you really are that person - the one I knew you were!"
    show reona happy
    "Glancing down, I see that Reona's reached out and taken hold of Jack's hand."
    "She's squeezing it for all she's worth, so much so that his fingers are turning white!"
    "Suddenly feeling like I'm intruding on a private moment, I take a step backwards."
    "And I keep on taking them until I'm sure that I've gotten out of their way."
    "I've seen enough to guess where things are going."
    "And I know that they're going to want a little time alone."
    "Which means I'm going to have to pump old Fanny for more information on her roses."
    "So Jack has better be bloody well grateful once today is over!"
    $ reona.flags.campaign_delay = TemporaryFlag(True, 2)
    return


label reona_jack_05a:
    if reona.purity.max < 100:
        $ reona.purity.max = 100
    menu:
        "That's the end of Demons and Demigods's campaign. Let's celebrate!"
        "Let's go to the Winchester":
            pass
        "Maybe later":
            $ bree.love -= 3
            $ sasha.love -= 3
            $ reona.love -= 5
            if Harem.find(minami, name='home'):
                $ minami.love -= 3
            $ hero.cancel_event()
            return
    scene bg pub
    "You know those scenes in the movies, where the triumphant sports team strides into the local bar and celebrates?"
    "Well imagine that same kind of thing, only with a small local diner, and its a bunch of role-players that are celebrating."
    "Because that's exactly what happens once we've wrapped up the big finale in Jack's game of Demons and Demigods."
    "The party totally smashed it, defeating all of the obstacles in our way and putting down the big bad at the end."
    "A big bad that, I must also say, was expertly put together and portrayed by Jack in his role as games-master."
    "In fact it went so well that we all agreed a celebration was in order, and the diner seemed like the best choice."
    "More wholesome than the local pub and open in the afternoon, where a nightclub wouldn't be open for hours."
    "Plus it has the bonus of laminated menus - always a sign of true class..."
    show sasha casual zorder 2 at mostleft5
    show bree casual zorder 3 at left5
    with easeinright
    "I push the door open and hold it as Sasha and Bree rush inside and try to get one of the best tables in the place."
    if Harem.find(minami, name='home'):
        show minami casual zorder 4 at center with easeinright
        "Minami keeps pace with me, sticking close to my side and holding onto my arm."
    show reona casual zorder 0 at mostright5
    show jack casual zorder 1 at right5
    with easeinright
    "But looking back over my shoulder, I see Reona and Jack walking slowly at the back of the group."
    "And what's more, they seem to be in a world all of their own, a little apart from the rest of us."
    "I keep a hold of the door as they saunter through it."
    "And as I do so, I can't help hearing a little snippet of their conversation."
    show jack worried
    jack.say "And when you pulled off the turning of that vampire in the crypt, Reona..."
    jack.say "My heart was in my mouth when you rolled the dice to make the check!"
    show jack annoyed
    show reona guilty
    reona.say "I had no idea if I could even do that!"
    reona.say "But I was, like, my sword looks like an upside down cross, right?"
    reona.say "And I use it to fight as a holy warrior - so that should work the same way as a cleric's holy symbol, yeah?"
    show reona normal
    show jack smile
    jack.say "Oh, totally, Reona, totally..."
    show jack normal
    "I can't help shaking my head as I close the door and follow them to the table the others have found."
    "On the one hand I'm amazed to hear Reona talking like a nerd of veteran standing."
    "And on the other, I can't help being astonished that she's almost linking arms with Jack!"
    "The Reona that I bumped into back when we met would never have done either of those things."
    "But here she is, right in the middle of a band of geeks, and fitting in just fine."
    "Though by the time we make it over to the table, things don't seem to be going so smoothly anymore."
    "Because I can see the girls already seated around it, and Jack waving his hands in the air."
    show jack whining at startle(0.05,-10)
    jack.say "Are you serious?"
    jack.say "This table is way too small!"
    show jack normal
    show bree vangry at startle(0.05,-10)
    bree.say "What do you want me to do about it, Jack?"
    bree.say "This is the only one that was free."
    show bree annoyed
    show sasha vangry at startle(0.05,-10)
    sasha.say "Yeah, Jack..."
    sasha.say "All the others are only two-seaters!"
    show sasha annoyed
    if Harem.find(minami, name='home'):
        show minami vangry at startle(0.05,-10)
        minami.say "Maybe if you'd hurried up getting here..."
        minami.say "Rather than dawdling along with your girlfriend!"
        show minami annoyed
    show reona annoyed at startle(0.05,-10)
    reona.say "Hey!"
    show reona guilty
    reona.say "What did you just say?!?"
    show reona sad
    "I can see the good vibes and party atmosphere about to be swept away."
    "Unless I step up and really try to do something about it, that is."
    mike.say "Hey, hey, hey..."
    mike.say "We came here to eat and toast our victory - not to squabble like little kids!"
    mike.say "Now what's the problem here?"
    "Jack points to the table where the rest of the girls are sitting."
    show jack whining at startle(0.05,-10)
    jack.say "There's only one seat left, see?"
    jack.say "That means you, me or Reona gets it."
    show jack sad
    show reona whining
    reona.say "And it means we can't all sit together!"
    show reona sad
    "Jack crosses his arms over his chest, like he's made his point."
    "And Bree uses this as her cue to speak up for the others."
    show bree talkative at startle(0.05,-10)
    bree.say "It's not like this is our fault, [hero.name]."
    bree.say "All the other big tables are already taken."
    show bree gloomy
    "All it takes is a quick glance around the place to see that Bree's right."
    "The other unoccupied tables all seem to be two-seaters."
    menu:
        "Point out the two-seater table nearby":
            scene drink_room_pub
            show drink_table_pub_nonpc
            show drink_room_fg_pub
            with dissolve
            "I look over at the nearest empty two-seater table."
            "And then back at Jack and Reona."
            mike.say "I bet you two could easily get in on the conversation over there."
            mike.say "Plus you could just keep on talking about whatever held you up on the way here."
            scene bg pub
            show sasha casual zorder 2 at mostleft5
            show bree casual zorder 3 at left5
            if Harem.find(minami, name='home'):
                show minami casual zorder 4 at center
            show reona casual zorder 0 at mostright5
            show jack casual zorder 1 at right5
            with dissolve
            "For a moment I think Jack's actually going to be dumb enough to argue the toss."
            "But then I see the information slowly work its way through his head."
            "And once it has, the look on his face totally changes."
            show jack smile
            jack.say "He's got a point, Reona."
            jack.say "We didn't really get to finish that conversation off."
            show reona interested
            "The idea must be one that appeals to Reona."
            show reona at center, traveling(2, 1.5, (2040, 1220))
            show jack at center, traveling(2, 1.5, (1840, 1220))
            "As she nods and smiles, eagerly following Jack to the closest free table."
        "Rush on the empty chair":
            "I make a point of sitting down in the empty chair without saying another word."
            "At least not until my backside is firmly planted on the seat."
            mike.say "Look guys..."
            mike.say "You're all adults here."
            mike.say "So why don't you sort it out like adults, huh?"
            show jack annoyed
            "For a moment it looks like Jack's going to say something rash."
            "But then he seems to consider the options a little more closely."
            show jack smile
            "And I'm relieved to see the colour of his face return to normal."
            jack.say "Why don't we take one of the two-seaters, Reona?"
            jack.say "That way we can finish off our conversation from before."
            show reona interested
            "The idea must be one that appeals to Reona."
            show reona at center, traveling(2, 1.5, (2040, 1220))
            show jack at center, traveling(2, 1.5, (1840, 1220))
            "As she nods and smiles, eagerly following Jack to the closest free table."
    "I watch with a sense of relief and no little accomplishment as they hurry off."
    "And then I turn my attention to the menu, as well as the conversation at my own table."
    "Soon enough I'm lost in the back and forth with the other girls."
    "On top of that we're all ordering something to eat and drink too."
    "So spying on Jack and Reona is kind of out of the question."
    "It's only when everyone else is staring at something on Sasha's phone that I see a chance."
    scene bg black
    show drink_room_pub
    show drink_table_pub_nonpc zorder 9
    show drink_room_fg_pub
    show reona casual embarrassed zorder 1 at center, zoomAt(1.4, (840, 920))
    show jack casual happy zorder 1 at center, zoomAt(1.6, (320, 1100))
    with fade
    "Which allows me to lean a little closer to Jack and Reona's table so I can listen in."
    "And yeah, I know that sounds like a bit of a jerk thing to do."
    "But look at this thing from my point of view for a moment."
    "Reona's been on a pretty crazy journey recently."
    "She's been discovering things about herself that she never knew before."
    "And then you have Jack, one of those guys that could fuck up watching paint dry."
    "Can you really blame me for wanting to keep an eye on what they're doing together?"
    show jack normal
    show reona lying leftback
    reona.say "I gotta say, Jack..."
    reona.say "Demons and Demigods is something I NEVER thought I'd get into."
    reona.say "But I dunno..."
    reona.say "Playing it with you was so much fun!"
    show reona embarrassed
    show jack embarrassed blush with dissolve
    "I can see that Jack's already blushing as Reona heaps praise onto him."
    "And it comes as no surprise that he waves it away with a dismissive gesture."
    "But he's clearly loving the fact a hot girl is so into one of his major passions in life."
    show jack happy -blush
    jack.say "Well, it's a team effort, Reona."
    jack.say "Everyone working together to make it so cool."
    "Reona shakes her head at this."
    show reona shout rightopen
    show jack guilty
    reona.say "Bullshit, Jack!"
    show reona lying
    reona.say "You're the one that does all the hard work."
    reona.say "All the rest of us just get to have fun."
    reona.say "I don't know how you can be so calm and understanding with everyone."
    reona.say "Especially when you were having to teach me how to play."
    show reona embarrassed rightnormal
    "Jack shrugs at this."
    show jack happy
    jack.say "It's easy when it's someone you care about, Reona."
    jack.say "And I could see that you were getting so much out of it too."
    jack.say "That's one of the really amazing things about the game."
    jack.say "Playing a different person can help you discover things about yourself."
    show jack worried
    jack.say "Which I know sounds totally wrong!"
    "Reona shakes her head again."
    show reona lying
    reona.say "No, Jack..."
    reona.say "I get it, I totally do!"
    reona.say "Like, there were so many times that you made me think about what my character should do."
    reona.say "Things that were about the morality of the situation, what was right and what was wrong."
    reona.say "It made me think about myself, and the person that I am in real life too."
    show reona guilty
    reona.say "Did you..."
    "Reona pauses, like she's really trying to summon the courage to ask something."
    reona.say "Did you, like, do that on purpose?"
    reona.say "You know, because you know the real me?"
    show jack guilty
    "Now I can see Jack starting to squirm and look a little uncomfortable."
    show jack worried blush with dissolve
    jack.say "Erm..."
    jack.say "Well, yeah, Reona..."
    show jack happy -blush with dissolve
    jack.say "Part of being a good games-master is knowing how to challenge the characters."
    jack.say "But that's all taken care of in the rules and rolling the dice."
    jack.say "If you want to take things to the next level, you have to challenge the players themselves."
    jack.say "And I've always known that you're a good person - one of the best I ever met."
    "Jack pauses, and I can see he's gearing up for the big one."
    show jack worried
    jack.say "Don't be mad, Reona..."
    show jack happy
    jack.say "But I thought you needed to discover that about yourself."
    show reona lying
    show jack guilty
    reona.say "Oh, Jack..."
    reona.say "Why are you so kind to me?"
    reona.say "Especially after I treated you so badly!"
    show reona guilty
    show jack happy blush
    jack.say "Because I always saw the good in you, Reona..."
    jack.say "Even when you couldn't see it in yourself."
    show jack smile
    "I take a look down at the table between Jack and Reona."
    "And I see that they've joined hands, totally without thinking about it!"
    show reona happy
    "It's when I glance back up that I realise Reona is looking right at me."
    "I feel a stab of panic in the pit of my stomach, fearing that she's going to be mad."
    show reona interested with dissolve
    "But then I notice the look on her face is one of happiness, maybe even gratitude."
    "Am I being a total egomaniac here, or is Reona silently thanking?"
    "Letting me know she's grateful that I set all of this in motion?"
    show jack guilty
    jack.say "Erm..."
    show jack happy
    jack.say "Reona..."
    show reona guilty
    "All of a sudden the spell is broken and Reona turns her attention back to Jack."
    "I look away too, feeling more than a little guilty for listening in."
    "But all the same, I'm still not able to keep myself from continuing to do so."
    show reona lying
    reona.say "Yeah, Jack..."
    reona.say "What is it?"
    show jack guilty
    pause 1
    show jack worried
    jack.say "I wanted to ask if..."
    jack.say "I was wondering if you'd like to..."
    jack.say "I really feel as if I could kiss you right now."
    show jack happy
    jack.say "But only if you're up for it, of course!"
    "I feel like I'm holding my breath as I wait to see what happens next."
    "Like nothing can continue for me until I know what Reona's answer will be."
    "In the end she doesn't say a word, just leans forwards a little."
    "Enough to place her lips gently against Jack's."
    scene bg black
    show bg pub
    show reona kiss jack casual
    with fade
    "The kiss that follows is kind of a beautiful thing, as much as anything involving Jack can be."
    "It's tender and soft, meaningful in the extreme as the first public show of affection between them."
    "Though Jack does rather spoil it at first, by sitting there with his eyes open in surprise."
    "Which kind of makes him look like he's been slapped in the face with a wet fish!"
    "But soon enough he closes them and leans into it too, surrendering to the moment."
    "That's when I notice that everyone else is looking at them too."
    "And I feel like this is one of those rare moments in life."
    "One that deserves to be immortalised with a toast."
    "So getting to my feet, I raise my glass above my head."
    scene bg pub
    show reona casual happy zorder 0 at mostright5
    show jack casual happy zorder 1 at right5
    show bree casual zorder 3 at left5
    show sasha casual zorder 2 at mostleft5
    if Harem.find(minami, name='home'):
        show minami casual zorder 4 at center
    with dissolve
    mike.say "Ahem..."
    mike.say "I'd like to propose a toast."
    mike.say "To new beginnings and old friends..."
    show bree happy at startle(0.05,-10)
    show sasha happy at startle(0.07,-11)
    if Harem.find(minami, name='home'):
        show minami happy at startle(0.04,-7)
    show jack happy at startle(0.08,-12)
    show reona happy at startle(0.06,-11)
    mike.say "Finding their way back to each other!"
    show bree happy at startle(0.05,-10)
    show sasha happy at startle(0.07,-11)
    if Harem.find(minami, name='home'):
        show minami happy at startle(0.04,-7)
    show jack happy at startle(0.08,-12)
    show reona happy at startle(0.06,-11)
    "I'm glad that this is enough to get me a round of cheers and clapping from the others."
    "Because it helps to hide the fact everyone else in here is staring at me like I'm insane!"
    "Needless to say I'm relieved to be able to sit down and plough into my burger again."
    $ bree.love += 3
    $ sasha.love += 3
    if Harem.find(minami, name='home'):
        $ minami.love += 3
    $ reona.hide()




    return



label reona_jack_01b:
    show reona
    "Now that Jack's filled me in on the details of how he and Reona know each other, it should be mystery solved."
    "I know who they are to each other and the reasons behind why they fell the way they to towards each other too."
    "But somehow that's just not enough for me to be satisfied, because I've only heard Jack's side of the story."
    "I mean sure, the fact that Reona hardly ever mentions him seems to back up all that he said about it."
    "The problem is that I usually find there's always something that one side doesn't know about the other."
    "So until I hear it from Reona's own mouth, I'm never going to be totally at ease with how things are between them."
    "Which means picking the right moment to press Reona on the matter."
    "And as soon as I'm sure she's in a receptive mood, I make my move."
    mike.say "Reona..."
    mike.say "I was talking to Jack the other day."
    show reona pensive
    "Reona looks around at this, vague interest in her eyes."
    reona.say "Huh?"
    reona.say "Who's Jack?"
    mike.say "You know who I mean."
    mike.say "Long brown hair?"
    mike.say "Into geeky stuff?"
    mike.say "Erm..."
    "I'm going to hate myself for saying this."
    "But Reona's showing no signs of recognition whatsoever."
    mike.say "Kind of..."
    mike.say "Well...kind of pudgy?"
    show reona surprised
    "As soon as I mention Jack's weight, Reona's expression changes."
    "It's like I can see the light going on in her head."
    "And she nods at me with a smile on her face."
    reona.say "Oh..."
    reona.say "That Jack!"
    show reona normal
    reona.say "Sure I know him - we met back when I started my course at college."
    "I feel sense of relief that we're finally on the same page."
    "Even if the price was drawing attention to the size of Jack's gut!"
    mike.say "Yeah..."
    mike.say "He told me all about how you two met."
    mike.say "But he also told me that you don't talk to him anymore."
    mike.say "And I was wondering why that is?"
    "Obviously I'm not going to mention the reason that Jack suggested."
    "Because I'm sure even a girl as forward as Reona would find it insulting to be called a slut!"
    "So instead I just try to drop the question and see what she has to say for herself."
    show reona annoyed
    reona.say "Okay, [hero.name]..."
    reona.say "I don't know what Jack told you."
    reona.say "But we kind of got thrown together back then."
    show reona sad
    reona.say "When we started to meet more people, that kind of killed it."
    reona.say "Because it was obvious we were very different types, you know?"
    "I can't help nodding along as I hear what Reona has to say for herself."
    show reona normal
    "Because all of it makes sense when she's the one explaining it to me."
    "She's a hot, outgoing girl that doesn't have to try hard to be popular."
    "And with the best will in the world, I know that Jack's a standard nerd!"
    "Plus he has a habit of falling in love at the drop of a hat too."
    mike.say "I can believe that, Reona."
    mike.say "Sometimes people just aren't compatible."
    show reona sad
    "Reona nods at this."
    show reona annoyed
    reona.say "Plus he smells way too much like a virgin to me!"
    reona.say "All desperation and no experience!"
    show reona normal
    "Just when she was winning me over, Reona goes and drops in a line like that."
    "Aiming a personal insult at Jack and reminding me that she can be a bit of a bitch too."
    mike.say "Jack might not me the most experienced guy in the world."
    mike.say "But I don't think Jack's an actual virgin, Reona!"
    show reona happy
    reona.say "Well you could have fooled me!"
    "Reona seems to see the serious look on my face."
    show reona pensive
    "And it makes her change her tune a little."
    reona.say "Okay, okay..."
    reona.say "Maybe not an actual virgin."
    reona.say "But he needs to be taken in hand and shown the way."
    show reona normal
    reona.say "If you know what I mean?"
    show reona happy
    "Reona raises an eyebrow as she smiles at me."
    "And it begins to dawn on me what she means."
    mike.say "Are..."
    mike.say "Are you offering to help Jack out?"
    mike.say "To give him the experience he needs in the bedroom?!?"
    "Reona chuckles and shakes her head."
    show reona flirt
    reona.say "Oh no, [hero.name]..."
    reona.say "This is a job I can't handle on my own."
    reona.say "I'm saying that we should both take the boy in hand."
    show reona interested
    reona.say "Together we can get the virgin stink off of him."
    reona.say "What do you say?"
    menu:
        "Sounds like a plan!":
            "I open my mouth to say no, out of sheer instinct."
            "But then I pause for a moment as I actually think about it."
            "If I want to build a bridge between Jack and Reona, then why not like that?"
            "It'd show Reona that Jack's way more interesting and adventurous than she thought."
            "Plus it'd prove to Jack that Reona's not totally adverse to spending time with him."
            "Hell, she just told me she's willing to fuck him under the right circumstances!"
            mike.say "You know what, Reona..."
            mike.say "I think that's a great idea!"
            show reona happy
            "Reona seems delighted with my reaction."
            "So much so that she even claps her hands with glee."
            reona.say "Yay!"
            reona.say "There's only one thing I like more than a cock."
            reona.say "And that's two cocks at once!"
            show reona devious
            "I can't help staring at Reona as she admits that."
            "Wondering if Jack wasn't at least a little bit right about her."
            "But luckily for me, she doesn't seem to notice at all."
            mike.say "Ah..."
            mike.say "Yeah, Reona..."
            mike.say "Well, you leave asking Jack to me."
            mike.say "We're the ones on speaking terms, after all!"
            show reona flirt
            reona.say "Okay, [hero.name]..."
            reona.say "You go rustle up that extra cock for me!"
            mike.say "Erm, okay..."
            mike.say "I'll be in touch."
            $ reona.flags.help_virgin_jack = True
        "Love the guy! But I don't want to see him naked...":
            "The moment that Reona suggests we both fool around with Jack, I know what my answer will be."
            "I was trying to get to the bottom of the problem between them by asking all those questions."
            "Not for one moment did I want to end up getting into a game of sexual twister with the two of them!"
            mike.say "No way, Reona!"
            mike.say "For sure Jack's my friend."
            mike.say "But I don't want to have sex with him!"
            show reona sad
            "Reona shrugs at this, like she doesn't care either way."
            show reona annoyed
            reona.say "Suit yourself, [hero.name]."
            reona.say "It was just a suggestion."
            reona.say "Might have been fun though..."
            show reona normal
            "Reona lets the words hang in the air for a moment."
            "Almost like she's giving me one last chance to change my mind."
            "But that's not something that's going to happen."
            mike.say "Nope."
            show reona sad
            mike.say "No way."
            mike.say "No chance whatsoever."
            mike.say "Jack can find his own hook-ups."
            $ reona.flags.help_virgin_jack = False
    return

label reona_jack_02b:
    "Now that I've agreed to try and broker a threesome between Jack, Reona and myself, there's only one more thing to do."
    "And that's obviously to track down Jack and try to explain the idea to him in a sane and logical manner."
    "Which I can't help thinking is going to be a challenge, based on the way talked about Reona the last time I saw him!"
    "Seriously, Jack seems to see her as the worst of the worst, a slut that tossed him aside as soon as she had no use for him."
    "And on the other side of the coin, Reona thinks that Jack has the stink of a virgin on him."
    "Whatever that's supposed to mean..."
    "But I take hope in the fact that she was so quick to suggest the threesome."
    "And that has to mean that she can see past her issues with Jack, right?"
    "I just hope that I can convince him to do the same, or else this thing isn't going to happen."
    "So the next time I see Jack, I do all that I can to broach the subject in a subtle manner."
    show jack at center, zoomAt(1.5, (640, 1040)) with dissolve
    mike.say "Hey, Jack..."
    mike.say "How are you doing, buddy?"
    "Jack shrugs at this and makes a kind of grunting sound."
    jack.say "Meh..."
    jack.say "I've been better, man."
    jack.say "But I guess I can't complain."
    "I try to ignore the fact that he just contradicted himself."
    "And instead I start to bait the trap that I want to set for him."
    mike.say "Oh, by the way..."
    mike.say "I was talking to Reona the other day."
    show jack sad
    show fx anger
    "At the mere mention of Reona's name, Jack shoots me a hard glance."
    "One that's so hard I feel like it's slapping me across the face."
    show jack angry
    jack.say "Oh yeah?"
    jack.say "And what did that little hussy have to say for herself, huh?"
    jack.say "Did she tell you about all the Jock cocks she's been riding?"
    show jack sad
    hide fx
    "I can feel myself beginning to sweat as Jack verbally unloads on the subject of Reona."
    "And the task ahead now feels like an uphill struggle for me."
    mike.say "Erm..."
    mike.say "No, Jack..."
    mike.say "Not exactly..."
    show jack angry
    jack.say "Why not?"
    jack.say "Did she have a handful of dicks in her mouth at the time?!?"
    show jack sad
    "Oh man..."
    "I'm just going to have to come out and say it."
    mike.say "Not this time, Jack!"
    mike.say "You're not going to believe this..."
    mike.say "But she actually asked if the two of us were up for a threesome!"
    mike.say "I know how you feel about her, so if you want me to tell her to get lost..."
    "Before I can finish what I have to say, Jack leaps straight in."
    show jack perv at startle
    "And the look on his face shows the fastest and most complete turn-around I've ever seen!"
    show jack at center, traveling(1.75, 0.2, (640, 1150))
    jack.say "A THREESOME?!?"
    jack.say "With me as one of the three?"
    jack.say "Of course I want to do it!"
    jack.say "Does she want to do it right now?!?"
    show jack at center, traveling(1.5, 0.5, (640, 1040))
    "I have to take a step backwards as Jack's leaning over me."
    "He's getting in my face too, grabbing me by the arms."
    mike.say "Jack..."
    with vpunch
    mike.say "JACK!"
    mike.say "Calm down, for god's sake!"
    "My words seem to have the desired effect on Jack."
    show jack at center, traveling(1.25, 0.5, (640, 880))
    "As he lets go of me and backs away a few feet too."
    show jack normal
    "Jack holds up his hands to show me that he's back in control of himself."
    jack.say "Sorry, [hero.name], sorry..."
    jack.say "I might have got a little over-excited for a moment there."
    jack.say "Please tell Reona that I'm very much up for what she's proposing."
    jack.say "If you would be so kind?"
    "I'm straightening myself up as he says all of this."
    "And I nod slowly, but still keep my distance from him."
    mike.say "Okay, Jack..."
    mike.say "I'll do that."
    mike.say "Talk to you soon."
    hide jack with dissolve
    "With that I turn and start to walk away."
    "I see Jack give me a brief wave, then I turn my head."
    "But before I'm totally out of sight of him, I risk a glance backwards."
    "Which is when I see him running around in a circle, punching the air."
    "And I guess that means he's celebrating the offer I just made him."
    return

label missed_reona_jack_03b(from_cancel=False):
    if not from_cancel:
        "Shit, I missed my date. Reona is going to be mad."
        $ reona.love -= 10
    return

label reona_jack_03b(appointment=None):
    $ DONE["reona_jack_03b"] = game.days_played
    scene bg livingroom
    "I feel like I've been running between Jack and Reona like crazy in order to pull this thing off."
    "Getting word from one of them and then hurrying off to make sure the other is on the same page."
    "But now the big day is finally here, and we're all set to meet up for the very first time."
    "Of course the only place where we could do it turns out to be mine, no surprise there."
    "So I've also had to make sure that my housemates are safely out of the way too."
    "A quick glance at the time tells me that I still have the chance to straighten the place up."
    play sound door_knock
    "And I'm just about to make a grab for the vacuum cleaner when there's a knock at the door."
    "At first I'm not sure who it could be, as Jack and Reona aren't due to arrive yet."
    "But I quickly shake off my confusion and make for the door."
    "Because whoever it is and whatever they want, I have to get rid of them as soon as possible!"
    "So with that in mind, I begin that process before the door is even half open."
    scene bg black with dissolve
    pause 0.1
    scene bg house
    with wiperight
    mike.say "What do you want?"
    mike.say "Whatever it is, I don't want any!"
    mike.say "I don't have the time for..."
    show jack casual surprised at center, zoomAt(1.5, (640, 1040)) with dissolve
    jack.say "Whoa..."
    jack.say "What are you talking about, man?!?"
    jack.say "Wait...I did get the right day, didn't I?"
    "All I can do is blink in surprise at the sight of Jack, standing on the doorstep."
    jack.say "Well?"
    jack.say "Did I get the day right or not?"
    "Suddenly my brain seems to catch up with what's going on in front of me."
    "And I shake my head, trying to make sure what comes out of my mouth is relevant too."
    mike.say "Right day, Jack..."
    mike.say "But wrong time."
    mike.say "You're too early."
    "I'm expecting Jack to look embarrassed at this."
    "At least to offer me some kind of apology."
    show jack happy at center, zoomAt(1.0, (640, 1040)), startle
    "But instead he just shrugs and lets out a peal of laughter."
    "And what's worse is that he does this while shouldering his way past me and into the house!"
    scene bg livingroom with fade
    pause 0.1
    show jack at right with easeinright
    jack.say "Well, can you blame me?"
    jack.say "I wasn't going to turn up late."
    jack.say "Not for something like this!"
    "Jack doesn't stop once he's in the hallway either."
    show jack at center with ease
    "Instead he keeps on going, bustling into the house without asking permission."
    "So I guess there's no point in trying to hold him to account for his faux pas."
    "Instead I close the door and follow behind him."
    "And when I catch up to Jack, he's looking around the place."
    "Hell, he's even lifting up cushions and peeking behind the curtains!"
    jack.say "So..."
    jack.say "Is Reona here yet?"
    "I slap Jack's hand away from the next thing he tries to look under."
    mike.say "No, Jack..."
    mike.say "Reona isn't here yet."
    mike.say "And even if she was, she wouldn't be hiding under a cushion!"
    show jack happy at startle
    "Jack laughs again, rubbing the back of his head with one hand."
    jack.say "Ha..."
    jack.say "Yeah, yeah..."
    jack.say "Of course not!"
    show jack normal
    jack.say "Sorry...I'm just feeling a little nervous, that's all."
    jack.say "So when is she getting here?"
    mike.say "Unlike you, probably the time we actually agreed!"
    play sound door_knock
    "As if saying that was tempting fate, there's the sound of another knock at the door."
    "I turn towards the hallway, noting that if this is Reona, she's still a little early."
    show jack at center, traveling(1.5, 0.2, (840, 1040))
    pause 0.2
    with hpunch
    "But before I can take a step in that direction, Jack elbows me out of the way."
    mike.say "Wha..."
    mike.say "Hey!"
    "By the time I regain my balance, Jack's already at the front door."
    scene bg black with dissolve
    pause 0.1
    scene bg house
    show reona annoyed at right5
    with wiperight
    pause 0.2
    show jack happy at left with easeinleft
    "And I watch as he throws it open, revealing Reona on the doorstep."
    reona.say "Oh..."
    show reona normal
    reona.say "Hey, Jack..."
    jack.say "Hi, Reona!"
    jack.say "So great to see you."
    jack.say "You look amazing!"
    show reona embarrassed
    reona.say "Erm..."
    reona.say "Thanks, Jack..."
    reona.say "Is [hero.name] here too?"
    "I finally make it to the door and make a point of shoving Jack aside."
    mike.say "Yeah, Reona..."
    mike.say "I'm here."
    mike.say "Come on in."
    show reona happy
    "Reona seems to recover a little of her composure as she lays eyes on me."
    scene bg livingroom with fade
    pause 0.2
    show jack at left5
    show reona happy at right5
    with easeinright
    "And she does as I say, stepping over the threshold and into the house."
    "Almost as soon as she does so, Jack pipes up again."
    show jack perv
    jack.say "So..."
    jack.say "We're going to have a threesome, right?"
    "Reona chuckles and shakes her head."
    reona.say "Top marks for enthusiasm, Jack."
    reona.say "But you lose points for going too fast!"
    show jack sad
    jack.say "Wha..."
    jack.say "What are you saying, Reona?"
    jack.say "Aren't we going to do it?"
    show reona devious
    "Reona seems to be enjoying the way that she has Jack wrapped around her finger."
    "And I have to admit that watching her torture him is pretty intriguing for me too."
    show reona happy
    reona.say "Oh, Jack - don't worry."
    reona.say "We're going to have some serious fun together."
    reona.say "But we need to take things slowly at first."
    reona.say "Start out simple and build it up from there."
    show jack normal
    jack.say "Okay, okay..."
    jack.say "Sorry...I just don't want to make this weird!"
    jack.say "I mean, I know it kind of is weird already, the three of us together."
    jack.say "I guess what I mean is that I don't want to make it extra weird!"
    show reona at startle
    "Reona chuckles and begins to stroke Jack on the chest."
    reona.say "Of course it's weird, Jack..."
    show reona flirt
    reona.say "Weird is the spice that makes it taste SO good!"
    show jack blush
    show reona normal
    "I can see that Jack's on the verge of exploding."
    "His barely suppressed desire bubbling just below the surface."
    "So this seems like a good place for me to step in."
    mike.say "My thoughts exactly, Reona."
    mike.say "About taking things slowly, that is!"
    mike.say "That's why I planned ahead."
    menu:
        "Play video games with them":
            "I gesture towards the sitting room."
            mike.say "I thought we could play some videogames?"
            mike.say "That way we can unwind and have some fun."
            mike.say "Plus we'll be getting to know each other at the same time."
            show reona happy
            "Reona nods happily and walks into the sitting room ahead of Jack and I."
            "But I can see that he's still struggling to control himself."
            "On the one hand doing something so familiar must be a comfort."
            "Yet on the other he has to do it with Reona in the room."
            "Not to mention with so much sexual tension in the air."
            "With that in mind, I put a hand on Jack's shoulder as we walk in behind Reona."
            mike.say "Just relax, okay?"
            mike.say "Don't overthink things and fuck it up."
            jack.say "What?"
            jack.say "Oh...oh yeah, man."
            jack.say "Don't worry, I'm cool."
            "The look on Jack's face says the exact opposite."
            "But I nod and let him go all the same."
            "Once we're in the sitting room, I turn on the Z-Box."
            "And then I toss joypads to Jack and Reona."
            "I also make sure that we play games that are easy to pick up."
            "Ones that encourage us to play in a light-hearted, fun manner."
            "Pretty soon, Reona and I are relaxing and having a good time."
            "So much so that I quite forget about keeping an eye on Jack."
            "When I look his way again, I get a shock."
            "Because he's red in the face, like he's straining with effort of something."
            "And I swear that I can actually see veins standing out on his forehead!"
            "Gently nudging Reona, I nod towards Jack."
            "Thankfully it doesn't take more than that for her to notice it too."
            "And she seems to know just how to deal with the problem."
            reona.say "Hmm..."
            reona.say "I'm getting tired of playing with this thing."
            "She tosses the joypad aside without a care as she says this."
            "Then Reona puts a hand on each of our groins."
            hide reona
            show reona double hj jack mikenpc jacknpc down mike_close
            with fade
            reona.say "I think I need a joystick instead..."
            "Jack and I watch in stunned silence as she unzips our flies."
            "A feat made all the more impressive as she does each with one hand."
            "Then Reona reaches inside, and I feel her fingers close around my cock."
            "She must be doing the exact same thing to Jack too."
            "Because his face has an expression of genuine surprise on it."
            "And I guess mine must be a perfect mirror image of it right now too!"
            show reona double hj jack onjack
            "Of course Reona knows exactly what effect she's having on the two of us."
            show reona double hj jack onmike mouth_lick
            "A quick glance at her face shows me that she's smiling like a Cheshire Cat."
            "And I know the effect she's having on me too."
            "Because I'm already hard as a rock!"
            "My guess is that Jack's in the same position, though I refrain from checking."
            "The reason being that, despite what Reona said, there is such a thing as too weird."
            "Instead I sit back and let her have her way with me."
            "Reona seems to have no problem handling Jack and I at the same time."
            show reona double hj jack speed_jack speed_mike mike_smile jack_smile at startle(0.05,-10)
            "Her hands move up and down in almost perfectly synchronised motions."
            "Plus she knows just when to squeeze and when to ease off too."
            "I'm getting off on the feeling so much that I daren't move a muscle."
            "In fact I don't think I'd move even if my housemates walked in on us right now."
            "The one time that I do move a part of my body is to twist my head around."
            "And I regret that instantly, as my gaze meets Jack's."
            "He's grinning almost as much as Reona is, like he can't believe his luck."
            "But I manage to tear my eyes away before he manages to put me off."
            "Though that seems to have no effect on what's happening down below."
            "Because within mere moments, I can help beginning to pant."
            "I know that I'm about to cum, and I can hear Jack making similar noises too."
            "That means Reona's skilled enough to make sure we both lose it at the same time!"
            "But I don't have any chance to think about that, as things start to speed up."
            show reona double hj jack mikecum jackcum mike_close jack_ahegao -speed_mike -speed_jack with vpunch
            "And before I know it, I feel myself shooting my load."
            with vpunch
            "Reona lets out a filthy giggle as cum seeps from between her fingers."
            with vpunch
            "But all I can do is gasp for breath."
        "Dip in the pool with them":
            "I point to the French windows and out into the garden beyond."
            mike.say "I thought we could take a dip in the pool?"
            mike.say "That way we can cool off and have some fun."
            mike.say "Plus we'll be getting to know each other at the same time."
            "Jack and Reona share a look of genuine surprise at this."
            "Then they turn their gazes on me as one."
            jack.say "Nobody mentioned the pool before now."
            jack.say "I don't have my trunks with me!"
            show reona flirt
            reona.say "Me neither, [hero.name]."
            reona.say "Unless..."
            reona.say "You want to do some skinny-dipping?!?"
            "I hold up a hand at this."
            "And I shake my head too."
            mike.say "No need to worry about that."
            mike.say "I've got spare trunks and bathing suits you can use."
            "This seems to mollify Jack and settle Reona down a little too."
            scene bg pool with fade
            "And once I've handed them over, we all go off to change."
            show reona sexyswimsuit with dissolve
            "When I walk out to the side of the pool, I see that Reona's beaten out to it."
            "She's sitting on the edge, kicking her legs in the water as she waits."
            reona.say "Hey, [hero.name]..."
            reona.say "Looking good!"
            mike.say "Ah..."
            mike.say "Thanks, Reona..."
            mike.say "You too!"
            "The reason for my pausing before returning the compliment is pretty obvious."
            "Because that's a massive understatement - Reona looks phenomenal!"
            "The swimsuit shows off her body like a dream."
            show reona sexyswimsuit at right with ease
            show jack swimsuit at left with easeinleft
            jack.say "Erm..."
            jack.say "Hi, guys!"
            "Reona and I turn as one to see Jack walking towards the pool."
            "But instead of striding confidently, he's covering himself with a towel."
            "Reona seems to take this as a personal insult."
            "Because she gets up and grabs hold of it with both hands."
            reona.say "Lose the towel, Jack..."
            reona.say "I want to see the merchandise!"
            jack.say "No..."
            jack.say "Stop it!"
            jack.say "Waah!"
            "I watch as together they push and pull, the tumble into the water."
            "Jack pops up first, spluttering and gasping, his towel nowhere to be seen."
            "Then Reona appears beside him, grabbing his belly with both hands."
            reona.say "Mmm..."
            reona.say "Jack, I love a big bear of a guy!"
            jack.say "You...you do?!?"
            "I shake my head as I climb into the water with far less drama."
            reona.say "Hmm..."
            reona.say "I'm a pretty good swimmer, you know?"
            reona.say "Let me show you guys my favourite stroke..."
            "I've just reached Jack and Reona as she says this."
            "Just in time for her to put a hand on each of our groins."
            reona.say "Just let me get hold of something first..."
            hide reona
            show reona double hj jack mikenpc jacknpc pool down mike_close naked
            with fade
            "Jack and I watch in stunned silence as she reaches into our trunks."
            "A feat made all the more impressive as she does it without looking."
            "Then Reona reaches inside, and I feel her fingers close around my cock."
            "She must be doing the exact same thing to Jack too."
            "Because his face has an expression of genuine surprise on it."
            show reona double hj jack onjack
            "And I guess mine must be a perfect mirror image of it right now too!"
            "Of course Reona knows exactly what effect she's having on the two of us."
            show reona double hj jack onmike mouth_lick
            "A quick glance at her face shows me that she's smiling like a Cheshire Cat."
            "And I know the effect she's having on me too."
            "Because I'm already hard as a rock!"
            "My guess is that Jack's in the same position, though I refrain from checking."
            "The reason being that, despite what Reona said, there is such a thing as too weird."
            "Instead I stand still and let her have her way with me."
            "Reona seems to have no problem handling Jack and I at the same time."
            show reona double hj jack speed_jack speed_mike mike_smile jack_smile at startle(0.05,-10)
            "Her hands move up and down in almost perfectly synchronised motions."
            "Plus she knows just when to squeeze and when to ease off too."
            "I'm getting off on the feeling so much that I daren't move a muscle."
            "In fact I don't think I'd move even if my housemates walked in on us right now."
            "The one time that I do move a part of my body is to twist my head around."
            "And I regret that instantly, as my gaze meets Jack's."
            "He's grinning almost as much as Reona is, like he can't believe his luck."
            "But I manage to tear my eyes away before he manages to put me off."
            "Though that seems to have no effect on what's happening down below."
            "Because within mere moments, I can help beginning to pant."
            "I know that I'm about to cum, and I can hear Jack making similar noises too."
            "That means Reona's skilled enough to make sure we both lose it at the same time!"
            "But I don't have any chance to think about that, as things start to speed up."
            show reona double hj jack mikecum jackcum mike_close jack_ahegao -speed_mike -speed_jack with vpunch
            "And before I know it, I feel myself shooting my load."
            with vpunch
            "Reona lets out a filthy giggle as cum floats up to the surface from below."
            with vpunch
            "But all I can do is gasp for breath."
    scene bg bathroom with fade
    "Afterwards, Jack and I go off to separate bathrooms to get cleaned up."
    scene bg livingroom
    show reona normal
    with fade
    "And when we return, Reona is waiting for us, still looking pleased with herself."
    show reona happy
    reona.say "How fun was that, huh?"
    reona.say "I think we make a pretty cute threesome."
    show reona at right with ease
    show jack happy at left with easeinleft
    "Jack hurries to agree with her."
    "Nodding his head like crazy."
    jack.say "Oh yeah, Reona..."
    jack.say "You're so right!"
    jack.say "Erm..."
    jack.say "Maybe we could do it again soon?"
    "Now it's my turn to nod my head."
    "Because I totally agree that this went well."
    "Far better than I ever expected it to."
    mike.say "I'd like that too, Reona."
    mike.say "If you're up for it?"
    show reona flirt
    "Reona adds a third nod to the conversation."
    reona.say "Oh, totally..."
    reona.say "And next time, I think we should do even more!"
    "At this, Jack makes a strange sound, almost like he's having a seizure."
    "And for a moment I think that he might actually pop a vein in his head!"
    "So I guess that's decided then - we're taking this thing to the next level."
    return

label missed_reona_jack_04b(from_cancel=False):
    if not from_cancel:
        "Shit, I missed my date. Reona is going to be mad."
        $ reona.love -= 10
    return

label reona_jack_04b(appointment=None):
    $ DONE["reona_jack_04b"] = game.days_played
    scene bg map with fade
    "I've got to admit that, while I had my misgivings, Reona, Jack and I seemed to get on well the last time we all got together."
    "Well enough that everyone was keen to do it again as soon as the change presented itself."
    "But this time I wanted to make sure that we did it somewhere other than my own home."
    "And that's because it was hard enough to make sure my housemates weren't in the one time."
    "If I start insisting that they clear out all the time, then they're going to get suspicious."
    "Plus the last time, Jack and Reona fled the scene of the crime and left me to clean up!"
    "No, this time I want the date to happen on neutral ground, where I won't be left carrying the can."
    "Wait a minute...is that right?"
    "Is this an actual date?"
    "Oh man, I never thought that I'd be on a date with Jack!"
    "Maybe it'd make more sense if I thought of it as Reona being on a date with the both of us."
    "You know, rather than me being on a date with another guy and one of my best friends?"
    scene bg beach at center, zoomAt(2.25, (0, 1175)) with fade
    "All of this and more is running through my head as we arrive at the beach."
    "So much so that I don't really pay much attention as we're grabbing our stuff from the car."
    show reona normal at center, zoomAt(1.25, (340, 940)) with easeinright
    jack.say "Erm..."
    jack.say "Hello?"
    jack.say "Is anyone actually going to help me out here?!?"
    "Reona and I turn as one to see what the problem is."
    show jack at center, zoomAt(1.25, (940, 940)) with easeinright
    "And we're instantly greeted by the comical sigh of Jack, struggling with most of the stuff."
    "He's tottering this way and that, like he's going to drop something any second."
    "It's such a ridiculous image that I can't help laughing."
    show reona happy at startle
    "And pretty soon, Reona joins in too."
    reona.say "What are you waiting for, [hero.name]?"
    reona.say "Aren't you going to help him?"
    "I look at Jack and then in the direction of the beach."
    mike.say "You know what, Reona..."
    mike.say "I bet we could make a dash for the beach."
    mike.say "And he'd never be able to catch us."
    show reona interested
    "Reona looks at me in kind of an odd way."
    "Like part of her is shocked I'd suggest such a thing."
    "But another part of her is intrigued by the mischief we could cause."
    menu:
        "Run away from Jack with Reona":
            "Without another word, I turn my back on Jack."
            hide reona
            hide jack
            with dissolve
            show bg beach at center, traveling(2.0, 1.0, (340, 1075))
            "And then I start to run down the path towards the beach."
            "As I do so, I can hear two things going on behind me."
            "The first is the sound of Reona running to keep up."
            "And of course the second is Jack starting to protest."
            jack.say "Hey!"
            jack.say "Where are you going?"
            jack.say "Get back here, you pair of jerks!"
            "I don't stop or look back, I just keep on running."
            "Pounding down the path until I reach the sand."
            scene bg beach with fade
            "Then I turn and allow myself to watch the fun."
            show reona at center, zoomAt(1.0, (1140, 720)) with easeinright
            show reona at center, traveling(1.5, 0.5, (340, 1040))
            "Reona arrives by my side a few moments later."
            show jack angry blush at center, zoomAt(1.0, (1140, 720)) with easeinright
            show jack at center, traveling(1.5, 1.0, (940, 1040))
            "And together we watch Jack as he comes puffing and panting after us."
            show jack surprised
            jack.say "Urgh..."
            jack.say "Argh..."
            jack.say "I'm gonna...gonna die!"
            "Jack drops all of the stuff on the sand in front of himself."
            show jack at center, zoomAt(1.5, (940, 1440)) with MoveTransition(0.2)
            pause 0.2
            show jack at center, zoomAt(1.0, (940, 1440)), vshake
            "And then he collapses onto his hands and knees, gasping for breath."
            jack.say "That was...so mean..."
            jack.say "You know I'm...out of shape!"
        "Take some of the stuff from Jack":
            "I walk over to where Jack's standing and take some of his burden."
            "But I'm careful not to get too close or leave the choice to him."
            "Because I know how easy it would be to dump the lot onto me."
            "And once I'm happy with what I'm carrying, I turn to walk down to the beach."
            show jack sad
            jack.say "Urgh..."
            jack.say "You could have..."
            jack.say "Could have...carried more!"
            "I shake my head at Jack's complaining."
            mike.say "I reckon I'm carrying more than you, Jack!"
            mike.say "Maybe if you went to the gym a little more often..."
            mike.say "Then you'd be able to handle a bit of light lifting."
            scene bg beach with fade
            "Ignoring Jack's complaints, I keep on down the path until I reach the sand."
            "Then I turn, expecting to see him right behind me."
            show reona at center, zoomAt(1.0, (1140, 720)) with easeinright
            show reona at center, traveling(1.5, 0.5, (340, 1040))
            "Reona arrives by my side a few moments later."
            show jack angry blush at center, zoomAt(1.0, (1140, 720)) with easeinright
            show jack at center, traveling(1.5, 1.0, (940, 1040))
            "And together we watch Jack as he comes puffing and panting after us."
            show jack surprised
            jack.say "Urgh..."
            jack.say "Argh..."
            jack.say "I'm gonna...gonna die!"
            "Jack drops all of the stuff he's carrying on the sand in front of himself."
            show jack at center, zoomAt(1.5, (940, 1440)) with MoveTransition(0.2)
            pause 0.2
            show jack at center, zoomAt(1.0, (940, 1440)), vshake
            "And then he collapses onto his hands and knees, gasping for breath."
            jack.say "That was...so mean..."
            jack.say "You know I'm...out of shape!"
        "Help Jack with the stuff":
            "I walk over to where Jack's standing with my arms wide open."
            "More than ready to help out a friend in need."
            mike.say "Let me get some of that for you, buddy!"
            jack.say "Okay, [hero.name]…"
            jack.say "How about all of it?"
            "Before I have the chance to react, Jack leaps into action."
            "Dumping all of the stuff into my arms, he relieves himself of the burden."
            show jack at center, zoomAt(1.25, (140, 940)) with ease
            "And then he starts running off down the path towards the beach."
            mike.say "Jack!"
            mike.say "You asshole!"
            show jack happy
            jack.say "What's that, [hero.name]?"
            jack.say "I can't hear you!"
            jack.say "Come on, Reona..."
            jack.say "Let's go!"
            "Reona looks at me for a moment, like she might stay."
            "But then she shrugs and turns to run after Jack."
            hide reona
            hide jack
            with easeoutleft
            "Which leaves me to lug all of the stuff down to the beach on my own."
            "Though as soon as I shoulder it and get started, it doesn't seem so bad."
            "My guess is that Jack was struggling thanks to his being pretty unfit."
            "And my regular trips to the gym seem to be standing me in good stead."
            scene bg beach
            show reona at center, zoomAt(1.5, (340, 1040))
            show jack angry blush at center, zoomAt(1.5, (940, 1440))
            with fade
            "By the time I make it to the beach, I'm expecting to be met with mockery."
            "To have Jack laughing at me and Reona joining in too."
            "But instead I'm greeted with the sight of Jack down on all fours."
            show jack surprised
            jack.say "Urgh..."
            jack.say "Argh..."
            jack.say "I'm gonna...gonna die!"
            mike.say "Geez..."
            mike.say "What happened to him?"
            show reona devious
            reona.say "I think he gave himself stitch."
            reona.say "You know, from running down the path?"
    show reona normal
    show jack normal at center, zoomAt(1.5, (940, 1040))
    with fade
    "Now that we're all down on the beach with our stuff, we can start getting settled in."
    "I'm liking the spot where we stopped after walking down from the carpark."
    "So I make a point of spreading my towel out on the sand."
    show jack normal at center, zoomAt(1.5, (840, 1040)) with ease
    "But as soon as I do, Jack steps in and picks it up again."
    mike.say "Huh?"
    mike.say "What's the problem, Jack?"
    mike.say "I thought we were going to stay right here?"
    "Jack shakes his head at this and points to a spot further down the beach."
    jack.say "Ah..."
    jack.say "No..."
    jack.say "I think we should go over there."
    show reona guilty
    "Reona's looking in that direction too."
    "And she doesn't seem very impressed with the idea."
    show reona sad
    reona.say "But that's in the shade, Jack!"
    reona.say "We won't get much sun over there."
    "But it seems that Jack's not listening to her protests."
    "Because he's already gathered up his share of the stuff."
    hide jack with easeoutleft
    "And now he's walking over to the spot he pointed out."
    show reona angry at center, zoomAt(1.5, (640, 1040)) with ease
    "Reona looks like she's about to shout after him."
    "But I think I have an idea of what's going on."
    "So I step in to stop her raising her voice."
    mike.say "Reona..."
    mike.say "I think Jack's a little worried about being seen on the beach."
    show reona surprised
    "Reona looks at me like she doesn't really get what I just said."
    reona.say "Well what does that mean?"
    reona.say "Even I'm not that outrageous, [hero.name]."
    reona.say "I might want to get up to some fun stuff later."
    reona.say "But not where everyone else can see us!"
    mike.say "No, Reona..."
    mike.say "I mean Jack's self-conscious about his appearance."
    mike.say "He still thinks the beach is where jocks kick sand in nerd's faces!"
    mike.say "So maybe we just go along with it?"
    show reona annoyed
    "Reona shrugs and then helps me pick up the rest of the stuff."
    scene bg beach
    show jack at center, zoomAt(1.5, (340, 1040))
    with fade
    pause 0.2
    show reona at center, zoomAt(1.5, (940, 1040)) with easeinright
    "Then we walk over to the spot that Jack's chosen."
    jack.say "You see?"
    jack.say "This is going to be much better."
    show jack wink
    "All this gets him is a couple of nonchalant nods."
    "But that seems to be enough to settle the matter."
    hide jack
    hide reona
    with easeoutbottom
    "Once we're happy with how things are set up, everyone settles down on the sand."
    "The weather is great and the beach is really the place to be on a day like this."
    "So it's enough to just lie back and take it all in for a while."
    "Reona's lying in the middle, with Jack and me to either side."
    "And it really feels like we're enjoying a comfortable silence."
    "In fact it seems like some of us are finding it a little too relaxing."
    show reona surprised at center, zoomAt(1.5, (640, 1340)) with easeinbottom
    reona.say "What in the hell is that noise?"
    reona.say "It sounds like some revving up a chainsaw!"
    mike.say "Don't worry, I've heard that before."
    "I prop myself up on my elbows and point in Jack's direction."
    "And sure enough, I see that he's fallen asleep and started snoring."
    reona.say "Does he always make a sound like that?"
    mike.say "Yeah, I'm afraid so!"
    show reona angry
    "I see that Reona's staring at Jack pretty hard."
    "And for a moment I think she's going to poke him in the ribs or something."
    "But then the look on her face seems to change into one of interest."
    show reona surprised
    reona.say "Ooh..."
    reona.say "He must be having some interesting dreams."
    reona.say "Look!"
    "Reona points to Jack's trunks, and I see what she's talking about."
    "Something in there is getting larger by the second!"
    reona.say "You know what..."
    reona.say "That gives me an idea!"
    hide reona
    hide jack
    show reona double hj jack beach swimsuit jacknpc down onjack jack_close
    with fade
    "I watch with interest as Reona sits up and reaches over towards Jack."
    "And then my interest redoubles as I see her slide a hand into his trunks!"
    "Jack groans and shifts a little as all of this is happening, but doesn't stir."
    "I didn't expect him to, as he's notoriously hard to wake up."
    "But I still feel compelled to offer a word of warning to Reona."
    mike.say "Be careful, Reona..."
    mike.say "Don't they say it's dangerous to wake someone up like that?"
    "Reona smiles and shakes her head, dismissing my warning."
    reona.say "Don't be silly, [hero.name]."
    reona.say "That's sleepwalking."
    reona.say "This is sleep-wanking - it's a totally different thing!"
    "I nod at this, only half hearing what Reona's saying."
    "The truth is that I'm way too fascinated with what's happening to Jack."
    show reona double hj jack mikenpc onmike
    "But then I feel the sensation of something squeezing my own cock!"
    mike.say "What the..."
    "Looking down, I see that Reona's managed to do the same thing to me."
    "Her other hand is now down the front of my own trunks!"
    show reona double hj jack down mouth_lick
    reona.say "Did you think I'd leave you out?"
    reona.say "That you wouldn't get to be in on all the fun?"
    "The last thing that I'm sure I hear is the sound of Reona's laughter."
    "Because after that, my senses are flooded with sensations of pure pleasure."
    show reona double hj jack speed_jack speed_mike
    "The technique that Reona uses isn't subtle or even gentle."
    "And who can blame her for that?"
    "She's handling two guys at the same time."
    "One of them still being asleep!"
    "But all the same, it gets the job done nicely."
    show reona double hj jack onjack
    "Pretty soon I can hear the sound of Jack groaning away as Reona works at him."
    "Or maybe that's me - it's hard to tell what's coming from where right now."
    "And I'm glad that we decided to let Jack have his way and settle here."
    "Because there's no way Reona could have gotten away with this at a busier place on the beach."
    "Especially now that she's managed to get both cocks out into the open!"
    show reona double hj jack onmike
    "Reona looks from one side to the other, smiling at the results of her labours."
    "But all I can do is lean back on the sand, as its effects overtake me."
    "A moment later it becomes too much for me to bear."
    show reona double hj jack up -speed_mike mikecum open tongueout with vpunch
    "And I slum down onto my back as I feel myself starting to cum."
    "Once I'm done, Reona leaves me to recover as best I can."
    show reona double hj jack down onjack jackcum
    "And she turns her attentions to Jack instead."
    show reona double hj -speed_jack jackcum with vpunch
    "I don't actually see what happens at the end."
    "But once I'm able, I look over and see her tucking him back into his trunks."

    hide reona
    show reona happy leftback rightok at center, zoomAt(1.5, (340, 1340))
    with fade
    "Reona holds a finger to her lips, urging me to keep quiet."
    "Then we both set about acting like nothing actually happened."
    show reona happy rightnormal
    "I'm amazed that Jack was able to sleep through all of that."
    show jack happy at center, zoomAt(1.5, (940, 1340)) with easeinbottom
    "But once he wakes up, I can't help grinning at the fallout."
    show jack wink
    jack.say "Huh..."
    jack.say "I must have fallen asleep."
    jack.say "Because I had the strangest dream!"
    jack.say "I dreamed that Reona was..."
    show jack surprised
    "All of a sudden, Jack's expression changes to one of genuine surprise."
    show jack blush
    "He lifts the waistband of his trunks, and his eyes go wide at what he sees."
    show reona flirt
    reona.say "What is it, Jack?"
    mike.say "Yeah, buddy..."
    mike.say "Are you okay?"
    jack.say "I...I'm fine..."
    jack.say "I just need to cool off in the sea..."
    jack.say "Right now!"
    "Reona and I watch as Jack sprints to the water and wades in up to his waist."
    "It's pretty obvious he thinks he had an accident while he was dozing."
    "And neither of us is going to explain what actually happened to him."
    "Because that's enough to keep us entertained for the rest of the date."
    "And maybe the one after that too!"
    return

label reona_jack_05b:
    "Today just seems to be one of those days when the stars have aligned and everything's just worked out perfectly."
    "I've got the house to myself for most of the day, so the plan for me was going to be that there is no plan."
    "All I wanted to do was hang-out on my own, maybe watch some TV or play on the Z-Box, if I could be bothered."
    play sound cell_vibrate
    "But I've only been slobbing on the sofa in the sitting room for what feels like a few minutes when my phone rings."
    $ result = renpy.call_screen("smartphone_choice", "Reona")
    if not result:
        $ reona.love -= 5
        $ reona.sub -= 2
        $ hero.cancel_event()
        return
    "So I idly pick it up and answer the call, not even bothering to check who's on the other end."
    mike.say "Hey..."
    mike.say "What's up?"
    reona.say "Hey, [hero.name]…"
    reona.say "It's me, Reona!"
    "The sound of Reona's voice is more than enough to begin stirring me from my state of lethargy."
    "Maybe not enough to make me leap up off of the sofa, but it certainly wakes me up a little."
    mike.say "Hi, Reona..."
    mike.say "Great to hear your voice!"
    mike.say "What can I do for you?"
    reona.say "Oh, nothing much..."
    "Reona's tone is light and casual, as we're just chatting about nothing in particular."
    reona.say "I was just wondering what you were doing right now."
    reona.say "I'm doing precisely nothing, and I'm pretty bored!"
    "Now there's an offer that I'm not about to let pass me by."
    "I can almost feel the energy returning to my limbs as she says this."
    "But I don't want to seem desperate, so I try to play it cool."
    mike.say "Well..."
    mike.say "I don't have any concrete plans for the day."
    mike.say "So I guess you could come over here, if you want?"
    "Reona doesn't hesitate to reply to my offer."
    reona.say "That sounds great, [hero.name]!"
    reona.say "So...are you going to come and let me in, or what?"
    "I find myself frowning in confusion at the question."
    mike.say "What are you talking about, Reona?"
    mike.say "Just ring the bell when you get here."
    mike.say "I'll let you in then."
    play sound door_bell
    "The very moment I finish saying all of this, I hear the doorbell ring."
    mike.say "Wait..."
    mike.say "Are you..."
    reona.say "Yeah, I'm at the front-door..."
    reona.say "Hurry up and let me in!"
    "Reona ends the call as I begin dragging myself up off of the sofa."
    "I'm still pretty confused as to what's going on here."
    "And the best sense I can make of it all is that she was out there all the time."
    "God knows why she didn't just ring the bell in the first place!"
    scene bg black with dissolve
    pause 0.1
    scene bg house
    show reona happy leftback
    with wiperight
    "I open the door to be greeted with the sight of Reona on the porch."
    "And that does a great deal to make me forget about all of the previous weirdness."
    show reona rightpeace leftpeace
    reona.say "Here I am!"
    mike.say "Yeah, there you are!"
    reona.say "So..."
    reona.say "Can I come in?"
    mike.say "Sure, sure..."
    "I step back, letting Reona into the hallway."
    hide reona with easeoutleft
    "And once she's inside, I make to close the door and follow her."
    play sound cell_vibrate
    "But as I do so, my phone starts to ring again."
    "At first I think that it's going to be Reona."
    play sound cell_vibrate
    "Hell, she called me from the other side of the door just now."
    "So why not call me from another room of the house?"
    $ renpy.show(f"{hero.layered_image()} p down")
    "But when I look at the name on the screen, I see that it's actually Jack."
    "Pausing in the hallway, I decide to take the call and get it over with."
    $ renpy.show(f"{hero.layered_image()} p speak")
    mike.say "Hey, Jack..."
    jack.say "Hey, man..."
    jack.say "Are you..."
    mike.say "Sorry, Jack..."
    mike.say "I can't talk right now."
    mike.say "Reona just came over and I need to entertain her."
    mike.say "You know how it is!"
    "I'm expecting that to end the conversation, for Jack to leave me in peace."
    "But instead he presses on, pretty much ignoring me."
    jack.say "She did?"
    jack.say "That's great, because I wanted to come over too!"
    jack.say "We got on so well the last time we were all together."
    jack.say "I think we should all hang-out again."
    mike.say "Ah..."
    mike.say "I don't know about that, Jack..."
    mike.say "Reona's here right now."
    mike.say "And it could take you a while to get over here..."
    jack.say "No need to worry about that."
    jack.say "I'm right over here, look!"
    scene bg house with fade
    play sound hitting_bushes
    "I hear the sound of rustling coming from the nearby bushes."
    "And then I watch in amazement as Jack emerges from amongst them."
    "He sprints across the lawn and onto the patio, then into the hallway."
    show jack with dissolve
    mike.say "Wait a minute..."
    mike.say "Were you..."
    mike.say "Were you hiding in the undergrowth?!?"
    show jack surprised
    jack.say "No!"
    jack.say "I was just...erm..."
    jack.say "I was on a trek through the wilderness and I somehow ended up in there by mistake!"
    "I'm about to call bullshit on that explanation."
    "But then I hear Reona calling me from the sitting-room."
    reona.say "Hey!"
    reona.say "What's with the hold-up?"
    hide jack with easeoutleft
    "Before I can say a word, Jack hurries past me."
    "And he's already calling out to Reona too!"
    jack.say "Hey, Reona..."
    jack.say "It's just me..."
    jack.say "It's just Jack..."
    "Suddenly Jack stops speaking, and that can only mean something is wrong."
    "I chase after him and come to a halt in the doorway to the sitting-room."
    scene bg livingroom
    show reona naked leftback at left
    show jack perv at center, zoomAt (1.0, (1040, 720))
    with fade
    "Which is where I see Jack standing with his mouth hanging open."
    "And Reona staring back at us both, totally naked!"
    reona.say "Oh, hey, Jack!"
    reona.say "Are you going to be joining in too?"
    show jack at center, traveling (1.25, 0.3, (840, 880))
    "At this, Jack turns to me with an eager look on his face."
    jack.say "Oh boy, [hero.name]!"
    jack.say "I sure hope that I can?"
    mike.say "Can he, Reona?"
    mike.say "I mean, this is the first I knew about us getting it on!"
    show reona devious at startle
    "Reona shakes her head at this and lets out a peal of laughter."
    reona.say "Well we do have the place to ourselves."
    reona.say "So what else were you thinking I wanted to do?"
    "My suspicions are growing by the second."
    "And I'm starting to think that these two were actually staking out my house!"
    "But then it hits me like a bolt of lightning - why in the hell would I care?"
    "So what if Reona and Jack were hanging around in the hope of getting some action?"
    "Because I'm also going to be involved in that action myself!"
    "I'm nodding as this revelation hits me."
    "And I'm also pulling off my clothes at the same time."
    mike.say "Whatever..."
    mike.say "Who cares about the details?"
    mike.say "Let's just have some fun!"
    "I hurry into the sitting-room and straight towards Reona."
    "All thought of anything else disappearing from my mind."
    "And I can hear Jack struggling to undress and follow on my heels too."
    show jack naked with dissolve
    jack.say "Wait..."
    jack.say "Wait for me!"
    menu:
        "Fuck Reona":
            "The fact that I make it into the room and to Reona first means I can choose who does what to whom."
            "And since this is my house, I don't see any problem with me being the on that gets to fuck her."
            "With that in mind, I sit down on the sofa and then grab hold of Reona by the haunches."
            hide jack
            hide reona
            show reona threesome mikefuck
            with fade
            "She lets out a squeal of delight at my touch, but does nothing to stop me having my way with her."
            mike.say "Stand back and watch a professional at work, Jack!"
            mike.say "Who knows, you might learn something!"
            "With that, I pull Reona down onto my lap."
            menu:
                "Fuck her pussy":
                    reona.say "Whoa..."
                    reona.say "Here we go, [hero.name]!"
                    reona.say "You'd better give me the ride of my life!"
                    "With Reona's words echoing in my ears, I set about doing just that."
                    "And I'm already aiming my cock squarely at Reona's pussy!"
                    menu:
                        "Use butt-plug":
                            $ used_plug = True
                            "But at the last moment I remember that will leave her ass empty."
                            "Which seems more than a little wasteful to me."
                            "So I decide to take action."
                            mike.say "Jack..."
                            mike.say "Look in that drawer and grab the butt-plug!"
                            "Jack hurries to do as he's told, pulling out the toy in question."
                            "But once he has it, he holds it up as he stares at it in amazement."
                            jack.say "Why'd you have stuff like this in the sitting-room?"
                            mike.say "That doesn't matter right now."
                            mike.say "Just get over here and use it already!"
                            show reona threesome mikefuck plug
                            "Jack hurries to obey, thrusting the toy between Reona's thighs."
                            "I watch as he works it into her ass, not stopping until it's all the way in."
                            show reona threesome mikefuck mouth_moan
                            "And I can hear Reona moaning the whole time."
                            reona.say "Mmm..."
                            reona.say "Oh yeah..."
                            reona.say "That feels so good!"
                        "Do not use toys":
                            $ used_plug = False
                            "I think about using the toys I have stashed in a convenient drawer."
                            "But then that kind of feels like cheating, especially in front of Jack."
                            "So I resolve to do without them, and get right down to business."
                    "Sliding my hands under Reona's knees, I hoist her into the air."
                    "And when I begin to lower her down again, my cock in perfect position."
                    show reona threesome mikefuck up mouth_normal
                    "This means that her pussy comes right down on the head, pressing against her lips."
                    "I was expecting to have to do quite a bit of work at this stage."
                    "To have to tease Reona's pussy until it finally opened up to me."
                    "But she must have been more aroused than I thought."
                    "Because I can already feel the tip sliding around her folds."
                    "Which means that she's slick and anticipating what comes next."
                    "Reona's also helping me out by doing all she can to push downwards too."
                    "This means that what I had planned as a smooth effort on my part becomes impossible."
                    "And what replaces it is a crazy free-for-all as we both try to get things started."
                    "But this comes to an end almost as quickly as it begins."
                    "Reona's pussy only gets wetter and more willing as time goes on."
                    show reona threesome mikefuck vaginal mouth_hurt eyes_open
                    "Until, without warning, the head of my cock sinks into her."
                    "As soon as this happens, everything changes."
                    "Now that there's no more need to struggle, we're both pulling for the same goal."
                    show reona threesome mikefuck at startle(0.05,-10)
                    "Reona pushes down from above as I push up from below."
                    "And in one smooth motion, we keep on going until I can go no further."
                    "What follows is a pause that seems to go on forever."
                    "Myself enjoying the sensation of being buried deep inside of Reona."
                    "And her savouring the feeling of her pussy being filled by my cock."
                    "But in reality, it could only have lasted for a few mere seconds."
                    show reona threesome mikefuck at startle(0.05,-10)
                    "Because the next moment sees me bouncing Reona up and down on my lap."
                    show reona threesome mikefuck mouth_moan eyes_close at startle(0.05,-10)
                    "She moans and pants as she rides my cock, unable to do anything but take it."
                    "I'm leaning back as far as I can go right now."
                    show reona threesome mikefuck at startle(0.05,-10)
                    "And Reona's practically draped over me like I'm a human recliner."
                    "Somehow she's still managing to keep her head up."
                    show reona threesome mikefuck jack
                    "But any moment I'm expecting it to fall backwards."
                    jack.say "Oh boy, oh boy, oh boy!"
                    jack.say "This is SO hot..."
                    jack.say "I can't believe we're actually doing this!"
                    show reona threesome mikefuck hand_jack
                    "The sound of Jack's voice serves to bring me back to reality."
                    "And while I'm not about to let him put me off, it's still a distraction."
                    "I'm about to open my mouth and say something to him."
                    show reona threesome mikefuck eyes_open mouth_normal
                    "But then I notice that Reona's already taken the matter into her own hands."
                    "Or to be more accurate, out of Jack's."
                    "I see that he was standing there with his dick in his hand."
                    "Probably making a half-hearted effort to get himself off."
                    "But now Reona's grabbed hold of it."
                    "And she's pulling it towards her lips!"
                    show reona threesome mikefuck mouth_moan
                    reona.say "Give me that thing..."
                    reona.say "Before you..."
                    reona.say "Hurt yourself!"
                    show reona threesome mikefuck mouth_normal
                    "I watch as Reona gives Jack's cock a hard tug."
                    "Of course he has no choice but to follow it."
                    show reona threesome mikefuck blow -hand_jack
                    "And as soon as he's close enough, she shoves it straight between her lips."
                    "Jack gasps, both in amazement and from the sensations he must be feeling."
                    "I watch as his eyes kind of glaze over, and he succumbs to Reona's efforts."
                    "Which leaves me alone to finish off the job that I started."
                    if used_plug:
                        show reona threesome mikefuck down
                        "I figure that the butt-plug I had Jack put in Reona's ass can help me get that done."
                        show reona threesome mikefuck analgape mouth_hurt eyes_open normal -plug
                        "So I use one hand to reach down and take hold of it, as firmly as I can."
                        "And then I yank the thing out in one motion, with a comical popping sound."
                        show reona threesome mikefuck vaginal blow
                        "Reona moans and I can already feel her starting to squeeze my cock hard."
                        "All of which means that she's going to cum within seconds!"
                    else:
                        "So using the last of my strength, I pick up speed."
                        "Reona moans and I can already feel her starting to squeeze my cock hard."
                        "All of which means that she's going to cum within seconds!"
                    show reona threesome mikefuck mouth_moan
                    "It's all I can do to hold onto Reona as she begins to lose it."
                    "And I know that I have to make a decision pretty quickly."
                    "I need to decide how this is going to end!"
                    menu:
                        "Cum inside":
                            "I strengthen my hold on Reona, determined to keep her where I want her."
                            with vpunch
                            "That's because a moment later I lose it, shooting my load into her."
                            show reona threesome mikefuck mikecum bodycum orgasm fx
                            with vpunch
                            with vpunch
                            "Reona lets go of Jack's cock, throwing her head back."
                            with vpunch
                            "And she quivers from head to toe as we both cum one after the other."
                        "Pull out":
                            "I strengthen my hold on Reona, but at the same time I'm moving beneath her."
                            with vpunch
                            "At the last possible moment, I manage to pull my cock out of her."
                            show reona threesome mikefuck up mikecum bodycum orgasm fx
                            with vpunch
                            with vpunch
                            "Reona lets go of Jack's cock, throwing her head back."
                            with vpunch
                            "And she quivers from head to toe as I shoot my load over her belly."
                        "Let Reona finish you off":
                            call reona_jack_05b_hj_finish from _call_reona_jack_05b_hj_finish
                "Fuck her ass":
                    reona.say "Whoa..."
                    reona.say "Here we go, [hero.name]!"
                    reona.say "You'd better give me the ride of my life!"
                    "With Reona's words echoing in my ears, I set about doing just that."
                    "And I'm already aiming my cock squarely at Reona's ass!"
                    menu:
                        "Use pleasure beads":
                            $ used_beads = True
                            "But at the last moment I remember that will leave her pussy empty."
                            "Which seems more than a little wasteful to me."
                            "So I decide to take action."
                            mike.say "Jack..."
                            mike.say "Look in that drawer and grab the pleasure beads!"
                            "Jack hurries to do as he's told, pulling out the toy in question."
                            "But once he has it, he holds it up as he stares at it in amazement."
                            jack.say "Why'd you have stuff like this in the sitting-room?"
                            mike.say "That doesn't matter right now."
                            mike.say "Just get over here and use it already!"
                            show reona threesome mikefuck beads
                            "Jack hurries to obey, thrusting the toy between Reona's thighs."
                            "I watch as he works each bead into her pussy, not stopping until they're all up there."
                            show reona threesome mikefuck mouth_moan eyes_close
                            "And I can hear Reona moaning the whole time."
                            reona.say "Mmm..."
                            reona.say "Oh yeah..."
                            reona.say "That feels so good!"
                        "Do not use toys":
                            $ used_beads = False
                            "I think about using the toys I have stashed in a convenient drawer."
                            "But then that kind of feels like cheating, especially in front of Jack."
                            "So I resolve to do without them, and get right down to business."
                    "Sliding my hands under Reona's knees, I hoist her into the air."
                    "And when I begin to lower her down again, my cock in perfect position."
                    show reona threesome mikefuck up mouth_normal
                    "This means that her ass comes right down on the head, pressing against her hole."
                    "I was expecting to have to do quite a bit of work at this stage."
                    "To have to tease Reona's ass until it finally opened up to me."
                    show reona threesome mikefuck anal eyes_open mouth_hurt fx
                    "But she must have been more aroused than I thought."
                    "Because I can already feel the tip sliding around her hole."
                    "Which means that she's slick and anticipating what comes next."
                    "Reona's also helping me out by doing all she can to push downwards too."
                    "This means that what I had planned as a smooth effort on my part becomes impossible."
                    "And what replaces it is a crazy free-for-all as we both try to get things started."
                    "But this comes to an end almost as quickly as it begins."
                    "Reona's ass only gets wetter and more willing as time goes on."
                    "Until, without warning, the head of my cock sinks into her."
                    "As soon as this happens, everything changes."
                    "Now that there's no more need to struggle, we're both pulling for the same goal."
                    show reona threesome mikefuck at startle(0.05,-10)
                    "Reona pushes down from above as I push up from below."
                    "And in one smooth motion, we keep on going until I can go no further."
                    "What follows is a pause that seems to go on forever."
                    "Myself enjoying the sensation of being buried deep inside of Reona."
                    "And her savouring the feeling of her pussy being filled by my cock."
                    "But in reality, it could only have lasted for a few mere seconds."
                    show reona threesome mikefuck at startle(0.05,-10)
                    "Because the next moment sees me bouncing Reona up and down on my lap."
                    show reona threesome mikefuck mouth_moan eyes_open at startle(0.05,-10)
                    "She moans and pants as she rides my cock, unable to do anything but take it."
                    "I'm leaning back as far as I can go right now."
                    show reona threesome mikefuck at startle(0.05,-10)
                    "And Reona's practically draped over me like I'm a human recliner."
                    "Somehow she's still managing to keep her head up."
                    show reona threesome mikefuck jack
                    "But any moment I'm expecting it to fall backwards."
                    show reona threesome mikefuck hand_jack
                    jack.say "Oh boy, oh boy, oh boy!"
                    jack.say "This is SO hot..."
                    jack.say "I can't believe we're actually doing this!"
                    "The sound of Jack's voice serves to bring me back to reality."
                    "And while I'm not about to let him put me off, it's still a distraction."
                    "I'm about to open my mouth and say something to him."
                    show reona threesome mikefuck eyes_open mouth_normal
                    "But then I notice that Reona's already taken the matter into her own hands."
                    "Or to be more accurate, out of Jack's."
                    "I see that he was standing there with his dick in his hand."
                    "Probably making a half-hearted effort to get himself off."
                    "But now Reona's grabbed hold of it."
                    "And she's pulling it towards her lips!"
                    show reona threesome mikefuck mouth_moan
                    reona.say "Give me that thing..."
                    reona.say "Before you..."
                    reona.say "Hurt yourself!"
                    show reona threesome mikefuck mouth_normal
                    "I watch as Reona gives Jack's cock a hard tug."
                    "Of course he has no choice but to follow it."
                    show reona threesome mikefuck blow -hand_jack
                    "And as soon as he's close enough, she shoves it straight between her lips."
                    "Jack gasps, both in amazement and from the sensations he must be feeling."
                    "I watch as his eyes kind of glaze over, and he succumbs to Reona's efforts."
                    "Which leaves me alone to finish off the job that I started."
                    if used_beads:
                        "I figure that the pleasure beads I had Jack put in Reona's pussy can help me get that done."
                        show reona threesome mikefuck pulled mouth_hurt eyes_open normal
                        "So I use one hand to reach down and take hold of the end of the string, as firmly as I can."
                        "And then I yank the thing out in one motion, with a comical popping sound."
                        "Reona moans and I can already feel her starting to squeeze my cock hard."
                        show reona threesome mikefuck blow
                        "All of which means that she's going to cum within seconds!"
                    else:
                        "So using the last of my strength, I pick up speed."
                        "Reona moans and I can already feel her starting to squeeze my cock hard."
                        "All of which means that she's going to cum within seconds!"
                    "It's all I can do to hold onto Reona as she begins to lose it."
                    "And I know that I have to make a decision pretty quickly."
                    "I need to decide how this is going to end!"
                    menu:
                        "Cum inside":
                            with vpunch
                            "I strengthen my hold on Reona, determined to keep her where I want her."
                            show reona threesome mikefuck orgasm mikecum bodycum
                            with vpunch
                            with vpunch
                            "That's because a moment later I lose it, shooting my load into her."
                            with vpunch
                            "Reona lets go of Jack's cock, throwing her head back."
                            "And she quivers from head to toe as we both cum one after the other."
                        "Pull out":
                            with vpunch
                            "I strengthen my hold on Reona, but at the same time I'm moving beneath her."
                            show reona threesome mikefuck orgasm up mikecum bodycum
                            with vpunch
                            with vpunch
                            "At the last possible moment, I manage to pull my cock out of her."
                            with vpunch
                            "Reona lets go of Jack's cock, throwing her head back."
                            "And she quivers from head to toe as I shoot my load over her belly."
                        "Let Reona finish you off":
                            call reona_jack_05b_hj_finish from _call_reona_jack_05b_hj_finish_1
        "Let Jack fucks Reona":
            "The fact that I make it into the room and to Reona first means I can choose who does what to whom."
            "And for some reason I feel a wave of generosity sweep over me as I come to make the decision."
            "So as Reona lies back on the sofa, waiting to see where this is going, I step aside and motion to Jack."
            mike.say "You want to take this one, buddy?"
            show jack surprised
            "For a moment, Jack doesn't seem to understand what I mean."
            "He looks from me to Reona and then back again."
            "And as he does so, recognition seems to glimmer in his eyes."
            jack.say "Are..."
            jack.say "Are you serious?"
            jack.say "Of course I do!"
            "Jack almost leaps in the air as he hurries towards the sofa."
            "And his enthusiasm is infectious, as Reona starts to chuckle too."
            hide jack
            hide reona
            show reona threesome jackfuck jack
            "She rolls onto her side as Jack reaches the end of the sofa."
            "Then she wiggles her ass in his general direction."
            "An obvious signal that she's ready for him."
            "But rather than getting on with it, Jack looks at me for instruction."
            jack.say "Erm..."
            jack.say "Where should I put it?"
            menu:
                "Tell Jack to fuck Reona's pussy":
                    mike.say "For god's sake, Jack!"
                    mike.say "You need me to wipe your ass for you too?"
                    mike.say "Just keep things simple and aim for the pussy, okay?"
                    "This little chewing out seems to do the trick."
                    "Jack nods his head as he leaps into action."
                    "I watch as he lifts one of Reona's thighs and spreads her legs."
                    "Then he starts to rub the head of his cock against her exposed pussy."
                    "The truth is that I'm now worried about Jack being able to hack it."
                    "That his nerves are going to get the better of him and ruin his performance."
                    "But from the look on Reona's face, she's not at all frustrated."
                    "Instead his bumbling seems to be amusing her, as there's a smile on her face."
                    "It's as I watch them interact that I realise I'm just standing around doing nothing."
                    show reona threesome jackfuck mike
                    "I've gone to all the trouble of getting naked, and I can feel myself getting hard."
                    "But I've already gone and handed the staring role to Jack."
                    "It's while I'm waiting for inspiration to strike that Jack hits his stride."
                    "Reona's laid on the sofa, propping herself up on her shoulder."
                    "And I confess that I've been paying more attention to her than Jack."
                    show reona threesome jackfuck jack_vaginal eyes_lookback
                    "So when I see her almost go cross-eyed and her jaw drop, I know something just happened."
                    jack.say "Oh man..."
                    jack.say "Oh wow..."
                    jack.say "Oh fuck - I'm in!"
                    "And with that, Jack's away, thrusting in and out of Reona like his life depends on it."
                    "What he lacks for in technique, he definitely makes up for in sheer enthusiasm."
                    show reona threesome jackfuck eyes_close
                    "And it seems to be working too, because Reona's eyes are starting to glaze over."
                    "Her entire body is moving in sympathy with Jack's efforts too."
                    "Thighs slapping against his and breasts swaying from side to side."
                    "And by that I do mean Reona's magnificent breasts."
                    "Not Jack's man-boobs!"
                    reona.say "Why are you..."
                    reona.say "Just standing there..."
                    reona.say "[hero.name]?"
                    "Reona's words come on bursts of two or three."
                    "And that's because she's being fucked pretty hard right now."
                    "But they also take me by surprise."
                    "Because I was sure that she was out of it."
                    show reona threesome jackfuck turn eyes_opened
                    "I open my mouth, thinking to offer up some witty response."
                    show reona threesome jackfuck handjob mouth_ahegao
                    pause 0.2
                    show reona threesome jackfuck forth
                    pause 0.2
                    show reona threesome jackfuck back
                    pause 0.2
                    show reona threesome jackfuck forth
                    pause 0.2
                    show reona threesome jackfuck back
                    pause 0.2
                    show reona threesome jackfuck forth
                    pause 0.2
                    show reona threesome jackfuck back
                    "But before I can do that, Reona opens hers."
                    "And then her head darts forwards."
                    show reona threesome jackfuck blow eyes_close
                    "Before I know what's happening, she has my cock in her mouth."
                    "She begins working it with her lips, tongue and teeth."
                    "And any objections I might have had simply vanish without a trace."
                    "All I can do is stand there and let Reona have her way with me."
                    "Every second that I'm in her mouth, I can feel the end coming closer."
                    "The moment when I won't be able to hold on any longer approaching."
                    "But I can also feel the way Reona's moving too."
                    "And if I had to guess, I'd say that she's even closer than me."
                    "Then a thought occurs to me."
                    "That I might be able to have a hand in making it happen."
                    "So using the last of my strength, I push myself further into Reona's mouth."
                    "Reona moans and I can already feel her starting to squeeze my cock hard."
                    "All of which means that she's going to cum within seconds!"
                    jack.say "Urgh..."
                    jack.say "[hero.name]..."
                    jack.say "What do I do?!?"
                    "I can't believe what I'm hearing."
                    "Is he actually asking me how to end it?"
                    menu:
                        "Inside Jack!!":
                            mike.say "Keep going, you twat!"
                            mike.say "Keep going!"
                            with hpunch
                            "I strengthen my hold on Reona, determined to keep her where I want her."
                            show reona threesome jackfuck normal eyes_ahegao mikecum jackcum facecum bodycum_top -blow
                            with hpunch
                            with hpunch
                            "That's because a moment later Jack loses it, shooting his load into her."
                            "Reona lets go of my cock, throwing her head back."
                            "And she quivers from head to toe as they both cum one after the other."
                        "Pull out Jack!!":
                            mike.say "Pull out, you twat!"
                            mike.say "Pull out right now!"
                            with hpunch
                            "I strengthen my hold on Reona, but at the same time I'm moving beneath her."
                            show reona threesome jackfuck jack_out normal eyes_ahegao mikecum jackcum facecum bodycum_bot bodycum_top -blow
                            with hpunch
                            with hpunch
                            "At the last possible moment, Jack manages to pull his cock out of her."
                            with hpunch
                            "Reona lets go of my cock, throwing her head back."
                            "And she quivers from head to toe as Jack shoots his load over her belly."
                        "Let Reona finish you off":
                            call reona_jack_05b_hj_finish from _call_reona_jack_05b_hj_finish_2
                "Tell Jack to fuck Reona's ass":
                    mike.say "For god's sake, Jack!"
                    mike.say "You need me to chew your food for you too?"
                    mike.say "Just keep things simple and aim for the ass, okay?"
                    "This little chewing out seems to do the trick."
                    "Jack nods his head as he leaps into action."
                    "I watch as he lifts one of Reona's thighs and spreads her legs."
                    "Then he starts to rub the head of his cock against her exposed hole."
                    "The truth is that I'm now worried about Jack being able to hack it."
                    "That his nerves are going to get the better of him and ruin his performance."
                    "But from the look on Reona's face, she's not at all frustrated."
                    "Instead his bumbling seems to be amusing her, as there's a smile on her face."
                    show reona threesome jackfuck mike
                    "It's as I watch them interact that I realise I'm just standing around doing nothing."
                    "I've gone to all the trouble of getting naked, and I can feel myself getting hard."
                    "But I've already gone and handed the staring role to Jack."
                    "I think about using the toys I have stashed in a convenient drawer."
                    "But then that kind of feels like cheating, especially when Jack's taking the lead."
                    "So I resolve to do without them, and look for another way to get involved."
                    "It's while I'm waiting for inspiration to strike that Jack hits his stride."
                    "Reona's laid on the sofa, propping herself up on her shoulder."
                    "And I confess that I've been paying more attention to her than Jack."
                    show reona threesome jackfuck jack_anal eyes_open
                    "So when I see her almost go cross-eyed and her jaw drop, I know something just happened."
                    jack.say "Oh man..."
                    jack.say "Oh wow..."
                    jack.say "Oh fuck - I'm in!"
                    "And with that, Jack's away, thrusting in and out of Reona like his life depends on it."
                    "What he lacks for in technique, he definitely makes up for in sheer enthusiasm."
                    "And it seems to be working too, because Reona's eyes are starting to glaze over."
                    "Her entire body is moving in sympathy with Jack's efforts too."
                    "Thighs slapping against his and breasts swaying from side to side."
                    "And by that I do mean Reona's magnificent breasts."
                    "Not Jack's man-boobs!"
                    reona.say "Why are you..."
                    reona.say "Just standing there..."
                    reona.say "[hero.name]?"
                    "Reona's words come on bursts of two or three."
                    "And that's because she's being fucked pretty hard right now."
                    "But they also take me by surprise."
                    "Because I was sure that she was out of it."
                    show reona threesome jackfuck turn eyes_opened
                    "I open my mouth, thinking to offer up some witty response."
                    show reona threesome jackfuck handjob mouth_ahegao
                    pause 0.2
                    show reona threesome jackfuck forth
                    pause 0.2
                    show reona threesome jackfuck back
                    pause 0.2
                    show reona threesome jackfuck forth
                    pause 0.2
                    show reona threesome jackfuck back
                    pause 0.2
                    show reona threesome jackfuck forth
                    pause 0.2
                    show reona threesome jackfuck back
                    "But before I can do that, Reona opens hers."
                    "And then her head darts forwards."
                    "Before I know what's happening, she has my cock in her mouth."
                    "She begins working it with her lips, tongue and teeth."
                    "And any objections I might have had simply vanish without a trace."
                    "All I can do is stand there and let Reona have her way with me."
                    "Every second that I'm in her mouth, I can feel the end coming closer."
                    "The moment when I won't be able to hold on any longer approaching."
                    "But I can also feel the way Reona's moving too."
                    "And if I had to guess, I'd say that she's even closer than me."
                    "Then a thought occurs to me."
                    "That I might be able to have a hand in making it happen."
                    "So using the last of my strength, I push myself further into Reona's mouth."
                    "Reona moans and I can already feel her starting to squeeze my cock hard."
                    "All of which means that she's going to cum within seconds!"
                    jack.say "Urgh..."
                    jack.say "[hero.name]..."
                    jack.say "What do I do?!?"
                    "I can't believe what I'm hearing."
                    "Is he actually asking me how to end it?"
                    menu:
                        "Inside Jack!!":
                            mike.say "Keep going, you twat!"
                            with hpunch
                            mike.say "Keep going!"
                            with hpunch
                            "I strengthen my hold on Reona, determined to keep her where I want her."
                            show reona threesome jackfuck normal eyes_ahegao mikecum jackcum facecum bodycum_top -blow
                            with hpunch
                            with hpunch
                            "That's because a moment later Jack loses it, shooting his load into her."
                            "Reona lets go of my cock, throwing her head back."
                            "And she quivers from head to toe as they both cum one after the other."
                        "Pull out Jack!!":
                            mike.say "Pull out, you twat!"
                            mike.say "Pull out right now!"
                            with hpunch
                            "I strengthen my hold on Reona, but at the same time I'm moving beneath her."
                            show reona threesome jackfuck jack_out normal eyes_ahegao mikecum jackcum facecum bodycum_bot bodycum_top -blow
                            with hpunch
                            with hpunch
                            "At the last possible moment, Jack manages to pull his cock out of her."
                            with hpunch
                            "Reona lets go of my cock, throwing her head back."
                            "And she quivers from head to toe as Jack shoots his load over her belly."
                        "Let Reona finish you off":
                            call reona_jack_05b_hj_finish from _call_reona_jack_05b_hj_finish_3
    show reona happy naked at left5
    show jack happy naked at right5
    with fade
    "Once it's all over, reality settles back over the room and everyone in it."
    "It's not like we start scuttling around in a blind panic to hide the evidence."
    hide reona
    hide jack
    show reona casual leftback at left5
    show jack casual at right5
    with fade
    "More like we move to get dressed at a brisk pace for fear of being discovered."
    "Reona and Jack make polite conversation with me throughout the process."
    hide jack
    hide reona
    with easeoutright
    "But when we're done, they make their excuses and leave through the front door."
    "That means I'm left alone in the house again, just slumped on the sofa watching TV."
    "It feels pretty weird, almost like it was all a dream that I cooked up in my head."
    "One thing's for certain, I'm not going to tell my housemates what just happened."
    "And not out of a sense of embarrassment either."
    "I'm just sure none of them would believe me!"
    $ reona.sexperience += 1
    return

label reona_jack_05b_hj_finish:
    "Just as I'm gearing up to let myself go, Reona leaps into action."
    "This comes as a massive surprise to me, and Jack reacts in the same way too."
    "Up to now, Reona seemed to be taking an almost passive role in what was going on."
    "Sure, she took it upon herself to start using her mouth to dole out pleasure."
    "But apart from that, she's pretty much laid there and taken it."
    hide jack
    hide reona
    show reona double hj jack jacknpc mikenpc jack_smile mike_smile down onjack naked
    with fade
    "Now she's sitting up on the sofa, and she's handling us both at once!"
    "The sense of being stunned continues as Reona works my cock and Jack's."
    "Using her hands, she juggles two guys at once."
    "And it's hard to tell which of us is getting what from one moment to the next."
    "All I know is that the pleasure I'm feeling is building by the second."
    "Pretty soon it's too much for me to take, and I can't hold on any longer."
    "Reona seems to be even more aware of this than I am."
    "She stops almost all of what she's doing and sits back on the sofa."
    show reona double hj jack speed_jack speed_mike mike_close onmike
    "It's only now that I realise Jack is in the exact same position as me."
    "That and the fact Reona has us perfectly lined up for what happens next."
    "Which is that we shoot our loads within mere seconds of each other."
    "This means that Reona is hit from both sides at once."
    show reona double hj jack jackcum jack_ahegao -speed_jack cum_hand_jack with vpunch
    pause 0.5
    show reona double hj jack mikecum up open tongueout mike_close -speed_mike cum_hand_mike with vpunch
    "She's spattered first on one cheek and then on the other."
    "And the whole thing seems to happen in slow motion as I look on."
    "Lines of thick, sticky white cum line her face and run down her cheeks."
    "But all the while it's happening, Reona's smiling and laughing."
    "The delight on Reona's face is as plain to see as the cum itself."
    "And I watch in silent amazement as she licks it from her lips."
    return

label reona_birthday_date_male:
    $ DONE["reona_birthday_date_male"] = game.days_played
    $ game.active_date.clothes = "casual"
    scene bg park
    "I've been enjoying spending time with Reona since Jack introduced me to her."
    "She's fun to be around and always seems to know how to get the most out of life."
    "And yeah, sure - let's talk about the elephant in the room."
    "So, she is more than a little forward when it comes to her more...physical appetites."
    "But is that really such a bad thing?"
    "I mean, if she were a guy, people would just say she was in touch with her own sexuality."
    "And the thing is that I'm convinced there's a lot more to her than that as well."
    "Which is why I jumped on the chance to take Reona out on a date to celebrate her birthday."
    "But the stroke of genius in my plan is that we're not going on a typical date."
    "Oh no - we're going to have a picnic in the park!"
    "Can you think of a more healthy and wholesome way to spend our time together?"
    "I'm sure that Reona won't take long to show her more placid side once we're into it."
    show reona sad at left with easeinleft
    "So when I see her walking towards the gates of the park, I give her a smile and a wave."
    show reona at center with ease
    "But even before she reaches me, I can see that she's not smiling back."
    mike.say "Erm..."
    mike.say "Hey, Reona..."
    mike.say "What's with the long face?"
    show fx anger
    "Reona crosses her arms over her chest."
    "And she cocks her head on one side as she scowls at me."
    show reona angry
    reona.say "It's looking less and less like this is a joke, [hero.name]."
    hide fx
    reona.say "Like, you're not going to shout 'Surprise'..."
    reona.say "And tell me that we're really going to a club or a decent restaurant!"
    "I take a guilty look at the picnic hamper that's clutched in my hands."
    "And I realise that Reona's not kidding around here!"
    if randint(0, 1) == 0:
        menu:
            "Say that everything will be fine":
                "Okay, okay..."
                "I can feel my blood-pressure rising right now."
                "But I have to rise above it and defuse the situation."
                "So I take a deep breath and smile at Reona."
                mike.say "Anyone could take you to a club or a restaurant, Reona."
                mike.say "But how many other guys would serve you up a hand-made picnic lunch?"
                mike.say "I mean, aren't you even a little bit curious as to what's in here?"
                "I lift the lid of the hamper just a little."
                "Not enough for Reona to see what's inside."
                "But more than enough to pique her interest."
                show reona annoyed
                reona.say "Well..."
                reona.say "Yeah, yeah..."
                $ game.active_date.score += 15
                reona.say "I guess that is pretty cool!"
                "Reona still looks a little annoyed."
                "But she lets me lead her into the park all the same."
                "Who knows, maybe this date will work out after all."
            "Be pissy with Reona":
                "Urgh..."
                "We're already getting off to a really bad start here."
                "How can she be so ungrateful?"
                "Especially after all the effort I went to preparing a picnic for us!"
                mike.say "That's a pretty mean thing to say, Reona."
                mike.say "I've put a lot of work into making today special."
                mike.say "Not just throwing money at it!"
                show reona angry
                "Reona rolls her eyes."
                "As if she finds my protests boring in the extreme."
                reona.say "Alright, alright!"
                reona.say "Geez..."
                reona.say "We'll do your stupid picnic, okay?"
                $ game.active_date.score -= 10
                reona.say "Are you happy now?"
                show reona annoyed
                "Obviously I'm far from happy right now."
                "But maybe I can salvage the date before it's too late."
                "So I force a smile onto my face and lead Reona into the park."
    else:
        "Sure, I could just argue the toss with Reona."
        "I could tell her that it sucks she's not into the idea."
        "But maybe there's a better way."
        "A way that makes her change her mind."
        "But still lets her think that it was her idea all along."
        if hero.charm >= 65:
            "I smile and raise an eyebrow at Reona."
            mike.say "Oh come on, Reona..."
            mike.say "You didn't really think we were just going to stroll around the park, did you?"
            show reona angry
            show fx question
            "Reona frowns at this and narrows her eyes."
            "I can see that she doesn't like the implication that she's not picked up on something."
            "But at the same time, she also looks more than a little curious to find out what that thing is."
            show reona angry
            reona.say "Huh?"
            reona.say "What are you talking about?"
            hide fx
            mike.say "The park's a pretty big place, Reona."
            mike.say "There are lots of secluded paths."
            mike.say "Lots of places hidden amongst the trees."
            mike.say "And that's where we can have our picnic - somewhere nobody can find us!"
            show reona happy
            show fx exclamation
            "A look of understanding slowly dawns on Reona's face."
            "And she begins to look more interested in the prospect."
            reona.say "Well why didn't you say that in the first place?"
            hide fx
            show reona flirt
            $ game.active_date.score += 15
            reona.say "When you put it like that, the whole thing sounds much better!"
            "I gesture for Reona to follow me into the park."
            "And much to my relief, she does just that."
        else:
            mike.say "Who knows, Reona..."
            mike.say "If you're really good, you might get a reward."
            mike.say "If you know what I mean?"
            "I make sure to add a suggestive wink to make my meaning clear."
            "But it doesn't seem to have the intended effect on Reona."
            show reona annoyed
            "In fact it has the effect of making her face darken."
            "Letting me know that my words have seriously backfired."
            show reona angry
            reona.say "And what's that supposed to mean, huh?"
            show fx anger
            $ game.active_date.score -= 10
            reona.say "Are you dangling the chance of sex in front of me, [hero.name]?"
            reona.say "Because you think I'm just some cheap slut?"
            hide fx
            mike.say "No, Reona!"
            mike.say "That's not it at all!"
            hide reona with easeoutright
            "Reona turns her back on me and storms off."
            "And I guess it's just my dumb luck that this means she walks straight into the park."
            "So I waste no time in hurrying after her, hoping to be able to make amends."
    scene bg black with dissolve
    pause 1
    scene bg park
    show reona happy at center, zoomAt(1.5, (640, 1040))
    with dissolve
    "Reona and I are soon strolling through the park together."
    "And it seems like the pleasant nature of the place is having an effect on her."
    "Reona's smiling and laughing at my jokes, her mood seeming to have improved."
    "But just then I see a bunch of guys throwing a frisbee around on a wide expanse of grass."
    "I can't help looking at them with a sour expression on my face, which Reona notices."
    show reona surprised
    reona.say "What's up, [hero.name]?"
    reona.say "You got something against frisbees?"
    mike.say "What?"
    mike.say "Oh no, I don't, Reona."
    show reona normal
    mike.say "I just don't seem to have any luck around those things."
    mike.say "In fact, it's kind of like I'm a magnet for them, you know?"
    show reona happy at startle
    "Reona chuckles and shakes her head."
    reona.say "That sounds crazy!"
    "But then I see her instinctively leap aside."
    show reona surprised at hshake
    reona.say "What the hell?!?"
    if randint(0, 1) == 0:
        "I have just enough time to see the frisbee out of the corner of my eye."
        "And I swear that I feel the thing graze the side of my head as it flies by."
        with hpunch
        "I lurch out of the way, and it hits the ground a few feet away from us."
        reona.say "Wow..."
        show reona normal
        reona.say "You weren't kidding."
        reona.say "That thing nearly took you out!"
        "I start to nod, but then I see the guys that threw the frisbee."
        "They're quite a distance off, walking towards us slowly."
        "But they're clearly gesturing for me to throw the thing back."
        "Sensing the chance for some revenge, I bend down to pick it up."
        mike.say "Watch this, Reona."
        mike.say "This is how you really throw a frisbee."
        if hero.fitness >= 40:
            "I wind up for what should be a pretty easy throw."
            "And I let go at the perfect moment."
            "This sends the frisbee sailing back towards its owners."
            "They reach up, trying to catch it."
            "But then they start letting out cries of disappointment."
            "Because it keeps on going, straight over their heads."
            show reona happy at startle
            "I hear Reona laughing as they start to run after it."
            reona.say "Ooh..."
            show reona normal
            reona.say "You can be pretty mean, [hero.name]!"
            mike.say "They said they wanted me to throw it back, Reona."
            mike.say "It's not my fault they didn't say how high!"
            $ game.active_date.score += 15
            "We walk on, still looking for a spot to have our picnic."
            "But I feel a little better about things now."
            "Especially after the chance to impress Reona like that."
        else:
            "I wind up for what should be a pretty easy throw."
            "But somehow I end up letting go at the wrong moment."
            "Then all I can do is watch in horror as the frisbee sails off into the air."
            "And then proceeds to fall back down in the middle of the nearby boating lake."
            "Of course the owners of the frisbee see all of this."
            "And they instantly start shouting threats and insults in my general direction."
            mike.say "Oh shit..."
            mike.say "I think we'd better run!"
            show reona normal with fade
            "I take off a moment later, with Reona close on my heels."
            "Luckily for us, the guys seem more interested in trying to recover their frisbee."
            "And on top of that, I know the park better than most."
            "So it doesn't take long for me to lose them."
            "Maybe it'd be a better idea to stick to the more secluded areas of the park for a while."
            "At least until they get bored and decide to head home."
    else:
        "The frisbee just manages to miss hitting me in the head."
        "And then it finally hits the ground a couple of feet away."
        "I gesture at the thing as Reona looks on in amazement."
        mike.say "You see what I mean?"
        reona.say "Wow..."
        show reona normal
        reona.say "You weren't kidding."
        reona.say "That thing nearly took you out!"
        "I start to nod, but then I see the guys that threw the frisbee."
        "They're quite a distance off, walking towards us slowly."
        "But they're clearly gesturing for me to throw the thing back."
        "I look at the frisbee, then at Reona."
        "And I know what I have to do next."
        menu:
            "Leave":
                "I just shrug and walk away, leaving the frisbee right where it is."
                "Reona stares at me for a moment, but then she hurries to catch up."
                "I can vaguely hear the sounds of the guys shouting behind me."
                "But they're way too far off to be able to reach us before we turn a corner up ahead."
                "So I just ignore them and keep on walking."
                show reona angry
                reona.say "That was pretty mean of you!"
                reona.say "The least you could have done was throw it back."
                show reona annoyed
                mike.say "Nope, the least I could have done was nothing."
                mike.say "Which is exactly what I just did."
                show reona angry
                "For a moment I think Reona's going to challenge me again."
                $ game.active_date.score -= 10
                show reona annoyed
                "But then she seems to change her mind and just let the matter drop."
                "I can tell she doesn't approve of what I just did."
                "So maybe I need to make sure to impress her more from this point on."
            "Throw the frisbee back":
                "Without pausing, I bend down and pick up the frisbee."
                "I wind up for what should be a pretty easy throw."
                "And I let go at the perfect moment."
                "This sends the frisbee sailing back towards its owners."
                "They reach up, most of them missing it."
                "But one of them finally manages to snatch it out of the air."
                "They yell their thanks, but I ignore them as we walk away."
                show reona happy
                reona.say "I've got to admit..."
                reona.say "That was a pretty good throw!"
                show reona normal
                mike.say "Thanks, Reona."
                mike.say "I won't lie..."
                mike.say "Part of me wanted to throw that thing in the lake!"
                $ game.active_date.score += 15
                show reona happy at startle
                "Reona chuckles, and then she takes hold of my arm."
                "I can tell that she approves of what I did back there."
                "But that she also seems to like my honesty too."
    scene bg park at center, zoomAt(1.75, (180, 740))
    show reona at center, zoomAt(1.5, (640, 940))
    with fade
    "Finally we find our way to a nice spot on the edge of the wooded part of the park."
    "I spread out the blanket that I brought along and start setting out the picnic."
    show reona at center, zoomAt(1.5, (640, 1140))
    with ease
    "And for all of her previous sulking, Reona really does seem to be getting interested."
    "She keeps asking me what's in the dishes and containers as I take them out."
    show reona surprised
    reona.say "What's this?"
    mike.say "Erm..."
    mike.say "That's hummus, I think."
    reona.say "And this?"
    mike.say "Olives - be careful, those aren't pitted!"
    if randint(0, 1) == 0:
        "Reona seems amazed when everything is spread out before her."
        "She looks from one side of the blanket to the other, shaking her head."
        show reona happy
        reona.say "This looks so great, [hero.name]."
        reona.say "Don't tell me you made all of this yourself!"
        "I can't help smiling and shrugging a little."
        mike.say "What can I say, Reona..."
        mike.say "I kind of have a talent for this kind of thing!"
        show reona surprised
        "Reona looks suitably impressed with my admission."
        "And she doesn't hesitate to jump right in."
        if hero.has_skill("cooking"):
            show reona happy
            "I watch as Reona takes her first bite."
            "And she's smiling the whole time."
            "Right up to the moment she actually tastes it."
            show reona surprised
            reona.say "Mmm..."
            reona.say "Mmmm..."
            mike.say "Reona?"
            mike.say "Are you okay?"
            "Reona hastily swallows."
            show reona happy
            "And then she shoots me a smile."
            reona.say "[hero.name]..."
            reona.say "This stuff tastes amazing!"
            reona.say "You must be like, a genius level chef, or something!"
            $ game.active_date.score += 15
            "I watch with satisfaction as Reona continues to eat."
            "Safe in the knowledge that my culinary skills are seriously impressing her."
        else:
            show reona happy
            "I watch as Reona takes her first bite."
            "And she's smiling the whole time."
            "Right up to the moment she actually tastes it."
            show reona surprised
            reona.say "Urgh..."
            mike.say "Reona?"
            mike.say "Are you okay?"
            show reona annoyed
            reona.say "Bluergh..."
            show reona at startle
            "Reona spits out the food onto the grass."
            "And then she wipes her mouth on a napkin."
            "Like she's desperate to get the taste out of her mouth."
            show reona angry
            reona.say "Fuck..."
            reona.say "That stuff tastes awful!"
            $ game.active_date.score -= 10
            "I cringe as I watch Reona reacting to my cooking."
            "At the same time starting to put the rest of the picnic back into the basket."
    else:
        "I think about lying and claiming that I made all of this myself."
        "But then I remember that some of it is still in the packaging from the supermarket."
        "So I decide that the best thing to do is just come clean."
        menu:
            "Get pissy with Reona":
                "In fact, I feel like putting Reona in her place."
                "Because what's wrong with me having bought the food?"
                "I'm not a world-famous chef for god's sake."
                "And she's not a restaurant critic either!"
                show reona surprised
                mike.say "Of course I didn't make this myself."
                mike.say "You think I have time for that kind of thing?"
                mike.say "I can barely afford to be taking time off for this picnic."
                mike.say "You want me to be making gourmet food for you as well?!?"
                "Reona leans back and looks at me in amazement."
                "Then she looks away and shakes her head."
                show reona angry
                $ game.active_date.score -= 10
                reona.say "Geez..."
                reona.say "Way to over-react!"
                reona.say "I was only asking..."
                show reona annoyed
                "Reona goes back to eating."
                "Which leaves me to enjoy the awkward atmosphere I've created in silence."
            "Laugh it off":
                mike.say "Nah..."
                mike.say "Most of this stuff I bought for the occasion."
                mike.say "Sorry to disappoint you, Reona."
                show reona normal
                "Reona looks up from what she's eating and shrugs."
                reona.say "It's okay, [hero.name]."
                reona.say "It tastes pretty good anyway."
                reona.say "And that's good enough for me."
                "She goes back to what she's eating for a moment."
                "But I get the impression that she's got something else to say."
                "And a moment later, I'm proven right."
                show reona annoyed
                reona.say "I guess it's not where the food came from that counts."
                reona.say "Just where you eat it."
                show reona happy
                $ game.active_date.score += 15
                reona.say "And who you eat it with!"
                "I nod and smile, happy to agree with her."
                "And happy to have pulled the picnic off in the first place too."
    "The picnic food seems to be disappearing fast."
    "And I had no idea that Reona's appetite was so big!"
    "We're almost done eating, and there's not much left to clean up."
    "So I start collecting everything up, making sure not to litter."
    play sound dog_big
    "Suddenly I hear a familiar sound, and I look up from what I'm doing."
    "That's when I see a dog, off it's lead and bounding straight towards us!"
    show reona surprised
    reona.say "Aww!"
    reona.say "Look, [hero.name]..."
    show reona happy
    reona.say "That doggy's coming over to say hello!"
    if hero.has_skill("animalhated"):
        scene bg park with vpunch
        "I start shaking my head and getting to my feet."
        "Because I know exactly what's going to happen next."
        "And sure enough, as soon as it gets a whiff of me, the dog goes nuts."
        "It's yapping and snarling, showing it's teeth."
        "I swear that it wants to tear me limb from limb!"
        menu:
            "Flee":
                with vpunch
                "I jump backwards, but that doesn't stop the dog."
                "It makes a leap for me, launching itself into the air."
                "But I manage to leap to one side."
                with hpunch
                "Then I make a dash for the nearest tree, the dog snapping at my heels."
                play sound dog_big_growl
                "Scrambling up it, I look down to see my tormentor barking up at me."
                show reona surprised with dissolve
                reona.say "[hero.name]!"
                reona.say "What are you doing?!?"
                mike.say "I'm saving myself!"
                mike.say "What does it look like?"
                mike.say "That thing's out for my blood!"
                show reona normal
                "Reona shakes her head as she gazes at the dog."
                "As if it knows what's going on, the thing stops barking."
                "And it has the audacity to begin licking her hand as well!"
                "Dog owner" "SORRY!"
                "We both look around to see someone come running up, lead in hand."
                "Dog owner" "Little bugger got away from me!"
                "The owner puts the dog back on the lead and proceeds to drag it away."
                "Already feeling foolish and humiliated, I inch my way back down the tree."
                show reona normal
                $ game.active_date.score += 10
                "And I do the best I can to ignore the way that Reona's giggling at me too."
            "Kick the dog":
                with vpunch
                "I jump backwards, but that doesn't stop the dog."
                "It makes a leap for me, launching itself into the air."
                "And in that split-second I feel like I have to defend myself."
                "I don't actually kick the damn thing."
                with hpunch
                show reona surprised
                pause 0.2


                "More like I just stick my foot out and it connects with the brute."
                "But I feel the impact all the same."
                play sound dog_crying
                "And I guess the dog does too, as it lets out a yelp of pain."
                "Then it turns tail and races off into the trees."
                show reona angry
                reona.say "[hero.name]!"
                reona.say "What are you doing?!?"
                mike.say "I was defending myself!"
                mike.say "What does it look like?"
                mike.say "That thing was out for my blood!"
                show reona sad
                "Reona shakes her head as she gazes after the dog."
                $ game.active_date.score -= 10
                reona.say "That poor doggy!"
                reona.say "It could have been seriously hurt..."
                "I look at her in sheer amazement."
                "But it seems like she's not going to show me any sympathy whatsoever."
                "So I go back to clearing away the remains of the picnic."
                "All the time muttering under my breath."
    else:
        "True to the canine stereotype, the dog hurries straight over to the leftovers."
        "And before either of us can do a thing about it, begins to eat whatever's within reach."
        show reona happy
        reona.say "Aww!"
        reona.say "The poor thing's hungry."
        mike.say "Really?"
        mike.say "It looks pretty well fed to me!"
        menu:
            "Let the dog eat the leftovers":
                "I shake my head as I stand back and let the dog have its way."
                "It doesn't feel right, but I don't want to upset Reona either."
                "So the best thing to do seems to be nothing at all."
                "Reona keeps on beaming at the dog as it helps itself to out leftovers."
                "Dog owner" "SORRY!"
                "Dog owner" "So sorry!"
                "We both look around to see someone come running up, lead in hand."
                "Dog owner" "Little bugger got away from me!"
                "The owner puts the dog back on the lead and proceeds to drag it away."
                "All the time he keeps on apologizing for the dog."
                "And the two of us keep on nodding and smiling in return."
                "Once they're out of earshot, I think about complaining."
                $ game.active_date.score += 15
                "But then I see that Reona's still got a smile on her face."
                "I guess she must have a real thing for dogs."
                "So I go back to clearing away the remains of the picnic."
                "And I keep it to myself instead."
            "Get rid of the dog":
                "I don't actually kick the damn thing."
                with hpunch
                show reona surprised
                pause 0.2


                "More like I just stick my foot out and it connects with the brute."
                "But I feel the impact all the same."
                play sound dog_crying
                "And I guess the dog does too, as it lets out a yelp of pain."
                "Then it turns tail and races off into the trees."
                show reona angry
                reona.say "[hero.name]!"
                reona.say "What are you doing?!?"
                mike.say "I was just getting rid of it!"
                mike.say "What does it look like?"
                mike.say "Dog's aren't supposed to eat human food."
                show reona sad
                "Reona shakes her head as she gazes after the dog."
                $ game.active_date.score -= 10
                reona.say "That poor doggy!"
                reona.say "It could have been seriously hurt..."
                "I look at her in sheer amazement."
                "But it seems like she's not going to show me any sympathy whatsoever."
                "So I go back to clearing away the remains of the picnic."
                "All the time muttering under my breath."
    scene bg park
    show reona
    with fade
    "Pretty soon all of the stuff is packed away in the picnic basket."
    "And the only evidence of us having been here at all is the flattened grass."
    "I'm thinking that this is the perfect time for us to walk off together."
    "Maybe stroll around the more picturesque parts of the park."
    "But Reona seems to have something else on her mind."
    "She lingers around as I get ready to go, like she doesn't want to leave."
    mike.say "You okay, Reona?"
    reona.say "I'm fine, [hero.name]."
    reona.say "Just wondering if you'd forgotten something?"
    mike.say "Like what?"
    show reona annoyed at center, zoomAt(1.5, (640, 1040))
    reona.say "Oh, I don't know..."
    reona.say "Maybe like, my birthday present?"
    if not hero.has_gifts:
        "Oh bollocks!"
        "I knew there was something I'd forgotten."
        "Looks like I'm going to have to lie my way out of this one."
        mike.say "But, Reona..."
        mike.say "I already gave it to you!"
        mike.say "This date IS your present."
        show reona sad
        $ game.active_date.score -= 20
        $ reona.love -= 10
        "Reona's face falls as I say all of this."
        "Another girl might have at least tried to look pleased."
        "But not her, as she has disappointment written all over her face."
        show reona angry
        reona.say "Oh great!"
        reona.say "Lucky me!"
        reona.say "A walk in the park and some sandwiches!"
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_25
        if _return != "done":
            if _return not in ["None", "exit"]:
                "I reach into the basket and pull out the gift I had hidden in there."
                "There might have been a more romantic moment to give it to Reona."
                "But as she's kind of calling my bluff, right now will have to do."
                mike.say "Happy birthday, Reona!"
                show reona happy
                reona.say "Oh yeah!"
                reona.say "Thanks, [hero.name]!"
                "Another girl might have acted demurely, or tried to hide their excitement."
                play sound [paper_ripping_1, paper_ripping_2]
                "But not Reona, as she simply tears off the wrapping paper to get at what's inside."
                if _return:
                    "Of course that means Reona can't hide her reaction once she sees it too."
                    show reona surprised
                    "And the moment she does, her face lights up."
                    reona.say "Oh no..."
                    reona.say "No fucking way!"
                    mike.say "Erm..."
                    mike.say "Reona..."
                    mike.say "Is something wrong?"
                    show reona happy
                    reona.say "No, no..."
                    $ game.active_date.score += 15
                    reona.say "It's great - just what I wanted!"
                    "Reona throws her arms around me and hugs me tightly."
                    "And all the while I'm basking in the warm light of her gratitude."
                else:
                    "The only problem is this honesty means she can't hide her reaction to seeing it too."
                    show reona surprised
                    "And the moment she does, Reona looks pretty disappointed."
                    reona.say "Oh..."
                    $ game.active_date.score -= 10
                    reona.say "Is this it?"
                    mike.say "Erm..."
                    mike.say "Yeah, Reona..."
                    mike.say "Is something wrong?"
                    show reona annoyed
                    reona.say "It just looks a little small, you know?"
                    "Reona kind of shrugs and shoves the gift back into the box."
                    "Which leaves me feeling crushed by her ungrateful reaction."
            else:
                "Oh bollocks!"
                "I knew there was something I'd forgotten."
                "Looks like I'm going to have to lie my way out of this one."
                mike.say "But, Reona..."
                mike.say "I already gave it to you!"
                mike.say "This date IS your present."
                show reona sad
                $ game.active_date.score -= 20
                $ reona.love -= 10
                "Reona's face falls as I say all of this."
                "Another girl might have at least tried to look pleased."
                "But not her, as she has disappointment written all over her face."
                show reona angry
                reona.say "Oh great!"
                reona.say "Lucky me!"
                reona.say "A walk in the park and some sandwiches!"
    scene bg park
    show reona
    with fade
    "With the picnic basket in hand, I walk Reona back towards the entrance of the park."
    "I feel like the date went well, all things considered."
    "And the days far from over, so we could always do something else."
    "But as this is Reona's birthday, I don't feel like I can just come out and ask her."
    "So I have to do so in a passive manner, fishing for the response that I really want."
    mike.say "So..."
    mike.say "There's the entrance to the park."
    mike.say "Have you got some way of getting home, Reona?"
    if game.active_date.score >= 80 and reona.sexperience >= 1:
        show reona surprised
        "Reona looks a little surprised at me asking her that."
        "She glances around, and then looks at me, her brows wrinkled."
        reona.say "You're not really thinking of going home, are you?"
        show reona normal
        reona.say "It's still early, and I'm not even a little tired!"
        "I try to keep from smiling and letting on how delighted I am to hear her say that."
        "But it's a real battle to keep my voice level and from giving me away."
        mike.say "Oh yeah, Reona?"
        mike.say "Well that's fine by me."
        mike.say "Whatever you want to do."
        show reona at center, zoomAt(1.5, (640, 1140))
        "Reona nods and takes hold of my hand."
        "And then she starts pulling me back into the park."
        reona.say "Didn't you say something about you knowing this place really well?"
        show reona flirt
        reona.say "Like you know all the bits where nobody can find you?"
        mike.say "Sure, Reona..."
        mike.say "I'd love to show them to you."
        "Part of me can't believe I've actually pulled this off."
        "But I resist the urge to pinch myself."
        "Instead I lead Reona towards the safest spot in the park I can think of."
        "And all the time my mind is racing with images of what we might do once we get there!"
        call reona_birthday_sex_male from _call_reona_birthday_sex_male
    else:
        "Reona doesn't hesitate for a second."
        "She just nods and points in the direction that she came."
        reona.say "It's no problem."
        reona.say "I just walk a couple of blocks that way."
        reona.say "How about you?"
        "I wave my hand like it's nothing."
        "Like I'm ready to call it a day too."
        mike.say "Pretty much the same here."
        mike.say "But in the opposite direction."
        show reona happy
        "Reona nods and smiles."
        show reona at left with ease
        "Then she gives me a wave as she starts to walk away."
        reona.say "See you around, [hero.name]."
        show reona flirt
        reona.say "Or maybe I'll call you."
        hide reona with easeoutleft
        "I wave back as I stand there, watching her disappear down the street."
        "Damn it!"
        "I was sure that she's want to do more with me today."
        "I guess I'll just have to try doubly hard to impress her next time."
        "If there even in a next time!"
    return

label reona_birthday_sex_male:
    "I can think of half-a-dozen places off the top of my head that might do."
    "But then I remember that I'm not with any ordinary girl right now."
    "Reona's a bit more wild than that, so I need to be sure we're off the beaten track."
    "I need to take her somewhere that I can be sure we won't be seen or heard."
    "So that's why I head to the very back of the park, where I know it borders on the woods."
    show reona surprised
    reona.say "Just where are we going, [hero.name]?"
    reona.say "I thought we were gonna fool around, you know?"
    show reona annoyed
    reona.say "Not go hiking into the wilderness!"
    mike.say "Don't worry, Reona."
    mike.say "I'm taking us to a great spot."
    mike.say "And it's just up ahead."
    "I'm not just saying that to placate Reona either."
    scene bg black with dissolve
    scene bg forest
    show reona surprised
    with dissolve
    "As a few moments later we emerge from between the trees into a small clearing."
    "It's too small of a space to really be of interest to anyone walking nearby."
    "Yet it's still pretty enough to be worth the effort of reaching for what we have in mind."
    "Reona walks into the middle of the clearing and scans her surroundings."
    show reona normal
    reona.say "Huh..."
    reona.say "Wadda ya know..."
    show reona happy
    reona.say "You were right - this place does look pretty great!"
    "I'm about to open my mouth and say something sarcastic in response."
    "But the words die in my throat and my jaw hangs open as I watch what Reona does next."
    show reona bottomless flirt with dissolve
    "Without waiting for any kind of signal, she reaches up and pulls down her panties."
    "And once they reach her ankles, she kicks them off without a care in the world."
    mike.say "Huh..."
    mike.say "Wha..."
    "Reona must have heard me mumbling in confusion."
    show reona annoyed
    "As she looks back at me over her shoulder."
    reona.say "What are you staring at?"
    show reona flirt
    reona.say "Are we gonna fuck, or what?"
    reona.say "Because I like the look of that spot over there!"
    "Reona walks over towards the spot she pointed out."
    "And she keeps on stripping off her clothes as she goes."
    show reona naked with dissolve
    "So that by the time she reaches it, she's completely naked."
    "Then she leans her arms on a particularly sturdy branch."
    "But she makes sure to stick her ass out as she does so."
    "Seeing it naked and swaying from side to side is enough to snap me out of it."
    "I feel like I've been slapped int he face or doused with ice-cold water."
    "And I hurry to follow in Reona's footsteps."
    "Crossing the clearing, I tear off my own clothes."
    "I'm naked by the time I make it to Reona."
    "And needless to say that my body's ready for her too."
    show reona doggy forest naked mike with fade
    "She jumps a little and lets out a filthy giggle as I grab hold of her."
    reona.say "Hey there!"
    reona.say "I think you have something for me, yeah?"
    reona.say "A little extra birthday gift?"
    "I nod eagerly, already pushing my hardening cock between her buttocks."
    "And when I say that I've grabbed hold of her, that's not strictly true."
    "Because what I'm actually doing is squeezing and massaging her ass."
    "I feel like I've been waiting forever to get my hands on Reona."
    "And now her ample buttocks feel so good under my fingers."
    "It's not like she does anything to discourage me either."
    "Instead she keeps right on wriggling and giggling."
    "Letting me know that she's liking the sensation of being handled in that way."
    reona.say "Mmm..."
    reona.say "You know what, [hero.name]..."
    reona.say "I never got fucked in the middle of nature before."
    reona.say "So this is kind of a first for me!"
    "I'm more than a little surprised to hear Reona admit to a thing like that."
    "In my mind she's the kind of girl that must have done it all."
    "And the admission only makes me want to do this more desperately."
    "But a moment later I get a good clue that Reona feels the same way too."
    "As I feel her reach back and grab a hold of my cock."
    mike.say "Ungh..."
    mike.say "Careful with that, Reona!"
    reona.say "Ah, come on, [hero.name]!"
    reona.say "Don't be such a pussy."
    show reona doggy vaginal mouth_pleasure
    "With that, Reona presses the head of my cock between her legs."
    "And she makes sure to rub it up against the lips of her pussy too."
    "After that I don't need to be encouraged anymore."
    "Sheer instinct takes over, and my grip on Reona tightens."
    show reona doggy eyes_pleasure mouth_normal smash with hpunch
    "At the same time I thrust myself forwards with all my strength."
    "Reona's pushed against the branch with nowhere to go."
    "I can feel the muscles of her pussy trying to resist."
    "But the sounds that she's making tell me she wants the opposite."
    show reona doggy eyes_closed -smash
    reona.say "Ah..."
    reona.say "Mmm..."
    reona.say "Oh fuck..."
    show reona doggy mouth_pleasure
    reona.say "Yeah, just like that!"
    show reona doggy smash bounce with hpunch
    pause .15
    show reona doggy -bounce
    pause .15
    show reona doggy -smash
    pause .75
    show reona doggy smash bounce with hpunch
    pause .15
    show reona doggy -bounce
    pause .15
    show reona doggy -smash
    pause .75
    show reona doggy smash bounce with hpunch
    pause .15
    show reona doggy -bounce
    pause .15
    show reona doggy -smash
    "All this time I'm pushing hard, nothing else on my mind."
    "And as I begin to get my way, Reona starts to wail."
    show reona doggy mouth_teeth
    reona.say "Oooh..."
    reona.say "Get inside me..."
    reona.say "I...I wanna be fucked...hard!"
    "Suddenly Reona's body surrenders to me, and I sink into her."
    show reona doggy smash bounce with hpunch
    pause .15
    show reona doggy -bounce
    pause .15
    show reona doggy -smash
    pause .5
    show reona doggy smash bounce with hpunch
    pause .15
    show reona doggy -bounce
    pause .15
    show reona doggy -smash
    "I've been using so much force that there's no way for me to slow down."
    "My cock slides all the way into Reona until it can't get any deeper."
    "I can feel it forcing the muscles of her pussy aside as it fills her."
    show reona doggy smash bounce with hpunch
    pause .15
    show reona doggy -bounce
    pause .15
    show reona doggy -smash
    pause .5
    show reona doggy smash bounce with hpunch
    pause .15
    show reona doggy -bounce
    pause .15
    show reona doggy -smash
    "Normally I'd stop right there and enjoy the sensation for a moment."
    "And I'd let the girl I'm with feel it too."
    "But I guess Reona just does something to me."
    "Something that makes me hold nothing back."
    "Because I waste no time in beginning to move inside of her."
    show reona doggy smash bounce eyes_ahegao mouth_normal with hpunch
    pause .15
    show reona doggy -bounce
    pause .15
    show reona doggy -smash
    pause .3
    show reona doggy smash bounce with hpunch
    pause .15
    show reona doggy -bounce
    pause .15
    show reona doggy -smash
    pause .3
    show reona doggy smash bounce with hpunch
    pause .15
    show reona doggy -bounce
    pause .15
    show reona doggy -smash
    pause .3
    show reona doggy smash bounce with hpunch
    pause .15
    show reona doggy -bounce
    pause .15
    show reona doggy -smash
    pause .3
    show reona doggy smash bounce with hpunch
    pause .15
    show reona doggy -bounce
    pause .15
    show reona doggy -smash
    "I thrust my cock back and forth, not letting up for a second."
    "Before Reona was leaning herself on the branch in front of her."
    "But now she's being pushed over it by the force with which I'm pounding her."
    "Her arms are hung over it, flopping uselessly before her."
    "And I can hear the sound of the wood creaking with every move I make."
    "With every moment that passes I'm more relieved that we came here to do it."
    "I know that I couldn't make myself hold back if I tried."
    "And the only reason Reona's not crying out is that she's insensible from my efforts."
    show reona doggy smash bounce with hpunch
    pause .15
    show reona doggy -bounce
    pause .15
    show reona doggy -smash
    pause .3
    show reona doggy smash bounce with hpunch
    pause .15
    show reona doggy -bounce
    pause .15
    show reona doggy -smash
    pause .3
    show reona doggy smash bounce with hpunch
    pause .15
    show reona doggy -bounce
    pause .15
    show reona doggy -smash
    "My thighs are slapping hard against her buttocks, the skin of both turning red."
    "I can only hope that the branch is up to all of the abuse we're giving it."
    "Because the last thing I want is for it to break and us all to tumble forwards."
    "Even so, I keep on going ever harder, fucking Reona with all my might."
    show reona doggy mouth_teeth
    reona.say "Oh..."
    reona.say "Oh fuck..."
    reona.say "I'm...I'm cumming!"
    reona.say "You're making me cum!"
    "I take a firmer hold of Reona as her entire body begins to shake."
    "At the same time I can feel the orgasm take hold as she squeezes my cock."
    "In fact the spasms of the muscles in her pussy are getting stronger all the time."
    "So much so that I know I'm not going to be able to resist."
    show reona doggy smash bounce mouth_ahegao with hpunch
    pause .15
    show reona doggy -bounce
    pause .15
    show reona doggy -smash
    pause 1.25
    show reona doggy smash bounce with hpunch
    pause .15
    show reona doggy -bounce
    pause .15
    show reona doggy -smash
    pause 1.5
    show reona doggy smash bounce with hpunch
    pause .15
    show reona doggy -bounce
    "And I feel myself losing it too, shooting my load into Reona."
    "Soon her body begins to go limp, her limbs buckling under her."
    show reona doggy eyes_closed -smash
    $ reona.sexperience += 1
    "The only thing holding Reona up now is the branch and my own hands."
    "So I use the last of my strength to lower her to the ground."
    "That done, I sit on the grass at her side, gasping for breath too."
    scene bg black with dissolve
    return

label reona_preg_talk:

    if reona.purity > 66:
        call reona_preg_talk_high_purity from _call_reona_preg_talk_high_purity
    elif reona.purity > 33:
        call reona_preg_talk_average_purity from _call_reona_preg_talk_average_purity
    else:
        call reona_preg_talk_low_purity from _call_reona_preg_talk_low_purity

    return

label reona_preg_talk_low_purity:
    show reona sad
    "I can tell that there's something up even before Reona makes it over to where I'm standing."
    "Because she's got her hands balled into fists down by her sides as she strides over."
    "And the look on her face is one that makes me take an unconscious glance over my shoulder."
    "The natural urge to flee becoming stronger the closer Reona gets."
    "This means that by the time she's near enough to start shouting at me, I'm already flinching."
    show reona angry
    reona.say "Hey, you!"
    reona.say "Yeah, you know that I mean you, buddy!"
    reona.say "You've got some serious explaining to do!"
    "I'm still feeling the urge to turn tail and flee."
    "But instead I reach down into my gut and somehow find the courage to stand my ground."
    "After all, what can I have done that's so bad Reona looks like she wants to kill me?"
    "Most likely this is just going to turn out to be one of those silly little mistakes."
    "We'll probably be laughing about it in no time."
    mike.say "Erm..."
    mike.say "Hi, Reona..."
    mike.say "What's the matter?"
    "Now one of the fists has a finger sticking out of it."
    show reona angry at center, zoomAt(1.5, (640, 1040)) with vpunch
    "And Reona's jabbing it about an inch from my eye."
    reona.say "Don't give me that bullshit."
    reona.say "Not after you went and got me pregnant!"
    "Okay..."
    "Maybe we're not going to be laughing about this any time soon."
    mike.say "Whoa..."
    mike.say "Wait a minute there, Reona!"
    mike.say "Are you serious?!?"
    mike.say "Because that's a serious accusation."
    mike.say "So you need to be...erm, serious about it!"
    show reona annoyed
    "Reona doesn't seem in the least bit thrown by my response."
    "In fact it only appears to have the effect of making her bolder still."
    "She reaches into her pocket and pulls out a piece of white plastic."
    "Which she then proceeds to toss into my face."
    "I only just manage to catch the thing before it hits me between the eyes."
    "And looking down at it in the palm of my hand, I'm not surprised to see what it is."
    "A used pregnancy test, the kind you buy at a pharmacy and use at home."
    "And the red bar on the test strip is right next to the word 'positive'!"
    reona.say "You see?"
    show reona angry
    reona.say "You'd better help me get out of this mess, [hero.name]."
    reona.say "Because you sure as hell had a hand in getting me into it!"
    "I can't help starting to nod as the gravity of the situation dawns on me."
    "Sure, Reona's being a massive bitch right now."
    "And this could only have been the result of an accident."
    "But I'm as responsible for it as she is."
    "So I need to be responsible for taking care of it too."
    menu:
        "We should keep the baby":
            "And by that I mean taking care of the baby as a responsible parent."
            show reona sad
            mike.say "Don't worry, Reona..."
            mike.say "I'm the father of this child."
            mike.say "And that means I have a responsibility."
            mike.say "I'll be with you every step of the way."
            mike.say "And then we're going to raise this kid together - as a family!"
            "I'm fully expecting Reona's mood to improve once I'm done saying all of this."
            "But instead I see that she's now staring in complete amazement."
            "Almost like I have steaming turds hanging out of my mouth."
            show reona annoyed
            $ reona.sub -= 10
            reona.say "What the actual fuck are you talking about?"
            reona.say "We're not raising the bloody thing together, you idiot!"
            reona.say "I want you to give me money to get a fucking termination!"
            "Now it's my turn to stare at Reona."
            "Shaking my head as I can't understand what she's saying."
            mike.say "A termination?"
            mike.say "But you can't..."
            mike.say "That's my kid too!"
            reona.say "Oh get a bloody clue, [hero.name]."
            reona.say "It's not a kid, and I won't let it grown until it becomes one."
            show reona sad
            reona.say "It's a mistake, that's all."
            reona.say "So are you going to help me or not?"
            mike.say "No, Reona, I'm not!"
            mike.say "I won't help to kill my own child!"
            hide reona
            show reona angry
            $ reona.love -= 20
            reona.say "Urgh..."
            reona.say "Fucking typical!"
            reona.say "I should have known you'd turn out to be a deadbeat."
            show reona at right with ease
            "With that, Reona turns on her heel and starts to walk away."
            show reona annoyed
            reona.say "Don't worry, I'll handle this myself."
            reona.say "And you won't be seeing me again either."
            reona.say "You lousy excuse for a man!"
            hide reona with easeoutright
            $ reona.set_gone_forever()
            "I could chase after Reona, beg her to change her mind."
            "But I kind of feel like I just saw her true colours on display."
            "And if that's who she really is, then maybe what she wants is for the best."
            "Because I can't say that I want her in my life after this."
            "And any kid we might have had together would be screwed with her as it's mother too."
        "You should have a termination":
            "And by that I mean making sure that Reona and I don't end up as unwilling parents!"
            "Sure, it might sound like a heartless thing to do."
            "But what kid really deserves Reona as it's mother?!?"
            show reona sad
            mike.say "Don't worry, Reona..."
            mike.say "I've been squirreling some money away."
            mike.say "I was supposed to be saving it towards a deposit on a house of my own."
            mike.say "But I guess this is kind of an emergency."
            show reona normal
            $ reona.love += 10
            "Reona crosses her arms over her chest and nods."
            "Her mood might not have softened to any great degree."
            "But at least she's not openly hostile to me anymore."
            reona.say "Now that sounds like a plan."
            reona.say "The first sensible thing you've said since I told you."
            show reona annoyed
            reona.say "But you'd better make it fast."
            reona.say "I want this thing out of me asap!"
            "I'm nodding even as I get out my mobile and pull up my banking app."
            "I suppose that I should be thankful that I can get out of this one so easily."
            "Imagine the mess I'd have been in if Reona insisted on keeping the baby?"
            "She could have fleeced me good and proper when it came to maintenance payments!"
            "So all of my savings is probably a small price to pay."
            mike.say "There, Reona..."
            mike.say "I've set the ball rolling."
            mike.say "We'll soon have this all sorted out."
            show reona happy
            reona.say "Good boy, [hero.name]!"
            reona.say "Now let's celebrate the good news with some unprotected sex!"
            show reona flirt at startle(0.05, -10)
            reona.say "KIDDING!"
            reona.say "Hah..."
            show reona happy
            reona.say "The look on your fucking face!"
            mike.say "Erm..."
            mike.say "Yeah, Reona..."
            mike.say "It's so funny I forgot to laugh!"
            $ reona.unpreg()
    return

label reona_preg_talk_average_purity:
    show reona pensive at center, zoomAt(1.3, (640, 900))
    with easeinleft
    "I'm usually pretty excited to look up and see Reona hurrying towards me."
    "I mean, when a girl looks as hot as she does, what red-blooded guy wouldn't?"
    "But that sense of excitement soon begins to fade when I read the look on her face."
    "Because right now Reona has a worried look about her, and her eyes are downcast too."
    "Concerned about what could be affecting her, I close the distance between us."
    show reona sad at center, traveling(1.5, 0.3, (640, 1040))
    "Then I take hold of her hands, almost shaking her until she looks up at me."
    mike.say "Reona..."
    mike.say "What's wrong?"
    mike.say "You look like you just had some really bad news!"
    show reona sadsmile
    "Reona doesn't hesitate to look me in the eye as I'm saying all of this."
    "But I note that she neither nods or shakes her head too."
    "Almost as if she can't really answer the question."
    show reona shout
    reona.say "I..."
    reona.say "I'm not sure, [hero.name]…"
    reona.say "If it's good or bad, that is..."
    show reona sadsmile
    "Reona's words do nothing to help be even begin to get a handle on things."
    "But I can see that she really is in a bad place right now."
    "So the best thing for me to do would be to comfort her."
    "That way she's more likely to get her head in check."
    mike.say "It's okay, Reona..."
    mike.say "You take your time."
    mike.say "Tell me what you can and we'll work out the rest between us."
    show reona normal
    "Reona nods at this."
    "And she manages to give me a weak smile."
    "Which I find surprisingly reassuring."
    show reona talkative
    reona.say "Okay, [hero.name]…"
    reona.say "I'll do my best."
    reona.say "But you have to promise not to be mad, yeah?"
    show reona normal
    mike.say "Sure thing, Reona..."
    mike.say "I promise."
    "Even as I say the words, I'm hoping that I won't come to regret them."
    "Because I have no idea what's going to come out of Reona's mouth next."
    "It could be something totally innocent that she's blown out of all proportion."
    "Or else something bad enough to make me throw myself under the next passing bus."
    "All I can do is stand there and wait to hear it."
    show reona talkative
    reona.say "So, I've been feeling pretty shitty in the morning recently."
    reona.say "And I thought about what it could be for a while."
    reona.say "But a friend said that I should get one of those tests, you know?"
    reona.say "So I did that, and I used it..."
    show reona normal
    with vpunch
    mike.say "Whoa..."
    mike.say "Wait a minute, Reona..."
    mike.say "Are you talking about the kind of test I think you are?!?"
    show reona talkative
    "Reona looks at me as if she's a little confused."
    show reona flirt
    reona.say "Well, if the test you're thinking of is a pregnancy test, then yeah!"
    show reona normal
    "The moment the words are out of her mouth, I'm sure I know what's coming next."
    "There's no way she's going to tell me it was negative."
    "That and we have to be more careful in future."
    "Because nobody builds up a negative pregnancy test like this."
    with hpunch
    mike.say "So you're pregnant?!?"
    show reona surprised
    reona.say "Whoa..."
    reona.say "Yeah, I am!"
    reona.say "How did you guess?"
    show reona interested
    mike.say "Let's just say it was a lucky one..."
    "Reona seems to miss the sarcastic tone of my voice entirely."
    "Or maybe she's too focussed on the matter at hand to give it any time."
    "Either way, she gets straight to the point."
    show reona shout
    reona.say "I don't know what to do about it, [hero.name]!"
    show reona talkative
    reona.say "Before I'd have wanted to get rid of it."
    reona.say "But since you started teaching me to respect myself more..."
    reona.say "Well now I can't just do something like that anymore."
    show reona annoyed
    reona.say "Now I have to spend time actually thinking about stuff!"
    show reona talkative
    reona.say "So seeing as you're the smart one, and it's your kid..."
    show reona whining
    reona.say "What should I do?!?"
    show reona interested
    menu:
        "I should convince her to keep the baby":
            "Now I can see the consequences of trying to get Reona to change her ways!"
            "But she is right to get me involved in the decision-making here."
            "Because I'm as responsible for this situation as she is."
            mike.say "There's only one thing we can do, Reona..."
            mike.say "And that's to be responsible adults."
            mike.say "We made this baby together."
            mike.say "So we're going to have to raise it together too!"
            show reona surprised at startle
            "I can see that my answer's kind of scared Reona."
            "And for a moment I think she's going to argue with me."
            "That she's going to insist on getting a termination."
            show reona normal
            "But then she surprises me by nodding firmly."
            show reona talkative
            reona.say "Okay, [hero.name]…"
            reona.say "If that's what we have to do."
            show reona happy
            $ reona.love += 10
            reona.say "Then we can do it together!"
            show reona normal
            "Reona sounds like she's going on a roller-coaster of emotions right now."
            "And I have to say that I feel pretty much the same."
            "But when she reaches out and takes my hand, all of that changes."
            "I know she's doing so to seek reassurance from me."
            "Yet it also has the unexpected effect of making me feel more confident too."
            "And I can feel the resolve growing in me to make the best of this thing."
            "Sure, we might not have planned to be starting a family just yet."
            "But that doesn't mean we can't make a success of it."
            $ reona.flags.toldpreg = True
        "I think we should get a termination":
            "Now I can see the consequences of trying to get Reona to change her ways!"
            "Because as she said, the old her would have just gotten a termination herself."
            "Thanks to my own meddling I'm having to get involved in the decision too."
            mike.say "I know that I've been encouraging you to think differently, Reona..."
            mike.say "But that doesn't mean there aren't situations where the old you would still have been right."
            show reona surprised
            "Reona looks at me in amazement."
            show reona talkative
            reona.say "You..."
            reona.say "You mean..."
            show reona normal
            mike.say "Yes, Reona..."
            mike.say "I think a termination would be the best thing."
            show reona pensive
            "Reona starts to nod slowly, as though she's thinking it through."
            "But I can see that she's not totally convinced."
            show reona sad
            reona.say "But couldn't we..."
            reona.say "Like, you know..."
            reona.say "Keep it and start a family?"
            show reona normal
            "I shake my head, trying to be as sensitive as I can."
            "But all the time wanting to close down the discussion."
            show reona sad
            mike.say "No, Reona..."
            mike.say "This kind of thing needs to be planned, yeah?"
            mike.say "We need to be prepared emotionally and financially."
            mike.say "Until then we're just not ready to raise a kid."
            show reona pensive
            "By now Reona seems to have gotten it through her head."
            "And her nodding is that much more emphatic."
            show reona sad
            reona.say "I guess you're right, [hero.name]…"
            reona.say "Or else I'd be the one teaching you new stuff!"
            "I nod and smile, glad to have won Reona over to my way of thinking."
            $ reona.love -= 20
            $ reona.unpreg()
    return

label reona_preg_talk_high_purity:
    show reona shout leftnormal rightopen at center, zoomAt(1.0, (640, 720))
    with easeinright
    reona.say "[hero.name]!"
    show reona shout at center, traveling(1.25, 0.3, (640, 880))
    reona.say "[hero.name]!!"
    show reona angry at center, traveling(1.35, 0.2, (640, 940))
    reona.say "I need to talk to you - RIGHT NOW!"
    show reona normal rightnormal
    "I know it's not good when I hear someone calling my name like that."
    "And I know it's doubly so when they add that line right after it."
    show reona devious at center, traveling(1.5, 1.0, (640, 1040))
    "So when I look up to see Reona coming towards me, looking like she means business..."
    "Well, let's just say that I'm not at all surprised."
    show reona normal
    mike.say "Erm..."
    mike.say "Hey, Reona..."
    mike.say "Was there something you needed from me?"
    "I'm doing the best I can to seem calm and confident right now."
    "But my honest instinct is to turn on my heel and run in the opposite direction."
    "Because I just know that Reona's going to be riding my ass about something in a few seconds."
    "I just wish that I knew what it was so that I could at least be prepared."
    show reona talkative
    reona.say "Oh, I already got something from you."
    show reona angry
    reona.say "Something that you're going to take responsibility for too!"
    show reona devious leftnormal
    "Reona comes to a halt as she says this."
    "Then she thrusts her stomach out at me."
    "And adds a glare as she points to it with her finger."
    show reona talkative
    reona.say "Look at that..."
    reona.say "Right there!"
    show reona normal
    "I blink for a moment as I stare at Reona's stomach."
    "Because to me it doesn't look any different to the last time I saw it."
    "So I have no idea what in the hell she's even talking about."
    mike.say "What's the matter, Reona?"
    mike.say "Did you get sick from the last meal I bought you?"
    show reona angry at startle
    with hpunch
    reona.say "WHAT?!?"
    show reona talkative
    reona.say "No, [hero.name]…"
    show reona annoyed
    reona.say "I'm pregnant, isn't it obvious?"
    show reona normal
    "All I can do is shake my head at this."
    mike.say "No, it isn't."
    mike.say "Are you sure you're not getting confused, Reona?"
    mike.say "Like, mixing up the symptoms of pregnancy with food poisoning?"
    show reona angry
    "Reona looks a little more irate than before."
    "And she shakes her head, dismissing the notion."
    show reona annoyed
    reona.say "Not unless I bought the wrong kind of test at the drug store!"
    reona.say "It certainly said pregnancy test on the box."
    reona.say "And when I used it, the result was positive too!"
    show reona normal
    "I can finally feel the weight of realisation settling upon me."
    "And I can only guess that it must be showing on my face too."
    show reona devious
    "Because Reona starts to nod and give me a knowing grin."
    show reona talkative
    reona.say "There you go."
    reona.say "Finally realising the truth, huh?"
    reona.say "Because it is true, [hero.name]."
    show reona happy
    reona.say "We're going to be parents!"
    show reona normal
    "I somehow manage to catch the last part of that better than the rest."
    "And I instantly feel the inevitable question forming on my lips."
    mike.say "What do you mean, Reona?"
    mike.say "We're only going to be parents if we choose to keep it."
    show reona devious
    reona.say "And that's what we're going to do."
    show reona talkative
    reona.say "We're going to keep it."
    reona.say "You taught me to change my ways, [hero.name]."
    reona.say "The old me would have wanted to get rid of it, to run away from my responsibilities."
    show reona interested
    reona.say "But the new me isn't going to let that happen."
    show reona normal
    menu:
        "I guess she's right, we should keep it":
            "I have to admit that I feel kind of bullied by the way Reona's acting."
            "But I was the one that began the process of 'fixing' her moral defects."
            "So it'd be pretty hypocritical of me to demand she have a termination."
            "Because is there any worse way to dodge moral responsibility than that?"
            mike.say "Y...yeah..."
            mike.say "You're right, Reona..."
            mike.say "We should have been more careful, been sure to use protection."
            mike.say "And now we have to take responsibility for the consequences of our actions."
            show reona interested
            "Reona seems to like what she's hearing."
            "As she nods and makes approving sounds all the while I'm talking."
            show reona happy
            "And once I'm done, she shows her agreement with a huge smile."
            show reona talkative
            reona.say "My thoughts exactly, [hero.name]."
            reona.say "It's so good to know we're on the same page."
            show reona devious
            reona.say "I had considered asking you to marry me too."
            show reona talkative
            reona.say "You know, so the child wouldn't be born out of wedlock?"
            reona.say "But I think we can discuss that over the next nine months or so."
            show reona normal
            mike.say "Oh..."
            mike.say "I guess so, Reona..."
            mike.say "Thanks for being so...considerate?"
            show reona happy
            $ reona.love += 10
            "Reona nods one more time."
            show reona normal
            "And I feel like I'm handing over the reigns of my life to her."
            $ reona.flags.toldpreg = True
        "I'm not being pushed into this":
            "I have to admit that I feel kind of bullied by the way Reona's acting."
            "I know that I was trying to 'fix' her morals by starting all of this."
            "But the idea was to improve her, not me!"
            "Now I'm being strong-armed into becoming a father!"
            mike.say "Hold on a minute, Reona..."
            mike.say "You're not just going to stride up and demand that I have a kid with you!"
            show reona angry at startle
            "I see Reona bristle at this."
            "And she seems to be getting angrier by the second!"
            show reona shout
            with hpunch
            reona.say "You ARE having a kid with me, [hero.name]!"
            show reona sadshock
            reona.say "I'm already pregnant, don't you get it?!?"
            show reona angry
            reona.say "Be a man and step up!"
            show reona sadfrustrated
            "I shake my head, not willing to be pushed around."
            mike.say "Just accepting it isn't a moral thing, Reona."
            mike.say "In fact it can be the worst choice of all."
            mike.say "Like, we could come to resent the kid."
            mike.say "And that's really fuck them up!"
            show reona sad
            "Now Reona's the one shaking her head."
            show reona angry
            reona.say "I can't believe I'm hearing this."
            reona.say "Especially from you!"
            show reona annoyed
            reona.say "Do what you like, [hero.name]..."
            show reona angry
            $ reona.love -= 20
            reona.say "But I'm keeping this kid!"
            reona.say "And if you're not going to help out, then I guess it's over between us."
            hide reona with easeoutright
            $ reona.set_gone_forever()
            "With that, Reona turns on her heel and strides away."
            "I think about following her, trying to get my point across."
            "But I get the feeling nothing I say would work right now."
    return

label reona_male_ending:
    $ game.hour = 16

    if "reona_redemption_07" in DONE and reona.purity >= 95:
        jump reona_redemption_ending


    if renpy.has_label("reona_achievement_3") and not game.flags.cheat:
        call reona_achievement_3 from _call_reona_achievement_3
    $ game.room = "church"
    show bg church wedding with fade
    "As a guy you never sit down and plan out your wedding day years in advance."
    "Hell, you never even spare a serious thought for if you'll actually tie the knot in your lifetime."
    "It's just one of those things that you might do, if the circumstances are right."
    "Or you might not, and if so then it's not exactly a big deal."
    "And planning a wedding with Reona's taught me that it can be just like that for a girl too."
    "Sure, some of them spend ages working it out to the tiniest detail."
    "And from a worryingly young age too!"
    "But the idea that they all do that is one of those old stereotypes that just doesn't hold up."
    "Because believe me, Reona was as casual about all of the planning as I was myself!"
    "I mean, it was only by chance that we ended up tying the knot in an actual chapel."
    "We were all for popping along to the registry office and getting it done in record time."
    "But let's just say that certain members of our respective families made their feelings clear."
    "Which is how I came to find myself standing at the altar today."
    "Dressed up in a very fancy and extremely uncomfortable suit."
    "And sweating from the pressure of all the eyes that are on me right now."
    "Every time I look back over my shoulder, I see them all staring at me."
    "Half of the seats filled with Reona's friends and family."
    "The other half filled with anyone and everyone that means something to me."
    "I keep on willing her to arrive so that the ceremony can get started."
    "So much so that when the music starts to play, I totally fail to notice."
    "All I know is that every head in the chapel turns to look back at the doors."
    "And I feel a surge of relief, knowing that they're finally not looking at me!"
    "In the end it's the priest that makes me wake up and pay attention."
    "Because he gives me a stern look, then nods in the same direction."
    "This is enough to snap me out of it and turn my head too."
    show reona wedding normal at center, zoomAt (1.0, (640, 740))
    with fade
    "And that's when I see Reona walking into the chapel."
    "The moment I lay eyes on her I remember how we got here and why."
    "It's not just that she looks amazing in her wedding dress."
    show reona happy
    "It's the smile on her face and the feelings she stirs up inside of me."
    if reona.is_visibly_pregnant:
        "But there's also the fact that Reona's cradling her belly too."
        "Reminding me of the fact that we're not just getting married today."
        "Pretty soon we're also going to become a family."
        "And that's something I couldn't be more excited about if I tried."
    else:
        "And the fact that I know the girl I'm marrying is the best version of Reona possible."
        "She's managed to come to terms with the past and how it shapes her personality in the present."
        "Instead of controlling her actions, she's now the one in charge of her powerful libido."
        "A fact that I've been reaping the benefits of ever since she achieved that too!"
    show reona wedding normal at center, traveling (1.5, 2.0, (640, 1040))
    "As Reona reaches the altar, our eyes meet for the first time today."
    "And I can be sure that the smile on my face is as wide as the one on her own!"
    mike.say "Whoa..."
    mike.say "You look incredible, Reona!"
    show reona embarrassed
    reona.say "Aw..."
    reona.say "Thanks, [hero.name]."
    show reona pensive
    reona.say "You look...very smart!"
    show reona happy
    show wedding reona with fade
    "All I can do in response to that is shrug."
    "Because at least Reona's being honest with me."
    "Priest" "If I could interrupt for a moment?"
    show wedding reona priest with dissolve
    "At the sound of the priest's voice, Reona and I turn our attention to him."
    "And this seems to be the right decision, as he then launches straight into it."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here to today to witness the union of these two people..."
    "You all know what comes next, right?"
    "I mean, you've seen a wedding play out a thousand times before."
    "So we can skip ahead to the really important bits."
    "Like the part where the priest says..."
    "Priest" "Do you, [hero.name], take Reona to be your lawful, wedded wife?"
    mike.say "Yes, I do!"
    "Priest" "And do you, Reona, take [hero.name] to be your lawful, wedded husband?"
    reona.say "Yes, I do!"
    "The priest nods."
    "Priest" "Then I call upon all those present..."
    "Priest" "If they know of any lawful or moral reason that these two may not be wed..."
    "Priest" "To speak now, or forever hold their peace!"
    "The silence that descends over the chapel should just be for the sake of tradition."
    "But a small part of me is still worried that someone might actually speak up."
    "Like maybe Jack's jealousy will get the better of him."
    "Or the guy that screwed Reona up so badly in the past could show up."
    "Luckily for me, none of my fevered imaginings seem to be coming true."
    "Finally, the priest gives a satisfied nod and gets the show going again."
    "And it's only then that I realise I've actually been holding my breath!"
    "Priest" "Then I declare you husband and wife."
    "Priest" "You may kiss the bride!"
    show wedding reona -priest with dissolve
    "I turn to Reona, meaning to make this a romantic moment."
    "But instead I find myself being almost pounced on by her instead!"
    scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
    show reona kiss wedding
    with hpunch
    $ reona.flags.kiss += 1
    "Though I do have to admit that the kiss which follows is well worth it."
    "And afterwards it takes a while for me to come back down to earth again."
    "That and to realise that we actually did it."
    "Reona and I tied the knot - we're husband and wife!"
    show reona ending with fade
    if reona.sexperience == 0:
        reona.say "You know it's kind of crazy when I actually sat down and thought about all of this."
        reona.say "Actually took the time to look back and take stock of all that we've been though together."
        reona.say "Sometimes I forget that [hero.name] and I met under such totally random circumstances."
        reona.say "Like, if we hadn't been looking at the results for those examinations at the exact same time."
        reona.say "Or if he'd never shown any interest in helping me out with my studies."
        reona.say "We'd be in totally different places right now, with totally different people."
        reona.say "Hell, we'd both be different people too!"
        reona.say "Because I know that he's had a real effect on the person I am today."
        reona.say "And I like to flatter myself that I've had the same effect on him too."
        reona.say "Back when we first met, I couldn't have imagined that a guy would ever say no to me."
        reona.say "And I couldn't imagine any kind of interaction like that without sex being involved."
        reona.say "So yeah...it came as a real surprise when [hero.name] turned me down."
        reona.say "Hah...who am I trying to kid!"
        reona.say "It was a massive shock - a total slap in the face for me."
        reona.say "Of course I went through the usual ritual of tyring to explain it away."
        reona.say "Like, I wondered if I didn't make myself clear enough to him."
        reona.say "Or maybe he was already involved with someone and trying to be faithful."
        reona.say "I even wondered if he might be into guys for a while!"
        reona.say "But eventually he managed to convince me that there was nothing wrong."
        reona.say "He just wanted to take things slowly, to earn my trust before we went there."
        reona.say "And that was what set me on the path of questioning myself."
        reona.say "Here was a guy that wanted to be with me."
        reona.say "But he also didn't want to do it with me."
        reona.say "At least not right away."
        reona.say "Of course this threw me into a state of total confusion."
        reona.say "The only explanation that I could come up with was that he thought I was damaged goods."
        reona.say "That I was never going to be good enough for him, because of what happened in my past."
        reona.say "I felt like the only thing I could do was explain myself to him, with nothing held back."
        reona.say "I was sure that it'd be enough to make him dump me on the spot, so I prepared for the worst."
        reona.say "But then he went and surprised me again, by understanding and doing all he could to help."
        reona.say "I already knew that I was in love with him, and that kind of sealed the deal."
        reona.say "So when he proposed to me, getting down on one knee like a goof, I said yes."
        reona.say "After that, [hero.name] encouraged me to complete my college course."
        reona.say "And with his help I passed."
        reona.say "Sure, my grade wasn't the highest or anything like that."
        reona.say "But it was far better than I'd have done on my own."
        reona.say "I was going to look for a job after that, really I was."
        reona.say "But then the chance for us to move in together came along."
        reona.say "And handling all of that took up my time."
        reona.say "Before I knew it, [hero.name] was going out to work every day."
        reona.say "And I was staying at home, handling the domestic side of things."
        reona.say "But I found that I didn't hate it."
        reona.say "In fact, I was really starting to love it."
        if reona.is_visibly_pregnant:
            reona.say "We already had Helen by that time, so we were officially a family."
            reona.say "And maybe the ease at which we slipped into the role as parents helped."
            reona.say "Me taking her to school and picking her up every day."
            reona.say "Then seeing how her face lit up when [hero.name] got home from work."
        else:
            reona.say "In fact I've come to love it so much that I think I want more."
            reona.say "I'm pretty sure that [hero.name] sees kids as a part of our future."
            reona.say "So I don't think it'll be long before we have a little addition to the family."
            reona.say "God knows we've been putting in enough practice!"
        reona.say "And don't think for a moment that I've given up on life."
        reona.say "Or that I've just settled for being a home-maker."
        reona.say "I'm working harder at this than I ever have at anything in my life."
        reona.say "I'm also reaping all the rewards of that hard work too."
        reona.say "And who knows, I might choose to go back out there once."
        reona.say "To put my qualifications to use and make a career for myself."
        reona.say "Because if there's one thing [hero.name]'s taught me, it's that I can achieve anything."
        reona.say "So long as I put all that I have into it and really believe in myself."
    else:
        reona.say "You know it's kind of crazy when I actually sat down and thought about all of this."
        reona.say "Actually took the time to look back and take stock of all that we've been though together."
        reona.say "Sometimes I forget that [hero.name] and I met under such totally random circumstances."
        reona.say "Like, if we hadn't been looking at the results for those examinations at the exact same time."
        reona.say "Or if he'd never shown any interest in helping me out with my studies."
        reona.say "We'd be in totally different places right now, with totally different people."
        reona.say "And I can't imagine what would have happened if he'd turned down my advances too!"
        reona.say "But then of course he couldn't - what guy's ever been able to resist my charms?"
        reona.say "Sure, it took him a while to get his head around just how liberated I am in that department."
        reona.say "He had to make sense of it all for himself, I guess."
        reona.say "Really come to terms with the idea of a girl the likes of me being for real."
        reona.say "But once he did, then he never once looked back!"
        reona.say "And it's not like I was the only one dishing out the life-lessons either."
        reona.say "Because when he found out what I'd been through, [hero.name] really helped me out."
        reona.say "I know it might not look like it, but there were times when I could be really down on myself."
        reona.say "Thinking that the only way I could boost my self-esteem was to let any and every guy have his way with me."
        reona.say "[hero.name] showed me that I was wrong to think that way."
        reona.say "Anyone else would have told me that all the flirting and the sex was the problem."
        reona.say "That I has to tone it down in order to deal with all of the emotional issues."
        reona.say "But he taught me that I could separate the two things."
        reona.say "That I could work on building up my self-confidence and sense of worth."
        reona.say "And at the same time I could still indulge the sensual side of my nature."
        reona.say "And boy, did we ever indulge it after that!"
        reona.say "I guess the real lesson he taught me was that I didn't need the attention of every guy I met."
        reona.say "Just that I needed all the attention of the right one."
        reona.say "Once I'd managed to wrap my head around that, everything else just fell into place."
        reona.say "I mean sure, I didn't do as well as I might have in terms of my college grades."
        if reona.is_visibly_pregnant:
            reona.say "And by then, Helen was well and truly on the way."
            reona.say "So we were already a family, and I had the baby to care for."
            reona.say "All of which kind of decided what happened next."
        else:
            reona.say "But luckily for me, [hero.name] already had a plan."
            reona.say "And he kind of saw me as, what did he call it..."
            reona.say "Oh yeah, his 'Trophy Wife'!"
            reona.say "Which I still think sounds kind of cool."
        reona.say "So anyway, we ended up moving in together."
        reona.say "[hero.name]'s career was really starting to take off."
        reona.say "And that meant I could stay at home and be a perfect domestic goddess."
        reona.say "Only it turned out that I'm not so good at that kind of thing."
        reona.say "So I mainly spend my time doing everything I can to look good for him."
        reona.say "Because he works so hard to keep me in the style I've become accustomed to."
        reona.say "And what kind of a wife would I be if I didn't give him something nice to come home too?"
        reona.say "That's why I've been getting into all kinds of exciting new styles and techniques recently."
        reona.say "Everything from Tantric sex to ways of tying each other up for the thrill of it."
        reona.say "And the best thing to do is not give [hero.name] any kind of warning either."
        reona.say "Instead I like to lie in wait, somewhere in the house where he can't see me."
        reona.say "Then I leap out at him as soon as he comes into the house."
        reona.say "Usually he's more than up for discovering all the new stuff I've learned."
        reona.say "But there are times when he clutches his chest and moans about his heart."
        reona.say "Though I tend to put that down to him just being tired from working so hard."
        reona.say "I'm pretty sure he's got many years of fun left in him yet."

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not reona.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_23
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_23
    scene bg black with dissolve
    pause 1.0
    $ game.set_new_game_plus()
    $ renpy.full_restart()


label reona_redemption_ending:

    $ game.room = "church"
    show bg church wedding with fade
    "This is one of those days that I honestly thought would never come around."
    "Like, I know that I asked Reona to marry me and remember her saying yes."
    "And all of the planning that went into today is still right there in my memory."
    "But somehow it all still seems totally unreal, like I'm dreaming and might wake up any second."
    "Even the fact that I'm feeling pretty uncomfortable in my wedding suit doesn't seem to help."
    "Glancing back over my shoulder at the chapel and the pews full of guests - nope, not cutting it."
    "Pulling at the scratchy, stiff collar of my shirt as I break into a nervous sweat - nope!"
    "But then there's the sudden sound of music, swelling to fill the chapel."
    "Oh man, there it is!"
    "The first thing that makes me feel like this is reality."
    show reona wedding normal at center, zoomAt (1.0, (640, 740))
    with fade
    "And when the doors open so that Reona can sweep into the chapel too..."
    "That's when it happens, that's when everything comes into focus."
    "It's real, all of it!"
    show reona wedding normal at center, traveling (1.5, 5.0, (640, 1040))
    "Reona's walking down the aisle towards me, looking like a princess in her dress."
    "Even though the music she chose to enter to is playing, I can hear the murmurs from the guests."
    "All eyes are on her, and all of the words being spoken in hushed tones about how beautiful she looks."
    "It's almost like none of the people in attendance can believe what they're seeing."
    "And I'm chief amongst them."
    "That's her, that's the girl that I'm going to marry!"
    "Maybe what's making everything seem so unreal is the amount of time we've waited for this."
    "The fact that Reona and I agreed not to give in to our natural temptations to be physical."
    "Now all of that pent-up energy is about to be released, our patience is about to pay off."
    "But even now I can feel the need to put a lid on my libido."
    "Because this is a special moment, the ceremony that will unite us and formalise our bond."
    "I'm sure there will be plenty of time for the more carnal side of things later tonight."
    "Right now I need to focus on remembering the words to the ceremony and my part in it."
    "Though when Reona finally makes it to the altar, she seems almost as excited as me."
    show reona talkative
    reona.say "[hero.name]…"
    show reona happy
    reona.say "You'd better pinch me, yeah?"
    reona.say "Because I can't believe we're really doing this!"
    show reona normal
    mike.say "Me too, Reona..."
    mike.say "We're getting married - how crazy is that?"
    "Priest" "Ahem..."
    "At the sound of the priest clearing his throat, Reona and I snap to attention."
    "Both of us standing up straight and turning to face him like soldiers on a parade-ground."
    "Luckily for us, this seems to amuse the priest more than anything."
    "Because I can see a twinkle in his eye as he begins the ceremony in earnest."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To witness the joining together of these two people..."
    "Priest" "In the bonds of holy matrimony..."
    "You really don't need to know what happens next, do you?"
    "I mean, every one knows how these things go."
    "And even if you don't, it's not like I could recount it to you myself."
    "Because everything seems to pass me by in a total blur."
    "The only time I can remember a thing is when I had to actually speak."
    "Priest" "Do you, Reona..."
    "Priest" "Take this man, [hero.name]..."
    "Priest" "To be your lawful, wedded husband?"
    show reona shy blush at startle
    reona.say "I do."
    show reona happy
    "Priest" "Very good."
    "Priest" "And do you, [hero.name]..."
    "Priest" "Take this woman, Reona..."
    "Priest" "To be your lawful, wedded wife?"
    mike.say "You bet I do!"
    "The priest nods and then turns his attention to the assembled guests."
    "Priest" "I call upon those here present..."
    "Priest" "That if you know of any reason these two many not be joined in matrimony..."
    "Priest" "Speak now, or forever hold your peace!"
    "I know that this is the point where everyone looks around and shares a chuckle."
    "But my nerves are frayed to the point where I'm feeling genuinely worried."
    "So it comes as a true relief when the priest nods and gets things moving again."
    "Priest" "So be it."
    "Priest" "It gives me great pleasure to declare you married."
    "Priest" "You may kiss the bride, or the groom..."
    "Priest" "Whatever way you want to do it really - but it is customary to keep it between yourselves!"
    hide reona
    show reona kiss wedding
    with hpunch
    $ reona.flags.kiss += 1
    "I can hardly hear a word the priest is saying as I throw my arms around Reona."
    "And at the same time, she practically leaps into my embrace too."
    "The kiss we exchange starts out pretty tame, but it soon begins to get more intense."
    "And by the time it ends, I can sense the release that's about to happen between us."
    "The fact that we've waited this long means that Reona and I are like a powder-keg."
    "And neither of us needs to say a word on the subject."
    "As we both know that the lid's going to be blown off it tonight!"


    scene reona_redemption_ending with fade
    reona.say "It's so weird to be sitting down to do something like this, to record my thoughts on the way my life's played out."
    reona.say "And not because it's turned out so different to how I thought it would when I was younger either."
    reona.say "To be perfectly honest, I never really spent that much time thinking of such things back then."
    reona.say "No, it feels weird because there was a time when I'd have just laughed in your face if you asked me to do this."
    reona.say "Think deeply and reflect on something I've done?"
    reona.say "Make a record of it as well?"
    reona.say "God, I couldn't have been less interested in doing something like that."
    reona.say "So yeah, back when I was starting out, I was one of those girls without a thought in her head."
    reona.say "Well, unless it was about clothes, make-up or getting the attention of the boys that I liked."
    reona.say "And man, did I ever manage to get their attention!"
    reona.say "Sure, I had all of the usual people in my life telling me that I was making mistakes, that I'd regret it."
    reona.say "But what teenage girl is going to listen to all of that when she has boys falling over themselves to get to her?"
    reona.say "In fact I was so good at getting attention that it soon became the most important thing in my life."
    reona.say "The only problem was that I kept finding things didn't feel so good when I was alone."
    reona.say "Like, I'd be laid in bed at night, and in the silence, all of the voices came back."
    reona.say "The ones that I could easily drown out in the daytime suddenly seemed to be so much louder."
    reona.say "They kept telling me that I wasn't really happy with my life, that I was totally hollow."
    reona.say "But do you think that was enough to make me start listening to them and shaping up?"
    reona.say "Well if you do, then you're dumber than you look!"
    reona.say "No, I chose to do what most people in my position do - to fill that hole with more of the same vices."
    reona.say "Back then I thought that I was getting those black moments because I wasn't doing enough fun shit."
    reona.say "That the answer was more, not less."
    reona.say "So I just kept on repeating the cycle, making it more intense the whole time."
    reona.say "Though I was never totally stupid - I knew that there were other things I needed to get on in life."
    reona.say "The only problem was that there was only one way I knew of to get anything I wanted."
    reona.say "So that's how the whole seducing of the nerds thing started."
    reona.say "In school I needed the grades to pass my exams and go on to college."
    reona.say "And brainy geeks who thought I was hot were the answer to my prayers."
    reona.say "I must have gotten through almost a dozen of those poor suckers before I even laid eyes on Jack for the first time."
    reona.say "I used them and then cast them aside, like I'd cracked open their huge heads and sucked the knowledge out of their brains."
    reona.say "Once I was done with them, they were totally destroyed, but I just told myself they'd get over it."
    reona.say "I told myself it wasn't like any of them would do something dumb and hurt themselves over me..."
    reona.say "Urgh...I hate myself so much sometimes!"
    reona.say "How could I have been that person?"
    reona.say "Any one of those poor boys could have done something desperate because of me!"
    reona.say "And Jack was just another of my victims, someone that I used up and then tossed into the gutter."
    reona.say "Hell, I never even thought of the guy again until after I met [hero.name]."
    reona.say "And yeah, he was already being lined up for the same fate as all the others."
    reona.say "Step one, find you need to pass an exam or write an essay."
    reona.say "Step two, look vulnerable in front of a cute-looking geek."
    reona.say "Step three, charm him into tutoring you and gettin a passing grade."
    reona.say "Step four, keep him sweet while you need him by giving him the keys to the kingdom."
    reona.say "But boy, was I shocked when [hero.name] stopped me from completing step four!"
    reona.say "I went through all of the usual phases of trying to handle rejection."
    reona.say "At first I thought he might not be into girls at all."
    reona.say "Then I assumed that her was scared shitless of me."
    reona.say "But it soon dawned on me that he just didn't want me that way."
    reona.say "Then he really blew my mind by explaining that he did like me, but wanted to get to know me."
    reona.say "This was a crazy thing for me to hear, because I just didn't think anyone could like me for...well, for me!"
    reona.say "I could have walked away right there and then, found someone else to work my tricks on."
    reona.say "But that was when the voices started to come back again, the ones I'd been drowning out for years."
    reona.say "Slowly I began to realise that they sounded a hell of a lot like what [hero.name] was saying."
    reona.say "That I didn't have to give myself away in order to have someone like me."
    reona.say "That there could be meaning in friendship and love that came without a price."
    reona.say "Thing is though, this isn't a fairy-tale, and so that wasn't the end of the story."
    reona.say "Sure, I'd taken the first step, but the rest of the journey wasn't easy either."
    reona.say "And that's where I really started to learn what [hero.name] meant."
    reona.say "Because he was there for me every step of the way."
    reona.say "He supported me when I needed it, and gave me space when I wanted to be alone."
    reona.say "And little by little, my life started to change."
    reona.say "I felt something growing inside of me, small at first, but getting larger all the time."
    reona.say "That thing, I realised was self-respect, the ability to see my value and treasure it."
    reona.say "So there you have it - now I'm a nun!"
    reona.say "Kidding!"
    reona.say "Of course I'm not perfect, and I do still like to sneak off to the bedroom when we get the chance!"
    reona.say "But the Reona you see before you today is, I think, more the person I was always supposed to be."
    reona.say "At least she's the only version of me I think deserves to be married to [hero.name]."
    reona.say "The only version that's worthy of being a mother to Chastity, our little girl."
    reona.say "Who I can hear is calling for me right now!"
    reona.say "Sorry, I'm going to have to go, because it's storytime for her."
    reona.say "As for the future - who knows?"
    reona.say "But at least I have one to look forward to now."
    reona.say "And I'm sure that I can handle whatever it has to bring too."


    scene bg black with dissolve
    pause 1.0
    $ game.set_new_game_plus()
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
