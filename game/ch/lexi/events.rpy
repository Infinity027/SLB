init python:
    Item("danny_corpse", display_name="Danny's corpse")

    Event(**{
    "name": "lexi_start",
    "label": "lexi_start",
    "priority": 500,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("nightclub", "nightclubbar"),
            IsFlag("lexiStart"),
            MinStat("money", 10),
            ),
        PersonTarget(lexi,
            IsFlag("lexiDelay", False)
            ),
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "lexi_event_02",
    "label": "lexi_event_02",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("lexi_start"),
        IsNotDone("lexi_event_02b"),
        IsSeason(0, 1),
        IsHour(20, 0),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom"),
            HasStamina(),
            ),
        PersonTarget(lexi,
            IsFlag("lexiDelay", False),
            ),
        ],
    "max_girls": 0,
    "gallery": {"character":"lexi", "label": "lexi_event_02", "id":"Pool", "icon": "lexi stand pool", "scene": "livingroom"},
    "music": "music/roa_music/alley.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "lexi_event_02b",
    "label": "lexi_event_02b",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("lexi_start"),
        IsNotDone("lexi_event_02"),
        IsSeason(3),
        "game.day < 25",
        IsHour(12, 18),
        HeroTarget(
            IsGender("male"),
            IsRoom("mall1"),
            HasStamina(),
            ),
        PersonTarget(lexi,
            IsFlag("lexiDelay", False),
            ),
        ],
    "max_girls": 0,
    "music": "music/roa_music/alley.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "lexi_event_03_hide",
    "label": "lexi_event_03_hide",
    "conditions": [
        Or(
            IsDone("lexi_event_02"),
            IsDone("lexi_event_02b")
            ),
        PersonTarget(lexi,
            Not(IsPresent()),
            Not(IsHidden()),
            MinStat("love", 100),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "lexi_event_03_look",
    "label": "lexi_event_03_look",
    "conditions": [
        IsDone("lexi_event_03_hide"),
        IsDayOfWeek(5, 6),
        IsHour(17, 23),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(lexi,
            IsFlag("DannyDelay", False)
            ),
        ],
    "do_once": True,
    })

    Activity(**{
    "name": "look_for_lexi_park",
    "label": "look_for_lexi_park",
    "conditions": [
        HeroTarget(
            HasRoomTag("park"),
            MinStat("energy", 2),
            MinStat("hunger", 1),
            MinStat("grooming", 1),
            MinStat("fun", 1),
            ),
        PersonTarget(lexi,
            IsFlag("looking"),
            IsFlag("lookpark", False),
            ),
        ],
    "icon": "lexi",
    "display_name": "Look for Lexi",
    "do_once": True,
    })

    Activity(**{
    "name": "look_for_lexi_mall",
    "label": "look_for_lexi_mall",
    "rooms": ("mall1", "mall2"),
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            MinStat("energy", 2),
            MinStat("hunger", 1),
            MinStat("grooming", 1),
            MinStat("fun", 1),
            ),
        PersonTarget(lexi,
            IsFlag("looking"),
            IsFlag("lookmall", False),
            ),
        ],
    "icon": "lexi",
    "display_name": "Look for Lexi",
    "do_once": True,
    })

    Activity(**{
    "name": "look_for_lexi_alley",
    "label": "look_for_lexi_alley",
    "rooms": "alley",
    "conditions": [
        HeroTarget(
            MinStat("energy", 2),
            MinStat("hunger", 1),
            MinStat("grooming", 1),
            MinStat("fun", 1),
            ),
        PersonTarget(lexi,
            IsFlag("looking"),
            IsFlag("lookalley", False),
            ),
        ],
    "icon": "lexi",
    "display_name": "Look for Lexi",
    "do_once": True,
    })

    Activity(**{
    "name": "look_for_lexi_club",
    "label": "look_for_lexi_club",
    "rooms": ("nightclub", "nightclubbar"),
    "conditions": [
        HeroTarget(
            MinStat("energy", 2),
            MinStat("hunger", 1),
            MinStat("grooming", 1),
            MinStat("fun", 1),
            ),
        PersonTarget(lexi,
            IsFlag("looking"),
            IsFlag("lookclub", False),
            ),
        ],
    "icon": "lexi",
    "display_name": "Look for Lexi",
    "do_once": True,
    })

    Event(**{
    "name": "lexi_event_04",
    "label": "lexi_event_04",
    "duration": 1,
    "conditions": [
        IsDayOfWeek(1, 2, 3, 4, 5),
        IsHour(10, 14),
        HeroTarget(IsRoom("map")),
        HasVehicle(motor=True),
        PersonTarget(lexi,
            IsFlag("looking"),
            IsFlag("lookpark"),
            IsFlag("lookmall"),
            IsFlag("lookalley"),
            IsFlag("lookclub"),
            ),
        ],
    "music": "music/roa_music/alley.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "lexi_event_05",
    "label": "lexi_event_05",
    "duration": 1,
    "conditions": [
        IsDone("lexi_event_04"),
        HeroTarget(IsRoom("livingroom")),
        PersonTarget(lexi,
            IsFlag("DannyDelay", False),
            MinStat("love", 120),
            ),
        ],
    "music": "music/roa_music/alley.ogg",
    "do_once": True,
    })

    WakeUpEvent(**{
    "name": "lexi_event_06",
    "label": "lexi_event_06",
    "duration": 2,
    "conditions": [
        IsDone("lexi_event_05"),
        IsHour(5, 9),
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(lexi,
            IsFlag("DannyDelay", False),
            MinStat("love", 140),
            ),
        ],
    "music": "music/roa_music/alley.ogg",
    "do_once": True,
    })

    Activity(**{
    "name": "lexi_event_07a",
    "display_name": "Dump Danny's corpse",
    "label": "lexi_event_07a",
    "duration": 4,
    "rooms": "beach",
    "conditions": [
        InInventory("danny_corpse"),
        IsHour(20, 6),
        PersonTarget(lexi,
            IsFlag("bypass_danny_corpse", 0),
            ),
        ],
    "do_once": True,
    "icon": "danny",
    })

    Activity(**{
    "name": "lexi_event_07b",
    "display_name": "Dump Danny's corpse",
    "label": "lexi_event_07b",
    "duration": 4,
    "rooms": "forest",
    "conditions": [
        InInventory("danny_corpse"),
        IsHour(20, 6),
        PersonTarget(lexi,
            IsFlag("bypass_danny_corpse", 0),
            ),
        ],
    "do_once": True,
    "icon": "danny",
    })

    InteractEvent(**{
    "name": "lexi_event_08",
    "label": "lexi_event_08",
    "duration": 1,
    "conditions": [
        HeroTarget(IsGender("male")),
        Not(InInventory("danny_corpse")),
        IsDone("lexi_event_06"),
        PersonTarget(lexi,
            IsActive(),
            IsFlag("bypass_danny_corpse", 0),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "date_lexi_meet_jack",
    "label": "date_lexi_meet_jack",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("date_mall1")),
        PersonTarget(lexi,
            OnDate(),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "date_lexi_meet_jack_2",
    "label": "date_lexi_meet_jack_2",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("date_lexi_meet_jack"),
        IsTimeOfDay("afternoon"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            ),
        PersonTarget(lexi,
            Not(IsHidden()),
            IsFlag("lexijack", False),
            ),
        ],
    "chances": 5,
    "do_once": True,
    })

    Event(**{
    "name": "date_lexi_meet_jack_3",
    "label": "date_lexi_meet_jack_3",
    "conditions": [
        IsDone("date_lexi_meet_jack_2"),
        HeroTarget(
            IsActivity("talk"),
            IsFlag("pimpingjack"),
            ),
        PersonTarget(lexi,
            IsPresent(),
            Not(IsHidden()),
            IsActive(),
            IsFlag("lexijack", False),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "date_lexi_meet_jack_4",
    "label": "date_lexi_meet_jack_4",
    "conditions": [
        IsDone("date_lexi_meet_jack_3"),
        IsTimeOfDay("afternoon"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsRoom("map")
            ),
        PersonTarget(lexi,
            Not(IsHidden()),
            IsFlag("lexijack", False),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "date_lexi_meet_ryan_1",
    "label": "date_lexi_meet_ryan_1",
    "conditions": [
        IsDone("date_lexi_meet_jack_2"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_mall1"),
            Not(IsFlag("ryandead")),
            IsFlag("pimpingjack")
            ),
        PersonTarget(lexi,
            OnDate(),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "date_lexi_meet_ryan_2",
    "label": "date_lexi_meet_ryan_2",
    "conditions": [
        IsDone("date_lexi_meet_ryan_1"),
        IsTimeOfDay("afternoon", "evening"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(IsFlag("ryandead"))
            ),
        PersonTarget(lexi,
            IsFlag("lexiryan", False),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "date_lexi_meet_ryan_3",
    "label": "date_lexi_meet_ryan_3",
    "conditions": [
        IsDone("date_lexi_meet_ryan_2"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(IsFlag("ryandead"))
            ),
        PersonTarget(lexi,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("lexiryan", False),
            IsFlag("pimpingryan"),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "date_lexi_meet_master_1",
    "label": "date_lexi_meet_master_1",
    "conditions": [
        IsDone("date_lexi_meet_jack_2"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_beach"),
            IsFlag("pimpingjack"),
            ),
        PersonTarget(lexi,
            OnDate(),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "date_lexi_meet_master_2",
    "label": "date_lexi_meet_master_2",
    "conditions": [
        IsDone("date_lexi_meet_master_1"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_beach"),
            IsFlag("pimpingmaster"),
            ),
        PersonTarget(lexi,
            OnDate(),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "date_lexi_meet_master_3",
    "label": "date_lexi_meet_master_3",
    "conditions": [
        IsDone("date_lexi_meet_master_2"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_beach"),
            IsFlag("pimpingmaster"),
            ),
        PersonTarget(lexi,
            OnDate(),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "lexi_bj_alley",
    "label": "lexi_bj_alley",
    "duration": 1,
    "conditions": [
        IsHour(0, 5),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsRoom("alley"),
            ),
        PersonTarget(lexi,
            Not(IsHidden()),
            Not(IsRoom("alley")),
            MinStat("love", 100),
            ),
        ],
    "music": "music/roa_music/alley.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "lexi_sell_drugs",
    "label": "lexi_sell_drugs",
    "conditions": [
        IsHour(0, 5),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsRoom("alley"),
            ),
        PersonTarget(lexi,
            Not(IsHidden()),
            MinStat("love", 150),
            ),
        ],
    "music": "music/roa_music/alley.ogg",
    "gallery": {"prepare": ["game.hour = 2"], "character":"lexi", "id": "Drugs", "label": "lexi_sell_drugs", "icon": "lexi stand2 alley casual manoutfit cum"},
    "do_once": True,
    })

    Event(**{
    "name": "lexi_preg_talk",
    "max_girls": 1,
    "label": "lexi_preg_talk",
    "do_once": False,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(lexi,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("toldpreg", False),
            MinCounter("pregnant", 6),
            ),
        ],
    "music": "music/roa_music/alley.ogg",
    })

    Event(**{
    "name": "lexi_sasha_1",
    "label": "lexi_sasha_1",
    "music": "music/roa_music/alley.ogg",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("date_mall1")),
        PersonTarget(lexi,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 150),
            MinStat("sub", 25),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            IsRoom("clothesshop", "mall1", "mall2"),
            MinStat("love", 150),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "lexi_sasha_dance",
    "label": "lexi_sasha_dance",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("lexi_sasha_1"),
        PersonTarget(lexi,
            OnDate(),
            IsRoom("date_nightclub")
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            IsRoom("nightclub", "nightclubbar"),
            Not(HasCheated()),
            Or(
                IsFlag("sexydate"),
                IsFlag("sluttydate"),
                ),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "lexi_sasha_fuck",
    "label": "lexi_sasha_fuck",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("lexi_sasha_dance"),
        HeroTarget(
            IsGender("male"),
            HasStamina(),
            ),
        PersonTarget(sasha,
            OnDate(),
            IsRoom("date_nightclub"),
            Not(HasCheated()),
            ),
        PersonTarget(lexi,
            IsRoom("nightclub", "nightclubbar")
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "lexi_slave_request",
    "label": "lexi_slave_request",
    "duration": 1,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("talk")),
        PersonTarget(lexi,
            IsActive(),
            MinStat("sub", 50),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "lexi_sasha_samantha_nightclub",
    "label": "lexi_sasha_samantha_nightclub",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("lexi_sasha_fuck", "samantha_event_A04"),
        HeroTarget(
            IsGender("male"),
            HasStamina(),
            ),
        Or(
            PersonTarget(lexi,
                OnDate(),
                ),
            PersonTarget(sasha,
                OnDate(),
                ),
            ),
        PersonTarget(lexi,
            Not(IsHidden()),
            IsRoom("date_nightclub", "nightclub", "nightclubbar"),
            ),
        PersonTarget(samantha,
            Not(IsHidden()),
            IsRoom("nightclub", "nightclubbar"),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            IsRoom("date_nightclub", "nightclub", "nightclubbar"),
            ),
        ],
    "do_once": True,
    })


    Event(**{
    "name": "lexi_dwayne_event",
    "label": "lexi_dwayne_event",
    "conditions": [
        IsDone("aletta_event_05"), 
        IsTimeOfDay("afternoon", "evening"),
        HeroTarget(
            IsActivity("work", "workhard", "work_personal", "workhard_personal"),
            IsFlag("dwaynedead", False), 
            MinFlag("promoted", 1),
            ),
        PersonTarget(lexi,
            Not(IsHidden()),
            MinStat("sexperience", 1)
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            MaxStat("sexperience", 0)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    })

    Event(**{
    "name": "lexi_pregnant_request",
    "label": "lexi_pregnant_request",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(lexi,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            IsFlag("status", "girlfriend"),
            ),
        'game.days_played - lexi.flags.girlfriend_day >= 7',
        'not lexi.pregnant',
        ],
    "music": "music/roa_music/alley.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "lexi_asleep",
    "label": "lexi_asleep",
    "priority": 1500,
    "conditions": [
        HeroTarget(IsRoom("livingroom")),
        PersonTarget(lexi,
            IsPresent(),
            Not(IsHidden()),
            IsActivity("sleep"),
            ),
        ],
    "once_day": True,
    "do_once": False,
    "once_hour": False,
    })

    Event(**{
    "name": "lexi_asleep_trailer",
    "label": "lexi_asleep_trailer",
    "priority": 1500,
    "conditions": [
        HeroTarget(IsRoom("trailerinside")),
        PersonTarget(lexi,
            IsPresent(),
            Not(IsHidden()),
            IsActivity("sleep"),
            ),
        ],
    "do_once": False,
    "once_hour": False,
    })

    Event(**{
    "name": "lexi_trailer_onfire",
    "label": "lexi_trailer_on_fire",
    "duration": 1,
    "priority": 500,
    "conditions": [
        Or(
            And(
                IsDone("lexi_sasha_fuck"),
                PersonTarget(samantha,
                    Or(
                        IsHidden(),
                        IsGone(),
                        ),
                    ),
                ),
            And(
                IsDone("lexi_sasha_samantha_nightclub"),
                PersonTarget(samantha,
                    Not(IsHidden()),
                    ),
                ),
            ),
        HeroTarget(
            IsRoom("trailer"),
            IsFlag("ongoinghomeharem", False),
            ),
        PersonTarget(lexi,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "music": "music/roa_music/alley.ogg",
    "do_once": True,
    })

    WakeUpEvent(**{
    "name": "lexi_morningwood",
    "priority": 500,
    "label": "lexi_morningwood",
    "duration": 1,
    "conditions": [
        IsHour(5, 9),
        HeroTarget(IsGender("male"),
            Not(InFlag("slept_with", "lexi")),
            Not(IsFlag("morningwood")),
            ),
        PersonTarget("lexi",
            Not(IsHidden()),
            IsRoom("livingroom"),
            IsActivity("sleep"),
            MinStat("love", 160),
            MinStat("sexperience", 2),
            ),
        RoomTarget("livingroom",
            NPCNumber(1)
            ),
        ],
    "chances": 20,
    "do_once": False,
    "once_month": True,
    })

label lexi_start:
    $ lexi.flags.lexiDelay = TemporaryFlag(True, 1)
    "Nightclubs are always so so."
    "Sometimes they're lavish and worth the effort to enter. You might even end up brushing shoulders with some high profile people."
    "Other times they're as tacky as they get. And they usually smell like puke."
    "Luckily this one is actually pretty damn good. Not the first time I've come here either."
    "I decided to come here on my own this time, since my friends are busy."
    "Usually they'd be happy to tag along, but I guess we all have our commitments to get to."
    "For now...my only commitment is trying to have a good time, and forget about nearly getting assaulted a while back."
    "Well, I actually was. Talk about danger..."
    "Leaning against the bar edge, I order a drink for myself casually, and scan the room."
    "Sipping my drink while dressed rather suavely, I figure I look inviting enough."
    "Naturally I'm looking to see if there are any lovely looking ladies around who might happen to be here alone too."
    "Who I don't expect to see is a familiar face."
    mike.say "No...fucking...way..."
    show lexi date happy at left with dissolve
    "It was only one time we met, but the event is so burned into my memory at this point that I recognize her instantly."
    "Blonde hair. Big boobs. Hell, she's wearing a crop top with the word 'SLUT' printed on it."
    "Yes, it could only be her. Though I know I shouldn't, I find myself walking towards that shady part at the back."
    "As I come closer, paying all my attention to her, I can see some sleight of hand beneath the booth table she's sitting at."
    "So...she not only plays accomplice in muggings, but she likes to dabble in drugs too?"
    "I'm not exactly a priest myself, but I don't take kindly to seeing it either."
    "The idea of her making any sort of money off this makes me angry."
    "She doesn't deserve it! She doesn't deserve anything..."
    lexi.say "See you around."
    "I can just pick up on her farewell to the guy sitting there with her. He gets up carefully, and casually struts away with the good stuff in his pocket."
    "The seat opposite her seems free now, and I assume it's for any potential buyer to take."
    "Well, I can be quite a good actor when I want to be. Maybe I ought to adopt that role."
    "Alternatively...I suppose I could just report her to one of the bouncers like a tattletale. Would be kind of lame, but at least it would mean she couldn't rope me into anything."
    menu:
        "Approach her directly.":
            "I can't be bothered with wasting time. I'd rather deal with this, right here and now."
            "I'm not the kind of guy who likes to wait around and hope. It's better to face things head on, in my own opinion."
            show lexi date at center with dissolve
            "So I approach her table just like that, and sit down in the chair opposite her side."
            "For a moment she doesn't seem to notice me, too busy fiddling around on her phone. I suppose I don't stand out much, but still..."
            "I can't wait to see how she reacts when she notices that it's me..."
            "After a few more minutes, Lexi finally rolls her eyes, clicks her tongue and puts her phone down."
            "Only then does she look up, and her eyes quickly widen like saucers."
            mike.say "Hello again."
            "Oh, it feels good. Just seeing that flash of alarm on her face, however brief it might be, is immensely satisfying."
            show lexi date annoyed
            lexi.say "...Aw shit..."
            mike.say "You're damn right 'aw shit'. Don't think I forgot what happened back there."
            if not game.flags.dannyvictory:
                lexi.say "Calm down, it wasn't nothin' personal."
                mike.say "Oh? Nothing personal? Well sure, maybe it wasn't. That would actually make sense."
                mike.say "What doesn't make sense to me though, is how you can possibly justify telling me to calm down."
                mike.say "Bear in mind that you left me beaten and without any money. It wasn't a good time having to cancel all my cards."
            else:
                if not game.flags.dannyvictory > 1:
                    mike.say "Luckily I managed to stop things from going any further, but it was hardly a lot of fun."
                "Lexi leans back a bit and sighs."
                lexi.say "Yeah well...Danny knew to back off then."
                mike.say "I'm sure he did, wise choice."
                "It's nice to actually feel like an alpha here."
                if not game.flags.dannyvictory > 1:
                    mike.say "What's really funny is that you still tried to call to me after doing that."
                    mike.say "Did you think I was going to forgive you?"
            show lexi date
            lexi.say "Look, I know you must be pissed off about what happened, but we all gotta make a living don't we?"
            mike.say "Or you could, you know, get a job."
            lexi.say "I have a job."
            mike.say "And what's that, dealing drugs?"
            "She quickly huddles over the table and glares at me, hissing through her teeth. I can see her tongue piercing glinting between them."
            show lexi date annoyed
            lexi.say "Are you insane!? What the hell are you tryin' to do here!?"
            mike.say "Rat you out, maybe? I think it would be well deserved, considering the hell you've already put me through."
            lexi.say "Okay okay, look!"
            hide lexi
            show lexi date close sad
            "She leans closer, seemingly not caring that her boobs are practically popping out of that crop top."
            lexi.say "It's either this, or the mugging. I don't have a lot of options here, and less people will get hurt this way right?"
            mike.say "In the short term maybe..."
            lexi.say "Exactly. So cut me some slack."
            "I take my time, rapping my fingers against the table-top and observing her anxious face."
            "It feels nice to be holding all the cards here. She may have had the upper hand back in the alleyway, but right now I'm the one with the advantage."
            lexi.say "Will you? Will you please let me off just this once?"
            mike.say "...Why should I? What's in it for me?"
            "She hesitates, and the corners of my lips curl upwards smugly."
            mike.say "Well? Please, I'm dying to know what my prize will be for all the effort."
            show lexi normal
            lexi.say "That's...alright fine, I'll blow you."
            "Now it's my turn to be startled. I just about fall out of my seat when she so casually suggests it."
            mike.say "...I'm sorry...what?"
            lexi.say "You heard me. Let's go to the bathroom and I'll suck you off, no problem."
            mike.say "Um..."
            "I'm left speechless. I don't quite know what to say to that."
            "I could accept it but...what if she tries to take advantage of me again?"
            "I'd rather that she didn't steal anything from me, for example."
            "But I guess, if I keep my wits around me I might be fine."
            "All I really want is to get something back for what happened to me before."
            "Honestly...I feel like I definitely deserve it..."
            lexi.say "Well? You up for it?"
            menu:
                "Yes":
                    mike.say "...Fine. Fine, let's go."
                    "I stand up along with her. She takes my hand firmly, and just like that I'm being tugged along with her."
                "No":
                    show lexi annoyed
                    mike.say "Fuck off!"
                    "Disgusted I leave her here..."
                    $ lexi.set_gone_forever()
                    return
        "Tell someone else.":
            "Actually, approaching her straight up seems like a completely dumb idea."
            "I don't know what Lexi herself is capable of, and if Danny comes out of the woodwork again, I'm totally screwed."
            "It's far better for me to play it safe and let one of the staff members know."
            "Yes, it's the lamer of the two options, but I'd rather do this than end up getting attacked again."
            hide lexi with dissolve
            "I scan the entrance to the nightclub for someone who seems good to notify."
            "There's a pretty big looking bouncer there. I don't think that even someone like big boy Danny would mess with him."
            "So, I walk over with a confident stride, fully committed then. If I end up having to pay some sort of consequence then so be it."
            "All I want to ensure is that Lexi doesn't get to fuck me up and then walk away without any kind of punishment."
            show dwayne at right4, blacker with dissolve
            mike.say "Excuse me sir-"
            show fx exclamation at top_mostleft
            "Girl" "Oh! Sorry, sorry!"
            "I'm about to talk to the bouncer, he's already half-turned to hear what I have to say, but I suddenly hear a girl calling out."
            hide fx
            show fx exclamation at top_mostleft
            "Girl" "Don't mind him, haha!"
            "Bouncer" "Uh...can I help either of you?"
            hide fx
            show lexi date happy at left with moveinleft
            with hpunch
            hide lexi
            show lexi date happy at center, zoomAt(1.65, (400, 1140)) with hpunch
            "An arm links around my own, and I look down to see none other than Lexi, clinging to me like some sort of drugged up koala."
            "She smiles up at me in a sickly sweet manner, and for once I'm more focused on her face than her chest."
            "So...this is a part of her plan then?"
            "I figure it out in my head, what seems probably at least. She must have seen me from the back and come rushing over to stop me from saying anything."
            "Guess she was a step ahead of me after all."
            mike.say "Hello...Lexi..."
            lexi.say "Hello babe, I'm so glad you could come!"
            "She grins at me, and I let out a heavy sigh. I don't know what's more insulting. The fact that she's pretending to be my girlfriend?"
            "Or the fact that I'm just letting this happen..."
            "Bouncer" "Look, I got work to do, so can you say what you were gonna say or leave?"
            "I pause, feeling her squeezing my arm all the more."
            "I guess that's my warning."
            mike.say "Um...no it's...it's nothing. Sorry, sorry to bother you."
            "Bouncer" "Whatever."
            hide dwayne
            show lexi date happy at center, zoomAt(1.65, (640, 1140))
            with fade
            "I back up along with Lexi, and we keep walking away until we're in a quiet corner of the nightclub where nobody can really see us."
            hide lexi
            show lexi date angry at center, hshake
            "Only then does she let go of me and plant her hands firmly on her hips instead. The look in her eyes is deadly..."
            lexi.say "What the HELL?"
            mike.say "I guess you figured me out. Just like I figured you out."
            lexi.say "Oh fuck off...you got no business bothering me!"
            mike.say "Kind of like how you had no business bothering me the other night?"
            "It feels good to actually say it to her. Call her out on it."
            if not game.flags.dannyvictory:
                mike.say "Remember how I got beaten up by your boyfriend and left there without any money?"
                mike.say "Bet you would have stolen my clothes too if they were worth anything."
                show lexi date annoyed
                "She sighs and looks down, tapping her foot."
                lexi.say "Don't be so annoyed. We all do things our own way, and that's my way of doing things."
                mike.say "Right."
                "Well she sure goes about things in a bad sort of way then."
                lexi.say "Besides, you tried to kick him in the dick. Do you really think he was gonna let it slide?"
                mike.say "Screw me for using self defense right?"
                show lexi date sad
                lexi.say "...You should've just let us take your money, and you wouldn't have ended up getting hurt."
                "Right. That's a fair argument."
                mike.say "But then I would have never caught you dealing drugs, would I, Lexi?"
            else:
                mike.say "It's a miracle I actually managed to get out of that mess."
                lexi.say "Oh yeah. Gotta thank you for kicking my boyfriend's butt."
                "She scowls bitterly. I only tut."
                mike.say "I had good reason for doing it. He was threatening to kill me!"
                lexi.say "Yeah but he wouldn't have! Hell, who do you think we are?"
                "I stare at her blankly."
                mike.say "Scum."
                show lexi date angry
                "Never mind Danny, she looks fit to murder me for saying that."
                lexi.say "You better stop running your mouth!"
                mike.say "And you'd better stop selling drugs to people."
                lexi.say "-!"
            show lexi date annoyed
            "She shuts her mouth. Whatever she was planning on saying next, she seems to have abandoned the idea."
            "It's nice to see her being quiet like this."
            "These are certainly interesting circumstances. I can see quite clearly, she's very uneasy."
            "The other night, I was the one who was at a horrible disadvantage. Yet now, things have completely switched around, and I couldn't be happier about it."
            mike.say "That's right. Think carefully about your next move, because I'm not afraid to tell someone about this."
            show lexi date normal
            lexi.say "Alright! Alright alright, let's just...let's just take this slow..."
            mike.say "Take it slow? Why bother?"
            mike.say "I can just finish exactly what I already started before and tell that bouncer what I intended."
            "I can see hints of anger flickering in her eyes, but she seems to be urging herself internally to stay calm too."
            show lexi date annoyed
            "I guess it's only in her own better interest if she keeps her cool."
            lexi.say "...You'll ruin me. I don't have a lot of choices, come on!"
            mike.say "What do you mean by that?"
            show lexi date sad
            lexi.say "I mean...well...I mean look at me..."
            show lexi date b
            "Eyeing me, she runs her hands from her chest to her incredibly short skirt, showing off and amplifying her body all the more."
            lexi.say "In a meeting they'd take one look at me and kick me out on my ass."
            lexi.say "Even if I wanted to apply for a job there's no way I would ever get it."
            "Admittedly, I can sort of see her point there. Though I suppose it would depend."
            show lexi date
            lexi.say "But when it comes to my body, it's something I can use to lure in suckers like you and make a quick buck with Danny's help."
            mike.say "Right. Yeah, I'm well aware of that now."
            "Even if I was partially drunk back then, I still feel like I was such an idiot for falling for it."
            lexi.say "Besides that...if I don't want to trick other people, I have to do something like this. Stay under the radar."
            mike.say "If you're trying to make me feel bad for you..."
            show lexi date a annoyed
            lexi.say "I'm not! But don't you get it? It's just how I gotta do things."
            "How she has to do things?"
            "If she didn't dress up like a slut, literally, she might be able to land herself a decent job."
            "I know what a girl wears shouldn't matter but...I don't know if I can imagine seeing Lexi in an office cubicle."
            "I feel like she'd go insane in a place like that anyway."
            mike.say "Are you really that desperate to keep this hidden?"
            lexi.say "Of course I am! If I don't, I'll end up in jail."
            "Now there's a place that I could see her fitting in."
            lexi.say "Please...please, I'll give you something in return if you can keep this private."
            "I perk up a little bit when she suggests that."
            mike.say "And when you say 'something'...you mean...what exactly?"
            show lexi date normal
            "A sultry look immediately bleeds into her gaze."
            lexi.say "How about I blow you in the toilets here? You'll love it, trust me. I am that good."
            "Hearing her say 'trust me' is ridiculous, but I find myself drawn in by the proposal anyway..."
            menu:
                "Yes":
                    "Just like that, I'm nodding my head. Agreeing."
                    "Maybe I actually do want this."
                "No":
                    show lexi annoyed
                    mike.say "Fuck off!"
                    "Disgusted I leave her here..."
                    $ lexi.set_gone_forever()
                    return
    scene bg restroom with fade
    "We sneak off toward one of the bathrooms, and she immediately pulls me into the cubicle at the far end of the room."
    "It's not very classy, but at least it's pretty clean. Small mercy, I guess."
    show lexi date with dissolve
    lexi.say "Ok, now promise me before we start anything. I need you to make a deal with me."
    "Hesitating, I watch her uneasily until she speaks again."
    lexi.say "You won't tell anyone, alright? Not a single person, or I swear I'll be pissed!"
    "I blink a few times, before simply nodding to her."
    mike.say "Okay, fine, no problem."
    "It kind of is a lot to ask but...well I suppose I am getting something in return for my silence."
    show lexi date close
    lexi.say "Shake on it then."
    "She holds out her hand, and so I take it. It's the first time we've touched each other properly."
    "Admittedly, it's pretty nice. But we're not here for this kind of thing."
    show lexi bj date with fade
    "As soon as I finish shaking and pull my hand back, she gets down on her knees and reaches up for my belt."
    "Her fingers deftly work my belt loose, and soon she has my dick out of my boxers."
    "I lean back against the cubicle wall and hitch my breath, as if I'm bracing myself."
    "I'm looking forward to it but I'm also a little scared."
    "Maybe just because this is a first...and she did pretty much screw me over before..."
    show lexi bj suck
    show mouth_insert lexi zorder 1 at zoomAt(1, (820, 200))
    "Yet the very moment her lips slip around the tip of my dick, I start to feel a twinge of pleasure."
    "It's very pleasurable. Already I can feel myself starting to get into it, and things have only just kicked off."
    lexi.say "Mm..."
    "She lets out a moan, and I groan too, craning my head back and closing my eyes."
    show lexi bj deepthroat open
    "Her mouth slips further up towards the base of my dick, and I'm honestly quite surprised by how far she's able to take it in."
    "I'm glad for it though."
    mike.say "Fuck..."
    show lexi bj suck closed
    "I can't help saying it. She sucks me harder still."
    "It feels crazy good. My legs quiver and I bite my lip as she starts to quicken her pace."
    "Lexi blows me faster and faster, until finally she parts from my dick just in time for me to cum."
    menu:
        "Mess her face up":
            hide mouth_insert
            show lexi bj smile cum left -suck
            with vpunch
            "On a whim I grab her hair and prevent her from catching my jeez with her mouth, covering her face with it."
            with vpunch
            lexi.say "Hey!!!!"
            show lexi bj facial left -cum with vpunch
            lexi.say "Fuck you messed up my make up moron!"
            mike.say "Serves you right."
            show lexi bj facial -left
            "For a moment we both stare at each other, but since I'm so weary it doesn't feel awkward."
            "Lexi stands up then and wipes her face with the back of her hand."
            hide lexi
            show lexi date cum close
            with fade
        "Let her do her thing":
            show lexi bj open cum
            show mouth_insert lexi cum zorder 1 at zoomAt(1, (820, 200))
            with vpunch
            "Deftly, she catches it all on her tongue..."
            show lexi bj normal showcum nodick -cum with vpunch
            "Then as if bragging she shows me her mouth full of my jizz..."
            show lexi bj swallow with vpunch
            "...and swallows the lot..."
            hide mouth_insert
            show lexi bj smile
            mike.say "Fuck, that's the sluttiest thing a girl has ever done to me."
            lexi.say "Thanks."
            "For a moment we both stare at each other, but since I'm so weary it doesn't feel awkward."
            "Lexi stands up then and wipes her mouth with the back of her hand."
            hide lexi
            show lexi date
        "Pull her deeper":
            show lexi bj left right
            "I decide to go all the way and grab her hair."
            show lexi bj deepthroat closed with vpunch
            "I pull her face down on a forced deepthroat..."
            show lexi bj cum
            show mouth_insert lexi cum zorder 1 at zoomAt(1, (820, 200))
            with vpunch
            "And blow my load deep in her mouth."
            show lexi bj open with vpunch
            "She looks up at me with teary eyes."
            show lexi bj smile -deepthroat -cum -left
            "For a moment we both stare at each other, but since I'm so weary it doesn't feel awkward."
            "Lexi stands up then and wipes her mouth with the back of her hand."
            hide mouth_insert
            hide lexi
            show lexi date
            with fade
    lexi.say "So, we done?"
    "I take a moment to dab my own brow with my shirt sleeve, before nodding and pulling up my pants again."
    mike.say "Seems like it."
    show lexi happy
    lexi.say "Great! Well then, glad that's sorted."
    "Admittedly, I feel a series of emotions, all mixed together."
    "On the one hand, it felt damn good, and I can't deny that. She clearly knows exactly what she's doing."
    "On the other...it almost feels like I'm still letting her off the hook too easily."
    "But after we shook on it, I'd feel like a douche to go back on that promise."
    mike.say "Yeah, fine."
    show lexi normal
    lexi.say "Hey now, cheer up honey. I gave you what you wanted."
    mike.say "Yeah, true."
    show lexi happy
    "She grins at me, seemingly unfazed. It was definitely too easy for her."
    lexi.say "Yep. There's your night to remember."
    hide lexi with dissolve
    $ lexi.flags.walletamount = min(hero.money.val, 500)
    $ hero.money -= lexi.flags.walletamount
    "She leaves me there, and I let out a sigh."
    "Like instinct, my hand goes for my pocket. And as I suspect...she took it."
    "My wallet."
    mike.say "...Dammit."
    return

label lexi_event_02:
    play sound cell_vibrate loop
    "Somehow, when I see the 'Unknown' number flashing up as my phone buzzes, I already know who it's going to be."
    "Lexi. Without a doubt."
    stop sound
    $ result = renpy.call_screen("smartphone_choice")
    if not result:
        $ hero.cancel_event()
        return
    $ lexi.unhide()
    $ lexi.flags.nodate = False
    $ lexi.flags.nokiss = False
    if lexi.love.max < 100:
        $ lexi.love.max = 100
    $ lexi.sexperience += 1
    $ hero.smartphone_contacts.append("lexi")
    "Turns out, I'm right."
    mike.say "You've got some nerve calling me after stealing my shit."
    lexi.say "Oh boohoo, at least I bothered, right?"
    mike.say "Yeah, and right now I'm bothering to cancel my credit cards-"
    "I glance back at the laptop screen, tapping away on the keyboard with one hand."
    mike.say "-So have fun with that."
    lexi.say "Look, whether you cancel them or not doesn't matter. I never used 'em."
    mike.say "..."
    "I'm prompted to pause when she says that. It doesn't make sense, why bother stealing my wallet if she isn't going to try and run my bank balance dry?"
    mike.say "...What's the matter, too scared of getting caught?"
    lexi.say "I'm not scared of anything! I just...I decided against it."
    mike.say "Oh how noble. A sudden change of heart."
    lexi.say "I ain't a bad person."
    mike.say "Uh huh. Yeah, just a slutty drug deale-"
    lexi.say "HEY."
    "I can tell by her tone that she's suddenly dead serious. It actually makes me flinch a bit."
    mike.say "...What??"
    lexi.say "Don't. Call. Me. A. Slut."
    mike.say "Fine, fine."
    lexi.say "And we put the drug business behind us when I sucked you off too."
    mike.say "Well, that was before you stole my wallet."
    lexi.say "So what, you holdin' a grudge now?"
    "I roll my eyes and sigh down the phone from my end."
    mike.say "Yeah, and rightfully so, wouldn't you say?"
    lexi.say "..."
    "There's a long pause from her side."
    "I guess I stumped her with that one."
    lexi.say "...Can you at least...let me come over?"
    mike.say "Excuse me?"
    lexi.say "I mean I know where your address is now. It's written in your wallet."
    "Fuck!"
    "I guess she knows too much about me now. Dammit..."
    mike.say "Why would I...let you come to my house?"
    lexi.say "Well...so I can give your wallet back."
    mike.say "The hell? Are you serious?"
    "She can't be..."
    lexi.say "I am. And you can't say no to me."
    mike.say "...And why is that?"
    lexi.say "Hah! Cuz I'm already there!"
    "At first I don't understand. Then I put two and two together."
    mike.say "...You're joking, right?"
    lexi.say "Cul de sac for rich people...stupid comedy doormat that says 'LEAVE'? Ring a bell, asshole?"
    "It does."
    lexi.say "Look out your damn window."
    mike.say "Charming. Alright-"
    "I go to do just that, I look through the windows to see her on the street."
    "A top that might as well be a bra, ridiculously short shorts, and a thong poking out on either hip."
    "Yeah. It's definitely Lexi."
    "She seems to notice me, and waves using the phone, giving me a shit-eating grin."
    "Well. Great."
    mike.say "...I'll be right here."
    show bg house
    show lexi casual
    with wiperight
    "Bitterly, I go to the front door and let her in."
    show bg kitchen with fade
    "Once she does, I lead her inside to my kitchen area, scowling all the way."
    "After we reach my kitchen I lean against the island and mentally prepare myself."
    "Just in case she starts arguing with me again..."
    show lexi surprised
    lexi.say "Ooh, so you're rich enough to afford a house? Maybe I should have taken your cards after all..."
    mike.say "Ahem."
    "I catch her attention with a cough and hold my hand out expectantly."
    mike.say "Hand it over."
    show lexi normal
    lexi.say "Hah. Fine, relax-"
    "She actually does it, and I take my wallet back with some relief."
    "Good. At least that's a weight off my shoulders. Big time."
    "I check inside to make sure, and then look back at her."
    $ hero.money += lexi.flags.walletamount
    mike.say "Looks like everything's there."
    lexi.say "Would I lie to you?"
    mike.say "Yes. 100%%, yes."
    lexi.say "Well, you got it back anyway. And...that should mean there are no hard feelings between us now?"
    "I let out a heavy sigh, tempted to yell at her."
    "Is she just delusional? Why does she assume that everything is suddenly going to be alright?"
    mike.say "...Do you have some other reason for coming here?"
    show lexi casual sad
    "I'm just about ready to smack my forehead off the edge of the counter, but her honest look catches me off guard."
    "She actually looks kind of...sad? Just for a moment, but I notice it."
    show lexi normal
    lexi.say "Well I...wanted to explain a few things. Y'know, like I don't really mean to do that kind of shit, I just have to."
    mike.say "And by 'shit' I'm guessing you mean the whole robbing people thing?"
    lexi.say "And the drugs too..."
    mike.say "I thought we weren't going to talk about those."
    show lexi annoyed
    lexi.say "And we ain't! But..."
    "Her momentary defensiveness fades away again, and she seems to shrink even further."
    mike.say "...Just sit down. Want something to drink?"
    show lexi normal
    lexi.say "Yeah, got anything strong?"
    "As soon as I suggest it she immediately sits down like she owns the place, and I wonder if I've made some sort of grave mistake."
    "Well...no turning back now, I guess."
    mike.say "Let me check."
    "Soon enough I pour us both some wine, and she laughs, picking up her glass and examining it."
    show lexi casual surprised
    lexi.say "Wow. You really are a posh boy."
    mike.say "Why? Because I have a nice house I worked for, and I drink wine?"
    "Screw me for trying to be a good host."
    show lexi normal
    lexi.say "Ugh, it's whatever."
    lexi.say "Anyway...how'd you afford a life like this?"
    mike.say "I mean...I worked for it, just like anyone else."
    mike.say "Except you, I guess. You love your shortcuts, right?"
    show lexi casual sad
    "She grimaces."
    lexi.say "Told ya, I got no choice in it. So..."
    "Again, she goes quiet and just focuses on drinking for a moment."
    "I figure I'm as well doing the same, and the atmosphere becomes pretty awkward between the two of us."
    lexi.say "...It's...just that I have no choice."
    mike.say "Humans have free will, don't we? So how can you not decide for yourself?"
    hide lexi
    show lexi casual angry at center, zoomAt(1.65, (640, 1140)), hshake
    show fx exclamation
    lexi.say "Because!"
    "She suddenly snaps her head towards me."
    hide fx
    lexi.say "I owe somebody a debt, so it isn't that simple!"
    mike.say "Who?"
    lexi.say "...Remember that big guy who nearly killed you in the alley? Danny? My boyfriend?"
    "'Nearly killed' me, eh? Well...at least she's acknowledging it now."
    mike.say "Yeah, kinda hard to forget someone like him."
    show lexi casual sad -close
    lexi.say "Well, he's a gangsta. I owe him a debt too, his whole gang really, so I gotta...obey him otherwise..."
    "Judging by the way she trails off then, I decide not to press for details. But I do need to know a bit more about this."
    mike.say "Right...and that's why you're doing all of this?"
    lexi.say "...Basically. I mean, I'm just fucking tired of it."
    "She downs the rest of her wine in one go and slams the glass down. I wince."
    mike.say "It's not a shot Lexi. Anyway, I'm sorry you're in that position but..."
    mike.say "...It doesn't change what you've already done."
    lexi.say "Yeah, I get it, I suck. Relax."
    "I mean if she's referring to what happened in the bathroom..."
    lexi.say "At least now you know why I'm doing these things."
    mike.say "..."
    "Taking a moment to pause and think it all over, I can't bring myself to actually get mad at her."
    "I guess...maybe I feel kind of bad for her? It's easy to just blame her for all of this but...she had her reasons I guess."
    mike.say "Okay...fine."
    "She looks up at me hopefully, and I give in entirely."
    mike.say "We can let bygones be bygones and...move on from this."
    show lexi casual happy
    lexi.say "Really!?"
    "Lexi perks up in an instant."
    mike.say "Yeah really. Just...don't pull anything like that again, please."
    show lexi normal
    lexi.say "Deal. Thanks for listening to me."
    "I'm surprised by just how nice and open she's being."
    "Of course, it could turn out to all be deception but...I can't help but trust her."
    "Plus when she's not being so bitchy she actually looks really quite attractive."
    show lexi casual surprised
    show fx exclamation
    lexi.say "Hmm...hey, woah-!"
    "Something suddenly catches her eye as she turns to look out of the sliding glass doors."
    hide fx
    "I'm guessing she spotted the pool. The lights just turned on a few minutes ago."
    show lexi normal
    show fx exclamation
    lexi.say "You have a swimming pool!?"
    mike.say "Yeah uh...it came with the house. Might need to be cleaned, I haven't used it in a while."
    hide lexi with moveoutleft
    "That lie doesn't seem to phase her, she just rushes to the doors anyway and slides them open."
    "They bang and I cringe again. Doesn't she know how to treat other people's property?"
    mike.say "Lexi, hold up!"
    scene bg pool
    show lexi casual happy
    with fade
    "I hurry after her, and rush through the open door."
    "She's already standing at the edge of the pool, looking down into it eagerly."
    show lexi underwear nophone with dissolve
    "That and...she's pulling off some of her clothes."
    "She's not wearing many, so it won't take long before I have a naked chick hanging around in my garden."
    mike.say "Lexi could you just wait a minute!?"
    show lexi naked b blush with dissolve
    "Not listening to me, even still, she pulls off her bra and panties and dives into the water with only a little grace."
    hide lexi with dissolve
    play sound water_splash
    "I end up getting splashed a bit considering I bothered to run over and try to stop her."
    mike.say "..."
    show lexi naked nophone
    "Lexi turns in the water partially after surfacing again, and grins at me devilishly."
    "Before I can use my arms as a shield (or get a proper look at her body), she splashes some water right into my face."
    "I end up with a soaked shirt too, and I groan after wiping the droplets out of my eyes."
    mike.say "...Really?"
    show lexi happy
    lexi.say "Lighten up and join me! All the heavy shit is out of the way now, right?"
    "I guess so..."
    show lexi normal
    "And now that I can actually see her properly, it's hard not to notice."
    "The water distorts her figure a little bit below the torso, but I can still see her pretty clearly thanks to how still it is now."
    show lexi a close naked at top_to_bottom
    "Her body is...gorgeous. I can't deny it."
    "Her chest is ample, and it tapers nicely into a full set of hips as well. She's slender and curvy in all the right places."
    "I guess I could have anticipated this, considering the kind of clothes she wears don't typically hide anything. But..."
    show lexi a close naked wink at bottom_to_top
    "Seeing it in full...is really something."
    lexi.say "Hey, stick your tongue back in your mouth, perv."
    mike.say "Excuse me?"
    "She chuckles and swims to the edge of the pool, folding her arms and resting her chest against the edge."
    "I can see her breasts pressing up together, dripping with chlorinated water."
    "It's...inviting, frankly."
    show lexi blush
    lexi.say "Interested? Why don't you join me?"
    lexi.say "I mean, it's not like you have anything to worry about this time. You can't take your wallet in the pool."
    "True."
    "Well...maybe I should."
    "Or...should I?"
    menu:
        "Join her":
            "Going for an early night swim with a hot girl?"
            "I guess any sane person would say 'yes'."
            "So without really giving myself any more room for hesitation, I take off my clothes and slip into the water with her."
            "Yes...I'm completely nude."
            "And she just stares at me."
            "Stares and stares..."
            lexi.say "Wow...you actually did it."
            mike.say "Well...I figured it was better than just standing around awkwardly until you get out."
            mike.say "And dressed."
            lexi.say "Well I'm impressed. So..."
            $ hero_clothed = False
        "Go back inside":
            "...I'm not an idiot."
            "Lexi may have had the courtesy to bring my wallet back, but what she's doing right now just makes it seem like she's playing some kind of game with me."
            "So I'm not going to bite the bait."
            show lexi surprised
            lexi.say "Hey, aren't you gonna come in?"
            mike.say "Yeah, no thanks-"
            hide lexi with dissolve
            "I walk past the edge of the pool, aiming to head back inside and just drink the rest of that bottle."
            "I guess I don't account for just how close to her I am."
            "Her wet hand snakes out of the water and suddenly grasps my ankle, tugging it sharply and yanking me right over."
            with hpunch
            mike.say "GAH!"
            play sound water_splash
            with vpunch
            "She's lucky that I end up landing in the water."
            "Not smacking my head off the concrete."
            mike.say "Fuck! What the hell!?"
            show lexi naked nophone b at center, zoomAt(1.65, (640, 1140)) with dissolve
            "I snap at her as soon as I'm above water again, and she looks over at me with a smug grin."
            lexi.say "Trust me, you're gonna wanna say yes to me tonight."
            "Before I can say a word in response, she comes closer."
            $ hero_clothed = True
    show lexi naked
    "Lexi doesn't waste time. I feel like I'm in the nightclub toilets again as she presses up against my front."
    "Those same tits are right up upon me now. Yes...they're great."
    "I'd be one stubborn idiot if I didn't admit that."
    "My hands drift down to her sides and grip them gently."
    "Under the water, her skin feels even warmer."
    "I guess it is pretty fancy...having a heated pool."
    show lexi blush
    lexi.say "Heh..."
    "Her own hands start to feel my body, tracing down what seems like every single inch of my skin."
    "Soon enough, they seal around several other inches too, and start to rub away even in the water."
    "I lean back and close my eyes, resting both elbows against the side of the pool."
    "I figure she's not going to suck me off underwater, so this is definitely going to be different from before."
    "But...am I really ready for things to go further?"
    "Well...I guess...there's no turning back now."
    show lexi wink
    lexi.say "Look at you...you're already getting hard."
    show lexi b
    "She grins up at me, before I can feel her hand slip away."
    "Lexi rests against the other side just by me, and shows off her figure for me."
    "I can see her standing with her legs spread a little, like she's just waiting for me to lift them and pull her close."
    "Yep...definitely no turning back now."
    mike.say "..."
    "I wade the few steps it takes to reach her, and reach under the water's surface again, my hands slipping to her ass cheeks and giving both of them a firm squeeze."
    "Using my reasonable strength, I hoist her up and spread her legs a little more."
    hide lexi
    if persistent.xray:
        show lexi stand pool vaginal xray with fade
    else:
        show lexi stand pool with fade
    if hero_clothed:
        "Partially submerged I managed to remove my clothes before pushing my dick up inside of her waiting pussy."
    else:
        "Partially submerged along with her, I push my dick up inside of her waiting pussy."
    lexi.say "Haa-!"
    "Immediately she yelps. I'm already rigid."
    "That only serves as a cue to make me shove in further and firmer."
    "I can tell by her reaction that she loves it."
    "I push in even more, and start to slip in and out of her steadily."
    "Just like that, we're gyrating and moving in tandem with one another, the warm water splashing and shifting around our naked bodies."
    "It's times like this that I'm grateful for having such a private garden."
    lexi.say "Ha...harder!"
    mike.say "Nn-"
    "I grunt and obey, picking up the pace, not holding back."
    "Her body starts to become more and more heated, her walls closing in around my length."
    "I close my eyes just like I did when she jacked me off earlier."
    show lexi stand pool ahegao
    "Things grow more and more intense."
    menu:
        "Cum inside":
            show lexi stand pool ahegao with hpunch
            "Eventually, it seems that both of us hit our respective peaks, and with one final shudder, I orgasm inside of her."
            with hpunch
            "It seems like my hot load triggers a burst of pleasure for her too, and she gasps sharply."
            with hpunch
            lexi.say "Ahh~!"
            "That's the ticket. I can feel her cum mingling in the water with my own, as I pull out and calm down."
        "Pull out":
            show lexi stand pool ahegao
            "I struggle to pull my cock out in the moments before I actually cum."
            lexi.say "Ahh~!"
            show lexi stand pool ahegao -vaginal with hpunch
            lexi.say "Y...you pulled out too quick-"
            with hpunch
            mike.say "My bad."
    "Honestly, I don't think I've ever been with a woman like this."
    "It's like it was too much. I hit my peak so quickly, and I've never been like that before."
    "Maybe it's just that...this was so unexpected."
    "Actually fucking a girl like Lexi, in this setting too."
    "...How could I have anticipated this?"
    "Actually...how could I have anticipated any of this?"
    scene bg pool at blur(16), dark with dissolve
    "Even after she leaves, looking smugly proud of myself, I get this strange feeling."
    "Like I don't want her to go."
    scene bg black with dissolve
    pause 1
    return

label lexi_event_02b:
    play sound cell_vibrate loop
    "I'm elbowing my way through the crowds of shoppers that are filling up the mall when I feel my phone vibrating."
    "As if I didn't already have enough trouble trying to get my shopping done before the festive season comes around!"
    "I struggle to pull my phone out and step away from the living river of human bodies to answer it."
    "The caller ID comes up as an unknown number, but even as I answer it, I have a funny feeling as to who this could be."
    stop sound
    $ result = renpy.call_screen("smartphone_choice")
    if not result:
        $ hero.cancel_event()
        return
    $ lexi.unhide()
    $ lexi.flags.nodate = False
    $ lexi.flags.nokiss = False
    if lexi.love.max < 100:
        $ lexi.love.max = 100
    $ hero.smartphone_contacts.append("lexi")
    mike.say "Lexi?!?"
    mike.say "That'd better not be you!"
    "I hear a filthy snort of laughter on the other end of the line."
    "And that's enough to confirm my suspicions, even before she speaks a word."
    lexi.say "And what if it is, huh?"
    lexi.say "What are you gonna do about it?"
    "I realise that a couple of passing shoppers are glancing in my direction."
    "I must have been shouting down the phone in my righteous anger at Lexi."
    "So I turn my back on them and make a titanic effort to suppress my rage."
    mike.say "You've got a lot of nerve calling me, Lexi!"
    mike.say "After what you did to me - I should call the police!"
    lexi.say "Blah, blah, blah!"
    lexi.say "Waa, waa, waa!"
    lexi.say "You're wasting your time with those limp-dicks."
    lexi.say "They won't do nothing for you!"
    "I wince at Lexi's mocking tone."
    "That and the fact her last proclamation was an oxymoron."
    mike.say "Look, are you just calling me to gloat, or what?!?"
    mike.say "Because I'm busy doing the things normal, non-criminal people do!"
    mike.say "I already wasted hours of my life cancelling my credit cards thanks to you!"
    lexi.say "Hey!"
    lexi.say "I never used your damn credit cards!"
    "I don't know why, but that last statement really gets under my skin."
    "It's like Lexi thinks I'm actually stupid enough to believe that."
    mike.say "Yeah, Lexi, sure you didn't!"
    mike.say "You stole my wallet and everything in it."
    mike.say "But you'd never dream of actually using my stuff!"
    mike.say "What kind of a moron do you take me for?!?"
    "Lexi pauses, and it's a few seconds before she speaks again."
    "And when she does, I can hear a change in her voice."
    "It's subtle, but it sounds like she's less cocky and more vulnerable."
    lexi.say "I...I'm not lying, okay?"
    lexi.say "I don't know why I didn't use them..."
    lexi.say "It didn't feel right...that's all I know!"
    lexi.say "Look, can we meet up?"
    lexi.say "You know, talk to each other in person?"
    mike.say "What good would that do?"
    lexi.say "I dunno...I just want to do it, that's all!"
    mike.say "You want to make a gesture, Lexi - is that it?"
    lexi.say "Yeah, yeah...I'm not good with words like you are!"
    lexi.say "Maybe I could come to your place?"
    lexi.say "I found your address in your wallet..."
    "No way that's going to happen!"
    "For all I know, she could be planning to steal everything I own!"
    mike.say "No..."
    mike.say "We should make it somewhere neutral..."
    mike.say "I'm at the mall right now - can you make it down here?"
    lexi.say "Sure thing - I'll be there before you know it!"
    scene bg mall1
    "As soon Lexi ends the call, I can't help glancing around."
    "She's got me so jumpy it's like I expect her to appear out of nowhere."
    "But in reality it takes her a little while to show up."
    "I make my way to the entrance of the mall, so I see her when she walks in."
    scene bg black with timelaps
    scene bg mall1
    show lexi happy
    with timelaps
    lexi.say "There you are!"
    mike.say "Yeah, Lexi, I'm right here."
    mike.say "And you have something for me, right?"
    show lexi annoyed
    "Lexi rolls her eyes in disbelief."
    "But she pull out my wallet and hands it over all the same."
    lexi.say "Geez, you've got a one-track mind!"
    "I don't respond, as I'm too busy checking the contents of my wallet."
    lexi.say "It's all there, I promise."
    "I nod as I discover that she's telling the truth."
    $ hero.money += lexi.flags.walletamount
    mike.say "It is, Lexi."
    mike.say "Thank you for being honest with me."
    show lexi happy
    "As I say this, the strangest change seems to come over Lexi."
    "Where before she was surly and rude, she softens and smiles at me."
    "And that makes me aware of the fact that she's really very pretty."
    "I mean, under all of the make-up and the slutty clothes she wears!"
    mike.say "What's the matter, Lexi?"
    mike.say "Was it something I said?"
    show lexi normal
    lexi.say "No...I mean yes..."
    lexi.say "I just...I kinda like it when you're nice to me!"
    show lexi sad
    "Suddenly her expression changes again."
    "And this time she looks sad."
    lexi.say "I'm not used to guys being nice to me..."
    "I know that I should be wary of Lexi, that this could all be a trick."
    "But somehow I can't resist the urge to reach out to her, to comfort her."
    "Maybe I'm just a sucker for a pretty face and a sob story."
    mike.say "I...I was just doing some Christmas shopping."
    mike.say "Would you like to hang around and keep me company?"
    mike.say "We could chat some more...unless you have somewhere else to be?"
    show lexi happy
    "Again Lexi's mood seems to change in an instant."
    show lexi at center, zoomAt(1.65, (640, 1140))
    "She wraps her arm in mine and leans against me."
    lexi.say "Sure thing, [hero.name]!"
    show lexi wink
    lexi.say "If anyone asks, I can pretend to be your fancy girlfriend!"
    "I can't help chuckling at the idea of Lexi pretending to be 'fancy'."
    "But I also feel a thrill of excitement as she clings onto me."
    "Part of me likes the fact that she's from the wrong side of the tracks."
    "She's trashy and cheap, but also exciting and downright sexy too."
    scene bg mall2
    show lexi at center, zoomAt(1.65, (640, 1140))
    with fade
    "We talk about nothing in particular at first."
    "But then we stop in front of a store that has a window full of biker jackets."
    "And that seems to set us both off thinking about what happened last time we met."
    mike.say "Lexi..."
    mike.say "Who was that biker guy you were with?"
    lexi.say "Oh...him..."
    lexi.say "That's Danny, my..."
    show fx drop
    show lexi sad
    lexi.say "Well, I dunno what he is exactly."
    lexi.say "Sometimes he acts like he's my boyfriend."
    show fx anger
    show lexi angry
    lexi.say "Other times he acts like he's my damn pimp!"
    show lexi annoyed
    mike.say "He doesn't sound like a nice guy."
    mike.say "So why do you stay with him?"
    show lexi sad
    "Lexi sighs, as if what she has to say weighs heavily on her."
    "But she says it anyway, like she needs to get it off her chest."
    lexi.say "I owe him and his buddies."
    lexi.say "So I got to work off my debt."
    lexi.say "And Danny likes me to work guys like you..."
    "And just like that I feel the entire situation shift beneath me."
    "Before I was mad at Lexi for tricking me and stealing my wallet."
    "But now I'm beginning to feel like a complete jerk."
    "Because it turns out she's a victim in all of this too."
    "A victim that's probably suffered a lot worse than I have."
    mike.say "It's not my business, Lexi, I know that."
    mike.say "And I'm not telling you what to do."
    mike.say "But couldn't you go to the police or something?"
    lexi.say "Nah, no use doing that."
    lexi.say "They'd just bang me up for what I done."
    lexi.say "And Danny'd still be waiting for me when I got out."
    "I can hear the helplessness in Lexi's voice."
    "And I don't have a simple solution to the Danny problem."
    "So I just let the subject drop."
    show lexi normal
    "Luckily it doesn't take long for Lexi to cheer up again."
    "She seems determined to make the most of her time away from Danny."
    "And so she throws herself into enjoying her time with me."
    "All too soon I'm done with my shopping and ready to head home."
    scene bg mall1
    show lexi at center, zoomAt(1.65, (640, 1140))
    with fade
    "But on the way out of the mall, Lexi takes hold of my hand."
    "She starts pulling me towards the nearest restroom."
    mike.say "Lexi!"
    mike.say "What are you doing?!?"
    show lexi happy
    lexi.say "You were nice to me, so I'm gonna be nice to you!"
    lexi.say "No strings attached this time - I promise!"
    "Suddenly I connect the dots in my head, and I know what's going on."
    "Lexi's pulling me into the restroom for the same reason she did last time!"
    menu:
        "Follow her":
            "I shrug and let Lexi have her way."
            "After all, why the hell not?"
            "She does kind of owe me one for stealing my wallet."
            "After this, we can probably call it even."
            scene bg publicbathroom
            show lexi
            with fade
            "Lexi hustles me into one of the cubicles."
            "And then she wastes no time in unzipping my pants."
            "Next she pulls them down to my ankles and gets down on her knees."
            "There's no teasing or delicate foreplay involved here."
            show lexi bj casual nopants with fade
            "Lexi just gets straight down to business."
            "And I can't say that it's not working."
            "My cock's already good and hard before she even touches it."
            "When she actually gets hold of it, I swear it grows an extra inch!"
            "Lexi smiles up at me, adding a wink just for good measure."
            show lexi bj suck
            show mouth_insert lexi zorder 1 at zoomAt(1, (820, 200))
            "And then she wraps her lips around the head."
            "Her technique is simple too, no pause or hesitation."
            "She just starts licking and sucking with gusto."
            show lexi bj deepthroat closed
            "It works too, making me gasp for breath as soon as she starts."
            "In fact, I soon have to brace myself against the walls of the cubicle!"
            "I've never had oral like this before, stripped down to the essentials."
            "And yet it feels incredible, just Lexi using her mouth to pleasure me."
            show lexi bj open suck
            "Her head bobs up and down, back and forth."
            "All the time she's looking up at me."
            "There's a genuine hunger in her eyes too."
            show lexi bj deepthroat
            "At first I think she just love the feel of a cock in her mouth."
            "But then I see that her eyes aren't glazed over or looking through me."
            "Lexi's actually holding my eye, watching how I react to her attentions."
            show lexi bj suck
            "It's almost like she's trying to see if she's pleasing me enough."
            "Like my enjoyment is more important to her than getting the job done quickly."
            show lexi bj deepthroat
            "And it's not at all like the first time she gave me oral either."
            "That felt like a business transaction more than a sexual encounter."
            show lexi bj suck
            "This time, Lexi's being rougher and faster, yet somehow more honest too."
            "All in all, it makes me that much more excited."
            show lexi bj deepthroat cum closed
            show mouth_insert lexi cum
            with vpunch
            "Which is probably why I feel myself cumming a moment later!"
            with vpunch
            "Lexi's ready for this, and she handles it with ease."
            show lexi bj open
            "She swallows every last drop, like she doesn't want to waste it."
            show mouth_insert lexi -cum
            show lexi bj normal showcum nodick -cum
            "And she looks extremely pleased with herself once she's done."
            hide mouth_insert
            lexi.say "Mmm..."
            lexi.say "How did you like that?"
            mike.say "That was..."
            mike.say "That was...WOW..."
            mike.say "That was amazing, Lexi!"
            scene bg publicbathroom
            show lexi normal at center, zoomAt(1.65, (640, 1140))
            with fade
            "Lexi giggles and helps me pull up my pants."
            "Then she plants a kiss on my lips."
            lexi.say "If I were yours, I'd do that for you every day!"
            show lexi wink
            lexi.say "Every...single...day!"
            scene bg mall1
            show lexi at center, zoomAt(1.65, (640, 1140))
            with fade
            "Once I'm decent, we sneak out of the restroom."
            "I crack a smile, trying to show Lexi that I'm not mad at her anymore."
            "And she seems to pick up on that, giving me a weak smile in return."
            mike.say "For what it's worth, Lexi - I forgive you for taking my wallet."
            mike.say "And I had a great time with you today!"
            lexi.say "You did?"
            lexi.say "Well...we could hang out some more, yeah?"
            mike.say "Sure thing, Lexi."
            mike.say "You've got my number, so call me!"
        "Don't follow her":
            mike.say "Wait a minute, Lexi."
            mike.say "You don't have to do that!"
            show lexi annoyed
            "Lexi stops in her tracks, frowning at me like she doesn't understand."
            "I guess she's just not used to guys turning her down when she offers it to them."
            show lexi angry
            lexi.say "What the fuck, [hero.name]?"
            lexi.say "You were into it the last time!"
            "I shake my head, trying to explain myself."
            mike.say "That's not it, Lexi."
            mike.say "Look, I like you a lot, really I do."
            mike.say "But you don't have to suck my cock just because I was nice to you!"
            mike.say "It doesn't mean you owe me something in return."
            mike.say "Sometimes it's okay just to be grateful and say as much."
            show lexi annoyed
            "Lexi looks more than a little hurt at first."
            "But I can see that she's turning it over inside of her head."
            lexi.say "I...I guess I just kind of assumed..."
            show lexi sad
            lexi.say "Sorry..."
            lexi.say "I'm not used to people being kind to me."
            lexi.say "Not without wanting something."
            "I crack a smile, trying to show Lexi that I'm not mad at her."
            show lexi normal
            "And she seems to pick up on that, giving me a weak smile in return."
            mike.say "For what it's worth, Lexi - I forgive you for taking my wallet."
            mike.say "And I had a great time with you today!"
            show lexi surprised
            lexi.say "You did?"
            show lexi normal
            lexi.say "Well...we could hang out some more, yeah?"
            mike.say "Sure thing, Lexi."
            mike.say "You've got my number, so call me!"
    hide lexi with dissolve
    "I walk away leaving Lexi standing in the entrance to the mall."
    show lexi casual sad with dissolve
    "And when I look back, she's still there, watching me go."
    "In the short time I've known her, she's never looked like she does now."
    "Lexi looks thoughtful, like she's got a lot on her mind."
    $ game.room = "street"
    return

label lexi_event_03_hide:
    $ lexi.hide()
    $ lexi.flags.DannyDelay = TemporaryFlag(True, 7)
    return

label lexi_event_03_look:
    "It had been one of those weeks from hell at work, no room in my head for much else."
    "But as soon as I had a moment to come up for air, my sex-obsessed brain began to remind me of Lexi."
    "Well, specifically it began to remind me of her physical charms and what they did to me at close range."
    "Call me an old romantic, but I was suddenly far more interested in the figure of that pure trailer trash than the figures on a spreadsheet."
    "But when I picked up my phone and called her, there was no answer."
    "Each time the call just rang out and then went to voicemail, likewise there was no response to texts either."
    "That was weird, as from what I knew of Lexi, she always had her mobile glued to her hand."
    "Also if she wasn't either using her mouth to spout her opinions or wrap around someone's dick, she was usually chatting into her phone."
    "Maybe I should look for her..."
    $ lexi.flags.looking = True
    return

label look_for_lexi_park:
    "I look all over the park for any sign of Lexi, but nothing."
    $ lexi.flags.lookpark = True
    return

label look_for_lexi_mall:
    "I look all over the mall for any sign of Lexi, but nothing."
    $ lexi.flags.lookmall = True
    return

label look_for_lexi_alley:
    "I look all over the alley for any sign of Lexi, but nothing."
    $ lexi.flags.lookalley = True
    return

label look_for_lexi_club:
    "I look all over the nightclub for any sign of Lexi, but nothing."
    $ lexi.flags.lookclub = True
    return

label lexi_event_04:
    $ lexi.flags.looking = False
    "After spending some time trying to track down Lexi the 'old-fashioned' way, I decided to try a more modern approach."
    "Sly as she most certainly was, Lexi was not the most tech-savvy person."
    "And so it didn't take me long to track down the location of her phone using an app on my own."
    "Looking at the address which came up, I shook my head and laughed ruefully."
    "It couldn't have been more obvious unless it came with an ad for slutty girls with massive chests and Daisy Dukes available to rent by the hour."
    "It was supposed to be my lunch hour, but I thought what the hell."
    "I hopped into my car and drove over there within no more than a couple of minutes."
    show bg trailer with fade
    "The trailer park turned out to be pretty much what I expected."
    "Run-down trailers with sullen, surly-looking people seemed to stretch on as far as the eye could see."
    "I suddenly felt rather exposed as people in MAGA caps and wife-beaters eyed me suspiciously from their folding chairs."
    "I stopped the car outside a particularly dumpy-looking trailer as soon as I saw Lexi crouched atop the stairs leading to the open door."
    "She was smoking a cigarette and seemed to be trying as hard as she could not to look up at anyone passing by."
    mike.say "Lexi...hey, Lexi - what's up?"
    "Lexi seems to brighten unconsciously as she recognizes my voice, looking up before she can stop herself from doing so."
    show lexi casual b beat with dissolve
    "In the moment before she looks away sharply, I glimpse the purple of what look like bruises and the red of blood."
    mike.say "Shit - Lexi, what in the hell happened to you?"
    lexi.say "Nothing...nothing...I just, just fell down in the shower, that's all."
    "I feel instantly bad that my first thought is to doubt Lexi's sincerity because I don't believe her trailer actually has a shower."
    mike.say "No...no, you didn't - because if you did, you'd be laughing it off, saying that you were drunk or high, or something."
    show lexi casual a beat close
    "Lexi finally looks up at me, showing the cuts and bruises for the first time."
    mike.say "Danny did this to you, didn't he?"
    "The fact that she doesn't contradict me tells me that I'm right."
    mike.say "That pimping piece of shit!"
    lexi.say "He's not just a pimp - he deals drugs and has his thumb in lots of other stuff too."
    mike.say "What on earth does that have to do with it?"
    lexi.say "He just gets really pissed when people pigeon-hole him, that's all."
    mike.say "Like I care what pisses him off - I hate that that low-life gorilla keeps putting his hands on you!"
    lexi.say "Yeah, well...maybe you should start to care what pisses him off."
    "Suddenly she sounds deadly serious, and I can feel ice in my gut."
    mike.say "What does that mean?"
    lexi.say "He said he's gonna kill you if I keep on seeing you on the side."
    lexi.say "That's why I didn't call you back...I wanted to keep you safe from him."
    "Suddenly the reality of what Lexi's saying begins to sink in."
    "This isn't an idle threat from some lame punk, but a serious promise from a genuinely violent sonofabitch."
    menu:
        "Back Off":
            "I recall the last run-in I had with Danny."
            "Specifically how close I came to never being able to run or walk again."
            mike.say "Maybe I should back off...you know, get out of Danny's territory?"
            lexi.say "Yeah, I guess that'd keep you safe at least..."
            "I can see that Lexi's leaving the words hanging, waiting for me to say more."
            mike.say "I mean, if I hang around, then...then he's just going to keep beating you up, isn't he?"
            show lexi casual b beat
            "Lexi looks away from me, genuine sadness and disappointment now visible in her eyes."
            lexi.say "Well...I guess it'll give him one less thing to beat on me for...and that's gotta be something."
            $ lexi.set_gone_forever()
        "Stand up to Danny":
            $ lexi.unhide()
            $ lexi.flags.DannyDelay = TemporaryFlag(True, 3)
            if lexi.love.max < 120:
                $ lexi.love.max = 120
            $ lexi.flags.trailer = True
            "Looking at the state he's left Lexi in, I suddenly don't give a shit about how big or dangerous Danny might happen to be."
            "I just hate the sight of Lexi in such a mess and so afraid - it makes me fucking mad."
            "Does this mean that I'm falling for her that badly?"
            mike.say "Yeah, big fucking man, isn't he - taking his anger out on you!"
            mike.say "Let's see what the dumb ape has up his sleeve when he's got to slap another man around."
            show fx question
            "Lexi looks up at me with surprise and even astonishment in her red-rimmed eyes."
            "Has no one ever stood up for her before, never fought for her like this?"
            hide fx
            "For a moment, the trailer-park trash image falls away, and she looks every bit like a classic damsel in distress."
            lexi.say "[hero.name], be careful - he'll really kill you!"
            mike.say "Not if I kill him first!"
    "I kiss Lexi once on the forehead to say goodbye, not wanting to aggravate her already painful bruises."
    hide lexi with dissolve
    "As I climb back into my car, I can feel myself already weighing up what I've just done."
    "But as I can't exactly change my mind now, I simply start the car, hoping that I've made the right decision as far as Lexi's concerned."
    return

label lexi_event_05:
    show bg livingroom
    play sound door_bell
    "The sound of the doorbell ringing makes me look up from my laptop and lose my train of thought."
    "Still on auto-pilot, I get up and wander towards the front door."
    "Once there, I don't even bother to check the video camera built into my fancy, expensive, accessible online doorbell."
    scene bg house
    show danny angry at center, zoomAt(1.65, (640, 1140)) with hpunch
    "Even though the chain is on, it doesn't stop a massive, tattooed arm reaching suddenly around the door and grabbing my throat."
    "I manage to make a strangled sound as I'm tossed backwards and someone puts a boot to the door."
    scene bg house
    show danny angry zorder 5 at center
    show victor as thug1 zorder 3 at right5, blacker
    show jack as thug2 zorder 2 at left, blacker
    show dwayne as thug4 zorder 4 at left4, blacker
    with fade
    "It doesn't take long for the chain to break, letting Danny stride into my hallway unopposed."
    "Turning up on my doorstep and laying their hands on me - who else was it going to be?"
    "I guess I should be impressed that the slobbering ape was smart enough to ring the bell, rather than just hammer on the door and bellow threats from the street."
    thug_say "Little pig, little pig - let me in!"
    "His words are met with gruff laughter."
    "As I get to my feet, still rubbing my throat, I see there are perhaps three or four other guys crowding the doorway behind Danny."
    "Looks like he's brought some friends along to lend a helping hand."
    thug_say "You know why I'm here, asshole."
    mike.say "Let me guess - you've found God and become a particularly aggressive Jehovah's Witness?"
    "At least two of his cronies chuckle at my suggestion, but a threatening look from Danny soon shuts them up."
    thug_say "Don't play the comedian with me - I told that stupid whore to keep away from you."
    thug_say "She didn't do as she was told, so now you gotta pay the price."
    menu:
        "Use Brains" if hero.knowledge < 50:
            mike.say "Whoa, Danny, wait a minute...what's this about you telling her to leave me alone?"
            "Danny frowns for a second, confused and trying to smell bullshit."
            mike.say "Seriously, man - she never told me anything like that."
            mike.say "In fact, she told me you were just her pimp!"
            thug_say "Well...I am her goddamn pimp!"
            "I scramble desperately for my wallet, maybe sensing a way out of the imminent beating which Danny has in mind."
            mike.say "What's the hourly rate?"
            mike.say "If I'd known that was the arrangement, I'd have already paid you myself!"
            "I proffer a handful of notes, which a still confused Danny snatches without pause or hesitation."
            thug_say "Yeah, whatever - just understand that, as far as you're concerned, Lexi's closed for business!"
            "With that, he and his cackling cronies turn and walk away, no doubt laughing at the pussy they just fleeced in his own home."
            if hero.money > 500:
                $ hero.money -= 500
            else:
                $ hero.money = 0
            $ lexi.set_gone_forever()
        "Use Brawn" if (hero.fitness + (10 * hero.has_skill("martial_arts"))) < 50:
            show danny fist
            thug_say "I promised Lexi that I wouldn't kick the shit out of you."
            "Danny laughs as he sees the glimmer of hope in my eyes at this admission."
            thug_say "But they didn't."
            "He gestures to his cronies standing in the doorway."
            play sound punch_hard
            pause 0.2
            with vpunch
            show layer master at blur(5)
            "I don't know where the first punch comes from, only that it sends me reeling."


            pause 0.2
            with vpunch
            "There's no chance to even cover my head as the blows begin to rain down from all angles."
            "The only mercy is that, with so many connecting and no means to fend them off, it's not long before I get knocked on my ass."
            "Once I'm on the hallway floor, they seem to lose interest quickly."
            "I only feel a few kicks to the stomach and groin before I'm left alone."
            stop sound
            "The last thing that I feel is someone rifling through my pockets, taking my wallet and phone."
            "I'm only sure it's Danny because he pauses to hiss something threatening into my ear."
            "In my dazed state, none of it makes any sense - but I think that I still get the essential message all the same."
            call injured from _call_injured_8
            if hero.money > 500:
                $ hero.money -= 500
            else:
                $ hero.money = 0
            $ lexi.set_gone_forever()
        "Use Brains" if hero.knowledge >= 50:
            if lexi.love.max < 140:
                $ lexi.love.max = 140
            $ lexi.flags.DannyDelay = TemporaryFlag(True, 3)
            mike.say "Christ, Danny - just how fucking dumb are you?"
            thug_say "What the hell did you just call me?!?"
            mike.say "Try to listen to me, man - I didn't call you anything, I asked you a question."
            mike.say "This kind of thing might work in a back alley or a sleazy nightclub."
            mike.say "But look around you - this is suburbia, you just walked up to my door and got filmed by a dozen cameras!"
            "Danny's cronies begin to glance around nervously, muttering to one another and shuffling backwards."
            show danny -angry
            "Danny too is looking less sure of himself now, trying to muster his former strength."
            mike.say "How about this, Danny?"
            mike.say "You had your pound of flesh as far as Lexi's concerned."
            if lexi.is_visibly_pregnant:
                mike.say "But now she's pregnant with my kid, and it's time for you to find another vulnerable girl to exploit."
            else:
                mike.say "But now she's mine, and it's time for you to find another vulnerable girl to exploit."
            mike.say "Walk away now, leave us alone, and I won't call the cops or let them have the footage from my security cameras."
            "Danny tries to pull himself up for one last try at me, but one of his cronies puts a hand on his shoulder whilst shaking his head."
            "I can hear Danny mouthing something that might be a threat as he walks away, but it's half-hearted and lame."
        "Use Brawn" if (hero.fitness + (10 * hero.has_skill("martial_arts"))) >= 50:
            if lexi.love.max < 140:
                $ lexi.love.max = 140
            $ lexi.flags.DannyDelay = TemporaryFlag(True, 3)
            thug_say "I promised Lexi I wouldn't touch you - but these guys didn't!"
            hide danny
            show danny angry zorder 1 at center with dissolve
            "Danny waves his cronies forward, and now I see that there are three of them."
            "Luckily, none of them are carrying weapons, and they don't think to rush me all at once."
            "The first one, a rat-faced guy in a denim vest swings messily at me and gets a punch to the groin for his trouble."
            play sound [woosh_punch, "<silence .1>", punch_hard]
            with hpunch
            pause 0.2
            hide victor as thug1 at right5 with moveoutbottom
            "The second, a fat fuck with a shaved head is in range of a kick to the gut before he realizes his friend went down."


            pause 0.3
            hide dwayne as thug4 at left4 with moveoutbottom
            "The third and last, a big bearded biker type, almost walks straight into a fist that spreads his nose across his left cheek."
            play sound punch_hard
            pause 0.2
            hide jack as thug2 at left with moveoutleft
            "With all three of his lackeys on their asses, all eyes turn to Danny."
            "I look at him to see if he's going to be number four, and his downed cronies look to see if he's going to make me pay."
            show danny normal
            "Danny glances at me, then at them, and then back to me."
            if game.flags.thugfight:
                show danny scared
                "Maybe he's genuinely shitting himself, or maybe he's recalling me handing him his own ass the last time round."
            else:
                show danny scared
            "Without saying a word, Danny turns and runs out the front door."
            hide danny with dissolve
            "Stunned for a moment, it takes his cronies perhaps ten seconds to get up and follow his lead."
            call injured from _call_injured_9
    scene bg livingroom with fade
    "Finally able to close and double-bolt the front door, I realize only then that I'm shaking like a shitting dog."
    "In that second, I'm not thinking of the consequences of what just happened or who came out on top."
    "I'm just gasping for breath, hoping that it means I never have to see Danny again."
    "Either on my doorstep or anywhere else."
    return

label lexi_event_06:
    show bg bedroom1
    play sound cell_vibrate
    "I can't recall if the dream was about anything pleasant or not, as it fades from my mind as my phone unceremoniously wakes me up."
    "Bleary-eyed, I see firstly that it's far too early for phonecalls, and secondly that the call's from Lexi."
    stop sound
    $ result = renpy.call_screen("smartphone_choice", "Lexi")
    if not result:
        $ hero.cancel_event()
        $ lexi.love -= 5
        return

    "I don't know which is more annoying in that moment, but I decide to take the call anyway."
    mike.say "I'd say what time do you think it is, Lexi."
    mike.say "But what would it get me..."
    thug_say "Jack and shit, asshole - and Jack just left town!"
    "At the sound of Danny's mocking tones, I almost drop the phone in surprise."
    mike.say "Danny...what the hell?!?"
    thug_say "That's right, prick."
    mike.say "Where's Lexi...what have you done to her?"
    thug_say "Settle down, man - I haven't done anything to her...yet!"
    mike.say "You bastard - let her go, or I'll call the cops!"
    thug_say "Oh no you don't - this is between you and me."
    if lexi.is_visibly_pregnant:
        thug_say "Call the cops, and all they'll find of her is pieces - same goes for the kid too."
    else:
        thug_say "Call the cops, and all they'll find of her is pieces."
    mike.say "Bastard!"
    thug_say "Yeah, you already called me that once."
    thug_say "Look, if she means that much to you, then you'll meet me at the address I text you after I hang up."
    thug_say "If you want to see her again and you want to see her alive, you'll come quick and you'll come alone."
    if lexi.is_visibly_pregnant:
        "After he hangs up I feel my guts churning at the thought of what he might do to Lexi and the baby."
    else:
        "After he hangs up I feel my guts churning at the thought of what he might do to Lexi."
    menu:
        "Call Camila" if not camila.flags.schedule == "hospital" and ((not camila.hidden and camila.love >= 80) or Harem.together('camila', 'lexi', name='criminal')):
            "Part of me is terrified of what Danny will do to Lexi if I do call the cops."
            "But another part of me is screaming that I know one particular cop that's tougher than the rest."
            "The kind of cop that eats scumbags like him for breakfast!"
            "Without another thought, I dial Camila's number and wait impatiently for her to answer."
            camila.say "[hero.name]..."
            camila.say "What's up?"
            mike.say "Camila...Camila..."
            mike.say "I need your help!"
            mike.say "And I need it now!"
            "I'm practically ranting down the phone by now, almost in hysterics."
            camila.say "Whoa!"
            camila.say "Slow down a little..."
            camila.say "Tell me what's happened, okay?"
            "I manage to get a little more control of myself."
            "And then I try to explain the situation more carefully."
            mike.say "It's Lexi..."
            mike.say "She's been kidnapped!"
            if Harem.together('camila', 'lexi', name='criminal'):
                camila.say "WHAT?!?"
                camila.say "Who took her, [hero.name]?"
                camila.say "Because they're gonna answer to me!"
            else:
                camila.say "Is that the same Lexi I know from the streets?"
                camila.say "The one I must have busted a hundred times already?"
                mike.say "Uh...yeah..."
                mike.say "Does that make a difference?"
                camila.say "Not really - nobody kidnaps a woman on my turf!"
                camila.say "Even if she is a massive skank..."
            mike.say "The guy who did it is called Danny."
            mike.say "He told me where to meet him."
            mike.say "But he also said I shouldn't call the cops!"
            "I hear Camila chuckle on the other end of the line."
            camila.say "You didn't call the cops, [hero.name]."
            camila.say "All you did was call a friend!"
            camila.say "Now stay where you are - I'm on my way!"
            show bg house with fade
            "I wait impatiently for Camila to show up."
            "And when her cruiser screeches to a halt outside, I hurry over."
            play sound car_door
            "She shoves the door open and motions for me to jump in."
            show bg map with fade
            "Then we speed off to the location that Danny gave me for the rendezvous."
            "When we arrive, I see it's another conveniently shady alleyway."
            "What is it with this guy and alleyways?"
            "Is he allergic to cleanliness and open spaces or something?"
            show bg taxi at center, zoomAt(1.5, (940, 1040)) with fade
            play sound car_door
            with vpunch
            pause 0.4
            play sound car_door
            show camila a annoyed at center, zoomAt(1.5, (940, 1040)) with easeinright
            "Camila nods to the entrance of the alleyway as we get out."
            camila.say "You walk in there ahead of me."
            camila.say "Act like I'm not even here."
            "I can't help swallowing with fear and trepidation."
            mike.say "Are you sure that's a good idea?"
            mike.say "What if he jumps me or something?"
            show camila a wink
            "Camila give me a wry smile as she pulls out her pistol."
            camila.say "Don't worry about a thing."
            camila.say "I'll be covering you the whole time."
            "I nod and turn towards the mouth of the alleyway."
            "All the time trying to look like I'm anything other than terrified."
            scene bg alley with fade
            mike.say "Lexi...are you there?"
            mike.say "It's me, [hero.name]."
            show bg alley at center, zoomAt(1.5, (940, 940))
            show lexi b beat nophone at center, zoomAt(1.5, (640, 1040)), dark
            with hpunch
            "Suddenly I see Lexi, on her side, hands bound behind her back and mouth stuffed with a ball gag."
            "I start to make towards her, but then I see her eyes widen as she looks over my shoulder."
            play sound gun
            "Before I can turn to see what Lexi's staring at, there's a deafening boom."


            "It's followed by the sound of metal striking metal, and a human cry of pain."
            scene bg alley
            show danny angry fist at right with easeinright
            "I spin round just in time to see Danny, caught in the act of leaping out of the shadows."
            "He's clutching his wrist, where blood is already pumping from a nasty wound."
            "And a quick glance down lets me see a pair of wicked-looking machetes at his feet."
            show camila angry at left with easeinleft
            camila.say "Don't move, creep!"
            show danny surprised at right5 with ease
            camila.say "That first shot was a warning."
            camila.say "The next one I put right between your eyes!"
            danny.say "Oh fuck..."
            danny.say "Oh fuck..."
            show danny angry
            danny.say "You fucking shot me!"
            show danny angry -fist at right
            show camila a handcuff at right5
            with ease
            pause 0.2
            show danny angry -fist at right, hshake
            show camila a handcuff at right5, hshake
            "Camila ignores Danny's stunned protests as she closes the distance between them."
            "Then she shoves him hard against the wall, making sure to jerk his arm as she cuffs him."
            hide camila
            hide danny
            with easeoutright
            pause 0.5
            show bg alley at center, zoomAt(1.5, (940, 940))
            show lexi b beat nophone at center, zoomAt(1.5, (640, 1040)), dark
            with hpunch
            "While she tosses Danny into the back of her cruiser, I hurry over to check on Lexi."
            hide lexi
            show lexi b beat nophone at center, zoomAt(1.5, (640, 1040))
            with dissolve
            lexi.say "Oh fuck, oh, fuck...I'm so glad you're okay!"
            mike.say "Screw me - what about you?"
            scene bg alley
            show lexi kiss zorder 2
            with fade
            $ lexi.flags.kiss += 1
            "Lexi answers me by wrapping herself around me and kissing me with a sudden violence that takes me by surprise."
            if Harem.together('camila', 'lexi', name='criminal'):
                camila.say "Hey!"
                show camila surprised zorder 1 at right with easeinright
                camila.say "What about me, Lexi?"
                show camila angry
                camila.say "I was the one that shot the asshole!"
            else:
                show camila annoyed zorder 1 at right with easeinright
                camila.say "Ahem..."
            scene bg alley
            show lexi a beat nophone zorder 2 at center, zoomAt(1.5, (440, 1040))
            show camila a zorder 1 at center, zoomAt(1.5, (840, 1040))
            with fade
            "Lexi breaks off the kiss as Camila walks over to where we're standing."
            lexi.say "So..."
            lexi.say "What happens to Danny now?"
            show camila normal
            camila.say "I take him down to the precinct and charge his ass, that's what!"
            show camila angry
            camila.say "Armed kidnapping on top of the record he's already earned himself?"
            show camila happy
            camila.say "My guess would be that he's going away for a VERY long time!"
            "Lexi, Camila and I spend a little longer talking."
            "Mostly making sure that Lexi's okay."
            hide camila with easeoutright
            "Then Camila excuses herself to drive Danny to the police station."
            "Which leaves me to walk Lexi back home."
            "Well, that and to hope we've seen the last of Danny."
            if lexi.love.max < 200:
                $ lexi.love.max = 200
            $ game.room = "alley"
            $ lexi.flags.bypass_danny_corpse = True
        "Go alone":
            show bg house with fade
            "I scramble out of bed and clamber into some clothes before dashing out the door."
            "I sit panicking for what feels like an age before the promised text arrives from Lexi's phone."
            "Hammering the address into the GPS, I see it's another conveniently shady alleyway."
            "What is it with this guy and alleyways?"
            "Is he allergic to cleanliness and open spaces or something?"
            show bg map with fade
            "The ride over there consists of me going as fast as I can and then desperately trying to slow down to avoid suspicion."
            show bg alley with fade
            "I manage to arrive twenty minutes later, instantly regretting not bringing my handgun when I see the entrance to the alleyway."
            "I take a deep breath, and start to walk into the less than welcoming darkness."
            mike.say "Lexi...are you there?"
            mike.say "It's me, [hero.name]."
            show lexi b beat casual nophone with dissolve
            "Suddenly I see Lexi, on her side, hands bound behind her back and mouth stuffed with a ball gag."
            "I start to make towards her, but then I see her eyes widen as she looks over my shoulder."
            if (hero.fitness + (15 * hero.has_skill("martial_arts"))) < 75:
                "I realize that she's seen something over my shoulder a split-second too late."
                hide lexi
                play sound knife
                queue sound knife_stab
                pause 0.2
                show danny fight2 mike sad at center, hshake
                pause 0.2
                with hpunch
                "I feel the jarring impact of something heavy and yet sharp in my stomach a second later."
                scene bg alley at center, blood
                show danny fight2 mike sad at center, blood
                with dissolve
                "There's no time to react, or even to scream as I collapse into a heap on the ground."
                scene bg alley at blood
                show lexi b beat casual nophone at right, blood
                show danny angry at left, blood
                with dissolve
                "I can hardly hear Lexi, screaming around the gag in her mouth as Danny steps over me to gloat."
                "He's saying something as he waves a pair of machetes before me."
                "The blood on one of them drips onto the ground and splatters Lexi as he does so, making her flinch and recoil."
                "I can't feel any pain, just fatigue making it impossible to move...even to lift my head."
                "Everything seems to become ever more unreal, as I watch Danny haul Lexi reluctantly to her feet."
                "I could be watching a silent movie as he unceremoniously yanks down her shorts and opens his flies."
                "I suppose this is meant to be one final insult, his screwing her in front of me as I slip away."
                scene bg alley at blur(8), dark, blood
                show lexi b beat casual nophone at right, blur(8), blood
                show danny angry at left, blur(8), blood
                with dissolve
                "But it all seems so remote right now that I can't even..."
                "I can't even recall why I'm here."
                "And then it all goes black."
                "And I'm not anywhere any longer."
                scene bg black with dissolve
                pause 1.0
                $ renpy.full_restart()
            else:
                hide lexi
                play sound woosh_punch
                show danny fight2 none sad at center, hshake
                "I realize that Lexi's seen danger over my shoulder, and instinctively sidestep."
                play sound woosh_punch
                show danny fight2 none sad at center, hshake


                with hpunch
                "I hear the whistle of something passing over my head, and then a metallic clang as a heavy blade clatters into a dumpster by my side."
                show lexi beat casual b nophone zorder 1 at right
                show danny angry zorder 2 at left
                "Turning to place myself between Lexi and the attacker, I'm not surprised to see Danny emerging from the shadows."
                "He's swearing under his breath as he tries to shake feeling back into the hand that was holding the machete now visible on the ground."
                "That'd be more of a relief if he wasn't holding its twin in the other hand."
                show danny at center
                show lexi at mostright4
                with move
                "He doesn't say a word as he squares up to me, letting me know that this is only going to end with one of us either bleeding or dead."
                "We both eye the fallen machete, knowing that to make a move for it would leave us open."
                "The only problem is that he already has the advantage it'd give me."
                hide danny
                show danny angry fist at zoomAt (1.2, (300, 0))
                hide lexi
                with vpunch
                "In the end, I make the first move - stepping in close and grabbing his wrist with both hands."
                "I know Danny's probably used to his size and strength making people back off."
                "So I try to use this to my advantage and catch him off guard."
                play sound punch_hard
                pause 0.2
                hide danny
                show danny fight alone at right, hshake
                with hpunch
                "He logically begins to punch me square in the face, but he hasn't bargained on just how desperate I am to live right now."
                play sound punch_hard


                with hpunch
                "Between his punches, I pull my head back and then smash my forehead down onto his nose as often as I can manage."
                hide danny
                show danny angry fist at zoomAt (1.2, (300, 0))
                "Danny had been wanting to free his arm and make a show of killing me with his remaining machete."
                "But all I want to do is render him unconscious, and in the end, my simpler goal wins out."
                hide danny
                play sound knife
                queue sound knife_stab
                pause 0.2
                show danny fight2 danny at center, hshake
                pause 0.2
                with hpunch
                "Dazed and unsteady on his feet, he stumbles and falls, the machete slitting him open from belly to breastbone as he goes down."
                "As soon as Danny is dealt with, I rush over to pull the gag out of Lexi's mouth and begin untying her."
                play sound body_fall
                pause 0.4
                hide danny
                show lexi beat casual nophone with moveinright
                lexi.say "Oh fuck, oh, fuck...I'm so glad you're okay!"
                mike.say "Screw me - what about you?"
                hide lexi
                show lexi kiss
                $ lexi.flags.kiss += 1
                "Lexi answers me by wrapping herself around me and kissing me with a sudden violence that takes me by surprise."
                "The cuts and bruises I'm covered in suddenly don't seem to matter, and I could probably have been persuaded to fuck her, right there and then."
                hide lexi kiss
                show lexi beat casual nophone
                "When the moment passes, Lexi looks down at Danny's immobile body."
                lexi.say "Is he...dead then?"
                mike.say "Unless he knows a way to survive bleeding out with his guts in his hands."
                lexi.say "Huh...he was always like some kind of human cockroach...I guess part of me thought he'd never croak."
                lexi.say "I always thought I'd be dancing on his dead body and singing a fucking song."
                lexi.say "But all I feel right now is numb...just glad you're alive and he's not."
                "I shrug and kick the corpse just to be sure."
                mike.say "At least he won't be able to threaten you or me again."
                mike.say "I just wonder where we go from here?"
                lexi.say "First we cut off his hands and smash out his teeth, so he can't be identified."
                lexi.say "Then we weight the body with stones and dump it in the river, hope that the fish eat what's left before someone pulls it out."
                "I stare at Lexi, utterly flabbergasted at the plan she just laid out in such gory detail."
                lexi.say "What's the matter?"
                show lexi happy
                lexi.say "Do you think I never laid awake at night plotting out how I'd get rid of the evidence if I ever managed to kill that bastard myself?"
                "I shake my head in amazement, wondering what other unexpected surprises lurks in the unexplored regions of Lexi's brain."
                "But I can't deny that her plan is at least practical and we have the tools at hand to pull it off."
                "I nod and bend to pick up the machete not currently buried in Danny's rapidly cooling guts."
                mike.say "Okay, Lexi - this corpse ain't gonna mutilate itself."
                mike.say "Let's get started."
                call injured from _call_injured_10
                $ hero.gain_item("danny_corpse")
                if lexi.love.max < 160:
                    $ lexi.love.max = 160
                $ game.room = "alley"
                $ game.flags.dannydead = True
    return

label lexi_event_07a:
    "I gasp and groan as I struggle to pull Danny's body in the small boat."
    "And I'm thankful that I wrapped him up in plastic before I drove all the way out here."
    "Because at least I don't have to look the scumbag in the face while I'm doing this."
    "All I can hear is the sound of the waves as sail deeper into the sea."
    "But I'm still paranoid, constantly listening out for the sound of another living soul."
    "I've gotten myself into some pretty dumb messes in my time, no doubt about it."
    "But I never thought that I'd find myself in a situation like this one."
    "I mean, how on earth did I end up lugging a dead body around in the night?!?"
    "Lexi - that's how."
    "All of this is down to Lexi!"
    "I was just trying to protect her from that jerk, Danny."
    "And I thought that I was doing the right thing too."
    "He would have gone too far with Lexi, sooner or later."
    "But rather than him killing her, I ended up killing him!"
    "I just hope that she's worth all the effort that I'm going to for her."
    "After all, she's made me into a murderer!"
    "I try to push any such thoughts out of my head as I decide that I am far enough."
    "There's going to be plenty of time to wrestle with my conscience later."
    show danny corpse ocean with fade
    "I drag Danny's corpse as close to the side of the boat as I dare."
    "The last thing I want is to fall off as I push it over."
    "Or worse, tumble into the water leaving the body for someone to find in my rental boat!"
    "I pause for a moment, wondering if I should say a few words first."
    "But then I shake my head, cursing myself for being so stupid."
    "This isn't some chance to see Danny off with a damn tribute."
    "The guy was a massive piece of shit who got what he deserved!"
    "And I'm the one that killed him too - so what am I waiting for?"
    "Spurred into action by this revelation, I give the body an experimental kick."
    "When it hardly moves an inch, I know that this isn't going to be easy."
    "Part of me had been hoping that I could just roll him over with my foot."
    "But I'm also not going to pick up the body and throw it in either."
    "All I can see happening there is be over-balancing and following it down."
    "So instead I choose to get down on my knees and roll Danny over ledge."
    "No matter how hard I try, I can't roll him over."
    "And so I resort to pushing his head and then his feet in turn."
    "Inch by inch, more of the body teeters over the edge."
    "Then, all of a sudden, gravity takes control, and it topples over."
    hide danny corpse with fade
    "I leap back, still afraid of falling along with it."
    "But then I hear the sound of it hitting the waves."
    "Instantly my mind is filled with the worst possible scenarios."
    "What if the body washes up on the beach tomorrow morning?"
    "Should I have weighted the body down before I dumped it?"
    "I mean, I know they say that shit floats."
    "And Danny was one of the biggest turds I ever met!"
    "All of these thoughts are running around in my head as I look over the edge."
    "But then I turn and flee back the way that I came, almost on auto-pilot."
    "Maybe it'll all be okay."
    "Maybe Danny's body will sink straight to the bottom of the sea."
    "Or maybe it'll be washed out into the ocean and eaten by a shark."
    "Whatever happens, I have to remember why I'm doing this in the first place."
    "And that's because I wanted to step in and save Lexi from that creep."
    "Being able to have her all to myself is just a bonus, of course!"
    "So with that in mind, I hurry off into the night."
    "Lexi's made a murderer out of me."
    "I just hope that she's worth it!"
    $ hero.lose_item("danny_corpse")
    if lexi.love.max < 180:
        $ lexi.love.max = 180
    return

label lexi_event_07b:
    "Dragging the body behind me with one hand, I try to shoulder the spade with the other."
    "It's tough going, dragging something so awkward and heavy over uneven ground like this."
    "But I keep on, gasping and groaning every step of the way, looking for the perfect spot."
    "I turn and glance around at each and every sound I hear, paranoid of being discovered."
    "And it's just a small mercy that I decided to wrap Danny's corpse up in plastic beforehand."
    "At least I don't have to look at his ugly face while I'm doing this."
    "I've gotten myself into some pretty dumb messes in my time, no doubt about it."
    "But I never thought that I'd find myself in a situation like this one."
    "I mean, how on earth did I end up lugging a dead body around in the night?!?"
    "Lexi - that's how."
    "All of this is down to Lexi!"
    "I was just trying to protect her from that jerk, Danny."
    "And I thought that I was doing the right thing too."
    "He would have gone too far with Lexi, sooner or later."
    "But rather than him killing her, I ended up killing him!"
    "I just hope that she's worth all the effort that I'm going to for her."
    "After all, she's made me into a murderer!"
    "I shake off the thought as best I can, realising that it's not helping."
    "And almost the same moment I do, I realise that I'm standing in a clearing."
    "I take a moment to have another glance around, searching for any sign of human life."
    "When I see and hear nothing, I decide that this is the perfect spot to bury Danny."
    show danny corpse forest with fade
    "Letting go of the corpse, I get straight to work with the spade."
    "The ground is hard and filled with plenty of rocks and roots."
    "But I just keep on going, muttering under my breath the whole time."
    "I don't know how long it takes me to dig down to a depth of a good few feet."
    "All I know is that it feels like it takes too long, like it takes forever."
    "I keep thinking that I'll see the first light of dawn any second."
    "And that I'll be seen the very moment that happens for sure."
    "But somehow the darkness holds all the time I'm digging the hole."
    "I climb out of it still under the cover of night and toss down the spade."
    "I'm too exhausted by now to even think of picking up the corpse."
    "So instead I sink down onto my knees and start to push it towards the hole."
    "No matter how hard I try, I can't roll him over."
    "And so I resort to pushing his head and then his feet in turn."
    "Inch by inch, more of the body teeters over the edge."
    "Then, all of a sudden, gravity takes control, and it topples into the hole."
    "Struggling to my feet, I pick up the spade and take a deep breath."
    "I pause for a moment, wondering if I should say a few words first."
    "Then I shake my head, cursing myself for being so stupid."
    "This isn't some chance to see Danny off with a damn tribute."
    "The guy was a massive piece of shit who got what he deserved!"
    "And I'm the one that killed him too - so what am I waiting for?"
    "I start half shovelling and half dragging the dirt into the hole."
    "And all the time my head is beginning to fill with questions."
    "What if I haven't gone deep enough into the woods?"
    "What if I haven't buried him deep enough in the ground?"
    "Will his body still rot wrapped up in all that plastic?"
    "I mean, Danny was probably the biggest shit I ever met."
    "And shit turns into fertilizer when you bury it, right?"
    "All of this is bouncing around inside my head as I pat the earth down."
    hide danny corpse with fade
    "Then I turn on my heel and flee back the way I came, almost on autopilot."
    "What if somebody spots the tell-tale signs of disturbed earth?"
    "What if somebody's dog smells that he's down there and digs him up?"
    "Maybe it'll be okay."
    "Maybe nobody comes out this far to walk or exercise their dog."
    "Or maybe a bear will dig up Danny's body and eat it."
    "Bears do that, don't they - eat people?"
    "Whatever happens, I have to remember why I'm doing this in the first place."
    "And that's because I wanted to step in and save Lexi from that creep."
    "Being able to have her all to myself is just a bonus, of course!"
    "So with that in mind, I hurry off into the night."
    "Lexi's made a murderer out of me."
    "I just hope that she's worth it!"
    $ hero.lose_item("danny_corpse")
    if lexi.love.max < 180:
        $ lexi.love.max = 180
    return

label lexi_event_08:
    if lexi.love.max < 200:
        $ lexi.love.max = 200
    show lexi sad nophone
    "Lexi looks worried from the first moment I lay eyes on her, guilty and almost jumpy too."
    "But I guess that's perfectly natural, given what we've both been through recently."
    "After all the shit that she's had to put up with from Danny, she should be elated."
    "But she's been under his thumb for so long, maybe it's hard to believe that he's really gone."
    "For all I know, Lexi could be convinced that the creep's going to come back from the dead!"
    "Eww...now that I come to think of it, Zombie Danny would be even worse than living Danny!"
    "I try my best to force a smile onto my face, hoping to cheer Lexi up."
    lexi.say "Is it..."
    lexi.say "Did you..."
    "Lexi wrings her hands as she holds them under her chin."
    "She seems to emotional that she can't even get her words out!"
    mike.say "Yeah, Lexi."
    mike.say "I did it and it's done!"
    mike.say "I put Danny's body where nobody'll ever find it."
    show lexi happy
    "Well, at least where I hope nobody will ever find it!"
    "But now's not the time to be worrying Lexi with little details like that."
    "We're finally rid of that scumbag, and we should be able to enjoy that freedom."
    "I'm glad to see the look on Lexi's face change as I say all of this."
    "She goes from looking worried to elated, smiling like a Cheshire cat."
    lexi.say "Oh, [hero.name]!"
    lexi.say "Whatever did I do to deserve a guy like you?"
    lexi.say "You're like SO different to Danny."
    lexi.say "Like the total opposite of the creep."
    lexi.say "You're the Anti-Danny!"
    mike.say "Ah...yeah, Lexi."
    mike.say "If you say so!"
    "It doesn't seem to matter what I say now."
    "Lexi's already worked herself up into a state of euphoria."
    "I'm still shaken up from the experience of dumping a body."
    "I want to share her delight at finally being free of Danny."
    "But the reality of what I've done won't stop nagging at the back of my mind."
    show lexi normal
    lexi.say "This is it, [hero.name]!"
    lexi.say "This is the start of our new lives together."
    lexi.say "You're like my knight in shining armour."
    lexi.say "What you did is SO romantic!"
    "Wait a minute..."
    "What I did?!?"
    "Lexi's making it sound like killing Danny was all my idea!"
    "I open my mouth to protest, at least to remind her we're in this together."
    show lexi close flirt
    "But then she wraps her arms around my waist and hugs me tight."
    "Lexi presses herself against me, sighing with a deep and genuine satisfaction."
    "I can feel myself melting even before she opens her mouth to speak."
    lexi.say "Mmm..."
    lexi.say "I've never felt this safe before, [hero.name]."
    lexi.say "I've never felt this happy too."
    lexi.say "And it's all because I love you!"
    "That's it, right there."
    hide lexi
    show lexi kiss
    with fade
    $ lexi.flags.kiss += 1
    "As soon as Lexi speaks those words, she's got me."
    "All I can do is return the hug, wrapping her in my arms."
    "I'd do anything to hear her talking about me like that."
    "And I do mean anything - because I already killed a guy for her!"
    return

label lexi_male_ending:
    $ game.hour = 16










    if renpy.has_label("lexi_achievement_3") and not game.flags.cheat:
        call lexi_achievement_3 from _call_lexi_achievement_3
    $ game.room = "church"
    scene bg church wedding with fade
    "It's crazy, I know, but a large part of me still can't believe that today has actually arrived."
    "This thing is really happening - Lexi and I are about to stand in front of a priest and get married!"
    "I...well, I kind of feel bad for saying this..."
    "But when I first met her, Lexi was the last girl in the world I could have imagined doing this with."
    "She was mad, bad and pretty dangerous to know, mixed up in all sorts of nefarious schemes."
    "And yet there was always something about her, something that drew me to her."
    "It was like underneath it all, she was just a great girl that lived life to the full."
    "I guess I was lucky to discover that, as she left all the bad stuff behind, that's just what she was."
    "The Lexi that I got to know and grew to love is just wonderful in so many ways."
    "Sure, she's still more than a little wicked and likely to break all the rules."
    "But it's usually in a good way, if that makes sense?"
    "Or at least in a way that's good for the both of us!"
    "Anyway, that's enough of me waxing lyrical about Lexi and her foibles."
    "The music just started playing and I think I can see her coming down the aisle."
    show lexi wedding nophone at center, zoomAt(1.0, (640, 730)) with dissolve
    "When I actually get a good look at her, I can't help smiling."
    "Lexi looks stunning in the dress that she's chosen."
    "It flatters her and still manages to reflect her quirky personality as well."
    if lexi.is_visibly_pregnant:
        "And it somehow manages to accommodate her swelling belly too!"
        if lexi.flags.mikeBabies >= 1:
            "It didn't come as any surprise to learn that Lexi's carrying twins."
        "There's still some time to go before she's due, but she already looks fit to burst."
        "Not that it matters to me - as all I can see is the future that we're planning together."
    else:
        "Case in point - I can see that Lexi's actually chewing gum right now."
        "And she proves it by blowing a large, pink bubble as she walks towards me."
        "The bubble pops and Lexi sucks it back into her mouth with an audible cracking sound."
        "Then she smiles at me, unashamed as ever."
    show lexi close blush at center, traveling(1.5, 3.0, (640, 1040))
    "Lexi stands by my side, paying more attention to me than she does the priest."
    "Even now I can tell that she's enjoying having my eyes playing over her."
    "And, well...she does look amazingly hot!"
    show wedding lexi with fade
    "All I can think about in that moment is what she's wearing under that dress."
    "That and when I'll have the chance to get her out of it..."
    "Priest" "Ahem..."
    show wedding lexi priest with dissolve
    "At the sound of the priest's little reminder, I snap to attention."
    "But if the reprimand was meant for Lexi as much as me, she pays it no mind."
    "Instead she lets out a particularly filthy laugh as she faces front and centre."
    "Clearly she's amused at my being told off for eyeing her up on this special occasion!"
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here to today to witness the union of these two people..."
    "I can hear the priest as he drones on with the ceremony."
    "And I've rehearsed this thing so many times that I feel confident not paying attention."
    "Instead I fill my mind with ideas of what Lexi and I can get up to later."
    "Which is why the part where I'm supposed to get involved kind of sneaks up on me!"
    "Priest" "Do you, [hero.name], take Lexi to be your lawful, wedded wife?"
    mike.say "Yes...yes, I do!"
    "Priest" "And do you, Lexi, take [hero.name] to be your lawful, wedded husband?"
    lexi.say "Yeah, I do!"
    "The priest nods, unable to suppress a smile at Lexi's enthusiasm."
    "Priest" "I call upon all those present..."
    "Priest" "If they know of any lawful or moral reason that these two may not be wed..."
    "Priest" "To speak now, or forever hold their peace!"
    "The silence that descends over the chapel should just be for the sake of tradition."
    "But I've secretly been dreading this moment the whole time."
    "Part of me can't help wondering if Lexi's past is about to catch up to us."
    "Is the ghost of that scumbag Danny about to crash the party?"
    "Or are the police going to roll up and drag Lexi away in handcuffs?!?"
    "Finally, the priest gives a satisfied nod and gets the show going again."
    "And it's only then that I realise I've actually been holding my breath!"
    "Priest" "Then I declare you husband and wife."
    "Priest" "You may kiss the bride!"
    scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
    show lexi kiss wedding
    with fade
    $ lexi.flags.kiss += 1
    "I lean in, expecting one of those sweet kisses you see couples exchanging at this point."
    "But Lexi surprises me by clamping onto me and sticking her tongue straight down my throat!"
    "After a moment of surprise, I give in and return the gesture."
    "I mean, I never fell for Lexi on account of her being chaste or demure."
    "So why shouldn't I go with it now!"
    if not "date_lexi_meet_jack_4" in DONE:
        scene lexi ending
        $ babies = lexi.flags.mikeBabies + 1 if lexi.is_visibly_pregnant else lexi.flags.mikeBabies
        if babies == 1:
            show lexi ending daughter
        elif babies >= 2:
            show lexi ending daughter son
        with fade
        lexi.say "So, what?"
        lexi.say "I just talk about me and [hero.name]?"
        lexi.say "That's it?!?"
        lexi.say "Huh...okay, if that's what you want."
        lexi.say "First thing to confess is that when I first met [hero.name], I thought he was just another mark."
        lexi.say "Just another dumb guy that was going to be parted from his cash as easily as all the rest were."
        lexi.say "Sure, I noticed right from the start that he was pretty cute, and a sweet sort to boot."
        lexi.say "But that's just how I was back then - I didn't see people as people."
        lexi.say "I guess I just saw them for what they were worth to me, how I could exploit them."
        lexi.say "But [hero.name], well, he was one of the ones dumb enough to keep coming back for more."
        lexi.say "At least that's what it seemed like to begin with."
        lexi.say "It took me a while to realise that he was actually coming back for me."
        lexi.say "Because...because he liked me that much..."
        lexi.say "Look, I know this is making me sound like a really cold-hearted bitch."
        lexi.say "But my life was hard back then, I was in a bad place and in with bad people."
        lexi.say "[hero.name] was different though, he seemed to like me for me."
        lexi.say "He wasn't just interested in how he could exploit me."
        lexi.say "Not like that piece of shit Danny!"
        lexi.say "Oh, the day he kicked that guy's ass in the alleyway."
        lexi.say "It was like I had a knight in shining armour or something!"
        lexi.say "I think that was when I finally started to get it."
        lexi.say "When I understood that [hero.name] really was in love with me."
        lexi.say "It's not just that though, you know?"
        lexi.say "He kind of comes from a different place than me."
        lexi.say "But [hero.name] never tried to make me change to be more like other girls."
        lexi.say "He never sneered at my trailer or how I dress either."
        lexi.say "And when you've been called trash as often as I have..."
        lexi.say "Well, it's not nothing, I can tell you."
        lexi.say "That's how I know it's real, that he's not just slumming it with me."
        lexi.say "Because he'd have gotten tired of it by now, I just know it."
        if babies == 1:
            lexi.say "And the last thing that he'd ever have done was jump into starting a family with me."
            lexi.say "Ever since Chantel arrived, [hero.name]'s been the perfect daddy to her."
            lexi.say "He adores that little rascal, you can see it in his eyes whenever he looks at her."
        elif babies >= 2:
            lexi.say "And the last thing that he'd ever have done was jump into starting a family with me."
            lexi.say "Ever since Chantel and Tyrone arrived, [hero.name]'s been the perfect daddy to them."
            lexi.say "He adores those two little rascals, you can see it in his eyes whenever he looks the pair."
        else:
            lexi.say "And the last thing that he'd ever have done was jump into setting up a home with me."
            lexi.say "Yeah, that's right - I moved out of the trailer park and into an actual house with [hero.name]!"
            lexi.say "Sure, some of the neighbours don't seem to like what they see when I'm lounging by the pool."
            lexi.say "But screw them anyway - who cares about what they think?"
        lexi.say "It's still hard for me to believe it some days, and I feel like pinching myself."
        lexi.say "I have a husband and an actual house - which I suppose means I'm a housewife!"
        lexi.say "[hero.name] keeps dropping hints that I should do something with all the free time I have now."
        lexi.say "Maybe take a course at the local community college, even start up a business of my own."
        lexi.say "But for now I'm having too much of a good time just enjoying being a lazy wife!"
        lexi.say "Who needs to worry about stuff like that when I have the rest of my life ahead of me?"
        lexi.say "I could even stand to lose it all again and go back to the trailer park."
        lexi.say "So long as I have [hero.name] with me, that is."
        lexi.say "He makes me feel like I can do anything."
        lexi.say "And I guess that's what being in love feels like."
    else:
        $ game.room = "nightclub"
        scene lexi ending2
        lexi.say "You want me to do this?"
        lexi.say "I'm going to get to talk to people for real?!?"
        lexi.say "That's great - they finally get to hear the real me!"
        lexi.say "And it's about fucking time too!"
        lexi.say "Oops...sorry - am I supposed to keep it clean?"
        lexi.say "Whatever..."
        lexi.say "This ain't some fairy-tale and I'm no goddamn princess, that's for sure!"
        lexi.say "Yeah, it's weird the way things turn out in the end."
        lexi.say "I mean, sure I liked [hero.name] when I first met him."
        lexi.say "But back then he was just another mark for me to work."
        lexi.say "I was just supposed to show him a good time like all the rest."
        lexi.say "Then hand his wallet over to Danny and forget about him."
        lexi.say "But there was...well, there was just something different about him."
        lexi.say "Yeah, yeah, yeah - I know what you're thinking!"
        lexi.say "Sure his cock was pretty big and he knew how to use it."
        lexi.say "But that's more common than you might think."
        lexi.say "And yeah, everyone gets pissy when you rip them off like that."
        lexi.say "But with [hero.name] there was something different."
        lexi.say "It was like, of course he was pissed."
        lexi.say "But he was pissed with me for not being better, you know?"
        lexi.say "He never ratted me out to the cops."
        lexi.say "And he could look me in the eye when I saw him again."
        lexi.say "It was then that I...I started to really like the guy!"
        lexi.say "The only thing between us was Danny..."
        lexi.say "I was worried that he might hurt, [hero.name]."
        lexi.say "But in the end, it was the other way around!"
        lexi.say "[hero.name] put Danny right on his ass - got rid of him for good!"
        lexi.say "I did wonder if he'd stop me doing that kind of thing anymore."
        lexi.say "I dunno..."
        lexi.say "Going straight might have been kinda nice..."
        lexi.say "But when he took over as my pimp, I soon forgot about all that."
        lexi.say "Because [hero.name] turned out to be the best pimp a girl could want!"
        lexi.say "Sure, Danny had the muscle and he wasn't dumb."
        lexi.say "But [hero.name]'s like a genius or something!"
        lexi.say "And even better, he'd never treat me as bad as that scumbag did."
        lexi.say "[hero.name] has all kinds of new ideas too."
        lexi.say "The kind of stuff that Danny would never have thought of - not in a million years!"
        lexi.say "We're making so much money together now that he jokes we'll soon need an accountant!"
        lexi.say "I don't know what an accountant does exactly."
        lexi.say "But I do know that needing one means you're legit!"
        lexi.say "And it's not all business - fuck no!"
        lexi.say "[hero.name] and I are in love, and it's for real."
        lexi.say "He may pimp me out to the highest bidder and live off of the profits."
        lexi.say "But I know that he's only doing it for the sake of the business."
        lexi.say "That's why I'd have been dumb to turn him down when he asked me to marry him."
        lexi.say "So now he's my pimp, my husband and my best friend, all rolled into one!"
        if lexi.flags.mikeBabies or lexi.is_visibly_pregnant:
            lexi.say "And if he didn't love me, he'd never have started a family with me."
            lexi.say "Ever since Chantel and Tyrone arrived, [hero.name]'s been the perfect daddy to them."
            lexi.say "He adores those two little rascals, you can see it in his eyes whenever he looks the pair."
        else:
            lexi.say "And if he didn't love me, he'd never have set up a home with me."
            lexi.say "Yeah, that's right - I moved out of the trailer park and into an actual house with [hero.name]!"
            lexi.say "Sure, some of the neighbours don't seem to like what they see when I'm lounging by the pool."
            lexi.say "But screw them anyway - who cares about what they think?"
        lexi.say "Hmm...you know what?"
        lexi.say "Now that I think of it..."
        lexi.say "All of that does kind of sound like a fairy-tale."
        lexi.say "So maybe I am some kind of a princess after all?"
        lexi.say "Just the sexy kind."
        lexi.say "The kind that you can rent her ass at an hourly rate!"

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not lexi.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_14
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_14
    $ game.set_new_game_plus()
    $ renpy.full_restart()


label lexi_sasha_dance:
    scene bg nightclub at center, zoomAt(1.25, (480, 880))

    $ previous_sexy = lexi.flags.sexydate
    $ previous_slutty = lexi.flags.sluttydate
    $ lexi.flags.sexydate = False
    $ lexi.flags.sluttydate = False
    show lexi date nophone zorder 1 at center, zoomAt(1.25, (640, 880)), slide(45, 1.5)
    show layer master at lparty
    with fade
    "I have to confess that there's nothing I love more than getting into a club and onto the dance-floor with Lexi."
    "You can pay good money to watch a girl wrap herself around a pole or give you a pretty nice lap-dance."
    "But dancing with Lexi is like having the best of both those things all at once - for free."
    "And the best thing of all is that the girl doing it won't get mad if you put your hands on her either."
    "In fact, she's more likely to take issue with you not doing that!"
    "Almost as soon as we're through the doors and into the club, Lexi make straight for the dance-floor."
    scene bg nightclub
    show dance lexi date at slide(10, 0.7)
    show layer master at lparty
    with fade
    "And thanks to the fact that she's holding my hand in a vice-like grip, so do I."
    "There's not even time for me to take a look around or see if I recognize the song that's playing."
    "As whatever it is, Lexi's already moving to the beat."
    "Well, that and she's moving against me at the same time!"
    "As she wraps her arms around my neck, Lexi starts to grind against me in time to the music."
    "And ironically, that's how I recognize it as a track that I know pretty well."
    "It's a heavy, industrial metal track that has the filthiest lyrics imaginable."
    "All of which just feels so right for Lexi and what she's doing to me right now."
    "Not to mention the effect that her efforts are having too!"
    "Like the music, the club is a dark and noisy affair, playing metal and other heavy kinds of music."
    "This means that Lexi's pretty much all I can see on the dance-floor."
    "And that's fine with me, as I look down to see her pressed against me."
    scene bg nightclub at center, zoomAt(1.5, (480, 1050)), blur(5)
    show lexi kiss date at slide(30, 1.0)
    show layer master at lparty
    with fade
    "Her mouth is coming towards mine, her tongue snaking out for a kiss."
    "Her breasts are pushed up by her top so much that they could pop out at any moment."
    "I angle my head down, already able to imagine the feeling of Lexi's tongue, darting between my lips..."
    "It's at that very moment I feel something come between us, leaving me dumbstruck and open-mouthed."
    "All I can see at first is a blur of pale skin and dark clothes."
    "But I feel the warmth of another body pressing close, pushing Lexi aside."
    scene bg nightclub
    show 3dance_mike
    show 3dance_girl_lexi at slide(10, 0.9)
    if lexi.is_visibly_pregnant:
        show 3dance_pregnancy_lexi_pregnant at slide(10, 0.9)
    if lexi.is_collared:
        show 3dance_collars_lexi_collar at slide(10, 0.9)
    show 3dance_girl_sasha at slide(10, 0.8)
    if sasha.is_visibly_pregnant:
        show 3dance_pregnancy_sasha_pregnant at slide(10, 0.8)
    if sasha.is_collared:
        show 3dance_collars_sasha_collar at slide(10, 0.8)
    if sasha.flags.boobjob:
        show 3dance_sasha_boobjob at slide(10, 0.8)
    if sasha.flags.haircut:
        show 3dance_haircuts_sasha_haircut at slide(10, 0.8)
    show layer master at lparty
    with fade
    "It's only when I finally catch sight of the flashing eyes and smiling lips that I recognize Sasha."
    "Of course, this is one of the clubs that she likes to frequent."
    "And we may have been here together before now, but the memory somehow eluded me."
    "Or maybe I brought Lexi here with the unconscious knowledge we might run into Sasha..."
    "Either way, Sasha seems to have been inspired to go head-to-head with Lexi."
    "That said, she doesn't even try to copy the other girl's obvious style of flaunting herself."
    "Instead, Sasha seems to have become some kind of black-hearted banshee on the dance-floor."
    "She wraps one hand around the back of my neck, hanging her weight off of me."
    "At the same time, her free hand strokes the side of my face."
    "And then it travels steadily downwards, eventually passing below my waist."
    "I feel Sasha cup and then squeeze my cock, her mouth stretching into a smile as she does so."
    "The flashing, strobing lights above make her skin seem to glow with an ethereal quality."
    "And her bared teeth make her resemble a vampire, intent upon feeding from its next willing victim."
    "It's then that Lexi makes a spirited effort to push her way back into my attentions."
    "She succeeds only in jostling Sasha aside a little, but manages to gain all of the other girl's attention."
    "The way that Sasha looks at Lexi only serves to make her look all the more like a gothic succubus."
    "And I see the same impression actually make Lexi quail and draw back a little."
    "But then Sasha seems to eye her up in the same way, and reaches out to pull her even closer."
    "I recognize the way that Lexi flushes and trembles at this."
    "Sasha did the very same thing to me only moments before."
    "And so that's how we end up dancing in a three-way embrace."
    "Unable to choose between the two girls, I simply choose not to."
    $ lexi.flags.sexydate = previous_sexy
    $ lexi.flags.sluttydate = previous_slutty
    return

label lexi_sasha_fuck:
    "Everything just seems to be going right for me tonight, like I'm on a winning streak or something."
    "The nightclub that we're in has the best atmosphere that I can remember for a really long time."
    "Everything the DJ plays is a track that I know and actually like dancing to."
    show dance sasha with dissolve
    "And on top of all that, Sasha's in the mood to dance really close to me."
    "By which I mean REALLY close!"
    "As she presses herself against me and grinds away, there can't be as much as an inch between us."
    "Which makes what happens next all the more impressive."
    show dance lexi with dissolve
    "Because when I next look down, expecting to see Sasha, I'm greeted with the sight of Lexi instead!"
    "I had no idea she was on the dance-floor at all, let alone anywhere near Sasha and I."
    "But somehow she's managed to wedge herself between us, as if trying to push the other girl out of the way."
    "Maybe the right thing to do would be to go right back to dancing with Sasha alone."
    "Or even to make a point of telling Lexi off for cutting in like that."
    "But a quick glance at Sasha's face tells me that neither of those will be required of me."
    "Instead of looking irritated or annoyed at having some competition, she simply smiles to herself."
    hide dance
    show 3dance lexi sasha
    with dissolve
    "And then she redoubles her own efforts, managing to push her way back into the fray."
    "Pretty soon I find myself caught in the orbit of both girls, unable to escape even if I wanted to."
    "I know full well how filthy Lexi can get in a situation like this."
    "But Sasha seems to be pulling out all the stops, giving her some serious competition."
    "Even as Lexi begins to shake her ass in front of me, I can feel Sasha pressing up close from behind."
    "A moment later, I have buttocks working against my groin and another groin doing the same to my own ass too!"
    "The girls begin to circle me then, making me feel like I'm being stalked by a couple of she-wolves."
    "Lexi pushes her breasts towards me, shaking them so that they bob and bounce the whole time."
    "And Sasha flashes her legs and ass at me, taking advantage of the short skirt she's wearing."
    "If this is a contest to see which of them can outdo the other, then they need a more impartial judge."
    "All I can do is follow them with what feels like ever more clumsy steps of my own."
    "One moment I can't take my eyes off of Sasha, and the next Lexi cuts in and leads me off by the nose again."
    "I don't know how long this goes on for, as I begin to lose track of time."
    "And I actually start to worry that my already stiff cock is starving my brain of oxygen."
    "This means that I only snap out of it when I see Lexi and Sasha start to slow their dancing down."
    "While neither of them stops completely, it's clear to see that something's just changed between them."
    "And then I realize what it is - they're not competing anymore."
    "For some unknown reason, they've stopped pitting their dirtiest moves against each other."
    "As soon as they're close enough, Lexi leans over to whisper into Sasha's ear."
    "I only have time to see this result in a giggle and an enthusiastic nod."
    hide 3dance
    show sasha date at right5
    show lexi date at left5
    with dissolve
    "And then they each grab one of my hands and literally haul me off the dance-floor."
    "They take me so completely by surprise that I can't even begin to make a show of resistance."
    "Not that I really want to stop myself being dragged off by the pair of them, you understand."
    "But this also means that they have the upper hand when I finally see where they're taking me."
    mike.say "Ah, girls..."
    mike.say "I'm pretty sure that's the ladies bathroom!"
    "All this gets me is another round of giggling and snickering from Lexi and Sasha."
    scene bg restroom
    show sasha date at right5
    show lexi date at left5
    with fade
    "They exchange conspiratorial glances as they shove me through the door and hurry after."
    "Mercifully, once we're inside, I see that the bathroom is empty."
    "For the moment at least, the three of us are alone in here."
    mike.say "Okay, okay..."
    mike.say "Sasha, Lexi...you've had your fun."
    mike.say "But the joke's over."
    "I go to walk between them, making for the door back into the nightclub."
    "But as soon as I'm within reach, they seize my arms and fling me back again."
    sasha.say "Not so fast, [hero.name]!"
    lexi.say "Yeah - where do you think you're going in such a hurry, huh?"
    mike.say "Out of here."
    mike.say "Before someone tells security and I get tossed out of the club and onto my face!"
    "I watch as both of the girls shakes their heads and tut in apparent disappointment."
    "Apparently that wasn't the answer they were looking for."
    sasha.say "You need to understand that this is the girl's bathroom."
    lexi.say "And in here, we're the ones that set the rules, [hero.name]!"
    sasha.say "So you're not going anywhere until we say so."
    mike.say "Ah...I see."
    mike.say "And what exactly is going make that happen?"
    lexi.say "Way I see it, we just put on quite a performance out there."
    sasha.say "And all of it just for you."
    lexi.say "So we want to be paid back in kind."
    mike.say "Y...you mean..."
    sasha.say "What we mean, [hero.name], is that you're going nowhere."
    sasha.say "Not until you put on a performance for us."
    "With that, they begin to shove me back again."
    "But this time it's with more force and a particular direction in mind."
    "Between them, Lexi and Sasha succeed in pushing me into the nearest cubicle."
    "I stagger the last couple of steps backwards, landing noisily on the toilet."
    "Then I hear the sound of the bolt being shot, sealing me in there with the pair of them."
    scene nightclub 3bj with fade
    "It's only as Lexi and Sasha get down on their knees that I feel my mood starting to change."
    "And as they tug my pants and shorts down to my ankles, I'm already thinking this might actually be worth the risk."
    show nightclub 3bj dick
    "So much so that I'm not really put off when my cock springs up in front of them and earns another round of giggles."
    "Especially when they both lean forward and start to lick at it with their tongues."
    "All I can do is sit back on the toilet, bracing my arms against the sides of the cubicle."
    "As something tells me that I'm going to have to hold on tight during this ride..."
    "I'd expected one of them to take the lead with the licking and the other to maybe tickle my balls."
    "But instead, both Lexi and Sasha keep right on licking away."
    "Although it soon becomes apparent that Lexi's claimed the top end for herself."
    "I watch as she takes my head into her mouth, savoring every little bit that goes in there."
    "Not to be outdone or pushed into second place by this, Sasha takes my balls firmly in her hand."
    "I feel her start to squeeze them as her tongue keeps right on licking at my shaft."
    "At the same time, Lexi's already started taking my cock pretty deep into her mouth."
    "Her head bobs up and down in my lap, and she shows no sign of gagging as she does so."
    "In the end, she has so much of the length in her mouth that her lips come close to touching Sasha's tongue!"
    "With the sensations that she's giving me and the sounds that she's making, Lexi's sure to make me cum."
    "But then, before she can push me over the edge, she's unceremoniously pushed aside."
    "For a moment, I think that Sasha's going to make straight for my cock as she gets up from the floor."
    "So you can imagine my surprise when she pushes me aside as well, and clambers onto the toilet herself."
    scene nightclub threesome
    "As soon as her knees are on the seat, Sasha reaches back and yanks down her tights and panties."
    "Her voice is breathy, so that she sounds like she's almost panting as speaks."
    sasha.say "[hero.name]..."
    sasha.say "I need...your cock."
    sasha.say "Please...put it in me!"
    show nightclub threesome mike
    "Normally there'd be nothing on this earth that could stop me from giving Sasha exactly what she wants."
    "But right now there are other people to think about too."
    "I glance at Lexi, who's now getting up off of the floor herself."
    lexi.say "Don't look at me, [hero.name]."
    lexi.say "You should know it's rude to keep a lady waiting..."
    "All I can do is shrug at this, getting ready to oblige."
    "But then Lexi catches me off guard by climbing onto the toilet too!"
    show nightclub threesome lexi
    "She straddles Sasha's back, facing me and smiling at my all too evident surprise."
    "Pointing to Sasha's exposed ass, she nods and raises her eyebrows."
    lexi.say "Don't just stand there staring at me, [hero.name]."
    lexi.say "Get on with it - make with the cock already!"
    "Starting to feel a little bit like a resident at a stud farm, I start to do as I'm told."
    menu:
        "Fuck Sasha's ass" if sasha.flags.sexydate or sasha.flags.sluttydate:
            "But even though I'm the one being ordered about here, it doesn't mean I have to be predictable."
            "That's why I part Sasha's buttocks just enough before I thrust my cock between them."
            "If she realizes what I'm doing at all, then it's at the very last moment and too late to protest."
            show nightclub threesome anal sashamoan
            "Because a second later I push the head of my cock straight into the puckered hole of her ass."
            "Sasha lets out a strange sound that's half yelp and half moan."
            "But there's nothing that she can do to keep it from sinking ever deeper into her."
            "As if puzzled by the sounds that the other girl's making, Lexi glances downwards."
            lexi.say "[hero.name], you sly dog!"
            lexi.say "You'd better hope her ass is up to taking all of that meat in one go!"
            "Rather than distracting me, I find that Lexi's taunts are actually spurring me on."
            "And so I start to thrust in and out of Sasha's ass with as much energy as I can summon."
            "In turn, this makes her moans become all the more loud and frantic."
            "Which, of course, only serves to make me more eager to pound her that much harder."
            "It's almost as if the three of us are so much more potent as a threesome."
            "Like Sasha's body makes me so very hot to begin with."
            "But Lexi's presence serves as a weird catalyst, pushing it over the top."
            "I know I should be paying more attention to Sasha as I fuck her ass."
            "And yet I can't help locking eyes with Lexi as I do so."
            "Her face is so full of wicked delight that I feel fixated on it."
            "Lexi pushes her hand down her shorts as she rides Sasha's back."
            "And I just know that she's playing with her pussy the whole time."
            "Then she pulls those same fingers back out, and licks them slowly."
            "Feeling like I've been hypnotized, I yank my cock out of Sasha's ass."
            "Her moans become tinged with sudden disappointment, but I'm not listening."
            show nightclub threesome suck
            "Instead I watch as Lexi leans forward and begins to suck on my dick again."
            "She doesn't seem in the least bit concerned at where it's just been."
            "Which of course only serves to make what she's doing that much hotter."
            show nightclub threesome sashanormal
            "Lexi sucks and licks away, also paying no attention to Sasha's quivering beneath her."
            "But the difference this time is that I'm already pretty close to cumming."
            "I have maybe a couple of seconds at the most to decide how I want to finish this thing..."
            menu:
                "Cum in Lexi's mouth":
                    "There's no chance I can pull my cock out of Lexi's mouth in time."
                    "And it's not like I really want to stop what she's doing either."
                    $ lexi.sub += 5
                    show nightclub threesome cum with hpunch
                    "So I wait until the very last moment possible, and then push it further in."
                    with hpunch
                    "This takes Lexi by surprise, making her cough and splutter around the shaft."
                    with hpunch
                    "But she's the kind of girl that's long since managed to conquer her gag reflex."
                    with hpunch
                    "Which means that she manages to hold on as I shoot my entire load at the back of her throat."
                    "I pull my cock out of her mouth as she chokes it all down."
                    "Leaving glistening strings of cum between her lips and the head."
                "Cum inside of Sasha's ass":
                    "I steal a glance at Sasha as she keeps on moaning like a wounded animal."
                    "And the thought of leaving her in a state like that is just too much."
                    show nightclub threesome fuck anal sashamoan
                    "So I pull my cock out of Lexi's mouth and push it hastily back up Sasha's ass."
                    "The muscles up there haven't had time to recover, and Lexi's spit makes it nice and slippery."
                    "This means that I'm back up there before Sasha truly realises what's happening to her."
                    "Her moans resume once more, quickly returning to the sounds she was making while I fucked her before."
                    "Lexi looks at me, her mouth hanging open and something that could be shock in her eyes."
                    $ sasha.sub += 5
                    show nightclub threesome cum sashaahegao with hpunch
                    "But by then I'm already cumming, and that takes up all of my attention."
                    with hpunch
                    "After the last few thrusts into Sasha's ass, I pull out."
                    with hpunch
                    "Leaving glistening threads of cum stretching from her ass to the tip of my cock."
                "Cum over Lexi and Sasha's faces":
                    "What a dilemma - do I disappoint Lexi or Sasha?"
                    "If my cock goes off in the former's mouth or the latter's ass, one's getting a raw deal."
                    "So lacking any other choice, I pull my cock out of Lexi's mouth before I cum."
                    "She looks at me askance, just at the same moment that Sasha turns her head to gaze back over her shoulder."
                    show nightclub 3bj dick
                    "I have just enough time to grab both of them and throw them on the ground."
                    $ sasha.sub += 2
                    $ lexi.sub += 2
                    show nightclub 3bj cumshot with vpunch
                    "This means that when my cock finally erupts, both of them are in the line of fire."
                    show nightclub 3bj cum with vpunch
                    "The cum hits Lexi first, making her reel back and pull a pretty amusing face."
                    with vpunch
                    "But I aim the rest to spatter straight into Sasha's unsuspecting features."
                    show nightclub 3bj kiss
                    "Both of them get a pretty good painting with the sticky, glistening streamers."
                    show nightclub 3bj -dick
                    "Still frozen in surprise as it begins to run slowly down their faces."
            $ sasha.flags.anal += 1
        "Fuck Sasha's pussy":
            "Sure, it might look and sound like I'm being pushed around by Lexi and Sasha right now."
            "But it's not as though they're demanding that I do anything I wouldn't do given the chance anyway."
            "And any opportunity to get inside of Sasha's pussy is one that's definitely worth taking."
            show nightclub threesome vaginal sashamoan
            "So that's why I don't hesitate to step up and push my cock straight between her lips."
            "I don't need to hear the way that Sasha moans and pouts to know that she wants it in her."
            "She's already pretty slick down there, letting me slip inside without any serious effort at all."
            "As my cock sinks into Sasha, Lexi looks down, an impish smile spreading across her face."
            lexi.say "Mmm..."
            lexi.say "I just LOVE that sound!"
            lexi.say "All squishy and sticky!"
            "I know that I should be giving all of my attention to fucking Sasha."
            "But there's just something so wonderfully filthy about Lexi's mouth."
            "I'm pretty sure that Sasha can't hear what she's saying either."
            "As she keep on moaning as I begin to pound her even harder."
            "And as good as it feels to have my cock this deep inside of Sasha..."
            "Almost without thinking, I feel myself pulling out of her pussy."
            "At the same time I grab the back of Lexi's head with one hand."
            "The moment that I have my cock out of Sasha, I pull the other girl's head straight down."
            show nightclub threesome suck
            "Lexi doesn't even have time to realize what's happening before it's deep in her mouth."
            "Her eyes go wide in genuine surprise, but then her instincts kick in."
            "It's as if she switches into auto-pilot, licking and sucking with serious gusto."
            "Apart from talking dirty, there's no better way for Lexi to use her mouth."
            "And now that she's silent, I can actually hear the sounds that Sasha's making too."
            show nightclub threesome sashanormal
            "Her moans have now taken on a more plaintive tone."
            "And I'm sure that she's none too happy at being deprived of my cock on such short notice."
            "The problem is that the blowjob that I'm getting out of Lexi is pretty fucking incredible."
            "Add to that the fact that I'm dangerously close to cumming too."
            "I have to make a hard decision, and decide who's going to get it when it comes..."
            menu:
                "Cum in Lexi's mouth":
                    "I don't think there's even time to pull my cock out of Lexi's mouth."
                    "Well, that and the fact that I don't exactly want her to stop!"
                    "But just to make doubly sure, I shove it as far in as it'll go."
                    $ lexi.love += 5
                    show nightclub threesome cum with hpunch
                    "Even as good as she is at this kind of thing, Lexi still coughs and splutters."
                    with hpunch
                    "Thankfully her suppressed gag-reflex has been tamed enough to cope."
                    with hpunch
                    "And that's a relief as she takes the entire thing straight down the back of her throat."
                    "She's still gulping it down as I pull my cock from between her lips."
                    "Leaving glistening strings of cum between her tongue and the tip."
                "Cum inside of Sasha's pussy":
                    "I can't help being affected by the sounds that Sasha's making."
                    "And it just doesn't seem fair to leave something like that unfinished either."
                    "So before I can get second thoughts, I yank my cock out of Lexi's mouth."
                    "Her spit makes it nice and slippery, so I can slide straight back into Sasha."
                    show nightclub threesome fuck vaginal sashamoan
                    "This means that I'm balls deep before she even knows what's happening."
                    "Sasha's moans begin to rise in volume and intensity once more."
                    "But Lexi looks at me, her mouth still hanging open and shock in her eyes."
                    $ sasha.love += 5
                    show nightclub threesome cum sashaahegao with hpunch
                    "Not that I can do anything about it, as it's just then that I finally cum."
                    with hpunch
                    "I fill Sasha completely, semen dripping from her pussy before I've even thought of pulling out."
                    with hpunch
                    "And when I do, it leaves glistening threads of cum stretching from her pussy to the tip of my cock."
                "Cum over Lexi and Sasha's faces":
                    "Never in my entire life have I wanted to have two cocks as I do right now!"
                    "If my cock goes off in either mouth or pussy, someone's getting a raw deal."
                    "So I figure that it's better to slightly disappoint them both, rather than thoroughly piss one of them off."
                    "Lexi stares at me in surprise as I pull my cock out of her mouth."
                    "And Sasha chooses that same moment to look back over her shoulder."
                    show nightclub 3bj dick
                    "I barely enough time to maneuver both of them into position on the ground."
                    $ lexi.love += 3
                    $ sasha.love += 3
                    show nightclub 3bj cumshot with vpunch
                    "Now both of them are right in the line of fire."
                    show nightclub 3bj cum with vpunch
                    "It hits Lexi first, making her grimace as she's covered in the white stuff."
                    with vpunch
                    "The next few shots spatter across Sasha's face and into her open mouth."
                    show nightclub 3bj kiss
                    "Both of them get a pretty good covering of sticky, glistening streamers."
                    show nightclub 3bj -dick
                    "And their faces remain rigid as it begins to run down their cheeks and drip from their chins."
    "There's no time to hang around and enjoy the afterglow once we're done."
    "As it suddenly begins to dawn on us how lucky we were not to get caught in the act."
    "Everyone pulls their clothes back on and hurries to clean up the best that they can."
    show bg restroom with fade
    show sasha at right
    show lexi at right4
    with moveinright
    "Sasha and Lexi open the cubicle door as I stand back to keep from being seen."
    show sasha at right5
    show lexi at left5
    with ease
    "But thankfully our luck holds, and the coast's clear for us to run out of there."
    "Still trying to look nonchalant and natural, we head straight back to the dance-floor."
    show bg nightclub
    show sasha happy at right5
    show lexi happy at left5
    with fade
    "Once we're there, I notice that a lot of the fire's gone from Lexi and Sasha's dancing."
    "Don't get me wrong, they're neither tired out nor boring to be around."
    "It's just that the fire seems to have burned down to glowing embers instead."
    "The three of us dance together for what feels like a really long time."
    "But now it's more like we're satisfied and sated than before we took the chance sneak into the bathroom."
    "There's no trying to outdo each other, and I feel like everyone's somehow more connected than before."
    "Who knows - maybe we've found the perfect balance as a threesome..."
    $ sasha.sexperience += 1
    $ lexi.sexperience += 1
    return

label lexi_slave_request:
    show lexi
    mike.say "Lexi, what's wrong?"
    mike.say "You're really starting to freak me out right about now!"
    show lexi surprised
    "Lexi chuckles and cocks her head on one side, a quizzical look on her face."
    show fx question
    lexi.say "Huh?"
    lexi.say "What're you talking about, [hero.name]?"
    mike.say "Lexi, first you drop off the radar for days on end, no calls, no texts, no nothing."
    hide fx
    mike.say "Then you call me up, out of the blue and ask me to come over her, and you're being super sweet and nice."
    mike.say "That's not the normal you, and I know the normal you...hell, I kinda adore the normal you!"
    show lexi blush sad
    "Lexi actually blushes a little, looking away as though she can't meet my eye."
    "That's scary too, as I've never seen this girl blush before, no matter what was going on at the time."
    lexi.say "Ah...it's not easy for me to say..."
    mike.say "Try, Lexi...I'm listening."
    show lexi annoyed
    lexi.say "Well, you know how we saw that Sasha chick when we were out shopping the other day?"
    "The first time my girlfriend on the side met my slave - how could I forget?"
    mike.say "Yeah...I do."
    lexi.say "And do you remember what we talked about after?"
    "Ah, of course...now it starts to make some kind of sense!"
    mike.say "Yeah, Lexi...I remember that as well."
    lexi.say "I've been thinking a lot about it...about what you said I could be..."
    mike.say "You've been thinking about whether or not you want to be my slave too...just like Sasha already is?"
    "Lexi nods, still unable to meet my eye."
    lexi.say "Yup, just that."
    lexi.say "And I think...that is to say that...I want to."
    "She still can't quite bring herself to say the actual word out loud."
    mike.say "You want to be what, Lexi?"
    mike.say "Come on, out with it - you can't truly become it, not if you can't say it to my face."
    "Slowly, Lexi looks up and manages to meet my eye."
    "It's hard to believe that she's this shy and maybe even scared of something after all."
    show lexi normal
    lexi.say "[hero.name], I want...I want to be your...slave."
    lexi.say " I want to be your slave."
    "I get the feeling that Lexi repeats herself as much for her own benefit as mine."
    menu:
        "No":
            mike.say "I have to be honest, Lexi - I don't think that'd be a good idea."
            show lexi sad
            "Lexi keeps up the theme of unfamiliar facial expressions, now showing crestfallen disappointment."
            lexi.say "But...but why not?"
            lexi.say "We've done all kinds of crazy shit since we hooked up!"
            lexi.say "And I'm well used to doing as I'm told...it comes with being pimped out for so long!"
            "I sigh at her words, not liking being forced to make the admission that's coming next."
            mike.say "That's part of the problem, Lexi...this is different to what you've known before."
            lexi.say "How?"
            mike.say "Back then you were obeying Danny because he controlled you, beat you, even threatened to kill you."
            mike.say "You were afraid of him, Lexi."
            mike.say "This kind of master and slave relationship isn't like that - it's based on trust."
            mike.say "I don't want to become like Danny, and I really don't want to see you go back to being afraid of someone who should love you."
            mike.say "Lexi, I've fallen for who you've grown into since we got rid of that sack of snake feces."
            mike.say "I won't stifle that person for the sake of getting freaky or having you give me an ego rub."
            "Lexi looks even more disappointed now, but as the meaning of my words sinks in, she begins to smile weakly."
            show lexi normal
            lexi.say "You...you really mean that...that you like me just the way I am?"
            mike.say "Yeah, Lexi - you're honest, uninhibited and I have more fun than I could imagine with you already."
            mike.say "I don't want to change you, or for you to change for me."
        "Yes":
            if lexi.sub.max < 90:
                $ lexi.sub.max = 90
            mike.say "I don't know, Lexi - are you ready to devote yourself to me, mind and body?"
            show lexi happy
            "Lexi nods eagerly at the question."
            mike.say "Are you able to obey me, without question, no matter what I ask of you?"
            "She nods again."
            mike.say "Will you submit yourself willingly to any punishment that I decide you deserve?"
            "I see Lexi almost shiver at the mention of punishments, but she nods all the same."
            mike.say "Lexi, can you accept me as your one and ONLY master?"
            show lexi blush
            "Lexi's cheeks are almost burning now, but I can't tell if from embarrassment or arousal."
            mike.say "Alright then...if you can promise me all of that, then I can accept you as my slave."
            show lexi normal
            "Lexi sits with her hands in her lap, looking up at me eagerly, waiting to be given her first command as a slave."






            lexi.say "Th...Thank you...M...M...Master..."
            "There's a sense of anticipation in her words, and one of release as well."
            "Maybe Lexi's been longing for something like this to happen to her for a very long time and just didn't know it."
            $ lexi.status = "sex slave"
    $ hero.cancel_activity()
    return

label lexi_sasha_1:
    scene bg mall1
    show lexi
    with fade
    lexi.say "Hey, I wanna look in here!"
    mike.say "Erm...I didn't think that whole goth thing was your bag."
    lexi.say "Maybe I want to try something new...they got straps, spikes and stuff like that too."
    show lexi wink
    lexi.say "Don't tell me you wouldn't like to tie me up and spank me?!?"
    hide lexi with moveoutright
    scene bg clothesshop with fade
    show lexi happy at left with moveinleft
    "Before I can come up with another lame excuse, Lexi's already dragging me towards the store entrance."
    "I can't protest any louder for fear of making a scene or letting Lexi know what's the real source of my reluctance."
    "At the same time, I don't want Sasha to hear my voice either."
    "I try to hang back a little, as Lexi busies herself digging through items of clothing in black and conspicuously made of rubber."
    "Just as I'm beginning to think that Sasha might be on a break or tied up in the back of the store, I hear the inevitable sound of her voice behind me."
    show sasha at right with dissolve
    sasha.say "Oh, hey [hero.name], haven't seen you in here before."
    sasha.say "What's up?"
    mike.say "Hey, Sasha - I was just in the mall, and I guess I thought I'd say hello."
    show sasha annoyed
    "Sasha suddenly notices Lexi, and I can see her eyes sweeping over the other girl in harsh judgement."
    sasha.say "Urrgh...we get one of these every so often."
    sasha.say "Refugees from the discount stores or Goodwill by the pound!"
    "I grin nervously, thinking that if Lexi stays put, maybe I can wrap up talking to Sasha before either sees the other or knows I know them too."
    show lexi normal at left5 with ease
    lexi.say "Hey, [hero.name] - this one's got a hole in the crotch!"
    lexi.say "That's gotta be for fucking, right?"
    show sasha shocked at right5 with ease
    "Sasha fixes me with an almost horrified stare as Lexi bounds over, clutching something shiny and unbelievably small in her hands."
    "Suddenly, both of them are looking at each other, and then back at me."
    show sasha annoyed
    "Feminine instinct means that they both know something's up."
    "And they're evidently waiting for me to attempt an explanation to clear everything up neatly in a package."
    "Probably with a bow on top too."
    if not sasha.is_sex_slave:
        show sasha angry
        mike.say "Ah, Lexi...meet Sasha!"
        mike.say "She's...my housemate."
        "While Lexi doesn't seem to initially pick up on the awkward tone of my voice, Sasha's eyebrows raise significantly at being described as nothing more than my housemate."
        lexi.say "Oh, hey there, Sasha!"
        show sasha normal
        sasha.say "Hello...Lexi...how do you know [hero.name] here?"
        lexi.say "Well, it's kind of romantic, you know?"
        sasha.say "Really?"
        lexi.say "Oh yeah - we met in a club one night, and he saw off my old boyfriend, who was also kinda my pimp at the time."
        sasha.say "You don't say?"
        show lexi happy
        lexi.say "I do...and now we're fuck buddies!"
        show sasha happy
        sasha.say "Wow - it's like some kind of fairy tale come true."
        "Lexi nods, apparently unaware of the sarcasm dripping from Sasha's words."
        show lexi at left with ease
        "She returns to browsing the racks, blissfully unaware of what's happening just out of earshot."
        mike.say "Sasha...I can explain..."
        show sasha angry
        sasha.say "Really, [hero.name]?"
        sasha.say "Because if you can, I want to hear it."
        sasha.say "It must be some really crazy explanation."
        "I begin to open my mouth, but then my shoulders sag as I realize the game is up."
        show sasha annoyed
        sasha.say "Oh, [hero.name] - I'm not mad...just disappointed, I guess."
        sasha.say "I thought what we had was good, that it was enough."
        $ sasha.love -= 25
        $ sasha.flags.cheated = True
        show sasha sad
        sasha.say "Looks like it was only good enough for me."
        hide sasha with moveoutright
        "We linger around for a few more minutes, until Lexi's done browsing."
        scene bg mall1
        show lexi normal
        with fade
        "Back out in the mall, she seems to sense that there's something wrong."
        show lexi surprised
        lexi.say "Blowjob for your thoughts?"
        mike.say "What...oh, yeah - I think I just went and ruined my relationship with Sasha back there."
        lexi.say "How come?"
        mike.say "Well...I guess I wasn't being strictly honest when I said that she was just my housemate, if you get what I mean!"
        lexi.say "Yeah, I kinda got that vibe off of her...I just didn't want to rub your nose in it."
        mike.say "You're not mad at me?"
        show lexi normal
        "Lexi laughs in a snorting, unselfconscious manner that speaks of her easy sexuality and basically honest nature beyond her initial appearance."
        show lexi annoyed
        lexi.say "[hero.name], you think that Danny didn't screw around with whatever took his fancy?"
        lexi.say "He couldn't have given a shit, and he was beating the hell out of me at the same time, too!"
        show lexi surprised
        lexi.say "So you fucked this Sasha bitch, so what?"
        lexi.say "You can keep on doing it, if she'll let you, for all it bothers me."
        show lexi happy
        lexi.say "Gimmie the choice between a good guy that fucks another woman on the side and a bastard that does the same and hits me, and I'll take you every time."
        lexi.say "And if the raging bitch can't learn to share, then fuck her."
        show lexi wink
        lexi.say "Because you can always fuck me instead!"
    else:
        show sasha normal
        if lexi.sub.max < 50:
            $ lexi.sub.max = 50
        if sasha.flags.mikeNickname:
            sasha.say "Who is this, [hero.name]?"
            "I don't immediately answer, instead watching Lexi's response to the other girl's submissive posture and term of address."
        else:
            "After a brief moment Sasha bows her head slightly."
            sasha.say "Who is this, [hero.name]?"
            "I don't immediately answer, instead watching Lexi's response to the other girl's submissive posture."
        "She looks at Sasha's downcast gaze, then at me with a puzzled expression on her face."
        mike.say "This is Lexi, Sasha - another girl that I've been fucking at the same time as you."
        sasha.say "Oh, I see."
        sasha.say "Does she please you, [hero.name]?"
        show lexi blush
        mike.say "She satisfies me, yes...but she's not as obedient as you."
        show sasha happy
        show lexi surprised at left5, vshake
        "Lexi notes the instant and sincere smile this last comment elicits from Sasha, her mouth hanging open in genuine surprise."
        mike.say "Are you jealous of Lexi, Sasha?"
        show sasha sad
        "Sasha looks down at the floor for a moment, obviously thinking hard about her answer."
        sasha.say "Yes, [hero.name]."
        show sasha normal
        "She looks up and catches my questioning look."
        sasha.say "But only because she occupies time when I might be pleasuring you myself."
        sasha.say "Maybe...maybe we could both pleasure you at once, [hero.name]?"
        sasha.say "Then we could try to outdo each other in gratifying you, [hero.name]!"
        mike.say "Maybe, Sasha, maybe."
        mike.say "Well, I don't need to talk to you any longer, so you can go."
        mike.say "I may fuck Lexi here before I come home."
        mike.say "But I promise that I'll still have enough energy to do you as well, even if it's just letting you give me a blowjob."
        show sasha happy
        "Sasha nods happily at the last part, turning away and getting back to her work on the shop floor."
        hide sasha with moveoutright
        "I can see Lexi looking at me in what might actually be fascinated awe as we leave."
        "Based on her past with that scumbag Danny, it must be odd to see a woman so obedient and submissive without a hint of violence in the offing."
        show lexi at center with ease
        show fx question
        lexi.say "[hero.name]...what was that back there?"
        if sasha.flags.mikeNickname:
            lexi.say "Why was that Sasha girl talking to you like that...calling you '[sasha.heroname]' all the time?"
        else:
            lexi.say "Why was that Sasha girl behaving like that with you...?"
        mike.say "Ah, I don't exactly advertise it, Lexi...but I've kinda been getting really into BDSM recently...bondage and all that stuff."
        "Lexi nods slowly, clearly turning this revelation over in her mind and getting to grips with how it changes her image of me."
        mike.say "There's really no other way to say it - Sasha's my slave and I'm her master."
        lexi.say "It looks kinda...kinda kinky."
        mike.say "You have no idea, Lexi!"
        "I can see that this whole thing is putting Lexi on the wrong foot."
        "She's clearly so used to being able to shock me with her own outrageous past, that it's made her unsure and more than a little confused."
        lexi.say "Would you...well...would you like me to be like that too?"
        mike.say "You don't have to do it in order to keep me, Lexi."
        mike.say "I won't stop wanting to fuck you just because you're not my slave too."
        mike.say "But if you're interested, then yes...I'd let you be my slave as well."
        mike.say "If I'm honest, your past kept me from bringing it up."
        mike.say "I don't want to turn into Danny 2.0...you know?"
        "Lexi thinks for a couple of minutes, a long time for her to keep from talking, and then slowly shakes her head."
        lexi.say "I don't think it's the same...I don't think you're the same as him, not at all."
        mike.say "Okay, if that's how you feel, we'll give it a shot."
        show lexi happy
        "Lexi smiles in an oddly satisfied manner, and I can't tell if she's genuinely happy or just wanting to outdo Sasha."
        lexi.say "Maybe we can try that thing that Sasha talked about too?"
        if sasha.flags.mikeNickname:
            lexi.say "You know, trying to see who can be the best slave and please the [sasha.heroname] the most?"
        else:
            lexi.say "You know, trying to see who can be the best slave and please you the most?"
        $ game.active_date.score = 100
    "I begin to wonder about the relative merits of Sasha and Lexi."
    "As well as any possible ways they could be convinced to tolerate the presence of the other, now that they know I've been seeing them behind each other's backs."
    $ game.room = "mall1"
    return

label lexi_preg_talk:
    show lexi sad
    "I can sense that there's something up with Lexi almost the moment that I see her."
    "She might be a professional when it comes to using her natural charms to get her way."
    "But she's actually pretty bad at lying when she can't use her hips, ass or chest to her advantage."
    "She's visibly edgy, glancing over her shoulder as she walks up the driveway to the house."
    "When I open the door, she almost darts inside, as if she's afraid of being seen."
    "My mind leaps to the most obvious conclusion imaginable."
    mike.say "What's up, Lexi?"
    if not game.flags.dannydead:
        mike.say "Has that ape Danny been beating you again?"
        show lexi surprised
        show fx question
        lexi.say "What?"
        "Lexi looks startled, but I don't know if it's at the mention of violence or just of a thug like Danny."
        lexi.say "No, no...well, no more than usual."
        hide fx
        "If it were anyone else saying that, I'd have been horrified and telling her to call the police."
        "But then, if it were anyone else, I wouldn't be asking them that question in the first place."
        "It strikes me as odd how quickly I've come to accept the strangeness of Lexi's life as almost normal for her."
        show lexi sad
        "Though her face still looks preoccupied, her body gives out the same vibes as always."
        "I find it hard to make myself look serious and keep from staring at the way her skimpy clothes do nothing to hide her astonishing body."
        mike.say "So, lexi...what's up, for the second time of asking?"
    show lexi blush
    lexi.say "Erm...well...this is kinda hard to say..."
    "It must be bad, as Lexi's never been short of words or afraid of saying whatever comes into her head before now."
    mike.say "Don't worry, you can tell me anything, Lexi."
    show lexi normal
    "She smiles weakly at this, showing that rare honest vulnerability that makes her so much more than the cheap little harlot she seems to be in the outside."
    lexi.say "Well...with what we've been doing...I thought I ought to tell you..."
    "My smile gets ever more pained as I'm convinced that she's about to tell me she's had bad news from the VD clinic."
    lexi.say "I'm pregnant - or I think I am!"
    "My mouth moves, but no words seem to come out."
    pause 2.0
    show lexi annoyed
    lexi.say "Well, say something, for fuck's sake - even if it's something mean about me and the way I live my life, just say something already!"
    "Of all the things I could have imagined her saying, I was not prepared for that."
    mike.say "Wow, Lexi - that's caught me off guard!"
    lexi.say "Well, I thought I'd tell you, 'cos you're the smartest person I know - the least crooked as well."
    mike.say "I guess I should be flattered...wait a minute, Lexi - the kid is mine, isn't it?!?"
    "Any other woman, I'd have expected to confirm the fact within a second."
    pause 2.0
    "But Lexi instead pauses for a moment, as if totting up the chances in her head."
    show lexi normal
    lexi.say "Oh, I'm almost totally certain it's probably yours."
    mike.say "You don't say?"
    show lexi sad
    "Lexi doesn't say anything more, just looks at me with eyes that have never looked so large and pleading."
    "She looks so much like a vulnerable little girl in that moment."
    "I can't help but pick up on the fact that she wants me to tell her what to do, to make it all better for her."
    menu:
        "Tell her to abort":
            mike.say "You can't look after a baby, Lexi - Christ knows you're struggling to look after yourself."
            mike.say "I don't like it, but the best thing would probably for you to abort it now, before it's too late."
            show lexi annoyed
            "Lexi's expression becomes visibly more hopeful, but I can see she wants me to add something more to my advice."
            if hero.money >= 200:
                menu:
                    "Tell her you'll pay for it":
                        $ hero.money -= 200
                        $ lexi.love += 5
                        $ lexi.sub -= 5
                        show lexi happy
                        mike.say "Don't worry about the money, either - it's probably mine, and anyway, it's time someone was nice to you for a change."
                        "Lexi looks at me in a different way to normal, without a hint of calculation or cynicism."
                        "I wonder how often someone in her life as acted in her best interests out of pure affection for her alone."
                    "Don't":
                        $ lexi.love -= 10
                        $ lexi.sub += 5
                        show lexi sad
                        mike.say "The money shouldn't be a problem, not with how good you are at picking pockets and screwing gullible marks over."
                        "Lexi says nothing, just nods meekly, clearly having been expecting more from me."
            else:
                $ lexi.love -= 10
                $ lexi.sub += 5
                mike.say "The money shouldn't be a problem, not with how good you are at picking pockets and screwing gullible marks over."
                "Lexi says nothing, just nods meekly, clearly having been expecting more from me."
            $ lexi.unpreg()
        "Tell her to keep the baby and that you will support her":
            $ lexi.love += 10
            $ lexi.sub += 10
            mike.say "You can look after a baby, Lexi - so long as you have someone to look after you too."
            show lexi surprised
            "Lexi's eyes are suddenly full of what looks like surprise, confusion and not a little fear as well."
            mike.say "Wait a minute, Lexi - before you say no, just hear me out."
            mike.say "You once told me that you live the life you live because you don't have a choice."
            mike.say "Well now I'm giving you that choice, because I think you're worth a hell of a lot more and you're being wasted in the life you're living."
            mike.say "Have the baby, and I'll be right by your side from now on."
            if not game.flags.dannydead:
                mike.say "Fuck Danny and fuck the past - it'll be just us, and whatever we want to make of it."
            else:
                mike.say "Fuck the past - it'll be just us, and whatever we want to make of it."
            "Lexi looks literally stunned, nodding with a blank expression on her face."
            $ lexi.flags.toldpreg = True
    "The apprehension from when she came in gone, Lexi drains her glass as the weight of what we just agreed finally starts to sink in."
    "I can feel the same weight too, and I'm already trying to work it all out inside of my head."
    return

label lexi_bj_alley:
    $ hero_name_upper = hero.name.upper()
    scene bg alley
    lexi.say "[hero_name_upper]...HEY, [hero_name_upper]!"
    "I spin around at the sound of someone shouting my name in the middle of the street."
    "It's pretty late at night right now, and this isn't the best of places to be hanging around."
    "The only thing that keeps me from making a run for it is the fact that the voice is definitely female."
    "It also sounds very familiar, as well as more than a little worse for wear."
    lexi.say "HEY...HEEYYY [hero_name_upper]!"
    lexi.say "It's me!"
    lexi.say "It's Lexi!"
    "If I hadn't just been told in such emphatic terms just who was calling out for me, it'd have soon become clear anyway."
    show lexi happy blush with dissolve
    "Looking over my shoulder, I see the unmistakable sight of Lexi as she hurries down the side-walk towards me."
    "She looks more than a little unsteady and somewhat dishevelled, but for her, that's nothing new."
    "It's only when she catches up to me, pressing her hands on my chest and giggling, that I see she's a tad drunk."
    mike.say "Hey, Lexi."
    mike.say "Fancy bumping into you like this."
    mike.say "What are the chances, huh?"
    "Knowing the kind of things she gets up to and the people she associates with, that's obviously not true."
    "This is exactly the kind of sleazy location that I'd expect to find Lexi hanging around on any given night."
    show lexi annoyed
    lexi.say "Hey, I said hello to you, [hero.name]."
    lexi.say "And I thought you were going to blank me!"
    "Having started out in an ebullient mood, Lexi now seems to be quickly tipping over into morose."
    lexi.say "You weren't going to do that, were you, [hero.name]?"
    lexi.say "Huh..."
    mike.say "Erm, no...of course not, Lexi."
    mike.say "I was just...excited to see you, that's all!"
    show lexi happy
    "The moment that I paint my reaction to meeting her in such positive terms, Lexi's entire mood changes."
    show lexi close
    "Her eyes shine up with obvious delight, and she presses herself as close to me as she can manage."
    lexi.say "Mmmm...that's what I wanted to hear!"
    show lexi normal
    lexi.say "Because I like you, [hero.name]...I REALLY like you a lot."
    show lexi sad blush
    lexi.say "And it'd have made me sad to have you blank me..."
    "I smile nervously, a battle raging inside of me over how drunk Lexi is and yet also how hot."
    "My hands are on her now, I swear more out of the need to hold her up than anything else."
    mike.say "I...I like you too, Lexi."
    show lexi happy -blush
    "I feel Lexi wrap her arms around my waist as she looks up at me, still smiling."
    lexi.say "Do you know WHY I like you, [hero.name]?"
    "I shake my head, swallowing nervously at the same time."
    lexi.say "I like you because you like me for me, not for the money I make."
    lexi.say "You do nice things for me, and that makes me happy."
    "It's only now that I become aware of the fact that one of her hands is caressing my groin."
    show lexi flirt
    "Lexi grins as she massages my cock through the front of my pants."
    lexi.say "And when people do nice things for me, I do nice things for them too."
    lexi.say "I make them happy..."
    "And with that, she clasps my wrist with a surprisingly strong grip, and pulls me after her."
    "Before I know what's happening, Lexi's dragged me halfway down the nearest alleyway."
    show lexi bj alley casual nodick with hpunch
    "She pushes my back roughly against the wall, making me gasp."
    "And then she wastes no time in getting down on her knees and fumbling with my flies."
    "I know that I should probably try to stop her, but something keeps me from moving a muscle."
    "I know what you're thinking, trust me."
    "But there's the fact that we're standing in the middle of a dodgy neighbourhood at night."
    "If I make Lexi stop what she's doing, there's a good chance that she'll feel rejected and kick off."
    "And believe me, the last thing I want is to be stuck with a belligerent Lexi in a place like this!"
    "I'd be lucky to get away with an arrest for soliciting, rather than simply having my throat slit."
    "Meanwhile, Lexi has made progress despite the clumsiness that comes from being drunk."
    show lexi bj dick
    "She reaches into my unzipped flies and pulls out my cock, smiling at the sight of how stiff it is."
    "What do you expect?"
    "I've been dragged into an alleyway by a hot, slutty girl, intent on putting it in her mouth."
    "Whether it's the sight of Lexi's willing lips or the danger involved, it's more than a little exciting!"
    show lexi bj showcum
    lexi.say "Mmm..."
    "Lexi makes some rather agreeable sounds as she starts to lick at the tip."
    lexi.say "So big and so hard, just for little old me!"
    show lexi bj suck closed
    show mouth_insert lexi zorder 1 at zoomAt(1, (820, 200))
    "And then she takes it into her mouth, wrapping her tongue around the shaft."
    "It's not the most elegant of blowjobs, in fact it's pretty damn sloppy."
    "But what it lacks in style, it more than makes up for in terms of enthusiasm."
    show lexi bj open
    "Soon all I can hear is the sound of Lexi's lips sucking and her throat gagging."
    "I'm not being pushed back against the wall by her any longer, but leaning against it for support."
    show lexi bj normal showcum slap
    "At one point, Lexi fumbles my cock, making it pop out of her mouth and slap her on the cheek."
    lexi.say "Oops!"
    show lexi bj smile -slap
    lexi.say "I'm such a clumsy girl!"
    show lexi bj deepthroat closed
    "And before I can as much as say a word, she crams my balls into her mouth."
    "The experience is so intense for me that I've almost forgotten just where we are."
    "My own gasping and moaning gets louder, until a passing car illuminates us with its headlights."
    "Perhaps it's the sudden realisation of just how close we are to the street that does it."
    "Or maybe Lexi's just pushed me beyond the point of no return at that exact moment."
    show lexi bj left right
    "Either way, I can't hold back from cumming any longer."
    show lexi bj normal swallow facial with vpunch
    "Still sucking on my balls, the shower of cum takes Lexi completely by surprise."
    hide mouth_insert
    "She spits out the mouthful of testicles that she's been sucking on and yelps, far too loud for my liking."
    show lexi bj smile -left -right nodick
    lexi.say "Hey, no fair!"
    lexi.say "I wanted that in my mouth, not all over my face!"
    "All I can do is shake my head and let out a rueful laugh."
    "I'm just glad that she managed to finish before we were discovered!"
    return

label lexi_sell_drugs:
    scene bg alley
    show lexi casual
    "I see Lexi giving a small white package to some random dude..."
    "Fuck, she's dealing again."
    "I wait for a while then corner her in the alleyway, keeping her from leaving as I confront her."
    mike.say "I thought you said you wouldn't be dealing drugs anymore now that we're together."
    "Flustered, she snaps back."
    show lexi annoyed
    show fx anger
    lexi.say "Look, until you whisk me off my feet and get me out of the trailer park for good, I gotta keep myself supported somehow."
    mike.say "Supported? I do so much for you already. It'll be a little longer, I promise Just... come on!"
    "She frowns, but then she nods at me. "
    lexi.say "Alright, alright, but a gal like me can't just go unpunished for not listenin' to ya."
    show lexi close
    "Catching onto her quickly, I chuckle and place my hand upon her cheek, tapping her gently."
    "I then run my fingers through her hair and shove her down onto her knees."
    hide lexi with moveoutbottom
    show lexi bj nobg casual casual nodick with fade
    mike.say "You've really been a bad girl. Show me how sorry you are!"
    hide lexi
    show lexi bj nobg casual
    "She wastes no time in undoing my pants and tugging them apart, letting my cock spring open."
    show lexi bj suck
    show mouth_insert lexi zorder 1 at zoomAt(1, (820, 200))
    "Staring up at me with eyes that were definitely not sorry, she sucks my cock with the hungry skill that she can muster. "
    show lexi bj deepthroat open
    "Her eyes roll back as she tastes me, her tongue lapping up under the head as she gets into the rhythm. "
    "There's not much I can do in this situation. "
    "Having the power over her is just too much, and the threat of being found only makes things worse."
    show lexi bj suck left right
    "I groan, gripping her hair, and pulling her back."
    hide mouth_insert
    show lexi bj normal cum -open
    "She stares in shock at my swollen pole, only to squeal when warm streams of cum shoot off and cling to her face, rolling slowly down along her. "
    show lexi bj facial
    lexi.say "O... oh fuck..."
    mike.say "That's right. You are mine to do as I want!"
    if persistent.xray:
        show lexi stand2 alley casual manoutfit cum xray with fade
    else:
        show lexi stand2 alley casual manoutfit cum with fade
    with hpunch
    "I pull her up and slam her against the wall, my hands moving down along her body and lifting her legs. "
    "I hold her up against the wall by her waist and she instinctually takes me by the shoulders. "
    if persistent.xray:
        show lexi stand2 vaginal xray
    "With no more pomp, I thrust my still hard cock deep into her. "
    "Grunting, I whisper into her ear. "
    mike.say "Take it, and take it raw."
    mike.say "I'm gonna knock you up, and then you won't be able to sell drugs, you'll be so busy."
    lexi.say "Oh... oh fuck! Aaah, I'm a useless whore..."
    "I nip her on the ear as I continue to thrust away at her. "
    mike.say "Oh no, you don't... you aren't useless."
    mike.say "You're mine, and that makes you the most important thing right here and now."
    lexi.say "Oooh... oh, you're... you're so sweet!"
    if persistent.xray:
        show lexi stand2 alley casual manoutfit cum ahegao xray with hpunch
    else:
        show lexi stand2 alley casual manoutfit cum ahegao with hpunch
    "I hilt into her, tilting my own head back as I shoot off deep into her. "
    "She rolls her tongue out, going into full ahegao as I spurt up into her, filling her up, and leaving her swelling with my jizz."
    hide lexi
    show lexi casual
    with fade
    "I step back and she slides down along the wall, huffing in a dazed mess. "
    lexi.say "Aa... aaah.... N... no more... selling... b... boss..."
    return

label date_lexi_meet_jack:
    show lexi
    "As we walk around the mall I hear a voice."
    jack.say "Hey, [hero.name]!"
    show jack happy at left
    show lexi at right4
    with moveinleft
    "I turn around and see Jack walking toward us."
    mike.say "Hey, Jack."
    show jack perv
    jack.say "Woah man, who's the cutie?"
    mike.say "Jack this is Lexi, Lexi meet Jack."
    jack.say "Hi hot stuff!"
    show lexi annoyed
    lexi.say "..."
    jack.say "You should swing by, I got weed."
    mike.say "Sorry man, we are in the middle of a date."
    mike.say "See you around."
    show lexi at center
    hide jack
    with moveoutleft
    $ lexi.flags.lexijack = TemporaryFlag(True, 3)
    return

label date_lexi_meet_jack_2:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Jack")
    if not result:
        $ hero.cancel_event()
        return
    mike.say "Hey Jack."
    jack.say "Hi bro."
    jack.say "I wanted to ask..."
    mike.say "What?"
    jack.say "Are you serious about that girl you were with at the mall?"
    mike.say "Lexi?"
    menu:
        "Yes":
            mike.say "Yeah, totally."
            jack.say "Ok then, have fun I guess..."
        "Not really":
            mike.say "She's just a sweet piece of ass."
            jack.say "Do you think I could get a slice?"
            mike.say "What do you mean?"
            jack.say "Well I would pay good money to fuck that ass..."
            jack.say "And with that look of her I am pretty sure she would be willing."
            menu:
                "No way!":
                    mike.say "Nope, I am not a pimp..."
                    jack.say "Fuck man, you suck..."
                    $ game.flags.pimpingjack = False
                "Ok":
                    mike.say "500{image=gui/icons/icon_money.png}"
                    jack.say "Sold!"
                    mike.say "I'll see what I can do."
                    jack.say "Thx man, you're a real friend."
                    $ game.flags.pimpingjack = True
                    $ lexi.flags.lexijack = TemporaryFlag(True, 2)
    return

label date_lexi_meet_jack_3:
    show lexi
    mike.say "Hey Lexi do you remember my friend Jack?"
    show lexi surprised
    lexi.say "The weird guy we met at the mall?"
    mike.say "He asked me if you would be willing to fuck him..."
    show lexi annoyed
    lexi.say "Why would I do that?"
    mike.say "He is willing to pay."
    show fx drop
    lexi.say "..."
    $ lexi.love -= 10
    lexi.say "Ok."
    lexi.say "You get half of it, but not a cent more."
    mike.say "... ok."
    hide lexi
    $ lexi.flags.lexijack = TemporaryFlag(True, 2)
    return

label date_lexi_meet_jack_4:
    show bg trailer with fade
    "So I find myself standing rather awkwardly outside of Lexi's trailer, looking at my watch."
    "It's getting close to the time that I agreed with Jack for him to show up for his 'appointment' with Lexi."
    show lexi casual annoyed with dissolve
    lexi.say "Jeez, what are you even doing out here?"
    mike.say "Erm...I dunno - I was just waiting for Jack to show up."
    lexi.say "That's sweet of you, but maybe I should be the one showing the nerves?"
    mike.say "Give me a break, Lexi - I've never pimped anyone before now!"
    lexi.say "Urgh...just leave it to me, I've been pimped enough times for us both!"
    lexi.say "Look, just take his money and send him in to me."
    lexi.say "Think you can handle that?"
    "I nod, trying to look confident."
    lexi.say "Okay...God help me...just back me up if you hear any serious shit going down, yeah?"
    mike.say "Should we agree on a safe word?"
    lexi.say "Yeah, I was thinking of something like 'GET THIS FUCKING ASSHOLE OFF OF ME!!!'...what do you think?"
    "I sigh and nod to acknowledge her sarcastic point."
    "Lexi walks back into the trailer and I return to watching for Jack's arrival."
    hide lexi with dissolve
    "He pulls up a few minutes later, his new and shiny compact car looking distinctly out of place in the trailer park."
    show jack normal at left with moveinleft
    "Jack almost jumps out of the car, apparently already anticipating what Lexi has in store for him."
    show jack happy
    jack.say "Hey, man - where's Lexi?"
    jack.say "She's in the trailer, right?"
    show jack normal at left4 with ease
    "He goes to enter the trailer, and looks surprised when I bar his path."
    jack.say "What's up?"
    mike.say "Cash up front."
    jack.say "Oh, oh right...okay."
    "He hurriedly ferrets out his wallet and presses 500{image=gui/icons/icon_money.png} in bills into my hand."
    show jack happy
    jack.say "Sorry, man - I guess I'm not as clued up on this kind of thing as you are!"
    hide jack with fade
    "I furtively shove the notes into my pocket without counting them and close the trailer door."
    "As soon as I feel enough time has passed to make it look a little less obvious, I dart around the back of the trailer."
    "Luckily for me, Lexi's trailer has only a rickety fence behind it, so no one can see me as I scramble atop an old patio table dumped there."
    show lexi pimping with fade
    "I already chose the window to let me look into Lexi's bedroom and watch the action about to take place."
    show lexi pimping laying with fade
    "I can see Jack standing by the door and Lexi laid on the bed in a typically slothfully manner."
    "Their lips are moving, but I'm not really interested in what either of them is saying."
    "For all of his eagerness in front of me, Jack looks pretty nervous now he's alone with Lexi."
    "Lexi, by way of contrast, is acting all nonchalant and relaxed."
    "She stays reclined on the bed, not bothering to get up as she reaches for Jacks flies without asking permission first."
    "Where he was almost quaking before, Jack now freezes in place as Lexi's hand creeps into his pants."
    show lexi pimping handjob with fade
    if renpy.has_label("lexi_achievement_5") and not game.flags.cheat:
        call lexi_achievement_5 from _call_lexi_achievement_5
    "She keeps talking to him as she massages his dick until I can clearly see it standing to attention through his shorts."
    "Lexi almost carelessly yanks Jacks now painfully erect dick out of his flies in one move."
    "He gasps in pain, and she giggles at the sound, still stroking his shaft all the while."
    show lexi pimping blowjob casual with fade
    "Holding his eye, she leans forwards and begins to lick the tip and kiss it, wrapping her lips softly around it."
    "Then she closes her eyes and takes him slowly into her mouth, making small sounds of pleasure as she does so."
    "I find that I'm not so much watching them both as just focussing on Lexi and putting myself in Jack's place."
    "Memories of the last blowjob Lexi gave me come flooding back, and I can feel my own dick rapidly stiffening."
    "Lexi brings Jack almost to the point of blowing his load in her mouth."
    hide lexi with fade
    "But then she pulls away with an almost audible sound and leaves him gasping."
    "Taken by surprise, Jack gapes as she casually tosses him a condom."
    "She unbuttons and yanks down her tiny denim shorts, tossing them into the corner of the untidy room."
    "Then Lexi climbs onto the bed with her back to him and pulls off her T-shirt."
    "Unhooking her bra, it's impossible not to see her large, heavy breasts fall free, even from behind."
    "She puts her hands on the headboard and bends forwards, proffering her ass to him."
    "During all this, Jack has been struggling to pull his pants off and put on the condom at same time."
    "He almost loses his balance and falls flat on his face as he finally manages one and then the other."
    show lexi pimping fuck with fade
    "Luckily for him, he falls onto the bed and desperately clambers onto Lexi for all he's worth."
    "Lexi makes no attempt to build this up into something more than it is."
    "She's been sold to Jack as a piece of ass that he can fuck without consequences, and that's what she's giving him."
    "As he thrusts away desperately, she writhes and moans like he's showing her something entirely new."
    "But I've heard Lexi do the same with me, and I can see right through her performance."
    "Unsurprisingly, Jack can't hold on for very long, and he soon groans massively as he cums."
    hide lexi with fade
    "Lexi coos and giggles, rubbing her hands over her belly and breasts to show off the fact that they're suitably slick with sweat."
    "They exchange a few awkward words as he wipes his dick on a grubby T-shirt she offers him."
    "And I choose this as the perfect moment to climb down and sneak back around to the front of the trailer."
    show jack perv with dissolve
    "When he emerges from the door, Jack has assumed an air of confidence that doesn't hold true with his performance inside."
    mike.say "Well - do we have a satisfied customer, or what?"
    jack.say "Best five hundred dollars I ever spent, man!"
    mike.say "Yeah, she sure is something, isn't she?"
    jack.say "You know it - and I think she enjoyed herself too...if you know what I mean?"
    "Jack winks at me in a suggestive manner."
    mike.say "Really - you don't say?"
    jack.say "I DO say!"
    mike.say "Well, thanks for the cash - I think Lexi'll be putting hers towards finishing up her acting classes at night school."
    show jack normal
    jack.say "Acting classes?"
    mike.say "Oh yeah - you really should see her when she wants to put it on, utterly convincing."
    "Jack seems to deflate a little and I grin wickedly inside at the sight."
    hide jack
    "With that he climbs back into his car, making aimless small talk and obviously wanting to get away as quickly as possible."
    show lexi casual
    "I wave him off as I count his money and then divide it up between Lexi and myself."
    "Pimping might not be easy, but that doesn't mean it can't be fun."
    $ hero.money += 250
    hide lexi
    return

label date_lexi_meet_ryan_1:
    scene bg mall1
    "Call me cynical if you like, but one of the advantages of being with Lexi is that she's a cheap date."
    "Maybe it's because she's spent most of her life living on a trailer park."
    "Or maybe the fact that she's dated deadbeats the likes of Danny in the past."
    "Whatever the reason, it means that she's not the kind of girl that needs to be wined and dined."
    "I mean, she's always thrilled at the prospect of me taking her to the mall."
    "Just the chance to wander around window-shopping seems to be more than enough for her."
    "And it's not like I just get to be a tight-ass in terms of spending money when we do it either."
    "I also get to see the way that everyone looks at me thanks to having Lexi on my arm."
    "Trust me, she's the kind of girl that makes every guy jealous."
    "And she always gets their own girlfriends glaring at them as they check her out too!"
    "It makes me feel pretty special to be seen walking around with her."
    "But sometimes I can't help feeling that people might get the wrong idea."
    "That they might think I'm paying her to be with me or something like that."
    "Or worse, that I'm parading Lexi around in the hope of pimping her out!"
    "Then my mind gets to thinking that I could probably make good money that way."
    "And I have to force myself to think of something else."
    show lexi with dissolve
    lexi.say "Hey, [hero.name]!"
    lexi.say "Hello - earth to, [hero.name]!"
    mike.say "Huh..."
    mike.say "Wha..."
    mike.say "Oh...sorry, Lexi."
    mike.say "I was just thinking about something and got distracted, that's all."
    show lexi a at startle
    "Lexi plants her hands on her hips and shakes her head."
    lexi.say "Yeah well..."
    show lexi annoyed
    lexi.say "Your problem is that you think too much!"
    lexi.say "I say that you should think less and do more, you know?"
    show lexi happy
    lexi.say "That way life's a lot more fun, trust me!"
    show lexi normal
    "I can't help chuckling at Lexi's advice."
    "It's pretty simple, but it also makes a lot of sense when you really think about it."
    "Kind of like Lexi herself!"
    mike.say "Okay, Lexi - I'll try to keep that in mind!"
    ryan.say "Do my eyes deceive me?"
    ryan.say "[hero.name], that can't be you?"
    ryan.say "Not with a girl as hot as that one!"
    "The sound of the voice that I hear behind me is familiar enough to tell me who it is."
    "The condescending tone and insulting words just serve to confirm that it can't be anyone else."
    "I turn around, already steeling myself for a conversation with Ryan."
    show ryan smile at left
    show lexi at right4
    with moveinleft
    mike.say "Hello, Ryan..."
    mike.say "Fancy seeing you here!"
    "Ryan's face has that same look of arrogant superiority as ever."
    "The raised eyebrows and shit-eating grin that I hate so much."
    "But I can already see that I'm not the person he's most interested in right now."
    "Ryan's trying to hide it, but he's just not able to keep from staring at Lexi."
    ryan.say "Yeah, yeah..."
    show ryan annoyed
    ryan.say "I hardly ever come down here normally."
    ryan.say "But then I never knew there was anything worth seeing around the mall before now!"
    "Lexi can't help picking up on the fact that Ryan's obviously talking about her."
    "After all, with the line of work she used to be in, she's pretty good at reading people."
    show lexi happy
    "And right now she's smiling back at him pleasantly, but sticking close by my side."
    lexi.say "[hero.name]..."
    show lexi normal
    lexi.say "You're supposed to introduce me to your friend!"
    "I almost flinch at the idea of Ryan being an actual friend."
    "But I guess that I have to at least pretend to be friendly towards him."
    "So I force a grin onto my face and make the introductions."
    mike.say "Ryan, this is Lexi."
    mike.say "We're kind of dating each other."
    show ryan smile
    mike.say "Lexi, this is Ryan."
    mike.say "We used to live in the same house together."
    "I get sideways glances from both Lexi and Ryan at this."
    "It seems neither of them is pleased with my half-hearted efforts."
    show lexi annoyed
    lexi.say "[hero.name]!"
    lexi.say "What's up with you?"
    lexi.say "We're DEFINITELY dating each other, Ryan!"
    ryan.say "Don't worry about it, Lexi."
    ryan.say "[hero.name]'s just messing around."
    ryan.say "You know, having a joke?"
    ryan.say "We're really very good friends, you know?"
    "I roll my eyes and mutter something under my breath."
    show ryan annoyed
    ryan.say "Huh?"
    ryan.say "What was that, [hero.name]?"
    menu:
        "BFF!":
            mike.say "I said that's right."
            mike.say "Ryan and I go way back."
            show ryan smile
            "Ryan's got that shit-eating grin on his face again."
            "And I guess it's because he knows that I'm backing down."
            "He knows that I'm not going to call him on his bullshit in front of Lexi."
            ryan.say "Well, I can't stand around here talking all day."
            ryan.say "I have to go take care of business!"
            ryan.say "Nice meeting you, Lexi - maybe I'll see you around..."
            hide ryan with moveoutleft
            "With that, Ryan turns and walks away."
            show lexi at center with move
            "Which leaves Lexi and me to get back to our date."
        "Asshole..." if hero.flags.knows_ryancheats:
            mike.say "I said we WERE friends, Ryan."
            mike.say "At least until I found out what a cheating rat you were!"
            show ryan smile
            "Ryan's got that shit-eating grin on his face again."
            "And it's because I just let him know that he's living rent-free in my head!"
            ryan.say "Oh, [hero.name]!"
            ryan.say "You're not still hung-up about all that, are you?"
            ryan.say "It was in the past - water under the bridge."
            ryan.say "Sam and I have moved on, and so should you."
            "I open my mouth to argue."
            "But Ryan beats me to it."
            show ryan annoyed
            ryan.say "Well, I can't stand around here talking all day."
            ryan.say "I have to go take care of business!"
            show ryan smile
            ryan.say "Nice meeting you, Lexi - maybe I'll see you around..."
            hide ryan with moveoutleft
            "With that, Ryan turns and walks away."
            show lexi at center with move
            "Lexi watches him go, then turns to me."
            show lexi normal
            lexi.say "So, which one of you is the douche for real?"
            mike.say "He is, Lexi!"
            mike.say "Trust me on this one, okay?"
            show lexi smile
            "Lexi nods and smiles, taking hold of my hand."
            "And thanks to her efforts, I soon forget all about Ryan."
    $ lexi.flags.lexiryan = TemporaryFlag(True, 3)
    return

label date_lexi_meet_ryan_2:
    "The sound of my phone ringing tears my attention away from what I'm doing."
    play sound cell_vibrate
    "I pick it up and check to see if it's a number that I recognise."
    "And part of me's hoping that it isn't so I can just let it go to voicemail."
    "But then I see from the caller ID that it's Ryan."
    $ result = renpy.call_screen("smartphone_choice", "Ryan")
    if not result:
        $ hero.cancel_event()
        return
    "What in the hell is that douchebag calling me for?"
    "A moment later I recall the date I was on with Lexi the other day."
    "We were at the mall and we bumped into Ryan there too."
    "Maybe it's something to do with that?"
    "But whatever it could be, I have no idea."
    "So there's only one way to find out - and that's answering the call."
    mike.say "Ah..."
    mike.say "Hey, Ryan..."
    mike.say "To what do I owe the honour of you calling me?"
    "I hear the sound of Ryan chuckling on the other end of the line."
    "Like the idea of me being suspicious of his motives is just plain crazy."
    ryan.say "[hero.name], buddy..."
    ryan.say "Since when do I need an excuse to call you?"
    ryan.say "Can't one friend call another just because they want to catch up?"
    "If I was suspicious before, I'm doubly so now!"
    "But I decide to play along for the moment."
    "Maybe that way I can discover what this is all about."
    mike.say "Yeah, Ryan..."
    mike.say "Sure..."
    mike.say "So what, you just want to catch up with me?"
    ryan.say "Kind of, [hero.name], kind of..."
    ryan.say "I actually wanted to congratulate you."
    "Well now I am confused."
    "Since when did Ryan ever congratulate anybody?"
    "All he ever seemed to do was put me down!"
    mike.say "On what, Ryan?"
    mike.say "How well I'm looking these days?"
    ryan.say "Hell no, [hero.name]!"
    ryan.say "On scoring a super-hot babe like that!"
    "Oh, I see what's going on here!"
    "This is really all about Lexi."
    mike.say "Erm..."
    mike.say "Thanks...I guess!"
    mike.say "Lexi really is something special."
    ryan.say "Special?!?"
    ryan.say "Come on, [hero.name] - she's a goddess!"
    ryan.say "She's so far above your level too."
    ryan.say "I mean, you two can't be exclusive, can you?"
    ryan.say "That's why I wanted to ask you for her number!"
    "I know that Ryan's a cheating piece of shit."
    "But I never thought that he'd do something like this!"
    "He's actually calling me up to ask if he can make a move on Lexi!"
    menu:
        "Piss off!":
            "This is low, even for him!"
            "I don't even hesitate to tell Ryan exactly what I think of him."
            mike.say "How fucking dare you, Ryan!"
            mike.say "What kind of a friend calls someone up and asks for that?!?"
            mike.say "I should track you down and kick your ass!"
            ryan.say "Whoa, whoa, whoa..."
            ryan.say "Settle down, [hero.name]!"
            ryan.say "I was just testing you, that's all!"
            ryan.say "Trying to see if you were serious about this girl!"
            "What Ryan's saying sounds too ridiculous to believe."
            "But I can hear that familiar tone of sincerity in his voice."
            "Which I guess is the same one that he used on Sam to charm her."
            "I could keep pressing him, but there doesn't seem to be any point."
            "He's already backed down and started to cover his tracks."
            mike.say "Whatever, Ryan..."
            mike.say "Just don't ever do that to me again, okay?"
            ryan.say "Okay, [hero.name], you got it."
            "After that, I hang up the call."
            "I'm still fuming at the nerve of the guy."
            "But at least I told him off."
            "Maybe that'll be enough to stop him sniffing around Lexi in the future."
            $ game.flags.pimpingryan = False
        "I'll send it":
            "But then a thought occurs to me - am I taking this too personally?"
            "I mean, Lexi used to do this kind of thing all the time before we met."
            "She's got plenty experience, and she seemed to be pretty good at it too."
            "Am I letting my feelings get in the way of a chance to make money?"
            "After all, it's not like Lexi's going to get attached to a sleaze like Ryan."
            "He's the kind of guy that she could see through in an instant."
            "If anything, she'd be the one more likely to exploit him!"
            mike.say "Yeah..."
            mike.say "You got me, Ryan!"
            mike.say "Lexi and I do have an open relationship."
            ryan.say "I knew it!"
            ryan.say "I just knew it!"
            "I roll my eyes and bite my lip as Ryan congratulates himself."
            "He always did have a high opinion of himself."
            "But I need to indulge him in order for this to work."
            mike.say "Because it's you, I'll send you her number."
            mike.say "But be warned - Lexi's a professional."
            mike.say "And she's very good at what she does."
            ryan.say "Sure, sure..."
            ryan.say "I understand how these things work, [hero.name]!"
            ryan.say "And don't worry about a thing."
            ryan.say "I promise I won't take away your new toy!"
            "Ryan's still laughing as he hangs up the call."
            "I just hope that I'm right in thinking Lexi can handle this."
            "The last thing I want is for her to actually fall for Ryan's bullshit!"
            $ game.flags.pimpingryan = True
            $ lexi.flags.lexiryan = TemporaryFlag(True, 2)
    return

label date_lexi_meet_ryan_3:
    scene expression f"bg {game.room}"
    "I've been waiting to hear back from Lexi about her...shall we say 'encounter' with Ryan."
    "Or to be more honest, I've been eager to know just what went on and what went down."
    "Part of me is thrilled at the prospect of having actually been able to pimp Lexi out."
    "But another part of me is still worried that she might somehow have fallen for Ryan's so-called charms."
    "All the same, I try to look all calm and collected when I see her next."
    "Almost like the whole thing is an afterthought for me."
    show lexi normal nophone with dissolve
    lexi.say "So?"
    mike.say "So what, Lexi?"
    lexi.say "So, aren't you going to ask me how it went?"
    lexi.say "You know, with your friend Ryan?"
    "I nod and roll my eyes."
    mike.say "Oh right!"
    mike.say "You were going to do that thing with him, weren't you?"
    mike.say "How did it go?"
    show lexi happy at startle
    "Lexi laughs and shakes her head."
    "And I can tell that she's not fooled for a second."
    lexi.say "You don't have to play innocent with me, [hero.name]!"
    lexi.say "I'm hardly new to this kind of thing, am I?"
    show lexi normal
    lexi.say "It's business, a way to make some money, that's all!"
    mike.say "I...I know that, Lexi."
    mike.say "But I am new to this kind of thing, remember?"
    mike.say "I grew up my whole life being told it was something only bad guys did."
    mike.say "I'm still adjusting to the idea it's strictly professional, you know?"
    show lexi wink at center, zoomAt(1.65, (640, 1140))
    "Lexi leans in and places a kiss on my cheek."
    "It's totally unexpected and instantly lifts my mood."
    show lexi normal
    lexi.say "It's okay, [hero.name]."
    lexi.say "I don't need you to become a hardened pimp overnight."
    lexi.say "I actually prefer you a little bit innocent, yeah?"
    show lexi c happy
    lexi.say "It helps to keep me grounded."
    lexi.say "Keeps me from slipping back to my lowest point."
    "Lexi reaches into her bra as she's saying all of this."
    "I watch as she rummages around, hand between her breasts."
    "Then she pulls something out from her considerable cleavage."
    show lexi a normal
    lexi.say "Here's your share, [hero.name]."
    lexi.say "Two hundred dollars of Ryan the creep's money!"
    "I can't help raising my eyebrows as she hands it over to me."
    show lexi happy
    "Lexi notes my surprise and lets out a filthy laugh."
    $ hero.money += 200
    lexi.say "You think I do that kind of shit for small-change?!?"
    show lexi wink
    lexi.say "I don't let nobody like Ryan near me for less than top-dollar!"
    lexi.say "And that's just for starters, you know?"
    show lexi normal
    lexi.say "If you're really up for this, we can make some serious money!"
    menu:
        "Consider it":
            "I'm amazed at how professional Lexi's being about all of this."
            "That and how easily I can handle the idea when she does that too."
            "So long as this is business and we keep it that way, I think I'll be fine."
            "And the money is just too good to ignore!"
            mike.say "I'm up for it if you are, Lexi."
            mike.say "I mean, you're the one delivering the goods."
            mike.say "If you know what I mean?"
            show lexi happy at startle
            "Lexi laughs and shakes her head at me."
            lexi.say "You think that asshole Danny ever asked me what I thought about it?"
            show lexi normal
            lexi.say "That's how I know that I'm up for this, [hero.name]!"
            lexi.say "I know that we can make some serious money together."
            lexi.say "But I also know that you're gonna be looking out for me too!"
            "Lexi leans in and kisses me full on the lips."
            hide lexi
            show lexi kiss
            with fade
            $ lexi.flags.kiss += 1
            "She's so intense and passionate that she almost pushes me over."
            "And I know then that she's going into this thing willingly."
            hide lexi kiss
            show lexi happy nophone at center, zoomAt(1.65, (640, 1140))
            with fade
            "It doesn't matter how many guys Lexi sleeps with for money."
            "It's me that she loves, and that's worth more than all the money in the world."
            "And it's not like I'm stepping into Danny's shoes either."
            "All that jerk did was exploit Lexi, to use her."
            "We're going to be partners in this thing, to work together."
            "I'm not going to force Lexi into doing anything she doesn't want to."
            "And I don't think that I could do that even if I tried!"
            $ lexi.flags.lordofthepimp = True
        "That's a solid no":
            "I know instantly that I can't ask Lexi to do that again."
            "The mere thought of her being with other guys is just too much."
            "And I don't want to turn into the kind of guy Danny was either."
            mike.say "I'm sorry, Lexi..."
            mike.say "But no..."
            mike.say "I don't want to do this again."
            mike.say "And I'm sorry I ever asked you to do what you did with Ryan too!"
            "I'm expecting some kind of emotional outburst from Lexi any moment."
            "Either anger at me not supporting her in keeping on with it."
            "Or relief that I don't want her to go back to her old way of life."
            "But instead she just shrugs and then nods her head."
            show lexi normal
            lexi.say "No worries, [hero.name]."
            lexi.say "If that's what you want, it's fine by me."
            mike.say "You're okay with just quitting?"
            lexi.say "Sure, it's not like I'm desperate to go back on the game."
            show lexi happy
            lexi.say "I can get all the cock I want from you whenever I want it."
            show lexi wink
            lexi.say "And so long as I'm mooching off you for money, I'll be fine!"
            "I guess that's a positive answer."
            "I mean, I might have liked Lexi to say something about being in love with me."
            "But at least she's happy with the way things are."
            $ game.flags.pimpingryan = False
    return

label date_lexi_meet_master_1:
    scene bg beach
    show lexi smile swimsuit nophone
    with fade
    "Knowing how little Lexi's in the habit of wearing on an average day, I've kind of set myself a challenge."
    "And that's to see if I can actually manage to get her wearing even less without actually being naked."
    "So what better place to take her on a date than the beach?"
    "Somewhere you can get away with wearing next to nothing and nobody bats an eye at it!"
    show lexi at center, zoomAt(1.25, (640, 900))
    "And, of course, Lexi exceeds all of my expectations when we get there and walk down to the sand."
    "If you didn't look closely, you could be mistaken for thinking she's wearing nothing at all."
    "Plus the sand is a little hot today too, so she leaps and squeals as soon as she steps onto it!"
    show lexi annoyed at startle
    lexi.say "Ouch..."
    show lexi surprised at startle
    lexi.say "Ow..."
    show lexi angry at startle
    lexi.say "Fucking hell!"
    show lexi sad at startle
    "I watch in fascination as Lexi hops around on the hot sand."
    "I know that I should step in and help her."
    "But everything's bouncing up and down in front of me."
    "And it's pretty hypnotic too!"
    show lexi angry
    lexi.say "Hey!"
    lexi.say "How come your feet aren't burning too?"
    show lexi annoyed
    mike.say "Huh..."
    mike.say "Oh yeah...sorry, Lexi!"
    mike.say "The sand's cooler over here in the shade, I guess."
    hide lexi
    show lexi annoyed swimsuit nophone at center, zoomAt(1.5, (640, 1040)), startle
    "Still cursing and hopping from one foot to the other, Lexi hurries over."
    show lexi happy
    lexi.say "Shit..."
    lexi.say "That's SO much better!"
    show lexi smile
    "I nod and smile, still ogling Lexi's body as much as I can."
    "And I'm already wondering if I can wrangle something out of this for myself."
    "I mean, maybe she'll want a foot massage to soothe her pain?"
    show lexi angry
    lexi.say "Eww..."
    lexi.say "What's that dirty old geezer staring at?"
    hide lexi with fade
    "I snap out of it when I hear Lexi complaining."
    "And I look in the direction she's pointing."
    mike.say "What geezer, Lexi?"
    mike.say "I don't see anyone."
    lexi.say "That one there - in the tall grass!"
    lexi.say "He just popped up and started leering at me!"
    scene bg beach at center, zoomAt(2.5, (0, 1440))
    show master at center, zoomAt(1.5, (840, 1240))
    with fade
    "Now I see what she's talking about."
    "I spot the bald, wrinkled head in the grass."
    "And I recognise who it is almost as soon as I do."
    mike.say "Huh..."
    mike.say "It's a guy who calls himself the 'Master'!"
    mike.say "He's a weirdo that hangs around the beach."
    mike.say "Claims to be a martial arts guru or something like that."
    scene bg beach
    show lexi smile swimsuit nophone at center, zoomAt(1.25, (540, 900))
    with fade
    lexi.say "'Master' huh?"
    lexi.say "More like 'Masturbator'!"
    show lexi annoyed
    "Lexi frowns and sticks a middle finger up in his direction."
    show master at right with easeinright
    "But rather than being discouraged, the Master starts scuttling towards us."
    show lexi angry
    lexi.say "What the fuck?!?"
    lexi.say "Why is he coming over here?"
    show lexi annoyed
    mike.say "How the hell would I know, Lexi?"
    mike.say "Like I said, he's a local weirdo."
    mike.say "He probably doesn't even know what day of the week it is!"
    show master at right5
    show lexi at center, zoomAt(1.25, (340, 900))
    with ease
    "Lexi backs off and stands a little behind me as the Master reaches us."
    "He has a creepy grin on his wrinkled face, like he's seen something he likes."
    "And he hardly seems to notice me at all, his attention focused on Lexi instead."
    show master at center, zoomAt(1.25, (840, 900))
    master.say "Ooh..."
    master.say "Hello, my dear!"
    master.say "And what are you doing out here all alone?"
    "I shake my head at the old fool's words."
    "Then I put myself firmly between him and Lexi."
    mike.say "She's not on her own, old man."
    mike.say "She's here with me, okay?"
    show master at center, zoomAt(1.0, (940, 900)), startle with move
    "The master jumps in the air and scuttles back a way."
    "As though he hadn't noticed me until I actually spoke to him."
    master.say "Argh!"
    master.say "Where did you come from, eh?"
    show lexi angry
    lexi.say "He was there the whole time, you stupid old goat!"
    lexi.say "And you'd better back off, or else he'll kick your ass!"
    show lexi annoyed
    "I hold up a hand to Lexi, trying to get her to calm down."
    "But at the same time I still keep the old man from coming any closer."
    mike.say "Slow down, Lexi."
    mike.say "We're not there just yet!"
    mike.say "But you'd better tell me what the hell you want, old man!"
    "The master mutters to himself, straining to see around me and ogle Lexi."
    "He rubs his hands together the whole time, making him seem even more creepy."
    show master normal at startle
    master.say "Oh, nothing much..."
    master.say "Just the chance to touch those..."
    show master happy
    master.say "Those pretty little things on your chest, my dear!"
    "I almost burst out laughing at this."
    "I mean, who calls tits like Lexi's 'little things' with a straight face?"
    "But at least now I know what all of this is about."
    "The old man pleads with me as he rummages in his pockets."
    show master perv at startle
    master.say "Please!"
    master.say "I can pay!"
    master.say "I have money!"
    "Suddenly he's holding out a handful of crumpled bills."
    "There must be at least fifty bucks right there!"
    "I look at the money and then at Lexi."
    "All the time trying to figure what I should do next..."
    menu:
        "Consider it":
            "But then it comes to me."
            "I snatch the bills out of the Master's hand."
            $ hero.money += 25
            "Then I look at Lexi and nod in his direction."
            mike.say "You're up, Lexi."
            mike.say "Take him into the long grass and sort him out."
            show lexi surprised at startle
            $ lexi.love -= 4
            "Lexi looks at me in genuine surprise for a moment."
            "And I think she's actually going to refuse."
            "But then I wave the money under her nose."
            "Which seems to snap her out of it."
            show lexi normal
            lexi.say "Sure, [hero.name], sure..."
            lexi.say "Let's get this over with, okay?"
            show lexi smile
            show master happy at startle
            "The Master claps his hands together with glee."
            hide master with easeoutright
            "And then he scuttles into the grass before us."
            hide lexi with easeoutright
            "Lexi and I follow him until we're well hidden."
            scene bg beach at center, zoomAt(2.5, (0, 1440))
            show master zorder 2 at center, zoomAt(1.65, (940, 1140))
            with fade
            show lexi annoyed swimsuit nophone zorder 1 at flip, center, zoomAt(1.65, (440, 1140)) with easeinleft
            "Then she takes a deep breath and unhooks her top."
            show lexi annoyed topless
            "Freed from their bondage, her breasts swing and sway."
            "And without asking permission, the Master pounces on them."
            show master happy
            master.say "Ooh..."
            show master perv at center, zoomAt(1.65, (800, 1140)) with ease
            show lexi annoyed topless grope
            master.say "Ha, ha, ha..."
            master.say "Come to papa..."
            "Lexi does the best she can to look the other way."
            "And I'm not exactly keen on watching the old goat gratify himself either."
            "I swear at one point he's actually drooling as he fingers her nipples too!"
            "Eventually I get tired of listening to the sound of his voice."
            "So I walk over and give him a gentle shove to let him know he's done."
            show lexi annoyed topless -grope
            show master angry at center, zoomAt(1.65, (940, 1140)) with ease
            master.say "Hey!"
            master.say "What gives?!?"
            master.say "Didn't I pay you already?"
            mike.say "Time's up, old man!"
            mike.say "Now you'd better piss off."
            mike.say "Go crawl back under the rock you came out from!"
            "Lexi nods as she puts her top back on."
            show lexi sad swimsuit -topless
            "And she sticks her tongue out at him for good measure as we walk away."
            scene bg beach
            show lexi normal swimsuit nophone at center, zoomAt(1.5, (640, 1040))
            with fade
            lexi.say "So..."
            lexi.say "What's my cut of the money, [hero.name]?"
            lexi.say "After all, I was the one he had his filthy hands all over!"
            show lexi smile
            mike.say "Hmm...let's see, Lexi..."
            mike.say "Maybe you're going to have to let me do the same to earn it!"
            show lexi angry
            lexi.say "Hey, no fair!"
            lexi.say "I let you play with my tits for free all the time!"
            show lexi annoyed
            mike.say "It's not my fault you give it away for free, Lexi!"
            mike.say "Looks like it's a good job I'm the one handling these deals for you!"
            $ lexi.love -= 2
            $ game.flags.pimpingmaster = True
            $ lexi.flags.leximaster = TemporaryFlag(True, 2)
        "Just piss off":
            "But then it comes to me."
            show master at hshake
            "I shake my head and slap the Master's outstretched hand."
            "This sends his dirty clump of bills flying in all directions."
            show master angry
            master.say "Hey!"
            master.say "What are you doing?!?"
            show master at center, zoomAt(1.0, (940, 1100)), startle with move
            "And just like that he's scrabbling around on the sand."
            "As he chases down the scattered bills, he hurls curses at me."
            master.say "You jerk!"
            master.say "What did you do that for, huh?"
            master.say "All I wanted was a quick squeeze!"
            hide master with dissolve
            "I let out a snort of derision and turn my back on him."
            "And at the same time, I take hold of Lexi's hand."
            mike.say "Come on, Lexi."
            mike.say "Let's get away from this creep!"
            mike.say "The only person that handles your breasts is me."
            mike.say "And I'm not paying for the privilege!"
            hide lexi
            show lexi happy swimsuit nophone at center, zoomAt(1.5, (640, 1040)), startle
            "Lexi laughs and kicks sand at the master."
            show lexi smile
            "Then she takes my arm and we walk away."
            show lexi normal
            lexi.say "I never saw you be a bully like that before, [hero.name]..."
            show lexi wink
            lexi.say "It was kind of sexy, you know?"
            lexi.say "And it kind of makes me want you inside of me too..."
            $ lexi.love += 4
            $ game.flags.pimpingmaster = False
    return

label date_lexi_meet_master_2:
    scene bg beach
    show lexi smile swimsuit nophone at center, zoomAt(1.0, (640, 720))
    with fade
    "The first attempt Lexi and I made to have a date at the beach was crashed by the so-called 'Master'."
    "The creepy old man that's always slinking around somewhere in the long grass, watching the girls."
    "But we've both decided to put that behind us and try again, taking advantage of the decent weather."
    "And things seem to be going pretty well, with Lexi looking like she's having a great time."
    "I purposefully steer her well away from the spot where the Master popped up when we were here last."
    "And I'm even starting to forget about the old pervert and have a good time myself."
    show lexi normal at center, traveling(1.25, 0.3, (640, 880))
    lexi.say "Huh..."
    lexi.say "I wonder how much it is to hire one of those jet-skis?"
    show lexi smile
    mike.say "I dunno, Lexi..."
    mike.say "I never rode one myself."
    show lexi normal
    lexi.say "Ah, I was just thinking..."
    lexi.say "They look like fun, don't they?"
    show lexi smile
    master.say "Oh no, dear!"
    master.say "Way too dangerous, if you ask me!"
    show lexi surprised at center, traveling(1.25, 0.1, (340, 880)) with vpunch
    lexi.say "What the fuck?!?"
    mike.say "Jesus Christ!"
    show master at center, zoomAt(1.30, (1040, 940)) with dissolve
    "Lexi and both spot the Master at the same time."
    "He's standing behind us, sticking his head into the gap between our bodies."
    "We leap in opposite directions, trying to get away from the old pervert."
    show master happy at startle
    master.say "Ha, ha..."
    master.say "How did I manage to sneak up on you?"
    master.say "Well, that's thanks to a lifetime devoted to studying martial arts!"
    show master normal
    mike.say "That's not the question that was on my mind!"
    show lexi angry
    lexi.say "And you'd better hope you remember those martial arts."
    lexi.say "Because I'm just about ready to kick your ass, old man!"
    show lexi annoyed
    show master at center, traveling(1.2, 0.3, (1040, 880))
    "The Master smiles and begins to back away."
    "He holds his hands up in a gesture of surrender."
    show master happy
    master.say "Now, now..."
    master.say "No need to be like that!"
    master.say "You were just standing here wondering about the price of those jet-skis."
    master.say "And I was just wondering about the price of this young ladies services."
    master.say "So we're not so very different, now are we?"
    show master normal
    show lexi blank
    "I roll my eyes and clench my fists."
    "If Lexi wants to kick this guy's ass, she's going to have to get in line!"
    "But when I look over in her direction, she's wearing a thoughtful expression."
    show lexi normal
    lexi.say "Urgh..."
    lexi.say "What do you want now, old man?"
    lexi.say "Because what you wanted last time ain't on the menu no more!"
    show lexi blank
    "The Master shakes his head."
    "At the same time he bobs up and down on the spot."
    show master happy
    master.say "Oh no..."
    master.say "No, no, no!"
    master.say "This time I was going to ask for oral relief!"
    show master perv
    master.say "Is that on the menu for today?"
    master.say "And if so, how much?"
    show master normal
    show lexi smile
    "Lexi lets out a snort of derision and turns to look at me."
    show lexi normal
    lexi.say "Your call, [hero.name]."
    lexi.say "What's it gonna be, huh?"
    show lexi blank
    menu:
        "Tell Lexi to give the Master a blow-job":
            "I look at Lexi for a moment, then back at the Master."
            mike.say "Oral is one hundred bucks, old man."
            mike.say "No extras, just the basic package."
            mike.say "And she does NOT swallow!"
            show lexi smile
            "Lexi cocks her head on one side."
            "But she also nods, letting me know she approves."
            "The Master nods and chuckles with glee."
            "He's already pulling notes out of his pockets."
            "Then he hands me a crumpled bunch of notes."
            "I take the time to count out the money."
            "And once I'm satisfied it's all there, I give Lexi a nod."
            show lexi normal
            lexi.say "Urgh..."
            lexi.say "Okay, let's get this over with!"
            show lexi smile
            "The master cackles with glee, beckoning for us to follow him."
            "Then he leads us into the tall grass where we won't be seen."
            "At first I tell myself that I'm not going to watch."
            "I'm just going to stand guard over Lexi and make sure nobody sees us."
            "But almost the moment she kneels down in the sand, I can't resist."
            "I keep finding my eyes drawn to Lexi as she tugs down the Master's shorts."
            scene bg black
            show lexi bj master beach swimsuit
            with fade
            "Then his cock pops up in front of her face, and it's bigger than I expected!"
            "It looks like Lexi's surprised too, as her eyes go wide."
            "But then she checks herself and resumes her professional demeanour."
            master.say "Hmm..."
            master.say "Do you see something you like, my dear?"
            master.say "Are appearances deceptive?"
            mike.say "Shut up, old man!"
            mike.say "No talking, okay?"
            master.say "I understand, I understand!"
            master.say "No need to get so angry!"
            "At that moment, Lexi grabs hold of the Master's cock."
            play sexsfx1 bj_sucking loop
            show lexi bj msuck
            "She squeezes it at the base as she puts the head into her mouth."
            "And that's more than enough to distract the old goat."
            show lexi bj deepthroat
            master.say "Oooh..."
            master.say "Oh yes!"
            "What follows is a lesson in practicality from Lexi."
            show lexi bj msuck
            "She works the Master from one end of his cock to the other."
            play sexsfx1 bj_deepthroat loop
            show lexi bj deepthroat
            pause 0.2
            show lexi bj msuck
            "Her head bobs up and down, her lips and tongue move the whole time."
            "And watching her, I almost forget who she's blowing and that it's for money."
            "Because when it comes to oral, Lexi's refined it to a fine art."
            "Every move she makes pushes him further along."
            "And the whole time he's losing it more and more."
            "The Master seems almost delirious, his head wobbling atop his scrawny neck."
            show lexi bj deepthroat closed
            pause 0.2
            show lexi bj msuck
            pause 0.2
            show lexi bj deepthroat
            "He's making a gurgling sound, which is pretty disgusting to hear."
            "So I do the best I can to ignore him and instead focus on Lexi."
            show lexi bj deepthroat
            pause 0.2
            show lexi bj msuck
            pause 0.2
            show lexi bj deepthroat open
            "All of a sudden, Lexi extends a single finger."
            "Then she shoves it somewhere in the Master's anatomy."
            show lexi bj deepthroat
            pause 0.2
            show lexi bj msuck
            pause 0.2
            show lexi bj deepthroat
            "I don't see exactly where it goes, but the effect is instant."
            "The Master wails and his entire body starts to convulse."
            show lexi bj msuck
            pause 0.2
            show lexi bj normal
            "Lexi uses that as her excuse to pull his cock out of her mouth."
            play sexsfx1 final_thrust
            show lexi bj normal cum with vpunch
            "And she sits back, a look of grim satisfaction on her face as he loses it."
            with vpunch
            "The sight of the old man shooting his load is finally enough to make me look away."
            stop sexsfx1
            scene bg beach with fade
            show lexi smile swimsuit nophone at center, zoomAt(1.5, (640, 1040)) with easeinright
            "Lexi's by my side a moment later, taking hold of my arm."
            "Together we walk away, leaving the Master to roll around in the sand."
            "Neither of us says a word as we return to the sand."
            "But the feeling of the notes in my pocket makes it all seem worthwhile."
        "Tell the Master to fuck off":
            "I don't even hesitate to make my opinion known."
            "Asking to feel Lexi's breasts was bad enough."
            "But this is just too much for me to take."
            mike.say "Get lost, you disgusting old man!"
            show master surprised at center, zoomAt(1.0, (940, 860)), startle
            "I step forwards and give the Master a hard shove."
            "Part of me's expecting him to pull some crazy martial arts move."
            "That I'll suddenly find myself flying through the air."
            hide master with moveoutbottom
            "But instead the old fool just goes tumbling onto the sand."
            "He lands hard, and the impact looks pretty painful too."
            master.say "Aargh!"
            master.say "Ooh..."
            master.say "I think I broke something!"
            mike.say "Well I'll break something for sure..."
            mike.say "And I'll start on the count of ten..."
            mike.say "One...two...three..."
            "I watch as the Master's skinny limbs thrash in the sand."
            "He only half makes it up before he starts to flee from my wrath."
            "Which means that he almost scuttles away on all fours."
            show lexi smile at center, traveling(1.5, 0.3, (640, 1040))
            "Lexi watches him go, a smile of satisfaction on her face."
            show lexi normal
            lexi.say "That'll teach him!"
            lexi.say "But I already lined my lips up for a BJ!"
            show lexi wink
            lexi.say "Oh...I know - would you like one as a reward?"
            $ game.flags.pimpingmaster = False
    return

label date_lexi_meet_master_3:
    scene bg beach
    show lexi smile swimsuit nophone at center, zoomAt(1.0, (640, 720))
    with fade
    "I was honestly going to suggest that Lexi and I avoid the beach when it came time for our next date."
    "We'd already tried to have a nice day there on more than one occasion, and it never went to plan."
    "Mainly because of that creepy old so-called martial arts master that's always hanging around there."
    "Each time we were able to deal with him one way or another, but I'd just about had enough of him."
    "But Lexi wouldn't hear a word of it."
    "She said that she wanted to go back to the beach, creepy old man be damned!"
    "I could have argued with her, insisted that we go somewhere else."
    "But the truth was that I couldn't come up with an alternative that appealed."
    "So here we are, walking across the sand again and trying to look like we're having fun."
    "Even so, I keep glancing at the tall grass around the dunes at the edge of the beach."
    show lexi blank swimsuit nophone at center, traveling(1.25, 0.3, (640, 880))
    "Lexi's stealing the occasional glance too, narrowing her eyes whenever she sees movement."
    mike.say "This is crazy, Lexi!"
    mike.say "Let's forget about it and go somewhere else, yeah?"
    show lexi annoyed
    "Lexi shakes her head at this."
    "Her jaw set at a belligerent angle."
    show lexi angry
    lexi.say "No way, [hero.name]!"
    lexi.say "I'm not changing my plans because of that old pervert!"
    lexi.say "I just wish I'd thought to bring along man can of mace!"
    show lexi annoyed
    "I can't help chuckling at the image of Lexi spraying the Master."
    show lexi blank
    "Sure, it probably wouldn't be the right thing to do."
    "But it'd be funny to see him get his just desserts for once!"
    mike.say "Maybe he took the day off?"
    mike.say "There's been no sign of him so far."
    show lexi normal
    lexi.say "Nah, he's here alright."
    lexi.say "When you've worked the sex-trade for as long as I have, you develop an instinct for this."
    lexi.say "I can almost smell it on the air when there's a per hanging around me!"
    show lexi blank
    "All I can do is shrug and nod at that statement."
    mike.say "I can believe that, Lexi!"
    mike.say "That guy looked like he could use a shower!"
    "Almost the same moment I'm done talking, I hear an angry cry."
    "A head pops up from the grass around the dunes too."
    "And, of course, it's the Master again."
    show master happy at center, zoomAt(1.0, (1040, 740)) with easeinright
    master.say "Hey!"
    master.say "I'll have you know that I shower on a regular basis!"
    master.say "And even when I can't, my natural scent is actually an aphrodisiac!"
    show master normal
    show lexi blank swimsuit nophone at center, traveling(1.25, 0.3, (340, 880))
    "Lexi takes a step back as the Master scuttles out of the grass."
    "She's not exactly standing behind me."
    "But she's clearly not keen on there being nothing between the two of them."
    "I take a step forwards before the Master can get over to us."
    "I'm bound and determined to keep him from just strolling up to Lexi."
    mike.say "That's close enough!"
    mike.say "Take another step and you'll regret it."
    show master at center, traveling(1.25, 0.3, (940, 900))
    "The Master capers around in front of me, hopping from one foot to the other."
    "All the time he's trying to sneak a look at Lexi who darts in the opposite direction."
    show master perv
    master.say "Don't be so mean to me!"
    master.say "I'm ill, in need of healing!"
    master.say "And you can provide the cure, my dear!"
    show master sad
    show lexi angry
    lexi.say "Oh yeah?"
    lexi.say "I think you're sick, old man."
    lexi.say "But it's in the head where you got it."
    lexi.say "Your brain's all fucked up!"
    show lexi annoyed
    mike.say "Let me guess, old man..."
    mike.say "The only thing that can cure you is sex?"
    mike.say "And that's why you're harassing us, right?"
    "The Master nods eagerly."
    show master happy
    master.say "How very perceptive of you, my boy!"
    master.say "Are you skilled in the mystic arts too?"
    master.say "Yes, my Chi is out of balance."
    master.say "And only sexual congress can bring it back into alignment!"
    show master perv
    master.say "Specifically, sex with a hottie like her!"
    show master normal
    "I can't help but burst out laughing."
    "This guy is so easy to see through he's practically transparent!"
    mike.say "What do you think, Lexi!"
    mike.say "Do you want to heal the old goat's spiritual ailments?"
    mike.say "Or do you want me to give him some physical ones to take his mind off them?"
    show lexi normal
    lexi.say "Your call, [hero.name]."
    lexi.say "We're gonna make him pay."
    lexi.say "One way or another!"
    show lexi blank
    menu:
        "Let the Master fuck Lexi":
            "I put a hand on Lexi's shoulder and guide her in front of me."
            "Then I wave a hand up and down, like I'm showing her off."
            mike.say "Two hundred {image=gui/icons/icon_money.png}, old man."
            mike.say "That's what it'll cost you to get some of this!"
            mike.say "Serious money, you got that?"
            "Part of me is expecting Lexi to push my hands away."
            "Expecting her to object to being offered up like this."
            "But then she puts a hand on her hip and strikes a pose."
            show lexi normal
            lexi.say "Yeah, old man..."
            lexi.say "This is too much for a bum like you to afford!"
            show lexi smile
            "The Master is practically drooling by now."
            "He keeps on nodding as he rubs his hands together."
            "Then he thrusts them into his pocket and pulls out a roll of notes."
            show master happy
            master.say "I presume cash is preferable...hmm?"
            show master normal
            show lexi surprised
            "Lexi's eyes go wide at the sight of the money."
            show lexi blank at center, zoomAt(1.0, (340, 880)), stepback(0.2, 60, 0)
            pause 0.2
            play sound woosh_punch
            "She snatches it out of the Master's hand."
            "Then she shoves it into mine."
            show lexi normal
            lexi.say "Cash is VERY MUCH preferred!"
            lexi.say "Make yourself useful, [hero.name], and count this."
            lexi.say "If it's enough, then we've got a deal."
            show lexi smile
            "I shrug and do as I'm told."
            "I flip through the roll, silently totting up the total."
            "Then I nod and shove it into my own pocket."
            mike.say "Two hundred, on the dot."
            hide lexi with easeoutright
            "Lexi nods and starts to walk towards the dunes."
            "The Master capers from one foot to the other."
            hide master with easeoutright
            "But he's also following close on her heels."
            "I bring up the rear, trying to make sure we don't look too obvious."
            "But at the same time, I'm also watching the Master too."
            "One false move, and I tell myself that he'll regret it!"
            scene bg beach at center, zoomAt(1.5, (640, 1040)), blur(5)
            show lexi smile swimsuit nophone at center, zoomAt(1.5, (440, 1040))
            show master perv at center, zoomAt(1.5, (940, 1080))
            with fade
            pause 0.5
            show lexi smile naked with dissolve
            "Once we're safely out of sight, Lexi begins to strip-off."
            "She does it in a business-like manner, not even looking at the Master."
            "But that doesn't seem to bother him in the slightest."
            show master naked with dissolve
            "He's nodding the whole time, pulling off his own clothes."
            "And I can already see that he's pretty excited at the prospect of what lies ahead."
            "Naked he kind of looks like a tortoise that's been deprived of it's shell."
            "And yet I have to shake my head in admiration when I see his manhood."
            "Either his martial arts are actually good for something."
            "Or else he's just been blessed by nature."
            show lexi surprised
            "Whatever the case, Lexi's got a challenge on her hands!"
            "She's about to get down to business when she spots it too."
            show lexi normal
            lexi.say "Alright, listen up..."
            lexi.say "Whoa...change of plan!"
            lexi.say "Get down there, on your back - NOW!"
            scene bg black
            show lexi cowgirl naked beach master out up smile
            with fade
            "The Master hurries to do as he's told."
            "And his cock sways in the air as he does so."
            "Lexi waits until he's in position, then she stands over him."
            "I watch as she lowers herself down and grabs his cock."
            "Then Lexi guides it between her thighs."
            "She's more than a little rough as she presses it against her pussy."
            "But that doesn't seem to bother the Master in the slightest."
            play sexsfx1 slide_in
            show lexi cowgirl vaginal middle
            "Instead he nods and cackles with delight as it inches into her."
            master.say "Oh my..."
            master.say "Oh goodness me..."
            master.say "I can feel my chakras healing already!"
            play sexsfx1 fuck_calm loop
            show lexi cowgirl down
            "Lexi sits down atop him with as much force as she can muster."
            show lexi cowgirl middle masterhand
            pause 0.25
            show lexi cowgirl down
            "The old man wheezes, but then she's riding him with a vengeance."
            show lexi cowgirl middle
            pause 0.25
            show lexi cowgirl down
            "I'd say she was riding him like her life depended on it."
            "But with a guy that old, I'd be afraid of tempting fate!"
            "Because it's more like the old geezer's the one that's going to expire!"
            play sexsfx1 fuck_calm loop
            show lexi cowgirl middle normal pleasure
            pause 0.25
            show lexi cowgirl down
            pause 0.25
            show lexi cowgirl middle
            pause 0.25
            show lexi cowgirl down
            "I have to admire the way that Lexi goes about the task."
            "She keeps her hands away from the Master, like she doesn't want to touch him."
            "But at the same time she uses her weight to pin him down on the sand."
            "And she also makes sure that her chest is well out of his reach too!"
            "Not that it stops the sleazy old creep trying to get a hold of them."
            "All in all, the Master looks like he's having some kind of seizure."
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            pause 0.15
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            "He keeps chuckling and gurgling as Lexi bounces up and down on his cock."
            "But with each minutes that passes, the sounds are becoming ever stranger."
            play sexsfx1 fuck_moderate loop
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            pause 0.15
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            "In fact, he's starting to sound more like he's delirious than anything else!"
            show lexi cowgirl middle -masterhand
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            pause 0.15
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            "His head is lolling about and his arms aren't reaching for Lexi anymore."
            master.say "Blurgh..."
            master.say "Errgh..."
            master.say "Mmm..."
            show lexi cowgirl middle -masterhand
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            pause 0.15
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            "All of a sudden the Master's movements become jerky and he stiffens."
            "It only takes me a moment to figure out what's happening to him."
            show lexi cowgirl middle -masterhand
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            pause 0.15
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            mike.say "Lexi..."
            mike.say "He's gonna blow!"
            show lexi cowgirl pleasure
            lexi.say "I'm way ahead of you!"
            show lexi cowgirl middle -masterhand ahegao panting
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            pause 0.15
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            "And she's not kidding either."
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            pause 0.15
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down with vpunch
            pause 0.15
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl up out with vpunch
            play sexsfx1 slide_out
            "Lexi practically leaps off of the old man as she says all of this."
            "And we both watch as the Master shoots his load."
            play sexsfx1 final_thrust
            show lexi cowgirl cumshot with vpunch
            "It goes straight up in the air, like an impressive white fountain."
            show lexi cowgirl with vpunch
            "At the same time his body jerks and spasms."
            show lexi cowgirl -cumshot cum with vpunch
            "So I guess he's having a pretty dramatic orgasm."
            "Once he's stopped moving, the Master goes still."
            scene bg beach at center, zoomAt(1.5, (640, 1040)), blur(5)
            with fade
            pause 0.5
            show lexi smile naked nophone at center, zoomAt(1.5, (640, 1040)) with easeinbottom
            "She hops to her feet and then hurries to my side."
            "Lexi and I look down at him, both wondering the same thing."
            show lexi normal
            lexi.say "Do you think he's...you know?"
            show lexi blank
            mike.say "I don't know - he looks half dead most of the time!"
            show lexi normal
            lexi.say "If he is, then it's one less creep to worry about."
            show lexi blank
            mike.say "Yeah, but don't forget what you two just did."
            mike.say "You could end up getting charged with murder!"
            show lexi surprised
            lexi.say "FUCK OFF!"
            show lexi angry
            lexi.say "You can't go down for screwing someone to death!"
            show lexi blank
            master.say "I...I'm not dead!"
            with vpunch
            mike.say "Aargh!"
            show lexi surprised
            lexi.say "Holy shit!"
            show lexi blank
            master.say "I feel alive!"
            master.say "I feel happy!"
            show lexi normal
            lexi.say "Yeah, well - you'll have to feel yourself from now on!"
            show lexi smile swimsuit
            "Lexi plucks her clothes up and quickly gets dressed."
            hide lexi with easeoutleft
            "Then she takes hold of my hand, leading me away from the Master."
            scene bg beach with fade
            show lexi smile swimsuit nophone at center, zoomAt(1.5, (640, 1040)) with easeinright
            "Together we walk back to the sand thinking about the money we just made."
            mike.say "We could use that two hundred bucks to get away, Lexi."
            mike.say "Go somewhere nice for the weekend, just you and me."
            mike.say "How does that sound?"
            show lexi normal
            lexi.say "If you can make one hundred stretch to cover that, I'm in."
            lexi.say "Because half of that money's mine, [hero.name]."
            lexi.say "And I'm gonna spend it on me."
            lexi.say "On something nice to take my mind off screwing that old goat!"
            show lexi smile
            $ hero.money += 100
        "Tell the Master to get lost":
            "I shake my head and let out a more rueful laugh."
            mike.say "You know what, buddy..."
            mike.say "I'm getting pretty sick of you bugging us."
            "I shoot out a hand, palm open."
            "And it connects with the Master's shoulder."
            "He's clearly not expecting it, his attention all being on Lexi."
            "This means that the blow catches him off-guard."
            show master zorder 1 at center, traveling(1.2, 0.2, (940, 860))
            "He staggers backwards, almost falling onto his scrawny ass."
            show lexi annoyed at flip, center, traveling(1.25, 0.3, (340, 880))
            "But it seems that Lexi's not content to leave it at that."
            show lexi zorder 2 at flip, center, traveling(1.1, 0.2, (740, 760))
            pause 0.2
            show master at center, zoomAt(1.0, (940, 860)), startle
            "She shoots out from behind me and kicks him square in the groin."
            show master angry
            master.say "Oooh..."
            master.say "Right in the sacred scrolls!"
            hide master with moveoutbottom
            "He collapses into a heap on the sand."
            "And that's where he stays, clutching at his groin."
            show lexi angry
            lexi.say "That's not nearly as much as you deserve, old man!"
            lexi.say "Next time, I'll cut them off with a rusty hacksaw!"
            show lexi annoyed at center, traveling(1.5, 0.3, (640, 1040))
            "That done, she takes hold of my arm."
            "And then she leads me off down the beach."
            "As we walk the sound of the Masters groans fade into the distance."
            "And as they do, I can feel my mood improving more with each passing moment."
            $ game.flags.pimpingmaster = False
    return

label lexi_sasha_samantha_nightclub:
    "You know those nights when you're just not feeling it?"
    "The ones where, no matter how hard you try, it's just not working?"
    "Well, this isn't one of those nights!"
    "Tonight I feel like the stars have aligned and I can do no wrong."
    "It's late, I've got a real buzz going on, and the music is hitting the spot."
    "Oh yeah, sorry..."
    scene bg nightclub with fade
    "I should have mentioned already - I'm in a nightclub."
    "Truth be told, I can't exactly remember who I actually came here with."
    show 3dance lexi sasha with dissolve
    "But my gaze is filled with the sight of Sasha dancing to my left."
    "Sasha - all dark, gothic and mysterious."
    "And Lexi doing something that should really involve a stripper's pole to my right."
    "Lexi - oozing the kind of sex-appeal that probably should be illegal!"
    "They're dancing together, like they're feeding of each other's energy."
    "And the best thing of all is that they're dancing with me too!"
    "That is if you can call what they're doing actual dancing."
    "My guess is that if we were doing the same stuff on the horizontal as we are the vertical..."
    "Well, you get the picture, right?"
    "Maybe I should be trying to sober up and reign it in, before this gets out of hand."
    "But the time for that was probably more than a couple of drinks ago."
    "And now the only way I can see this ending is when the club closes in the early hours of the morning."
    "Either that or when we get thrown out of the place for committing an outrage against common decency!"
    "The only time that I take my eyes off of Sasha and Lexi is to check out the faces in the crowd."
    "Yeah, I admit it - I'm getting off on the looks that we're attracting."
    "I can see both guys and girls watching us with obvious envy in their eyes."
    "And can you really blame them?"
    "Sasha and Lexi are both hot in their own unique ways."
    "But right now they're doing the best they can to outdo each other on the dance-floor."
    "They have to keep their rivalry civil, making it look like they're the best of friends."
    "And yet the need to compete that exists between them is making the show all the more intense and exciting!"
    "The smile on my face is pretty much fixed as I watch them."
    "It feels almost surreal that they're both trying to impress me!"
    "But the next time I steal a glance at the crowd, my smile begins to fade a little."
    "And that's because I recognise one of the faces staring back at me across the dance-floor."
    "Is that...yes, it is - that's Sam!"
    "Her expression is different to those of the other onlookers."
    "It's somehow more subtle, meaning that I can't make it out from this distance."
    "Which shouldn't be a problem for much longer, because she's already coming closer."
    "In the few seconds that I have before Sam closes the distance between us, my mind is racing."
    "Did she just happen to be in the same place as me tonight?"
    "Did I tell her what my plans were, thinking that she'd never turn up?"
    "Or has she been following me the whole time, waiting to catch me in the act?"
    "Just as Sam makes it over to where we're dancing, Sasha and Lexi notice that something's up."
    "And as one, they turn to look in the direction that I'm staring too."
    scene bg nightclub
    show lexi date at center
    show sasha date at right
    with fade
    "This means that they're treated to the sight of Sam striding up."
    show samantha date a annoyed at left with moveinleft
    "She has her arms crossed over her chest, and the look on her face says she means business..."
    if samantha.flags.nonexclusive:
        if samantha.flags.nickname == "cupcake":
            mike.say "C...Cupcake..."
        else:
            mike.say "S...Sam..."
        mike.say "What are you doing here?!?"
        "It seems as though my astonishment amuses Sam."
        show samantha normal
        "She smiles slowly, glancing from Sasha to Lexi and then back at me."
        samantha.say "Oh, let's just say that I was curious."
        samantha.say "You know, after we agreed seeing other people was cool?"
        mike.say "Oh...yeah..."
        if samantha.flags.nickname == "cupcake":
            mike.say "Of course, Cupcake."
        else:
            mike.say "Of course, Sam."
        mike.say "We did say that - didn't we!"
        show fx question at left
        samantha.say "Well?"
        samantha.say "Aren't you going to introduce me to your friends?"
        "I nod eagerly, thankful to be well and truly off the hook."
        if Harem.find(samantha, name='home'):
            mike.say "You already know Sasha, and this is Lexi."
            show sasha happy
            sasha.say "Hi, Sam!"
            show lexi happy
            lexi.say "Hey there!"
            mike.say "Lexi - this is Sam."
            mike.say "I've...well...kind of been seeing Lexi too at the same time!"
        else:
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake, this is Sasha and Lexi."
            else:
                mike.say "Sam, this is Sasha and Lexi."
            show sasha happy
            sasha.say "Hello, Sam."
            show lexi happy
            lexi.say "Hey there!"
            mike.say "Sasha. Lexi - this is Sam."
            show sasha normal
            show lexi normal
            mike.say "I've...well...kind of been seeing you all at the same time!"
        "I've been inside of a packed nightclub, dancing for what feels like hours."
        "So why is it only now that I can feel myself starting to sweat?"
        show sasha flirt
        show lexi happy
        "Now I can see the knowing smiles spreading on Sasha and Lexi's faces too."
        samantha.say "What?"
        samantha.say "Did this naughty boy not tell you about me?"
        if not Harem.find(samantha, name='home'):
            sasha.say "Nah, of course not!"
        lexi.say "I kinda wish he had!"
        samantha.say "Well, it sounds like you're handling it well enough."
        samantha.say "What do you say the four of us make up for lost time?"
        "I blink a couple of times at this, not really sure what's going on."
        "Did I just become part of a foursome?"
        "Without even saying a word?"
        "As if in answer to the unspoken question, Sam move closer to me."
        "She's dancing before I know it, matching anything the others have already pulled off."
        "Sasha and Lexi don't seem to need telling, and start to dance around me too."
        "And so all that I can do is shrug and join them."
        "Looks like I don't really have a say in the matter."
        "Not that I'm objecting!"
        $ game.pass_time(1)
        $ game.active_date.stay_coffee = False
        call foursome_lexisamsasha from _call_foursome_lexisamsasha_3
    else:
        if samantha.flags.nickname == "cupcake":
            mike.say "Wha...ah...Cupcake!"
        else:
            mike.say "Wha...ah...Sam!"
        mike.say "What are you doing here?"
        "Sam cocks her head on one side, her expression impossible to read."
        "She takes a moment to look Sasha and Lexi up and down."
        "And I'm amazed to see that they both avoid her gaze."
        "It's like there's some secret female body-language going on here."
        "And the pair of them know it means they're in deep trouble right now!"
        "But then her eyes are back on me."
        "And in that moment, I feel the exact same way as Sasha and [bree.name]."
        show samantha angry
        samantha.say "That's not the question, is it, [hero.name]?"
        samantha.say "The question's what are YOU doing here?"
        samantha.say "Oh, and what are you doing with these two sluts?"
        show lexi annoyed
        lexi.say "Hey..."
        "At the sound of Lexi's protest, Sam turns and glares at her."
        show sasha annoyed
        sasha.say "Ah, Lexi..."
        sasha.say "Let's go grab a drink, yeah?"
        hide lexi
        hide sasha
        show samantha angry at center
        with moveoutright
        "With that, they scuttle off together."
        "Which leaves me to face the fuming Sam alone."
        if samantha.flags.nickname == "cupcake":
            mike.say "Cupcake, I..."
        else:
            mike.say "Sam, I..."
        with hpunch
        "I hear the sound of the slap before I feel it."
        "My head turning from the blow as the pain begins to become real."
        show fx anger
        samantha.say "How could you do that, [hero.name]?"
        samantha.say "How could you lie to me after you gave me your word?"
        if samantha.flags.nickname == "cupcake":
            mike.say "Cupcake...I...I thought..."
        else:
            mike.say "Sam...I...I thought..."
        samantha.say "You thought I'd never find out."
        samantha.say "That's what you thought!"
        if samantha.flags.nickname == "cupcake":
            mike.say "Please, Cupcake..."
        else:
            mike.say "Please, Sam..."
        mike.say "I can explain!"
        show fx anger
        samantha.say "What, like Ryan tried to explain?"
        samantha.say "Save us both the wasted time, [hero.name]."
        samantha.say "Let's just skip to the part where I tell you it's over."
        samantha.say "The part where I don't have see your face anymore!"
        hide samantha with moveoutleft
        "And with that, she turns on her heel and storms off."
        "Which leaves me standing alone in the middle of the dance-floor."
        "Alone and amazed at the complete one-eighty my night just took..."
        $ samantha.set_gone_forever()
        $ game.active_date.stay = False
        if date_girl:
            $ renpy.hide(date_girl.id)
        if active_girl:
            $ renpy.hide(active_girl.id)
        $ game.room = game.room.replace("date_", "")
    return

label foursome_lexisamsasha:
    scene bg house with fade
    "I think it kind of helps that we're all a little drunk when we pile in through the door and head upstairs."
    "The whole thing of Sam getting in on the action with Sasha, Lexi and myself just seems a little unreal."
    "And so having more than a couple of drinks still affecting my judgement makes it that much easier to handle."
    "Don't get me wrong, I'm not saying that there's anything I don't like about the idea."
    "It's just hard to actually believe that I'm about to fool around with three girls at once!"
    "I mean, any one of them would be a serious win even on their own."
    "And two of them would be a dream come true."
    "But all three?"
    "It's mind-blowing!"
    scene bg bedroom1 with fade
    "In fact, my mind still seems to be reeling from it once we're through the door to my bedroom."
    show samantha date with dissolve
    samantha.say "Come on, [hero.name] - what are you waiting for?!?"
    "I shake my head and hurry to follow Sam into my room."
    "Funny - I'd have expected it to be Sasha or me that was taking the lead here."
    "After all, it is our place where the actions about to take place."
    "But Sam seems to still have that same air of authority about her she had back in the nightclub."
    "Even Lexi, who's normally more forward than is strictly healthy, is following in her wake."
    if samantha.flags.nickname == "cupcake":
        mike.say "I...I'm coming, Cupcake!"
    else:
        mike.say "I...I'm coming, Sam!"
    samantha.say "Geez, I've heard of premature ejaculation."
    show samantha happy
    samantha.say "But that's just ridiculous!"
    show sasha date happy at left
    show lexi date happy at right
    "It's a cheap joke, but Sasha and Lexi burst out laughing all the same."
    lexi.say "Aww, save some for us, [hero.name]!"
    sasha.say "Yeah, don't go blowing your load over the trailers."
    sasha.say "Save it for the main feature!"
    mike.say "Ha ha, guys."
    mike.say "Keep this up and none of you are going to get any cock tonight!"
    "I see their eyes go wide at my petulant little threat."
    "The three of them exchange amused glances, shaking their heads the whole time."
    "But it's Sam that takes the first step, maintaining her role as alpha female."
    samantha.say "Oh no you don't."
    samantha.say "There's no way you're keeping that thing to yourself!"
    "And with that, she grabs a handful of my shirt."
    "With her free hand, she waves to Sasha and Lexi."
    samantha.say "Someone left us a present, girls."
    samantha.say "What do you say we unwrap it?"
    "This gets another round of giggles from Sasha and Lexi."
    "And they advance on me from both sides, eager to do Sam's bidding."
    "What follows is a speedy and ruthless stripping off of all that I'm wearing."
    "One moment I seem to be standing there fully dressed."
    "And the next I'm completely naked."
    "Sam seems to have left most of the stripping to the other girls, as she's almost naked too."
    "She wastes no time in shoving me square in the chest, sending me tumbling backwards."
    "Luckily for me, the bed is there to break my fall."
    "But still, I swear that Sam's on me before I've even hit the mattress."
    samantha.say "I call dibs on his cock."
    samantha.say "Any objections?"
    scene foursome lexisamsasha with fade
    "Sam's laid atop me as she says this, grabbing my dick with her hand."
    "And I can tell you that if anyone objects, it certainly won't be me!"
    "But the lead that Sam's taken still seems to be enough to keep the others in line."
    "No one challenges her claiming of my cock, but Sasha jumps in a moment later."
    sasha.say "I claim the mouth!"
    show foursome lexisamsasha lexiblush
    lexi.say "Aww, no fair!"
    lexi.say "What do I get - his asshole?!?"
    "Sam chuckles with satisfaction as she begins to rub my cock up and down."
    "That and the look of amusement on her face give her a distinctly feline aspect."
    "You could seriously stick ears and whiskers on her right now and it'd finish off the look!"
    samantha.say "Ah, come on, Lexi."
    samantha.say "You look like the kind of girl that can improvise."
    samantha.say "You know, get lemons and make lemonade?"
    "Lexi looks like she's about to say something pointed in return."
    "But it's at that very moment Sam lowers herself onto me."
    "She guides my now rock-hard cock straight towards the lips of her pussy."
    "And it doesn't take me long to realise that she's every bit as wet as I am hard!"
    mike.say "Oh, fuck..."
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake...that feels amazing!"
    else:
        mike.say "Sam...that feels amazing!"
    "Sam gives Lexi one last smile as she sinks down and onto me."
    "The fact that I'm now well and truly inside of her seeming to settle the argument."
    "That done, she beckons Sasha over with a single finger."
    samantha.say "Sasha, how about you shut him up, huh?"
    samantha.say "Maybe give him something useful to do with his mouth?"
    "By now, Sasha and Lexi are as naked as Sam and me."
    "And Sasha doesn't need to be told twice to get involved in the action."
    "She also doesn't need to have what Sam meant by that last comment spelled out either!"
    show foursome lexisamsasha sashablush
    sasha.say "Don't worry, Sam."
    sasha.say "I know just the thing!"
    "Sasha pushes her herself towards me, catching my head between her thighs."
    "Pretty soon all I can see is the lips of her pussy as they close in on my face."
    "It fills my senses, and the musky scent of her is all that I can smell."
    "I don't have time to open my mouth before Sasha almost sits on my face."
    "Which means that I pretty much kiss her lower lips with my own!"
    "There's nothing else that I can do but what's being demanded of me."
    "And so I part my lips and push my tongue against Sasha's pussy."
    "She must have been more than ready for this, because she moans almost in the same instant."
    "Her folds are already moist and the lips ready to part, letting my tongue slip inside."
    "I can taste the bitterness of her pussy, feel it seeping down my throat."
    "It's like I'm drinking Sasha down with every swallow, and I want to drink her dry!"
    show foursome lexisamsasha samanthapleasure
    "My tongue starts to move inside of her in time with my cock inside of Sam."
    "When she forces herself down upon me, I thrust that much deeper into Sasha too."
    show foursome lexisamsasha sashapleasure
    "The effect is made that much more powerful by their competing moans and cries."
    "To me they sound like a pair of desperate sirens, trying to lure me to my doom!"
    "But all the same, there's a difference to the sounds that Sasha's making."
    "I have to struggle to make it out, but she definitely sounds more rasping than Sam."
    "Opening my eyes, I find that I can just make out Sasha's face looming over me."
    "A hand is clutching at her throat, and it takes me a moment to realise it's not her own."
    "My eyes follow the arm the hand's attached to, discovering Lexi at the other end."
    "Is she..."
    "Yes, she is - she's choking Sasha!"
    "It takes me a couple of seconds to recall that it's something Sasha actually likes."
    "Sure, her eyes are bulging from the pressure being exerted on neck."
    "But she's clearly enjoying the sensation almost as much as the oral I'm giving her!"
    "At least I hope she's not enjoying it more!"
    "It's then that Lexi notices me watching what she's doing."
    "Maybe she senses this is her moment to snatch a bit of the limelight?"
    "A chance perhaps to get her own back on Sam for relegating her to third place?"
    "Either way, she holds my eye as she leans in closer to Sasha."
    "At first I think she's going to begin kissing the other girl."
    "But then she pauses and begins to hock up in her own mouth."
    show foursome lexisamsasha lexidrool lexipleasure
    "Still holding my eye, Lexi then spits straight between Sasha's open lips."
    "She dribbles the saliva in there, taking her time and making the spectacle last."
    "All that Sasha can do is try to keep from choking as she's forced to swallow Lexi's spit."
    "I don't honestly know whether to be grossed out or turned on by the sight."
    with vpunch
    "But within moments, that becomes a moot point as I can feel myself cumming."
    with vpunch
    "The cries coming out of Sam reach a crescendo as I let go inside of her."
    with vpunch
    "But I can't be sure if the sounds coming from Sasha are on account of my tongue."
    with vpunch
    "For all I know, they could be from her gagging on the load Lexi just spat into her mouth!"
    "Whatever the cause, I gasp for breath as soon as she releases me from between her thighs."
    "All I can do in the moments after my climax is lie on my back panting and spent."
    "I barely feel Sam as she slithers off of me and collapses at my side."
    "Taken together, the sound of the four of us is quite something to hear."
    "In any other situation, we could easily be mistaken for having just run a marathon."
    "And maybe the feeling of utter exhaustion would be the same too."
    "But I take great pleasure in the fact that everyone's wearing a satisfied expression."
    "Maybe there's something to this idea of a foursome after all?"
    $ samantha.sexperience += 1
    $ DONE["foursome_lexisamsasha"] = game.days_played
    call sleep (["lexi", "samantha", "sasha"]) from _call_sleep_foursome_lexisamsasha
    return

label lexi_trailer_on_fire:
    show lexi sad a -c
    "When I lay eyes on Lexi, it comes as a shock to see that she's in a pretty bad state."
    "Yeah, yeah - I know that Lexi's not exactly what you'd call a refined sort of girl."
    "She lives in a trailer park and dresses like hot trash - she's pretty much a walking stereotype."
    "Even so, she always makes it look good, owning the image and oozing sex-appeal."
    "But right now, the only thing Lexi's oozing is exhaustion and nervous energy."
    "I hurry up to her, worried about what she's going to have to tell me."
    mike.say "Lexi, my god!"
    mike.say "Are you okay?"
    mike.say "What happened to you?"
    "Lexi shakes her head at this, letting out a rueful chuckle."
    lexi.say "I look that bad, huh?"
    "I instantly regret what I just said to Lexi."
    "Her expression making me realise just how insensitive it sounded."
    mike.say "Ah, hell..."
    mike.say "I'm sorry, Lexi."
    mike.say "I was just surprised to see you like this, that's all."
    lexi.say "It's okay, [hero.name]."
    lexi.say "I know where you're coming from."
    lexi.say "I've had a pretty bad time of it over the last day or so."
    lexi.say "You're one of the first people to actually ask if I was okay!"
    lexi.say "Can you believe that?!?"
    mike.say "What happened, Lexi?"
    show lexi annoyed a -c
    lexi.say "Well, the main thing is that my trailer burned down."
    lexi.say "All the rest of it kind of follows on from that!"
    "My eyes go wide at the news of Lexi's home being consumed by fire."
    "Sure, it was only a trailer - but it was all she had to call home."
    mike.say "What?!?"
    mike.say "How on earth did that happen?"
    lexi.say "All I know is that I didn't do it by smoking in bed."
    lexi.say "I got home the other night...well, I got to where home should have been."
    lexi.say "And all I found was a heap of burnt crap."
    lexi.say "Now I'm homeless, and everything I owned was in there too!"
    "Lexi's story sets my mind racing as to the possibilities."
    "Sure, it could have been nothing more than an unfortunate accident."
    "But she's made a habit of mixing with some shady characters in the past."
    "There's that, and the fact that she's not shy of screwing people over too."
    mike.say "You don't think it could be anything to do with Danny, do you?"
    lexi.say "Not unless he's come back as a zombie or something!"
    lexi.say "We took care of that jerk, remember?"
    mike.say "Not Danny himself!"
    mike.say "I was thinking of any buddies he had."
    mike.say "Could they be out for revenge on you and me?"
    show lexi sad a -c
    "Lexi shrugs helplessly at the question."
    "And I see again just how exhausted and weary she looks."
    lexi.say "I dunno, [hero.name]."
    lexi.say "All I do know is that I'm tired and I want to crash somewhere."
    lexi.say "Would you let me come to your place so that I could grab a shower?"
    lexi.say "I promise I won't be any trouble."
    lexi.say "I'll even sleep on the couch if you want!"
    menu:
        "Of course you can come!":
            "There's no question about it, I have a duty to do all I can to help Lexi."
            "I was the one that came into her life and aided her in getting rid of Danny."
            "So I can't chicken out now and leave her to face the consequences alone."
            "And more importantly, I want to keep her safe because of my feelings for her."
            mike.say "Of course you can come back to my place, Lexi."
            mike.say "I want to keep you as safe as I can and as close as I can."
            mike.say "Don't worry about anything - I'll protect you."
            "I half expect Lexi to make some kind of joke out of my proclamation."
            "She's not usually the kind to need a champion fighting her corner."
            show lexi happy close
            "But instead she throws her arms around me and hugs me tight."
            lexi.say "Oh, thanks, [hero.name]!"
            lexi.say "You're the greatest."
            "I put my arms around Lexi, stroking her hair and patting her back."
            "Is it wrong that I'm actually liking the way that she's throwing herself at me right now?"
            "For a moment I almost forget that this is a serious matter, just enjoying the sensation."
            "But then I force myself to stop imagining just how grateful Lexi might prove to be."
            "She came to ask for my help, and only a true creep would take advantage of her in a time of need."
            mike.say "We can sort out where you'll sleep when we get back to my place."
            mike.say "Don't worry about any of that stuff right now."
            show fx question
            show lexi annoyed blush
            lexi.say "What about your housemates?"
            lexi.say "Won't they mind me staying?"
            mike.say "I'll talk to them."
            mike.say "I'm sure they'll want to help out too."
            show lexi normal
            "Lexi nods as she releases me from her embrace and takes my arm."
            "We start towards my place, with her leaning against me."
            "And I try to focus on the problem at hand, rather than the sensation of her beside me."
            "But all the same, it's a task that proves challenging in the extreme."
            $ game.flags.asklexiinhomeharem = True
            $ game.flags.ongoinghomeharem = "lexi"
            $ lexi.flags.trailer = False
        "It's not possible.":
            "I want to help Lexi in any way that I can."
            "But what if this really is some kind of revenge attack?"
            "I don't want have the house I live in burned down too!"
            mike.say "I can't put you up right now, Lexi."
            mike.say "The house is really crowded as it is."
            show lexi annoyed a -c
            lexi.say "Aw..."
            show fx exclamation
            lexi.say "Please, [hero.name]!"
            lexi.say "You're the only decent guy I know!"
            "I shake my head, trying to end the debate."
            mike.say "It's not just that, Lexi."
            mike.say "You might not be safe at my place."
            lexi.say "Huh?"
            lexi.say "What do you mean?"
            mike.say "Well, what if this is someone trying to get you because of Danny?"
            mike.say "If so, they probably already know I was involved and where I live."
            show lexi sad a -c
            "Lexi nods her head slowly, beginning to see my point."
            lexi.say "They might set fire to your house too!"
            mike.say "Exactly my point."
            mike.say "Look, I'll take you to a hotel or something and rent you a room."
            mike.say "We can figure out what to do next once you're rested."
            "Lexi nods again, now keen to see my plan through."
            "I just hope that I'm right in thinking that this is the right thing to do."
            $ game.flags.lexirefusedinhomeharem = True
    return

label lexi_dwayne_event:
    scene expression f"bg {game.room}"
    "Closing the deal had kept both myself and Aletta up for almost twenty four hours before it was finally all signed and sealed."
    "Getting to spend so much time in her company would have been welcome, if we'd been doing almost anything other than slaving over the final, excruciating details."
    "As usual, Dwayne was sure to come sweeping in at the very end, all fake smiles and alpha male bullshit, making certain his face was the one that everyone saw."
    "I think all anyone else wanted to do was go home and collapse into bed."
    "But Dwayne wanted to go out to a favourite nightclub of his and celebrate."
    "And as Dwayne is the boss - what he wants, he gets."
    $ game.hour = 22
    scene bg black with timelaps
    scene bg nightclub with timelaps
    "As I barge through a crowd of fellow club-goers to get to the bar, I'm at least thankful that Dwayne has a booth in the VIP section of the club."
    "He ordered something expensive and sparkling from one of the waitresses as soon as we got in there."
    "But I used the chance to get something else as an excuse to escape his overbearing personality for a couple of minutes."
    "Shouldering my way to the bar, I resign myself to waiting for the chance to catch the bartender's eye."
    lexi.say "Well, don't you look like the bigshot businessman tonight!"
    "It takes me a moment to realise the comment is aimed at me, and I glance round absently to discover its source."
    show lexi date with dissolve
    "I instantly recognise Lexi, the less than respectable girl that brought so much disruption and chaos into my life recently."
    "But also the irresistibly loose and uninhibited trailer-park princess that I can't help getting stiff at the mere thought of too."
    mike.say "What...oh, this?"
    "I gesture to my crumpled shirt and trousers, thinking that, to her, this must be the epitome of office-culture smartness."
    mike.say "I just got off of work...I'm here with some colleagues."
    mike.say "What about you?"
    show lexi flirt
    lexi.say "Oh, you know - little bit of this, little bit of that...little bit of the other!"
    show lexi wink
    "She gives me a lewd wink that reminds me of the fact she's not above accepting compensation for her attentions."
    mike.say "Okay, whatever - you keep yourself safe, Lexi."
    show lexi normal
    lexi.say "Don't worry, I always do!"
    mike.say "Well, maybe I'll see you later - for a dance or something?"
    lexi.say "Sure...I like the sound of 'or something' best!"
    "I shake my head at her and laugh, picking my way back to the VIP booth."
    scene bg vip
    show aletta date normal blush
    with fade
    "When I get back, Aletta seems to already be on the way towards being drunk."
    "I don't know if it's more from being dead tired, or else from the need to tolerate Dwayne's being a domineering asshole his every waking moment."
    show dwayne at left with dissolve
    dwayne.say "Hey, [hero.name] - who was that little tramp you were talking to at the bar?"
    mike.say "Oh, you saw that?"
    dwayne.say "I never miss seeing a woman, believe me on that."
    mike.say "Ah, her name's Lexi...I kind of know her a little, I guess."
    dwayne.say "How's she to fuck?"
    "The bluntness of the question takes me by surprise."
    mike.say "How did you..."
    dwayne.say "How did I know that you've fucked her?"
    "He smiles that familiar smile, all expensive cosmetic dental-work and shit-eating confidence."
    dwayne.say "Simple matter of reading both of your body language, seeing the way you instinctively leaned in towards each other, shit like that."
    dwayne.say "She turns tricks, doesn't she?"
    mike.say "Well...she used to..."
    dwayne.say "I bet you more than you made last month that she still does!"
    mike.say "Hey!"
    dwayne.say "Calm yourself down, I didn't mean anything by it!"
    dwayne.say "Tell you what - why don't you go ask her to join us?"
    "I hesitate for a moment, worried about putting Lexi in the orbit of a sexually voracious prick like Dwayne."
    "But then I reason that there's nothing to stop him tracking Lexi down on his own."
    "And if I'm here, with Aletta as well, maybe he'll think twice about pushing himself on her."
    show lexi date at right with fade
    "So a few minutes later, Lexi finds herself sitting in the booth with us."
    "I introduce her to Dwayne and Aletta, keeping my description of them to the basic facts."
    "My guess is that Lexi's wise, or jaded enough to pick up on the sexual dynamics that already exist between Dwayne and Aletta."
    "It's the one between Aletta and myself that I'm hoping she's less sure of."
    "Aletta pretty much ignores Lexi after that, leaving her to have a typically one-sided conversation with Dwayne, that I try to pitch in on when the chance arises."
    "I'm not really listening when Dwayne says something to Lexi which changes the tone quite suddenly."
    show lexi angry at right, hshake
    lexi.say "You want me to do what?!?"
    dwayne.say "Whoa, why the big blow up?"
    dwayne.say "All I did was ask you how much for a fuck!"
    dwayne.say "I know how it is and how this works...it's just a straight-up fuck in the privacy of the booth, nothing fancy."
    dwayne.say "Come on, [hero.name] - don't either of you act the innocent, it's just like any other business proposition."
    "Lexi drags me into a corner, away from Dwayne's hearing."
    hide dwayne
    hide aletta
    show lexi at center
    with fade
    mike.say "I'm sorry, okay - I had no idea he wanted to proposition you like that, honestly!"
    show lexi annoyed
    lexi.say "Urrgh, how many times do you need to be told - I'm fine with making money like this."
    show lexi normal
    lexi.say "I was just playing it shocked back there because I thought he might be into it!"
    lexi.say "So...what do you think?"
    lexi.say "Should I do it or not?"
    menu:
        "Do it":
            mike.say "He's a grade A asshole, but you've probably dealt with worse than him before."
            show lexi happy
            lexi.say "Yeah, Danny'd have used his dick as a toothpick."
            "I try not to wince at the mental image that conjures."
            mike.say "I suppose it's just business, Lexi."
            mike.say "I can tell you as well that he's fucking loaded."
            mike.say "So if you want the money, I won't stop you."
            show lexi normal
            lexi.say "And you're okay with it?"
            "I look at her in genuine surprise."
            lexi.say "Don't think I'm growing a conscience - he's your boss, I don't want it to get awkward for you."
            mike.say "It already is awkward, believe me."
            "I hustle Lexi back to where Dwayne is sitting before she can ask me what I mean."
            show dwayne at left
            show lexi at right4
            with fade
            dwayne.say "Well?"
            "In way of answer, Lexi saunters over and sits on his lap, being sure to bounce enough to make her breasts jiggle an inch from his face."
            "Dwayne doesn't need to be led by the hand, and he responds by brazenly yanking off her T-shirt and pulling down the straps of her bra."
            show lexi topless with dissolve
            "Her large, heavy breasts spill out and she laughs, but I notice not without a little nervousness."
            "I watch as Dwayne continues to undress Lexi, peeling her like a delicate fruit he's not afraid to bruise in the process."
            show lexi naked with dissolve
            "Soon she's utterly naked, still sitting upon his knee."
            "Dwayne amuses himself by squeezing her exposed breasts with one hand and stroking between her thighs with the other."
            if lexi.is_visibly_pregnant:
                "Dwayne pauses for a second, placing his hand on the curve of Lexi's rounded belly."
                dwayne.say "Hey, you're not just extra thick, are you?"
                dwayne.say "Who got you in the family way, Lexi?"
                "Lexi is suddenly struck silent, not used to being questioned about her pregnancy in a situation like this."
                "She shoots a brief glance at me, and that's all Dwayne needs to answer his question."
                dwayne.say "[hero.name], you stud!"
                "I can see from the evil glint in his eye that this revelation isn't going to keep Dwayne from having his way with Lexi."
                "Indeed, it's going to make screwing her in front of me all the more enjoyable for him."
                "Dwayne stands up and proceeds to strip his clothes off without a hint of modesty."
                "Once he's naked, I see Lexi's eyes visibly widen at the size of his penis."
                "Maybe she thought he'd prove to be all talk and gym sculpted muscles."
                dwayne.say "Don't worry, little lady - I promise to be gentle!"
                "He looks my way as he says this, clearly speaking more to me than to Lexi."
                "Dwayne guides Lexi down onto the closest couch so that she's on all fours and looking straight at me."
                "I don't know if it's the sight of Lexi herself or the opportunity to humiliate me, but either way he's having no trouble getting an erection."
                "His massive cock bobs and swings above Lexi's exposed buttocks like a sexual battering-ram."
                "I can't help noticing the similarity in the way the light reflects off both Dwayne's head and the helmet of his dick at the same time."
                dwayne.say "Here I come, girl - see if you can tell when I get there!"
                scene nightclub threesomelexi dwayne
                show nightclub threesomelexi dwayne naked
                with fade
                "Lexi might have been about to say something in return, but all she manages to let out is a strangled cry as Dwayne forces his way into her."
                "I can't tell how ready she was for him, but he doesn't stop or pause for as much as a second."
                "Lexi's eyes are fixed on mine as she endures the sensation of his huge size being thrust mercilessly into her pussy."
                "But when I glance up, I can see Dwayne's eyes are on me as well."
                "He's simply loving the fact that I'm watching him fuck the girl that's already pregnant with my baby."
                "I've only ever heard of what Dwayne's like in terms of sex from Aletta, and even though she was scathing, she didn't do him justice."
                "Dwayne pounds away at Lexi as though he's working out at the gym, working her like she's an exercise machine and he needs to get his reps in."
                "Lexi seems to be animated solely by the presence of his cock inside of her, swaying and bouncing to its relentless rhythm."
                show nightclub threesomelexi dwayne ahegao
                "I know that she's some kind of crazy sex-machine in her own right, but it looks like Dwayne's going to cause her to malfunction badly."
                "The spell is broken, however, when I feel something clawing at the front of my trousers."
                "I look down to see that Lexi is using one hand to desperately open my flies."
                "That done, she pulls out my own dick and begins to minister to it with her lips and tongue."
                "Without thinking, I look up to see what Dwayne's reaction will be."
                "He looks suitably pissed for a moment, but then I see the same fake expression of friendliness that he uses in the office slide over his features."
                "I realise that by trying to appear so sexually uninhibited and open, he's backed himself into a corner from which he can't object to what Lexi's doing without blowing the whole thing."
                "I close my eyes and try to forget that he's there at all, just allowing the sensation of Lexi's expert mouth around my cock carry me away from the moment."
                "The feeling comes to an end just before I feel myself about to cum."
                show nightclub bj lexi dwayne naked with fade
                "My cock is unceremoniously yanked out of Lexi's mouth as Dwayne almost shoves her onto the floor."
                show nightclub bj lexi dwayne cum with hpunch
                "The effect is that she ends up kneeling before us, my climax hitting her on the left cheek a second after Dwayne's hits her on the right."
                show nightclub bj lexi dwayne ahegao with hpunch
                "The expression on her face might have been comical for its unpreparedness and surprise as the cum splatters her from two angles at once."
                "As it is, I can't help feeling like she's being metaphorically slapped in the face, twice over."
            else:
                "Dwayne grins as he bounces Lexi up and down on his knee, leering on the way it makes her bounce and sway."
                dwayne.say "Make no mistake, baby - I'm going to enjoy having you!"
                "He looks at me the whole time, making it plain he's actually more interested in my reaction to his words than Lexi's."
                "Dwayne proceeds to strip off without a hint of shame or embarrassment, showing off his gym-built body and even more so his reputedly enormous cock."
                "Which only remains reputedly enormous until the moment I catch an unwanted view of it, almost mistaking it instead for a small elephant's trunk."
                "He sees the look of genuine surprise on Lexi's face as she too catches sight of it."
                dwayne.say "Don't be disappointed, little lady - it does get bigger...much bigger!"
                "With that he pushes Lexi down so that she's crouching on all fours on the nearest couch."
                "Dwayne doesn't waste time with any foreplay, instead simply lining up his now massively erect dick with Lexi's exposed pussy and forcing his way into her."
                "Lexi actually yelps and cries out in pain as she's made to take him in without pause, her muscles quivering in sympathy with her pussy, making her shake visibly."
                scene nightclub threesomelexi dwayne
                show nightclub threesomelexi dwayne naked
                with fade
                "Dwayne grins at me as he begins to thrust into her, eliciting yet more cries and moans from Lexi."
                "I've seen that same expression on his face before, when he's mercilessly crushing someone else's ambitions in the workplace."
                "There he likes to make a show of it and impress upon his colleagues his alpha male status, and it looks like sex, for him, is more of the same."
                "I've never seen Lexi in a state like this before, as Dwayne exposes her to the evident stamina of his gym-crafted physique."
                "Usually she's good at putting on the moans and pants to flatter her partner, but the sounds she makes now are ragged, pained and very real in nature."
                show nightclub threesomelexi dwayne ahegao
                "Lexi's breasts swing almost violently, slapping against one another and her legs are visibly trembling now."
                "Dwayne's grin is now pretty much a lascivious leer, as he wallows in what he's doing to Lexi right before my eyes."
                "His expression sours a moment later, when he sees that Lexi is desperately tugging at my flies."
                "Surprised by this, I offer no resistance as she pulls out my own dick and begins to bring it to life with her lips and tongue."
                "Dwayne deliberately breaks eye-contact then, looking away in annoyance."
                "It's then I hear a stifled moan coming from elsewhere in the room."
                "Glancing over his shoulder, I see Aletta, sitting on the couch opposite."
                "She's clearly watching the proceedings, probably glad not to be playing the part of Dwayne's fuck-toy for once."
                "As I watch, I can see that she's trying to keep still."
                "But one of her hands is hovering around her huge breasts, while the other is creeping towards her groin."
                "She's obviously getting massively turned-on by watching, trying to keep herself from touching herself."
                "I can't be sure if she's imagining herself taking one from Dwayne or else giving me a blowjob."
                "Suddenly I hit upon an idea to find out which."
                "Making sure I have Aletta's eye, I mouth the words 'I wish this was your mouth', while pointing at the top of Lexi's head."
                "Aletta makes an almost unconscious nod, and finally she can't keep her hands at bay any longer."
                "She begins to immediately massage her right breast, fingers pinching harshly at the stiffening nipple."
                "At the same time she openly rubs herself through the crotch of her trouser-suit's pants."
                "Aletta's moaning is too low to reach Dwayne's ear, but I can pick it out thanks to looking straight at her."
                "Lexi's expertise at giving a blowjob might be arousing me physically."
                "But I have to admit to feeling guilty that it's the sight of Aletta openly masturbating before me that's arousing my mind."
                show nightclub bj lexi dwayne naked with fade
                "Before I can lose myself in Lexi's mouth, Dwayne pulls her onto the floor so that she's kneeling between us."
                show nightclub bj lexi dwayne cum with hpunch
                "Lexi takes my ejaculation on one cheek and Dwayne's on the other within mere seconds of each other."
                show nightclub bj lexi dwayne ahegao with hpunch
                "She doesn't even have time to react, her dazed expression twisting into a grimace as she's painted white."
        "It's not a good idea":
            mike.say "No, I think you should tell him to get lost."
            show lexi normal
            lexi.say "Be honest - are you just saying that because he's your boss and you hate him?"
            mike.say "I won't deny that's a part of it, yeah."
            mike.say "But he's a world-class prick too."
            mike.say "Plus he's already fucking Aletta over there too, and treating her like shit whenever he gets the chance."
            "Lexi glances over at Aletta, earning herself a frosty stare for her troubles."
            lexi.say "No kidding...she looks like she's been chewing a wasp!"
            mike.say "Look, Lexi - it's up to you whether or not you take Dwayne's money."
            mike.say "I'm just saying it'd be a lot more pleasant for both of us if you didn't."
            lexi.say "Okay, it's not like I'm lacking in potential customers anyway."
            lexi.say "Tell him no way."
            "We walk back over to where Dwayne and Aletta are sitting, with me trying not to contemplate the implications of Lexi's last statement too closely."
            show dwayne at left
            show aletta date at center
            show lexi date at right
            with fade
            dwayne.say "Well, what do you say?"
            mike.say "The answer's no, I'm afraid - she's not for sale tonight."
            dwayne.say "You say that like you're her goddamn pimp or something...are you her pimp?"
            "The implications of what Dwayne could tell the police suddenly occur to me, but I hit back with the implications for him in turn."
            mike.say "No more than you were just trying to solicit sex from her...hey, Dwayne?"
            "Dwayne grimaces, clearly aware of what could be taken as a threat beneath the outward meaning of my words."
            "But then his expression changes as he puts on his fake friendly expression again."
            dwayne.say "To hell with it - did you really think I was going to pay to fuck her?"
            dwayne.say "No way...I was just messing with you!"
            "He laughs loudly, apparently not concerned in the slightest that he's the only one doing so."
            dwayne.say "Aletta, don't just sit there with that miserable frown on your face."
            dwayne.say "Get over here and put your mouth to a better use!"
            "Aletta gives an audible sigh and comes over to where he's sitting."
            show aletta behind dwayne at mostleft5 with ease
            "As she passes by, she gives me an long and lingering look while Dwayne's not paying attention."
            "For a moment I almost regret telling Lexi not to take Dwayne's money."
            "I think that I could have kept his hands off of her and maybe even gotten to spend time with her alone."
            "Great - now I feel guilty for having it bad for Aletta and for almost pimping Lexi to the asshole in the same night!"
            "Dwayne shows his true level of pettiness by making Aletta dance for him in the most suggestive manner he can think up."
            "He makes her bend over and stretch, this way and that, chuckling at the way in which her voluptuous figure succumbs to gravity with each new pose."
            "Finally he opens the front of her blouse, almost tearing the buttons off in the effort."
            "Without even asking for permission, he manhandles Aletta's heavy breasts out of her bra and begins to massage her large nipples with a finger and thumb."
            dwayne.say "Fuck me, Aletta - your breasts are something else."
            dwayne.say "They make me want to milk you like a damn cow!"
            show aletta flirt blush
            "Aletta's cheeks flush red with embarrassment, and she moans softly at his attentions."
            dwayne.say "You sound as if you're mooing, just like a cow!"
            dwayne.say "Since I can't milk you, let's see you milk me."
            "He pushes her head down towards his groin, almost forcing her onto her knees before him."
            "Aletta obligingly opens his flies and pulls out his dick."
            "Lexi goggles at the sheer size of it, despite the sheer number she must have seen in her line of work."
            "Aletta doesn't pause or hesitate, just puts her lips around it and begins to obediently pleasure her boss and boyfriend."
            scene nightclub bj aletta lexi with fade
            "A moment later, I feel Lexi's hands on my crotch and look down to see her hastily unzipping my own flies too."
            "Soon she has my dick out and is on her knees, following Aletta's lead."
            show nightclub bj aletta alettalewd
            "I can't say if it's out of mutual arousal or simple professional pride and not wanting to be outdone on her part."
            "But why look a gift horse in the mouth - or, for that matter, a gift blowjob?"
            show nightclub bj aletta lexilewd
            "As if not to be outdone by the other woman, Lexi also hastily hikes up her top and shakes her breasts out of her bra."
            "She guides my hands to them and almost urges me to begin squeezing and pinching."
            "Suddenly, Dwayne stands up and drags his cock out of Aletta's mouth without warning."
            dwayne.say "Aletta, strip off - and then strip me too!"
            "He eyes me triumphantly, clearly thinking that he's upped the stakes so much that I won't be willing to follow his lead."
            "But while he might have got the measure of me, he's sorely underestimated the lengths to which Lexi is willing to go."
            "Without as much as a words from me, Lexi cuts short the blowjob and pulls me to my feet."
            "She strips with a speed and eagerness that puts Aletta to shame by comparison, and then does the same for me."
            "Dwayne almost sneers in response, pushing Aletta back onto the couch and giving her no warning as her hoists her legs into the air."
            "She barely has time to moan helplessly as he pushes into her exposed pussy with one forceful motion."
            "He seems to think that he's outdone Lexi again, but she responds by pushing me down onto the same couch, not far from where Aletta is being relentlessly pounded."
            "Lexi turns her back on me and proceeds to clamber onto my lap, guiding my hands under her knees as she does so."
            scene nightclub foursome aletta lexi
            show nightclub foursome aletta lexi naked
            with fade
            "I don't need any further prompting, and I waste no time in manoeuvring Lexi onto my waiting dick."
            "Lexi's curves and thick thighs mean that she's not a girl that I can toss about easily."
            "But the weight and feel of her in my arms is a real turn on, as is the feeling of lowering her onto my dick and then controlling her motions."
            "Gravity and her own weight do most of the work for me, pressing her downwards and intensifying the sensations on my cock as she rides it."
            show nightclub foursome aletta lexi lexiahegao
            "Lexi's hands desperately grasp for anything that could help to hold her up, but there's nothing within reach and she's totally at my mercy."
            show nightclub foursome aletta lexi alettaahegao
            "She's squealing now, probably only moments from cumming, but I can't help glancing over at Dwayne and Aletta out of sheer morbid curiosity."
            "Dwayne notes my attention, and promptly pulls out of Aletta, raising a muted protest."
            "He forces her onto the floor, kneeling before him."
            "Clearly he intends to make a show of his own climax."
            "The strangeness of the scene seems to have gotten to me, and I follow his example."
            scene nightclub cumshare aletta lexi
            show nightclub cumshare aletta lexi naked
            with fade
            "Releasing Lexi from my grasp, I make her copy Aletta's position, and then wait to see what happens next."














            "While Aletta kneels before him, Dwayne amuses himself by slapping her as hard as he can on the cheek with his dick."
            show nightclub cumshare aletta lexi alettalewd
            "Aletta winces with each and every relatively soft, yet humiliating blow, knowing better than to object."
            "Lexi counters this by licking and kissing the tip of my cock, a suggestive look in her eye as she does so."
            "Clearly the act of degrading Aletta in front of others does it for Dwayne."
            show nightclub cumshare aletta lexi alettaahegao cum_dwayne
            "As a few seconds later he loses himself all over her face, dragging it across her cheek and over her nose."
            "Aletta instinctively closes her eyes and screws up her features, meaning the cum is forced into the temporary wrinkles and crevices this makes."
            "By contrast, Lexi seems to know just when I'm cumming myself."
            show nightclub cumshare aletta lexi lexilewd
            "She closes her eyes and sticks out her tongue, almost like she's trying to catch the first drops of a warm, summer rain."
            show nightclub cumshare aletta lexi cum with hpunch
            "The cum spatters down upon her face, keeping up the same impression."
            with hpunch
            "At least that is until it runs too slowly down to her chin and begins to drip off in large, pearlescent globules."
    "Once everyone is fully dressed and looking at least passably decent, Dwayne spreads his arms in an expansive gesture."
    dwayne.say "So, who's coming on to the next stop on the trail?"
    dwayne.say "I know a great after-club, and then - a sex-shop where you wouldn't believe what you can pay to have done to you!"
    "Lexi and I mutter some half-hearted apologies and announce that we're planning to slink off home to bed."
    "Aletta gives me an imploring look, but all I can do is shrug my shoulders hopelessly."
    "There's really nothing I can do to stop Dwayne dragging her along in his shadow for the rest of the night."
    $ hero.replace_activity()
    $ game.pass_time(2)
    return

label lexi_pregnant_request:
    show lexi surprised
    lexi.say "Oh, [hero.name]..."
    lexi.say "I got a crazy idea - you wanna hear it?"
    "There's no build up or chance for me to tune into what's on Lexi's mind."
    "One moment she's as quiet as a mouse."
    "Well...as quiet as Lexi ever gets."
    "And the next she springs it on me."
    "Out of nowhere and without warning."
    show lexi normal
    lexi.say "I was thinking we should have a baby!"
    mike.say "Huh..."
    mike.say "What...what did you say?"
    mike.say "A baby?!?"
    "Lexi seems not to notice the shock and surprise in my voice."
    "Either that or she chooses to ignore it and keeps on talking."
    lexi.say "Yeah, a baby."
    lexi.say "You and me."
    show lexi happy
    lexi.say "Great idea, right?"
    "Put on the spot, I can't think of anything to say."
    "All I can do is blink at Lexi in stunned silence."
    "Up to now, the biggest thing on my mind was what to have for lunch!"
    show lexi surprised
    lexi.say "What's up, [hero.name]?"
    lexi.say "You look like I just blew your mind!"
    "But then I see her eyes narrow and she frowns at me."
    show lexi annoyed
    lexi.say "Wait a minute..."
    lexi.say "You think it's a good idea, right?"
    lexi.say "You DO wanna have kids with me, yeah?"
    "I try my best to shake off the funk that Lexi's put me in."
    "As I can see that this conversation is in danger of taking a bad turn."
    mike.say "I...I honestly hadn't given it that much thought, Lexi."
    mike.say "We've been having so much fun lately, you know?"
    mike.say "I really haven't been thinking that far ahead!"
    "I can see that the compliment goes someway towards mollifying Lexi."
    show lexi normal
    "She raises her eyebrows a little and gives me a smile."
    lexi.say "Well, yeah, [hero.name]."
    show lexi wink
    lexi.say "I WAS there the whole time, remember?!?"
    lexi.say "I just...got to thinking myself."
    show lexi normal
    lexi.say "Thinking about where we're going together."
    "This is a new experience for me, hearing Lexi talk about the future."
    "Until now, I thought she only ever lived in the moment."
    "Her life and the way she chooses to live it made me sure of that."
    "But apparently she has hidden depths that I totally missed."
    mike.say "And you think that place is us having kids?"
    mike.say "And having them right now?"
    show lexi happy
    "Lexi nods at this, the smile on her face becoming a little strained."
    show lexi normal
    "I can really see how much she's into the idea."
    "That and how desperate she is to hear my answer!"
    "I'd always assumed that I'd end up with a wife and kids."
    "You know, house in the suburbs, a lawn and a dog - all that stuff."
    "But it was always far in the future."
    menu:
        "Agree":
            "And it's in that moment that the thought hits me."
            "I could never have imagined meeting and dating a girl like Lexi."
            "Never mind that I would actually end up falling in love with her!"
            "But I did, and now I can't imagine not being with her."
            "So why should I start holding back now?"
            mike.say "You know what, Lexi - you're right."
            mike.say "We're great together."
            mike.say "And I know we'll be great parents too!"
            show lexi surprised blush
            "Lexi's eyes go wide and her mouth drops open."
            "I think this might be the first time I've seen her lost for words!"
            mike.say "Ah, Lexi..."
            mike.say "Are you feeling okay?"
            "I lean forwards a little, trying to get a response out of her."
            show lexi happy
            "And that's the moment Lexi chooses to let out a scream of delight."
            show lexi close with vpunch
            "She jumps up, wrapping her arms around my neck."
            show lexi normal
            lexi.say "Oh wow!"
            lexi.say "You really mean it?"
            lexi.say "You wanna have a kid with me?!?"
            mike.say "Urgh..."
            mike.say "Y...yeah, Lexi..."
            mike.say "That's what I said!"
            lexi.say "Great!"
            lexi.say "You're gonna be such a good daddy, [hero.name]."
            lexi.say "I'll be the best mommy in the world!"
            lexi.say "And we can get started right now..."
            $ lexi.love += 2
            $ lexi.flags.pregrequest = True
        "Refuse":
            "And the wife I imagined was never anything like Lexi!"
            "I mean, I love her - really I do."
            "But is she really mommy material?"
            mike.say "I...I don't think we can be hasty, Lexi."
            mike.say "Having kids is a big step."
            mike.say "I think we both need to be ready."
            show lexi sad
            lexi.say "Oh, I see how it is, [hero.name]."
            lexi.say "You say WE."
            lexi.say "But you really mean ME!"
            "I throw my hands up in a pleading gesture."
            "And Lexi plants hers on her hips."
            "She's glaring at me now, shaking her head."
            mike.say "No, Lexi!"
            mike.say "That's not it at all!"
            "Well, it's more than a small part of it."
            "But I can't admit that to Lexi."
            "I love her too much to be that brutally honest!"
            mike.say "I'm not ready either, Lexi."
            mike.say "I mean look at me."
            mike.say "I'm basically an overgrown man-child."
            mike.say "You're probably learning about kids just from being with me!"
            "Lexi tries to keep the angry expression on her face."
            "But I can already see that she's starting to crack."
            "A moment later, she can't help but start laughing."
            show lexi happy
            lexi.say "Yeah, [hero.name]..."
            lexi.say "You're right there!"
            show lexi normal
            "She nods slowly."
            "And I know then that she's come round to my way of thinking."
            lexi.say "Okay, [hero.name], you win."
            lexi.say "Maybe we'll wait a while."
            $ lexi.love -= 2
    return

label lexi_asleep:
    show sleep lexi
    "Lexi is sleeping, I should leave before I wake her up..."
    $ game.room = "kitchen"
    return

label lexi_asleep_trailer:
    show sleep lexi trailer
    "Lexi is sleeping, I should leave before I wake her up..."
    $ game.room = "trailer"
    return

label lexi_birthday_date_male:
    $ DONE["lexi_birthday_date_male"] = game.days_played
    $ game.active_date.clothes = "casual"
    "The day of Lexi's birthday has finally come around, and I'm feeling pretty nervous."
    "Because I've got the entire day planned out ahead of time, and I want it all to come off perfectly."
    if Harem.find('lexi', name='home'):
        "Plus I want it to be a surprise for Lexi too, which is why I've chosen to leave from home."
        "That way she won't have any idea where we're going until we reach our destination."
        show bg secondfloor with fade
    else:
        "Plus I want it to be a surprise for Lexi too, which is why I've chosen to pick her up from her home."
        "That way she won't have any idea where we're going until we reach our destination."
        "So when I arrive at Lexi's trailer, I'm already feeling more than a little under pressure."
        show bg trailer with fade
    play sound door_knock
    mike.say "Knock, knock, Lexi!"
    mike.say "Are you ready to go?"
    lexi.say "Oh, hey, [hero.name]..."
    lexi.say "I'll be right there..."
    lexi.say "Just putting the last touches to my birthday outfit!"
    "Birthday outfit?"
    "I like the sound of that!"
    "So I do as I'm told, patiently waiting for Lexi to show herself."
    "And when she does, I have to blink and take a second glance."
    show lexi casual normal nophone with dissolve
    lexi.say "Hey!"
    lexi.say "What are you looking at me like that for?"
    lexi.say "Don't you like my birthday outfit?!?"
    mike.say "Erm..."
    mike.say "I dunno, Lexi..."
    mike.say "It's hard to say when there's so little of it!"
    show lexi annoyed at startle
    "Lexi plants her balled fists on her hips and stamps her foot."
    "All of which makes the copious amounts of flesh on show jiggle in the most distracting way."
    lexi.say "So what are you trying to say?"
    lexi.say "Do you like it or not?!?"
    menu:
        "It's great":
            "I was kind of hoping that Lexi would dress a little more smartly today."
            "Or at the very least wear a little more than she does on any other given day."
            "But then I find myself wondering why in the hell I'm so bothered by it."
            "She looks amazing, as always."
            "So I just shrug it off."
            mike.say "Of course I like it, Lexi."
            mike.say "You just look so hot in it, that's all."
            mike.say "I was thinking how luck I am to be seen with you!"
            show lexi happy
            "My answer seems to appeal to Lexi's vanity."
            "And as a result, her demeanour changes in an instant."
            lexi.say "Aw!"
            show lexi normal
            lexi.say "Do you really like it that much?"
            lexi.say "Then that's settled - let's hit the town!"
            "Lexi wraps her arm in mine, and we're all ready to go."
            $ game.active_date.score += 15
        "It's fine":
            mike.say "It's not that I don't like it, Lexi."
            mike.say "More like today was supposed to be special, you know?"
            mike.say "And that's pretty much what you wear on a normal day."
            "Lexi's demeanour doesn't change at all in response to my explanation."
            "In fact, if anything, she doubles down on the stance she was taking before."
            lexi.say "Well if you don't like it, that's too bad."
            lexi.say "Because today's my birthday."
            lexi.say "And I'm not changing for you or anyone!"
            "I do the best I can to force a smile onto my face."
            "But the whole time I'm gritting my teeth to keep from saying more."
            "And so it kind of looks like a grimace instead."
            mike.say "Okay, Lexi, okay..."
            mike.say "Let's just agree to disagree."
            mike.say "Then we can get going."
            $ game.active_date.score -= 10
    scene bg mall1
    show lexi normal nophone at center, zoomAt (1.5, (640, 1040))
    with fade
    "We soon arrive at the mall, where we're going to be having our date."
    "And I'm all ready to begin apologising to Lexi that it's not somewhere fancier."
    "Because most of the girls I've known would think this was a lame choice."
    "But Lexi seems to be over the moon as we walk in through the automatic doors."
    lexi.say "The mall?"
    lexi.say "Pretty classy choice."
    show lexi happy
    lexi.say "I totally feel like a sophisticated lady walking in here!"
    "I can't help smiling and shaking my head as this."
    show lexi surprised
    "But Lexi seems to be puzzled by my reaction."
    lexi.say "Huh?"
    lexi.say "What's so funny?"
    lexi.say "Did I say something wrong?"
    if hero.charm >= 50:
        if hero.charm >= 75:
            mike.say "You know what, Lexi..."
            mike.say "That's one of the things I love about you."
            "Lexi frowns and wrinkles her nose in confusion."
            lexi.say "What's that supposed to mean?"
            lexi.say "That you like that I like normal stuff?"
            "I chuckle and shake my head."
            mike.say "No, Lexi..."
            mike.say "That's not it at all."
            mike.say "What I mean is that you take pleasure in even the smallest of things."
            mike.say "You live life to the fullest, make every moment enjoyable."
            show lexi happy
            "I'm not sure if Lexi totally gets what I'm trying to say to her."
            "But she seems to like the sound of it regardless."
            "She smiles and nods her head."
            lexi.say "Well some of the guys I've dated had pretty small things."
            lexi.say "And I sure had to make the most of those!"
            $ game.active_date.score += 15
        else:
            mike.say "Heh..."
            mike.say "Most people wouldn't be so excited to come to the mall, Lexi."
            mike.say "But I guess it's different for you, yeah?"
            mike.say "Because you come from a trailer park."
            show lexi annoyed
            "Lexi narrows her eyes at this."
            "And she gives me a hard stare."
            lexi.say "Whoa!"
            lexi.say "Don't hold back, [hero.name]."
            lexi.say "Tell me what you really think of me!"
            "I realise how what I said must have sounded to Lexi."
            "And I instantly start babbling as I try to make amends."
            mike.say "Uh...no...."
            mike.say "That came out wrong!"
            mike.say "That wasn't how I meant to say it at all!"
            "But for all of my efforts, Lexis quick to cut me off."
            lexi.say "Yeah, well..."
            lexi.say "That's what you said, period."
            lexi.say "So maybe think before you open your mouth next time!"
            $ game.active_date.score -= 10
    else:
        menu:
            "As in this movie, \"Wetty Prouman\"":
                mike.say "No, Lexi..."
                mike.say "It's just easy to take a place like this for granted, that's all."
                mike.say "I guess it is pretty amazing, when you think about it."
                mike.say "All of this stuff under one roof."
                show lexi happy
                "Lexi nods and offers me a smile too."
                "I can see that she's genuinely excited to be here."
                "So indulging her would be a better idea than mocking her."
                lexi.say "So..."
                lexi.say "Now that we're here..."
                lexi.say "What are we going to do?"
                lexi.say "See a movie?"
                lexi.say "Grab a pizza?"
                lexi.say "Tell me already, because I'm dying to know!"
                mike.say "Slow down a little, Lexi."
                mike.say "It's supposed to be a surprise, remember?"
                mike.say "Trust me, you're going to love it."
                $ game.active_date.score += 15
            "As in this movie, \"The Mall Pig\"":
                mike.say "Just that this is only the local mall, Lexi!"
                mike.say "I mean, we're not strolling in downtown New York or anything."
                mike.say "You must come here all the time, right?"
                show lexi angry
                "For a moment I think that Lexi's going to bite my head off."
                "Like she's going to lose it for me insinuating that she's trailer trash."
                "But then I take a closer look and I can tell that's not the case at all."
                show lexi annoyed
                "If anything, she actually looks embarrassed, even kind of edgy."
                mike.say "What's the matter, Lexi?"
                mike.say "Did I say something wrong?"
                lexi.say "I don't want to talk about it, okay?"
                lexi.say "Let's just say that some of us have a past."
                lexi.say "And some of it might involve getting caught in a place like this."
                lexi.say "Maybe getting a five-finger discount on stuff..."
                "I nod and do the best I can to change the subject."
                "Sometimes I forget that Lexi has a somewhat chequered past."
                "And the last thing that I want is to bring it up."
                $ game.active_date.score -= 10
    show lexi normal
    "I do the best I can to hide the fact that I'm steering Lexi in a certain direction."
    "But she actually helps me out on that score by being so enamoured of the whole place."
    "So I don't have any trouble making sure that we end up where I want us to be."
    mike.say "This is it, Lexi."
    mike.say "Here we are!"
    "Lexi looks up at the sign on the shop we're standing in front of."
    show lexi surprised
    "And I can already see a look of surprise on her face."
    lexi.say "Are you sure, [hero.name]?"
    lexi.say "This is a lingerie store."
    lexi.say "A really expensive one too!"
    mike.say "I know that, Lexi."
    mike.say "I want to buy you something new to wear."
    mike.say "Something a little...special."
    show lexi happy
    "Lexi gives me a knowing smile."
    with hpunch
    "And then she elbows me in the ribs."
    lexi.say "Oh, I see."
    lexi.say "You want to buy me something real sexy, right?"
    "I can't help blushing as Lexi puts me on the spot."
    "But she's one hundred percent right, so I can't deny it."
    mike.say "Y...yeah, Lexi."
    mike.say "If you're okay with that?"
    show lexi normal
    lexi.say "Sure I am, [hero.name]."
    lexi.say "It's your money - and I get to bag some seriously sexy underwear."
    lexi.say "So everyone wins, right?"
    "I nod, feeling a surge of relief."
    "And I let Lexi take hold of my hand as we walk inside."
    scene bg clothesshop with fade
    show lexi nophone at left with easeinleft
    "Much as I expected, Lexi makes for the skimpiest and most outrageous stuff she can find."
    show lexi at right4 with ease
    "I watch as she flits from one rack to the next, holding one item up against her and then the next."
    show lexi at left5 with ease
    "And with each one that she tries, I find ever more arousing images popping into my head."
    show lexi normal nophone at center, zoomAt (1.5, (640, 1040)) with fade
    "Eventually Lexi has an armful of items that she wants to try on."
    "She shoves them into my arms."
    "And then she beckons for me to follow her."
    lexi.say "Come on, [hero.name]..."
    show lexi wink
    lexi.say "Last one to the changing rooms is frigid!"
    show lexi normal nophone at center, zoomAt (1.5, (640, 1040)) with fade
    "Once we're at the cubicles, Lexi grabs the underwear from me."
    if randchoice(["knowledge", "fitness"]) == "knowledge":
        "But just before she disappears into the cubicle, Lexi pauses for a moment."
        lexi.say "Ah, shit!"
        lexi.say "This is the wrong size."
        lexi.say "Go back and get me the right one, yeah?"
        "Lexi shoves the offending item into my hands."
        hide lexi with dissolve
        "And then she slips through the curtain before I can say a word."
        "It's only as I hurry back to the shop floor that I realise something."
        "I have no idea what size Lexi's supposed to be!"
        if hero.knowledge >= 75:
            "I take a moment to pause and rack my brains on the subject."
            "I go over all the times I can recall Lexi mentioning it."
            "I also try to recall when I've caught sight of the labels on her clothes too."
            "And then it hits me - she's a size ten, I'm sure of it!"
            "I hurry to the rack where the item came from."
            "And there's a size ten, just waiting for me."
            "Back in the changing rooms I hand it over."
            "At the sound of my voice, Lexi's hand shoots out from behind the curtain."
            "And then it disappears just as quickly once she grabs the item from me."
            lexi.say "Wait a minute..."
            lexi.say "This is the right size."
            lexi.say "Somebody's been paying attention!"
            "I can't help feeling more than a little smug at the praise."
            "Because it's always good to score a few Brownie points."
            $ game.active_date.score += 15
        else:
            "I rack my brains, trying to recall if I ever heard Lexi mention her size."
            "And I do the best I can to think if I ever saw it on the label of her clothes too."
            "But no matter how hard I try, I keep on drawing a blank."
            "In the end I have no choice but to just pick a size and hope for the best."
            "So I go for the one that sounds most flattering and return to the changing rooms."
            mike.say "Here you go, Lexi."
            "At the sound of my voice, Lexi's hand shoots out from behind the curtain."
            "And then it disappears just as quickly once she grabs the item from me."
            "But it also doesn't take long for it to be tossed back in my face again."
            lexi.say "What do you think I am?"
            lexi.say "A fucking whale?!?"
            lexi.say "Get me a size ten, you stupid asshole!"
            "Feeling suitably chastened, I hurry to do as I'm told."
            $ game.active_date.score -= 10
    else:
        hide lexi with dissolve
        "Lexi disappears into the cubicle, and I can hear her moving around inside."
        "But I hardly have the chance to wonder what's actually going on in there."
        show lexi underwear nophone with dissolve
        "Because a moment later she throws back the curtain and strikes a pose."
        lexi.say "So, [hero.name]..."
        lexi.say "What do you think?"
        mike.say "Wow, Lexi..."
        mike.say "Just...wow!"
        "Well what else do you expect me to say?"
        "Lexi's standing there in incredible underwear."
        show lexi happy
        "She nods and smiles."
        lexi.say "Wait til you see the next one!"
        hide lexi with dissolve
        "With that, she closes the curtain again."
        if hero.fitness >= 75:
            show lexi underwear nophone with dissolve
            "In the time that follows, Lexi repeat the action again and again."
            "I manage to keep on reacting in the same manner."
            "I nod and smile, even offer compliments as she shows off choices."
            "The little fashion show seems to be dragging on for a long time."
            "But I know that I'm in good shape, and my stamina's up to it."
            "So I don't have any real problems in keeping myself awake."
            "This means that I can enjoy the sight of Lexi parading up and down."
            "And it's a long parade too."
            "As she seems to be intent on trying everything in the shop on for size!"
            "But why should that bother me?"
            "I'm getting to see her in outfits that'll certainly stick in my mind."
            "And I have the added bonus of knowing she'll be taking at least one of them home with her."
            "So I'll definitely get to see her in it again."
            "And if I'm lucky, very soon too!"
            $ game.active_date.score += 15
        else:
            "In the time that follows, Lexi repeat the action again and again."
            "At first I manage to keep on reacting in the same manner."
            "I nod and smile, even offer compliments as she shows off choices."
            "But after a while I can feel myself getting tired."
            "My eyes even start to close from the weariness."
            "Looking over my shoulder, I see a bench nearby."
            "It's easily close enough for me to still see Lexi from."
            "And so I hurry over and sit down on it."
            "Lexi hasn't reappeared yet."
            "So I figure that I can just close my eyes for a moment..."
            show lexi underwear surprised nophone with fade
            lexi.say "Hey!"
            lexi.say "What are you doing?"
            mike.say "Huh...wha..."
            show lexi angry
            lexi.say "You were asleep!"
            mike.say "N...no...I..."
            lexi.say "Don't try to deny it - you have drool on your chin!"
            "I look away self-consciously as I wipe the drool from my chin."
            "Maybe a coffee is what I need right now..."
            $ game.active_date.score -= 10
    hide lexi with dissolve
    "As soon as Lexi's made her decision, she goes back into the cubicle to get dressed."
    show lexi casual nophone with dissolve
    "Then she strides out from behind the curtain, handing me the stuff that she wants."
    "I follow on her heels as she makes for the cash register, trying to keep up."
    "And I've got to admit, Lexi really seems to be enjoying herself right now."
    "Almost like she's enjoying the chance to play at being a high-class lady."
    show lexi happy
    "She even stands back and smiles as the cashier rings up her purchases."
    "And it's only my eyes that bulge painfully as I see the final total pop up."
    "But I did promise her a shopping spree for her birthday."
    "So all I can do is grit my teeth and take the hit."
    scene bg mall1
    show lexi normal nophone at center, zoomAt (1.5, (640, 1040))
    with fade
    "Once we're done, we head out of the store and back into the mall."
    lexi.say "What now, [hero.name]?"
    lexi.say "You got any more pleasant surprises in store for me, huh?"
    mike.say "Well, Lexi..."
    mike.say "I was thinking that we might grab a coffee."
    mike.say "How about trying out the maid cafe?"
    "Lexi cocks her head on one side as she considers the offer."
    show lexi happy
    lexi.say "Why not..."
    lexi.say "I do love those cute uniforms they have the staff wear."
    scene bg maidcafe with fade
    show lexi nophone zorder 2 at left with easeinleft
    "With that decided, we head straight over there."
    if "bree_event_04" in DONE and not bree.hidden:
        show lexi annoyed
        "It's pretty busy once we arrive, and Lexi seems disappointed."
        "But I'm not worried, because I have an ace up my sleeve."
        "And this one just so happens to be called [bree.name]!"
        show lexi normal
        show bree b maid zorder 1 at right with easeinright
        bree.say "Hey there, [hero.name]!"
        bree.say "Lucky you made that reservation, huh?"
        show bree b wink
        "[bree.name] offers me a conspiratorial wink."
        "The truth is that I don't have a reservation at all."
        "[bree.name] agreed to shuffle me to the front of the queue when I arrived today."
        "All for the sake of earning an unspecified favour."
        "One that she can call in any time she likes in the future."
        show bree normal
        "As [bree.name] shows us to the table, Lexi can't help staring at her outfit."
        show lexi zorder 2 at center, zoomAt(1.5, (640, 1040)) with fade
        pause 1.0
        show lexi at center, zoomAt(1.5, (640, 1140)) with ease
        "And once we sit down, [bree.name] seems moved to comment on the fact."
        bree.say "Like the uniform?"
        bree.say "It is pretty sweet, isn't it?"
        show lexi happy
        lexi.say "Oh yeah, you bet!"
        lexi.say "Say..."
        lexi.say "Have you ever thought of going on the game?"
        lexi.say "You know, doing a little sex-work on the side?"
        lexi.say "Looking like that, you'd be a hit with the anime creeps!"
        show bree surprised
        "[bree.name]'s face falls as she hears what Lexi says."
        "And I can seen that she's ready to storm off."
        mike.say "Ah, [bree.name]..."
        mike.say "Just get us a couple of coffees, okay?"
        mike.say "I think I need to talk to my date in private."
        hide bree with easeoutright
        menu:
            "She's damn right!":
                mike.say "Are you serious, Lexi?"
                mike.say "You really think [bree.name] could pull that off?"
                show lexi flirt
                "I watch as a wicked smile creeps across Lexi's face."
                "She leans back in her chair and gives me a knowing wink."
                lexi.say "So you like the idea of that, huh?"
                lexi.say "Little [bree.name] there, selling her ass to the highest bidder?"
                mike.say "No...I..."
                mike.say "Well...I suppose..."
                show lexi happy
                lexi.say "It's okay, [hero.name]."
                lexi.say "Nothing to be ashamed of in that."
                lexi.say "You wouldn't believe how common that little fantasy is!"
                lexi.say "Actually...we could see if she's up for some fun, you know?"
                mike.say "You...you mean a...a threesome?"
                "Lexi shrugs, but the smile doesn't leave her face."
                lexi.say "Just a suggestion..."
                $ game.active_date.score += 15
            "She's going too far!":
                mike.say "LEXI!"
                mike.say "Where do you get off saying stuff like that?"
                show lexi annoyed
                "Lexi leans back in her chair and shakes her head."
                lexi.say "Stuff like what?!?"
                lexi.say "That was a genuine compliment."
                lexi.say "I don't go round telling every girl I see they could do that."
                lexi.say "And I should know."
                "I shake my head and roll my eyes."
                mike.say "Yeah, well..."
                mike.say "Somehow I don't think people are going to see it that way."
                mike.say "So maybe lay off suggesting that they take up sex-work, okay?"
                mike.say "Especially when it comes to my housemates."
                lexi.say "Whatever..."
                lexi.say "You people need to learn to take a compliment."
                $ game.active_date.score -= 10
    else:
        show lexi annoyed
        "It's pretty busy once we arrive, and Lexi seems disappointed."
        "But I'm not worried, because I have an ace up my sleeve."
        "And that's something called a reservation!"
        show bree a maid zorder 1 at right, blacker with easeinright
        "Waitress" "Hey there!"
        "Waitress" "Do you have a reservation, huh?"
        mike.say "Indeed I do!"
        show lexi normal
        "The waitress offers me a conspiratorial wink."
        "But as she shows us to the table, Lexi can't help staring at her outfit."
        show lexi zorder 2 at center, zoomAt(1.5, (640, 1040)) with fade
        pause 1.0
        show lexi at center, zoomAt(1.5, (640, 1140)) with ease
        "And once we sit down, the waitress seems moved to comment on the fact."
        "Waitress" "Like the uniform?"
        "Waitress" "It is pretty sweet, isn't it?"
        show lexi happy
        lexi.say "Oh yeah, you bet!"
        lexi.say "Say..."
        lexi.say "Have you ever thought of going on the game?"
        lexi.say "You know, doing a little sex-work on the side?"
        lexi.say "Looking like that, you'd be a hit with the anime creeps!"
        "The waitress's face falls as she hears what Lexi says."
        "And I can seen that she's ready to storm off."
        mike.say "Ah..."
        mike.say "Could we just get a couple of coffees, okay?"
        mike.say "I think I need to talk to my date in private."
        hide bree with easeoutright
        menu:
            "She's damn right!":
                mike.say "Are you serious, Lexi?"
                mike.say "You really think she could pull that off?"
                show lexi flirt
                "I watch as a wicked smile creeps across Lexi's face."
                "She leans back in her chair and gives me a knowing wink."
                lexi.say "So you like the idea of that, huh?"
                lexi.say "Little Miss Maid there, selling her ass to the highest bidder?"
                mike.say "No...I..."
                mike.say "Well...I suppose..."
                show lexi happy
                lexi.say "It's okay, [hero.name]."
                lexi.say "Nothing to be ashamed of in that."
                lexi.say "You wouldn't believe how common that little fantasy is!"
                lexi.say "Actually...we could see if she's up for some fun, you know?"
                mike.say "You...you mean a...a threesome?"
                "Lexi shrugs, but the smile doesn't leave her face."
                lexi.say "Just a suggestion..."
                $ game.active_date.score += 15
            "She's going too far!":
                mike.say "LEXI!"
                mike.say "Where do you get off saying stuff like that?"
                show lexi annoyed
                "Lexi leans back in her chair and shakes her head."
                lexi.say "Stuff like what?!?"
                lexi.say "That was a genuine compliment."
                lexi.say "I don't go round telling every girl I see they could do that."
                lexi.say "And I should know."
                "I shake my head and roll my eyes."
                mike.say "Yeah, well..."
                mike.say "Somehow I don't think people are going to see it that way."
                mike.say "So maybe lay off suggesting that they take up sex-work, okay?"
                mike.say "Especially when it's someone that's about to take my food order!"
                lexi.say "Whatever..."
                lexi.say "People really need to learn to take a compliment."
                $ game.active_date.score -= 10
    show lexi normal
    lexi.say "Anyway..."
    lexi.say "Last thing I heard, it was someone's birthday."
    lexi.say "So what did you get me?"
    "I look at Lexi with a blank expression on my face."
    mike.say "What do you mean, Lexi?"
    mike.say "I just bought you some nice lingerie."
    mike.say "And I'm paying for the coffee we're drinking too."
    show lexi happy
    lexi.say "I know that!"
    lexi.say "But that's the stuff you told me about already."
    show lexi normal
    lexi.say "Where's my surprise present?"
    if not hero.has_gifts:
        "I shake my head and laugh."
        mike.say "I'm serious, Lexi!"
        mike.say "That's what you're getting for your birthday."
        show lexi annoyed
        "Lexi frowns and stares down into her coffee."
        lexi.say "Huh..."
        lexi.say "I never knew you were such a cheap bastard!"
        $ game.active_date.score -= 10
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_13
        if _return != "done":
            hide lexi
            show lexi at center, zoomAt(1.5, (640, 1140))
            if _return not in ["None", "exit"]:
                "I hold up my hands in a gesture of surrender."
                mike.say "Okay, Lexi..."
                mike.say "You got me."
                "I pull out the surprise gift I've been holding back."
                "And I hand it over to Lexi."
                "She almost snatches it out of my hand."
                play sound [paper_ripping_1, paper_ripping_2]
                "And then she proceeds to tear off the wrapping paper."
                if _return:
                    show lexi surprised
                    "But as soon as she sees what's inside, Lexi lets out a gasp."
                    mike.say "What's the matter, Lexi?"
                    mike.say "Is there something wrong?"
                    lexi.say "Wrong?"
                    show lexi happy
                    lexi.say "No way - this is fucking amazing!"
                    "I smile as Lexi pulls the gift out of the box."
                    "And I feel satisfaction rising inside of me as she gushes over it too."
                    $ game.active_date.score += 15
                else:
                    show lexi annoyed
                    "But as soon as she sees what's inside, Lexi lets out a groan."
                    mike.say "What's the matter, Lexi?"
                    mike.say "Is there something wrong?"
                    lexi.say "Ah..."
                    lexi.say "It's just kinda lame, that's all!"
                    "I bite my tongue as I feel irritation building inside of me."
                    "And I tell myself that next time, I'll forget for real."
            else:
                "I shake my head and laugh."
                mike.say "I'm serious, Lexi!"
                mike.say "That's what you're getting for your birthday."
                show lexi annoyed
                "Lexi frowns and stares down into her coffee."
                lexi.say "Huh..."
                lexi.say "I never knew you were such a cheap bastard!"
                $ game.active_date.score -= 10
    show lexi with fade
    with vpunch
    "I've almost finished off my coffee when I jump in my seat."
    "And that's because I feel something touching my leg under the table!"
    mike.say "Whoa!"
    mike.say "What was that?"
    show lexi happy
    "Lexi giggles and shakes her head."
    "Then I feel the sensation a second time."
    "But now it's kind of starting to make sense."
    lexi.say "Boy, are you jumpy!"
    lexi.say "I thought all guys loved stuff like that?"
    "Lexi's eyes draw mine to the edge of the table."
    "Then she adds a subtle nod to make sure I get the message."
    "So I lift the table-cloth and have a look underneath."
    "Straight away I'm rewarded with the sight of Lexi's legs."
    "She's rubbing her feet against my legs too."
    "And they do look exceptionally good in that new underwear!"
    "But then I take a closer look."
    "Because what she has on under there looks familiar."
    "Like some of the stuff she tried on, but not the things she bought."
    mike.say "Wait a minute..."
    mike.say "Did you sneak those into the bag when I wasn't looking?"
    mike.say "I don't remember the girl ringing them up at the til."
    show lexi normal
    lexi.say "That's because she didn't."
    lexi.say "I just kept these on and walked out of the store!"
    mike.say "You mean..."
    mike.say "You stole them?"
    show lexi happy
    "Lexi nods and smiles."
    lexi.say "You're damn right I did!"
    lexi.say "Doesn't it make them feel so much sexier?"
    menu:
        "Sexier and scary":
            "For a moment I think about telling Lexi off."
            "But as I look into her eyes, I know that I won't do it."
            "Because I can already feel my cock getting harder by the moment."
            mike.say "Uh..."
            mike.say "Y...yeah, Lexi!"
            mike.say "It's really kind of sexy."
            "Lexi nods and leans in closer."
            show lexi flirt
            lexi.say "That's right, [hero.name]."
            lexi.say "The danger's like a spice."
            lexi.say "It makes everything taste that much better."
            lexi.say "That much more wicked!"
            "All I can do is swallow loudly and nod in agreement."
            $ game.active_date.score += 15
        "Sexier and dangerous":
            mike.say "No, Lexi..."
            mike.say "It's kind of a massive turn-off for me!"
            show lexi annoyed
            lexi.say "Geez..."
            lexi.say "I never knew you were so repressed."
            lexi.say "You might want to see a therapist about that."
            "I can't believe what I'm hearing right now."
            "And I have to fight to keep my voice down as I reply."
            mike.say "You think I need to get help?"
            mike.say "What about you and your kleptomania?!?"
            mike.say "Are you actually trying to get me arrested or what?"
            lexi.say "Ah, lighten up a little."
            lexi.say "This is nothing compared to some of the other shit I've done."
            lexi.say "You should be grateful I never got you into any of that."
            $ game.active_date.score -= 10
    scene bg mall1
    show lexi normal nophone at center, zoomAt (1.5, (640, 1040))
    with fade
    "Our coffee drunk and the bill settled, we head out of the cafe."
    "As Lexi and I wander aimlessly through the mall, I get a feeling."
    "It's that indefinable but very real sense that the date is coming to an end."
    "So I start to walk in the vague direction of the main exit."
    "Lexi seems to be aware of it too, as she speaks up on the way."
    lexi.say "We done here?"
    lexi.say "Are you calling it a day?"
    mike.say "Erm..."
    mike.say "That's up to you, Lexi."
    mike.say "What's your call?"
    if game.active_date.score >= 80:
        show lexi happy
        lexi.say "No way am I ready to go home."
        lexi.say "I wanna keep on having fun."
        show lexi flirt
        lexi.say "Can you handle that?"
        "I nod eagerly as Lexi says just what I wanted to hear."
        mike.say "Sure thing, Lexi."
        mike.say "Where do you want to go?"
        mike.say "What do you want to do?"
        show lexi happy
        "Lexi smiles as she takes hold of my hand."
        lexi.say "Oh, I think we can come up with something..."
        "And with that, we walk out of the mall together."
        "My brain racing to figure out what she has in mind."
        call lexi_birthday_sex_male from _call_lexi_birthday_sex_male
    else:
        show lexi yawn
        "Lexi lets out a yawn before she answers."
        "One that I can't help thinking is a little forced."
        show lexi sad
        lexi.say "Oh..."
        lexi.say "Sounds like I'm more tired than I thought!"
        lexi.say "we should probably call it a day."
        mike.say "Okay, Lexi..."
        mike.say "If that's what you want?"
        show lexi normal
        lexi.say "Yeah, it is."
        lexi.say "Catch you later, [hero.name]."
        lexi.say "And thanks for today."
        "I nod and smile."
        hide lexi with easeoutleft
        "Then I wave as Lexi walks away."
        "I really hope she meant that."
        "Because I just spent a lot of money on her ass!"
    return

label lexi_birthday_sex_male:
    scene bg street
    with fade
    "I'm still buzzing as Lexi and I walk out of the mall and onto the street."
    "Mainly from the thrill of finding out that she stole the lingerie she's wearing."
    "We just literally walked out of the place with it under her clothes!"
    "And the thought is making my heart pound in my chest right now."
    "Just thinking that any moment an alarm could go off."
    "Or else security could start chasing after us."
    "Suddenly I feel an unexpected hand grab hold of me."
    "And I'm afraid that my fears have come true."
    "That a security guard, or worse a cop, has collared me."
    "But then I realise that the hand I can feel is squeezing my groin."
    "And it seems unlikely that an arresting officer would grab me by the cock!"
    lexi.say "Ooh!"
    lexi.say "Someone's real excited!"
    "I look down at the hand grabbing me."
    show lexi happy with dissolve
    "And then I follow the arm and find it belongs to Lexi."
    lexi.say "Like I said..."
    lexi.say "It's an thrill, right?"
    show lexi normal
    lexi.say "A real adrenaline rush?"
    "We're still walking away from the mall as she's saying all of this."
    "And I'm having to fight to control myself, to keep from braking into a run."
    mike.say "Y...Yeah, Lexi..."
    mike.say "I feel kinda weird."
    mike.say "Scared and excited all at the same time."
    mike.say "How do you even start to handle it?"
    show lexi wink
    lexi.say "You gotta do something to bleed it off, [hero.name]."
    lexi.say "Something to release the pressure."
    show lexi normal
    lexi.say "Tell you what..."
    lexi.say "I'll show you what usually works for me."
    "Lexi looks left and right."
    "Then, without warning, she ducks into an alleyway."
    "I have no time to react, and so I'm pulled in with her."
    scene bg alley
    show lexi normal
    with fade
    "Lexi keeps on walking down the alley, taking us further from the street."
    "And she only stops when she seems sure that we can no longer be seen."
    "Then she lets go of my hand and turns her back on me."
    "For a moment I have no idea what's going on."
    show lexi b
    "But then she bends over, thrusting her ass backwards."
    "At the same time, Lexi lifts her skirt too."
    "And I can see the underwear she has on up close!"
    show lexi happy
    lexi.say "You see what you're feeling right now is the rush."
    lexi.say "There's adrenaline coursing through your veins."
    lexi.say "And you feel like you want to just run."
    show lexi normal
    lexi.say "Or fight."
    show lexi flirt
    lexi.say "Or...fuck!"
    "As she says all of this, Lexi reaches back."
    "And she begins to inch down her panties."
    show lexi wink
    lexi.say "But you can't walk around with it all bottled up inside."
    lexi.say "You'll go crazy at the worst, give yourself away at the least."
    lexi.say "So the best thing is to just give in and let it all out!"
    "There's no need for Lexi to spell it out any clearer for me."
    "Because as she's pulling down her panties, I'm unzipping my flies."
    "And by the time they fall around her ankles, I'm already reaching out for her."
    show lexi stand grope vaginal alley with fade
    "Lexi let's out a little yelp as I grab her from behind."
    "That lets me know that she's as desperate for this as I am."
    "But it also serves to urge me on, faster than before."
    "Lexi only just manages to throw her arms up in time."
    "Because a moment later, I almost ram her into the wall!"
    "I'm that desperate to get my hands on her that I don't wait."
    show lexi stand pull
    "I just pull her backwards as I push us both forwards."
    "The head of my cock is shoved roughly between Lexi's buttocks."
    "And for a moment I think it's going to be pushed into her ass."
    "But at the last second she twists her body."
    "Which sends it all the way between her thighs."
    "There I feel it slide along Lexi's pussy."
    show lexi stand grope
    "And as soon as I feel how hot and wet it is, I don't want anything else."
    "Lexi's hardly resisting me either, in fact she's urging me on the whole time."
    "Now she starts to push herself backwards and into me."
    "Like she's every bit as desperate for this to happen."
    "The combination of us both being crazily aroused means it happens fast."
    "One moment we're straining against the resistance down there."
    show lexi stand pull
    "And the next it disappears, letting me inside."
    "But this isn't a slow, gentle sinking in."
    "Instead I make it all the way into Lexi in a series of rough thrusts."
    "With each successive one, she gasps and moans, yet still urges me on."
    lexi.say "Urgh..."
    lexi.say "F...Fuck..."
    lexi.say "Harder...harder!"
    "I can hear Lexi's demands, but I have no idea if they affect me."
    "Because I'm already trying to do exactly what she's demanding."
    "All of that nervous energy and barely suppressed fear is flowing out of me."
    "And it's being converted into the energy I'm using to fuck Lexi right now."
    show lexi stand choke
    "I feel like I'm shaking, becoming light-headed."
    "But none of it is enough to make me even think of stopping."
    "Deep down I know there's only one thing that will."
    "By now Lexi's panting desperately."
    "Her body is pressed hard against the wall as I pound her from behind."
    "I doubt that she's really doing much of anything to hold herself up."
    "In fact her muscles seem to have turned to water in the face of my attentions."
    "That is until I feel the ones around my cock begin to twitch and clench."
    "Lexi doesn't say a word to warn me, but I know just what it means."
    "She's about to cum, and so I hold on tighter than ever."
    "Now I really am holding Lexi up, supporting her as her body quakes."
    "But she's pushing me over the edge too."
    "So I need to decide what to do before I lose it."


    "I push harder than ever."
    "Sandwiching Lexi between myself and the wall."
    with hpunch
    "Only then do I feel safe to let go."
    show lexi stand ahegao xray with hpunch
    $ lexi.love += 2
    "With one last thrust, I shoot my load into her."
    with hpunch
    "Lexi's eyes roll back into her head and she slumps forwards."
    "And I have to hold her there until she begins to show signs of recovery."








    $ lexi.sexperience += 1
    call sleep from _call_sleep_88
    $ game.room = "bedroom1"
    return


label lexi_morningwood:
    "My alarm goes off, dragging me out of the delightful world of sleep and into the less pleasing one of the waking world."
    "But I need to get my ass out of bed and get on with the business of the new day, so I obey and leap out of bed."
    "Well, it'd be closer to the truth to say that I drag myself out of bed, moaning and yawning the whole time."
    "Then I stagger out of my bedroom and meander vaguely towards the bathroom to try and make myself presentable."
    play sound sasha_breathing loop volume 6
    scene bg livingroom with fade
    "It's as I pass the living room that I hear the unmistakable sound of someone cutting wood with a chainsaw."
    "A quick glance around the door shows me that I was mistaken - it's actually the sound of Lexi snoring!"
    show sleep lexi at center, zoomAt(1.0, (640, 720)) with fade
    "She's laid face down on the couch, looking like she collapses there the night before."
    "Her face is squashed up against a pillow and the covers are falling off her, slipping onto the floor."
    "But even heaped up and snoring like a particularly nasal pig, Lexi still catches my eye."
    "And that's because she's in the habit of sleeping in nothing but her panties and a skimpy top!"
    "As I'm watching, fate would have it the covers finally choose this moment to slide fully off."
    show sleep lexi at center, traveling(1.5, 0.3, (700, 1070))
    pause 0.1
    show sleep lexi at center, traveling(1.0, 0.3, (640, 720))
    "Which means I'm presented with a glorious view of Lexi's buttocks."
    "They seem to be moving up and down as she snores and shifts in her sleep."
    "The sight is almost hypnotic, making me forget all about the bathroom."
    "Instead I step into the doorway, straining to see more."
    "You might have that mental image of a beautiful girl sleeping."
    "That she's delicate and graceful, reclining like a woman in a classical painting."
    "Yeah, well you can forget any of that when it comes to Lexi!"
    "She's sprawled on her belly, face squished into the pillow."
    "In fact, I'm pretty sure she's been drooling into it as well!"
    "Her hair's a tangled mess and one leg's dangling off the sofa."
    "But fuck me - does she ever look sexy right now!"
    "Lexi's like the definition of a hot mess!"
    "I can already feel myself getting hard as I watch her."
    "And I know that I should really sneak off and go to the bathroom."
    "I mean, it's probably wrong to be watching her like this."
    "Plus I can always make sure the bathroom door is locked."
    "And then I could use the mental image of Lexi to relieve some pressure."
    "Or I could take a gamble and try to get a little closer..."
    show sleep lexi at center, traveling(1.2, 1.0, (700, 800))
    "I'm almost halfway across the room before I realise it."
    "Which I guess means that I made up my mind on an unconscious level."
    "And probably that I'm some kind of serious pervert too!"
    "But what the hell - I'm at peace with what I am."
    "Plus the sight of Lexi's ass up close eclipses any other concern."
    "The knickers that she's wearing are really little more than a thong."
    "Which means that everything is on show and within reach."
    show sleep lexi at center, traveling(1.35, 1.0, (850, 950))
    "And now that I'm closer, I get a better look at Lexi's top half too."
    "I can see that her breasts are barely being kept in by her top."
    "They look like the slightest movement could see them popping out!"
    "I wonder if I could..."
    show sleep lexi at center, traveling(1.5, 1.0, (700, 1070))
    "With the same unconscious actions that lead me to the sofa a moment before, I bend over."
    "And then I reach out to take hold of Lexi's underwear."
    "I don't try to pull them down, just pull the crotch aside."
    "Lexi doesn't seem to stir as I do so."
    "Instead she keeps right on snoring and shifting."
    "I can feel my heart pounding in my chest as I lean in closer still."
    "And I start to pull down my own shorts with my free hand."
    "Should I really be doing something like this?"
    "I know that, were the rolls reversed, Lexi wouldn't think twice."
    "So I can only hope that she sees herself as fair game too!"
    play sound sasha_panting loop volume 6
    with hpunch
    "Lexi grumbles and stirs as I ease myself down behind her."
    "This makes me freeze for a moment, holding my breath."
    "But then she makes a sound like a whoopee cushion with a slow puncture."
    "And she wriggles her ass at the same time."
    "The strange combination of slobbiness and sexiness makes no sense to me."
    "All I know is that I need to get my hands on Lexi - and soon!"
    "Almost afraid to breathe, I inch my cock towards its target."
    scene bg black
    show lexi doggy livingroom pleasure at center, zoomAt(1.5, (700, 1070))
    with fade
    "Luckily for me, Lexi's laid in a position that naturally parts her buttocks."
    "So all I have to do is pull one of them aside a little more."
    "And then I can slide the head of my cock against her pussy."
    "I can feel the soft folds of her lips now."
    "And I'm pretty sure that Lexi can feel me too."
    "Because she squirms and wriggles as I tease her with it."
    "I can hear her making little moaning sounds in her sleep."
    "But she still doesn't seem to be waking up."
    "Well, at least one part of her is!"
    "Lexi's pussy is getting wetter by the second."
    "It's responding to my attentions in the best way possible."
    "I can even smell the scent of it, which turns me on all the more!"
    "It's now or never - do this thing or run away before I get caught."
    play sexsfx1 slide_in
    show lexi doggy vaginal
    "So without giving myself time to think, I push downwards..."
    stop sound
    lexi.say "Oh..."
    show lexi doggy ahegao
    lexi.say "Oh...oh fuck!"
    lexi.say "My...my pussy!"
    play sound sasha_panting loop volume 6
    "Lexi sounds groggy and disoriented as I sink into her."
    "The feeling is amazing, like I'm bringing her to life."
    "I just hope it's as good for her as it is for me!"
    stop sound
    lexi.say "Wha...what the hell?!?"
    lexi.say "I'm getting fucked!"
    play sound sasha_panting loop volume 6
    show lexi doggy normal
    "She looks over her shoulder, eyes wide with surprise."
    "Lexi holds my eye for a moment, her brain beginning to wake up."
    "Then she narrows her eyes and her mouth curls into a sardonic smile."
    stop sound
    lexi.say "I might have known!"
    lexi.say "Sneaking around, taking advantage of me!"
    play sound sasha_panting loop volume 6
    show lexi doggy pleasure
    "Lexi closes her eyes and shivers."
    "Like she's suddenly aware of just how good this feels."
    stop sound
    show lexi doggy normal
    lexi.say "Well?"
    lexi.say "What are you waiting for?"
    lexi.say "You'd better be able to finish what you started!"
    show lexi doggy pleasure
    "I nod with enthusiasm."
    "But it's not like I need the encouragement."
    "I'm already as deep as I can get into Lexi."
    "And she looks so hot when she's a sleepy bed-head."
    scene bg black
    show lexi doggy livingroom vaginal pleasure
    with fade
    "I pretty much leap into action a moment later."
    "Lexi gasps, evidently not ready for just how awake I actually am."
    play sound sasha_moans_hard_medium loop volume 6
    play sexsfx1 fuck_calm loop
    show lexi doggy at stepback(speed=0.1, h=-10, v=0)
    pause 0.1
    show lexi doggy at stepback(speed=0.1, h=-10, v=0)
    "Then she literally cries out as I begin to pound her without mercy."
    "I should be worried about the sound waking somebody else up."
    "But right now all I can think about is fucking Lexi."
    stop sound
    lexi.say "Grrr..."
    show lexi doggy normal
    lexi.say "Oh man..."
    lexi.say "I didn't know how much I needed this..."
    lexi.say "Not until your cock was inside of me!"
    play sound sasha_moans_hard_medium loop volume 6
    "Lexi pulls up her top, spilling her breasts as she does so."
    "Then she massages them, squeezing without mercy."
    "The sight would have been enough to get me off on its own."
    "And I have to tear my eyes away to keep from losing it right there and then."
    show lexi doggy at stepback(speed=0.1, h=-10, v=0)
    pause 0.1
    show lexi doggy at stepback(speed=0.1, h=-10, v=0)
    "Instead I focus on thrusting into Lexi like my life depends on it."
    "Lexi's almost folded in half by now, pushed down into the sofa."
    "But she's nodding the whole time, letting me know that she's loving it."
    show lexi doggy at stepback(speed=0.1, h=-10, v=0)
    pause 0.1
    show lexi doggy at stepback(speed=0.1, h=-10, v=0)
    "She starts to gasp and then let out little cries."
    "And she can hardly get her words out."
    stop sound
    show lexi doggy pleasure
    lexi.say "Oh..."
    lexi.say "Oh yeah..."
    lexi.say "Gonna...gonna cum!"
    play sound sasha_moans_hard_medium loop volume 6
    "It's not like she needed to say it out loud."
    show lexi doggy at stepback(speed=0.1, h=-10, v=0)
    pause 0.1
    show lexi doggy at stepback(speed=0.1, h=-10, v=0)
    "The way she's wriggling on my cock's a dead giveaway!"
    "The sensation and the sight, as well as the admission are too much for me."
    play sexsfx1 cum_inside volume 6
    show lexi doggy ahegao creampie with hpunch
    "With one last thrust, I lose it as deep inside of Lexi as I can get."
    with hpunch
    "This only serves to add to her helplessness."
    with hpunch
    play sound "sd/moans/sasha/sasha_moans_light_orgasm.ogg"
    queue sound "sd/moans/sasha/sasha_panting.ogg" loop
    "She pushes her head into the pillow, clawing at the sofa with her hands."
    stop sound
    play sexsfx1 slide_out
    show lexi doggy normal -vaginal vaginaldrip
    lexi.say "Urgh..."
    lexi.say "Shit, [hero.name]..."
    lexi.say "Warn me the next time you're gonna do that!"
    "Lexi pauses for a moment."
    "Then she shakes her head."
    lexi.say "Nah..."
    lexi.say "On second thoughts, keep me in the dark!"
    stop sound
    stop sexsfx1
    $ lexi.sexperience += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
