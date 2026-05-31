init python:
    Event(**{
    "name": "sasha_b_event_01",
    "label": "sasha_b_event_01",
    "priority": 500,
    "music": "music/roa_music/smile_for_me.ogg",
    "conditions": [
        IsHour(9, 19),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        ],
    "duration": 1,
    "do_once": True,
    })

    Event(**{
    "name": "sasha_b_event_02_notify",
    "label": "sasha_b_event_02_notify",
    "priority": 500,
    "do_once": False,
    "quit": False,
    "conditions": [
        IsNotDone("sasha_b_event_02"),
        IsHour(9, 0),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom", "kitchen", "bathroom", "bedroom1")),
        PersonTarget(sasha,
            Not(IsHidden()),
            IsRoom("bedroom3"),
            Not(IsActivity("sleep")),
            Not(HasCheated()),
            IsDone("sasha_b_event_01"),
            ),
        ],
    })

    Event(**{
    "name": "sasha_b_event_02",
    "label": "sasha_b_event_02",
    "duration": 1,
    "priority": 500,
    "do_once": True,
    "music": "music/roa_music/smile_for_me.ogg",
    "conditions": [
        IsHour(9, 0),
        HeroTarget(
            IsGender("male"),
            IsRoom("secondfloor", "bedroom3")),
        PersonTarget(sasha,
            Not(IsHidden()),
            IsRoom("bedroom3"),
            Not(IsActivity("sleep")),
            Not(HasCheated()),
            IsDone("sasha_b_event_01"),
            ),
        ],
    })

    Event(**{
    "name": "sasha_b_event_03",
    "label": "sasha_b_event_03",
    "duration": 1,
    "priority": 500,
    "do_once": True,
    "music": "music/roa_music/smile_for_me.ogg",
    "conditions": [
        IsDone("sasha_b_event_02"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("pub"),),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(HasCheated()),
            ),
        ],
    })

    Event(**{
    "name": "sasha_b_event_04_notify",
    "label": "sasha_b_event_04_notify",
    "priority": 500,
    "do_once": False,
    "quit": False,
    "conditions": [
        IsDone("sasha_b_event_03"),
        IsNotDone("sasha_b_event_04"),
        IsHour(18, 0),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom", "kitchen", "bathroom", "bedroom1")),
        PersonTarget(sasha,
            Not(IsHidden()),
            IsRoom("bedroom3"),
            Not(IsActivity("sleep")),
            Not(HasCheated()),
            MinStat("love", 60),
            ),
        ],
    })

    Event(**{
    "name": "sasha_b_event_04",
    "label": "sasha_b_event_04",
    "music": "music/roa_music/smile_for_me.ogg",
    "duration": 1,
    "do_once": True,
    "priority": 500,
    "conditions": [
        IsDone("sasha_b_event_03"),
        IsHour(18, 0),
        HeroTarget(
            IsGender("male"),
            IsRoom("secondfloor", "bedroom3")),
        PersonTarget(sasha,
            Not(IsHidden()),
            IsRoom("bedroom3"),
            Not(IsActivity("sleep")),
            Not(HasCheated()),
            MinStat("love", 60),
            ),
        ],
    })

    AfterDateEvent(**{
    "name": "sasha_b_event_05",
    "label": "sasha_b_event_05",
    "priority": 500,
    "conditions": [
        MinDateScore(90),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(sasha,
            OnDate(),
            MinStat("love", 140),
            ),
        ],
    "do_once": True,
    })

    AfterDateEvent(**{
    "name": "sasha_b_event_06",
    "label": "sasha_b_event_06",
    "priority": 500,
    "conditions": [
        IsDone("sasha_b_event_05"),
        MinDateScore(90),
        PersonTarget(sasha,
            OnDate(),
            MinStat("love", 160),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "sasha_b_event_07",
    "label": "sasha_b_event_07",
    "priority": 500,
    "conditions": [
        IsDone("sasha_b_event_06"),
        HeroTarget(
            IsRoom("kitchen"),
            IsActivity("generic_meal"),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 180),
            ),
        PersonTarget(bree,
            Or(
                IsGone(),
                Not(IsGone()),
                ),
            Not(IsPresent()),
            ),
        PersonTarget("lexi",
            Or(
                IsGone(),
                Not(IsGone()),
                ),
            Not(IsPresent()),
            ),
        PersonTarget(samantha,
            Or(
                IsGone(),
                Not(IsGone()),
                ),
            Not(IsPresent()),
            ),
        PersonTarget(minami,
            Or(
                IsGone(),
                Not(IsGone()),
                ),
            Not(IsPresent()),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "sasha_event_01",
    "label": "sasha_event_01",
    "priority": 500,
    "conditions": [
        IsSeason(0, 1),
        HeroTarget(
            IsGender("male"),
            IsRoom("bedroom1")),
        PersonTarget(sasha,
            Not(IsHidden()),
            IsRoom("pool"),
            IsActivity("sunbath"),
            Not(HasCheated()),
            MinStat("love", 40),
            ),
        ],
    "music": "music/roa_music/smile_for_me.ogg",
    "do_once": False,
    "once_month": True,
    })

    InteractEvent(**{
    "name": "sasha_event_04",
    "label": "sasha_event_04",
    "priority": 500,
    "conditions": [
        IsDone("sasha_event_03"),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        PersonTarget(sasha,
            IsActive(),
            Not(HasCheated()),
            MinStat("love",80),
            ),
        ],
    "music": "music/roa_music/smile_for_me.ogg",
    "do_once": False,
    "once_month": True,
    })

    InteractEvent(**{
    "name": "sasha_event_05",
    "label": "sasha_event_05",
    "priority": 500,
    "conditions": [
        IsDone("sasha_event_04"),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        PersonTarget(sasha,
            IsActive(),
            Not(HasCheated()),
            MinStat("love", 100),
            MaxStat("sexperience", 0),
            ),
        ],
    "music": "music/roa_music/smile_for_me.ogg",
    "do_once": False,
    "once_month": True,
    })

    Event(**{
    "name": "sasha_band_event_01",
    "label": "sasha_band_event_01",
    "duration": 4,
    "priority": 500,
    "do_once": True,
    "conditions": [
        IsDayOfWeek("5"),
        IsHour(20, 21),
        HeroTarget(
            IsGender("male"),
            IsRoom("map"),
            MinFlag("band", 1),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            Not(HasCheated()),
            ),
        ],
    })

    Event(**{
    "name": "sasha_band_event_02",
    "label": "sasha_band_event_02",
    "duration": 4,
    "priority": 500,
    "do_once": True,
    "conditions": [
        IsDayOfWeek("5"),
        IsHour(20, 23),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("pub"),
            MinFlag("performance", 1),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            Not(HasCheated()),
            ),
        ],
    })


    Event(**{
    "name": "sasha_practice_01",
    "priority": 500,
    "label": "sasha_practice_01",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("practice_band"),
            MinFlag("bandpractice", 25),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(HasCheated()),
            MinStat("love", 50),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "sasha_practice_02",
    "label": "sasha_practice_02",
    "priority": 500,
    "do_once": True,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("practice_band"),
            IsFlag("bandcrossdress", True),
            MinFlag("bandpractice", 50),
            ),
        PersonTarget("sasha",
            Not(IsHidden()),
            Not(HasCheated()),
            ),
        PersonTarget("anna",
            Not(IsHidden()),
            Not(HasCheated()),
            ),
        PersonTarget("kleio",
            Not(IsHidden()),
            Not(HasCheated()),
            ),
        ],
    })

    Event(**{
    "name": "scottie_appears",
    "priority": 500,
    "label": "scottie_appears",
    "music": "music/roa_music/smile_for_me.ogg",
    "duration": 1,
    "conditions": [
        MinDaysPlayed(7),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "sasha_scottie_talk",
    "priority": 500,
    "label": "sasha_scottie_talk",
    "music": "music/roa_music/smile_for_me.ogg",
    "duration": 1,
    "conditions": [
        IsDone("scottie_appears"),
        HeroTarget(IsGender("male")),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("scottieDelay", False),
            IsFlag("disable_scottie_events", False),
            MaxStat("love", 99),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "disable_sasha_scottie_talk",
    "priority": 500,
    "label": "sasha_disable_scottie_events",
    "music": "music/roa_music/smile_for_me.ogg",
    "duration": 1,
    "conditions": [
        IsDone("scottie_appears"),
        Not(IsDone("sasha_scottie_talk")),
        HeroTarget(IsGender("male")),
        PersonTarget(sasha,
            IsFlag("disable_scottie_events", False),
            MinStat("love", 100),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "sasha_scottie_bj",
    "priority": 500,
    "label": "sasha_scottie_bj",
    "music": "music/roa_music/smile_for_me.ogg",
    "duration": 1,
    "conditions": [
        IsDone("sasha_scottie_talk"),
        HeroTarget(
            IsGender("male"),
            IsRoom("bedroom3", "secondfloor")),
        PersonTarget(sasha,
            Not(IsHidden()),
            IsRoom("bedroom3"),
            IsFlag("scottieDelay", False),
            IsFlag("disable_scottie_events", False),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "sasha_threesome_request",
    "priority": 500,
    "label": "sasha_threesome_request",
    "music": "music/roa_music/smile_for_me.ogg",
    "conditions": [
        IsDone("scottie_appears"),
        MinDaysPlayed(14),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(HasCheated()),
            IsFlag("disable_scottie_events", False),
            MinStat("love", 100),
            MinStat("sub", -25),
            MaxStat("sub", 24),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "disable_sasha_threesome_request",
    "priority": 500,
    "label": "sasha_disable_scottie_events",
    "music": "music/roa_music/smile_for_me.ogg",
    "conditions": [
        IsDone("scottie_appears"),
        Not(IsDone("sasha_threesome_request")),
        MinDaysPlayed(14),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        PersonTarget(sasha,
            IsFlag("disable_scottie_events", False),
            MinStat("love", 100),
            Or(
                MaxStat("sub", -26),
                MinStat("sub", 25),
            ),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "sasha_likes_blondes_1",
    "label": "sasha_likes_blondes_1",
    "duration": 1,
    "do_once": True,
    "music": "music/roa_music/smile_for_me.ogg",
    "priority": 500,
    "conditions": [
        IsHour(20, 0),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home")),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(HasCheated()),
            MinStat("love", 125),
            ),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    })

    Event(**{
    "name": "sasha_likes_blondes_2",
    "label": "sasha_likes_blondes_2",
    "duration": 2,
    "do_once": True,
    "music": "music/roa_music/smile_for_me.ogg",
    "priority": 500,
    "conditions": [
        IsHour(20, 0),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            IsFlag("LikesBlondes"),
            IsFlag("LikesBlondesDelay", False),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(HasCheated()),
            MinStat("love", 130),
            ),
        ],
    })

    Event(**{
    "name": "sasha_likes_blondes_3",
    "label": "sasha_likes_blondes_3",
    "do_once": True,
    "music": "music/roa_music/smile_for_me.ogg",
    "priority": 500,
    "conditions": [
        IsDone("sasha_likes_blondes_2"),
        HeroTarget(
            IsGender("male"),
            IsFlag("LikesBlondesDelay", False),
            IsFlag("LikesBlondes", False),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            Not(HasCheated()),
            ),
        ],
    })

    Event(**{
    "name": "sasha_breast_complex_1",
    "label": "sasha_breast_complex_1",
    "duration": 1,
    "do_once": True,
    "music": "music/roa_music/smile_for_me.ogg",
    "priority": 500,
    "conditions": [
        IsHour(20, 0),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        PersonTarget(sasha,
            Not(IsHidden()),
            Not(HasCheated()),
            MinStat("love", 50),
            ),
        ],
    })

    Event(**{
    "name": "sasha_breast_complex_2",
    "label": "sasha_breast_complex_2",
    "music": "music/roa_music/smile_for_me.ogg",
    "duration": 1,
    "do_once": True,
    "priority": 500,
    "conditions": [
        IsDone("sasha_breast_complex_1"),
        IsSeason(0, 1),
        IsDayOfWeek("67"),
        HeroTarget(
            IsGender("male"),
            IsRoom("pool")),
        PersonTarget(sasha,
            Not(IsHidden()),
            Not(HasCheated()),
            MinStat("love", 100),
            MinStat("sub", 75),
            ),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            "bree.get_clothes() == 'swimsuit'",
            ),
        ],
    })

    Event(**{
    "name": "sasha_breast_complex_3",
    "music": "music/roa_music/smile_for_me.ogg",
    "label": "sasha_breast_complex_3",
    "duration": 1,
    "do_once": True,
    "priority": 500,
    "conditions": [
        IsDone("sasha_breast_complex_2"),
        IsTimeOfDay("morning"),
        HeroTarget(
            IsGender("male"),
            IsRoom("bathroom")),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            Not(HasCheated()),
            MinStat("love", 150),
            MinStat("sexperience", 1),
            ),
        ],
    })

    Event(**{
    "name": "sasha_breast_complex_4",
    "label": "sasha_breast_complex_4",
    "music": "music/roa_music/smile_for_me.ogg",
    "duration": 1,
    "do_once": True,
    "priority": 500,
    "max_girls": 1,
    "conditions": [
        IsDone("sasha_breast_complex_3"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsFlag("BreastComplexDelay", False),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            Not(HasCheated()),
            IsFlag("BreastComplex"),
            ),
        ],
    })

    Event(**{
    "name": "sasha_breast_complex_5",
    "label": "sasha_breast_complex_5",
    "duration": 1,
    "music": "music/roa_music/smile_for_me.ogg",
    "do_once": True,
    "priority": 500,
    "conditions": [
        IsDone("sasha_breast_complex_4"),
        IsHour(10, 18),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            IsFlag("BreastComplexDelay", False),
            ),
        PersonTarget(sasha,
            Not(HasCheated()),
            IsFlag("BreastComplex"),
            ),
        ],
    })

    Event(**{
    "name": "sasha_event_coffee",
    "label": "sasha_event_coffee",
    "priority": 500,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("date_coffee")),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            Not(HasCheated()),
            MinStat("love", 50),
            ),
        ],
    "music": "music/roa_music/smile_for_me.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "sasha_sub_event_1",
    "label": "sasha_sub_event_1",
    "priority": 500,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("kitchen")),
        PersonTarget(sasha,
            IsActive(),
            Not(HasCheated()),
            MinStat("love", 125),
            MinStat("sub", 75),
            ),
        ],
    "music": "music/roa_music/smile_for_me.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "sasha_kiss_me",
    "label": "sasha_kiss_me",
    "max_girls": 1,
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            Not(HasCheated()),
            MinFlag("kiss", 1),
            MinStat("love", 150),
            ),
        ],
    "music": "music/roa_music/smile_for_me.ogg",
    "chances": 20,
    "once_day": True,
    "do_once": False,
    "quit": False,
    })

    Event(**{
    "name": "sasha_preg_talk",
    "label": "sasha_preg_talk",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate())
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(HasCheated()),
            IsFlag("toldpreg", False),
            MinCounter("pregnant", 6),
            ),
        ],
    "music": "music/roa_music/smile_for_me.ogg",
    "once_day": True,
    "do_once": False,
    "quit": False,
    })

    Event(**{
    "name": "sasha_event_bree_shower",
    "label": "sasha_event_bree_shower",
    "duration": 1,
    "music": "music/roa_music/smile_for_me.ogg",
    "conditions": [
        IsNotDone("sasha_event_bree_shower_2"),
        IsHour(20, 22),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsRoom("bedroom1"),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            MaxStat("love", 45),
            MinStat("lesbian", 10),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            MaxStat("love", 45),
            MinStat("lesbian", 10),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "sasha_event_bree_shower_2",
    "label": "sasha_event_bree_shower",
    "duration": 1,
    "music": "music/roa_music/smile_for_me.ogg",
    "conditions": [
        IsNotDone("sasha_event_bree_shower"),
        IsActiveHarem('home'),
        IsHour(20, 22),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsRoom("bedroom1"),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            MinStat("lesbian", 10),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            MinStat("lesbian", 10),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "sasha_shower_BJ",
    "label": "sasha_shower_BJ",
    "duration": 1,
    "conditions": [
        IsHour(20, 0),
        HeroTarget(
            IsGender("male"),
            IsActivity("take_a_shower")
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 150),
            MinStat("sub", 50),
            MinStat("sexperience", 1),
            ),
        ],
    "music": "music/roa_music/smile_for_me.ogg",
    "once_week": True,
    "once_day": False,
    "do_once": False,
    })

    InteractEvent(**{
    "name": "sasha_nightclub_comment",
    "label": "sasha_nightclub_comment",
    "conditions": [
        HeroTarget(IsGender("male")),
        Not(InInventory("fancy_clothes")),
        PersonTarget(sasha,
            IsActive(),
            ),
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "sasha_wearing_strapon",
    "label": "sasha_wearing_strapon",
    "priority": 1000,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("bedroom3")
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            MinStat("love", 140),
            ),
        ],
    "chances": 20,
    "do_once": True,
    "once_hour": False,
    })

    Event(**{
    "name": "sasha_pregnant_request",
    "label": "sasha_pregnant_request",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            IsFlag("status", "girlfriend"),
            MaxCounter("pregnant", 8),
            ),
        'game.days_played - sasha.flags.girlfriend_day >= 7',
        ],
    "once_day": False,
    "do_once": True,
    "quit": False,
    })

    SpecificTalkSubject(**{
    "name": "askaboutsasha",
    "display_name": "About Sasha",
    "label": "sasha_cheated_sam_advice",
    "icon": "button_sasha",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(samantha,
            IsActive(),
            IsFlag("knows_ryancheats"),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            HasCheated(),
            IsFlag("cheatedSamAdvice", False),
            ),
        ],
    "do_once": True,
    })

    WakeUpEvent(**{
    "name": "sasha_morningwood",
    "priority": 500,
    "label": "sasha_morningwood",
    "duration": 1,
    "conditions": [
        IsHour(5, 9),
        HeroTarget(IsGender("male"),
            Not(InFlag("slept_with", "sasha")),
            Not(IsFlag("morningwood")),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            IsActivity("sleep"),
            MinStat("love", 160),
            MinStat("sexperience", 2),
            ),
        RoomTarget("bedroom3",
            NPCNumber(1),
             NPCInRoom("sasha",),
            ),
        ],
    "chances": 20,
    "do_once": False,
    "once_month": True,
    })

label sasha_b_event_01:
    if game.room == "kitchen":
        scene bg kitchen
        "I ignore the toast that pops up from the toaster and go to open the door, since by the sound of those keys she's having trouble with it."
    else:
        scene bg livingroom
        "The sound of keys rattling gets my attention; it is too early for [bree.name] to have gone anywhere --unless she was coming home from the night before-- so it means that Sasha must be here!"
    scene bg black with dissolve
    scene bg house
    show sasha box normal
    with wiperight
    "When I open the door, all I see is a stack of boxes with a pair of long, bare legs sticking out from underneath them; the brown cardboard cartons are above the level of the girl's head."
    menu:
        "Invite her in":
            show sasha box angry
            mike.say "Come on in, Sasha."
            "I move out of her way so she has room to haul her stuff inside, then I follow."
            "When she comes back out of the room, I say hello."
        "Help her":
            mike.say "Oh jeez, let me help you with those."
            "I take the top two boxes carefully, and see a very pretty face framed by black hair, smiling at me."
            show sasha box happy
            "I lead the way to her room and deposit her stuff just inside the door, then step out into the hallway, turning to say hello when she comes out."
            $ sasha.love += 2
        "Take the boxes from her" if hero.fitness >= 5:
            mike.say "Here, give me those."
            "I take the boxes without waiting for her to respond, lifting them easily, and turn to take them to her new room."
            "When I come back out, she's standing in the hallway and I go to say hello."
            $ sasha.love += 3
            $ sasha.sub += 1
        "Go grab more boxes outside":
            mike.say "Oh hey! Yours is the first door on the left down the hall; I'll go out and grab another load for you, okay?"
            show sasha box happy
            "A muffled 'mm-hmm' comes from behind the boxes and I step aside so she has plenty of room to navigate. Heading out the door, I go up to her car, a small black two-door."
            "It has bumper stickers for metal and goth bands plastered all over the back of it, and a pair of little black rubber bats hangs from the rearview mirror where some people would hang fuzzy dice."
            "I grab a load of her stuff from the back seat and head back into the house, taking them into her room and setting them down. When I turn to head back out, she's standing in the hallway and I go to say hello."
            $ sasha.love += 1
    hide sasha
    scene bg livingroom with fade
    show sasha casual2
    mike.say "Hey, welcome to the house... Sasha ...?"
    "I'm fairly sure that's the right name; I've only met her once briefly."
    show sasha casual2 at center, zoomAt(1.5, (640, 1040))
    "I stick out my hand and she gives it a shake with a firm and confident grip, and I notice her nails are painted black."
    show sasha happy
    "She smirks, which actually looks pretty on her face, and pushes long inky hair back."
    sasha.say "I must be, since it'd be pretty funky if some other random girl just wandered in here with a stack of boxes."
    show sasha normal
    "She responds with a touch of surprisingly appealing sass."
    menu:
        "Joke" if hero.charm >= 8:
            mike.say "Nah, I get strange girls coming and going here all the time. Just usually not so early in the morning!"
            show sasha happy
            "I grin a little to show her I'm joking and she chuckles and shakes her head."
            show sasha shout
            sasha.say "In that case, I better sound-proof my room."
            show sasha happy
            "She retorts, surprising me into a startled laugh."
            $ sasha.love += 2
        "Laugh" if hero.charm >= 4:
            "I roll my eyes a little, but chuckle; if Sasha's always like this, it will add some amusing sarcasm to the house, though she probably won't get on all that well with [bree.name] at first."
            mike.say "Let's go get the rest of your stuff, non-random girl who wandered in here."
        "Be awkward":
            mike.say "Guess it would be, huh?"
            "I shuffle my feet a little and glance down with a small smile."
            mike.say "Want me to go get some more of your stuff, Sasha?"
            $ sasha.sub -= 5
    "Together, we manage to haul most of her stuff into her bedroom, where Sasha can sort it from there; she says she's going to come by with a U-Haul later today with her furniture."
    mike.say "I've got to go now. I'll see you when I get home; welcome to the house, Sasha."
    hide sasha
    return

label sasha_b_event_02_notify:
    $ renpy.say("", randchoice(["I hear banging from the hallway. Maybe I should see what's going on?", "I hear a loud thump from the hallway.", "I can distantly hear the sound of swearing. I think it's coming from the hallway."]))
    return

label sasha_b_event_02:
    if sasha.love.max < 40:
        $ sasha.love.max = 40
    show bg secondfloor
    "I walk in to the sound of boxes toppling over and some grade-A creative cursing."
    "Sounds like Sasha is trying to get things unpacked!"
    "I walk down the hallway and peer into her room; she's managed to muscle a dresser and a bookshelf into the room by herself, but the U-haul is still outside with her bed and a little more furniture in it."
    scene bg bedroom3
    show sasha upset
    with dissolve
    "Several boxes lay on the floor, a few with books and clothing tumbled out of them; they must have been stacked and fallen over."
    "Sasha looks frustrated enough to throw something."
    menu:
        "Tell her to keep it quiet":
            mike.say "Hey, I get that this is frustrating, but can you try to keep it down?"
            play sound door_slam
            pause 0.4
            scene bg door bedroom3 at center, zoomAt(1.25, (640, 880))
            with hpunch
            "She slams the door shut after glaring at me.."
            $ sasha.love -= 5
            return
        "Offer to help":
            show sasha normal
            mike.say "Hey, looks like you've got a lot going on here; need some help with unpacking?"
            $ sasha.love += 2
            show sasha shout
            sasha.say "What I really need is some muscle to help move the furniture in. You game?"
            show sasha normal
            menu:
                "Accept" if hero.energy > 2:
                    mike.say "Sure, let's get these boxes out of the way and we'll get started!"
                    $ sasha.love += 2
                "Refuse":
                    mike.say "Sorry, I don't have time right now."
                    $ sasha.love -= 2
                    return

    hide sasha
    scene bg house with fade
    "Sitting in the U-Haul are a full-size bed, a small computer desk, a beat-up green recliner, and a pair of nightstands."
    "On the lawn are a stand lamp and a desk lamp, along with a few stray boxes."
    show sasha shout at center, zoomAt(1.25, (540, 880)) with easeinleft
    sasha.say "Let's get started with the bed."
    show sasha normal
    "Sasha says to me with a small grin."
    menu:
        "Joke and agree" if hero.charm >= 10:
            mike.say "Already? That's quick."
            "I respond with a wink to show I'm just teasing."
            show sasha happy
            sasha.say "Yeah, well, no point in waiting. It's got to happen eventually, right?"
            show sasha normal
            "Sasha smirks."
            "I chuckle at her response, and we get started hauling the furniture in, too busy to converse much further for the moment."
            $ sasha.love += 1
        "Just agree":
            mike.say "Whatever you say."
            "I reply, moving to the split box-spring to take an end of it while she takes the other."
            mike.say "You're the boss, boss."
            show sasha happy
            sasha.say "Heh. Damn right I am."
            show sasha normal
            "She answers, taking her own end so we can start lugging it inside."
            $ sasha.love += 1
    scene bg bedroom3
    show sasha shout at center, zoomAt(1.25, (640, 880))
    with fade
    sasha.say "You wanna help me get these boxes empty?"
    sasha.say "I'll be able to sort everything out and get stuff where it belongs way easier if I can just see everything."
    show sasha normal
    "Sasha watches me with those pretty, dark eyes and a small half-smile."
    menu:
        "Refuse":
            mike.say "Sorry, I don't have time tonight."
            "I've got to get a good night of sleep so I can keep pushing for that promotion at work."
            $ sasha.love -= 1
            return
        "Accept" if hero.energy > 5:
            mike.say "Sure, let me get the box cutter."
            $ sasha.love += 1
    with fade
    "I help her get her bed and the furniture placed just where she wants them and then get started opening up the slew of boxes she's got scattered through the room."
    "Sasha has a lot of books!"
    "All sorts of topics, with a lot of fantasy and science fiction."
    "Plenty of music too; her CD tower is going to be full before they're all unpacked."
    "She's got a nice stereo set up on the big book shelf, and I prepare myself to deal with some loud music now and then."
    scene unpack sasha with fade
    "I sit on the edge of the bed and slit the flaps open on a smallish box, then open it up and blink in surprise."
    "It's full of toys, and not the kind kids play with!"
    show unpack sasha mikeshy
    mike.say "Wow."
    "I murmur softly before I can stop myself."
    "Sasha turns and looks at me with a brow raised, then grins as she sees the box I've opened."
    "She shows no shame at all, no shyness or embarrassment; this woman is confident!"
    sasha.say "What, you've never seen sex toys before?"
    menu:
        "No":
            mike.say "Well... no."
            "I say a little defensively, suddenly feeling shy under her frank gaze."
            $ sasha.love += 1
            show unpack sasha blush
            sasha.say "Aww."
            "Sasha coos with a little smile."
            sasha.say "Well, take a good look and get an education!"
            show unpack sasha mikenormal normal
            menu:
                "Don't look at the toys":
                    mike.say "No, it seems sort of private to me. I'll leave it on your nightstand."
                    $ sasha.love -= 1
                    $ HIDE_UI = True
                    scene bg black with dissolve
                    pause 0.1
                    scene bg bedroom3
                    $ HIDE_UI = False
                    show sasha
                    "Job done, I tuck the box-cutter back in my pocket."
                    mike.say "That's the last of them!"
                    menu:
                        "Offer more help" if hero.energy > 7:
                            mike.say "Do you need any more help?"
                            "Sasha shakes her head."
                            sasha.say "Nah, thanks. You've done your Big Strong Man deed for the day."
                            $ sasha.love += 1
                        "Stop helping":
                            mike.say "That's it for me. Good luck with your unpacking!"
                    sasha.say "Thanks for the help. Catch you later."
                    "She then moves to the next box of stuff."
                    return
                "Look at the toys":
                    pass
                "Joke" if hero.charm >= 10:
                    mike.say "Planning on a demonstration?"
                    "I ask with a snicker. Sasha laughs and wags her finger mock-scoldingly at me, then goes back to putting her books on the shelf."
                    $ sasha.love += 1
            show unpack sasha search
            "I start sorting through the box."
            show unpack sasha dildo shown
            "Which has several dildos of various sizes --including one that sort of astounds me--."
            show unpack sasha vibrator
            "A few of which have control knobs for vibration."
            "A box of ribbed condoms is in here as well, along with what looks like a leather thong!"
            show unpack sasha -vibrator -shown search
            "I pull the thong out and realize what it is by the circular opening at the front; a strap on!"
            show unpack sasha mikeshy
            mike.say "So, you're into girls?"
            "Sasha smirks at me."
            show unpack sasha evil
            sasha.say "And boys. Never know what you'll like until you try it!"
            menu:
                "Be surprised" if hero.charm < 10:
                    show unpack sasha mikefear
                    mike.say "You use this on guys?"
                    "I cringe a little at the thought and shake my head; no way I'd let a girl use one of these on me, no matter how hot she is!"
                    "Sasha shrugs, seeming disinterested suddenly and returns to putting away her books."
                    sasha.say "Everybody has their kinks."
                    sasha.say "Go ahead and leave the box on the nightstand; I'll put that stuff away later."
                    "I put the strap-on back in the box and resume the process of getting all the other boxes open, wondering if there are more surprises in store."
                    $ sasha.love -= 1
                "Be surprised" if hero.charm >= 15:
                    show unpack sasha mikenormal
                    mike.say "You use this on guys?"
                    "I look at it with even more curiosity, wondering how that would feel."
                    "I've heard that it can feel really good, but I've never given it much thought before."
                    "Seeing the equipment that would let a girl do it, now I'm curious."
                    "Sasha smiles a little and shrugs."
                    show unpack sasha normal
                    sasha.say "Sure. Some guys really love it. Especially the submissive ones. And I like being in control."
                    "She adds with a grin."
                    sasha.say "Go ahead and leave the box on the nightstand."
                    $ sasha.love += 1
                "Be interested":
                    show unpack sasha mikeshy
                    mike.say "Wow.. that.. seems kinda hot."
                    "I wonder how it would feel, and I peer in the box at the various dildos that might fit into the strap-on with curiosity."
                    "Sasha grins wickedly at me."
                    show unpack sasha evil
                    sasha.say "Oh, believe me, it's hot. Go ahead and leave the box on the nightstand."
                    $ sasha.love += 2
        "Yes":
            show unpack sasha mikenormal normal
            mike.say "Sure I've seen sex toys before, but not this many unless I was in a sex shop!"
            "I grin at her, making sure my tone is teasing so she won't get offended."
            show unpack sasha evil
            sasha.say "Spend much time in sex shops, do you?"
            show unpack sasha blush
            "She smirks at me."
            menu:
                "Yes":
                    mike.say "Hey, everybody needs a little spice in the bedroom, right?"
                    "Sasha grins."
                    show unpack sasha evil
                    sasha.say "Absolutely. The spicier, the better! Go ahead and put that on the nightstand; I'll unpack it later."
                    $ sasha.love += 2
                "No":
                    mike.say "Ha! No, I don't need any help in that department."
                    mike.say "No I was always too shy..."
                    "Sasha grins."
                    show unpack sasha evil
                    sasha.say "Don't know what you're missing. Go ahead and put that on the nightstand; I'll unpack it later."
    scene bg bedroom3 with fade
    "The Naughty Box set aside on the nightstand, I open up the rest of the boxes so she can see what stuff she's got where."
    "Job done, I tuck the box-cutter back in my pocket."
    show sasha at center, zoomAt(1.25, (640, 880)) with dissolve
    mike.say "That's the last of them!"
    menu:
        "Offer more help" if hero.energy > 7:
            mike.say "Do you need any more help?"
            "Sasha shakes her head."
            show sasha shout
            sasha.say "Nah, thanks. You've done your Big Strong Man deed for the day."
            $ sasha.love += 1
        "Stop helping":
            mike.say "That's it for me. Good luck with your unpacking!"
    show sasha shout
    sasha.say "Thanks for the help. Catch you later."
    show sasha normal
    "She then moves to the next box of stuff."
    return

