init python:
    Event(**{
    "name": "minami_kiss_me",
    "label": "minami_kiss_me",
    "max_girls": 1,
    "music": "music/roa_music/new_days.ogg",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(minami,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            MinFlag("kiss", 1),
            MinStat("love", 150),
            ),
        ],
    "chances": 20,
    "once_day": True,
    "do_once": False,
    "quit": False,
    })

    Event(**{
    "name": "minami_event_02",
    "label": "minami_event_02",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("minami_event_01"),
        HeroTarget(IsGender("male")),
        IsHour(10, 20),
        MinDaysPlayed(26),
        ],
    "music": "music/roa_music/new_days.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "minami_event_03",
    "label": "minami_event_03",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("minami_event_02"),
        IsHour(14, 18),
        HeroTarget(HasRoomTag("home")),
        PersonTarget(minami,
            IsFlag("moveindelay", False),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            ),
        ],
    "music": "music/roa_music/new_days.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "spank_minami",
    "label": "spank_minami",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsHour(8, 20),
        HeroTarget(
            HasRoomTag("home"),
            Not(IsRoom("livingroom")),
            ),
        PersonTarget(minami,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            MinStat("love", 160),
            MinStat("sub", 50),
            MinStat("siscon", 80),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            ),
    ],
    "music": "music/roa_music/new_days.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "minami_preg_talk",
    "label": "minami_preg_talk",
    "do_once": False,
    "music": "music/roa_music/new_days.ogg",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(minami,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("toldpreg", False),
            MinCounter("pregnant", 6),
            ),
        ],
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_siscon_01",
    "label": "minami_siscon_01",
    "duration": 1,
    "priority": 500,
    "conditions": [
        HeroTarget(IsRoom("studio")),
        PersonTarget(minami,
            Not(IsHidden()),
            IsFlag("sisconDelay", False),
            MinStat("love", 190),
            Not(MaxStat("siscon")),
            ),
        ],
    "music": "music/roa_music/new_days.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "minami_siscon_02",
    "label": "minami_siscon_02",
    "duration": 1,
    "priority": 500,
    "conditions": [
        HeroTarget(
            HasRoomTag("home"),
            MaxStat("energy", 2),
            ),
        PersonTarget(minami,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            IsFlag("sisconDelay", False),
            MinStat("love", 190),
            MinStat("siscon", 20),
            Not(MaxStat("siscon")),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_siscon_03",
    "label": "minami_siscon_03",
    "duration": 1,
    "priority": 500,
    "conditions": [
        HeroTarget(IsActivity("take_a_shower")),
        PersonTarget(minami,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            IsFlag("sisconDelay", False),
            MinStat("love", 190),
            Not(MaxStat("siscon")),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_siscon_04",
    "label": "minami_siscon_04",
    "priority": 500,
    "conditions": [
        IsHour(21, 23),
        HeroTarget(IsActivity("sleep")),
        PersonTarget(minami,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            IsFlag("sisconDelay", False),
            MinStat("love", 190),
            Not(MaxStat("siscon")),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_siscon_05",
    "label": "minami_siscon_05",
    "duration": 1,
    "priority": 500,
    "conditions": [
        HeroTarget(IsRoom("livingroom")),
        PersonTarget(minami,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            IsFlag("sisconDelay", False),
            MinStat("love", 190),
            Not(MaxStat("siscon")),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_siscon_06",
    "label": "minami_siscon_06",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsNotDone("minami_siscon_06b"),
        IsSeason(0, 1),
        HeroTarget(IsRoom("pool")),
        PersonTarget(minami,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            IsFlag("sisconDelay", False),
            MinStat("love", 190),
            MinStat("siscon", 60),
            Not(MaxStat("siscon")),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            ),
        Or(
            PersonTarget(minami,
                IsRoom("pool")
                ),
            PersonTarget(bree,
                IsRoom("pool")
                ),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_siscon_06b",
    "label": "minami_siscon_06b",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsNotDone("minami_siscon_06"),
        IsSeason(3),
        "18 <= game.day < 25",
        HeroTarget(IsRoom("date_mall1")),
        PersonTarget(minami,
            OnDate(),
            IsFlag("sisconDelay", False),
            MinStat("love", 190),
            MinStat("siscon", 60),
            Not(MaxStat("siscon")),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_siscon_07",
    "label": "minami_siscon_07",
    "duration": 1,
    "priority": 500,
    "conditions": [
        HeroTarget(IsRoom("livingroom")),
        PersonTarget(minami,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            IsFlag("sisconDelay", False),
            MinStat("love", 190),
            Not(MaxStat("siscon")),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_siscon_08",
    "label": "minami_siscon_08",
    "duration": 1,
    "priority": 500,
    "conditions": [
        HeroTarget(IsRoom("livingroom")),
        PersonTarget(minami,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            IsFlag("sisconDelay", False),
            MinStat("love", 190),
            MinStat("siscon", 40),
            Not(MaxStat("siscon")),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_siscon_09",
    "label": "minami_siscon_09",
    "priority": 500,
    "conditions": [
        HeroTarget(IsRoom("secondfloor")),
        PersonTarget(minami,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            IsFlag("sisconDelay", False),
            MinStat("love", 190),
            MinStat("siscon", 20),
            Not(MaxStat("siscon")),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_siscon_10",
    "label": "minami_siscon_10",
    "priority": 500,
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            IsRoom("nightclub", "nightclubbar", "date_night"),
            ),
        PersonTarget(minami,
            Not(IsHidden()),
            IsRoom("nightclub", "nightclubbar"),
            IsFlag("sisconDelay", False),
            MinStat("love", 190),
            MinStat("siscon", 80),
            Not(MaxStat("siscon")),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    InteractEvent(**{
    "name": "minami_siscon_cap_01",
    "label": "minami_siscon_cap_01",
    "duration": 1,
    "priority": 500,
    "conditions": [
        PersonTarget(minami,
            IsActive(),
            HasRoomTag("home"),
            IsFlag("sisconDelay", False),
            MinStat("love", 190),
            MinStat("siscon", 20),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    InteractActivity(**{
    "name": "minami_siscon_cap_02",
    "display_name": "Practice dating with Minami",
    "label": "minami_siscon_cap_02",
    "icon": "askdateminami",
    "duration": 4,
    "conditions": [
        IsDayOfWeek(6, 7),
        IsTimeOfDay("afternoon"),
        PersonTarget(minami,
            IsActive(),
            IsFlag("sisconDelay", False),
            IsFlag("practiceDate"),
            MinStat("love", 190),
            MinStat("siscon", 40),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_siscon_cap_03",
    "label": "minami_siscon_cap_03",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsHour(14, 18),
        HeroTarget(IsRoom("livingroom", "bedroom5")),
        PersonTarget(minami,
            Not(IsHidden()),
            HasRoomTag("home"),
            IsFlag("sisconDelay", False),
            MinStat("love", 190),
            MinStat("siscon", 60),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_siscon_cap_04",
    "label": "minami_siscon_cap_04",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsHour(14, 18),
        HeroTarget(IsRoom("livingroom", "bedroom5")),
        PersonTarget(minami,
            Not(IsHidden()),
            HasRoomTag("home"),
            IsFlag("sisconDelay", False),
            MinStat("love", 190),
            MinStat("siscon", 80),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_practice_blowjob",
    "label": "minami_practice_blowjob",
    "duration": 2,
    "priority": 500,
    "conditions": [
        IsHour(20, 0),
        HeroTarget(
            IsRoom("livingroom", "bedroom5"),
            HasStamina(),
            ),
        PersonTarget(minami,
            Not(IsHidden()),
            HasRoomTag("home"),
            IsFlag("sisconDelay", False),
            MinStat("love", 190),
            MinStat("siscon", 90),
            ),
        ],
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_practice_sex",
    "label": "minami_practice_sex",
    "duration": 2,
    "priority": 500,
    "conditions": [
        IsHour(20, 0),
        HeroTarget(
            IsRoom("livingroom", "bedroom5"),
            HasStamina(),
            ),
        PersonTarget(minami,
            Not(IsHidden()),
            HasRoomTag("home"),
            IsFlag("sisconDelay", False),
            MinStat("love", 190),
            MinStat("siscon", 100),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_meet_alexis",
    "label": "minami_meet_alexis",
    "priority": 500,
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            IsRoom("mall1"),
            ),
        PersonTarget(minami,
            Not(IsHidden()),
            HasRoomTag("mall_southside"),
            ),
        PersonTarget("alexis",
            Not(IsHidden()),
            HasRoomTag("mall_southside"),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_meet_jack",
    "label": "minami_meet_jack",
    "priority": 500,
    "conditions": [
        HeroTarget(HasRoomTag("pub"),),
        PersonTarget(minami,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_meet_kylie",
    "label": "minami_meet_kylie",
    "priority": 500,
    "conditions": [
        HeroTarget(HasRoomTag("uni")),
        PersonTarget(minami,
            Not(IsHidden()),
            HasRoomTag("uni"),
            ),
        PersonTarget("kylie",
            Not(IsHidden()),
            HasRoomTag("uni"),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_meet_morgan",
    "label": "minami_meet_morgan",
    "priority": 500,
    "conditions": [
        HeroTarget(IsRoom("coffeeshop")),
        PersonTarget(minami,
            Not(IsHidden()),
            HasRoomTag("mall_southside"),
            ),
        PersonTarget("morgan",
            Not(IsHidden()),
            HasRoomTag("mall_southside"),
            MaxStat("male", 80),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_react_kylie_sentence",
    "priority": 1500,
    "label": "minami_react_kylie_sentence",
    "conditions": [
        IsNotDone('kylie_trial_3', 'kylie_trial_3_missed'),
        Or(
            "'kylie_trial_2' in DONE and DONE['kylie_trial_2'] + 7 >= game.days_played",
            "'kylie_trial_2_missed' in DONE and DONE['kylie_trial_2_missed'] + 7 >= game.days_played",
            ),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget("kylie",
            IsFlag("trial_verdict", "tried_but_guilty"),
            ),
        PersonTarget(minami,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "angela_visit",
    "label": "angela_visit",
    "priority": 500,
    "duration": 4,
    "conditions": [
        IsDayOfWeek(6, 7),
        IsHour(14, 16),
        HeroTarget(HasRoomTag("home")),
        PersonTarget(minami,
            Not(IsHidden()),
            HasRoomTag("home"),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    InteractEvent(**{
    "name": "minami_angela_conversation",
    "label": "minami_angela_conversation",
    "priority": 500,
    "conditions": [
        IsDone("angela_visit"),
        PersonTarget(minami,
            IsActive(),
            MinStat("love", 100),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    InteractEvent(**{
    "name": "minami_angela_acceptation",
    "label": "minami_angela_acceptation",
    "priority": 500,
    "conditions": [
        IsDone("minami_angela_conversation"),
        PersonTarget(minami,
            IsActive(),
            MinStat("love", 150),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_love_nightclub",
    "label": "minami_love_dating",
    "conditions": [
        IsDone("angela_visit"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_nightclub")),
        PersonTarget(minami,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_love_beach",
    "label": "minami_love_dating",
    "conditions": [
        IsDone("angela_visit"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_beach", "date_nudistbeach")),
        PersonTarget(minami,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_love_cinema",
    "label": "minami_love_dating",
    "conditions": [
        IsDone("angela_visit"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_cinema")),
        PersonTarget(minami,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_love_home",
    "label": "minami_love_dating",
    "conditions": [
        IsDone("angela_visit"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_livingroom")),
        PersonTarget(minami,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_love_mall",
    "label": "minami_love_dating",
    "conditions": [
        IsDone("angela_visit"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_mall1")),
        PersonTarget(minami,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_love_park",
    "label": "minami_love_dating",
    "conditions": [
        IsDone("angela_visit"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_park")),
        PersonTarget(minami,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_love_pub",
    "label": "minami_love_dating",
    "conditions": [
        IsDone("angela_visit"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_pub")),
        PersonTarget(minami,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_love_restaurant",
    "label": "minami_love_dating",
    "conditions": [
        IsDone("angela_visit"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_restaurant")),
        PersonTarget(minami,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_love_waterpark",
    "label": "minami_love_dating",
    "conditions": [
        IsDone("angela_visit"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_waterpark")),
        PersonTarget(minami,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_event_04",
    "label": "minami_event_04",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("minami_event_03"),
        IsTimeOfDay("afternoon"),
        HeroTarget(HasRoomTag("home")),
        PersonTarget(minami,
            Not(IsHidden()),
            HasRoomTag("home"),
            MinStat("love", 160),
            MinStat("siscon", 100),
            MinStat("sexperience", 1),
            ),
        ],
    "music": "music/roa_music/new_days.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "minami_asleep",
    "label": "minami_asleep",
    "priority": 1500,
    "conditions": [
        HeroTarget(IsRoom("bedroom5")),
        PersonTarget(minami,
            IsPresent(),
            Not(IsHidden()),
            IsActivity("sleep"),
            ),
        ],
    "do_once": False,
    "once_hour": False,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_likes_blondes",
    "label": "minami_likes_blondes",
    "duration": 1,
    "do_once": True,
    "music": "music/roa_music/new_days.ogg",
    "priority": 500,
    "conditions": [
        IsDone("sasha_likes_blondes_2"),
        IsTimeOfDay("morning", "afternoon"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home")),
        PersonTarget(minami,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 120),
            ),
        ],
    })

    InteractEvent(**{
    "name": "minami_murder_talk_sasha",
    "label": "minami_murder_talk_sasha",
    "do_once": True,
    "conditions": [
        PersonTarget(minami,
            IsActive(),
            ),
        PersonTarget("kylie",
            IsFlag("killed", "sasha")
            ),
        ],
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "minami_pregnant_request",
    "label": "minami_pregnant_request",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(minami,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            IsFlag("status", "girlfriend"),
            MaxCounter("pregnant", 8),
            ),
        'game.days_played - minami.flags.girlfriend_day >= 7',
        ],
    "do_once": True,
    "quit": False,
    })

    WakeUpEvent(**{
    "name": "minami_morningwood",
    "priority": 500,
    "label": "minami_morningwood",
    "duration": 1,
    "conditions": [
        IsHour(5, 9),
        IsDone("minami_practice_sex"),
        HeroTarget(IsGender("male"),
            Not(InFlag("slept_with", "minami")),
            Not(IsFlag("morningwood")),
            ),
        PersonTarget(minami,
            Not(IsHidden()),
            IsActivity("sleep"),
            MinStat("love", 160),
            MinStat("sexperience", 2),
            ),
        RoomTarget("bedroom5",
            NPCNumber(1),
            NPCInRoom("minami",),
            ),
        ],
    "chances": 20,
    "do_once": False,
    "once_month": True,
    })

    WakeUpEvent(**{
    "name": "minami_snooping",
    "priority": 500,
    "label": "minami_snooping",
    "conditions": [
        IsActiveHarem('home'),
        IsHour(5, 9),
        GameTarget(
            IsFlag("threesomelastnight"),
            IsFlag("ongoinghomeharem", False),
            ),
        PersonTarget(minami,
            Not(IsHidden()),
            MinStat("sexperience", 1),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    })

    InteractEvent(**{
    "name": "minami_murder_talk_bree",
    "label": "minami_murder_talk_bree",
    "do_once": True,
    "conditions": [
        PersonTarget(minami,
            IsActive(),
            ),
        PersonTarget("kylie",
            IsFlag("killed", "bree")
            ),
        ],
    })

    InteractEvent(**{
    "name": "minami_murder_talk",
    "label": "minami_murder_talk",
    "do_once": True,
    "conditions": [
        PersonTarget(minami,
            IsActive(),
            ),
        PersonTarget("kylie",
            Not(IsHidden()),
            IsFlag("schedule", "jail"),
            ),
        ],
    })

    SpecificTalkSubject(**{
    "name": "bree_talk_minami",
    "display_name": "About Minami",
    "label": "bree_talk_minami_01",
    "duration": 0,
    "icon": "button_minami",
    "conditions": [
        IsDone("minami_event_02"),
        Not(IsDone("minami_event_03")),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(bree,
            IsActive(),
            ),
        PersonTarget(minami,
            IsFlag("nomovein", False)
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "sasha_talk_minami",
    "display_name": "About Minami",
    "label": "sasha_talk_minami_01",
    "duration": 0,
    "icon": "button_minami",
    "conditions": [
        IsDone("minami_event_02"),
        Not(IsDone("minami_event_03")),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(sasha,
            IsActive(),
            ),
        PersonTarget(minami,
            IsFlag("nomovein", False)
            ),
        ],
    "do_once": True,
    })


label minami_murder_talk_sasha:
    "It's been a couple of days since it happened, since Kylie broke in and did what she did."
    "There's a cloud hanging over the house, of course there is, with rape and murder involved."
    "And nobody seems to want to talk to anyone else, just keep their grief to themselves."
    "I'd be more than happy with that, were it just myself that I had to be worried about."
    "After all, it's not like I was merely a witness to the awful things Kylie did that night."
    "But I've never been anything other than protective when it comes to Minami."
    "And I almost forget about my own trauma as I become ever more concerned for my little sister."
    "It's made worse by the fact that I can tell she's deliberately avoiding me."
    "Which makes me begin to think that she's been far more deeply affected than I suspected."
    show minami c sad with dissolve
    "So in the end, there's nothing I can do other than sit Minami down and make her talk to me."
    mike.say "Minami..."
    show minami c surprised
    minami.say "Huh..."
    minami.say "Oh, hey, big bro!"
    show minami c sad
    minami.say "How are you holding up?"
    "There she goes again, trying to make the conversation about me."
    "I'm sure that she's using her concern as a shield to hide behind."
    mike.say "I...I'll be okay, Minami."
    mike.say "I'm sure I'll get over it in time."
    "Minami nods at this, but she doesn't look like I've convinced her."
    "In fact, she seems ready to jump in and question what I just said."
    "And so I make sure that I beat her to it."
    mike.say "Actually, it was you that I wanted to talk about."
    show minami c surprised
    show fx exclamation
    "Minami's eyes go wide with surprise."
    minami.say "Wh...why would you want to do that?"
    minami.say "I'm fine, big bro - trust me!"
    hide fx
    "I shake my head, refusing to be so easily turned aside."
    mike.say "It's okay, Minami."
    mike.say "I know you're trying to be strong for me."
    mike.say "But I won't be fine until I know that you're fine."
    mike.say "Or that you're not..."
    show minami c normal
    "For a moment I'm sure that Minami will keep up the act."
    show minami c sad
    "But then I see the fact that her lip is quivering and her eyes are watering."
    show minami c cry close with hpunch
    "All at once, she lets out a helpless wail and throws her arms around me."
    "I'm not prepared for the move, but I soon recover and return the gesture."
    mike.say "Hey..."
    mike.say "Hey there, it's okay."
    mike.say "I won't let anyone hurt you, not ever."
    "Minami clings even more tightly to me, as if she's never going to let go."
    "And I have to admit, being able to offer her comfort feels pretty good."
    "The knowledge that she needs me and I'm useful helps to lessen my own traumatic thoughts."
    minami.say "Oh, big bro..."
    minami.say "That horrid girl!"
    minami.say "What she did to you was awful!"
    minami.say "And she killed poor Sasha too!"
    mike.say "This place won't be the same without her, I know that."
    mike.say "But Sasha wouldn't have wanted us to be sad forever, Minami."
    mike.say "Remember how tough she was?"
    mike.say "She'd have told us to get over it and not let Kylie win."
    show minami c sad
    "I hear Minami sniffle and snuffle against my shoulder."
    "But then I feel her nod as well."
    minami.say "We have to be strong for [bree.name] too!"
    minami.say "She's like my big sister, you know?"
    mike.say "We'll get through this together, Minami."
    mike.say "No matter how long it takes, we will - I promise you that."
    "I make no effort to break the hold that Minami has on me."
    "And I just keep on returning the gesture with just as much enthusiasm."
    "It feels like as long as I keep hold of Minami, everything will be okay."
    scene bg black with dissolve
    return

label minami_murder_talk_bree:
    "The atmosphere around the house has been tense, nobody wanting to talk too much."
    "Which, when you consider the nature of what Kylie did when she broke in..."
    "Well, let's just say that everyone's been trying to come to terms with it ever since."
    "I know that my housemates are trying to give me all the space I need to handle it too."
    "But still can't keep from feeling guilty when I see them, like I should be doing something."
    "It's Minami that causes me the most concern though."
    "She's always been someone that I've done my best to protect, to shield from harm."
    "Sure, she wasn't involved in the violence that took place that night."
    "But that doesn't mean she hasn't been affected by it in a very real sense."
    "And in the end, I feel that I have to sit her down and talk about it all."
    show minami c sad with dissolve
    mike.say "Minami..."
    show minami c surprised
    show fx exclamation
    mike.say "Have you got a spare minute?"
    "Minami looks surprised at the sound of my voice, like she was miles away."
    "But I soon see the mask that she's been putting on replace that expression."
    show minami c happy
    "And a moment later she appears to be all sunshine and rainbows."
    minami.say "Oh, hey, big bro!"
    minami.say "Sure thing - I've always got time for you!"
    "She cocks her head to one side as she says this."
    show minami c sad
    "And her face becomes solicitous and concerned."
    minami.say "You want to talk about what happened?"
    "I nod, trying to ignore the way she's making this about me."
    "All that'll make me feel better right now is knowing how she's feeling herself."
    mike.say "Yeah, Minami."
    mike.say "I just wanted to ask how you're bearing up?"
    show minami c normal
    "Minami wrinkles her nose and then shakes her head, as if amused."
    minami.say "Oh, don't worry about me, big bro."
    minami.say "I'm tougher than I look!"
    mike.say "If you say so, Minami."
    mike.say "I...I'm devastated by what that psycho did to [bree.name]."
    mike.say "But I feel guilty because..."
    mike.say "Well, because I'm also glad she didn't hurt you!"
    show minami c surprised
    "Minami stares at me in silence, her eyes growing wider by the second."
    "I can tell that she was expecting this chat to be all about other people."
    "After all, [bree.name] and I were the ones that Kylie actually attacked."
    "I don't think she's prepared for the conversation to be about her."
    "Minami opens her mouth to say something, but no words come out."
    "I can see that her lip is already starting to quiver."
    "And then she finally breaks."
    show minami c cry close with hpunch
    "Minami pretty much throws herself against me, burying her head into my chest."
    "She's sobbing and sniffling as she clings to me, shaking with emotion."
    "I wrap my arms around her petite frame, holding her close while she cries."
    mike.say "Hey...hey..."
    mike.say "It's okay, Minami - I'm here for you."
    mike.say "I won't let anyone harm a hair on your head."
    "Minami lifts her head a little, just enough for me to hear her speak."
    minami.say "I...I miss [bree.name], big bro."
    minami.say "She was so fun and so pretty too."
    minami.say "She was like my big sis!"
    minami.say "But I couldn't do anything to save her!"
    "All I can do is hold Minami and let her cry it out."
    "The truth is that I really do feel guilty, just like I said."
    "I'd give anything to have [bree.name] back, anything at all."
    "But all I can think about is the need to keep Minami safe right now."
    "The mere thought that the same thing could happen to her..."
    "It's just too much."
    "And so I make a silent vow to protect her with my life from now on."
    scene bg black with dissolve
    return

label minami_murder_talk:
    "It's been a while since the night when everything went down."
    "But it'd be totally wrong to say that things are getting back to normal."
    "After what happened, I don't think this place is ever going to be the same again."
    "So it's more like we're all trying to adjust to the new normal."
    "And even though I was right in the middle of it all..."
    "There's someone else that I'm more worried about right now."
    show minami c sad at center, zoomAt(1.0, (640, 720)) with dissolve
    "Of course that's Minami."
    "Mercifully she didn't see or hear anything on the actual night."
    "But she still lives under the same roof where it all happened."
    "And as her adopted brother, I feel responsible for making sure she's okay."
    "More then once I get the impression that she's about to say something."
    "That she's on the brink of bringing up the subject with me."
    "Yet every time something seems to stop her."
    "It's almost like she's mustering her courage."
    "But then the nerves get the better of her."
    "I keep on leaving it, assuming that she'll be ready to talk about it soon."
    "Though I'm beginning to think that I should maybe raise the subject myself."
    show minami c sad at center, traveling(1.5, 1.0, (640, 1040))
    "Which, oddly enough, is the very moment Minami seems to find her own voice."
    minami.say "Big Bro..."
    mike.say "Oh..."
    mike.say "Hey, Minami!"
    mike.say "Are you okay?"
    "Minami looks a little bashful for a moment."
    "And she shakes her head, dismissing my concerns."
    show minami c surprised
    show fx exclamation
    minami.say "Of course I am, Big Bro!"
    minami.say "I'm the one that should be checking up on you."
    minami.say "Especially after what you've been through!"
    if kylie.flags.rape and (not kylie.flags.killed == 'bree' and not kylie.flags.killed == 'sasha'):
        "The mere mention of what happened to me on that night hits me like a jolt."
        "Almost like being reminded is causing me physical pain."
        show minami c sad
        "I do the best I can to hide it, but Minami knows me too well for that to work."
        "She hurries over to me, opening her arms to give me a hug."
        show minami c sad at backforth(1.0, 10, 0)
        "But at the last moment she seems to remember what happened."
        "And she holds back, worried she might be doing the wrong thing."
        minami.say "I'm sorry, Big Bro..."
        minami.say "I just thought that after...what happened..."
        minami.say "You might not want to be touched?"
        "By way of answer, I shake my head."
        "And I open my arms wide."
        mike.say "I'll make an exception for you, Minami."
        show minami c normal
        "This seems to satisfy Minami's worries."
        "And she almost leaps into my arms."
        "For a while, all she does is cling onto me."
        "It doesn't take long for me to start feeling better."
        "The simple physical contact satisfying me on a level words never could."
        "Hell, I think I can even start to feel the stirring of something else inside of me too."
        "I know that this isn't the time or the place."
        "But having Minami so close to me is kind of getting my libido going too!"
        "Which is a relief."
        "Because there was a time that I thought Kylie might have killed it off for good."
        "When Minami finally lets go of me, it's not like that feeling vanishes either."
        "Which I also choose to take as a positive sign."
    elif not kylie.flags.rape and (kylie.flags.killed == 'bree' or kylie.flags.killed == 'sasha'):
        "The mere mention of what happened on that night hits me like a jolt."
        "Almost like being reminded is causing me physical pain."
        show minami c sad
        "I do the best I can to hide it, but Minami knows me too well for that to work."
        "She hurries over to me, opening her arms to give me a hug."
        show minami c normal at backforth(1.0, 10, 0)
        "I open my arms to return the gesture, pulling her body against mine."
        "And this might make me seem like some kind of creep, given the circumstances."
        "But having Minami so close to me is kind of getting my libido going too!"
        "Which is a relief."
        "Because there was a time that I thought Kylie might have killed it off for good."
        "When Minami finally lets go of me, it's not like that feeling vanishes either."
        "Which I also choose to take as a positive sign."
        mike.say "Thanks, Minami..."
        mike.say "I really needed that!"
        show minami c happy
        minami.say "Anytime, Big Bro!"
        minami.say "I'm always available for hugs!"
        if kylie.flags.killed == 'bree':
            mike.say "The problem is that I can't stop thinking about Bree."
        elif kylie.flags.killed == 'sasha':
            mike.say "The problem is that I can't stop thinking about Sasha."
        "At the mere mention of her name, Minami's face falls."
        show minami c normal
        minami.say "Me too!"
        minami.say "This place is never going to be the same again, is it?"
        if kylie.flags.killed == 'bree':
            minami.say "I mean, I keep expecting to see her hogging the Z-Box!"
        elif kylie.flags.killed == 'sasha':
            minami.say "I mean, I keep expecting to hear her playing her rock music super-loud!"
        show minami c sad
        minami.say "But then I realise that she's gone."
        minami.say "And that's never going to happen again."
        "I put an arm around Minami's shoulder."
        "And she responds by leaning her weight against me."
        "I have no idea how to handle something like this."
        "This is the first time that Minami's had to deal with the death of an actual human being."
        "Even worse, it happened as a result of violence and in the house where she's living."
        mike.say "I know, Minami..."
        mike.say "I keep thinking that I see her turning a corner in the house."
        mike.say "Or I swear I hear her in a room I'm walking into."
        mike.say "But when I get in there, she's not there, obviously!"
        show minami c normal
        minami.say "Things are going to be weird for a time..."
        minami.say "Aren't they?"
        mike.say "I guess so, Minami."
    elif kylie.flags.rape and (kylie.flags.killed == 'bree' or kylie.flags.killed == 'sasha'):
        "The mere mention of what happened to me on that night hits me like a jolt."
        "Almost like being reminded is causing me physical pain."
        show minami c sad
        "I do the best I can to hide it, but Minami knows me too well for that to work."
        "She hurries over to me, opening her arms to give me a hug."
        show minami c sad at backforth(1.0, 10, 0)
        "But at the last moment she seems to remember what happened."
        "And she holds back, worried she might be doing the wrong thing."
        minami.say "I'm sorry, Big Bro..."
        minami.say "I just thought that after...what happened..."
        minami.say "You might not want to be touched?"
        "By way of answer, I shake my head."
        "And I open my arms wide."
        show minami c normal
        mike.say "I'll make an exception for you, Minami."
        "This seems to satisfy Minami's worries."
        "And she almost leaps into my arms."
        "For a while, all she does is cling onto me."
        "It doesn't take long for me to start feeling better."
        "The simple physical contact satisfying me on a level words never could."
        "Hell, I think I can even start to feel the stirring of something else inside of me too."
        "I know that this isn't the time or the place."
        "But having Minami so close to me is kind of getting my libido going too!"
        "Which is a relief."
        "Because there was a time that I thought Kylie might have killed it off for good."
        "When Minami finally lets go of me, it's not like that feeling vanishes either."
        "Which I also choose to take as a positive sign."
        mike.say "Thanks, Minami..."
        mike.say "I really needed that!"
        show minami c happy
        minami.say "Anytime, Big Bro!"
        minami.say "I'm always available for hugs!"
        show minami c normal
        if kylie.flags.killed == 'bree':
            mike.say "The problem is that I can't stop thinking about Bree."
        elif kylie.flags.killed == 'sasha':
            mike.say "The problem is that I can't stop thinking about Sasha."
        "At the mere mention of her name, Minami's face falls."
        minami.say "Me too!"
        minami.say "This place is never going to be the same again, is it?"
        if kylie.flags.killed == 'bree':
            minami.say "I mean, I keep expecting to see her hogging the Z-Box!"
        elif kylie.flags.killed == 'sasha':
            minami.say "I mean, I keep expecting to hear her playing her rock music super-loud!"
        show minami c sad
        minami.say "But then I realise that she's gone."
        minami.say "And that's never going to happen again."
        "I put an arm around Minami's shoulder."
        "And she responds by leaning her weight against me."
        "I have no idea how to handle something like this."
        "This is the first time that Minami's had to deal with the death of an actual human being."
        "Even worse, it happened as a result of violence and in the house where she's living."
        mike.say "I know, Minami..."
        mike.say "I keep thinking that I see her turning a corner in the house."
        mike.say "Or I swear I hear her in a room I'm walking into."
        mike.say "But when I get in there, she's not there, obviously!"
        show minami c normal
        minami.say "Things are going to be weird for a time..."
        minami.say "Aren't they?"
        mike.say "I guess so, Minami."
    "Minami lets out a massive sigh."
    "And I get the feeling there's a whole lot of emotion tied up in it."
    show minami c sad
    minami.say "I..."
    minami.say "I just can't believe that Kylie's ended up in jail."
    minami.say "Someone I used to know is doing time for all that stuff!"
    "For a moment I'm confused by what Minami's saying."
    "But then I remember that she and Kylie go way back."
    "I think they were even friends while they were at school."
    mike.say "I suppose you never really know some people, Minami."
    mike.say "They keep things hidden, deep down inside of them."
    minami.say "You're right, Big Bro..."
    minami.say "I mean, Kylie was always super-intense."
    minami.say "But everyone could be that way about something that mattered to them."
    "Minami pauses, looking at me in an odd manner."
    "Like she's seeing me in a different light all of a sudden."
    "Or else noticing something that's always eluded her before now."
    minami.say "It's just weird that for Kylie..."
    minami.say "That was you, Big Bro!"
    mike.say "Tell me about it!"
    scene bg black with dissolve
    return

label minami_angela_conversation:
    "After overhearing the call between my parents, I can't help feeling stunned by what they actually said."
    "Well, technically I only heard my Mom's side of the conversation, but it was still enough to shock me."
    "And try as I might, there's no way I can even begin to make sense of the thoughts running around inside of my head."
    "More than once I tell myself that it simply can't be true, that I must have misheard them or misunderstood."
    "But no matter how hard I try, I still come back to the conclusion that I wasn't mistaken at all."
    "And the worst thing is that I have absolutely no idea what that means for Minami and myself either!"
    "Do Mom and Dad really know about what's happened between the two of us since she moved in here?"
    "If that's the case, then why do they seem to be chatting about it on the phone?"
    "And just what the hell did Mom mean when she said that she'd picked Minami to be my 'perfect wife'?!?"
    "All of this was made that much worse on account of the fact that I was left to struggle with it on my own."
    "Minami took off before Mom had wrapped up the call, and she's been avoiding me ever since."
    "That means that I don't really know how much she heard, which complicates things too."
    "My guess is that hunting Minami down and making her talk to me would only make matters worse."
    "And I'm not about to go marching up to Mom and demand to know what's going on either."
    "So I choose the only other option I can think of, and just pretend like nothing happened."
    "It takes a while, and I spend almost every moment of that time with my mind racing."
    show minami sad with dissolve
    "But the payoff finally comes when Minami sidles up to me in silence."
    "I look her in the eye, but keep silent, letting her make the first move."
    "She looks sheepish, biting her lip as if gathering the will to speak."
    minami.say "H...hey, big bro."
    mike.say "Hey, Minami."
    mike.say "Are you okay?"
    show minami annoyed
    minami.say "If you mean okay like - yeah, but not really."
    minami.say "I'm okay like that."
    mike.say "Hmm..."
    mike.say "I'm okay like that too, Minami."
    show minami normal
    "Minami sighs a little, but then she actually smiles at me."
    "It's small and pretty weak, but it has an almost immediate effect."
    "I feel myself smiling too, drawing strength from just having her next to me again."
    "All thoughts of how she left me alone simply drain away, not seeming to matter anymore."
    mike.say "How much of it did you hear?"
    minami.say "Erm..."
    minami.say "The last thing I remember was Mom talking about wedding bells."
    "I nod, thankful to know that we're at least on the same page in that respect."
    show minami sad
    minami.say "I...I'm sorry I ran away, big bro."
    minami.say "I was scared by what I heard!"
    "I shake my head, dismissing her apology."
    mike.say "It's fine, Minami."
    mike.say "Don't worry - I understand."
    "I guess I was being harsh on her for running out on me."
    "I mean, it was pretty weird for me to hear my Mom talking like that."
    "But it must have been so much worse for Minami."
    "All that crazy stuff about her being picked to be my wife!"
    "And coming from someone she should have been able to trust too."
    "I can't even begin to imagine how that must have made her feel."
    minami.say "What does it mean, big bro?"
    minami.say "What does any of it mean?"
    "I find myself shaking my head again, not sure of what to tell her."
    mike.say "I wish I knew, Minami."
    mike.say "But one thing I can tell you is that I didn't know either."
    mike.say "It's really important for me to know you believe that, yeah?"
    show minami normal
    "Minami takes a firm hold of my hand, leaning against me as she does so."
    "Like the smile beforehand, it's a small gesture."
    "But in the exact same way, it serves to reassure me again."
    minami.say "I believe you, big bro, honestly I do."
    minami.say "You know, why, don't you?"
    minami.say "Because you wouldn't have tried so hard to resist me otherwise!"
    minami.say "But...but I'm still scared, big bro."
    minami.say "Scared of what all this means for us..."
    "There's an unconscious pang in my stomach at the mere mention of our relationship."
    "And I instinctively feel angry at my parents for what they've done."
    "Angry that their actions could ruin what already exists between Minami and I."
    "Not to mention the irony that it seems they were scheming in secret to make the exact same thing happen!"
    mike.say "I know, Minami, I know."
    mike.say "I can't believe Mom and Dad would do something like that."
    mike.say "It's crazy to think that they could've been planning out the whole of our lives."
    mike.say "Right from when we were little kids until now!"
    minami.say "I don't know what to believe anymore, big bro."
    minami.say "Is anything that they told us true?"
    "The implications of Minami's question don't hit me straight away."
    "But then my mind begins to turn them over, slowly at first and then with ever more speed."
    mike.say "What are you saying, Minami?"
    mike.say "Are we still talking about the telephone call?"
    minami.say "Think about it, big bro!"
    "As she uses that familiar term of endearment, Minami's smile becomes almost melancholy."
    minami.say "I keep calling you that out of habit - but is it really true?"
    minami.say "If they kept this crazy scheme from us all these years."
    minami.say "Then what else have they been lying about too?"
    mike.say "Minami..."
    mike.say "I don't think I like where this is going!"
    show minami angry
    "Minami looks at me with genuine disbelief in her eyes."
    minami.say "Jesus, big bro!"
    minami.say "Who cares if you like it or not?!?"
    minami.say "We just found out our Mom and Dad are playing some kind of sick game with us!"
    minami.say "And what if they managed to pull it off, huh?"
    minami.say "Did you ever think of that?"
    mike.say "What are you trying to say, Minami?"
    minami.say "Isn't it obvious, big bro?"
    minami.say "What if this..."
    minami.say "What if us being together..."
    minami.say "What if it's just because of what they did?"
    mike.say "Does that even matter, Minami?"
    mike.say "I know how I feel about you, it's just about all I DO know right now."
    minami.say "Well..."
    minami.say "Well of course YOU do."
    minami.say "They picked me out for you, didn't they!"
    hide minami with dissolve
    "And with that, Minami turns and runs away for the second time in such a short while."
    "But this time, I feel so much more alone than I did the last that it actually hurts."
    return

label minami_angela_acceptation:
    "After what happened the last time I spoke to Minami, I find myself leaving her alone for a second time."
    "Which, under the circumstances of what we discussed and what we said to each other, is the last thing I want to do."
    "But it's not as if I feel that I have any kind of choice in the matter, not with what we just discovered about our parents."
    "I had hoped that when we got together to chew it over that first time, we could make some kind of sense out of it all."
    "Maybe that was hoping for a miracle, what with us now knowing that Mom and Dad have been manipulating us since we were kids."
    "All the same, the last thing that I wanted was for us to leave it in a place where we were even less sure of where we both stood."
    "But that's what happened, with Minami wondering if what we have together was ever real in the first place."
    "Or if we were only forced together thanks to Mom and Dad meddling with our lives this whole time."
    "Not knowing what to expect, all that I can do is hope for the best while preparing for the worst."
    "Which is why I'm ready to hear whatever Minami has to say when she finally chooses to confront me."
    "Believe me, the very last thing that I want is for her to tell me that it's all over."
    "But as painful as that would be, not knowing what Minami wants is much worse."
    show minami sad with dissolve
    minami.say "B...big bro?"
    mike.say "Yeah, Minami."
    minami.say "Are...are you mad at me?"
    "I give Minami a sad smile at this."
    "But I shake my head at the same time."
    mike.say "No, Minami, I'm not mad."
    mike.say "I'm just worried about what you're going to say next."
    "Minami clenches her fists and clutches them to her chest."
    show minami normal blush
    "The meek look on her face is instantly replaced by one of passionate concern."
    minami.say "Oh, big bro!"
    minami.say "I can't stand to see you so sad!"
    minami.say "Ooh, how could I have been so stupid?!?"
    mike.say "Wh...what do you mean, Minami?"
    mike.say "What are you trying to tell me?"
    minami.say "All this time I was feeling so sorry for myself."
    minami.say "I was just being selfish - I wasn't thinking of you at all!"
    mike.say "No, Minami."
    mike.say "Don't ever think that about yourself."
    mike.say "We just found out that Mom and Dad did all of that stuff to you."
    mike.say "You have every right to feel mad - I know that I do!"
    show minami happy
    minami.say "Oh, big bro - you're SO good to me!"
    minami.say "This is going to sound crazy, I know it."
    minami.say "But since we found out...well..."
    minami.say "I've been feeling glad that Mom and Dad did what they did."
    minami.say "At least a little..."
    "I find myself staring at Minami, my mouth hanging open in surprise."
    "Did she actually just say what I think she did?!?"
    mike.say "Minami, you can't actually mean that?"
    minami.say "No, no, no..."
    minami.say "You have to understand, big bro."
    minami.say "I'd still rather it hadn't happened, believe me."
    minami.say "But whenever I think about it, I get sad at the thought of being without you."
    "I find myself stepping forward and putting my hands on Minami's shoulders."
    "It's not a conscious move, but I can't help the need to hold her."
    mike.say "Minami, they used you."
    mike.say "And that's wrong, no matter how much we want the end result."
    show minami close
    "Minami takes a step forward of her own, wrapping me in her arms at the same time."
    "The sensation is instantly comforting, almost making me forget everything else."
    minami.say "No, big bro, you're wrong."
    minami.say "Mom and Dad could have set all of this up."
    minami.say "They could have meant for us to sleep together."
    minami.say "They could have wanted us to end up getting married."
    minami.say "But the one thing that they could never do was make me fall in love with you."
    minami.say "Because you did that yourself."
    hide minami
    show minami kiss
    with dissolve
    $ minami.flags.kiss += 1
    "I feel the warmth of Minami's hands on my cheeks as she pulls me down towards her."
    "And when she plants a kiss on my lips, I'm powerless to resist."
    "Before I know what's happening, I'm kissing her back with ever more passion."
    "She's right, she's damn right."
    "Why couldn't I see that before?"
    "Mom and Dad might have manipulated us in the past."
    "But now we know the score, and that's all going to come to an end."
    "Minami and I can choose what happens from this point on - us and nobody else."
    "So if we choose to stay together out of genuine love for each other, that's all there is to it."
    "From now on, we're the ones that are going to be in control of our own lives."
    "And right now, I choose to hold on tight to the girl that I love."
    $ minami.flags.nopropose = False
    return

label minami_asleep:
    if samantha.room == game.room:
        show multisleep minamisam minami samantha
        "Minami and Sam are sleeping, I should leave before I wake them up..."
    else:
        show sleep minami
        "Minami is sleeping, I should leave before I wake her up..."
    $ game.room = "secondfloor"
    return

label minami_love_dating:
    if minami.love.max < 200:
        $ minami.love.max += 20
    if minami.love.max > 200:
        $ minami.love.max = 200
    return

label angela_visit:
    scene bg livingroom
    "Mom coming over to visit shouldn't really have been anything like a big deal."
    "Just a chance for her to check up on Minami, to see how she's settling in here."
    "Oh, and to catch up with her only son, of course."
    "What do you expect me to say - I love my Mom and I'm not ashamed to admit it!"
    show minami casual annoyed at right with easeinright
    "But for some reason, her imminent arrival seems to send Minami into a state of panic."
    show minami scared at right, hshake
    show fx exclamation at right
    pause 1.0
    show minami annoyed at left with move
    hide fx
    "So much so that she spends the days before Mom's arrival making sure every single thing is perfect."
    hide minami with easeoutleft
    "I mean, I know that we kind of had sex with each other a couple of days ago."
    "But there's a simple enough solution to that potentially awkward fact."
    "And that's that we just don't tell Mom about it."
    "That way, everyone's happy and the visit goes without a hitch."
    "So the day finally arrives, and Mom turns up pretty much when she's expected."
    scene bg house
    show angela casual at center
    with wiperight
    "As she pulls up in front of the house, Minami and I are there to greet her."
    show minami casual happy at left with moveinleft
    minami.say "MOM!"
    minami.say "It's SO great to see you!"
    show minami normal
    mike.say "Hey, Mom."
    mike.say "Same here - but maybe with a little less helium and sugar involved!"
    show angela happy
    angela.say "Ha, ha!"
    angela.say "Oh, I've missed how much you make me laugh, [hero.name]."
    show angela talkative
    angela.say "And you, Minami - the house is so quiet without you!"
    show angela normal
    "I guess I should take a moment to address the elephant in the room."
    "Or maybe the cougar in the driveway..."
    "Yeah, my Mom's hot - just get over it already."
    "In fact, it's something that I've always been oddly proud of, ever since I was a little kid."
    "Sure, my friends all had massive crushes on her when we were growing up."
    "But that kind of made me proud of her - that she was the most beautiful of all the Moms in the neighbourhood."
    "It made her seem all the more special to me, and it made me love her all the more too."
    "And it might be absence making the heart grow fonder, but right now she looks better than ever."
    "Ah, but don't go getting the wrong idea."
    "Me and Minami was only okay because she's my ADOPTED sister, okay?"
    "Right - I'm glad we got that settled."
    show bg livingroom
    show angela casual at left5
    show minami casual normal at right5
    with fade
    mike.say "You must be tired from the drive over here, Mom?"
    show minami talkative
    minami.say "Yeah, Mom - you should go in and sit down on the sofa."
    show minami happy
    minami.say "[hero.name] can get your bags from the car for you."
    show minami normal
    mike.say "Wha..."
    mike.say "Minami!"
    show minami tehe
    show angela happy at startle
    "Mom chuckles at the sight and sound of us suddenly squabbling in front of her."
    angela.say "Ah, now that reminds me of home!"
    angela.say "It's good to know that you two have been getting on so well."
    show angela talkative
    angela.say "[hero.name], it would be a great help if you could get my bags."
    angela.say "But I want you to help out too, Minami - okay?"
    show angela normal
    show minami a talkative
    "Together" "OKAY MOM!"
    scene bg house with fade
    "And just like that we both snap to attention, each eager to look good in our Mom's eyes."
    "She smiles and shakes her head, the affection she feels for us clear to see in her expression."
    "It's no surprise that I end up shouldering the heaviest of the bags that Mom's brought for her stay."
    "Minami takes her pick of the lightest, and then pretty much leaves the rest to me."
    scene bg door entrance at center, zoomAt(1.25, (640, 880))
    show minami casual at center, zoomAt(1.25, (640, 880))
    with fade
    "This means that I reach the front door after she's already been there for a couple of seconds."
    "At first I think that she's had a change of heart and is going to take at least one bag off me."
    mike.say "Thanks for the help, Min..."
    show minami c annoyed
    minami.say "Shh!"
    show minami c talkative
    minami.say "Just shut up and listen!"
    show bg door entrance at center, traveling(1.35, 0.3, (640, 940))
    show minami c annoyed at center, traveling(1.25, 0.3, (840, 880))
    "Puzzled by her strange reaction, I do as I'm told and glance over her shoulder into the house."
    scene bg livingroom
    show angela casual a pinch
    with blinds
    "Immediately I see that Mom's standing in the middle of the sitting room, rather than sitting down."
    "She has her mobile to her ear, and it appears that we've walked in half way through a call."
    show angela talkative a pinch
    angela.say "No, no - everything's fine, dear."
    show angela normal a pinch
    "Realising that she must be talking to Dad, I make to ask Minami what's up with her listening in."
    show bg door entrance at center, zoomAt(1.35, (640, 940))
    show minami casual c annoyed at center, zoomAt(1.25, (840, 880))
    with hpunch
    "But she silences me again, this time with a sharp elbow to the gut."
    mike.say "Ooh..."
    mike.say "Hey, what the..."
    show minami c vangry
    minami.say "Listen!"
    show minami c annoyed
    "Minami hisses the word, making me do as I'm told."
    scene bg livingroom
    show angela casual talkative a pinch
    with blinds
    angela.say "Of course they're behaving like they did back home."
    angela.say "But the bickering and fighting like kids is just for show, trust me."
    angela.say "Because I'm a woman too, and I KNOW the signs, dear - that's why!"
    show angela normal a pinch
    "Mom falls silent for a moment, nodding her head at whatever Dad's saying in the other end of the line."
    show angela protest a pinch
    angela.say "No, I'm not going to ask them about it just yet."
    angela.say "It could be too early, and that'd blow the whole thing."
    show angela talkative a pinch
    angela.say "We've waited decades for this to happen, dear."
    angela.say "So a couple of days isn't going to matter."
    angela.say "Just trust me - I was the one that picked Minami out in the first place."
    angela.say "I knew that she was the perfect wife for [hero.name] back then."
    angela.say "And I know it's still true now."
    show angela happy
    angela.say "Like I said, dear, trust me - we'll be hearing the sound of wedding bells soon enough!"
    show angela normal
    "It takes a couple of seconds for the implications of what I just heard to fully sink in."
    "But when it finally does, I feel like a massive weight is pressing down, threatening to crush me."
    show bg door entrance at center, zoomAt(1.35, (640, 940)) with blinds
    mike.say "Minami..."
    mike.say "Minami, is that true?"
    scene bg house with fade
    "When there's no answer to my question, I glance around, searching for Minami."
    "But she's nowhere to be found, and I see that I'm standing alone on the porch of the house."
    $ minami.love -= 180
    $ minami.love.max = 50
    $ minami.flags.topless = False
    $ minami.flags.naked = False
    $ minami.flags.giftslave_collar = False
    return

label minami_practice_blowjob:
    $ minami.flags.sisconDelay = TemporaryFlag(True, 1)
    show minami a hunt close
    minami.say "Hey there, big bro!"
    mike.say "Wha...what..."
    mike.say "H..Hey, Minami!"
    "Yeah, I know it looks pretty stupid on the surface of things."
    "Me, a grown man, jumping out of my skin at a couple of words from a girl of Minami's size."
    "But when you know what she's been making me do for her these past couple of days..."
    "Well, let's just say that you'd have a lot more sympathy for me if you knew, okay?"
    "Let's just say that my last attempt to educate her in the art of dating was pretty traumatic."
    "And since then, I've been living in fear of what she'll dream up next!"
    mike.say "What's up?"
    minami.say "I wanted to talk about my next lesson, big bro."
    "Of course she does!"
    mike.say "Ah..."
    mike.say "Don't you think we covered the important stuff already, Minami?"
    mike.say "The do's and dont's of dating, kissing one on one, even what a guy's junk looks like."
    mike.say "I'd say you're good to go!"
    show minami tehe
    "Minami smiles as she shakes her head."
    minami.say "Nice try, big bro!"
    minami.say "But you haven't got me past second base yet!"
    show minami hunt
    "Now I can feel myself actually starting to break out in a cold sweat."
    "Past second base - does she even know what that would involve?!?"
    "Wait a minute...maybe that's it!"
    "No one ever seems to know exactly what each of the four bases actually is."
    "If I'm lucky, Minami might think they're all stuff at the tamer end of the sexual spectrum."
    "And if not, I can always try to convince her that she's got it wrong."
    mike.say "Okay, Minami, okay."
    mike.say "Just indulge me a little here."
    mike.say "What exactly would you need to learn for third base?"
    show minami happy
    "Minami looks at me like I'm joking, smirking as she does so."
    minami.say "Big bro, don't be silly."
    minami.say "You know what third base is!"
    mike.say "Yeah, of course I do."
    mike.say "But I'm the teacher here, Minami."
    mike.say "So indulge me, yeah?"
    show minami tehe
    "Minami shakes her head again, but then nods in agreement."
    minami.say "Third base is oral, big bro."
    minami.say "So I need you to teach me the right way to give a blowjob!"
    show minami hunt
    "Shit - so much for her thinking third base is something less than X-rated!"
    "And from the look on her face, she's never going to let me tell her otherwise."
    mike.say "Ah...well..."
    mike.say "We could...we could use something for practice."
    mike.say "Like...like a carrot...or a cucumber maybe!"
    show minami annoyed
    minami.say "Aw, but, big bro - that won't work."
    minami.say "I need to know how to get a guy real hard too!"
    show minami hunt
    minami.say "I need to use your's for practice..."
    menu:
        "Refuse":
            mike.say "Jesus wept, Minami!"
            mike.say "You can't actually be wanting me to let you..."
            mike.say "To let you...practice..."
            mike.say "On me..."
            show minami annoyed
            "Minami frowns, already beginning to pout in response to my answer."
            "I can see that she's trying to think up a way round this, how to spin it in the direction she wants."
            minami.say "It's only for practice, big bro."
            minami.say "Just think of it like if a prostitute gave you a blowjob."
            mike.say "Yeah, that doesn't help all that much, Minami!"
            mike.say "I don't want to think of you giving head."
            mike.say "And treating you like a hooker just makes it that much worse!"
            show minami sad
            minami.say "Oh, please, big bro!"
            minami.say "You'd be helping me out so much."
            minami.say "And getting something nice at the same time!"
            mike.say "I said no, Minami, and I mean it."
            show minami angry -close
            minami.say "Urgh, you're SO unreasonable, big bro!"
            "And with that, Minami storms off, still muttering curses under her breath."
            $ minami.siscon -= 5
            $ hero.cancel_event()
        "Agree":
            "Sometimes I wonder if this is how all of the scoundrels and scumbags in the world got started."
            "Taking one more step at a time downwards, until they trip and land on their arses."
            "And from there, it's just an ever faster slide down the slippery slope to hell!"
            "But still, she does have a point."
            "These days, almost every guy she meets will expect her to know what she's doing down there."
            "Unless she hears it from someone like me, the criticism she gets could ruin her confidence for life!"
            mike.say "Jesus, wept, Minami!"
            mike.say "I just know I'm going to regret this..."
            show minami happy
            "Minami lets out a squeal of joy and grabs hold of my hand."
            show bg bedroom5 with fade
            "Without needing to be told, she pulls me towards her bedroom."
            "Obviously, I do nothing to stop her."
            "The last thing I need right now is someone else seeing what I'm about to let her do!"
            hide minami with dissolve
            "I lie down on her bed, undoing my flies."
            "And Minami lies down next to me, intently watching my every move."
            "The whole time trying not to think too much about what's going to happen next."
            show minami bj bedroom5 blush with fade
            "She lowers her head over me without pause or hesitation."
            "And the look of determination on her features makes her look extra cute..."
            "No, I have to stop thinking of her like that!"
            "The only reason that I'm doing this is to help her out."
            "I won't let myself take any pleasure from it."
            "It's then that I realise Minami's staring up at me, awaiting my instructions."
            mike.say "Ah, let's see..."
            mike.say "Be gentle, okay?"
            mike.say "Don't put more in your mouth than you can handle."
            mike.say "And don't be fooled by the name - suck all the way."
            show minami bj lick
            "Minami nods dutifully, already reaching out for my cock."
            show minami bj out
            "I needn't have worried about being able to rise to the occasion."
            "Despite my mental gymnastics over this idea, my body seems totally on board."
            "I always had a habit of getting an erection during inappropriate situations."
            "And for once, it's come in handy..."
            show minami bj close
            "Mercifully, Minami closes her eyes as she leans in to get started."
            "I try to think of something else, anything else."
            "But my eyes settle on her face as she begins to lick at the tip of my cock."
            "God but she's cute."
            "How did I never notice that before?!?"
            "She's fucking beautiful!"
            show minami bj suck -out
            "And she has my cock in her perfect mouth..."
            "Just like that, we step over an invisible boundary."
            "Minami's head starts to bob up and down, and I feel her efforts spreading through me."
            "And as they do, I know that things can never be the same between us again."
            "I thought that I'd have to coach her through each and every step of this."
            "But she's a natural, either having the perfect instinct, or else she's done this before."
            "All I can do is make approving sounds, urging her on the whole time."
            "Suddenly, I know that I'm about to cum."
            "It's not Minami's savant technique that's finished me off quickly though."
            "More the overwhelming mixture of desire and guilt that's currently churning up my guts."
            show minami bj out -suck
            "I reach down and pull Minami's head off of my cock."
            "She splutters in surprise, blinking up at me with wide eyes."
            show minami bj out cumshot with vpunch
            "And then I cum, straight into her unsuspecting face."
            show minami bj facial cum -cumshot
            "The semen paints strings of glistening white across Minami's nose and cheeks."
            show minami bj -out
            "Some of it even drips into her still open mouth."
            minami.say "Why did you make me stop, big bro?"
            minami.say "Did I do something wrong?"
            show minami bj swallow
            "I can't help gasping as I struggle to answer her question."
            mike.say "No...Minami..."
            mike.say "You...passed..."
            mike.say "Top...of...the...class..."
            scene bg black with dissolve
            $ game.room = "secondfloor"
            $ minami.flags.noDirtyText = False
            $ minami.siscon.max = 100
            $ minami.siscon += 5
    return

label minami_practice_sex:
    "I never used to be sure of just what people meant when they used the term 'down the rabbit hole' to explain the situation they were in."
    "Sure, I know it had something to do with a book in which a whole lot of weird shit happens to some girl called 'Alice'."
    "But there was nothing in my own experience that I could really apply it to, and so it didn't really mean anything to me."
    "Then I agreed to start helping Minami on her quest to get clued-up on the world of dating, romance and everything beyond."
    "And pretty soon I began to realise that it describes an ever stranger trip into an unfamiliar and trippy world."
    "It started out innocently enough, with me taking Minami out on a practice date."
    "But then she wanted to get into the more, shall we say...physical aspects of it all."
    "Teaching her how to kiss someone was crazy enough at the time, and left me feeling like I needed a shower."
    "And from there it escalated to her asking to be shown what the male anatomy looks like - if you know what I mean?"
    "At that point, I guess I should have known that I was already on a downward spiral into damnation."
    "A road to hell, paved with my own good intentions not to let my little sister suffer for lack of practical experience."
    "Next came the appeal for me to let her practice her technique for a blowjob on me."
    "All of which left me feeling like I must have suffered some kind of psychotic break."
    "And then just as I was thinking things might get back to normal, Minami corners me again..."
    show minami a casual happy with dissolve
    minami.say "Hey, big bro!"
    mike.say "Ah...hey, Minami..."
    mike.say "What do you want this time?"
    show minami close angry
    show fx anger
    "She frowns at this, as if offended at the assumption I just made."
    minami.say "How do you know I want something, big bro?"
    show minami normal
    minami.say "I could just want to say hi to my favourite housemate."
    "I note with interest that she calls me her housemate, rather than her brother."
    "It's enough to make me raise an eyebrow in interest, but also to call her bluff."
    mike.say "Point taken, Minami."
    mike.say "So, do you want something or not?"
    show minami happy
    minami.say "You got me, big bro."
    minami.say "I DO want something!"
    "I roll my eyes and let out a sigh of resignation."
    mike.say "Okay, Minami - spit it out!"
    "It's only after I utter the words that I become aware of the image they bring to mind..."
    show minami normal blush
    minami.say "Well, you know that you've been giving me these lessons?"
    mike.say "Yeah, Minami - how could I forget!"
    minami.say "And you know how they're kind of covering one base after another?"
    mike.say "Come on, Minami - get to the point!"
    show minami annoyed
    show fx exclamation
    minami.say "Geez, big bro!"
    minami.say "Will you let me finish before you jump down my throat?!?"
    mike.say "Just say it, okay?"
    show minami normal
    "Minami takes a deep breath, and then does as I ask."
    minami.say "What about sex, big bro?"
    mike.say "What about it?"
    minami.say "You know what I mean - how will I know what to...to do?!?"
    "Suddenly I feel like a black hole just opened up in the pit of my stomach."
    minami.say "So I was thinking maybe..."
    minami.say "Maybe you could show me how it's done?"
    menu:
        "Refuse":
            "That's it."
            "Right there - that's the final straw!"
            mike.say "Minami, listen to yourself for a minute."
            mike.say "Listen to what you just asked me to do!"
            show minami annoyed
            minami.say "Oh, come on, big bro!"
            minami.say "You'd just be helping me out, that's all!"
            mike.say "No, Minami, that's not it."
            mike.say "I'd be having sex with my own little sister."
            mike.say "There's a word for that, you know?"
            mike.say "They call it 'incest'!"
            show minami angry
            show fx anger
            "Minami shakes her head, desperately trying to talk me around."
            "And in a way, I have to admire her for having the front to even try."
            minami.say "That's only for when you're related, big bro."
            minami.say "We both know I was adopted - and if I wasn't, we could have met in the street!"
            mike.say "But we didn't, Minami."
            mike.say "We grew up together, and that's the whole point!"
            "Minami opens her mouth to argue for a second time."
            "But then she looks me in the eye and seems to think better of it."
            show minami sad
            minami.say "Ooh, big bro!"
            minami.say "You can be SO mean sometimes!"
            "And with that, she hurries away, leaving me to shake my head in disbelief."
            "She just basically asked me to have sex with her."
            "And she thinks I'm the one that's being mean by saying no?!?"
            $ minami.love -= 20
        "Accept":
            $ minami.sexperience += 1
            $ minami.flags.nosex = False
            "If only I hadn't already let myself get dragged into this mess."
            "Then that would probably have been the final straw."
            "But I'm already so deep into this thing that it doesn't actually sound all that crazy anymore."
            "And if I do this, then it'll finally be over, right?"
            "I mean, there's nothing more that she can ask of me after this, is there?"
            mike.say "I'm going to regret saying this, Minami."
            mike.say "But okay - if that's what you really want."
            show minami happy
            show fx heart
            "Minami doesn't say as much as a word."
            "She just takes me by the hand and begins to lead me towards my bedroom."
            "And all the way there, she's grinning like a Cheshire Cat..."
            scene bg bedroom1 with fade
            "The silence endures as we close the bedroom door behind us and strip off our clothes."
            "I try to keep it sterile and emotionless, but a mere glance at Minami tells me that'll be impossible."
            show minami naked blush with dissolve
            "She stand there for a couple of seconds, totally naked."
            "And then she climbs onto the bed and beckons for me to follow her."
            minami.say "Come on, big bro."
            "She pats the mattress beside her, and I can already feel my body moving to obey."
            "I lie down next to Minami, struggling and failing to keep from gazing at her body."
            "I always knew my little sister was cute."
            "But I never let myself acknowledge that she was so achingly beautiful."
            "So effortlessly sexy..."
            show minami hunt
            show fx exclamation
            minami.say "Ooh, hello there!"
            "Minami giggles, and I look down to see that my erect cock is rubbing against her thigh."
            minami.say "Looks like someone's ready to show me what he can do!"
            mike.say "I...well...yeah..."
            mike.say "It's not like I can help it, being this close to a sexy..."
            "I stop myself before I actually say it."
            "Before I openly admit that I find Minami pretty irresistible."
            mike.say "Anyway..."
            mike.say "Let's get down to business, shall we?"
            "Minami nods happily, giving me a mock salute as she does so."
            minami.say "Okay - let's do it, big bro!"
            "Oh god..."
            "Here goes nothing!"
            $ CONDOM = False
            if hero.has_condom():
                mike.say "Safety first, Minami."
                "I point at the condoms on the bedside table, and she obediently leans over and grabs one."
                mike.say "Okay, push the condom away from the edge before you rip the packet, otherwise you might tear it."
                "Minami nods, taking excessive care to remove the condom without damaging it."
                mike.say "Now, pinch the bit at the top to keep the air out."
                mike.say "Then roll it over..."
                "I pause, steeling myself for what I have to say next."
                mike.say "Roll it over my cock!"
                "Minami does as she's told, concentration written all over her face."
                "Shit..."
                "Her hands feel so good on me!"
                "It's all I can do to keep from letting out a moan of pleasure."
                "Once the condom is on, Minami looks up at me, eagerly awaiting my next instruction."
                $ CONDOM = hero.use_condom()
            mike.say "Ah...right..."
            mike.say "This is where you might need to use some lube!"
            "A curious frown appears on Minami's face as her hand darts between her thighs."
            minami.say "Mmm..."
            minami.say "I don't think so, big bro."
            minami.say "I'm pretty wet down there already!"
            "I can't help letting out a gasp at the mere thought of Minami stroking her own wet pussy."
            mike.say "Urgh..."
            mike.say "Okay, Minami..."
            mike.say "You need to get on top of me."
            "I figure that it's best for her to do this cowgirl."
            "That way she can be the one in control and she'll learn the most."
            "Better that than laying passive on her back and leaving it all to the guy."
            "But the only thing is, this time, the guy in question is me!"
            hide minami
            if CONDOM:
                show minami cowgirl condom
            else:
                show minami cowgirl
            with fade
            "Minami does as she's told, eyeing my cock the whole time."
            "She straddles my waist easily enough."
            "And for the first time I feel the slick sensation of her pussy against my naked skin."
            minami.say "Oh, big bro..."
            minami.say "Are you SURE I can fit that inside of me?"
            minami.say "It's SO big up close!"
            "Well, at least I know she can pull off talking dirty!"
            "Minami takes hold of my cock with her hand."
            "And then she raises herself up as she guides it between her legs."
            show minami cowgirl vaginal surprised
            "As she presses the head against the lips of her pussy, looking to me for my approval."
            "This is it, the point of no return."
            "I can stop her from doing it with no more than a word."
            "But then I find myself nodding, almost without knowing that I'm doing it!"
            "I see Minami smile, and then return the nod herself."
            "Then she pushes herself down and onto me..."
            show minami cowgirl vaginal orgasm
            minami.say "Ah...Aah..."
            minami.say "It...it hurts!"
            mike.say "Th...that's your hymen, Minami..."
            mike.say "It has to...to tear!"
            "And then it does, without warning."
            "Minami sinks down, her whole weight pressing her onto my cock."
            show minami cowgirl vaginal ahegao
            minami.say "Oh...oh fuck!"
            minami.say "Big bro...it feels so...so good!"
            "I have to admit that it feels pretty good from where I'm sitting too!"
            "And there's no need to tell Minami what to do, as she now reacts on pure instinct alone."
            "She grabs hold of me with both hands, starting to ride me for all she's worth."
            "I put my hands out and take a hold of her too, meaning to keep her steady."
            show minami cowgirl up
            "But then she surprises me by grabbing my wrists and thrusting my hands onto her bare breasts."
            "Each one fits almost perfectly into the palms of my hands."
            "And I can feel just how stiff her nipples are right now."
            "I don't so much deliberately squeeze them, as let Minami push against me."
            "Which means that they're pressed into my palms with all the force she can summon."
            show minami cowgirl speed
            minami.say "I love it, big bro..."
            minami.say "I love your cock inside of me!"
            "I can't take much more of this, as Minami's pounding me as if her life depended on it."
            "Already I can feel myself cumming, and I have no idea if she's even close to doing the same."
            "Instinct takes over now, and I tear my hands away from Minami's breasts to seize her by the waist."
            "Suddenly I'm the one thrusting into her with all my might."
            "She's practically screaming by this point, almost in time with my pushing into her."
            show minami cowgirl creampie with vpunch
            if not CONDOM:
                $ minami.impregnate()
            "And when I lose it, she arches her back and wails without restraint."
            minami.say "Ah...yeah...yeah..."
            minami.say "Make me cum, big bro!"
            "When it's all over, Minami flops down onto me, wriggling and writhing with my cock still inside of her."
            "She slides off of it, her entire body as slick with sweat as my own."
            mike.say "Well...Minami..."
            mike.say "Did you...learn what...you wanted to?"
            minami.say "Phew!"
            minami.say "Yeah, big bro."
            minami.say "I learned EVERYTHING I needed to know..."
            scene bg black with dissolve
    return

label minami_meet_alexis:
    show bg mall1
    "I was sure that I'd ticked off all of the essential things that I needed to educate Minami on in and around town."
    "But it seems that Minami and I have a very different definition of the word 'essential'."
    show minami with dissolve
    "Which is how we end up strolling around the local mall, her arm wrapped in mine and a huge smile on her face."
    "Her enthusiasm is infectious though, and I soon find that I'm enjoying myself far more than I expected to."
    show minami surprised
    show fx exclamation
    minami.say "Oh...my...god!"
    mike.say "What is it, Minami?"
    mike.say "What's the matter?"
    hide fx
    show minami happy
    minami.say "You have a 'WOW Sushi' here!"
    minami.say "That is so cool - the mall back home never had one of those!"
    mike.say "Well, this is pretty big city, Minami."
    mike.say "And we did grow up in a small town..."
    show minami normal
    "I'm not sure that Minami hears my reply, or pays it much attention even if she does."
    "As a couple of seconds later, I find myself being pulled towards the next shiny thing in her field of vision."
    "The best I can do is just shrug, and try to see this place from her point of view."
    "Sure, to me it's just the same old mall that I've been coming to for a couple of years now."
    "But to Minami, it's a whole new world of undiscovered delights and consumerist wonders."
    show minami happy
    minami.say "Thanks SO much for bringing me here, big bro!"
    minami.say "This is a real fun date."
    show minami normal
    "What...wait!"
    "Did she just use the word 'date' to describe what we're doing here?"
    mike.say "Ah, Minami..."
    mike.say "I don't exactly know what I'd call this."
    mike.say "But we're definitely not on a date!"
    "Minami smiles at me and rolls her eyes, amused at my reaction."
    show minami happy
    minami.say "Oh lighten up, big bro!"
    minami.say "No one here knows that I'm your sister."
    minami.say "We just look like a pretty girl and a cute guy out together, having fun."
    minami.say "And what else would you call that but a date, huh?"
    "I have to admit that she's got a point!"
    show minami normal
    alexis.say "At least one person here knows you're his sister, Minami!"
    "I turn around at the sound of the voice, genuinely surprised to hear it."
    show minami surprised at center, vshake
    "But Minami practically jumps out of her skin, letting out a wail of shock."
    "It's almost as if she's been caught in the act of misbehaving and fears that a punishment might follow."
    show alexis at right5
    show minami at left5
    with moveinright
    "I know that I shouldn't, but I laugh as soon as I see that the mysterious voice belongs to Alexis."
    mike.say "Hey, Alexis."
    alexis.say "Hey, [hero.name]."
    alexis.say "Hello, Minami - long time no see, yeah?"
    "Minami seems to recover quickly from her initial shock."
    show minami annoyed
    "She crosses her arms over her chest and frowns back at Alexis."
    minami.say "Not long enough, if you ask me!"
    minami.say "I don't know how you can speak to my poor big bro."
    minami.say "Not after what you did to him!"
    mike.say "Come on, Minami."
    mike.say "That was years ago."
    mike.say "Alexis and I were just a couple of kids back then."
    show alexis happy
    alexis.say "Yeah, and some of us have grown up since then!"
    "The tone in which Alexis says this makes Minami bristle."
    show minami angry
    minami.say "And what's that supposed to mean?!?"
    minami.say "You wicked, cheating bit..."
    "I hastily clamp a hand over Minami's lips, stopping her before the whole insult can escape them."
    "Her eyes flare with anger, and she struggles to break free, wanting to get back into the fight."
    mike.say "Ah, we have to go now, Alexis."
    mike.say "But it was great bumping into you."
    mike.say "Wasn't it, Minami?"
    minami.say "Mmmmh..."
    minami.say "Fugging mitch..."
    "Still smiling nervously back at Alexis, I drag Minami away as quickly as I can."
    hide alexis
    show minami at center
    with moveoutright
    "She's fairly light, and so the task doesn't prove all that hard to accomplish."
    "It's actually taking my hand off of her mouth and letting her go that worries me..."
    hide minami
    return

label minami_meet_jack:
    show bg street
    show minami
    with fade
    "Most of my day so far has been taken up with showing Minami around my neighborhood so that she can get her bearings."
    "Which boils down to nothing more than cluing her into where the shops and other amenities are located in relation to the house."
    "It's necessary if I want her to become self-sufficient and not to be constantly relying on me for everything."
    "But it's a tiring slog from one place to the next, and before too long, we're both bored senseless."
    "Then it occurs to me that there are some essential local businesses that are more pleasant than others."
    mike.say "And next, next on our agenda is..."
    show minami annoyed
    minami.say "Urgh..."
    minami.say "This had better be good, big bro!"
    mike.say "The Winchester Arms - also known colloquially as simply 'The Winchester'!"
    "I make a sweeping gesture with one arm, taking in the frontage of the pub."
    show minami normal
    "Minami's mood instantly improves at the sight of something a little more fun than a laundromat or convenience store."
    "She claps her hands in glee, treating me to one of her cutest smiles too."
    show minami tehe
    minami.say "Ooo..."
    minami.say "So this is where you hang out, big bro?"
    minami.say "And you're going to let me in on it too!"
    show minami normal
    "I hold the door open for Minami, shaking my head at her enthusiasm."
    mike.say "It's just the local pub, Minami."
    mike.say "I'm not letting you into some secret clubhouse or something!"
    show minami happy
    minami.say "Oh, big bro!"
    minami.say "You don't know how long I waited to get to do things like this."
    minami.say "I was always so jealous when you left home."
    minami.say "And I wanted to be where you were, doing the things you were doing..."
    mike.say "Erm...yeah."
    mike.say "Okay, Minami...whatever you say!"
    show bg pub with fade
    "I usher Minami into the pub and make my way to the bar with her in tow."
    "After she shows the bartender her ID, we get a couple of drinks and look for somewhere to sit."
    jack.say "Hey, [hero.name] - over here!"
    show minami surprised
    show fx exclamation
    minami.say "Oh...My...God!"
    minami.say "I know him - that's Jack!"
    hide fx
    show minami normal at left5
    show jack normal at right5
    with moveinright
    "Before I can say as much as a single word, Minami bounds over to the table where Jack's sitting."
    minami.say "Hey, Jack!"
    minami.say "It's me - Minami!"
    minami.say "You remember me, right?"
    "I arrive a couple of seconds after Minami, in time to see the stunned look on Jack's face."
    "The sight of a perky young girl the likes of Minami bouncing towards him across a crowded pub must be quite something!"
    "I give my friend a wave for the sake of being polite, but I doubt that he even notices my presence."
    jack.say "Y...you can't be Minami."
    jack.say "Minami's a little girl."
    jack.say "And you...you're..."
    show minami a angry
    "Minami plants her balled fists on her hips, curling her lip as she does so."
    minami.say "I'm what, exactly?!?"
    show jack perv
    jack.say "You're a gorgeous babe - that's what you are!"
    show minami happy
    "Every trace of irritation and anger drains from Minami's face the same instant that she hears the compliment."
    "Instead of clenching her hands, Minami clasps them under her chin as she beams happily at her new admirer."
    minami.say "Oh, Jack."
    minami.say "Do you really mean that?"
    "Jack begins to nod, and looks like he's about to say more."
    "But I take the opportunity to cut into the conversation before he can speak."
    mike.say "Lay off the flattery, Jack."
    mike.say "My LITTLE SISTER's already got an over-sized ego as it is!"
    "The emphasis that I place on my familial relationship with Minami seems to do the trick."
    show jack normal
    "Jack snaps out of his trance and turns towards me for the first time."
    jack.say "Oh, hey there, [hero.name]."
    jack.say "I didn't see you come over!"
    "Of course not - he was too busy drooling over my sister!"
    mike.say "I guess your mind was on other things, yeah?"
    jack.say "Huh...sure...whatever..."
    minami.say "I have to go to the girl's room."
    minami.say "Be here when I get back!"
    jack.say "You bet I will!"
    hide minami
    show jack normal at center
    with moveoutleft
    "As soon as Minami is out of earshot, I fix Jack with an irate stare."
    mike.say "Jack, will you stop perving on her for one second?"
    mike.say "That's my little sister, for god's sake!"
    "Jack shrugs at my outburst, holding his hands up as if he's helpless."
    jack.say "She WAS your little sister last time I saw her."
    jack.say "But all I see now is one hot babe!"
    jack.say "I don't know how you can keep control of yourself around her - I couldn't do it!"
    mike.say "Like I said, she's my SISTER!"
    jack.say "You mean she's your adopted sister, dude."
    jack.say "That has to make a difference, right?"
    mike.say "The only thing that'll make a difference to me is if we can drop the subject - right now!"
    jack.say "Okay, okay."
    jack.say "But she's still going to be on my mind when I fall asleep tonight!"
    "I try as best I can to keep a mental image forming, but it's too late."
    "That's one that's going to stay with me for a long time and cost a fortune in therapist's fees..."
    scene bg black with dissolve
    return

label minami_meet_kylie:
    show expression f"bg {game.room}"
    "I could have left Minami to find her way around the college campus on her own without feeling all that guilty."
    "After all, it's not the biggest of places and if she's smart enough to study there then she's also smart enough to cope."
    "But I'm enjoying the role of big brother so much that I decide to give her the guided tour instead."
    show minami zorder 2 at center with dissolve
    "And to be completely honest, it's a massive ego rub to have Minami following me around like a loyal little puppy."
    "Suddenly all of the mundane knowledge that I have about the place is transformed into fascinating nuggets of information."
    "And I liberally drop these into the conversation as we go, Minami hanging off my arm, nodding the whole time."
    "At first I try to keep it sensible and help her to find the theaters where her lectures will be held and the like."
    "But it soon becomes more about me letting her in on the little hints and tips I've accumulated over my time studying there too."
    "I'm talking stuff like short-cuts between the lecture halls and seats where you can sleep without being discovered."
    "With each and every tip I impart, Minami seems to become ever more impressed, basking in my supposed wisdom."
    minami.say "Oh, big bro."
    minami.say "I don't know what I'd do without you!"
    mike.say "Huh!"
    mike.say "What do you mean, Minami?"
    minami.say "I mean I'd have been totally lost, wandering about here on my own."
    show minami happy
    minami.say "But with you here, I feel like I know this whole place already!"
    "I look down to see her beaming smile and wide, innocent eyes staring back up at me."
    "Minami looks like she's hanging on my every word, and it's enough to make me blush."
    mike.say "Ah, don't be silly, Minami!"
    show minami normal
    minami.say "I'm not, big bro."
    minami.say "If it weren't for you, I'd feel so scared and alone..."
    kylie.say "Minami?!?"
    kylie.say "Is that really you?!?"
    "For a moment there, I had the feeling that the mood between Minami and I was about to change."
    "Like she was on the brink of confessing something that had been buried deep down inside of her."
    "But then someone else butts in, and the feeling disappears in an instant."
    "Our heads spin around as one, turning to face the direction from which the voice came."
    "I swear there was nobody there a second before, not even someone passing that could have seen us."
    show minami surprised zorder 2 at left4
    show kylie surprised zorder 1 at top_mostright
    with moveinright
    "Yet there stands Kylie all the same, eyes almost as wide as Minami's, staring at us intently."
    minami.say "Hey, Kylie!"
    minami.say "Don't tell me you go here too?!?"
    show kylie annoyed
    "As Minami acknowledges her, I swear I see a subtle shift in Kylie's demeanour."
    "Before she appeared surprised, even shocked at the sight of my little sister."
    show kylie happy
    "But now a smile spreads across her face, and her mood warms visibly."
    kylie.say "Erm, yeah - didn't [hero.name] tell you that?"
    show minami angry
    minami.say "No, he didn't!"
    show kylie normal at right5 with ease
    "As Kylie reaches us, Minami turns around to wag a finger in my face, playfully telling me off."
    minami.say "Bad big bro, very, very bad!"
    minami.say "You should have told me my BFF was going here too!"
    "Of course, Kylie's almost the same age as Minami, give or take a couple of months."
    "At some point I must have known that they were friends back in high-school."
    "But I guess I had enough drama of my own going on back then."
    "So it's no wonder the details got blurred and forgotten over time."
    show minami normal
    mike.say "Okay, okay - my bad."
    mike.say "I guess I was so caught up in things that it slipped my mind."
    show kylie annoyed
    "Kylie nods slowly, but I see that she's still eyeing me with a visible measure of suspicion."
    minami.say "Ah, who cares about any of that."
    minami.say "All that matters is we're all here now."
    minami.say "My very best friend from school."
    minami.say "And my big bro, that I LOVE!"
    show kylie surprised
    "Suddenly Kylie's gaze homes in on Minami like a laser seeking its target."
    kylie.say "What did you say?"
    show minami tehe
    minami.say "That I love my big bro - more than ANYTHING in the whole world!"
    show minami tehe zorder 2 at center, zoomAt(1.5, (540, 1040)) with hpunch
    "As if she feels the need to emphasize the point, Minami hugs me as tight as possible."
    "She presses her face into my chest, making a satisfied sound that reminds me of a purring cat."
    show kylie angry
    "I see Kylie's eyes narrow in reaction to this, and she looks at Minami in a way that's almost disturbing."
    show kylie normal
    "But then, as quickly as it appeared, the predatory glare in Kylie's eyes is gone."
    kylie.say "Of course you do, Minami."
    kylie.say "He's your 'big bro' after all!"
    show minami happy
    "Seemingly oblivious to the storm that just passed over Kylie's features, Minami smiles back at her."
    minami.say "He sure is!"
    minami.say "Oh, it's going to be so much fun having the both of you here!"
    show kylie happy
    "Kylie nods slowly, smiling the whole time."
    kylie.say "Oh yeah, Minami."
    kylie.say "So much fun it'll be a scream..."
    mike.say "Well, we should really get going."
    mike.say "This tour isn't going to finish itself!"
    hide minami
    show minami a normal at left5
    show kylie crazysad
    "I hustle Minami away as quickly as I can manage, while she waves back at Kylie the whole time."
    "But no matter how I try, I can't shake the image of Kylie's eyes as she stared at my little sister."
    scene bg black with dissolve
    return

label minami_meet_morgan:
    show bg coffeeshop
    show minami
    with fade
    "There are some people that I thought it'd be pretty tough to introduce Minami to now that she's living with me."
    "I mean, I know some quirky and even spiky people when you catch them at the wrong time or say the wrong thing."
    "And Minami's had a fairly sheltered upbringing, which means that she's sometimes lacking in tact."
    "But I'd been racking my brains for people that might be an easier option, you know - less of a potential disaster?"
    "And that's when I remembered that Minami knew most of my friends, back when I was at high-school."
    "That's at least a handful of people that she should already have an in with, surely?"
    "So when we bumped into Morgan on the way to pick up a takeout from the local coffee shop, I wasn't all that worried."
    show minami at left5
    show morgan at right5
    with moveinright
    morgan.say "[hero.name], hey there!"
    mike.say "Morgan - great to see you."
    "I open my mouth to say more."
    "But the sound of a cough at my elbow stops me short."
    show minami a angry
    minami.say "Erm, hello?"
    minami.say "What about me?"
    minami.say "I'm like, standing RIGHT here!"
    show morgan b
    "Morgan looks at Minami, then back to me."
    "She has an ironic smile on her face, as if we're enjoying a private joke."
    "A joke the existence of which Minami is not even aware."
    morgan.say "Yeah, sure - THERE you are alright!"
    mike.say "Ah...Morgan, you remember Minami - right?"
    mike.say "My little sister?"
    show morgan surprised
    "A look of recognition dawns on Morgan's face, and she nods a second later."
    show minami normal
    morgan.say "Oh yeah, I DO remember you."
    show morgan happy
    morgan.say "You were always tagging along, following [hero.name] around."
    morgan.say "Seems like some things never change!"
    show minami angry
    "Minami looks Morgan over with a haughty expression."
    "But if Morgan's comment was intended as a challenge, she doesn't rise to it."
    "Instead she uses the time-honored tactic of a passive-aggressive response."
    show minami normal
    minami.say "Well, it looks like SOME things do."
    show morgan a annoyed
    "Morgan frowns at this, crossing her arms over her chest in a defensive gesture."
    morgan.say "And just what is that supposed to mean?"
    minami.say "Well, last time we met, I was sure you were a guy!"
    show morgan surprised
    "As soon as the words are out of Minami's mouth, my eyes go wide and I jump straight into the exchange."
    mike.say "Whoa, hey there, Minami."
    mike.say "Are you crazy?"
    mike.say "I was the only one that thought Morgan was a guy - and I was dead wrong!"
    show minami surprised
    "The look of confusion that Minami pulls off then could seriously earn her an Oscar."
    minami.say "Oh, really?!?"
    show minami normal
    minami.say "I'm SO sorry, Morgan - I had no idea!"
    minami.say "I guess I'm just so used to big bro being right, I just took his word for it."
    minami.say "Can you ever forgive me?"
    "I've seen this maneuver on Minami's part before - the full force of her apparent innocence, concentrated on one spot."
    "It's like someone using a magnifying glass to focus the sun's rays and ignite a fire."
    "And even Morgan isn't immune to the effects of this terrible weapon!"
    show morgan normal
    morgan.say "I...well...I guess..."
    morgan.say "It's okay, Minami."
    morgan.say "At least you know the truth now."
    show minami happy
    "Minami beams once more as Morgan forgives her, all sweetness and light again."
    minami.say "Aww, thanks, Morgan."
    minami.say "I like you better as a girl anyway."
    minami.say "I mean, you're just SO pretty!"
    show morgan blush
    "Caught completely off-guard, I see Morgan blush at the compliment."
    morgan.say "Th...thanks, Minami..."
    morgan.say "That's so nice of you to say!"
    "We say our goodbyes to Morgan and join the queue to buy some coffee."
    hide morgan
    show minami normal at center
    with fade
    "The whole time I keep stealing glances at Minami, who looks for the world like nothing at all happened back there."
    "Did she get this manipulative while I was away from home?"
    "Or has she always had that kind of talent and I just failed to notice it?"
    return

label minami_react_kylie_sentence:
    show minami constipated
    "As soon as I look up and see Minami's face, I know exactly what the problem is."
    "After all, I've known her since we were both kids, grown up alongside her."
    "So I can usually read the expression on her face like a book."
    "Right now she looks upset almost to the point of being distraught."
    "But there's also confusion in her eyes, like she doesn't know if she's right."
    "And all of that means she's not come to discuss the rota for the household chores!"
    mike.say "Minami..."
    mike.say "Do you need to talk about something?"
    mike.say "Because you look like you've a lot on your mind."
    "Minami stares at me for a moment, almost like she's stunned."
    "Then she begins to nod her head, and I think she might actually cry."
    minami.say "Yeah there is, big bro..."
    minami.say "But...but I'm scared of something!"
    "I think I might know what that is."
    "But it'd be better for me to hear it from Minami herself."
    "Better than me making an assumption and getting it totally wrong."
    mike.say "It's okay, Minami..."
    mike.say "I'm here for you."
    mike.say "Whatever it is, you can tell me."
    "Minami looks me in the eye."
    "But then just as quickly, she looks away again."
    minami.say "Are you sure?"
    minami.say "I'm worried you'll be mad at me!"
    "Now I really am getting confused."
    mike.say "Minami..."
    mike.say "I...I don't understand."
    mike.say "What could possibly make me mad at you?!?"
    "Minami turns to face me again."
    "And when she does so, I see that she's wringing her hands together."
    show minami sad
    minami.say "It's..."
    minami.say "It's about Kylie, big bro..."
    minami.say "And what they're going to do to her!"
    "Now things are beginning to make some kind of sense."
    "What Kylie did that night when she broke in here was bad enough."
    "And once she was behind bars, I thought that would be the end of it."
    "I thought that we'd all have the time we needed to heal."
    "But all of that changed when I got the news she was going to get the death penalty."
    "I suppose most people would be over the moon at that, satisfied she was getting justice."
    "But for me the honest truth is that it left me feeling kind of empty and confused."
    "And it certainly didn't make me feel any better about everything that happened either."
    "I guess that all I can do is listen to what's bothering Minami."
    "That and be honest with her about how it all makes me feel too."
    mike.say "You can tell me what you're feeling, Minami."
    mike.say "I promise that I won't be mad at you, whatever it is."
    "Minami studies me in silence for a moment."
    "Like she's trying to see if staring into my eyes will reveal whether or not I'm being truthful."
    "And I'm relieved to find that she does seem to trust me on that score."
    "Because a few seconds later, Minami finally starts to open up to me."
    minami.say "I know I should hate Kylie for what she did."
    minami.say "And, well...I do hate WHAT she did, big bro."
    show minami cry
    minami.say "But it's so hard to forget how she used to be."
    minami.say "You know, back when we were kids?"
    "I nod at all the stuff Minami's saying."
    "But silently I'm almost kicking myself."
    "Because I'd half forgotten that she and Kylie were friends back then."
    "Alexis and I were close, of course - but so were both our little sisters."
    "So no wonder Minami's struggling to come to terms with how Kylie turned out."
    mike.say "I've spoken to Alexis about all of this, Minami."
    mike.say "She's just as baffled by it as you are."
    mike.say "And she's Kylie's own sister!"
    show minami sad
    minami.say "There's more though, big bro..."
    minami.say "I...I don't know if killing her is the right thing!"
    minami.say "I mean, aren't people supposed to learn from their mistakes?"
    show minami cry
    minami.say "How can Kylie do that if they end her life?!?"
    "I was hoping to be able to talk this through with Minami."
    "That we could both open up to each other about our feelings."
    "But that's a question that's way beyond my ability to answer."
    "So I guess we're back to being honest again."
    mike.say "I can't answer that one, Minami."
    mike.say "I don't know if anyone can."
    mike.say "If anyone should be happy Kylie got the death penalty, it should be me."
    mike.say "But you know what?"
    show minami surprised
    mike.say "It doesn't make me feel any better!"
    "Minami looks shocked to hear me say such a thing."
    "Like she was expecting me to come out with the opposite."
    minami.say "Really, big bro?"
    show minami sad
    minami.say "Even after she...she hurt you so badly?"
    "I shrug and shake my head."
    mike.say "Since when did hurting someone else help?"
    mike.say "Like, when you're in pain yourself?"
    mike.say "It doesn't make it hurt any less."
    minami.say "So what are you saying, big bro?"
    minami.say "That there's no right or wrong answer?"
    mike.say "I don't know, Minami..."
    mike.say "Maybe I'm more saying you have to find the answer that makes sense to you?"
    mike.say "But talking about it and saying how you feel has got to help, right?"
    show minami sadsmile
    "Minami smiles and leans her head on my shoulder."
    minami.say "Okay, big bro..."
    minami.say "I think we can do that!"
    return

label minami_siscon_cap_04:
    $ minami.flags.sisconDelay = TemporaryFlag(True, 1)
    show bg livingroom
    "By now I'm getting more used to the idea of helping Minami out with her efforts at mastering the art of dating."
    "Sure, it's awkward, and I have no notion whatsoever as to whether or not I'm doing more harm than good."
    "But it feels pretty good to know that my little sister felt she could come to me for advice in her time of need."
    "Looking back, even the embarrassing memory of what happened when we tried to go over the basics of kissing doesn't seem so bad."
    "It was just a misunderstanding, the star pupil surprising her teacher with unexpected enthusiasm, and nothing more."
    show minami with dissolve
    "And this means that when Minami comes to me again, with that same look on her face, I'm pretty upbeat about the whole thing."
    mike.say "Hey, Minami."
    mike.say "Is it time for another lesson already?"
    show minami surprised
    "It seems that my eagerness takes Minami by surprise."
    "At first, she seems to struggle to answer the question."
    show minami normal
    minami.say "Ah, yeah, big bro."
    minami.say "You must have read my mind!"
    mike.say "Okay, so what's it to be this time, huh?"
    mike.say "Advice on amóre?"
    mike.say "Revision for romance?"
    minami.say "Erm...no."
    minami.say "It's kinda more specific..."
    mike.say "Really?"
    mike.say "And just what would that entail?"
    "Minami pauses to take a deep breath, and then lets it out again."
    show minami happy
    "Then she forces a smile onto her face before she gives me an answer."
    minami.say "Well..."
    minami.say "I want to know all about...cocks."
    "My mouth works in silence for a moment, no words making it from my brain to my tongue."
    "All of this time, I'm still trying to figure out if she actually just said what I heard."
    mike.say "You want to know about what?!?"
    show minami annoyed
    "Minami shakes her head, exasperated at my apparent lack of maturity."
    minami.say "Cocks, big bro!"
    minami.say "You know, the things that you guys are supposed to use in place of actual brains?!?"
    "I wave my hands in the air, trying to get Minami to keep her voice down."
    mike.say "Yes, thank you - I think I know what a cock is!"
    mike.say "And you do too, for what it's worth!"
    mike.say "Doubt you slept through that particular biology lesson, Minami."
    "Minami throws her own hands in the air, frustrated with my reaction."
    minami.say "Like, what has that got to do with actual sex, big bro!"
    minami.say "You're not telling me you base your technique on a diagram of a vagina, are you?"
    mike.say "Hey, now you wait a minute, Minami."
    mike.say "You asked me to help you learn about dating - not sex!"
    show minami angry
    minami.say "But that's a part of dating too."
    minami.say "Come on - you can't leave me at first base!"
    mike.say "Yeah, Minami, you say that."
    mike.say "But what is getting you past second base going to cost me?!?"
    show minami hunt
    "She betrays her true intentions a moment later, as her eyes glance down below my waist."
    "They shoot straight back up again, and she tries her best to make like it never happened at all."
    "But the damage is already done."
    mike.say "Oh no!"
    mike.say "No way, Minami!"
    show minami sad
    minami.say "Please, big bro!"
    minami.say "I only need a little peek at it!"
    "Minami has her hands clasped together as she whines and pleads for her own way."
    "She's already making to get down on her knees, right there in front of me."
    "She could just be getting overly dramatic and planning to beg on her knees."
    "But she could as easily be trying to get closer to her ultimate goal too!"
    menu:
        "Refuse":
            mike.say "How many times do I have to say it, Minami?"
            mike.say "No, I am not showing you my manhood!"
            "I walk backwards and away from her, but she comes scurrying after me."
            show minami hunt
            minami.say "Just a quick glance, big bro."
            minami.say "I swear that's all I need!"
            "Finally managing to get some distance between us, I turn my back on Minami."
            mike.say "NO!"
            mike.say "Go and watch some porn, Minami."
            mike.say "That way you can stare at all the cocks you like!"
            show minami angry
            "Minami stamps her foot in anger, and then storms off without saying another word."
            hide minami with moveoutright
            "I watch her go, hoping for all I'm worth that nobody overheard that conversation."
            $ minami.siscon -= 5
            $ hero.cancel_event()
        "Agree":
            "I'm about to shoo Minami away from my groin, but then a thought occurs to me."
            "How many girls are lucky enough to know all about this kind of stuff before they get out there?"
            "Most guys are pretty clueless too, but they at least know what to do with their cocks."
            "Would I really be a good big brother if I let Minami go out there without cluing her up first?"
            "Yeah, yeah, yeah - I know how it looks."
            "But we've never had the most normal of sibling relationships."
            mike.say "Oh god..."
            mike.say "I'm going to regret this, I just know it!"
            hide minami
            show minami close happy
            "Hope appears in Minami's eyes, and her hands start to move towards their prize once more."
            mike.say "But not here!"
            mike.say "First we go somewhere more private..."
            hide minami
            show bg bedroom1
            show minami normal
            with fade
            "After hastily retreating to the safety of my bedroom, I close the door and take a deep breath."
            "Minami is sitting happily on the bed, just waiting for the show to begin."
            "I take a deep breath, which does nothing to prepare me for what I'm about to do."
            "Standing a couple of feet away from Minami, I undo my pants and pull them down."
            mike.say "There, Minami - are you happy now?"
            minami.say "Ooh..."
            minami.say "Mmm..."
            mike.say "Wha...what are those noises supposed to mean?"
            "Minami reluctantly tears her eyes away from my groin and looks me in the face."
            minami.say "Huh?"
            mike.say "You're not saying anything, Minami - just making weird noises!"
            mike.say "Is there something wrong?"
            minami.say "Oh, no, big bro."
            minami.say "It's...very nice."
            mike.say "That's it?!?"
            minami.say "Hey, what more do you want me to say?"
            minami.say "I was trying not to make it weird!"
            mike.say "Well you didn't manage it - you just made me paranoid!"
            show minami blush
            "Her cheeks turning red as she gets flustered, Minami protests instantly."
            minami.say "What do you want me to say, big bro?!?"
            minami.say "It's so nice that I want to touch it!"
            minami.say "I...I never thought it would be so...big!"
            "Now it's my turn to feel my cheeks flushing red."
            mike.say "I just made it weird, didn't I?"
            minami.say "Yeah, big bro, you did."
            mike.say "I'm going to pull my pants up now, okay?"
            minami.say "Okay, big bro..."
            "And as I do so, Minami can't hold it in any longer."
            show minami happy
            "She bursts into peals of nervous laughter as I burn with shame at my own dumb vanity..."
            $ game.room = "bedroom1"
            $ minami.siscon.max = 90
            $ minami.siscon += 5
    return

label minami_siscon_cap_03:
    $ minami.flags.sisconDelay = TemporaryFlag(True, 1)
    show bg livingroom
    "You know that strange feeling, when you somehow just know that you're being watched?"
    "Well, I'm getting that same feeling right now, and it's so bad that I can't help but look up."
    "And for once, it proves to be more than just a strange hunch which turns out to be nothing."
    show minami with dissolve
    "Because the first thing I see is Minami, looking straight at me, a sickly sweet smile on her face."
    "In addition to that, she has her hands clasped behind her back as she traces a line on the ground with one foot."
    "And though she doesn't come right out and say it, I'm instantly sure that she's after something."
    "After all, we did grow up together."
    "I've seen her pull that kind of pose on Mom and Dad pretty often in the past before inevitably getting her own way."
    "Little does she know that I'm wise to all of her little games, and won't be such of a pushover."
    mike.say "Okay, Minami - out with it."
    show minami surprised
    "Minami does her best impression of looking shocked and surprised."
    minami.say "Oh, big bro!"
    minami.say "Whatever do you mean?"
    mike.say "Don't give me that, Minami."
    mike.say "You want something, I know it."
    mike.say "So no beating about the bush - out with it, now!"
    show minami annoyed
    minami.say "Alright, alright, I get the message already!"
    "I nod, preparing myself for whatever Minami is about to say."
    show minami normal
    minami.say "I just wondered if it was time for my next lesson yet?"
    minami.say "You remember - my next lesson in dating?"
    "Of course, I let Minami talk me into teaching her the basics of dating."
    "I admit that I'd been trying to forget all about it in the hope that she might too."
    "But it seems as though that hope was very much in vain."
    mike.say "Oh, yeah..."
    mike.say "Sure thing, Minami."
    mike.say "I was actually gonna talk to you about that."
    show minami happy
    minami.say "That's great, big bro - because I'm all ready for it!"
    mike.say "Yeah, that's the thing, you see."
    mike.say "I'm not sure that you need anymore..."
    show minami normal
    "But I might as well have been talking to thin air, as Minami carries on talking straight over me."
    minami.say "The next thing you teach me can only be one thing."
    minami.say "It just HAS to be kissing - right?!?"
    "What in the hell?!?"
    "Is she actually serious?"
    mike.say "Minami, don't tell me you've never kissed someone before?"
    show minami annoyed blush
    "Minami suddenly becomes bashful, refusing to meet my eye."
    minami.say "Big bro, don't tease me like that!"
    minami.say "So what if I haven't?"
    minami.say "I was...saving myself for the right guy, you know?"
    mike.say "Well, isn't that all the more reason to not learn from me?"
    mike.say "Do you really want your first time to be with your brother and not this 'right guy'?"
    show minami normal
    minami.say "But what if the right guy was..."
    "Minami stops herself before she can finish what she's saying."
    "And for a moment, I think she was about to say something important."
    show minami normal -blush
    "But then she seems to shake it off and start over again."
    minami.say "It's not like it'd really count with you, big bro."
    minami.say "And it'd only be this once, I promise - please?"
    menu:
        "Refuse":
            mike.say "Ah, no way, Minami."
            mike.say "It'd just be way too weird!"
            show minami sad
            minami.say "Aww, no fair!"
            minami.say "What am I supposed to do instead, huh?"
            "All I can do is shrug my shoulders and shake my head."
            mike.say "I don't know, Minami."
            mike.say "Maybe you could practice on your hand or something?"
            show minami angry
            "Minami makes a harrumphing sound and almost stamps her foot in response."
            "As she turns to go, I hear her muttering something under her breath."
            minami.say "Maybe I'll ask [bree.name] and Sasha for help..."
            $ minami.lesbian += 10
            $ minami.siscon -= 5
            $ hero.cancel_event()
        "Agree":
            "Would it really be that much of a bad thing to help her out?"
            "I mean, you hear about teenage girls practicing on each other all the time, right?"
            "And I am her brother, so there's no chance either of us could get the wrong idea."
            mike.say "Ah, what the hell."
            mike.say "If you're sure it'll help, Minami."
            show minami happy
            minami.say "Ooh, this is SO exciting!"
            minami.say "Promise you'll be gentle, big bro?"
            mike.say "I...of course I will, Minami!"
            mike.say "Okay...let's start off simple, just touching lips."
            show minami close blush
            "At this, Minami instantly leans forward, pursing her lips and screwing up the rest of her face."
            "It's all that I can do to keep from bursting out laughing."
            mike.say "Try relaxing, Minami."
            mike.say "Just be natural."
            "She nods, and this time does as she's told."
            show minami kiss with dissolve
            $ minami.flags.kiss += 1
            "I touch my lips gently to hers, keeping the pressure light."
            "It feels so good that I can't help feeling a little envious of Minami's imaginary 'right guy'."
            "At first she doesn't move at all, but then I feel her lips stir slightly."
            "That's good, she's following her instincts."
            "So I encourage her by doing the same."
            "A moment later, I feel her lips part, and then her tongue darts into my mouth."
            "I should call it off, right there and then."
            "But I don't, and I'd like to be able to blame that on the shock."
            "The truth is that Minami's tongue feels incredible, and I just can't help kissing her back."
            "In mere moments, the kiss goes from chaste and gentle to passionate and intense."
            "I can already feel my cock getting hard, and the sound of Minami starting to gasp..."
            "Shit - I can't let this happen!"
            "Summoning all of my remaining willpower, I tear myself away from Minami."
            mike.say "I...I'm sorry, Minami..."
            mike.say "I don't know what came over me!"
            hide minami
            show minami hunt
            with dissolve
            "Minami has a hand on her chest, panting as she regards me with wide, almost hungry eyes."
            minami.say "M...me too, big bro."
            minami.say "You're a REALLY good kisser though!"
            minami.say "But...was I supposed to feel it...down here?"
            "I follow Minami's other hand, as she points down between her thighs."
            mike.say "Yes...no...shit, I don't know anymore!"
            minami.say "Ooh, I think you need to lie down, or maybe take a cold shower!"
            $ minami.flags.nokiss = False
            $ minami.flags.noFlirtyText = False
            $ minami.siscon.max = 80
            $ minami.siscon += 5
            $ minami.love += 5
    return

label minami_siscon_cap_02:
    $ minami.flags.sisconDelay = TemporaryFlag(True, 1)
    $ minami.flags.nodate = False
    $ minami.flags.noproposedate = False
    show bg aquarium
    "After much heated debate and spirited discussion, Minami and I settle on the Aquarium as the setting for our first lesson in dating."
    "At first, she suggested that we have a meal at a nice restaurant, which I shot down as being second or even third date territory."
    "My initial suggestion was a trip to the mall, but Minami just rolled her eyes, calling that boring and predictable."
    "But when the aquarium came up, neither of us objected - which meant that I pounced on it as a good compromise."
    show minami casual with dissolve
    "Almost as soon as I've bought our tickets and we're through the entrance, Minami takes hold of my hand."
    "Surprised at this, I glance down at our intertwined fingers and then back up at her."
    mike.say "Erm, Minami..."
    show minami a blush at center, zoomAt(1.5, (640, 1040))
    minami.say "Yeah, big bro?"
    mike.say "What's with holding my hand?"
    mike.say "I mean, there's a map in the leaflet that came with the tickets."
    mike.say "And it's not like I'm worried about you getting lost either."
    show minami a annoyed
    "Minami tilts her head to one side and gives me one of her most condescending looks."
    minami.say "Don't be such a dope, big bro!"
    minami.say "This is supposed to be a date."
    show minami a normal
    minami.say "And on a date you hold the girl's hand!"
    mike.say "Yeah, but this isn't actually a REAL date, Minami."
    mike.say "It's more like I'm showing you the ropes, you know?"
    mike.say "We're not trying to convince people it's the real thing."
    show minami a angry -blush
    "Suddenly I see a change in Minami's expression, her smile turning into a frown."
    minami.say "Why, big bro?"
    minami.say "Do you think I'm not pretty enough for them to believe it?"
    minami.say "Are you trying to say they wouldn't think I could get a date?"
    menu:
        "Refuse":
            $ minami.flags.dateHoldHand = False
            hide minami
            show minami c casual annoyed
            mike.say "Minami, stop it - you're being ridiculous."
            mike.say "It doesn't matter what anyone else thinks."
            mike.say "And this is only your first lesson."
            mike.say "Worry about getting it right when you're on an actual date!"
            "Minami stares at her feet as she reluctantly pulls her hand out of mine."
            "I know full well that she's sulking now, but I don't let it bother me."
            "The fact that she's dropped the subject lets me know that I've gotten through to her."
        "Accept":
            $ minami.flags.dateHoldHand = True
            $ minami.love += 5
            "I don't want to hurt Minami's feelings."
            "That could end the lesson before it even gets started!"
            mike.say "Of course not, Minami - don't be ridiculous."
            mike.say "How could someone as cute as you not get a date?"
            "It's blatant flattery, I know."
            show minami a normal
            "But as usual, it seems to work on her."
            show minami a blush
            minami.say "Really, big bro?"
            mike.say "Really, Minami."
            mike.say "Look, if you want to hold my hand, then go right ahead."
            "Minami smiles and squeezes my hand tighter than ever."
    show minami a normal
    "We go slowly around the aquarium, taking our time and lingering whenever something catches our attention."
    "The conversation wanders between Minami asking questions and me offering pointers."
    "But all the same, the aquarium has some pretty impressive specimens on show."
    "And more than once we find ourselves actually stopping to stare at what's behind the glass in awe."
    show minami a happy
    minami.say "Ooh, these fish are SO pretty!"
    minami.say "Aren't they the ones from that film?"
    minami.say "The one where the other fish keeps forgetting everything?"
    "I can't help chuckling at the rapid fire nature of Minami's questions."
    show minami a sad blush
    "But at the sound of my laughter, she blushes and looks at me with genuine concern in her eyes."
    minami.say "What's wrong, big bro?"
    minami.say "Did I do something wrong?"
    "At first I'm not sure how to answer that question."
    "Sure, Minami can get carried away and talk too much."
    "But that's just part of her personality, and I don't want to teach her to suppress that either."
    mike.say "No, Minami, you didn't."
    mike.say "But maybe say one thing that's on your mind, rather than everything."
    "She nods at this, a serious look on her face as though she's trying to commit the advice to memory."
    show minami a normal
    "We move on to another tank, this one far larger than all of the previous ones."
    "We're literally standing in front of a wall of glass, staring into the inky depths."
    "Though we can't see what's actually in the tank, it's full of seaweed and coral, lit with an eldritch ambience."
    show minami a happy
    minami.say "Wow, it's like an enchanted, underwater world in there!"
    "Minami leans in for a closer look, practically pressing her nose against the glass."
    minami.say "You know, I always wanted to be a mermaid when I was little."
    minami.say "And this place is making me feel like that again."
    minami.say "I could make that my next cosplay project."
    show minami a normal
    "She turns her head towards me, catching my eye."
    minami.say "What do you think, big bro?"
    minami.say "Would I look cute in a tail, huh?"
    minami.say "Maybe with a matching seashell bra?"
    mike.say "Maybe that's a little too much information for a first date, Minami!"
    "Minami shakes her head at my disapproval, turning back to the tank."
    "But then something moves behind the glass, a dark shape emerging from the black."
    "I see that it's a shark, no clue as to what type, but it's a damn huge specimen whatever it is!"
    "The sight makes me jump, but Minami is virtually face-to-face with the monster."
    show minami a surprised with hpunch
    minami.say "AHH!"
    minami.say "BIG BRO - SAVE ME!"
    if not minami.flags.dateHoldHand:
        "Minami leaps backwards, desperate to put as much distance between herself and the shark as possible."
        "In her haste, she tumbles off of her feet."
        hide minami with moveoutbottom
        play sound body_fall
        pause 0.3
        with vpunch
        "And she lands heavily on her backside and letting out another shriek of alarm."
        "I shake my head in amusement, rapping my knuckles on the glass as I chuckle to myself."
        mike.say "I think the glass is thick enough to do that for me, Minami!"
        minami.say "Don't be mean, big bro."
        minami.say "I was really scared that it'd get me!"
        show minami casual sad with moveinbottom
        "I kneel down to help Minami back to her feet, still shaking my head."
        mike.say "Well don't worry, you're safe now."
        mike.say "And just for the record, don't do that on a real date!"
        show minami angry
        minami.say "Big bro!"
        minami.say "It's NOT funny!"
        show minami tehe
        "But as Minami dusts herself off, she shrugs awkwardly."
        minami.say "Well, maybe it is a LITTLE funny..."
        mike.say "Sense of humour, Minami - very important in a potential partner!"
        "Minami punches me weakly on the arm, and we get back to our stroll around the aquarium."
        $ minami.siscon -= 5
        $ hero.cancel_activity()
    else:
        $ minami.siscon.max = 60
        "Minami leaps backwards, desperate to put as much distance between herself and the shark as possible."
        show minami at center, zoomAt (1.75, (650, 1140)) with hpunch
        "But the fact that she's still holding my hand means that she throws herself straight into my arms instead."
        "Minami clings to me desperately, and before I know it, I react on pure instinct alone."
        "I pull her into a tight embrace, holding her against my chest."
        "My hand is pressed against Minami's chest, and I can feel the curve of one petite breast under my palm."
        "Her heart is literally pounding away in her chest, like a frightened little animal."
        mike.say "Hey, hey..."
        mike.say "It's okay, Minami, it's okay..."
        "She looks up at me, her eyes still wide with fear."
        "I can't help what happens next, as the urge to protect her is just too strong."
        "And so I pull her even closer to me, feeling her body pressing against mine."
        minami.say "Erm, big bro..."
        mike.say "Yeah, Minami?"
        minami.say "It's behind the glass, isn't it?"
        mike.say "Yeah, Minami, it is."
        $ minami.siscon += 5
        "Minami looks away, burying her head in my chest for a moment."
        show minami a happy
        "But then she surprises me by bursting out laughing."
        minami.say "Wow - that must have looked so stupid!"
        minami.say "I guess I shouldn't do that on a real date?"
        mike.say "No, Minami, you probably shouldn't!"
        "We both laugh then, sharing a moment of smiles and bashful looks."
        "And then Minami's gaze settles on my hand, still laid upon her chest."
        mike.say "Oh, shit!"
        mike.say "I'm sorry, Minami!"
        show minami a normal blush
        minami.say "It's okay, big bro - you were only trying to protect me..."
        "Slowly, Minami takes hold of my hand, grasping it once more."
        minami.say "Come on, let's get going."
        minami.say "I'm sure you've got loads more to tell me."
        "Minami leans her head against my shoulder, and we get back to our stroll around the aquarium."
    return

label minami_siscon_cap_01:
    $ minami.flags.sisconDelay = TemporaryFlag(True, 1)
    show minami blush
    "Growing up with someone, you get to know them pretty well, all the way down to their little quirks and habits."
    "Some may come and go, but there are always those that they keep and so become a part of their personality for good."
    "And Minami's no exception to that rule either, having so many that I sometimes think I could write a book on the subject."
    "But one of her truly defining quirks is the way that she always becomes almost sickly sweet when she wants something."
    "So when I notice that Minami's being nothing but nice and complimentary for the best part of the day, alarm bells start to ring."
    "I have no idea how long she'll keep this up before actually coming out and asking me for whatever it is that she wants."
    "That'll depend on the nature of the thing and the amount of outrage she guesses it'll cause when she does so."
    "Under these circumstances, I have one of two distinct choices."
    "The first is that I can ride it out and let Minami get there on her own."
    "Or the second is to call her bluff and demand to know what's up with her."
    "And call me a masochist, but I choose the latter."
    mike.say "Minami?"
    show minami hunt
    minami.say "Hey, big bro."
    show minami close hunt
    minami.say "What can I do for you, huh?"
    "Wow - I can almost feel my blood-sugar rising as she flutters her eyelids at me!"
    mike.say "Cut the crap, Minami."
    mike.say "I know what you're doing here."
    mike.say "What is it you want?"
    show minami surprised
    "For a couple of seconds, Minami does her level best to look confused and a little hurt."
    "Undeterred, I keep right on staring at her in the stoniest silence I can manage."
    "And it doesn't take too much longer for her to crack."
    hide minami
    show minami annoyed
    "Minami lets out a groan of resigned defeat."
    minami.say "Urrgh..."
    minami.say "Okay, big bro, okay - you win!"
    minami.say "I DO want to ask you something."
    show minami normal
    minami.say "But I was only being nice because you're such a great big bro!"
    mike.say "Whatever you say, Minami."
    mike.say "So come on, spit it out?"
    "Minami takes a moment to collect herself, visibly recharging her smile with fresh charm."
    "I take a deep breath, just waiting to hear whatever she comes out with next."
    "No matter how I try, I can't think that it's going to be anything other than a pain in the neck for me."
    minami.say "Well, big bro."
    minami.say "You know I came here to go to college, obviously."
    minami.say "But there's more to college than just studying, right?"
    "I narrow my eyes, trying to see where Minami's going with this."
    minami.say "It's like, you go to the university of life too."
    mike.say "The university of life?"
    minami.say "Sure, big bro."
    minami.say "You don't just study, do you?"
    minami.say "You do things like going to the Winchester and nightclubs too."
    mike.say "Well, yeah..."
    mike.say "I have to let off steam somehow."
    show minami blush
    "Minami nods at this, seizing on the admission as soon as I make it."
    minami.say "And you have...girlfriends..."
    mike.say "Again, yeah..."
    "Minami looks down at her hands as she wrings them together."
    "And for the first time since she started talking, I can't be sure if she's acting or not."
    show minami sad
    minami.say "I...I never got to do any of that back home."
    minami.say "And I'm scared that I don't know how..."
    "Is that it?"
    "Is she really just fretting about getting out there on the dating scene?"
    mike.say "It's not hard to learn, Minami."
    mike.say "I'm sure you'll pick it up quickly."
    minami.say "But what if I don't?!?"
    minami.say "That's why I was wondering if..."
    show minami normal
    minami.say "If you'd teach me how?"
    mike.say "Ah, how exactly would I do that, Minami?"
    mike.say "Do you want me to write it down on paper, or what?"
    minami.say "No, don't be silly, big bro!"
    minami.say "I was thinking you could SHOW me."
    minami.say "It'd be like dating school, with me as the student and you as the teacher."
    menu:
        "Refuse":
            "I might have thought she was crazy to be so worried about all of this stuff before."
            "But now she's pitched me that little idea, I'm pretty sure Minami's in danger of losing her marbles!"
            mike.say "Minami, for god's sake!"
            mike.say "You're getting WAY too serious about this."
            mike.say "They don't tell you this in the movies and on TV - but you're going to screw-up."
            mike.say "That's just part of dating, Minami."
            mike.say "Sometimes it's a hit, sometimes it's a miss."
            show minami sad
            $ minami.love -= 5
            minami.say "But...but if you help me out, big bro..."
            minami.say "Then I'd get more hits, right?"
            "I shake my head, letting her know that I mean what I say."
            mike.say "Trust me, Minami - I've been there myself."
            mike.say "It's the memory of the fails that make the wins so sweet."
            show minami angry
            minami.say "Aww..."
            minami.say "No fair, big bro!"
            "Minami crosses her arms over her chest."
            "And I can see the signs of a major sulk in the expression spreading over her face."
            mike.say "Sorry, Minami."
            mike.say "But no one ever said life was fair."
            mike.say "And that goes double for dating too!"
            $ minami.siscon -= 5
            $ hero.cancel_event()
        "Agree":
            "It sounds like a pretty crazy idea at first, but then I actually start to think about it more deeply."
            "I'd sure have liked to know some of the pitfalls that caught me out when I was first going out on real dates."
            "And it's not as if I'd be doing anything other than showing Minami the proverbial ropes."
            "This could be like one of those funny montages in a movie, where someone teaches the clueless girl to be a prom queen!"
            "Well, maybe nothing so grand as that."
            "More like teaching Minami not to chew with her mouth open or use the tablecloth as a napkin."
            $ minami.siscon.max = 40
            $ minami.siscon += 5
            $ minami.flags.practiceDate = True
            mike.say "You know, Minami, that does kind of sound like fun."
            mike.say "But you have to remember that I only know what I know."
            mike.say "I'm not some kind of modern-day Casanova!"
            show minami close happy
            "Minami's smile is pretty huge by now, showing her delight at getting her own way."
            minami.say "Shut up, big bro."
            minami.say "Now you ARE being silly!"
            minami.say "You were always going on dates back home."
            mike.say "Well, I don't know about that..."
            minami.say "And I always used to watch you with all those girls."
            minami.say "I was SO jealous."
            minami.say "I used to think how lucky they were to have a boyfriend as great as you!"
            minami.say "That's why I just know you'll be such a great teacher."
            "I try to stop Minami before my head's too big to fit through the door."
            mike.say "Ah, okay...yeah..."
            mike.say "We'll start with something simple - like a practice date!"
    return

label minami_siscon_10:
    show bg nightclub
    "I didn't really have a plan in mind for tonight, I just knew that I was tired of kicking around the house."
    "And so going out seemed to be the clearest answer, a change of scene to wake me up and improve my mood."
    "There's no one around to ask along when I'm leaving, so I just grab my jacket and head out the door."
    "It feels pretty good to be doing this on a whim, seeing where my instinct takes me."
    "I drift downtown, passing various familiar pubs and then the more upmarket bars in the center of the city."
    "Eventually I find myself outside a club that's always been high on my list of night-time destinations."
    "And so I join the back of the queue, reasoning that there's a good chance of meeting someone I know inside."
    "Once I'm past the bouncers on the door and mingling with the crowd, I'm sure this was the right decision."
    "I feel totally free to do whatever the hell I want in here - dance, drink, or anything else that's legal."
    "Usually I'm here with someone else, and so I'm trying to please them before myself."
    "But now I can dance to what I like and stay as late as the whim takes me."
    "Grabbing a drink from the bar, I hover around the edge of the dance-floor for a while."
    "I'm not plucking up the courage to get out there, just enjoying the chance to pick my moment."
    "My luck seems to be in, as an old favorite of mine gets played just as I'm finishing my drink."
    "And then the perfect spot on the dance-floor opens up too, like it was meant to be."
    "A moment later, I'm out there and dancing without a care in the world."
    "The funk that made me leave the house seems like a distant memory right now."
    "Instead I feel like I could take on the world!"
    "And I must really be giving out the exact same positive vibes."
    "As I soon have company on the dance-floor too!"
    "I look down to see a cute, petite girl in a cropped top and tartan skirt dancing really close to me."
    "I'm not looking to get into anything serious, sure."
    "But then a little flirting on the dance-floor never hurt anyone..."
    "So I make a move to dance a little closer to the mysterious girl."
    "And she returns my interest, leaning herself into me so that I can feel her ass against my groin!"
    "Wow - she really is into me!"
    "Feeling much the same way, I lean forwards."
    "As I haven't actually seen her face clearly yet."
    show minami close with dissolve
    minami.say "Hey there, big bro."
    minami.say "You're a way better dancer than I expected!"
    with hpunch
    mike.say "HUH...WHA...MINAMI?!?"
    menu:
        "Stop dancing":
            hide minami close
            show minami
            "Even with the dance-floor as crowded as it is, I still leap away from Minami."
            "The very same feelings that I was experiencing a moment before evaporate as I do so."
            "And in their place I feel shock and a creeping sense of horror at what just happened."
            show minami surprised
            minami.say "What's the matter, big bro?"
            minami.say "Did I poke you some place painful?"
            "Even with me reacting like I just did, Minami still seems to be oblivious to the reason why."
            "I shake my head as I hurry off of the dance-floor, feeling queasy at what just happened."
            show minami sad
            "Minami hurries after me, seemingly worried that I might be ill or something."
            minami.say "Tell me what's up, big bro!"
            minami.say "You're really starting to scare me now!"
            "I finally manage to get my head in order enough to turn around and face her."
            mike.say "Minami, what were you thinking back there?"
            mike.say "I'm your brother - you can't go doing...THAT to me!"
            show minami normal
            "The relief that was showing on Minami's face at my talking to her suddenly disappears."
            "And in its place is one of those innocent and yet annoying grins that she's so good at pulling."
            show minami happy
            minami.say "Aw, don't be such a prude, big bro."
            minami.say "Isn't that how people are supposed to dance in a place like this?"
            mike.say "Well...yeah, I suppose."
            mike.say "But not with their little sisters!"
            minami.say "Come on - we both know it's just a bit of fun."
            minami.say "And I promise that if you don't tell anyone I'm your sister."
            minami.say "Then I won't tell anyone you're my brother either!"
            hide minami with moveoutleft
            "And with that, she bounces back onto the dance-floor."
            "All I can do is stand there and watch."
            "That, and wondering what happened to my innocent little sister..."
        "Continue":
            hide minami close
            show minami happy
            "No matter how crowded the dance-floor is, my first instinct is to leap away from Minami."
            "But then the smile on her face and the way that she giggles at my reaction makes me stop myself."
            "When did I become so much of a prude that I can't see the funny side of things?"
            "Sure, it's a little outrageous for her to be pranking me like this."
            "But isn't this a perfect chance to show her that I'm still capable of being outrageous too?"
            minami.say "What's the matter, big bro?"
            minami.say "Did I poke you some place painful?"
            hide minami
            show minami close
            "I put my hands on Minami's waist and pull her a little closer."
            "And then I whisper in her ear."
            mike.say "How could you not?"
            mike.say "When I've got one as big as this..."
            show minami surprised blush
            "The look of shock that crosses Minami's face at this is more than enough payback for me."
            "And the expression of scandalous amusement that follows it is even better."
            show minami tehe
            minami.say "I knew there was a reason I still called you 'BIG bro'!"
            "I know I shouldn't, but I can't help laughing at Minami's terrible joke."
            "It means that my guard is down as we keep on dancing together."
            "Which in turn means that I'm totally unprepared for what happens next."
            "I swear that I don't know if it happens totally by accident."
            "Or if Minami somehow manages to flip up her dangerously short skirt on purpose."
            "But either way, the end result is still the same."
            "I feel the firm cheeks of her ass press into my groin again."
            "And this time they rub against my already painfully erect cock."
            "Even over the pounding music, I can hear Minami let out a sudden cry."
            "But then it seems to melt into a more mellow and sensual sound."
            show minami hunt
            minami.say "Oh, big bro..."
            minami.say "You're so big..."
            minami.say "It feels so..."
            mike.say "Ah, what was that, Minami?"
            mike.say "I couldn't hear you over the music?"
            "I say this as I hastily yank Minami off of the dance-floor and into another part of the club."
            "As lame as the excuse that I just used is, I don't want to know where that was going!"
            $ minami.siscon += 10
    $ minami.flags.sisconDelay = TemporaryFlag(True, 1)
    return

label minami_siscon_09:
    show bg secondfloor with fade
    "I'm walking innocently across the hallway to my room, when I hear the sound of someone calling my name."
    minami.say "Hey, big bro."
    minami.say "Come here - I got something to show you!"
    show minami with dissolve
    "I turn around to see Minami, almost bouncing on the spot like a hyperactive jack-in-the-box."
    "My interest piqued, I walk over to where she's standing, keen to indulge my little sister for a moment."
    mike.say "Minami, what's up?"
    mike.say "You look like you're on a sugar-rush, or something!"
    "Minami gives me one of those cute little smiles that she does so well."
    "Cocking her head on one side, she beckons me to come closer."
    "I'm not sure what the need for such secrecy is, but I decide to play along all the same."
    hide minami
    show minami close
    "As soon as I'm close enough for us not to be overheard, Minami leans in even closer."
    minami.say "You know how you used to be into cosplay, big bro?"
    "She says that like I was into it hard-core, but in reality I only ever dabbled."
    "Most of my efforts were pretty simple, and I only went to a couple of conventions."
    mike.say "Uh, yeah - I guess so."
    minami.say "Well, after you moved out, I got into it too."
    minami.say "You could say that you inspired me to follow in your footsteps."
    "Okay, it's a cliche, I know."
    "The perky little Asian girl that likes to dress up as characters from her favorite Manga and Anime."
    "But Minami's never been anything other than talented when it comes to the creative side of things."
    "And she tends to throw herself into her hobbies too, not doing anything without dedication and passion."
    "So I suppose that it shouldn't come as a surprise that she's into a scene like that."
    mike.say "That's really cool, Minami."
    mike.say "But I was never that good at it!"
    mike.say "I bet you're way better than I ever was."
    hide minami close
    show minami happy
    "I see Minami's eyes flash with pride at the compliment, and she smiles even wider than before."
    "I swear that her chest swells with pride as I stand there watching her too."
    "Suddenly, she reaches out and grabs my wrist with both hands."
    minami.say "You HAVE to come with me, big bro."
    minami.say "I brought some of my outfits with me."
    minami.say "And you'll seriously freak when you see me in them!"
    menu:
        "Refuse":
            "This started out as Minami just confessing her hobby to me and getting compliments in return."
            "But all of a sudden she seems to be getting super excited and even a little hyper over it."
            "I know how giddy Minami can become when she's wrapped up in something she's this passionate about."
            "And I really don't want to go encouraging her to indulge in stuff that'll keep her cooped up inside."
            "The best thing for her would be to get out there and socialize at college, get a real life of her own."
            mike.say "Nah, I'm okay, Minami."
            mike.say "I'd love to see what you've come up with, really I would."
            mike.say "But I need to catch up on my studies so badly it's unreal."
            show minami sad
            "Minami looks instantly deflated, almost on the brink of falling into a sulk."
            minami.say "But...but..."
            mike.say "Oh, that reminds me - I meant to ask how your studies are going too?"
            mike.say "I remember that I was so busy in my first year of college."
            mike.say "It meant I had almost no time for my hobbies either!"
            mike.say "Sucks, I know - but you gotta put in the time if you want the grades at the end of it."
            "Now she's staring at her feet, and I'm starting to feel like I've crushed her youthful spirit."
            minami.say "I...I guess you're right, big bro."
            minami.say "I've kinda been putting off hitting the books."
            minami.say "Maybe I should study some today?"
            "My smile in response to this is more genuine that you might think."
            "Because, despite all of the evidence to the contrary, I can be a proper adult when the need arises."
            mike.say "Good luck with that, Minami!"
            "I give her a thumbs-up as she turns to trudge up the stairs to the attic."
            hide minami with dissolve
            "And as she goes, I only slightly feel like I'm turning into a proper old man."
        "Agree":
            "I guess this is where I have to be more than a housemate and chaperone to Minami."
            "After all, she's not a robot - being creative is as important as her doing well at college."
            "Plus, she seems really eager to have my approval, and she did get into this after seeing me do it before her."
            "I suppose that I should be flattered that she thinks my old hobbies were anything other than lame."
            mike.say "Okay, Minami."
            mike.say "I was going to go hit the books."
            mike.say "But I think I can spare you a couple of minutes."
            "Minami let's out a piercing squeal of pure delight, and instantly begins to haul me up the attic stairs."
            show bg bedroom5 with irisin
            "As soon as we're inside of her room, Minami pushes the door shut and turns the lock."
            with vpunch
            "Once she's sure we won't be disturbed, I find myself pushed roughly down onto her bed."
            minami.say "Wait right there, big bro."
            minami.say "You're gonna LOVE this, I promise!"
            hide minami with moveoutright
            "I can only nod and watch as Minami hurries behind a screen that hides a corner of the room from view."
            "The sound of her busily stripping off comes from behind it, and then clothes start to fly around the place."
            "Every single item of clothing that Minami was just wearing is tossed over the screen."
            "I'm okay with this, until I realize that her bra and panties have landed next to me on the bed."
            "Instinctively, I try to toss them away."
            "But then I realize that this would mean actually touching my little sister's underwear!"
            "Before I can make up my mind which possibility is worse, I hear Minami call out again."
            minami.say "Check me out, big bro!"
            minami.say "What do you think of this little number?"
            "My head snaps up from my efforts to distance myself from Minami's underwear."
            show minami halloween with easeinright
            "But as soon as I see what she's wearing, I forget about everything else."
            minami.say "Pretty nice, huh?"
            show minami at center, hshake
            "Minami twirls around on the spot as she shows off the Japanese schoolgirl's uniform she's wearing."
            "It fits every cliche that I can think of, and probably several dozen unknown outside of Japan itself!"
            "Not only that, but the way she's twirling makes the incredibly short skirt ride up."
            "This means I can see the dangerously small pair of panties that she has on underneath as well."
            "Minami stops twirling and leans forwards, resting a hand on her knee."
            minami.say "I know it looks good from this angle."
            "Then she turns her back on me and proceeds to wiggle her ass an inch from my face."
            show minami tehe
            minami.say "But it's better from this one!"
            minami.say "Don't you think, big bro?"
            "I blink a couple of times before I regain the ability to speak."
            mike.say "Honestly, Minami - it's hard to find the words to do it justice..."
            show minami happy at center, vshake
            "Minami jumps up and down at this, treating me to yet another remarkable display at very close range."
            "Afterwards, I almost stagger down the stairs from the attic, heading for my bedroom."
            "But this time it's for to lie down and recover, rather than to hit the books..."
            $ minami.siscon += 10
    $ minami.flags.sisconDelay = TemporaryFlag(True, 1)
    return

label minami_siscon_08:
    show bg livingroom
    "It's one of those quiet moments, when everyone's in the same room at the same time."
    show sasha at left5
    show bree at right5
    with dissolve
    "[bree.name], Sasha and myself, sharing the same space and breathing the same air."
    "But we're all happy to be quiet, engrossed in out own little worlds."
    "That is until those worlds are subject to a hostile invasion by Minami."
    minami.say "Hey, you guys."
    minami.say "Look what I found!"
    show minami at top_mostright with moveinright
    "Minami comes bounding into the room, waving whatever she has clutched in her hand."
    sasha.say "Let me guess - is it some manners?"
    bree.say "Sasha, be nice!"
    bree.say "What you got there, Minami?"
    "Minami looks pleased with the attention and indulgence that [bree.name]'s showing her."
    show minami at center
    show sasha at left
    show bree at right
    with move
    "She hurries over to where the older girl is sitting, eager to show off her find."
    show sasha annoyed
    sasha.say "Ah, it's just a plain old pack of playing cards."
    sasha.say "BORING!"
    "Sasha's lack of enthusiasm seems to have no effect whatsoever on Minami."
    "Instead of being discouraged, she opens the packet and starts to shuffle the cards."
    bree.say "Hey, Minami - you're pretty good at that!"
    bree.say "Where did you learn to be a card-shark?"
    "I see [bree.name] casting a glance my way, as if suggesting that Minami might have picked it up from me."
    "But all she gets for her trouble is a wry smile and a quick shake of the head."
    mike.say "Sorry, not guilty!"
    mike.say "It was our Dad that taught her all of that."
    mike.say "He's into all kinds of tricks and stuff like that."
    mike.say "Sleight of hand and card-tricks, you know?"
    "Sasha rolls her eyes in disgust, clearly not impressed."
    sasha.say "Geez, I bet he was a riot at parties!"
    "But for all of the bile that she's pouring on things, [bree.name] and Minami don't seem to even notice."
    minami.say "Hey, big bro - do you remember that game we used to play?"
    mike.say "Ah, yeah, of course I do."
    mike.say "We used to play poker most of the time back home."
    minami.say "Whatever, I don't remember what it was called."
    minami.say "But I heard about this great version of it where you play for something really fun."
    minami.say "It's like, when you lose a hand, you have to take off some clothes!"
    "Did she just say what I think she said?"
    mike.say "You mean strip poker, Minami?!?"
    minami.say "Is that what it's called?"
    minami.say "Wow, I had NO idea it was so popular!"
    minami.say "Anyway, I think we should play a game of it."
    minami.say "[bree.name], Sasha, me and YOU!"
    sasha.say "Oh no, no way - you can count me out!"
    hide sasha
    show bree at right5
    show minami at left5
    with moveoutleft
    minami.say "Aww, Sasha, you're being a spoilsport!"
    minami.say "How about you, [bree.name], huh?"
    bree.say "I...well...I guess I could play a game...maybe..."
    bree.say "But I don't really know the rules..."
    minami.say "Yay, [bree.name], you're the greatest!"
    minami.say "I wish I had a big sister just like you!"
    "Before I know it, Minami rounds on me too."
    minami.say "What about you, big bro?"
    minami.say "You're not gonna be a boring stick-in-the-mud like Sasha, are you?"
    menu:
        "Refuse":
            "I don't even have to think before the response comes out of my mouth."
            "Shaking my head, I let out an burst of laughter."
            mike.say "Minami, there's NO way I'm playing strip poker with you."
            mike.say "That has to be one of the single worst ideas you've ever cooked up!"
            show minami sad
            "Minami looks instantly crestfallen, her eyes going wide and her lips beginning to quiver."
            "[bree.name] falls for it instantly, as I see sympathy appear in her own eyes."
            "But I know my little sister all to well to be taken in by one of her oldest tricks."
            mike.say "Hey, don't try the hurt-little-puppy routine on me, Minami!"
            mike.say "I know it always worked on Mom and Dad."
            mike.say "But it won't work on me, okay."
            mike.say "If anyone wants me, I'll be in my room."
            hide bree
            hide minami
            with dissolve
            "And with that, I walk out of there, leaving [bree.name] to her chosen fate."
            "Over my shoulder, I can still hear their conversation as I leave."
            bree.say "Are you sure that you still want to play, Minami?"
            bree.say "Won't it be less fun with only the two of us?"
            minami.say "Don't worry, [bree.name]."
            minami.say "I'll make sure it's EXTRA fun, now that all the boring people are gone!"
            "My last thought on the matter is that I hope [bree.name] knows what she's getting into..."
        "Agree to play":
            "I don't see how I can get out of playing at least one game with Minami."
            "Behind all of that feigned innocence, I know that she's a pretty mean poker player."
            "Chances are that she'll have [bree.name] stripped down to her underwear before she knows what hit her!"
            mike.say "Okay, Minami - you win."
            mike.say "Let's just get it over with and have a couple of quick hands."
            show bree surprised
            "At this, [bree.name] looks even more puzzled than before."
            bree.say "'Hands'?"
            bree.say "I thought you played poker with cards?"
            "Oh god, what is she getting herself into?"
            show bree normal
            "But almost as soon as we sit down and Minami's dealt out the first hand, I see what she's up to."
            "She could easily take advantage of [bree.name]'s inexperience, but she doesn't."
            "Instead she seems to be deliberately making rookie mistakes, as if she's trying to lose."
            "At this rate, she'll be naked before either [bree.name] or myself have shed a single piece of clothing."
            "It's then that a plan pops into my head, one that'll see me roundly humiliated."
            "But if I'm lucky, it'll keep me from having to see all of my little sisters rounded bits!"
            "I start copying Minami's own efforts, trying to play even worse than she is herself."
            "The only reason that it works is because, as good as she is at poker, I'm better."
            "Pretty soon I'm sitting there in just my shorts, blushing a suitably deep shade of red."
            "[bree.name] still has most of her clothes on, and seems bemused by the situation."
            "But Minami's smiling like a cat that got the cream."
            show bree happy
            bree.say "Wow, [hero.name], you're really bad at this game!"
            show minami happy
            minami.say "Yeah, [bree.name], he sure is!"
            minami.say "But at least he made a good showing of showing himself off!"
            show minami tehe
            "She gives me a quick wink while checking out my exposed body."
            "And it's then that I realize that the little minx has double-crossed me."
            "She never intended to strip off her own clothes, just to get me out of mine!"
            "All I can do is seethe in silence."
            "That and vow never to play another hand of poker with her while she's staying here..."
            $ minami.siscon += 10
    $ minami.flags.sisconDelay = TemporaryFlag(True, 1)
    return

label minami_siscon_07:
    show bg livingroom
    "One of the weirdest things about having Minami living under the same roof as me is seeing her becoming part of the daily routine."
    "Sure, I can still remember what it used to be like when we were both living back at home while growing up."
    "But I've gotten so used to this being my home now that seeing elements of my former life here is pretty strange."
    "It's made even stranger by the fact that I keep seeing Minami doing all of the same stuff that [bree.name] and Sasha do too."
    show bree sleep at left5 with dissolve
    "Point in case - I just walked into the sitting room and happened upon [bree.name] sitting there, playing videogames in her underwear."
    "Don't think I'm getting jaded here, as it's still quite a sight to see!"
    "But you just kind of find yourself getting used to it after a while, and it's not such a big deal anymore."
    show minami underwear norobe at right5 with dissolve
    "What's a much bigger deal to me is the fact that she's playing alongside Minami."
    "And I don't know if she's doing it out of habit, or else just to get into the spirit of things around here."
    "But Minami's also sitting there in nothing but her panties and a cut-off T-shirt too!"
    "I must have been standing there for longer than I realized."
    "As [bree.name] notices my presence and pauses the game while she glances over her shoulder at me."
    bree.say "Oh, hey, [hero.name]."
    bree.say "You should have told me that Minami was such a sick gamer!"
    "Minami looks a little petulant at first, as though she's annoyed at the interruption to her game."
    "But at the mention of my name, she instantly becomes the very definition of sweetness and light."
    minami.say "Big bro, you should see how great [bree.name] is at this game!"
    minami.say "I mean really - she's like WAY better than you!"
    "I give this obvious insult a weak smile."
    mike.say "Well, I have been busy with work and college recently."
    mike.say "I haven't had much time for games..."
    show minami happy
    "Minami bursts into a fit of giggles at this, covering her mouth with one hand."
    minami.say "Why so serious, big bro?"
    minami.say "You sound more like Dad every day!"
    show bree happy
    "[bree.name] can't keep from snickering at this too, visibly enjoying my discomfort."
    bree.say "Why don't you sit down and watch me beat Minami's ass, [hero.name]?"
    minami.say "Yeah, big bro - watch us, please!"
    minami.say "Or have you got to go take a class at boring school?"
    menu:
        "Refuse":
            "I'll admit that I've accepted pretty much the same offer from [bree.name] many times in the past."
            "And I'll also admit that my motivation for doing so hasn't been to watch the game she was playing."
            "Like any serious gamer, she gets pretty animated when engrossed in the experience."
            "But my guess is that Minami probably falls into the same category as well."
            "So the last thing that I want is to sit here and watch her half-naked body jiggling up and down."
            mike.say "I'll have you know that I'm top of the class at boring school."
            mike.say "My tutors say that, with real hard work, I'll be fossilized before the age of thirty!"
            show minami annoyed
            show bree normal
            "Minami rolls her eyes in obvious disgust, and turns her attention straight back to the game."
            minami.say "Urgh..."
            minami.say "You're no fun anymore!"
            "[bree.name] holds my eye for a little longer, a wry smile playing in the corners of her mouth."
            "I can see that she understands where I'm coming from far better than Minami ever could."
            "And even when she turns her own attention back to the game too, I still feel like she gets it."
            "I try to keep that in mind as I turn and walk out of the room."
            "Sometimes being the responsible adult in a situation means that you have no choice but to be boring."
        "Stay and watch":
            "I nod hastily, trying to banish the unwanted image of [bree.name] doing anything to my little sister's ass from my mind's eye."
            "Although I'd never admit as much to Minami, that comment about getting more like Dad really hurt."
            "But maybe by showing that I'm willing to watch their gaming session I can start to change her mind?"
            "So I flop down onto the sofa, holding up my arms in a gesture of surrender."
            mike.say "Okay, okay - you win."
            minami.say "Yay!"
            show minami tehe
            minami.say "Okay, [bree.name] - let's get it on!"
            minami.say "I'm gonna make you beg for mercy!"
            show bree evil
            bree.say "Oh no...no way."
            bree.say "You'll be the one that gets the spanking, Minami!"
            "Fuck me - are they doing this on purpose?!?"
            "Even before they get started, my head is already full of vivid pictures that make me want to blush."
            "And before too long, they're both so into it that the inevitable jostling and jiggling begins in earnest."
            "What - did you think that girl gamers sit still and stay demure the whole time?"
            "Oh god...have you ever visited the planet Earth?"
            "They couldn't sit still if their lives depended on it."
            "Within mere minutes, [bree.name] and Minami are bouncing up and down on their asses, right in front of me."
            "And it takes no time whatsoever to figure out that neither of them is wearing a bra, either!"
            "I don't know where to look - no, that's a lie."
            "I know exactly where I have to look, and that's straight at the TV screen."
            "The only problem is that I can see their reflections in it too."
            "And, if you'll allow me the use of an awful gaming-related pun."
            "I can feel my own joystick wanting to play too."
            "As slowly and surreptitiously as possible, I reach across and grab a cushion."
            "Pinning it to my groin, I try with all of my might to force such thoughts out of my mind."
            "But then [bree.name] and Minami actually start slapping each other and landing weak punches."
            "Oh shit - what if they start wrestling or something?!?"
            "But then, Minami's relative youth throws me a lifeline."
            show minami angry
            minami.say "Argh!"
            minami.say "NO WAY - this is bullshit!"
            hide minami
            show bree surprised at center
            with moveoutright
            "I watch as she gets up and throws down her controller before storming out of the room."
            "How crazy is that - saved by a rage-quit!"
            "[bree.name] looks almost as surprised as me, glancing back over her shoulder in my direction."
            bree.say "Wow, that's some temper she had on her!"
            bree.say "You wanna take over, [hero.name]?"
            show bree normal
            "Painfully aware of what's going on in my shorts right now, I can only smile and shake my head."
            mike.say "No thanks - I'm fine right here..."
            $ minami.siscon += 10
    $ minami.flags.sisconDelay = TemporaryFlag(True, 1)
    return

label minami_siscon_06b:
    show bg mall1
    "I don't like coming to the mall when I have to do any actual serious shopping."
    "And I know that sounds crazy, because the whole idea of a mall is to shop."
    "But hear me out on this one, okay?"
    "I do most of my actual shopping online."
    "It's quicker, easier and comes with the added bonus of not having to deal with actual people."
    "So when I go to the mall, it's really more of a social thing, you know?"
    "I like to stroll along, window-shopping and taking it all in."
    "And it's even better when I'm doing that with a date too!"
    "So you can imagine that Christmas shopping with Minami isn't really my thing."
    "The mall's packed to bursting with rude shoppers, elbowing and pushing at me."
    "And I have to hurry to follow Minami as she slips through the crowd with ease."
    "Honestly, it's like she's some kind of annoying retail fairy or something!"
    "She flits from one window to the next, totally forgetting why we're here."
    mike.say "H...hey!"
    mike.say "Minami..."
    mike.say "Slow down!"
    "I have no idea if Minami actually hears what I'm saying."
    "But luckily for me she seems to stop and beckon me over at the same time."
    minami.say "Big bro..."
    minami.say "Over here - quick!"
    "I do my best to get over to where Minami's standing."
    "But it takes more than a little effort on my part."
    "I stand on a few feet and get some dirty looks."
    show minami
    "And then I'm finally standing behind Minami."
    minami.say "What took you so long, big bro?"
    mike.say "I had to fight my way over here, Minami!"
    mike.say "In fact, I think some woman kneed me in the groin back there!"
    minami.say "Oh, never mind that."
    show minami happy
    minami.say "Just look at what they've got in here!"
    "Just like that, Minami dismisses my concerns."
    "She's far more interested in the contents of the window."
    "I lean in to get a better look, my head almost side-to-side with Minami's."
    mike.say "What is it?"
    mike.say "We're supposed to be shopping for gifts, remember?"
    "Just as I say this, the crowd of passing shoppers seems to surge."
    show minami surprised blush close
    "The result is that I'm pushed into Minami."
    "And, in turn, she's pressed against the glass of the window."
    "I hear her squeal in surprise and alarm."
    "But I also feel her body as it's trapped between mine and the glass."
    "My groin is pushed hard against her petite little backside."
    "Instantly I try to pull back, but the crowd holds me in place."
    "So all I succeed in doing is grinding myself against Minami."
    minami.say "Wha..."
    minami.say "What the hell?!?"
    minami.say "Big bro - what are you doing?!?"
    mike.say "I...I'm sorry, Minami!"
    mike.say "I got pushed..."
    mike.say "I didn't mean to..."
    show minami annoyed
    "Minami lets out an exasperated sigh."
    "And then she tries to resolve the situation herself."
    "Which only makes things worse as she wriggles against me."
    minami.say "Oh..."
    minami.say "Ah..."
    minami.say "What have you got in your pocket, big bro?"
    minami.say "It feels really hard..."
    "Suddenly I see a gap in the crowd."
    "I see that the shop is pretty empty too."
    show minami surprised -blush
    "And so I hustle Minami inside without stopping to ask her permission."
    "She opens her mouth to protest, but then sees where we're headed."
    "Minami helps to push through the throng of bodies."
    "And a moment later we're inside the shop."
    scene bg clothesshop
    show minami normal
    with fade
    minami.say "I get it, big bro."
    minami.say "You saw the stuff in the window, yeah?"
    show minami tehe
    minami.say "And it's SO cute you had to come in here!"
    "I look at Minami in confusion."
    "I never even got the chance to see what was in the damn window."
    "But she doesn't seem to be interested in reading my expression."
    show minami happy
    minami.say "I have to try this on!"
    minami.say "And this..."
    minami.say "Ooh...and this one too!"
    "Before I can object, she's shoved half-a-dozen thing into my hands."
    "And then she's off around the shop, adding more stuff to the pile!"
    "In hurry after Minami as best I can, trying in vain to get her attention."
    mike.say "Minami..."
    mike.say "I thought you'd seen a gift for someone else in here?"
    mike.say "We're supposed to be shopping for Christmas gifts, remember?!?"
    show minami normal
    minami.say "Yeah, yeah, big bro, whatever..."
    minami.say "I won't be long, okay?"
    minami.say "We can still do all of that after I buy something cute for myself!"
    hide minami with dissolve
    "Nothing I say seems to make a difference."
    "Minami just tunes me out as she goes here and there around the shop."
    "The next thing I know, I'm standing outside a cubicle in the changing rooms."
    mike.say "Minami!"
    mike.say "Have you tried all that stuff on yet?"
    mike.say "Seriously - this place will be closing soon!"
    minami.say "Just a minute, big bro!"
    minami.say "I think I want this outfit, but I'm not sure."
    minami.say "Tell me what you think, okay?"
    "What is this - a damn fashion show?!?"
    "I open my mouth to tell Minami off for a second time."
    show minami underwear norobe with dissolve
    "But that's when she sweeps the curtain between us aside."
    "And the words die on my tongue."
    minami.say "Well, big bro..."
    minami.say "What do you think?"
    "It's hard to say what I think in that moment."
    "And that's because it's not my brain that's in charge."
    "Minami's standing there, wearing nothing but underwear."
    "So it's my cock that takes over doing all the thinking for me!"
    "But underwear doesn't really cut it, not to describe what she has on."
    "That's lingerie, undergarments designed simply to flatter and display."
    "And it's doing just that to Minami's body right now!"
    "Bra, panties, stockings and garter-belt - all of it assaults my eyes."
    show minami tehe
    "Then Minami makes it ten times better by posing and pouting."
    "Every inch of her elfin body is on show, and it looks incredible."
    "She's making me hard as a rock, and I can't tear my eyes away."
    minami.say "Say something, big bro!"
    minami.say "Or you'll make me think that you hate it!"
    menu:
        "Compliment Minami":
            "Suddenly all thought of the Christmas shopping disappears."
            "Just like that, it vanishes from my mind in a puff of sexual desire."
            "The grin on my face must be a mile wide."
            "Because I can see the look of delight on Minami's face at my reaction."
            mike.say "Wow, Minami...just...WOW!"
            mike.say "You have to buy that - all of it!"
            show minami happy
            "Minami giggles with delight."
            "And she covers her mouth with one hand."
            "All of which only serves to make her look even hotter."
            minami.say "Aw..."
            minami.say "That's so sweet of you to say, big bro!"
            show minami sad
            minami.say "I know it's a little naughty of me."
            minami.say "I mean, wasting time when we're supposed to be Christmas shopping..."
            mike.say "Ah, screw the shopping, Minami!"
            mike.say "We can do that anytime."
            mike.say "I don't get to see you dressed like that every day!"
            show minami normal
            "Minami laughs again, but this time it's lower and more knowing."
            "She leans closer to me, raising an eyebrow as she does so."
            hide minami
            show minami close underwear norobe
            minami.say "So that means you'd like to see me in my underwear more often, big bro?"
            mike.say "Yes...I...I mean no...I mean..."
            show minami close happy
            minami.say "Aw...you sound confused!"
            minami.say "That's how nice compliments make me feel."
            minami.say "And the one you just gave me was SO nice."
            show minami close normal blush
            minami.say "So nice it'll make my head spin for ages."
            minami.say "And I might do things that are pretty crazy too."
            minami.say "Like putting on my underwear and then forgetting the rest of my clothes!"
            minami.say "Then I might go and forget which door is the one to my bedroom..."
            "I'm so entranced by Minami's words that I don't see what her hand is doing."
            "The first thing I know about it is when she begins to caress my cock."
            "Minami strokes and squeezes it through my pants, making me gasp at the sensation."
            mike.say "I...I could help you out, Minami!"
            mike.say "Remind you...maybe?"
            minami.say "I'm sure you could, big bro."
            minami.say "You could bring me back to HARD reality!"
            "With that, Minami plants a quick kiss on my lips."
            hide minami with dissolve
            "And then she's gone, darting back behind the curtain."
            "I look around as my cheeks flush red."
            "It's hard to straighten up while my cock is this hard."
            "But I do my best to sort myself out as I wait for Minami."
            show bg mall1
            show minami
            with fade
            "Neither of us mentions what just happened as we keep on with the shopping."
            "Minami's her usual self, flitting here and there as the whim takes her."
            "But she swings the bag with her new lingerie in it happily."
            "And that's because she knows that I keep staring at it."
            "Staring and wondering just when I'll get to see her in it again."
            $ minami.siscon += 10
            $ game.active_date.score += 20
        "Tell Minami off":
            "Suddenly I feel the effects of Minami's sexy body wearing off."
            "I give myself a shake, shuddering as I regain control of my senses."
            "And then I fix her with my sternest of disapproving stares."
            mike.say "Minami..."
            mike.say "Of all the dumb shit you could pull!"
            mike.say "We haven't got time for you to parade around in your pants!"
            show minami sad
            "Instantly Minami's mood changes."
            "She looks down at her feet and she seems to shrink a little too."
            "All of the power she had a moment before disappears at the same time."
            "Now she just looks like a silly little girl that's been scolded by an adult."
            minami.say "Y...you don't have to be so mean, big bro!"
            show minami cry
            minami.say "I was only trying some stuff on..."
            minami.say "I...I'll take it off, okay?"
            "I'd been expecting Minami to fire straight back at me."
            "For her to have one of her infamous strops in the dressing room."
            "But now I'm worried that she's going to burst into tears."
            mike.say "I'm sorry, Minami."
            mike.say "Maybe I was a bit harsh on you just now."
            mike.say "But it's getting so close to Christmas, you know?"
            mike.say "And there's so much stuff to get done before the big day."
            show minami sad
            "Minami nods, but she can't help sniffling a little too."
            hide minami
            "She closes the curtain and changes back into her own clothes."
            show bg mall1
            show minami sad
            with fade
            "And she's quiet the rest of the time we're at the mall."
            "Which means that we get most of the Christmas shopping done."
            "But it also means that I end up feeling guilty too."
            "Maybe that was her intention all along?"
            $ game.active_date.score -= 20
    $ minami.flags.sisconDelay = TemporaryFlag(True, 1)
    return

label minami_siscon_06:
    show bg pool with dissolve
    "It's the first time the weather's been anything close to decent since Minami moved in, hot sun and a blue, cloudless sky."
    "And as usual, everyone seems to have made the unconscious decision that it's going to be a day spent mostly lounging by the pool."
    show bree swimsuit
    "I make it out there a little time after [bree.name], who's already laid on one of the loungers in her swimsuit."
    "It's a toss-up as to whether Sasha will join us or instead choose to preserve her pale complexion a little longer."
    "But I'm fully expecting to see Minami make an appearance, as she was thrilled at the idea of us having our own pool."
    "She's still inside somewhere, no doubt getting herself ready for a swim."
    "So I just settled down in the lounger beside [bree.name], happy to wait for my little sister to show up."
    show bree happy
    "At the sound of me sitting by her, [bree.name] makes a small, satisfied sound and looks up with a smile on her face."
    bree.say "Mmm..."
    bree.say "What's with the sun today, [hero.name]?"
    bree.say "I already put some sun-screen on."
    show bree normal
    bree.say "But I feel like I'm burning to a crisp out here!"
    mike.say "Yeah, it's crazy hot today."
    mike.say "Maybe you should put another layer on?"
    "[bree.name] moans and stretches in a lazy manner, putting me in mind of an exhausted cat."
    bree.say "Oh, I just can't find the energy to move."
    bree.say "I know it's cheeky of me to ask - but would you mind..."
    "Would I mind rubbing sunscreen into my hot, blonde housemate as she reclines in her swimsuit?!?"
    "No wonder [bree.name] didn't feel the need to actually finish asking that question!"
    "A second later, the sunscreen's in my hand and I'm squeezing out a generous blob between my sweaty palms."
    "[bree.name] gives me a lazy, languid smile as I hover over her in anticipation."
    "Laid on her belly, she surprises me by reaching back and undoing the top of her swimsuit."
    "She sees my eyes go wide at this and no doubt hears me gulp in amazement."
    show bree flirt blush
    bree.say "What's the matter, [hero.name]?"
    bree.say "You wouldn't want me to get any nasty tan lines, would you?"
    "I shake my head at this, already reaching out to begin the task that I've been assigned."
    "Making sure to do a thorough job, I start at the nape of [bree.name]'s neck and work my way down her back."
    "It seems only right to massage her skin as I go as well - just to make sure the sunscreen is well rubbed in."
    "[bree.name] keeps me motivated and lets me know that I'm doing a good job with frequent sighs and appreciative noises."
    "And by the time I'm done, I feel like I've drawn all the heat out of her body and into mine instead!"
    show minami swimsuit at top_mostleft
    show bree at right5
    with moveinleft
    minami.say "Woah, big bro - you're like a pro masseur or something!"
    "At the sound of Minami's voice, my head jerks around and my face flushes with embarrassment."
    "I see that she's standing a couple of feet away from the loungers, a huge grin on her face."
    "As she's barefoot, neither of us could have heard her walking over here."
    "And what's worse is that I have no way of knowing just how long she's been watching either!"
    minami.say "Would you mind giving me the same treatment [bree.name] just got?"
    minami.say "I'm afraid I might miss a spot."
    minami.say "And you know how easily I burn, right?"
    "I look at Minami for a moment, trying to figure out what the best course of action would be."
    "She's wearing a bikini that leaves little to the imagination, with no towel or sarong wrapped around her."
    "And even from this distance, I'm already uncomfortably aware of how it shows off her figure."
    "Sure, Minami's petite and hardly buxom in terms of her build."
    "But there's just no denying the fact that she's grown into a woman while I was away from home..."
    menu:
        "Refuse":
            "Maybe I'm being a hypocrite here, and I should really have thought before I agreed to help [bree.name] out."
            "But all the same, there has to be a difference between my housemate and my little sister, right?"
            "Even if I do what she wants, I'd still be fooling myself into thinking that it was purely innocent."
            "I mean, I can hardly look at Minami in that swim-suit for more than a couple of seconds before it gets awkward."
            "The last thing I need is to do something that might encourage me to see her in that way."
            mike.say "Come on, Minami, get real!"
            mike.say "What, did your last slave die of?"
            show bree happy -blush
            "[bree.name] can't help breaking out into giggles at this."
            "She tries to cover her mouth, but the damage is already done."
            show minami angry
            "Minami's face darkens and she begins to openly pout at being rebuffed."
            "She crosses her arms over her chest, and even makes a point of stamping her foot on the ground."
            "I guess that's her best attempt at looking threatening."
            "But it doesn't help that all her efforts do is serve to make her look cute, like an angry puppy."
            minami.say "Hey, that's not fair!"
            minami.say "How come you'll do it for [bree.name] and not me?!?"
            "I shoot [bree.name] an exasperated look, rolling my eyes for effect."
            mike.say "Erm, maybe because she asked like an adult, Minami."
            mike.say "And not like a petulant little kid!"
            show minami surprised
            "I watch as Minami's mouth literally drops wide open."
            "For a moment, she stands there as still as a statue."
            show minami angry
            "But then she plants one balled fist on her hip and points at me with her other hand."
            minami.say "What gives, big bro?"
            minami.say "You're supposed to be nice to me while I'm living here."
            minami.say "And that was just plain mean!"
            "I shrug her words off, enjoying how easily her little tantrum is to ignore."
            "Plus, it feels good to have [bree.name] watch me handle Minami with such ease and maturity."
            mike.say "Whatever, Minami."
            mike.say "I'm pretty sure that doesn't include having to rub sun-screen into your ass for you!"
            minami.say "Ooh, you make me so mad sometimes!"
            minami.say "You just wait 'til I tell Mom and Dad what you did."
            minami.say "You're going to be in so much trouble, big bro!"
            hide minami
            show bree normal at center
            with moveoutleft
            "And with that, she turns on her heel and storms back inside the house."
            "[bree.name] looks at me with vague concern on her face."
            "But I just shrug again, dismissing it as nothing to worry about."
            mike.say "Now then, [bree.name], where were we?"
            mike.say "You sure you have enough sun-screen on your legs?"
        "Agree":
            "You know, if I refuse to do the same for Minami, I'm kind of admitting that I'm a hypocrite."
            "Worse still, that I'm also the kind of massive perv that only helps a girl out for the sake of a cheap thrill."
            "Plus, I need to get over these dumb hang-ups that I have about Minami and her body."
            "I can't keep on averting my eyes every time she walks into the room wearing something slightly revealing."
            "I guess what I really need is to start seeing Minami as an adult, because she's certainly not a kid anymore!"
            mike.say "Ah, yeah, I suppose so, Minami."
            mike.say "Why don't you come and take this lounger?"
            mike.say "I can put this stuff on you while you're laid down."
            show minami happy
            "Minami nods and smiles, clearly delighted to have gotten her own way so easily."
            show minami at left4 with move
            "But as she hurries over to take the lounger, I see [bree.name] raise her eyebrows at me."
            "I shake my head at her in return, dismissing the unspoken question that she's asking."
            minami.say "Oops - I'd better whip my top off too."
            minami.say "I don't want any tan-lines either!"
            mike.say "Sure, Minami."
            mike.say "Whatever you say..."
            show minami topless
            "My eyes get steadily wider as I watch Minami untie her bikini top."
            "I see the motion of her petite, yet perfectly-formed breasts as they succumb to gravity..."
            "Oh god - what am I even doing here?!?"
            "My own little sister is already making me get hard."
            "And I haven't even laid a finger on her yet!"
            minami.say "There you go, big bro."
            minami.say "But don't worry - you don't have to be too gentle with me."
            minami.say "Sometimes, I like it a little rough..."
            hide bree
            show minami at center
            with moveoutright
            "I try not to let what Minami just said sink in as I squeeze the sun-screen into my palm."
            "All I have to do is treat this like it's a favor, or like I really am a professional masseur."
            "But almost the second that I put my hands on Minami's shoulders, she lets out a deep, almost sensual groan."
            minami.say "Mmm..."
            minami.say "That feels SO good, big bro."
            minami.say "It's like you have magic hands or something!"
            "Again, I try to filter out the implications of what she's saying and the sounds that she's making."
            "But Minami only adds to the situation by responding to my touch in the same manner."
            "Wherever my hands go, she shivers and shudders, as if turned-on by the contact."
            "And when I finally get as low as her waist, she raises her ass like can't help herself!"
            mike.say "OKAY...I mean, okay..."
            mike.say "That's it, Minami - I'm all done!"
            mike.say "I mean...you're all done."
            show minami hunt
            "Minami looks back over her shoulder at me, her eyes wide with what looks worryingly like arousal."
            minami.say "Ah, thanks, big bro."
            minami.say "You rubbed it SO deep into me."
            minami.say "It was like I could feel you touching me on the inside..."
            "After that I decide that a dip in the cold water of the pool is in order."
            "And I'm sure to stay submerged below the waist until I'm sure that it's safe to emerge once more..."
            $ minami.siscon += 10
    $ minami.flags.sisconDelay = TemporaryFlag(True, 1)
    return

label minami_siscon_05:
    scene bg livingroom with fade
    "I hear Minami struggling with something before I actually see her, and so I hurry to help based on that alone."
    "But as it turns out, I'm a little too late, getting to her just as she drops the armful of books she has onto the floor."
    "She curses out loud, letting me know that she's learned a few new profanities since I moved away from home."
    show minami angry with dissolve
    minami.say "Ah, shit, shit...fuck!"
    "And then she immediately crouches down and starts trying to gather up the books once more."
    "All I can do by then is kneel down and join in her efforts, gathering up the larger titles myself."
    mike.say "Don't try to carry the whole lot, Minami."
    mike.say "Here, let me help you with those, okay?"
    show minami happy
    "Minami looks up and gives me one of the sweet smiles that I always associate with her in my mind."
    minami.say "Thanks, big bro."
    minami.say "It was kinda dumb of me to think I could manage on my own!"
    "I give Minami a smile in return, not even needing to ask what all of the books are for."
    "Every single one of them is a text-book, and all of them have the familiar label of the college library too."
    "As we stand up and Minami starts to make for her bedroom in the attic, I follow on her heels."
    mike.say "Is this really the reading you've been given for your first semester?"
    show minami normal
    minami.say "What - you think I'd sit around reading this kind of stuff for fun?!?"
    minami.say "It's so much more intense than school ever was."
    show minami sad
    minami.say "I feel like I'm falling behind already, big bro!"
    "I shake my head and shrug, feeling helpless in the face of Minami's plight."
    mike.say "I must have had this much to wade through back when I started my course."
    mike.say "I guess my brain just dealt with the trauma by making me forget all about it."
    mike.say "That or I burned out enough brain-cells to erase it from my memory."
    show bg secondfloor
    show minami normal
    with fade
    "As we reach the foot of the attic stairs, Minami stops and gives me one of those sideways glances."
    "I'm immediately on guard, as it's one of those things she does as a preamble to asking for something."
    mike.say "Minami - why are you looking at me like that?"
    minami.say "Weeeell..."
    minami.say "I was just thinking how you did pretty well at school, big bro."
    minami.say "And you always told Mom and Dad you were passing college too..."
    mike.say "Urgh..."
    mike.say "Come on, Minami - out with it already!"
    show minami tehe
    minami.say "Well, what if you helped me out a little, huh?"
    minami.say "I don't mean help me cheat or anything."
    minami.say "Just give me some pointers - like a tutor, you know?"
    minami.say "But better, because it'd be you, and not some stuffy old guy!"
    menu:
        "Refuse":
            mike.say "Ah, I don't know if that would be such a good idea, Minami."
            show minami sad
            "I can see the look of disappointment sweep over Minami's face."
            minami.say "Aww..."
            minami.say "PLEASE, big bro."
            minami.say "You're so smart, it'd be easy for you, I just know it!"
            "Minami always was good at piling on the flattery when she wanted to."
            "But an ego-rub won't change the fact that I don't really want to do it."
            mike.say "No, Minami - I really couldn't."
            mike.say "I'm behind with my own studies as it is."
            mike.say "And you're doing a totally different subject anyway."
            mike.say "I wouldn't know where to even start."
            minami.say "Then I can teach you so you can teach me, right?"
            "I shake my head as I put the books down on the bottom step and begin to back off."
            mike.say "I'm sorry, Minami."
            mike.say "Maybe you could check out the bulletin board at college?"
            mike.say "There's usually a couple of older students offering their services as tutors every semester."
            hide minami with dissolve
            "With that I turn and walk away, signaling the end of the conversation."
            "Sure, I feel pretty bad about basically leaving Minami to fend for herself."
            "But these are just some of the skills she's going to have to learn."
            "And she'll need them if she wants to survive in the big, bad world too."
        "Agree to help":
            "I'm all set to say no and turn Minami down flat."
            "But then more memories of my own first semester at college come flooding back."
            "I remember just how hard it was for me, how I struggled to get to grips with my studies."
            "If I'd had someone to help me out, things would have gone a lot more smoothly."
            mike.say "Okay, Minami - I'll spare a little time to help you get started, okay?"
            mike.say "But I can only handle the basics, you know - give you some study tips?"
            mike.say "I never took the same subjects and classes as you."
            show minami happy
            "Minami's grin spreads until it seems to reach from ear to ear."
            minami.say "Oh, thanks, big bro."
            minami.say "I know I can handle anything if I have YOUR help!"
            show bg bedroom5
            show minami normal
            with fade
            "Minami leads me up the stairs and into the attic, dropping the books on her bed."
            "Instantly I can see several changes that could be made to help out with her studies."
            mike.say "Have you been using the desk, Minami?"
            minami.say "Well...yeah."
            minami.say "Why wouldn't I?"
            mike.say "It's not very organized, that's the problem."
            "I wave Minami over and have her sit at the chair before the desk."
            "And then I pull up a stool and sit by her side."
            mike.say "If you have a system that works like this, then you'll do better."
            "I start reorganizing the books and stationery on the desktop."
            "Minami watches my every action, leaning in close to see what I'm doing."
            minami.say "Oh, I see!"
            minami.say "That's a real help, big bro."
            show minami close
            "It's only at this point I begin to realize just how close she is to me."
            "And then I feel the sensation of her hand on my thigh, sliding upwards..."
            "Minami turns her head towards me, her face no more than an inch from mine."
            minami.say "I'm SO grateful for all your help, big bro."
            show minami close hunt
            minami.say "Sometimes, I wonder what else you could show me..."
            "Her voice is quiet and breathy, and sounds laden with hidden meanings."
            "I've never heard Minami talk like this before, and it catches me completely off-guard."
            "But what snaps me out of it a moment later is the feeling of her hand reaching my groin..."
            mike.say "Well...that's enough for now, Minami!"
            "I almost leap up as I blurt out the words, in danger of tumbling over backwards as a result."
            "Minami doesn't seem in the least bit thrown at any of this."
            show minami happy
            "Instead she just smiles at me, a perfect picture of innocence."
            minami.say "Thanks again, big bro."
            minami.say "Can't wait to see what you teach me next time!"
            $ minami.siscon += 10
    $ game.room = "secondfloor"
    $ minami.flags.sisconDelay = TemporaryFlag(True, 1)
    return

label minami_siscon_04:
    scene bg bedroom1 at dark with fade
    $ minami.flags.sisconDelay = TemporaryFlag(True, 1)
    "I'm sound asleep, dead to the world until and I have no intention of stirring before my alarm goes off in the morning."
    "But then I feel something shaking me out of my slumber, dragging me towards waking, whether I like it or not."
    "At first I have no idea what could have done it, as everything is still bleary and confusing."
    scene bg blank
    pause 0.2
    scene bg bedroom1
    pause 0.1
    show bg bedroom1 at dark with dissolve
    "Then there's a sudden flash of light that illuminates the room, even through the closed blinds."
    play sound thunder_single
    play sfx1 thunder_deep
    "The terrible rumble that follows close on its heels explains everything a moment later."
    "There's a thunderstorm going on out there, and quite a spectacular one by the look of it too."
    "I turn over in bed, assuming that the sheer volume of the thunder was enough to wake me."
    "I've never been afraid of that kind of thing, and so I expect to fall back asleep without a problem."
    "But in the lull between the cracks of thunder, I realise that I can also hear a second sound."
    play sound door_banging
    "The difference is that this one is coming from inside the house."
    "To be more specific, it's the sound of someone hammering on my bedroom door."
    "I try to ignore it, hoping that whoever's wanting to bother me in the middle of the night will take a hint."
    "But they don't, and just keep on knocking on the door ever more frantically."
    "Swearing under my breath, I toss off my bedclothes and swing my legs off of the mattress."
    "I have a choice selection of insults and curses prepared for the person I find on the other side of the door."
    show minami c sad sleep at center, dark with fade
    "But when I yank it open, I'm presented with the sight of Minami."
    "She's wrapped up tightly in a blanket, and her hand is still outstretched for another round of knocking."
    scene bg blank
    pause 0.2
    play sound thunder_single
    scene bg bedroom1
    show minami c surprised sleep
    pause 0.1
    show bg bedroom1 at dark with dissolve
    "It's hard to make out the expression on her face, but then another flash of lightning illuminates her."
    show minami c surprised sleep at center, vshake
    "Minami jumps and lets out a terrified squeal, her eyes wide and full of fear."
    "In that moment, she looks like something out of a horror movie, and I can't help crying out in alarm myself."
    mike.say "Shit, Minami..."
    mike.say "You nearly gave me a heart attack!"
    mike.say "What on earth do you want?!?"
    show minami cry
    minami.say "It's the storm, big bro."
    minami.say "I'm all alone up there - and I'm scared!"
    "Of course, Minami was always terrified of thunder and lightning as a kid."
    "I guess I just wrongly assumed that she'd have grown out of it by now."
    "It can't help that there are no blinds up in the attic either."
    mike.say "Erm...okay, Minami."
    mike.say "But what do you want me to do about it?"
    show minami sad
    "Minami takes a step forward, almost crossing the threshold into my bedroom."
    minami.say "I was kinda wondering..."
    minami.say "Could I sleep with you?"
    minami.say "Just for tonight, until the storm is passed?"
    menu:
        "Refuse":
            "Is she actually serious?"
            "Minami's almost a grown woman, starting her course at college and making her own way in the world."
            "Back when we were kids, I'd have agreed to let her jump into my bed without hesitating."
            "But we're adults now, and that kind of thing just doesn't feel right anymore."
            "Plus, she really needs to start relying on herself if she's going to survive in the big, bad world."
            show minami sad
            mike.say "Nice try, Minami!"
            mike.say "But you're a big girl now."
            mike.say "Plus there's no room for you in my bed - I'd have to sleep on the floor."
            show minami cry
            minami.say "Nooo, big bro!"
            minami.say "Please let me sleep with you."
            minami.say "I'll be so quiet you won't even know I'm there!"
            mike.say "I won't know you're there because you won't be there, Minami."
            mike.say "Don't be silly, it's just a storm, that's all."
            mike.say "Pin a sheet over the window if it helps."
            mike.say "But don't wake me up again - I need to get some sleep!"
            hide minami with dissolve
            "I close the door before Minami can say another word."
            "Sure, I feel bad doing that to her."
            "But I guess this is what they call tough love."
            "If I keep on giving in and letting her have her way, she'll never learn to fend for herself."
            "I just hope that between the storm and my nagging guilt, I can actually get some decent sleep."
        "Accept":
            $ minami.siscon += 10
            mike.say "Okay, Minami."
            mike.say "If you're sure that's the only thing that'll help you sleep?"
            show minami a normal
            "Minami beams at me as she hurries into my room, delighted to have gotten her own way."
            "She nods hastily as she waits for me to close the door behind her."
            show minami happy
            minami.say "Oh, I am, big bro."
            minami.say "I just want to be with someone that reminds me of home."
            minami.say "Someone that makes me feel safe and I know can protect me."
            "I walk back over to the bed and climb in as Minami trots around to the other side."
            "It strikes me just how weird this situation would be were she any other girl."
            "But she's my little sister, and so it's just like me sharing an umbrella with her in the rain."
            "My head back on the pillow, I watch as Minami lets the sheet drop from her shoulders."
            "For a moment, I assume that she's just wearing skimpy pyjamas."
            scene bg blank
            pause 0.2
            scene bg bedroom1
            show minami surprised naked
            pause 0.1
            show bg bedroom1 at dark with dissolve
            "But then a flash of lighting shows the outline of her body."
            "And I see for the very first time that she's totally naked."
            play sound thunder_single
            pause 0.2
            show minami c cry naked at center, vshake
            "Before I can say a word, the thunderclap that follows makes her jump."
            "Then Minami lets out a little cry and scampers under the covers."
            hide minami
            show minami naked close blush with hpunch
            "I'd been expecting her to keep her distance, but instead she literally clings to me."
            minami.say "Oh, big bro..."
            minami.say "I'm so scared!"
            minami.say "Hold me like you used to back home!"
            "And with that, she wriggles her backside into my lap, pulling my arms around her."
            "For what feels like an eternity, I'm afraid to move an inch, even to breathe."
            "I've always tried to ignore the fact that Minami has a pretty amazing body."
            "But now I can feel almost every inch of it."
            "Pressing against me with nothing between us but my shorts and t-shirt."
            show minami hunt
            minami.say "Mmm..."
            minami.say "That feels so nice, big bro."
            minami.say "Your arms are so strong - I feel totally safe here..."
            "I can hear the sleep creeping into Minami's voice as she says this."
            "And she wriggles even further into me as she settles down to see out the storm."
            "It's times like this that I wish I could just turn off my instincts as a guy."
            "Because as I lie there, awake and aware of everything that's happening, I can feel it begin to happen."
            "No matter how hard I try to fight it, my cock starts to stiffen inside of my shorts."
            "All I can do is keep still and silent, praying that Minami doesn't feel the erection she's giving me."
            "Who knows - maybe I'll fall asleep and it'll just fade away?"
            "Or maybe I'll pass out from it starving my brain of blood or simply on account of sheer shame..."
            scene bg black with dissolve
    return

label minami_siscon_03:
    $ minami.flags.sisconDelay = TemporaryFlag(True, 1)
    if bree.is_gone_forever and sasha.is_gone_forever:
        "With [bree.name] and Sasha gone the house was pretty quiet."
    elif bree.is_gone_forever:
        "I never thought that having just one more person living under the same roof as Sasha and me would be like this."
    elif sasha.is_gone_forever:
        "I never thought that having just one more person living under the same roof as [bree.name] and me would be like this."
    else:
        "I never thought that having just one more person living under the same roof as [bree.name], Sasha and me would be like this."
    "Suddenly the house feels pretty cramped, and I find myself wanting to spend as much time as I can in my room or out and about."
    "Part of me wonders if it's actually the addition of another warm body, or that Minami's my little sister which is making it so hard."
    "I understand that this must be scary for her, as it's her first time away from home as well as away from Mom and Dad too."
    "But I'm just not ready to play the role of surrogate parent to her from dawn to dusk."
    "This means that I find myself spending more time in my room than before or hurrying or lingering at the office of an evening."
    "Even the act of taking a shower has become like a little oasis of solitude in the middle of an exhaustingly social day."
    "Today I shoot into the bathroom as soon as it's free, almost leaping into the shower cubicle."
    play sound shower loop
    "I close the door behind me and turn on the water, wanting it as hot and fast as I can get it."
    "The glass panes of the cubicle steam up in a matter of seconds, and all I can hear is the cascading of the water."
    "It's a terrible cliche, I know - but I really do feel like it's washing away the troubles of the day."
    play sfx1 door_knock
    "But my relaxation is put on hold a moment later, when I hear a frantic knocking at the bathroom door."
    "Who in the hell is that?"
    play sfx1 door_knock_more
    "Can't they hear that I already have the shower running in here?"
    "That's when I know that it must be Minami, as [bree.name] and Sasha wouldn't hassle me like this."
    "Opening the shower door, I yell as loud as I can manage."
    mike.say "MINAMI, IS THAT YOU?"
    minami.say "Yeah, big bro, it's me."
    mike.say "WHAT IN THE HELL DO YOU WANT?"
    minami.say "You have to let me in - I REALLY need to pee!"
    "Surely she can't be serious?"
    mike.say "CAN'T YOU WAIT A LITTLE!"
    minami.say "I can't..."
    minami.say "Let me in - I promise I'll be quick and I won't look!"
    menu:
        "NO WAY!!":
            mike.say "NO WAY!"
            "I hear some indistinct cursing from the other side of the door."
            "But there's no more knocking and protesting after that."
            "Afterwards, I find that the shower's lost its appeal."
            "So I wash quickly and get out of there."
            stop sound fadeout 1.0
            "All the time cursing the fact that Minami's ruined one of my few moments of peace."
        "Accept":
            "I shake my head in frustration, wondering how Minami always manages to put me in positions like this."
            "What choice do I have here - I can't leave her to piss her panties on the landing!"
            mike.say "OKAY, BUT YOU'D BETTER DO JUST THAT, MINAMI!"
            "A second later, I hear the sound of the door opening and closing."
            "And Minami scuttles into the bathroom, making straight for the toilet."
            "She makes a point of looking away from the direction of the shower as she does so."
            "I watch as she pulls down her panties and sits on the toilet, still looking away."
            "But then I realise that I'm now the one watching her taking a piss."
            "Embarrassed in the extreme, I hastily close the door of the cubicle and try to get back to my shower."
            "I'd assumed that the steam fogging the panes would keep me from being seen."
            "But the cold air that Minami let in when she entered means it's already faded away to nothing."
            "This means that I'm effectively standing naked in a glass booth a few short feet from her."
            "I try not to look in her direction, but soon the temptation is too great."
            "Glancing over my shoulder, I definitely catch Minami sneaking a look at my bare ass."
            "Her eyes dart away and her head turns in the opposite direction as she's rumbled."
            "But by then, she's already seen all that there is to see."
            "And the only thing she actually missed is the sight of me flushing red in response."
            "Before I can muster the courage to say anything, Minami finishes up and flushes the toilet."
            "She's gone before I can object, and the water from the shower head turns freezing cold a moment later."
            "All I can do is leap out of the cubicle, cursing my luck."
            "But the irony of getting a cold shower isn't lost on me for a moment..."
            stop sound fadeout 1.0
            $ minami.siscon += 10
    return

label minami_siscon_02:
    $ minami.flags.sisconDelay = TemporaryFlag(True, 1)
    show bg secondfloor with fade
    "Okay, before I admit to this, let me just state for the record that it's something that happens to everyone."
    "And it's also not something that I tend to make a habit of doing on a regular basis either."
    "But all that being said, I've gone and left it almost too late to answer the call of nature."
    "So trying not to look too much like I'm running, I make my way quickly to the bathroom."
    "Thanks to the insistent urging of my bladder, I almost burst straight in there and make for the toilet."
    "All that stops me doing so is the sight of the closed door and a very real fear of walking in on someone."
    "Summoning all of my willpower, I pause with my hand hovering over the door-handle."
    mike.say "Hello?"
    mike.say "Is there anyone in there?"
    mike.say "I'm kind of in a hurry here!"
    "I don't have to wait too long for an answer, as I hear Minami speak up inside."
    minami.say "Hey, big bro."
    minami.say "You really gotta go, huh?"
    mike.say "Yeah, Minami - I REALLY gotta go!"
    "What is this, conversations over a bursting bladder?!?"
    mike.say "Well..."
    mike.say "Are you done in there, or what?"
    minami.say "Oh yeah, sorry!"
    minami.say "I'm just wrapping it up now."
    minami.say "You can come right on in, no worries!"
    "What does that even mean?"
    "Was she on her way out when I started knocking?"
    "What else can she have been doing in there that I can just stroll on in?"
    menu:
        "Go in the yard":
            "If this were [bree.name] or Sasha, it might feel okay to take them at their word."
            "Hell, it might even be a thrill to walk in there and find them unprepared..."
            "But this is different."
            "This is Minami."
            "My kid sister for goodness sake!"
            "I'm pretty sure that kind of thing is perverse, and maybe even illegal in some countries too."
            mike.say "It's okay, Minami."
            mike.say "Don't worry about it."
            mike.say "I'll just go outside."
            minami.say "Aww, don't be a prude, big bro."
            minami.say "It's not like I haven't seen it all before!"
            "I'm pretty relieved at the sudden twinge of my bladder that makes me dash off downstairs."
            "Sure, there was a time when we might have caught a sight of each other in the nude."
            "But we were only little kids back then, so I'm sure it doesn't count."
            show bg house with fade
            play sound door_slam
            "I manage to make it outside just in time, slamming the door behind me."
            "I get an immense feeling of physical relief as I finally get to drain my bladder."
            "But it does nothing to relieve the embarrassment that I feel at Minami inviting me into the bathroom with her..."
        "Accept":
            "She must be decent in there, right?"
            "Why else would Minami be fine with me coming in right now?"
            "And if I don't do something soon, I'm going to piss myself for sure."
            mike.say "Okay, Minami - I'm coming in."
            minami.say "Sure thing, big bro."
            "I twist the handle and push the door open, walking straight into the bathroom."
            "On the strength of my hunch that she's decent, I make no effort to avert my eyes as I do so."
            "And if taking Minami on her word was my first mistake, not looking down was my second."
            scene bg bathroom
            show minami naked
            with wiperight
            minami.say "What's up, big bro?"
            minami.say "I thought you were desperate to go."
            minami.say "Now you're just standing there, staring at me!"
            "Of course I'm staring at her."
            "She's totally naked for god's sake!"
            "My best guess is that Minami just stepped out of the shower before I knocked."
            "She might have been towelling herself off a moment ago."
            "But now the towel lies in a heep around her feet."
            "And what makes it worse is the fact that she's not even trying to cover herself up!"
            "Minami has her hands balled into fists and planted firmly on her thighs."
            "Firm would also be the perfect word to describe her..."
            "Oh god, no - I can't believe that I almost said that!"
            "What's wrong with me?!?"
            show minami close naked hunt
            minami.say "Oh, come on!"
            minami.say "Pick your jaw up off of the floor, big bro."
            minami.say "It's not like you never saw me naked before!"
            mike.say "Y..yeah, Minami..."
            mike.say "B...but we were kids back then!"
            minami.say "Aww, don't be such a prude, big bro."
            minami.say "It's okay for you to see me like this."
            minami.say "'Cos I know you'd never make it weird!"
            "That's easy for her to say..."
            "Minami smiles innocently at me as she bends over to pick up her towel."
            "And I swear that she makes sure I see every bit of that motion too."
            "Then she wraps it quickly around herself and trots towards the door."
            minami.say "Bathroom's all your's, big bro!"
            minami.say "Don't you go pissing your pants now..."
            "Somehow, the mention of what I actually came in here for serves to reawaken my bladder."
            "So by the time Minami's left the room, I'm struggling to keep from having an accident."
            "But in a way, it's quite a welcome distraction from all that I've just seen..."
            $ minami.siscon += 10
    return

label minami_siscon_01:
    $ minami.flags.sisconDelay = TemporaryFlag(True, 1)
    scene bg studio with fade
    "Minami's arrival pretty much throws whole house and the routines that I've grown used to into chaos."
    "And so I find myself getting desperate to do the things that are familiar to and yet don't involve her being there."
    "Band practice is pretty high up on that list, and I breathe a sigh of relief at there being no need to even mention Minami."
    "But after the usual pre-practice banter has passed between Anna, Kleio, Sasha and myself, an unexpected sound draws our attention."
    "Suddenly, the door to the practice room burst open."
    show minami happy at right with moveinright
    "And then Minami comes bustling in, filling the air with noise and chatter."
    minami.say "O...M...G!"
    minami.say "This...is...so...cool!"
    "She practically bounces her way around the practice room."
    "Threading between the instruments and gear, she comes dangerously close to causing some serious damage as she does so."
    minami.say "You said you were in a band, big bro."
    minami.say "But I always thought it was one of those with trumpets, tubas and all that shit."
    minami.say "This is like a REAL band though."
    minami.say "And you're like a real rock star too!"
    if Person.find("kleio"):
        show kleio at left5 with dissolve
    else:
        show kleio normal at left5 with dissolve
    "I feel Kleio fix me with a glance and a sneer before she even opens her mouth to speak."
    if Person.find("kleio"):
        kleio.say "Hey, Loverboy - who's little miss sugar rush here?"
    else:
        kleio.say "Hey, Loverboy - who's little miss sugar rush here?"
    show minami at center with move
    "At the sound of her voice, Minami rounds on Kleio with such speed the other girl actually recoils in surprise."
    minami.say "Oh wow - you're like some kind of serious rock chick, aren't you?"
    minami.say "I bet you don't take shit from ANYONE!"
    "Kleio looks baffled by Minami's words, slowly realising that she's being complimented."
    if Person.find("kleio"):
        kleio.say "Well...I guess...I guess I kind of am."
    else:
        kleio.say "Well...I guess...I guess I kind of am."
    minami.say "And you with the drums!"
    if Person.find("anna"):
        show anna at right, vshake
    else:
        show anna normal at right, vshake
    "Anna jumps on her drum stool and squeaks in alarm as she becomes the centre of Minami's attention."
    minami.say "You're so small - but I bet you make so much noise!"
    if Person.find("anna"):
        anna.say "Yeah...but, that's kind of the idea..."
    else:
        anna.say "Yeah...but, that's kind of the idea..."
    "I can see that I'm going to have to step in here and take Minami firmly in hand."
    "Otherwise we're not going to get fuck all done for her sticking her nose into everything."
    mike.say "Minami, I thought I told you to wait until we were done?"
    show minami sad
    "At the sound of my voice, Minami instantly turns sulky and starts to whine."
    minami.say "Aww, I know, big bro."
    minami.say "But that's SO boring."
    minami.say "And I really want to hear you play..."
    menu:
        "Send her back":
            "Normally I'd be more than flattered by Minami wanting to see me play."
            "But it feels like she's been under my feet since the moment she arrived."
            "What I really need right now is the chance to let off some serious steam."
            "On top of that, she's my little sister, and it's not fair to inflict her on the others either."
            mike.say "No, Minami - you need to get your ass out of here."
            mike.say "I'll make it up to you, okay?"
            mike.say "You can come to the very next gig that we play - how's that?"
            "Minami's face darkens, and she's now very definitely sulking."
            minami.say "Aww...but I..."
            mike.say "No, I'm not discussing it with you."
            mike.say "Get out of here!"
            minami.say "Okay, okay - I'm going already!"
            hide minami with moveoutright
            "As soon as the door closes behind her, I look at the others and shake my head."
            mike.say "Really, guys - I'm sorry you had to see that."
            mike.say "She's a good kid, but you have to be firm with her."
            if Person.find("anna"):
                show anna surprised
            else:
                show anna normal
            "Anna looks bemused at this, blinking and shaking her head."
            if Person.find("anna"):
                anna.say "What do you mean, [hero.name]?"
                anna.say "She wanted to hear you play, that's all!"
                show anna annoyed
            else:
                anna.say "What do you mean, [hero.name]?"
                anna.say "She wanted to hear you play, that's all!"
                show anna normal
            if Person.find("kleio"):
                show kleio happy
                kleio.say "Nah, Loverboy's right, Anna."
                kleio.say "You gotta put your foot down with kids like her!"
                show kleio normal
            else:
                show kleio normal
                kleio.say "Nah, Loverboy's right, Anna."
                kleio.say "You gotta put your foot down with kids like her!"
                show kleio normal
            "I could point out that Minami's not that much younger than Kleio herself."
            "But I prefer to have her on my side of the argument for once."
            mike.say "It's okay, Anna."
            if Person.find("anna"):
                show anna normal
            else:
                show anna normal
            mike.say "She's pretty much like rubber - she'll bounce back quickly."
            "We press on with the practice and the incident's soon forgotten."
            "Afterwards, I feel suitably refreshed and like it was worth the effort to kick Minami out."
            "Sure, she keeps on sulking on the ride home."
            "But her mood brightens almost as soon as something comes along to distract her again."
        "Let her stay":
            "I take a deep breath and then let it out, staring at Minami the whole time."
            "I know full well that I shouldn't hesitate to kick her out on her ass."
            "But I am kind of liking the way she's so desperate to see me in action."
            "And maybe we could use the feedback before our next gig?"
            show minami happy
            mike.say "Okay, Minami - you can stay."
            mike.say "But you sit right over there, don't move and keep quiet the whole time."
            "Minami claps her hands together in excitement."
            minami.say "YES!"
            minami.say "Thanks, big bro - you're the best!"
            "As she bounces over to the spot I indicated, I hear snickering from behind me."
            hide minami
            if Person.find("kleio"):
                show kleio at left5
                $ kleio.sub -= 5
            else:
                show kleio at left5
            if Person.find("anna"):
                show anna at right5
                with move
                $ anna.sub -= 5
            else:
                show anna at right5
                with move
            "Turning around, I see Anna trying to stifle her laughter and Kleio openly shaking her head."
            if Person.find("kleio"):
                kleio.say "Masterfully done, big bro."
                kleio.say "You really told her!"
            else:
                kleio.say "Masterfully done, big bro."
                kleio.say "You really told her!"
            if Person.find("anna"):
                anna.say "Yeah, [hero.name] - you really are the best!"
            else:
                anna.say "Yeah, [hero.name] - you really are the best!"
            show sasha annoyed at center with dissolve
            $ sasha.sub -= 5
            "Sasha just rolls her eyes and shakes her head."
            "Living under the same roof, she's already well aware of how Minami can wrap me around her finger."
            "The session starts in earnest, and Minami manages to keep her promise."
            "Well, for about five minutes, that is."
            "She spends the rest of the time we're in the practice room acting like my own personal groupie."
            "Everything that I do seems to make her pop like a lunatic, waving and cheering my praise."
            "At first, I have a massive smile plastered across my face."
            "But then I catch the looks that the others are shooting me, and my heart sinks into my shoes."
            "I fumble my way through the rest of the session, muttering apologies the whole time."
            "Afterwards, I gather up my stuff and say sorry one last time."
            scene bg black with timelaps
            scene bg street
            show minami sad
            with timelaps
            $ game.room = "street"
            $ game.hour = 23
            "On the drive home, she seems to sense that something's up."
            minami.say "Big bro..."
            minami.say "Are you mad at me?"
            mike.say "What...no, Minami."
            mike.say "I just felt like I didn't play well tonight, that's all."
            show minami surprised
            minami.say "Huh...what do you mean?"
            minami.say "I thought you did great - I was so proud of you!"
            show minami normal blush
            minami.say "Do girls faint when you get on stage?"
            minami.say "Because I think they would - you're that good, big bro!"
            mike.say "I...I don't know about that, Minami!"
            show minami happy
            "She smiles and giggles at my protests of modesty."
            "But all the same, the ego-rub sure feels good..."
            $ minami.siscon += 10
    return

label minami_preg_talk:
    show minami
    "I know that there's something up almost as soon as I set eyes on Minami, even though she's wearing a smile."
    "She's normally so upbeat and nothing seems to get her down, a regular ball of infectious energy."
    "But everything about her feels like it's forced, as though she's trying to put a brave face on."
    "I try as best I can to keep the concern that I feel for her off of my own face."
    "My instinct tells me that coming straight out and demanding to know what's wrong would only make matters worse."
    "Far better to let Minami pluck up the courage to tell me herself and in a way of her own choosing."
    mike.say "Hey, Minami."
    "For all of her efforts to look like she's perfectly fine, Minami still lets out a sigh before replying."
    minami.say "Hey, big bro."
    show minami sad
    minami.say "I...I kinda need to talk to you."
    "Still pretending to have no idea that she's got a load on her mind, I raise my eyebrows and try to look surprised."
    mike.say "Oh yeah?"
    mike.say "Well, you don't have to ask permission, Minami."
    mike.say "If you want to tell me something, then just go right ahead."
    mike.say "After all we've been through recently, I don't think there's anything we can't handle between us!"
    show minami annoyed
    "At this, Minami frowns for the first time."
    "She looks away, as if reluctant to meet my eye."
    minami.say "I hope so, big bro."
    minami.say "I really do!"
    show minami c
    "Minami clasps her hands together beneath her chin, staring at the ground."
    mike.say "Minami..."
    mike.say "Whatever you have to say, it can't be that bad - surely?"
    show minami cry
    "It's only when Minami looks back up that I see the beginnings of tears in her eyes."
    minami.say "You say that now, big bro."
    minami.say "When you don't know what it is..."
    mike.say "Then tell me, Minami."
    mike.say "Tell me what it is."
    mike.say "And then I can tell you what I think of it."
    show minami sad
    "Minami nods sadly, perhaps realising the futility of keeping silent."
    minami.say "I...I'm pregnant, big bro."
    minami.say "I'm going to have your baby!"
    "The revelation hits me like a sudden and unexpected slap to the face."
    "The girl that was once my little sister, and then my girlfriend is now carrying my child!"
    minami.say "I need to know what you want to do, big bro."
    minami.say "I mean...I'm going to keep the baby, I know that much."
    minami.say "But I don't know what you want..."
    menu:
        "Reject her":
            "I shake my head, taking a step back and away from Minami, distancing myself from her."
            "Of course, she instantly senses what this gesture means, and makes to follow me."
            mike.say "Oh no!"
            mike.say "No way, Minami!"
            show minami cry
            "Minami starts to speak, an objection, or maybe a plea forming on her lips."
            "But I've already built up too much momentum for her to be able to get even a single word in."
            mike.say "I would have stayed with you anyway."
            mike.say "There was no need for you to go and pull something like this!"
            show minami surprised at center, vshake
            "Minami looks at me in amazement, clearly stunned by this accusation."
            minami.say "What?"
            minami.say "You actually think I did this on purpose?!?"
            mike.say "Well it fits, doesn't it?"
            "All Minami can do is shake her head in denial."
            mike.say "Oh come on, Minami!"
            mike.say "After all that stuff we found out Mom and Dad did to screw with us?"
            mike.say "You must have been scared that I'd break things off between you and me."
            mike.say "Getting pregnant must have seemed like a sure way to keep it going."
            show minami cry
            "By now, Minami really is crying, tears streaming down her cheeks."
            minami.say "No, big bro - that's not true."
            minami.say "You have to believe me!"
            "Now it's my turn to shake my head and turn away from Minami."
            mike.say "I'm sorry, Minami, but I don't."
            mike.say "Keep the baby or don't, that's your choice."
            mike.say "But whether to be a part of it's life is mine."
            mike.say "And I won't let you use it to blackmail me."
            show minami surprised
            "Minami looks at me like all of a sudden she doesn't know me anymore."
            "For a moment, I think that she's going to say something else, maybe argue her case again."
            hide minami with dissolve
            "But then she turns and runs away, leaving me to watch her as she disappears from sight."
            $ minami.set_gone_forever()
            $ Room.find("bedroom5").hide()
            $ Room.find("attic").hide()
        "Take responsibility":
            show minami at center, zoomAt (1.65, (650, 1140))
            "I shake my head, taking a step towards Minami and pulling her into a tight embrace."
            "She flinches a little in surprise, but then returns the gesture, wrapping her arms around me in return."
            mike.say "Minami, that's the best news ever!"
            show minami surprised
            minami.say "R...really?"
            "Releasing her from the embrace, I can't help nodding like crazy."
            mike.say "Of course it is, Minami - don't you see what it means?"
            show minami sad
            minami.say "Erm, no."
            minami.say "I don't think I do..."
            mike.say "Think about it, Minami."
            mike.say "My Dad and the woman I thought was my Mom manipulated us both."
            mike.say "And when we found out what they did, it could have ended us, right?"
            "Minami nods slowly, not enjoying the reminder of what our so-called parents put us through."
            mike.say "But it didn't, because what we have is too strong."
            mike.say "We're together because WE want to be, not thanks to them."
            mike.say "And this baby is the perfect proof of that."
            show minami normal
            "I can see the light of understanding begin to grow in Minami's eyes."
            minami.say "I...I don't love you because of what they did, [hero.name]."
            minami.say "I love you in spite of it..."
            mike.say "That's it, Minami."
            mike.say "That's exactly how I feel too!"
            mike.say "Our child is the first thing we'll do together."
            mike.say "The first thing we do in the life that we make together."
            "Minami takes hold of my hands, gripping them tightly."
            show minami happy blush
            "She gazes up at me, practically glowing with pride and happiness."
            minami.say "You're right, [hero.name]."
            minami.say "We were only pretending to be a family before."
            minami.say "But now we can start one of our very own!"
            $ minami.flags.toldpreg = True
    return

label minami_event_03:
    show bg livingroom
    "When the big day finally arrives, I'm reduced to a bag of nerves as I wait for Minami to turn up on my doorstep."
    "I feel like I'm checking the time every two seconds, and I can't distract myself, no matter how hard I try."
    "The sound of every car pulling up in the street outside makes me think it's a cab dropping her off."
    "Seeing the appointed time for her arrival come and go really shouldn't be that much of a shock."
    "Minami's one of those people that kind of breeze through life, leaving a trail of chaos in their wake."
    "But she's never aware of the trouble that she causes, and so brushes it off as easily as she creates it."
    play sound door_bell
    "When I finally hear the sound of the door-bell ringing, I almost forget what I'm actually waiting for."
    "Part of me seemed to have come to the unconscious conclusion that I'd be trapped in that state of limbo forever."
    play sound door_bell
    "So by the time I'm up and off of my backside, hurrying to the door, the bell's rung more than half-a-dozen times already."
    show bg house with wiperight
    "Once I get there, I yank the door open, my head full of lectures for Minami on the subject of her time-keeping."
    "But, of course, all of that evaporates the moment I lay eyes on her..."
    "Minami has her back turned to me at first, looking back at the cab as it drives away."
    "She has an over-stuffed hiking rucksack on her back, and various other bits of luggage scattered around her feet."
    "Which means that I can't get that good of a look at her or she at me until she turns around."
    show minami a casual with dissolve
    "When she does, I feel myself almost gasp out loud."
    "And there's the sudden sensation of butterflies in my stomach."
    show minami a happy
    minami.say "HEY, BIG BRO!!!"
    minami.say "Here I am!"
    show minami close with vpunch
    "Dropping her rucksack from her back, Minami practically leaps at me."
    "I feel her arms wrap around my neck as she pulls me into a tight embrace."
    "As she's easily a head or more shorter than me, I have to wrap my hands around her waist, supporting her weight."
    "She almost knocks the air out of me as she does this, hanging off me like her life depends on it."
    "I was in my mid-teens when I first realised that my little sister was pretty."
    "I'd been aware of girls for some time by then."
    "But Minami had always been more like another boy when we were growing up together."
    "From that point on, she just seemed to get more feminine and beautiful with each year that passed."
    "Understand that I wasn't looking at her in THAT way."
    "She's my sister, and it more weirded me out and made me worry about how other guys might see her."
    "But in the time that I've been away from home, that same process seems to have gone into overdrive!"
    "Before Minami looked to me like a young girl just starting to blossom."
    "Now she looks like she could walk into a room and have every eye on her within seconds."
    "And what makes it worse, is that I can tell she now has a woman's body to go with the pretty face."
    "She's literally hugging me so tightly that I don't need to see it for myself to be sure!"
    mike.say "Yeah, Minami."
    mike.say "Here you are..."
    hide minami
    show minami casual normal
    "Minami unwraps herself from me, hopping back down to the ground as she does so."
    minami.say "So - what are you waiting for?!?"
    minami.say "Aren't you going to invite me in?"
    minami.say "I'm SO looking forward to you giving me the grand tour!"
    "She looks down at her bags, and then back up at me."
    "Those huge, spell-binding eyes fix upon my own."
    show bg livingroom with fade
    "And before I know it, I'm hastily gathering up all of Minami's luggage as she skips into the house before me."
    "Yeah, I know how it looks - and you can call me a sucker if you like."
    "But until she's fixed you with that gaze, you have no right to judge me!"
    minami.say "Ooh, this must be the hall."
    minami.say "And this is the kitchen!"
    hide minami with moveoutright
    "Her voice becomes more distant as she wanders off without me, sticking her nose in wherever the whim takes her."
    "I manage to stagger as far as the sitting room, when my strength gives out and I drop her bags in a heap."
    if sasha.hidden:
        "This earns me an inquisitive stare from [bree.name], who is lounging on the sofa, ignoring the TV."
        if not "bree_talk_minami" in DONE:
            show bree casual zorder 2 at left5 with dissolve
            bree.say "Oh wow, [hero.name] - are you going away for the weekend or something?"
            mike.say "That's just Minami's things."
            bree.say "Huh...who's Minami?"
            "I open my mouth to speak, realising that I've forgotten to explain all of this to one of my housemates."
            show bree at left
            show minami casual at right
            with moveinright
            "But at that very moment, Minami comes skipping into the room, all smiles and innocence."
            minami.say "Oh, hi there!"
            minami.say "I'm Minami."
            minami.say "You must be [bree.name]."
            minami.say "[hero.name]'s told me so much about you - I feel like I know you already!"
            show bree casual cry
            $ bree.love -= 30
            "[bree.name] looks like she's been slapped in the face with a fish."
            show bree casual angry
            bree.say "He has?!?"
            mike.say "Minami's my little sister, remember?"
            show bree surprised
            "[bree.name] stares blankly at me for a moment."
            "But then she seems to catch on, and gives a weak nod of her own."
            show bree normal
            bree.say "Minami...yeah...sure."
            bree.say "How could I have forgotten!"
            "Minami sighs and let's out a gasp in relief."
            minami.say "Thank heaven for that!"
            minami.say "For a second there, I was scared that [hero.name] had been a moron and not told you I was moving in!"
            "At the mention of her moving in, I can almost hear the sound of [bree.name] drawing in breath to let out a cry of alarm."
            "But I manage to cut her off before she can make her true feelings known."
            mike.say "Hey, Minami - what do you say I show you where you'll be sleeping?"
            "I steer my little sister out of the room before anything else can go wrong."
            "But on the way out, I look back over my shoulder for a second."
            hide minami
            show bree casual surprised at left4
            with moveoutright
            "[bree.name]'s eyes are wide and confused, as though she still doesn't really know what just happened."
        else:
            show bree casual zorder 2 at left5
            with dissolve
            bree.say "I see pink bags in that pile, [hero.name]!"
            sasha.say "Yeah, and even you're not THAT girly!"
            mike.say "Ha, ha...very funny."
            show bree at left
            show minami casual at right
            with moveinright
            "At that moment, Minami comes skipping into the room, all smiles and innocence."
            minami.say "Oh, hi there!"
            minami.say "I'm Minami."
            minami.say "You must be [bree.name]."
            minami.say "[hero.name]'s told me so much about you - I feel like I know you already!"
            show bree casual happy
            "Instantly, [bree.name] and Sasha are all welcoming smiles."
            "And I can already feel bonds of feminine friendship between the three of them starting to grow."
            show bree normal
            bree.say "That's SO weird, Minami."
            bree.say "Because we feel the same way too!"
            show minami casual at right, vshake
            show fx exclamation
            minami.say "NO WAY!"
            minami.say "Oh, wow - this is going to be so much fun, I just know it already!"
            mike.say "Hey, Minami - what do you say I show you where you'll be sleeping?"
            "I steer my little sister out of the room before anything else can be said."
            "But on the way out, I look back over my shoulder for a second."
            hide minami
            show bree casual at left4
            with moveoutright
            "Now [bree.name] is grinning at me, making me dread what she have planned for Minami in the near future."
    else:
        "This earns me an inquisitive stare from [bree.name] and Sasha, who are lounging on the sofa, ignoring the TV."
        if not "bree_talk_minami" in DONE and not "sasha_talk_minami" in DONE:
            show bree casual zorder 2 at left5
            show sasha casual zorder 1 at right5
            with dissolve
            bree.say "Wow, [hero.name] - who's is all that stuff?"
            sasha.say "Yeah, [hero.name] - are you going on holiday for a year or something?"
            "I open my mouth to speak, realising that I've left it rather late to explain all of this to my housemates."
            show sasha at left4
            show bree at left
            show minami casual at right
            with moveinright
            "But at that very moment, Minami comes skipping into the room, all smiles and innocence."
            minami.say "Oh, hi there!"
            minami.say "I'm Minami."
            minami.say "You must be [bree.name] and Sasha."
            minami.say "[hero.name]'s told me so much about you both - I feel like I know you already!"
            show sasha casual wtf
            "At this, Sasha fixes me with a cold glare."
            show bree casual lose
            "[bree.name], on the other hand, looks almost dumstruck."
            show sasha casual annoyed
            sasha.say "Oh, has he?"
            sasha.say "That's not fair - because he's not told us a thing about you!"
            show minami sad
            "Minami frowns, and then turns to me, cocking her head on one side."
            minami.say "Is that true, [hero.name]?"
            minami.say "Did you not tell them that I'd be moving in?"
            $ sasha.love -= 50
            $ bree.love -= 30
            "At the mention of her moving in, I can almost hear the sound of Sasha drawing breath to object."
            "But she's cut off by [bree.name], who jumps in before the other girl can make her true feelings known."
            show bree casual happy
            bree.say "Don't listen to her...Minami, was it?"
            bree.say "She's just joking around."
            bree.say "Of course [hero.name] told us all about you."
            bree.say "What kind of a useless moron would forget to do that?!?"
            "Thankful for the lifeline that [bree.name] just tossed me, I'm more than happy to take the implied insult on the chin."
            mike.say "Hey, Minami - what do you say I show you where you'll be sleeping?"
            "I steer my little sister out of the room before anything else can go wrong."
            "But on the way out, I look back over my shoulder for a second."
            hide minami
            show sasha casual angry at right5
            show bree casual angry at left5
            with moveoutright
            "Sasha's eyes are wide, giving me a look that could kill at one hundred paces."
            "And while it's not nearly as hostile, [bree.name]'s own look tells me that I owe her for saving my ass back there."
        elif not "sasha_talk_minami" in DONE:
            show sasha casual zorder 1 at right5 with dissolve
            sasha.say "Shit, [hero.name] - you going on holiday for a year or something?"
            show bree casual zorder 2 at left5 with dissolve
            bree.say "Nah, that'll just be Minami's stuff."
            bree.say "She's moving in today - remember?"
            show sasha annoyed
            "I open my mouth to speak, realising that I've forgotten to explain all of this to one of my housemates."
            "But at that very moment, Minami comes skipping into the room, all smiles and innocence."
            show sasha at left4
            show bree at left
            show minami casual at right
            with moveinright
            minami.say "Oh, hi there!"
            minami.say "I'm Minami."
            minami.say "You must be [bree.name] and Sasha."
            minami.say "[hero.name]'s told me so much about you both - I feel like I know you already!"
            show bree happy
            "[bree.name] has a pained smile on her face as Minami says all of this."
            show sasha casual wtf
            "But Sasha plainly looks livid, like she could kill me with her bare hands."
            sasha.say "Oh, has he?"
            sasha.say "That's not fair - because he's not told me a thing about you!"
            show sasha annoyed
            show bree normal
            show minami sad
            "Minami frowns, and then turns to me, cocking her head on one side."
            minami.say "Is that true, [hero.name]?"
            minami.say "Did you not tell Sasha that I'd be moving in?"
            $ sasha.love -= 50
            "At the mention of her moving in, I can almost hear the sound of Sasha drawing breath to object."
            show bree happy
            "But she's cut off by [bree.name], who jumps in before the other girl can make her true feelings known."
            bree.say "Don't listen to her, Minami."
            bree.say "She's just joking around."
            bree.say "Of course [hero.name] told us all about you."
            bree.say "What kind of a useless moron would forget to do that?!?"
            "Thankful for the lifeline that [bree.name] just tossed me, I'm more than happy to take the implied insult on the chin."
            mike.say "Hey, Minami - what do you say I show you where you'll be sleeping?"
            "I steer my little sister out of the room before anything else can go wrong."
            "But on the way out, I look back over my shoulder for a second."
            hide minami
            show sasha casual angry at right4
            show bree casual normal at left4
            with moveoutright
            "Sasha's eyes are wide, giving me a look that could kill at one hundred paces."
            "And while it's not hostile, [bree.name]'s own look tells me that I owe her for saving my ass back there."
        elif not "bree_talk_minami" in DONE:
            show bree casual zorder 2 at left5 with dissolve
            bree.say "Oh wow, [hero.name] - are you going away for the weekend or something?"
            show sasha casual zorder 1 at right5 with dissolve
            sasha.say "Is he hell, [bree.name]."
            sasha.say "That's just Minami's crap."
            bree.say "Huh...who's Minami?"
            "I open my mouth to speak, realising that I've forgotten to explain all of this to one of my housemates."
            show sasha at left4
            show bree at left
            show minami casual at right
            with moveinright
            "But at that very moment, Minami comes skipping into the room, all smiles and innocence."
            minami.say "Oh, hi there!"
            minami.say "I'm Minami."
            minami.say "You must be [bree.name] and Sasha."
            minami.say "[hero.name]'s told me so much about you both - I feel like I know you already!"
            show bree casual cry
            $ bree.love -= 30
            "[bree.name] looks like she's been slapped in the face with a fish."
            show sasha casual wtf
            "But Sasha plainly looks livid, suddenly realising I forgot to tell the other girl about all of this."
            show bree casual angry
            bree.say "He has?!?"
            show sasha annoyed
            sasha.say "Of course he has, [bree.name]."
            sasha.say "Minami's his little sister, remember?"
            show bree surprised
            "[bree.name] stares blankly at Sasha for a moment as the other girl nods suggestively."
            "But then she seems to catch on, and gives a weak nod of her own."
            show sasha normal
            show bree normal
            bree.say "Minami...yeah...sure."
            bree.say "How could I have forgotten!"
            "Minami sighs and let's out a gasp in relief."
            minami.say "Thank heaven for that!"
            minami.say "For a second there, I was scared that [hero.name] had been a moron and not told you I was moving in!"
            "At the mention of her moving in, I can almost hear the sound of [bree.name] drawing in breath to let out a cry of alarm."
            "But I manage to cut her off before she can make her true feelings known."
            mike.say "Hey, Minami - what do you say I show you where you'll be sleeping?"
            "I steer my little sister out of the room before anything else can go wrong."
            "But on the way out, I look back over my shoulder for a second."
            hide minami
            show sasha casual annoyed at right4
            show bree casual surprised at left4
            with moveoutright
            "[bree.name]'s eyes are wide and confused, as though she still doesn't really know what just happened."
            "But Sasha's own look tells me that I owe her for saving my ass back there."
        else:
            show bree casual zorder 2 at left5
            show sasha casual zorder 1 at right5
            with dissolve
            bree.say "I see pink bags in that pile, [hero.name]!"
            sasha.say "Yeah, and even you're not THAT girly!"
            mike.say "Ha, ha...very funny."
            sasha.say "Nice to know that you agree with us, [hero.name]!"
            show sasha at left4
            show bree at left
            show minami casual at right
            with moveinright
            "At that moment, Minami comes skipping into the room, all smiles and innocence."
            minami.say "Oh, hi there!"
            minami.say "I'm Minami."
            minami.say "You must be [bree.name] and Sasha."
            minami.say "[hero.name]'s told me so much about you both - I feel like I know you already!"
            show bree casual happy
            show sasha casual happy
            "Instantly, [bree.name] and Sasha are all welcoming smiles."
            "And I can already feel bonds of feminine friendship between the three of them starting to grow."
            show bree normal
            bree.say "That's SO weird, Minami."
            bree.say "Because we feel the same way too!"
            show minami casual at right, vshake
            show fx exclamation
            minami.say "NO WAY!"
            sasha.say "Yes way, Minami."
            sasha.say "And we want to know ALL about you."
            sasha.say "That, and about [hero.name] too..."
            hide fx
            show sasha joke
            "Sasha catches my eye as she says this, her smile radiating pure evil."
            minami.say "Oh, wow - this is going to be so much fun, I just know it already!"
            mike.say "Hey, Minami - what do you say I show you where you'll be sleeping?"
            "I steer my little sister out of the room before anything else can be said."
            "But on the way out, I look back over my shoulder for a second."
            hide minami
            show sasha casual at right4
            show bree casual at left4
            with moveoutright
            "Now both [bree.name] and Sasha are grinning at me, making me dread what they have planned for Minami in the near future."
    scene bg secondfloor with fade
    "With my little sister following close on my heels, I begin to climb the stairs in earnest."
    "I guess there's no putting it off any longer."
    "I need to tell her what the sleeping arrangements are going to be."
    scene bg attic
    if not "cleaning_attic" in DONE:
        show minami casual
        with fade
        mike.say "The long-term plan is for you to have the attic room, Minami."
        minami.say "Oh, big bro - that sounds great!"
        mike.say "Ah, yeah..."
        mike.say "The only problem is that I haven't actually cleaned it out yet."
        $ minami.love -= 20
        show minami sad
        "I can see the familiar look of disappointment growing on Minami's face."
        "The one that she used back when we were kids."
        "The one that always involved tears, pouting and ultimately getting her own way."
        mike.say "But I will, okay?"
        mike.say "I will get it sorted as soon as I can."
        "Minami nods at this, but still sniffles a little as she asks the inevitable question."
        minami.say "But...where am I gonna sleep until then, big bro?"
        mike.say "I thought you could sleep in my room."
        "For a moment, the look on Minami's face is hard to read."
        "It looks like a mixture of surprise and disbelief."
        "But also as though she can't believe her luck and is trying to hide it from me at the same time."
        minami.say "Oh...I see."
        minami.say "Well...I guess it would be warmer for the two of us!"
        "Wait, what?!?"
        "She can't possibly be suggesting that I mean..."
        mike.say "No, Minami!"
        mike.say "I mean I'd be sleeping on the sofa."
        mike.say "Just until your room is ready."
        show minami blush
        "Minami seems embarrassed for just a couple of seconds."
        "Like she's admitted to something that she shouldn't have."
        show minami normal
        "But then as quickly as the look came, it disappears again."
        "And as though nothing's happened, she's all smiles and giggles again."
        minami.say "Of course that's what you mean, big bro."
        minami.say "Geez - I was only joking around!"
        minami.say "Sure...I'll take your bed until you sort out my room."
        "I nod, the relief at having that settled washing away any other concern on my mind."
        "I just hope that I can get the attic cleaned out before Minami goes rooting through my room!"
    else:
        show minami casual
        with fade
        mike.say "I took the liberty of cleaning out the attic room for you, Minami."
        mike.say "It's pretty sparse right now."
        mike.say "But I'm sure you can do something with it..."
        "I trail off as I look back over my shoulder to see Minami's reaction."
        "I'd been expecting her to moan at it not being decorated."
        "Or maybe bemoan that number of steps that she'd have to climb to get to it."
        "But instead, her eyes are wider than ever, making her look like a cartoon character."
        show minami happy
        minami.say "Big bro, you remembered!"
        mike.say "I what?"
        "Before I can get an answer out of her, Minami darts past me and into the attic."
        "I follow her, and walk in just in time to see her turning circles in the middle of the floor."
        "As soon as she sees me, Minami dashes over and pulls me into another fierce hug."
        show minami close
        minami.say "You remembered how I always wanted the attic room, back when we were kids!"
        minami.say "I begged mom and dad to let me have it for my room."
        minami.say "I even held my breath until I passed out and hit my head on the coffee table."
        minami.say "They just said that I was being stupid and spoiled."
        minami.say "But you remembered, big bro!"
        minami.say "Because you're the best big brother ever!"
        mike.say "Ah...yeah, Minami."
        mike.say "I remembered all of that."
        mike.say "No way did I just stick you in the only spare room we had..."
        minami.say "I love you, big bro!"
        "Minami finally releases me from her embrace and starts to flit around the room."
        minami.say "I can have my bed here, and my wardrobe over here."
        minami.say "And I'll need a mirror here - so that I can try on my clothes."
        show minami hunt
        "At the mention of clothes, Minami's eyes seem to light up anew."
        minami.say "I brought SO many new cute outfits, big bro."
        minami.say "Would you like to see me in them, huh?"
        mike.say "No, Minami..."
        mike.say "I'm sure I'll see enough of you in them around the house!"
        "Minami looks a little deflated at this."
        "But she's soon distracted by something else."
        "I smile and go along with the course of her short attention span."
        "All in all, I think I came out of this one pretty well."
    scene bg black with dissolve
    $ minami.unhide()
    $ Room.find("bedroom5").unhide()
    $ Room.find("attic").hide()
    $ hero.smartphone_contacts.append("minami")
    $ minami.flags.sisconDelay = TemporaryFlag(True, 1)
    return

label bree_talk_minami_01:
    "It's all well and good me promising Minami that she's okay to move in here with me."
    "But that's only a yes from one third of the people that call this place home."
    "If this is going to fly, I need to get [bree.name] and Sasha on board with the idea too."
    "So rather than put it off, I jump on the first chance that I get to talk it through with [bree.name]."
    show bree
    mike.say "Um...[bree.name]?"
    show bree happy
    bree.say "Oh, hey, [hero.name] - what's up?"
    "[bree.name] smiles at me as she says this, all blonde hair and bewitching smiles."
    "I swallow hard, dreading the subject that I have to bring up with her."
    "But I press on, as there's really no way of avoiding it."
    mike.say "Well..."
    mike.say "You remember me talking about Minami?"
    show bree normal
    "She frowns a little, wrinkling her nose in that cute way she has."
    bree.say "Yeah, I do."
    bree.say "She's your...sister, right?"
    "I nod at this, encouraged that she remembers me mentioning Minami."
    "Maybe the fact that I'm not dropping this on her out of the blue will count in my favour?"
    mike.say "Yeah, that's right."
    mike.say "And you remember that she's going to college here too?"
    "Now it's [bree.name]'s turn to nod."
    bree.say "Oh, yeah."
    bree.say "You said she might hang around here too, didn't you?"
    bree.say "That's cool with me, [hero.name]."
    "[bree.name] chuckles, shooting me an amused look."
    bree.say "Actually, I'm looking forward to it."
    bree.say "I figure she'll have all kinds of great stories about you as a kid!"
    "Without even noticing that I'm doing it, I begin to rub the back of my head."
    "The nerves are threatening to get the better of me, so I press on regardless."
    mike.say "Ah, that's just the thing, [bree.name]."
    mike.say "I just found out that Minami might be hanging around a bit longer than I thought."
    mike.say "In fact, she might have to stay here a while."
    show bree surprised
    bree.say "Oh...okay."
    bree.say "Does she need to stay while she gets her own place sorted?"
    show bree normal
    bree.say "Because I'm sure we can put up with her for a while."
    mike.say "No, [bree.name]."
    mike.say "More like she hasn't got her own place worked out."
    mike.say "Because she thinks she's going to be moving in here..."
    show bree surprised
    "[bree.name]'s eyes go suddenly wide as the implications of my words sink in."
    "I can't help wincing a little, thinking that she'll explode any second."
    bree.say "That's...that's..."
    "I close one eye in anticipation of being blistered."
    show bree happy at center, zoomAt (1.65, (650, 1140)), vshake
    show fx exclamation
    bree.say "THAT'S AMAZING!"
    mike.say "What, wait...it is?!?"
    hide fx
    show fx exclamation
    bree.say "It's like the best news EVER!"
    "All I can do is stare at her, my mouth hanging open in complete shock."
    hide fx
    bree.say "Oh, [hero.name] - this is gonna be so cool!"
    bree.say "I never had a kid sister growing up, so she can be like my step-sister too!"
    hide bree
    show bree happy at center, zoomAt (1.65, (650, 1140)), vshake
    "[bree.name] starts practically hopping on the spot, waving her hands in excitement."
    bree.say "We can play videogames together, paint each other's nails, have sleepover parties!"
    bree.say "I can't wait for her to get here!"
    "All I can do is offer a weak smile, nodding with what I hope looks like enthusiasm."
    "Somehow, [bree.name]'s managed to reassure me that she's more than happy for Minami to move in."
    "But at the same time, she's also scared the hell out of me when I think about what'll happen when she does..."
    hide bree
    return

label sasha_talk_minami_01:
    "My saying yes to Minami over the phone was the easy part of her moving in with me."
    "The real hard work begins almost as soon as we end the call and I'm left on my own to make it happen."
    "[bree.name] might be the easier of the two to convince, just based on my experience of my past dealings with her."
    "But when it comes to Sasha, I have absolutely no idea as to just how she'll react."
    "She might be open to being talked around, or else she might choose to kill me on the spot!"
    "I could brood on this for days, but Minami's arrival is getting ever closer."
    "So the only thing to do is bite the bullet and take the goth by the piercings..."
    show sasha
    mike.say "Sasha..."
    "At the sound of her name, Sasha looks up from whatever she's doing."
    sasha.say "Hmm..."
    sasha.say "Oh, hi, [hero.name]."
    sasha.say "What's up?"
    "I try to look casual, like I'm just starting the conversation on a whim."
    "But all the same, I'm pretty sure that my smile looks like a forced rictus grin."
    mike.say "Nothing really..."
    mike.say "Nothing at all!"
    show sasha annoyed
    "Sasha shrugs and shakes her head."
    sasha.say "Okay, I guess I'll just wait until something is."
    "With that, she turns her attention away from me once more."
    mike.say "No, Sasha..."
    sasha.say "Ah, so there really is something up, yeah?"
    mike.say "Erm...yeah, there is."
    show sasha normal
    "Sasha gives me her full attention again, a satisfied smile spreading across her face."
    sasha.say "I thought as much!"
    sasha.say "Come on then - spill your guts."
    "I let out a weary sigh, admitting defeat in front of Sasha as I do so."
    mike.say "Okay, so - you remember me telling you about Minami?"
    sasha.say "That's your sister, right?"
    mike.say "Yeah, the one that's coming to college here."
    "Sasha nods, looking at me as though she's not quite sure what my point is here."
    sasha.say "I know that too, [hero.name]."
    sasha.say "I thought I already told you I was okay with that?"
    sasha.say "She can hang out here all she likes."
    sasha.say "So long as she keeps out from under my feet."
    "At this, I guess my grin becomes even wider and more forced."
    show sasha angry
    "As Sasha's face instantly darkens as soon as she notices."
    "She fixes me with a stare that could flay flesh off of the bone."
    sasha.say "[hero.name], what's the matter?"
    sasha.say "Whatever it is, you'd better tell me - right now!"
    mike.say "My sister called me and she thinks she's moving in with us!"
    show sasha annoyed
    "The words come tumbling out of my mouth before I can stop them."
    "But Sasha seems to sense the state of disarray that I'm in too."
    "She groans and rolls her eyes in annoyance."
    "Yet she makes no attempt to lay into me at the revelation I just delivered."
    sasha.say "And let me guess - you just rolled over and told her it was happening?"
    "All I can do is nod in response, feeling utterly pathetic as I do so."
    sasha.say "I think I'm beginning to see how your relationship with this Minami works, [hero.name]."
    show sasha normal
    sasha.say "Okay, she can move in with us as far as I'm concerned."
    sasha.say "But you keep her out of my way, and understand that I'm not playing big sister."
    mike.say "Thanks, Sasha."
    mike.say "This means a lot to me, and you won't even know she's here - I promise."
    show sasha annoyed
    sasha.say "I seriously doubt that, [hero.name]."
    show sasha normal
    sasha.say "But I guess having her here does kind of make sense."
    mike.say "Really?!?"
    sasha.say "Sure it does."
    sasha.say "She's a young girl, moving to a big city that's totally new to her."
    sasha.say "We should all keep an eye on her - you most of all!"
    "I nod furiously as Sasha turns her attention away from me and back to what she was doing previously."
    "And I take the fact she's now studiously ignoring me as confirmation that I've been dismissed from her presence."
    "I walk away thankful that I have Sasha's blessing, and for only the cost of her blistering me over it."
    "All things considered, that could have gone far worse than it did."
    return

label minami_event_02:
    "You know those times when you get a strange feeling that you can't quite explain?"
    "It's like thinking you're being watched, just something you can't put your finger on."
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Minami")
    if not result:
        $ hero.cancel_event()
        $ minami.love -= 5
        return
    "But then my phone rings, and I see that it's Minami on the line."
    "Instantly I forget all about the weird feeling and pick up the call."
    mike.say "Ah, hey, Minami."
    mike.say "You caught me on the hop."
    mike.say "I wasn't expecting a call from you!"
    "I hear an irrepressible giggle on the other end of the line."
    "And I'm instantly reminded of my little sister."
    "In fact, I can even picture the expression that must be on her face right now."
    "Then it hits me how vivid that picture is, and I realise that I must be really missing her."
    minami.say "Aww, big bro - what are you even like!"
    minami.say "I thought that I'd be the only thing on your mind right about now."
    "This comment strikes me as a little odd, making me frown in confusion."
    "But then I shake it off, remembering that Minami can be a little self-obsessed at times."
    "So I guess it's perfectly natural for her to assume that I'm always thinking of her."
    mike.say "Of course, Minami - how could I forget about you!"
    "Minami lets out another peal of giggles."
    minami.say "Oh, big bro, you're so funny!"
    minami.say "I just knew you were joking."
    mike.say "Of course I was joking, Minami."
    mike.say "But I guess you just know me too well to fall for it!"
    "Sure, I feel a little guilty at letting Minami think she's right."
    "But in my experience, indulging her a little here and there reaps bigger rewards later on."
    minami.say "So, I suppose you already know why I'm calling, right?"
    mike.say "Yeah, of course I do!"
    "My mind's racing as I say this, trying to cash the cheque my mouth just wrote."
    mike.say "You'll be coming to college soon, right?"
    mike.say "So it's got to be something to do with that."
    minami.say "Well done, big bro - you're getting warmer!"
    mike.say "Ah..."
    mike.say "You got your accommodation sorted, yeah?"
    mike.say "And you want me to check it out for you, maybe?"
    mike.say "Have your big brother make sure it's good enough for you?"
    "Minami giggles yet again, and I can almost see her shaking her head at my cluelessness."
    minami.say "Come on, big bro - stop messing with me."
    minami.say "You already checked out where I'll be staying."
    mike.say "Erm...I did?"
    minami.say "Well, I'm gonna be living with you...aren't I?"
    "I recognise the way that Minami's tone changes, the bounce draining out of her voice."
    "Suddenly my mental image of her shrinks, and she looks instantly small and vulnerable."
    "All I can think of is her lip starting to tremble as the rug is pulled from under her."
    "Okay, okay - I know how bad all of this sounds."
    "And yes, Minami's more than a little spoiled, maybe even entitled."
    "But she's my little sister, who my parents loved enough to adopt and made me promise to look after."
    "And the very moment that I see her in the least bit scared, afraid or unsure, I want to protect her."
    menu:
        "No":
            "And yet, this isn't just about me and the need I have to play the masterful big brother."
            "I have to think of [bree.name] and Sasha too, how Minami moving in here would affect them."
            "Plus the fact that if Minami's going out into the big, bad world, she can't be coddled the whole time."
            "It's long overdue that she learns to look after herself and not manipulate people to get her own way!"
            mike.say "Ah, no, Minami."
            mike.say "I think I'd have remembered agreeing to that!"
            mike.say "Mom and Dad might have mentioned it as a possibility, sure."
            mike.say "But we never decided that was going to happen."
            "There's an awkward silence on the other end of the line."
            "And I feel like holding my breath in anticipation of what's to come."
            minami.say "WHAAAA...ha...ha...ha!"
            minami.say "What do you even mean, big bro?!?"
            minami.say "I have to leave home in like THREE DAYS."
            minami.say "I'm gonna be homeless!"
            minami.say "I'm gonna have to live in a cardboard box!"
            "I can hear the panic in her voice, making me want to do a U-turn on my decision."
            "But I know this is how Minami operates, and so I try to keep a level head as she's losing hers."
            mike.say "Calm down, Minami."
            mike.say "You're not going to be homeless, for god's sake."
            mike.say "I can call the college and get you a room in the halls of residence."
            minami.say "But I'll be living with strangers, big bro!"
            minami.say "I won't know anyone at all!"
            mike.say "Don't worry, Minami - everyone'll be in the same situation as you."
            mike.say "I'll make the call and then get back to you, okay?"
            "I feel bad ending the call before she can protest again."
            "But she was already in serious danger of talking me round to her way of thinking."
            "I just hope that I can come through on the promise I made her."
            "And that the other students can put up with her too!"
            $ minami.flags.nomovein = True
            $ minami.set_gone_forever()
        "Yes":
            "So that's what I do, and it's what I'll always do - so just deal with it!"
            mike.say "Yeah, Minami, you are."
            mike.say "Of course you're staying with me."
            mike.say "I can't believe that I forgot that, even for a second!"
            mike.say "I guess I've just been so busy that it slipped my mind, that's all."
            minami.say "O...okay, big bro."
            minami.say "Is it still okay?"
            minami.say "I don't want to be a burden..."
            mike.say "Don't be silly, Minami."
            mike.say "You could never be a burden to me."
            mike.say "And don't worry - everything's sorted for when you get here."
            "On the other end of the line, I hear Minami make a sound of pure and unadulterated joy."
            minami.say "Oh, big bro, you really ARE the best!"
            minami.say "I'll be there in three days!"
            minami.say "I've missed you SO much while you've been away."
            minami.say "I just know I'm going to love living with you!"
            mike.say "Me too, Minami."
            mike.say "You just worry about getting here, and leave the rest to me."
            "I manage to hold it together as we wrap up the call."
            "But the moment that it's over, the enormity of all that I've promised Minami finally hits home."
            "Now all I have to do is talk my housemates into letting her live with us."
            "That and behave like it was the idea all along!"
            "If I manage to pull all of that off, I just hope Minami's grateful."
            "But let's just say that I'm not pinning my sanity on it..."
            $ minami.flags.moveindelay = TemporaryFlag(True, 4)
    return

label spank_minami:
    sasha.say "Oh...my...GOD!"
    sasha.say "You have to be fucking kidding me!"
    minami.say "It was an accident, okay!"
    minami.say "And why'd you leave it there in the first place?!?"
    "At the sound of raised voices, I all but run into the living room."
    scene bg livingroom
    show minami casual angry at left
    show sasha casual angry at right
    with fade
    "And as soon as I get there, I find myself in the middle of an argument."
    "Sasha and Minami are squaring off in the middle of the room."
    "They're glaring at each other, anger burning in their eyes."
    "And on the floor between them I see the source of the conflict."
    "Sasha's bass, sitting in a pool of spilt liquid."
    "I raise my hands as I approach the girls."
    "And I try to play the part of peacemaker."
    mike.say "Ah...hey, guys?"
    mike.say "Do you realise they can hear you yelling in space?"
    "I was kind of hoping that might have diffused the situation."
    "But instead, Sasha and Minami turn to face me."
    "And each one seems keen to paint the other as the bad guy."
    show sasha vangry
    sasha.say "Do you know what your dumb little sister did, [hero.name]?!?"
    sasha.say "She only went and spilled her juice over my goddamn bass!"
    show sasha angry
    "I open my mouth to speak."
    "But Minami jumps in before I can say a word."
    minami.say "Big bro, I tripped over it!"
    minami.say "She left it in the middle of the floor."
    minami.say "I could have been seriously injured!"
    "Oh great, this is just what I needed!"
    "I wanted to calm things down in here."
    "But now it looks like I'm trapped right in the middle."
    "Sure, Sasha shouldn't leave things lying around the house."
    "Especially something like a valuable musical instrument."
    "But then Minami shouldn't be so clumsy either."
    "She's always bumping into things and causing chaos!"
    "Both of them have got a point."
    "So who do I side with?"
    menu:
        "Support Minami":
            "Well, cause and effect says that this is Sasha's fault."
            "She was the one that left her stuff lying around the place."
            mike.say "Geez, Sasha..."
            mike.say "You need to learn to pick up after yourself."
            show sasha surprised
            show minami normal
            "Sasha's expression suddenly changes to one of disbelief."
            "And at the same time, Minami begins to look pretty smug."
            sasha.say "What?!?"
            sasha.say "This was a one-off, [hero.name]!"
            show sasha annoyed
            sasha.say "Look around the place - do you see tons of my shit left lying around?!?"
            "I shrug Sasha's explanation off even as she makes it."
            "Sure, she might have a point."
            "But if you ask me, it's still an excuse."
            mike.say "Whatever, Sasha."
            mike.say "If it hadn't been there, Minami wouldn't have tripped over it."
            mike.say "End of story."
            show sasha angry
            sasha.say "Argh!"
            sasha.say "I should have known that you'd back up your little sister!"
            $ sasha.love -= 5
            hide sasha
            show minami at center
            with moveoutright
            "And with that, Sasha snatches up her soaked bass and storms out."
            show minami tehe
            minami.say "Thanks for coming to my rescue, big bro!"
            mike.say "No worries, Minami."
            show minami normal
            minami.say "Sasha seemed pretty mad..."
            show minami sad
            minami.say "You think she's going to be okay?"
            mike.say "She's a big girl, she can look after herself."
        "Support Sasha":
            "Sure, the accident wouldn't have happened if Sasha picked up after herself."
            "But the bass is pretty big, you know - kind of hard to miss."
            "And it's time Minami started to take responsibility for herself."
            "She can't always be expecting me to come to her rescue."
            mike.say "Geez, Minami..."
            mike.say "We're not back home anymore."
            mike.say "You can't expect everyone to keep the place clean like Mom did!"
            show sasha normal
            show minami surprised
            "Minami's jaw drops open as she realises that I'm not going to back her up."
            "At the same time, Sasha begins to look decidedly smug."
            minami.say "Big bro!"
            minami.say "How can you be on HER side and not mine?!?"
            show minami sad
            minami.say "I didn't mean to do it - and I got hurt too!"
            "I shake my head, dismissing Minami's pleas of innocence."
            "She might have a point."
            "But it's still an excuse."
            mike.say "Knock it off, Minami."
            mike.say "We're all adults here."
            mike.say "And you need to take responsibility for once."
            minami.say "Oooh..."
            minami.say "You...you..."
            show minami cry
            minami.say "You big meanie!"
            minami.say "Mom and Dad wouldn't have treated me like this!"
            menu:
                "Shrug it off":
                    mike.say "Well I'm not Mom and Dad."
                    mike.say "Maybe it's time you realised that, Minami!"
                    show minami angry
                    "Minami actually stamps her foot at this."
                    $ minami.love -= 5
                    hide minami
                    show sasha sad at center
                    with moveoutleft
                    "Then she balls her fists and storms out."
                    "Sasha and I watch her go."
                    "But she's the one that breaks the awkward silence."
                    sasha.say "I...I'm sorry if I was a bit hard on her, [hero.name]."
                    sasha.say "I guess I just saw red."
                    sasha.say "Is she going to be okay?"
                    "I shake my head and let out a sigh."
                    mike.say "That's up to her, Sasha."
                    mike.say "She's a big girl now."
                    mike.say "And it's time she started acting like one."
                "Punish Minami":
                    mike.say "Yeah, well I'm not Mom and Dad."
                    mike.say "And if I were them, I'd have done things differently."
                    hide sasha
                    show minami annoyed at center
                    with moveoutright
                    "I hardly notice Sasha pick up her bass and slip out of the room."
                    "Because all of my attention is focused on Minami right now."
                    mike.say "Like maybe I'd have doled out a little punishment every now and then..."
                    "With that, I take hold of Minami's wrist and sit down on the sofa."
                    "Taken by surprise, she doesn't have the time to resist."
                    hide minami
                    show minami spank
                    with vpunch
                    "And so she ends up bent over my lap a moment later."
                    minami.say "Big bro..."
                    minami.say "What are you..."
                    "Minami only has time to get that far."
                    "Because as she's speaking, I lift up her skirt."
                    show minami spank middle speed
                    "And then I bring my hand down on her exposed buttocks."
                    show minami spank down surprise
                    play sound spank
                    with hpunch
                    "The sound of the contact is unexpectedly loud."
                    show minami spank down pain
                    "A crack that takes everyone by surprise."
                    minami.say "Ah..."
                    show minami spank middle
                    minami.say "Y...you spanked me!"
                    show minami spank down
                    play sound spank
                    with hpunch
                    "The second slap lands a second later."
                    "And Minami yelps again."
                    mike.say "I'm not done yet, Minami."
                    mike.say "Not by a long shot!"
                    show minami spank middle
                    "And with that, I keep on going."
                    show minami spank down
                    play sound spank
                    with hpunch
                    "Every slap to her cheeks makes Minami wail."
                    show minami spank middle
                    "She wriggles and writhes in my lap too."
                    show minami spank down
                    play sound spank
                    with hpunch
                    "Her petite body squirms the whole time."
                    show minami spank middle
                    "And I can feel my cock getting hard beneath her too!"
                    show minami spank down marks pleasure
                    play sound spank
                    with hpunch
                    "Soon enough Minami's butt-cheeks are bright red."
                    show minami spank middle
                    "A perfect match for the cheeks on her face as well."
                    show minami spank down
                    play sound spank
                    with hpunch
                    "I can see the shame that's making them burn."
                    "I only stop when my hand feels numb."
                    hide minami spank
                    show minami hunt
                    "And then I let Minami get to her feet."
                    "It's only now that I actually realise what I just did."
                    "Any moment I'm expecting Minami to slap me across the face."
                    "She'd be well within her right to do it too!"
                    "But instead she just stands there, hands behind her back."
                    minami.say "Th...thank you, big bro."
                    minami.say "That was weird..."
                    minami.say "But weird in a good way!"
                    hide minami with moveoutright
                    "Before I can ask her what she means, Minami hurries out of the room."
                    "Which leaves me alone with a sore hand."
                    "That and wondering what the hell just happened between us."
                    if minami.sub.max < 100:
                        $ minami.sub.max = 100
                    $ minami.sub += 2
    $ game.room = "livingroom"
    return

label minami_kiss_me:
    call minami_greet from _call_minami_greet_5
    show minami
    "I lean in close to Minami, nothing more than a familiar gesture that I've made a thousand times before."
    "And I'm so close that I don't even see her head turn as I do so, or her lips part."
    menu:
        "Kiss her" if not minami.flags.nokiss:
            hide minami
            show minami kiss
            with dissolve
            "She kisses me softly, and full on the mouth, lingering in the moment."
            "And before I know what's happening, I'm kissing her back too."
            "Neither of us seems to care about the taboo of what we're doing."
            "And the kiss becomes more intense with each second that passes."
            "Because right now, all we care about is each other..."
            $ minami.flags.kiss += 1
            $ minami.love += 1
            $ minami.siscon += 1
            hide minami kiss with dissolve
        "Don't kiss her":
            "Minami looks hurt when I push her away."
            $ minami.love -= 1
    hide minami
    return

label minami_get_out_male:
    if game.from_room != "bathroom":
        show minami angry
        if minami.activity["clothes"] == "underwear":
            minami.say "Please can you step out?"
        else:
            minami.say "I am naked. Please can you step out?"
        if not minami.flags.peeping_tom:
            $ minami.siscon += 1
        hide minami
    else:
        "I hear a voice through the door."
        if game.room == "bathroom":
            minami.say "[hero.name] I need the bathroom, can you step out?"
        else:
            minami.say "[hero.name], can you step out?"
        mike.say "Sure."
    return

label minami_not_get_out_male:
    if minami.get_clothes() == "naked":
        call minami_not_get_out_naked_male from _call_minami_not_get_out_naked_male
    else:
        call minami_not_get_out_clothed_male from _call_minami_not_get_out_clothed_male
    return

label minami_not_get_out_naked_male:
    show minami
    "Minami is naked..."
    mike.say "Sorry, Minami. I didn't know you would be here."
    minami.say "You know... I don't mind if you come in..."
    if not minami.flags.peeping_tom:
        $ minami.siscon += 1
    hide minami
    return

label minami_not_get_out_clothed_male:
    show minami
    if minami.get_clothes() == "underwear":
        "Minami is in her undies..."
    mike.say "Sorry, Minami. I didn't know you would be here."
    minami.say "Stop it, we know each other well enough not to be bothered by that..."
    if not minami.flags.peeping_tom:
        $ minami.siscon += 1
    hide minami
    return

label minami_likes_blondes:
    minami.say "Hey there, big bro!"
    minami.say "Watcha doing?"
    show minami with dissolve
    "At the sound of Minami's voice, my head snaps around to see her standing in front of me."
    "Or to be more precise, it's the exact tone of her voice that makes me jump to attention."
    "It's one that I've heard her use so many times in the past, on Mom, Dad and me alike."
    "She's trying to sound nonchalant, but there's a sly, almost wheedling quality to it."
    "And the only possible explanation is that she wants something."
    "But it's something she thinks she can't be upfront about too."
    mike.say "Ah, nothing important, Minami."
    mike.say "Not as important as you, anyway."
    "Sure, it's a shameless bit of flattery on my part."
    "But it puts a smile on Minami's face all the same."
    show minami blush
    minami.say "Aww, big bro!"
    minami.say "That's so sweet."
    "I return Minami's smile, trying to keep her in a good mood."
    mike.say "Was there something you needed, Minami?"
    mike.say "Or did you just come to say hi?"
    "I watch as Minami clasps her hands behind her back and rolls her eyes."
    "I know that it's all an act, her trying to look innocent and all that."
    "But she's so cute when she does this that I can't help enjoying the show."
    show minami -blush
    minami.say "Oh no..."
    minami.say "I was just passing and thought I'd see how you were, big bro."
    mike.say "So there's nothing eating you right now, huh?"
    mike.say "No juicy morsel of gossip that you're just dying to talk about?"
    "For a moment I think that Minami might actually be able to hold back."
    "That maybe she's telling the truth and she does just want to chat."
    "But then I see the cracks start to appear, and she can't help herself."
    minami.say "Well, big bro..."
    minami.say "Now that you mentioned it..."
    minami.say "What's up with Sasha dying her hair?!?"
    "Ah, so that's what this is all about."
    "Sasha just dyed her black hair blonde."
    "And Minami's fishing for a reason why."
    mike.say "I dunno, Minami."
    mike.say "Maybe she just wanted a change?"
    minami.say "I guess, big bro."
    show minami annoyed
    minami.say "But she's like a goth, or a metal fan or something."
    minami.say "I thought she was into all that dark stuff."
    minami.say "It's super weird for her to just change like that."
    show minami normal
    minami.say "Unless she did it for someone..."
    "I know exactly where Minami's going with this."
    "But I'm still not going to give her the satisfaction of a straight answer."
    mike.say "Maybe she's got a secret admirer, Minami?"
    mike.say "You know, a lot of guys think blondes are hot."
    "The moment that the words are out of my mouth, Minami pounces on them."
    "She's been stalking around like a cat all this time."
    "And now she finally has something that she can sink her claws into."
    minami.say "You say 'guys', big bro..."
    minami.say "But is that ALL guys?"
    minami.say "I mean, you're a guy, right?"
    mike.say "I was last time I checked, Minami."
    minami.say "Are you one of them?"
    show fx question
    minami.say "Do you think blondes are hot?"
    menu:
        "I do":
            "Well, the short answer is that I do."
            "So what's the point in trying to deny it?"
            mike.say "Yeah, Minami."
            mike.say "I think blondes are pretty hot."
            mike.say "Sasha looks hotter too, now that she's gone blonde."
            "Minami nods at this, trying to keep her face neutral."
            "But you don't need to be a genius to see what's happening here."
            "It's all she can do to keep from touching her hair."
            "Her thick, glossy and gorgeous hair."
            "Which just happens to be as black as an ebony midnight!"
            show minami annoyed
            minami.say "Oh...I see."
            minami.say "That's...interesting, big bro."
            mike.say "Are you okay, Minami?"
            mike.say "You look kind of edgy."
            mike.say "Like there's somewhere you need to be?"
            show minami normal blush
            minami.say "Yeah...I..."
            minami.say "I need to pick something up from the drugstore - that's it!"
            minami.say "I wonder if they're still open right now? Wait here"
            hide minami with moveoutright
            "And with that, Minami hurries off."
            $ minami.flags.haircut = True
            $ game.pass_time(1)
            scene bg black with timelaps
            scene bg livingroom with timelaps
            show minami happy with moveinright
            minami.say "What do you think big bro?"
            menu:
                "I like":
                    mike.say "I like it Minami."
                    $ minami.love += 1
                "I don't like":
                    mike.say "I prefer your natural color."
                    $ minami.sub += 1
                    show minami annoyed
                    minami.say "Oh...I see."
                    hide minami with moveoutright
                    $ minami.flags.haircut = False
            $ game.room = "livingroom"
        "Not really":
            "Well, the short answer is that I don't."
            "So what's the point in trying to tease her about it?"
            mike.say "Nah, Minami."
            mike.say "Blondes don't do it for me."
            mike.say "Doubly so when it's out of a bottle too!"
            "Minami nods at this, trying to keep her face neutral."
            "But you don't need to be a mind-reader to sense what's going on in her head right now."
            "It's all she can do to keep from touching her hair."
            "Her thick, glossy and gorgeous hair."
            "Which just happens to be as black as an ebony midnight!"
            show minami annoyed
            minami.say "Oh...I see."
            minami.say "That's...interesting, big bro."
            show fx question
            minami.say "So you don't think it makes Sasha look hotter?"
            mike.say "No way, Minami!"
            mike.say "I preferred her when she was rocking the black hair."
            mike.say "That's so much sexier!"
            show minami happy
            "It's almost like Minami can't keep her triumph from bursting out."
            "I think she might start purring like a cat any second!"
            "But she somehow manages to keep it all in."
            "She simply leans closer and plants a little kiss on my cheek."
            mike.say "Huh?!?"
            mike.say "What's that for?"
            minami.say "Oh, just for being the best big bro."
            "And with that, Minami hurries off."
    return

label minami_event_04:
    scene expression f"bg {game.room}"
    "Drawn by the sound of someone wailing and pleading for help, I walk around the side of the house."
    "It's not until I turn the corner that I recognise the voice as belonging to Minami."
    scene bg house with fade
    "But what's much more surprising than that is the view that greets me once I'm around the back."
    "There's Minami's butt, wiggling from side to side as it sticks up in the air!"
    "At first I think that she must be on her hands and knees for some unknown reason."
    "But then I notice that it's only the lower half of her that's visible."
    scene minami stuck with fade
    "The rest of her seems to be on the other side of the door, sticking through a small hole."
    "Of course - the cat-flap, or the doggy-door, whatever you call it."
    "So that explains how Minami ended up down there, but not why."
    mike.say "Ah, Minami..."
    mike.say "What on earth are you doing?"
    "At the sound of my voice, Minami seems to redouble her struggling."
    "Her legs begin scrambling as though she's trying to escape being seen."
    "Which is ridiculous to watch, as she's well and truly stuck."
    minami.say "Big bro?"
    minami.say "Is that you?"
    minami.say "Oh shit - this is SO embarrassing!"
    if not bree.hidden:
        bree.say "[hero.name]!"
        bree.say "Thank god you're here!"
        "[bree.name]'s face pops up in the kitchen window, making me jump a little."
        "I can tell from the harassed look on her face that she's been trying to help."
        "But despite whatever she might have tried, Minami's still stuck."
    mike.say "I'm still not sure what's going on here..."
    minami.say "I...I lost my keys, big bro."
    minami.say "I was going to call you and ask you to let me in."
    minami.say "I thought you'd be mad at me for being so scatter-brained."
    minami.say "And I got all embarrassed."
    minami.say "But then I saw the doggy-door..."
    mike.say "And you thought you could fit?"
    minami.say "You have to help me, big bro!"
    minami.say "I can't stay stuck like this!"
    "I nod, trying to clear my mind while Minami whines for me to free her."
    if not bree.hidden:
        "Maybe talking to [bree.name] would be a better idea?"
        "After all, she's been doing all she can to help since before I arrived on the scene."
        mike.say "No luck just pulling her through on your side, [bree.name]?"
        bree.say "No, [hero.name]."
        bree.say "But maybe if you push and I pull?"
        bree.say "Okay - let's give it a try."
    show minami stuck mike
    if not bree.hidden:
        "[bree.name] disappears from the window and I crouch down behind Minami."
    else:
        "I crouch down behind Minami."
    "I put my hands on her ass and take a firm hold."
    "Which makes her squeal and wriggle in alarm."
    minami.say "Hey - what's happening?!?"
    if not bree.hidden:
        mike.say "Hold on, Minami."
        mike.say "[bree.name]'s going to pull while I push."
        show minami stuck mike bree pull
    else:
        mike.say "Push forward as hard as possible Minami."
    "A moment later I feel Minami being pulled forwards."
    "And I push as hard as I dare too."
    if not bree.hidden:
        show minami stuck mike bree breetryhard pull
    minami.say "Ow...ow...ow..."
    minami.say "That hurts!"
    if not bree.hidden:
        "[bree.name] stops pulling and I stop pushing."
        "But then I hear her shout from the other side of the door."
        show minami stuck mike -bree lay
        bree.say "Let's try again when you're ready, okay?"
        mike.say "Okay, [bree.name] - give me a second to catch my breath."
    else:
        "Minami stops pushing and I do the same."
        show minami stuck mike lay
        minami.say "Let's try again when you're ready, Big bro?"
        mike.say "Okay, Minami - give me a second to catch my breath."
    "Actually, I don't need to catch my breath at all."
    "More like I need to rearrange things inside of my pants."
    "I've been pushing on Minami's pert little ass this whole time."
    "And it's made me as stiff as a board down there!"
    "Actually, now that I come to think of it."
    "She's helpless right now and [bree.name]'s on the other side of the door..."
    menu:
        "Be bad":
            "So what's the point in letting it go to waste?"
            "Hastily unzipping my pants, I pull out my cock."
            "And then I lift up Minami's skirt and pull down her panties."
            show minami stuck mike up
            minami.say "Wha...what's going on?"
            minami.say "Big bro, what are you doing back there?"
            mike.say "Nothing to worry about, Minami."
            mike.say "Just loosening things up..."
            "All this time my eyes are focused on what lies between Minami's legs."
            "The neat, tight little lips of her pussy are laid bare before me."
            "And I can't resist teasing them with the tip of my cock."
            show minami stuck mike up minamisurprised
            minami.say "Oh...oh god!"
            minami.say "What's that?!?"
            "For all of the alarm in her voice, Minami's body betrays her."
            "I can already feel the folds of her pussy getting slick."
            "And they begin to part almost as soon as I push against them."
            mike.say "Just pushing, Minami..."
            mike.say "That's all..."
            show minami stuck mike up minamitryhard
            "A moment later I feel my cock sink into Minami."
            "And I do just what I said I would, pushing all the way inside of her."
            show minami stuck mike up minamisurprised
            $ minami.love += 4
            "Minami's cries of alarm stretch out into a long moan."
            "She begins to pant almost as soon as I start to thrust in and out."
            "But the sound is punctuated with yelps as I pound her ass against the door."
            if not bree.hidden:
                bree.say "That's great, [hero.name]."
                bree.say "Whatever you're doing, don't stop."
                bree.say "Keep it up and we'll have her free in no time!"
                "Of course, [bree.name]'s got no idea what's going on."
                "But I can't help being thrilled by her urging me to keep going."
                "And I start to redouble my efforts as a result."
            "Every time I push forwards, I go as deep into Minami as possible."
            if not bree.hidden:
                "The thrill of what I'm doing and the danger lend a sense of urgency."
                "All of which means it's not long before I can feel myself cumming."
            "With one final effort, I push all of my weight against Minami's ass."
            show minami stuck mike up minamiahegao with hpunch
            "I shoot my load into her, and she squeals as she's jolted forwards."
            "The force I manage to put into it jams her through the hole."
            with hpunch
            "Minami almost pops off of my cock, cum dripping out of her as she goes."
            "Luckily for me, her skirt is pulled down as she goes through the doggy-door."
            "And once she's inside it looks like the same thing yanked down her panties too."
            "I get gingerly to my feet as the backdoor opens to let me in."
            scene bg kitchen
            if not bree.hidden:
                show bree at left
            show minami blush at right
            with fade
            if not bree.hidden:
                "And once inside, [bree.name] and I look down at Minami, in a heap on the floor."
                "She can hardly meet our eyes, her cheeks flushed red with embarrassment."
            else:
                "And once inside, I look down at Minami, in a heap on the floor."
                "She can hardly meet my eyes, her cheeks flushed red with embarrassment."
            minami.say "Ooh..."
            minami.say "Big bro.."
            minami.say "What did you push me with?!?"
            $ minami.sub += 1
        "Be good":
            "But this is no time to be thinking of things like that."
            "What kind of a guy would take advantage of Minami while she's helpless?"
            "Instead I redouble my efforts to free her."
            if not bree.hidden:
                mike.say "Right, [bree.name] - let's do it!"
                bree.say "Okay, [hero.name] - here goes!"
            minami.say "Oh shit!"
            if not bree.hidden:
                show minami stuck mike bree pull
                "[bree.name] pulls with all her might on one side of the door."
                "And at the same moment, I push from the other."
            "For a moment, I don't think it's going to work."
            if not bree.hidden:
                show minami stuck mike bree breetryhard pull
            "But then something gives, and Minami shoots forwards."
            with hpunch
            minami.say "Aargh!"
            "I almost smash my face into the door as she comes unstuck."
            "And the last thing I see is her feet disappearing through the doggy-door."
            "I get gingerly to my feet as the backdoor opens to let me in."
            scene bg kitchen
            if not bree.hidden:
                show bree at left
            show minami blush at right
            with fade
            if not bree.hidden:
                "And once inside, [bree.name] and I look down at Minami, in a heap on the floor."
                "She can hardly meet our eyes, her cheeks flushed red with embarrassment."
            else:
                "And once inside, I look down at Minami, in a heap on the floor."
                "She can hardly meet my eyes, her cheeks flushed red with embarrassment."
            minami.say "Ooh..."
            minami.say "Big bro.."
            minami.say "My ass is so sore!"
            $ minami.sub += 2
    return

label minami_pregnant_request:
    "Had it been any other girl, I might have missed the signs."
    "But I've known Minami since we were both kids."
    "And so I can pretty much read her like a book."
    "There's something on her mind, it's written all over her face."
    "So I might as well take a deep breath and just ask the question."
    mike.say "Minami..."
    mike.say "Is everything okay?"
    mike.say "You seem a little distracted, you know?"
    show minami surprised
    "Minami looks surprised at first, like she's been caught out."
    show minami normal
    "But then she shakes her head and gives me a sweet little smile."
    "It's one of the kind that always manages to melt me."
    "And so I can't help being drawn in by it."
    show minami blush
    minami.say "Oh, big bro!"
    minami.say "You can read me like a book."
    minami.say "But yeah, there is something I wanted to ask you."
    "Minami takes a deep breath and then lets it out as an even bigger sigh."
    minami.say "And get ready, because it's kind of a big ask!"
    "I do my best to keep a smile on my face."
    "And I give Minami what I hope looks like an encouraging nod."
    "But I can already feel the apprehension building inside of me."
    "What on earth could she have be about to ask me?"
    mike.say "Go on, Minami."
    mike.say "You can ask me anything - you know that!"
    minami.say "Okay, big bro."
    minami.say "Here goes nothing..."
    minami.say "I've decided that I want to have a baby - with you!"
    "Suddenly I feel like I've had the air literally dragged out of my lungs."
    "All I can do is blink as I open and close my mouth in complete silence."
    "Minami watches me with the smile still fixed on her face."
    "If anything, she seems to be sympathetic to my situation."
    show minami sad blush
    minami.say "Aww, poor big bro!"
    minami.say "I did say it was a big one."
    minami.say "But anyway - what do you think?"
    minami.say "You wanna have a baby with me, huh?"
    "By now I can feel some of the confusion starting to lift."
    "I can finally begin to make some sort of sense out of it all."
    "And then I realise I wasn't hearing her wrong."
    "Minami really does want to have a baby with me!"
    menu:
        "Agree":
            "My gut instinct is to remind Minami of all the crap that we've been through already."
            "She's gone from being my adopted sister to my girlfriend."
            "And on top of that there's been all the drama with Mom and Dad too."
            "But then it hits me that I'm still letting all of that steer our lives."
            "Aren't we supposed to be putting all that behind us?"
            "Shouldn't we be living the lives that we want?"
            mike.say "I might be crazy for saying this, Minami."
            mike.say "But yeah, I want to have a baby with you!"
            show minami surprised
            "Now it's Minami's turn to stare at me in shocked silence."
            "But she seems to take far less time to recover her senses."
            minami.say "Did...did you say yes?"
            minami.say "Did you really say yes?!?"
            "I can't help grinning at Minami."
            show minami happy
            "And when I nod in response, she squeals happily."
            minami.say "Oh...my...god!"
            minami.say "I'm going to be a mommy!"
            minami.say "This is going to be the best thing ever!"
            show minami close
            "Minami throws her arms around me and hugs me as tight as she can."
            "And I return the gesture, enjoying the sensation of her body against mine."
            "She moves in my embrace, letting me feel every motion she makes."
            minami.say "I can't wait to get started, big bro."
            minami.say "And I never got pregnant before."
            minami.say "So we're gonna need a LOT of practice..."
            $ minami.love += 2
            $ minami.flags.pregrequest = True
        "Refuse":
            "I can't actually believe that she'd ask me to do something like this."
            "Not after all of the drama that we've been through together."
            "She's literally gone from being my adopted sister to my girlfriend."
            "And on top of that there's all the drama that came along with it too!"
            mike.say "Minami, I really don't think we're ready for that."
            mike.say "At least not yet."
            show minami annoyed
            minami.say "Y...you don't want to have kids with me?"
            minami.say "Is that it, big bro?"
            minami.say "You think it'd be too weird?"
            "I can see the tears already beginning to well in Minami's eyes."
            "She looks like she's about to burst out crying."
            "And it breaks my heart to see her like that."
            show minami sad
            mike.say "No, Minami, no..."
            mike.say "It's not like that at all!"
            minami.say "Then tell me how it is, big bro?"
            minami.say "I want to be with you."
            minami.say "I want to have your babies!"
            "Minami's on the verge of wailing by now."
            "And I'm struggling to calm her down."
            mike.say "I want that too, Minami - really I do!"
            mike.say "But I don't want to rush into anything, yeah?"
            mike.say "Look, Mom and Dad were really screwed up."
            mike.say "And I don't want to screw us up too!"
            mike.say "I love you too much to let that happen."
            "Minami bites her lips and screws up her face."
            show minami cry
            "And then finally she begins to sob."
            minami.say "Oh, big bro..."
            minami.say "You're so good to me!"
            minami.say "And I love you SO much!"
            minami.say "Just promise that I can have your babies one day?!?"
            show minami close
            "Minami throws her arms around me, pressing her head into my chest."
            "And I wrap my arms around her too, pulling her closer still."
            $ minami.love -= 2
    return

label minami_male_ending:
    $ game.hour = 16




    if renpy.has_label("minami_achievement_3") and not game.flags.cheat:
        call minami_achievement_3 from _call_minami_achievement_3
    $ game.room = "church"
    scene bg church wedding with fade
    "They always say stuff like you never know what's around the corner, you know?"
    "That life's what happens to you while you're making plans that never come off."
    "And I'll admit I used to think that all of that was nothing more - just stuff people said."
    "But standing here at the altar, waiting for Minami to come walking down it..."
    "Well, I couldn't have been more wrong!"
    "And I shudder to think what a younger version of me would have made of all this."
    "Back then Minami was just my annoying little sister, a blight on my teenage social life."
    "Sure, I knew that she adored me, because she followed me around like a puppy."
    "And yeah, I knew that she was adopted - not that it mattered at the time."
    "But I guess that I never really knew her as a person."
    "At least not until she came here to study and moved into the same house as me."
    "Of course I'd lived with her before, but not like this."
    "Without Mom and Dad there, we were forced to adapt."
    "We kind of had to learn to see each other as adults and not kids."
    "She was still the same old Minami most of the time."
    "She could be childish and more than a little spoilt at her worst."
    "But I also came to appreciate the things about her that were harder to see back home."
    "Like the fact that she's sweet, loyal and full to bursting with life..."
    "Sorry, sorry..."
    "I know that I'm singing her praises when I haven't even mentioned the elephant in the room."
    "Yes, Minami and I were raised as brother and sister."
    "But she was adopted, so that makes this officially NOT weird or creepy!"
    "And yes, my Mom and Dad were kind of manipulating us into getting hitched the whole time."
    "But again, we found out and thwarted their dastardly scheme, like a couple of kid detectives."
    "All of which left us free to...well...to get married anyway."
    "But the difference is that we wanted to do this, we weren't manipulated into it."
    "I guess that's the beautiful truth of our relationship."
    "Mom and Dad thought they were pushing us towards what they wanted."
    "And instead Minami and I grew to love each other for our own reasons."
    "I mean, we found out that our childhoods were built on a lie."
    "Yet we're still tying the knot today."
    "Which can only be because we love each other."
    "Just then, music swells and I'm shaken out of my musings."
    show minami wedding blush at center, zoomAt(1.0, (640, 720)) with dissolve
    show minami at center, traveling(1.5, 5.0, (640, 1040))
    "I turn my head to see Minami starting to walk up the aisle."
    "She looks radiant in the dress she chose."
    "The combination of Japanese designs and a modern cut suit her down to the ground."
    "And most beautiful of all, her smile is beaming."
    if minami.is_visibly_pregnant:
        "The adjustments made to accommodate her swelling belly are subtle."
        "But the sight of it makes me feel butterflies in my own stomach."
        "I'm still staggered by the fact that our child is growing inside of her!"
    else:
        "All in all, Minami looks more than ever like the woman she was meant to be."
        "She's still petite and youthful, but there's a maturity about her now that's growing all the time."
        "It makes my stomach fill with butterflies at the thought of spending my life with her!"
    show wedding minami with fade
    "Minami smiles up at me as she reaches the altar, her cheeks flushing with emotion."
    "I can see how nervous she is right now, how excited too."
    show wedding minami priest with fade
    "But she keeps a lid on her emotions as the priest begins the ceremony."
    "Priest" "Dearly beloved."
    "Priest" "We are gathered here to unite these two souls in holy matrimony..."
    "The ceremony seems to pass in the blink of an eye."
    "And before I know it, we're a the point where we exchange our vows."
    "Priest" "Do you, [hero.name], take Minami to be your lawful, wedded wife?"
    mike.say "I...I do!"
    "The priest nods as Minami beams up at me."
    "Priest" "And do you, Minami, take big bro..."
    "I see the priest's eyes go wide as he accidentally uses Minami's pet name for me."
    "He must have heard her say it so many times that it rubbed off on him!"
    "Minami's eyes go wide and she giggles in amusement."
    "And I can't help smiling too."
    "Priest" "Ahem..."
    "Priest" "Where was I..."
    "Priest" "Ah yes...do you, Minami, take [hero.name] to be your lawful, wedded husband?"
    minami.say "Of course I do - yes!"
    "The priest nods, clearly relieved to have gotten that part of the ceremony over and done with."
    "Priest" "I call upon all those present."
    "Priest" "That if anyone knows of a reason these two should not be wed..."
    "Priest" "Let them speak now, or forever hold their peace!"
    "For a moment, both Minami and I are still, holding our breath."
    "I feel her take my hand, squeezing it tightly."
    "Both of us are just waiting for Mom or Dad to crash through the church doors at any moment..."
    "Priest" "...very well."
    "Priest" "I therefore pronounce you husband and wife."
    "Priest" "You may kiss the bride."
    "Minami and I let out an audible sigh of relief."
    scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
    show minami kiss wedding
    with fade
    $ minami.flags.kiss += 1
    "And then I pull her towards me to do just as the priest said."
    "Minami kisses me back with just as much eagerness, almost leaping into my arms."
    "That's it, we did it."
    hide minami
    show minami wedding happy at center, zoomAt(1.5, (640, 1040))
    with fade
    "We're not pretending to be adopted siblings anymore."
    "We're husband and wife."
    "And we're taking the first steps in writing our own story on our own terms."

    show minami ending with fade
    minami.say "Hey there, everyone - it's me, Minami!"
    minami.say "You know, the smart, cute and spunky little sister that everyone loves?"
    minami.say "Yeah, that's the one!"
    minami.say "Anyway, it's finally my turn to tell a part of the story - so yay!"
    minami.say "Here goes..."
    minami.say "I suppose it's a bit weird, the way that big bro and I got to where we are."
    minami.say "I mean, it's what I always wanted, even when I was younger."
    minami.say "We're together, and he loves me SO much that it's almost unreal."
    minami.say "But I guess that's kind of what makes it feel a little weird sometimes too."
    minami.say "I got exactly what I wanted - all of my dreams have come true."
    minami.say "It's just how we got here was a lot more twisty and strange than I imagined it would be."
    minami.say "Like when we found out that Mom and Dad had been manipulating us all our lives."
    minami.say "I was so freaked out when I discovered that was why they adopted me."
    minami.say "That they picked me out as the perfect wife for big bro."
    minami.say "It...it made me wonder about us, you know?"
    minami.say "Made me wonder if what I felt for him was even real."
    minami.say "But that was when he helped me to see the truth."
    minami.say "Big bro was there for me through it all."
    minami.say "He was like my rock, yeah?"
    minami.say "No matter how hard it got, he was always there for me."
    minami.say "And that's when I realised how I really felt about him."
    minami.say "Even knowing what Mom and Dad did, I still loved him."
    minami.say "Sure, they brainwashed me pretty good."
    minami.say "But I still don't think that they could make me love him."
    minami.say "It was big bro did that, him and nobody else!"
    minami.say "And you know what - it's still a bit weird."
    minami.say "But it's a good weird, if that makes sense?"
    minami.say "After the wedding, we lived with [bree.name] and Sasha for a little while."
    minami.say "But we were already looking for a place of our own."
    minami.say "We moved out a couple of months later, into a house all our own."
    minami.say "Big bro's still doing whatever he does at work every day."
    minami.say "And I'm still studying at uni, working towards my degree."
    if minami.flags.mikeBabies >= 1 or minami.is_visibly_pregnant:
        minami.say "It's gotten a little bit more crowded around here since Mei arrived on the scene."
        minami.say "And big bro's trying his very best to be a working daddy and a doting husband."
        minami.say "Truth is, he's pretty hopeless - but his heart's in the right place!"
    else:
        minami.say "I still have no idea what comes after that."
        minami.say "But I'm looking forward to finding out."
    minami.say "As for planning out our future together, we haven't really talked about it."
    minami.say "I guess that's because someone else was scheming to steer us down a certain path."
    minami.say "It wasn't planning stuff that got us where we are today."
    minami.say "And so maybe we're better off leaving the future up to chance?"
    minami.say "At least I know that I'm not going to be the one wasting time worrying about it."
    minami.say "I've got far better things to do with my life!"
    minami.say "And I'm sure big bro does too."

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not minami.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_15
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_15
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label minami_morningwood:
    "I'm up unusually early this morning, and with no urge to turn off the alarm and go back to sleep."
    "That's pretty unusual for me, and at first I have no idea why I'm awake and full of energy."
    "But when I pull back the bedclothes and swing my legs onto the floor, the mystery is solved."
    "I'm presented with the sight of morning wood."
    "Or more like morning forest!"
    menu:
        "Try to ignore the inconvenience":
            $ hero.fun -= 5
            $ hero.cancel_event()
            return
        "Let Minami know what she's responsible for":
            pass
    "No wonder I've woken up like this - I need to put what's between my legs to good use!"
    "I hop out of bed as quietly as I can, then scuttle to the door."
    scene bg secondfloor with fade
    "Slipping out, I hurry through the house until I reach Minami's bedroom."
    "I ease the door open, praying that the sound doesn't wake her or anyone else."
    "Because this is going to be pretty tough to explain if someone catches me!"
    "Luckily for me, the door opens almost without a sound."
    scene bg bedroom5 with fade
    "I slip inside and close it behind me, already scanning the room."
    "I can see Minami's bed in the gloom and make out the shape upon it."
    "And as I edge my way closer, I can hear the sound of her breathing too."
    "Minami doesn't snore."
    "Well...not exactly."
    "Instead she makes a little breathy sound, almost like a sigh."
    show sleep minami with fade
    "She's laid on her back, arms stretched out above her head."
    "Sound asleep she looks even more beautiful than when she's awake."
    "In fact, she looks like a cute little pixie or an imp."
    "One that's fallen fast asleep after a long spell of naughtiness."
    "Rather than fading, my erection is getting more intense by the second."
    "It feels like my cock is throbbing simply from being this close to minami."
    "I cover the last few feet to the foot of the bed."
    "Then I lift the covers and slide under them."
    "The first thing I see is the little nightie Minami has on."
    "Oh man...is she trying to torture me?"
    "That thing's barely long enough to keep her decent!"
    minami.say "Mmm..."
    minami.say "B...b...b..."
    minami.say "Big...Bro..."
    "For a moment I think the sound is Minami waking up."
    "I flinch, ready to make a dash for the door."
    "But then I realise that Minami's just babbling in her sleep."
    "I breathe a sigh of relief."
    "Then I listen more closely, my interest piqued."
    minami.say "Oooh..."
    minami.say "Big...Bro..."
    minami.say "SO...Big...Bro..."
    "I look down as one of Minami's hands moves."
    "And I see it come to rest on one of her pert little breasts."
    "Then my eyes go wide as she starts to squeeze and fondle it."
    "A closer look shows me that her nipples are hard as tiny rocks!"
    "I watch in fascination, unable to tear my eyes away."
    "Well, that is until Minami's other hand reaches down between her thighs."
    "I hold my breath as it hitches up her nightie."
    "And then it begins to stroke at her neat little pussy!"
    "I can't help leaning in closer for a better look."
    "Minami keeps on babbling as she seems to pleasure herself in her sleep."
    minami.say "Big Bro..."
    minami.say "My Big Bro..."
    minami.say "Big for me..."
    minami.say "Mmm...all mine..."
    "I can't keep from leaning in until I'm practically looming over Minami."
    "She's playing with herself in her sleep!"
    "And she's dreaming of me while she's doing it!"
    "This is amazing!"
    "I'm trying not to touch Minami for fear of waking her."
    "But my cock must be hanging lower than I thought."
    "Because I suddenly feel her hand close around my shaft!"
    mike.say "Urgh!"
    minami.say "Oh..."
    minami.say "All for me..."
    minami.say "Big Bro inside me..."
    "Minami's hand tugs at my cock, pressing it into the lips of her pussy."
    scene minami missionary
    show minami missionary closed
    with fade
    "And I have no choice but to go along with it or else risk being caught in the act."
    "She must be pretty worked up, as I sink straight into her without resistance."
    "As soon as I'm inside her, Minami arches her back."
    "Her legs and arms wrap around me, holding me tight."
    "And she clings to me like her life depends on it!"
    mike.say "Oh shit..."
    mike.say "Minami..."
    "At the sound of my voice, Minami's eyes slowly open."
    show minami missionary open
    "But there's no sudden shock or surprise in them."
    "In fact, she treats me to a slow, sleepy smile."
    minami.say "Oh..."
    minami.say "Big bro..."
    minami.say "I thought I was dreaming."
    minami.say "But this is SO much better!"
    "Minami tightens her hold on me, giggling with delight."
    "And I can't help redoubling my efforts now that she's awake a seems to approve."
    show minami missionary speed
    "Her body only seems to become more accommodating to me, her moans more wanton."
    show minami missionary closed
    "Part of me can't believe this thing is playing out so well."
    "I was kind of worried Minami would freak out at finding me in her bed."
    "But she's loving every minute of being woken up like this!"
    "The only question is how long I can keep going."
    "I'm already thrilled at the way I've managed to surprise her."
    "And every thrust feels like it's a stolen pleasure."
    "The mischievous nature of what we're doing only adds to the pressure."
    "That and he fact that Minami's desperate for me to fuck her!"
    minami.say "Ooooh..."
    show minami missionary open
    minami.say "Oh...big bro..."
    minami.say "You're gonna...make me...make me cum!"
    "Minami's not joking either!"
    "I can feel her body quaking as her orgasm takes hold."
    "She bucks and twitches under me, squeezing my cock."
    "And as soon as that happens, I don't have a hope of holding on."
    with hpunch
    "I can only let go and shoot my load into her."
    show minami missionary ahegao with hpunch
    "Minami nods as she let out a series of little whimpers."
    "But the look in her eyes tells me that she's satisfied."
    "A moment later I tumble off her and roll onto my back."
    "Minami turns onto her side and lays her head on my chest."
    minami.say "Mmm..."
    minami.say "You're so much better than my alarm clock, big bro!"
    minami.say "And you can wake me up like that anytime you like..."
    $ minami.sexperience += 1
    $ game.room = "bedroom5"
    $ hero.flags.morningwood = TemporaryFlag(True, "day")
    return

label minami_snooping:
    $ game.hour = 7
    scene bg bedroom1
    "I wake up fuzzily, the reluctance that I always feel to start the day making me want to turn over and go straight back to sleep."
    "And so I fumble around blindly on the bedside table, trying to hit the snooze button on my phone and kill the alarm."
    "It's then that I notice something really weird, namely that there's no alarm to silence."
    "Before I can even begin to think about what's going on, I see the shape of something rising up beneath the covers."
    "Look, before you say it, I know what you're thinking, and you're wrong."
    "I get morning wood just like any other guy, sure."
    "But if that's my dick, then there's something wrong down there."
    "Because even I wouldn't want it to get that large - or want there to be two of them either!"
    "I lift the bedclothes, still not totally awake or able to make sense of what's going on."
    "Though hearing the sound of giggling coming from down there does start to help clear things up."
    "And so it comes as less of a surprise when I see two faces staring up at me from under there."
    scene bg black
    show bj breeminamisasha bree sasha breehand
    bree.say "[hero.name] - you're finally awake!"
    sasha.say "Damn it..."
    sasha.say "I was sure we could do this without waking him!"
    "I shake my head, baffled by what I'm seeing."
    mike.say "Huh..."
    mike.say "Do...do what?"
    show bj breeminamisasha sashahappy breehappy
    "Rather than answer my question, [bree.name] and Sasha look at each other, giggling again."
    "And then, almost as one, they lean in and begin to lick at the base of my cock."
    mike.say "Oh...oh, I see!"
    "[bree.name] and Sasha eye me as they go to work, impish delight clear to see in their gazes."
    "First they suck on one of my balls each, making me gasp at the sudden sensation."
    "And then they release them in order to start climbing the shaft with their lips and tongues."
    "But at the same time, I feel fingers and thumbs still caressing my scrotum all the while."
    "Though I can't tell whether they belong to [bree.name] or Sasha!"
    "Not that it matters, as I'm far more interested in the sensations they're creating higher up."
    "With [bree.name] on my left and Sasha on my right, they finally reach the head of my cock."
    "There they take it in turns to take the head between their lips and caress the tip with their tongues."
    "And only when both have had more turns than I can count does Sasha allow [bree.name] to swallow me deeper."
    show bj breeminamisasha breeonmouth
    "While [bree.name]'s head bobs up and down, Sasha goes back to licking me up and down."
    "[bree.name] takes me right up to the point where I think I'm about to come."
    show bj breeminamisasha sashaonmouth sashahand -breehand
    "Then she releases me, allowing Sasha to eagerly take her place."
    "The change is almost seamless for me, and soon they're working me in the same way again."
    show bj breeminamisasha breeonmouth breehand -sashahand
    "If we'd been doing this at the end of the day, or with more warning, I could have gone longer."
    "But thanks to them taking me by surprise like this, I know I can't hold on anymore."
    show bj breeminamisasha breeopen sashaopen -breeonmouth
    "As if sensing what's about to happen, [bree.name] lets my cock fall out of her mouth just in time."
    "And then they both lean in close, letting the inevitable happen."
    show bj breeminamisasha breeshot breefacial sashafacial
    "When it does, no more than a second or two later, [bree.name] and Sasha get a literal face-full."
    "The cum hits the sides of their faces closest to me, striping their cheeks and foreheads."
    "Holding their mouths open too, they even manage to catch some on their tongues."
    "[bree.name] and Sasha giggle to one another as they swallow all that they can catch too."
    scene bg bedroom1
    show sasha underwear at left
    show bree underwear at right
    "I watch helplessly as they slip out from under the bedclothes, waving to me as they go."
    sasha.say "I feel SO full, [bree.name]."
    sasha.say "Might have to skip breakfast this morning."
    bree.say "Ah, I know what you mean, Sasha."
    bree.say "I wish I could start the day like this every time!"
    hide bree
    hide sasha
    "I shake my head as the door closes behind them, unable to believe my luck."
    "I'm living under the same roof as two insanely hot girls."
    "And we're sharing each other at the same time as we're sharing the house!"
    "Ah, no...that should be living with three hot girls."
    "Can't forget Minami too..."
    "For all that's changed between Minami and myself recently, some things are still just the same as they've always been."
    "Of course the fact that we've actually bitten the bullet and slept together is a pretty big deal."
    "Yet she's still the same old Minami, and that means she's just as nosey as ever!"
    "At first I was sure that I could keep the fact that [bree.name], Sasha and I are a threesome hidden from her."
    "But just recently I've noticed Minami sniffing around, looking for clues to see if something's going on."
    "She keeps on quizzing me about what my plans are and whether I'll be in or out for most of the day."
    "And I keep overhearing her asking [bree.name] and Sasha the same things too."
    "I'm still laid there, naked under the covers and my mind wandering, when Minami literally bursts in on me."
    show minami sleep with hpunch
    minami.say "Hah, caught you!"
    minami.say "I knew that you were..."
    show fx question
    minami.say "On your own in bed?!?"
    "I sit bolt upright, genuinely shocked at her suddenly appearing out of nowhere."
    mike.say "Jesus Christ, Minami!"
    mike.say "Haven't you ever heard of knocking?!?"
    mike.say "You scared the living shit out of me!"
    "Minami does that thing to me then."
    show minami sad
    "The thing where she instantly turns into a frightened little animal caught in the headlights of oncoming traffic."
    "And as much as I want to yell at her, tell her to get the hell out, I'm already regretting my harsh words to her."
    show minami blush
    minami.say "I...I'm sorry, big bro."
    minami.say "I just wanted to...to..."
    show minami normal -blush
    minami.say "Surprise you...yeah, that's right - to surprise you!"
    "I roll my eyes, sitting up in bed and letting the covers fall down to my waist."
    "I should be telling her off for barging in like that."
    "But then I see Minami eyeing me up from across the room."
    show minami hunt
    "She's all but licking her lips at what she can see, unable to keep from showing how horny she is right now."
    "And if she thought she was going to walk in on [bree.name], Sasha and me, then there's no wonder!"
    "Fuck me, but my sister's such a filthy little bitch."
    "Though I can't deny she can have the same effect on me too!"
    "And she looks super-hot, standing there in her pyjamas, wanting it so badly..."
    minami.say "Ah, big bro..."
    mike.say "Yeah, Minami?"
    minami.say "Well...you're in bed."
    minami.say "And I'm in your room."
    minami.say "So...I could be in your bed."
    show minami blush
    minami.say "And you could be in me too..."
    menu:
        "I'm not in the mood.":
            mike.say "Minami, it's first thing in the goddamn morning!"
            show minami -blush
            minami.say "Aww, big bro!"
            minami.say "It doesn't have to be epic or anything."
            minami.say "Even if it's over quickly, that's okay - I just want you in me, please!"
            mike.say "No, Minami, no way."
            mike.say "Maybe later, but not now - and that's final."
            show minami angry
            show fx exclamation
            minami.say "No fair - I'm horny as hell!"
            mike.say "Then go break out your toys, Minami!"
            "Balling her fists and planting them on her waist, Minami gives me a sullen look."
            minami.say "Why don't you want to fuck me, big bro?"
            minami.say "Is it because you've got something going on with another girl?"
            show fx question
            minami.say "Maybe something with [bree.name] or Sasha, huh?"
            menu:
                "There's nothing between me and [bree.name] or Sasha!":
                    "I shake my head, trying to laugh off the accusation as ridiculous."
                    mike.say "That's crazy, Minami."
                    mike.say "You should listen to yourself, you really should."
                    mike.say "You're starting to sound paranoid!"
                    show minami annoyed
                    "Minami frowns at this, wrinkling her nose in annoyance."
                    minami.say "Well, I think it's crazy that you won't fuck me, that's what I think."
                    show fx anger
                    show minami angry
                    minami.say "And if I have to make do with a vibrator, then you can do the same with your hand!"
                    hide minami
                    "And with that, she storms out of my bedroom, leaving me alone and feeling frustrated."
                    $ minami.love -= 5
                    $ minami.flags.haremdenied += 1
                    if minami.flags.haremdenied < 3:
                        $ hero.cancel_event()
                "I sleep with [bree.name] and Sasha.":
                    "I shrug, feeling tired of keeping the secret and worrying about being discovered the whole time."
                    "Sure, I maybe should have cleared it with [bree.name] and Sasha beforehand."
                    "But the words are out of my mouth before the potential fallout can stop me."
                    show minami normal
                    mike.say "If you really want to know the truth Minami, then okay."
                    mike.say "I'm sleeping with [bree.name] and Sasha."
                    show fx exclamation
                    "Minami's eyes go wide with shock, her mouth hanging open as she shakes her head."
                    show fx question
                    minami.say "You...you're serious, big bro?"
                    minami.say "You're doing them both, and neither of them knows it?!?"
                    "I shake my head, trying to sound as reasonable as I can."
                    "Rather than like the kind of creep that sleeps with his little sister and his housemates under the same roof..."
                    mike.say "No, Minami - it's not like that."
                    mike.say "[bree.name], Sasha and I are in a committed relationship."
                    mike.say "A threesome, if you like."
                    "By now, Minami's eyes are like saucers, her mouth quivering at what she's hearing."
                    "I honestly expect her to explode at any moment."
                    "So it comes as some surprise when she simply nods instead."
                    minami.say "Th...that makes sense...kind of...I guess."
                    minami.say "This is the big city, after all..."
                    minami.say "I'm sorry, big bro - things are just so...different here!"
                    hide minami
                    "And with that, Minami turns and walks out of my bedroom, leaving me alone again."
                    "But as calm as she seemed to be just now, I can't help thinking this matter's not settled."
                    $ game.flags.ongoinghomeharem = "minami"
                    $ game.flags.tempminamiharem = TemporaryFlag(True, randint(1, 3))
            return
        "Come here.":
            "[bree.name] and Sasha took it out of me just now, but I know I still have enough left for Minami too."
            "I don't have to be up for a while yet, so I can easily squeeze in some lazy sex with her."
            "Plus it'll take her mind off the task of trying to find out what's going on between me and the other girls too..."
            mike.say "You know what, Minami - that makes it sound like I'm still dreaming!"
            mike.say "So let's see if I am, huh?"
            "I lift the bedclothes, making it plain that she's about to get what she wants."
            show minami hunt
            show minami blush
            "Minami's cheeks flush red at the compliment."
            show minami naked
            "And she instantly tears off her pyjamas, hopping to the side of the bed."
            "If my cock had begun to get soft for even an instant, the sight of Minami soon fixes that."
            "As she slips under the sheets and wriggles her ass into my lap, it's hard as rock once more."
            scene minami cowgirl
            "Minami wastes no time in grabbing it by the shaft and thrusting it between her thighs with one hand."
            show minami cowgirl up
            "And with the other, she pushes my hands onto her petite breasts without a second's pause."
            show minami cowgirl surprised
            minami.say "Whoa, big bro."
            minami.say "You're a BEAST this early in the morning!"
            show minami cowgirl vaginal
            minami.say "Oh...oh, yeah!"
            "She guides me into herself as she says this, quivering the whole time."
            "There's no resistance whatsoever, meaning that she must have been slick well before now."
            "And the thought of her standing there, dripping into her pyjamas makes me want her all the more."
            mike.say "What about you, Minami?"
            mike.say "You're the dirty little mare that wants it so bad!"
            mike.say "I bet you woke up wanting it up you, right?"
            show minami cowgirl orgasm
            "By now I'm already as deep into Minami as I can go, gaining speed with every passing second."
            "She's yelping and wailing too, nipples stiff between my fingers as I squeeze her breasts hard."
            show minami cowgirl speed
            minami.say "Yeah...yeah..."
            minami.say "You know me...big bro..."
            minami.say "I...dream of it...you...fucking me!"
            minami.say "Wake up...wet...pussy wanting...you to fill it!"
            "God but she's something else when she's like this!"
            "All I can think of is how much I want her, how good she feels around my cock..."
            "And then it's all over, just like that."
            show minami cowgirl creampie ahegao with vpunch
            "I feel myself cumming inside of Minami and her leaning back into me as hard as she possibly can."
            with vpunch
            "Even when I'm done, she's still wriggling and writhing on my cock, twitching with exquisite pleasure."
            with vpunch
            "Instinctively, I wrap Minami in my arms, spooning her with the whole of my body."
            "I stay inside of her for as long as I possibly can."
            "And I enjoy the sensation of surrounding her so completely."
            "A part of me knows that I'll have to deal with the problem of [bree.name] and Sasha."
            "Sooner or later, Minami will find out - of that I have no doubt."
            "But for now, I don't want to do anything but lie here with her in my arms."
            $ minami.flags.haremdenied += 1
            if minami.flags.haremdenied < 3:
                $ hero.cancel_event()
    if minami.flags.haremdenied >= 3:
        $ Harem.find(sasha, name="home")[0].leave("minami")
        $ game.flags.ongoinghomeharem = False
    return


label minami_birthday_date_male:
    $ DONE["minami_birthday_date_male"] = game.days_played
    $ game.active_date.clothes = "date"
    scene bg street with fade
    minami.say "Ouch!"
    minami.say "Big bro, I nearly walked into something hard!"
    minami.say "Can't you let me see where we are yet?!?"
    mike.say "What and spoil the surprise?"
    mike.say "No way, Minami!"
    mike.say "Just a little further, I promise."
    "I have my hands over Minami's eyes right now."
    "And I'm doing the best I can to guide her steps."
    "But you can imagine how hard that is in a public place."
    "Plus there's the fact that she's complaining the whole time too!"
    "Finally getting her in the exact spot I wanted, I breathe a sigh of relief."
    mike.say "Okay, Minami..."
    mike.say "Here we go!"
    show minami a date annoyed at center, zoomAt(1.5, (840, 1040)) with easeinright
    "I whip away my hands, letting Minami see where we are for the first time."
    show minami a surprised at center, zoomAt(1.5, (640, 1040)) with ease
    "And I'm pretty pleased to see the look of annoyance on her face disappear."
    "It becomes one of amazement as she turns around, staring at her surroundings."
    minami.say "Oh wow..."
    minami.say "This is..."
    show minami a normal at startle
    minami.say "This is the aquarium!"
    "I nod happily, pleased with her reaction."
    mike.say "It sure is."
    mike.say "You've been bugging me to bring you here since you moved in."
    mike.say "So here we are."
    mike.say "Happy birthday, Minami!"
    show minami happy
    "Minami shoots me a smile, then goes back to gawping at all she can see."
    "And who can blame her for that."
    "Especially when we're standing in front of a tank shaped like a column."
    "One must be two storeys tall, and is filled with the most stunning tropical fish."
    minami.say "Oh, this is going to be SO cool!"
    show minami normal
    minami.say "You should have brought me here sooner, big bro!"
    "I detect a hint of accusation in Minami's tone as she says this."
    "Like she's having a stab at me for waiting so long to bring her here."
    menu:
        "Don't react":
            "Ah, what does it matter if Minami's acting a little spoilt?"
            "I'm not going to let that get in the way of us having a good time."
            mike.say "Well whatever, Minami."
            mike.say "We're here now."
            mike.say "So let's make up for lost time."
            "Minami looks a little surprised by my attitude."
            "But she nods and puts her arm in mine."
            minami.say "That's one of the things I like about you, big bro."
            show minami happy
            minami.say "You're so much more laid back than mom and dad."
            minami.say "Like you really know how to have fun!"
            $ game.active_date.score += 15
        "We're here now aren't we?":
            mike.say "Well we're here now, Minami."
            mike.say "Surely that's the important thing?"
            "Minami shoots me a withering look."
            "And she shakes her head."
            show minami annoyed
            minami.say "You know what, big bro..."
            minami.say "You're starting to sound so much like dad."
            minami.say "I mean, it's not even funny!"
            mike.say "Hey!"
            mike.say "I do not sound like dad!"
            minami.say "You will until you quit grouching!"
            minami.say "So you'd better shut up and let me enjoy myself."
            $ game.active_date.score -= 10
    scene bg aquarium
    show minami a normal date
    with fade
    "As we stroll around inside the aquarium, I can see I made the right choice."
    show minami a date happy at left with fade
    "Minami's flitting from one tank to the next, gazing at the fish in wonder."
    show minami a normal at center, right with fade
    "She seems to want to stop and read the information by each one too."
    show minami a surprised at center, zoomAt(1.4, (1040, 1000)) with fade
    "Oohing and aahing as she absorbs facts about this underwater world."
    "More than once, Minami calls me over to a tank and asks me what I think."
    show minami a normal at center, zoomAt(1.5, (340, 1040)) with fade
    "But she seems most interested in the ones that contains seahorses and jellyfish."
    "In fact, she keeps looking from one to the other."
    "Like she's trying to make up her mind about something."
    mike.say "What's the matter, Minami?"
    minami.say "Hmm..."
    minami.say "Seahorses or jellyfish, big bro?"
    mike.say "What about them?"
    minami.say "Just pick one already!"
    show minami annoyed
    minami.say "Seahorses or jellyfish?"
    "It doesn't look like Minami's going to be any more forthcoming."
    "So I guess I'll just have to pick one or the other."
    menu:
        "Seahorses":
            mike.say "Ah..."
            mike.say "Seahorses?"
            show minami surprised
            "Minami looks surprised by my choice."
            "But then she seems to ponder it a little deeper."
            "Narrowing her eyes and nodding."
            show minami normal
            minami.say "Most guys would have said jellyfish."
            minami.say "But not you, big bro."
            minami.say "Because you can see past a seahorse's long face."
            minami.say "And to the true beauty that hides inside of it."
            mike.say "Erm..."
            mike.say "Thank you - I think!"
            show minami happy
            "Minami smiles and takes hold of my hand."
            "Then she leads me to the next exhibit."
            $ game.active_date.score += 15
        "Jellyfish":
            mike.say "Ah..."
            mike.say "Jellyfish?"
            show minami surprised
            "Minami looks surprised by my choice."
            "But then she seems to ponder it a little deeper."
            "Narrowing her eyes and nodding."
            show minami normal
            minami.say "I suppose that makes sense."
            minami.say "Jellyfish are elegant and beautiful to the eye."
            minami.say "So as a typical guy, you'd be attracted to that."
            minami.say "But you fail to notice their deadly sting."
            minami.say "Until it's too late!"
            "Minami turns and walks away."
            "Which leaves me in a stare of confusion as I hurry after her."
            $ game.active_date.score -= 10
    show minami normal at center, zoomAt(1.5, (640, 1040)) with fade
    "The next thing we come across is the entrance to the small theatre in the aquarium."
    "Minami takes one look at the sign announcing the next show and lets out a squeal of delight."
    show minami surprised at startle
    minami.say "Oooh!"
    show minami happy
    minami.say "Big bro, they have a mermaid show on today!"
    minami.say "And mermaids are SO cute!"
    minami.say "We HAVE to see it."
    "Before I can say as much as a single word, Minami leaps into action."
    show minami normal with hpunch
    "She grabs hold of my wrist and drags me through the doors."
    hide minami with easeoutright
    "Then she marches me down one of the rows of seats inside."
    "I see that instead of a stage, the theatre has a tank forming the wall we're facing."
    "There doesn't seem to be a way out of this for me."
    "So I just decide to settle down in my seat and enjoy the show."
    "Who knows - maybe the mermaids will be seriously hot?"
    scene swimmingrace_bg_03 at center, zoomAt(1.75, (1000, 1040)), dark, blur(5)
    "As the show begins, I see that I was right."
    "All of the mermaids are played by pretty cute girls."
    "And they might all be wearing mermaid costumes."
    "But that doesn't mean I can't see the shapes of their legs beneath."
    "So it's well worth my time to watch the goings on in the tank."
    show minami a date normal at center, zoomAt(2.0, (1040, 1240)) with dissolve
    "A little way into the show, Minami leans in close."
    "And she whispers into my ear."
    minami.say "Hey, big bro..."
    minami.say "I'm getting an idea for my next cosplay project."
    menu:
        "Listen to her idea":
            mike.say "Let me guess, Minami..."
            mike.say "Is it something to do with mermaids?"
            "Minami nods eagerly, not picking up on my sarcasm."
            show minami happy
            minami.say "Got it in one!"
            minami.say "But those girls have such amazing bodies!"
            minami.say "Do you really think I could pull it off too?"
            if hero.charm >= 75:
                "I smile and shake my head."
                mike.say "Of course you can pull it off, Minami."
                mike.say "Who says mermaids have to be big, bouncing bimbos!"
                mike.say "I bet a petite one with a natural figure would look great."
                show minami tehe
                "Minami looks delighted with my answer."
                "She practically beams as she soaks up the praise too."
                minami.say "Thanks for the vote of confidence, big bro."
                minami.say "Just for that, you get a reward."
                minami.say "When I'm done making my mermaid costume..."
                show minami happy
                minami.say "You're going to be the first person to see me in it!"
                "I nod, humouring Minami at first."
                "But as I watch the rest of the show, the idea grows on me."
                "I bet she would look great in one of those costumes."
                "And even better, I could have the chance to peel it off her too!"
                $ game.active_date.score += 15
            else:
                "I look at the girls performing in the tank."
                "And then back at Minami sitting next to me."
                "Not even trying to hide the fact I'm sizing her up."
                mike.say "Sure you could, Minami."
                mike.say "Your tits might be smaller than most of theirs."
                mike.say "But you can always make up for that by showing off more flesh!"
                show minami annoyed
                "Minami looks horrified by my answer."
                "And she turns her gaze away from me."
                "Instead looking straight at the tank."
                "Urgh...women!"
                "They ask you a question."
                "Then they freak out when you give them an honest answer!"
                $ game.active_date.score -= 10
        "Suggest an alternative" if hero.has_skill("hypnosis"):
            mike.say "Let me guess, Minami..."
            mike.say "Is it something to do with mermaids?"
            "Minami nods eagerly, not picking up on my sarcasm."
            show minami happy
            minami.say "Got it in one!"
            "I'm nodding too by now, because I like the sound of that."
            "Only I think the costume could to with a few modifications."
            "And if I'm honest, one major element removing!"
            "I think this calls for a little of the old hypnosis..."
            show minami normal
            mike.say "Minami..."
            mike.say "Look into my eyes."
            mike.say "Don't look around my eyes - look into my eyes!"
            show minami mindless
            mike.say "Okay you're under my power."
            mike.say "When you wake you will want to dress as a mermaid."
            mike.say "But you won't want to wear a seashell bra or bikini top."
            mike.say "And you'll want to lounge around the pool at home dressed like that!"
            mike.say "Aaannnd...you're awake again."
            if not active_girl.flags.hypnosisConsent and randint(1, 100) <= 25 + active_girl.flags.hypnosisOffset:
                "Minami blinks in confusion for a moment."
                show minami annoyed
                "Then she frowns at me and shakes her head."
                minami.say "Big bro!"
                show minami angry
                minami.say "What was all that silly stuff you just said?"
                minami.say "About me going topless as a mermaid?!?"
                mike.say "Erm..."
                mike.say "I was just joking, Minami."
                mike.say "That's all!"
                "Minami gives me a suspicious look."
                show minami normal
                "Then she turns her gaze back to the mermaids in the tank."
                minami.say "Maybe letting you see my mermaid costume isn't such a good idea after all!"
                "Bloody hell!"
                "I really need to practice my hypnosis skills more regularly!"
                $ game.active_date.score -= 10
            else:
                "Minami blinks in confusion for a moment."
                "Then she frowns and cocks her head on one side."
                minami.say "You know what would make my cosplay unique?"
                minami.say "If I didn't wear one of those silly seashell bras!"
                show minami flirt
                minami.say "I bet no real mermaid would be seen dead in one!"
                "I nod eagerly as the suggestion takes root in Minami's brain."
                minami.say "Hmm..."
                minami.say "I'm going to need to practice swimming in a tail too."
                show minami happy
                minami.say "Lucky for me we have a pool at home!"
                "Minami looks at me a moment later."
                "And she seems worried about something."
                show minami annoyed
                minami.say "Erm, big bro..."
                minami.say "Would you mind me going topless as a mermaid?"
                minami.say "You know, by the side of the pool?"
                "I do the best I can not to look excited at the prospect."
                mike.say "If that's what it takes, Minami."
                mike.say "Then I'm willing to make the sacrifice."
                show minami happy
                minami.say "Oh, thanks, big bro - you're the best!"
                $ game.active_date.score += 15
        "Propose an alternative to the show" if hero.has_skill("high_libido"):
            "I nod, too preoccupied with watching the show to really listen."
            "The sight of all those female bodies in revealing costumes."
            "It's just too much for me to bear."
            "And I know I'm going to need some relief!"
            show minami normal
            minami.say "I want to create a mermaid costume."
            minami.say "But those girls have such amazing bodies!"
            minami.say "Do you really think I could pull it off too?"
            mike.say "Forget about pulling that off, Minami."
            mike.say "I need you to pull this off instead!"
            "I've already opened my flies and pulled out my cock with one hand."
            "And I use the other to put Minami's hand on it."
            if minami.love + hero.charm >= 200 and minami.sexperience >= 1:
                "Minami looks down and I hear her yelp with surprise."
                show minami surprised
                "I hold my breath, convinced I'm going to get called out by her."
                "Or else caught out by an employee coming over to see what all the fuss is about."
                "But then Minami surprises me with a mischievous grin."
                show minami flirt
                minami.say "Oh, big bro..."
                minami.say "You want a hand-job from Minami the mermaid?"
                "Minami begins to stroke the shaft of my cock."
                "And I nod hastily, trying to encourage her all the more."
                "Minami works my cock for almost the whole of the remaining show."
                "And it makes the sight of all those half-naked bodies all the more enjoyable."
                "Just before the show ends, I shoot my load over her hand."
                show minami happy
                "Looking down, I see Minami gazing up at me, the same smile still on her face."
                $ game.active_date.score += 15
            else:
                "Minami screws up her face in disgust."
                show minami surprised
                "And she pulls her hand away with surprising strength too."
                minami.say "Eww!"
                show minami angry
                minami.say "Big bro!"
                minami.say "Put that thing away!"
                "I almost jump out of my seat as Minami wails at me."
                show minami annoyed
                "And I rush to do as she says too."
                "For fear of an employee coming over to see what all the fuss is about."
                "The problem is that this means I spend the rest of the show with an erection."
                "And by the end of it, I'm feeling totally frustrated!"
                $ game.active_date.score -= 10
    scene bg aquarium
    show minami a normal date
    with fade
    "Once we're out of the theatre, there's still a lot of the aquarium to see."
    "And Minami shows no signs of getting bored of staring at more tanks full of fish."
    "The room we walk into seems to have some pretty unusual stuff in it."
    "And I notice the theme here is endangered species."
    show minami surprised
    minami.say "Oh, big bro!"
    show minami sad
    minami.say "Have you read what it says here?"
    minami.say "About how many species could go extinct?"
    show minami annoyed
    minami.say "Those poor whales and dolphins!"
    "I read the signs that Minami's pointing to."
    "And she's right, it does make for grim reading."
    menu:
        "It's depressing!":
            "Fucking hell...that's so depressing!"
            mike.say "Yeah, Minami..."
            mike.say "That's fucking grim!"
            "Minami nods her head."
            show minami normal
            "But she still looks incredibly concerned."
            minami.say "But what can we do, big bro?"
            show minami annoyed
            minami.say "We're not running the world, are we?"
            "I shake my head and sigh."
            mike.say "That doesn't mean we should do nothing, Minami."
            mike.say "If we do all we can, then that's something."
            mike.say "And the more people we encourage to do the same thing..."
            minami.say "It all has to add up!"
            show minami happy
            minami.say "If everyone helps, then we could save them!"
            $ game.active_date.score += 15
        "It's more complex":
            "But I feel like what they're saying ignores the bigger picture."
            mike.say "It's not just the whales, Minami."
            mike.say "The problems much bigger than that!"
            "Minami shakes her head, unable to see my point."
            minami.say "But those poor creatures!"
            minami.say "Shouldn't we be saving the cute ones first?"
            mike.say "I don't think so."
            mike.say "It'd be dumb to save the whale and not the world."
            show minami angry
            "Minami makes a petulant sound and starts to sulk."
            minami.say "Well, big bro..."
            minami.say "I think that's just mean!"
            $ game.active_date.score -= 10
    show minami normal
    "We're almost done walking around the aquarium."
    "But then I see Minami looking at me sideways."
    show minami annoyed
    "And I just know that means there's something on her mind."
    mike.say "What is it, Minami?"
    show minami normal
    minami.say "What is what?"
    mike.say "Come on, Minami!"
    mike.say "I know what that look means."
    mike.say "So out with it already!"
    minami.say "Okay, okay..."
    show minami hunt
    minami.say "I was kinda wondering if you got me anything for my birthday?"
    if not hero.has_gifts:
        "Ah shit!"
        "I knew there was something I'd forgotten."
        "Well, it's too late now."
        "I'm just going to have to bullshit my way out of this one."
        mike.say "But I did get you something, Minami."
        mike.say "It was this trip to the aquarium!"
        show minami normal
        "I see Minami's face drop a little."
        "But she instantly tries to hide her disappointment."
        "I guess she doesn't want to seem ungrateful."
        show minami normal
        minami.say "Oh yeah..."
        minami.say "Of course!"
        minami.say "Sorry, big bro - this is the best gift ever!"
        "Phew..."
        "Looks like I got away with that one!"
        $ game.active_date.score -= 20
        $ minami.love -= 10
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_14
        if _return != "done":
            if _return not in ["None", "exit"]:
                mike.say "Of course I did, Minami."
                "I pull out the gift and hand it over."
                show minami normal
                mike.say "It's not huge."
                mike.say "Because I paid for us to get in here too."
                mike.say "But I hope you like it all the same."
                play sound [paper_ripping_2, paper_ripping_1, paper_ripping_2]
                "Minami accepts the gift and begins to open it a second later."
                show minami happy
                minami.say "Thanks, big bro!"
                minami.say "I'm sure it'll be great."
                show minami normal
                if _return:
                    "As soon as she sees what's inside the wrapping, Minami's expression changes."
                    "Before it was one of anticipation, but now it's unmistakably one of amazement."
                    "She looks up at me, shaking her head in disbelief."
                    show minami happy
                    minami.say "Big bro..."
                    minami.say "Where did you find this?!?"
                    minami.say "Nobody knows where to get stuff like this!"
                    "I shrug and smile, enjoying being praised by Minami."
                    mike.say "Ah, it's not that hard, Minami."
                    mike.say "Especially when it's for someone as special as you!"
                    "Minami answers that by throwing her arms around me and squeezing with all her might."
                    minami.say "Oh, big bro..."
                    minami.say "You really are the best!"
                    $ game.active_date.score += 20
                else:
                    "As soon as she sees what's inside the wrapping, Minami's expression changes."
                    "Before it was one of anticipation, but now it's unmistakably one if disappointment."
                    "But she still tries to hide it from me as best she can."
                    show minami annoyed
                    minami.say "Oh..."
                    minami.say "That's..."
                    minami.say "Nice...that's very nice."
                    show minami normal
                    "I feel my smile turning into a painful grimace as all of this is happening."
                    "And it's a relief when Minami puts the thing away and tries to change the subject."
                    $ game.active_date.score -= 10
            else:
                "Ah shit!"
                "I knew there was something I'd forgotten."
                "Well, it's too late now."
                "I'm just going to have to bullshit my way out of this one."
                mike.say "But I did get you something, Minami."
                mike.say "It was this trip to the aquarium!"
                show minami normal
                "I see Minami's face drop a little."
                "But she instantly tries to hide her disappointment."
                "I guess she doesn't want to seem ungrateful."
                show minami normal
                minami.say "Oh yeah..."
                minami.say "Of course!"
                minami.say "Sorry, big bro - this is the best gift ever!"
                "Phew..."
                "Looks like I got away with that one!"
                $ game.active_date.score -= 20
                $ minami.love -= 10
    show minami normal
    "Of course, the people that run the aquarium aren't stupid."
    "So on the way out of the place, we have to pass through the obligatory gift shop."
    "Suddenly we're surrounded by an ocean of colourful, aquatic-themed crap."
    "And Minami seems to be in her element!"
    minami.say "Oh...my...god!"
    show minami happy
    minami.say "They have T-shirts with dolphins on them!"
    minami.say "They have mugs shaped like manatees!"
    minami.say "And they have PLUSHIES!"
    "Minami dashes over to a huge pile of stuffed animals."
    "And for a moment I actually think she's going to dive bodily into them!"
    "But luckily for me, she just turns around with her arms filled."
    "Then she hugs them all under her chin."
    "And as she does so, she's looking at me with those huge eyes of hers!"
    show minami normal
    minami.say "Big bro..."
    mike.say "No, Minami!"
    minami.say "Please, big bro..."
    mike.say "Don't say it!"
    show minami happy
    minami.say "But they're SO CUTE!"
    menu:
        "Buy her plushies" if hero.money >= 200:
            "I feel like saying something about cuteness being exploited for nefarious ends."
            "About it being used for the purpose of emotional blackmail."
            "But instead I just sigh and then nod."
            mike.say "Okay, Minami, you win."
            mike.say "But we can't buy all of them."
            show minami normal
            mike.say "So just choose the ones you can't possibly live without, okay?"
            "Minami nods and returns to the plushie pile."
            "And when she comes back, I see she has less of them in her arms."
            "Maybe not as few as I'd have liked."
            show minami happy
            "But at least less than she had before."
            "Then we go to the checkout and I watch as the prices are rung up on the till."
            $ game.active_date.score += 15
            $ hero.money -= 200
        "Just leave":
            mike.say "No way, Minami."
            mike.say "Your room's already stuffed full of those things!"
            "Minami begins to pout almost as soon as I say no."
            show minami angry
            "And for a moment, I think she's actually going to stamp her foot."
            "But instead she frowns at me and turns her back."
            "Though I am relieved to see that she's walking back to the plushie pile."
            "Minami drops the stuffed animals and turns towards the door."
            "Which means that I have to hurry after her."
            $ game.active_date.score -= 10
    scene bg street
    show minami date normal
    with fade
    "Once we're out of the aquarium, I realise that it's later than I expected."
    mike.say "So..."
    mike.say "You want to head home, Minami?"
    mike.say "I mean...I'm not that tired myself."
    mike.say "But how about you?"
    if game.active_date.score >= 80 and minami.sexperience >= 1:
        show minami happy
        minami.say "Oh, I want to go home, big bro."
        minami.say "Can we get a taxi or something?"
        "I nod, already looking to flag one down."
        mike.say "It's okay to admit you're tired, Minami."
        mike.say "We packed a lot in today."
        show minami close date normal
        "Minami chooses that moment to step up close."
        "And she wraps her arms around me too."
        "Pressing her body close to mine."
        minami.say "Oh, I'm not tired."
        minami.say "I just want to be alone with you."
        show minami flirt
        minami.say "You know what I mean?"
        "I nod eagerly, hoping that I really do."
        "Because if Minami actually means she wants to watch TV on the sofa..."
        "Then I'm going to be majorly disappointed!"
        call minami_birthday_sex from _call_minami_birthday_sex
    else:
        minami.say "Nah, I'm still good."
        mike.say "Oh...great!"
        mike.say "Maybe we could..."
        "Minami holds up a hand, cutting me off before I can finish."
        show minami annoyed
        minami.say "Hold on there, big bro."
        minami.say "I told some of the girls from college I'd meet them later."
        "I shrug and nod."
        mike.say "Okay, Minami."
        mike.say "Maybe I could..."
        minami.say "Oh no..."
        show minami normal
        minami.say "Girls only!"
        minami.say "Catch you later, bi bro!"
        hide minami with easeoutright
        "And just like that, Minami turns and walks away."
        scene bg street with fade
        "Which leaves me standing all alone."
        "And feeling more than a little used too!"
    return

label minami_birthday_sex:
    scene bg house
    show minami date normal
    with fade
    "As soon as we arrive home and jump out of the taxi, Minami takes the lead."
    "She grabs hold of my wrist, almost dragging me up to the front door."
    "And then she makes it hard for me to open the damn thing by clinging onto me."
    "Under any other circumstances I'd be more than okay with what she's doing."
    "But right now I know that there's better things to be had if only I can make it inside!"
    hide minami
    show minami close date normal
    mike.say "Minami!"
    mike.say "Can't you wait a couple of seconds?"
    mike.say "At this rate, I'm going to drop my keys!"
    "All this earns me from Minami is a mischievous giggle."
    "Well, that and more of the same as she caresses me with both hands."
    minami.say "What's the matter, big bro?"
    show minami hunt
    minami.say "Am I too much for you to handle?"
    minami.say "Even as little as I am?"
    "Minami's pretending to pout as she says all of this."
    "Putting on her best impression of being helpless."
    "But I know full well that she's anything other than innocent."
    "And the mere thought of that is already making me hard!"
    "Finally I mange to extricate myself from Minami enough to open the door."
    scene bg livingroom
    show minami close date hunt
    with fade
    "We all but fall into the hallway, as she recovers her hold on me."
    "And I'm certain she's going to pounce on me right there."
    "So I blurt out a question in the hope of winning a momentary reprieve."
    mike.say "Urgh..."
    mike.say "So, Minami..."
    mike.say "Your place or mine?"
    mike.say "I...I mean, your ROOM or mine?"
    "This seems to be enough to stop Minami, for a moment at least."
    "And she gives me a knowing look."
    minami.say "Your room, obviously!"
    minami.say "Because mine is a mess right now!"
    "With that, I feel her grab hold of my arm for a second time."
    scene bg secondfloor
    show minami date hunt
    with fade
    "And as she pulls me towards the stairs, I go willingly."
    "As there's now nothing between us and our ultimate goal."
    "Minami hurries into the room ahead of me, not stopping to close the door."
    "Which leaves me to turn and close it behind us, as I don't want to be disturbed."
    scene bg bedroom1
    show minami date hunt
    with fade
    mike.say "Ok, Minami..."
    mike.say "I think we're alone..."
    "As soon as I turn around, Minami flies into action."
    "And she really does pounce on me this time!"
    "I'm forced to catch her as she leaps into my arms."
    "The weight of her forces me to stagger backwards."
    "And if not for the door, I'd have ended up on my back."
    "Minami doesn't give me any time to recover either."
    "Her arms are wrapped around my neck and her legs around my waist."
    hide minami
    show minami kiss date
    with fade
    $ minami.flags.kiss += 1
    "Then I feel her lips against mine, soft and impossibly sweet."
    "My own arms grab hold of her ass, holding up her weight."
    "And I return the kiss without the need for a single conscious thought."
    "Minami kisses me hungrily, her tongue deep in my mouth."
    "I can hear her gasping for breath the whole time."
    "Or maybe gasping from the desire that she's feeling."
    "I begin move my hands, trying to get a better grip on Minami."
    "And that's when the tips of my fingers stray between her legs."
    "I feel them slide over something that's warm and slick."
    "But Minami's reaction is far more dramatic than mine."
    "She quivers in my arms, her entire body shaking."
    "That's when I realise that I must be brushing her pussy."
    "And that she had to have pulled off her panties while I had my back turned."
    "I knew that she wanted it before now, and badly too."
    "Yet somehow that physical signal serves to turn me on more than anything else."
    "Now I'm not just eager to make love to Minami."
    "I feel like I just have to fuck her as soon as I possibly can."
    "There's no room for anything else in my head."
    "With this in mind, I start to walk across the room, heading for her bed."
    "She's still kissing me, and I keep on stroking her pussy with one hand."
    "Only when I feel the edge of the bed against my legs do either of those things stop."
    "And they stop because I throw Minami bodily down onto the mattress."
    minami.say "Oh, big bro!"
    minami.say "I love it when you take control!"
    "Minami smiles up at me as she says this."
    "And I can see her hitching up her skirt as she does so too."
    "Sure, she might like me being dominant some of the time."
    "But that doesn't stop her from being a tease."
    "Rather then offer an answer, I being to strip off my clothes."
    "I toss them aside as I climb onto the bed, looming over Minami."
    "I can see the anticipation building in her eyes."
    "All the while she's struggling out of her clothes too."
    "She manages it just as I'm on top of her."
    "The bra she's wearing pops off, freeing her pert little breasts."
    scene bg black
    show minami missionary
    with fade
    "They bounce and jiggle as they settle into their natural positions."
    "And the sight of them is almost enough to make me lose it, right there and then!"
    "Rather than lying down on top of Minami, I lower my head to her chest."
    "And I set about caressing her breasts with my lips and tongue."
    "I can feel her nipples hardening as I have one in my mouth."
    "Even better, I can hear Minami start to moan with pleasure."
    "And I can feel her wriggling beneath me too!"
    minami.say "Ah..."
    minami.say "Ooh..."
    minami.say "Please...don't stop!"
    "I could take that to mean Minami wanting to linger on her breasts."
    "But I have other ideas, and so I lower my head further still."
    "My lips travel slowly downwards, kissing Minami's flat stomach."
    "And with every inch, I my senses fill with the scent of my ultimate goal."
    "Minami is still wriggling with pleasure as my head dips between her thighs."
    scene bg black
    show minami cunnilingus mike lickpussy
    with fade
    "Though the moment my lips reach the ones between her legs, things seem to pick up."
    "Minami thrashes her arms on the bed as I start to lick and kiss her pussy."
    "But I don't even spare a thought for anything else as the taste fills my mouth."
    "Minami tastes musky and sweet, like that's the flavour of her sexual desire."
    "I push my tongue as deep into her as I can manage, hooked on the taste of her."
    "Minami's thighs close on me like the arms of a trap."
    "She pushes me down like her life depends on it."
    minami.say "B...big bro..."
    minami.say "I want you...so bad..."
    minami.say "Want you...inside me!"
    "As enthralled by Minami's pussy as I am right now..."
    "There's no way I can ignore her when she asks for something like that!"
    "Yeah, of course I want her right now, more than anything."
    "But the compulsion I feel is still hard to explain."
    "It's like Minami's able to command me with a single word."
    "I don't so much stand up, as leap up."
    "And the hop sees me landing on top of her."
    "I'm arched over Minami so that I can look her in the eye."
    scene bg black
    show minami missionary bedroom5
    with fade
    "Because my groin is on a level with her own."
    "But the height difference means our heads would otherwise be a foot apart."
    "And I want to be able to look her in the eye as the inevitable happens."
    "I don't even have to direct traffic down there, it just all clicks."
    "Minami's so ready for me that all it takes is a firm push on my part."
    mike.say "Oh fuck..."
    mike.say "Minami..."
    mike.say "You're amazing..."
    mike.say "The best!"
    "Minami nods desperately, pulling me down onto her."
    "She wraps her legs around me, embracing me as she does so."
    show minami missionary closed
    minami.say "Yes..."
    minami.say "Oh yeah..."
    minami.say "Fill me up, big bro..."
    minami.say "Please?"
    "I don't need to be asked to do that."
    "And I feel myself beginning to move inside of Minami a moment later."
    "The only part of my body in action is my groin and thighs."
    show minami missionary speed
    "They move with a furious speed as I thrust into Minami."
    "The rest of our bodies are locked together in a tight embrace."
    "Like we're afraid of being torn apart any second."
    "And that's the way I feel as I make love to Minami."
    "Desperate to make every second count and yet eager to see nature take its course."
    "It's almost like we feel that we have to do this thing in order to claim each other."
    "To mark each other out as belonging together."
    "I can feel Minami pulling me down onto her."
    "At the same time she's pushing herself up too."
    "Somehow we manage to move even faster and with more intensity than before."
    "Yet it still feels like we're curling up into an even tighter ball."
    "Where is this going to end?"
    "Are we going to burst into flames or something?"
    "But then I'm reminded of the way that this kind of thing usually ends."
    minami.say "Oh fuck..."
    minami.say "Big bro..."
    minami.say "I'm gonna cum!"
    "Minami squeezes me even harder as she loses it."
    "And the sensation is more than enough to do the same to me."
    with hpunch
    "I shoot my load into Minami while we're tied up together."
    show minami missionary ahegao with hpunch
    "Which makes her redouble her clenching and squeezing too."
    with hpunch
    "I can feel myself collapsing onto the bed."
    "But Minami doesn't release me as it happens."
    "Instead we roll together like a human pretzel."
    "Lying on the bed still entwined in each other's limbs."
    "Totally satisfied, I can already feel myself drifting towards sleep."
    "Though I'm sure I'll be a mass of cramps and aches in the morning because of it."
    $ minami.sexperience += 1
    call sleep ("minami") from _call_sleep_67
    $ game.room = "bedroom1"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
