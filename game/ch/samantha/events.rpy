init python:
    Event(**{
    "name": "samantha_start",
    "label": "samantha_start",
    "priority": 500,
    "conditions": [
        IsDone("samantha_event_01")
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "samantha_event_02",
    "priority": 500,
    "label": "samantha_event_02",
    "duration": 1,
    "conditions": [
        IsDone("samantha_start"),
        HeroTarget(
            IsGender("male"),
            IsRoom("bakery")
            ),
        PersonTarget(samantha,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 40),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/the_one.ogg",
    })

    Event(**{
    "name": "samantha_event_03",
    "label": "samantha_event_03",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("samantha_event_02"),
        IsHour(9, 17),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("park")
            ),
        PersonTarget(samantha,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 60),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/the_one.ogg",
    })

    Event(**{
    "name": "samantha_event_04",
    "label": "samantha_event_04",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("samantha_event_03"),
        IsNotDone("samantha_event_B01"),
        HeroTarget(
            IsGender("male"),
            Not(IsFlag("ryandead")),
            IsRoom("nightclub", "nightclubbar")),
        PersonTarget(samantha,
            Not(IsPresent()),
            Not(IsHidden()),
            MinStat("love", 80),
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "samantha_event_05",
    "display_name": "About Ryan",
    "label": "samantha_event_05",
    "duration": 0,
    "icon": "button_ryan",
    "conditions": [
        IsDone("samantha_event_04"),
        IsNotDone("samantha_event_B01"),
        HeroTarget(IsGender("male")),
        PersonTarget(samantha,
            IsActive(),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "samantha_event_A01",
    "label": "samantha_event_A01",
    "duration": 1,
    "priority": 500,
    "max_girls": 0,
    "conditions": [
        IsDone("samantha_event_05"),
        IsNotDone("samantha_event_B01"),
        IsNotDone("samantha_event_A02"),
        IsHour(22, 4),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            HasStamina()),
        PersonTarget(samantha,
            Not(IsPresent()),
            IsFlag("knows_ryancheats"),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "samantha_event_A02",
    "label": "samantha_event_A02",
    "duration": 2,
    "priority": 500,
    "conditions": [
        Or(
            IsDone("samantha_event_A01"),
            IsDone("samantha_event_E01"),
        ),
        HeroTarget(
            IsGender("male"),
            IsRoom("bakery")),
        PersonTarget(samantha,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 100),
            IsFlag("knows_ryancheats"),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/the_one.ogg",
    })

    InteractEvent(**{
    "name": "samantha_event_A03",
    "label": "samantha_event_A03",
    "duration": 2,
    "priority": 500,
    "conditions": [
        IsDone("samantha_event_A02"),
        HeroTarget(IsGender("male")),
        PersonTarget(samantha,
            IsActive(),
            MinStat("love", 150),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/the_one.ogg",
    })

    InteractEvent(**{
    "name": "samantha_event_A04",
    "label": "samantha_event_A04",
    "duration": 2,
    "conditions": [
        IsDone("samantha_event_A03"),
        HeroTarget(
            IsGender("male"),
            IsFlag("ongoinghomeharem", False)
            ),
        PersonTarget(samantha,
            IsActive(),
            MinStat("love", 170),
            ),
        ],
    "priority": 500,
    "do_once": True,
    "music": "music/roa_music/the_one.ogg",
    })





























    Event(**{
    "name": "samantha_event_B02",
    "label": "samantha_event_B02",
    "duration": 2,
    "conditions": [
        IsDone("samantha_event_B01"),
        IsHour(10, 18),
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            IsGender("male"),
            ),
        PersonTarget(samantha,
            IsPresent(),
            Not(IsHidden()),
            Not(IsFlag("knows_ryancheats")),
            MinStat("love", 120),
            Not(IsFlag("delay")),
            ),
        ],
    "do_once": True,
    "priority": 500,
    "music": "music/roa_music/the_one.ogg",
    })

    Event(**{
    "name": "samantha_event_B03",
    "label": "samantha_event_B03",
    "duration": 2,
    "max_girls": 0,
    "conditions": [
        IsDone("samantha_event_B02"),
        IsHour(20, 0),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home")
            ),
        PersonTarget(samantha,
            MinStat("love", 140),
            ),
        ],
    "priority": 500,
    "music": "music/roa_music/the_one.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "samantha_event_B04",
    "label": "samantha_event_B04",
    "duration": 1,
    "priority": 500,
    "max_girls": 0,
    "conditions": [
        IsDone("samantha_event_B03"),
        IsHour(16, 0),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            IsActivity("None"),
            Not(OnDate()),
            ),
        PersonTarget(samantha,
            IsFlag("unknown_father"),
            ),
        Or(
            PersonTarget(samantha,
                IsVisiblyPregnant(),
            ),
            IsDone("samantha_wedding_baby"),
            ),
        ],
    "music": "music/roa_music/the_one.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "samantha_event_C01",
    "label": "samantha_event_C01",
    "priority": 100,
    "conditions": [
        IsDone("samantha_event_B03"),
        IsHour(14, 15),
        HeroTarget(
            IsGender("male"),
            Not(IsFlag("ryandead")),
            Not(OnDate())),
        PersonTarget(samantha,
            Not(IsPresent()),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            Not(IsFlag("knows_ryancheats")),
            MinStat("love", 160),
            ),
        ],
    "chances": 10,
    "do_once": True,
    "music": "music/roa_music/the_one.ogg",
    "quit": False,
    })

    Event(**{
    "name": "samantha_event_C02",
    "label": "samantha_event_C02",
    "duration": 2,
    "priority": 500,
    "conditions": [
        IsDone("samantha_event_C01"),
        HeroTarget(
            IsGender("male"),
            Not(IsFlag("ryandead")),
            IsRoom("bakery")),
        PersonTarget(samantha,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 170),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/the_one.ogg",
    })

    Event(**{
    "name": "samantha_event_C03",
    "label": "samantha_event_C03",
    "duration": 2,
    "priority": 500,
    "conditions": [
        IsDone("samantha_event_C02"),
        IsDayOfWeek(5, 6, 7),
        IsHour(20, 22),
        HeroTarget(
            IsGender("male"),
            Not(IsFlag("ryandead")),
            IsRoom("livingroom"),
            IsFlag("sam_ryan_threesome"),
            ),
        PersonTarget(samantha,
            MinStat("love", 180),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/the_one.ogg",
    })


    Event(**{
    "name": "samantha_event_D01",
    "label": "samantha_event_D01",
    "duration": 2,
    "priority": 500,
    "conditions": [
        Or(
            IsDone("samantha_event_B01"),
            And(
                IsDone("samantha_event_B03"),
                PersonTarget(samantha,
                    Not(IsFlag("excused")),
                ),
            ),
        ),
        IsNotDone("samantha_event_D02"),
        IsDayOfWeek(6, 7),
        IsHour(14, 18),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home")),
        PersonTarget(samantha,
            Not(IsHidden()),
            IsFlag("knows_ryancheats"),
            IsFlag("cuck_ryan"),
            MinStat("love", 110),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/the_one.ogg",
    })

    Event(**{
    "name": "samantha_event_D02",
    "label": "samantha_event_D02",
    "duration": 2,
    "priority": 500,
    "conditions": [
        Or(
            IsDone("samantha_event_D01"),
            And(
                IsDone("samantha_event_B01"),
                PersonTarget(samantha,
                    Not(IsFlag("cuck_ryan")),
                    ),
                ),
        ),
        IsDayOfWeek(6, 7),
        IsHour(14, 18),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            HasStamina(),
            ),
        PersonTarget(samantha,
            IsFlag("cheatDelay", False),
            IsFlag("knows_ryancheats"),
            MinStat("love", 120),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/the_one.ogg",
    })

    Event(**{
    "name": "samantha_event_D03",
    "label": "samantha_event_D03",
    "duration": 2,
    "priority": 500,
    "conditions": [
        IsDone("samantha_event_D02"),
        IsDayOfWeek(6, 7),
        IsHour(14, 18),
        HeroTarget(
            IsGender("male"),
            Not(IsFlag("ryandead")),
            HasRoomTag("home"),
            HasStamina(),
            ),
        PersonTarget(samantha,
            IsFlag("cheatDelay", False),
            MinStat("love", 130),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/the_one.ogg",
    })

    Event(**{
    "name": "samantha_event_D05",
    "label": "samantha_event_D05",
    "duration": 2,
    "priority": 500,
    "conditions": [
        IsDone("samantha_event_D04"),
        IsNotDone("samantha_event_D05B"),
        IsDayOfWeek(6, 7),
        IsHour(14, 18),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            HasStamina(),
            ),
        PersonTarget(samantha,
            IsFlag("cheatDelay", False),
            IsFlag("natalie", False),
            MinStat("love", 140),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/the_one.ogg",
    })

    Event(**{
    "name": "samantha_event_D05B",
    "label": "samantha_event_D05B",
    "duration": 2,
    "priority": 500,
    "conditions": [
        IsDone("samantha_event_D04"),
        IsNotDone("samantha_event_D05"),
        IsDayOfWeek(6, 7),
        IsHour(14, 18),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            HasStamina(),
            ),
        PersonTarget(samantha,
            IsFlag("cheatDelay", False),
            IsFlag("natalie"),
            MinStat("love", 140),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/the_one.ogg",
    })

    Event(**{
    "name": "samantha_event_E01",
    "label": "samantha_event_E01",
    "duration": 1,
    "priority": 100,
    "conditions": [
        Or(
            And(
                IsDone("samantha_event_B03"),
                PersonTarget(samantha,
                    IsFlag("excused")
                    ),
                ),
            IsDone("samantha_event_D05"),
            IsDone("samantha_event_D05B"),
        ),
        IsHour(14, 15),
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(samantha,
            Not(IsPresent()),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            MinStat("love", 160),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/the_one.ogg",
    "quit": False,
    "clothes": "casual",
    })

    Event(**{
    "name": "samantha_meet_bree",
    "label": "samantha_meet_bree",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            MinDaysPlayed(20),
            HasRoomTag("pub"),),
        PersonTarget(samantha,
            Or(
                IsRoom("date_pub"),
                HasRoomTag("pub"),
                ),
            Not(IsHidden()),
            ),
        PersonTarget(bree,
            Or(
                IsRoom("date_pub"),
                HasRoomTag("pub"),
                ),
            Not(IsHidden()),
            ),
        Or(
            PersonTarget(samantha,
                IsPresent(),
                ),
            PersonTarget(bree,
                IsPresent(),
                ),
        ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "samantha_meet_sasha",
    "label": "samantha_meet_sasha",
    "conditions": [
        MinDaysPlayed(12),
        HeroTarget(
            IsActivity("None"),
            IsGender("male"),
            HasRoomTag("pub"),),
        PersonTarget(samantha,
            Or(
                IsRoom("date_pub"),
                HasRoomTag("pub"),
                ),
            Not(IsHidden()),
            ),
        PersonTarget(sasha,
            Or(
                IsRoom("date_pub"),
                HasRoomTag("pub"),
                ),
            Not(IsHidden()),
            ),
        Or(
            PersonTarget(samantha,
                IsPresent(),
                ),
            PersonTarget(sasha,
                IsPresent(),
                ),
        ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "samantha_chat_bree",
    "label": "samantha_chat_bree",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Or(
                IsRoom("date_pub"),
                HasRoomTag("pub"),
                ),
            IsFlag("samanthaknowsbree"),
            ),
        PersonTarget(samantha,
            Or(
                IsRoom("date_pub"),
                HasRoomTag("pub"),
                ),
            Not(IsHidden()),
            ),
        PersonTarget(bree,
            Or(
                IsRoom("date_pub"),
                HasRoomTag("pub"),
                ),
            Not(IsHidden()),
            ),
        Or(
            PersonTarget(samantha,
                IsPresent(),
                ),
            PersonTarget(bree,
                IsPresent(),
                ),
        ),
        ],
    "chances": 10,
    "do_once": False,
    "once_day": True,
    })



    Event(**{
    "name": "samantha_preg_talk",
    "label": "samantha_preg_talk",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsHour(19, 21),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        PersonTarget(samantha,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("tellpregnant", 1),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/the_one.ogg",
    })

    Event(**{
    "name": "samantha_babyshopping",
    "label": "samantha_babyshopping",
    "duration": 1,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("date_mall1")),
        PersonTarget(samantha,
            IsPresent(),
            Not(IsHidden()),
            MinCounter("pregnant", 10),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/the_one.ogg",
    })

    InteractEvent(**{
    "name": "samantha_waterpark_comment",
    "label": "samantha_waterpark_comment",
    "conditions": [
        HeroTarget(IsGender("male")),
        Not(InInventory("swimsuit")),
        PersonTarget(samantha,
            IsActive(),
            ),
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "samantha_pregnant_request",
    "label": "samantha_pregnant_request",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(samantha,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            IsFlag("status", "girlfriend"),
            MaxCounter("pregnant", 8),
            ),
        'game.days_played - samantha.flags.girlfriend_day >= 7',
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "samantha_forgot_money",
    "label": "samantha_forgot_money",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasRoomTag("pub"),),
        PersonTarget(samantha,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "chances": 5,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "samantha_buy_dress",
    "label": "samantha_buy_dress",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("clothesshop")),
        PersonTarget(samantha,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "chances": 5,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "samantha_kiss_me",
    "label": "samantha_kiss_me",
    "max_girls": 1,
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(samantha,
            IsPresent(),
            Not(IsHidden()),
            MinFlag("kiss", 1),
            MinStat("love", 150),
            ),
        ],
    "music": "music/roa_music/the_one.ogg",
    "chances": 20,
    "once_day": True,
    "do_once": False,
    "quit": False,
    })

    Event(**{
    "name": "samantha_asleep_bedroom2",
    "label": "samantha_asleep_bedroom2",
    "priority": 1500,
    "conditions": [
        HeroTarget(IsRoom("bedroom2")),
        PersonTarget(samantha,
            IsPresent(),
            Not(IsHidden()),
            IsActivity("sleep"),
            ),
        PersonTarget(bree,
            Not(IsPresent()),
            ),
        ],
    "do_once": False,
    "once_hour": False,
    })

    Event(**{
    "name": "samantha_asleep_bedroom3",
    "label": "samantha_asleep_bedroom3",
    "priority": 1500,
    "conditions": [
        HeroTarget(IsRoom("bedroom3")),
        PersonTarget(samantha,
            IsPresent(),
            IsActivity("sleep"),
            ),
        PersonTarget(sasha,
            Not(IsPresent()),
            ),
        ],
    "do_once": False,
    "once_hour": False,
    })

    Event(**{
    "name": "samantha_asleep_bedroom5",
    "label": "samantha_asleep_bedroom5",
    "priority": 1500,
    "conditions": [
        HeroTarget(IsRoom("bedroom5")),
        PersonTarget(samantha,
            IsPresent(),
            Not(IsHidden()),
            IsActivity("sleep"),
            ),
        PersonTarget(minami,
            Not(IsPresent()),
            ),
        ],
    "do_once": False,
    "once_hour": False,
    "music": "music/roa_music/new_days.ogg",
    })

    Event(**{
    "name": "samantha_booty_call",
    "label": "samantha_booty_call",
    "duration": 2,
    "priority": 500,
    "conditions": [
        Or(IsDone("samantha_event_D05"), IsDone("samantha_event_D05B")),
        IsTimeOfDay("afternoon", "evening"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            Not(OnDate()),
            IsActivity("None"),
            HasStamina(),
            ),
        PersonTarget(samantha,
            Not(IsActivity("sleep")),
            MinStat("love", 150),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/the_one.ogg",
    })


    Event(**{
    "name": "samantha_wedding_baby",
    "label": "samantha_wedding_baby",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("samantha_event_B01"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("mall_southside"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(samantha,
            Not(IsHidden()),
            Not(IsFlag("divorced")),
            Or(
                And(
                    Not(IsFlag("ryanpregnancydelay")), 
                                                       
                    IsDone("samantha_preg_talk_ryan"), 
                    MaxCounter("pregnant", 0)
                    ),
                MinCounter("pregnant", 50)
                ),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/the_one.ogg",
    })

    Event(**{
    "name": "samantha_preg_talk_ryan",
    "label": "samantha_preg_talk_ryan",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("samantha_event_B01"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            ),
        PersonTarget(samantha,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            Not(IsFlag("divorced")),
            And(
                Not(IsFlag("ryanpregnancydelay")),
                MaxStat("sexperience", 0),
                ),
            Not(IsFlag("post_wedding_baby_talk_delay")),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/the_one.ogg",
    })

    Event(**{
    "name": "samantha_side_event_01",
    "label": "samantha_side_event_01",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("samantha_event_B01"),
        Not(IsDone("samantha_event_E01")),
        IsHour(13, 18),
        HeroTarget(
            IsGender("male"),
            Not(IsFlag("ryandead")),
            Not(OnDate()),
            ),
        PersonTarget(samantha,
            Not(IsPresent()),
            Not(IsHidden()),
            IsFlag("engaged"),
            IsFlag("knows_ryancheats"),
            MinStat("love", 90),
            ),
        HasVehicle(motor=True),
        ],
    "chances": 15,
    "do_once": True,
    })

    Event(**{
    "name": "samantha_side_event_02",
    "label": "samantha_side_event_02",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("samantha_event_B01"),
        Not(IsDone("samantha_event_E01")),
        IsDayOfWeek("67"),
        IsTimeOfDay("evening"),
        HeroTarget(
            IsGender("male"),
            Not(IsFlag("ryandead")),
            Not(OnDate()),
            ),
        PersonTarget(samantha,
            Not(IsPresent()),
            Not(IsHidden()),
            IsFlag("engaged"),
            IsFlag("knows_ryancheats"),
            MinStat("love", 100),
            ),
        ],
    "chances": 15,
    "do_once": True,
    })

    InteractEvent(**{
    "name": "sam_murder_talk_bree",
    "label": "sam_murder_talk_bree",
    "do_once": True,
    "conditions": [
        PersonTarget(samantha,
            IsActive(),
            ),
        PersonTarget("kylie",
            IsFlag("killed", "bree")
            ),
        ],
    })

    Event(**{
    "name": "samantha_exclusive_cheated",
    "priority": 1000,
    "label": "samantha_exclusive_cheated",
    "conditions": [
        IsDone("samantha_event_A04"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("dateroom")),
        PersonTarget(samantha,
            Not(IsHidden()),
            IsFlag("girlfriend"),
            IsFlag("nonexclusive", False),
            ),
        "samantha.room == game.room.replace('date_', '')",
        ],
    "do_once": True,
    })


label samantha_preg_talk_ryan:
    "Did you ever have one of those moments when you really had to bite your tongue?"
    "When you had to smile and try to hide the fact that you're dying a little inside?"
    "Yeah, I know that sounds really dramatic, but we've all been there."
    "The worst is when someone just drops a revelation in a casual conversation."
    show samantha at center, zoomAt(1.25, (640, 900)) with dissolve
    "You're never ready for it, like right now, when Sam does that very thing to me..."
    samantha.say "Oh, yeah..."
    samantha.say "I can't believe I almost forgot to tell you, [hero.name]!"
    show samantha a happy
    samantha.say "Great news - Ryan and I, we're having a baby!"
    "It takes a moment for the words to fully sink in."
    "Time that I spend staring at Sam, my mouth hanging open."
    "Luckily for me, she seems to take this as nothing more than genuine surprise."
    show samantha a normal
    samantha.say "I know, I know..."
    samantha.say "It's crazy, isn't it?"
    show samantha a happy at center, zoomAt(1.0, (640, 900)), startle
    samantha.say "I'm going to be a mom!"
    "I finally manage to shake off the initial shock of the revelation."
    with hpunch
    "And I shake my head to regain control of my senses before answering."
    show samantha normal
    "Again, Sam seems to take this as me being floored by the news."
    "So she doesn't question my reaction, just waits patiently for me to answer."
    if not hero.flags.knows_ryancheats:
        "I have no idea whether or not Sam knows how I feel about her."
        "Even though I held a torch for her all the time we lived together."
        "Hell, I'm still holding that same torch right now!"
        "But none of that really matters, does it?"
        "If I never had the guts to tell her how I feel, that's my fault."
        "I can't let it get in the way of her living her life with Ryan."
        "And so I swallow my own feelings and put a smile on my face."
        mike.say "That's..."
        if samantha.flags.nickname == "cupcake":
            mike.say "That's great, Cupcake - fantastic news!"
        else:
            mike.say "That's great, Sam - fantastic news!"
        mike.say "I know that you'll make a great mom."
        show samantha happy
        "Sam's face breaks into a smile at this."
        "The exact kind of smile that makes my heart ache."
        samantha.say "Aw, thank you, [hero.name]!"
        samantha.say "And Ryan too?"
        samantha.say "You think he'll make a great dad, right?"
        "Sam keeps right on smiling as she asks me this."
        "But there's no way she can know how it's twisting a knife inside of me."
        if samantha.flags.nickname == "cupcake":
            mike.say "Yeah, Cupcake..."
        else:
            mike.say "Yeah, Sam..."
        mike.say "Of course he will!"
        mike.say "You're going to be a perfect little family unit!"
        "I somehow manage to keep the smile fixed on my face."
        "And Sam doesn't notice the strain it causes me to do so."
        show samantha normal
    else:
        menu:
            "Keep your mouth shut":
                "As if it wasn't bad enough to be holding a torch for Sam all this time."
                "And on top of that I'm keeping the secret that Ryan's a cheating scumbag."
                "Now I'm going to have to smile and pretend to be happy about this too!"
                "But I suppose that none of that stuff really matters."
                "I've already chosen to keep all of that to myself."
                "So what right do I have to dump it all onto Sam right now?"
                "It'd just be selfish of me to ruin her chances of being happy."
                "So I swallow my true feelings and put a smile on my face."
                mike.say "That's..."
                if samantha.flags.nickname == "cupcake":
                    mike.say "That's great, Cupcake - fantastic news!"
                else:
                    mike.say "That's great, Sam - fantastic news!"
                mike.say "I know that you'll make a great mom."
                show samantha happy
                "Sam's face breaks into a smile at this."
                "The exact kind of smile that makes my heart ache."
                samantha.say "Aw, thank you, [hero.name]!"
                samantha.say "And Ryan too?"
                samantha.say "You think he'll make a great dad, right?"
                "Sam keeps right on smiling as she asks me this."
                "But there's no way she can know how it's twisting a knife inside of me."
                "Part of me wants to tell her the truth."
                "To say that he's a scumbag that doesn't deserve her."
                "But I've already made my choice."
                if samantha.flags.nickname == "cupcake":
                    mike.say "Yeah, Cupcake..."
                else:
                    mike.say "Yeah, Sam..."
                mike.say "Of course he will!"
                mike.say "You're going to be a perfect little family unit!"
                "I somehow manage to keep the smile fixed on my face."
                "And Sam doesn't notice the strain it causes me to do so."
                hide samantha fade
            "Tell her about the cheating":
                "After all that I've seen and kept quiet about between Sam and Ryan."
                "I know that I should just smile and pretend to be happy about this too."
                "But somehow I start speaking before I know what I'm doing."
                "And then it's too late, everything just comes spilling out."
                if samantha.flags.nickname == "cupcake":
                    mike.say "I can't keep doing this, Cupcake!"
                else:
                    mike.say "I can't keep doing this, Sam!"
                mike.say "I can't keep covering for him!"
                show samantha surprised at center, zoomAt(1.0, (640, 900)), startle
                "Sam looks puzzled, shaking her head in confusion."
                samantha.say "Covering for who, [hero.name]?"
                samantha.say "Wh...what do you mean?"
                if samantha.flags.nickname == "cupcake":
                    mike.say "Ryan's cheating on you, Cupcake."
                else:
                    mike.say "Ryan's cheating on you, Sam."
                mike.say "He's been cheating on you all along!"
                show samantha at center, zoomAt(1.0, (640, 900)), startle
                "Sam keeps on shaking her head."
                "As if the mere motion will make what I just said untrue."
                samantha.say "He...he wouldn't do that to me!"
                samantha.say "Not after all we've been through."
                show samantha sad
                samantha.say "Why are you saying that, [hero.name]?"
                samantha.say "Are you jealous - is that it?"
                "Sam's right about how I feel."
                "But not about why I'm doing this."
                if samantha.flags.nickname == "cupcake":
                    mike.say "This isn't about me, Cupcake."
                else:
                    mike.say "This isn't about me, Sam."
                mike.say "It's about you."
                mike.say "And I guess it's about your baby too."
                samantha.say "But...why tell me this now, [hero.name]?"
                show samantha a
                samantha.say "Why wait until I was pregnant?"
                if samantha.flags.nickname == "cupcake":
                    mike.say "I don't know, Cupcake."
                else:
                    mike.say "I don't know, Sam."
                mike.say "Until now I kept quiet because I thought it'd be okay."
                mike.say "Maybe I thought you wouldn't believe me."
                mike.say "That you'd just think I was trying to break you up."
                mike.say "But now there's a kid involved..."
                mike.say "Well, that changes things, doesn't it?"
                "Sam falls silent at this, nodding slowly."
                "She seems to be pondering my words deeply."
                show samantha a cry
                "But then she finally looks me in the eye and speaks."
                samantha.say "I think I'd like to be alone now, [hero.name]."
                samantha.say "I need to think about what you've said."
                hide samantha
                show samantha a cry
                with dissolve
                "All I can do is nod in turn."
                hide samantha a with moveoutright
                "And then watch in silence as she walks away."
                $ samantha.flags.knows_ryancheats = True
                $ samantha.love -= 20
                $ samantha.flags.nokiss = False
    $ samantha.flags.ryanpregnancydelay = TemporaryFlag(True, 30)
    $ samantha.flags.NPCpregnancy = "ryan"
    return

label samantha_preg_talk:
    $ samantha.flags.tellpregnant = 2
    if Harem.find_by_name("home").is_member(samantha):
        "I'm just going about my daily routine when a soft voice interrupts my thoughts."
        samantha.say "Hey [hero.name], do you have a moment?"
        show samantha with dissolve
        "Turning to face her, I can't help but smile. Samantha always lights up my day, and I can't believe she agreed to move in with us."
        "In her hands, she's holding a small white box with the bakery logo printed on it's surface."
        "Opening my arms we meet in a soft embrace. I can hear her usually gentle heartbeat beating fast; much faster than usual."
        "Taking a step back from her, I gesture to the box she still holds."
    else:
        play sound door_knock
        "A knock on the front door gets my attention."
        queue sound door_knock
        "I want to ignore it and don't move for a few long seconds. But the knocking persists."
        mike.say "Alright, alright."
        scene bg black with dissolve
        scene bg house
        show samantha casual
        with wiperight
        "I reluctantly rise from my spot on the couch and head to the door. I flip the gold painted lock and come face to face with Samantha."
        if samantha.flags.nickname == "cupcake":
            mike.say "Cupcake?"
        else:
            mike.say "Sam?"
        "She stands on the porch with soft eyes and small, white box in her hands with the bakery logo."
        samantha.say "Hi! I'm sorry, I didn't tell you I was coming over, did I?"
        samantha.say "I got super caught up at work! Is this okay?"
        "She already knows what I'm going to say."
        mike.say "Yeah, sure. Come on in."
        "I stand aside and hold the door wider, letting her walk in. She seems a little nervous, clutching at her box tighter."
        scene bg livingroom
        show samantha casual
        with fade
    mike.say "What's that?"
    if not Harem.find_by_name("home").is_member(samantha):
        "I gesture to her box."
    samantha.say "Oh. Just something I made at work."
    samantha.say "It's for you!"
    if Harem.find_by_name("home").is_member(samantha):
        "Sam shoves the box at me, and quickly walks past."
    else:
        "Sam shoves the box at me after I shut the door. I fumble but take it from her."
    samantha.say "I'm going to get some water!"
    hide samantha with moveoutright
    "She exclaims before heading to the kitchen. This all seems... suspicious."
    "I start to follow behind her but slow as I open the lid. I come to a full stop."
    "Inside is a rather large cupcake, the top covered in two colours of icing- one half is pink and the other is blue. A white question mark is painted on the middle."
    mike.say "..."
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake?"
    else:
        mike.say "Sam?"
    scene bg kitchen
    show samantha casual blush
    with fade
    "I pick up the pace, getting to the kitchen. Sam is waiting at the counter, cheeks dusted red and waiting for me. On the surface in front of her is a long, white stick."
    mike.say "Are you...?"
    "I can't seem to form words. I know what's happening, I just can't seem to process it."
    samantha.say "[hero.name]... I'm pregnant!"
    "She taps a perfect nail on the pregnancy test and two little pink stripes stare back at me."
    mike.say "This is..."
    "I don't know what to say."
    menu:
        "Hug her":
            hide samantha
            show samantha casual close surprised
            $ samantha.love += 5
            "I rush forward and gather her into my arms. She seems surprised at first but melts into me."
            show samantha flirt
            samantha.say "... So you're okay with all this?"
            mike.say "Hell yes, I am."
            show samantha happy
            "Sam pulls away and the warmth is gone. But once I see her happy tears, the warmth blooms in my chest this time."
            samantha.say "You're going to be a great father, [hero.name]!"
            samantha.say "Thank you..."
            "She goes back into my arms and I hold her. A future children's book writer, baker, and beautiful girlfriend? She would be a great mother, too."
        "Back away":
            "Panic rises in my chest as soon as I get over the shock. My hands shake and I shift away from her."
            show samantha sad
            "Samantha's face visibly falls."
            samantha.say "[hero.name]?"
            mike.say "I- I'm sorry. Is this what you meant the other morning?"
            samantha.say "... Yeah, I just... maybe I should have told you then."
            "I set the cupcake down on the counter next to the positive pregnancy test."
            samantha.say "W-What's wrong?"
            mike.say "I just..."
            "I don't really know how to word this."
            mike.say "I don't really think we're ready for this."
            "Samantha seems sad but has a spark of understanding in her eyes. Her mouth twitches as she struggles for a response."
            samantha.say "Maybe... but we can become ready for it. I'm willing to try."
            mike.say "What if it doesn't work out?"
            hide samantha
            show samantha casual close normal
            "Samantha steps forward and takes my hand, gripping it tightly. Her fingers are warm."
            samantha.say "I won't let it not work out. If we're both willing to try, we can do anything."
            "I look down, but she doesn't let my eyes reach the floor."
            samantha.say "Please? Try for me. I promise everything will be okay."
            "I stare back at the sloppy cupcake on the counter. Globs of icing hang off the side and the question mark is shaky. She must have really been worried about coming to me with this."
            mike.say "Alright. Let's do it. We can do it."
            show samantha happy
            "Sam's face lights up with joy. She lurches forward and wraps her arms around my neck. I catch her, squeezing her back."
        "Tell her it's probably Ryan's":
            mike.say "Are you sure it's not Ryan's?"
            show samantha surprised
            samantha.say "[hero.name]!"
            samantha.say "You fucking jerk!"
            mike.say "I think you should leave..."
            mike.say "I am pretty sure it's not mine."
            show samantha sad
            samantha.say "I never thought you would do that..."
            show samantha angry
            samantha.say "I never want to see you again!"
            $ samantha.set_gone_forever()
    scene bg black with dissolve
    return

label samantha_wedding_baby:
    if samantha.flags.NPCpregnancy == "ryan" or samantha.sexperience <= 0:
        $ mike_pregnancy = False
    else:
        if persistent.pregnancy_end:
            $ samantha.flags.mikeBabies += 1
        $ mike_pregnancy = True
    if persistent.pregnancy_end:
        $ samantha.unpreg()
    "I know that I came to the mall for something, that there was something I needed from here."
    "And I'm pretty sure that I was headed straight for the store that sells it too."
    "But all thought of such things vanishes from my head as soon as I hear a familiar voice."
    ryan.say "Hey there, buddy!"
    ryan.say "Over here!"
    "My head spins around at the sound of Ryan's voice, my eyes searching for him."
    "But at the same time, part of me is hoping and praying that he's alone."
    "That, like me, he just happened to be at the mall on his own to pick something up."
    show samantha a happy zorder 2 at right5
    show ryan casual smile zorder 1 at left4
    with dissolve
    samantha.say "Hey, [hero.name]."
    samantha.say "Fancy seeing you here..."
    show samantha a normal
    "Damn it!"
    "Why did she have to be with him?"
    "Why does it always have to feel like Ryan's rubbing my face in his happiness?"
    "Isn't it enough that he got the girl and he's getting away with cheating on her too?"
    if samantha.sexperience:
        "Well...Sam is cheating on him with me too."
        "So I guess that does balance things out a little."
    "I do the best I can to force a genuine smile onto my face."
    "I just hope that it's convincing enough."
    mike.say "Hey, Ryan!"
    if samantha.flags.nickname == "cupcake":
        mike.say "Hey, Cupcake!"
    else:
        mike.say "Hey, Sam!"
    mike.say "How in the hell are you guys doing?"
    show ryan annoyed
    "Ryan frowns at me and shakes his head."
    "Then he looks down at what's in front of them."
    ryan.say "Aren't you going to say hi to the new arrival?"
    ryan.say "I'm sure little Annika here is keen to meet her uncle [hero.name]!"
    "I look down and see that there's a baby stroller in front of Sam and Ryan."
    "How in the hell could I have missed that?!?"
    "And sure enough, there's a gurgling infant in there too!"
    mike.say "That's..."
    mike.say "That's a baby!"
    ryan.say "Wow!"
    ryan.say "There are no flies on you, [hero.name]!"
    if samantha.flags.tellpregnant == 2 or "samantha_preg_talk_ryan" in DONE:
        samantha.say "You sound surprised."
        samantha.say "Didn't we tell you we were pregnant?"
    if samantha.flags.tellpregnant == 2:
        "Sam underlines the question with a meaningful stare."
        "Of course she told me that she was pregnant."
        "How could I have missed it when I've seen her naked so many times in recent weeks?"
        "It's just the shock of actually seeing the kid in the flesh for the first time!"
    if samantha.flags.tellpregnant == 2 or "samantha_preg_talk_ryan" in DONE:
        if samantha.flags.nickname == "cupcake":
            mike.say "Of course you did, Cupcake!"
        else:
            mike.say "Of course you did, Sam!"
        mike.say "I...I just have a lot on my mind right now, that's all."
    mike.say "Congratulations...both of you!"
    show ryan smile
    "Ryan beams like he always does, behaving like all the praise is for him alone."
    "But Sam looks more downbeat, and her smile seems like it's a little forced."
    "I mean, obviously she's going to be exhausted from the act of giving birth."
    "Yet there's still something more to it than that."
    "Most new mothers are practically radiant and full of joy."
    "Sam looks like she hasn't slept in a month and she's depressed to boot."
    if samantha.flags.nickname == "cupcake":
        mike.say "Are you okay, Cupcake?"
    else:
        mike.say "Are you okay, Sam?"
    mike.say "You look pretty beat!"
    show samantha at right5, startle
    samantha.say "Oh, you know how it is..."
    show ryan annoyed
    show samantha annoyed
    samantha.say "Feeding in the middle of the night..."
    samantha.say "Crying at random for hours on end..."
    show samantha normal
    ryan.say "And that's just Sam here!"
    show ryan smile at left4, startle
    show samantha annoyed
    "As Ryan bursts into laughter at his own joke, I press Sam further."
    if samantha.flags.nickname == "cupcake":
        mike.say "Seriously, Cupcake..."
    else:
        mike.say "Seriously, Sam..."
    mike.say "Are you okay?"
    show ryan annoyed
    samantha.say "I...I'll be fine, [hero.name]."
    samantha.say "It's just adjusting to being a mom...that's all!"
    if samantha.sexperience:
        show samantha normal at center, zoomAt(1.15, (740, 800))
        "Sam leans in closer, making sure that Ryan can't hear her."
        samantha.say "We'll talk first chance we get, okay?"
        hide samantha
        show samantha at right5
    if mike_pregnancy:
        "About how this affects us - and about Annika's daddy!"
    show samantha normal
    "Sam forces another weak smile onto her face."
    "But then the baby begins to wail."
    "That sound focuses Sam's attention like a laser."
    "And suddenly the kid's the only thing she has time for."
    show ryan smile at left4, startle
    ryan.say "Oops!"
    ryan.say "Looks like duty calls!"
    show ryan at left5 with move
    ryan.say "See you around, [hero.name]!"
    "I nod and smile almost as weakly as Sam."
    hide samantha
    hide ryan
    with moveoutleft
    "And I watch as she and Ryan hurry off to do whatever it is that new parents do."
    "Well, at least I don't have to find out the gory details just yet!"
    if mike_pregnancy:
        "But what did Sam mean when she said that just now?"
        "Surely she knows who the father is?"
        "And that's Ryan - right?!?"
    "Now, if only I could remember what I came here for in the first place..."
    return

label samantha_booty_call:
    "The expression on my face is usually pretty blase and uninterested whenever I pick up my phone and force myself to see what tiresome person in on the other end of the line this time."
    "Inevitably it's always someone that I can't stand, or some arsehole that wants to take advantage of me and dress it up as doing them a favour."
    "But on this occasion, as soon as I see the name of the calling, I go scrambling for my phone as though it were news of a massive win on the lottery."
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Samantha")
    if not result:
        $ hero.cancel_event()
        $ samantha.love -= 5
        return
    if samantha.flags.nickname == "cupcake":
        mike.say "Hey, Cupcake - great to hear from you!"
    else:
        mike.say "Hey, Sam - great to hear from you!"
    "By the way, if you think I sound pretty shallow right about now, you're welcome to your opinion."
    "But Sam's pretty much the closest thing to an actual lottery win in my life right about now!"
    samantha.say "Hey, [hero.name]...what are you doing right now?"
    "From the pause and the tone of her voice, I'd say that was a rather loaded question."
    "Intrigued by the possibilities of what Sam might be building up to asking me, I decide to play along."
    mike.say "Oh, you know, the usual - a whole lot of nothing."
    mike.say "Why do you ask?"
    "I hear Sam chuckle on the other end of the line, which for me is like hearing the sound of birds singing in the trees on a summer's day."
    samantha.say "Well, I was wondering if I could come over to your place?"
    samantha.say "That way you could do a whole lot of nothing with company."
    samantha.say "Or we could do a whole lot of something else instead..."
    "Like I need any more encouragement than that!"
    mike.say "O...okay, I'll stay right there!"
    samantha.say "That's great - see you real soon..."
    "As soon as the call ends and before I rush to clean up a little, I actually take a moment to stop and pinch myself as hard as I can."
    "Nope, I'm not asleep and dreaming after all."
    "I did just get what I'm pretty sure amounts to a genuine, bona fide booty call."
    "And what's even more amazing is that it was from Sam!"
    play sound door_bell
    "Some moments later, the sound of the doorbell pulls me out of my thoughts. She's there."
    "I force myself to take a moment and perform a quick check-list before opening the door."
    "No matter how eager I might be to see her, there's no sense in Sam knowing that I'm a desperate, sweaty mess."
    "Even if that's just what I feel like right now..."
    "Okay, I'm not covered in anything unpleasant."
    "I don't smell either - well, at least not in a bad way."
    "And last of all, a quick glance down confirms that I have managed to remember to actually wear clothes."
    "All present and pretty much correct."
    "So there should be nothing to prevent me from being perfectly pleasant and charming company for Sam."
    "Feeling a corresponding boost in my sense of confidence, I reach out the door knob..."
    scene bg house
    show samantha wedding normal
    with wiperight
    "Standing there, in the open doorway, decked out from head to toe in the purest white, is Sam."
    "Now that might not have been as issue at all, if only the white didn't happen to be that of the dress that she got married in."
    "In an instant, with the perfect reminder of how she looked on her wedding day before me, every emotion that I felt on that occasion comes flooding back."
    "Sam's even wearing the same veil she had on the day and holding a bouquet in her tightly clasped hands."
    "At the sight of my mouth hanging open in such obvious surprise and awe, a slow smile begins to spread across Sam's face."
    samantha.say "I take it you remember the last time you saw me in this little number?"
    "I can only nod in response, still too staggered to speak."
    samantha.say "They say that a bride's supposed to be the most beautiful woman present at her wedding."
    samantha.say "That all eyes are supposed to be on her and she should be the sole object of desire."
    "As she recounts these wedding traditions, Sam's face darkens visibly, as if covered by a shadow of memory."
    show samantha sad
    samantha.say "But that wasn't the case for me - was it, [hero.name]?"
    "I shake my head, not wanting to get into the gruesome details of what Ryan did to her before and immediately after the ceremony."
    samantha.say "No, it wasn't."
    samantha.say "The one man that should have had eyes only for me was cheating on me with some little slut."
    samantha.say "Do you know how that feels, [hero.name]?"
    samantha.say "Can you begin to imagine what it's like to wonder if he was thinking about her while we were standing at the altar?!?"
    "Finally, I manage to utter a couple of words in response."
    if samantha.flags.nickname == "cupcake":
        mike.say "No, Cupcake...I can't."
    else:
        mike.say "No, Sam...I can't."
    show samantha normal
    "As if cheered to hear the sound of my voice, Sam's expression becomes open and pleasant once again."
    samantha.say "But I do take heart from the fact that there was someone there that was thinking of me in that way."
    samantha.say "Be honest, [hero.name]...when you saw me in this dress, you wanted to fuck me pretty badly, didn't you?"
    show samantha flirt
    "The frank nature of the question makes me gulp and gasp for breath as Sam puts me on the spot."
    "What can I say to that?"
    "One thing that I certainly can't do is lie!"
    if samantha.flags.nickname == "cupcake":
        mike.say "Y...yes, Cupcake."
    else:
        mike.say "Y...yes, Sam."
    mike.say "You looked so beautiful - just like you do now."
    mike.say "I'd be lying if I said that I didn't want you..."
    "Sam narrows her eyes for a second."
    show samantha normal
    samantha.say "And by 'wanted', you mean 'wanted to fuck' - am I right?"
    "I have no idea why she's being so pedantic about this point, but I feel the need to play along all the same."
    if samantha.flags.nickname == "cupcake":
        mike.say "Yes, Cupcake - that's what I meant."
    else:
        mike.say "Yes, Sam - that's what I meant."
    samantha.say "Good, because that's exactly what I'm giving you the chance to do, [hero.name]."
    show samantha flirt
    samantha.say "We're going to roll back the clock and you're going to fuck me, just like you wanted to do on my wedding day."
    "While this all sounding pretty weird and intense, almost like I'm being dragged into making a revenge porn, it's still Sam offering herself up to me on a platter."
    "It's not as though her asking me to have sex with her in a particularly kinky manner is going to put me off taking her up on the offer."
    "I nod with genuine enthusiasm and make a step back to let her walk in through the open front-door, but Sam stops before entering the living room."
    show samantha normal
    samantha.say "But there's just one condition."
    "Ah, here it comes..."
    samantha.say "I want you to make me feel like the dirty little slut, not the pure and pristine bride!"
    mike.say "Oh...okay, Sam...if you say so."
    samantha.say "I want to show that cheating prick that I'm a woman too, that I can be every bit as much of a filthy whore."
    mike.say "If that's what you want, then I'll do my best..."
    "With all that said, Sam walks in the house."
    scene bg livingroom
    show samantha wedding normal
    with fade
    "Although I've seldom seen this side of her normally sweet and gentle personality, I have to admit that she's seriously turning me on right now."
    "It seems that the flip-side of that pleasant persona is pretty wild and outrageous, almost as if she were compensating for something or releasing her pent up frustration all at once."
    scene bg bedroom1
    show samantha wedding normal
    with fade
    "Sam simply pounces on me the moment that she's led me to my bedroom and closed the door behind us."
    "Tossing the bouquet aside and almost tearing the veil off of her head, she literally wraps her legs around me so that I have to hold her up."
    hide samantha
    show samantha kiss wedding mc_casual
    with dissolve
    $ samantha.flags.kiss += 1
    "In the moments when she's not forcing her tongue into my mouth, I catch glimpses of her white stockings beneath the bunched up skirts of her dress."
    "I can remember catching the briefest glimpse of those same tights as she walked down the aisle."
    "And so to have them wrapped around me like this really does feel like a fantasy brought to life."
    "Still carrying all of Sam's weight, I stagger towards the bed in the hope of depositing her there."
    "Feeling the edge of it against my knees, I let myself fall forwards and onto it, sure that she won't let go even if I ask nicely."
    "We land on the bed without any kind of injury, but the surprise of the fall has the desired effect of breaking Sam's grip on me."
    hide samantha kiss
    show samantha wedding normal
    with dissolve
    "Well, she was the one that said she wanted to be treated like a slut."
    "So here goes nothing..."
    "I stand up and turn to face her, giving her a gentle but firm shove back onto the bed when she tries to follow."
    mike.say "Get over here and put your mouth to good use."
    "I can see Sam's large eyes widen yet further as I point at her and then to my groin."
    show samantha surprised
    mike.say "Well, what are you waiting for - it's not going to suck itself, is it?"
    "For a moment I'm worried that I've gone to far, that she'll call a halt to this whole thing and slap the taste out of my mouth."
    "But instead she begins to nod almost frantically, as if remembering that she was the one that asked to be treated in such a manner."
    show samantha bj2 with fade
    "A second later she crawls eagerly forwards and begins to fumble with my flies, almost desperate to obey my demands."
    "There's no surprise that Sam finds my dick already standing to attention and more then ready for her when she pulls it out."
    "And yet there's still a big part of me that's not totally comfortable with the idea of treating her like this."
    "But I try my best to push those those concerns aside, and concentrate on what she's about to do instead."
    "For her own part, now that she seems to be well into playing the part, Sam doesn't hesitate for even a moment."
    "Licking her lips in anticipation, she sticks out her tongue and wraps it around the head of my cock."
    "And from there she opens her mouth wide enough to start taking as much as she can possibly manage inside."
    "There's no delicate building of intensity here, and no pretence of being either shy or demure."
    show samantha bj2 suck
    "Determined to behave like a completely hopeless slut, Sam sucks on my cock with no sense of shame whatsoever."
    "At the same time, she moans and even begins to drool a little as her mouth is filled almost to the point of bursting."
    "Once Sam has my cock as deep as she can take it, she begins to bob her head back and forth."
    "At the same time she circles the finger and thumb around the base, working the shaft with that as well."
    show samantha bj2 open2
    "The whole time she's doing this, Sam is looking up at me and holding my eye."
    "It's as though she wants desperately for me to see her degrade herself for my benefit, to be aware of just how much this is costing her in terms of her dignity."
    show samantha bj2
    "By now, the drool is seeping out of the sides of Sam's mouth and dripping from her chin."
    "And yet she shows no sign of either wiping it away or stopping any time soon."
    "I could cum at any moment, but I somehow feel that, as humiliating as this is, it's still not enough to satisfy her."
    hide samantha bj2
    show samantha wedding flirt blush
    with fade
    "Pulling my cock out of Sam's mouth with an audible popping sound, I put a hand on her shoulder and again push her back onto the bed."
    "Only this time I don't give her the chance to recover her balance or ask what I want of her."
    "As she lays sprawled on her back, I climb up onto the bed and roughly remove her dress to reveal what's beneath."
    show samantha naked
    "Surprisingly, there's no sign of pieces of fabric between me and her naked body."
    mike.say "I see that you came here with a specific idea."
    show samantha flirt blush
    mike.say "Turn over, and get on your hands and knees - NOW!"
    "I have no idea if Sam's playing the part of the cheap whore so well because she's that into it."
    "Or else I'm putting on a good enough performance to convince her that I actually mean what I'm saying."
    "Either way, she drags herself backwards up the bed, panting as she goes."
    "Aware of what she's been ordered to do next, Sam struggles to get onto her hands and knees."
    show samantha doggy nomike smile with fade
    "All the while she keeps glancing back over her shoulder at me, eyes full of apprehension and barely concealed interest in just what I have in mind."
    "Kneeling behind her, I grasp her around the waist and pull her against me, grinding myself into her backside."
    mike.say "Oh-ho...you should see the state of your pussy right now."
    mike.say "It's dripping like a fucked up fridge!"
    show samantha doggy -nomike out
    "I reach out and run a finger around the outside of Sam's lips, feeling her quiver with suppressed desire as I do so."
    mike.say "But you're not getting what you want tonight, you horny little bitch."
    mike.say "Tonight's all about me using you up, like a rubber."
    mike.say "It's about me having my fun and then tossing you away, like the trash that you really are!"
    "I have no idea if I'm going too far by now, but I know that it's too late for me to stop now."
    "Without as much as a single word of warning, I pull Sam's buttocks apart and begin to push the head of my cock into her exposed anus."
    show samantha doggy anal
    "The cry that she lets out now is too high-pitched and full of shock to be anything other than genuine."
    show samantha doggy scream closed
    "Fearing that she might try to call the whole thing off at any second, I twist my left hand into her hair and yank her head back sharply."
    "Sam instantly leans backwards, hoping to alleviate the pain she's feeling."
    show samantha doggy scream wink
    "And then I reward her efforts by using that motion to force my cock yet further into her."
    mike.say "How does it feel, huh?"
    mike.say "To have a cock shoved up your ass?"
    mike.say "And all the while, your poor little pussy is weeping away for want of it!"
    "Sam yelps with each and every thrust, the sound turning me on immensely."
    "As much as do I love the feel of my cock being up her tight backside, I'm not sure if it's truly that or the constant cries that's turning me on more..."
    show samantha doggy smile closed
    "She seems more like an animal now, broken down to the point where all that she has left is the most base of sensual responses."
    "I can't help wondering if this is what breaking an elegant and beautiful horse must feel like."
    "Taking something pure and almost perfect in it's apparent innocence, and the bending it to your will until its own is truly broken."
    "I find the thought disturbing and arousing in almost equal measures."
    "Or perhaps slightly more of the latter, as I can soon feel the urge to cum mounting inside of me."
    "Almost as harshly as I forced my cock into Sam's ass, I yank it out again, making her scream almost as loudly as she did when it was up there."
    show samantha doggy out smile closed
    mike.say "I'm not cumming inside of you, bitch."
    mike.say "I wouldn't cum in either of your holes, not if my life depended on it."
    mike.say "The best you deserve from me is a shot in the damn face."
    mike.say "So get up and take it - NOW!"
    "Sam hurries to obey, practically crouching before me like a beaten dog."
    show samantha bj with fade
    "She reaches out gingerly, taking my cock in her hands."
    show samantha bj suck
    "Still slick from her own ass, it nevertheless finds its way back into her mouth as she meekly finishes me off."
    "But true to her orders, Sam pulls it out the second before I cum, allowing the whole thing to spatter over her face."
    show samantha bj -suck cumshot with vpunch
    "By the time I'm truly done, she's a sweating, panting mess."
    show samantha bj cumface with vpunch
    "Her hair is a tangled mass, her make-up smeared with cum and spread crazily here and there."
    hide samantha bj
    show samantha naked flirt blush cum
    with fade
    "Panting and with a glazed expression, she reaches for her phone and snaps a selfie of the whole glorious ruin that she's become."
    show samantha selfie cum with fade
    "But perhaps the true crowning glory of the picture is the fact that my cock is still half hanging out of her mouth as she snaps it."
    "I fall back onto the bed, watching Sam's actions with a mixture of horror and genuine admiration."
    "From the wicked smile that grows on her face as she starts to send a message, I can guess just who that selfie is intended for."
    "And I'd like to be able to say that I feel a modicum of sympathy for him."
    "But the cold, honest truth is that I really don't."
    $ samantha.sexperience += 1
    $ samantha.love += 2
    $ samantha.sub += 2
    return

label samantha_asleep_bedroom2:
    show multisleep breesam samantha
    "Samantha is sleeping, I should leave before I wake her up..."
    $ game.room = "secondfloor"
    return

label samantha_asleep_bedroom3:
    show multisleep sashasam samantha
    "Samantha is sleeping, I should leave before I wake her up..."
    $ game.room = "secondfloor"
    return

label samantha_asleep_bedroom5:
    show multisleep minamisam samantha
    "Samantha is sleeping, I should leave before I wake her up..."
    $ game.room = "secondfloor"
    return

label sam_murder_talk_sasha:
    "As you can imagine, the atmosphere around the house has been pretty strained since it happened."
    "And the fact that I'm calling the incident 'it' pretty much lets you know that it's bad."
    "I mean, how can you even begin to process the fact that someone broke into your house and raped you?"
    "That and worse, that she actually topped it all off by literally killing one of your housemates too?"
    "It takes me the first few days just to be able to think of Kylie without breaking into a cold sweat."
    "And even when I can manage that, I keep on seeing the whole thing playing out, over and again."
    "When I close my eyes, all I can see is the image of what happened to poor Sasha."
    "It's vivid and stark, like the scene is etched into my mind and I'll never be able to forget it."
    "I'm so wrapped up in my own mental trauma that I almost don't notice the others are avoiding me."
    "At first I just assume that everyone's feeling the same, that they need their mental space."
    "But soon enough I start to become worried that there's more to it than that."
    "Could they actually be avoiding me because I was the one that knew Kylie?"
    "Am I tainted by association with that crazy bitch?"
    "In the end, I decide to just up and ask."
    "I figure that either way, it's better to know the truth."
    "And I hope that Sam, the one that I've known the longest, will be straight up and honest with me."
    show samantha sad with dissolve
    mike.say "Ah..."
    if samantha.flags.nickname == "cupcake":
        mike.say "Hey, Cupcake!"
    else:
        mike.say "Hey, Sam!"
    show samantha surprised
    "Sam stops in her tracks, looking a little surprised to see me."
    "But she recovers quickly, hiding whatever she's feeling behind a mask of sympathy."
    show samantha normal
    samantha.say "Oh, hey, [hero.name]."
    samantha.say "How are you holding up?"
    "All I can do is shrug and let out a sigh."
    "The truth is that I'm not doing great - who would after what happened?"
    "But I still don't want to wallow in self-pity or be smothered with someone else's sympathy."
    "So I tell a lie, only a small one, just to move the conversation on."
    mike.say "Better than I did on the day it happened."
    if samantha.flags.nickname == "cupcake":
        mike.say "How about you, Cupcake?"
    else:
        mike.say "How about you, Sam?"
    show samantha surprised
    "I can see that the question catches Sam out, putting her on the backfoot."
    "Maybe she expected the whole conversation to be about me, rather than the both of us."
    samantha.say "I...I'm okay, [hero.name]."
    samantha.say "After all, that crazy girl didn't hurt me - did she?"
    "I want to be subtle about this, but I can't keep from stating the obvious."
    mike.say "The crazy girl that I was involved with?"
    show samantha sad
    samantha.say "I...I didn't mean it like that, [hero.name]."
    if samantha.flags.nickname == "cupcake":
        mike.say "But it's true, Cupcake - I'm the one that brought Kylie here."
    else:
        mike.say "But it's true, Sam - I'm the one that brought Kylie here."
    mike.say "If it weren't for me, Sasha would still be alive."
    samantha.say "Come on, [hero.name] - you can't believe that?!?"
    samantha.say "I thought that it was...that it might be my fault!"
    show samantha close
    "Now the roles are suddenly reversed, as I find myself baffled by Sam's confession."
    "I shake my head, trying to dismiss what she just said almost the moment I hear it."
    if samantha.flags.nickname == "cupcake":
        mike.say "What do you mean, Cupcake?!?"
    else:
        mike.say "What do you mean, Sam?!?"
    mike.say "That's just crazy!"
    samantha.say "Really, [hero.name]?"
    samantha.say "How is it any more crazy than you trying to take the blame for what a psycho did?"
    mike.say "Oh yeah..."
    if samantha.flags.nickname == "cupcake":
        mike.say "Point taken, Cupcake."
    else:
        mike.say "Point taken, Sam."
    samantha.say "Yeah, well..."
    samantha.say "With me it was thinking that my moving back in here was bad luck."
    samantha.say "Like I'd come back to the place where it started to go wrong with Ryan and me."
    samantha.say "But it wasn't - it was just a crazy girl doing what her crazy brain told her to do."
    samantha.say "You just had the misfortune to be the guy she fixated on, [hero.name]."
    samantha.say "And Sasha was in the wrong place at the wrong time."
    samantha.say "It sucks and it's not fair, but you're not right to blame yourself."
    if samantha.flags.nickname == "cupcake":
        mike.say "It still hurts, Cupcake."
    else:
        mike.say "It still hurts, Sam."
    samantha.say "I know, [hero.name]."
    samantha.say "But that's because it's supposed to."
    samantha.say "All the guilt and pain you're feeling - that's the proof your not insane."
    show samantha normal
    samantha.say "It's proof that you're not like her."
    "I feel Sam squeezing my hand tighter as she says this, holding my eye the whole time."
    "Knowing that she's there for me does make me feel better, more confident for the future."
    "I squeeze her hand in return, nodding to show that her words have had the desired effect."
    show samantha sad
    samantha.say "I feel like I never had the chance to get to know Sasha."
    samantha.say "Not properly, at least."
    show samantha normal
    samantha.say "I think I'd like you to tell me all about her, [hero.name]."
    "I nod again, beginning to warm to the idea."
    "And then I can't help laughing just a little."
    "As I can think of the perfect stories to tell Sam."
    "And I just know that they'll have her laughing too."
    return

label sam_murder_talk_bree:
    "I know that I shouldn't be trying to hide away from the reality of what happened the other night."
    "There's no way that it's healthy to take something like that and shove it down inside my guts."
    "But that's the problem when it's a thing that's happened to you and not someone else."
    "All the advice that you hear about dealing with stuff, it doesn't help at all when it's you."
    "You're too busy trying to deal with what was done to you to be able to step back and think straight."
    "I suppose I started avoiding the others around the house without even realising it."
    "Every time I heard voices I'd turn and head in the opposite direction."
    "Every time I was about to enter a room and heard the same, I'd walk past the door."
    "In the end it's Sam that finally corners me."
    "The look on her face is gentle and sympathetic."
    "But I can tell from her body-language that she's not going to be put off."
    show samantha sad
    samantha.say "Hey, [hero.name]!"
    samantha.say "Where'd you think you're going?"
    "The question catches me completely off guard."
    "I stop dead, turning to face Sam as she walks up to me."
    mike.say "Huh..."
    mike.say "Wha...what's that?"
    mike.say "I wasn't going anywhere!"
    show samantha normal
    "I know the smile that's spreading across Sam's face right now."
    "I've seen it before, when she's amused by something."
    "Specifically something that she doesn't believe in the slightest."
    samantha.say "Quit with the bullshit, [hero.name]."
    samantha.say "You've been avoiding everyone for days now!"
    samantha.say "But I'm not leaving you alone until I get a word out of you."
    "I shrug, trying as best I can to brush Sam's concern aside like nothing's amiss."
    if samantha.flags.nickname == "cupcake":
        mike.say "Ah, I'm okay, Cupcake."
    else:
        mike.say "Ah, I'm okay, Sam."
    mike.say "You know me - I'm tougher than I look!"
    samantha.say "Again with the bullshit!"
    show samantha sad
    samantha.say "That madwoman hurt you, [hero.name]."
    samantha.say "She killed poor [bree.name] in front of you!"
    if samantha.flags.nickname == "cupcake":
        mike.say "I'm okay, Cupcake - really!"
    else:
        mike.say "I'm okay, Sam - really!"
    "Sam nods at this, but I can see that she's far from convinced."
    samantha.say "So you're that special kind of 'okay', right?"
    samantha.say "The kind that's not really okay, but doesn't want to talk about it?"
    "I can't help letting out a rueful chuckle and nodding."
    "And I can see that the admission has gone some way to satisfying Sam too."
    show samantha normal
    samantha.say "That's fine, [hero.name]."
    samantha.say "Because I'm that same kind of okay too!"
    show samantha close
    "Sam reaches out, and I feel her take hold of my hand."
    "She squeezes it tightly, and the sensation feels instantly reassuring."
    show samantha sad
    samantha.say "You know, when I moved back in here, I expected less drama!"
    samantha.say "Oh god - I can't believe what happened to poor [bree.name]."
    samantha.say "I feel like I hardly got to know her at all!"
    show samantha normal
    mike.say "She was always full of life, a real ray of sunshine."
    mike.say "Maybe the best way we can remember her is to live life to the full?"
    "Sam nods, a sad smile on her face as she does so."
    "She leans her head on my shoulder and wraps her arms around me."
    "And as I hold her the same way, I realise that my mood has changed."
    "For the first time since it happened, I don't feel scared or depressed."
    "I'm actually able to think of what the future might hold for us all."
    return

label samantha_waterpark_comment:
    show samantha a
    "Did you ever have that problem where you really want to pay attention to what a girl's saying and give her an intelligent reply?"
    "But the trouble is that she's got that ability to turn you into a helpless mass of quivering hormones whenever she's near?"
    "So rather than sounding like a guy that's in control and worth taking a chance on, you sound like a hopeless, drooling moron?"
    "If you just said no, then screw you!"
    "But if you said yes, then you pretty much get the power that Sam has over me."
    "It's not like she has to say anything even vaguely flirty or suggestive either."
    "Just a casual comment that should be nothing more than small-talk can set me off."
    samantha.say "Ooh, I meant to tell you this before, [hero.name]."
    samantha.say "But did you see that there's a really great water-park just around the corner from here?"
    samantha.say "I was thinking that we should check it out sometime - but you'd need to buy a swimsuit first!"
    "And there she goes again - right there!"
    "All she's done is suggest that we go to a water-park, a place where people go to have clean, wholesome fun."
    "But all I can imagine are images of her running into the water, laughing and trying to keep from being soaked as she does so."
    "I have no idea what kind of a swimsuit Sam might own herself, and so my imagination just fills in the blanks."
    scene expression f"bg {game.room}" at blur(16), dark
    show samantha b happy swimsuit at center, blur(5)
    with dissolve
    "Of course the picture that forms in my mind is hardly going to be that of a conservative one-piece in black."
    "So instead I imagine her wearing the kind of bikini that's more straps than actual material."
    "I suppose it's ironic that my imagination would put her in something that you could say leaves nothing to the imagination!"
    "In my mind's eye, I see Sam giggling and then letting out a laugh that's almost a scream and I splash her mercilessly."
    "She puts up her hands to shield herself, but still ends up getting soaked from head to toe all the same."
    "The water makes the scant material of her bikini cling to her body all the more."
    "And her hair falls around her face in curling tendrils."
    "She's panting a little from the excitement of being chased into the water, her mouth open in an unconscious smile."
    "As I get closer to her, I swear that I can actually hear the sound of her heart beating at my approach..."
    scene expression f"bg {game.room}"
    show samantha a surprised at center, zoomAt(1.5, (640, 1040))
    with hpunch
    samantha.say "Hello - earth to [hero.name]!"
    "Sam waves a hand before my eyes, causing me to snap back to reality."
    "The vision of her, soaking wet and clad only in a bikini vanishes instantly."
    "But the effect that it had on me in those few brief moments does not disappear as easily."
    samantha.say "Are you okay?"
    samantha.say "It looked like you zoned out for a minute back there?"
    mike.say "Huh...oh, no...I'm okay."
    mike.say "And we should, definitely!"
    show samantha happy
    "Sam gives me a puzzled smile, cocking her head on one side."
    samantha.say "We should what, exactly?"
    show samantha normal
    mike.say "Go to the water-park...we really should go to that water-park you mentioned."
    "Sam nods her head at this, clearly delighted to have me agree to her idea."
    samantha.say "That's great - but you still need to buy a swimsuit!"
    if samantha.love >= 50:
        show samantha a flirt at center, zoomAt(1.85, (640, 1240))
        "She leans in close and winks, in a conspiratorial manner."
        samantha.say "You weren't thinking of getting some budgie-smugglers, were you?"
        samantha.say "We wouldn't want all the girls eyeing you up and the guys getting jealous, now would we?"
    "And just like that, she's done it to me again."
    "I make a mental note that, whatever kind of swimsuit I do end up buying, it won't be anything tight."
    "As I just don't think that I could walk around in public with my feelings for Sam showing through the material of my trunks!"
    show screen message(title="Buy a swimsuit!",what="Samantha told me to buy a {b}swimsuit{/b} to be able to go to the water-park.")
    pause
    hide screen message
    hide samantha
    return

label samantha_male_ending:

    $ game.hour = 16

    if renpy.has_label("samantha_achievement_3") and not game.flags.cheat:
        call samantha_achievement_3 from _call_samantha_achievement_3
    $ game.room = "church"
    scene bg church wedding with fade
    "I suppose most people have spent a lot of time imagining the day they'd get married, planning everything down to the most minute detail."
    "But I've never been one of them, and for most of my life I hadn't really given serious thought to the idea of whether I would ever tie the knot."
    "And now that I am, and the big day is finally here, it all seems pretty surreal, like something that's happening to another person while I'm just looking on."
    "I suppose I was never even sure that Sam would say yes, let alone that we'd make it this far."
    "We made sure to do things differently from the abortive plans she'd previously made with Ryan, choosing a traditional service at a small chapel."
    "The guest list was short, mainly consisting of close family and friends for Sam's side."
    "I have almost no family, and those I do have don't keep in contact, so for me it was an even smaller number of friends in attendance."
    "Though neither of us came out and said as much, I think we were both relieved to be making this a quiet affair, with only the eyes that we chose looking on."
    "My distinct lack of reliable and likeable male friends meant that there was no best man or groomsmen involved."
    "And so on the day, I find myself standing alone at the altar, with only the priest performing the ceremony."
    "But rather than being intimidated as I look back down the length of the chapel, I find that I only feel a sense of anticipation."
    "I guess that it's because I never conjured up images of this day in my mind that I kind of don't know exactly what to expect."
    "In turn, this means that I'm not at all nervous about the many small things that you normally hear of people fretting over at this point."
    "I'm actually just waiting, anticipating the moment when the music that I barely remember choosing will start to play."
    "But I'm really waiting to see Sam come walking in through the doors at the other end of the chapel."
    "When the music starts up for real, I almost fail to register the fact."
    "And it's only when the doors do open, allowing the intense light of day to flood in, that I shake myself back into the moment."
    "At first it's quite impossible to even make Sam out as she walks slowly into the chapel and up the aisle."
    "All I can see is her silhouette, until my eyes adjust themselves and she finally comes into focus."
    show samantha wedding flirt at center, zoomAt(1.0, (640, 1040)) with dissolve
    show samantha at center, traveling(1.5, 5.0, (640, 1040))
    if not samantha.is_visibly_pregnant:
        "Get ready for some serious cliches from here on in, because I'm too caught up in the moment to be all laid back and original right now."
        "Sam's always been one of the most beautiful girls I can ever remember meeting."
        "Able to turn me on with as little as a smile and drive me crazy with anything much more than that."
        "But today she seems to have become all of that and more in my eyes."
        "Right now it feels as if all of the qualities that made me fall for her are at the surface and on show for everyone to see."
        "Her dress is actually quite a simple affair of white, all the better to show off Sam's natural beauty."
        "She's clutching a bouquet of white flowers, the same as the kind that decorate the chapel."
        show wedding samantha with fade
        "Before I know it, she's walked the short distance up the aisle and is standing before me."
    else:
        "Sam looks simply radiant as she walks up the aisle towards me."
        "In fact, I don't think that I can ever recall thinking her more beautiful than she looks here today."
        "Perhaps the now rather pronounced curve of her belly means that her white dress could not have been more complicated in terms of its cut."
        "But to me, it just adds to the perfection of the moment."
        "We talked a great deal about the fact that she was pregnant before the wedding."
        "And neither of us felt that it was a thing that we should either be ashamed of or try to hide."
        if not samantha.flags.NPCpregnancy:
            "The child growing inside of her is there because of the love we feel for each other."
            "Probably a more honest declaration of our love so than any wedding ceremony could be."
        show wedding samantha with fade
        "Sam reaches me at the altar while I'm still enjoying the sight of her approach, shaking her head with a smile."
    "Priest" "Ahem...shall we begin?"
    show wedding samantha priest with dissolve
    "From there I try to concentrate on the moment, really I do."
    "But the words of the ceremony are nothing more than a blur, and it's a wonder I even remember to speak at my various cues."
    "There's the usual pause for dramatic effect as we get to that certain point in the proceedings..."
    "Priest" "If anyone present can show just cause as to why this couple may not be lawfully joined together in matrimony, let them speak now or forever hold their peace."
    "There follows a pregnant silence, and I wonder if this is the moment when Ryan will come barging through the doors."
    "Or even worse, one of the girls from my own past exploits!"
    "But after a few seconds, it becomes apparent that we're not about to be treated to a cinematic interloper, and the ceremony proceeds without any further interruptions."
    "All too soon we're approaching the final stages of the ceremony, reciting vows and exchanging rings."
    if not samantha.is_sex_slave:
        "Each of these is a simple affair, as Sam and I agreed beforehand that we find significance in each other, and not in repeated words or objects."
        "Priest" "It gives me great pleasure to pronounce you man and wife."
        "Priest" "You may kiss the bride."
        show wedding samantha -priest with dissolve
        "I don't need to be told twice."
        scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
        show samantha kiss wedding
        with dissolve
        $ samantha.flags.kiss += 1
        "Embracing Sam, I bend her over as far as possible and kiss her deeply."
        "As real as this all feels, there's still that little part of me that almost refuses to believe it."
        "Holy shit - not only did I get the girl in the end, but she followed me up the aisle and became my wife as well!"
    else:
        "I can see the look on the priest's face change as he realises what's about to happen."
        "And he can't help starting to sweat as the time comes for him to announce it too."
        "Priest" "Ah..."
        "Priest" "I...erm..."
        "Priest" "Well...the time has come for Samantha to make a...unique gesture."
        "Priest" "One which she feels is appropriate to demonstrate her devotion to her new partner."
        "Priest" "So from this point on, all of this is her idea alone!"
        scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
        show samantha b wedding at center, zoomAt(1.5, (640, 1040))
        with fade
        "The priest backs off, trying to distance himself physically like he just did verbally."
        "And at the same time, Sam turns to face me."
        show samantha b at center, zoomAt(1.5, (640, 1260)) with move
        "She smiles as she kneels down in front of me."
        "I can already hear ripples of conversation amongst the guests."
        "People on both sides of the chapel asking each other what's going on."
        "But a moment later, sounds of gasps and exclamations can be heard too."
        "That's because Sam's put down her bouquet and is unzipping my flies."
        "She seems supremely confident as she reaches into my pants."
        hide samantha
        show samantha bj2 open
        with fade
        "Sure that she's doing something that perfectly expresses her feelings."
        "And as for me?"
        "Well...I have to admit that my heart is pounding in my chest right now!"
        "Sam explained to me what she wanted to do."
        "She convinced me to go through with it too."
        "But I'm still doing all I can not to look out at the assembled guests."
        "What I'm feeling is a heady mixture of genuine fear and excitement."
        "Keeping my eyes fixed on what Sam's doing, I try to block out everything else."
        show samantha bj2 lick
        "So long as I keep my attention on her, I should be okay."
        "By now she's got my cock out of my pants."
        "Sam's stroking it, trying to get it to stand to attention."
        "Hey, cut me a little slack, okay?"
        "All of this is happening on my wedding day."
        "Not to mention in front of everyone we invited along to watch too!"
        "Even so it doesn't take long for it to start responding to her efforts."
        "And as my cock gets harder by the second, ignoring anything else seems to get easier."
        "This means that by the time Sam is kissing the head of my cock, I'm focused."
        "Nothing else registers save for what she's doing to me."
        show samantha bj2 suck
        "I watch with baited breath as Sam takes my cock into her mouth."
        "It goes in a little at a time, tiny pauses marking her progress."
        "And by the time it's deep enough for her to begin, I can't breathe."
        show samantha bj2 suck open2
        "Only when Sam begins to move her head back and forth can I exhale."
        "Even then my breath comes in ragged gaps of pleasure."
        "That's because Sam's pretty damn good at this kind of thing."
        "Lips, teeth and tongue, she uses them all to great effect."
        show samantha bj2 suck closed
        "But there's even more to it than that."
        "Sam's not just giving any average blowjob here."
        "She's chosen to do this as a means to show her love for me."
        "And that sentiment permeates everything that she does too."
        show samantha bj2 suck open2
        "Sam takes infinite care to make sure that every moment is incredible."
        "She devotes herself to making me feel every aspect of her affection."
        "If I were a more poetic kind of guy, I might even say it was an act of worship!"
        "But maybe that's a little blasphemous, considering we're in a chapel right now..."
        "Sam works the head and the shaft, squeezes my balls too."
        "All of which means that I'm soon on the brink of losing control."
        "As always, she's ahead of the game and one hundred percent in charge."
        "Knowing that I'm close to cumming, Sam prepares to handle it."
        menu:
            "Facial":
                show samantha bj2 lick
                "Sam opens her mouth and lets my cock slide out."
                "Then she kneels in front of me, waiting for it to happen."
                "The smile on her face makes her look pure and innocent."
                show samantha bj2 tits closed with hpunch
                "And so when I shoot my load over it, the effect is pretty special!"
                show samantha bj2 open with hpunch
                "Sam doesn't even flinch once, happily letting me paint her face."
                with hpunch
                "Soon it's covered in stick stripes of wet cum."
            "Swallow":
                show samantha bj2 suck closed
                "Sam keeps my cock in her mouth as it happens."
                with hpunch
                "And she swallows every drop as it shoots out of me."
                with hpunch
                "Not faltering once, she takes all I have to give."
                show samantha bj2 lick open with hpunch
                "And when I'm done, Sam opens her mouth and lets my cock slide out."
                "The smile on her face makes her look pure and innocent."
                "Like her hunger had finally been satisfied."
        "Almost as one, everyone in attendance surges to their feet."
        "For a moment I think they're going to storms out of the chapel."
        "Or worse, storm the altar and burn us as heretics!"
        "But then I hear them clapping, applause filling the air."
        "Some of them are even cheering too!"
        "Seems like Sam's performance met with their approval after all!"
    scene samantha ending
    if game.flags.nudistBeach == True:
        show samantha ending naked
    with fade
    samantha.say "They say that life is the things that happen while you're busy making plans, and I think my own path to getting here proves that's often the case."
    samantha.say "I'd always imagined the way my life would turn out, as far back as I can remember, planning things and dreaming up images of just what it would all look like."
    samantha.say "But then I found that when you have a fixed notion in your head of how things are supposed to turn out for you, sometimes it blinds you to what should have been obvious."
    samantha.say "Take my choice in men - I'd been convinced that, when the right guy came along, I'd know it somehow and be able to make things work with him because it was meant to be."
    samantha.say "So when I moved into the house with [hero.name] and Ryan, the former was friendly and a little quiet, whereas the latter couldn't wait to charm me with his personality and big plans for his life."
    samantha.say "Guess which one of them I fell for and which one of them I probably should have taken a second look at?"
    samantha.say "You'd be right if you assumed that they weren't one and the same person!"
    samantha.say "[hero.name] soon became just a good friend, while Ryan pursued me and won me over."
    samantha.say "And when he asked me to marry him, I thought it was proof that I'd made the right decision."
    samantha.say "Turns out that I was wrong...sort of."
    samantha.say "Ryan was definitely one to pursue a woman, but not the kind to keep it to a single conquest at a time."
    samantha.say "The fact that it was [hero.name] who proved it to me might be cause enough for some people to be suspicious of his motives."
    samantha.say "And I wasn't without my own reservations at the time, it's fair to say."
    samantha.say "But he was very honest with me, didn't deny for a second that he had always possessed feelings for me."
    samantha.say "And after that he left the whole thing in my own hands, not trying to push himself on me for a moment."
    samantha.say "That was when I started to wonder if I hadn't been wrong on all those occasions when I went looking for the things that I thought I wanted."
    samantha.say "I began to think about what might happen if I decided to accept life as it happened and see what it would bring."
    samantha.say "I'm happy to say that it brought [hero.name] to me, and all of the happiness we've had since."
    samantha.say "When, out of the blue, he asked me to marry him, it seemed to be another instance of life taking that unexpected path."
    samantha.say "And so I said yes."
    samantha.say "It hasn't been that long since we tied the knot, and we're still learning to live together as man and wife."
    samantha.say "But a lot has changed in that short space of time."
    samantha.say "[hero.name] moved out of the house that we used to share, and we both finally exorcised the bad memories it held for us."
    samantha.say "We moved to a smaller, but more remote little place up on the coast, within sight of the windswept beach."
    samantha.say "The nature of his job meant that he could work from home."
    samantha.say "And I finally put pen to paper, at least in a metaphorical sense, and wrote down the first of what became many stories in a career as a children's writer."
    samantha.say "I'm not likely to become the next JK Rowling any time soon, but I have a keen agent and a willing publisher, so things are looking good."
    samantha.say "That's what I was doing, just before I began typing this little reflection - working on a story."
    if not samantha.is_visibly_pregnant:
        samantha.say "But now I can hear [hero.name] calling me from just outside."
        samantha.say "He's wanting to go on one of the long walks we've taken to having down the beach together."
        samantha.say "Every day we simply head out and walk in the direction that our whim takes us."
        samantha.say "We talk, swap ideas and always keep an eye out for any interesting driftwood or other detritus washed up overnight."
        samantha.say "[hero.name] keeps talking about starting to make sculptures out of what we collect, even selling it at the flea market in the nearest little town."
        samantha.say "He bristles when I tell him to grow a beard and start drinking local IPAs, to become a true hipster."
        samantha.say "But the truth is that I think this new life is changing us both for the better."
        samantha.say "Or maybe just washing over us, like the tide on the driftwood, rubbing away until we're worn down to who we were always supposed to be."
    else:
        samantha.say "But now I can hear [hero.name] calling me from the living room."
        samantha.say "I can hear the small, sweet cries of Isaac too, sounds that are already starting to resemble words."
        samantha.say "Our is starting to toddle now, but he still won't take a single faltering step without his mother being present to watch and clap his efforts."
        samantha.say "I know that sometimes [hero.name] finds the life we're living out here quiet and sedate in comparison to the city."
        samantha.say "But I think that he's becoming satisfied with things in a whole different way to what would have made him happy in the past."
        samantha.say "It's funny how seeming to have less and so often make you want less too."
        samantha.say "I suppose it's just a case of learning what truly has value in life."
    samantha.say "I'm pretty sure that this isn't the end of our story, not by a long measure."
    samantha.say "But perhaps it might the point where our story changes subtly."
    samantha.say "Changes in a way that means it's more interesting to us than to anyone that might happen to be in on it too."

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not samantha.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_18
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_18
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label samantha_babyshopping:
    show samantha happy
    samantha.say "I'm growing really excited."
    "A grin is plastered on her face, not an uncommon, or unwelcome, sight, and it makes me smile at her in response."
    mike.say "It won't be long now, we haven't much time to wait."
    show samantha normal
    samantha.say "They've been kicking a lot lately, I think they're getting as restless as us."
    mike.say "We might even get an early arrival in that case."
    show samantha annoyed
    samantha.say "Oh, I hope so."
    samantha.say "Not early enough for it to be unhealthy of course, but I just can't wait much longer!"
    "I laugh, snaking an arm around Samantha's shoulder and pulling her closer."
    mike.say "They're going to be quite the looker with us as the parents."
    show samantha happy
    "This time it was Samantha's time to laugh, blushing as she placed a light kiss on my cheek."
    samantha.say "I hope they're just like you."
    mike.say "And I hope they're just like you, so fingers crossed they get the best of both worlds."
    show samantha a normal
    samantha.say "I've been making a list of things we need."
    "Samantha began as she pulled a sheet of paper from her pocket."
    "My jaw drops as I catch sight of what's written on it. It wasn't one piece of paper, it was four, each with both sides filled to the brim with things to buy."
    "Suddenly my wallet feels very empty, but I gulp, and nod as Samantha continues."
    samantha.say "So I think we should get..."
    "Though I can see the list myself, Samantha reading it aloud makes it seem that much longer."
    samantha.say "And then we can finish with just a few sets of bibs! Got it?"
    mike.say "Yeah I uh... I got it."
    "She grins at me as I nod along, my hands feeling awfully sweaty."
    show samantha at center, zoomAt(1.5, (640, 1040))
    "Thankfully, Samantha doesn't mind that as she leans in, taking my hands in hers and stepping close."
    "I find myself lost in her eyes for a few moments."
    show samantha flirt
    samantha.say "I love you, [hero.name]."
    "I wink at her, leaning in and embracing her."
    mike.say "I love you too."
    show samantha happy
    "Seeing her so overjoyed, that cute little smile, the way her entire face lights up with glee, makes everything worth it."
    "It's priceless."
    mike.say "Come on then, lots to do."
    scene bg drugstore
    show samantha casual normal at center, zoomAt(1.5, (640, 1040))
    with fade
    "I pull away quickly, keeping her hand in mine and motioning for her to lead."
    "I wouldn't know where to start, despite planning the trip, and it's clear she's come more than prepared."
    "She's even picked out specific products ahead of time, a level of forethought I'd never have achieved."
    mike.say "You really know what you're doing, huh?"
    samantha.say "Well, it's kinda embarrassing."
    samantha.say "I didn't think you'd want to spend all day browsing different onesies, so I came down yesterday to pick some things out."
    "I'm almost stunned for a moment."
    mike.say "You made this trip twice just to make it easier on me?"
    show samantha flirt
    samantha.say "I knew you'd be stressed out with the baby so close, and it was making me restless, so yep."
    "She looks a little sheepish, but I'm too busy appreciating her to calm her down immediately."
    mike.say "I can't believe you sometimes."
    mike.say "You're so thoughtful, it's impressive."
    show samantha happy
    samantha.say "Hehe, I just want to do everything I can to make this easier on you."
    mike.say "That's my job, I should be doing that for you."
    samantha.say "You already do so much, I just had to return the favour."
    hide samantha
    show samantha surprised at center, zoomAt(1.5, (640, 1040)), vshake
    "I scoff, and are about to retort when she suddenly yelps."
    samantha.say "Ah! They're kicking."
    hide samantha
    show samantha babyshopping
    with fade
    "I practically drop my bags where I stand, freeing up my hands for Samantha to guide to her stomach."
    "Her skin is warm, and, sure enough, I soon feel something bump my hand."
    "I'm surprised at just how violent it is, and it must have shown since Samantha quickly began laughing."
    mike.say "Wow, they're going to be a real fighter, huh?"
    samantha.say "It definitely feels like it, a little minx too, she keeps waking me up with this."
    "I wave a finger disapprovingly at Samantha's stomach, shaking my head and putting on my best stern voice."
    mike.say "Now now, Mommy needs her rest, stop waking her up."
    "Samantha laughs at my expression."
    samantha.say "You already look like a dad, now you just need some bad jokes and you're golden."
    mike.say "Bad jokes?"
    mike.say "How do you make holy water?"
    samantha.say "I don't know, how?"
    mike.say "You boil the hell out of it."
    "Samantha visibly cringes, though laughs anyway, whether or not it's simply out of pity I can't tell."
    samantha.say "Hehe, you really are ready to be a dad."
    mike.say "If that's all it takes, I'll be the best dad ever."
    samantha.say "I'm sure you will be anyway, [hero.name]."
    "Another kick interrupts my train of thought, Samantha yelping quietly at what I can only assume was a particularly strong one."
    samantha.say "Maybe they'll be an athlete."
    mike.say "They've certainly got the strength for it."
    mike.say "What do you think, do you want to be an athlete?"
    "I ask the mound on Samantha's stomach, then leant in, placing my cheek lightly against it."
    "I can't make out Samantha's face, but she has to be blushing, I can tell from the way even her stomach grew slightly warmer."
    mike.say "Interesting..."
    "I muse, smirking to myself."
    if samantha.flags.nickname == "cupcake":
        mike.say "They say they want to be a scientist, Cupcake."
    else:
        mike.say "They say they want to be a scientist, Samantha."
    samantha.say "Hehe, you're lucky, she never talks to me."
    mike.say "Why don't you talk to Mommy?"
    "I ask, pressing myself a little further into her stomach, not hard enough to harm the baby of course, but enough to freshly embarrass Samantha."
    if samantha.flags.nickname == "cupcake":
        mike.say "Ah, they say it's because I'm the cooler parent. Sorry Cupcake, straight out of the baby's mouth."
    else:
        mike.say "Ah, they say it's because I'm the cooler parent. Sorry Samantha, straight out of the baby's mouth."
    samantha.say "Oh, is that right? I'll remember that the next time they're craving a chocolate muffin."
    mike.say "Hear that? No more chocolate muffins for you."
    "I start to laugh, but am cut off by a foot to my cheek."
    "Startled, I quickly pull back, though quickly break into laughter alongside Samantha."
    samantha.say "I don't think she liked that."
    mike.say "Well, I wouldn't be happy if someone threatened to take MY muffins away."
    hide samantha
    show samantha close
    with fade
    "I stand and quickly embrace Samantha, squeezing her tightly."
    samantha.say "They're going to be amazing."
    mike.say "Just like their mother."
    samantha.say "Just like their dad."
    "I shut her up with a kiss, otherwise we'd be here arguing over who's best for the rest of the day."
    "Samantha seems embarrassed the entire situation happened in public, but thankfully we're soon off again before someone walks down the aisle we'd been standing in."
    scene bg black with timelaps
    scene expression f"bg {game.room}" with timelaps
    "By the time the day's over, I've got enough bags that I struggle to carry them all, and despite it being only a short walk I have to get a cab home."
    "It's better to have bought everything now than later though, and seeing how happy Samantha was as she picked out cute clothes was worth it alone."
    return

label samantha_meet_sasha:
    $ game.flags.sashaknowssamantha = True
    show samantha at left
    show sasha at right
    with dissolve
    sasha.say "Hi, I am Sasha."
    show samantha happy
    samantha.say "I am Samantha, nice to meet you."
    show sasha annoyed
    sasha.say "The ex crush?"
    if sasha.love > 100:
        sasha.say "You must cry at night, like a lot."
        show samantha surprised
        samantha.say "Why?"
        show sasha happy
        sasha.say "Well you missed on the stallion there."
        mike.say "..."
        if samantha.flags.knows_ryancheats:
            show samantha happy
            samantha.say "It's never too late."
            show sasha annoyed
            sasha.say "Had a chance, blew it, move along."
            $ sasha.love += 2
            $ samantha.love += 2
        elif samantha.love > 40:
            show samantha normal
            samantha.say "It was a close call with Ryan, I drew lots."
            $ samantha.love += 2
            $ sasha.love += 1
        else:
            show samantha happy
            samantha.say "He is a true friend, that's for sure."
    else:
        show samantha flirt
        samantha.say "That's for him to say."
        show samantha normal
        samantha.say "I've got to go."
        show sasha normal
        sasha.say "Bye."
    hide sasha
    hide samantha
    with dissolve
    return

label samantha_chat_bree:
    show samantha at left
    show bree at right
    with dissolve
    "Samantha and [bree.name] are talking near the bar."
    if samantha.flags.engaged and not samantha.flags.engaged2:
        $ samantha.flags.engaged2 = True
        show bree happy
        bree.say "I am so happy for you!!"
        show samantha happy
        samantha.say "Thank you, I am so happy for myself too."
        show bree annoyed
        bree.say "I wish I had someone too."
        show samantha surprised
        samantha.say "[hero.name] doesn't interest you?"
        if bree.love > 80:
            bree.say "Yes but I am not sure he sees me like that."
        elif bree.love > 100:
            show bree flirt
            bree.say "Yes but just for a good fuck, he is so hot."
            $ samantha_love += 1
            if samantha.love >= 100:
                show samantha flirt
                samantha.say "I wouldn't mind fucking him too..."
                $ bree_love += 1
                show samantha happy
                samantha.say "But I am not sure sucking my groom's best friend's dick would be proper."
                show bree happy
                bree.say "LOL!"
        else:
            bree.say "I won't be satisfied with your leftovers!"
    elif not samantha.flags.knows_ryancheats:
        show samantha sad
        samantha.say "Ryan has been going to that strip club a lot recently."
        show bree surprised
        bree.say "Why, I don't think that those girls have anything on you."
        samantha.say "He think I don't know but I do, I just play along."
        show bree annoyed
        bree.say "I am not sure that this is a healthy way of doing things."
        samantha.say "He just need to keep thinking of himself as some kind of apex predator..."
        bree.say "What a douche."
        samantha.say "But a cute one."
        bree.say "True..."
    elif samantha.flags.knows_ryancheats and randint(1, 2) == 1:
        show samantha blush
        samantha.say "I just fucked [hero.name] the other day..."
        show bree surprised
        bree.say "What? You are kidding right?"
        show samantha flirt
        samantha.say "I was a little drunk."
        $ bree.love += 1
        $ samantha.love += 1
    elif samantha.flags.knows_ryancheats:
        show bree angry
        bree.say "I can't believe Ryan cheated on you..."
        show samantha sad
        samantha.say "Yeah, me neither, I am still in shock."
        show bree normal
        bree.say "You are like the perfect woman."
        bree.say "Beautiful, funny, and you love to suck dicks."
        show samantha flirt
        samantha.say "I sure do..."
        samantha.say "Thank you [bree.name]."
    elif samantha.flags.engaged:
        bree.say "Show me the ring again."
        "Samantha shows her hand to [bree.name]."
        show bree happy
        bree.say "It's so beautiful!!!"
    else:
        "They just chat about girly stuff."
    hide bree
    hide samantha
    with dissolve
    return

label samantha_meet_bree:
    $ game.flags.samanthaknowsbree = True
    show samantha at left with dissolve
    "Samantha looks toward [bree.name]."
    samantha.say "I bet that this is one of your new roommates?"
    mike.say "Yep, want to meet her?"
    samantha.say "Why not, could be fun..."
    show bree at right with easeinright
    mike.say "Hey, [bree.name] this is Samantha My ex roommate."
    show samantha happy
    samantha.say "Nice to meet you."
    show bree happy
    bree.say "Nice to meet you too."
    if bree.love > 100:
        bree.say "So, you are the poor girl that let this fine young man go away?"
        show samantha normal
        samantha.say "That's one way of saying it."
        bree.say "Let me thank you in behalf of the other women."
        if samantha.love > 100:
            show bree normal
            show samantha flirt
            samantha.say "Don't get cocky, I might just take him back."
            $ samantha.love += 2
            $ bree.love += 2
        else:
            samantha.say "You are welcome."
            $ samantha.love += 1
            $ bree.love += 1
    else:
        bree.say "I am so glad you put that ad, that house is awesome."
        samantha.say "You are welcome."
    hide bree
    hide samantha
    with dissolve
    return

label samantha_start:
    if samantha.love.max < 40:
        $ samantha.love.max = 40
    $ samantha.unhide()
    return

label samantha_move_in:
    scene bg street with fade
    menu:
        set menuset
        "Light Boxes":
            "I pick up as many of the smaller boxes as I can and head inside."
            scene bg samhome with fade
            "I hadn't actually seen her new apartment yet, so when I walked in I could help but feel the homey atmosphere."
            "Despite some of the furniture still packed in boxes, it felt cramped, but in a cozy way."
            "I knew Sam would definitely love it here."
            "I carefully placed the boxes next to a sofa as Samantha passed by me to get more things."
            $ LB = False
        "Heavy Boxes":
            if hero.fitness >= 20:
                "I lift the boxes with ease and head into the apartment. I set them down next to the door and stand up to stretch my back."
                samantha.say "Oh, wow! Thanks for getting those. You're pretty strong!"
                $ samantha.love += 2
            else:
                "I don't know if I can lift these. I should probably wait for Samantha so we can both take it in."
                menu:
                    "Wait":
                        show samantha casual normal with moveinleft
                        "Samantha finally comes back outside and smirks at me."
                        samantha.say "Need some help?"
                        "I grumble a vague response, but we both grab side of the box and lift together. In no time, we have it sitting in the middle of the main bedroom."
                        samantha.say "Good work, team!"
                        hide samantha with moveoutleft
                    "Take in the Boxes":
                        "I find a grip under the boxes and lift with everything I have. It comes with me, but the second I try to take a step, it all comes crumbling down."
                        play sound body_fall
                        pause 0.3
                        with hpunch


                        with vpunch
                        with hpunch
                        "The boxes fall from my arms and I wince as I hear something break. That definitely wasn't good."
                        "Before I could check for damage, Samantha must have heard, as she came sprinting outside."
                        show samantha casual surprised with moveinleft
                        samantha.say "Oh no!"
                        mike.say "I'm so sorry!"
                        show samantha sad
                        "Samantha shook her head in dismissal and pulled The cardboard open."
                        "Inside was a variety of jewelry boxes, makeup palettes, and other things I couldn't quite name."
                        "What stood out the most, though, was a large, engraved mirror."
                        "Cracks webbed the glass and broken shards were strewn across the bottom of the box."
                        "I cringed as I watched her face fall at the sight."
                        mike.say "I'm really sorry about that. I'll pay for a new one!"
                        "After I said that, I hoped it wouldn't be too much. With my luck, it would be some sort of rare heirloom that she cherished every morning."
                        samantha.say "No, no, it's okay. Besides, I should be more concerned for you!"
                        samantha.say "You have seven years of bad luck now!"
                        show samantha normal
                        "She smiled up at me trying to brush it off but I could see the tightness in her lips."
                        "I started helping her take the rest in, deciding to let it go like she wanted."
                        $ samantha.love -= 1
                        hide samantha with moveoutleft
            $ HB = False
        "Take in the Desk":
            show samantha casual normal with moveinleft
            "As turn to pick up the desk, I find Samantha suddenly next to me."
            show samantha annoyed
            samantha.say "I'll help you take this one in."
            samantha.say "Ryan says it's a family gift- I don't want it getting ruined."
            mike.say "Are you saying you don't trust me?"
            show samantha normal
            samantha.say "You know I wouldn't! I'm saying we should be extra careful."
            mike.say "Alright, alright."
            "We both take the desk in slowly and set in down inside. Samantha sighs in relief."
            hide samantha with moveoutleft
            $ DESK = False
    return

label samantha_event_02:
    if samantha.love.max < 60:
        $ samantha.love.max = 60
    $ samantha.flags.engaged = True
    "Coming through the glass doors of the bakery, I could already see how crowded it was."
    "This place was a local hangout next to the coffee shop and always had a lively atmosphere- it was a good change of pace."
    "I stood in line behind a few other people and squinted at the chalkboard menu."
    "Even though I'd been here a million times, I still scan the familiar menu everytime I come in- and promptly order the same thing I always do."
    "Eventually it was my turn to order."
    show samantha casual normal
    samantha.say "Hello! What can I get for ya- [hero.name]!"
    show samantha happy
    mike.say "Hey. I didn't know you were working today."
    samantha.say "Yup! I'm covering for my friend's shift."
    show samantha sad
    samantha.say "She called in this morning sick; The poor girl sounded terrible."
    mike.say "Sounds pretty bad."
    show samantha normal
    samantha.say "Oh, I'm sure she'll be fine. Besides, I like working here."
    samantha.say "Anyhow, what would you like? Same thing?"
    mike.say "No! I'll take..."
    menu:
        "The usual.":
            mike.say "A chilled espresso- but with an extra sugar this time."
            "Samantha covers her mouth and giggles at me."
            samantha.say "That's what you call different? Alright! Coming right up."
        "Something new.":
            mike.say "Um... green tea and... a blueberry muffin."
            show samantha happy
            "Samantha grins and claps her hands happily."
            samantha.say "Feeling adventurous are we? Right away!"
            $ samantha.love += 1
    hide samantha with moveoutright
    pause 1
    show samantha casual normal with moveinright
    samantha.say "Here you go!"
    "Samantha hands me a crisp brown bag with the inky, black bakery logo painted on the front. I hand her a few dollars and coins to pay."
    if samantha.flags.nickname == "cupcake":
        mike.say "Thanks, Cupcake! I'll see you later-"
    else:
        mike.say "Thanks, Sam! I'll see you later-"
    samantha.say "Wait! I have my break in a few minutes."
    show samantha happy
    samantha.say "We can sit down and talk a little!"
    menu:
        "No thanks.":
            mike.say "Sorry, but I can only stay for a little while."
            show samantha casual sad
            samantha.say "Aw, that's too bad."
            samantha.say "It was good seeing you, then!"
            $ samantha.love -= 1
            hide samantha
            return
        "Sure!":
            samantha.say "Yaay! Pick a seat for us and I'll be over before you know it."
            "I nod my head and turn to find a seat, choosing one next to the window."
    scene bg bakery
    show samantha casual normal
    with fade
    "Samantha hops out from behind the counter with a large brown bag and a steaming cup in the other. She pulls out the chair on the other side of the table and sits down."
    show samantha at center, zoomAt(1.5, (640, 1140))
    samantha.say "So~"
    mike.say "... So what?"
    show samantha happy
    samantha.say "Tell me all about your roommates!"
    samantha.say "You didn't say too much last time, so how's it going?"
    mike.say "They're... interesting?"
    show samantha normal
    samantha.say "Don't give me that! Tell me then what you think of them!"
    mike.say "They're..."
    menu:
        "Entertaining.":
            mike.say "They're not bad or anything. [bree.name]'s a complete nerd and plays video games all the time."
            show samantha happy
            samantha.say "You say that like you don't do the same thing."
            mike.say "I don't as much anymore!"
            show samantha normal
            samantha.say "What about the other one? Sasha, right?"
            mike.say "Yeah. I don't think she likes me that much."
            samantha.say "Aw, don't say that!"
            show samantha happy
            samantha.say "I'm sure she'll warm up to you."
            $ samantha.love += 1
        "Just roommates.":
            mike.say "That's all they are. As long as they pay their share, I don't really care what they do."
            samantha.say "You should at least get to know them a little bit!"
            samantha.say "Who knows, maybe you'll like them more than you think."
            "Samantha winks at me and I roll my eyes. All she does is lightly laugh at my response."
        "Pretty attractive.":
            show samantha surprised
            samantha.say "Ooh~ so you are interested in something."
            mike.say "Don't say it like that! But yeah, [bree.name] and Sasha are more than good looking."
            show samantha happy
            samantha.say "Don't be afraid to ask a girl to hook you up~ I can be an A+ wingwoman when I want to be."
            $ samantha.love += 1
    show samantha normal
    "We both sip our drinks in a comfortable silence. She pulls out a bagel and cookies out from her bag and happily chomps on her sweets."
    "We talk for a while longer before another employee calls out to Samantha and tells her to get back to service."
    show samantha surprised
    samantha.say "Aw, I have to go. Wait-!"
    hide samantha
    show samantha casual surprised at center, zoomAt (2, (650, 1350))
    "Samantha jumps forward and grabs onto my hands."
    samantha.say "Do you want to help me move the rest of my stuff in tonight?"
    show samantha normal
    samantha.say "Ryan's working tonight so he won't be home until I'm asleep."
    samantha.say "It would be great to surprise him with a finished home!"
    if samantha.flags.nickname == "cupcake":
        mike.say "I don't know, Cupcake..."
    else:
        mike.say "I don't know, Sam..."
    samantha.say "I'll buy you some more coffee- and how about a slice of our cake?"
    menu:
        "I've got other plans.":
            mike.say "Sorry, but I need to get a few things done today. And I have work tomorrow so I can't stay out too late."
            show samantha casual sad
            samantha.say "Aw, that's too bad."
            samantha.say "Okay, I understand. Thanks for sitting with me though!"
            samantha.say "It was fun talking."
            hide samantha
            show samantha casual at center
            hide samantha with moveoutright
            "Samantha stands up and waves at me, returning back to her spot at the counter. I get up and head back outside."
            $ samantha.love -= 1
            return
        "Alright. I'll come over later today.":
            show samantha casual happy
            samantha.say "Yaay! Thank you so much! I'll see you after work."
            $ game.pass_time(21 - game.hour)
    scene bg black with timelaps
    scene bg street
    show samantha casual normal
    with timelaps
    "She is standing out in the middle of the street next to a pile of boxes and a small, dark mahogany desk."
    mike.say "What's with all the stuff out here?"
    samantha.say "The moving truck just dumped the rest outside and I haven't seen them since. Can you believe that?"
    "I rose an eyebrow in suspicion but accepted the explanation. There was probably more to it- I'll just assume Ryan pissed them off."
    mike.say "That sucks! We should move this stuff in before it gets too late then."
    samantha.say "Great! Grab whatever you want, all I need is for it to be inside."
    "Samantha grabs a stack of medium sized boxes and made her way inside."
    samantha.say "The door's open! So don't worry about that."
    "I stared at the pile of boxes, wondering where to start."
    "Some of the boxes seemed pretty heavy, and I didn't want to risk breaking anything if I dropped it."
    "Not to mention, that would be humiliating in front of Samantha. Where should I start?"
    hide samantha with moveoutleft
    $ LB = True
    $ HB = True
    $ DESK = True
    $ menuset = set()
    while DESK or HB or LB:
        call samantha_move_in from _call_samantha_move_in
    scene bg samhome
    show samantha casual surprised
    with fade
    show fx exclamation
    samantha.say "Whoo!"
    show samantha happy
    samantha.say "Thanks for taking that stuff in. You were a big help!"
    hide fx
    mike.say "Yeah, no problem. Happy to get this out of your way- but don't think that means I'll forget about that free coffee."
    show samantha normal
    samantha.say "I'm a woman of my word."
    "We stare at each other for a moment and I could see a distressed look rise up in her eyes."
    mike.say "Something wrong?"
    "A minute passes as she tries to bring the words out, but instead she grabs onto my hands."
    samantha.say "You have to promise not to tell anyone."
    mike.say "..."
    mike.say "Of course."
    samantha.say "Well..."
    "Samantha lifts her hand and shows me her fingers."
    "It's only then that I notice the shiny, gold ring gracing her fourth digit."
    "Looking back up at her face, I see cheerful tears in her eyes."
    show samantha flirt
    samantha.say "Ryan proposed!"
    mike.say "..."
    "I didn't know what to say. My heart sank at the news. Was Ryan officially taking Sam away from me?"
    samantha.say "He told me to keep it a secret for now, but I can't hold it in any longer!"
    menu:
        "Be supportive":
            if samantha.flags.nickname == "cupcake":
                mike.say "... That's great, Cupcake! I know you'll be happy together."
            else:
                mike.say "... That's great, Sam! I know you'll be happy together."
            show samantha happy
            samantha.say "Thank you! I'm so lucky to have him."
            mike.say "I better be invited to the wedding."
            samantha.say "Haha, absolutely. You'll be first on the list!"
            play sound cell_vibrate
            "My phone vibrates in my pocket and I check the time- it was getting pretty late. I wondered what was holding up Ryan for so long?"
            show samantha normal
            samantha.say "I've kept you for too long, haven't I? I'm sorry! You should get home soon."
            mike.say "You're right. I have work tomorrow, so I'll head out."
            show samantha at center, zoomAt (1.65, (650, 1140))
            "We both head to the door and Samantha sees me out, but not before pulling me into a tight hug."
            samantha.say "Thank you so much, [hero.name]!"
            $ samantha.love += 2
        "Be disapproving":
            mike.say "I don't know... don't you think you're too young to be jumping into that? And you just moved in together. What if you don't like it?"
            show samantha surprised
            samantha.say "What do you mean? We love each other. That's all that matters, right?"
            mike.say "I don't think you guys are thinking straight."
            show samantha sad
            "Samantha had a pained expression of betrayal. She'd trusted me with something she'd been holding back and here I was spitting all over her dream."
            samantha.say "I've always wanted to be with him like this. I'm happy, he's happy and that's all I need. Maybe you should leave. Thanks for all the help today."
            "Without another word, she walks me to the door and before I can say goodbye, it's already shut tight behind me."
            $ samantha.love -= 2
    hide samantha with dissolve
    $ game.room = "street"
    return


label samantha_event_03:
    if samantha.love.max < 80:
        $ samantha.love.max = 80
    $ samantha.flags.weddingtime = TemporaryFlag(True, 7, "samantha_wedding_flag")
    "As I walk into the park and look around, there are groups of people hanging out."
    show samantha annoyed at center, zoomAt(1.0, (1000, 900)) with dissolve
    "Suddenly, I spot Samantha sitting alone at a table under a tree."
    "She's hunched over a book with papers scattered all over the surface."
    "I come up next to her, but she doesn't seem to have noticed, heavily entranced by the work in front of her."
    "Peering over her shoulder, I can see scribbles of pencil and markings."
    "She still hadn't noticed me yet."
    menu:
        "Hey, Samantha.":
            show samantha happy
            "Samantha raises her head and looks back at me, smiling warmly."
            samantha.say "Hi, [hero.name]! Fancy seeing you here."
            "I sit down across from her."
        "Scare":
            show samantha surprised at center, zoomAt(1.0, (1000, 900)), vshake
            "I quickly bring my hands down on her shoulders and I can feel her jump in surprise."
            "The pencil in her hand jerked and made a long mark over a line of writing."
            samantha.say "Eep!"
            "I chuckle lightly at her reaction."
            show samantha angry
            "My grin fell a little when I saw that she looked upset."
            samantha.say "[hero.name]?! That's not funny!"
            "She leans back and attempts to swat me away, but I move out of her reach."
            mike.say "Sorry, sorry!"
            $ samantha.love -= 1
            "I sit down across from her sheepishly."
    show samantha normal at center, zoomAt(1.5, (640, 1140)) with fade
    mike.say "What are you working on?"
    show samantha annoyed
    samantha.say "Just some homework."
    "Her face was tense with frustration."
    "She didn't seem to be having an easy time."
    menu:
        "You look like you're having trouble.":
            show samantha surprised
            samantha.say "No, I'm...!"
            show samantha annoyed
            "She struggled to say something but eventually deflated."
            "She didn't seem very happy with my observation."
            samantha.say "I guess... if you know anything about the subject, do you think you could help me out?"
            $ samantha.love -= 1
        "Sounds difficult. Need any help?":
            show samantha normal
            "Sam purses her lips, but in the end it turns warm and relaxed."
            samantha.say "You know what... yeah. I could use some pointers. Thanks!"
            $ samantha.love += 1
        "Homework doesn't sound fun. Good luck with that!":
            samantha.say "Yeah... thanks. I'll see you later then."
            $ samantha.love -= 1
            hide samantha with dissolve
            return
    "Sam hands me the paper she'd been writing on. Staring down at the sheet, it was covered in notes and numbering problems."
    if hero.knowledge >= 25:
        show samantha normal
        "It looked like statistics. I remembered it was one of the core classes she was taking, so she must not have liked it as much since it was required."
        mike.say "Stats, right? I remember taking that class. I didn't like it too much. But, I guess I didn't like a lot of my classes now that I think about it."
        samantha.say "Yeah! I don't like it too much either."
        mike.say "Alright... let's start here."
        "I take Samantha's pencil and lightly tap it to one of the numbers on the paper in front of me. Sam leans forward over the table to see."
        "Her blonde hair curtains over her face and she has her arms crossed under her breasts."
        mike.say "Uhm..."
        "I try not to let my eyes wander down and redirect my focus."
        mike.say "Well, your first mistake is here..."
        scene bg black with timelaps
        scene bg park
        show samantha normal at center, zoomAt(1.5, (640, 1140))
        with timelaps
        mike.say "Get it?"
        "Samantha's eyes had been trained on me the entire time. It was nice to have her unbreakable attention, even if it was usually reserved for Ryan."
        samantha.say "I think so."
        "I hand her the pencil and she gently takes it from me as if I'd somehow blessed it."
        mike.say "Try it out on the next problem."
        "She nods and a look of determination crosses over her face. She begins slowly writing out her answer. When she's finished, she turns the paper back over to me."
        "Looking it over, I can tell that it's wrong."
        menu:
            "Were you listening to me at all?":
                $ samantha.love -= 1
                $ samantha.sub += 5
                show samantha sad
                samantha.say "I was! I'm sorry. I just don't understand it, I guess."
                mike.say "Try to pay attention this time."
                "I re-explain what I can, faster this time. She seems to become more confused, so I slow down."
                mike.say "Understand?"
                "She grabs her pencil and moves onto the next problem. She does better, but still makes a few mistakes."
                mike.say "No... try again."
                "Sam groans and runs a hand through her hair."
                samantha.say "I don't think I can do this!"
                "She starts packing up her things and closes her books."
                mike.say "What? Can't we try it one more time."
                samantha.say "No, it's alright. I'll stay after class and see if one of the teachers can explain it."
                mike.say "Stay after? Don't you have work in the evening?"
                samantha.say "Yes, but I can't afford to fail this course. I need my grades high to keep my parents happy, you know?"
                mike.say "Oh, alright. Sorry I couldn't help you then."
                show samantha normal
                samantha.say "It's okay! I appreciate the thought."
            "Good try, but you should do it like this.":
                "I correct her answer easily and explain each step."
                show samantha surprised
                samantha.say "Oh...! I got it. Thanks!"
                mike.say "Do the next one."
                show samantha normal
                samantha.say "Okay..."
                samantha.say "..."
                samantha.say "Like this?"
                "I look over her work."
                mike.say "Yeah, that's great! Nice."
                show samantha happy
                "She happily claps her hands and her face is practically glowing."
                samantha.say "Yayy! I think I can do it now. Thank you so much!"
                mike.say "No problem."
                samantha.say "Seriously~ You should be a teacher or something."
                mike.say "Haha... I don't think it suits me much."
        mike.say "... Wasn't Ryan supposed to be studying with you?"
        show samantha sad
        samantha.say "Oh. He's been pretty busy lately. He hasn't been coming home at night and I'm worried that he might be overworking himself. I didn't want to bother him."
        mike.say "That sucks. You guys should be with each other more."
        menu:
            "You can always come to me if you need help.":
                show samantha happy blush
                "Samantha beams and I can see a blush rise on her cheeks."
                samantha.say "Thanks, [hero.name]. I really appreciate it."
                $ samantha.love += 2
            "Ask Ryan to help you next time.":
                samantha.say "You're right. I'm sorry if I bothered you."
                menu:
                    "You didn't bother me.":
                        mike.say "No, it was fun, really. I just think you should get with him more since you guys are getting married."
                        show samantha happy
                        samantha.say "Yeah! That's true. You always know what to say, huh?"
                        $ samantha.love += 1
                    "Stay silent.":
                        samantha.say "I'll stay after class next time. Maybe a teacher will have time for me."
                        $ samantha.love -= 1
        show samantha normal
        samantha.say "Well, I should get going."
    else:
        "I didn't really know what I was looking at. It had to be some sort of math, right? Numbers and symbols littered the page, not really connecting in my brain."
        mike.say "Uhm... math?"
        samantha.say "Yup! I know it's not really your thing, so you don't have to help me."
        "I would act offended at her words, but I knew there was nothing malicious behind her tone. Besides, she was right."
        "She was also giving me a way out of this."
        mike.say "No, I can still help you! It'll just take me a bit longer. But two heads are better than one, right?"
        show samantha happy
        samantha.say "Alright, yeah! Let's do this!"
        show samantha normal
        "I internally berate myself. I should have taken the easy way out- there was no way this could end well."
        samantha.say "Do you know how to do this part? I keep messing up."
        "She points down at a seemingly random space on the page. I stare past her finger, trying to think of an answer."
        menu:
            "Change the subject.":
                mike.say "Hmm, yeah... why'd you come all the way out here to work on this, anyway?"
                "Sam raises an eyebrow at me, but answers."
                samantha.say "Because I don't like being cooped up in my house all day! I can't just go between university, the bakery and home."
                show samantha annoyed
                samantha.say "I would go crazy! Ryan isn't home that often at any rate."
                samantha.say "..."
                samantha.say "You have no idea, do you?"
                mike.say "What? I- uhm- ... no."
                show samantha happy
                "Surprisingly, Samantha giggles at me."
                samantha.say "Well, it's sweet of you to have offered."
                show samantha normal
                samantha.say "I wonder if I could just ask one of my teachers. But they're always busy."
                mike.say "What about Ryan?"
                samantha.say "He leaves in the morning for work and has been coming home late. I don't want to stress him out."
                if samantha.flags.nickname == "cupcake":
                    mike.say "C'mon, Cupcake. You're the one person who couldn't stress him out. You said he was going to study with you anyway."
                else:
                    mike.say "C'mon, Sam. You're the one person who couldn't stress him out. You said he was going to study with you anyway."
                samantha.say "Alright, you have a point."
                samantha.say "I'll ask him next time! Thanks, [hero.name]!"
            "Think of an answer.":
                mike.say "Hmm..."
                if hero.charm >= 25:
                    mike.say "Try using these and make them the dividend."
                    show samantha surprised
                    samantha.say "Will that work?"
                    mike.say "Probably."
                    show samantha normal
                    "Samantha giggles at my smooth answer, but does my suggestion anyway."
                    samantha.say "Nope! That doesn't look right."
                    mike.say "Aw, well, that's my contribution."
                    samantha.say "Quite the attempt!"
                    mike.say "What can I say? I'm good at what I do."
                    show samantha happy
                    "Samantha and I laugh and she closes her book with a sigh."
                    samantha.say "What are you up to? I didn't expect to see you today."
                    mike.say "Oh, just looking for someone to hang out with. Lucky I found you."
                    samantha.say "Aren't you! Well, at least you can entertain me out of my homework, hm?"
                    mike.say "I wouldn't put it like that. We should go hang out somewhere else if you don't want to work."
                    samantha.say "Tempting! But I should get home soon."
                    $ samantha.love += 5
                else:
                    mike.say "Uhm... you could try those- numbers? Why are there letters?"
                    show samantha happy
                    "Samantha laughs and pushes a strand of hair behind her ear."
                    samantha.say "You're good at a lot of things, [hero.name], but statistics is not one of them."
                    mike.say "Ah, I'm hurt!"
                    show samantha normal
                    "She rolls her eyes playfully and closes her books and packs up. She seems to have accepted that she wouldn't be getting it done today."
                    mike.say "But, seriously. Sorry I can't help you."
                    samantha.say "Don't worry about it. I should know how to do this ny now. But I can barely pay attention! I can't stop thinking about Ryan."
                    samantha.say "He wants to get married soon and I'm excited to start planning."
                    mike.say "Soon?"
                    samantha.say "He wants everything set up in a few months."
                    mike.say "A few months?! That doesn't make sense."
                    show samantha happy
                    samantha.say "Of course it does! He loves me. I want to be his wife soon, too."
                    "I shake my head but don't say anything this time. If they really did want to move fast then nothing I could say would stop them for a second."
                    samantha.say "Well, I should get going."
    show samantha normal
    mike.say "Alright. I'll see you later?"
    samantha.say "Definitely! I need to go shopping, so we can meet up then. I need a few things for the new home."
    "Shopping with Samantha usually meant buying books or clothes. Not the most exciting thing to do, but I was okay with it as long as she didn't take forever."
    mike.say "Sure... sounds good."
    "She must have noticed my lack of enthusiasm, putting her hands on her hips."
    samantha.say "I'm also going out to party. You know, drinking, dancing- how about that?"
    mike.say "I can definitely do that."
    samantha.say "That's what I thought. But you should join me for a little shopping if you have the time. I'm not going to the usual place. We'll have fun!"
    "She winked at me and I simply blinked back in confusion."
    "I guess I would find out what that meant next time we met."
    samantha.say "I'll see you then, [hero.name]!"
    hide samantha
    show samantha casual
    "She gathered her things in her arms and headed for the entrance with a wave. I waved back, watching her go."
    hide samantha with dissolve
    "I slumped back to the table, a boredom coming over me. What would I do now?"
    return

label samantha_event_04:
    $ hero.flags.knows_ryancheats = True
    "The nightclub was more crowded than I had expected."
    "I think it opened about an hour ago, but here people were, rocking to the music with drinks in hand."
    "I inched around the dance floor to the open bar in the back."
    "Sitting down, I order a drink and wait to be served."
    "I absent-mindedly browse my phone, scrolling through my contacts."
    "Maybe I should call Sam to hang out again."
    "That would certainly lighten things up."
    "But she was probably with Ryan."
    ryan.say "Hey. Can I get you something to drink?"
    "As if reading my mind, Ryan's voice popped up nearby."
    show ryan casual smile at left5
    show audrey normal at top_mostleft, blacker
    with dissolve
    "My head snapped up, seeing him on the other side of the long bar next to a busty girl with silky black hair."
    "Girl" "Ryan! I didn't think I'd see you today."
    "The girl stands up and throws her arms around Ryan."
    "I couldn't help the suspicion that rose in me."
    "What was going on?"
    show ryan casual smile
    ryan.say "Of course, baby. I can't just leave you here sober."
    "The girl giggled, a small hand coming to cover her mouth."
    "A blush covered her face as the bartender slid a bright coloured drink over to them."
    "The girl took the drink in one hand and grabbed at his arms with the other, pressing it between her breasts."
    "Girl" "What have you been up to all week? I haven't seen you for a few nights."
    ryan.say "Oh, ya know. Working."
    "Girl" "You work too much. Spend more time with me!"
    ryan.say "How am I supposed to spoil you then?"
    "The girl giggled again and pressed against him more."
    "Girl" "How about I just wait at your house? It would save you the trip and we could have fun all night~"
    ryan.say "Nah- you wouldn't like my shitty apartment. Besides, I have room-mates, so I don't want them to seduce you away from me."
    "Girl" "Ryan! No one could take me away from you."
    "I stared with wide eyes at the scene before me."
    "There was no way this was actually happening."
    "Sure, Ryan was a douchebag, but he and Samantha were the happiest people I knew..."
    "But apparently not."
    "As the two talked more, I could feel anger replace the suspicion."
    "How can he do this to Sam?"
    "How can anyone do this to a sweet girl like her?"
    "The bartender gave me my drink, but I held it with numb hands."
    "There is no way Samantha would believe me if I just told her about this."
    "I stared blankly at my phone and back up at Ryan."
    "Making an easy decision, I lifted my phone and opened the camera."
    "Ryan was so attentive to the girl leaning over him that he didn't even notice."
    "I snap a few photos."
    "I couldn't just send these to her without saying anything, could I?"
    "She would break down."
    "I had to be there for her."
    "I lifted the phone to my ear after dialling her number."
    play sound phone_calling
    "..."
    "Voicemail. Was her phone off?"
    "I'd have to find her later then."
    "I threw a few dollars onto the counter with a tip and slid out of my seat."
    scene bg street with fade
    "I practically ran out of the club, feeling like Ryan might see me if I stayed any longer."
    "I had to find Sam."
    $ game.room = "street"
    return

label samantha_event_05:
    if samantha.love.max < 100:
        $ samantha.love.max = 100
    show samantha
    "Do I really want to do this?"
    "Her heart will be broken."
    "She loves Ryan with every part of her body."
    "I will only be hurting her."
    "I can't stand to see her cry over everything."
    menu:
        "Show Her the Pictures":
            samantha.say "..."
            samantha.say "Is something wrong?"
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake, I-"
            else:
                mike.say "Sam, I-"
            "How should I say it?"
            mike.say "I was at the nightclub the other day."
            samantha.say "Hmm~? Meet anyone nice?"
            mike.say "I saw Ryan..."
            mike.say "With another girl."
            show samantha surprised
            samantha.say "... That's not funny."
            mike.say "I'm serious."
            show samantha angry
            samantha.say "Bullshit!"
            samantha.say "Don't say something like that!"
            "I pull out my phone and unlock it."
            "I tap open the photo album and hand it to her."
            "She stares down at the picture, expression still firm."
            "She blinks rapidly and finally frowns."
            show samantha surprised
            samantha.say "This isn't real."
            samantha.say "I...don't understand."
            show samantha sad
            "She hands me back my phone...."
            "I don't say anything until her eyes wet with tears."
            if samantha.flags.nickname == "cupcake":
                mike.say "Oh, Cupcake-"
            else:
                mike.say "Oh, Sam-"
            show samantha cry
            "She drops her head into her hands and sobs."
            "My heart stops."
            "What do I do?"
            show samantha cry at center, zoomAt(1.5, (640, 1040))
            "I decide to pull her into a side hug and she immediately leans into me."
            samantha.say "Tell me it isn't real! Please!"
            "I don't say anything and let her cry."
            samantha.say "I- I have to go."
            hide samantha
            show samantha sad
            "She sniffs and roughly stands from where we sat."
            if samantha.flags.nickname == "cupcake":
                mike.say "Wait- Cupcake!"
            else:
                mike.say "Wait- Sam!"
            "I get up and breath a sigh."
            "If she wants to talk about it again, she will. I don't doubt that."
            $ samantha.flags.knows_ryancheats = True
            $ samantha.hide()
        "Let Her Be Happy":
            "There was no way I can do this to her."
            "It's better to let her think Ryan is faithful to her, isn't it?"
            "Gripping my phone tightly, I walk away without saying a word, letting her stay in her beautiful ignorance."
            $ wedding_day = game.calendar.get_next_day_of_week("sunday")
            $ hero.calendar.add(wedding_day, LabelAppointment((12, 20), "samantha", "Sam and Ryan's wedding", "samantha_event_B01"))
    hide samantha
    return

label samantha_event_A01:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Samantha")
    if not result:
        $ hero.cancel_event()
        $ samantha.love -= 5
        return
    $ samantha.flags.nokiss = False
    $ samantha.unhide()
    "I'm distracted for a moment- my phones is buzzing in my pocket."
    "The contact name is Samantha."
    if samantha.flags.nickname == "cupcake":
        mike.say "Hello? Cupcake?"
    else:
        mike.say "Hello? Sam?"
    samantha.say "He-ey there."
    "..."
    "That didn't sound good."
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake? Are you okay?"
    else:
        mike.say "Samantha? Are you okay?"
    samantha.say "Never been better. I want to see you."
    mike.say "What?"
    samantha.say "Come here!"
    mike.say "... Where are you?"
    samantha.say "I'm outside your house. I knocked but no one will open the door. Open up! Open-n up!"
    mike.say "... Okay. I'll be right there."
    play sound phone_calling
    scene bg black with fade
    scene bg house
    show samantha casual sad blush
    with wiperight
    "I stare at her. Her cheeks are stained red and she smelled like..."
    mike.say "Are you drunk?"
    samantha.say "Ju-ust a little~ I'm a good girl though."
    show samantha at center, zoomAt(1.5, (640, 1040))
    "Before I know what's happening, she leans heavily onto me, burying her face in my shirt."
    if samantha.flags.nickname == "cupcake":
        mike.say "Uh, Cupcake?"
    else:
        mike.say "Uh, Samantha?"
    samantha.say "You still love me don't you?"
    samantha.say "Tell me you love me."
    menu:
        "I still love you.":
            "Samantha giggles, but it turns into a sob."
            samantha.say "I know you do, I know you do."
            $ samantha.love += 2
        "Say Nothing":
            "Samantha sobs into my shirt and I could feel the tears soaking through."
            samantha.say "You do! I know you do!"
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake, you know I'll always be your friend..."
            else:
                mike.say "Samantha, you know I'll always be your friend..."
            "I take her to the couch and we sit there until she cries herself to sleep."
            return
    if samantha.flags.nickname == "cupcake":
        mike.say "Come on, Cupcake. Wait in my room and I'll get you some water."
    else:
        mike.say "Come on, Sam. Wait in my room and I'll get you some water."
    "I take her lazy nod as a yes and lead her to my door."
    scene bg bedroom1
    show samantha casual sad
    with fade
    "She sits on my bed with a hazy blank stare."
    mike.say "I'll be right back."
    hide samantha
    scene bg kitchen
    with fade
    "I grab a glass from the cabinet and fill it with water at the sink."
    "I didn't really know how to deal with a drunk Samantha."
    "Especially a sad one."
    "I didn't know what the hell to do."
    scene bg bedroom1 with fade
    mike.say "Here. I got you some-"
    show samantha underwear blush flirt with dissolve
    "I cut myself off and almost drop the water."
    "There was Samantha, laying on my bed with just her bra and tugging at her panties."
    samantha.say "You're so sweet! Come here and let me thank you!"
    mike.say "You... you're drunk. You'll regret this later."
    "It was taking everything in me to hold myself back from jumping into bed with her."
    samantha.say "I need you! You want to make me feel better, don't you?"
    "I hesitated. Samantha seemed to noticed, and pulled her panties down to her knees."
    "My legs carried me faster than my brain could think."
    "When I came to the edge of the bed, she spread her legs and wrapped them around my waist."
    samantha.say "Take all that stuff off, won't you?"
    "I looked down and realized she was talking about my clothes."
    "I numbly unbuttoned my jeans and threw my shirt across my bedroom."
    show samantha at center, zoomAt(1.85, (640, 1340)) with hpunch
    "Apparently I was going too slow, because she tugged on me with her legs and I fell on top of her."
    "With my elbows either side of her head, I could feel her hot breath ghosting across my face."
    "The unique smell of alcohol tinged her scent."
    samantha.say "You'll make me happy, won't you?"
    samantha.say "Be rough, like my baby."
    samantha.say "Do what you want with me."
    "Her baby? Was she talking about Ryan?"
    menu:
        "Let her lead":
            "I didn't reply, instead gently pressing my lips onto hers."
            "She froze at first, her eyes wide."
            "Eventually she melted into me."
            "I could feel her throw her arms around my neck and my chest swelled."
            "I finally had her and she was mine to love."
            mike.say "I'll treat you right."
            "I pulled her up by her waist higher up on the bed."
            "She let me drag her with ease."
            "Only her breasts were covered by now, her panties thrown somewhere on the floor when she tugged me on top of her."
            "I gently reached behind her back and unhook her bra."
            "She pushes herself up a little to help."
            show samantha naked at center, traveling (1.85, 10.0, (640, 1040))
            "Once it's off, her large breasts spill out."
            "Her nipples were pierced with simple rings."
            samantha.say "I wore them just for you~"
            "I didn't know if she was being sincere or was too drunk to think straight."
            "Nonetheless, I dipped my mouth down onto one of the rings and sucked smoothly."
            "A soft moan sounded above me. I took that as a good sign."
            "I took more of her breast into my mouth and sucked harder. Her back arched and I moved with her."
            "I made my hands busy by groping at her sides and hips, going lower and lower until I reached the heat of her vagina."
            "Sam gasps above me and opens her legs as far as she can when I test a finger at her opening. I stop for a moment, feeling metal. Ryan really did have her pierce everything."
            "I toy with it for a second before rubbing a knuckle against her clit."
            "It's already slick and wet."
            samantha.say "[hero.name]!"
            samantha.say "Let me help you, too."
            "Before I can react, she flips me over and the next thing I know I'm on my back."
            "Her perfect hands snake down to my member and I hold back a moan when she expertly grasps it and squeezes gently."
            "Her arms move up and down."
            "One hand goes down and massages the base and I can't keep the noises back this time."
            samantha.say "I'll get ready for you."
            "It's practically a whisper, like she talking to herself."
            "She takes her hands off me and shoves two fingers into herself, stretching her entrance easily."
            "A look of discomfort comes across her face for a moment, but it doesn't stop her from inserting more digits."
            "My tongue darts out to wet my lips."
            "I could feel myself get harder at the sight."
            "There was something about her shiny, blonde hair draped over her shoulders and the blush that had spread from her face to her whole body that made her undeniably beautiful."
            "She was taking care of me more than I was taking care of her, wasn't she?"
            "Well, whatever she wanted."
            if hero.has_condom():
                menu:
                    "Use a condom":
                        $ CONDOM = hero.use_condom()
                        "I put a condom on then push inside of her."
                    "Do it raw":
                        $ CONDOM = False
                        "I spit into my hand, try to cover my dick as much as I can and push inside of her."
            else:
                $ CONDOM = False
                "I spit into my hand, try to cover my dick as much as I can and push inside of her."
            samantha.say "Ready, sweetie?"
            "I grab her hips and position her above my erection."
            hide samantha
            show samantha cowgirl up
            with fade
            "I slowly lower her on, and she groans as I fill her up."
            show samantha cowgirl down vaginal
            "I give her a moment to adjust, but she gets used to it quickly."
            show samantha cowgirl up pleasure
            pause 0.4
            show samantha cowgirl down at startle(0.05,-10)
            pause 0.4
            show samantha cowgirl up
            pause 0.4
            show samantha cowgirl down at startle(0.05,-10)
            pause 0.4
            show samantha cowgirl up
            pause 0.4
            show samantha cowgirl down at startle(0.05,-10)
            "I jerk my own hips slightly and she takes the hint. We both move back and forth together, slapping loudly as I move in and out."
            show samantha cowgirl up speed orgasm
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            pause 0.3
            show samantha cowgirl up
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            pause 0.3
            show samantha cowgirl up
            pause 0.2
            show samantha cowgirl down with vpunch
            "The heat becomes overwhelming and she's satisfyingly tight. Eventually, I feel the climax coming."
            if not CONDOM:
                "Before I can warn her and pull out, she leans down and licks at my lips."
                show samantha cowgirl orgasm creampie with vpunch
                "As I open my mouth to let her in, I flood inside of her and she loudly gasps."
                $ samantha.impregnate()
            else:
                "She leans down and licks at my lips."
                show samantha cowgirl orgasm creampie with vpunch
                "As I open my mouth to let her in, I flood inside the condom and she loudly gasps."
            with vpunch
            "We're both breathing heavily."
            hide samantha
            show samantha naked flirt at center, zoomAt(1.85, (640, 1240))
            with fade
            "Samantha lays on top of my chest and slowly raises herself off of me."
            "I see tears come to her eyes again and get worried."
            "My concern instantly disappears when she speaks."
            samantha.say "Thank you. Thank you for telling me about him."
            "I only pat her back in response."
            "We stay that way until her breath evens out and she's lightly snoring on top of me."
            "Feeling content, I close my eyes with her."
        "Take her":
            "Well, with that kind of permission, there was no way I was backing down."
            "I knew what I wanted."
            "I gripped her hips tightly and crawled on top of her."
            "I shove my clothes off the side of the bed."
            scene bg black
            show samantha missionary at center, zoomAt(1.3, (640, 930))
            "Sam's laid out on her back."
            if samantha.sub >= 50:
                samantha.say "Oh, [hero.name] - please, be gentle?"
            else:
                samantha.say "[hero.name], I want you inside of me!"
            "It's at times like this that I have to kind of mentally slap myself."
            "Because there's a part of me that would just stay right where I am."
            "Starting down at the sight of Sam, laid out naked in front of me."
            "Unable to actually believe that this is happening, that I get to do this with her!"
            "But that's not the kind of thinking that gets the job done."
            "So I direct my gaze downwards, glancing between Sam's thighs."
            "And the moment I do that, what I see does the trick."
            "That neat, perfect little pussy - that's what I want!"
            "Sam seals the deal a moment later, when she draws up her legs so that they part."
            "And at the same time she extends her arms, beckoning me to come to her."
            "Of course there's nothing that I want more in the world right now than to do that."
            "But I have to battle against my instinct to just thrown myself at her."
            "Because I don't want to come across as desperate - or to flatten her!"
            "And so I force myself to lie down slowly and gently atop her instead."
            show samantha missionary closedeyes
            "As I do so, Sam wraps her arms around me, pulling me closer still."
            "Somehow, while my mind is all over the place, we manage to pull it off perfectly."
            "By which I mean that we come together like two halves of a puzzle to form a whole."
            "Her limbs fold around me, and I wrap myself up in her too."
            "At the same time I can feel my manhood pressing against the lips of her sex."
            "Everything happening between us seems to be totally natural and instinctive."
            show samantha missionary normaleyes at center, traveling(1.0, 1.0, (640, 720))
            "And so when I begin to move, she matches my motions."
            "The head of my cock is already pressing against the lips of her pussy."
            "Every movement I make causing Sam to gasp at the sensation."
            "But there's no sense of me fumbling or struggling to know what to do next."
            "Instead I feel like I'm walking a linear, logical path that leads straight ahead."
            "With each pass, Sam yields a little more, relaxes just a fraction."
            "And I have to fight to keep from holding my breath every time."
            "Wondering if this is going to be the one that sees her open herself to me."
            "Soon the rhythm begins to take over, and I tune out just a little."
            "All of which means that when it does finally happen, I'm taken by surprise."
            hide samantha
            show samantha missionary cumeyes
            samantha.say "Oh..."
            samantha.say "Oh, [hero.name]..."
            mike.say "What the..."
            mike.say "Oh...oh fuck!"
            show samantha missionary closedeyes pussy at startle(0.05,-10)
            "My eyes are wide and my mouth hanging open as I sink into Sam."
            "And I'm so shocked that I must he half the way into her before I regain my senses."
            "Which is easier said than done, as what I'm feeling is almost overwhelming."
            "Suddenly I'm filling her up more with each passing second."
            "Feeling everything that I wanted being thrust upon me all at once."
            "Thankfully I'm soon as deep as I can possibly go."
            "That means I can stop and take stock of the situation."
            "But again my unconscious mind seems to be in a position to take over."
            "Because as soon as I pause, it rebels against me."
            "The animal in me doesn't want to stop and think - all it wants is Sam."
            "And now that I'm buried inside of her, it's not going to be denied!"
            "All of a sudden my muscles tense and my limbs start to move."
            show samantha missionary at startle(0.05,-10)
            "I rise up and then sink down again, repeating the action as soon as it's done."
            show samantha missionary at startle(0.05,-10)
            pause 0.2
            show samantha missionary at startle(0.05,-10)
            "And I'm picking up speed too, going faster with each passing second."
            "Sam doesn't seem to be aware of the fact that I've totally lost control of myself."
            show samantha missionary at startle(0.05,-10)
            pause 0.2
            show samantha missionary at startle(0.05,-10)
            "She just clings onto me the whole time, likely overwhelmed by what I'm doing."
            "I have no idea of just how long I'm capable of keeping up this kind of pace."
            show samantha missionary at startle(0.05,-10)
            pause 0.2
            show samantha missionary at startle(0.05,-10)
            "And I can't seem to keep track of how long I've already been at it either."
            "There's nothing but the act of making love to Sam, nothing else matters."
            show samantha missionary at startle(0.05,-10)
            pause 0.2
            show samantha missionary at startle(0.05,-10)
            "So I keep on going, pounding away until the pressure builds to breaking point."
            "Only then do I remember what comes next."
            show samantha missionary at startle(0.05,-10)
            pause 0.2
            show samantha missionary at startle(0.05,-10)
            mike.say "Oh shit..."
            mike.say "I'm...I'm gonna cum!"
            "I need to make sure I don't let go inside of Sam."
            "It's a pain, but we didn't bother to use a condom."
            show samantha missionary dickout
            "So I make sure to do it before the inevitable happens."
            show samantha missionary cumeyes cumshot ahegao with vpunch
            "Sam and I cum almost at the same moment, each affecting the other."
            show samantha missionary outside2 with vpunch
            "I feel her squeezing me tightly as I pull out of her."
            show samantha missionary outside with vpunch
            "And she's in the grips of her orgasm as I shoot my load over her belly."
            show samantha missionary closedeyes with vpunch
            "Luckily we're both laid down on the bed."
            "So we can easily collapse into a heap afterwards."
    $ samantha.sexperience += 1
    $ samantha.flags.cuck_ryan = True
    scene bg black with dissolve
    return

label samantha_event_A02:
    if samantha.love.max < 150:
        $ samantha.love.max = 150
    $ samantha.flags.nodate = False
    $ samantha.flags.nokiss = False
    $ samantha.flags.engaged = False
    show samantha happy with dissolve
    samantha.say "[hero.name]!"
    "Sam comes towards me from the counter, hanging up her apron."
    "She has a purse slung over her shoulder and a paper bag with the bakery logo plastered on the front in the other."
    "I smile nervously."
    mike.say "Hey."
    show samantha normal
    samantha.say "Don't look so nervous!"
    samantha.say "I have some news."
    mike.say "News?"
    samantha.say "Yup! Walk with me?"
    "I nod and stand up."
    "Pushing my chair in and grabbing my cup, I follow her out the door."
    scene bg mall1
    show samantha normal
    with fade
    "She's gripping tightly at the bakery bag and pursing her lips."
    "Was something wrong?"
    mike.say "What's up?"
    samantha.say "..."
    samantha.say "I broke up with Ryan."
    "My brain short circuits for a moment."
    "The guy she's been falling all over for the past who knows how many years is gone?"
    "Dropped?"
    samantha.say "Don't look at me like that!"
    samantha.say "I thought a lot about what you said."
    samantha.say "I asked Ryan about it when I got home."
    samantha.say "He tried to deny it at first, but when I said you had pictures he... fell apart."
    mike.say "I don't know what to say."
    mike.say "Are you okay?"
    samantha.say "I'm okay."
    samantha.say "Better than okay."
    show samantha annoyed
    samantha.say "I feel... angry- and upset."
    show samantha normal
    samantha.say "But I'm glad I found out."
    mike.say "You? Angry? How scary."
    with hpunch
    "She smacks me on the shoulder but gives me a smile."
    "I can tell she's still sad about the whole situation, but she's taking it better than I thought."
    "You know, after the whole mental breakdown part."
    samantha.say "I think I've made a decision."
    mike.say "Oh?"
    show samantha flirt
    samantha.say "I... I want to go on a date with you."
    "If I was short circuiting before, I was shutting down this time."
    "Was I hearing her right?"
    "There was no way."
    "She seemed to notice my speechlessness."
    show samantha normal blush
    samantha.say "You've always been there for me."
    samantha.say "You're honest, you spend time with me..."
    samantha.say "I really like you, [hero.name]."
    mike.say "I- I don't know what to say."
    show samantha surprised
    samantha.say "Oh! I'm sorry. Did I read things wrong?"
    menu:
        "Yes, I'd love to go out with you":
            $ samantha.love += 1
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake... I'd love to go on a date with you."
            else:
                mike.say "Sam... I'd love to go on a date with you."
            show samantha happy
            samantha.say "Really? Oh thank you!"
        "No, I don't see you that way":
            mike.say "I don't know if I like you like that."
            $ samantha.love -= 5
            mike.say "...I'm not sure about us."
            show samantha sad
            samantha.say "Oh. I understand. I'm sorry."
            "What am I doing... I can't do that to her..."
            show samantha normal
            mike.say "But I am willing to give it a try."
            return
    mike.say "What about Ryan?"
    mike.say "He's probably not going to accept it that easily."
    show samantha annoyed
    samantha.say "I don't care."
    samantha.say "No means no."
    show samantha normal
    samantha.say "He hasn't been home in a few days anyway."
    mike.say "..."
    mike.say "Maybe we can try. I'll go on a date with you."
    show samantha happy
    samantha.say "Really? Alright! Thank you! You won't regret it, I promise."
    "I knew I wouldn't."
    "Samantha was too sweet to make anyone regret anything- except making Ryan regret ever losing her."
    mike.say "Are you sure you're ready? That you've had enough time?"
    show samantha normal
    samantha.say "I think that the sooner I forget about Ryan, the better I'll feel."
    mike.say "Fair enough."
    show samantha happy
    samantha.say "Yay~! Let's go!"
    mike.say "What? Right now?"
    samantha.say "Yes, right now! I'm off work and you're free, right?"
    mike.say "Yeah."
    show samantha normal
    samantha.say "So, let's do it!"
    samantha.say "Who knows when the next time we'll both be free like this?"
    samantha.say "We both have work and I have university."
    samantha.say "It's a good time!"
    mike.say "Alright, then, let's go. Have a place in mind?"
    show samantha flirt
    samantha.say "Um... I'll admit, I didn't really think this through."
    samantha.say "I didn't think I'd make it this far."
    "She didn't think she'd make it this far? With me?"
    mike.say "That's okay. We can think of somewhere to go."
    show samantha normal
    samantha.say "Like where?"
    menu:
        "Movie Theatre":
            mike.say "We could watch a movie?"
            show samantha happy
            samantha.say "Ooh! Good idea! What's showing?"
            mike.say "I'm not too sure. Let's go and find out."
            scene bg black with timelaps
            scene bg cinema with timelaps
            "The theatre has a good crowd today."
            "A new movie must have come out that I didn't hear about."
            show samantha casual with dissolve
            samantha.say "I forgot! That new horror movie came out yesterday."
            mike.say "Want to see that? It has to be good with all these people around."
            show samantha sad
            samantha.say "Um... alright. We can see that one."
            "She looks a little pale, but I don't really register it until we're at the booth buying tickets."
            hide samantha
            show watch movie samantha blush
            with fade
            "We make our way to our seats and sit near the front."
            mike.say "Are you going to be okay? Should we see something else?"
            samantha.say "No! I'm okay. It's just a movie."
            "I can tell she's lying, but I can't help but admit that her denial is kind of cute."
            "After a few minutes of waiting, the previews begin. Boring trailers flash past the screen, only a few catching my attention."
            "The lights dim and the conversation dies down."
            "A typical horror movie title plasters itself in front of us."
            samantha.say "This doesn't sound too bad."
            "The movie has a slow start. A couple move into a house and slowly realize that it's haunted. It's nothing too exciting, but the first scare has Samantha jumping in her seat next to me."
            samantha.say "Oh my gosh!"
            "The film continues. Gore and blood flow not too soon after."
            "I look over; Samantha seems a little green in the face."
            "Her hands are gripping the arm rests."
            "I lay my hand on top of hers. She jolts in surprise for a moment but immediately relaxes, lacing her fingers with mine."
            "She takes to burying her face into my shoulder for the rest of the movie."
            "The credits roll."
            samantha.say "Is it over?"
            mike.say "Yeah. That scary?"
            samantha.say "... It wasn't scary."
            mike.say "Whatever you say. Let's head out."
            "Samantha nods and we stand up, filing out with the rest of the crowd. She hangs onto my arm until we get outside."
        "Shopping":
            samantha.say "Sure! I need to stop by the clothes store anyway, so good choice!"
            scene bg black with timelaps
            scene bg clothesshop
            show samantha casual
            with timelaps
            "By the time we get to the clothes store, Samantha already has a few other bags in her hands from stopping by the bookstore."
            "When we walk in, it's pretty empty, save for the clerk leaning boredly on the checkout counter."
            samantha.say "Hey!"
            mike.say "What?"
            samantha.say "You should choose something for me?"
            mike.say "Really? I don't have much of a fashion sense."
            samantha.say "Have some faith! I want to see what you come up with."
            show samantha happy at left with ease
            samantha.say "Don't take too long!"
            hide samantha with easeoutleft
            "With that, she goes to her own aisle in the female section, grabbing a shopping cart on the way."
            "Where should I even start?"
            $ renpy.dynamic("clothes_choice")
            menu:
                "Modest top":
                    "There's a red blouse hanging daintily on a featured shelf near the front."
                    "It's frilly with lace on the shoulders."
                    "It looks like it would fit her well."
                    $ clothes_choice = "modesttop"
                "Daring swimsuit":
                    "Making my way to the water area, swimsuits of all shapes and sizes cover the walls and racks."
                    "My eye catches a purple suit; very very daring, I don't know if any sane woman would wear it."
                    $ clothes_choice = "swimsuit"
                    "Maybe we could go swimming sometime."
                    "She probably already had something for it, but I couldn't help but think it would look good on her even if she wouldn't even think of wearing it."
                "Sexy top":
                    "There's a crop top with an open back, tying together at the bottom on one of the racks."
                    "Would Sam even wear something like that?"
                    "No point in not trying. Besides, if she didn't like it, she could just tell me to put it back."
                    $ clothes_choice = "sexytop"
            "I hold up my choice for Samantha to see once we meet up again."
            show samantha casual at left with easeinleft
            "Her cart is piled with jeans and shirts."
            show samantha surprised at center with ease
            samantha.say "Ooh~!"
            if clothes_choice == "modesttop":
                show samantha happy
                samantha.say "I can't believe you said you don't know fashion! This one is pretty!"
                $ samantha.love += 1
            elif clothes_choice == "swimsuit":
                samantha.say "I almost forgot!"
                show samantha happy
                samantha.say "I needed a new swimsuit."
                $ samantha.love += 1
                if not samantha.love >= 75 or not samantha.sub >= 25 or not hero.charm >= 50:
                    show samantha blush
                    samantha.say "But this one is a little bit too much."
                    show samantha normal
                    samantha.say "Anyway..."
                else:
                    show samantha flirt blush
                    samantha.say "If you think I would look good in it I might wear it, but it's showing a lot of skin..."
                    $ samantha.sub += 1
                    $ samantha.flags.sexyswimsuit = True
                show samantha normal
                samantha.say "We have to go swimming sometime."
                show samantha happy
                samantha.say "Thanks, [hero.name]!"
            elif clothes_choice == "sexytop":
                samantha.say "..."
                show samantha flirt
                samantha.say "I like it. And I'm sure you do too."
                "I almost miss the wink she throws me and promptly choke on air."
                $ samantha.sub += 1
            samantha.say "Alright, well I'm ready! Thank you so much for helping me out."
        "Restaurant" if 11 <= game.hour <= 13:
            mike.say "There's that restaurant down the street."
            samantha.say "As much as I love eating at the bakery, real food sounds like a good idea."
            mike.say "Heresy!"
            samantha.say "Shut up!"
            scene bg black with timelaps
            scene bg restaurant
            show samantha casual at center, zoomAt(1.5, (640, 1140))
            with timelaps
            "We're seated quickly at a nice table."
            "I'm glad we got here early; more people were already starting to file in."
            "We both order drinks and stare at the menu."
            mike.say "What are you getting?"
            samantha.say "Hmm."
            samantha.say "How about we order for each other! We can both try something new."
            mike.say "Oh. Sure."
            show samantha happy
            samantha.say "Yayy! Get something good!"
            show samantha normal
            "I look back down at the menu, but my mind suddenly goes blank. What would Sam want to eat?"
            menu:
                "Spaghetti":
                    "Seemed simple enough. Why not?"
                    "The waitress comes over and takes our order, a pad and pencil in hand. I order a plate of spaghetti for Samantha."
                    samantha.say "Can I get... the chicken casserole?"
                    show samantha happy
                    "Interesting. I don't think I've ever had that before. I shrug at her, but she smiles at me."
                    $ samantha.love += 1
                "Hamburger":
                    "everyone loves hamburgers, right?"
                    "The waitress comes over and takes our order, a pad and pencil in hand. I get an order of french fries and a hamburger for Samantha."
                    samantha.say "Can I get... the chicken casserole?"
                    show samantha happy
                    "Interesting. I don't think I've ever had that before. I shrug at her, but she gives me a warm grin."
                    samantha.say "Thanks, [hero.name]! I love some good comfort food."
                    $ samantha.sub += 1
                    $ samantha.love += 1
                "Salmon":
                    "I can't remember if she likes seafood or not. I know this restaurant doesn't make bad fish, so it wouldn't hurt to try."
                    "The waitress comes over and takes our order, a pad and pencil in hand. I order a platter of salmon for Samantha."
                    samantha.say "Can I get... the chicken casserole?"
                    show samantha sad
                    "Interesting. I don't think I've ever had that before. I shrug at her. She gives me a half-hearted smile- oops. Does she not like fish?"
            show samantha normal
            "Once our food comes out, we finish it quickly. My chicken casserole is good, but I don't think I'd get it regularly. The waitress comes over with the check and I pull out my wallet. As I lay down the cash, Sam snatches the bill and pull it to her chest."
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake-"
            else:
                mike.say "Sam-"
            show fx exclamation
            samantha.say "Half and half! At least!"
            "I sigh, but eventually give in when I realize that she wouldn't be giving it back until I agreed. Her expression is content when the waitress picks it up and thanks us for coming."
    scene bg street
    show samantha casual at center, zoomAt(1.5, (640, 1040))
    with fade
    "Samantha and I stand outside of her house."
    "There's no car in the driveway, so I assume Ryan's out doing... whatever he does with his time."
    "Walking her home was surprisingly comfortable despite the silence."
    "She insisted on holding my hand the whole way here."
    show samantha happy
    samantha.say "That was fun!"
    mike.say "Yeah, it was."
    samantha.say "We should do that more often."
    show samantha normal
    samantha.say "..."
    samantha.say "Thanks, [hero.name]."
    mike.say "Hm? For what?"
    samantha.say "For being here."
    samantha.say "And coming out with me today."
    samantha.say "I was nervous that you would say no."
    show samantha flirt blush
    samantha.say "I... really like you, [hero.name]."
    show samantha at center, zoomAt(2.0, (640, 1340))
    "Suddenly, her eyelids are fluttering and she's leaning in."
    "This was... strange."
    "But I liked it."
    "I didn't know what I was waiting for."
    "My long time crush was finally accepting me."
    "I close the distance."
    hide samantha
    show samantha kiss
    with dissolve
    $ samantha.flags.kiss += 1
    "Her lips are as plump and soft as they look."
    "My hand rests on her hip and I feel her arms wrap around my neck."
    "It only lasts for a few seconds, but it's enough for Sam's face to go completely red."
    "I probably look the same."
    hide samantha
    show samantha casual blush
    with dissolve
    samantha.say "I'll see you later, [hero.name]."
    "My head is fuzzy- christ, how old am I? I'm acting like a kid, dizzy from romance. I manage to raise my hand and wave."
    mike.say "See ya."
    "She giggles and gives me one more peck, this time on the cheek."
    hide samantha with moveoutleft
    "The next thing I know, I'm standing alone on her porch, staring at the closed door in front of me."
    $ game.room = "street"
    return

label samantha_event_A03:
    if samantha.love.max < 170:
        $ samantha.love.max = 170
    "I was sure that the only thing holding Sam and I back was the fact she still hadn't broken things off with Ryan."
    "We'd actually managed to talk about it, me broaching the subject and her reluctantly opening up about it."
    "And so when she followed through, officially letting Ryan know that their marriage was over, I couldn't have been happier."
    "But it didn't take long for me to realise that the changes I'd imagined had not begun to materialise."
    "Don't get me wrong - it's not like Sam suddenly went cold on me, or that our relationship started to suffer."
    "It was just that we seemed to keep on going pretty much as we had before she left Ryan and we became an actual couple."
    "This means that when she actually does look me square in the eye, letting me know she wants to talk, I assume the worst."
    show samantha blush with dissolve
    samantha.say "[hero.name]..."
    if samantha.flags.nickname == "cupcake":
        mike.say "Uh, yeah, Cupcake?"
    else:
        mike.say "Uh, yeah, Sam?"
    samantha.say "I have something that I want to tell you."
    samantha.say "Kind of a confession, I guess."
    "At that moment, it feels like someone just reached into my chest and grabbed hold of my heart."
    "All I can think is that Sam's about to tell me the worst possible thing that I can imagine."
    "I picture her telling me that it's just not working out the way that she thought it would between us."
    "Or that she's realised that, in spite of all the shit he did behind her back, she really did love Ryan after all."
    "There's a million things that I want to say in that moment."
    "I could beg, plead or argue before she has the chance to say another word."
    "But instead I bite down on my irrational panic, nodding for her to go on."
    if samantha.flags.nickname == "cupcake":
        mike.say "Ah...okay, Cupcake."
    else:
        mike.say "Ah...okay, Sam."
    mike.say "That sounds...kind of dramatic!"
    samantha.say "Yeah, I guess it kind of does!"
    show samantha close sad
    samantha.say "But then I do have something important to say to you."
    mike.say "I thought you might..."
    "Sam gives me a nervous smile, which does little to help assuage my fears."
    samantha.say "Well, here goes nothing!"
    samantha.say "You remember when you kind of called me out on still wearing my wedding ring?"
    "I nod, already dreading where she's going with this."
    samantha.say "I still had so much stuff to work through in my head, you know?"
    samantha.say "For so long I thought that it was normal, the way Ryan and I were as a couple."
    samantha.say "It was only when you opened my eyes to what he really was that I realised..."
    samantha.say "I realised that I'd been fooling myself for so damn long."
    samantha.say "That I'd been such a fool, let him use me all the time we were together."
    "Now I find myself shaking my head, disagreeing with Sam's low opinion of herself."
    if samantha.flags.nickname == "cupcake":
        mike.say "Don't say that, Cupcake."
    else:
        mike.say "Don't say that, Sam."
    mike.say "He's a manipulative jerk!"
    mike.say "What happened was no way your fault."
    show samantha happy
    "Sam laughs and smiles at me, shaking her own head a little too."
    samantha.say "Oh, [hero.name]."
    samantha.say "Sometimes I think you'd swear black was white for my sake!"
    show samantha normal
    samantha.say "You know as well as I do that it takes two people for something like that to work."
    samantha.say "But you were the one that showed me how wrong I was."
    samantha.say "You made me start questioning it all."
    mike.say "So..."
    if samantha.flags.nickname == "cupcake":
        mike.say "So why did it take so long, Cupcake?"
    else:
        mike.say "So why did it take so long, Sam?"
    "Sam sighs wearily at this, shrugging as she does so."
    samantha.say "I don't know, [hero.name]."
    samantha.say "I guess that it just took me some time to realise how wrong it all was."
    samantha.say "Well, that and the fact I had something else to deal with too."
    "My eyebrows shoot up at this, and I can't hide my sudden interest."
    if samantha.flags.nickname == "cupcake":
        mike.say "Wha...what was that, Cupcake?"
    else:
        mike.say "Wha...what was that, Sam?"
    show samantha happy
    "Now Sam gives me a little smile and a laugh, looking away a little as she does so."
    "It's one of those casual gestures that she does out of habit, maybe even without knowing."
    "But it's always been something that makes her look absolutely irresistible to me."
    "Somehow it just lights her face up in the most perfect way imaginable."
    show samantha normal
    samantha.say "Haven't you guessed by now, [hero.name]?"
    samantha.say "I was discovering what I had with Ryan wasn't really love."
    samantha.say "And it was because you were showing me the real thing at the same time!"
    "Sam looks me straight in the eye as she says this."
    "And her words hit me we what feels like actual physical force."
    mike.say "Y...you...you mean?!?"
    show samantha flirt blush
    samantha.say "Yes, [hero.name] - I love you!"
    samantha.say "I'd have told you sooner, really I would."
    samantha.say "But I was worried that I wasn't ready, that I didn't have my head together - you know?"
    if samantha.flags.nickname == "cupcake":
        mike.say "It...it's okay, Cupcake...it's okay!"
    else:
        mike.say "It...it's okay, Sam...it's okay!"
    mike.say "It was...it was worth waiting for!"
    show samantha happy
    "Sam laughs again, clearly amused by the dramatic nature of my reaction."
    samantha.say "Wow, [hero.name]."
    samantha.say "I thought I was the one that was going to end up an emotional mess!"
    samantha.say "Would this help?"
    show samantha kiss with dissolve
    $ samantha.flags.kiss += 1
    "And with that, Sam leans in and presses her lips to mine."
    "The moment she does so, I can feel the tension and worry draining out of my body."
    "And as the kiss becomes ever more intense, it's replaced by a relaxed sensation of delight."
    "I did it!"
    "I managed to save my friend from being married to a jerk and I won the heart of the girl of my dreams."
    "And all at the same time, thanks to them being less than one person!"
    return

label samantha_event_A04:
    if samantha.love.max < 200:
        $ samantha.love.max = 200
    "I should have known that it was too good to last - this golden age of having Sam all to myself without any complications."
    "I guess I was just so tied up in the thrill of finally getting the girl that I always wanted."
    "Too busy thinking that it meant I could do no wrong and not paying attention to what was happening right under my nose."
    "I mean, it's my own fault, I know that now."
    "How could I think that I was going to get away with something like that?"
    "I should have had an excuse ready for this moment, been able to explain myself."
    "But when Sam asks me the inevitable question, I'm totally unprepared."
    show samantha
    samantha.say "[hero.name], I need to ask you something."
    if samantha.flags.nickname == "cupcake":
        mike.say "Erm, okay, Cupcake."
    else:
        mike.say "Erm, okay, Sam."
    mike.say "What is it?"
    show samantha blush
    samantha.say "You've been really furtive with your phone since we started dating."
    samantha.say "Like you never leave it unlocked around me or let me see your texts."
    mike.say "Ah...well..."
    mike.say "That's just work stuff, you know?"
    mike.say "I have to keep it under wraps."
    mike.say "And it's pretty boring anyway."
    show samantha annoyed
    "Sam looks at me sideways."
    "She nods, but her expression says she's not buying it."
    samantha.say "Yeah, I suppose."
    samantha.say "But I could have sworn you called me by another name the other day."
    samantha.say "[hero.name], be honest with me, okay?"
    show fx question
    samantha.say "Are you seeing other girls behind my back?"
    "I try my best not to look like I've been put on the spot by the question."
    "But I can already feel myself starting to sweat."
    "What do I tell her?"
    "Do I admit that I've been cheating on her and accept the consequences?"
    "Or do I laugh it off and start lying through my teeth?"
    menu:
        "I admit." if samantha.sub < 75:
            "I can't do it."
            "I just can't lie to Sam."
            "It'd be the easier option, sure."
            "But then I'd be just as bad as that jerk Ryan."
            if samantha.flags.nickname == "cupcake":
                mike.say "Okay, Cupcake, you got me."
            else:
                mike.say "Okay, Sam, you got me."
            mike.say "It's nothing serious, but I have kinda been seeing other girls."
            show samantha normal
            "Sam looks at me, nodding her head slowly."
            "I was expecting her to explode and dump me in a second."
            "But instead she actually looks like she's relieved!"
            if samantha.flags.nickname == "cupcake":
                mike.say "I...I get it if you want to end it, Cupcake."
            else:
                mike.say "I...I get it if you want to end it, Sam."
            mike.say "And for what it's worth, I'm sorry, yeah?"
            show samantha sad
            samantha.say "It's not what I wanted to hear, [hero.name]."
            samantha.say "That's for sure!"
            mike.say "But..."
            show samantha annoyed
            samantha.say "But we didn't get started under the best circumstances, now did we?"
            samantha.say "Everything just kind of happened in a crazy rush."
            samantha.say "And I don't recall sitting down and laying out the ground rules either!"
            mike.say "So you...don't want to dump me?"
            show samantha normal
            "Sam nods at this, beginning to smile a little."
            samantha.say "No, I just want you to stop seeing other people, that's all."
            samantha.say "If being with Ryan taught me one thing, it's that people are never perfect."
            samantha.say "But you just did something that Ryan would never have done, [hero.name]."
            samantha.say "You told me the truth and you said sorry."
            samantha.say "And that means I know you care for me."
            if samantha.flags.nickname == "cupcake":
                mike.say "I...I do, Cupcake."
            else:
                mike.say "I...I do, Sam."
            mike.say "Honestly, I do."
            samantha.say "Knowing that means I can give you another chance."
            show fx question
            samantha.say "Just promise me that you'll be faithful, that's all?"
            menu:
                "I will be faithful.":
                    if samantha.flags.nickname == "cupcake":
                        mike.say "I promise, Cupcake."
                    else:
                        mike.say "I promise, Sam."
                    mike.say "From now on, we're totally exclusive."
                    show samantha happy
                    "Sam nods happily and plants a kiss on my cheek."
                    samantha.say "That's all I need to hear!"
                    $ samantha.set_girlfriend()
                "I can't promise.":
                    if samantha.flags.nickname == "cupcake":
                        mike.say "I am sorry Cupcake."
                    else:
                        mike.say "I am sorry Sam."
                    mike.say "I don't know if I'm committed enough to promise you to be faithful."
                    show samantha sad
                    samantha.say "That's too bad."
                    samantha.say "It was hard enough when I learned about Ryan. I can't be fooled again."
                    samantha.say "Goodbye [hero.name]."
                    hide samantha with dissolve
                    "And with that, she's gone."
                    $ samantha.set_gone_forever()
        "I admit." if samantha.sub >= 75:
            "There's no way I can lie to Sam."
            "Even if it means that she ends up dumping me."
            "That way I'd be no better than Ryan."
            "I'd be just another cheating liar!"
            if samantha.flags.nickname == "cupcake":
                mike.say "I can't lie to you, Cupcake."
            else:
                mike.say "I can't lie to you, Sam."
            mike.say "There have been some dates with other girls since we got together."
            "I keep expecting Sam to blow her top at any moment."
            "I think maybe she's going to lash out and hit me or something."
            show samantha normal
            "But instead I see that she's actually nodding, looking almost relieved."
            mike.say "Ar...aren't you mad?"
            mike.say "I thought you'd want to kill me!"
            show samantha happy at center, vshake
            "Sam takes me by surprise then, actually bursting into peals of laughter."
            "It's so loud and sudden that I can't help thinking she might be going crazy."
            samantha.say "Oh, god no, [hero.name]!"
            show samantha normal
            samantha.say "After all, we were going behind Ryan's back when this thing got started."
            samantha.say "And I'm not a fucking hypocrite!"
            mike.say "Then...you...don't want to break up with me?"
            samantha.say "No, [hero.name], just for you to be honest with me."
            show samantha annoyed
            samantha.say "You see, I used to think the worst thing that Ryan did was fuck other girls."
            samantha.say "But what we did together made me realise it was the lying that was worse."
            show samantha normal
            samantha.say "So just promise that you'll be honest with me in future, yeah?"
            samantha.say "If you fuck someone else, tell me all about it."
            show samantha flirt blush
            samantha.say "Who knows - I might like the sound of it too!"
            "I nod silently, more than a little stunned at what Sam just said."
            "Am I actually asleep and dreaming right now?"
            "Because it sure as hell sounded like she said I was okay to fuck around."
            "That I can screw whoever I like, so long as she knows all about it!"
            "When I finally manage to respond, I try my best to sound all cool and collected."
            if samantha.flags.nickname == "cupcake":
                mike.say "Yeah, Cupcake, whatever you say."
            else:
                mike.say "Yeah, Sam, whatever you say."
            mike.say "I mean, if that's what you want."
            mike.say "I guess we could make it work!"
            show samantha happy
            "The smile on Sam's face tells me that she sees straight through me."
            "But she nods all the same, planting a kiss on my cheek."
            samantha.say "That's all I need to hear!"
            $ samantha.flags.nonexclusive = True
            $ game.flags.ongoinghomeharem = "samantha"
        "You're the only one Sam.":
            "There's no way I can do it."
            "I can't possibly tell Sam the truth!"
            "Not after how long it took get where we are right now."
            "If she finds out that I'm as much of a cheating scumbag as Ryan ever was..."
            "No, the only choice is to lie through my teeth and hope she believes me!"
            if samantha.flags.nickname == "cupcake":
                mike.say "No way, Cupcake!"
            else:
                mike.say "No way, Sam!"
            mike.say "Don't even think that."
            "Sam's eyes narrow as I begin lying to her."
            "And she crosses her arms over her chest."
            show fx question
            samantha.say "Well what's going on then?"
            samantha.say "And you'd better make this a good explanation."
            show fx exclamation
            samantha.say "Because Ryan lied all the time, and look where that got him!"
            "Yeah, sure, Sam - you were clueless until I put the evidence under your nose!"
            "I don't know where the thought comes from, but there it is."
            "How dare she lecture me about telling the truth?"
            "Especially when she lived a lie with that guy for so long."
            "And then she was the one that wanted to pay him back in kind too!"
            "But I can't throw all of that in her face, so I take a different course."
            if samantha.flags.nickname == "cupcake":
                mike.say "This isn't about me at all, is it, Cupcake?"
            else:
                mike.say "This isn't about me at all, is it, Sam?"
            mike.say "This is about Ryan and how he hurt you."
            show samantha surprised
            show fx question
            samantha.say "Wh...what do you mean?"
            mike.say "You trusted Ryan, and he betrayed you."
            mike.say "It's only natural that you'd worry I might do the same."
            mike.say "But it's okay, I forgive you."
            show samantha sad
            "Sam shakes her head, looking confuses as my words sink in."
            samantha.say "No...no, that's not right..."
            samantha.say "But...maybe you do have a point, [hero.name]."
            samantha.say "I guess I never thought about it that way!"
            "I know I'm gas-lighting her, but it seems to be working."
            "I nod and smile, encouraging her in that thought."
            show samantha normal
            "Sam nods too, and plants a kiss on my cheek."
            samantha.say "That's all I need to hear!"
            $ samantha.set_girlfriend()
    return

label samantha_wedding_flag:
    if "samantha_event_05" not in DONE:
        $ renpy.dynamic("wedding_day")
        $ wedding_day = game.calendar.get_next_day_of_week("sunday")
        $ hero.calendar.add(wedding_day, LabelAppointment((12, 20), "samantha", "Sam and Ryan's wedding", "samantha_event_B01"))
    return


label samantha_event_B01(appointment=None):
    if samantha.love.max < 120:
        $ samantha.love.max = 120
    "Time to go to Sam and Ryan's wedding."
    scene bg church wedding with fade
    "Church bells ring loudly, piercing my ears as if they personally wanted to shame me."
    "Samantha's wedding day came quickly- much too quickly."
    if hero.flags.knows_ryancheats:
        "I can't stop thinking about Ryan."
        "He was a lying cheat, but I didn't say anything."
        "But, this was for the best, right?"
        "Sam is happy and that's all that matters to me."
    "Girl" "Oh my gosh! [hero.name], is that really you?"
    show natalie date with dissolve
    "I turn to see one of Samantha's friends, dressed up in the requested colours."
    "She looked familiar, but I only could bring up vague memories."
    "Girl" "I haven't seen you since ages! How have you been?"
    mike.say "Uh... great."
    "I was great."
    "Fantastic."
    show natalie happy
    "Girl" "Good!"
    "Girl" "Can you believe those two are finally getting married?"
    "Girl" "It seems like only yesterday that they were fawning over each other in first year."
    menu:
        "Support":
            mike.say "Yeah."
            "Sam looks really happy."
            mike.say "She's been waiting for this for a long time."
            "She swoons at me, like I'm the one getting married."
            "Girl" "They're so sweet!"
        "Oppose":
            mike.say "Don't you think they're going a little fast?"
            mike.say "They're way too young to be getting into something so serious."
            show natalie normal
            "Girl" "What!?"
            "Girl" "If anyone should get married on the spot, it's them!"
            show natalie happy
            "Girl" "Ryan is the perfect man for her, loving, sweet... he'll give her everything she needs."
            "Ouch."
    "Girl" "I saw Sam's dress earlier."
    "Girl" "She is a goddess!"
    "Girl" "Ryan's got it good."
    mike.say "Oh. Are you a bridesmaid?"
    "Girl" "Yup!"
    "Girl" "I couldn't even think of turning her down when she asked me."
    "To be honest, I was kind of assuming she would ask me to have some sort of role, too. Ryan probably had something to do with it."
    mike.say "... Sounds nice."
    show natalie normal
    "Girl" "I heard you three lived together for a while."
    "She leaned in like she was telling a secret."
    "Girl" "It wasn't too loud was it?"
    "Why the hell was everyone so straightforward with this kind of thing?"
    mike.say "Wha-?! No!"
    show natalie happy
    "Girl" "They totally were!"
    "I groan, looking around for other people to talk to."
    "Everyone else is engaged in conversation, excited about the couple to be."
    "Guess this is what I'm stuck with."
    menu:
        "Ask about their friendship":
            "How long have you known Samantha?"
            show natalie normal
            "Girl" "Hmm... since middle school, I think."
            "Girl" "I met her in social studies."
            "Girl" "I was out sick for a long time, and she helped me catch up, best friends ever since!"
            mike.say "Sounds like something she would do."
            mike.say "She's a sweet girl."
            show natalie happy
            "Girl" "Ha! In more ways than one."
            "Girl" "That girl has a strong sweet tooth."
            mike.say "Yeah- she doesn't work at the bakery for nothing."
            mike.say "Sometimes I think she'd even work there if they paid her in desserts."
            "Girl" "Or just cinnamon rolls."
            "Girl" "I remember she brought one for lunch everyday."
            "Girl" "Then her mom wouldn't let her anymore because she'd always come home with a sugar rush."
            "Girl" "Sam was so cute!"
        "Ask about the decoration":
            mike.say "Did someone help her plan this whole thing?"
            if hero.flags.knows_ryancheats:
                mike.say "Ryan couldn't have been very helpful. He's always- ... working."
                "I try not to choke on the last word."
            "Girl" "I did!"
            show natalie normal
            "Girl" "At least, I was one of them."
            "Girl" "Samantha's mom helped her through a lot of it."
            mike.say "That's good."
            "Girl" "Yeah! But I have to say, we didn't do much."
            "Girl" "We just opened up some doors that led her to the prize!"
            show natalie happy
            "Girl" "I absolutely love the colours she chose."
            "Girl" "And the absolutely fit her too."
            "I take a good look around- the church is decorated in white and royal gold colours."
            "It's simple, but stands out."
            "The colours are classy, but the rest of the decorations that I managed to spot in the reception hall when I came in were pretty tame."
            mike.say "I think it matches her really well."
        "Ask about the food":
            mike.say "Do you know what food they'll be serving."
            "Girl" "Of course, that girl chose the sweetest items on the menu."
            "Girl" "Duck with chocolate sauce, mashed potatoes, and salad."
            show natalie normal
            "Girl" "But, between you and me, I'm pretty sure Ryan talked her into that last one."
            mike.say "Chocolate sauce?"
            "Girl" "Yep. Weird, but the fanciest sweet thing she could find."
            "Girl" "And trust me, she looked over that menu for hours."
            show natalie happy
            "Girl" "She really wants everything to be perfect."
    mike.say "Do you know what time everything starts?"
    "She looks down at the watch on her wrist and hums."
    "Girl" "Should be starting really soon."
    "Girl" "We'll need to find our seats."
    "Not a moment after, a man wearing religious clothes gets our attention, telling us to get ready."
    hide natalie with dissolve
    "I get to my seat easily."
    "Samantha's friend, whatever her name was, rushes outside, hooking her arm around a groomsman who I can't get a good look at before the doors close."
    "Ryan stands at the front, hands twitching nervously, but he has a wide grin on his face."
    "If I didn't know better, I would call it a blatant smirk, but I push the thought as far back in my mind as I can."
    "It's loud in the hall for a long moment, before it quiets down and piano music fills the space."
    "I hold my breath."
    "Why did I come here?"
    "There was no way I could watch this."
    "What was I thinking?"
    "Before I could get up and bolt, pairs start walking through elegantly to the front."
    "I can feel something building in my chest."
    "Guilt? Regret? I couldn't tell."
    "The music sounds broken in my ears."
    "Was the pianist feeling okay?"
    "I quickly glance around."
    "No one else seems bothered."
    "Was I feeling okay?"
    "My heart jumps in my throat when the tune changes and the doors open wide."
    "The crowd turns back to see the bride: Samantha."
    show samantha wedding blush with dissolve
    "I try not to look."
    "I fail."
    "I have to stop myself from gasping."
    "She's wearing a gorgeous short white dress, very simple but incredibly classy."
    "My eyes follow her down the aisle."
    "She catches my eye."
    "She gives me a smile full of hope and innocence."
    "My lips struggle for a moment."
    menu:
        "Smile Back":
            "I force my mouth to twitch up in a smile, giving her a quick thumbs up."
            "Her eyes twinkle."
            $ samantha.love += 1
        "Look Away":
            "I quickly look away, focusing my attention on the bridesmaids."
            "I can barely look at her without feeling guilty."
            "The priest began speaking, filtering half heartedly through my ears."
            "It felt like I was watching this through someone else's perspective."
            "..."
    "Vows are being said."
    "Samantha looks teary eyed."
    samantha.say "Ryan~"
    "She chokes and grabs his hands, lacing their fingers together."
    samantha.say "I've felt connected to you ever since I saw you."
    samantha.say "When I met you in first year, I knew I wanted to be with you forever."
    samantha.say "You've treated me with more love and kindness than I deserve."
    samantha.say "I can only hope that I can repay you someday."
    "Oh, Samantha."
    "You deserve so much more than you think."
    "Before I knew it, they're kissing."
    "People are clapping and whistling in the seats next to me."
    "At least she was happy."
    scene bg black with timelaps
    scene bg restaurant with timelaps
    "I'm sitting at one of the many circular tables in the hall, a ceramic plate in front of me with a slab of duck covered in a brown sauce- I suppose that's the chocolate."
    "People are dancing at the middle of the floor."
    "The music keeps switching between upbeat pop and rock music."
    "A strange combination."
    "I couldn't tell where Sam was at this point."
    "She had immediately gone to dance with Ryan once formalities were done with."
    "What should I do now..."
    $ BATHROOM = False
    menu:
        "Go for a walk" if hero.flags.knows_ryancheats:
            $ samantha.flags.knows_ryancheats = True
            "As much as I told myself that I was skulking around on the landing of the metal fire escape at the back of the wedding venue to get some fresh air, I knew I wasn't even fooling myself."
            "Even the excuse of needing to sneak a cigarette would have been enough to make me able to accept my own logic."
            "But as it was, all I could do was admit to myself that I really didn't want to be here in the first place."
            "And that I was trying to spend as little time around the other guests as I could possibly manage."
            "And who was I to Sam and Ryan anyway?"
            "Nothing but a former housemate that they'd probably invited as an afterthought."
            "The fact that I hated his guts and still kind of held a torch for her was my concern alone."
            "Even if the jerk had been cheating on her, right up to the so-called big day - this was still the start of a new life for them."
            "The last thing they'd want was me hanging around, with the stench of the past all over me."
            "I was just trying to pull myself together and walk back into the building, when I heard the sound of the door behind me suddenly opening."
            show samantha wedding sad with dissolve
            "I confess that I jumped a little, but then the figure that came rushing out onto the small landing wasn't in any greatly composed state either."
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake...what in the hell are you doing out here?"
            else:
                mike.say "Sam...what in the hell are you doing out here?"
            "She looks edgy and more than a little dishevelled, streaks and smudges in her make-up give tell-tale hints that she's recently been crying."
            "But that's not as notable as the fact that she's already in her wedding dress, hair all done up for the ceremony."
            "At times like this, I always feel that I should be a million miles away from selfish thoughts of a carnal nature."
            "But god, Samantha looks beautiful in that dress."
            mike.say "Isn't the dinner about to start?"
            "I hate to say this one, but..."
            mike.say "Won't Ryan be worried where you are?"
            "Samantha looks at me for a moment, as though she doesn't quite recognise me or understand what I'm saying."
            "Then she shakes her head and seems to come back into the moment."
            show samantha angry
            samantha.say "Fuck the wedding...and fuck Ryan too!"
            show samantha happy
            "She realises the irony of her last statement, and begins to laugh almost crazily."
            show samantha wedding cry
            "But after only a couple of seconds, the laughs turn into sobs, and she throws her arms around my neck."
            show samantha wedding at center, zoomAt(1.5, (640, 1040)) with hpunch
            "I return the embrace, a little more slowly, but with genuine conviction and sympathy."
            samantha.say "Oh, [hero.name]...is it true?"
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake, I really wish I could say it wasn't...but it is."
            else:
                mike.say "Sam, I really wish I could say it wasn't...but it is."
            samantha.say "Bastard..."
            "She hisses the word into my shoulder bitterly."
            "I should be thinking about Sam right now..."
            "Well, I am - but..."
            "I really should be feeling sorry for her and trying to be a good friend in her time of need."
            "Instead, all I can think of is how good she feels against me...how amazing the scent of her hair smells..."
            "After maybe a minute of us holding each other, she lifts her head and regards me."
            show samantha wedding sad
            "She's looking at me with those huge, slumberous blue eyes and long lashes now."
            samantha.say "[hero.name]...you'd never do that to me, would you...not if you loved me?"
            samantha.say "Please, I just need to know that it's not me..."
            samantha.say "That not all guys are like him..."
            "I'm only human, and I can't say what I'd do were the circumstances putting me in Ryan's place."
            "But that's not the kind of harsh honesty Sam needs right now."
            if samantha.flags.nickname == "cupcake":
                mike.say "It's not you, Cupcake - any man would be crazy to do that to you."
            else:
                mike.say "It's not you, Sam - any man would be crazy to do that to you."
            mike.say "He's just a scumbag...and he doesn't realise how lucky he is to have you."
            show samantha normal
            "Samantha smiles weakly through her tears, clearly cheered by what I've said."
            samantha.say "Thank you, [hero.name]...I feel so gutted by all of this...I guess I just needed to talk to a friend."
            "Yeah, because that's all I've ever wanted to be - the friend, the shoulder to cry on!"
            hide samantha
            show samantha close wedding flirt blush
            samantha.say "You've always been a good friend to me, [hero.name]."
            "What's this now?"
            "I hear a subtle change in the tone of Sam's voice, as though she were pulling herself together and seeing things from a new angle all of a sudden."
            samantha.say "A really good friend...and I haven't ever returned the favour...not really..."
            "Were still almost embracing at this point, and rather than backing off, Sam instead presses herself closer against me."
            samantha.say "Maybe I could change all that...starting right now?"
            "Oh shit - I can feel her hand on my crotch!"
            menu:
                "Push her back":
                    if samantha.flags.nickname == "cupcake":
                        mike.say "Cupcake, think about this - are you really being sensible here?"
                    else:
                        mike.say "Sam, think about this - are you really being sensible here?"
                    samantha.say "He fucked another woman behind my back, [hero.name]."
                    samantha.say "And he was just going to marry me without telling me that!"
                    "I can sense the venom creeping into her voice now, the anger that she's been suppressing at what Ryan did behind her back."
                    samantha.say "If he can do that, then why can't I?!?"
                    if samantha.flags.nickname == "cupcake":
                        mike.say "You're not seeing things clearly right now, Cupcake..."
                    else:
                        mike.say "You're not seeing things clearly right now, Sam..."
                    samantha.say "What's the matter, [hero.name]...don't you like what's on offer?"
                    samantha.say "Didn't you ever look at me back then and wonder what it'd be like to fuck me?"
                    "Hell - why do girls only talk to me like this when I'm trying to be the good guy?"
                    if samantha.flags.nickname == "cupcake":
                        mike.say "Cupcake, I'd be lying if I said no to that."
                    else:
                        mike.say "Sam, I'd be lying if I said no to that."
                    mike.say "If you'd asked me that before, I'd have said yes in an instant."
                    mike.say "I still would - if you weren't about to get married..."
                    "Sam's embrace loosens a little, as some of the intensity leaves her eyes to be replaced by sadness."
                    if samantha.flags.nickname == "cupcake":
                        mike.say "Please, Cupcake - if we ever do have a chance...not like this, don't let it be like this!"
                    else:
                        mike.say "Please, Sam - if we ever do have a chance...not like this, don't let it be like this!"
                    mike.say "If you turn me into the same kind of guy as Ryan - how long will it be before you hate me like you do him?"
                    samantha.say "Oh, [hero.name]...you're too good for your own good."
                    samantha.say "And you're probably too good for me too!"
                    "Oh yeah, I'm a goddamn saint!"
                    "The patron saint of talking himself out of a sure thing!"
                    $ samantha.flags.nokiss = False
                    $ samantha.flags.nodate = False
                "Accept Samantha":
                    "What the hell?"
                    "Maybe, under the circumstances, it's the best thing for her to do?"
                    "Then she can go through with this whole fucking charade at least knowing that she got one back on the prick."
                    "Honestly, how selfless am I?"
                    if samantha.flags.nickname == "cupcake":
                        mike.say "Cupcake...it'd be my pleasure to let you!"
                    else:
                        mike.say "Sam...it'd be my pleasure to let you!"
                    "Sam's eyes flash at this, and her smile is so wicked that it's almost enough to get me hard all on its own."
                    "A moment later, she's gathering up the skirts of her dress and kneeling down on the landing in front of me."
                    "I catch a glimpse of white stockings and garters, and it reminds me of just how astonishing Sam's body happens to be."
                    "Sam opens my flies and pulls out my dick like a woman on a mission, grinning and shooting me glances as she does so."
                    "I can see from her expression just how much she's getting off on playing the part of the bad girl right now."
                    "And her enthusiasm is certainly infectious."
                    "I'm hard before she has my cock anywhere near her mouth, and she gives me one last look before she begins."
                    hide samantha
                    show samantha bj2 lick
                    with fade
                    "The look is one that says this was inevitable, that we were always destined to do something like this, when the time was right."
                    "I can't say I feel the same, or that I ever thought this would happen."
                    show samantha bj2 lick wet
                    "Sure, I imagined it - but I never expected to be doing this with Sam."
                    "Especially on her wedding day, mere minutes after the ceremony!"
                    show samantha bj2 suck
                    "She closes her lips around the head of my cock and begins to caress it with her tongue."
                    "I can feel her teeth almost as much as her lips and tongue, and she's trying to make up for her unease with enthusiasm."
                    show samantha bj2 suck closed
                    "It's not the best blowjob I've ever had, and Sam's technique leaves a lot to be desired."
                    "But on the flip side, I'm getting oral from a girl that I thought was going to be out of my life forever, and with an utter prick too."
                    show samantha bj2 suck open2
                    "Not to mention the fact that I'm actually getting blown by the bride right after she took her wedding vows!"
                    "And those factors more than make up for it."
                    "In the end, it's more the sight of her down there and the knowledge of what's behind all of this that makes me cum."
                    "Rather than Sam's willing, but not very stellar abilities."
                    show samantha bj2 suck cum with hpunch
                    "I lose myself in her mouth, watching her struggle to keep from spitting out my cum and keep from swallowing it on instinct."
                    with hpunch
                    "At first I can't imagine why she seems to be holding it in her mouth, almost gargling with it."
                    show samantha bj2 suck cum tits with hpunch
                    "But then, as the remainder of it slips down her throat, she notes my puzzled expression and smiles again."
                    hide samantha
                    show samantha bj2 tits
                    samantha.say "I want you to be on my lips when he kisses me."
                    samantha.say "I want to pay him back by having his bride taste of another man's cum!"
                    mike.say "What can I say - I can't think of a more deserving guy!"
                    $ samantha.flags.cuck_ryan = True
                    $ samantha.flags.nokiss = False
                    hide samantha
            show samantha wedding
            with fade
            "With that, Sam straightens out her dress and gives me a wan smile."
            samantha.say "Wish me luck, [hero.name]?"
            if samantha.flags.nickname == "cupcake":
                mike.say "Good luck, Cupcake."
            else:
                mike.say "Good luck, Sam."
            "I don't say it, but I mentally add 'you're going to need it'."
        "Go to the bathroom":
            $ BATHROOM = True
            "I stand up to go to the bathroom."
            "I could really use some time to myself- freshen up a little."
            "The restroom is down the hall from my table, so it's a short walk."
            scene bg publicbathroom with fade
            "When I swing open the door with the typical men's logo on it, I'm grateful that it's empty."
            "Standing in front of the mirror, I stare at myself, shifting left and right."
            "The bags under my eyes compliment my suit well. After all, I can't exactly afford a tailored one at the moment, and I'm pretty sure this is the only time I'll be using it- so, it's rented."
            "It looks slightly worn, but it's not too bad. Not in my opinion at least."
            "I straighten my tie and turn to one of the stalls across from the urinals."
            "The stall door creaks open with little force and I lock it behind me."
            "I flip the seat down heavily sit on top of it."
            "Taking a deep breath, I pull out my phone."
            "If Samantha ever caught me looking bored at my table, there was no way she would let me live it down."
            $ renpy.music.set_audio_filter("voice", af.Reverb(0.5))
            $ renpy.music.set_audio_filter("sfx1", af.Reverb(0.5))
            if bree.hidden:
                "I start scrolling over my social medias."
                "Soon, I lose track of time while doomscrolling over the whole internet."
                play sfx1 door_slam
                "The door to the bathroom slamming open pulls me out of my torpor."
            else:

                $ renpy.dynamic("old_room_outfit")
                $ old_room_outfit = Room.find(game.room).outfit
                $ Room.find(game.room).outfit = "date"
                play sound cell_vibrate
                "I blink in surprise when it vibrates."
                $ nvl_mode = "phone"
                nvl clear
                bree_nvl "Heyoo~"
                bree_nvl "How's your wedding? <33"
                "The second [bree.name] saw me bring in a plastic wrapped suit through the living room, she demanded to know what I was 'getting all classy' for."
                "Strangely enough, she helped me get ready despite my resistance."
                "Even Sasha threw in her own opinion as I was walking out- though it was a lot less constructive."
                mchero_nvl "It's not my wedding."
                bree_nvl "Sure sure."
                bree_nvl "How's 'Samantha's wedding?"
                menu:
                    "Fine":
                        mchero_nvl "It's going fine. Samantha looks happy about it."
                        bree_nvl "😆"
                        bree_nvl "'fine' is not usually a great word for a wedding ya know."
                        mchero_nvl "Whatever."
                    "I want to go home":
                        mchero_nvl "Not great, I want to go home."
                        $ bree.love += 5
                        bree_nvl "Aww poor baby!"
                bree_nvl "I'll make you some hot cocoa when you get back to cheer you up."
                mchero_nvl "Fuck off! 😖"
                bree_nvl "😜"
                play sfx1 door_slam
                "The door to the bathroom slamming open tears my attention away from [bree.name]."
                $ Room.find(game.room).outfit = old_room_outfit
            "I don't think much of it- until a strange giggle makes me wonder if I'm in the right place."
            ryan.say "Shh."
            "Girl" "I can give it to you better, sweetie."
            ryan.say "Prove it."
            "What the fuck. Was that Ryan? No way. Not at his wedding."
            "But there he was, clearly through the crack in my stall, along with that bridesmaid from earlier."
            play sfx1 pants_unzip volume 0.3
            "Something unzips."
            "Girl" "You're so... composed! Not even Samantha can keep a treasure like you."
            ryan.say "Shut up and suck it."
            "No, no way."
            "I am not sitting through Ryan getting a blowjob in a shitty restaurant bathroom."
            "My hand touches the lock, but pauses."
            "I can't just walk out and pretend like I didn't see anything."
            "Ryan would get angry, threaten to keep me quiet."
            "He would wonder why I wouldn't say anything to Samantha."
            "I didn't need that on top of everything else."
            if not hero.flags.knows_ryancheats:
                "There is no way Samantha would believe me if I just told her about this."
                "I stare blankly at my phone and back up at Ryan."
                "Making an easy decision, I lift my phone and open the camera."
                "I snap a few photos."
                "I can't just send these to her without saying anything, can I?"
                "She would break down."
                "I have to be there for her."
                $ hero.flags.knows_ryancheats = True
            $ samantha.flags.natalie = True
            play sfx1 bj_sucking loop volume 0.3
            pause 0.7
            ryan.say "Hnng-"
            "A wet sound filled the bathroom followed by a loud pop."
            "I cover my ears to block out the girl's moans."
            "This is officially the worst wedding I've ever been to."
            play sound cell_vibrate
            "My phone vibrates in my hand, and it makes my heart stop for a few seconds."
            "When the two don't stop, I sigh in relief."
            "Apparently everything sounds louder when you feel like you're going to die at any moment."
            "It's another text from [bree.name]."
            "I briefly consider responding, and accidentally glance up."
            show bg black
            show ryan natalie blowjob sucking
            with fade
            "Through the crack, I can see Ryan's hands tangled through the girl's hair and her lips firmly locked onto his member."
            "Her nose is buried deep into his pubic hair, and it looks like she's taking him all the way to the base."
            show ryan natalie blowjob licking with dissolve
            "Does she have a gag reflex?!"
            show ryan natalie blowjob sucking with dissolve
            "As fast as I look up, I look back down."
            "I decide to just fix my eyes on the floor, trying to ignore the two right in front of my door."
            "I don't know how much time passes, but by the time I finish counting every square tile one the floor, the bathroom door shuts again and it's once again silent."
            "Fuck me."
            $ renpy.music.set_audio_filter("voice", None)
            $ renpy.music.set_audio_filter("sfx1", None)
            call stop_all_sfx from _call_stop_all_sfx_33
        "Dance":
            "I might as well see what's going on on the main floor. Maybe I'd get a chance to talk to Samantha."
    scene bg restaurant
    show natalie date happy
    with fade
    "Girl" "That was so exciting!"
    "I jump in surprise at her sudden presence, breaking me out of my thoughts."
    "She plops down in the chair next to me, leaning forward on the table with her elbows."
    "Girl" "And romantic!"
    "Girl" "I wish I had someone to treat me like that, don't you?"
    mike.say "Um... yeah, I guess."
    if BATHROOM:
        "I stare at her warily, the image of Ryan's dick shoved far down her throat at the forefront of my mind."
        "I can't help but notice that her lips were more plump and red than when I first saw her when I got here."
    "Girl" "The food's really good!"
    show natalie normal
    "Girl" "I'm a little surprised to be honest."
    "Girl" "..."
    show natalie happy
    "Girl" "Wanna dance with me?"
    "I look up at her. She stares at me with a slight blush on her face. Is she being serious?"
    mike.say "I don't know. I don't really dance-"
    with vpunch
    "She suddenly grabs my arm and pulls me up before I can react."
    "Girl" "That's okay! I don't either. But we can both try!"
    "The middle of the hall was filled with darkened mood lights and dancing couples."
    "The music playing turns somewhat slow and mellow."
    "She puts her hands on her hips as if she were expecting something."
    "Didn't I just say I didn't know how to do this crap?"
    "I wrack my brain for some sort of reference."
    "Movies? Sure. I nervously put my hands up in the formal dance position."
    "She smirks, takes my hands and puts the other on her hip. We swayed back and forth."
    "She seems to be enjoying it, but I can't help but feel awkward."
    "Samantha and Ryan were somewhere around here."
    "I want to talk to her- congratulate her or something."
    "At the same time, I don't want to see them so in love."
    show natalie normal
    show samantha wedding at top_mostleft with easeinleft
    samantha.say "[hero.name]!"
    "Speak of the devil."
    samantha.say "I'm so glad to see you! Thank you so much for coming."
    show samantha at left4
    show natalie at right5
    with ease
    "She puts a gentle hand on my shoulder."
    "Her friend backs away from me with a huff."
    "I finally relax."
    if samantha.flags.nickname == "cupcake":
        mike.say "Hey, Cupcake."
    else:
        mike.say "Hey, Sam."
    show natalie date happy
    "Girl" "Sam! You're so beautiful! Look at you!"
    "Her cheeks tinge red and she set a soft hand on her face."
    show samantha wedding happy
    samantha.say "Thank you! You look great too. Thanks for being my bridesmaid... and helping me put things together."
    "Girl" "This is all you! No more 'thank you's- enjoy yourself."
    show samantha wedding normal
    show natalie date normal
    samantha.say "I will- in fact~"
    "Samantha turns to me."
    samantha.say "May I have this dance?"
    mike.say "..."
    menu:
        "Yes":
            mike.say "Of course."
            "She claps her hands gleefully."
            samantha.say "Yay~! I hope you don't mind, Natalie."
            "Natalie? ... Oh."
            natalie.say "He's yours!"
            "Natalie winks at Sam, but I can see her hesitation."
            hide natalie
            show samantha wedding at center
            with easeoutright
            "I turn to Sam, who's already moving closer."
            show samantha at center, zoomAt(1.5, (640, 1040)) with dissolve
            "I automatically put my hand on her hip and she tenderly takes my other hand."
            mike.say "Having a good night?"
            show samantha happy
            "She laughs, a genuine smile coming across her face. It's beautiful."
            samantha.say "You wouldn't believe. This has been... my dream. I can't believe it's happening right now."
            mike.say "Ha! I can. You guys were all over each other when we still lived together."
            show samantha normal
            samantha.say "You know what I mean."
            samantha.say "..."
            show samantha sad
            samantha.say "You look sad."
            mike.say "I- I'm not. I'm happy for you."
            "Samantha frowns at me. I blink rapidly, trying to control my expression."
            mike.say "Don't worry about me. This is your big night- let's have some fun."
            show samantha normal
            "It looks like she wants to say more, but she shakes her head and gets closer."
            mike.say "I heard it took quite a lot of work to throw this thing together so fast."
            samantha.say "Ugh. Don't get me started. I'm used to sleepless nights from college, but this was something else!"
            samantha.say "What do you think for a bunch of rush planning?"
            menu:
                "It's beautiful":
                    mike.say "I think you did a great job. You look fantastic, the food is good... you should be proud of yourself."
                    show samantha wedding blush
                    "A blush presents itself above her light makeup."
                    samantha.say "Thank you. You're so sweet!"
                    $ samantha.love += 1
                "It could have used some more work.":
                    mike.say "It could use some more work."
                    show samantha annoyed
                    samantha.say "Of course it could! But there was no time."
                    mike.say "I wouldn't worry about it. Everyone's enjoying themselves and we're here now."
                    show samantha happy
                    samantha.say "Good point."
            show samantha normal
            "The music changes to a traditional slow dance and I find myself almost hugging her, swaying back and forth with the flowing music."
            "The night ends with her head on my chest, eyes closed."
            "The guilt eventually subsides as we melt together in the middle of the dance floor."
            "Her soft blonde hair is tickling at my chin, but I can't pull away."
            "She's warm and light."
            "I hope she can't hear my heart pounding in my chest."
            "The night comes to a calm end, dancing with my best friend in the middle of the dance floor."
        "Ask about Ryan":
            show samantha wedding
            "I can't steal away the bride on her wedding night."
            mike.say "Shouldn't you be dancing with Ryan?"
            samantha.say "I've been with Ryan all night!"
            samantha.say "I want to say hi to my friends."
            "She playfully tugs at my arm, but I pull away."
            show samantha sad
            "Her face falls."
            show natalie date happy
            natalie.say "I think I see Ryan over there!"
            natalie.say "You should go snatch him up before another girl gets to him."
            hide samantha
            hide natalie
            show ryan tux smile
            show sasha wedding at flip, left5, blacker
            with fade
            "I follow her line of sight to see Ryan talking to another girl, getting far too close for comfort."
            if hero.flags.knows_ryancheats:
                "Sam giggles, but my chest burns with anger that I force down, knowing what he was probably doing."
                "During his wedding."
            hide ryan
            hide sasha
            show natalie date normal at right5
            show samantha wedding normal at left5
            with fade
            samantha.say "Alright, alright."
            natalie.say "Quick! I hear a slow dance starting!"
            show samantha wedding annoyed
            samantha.say "Ooh! But, you owe me a dance once all this is over, [hero.name]!"
            mike.say "..."
            samantha.say "Promise!"
            mike.say "Fine. I promise."
            hide natalie
            show ryan tux smile at left4
            show samantha wedding happy at right4
            with fade
            "She grins wide, then scuttles over to Ryan, getting his attention. Ryan looks down at her, his face morphing into kindness. I move back to Sam's friend."
            hide ryan
            hide samantha
            show natalie date happy at center
            with fade
            natalie.say "They're so cute. You'll keep dancing with me, right?"
            mike.say "Um-"
            show natalie at center, zoomAt(1.5, (640, 1040))
            "She gets closer to me before I can answer, forcing me into the slow dance."
            "We move around the hall for a while. She's talking, but I'm not really focused."
            "I only stare over her back, watching Ryan and Samantha hold each other tightly."
            show natalie date normal
            natalie.say "Hey- are you listening?"
            mike.say "Sorry, what?"
            natalie.say "What are you so distracted by? Are you not into me or something?"
            mike.say "No, that's not it, - ... um."
            "Shit, what's her name? I don't even remember when I met her, my mind can't even pull up the first letter. Wendy? Irene?"
            natalie.say "... Natalie!"
            "Not even close."
            mike.say "Sorry. I-"
            natalie.say "No, whatever. I can tell you're not interested."
            mike.say "..."
            mike.say "I mean, you're not wrong."
            "Natalie's mouth hangs open as if I'd personally offended her."
            with vpunch
            "She makes an upset little screech before slapping me on the shoulder with little force and turns on her heel."
            hide natalie with moveoutright
            mike.say "... At least that's over."
            "I move back to my seat, alone once again. I taste the untouched duck."
            "It's... sweet. But not in a bad way."
            "Sam really did make a good choice."
            "A waiter spots me and comes around to fill my tall glass with pale champagne."
            "I mutter a thanks."
            "Not my choice of drink, but it would be good enough for now."
            "I start gulping it down, hoping to feel the familiar buzz in the back of my mind."
            "The sooner it came, the better."
    scene bg black with dissolve
    $ samantha.flags.delay = TemporaryFlag(True, 1)
    $ samantha.flags.post_wedding_baby_talk_delay = TemporaryFlag(True, 30)
    return

label samantha_event_B02:
    $ renpy.dynamic("book")
    if samantha.love.max < 140:
        $ samantha.love.max = 140
    $ samantha.flags.nokiss = False
    samantha.say "[hero.name]!"
    "I recognize Samantha's voice behind me easily."
    show samantha
    "Once I spot her, my eyes dart to the shiny new ring on her finger, sparkling under the light."
    "She comes up to me and grabs my arm."
    samantha.say "How are you?"
    mike.say "You know- working."
    show samantha annoyed
    "Sam pushes out her lip in a pout."
    "She's trying to be playful, but I can see something else hiding beneath."
    "Gloom? It didn't look good on her."
    mike.say "Something wrong?"
    show samantha normal
    samantha.say "Hm? What do you mean?"
    mike.say "I've known you long enough to see when you're sad."
    mike.say "You know you can talk to me, right?"
    "She's silent for a long moment, adjusting her pressure on my arm, squeezing dejectedly."
    show samantha sad
    samantha.say "It's just..."
    samantha.say "I- I thought that once we got married, Ryan would be around more."
    samantha.say "That we'd finally be a real family; eating meals together, falling asleep in each others arms- but he's never home."
    mike.say "Oh. I'm sorry."
    show samantha happy
    samantha.say "Haha! It's not your fault."
    mike.say "Have you talked to him about it?"
    show samantha sad
    samantha.say "I'm kind of scared to."
    "My expression must be something like concerned, because she instantly raises her arms in denial."
    show samantha normal
    samantha.say "Not like that!"
    samantha.say "Never like that."
    show samantha annoyed
    samantha.say "He's always so busy."
    samantha.say "I'm afraid that if I tell him to spend more time with me that he'll think I'm being... possessive."
    samantha.say "I don't want that! I've always let him have his freedom."
    samantha.say "I've never been that overbearing girlfriend, but... what if he thinks I've changed just because we're married now?"
    mike.say "What? You're afraid he'd leave you if you ask him for something?"
    samantha.say "No, no, not leave. It's complicated- but yes."
    mike.say "Seriously!? That guy would do anything for you."
    "Okay, probably not anything. But she needs the encouragement."
    mike.say "If he's neglecting you, you should talk to him."
    samantha.say "He's not neglecting me!"
    mike.say "It sure sounds like he is."
    samantha.say "... Fine. I'll talk to him. But he is not neglecting me!"
    "I shake my head and don't answer. Whatever you say, Sam."
    show samantha normal
    samantha.say "Anyway~ I wanted to hang out with you."
    mike.say "Ha! With me?"
    samantha.say "Yes! Don't say it like that."
    samantha.say "I've been meaning to pick up some novels from the bookstore in the mall. Will you go with me?"
    mike.say "Yeah, alright."
    show samantha happy
    samantha.say "Yay!"
    hide samantha
    scene bg bookstore
    with fade
    "I find myself between shelves of books, looking blankly at titles and covers."
    "Nothing was really catching my attention."
    show samantha with dissolve
    samantha.say "[hero.name]! What do you think of this one?"
    "Sam rushes at me with a book in hand from the children's section. It's large and colourful, with about ten pages max."
    menu:
        "Why are you looking for kids books?":
            mike.say "Aren't these a little young for you?"
            samantha.say "They're not for reading! They're for studying. You know I want to write children's books."
            mike.say "Oh yeah."
        "Take Book":
            "I turn the book over in my hands. It's got an abstract art style with vibrant colours and strange characters."
    mike.say "It's... nice?"
    show samantha annoyed
    samantha.say "That's all you got? You can do better than that~"
    show samantha normal
    if hero.knowledge >= 50:
        "I stare flip open the book and analyze the pages. The paper was the usual overly thick texture that most kids books had."
        mike.say "I guess..."
        mike.say "The art is different. But I don't think it matches your style. You have a softer appeal."
        samantha.say "Hmm."
        mike.say "As for the writing, it's got an interesting story as far as that goes- but I think you could study the theme and moral ending."
        "Sam nods along attentively with my words. It felt good to have her listen."
        samantha.say "I take it that means it's a good choice?"
        mike.say "Sure."
        "She gives me a finger salute and tucks it under her arm."
    else:
        "I stare blankly at the cover. The amount of colours makes my head swim, not used to the brightness. Compared to my room, this was practically a rainbow."
        mike.say "It's got... a lot... of colours?"
        samantha.say "Quite the articulate, aren't you?"
        mike.say "Shut up!"
        mike.say "..."
        mike.say "I like it."
        "Sam nods her head dutifully and tucks it under her arm."
    samantha.say "So? Are you getting anything?"
    mike.say "I guess I will while I'm here."
    show samantha happy
    samantha.say "Good! I'm going to keep looking around."
    hide samantha with dissolve
    "I'm left by myself as she retreats back to the children's section, hunting for more books. I didn't really know where to start."
    menu:
        "Cooking" if "skill_book_cooking" not in hero.inventory and not hero.has_skill("cooking"):
            "Pictures of delicious food and pristine recipes litter the covers of every book in the aisle. I grab at the first one that catches my eye."
            mike.say "Baking?"
            "I turn the pages quickly, skimming through the words. Complicated desserts that I could never probably perfect stare back at me with intimidation."
            "I take the book up to the counter to pay. Sam's already up there waiting for me, plastic bags in hand."
            $ hero.gain_item("skill_book_cooking")
            $ book = "cooking"
        "Sports":
            "Football, baseball, soccer... every sport I could imagine was laid out in front of me. Some were magazines, some were thick books examining every aspect of the game."
            "My hand hovers over a magazine, covering a broad area of each one."
            "I grab the magazine, the flimsy pages flopping around in my hand. I walk up to the counter, digging out my wallet."
            $ hero.gain_item("fitness_book")
            $ book = "sports"
        "Fiction":
            "The fantasy and science fiction call my name. The newest publishers grace the shelf with shiny, new, hardback covers."
            "I flip over the back of one, reading the summary. Dragons, space, battles... what's more to love?"
            "The decision is easy. The book has my name on it before I even set it down in front of the store clerk to pay."
            $ hero.gain_item("charm_book")
            $ book = "fiction"
    show samantha with dissolve
    samantha.say "Find what you were looking for?"
    mike.say "Yup!"
    "I wave the single book in front of her and she stares at it intently."
    if book == "cooking":
        show samantha happy
        "Sam's face lights up instantly."
        samantha.say "You have to bake me something! Look at all these recipes. Good choice!"
        mike.say "..."
        mike.say "You work at a bakery."
        samantha.say "Excuses!"
    elif book == "sports":
        samantha.say "You're a sports junkie, hm?"
        mike.say "Junkie is a strong word."
        samantha.say "Sure, sure. Maybe you'll finally learn how to play darts with me."
        mike.say "I don't think that's covered in here."
    elif book == "fiction":
        samantha.say "Ooh! Exciting! I should have expected that, considering your room."
        mike.say "Hey! My room looks great."
        samantha.say "If your version of great also means nerdy then, yeah, it's great."
    show samantha happy
    samantha.say "Thanks for coming with me! This was fun."
    mike.say "No problem. Are you heading home?"
    show samantha sad
    samantha.say "... Yeah, I guess I am."
    "She looks sad again. Was she really that lonely?"
    if samantha.flags.nickname == "cupcake":
        mike.say "Aw, Cupcake."
    else:
        mike.say "Aw, Sam."
    samantha.say "I-"
    show samantha cry
    samantha.say "..."
    "My heart sinks when tears start running down her cheeks. Oh shit."
    show samantha at center, zoomAt(1.5, (640, 1040))
    "I pull her into a hug. She wraps her arms around my torso."
    mike.say "Want to hang at my house instead?"
    "I can feel her nod her head in the crook of my neck."
    mike.say "Alright. Let's go."
    hide samantha
    scene bg livingroom
    show samantha casual normal zorder 2 at center, zoomAt(1.5, (640, 1140))
    with fade
    "Samantha is sitting on the couch, looking through her new book. The tears have long since dried."
    scene bg kitchen with fade
    "I'm in the kitchen making her some sweet tea."
    "Once I drop the bag into the steaming water and add copious amounts of sugar, I carefully make my way back to where she sits."
    scene bg livingroom
    show samantha casual normal zorder 2 at center, zoomAt(1.5, (640, 1140))
    if not bree.hidden:
        show bree casual zorder 1 at right
        with fade
        "When I turn the corner, I see [bree.name] has come down from her room."
        show bree happy
        bree.say "Hiya! Did [hero.name] really bring home a girl?! He's growing up so fast!"
        mike.say "[bree.name]-"
        if not game.flags.samanthaknowsbree:
            $ game.flags.samanthaknowsbree = True
            show bree normal
            bree.say "You look familiar. Did you help Ryan find this house for me?"
            mike.say "[bree.name]-"
            "Despite her incessant talking, Samantha doesn't seem bothered. So, I just set down her tea on the coffee table in front of her."
            samantha.say "Yeah, that's me."
            bree.say "That means- you just got married, right?"
            samantha.say "Yup!"
            show bree happy
            bree.say "Ha! I can see why [hero.name] was so depressed."
            mike.say "[bree.name]! Okay, go back to your little hermit hole."
            show bree annoyed
            bree.say "Hermit hole!? If that's what you think of it, then you haven't even had a glimpse at my game collection. More like paradise, you sad sap!"
        else:
            samantha.say "Hi, [bree.name]."
            bree.say "Hi."
            bree.say "I'll be in my bedroom, don't do anything I wouldn't do."
        hide bree with easeoutright
        "With that, [bree.name] retreats back up the stairs. I try not to let my face heat up."
        mike.say "I have no idea what she's talking about."
        show samantha happy
        "Samantha simply giggles, a hand lightly covering her mouth."
        samantha.say "She seems like a lively girl. Are you glad she's your roommate?"
        mike.say "I suppose you guys could have done worse."
        show samantha normal
        samantha.say "Don't be mean! She's pretty."
        mike.say "Whatever."
        show samantha happy
        samantha.say "I mean it! You guys would be cute together."
        mike.say "You're funny."
        show samantha normal
        "She rolls her eyes and gives up. Picking up the cup of tea, she takes a sip."
    else:
        mike.say "Here's your tea. I hope it'll be fine."
    samantha.say "Not bad."
    mike.say "Ouch."
    samantha.say "Wha-! It's good. Don't get all upset. It just needs a little more sugar."
    mike.say "There are, like, three teaspoons in there."
    samantha.say "Mh hmm. Like I said, it needs more sugar."
    "A moment passes in silence as she drinks the rest of her tea."
    mike.say "So, what can we do to cheer you up?"
    samantha.say "I don't know. What'cha got around here?"
    menu:
        "Bake Something" if book == "cooking" or hero.has_skill("cooking"):
            mike.say "We could bake something."
            if r == "Cooking":
                samantha.say "Ooh! Putting that book to use, I see."
                "I pick up the book from where I'd tossed it on the coffee table and look through for simple recipes."
            mike.say "Cupcakes?"
            samantha.say "Yes! Let's do it!"
            hide samantha
            scene bg kitchen
            show samantha
            with fade
            "Samantha rushes past me into the kitchen. I hear clanking pots and opening drawers already. I follow her."
            samantha.say "Eggs, vanilla, baking powder-"
            if book == "cooking":
                mike.say "Whoa- wait, you haven't even seen the recipe yet."
                samantha.say "I work at a bakery. I know how to make cupcakes."
                "I shrug. Good point. I close the cookbook and set it on the counter. I find a few large mixing bowls and set them next to the ingredients."
            samantha.say "Mix these, please!"
            "She says 'please' but it sounds more like a command. Nonetheless, I take the ingredients she shoves at me and mindlessly pour them into a bowl, whisking them together."
            "She does the same, mixing up the dry stuff with a fork."
            samantha.say "Hmm... where's the flour?"
            mike.say "Uh, on the top shelf, I think."
            "Samantha goes to the shelf I point at. It's a few inches taller than her. I don't think she can reach and she tries anyway, standing on her toes."
            mike.say "Do you need-"
            show samantha surprised at center, vshake
            samantha.say "Eeek!"
            "A puff of white in the corner of my vision has me whipping around. Samantha stands, arms still raised above her to get the bag."
            "She's covered from head to toe in dusty flour. The floor wasn't looking much better. I can't help it- I start laughing."
            show samantha annoyed
            samantha.say "Are you laughing?!"
            "I try to get a hold of myself- I really do. Before I can, Samantha grabs a pile of flour off the floor and blows it right into my face."
            "I was lucky my eyes were closed."
            mike.say "Wha-?! What the fuck?!"
            show samantha happy
            "Now she's laughing."
            show samantha normal
            samantha.say "You're right! It is really funny!"
            "Wiping at my face, I get a good look at the mess. This was going to be a nightmare to clean up."
            mike.say "Is there any left?"
            samantha.say "..."
            show samantha happy
            samantha.say "Yep! There enough left in the bag."
            "She picks up the remains of the flour and pours in into the bowl."
            "Samantha's a mess, but she's beaming; and that's all that matters."
            scene bg black with timelaps
            scene bg kitchen
            show samantha casual
            with timelaps
            "Samantha pulls the cupcakes out of the oven. They look perfect with her watchful eye. The bottom floor of the house smells fantastic."
            "She sets down the hot tray on top of the counter to let them cool. She shakes her arms, still covered in white powder."
            if bree.hidden:
                mike.say "Want me to find you some extra clothes? I might be able to find something upstairs."
                samantha.say "No, it's alright. This was my fault anyway."
                mike.say "... You have a point. Alright."
                show samantha happy
                play sound cell_vibrate
                "As she pulls out her phone, her smile slowly fade away."
                show samantha normal
                samantha.say "It's Ryan, he's home."
                samantha.say "We have a few things to talk about. Sorry, I have to go."
                mike.say "Oh... okay, no problem."
                samantha.say "Thank you so much for having me over."
                mike.say "You're always welcome here."
                show samantha happy
                pause 0.2
                show samantha with moveoutright
                "A wide smile graces her face. I walk her to the door."
                "She gives me a small wave- then pulls me into a hug. I watch her go."
            else:
                mike.say "Want me to find you some extra clothes? I don't think [bree.name] will mind."
                samantha.say "No, it's alright. This was my fault anyway."
                mike.say "Oh, come on. You don't want to walk home like that, do you?"
                samantha.say "... You have a point. Alright."
                scene bg secondfloor with fade
                "I let her stay with the cupcakes and walk upstairs."
                scene bg door bedroom2 with fade
                pause 0.2
                play sound door_knock_light
                "I knock lightly on her door."
                play sound door_knock_more
                "No answer. I knock louder."
                play sound door_open
                scene bg black with dissolve
                pause 0.5
                scene bg bedroom2
                show bree casual annoyed
                with wipeleft
                "There's a crashing sound from the other side and the door flings open."
                stop sound
                show bree vangry
                bree.say "This better be good! I'm in the middle of a fight-"
                show bree stuned at center, vshake
                "She abruptly stops at the sight of my face, holding her headphones in one hand. I must not have washed my face enough. Goddammit Samantha."
                show bree surprised
                bree.say "What the hell are you guys doing?"
                show bree stuned
                mike.say "Can I borrow some clothes for Samantha?"
                show bree smile
                bree.say "Having fun down there? Sure, but you better not mess them up with your dirty foreplay. I want these back!"
                show bree normal
                mike.say "That's not-!"
                "[bree.name] shoves a pile of clothes into my hands and shuts the door in my face. That girl would be the end of me."
                scene bg kitchen
                show samantha
                with fade
                mike.say "Here."
                show samantha happy
                samantha.say "Thanks. Oh! You should tell [bree.name] I said thank you. I think I have to go, though."
                mike.say "Oh... okay, no problem."
                show samantha normal
                samantha.say "I'm sorry! Ryan texted me and said he was home and... we have a few things to talk about. Thank you so much for having me over."
                mike.say "You're always welcome here."
                show samantha happy
                pause 0.2
                show samantha with moveoutright
                "A wide smile graces her face. I let her change in the bathroom, then walk her to the door."
                "She gives me a small wave- then pulls me into a hug. I watch her go."
        "Have Drinks":
            mike.say "I think there's still some wine left if Sasha hasn't gotten to it yet."
            show samantha happy
            samantha.say "Sounds like a plan."
            scene bg kitchen
            show samantha casual
            with fade
            "We both move to the kitchen. I open up a cupboard and pull out a half full bottle of red wine."
            "Sam gets two glasses, still remembering where things were last time she was here."
            "I tilt the bottle and fill each glass to the brim. Samantha nods in approval. She takes a long drink. I do the same."
            mike.say "It can't all be bad. What are some good things going on with you two?"
            show samantha flirt
            samantha.say "Well... the night of the wedding, he took me to bed and made love. It was the most passion he's had for a while."
            mike.say "Oh-"
            samantha.say "He's been getting really dominant lately. I can't say I hate it."
            mike.say "Not really what I meant, but good start."
            show samantha normal
            "She giggles and takes another gulp."
            samantha.say "He gave me a stack of new books when he finally got home yesterday. I haven't started them yet, but they look good."
            mike.say "That's nice."
            samantha.say "Hmm."
            "The air is tense, but it slowly unravels as we drink more."
            menu:
                "University":
                    mike.say "How's the studying going? Doing any better with that stuff?"
                    show samantha annoyed
                    samantha.say "I haven't had too much time to work on it lately, but my grades are rising at least. God, I hate math."
                    mike.say "Ditto."
                    show samantha normal
                    samantha.say "My literature classes are really great, though. We get to write an essay on story structure."
                    mike.say "Really? How's that going?"
                    samantha.say "I'm finished!"
                    mike.say "Oh."
                "Work":
                    mike.say "Still loving the bakery?"
                    show samantha happy
                    samantha.say "How is that even a question?! Of course I do."
                    show samantha normal blush
                    samantha.say "Oh, I'm so excited for next week. We're getting new recipes in as a standard."
                    mike.say "What are they?"
                    samantha.say "Guess! They're my favourite."
                    menu:
                        "Tiramisu":
                            samantha.say "Nope! But that's a great idea. I should suggest that."
                            samantha.say "We're adding fresh cinnamon rolls to the menu! The bakery's going to smell so good."
                            mike.say "It already does."
                        "Cinnamon Rolls":
                            show samantha happy
                            samantha.say "Yes, yes! You remembered!"
                            mike.say "You had them all over the house. Of course I remember."
                        "Funnel Cake":
                            show samantha annoyed
                            samantha.say "It's a bakery, not a fair!"
                            mike.say "What, are you saying you don't like those?"
                            show samantha normal
                            samantha.say "No! That's not what I mean. Cinnamon rolls! We're going to start making cinnamon rolls."
                "Fun":
                    mike.say "What do you do all day? Y'know, other than obsess over Ryan."
                    "She gives a playful glare, but answers anyway."
                    samantha.say "Darts... writing. I like hanging out with you! Does that count?"
                    mike.say "..."
                    mike.say "Yeah, I guess it does."
            play sound cell_vibrate
            show samantha surprised
            "A sudden buzzing grabs both of our attention: Samantha's phone. She pulls it out of her back pocket."
            show samantha normal
            samantha.say "Ryan sent me a text."
            samantha.say "He says he's home!"
            mike.say "Are you saying you're leaving?"
            show samantha flirt
            "She looks up at me with large eyes, pleading for forgiveness."
            samantha.say "I'm sorry!"
            mike.say "No, it's fine. As long as you have a talk with him!"
            samantha.say "..."
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake! You have to!"
            else:
                mike.say "Sam! You have to!"
            samantha.say "Alright! I will."
            mike.say "Good."
            "She finishes her glass and sets it on the counter. I walk her to the door."
            scene bg house
            show samantha casual
            with fade
            samantha.say "Thanks for having me over, [hero.name]. I really appreciate it."
            mike.say "Anytime."
            "Samantha gives me a friendly wave goodbye and steps off the porch. I smile and close the door behind her."
    scene bg black with dissolve
    $ game.room = "livingroom"
    return

label samantha_event_B03:

















    $ renpy.dynamic("answer")
    if samantha.love.max < 160:
        $ samantha.love.max = 160
    play sound cell_vibrate
    "My phone buzzes suddenly in my back pocket. When I open it up, Samantha's name blares at me from the screen; it's a text."
    samantha.say "Hey."
    mike.say "Hey. What's up?"
    samantha.say "Nothing much."
    samantha.say "Can I come over?"
    mike.say "Right now?"
    samantha.say "Yes."
    samantha.say "My house is just really empty right now."
    samantha.say "I don't know what to do."
    menu:
        "Of course you can":
            mike.say "Yeah. You can come over."
            samantha.say "Thanks."
            samantha.say "I really appreciate that you've been here for me."
            $ answer = True
        "Too busy":
            if samantha.flags.nickname == "cupcake":
                mike.say "Sorry, Cupcake. I'm really busy right now."
            else:
                mike.say "Sorry, Sam. I'm really busy right now."
            mike.say "Maybe next time?"
            samantha.say "Alright. Sorry for bothering you."
            $ answer = False
    scene bg black with timelaps
    scene bg livingroom with timelaps
    play sound door_knock
    "I'm broken out of my thoughts by a knock at the door."
    scene bg black with dissolve
    scene bg house
    show samantha casual sad
    with wiperight
    if answer:
        if samantha.flags.nickname == "cupcake":
            mike.say "Hey, Cupcake."
        else:
            mike.say "Hey, Sam."
        samantha.say "Hi, [hero.name]. Thanks for letting me come."
    else:
        if samantha.flags.nickname == "cupcake":
            mike.say "Cupcake?"
        else:
            mike.say "Sam?"
        samantha.say "Hi..."
        show samantha sad
        samantha.say "I'm sorry. I know you said you were busy, but..."
        samantha.say "I just need some company right now."
        mike.say "Oh. Alright."
    scene bg livingroom
    show samantha casual sad
    with fade
    "I take Samantha into the living room. She stands nervously, rubbing her hands, looking at the stairs as if she's worried someone will walk in."
    mike.say "Are you alright?"
    samantha.say "I- um-"
    show samantha cry
    "Tears drop down her cheeks one by one. I don't know what to say."
    mike.say "Want to go somewhere else?"
    "She nods her head, furiously dabbing at her eyes with the edge of her sleeve. We move to my room. By the time we get there, she's full blown sobbing."
    scene bg bedroom1
    show samantha casual cry
    with fade
    mike.say "..."
    menu:
        "What's wrong?":
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake... are you okay? Did something happen?"
            else:
                mike.say "Sam... are you okay? Did something happen?"
            samantha.say "I- I..."
            samantha.say "I don't- I- "
            "She doesn't seem ready to talk, so I try to give her some space."
        "Let her cry":
            "..."
    show samantha sad at center, zoomAt (1.5, (640, 1140))
    "I let her sit on my bed and take my place beside her. She leans on my shoulder and I wrap an arm around her."
    samantha.say "I talked to Ryan."
    "My insides freeze. Is that why she's crying? Before she says another word, rage start building up in my throat."
    samantha.say "I talked to him- I really tried. When I asked why he was never home he got upset."
    samantha.say "I said I wanted us to spend more time together. Ryan... Ryan said that just because I was his wife now doesn't mean I get to control him."
    samantha.say "That was a couple days ago. He hasn't been home since."
    "Ryan... left? No, he didn't leave. He would be back, I'm sure of it."
    "He was a douchebag, but he wouldn't just up and leave Samantha if they had a little argument."
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake, I'm so sorry."
    else:
        mike.say "Sam, I'm so sorry."
    samantha.say "I shouldn't have brought it up. This is all my fault."
    mike.say "Hey! Don't say that- this is in no way your fault. Ryan's a dick and that's the end of it."
    samantha.say "No, it is! I was... too aggressive. I made him upset. I should have been calmer about it."
    "That was blatantly untrue. Samantha was the kindest girl I've ever met. If anyone had been aggressive, it was Ryan."
    "No debate. I don't think Samantha could even raise her voice sometimes."
    mike.say "That's not true. I know it didn't happen like that and you know it too."
    "She doesn't answer, but shakes her head. I take her hands in mine; their shaking and pale. It was hard to watch, my throat constricting in concern."
    mike.say "Listen to me; we're going to forget about Ryan for tonight. He doesn't deserve for you to think about him."
    samantha.say "But-"
    mike.say "No 'but's. You're going to think about yourself for once."
    samantha.say "... I can't. I'm sorry."
    mike.say "You have to. If not for you, then do it for me."
    show samantha normal
    samantha.say "I don't know how."
    "My mind races. What can I do? How can I distract her?"
    samantha.say "..."
    samantha.say "Mmph-!"
    hide samantha
    show samantha kiss casual
    with dissolve
    $ samantha.flags.kiss += 1
    "The next thing I know... I lean in to kiss her."
    "And promptly give myself a heart attack. What am I thinking? This would only make things worse. I'd be lucky if she didn't walk out on me right now."
    hide samantha kiss
    show samantha casual normal at center, zoomAt (1.5, (640, 1140))
    with dissolve
    mike.say "Oh god- I'm so sorry! I don't-"
    hide samantha
    show samantha kiss casual
    with dissolve
    $ samantha.flags.kiss += 1
    "Her eyes are glassy for a moment. I blink, and her lips are back on mine, but I didn't start it this time."
    "My hands snake up into her blonde locks. It's soft and clean, as if she spent the entire day brushing it out of boredom."
    "My blood boils as I realize she probably did purely out of anxiety."
    "Her tongue prods at my lips. I breathe in, taking in her tongue with the sudden lack of air. The muscle is unbelievably soft."
    "I can taste the salt in her tears mixed with warm, sweet saliva."
    "Samantha's hands find the front of my chest. She's stuck between grabbing blindly and coherently exploring every curve and dip of my body."
    "I need to do the same. I lift my hands under her shirt, touching her bare back. I find the strap of her bra easily, plucking at it absently with one hand."
    "The other traces along each bone of her spine, slowly getting lower and lower."
    "She gasps into my mouth once I reach her waistband. I slip my fingers underneath, tugging lightly."
    "At the same time, her hands are at my hips, gripping tightly. My lower half becomes warm and my jeans strain against my crotch."
    "The hand I have on her strap fumbles for a moment before undoing the clasp. Samantha's bra comes loose and falls down her front."
    "My shirt comes off in the next second."
    hide samantha kiss
    show samantha casual flirt blush at center, zoomAt (1.5, (640, 1140))
    with dissolve
    samantha.say "[hero.name]!"
    "Samantha's shirt comes over her head, her bra hitting the floor. Her large breasts lay perfectly round in front of me."
    show samantha naked with dissolve
    "I push her back onto the covers and immediately take one of her nipples into my mouth. She gasps below me."
    if samantha.piercings.nipples.worn:
        "My tongue shoots out of my mouth and hits something hard. A piercing?"
        "My mind briefly brings up images of our time at the sex shop- yep. Definitely a piercing."
        menu:
            "Play with the piercing":
                "Making my mind, I loop my tongue around the metal and suck hard."
                samantha.say "Hhng-!"
                "My teeth clack against the piercing. I pull up, to the side. She's writhing underneath me."
                "The mix of skin and metal make my face heat in anticipation."
                "My hands twitch, needing something to do. One snakes under her hip, grasping at her plump ass."
                "The other plays with the other nipple piercing, rubbing circles around it teasingly."
            "Ask her to take it out":
                mike.say "Can you-"
                $ samantha.piercings.nipples.worn = False
                "Before I get out my request, she pulls out the piercing, tossing them to the side as if reading my mind."
                "My mouth finds her soft flesh, sucking her nipple into my mouth. Her skin is soft, almost sweet- like eating candy."
                "I gently rake my teeth across her tender nipple. Distantly, I hear her gasp."
                "My tongue sprints circles on her skin. Moving from the pointy center, I go down."
                "I poke my tongue between her breast and the skin underneath, my nose practically buried in her pillow-like boobs. Her hands are in my hair."
                "Every touch she gives me is loving; gentle."
    else:
        "My mouth finds her soft flesh, sucking her nipple into my mouth. Her skin is soft, almost sweet- like eating candy."
        "I gently rake my teeth across her tender nipple. Distantly, I hear her gasp."
        "My tongue sprints circles on her skin. Moving from the pointy center, I go down."
        "I poke my tongue between her breast and the skin underneath, my nose practically buried in her pillow-like boobs. Her hands are in my hair."
        "Every touch she gives me is loving; gentle."
    samantha.say "[hero.name]! Please! I need-"
    "Samantha pulls down her pants, pushing them off of the bed."
    "Her fingers are expertly unbuttoning my jeans and the building pressure is finally released as mine fall to the floor as well, boxers following suit."
    "My length points to the ceiling, not wanting to wait any longer."
    "I spread her thighs and she obediently opens them for me. My skin is hot, radiating warmth."
    "It's almost suffocating. The only thing keeping me from her was the thin cloth covering her lower half."
    "I push my nose into her panties, her scent making me dizzy."
    "There's a damp spot staining through; I pull back. Her legs are thick and beckoning me back down."
    "I lower my face into her thighs. I nip at her panties and pull hard with my teeth until they're at her knees."
    "Going back up, she's already wetter, leaking anxiously and breathing hard. I'm doing the same."
    menu:
        "Go down on her" if hero.sexperience >= 10:
            scene bg bedroom1
            show samantha cunnilingus middle
            with fade
            "Deciding to give her the pleasure she needs, my tongue darts out and licks at her vagina. It's hot and she twitches below me."
            show samantha cunnilingus down
            samantha.say "Oh my god!"
            show samantha cunnilingus middle
            "Her words spur me on. My eyes lock onto her clit; I dive in, mouth latching onto her."
            show samantha cunnilingus up
            "Her taste is unique and her smell is intoxicating. It's nothing like I'd ever experienced."
            show samantha cunnilingus middle
            "Her hips wiggle under me in pleasure. She tugs hard at my hair."
            show samantha cunnilingus down fingerass
            "I ignore her grunt of disappointment as I lean back, gulping down a breath. Before she can recover, I shove my fingers into my mouth, get them wet, and am opening her ass up."
            show samantha cunnilingus middle
            samantha.say "I need you, I need you!"
            show samantha cunnilingus up
            mike.say "You'll have me."
            show samantha cunnilingus middle
            "I pump my finger inside her while licking at her clit like it's the most tasty thing in the world, and it might be."
            show samantha cunnilingus down
            mike.say "Ready? Are you alright?"
            show samantha cunnilingus up
            samantha.say "Get inside of me."
        "Just fuck her":
            pass
    "The hardness in between my legs can't be ignored any longer."
    if hero.has_condom():
        menu:
            "Use a condom":
                $ CONDOM = hero.use_condom()
                "I put a condom on then push inside of her."
            "Do it raw":
                $ CONDOM = False
                "I spit into my hand, try to cover my dick as much as I can and push inside of her."
    else:
        $ CONDOM = False
        "I spit into my hand, try to cover my dick as much as I can and push inside of her."
    hide samantha
    show samantha reversecowgirl vaginal
    with fade
    if CONDOM:
        show samantha reversecowgirl vaginal condom
    samantha.say "Agh- ahh!"
    "I only hesitate for a moment, but when my brain registers her cries as desire instead of pain, I keep going. Her wetness helps guide me along."
    "She's warm, and I need more. I push in and out hard, our bodies slapping together in passion; the sound mixes with our moans."
    show samantha reversecowgirl speed
    "Her insides grip at me, sucking me inside of her like nothing else. I realize my eyes are screwed shut and pry them open."
    "Samantha's face is slack with indulgence. Her face is red along with her chest. Her breasts bounce with each thrust, nipples hard."
    samantha.say "Ah... [hero.name]."
    show samantha reversecowgirl pleasure
    "I'm slipped over onto my back, dizzy. When I come to my senses, she's on top of me her ass facing me."
    "I groan at the action."
    "Taking control, she bounces up and down. My dick is as hard as it will go, and I'm at the edge."
    "My hands find their way to her hips. My fingers dig into her skin, her plush flesh easily giving way."
    "I can feel it coming. The pressure builds low. I need release."
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake! I- I'm gonna-"
    else:
        mike.say "Sam! I- I'm gonna-"
    "My limbs go limp, my lower half spasms. I can feel myself gasping."
    show samantha reversecowgirl orgasm
    "There's a rushing in my ears, my vision blackens at the edges at the overwhelming satisfaction."
    menu:
        "Pull out" if hero.sexperience >= 15:
            "As much as I don't want to, something in the back of my mind is tugging at me."
            show samantha reversecowgirl -vaginal -speed cumshot with vpunch
            "I slip out of her slick tunnel just in time as hot semen spills out of me and stains her inner thighs."
            with vpunch
            samantha.say "Ah- [hero.name]. You're so warm."
            show samantha reversecowgirl -cumshot cum onbody with vpunch
            "Her cheeks are still burning red, but her eyes are drooping."
            "She runs a shaky hand through my tangled hair and pulls me up for another kiss."
            "Samantha's lips are plush, her mouth just as soft."
            "It's almost like I'm dreaming- but I'm definitely not."
            "I feel tired- Sam really wore me out."
            "I collapse next to her on the bed and she looks over at me."
            "I clear my throat."
            hide samantha reversecowgirl
            show cuddle samantha
            with fade
            mike.say "Um-"
            samantha.say "Shh."
            mike.say "But-"
            samantha.say "The second I start thinking about what we just did, I'll freak out. I just want to... enjoy this."
            mike.say "... Alright."
            "Samantha's shoulders relax and she turns onto my chest, breathing in deeply."
            "I can't really help the increasing weight of my eyes."
            "Darkness settles over my mind, Sam as my welcoming blanket."
        "Cum inside":
            show samantha reversecowgirl orgasm creampie -speed with vpunch
            if not CONDOM:
                "I spill into her."
                if samantha.impregnate(force=True, secret=True):
                    $ samantha.flags.pill = False
                    $ samantha.hide()
                    $ samantha.flags.unknown_father = True
            else:

                "I spill into the condom."
            with vpunch
            "The pressure finally comes loose, unwinding. My hearing slowly returns and I find myself staring at my ceiling, breathing heavy."
            "Sam is on top of me, collapsed, and I feel warm for a whole different reason."
            "My crush from the past- I've finally won her back."
            hide samantha reversecowgirl
            show cuddle samantha
            with fade
            "My arms wrap around her back."
            "We're both exhausted."
            "Her hair is everywhere, strands falling over my face."
            "I can't bring myself to care, focusing on the heaviness of my eyelids."
            "I fall into darkness, happily embracing the sleep that comes shortly after."
    scene bg bedroom1 at blur(16), dark, dark with dissolve
    pause 1.0
    samantha.say "..."
    samantha.say "Ew."
    "Samantha's hands move over my chest."
    "I hear her moving on top of the covers uncomfortably."
    samantha.say "Ew."
    "Her words finally break through the haze of sleep."
    scene bg bedroom1
    show samantha naked annoyed
    with dissolve
    "My eyes flutter open to see her not looking at me- thank god- but at her legs."
    "Oh yeah. We never did clean up, did we?"
    mike.say "Ew? It's not that bad."
    "Sam looks up at me with a mix of disgust and a half hearted glare."
    show samantha sad
    samantha.say "When it's cold and sticky, it is!"
    mike.say "Okay. Point taken."
    mike.say "The bathroom should be open if you wanna... clean up."
    show samantha normal
    "Samantha nods."
    samantha.say "A shower would be nice."
    "Despite sitting up slowly, black skirts at the edge of my vision."
    "I wait a moment for the head rush to pass, and when it does, Sam's standing at the edge of my bed."
    "She's trying not to let her thighs rub together as she walks but... in her case, that's kind of impossible."
    "When she gets to the door, she hesitates for a moment, before grabbing a stray blanket and wrapping it around herself and leaves the room."
    hide samantha with dissolve
    "That leaves me with my thoughts."
    "I should feel bad for Ryan- and I do, to some extent."
    "He let himself lose the perfect girl. That was his fault."
    "If a sweet girl like Sam would let her loyalty fall through, he must have really been a dick these past weeks."
    "Maybe I could finally tell her what I saw with Ryan... was this a good time?"
    "I don't think any time is 'good'. But I felt more confidence now. She wanted to be with me, right?"
    "A few minutes pass, and I throw on yesterday's clothes- I'll just shower after her."
    "Pulling the t-shirt over my head, I furrow my brows at the growing conflict."
    "There's no way I would get through telling Samantha about Ryan without her breaking down into tears."
    "I never want to see her like that. Maybe I really should just keep it to myself."
    show samantha naked with dissolve
    "Before I can make up my mind, my bedroom door swings open. Sam's hair is damp, dripping with water, and pulled into a ponytail, with a fluffy white towel wrapped around her chest."
    "She looks much happier now that she's clean."
    "But when her eyes land on me, they grow harder as if she doesn't know what to say."
    "I don't know what to say. We definitely can't just leave it like this."
    show samantha -naked with dissolve
    "She starts pulling on the clothes she had on last night."
    menu:
        "Tell her Ryan cheated" if hero.flags.knows_ryancheats:
            $ samantha.flags.knows_ryancheats = True
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake... we need to talk."
            else:
                mike.say "Sam... we need to talk."
            show samantha sad
            samantha.say "You're right. We shouldn't have done this."
            mike.say "No! I mean- yes. But, no. Not about that."
            show samantha surprised
            samantha.say "What do you mean?"
            "I realize just saying it won't convince her, especially after last night."
            "I grab my phone off of the night-stand, remembering the picture I took."
            samantha.say "Is something wrong?"
            mike.say "I think I know why Ryan's been so distant."
            "Samantha looks confused, but doesn't say anything. I swipe open my phone, my finger hovering over the picture from the bar."
            if "samantha_event_04" in DONE:
                mike.say "I saw Ryan at the bar. With another girl."
            else:
                mike.say "I saw Ryan at the wedding. With another girl."
            samantha.say "..."
            "I turn the screen to her, the dark image lighting up her paled face. Her pupils dilate when she spots Ryan."
            samantha.say "..."
            samantha.say "When did this happen?"
            "I open my mouth to answer, but quickly close it in realization."
            samantha.say "How long have you known about this?"
            mike.say "Um... for a while."
            samantha.say "You've known about this... and you didn't tell me?"
            "Guilt washes over me at her words."
            show samantha angry
            samantha.say "I just got married! And you didn't even tell me before the wedding."
            menu:
                "You're not much better":
                    "I suddenly feel upset. Does she know where she is right now?"
                    mike.say "Do you think you're much better than him? You just went behind his back."
                    mike.say "You can't be mad when you do the same thing to him."
                    show samantha sad
                    samantha.say "I- that's not-!"
                    "I seem to have hit her hard. Her wide eyes shine with guilt."
                    samantha.say "No, no..."
                    show samantha cry
                    "Tears start pouring down her face with now end. She forcefully wipes at her cheeks, but to no avail as it's only replaced with more."
                    "Samantha snatches her phone from somewhere off the ground, where it must have fallen with her clothes."
                    if samantha.flags.nickname == "cupcake":
                        mike.say "Cupcake- wait!"
                    else:
                        mike.say "Sam- wait!"
                    hide samantha with dissolve
                    "But the door is already shutting behind her. I jump off the bed and chase after her."
                    scene bg livingroom with fade
                    play sound door_slam
                    "By the time I get to the hallway, I hear the front door slamming. Shit."
                    $ samantha.love -= 20
                    $ samantha.flags.nokiss = False
                "I'm sorry":

                    if samantha.flags.nickname == "cupcake":
                        mike.say "You're right. I'm sorry. Really, Cupcake, I'm so sorry I didn't tell you."
                    else:
                        mike.say "You're right. I'm sorry. Really, Sam, I'm so sorry I didn't tell you."
                    samantha.say "What the hell, [hero.name]? What were you thinking?"
                    mike.say "I was thinking that I wanted you to be happy. I didn't want to let Ryan bring you down like that."
                    show samantha sad
                    "She goes silent at that, and eventually sighs. Samantha sits next to me on the bed. I try not to look at her, until I hear a sob."
                    if samantha.flags.nickname == "cupcake":
                        mike.say "Oh, Cupcake."
                    else:
                        mike.say "Oh, Sam."
                    show samantha cry
                    "I put an arm around her. She dives into my shoulder and cries."
                    samantha.say "What do I do, [hero.name]? I- I don't know what to do anymore."
                    mike.say "Whatever you think is right. I want you to be happy. That's all that matters."
                    "We stay there for a while after that. Her sniffles fill the room as the sun rises into the night, but I finally feel that weight lift off of my chest."
                    $ samantha.flags.unknown_father = False
                    $ samantha.flags.excused = True
                    $ samantha.unhide()
        "Say nothing":

            if hero.flags.knows_ryancheats:
                "It's better to not say anything."
                "If Ryan couldn't handle it himself, then why should I be the one to break the bad news?"
                "His commitment issues were officially not my problem."
            samantha.say "[hero.name]."
            "I look up at the mention of my name."
            samantha.say "We need to talk."
            "I'm already dreading this conversation."
            mike.say "Yeah... I know."
            samantha.say "About Ryan-"
            mike.say "If you want to tell him about this, you can."
            mike.say "I won't be mad. You can blame all of this on me."
            show samantha sad
            samantha.say "No, no! This is just as much my fault."
            samantha.say "I just... don't know what to say. I feel guilty for betraying him like this, but I also want you."
            mike.say "... me?"
            show samantha normal blush
            samantha.say "Yes, you. I want all of this to work out. I don't want anyone to be upset."
            samantha.say "I especially don't want you and Ryan to lose your friendship because of me."
            "'Friendship' is a strong word, but I don't correct her."
            "She goes quiet, seemingly lost. A terrible idea pops into my head and I'm suggesting it before I can shut the fuck up."
            mike.say "You know what would help you guys fix things?"
            samantha.say "Hm?"
            mike.say "Mix things up. Tell him you want something new."
            samantha.say "Like what?"
            mike.say "How about a threesome?"
            show samantha surprised
            "That might work, for Ryan at least. He can find another girl to take to bed with Samantha. That would probably peak his interest."
            samantha.say "..."
            "Did I overstep my bounds? Now that I think about it, Sam doesn't want to hear about other girls-"
            samantha.say "Are you sure?"
            mike.say "Yeah, why not."
            samantha.say "You really think Ryan would be into that?"
            mike.say "I have no doubts."
            show samantha normal
            "Samantha stares at me, narrowing her eyes. I feel relieved that she didn't get angry at my proposal."
            samantha.say "I guess I don't mind... this could work."
            mike.say "Sweet."
            samantha.say "I... I'll call him right now. I should see him at home!"
            mike.say "Uh, okay."
            samantha.say "Thanks, [hero.name]! I'll let you know what he says."
            mike.say "You really don't need to do that-"
            hide samantha with dissolve
            "She's already gone, phone pressed up against her ear."
            "What have I done? Did I just tell Sam to have sex with more people that weren't me? I should advocate for myself more often."
            "I ignore the feeling in the back of my mind that's telling me it was a bad idea."
            if hero.flags.knows_ryancheats:
                "Ryan would definitely agree, and he would probably bring along that girl I saw him with at the bar. Oops."

    $ samantha.flags.cuck_ryan = True
    $ samantha.sexperience += 1
    return

label samantha_event_B04:
    if samantha.love.max < 200:
        $ samantha.love.max = 200
    $ samantha.unhide()
    $ samantha.flags.tellpregnant = 2
    play sound cell_vibrate
    "..."
    queue sound cell_vibrate
    "It vibrates again."
    "Whoever it is can wait."
    "I shove the phone into my pocket..."
    scene bg livingroom with fade
    "I can hear the rain from inside."
    "Where was my umbrella?"
    "I look around the front for a few moments before I conclude one of my roommates used it or lost it somewhere."
    "Sighing, I turn the knob and pull open the door."
    scene bg black with dissolve
    scene bg house
    show samantha casual cry
    with wiperight
    "..."
    samantha.say "... [hero.name]."
    "Samantha stands outside in the rain, barely covered by the porch roof."
    "Her hair is wet and her clothes are dotted with raindrops."
    "She's shivering, arms wrapped around her middle."
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake? What are you doing here?"
    else:
        mike.say "Sam? What are you doing here?"
    "I didn't really understand."
    "I was almost expecting to never see her again at this point."
    "But here she is."
    "Inspecting closer, I realize she probably walked here."
    show samantha sad
    samantha.say "I need to talk to you."
    "The idea of work flew out of my mind."
    scene bg livingroom
    show samantha casual sad at right
    with fade
    "I stepped aside, letting her in. She was being..."
    "Unusually serious."
    "It was hard to tell if she was going to give me horrible news or not."
    "I start walking to the couch, figuring she'd want to sit down."
    "She stays by the door."
    "I stare at her for a few long seconds."
    samantha.say "I... um."
    samantha.say "I'm pregnant."
    "..."
    "What?"
    mike.say "Oh."
    mike.say "Congratulations."
    "It slips out before I can process what she even says."
    "Her lack of expression gives me the much needed time to come to terms."
    mike.say "Oh."
    "By the way she's been talking about Ryan, it doesn't sound like they've been spending a lot of personal time together."
    "Now that I think about it, we didn't even use a condom."
    mike.say "You think it's mine?"
    samantha.say "I don't know."
    "I take a few steps closer to her."
    "It looks like she wants to back away and the wall behind her stops her."
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake I-..."
    else:
        mike.say "Sam I-..."
    "What can I even say?"
    "It's like I can physically feel my world crashing down around me."
    "Did I just... ruin Sam's marriage?"
    "Or worse, her life?"
    "It's no use thinking like this."
    mike.say "I'll get you a towel."
    scene bg livingroom at blur(16), dark, dark with dissolve
    "Before she can say anything else, I rush to the linen closet and grab one of our fluffiest towels."
    scene bg livingroom
    show samantha casual sad at right
    with dissolve
    "When I come back, she's still standing in the same spot."
    "I hand it to her. Samantha takes it silently and holds it numbly in her hands."
    mike.say "What are you going to do with it?"
    show samantha surprised
    samantha.say "What?"
    mike.say "I mean... do you have a plan?"
    show samantha sad
    samantha.say "I just ran here from my fucking home. Does it sound like I have a plan?"
    "I don't think I've ever heard her swear before."
    "It sounds wrong coming out of her mouth."
    if samantha.flags.nickname == "cupcake":
        mike.say "I'm so sorry, Cupcake."
    else:
        mike.say "I'm so sorry, Sam."
    show samantha annoyed
    samantha.say "I don't want to hear it. This... I'm just as guilty as you. I can't lie to Ryan- I won't."
    show samantha sad
    samantha.say "I just want to know... if it really is yours, will you be here? Or am I going to be alone?"
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake..."
    else:
        mike.say "Sam..."
    menu:
        "I'll be there.":
            if samantha.flags.nickname == "cupcake":
                mike.say "Every step of the way, Cupcake. I wouldn't leave you like that."
            else:
                mike.say "Every step of the way, Samantha. I wouldn't leave you like that."
            hide samantha
            show samantha close pregnant cry
            "Sam nods, tears finally falling from her lashes, mixing with heavy rain. She rushes forward and throws her arms around me."
            samantha.say "Thank you- thank you."
            mike.say "Here's what we'll do, okay? We'll set up an appointment for you and get a real strategy. Then we can go from there."
            show samantha sad
            samantha.say "Okay."
            mike.say "Do you... want to keep it? With Ryan?"
            samantha.say "Keeping it? That's not even a question. I can't just get rid of it."
            samantha.say "It's not some trash left over- this is a person. If Ryan wants one or not, I'm keeping it."
            mike.say "I- alright."
            play sound cell_vibrate
            "My phone buzzes in my back pocket. I quickly turn my phone off."
            mike.say "Do you want to stay here? You could probably do with some de-stressing. Tea?"
            samantha.say "..."
            samantha.say "Sure."
            "Her sobs were subsiding the more we talked. Samantha's face was contorted, trying not to have a full blown freak out."
            mike.say "I don't want you to worry about Ryan, okay. I'll take everything for you- we can say it's my fault. That you weren't in the right mind."
            samantha.say "No. I feel guilty enough. I have to tell Ryan, and I will."
            mike.say "Alright. If you need me there, I will be."
            show samantha normal
            samantha.say "Thank you."
            scene bg kitchen with fade
            "I get Samantha settled on the couch and go to make tea for her."
            "As I grab spoonful after spoonful of sugar, I try not to overthink this, or think at all."
            "If it wasn't mine, then there was nothing to worry about other than Ryan being pissed with me."
            if hero.flags.knows_ryancheats:
                "At the same time, I still had dirt on him."
                "Pulling that out could result in a less than pretty black eye, but... okay, I'm definitely overthinking."
                "What Samantha needs is someone to lean on. If I had to be that person, then so be it."
        "There's no way.":
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake- what? There's no way either of us can do this. Not even you and Ryan."
            else:
                mike.say "Sam- what? There's no way either of us can do this. Not even you and Ryan."
            mike.say "You're still studying in university, I need roommates to pay for my house, and you just got married. Where is this money going to come from?"
            samantha.say "..."
            mike.say "I think you should work this out with Ryan. You two are a couple. You have parents that can help you out. It's better if I stay out of this."
            show samantha surprised
            samantha.say "Even if it's yours?"
            mike.say "..."
            mike.say "I-"
            show samantha sad
            samantha.say "I get it. Goodbye, [hero.name]."
            hide samantha with moveoutright
            "Before I can stop her, she's back out the door, running down my street. I fucked up, didn't I?"
    scene bg black with dissolve
    return

label samantha_event_C01:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Samantha")
    if not result:
        $ hero.cancel_event()
        $ samantha.love -= 5
        return
    if samantha.love.max < 170:
        $ samantha.love.max = 170
    samantha.say "Hey, [hero.name]!"
    mike.say "Hey!"
    samantha.say "How's your morning?"
    mike.say "Fine. yours?"
    samantha.say "Good!"
    samantha.say "I have another question for you."
    mike.say "Shoot."
    samantha.say "Do you like my piercings?"
    menu:
        "They're great":
            $ samantha.love += 1
            mike.say "They're fine with me. it's sexy on you."
            samantha.say "Wow! Thanks <3"
        "I'd rather you not wear them":
            $ samantha.love -= 1
            mike.say "I don't know. they don't really suit you."
            samantha.say "Oh. Alright then."
    samantha.say "Hmm~"
    samantha.say "How many girls have you had sex with?"
    mike.say "..."
    mike.say "Whoa. over text?"
    samantha.say "It's important!"
    mike.say "Well..."
    menu:
        "I can't even count":
            $ samantha.love -= 1
            mike.say "I can't really give a number. too many to count."
            samantha.say "Oh..."
        "A few":
            $ samantha.love += 1
            mike.say "A few here and there."
            samantha.say "Oh. Who?"
            mike.say "No."
            samantha.say "Okay. Sorry."
        "Just you":
            mike.say "Honestly, just you."
            samantha.say "..."
            samantha.say "Really?"
            samantha.say "That's... so sweet, [hero.name]!"
            $ samantha.love += 2
    samantha.say "So."
    samantha.say "Do you mind incense or candles?"
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake?"
    else:
        mike.say "Sam?"
    samantha.say "Yes?"
    mike.say "Why are you asking me all this?"
    samantha.say "Because I need to know! We all do!"
    mike.say "What??"
    samantha.say "My shift starts in a few minutes, I'll have to talk to you later."
    "But let me know!"
    "..."
    "I don't know what that's supposed to mean. These questions about my... preferences haven't stopped. At first, I was fine with answering them."
    "I thought she was mostly curious and I'm not going to say no if she wants to spend another night with me."
    "But now it's a little too much. Maybe I should visit her once she's done with work and ask her what this is all about."
    return

label samantha_event_C02:
    if samantha.love.max < 200:
        $ samantha.love.max = 200
    "The bakery has the usual smell; cinnamon, sugar, and freshly baked cakes."
    "It's welcoming enough as I open the glass doors."
    "I don't see Samantha at the counter- she must be in the kitchen today."
    "I check the time on my phone- only ten minutes until she's off work."
    "I guess I can wait at one of the tables."
    "Before I take a seat near one of the windows,I order a small cup of coffee."
    "The chair lightly scrapes the floor as I pull it out and sit."
    "Now all there is to do it wait."
    show ryan casual annoyed zorder 2 at center with dissolve
    ryan.say "You."
    "I look up. Ryan? What was he doing here?"
    mike.say "Me?"
    ryan.say "You."
    show ryan casual annoyed at center, zoomAt(1.5, (640, 1140))
    "He takes the chair at the opposite side of the table and sits. Um-"
    ryan.say "What do you think you're doing?"
    "I blink slowly. I try to wrack my brain, thinking of anything I could have done wrong within the last week."
    "Other than fucking his wife, but it's not like he doesn't deserve it."
    mike.say "... Sitting?"
    "He doesn't seem to like that response."
    ryan.say "No. Are you serious?"
    mike.say "Can you explain please?"
    "He leans in, as if to tell me a secret."
    show ryan casual angry
    ryan.say "You. You told Sam a threesome was a good idea."
    "Oh."
    mike.say "She was asking for advice."
    ryan.say "And you tell her shit like that?!"
    mike.say "It was just a suggestion, dude."
    ryan.say "And now she's got it in her head that it's a good idea!"
    mike.say "Are you of all people saying you wouldn't be into a threesome?"
    ryan.say "Where the hell would you get the idea that I would want to do that with-"
    show samantha casual zorder 1 at right with dissolve
    samantha.say "Ryan!"
    "Sam appears at the side of our table, apron still on and flour dusting her cheeks. She notices me."
    samantha.say "[hero.name]! You're here too?"
    mike.say "Yeah... I just wanted to talk to you."
    samantha.say "Oh! Me too."
    "She clasps her hands together and looks at me, as if waiting for me to start."
    mike.say "Uh...-"
    "It wouldn't be a good idea to have this conversation in front of Ryan."
    mike.say "Maybe we could go somewhere more... private?"
    "Ryan looks like he wants to say something, but Samantha cuts him off."
    samantha.say "Sure! How about we all head home and we can talk there."
    mike.say "That seems a little-"
    show ryan casual annoyed
    ryan.say "No. I agree. We can get a few things settled there."
    "I'm surprised when Ryan speaks. Now I was intrigued."
    mike.say "... Fine."
    ryan.say "Good."
    hide ryan
    show ryan casual annoyed
    "He stands, a smug look plastered on his face. Samantha smiles at me and gets up after him."
    samantha.say "Let's get there!"
    "She grabs my hand and pulls me up, her touch lingering."
    hide samantha
    "Ryan's smug expression turns into a glare."
    scene bg street with fade
    scene black
    play sound car_door
    pause 0.4
    play sound car_door
    queue sound car_ignition
    scene bg street with fade
    with vpunch
    "We all pile into Ryan's car- which I would never admit is nicer than mine but it is- and quickly make our way to their house."
    "The atmosphere is tense, almost making me want to leap out of the car at the next light."
    "Sam doesn't seem to register it at all, tapping away on her phone with a satisfied smile."
    "We come to a stop in my driveway."
    "Ryan kills the ignition and immediately gets out."
    samantha.say "Let's go!"
    "I nod, nerves starting to get to me. I get out anyway."
    scene bg samhome
    show samantha casual at left5
    show ryan casual annoyed at right5
    with fade
    "We all get through the front door and pile into the living room."
    show samantha casual
    "Samantha gestures to the sofa."
    "I reluctantly take a seat."
    "Ryan sits across from me in the armchair with Sam next to me on the cushion."
    samantha.say "So-"
    ryan.say "Are you stupid?"
    "I blink in confusion."
    "Ryan's usually insulting me but most of the time with clear reason."
    mike.say "Um...?"
    "I look between both of them rapidly."
    mike.say "Are you seriously that upset about the threesome thing?"
    mike.say "Because you didn't have to take that seriously-"
    show ryan angry
    ryan.say "Why the hell wouldn't I take that seriously?!"
    show samantha casual annoyed
    samantha.say "Ryan! When I said I wanted to us to talk with [hero.name] you said you would hear everyone out. Now is that time!"
    "Ryan deflates, leaning back in his chair."
    show ryan casual annoyed
    ryan.say "Fine. Whatever."
    ryan.say "I just want to know... you're not joking about this? You really want to? Because it's not funny."
    "My brain whirs, trying to piece this together. What?"
    show samantha casual normal
    "Samantha laces her fingers together and puts her hands on her lap."
    samantha.say "He was very serious! I was surprised too, but this is a good idea, Ryan!"
    "Oh."
    mike.say "Wait-"
    menu:
        "I'm interested":
            "That's... not what I meant. Not at all. But if they're really asking..."
            mike.say "Uh, yeah. I'm interested."
            show samantha happy
            "Samantha's face softens."
            samantha.say "See! I told you he meant it."
            show samantha normal
            ryan.say "..."
            ryan.say "Alright."
            mike.say "Alright?"
            ryan.say "Whatever. Sam has rules though."
            show samantha casual annoyed
            samantha.say "It's not rules! It's more like... a checklist."
            mike.say "Wait. So is that why you've been asking me all those questions lately?"
            show samantha flirt
            "Samantha sheepishly nods."
            samantha.say "I'm sorry. I didn't make that sound very clear, did I?"
            samantha.say "But now that we're all in agreement...!"
            "Sam takes a printed sheet out of her purse."
            "She hands it to me, and I take it gingerly."
            "I quickly scan it, and my eyes widen."
            "Pretty much all of the questions she's asked me over the past few days are accumulated here along with other- and more medically inclined."
            "Stuff about past partners, STDs-"
            samantha.say "I want you to fill that back so Ryan and I can know how to go about things!"
            samantha.say "Once you do we can... schedule something when we're all free."
            show samantha happy blush
            "As I look up from the sheet, Samantha winks at me. A shiver goes down my spine. Looks like I have homework."
            $ game.flags.sam_ryan_threesome = True
        "That's not what I meant":
            mike.say "No. No, no. That's not what I meant. Not in a million years."
            show samantha surprised
            "Sam's eyes widen and the glare falls back onto Ryan's face, though a hint of smugness comes with it too."
            mike.say "I meant- like- ya know? With another girl!"
            samantha.say "Another... girl?"
            "Samantha seems conflicted with that idea, as if it's never occurred to her. She turns to Ryan with genuine curiosity."
            samantha.say "Would you...?"
            "She pauses, not knowing how to ask. Ryan seems to take this as a challenge."
            show ryan casual angry
            ryan.say "Really?! You think I'd want to be with any other girl than Sam?"
            ryan.say "You must not be paying attention, [hero.name]."
            show ryan casual annoyed
            ryan.say "Thanks, but no thanks- your advice is unnecessary."
            mike.say "Wait- are you-?"
            ryan.say "I think it's best if you leave."
            mike.say "What?!"
            show samantha casual sad
            samantha.say "Ryan! He didn't mean it in a bad way!"
            show ryan casual angry
            ryan.say "I don't care, Sam!"
            ryan.say "[hero.name], get out!"
            "I don't need more of an invitation to leave. I promptly stand and head for the door."
            mike.say "See you later, Sam."
            "It comes out as a mutter to her but Ryan hears anyway."
            ryan.say "Uh, no, you won't."
            ryan.say "Stay away from my wife."
            "Responses well up in my chest, begging to be let out. But I already made my decision."
            scene bg street
            play sound door_slam
            pause 0.5
            with vpunch
            "I grab the door handle and shove it open. I quickly slam it behind me, wishing I could put more force behind it."
            "I take a deep breath as I stand on their porch. That was... awkward, to say the least."
            "Sam seemed to understand what I meant, but Ryan's being an asshole."
            "What else is new?"
    $ game.room = "street"
    return

label samantha_event_C03:
    scene bg livingroom
    "I stand by the doorway awkwardly, waiting for my two guests to arrive."
    "I can't remember the exact course of events leading up to this moment, in fact, I can't quite convince myself that I'm not dreaming, but a cautionary pinch of my arm puts those fears to rest."
    "Time seems to be moving oddly slowly, the soft ticking of the clock in the background almost painful to hear."
    "Tick. Tick."
    "I briefly consider just taking it down, getting rid of the batteries to provide me some comfort, but I'm well aware I'd just end up checking my phone every few seconds anyway."
    "Tick. Tick."
    "That doesn't mean I'm not annoyed of course, but I'm mostly just nervous. This is going to be... A weird, weird afternoon."
    "Tick. Tick."
    "Are they late? I can't remember any-more whether she said three fifteen or three thirty, it doesn't really matter I suppose, but..."
    play sound door_bell
    "In place of the familiar tick of the clock, I hear someone at the door, hitting the doorbell before I could swing it open to face them."
    scene bg black with dissolve
    scene bg house
    show ryan casual annoyed at right5
    show samantha casual at left5
    with wiperight
    "Ryan and Samantha stand on the other side, Samantha's finger still on the doorbell, and I quickly realise how awkward I look."
    "I offer a wavy smile to try and relieve the tension, Ryan shaking his head while Samantha returns it with a genuine grin that puts all my worries at ease."
    "The two quickly step inside and Ryan leads us to my bedroom before I could suggest anything else, he seems either overly eager to start, or get it over with."
    scene bg bedroom1
    show ryan casual annoyed at right5
    show samantha casual at left5
    with fade
    "Samantha simply follows along, content to do as she's told, and I don't want to start an argument now of all times so I do the same."
    "There's a few moments of silence when we all find ourselves by my bed, each of us knew exactly where this was going but it seemed like none knew how to start."
    hide ryan
    hide samantha
    show samantha kiss casual
    with dissolve
    $ samantha.flags.kiss += 1
    "Not wanting to let Ryan show me up, and also finding myself drawn irresistibly to Samantha's lips by now, I step forwards and quickly pull her into a kiss."
    "I pull her body against mine, letting her press her mounds against my chest, letting me feel her heat radiating off her even through our layers of clothing."
    "She gasps but quickly begins to return my advances, leaving Ryan the neglected third wheel, a fact which pleases me greatly."
    "I let him watch as I touch and claim his mate, my hands gripping her waist tightly, venturing down to grope her ass through her clothing."
    "My hands knead and squeeze her curvaceous form as I push her forwards, nudging her closer and closer to the bed as Ryan can do nothing but watch."
    "Soon enough we topple over, landing with a pomf on the bedsheets, though we barely leave one another's embrace, eventually parting only so I can begin lifting my shirt over my head."
    "I see Ryan step forwards out of the corner of my eye, mimicking my movements and planting his lips on Samantha's mouth, and while she kisses back with passion, she's soon turned her attention back to me as I begin undressing her too."
    show samantha kiss naked with dissolve
    "Her top is the first to go, her heaving breasts falling out into the open, protected only by her bra but I quickly rectify that problem, leaving her erect nipples to be tickled by the cool air."
    "I let my lips roam her flesh, trailing slowly down from her neck to her breasts and then lower still as I quickly slip the rest of her clothes from her body, drawing a yelp, a shudder, and a moan for my efforts."
    "I take my time exploring her, savouring her body, circling my tongue around her nipples even, leaving her soaking and needy in no time."
    "I lie back and let her return the favour, her fingers fumbling with my belt for a few moments but eventually dragging my pants from me in no time."
    "Her erect nipples brush tantalisingly against my naked chest, sending shivers down my spine before finally my cock is released from it's denim prison."
    "I can tell from the sparkle in Samantha's eyes alone that she wasn't expecting my size, let alone her gasp when she's suddenly face to face with my member."
    "I glance across to Ryan and find he's stripped down too, and the sight of Samantha moaning and writhing, even if it was under my touch, has him similarly ready to go."
    "Looking to Samantha for guidance, I find her glancing between the two of us quickly, I can practically see the cogs turning in her mind for exactly what position she wants to adopt for the two of us."
    "Eventually, she seems to have made up her mind, motioning for Ryan to come closer as she began to straddle me, positioning her ass above my waist."
    "I lie back and wait, my cock twitching in anticipation in the open air."
    "It isn't hard to see why she chose to straddle me over Ryan, I'm noticeably larger than he is down below and from the moment we arrived I've been fawning over her much more than he had."
    show samantha mmf shut with fade
    "I shiver as her cunt lightly brushes up against my rod, and smirk as I watch her do the same, Ryan rushing over to her side and ungracefully thrusting his cock towards her face."
    "Samantha almost outright ignores him for a few seconds as she braces herself, looking down towards me and grinning."
    "Slowly, she let her hips fall, my cock pressing against her tight entrance for a few almost agonising moments before her slit relented, opening and letting me slip inside, her well lubricated tunnels immediately squeezing me tightly."
    "We both gasp, and after a few seconds to grow accustomed to the sensation, to the dripping juices running down my length, to the hot, fleshy walls milking my cock, I begin thrusting, pushing Samantha to start bouncing in place."
    "She does exactly that, her ass lifting and falling as her tits began bouncing in a way incredibly pleasing to the eye."
    show samantha mmf ryan closed2 suck -shut
    "As she does, she leans over and envelops Ryan's length in one too, her nose quickly pushing down to tickle Ryan's waist."
    "I focus more on the way her ass slaps into my legs with each bounce though, the way that if I pushed my hips forwards just right I could make her squeal with pleasure even now, just as we've gotten started."
    "Samantha seems to be enjoying herself already, and I certainly know I aim to please, so, gripping her waist, I slowly begin picking up the pace."
    show samantha mmf ryan closed tongueout out
    "She moans and splutters around Ryan's cock as I expertly pleasure her, her knees already beginning to waver and grow weak under my efforts."
    "I groan as I begin to lose myself in the sea of ecstasy Samantha has already thrown herself into, my cock sliding in and out with more ease after every thrust."
    "I can feel her pussy moulding to my shape, learning my cock's size and form and milking it more effectively as a result."
    "Her flesh quickly relents under my grip as I play with her ass, giving it one or two playful slaps even as I thrust."
    "My hands send shock-waves through her body, her fat pooling in all the right places."
    "I let my other hand grasp her breasts, beginning to knead and play with them again, twisting and pulling her nipples in just the right way to make her moan around Ryan's cock."
    show samantha mmf ryan suck -tongueout
    "She's clearly struggling to focus on the blowjob thanks to my ministrations, a fact I find flares a twisted sort of pleasure within me."
    "I begin to make it my effort to distract her as much as possible, to make her squeal and moan and whimper and anything else to stop her tongue with it's no doubt expert service of Ryan's pitiful member."
    "Her wet, sopping cunt suddenly finds itself the victim of my vicious attack as I suddenly begin thrusting furiously at different angles, varying my speed, finding the perfect spots to make her shudder and scream."
    "It doesn't take long before Samantha is absolute putty in my hands, her pussy clamping down and spasming around my rod and her attention entirely focused on me rather than her husband."
    "He continues to thrust pitifully into her mouth but it's clear that Samantha's no longer servicing him with passion, instead focusing on pushing her weight down further on me, taking me deeper and deeper."
    show samantha mmf ryan oral
    "Despite this Ryan is still the first to cum, shooting his small load down her throat then backing off to leave us to it."
    show samantha mmf -ryan -oral shut face
    "I can't tell if Samantha is even aware of his absence any-more, but with nothing left to muffle them her cries fill the room more than ever."
    "We keep up our frantic, passionate lovemaking for a short while longer, but with each of us giving it our all, neither bothering to restrain ourselves in the slightest, it's only a matter of time before orgasm arrives."
    show samantha mmf closed2
    "It hits fast and hard, my vision turning white as I pump my thick, sticky load into her womb, officially marking her as mine."
    "I feel her body tense, spasm as she lets loose one final cry, finally having pushed her over the edge."
    show samantha mmf pussy up tongueout with vpunch
    "As my cock twitches her pussy spasms, working to milk me for every last drop, granting me an orgasm so intense I very nearly pass out."
    "Eventually though, as all good things do, it comes to an end, Samantha collapsing on top of me and the two of us lying there, panting in each other's arms."
    "I nearly forget about Ryan entirely until eventually, after recovering, Samantha pushes herself up and grins at him, telling him about what a good idea this had been and how much fun she'd had."
    "I smirk at him behind her back, and offer a cocky wink before he gets a chance to turn away, and soon enough, the two were gone, leaving me alone with my satisfaction."
    scene bg black with dissolve
    return

label samantha_event_D01:
    if samantha.love.max < 120:
        $ samantha.love.max = 120
    if samantha.sub.max < 60:
        $ samantha.sub.max = 60
    $ samantha.flags.cheatDelay = TemporaryFlag(True, 3)
    $ samantha.flags.nodate = False
    show bg livingroom
    "It feels like this is the first time in ages that I've had a day all to myself and with nothing to do."
    "Weird as it sounds, I tend to have to work pretty hard and plan ahead if I want to make sure that I have one!"
    "With a job, two colourful housemates and a healthy social life, I tend to be busy most of the time."
    "But today I have no work to catch up on and both [bree.name] and Sasha are out of the house for a couple of hours."
    "This leaves me free to do nothing more taxing than slobbing on the sofa, not watching whatever's on the TV screen."
    "Now that is something that I'm pretty damn good at, and before too long I have no idea what I'm even watching any more!"
    play sound door_bell
    "Maybe that's why it takes me a good couple of minutes to realise that the doorbell I can hear isn't actually on the TV."
    "Sitting up, I shake my head in an effort to get it back into reality."
    "And then I haul myself off of the sofa and begin my resentful trudge towards the front door."
    scene bg black with dissolve
    scene bg house
    show samantha casual
    with wiperight
    "But the moment that I open it, a miraculous transformation overtakes me."
    "Suddenly I feel more awake and alert than I have all day, my back straightening and energy surging through my limbs."
    "There's no real mystery to what causes this sudden change of mood and wakes me from my semi-torpor."
    "It's one hundred percent on account of exactly who I see standing on the doorstep before me."
    show samantha close casual happy
    samantha.say "Hey, [hero.name]!"
    if samantha.flags.nickname == "cupcake":
        mike.say "Ah...Hi, Cupcake."
    else:
        mike.say "Ah...Hi, Sam."
    samantha.say "Sorry to just drop on you like this!"
    samantha.say "But I was passing and I wondered if you'd be in..."
    "This explanation immediately sets off alarm bells in my mind."
    "Sam and Ryan's new place is all the way over on the other side of town."
    "And I live way too far into the suburbs for her to have been running errands around here."
    "But for all of my suspicions, that's not to say I'm anything less than thrilled to see her."
    "So I ignore everything save for that, and step hastily aside to usher her into the hall."
    if samantha.flags.nickname == "cupcake":
        mike.say "Sure...sure thing, Cupcake."
    else:
        mike.say "Sure...sure thing, Sam."
    mike.say "I'm in...as you can see!"
    mike.say "You should come in too...."
    mike.say "I mean, come in!"
    scene bg livingroom
    show samantha casual
    with fade
    "Sam smiles at my getting tongue-tied as she steps inside and I close the door behind her."
    samantha.say "I hope I'm not interrupting anything?"
    samantha.say "Because I can always come back another time..."
    mike.say "No...no, it's okay."
    mike.say "I was just taking some time out."
    mike.say "But I could use a bit of company."
    "I show her into the sitting room, which still feels a little odd to me."
    "After all, it wasn't a million years ago that she and Ryan were living here with me."
    "We stand in the middle of the room, close enough for friends and far enough apart to be platonic."
    "I see her glancing around at the decor, pausing when she notes something that's different to when she lived here herself."
    samantha.say "I see you haven't done much redecorating since we moved out."
    mike.say "I can't say we have."
    mike.say "[bree.name], Sasha and I, that is..."
    "Sam raises her eyebrows a little at the mention of my new housemates."
    samantha.say "How are you finding it, living with two girls?"
    show samantha happy
    samantha.say "I suppose that'd be most guy's dream come true!"
    "Though she asks the question in a joking manner, I can sense that there's more to it than that."
    show samantha normal
    "Sam's well aware of the fact that I have feelings for her."
    "And I know for sure that her mentioning [bree.name] and Sasha means she's fishing for a clue as to how I feel about them too."
    mike.say "Yeah, well - most guys don't have to deal with their slobby habits and dirty laundry strewn around the place!"
    show samantha happy
    samantha.say "Oh, come on, [hero.name]!"
    show samantha normal
    mike.say "Hey, I'm not saying they aren't cute girls."
    mike.say "But when you live with someone, you get to know them VERY well!"
    show samantha surprised
    "At this, Sam cocks her head on one side, a quizzical look on her face."
    samantha.say "Is that so?"
    samantha.say "Maybe I should ask what you got to know about me, huh?"
    if samantha.flags.nickname == "cupcake":
        mike.say "Sometimes it's the opposite, Cupcake."
    else:
        mike.say "Sometimes it's the opposite, Sam."
    mike.say "Sometimes you never get to know a girl as much as you'd have liked to..."
    show samantha normal
    "Sam holds my eye for a moment, and then looks away."
    show samantha sad
    samantha.say "Yeah..."
    samantha.say "About that..."
    show samantha normal
    "Sam takes a deep breath before she looks back around at me."
    samantha.say "Confession time - I kind of didn't just happen to be passing."
    samantha.say "I wanted to talk to you...about what you told me?"
    "I take a deep breath, hold it for a second and then let it out in one go."
    if samantha.flags.nickname == "cupcake":
        mike.say "Okay, Cupcake."
    else:
        mike.say "Okay, Sam."
    mike.say "We can do that."
    "Sam makes to open her mouth, but she's cut off before she can get out even a single word."
    play sound cell_vibrate loop
    "The sound of her mobile vibrating interrupts the conversation."
    "And she instinctively glances down at it in the palm of her hand."
    show samantha annoyed
    samantha.say "Shit...it's HIM!"
    samantha.say "Sorry - I have to answer it, or he'll get suspicious."
    stop sound
    "I don't need to see the screen of her phone to know that it's Ryan calling."
    show samantha normal
    samantha.say "Hey, babe - what's up?"
    samantha.say "Where am I?"
    "Sam glances at me while she says this, clearly pondering her answer."
    samantha.say "I just popped in to see [hero.name]."
    "At this, I begin to shake my head and wave my hands, urging Sam not to get me involved."
    samantha.say "Because I was passing by - that's why."
    samantha.say "I don't know..."
    samantha.say "I guess I just wanted to take one last look at the place, for old time's sake."
    "For a couple of seconds she falls silent, nodding her head and then shaking it."
    "I see Sam roll her eyes at me, letting me know that Ryan's droning on about something or other."
    "But then her face contorts into a frown, and she silently mouths an impressive tirade of profanities."
    "Clamping her hand over the phone, Sam thrusts it towards me."
    samantha.say "He wants to talk to you!"
    mike.say "WHAT?!?"
    samantha.say "He wants to talk to his old buddy!"
    samantha.say "What can I tell him?"
    samantha.say "Quick, take the phone and do it, or else he'll get suspicious!"
    "Reluctantly, I let Sam shove the phone into my hand."
    "Raising it to my ear, I try to force a smile onto my face and into my voice."
    mike.say "H...hey, man!"
    ryan.say "Hey, [hero.name], old buddy!"
    "So much of my attention is on the phone-call that I don't notice what Sam's doing at the same time."
    with vpunch
    "Suddenly I feel myself being shoved backwards, sending me tumbling onto the sofa."
    mike.say "Whoa!"
    ryan.say "Ah, what's up, [hero.name]?"
    mike.say "Nothing...nothing at all."
    mike.say "I just tripped...tripped over my own feet."
    ryan.say "Jesus, you're such a clumsy bastard!"
    show samantha bj3 lick open with fade
    "All I can do is laugh at this, while looking down at what Sam's doing to me."
    "Of course it was her that pushed me down, and now she's taking advantage of my confusion."
    "I see her kneeling before me, already tugging at my belt and unzipping my flies."
    show samantha bj3 lick up
    "Sam looks up and catches my eye, giving me a sly smile and dirty wink."
    "I try to shake my head and wave for her to stop it, but she simply ignores me, carrying on regardless."
    "Her fingers close around my cock, and she begins to pull it out of my pants."
    mike.say "SO...so, Ryan - how are you finding married life?"
    "I hear Ryan give one of his characteristic sniggers."
    "All self-satisfaction and delight at the chance to talk about himself."
    ryan.say "Great, [hero.name], just great."
    ryan.say "You have a sweet little wife to come home to every night."
    ryan.say "But you want to know a secret?"
    show samantha bj3 lick close tongue
    "By this point, Sam has my cock in her hands, stroking away at the shaft."
    "As Ryan's words reach my ear, she leans in and begins to kiss and lick at my balls too."
    mike.say "Sure, Ryan, sure!"
    ryan.say "Well, nothing else changes - nothing at all!"
    ryan.say "I'm still the same guy I was before, you know?"
    mike.say "Mmm..."
    ryan.say "I have the same feelings, desires and needs..."
    "I can't offer an answer of any kind, let alone call Ryan out as he tells me all of this."
    "And that's because Sam chooses that exact moment to run her tongue up the length of my shaft."
    show samantha bj3 blow up
    "Once she reaches the very top, she parts her lips and takes the head into her mouth."
    "Whether or not the blowjob that follow is exceptional or as ordinary as they come, I couldn't tell you."
    "All that matters to me is the fact that Sam has my cock in her mouth and is sucking away the whole time."
    "This girl that I hid my affections for while we lived under the same roof is pleasuring me in that very place!"
    ryan.say "[hero.name], you understand what I mean?"
    ryan.say "[hero.name], are you listening to me?!?"
    mike.say "Ah...y...yeah, Ryan - I hear you, loud and clear!"
    ryan.say "Just checking you hadn't fallen asleep on me!"
    show samantha bj3 blow close
    "I laugh nervously, and the sound almost turns into a gasp as Sam grabs the base of my cock."
    "While her head bobs up and down, she starts to work it with her fingers clasped around the shaft."
    ryan.say "I mean, don't think I'm a rat or anything like that."
    ryan.say "But what Sam doesn't know can't hurt her, right?"
    mike.say "Sure, Ryan, yeah..."
    mike.say "What she doesn't know..."
    show samantha bj3 blow up
    "I'm looking down at Sam as I say this, eyes wide with guilt and shame."
    "But rather than being irate at what she just heard, I see a new determination flare in her eyes."
    "And then, she begins to fellate me with a new-found energy and intensity."
    "I can feel my free hand digging into the cushions of the sofa as Sam goes at me."
    "Ryan's still droning on about some bollocks in my ear, but I can't hear a word he's saying."
    "Suddenly I feel myself about to cum, and then the sensation of Sam releasing me from her mouth."
    mike.say "Oh...oh shit!"
    show samantha bj3 lick cum tongue with vpunch
    "I watch as everything that I have hits Sam square in the face, striping her with sticky, white lines of cum."
    with vpunch
    "She manages to close her eyes in time, but her mouth is wide open, and I see it hit her tongue and lips too."
    with vpunch
    "But the whole time that it's happening, Sam wears a smile on her face and looks delighted with the outcome."
    ryan.say "Hey...what the hell!"
    ryan.say "What's the matter on your end?!?"
    ryan.say "Is Sam okay?"
    "I suppose that I should give him some credit for at least remembering to ask after his wife's safety!"
    hide samantha
    show samantha casual flirt cum
    with fade
    "But before I can say another word, Sam snatches the phone out of my hand."
    "Still licking the cum off of her lips, she puts it to her ear."
    samantha.say "I'm here, babe - no need to worry."
    samantha.say "No, no...we're both fine, really."
    samantha.say "[hero.name]'s just been baking, and he thought he'd burnt something, that's all!"
    samantha.say "I know, I know - he's such a clutz!"
    "Sam gives me a knowing wink as she says this, and runs her tongue around her lips once more."
    samantha.say "What am I eating?"
    samantha.say "Oh, [hero.name] made some cream donuts, and I tried one of them."
    samantha.say "He must have put too much in them, because the cream spurted out when I bit mine."
    samantha.say "Yeah, all over me!"
    "In watch as Sam wraps up the call, smoothly lying to Ryan about where she's been and what we've done together."
    "Sure, it feels good to be getting back at him for what he did to her."
    "And it feels better still to be on the receiving end of Sam's affections at the same time."
    "But part of me wonders if we're really no better than Ryan himself."
    "Maybe two wrongs don't make a right."
    "Or maybe I just need more convincing that they do?"
    $ samantha.flags.cuck_ryan = True
    return

label samantha_event_D02:
    if samantha.love.max < 130:
        $ samantha.love.max = 130
    if samantha.sub.max < 70:
        $ samantha.sub.max = 70
    $ samantha.flags.cheatDelay = TemporaryFlag(True, 3)
    show bg livingroom
    "As you can imagine, Sam's unexpected visit last weekend left me in a bit of a confused state."
    "On the one hand, it felt like a dream come true - the girl that I'd thought lost turning up on my doorstep out of the blue."
    "Well, that and then her proceeding to show her affection for me in a very real, very physical sense!"
    "But on the other it threw up a lot of questions in my mind, most of which I just couldn't answer."
    "The foremost of these was just what Sam's intentions towards me might be right now."
    "I was the one that told her about Ryan's getting a blowjob on their wedding day."
    "So I could have understood Sam wanting to pay him back in kind."
    "And me being the most obvious choice of who to do it with too."
    "But what bugged me was whether there could be more to it than that."
    "If not, I wasn't sure that I could be okay with just being used to get back at another guy like that."
    "Fun as it was for me, I told Sam all of that out of friendship."
    "Well...that and the fact that I've always held a torch for her, of course!"
    play sound door_bell
    "All of this means that when I hear the bell at the front door, I'm more than a little preoccupied."
    "It's only when I make it to the door and happen to glance at the calendar on the notice-board that it hits me."
    "That's the weekend, same as Sam's last visit."
    "A quick look at my phone tells me it's around the same time in the afternoon too."
    "No, I think as I open the door, surely not?"
    scene bg black with dissolve
    scene bg house
    show samantha casual happy
    with wiperight
    samantha.say "Hey, [hero.name]!"
    "Yeah, there she is, as large as life."
    if samantha.flags.nickname == "cupcake":
        mike.say "Ah...Hi, Cupcake."
    else:
        mike.say "Ah...Hi, Sam."
    "She smiles broadly at me, waiting patiently for me to invite her in."
    mike.say "Is it just me, or are you getting a sense of Deja vu as well?"
    "Sam laughs and waves a hand in front of her, dismissing my concerns."
    samantha.say "Yeah, I know - same time and place!"
    samantha.say "But that's how I knew I had to come see you again."
    mike.say "Huh?"
    mike.say "I don't follow..."
    show samantha normal
    samantha.say "Let me explain!"
    samantha.say "I was driving along the same stretch of road at the same time as last week."
    samantha.say "And it got me thinking about you and this place."
    samantha.say "And the last time I was here..."
    "Sam lets those words sink in, as we both recall very well just what happened on that occasion."
    show samantha blush
    "She blushes a little, and then hurries on with her explanation."
    samantha.say "Well...it reminded me that I left something behind when I left."
    samantha.say "So I just thought I'd swing by and get it."
    "The whole thing sounds plausible, so I decide to give Sam the benefit of the doubt."
    scene bg livingroom
    show samantha casual
    with fade
    "As I show her in, a thought does occur to me though."
    mike.say "How did you know that I'd be in?"
    mike.say "I mean, you could have called ahead to check."
    "Sam shrugs, brushing the question off as she walks past me and into the sitting room."
    samantha.say "Like I said, it was just a spur of the moment thing."
    samantha.say "I could have asked one of your housemates, or else pushed a note through the door."
    "Again, plausible enough."
    "Wait a minute, what am I doing here?"
    "Why am I scrutinising every word she says?"
    "After all, this is a perfect excuse to spend a little more time alone with her."
    "Just then, another thought pops into my mind, and I begin to glance over Sam's shoulder and out the window."
    mike.say "You did come here alone, didn't you?"
    mike.say "Ryan's not waiting in the car, is he?"
    show samantha casual happy
    "Sam throws back her head and laughs at my apparent paranoia."
    samantha.say "No, [hero.name], he's not!"
    show samantha normal
    samantha.say "And you can stop worrying about him too."
    samantha.say "He doesn't suspect a thing!"
    "Sam sits herself down on the sofa, patting a spot by her side for me to join her."
    "It seems a pretty relaxed way to go about searching for whatever she lost."
    "But I shrug off the thought and sit down as instructed."
    show samantha close
    "Come to think of it, Sam's not even mentioned just what it was she's looking for."
    mike.say "Erm...so, what was it that you left behind?"
    "Sam's grin becomes suddenly wider, even looking a little predatory to my eyes."
    "She leans in so close that I can feel her warm breath against my cheek."
    "And then I also feel the sensation of her hand, rubbing and squeezing my groin."
    show samantha flirt blush
    samantha.say "Oh, don't worry."
    samantha.say "I think I found it already!"
    hide samantha
    show samantha kiss casual
    with dissolve
    $ samantha.flags.kiss += 1
    "Before I can say another word, Sam leans in and kisses me square on the lips."
    "A part of me knows that this is wrong, as she's still a married woman."
    "But that better part loses out to the one that's always been crazy about her."
    "All the time the kiss is going on, I can feel Sam opening my flies and slipping her hand inside."
    "She's massaging my cock a moment later, not needing to do too much work to get it hard."
    hide samantha
    show samantha casual flirt close
    with dissolve
    "By the time Sam breaks off the kiss, she already has it out and gripped in her hand."
    "I fall back on the sofa, gasping for air."
    show samantha bj4 lick rest with fade
    "A little from being short of breath, and a little from the sensation of her fingers working my dick."
    samantha.say "Mmm..."
    samantha.say "That's what I came back to find, [hero.name]."
    samantha.say "The feeling of your cock in my hand!"
    samantha.say "And the taste of it on my tongue..."
    mike.say "Well...I...I'm glad you found what you wanted!"
    "Sam smiles at this, biting her lip in anticipation as she glances from my eyes and down to my cock."
    "And then she leans forward to kiss the base of the shaft, licking around it a moment later."
    "Slowly and with infinite attention to what she's doing, Sam begins to trace a line upwards."
    show samantha bj4 lick rest up
    "She makes a satisfied sound at the end of each and every lick."
    "And her eyes hold mine the whole time, large and full of desire."
    "They only close once she reaches the very top, her gaze moving down."
    "Sam does this as she finally takes the head of my cock into her mouth."
    "I can vividly recall the feel of her tongue from the last time we did this."
    "And yet somehow it feels all the more intense and incredible this time around."
    "Before Sam was perhaps a little hesitant, all of this being new to us."
    "But there seems to be no such issue on this occasion."
    "She swallows me deeper and with such confidence that I can't help gasping in genuine surprise."
    "I look down at Sam, still finding it hard to believe that this is happening at all."
    "And maybe she senses that my eyes are on her and begins to put in that much more effort."
    "Sam squeezes my balls with one hand, making me flinch in pleasant surprise."
    show samantha bj4 lick phone
    "But it's only then I notice what her free hand is actually doing at the same time."
    if samantha.flags.nickname == "cupcake":
        mike.say "Ah...Cupcake..."
    else:
        mike.say "Ah...Sam..."
    mike.say "What are you doing?!?"
    "Now my eyes are firmly fixed on the mobile in Sam's hand."
    "I watch in horror as she flicks to the contacts and calls a number."
    "She does all of this without even looking at the phone, making me think that she's practiced this beforehand."
    "And then she holds it up, clearly expecting me to take the damn thing from her."
    "I go to do just that, but then I see the name above the number."
    mike.say "What the hell?"
    mike.say "Are you crazy?!?"
    "She's calling Ryan!"
    "Right now, and with my cock in her mouth, she's actually calling him!"
    "Sam ignores my cries of alarm, letting my cock slide out of her mouth."
    "In the few moments that I have before the call connects and he picks up, my mind races."
    "I could take the thing and toss it aside - but what would that get me?"
    "Sam's hell-bent on revenge, and whether I like it or not, it looks like she's decided I'm in on it too."
    "And if I don't play along, would she tell Ryan all about what we've already done?"
    "I make a split-second decision that it's just not worth the risk."
    ryan.say "Hello, baby!"
    ryan.say "Where have you gotten to?"
    "I take a deep breath, waiting for Sam to start speaking."
    "Trying as hard as I can not to make a sound like a guy getting a blowjob from his friend's wife."
    "Like I'd even know how that would sound..."
    show samantha bj4 lick phone closed shut
    samantha.say "Hey, baby!"
    samantha.say "Guess who I'm with right now?"
    "There's a pause on the other end of the line."
    "And in my mind I can only picture Ryan's face as the penny finally drops."
    ryan.say "Don't tell me, you're with [hero.name]?"
    samantha.say "Right first time - what are the chances, huh?"
    ryan.say "Don't tell me you're over there making a nuisance of yourself again?"
    "Sam laughs, shaking her head as she does so."
    ryan.say "I'm your husband, for god's sake."
    ryan.say "You're supposed to spend all of your time harassing me!"
    samantha.say "I guess I just can't keep away!"
    ryan.say "Well, you shouldn't impose on [hero.name] for too much longer."
    ryan.say "Or he can give you a proper mouthful, and with my blessing too!"
    "I can't help looking down as Ryan speaks the words, noting what Sam actually has in front of her face."
    show samantha bj4 lick phone smile up
    samantha.say "Don't sweat it, Ryan - I'm sure he will!"
    ryan.say "Where in the hell is he, anyway?"
    ryan.say "Aren't you going to put him on the phone?"
    "I want to shout out loud a moment later, as I can tell that I'm on the brink of cumming..."
    menu:
        "Push her head":
            show samantha bj4 deep phone deepclosed
            "Almost without thinking, I reach out my free hand and grasp the back of Sam's head."
            $ samantha.sub += 5
            "I push her down suddenly, making her take the head into her mouth once more."
            "But I don't stop there, and instead keep on going, forcing my cock even further down her throat as I do so."
            "Sam makes a muffled, almost strangled sound as she's made to deep-throat my cock."
            ryan.say "What in the hell was that?!?"
            "I reach out and snatch the phone from Sam's flailing hand."
            show samantha bj4 deep rest deepup
            mike.say "It was Sam."
            mike.say "I think something went down the wrong way..."
            ryan.say "[hero.name]...is that you?"
            mike.say "Ah...hey, Ryan!"
            mike.say "Would you believe it, Ryan - Sam really does have a mouthful right now?"
            ryan.say "Oh, right."
            ryan.say "You guys eating a snack or something?"
            mike.say "Erm...yeah, you could say that."
            ryan.say "Wow, she must really like eating what you've got to offer!"
            ryan.say "Geez, she always was a messy eater!"
            ryan.say "If you want to give her the Heimlich, you've got my permission, buddy."
            mike.say "Sure thing...buddy!"
            show samantha bj4 deep deepthroat with vpunch
            "Even as I'm saying this, I can feel myself cumming in Sam's mouth."
            with vpunch
            "By now she's realised what's happening, and the gagging has lessened."
            show samantha bj4 lick openmouth mouth with vpunch
            "But all the same she can't keep from coughing as I pull my cock out of her mouth."
            "Sam's breath comes in ragged gasps the whole time."
            "And I can see trails of saliva and cum between her lips and the head of my cock."
            show samantha bj4 lick shut -mouth closed
            ryan.say "Is she okay?"
            mike.say "Yeah, I think so."
            show samantha bj4 lick openmouth up
            mike.say "Looks like she swallowed most of it!"
            ryan.say "Urgh..."
            ryan.say "I don't want to speak to her in that state!"
            ryan.say "Just tell her not to be such a greedy cow in the future."
            "And with that, he ends the call."
        "Cum on her face":
            "Sam opens her mouth to answer Ryan's question, and that's the exact moment my orgasm chooses to hit."
            $ samantha.love += 5
            show samantha bj4 lick face closed with vpunch
            "Cum shoots straight into Sam's surprised face and between her open lips."
            with vpunch
            "She makes a choking, almost desperate sound of surprise."
            ryan.say "What in the hell was that?!?"
            show samantha bj4 lick face down
            samantha.say "It was me..."
            samantha.say "I think something went down the wrong way..."
            ryan.say "Geez, you need to stop stuffing your face!"
            "Wiping the glistening cum off of her face, Sam rolls her eyes at her husband's less than kind comment."
            show samantha bj4 lick face up
            samantha.say "Look, I've got to go clean up a bit."
            samantha.say "So I'm gonna give the phone to [hero.name], okay?"
            "The whole of this conversation takes place as I'm staring at Sam's face."
            "Almost every inch of it is covered in a glistening mask of semen."
            "I watch as it begins to run down her cheeks, drip from her nose and chin."
            "A couple of strands even stretch from her lips to the head of my cock."
            "I'm only shaken out of my momentary fixation on Sam's semen face-mask when she hands me the phone."
            mike.say "Erm...hey, Ryan!"
            ryan.say "Jesus, [hero.name], is Sam really okay?"
            mike.say "Ah, yeah...I guess."
            mike.say "I...I think she's finished coughing it all up."
            ryan.say "Urgh...charming!"
            ryan.say "I don't think I need to speak to her in a state like that."
            ryan.say "And I know I can trust you to look after her for me - right?"
            mike.say "Sure...sure thing."
            "And with that, he hangs up on me."
    hide samantha
    show samantha casual blush flirt
    with fade
    "I watch as Sam wipes her mouth clean on the back of her hand and then almost sneers at the phone in my hand."
    "Part of me wants to be mad at her for paying Ryan back in the same way he betrayed her."
    "That part of me would probably lecture her about becoming just as bad as him."
    "But I know that I'm not going to do anything of the kind."
    "I guess that my desire for Sam is just that much greater than my loyalty to Ryan."
    "Sure, I might be lowering myself to the same level as the guy by going along with all of this."
    "But I think, given the choice, I'd rather be guilty and have Sam doing things like this to me."
    "Than be alone and secure in the knowledge that I did the right thing."
    scene bg black with dissolve
    $ samantha.flags.cuck_ryan = True
    return


label samantha_event_D03:
    if samantha.love.max < 140:
        $ samantha.love.max = 140
    if samantha.sub.max < 80:
        $ samantha.sub.max = 80
    $ samantha.flags.cheatDelay = TemporaryFlag(True, 3)
    show bg livingroom
    "What with her repeating the weekend visit to my house for a second time, things seem to be getting serious between Sam and me."
    "I don't recall exactly what I hoped would happen back when I first told her about Ryan's philandering on her wedding day."
    "And maybe one of the reasons I did choose to tell her all about it because I'd always regretted there not being more than friendship between us."
    "But I don't think I could ever have imagined that I'd end up getting dragged into Sam's plans to pay Ryan back for his cheating on her."
    "At least not like this!"
    "I guess whatever I might have hoped is academic now, as Sam and I are pretty much having an affair."
    "At least that's what I hope is going on between us."
    "I don't know if I could handle just being used to get back at a guy like Ryan."
    "Especially by a girl that I have such strong feelings for as well!"
    play sound cell_vibrate loop
    "Maybe that's why I sound so eager to please when Sam calls me up out of the blue?"
    stop sound
    samantha.say "Hey, [hero.name] - what are you doing right now?"
    if samantha.flags.nickname == "cupcake":
        mike.say "Ah...Hi Cupcake."
    else:
        mike.say "Ah...Hi Sam."
    mike.say "I guess I'm not really doing much of anything."
    "Sam makes a sound like someone answered a question incorrectly on a gameshow."
    samantha.say "Wrong!"
    samantha.say "The correct answer was that you're getting up off of your ass."
    mike.say "What..."
    samantha.say "And then you're going to the front door to let me in!"
    mike.say "What...you're outside?"
    mike.say "Like, right now?"
    "Even though I've asked the question, I'm already standing up and walking into the hallway."
    scene bg black with dissolve
    show bg house
    show samantha flirt casual
    with wiperight
    "I make it to the door and open it before Sam can reply."
    samantha.say "Well, aren't you going to invite me in?"
    mike.say "Uh, yeah...of course."
    show bg livingroom with fade
    "Although I must seem more than a little confused, Sam either ignores it or else totally fails to notice as much."
    show bg bedroom1 with fade
    "Instead she breezes happily into the house, making straight for my bedroom this time."
    "Under any other circumstances, I'd just chalk this up to the fact she lived here and so knows her way around."
    "But after what we got up to on her previous couple of visits, it takes on another meaning entirely."
    "I follow Sam into my room, trying not to look either suspicious or sheepish as I do so."
    "But she notices my hesitance almost as soon as she sits down on the bed and looks up at me."
    show samantha close normal casual with dissolve
    samantha.say "What's the matter, [hero.name]?"
    samantha.say "I thought you'd be glad to see me."
    samantha.say "You know, you've been on my mind all week long!"
    "Sam pats the spot on the bed next to her, and I oblige her by sitting down."
    if samantha.flags.nickname == "cupcake":
        mike.say "I...I am glad to see you, Cupcake."
    else:
        mike.say "I...I am glad to see you, Sam."
    mike.say "I haven't been able to think about anything else..."
    samantha.say "But..."
    mike.say "But I don't want to think that you're just..."
    mike.say "Well...using me to get back at Ryan!"
    show samantha surprised
    "I see Sam's eyes go wide at this, as though she's genuinely surprised."
    samantha.say "No...of course not, [hero.name]!"
    show samantha normal
    samantha.say "I could have gone out and fucked any random guy I met to do that."
    samantha.say "I want to get back at him with you so we can both rub his smug face in it."
    "Sam reaches out and takes hold of my hands as she says this."
    show samantha flirt
    samantha.say "But I hope there's going to be a lot more to it when he's out of the picture."
    samantha.say "If that's what you want too?"
    "I nod at this, feeling relieved."
    show samantha blush
    samantha.say "Okay, so now that's all cleared up - how about we do something fun?"
    "I nod again, unable to keep from swallowing in anticipation."
    samantha.say "That's great, [hero.name]."
    samantha.say "Because I want to climb on top and have you fuck me!"
    "It takes a moment for what Sam just said to fully sink in."
    "Did the one that almost got away just ask me to fuck her?"
    mike.say "You want me to what?"
    samantha.say "Fuck me, [hero.name] - right here and right now."
    "As if the matter-of-fact way in which she says it isn't enough, Sam takes physical action to make her intentions clear."
    "She pushes me onto my back leaving me laid flat on the bed."
    show samantha naked
    "Then she pulls up her dress and yanks down her panties."
    show samantha close naked
    samantha.say "Come on, [hero.name], what are you waiting for?"
    samantha.say "I know just how much you've always wanted me!"
    "I don't know if it's more the sight of her offering herself to me like that."
    "Or else it's the knowing look on her face as she tempts me with herself."
    "But either way, I do know that there's absolutely no way I can resist such an offer."
    mike.say "Ah, what the hell."
    mike.say "Fuck Ryan!"
    "Sam smiles over her shoulder and shakes her head."
    samantha.say "No, fuck me!"
    hide samantha
    show samantha reverse
    with fade
    "It takes no more than a couple of seconds for her to tear off my clothes and toss them aside."
    "Somehow I just know that this isn't going to be the slowest or most romantic fuck of all time."
    "My desire for her seems to take over completely, and all I want is to get my hands on her."
    "With her back still turned to me, Sam straddles my thighs and takes hold of my cock."
    show samantha reverse vaginal up
    "She guides it to just the right point, sliding the head along her already moist lips."
    "And as she begins to lower herself onto it, she looks back over her shoulder at me."
    "This means that I see the sensations she's feeling reflected in her face."
    show samantha reverse orgasm down
    "Sam closes her eyes and opens her mouth ever wider as the head inches inside of her."
    "I can hear her breathing become more like a series of gasps and sighs at the same time."
    "Pushing herself down and onto my cock, the pleasure on her face becomes ever more intense."
    "As if each new inch that enters her body steps up the intensity by a considerable degree."
    "And then I finally feel the weight of her press down upon me."
    "So I know I can't get any deeper inside of her."
    "Sam sits atop me for a while, seemingly happy to savour the moment."
    show samantha reverse calling pleasure
    "But then I see that she has something in her hand."
    "And I guess I should have known just what it would be!"
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake - what are you..."
    else:
        mike.say "Sam - what are you..."
    "Just as I begin to speak up, Sam starts to ride me."
    "Somehow she manages to use her weight and the sensation it gives me just so."
    "The combination of the two things means that all I can do is struggle helplessly beneath her."
    if samantha.flags.nickname == "cupcake":
        mike.say "No, Cupcake!"
    else:
        mike.say "No, Sam!"
    "But it's already too late, as I can read the name above the number she's calling."
    "As it begins to ring, Sam waves the phone over her shoulder at me and shakes her head."
    "The implication is pretty obvious."
    "And so I stare at her in tense silence for a couple of seconds, before nodding hastily."
    "Sam smiles at me sweetly, secure in the knowledge that she's the one in complete control."
    ryan.say "Hey, babe - what's up?"
    ryan.say "I thought you said you'd be at the gym the rest of the afternoon?"
    "By the time she replies, Sam's pace has increased a great deal."
    "So when she speaks, it's with the gasps and heavy breathing of someone pushing themselves to the physical limit."
    show samantha reverse up smile
    samantha.say "I am...still at the...gym."
    samantha.say "Just...checking in!"
    show samantha reverse down pleasure
    ryan.say "So, you just wanted to hear the sweet, sweet sound of my voice, huh?"
    "At this, Sam's face wrinkles with disgust, and she mimes poking her fingers down her throat."
    "But her answer betrays none of the same sentiment."
    show samantha reverse up smile
    samantha.say "Ah...you got me."
    samantha.say "You always...know what I feel like...on the inside!"
    show samantha reverse down pleasure
    "The hidden meaning of this statement isn't lost on me for a second."
    "And I have to say that I know better than Ryan on that score right now!"
    ryan.say "Say...you're really sounding like they're pounding you over there!"
    ryan.say "Are you sure you can take what they have to give?"
    "Sam laughs off the concern in Ryan's tone, clearly amused at manipulating him so."
    show samantha reverse up
    samantha.say "It's this...new coach they just...hired."
    show samantha reverse down
    samantha.say "He's really...riding me today!"
    ryan.say "Shit, it sure sounds like it too!"
    show samantha reverse vaginal up
    pause 0.4
    show samantha reverse vaginal down at startle(0.05,-10)
    pause 0.4
    show samantha reverse vaginal up
    pause 0.4
    show samantha reverse vaginal down at startle(0.05,-10)
    pause 0.4
    show samantha reverse vaginal up
    pause 0.4
    show samantha reverse vaginal down at startle(0.05,-10)
    samantha.say "Yeah...he's...some kind of...prick."
    show samantha reverse vaginal up
    pause 0.4
    show samantha reverse vaginal down at startle(0.05,-10)
    pause 0.4
    show samantha reverse vaginal up
    pause 0.4
    show samantha reverse vaginal down at startle(0.05,-10)
    pause 0.4
    show samantha reverse vaginal up
    pause 0.4
    show samantha reverse vaginal down at startle(0.05,-10)
    samantha.say "But...don't worry...I'll get...my money's worth!"
    ryan.say "Yeah, you see that you do, baby."
    "Suddenly I feel the inevitable begin to happen, and I grab hold of Sam by the haunches."
    show samantha reverse vaginal up orgasm
    pause 0.2
    show samantha reverse vaginal down at startle(0.05,-10)
    pause 0.3
    show samantha reverse vaginal up
    pause 0.2
    show samantha reverse vaginal down at startle(0.05,-10)
    pause 0.3
    show samantha reverse vaginal up
    pause 0.3
    show samantha reverse vaginal down at startle(0.05,-10)
    samantha.say "Whoa!"
    samantha.say "Looks like he's going for a big finish!"
    samantha.say "I have to go - love you."
    ryan.say "Okay - love you more!"
    if renpy.has_label("samantha_achievement_5") and not game.flags.cheat:
        call samantha_achievement_5 from _call_samantha_achievement_5
    show samantha reverse vaginal up orgasm fuck phone
    pause 0.2
    show samantha reverse vaginal down at startle(0.05,-10)
    pause 0.3
    show samantha reverse vaginal up
    pause 0.2
    show samantha reverse vaginal down at startle(0.05,-10)
    pause 0.3
    show samantha reverse vaginal up
    pause 0.3
    show samantha reverse vaginal down creampie with vpunch
    "Almost the same moment that Sam wraps up the call, I cum as deep inside of her as I can."
    show samantha reverse ahegao with vpunch
    "She instantly drops the phone and starts to massage her breasts almost in desperation."
    with vpunch
    "I can feel her grinding herself on my cock."
    "Like she wants to wring pleasure out every moment it's still inside of her."
    "And it's not like she's having to make do with a few short seconds either."
    with vpunch
    "I don't know if it's just been a while since I shot my load."
    "Or else I've always had this in me, just storing it up for Sam alone."
    with vpunch
    "Either way, I keep on cumming until she's as full as can be."
    show sexinserts samantha bottom cum zorder 1 at center, zoomAt(0.75, (770, 870))
    show samantha reverse -vaginal dickcum orgasm
    with vpunch
    "And when I finally manage to drag my cock out of her pussy, Sam instantly starts to leak."
    "All I can hear is the sound of her panting from sheer exhaustion."
    "And all I can see is the cum, dripping steadily out from between her swollen lips."
    if not samantha.flags.pill and not samantha.is_visibly_pregnant:
        "It's then that a random thought strikes me."
        if samantha.flags.nickname == "cupcake":
            mike.say "Cupcake..."
        else:
            mike.say "Sam..."
        samantha.say "Hmm?"
        mike.say "You are on the pill - right?"
        show samantha reverse smile
        samantha.say "Mmm...nope."
        show samantha reverse orgasm
        samantha.say "There's no point - Ryan always uses a rubber anyway!"
        "All of a sudden, the steady stream of semen still running out of Sam's pussy takes on far greater significance."
        "I look at her in honest surprise, but all she does is smile right back at me."
        "From her expression, you'd think there was nothing more innocent in the entire world."
    hide sexinserts
    $ samantha.sexperience += 1
    return

label samantha_event_D04:
    $ DONE["samantha_event_D04"] = game.days_played
    $ samantha.flags.cheatDelay = TemporaryFlag(True, 3)
    if samantha.sub.max < 90:
        $ samantha.sub.max = 90
    show samantha
    "There's nothing more terrifying as a guy than hearing the words 'we need to talk' coming from your significant other."
    "So that's why I'm super wary when using them myself, assuming that they're as scary for a girl to hear too."
    "But the moment that I turn to Sam and utter those four dreaded words, I begin to wonder if I was wrong on that score."
    if samantha.flags.nickname == "cupcake":
        mike.say "Ah, Cupcake?"
    else:
        mike.say "Ah, Sam?"
    samantha.say "Hmm...yeah, [hero.name]?"
    mike.say "I...I think we need to talk..."
    "The hunted look that I had been expecting to see suddenly appear in Sam's eyes fails to materialise."
    "Instead she leans in closer, smiling the whole time and nodding her head in agreement."
    samantha.say "Of course we can talk, [hero.name]!"
    samantha.say "We have so much to catch up on since I moved out."
    samantha.say "And there are so many things we can say to each other now that we never could before."
    "As she reels all of this off, it begins to occur to me that there may have been a slight misunderstanding here."
    samantha.say "And can I just say how refreshing it is to hear you asking me that?"
    samantha.say "So many guys are terrible about really talking to a girl."
    samantha.say "It's really great that you actually want to do it, [hero.name]!"
    "Ah, I think I see the source of the problem."
    "I wanted to talk about something specific, like a guy would."
    "And Sam thinks I want to talk in general, and at length, about our relationship in general."
    show samantha annoyed
    samantha.say "Now Ryan - there's a guy that'd never ask to do that!"
    "At the mention of Ryan's name, I see an opening and jump on it."
    mike.say "Actually, he was one of the things that I wanted to talk about."
    show samantha surprised
    samantha.say "Yeah?"
    samantha.say "How so?"
    "I pause before going on, trying to take a deep breath without looking like I'm taking one at all."
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake, we've been seeing each other for a while now, right?"
    else:
        mike.say "Sam, we've been seeing each other for a while now, right?"
    show samantha normal
    "Sam nods, unable to find fault with this statement."
    mike.say "Long enough for us both to know it's not just some crazy fling, you know?"
    mike.say "Long enough for it to be more than us both wanting to stick it to Ryan?"
    "Sam nods again, but noticeably more slowly this time."
    "And I can see that the direction I'm headed in is finally becoming clear to her."
    "She doesn't answer as quickly in the positive as I might have liked."
    "But I choose to take the fact that she keeps on nodding as a positive sign."
    samantha.say "I guess you're right, [hero.name]."
    samantha.say "After you told me what he did behind my back..."
    samantha.say "Well, I could have just gone out and fucked anyone for revenge."
    "I feel a twinge in my chest as she admits this, hoping that it means what I think it means."
    samantha.say "What we ended up doing together wasn't just out of hating Ryan."
    samantha.say "It was out of realising we were supposed to be the ones together as well."
    "Now it's my turn to nod, trying to show Sam that I agree and think she's one hundred percent correct."
    mike.say "That's why I want to talk about him."
    mike.say "About the fact that you're still wearing his ring."
    "Sam can't help glancing down at the wedding ring on her finger, the symbol of their marriage."
    "I feel like a dick to even be bringing it up like this, but what choice do I have?"
    "Right now Sam's keeping Ryan in the dark about her true feelings for him."
    "And at the same time, she's keeping her relationship with me under wraps."
    if samantha.flags.nickname == "cupcake":
        mike.say "I know it's hard, Cupcake."
    else:
        mike.say "I know it's hard, Sam."
    mike.say "But as long as we keep this thing hidden, we're just having an affair."
    mike.say "And I...well, I want us to be more than that."
    if samantha.flags.nickname == "cupcake":
        mike.say "I want you to leave him, Cupcake."
    else:
        mike.say "I want you to leave him, Sam."
    "Sam looks at me for a moment, and then turns her gaze away, refusing to meet my eye."
    show samantha sad
    samantha.say "I know all that."
    samantha.say "Of course I do!"
    "She sighs heavily before going on."
    samantha.say "I guess it's just been so much fun to be the one breaking the rules for a change."
    samantha.say "Maybe I got a little too carried away, a little too comfortable playing a bad girl?"
    samantha.say "And I know that I shouldn't be able to keep on lying to Ryan either."
    samantha.say "Maybe I'm just not at that stage because we've been having so much fun behind his back."
    samantha.say "Maybe once it's officially over, I won't be able to stand the sight of him..."
    mike.say "So you'll do it?"
    mike.say "You're saying you'll break it off with him?"
    show samantha normal
    "Sam turns her head to look me in the eye once again, her expression calm and controlled."
    show samantha close
    samantha.say "I'm saying that I'll think about it."
    samantha.say "And I really mean that, [hero.name]."
    samantha.say "I just need a little time, that's all."
    "And with that she effectively lets me know that the subject's closed and the discussion is over."
    "As we turn to less intense and awkward matters, I still can't help wondering what she'll end up doing."
    "And I hope that the right thing in her mind is the same as the one in mine."
    return

label samantha_event_D05:
    if samantha.love.max < 160:
        $ samantha.love.max = 160
    if samantha.sub.max < 100:
        $ samantha.sub.max = 100
    $ samantha.flags.cheatDelay = TemporaryFlag(True, 3)
    play sound cell_vibrate
    samantha.say "Hey, [hero.name] - what are you doing right now?"
    samantha.say "Come on!!! Open the front door and let me in!"
    scene bg black with dissolve
    show bg house
    show samantha flirt casual
    with wiperight
    "I make it to the door and open it before Sam can reply."
    samantha.say "Well, aren't you going to invite me in?"
    mike.say "Uh, yeah...of course."
    scene bg livingroom
    show samantha flirt casual at right
    with fade

    "Sam hurries me into the bedroom, as if she's as eager as can be to get down to it."
    hide samantha with easeoutleft
    "And I begin to hurry after her, the exact same thing occupying my mind."
    "But then I hesitate for a moment, stopping in my tracks as a thought occurs to me."
    "Where is this thing actually going right now?"
    "Are we about to screw because we're crazy about each other?"
    "Or is this another case of Sam using me in her efforts to get back at Ryan?"
    scene bg bedroom1 with fade
    "Perhaps sensing my concern, she stops herself and glances back over her shoulder at me."
    show samantha close casual surprised with dissolve
    samantha.say "Hey, [hero.name]...what's up?"
    mike.say "Ah...it's nothing."
    show samantha normal
    samantha.say "If it was nothing, it wouldn't be bugging you!"
    mike.say "Well...it's the whole situation with Ryan, you know?"
    "Sam smiles at this and shakes her head."
    samantha.say "Don't even think about him until afterwards, okay?"
    samantha.say "At least not for the next couple of minutes!"
    "There's just something about the way she says 'minutes' that shakes me out of my funk."
    mike.say "Wait...what...what do you mean by minutes?!?"
    mike.say "Was that some kind of comment on my stamina?"
    show samantha flirt
    "Sam chuckles and looks away, refusing to answer my question."
    samantha.say "Maybe...maybe not."
    samantha.say "Maybe you need to show me I'm wrong..."
    "Look, I know exactly what she's doing here, okay?"
    "As sweet and unassuming as she can be, Sam's no true innocent."
    "I can tell when she's trying to manipulate me into giving her just what she wants."
    "The only problem is that she also has a way of making me want what she wants too!"
    hide samantha
    show samantha casual flirt blush
    with dissolve
    "I stand there for a moment as Sam turns her back on me and starts to walk towards the bed."
    show samantha underwear with dissolve
    "She begins to strip off her clothes at the same time, tossing them aside as she goes."
    show samantha close naked with dissolve
    "By the time she reaches the bed, she's completely naked and, save for that same smile."
    "There's no way that I can shake off what I've just seen."
    "After all, I'm only human."
    "And so I find myself hurrying after Sam once again, desperately yanking off my own clothes."
    "So sees the effect that she's had on me, and begins to giggle in amusement."
    hide samantha
    show samantha kiss naked
    with fade
    $ samantha.flags.kiss += 1
    "But as soon as I make it to her, I press my lips against her own."
    "This silences her giggles instantly, and she responds to the kiss a mere second later."
    "Sam leans into me then, pulling me into a close embrace."
    "The warmth of her skin feels incredibly good against mine."
    "And the softness of her body is like nothing else I can imagine."
    "But it's a softness that makes me hard, and with some speed too."
    "I feel Sam reach down and begin to stroke my stiffening cock, which breaks the kiss as I gasp."
    hide samantha
    show samantha close naked flirt blush
    with fade
    samantha.say "Mmm..."
    samantha.say "What have we here?"
    mike.say "Ah..."
    mike.say "You...you like what you feel?"
    samantha.say "Hmm...yeah, I sure do!"
    samantha.say "I just wonder how good it'd feel inside of me..."
    "There are times when you just can't keep up the manly stud act, no matter how hard you try!"
    "I can feel myself swallowing nervously and beginning to pant, my cheeks going red."
    "The knowledge that Sam wants my cock inside of her still does that to me, and without fail."
    "All I can do is follow, as she keeps hold of my manhood with one hand and takes me by the wrist with the other."
    "Sam pulls me in her wake, all the way to the bed and then onto it."
    "Still holding onto my cock, she makes to lay down on her side."
    "But it's in that very same moment that I can feel myself regaining some control of myself."
    "And almost instantly, I can see what I want and how to get it."
    hide samantha
    show samantha doggy out
    with fade
    "The sound of my hands clapping hold of Sam's ass is louder than I expected."
    "But not as loud as the yelp of shock that she lets out as she feels it."
    "The fact that she also lets go of my cock in her surprise helps me out too."
    "It means that I can pull her backwards, pushing it between her buttocks."
    "Sam yelps again, probably unsure of just where I'm going to stick it."
    "And that uncertainty she's feeling makes the whole thing just that much more fun for me."
    "This means that when I finally give in and let her in on the secret, she's more than ready for it."
    "I take a couple of seconds to just rub the head of my cock against Sam's pussy."
    "She moans a little as it slides up and down the slick lips, glancing back over her shoulder."
    "I can already see the desire building in her eyes, the need for me to go further still."
    show samantha doggy vaginal
    "And as I begin to push into her, I see Sam's mouth open in sympathy with her pussy."
    "No matter how many times we do this, I still can't believe just how good she feels."
    if samantha.is_visibly_pregnant:
        show samantha doggy milk
        "I can feel the added weight to Sam's body from her heavy, swollen belly."
        "And her breasts hang down, already growing in anticipation of what's to come, already leaking."
    else:
        "I never imagined that Sam's body could look any more amazing than when I stole glances at her clothed."
        "But once naked, she's something else altogether."
    show samantha doggy scream
    samantha.say "Oh...[hero.name]..."
    samantha.say "It feels so, SO good inside of me!"
    samantha.say "You...you really...showed me...how good it feels!"
    samantha.say "I never want you to stop...do this to me forever!"
    "Jesus, that's another thing I had no idea she'd be so good at!"
    "Dirty talk coming out of those perfect lips - it just sounds so...so right..."
    "By now, Sam's talked me into such a state that there's no chance of taking it slow."
    "And so before too long, I'm banging her as hard as I possibly can."
    "But it's not like she shows even a single sign of it being too much for her."
    "Instead she takes everything that I have to give her, never uttering a single sound of complaint."
    "Sam's body is becoming slick with sweat, making it hard for me to keep a hold of her."
    "Which means that my efforts become all the more intense and desperate as I keep on pounding her."
    "Every other second I seem to be struggling to stop her from slipping out of my hands."
    "Either that, or I'm struggling to keep her from slipping off of my cock."
    "All of the dirty talk has stopped now too, replaced by a serious amount of moaning from Sam."
    "At the same time, she looks back at me over her shoulder."
    "Every thrust into her seems to make the sounds coming out that much more intense."
    "Before too long, I know that it just can't go on like this for much longer."
    "I bite my lip as I can sense that I'm not far from cumming."
    "The strange thing is that it seems to have more of an effect on Sam than me."
    "Before she's been happy to stay on her hands and knees and take a pounding."
    "But now she begins to twist and turn in front of me, sliding here and there."
    "Unlike before, I can do nothing to keep her slick body from slipping out of my clutches."
    hide samantha
    show samantha close naked
    with fade
    "I make a disappointed sound as I feel Sam slip off of my cock."
    "But she either doesn't notice or else chooses to ignore my dismay at what she's doing."
    "Instead she pushes me backwards without asking permission or telling me what's going on."
    "And it's then I see her cleavage being pushed forwards, and feel it wrap around my cock."
    hide samantha
    show samantha bj
    with fade
    "In a mere matter of seconds, Sam has it just where she wants it."
    "And then she begins to press her breasts together, massaging my member as she does so."
    "Even after I've just been inside of her, the feeling is still pretty intense."
    "My already sensitive cock is now sandwiched between the soft pillows of Sam's chest."
    "All I can do is stare down at them, eyes wide and mouth half open."
    "I may be biased, but I think Sam's breasts are probably the most incredible I've ever seen."
    "Not too small and not too large, but just right, and the perfect shape as well."
    "And now they're pressing down on my cock!"
    "It's already as sensitive as it can be from being inside of Sam."
    "So it's not long before I can feel the sensation of my climax returning with a vengeance."
    show samantha bj cumshot with vpunch
    if samantha.flags.nickname == "cupcake":
        mike.say "Oh...Cupcake..."
    else:
        mike.say "Oh...Sam..."
    mike.say "Oh...fuck...fuck!"
    "And with that, I see the head of my cock emerge from between her breasts."
    with vpunch
    "The cum hits Sam square in the face, and she makes no effort to stop it."
    show samantha bj -cumshot cumface with vpunch
    "I find that I'm holding my breath as it paints her features with glistening white lines."
    "To me it all happens in extreme slow motion and to one of those stirring classical tunes."
    "With Sam taking everything I have to give her, and never as much as flinching once."
    hide samantha
    show samantha naked cum
    with fade
    "Afterwards I collapse onto the bed, exhausted and utterly spent."
    "My breathing is heavy and my heart is pounding as I watch Sam reach for something on the floor by the side of the bed."
    "Then my heart sinks for a moment as I realise that it's her mobile."
    show samantha close naked cum
    "What in the hell is she going to do this time?"
    "Call Ryan up and have yet another conversation about where he thinks she is?"
    "Chat to him happily as my cum runs down her face?"
    show samantha selfie with fade
    "I daren't move a muscle as she holds up the phone and snaps a picture of us both."
    "My own smile looks a little forced, and hers is dripping with semen."
    "And then I see that she's typing something into the phone, and so I drag myself closer to see what it is."
    "I see instantly that it's a text, and that she's sending it to Ryan."
    "But then the words become clear, and I can feel a massive weight lifting off of my shoulders."
    "In fact, what Sam's writing makes me feel as if I could walk on air!"
    show samantha selfie
    "'Honey,' it reads, 'I want a divorce!'"
    "As she hits send, Sam turns to me and smiles."
    samantha.say "See - I told you not to think about him until afterwards."
    show samantha selfie
    samantha.say "And pretty soon, neither of us will ever have to think of him again!"
    $ samantha.sexperience += 1
    scene bg black with dissolve
    return

label samantha_event_D05B:
    if samantha.love.max < 160:
        $ samantha.love.max = 160
    if samantha.sub.max < 100:
        $ samantha.sub.max = 100
    $ samantha.flags.cheatDelay = TemporaryFlag(True, 3)
    play sound door_bell
    "I wasn't expecting any visitors this afternoon, but I'm still not surprised when the doorbell rings."
    show bg house
    show samantha casual zorder 2 at center
    with wiperight
    "Sam's been stopping by pretty regularly over the past couple of weekends for a little fun."
    "And so when I get to my feet and hurry to open the door, I'm not surprised to see her standing there."
    if samantha.flags.nickname == "cupcake":
        mike.say "Hey, Cupcake!"
    else:
        mike.say "Hey, Sam!"
    samantha.say "[hero.name], hi!"
    show natalie zorder 1 at center with dissolve
    natalie.say "Hello there!"
    "I wasn't expecting to hear another voice."
    "And I guess the surprise must show on my face."
    samantha.say "Ah, [hero.name], you remember Natalie - right?"
    show samantha casual at left4
    show natalie casual at right5
    with move
    "At this I see someone lean around from behind Sam."
    "I instantly recognise the brunette giving me a friendly smile and a wave."
    "She was one of the bridesmaids at Sam and Ryan's wedding."
    "I remember dancing with her at the reception."
    "But I also recall what I saw her doing with Ryan behind Sam's back too."
    if samantha.flags.nickname == "cupcake":
        mike.say "Yeah, I remember her, Cupcake."
    else:
        mike.say "Yeah, I remember her, Sam."
    samantha.say "That's great, [hero.name]."
    samantha.say "Well...are you going to invite us in or not?"
    mike.say "Sure, sure..."
    mike.say "Where the hell are my manners!"
    "I step aside to let Sam and Natalie enter, closing the door behind them."
    show natalie at right with move
    hide natalie with dissolve
    show samantha at left5 with move
    show samantha at left4, hshake
    "But when Natalie walks into the sitting room, I catch Sam by the arm."
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake..."
    else:
        mike.say "Sam..."
    mike.say "What's going on here?"
    mike.say "That's the girl Ryan cheated on you with!"
    show samantha angry
    samantha.say "You think I don't know that, [hero.name]?"
    samantha.say "She pretended to be my BFF."
    samantha.say "She used me."
    samantha.say "Then she stabbed me in the back!"
    mike.say "So why is she here now?!?"
    show samantha annoyed
    samantha.say "Natalie wants whatever I have, [hero.name]."
    samantha.say "So I told her about what I have going on with you."
    samantha.say "She jumped at the chance to get involved."
    show samantha normal
    samantha.say "Now we get to use her."
    if samantha.flags.nickname == "cupcake":
        mike.say "How does that work, Cupcake?"
    else:
        mike.say "How does that work, Sam?"
    samantha.say "We double-team her, then send Ryan some candid shots."
    samantha.say "And then I drop her like a bad habit!"
    menu:
        "Refuse":
            "I can hardly believe those words are coming out of Sam's mouth."
            "Sure, I've been screwing her behind Ryan's back."
            "But I loved her way before they tied the knot."
            "This is just revenge for the sake of it, for the sake of hurting someone."
            if samantha.flags.nickname == "cupcake":
                mike.say "Listen to yourself, Cupcake."
            else:
                mike.say "Listen to yourself, Sam."
            mike.say "This isn't like you."
            show samantha surprised
            samantha.say "Huh..."
            samantha.say "What do you mean?"
            mike.say "I thought it was enough to find out that Ryan was cheating."
            mike.say "I never thought you'd want to beat him at his own game."
            samantha.say "What does that mean, [hero.name]?"
            samantha.say "Are you saying you won't do it?"
            $ samantha.love -= 20
            if samantha.flags.nickname == "cupcake":
                mike.say "Yeah, Cupcake."
            else:
                mike.say "Yeah, Sam."
            mike.say "I think it's a step too far."
            show samantha casual annoyed
            natalie.say "Sam..."
            natalie.say "Is something up?"
            "I don't know if she overheard the conversation or just got tired of waiting."
            "But we both look round to see Natalie standing in the sitting room doorway."
            samantha.say "Ah...yeah."
            samantha.say "[hero.name] just told me he's got something on."
            natalie.say "Oh...right."
            show samantha sad
            samantha.say "It's my fault, Nat."
            samantha.say "I should have called ahead."
            samantha.say "But I guess that's what you get for being spontaneous!"
            show natalie at right5 with dissolve
            show samantha angry
            "As they leave, Sam fixes me with a look that speaks volumes."
            "And amongst other things, it says that we'll be talking about this soon enough."
        "Accept":
            "I can already feel my cock hardening at the idea Sam's putting into my head."
            "It sounds like a pretty sweet deal from where I'm standing."
            "The chance to have some fun with a couple of hot girls."
            "And stick it to Ryan at the same time."
            "What's not to like?"
            if samantha.flags.nickname == "cupcake":
                mike.say "Sounds good to me, Cupcake."
            else:
                mike.say "Sounds good to me, Sam."
            show samantha happy
            samantha.say "Great, [hero.name]."
            samantha.say "I knew I could count on you to help me."
            scene bg livingroom
            show samantha casual at right5
            show natalie casual at left4
            with fade
            "We walk into the sitting room, where Natalie has been waiting."
            natalie.say "Are we..."
            natalie.say "Did he say..."
            samantha.say "Don't worry, Nat."
            samantha.say "It's on, it's on."
            show natalie happy
            natalie.say "Oh...yay!"
            natalie.say "This is going to be SO much fun!"
            show samantha flirt
            samantha.say "Sure thing, Nat."
            samantha.say "I'll make sure everyone gets what they deserve!"
            show samantha casual at center
            show natalie casual at left5
            with ease
            "I cast Sam a questioning glance as we walk up the stairs to my room."
            "That was such a loaded line that I can't believe Natalie won't get suspicious."
            show samantha casual at left4
            show natalie casual at left
            with ease
            "But Sam just shakes her head, dismissing my fears."
            samantha.say "You just HAVE to suck [hero.name]'s dick, Nat."
            samantha.say "Trust me - it's so much better than Ryan's!"
            show bg bedroom1
            show samantha casual at right5
            show natalie casual at left5
            with fade
            "Sam says this as soon as the door is closed behind us."
            "She doesn't need any more encouragement than that."
            show natalie naked with dissolve
            "A moment later, Natalie is down on her knees and stripping off."
            show samantha naked with dissolve
            "Sam and I follow her example as quickly as we can."
            "And it's not like I need to make an effort to rise to the occasion either."
            "Natalie's cute enough to begin with."
            "But under those clothes, she's got a tight, petite little body too."
            "Maybe I can sympathise with Ryan just a tiny bit..."
            samantha.say "Get on the bed, Nat."
            samantha.say "On all fours, yeah?"
            "We both glance around at Sam, but then do a double-take."
            "She's just finished securing a large strap-on around her waist."
            show natalie normal at left5, hshake
            natalie.say "S...Sam..."
            natalie.say "Wha...what's that?"
            show samantha happy
            "Sam just smiles, slapping the head of the dildo so it wobbles from side to side."
            samantha.say "Oh, this little thing?"
            show samantha flirt
            samantha.say "[hero.name] and I do this kind of thing all the time."
            samantha.say "But if you're too scared..."
            natalie.say "No...no, Sam."
            show natalie happy
            natalie.say "It's okay...really!"
            hide samantha
            hide natalie
            show samantha threesome2 with fade
            if renpy.has_label("natalie_achievement_1") and not game.flags.cheat:
                call natalie_achievement_1 from _call_natalie_achievement_1
            "I take hold of Natalie's head, guiding my cock into her mouth."
            "At the same time, I watch Sam lubing up the dildo."
            "I shake my head at her, trying to keep from laughing at Natalie's plight."
            "She gives me a wink in return, and then grabs hold of Natalie's buttocks."
            "Well, it looks like we're going through with this thing!"
            "So here goes..."
            "I have my cock about halfway into Natalie's mouth."
            "And that's when Sam makes her move at the other end."
            "I feel the sensation of her pushing the dildo into Natalie's ass."
            "And the result is her trying to cry out in sudden alarm."
            "Of course, all this means in reality is that I can shove my cock in further still."
            "Which is exactly what I do a moment later."
            "There's nothing that Natalie can do but surrender to the treatment."
            "That or choke on the large mouthful of cock she has right now."
            "I grab hold of her braid to make sure the message is received."
            "And Sam keeps right on pushing into her ass from the other end."
            "Soon enough we've settled into a rhythm, and Natalie's forced to accept it."
            "I'll give praise where it's due."
            "The petite brunette doesn't gag or flinch once."
            "She takes everything that Sam and I have to give her."
            "And I can see that Sam has a lot more of that in her than me!"
            "I'm just enjoying having Natalie's lips and tongue wrapped around my cock."
            "But one look at Sam tells me that she's taking out her frustrations on Natalie's ass."
            "She all but pounds away on the other girl, not letting up on her for a second."
            "Just the sight of it is enough to make me feel like I want to cum."
            "And Sam must read that on my face, as she shakes her head desperately."
            samantha.say "No...ah..."
            samantha.say "Not...yet..."
            "With that, she yanks the dildo out of Natalie's ass."
            "There's an almost comical pop, and then she collapses onto the bed."
            "My cock comes out Natalie's mouth, and Sam instantly pounces."
            show samantha threesome1 with fade
            "She goes to work then, giving me head like her life depends on it."
            "Still dazed, all Natalie can do is suck on my balls as she watches."
            "Again, Sam is the one that seems to have something to prove."
            "And she goes at it as if to show she's better than Natalie in every way."
            "All of which means it doesn't take me long to reach my climax..."
            "But almost as soon as she feels the cum on her tongue, Sam on the move again."
            "Before I know what's happening, she has me on my feet by the bed."
            show samantha threesome3 glasses with fade
            "She and Natalie are laid on their backs beneath me."
            show samantha threesome3 cumshot with vpunch
            "It's only as I start to cum over them that I see the selfie-stick."
            show samantha threesome3 nataliefacial samanthafacial with vpunch
            "Sam films each and every moment, as my load rains down on their faces."
            show samantha threesome3 -cumshot nataliebody samanthabody with vpunch
            "Both of them get an equal dose, striped from forehead to chin."
            "Natalie looks surprised, blinking and gasping as she takes it."
            "But I see that Sam looks more determined."
            "She looks up at the phone, smiling the whole time."
            "And even before we're done, I know just who the film's meant for..."
            $ game.flags.nataliestart = True
            $ samantha.sexperience += 1
            $ game.flags.natalie_sex += 1
    scene bg black with dissolve
    return

label samantha_event_E01:
    play sound cell_vibrate loop
    "My phone buzzes violently in my pocket."
    "I'm already pulling on my clothes as I swipe the screen to check."
    $ result = renpy.call_screen("smartphone_choice", "Samantha")
    if not result:
        stop sound
        $ hero.cancel_event()
        $ samantha.love -= 5
        return
    $ samantha.flags.nodate = False
    $ samantha.flags.nokiss = False
    $ samantha.flags.divorced = True
    $ samantha.flags.engaged = False
    if samantha.love.max < 170:
        $ samantha.love.max = 170
    "It's Samantha. I pick my phone up and move to respond."
    stop sound
    "I don't really know what to say."
    "She... wants to meet me at the park."
    "My eyes dart up to the time at the top of the screen."
    "I've got time."
    "I quickly accept."
    "She says thanks and doesn't explain more than that."
    "I don't ask for more, afraid she might back out if I pressure her."
    "Ever since I told her Ryan cheated, I've felt bad that I made her so upset- but a relief of weight I didn't even know was there lifted off my chest the moment I admitted it."
    scene bg park with fade
    "I get to the park fast, and find myself panting as I get to the footpath leading into the area."
    "I spot Samantha's golden hair easily."
    "It looks like she hasn't found a spot to settle down yet."
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake!"
    else:
        mike.say "Sam!"
    show samantha casual sad with dissolve
    "She spins around, her eyes wide. We move towards each other and meet in the middle."
    samantha.say "..."
    samantha.say "Hi, [hero.name]."
    mike.say "Hey..."
    mike.say "How have you been?"
    samantha.say "Okay, I guess."
    mike.say "Good, good."
    "An awkward silence stretches between us. Samantha shakes her head lightly before looking up at me."
    samantha.say "Look, I'll get to the point. I'm still upset that you didn't tell me about Ryan sooner."
    samantha.say "But I want to thank you. You might not have told me at all, but you did."
    "I don't respond, deciding to let her speak."
    samantha.say "And I... want to break up with him."
    mike.say "I- oh."
    mike.say "Really?"
    samantha.say "Yes, really. I don't want to be with him anymore if he's going around with other women. I... I didn't want to believe it at first. But..."
    show samantha sad
    "Samantha starts to tear up and before I can even try to console her, she pulls herself together."
    mike.say "What?"
    samantha.say "I was heading out for work the other day. As I was leaving, I saw a girl at the door asking for him."
    samantha.say "Ryan said it was just a coworker who lived down the street looking to get a ride."
    samantha.say "But... it was the same girl in the picture you showed me."
    "Oh. She actually comes to their house? That's... low."
    if samantha.flags.nickname == "cupcake":
        mike.say "Aw, I'm sorry, Cupcake."
    else:
        mike.say "Aw, I'm sorry, Sam."
    samantha.say "No, no. It's okay. I should have seen it before."
    mike.say "There's no way you could have. He just pretended to love you-"
    ryan.say "Shut up!"
    show samantha surprised
    "Samantha's eyes move to look behind me and before I turn to look, I already know who it is."
    show ryan casual angry at left
    show samantha casual annoyed at right
    with moveinleft
    samantha.say "Ryan?! Did you follow me here?"
    "Ryan's face is red with anger. He ignores Samantha and comes straight up to me."
    ryan.say "How dare you?! Why would you tell her? What the hell is wrong with you?!"
    mike.say "What's wrong with me?"
    show ryan at left5 with hpunch
    "As I talk, Ryan shoves at my shoulder, making me stumble back slightly."
    show samantha casual surprised
    samantha.say "Ryan! Stop it!"
    mike.say "You don't deserve her."
    ryan.say "Shut up! She's my wife, you homewrecker!"
    show ryan at left4 with move
    "He shoves me again, but this time I expect it, not budging."
    show samantha casual annoyed at top_mostright with move
    samantha.say "Ryan! We're done! Are you even listening?!"
    ryan.say "Shut it, Samantha!"
    show samantha casual surprised
    "Ryan's rage turns to her."
    menu:
        "Fight":
            hide samantha with dissolve
            "I don't even have to think about it."
            play sound punch_hard
            pause 0.2
            show ryan fight punchryan at center, hshake
            pause 0.2
            with hpunch
            "I pull my fist back and aim straight for his face."
            "He apparently doesn't expect me to actually throw a punch, so it lands head on."
            "Ryan stumbles back, shock plastered on his now bloodied face."
            "Red pours out of his nose and onto his lips. My knuckles start to sting and ache from the impact."
            if hero.fitness >= 50:
                "Ryan charges at me but I side step him before he can shove his elbow into me."
                "I lift my foot and aim a hard kick at his side, making him step back and hunch over."
                play sound punch_hard
                pause 0.2
                show ryan fight punchryan at center, hshake
                pause 0.2
                with hpunch
                "He recovers faster than I expect, gathering himself easily. Before he can come at me again, I rush forward and aim my fist right at his chest."
                "It lands and his breath wheezes out painfully."
                "Ryan coughs and tries to get the air back."
                "I roughly push him to the ground and he keels over submissively."
                hide ryan
                hide samantha
                show samantha casual close angry
                samantha.say "[hero.name]! Ryan! Stop, please!"
                "Sam's voice breaks me out of my stupor."
                "The adrenaline is rushing past my ears and making my arms shake, so I'm surprised I even heard her."
                "I back up, and Ryan stays on the ground."
                "As he catches his breath, he glares up at me with unbridled hatred."
                show samantha annoyed
                "Samantha grabs my hand and starts to drag me away."
                "I don't fight it."
                "We leave Ryan there, but I think he's learned not to come near her again."
            else:
                play sound punch_hard
                pause 0.2
                show ryan fight punchmike at center, hshake
                pause 0.2
                with hpunch
                "Ryan charges at me and shoves his elbow into my ribs."
                "I wheeze, feeling something crack on impact."
                samantha.say "Stop! Please!"
                "I try to straighten but wince."
                play sound punch_hard
                pause 0.2
                show ryan fight punchmike at center, hshake
                pause 0.2
                with hpunch
                "A fist to the side straightens my back for me as my body twitches away."


                pause 0.2
                with vpunch
                "Another fist comes, but I manage to block with the side of my arm."
                "Is it really blocking if you still feel the pain, though?"
                play sound punch_hard
                pause 0.2
                show ryan fight punchryan at center, hshake
                pause 0.2
                with hpunch
                "I push back at Ryan as hard as I can."
                "He slips on the mud under his feet and lands on his side."
                "He hisses in pain and stands back up."
                hide ryan
                hide samantha
                show samantha casual close angry
                "Before I can react, Samantha launches herself in front of me, arms out protectively."
                "Ryan doesn't seem deterred, coming closer and raising his fist."
                "But at last he falters."
                "His eyes soften at Sam and he lowers his arm."
                "Ryan shakes his head roughly and turns away."
                "He stops for a long moment, looking like he wants to say something."
                "And he leaves."
                "It's quiet for a long moment before I sit down heavily on the ground, wincing at the ache in my ribs."
                hide samantha
                show samantha casual
                samantha.say "[hero.name]! Oh my gosh... are you okay?"
                mike.say "It's okay. I'm fine."
                "Maybe. I might have to stop by the clinic on the way back home, but I'm not going to die."
                samantha.say "I'm so sorry this happened!"
                "Sam looks like she's about to burst into tears again and I can practically see the guilt blanketing over her."
                if samantha.flags.nickname == "cupcake":
                    mike.say "Cupcake. This isn't your fault. This is in no way your fault."
                else:
                    mike.say "Sam. This isn't your fault. This is in no way your fault."
                "Sam shakily nods her head unconvincingly. She instead stares at me, searching for something."
                mike.say "What-"
                show samantha kiss casual
                $ samantha.flags.kiss += 1
                "I'm cut off as she leans forward, pressing her lips into mine."
                samantha.say "... Thank you."
                "It's a whisper, but I hear her loud and clear."
                hide samantha
            call injured from _call_injured_11
        "Leave":
            "I block his vision and back up."
            mike.say "Ryan. You need to calm down."
            ryan.say "Fuck you!"
            "I gesture for Samantha to start leaving and she takes the hint."
    scene bg black with dissolve
    return


label samantha_are_you_sick:
    call samantha_greet from _call_samantha_greet_1
    show samantha sad
    samantha.say "Seriously, do something, you look like you are dying..."
    show samantha flirt blush
    if samantha.love > 80:
        samantha.say "You want me to play doctor?"
        $ samantha.love += 1
    elif samantha.love > 120:
        samantha.say "I could be your sexy nurse..."
        $ samantha.love += 1
        if samantha.flags.engaged and not (samantha.flags.cuck_ryan or samantha.flags.knows_ryancheats):
            samantha.say "Just kidding, don't get your hopes up."
    $ samantha.love += 1
    return

label samantha_buy_dress:
    show samantha
    "Samantha is looking at a sexy dress with hesitating eyes..."
    call samantha_greet from _call_samantha_greet_2
    samantha.say "That dress is gorgeous, but I can't afford it."
    if hero.money >= 100:
        $ result = renpy.display_menu([("Propose to buy it", 1), ("Say nothing", 2)])
        if result == 1:
            mike.say "I'll get it for you..."
            show samantha happy
            if samantha.love > 40:
                samantha.say "Thank you so much [hero.name]!"
                $ hero.money -= 100
                $ samantha.love += 2
            elif samantha.love > 20:
                samantha.say "I can't accept it but thanks for the offer."
                $ samantha.love += 1
            else:
                "Samantha smiles at me."
                samantha.say "Go get a girlfriend to buy clothes to instead of me."
                $ samantha.love += 1
            show samantha normal
        else:
            samantha.say "Maybe next month..."
            $ samantha.love -= 1
    else:
        samantha.say "It wouldn't be wise..."
    hide samantha
    return

label samantha_forgot_money:
    show samantha surprised
    samantha.say "Fuck!"
    if samantha.flags.nickname == "cupcake":
        mike.say "What's up Cupcake?"
    else:
        mike.say "What's up Samantha?"
    $ samantha.flags.greeted = TemporaryFlag(True, "day")
    show samantha sad
    samantha.say "I forgot my money."
    if hero.money >= 50:
        $ result = renpy.display_menu([("Propose to help", 1), ("Say nothing", 2)])
        if result == 1:
            mike.say "Don't worry, I'll pay for you."
            show samantha happy
            samantha.say "Thanks, you are a true friend."
            $ hero.money -= 50
            $ samantha.love += 1
        else:
            samantha.say "I'll have to make them write it on my tab..."
            $ samantha.love -= 1
    else:
        samantha.say "I'll have to make them write it on my tab..."
    hide samantha
    return

label samantha_kiss_me:
    call samantha_greet from _call_samantha_greet_3
    show samantha
    if samantha.flags.knows_ryancheats and not samantha.flags.kiss:
        "Samantha looks at me longingly."
        if samantha.love < 160:
            hide samantha
            return
    if samantha.flags.kiss:
        hide samantha
        show samantha kiss
        with dissolve
        "I'd spent so long imagining how it would go if I ever had the chance to kiss Sam."
        "Going over every possible detail in my mind until it was as familiar as the sight of my own face in the mirror."
        "That's why she takes me completely by surprise when she's the one to step up and kiss me."
        "It's a possibility that never even crossed my mind, and so I can't react at first."
        "I just stand there, letting her kiss me, until finally I find the will to return the gesture."
        "This feels crazy, like the world turned upside down."
        "But the kiss itself, that feels so right that it can't be wrong."
        hide samantha kiss
        show samantha
        with dissolve
        if samantha.flags.engaged and not (samantha.flags.cuck_ryan or samantha.flags.knows_ryancheats):
            samantha.say "I should seriously stop doing that..."
        $ samantha.flags.kiss += 1
        $ samantha.love += 1
    else:
        "Samantha seems to hesitate a little, then leans toward me, she obviously tries to kiss me."
        $ result = renpy.display_menu([("Kiss her", 1), ("Don't kiss her", 2)])
        if result == 1:
            hide samantha
            show samantha kiss
            with dissolve
            "I'd spent so long imagining how it would go if I ever had the chance to kiss Sam."
            "Going over every possible detail in my mind until it was as familiar as the sight of my own face in the mirror."
            "That's why she takes me completely by surprise when she's the one to step up and kiss me."
            "It's a possibility that never even crossed my mind, and so I can't react at first."
            "I just stand there, letting her kiss me, until finally I find the will to return the gesture."
            "This feels crazy, like the world turned upside down."
            hide samantha kiss
            show samantha
            with dissolve
            mike.say "What was that all about?"
            if samantha.flags.engaged and not (samantha.flags.cuck_ryan or samantha.flags.knows_ryancheats):
                show samantha surprised
                samantha.say "Oh my god... Why did I do that... Ryan..."
            else:
                show samantha flirt
                samantha.say "Face it tiger, you just hit the jackpot!"
            $ samantha.flags.kiss += 1
            $ samantha.love += 1
        elif result == 2:
            show samantha sad
            "Samantha looks hurt when I push her away."
            $ samantha.love -= 1
    hide samantha
    return

label samantha_birthday_date_male:
    $ DONE["samantha_birthday_date_male"] = game.days_played
    $ game.active_date.clothes = "date"
    scene bg door restaurant
    show samantha date
    with fade
    "I have to keep reminding myself that the reason I'm out with Sam is to celebrate her birthday."
    "That should mean that she's the centre of attention, the one that's getting a treat tonight."
    "But the problem is that I feel so lucky to be spending this time alone with her."
    "And it's making me feel like I'm the one being treated instead!"
    scene bg restaurant
    show samantha date at right
    with fade
    "As soon as we walk into the restaurant, a waiter hurries over to seat us."
    mike.say "Ah, we should have a reservation?"
    "Waiter" "Yes, here it is."
    "Waiter" "Would you like a table by the window?"
    "Waiter" "Or one of the booths along the back wall?"
    "I shrug at the question, not really having a preference."
    "And so I turn to Sam and ask her instead."
    if samantha.flags.nickname == "cupcake":
        mike.say "You're the birthday girl, Cupcake."
    else:
        mike.say "You're the birthday girl, Sam."
    mike.say "What do you think?"
    samantha.say "Hmm..."
    samantha.say "Maybe the booth?"
    samantha.say "Then we can chat in peace."


    menu:
        "Agree":
            if samantha.sub >= 50:
                $ game.active_date.score -= 10
            else:
                show samantha happy
                $ game.active_date.score += 15
            mike.say "You know what - I think the booth sounds best."
            if samantha.flags.nickname == "cupcake":
                mike.say "I don't really want to share you with everyone else, Cupcake!"
            else:
                mike.say "I don't really want to share you with everyone else, Sam!"



            "That decided, the waiter shows us to a vacant booth."
        "Ask for the window table":
            if samantha.sub >= 50:
                $ game.active_date.score += 15
            else:
                show samantha happy
                $ game.active_date.score -= 10
            mike.say "You know what - I like the sound of that table by the window."
            mike.say "After all, we've got nothing to hide."
            if samantha.flags.nickname == "cupcake":
                mike.say "Do we, Cupcake?"
            else:
                mike.say "Do we, Sam?"

            samantha.say "Nothing at all, [hero.name]."
            "As if to underline the point, Sam wraps her arm around mine."
            "I can feel her press herself against me."
            "And the sensation is quite something too!"
            "That decided, the waiter shows us to the table by the window."
    hide samantha
    show samantha date normal at center, zoomAt(1.5, (640, 1140))
    with fade
    "Once we're settled at the table, the waiter hands us a pair of menus."
    "There's the usual round of studying and scrutinising."
    "But in the end we choose what we want to eat and the waiter leaves us alone."
    mike.say "This is a pretty nice place, huh?"
    "Sam smiles back at me, looking this way and that."
    samantha.say "Yeah, it is..."
    "I can sense the imminent approach of a 'but' in the conversation."
    samantha.say "Ah...what the hell."
    samantha.say "I guess I should have told you anyway."
    if samantha.flags.nickname == "cupcake":
        mike.say "Told me what, Cupcake?"
    else:
        mike.say "Told me what, Sam?"
    samantha.say "Well...Ryan and I used to come here a lot."








    samantha.say "Anyway..."
    samantha.say "Why are we even talking about Ryan?"
    "Sam makes tries to shake off the mood the mere mention of the name's put her in."
    "She ends up smiling at me, but the effort it requires is almost written on her face."
    samantha.say "Actually, isn't it someone's birthday?"
    if not hero.has_gifts:
        $ game.active_date.score -= 20
        show samantha sad
        "I raise my glass at this, motioning for Sam to do likewise."
        mike.say "Here's to the birthday girl!"
        samantha.say "I'll drink to that!"
        "We both take a drink, laughing the whole time."
        "I get the vaguest feeling that Sam was expecting something more."
        "But it's soon forgotten as the food arrives a moment later."
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_16
        $ renpy.log(f"Sam give_a_gift - choose_gift result: {type(_return)}{_return}")
        if _return != "done":
            if _return not in ["None", "exit"]:
                if samantha.flags.nickname == "cupcake":
                    mike.say "Here you go, Cupcake."
                else:
                    mike.say "Here you go, Sam."
                mike.say "Happy Birthday!"
                show samantha surprised
                samantha.say "Oh, [hero.name] - you didn't need to get me anything."
                show samantha happy
                samantha.say "But I'm happy you did!"
                show samantha normal
                "I hand the gift over to Sam."
                play sound [paper_ripping_2, paper_ripping_1]
                "And then I watch as she opens it."
                if _return:
                    show samantha surprised
                    $ game.active_date.score += 20
                    samantha.say "Oh, [hero.name]..."
                    samantha.say "How did you know?"
                    if samantha.flags.nickname == "cupcake":
                        mike.say "Is...is there something wrong, Cupcake?"
                    else:
                        mike.say "Is...is there something wrong, Sam?"
                    show samantha happy
                    samantha.say "It's so perfect - Ryan would never have..."
                    samantha.say "Let's...let's just say it's perfect, yeah?"
                else:
                    show samantha sad
                    $ game.active_date.score -= 20
                    samantha.say "Ah, yeah..."
                    samantha.say "That's...that's very thoughtful of you!"
                    if samantha.flags.nickname == "cupcake":
                        mike.say "Is...is there something wrong, Cupcake?"
                    else:
                        mike.say "Is...is there something wrong, Sam?"
                    show samantha surprised
                    samantha.say "No...no..."
                    samantha.say "Oooh, look - doesn't the food look amazing?"
            else:
                show samantha sad
                $ game.active_date.score -= 20
                "I raise my glass at this, motioning for Sam to do likewise."
                mike.say "Here's to the birthday girl!"
                samantha.say "I'll drink to that!"
                "We both take a drink, laughing the whole time."
                "I get the vaguest feeling that Sam was expecting something more."
                "But it's soon forgotten as the food arrives a moment later."
    show samantha normal blush
    "I can see that Sam looks more than a little emotional right now."
    "Her voice is getting just a bit wobbly and uneven."
    "And I'm just wondering if I shouldn't say something to her."
    "But that's when I realise that she's way ahead of me in terms of what she's drinking."
    "I watch as she polishes off what must be at least her fourth or fifth drink so far."
    "No wonder she's starting to slur her speech!"
    $ sam_drunk = 0
    menu:
        "Tell her to slow down":
            if samantha.sub >= 50:
                show samantha happy
                $ game.active_date.score += 15
            else:
                $ game.active_date.score -= 10
            mike.say "Whew - what are we even drinking tonight?"
            if samantha.flags.nickname == "cupcake":
                mike.say "I don't know about you, Cupcake."
            else:
                mike.say "I don't know about you, Sam."
            mike.say "But this stuff is going straight to my head!"
            "At first I think Sam's going to react badly."
            "That she's going to accuse me of being a pussy."
            "Or even worse, assume that I'm calling her a lush."
            "But then she puts a hand to her forehead and nods."
            samantha.say "I...I am feeling a little light-headed."
            samantha.say "Maybe we should both slow down a bit?"
            "I nod at this, grateful to have avoided making a scene."
        "Let her have her birthday fun":
            $ sam_drunk += 1
            if samantha.sub < 50:
                show samantha happy
                $ game.active_date.score += 15
            "But then it is Sam's birthday."
            "And it sounds like she's got a lot to get off of her chest too."
            "Maybe what she really needs is the chance to blow it all off?"
            if samantha.flags.nickname == "cupcake":
                mike.say "Hey, Cupcake - you need a top up there?"
            else:
                mike.say "Hey, Sam - you need a top up there?"
            samantha.say "Oh...yeah, sure thing!"
            samantha.say "You know, If Ryan were here right now, he'd be on my case like crazy."
            samantha.say "'You're drunk, Sam!'"
            samantha.say "'You're embarrassing me, Sam!'"
            samantha.say "Not like you, [hero.name]."
            samantha.say "You accept me for who I am - warts and all!"
            if samantha.flags.nickname == "cupcake":
                mike.say "What can I say, Cupcake?"
            else:
                mike.say "What can I say, Sam?"
            mike.say "I'm just trying to be the best friend I can!"
    show samantha normal
    "The rest of the meal passes without incident."
    "And all too soon it's time to ask for the bill."
    if hero.money >= 200:
        show samantha happy
        $ game.active_date.score += 15
        $ hero.money -= 200
        "I toss down enough to cover the bill without pausing."
        "But then a thought occurs to me, and I toss down an extra bill as a tip."
    else:
        $ game.active_date.score -= 10
        if samantha.flags.nickname == "cupcake":
            mike.say "Erm, Cupcake..."
        else:
            mike.say "Erm, Sam..."
        mike.say "I'm a little short here!"
        samantha.say "Oh, [hero.name] -what are you like?"
        samantha.say "It's just like back when we were housemates!"
        samantha.say "I was always lending you money then too."
    show samantha normal
    if samantha.flags.nickname == "cupcake":
        mike.say "Ah, what now, Cupcake?"
    else:
        mike.say "Ah, what now, Sam?"
    mike.say "You want to call it a night?"
    mike.say "Or we could go someplace else?"
    if not game.active_date.score >= 30:
        samantha.say "Aw, I'd love to, [hero.name]."
        samantha.say "But I'm feeling beat."
        samantha.say "That and I have to be up early in the morning."
        if samantha.flags.nickname == "cupcake":
            mike.say "Okay, Cupcake, no problem."
        else:
            mike.say "Okay, Sam, no problem."
        scene bg street with fade
        "I hail a taxi for Sam once we're outside the restaurant."
        "She climbs into the back and waves to me as it pulls away from the curb."
        return
    else:
        show samantha happy
        samantha.say "Of course we should go somewhere else, [hero.name]!"
        samantha.say "I'm having a good time, and I don't want it to end yet."
        if samantha.flags.nickname == "cupcake":
            mike.say "Okay, Cupcake, that's great."
        else:
            mike.say "Okay, Sam, that's great."
        mike.say "Where should we go next?"
        samantha.say "I know, let's hit a nightclub!"
        samantha.say "I have a VIP pass for this place downtown."
        scene bg street with fade
        "I hail a taxi as soon as we're outside the restaurant."
        "Sam climbs in with me following close on her heels."
    scene bg street
    show samantha date normal
    with fade
    "As soon as we jump out of the taxi in front of the nightclub, we're greeted with a long line to get in."
    "We dutifully join the very back of the queue, as I figure that it's a waste of breath complaining."
    "But then a thought occurs to me and I turn to Sam, cocking my head to one side."
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake, didn't you say that you had a VIP pass for this place?"
    else:
        mike.say "Sam, didn't you say that you had a VIP pass for this place?"
    mike.say "I thought you mentioned it back at the restaurant."
    samantha.say "Um, yeah, that's right."
    samantha.say "What's up?"
    samantha.say "The queue's not put you off, has it?"
    mike.say "No, that's not it."
    mike.say "Actually, I was wondering if your pass would let us skip the queue?"
    "At this, Sam digs around in her purse and pockets until she finds the pass."
    "She squints at it in the imperfect light, trying to make out the fine print."
    samantha.say "Ah...yeah, I think so."
    samantha.say "We could just go straight in if we wanted."




    menu:
        "Wait":
            if samantha.sub >= 50:
                $ game.active_date.score -= 10
            else:
                show samantha happy
                $ game.active_date.score += 15
            "I look at the length of the queue again."
            "And it doesn't look nearly as long as it did before."
            mike.say "It's moving pretty quick."
            mike.say "I'm fine with waiting."




            "And so we wait patiently until we reach the front of the queue."
            "The bouncer on the door takes his sweet time about it."
            "But then he finally nods and waves us inside."
        "Jump the queue":
            if samantha.sub >= 50:
                show samantha happy
                $ game.active_date.score += 15
            else:
                $ game.active_date.score -= 10
            "I look at the length of the queue again."
            "And it looks even longer than it did before."
            mike.say "Ah, screw this!"
            mike.say "What's the point of having a VIP pass if you act like a pleb?!?"





            "And so we step out of line and walk straight to the front."
            "The bouncer nods at the pass and waves us straight in."
    scene bg nightclub
    show samantha date normal
    with fade
    "Once we're inside the club, the atmosphere is pretty infectious."
    "I can already feel the beat of the music that's playing as it hooks me."
    "And all that I want to do is hit the dance floor as soon as possible."
    "It's then that I see the perfect space open up, right in the middle of the dancing throng."
    if samantha.flags.nickname == "cupcake":
        mike.say "Hey, Cupcake."
    else:
        mike.say "Hey, Sam."








    menu:
        "Let's dance":
            if samantha.sub >= 50:
                show samantha happy
                $ game.active_date.score += 15
            else:
                $ game.active_date.score -= 10
            if samantha.flags.nickname == "cupcake":
                mike.say "Come on, Cupcake - don't be a stick-in-the-mud!"
            else:
                mike.say "Come on, Sam - don't be a stick-in-the-mud!"
            hide samantha
            show dance samantha date
            with fade
            "With that, I take Sam by the hand, leading her onto the dance floor."


            "She seems a bit awkward at first."
            "Almost as if she's not comfortable with so many pairs of eyes on her."
            "But I soon manage to make her concentrate on me instead of the crowd around us."
            "In the end, we're dancing pretty close together."
            "And Sam starts to forget herself, moving even closer to me."
            "By the time the music changes, altering the mood, she's all but pressed against me."
            "We're both hot, sweaty and gasping for breath as we leave the dance floor."
            "Maybe some time to chill out in the VIP lounge is what we need most of all right now..."
            hide dance
        "Let's drink":
            if samantha.sub >= 50:
                $ game.active_date.score -= 10
            else:
                show samantha happy
                $ game.active_date.score += 15
            "I can see that Sam's wanting to hit the VIP lounge first."
            "And as it's her birthday, I guess she should get her way."
            if samantha.flags.nickname == "cupcake":
                mike.say "Okay, Cupcake."
            else:
                mike.say "Okay, Sam."
            mike.say "I am curious to see what it's like."
            mike.say "Let's hit the VIP lounge."



    scene bg vip
    show samantha date normal
    with fade
    "I let out an impressed whistle as we walk into the VIP lounge."
    mike.say "Hey, this place is really nice!"
    samantha.say "Well, duh - isn't it supposed to be?!?"
    "I shake my head at Sam, giving her a knowing smile."
    "It feels so great to be able to joke with her like this."
    "And I wonder how I ever coped without her in my life."
    "She really is someone very special to me on so many different levels."
    "We claim a private booth in which we can't be seen from outside."
    "And then we start to order drinks from the bar that exclusively serves the VIP lounge."
    "It doesn't take long before we're chatting about old times and laughing our asses off."
    "The whole time the drinks are flowing, and I begin to lose track of just how many I've had."
    if samantha.flags.nickname == "cupcake":
        mike.say "Jesus, Cupcake - my head's spinning!"
    else:
        mike.say "Jesus, Sam - my head's spinning!"
    mike.say "Maybe we should slow down..."
    show samantha happy
    "Sam laughs out loud at this, lurching towards me as she does so."
    show samantha date close happy with hpunch
    "She collapses across my lap, looking up at me while still giggling."
    samantha.say "Look, [hero.name] - I've fallen for you!"
    "She reaches up and wraps her hands around my neck."
    "And then she tries to pull me down towards her."
    menu:
        "Tell her to slow down":
            if samantha.sub >= 50:
                $ game.active_date.score -= 10
            else:
                show samantha happy
                $ game.active_date.score += 10
            show samantha normal
            "But when I instinctively resist, a frown appears on her face."
            samantha.say "What?"
            samantha.say "What's the problem, [hero.name]?"
            samantha.say "You like me...and I like you..."
        "Let her have her birthday fun":
            $ sam_drunk += 1
            if samantha.sub >= 50:
                $ game.active_date.score += 10
            else:
                show samantha happy
                $ game.active_date.score -= 10
            "I'm every bit as far gone as Sam is right now."
            "And so I don't even think of stopping her."
            hide samantha
            show samantha kiss date
            with dissolve
            $ samantha.flags.kiss += 1
            "Our lips meet and I feel her tongue dart between my lips."
            "Once we've gone that far, there's no chance of putting a stop to it."
            "Sam kisses me with ever more intensity."
            "But then she begins to twist so that her head turns into my lap."
            hide samantha
            show samantha date close normal
            with dissolve
            "This breaks the kiss with a loud gasp from both of us."
            "And as I look down, I see her already fumbling with my flies..."
    if not sam_drunk == 0 or not game.active_date.score >= 50:
        if samantha.flags.nickname == "cupcake":
            mike.say "Cupcake, you're drunk."
        else:
            mike.say "Sam, you're drunk."
        mike.say "You're not thinking straight."
        mike.say "This is a bad idea - trust me!"
        hide samantha
        show samantha date normal at center, zoomAt(1.5, (640, 1140))
        "I help Sam to sit up again."
        "And the gesture seems to help sober her up a little."
        show samantha surprised
        samantha.say "Whoa...my head!"
        show samantha sad
        samantha.say "Maybe you're right, [hero.name]."
        samantha.say "I don't feel so good..."
        "I help Sam to her feet and lead her through the club and out into the street."
        scene bg street with fade
        "And then I hail a taxi and see her safely into the back seat."
        return
    else:
        call samantha_birthday_sex from _call_samantha_birthday_sex
    return

label samantha_birthday_sex:
    scene bg vip
    show samantha close date flirt blush
    with fade
    "I'm thankful for the fact that the booth we're in is totally private, so no one can see what Sam's doing."
    "But as she hungrily tears at my flies and reaches in for my cock, I wonder if the same thought even occurred to her!"
    "Needless to say that she finds it already standing to attention as she pops it out and grabs it in her hand."
    show samantha happy
    samantha.say "Ah..."
    show samantha flirt
    samantha.say "Now that's what I'm talking about!"
































    "I can feel the sweat beading on my forehead."
    "But my breathing is controlled and I'm far from spent."
    "And I think that Sam can sense all of this from the way I'm still looking at her hungrily."
    samantha.say "[hero.name]..."
    samantha.say "Why are you looking at me like that?"
    if samantha.flags.nickname == "cupcake":
        mike.say "Like what, Cupcake?"
    else:
        mike.say "Like what, Sam?"
    samantha.say "Like you're still ravenous - and I'm the main course!"
    "I don't bother to answer her question."
    "Instead I turn her around and push her forwards until she's kneeling in the seat."
    "Sam glances back over her shoulder at me as I pull her skirt up."
    "And then I hear her gasp in anticipation as I tug down her panties too."
    show sam nightclub sex with fade
    "I hold onto her haunches as I probe between her buttocks."
    "The head of my cock finds the folds of her pussy a moment later."
    "And it's every bit as wet and slick as I'd hoped it would be."
    "I don't stop to ask for permission, just push my way into her."
    "Sam moans softly, almost mewling in pleasure at the sensation."
    samantha.say "Oooh...oh..."
    samantha.say "Yes...please..."
    samantha.say "Stick it in me, [hero.name]!"
    samantha.say "Your cock feels SO good!"
    "By now I'm up to my balls inside of Sam."
    "I can feel her quivering and shaking from the me just pushing in there."
    "And so when I begin to thrust in and out of her, the effect is all the more impressive."
    "Sam rides my cock like her life depends on it, starting to moan and wail too."
    "We're not making beautiful, delicate love here."
    show sam nightclub sex wet
    "I'm fucking her, plain hard and simple."
    "And she's loving every single moment of it too!"
    "The sound of the music outside the booth drowns everything else out."
    "But inside, all I seem to be able to hear is the sound of us going at it."
    "Sam crying like a vixen on heat."
    "That and the sound of my thighs slapping against her bare buttocks."
    show sam nightclub sex cum -wet with hpunch
    "And when I cum, it's in a sudden, almost brutal thrust."
    with hpunch
    "She feels it like nothing before, jerking as I fill another one of her holes."
    with hpunch
    "Sam gasps and flinches around my cock, and I know that she's cumming too."
    "After I'm done, I pull out of her slowly, feeling her shudder as I do so."
    "Still shaking from the aftershocks of her orgasm, Sam cleans herself up as best she can."
    scene bg street with dissolve
    "We leave the club quietly, hailing a taxi once we're on the street outside."
    "Only now do I feel the fatigue beginning to catch up with me."
    "And I wonder if I can stay awake for the duration of the journey home."











    return

label samantha_exclusive_cheated:





    "This date with [active_girl.name] goes pretty well. And I wonder about my next move."
    "Girl" "[hero.name]?"
    "Still lost in my thoughts, I turn back to see who's calling."
    play sound spank
    with hpunch
    scene expression f"bg {game.room}" at center, zoomAt (1, (640, 1145)), blur(4), swing(1.07, 0.6, 1.08, -0.6, 0.5)
    show samantha angry at center, blur(2), zoomAt (1, (640, 840)), swing(1.0, 0.4, 1.0, -0.4, 0.5)
    with fade
    "Which I guess is why the sudden sensation of being struck in the face comes as a complete surprise!"
    "Suddenly I'm seeing stars, and my cheek feels like it's been blistered with a cheese-grater."
    "I honestly don't think I'd have even known what was happening."
    "That is if not for the yelling that comes along in it's wake..."
    scene expression f"bg {game.room}"
    show samantha angry
    show fx anger
    with dissolve
    samantha.say "How does that feel, you lying piece of shit?!?"
    mike.say "Huh...wha..."
    mike.say "H...hey..."
    mike.say "What the hell?!?"
    play sound spank
    show samantha angry at center, zoomAt (1.5, (640, 1040))
    with hpunch
    "Sam doesn't hesitate to slap me a second time, catching me on the other cheek."
    show fx anger
    samantha.say "You lied to me, you bastard!"
    samantha.say "And like a moron, I believed you!"
    mike.say "What are you even talking about?!?"
    mike.say "Didn't we just get through dealing with this?"
    "Sam makes to hit me for a third time, aiming a back-handed blow at my face."
    hide samantha
    show samantha casual angry
    "But this time I'm ready for it, and I manage to slink backwards and out of range."
    samantha.say "Yeah, I thought we did too."
    show samantha casual annoyed
    samantha.say "But then I started having my doubts."
    samantha.say "So I followed you."
    "I'm surprised by the shock I feel at her telling me this."
    "And I can't say if it's more from guilt or the invasion of my privacy!"
    mike.say "You followed me?!?"
    mike.say "How could you do that?"
    show samantha casual angry blush
    "Sam's fuming at me by now, her eyes wide with rage."
    "I fully expect her to start grinding her teeth or foaming at the mouth."
    show fx anger
    samantha.say "How could I not?!?"
    samantha.say "I needed to know if you were telling the truth, [hero.name]."
    samantha.say "I needed to know that I could trust you!"
    show fx anger
    samantha.say "But now, I see you with her, so I know that I can't!"
    if samantha.flags.nickname == "cupcake":
        mike.say "I...I'm sorry, Cupcake."
    else:
        mike.say "I...I'm sorry, Sam."
    show samantha sad
    samantha.say "You know, if you'd have just come out and told the truth, I'd have forgiven you."
    samantha.say "What Ryan did taught me that nobody's perfect, [hero.name]."
    samantha.say "And I didn't need to think that you're perfect."
    samantha.say "All I needed was to know that you were honest with me..."
    "With that, Sam turns her back on me and starts to walk away."
    hide samantha with dissolve
    "I think about running after her, about pleading with her."
    "But my cheeks are still stinging from the slaps she gave me."
    "And something tells me that there's going to be no talking her round this time."
    "She doesn't even need to say that it's over in as many words."
    "I know without being told that I just watched our relationship come to a crashing end."
    "And all I did was stand here, watching Sam walk away from me."
    $ samantha.set_gone_forever()
    $ game.active_date.stay = False
    $ renpy.hide(date_girl.id)
    $ renpy.hide(active_girl.id)
    $ game.room = game.room.replace("date_", "")
    return

label samantha_pregnant_request:
    "Most of the time you can tell when a girl wants to ask something but can't summon up the courage."
    "You know what I mean - they beat about the bush, or they try to come at it from another angle?"
    "But then there are the girls that have enough confidence just to come out and say it."
    "And guess which camp Sam falls into..."
    show samantha
    samantha.say "Hey, [hero.name]..."
    samantha.say "What do you think about us having a baby?"
    with vpunch
    "I almost choke on my own tongue as what she just said sinks in."
    "But all my apparent distress gets me from Sam is a chuckle and a shake of the head."
    show samantha annoyed
    samantha.say "Wow!"
    samantha.say "I didn't think it was that repulsive of an idea!"
    "Starting to recover a little, I shake my head desperately."
    "The last thing that I want is for Sam to think that I find anything involving her repulsive!"
    mike.say "Ah, no..."
    if samantha.flags.nickname == "cupcake":
        mike.say "No way, Cupcake!"
    else:
        mike.say "No way, Sam!"
    mike.say "That's not what I meant."
    mike.say "You just caught me off-guard, that's all."
    show samantha normal
    samantha.say "Okay, okay..."
    samantha.say "I believe you, [hero.name], honestly I do!"
    samantha.say "But take a moment to think about it, yeah?"
    "I really wasn't joking when I said that Sam had taken me by surprise."
    "And even now she's giving me some time to think about it, I'm still in a spin."
    "Does she really expect me to be able to give her an answer on the spot?"
    samantha.say "I said take a moment, [hero.name]."
    samantha.say "I didn't say take forever!"
    "Apparently that's exactly what she's expecting!"
    if samantha.flags.nickname == "cupcake":
        mike.say "Okay, Cupcake."
    else:
        mike.say "Okay, Sam."
    mike.say "I'm thinking..."
    mike.say "I'm still thinking..."
    "I hate being put on the spot like this at the best of times."
    "But this is a really serious decision, which makes it that much worse."
    "If I spring for the wrong answer, then I've screwed up badly!"
    menu:
        "Agree":
            "I always saw kids in the future for Sam and me."
            "Only I never really thought about it being the immediate future!"
            "But then when have we been able to plan for the long-term?"
            "I spent so long holding a torch for Sam when she was with Ryan."
            "And then, when that came to an end, everything seemed to happen so fast."
            "So if there's something we both want out of life, why should we wait?"
            if samantha.flags.nickname == "cupcake":
                mike.say "I always wanted kids, Cupcake."
            else:
                mike.say "I always wanted kids, Sam."
            mike.say "So why not now?"
            "Sam's eyes go wide at this."
            "And I can see she's delighted with my answer."
            show samantha blush
            samantha.say "You really mean that?"
            samantha.say "You're not just saying it to make me happy?"
            "I shake my head, dismissing her fears."
            mike.say "I'm not Ryan, remember?"
            mike.say "I love you too much not to be honest!"
            show samantha close flirt
            "Sam leans into me, wrapping her arms around my waist."
            "I do the same in return, enjoying moment."
            show samantha normal
            samantha.say "This is a big step, [hero.name]."
            samantha.say "Kids are going to change our lives forever."
            show samantha happy
            samantha.say "But at least we get to have some fun along the way!"
            $ samantha.love += 2
            $ samantha.flags.pregrequest = True
        "Refuse":
            "It's not like I don't see kids in the future for Sam and me."
            "Just not in the immediate future, that's all!"
            "I mean, it's not that long ago that she was planning her future with Ryan."
            "Wait a minute..."
            "What if this is something to do with how all of that ended?"
            "It'd be a big mistake for us to have kids just because of that."
            "Just because Sam maybe thinks it'd make our relationship more solid."
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake, be honest with me, yeah?"
            else:
                mike.say "Sam, be honest with me, yeah?"
            mike.say "This is different, totally different."
            mike.say "But were you planning to have kids so soon with Ryan?"
            show samantha annoyed
            "Suddenly Sam becomes defensive."
            "She frowns as she crosses her arms and glares at me."
            samantha.say "What the hell's that supposed to mean?!?"
            samantha.say "You think I'm just replacing him with you or something?"
            if samantha.flags.nickname == "cupcake":
                mike.say "No, Cupcake - of course not."
            else:
                mike.say "No, Sam - of course not."
            mike.say "I just want to be sure that you're ready for kids, you know?"
            mike.say "That you're not trying to do it for any other reason."
            mike.say "Because I don't need you to have my babies to stay with you."
            mike.say "And I'm willing to wait until the time is right."
            "Sam opens her mouth to say something ferocious."
            "But then she stops and her mood seems to change."
            show samantha sad
            "She nods, looking a little sad."
            samantha.say "That...actually makes a lot of sense, [hero.name]."
            samantha.say "I suppose I never looked at it that way before!"
            samantha.say "Maybe we should wait after all?"
            "I nod at this, happy we can agree with one another."
            $ samantha.love -= 2
    return


label samantha_side_event_01:
    play sound cell_vibrate
    pause 1.0
    "Getting texts out of the blue from either Sam or Ryan seems to have become quite the thing in my life."
    "So when I get one at random one afternoon from the former, I'm at least glad to see it's not from the latter."
    samantha.say "Miss U - when can U cum over?"
    "Well, at least she hasn't totally degenerated into text-speak."
    "Not wanting to be drawn into a long, turgid text conversation, I decide to just call her instead."
    play sound phone_calling
    "I know, I'm an old romantic at heart..."
    stop sound
    samantha.say "Hey, [hero.name] - you got my text?"
    if samantha.flags.nickname == "cupcake":
        mike.say "Yeah, Cupcake, I got it."
    else:
        mike.say "Yeah, Sam, I got it."
    samantha.say "Well...can you...come over, that is?"
    menu:
        "Sure":
            mike.say "Sure, I'd love to see some more of you."
        "I'm quite busy right now":
            mike.say "Sorry Sam, maybe some other time?"
            samantha.say "Alright. Sorry for bothering you."
            $ samantha.love -= 5
            $ hero.cancel_event()
            return
    mike.say "But what about Ryan?"
    samantha.say "Don't worry about him, he's not here right now."
    samantha.say "And he won't be back for a long time yet, either."
    mike.say "Erm...okay, I guess that means there's nothing to keep me from dropping in to see you."
    samantha.say "Great - I'm looking forward to it already..."
    scene bg house
    with fade
    play sound car_door
    queue sound car_ignition
    with hpunch
    "Still a little curious, I hop into the car and drive the short distance over to Sam and Ryan's place."
    "On the way, I tell myself that my nerves are probably nothing more than the feeling that I'm going behind Ryan's back in seeing Sam without his knowledge."
    "But then she was my friend before she was his wife, and he's hardly in a moral position to judge me for just wanting to spend time with her."
    "If that was all I really wanted to do..."
    show bg street with fade
    "Sam's already standing in the doorway, leaning against the frame as I pull up and park the car."
    stop sound
    "Though she's silhouetted in the light from the hallway behind her, I can already see that she's wearing something figure-hugging and stretchy."
    show samantha normal sport at top_mostleft with easeinleft
    "As I get closer, I can see that it's a pair of black leggings with a turquoise band of lace around the waistband."
    "She has on a vest-top in the same colour, that leaves her midriff bare and shows off her breasts very well indeed."
    "I can't for the life of me decide if the outfit is yoga gear, pyjamas or actually underwear."
    "Either way, the turquoise really brings out the colour of her eyes, and she looks very sexy in it."
    show samantha happy at left with ease
    samantha.say "Hey there, glad you could make it over."
    if samantha.flags.nickname == "cupcake":
        mike.say "Hey, Cupcake - good to see you."
    else:
        mike.say "Hey, Sam - good to see you."
    "She notices me glancing around a little nervously."
    samantha.say "I told you Ryan's not here already!"
    show samantha normal
    samantha.say "Trust me, he's not hiding in the bushes, waiting to pounce!"
    "I nod, realising how paranoid I must seem right now."
    mike.say "Okay, okay...I'm just not used to doing this kind of thing behind his back!"
    show samantha annoyed
    samantha.say "Don't think of it that way - I don't."
    samantha.say "This isn't like what Ryan did to me."
    show samantha normal
    samantha.say "This is the way things always should have been, and we're just putting it right, one step at a time!"
    scene bg samhome
    show samantha normal sport
    with fade
    "With that, she ushers me inside and closes the door."
    show samantha at center, zoomAt (1.5, (640, 1040)) with dissolve
    "We stay in the kitchen for a while, just chatting about nothing in particular."
    "Somehow a glass of wine appears in my hand, and soon after one materialises in Sam's too."
    "For a moment I feel like I've been transported back in time to when we lived together."
    show samantha happy
    "Only this time someone was kind enough to erase Ryan from the picture."
    "We're getting on so well that I can't even begin to imagine why I ever let this girl slip through my hands."
    "But maybe, like she says, we're already on the path to righting that wrong?"
    "After a few more glasses of wine, we end up almost leaning against one another."
    "Though I can't tell if it's because we want to be closer, or for mutual support as we get steadily more drunk together."
    "Eventually it happens, and she's in my arms, the whole thing feeling as natural as breathing."
    hide samantha
    show samantha kiss sport
    with fade
    $ samantha.flags.kiss += 1
    "We kiss long and passionately, being thankful for the chance to take our own sweet time about it."
    "And before I know it, Sam's beaten down the last of my resistance."
    hide samantha
    show samantha normal sport
    with fade
    "She's leading me to the living room by one hand, without needing to say a single word."
    "Looks like I'm about to cuck Ryan on his own sofa!"
    "But when Sam leads me into the actual room, I instantly freeze on account of what I see laid on the couch."
    "It's Ryan, fully clothed and not moving a muscle!"
    mike.say "Fuck, what's he doing there!" with vpunch
    mike.say "You said he wasn't even here!"
    show samantha happy at startle
    "Sam laughs and strolls to the sofa so that she can lean over her husband."
    samantha.say "Hey, Ryan - wake up!"
    "No response."
    samantha.say "[hero.name]'s here...and he's going to screw my brains out, right in front of you!"
    "Still nothing."
    samantha.say "That's okay with you, right - I'll take your silence as a yes!"
    mike.say "Jesus, Sam - what did you do to him?"
    if samantha.flags.cuck_ryan:
        show samantha normal
        samantha.say "Oh, don't shit yourself on his account."
        samantha.say "I just slipped him a good dose of sleeping pills - he won't wake up until tomorrow morning, not even if you slap him silly."
        mike.say "Isn't that dangerous?"
        samantha.say "I know what I'm doing - I've been drugging him like this since the night of the honeymoon."
        samantha.say "He's always had to take the pills as long as I've known him."
        samantha.say "So he's used to taking them - never even notices an extra dose here and there on occasion."
        "Oh, well - that makes it perfectly okay then!"
        mike.say "If you say so..."
        show samantha happy
        "Sam laughs at my hesitation as she pulls her top off over her head and tosses casually aside."
        samantha.say "He was cheating on me behind my back, and I never knew it."
        show samantha normal
        samantha.say "So we're going to turn the tables on him - in his own house!"
        show samantha topless with dissolve
        "I have to admit, I've always wanted the chance to fuck Sam and get one over on Ryan."
        "I guess I just never thought he'd be there in the room when it actually happened!"
        "Oh yes, in all the confusion, I almost forgot - Sam just took her top off, didn't she?"
        "I can see from the look on her face that she's been aware I hadn't seemed to notice this whole time as well."
        show samantha happy
        samantha.say "Now he finally looks at these!"
        "She begins to massage her breasts, squeezing and pressing them together so that they instantly become all I can see."
        "A moment later she inches down her leggings and kicks them away, turning so that her ass is on show as she climbs onto the bed."
        show samantha naked with dissolve
        samantha.say "Well, if you want some of this, then you're just going to have to come and get it, aren't you..."
        "This is Sam, naked and on all fours, literally offering herself up to me."
        hide samantha
        show samantha doggy samlivingroom nomike smile
        with fade
        "Is Ryan's unconscious form really going to be able to put me off?"
        "And when you think about it, if I'm fucking her doggy style, I won't actually be able to see him at all!"
        "I strip off as quickly as I can, tossing my clothes aside with almost desperate abandon."
        "Looking over her shoulder at my progress, Sam can't help but laugh at my eagerness to reach her."
        samantha.say "Come on, over here!"
        "I'm on her in mere seconds after that, taking her by surprise and earning a gratifying squeal of near shock from Sam."
        show samantha doggy -nomike out
        "This melts into a moan of sheer pleasure as she feels my cock slip between her thighs and begin to press against the lips of her pussy."
        "There's no doubt that she's ready for this, as her skin is soft and warm against me, but she's hot and almost molten where it makes the most difference."
        "But still I take my time as my cock enters her, enjoying every small degree of progress."
        samantha.say "Fuck me, [hero.name]!"
        show samantha doggy vaginal
        "The strain in Sam's voice is pure music to me, and I begin to fuck her harder, trying to oblige."
        samantha.say "Oh yeah, that's right - I want it hard, [hero.name]!"
        "My pace quickens, as I hurry to stoke the fire in her further."
        samantha.say "Jesus, that's good...I want it harder, [hero.name]!"
        samantha.say "I want you to fuck me so hard that my pussy forgets all about my fucking prick husband!"
        "I'm practically thumping her ass by this point, making her thighs shake with the effort."
        show samantha doggy scream closed
        samantha.say "Fuck me so hard that I forget all about him..."
        samantha.say "Fuck my brains right...out...of...my...head!"
        "That's it - I can feel myself cumming as she shouts these last few words."
        show samantha doggy creampie with hpunch
        "There's no time to even think about what I'm doing as I force myself into Sam and let go."
        with hpunch
        "She's worked herself into such a state that she follows me within mere seconds."
        show samantha doggy out scream with hpunch
        "Sam arches her back and cums like an animal, like a beast."
        "I've never seen her like this before, almost feral in her aspect."
        "If she howled, I wouldn't be in the least bit surprised."
        "Slither out of her and collapse on the floor, utterly exhausted."
        "But it seems Sam still has a score to settle."
        hide samantha doggy
        show samantha naked
        with fade
        "She clambers over Ryan's still comatose form, settling with her crotch hovering over his face."
        "Sam waits for a few moments, and then grins wickedly as the first of my cum begins to seep out of her."
        "Gravity soon sends it spattering onto Ryan's still blissfully unaware features."
        hide samantha
        show samantha close naked angry
        samantha.say "You feel that, you asshole?"
        samantha.say "You smell it too?"
        "Ryan must unconsciously feel the cum, which is now dripping onto his face impressive amounts."
        "Even if I do say so myself."
        "His lips move, his mouth opens slightly, and some of the cum inevitably seeps in."
        "This understandably delights Sam."
        samantha.say "Taste it, you bastard...that's the taste of the guy that's fucking your wife!"
    else:
        show samantha normal
        samantha.say "I killed him, [hero.name], and I'm not ashamed to say that I did it so we could be together!"
        "For a moment, I can't do anything but make incoherent noises."
        samantha.say "Oh, [hero.name], you're lost for words at the level of my devotion to our love!"
        mike.say "Oh shit, oh shit, oh shit!"
        "Sam crawls onto the bed in front of me, grabbing handfuls of my t-shirt as she looks up at me pleadingly."
        samantha.say "Oh, [hero.name], it's this desire for you, that's what drove me to do it!"
        samantha.say "And if you don't take me now, if you don't prove that you DO love me..."
        samantha.say "I'm afraid that I might...I might...kill again!"
        show samantha naked with dissolve
        "Sam pulls down her leggings, exposing her ass and the first glimpses of her pussy."
        "She turns around, getting down on all fours as she straddles Ryan's body."
        hide samantha
        show samantha doggy samlivingroom nomike smile
        with fade
        samantha.say "I need you inside of me, [hero.name] - it's the only thing that can keep me from becoming a killer for love of you!"
        "I feel like I'm watching my life from afar, seeing some poor guy get pulled down into a web of murder and intrigue."
        "Already I'm thinking about how to dispose of the body and cover up Sam's terrible crime."
        "But more immediately, I need to keep her from feeling the urge to kill again."
        show samantha doggy -nomike out
        "As if on auto-pilot, I pull down my pants."
        "Even in such a state of mind, Sam can still get me hard, and it doesn't take long for me to be ready."
        show samantha doggy vaginal
        "There's little need to arouse her either, and as I push into her, I can't help thinking that the idea of murder is actually what's making her wet."
        show samantha doggy scream closed
        "I can't last long, but all the same, Sam moans and twitches like a cat on heat."
        with hpunch
        "And as I cum into her, all I can think is that I'm fucking a murderer atop the still warm corpse of her own husband."
        show samantha doggy creampie with hpunch
        "The best I can hope for is a sweet book deal before they send me down for life and strap her into the electric chair!"
        show samantha doggy out scream with hpunch
        "After we're done, Sam clambers over Ryan's corpse until her crotch is over his face."
        hide samantha doggy
        show samantha naked
        with fade
        "I look on in horror, as she lets my cum drip out of her and onto his already stiffening features."
        mike.say "My god, Sam...you're a monster!"
        hide samantha
        show samantha close normal naked
        samantha.say "Oh yeah...about that!"
        samantha.say "Funny thing - you see, he's not really dead."
        mike.say "WHAT?!?" with hpunch
        show samantha close happy
        samantha.say "I just doped him up real good with some sleeping pills, that's all."
        mike.say "So what was all that about?"
        samantha.say "Well, I knew you really wanted to fuck me, so I just decided to give you some motivation."
        samantha.say "And it worked!"
        "Good god - she might not be a murderer, but she's definitely a psycho!"
    scene bg house with fade
    "By the time I need to be driving home, Sam and I have had some strong coffee and most of the alcohol has worn off."
    "She still seems very high on herself, pleased with what she's achieved tonight."
    "On the other hand, I'm glad to have become so close to her in such a short space of time."
    "But the intensity of her emotions has really brought it home to me just how serious all of this could become."
    "Though for now, I'll just have to wait and see what our next encounter brings."
    $ samantha.sexperience += 1
    $ samantha.flags.cuck_ryan = True
    return

label samantha_side_event_02:
    "I'd like to say that in the weeks after Sam and Ryan's wedding I'd been able to forget about what happened before the ceremony, that it became a distant memory."
    "But it would be closer to the truth to admit that it was nagging at me a good amount of the time before I received a text message from Ryan himself."
    "It came pretty much out of the blue, and took the form of an invite to come over to their new place for an evening meal at the weekend."
    menu:
        "Accept invitation":
            pass
        "Decline invitation":
            "The largest part of me loathed the notion of setting foot into Ryan's house and having to listen to him bragging about every single aspect of his life."
            "So I turn the invitation down"
            $ samantha.love -= 5
            $ hero.cancel_event()
            return
    scene bg taxi car closed with fade
    "The largest part of me loathed the notion of setting foot into Ryan's house and having to listen to him bragging about every single aspect of his life."
    "But then I started to wonder about just how much he might know about the things Sam had learned on their wedding day, and whether she might have felt so guilty that she confessed all to him."
    "Turning him down would likely look like a snub and arouse his suspicions, and so I sent him a reply accepting the offer."
    "I had no further contact with either Ryan or Sam until the appointed night, fearing much the same things."
    scene bg taxi car open
    pause 1.0
    play sound car_door
    scene bg taxi car closed
    "And so when I stepped out of the taxi with a crappy bottle of wine in my hand, I still wasn't sure just what to expect."
    "Of course the house is a new-build, part of a development in a gentrified part of town."
    "The buildings from which it and the surrounding properties are converted looked to have once been something industrial that I can't identify."
    "But there was no doubt in my mind that Ryan would tell me all of that, at length, over dinner."
    play sound door_bell
    scene bg black with dissolve
    scene bg samhome at center, zoomAt(2.0, (240, 1340))
    show samantha date at center, zoomAt(1.25, (640, 920))
    with wiperight
    "To my surprise, it's was Sam who answers the door."
    show samantha happy
    "She smiles at the sight of me and takes the bottle of wine."
    "Though I can see there's something lurking beneath her otherwise happy expression."
    samantha.say "Hey, [hero.name], great to see you again so soon!"
    samantha.say "Thanks for the wine!"
    "Her tone is too loud and ebullient for the situation, and I frown in puzzlement."
    show samantha annoyed at center, zoomAt(1.5, (640, 1040))
    "A second later, she leans in closer and speaks in a more normal tone of voice."
    "I can only assume that she's been exaggerating her speech to keep Ryan from hearing what she says next."
    samantha.say "This was HIS idea...but I'm glad that you agreed to come."
    samantha.say "After the wedding, well...I really felt that we had unfinished business...you know?"
    mike.say "You could say that, yeah."
    mike.say "Look, Sam - if this is going to be in any way awkward..."
    show samantha normal
    samantha.say "No, no...it's fine, really...please don't go."
    "Her eyes are so full of pleading that I can't do anything but stay."
    scene bg samhome at center, zoomAt(1.5, (320, 1040))
    show samantha date at left5
    with fade
    "I step into the hallway and shrug off my coat, noting the improvement in Sam's mood as I do so."
    ryan.say "Hey, [hero.name] - how are you doing?"
    show ryan casual smile at center, zoomAt(1.0, (1040, 720)) with easeinright
    "Ryan appears, waving from a doorway that I presume leads into the sitting room."
    "He looks as smug as ever - and what in the hell is he wearing?"
    "Something grey and woollen, that looks as if it doesn't know if it wants to be a cardigan or a jacket."
    "Jesus - what a douche."
    mike.say "Hey, Ryan...good to see you."
    show ryan casual -smile at center, zoomAt(1.0, (780, 720)) with ease
    ryan.say "Sorry I didn't get to see you at the wedding - so many people, so busy, you know?"
    ryan.say "Sam told me she managed to have some intercourse with you though."
    with vpunch
    mike.say "What?!?"
    show ryan smile
    ryan.say "You know - social intercourse...chatting and exchanging a little gossip!"
    mike.say "Well, now that you mention it..."
    show samantha at left4 with ease
    "Sam chooses this rather awkward moment to jump in."
    samantha.say "I have to go check on the food."
    samantha.say "You can give [hero.name] the tour on your own, can't you...dear?"
    "There's a subtle hint of poison in the supposed term of endearment, but Ryan either misses it, or else chooses to ignore it completely."
    ryan.say "Of course, dear...I can handle [hero.name] here, don't you worry."
    hide samantha with easeoutleft
    "As she turns to walk away, I distinctly see Sam mouth the words 'meet me in the kitchen' for my benefit."
    scene bg samhome at center, zoomAt(2.0, (140, 1340))
    show ryan casual smile at center, zoomAt(1.15, (640, 820))
    with fade
    "From there I'm subjected to what feels like an eternity of plodding from one room to another as Ryan extolls the virtues of everything he owns."
    "I tune him out pretty quickly, and instead use the time to try to discern what the state of affairs between them must be."
    "Sam seems tense, but that could simply be because I'm here."
    "Though she has already dropped pretty strong hints that she wants the chance to bring up what happened between us at the wedding."
    "For his part, Ryan seems as oblivious and self-absorbed as ever, treating me with the same amount of condescension as always."
    "My guess was that so long as I was careful, it was probably safe to let my guard down a little."
    scene bg samhome at center, zoomAt(2.0, (0, 1140))
    show ryan casual smile at center, zoomAt(1.35, (640, 940))
    with fade
    "After the tour, Ryan and I end up in the sitting room, talking about some crap that's not important."
    mike.say "I never knew Sam was much of a cook - in fact, I can't ever remember her cooking the entire time we lived together!"
    ryan.say "Well, I'm the gourmet chef of the household, so I do most of the cooking around here."
    ryan.say "I took a course, you know, under a chef with a Michelin star, no less!"
    "I roll my eyes, trying to make it look like amazement, rather than boredom."
    show ryan annoyed
    ryan.say "But Sam's been trying to learn how to toss something simple together for a while now."
    ryan.say "So don't blame me if you wind up with food poisoning after tonight!"
    "I nod vaguely, wondering how this prick ever convinced a woman to put up with him, let alone marry him."
    mike.say "You mind if I go take a look at what she's making?"
    mike.say "Allergies, you know..."
    show ryan casual -annoyed
    "Ryan wrinkled his face in an expression meant to say that he understood."
    "And I was quick to take the opportunity to see less of his face for a few minutes."
    "The one thing the tour was helpful with was finding my way quickly to the kitchen."
    scene bg samhome at center, zoomAt(1.5, (960, 920))
    show samantha date at center, zoomAt(1.25, (640, 860))
    with fade
    "I walked in on Sam as she was chopping vegetables, the meal seeming to be too early in preperation to really say something like it smelled good merely as a compliment."
    samantha.say "Urgh...I thought you'd never tear yourself away from that bloviating prick!"
    show samantha at center, zoomAt(1.5, (640, 1040))
    "She puts down what she's doing and wraps her arms low around my waist."
    "I return the casual hug, thinking that we're just old friends, glad to be reunited after some time apart."
    "But when she unexpectedly turns her face up to me and kisses me slowly on the lips - I begin to think that maybe I've misread the situation here!"
    hide samantha
    show samantha kiss date
    with fade
    $ samantha.flags.kiss += 1
    if samantha.flags.cuck_ryan:
        "I've been waiting for the chance to kiss Sam for so long that this feels almost too good to be true."
        "She's practically throwing herself at me, and in the house where she and Ryan are supposed to be living as man and wife too!"
        "I slip my tongue into Sam's mouth without waiting for permission, and move my hands down to squeeze her buttocks through the tight blue dress she's wearing."
        "Sam begins to breathe more heavily in response to my actions, starting to move against me in a manner that makes her feelings entirely clear."
        hide samantha
        show samantha date at center, zoomAt(1.5, (640, 1040))
        with fade
        "When the kiss finally ends, she almost gasps, as if in relief for something that's been bothering her for a long time."
        samantha.say "God, I've been thinking about doing that to you non-stop since the wedding."
        samantha.say "Even on the honeymoon I was imagining it."
        samantha.say "When Ryan fell asleep, I was putting my fingers..."
        if samantha.flags.nickname == "cupcake":
            mike.say "Whoa, okay...okay, Cupcake...I get the picture!"
        else:
            mike.say "Whoa, okay...okay, Sam...I get the picture!"
        mike.say "I take it from all that the situation isn't any better between you two?"
        "She shakes her head, frowning at the mention of the subject."
        samantha.say "I tried, [hero.name], honestly I did."
        samantha.say "But the idea was already up here."
        "She points to her forehead."
        samantha.say "And it just kept getting worse the harder I tried."
        mike.say "So why am I here, in the middle of this scene of domestic bliss?"
        mike.say "If you'd wanted to hook up, you could have come to my place?"
        samantha.say "I don't know...maybe I thought there was a chance seeing you'd scratch the itch..."
        mike.say "Let me guess - it didn't?"
        "She shakes her head with a rueful look in her eyes."
        mike.say "For what it's worth, I'm not mad."
        mike.say "In fact, I'm more than willing to help you scratch that bothersome itch..."
        samantha.say "Jesus, [hero.name] - I thought you'd never ask!"
    else:
        hide samantha
        show samantha date at center, zoomAt(1.5, (640, 1040))
        with fade
        "When the kiss is over, I step back a little way, a puzzled look on my face."
        if samantha.flags.nickname == "cupcake":
            mike.say "Cupcake...what exactly was that all about?"
        else:
            mike.say "Sam...what exactly was that all about?"
        "She shrugs a little and cocks her head to one side as she answers."
        samantha.say "Well, let's just say that I've had some time to think about what you said to me back before the wedding."
        mike.say "All of the stuff about not messing around behind Ryan's back?"
        show samantha happy
        "Sam smiles at my gentle rebuke and reminder."
        samantha.say "I was thinking more about the part where I propositioned you..."
        samantha.say "And where you admitted that you'd always wanted me..."
        if samantha.flags.nickname == "cupcake":
            mike.say "I remember, Cupcake - I was there too!"
        else:
            mike.say "I remember, Sam - I was there too!"
        show samantha normal
        samantha.say "I got to thinking, you see...about how you could have taken advantage of my vulnerable mental and emotional state."
        samantha.say "But you didn't."
        mike.say "I also said that I didn't want to be a cheating shit, like Ryan - didn't I?"
        samantha.say "This isn't the same, [hero.name] - really it's not."
        "If she's reasoned out why it's not, then I want to hear her logic."
        samantha.say "That was one person betraying another."
        samantha.say "This is two people realising that...that they might have made a mistake."
        samantha.say "And taking a chance to put that right!"
        "I have to admit that I like the sound of it more when she puts it like that!"
        mike.say "You're still married to that...what did you call him...that 'bloviating prick' sat in the other room!"
        samantha.say "I can't ask for a divorce this soon into the marriage, his lawyer would gut me in the settlement!"
        samantha.say "You have to believe me when I say that I'll ask for one as soon as I can!"
    show samantha flirt blush
    samantha.say "In the meantime...how about you fuck me, right here and now?"
    mike.say "Whoa, you don't waste any time, do you?"
    mike.say "You'd do that - even with Ryan sitting in the next room?!?"
    show samantha normal
    samantha.say "[hero.name] - just how much time do you think I have to waste?"
    show samantha angry
    samantha.say "I already made the mistake of marrying a cheating bastard while there was a decent guy that wanted me right under my nose."
    show samantha flirt
    samantha.say "I lost all of that time - and now I want something back as way of compensation!"
    "She's leaning back against the kitchen counter as she says all of this."
    "One hand rubbing her stomach and the other playing with the hem of her tight, blue dress."
    "Sam tilts her head, letting her dirty blonde locks fall over one of her massive, blue eyes."
    "She never did have to try very hard when she wanted to look seductive."
    menu:
        "Push her back":
            if samantha.flags.nickname == "cupcake":
                mike.say "No, Cupcake...I don't think that's a good idea."
            else:
                mike.say "No, Sam...I don't think that's a good idea."
            show samantha annoyed
            "Sam begins to protest, but I cut her off abruptly."
            show samantha sad
            mike.say "If you ever want to divorce this guy and get your fair share, you need to keep a reign on that kind of thing!"
            mike.say "If Ryan walks in here and catches us, you'll be fucked - literally and figuratively!"
            mike.say "You've waited this long, Sam - what's wrong with waiting a little longer still?"
            mike.say "I know you can do it, that you're strong enough."
            "Sam looks at me with frustration and disappointment showing on her face."
            show samantha annoyed
            samantha.say "Aaahhh...I suppose you're right."
            if samantha.sexperience == 0:
                samantha.say "But I was so looking forward to feeling you inside of me for the first time..."
            else:
                samantha.say "But I was so looking forward to feeling you inside of me again..."
            "Thanks, Sam - you're really making this easy for me!"
        "Fuck her":
            "Ryan might be in the next room, but I'm not about to let that stop me getting my hands on his wife."
            "There's even a part of me that thinks I wouldn't actually mind him walking in on us, just to see the look on his face."
            show samantha surprised with hpunch
            "I put my hands on Sam's thighs and push her roughly into the counter."
            "She looks a little shocked at the sudden move, but then her face breaks into a willing grin, urging me on."
            show samantha flirt
            samantha.say "As soon as we get rid of that cunt in the sitting room, you can do this to me whenever you like!"
            "I lean in and start to kiss her neck as she's saying this, making her sigh in appreciation."
            samantha.say "We can play happy families, and I'll let you lift up my skirts whenever you like..."
            hide samantha
            show samantha doggy samkitchen nomike smile
            with fade
            "She pulls up the hem of her dress at this, guiding one of my hands to slip into her panties."
            "I kiss her the same moment that my fingers find her pussy, and both sets of lips are invitingly wet to the touch."
            "I yank Sam's panties down as she struggles blindly with my flies."
            "By the time she's freed my cock, I have them halfway down her thighs."
            show samantha doggy -nomike out smile
            "Sam obligingly turns so that she's facing the counter, dragging my dick over her thigh and one buttock as she goes."
            samantha.say "You're home early, dear - did you bring me a little present home from work?"
            "She looks back over her shoulder at me while pulling down the straps of her dress."
            "Sam's not wearing a bra underneath, and so her breasts are freed to sit proud upon her chest."
            "I can't keep from seeking for her pussy now, and I find it easily."
            show samantha doggy vaginal
            "She's slick and welcoming, and I press into her in one smooth motion."
            samantha.say "Oh, darling - you did bring me something special - and I love it!"
            "Sam picks up a knife and actually begins to chop more vegetables as I thrust in and out of her."
            show samantha doggy arm with hpunch
            "Sighing deeply and even panting as I fuck her ever faster and with more vigour."
            show samantha doggy pant
            samantha.say "Ah...I'm afraid dinner might be a while yet...so why don't you play with me while you wait?"
            show samantha doggy -arm
            "I take that as a cue to begin fondling her naked breasts, squeezing her nipples between my fingers and thumbs until they're stiff and erect."
            show samantha doggy closed with hpunch
            "I'm almost shoving Sam into the counter by now, almost pounding her with all of my weight, but she seems to be liking it all the more."
            "I wonder how much of our passion is actually pent-up anger at Ryan that's finally finding an outlet."
            "But even if it is, I don't care and I won't stop."
            "At least not until I cum."
            show samantha doggy scream with hpunch
            "Which I do, into Sam as deep as I can manage."
            with hpunch
            "She follows my example, stabbing the knife she's been using a good half inch into the cutting block as she does so."
            show samantha doggy smile wink with hpunch
            "Afterwards, she leans back against me, a satisfied smile on her face."
            samantha.say "Why, darling - I do believe that I can feel you, seeping out of me and running down my thighs!"
            $ samantha.sexperience += 1
            $ samantha.flags.cuck_ryan = True
    scene bg samhome at center, zoomAt(2.0, (0, 1140))
    show ryan casual at center, zoomAt(1.35, (640, 940))
    with fade
    "When I return to the sitting room, I try to look casual and meet Ryan's eye without showing any signs of guilt."
    "But he's had sufficient time to think of a whole new round of tedious subjects to talk about, all of which revolve around him."
    show ryan casual smile at center, zoomAt(1.35, (940, 940))
    show samantha date at center, zoomAt(1.35, (340, 940))
    with fade
    "Dinner, when it finally arrives, is understandably awkward for Sam and myself."
    "And she doesn't help matters much by insisting on playing footsie under the table."
    show samantha flirt
    "At one point, I swear, even trying to reach up at one point and stroke my groin with her toes."
    "Afterwards, I make my apologies and they call me a taxi."
    scene bg taxi car night with fade
    pause 0.5
    show samantha date at center, zoomAt(1.25, (640, 920)) with easeinleft
    "Sam insists on seeing me out, while Ryan just gives me an absent wave from the sofa as I get up to leave."
    show samantha happy at center, traveling(2.0, 0.5, (640, 1340))
    pause 0.5
    show samantha flirt at center, traveling(1.5, 0.5, (640, 1040))
    "Once we're alone, Sam kisses me quite sweetly on the doorstep."
    samantha.say "Come back soon?"
    mike.say "Of course!"
    show samantha happy
    pause 1.0
    hide samantha with easeoutleft
    "She smiles genuinely at that promise, and then slips back inside."
    "I'm left alone in the glow of the streetlights, reflecting on the odd course of events this evening."
    "And wondering where my relationship with Sam will take me next."
    scene bg black with dissolve
    pause 1.0
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