label sasha_b_event_03:
    if sasha.love.max < 60:
        $ sasha.love.max = 60
    "The Winchester is a little better lit than most bars, and the music --a local Classic Rock station-- is played low enough to not make people have to shout over it; it's my favorite place to grab a drink and maybe some good Pub food after work."
    "I go in and look over the tables, and see that there are plenty of little round two-seaters free before I glance toward the back of the room at the pool tables, and there I see a pair of familiar and very lovely legs."
    show sasha play pool with fade
    "Sasha is bent over the pool table, cue in hand, getting ready to take a shot."
    "Her little pert ass looks fantastic in those cut-off jean-shorts and I indulge myself a moment staring at her; that position is extremely sexy and distracting."
    "It's distracting to the other guys around the pool table too; she's got several pairs of eyes on that ass."
    menu:
        "Talk to her":
            "I ignore the bar and tables for the moment and walk up to stand beside Sasha."
            hide sasha
            show sasha
            "She straightens up with a little bit of surprise in her big dark eyes, then flashes me a grin."
            show sasha shout
            sasha.say "Well well, fancy meeting you here. Care to lose some money?"
            show sasha normal
            menu:
                "No":
                    mike.say "Pass, but I'll buy you a drink."
                    "I'm pleased when Sasha agrees and I go to the bar, bringing back her rum and cola along with my mug of beer."
                    "I enjoy the view of her taking those difficult shots leaned over the pool table, and she notices me looking, but I just flash her a grin."
                    $ sasha.love += 1
                "Yes":
                    mike.say "Nah, but I'm down for winning some."
                    "I say as I grab a cue off of the wall and the triangle to rack the balls back up."
                    hide sasha
                    show sasha play pool
                    with fade
                    "I'm good at pool, but so is she, and damned if she isn't distracting as hell the way she takes those shots in those tiny shorts."
                    "And she knows it too, flashing me a bit of a grin when she catches me looking."
                    hide sasha
                    show sasha
                    if randint(0, 1) == 1:
                        if hero.money >= 10:
                            $ hero.money -= 10
                        else:
                            $ hero.money.val = 0
                        show sasha shout
                        sasha.say "Good thing we were only betting a buck. A guy like you could lose his shirt to a gal like me."
                        show sasha normal
                        if randint(0, 1) == 1:
                            mike.say "Oh, you want me shirtless already?"
                            "I smile innocently as I ask the question, arching a brow, and she starts laughing good-naturedly."
                            $ sasha.love += 1
                        else:
                            mike.say "If we're betting shirts, I think the folks around here would prefer you lose!"
                            "I grin at her and she snickers, glancing around at the guys paying attention to the way she moves."
                            $ sasha.love += 2
                    else:
                        show sasha shout
                        sasha.say "You're pretty good! I haven't had that much fun playing pool in a while."
                        show sasha normal
                        $ sasha.love += 2
                    mike.say "You know, it's a little unfair playing with someone that gets so distracting taking those tough-angle shots."
                    $ sasha.love += 1
            hide sasha with fade
            "We go to the bar and I order a beer when the waitress comes over."
        "Leave her alone":
            hide sasha
            show bar
            with fade
            "I go to the bar and order a beer when the waitress comes over."
            "When Sasha finishes her game, taking a couple of bucks bet by a guy who was too distracted by her legs to play well, she turns and sees me."
            "I raise my hand in a friendly wave, and she saunters over after putting her pool queue back."
            hide bar
    show sasha shout
    sasha.say "Come here often?"
    show sasha normal
    mike.say "Often enough."
    mike.say "See you found the local hang-out easy enough. How's the moving going?"
    if game.days_played < 7:
        show sasha shout
        sasha.say "Slow. Most of my boxes are in, but I'm gonna need help with the furniture."
        sasha.say "Care to be my hero?"
        show sasha normal
        menu:
            "Yes, later":
                mike.say "Why not? But for now, let's have dinner."
                menu:
                    "Invite her" if hero.money >= 50 and hero.energy > 3:
                        $ hero.money -= 50
                        mike.say "I'll buy, it's my duty to show my new roommate a warm welcome."
                        "Sasha smiles and agrees."
                        "She scoots the chair to sit beside me to look over the menu and get food suggestions, and we make small-talk over dinner before heading back to the house."
                        $ hero.hunger += 8
                        $ sasha.love += 1
                    "Order food":
                        "Sasha agrees, asking for food recommendations since she's never been here before, and we make a little small-talk over the meal before heading back to the house."
                        $ hero.hunger += 3
                $ game.pass_time(1)
            "Yes, now" if hero.energy > 5:
                mike.say "I'd love to help. Do you want to go now?"
                "Sasha nods and gets up; she follows me home, and we get to work moving furniture."
                $ sasha.love += 2
                $ game.pass_time(1)
                $ game.room = "livingroom"
            "No":
                mike.say "Sorry, I don't really have the time."
                $ sasha.love -= 1
    else:
        show sasha shout
        sasha.say "It's over already, but thanks for asking."
        show sasha normal
        "We chat a little before going back home."
    scene bg black with dissolve
    return

label sasha_b_event_04_notify:
    $ renpy.say("", randchoice(["I hear some strange noises coming from the hallway. Maybe I should see what's going on?", "I hear a crashing from the hallway.", "I can distantly hear the sound of a guitar out of tune. I think it's coming from the hallway."]))
    return

label sasha_b_event_04:
    scene bg secondfloor
    play music "<from 7 to 188>music/deathless_harpies/Deathless_Harpies_Bass_outside.ogg" loop
    "I walk down the hall and stand outside of Sasha's door, listening, and it turns out I was right: it's the sound of a bass guitar, playing the bass line from an unknown rock song."
    "And just the bass line, which meant someone had very esoteric taste in music, or someone was actually playing the instrument."
    menu:
        "Leave":
            "Never had a musician for a room mate before."
            "I hope she doesn't play too late at night!"
            "I head back toward the kitchen, leaving Sasha alone to practice."
            $ hero.cancel_event()
            return
        "Open the door":
            scene bg bedroom3
            play music "<from 7 to 188>music/deathless_harpies/Deathless_Harpies_Bass_SashaRecording.ogg" loop
            show bass training sleep
            with wiperight
            "Curious, I open the door and peak inside to see Sasha sitting on the edge of her bed."
            "I'm lucky; her back is towards me so she won't catch me snooping."
            "Can't see the instrument, but I can enjoy the sound for a bit."
            stop music
            "I finally decide to call out to her and she abruptly stops playing."
            hide bass training
            show sasha sleep
        "Knock on the door":
            scene bg door bedroom3 at center, zoomAt(1, (640, 720)) with fade
            show bg door bedroom3 at center, traveling(1.5, 0.3, (640, 1040))
            pause 0.3
            play sound door_knock_light
            stop music
            "Curious, I knock lightly on her door and the music abruptly stops."
            "Yep, definitely Sasha as the musician."
            scene bg black with dissolve
            pause 0.5
            scene bg bedroom3
            show sasha sleep
            with wipeleft
            "A moment later and the door opens, revealing Sasha still in her PJs: super short shorts and a snug shirt, both in dark colors (surprise, surprise.)"
    play music "music/roa_music/smile_for_me.ogg" loop
    if sasha.love.max < 140:
        $ sasha.love.max = 140
    $ sasha.flags.schedule = "studio"
    mike.say "Hey, Sasha. I didn't know you played music."
    "I glance over at the radiance red bass guitar sitting on its stand. That must be hers."
    show sasha sleep shout
    sasha.say "Oh, yeah! Been playing for about five years now."
    sasha.say "Even got a band, mostly goth-punk stuff, some covers."
    show sasha normal
    menu:
        "Don't play too late.":
            "Sasha sounds excited to talk about this topic, but it's not really my thing."
            mike.say "That's cool. Just don't play too late, huh?"
            show sasha sleep angry
            pause 0.2
            play sound door_slam
            pause 0.4
            scene bg door bedroom3 at center, zoomAt(1.25, (640, 880))
            with hpunch
            "I wonder why she closes the door so sharply."
            $ sasha.love -= 5
        "That's great." if not hero.has_skill("guitar"):
            mike.say "Very cool!"
            "I do enjoy music, especially live shows."
            mike.say "Where do you play? Maybe I could catch a show some time."
            "Sasha gets an excited look in those pretty eyes."
            "It seems she likes the idea of having someone be enthusiastic about her music with her."
            show sasha shout
            sasha.say "We usually play down at the Black Box."
            show sasha normal
            "I've driven past the place before; cube-shaped black building, hence the name, usually catering to teens-20 somethings and playing alternative, goth, and punk music."
            "Some of that stuff is pretty good."
            mike.say "I know where it is. When's the next performance?"
            "She grins and saunters over to grab her bass by the neck, sitting on the bed as she most likely had been before I knocked."
            show sasha shout
            sasha.say "Pretty soon, I'll tell you when I know exactly. You should absolutely come; you'll have a blast. Plus, cheap drinks!"
            show sasha normal
            "I flash her a grin."
            mike.say "You had me at 'got a band'."
            play music "<from 7 to 188>music/deathless_harpies/Deathless_Harpies_Bass_SashaRecording.ogg" loop
            hide sasha
            show bass training sleep at center, zoomAt(1.5, (640, 1140))
            with fade
            "Sasha grins right back at me, starting to pluck the bass strings again."
            "I close the door to give her better acoustics for practicing."
            "Looks like I'll be hitting the bar pretty soon!"
            $ sasha.love += 1
            $ game.flags.performance = 1
        "That's great." if hero.has_skill("guitar"):
            "How cool! I was living with another musician."
            mike.say "Really? Hey, I play guitar. Maybe we could play together some time."
            "It would be a good way to bond with her."
            show sasha shout
            sasha.say "I'll do you one better! We're practicing every Friday at 8pm; wanna come hang and maybe jam with us after?"
            show sasha normal
            "That's the best offer I've had all week; I rarely get to play music with anyone else these days."
            "My old garage band days were over, though I suspected that attending this practice would put me in a garage again. Fine with me."
            mike.say "I'd love to! Gonna perform soon?"
            show sasha shout
            sasha.say "Yeah, we've got a gig at the Black Box on pretty soon."
            sasha.say "They do pretty good shows there, and the booze is cheap."
            sasha.say "Feel free to swing by if you're in the mood for goth or punk music."
            show sasha normal
            "Sometimes I was in the mood for punk music."
            "I didn't know much goth stuff, but maybe she'd wind up getting me into it."
            "Could be fun."
            mike.say "Make sure to give me the date and time when you have it."
            play music "<from 7 to 188>music/deathless_harpies/Deathless_Harpies_Bass_SashaRecording.ogg" loop
            hide sasha
            show bass training sleep at center, zoomAt(1.5, (640, 1140))
            with fade
            "I walked into the bedroom and we both sat on the edge of the bed."
            "I stayed with Sasha for a while, just listening to her music."
            $ sasha.love += 2
            $ game.flags.band = 1
    return

label sasha_b_event_05:
    show bg street
    show sasha at center, zoomAt(1.25, (640, 880))
    with fade
    "I'm no expert on the subject, but I get the distinct feeling that, all things considered, tonight's date went pretty well."
    "Neither of us came out and said as much, yet the atmosphere between us as we walk home just feels that good."
    "You know what I mean?"
    "One of those times when you can't say what it is, but everything feels right."
    "I mean, Sasha's not declaring her undying love for me, or anything like that."
    "Hell, we're not even holding hands as we walk along together."
    "And yet that same feeling is there, hanging in the air between us."
    "Which is one of the reasons that I'm almost afraid to say too much, or too little."
    "I'm that afraid of doing something to spoil the mood, to ruin the moment."
    show sasha embarrassed
    "Sasha must have picked up on it too, as she keeps casting sideways glances at me."
    "But maybe she's not as finely tuned in to the thoughts going through my head as I assumed."
    "Because after a short while, she's the one to break the silence between us."
    show sasha shout
    sasha.say "You okay, [hero.name]?"
    sasha.say "I mean, if you want to be quiet, that's fine."
    sasha.say "But you were really chatty tonight."
    sasha.say "And I kind of noticed the change in you just now."
    show sasha normal
    "I shake my head hastily, eager to dispel any illusions that Sasha might have as to why I'm not talking."
    mike.say "No, Sasha."
    mike.say "There's nothing up - really."
    mike.say "I just felt like this was one of those times, you know?"
    mike.say "When you're supposed to just keep quiet and enjoy the moment."
    show sasha embarrassed
    "Now it's Sasha's turn to look uncomfortable."
    show sasha blush
    sasha.say "Oh...right...I see."
    sasha.say "Erm...does that mean I just ruined your moment?"
    show sasha shy
    "I can't help letting out a chuckle at this, shaking my head again."
    mike.say "No way, Sasha - don't worry about it."
    mike.say "I just had a really great time tonight."
    mike.say "And I guess I'm overthinking the whole thing."
    show sasha embarrassed
    sasha.say "Me too, [hero.name]."
    sasha.say "That is, I had a good time too."
    sasha.say "Not that I'm overthinking it...though I might be starting to now!"
    show sasha shy
    "Sasha stops talking and looks me in the eye."
    "And we stay like that for a moment, almost frozen in place."
    show sasha happy at startle
    "But then, almost at the same instant, we both burst out laughing."
    show sasha shout
    sasha.say "Oh god..."
    sasha.say "This is SO dumb!"
    show sasha normal
    mike.say "I know, right?!?"
    mike.say "It's like both of us want to say something real bad."
    mike.say "But we can't find the words!"
    show sasha shout
    sasha.say "Yeah, yeah..."
    sasha.say "Neither of us knows how to just come out and say it!"
    sasha.say "Say that we really like each other..."
    show sasha normal
    "And just like that, both of us fall silent again."
    "Sasha just managed to say what neither of us could say by joking about it."
    "I have no idea what that says about the pair of us."
    "But I hope that it's something good!"
    mike.say "You...you mean that, Sasha?"
    show sasha shout
    sasha.say "It kind of slipped out without me thinking about it."
    sasha.say "So, yeah...I guess it must be true!"
    show sasha normal
    mike.say "I think so too."
    mike.say "That is...I feel the same way, Sasha."
    mike.say "Not that I think what you think about what you just said..."
    mike.say "Ah, this is getting confusing!"
    show sasha shout
    sasha.say "Okay, okay - let's start again."
    sasha.say "I like you, [hero.name]...a lot."
    show sasha normal
    mike.say "And I like you too, Sasha...a hell of a lot!"
    mike.say "There - we both managed to say it."
    show sasha shy at center, traveling(1.5, 0.3, (640, 1040))
    "Sasha wraps her arm in mine and we start walking again."
    show sasha shout
    sasha.say "It feels good to have said all of that, [hero.name]."
    sasha.say "But we REALLY need to work on our communication!"
    show sasha normal
    mike.say "Uh-huh."
    show sasha shout
    sasha.say "Are you actually serious?!?"
    sasha.say "Please tell me that was a joke!"
    show sasha happy at startle
    "And sharing a laugh, we stroll off into the night."
    if sasha.love.max < 160:
        $ sasha.love.max = 160
    return

label sasha_b_event_06:
    show bg street
    show sasha at center, zoomAt(1.5, (640, 1040))
    "From the very moment that the date is over and we're on our way back home, Sasha clings to me as close as she possibly can."
    "She wraps her arms around my waist as we walk, leaning her head against my shoulder."
    "And I encircle her with my own arm, enjoying the sensation of her body against mine."
    "But I'm far more thrilled by the simple fact that she feels the need to be so close to me."
    "At first, Sasha and I spending time together felt more like we were just friends hanging out."
    "It was only over time that I began to realize that it was starting to grow."
    "That it was starting to become something far more than mere friendship between us."
    show sasha shout
    sasha.say "You know something, [hero.name]."
    show sasha normal
    mike.say "Huh..."
    mike.say "What's that, Sasha?"
    show sasha shout
    sasha.say "Back when I first moved into the house - I really wasn't that sure about you."
    show sasha normal
    "The comment seems to come completely out of nowhere, making me frown a little."
    "I look down at her with a furrowed brow, wondering just where this is going."
    mike.say "Erm...okay, Sasha."
    mike.say "What's that supposed to mean?"
    show sasha shout
    sasha.say "I'm just trying to be honest, [hero.name], you know?"
    sasha.say "I feel like we're serious enough for that by now."
    show sasha normal
    mike.say "I guess so."
    show sasha shout
    sasha.say "Don't get me wrong though."
    sasha.say "I didn't mean I thought you were weird or creepy - nothing like that."
    sasha.say "I just wasn't sure who I was moving in with, that's all."
    show sasha whining
    sasha.say "I've ended up living with some real assholes in the past, trust me!"
    show sasha normal
    mike.say "But I'm not one of them, right?"
    show sasha shout
    sasha.say "No...no, no, no!"
    show sasha happy at startle
    "Sasha lets out a nervous laugh, aware that she's digging herself deeper and deeper by the second."
    show sasha embarrassed
    sasha.say "Urgh..."
    sasha.say "This isn't coming out right!"
    mike.say "You don't say..."
    show sasha shout
    sasha.say "What I mean is that I found out pretty quickly you were a nice person."
    sasha.say "And then I found out we had a lot in common, and I liked hanging out with you."
    sasha.say "But not with other people - just with you, alone..."
    show sasha embarrassed
    "I nod at this, beginning to feel like I know where Sasha's going with this."
    mike.say "I feel the same way too, Sasha."
    mike.say "There's nobody else I'd rather spend my time with than you."
    show sasha shout
    sasha.say "Yeah, but we're only just saying this stuff now, aren't we?"
    sasha.say "We went from housemates, to friends and then to dating almost without realizing it."
    sasha.say "I just don't want the same thing to happen in reverse, yeah?"
    show sasha sadsmile
    mike.say "You mean that you want to formalize things between us, Sasha?"
    "Sasha shakes her head a little."
    show sasha shy
    sasha.say "I'm not asking you to get down on one knee, [hero.name]!"
    sasha.say "Just for us both to admit that we're in a relationship."
    sasha.say "I kinda need that from you, okay?"
    show sasha embarrassed
    "I've never really seen Sasha like this."
    "So tongue-tied and struggling to say what she means."
    "I can't help chuckling at the way she's worked herself up over this."
    mike.say "Sure thing, Sasha - if that's what you need to hear."
    mike.say "We're in a relationship, you and me."
    mike.say "It's serious, and I want it to last for a very long time."
    show sasha shout
    sasha.say "And you mean that, yeah?"
    sasha.say "You're not just saying what I want to hear?"
    show sasha shy
    mike.say "No, Sasha - I mean it, really I do."
    mike.say "I want to be honest too."
    mike.say "And for the record, I was sure I liked you right from the start."
    mike.say "That and the fact that you were seriously hot..."
    show sasha blush
    sasha.say "Why, you old-fashioned romantic, you!"
    show sasha embarrassed
    "But for all the mock outrage in Sasha's voice, she still pulls me closer as we walk."
    $ sasha.set_girlfriend()
    if sasha.love.max < 180:
        $ sasha.love.max = 180
    return

label sasha_b_event_07:
    show sasha annoyed at center, zoomAt(1.5, (640, 1040))
    "Sasha and I are celebrating something with a pizza we ordered from one of our favourite local takeaways."
    "Or at least I think we're celebrating something, as we tend to only order spontaneous pizza when we do."
    "The only thing is that I can't think of anything that we need to celebrate right now."
    "And so far, Sasha's been tight-lipped about anything that she's thought of as well!"
    "I know that there's nothing much that can get between Sasha and food when she's hungry."
    "But things only seem to get that much more weird when the pizza arrives on the doorstep."
    "And that's because I'm fully expecting her to open the box and tear straight into it."
    "Seriously - she's usually got a slice in her hand before the door's closed on the delivery guy!"
    "Yet tonight she waits until we're sitting down and even until I'm eating before she starts."
    mike.say "What's wrong, Sasha?"
    mike.say "Is your ethnic hot one a little too hot for you?"
    "We ended up calling the pizza she likes to order that as a private joke."
    "Because we both think we vaguely know the flavour of the thing."
    "But neither of us can pin down exactly what type of cuisine it belongs to."
    show sasha surprised at startle
    sasha.say "What?"
    sasha.say "Oh...no, no."
    show sasha whining
    sasha.say "My head's just somewhere else tonight, that's all."
    show sasha embarrassed
    mike.say "Oh, I see..."
    mike.say "You want to talk about it?"
    show sasha sadsmile
    "Sasha looks at me for what feels like a long time."
    "It feels like she's weighing something up, making a decision."
    "And I begin to wonder if I've done the right thing here."
    "I mean, what if I just kicked a proverbial hornet's nest without realising it?"
    show sasha shout
    sasha.say "You know what, I think we should talk about it."
    sasha.say "After all, it is us that's on my mind."
    show sasha normal
    "Oh shit - here we go!"
    mike.say "Ah, Sasha..."
    mike.say "Didn't we already have that conversation?"
    mike.say "You know, the awkward one where we both admitted we liked each other?"
    show sasha shout
    sasha.say "I know, I know..."
    sasha.say "It's just..."
    show sasha whining
    sasha.say "Well, there's another conversation you have after that one."
    show sasha embarrassed
    mike.say "There is?"
    show sasha blush
    sasha.say "Yeah, [hero.name], there is..."
    sasha.say "It's the conversation where one of you tells the other that you love them!"
    show sasha shy
    "My eyes go wide at the mere mention of the word."
    "Sure, I'm crazy about Sasha."
    "But I never actually sat down and figured out if it was love!"
    mike.say "Oh...was..."
    mike.say "Was I supposed to have said that already?"
    show sasha happy at startle
    "At this, Sasha bursts out laughing."
    "But I can see that doing so seems to have released a lot of the tension she was holding in."
    show sasha joke
    sasha.say "No, you dumbass!"
    sasha.say "I was trying to say that to you!"
    show sasha normal
    mike.say "Y...you what?!?"
    show sasha blush
    sasha.say "I think I love you, moron!"
    show sasha shy
    mike.say "I do too!"
    mike.say "Love you, that is..."
    mike.say "I love you too, Sasha!"
    if Harem.find(sasha, name='home') and Harem.find(sasha, name='band'):
        mike.say "But what about the others?"
        mike.say "Do any of them feel the same way?"
        show sasha shout
        sasha.say "Do you mean our housemates or our bandmates?"
        show sasha normal
        mike.say "I mean both of them!"
        show sasha sadsmile
        "Sasha seems to sense the worry in my voice."
        "Her head sags a little lower, letting me know she feels the same."
        show sasha whining
        sasha.say "Oh hell..."
        sasha.say "This could turn into a REAL nasty mess, couldn't it?"
        sasha.say "I honestly never thought about all of that."
        show sasha annoyed
        mike.say "It's okay, Sasha - sounds like you had some strong feelings to handle."
        mike.say "I think we all knew the potential dangers when we got into it."
        mike.say "I mean, so many people, all with their own issues and emotions!"
        show sasha whining
        sasha.say "Yeah, I guess so."
        sasha.say "But it's gonna get real awkward around the house."
        sasha.say "Not to mention the practice room too!"
        show sasha annoyed
        mike.say "We'll have to keep it to ourselves for a while."
        mike.say "Just until we can figure out what to so next."
        mike.say "We can't lie to our housemates or the guys in the band."
        show sasha shout
        sasha.say "I know, it'd be going against the whole spirit of both relationship."
        show sasha sadsmile
        mike.say "We're agreed then?"
        show sasha normal
        "Sasha gives me a smile and nods."
    elif Harem.find(sasha, name='home'):
        mike.say "But what about the others?"
        mike.say "Do any of them feel the same way?"
        show sasha annoyed
        "Sasha lets out a sigh at this."
        "She shakes her head and shrugs."
        show sasha whining
        sasha.say "I have no idea."
        show sasha shout
        sasha.say "It's been hard enough for me to figure out my own feelings."
        sasha.say "Let alone trying to see how they all felt about it too."
        show sasha normal
        mike.say "It'd be so much easier if we didn't all live under the same roof!"
        mike.say "At least then we'd have some space to work it all out."
        show sasha shout
        sasha.say "Yeah, I know."
        sasha.say "But we don't - so what DO we do?"
        show sasha normal
        mike.say "I say we keep it to ourselves for a while."
        mike.say "And then we pick our moment to tell them."
        mike.say "We can't lie to them about something like that."
        show sasha shout
        sasha.say "I know, it'd be going against the whole spirit of the relationship."
        show sasha normal
        mike.say "We're agreed then?"
        "Sasha gives me a smile and nods."
    elif Harem.find(sasha, name='band'):
        mike.say "But what about the other guys in the band?"
        mike.say "What do they feel about it?"
        show sasha annoyed
        "Sasha shakes her head, shrugging at the same time."
        show sasha shout
        sasha.say "I dunno."
        sasha.say "Honestly, I don't!"
        sasha.say "All I've thought about is myself, I guess."
        sasha.say "It's selfish, but I needed to do it."
        show sasha normal
        mike.say "We won't be able to hide it form them for too long."
        mike.say "Even if we were still just bandmates, it'd be pretty obvious!"
        show sasha shout
        sasha.say "Shit - I've made a mess of this."
        sasha.say "What do we do?"
        show sasha normal
        mike.say "Don't say that, Sasha."
        mike.say "You can't help the way that you feel."
        mike.say "We'll just have to pick the right time to tell them, that's all."
        show sasha shout
        sasha.say "Okay, let's just hope the band's strong enough to take it!"
        show sasha normal
        mike.say "We're agreed then?"
        "Sasha gives me a smile and nods."
    else:
        show sasha shout
        sasha.say "Damn..."
        sasha.say "I wish I could have just come out and said it like that!"
        sasha.say "But it's pretty solid proof you mean it, [hero.name]."
        show sasha normal
    mike.say "Should we..."
    mike.say "I don't know..."
    mike.say "Kiss or something?"
    show sasha happy
    sasha.say "Oh, how terribly romantic of you!"
    hide sasha
    show sasha kiss
    with fade
    $ sasha.flags.kiss += 1
    "I don't give Sasha enough time to follow up with another sarcastic comment."
    "Instead I pull her close to me and kiss her with a passion."
    "She's taken completely by surprise, dropping her slice of pizza as a result."
    "But then I feel her melt into the kiss, returning it with equal enthusiasm."
    "Sure, there's going to be changes that come from this admission."
    "This is an important milestone in our relationship."
    "Some would say that it changes everything."
    "But right now, all I want to do is hold her and never let go..."
    if sasha.love.max < 200:
        $ sasha.love.max = 200
    return

label sasha_event_01:
    scene bg bedroom1
    "I hear a sound outside, and look out my window."
    scene bg pool
    show sasha swimsuit
    with fade
    "I see Sasha, lounging by the pool."
    show sasha shout
    sasha.say "[hero.name]! Come on down!"
    scene bg bedroom1
    hide sasha
    with fade
    "I have got nothing to do, so..."
    scene bg pool
    show sasha swimsuit normal
    with fade
    call sasha_greet from _call_sasha_greet_1
    "I stop and I can't help but stare at Sasha lounging there in nothing but her tiny bikini, her naked skin gleaming in the sun..."
    show sasha swimsuit happy
    sasha.say "Come on over here and sit with me!"
    show sasha normal
    menu:
        "No, thank you.":
            mike.say "No, thank you."
            show sasha annoyed
            $ sasha.love -= 1
            "I stand there awkwardly, not knowing what else to do; Sasha looks disappointed."
            return
        "If that is what you want, then yes!":
            mike.say "If that is what you want, then yes!"
            $ sasha.sub -= 1
            show sasha at center, zoomAt(1.5, (640, 1040)) with fade
            "I approach Sasha, and then sit at her feet and look up at her, waiting expectantly for what she might say."
            mike.say "So, Sasha, what can I do for you?"
        "Okay.":
            mike.say "Okay."
            show sasha swimsuit happy at center, zoomAt(1.5, (640, 1040)) with fade
            $ sasha.love += 1
            "I walk over, giving Sasha a smile as I sit down beside her."
            mike.say "So, Sasha, how are you?"
        "Well, I like that!":
            mike.say "Well, I like that!"
            $ sasha.sub += 1
            show sasha blush at center, zoomAt(1.5, (640, 1040)) with fade
            "I give her a smile, then walk over and sit by her shoulder on the chair, looking down at her friendly face. Struck by an impulse, I reach down and toy with her hair a bit."
    mike.say "So, Sasha... what is it you wanted to talk to me about?"
    show sasha swimsuit normal
    "She looks up at me with a wide smile, her eyes alight and eager."
    show sasha shout
    sasha.say "Well, [hero.name], how are you doing?"
    show sasha normal
    mike.say "Oh, I'm fine. How are you?"
    show sasha sad
    "She shrugs, looking a little lost, as if she is looking for something, something to make a difference, to change things."
    mike.say "Hey, is there something wrong?"
    show sasha whining
    sasha.say "No, no. Nothing's wrong."
    show sasha sadsmile
    "Somehow, the way she said that, I thought there must have been a 'but' just waiting to be said."
    mike.say "Well, then, is there something that could be better?"
    show sasha annoyed
    "She hesitates, as if startled, then put off, then she starts really thinking about the question, her face scrunched up in a cute way, her brows furrowed, clearly she is taking the question very seriously."
    show sasha whining
    sasha.say "Well... I- that is, sometimes I get the feeling that there should be more, more going on, I mean, something happening to change things, to move life forward."
    show sasha sadsmile
    mike.say "Oh come on, you're here Sasha! That makes a big change!"
    show sasha happy at startle
    "She laughs cheerfully, and I can't help but admire the curve of her jaw, and the way her breasts move with her laughter."
    mike.say "So- do you have anything going on? If you need someone to make something happen, I'd be happy to help!"
    show sasha shout
    sasha.say "No, not much at all is going on, [hero.name] - but..."
    show sasha embarrassed
    "She stops, looking a little anxious."
    show sasha shout
    sasha.say "But, if you want to - that is, in fact, I was hoping that maybe you could suggest something to do!"
    show sasha embarrassed
    "Well, I think to myself, how can I respond to that?"
    menu:
        "I'm sure you can think of something to do.":
            mike.say "I'm sure you can think of something to do."
            show sasha stuned
            $ sasha.love -= 1
            "She looks up at me, and sits still for a long moment, then smiles."
            show sasha shout
            sasha.say "Yes, I'm sure, too."
            show sasha normal
        "I can think of games we could play.":
            "I reach down and coil a finger in her hair, staring down into her eyes with a tight smile."
            mike.say "I can think of some games we could play."
            show sasha shy
            $ sasha.sub += 1
            "She looks up, meeting my eyes; she is silent for a long moment, then smiles, her eyes shining."
            show sasha blush
            sasha.say "Sure, I'd love to play some games with you."
        "I would love to do whatever you want.":
            mike.say "I would love to do whatever you want."
            $ sasha.sub -= 1
            show sasha normal
            "I look at her expectantly, waiting for whatever she wants - Sasha looks at me with a dark, thoughtful eyes. She cocks an eyebrow, and smiles."
        "Sure, I can think of things we could do together.":
            mike.say "Sure, I can think of things we could do together."
            show sasha shy
            $ sasha.love += 1
            "I reach down and take her hand, and hold it with a smile. Sasha looks down at my hand in hers, then looks to meet my smile with one of her own."
    show sasha shout
    sasha.say "Well, maybe we can do something together, go somewhere - are there any good places to go around here?"
    show sasha normal
    mike.say "Yeah, there are some good places to go, but actually..."
    "I stop, not sure how to go on, how to say this. I feel a strong desire, an undeniable urge, but I am not sure how to say it, to talk about it."
    mike.say "...but, actually, I would like to spend some time with you here, not going anywhere, just getting to know each other."
    show sasha shy
    "I watched her eyes light up eagerly, and I felt something like- like I needed to be careful, because I could make her happy, or I might make her sad, and I should be careful."
    show sasha shout
    sasha.say "Oh, that would be great!"
    show sasha normal
    mike.say "How about we go inside?"
    show sasha shout
    sasha.say "Oh, yeah, that would be great!"
    scene bg livingroom
    show sasha swimsuit shout at center, zoomAt(1.25, (640, 880))
    with fade
    sasha.say "So, [hero.name] what places are there to go around here?"
    show sasha normal
    mike.say "Well, let's see, there's- uh... a movie theater and a pub, there's a bakery if you like things fresh; a bookstore, coffeeshop and an arcade at the mall..."
    show sasha happy at startle
    sasha.say "*giggle!* So there's plenty of things to do around here; there are lots of options!"
    show sasha normal
    mike.say "Yeah, that's right."
    show sasha shout
    sasha.say "Well, would you take me out and show me some of them? Maybe we could go out and do something together?"
    show sasha normal
    menu:
        "Nah, that doesn't sound like a good idea.":
            mike.say "Nah, that doesn't sound like a good idea."
            show sasha sad
            $ sasha.love -= 1
            "The moment I said the words, I could see the affect of them. Her smile falters a little, her shoulders slump."
            show sasha whining
            sasha.say "Well, all right, if you don't think that would be a good idea..."
            return
        "I want you to come and do it with me.":
            mike.say "I want you to come and do it with me."
            $ sasha.sub += 1
            show sasha shy
            "She giggled, and almost dropped into a curtsy, looking up at me playfully."
            show sasha blush
            sasha.say "Alright, if that's what you want!"
        "Whatever you want to do is just fine with me.":
            mike.say "Whatever you want to do is just fine with me."
            $ sasha.sub -= 1
            "I lower my head, glancing up at her form under my brows, waiting for the answer she would give; Sasha seems to almost puff up, looking at me with a superior smile."
            show sasha shout
            sasha.say "Very good, I'm glad to hear that!"
        "Yeah, I'd love to do something together with you.":
            mike.say "Yeah, I'd love to do something together with you."
            show sasha happy
            $ sasha.love += 1
            "I look at Sasha and smile as I say it; she meets my gaze with a smile of her own."
            sasha.say "Yeah, I think it would be great to do things together!"
    hide sasha
    return

label sasha_event_03:
    scene bg street
    show sasha at center, zoomAt(1.25, (640, 880))
    "We walked home together, looking around at things as we went, not looking at anything in particular, just looking."
    "We talked as we walked, again, not about anything in particular. Just talking."
    scene bg house
    show sasha at center, zoomAt(1.25, (640, 880))
    with fade
    "When we reach the house, Sasha stops and turns and leans her back against the wall, looking up at me with a smile."
    show sasha shout
    sasha.say "I had a lovely time tonight."
    show sasha normal
    if sasha.sub <= -10:
        mike.say "Good, I'm happy I was able to entertain you."
        $ sasha.sub -= 1
        "I stand quiet, waiting for her response; Sasha stares at me for a long moment, then smiles. She reaches up and caresses my cheek affectionately."
        show sasha shout at center, zoomAt(1.5, (640, 1040))
        sasha.say "Good boy."
        show sasha normal
        "She smiles at me with a strange fiery glint in her eyes that makes my stomach tremble, but a heat rises in my cheeks, and I find myself smiling back."
        hide sasha
        show sasha
        "She pats my cheek again, then turns and strides in pausing in the doorway to glance expectantly over her shoulder at me, then turns and goes in."
        "My heart hammering, my mouth dry, I hurry after her."
    elif sasha.sub >= 10:
        mike.say "Good. I will take you out again."
        $ sasha.sub += 1
        "As I say it, I look down at Sasha, and she stares up at me, her eyes wide at my pronouncement. I raise my hand and clench her jaw in a gentle grip."
        "She smiles, closing her eyes as I caress her delicate jaw. Sasha moans softly, almost nuzzling my hand."
        hide sasha
        show sasha kiss
        with fade
        $ sasha.flags.kiss += 1
        "I raise her chin as I lean down to press my lips to hers in a long soft, gentle kiss."
        "Sasha surrenders to me, kissing me back, moaning softly into my lips as I taste her, as I take her."
        hide sasha
        show sasha at center, zoomAt(1.5, (640, 1040))
        with fade
        "I break it off, and look her closely as she slowly opens her eyes to look up into mine."
        mike.say "Come on inside."
        "I take her by the hand and lead her inside with me."
    elif sasha.love >= 50:
        mike.say "I'm glad you did."
        $ sasha.love += 1
        "I smile as I say it, and she smiles back at me, the moonlight shining on her cheek."
        show sasha at center, zoomAt(1.5, (640, 1040))
        "She reaches up and cups my cheek with her hand, going up on her toes to reach up and kiss me on the cheek."
        "She looks me in the eye, her smile turning slightly sultry."
        "I walk up to join her, and take her hand in mine. She looks up at me, and I look down at her, then we walk in together."
    else:
        mike.say "Good."
        $ sasha.love -= 1
        "I nod absently as I say it, and Sasha looks at me quietly for a moment, then nods herself, then she turns and walks in, and I walk in behind her."
    hide sasha
    $ DONE["sasha_event_03"] = game.days_played
    return

label sasha_event_04:
    scene bg livingroom
    show sasha at center, zoomAt(1.25, (640, 880))
    with fade
    "Sasha is sitting on the couch."
    show sasha shout
    sasha.say "So, [hero.name], do you have any family around here? Anyone you could call on if you needed help."
    menu:
        "Nope. Just you!":
            mike.say "Nope. Just you!"
            $ sasha.love += 1
            "I grin as I say it, trying to make a joke out of it, but also perhaps thinking that she might take it well."
            "Sasha grins back at me, then leans over the arm of her chair toward me."
            show sasha shout
            sasha.say "Well, if you're ever in need, just call on me!"
        "I give help, I don't need help.":
            mike.say "I'm more of the giving help and taking care type; I've never needed help."
            $ sasha.sub += 1
            "I say it with a tight, controlled smile, watching Sasha carefully to gauge her reaction."
            "Sasha smiles and looks down, then raises her eyes to glance up at me."
            show sasha shout
            sasha.say "Well, if I ever need help then, I know who to ask for it."
        "I do":
            mike.say "Yes, which is good for me, because I sometimes really need help."
            $ sasha.sub -= 1
            "Sasha leans back in her chair, looking at me with a long, quiet, thoughtful look and gives me a tight smile."
            show sasha shout
            sasha.say "Well, if you ever need help, I'll be there to give it to you."
        "No, but I don't need anyone.":
            mike.say "No, but that's okay, because I don't need anyone to be there for me."
            $ sasha.love -= 1
            "Sasha nods, her expression blank."
            show sasha whining
            sasha.say "Okay, fine. Good for you."
    hide sasha with fade
    return

label sasha_event_05:
    scene bg kitchen
    show sasha at center, zoomAt(1.25, (640, 880))
    with fade
    mike.say "Do you want something to drink? Some coffee or tea or something?"
    show sasha shout
    sasha.say "Sure, I'd love some juice."
    show sasha normal
    "I pour Sasha some juice."
    show sasha shout
    sasha.say "So how come you've never made a move on me before?"
    show sasha normal
    menu:
        "I never wanted to before, but now...":
            mike.say "I never wanted to before, but now..."
            $ sasha.love += 1
            "I cock my head to the side and say it with a smile, and Sasha returns it with a smile of her own."
            "She raises her glass to her lips and takes a drink, her sultry eyes glancing at me over the rim."
        "It didn't seem important to me.":
            mike.say "It didn't seem important to me."
            $ sasha.love -= 1
            show sasha annoyed
            sasha.say "Mhmm."
            "Sasha nods, then takes a drink from her juice, throwing her head back, then turning away as she lowers her glass."
        "I was waiting for a time of my choosing.":
            mike.say "I was waiting for a time of my choosing."
            $ sasha.sub += 1
            "I say it with a tight smile, staring intently into her eyes as I say the words, low and clear."
            show sasha shy
            "Sasha smiles, a little anxiously, a flush rising in her cheeks, and she raises the glass and takes a drink to cover herself, but she can't quite tear her eyes away from mine."
        "I didn't want to offend you":
            mike.say "I didn't want to offend you; I thought if you wanted it, you would make the first move."
            $ sasha.sub -= 1
            "Sasha smiles as I say it, her piercing eyes staring intensely into mine."
            "Her lips curved in an arch smile, she raises the glass to her lips and takes a modest sip, never taking her eyes from mine."
            show sasha shout
            sasha.say "Smart boy."
    hide sasha with fade
    return

label sasha_band_event_01:
    $ game.flags.band = 2
    $ Room.find("studio").unhide()
    $ Room.find("map").play_music()
    scene bg street
    show sasha casual annoyed
    "Sasha is waiting for me in front of the studio."
    show sasha whining
    sasha.say "Hurry up."
    sasha.say "We're already late.."
    sasha.say "This practice is ridiculously important."
    sasha.say "Battle of the Bands is pretty soon, and we only have a few rehearsals left before we have to perform."
    show sasha shout
    sasha.say "This could be our big break."
    show sasha normal
    "I sigh, but follow her dutifully, not wanting to argue when she's in this kind of mood."
    "Besides I don't want her to kick me out when I haven't even heard her play yet."
    "Her boasts about her musical prowess without any proof to back them up have gotten rather annoying, and I want to see, and hear this band for myself."
    scene bg studio
    show sasha at top_mostright with easeinright
    "We enter the small studio, and I follow her as she weaves through the tight hallways to the back."
    "She enters through the last door on the left, and beckons me to follow."
    show anna normal at center
    show kleio annoyed at left
    "Inside stand two girls, one more edgy than the other, hesitantly tuning their instruments."
    "The first is blonde, arms covered in tattoos, her frame almost boyish that if not for her massive breasts, I would've thought she was a boy."
    "The second is smaller, almost girlish, her hair short and pink and her body wonderfully curvy despite her small frame."
    "Their heads snap up when they hear Sasha, but their eyes quickly fall on me instead."
    "The smaller girl, with the pink hair, speaks up first."
    show anna normal
    show kleio annoyed at left, dark
    show sasha at top_mostright, dark
    anna.say "Who's the boy? Did you bring him?"
    show anna happy
    anna.say "Is he that roommate you talked about?"
    show anna normal at center, dark
    hide sasha
    show sasha at top_mostright
    show sasha casual annoyed at right with move
    "Sasha, scanning the room, cuts off her questions."
    show sasha whining
    sasha.say "Doesn't matter Anna. Where the hell is Amy?"
    show sasha upset
    "Despite Sasha's clear distraction, I take notice of what Anna said."
    "Was she talking about me?"
    show sasha casual annoyed at right, dark
    hide kleio
    show kleio annoyed at left
    "The other girl, the one with the short, blonde, almost boyish hair, shrugs, distracting me from my revelation."
    kleio.say "No idea. We've been calling and texting her, and she hasn't responded at all."
    "Anna pipes in, sounding too positive for such a shitty situation."
    hide anna
    show anna normal at center
    show kleio annoyed at left, dark
    anna.say "We think she bailed."
    show anna at center, dark
    hide sasha
    show sasha casual stuned at right
    "Sasha's body stiffens and her fists clench as she turns on the girl."
    show sasha shocked
    sasha.say "Anna, what do you mean, 'you think she bailed.'"
    show sasha angry
    sasha.say "She's our lead guitarist--she can't fucking bail!"
    show sasha casual upset at right, dark
    hide kleio
    show kleio annoyed at left
    "The first girl rolled her eyes at Sasha's anger, clearly not phased."
    kleio.say "Chill out, Sasha. We'll find someone else. It may just take a while."
    show kleio annoyed at left, dark
    hide anna
    show anna normal at center
    "Anna pipes up again, not phased by Sasha's scathing tongue."
    anna.say "We think she was never really going to join in the first place."
    anna.say "Kleio said she probably just wanted to pick up chicks."
    "After a moment, she shrugs."
    anna.say "At least, it makes more sense as to why she's not calling us after she slept with me."
    "It's clear to me, and the other girls, and anyone who might take a passing glance at Sasha, that she's seething mad and doesn't want to take this for an answer, nor does she even want to comment on Anna's love life."
    show anna at center, dark
    hide sasha
    show sasha casual vangry at right
    sasha.say "We'll never find someone, especially not in time for Battle of the Bands. It's hopeless."
    show sasha upset
    "She slumps back in the chair, crossing her arms, staring angrily at the wall."
    hide anna
    show anna normal at center
    hide kleio
    show kleio annoyed at left
    menu:
        "I can play guitar":
            mike.say "Um, well, you know, Sasha, I can play guitar?"
            show sasha casual annoyed
            show anna normal at center, dark
            show kleio annoyed at left, dark
            "Sasha rolls her eyes, dismissing me entirely."
            show sasha whining
            sasha.say "I'm sure you can, [hero.name]."
            sasha.say "You and every other boy on this planet."
            sasha.say "You'll be no help, we're doomed."
            show sasha casual annoyed at right, dark
            hide anna
            show anna normal at center
            "Anna glares at Sasha."
            anna.say "No need to be so cruel, Sasha."
            anna.say "He clearly wants to help."
            anna.say "Why not let him? What have we got to lose?"
            show anna normal at center, dark
            hide sasha
            show sasha casual annoyed zorder 2 at right
            "Sasha sighs, clearly annoyed, but she concedes, knowing she was out a guitar player, and—as far as I was aware—out of options."
            show sasha whining
            sasha.say "Whatever.."
            hide anna
            hide kleio
            show anna happy zorder 3 at center
            show sasha annoyed at top_mostright, dark
            show kleio annoyed zorder 1 at right, dark
            with ease
            "Kleio and Sasha step aside to sulk, scrolling through their phones, clearly looking for a replacement guitarist, but Anna smiles at me, gesturing to the guitar before stepping aside to turn on my mic."
            "I take a hesitant breath, before I carefully pick up the guitar."
            mike.say "Step aside, ladies. Hand me that guitar, let me show you what I can do."
            show anna happy at center, dark
            hide sasha
            show sasha casual happy zorder 2 at top_mostright
            "Sasha's head snaps up, and, before I know it, she's laughing at me, her whole body consumed in convulsions before I can even say anything more."
            show sasha shout
            sasha.say "[hero.name], I highly doubt you can do anything that would be good enough for us, but if you want to embarrass yourself, be my fucking guest."
            hide sasha
            hide kleio
            hide anna
            with dissolve
            "Annoyed by her words, I confidently stride forward, grabbing the neck of the guitar and yanking it into my arms."
        "Say nothing":
            "I stay silent, trying to fade into the background, but it's hopeless."
            show anna normal
            anna.say "Hey, [hero.name], can you play guitar?"
            show sasha casual whining
            sasha.say "Are you kidding me, Anna? You want to try [hero.name]? We are an all female band!"
            show sasha sad
            "After a moment though, she sighs."
            show sasha whining
            sasha.say "But if you really want to try, then be my fucking guest."
            hide sasha
            hide kleio
            with dissolve
            "The first girl steps aside to join Sasha, not paying me any attention at all as Anna gathers the guitar for me."
            show anna happy
            "She smiles at me, clearly curious and excited for me, before stepping aside to adjust my mic."
            hide anna with dissolve
            "Embarrassed, I fumble with the guitar, hoping I can at least get some of this right."
    "I tune the guitar quietly, watching the first girl and Sasha more than I watch Anna."
    "It's clear she's already sold—either that, or she's just attracted to me—but it's them, especially Sasha, that I want to impress. I want to show her what I can do."
    play music "<from 7 to 188>music/deathless_harpies/Deathless_Harpies_GuitarLead.ogg" loop
    "With one more inhale, and one more strum to test the guitar, I begin to play."
    "The music is louder than I expected it to be, the studio rather conducive to the sound of music."
    "It sounds even better than I thought it would, and, by the looks on their faces, it's clear Sasha and her bandmate are thinking the same way."
    "Across the room, Anna is beaming, clearly smug as she watches me play. Her body language screams, I told you so."
    "I can't help but smile before I open my mouth to sing."
    "At that point, Anna becomes so pleased that she rushes to the booth, slamming on an old recording of theirs on top of my voice."
    play music "<from 7 to 188>music/deathless_harpies/Deathless_Harpies_DrumsBassGuitars.ogg" loop
    "I quickly adjust to their record, mixing my voice in with their sounds."
    "Kleio and Sasha both roll their eyes, pretending to not be impressed, but it's clear that it's only their pride in their way."
    "I have them sold."
    "When the recording finally comes to an end, I finish out my guitar, holding the last note until my breath gives out, turning to the girls for their approval."
    $ Room.find("map").play_music()
    "I can't hold back the cocky grin on my face as I look at them."
    mike.say "So, what do you think?"
    show anna happy at center with dissolve
    "Anna rushes out of the booth, nearly tackling me with her hug."
    anna.say "Oh my gosh, [hero.name]! You did amazing! Kleio, Sasha, he has to join us."
    anna.say "You guys would be so, so stupid not to let him in!"
    show anna happy at center, dark
    show kleio annoyed at left
    with dissolve
    "The first girl, Kleio, rolls her eyes at her friend's enthusiasm."
    kleio.say "He's good, but not great, and his attitude needs some serious adjustment."
    kleio.say "I vote no."
    kleio.say "We can find someone way better. Preferably a girl."
    kleio.say "I'm not a fan of all this testosterone, anyway."
    hide anna
    show anna happy at center
    show kleio annoyed at left, dark
    "Anna pouts, clearly protective of my words, before turning desperately to Sasha."
    anna.say "Sasha, come on!"
    anna.say "You can't deny that what you just heard was good."
    anna.say "He simply has to join us."
    anna.say "It's for the good of the band."
    anna.say "Come on!"
    show anna happy at center, dark
    show sasha casual annoyed at right
    with dissolve
    "Sasha wavers, clearly wondering if she wants her pride to win, or her band."
    "Proud of myself, but still hesitant and unsure of these girls, I find myself wavering slightly."
    "After a long, pregnant pause, Sasha finally opens her mouth."
    show sasha casual shout
    sasha.say "What if we just let him in, just for Battle of the Bands? If he proves himself worthy, he can stay after that."
    sasha.say "If not, we're booting him, no if's, and's, or but's, alright?"
    show sasha normal
    hide anna
    show anna happy at center
    "Anna seems to ignore the second bit, simply squealing and jumping over to hug Sasha."
    anna.say "Sasha, you're the best!"
    anna.say "You won't regret it, I can tell he's going to be great for us!"
    show anna normal at center
    hide kleio
    show kleio annoyed at left
    "Kleio scoffs, before crossing her arms and turning to me."
    kleio.say "Chill out, Anna."
    kleio.say "Jesus Christ."
    kleio.say "Sasha didn't even ask him if he really wanted to join."
    kleio.say "He just played guitar—that's all."
    hide anna
    show anna happy at center
    "That observation seemed to make Anna falter, and she turned to me, eyes wide."
    anna.say "Well, you will join, won't you?"
    menu:
        "Yes":
            "I barely even have to consider it."
            "A grin overtakes my face as I find myself agreeing."
            mike.say "'Course I will. Seems like you guys need me, anyway."
            "Anna grins and hugs me again, her gratitude clearly abundant."
            anna.say "Oh, thank you so much, [hero.name]! You've saved us."
            "Her enthusiasm is infectious, and I can't help but smile, looking down at this woman as she grins up at me."
            "She's rather cute too, and I'd be lying if I said I didn't notice her breasts shoved up against my arm."
            "With a smug grin on my face, I realize that joining this band was the best idea I've had in a long time."
        "No":
            "It takes me a moment to really process what she's asking."
            "Joining a band would be super cool, and I'd definitely be lying if I said that I didn't want to spend more time with these insanely hot women, but joining a band is an insane time commitment, and one that I'm not sure I want."
            "Plus, it's clear that over half the band doesn't really want me here, and I'd be crazy to think that a band full of people who dislike one another would work."
            "I find myself opening my mouth to backpedal my way out of the situation, scrutinized under Kleio's annoyed gaze, when I catch sight of Anna again."
            "Her eyes are so full of hope and desperation that I falter again, wanting nothing more than to make her happy."
            "She's really cute when she's happy, and I wouldn't mind being able to make her happy, again and again and again..."
            "My mind is so lost in thoughts about fucking Anna that it barely even registers that I've opened my mouth to agree until it's already happened."
            mike.say "Yeah."
            "My gaze is still locked on Anna."
            mike.say "Yeah, I'll join."
            "Anna grins so wide I think it might break her face, and, ignoring Kleio and Sasha's annoyed glares, she rushes over to me and tackles me into a hug."
            "Although I'm uncomfortable, it's really hard to not smile when there's a cute girl basically straddling your arm."
            "As I look down at her grinning face, I hesitantly think that maybe joining a band wasn't such a bad idea after all, if it means I get to spend more time with her."
    "Kleio shatters my moment, scoffing as she turns aside to pluck at her guitar."
    kleio.say "You're ridiculous, Anna, honestly."
    "She tosses a scathing glance my way."
    kleio.say "You'd better be good."
    "For a moment, I watch Kleio, wondering what her problem was."
    "She stays silent for a moment, before turning to me with a devious glance."
    show kleio normal
    kleio.say "[hero.name], you can join our band, but you know, before you joined, it was an all-female band."
    kleio.say "If you want to stay, you'll have to cross dress."
    menu:
        "Ok":
            $ game.flags.bandcrossdress = True
            "I shrug, grabbing up the guitar before glancing to Sasha for guidance."
            "She's hiding a slight grin, the first time this whole practice I've seen her smile."
            "Anna stifles some laughter, too."
            "Clearly, they think this idea is hilarious."
            "I decide to play along."
            mike.say "Sure."
            mike.say "Of all the embarrassing things I've done, cross dressing is probably the least of my worries."
            mike.say "Show me a dress and buy me heels and I'm yours."
            "Kleio's eyes widen, and all three girls burst into laughter. I can't help but join in with them."
            "For a moment, we simply all laugh, but by the mischievous glint in Kleio's eyes, I can tell she's more serious than I thought. Or, at the very least, she's going to have a lot of fun embarrassing me."
            "As the laughter dies down, we get serious again, and Kleio turns to Sasha, waiting for her to begin the rehearsal."
        "No way":
            "My eyes widen, and I try to hide my disbelief."
            "Cross dressing? She has got to be kidding."
            "I try not to offend her, but also desperately trying to turn her down."
            mike.say "Uhh..."
            "Luckily, Anna comes to my rescue."
            anna.say "Lay off him, Kleio. He doesn't have to cross dress. Just because we were an all-girl band before doesn't mean we can't have a boy now."
            "I could kiss Anna I'm so happy. Luckily for me, Kleio doesn't push the point anymore, just rolls her eyes and looks to Sasha for her to begin rehearsal."
    show sasha annoyed
    "Rolling her eyes, Sasha stands up, crossing the room, gathering her guitar and turning to me."
    kleio.say "Take us away, [hero.name]."
    play music "music/deathless_harpies/Deathless_Harpies.ogg" loop
    "With a small grin, I begin to play."
    hide sasha
    hide kleio
    hide anna
    with fade
    "Time moves fast for all of us, and although, by the end of it, Sasha and Kleio are still hesitant, it's obvious that they're a lot less stingy than they were when we started."
    "I even caught Kleio smiling at me once or twice when she thought I wasn't looking."
    "Overall, it was a pretty good practice."
    $ Room.find("map").play_music()
    scene bg black with timelaps
    scene bg studio with timelaps
    "Eventually, though, we all crashed, exhausted, and we all unanimously decided to take a break."
    "Sipping on a Coke the girls had set aside, I find myself making casual conversation."
    mike.say "So, Anna, tell me about yourself."
    show anna blush at center with dissolve
    "Anna blushes, clearly embarrassed to be called out directly, but not unwilling to share."
    anna.say "Well, I go to University around here, actually. I moved here from Virginia just to go."
    "My eyebrows shoot up, unable to contain my surprise. I didn't peg her as a university girl."
    mike.say "Oh really? That's awesome. What are you studying?"
    anna.say "Biology."
    "She can't contain her massive grin as she speaks."
    anna.say "I want to be a scientist, actually. I know it's a little silly—I don't exactly look like a scientist—but hey, a girl can dream, right?"
    menu:
        "Yes":
            "I nod. Although I'm a little skeptical, I try not to show it."
            mike.say "Definitely. It's good that you're pursuing your dreams."
        "No":
            mike.say "I guess, but you may be just slightly off the mark there. You seem to be better suited here."
            "Although she seems hurt, she lets it slide."
    mike.say "Anyway, what brings you here?"
    anna.say "To the band, you mean?"
    mike.say "Yeah."
    anna.say "Oh! Well, I met Sasha at the store I go to at the mall all the time, because that's where she works, you know?"
    anna.say "And one day we got to talking, and I happened to mention that I played the drums. She brought up she had a band, and, well, from there, it's history."
    "She grins, glancing over at Sasha."
    anna.say "Isn't that right, Sasha?"
    hide anna with dissolve
    mike.say "Kleio, right?"
    show kleio normal with dissolve
    "Kleio glances over at me, almost startled as though I'm talking to her and not Anna, who had been soaking up my energy all afternoon."
    kleio.say "Yeah? What about it?"
    mike.say "Nothing, I was just trying to get to know my fellow bandmates better."
    kleio.say "Ah."
    "There was a pause."
    "I try again, unwilling to let this conversation fall flat just yet."
    mike.say "That's a really cool name."
    kleio.say "Thanks. I picked it myself."
    "I blink, a little startled but trying not to show it."
    mike.say "Oh, really? Is it a nickname?"
    "She nods, and then, almost as though she senses how much I was trying, she tosses me a bone."
    kleio.say "Sasha sorta helped me pick it out when we first met, isn't that right, Sasha?"
    hide kleio with dissolve
    "I sigh, turning towards Sasha, giving up on trying to interact with someone who clearly wants nothing to do with me."
    show sasha casual normal with dissolve
    "I turn to Sasha, a little overwhelmed by these new girls, unwilling to branch out yet."
    mike.say "What made you decide to start a band?"
    "She looks a little caught off guard, but for once, decides to answer honestly, and without a hint of her usual sarcasm."
    show sasha shout
    sasha.say "Well, I've known Kleio for a while, and her and I always used to joke about starting a band."
    sasha.say "But when I met Anna in the mall that day—I don't know, it just all ended up working out."
    sasha.say "We all pooled our money, and we got this studio for a few weeks."
    sasha.say "But if we don't make it back at Battle of the Bands, then we're through."
    show sasha normal
    "I give her a hopeful grin."
    mike.say "I'm sure we'll get there, I can feel it."
    "Seemingly stunned by my sincerity and unwavering optimism, Sasha gives me a rare smile."
    show sasha happy
    sasha.say "Thanks, [hero.name]."
    hide sasha
    return

label sasha_band_event_02:
    $ game.flags.performance = 2
    $ Room.find("studio").unhide()
    show anna happy at right with moveinright
    "As I nurse my drink at the bar, smiling softly at the people as they slowly fill up the venue, I'm suddenly startled by a small, pink-haired woman, smiling broadly as she comes up to me."
    if hero.charm >= 25:
        show anna happy at center with move
        "I look down at this small, pixie-like woman, trying to contain my laughter."
        mike.say "Hey there, little fairy. Did you get lost on the way to pixie hollow?"
        show anna normal
        "The woman seems unfazed by my joke, simply shaking her head."
        anna.say "Sasha said you'd be an asshole."
        anna.say "Come on—she sent me to get you."
        anna.say "Apparently we're in need of your 'big strong arms.' Looking at you now, though, I don't really know what she was talking about."
        "Hiding a grin, I realize this small woman has just as much power to dish it out as she does to take it."
        "Sticking out my hand, I offer it to her to shake."
        mike.say "I'll come, don't worry. But, first—what's your name?"
        "She smiles up at me as I get to my feet, anxious to return me to Sasha."
        anna.say "I'm Anna. Nice to meet you."
    else:
        show anna happy at center with move
        "This woman, although small, immediately captivates my attention."
        "She's absolutely beautiful—built like a model, with curves for miles—and her breasts, despite her small frame, are huge."
        show anna normal
        "I don't even attempt to hide my staring, unable to break my gaze until she finally speaks to me."
        anna.say "Uh, hi. Are you [hero.name]?"
        "My heart flutters in my chest as I realize, somehow, that this small sexy woman already knows my name."
        mike.say "Yeah, I am. What's up?"
        show anna happy
        anna.say "Sasha sent me to come get you. And, boy, am I glad she did. I'm Anna, and it is so, so nice to meet you."
        "Realizing her eyes were raking me up and down as much as mine were hers, I almost seem to drift to my feet beside her, not asking any more questions than I need to."
    show anna normal
    "Before I get a chance to say anything more, Anna begins to lead me towards the back of the bar, to the service door."
    "With a slight wink at the security guard, she gestures me inside."
    show anna at right with move
    "The brightly lit hallway is a direct contrast to the dark mood lighting of the bar, and I find myself reaching for Anna to guide me as my eyes adjust."
    "She does so happily, her fingers sliding and playing with mine as she weaves me through the small hallways to where the band is setting up."
    "My eyes have just adjusted to the light when I finally see Sasha, a wave of relief crashing over her as soon as she sees me."
    show sasha casual2 shout at left with dissolve
    sasha.say "Oh, thank God, you found him. Thank you, Anna."
    show sasha normal
    show anna normal
    "Anna grins up at me, refusing to leave my side."
    anna.say "No, no, thank YOU, Sasha. [hero.name] is awesome."
    "She looks up at me again, fluttering her long, beautiful eyelashes, and I feel my knees get weak."
    show sasha casual2
    "Sasha notices Anna's flirting, and unceremoniously pushes her aside to the other woman in the room."
    show kleio annoyed
    "She's looks much more stoic, and appears much more annoyed with my presence."
    kleio.say "This is ridiculous, Sasha—we don't need him to do this."
    kleio.say "We are more than capable on our own, or, worst comes to worst, we can borrow some security guards."
    kleio.say "Why do we need your friend back here."
    hide kleio
    show sasha casual2
    "Sasha shakes her head, completely disregarding her bandmate's words."
    show sasha shout
    sasha.say "Ignore her, please. That's Kleio, and she's a big believer in woman's rights."
    sasha.say "I am too, but I'm also a realist, and I realize, unlike some people, that we are incapable of lifting our two huge amps out onto the stage on our own."
    sasha.say "Even if we were, we don't need to risk breaking bones right before a show."
    show sasha normal
    "Kleio rolls her eyes, scoffing at Sasha's words, but says nothing more, clearly realizing that this is an argument not worth fighting."
    show sasha shout
    sasha.say "So, [hero.name] I know it's a lot to ask, but could you help us? We'd really appreciate it."
    show sasha normal
    menu:
        "Sure":
            mike.say "Uh, I mean, yeah, of course I can try. I don't know how much help I'll be, but I can try it."
            hide sasha
            show anna happy
            "Sasha smiles, and Anna dashes across the room, breaking from Kleio's side, to tackle me into a hug."
            anna.say "Thank you so much, [hero.name]! You've saved us!"
            hide anna
            show sasha casual2 shout
            sasha.say "That might be a little extreme, Anna, but, yes, thank you so much, [hero.name]."
            sasha.say "This means a lot to us."
            show sasha normal
            "I smile at them, but I'm unable to ignore Kleio's sulking in the corner. She snorts as the two other girls fawn over me, rolling her eyes as Anna refuses to let go of my body."
            hide sasha
            show anna happy
            anna.say "Here, I'll take him to where the amps are, okay?"
            "Before anyone has a chance to agree, Anna grabs my arm, and drags me out of the room."
            "Her tiny body clings hard against mine, her breasts pressed against my arm as she took her time leading me to the room."
            "When we finally reach our destination, I can't help but notice that she looks almost disappointed."
            "She scuffs her feet against the ground as we talk, stalling our goodbye for as long as she can."
            anna.say "Well, here we are."
            mike.say "Yep. So the amps are just in here, then?"
            anna.say "Yeah, they are. The stage doors are two large loading docks, and it should take you right to the stage."
            anna.say "Just place them on the lip, and we can handle the rest."
            mike.say "Alright, got it. Thank you, Anna. I appreciate your help."
            "Anna's eyes got wide again, and I swear, I could hear her heart fluttering wildly in her chest."
            anna.say "No, no—thank you! We couldn't even be doing this show without you. Thank you so much."
            "I smile, taking in her small, voluptuous body one last time before finally turning to the door."
            "With one last wave at Anna, I make my way into the room."
            hide anna
            if hero.fitness >= 25:
                "I make quicker work of my job than I expected to; the amps were heavy, and I could see why the girls needed help, but it was nothing I couldn't handle on my own."
                "By the time I finish, it was almost time for the show to start, so I slip down from the stage, returning to the bar for one more drink to settle my aching muscles before their set begins."
            else:
                "The amps are much larger and heavier than I thought they would be, and it takes me forever to drag their large bodies out onto the stage."
                "Embarrassingly, I have to go get one of the security guards to help me move the largest one, which he does without a second thought."
                "Embarrassed, by the time I finish the excruciating task, the show is mere minutes from starting, so, in a rush, I jump down from the ledge and rush to the bar, hoping to drink away my shame and ease my weary muscles before the show begins."
        "No":
            mike.say "Uh, I mean, I would, but, like, I think Kleio is right."
            "The security guards here are probably ten times stronger than I am, and I just feel like that would be a better option. Sorry."
            "Sasha's face twists, and she takes a step back from me, and, even though I'm tipsy, I can tell I hurt her feelings."
            "Kleio, though, looks up at me, a small smile on her face as, for the first time, I think she takes me in."
            "Nodding a small approval, she looks down again before Sasha notices her noticing."
            show sasha shout
            sasha.say "Oh, well, okay then. I guess you're right. Anna, you can take [hero.name] back out to the bar, and, while you're at it, you'll get a security guard, won't you?"
            show sasha normal
            "Looking kind of sad, Anna nods, coming up again to take my arm."
            hide sasha
            show anna normal
            anna.say "Come on, [hero.name]. I'll take you back out to the bar."
            "Allowing myself one more glance at Kleio, Anna slowly leads me out of the green room and back down the hallways we came."
            "When we reach the door that leads back to the main bar, Anna lingers by my side, clearly stalling. She shifts from foot to foot, thinking of something to say."
            anna.say "Well, thanks for trying to help, anyways. We appreciate it."
            mike.say "Yeah! Yeah, anytime, Anna. Sorry I couldn't be of any more help."
            anna.say "It's okay! Don't worry about it, honestly."
            mike.say "Yeah. Well, hey, good luck tonight. You guys are gonna sound amazing."
            show anna happy
            "Anna brightens up at these words, grinning widely at me once again."
            anna.say "I sure do hope so! Speaking of, I'd better get back. Once we get those amps out, I think we're gonna start the set."
            anna.say "You'd better get a drink and grab a spot quickly—we're hoping to pack the house!"
            hide anna
            "Her enthusiasm was infectious; I find myself grinning wider and wider as she rambles."
            "Giving her a wave goodbye as she finally sets her eye on a guard that she needs, our eyes linger on each other for one more energetic moment, before she's whisked away down the hall, and I make my way over to the bar."
            "By the time I get my drink in my hand, I realize that Anna wasn't lying—the house was packed already."
            "Shuffling my way towards the front, I manage to get a pretty good seat just as the set begins."
    with fade
    "The girls come out on stage, looking electrified, Sasha leaning close to the microphone, speaking in a low, breathy voice I hadn't yet heard from her."
    "The other girls look empowered, punkish, and, despite the stereotype, ready to rock 'n' roll."
    show sasha shout
    sasha.say "Thank you all for coming out to our show tonight."
    sasha.say "We are Deathless Harpies, and we aren't sorry about it."
    show sasha normal
    play music "music/deathless_harpies/Deathless_Harpies.ogg" loop
    "Their music was loud, angry, and the antithesis of everything I usually listened to—and yet, I could not drag my attention away."
    "Despite them missing a member, they did not seem to be missing anything, their presence swelling and filling the small room to the brim."
    "The drunk bodies around me swung and swayed to the music, enthralled with the punk sound of electric guitar and the heartbeat from Anna's drums."
    "Their music was electrifying, and I never wanted it to end."
    "By the end of their set, I found myself almost completely out of breath, so drawn into their performance that when their encore finally finished I felt as though I was missing an integral part of me."
    $ Room.find("map").play_music()
    "With one more grin at her bandmates, Sasha and her friends begin what was probably one of the greatest local concerts of my life."
    "My face flushed, my eyes wild, I didn't even hold myself back from rushing back into the green room to see Sasha and the band again."
    "With one flash of my card at the guard, he allowed my stumbling body back, then I scrambled wildly through the halls until I found the door again."
    with fade
    "Busting inside, I find all three bandmates, nursing small mixed drinks, smiling and laughing, clearly high off the success of their set."
    show sasha casual2
    mike.say "Holy shit, you guys—that was amazing! Sasha, you didn't tell me you guys were that good!"
    "Sasha smiles, but it's clear that she's trying to be modest. She nods slightly to me, hiding a slight blush before responding."
    show sasha shout
    sasha.say "I'm glad you liked it, [hero.name]. We've come really far, but we still have a ways to go."
    show sasha normal
    mike.say "Liked it? I loved it! It was fucking fantastic! You need to do this for a living, all of you do—holy shit, that was amazing."
    hide sasha
    show anna blush
    "Anna looks up at me, almost vibrating with excitement, the rush of the set, and my praise."
    "As though she couldn't contain herself any longer, she rushes across the room, tackling me into a warm, tipsy hug."
    anna.say "Thank you so much, [hero.name]! You're the best! You're welcome here with us, anytime!"
    hide anna
    show kleio annoyed
    "Kleio, the quietest one by far, looks up at this statement, looking slightly annoyed by Anna's words."
    kleio.say "Seriously?"
    hide kleio
    show anna happy
    "Anna spins around to meet her bandmate, not letting go of my waist as she speaks."
    anna.say "Don't be such a downer, Kleio!"
    anna.say "Of course [hero.name] is welcome!"
    anna.say "He's Sasha's roommate, after all, and he's so damn sweet—it'd be, like, cruelty to not let him hang out with us!"
    hide anna
    show kleio annoyed
    "Kleio rolls her eyes but drops the subject, continuing to quietly nurse her drink, pleased with herself and satisfied with that praise alone."
    "I got the vibe that she was very independent, very uncaring of what others thought about her, and, despite her nasty attitude, I could see the allure very, very clearly."
    hide kleio
    show anna happy
    "Anna, though, brought me back to focus."
    "She seems ridiculously hyper, almost bouncing off the walls, and, despite its seeming childishness, I can't help but find something sexy about her."
    "We all talk for what seems like hours, with even Kleio jumping in to the conversation at times, the energy of the girls so overwhelmingly infectious."
    "We all drink and laugh, except for Sasha, who just laughs, enjoying each other's presence and the overwhelming high from the performance."
    "As time goes on, though, the exhaustion from the night begins to creep in—slowly, carefully—and we find ourselves holding back yawns more and more as the night continues."
    "Finally, Sasha says what we've all been thinking—that it's time to go home and get some rest."
    "Anna is resting in my lap at this point, holding onto my neck tightly, nuzzling her face into my chest."
    anna.say "Oh, come on Sasha, just five more minutes. We're having so much fun..."
    "Despite her words, I can feel Anna dozing off beside me, and I hide a smile, knowing she just doesn't want the night to end."
    "Sighing, Kleio gets to her feet, gently taking Anna from me into her arms, righting her on the floor, allowing her small body to rest against her own, slowly guiding her towards the door."
    hide anna
    show kleio normal
    kleio.say "Come on, girls."
    kleio.say "Let's get some well-deserved rest."
    kleio.say "We did well today—let's try and reward ourselves."
    "Smiling, I gently lean on Sasha, allowing her to guide me to the door and out to our cars."
    "With one last wave at the girls, and a tight hug from Anna, we leave the bar, the car ride an exhausted, drunken blur."
    hide kleio
    "By the time we get home, I barely realize that any time has passed at all, with Sasha gently helping me into my room and taking off my nice clothes before leaving me to sleep."
    "I lay down on my bed and pass out almost immediately, my head filled with images of beautiful, punk girls and the endless, beautiful sounds of their hard rock 'n' roll band."
    return

label sasha_practice_01:
    "With the battle of the bands getting closer every day, we were practicing in every moment of free time that we had."
    "I thought we were sounding better than ever, but Sasha and Kleio seemed to be getting more frustrated with the smallest of details."
    "Anna and I tried to keep out of their frequent outbursts of emotion, but occasionally they were too much to ignore."
    show sasha angry
    sasha.say "FUCK...FUCK...FUCK!"
    show sasha upset
    show kleio angry at left
    kleio.say "Jeez, hold it together, Sasha!"
    show anna at right
    anna.say "Wow...Sasha, are you okay?"
    show sasha whining
    sasha.say "I just can't get this chord out of my head and onto the damn bass."
    sasha.say "I feel like I've got flaccid dicks for fingers!"
    show sasha upset
    "I offer Sasha an understanding smile while trying to keep such a weird mental image out of my mind."
    show sasha sadsmile
    "She sees the gesture and smiles back, seeming to get more reassurance from my silent show of support than the words of the other girls."
    show sasha shout
    sasha.say "Let's have a break...I'm just gonna have some me time in the bathroom."
    show sasha sad
    "The other girls nod as we all set down our instruments, but as she passes me, Sasha beckons me with a finger."
    hide sasha
    "It's clear that she wants me to follow her into the bathroom for some reason."
    "But I'm not sure if I should follow on her heels, or give it a few seconds to keep from drawing Kleio and Anna's attention."
    hide kleio
    hide anna
    menu:
        "Follow Sasha immediately":
            show bg restroom
            show sasha normal
            with fade
            "I arrive in the small bathroom almost literally right behind Sasha."
            show sasha happy
            "She turns and smiles broadly at the sight of me, clearly delighted that I read her so well."
            mike.say "Hey, Sasha - are you okay?"
            show sasha shout
            sasha.say "Yeah, just tense as hell...like we all are."
            show sasha flirt
            sasha.say "I need to let off some steam - and let's just say I didn't mention dicks back there by accident, either!"
            $ sasha.love += 5
        "Follow Sasha after a minute":
            "I give it about a minute, then follow Sasha into the bathroom."
            show bg restroom
            show sasha normal
            with fade
            "She looks over her shoulder at me, her mood improving at seeing me turn up."
            mike.say "Just wanted to see if you were doing okay?"
            show sasha whining
            sasha.say "Better than I was...I thought you weren't going to come see me for a moment."
            show sasha sadsmile
            mike.say "Sorry...I just thought you'd appreciate a few seconds alone, after being cooped up with all of us for so long."
            show sasha flirt
            sasha.say "Trust me, it's different when it's just the two of us."
        "Follow Sasha after five minutes":
            $ sasha.love -= 5
            "I wait a full five minutes, checking the time before I follow Sasha into the bathroom."
            show bg restroom
            show sasha upset
            with fade
            "She's sitting cross-legged on the toilet, arms folded over her chest and looking pretty annoyed."
            mike.say "Are you feeling any calmer, Sasha?"
            show sasha vangry
            sasha.say "Nope, but at least now I'm pissed for sitting here on my own in a damn bathroom for ages, so that's a change at least!"
            show sasha annoyed
            mike.say "Wait a minute...you wanted me to come quicker?"
            mike.say "Geez, sorry...guess I misread the situation."
            show sasha whining
            sasha.say "Yeah - same here!"
    show sasha normal
    "She stretches and lets out a long breath, which means getting even closer to me in the small space of the bathroom."
    show sasha shout
    sasha.say "Help me out here - teach me some way to squeeze a little of the stress out of me?"
    if sasha.is_collared:
        "Sasha's so close now that I can see the tension in her muscles, the tightness of the dog-collar that she wears around her neck, and her breathing is all I can hear."
    else:
        "Sasha's so close now that I can see the tension in her muscles, and her breathing is all I can hear."
    menu:
        "Tighten the dog collar round Sasha's neck" if sasha.is_collared:
            "Without speaking, I turn Sasha around and take hold of the leather collar she's wearing."
            show sasha happy
            "She gasps in surprise, but thanks to her delight in such things, doesn't object in the slightest."
            "I tighten it slowly and gently, allowing her to feel the gradual progression of its grip on her neck."
            "Sasha gasps, instinctively pressing herself against me, so that her ass is nestled in my lap."
            $ sasha.sub += 5
            "I don't keep it up for too long, just enough time for her to lose herself, and then I loosen my grip once more."
        "Massage Sasha's tense muscles":
            mike.say "You're wound up tighter than the strings on your own Bass!"
            "I begin to knead and massage the muscles of Sasha's shoulders, not being at all gentle with the knots and kinks that I find."
            show sasha normal
            "She makes no effort to protest, and pretty soon her expression begins mellow as she lets herself feel the benefit."
            show sasha shout
            sasha.say "Don't we have magic hands...now do the back as well."
            show sasha shy
            "She turns to allow me to massage her back, but surprises me by stripping off her t-shirt as she does so."
            "Before I can begin, her hands capture mine and guide them to her petite breasts."
            show sasha embarrassed
            $ sasha.sub -= 5
            "Too turned on to argue, I massage them instead, enjoying the sensation of her nipples as they stiffen under my touch."
        "Teach Sasha a breathing exercise":
            mike.say "I got sent on a stress-relief course by work last year, they taught me a breathing exercise that always works."
            "I talk Sasha through the exercise, trying to ignore the fact that she's almost looking daggers at me the whole time."
            "I guess she was hoping for something a little more tactile and impactful, but she grits her teeth and copies my actions."
            show sasha normal
            "After a couple of minutes pass, she's actually visibly calmer than before."
            $ sasha.love += 5
            show sasha shout
            sasha.say "I guess you were right...that has helped calm me down."
    show sasha shout
    sasha.say "Thanks for that...it seems to have done the trick."
    show sasha normal
    mike.say "Happy to be of help."
    show bg studio
    show kleio at left
    show anna at right
    with fade
    "We walk back into the practice room, neither of us wanting to admit to what just happened in the bathroom, but its implications already running through our minds."
    "Kleio and Anna try to look nonchalant and disinterested, but they both clearly want to know why we just spent so long in there together."
    show sasha shout
    sasha.say "What are we waiting for, the start of the next fucking ice age?"
    sasha.say "Let's get back to it, people!"
    hide sasha
    return

label sasha_practice_02:
    scene bg studio at center, zoomAt(1.2, (640, 880)), dark, blur(5)
    show mike crossdress upset
    with fade
    "I am a strong, confident and thoroughly modern man."
    "I am secure in my sexuality, and I have no fear of ridicule."
    "Or at least that's the mantra that I keep repeating inside of my head."
    show mike crossdress down
    "In reality I can't help tugging at the hem of the dress that I'm wearing."
    "And the sound of constant giggling is the scariest thing I can imagine."
    sasha.say "Come on out, [hero.name]."
    anna.say "Yeah, hurry up already."
    anna.say "We wanna see how you look!"
    kleio.say "You need help with your panties, Loverboy?"
    kleio.say "They cutting into your mangina?!?"
    show mike crossdress annoyed
    "How did I ever get myself into a situation like this?"
    "Saying that I'd dress in drag for the sake of getting into the band?"
    "Well, there's no way out of it now and no sense in putting it off any longer."
    "So I step out from behind the stack of speakers I've been using as cover."
    scene bg studio
    show anna b stuned at center, zoomAt(1.25, (940, 880))
    show sasha casual stuned at center, zoomAt(1.25, (640, 880))
    show kleio stuned at center, zoomAt(1.25, (340, 880))
    with fade
    mike.say "Okay, okay, here I am."
    mike.say "I hope you guys are happy now!"
    "I wasn't expecting a mature and dignified response."
    "And so I'm not surprised by the one that I get from the girls."
    show sasha happy at startle
    pause 0.1
    show anna b happy at startle
    pause 0.2
    show kleio happy at startle
    "They instantly burst into even louder peals of laughter."
    show sasha normal
    show kleio normal
    anna.say "Aw, you look so cute!"
    show anna b evil
    show kleio talkative
    kleio.say "Check out the ass on that!"
    show kleio seductive
    show sasha talkative
    sasha.say "That's really your colour, [hero.name]!"
    show sasha joke
    "I cross my arms over my chest and shake my head at them."
    "Maybe if I act like I'm unimpressed, they might grow up a little."
    "And maybe pigs will fly too!"
    mike.say "Well, you got what you wanted."
    mike.say "I'm standing here in the dress."
    mike.say "That means I'm in the band, right?"
    show sasha embarrassed
    "Sasha shrugs, her mouth turning into a resigned frown."
    show kleio normal
    show anna b normal
    "She looks to Anna and then to Kleio, who both nod in turn."
    show sasha talkative
    sasha.say "That was the deal, [hero.name]."
    sasha.say "And you kept your side."
    sasha.say "As far as I'm concerned, you're in."
    show sasha normal
    show anna b happy
    anna.say "Same here - so long as I can do your hair!"
    show anna normal
    show kleio talkative
    kleio.say "I say you're in, but it's provisional."
    kleio.say "And you're not a full band member until you play a gig like that!"
    show kleio happy at startle
    pause 0.2
    show anna b happy at startle
    pause 0.1
    show sasha happy at startle
    "This last comment elicits more laughter at my expense."
    "But I'm not about to be put off now."
    "Not after I've already endured this much abuse."
    show kleio normal
    show anna b normal
    show sasha normal
    mike.say "Whatever, Kleio."
    mike.say "The important thing is that I'm in the band, full stop!"
    "Getting no protests at this, I take it that the matter is closed."
    if anna.sexperience > 0 and kleio.sexperience > 0 and sasha.sexperience > 0:
        show sasha talkative
        sasha.say "Seriously though, [hero.name], this took some guts."
        show sasha normal
        show anna b talkative
        anna.say "Yeah, most guys I know would have never done this."
        show anna b normal
        show kleio talkative
        kleio.say "They're right, Loverboy, you've got balls!"
        show kleio normal
        "Hearing the girls talking like this after all the teasing catches me off guard."
        "And I find myself shrugging, even blushing a little as they compliment me."
        mike.say "Well...I...I wanted in on the band."
        mike.say "It really does mean that much to me, guys!"
        show sasha talkative
        sasha.say "I had no idea you were this passionate."
        show sasha normal
        show anna b talkative
        anna.say "Or this adventurous, [hero.name]!"
        show anna b normal
        show kleio talkative
        kleio.say "Yeah, it kinda makes a girl wonder, you know?"
        kleio.say "Wonder just how adventurous you can be!"
        show kleio normal
    elif anna.sexperience > 0 and kleio.sexperience > 0:
        hide sasha with dissolve
        show anna b at center, traveling(1.5, 0.3, (840, 1050))
        show kleio at center, traveling(1.5, 0.3, (440, 1050))
        "Once Sasha has gone off to do whatever, Anna and Kleio corner me."
        "They press in close, making sure that they can't be overheard."
        show kleio talkative
        kleio.say "I...I didn't think you'd do it, Loverboy."
        show kleio normal
        show anna b talkative
        anna.say "Yeah, [hero.name], you've got such big balls!"
        show anna b normal
        "I had no idea that wearing a dress can impress them both so much."
        "If I'd known, maybe I'd have done it sooner!"
        mike.say "Ah, it's no big deal, guys."
        mike.say "Especially if it means I can spend more time with you both!"
        show kleio blush
        "Is...is Kleio actually blushing a little?!?"
        show anna wink
        "And I can see that Anna has a certain twinkle in her eye all of a sudden."
        show kleio talkative
        kleio.say "You wanna try us on for size later?"
        show kleio seductive
        show anna happy
        anna.say "Yeah, I think I know just where you'd fit!"
        show anna normal
    elif sasha.sexperience > 0:
        hide anna
        hide kleio
        with dissolve
        show sasha at center, traveling(1.5, 0.3, (640, 1050))
        "Once the others have gone off to do whatever, Sasha corners me."
        "She leans in close so that we can't be overheard."
        show sasha talkative
        sasha.say "I didn't think you'd do it."
        sasha.say "But you sure showed me, [hero.name]!"
        show sasha normal
        "I try to shrug it off, but I'm grateful to hear her say it."
        mike.say "Being in the band's important to me, Sasha."
        mike.say "That and being in it with you."
        mike.say "That's why I did it."
        "Sasha smiles at this, nodding her head."
        show sasha talkative blush
        sasha.say "Well, remind me to thank you later."
        show sasha b flirt -blush
        sasha.say "You know - when we're alone?"
        show sasha normal
    elif kleio.sexperience > 0:
        hide sasha
        hide anna
        with dissolve
        show kleio at center, traveling(1.5, 0.3, (640, 1050))
        "Once the others have gone off to do whatever, Kleio corners me."
        "She leans in close so that we can't be overheard."
        show kleio talkative
        kleio.say "I...I didn't think you'd do it, Loverboy."
        kleio.say "But you sure showed me!"
        show kleio normal
        "I know how hard it must be for Kleio to admit something like that."
        "And so I shake my head and give her a smile."
        mike.say "It's just a dress - women wear them every single day!"
        mike.say "I want to show I'm committed to the band, Kleio."
        mike.say "And that I'm committed to you too."
        show kleio blush
        "Is...is Kleio actually blushing a little?!?"
        show kleio seductive
        kleio.say "Th...that's really...hot, [hero.name]!"
        kleio.say "You wanna...maybe hook up later?"
        show kleio normal
    elif anna.sexperience > 0:
        hide sasha
        hide kleio
        with dissolve
        show anna b at center, traveling(1.5, 0.3, (640, 1050))
        "Once the others have gone off to do whatever, Anna corners me."
        "She leans in close so that we can't be overheard."
        "And then stands on her tip-toes to make sure I can hear her too!"
        show anna b happy
        anna.say "Wow, [hero.name], you've got such big balls!"
        anna.say "Most guys would be terrified to wear a dress!"
        show anna b normal
        "I smile, enjoying the chance to bask in Anna's affections."
        mike.say "Ah, it's not that bad, Anna."
        mike.say "It's just a little fun, that's all!"
        show anna wink
        "Anna's smile grows suddenly wider."
        "And I can see she has a certain twinkle in her eye all of a sudden."
        show anna evil
        anna.say "Well, I'm little and fun too."
        anna.say "You wanna try me on for size, huh?"
        anna.say "Maybe feel how I fit?"
        show anna normal
    "I smile a little awkwardly, but nod at the same time."
    "It's an intriguing offer and one that I'm keen to take up."
    "But for now, the important thing is that I put my money where my mouth is."
    "Which means that I'm officially a member of the Deathless Harpies!"
    return

label scottie_appears:
    scene bg livingroom
    play sound door_banging
    "I'm about to open the door when a knock on the other side of it startles me to a halt."
    play sound door_banging
    "Actually, 'knock' is too passive -- someone's pounding on the door with their fist, impatient and demanding."
    "I draw my hand back from the doorknob, frowning. Who could that possibly be?"
    scottie.say "Open up! Hey! I know you're in there, you black-hearted bitch!"
    "Oh. That's... not for me."
    "I hear a groan from somewhere down the hallway, and then footsteps as the 'bitch' herself makes her way to the living room, propping her hands on her hips."
    show sasha vangry with easeinleft
    sasha.say "That's mine, I guess."
    show sasha annoyed
    "I give a nervous sort of chuckle and step aside, giving a sweeping gesture to the door that tells her: it's all yours."
    "But she doesn't seem to think that's how this goes, giving her head a short shake before folding her arms and tilting her head toward the door."
    show sasha shout
    sasha.say "Nuh uh. You answer it. I need a meat shield so his dumb ass doesn't try to barge inside."
    show sasha normal
    "I don't think I signed up for this. But it feels a little too pathetic, suddenly, to decline her while she's got those dark eyes locked on me like that."
    "If my masculinity is at stake, I guess I'll play the hero."
    play sound door_banging
    "The door hasn't stopped rattling in its frame under the assault for the duration of our brief exchange, and I make my way over to it and flip open the lock, pulling it ajar."
    stop sound
    scene bg house
    show scottie
    with wiperight
    "Seemingly surprised by this, the beefhead on the other side knocks the suddenly open air once before clearing his throat and composing himself, puffing himself up and setting a hateful scowl onto his face."
    scottie.say "Who the hell's this doofus? Where's Sasha?"
    scene bg livingroom
    show sasha angry
    sasha.say "I'm right here, genius..."
    show sasha annoyed
    "Sasha speaks from behind me, sounding exasperated already."
    show sasha vangry
    sasha.say "How the hell'd you get this address?"
    scene bg house
    show scottie
    scottie.say "I have my ways."
    "The bulky blonde in front of me answers, trying to sound gruff and mysterious, I'm sure."
    "I get the impression that he just stalked her social media, though, and it's not that deep."
    "I hear Sasha scoff behind me and step forward, stopping just behind my shoulder to address our uninvited guest."
    scene bg livingroom
    show sasha vangry
    sasha.say "Cry about whatever you came to cry about, then, and piss off."
    scene bg house
    show scottie
    "The dude's face screws up a little more, and for a second I think he is about to cry."
    "But then he puffs up a little bit more instead, seeming to regain himself, and turns up his volume instead."
    scottie.say "I want answers, you cheating whore!"
    scene bg livingroom
    show sasha annoyed
    "Sasha sighs, as though this song and dance isn't new."
    show sasha whining
    sasha.say "I didn't cheat on you, Scottie."
    scene bg house
    show scottie
    scottie.say "Yeah, right! Why else would you have left something like this?"
    "He flexes stupidly in front of our doorway, and I have to bite my tongue to stifle a laugh. What an embarrassment."
    scene bg livingroom
    show sasha upset
    "I turn a bit to glance back at Sasha, who's pinching the bridge of her nose."
    "She must be thinking the exact thing I'm thinking: how the hell did she ever date someone like this?"
    show sasha vangry
    sasha.say "Maybe because you're the kind of jackass who comes pounding on my door uninvited."
    scene bg house
    show scottie
    "He seems to completely miss this, or just not care. His eyes are fixed on me now, sizing me up."
    scottie.say "Who's this wimpunk? Huh? This what you're bangin' now? Your standards are low, Sasha."
    scene bg livingroom
    show sasha annoyed
    "She only grunts out a sound of exasperated disgust behind me, and I see her shift her weight and fold her arms from my peripheral."
    "Maybe she's tired of communicating with him already, but a beat of silence falls between them that's a little too long. It feels like my job to fill it."
    scene bg house
    show scottie
    menu:
        "Not as low as they were.":
            $ sasha.love += 2
            "I straighten myself and turn back to face 'Scottie' fully, my expression smug."
            mike.say "It'd be hard to downgrade from someone like you."
            "Scottie tenses up and clenches his jaw, and I feel like I can almost see him physically boiling like some old cartoon."
            scottie.say "Big talk for someone your size, punk! Take it outside and I'll grind you into the pavement!"
            scene bg livingroom
            show sasha vangry
            sasha.say "Alright, Scott, knock it off."
            show sasha upset
            "Sasha snaps, seemingly losing her already thin patience."
            show sasha vangry
            sasha.say "Get out of here before I call your mom and tell her you're still picking fights."
            show sasha upset
            "This time I don't hide my amusement, snickering openly at the idea that she was going to call his mommy like a middle schooler, and even more so at how quickly he seems to cower from the idea."
            scene bg house
            show scottie
            scottie.say "That's low, Sash."
            "His voice is a wounded mumble, now, a dog scolded."
            scottie.say "We had something special."
            sasha.say "It's hard to believe that's even true."
            "He looks even more hurt by this, and I think if he didn't storm up acting like such a dick I'd almost feel bad about how he turns away, drooping as he makes his way back down the hall."
        "You're right. Sasha's a goddess." if sasha.love >= 50:
            $ sasha.sub -= 5
            "I pull a crooked smile and lean an elbow against the doorframe, making sure 'Scottie' has a good view of the babe standing behind me, in my house, on my side of the door."
            mike.say "She's out of my league."
            "I speak cooly, buttering her up as much as I'm taunting this meathead."
            mike.say "But I'd say my chances are still pretty good, if she ever settled for a monkey like you."
            "Sasha gives a sort of soft chuckle behind me, and Scottie goes red in the face, tensing up like he's about to burst in front of me like a balloon."
            scottie.say "Say that to my face!"
            "Sasha sighs."
            sasha.say "He just did."
            scottie.say "Yeah, w-well--!"
            "Scottie stammers a bit, then clenches his beefy hands into fists, and I think, for a moment, he's planning on pummeling me in the doorway."
            scene bg livingroom
            show sasha upset
            "But Sasha steps back in before he can, stepping forward until she's nearly beside me and speaking in a low and serious tone."
            show sasha vangry
            sasha.say "Enough, Scott. Get out of here before I call the cops."
            scene bg house
            show scottie
            "He seems to teeter a moment on the idea of risking it to punch my teeth out, then deflates with a heavy, childish sigh, spinning back sharply and stomping his way down the hallway."
            scottie.say "This isn't over, you piss-soaked ramen noodle! You better hope I never catch you on the street!"
            "Though he's not the sharpest pencil in the box, I kind of do hope he never does. I could probably talk circles around him, but I don't know what he can do with those muscles if he goes into some kind of toddler hissy fit."
            "I guess I just hope I never bump into him in a back alley or something."
        "She'll be mine soon enough." if sasha.love >= 50:
            $ sasha.sub += 5
            "I let a cocky smirk cross my face and lean myself against the doorframe, making sure 'Scottie' has a clear view of his ex behind me while I speak."
            mike.say "Let it go, beefcake. She's in much better hands now."
            "Scottie sets his jaw, and I see his shoulders tense up, like he's ready to start swinging."
            scottie.say "What, yours? You probably couldn't lift her if she was begging for it!"
            mike.say "I guess I'll just have to test that out later."
            "Scottie starts going red in the face, almost visibly broiling, like some old-timey cartoon."
            scottie.say "Like hell you will!"
            scene bg livingroom
            show sasha vangry
            sasha.say "Alright."
            show sasha upset
            "Sasha raises her voice over both of us, stepping forward until she's almost beside me and giving me a slight shove on my shoulder, as if to say I'm being just as bad."
            sasha.say "Both of you knock it off."
            scene bg house
            show scottie
            scottie.say "Fight me for her, then, pipsqueak!"
            "Scottie nearly roars, disregarding her and clenching his big hands into fists."
            scottie.say "We'll see who's hands are better... hands!"
            scene bg livingroom
            show sasha vangry
            sasha.say "Scottie!"
            show sasha upset
            "This time her voice is a sharp bark, and like an obedient dog he deflates a little under the sound. It must be a tone he's learned means he's crossed a line."
            sasha.say "I said that's enough! Get out of here before I call your mother again."
            scene bg house
            show scottie
            "I laugh openly at how he cowers from this threat, and the implication that it's come to that before. He seems to unwind, his taut muscles relaxing as he steps back from the door."
            scottie.say "Come on, Sash... that's not fair."
            "Sasha jabbed a finger down the porch, her own jaw set."
            "Sighing, defeated, Scottie obeyed... but not without shooting me a death glance over his shoulder, that said: this isn't over yet."
            "That's fine. If it comes down to proving I can pin Sasha back against the wall and have my way with her any day, I'll fight any fights I need to."
    scene bg livingroom
    show sasha annoyed
    "She gave another exhausted, exasperated groan from behind me, and I stepped back from the doorway, allowing her to close it quietly behind me."
    show sasha whining
    sasha.say "Sorry about that..."
    show sasha sadsmile
    mike.say "An ex, I take it?"
    show sasha annoyed
    "She rolls her eyes and folds her arms beneath her breasts, shaking her head slightly in disapproval."
    show sasha whining
    sasha.say "Unfortunately."
    show sasha sadsmile
    "I can't help but snort an amused laugh, quirking a brow."
    mike.say "I wouldn't have pegged him as your type."
    show sasha shout
    sasha.say "Yeah, well."
    show sasha normal
    "She steps by me, a mysterious, catlike glimmer flashing in her eyes as she pass."
    show sasha joke
    sasha.say "Maybe you'd be surprised by what I'm into."
    show sasha normal
    "Ooh."
    "Something thrills through me as she purrs these words and moves past me back to her bedroom, and I turn and let my gaze follow her as she does."
    "My eyes linger, shamelessly, on the pert motion beneath her cutoff shorts before I draw in a deep breath and turn back away, a helpless smile crossing my face from ear to ear."
    $ sasha.flags.scottieDelay = TemporaryFlag(True, 7)
    return

label sasha_scottie_talk:
    show sasha annoyed
    "I can tell that something's bugging Sasha the moment that I see her."
    "She looks preoccupied and isn't really paying attention to anything or anyone around her."
    "I could just leave it alone, as whatever's bothering her is probably none of my business and she's not volunteering any information either."
    "But I get the irresistible urge to play the part of the understanding housemate, and I hope, maybe even friend."
    "And right now, it seems to me that Sasha could probably do with a sympathetic ear for her problems."
    mike.say "Penny for your thoughts, Sasha?"
    show sasha surprised
    sasha.say "Huh...what was that, [hero.name]?"
    show sasha stuned
    mike.say "I just thought that you looked like you had a something on your mind."
    mike.say "If you want to talk about it, I'm all ears..."
    show sasha normal
    "Sasha smiles at me in a way that makes me wonder if I want to limit my ambitions to being just a friend after all."
    show sasha happy
    sasha.say "That's sweet, [hero.name], thanks for the offer."
    show sasha shout
    sasha.say "Normally, I'd say no...but it's got to do with guy problems."
    sasha.say "So maybe you could give me some advice from the other side of the gender divide?"
    show sasha normal
    "Guy problems?"
    "Is this a chance to get a glimpse into Sasha's personal life?"
    mike.say "Sure, Sasha...if you think that'd help."
    "She smiles, the gratitude clear to see in her eyes, and puts a hand atop mine."
    show sasha shout
    sasha.say "Thanks, [hero.name] - you're a real friend to me."
    sasha.say "Most guys are only interested in getting into my knickers, but you're one of the good ones."
    show sasha normal
    "I almost blush at the fact that I was thinking about that very thing only a couple of seconds beforehand."
    mike.say "Anyway, you were going to tell me all about this problem that you have with a guy?"
    "What a smooth recovery!"
    show sasha shout
    sasha.say "Yeah, of course."
    sasha.say "Well, it's kind of one of those situations where you date someone for a while, and it's pretty okay."
    show sasha whining
    sasha.say "But then you break up for whatever reason, and you forget about all of the stuff that bugged you about them."
    show sasha normal
    "Sasha looks at me to check that I'm still following her, and I nod for her to continue."
    show sasha shout
    sasha.say "And then, when they inevitably call you up out of the blue, you're torn."
    sasha.say "Because all you can really remember is the good stuff, but you know that there was enough bad stuff to end it the first time."
    sasha.say "You know what I mean?"
    show sasha normal
    "Not really, as I don't have a string of former girlfriends calling me up all the time, trying to win me back!"
    "But I nod anyway, just to keep the conversation going and for the sake of feeling useful."
    mike.say "Sounds like there's more to it than that, Sasha."
    mike.say "Who is this guy, and what is it about him that's got you so tied up in a knot?"
    show sasha annoyed
    "Sasha sighs and nods her head, before she going on."
    show sasha shout
    sasha.say "His name's Scottie, and he's not as bad as all that."
    show sasha normal
    "Even with those few words on the subject, I instantly come to the conclusion that, in reality, he's probably much worse than all that."
    show sasha shout
    sasha.say "I mean, he could be really sweet when he was in the mood."
    sasha.say "And that body..."
    show sasha embarrassed
    "At that, Sasha seems to stare into space for a moment, as if the image it summons from her memory is just that impressive."
    mike.say "Ahem...maybe if we try to focus on the negatives that you mentioned, rather than the positives, Sasha?"
    mike.say "Like...what was the actual reason that you broke up with this Scottie?"
    show sasha normal
    "Sasha shakes her head, which seems to bring her back to reality, and then shrugs."
    show sasha whining
    sasha.say "I don't know...I guess he was just such an insensitive meat-head at times, you know - thick as fuck."
    show sasha sad
    "This guy sounds like a text-book case - a million dollar body and a ten cent brain."
    show sasha shout
    sasha.say "So, as a guy, what do you think I should do?"
    show sasha normal
    menu:
        "You should give him a second chance":
            $ sasha.love += 5
            "I could just dump on the guy, tell Sasha that he sounds like a complete asshole - which he kind of does."
            "But would that really make me any better than him in the long run?"
            "I mean, at least some of my motivation for trying to turn Sasha off the idea would be on account of my own jealousy."
            mike.say "I don't think you'd be even considering taking this guy back if you didn't like his good points more than his bad ones."
            "Sasha nods at this, her face taking on a thoughtful look as she ponders my reasoning."
            show sasha shout
            sasha.say "Huh, I suppose you're right!"
            sasha.say "Maybe he's realised what bugged me when we were together and wants to tell me he's really changed?"
            show sasha normal
            "I think it's more likely that he's sprouted a second head in the time they were apart."
            "But I nod all the same."
            show sasha shout
            sasha.say "And if not, I can always work really hard on changing him myself!"
            show sasha normal
            "I have to try real hard to keep from rolling my eyes and groaning at that old cliche."
            mike.say "Stranger things have happened..."
            "Sasha seems pleased with the way the conversations gone, relaxing noticeably for the first time since the subject came up."
            "Whatever kind of disaster this whole thing turns into, I think I deserve a ton of karma for the way I just handled it!"
        "Don't bother with the dude (Never meet Scottie again)":
            $ sasha.sub += 5
            "Jesus - this guy sounds like a bloody pain in the arse!"
            "I may be jealous of someone else having a chance with a girl as cute as Sasha."
            "But the way I see it, if she starts seeing this wanker again, then he'll be hanging around here all the time too."
            "So I'm not just against this for Sasha's sake, but for mine and [bree.name]'s as well!"
            mike.say "It's really great of you to think of giving this Scottie another chance, Sasha."
            mike.say "But he sounds to me like one of those guys that never really changes."
            "Sasha looks at me a little quizzically, as if not too sure of my sweeping statement."
            show sasha whining
            sasha.say "Really, because he sounded so sincere when we last spoke?"
            sasha.say "I was so sure of what he said that I was teetering towards taking him back."
            show sasha sadsmile
            "I shake my head and give her hand a little squeeze, just enough to reassure her of my sincerity."
            mike.say "Sasha, I think you can trust my judgement on this kind of thing."
            mike.say "The only motivation I have for saying this is my own experience and the fact that we're friends."
            mike.say "If you've been hurt by this guy in the past, then the healthiest thing would be to make a clean break of it."
            mike.say "Try seeing someone new, or don't..."
            "Wait a minute, that sounds even better!"
            mike.say "You know, a stint of celibacy might be just what the doctor ordered..."
            "And all the while, I can be working on my chances of getting in there myself!"
            show sasha normal
            "Sasha nods at this, looking as though she's becoming more open to the idea the more she thinks about it."
            $ sasha.flags.disable_scottie_events = True
        "You already know":
            "Part of me can't believe I'm hearing Sasha talk like this."
            "I mean, isn't she supposed to be a modern, independent woman?"
            "She shouldn't need to be asking another guy for advice on this guy!"
            mike.say "Seriously, Sasha?"
            mike.say "You already know the answer yourself."
            mike.say "You don't need me to tell you what to do!"
            show sasha surprised
            $ sasha.sub += 1
            "Sasha looks at me with a surprised expression on her face."
            show sasha annoyed
            "But then she nods and lets out a sigh of frustration."
            show sasha shout
            sasha.say "You're probably right, [hero.name]."
            sasha.say "I'm just asking you in the hope you'll agree with me."
            sasha.say "Thanks for the advice - it really made me see through my own bullshit!"
            show sasha normal
            $ sasha.love += 2
    "With that issue addressed, the conversation returns to more normal and neutral subjects."
    "I find myself hoping that I've made the right decision in terms of my advice to Sasha."
    "But I can still feel the shadow of this Scottie guy hanging over me, like an oppressive presence lurking in my immediate future."
    $ sasha.flags.scottieDelay = TemporaryFlag(True, 7)
    return

label sasha_scottie_bj:
    $ sasha.flags.scottieDelay = TemporaryFlag(True, 7)
    show bg secondfloor
    "It's really not my fault that Sasha isn't in the habit of making sure that she closes her bedroom door behind her."
    "Likewise it's not my fault that she does this just before getting into doing something that's so loud the sound carries easily."
    "And with both of those factors taken into account, can I really be held responsible for creeping up and peering in through the crack in that same door?"
    "I mean, I'm only human, after all..."
    "I crouch down outside of Sasha's door and peek inside, thankful that there's enough light for the entire scene to be visible as I do so."
    show bg bedroom3
    show sasha casual embarrassed at right5
    show scottie at left5
    with fade
    "There's Sasha, of course, looking as darkly hot as she ever has."
    "And there's a guy, tall and well-built, with long, blonde hair that's tied back in a ponytail."
    "He's wearing a band t-shirt that I recognise only because I've seen an almost identical one on Sasha that she uses as a night-shirt."
    "Is that where she got the damn thing from in the first place?"
    "Fuck, that's Scottie (I fucking hate that dude)."
    "Scottie has a dumb look on his face right now, like a dog that's realised it's about to get a treat."
    "And why wouldn't he - from the way Sasha's looking at him and letting out the occasional filthy giggle, that's going to be quite some treat!"
    "I shouldn't watch what's about to happen, but I find that I simply can't tear myself away from the door."
    "A heady mixture of genuine lust for Sasha and mounting jealousy towards Scottie keeps me firmly rooted to the spot."
    "It's as though I think that by watching them, I can somehow lessen the impact of what I see and be better armed against Scottie in the future."
    show sasha at right4
    show scottie at left4
    with ease
    "They begin slowly, with Sasha helping the dumb brute to pull off his t-shirt."
    "Of course, this means that his long hair falls over his face in just the right way the moment that his muscular chest is fully revealed."
    "Instantly I can see clearly the effect that Sasha described the guy as having on her."
    "She almost purrs as she runs her hands over the contours of his pecs and then down over his washboard stomach too."
    "Unconsciously, I feel my own hand against my admittedly smaller chest."
    "And I can't help contemplating making the gym a higher priority in my daily routine."
    "Scottie watches in blissful silence as Sasha begins to unzip his pants and then slips a hand inside."
    "Somehow she manages to unbuckle his belt with her free hand, while I guess she's squeezing away on his cock with the other."
    "The look on Scottie's big dumb face makes me sure that's the case, as he grins widely in appreciation at what she's doing."
    "As soon as she has his jeans unbuttoned at the waist, Sasha wastes no time in pulling both them and his shorts down in one rough motion."
    show scottie naked with dissolve
    "Part of me recoils at the notion of staring at another guy's cock, even more so as it's about to be handled by a girl I find deeply attractive."
    if not hero.has_skill("hung"):
        "But almost as soon as I see it rebound from the tension it's been under whilst restrained by his underwear, I can't help staring at Scottie's cock."
        "I guess that this is one of those shitty times in life, when just for a moment, you have to put your personal feelings aside and simply admit to the undeniable truth of a thing."
        "Okay, I'll admit it - Scottie's blessed with an impressive manhood."
        "Now let's just put that behind us and get back to the matter at hand, okay?"
    else:
        "Not as impressive as my own tool, but pretty good."
    menu:
        "Watch":
            $ sasha.flags.WatchedScottieBJ = True
        "Leave":
            "That's it - I've seen enough!"
            "As much as I have the hots for Sasha and the hates for Scottie, I'm no Peeping Tom."
            "Standing up and turning away from the door, I leave them to it."
            "Trying the whole time to ignore the sounds that are still spilling out of Sasha's room."
            return
    hide scottie
    hide sasha
    show sasha bj2 bedroom3 scottie casual
    with fade
    "Sasha also seems suitably impressed with what she sees, even though she's supposedly seen it all before."
    "Has she really missed the sight of his cock that much?"
    "Whatever the case may be, she now wastes no time in starting to caress and stroke both his balls and the shaft."
    "Sasha holds his eye the whole time, making him watch her like an animal hypnotised by the swaying and rearing of a venomous snake."
    "Still holding his eye, she then lowers herself down, using his body as support the whole way, until she's kneeling before him."
    $ renpy.sound.play("sd/moans/sasha/sasha_blowjob_low.ogg", loop=True)
    show sasha bj2 scottie lick
    "Only now does Sasha turn her eyes downward, as she takes one of his balls in her mouth and sucks on it with clear relish."
    "Scottie groans instantly, his expression changing swiftly from one of feckless anticipation to intense surprise."
    "Sasha keeps on sucking on his balls, changing from one to the other and squeezing what's not in her mouth with her fingers too."
    "I can clearly see his cock twitching and shaking from what she's doing just below it, and a bead of prejaculate glimmers in the light on the very tip."
    "Wouldn't it be a shame if the brute came before she even managed to get his cock in her mouth..."
    "But Sasha's no amateur at this game, and she soon releases Scottie's scrotum and moves on to the more pressing matter of his cock itself."
    hide sasha
    show sasha bj2 bedroom3 scottie closed casual
    "She begins by licking vigorously at the very base of his shaft, almost forcing a reaction with her tongue."
    "It seems that Scottie prefers things rough and heavy, as Sasha blends her licks here and there with actual nips from her teeth."
    "All of this serves to mean that, as she climbs ever higher up Scottie's cock, his reactions to her become all the more intense."
    "By the time she reaches the head, he almost red in the face and clearly covered in perspiration."
    "The guy looks as strong as an ox, and so the state that he's in can only be on account of Sasha's attentions."
    "Looks like she knows exactly how to make the guy dance to her chosen tune!"
    "Scottie makes things even easier for Sasha when he suddenly collapses onto the bed and remains sat upon the edge, panting in delight."
    $ renpy.sound.play("sd/moans/sasha/sasha_blowjob_medium.ogg", loop=True)
    show sasha bj2 scottie suck opened
    "This means that Sasha has no trouble in catching the head of his cock between her lips."
    "She holds it here for a moment or two, like it's her prey and she's enjoying the chance to toy with it."
    "And then she swallows the entire head, so that she can caress the sensitive tip of his manhood with the whole of her mouth."
    "Sasha keeps on taking a little more of him into her mouth at regular intervals, looking into his eyes as she does so."
    "Watching her, I'm reminded of a snake that dislocates it's jaw in order to swallow it's prey entirely and in successive stages."
    "I can even detect a hint surprise and disbelief in Scottie's eyes as he watches what Sasha's doing."
    "Has he forgotten what she's capable of, or is this a new level of skill that she's mastered in the time they've been apart?"
    "Once she's got him in as deep as she's going to take him, Sasha begins to move her head back and forth."
    "I can see her cheeks going hollow and then filling out again as she does all that she can to get Scottie off."
    "Sasha has her thumb and index-finger wrapped firmly around the base of Scottie's cock now."
    "And whenever a significant length of his cock is out of her mouth, she rubs these up and down vigorously."
    "Often her hand meets her own lips, and she seems to be determined to milk the guy for all that he's worth."
    scottie.say "Oh shit, Sasha...I'm gonna blow!"
    scottie.say "This is so awesome, babe!"
    "Is this guy for real?"
    "What's he going to say next?"
    "Bodacious...tubular...far out?"
    hide sasha
    show sasha bj2 bedroom3 scottie dick closed smile casual
    stop sound
    "But upon hearing Scottie's warning, Sasha finally releases his cock from her mouth."
    "Though she still keeps a tight hold on the slippery dick, almost flicking the tip with her tongue as she continues to lick at it."
    show sasha bj2 scottie opened open cum face with vpunch
    "This means that when Scottie cums, and cums mightily too, Sasha is almost hosed full on in the face."
    with vpunch
    "She closes her eyes as ropes of Scottie's cum spurt across her face and begin to slowly ooze down towards her chin."
    with vpunch
    "Not that she seems to mind, as her mouth opens in a satisfied smile and her tongue emerges to lick up the white droplets that are already upon her lips."
    scene bg secondfloor with fade
    "It's then that I realise the show is all but over, and which means it's high time I was making myself scarce."
    "I scuttle back to the relative safety of my room, mind filled with images of what I've just seen."
    "The whole thing makes me feel pretty conflicted, as while I hate the idea of this becoming a regular occurrence, I have to admit what I just saw was rather hot in nature."
    "I can't decide whether I want Scottie firmly out of the way so I can take his place."
    "Or whether I really want him to stick around in the hope of seeing more of the same between him and Sasha."
    return

label sasha_disable_scottie_events:


    $ sasha.flags.disable_scottie_events = True
    return

label sasha_threesome_request:
    show sasha shy
    "Sasha keep looking over at me, keeping her eyes on me for a couple of seconds and then turning away before doing the whole thing all over again."
    show sasha embarrassed
    "I try to ignore it as best I can, but it's like her gaze is boring into me every time she does it, and it's starting to get under my skin."
    show sasha shy
    "Every time she seems to be on the verge of saying something, and then chickens out at the very last minute."
    show sasha embarrassed
    "Finally, when I feel as though it's going to end with me screaming and running away in a state of sheer insanity, I decide to call her bluff."
    mike.say "Okay, Sasha - out with it!"
    show sasha surprised
    sasha.say "Huh, out with what?"
    show sasha stuned
    "I groan and roll my eyes in frustration."
    mike.say "Sasha, your eyes have been burning a hole in the side of my head for an age now."
    mike.say "What is it that you keep trying to pluck up the courage to ask me all this time?"
    show sasha whining
    "For a moment, Sasha's face seems to say that she's going to try and argue the point."
    show sasha sadsmile
    "But then she shrugs in apparent surrender."
    show sasha shout
    sasha.say "Okay, okay...I'll say it."
    sasha.say "But I'm not sure how receptive you're gonna be."
    sasha.say "So you've been warned, yeah?"
    show sasha normal
    "I nod, more for the sake of getting Sasha to finally spill her guts than actually wanting to know what it is she's been stewing on the entire time."
    mike.say "Go ahead, Sasha, surprise me!"
    "Sasha takes a deep breath before she obliges."
    show sasha shout
    sasha.say "Well...thing was...I was was kinda wondering if you'd be up for...maybe trying a threesome sometime soon?"
    show sasha sadsmile
    "Well, let's just say that while I'm not surprised, I am greatly intrigued!"
    mike.say "That sounds like a great idea, Sasha."
    mike.say "Why in the hell would you be hesitant to ask me that?"
    show sasha shout
    sasha.say "Ah...you can be kind of vanilla sometimes, you know?"
    sasha.say "I find it hard to guess what you'll be up for and what you won't most of the time..."
    show sasha normal
    "'Vanilla' - what does she mean by that?!?"
    "Maybe she needs to be reminded of just how adventurous and outrageous I can be when the mood takes me!"
    mike.say "I'm up for this, I can tell you that."
    show sasha happy
    "Sasha's mood suddenly picks up visibly and a wide smile spreads across her face at my declaration."
    sasha.say "Really?"
    sasha.say "That's great, really great."
    show sasha shout
    sasha.say "And don't you worry, the guy that I have in mind is perfect for this kind of thing."
    sasha.say "You'll get on so well with him, I promise!"
    show sasha normal
    "Wait a minute - did she just say 'guy'?!?"
    menu:
        "Change your mind":
            $ sasha.love -= 10
            mike.say "Whoa, whoa, whoa...Sasha - what do you mean you have a GUY in mind?"
            show sasha sad
            "Sasha looks at me oddly, as if she doesn't really understand my objection."
            show sasha happy
            "Then she puts her hand to her mouth to stifle a laugh she can't quite keep from bursting out."
            show sasha shout
            sasha.say "Oh, [hero.name] - did you just freak out because I wanted to invite another guy along for sex?"
            sasha.say "Aww, that's so cute and twentieth-century of you - to just automatically assume I'd be hooking us up with a girl!"
            show sasha normal
            "Before I was feeling uneasy and threatened about some other guy's cock waving about in my immediate vicinity."
            "But now I'm also burning up with embarrassment at Sasha calling me some kind of sexual throwback."
            show sasha shout
            sasha.say "Like I said before, don't worry."
            sasha.say "He really is perfect for this kind of thing, [hero.name]."
            sasha.say "You know, great body and a fucking massive..."
            show sasha normal
            mike.say "SASHA...this is not helping to sell me on the idea!"
            show sasha joke
            sasha.say "It'll be fine - I'll be there to look after you..."
            sasha.say "We can even make it clear before we get started that, under no circumstances, is he to put his cock up your ass."
            show sasha normal
            mike.say "No, Sasha...N...O...No - do you understand me?"
            show sasha sad
            "Sasha sighs in resentment, starting almost instantly to go into a pout."
            show sasha annoyed
            sasha.say "Urgh...whatever, [hero.name]."
            sasha.say "It would have been fun too - if someone not a million miles from here wasn't so sexually repressed..."
            $ sasha.flags.disable_scottie_events = True
        "Stick with it":
            show sasha shout
            sasha.say "His name's Scottie, and he's an old friend of mine..."
            show sasha normal
            "That name sounds oddly familiar to me, like Sasha's mentioned it before."
            mike.say "'Scottie'...where do I recognise that name from, Sasha?"
            "Sasha pauses, clearly knocked off of her stride by the question."
            show sasha shout
            sasha.say "I might have told you about him already - he and I used to date."
            sasha.say "But that was before I moved in with you and [bree.name]."
            sasha.say "It's well over now, and we're just good friends."
            show sasha normal
            "That's it, he's one of Sasha's former boyfriends."
            "And from the sound of it, she wants him to be a friend with benefits too!"
            "Whatever I might think about the reality of getting into a threesome with Sasha and another guy, I'm not about to let this guy make me look bad by comparison."
            mike.say "Sure, Sasha, sign me up."
            show sasha surprised
            $ sasha.love += 5
            sasha.say "You mean it - you're up for this?"
            show sasha stuned
            mike.say "Yeah, of course - it's the twenty-first century, Sasha."
            mike.say "What did you think, that I was backwards enough to just assume you wanted to bring along another girl?"
            mike.say "This is supposed to be sex between three equal, consenting adults, after all."
            mike.say "Not some sad little adolescent male wank fantasy!"
            show sasha normal
            "Sasha grins at me, clearly feeling pleasantly surprised at how liberated I've turned out to be."
            "I smile too, but it's more a rictus of worry that I might not be able to live up to the hype that I've created for myself."
            $ sasha.flags.scottiethreesome = 1
    "Once the discussion dies down, we both become silent for a short while."
    "But I can bet that Sasha's mind is on nothing but the matter of the threesome."
    "Because I know that's what is on my mind as well."
    return

label sasha_likes_blondes_1:
    scene bg livingroom
    show sasha at center, zoomAt (1.25, (640, 880))
    "It's one of those evenings when no one needs to spell it out, everyone just knows that you're all dog-tired and wanting to chill out in front of the TV."
    "To begin with, it's just Sasha and me, so there are lazy embraces and maybe a few more relaxed possibilities on the cards."
    show sasha at center, zoomAt (1.25, (440, 880))
    show bree sport at center, zoomAt (1.0, (940, 720))
    with easeinright
    show bree at center, traveling(1.25, 0.3, (840, 880))
    "But then [bree.name] joins us, and the mood becomes altogether more focused on simply filling the remaining hours of the day with laziness and inactivity."
    "At some point, one of us thinks to order pizza, but I'm so tired and unfocused that I really can't recall who."
    hide bree with easeoutright
    "Maybe it was [bree.name], as she's the first up and making for the door when the food arrives."
    show bree sport at center, zoomAt(1.25, (840, 880)) with easeinright
    "On her way back in, she bends over to put the boxes down on the coffee table, and I get an unexpected chance to check out her ass as she does so."
    "I wasn't looking to ogle [bree.name] in particular."
    "But as she's wearing yoga pants and her backside is no more than a metre from my face, I kind of can't help getting an eyeful."
    show sasha annoyed with hpunch
    "Sasha elbows me in the ribs, snapping me out of my reverie and letting me know that she can see what I'm doing."
    "As [bree.name] stands up, I feel the need to lessen the severity of my transgression somehow."
    mike.say "Did you do something to your hair, [bree.name]?"
    show bree smile
    bree.say "Erm, no...just washed it like I always do for a night in."
    show bree normal
    mike.say "Well, whatever you did...it looks pretty good."
    show bree talkative
    bree.say "Okay...thanks, [hero.name]...I guess."
    show bree normal
    "In the awkward silence that follows, I have no idea whether my clumsy attempt to cover my tracks has worked or actually made things worse."
    show sasha normal with fade
    "We eventually get back to making meaningless small-talk and watching the TV as the pizzas are slowly devoured."
    show bree happy
    "[bree.name] yawns a little later, starting everyone else off doing the same."
    show bree smile
    bree.say "Okay...I'm turning in, before I fall asleep right here on the couch!"
    show bree normal
    "Sasha and I make our excuses and say that we're staying up still later."
    hide bree with easeoutright
    "But even as I do so, I'm already worried that Sasha's going to chew me out for staring at [bree.name]'s backside."
    show sasha at center, zoomAt (1.25, (640, 880)) with ease
    "To her credit, Sasha waits almost a full five minutes before making what's supposed to be an innocent comment."
    show sasha shout
    sasha.say "[hero.name]...I heard you complimenting [bree.name] on her hair before."
    show sasha normal
    mike.say "Ah...yeah?"
    "How could she have failed to hear me?"
    "She was sitting right there next to me at the time!"
    show sasha shout
    sasha.say "This is gonna sound pretty dumb...but do you prefer blondes, or something?"
    show sasha whining
    sasha.say "I mean, you never complimented me like that."
    show sasha sadsmile
    "Although I'm relieved to not be answering the more dangerous question involving [bree.name]'s ass, this could still be a potential minefield in its own right."
    "I can see Sasha's looking at me like she expects an answer, and I can't think up a credible way out of giving her one."
    menu:
        "I prefer blondes":
            mike.say "Well, it's not that I PREFER blondes in any official capacity."
            mike.say "You know, I don't have a membership card for the 'International I Love Blondes Society' in my wallet next to my credit cards."
            show sasha shout
            sasha.say "But you do like them, don't you?"
            show sasha normal
            mike.say "Of course I like them, Sasha - I like women with all different colours of hair."
            mike.say "It's just that..."
            $ sasha.love -= 10
            show sasha whining
            sasha.say "It's just that what?"
            show sasha annoyed
            "I can feel myself clutching at straws as I stumble over my words."
            mike.say "It's just that you kinda get it drummed into you that blonde is best, you know?"
            mike.say "TV, magazines, movies - they're all full of blondes."
            mike.say "Even when someone's not blonde, there are ads all over the place for stuff to dye your hair blonde."
            mike.say "You get to the point where you're indoctrinated."
            show sasha normal
            "Sasha nods a little."
            show sasha whining
            sasha.say "You want to try being a non-blonde...that's pretty tough sometimes too."
            show sasha sadsmile
            mike.say "So yes...I guess that I do like blondes."
            mike.say "But it's never been a deal-breaker for me either."
            $ game.flags.LikesBlondes = True
            $ sasha.flags.LikesBlondesDelay = TemporaryFlag(True, 1)
        "I don't prefer blondes":
            mike.say "Me, prefer blondes?"
            mike.say "Hell no!"
            show sasha shout
            sasha.say "Really?"
            show sasha normal
            mike.say "Yes, really - I always hated the way that they're shoved down your throat."
            mike.say "Whenever you turn on the TV or open a magazine, it's just blondes, blondes, blondes."
            mike.say "They turn into 'blands' pretty quickly, if you know what I mean?"
            show sasha happy at startle
            "Sasha nods and laughs at the lame joke, seeming pleased with the answer."
            $ sasha.love += 5
            show sasha shout
            sasha.say "That's a relief to hear."
            sasha.say "I was thinking that you might have wanted me to go do something crazy, like bleach my hair!"
            show sasha normal
            mike.say "Nah, I like it just how you have it now."
            mike.say "Don't go changing it on my account."
            show sasha surprised
            "Sasha screws up her face in mock horror."
            sasha.say "But if you weren't into [bree.name]'s hair...you must have been checking out her butt!"
            mike.say "Sasha, I couldn't help it!"
            mike.say "It was like an inch from my face!"
            show sasha happy at startle
            "Sasha laughs and waves away my protests."
            show sasha shout
            sasha.say "Relax, [hero.name] - you're only human, and it's a nice butt!"
    show sasha normal
    "That's the last either of us has to say on the matter for the rest of the night."
    "I find myself hoping that it's nothing more than an idle conversation that Sasha will soon forget all about."
    "But then I remember how deep and emotional she can be, and I wonder, not for the first time, if what I've said will end up coming back to haunt me."
    return

label sasha_likes_blondes_2:
    $ sasha.flags.haircut = True
    scene bg livingroom
    "I admit that I have a habit of getting home and collapsing in front of the TV at the end of the day, zoning out and being hard to reach."
    "But in my defence, I have a tough job, my boss is an asshole of the highest order, and my personal life isn't exactly serene at the moment either."
    show sasha at center, zoomAt (1.0, (1040, 720)) with easeinright
    "So when someone walks confidently into the living room and almost seems to present themselves for an inspection, it takes me a couple of seconds to snap out of it."
    show sasha at center, zoomAt (1.0, (940, 720)) with ease
    "Almost immediately I know that this is the wrong decision, as the first thing I realise is that the person standing in front of me is female, and demanding attention."
    show sasha at center, zoomAt (1.0, (840, 720)) with ease
    "The second thing I realise is that the body and face belong to Sasha, but there's something bugging me about what I see."
    show sasha at center, zoomAt (1.0, (740, 720)) with ease
    "Luckily for me, my TV-addled brain is stirring rapidly from its former sluggishness."
    show sasha at center, traveling(1.25, 0.3, (640, 880))
    "This means I can make a vague connection between the fact that something's different about Sasha's appearance and the fact that she's almost demanding that I look her up and down."
    "My astute deduction, therefore, is that she's changed something, and now she wants a suitably genuine and spontaneous-sounding compliment on whatever that change is."
    show sasha shout
    sasha.say "Well, what do you think?"
    show sasha normal
    "I make as quick of an appraisal of her as I can manage, searching for the elusive change."
    "Her face and make-up look no different from the usual, no help there."
    "Clothes are the same band T-shirt and shorts, another blank."
    show sasha annoyed
    "Sasha looks increasingly impatient as I struggle to locate whatever it is I should instantly have noticed."
    "What else is there to see?"
    "What else can girl chance on a whim?"
    "Hair, that's it!"
    "Now that I'm actually fully awake and paying attention, I can see that it should have been obvious."
    "Sasha's hair is no longer its characteristic black, but instead a shockingly platinum blonde instead."
    "All that remains of the former colour is a hint of darkness around the roots."
    mike.say "Wow...that's really quite a...quite a change!"
    show sasha upset
    "Sasha instantly looks frustrated at the bland and noncommittal nature of my comment."
    show sasha vangry
    sasha.say "Really, [hero.name]?"
    sasha.say "Is that all you can summon up to say?"
    sasha.say "I was hoping for a 'fucking hell' or something like that, at the very least!"
    show sasha upset
    mike.say "Sorry...it's just a bit of a surprise, that's all."
    show sasha shout
    sasha.say "Well?"
    show sasha sadsmile
    mike.say "Well what?"
    show sasha shout
    sasha.say "Well now that you've had a chance to let this crazy news sink in - do you like it or not?"
    show sasha sadsmile
    menu:
        "I don't like it":
            mike.say "Erm...well...not really."
            $ sasha.love -= 10
            show sasha surprised at center, zoomAt(1.0, (640, 880)), vshake
            sasha.say "WHAT?!?"
            show sasha stuned
            mike.say "Ah...I'm going to guess that wasn't exactly what you wanted to hear...and that it's too late to change my answer."
            show sasha upset
            "Sasha puts her hands to her forehead in a gesture of frustration, then runs her fingers through her hair."
            "This only seems to make things worse, as she glances down to see the now blonde locks between her fingers."
            show sasha whining
            sasha.say "But the other night, when we were getting takeout with [bree.name] - you told me that you preferred blondes!"
            show sasha upset
            "Oh dear - it seems Sasha read far too much into a comment I made in the hope of covering the fact I was actually staring at [bree.name]'s ass."
            mike.say "Yeah, Sasha - I remember what I said at the time."
            mike.say "But I never actually said that you should go out and do something this drastic just to please me either!"
            show sasha annoyed
            "Sasha's anger seems to be simmering down into irritated resentment, as she mulls over this important fact."
            show sasha whining
            sasha.say "I...I just thought that you'd like it...that it'd make me more your type."
            show sasha sadsmile
            mike.say "Sasha, it doesn't work like that - not with me, anyway."
            mike.say "Just because I like blondes doesn't mean that I can't be with you if you've got black hair."
            mike.say "Hell, Sasha - I love cheeseburgers, but I don't want to eat them at every meal."
            show sasha annoyed
            "Sasha looks at me sideways, trying to make sense of my last comment."
            mike.say "Maybe that's a bad metaphor...but what I'm trying to say is that I don't need you to change in order to keep me interested in you."
            show sasha whining
            sasha.say "You might have been more specific about that."
            show sasha angry
            sasha.say "Jesus...this shit is going to take months to grow out!"
            show sasha stuned
            "A sudden flash of inspiration crosses Sasha's face."
            show sasha shout
            sasha.say "Unless I shave my head and start from scratch!"
            sasha.say "[hero.name], what do you think about girls with shaven heads?"
            show sasha normal
            "Her tone and expression are so sincere that I must look genuinely shocked at the question."
            show sasha happy
            sasha.say "Joking!"
            show sasha joke
            sasha.say "Don't worry, I'll just have to grow it out, I guess."
            show sasha normal
            $ game.flags.LikesBlondes = False
            $ game.flags.LikesBlondesDelay = TemporaryFlag(True, 7)
        "I love it":
            $ sasha.love += 5
            mike.say "I like it, Sasha...I like it a lot!"
            show sasha happy
            "Sasha doesn't say a word, but her face shows a genuine delight which makes the impact all the more impressive."
            mike.say "I think I didn't notice it at first because it looks so good."
            mike.say "Maybe this is how I always pictured you, and it took me a second to realise I wasn't imagining it?"
            "Cheesy line, I know."
            "But in my experience, girls don't really pick up on that kind of thing when they want to be flattered and you're obliging them."
            show sasha blush
            sasha.say "You really think so?"
            show sasha shy
            "Sasha's blushing now, drinking in the compliments eagerly."
            "I nod, and not out of a desire to simply make her feel good about herself and validate her decision."
            "I've always found dyed hair a big turn-on, and what with the black still showing at the roots, Sasha's platinum blonde locks are really doing it for me."
            "The combination of the two makes her normally dark look feel instantly more edgy and trashy somehow."
            "All I can think about is getting up to the kind of kinky shit that I already know Sasha likes in the bedroom."
            "But now I keep imagining those dirty blonde locks hanging over me or grabbing them firmly in one hand."
            show sasha shout
            sasha.say "I really wasn't sure if I should risk it."
            sasha.say "But after you complimented [bree.name] on her hair, I thought you'd like it if I were blonde too."
            show sasha normal
            if sasha.sexperience:
                "I have to call that a win - trying to cover up checking out another girl's backside and ending up with the one I'm fucking making changes I love thanks to my lame excuse at the time!"
            else:
                "I have to call that a win - trying to cover up checking out one girl's backside and ending up with another making changes I love thanks to my lame excuse at the time!"
            mike.say "You were right!"
            mike.say "But yours is better, much better."
            show sasha shout
            sasha.say "How so?"
            show sasha normal
            mike.say "[bree.name]'s is natural, so I guess it looks all sweet and innocent on her."
            mike.say "Yours is more down and dirty, you know?"
            show sasha joke
            "I know Sasha's kinks pretty well, and I'm not surprised that being described in such terms elicits a sly smile."
            mike.say "I suppose I'm trying to say it's more punk rock than pop - more Joan Jett than Joan Rivers."
            mike.say "Does...does it make you feel different?"
            mike.say "Does it make you feel more dirty, Sasha?"
            show sasha blush
            sasha.say "I don't know...but maybe there's a way we could find out?"
            show sasha shy
    hide sasha with easeoutright
    "Seemingly satisfied with what I've said on the subject, Sasha walks out of the room and leaves me alone once more."
    "I'm left reflecting that, though you can never see either coming, there are definitely good and bad surprises to be had in life."
    "But I'm still not entirely sure which kind just popped up in my own."
    return

label sasha_likes_blondes_3:
    $ sasha.flags.haircut = False
    return

label sasha_breast_complex_1:
    "I barely make it to the sofa before I collapse and let out a groan of utter exhaustion."
    "I'm so tired that I can't even be bothered to turn on the TV, so I just grab the first thing within reach to read."
    "It's a glossy women's lifestyle magazine, the kind of thing that Sam used to leave scattered around the house all the time."
    "Not ideal reading material, but there's usually at least one article or photoshoot that classes as VERY softcore titillation."
    "That could be just what I need right now, as anything more stimulating might render me unconscious with a mere glance."
    "I've been flicking through the pages for what feels like a couple of minutes before I get the feeling of being watched."
    show sasha at center, zoomAt(1.0, (1140, 720)) with dissolve
    "Glancing up blearily, I see Sasha, leaning in the doorway and grinning evilly in my direction."
    show sasha joke
    sasha.say "Getting in touch with your feminine side, eh?"
    show sasha normal
    "I take a while to answer, as in addition to being worn out, I'm also too busy checking Sasha out too."
    if sasha.get_clothes() == "sleep":
        "She's clearly winding down for bed, wearing nothing save for a pair of tight shorts and a cut-off band T-shirt."
        "Even without make-up, her mocking features are filled with wicked allure."
    mike.say "Huh?"
    mike.say "Oh...this?"
    "I hold up the magazine, trying to sound nonchalant."
    mike.say "Nah, it's just Sam's, she must have forgotten it...I was looking at the pictures, that's all."
    show sasha shout
    sasha.say "Why, you too much of a pussy to look at actual porn?"
    show sasha normal
    mike.say "No...it's just that there are actually some interesting and informative articles in here."
    "Sasha raises her eyebrows in questioning amusement."
    mike.say "Really, there are...like this one here 'Is Your Undersized Bra Causing You Harm?'"
    "Sasha keeps on staring at me, evidently enjoying watching me squirm and dig myself into a hole."
    mike.say "Well...not that the last one would be of interest to you..."
    show sasha wtf at center, zoomAt(1.25, (940, 880)), vshake
    $ sasha.love -= 5
    sasha.say "WHAT THE HELL?!?"
    mike.say "Erm...I'm sorry?"
    show sasha angry
    sasha.say "What in the hell is that supposed to mean?!?"
    show sasha upset
    "For a moment I'm wrong-footed and lost for words."
    "I genuinely can't fathom what I've said to take Sasha from zero to fuming in so short of a time."
    "But then I glimpse her hands going instinctively towards her breasts, as if she's trying to cover them up or hide them from sight."
    "Suddenly it all makes sense, and I realise that Sasha's secretly quite insecure about her breast size."
    "And I just went and made a comment that could be taken as meaning I think hers are too small to ever have an undersized bra."
    "Hooray for me."
    mike.say "Sasha I'm..."
    show sasha vangry
    sasha.say "Ah, shut up - just keep on wanking over women with fake tits as full of air as your big, dumb head and leave me out of it!"
    hide sasha with easeoutright
    "With that, she storms out of the room and I can hear her stomping footsteps all the way to her room."
    play sound door_slam
    "When the sound of the door slamming reaches my ear, I'm left alone with the magazine still clutched in my hand."
    "I wonder if I just put my foot in it because I'm dead tired."
    "Or if I could have been so blundering and insensitive after a good night's rest."
    "Either way, I just discovered one of Sasha's flashpoints in perhaps the worst way imaginable."
    return

label sasha_breast_complex_2:
    "Seeing as how it was the weekend and the weather was fine, the pool was the natural place I found myself relaxing."
    "But it took me a full twenty minutes to sit up and realise what was actually happening when [bree.name] announced that she was doing the same."
    "I felt like one of those guys living the fantasies I'd dreamed up as a pathetic teenager."
    show bree a at left with easeinleft
    "I try to stay relaxed and unmoved when [bree.name] strolls out in a white swimsuit and begins to tentatively dip her toes in the water."
    "I feel that she's basically doing the same thing."
    show bree b happy at center with ease
    "But it's like she's just too naturally hot to be able to keep from making whatever she does seductive and arousing."
    play sound water_splash
    pause 0.2
    hide bree a with moveoutbottom
    if sasha.get_clothes() != "swimsuit":
        show sasha casual shout at top_mostleft with dissolve
    else:
        show sasha shout at top_mostleft with dissolve
    sasha.say "Hey, [hero.name] - you want some company out here..."
    show sasha normal
    "I look up guiltily to see Sasha standing by my lounger, clearly thinking of joining me."
    "Or at least she was, until she realised that I was just getting a load of [bree.name] in her swimsuit, sporting in the pool."
    mike.say "Sure, Sasha...erm, it looks like [bree.name]'s staying in the water, so I could use someone to talk to."
    "My line sounds lame, mainly because it is."
    show sasha shout
    if game.hour < 12:
        sasha.say "Now you come to mention it, the water does look really good this morning."
    elif game.hour < 18:
        sasha.say "Now you come to mention it, the water does look really good this afternoon."
    else:
        sasha.say "Now you come to mention it, the water does look really good this evening."
    if sasha.get_clothes() != "swimsuit":
        sasha.say "Don't go anywhere, I'll be right back."
        hide sasha with easeoutleft
        "I sit there feeling more than a little puzzled, but another glance at [bree.name] soon cures me of that."
        scene bg pool at dark
        show bree b happy at center, zoomAt(2, (740, 1250)), rotation(30)
        with dissolve
        "She's doing a backstroke, and I can't help being hypnotised by her motions in the water."
        "Her glistening blonde locks and the way her swimsuit clings to her breasts make me think what she'd look like as a mermaid."
        scene bg pool with dissolve
        "But before I can imagine [bree.name] wearing nothing save for clamshells and a tail, another sight to distract me Sasha comes into view."
        show sasha swimsuit at top_mostleft with easeinleft
        "Sasha must have hastily changed and come back to the side of the pool."
        if not sasha.flags.sexyswimsuit:
            "As she's now wearing nothing save for a black bikini."
        else:
            "As she's now wearing nothing save for a red bikini."
    show sasha swimsuit normal at left with ease
    "She seems to take one quick glance over her shoulder, almost as if checking that I'm watching."
    play sound water_splash
    pause 0.2
    hide sasha a with moveoutbottom
    "And then she slips off into the water."
    scene bg pool at dark
    show sasha swimsuit happy at center, zoomAt(2, (540, 1250)), rotation(-30)
    with dissolve
    pause 1
    hide sasha
    show bree b happy at center, zoomAt(2, (740, 1250)), rotation(30)
    with dissolve
    "Watching both girls swim, I could almost believe [bree.name] having a halo and feathery wings, and Sasha sprouting horns and bat wings herself."
    "The pair of them are so different, and yet both so sexy in their own way, it's hard to choose which one to watch at any given moment."
    hide bree
    show sasha swimsuit happy at center, zoomAt(2, (540, 1250)), rotation(-30)
    with dissolve
    "Eventually Sasha emerges from the pool and comes to lie on the lounger next to mine."
    "She reclines for a while without saying a word, simply enjoying the sensation of the sun upon her skin."
    "While she's silent, I suddenly know which one of them that I want to watch."
    if not sasha.flags.haircut:
        "I can't take my eyes of the pale skin of Sasha's body and how it contrasts so strikingly with her jet-black hair."
    "Her breasts are more petite than [bree.name]'s, for sure."
    "But that only means that they stand more erect and proud on her chest, nipples stiff beneath her bikini top."
    "I start to think what it would be like to caress Sasha's little round breasts, to have one in each hand."
    "I realise that I could cover them, hold them entirely, as if my hands were some kind of living bra..."
    scene bg pool
    show sasha swimsuit happy at center, zoomAt(1.25, (640, 880))
    with dissolve
    sasha.say "[hero.name]...be honest with me, okay?"
    "Sasha keeps her eyes closed as she speaks, but her words don't instantly put me at ease."
    sasha.say "Does [bree.name] look good in that swimsuit she's wearing?"
    "Oh great, one attractive woman asking me in a roundabout way if I think another attractive woman is at all attractive."
    "No hidden traps or pitfalls there then!"
    mike.say "It looks good, I guess...on her."
    show sasha shout
    sasha.say "What does that mean?"
    show sasha normal
    mike.say "I suppose it means that I think she's got the figure to pull it off."
    show sasha shout
    sasha.say "Do I have the figure to pull it off?"
    show sasha normal
    "Careful now!"
    mike.say "I don't know about that...but she definitely couldn't pull it off the other way round."
    show sasha shout
    sasha.say "How so?"
    show sasha normal
    mike.say "Well, don't think I'm being mean, but I think there are times when you need ripe peaches, rather than over-sized melons."
    show sasha surprised
    "Sasha opens her eyes wide at the same moment she opens her mouth in what I take as a scandalised and yet still very much amused grin."
    show sasha normal at center, traveling(1.5, 0.5, (640, 1040))
    "I must have said something right, because Sasha's body-language becomes more open and she leans visibly towards me."
    "I should say more, but the fact her rapidly-drying breasts are coming closer makes me clam up and simply stare at them some more."
    hide sasha
    return

label sasha_breast_complex_3:
    "I push the door to the bathroom open and walk in while still feeling half asleep, and then jump at the sound of someone telling me off."
    show sasha naked angry
    with vpunch
    sasha.say "HEY - did you never hear of actually fucking knocking on a door?"
    show sasha upset
    mike.say "What...huh...oh, sorry...I guess I should have knocked, you're right."
    show sasha naked annoyed
    "Seeing that it's me and not [bree.name] that barged in on her, Sasha's expression softens a little and she stops reaching desperately for a towel."
    "It's kind of weird to be so prudish about being nude around someone that's gotten up to what we have, after all."
    "Even though I'm still not awake and I just got a little chewed out for my trouble, I still can't help looking Sasha up and down admiringly."
    "She's fresh out of the shower, hair hanging in wet tresses and skin pink from the warmth of the water."
    "Though she has her back to me, I can tell she's watching me in the mirror above the sink."
    show sasha naked normal
    "And her expression isn't long in softening as she realises that she's being admired."
    "I catch her smile in the mirror and she shakes her head at my interest."
    show sasha at left4 with ease
    "A moment later she hops around, leans forward and waggles her petite breasts at me."
    show sasha at right4 with ease
    "Then she hops back the other way, adding a last wriggle of her buttocks just to tease me."
    show sasha joke at center with ease
    sasha.say "That's all you're getting right now - I have plans for this morning, and they don't involve your dirty imagination!"
    show sasha shy
    "Smiling at the little show for my sole benefit, I nod in agreement and go back to eyeing up her buttocks."
    show sasha normal
    "Sasha pauses in the middle of brushing her teeth, the brush still in her mouth as she speaks."
    show sasha shout
    sasha.say "Not meaning to be weird, but why do your eyes always seem to be drawn specifically to my ass?"
    show sasha normal
    mike.say "Erm...because I'm a guy, and you have a great ass?"
    show sasha shout
    sasha.say "No, really - you can take it all in, but you always end up looking at my ass."
    show sasha normal
    "I don't really have an answer for that."
    "I haven't spent much time analysing my hierarchy of preferences when it comes to admiring Sasha's body."
    "I suppose that I'm too busy actually doing it to care very much."
    show sasha whining
    sasha.say "I guess what I mean is...don't you like my breasts?"
    show sasha sadsmile
    "The question seems so odd that I can't answer it either."
    show sasha whining
    sasha.say "I know most guys are supposed to like bigger ones, but I thought maybe you liked mine...even though they're pretty small?"
    show sasha sadsmile
    menu:
        "I like them small":
            mike.say "Sasha, your breasts are fucking amazing...they make me want to touch them whenever I set eyes on them."
            show sasha surprised
            sasha.say "Really?"
            show sasha whining
            sasha.say "You never said so!"
            show sasha normal
            mike.say "Sasha, this is the twenty-first century, you know?!?"
            mike.say "Most guys think saying something like that'll get them strung up, never mind dumped!"
            show sasha shout
            sasha.say "Most guys are idiots."
            show sasha normal
            mike.say "Okay, for the sake of not being one of them, and for the record."
            mike.say "Sasha, I hereby state that I not only love your breasts, I also cherish, worship and adore them."
            mike.say "I love the fact that I can fit them into the palms of my hands."
            mike.say "I love the way they stand up and beg for attention."
            mike.say "And I love the way they bounce when you're on top of me."
            $ sasha.love += 1
            show sasha embarrassed
            "Sasha screws up her face at the gushing praise I'm heaping upon her chest."
            show sasha blush
            sasha.say "Geez, lighten up there, Mr Shakespeare!"
            show sasha shy
            "She shakes her head to underline how she thinks I'm being over the top."
            show sasha a towel happy -naked with dissolve
            "But as she wraps herself in a towel and walks out, she has a glint in her eye and a twitch of a smile."
            "That makes me think she's not totally embarrassed by my proclamations."
        "I like them big":
            mike.say "They're great, Sasha - but..."
            show sasha whining
            sasha.say "But what?"
            show sasha sad
            mike.say "Well, don't take this the wrong way, but you wanted me to be honest, right?"
            show sasha whining
            sasha.say "Yeah...I suppose so."
            show sasha sad
            mike.say "The thing is that, while they're great, I do kinda more like larger breasts...usually."
            show sasha whining
            sasha.say "Oh...so you think mine are...too small?"
            show sasha sadsmile
            mike.say "No, no, that's not what I'm saying...well, kind of it is, but not...if you follow me?"
            show sasha whining
            sasha.say "I'm not sure that I do."
            show sasha sadsmile
            mike.say "I just like bigger ones, but yours are great too."
            show sasha naked sad
            "The look of disappointment and confusion on Sasha's face tells me that I'm in trouble here."
            "I open my mouth to go on, but she holds up a hand to cut me off."
            $ sasha.love -= 5
            $ sasha.sub += 5
            $ sasha.flags.BreastComplex = True
            $ game.flags.BreastComplexDelay = TemporaryFlag(1, 3)
            show sasha whining
            sasha.say "It's okay, I get it."
            show sasha a towel sad -naked with dissolve
            "She wraps herself up in a towel and stalks out of the bathroom without another word."
            "And I'm left thinking that I pretty much fouled that one up completely."
    hide sasha with dissolve
    "Now that I have the bathroom to myself, I can't honestly remember what I came in here for in the first place."
    "The only thing on my mind now are Sasha and her breasts."
    "But I suppose there are far worse things to be obsessed with."
    return

label sasha_breast_complex_4:
    show sasha at center, zoomAt(1.0, (640, 720))
    mike.say "What's up?"
    show sasha at center, traveling(1.5, 0.5, (640, 1040))
    "Sasha walks over and sits down next to me on the bed."
    show sasha whining
    sasha.say "Well, first of all I wanted to say sorry for being all weird and angry with you the past couple of days."
    show sasha sadsmile
    mike.say "Ah, I see...you mean about..."
    show sasha whining
    sasha.say "Yeah, yeah...about my breast size."
    show sasha sad
    mike.say "Apology accepted."
    show sasha normal
    "Sasha smiles wanly at my response, clearly pleased to know that she's back in good graces with me."
    show sasha shout
    sasha.say "I just got to thinking of how selfish and unfair I'd been about all of this, you know?"
    show sasha normal
    mike.say "I did feel a bit like you bit my head off, Sasha."
    mike.say "Especially when it was you who asked me to be honest!"
    show sasha shout
    sasha.say "I know...I'm sorry I was so unreasonable."
    show sasha annoyed
    sasha.say "I've come to realise that it's my problem, not yours."
    sasha.say "I've always been really insecure about the size of my breasts."
    show sasha shout
    sasha.say "But that's my fault, and I've been taking it out on you."
    sasha.say "I was so full of that feminist idea that my body was mine alone, that I totally forgot that you have rights too."
    show sasha normal
    "I just keep nodding, allowing her to say her piece."
    "But all the time I'm wondering where this is ultimately going."
    show sasha shout
    sasha.say "That's why I've given it some serious thought, and I've decided to have my breasts enlarged."
    show sasha normal
    "Of all the things she could have said, I wasn't expecting that."
    show sasha shout
    sasha.say "After all, I'd only be doing it to make myself more attractive to you."
    sasha.say "And if you want me more, then we both get something we want out of it."
    sasha.say "Don't we?"
    show sasha normal
    menu:
        "I'll help you pay for it" if hero.money >= 500:
            mike.say "Wow, Sasha - I'm such a lucky guy to have a girl that'd go to such lengths for me!"
            show sasha happy
            "Sasha's face positively lights up with delight at my approval."
            show sasha shout
            sasha.say "Okay - I've done some research on clinics with a good record in the city."
            sasha.say "And I think that I've come up with a way I can pay..."
            show sasha normal
            mike.say "Oh no, you're not paying for it - I am."
            $ sasha.love += 10
            $ sasha.sub += 10
            show sasha stuned
            "Sasha looks at me in genuine surprise."
            mike.say "I'm the one that wanted you to have bigger breasts, so the least I can do is pay for them."
            show sasha shy
            mike.say "Think of them as a gift that'll keep on giving for the both of us."
            mike.say "I know I'm already thinking of how to repay you after the surgery's over!"
            $ game.flags.BreastComplexDelay = TemporaryFlag(1, 7)
            $ sasha.hide()
            $ hero.money -= 500
        "That's a great idea":
            mike.say "We sure do!"
            mike.say "I can almost imagine them already!"
            "I cup Sasha's petite breasts in my hands without asking for permission, massaging them as I think of them massively increased in size."
            show sasha shout
            sasha.say "So you're okay with me getting it done?"
            show sasha shy
            "Sasha's cheeks have flushed as I continue to play with her nipples."
            "I can hear a question in her tone, but I'm more interested in pinching her now stiffening nipples than seeking it out."
            show sasha blush
            sasha.say "[hero.name]...it's just that...ah...I was...ah...wondering if you could...help me out...with the cost?"
            show sasha embarrassed
            mike.say "Woah, Sasha - that's pretty manipulative of you, don't you think?"
            $ sasha.love -= 10
            $ sasha.sub -= 10
            show sasha surprised
            sasha.say "Huh?"
            show sasha stuned
            mike.say "I mean - you come in here, all apologetic and demure to start with."
            mike.say "Then you tease me with your boobs and try to milk me for money!"
            show sasha surprised
            sasha.say "I...no...that's not it!"
            show sasha stuned
            mike.say "The least you could do is pony up the cash yourself."
            mike.say "That'd show me you were REALLY sorry."
            show sasha whining
            sasha.say "Uh..well...I guess so."
            $ game.flags.BreastComplexDelay = TemporaryFlag(1, 7)
            $ sasha.hide()
        "You should not do it":
            mike.say "You're serious?"
            show sasha shout
            sasha.say "Of course I am!"
            show sasha normal
            mike.say "Look, Sasha - I've been thinking too, and I don't really want you to have the surgery."
            show sasha stuned
            "Sasha's expression shows surprise at my confession, but also not a little relief too."
            show sasha surprised
            sasha.say "But...but I thought you said you liked bigger breasts than mine?"
            show sasha sadsmile
            mike.say "What I meant was that I like bigger breasts on girls with bigger breasts."
            mike.say "And I like your breasts on you!"
            show sasha shout
            sasha.say "Really?"
            show sasha normal
            mike.say "Yes...how could an over-sized pair of dumplings stand to attention like yours are right now?"
            show sasha happy at startle
            "Sasha giggles and instinctively covers her breasts with her hands."
            "But I can see that she's flattered and more than a little aroused by the praise I've just heaped on her petite chest."
            $ sasha.flags.BreastComplex = False
    show sasha normal
    "Once we're done talking about the subject, I feel much better, like the air has finally been cleared between us."
    "Sasha plants a kiss on my lips and scurries away to her own room, not saying another word."
    "Little by little, I think we're coming to understand each other so much better than before."
    return

label sasha_breast_complex_5:
    scene bg livingroom
    $ sasha.unhide()
    $ sasha.flags.boobjob = True
    $ today = game.calendar.day_of_week_name.capitalize()
    show sasha casual shout at center, zoomAt(1.25, (640, 880))
    if sasha.is_sex_slave:
        sasha.say "Hello, [hero.name]...I'm back."
    else:
        sasha.say "Hi."
    sasha.say "I hope that you're pleased to see me..."
    show sasha normal
    "Of course, today is [today], more than a week since Sasha left for the appointment at the clinic."
    "Specifically the appointment for her breast augmentation surgery."



    if sasha.is_sex_slave:
        "If she weren't so happily subservient to my will, I'd say she was trying to tease me."
        "But as it is, I think she's far more likely presenting me with an opportunity to exercise my control over her."
        mike.say "I'm definitely pleased to have a piece of my property back."
        mike.say "It means I have the chance to inspect the work that I've had done to it."
        "Sasha's pale cheeks colour a little at my speaking of her in such abstract terms."
    "I'm fully aware of just how intrusive, potentially painful and life-changing the enlargement of her breasts must have been."
    if sasha.is_sex_slave:
        "But I also know how arousing she finds my treating her like an object."
        "And the two in combination must be almost impossible to keep from turning her on to a great degree."
        "I make a vague gesture for Sasha to come and stand before me, winding an index finger in a circle at the same time."
        "She nods and, not needing to be told any more, walks obediently forwards until she stands perhaps two feet in front of me."
    else:
        "Sasha walks towards me."
    mike.say "Well, what are you waiting for?"
    mike.say "Strip."
    if sasha.is_sex_slave:
        "Sasha nods curtly, clearly enjoying being given orders by me once more."
    show sasha naked with dissolve
    "She slowly peels off her clothes, easing it down over her arms."






    "As she raises her arms to drag it over her head, I'm treated to a truly magnificent view."
    "First they rise in sympathy with her arms and shoulders, spreading out and then jiggling with the jerking of her muscles."
    "And then they descend in the same manner, settling onto her chest as gravity returns them to their normal position."
    "Sasha proceeds to then caress them, weighing them in the palms of her hands and even gently squeezing their heavy, fleshy masses."
    "If I'd been expecting the operation to leave Sasha with the god-awful kind of implants that make breasts look like soccer balls stuffed under the skin, I was dead wrong."
    "Clearly she'd been very wise when it came to choosing the clinic, as while they were clearly out of proportion to her petite figure, they still looked natural and very alluring."
    show sasha blush
    if sasha.is_sex_slave:
        sasha.say "Well, [hero.name]...will I do?"
        show sasha shy
        "I gave a grin that was almost a leer, and pointed to the floor right before me."
        mike.say "They look the part, but I want to take them for a test-drive, before I sign off on them."
        "Sasha again nods in obedience and kneels on the floor in front of me."
    else:
        sasha.say "Do you like them?"
        show sasha shy
        mike.say "I do."
        show sasha joke
        sasha.say "I am pretty sure you'll like them even more in a few minutes."
        show sasha shy
    show sasha at center, traveling(1.5, 0.5, (640, 1040))
    "She shuffles forwards on her knees, making her newly enlarged breasts sway back and forth as she comes."
    "I don't see where she produces the lube from, but nevertheless, it appears in her hands."
    "Sasha makes a great show of slowly rubbing the transparent liquid onto her breasts."
    "She once more massages and caresses them as she does so, spreading the lube between them and then over their entire mass."
    "Sasha pinches her enlarged nipples as she sweeps her hands over them, the darkened skin puckering as they become suddenly erect."
    "There's little to do for my sake once she opens my flies and reaches in to pull out my dick."
    scene bg black
    show sasha tittyfuck livingroom
    with fade
    "Placing the tip just beneath her now slick breasts, Sasha moves downwards so that it travels straight up and between them."
    "She makes perhaps a half-dozen more such passes, and then suddenly presses them together so that my dick is caught in the middle."
    "The unexpected pressure makes me gasp audibly as the head emerges, from the cleft."
    show chest_insert sasha zorder 1 at zoomAt(1, (40, 160))
    "Sasha's breasts are baffling mixture of softness and substance, both cushioning and squeezing at the same time."
    "She works me in that same way now, keeping the pressure up as she slides my dick between her breasts."
    "The way that her hands cause them to push together and then return to their resting shape is almost hypnotic to watch."
    "Sasha's new chest seems to almost possess a life of its own as she uses it to tease me and caress me all at the same time."
    show sasha tittyfuck mouthopen
    "All the while, Sasha pants and moans, as if the feeling of my dick is arousing her in the same manner as her breasts are me."
    if sasha.is_sex_slave:
        if sasha.flags.mikeNickname:
            sasha.say "Uh...uh, [hero.name]...please...may I..."
            mike.say "Speak up!"
        sasha.say "[hero.name]...please...may I...touch myself?"
        "I nod, trying not to look too turned on by her desperate desire to masturbate right in front of me."
    $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_low.ogg", loop=True)
    "Sasha wraps her breasts with one arm to keep them around my dick, while her free hand almost darts for her denim shorts."
    "I might not be able to see what she's doing, but soon I can feel the results."
    "Sasha's pants and moans become all the more pronounced, and she begins to move in time with her ministrations to herself."
    "The rhythm this creates is immediate and intense, as she's effectively stimulating herself and then me in turn as she moves in sympathy."
    show chest_insert sasha zorder 1 at zoomAt(1, (40, 360))
    show mouth_insert sasha zorder 2 at zoomAt(1, (40, 100))
    with dissolve
    "Sasha's lips are now puckering and parting, her tongue curling with the increasing pleasure she's feeling."
    "She's in serious danger of finishing me off any moment, but now I can't take my eyes of the appealing sight of her open, gasping lips."
    mike.say "Sasha, take me in your mouth...now."
    if sasha.flags.mikeNickname:
        sasha.say "Uhh...yes, yes...[hero.name]!"
    else:
        sasha.say "Yes [hero.name]!"
    $ renpy.sound.play("sd/moans/sasha/sasha_blowjob_low.ogg", loop=True)
    show sasha tittyfuck blow
    "Hurrying to obey, she wastes no time with kissing or caressing the head of my dick."
    "Instead she simply wraps her lips around it and eagerly swallows as much as she can without either gagging or choking."
    "Still with her own fingers inside of herself, Sasha sucks away at the same intensifying rhythm."
    "I could swear I can feel the very emanations spreading out from her pussy and through her entire body."
    stop sound
    show sasha tittyfuck blow cum
    show mouth_insert sasha cum
    with vpunch
    $ renpy.sound.play("sd/moans/sasha/sasha_blowjob_swallow.ogg", loop=True)
    pause 0.25
    with vpunch
    pause 0.25
    with vpunch
    "I cum mere seconds later, and Sasha struggles to take it all, keeping it in her mouth and not following her instinct to swallow."
    "A wave of my hand lets her know that she can release me, and she does so, keeping her eyes on me at the same time."
    stop sound
    if sasha.is_sex_slave:
        show sasha tittyfuck normal facecum eyesclosed -cum
        mike.say "Open wide - let me see it."
        "Sasha obliges me by opening her mouth wide, letting me see the cum still upon her tongue."
        mike.say "Very good...you may swallow it now."
        "She nods demurely as she complies."
        show mouth_insert sasha -cum
        sasha.say "Thank you, [hero.name]."
    hide chest_insert
    hide mouth_insert
    scene bg livingroom with fade
    "I pat the sofa beside me, and Sasha crawls up to curl herself beside me, almost like an oversized house-cat."
    "She makes no effort to cover up her breasts, still soaked in a mixture of sweat and lube."
    "I amuse myself by idly playing with her stiff nipples and listening to the soft moans this arouses from her."
    "Neither of us speaks, but I'm already thinking of the new possibilities where my submissive pet's new assets are concerned."
    return

label sasha_event_coffee:
    scene bg coffeeshop
    show sasha shout at center, zoomAt(1.5, (640, 1140))
    with fade
    sasha.say "Gee, [hero.name] thanks for suggesting we go here! It looks like a great place, and the coffee's real good, too!"
    show sasha normal
    menu:
        "It's not that good":
            mike.say "Nah, it's not that good."
            $ sasha.love -= 1
            "Sasha smiles weakly, and takes another sip of her coffee."
            show sasha shout
            sasha.say "Well, okay, if you say so."
        "You should have some of the pastries too" if sasha.sub > 25:
            mike.say "Very good, you should have some of the pastries too, you will like them."
            show sasha shy
            $ sasha.sub += 5
            "Sasha smiles and ducks her head, meeting my eyes for a moment, then looking down with a little smile."
            show sasha blush
            sasha.say "Okay, I will, thank you."
        "I'm happy that it pleases you" if sasha.sub < -25:
            mike.say "I'm so happy that it pleases you."
            $ sasha.sub -= 5
            "Sasha takes another sip of her coffee, looking at me from under her eyebrows with a knowing look and a little satisfied smile, pleased with my response."
            show sasha shout
            sasha.say "Very good, I'm glad to hear that!"
        "I'm glad you like it" if -25 <= sasha.sub <= 25:
            mike.say "Good, I'm glad you like it."
            $ sasha.love += 1
            "I meet Sasha's eye and smile as I say it; she meets my gaze with a smile of her own, then takes another sip of her coffee."
    show sasha shout
    sasha.say "So, [hero.name] do you come here often?"
    show sasha normal
    mike.say "Well, maybe not as often as I would like to."
    show sasha shout
    sasha.say "Oh? What does that mean?"
    show sasha normal
    mike.say "Well, I don't have many people I can take here, so I haven't had a good reason to come here."
    show sasha happy at startle
    "Sasha laughs, and I watch her hair play as she tosses her head back. It makes me smile."
    show sasha shout
    sasha.say "Hey, maybe I could be your reason to come here."
    show sasha normal
    menu:
        "We will come here again" if sasha.sub >= 25:
            "I fix her with a commanding eye and smile."
            show sasha shy
            $ sasha.sub += 5
            mike.say "You and I will come here again very soon."
            show sasha happy at startle
            "Sasha giggles, her eyes alight."
            show sasha blush
            sasha.say "Yes."
        "I would love to do that" if sasha.sub <= -25:
            "I smile and nod my head."
            mike.say "I would love to do that; anything you want."
            $ sasha.sub -= 5
            "Sasha looks at me with, her hands clasped on the table before her, and she smiles, her eyes piercing into mine."
        "I don't have time for that":
            mike.say "Actually... I don't know that I have time for that, really. Sorry."
            show sasha sadsmile
            $ sasha.love -= 5
            "I shrug helplessly, not knowing what else I can say. Sasha stares at me in silence for a moment, and then she shrugs in return."
        "Is that a come-on?" if -25 <= sasha.sub <= 25:
            mike.say "Is that a come-on?"
            $ sasha.love += 1
            "I raise an eyebrow, giving Sasha a surprised smile. She grins back at me."
            show sasha shout
            sasha.say "What do you think?"
    hide sasha
    return

label sasha_sub_event_1:
    $ renpy.dynamic(
        sasha_strap=False,
        sasha_beads=False,
        sasha_ropes=False,
        sasha_cunni = False,
        sasha_ballgag = False,
        sasha_naked = False,
    )
    $ sasha.status = "sex slave"
    $ sasha.flags.mikeNickname = "Master"
    scene bg kitchen
    show sasha at center, zoomAt(1.5, (640, 1040))
    "I take a long step closer to Sasha, then I reach out and put my hand on her arm, leaning close, I lower my face to hers-"
    show sasha shout
    sasha.say "Wait."
    show sasha normal
    "She raises her hand, pressing a finger to my lips."
    show sasha shout
    sasha.say "What is it you want, exactly?"
    show sasha normal
    "I smile down at her, my eyes staring into hers."
    mike.say "I want you."
    "I can feel my heart pounding in my chest as I tighten my grip on her, not to let her escape."
    mike.say "I want to have you, to hold you, to take you and pleasure you and use you, and make you happy."
    show sasha happy
    sasha.say "Why- that's-"
    hide sasha
    show sasha kiss
    with fade
    $ sasha.flags.kiss += 1
    "I cut off her words with a kiss, holding her against me, I press my lips to hers in a hot fiery passion, lips and tongue working at her- she freezes, then melts against me."
    "Going from cold to hot in my arms, her breasts pressed against me, her lips and tongue working at mine."
    "She moans as I run my hands over her, brushing her breasts, her hips and ass, caressing her hot body, pinching and squeezing her in all the right places."
    "We break apart, and I look down into her face. Then she opens her eyes to meet mine."
    hide sasha kiss
    show sasha blush at center, zoomAt(1.5, (640, 1040))
    with fade
    sasha.say "So what do you want from me?"
    show sasha shy
    "I smile, knowing that she is now mine."
    mike.say "I want you to kneel for me, Sasha."
    "I lay my hand on her chin and raise her head to look up at me; she stares almost worshipfully at me, waiting patiently, submissively, for whatever I choose."
    mike.say "You are mine, now, Sasha. My slave, my servant. I claim you."
    mike.say "Your body is mine, your soul is mine; I will use you and toy with you and tease you and pleasure you."
    show sasha blush
    sasha.say "These are yours. . . [hero.name]. I give them to you, I surrender to you. Take me!"
    show sasha shy
    "Like she needs to make it more clear to me, Sasha takes hold of my hand."
    hide sasha
    show sasha thumb out
    "She balls my fingers into a fist, but leaves my thumb sticking up."
    "And then she takes it into her mouth, sucking on it in the most suggestive way she can manage."
    show sasha thumb in
    "All the time she has her gaze fixed on me, eye to eye."
    "And I can picture what's going to come next!"
    "I reach down and grab her breasts, squeezing and kneading them, - Sasha moans as my fingers sink into her soft flesh, her face growing red, her breath coming faster while her nipples grow hard."
    "I lean down further and kiss her again as I slip a hand lowers, down into her panties."
    "She moans as I caress her, running my fingers over her tight little pussy; she trembles as I take her in my arms and raise her up, then turn toward the bedroom, carrying her away."
    hide sasha
    scene bg bedroom1 with fade
    call sasha_fuck_date_choices_male (from_event="sasha_sub_event_1") from _call_sasha_fuck_date_choices_male
    scene bg bedroom1
    show sasha naked
    if _return == "leave_without_gain":
        $ hero.cancel_event()
        return
    $ sasha.sexperience += 1
    if sasha.lesbian > MIN_LES_GIRL_SEX:
        $ sasha.lesbian -= 1
    if _return == "leave_with_gain":
        $ hero.cancel_event()
        return
    hide sasha
    call sasha_sleep_date_fuck from _call_sasha_sleep_date_fuck
    return

label sasha_kiss_me:
    call sasha_greet from _call_sasha_greet_5
    show sasha
    "Sasha's spontaneous and full of life, that's one of the things that I most love about her."
    show sasha at center, zoomAt(1.5, (640, 1040))
    "So when she beckons me closer, looking like she wants to confide with me on some secret, I don't hesitate."
    hide sasha
    show sasha kiss
    with fade
    $ sasha.flags.kiss += 1
    "But then she plants her lips on mine, and I suddenly understand what the secret was."
    "The kiss is intense and all the more enjoyable thanks to my not knowing that it was coming."
    "I return the kiss without pause or hesitation, not needing to have it explained to me."
    "Words couldn't hope to explain how I'm feeling right now anyway."
    $ hero.fun += 1
    hide sasha kiss
    return

label sasha_preg_talk:
    if "Harem.together('bree', 'sasha', name='home')" and bree.flags.pregtest and bree.room == sasha.room:
        call home_harem_preg_talk from _call_home_harem_preg_talk_1
    else:
        show sasha shout
        sasha.say "I kinda have something I need to tell you."
        show sasha sadsmile
        "I give her the same raised eyebrows, not letting on that I've already seen this coming."
        show sasha shout
        sasha.say "Well...you know how we've 'forgotten' to use protection a hell of a lot recently?"
        show sasha sadsmile
        "Even though I've been trying to play it cool, I can't keep my eyes from widening."
        mike.say "Do you mean what I think you mean?"
        show sasha shout
        sasha.say "Depends on whether or not you think I mean that I'm pregnant!"
        show sasha sadsmile
        "We both fall silent from the enormity of what Sasha just admitted."
        "But we can't stay silent forever, not with something of that magnitude hanging over the both of us."
        "Eventually, it looks as though Sasha is going to be the one to break the silence for the second time."
        if sasha.sub <= 50:
            "Sasha coughs loudly, taking control of the conversation."
            if sasha.love >= 180:
                show sasha shout
                sasha.say "We both had a hand in making this happen, so I think we both need to step up and take ownership of it as well."
                show sasha normal
                mike.say "Erm...you mean like, stepping up and being a man?"
                show sasha shout
                sasha.say "Geez, you make it sound like it's the scariest thing that you could imagine."
                show sasha normal
                mike.say "Well...it is kind of scary."
                show sasha shout
                sasha.say "How about you take it a step at a time?"
                sasha.say "Maybe try being a dad first, then step it up to a fully-fledged man at a later date, eh?"
                show sasha normal
                $ sasha.flags.toldpreg = True
            else:
                show sasha whining
                sasha.say "I can't raise a child on my own, and I can see from your face that you'd be no use to me either."
                show sasha sad
                "I open my mouth to speak, but Sasha's blunt appraisal of me means that my lips move and nothing comes out."
                show sasha whining
                sasha.say "Yeah, you see now would have been the time to speak up and prove me wrong."
                sasha.say "But all you can manage is a lousy impression of a goldfish."
                sasha.say "That's why I'm having a termination - the timing's just not right."
                mike.say "Erm...well...if you think that's what'd be best..."
                show sasha sad
                $ sasha.unpreg()
        else:







            "Sasha looks at me imploringly, clearly waiting for me to tell her what we're going to do."
            menu:
                "Let's keep the baby":
                    $ sasha.love += 10
                    mike.say "Well, I can't say that I was expecting you to say that."
                    show sasha shout
                    sasha.say "You're...you're not mad, are you?"
                    show sasha sadsmile
                    mike.say "No, I'm not mad - you'd know if I was mad."
                    show sasha shout
                    sasha.say "Okay...but what are we going to do?"
                    show sasha sadsmile
                    mike.say "We're going to keep it, that's what we're going to do."
                    show sasha shout
                    sasha.say "Really - you think that's for the best?"
                    show sasha normal
                    mike.say "I do, so just do as I say and it'll be fine - you'll see."
                    $ sasha.flags.toldpreg = True
                "Tell her to abort":
                    $ sasha.love -= 25
                    mike.say "We can't have a kid, Sasha - you know that as well as I do."
                    show sasha whining
                    sasha.say "But...but I'm pregnant, the test was positive!"
                    show sasha sad
                    mike.say "Well we'll just have to fix that then, won't we?"
                    show sasha whining
                    sasha.say "You mean...you want me to have an abortion?"
                    show sasha sad
                    mike.say "Who said anything about wanting - you're having one, and that's all there is to it!"
                    "Sasha looks down at her lap as any thoughts of doing otherwise fade from her mind."
                    show sasha whining
                    sasha.say "Okay...I suppose you know what's best."
                    show sasha sadsmile
                    $ sasha.unpreg()
                "Dump Sasha":
                    "I sigh and begin to rub my forehead with one hand, my frustration at the unexpected news clearly evident."
                    show sasha whining
                    sasha.say "What's wrong, [hero.name] - are you mad at me?"
                    show sasha sad
                    mike.say "Goddamn it, Sasha - of course I'm fucking mad at you!"
                    "Sasha flinches back at the anger evident in my voice."
                    mike.say "Jesus, how in the hell could you let this happen - how could you be so stupid?!?"
                    show sasha whining
                    sasha.say "But...but we both didn't remember to use..."
                    show sasha cry
                    mike.say "Shut up, Sasha - don't go trying to pin this one on me!"
                    mike.say "You're the one that's pregnant, and it's your problem -don't expect me to bail you out now!"
                    show sasha whining
                    sasha.say "[hero.name], what are you saying?"
                    show sasha cry
                    mike.say "Oh I think you know, but I'll spell it out for you, just to be sure - you're dumped, Sasha!"
                    $ sasha.flags.toldpreg = True
                    $ sasha.love -= 100
    return

label sasha_event_bree_shower:
    "I'm lying in bed, just scrolling through some mindless crap on my phone when I hear the first of the hushed giggles coming from outside the door."
    "Unable to tell if it's [bree.name] or Sasha that's finding something so funny that she just can't keep it in, I slide off the bed and sneak to my door and open it just enough to glance out."
    "My reward is to catch a fleeting glimpse of Sasha as she flits into the bathroom and then looks back over her shoulder."
    "She beckons with a crook of her finger to someone still unseen, and then [bree.name] appears, apparently answering the summons."
    "There are more giggles, slightly nervous in tone from [bree.name] and downright wicked from Sasha."
    "And then they disappear behind the closed bathroom door, leaving me more than a little intrigued as to just what's going on in there."
    "Now I find myself in a terrible dilemma, as I know that you could argue I have absolutely no right to see whatever the girls are up to."
    "But on the other hand, I do live in this house too, and I have a right to know if the dynamics between us are about to change in a significant manner."
    "In the end, I tell myself that we're a pretty open and honest household, sharing things like groceries and splitting the bills three ways."
    "So they'd probably be okay with me knowing what's going on in one of the communal areas of the house, right?"
    "Before my conscience has a chance to protest at the shakiness of my logic, I sneak out of my bedroom and across the hallway to the bathroom door."
    show bg secondfloor with fade
    "Crouching down and trying to keep as quiet as I can, it seems that I'm in luck, as the bathroom door isn't fully shut."
    "There's just enough of a gap for me to be able to peek inside and get a fairly good look at what [bree.name] and Sasha are up to in there."
    show bg bathroom with wiperight
    $ renpy.sound.play("sd/shower.ogg", loop=True)
    "I can hear the sound of water running in the background and see the steam fogging both the mirror on the wall and the glass of the shower cubicle."
    "But the sight of [bree.name] and Sasha stripping the last few items of clothing off of each other is more than enough to make all else seem unimportant right now."
    show shower breesasha with fade
    "Sasha seems to be taking the lead, grinning in delight as she pulls down [bree.name]'s panties."
    "[bree.name] herself looks more shy and embarrassed at what they're doing, her cheeks flushed from more than the heat rapidly building up in the bathroom."
    "A part of me can't believe what I'm actually seeing here."
    "The two incredibly hot girls that I'm sharing a house with are genuinely sneaking around to take a shower together!"
    "And what's more, I'm about to get a front row seat to watch the whole thing!"
    "Just as I'm congratulating myself on not only seeing [bree.name] and Sasha naked, but also the prospect of watching them soap each other up, everything changes in an instant."
    hide shower breesasha
    show samantha_showersex_bg
    show breesasha kiss naked at left
    with fade
    "Sasha's smile changes from wicked to something visibly more tender, and she cranes her neck forward to kiss [bree.name] gently."
    "The other girl shivers a little at first, but then begins to return the kiss with a growing measure of passion."
    "Still with their lips locked together, Sasha puts her hands on [bree.name]'s hips, walking her backwards into the falling water of the shower."
    "I feel my mouth grow suddenly dry, realising that I'm seeing something that most guys could only dream about witnessing."
    "Luckily for me, [bree.name] and Sasha are both far too engrossed in what they're doing to even think about closing the door of the shower cubicle."
    "And the steam rising as the water falls only serves to cover their naked bodies in a film of moisture that makes the whole thing that much more enjoyable to watch."
    "Their passionate kiss endures until Sasha runs her hand over [bree.name]'s body, down her belly and then between her slick thighs."
    "A moment later, [bree.name] breaks the kiss as she tilts her head back and begins to moan audibly at what Sasha's doing to her down there."
    hide sasha
    hide shower breesasha_bg
    show shower breesasha
    with fade
    "Though I can't see her fingers for [bree.name]'s thighs, it's clear to see that Sasha is engaged in the act of stroking, rubbing and probing to great effect."
    "[bree.name] sinks back against the wall as Sasha teases her more with each second that passes."
    "But then she arches her back and pushes herself away again upon her elbows."
    "And from the expression on her face, I can only guess that one or more of Sasha's fingers is now deep inside of her."
    "[bree.name] begins to almost jump on the spot, as though she can't take the sensations that she's feeling right now."
    "This sets her chest to bobbing up and down in sympathy, the sight made all the more impressive by the way the water rushes over them and covers them with droplets."
    "I can't see Sasha's face as well as I can [bree.name]'s, though I can clearly see that she's every bit as turned on by her own actions as is the girl receiving them."
    "Denied the chance to kiss [bree.name]'s lips for a second time by the way her head is cast back, Sasha bows down and begins to lick at her nipples instead."
    "Rather than causing [bree.name]'s chest to move less than before, this only serves to make her writhe and thrash as Sasha even takes her nipples between her teeth and nips at them hungrily."
    "Finally, Sasha goes lower still, sliding downwards until she's kneeling in front of [bree.name] in the bottom of the shower cubicle."
    "She doesn't allow enough time for the other girl to regain even a small amount of her composure."
    "Instead she leans quickly forward, and I see the briefest glimpse of her tongue as it darts towards [bree.name]'s already much aroused pussy."
    "Honestly, I don't know which one of the girls is turning me on more, as I feel my cock straining against my shorts at the sight of all this."
    "[bree.name]'s show of arousal and her naked body being shown off in all of its glory is a memory that'll stay with me for a long, long time."
    "But the sheer tenacity and technique that Sasha's putting into producing all of that arousal makes me long for the same treatment myself."
    "I'm pretty sure that from the way she's shaking and biting her bottom lip, [bree.name] won't be able to hang on in there much longer."
    "And I'm proven right just a few moments later, as she literally gasps and clasps the side of Sasha's head with both of her hands."
    "Still yelping and twitching from the strength of her orgasm, [bree.name] only just manages to guide Sasha's head away from her groin with shaking arms."
    "Now that the whole thing is over, the spell that it momentarily cast over me seems to vanish."
    "I realise that I'm only a couple of metres away from [bree.name] and Sasha, watching this intimate moment without a shred of excuse or permission."
    stop sound
    "This sends me darting back to my bedroom and hopping under the covers, all too aware of my still painfully erect cock."
    "Taking it in the palm of my hand, I close my eyes and try to summon a mental image of what I've just seen."
    "But I already know that whatever I can pull out of my memory, it won't even come close to the sight of the real thing just now."
    return

label sasha_male_ending:
    $ game.hour = 16












    if renpy.has_label("sasha_achievement_3") and not game.flags.cheat:
        call sasha_achievement_3 from _call_sasha_achievement_3
    $ game.room = "church"
    scene bg church wedding with fade
    "If you'd asked me to guess where my life would take me even a couple of months before today, I doubt that I'd have been able to predict anything as crazy or wonderful as what I'm doing right now."
    "I'm standing before the altar of an old church, in front of dozens of people who are all in gothic dress, while harps and lyres play in the background."
    "I ask you - who else could I be waiting for, but Sasha?"
    "It really doesn't matter to me that I can't identify most of the guests that are sitting behind me."
    "They could all be strangers or a mass gathering of professional wedding-crashers for all I care."
    "I've seen all of their names on the guest-list that we put together and heard an explanation of just who they are in relation to Sasha."
    "But in reality, she's the only person that I want to see."
    "I'd have been happy if it were just the two of us and the priest performing the ceremony."
    "Actually, we almost did just that - disappearing together with the intention of getting married in secret."
    "But in the end we decided that this was something that we wanted people to see and remember."
    "Suddenly the music changes from the sedate background noise we chose for while people were filing into the church to the piece for Sasha's procession down the aisle."
    "I take a deep breath, waiting for my first glimpse of her in the dress that she's been keeping under wraps until today."
    "Sasha's been careful to tell me nothing about the look she's chosen, not even dropping as much as a hint."
    "There's no prize for guessing that it'll most likely be something in keeping with the gothic theme that we've gone with for the entire wedding."
    "But still, this is her wedding dress, and even a girl as unique as Sasha is going to want to make an impression when she walks down the aisle."
    show sasha wedding shy at center, zoomAt(1.0, (640, 720)) with dissolve
    "And the moment that I see her enter the church, I can see that's just what she's managed to do..."
    show sasha wedding at center, traveling(1.5, 5.0, (640, 1040))
    if not sasha.is_visibly_pregnant:
        "Sasha sweeps into the church, a vision in red and black against her strikingly pale skin."
        "The dress is a bodice of red above flowing skirts of that same colour and folds of black."
        "Delicate sleeves of lace cover her arms, and three crimson roses have been woven into her tumbling, ebony hair."
        "In her hands, Sasha clutches a bouquet of black roses."
        "And her face is obscured by a veil of fine, black lace."
        "Oh, did I forget to mention - she kind of has a thing for black!"
        "And since I've grown to love her, so do I."
        "When I said she was a vision, I meant it."
    else:
        "Sasha sweeps into the church, a vision in red and black against her strikingly pale skin."
        "The dress is a bodice of red, cut to be sympathetic to the curve of her swelling belly."
        "Below are flowing skirts of that same colour and folds of black."
        "Delicate sleeves of lace cover her arms, and three crimson roses have been woven into her tumbling, ebony hair."
        "In her hands, Sasha clutches a bouquet of black roses."
        "And her face is obscured by a veil of fine, black lace."
        "Oh, did I forget to mention - she kind of has a thing for black!"
        "And since I've grown to love her, so do I."
        "When I said she was a vision, I meant it."
    "As much as she's an alternative kind of girl that doesn't define herself solely on her looks, I can still see that Sasha's enjoying the attention she's getting."
    show wedding sasha with fade
    "Joining me at the altar, even the veil that she's wearing can't do much to hide the smile on her face."
    "Though I'm sure that a good part of the reason for that smile is also on account of the fact that we're finally about to go through with it and tie the knot."
    show wedding sasha priest with dissolve
    "With Sasha finally standing by my side, the priest gives us a nod and a smile, letting us know that he's ready to start the ceremony proper."
    "You'd be wrong if you were thinking that we'd gone and composed long, dramatic passages of gothic verse for the purpose of our vows."
    "In reality, they're very simple and honest, uncomplicated sentiments that we feel for each other and want to be the basis of our union."
    "I can almost feel my hands shaking as we exchange rings."
    "And then the time comes for me to lift the veil from Sasha's face."
    "Now there's no illusions involved - I can definitely feel my hands shaking from the pressure and the emotions passing through me."
    "As crazy as it sounds, I feel as though I'm looking on that so familiar face in a totally new way, now that we're husband and wife."
    "The same eyes that I've looked into countless times as we made our way from housemates to friends and then lovers, seem somehow different to me now."
    "I look into them and Sasha looks back at me with the knowledge that we've just made a vow to spend the rest of our lives together."
    "And those new lives start right here and now."
    "Priest" "You may kiss the bride..."
    scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
    show sasha kiss wedding
    with fade
    $ sasha.flags.kiss += 1
    "Sasha wraps her arms around me as I pull her into a gentle embrace and kiss her full on the lips."
    "It feels as wonderful now as it did the very first time."
    "Outside, on the church steps, the guests toss confetti - which, of course, is black."
    "And then Sasha tosses her bouquet to the crowd, who mill around in anticipation."
    "But whoever catches it, I have no idea, as I only have eyes for her."
    "And I seriously hope that I always will."
    scene bg park
    show sasha ending
    with fade
    sasha.say "So, after we tied the knot, we saved up enough to put down a deposit on a ruined gothic castle in Transylvania."
    sasha.say "And now we live our lives in imitation of the most iconic vampires from the silver screen and the pages of classic horror literature."
    sasha.say "The end..."
    sasha.say "Hah, nope - but I had you fooled for a moment there, didn't I?"
    sasha.say "I guess if I were to compare meeting [hero.name] to anything, it'd be picking up a book with a goofy-looking cover."
    sasha.say "In that situation, you have one of two choices."
    sasha.say "Firstly, you can go with your gut reaction and assume that what's on the inside is going to be just as goofy and toss it aside."
    sasha.say "Or secondly, you can have a glance at the blurb on the back, maybe even read a couple of pages and see how it grabs you."
    sasha.say "That's how [hero.name] seemed to me when we first met - a paperback that looked like it could be fun, but with a cover that you just had to get past or not."
    sasha.say "And I'm glad that I did read those first couple of pages, because the story just seemed to get better and better as it went on."
    sasha.say "First I found out that he was pretty funny and charming."
    sasha.say "Then that he was into the same kind of stuff as me."
    sasha.say "Next I began to realise just how much I liked his company."
    sasha.say "And finally I discovered that the itch inside of me was for us to be more than just friends."
    sasha.say "Sure, he's a pretty typical guy sometimes - childish, with a short attention span and his mind on only one thing."
    sasha.say "But I know that I can be no bed of roses myself, and we both know when to give each other the space we need."
    sasha.say "It's funny, how I'd always sworn that I'd never be a wife with a home in the suburbs."
    sasha.say "But now that's exactly what I am, it's not all that bad after all."
    sasha.say "No one's chained me to the sink or made me behave like a Stepford Wife - at least so far..."
    if not sasha.is_visibly_pregnant:
        sasha.say "The only real fly in the ointment when we got back from the honeymoon was how the atmosphere in the house changed."
        sasha.say "I guess that [hero.name] and I being a couple kind of ruined the dynamic for [bree.name]."
        sasha.say "She started spending less time around us and more in her room, until she upped and told us she was moving out."
        sasha.say "Sure, it was sad - but she keeps in touch and seems to be doing well in her new place."
    else:
        sasha.say "The only real fly in the ointment when we got back from the honeymoon was how the atmosphere in the house changed."
        sasha.say "I guess that [hero.name] and I being a couple kind of ruined the dynamic for [bree.name]."
        sasha.say "And then when Dahlia came along, it must have felt like she was intruding on our little family the whole time."
        sasha.say "She started spending less time around us and more in her room, until she upped and told us she was moving out."
        sasha.say "Sure, it was sad - but she keeps in touch and seems to be doing well in her new place."
    sasha.say "I don't think marriage has changed us all that much though."
    sasha.say "We still have the band, go to gigs and see a movie every now and then."
    sasha.say "If you thought that I was going to paint the whole house black and fill the yard with tombstones, then I'm sorry to disappoint you."
    sasha.say "Maybe we do put out Halloween decorations up a little earlier than the rest of the neighbourhood and take them down later."
    sasha.say "But we do normal folks stuff as well, more often than you might think, too."
    sasha.say "We have BBQs and parties, swim in the pool and go to the beach."
    sasha.say "Well, maybe not the last one - you don't stay this pale by getting too much sun!"
    sasha.say "In fact, you want proof of just how normal we can be?"
    sasha.say "Then here we are, walking through the park on a nice, sunny day."
    sasha.say "Look at us, smiling and laughing like we don't have a care in the world."
    sasha.say "As far as anyone can tell, we're just another, normal couple leading normal lives."
    sasha.say "And no one needs to know the truth of just how different we are under the surface - or what goes on behind closed doors!"
    scene bg black with dissolve

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not sasha.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_19
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_19
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label sasha_shower_BJ:
    $ renpy.sound.play("sd/shower.ogg", loop=True)
    show sasha
    if not Harem.find_by_name("home"):
        "I have no idea whatsoever how [bree.name] would react to the idea that Sasha and I were getting up to something intimate under the same roof as her."
        "But all the same, it's certainly more than a little enjoyable to play along and believe that we're sneaking around and trying to keep from being caught."
    "Sasha reaches into the shower cubicle and turns on the water so that steam begins to rise and fog the glass of the door."
    "And then she turns to face me, already beginning to strip off the few clothes that she's wearing."
    "I stand there for a moment, quite happy to be watching Sasha as she reveals her body to me."
    "But then she makes a point of looking me up and down with a sense of amused urgency in her eyes, shaking her head at the same time."
    "It's at this moment that I realise I'm just standing there, not bothering to follow her example."
    "I make an apologetic gesture and scrabble to pull of my own clothes whilst still trying to keep most of my attention on Sasha, who by now is completely naked."
    "Still shaking her head at my tardiness, she opens the shower door and slips inside."
    "As I pull off the last of my clothes, I look up just in time to see her arm beckoning to me through the crack in the door."
    "Hurrying to follow, I almost blunder into the shower, expecting to find her waiting for me just inside."
    "But all I find once I'm inside is a wall of steam to greet me."
    "The shower cubicle can't be more than a couple of feet wide, but still Sasha's somehow managed to hide from me in here!"
    "I can just about hear her laughing at my expense over the sound of the water, but still I can't quite work out exactly where she is."
    "Putting my hands out in front of me, I grope for her in the confined space."
    "For a moment the tips of my fingers brush something soft and slick, and then it slips past me and I lose it once more."
    "Sasha's laughing even more now, so much so that I swear I can tell just where she must be."
    "I make another lunge for her, and this time almost manage to grasp what felt like part of a thigh or buttock."
    "This near miss wins me a whooping cry from Sasha, who clearly thought that she had eluded me as easily as the first time."
    "But then the possibility occurs to me that she might not be trying as hard as I thought, and maybe she actually wants to get caught."
    "My suspicions are all but confirmed when I feel the palms of her open hands press against my own, fingers twining between mine."
    "Chasing her has made me all the more eager to have her, and I immediately pull Sasha against me."
    "She feels incredible from the moment that we come together, skin to skin, her slippery belly and breasts sliding in a delightful manner."
    "I try to kiss her, but all that Sasha will allow me is the briefest of contact between our lips before she pulls away."
    "Before I can make my disappointment known, I feel her hand as it reaches down to stroke my cock and then gently squeeze my balls."
    "I could object, but sometimes, when they say that you really don't know what you want until you get it, they're telling the absolute truth."
    hide sasha
    show shower bj breesasha sasha
    with fade
    "Sasha keeps on playing with my now stiffening cock as she gets down on her knees before me."
    "And by the time she's able to look me in the groin, there's no more teasing required for what she has in mind to do next."
    "The only reason that I can see what's going on down there is on account of Sasha's jet black hair and the heavy make-up of the same colour that she's wearing."
    "But even this is beginning to streak and run down her face as the water of the shower cascades down upon her."
    "All that seems impervious to this gradual washing away is the black lipstick that she's wearing."
    show shower bj breesasha sashamouth
    "And I note this as I see the shape of her lips outlined in that way, closing gently over the head of my cock."
    "I'm grateful for the fact that Sasha seems to want to go slowly, taking me into her mouth a little at a time."
    "What with the heat and confined space in the shower, the last thing I need is to get over-excited and end up passing out!"
    "The care that she's taking also means that I can feel every single twist and turn that her tongue and lips make on the shaft too."
    "But that's not to say Sasha doesn't sprinkle a little pain in with the pleasure as well."
    "More than once I find myself gasping in a moment of discomfort as she sinks her teeth in, just enough to get such a reaction out of me."
    "I only realise just how deep Sasha seems intent on taking me when I look down and see how close her lips are getting to the base of my cock."
    "Maybe the shower starting to feel more like a sauna has loosened her throat up, or maybe she's just determined to deep throat me."
    "Either way, she surely can't take any more of it in there without being in danger of choking."
    "And yet that's exactly what she does, as I feel the muscles at the top of her throat begin to squeeze at me when they go into spasm."
    "While the heat wasn't getting to me before now, the sheer intensity of what Sasha's doing to me seems to be making me all the more susceptible."
    "For the first time I can feel my head starting to reel and my legs becoming weaker."
    "Not knowing what else to do, I put my hands on the side of Sasha's head and try to pull her off of my cock before I can faint away and end up hurting us both."
    "Needless to say, she's not exactly ready for this, and her already twitching throat muscles clamp down all the harder on my cock as a result."
    hide shower bj breesasha
    show shower bj breesasha sasha
    "This means that by the time I finally manage to drag my cock out of her Sasha is coughing and wheezing in order to catch her breath."
    show shower bj breesasha sasha shoot with hpunch
    "Unable to hold it in or else turn away from her, I cum a mere few seconds later."
    show shower bj breesasha sasha shoot facial with hpunch
    "Still fighting for air, Sasha takes the entire thing square in the face."
    with hpunch
    "The streamers of cum stripe her cheeks and forehead, but those that hit her mouth are immediately drawn in and swallowed."
    "Leaning against the wall, I find myself gasping for breath in a similar manner."
    "And I can't for the life of me tell if it's more from the heat of the shower or the sensation of release."
    stop sound
    $ sasha.flags.showerbj = True
    return

label sasha_nightclub_comment:
    show sasha at center, zoomAt(1.0, (640, 720))
    "Sometimes I feel like it's harder to live with Sasha than it is [bree.name]."
    "Sure, they're both super-hot girls with a hell of a lot to recommend them."
    "But Sasha's the one with a 'thing', if you know what I mean?"
    "She has an image and a persona that's all bound up with the way that she dresses and the music that she listens to."
    "She's the kind of person that tuts at things she thinks are lame and doesn't spare anyone's feelings when she does so either."
    "Of course, I want to impress her, to make her believe that I'm anything but lame."
    "And yet I'm always worried that she's going to interpret even my efforts to win her approval as the lamest thing imaginable."
    "That's usually how I wind up getting myself into conversations like this one..."
    show sasha shout at center, traveling(1.25, 0.3, (640, 880))
    sasha.say "Hey, [hero.name] - you got any plans for tonight?"
    show sasha normal
    mike.say "Erm, no, Sasha."
    mike.say "I was just going to stay in and catch up on some coursework I have due in."
    show sasha annoyed
    "Sasha rolls her eyes, and I can instantly tell that she's on the brink of uttering the L word."
    mike.say "But I'm free this weekend - if you're asking?"
    mike.say "You were asking, weren't you?"
    show sasha happy
    "Sasha smiles and sighs, as if she can't decide whether to be disappointed or amused with my answer."
    show sasha shout
    sasha.say "Well, I don't have anything definite planned."
    sasha.say "But there's a pretty decent club that just opened up in town."
    sasha.say "I was thinking of checking it out - but I don't know if it'd be your kind of thing..."
    show sasha normal
    "Just what is she trying to do?"
    "Dangle the chance of accompanying her to a nightclub in front of me and then snatch it away a second later?"
    "The excuse she just used is one of those instances where the person it's intended for is supposed to get it instantly."
    "They're supposed to understand that the speaker's giving them a get-out clause and the chance not to cause a scene."
    "I should really nod and smile, and certainly not pick at the statement any further."
    "None of which I have the good sense to do right now."
    mike.say "What's that supposed to mean?"
    mike.say "I go out partying."
    mike.say "I go to clubs too."
    show sasha annoyed
    "Sasha looks suitably awkward as I demand that she expand on her earlier point, her face creasing into a helpless frown."
    show sasha shout
    sasha.say "Yeah...okay...I get that."
    sasha.say "That's not what I meant, anyway..."
    show sasha normal
    mike.say "Well, what did you mean?"
    show sasha shout
    sasha.say "Alright, alright, [hero.name] - I meant your clothes, okay?"
    sasha.say "The place I'm talking about won't let you in dressed like you dress."
    show sasha normal
    "I glance down at myself, noting the casual nature of what I'm wearing."
    "But then I remember that I don't dress like this all the time."
    "I'm just in clothes that I've thrown on to mooch around the house and slob in front of the TV."
    "I look at Sasha in askance."
    show sasha shout
    sasha.say "No, you terminal moron - I don't mean the stuff that you put on to laze around the house after work!"
    show sasha normal
    mike.say "But...but I have decent clothes, really I do."
    mike.say "I go out in them all the time!"
    show sasha happy at startle
    "Sasha snorts in amusement and shakes her head at my pathetic pleas."
    show sasha shout
    sasha.say "Please - you mean the stuff I see you out in around the local bars?"
    sasha.say "That might get you into the vanilla clubs that are for the vanilla people."
    sasha.say "But not this place, [hero.name]."
    sasha.say "Because this place has teeth!"
    show sasha normal
    "My spirits sink at this, and I feel the weight of what just happened pressing down on me."
    "It really happened - Sasha called me out for being lame!"
    "But then a thought occurs to me."
    "If she really did think that I was lame, why would Sasha even bother talking to me about it?"
    "She was asking me if I had plans for the night, just now - right?"
    "And she only really backed off when the subject of my dress-sense came up."
    "So what if she's being subtle, giving me the chance to realise that she doesn't think I'm lame, just that I need to change up my wardrobe?"
    "Whether I'm right or wrong, that's something far more easy to deal with and actually do something about!"
    show screen message(title="Buy a nice outfit!",what="Sasha told me to buy a {b}fancy clothes{/b} to be able to go to the nightclub.")
    pause
    hide screen message
    hide sasha
    return

label sasha_wearing_strapon:
    scene bg secondfloor at blur(16), dark, dark with dissolve
    "I've been living with Sasha for so long now that a lot of the barriers between us have come down."
    "Don't get me wrong, I'm not talking about walking into the bathroom while she's using it."
    "Nothing crazy like that - although walking in on her in the shower is a whole different affair..."
    "It's just that I find myself skipping the little social niceties with her."
    scene bg secondfloor with dissolve
    "You know what I mean - the ones that you observe when you're getting to know each other."
    "The ones that you hope will make the other person believe that you're a normal, sane individual."
    show bg door bedroom3 at center, zoomAt(1, (640, 720))
    show bg door bedroom3 at center, traveling(1.5, 0.3, (640, 1040))
    pause 0.3
    play sound door_knock
    "But now that we're past that, I don't think twice before knocking on Sasha's bedroom door and walking in."
    scene bg black with dissolve
    pause 0.1
    scene bg bedroom3
    with wipeleft
    mike.say "Hey, Sasha!"
    mike.say "You have to see this..."
    "I trail off as I catch sight of Sasha standing in front of the mirror."
    "She has her back to me, but that's not a concern right now."
    "Because she also has nothing on but a skimpy t-shirt and her underwear!"
    "Whatever I was meaning to talk to Sasha about disappears from my mind."
    "Now all I can do is stare at the sight of her almost naked from the waist down."
    "Sasha's buttocks, thighs and calves look so good as she's standing there."
    "So good that I almost don't notice when she glances over her shoulder at me a moment later."
    show sasha vangry at center, zoomAt(1.5, (640, 1040)) with hpunch
    sasha.say "Hey!"
    sasha.say "Did you ever hear of knocking and waiting for an answer?"
    sasha.say "Who said you could come barging straight in here uninvited?!?"
    show sasha annoyed
    "It takes quite an effort on my part."
    "But I manage to tear my eyes off of Sasha's butt."
    mike.say "Sorry, Sasha, sorry!"
    mike.say "I...I just couldn't help it..."
    mike.say "You look SO hot right now!"
    show sasha normal
    "I see a grudging smile start to spread across Sasha's face."
    "She might be pissed with me walking in on her unannounced."
    "But that doesn't mean she's not vulnerable to such blatant flattery."
    show sasha shout
    sasha.say "Oh really?"
    sasha.say "You like what you see, [hero.name]?"
    show sasha normal
    "Still with her back turned to me, Sasha runs her fingers over the panties she's wearing."
    "It's only now that I can see they're not actually normal underwear at all."
    "In fact, what's visible to me looks more like straps than anything else."
    "But hey, I know that Sasha's a kinky kind of girl."
    "So outrageous underwear is something right up her street!"
    mike.say "Ah...yeah, Sasha."
    mike.say "Like I said - it's really hot!"
    show sasha happy
    sasha.say "That's great to hear, [hero.name]."
    show sasha shout
    sasha.say "Because some guys would be put off by this kind of thing."
    sasha.say "They'd be intimidated, you know?"
    show sasha normal
    "I swallow and shake my head, determined to show that I'm not that kind of guy."
    mike.say "Not me, Sasha."
    mike.say "I'm an enlightened, modern guy."
    mike.say "I can handle this kind of thing..."
    hide sasha
    show sasha strapon at center, zoomAt (1.15, (640, 840))
    with hpunch
    "It's just as I'm saying this that Sasha chooses to turn and face me."
    "As she does so, I see everything that was hidden from view presented to me."
    "Everything is as I expected - save for the massive cock swinging out in front of her!"
    "It's not underwear she has on at all - it's a huge strap-on!"
    "Sasha lets out a peal of laughter as she sees my eyes go wide."
    "But I guess it's fair payback for my having barged in on her just now."
    show fx question
    show sasha joke
    sasha.say "What's the matter, [hero.name]?"
    sasha.say "Feeling a little inadequate all of a sudden?"
    show sasha happy at startle
    "She laughs again, making the strap-on sway menacingly from side to side."
    show sasha normal
    if hero.sexperience >= 20:
        mike.say "You do know that thing's not real, right?"
        mike.say "And it's not just about sticking a cock on and pretending."
        show sasha at center, traveling (1.35, 0.3, (640, 940))
        "I step forwards and take hold of the phallus in one hand."
        "And then I use it to pull Sasha towards me."
        "She gasps a little at the bold gesture."
        "But I can tell from the look in her eyes that she's liking it."
        mike.say "You have to know what to do with it, Sasha."
        "She's looking me straight in the eye right now."
        "I can hear her breath coming in little gasps too."
        "Sasha must have gotten herself pretty worked up looking in the mirror."
        "She's turned on now, and I can feel the same thing happening to me too!"
        show sasha strapon blush
        sasha.say "Y...you're all talk, [hero.name]!"
        sasha.say "Just like a typical guy!"
        show sasha shy
        mike.say "You think so, Sasha?"
        mike.say "How about we see who's better at giving it?"
        mike.say "That and who likes taking it more too?"
        show sasha surprised
        "Sasha blinks in surprise."
        "Her mouth works silently until she manages to get the words out."
        show fx question
        sasha.say "You...you're not serious?"
        sasha.say "You wouldn't let me..."
        show sasha stuned
        "I smile, enjoying the sight of her wrong-footed for a moment."
        mike.say "Why not, Sasha?"
        mike.say "I already said I was a modern guy."
        mike.say "I'm not afraid of taking it from you."
        mike.say "That is, if you're brave enough to give it to me?"
        "Sasha says nothing for a few seconds."
        show sasha shy
        "But then she nods eagerly."
        mike.say "Okay, Sasha."
        mike.say "You choose the place and the time."
        mike.say "And I'll be there!"
        "With that I give her a smile and turn to walk out of her bedroom."
        "It feels good to have called Sasha's bluff like that."
        "I just hope that I can live up to the promise I made her!"
        $ sasha.sub += 2
    else:
        mike.say "Oh...oh god!"
        mike.say "S...Sasha..."
        mike.say "What the hell is that thing?"
        mike.say "What are you going to do with it?!?"
        show sasha happy at startle
        "Sasha's laughter becomes that much louder as I begin to panic."
        show sasha at center, traveling (1.35, 0.3, (640, 940))
        "She advances on me, thrusting the phallus in front of her as she comes."
        show sasha shout
        sasha.say "What do you think I'm going to do with it, [hero.name]?"
        sasha.say "It's a cock - I'm gonna use it to fuck someone!"
        show sasha normal
        "By now she's almost close enough for the thing to actually touch me."
        "My eyes are fixed on it, and I take a leap back to escape it."
        mike.say "Whoa..."
        mike.say "Y...you keep that thing away from me!"
        show sasha strapon shout
        sasha.say "Come on, [hero.name] - lighten up."
        show fx question
        sasha.say "Haven't you ever wondered what it'd be like?"
        sasha.say "You know, taking instead of giving?"
        sasha.say "Give it a chance and you might like it!"
        show sasha normal at center, traveling (1.5, 0.3, (640, 1040))
        "Sasha almost jumps forwards then, the phallus slapping me on the thigh."
        "I can't help it - I let out a cry of horror and bolt out of the door."
        "And I can still hear her laughing as I hurry away down the corridor."
        $ sasha.sub -= 2
    $ sasha.flags.strapon_known = True
    return

label sasha_pregnant_request:
    show sasha at center, zoomAt (1.25, (640, 880)) with fade
    "I thought that I had a pretty good handle on Sasha."
    "At least in terms of what she wants and where we're going."
    "But I must have been wrong on that score."
    "And that's because she surprised me with a question."
    "One that I could never have seen coming from her."
    "Not in a million years!"
    show sasha shout
    sasha.say "Hey, [hero.name]."
    show sasha normal
    mike.say "Ah, yeah, Sasha?"
    show sasha shout
    sasha.say "You ever think about us having a kid together?"
    show sasha normal
    "Sasha says this in such a casual, matter-of-fact way."
    "For a moment, I'm not sure I actually heard her right."
    mike.say "S...Sasha..."
    mike.say "Did you just say we should have a baby?!?"
    show sasha stuned
    "Sasha looks at me sideways, like I really haven't understood her at all."
    show sasha surprised
    sasha.say "What?!?"
    sasha.say "I didn't say we SHOULD!"
    show sasha shout
    sasha.say "All I said was did you ever THINK about it."
    sasha.say "But now that it's out there..."
    sasha.say "Do you think maybe we could?"
    show sasha normal
    "Somehow she's managed to turn this thing around on me."
    "Just like that it's gone from her asking the question to me being put on the spot!"
    mike.say "Well...I..."
    mike.say "I have thought about it, I guess."
    mike.say "But vaguely, you know?"
    mike.say "Like something we might do in the future?"
    show sasha sadsmile
    "Sasha looks a little crestfallen at this, as though it's the wrong answer."
    "The last thing that I want is to come across like an insensitive jerk."
    "But I can't just agree with her in order to get back on her good side either."
    "Having kids together is something that we both need to agree on for it to work."
    "We need to do what's best for the both of us."
    "Not to mention our theoretical offspring too!"
    show sasha whining
    sasha.say "Do you think I'd make a bad mom?"
    show sasha sadsmile
    "Oh shit - Sasha just hit me with a sucker-punch!"
    mike.say "Oh god, Sasha - of course not!"
    mike.say "It's just that you never mentioned kids before now."
    mike.say "And these days..."
    mike.say "Well...it's kind of sexist to assume that's what a girl wants!"
    show sasha normal
    "Sasha nods heavily, letting out an equally heavy breath as she does so."
    show sasha shout
    sasha.say "Yeah, yeah...I know."
    sasha.say "But putting all of that crap aside."
    sasha.say "What about it, huh?"
    show sasha normal
    menu:
        "Agree":
            "Why am I over-thinking this?"
            "What if I'd done that when it came to Sasha and me?"
            "We'd never have gotten beyond being housemates."
            "We'd still be little more than awkward friends!"
            "Maybe I need to be more impulsive?"
            mike.say "I think we should go for it, Sasha."
            mike.say "That's what I think."
            show sasha surprised
            "Sasha stares at me for a moment."
            "Her eyes are wide and her mouth is hanging open."
            show sasha normal
            "Then, all of a sudden, she starts talking again."
            show sasha happy
            sasha.say "Oh god..."
            sasha.say "Oh...[hero.name]..."
            show sasha shout
            sasha.say "Are you serious?!?"
            show sasha normal
            mike.say "Of course I am, Sasha!"
            mike.say "You just caught me out, that's all."
            mike.say "You made me think about it for real."
            mike.say "Sure, it's scary."
            mike.say "But I know that I love you - so what else matters?"
            "Sasha grabs hold of my hands and squeezes them tightly."
            show sasha happy
            "She's smiling so much that it's almost scary!"
            show sasha shout
            sasha.say "I don't know what having a baby's gonna be like."
            sasha.say "But I know the first part is going to be fun!"
            $ sasha.love += 2
            $ sasha.flags.pregrequest = True
        "Refuse":
            "I can't ignore the way that Sasha's question has made me feel."
            "And all of the questions that it's thrown up in my mind either."
            "If I said yes to her now, it'd be a huge mistake."
            "I'd only be doing it to make her happy here and now."
            "The one thing I'm sure of is that it'd end in disaster."
            mike.say "I think we already answered that one, Sasha."
            mike.say "Kids are something that we need to plan ahead for."
            mike.say "We can't just decide to bring a life into the world like that."
            mike.say "It's not fair on us or the kid."
            "Sasha sighs and nods again."
            "But this time she doesn't protest."
            show sasha shout
            sasha.say "I...I guess you're right, [hero.name]."
            sasha.say "If me asking you shows anything, it's that we're not ready."
            sasha.say "I think if we were, you'd have said yes straight away."
            show sasha sadsmile
            "All I can do is give Sasha a weak smile in response."
            "It hurts to have to let her down like this."
            "But I think it's the best thing for the both of us."
            $ sasha.love -= 2
    return

label sasha_cheated_sam_advice:
    show samantha
    if samantha.flags.nickname == "cupcake":
        mike.say "Ah...hey, Cupcake..."
    else:
        mike.say "Ah...hey, Sam..."
    samantha.say "Oh dear, someone sounds like they've got the world on their shoulders."
    samantha.say "Want to talk about it?"
    mike.say "Yeah...but I'm not sure you will once you know what's up."
    samantha.say "Well, you won't know that until you try me, will you?"
    "I take a deep breath and then just come out with it, consequences be damned."
    mike.say "I might have cheated on my girlfriend a little."
    mike.say "And she might have found out too..."
    $ samantha.love -= 10
    "There's an awkward silence between us, as if Sam is pondering my words."
    samantha.say "Hmm...I see."
    samantha.say "And did you ask me because you thought I'd be sympathetic?"
    samantha.say "Or because you wanted to see how someone that's been cheated on reacts?"
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake...I...I feel awful about this...guilty as hell!"
    else:
        mike.say "Sam...I...I feel awful about this...guilty as hell!"
    mike.say "But, maybe you're right."
    mike.say "I'm sorry - I see now that I shouldn't have talked to you about this..."
    samantha.say "No, [hero.name], wait - don't leave just yet."
    "I pause, waiting to hear what Sam will say next."
    samantha.say "I was lashing out at you just now, punishing you for what happened to me."
    samantha.say "I forgot what you did for me back then."
    samantha.say "And no one ever agonised over cheating on me like you are right now."
    if samantha.flags.nickname == "cupcake":
        mike.say "Thanks, Cupcake...but I'm not sure I deserve that compliment."
    else:
        mike.say "Thanks, Sam...but I'm not sure I deserve that compliment."
    mike.say "Will you help me find a way to make her take me back?"
    samantha.say "No, I can't."
    samantha.say "She has to want to do that herself."
    mike.say "But how do I..."
    samantha.say "You just have to keep on doing what you're doing, [hero.name]."
    samantha.say "Be honest, show her that you realise what you did was wrong and that you're sorry you hurt her."
    samantha.say "In the end, it's her decision to make."
    hide samantha
    "When the conversation with Sam is done, I mull over her advice again and again."
    "What she said makes sense, but I still feel scared to leave the decision entirely in Sasha's hands."
    "But then I asked for the advice from the person I thought could help me the most."
    "So if I really want to mend things with Sasha, what choice do I have?"
    $ sasha.flags.cheatedSamAdvice = 1
    return

label sasha_morningwood:
    "The moment that I wake up, I realise that I have the most acute case of morning wood imaginable."
    "My cock is so hard that it's almost painful!"
    "And I know that, if I want to get up and get the day started, I need to tackle it first."
    "I'm about to get on with the most obvious solution, taking matters into my own hands."
    "So I think about recalling a particularly hot memory or finding some material on my phone."
    "But then another thought occurs to me."
    "Why waste my time on something imaginary or a bunch of pictures?"
    "Especially when I have the real thing under the same roof as me!"
    menu:
        "Try to ignore the inconvenience":
            $ hero.fun -= 5
            $ hero.cancel_event()
            return
        "Let Sasha know what she's responsible for":
            pass
    "With that in mind, I slide out of bed and hurry to the door."
    scene bg secondfloor with fade
    "Then I hurry towards another door, trying to be as quick and quiet as I can."
    "I'm pretty sure that I'm the first person up and about this morning."
    "I haven't heard anyone else stirring yet, and everyone likes to sleep in when they can."
    "So as I ease the door to Sasha's room open, I'm pretty confident she's still in there."
    scene bg bedroom3 with fade
    "And my other hunch, that she's still asleep, is confirmed a moment later."
    "I can see her head on the pillow as I sneak inside and close the door."
    show sleep sasha with fade
    "Sure, Sasha has her back turned to me right now."
    "But I'm sure she's asleep because I can hear the sound of her snoring."
    "It's not like she's sawing wood in her sleep or anything."
    "The sound's quite subtle, even cute to my ear."
    "But it's still reassuring to hear as I creep over to her bed."
    "The covers have fallen away a little, just enough to reveal Sasha's back."
    "And they're also revealing a tantalising glimpse of her ass too!"
    "Taking one last look back at the door, I lift the covers a little more."
    "Just enough so that I can slowly slide under them and get into bed with Sasha."
    "I figure that she loves surprises, so this should be a hit with her."
    "And if not...well, I'll be the first to know!"
    "Luckily for me, Sasha likes to sleep in pretty skimpy stuff."
    "So after I slip off my own clothes, there's not much else to do."
    "I ease aside what she's wearing below the waist."
    "And then I lean forwards, inching my cock towards its intended target."
    "I'm actually holding my breath as it begins to stroke Sasha's lips."
    "Any moment now I'm going to find out if my gamble will pay off."
    "And the very second that Sasha starts to stir, I almost lose my nerve."
    "She shifts underneath me, moaning a little as I try to bring her pussy to life."
    sasha.say "Mmm..."
    sasha.say "Wha..."
    sasha.say "What's happening..."
    mike.say "Good morning, beautiful..."
    mike.say "I thought I'd wake you up with a surprise!"
    "Sasha looks back over her shoulder, her eyes still bleary from sleep."
    "But much to my relief, she smiles as soon as she realises that it's me."
    "Then she opens her mouth to let out a gasp at the sensation of what I'm doing to her."
    sasha.say "Oh..."
    sasha.say "You bad boy!"
    sasha.say "I know what you're after!"
    "I can't help chuckling at the tone of Sasha's voice."
    "And in doing so, I pause for a moment."
    sasha.say "Hey!"
    sasha.say "I don't remember telling you to stop!"
    "Before I can react, Sasha reaches down and grabs a hold of my cock."
    scene sasha doggy
    show sasha doggy bedroom3
    with fade
    "At the same time she rises up, getting on all fours."
    "And she rubs it hard against her pussy."
    show sasha doggy mike
    "Sasha's lips are pretty wet and slippery by now."
    "Which means that what happens next is kind of inevitable."
    "I struggle to keep a hold of her and get into a good position."
    "And while doing that, my cock begins to sink into her."
    sasha.say "Ah..."
    show sasha doggy vaginal entered
    sasha.say "Oh yeah..."
    sasha.say "That's better!"
    sasha.say "Now you're waking me up!"
    $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_low.ogg", loop=True)
    "I hardly need the encouragement that Sasha's giving me right now."
    "After the initial rush of sensation at being inside her, instinct takes over."
    "Sasha's pussy feels so fucking good I can't do it justice."
    "And I'm thrusting in and out of her without pause or hesitation."
    "I have my hands on Sasha's haunches, gripping her tight."
    "The speed I'm going at might not be the fastest I can manage."
    "But all the same, Sasha seems to enjoy this steady pace."
    "And I also make sure to go as deep as I can with every thrust."
    sasha.say "Oh, [hero.name]..."
    show sasha doggy scream
    sasha.say "That feels SO good!"
    "It's not like Sasha needs to tell me how good this feels."
    "It's like our bodies are waking up more with each passing second."
    "They're coming alive at the same time, awaking to each other."
    "This is so much better than being woken up by an alarm clock."
    "And it's the best way to deal with morning wood that I can think of too!"
    "Sasha turns her head, looking back at me over her shoulder."
    $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_medium.ogg", loop=True)
    show sasha doggy orgasm
    "Her eyes are full of the pleasure she's feeling."
    "She's biting her lip as if in hope of releasing the sensations building up inside her."
    "And she's also got one hand on her breasts, pinching and squeezing her stiff nipples."
    "Sasha nods, urging me on and letting me know that she wants more."
    $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_high.ogg", loop=True)
    "But there's only so much more of this I can take."
    mike.say "Sasha..."
    mike.say "I'm losing it!"
    sasha.say "Oh yeah..."
    sasha.say "Me too!"
    $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_orgasm.ogg", loop=True)
    with hpunch
    "Sasha quivers from head to toe as I shoot my load into her."
    show sasha doggy ahegao cum with hpunch
    "She buries her head in the pillow, gasping at the sensation."
    with hpunch
    "And it's all I can do to keep from waking the whole house too!"
    $ renpy.sound.play("sd/moans/sasha/sasha_panting.ogg", loop=True)
    "Afterwards we collapse onto Sasha's bed, panting and spent."
    "I can still feel her pussy as it twitches and squeezes my cock."
    "But neither of us has the energy to talk."
    "So Sasha simply nestles herself into my arms and pulls the covers over us both."
    stop sound
    $ sasha.sexperience += 1
    $ game.room = "secondfloor"
    $ hero.flags.morningwood = TemporaryFlag(True, "day")
    scene bg black with dissolve
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
