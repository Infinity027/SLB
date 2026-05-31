init python:
    Event(**{
    "name": "bree_about_kiss",
    "label": "bree_about_kiss",
    "max_girls": 1,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("bathroom", "bedroom2")),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            MinFlag("kiss", 1),
            MaxStat("love", 79),
            ),
        ],
    "music": "music/roa_music/juice.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "bree_talk_breakup",
    "label": "bree_talk_breakup_male",
    "max_girls": 1,
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 80),
            ),
        ],
    "music": "music/roa_music/juice.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "bree_kiss_me",
    "label": "bree_kiss_me",
    "max_girls": 1,
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(bree,
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
    "name": "bree_event_01",
    "label": "bree_event_01",
    "duration": 1,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 20),
            ),
        ],
    "priority": 500,
    "do_once": True,
    "music": "music/roa_music/juice.ogg",
    })

    Event(**{
    "name": "bree_event_02",
    "label": "bree_event_02",
    "duration": 1,
    "conditions": [
        IsDone("bree_event_01"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsRoom("arcade"),
            ),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 40),
            ),
        ],
    "priority": 500,
    "do_once": True,
    "music": "music/roa_music/juice.ogg",
    })

    Event(**{
    "name": "bree_event_03",
    "label": "bree_event_03",
    "duration": 1,
    "conditions": [
        IsDone("bree_event_02"),
        IsHour(10, 19),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        InInventory("zbox_360"),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 60),
            ),
        ],
    "priority": 500,
    "do_once": True,
    "music": "music/roa_music/juice.ogg",
    })

    Event(**{
    "name": "bree_pool_throat",
    "label": "bree_pool_throat",
    "conditions": [
        IsHour(9, 19),
        HeroTarget(
            IsGender("male"),
            IsActivity("swim_pool_home")),
        PersonTarget(bree,
            Not(IsHidden()),
            HasRoomTag("home"),
            Not(IsActivity("sleep")),
            MinStat("sub", 50),
            MinStat("sexperience", 1),
            ),
        ],
    "priority": 500,
    "music": "music/roa_music/juice.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "bree_event_bowsette",
    "label": "bree_event_bowsette",
    "duration": 1,
    "conditions": [
        IsDayOfWeek("12345"),
        IsHour(18, 20),
        MinDaysPlayed(21),
        HeroTarget(
            IsGender("male"),
            IsRoom("secondfloor", "bedroom2"),
            HasStamina()
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            IsRoom("bedroom2"),
            IsFlag("pregnant", False),
            MinStat("love", 100),
            ),
        ],
    "priority": 500,
    "music": "music/roa_music/juice.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "bree_talk_preg",
    "max_girls": 1,
    "label": "bree_preg_talk",
    "do_once": False,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(bree,
            IsActive(),
            IsFlag("pregtest", 1),
            ),
        ],
    "music": "music/roa_music/juice.ogg",
    })

    Event(**{
    "name": "bree_preg_test",
    "max_girls": 0,
    "label": "bree_preg_test",
    "do_once": False,
    "conditions": [
        IsHour(6, 11),
        HeroTarget(IsRoom("bathroom")),
        PersonTarget(bree,
            Not(IsHidden()),
            IsFlag("pregtest", False),
            MinCounter("pregnant", 6),
            ),
        ],
    "music": "music/roa_music/juice.ogg",
    })

    Event(**{
    "name": "bree_gone",
    "label": "bree_gone",
    "conditions": [
        PersonTarget(bree,
            IsFlag("gone"),
            IsFlag("goneDelay", False),
            ),
        ],
    "do_once": False,
    "quit": False,
    })

    InteractEvent(**{
    "name": "bree_anal_confession",
    "priority": 500,
    "label": "bree_anal_confession",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(bree,
            IsActive(),
            MinFlag("anal", 1),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/juice.ogg",
    })

    Event(**{
    "name": "bree_shower_BJ",
    "label": "bree_shower_BJ",
    "duration": 1,
    "conditions": [
        HeroTarget(IsGender("male")),
        IsHour(20, 0),
        HeroTarget(IsActivity("take_a_shower")),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 150),
            MinStat("sub", 50),
            MinStat("sexperience", 1),
            ),
        ],
    "once_week": True,
    "music": "music/roa_music/juice.ogg",
    "do_once": False,
    })

    Event(**{
    "name": "bree_go_to_the_beach",
    "label": "bree_go_to_the_beach",
    "conditions": [
        MinDaysPlayed(3),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        Not(HasVehicle()),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "music": "music/roa_music/juice.ogg",
    "do_once": True,
    "quit": False,
    })

    InteractEvent(**{
    "name": "bree_call_daddy",
    "label": "bree_call_daddy",
    "conditions": [
        Not(IsDone("bree_call_daddy_slutty")),
        HeroTarget(
            IsGender("male"),
            IsRoom("bedroom2")),
        PersonTarget(bree,
            IsActive(),
            IsFlag("collared"),
            MinStat("love", 150),
            ),
        ],
    "music": "music/roa_music/juice.ogg",
    "do_once": True,
    "quit": False,
    })

    InteractEvent(**{
    "name": "bree_call_slutty",
    "label": "bree_call_daddy_slutty",
    "conditions": [
        Not(IsDone("bree_call_daddy")),
        HeroTarget(
            IsGender("male"),
            IsRoom("bedroom2")),
        PersonTarget(bree,
            IsActive(),
            Not(IsFlag("collared")),
            MinStat("love", 150),
            ),
        ],
    "music": "music/roa_music/juice.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "bree_asleep",
    "label": "bree_asleep",
    "priority": 1500,
    "conditions": [
        HeroTarget(IsRoom("bedroom2")),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            IsActivity("sleep"),
            ),
        ],
    "do_once": False,
    "once_hour": False,
    })

    InteractEvent(**{
    "name": "bree_murder_talk_sasha",
    "label": "bree_murder_talk_sasha",
    "do_once": True,
    "conditions": [
        PersonTarget(bree,
            IsActive(),
            ),
        PersonTarget("kylie",
            IsFlag("killed", "sasha")
            ),
        ],
    })

    Event(**{
    "name": "bree_pregnant_request",
    "label": "bree_pregnant_request",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            IsFlag("status", "girlfriend"),
            MaxCounter("pregnant", 8),
            ),
        'game.days_played - bree.flags.girlfriend_day >= 7',
        ],
    "music": "music/roa_music/juice.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "bree_sasha_collar_reaction",
    "label": "bree_sasha_collar_reaction",
    "priority": 500,
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("collared", False),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("collared"),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "bree_event_office_01",
    "label": "bree_event_office_01",
    "duration": 1,
    "conditions": [
        IsDone("aletta_event_05"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work_personal", "workhard_personal")
            ),
        GameTarget(
            IsFlag("dwaynedead", False),
            IsFlag("dwaynefired", False),
            IsFlag("underinvestigation", False),
            IsFlag("suspended", False),
            IsFlag("fired", False),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            MinStat("love", 120),
            ),
        ],
    "priority": 500,
    "do_once": True,
    "music": "music/roa_music/juice.ogg",
    })

    Event(**{
    "name": "bree_event_office_02",
    "label": "bree_event_office_02",
    "duration": 1,
    "conditions": [
        IsDone("bree_event_office_01"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work_personal", "workhard_personal"),
            ),
        GameTarget(
            IsFlag("dwaynedead", False),
            IsFlag("dwaynefired", False),
            IsFlag("underinvestigation", False),
            IsFlag("suspended", False),
            IsFlag("fired", False),
            IsFlag("breeoffice_delay", False),
            ),
        ],
    "priority": 500,
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "bree_event_office_03",
    "display_name": "About Dwayne",
    "label": "bree_event_office_03",
    "icon": "button_dwayne",
    "conditions": [
        IsDone("bree_event_office_02"),
        HeroTarget(IsGender("male")),
        PersonTarget(bree,
            IsActive(),
            ),
        GameTarget(
            IsFlag("dwaynedead", False),
            IsFlag("dwaynefired", False),
            IsFlag("underinvestigation", False),
            IsFlag("suspended", False),
            IsFlag("fired", False),
            IsFlag("officebree", True),
            ),
        ],
    "do_once": True,
    })


    WakeUpEvent(**{
    "name": "bree_morningwood",
    "priority": 500,
    "label": "bree_morningwood",
    "duration": 1,
    "conditions": [
        IsHour(5, 9),
        HeroTarget(IsGender("male"),
            Not(InFlag("slept_with", "bree")),
            Not(IsFlag("morningwood")),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            IsActivity("sleep"),
            MinStat("love", 160),
            MinStat("sexperience", 2),
            ),
        RoomTarget('bedroom2',
            NPCNumber(1)
            ),
        ],
    "chances": 20,
    "do_once": False,
    "once_month": True,
    })

    Event(**{
    "name": "bree_sasha_pregnant",
    "label": "bree_sasha_pregnant",
    "duration": 1,
    "priority": 1000,
    "conditions": [
        IsActiveHarem('home'),
        Not(TogetherInHarem('home', 'bree', 'sasha')),
        HeroTarget(IsGender("male")),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            Not(IsFlag("collared")),
            MaxCounter("pregnant", 3),
            MinStat("love", 100),
            MinStat("sexperience", 1),
            ),
        PersonTarget(sasha,
            Not(IsPresent()),
            Not(IsHidden()),
            MinCounter("pregnant", 9),
            ),
        ],
    "do_once": True,
    })

    InteractEvent(**{
    "name": "bree_rape_talk",
    "label": "bree_rape_talk",
    "do_once": True,
    "conditions": [
        PersonTarget(bree,
            IsActive(),
            ),
        PersonTarget("kylie",
            IsFlag("killed", False),
            IsFlag("rape"),
            ),
        ],
    })

    Event(**{
    "name": "bree_fight_dad",
    "label": "bree_fight_dad",
    "duration": 4,
    "priority": 1500,
    "conditions": [
        HeroTarget(
            Or(
                IsRoom("alley"),
                HasRoomTag("street"),
                ),
            ),
        PersonTarget(bree,
            IsGone()
            ),
        PersonTarget("kylie",
            Not(IsFlag("killed", "bree"))
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "bree_fight_mourning_dad",
    "label": "bree_fight_mourning_dad",
    "duration": 1,
    "priority": 1500,
    "conditions": [
        HeroTarget(
            Or(
                IsRoom("alley"),
                HasRoomTag("street"),
                ),
            ),
        PersonTarget(bree,
            IsGone()
            ),
        PersonTarget("kylie",
            IsFlag("killed", "bree")
            ),
        ],
    "do_once": True,
    })

    AfterDateEvent(**{
    "name": "bree_stripclub_intro",
    "label": "bree_stripclub_intro",
    "priority": 1000,
    "duration": 1,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            ),
        MinDateScore(60),
        PersonTarget(bree,
            OnDate(),
            MinStat("love", 190),
            MinStat("sub", 40),
            ),
        ],
    "music": "music/roa_music/juice.ogg",
    "clothes": "sexydate",
    "do_once": True,
    })

label bree_sasha_collar_reaction:
    show bree
    "You could have been forgiven for thinking that things would be pretty different between [bree.name], Sasha and myself."
    "You know, now that we're not only living under the same roof, but also involved in a relationship with one another."
    "But I suppose there are some things about human beings that you just can't change."
    "Even when you've found the courage to break the taboos of conventional society in the way that we have."
    show sasha at center, zoomAt(1.25, (340, 880))
    show bree annoyed at center, zoomAt(1.0, (840, 720))
    with easeinleft
    "Like right now, when I can see the way that [bree.name]'s looking at Sasha, eyes narrowed and lips starting to pout."
    "I can't help sighing in weary resignation at the sight and shaking my head."
    show bree at center, traveling(1.25, 1.0, (640, 880))
    hide sasha with easeoutleft
    "It's bad enough when you're in a relationship where your other half's jealous of another girl out side of it."
    "So just imagine the potential for conflict and strife when she's jealous of another girl inside of it!"
    mike.say "Okay, [bree.name] - what is it, huh?"
    mike.say "What's the matter?"
    show bree surprised at vshake
    "She almost jumps at the sound of my voice, the question taking her by surprise."
    show bree b annoyed
    "[bree.name] glances away for a moment, as if she's trying to make it look like there's nothing going on."
    "But she makes the mistake of unconsciously fingering the bottom of her neck as she does so."
    "All it takes is one last look over at Sasha to confirm what this is really all about."
    mike.say "[bree.name], is this about the collar that I gave to Sasha?"
    show bree stuned
    "She meets my eye for the first time, sulky and sullen as she's forced to admit the truth."
    show bree sad
    bree.say "Well, yeah...I guess it is."
    show bree a gloomy
    "[bree.name] crosses her arms over her chest and takes a deep breath before telling me anything more."
    if bree.sub < 90:
        show bree angry at center, traveling(1.5, 0.3, (640, 1040))
        "I see an unconscious shiver run down [bree.name]'s spine."
        "And she shakes, as though trying to physically throw off a feeling that's making her feel uncomfortable."
        show bree vangry
        bree.say "Eww...I mean seriously, [hero.name]?"
        bree.say "I can't believe that you'd even think of giving something like that to a girl."
        show bree annoyed
        "She steals another sideways glances at Sasha, her voice dropping low and becoming conspiratorial."
        show bree sad
        bree.say "Or that she'd actually wear it."
        $ bree.love -= 10
        bree.say "If you ask me, it's pretty disgusting!"
        show bree angry
        "It's all that I can do to keep from pointing out that no one has asked her."
        "So with a serious amount of effort to keep a straight face, I try to play the diplomat."
        mike.say "Geez...I'm sorry, [bree.name]."
        mike.say "I honestly had no idea you felt so strongly about that kind of thing."
        mike.say "Sasha, now she's into it big time - loves it, in fact."
        "I know, I know - I'm throwing Sasha under the bus here."
        "But I need to have some way to keep [bree.name] sweet and not come off looking like some kind of perverted creep."
        show bree vangry
        bree.say "Well...I guess if she likes it..."
        bree.say "I just kind of thought it was a bit sleazy, that's all."
        show bree annoyed
        mike.say "Maybe I could talk to Sasha, tell her how you feel?"
        show bree stuned at center, traveling(1.5, 0.3, (640, 1040))
        "At this, [bree.name] starts towards me, putting a hand on my arm to keep me from going over to Sasha."
        show bree surprised
        bree.say "No...no, don't tell her it was me!"
        show bree sad
        bree.say "I mean, maybe mention something about it - but don't tell her I said all those things."
        show bree gloomy
        "I nod, trying to look surprised at her reticence, rather than relieved to have put her off complaining."
    else:
        show bree hesitating blush at center, traveling(1.5, 0.3, (640, 1040))
        "[bree.name] bites her lip before going on, and I can see a tension building in her as she does so."
        "It's clear that she desperately wants to say something about the collar Sasha's wearing."
        "But just what that might be, I can't hope to guess."
        $ bree.sub += 10
        show bree sad
        bree.say "Why...why does Sasha get a collar and I don't?"
        show bree gloomy
        "[bree.name]'s voice had practically become a petulant whine by the time she manages to get the words out."
        "She looks up at me with those huge eyes, almost like a kicked puppy."
        show bree sad
        bree.say "Did I say something wrong?"
        bree.say "Did I do something to make you cross with me, huh?"
        show bree gloomy
        "She pauses, and in that moment, and I actually think that she might shed a tear."
        show bree sad
        bree.say "Is it...is it because you love Sasha more than you love me?"
        show bree gloomy
        "Her words are completely unexpected, but they feel like a punch in the gut all the same."
        mike.say "[bree.name]...no!"
        mike.say "Of course not!"
        "I shake my head, realising the mistake that I've made."
        mike.say "No, [bree.name] - I love you just as much as I love Sasha, honestly I do."
        mike.say "I was just an idiot and gave her the collar that I got her before I gave you yours!"
        show bree happy
        "The smile that suddenly spreads across [bree.name]'s face tells me that I managed to say just the right thing."
        show bree flirt
        "She claps her hands together and looks at me expectantly."
        "And it's then that I realise she's expecting me to produce the aforementioned collar, right here and now."
        "Which would be something of an ask, as I obviously haven't got one to give to her."
        "I made all of that up on the spot, hoping to buy myself some time!"
        mike.say "I don't have your collar on me right now, [bree.name]."
        show bree gloomy
        "I see her quick smile turn just as swiftly into a pouty frown at this."
        mike.say "And that's because I...left it at...work."
        show bree normal
        mike.say "That's right - I left it at work!"
        mike.say "But don't worry, because I'll rush over there and grab it, ASAP!"
        show bree happy
        "By the time I hurry off, my mind racing as to just where I can buy a collar for her, [bree.name]'s smiling again."
        "It's a chore to be sure, but it's got to be worth the effort if it keeps her happy."
        "And if [bree.name]'s happy as well as Sasha, then I'm happy too."
    return

label bree_sasha_pregnant:
    "You know, I never thought that keeping two girls on the go at the same time would turn out to be this hard."
    "But then I suppose that I never really put much thought into the idea before now either."
    "Sure, I thought about all the obvious stuff, like how exciting it would be to sample two different flavours at once."
    "Maybe I even spared a couple of moments to wonder how you'd manage sneaking around so as not to get caught."
    "Back then, when it was all theoretical, I might even have thought that the thrill of being caught out would be fun."
    "But now that I'm actually living out what for most guys would be an impossible fantasy, it feels very different."
    "You see, the longer that you manage to keep it up, the harder it gets."
    "As the relationships with both girls get more complex, so do the lies that you have to tell to cover your tracks."
    "Sooner or later, it starts to get really hard to remember which of them you told what little bit of bullshit to steer them away from the other."
    "And getting one of them pregnant is probably the ultimate no-no."
    show sasha at right with easeinright
    "So now that Sasha's well and truly beginning to show, things are getting seriously hard for me."
    show sasha at center with ease
    "Every day her belly seems to be swelling, becoming visibly larger."
    show sasha at left with ease
    "A part of me is super excited at the prospect of being a dad."
    "But it gets pushed out of the way every time it pops up by the fear of being caught out."
    show bree annoyed at right with easeinright
    "The worst thing is that I can see [bree.name] beginning to notice that something's up."
    hide sasha with easeoutleft
    "Obviously she can see with her own eyes that Sasha's pregnant, that's not the real issue."
    show bree at center with ease
    "The fact that I've already told Sasha she should probably keep the finer details from [bree.name] is though."
    show bree at left with ease
    "I've pretty much convinced Sasha that we need to choose the right moment to tell our housemate about our relationship and the baby."
    hide bree with easeoutleft
    "Selling her on the grounds that it'll mean we probably have to make changes around the house."
    "That and how much it might freak [bree.name] out to know that we're starting a family right under her nose."
    "But she's getting ever more suspicious, and keeps on asking questions behind Sasha's back."
    "I guess she must be doing the same to Sasha behind my back too."
    "I just don't know how much longer we can keep on telling lies that back each other up."
    "Especially when I'm already lying about those lies to Sasha as well!"
    show bree b talkative at center, zoomAt(1.5, (640, 1040)) with easeinleft
    bree.say "[hero.name], have you got a minute spare?"
    bree.say "I want to talk to you - about Sasha."
    show bree normal
    "Here we go again!"
    "I take a deep breath and try to remember the last round of lies that I told [bree.name] on the same subject."
    mike.say "Sure, [bree.name] - what's on your mind?"
    show bree a annoyed
    "She sighs and crossed her arms over her chest, a worried expression on her face."
    show bree sad
    bree.say "Look, I know you said that we should just leave this alone."
    bree.say "But it's been eating away at me the whole time I'm in the same room as her."
    bree.say "I really think that we should sit Sasha down and make her tell us what's going on with her right now."
    show bree stuned
    "She seems to notice the pained look on my face."
    show bree normal
    "But luckily, she assumes that it's because she's dredging up an old conversation that we'd said was done with already."
    show bree talkative
    bree.say "I know, I know...we said that we'd let her tell us in her own time."
    bree.say "At least we should make her tell her who it was that landed her in this mess."
    bree.say "Whether the deadbeat's going to do the right thing or not - we'd know what she needs from us as friends."
    mike.say "I think she's been pretty good at letting us know what she need, [bree.name]."
    mike.say "And that's space."
    show bree annoyed
    "[bree.name] frowns at me, shaking her head in frustration."
    show bree vangry
    bree.say "I don't get it, [hero.name]."
    bree.say "I mean, I understand what you're saying."
    bree.say "But sometimes...sometimes I almost feel like you're standing up for this guy, whoever he is."
    show bree gloomy
    mike.say "Oh come on, [bree.name] - that's crazy!"
    mike.say "I just want to give Sasha space, that's all."
    mike.say "She's already living under the same roof as us while we're seeing each other."
    mike.say "And now she's pregnant too."
    show bree angry
    "[bree.name] squints at me, wrinkling her brow as she does so."
    "Suddenly I feel as though she's putting far too much thought into this for my liking."
    show bree talkative
    bree.say "It's weird, you know?"
    bree.say "Almost like you're more into keeping the peace around here than helping Sasha out..."
    bree.say "If she has to make a change for the sake of her baby, how does that affect us, even in the slightest?"
    show bree angry
    mike.say "Ah...it...it doesn't."
    show bree talkative
    bree.say "Then what's so bad about having it out with her?"
    bree.say "Unless..."
    show bree stuned
    "The look of sudden realisation spreading across her face is enough to make me feel a churning in the pit of my stomach."
    "But it's too swift for me to be able to get my lies straight and jump in before she beats me to the punch."
    show bree surprised
    bree.say "Oh god...oh god!"
    bree.say "All this time, I thought that you were being evasive to protect Sasha."
    bree.say "But you weren't - you were lying to me to protect yourself!"
    show bree stuned
    mike.say "[bree.name], please..."
    mike.say "I can explain..."
    "[bree.name] holds up a hand to fend off my desperate words."
    show bree cry
    "I can already see the tears welling in the corner of her eyes."
    bree.say "Don't...just don't..."
    bree.say "I'm going to my room now, and I'm going to start packing."
    show bree gloomy at center, zoomAt(1.5, (840, 1040)) with ease
    "I try to make a move towards her, try to say something."
    "But she cuts me off with another wave of her hand."
    show bree cry
    bree.say "Don't try to stop me."
    bree.say "I won't say anything to Sasha, I promise."
    bree.say "You two are going to need each other more than you can ever know."
    bree.say "And just for the record, [hero.name] - I'm not doing this for you, or her."
    bree.say "I'm doing it for the babies, because they're the only innocent in this whole thing - and they don't deserve to be hurt by it."
    bree.say "Especially after you already hurt everyone else that's involved."
    hide bree with easeoutright
    $ bree.set_gone_forever()
    $ Room.find("bedroom2").hide()
    "And with that, she storms off, leaving me alone with only my guilt for company."
    "I guess that I should be thankful for what she's doing, even though I don't feel like I deserve it."
    "Maybe the fantasy of having two girls on the go is a fantasy for a reason?"
    return

label bree_murder_talk_sasha:
    show bree gloomy at center, zoomAt(1.25, (640, 880))
    "There's been a cloud hanging over the house since the incident that happened with Kylie."
    "And it's not like that's a hard thing to understand, is it?"
    "I mean, look at what I'm doing right now - calling it 'the incident'!"
    "I can't even come out and say it."
    "Say that Kylie broke in here and actually killed Sasha in front of us..."
    "But we can't go on like this forever."
    show bree gloomy at center, zoomAt(1.5, (640, 1100)) with fade
    "Which is why I finally make [bree.name] sit down with me and talk about it."
    mike.say "I...I'm so sorry, [bree.name]."
    show bree stuned
    "[bree.name] looks at me for a moment like she doesn't know what I mean by that."
    "Her eyes are more than a little bloodshot, pink around the edges too."
    "I guess that she's been crying and finding it hard to sleep."
    "Both of which I can empathise with."
    show bree surprised
    bree.say "Wh...what?"
    bree.say "Why would you be sorry, [hero.name]?"
    show bree stuned
    "I take a deep breath, steeling myself for what lies ahead."
    mike.say "Because it was me that got involved with Kylie."
    mike.say "I was the one that brought her here in the first place."
    mike.say "I feel responsible for what happened."
    show bree gloomy
    "[bree.name] shakes her head at this, already fighting back more tears."
    "She surprises me by taking hold of my hands and squeezing them tightly."
    show bree surprised
    bree.say "No, no, no!"
    bree.say "You can't think that, [hero.name]."
    bree.say "There's no way you could have known she was..."
    show bree gloomy
    mike.say "Crazy?"
    show bree sad
    bree.say "Yeah, that's right."
    show bree gloomy at center, zoomAt(2, (640, 1380)) with fade
    "[bree.name] leans her head on my shoulder, pressing her weight against me."
    "It makes me feel instantly more guilty, but I don't even try to stop her."
    "I guess I need all the comfort that I can get right now, and so does she."
    show bree cry
    bree.say "What happened was awful, so awful..."
    bree.say "But that psycho could have killed all three of us, you know?"
    bree.say "You and I should be thankful that she didn't."
    bree.say "And I think..."
    show bree gloomy
    "[bree.name] pauses to stifle a sob."
    show bree normal
    "And then she pushes on with what she was going to say."
    show bree talkative
    bree.say "I really think Sasha would want us to get on with our lives."
    show bree normal
    mike.say "I...think I know what you mean, [bree.name]."
    mike.say "Sasha always lived life to the full, didn't she?"
    show bree talkative
    bree.say "Yeah - so she'd probably tell us off for moping around!"
    show bree normal
    "The thought of Sasha and her unique quirks makes me shake my head."
    show bree happy
    "[bree.name] seems to be affected in the same way, as she lets out a sudden laugh."
    "It's pained and I can see that she feels embarrassed to be finding this funny."
    show bree cry
    "But when she bursts into tears straight afterwards, I hug her close to me."
    "As I hold [bree.name], I start to feel a little better."
    "It's not much to cling to right now."
    "But maybe it's the first step towards healing for the both of us."
    return

label bree_rape_talk:
    "I fancy myself a modern guy in most respects, and so what I want to do shouldn't be an issue."
    "But even a modern guy can forgive himself for something on this kind of scale - right?"
    "I mean, [bree.name] and Sasha burst into my room and literally saved me from Kylie the other night."
    "Let's call it what it is - that mad bitch was going to rape me!"
    "And she'd have had her way if it weren't for my housemates coming to my rescue."
    "I know that I should thank them, at the very least, for what they did."
    "But I can't help feeling ashamed of the state that they found me in that night."
    "I know a modern guy shouldn't think it's any different for a man than a woman."
    "And yet I'm still embarrassed by what happened and afraid to show my face."
    show bree surprised at center, zoomAt(1.5, (640, 1040)) with hpunch
    "In the end, it comes down to me bumping into [bree.name] in the hallway."
    show bree happy
    "We both smile awkwardly, and it looks like nobody's going to speak."
    "But then we both open our mouths at the same exact moment."
    mike.say "[bree.name], I just..."
    show bree talkative
    bree.say "[hero.name], are you..."
    show bree blush sadsmile
    "As soon as we both start talking, we stop again."
    "I rub the back of my neck, trying to smile nonchalantly."
    "And [bree.name]'s cheeks have gone more than a little red too."
    "In the end, it's [bree.name] that recovers first."
    show bree talkative
    bree.say "Sorry, [hero.name]."
    bree.say "I just wanted to ask if you were okay?"
    show bree sadsmile
    mike.say "I...I'm still shaken up, [bree.name]."
    mike.say "But I'll be okay."
    "There's a moment of silence as [bree.name] nods her head."
    show bree happy
    bree.say "Good..."
    bree.say "That's good."
    show bree sadsmile
    mike.say "I was going to say thank you, just then."
    "Now [bree.name] really does look embarrassed."
    "She shakes her head and waves my words away."
    show bree talkative
    bree.say "Don't be silly, [hero.name]."
    bree.say "You'd have done the same for me!"
    show bree annoyed -blush
    "She shakes her head for a second time."
    show bree angry
    "But this time it's from annoyance at the memory of what Kylie did."
    show bree vangry
    bree.say "Urgh..."
    bree.say "The thought of what that horrid girl was doing to you!"
    show bree angry
    mike.say "Don't even think about it, [bree.name]."
    mike.say "And thank you - I really mean it."
    show bree happy
    "[bree.name] nods, her expression changing to one of happiness."
    show bree at center, traveling(2.5, 0.3, (640, 1640))
    "She leans forwards and plants a little kiss on my cheek."
    show bree wink
    bree.say "That's okay, [hero.name]."
    bree.say "We all have to stick together in this house."
    bree.say "It's us against the world!"
    return


label bree_fight_dad:
    "Everything happens so quickly that I can't even hope to keep upright, let alone defend myself."
    "One minute I'm walking down the street, checking my phone and minding my own business."
    with vpunch
    "And the next I feel something grab me by the collar, choking the breath right out of me."
    "Before I can even make a sound, let alone form the beginning of a protest, I'm hauled backwards."
    show breedad with hpunch
    breesdad "C'mere, mother-fucker!"
    breesdad "You an' me are gonna have words!"
    "The voice is gruff and threatening, sounding vaguely familiar to my ear."
    "But I barely get the chance to see the face it belongs to as I'm spun around to face my attacker."
    "What I do get to see up close is the sight of his clenched fist as it speeds towards me."
    with vpunch
    mike.say "Wha..."
    play sound punch_hard
    pause 0.2
    with hpunch
    mike.say "Urgh..."
    "I barely understand what just happened until the fist is drawn back for a second blow."
    "But I sure as hell feel the next punch as it connects squarely with my nose."
    play sound punch_hard
    pause 0.2
    with vpunch
    "The third and fourth are less distinct though, the impacts more fuzzy."
    play sound punch_hard
    pause 0.2
    with vpunch
    show layer master at blur(5)
    "Not because my attacker's pulling his punches, but because my head is starting to spin."
    breesdad "Not so tough now, huh?"
    breesdad "Where's your smart mouth now, asshole?!?"
    breesdad "Hard to talk when you're swallowin' your own teeth!"
    scene expression f"bg {game.room}" at center, zoomAt(1.35, (640, 720))
    show bree fight dad
    show layer master at blur(0)
    with vpunch
    "I don't feel my legs give way, just the sensation of my ass hitting the ground."
    "He follows me down too, not trying to keep me upright for a moment."
    "Instead he has a handful of my shirt."
    "And uses this to keep me from collapsing onto my back."
    breesdad "Oh no you don't."
    breesdad "Don't go passing out on me yet, you fucking shit!"
    "My vision's losing focus even as he yells this in my face."
    "I can taste blood in my mouth, even feel myself choking on it a little."
    "Maybe if I'd had a notion he was going to jump me."
    "Maybe then I'd have stood a chance, been able to fight back."
    "But I can tell that he's a big guy, and I know first-hand that his fists are like hams."
    "The face looking down at me is old enough to be one of my dad's buddies."
    "And old as the guy is, it's not like he's showing any signs of getting tired or blown up yet."
    breesdad "Maybe I should've tried talkin' first."
    breesdad "But I've seen your type before, buddy."
    breesdad "You're all bullshit and backchat."
    breesdad "Gotta cut straight to the chase, gotta send a message."
    play sound punch_hard
    pause 0.2
    with hpunch
    "As if to underline the point, he treats me to another couple of punches to the face."
    "Sure, they're not as vicious as the first ones he gave me."
    "But I the pain I'm feeling is soon amped up."
    "And I can feel more blood flowing after he's finished."
    "Finally he lets go of my shirt, allowing me to crumple to the ground."
    "He stands up working his knuckles as he does so, nodding to himself the whole time."
    breesdad "You make sure you learn the lesson I just taught you, prick."
    breesdad "This is what happens to any guy that messes with my little girl!"
    breesdad "You don't want to take the advanced class either - 'cos it's a fuckin' bitch!"
    "'My little girl'?!?"
    "Wait...is this about a girl?"
    "About someone that I've been messing around with?"
    "I think about opening my mouth to ask a question."
    "But the taste of blood on my tongue and the feeling of loose teeth stops me in my tracks."
    "After taking a beating I just took, actually asking for the girl's name would be suicide!"
    "And so I just lie there in agonised silence."
    scene expression f"bg {game.room}"
    show breedad
    with fade
    "The guy takes the time to spit on the ground next to me, shaking his head as he does so."
    "Then he turns on his heel and walks away."
    hide bree fight dad with easeoutleft
    "I note that he doesn't run or even hurry on his way."
    "Which means that he's pretty confident I won't be getting up any time soon."
    "And as I lie there, clutching at my pounded face, I know that he's right..."
    show bg black with dissolve
    $ hero.fun -= 10
    $ hero.energy -= 10
    $ hero.grooming -= 10
    return

label bree_fight_mourning_dad:
    if bree.flags.girlfriend or bree.flags.fiance or not kylie.sexperience:
        "I kind of feel like I've been walking around in a trance since it happened."
        "Hell, I'm even having trouble calling it what it was, the trauma's so bad."
        "So when I hear the sound of someone yelling close by, I just ignore it."
        "Because there's already so much stuff going on inside of my head, you know?"
        breesdad "[hero.name]…"
        breesdad "Hey, [hero.name]!"
        breesdad "You can hear me, yeah?"
        with vpunch
        "The only thing that stops me from walking away is the sensation of a hand on my shoulder."
        "And it's not a gentle hand either, but rather one that's clamping on like a bear-trap!"
        "I'm spun around before I can say a single word, but I'm less than pleased with that."
        show breedad at center, dark
        "So I end up with a frown on my face as I find myself facing the owner of the hand."
        mike.say "What the actual fuck?!?"
        mike.say "Who do you think you..."
        hide breedad
        show bruce
        with dissolve
        "Before I can finish what I'm saying, I recognise who has a hold of me."
        mike.say "B...Bruce?"
        mike.say "Is that really you?"
        mike.say "I'm sorry...I didn't mean to be rude!"
        "I'm used to seeing [bree.name]'s dad with a frown on his face."
        "Because he's one of those genuinely miserable old bastards."
        "You know the kind, right?"
        "Ex cops or teachers from state schools?"
        "But what's throwing me right now is that he doesn't look pissed."
        show bruce quiet
        "For once he looks emotional, like he's on the verge of tears."
        show bruce talkative
        breesdad "Nah, buddy..."
        breesdad "It's cool, it's cool - I totally get it."
        breesdad "You're mad, edgy, angry at the whole fucking world, right?"
        show bruce normal
        "Another time I'd have disagreed with him."
        "I'd have explained that I was pissed at being manhandled by some macho jerk."
        "But this doesn't seem to be the time or place to start throwing blame around."
        "So I just nod, putting a grim smile on my face."
        mike.say "Yeah, Bruce..."
        mike.say "That's it exactly."
        mike.say "I wanna...I wanna fight the whole fucking world!"
        show bruce talkative
        breesdad "Yeah, buddy..."
        breesdad "Ain't that the truth of it!"
        show bruce normal
        "For a moment there's a weird kind fire in Bruce's eyes."
        "Like he's going to throw caution to the wind and suggest something."
        "Something crazy like the two of us stock up on guns and become vigilantes."
        "Go out into the night and take justice into our own hands..."
        "But then he shakes his head and slaps me hard on the shoulder."
        show bruce talkative
        breesdad "I had it all worked out, you know?"
        breesdad "All the stuff I was gonna say to you about [bree.name]..."
        breesdad "But the second I saw you, it all just vanished out of my head!"
        show bruce normal
        mike.say "I'm sorry, Bruce..."
        mike.say "I know it's just words and it doesn't change anything..."
        "Bruce waves a hand in the air and shakes his head."
        show bruce talkative
        breesdad "I know, I know, buddy..."
        breesdad "But at times like this you gotta say things that matter."
        breesdad "In case you don't get to say it later, you gotta explain yourself."
        breesdad "Like when I first met you, I was kinda hard on you."
        breesdad "But that was just because I wanted the best for [bree.name], yeah?"
        show bruce normal
        "Bruce is looking at me with something in his eyes that I don't recognise."
        "In someone that was less of a shit-kicker, I'd have said it was pleading."
        mike.say "I get it, man..."
        mike.say "Dads look out for their daughters."
        mike.say "No guy's ever good enough."
        show bruce talkative
        breesdad "No, no, no..."
        breesdad "I was being hard on you because I saw something in you, buddy."
        breesdad "You seemed to make [bree.name] happy, that was the biggest thing."
        breesdad "But I was sure you were tough underneath, you know?"
        breesdad "Under all the modern pussy boy bullshit?"
        show bruce normal
        "I get the feeling that Bruce is really trying to open up to me right now."
        "The problem is that he still kind of sounds like he's insulting me too."
        mike.say "Erm..."
        mike.say "Thanks?"
        mike.say "I think?"
        "Bruce nods, seeming to think that I'm reading him loud and clear."
        show bruce talkative
        breesdad "I just needed to tell you that, buddy..."
        breesdad "To let you know I could have stood to have you as a son-in-law."
        if not "kylie_trial_2" in DONE:
            breesdad "But at least there's one thing to look forward to, right?"
            show bruce normal
            mike.say "There is?"
            show bruce talkative
            breesdad "Ah, come on, [hero.name]…"
            breesdad "Don't try being all woke and leftie with me!"
            breesdad "This way we get to watch that murdering bitch fry."
            breesdad "Get to see her pay for what she did to my little girl!"
            show bruce normal
            "All I can do is blink in genuine surprise."
            "It might sound crazy, but I hadn't really thought about that too much."
            "About whether I want to be there to see Kylie's execution."
            "Even if I could stand to watch it happen from elsewhere."
            mike.say "I..."
            mike.say "I guess so."
            "I don't think Bruce is really listening to what I'm saying right now."
            "Or else he's not picking up on the nuances of my tone."
            "Because he just grins, the expression almost turning into a genuine snarl."
            show bruce talkative
            breesdad "Yeah, you know that's gonna be fun to see."
            breesdad "I'll reserve you a front-row seat, [hero.name]…"
            breesdad "Hell, I'll even bring the fucking popcorn!"
        hide bruce
        show breedad
        "With that, Bruce seems to think that the conversation is over."
        "He shoots me one of those pointing gestures, you know?"
        "The kind overly macho guys use to say goodbye to their buddies?"
        hide breedad with easeoutleft
        "And then he turns on his heel and walks away."
        "Which leaves me feeling a new level of shame and grief hollowing me out."
        "Another whole layer of stuff that I'm going to have to process somehow."
        "But at least I get the chance to do that."
        "Which is more than you can say for poor [bree.name]."
    else:
        "I can't say that life's been much fun for me recently."
        "In fact I'd go as far as say that it's kind of been turned to shit."
        "And I've been wandering around like I'm not quite right in the head."
        "Which is why I don't turn around when I hear a voice shouting nearby."
        breesdad "Hey..."
        breesdad "Hey, you!"
        "I mean, the voice sounds vaguely familiar."
        "You know, like I maybe heard it somewhere before?"
        "But the person speaking sounds angry and bitter."
        "Which isn't something that I'm going to gravitate towards."
        with vpunch
        "It's only when I feel a hand on my shoulder that I start to pay attention."
        breesdad "Hey, dipshit..."
        breesdad "I'm talking to you!"
        "Before I can say a word, I find myself being spun around."
        show breedad with hpunch
        "And the first thing that I see when I stop turning is a rather angry face."
        "One that's even better at snapping me out of my funk than the hand on the shoulder."
        mike.say "B...Bruce?!?"
        mike.say "Oh man..."
        mike.say "I...I don't know...I meant to..."
        "I'm babbling and stumbling over my words as I try to get my brain in gear."
        "Which is understandable when you consider that the guy standing there is Bruce."
        "The tough cop father of [bree.name], my recently deceased housemate."
        "And the girl that I was supposedly in a relationship with."
        "At least until the psycho I was cheating on her with went and killed her!"
        "So yeah, you know that this is going to get super-intense pretty quickly."
        show bruce angry
        breesdad "You shut your fucking mouth, buddy..."
        breesdad "And open your goddamn ears too."
        breesdad "Because you're gonna hear what I have to say, whether you like it or not!"
        show bruce normal
        "As if he needs to make his point clearer, Bruce snatches a handful of my collar."
        with hpunch
        "Then he proceeds to shove me up against the nearest wall, and hard too."
        mike.say "Urgh..."
        "It all happens too fast for me to even think of putting up any resistance."
        "And even if I could have, it'd probably be the dumbest idea possible."
        "After all, this guy's a real hard-nosed kind of cop, proper tough guy."
        "Plus he's on the warpath right now, probably looking to hurt someone."
        "But seeing as his daughter just got murdered, can you blame him?"
        show bruce talkative
        breesdad "I never liked you..."
        breesdad "Not from the first second I knew you even existed."
        breesdad "Then moment my little girl told me she was moving in with some guy..."
        breesdad "I just knew I was gonna have to put my hands on him sooner or later."
        show bruce normal
        "I'm doing all I can to nod and look like I'm listening."
        "But it's hard when someone's spitting their anger straight into your face."
        "That and you're thinking they might start beating you any second!"
        show bruce talkative
        breesdad "And when she told me she was dating this jerk..."
        breesdad "I ain't gonna lie - the red mist started to come down over me!"
        show bruce normal
        "Bruce pauses for a moment, closing his eyes and taking a deep breath."
        show bruce talkative
        breesdad "But I told myself that I needed to change..."
        breesdad "I told myself that's what the old me would have done."
        breesdad "So I swallowed it and put a smile on my face - I played nice with you."
        show bruce normal
        "Even as scared as I am right now, that doesn't exactly ring true."
        "I mean, Bruce was never exactly nice to me."
        "Not on any of the few occasions I met him before..."
        "Well, I guess there's no other way to say it...before [bree.name] passed."
        "Maybe he became a little less of an asshole with time."
        "But that's an observation I'll probably keep to myself."
        "And instead of challenging Bruce's narrative, I nod the whole time."
        show bruce talkative
        breesdad "But I was right, wasn't I?"
        breesdad "I was fucking right all along!"
        show bruce normal
        play sound punch_hard
        "Bruce underlines his point by landing a punch right beside my head."
        "And it doesn't seem to bother him that means he's just connected with the wall!"
        "I flinch out of sheer instinct, wincing at the blood on his knuckles."
        mike.say "Y..yeah…"
        mike.say "You sure were, Bruce!"
        show bruce talkative
        breesdad "Yeah, you bet I was!"
        breesdad "Man, if only you'd cheated on her with a normal broad."
        breesdad "That way I'd have just beat the living shit out of your ass!"
        breesdad "But oh no, not you..."
        breesdad "Mister Fancy-pants here had to go and sleep around with a psycho."
        breesdad "A genuine, one hundred percent fucking fruit-cake."
        show bruce normal
        "Bruce stops shouting for a moment and shakes his head."
        "As usual, I'm not sure what he's going to do next."
        "Whether he's going to attack me or else collapse into a flood of tears."
        mike.say "Erm..."
        mike.say "I'm...sorry?"
        "I wince again as the words come out of me."
        "Still expecting Bruce to snap and start beating me."
        if not "kylie_trial_2" in DONE:
            "But instead he lets out a grim chuckle."
            show bruce talkative
            breesdad "Huh..."
            breesdad "At least this way there's one thing to look forward to, right?"
            show bruce normal
            mike.say "There is?"
            show bruce talkative
            breesdad "Ah, come on, [hero.name]…"
            breesdad "Don't try being all woke and leftie with me!"
            breesdad "This way we get to watch that murdering bitch fry."
            breesdad "Get to see her pay for what she did to my little girl!"
            show bruce normal
            "All I can do is blink in genuine surprise."
            "It might sound crazy, but I hadn't really thought about that too much."
            "About whether I want to be there to see Kylie's execution."
            "Even if I could stand to watch it happen from elsewhere."
            mike.say "I..."
            mike.say "I guess so."
            "I don't think Bruce is really listening to what I'm saying right now."
            "Or else he's not picking up on the nuances of my tone."
            "Because he just grins, the expression almost turning into a genuine snarl."
            show bruce talkative
            breesdad "Yeah, you know that's gonna be fun to see."
            breesdad "I'll reserve you a front-row seat, [hero.name]…"
            breesdad "Hell, I'll even bring the fucking popcorn!"
        else:
            "But instead he lets out a sad sigh, looking at me with tired eyes."
        hide bruce
        show breedad
        "With that, Bruce seems to think that the conversation is over."
        if not "kylie_trial_2" in DONE:
            "He shoots me one of those pointing gestures, you know?"
            "The kind overly macho guys use to say goodbye to their buddies?"
        hide breedad with easeoutleft
        "And then he turns on his heel and walks away."
        "Which leaves me feeling a new level of shame and grief hollowing me out."
        "Another whole layer of stuff that I'm going to have to process somehow."
        "But then in the grand scheme of things, is that really so bad?"
        "At least I got a better deal than poor [bree.name] did."
        "At least I got to live, even if I do feel wretched and guilty all the time."
    $ hero.fun -= 10
    return

label bree_asleep:
    if samantha.room == game.room:
        show multisleep breesam bree samantha
        "[bree.name] and Sam are sleeping, I should leave before I wake them up..."
    else:
        show sleep bree
        "[bree.name] is sleeping, I should leave before I wake her up..."
    $ game.room = "secondfloor"
    return

label bree_call_daddy:
    show bree b annoyed at center, zoomAt(1.25, (640, 880))
    "I can usually tell when there's something on [bree.name]'s mind, as she's not the best at concealing her thoughts and moods."
    "And as she keeps glancing sideways at me, it's clear that there's something she desperately wants to ask me right now."
    "From the way that she keeps fiddling with her collar, my best guess would be that she's uncomfortable or it's too tight."
    "But as she's so well trained and determined to behave herself, she makes no attempt even to ask for permission to speak."
    "So finally, when I'm sure that she's probably suffered enough, I decide to broach the subject."
    mike.say "[bree.name], you have permission to speak."
    mike.say "So you can tell me what the problem is."
    mike.say "Is it your collar that's too tight?"
    mike.say "Or maybe not tight enough?"
    show bree stuned at vshake
    "At the sound of my saying her name, [bree.name] perks up immediately."
    show bree smile
    "She looks me straight in the eye and gives me an eager, happy smile."
    show bree happy
    bree.say "Yes, Master!"
    show bree sadsmile
    "But as I reach for her collar, her expression becomes unsure."
    show bree sad
    bree.say "I...I mean no, Master!"
    show bree gloomy
    "I make a little frown and cock my head quizzically on one side."
    show bree sad
    bree.say "I'm sorry, Master."
    bree.say "No, my collar's fine."
    bree.say "I just...just wanted to ask you something."
    show bree sadsmile
    mike.say "Go ahead, [bree.name]."
    mike.say "While ever you've got permission to speak, you can ask me whatever you like."
    show bree normal
    "[bree.name] smiles in that cute, agreeable way again."
    show bree talkative
    bree.say "Well...I wondered if you liked it when I call you 'Master', Master?"
    show bree sadsmile
    "I have to admit, the question catches me a little off guard."
    "It's not something that I've really sat down and thought about, even since [bree.name] started calling me that."
    menu:
        "I like it":
            mike.say "Yes, [bree.name], I guess I really do like it when you call me that."
            mike.say "It makes me feel like you respect me, that you really appreciate what I do for you."
            mike.say "Like we all know our place too."
            show bree normal
            "[bree.name] nods at this, clearly satisfied with my explanation."
            show bree happy
            bree.say "Okay, Master."
            bree.say "If it makes you feel good, that's reason enough for me."
            show bree flirt at center, traveling(2, 0.5, (640, 1380))
            "She snuggles herself closer to me, making pleasant sounds of satisfaction."
            show bree talkative blush
            bree.say "I love you, Master."
            show bree normal
            mike.say "I love you too, [bree.name]."
        "I don't like it":
            mike.say "Now that I come to think of it, I really don't."
            mike.say "It sounds so old-fashioned and creepy, like something out of bad B-movie!"
            show bree lose
            "[bree.name] looks at me with mounting concern in her eyes."
            bree.say "I'm so sorry, Mas...erm..."
            show bree sad
            bree.say "Oh bother - I don't know what to call you now!"
            show bree annoyed
            "I see that [bree.name]'s lost in thought for a moment."
            show bree normal
            "But then the light of inspirations flashes in her eyes."
            show bree talkative blush
            bree.say "Maybe...maybe I could call you...'Daddy'?"
            show bree normal
            mike.say "What...why?"
            show bree flirt blush
            "[bree.name] suddenly goes all bashful, refusing to meet my eye and wringing her hands."
            bree.say "Well, I always liked the idea of being treated like a little girl..."
            show bree surprised
            bree.say "Not an ACTUAL little girl!"
            bree.say "Because that would be too creepy!"
            show bree flirt
            bree.say "More like I had a sugar-daddy that kept me like I was all young and innocent..."
            show bree happy -blush
            "At this, [bree.name] flutters her eyelashes at me, and I can't help but swallow audibly."
            mike.say "Well...we...we could definitely give it a try, see how it feels."
            bree.say "Oh, thank you...DADDY!"
            $ bree.flags.daddy = True
    return

label bree_call_daddy_slutty:
    show bree b
    "I can tell from the way she's looking at me that [bree.name] has something on her mind."
    "Most likely something that she wants to ask me, but is afraid to speak up about."
    "More than once she looks like she's plucked up the courage to actually say it."
    show bree annoyed blush
    "But then she seems to get embarrassed and nothing comes out of her mouth."
    "So in the end, I decide that the best thing is to take the bull by the horns..."
    mike.say "What's eating you, [bree.name]?"
    mike.say "You look like you've got something to ask me."
    show bree stuned
    "The instant that I say this, [bree.name] starts acting all innocent and surprised."
    "Which is pretty much proof positive that I'm right."
    show bree surprised
    bree.say "What?!?"
    bree.say "No...no way, [hero.name]!"
    bree.say "Why would you even..."
    show bree stuned
    "I raise an eyebrow at her suspicious protests."
    show bree normal
    "And it seems to have the desired effect."
    show bree talkative -blush
    bree.say "Okay, okay..."
    bree.say "There was something I'd been meaning to ask."
    bree.say "But you've got to promise you won't laugh, yeah?"
    show bree normal
    "Well, now I'm more than a little intrigued."
    "And so I nod, trying to put a serious and reassuring expression on my face."
    mike.say "Sure thing, [bree.name]."
    mike.say "What could you possibly ask me that'd make me laugh?"
    mike.say "Go on, ask away."
    show bree sadsmile
    "[bree.name]'s smile is more than a little nervous."
    "Which makes me all the more intrigued as to what's on her mind."
    show bree talkative
    bree.say "Well..."
    bree.say "I...I kinda like it when you call me stuff."
    bree.say "I mean, when we're doing it!"
    show bree flirt
    "I can see the light that's growing in [bree.name]'s eyes as she begins to explain herself."
    "It's the same one that fills her whenever we get the chance to do it."
    "The way she seems to throw herself into it every time we fuck!"
    show bree talkative
    bree.say "And..."
    bree.say "I want to call you stuff too, [hero.name]."
    show bree evil blush
    bree.say "I want to call you 'Daddy'..."
    bree.say "I...I don't know why."
    show bree flirt -blush
    bree.say "It just makes me feel...feel SO horny!"
    "Now that she's shared what was eating at her with me, [bree.name] waits for my answer."
    show bree normal
    "Her eyes are wide and she looks more vulnerable than I can ever recall seeing her."
    "But it doesn't take me long to come up with an answer."
    menu:
        "I like it":
            "Even the thought of [bree.name] calling me that is enough to turn me on."
            "And I can't keep it from showing as I look her in the eye."
            mike.say "Wow..."
            mike.say "Seriously, [bree.name] - that's SO fucking hot!"
            "I see the delight that fills [bree.name]'s eyes as I say the words."
            show bree happy
            "Her smile becomes wider still, and she claps her hands together happily."
            bree.say "So you're okay with it?"
            bree.say "I can call you that when we do it?!?"
            show bree normal
            mike.say "Sure thing, [bree.name]."
            mike.say "Just so long as we don't have to wait long until you do!"
            show bree flirt
            "[bree.name] claps again, giggling with sheer delight."
            show bree happy blush
            bree.say "Oh, I don't think that's gonna be a problem, Daddy."
            bree.say "Just thinking about it's getting me hot."
            bree.say "You know - making me imagine your cock inside of me?!?"
            show bree normal
            "Shit - she's getting me hot just talking about it too!"
            "For now I try to just nod and smile."
            "But all the while, my mind is full of the possibilities."
            $ bree.flags.daddy = True
        "I don't like it":
            "The very thought of [bree.name] calling me that is an instant turn-off."
            "And I can't keep myself from shivering with revulsion."
            mike.say "Urgh..."
            mike.say "Seriously, [bree.name] - that's fucked up!"
            show bree gloomy
            "I can see the disappointment and hurt my words are causing."
            "But I'm not about to lie to [bree.name] and let her call me that."
            "Being dishonest about that kind of thing is a bad path to start down."
            "So it's better to hurt her feelings now."
            "Because doing the opposite will do more damage later."
            show bree sad
            bree.say "Oh..."
            bree.say "I...I didn't realise."
            bree.say "I'm sorry, [hero.name]!"
            show bree gloomy
            "I nod, accepting her apology as the end of the matter."
            mike.say "It's okay, [bree.name]."
            mike.say "Let's just forget about it, okay?"
            show bree sadsmile
            "[bree.name] nods and forces a smile onto her face."
            "And I do the same in return."
    return

label bree_go_to_the_beach:
    show bree evil
    "Having a housemate like [bree.name] wandering about the place on a daily basis is pretty distracting at the best of times."
    show bree at left4 with move
    "I regularly find myself staring longer than I really should, running the risk of being seen and labelled a creep."
    show bree b happy at right5 with move
    "It's even worse when I get literally stopped in my tracks when she stretches or bends over for something within my line of sight."
    show bree a normal at center with move
    "Holding a conversation can be a challenge as well, trying to pay attention to what [bree.name]'s saying when she's just so darn distracting."
    "Right now would be a good example of this problem."
    "[bree.name]'s just asked me a question that totally slipped by me."
    "I've been nodding and making vaguely affirmative noises, but she's starting to look at me funny."
    "If I try really hard, maybe I can snap myself back to reality..."
    show bree talkative at center, zoomAt(1.5, (640, 1040))
    show fx exclamation
    bree.say "[hero.name]...[hero.name]!"
    bree.say "Are you even listening to me right now?"
    show bree normal
    "I shake my head and manage to make it at least look like I'm paying attention."
    "Luckily for me, [bree.name] seems to be more amused than anything else."
    show bree a happy at center, traveling(1.25, 0.5, (640, 880))
    "She giggles at my apparent distraction and shakes her head."
    show bree talkative
    bree.say "Oh, [hero.name] - you've always got your head in the clouds!"
    show bree normal
    mike.say "Sorry, [bree.name] - I was miles away."
    mike.say "What were you saying just now?"
    "[bree.name] shakes her head again, apparently finding foibles cute, rather than annoying."
    show bree normal
    "Which honestly doesn't help me as I try to ignore how cute she is herself."
    show bree talkative
    bree.say "What I said was that someone mentioned there was a beach nearby."
    bree.say "One not too far away from here?"
    show bree normal
    "She's right, of course - the beach pretty darn close, one of the real perks of living in this neighbourhood."
    "I'm about to second what she's been told, but then a sudden thought occurs to me."
    "What are the odds of [bree.name] actually needing me to confirm something that's common knowledge?"
    "That'd be pretty odd, unless..."
    "Unless she's really fishing for an invitation to the beach from me!"
    "Aware that I could be getting ahead of myself, I try to play it cool."
    mike.say "Ah...yeah, [bree.name]...that's right."
    mike.say "It's super close - if you're going to cycle there or drive."
    mike.say "But it's probably a bit too far to walk."
    show bree happy
    "[bree.name] smiles at this, clearly pleased with what she's been told."
    if hero.has_motor_vehicle:
        "But she doesn't seem to be about to take the bait that I've offered."
        "My car's sitting in the driveway of our house, yet she's not even asking me for a lift."
        "I know what I should do here, and that's play it cool."
        show bree normal
        "She'll catch my drift soon enough, so there's no need to go shooting my mouth off just yet..."
        mike.say "I have a car, you know!"
        mike.say "I could drive you...if you want?"
        "Damn it - smooth as a dog-shit sandwich!"
        show bree smile
        "[bree.name] smiles at my clumsily blurted offer all the same."
        bree.say "Aww, that's sweet of you to offer, [hero.name]."
        show bree happy
        bree.say "But I'm a big girl, and I think I can find my way to the beach!"
        $ bree.love += 1
    return

label bree_male_ending:
    $ game.hour = 16














    if renpy.has_label("bree_achievement_3") and not game.flags.cheat:
        call bree_achievement_3 from _call_bree_achievement_3
    $ game.room = "church"
    $ game.season = 1
    scene bg church wedding
    "There was a time when I'd have thought that a church wedding with all of the gaudy trimmings and traditional trappings was something I would avoid at all costs."
    "But I guess that a lot's changed, in terms of both myself and my life in recent times, enough to make me rethink a lot of the assumptions I made in the past."
    "What am I even trying to say here?"
    "It's [bree.name] that's changed me and my life, a great deal and all for the better!"
    "She's the reason that I'm standing at the altar in such a grand church, done up in a fancy suit and listening to the music playing that's supposed to accompany her down the aisle."
    "Everything about the wedding that we've planned is inspired by her, not that she'd be aware of that fact."
    "Me, well...I'm kind of a retiring type."
    "What's officially my side of the church is nowhere near filled by the few members of my family and close friends that I cared to invite."
    "By way of contrast, [bree.name]'s side is so full that guests are spilling over into the empty pews on the other."
    "Friends from as far back as her childhood and right up to the present day are crammed in next to a procession of relatives that never seems to end."
    "It honestly didn't look like this many people when we sat down to put the guest list together!"
    "But that's just my point - [bree.name] takes me out of my rut, puts me somewhere that I can't predict, she makes my life vital and exciting."
    "I mean it when I say that I can genuinely feel my heart racing, as I look back over my shoulder for the first glimpse of her entering the church."
    show bree b wedding flirt blush at center, zoomAt(1.0, (640, 720)) with dissolve
    "And there she is..."
    "Ah...I...wow!"
    "Sorry about that - it's just that, what with [bree.name] being such a stickler for tradition, she kept me from seeing the dress she's chosen until this very moment."
    "And I'm glad that she did, because she looks simply stunning."
    "I honestly can't remember how the kids and young teenagers that make up her bridal party are related to her or what any of their names are."
    "They could not be there at all for the tiny amount of attention that I can spare for them."
    show bree at center, traveling (1.5, 5.0, (640, 1040))
    "Right now, [bree.name]'s the only person that I want to lay eyes on."
    if not bree.is_visibly_pregnant:
        "I'm surprised to see that, despite being fond of tradition, [bree.name]'s chosen to wear pink."
        "A light, floating affair that's short in the front and long in the back."
        "Pink roses woven into a headband and the locks of her hair compliment the delicate tones of her skin."
        "And she clutches a bouquet of the same flowers, though their beauty is put to shame by the smile on her face as she walks towards me."
        "The expression on my face must be as easy to read as words on a page, making [bree.name] blush a little as she reaches my side."
        "Though my hand was supposed to be in my pocket to keep hold of the ring, I find myself now using it to pinch myself on the thigh instead."
        "Part of me just can't believe this is actually happening!"
    else:
        "I'm surprised to see that, despite being fond of tradition, [bree.name]'s chosen to wear pink."
        "A light, floating affair that's short in the front and long in the back."
        "Pink roses woven into a headband and the locks of her hair compliment the delicate tones of her skin."
        "And she clutches a bouquet of the same flowers, though their beauty is put to shame by the smile on her face as she walks towards me."
        "The dress has been tastefully cut to accommodate the curve of [bree.name]'s belly, and so this only adds to her radiance."
        "That's one thing that neither of us is old fashioned about."
        "We both take delight in being reminded of the fact that we're expecting our first child together."
    show wedding bree with fade
    "I'm about to say something to her, compliment the dress or make a comment about how good she looks."
    "But then there's a discreet cough, and I glance around to see the priest smiling and glancing at his watch."
    "I look back to [bree.name], who has an amused grin on her face, clearly aware that I was taken completely out of the moment at the sight of her."
    show wedding bree priest with dissolve
    "She shakes her head in a gesture of affection, and we both turn to face the priest, with me at least trying to look prepared for what lies ahead."
    "But I needn't have worried, as the whole thing comes off as smoothly as it did in the rehearsal."
    "In fact, once we've exchanged our vows and then the rings, it take me a few seconds to realise that it's for real this time."
    show wedding bree -priest with dissolve
    "[bree.name] and I are actually now husband and wife!"
    scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
    show bree kiss wedding
    with fade
    $ bree.flags.kiss += 1
    "When the time comes to kiss the bride, I don't do anything dramatic, like bending her over backwards."
    "Instead we kiss with a brief, understated brush of the lips."
    "But the electricity I feel as we do so is worth more than any amount of unrestrained Frenching."
    hide bree
    show bree b wedding happy at center, zoomAt (1.5, (640, 1040))
    with fade
    "All of the usual stuff follows the actual ceremony - throwing the bouquet over the shoulder, tossing confetti and the like."
    "For me, all of it's a blur, things that I'll need [bree.name] to talk me through when we get hold of the wedding album."
    "It's all I can do to tear my eyes away from her for more than a couple of seconds at a time."
    "Maybe I'll soon get used to the fact that the girl who was once only my housemate, then my friend and lover is now my wife."
    "But I don't think I'll ever be able to take someone as amazing as [bree.name] for granted, no matter how long she happens to be a part of my life."
    scene bg park
    show bree ending
    with fade
    bree.say "Bet you were thinking that this was the end of the story, and you were gonna hear from [hero.name] again to wrap it all up, huh?"
    bree.say "Well, surprise - you were wrong twice over!"
    bree.say "This is as much my story as it is [hero.name]'s, and I can assure you that it's far from over."
    bree.say "Sure, it took us a while to get here, and there were some bumps along the way."
    bree.say "But I don't think that I'd change anything, even if someone told me that I could."
    bree.say "Those bumps will become fond memories soon, and we'll laugh about them when we look back."
    bree.say "We have the rest of our lives to look forward to, and I'm going to make sure that we live every day to the full."
    bree.say "I'll admit, when I first moved into the house with him, that I maybe didn't appreciate [hero.name] as much as I should have."
    bree.say "He was sweet and looked pretty cute, but I guess I was in a fuss about living in a new place with new people."
    bree.say "So it kind of took me a while to notice him in that way, which meant that he grew on me a little at a time."
    bree.say "By the time I realised he was sneaking his way into my affections, it was too late!"
    bree.say "And now I can't imagine what life would be like without him."
    bree.say "Sure, he's a typical guy most of the time, forgetful, messy and with his mind always on the one thing a guy's mind is always on."
    bree.say "But he's also sensitive, caring and he makes me feel like I'm the thing that he wants most in the world."
    bree.say "So you don't need to remind me, as I know just how lucky I am to have found him."
    bree.say "After the wedding and the honeymoon, we came back to the house."
    bree.say "And for a little while at least, things felt like they were pretty much back to normal."
    bree.say "But somehow we all knew that the old times were gone, no matter how much we hated to admit it."
    bree.say "Somehow the place felt crowded now, even though there were still only three of us under the same roof."
    if not bree.is_visibly_pregnant:
        bree.say "Sasha never said as much out loud, but I think that we were cramping her style."
        bree.say "It's hard to be the spare wheel when the other people in the house do everything as a couple."
        bree.say "So she moved out a couple of months after the wedding and found a place of her own."
        bree.say "We still see her every now and again, though not as often as either of us would like."
        bree.say "But I can't hide the fact that part of me likes the fact we now have the house to ourselves."
        bree.say "It makes me feel like a wife from one of those silly, old-fashioned soap operas!"
    else:
        bree.say "Sasha never said as much out loud, but I think that we were cramping her style."
        bree.say "It's hard to be the spare wheel when the other people in the house do everything as a couple."
        bree.say "And when Poppy was born...well, that pretty much sealed the deal for her."
        bree.say "So she moved out a couple of months after the wedding and found a place of her own."
        bree.say "We still see her every now and again, though not as often as either of us would like."
        bree.say "But I can't hide the fact that part of me likes the fact we now have the house to ourselves."
        bree.say "I feel like we're a perfect little family unit!"
    bree.say "Is there much more to say than that?"
    bree.say "I mean, no one wants to be bored with details of what's happened to [hero.name] at work or me at uni, do they?"
    bree.say "It's like the way that you never see anyone use the toilet in a movie."
    bree.say "This is the part of the story where you want a montage of happy scenes, like snapshots of our lives, right?"
    bree.say "Well, how about a nice image of us, strolling through the park on a lovely summer day?"
    bree.say "That kind of sums it all up neatly, if you ask me."
    bree.say "We're smiling and laughing while the sun's beating down on us and times are good."
    bree.say "But if the sun goes behind the clouds or the rain starts to come down, then we can huddle together and smile at the memories we've made together."

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not bree.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_5
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_5
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label bree_anal_confession:
    $ bree.flags.anal = 2
    show bree normal
    "I would have just written it off as nothing more than a typically casual conversation with [bree.name], save for the fact that she really wasn't saying anything at all."
    "Some people have a habit of babbling like that, but with her, there's usually some kind of point that she gets to in the end."
    "But not today, as she seems to be flitting from one subject to another with no actual interest in what she's actually saying."
    show bree at center, zoomAt (1.5, (640, 1040)) with fade
    "In the end, I can't take it anymore and just want to hear what's really on her mind."
    mike.say "[bree.name], is there something that you wanted to say?"
    show bree evil
    bree.say "Ah, well...yeah, there kinda was."
    bree.say "It was about the other night..."
    show bree annoyed
    "This could be bad - but then what could be so bad that she have needed to wait all of this time to bring up?"
    mike.say "What about the other night?"
    show bree blush
    "[bree.name]'s blushing now and faltering as she tries to get her words out."
    mike.say "Did I do something that upset you, [bree.name]?"
    show bree surprised
    bree.say "No, no...I'm just...embarrassed to talk about it, that's all!"
    show bree annoyed
    "Now I think I understand where she's wanting to go with this."
    mike.say "I'm sorry that we ended up doing it that way, [bree.name]."

    show bree normal -blush
    "[bree.name] shakes her head, finally seeming to find the courage to explain herself completely."
    show bree talkative
    bree.say "Oh no, I'm not angry about it!"
    show bree evil blush
    bree.say "Just the opposite, really..."
    show bree flirt
    "She can hardly meet my eye as she admits this, her cheeks still burning with the shame it's making her feel."
    mike.say "You mean...you liked it when I took you up the ass?"
    show bree evil
    "[bree.name] bites her lip as she nods."
    bree.say "I...I liked it...a lot."
    show bree flirt
    "Wow - [bree.name] just found out that she's a dirty little girl, and that she loves it!"
    "Is it just me, or did it suddenly get hotter in here?"
    mike.say "So did I, [bree.name] - you were pretty amazing!"
    show bree stuned
    "She looks up at me, genuine surprise in her eyes at this unexpected praise."
    show bree surprised
    bree.say "I...I was?"
    show bree stuned
    "I'm not lying just for the sake of encouraging her, she really was!"
    mike.say "[bree.name], fucking your ass was incredible!"
    show bree flirt
    "She smiles at this, clearly loving the fact that I said so, but still feeling that she should be ashamed of herself for it."
    show bree hesitating
    bree.say "Would...would you like to...fuck my ass again some time?"
    show bree normal
    mike.say "[bree.name], it would be my pleasure!"
    "The look of satisfaction and excitement on [bree.name]'s face is enough to make me want to take a cold shower."
    "But the thought of what she just asked me to do is not something that's going to be washed away so easily."
    return

label bree_gone:
    $ bree.unhide()
    $ bree.flags.gone = False
    return

label bree_preg_test:
    scene bg bathroom
    "I walk into the bathroom groggily, my eyes still heavy from waking up only minutes ago."
    "Flicking the lightswitch, I squint at the bright light that reflects off of the ceramic tile."
    "I rub my face, trying to rid whatever tiredness I have left. I set some extra clothes I brought with me on the sink and turn on the shower."
    "It takes a minutes before it heats up, putting my hand under the water to check the temperature."
    "I step in, letting the heat run over my shoulders. Steam rises to the ceiling and fogs the mirror."
    "Once I manage to relax, the rest of the shower takes no time at all."
    "I don't want to get out, but I step onto the fuzzy rug anyway, grabbing a towel and wrapping it around my waist."
    "I take another towel from the rack and dry my hair."
    "When I'm done and as dry as I'll get myself I throw on my clothes for the day."
    "I go to brush my teeth, but find my toothbrush buried between hair products and other things I don't really recognize."
    "Ever since [bree.name] and Sasha moved in, I've been finding their stuff everywhere I look."
    "I don't completely mind, but when I can barely find my own things underneath, it starts to get annoying."
    "Once I spot my toothbrush, I make a move to grab it along with the paste."
    "As I pull back, my wrist hits a small container filled with some sort of lotion. I try to grab it as it falls, but I miss and I wince as it hits the floor."
    "I set my brush down and crouch to see where it landed. I can't find it."
    "Maybe it's behind the trash can? I push it aside and don't see it either. I'm about to stand back up, but see it inside the trash."
    mike.say "Shit."
    "I quickly take it out and set it back on the counter."
    "As I lift it, something catches my eye- a white stick poking out between a few tissues. Without thinking, I grab that too."
    "I inspect the stick closer. A pregnancy test? Who's was this?"
    "My brain immediately goes back to when I had sex with [bree.name]. This couldn't be...?"
    "I can hear my heartbeat in my ears, my anxiety shooting up."
    "If it was, then I had no idea what I would do. I flip the thing over to see the results. Two stripes."
    "How long has this been going on?"
    if not sasha.hidden:
        play sound door_knock
        pause 0.3
        with vpunch
        "I jump when I hear a knock on the bathroom door."
        sasha.say "Hey! How long are you going to be in there for?"
        mike.say "Uh- sorry!"
        "I call back to her and open the door."
        scene bg secondfloor
        show fx anger
        show sasha a towel annoyed
        "The cold air from the hallway hits me and makes me shiver."
        "I shove the test into my back pocket before she can see."
        "Her arms are crossed, looking annoyed."
        show sasha whining
        sasha.say "Are you done?"
        show sasha upset
        mike.say "Yup. Go ahead."
        show sasha normal at right4 with ease
        "She nods and pushes past me for her turn in the bathroom."
        show sasha stuned
        mike.say "Wait!"
        "She stops before closing the door. Sasha raises an eyebrow."
        mike.say "You haven't... taken a pregnancy test lately, have you?"
        show fx question at right4
        "No other way to really say it, but I have to know. Sasha stares at me, eyes full of suspicion."
        show sasha whining
        sasha.say "No. Why?"
        show sasha upset
        mike.say "Just asking."
    $ bree.flags.pregtest = 1
    return

label bree_preg_talk:
    if "Harem.together('bree', 'sasha', name='home')" and sasha.counters.pregnant >= 3 and bree.room == sasha.room:
        call home_harem_preg_talk from _call_home_harem_preg_talk
    else:
        show bree cry
        mike.say "[bree.name]?"
        "Her blonde hair whips around as she turns to look behind her."
        "Her eyes are rimmed red, her cheeks wet with tears."
        "She attempts to compose herself, but her smile falls as soon as she tries."
        show bree gloomy at center, zoomAt(1.5, (640, 1040))
        "I take a seat next to her, not knowing what to say."
        mike.say "What's wrong?"
        "I'm pretty sure I know what's wrong."
        bree.say "..."
        mike.say "I just... wanted to talk to you."
        show bree sad
        bree.say "I need to talk to you too."
        show bree gloomy
        "I nod, and start taking the pregnancy test out of my pocket."
        show bree sad
        bree.say "I- I... went to the pharmacy yesterday-"
        show bree gloomy
        "Before she can finish, I hand her the white stick."
        show bree stuned
        "She stares at it for a moment then bursts into tears."
        show bree cry blush
        bree.say "I'm so sorry."
        show bree gloomy
        menu:
            "You have nothing to be sorry about.":
                mike.say "You don't have anything to be sorry about."
                "[bree.name] slowly lifts her head."
                show bree surprised
                bree.say "You're not mad?"
                show bree stuned
                mike.say "Why would I be mad?"
                show bree sad
                if "bree_pregnant_request" in DONE:
                    bree.say "I don't know!"
                else:
                    bree.say "I don't know! Because we never talked about having kids."
                bree.say "I can barely afford rent and you need roommates."
                bree.say "We're not even married!"
                show bree gloomy
                mike.say "..."
                "She has a point. We're not exactly prepared for a baby."
                mike.say "That doesn't mean we can't try."
                show bree surprised
                bree.say "... For real?"
                show bree stuned
                mike.say "Yeah."
                show bree happy at center, traveling(2.5, 0.5, (640, 1640))
                "Her eyes start to well up again. She lunges forward and pulls me into a hug and I hug her back, squeezing her tightly."
                "Going through with this would be a struggle, but it would be worth it if I could do it with her."
            "You should have told me.":
                $ bree.love -= 25
                mike.say "Why the hell wouldn't you tell me right away?!"
                "[bree.name] winces as I raise my voice, but I can't help the irritation that rises in my chest."
                show bree sad
                bree.say "I'm sorry."
                show bree gloomy
                mike.say "This isn't something you just keep to yourself!"
                show bree sad
                bree.say "I wasn't going to! I was going to tell you."
                show bree gloomy
                mike.say "When?!"
                show bree sad
                bree.say "I don't know! When I was ready!"
                show bree a angry blush
                "Her face is turning red, the color crawling down her neck."
                show bree a vangry
                bree.say "You can't just like yell at me for this!"
                show bree a angry
                menu:
                    "I'm sorry.":
                        "I purse my lips and force myself to calm down. She was right. I may be upset, but I can't really imagine how she must be feeling."
                        mike.say "You're right. I'm sorry, [bree.name]."
                        show bree annoyed -blush
                        "She takes a breath and her shoulders relax."
                        show bree sad
                        bree.say "It's okay."
                        show bree sadsmile
                        "Silence stretches between us for a long minute."
                        show bree talkative
                        bree.say "Are we good?"
                        show bree sadsmile
                        mike.say "Sure."
                    "I'll do what I want.":
                        "No. This is ridiculous. How could she just keep this to herself?"
                        mike.say "You have to tell me when these things happen!"
                        show bree vangry
                        bree.say "I don't have to tell you anything!"
                        show bree angry
                        "Her face gets red, but I can tell it's from anger. She's more upset than I've ever seen her."
                        mike.say "[bree.name]-"
                        show bree vangry
                        bree.say "Shut up!"
                        bree.say "I'm leaving."
                        show bree angry
                        mike.say "What?!"
                        show bree angry blush at center, traveling(1.0, 0.3, (640, 720))
                        bree.say "I said I'm going! Leave me alone!"
                        hide bree with easeoutleft
                        "With that she stomps off angrily."
                        $ bree.love -= 50
        $ bree.flags.pregtest = 2
    return

label bree_event_bowsette:
    scene bg secondfloor
    bree.say "Hey, [hero.name]..."
    "The voice comes from [bree.name]'s room, but sounds off somehow."
    mike.say "[bree.name]?"
    bree.say "Um, can you come in please?"
    "It's definitely [bree.name], but it sounds as though she's trying to sound gruff for some reason."
    "Curious, I drop what I was doing and enter the room."
    scene bg black with dissolve
    pause 0.1
    scene bg bedroom2
    show bree bowsette talkative at center, zoomAt(1, (640, 720))
    with wiperight
    bree.say "So, What do you think?"
    show bree bowsette flirt
    "She's dressed in cosplay consisting of horns, a cute little crown, cuffs and a long, green tail."
    "Are those... spiked false teeth as well?"
    "I recognise the character near instantly and can't help but grin at the sight."
    show bree bowsette talkative at startle(0.1, 5)
    "[bree.name] blushes, struggling to make eye contact, but when I don't say anything she takes a moment to resolve herself, and speaks."
    bree.say "You dare enter the realm of the king of the Koopas?"
    show bree bowsette happy
    "The gruff voice is back, heavier now, and she strikes a pose, baring her 'claws'. Black fake nails in reality of course."
    mike.say "[bree.name], what are you doing?"
    "With a giggle, seemingly brought on by the drop in tension, [bree.name] drops the pose and scratches the back of her head awkwardly."
    show bree bowsette talkative at startle(0.1, 5)
    bree.say "I heard you talking about Bowsette the other day, I thought you'd like it..."
    show bree bowsette flirt
    mike.say "You did this for me?"
    show bree bowsette talkative at startle(0.1, 5)
    bree.say "Well, Yeah, I thought you might think it was cute?"
    show bree bowsette flirt
    "She seems to be fishing for something, but I don't mind. After the effort that clearly went into the costume she deserves the praise."
    mike.say "[bree.name], it's adorable."
    if bree.sexperience:
        show fx heart
        show bree bowsette blush at startle(0.1, 5)
        bree.say "I'm so glad you think so!"
        "My approval seems to have raised her spirits, her smile covers most of her face by now."

        scene bg bedroom2 at dark, blur(5)
        show bree bowsette blush at center, zoomAt(1.25, (640, 940)), top_to_bottom
        "I take a step closer and lean in, inspecting the costume closely."
        mike.say "This is really well made you know, you've got some real talent."
        "I can't see her face, but I'm positive how close my face is to her neck is embarrassing her as I look at the collar."
        bree.say "You really think so?"
        show bree bowsette blush at center, zoomAt(1.25, (640, 940)), bottom_to_top
        mike.say "Oh yeah, I'll try not to ruin it as I rip it off you."
        bree.say "Wa-"
        "Before she has a chance to object, or even question me, I push myself into her, latching my lips around her neck and littering it with kisses."
        "She stumbles backwards but I stay latched on, pressing her against the wall as she tries to catch her breath."
        "I wait for her to object, but instead I'm rewarded by a quiet little moan, as cute as it is arousing."
        "I pull my head back, but keep pressed against her, staring into her eyes as my hands travel further down her costume, fumbling with but eventually unhooking her skirt."
        "As it falls to the floor with a barely audible thump, she gives the slightest of nods, encouraging me to proceed, but I have something better in mind."
        mike.say "Aren't you going to stop me, oh big strong king?"
        bree.say "N-no fair!"
        "She whines, closing her eyes as my now free hands begin groping her through the skintight latex."
        "There's a moment of silence but it seems she got what I was hinting at as she forces herself to speak again in the cute, gruff voice she put on."
        bree.say "I-I'll have to endure it until I can return to normal!"
        mike.say "Well I hope that never happens, you're way hotter now, {i}Queen{/i} Koopa."
        scene bg bedroom2
        show bree bowsette naked
        "I hear another gasp as one of my hands begins rubbing her front through the suit, massaging her with just a single finger."
        mike.say "Come on Bowsette, let's draw you out of your shell."
        show bree bowsette naked
        "The hand groping her ass began under her suit, making more direct contact now, and discovering an interesting secret about the outfit."
        mike.say "Oh, so you aren't wearing anything under here?"
        bree.say "O-of course not, it would have ruined the outfit."
        mike.say "I'd have thought you'd at least have had a belt for the tail. I'm surprised they make butt plugs like this, more so that you own one."
        "I catch her eyes widen, then shut tight. I continue fondling her as I lean in closer, practically touching her ear."
        mike.say "So what do you say, does the queen want her knight to finish the job?"
        "I'm not even sure what Bowser's knight would be, those skeleton Koopa troopers? Bah, semantics."
        bree.say "Y-Yes. Your queen commands you?"
        "She seems to be struggling to keep up the persona, she wasn't great at it to begin with to be honest, but that just made the whole thing cuter."
        "Her voice is shaky and she keeps gasping for air as I press down harder on her slit, doing it sporadically enough she can never quite prepare herself."
        "I grasp her waist, mostly to steady her as I fear without the wall or myself she'd simply topple over with how weak her knees seem, then toss her onto the bed."
        show bree missionary bowsette bedroom2 with fade
        "She lands softly enough, rolling over once, then looking up to me with a mixture of fear, anticipation, and arousal in her eyes."
        mike.say "Anything for my queen."
        "I step closer as she shuffles in place, preparing for my arrival, slowly spreading her legs wide."
        "I watch her and she watches me. I revel in her submission for a moment, before unzipping my pants, my cock springing out into the open air, already fully erect."
        "I spot her breath catch in her throat, and gaze drop to my member."
        bree.say "I didn't know you'd like it this much."
        mike.say "Let me show you just how much I enjoy it."
        show bree missionary bowsette bedroom2
        "I let her lie in anticipation as I remove the rest of my clothes, feeling her prying eyes the entire time."
        mike.say "Ready, my queen?"
        bree.say "C-Come, Sir knight, I'm tired of waiting..."
        show bree missionary bowsette bedroom2 vaginal
        "I clamber onto the bed, just as tired of the build up as her, almost ripping her costume as I grabbed the thin strip covering her pussy and tore it to the side."
        "Now, with nothing in my way, I eagerly plunge my rod into her waiting hole, it being already soaking wet."
        "I'm well acquainted with [bree.name]'s body by now, and the roleplay only makes things even more exciting, even if she's not the best at it."
        "The effort she's putting in despite how hard it is for her is why it's so special."
        show bree missionary bowsette bedroom2 vaginal pleasure
        bree.say "Ahh,! Ahh,! I-, Ahh!"
        "Her moans fill the room, that and the sound of my crotch slapping against hers."
        "One of her hands reaches up for her crown as a particularly rough thrust on my part almost knocks it off her head."
        "I build up my speed as a reward for her devotion to the outfit."
        mike.say "How are you enjoying my pipe, Bowsette?!"
        "I know the puns are awful but I get a weird sort of sick glee out of them nevertheless."
        bree.say "S-So good! Y-you're a l-loyal knight!"
        mike.say "You make a better slut than a queen!"
        bree.say "Ah! Y-Yes [hero.name]! I-I'm a slutty turtle!"
        mike.say "Cum for me, you slut!"
        show bree missionary bowsette bedroom2 vaginal creampie arm ahegao
        "I reach over and grasp her horns, not sure how they're attached still, but they give me the leverage to give her several last, powerful thrusts."
        with hpunch
        "I feel her convulse, I watch her body shake and eyes roll backwards as her pussy clamps around my cock almost painfully tight."
        with hpunch
        "The sight and sensation drives me over the edge in return, gleefully pumping my seed inside her as she makes her final attempts to milk me dry."
        show bree missionary bowsette bedroom2 -vaginal ahegao with hpunch
        "Ecstasy overcomes us as our respective orgasms begin dying down, leaving me to collapse onto the bed beside her."
        hide bree
        show bree missionary bowsette bedroom2 normal
        "Exhausted, we each lay there for a few moments, panting and letting the sweat clinging to our bodies dissipate."
        "Eventually, I speak."
        mike.say "You need to dress up more often now, you know."
        "My eyes are closed, but I hear her laugh, then feel her lips delicately plant a kiss on my cheek."
        bree.say "I don't know, You really did a number on this suit, [hero.name]..."
        "I grin, but don't say more, and neither does she. We both just enjoy the moment, laid beside each other, still bathing in the afterglow of sex."
        "I don't exactly know how much time passes, but inevitably I'm reminded that a world exists outside of the room, and I should get out of bed."
        "[bree.name] seems almost disappointed when I look back over to her, but when she realises I'm staring she forces a grin."
        bree.say "I'll um, like, see if you actually ripped this and get to fixing it, I guess."
        mike.say "Heh, sounds like a plan. Can't wait to see what you dress up as next."
        "I lean over and place a kiss on her lips, which she reciprocates in kind."
        "Then, we each say our farewells and, after getting dressed of course, I'm on my way."
        $ bree.sexperience += 1
    else:
        show fx heart
        show bree bowsette happy blush
        bree.say "I'm really glad you like it!"
        "Her spirits seem to have been raised, although embarrassed she can't help but grin at me in return."
        show bree talkative
        bree.say "I want to take some photos before I take it off though, it took like, an hour to put on, so shoo!"
        "I raise my hands in mock surrender as she hurries me out of the room, flashing me a quick, but awkward, thumbs up before closing the door behind me."
        if bree.love >= 50:
            "I pause outside the door for a brief moment, before shouting back to her."
            mike.say "Next time, I'll be taking it off you!"
            "I almost regret not seeing her reaction, but I don't push it, I don't want to embarrass her too much."

    hide bree
    return

label bree_event_01:
    if bree.love.max < 40:
        $ bree.love.max = 40
    "I felt a small nagging sensation in the back of my mind telling me that something was wrong."
    "I quickly pat down my pockets."
    "As expected, most are filled to the brim with miscellaneous objects."
    "I heard the crinkle of old candy wrappers, and felt the familiar bulge of my wallet."
    "My keys poke through the fabric of my jeans and traced my palm and yet..."
    "No matter how long I spent searching my person, my phone was nowhere to be found."
    "These days, I did my best not to leave the house without it, even if only to pass the time browsing social media or whatever articles caught my eye during a dull moment."
    "Besides, finding it shouldn't be a monumental undertaking, I even had a vague recollection of leaving it on my nightstand."
    scene bg bedroom1 with fade
    "However, my memories quickly proved to be false."
    "My phone was absent from my nightstand, or my bedroom as a whole in fact."
    "I threw my sheets around, dug under my mattress, and evicted all of my various knick knacks from their rightful homes on display as I searched, but to no avail."
    "With my room a mess, and running considerably late already, I found myself frowning at the combination of stupidity on my part, and simple bad luck."
    "However, knowing that my phone must be in the house somewhere, I made my way back to the living room."
    scene bg livingroom with fade
    "The mess I created could be cleaned up another time, at the moment I had more pressing matters to deal with."
    "It was a problem for future [hero.name] to deal with."
    "Considering they were the two places in the house that I spent the most time, if my phone was nowhere to be found in the living room too, I'd have to ask someone to call me."
    "But, without a phone to do that, and with both Sasha and [bree.name] out of the house, I'd have to go outside and track down someone I knew."
    "This was such a pain..."
    "However, as I stepped into the room to begin searching, a face I hadn't expected greeted me from the couch."
    show bree phone 1 with fade
    "Or rather... Didn't greet me."
    "[bree.name] seems absorbed in some sort of handheld game, despite probably having only just sat down."
    "The two black earbuds in her ears were blasting the sounds of carnage loud enough for me to hear, and no doubt masking all sounds of my approach."
    "I must have been mistaken in assuming [bree.name] had been out of the house."
    "Upon initial meeting, I'd gotten the impression that [bree.name] would be the outgoing type, so when I heard no sounds coming from behind her door as I left, I'd assumed I'd been home alone."
    "Although, now that I thought about it, I don't think I've seen [bree.name] leave her room much since moving in."
    "It seemed like that cheerful and bubbly exterior hid quite the introvert."
    "Not that it mattered at the moment though, since my contemplation about the strange roommate I'd found myself with reminded me of the long and tiresome time I'd spent with her luggage."
    "As a result, [bree.name] still owed me a favor, and considering I was currently in need of help, I could think of no better time to cash it in."
    "I walked to her side and paused, glancing over her shoulder, yet she seemed too distracted by the on screen brawl to notice."
    "It was only when I tapped her shoulder did I get a reaction, and a rather explosive one at that."
    show bree phone 2 with vpunch
    bree.say "AHHHHHHHHHH!"
    "[bree.name] let out an ear piercingly loud yelp as she threw her hands into the air, almost sending her game flying across the room."
    "Fortunately for her, the vice like grip with which she held it kept the device firmly in place."
    "The sudden rather exaggerated reaction however, startled me in return, as I leapt backwards on instinct."
    "It took a moment or two for us each to calm down, during which [bree.name] slipped her headphones from their rightful place and scanned me."
    scene bg livingroom
    show bree a surprised sleep at center, zoomAt(1.25, (640, 940))
    show fx exclamation
    bree.say "You scared me!"
    show bree stuned
    "I didn't need to be told that, but at the very least she didn't seem to be holding a grudge."
    show bree talkative
    bree.say "I thought you'd gone outside, I couldn't see your jacket by the door."
    show bree normal
    "With my assumption that the search would only take a minute or two, I hadn't bothered shrugging off my jacket."
    mike.say "Yeah, I forgot my phone and couldn't find it."
    menu:
        "Mind lending a hand?":
            $ bree.love += 5
            show bree annoyed
            bree.say "Uhhhh..."
            "[bree.name] seemed conflicted, her gaze slowly drifting back towards her game."
            show bree normal
            "But, just before she said no, a flash of something I couldn't quite place appeared in her eyes."
            show bree happy
            "A smile grew on her face as she began eagerly nodding."
            bree.say "Sure! Where'd you last see it?"
        "Help me look.":
            $ bree.sub += 5
            show bree surprised
            bree.say "Wow, you could at least say please."
            show bree annoyed
            mike.say "You owe me one after dragging your things inside."
            show bree talkative
            bree.say "I..."
            show bree stuned
            "Although she appeared visibly reluctant, a short pause followed before objecting, where their entire demeanor seemed to change."
            show bree normal
            "A smile grew in place of her frown as she began eagerly nodding."
            show bree talkative
            bree.say "Alright! You got me there, where did you last see it?"
    show bree normal
    mike.say "I thought it was in my room, but I can't find it anywhere."
    bree.say "Hmm..."
    show bree b evil
    "[bree.name] pauses for a moment as she thinks, adopting a rather cliche pose with her hand on her chin."
    "She holds it for long enough to make me doubt whether she's actually going to be of any help before suddenly dropping it."
    play sound woosh_punch
    show bree a normal at center, traveling(1.5, 0.3, (640, 1040))
    "In one swift movement, her hand disappears into the couch cushions, and just as quickly it returns with my phone within her fingers."
    show bree happy
    show fx exclamation
    bree.say "Tada!"
    show bree normal
    "She proudly shoved the phone in my direction, the grin on her face wide and sweet."
    mike.say "That was quick, thanks."
    "My fingers brush against hers as I take the phone, but she doesn't seem to mind."
    "Her skin is surprisingly soft."
    show bree smile
    bree.say "Yeah, couch cushions are like, magnets for things like that!"
    bree.say "I always lose my keys down the side of my bed these days."
    show bree normal
    "Although I had been in somewhat of a rush earlier, by now I've resigned myself to being late."
    mike.say "I try not to leave my stuff in my pockets so they don't get lost."
    "Despite now being roommates, I still know surprisingly little about [bree.name]."
    "I've picked up one or two things, but since moving in I haven't seen her much."
    mike.say "So, how're you doing? Like the house?"
    show bree happy
    bree.say "Oh yeah, it's like, really great! Way better than my old place."
    show bree normal
    mike.say "Where'd you live before here?"
    show bree a surprised
    bree.say "Before here? Uh..."
    show bree a annoyed
    "She seemed reluctant to answer."
    "I didn't want to make [bree.name] uncomfortable, so I quickly changed the topic."
    mike.say "So uh, what're you playing?"
    show bree normal
    "[bree.name] seemed almost instantaneously relieved as I yielded on my initial question."
    "There was even a small sparkle in her eyes that gave away the genuine joy she felt at my interest."
    show bree talkative
    bree.say "Oh! It's Motor Racer 2!"
    show bree normal
    mike.say "2? I thought there were five already."
    show bree happy
    bree.say "Well yeah, but the second was like, way better than any of the new ones."
    show bree normal
    mike.say "I don't think I've ever played any of the originals."
    show bree talkative
    bree.say "You should! I think the arcade has got some original machines, I keep meaning to go visit."
    show bree normal
    mike.say "So you play a lot of video games?"
    "Despite it being far from an unreasonable question to ask, it seemed to catch [bree.name] off guard."
    show bree stuned
    show fx exclamation
    "Her eyes shot wide open, almost as if in panic as she began to stumble over her words."
    show bree surprised
    bree.say "N-No! I mean... Yes? Uh..."
    bree.say "Maybe?"
    show bree annoyed blush
    "Although it can't have helped, I found myself chuckling against my will, sending a light blush spreading across [bree.name]'s cheeks."
    show bree talkative
    bree.say "H-Hey! Don't laugh!"
    show bree normal
    mike.say "Sorry! You just got all flustered really easily."
    mike.say "What's the big deal?"
    show bree talkative
    bree.say "It's embarrassing, you know?"
    bree.say "Liking video games is like, really nerdy and uncool!"
    show bree sadsmile -blush
    "Oh, thanks."
    mike.say "I play video games, you know?"
    show bree surprised
    bree.say "Oh! I-I didn't mean you were nerdy and uncool! I-"
    bree.say "Ahh!"
    show bree sadsmile
    "I found myself laughing again at [bree.name]'s plight, but I didn't want to make her embarrassment worse, no matter how amusing that may have been."
    mike.say "It's fine, I don't mind."
    "Besides, nerdy and uncool isn't really inaccurate."
    show bree normal
    "Either way, once more I witnessed relief washing over [bree.name] from my words, although she still seemed to feel somewhat awkward."
    "One thing I have noticed in my slim time with [bree.name] is that the woman is exceptionally easy to read."
    "She seemed to wear every emotion and thought proudly on her face, even if she didn't intend to."
    show bree happy
    bree.say "Oh good! I was worried I'd offended you!"
    show bree normal
    mike.say "Nah, I'm not that easy to hurt."
    mike.say "I don't think just liking games makes you nerdy though."
    "It's a rather childish way of viewing what should, and usually is, a harmless hobby."
    "Plus, she was acting like being nerdy was a bad thing."
    show bree talkative
    bree.say "Well, I guess not..."
    show bree normal
    "I could tell she wasn't convinced, even if she yielded the point."
    "She probably just doesn't want to have an argument over something so petty, which is at least a sentiment I can agree with."
    mike.say "Anyway, I should get going."
    mike.say "I'm already late as it is, thanks for finding my phone though."
    show bree happy
    bree.say "No problem! It was easy as pie!"
    show bree normal
    mike.say "You should go down to that arcade, by the way."
    "I found myself speaking without really thinking about it."
    show bree talkative
    bree.say "Oh! Uh... Sure! I'll go eventually, I've just been settling in."
    show bree sadsmile
    "Fortunately for me, [bree.name] also happened to be a terrible liar."
    "Whatever the reason, I got the impression that something else had been holding [bree.name] back."
    "Maybe it was her worrying about seeming 'uncool'."
    "Maybe it was just laziness."
    "It didn't really matter the reason, but lounging around the house all day couldn't be good for her."
    mike.say "Maybe we could go together then?"
    mike.say "I mean, you piqued my interest about Motor Racer now."
    show bree surprised
    bree.say "Oh! Uh... Sure!"
    show bree normal
    mike.say "Great, we can figure out a time later."
    show bree happy
    bree.say "Yeah! That'll be fun!"
    show bree sadsmile
    "I don't think even she believed herself."
    "She seemed oddly apprehensive about the situation, and gave the impression that she was doubting everything she said even as she said it."
    "There was something about [bree.name] as a whole that piqued my interest."
    "It wasn't as though I didn't trust her, but she didn't seem to trust herself."
    "Something just seemed off about her..."
    "If nothing else, this trip would help me get a better read on the girl."
    mike.say "But yeah, I really should get going, later [bree.name]."
    show bree talkative
    bree.say "Bye [hero.name]! See you later!"
    show bree normal
    "I ended up spending a lot of time chatting with [bree.name], longer than intended, but at least it wasn't time wasted."
    "I feel like we grew closer."
    "Not that that's saying much."
    "Anyway, I need to hurry now before I miss it entirely."
    hide bree
    return

label bree_event_02:
    if bree.love.max < 60:
        $ bree.love.max = 60
    show bree talkative at center, zoomAt (1.25, (640, 880))
    bree.say "Hey [hero.name]!"
    bree.say "What's wrong? You look annoyed."
    show bree normal
    "My discomfort must have been obvious, so I quickly feigned a smile."
    "It had been a shock when I'd stepped inside, but I was already starting to grow a little used to it."
    "Once I've started playing games and distracting myself, I should be fine."
    mike.say "Nothing, don't worry about it."
    show bree talkative
    bree.say "Wanna play some games?"
    show bree normal
    mike.say "Yeah sure."
    show bree happy
    bree.say "Hehe, I was supposed to have class today."
    show bree normal
    mike.say "Supposed to?"
    show bree stuned
    "I watched [bree.name]'s eyes widen as I questioned her, it must have been a slip of the tongue because she quickly tries to cover up her own admission."
    show bree talkative
    bree.say "Oh! Uh, it got called off, the professor was really sick or something."
    show bree normal
    "While [bree.name] was easy to read emotionally, so easy I'm already confident in that statement, I found myself unable to tell whether or not she's lying."
    "Not that it mattered of course, it's really none of my business."
    mike.say "Huh, lucky you then."
    show bree talkative
    bree.say "Yeah! So I came here and played some games~!"
    show bree normal
    "Uh oh, that means she's practiced."
    mike.say "Should I be worried...?"
    show bree talkative
    bree.say "Nope! I know you haven't played before, so I'll go easy on you!"
    show bree normal
    mike.say "Glad to hear it, don't think I've been in an arcade since I was a kid."
    show bree happy
    bree.say "Oh, I love these places!"
    bree.say "Everyone's just having so much fun, and there are so many games to play!"
    show bree normal
    mike.say "You seem pretty passionate."
    show bree happy
    bree.say "Hehe, yep!"
    show bree talkative
    bree.say "Back home there was only one arcade, and it was really small."
    bree.say "It's really cool to see one as big as this!"
    show bree normal
    mike.say "Huh, don't you think it's a little mu-"
    show bree talkative
    bree.say "AH! Quick!"
    show bree normal
    mike.say "Wait, wh-ah!"
    with hpunch
    "I'm cut short from my surprise as [bree.name]'s hand wraps around my arm unexpectedly and begins yanking me off in a seemingly random direction."
    show bree at center, zoomAt (1.25, (540, 880)) with ease
    "I let out a quiet yelp as my feet struggle to keep up, stumbling over each other as [bree.name] sprinted full force towards a target I had yet to see myself."
    "I narrowly dodge one or two innocent bystanders before we finally come to a stop in front of an empty machine."
    show bree talkative
    bree.say "People have been on it since I got here! This is the first time I've seen it free!"
    show bree normal
    "As she withdrew her hand from my sleeve, I take a moment to examine the cabinet before us."
    mike.say "Motor Racer ..."
    show bree talkative
    bree.say "Yeah! Just in time, huh?"
    bree.say "It seems really popular!"
    show bree normal
    "Hopefully, that was just a sign of how good it was."
    show bree talkative
    bree.say "I was going to practice, but I ended up spending all my time on a bunch of light gun games waiting."
    show bree normal
    mike.say "Hopefully you'll still be a little rusty then."
    show bree happy
    bree.say "Come on, I'm sure you'll do great!"
    show bree normal
    "Although skeptical, I simply nodded as she went to put a coin into the machine."
    "I took the opportunity to glance at the machine again, and get in position ready to play."
    hide bree
    show bree arcade 1
    with fade
    if not hero.has_skill("video_games"):
        "I was anything but optimistic about my chances, and as the coin fell into the machine and [bree.name] stood back up, I saw a focus and determination in her gaze that only worried me more."
        "I could tell instantly that I would get destroyed here, and began to dread the game ahead, but it was too late to back out now as the racing care select screen popped up."
        "[bree.name] wasted no time in selecting a red sports car."
        "It took a moment or two, but I found a car I recognised from when I'd played the more recent games."
        "When the actual gameplay started though, I found myself at a loss."
        "As if the altered control scheme wasn't bad enough, when I finally got used to it, I found out that all I remembered didn't work in this version."
        "If nothing else, [bree.name] did make an attempt to go easy on me, and I picked out one or two occasions where she deliberately slowed down."
        "But even as she restrained herself, I struggled to match her, and on the few occasions where I did win a lap or two, it was clearly mostly due to luck."
        "Despite all of this however, I actually found myself having a lot of fun."
        "[bree.name] kept things light and I've never been too sore a loser, by the time we finally stopped so someone else could use the machine I'd definitely come a long way skillswise too."
        "I couldn't tell if I was enjoying it because the game itself was good, or because I had good company."
        "Time flew either way, in fact we only stopped when we did because I noticed a few people lurking and watching over our shoulders."
        "[bree.name] seemed too absorbed in what was happening on screen to notice, and acted incredibly apologetic and flustered when she realised we were hogging the game."
        "The sheer focus she showed when we were playing however was not only impressive, but almost uncharacteristic of the almost ditzy girl I thought I'd known."
        "It seemed like there were a few sides to [bree.name] that I had yet to discover."
        "In any case, the two of us had probably played straight for an hour or so, so we decided to grab drinks before doing anything else."
        scene bg arcade
        show bree normal at center, zoomAt (1.25, (640, 880))
        with fade
        "We stood off to one side, sipping at cans of cola from a vending machine, watching the room as we engaged in idle chatter."
        mike.say "You were right, that game was good."
        show bree happy
        bree.say "Hehe, did you doubt me?"
        show bree normal
        mike.say "Not at all, you seem to know more about this stuff than me at least. Better at it too."
        show bree talkative
        bree.say "Are you sure you've never played that before? You were really good!"
        show bree normal
        "I'm 90%% sure that she's just saying that to make me feel better, but despite my doubt, it feels good to hear."
        mike.say "Heh, you still kicked my ass though."
        show bree talkative
        bree.say "Well I've got way more practice! You'll be good enough to beat me soon enough!"
        show bree normal
        mike.say "Don't think I didn't notice you going easy on me, [bree.name]."
        show bree talkative
        bree.say "Well you're new! It wouldn't be fair not to!"
        show bree normal
        mike.say "Yeah yeah, I know. Still, I'm curious what you're like when you're trying your best now."
        show bree happy
        bree.say "Hehe, get better and one day I'll show you~!"
        show bree normal
        mike.say "As much as I'd like to spend all day everyday in here, I can't afford it on my wage."
        "Once again, I find myself envying professional gamers."
        if "zbox_360" in hero.inventory:
            mike.say "I do have a Zbox at home, maybe we could play on it sometime."
        else:
            show bree talkative
            bree.say "If only we had a game system to play it back home!"
            bree.say "It would be so much fun!"
            show bree normal
            mike.say "Huh, maybe when I have more cash then."
        show bree happy
        show fx heart
        $ bree.love += 2
        bree.say "Hehe, yay!"
        "Fun games with a cute girl? What isn't to like."
        "Besides, it'd give me a chance to get to know [bree.name] a little more, which is an intriguing opportunity if nothing else."
    else:
        "I'd never played this game before, but as I rested my finger over the controls, I felt oddly confident."
        "Racing games weren't my best genre, but I was still damn good at them."
        "I watched the screen as the coin slid into the slot, [bree.name] quickly joining me at my side and mimicking my stance."
        "I glanced over at her as the race car select screen began booting, and saw a level of focus and determination in her gaze that almost worried me."
        "I knew she'd go easy as I got to grips with this specific game's odd quirks, but after that?"
        "There was still so much to [bree.name] that I considered a mystery that I wasn't sure."
        "I thought I'd at least gotten used to her general demeanor, but looking at her now, she didn't seem even remotely like the same person."
        "Just how many more sides to her would I discover?"
        "Before I had too much time to dwell however, the game started."
        "It quickly became clear to me that [bree.name] had intended to give me a few moments to get around the controls before getting serious, but the moment the game loaded I crushed the pedal and rushed past her."
        "I was simply fortunate that it worked, although [bree.name] was quite the opposite."
        "What followed was some of the most intense few games I'd ever played."
        "Although [bree.name] had managed to quickly turn the tables, I managed to catch back up just as quickly, and it became clear that we were evenly matched in basically all areas."
        "Every race came close, and some even drew with both of us going out of the road, or hitting each other's cars so perfectly in sync that both our car slowed."
        "We stayed mostly silent as we played, focusing with all our might, and it was only during a brief respite where we had to put in more coins that I noticed a few people watching our game from afar."
        "By the time we did finally stop, I could feel my heart racing from the session, having gotten quickly pumped up during the duel."
        "Glancing across to [bree.name], she seemed to feel the same, and wore a wide grin on her face as we made eye contact."
        scene bg arcade
        show bree annoyed at center, zoomAt (1.25, (640, 880))
        with fade
        "When she spotted the small group that had formed to watch however, she quickly became flustered and seemed eager to make her retreat, so we darted away to get drinks."
        show bree talkative
        bree.say "You told me you hadn't played it before!"
        show bree normal
        mike.say "I haven't, it was just similar enough to the ones I have to pick up quickly."
        show bree talkative
        bree.say "You were so good!"
        show bree normal
        mike.say "Hey, I'm pretty sure you won more than me."
        show bree talkative
        bree.say "No way! You did like, so good!"
        show bree normal
        mike.say "I guess next time we'll have to keep track."
        show bree talkative
        bree.say "Totally! We'll definitely come back again soon!"
        show bree normal
        mike.say "I'd love to, but this session's already cost more than I expected."
        show bree talkative
        bree.say "If only we had a game system to play it back home!"
        bree.say "It would be so much fun!"
        show bree normal
        mike.say "Huh, maybe when I have more cash then."
        scene bg arcade
        $ bree.love += 2
        show fx heart
        show bree happy at center, zoomAt (1.25, (640, 880))
        bree.say "Yay!"
        show bree normal
        "She seems almost relieved that I said maybe, was she nervous?"
        "If anything, I'm the one that should be nervous."
        "Still, this opportunity is too good to pass up. Fun games with a cute girl, plus it'll give me a chance to learn more about [bree.name]."
    show bree talkative
    bree.say "I was worried about making friends when I moved here, but I already have one!"
    show bree normal
    mike.say "You were worried? Why?"
    show bree stuned
    "From the surprised expression on [bree.name]'s face, I once more get the impression that my question caught her off guard."
    "It's almost as if any time she tells me something about herself, she does so by accident."
    show bree surprised
    bree.say "Oh! Uh, it's just weird, you know? Moving into a new place, it's like, really nerve wracking."
    show bree sadsmile
    mike.say "Makes sense I guess."
    mike.say "No idea why you'd be nervous though, you're one of the nicest people I've met in a while."
    show bree flirt
    "Once more, I seem to have caught her off guard, as her eyes widen and a blush starts to form on her cheeks."
    show bree talkative blush
    bree.say "Oh! Um, thank you [hero.name]! I like, think you're really nice too!"
    show bree normal
    "Granted, with my luck with people that wasn't much of a claim on my part, but I didn't need to tell her that part."
    mike.say "Heh, thanks. So uh, day's still young, wanna go play something else?"
    show bree talkative
    bree.say "Definitely! Anything catches your eye?"
    show bree normal
    mike.say "Uh... You said you were playing those light gun games, right?"
    show bree talkative
    bree.say "Yeah! They're so fun! Some of the guns even have inbuilt recoil so it simulates actually firing one!"
    bree.say "I mean, obviously it's way weaker than an actual gun, but it's still cool!"
    show bree normal
    mike.say "Heh, sounds good to me."
    show bree happy -blush
    bree.say "Yay~!"
    hide bree with dissolve
    "With very little in terms of warning, [bree.name] turned and began darting off in a seemingly random direction, tossing her can over her shoulder on the way for it to land in one of many trash cans set up near where we stood."
    "Although I'm relieved that she didn't grab me this time, I find myself stumbling over my own feet as I begin rushing to catch up with her, caught entirely off guard."
    "Fortunately for me, she didn't go far, and before long we were using up the last of our change blasting away robots and aliens and all other manner of things on the screen in front of us."
    "Once again, [bree.name] was entirely right, and the game is a lot of fun."
    if hero.has_skill("video_games"):
        "Neither of us is quite as good at it, but between us we actually manage to finish one or two."
        "We seem to make a pretty good team, and covered each other quite well."
    else:
        "The games are surprisingly difficult however, and although we end up putting up a good fight, we don't get all that far in any of the games we try."
    show bree normal at center, zoomAt (1.25, (640, 880)) with fade
    "But predictably, our pockets became lighter with every passing minute and before long we were heading for the door once again."
    mike.say "That was pretty fun."
    show bree happy
    bree.say "I know, right? I love trips to the arcade!"
    show bree normal
    mike.say "If only it didn't cost so much."
    show bree happy
    bree.say "Hehe, I know right?"
    show bree talkative
    bree.say "I need to, like, get a job or something."
    show bree normal
    "Once again, the question of where their rent is coming from pops into my mind, but I don't want to pry too much."
    mike.say "Would you even have time to work with school?"
    mike.say "And even if you do get a part time job, won't be much time left for games then."
    show bree talkative
    bree.say "Ahh! Good point! Maybe I'll just stay home then~!"
    show bree normal
    mike.say "You should try to get out sometime, though."
    show bree talkative
    bree.say "Well, that's what I have school for!"
    show bree normal
    "That isn't really what school is for at all."
    mike.say "I guess so."
    mike.say "So uh, which game was your favorite?"
    show bree happy
    bree.say "Oh! I really liked..."
    "We continued to chat for a while as we walked, heading home together."
    show bg livingroom with fade
    "Time flew as we discussed a few unimportant things, and before long we were stepping back inside our house."
    hide bree with easeoutright
    "After a brief goodbye, [bree.name] predictably ducked back into her room."
    "I'm glad she seemed to enjoy herself, especially considering her reluctance to come in the first place."
    "Now I just have to make time to play a few more rounds with her sometime."
    $ game.room = "livingroom"
    return

label bree_event_03:
    if bree.love.max < 80:
        $ bree.love.max = 80
    "As expected, after visiting the arcade with [bree.name] not much changed."
    "I was loitering, lounging on our sofa idly checking my phone."
    "More than anything else, I was letting my mind wander, not taking in any of the seemingly endless information the screen presented to me."
    "My thumb flicked past a sea of articles and supposedly humorous images, before the sound of approaching footsteps knocked me out of my trance."
    show bree evil at right with easeinright
    "I glanced upwards to see [bree.name] emerge from the hallway connecting to her room, checking her own phone, although she seemed much more engaged with whatever was happening on her screen than I was mine."
    show bree at center with ease
    "So much so in fact, that she didn't notice me as I gave a short wave in her direction, leading me to open my mouth."
    mike.say "Hey [bree.name]."
    show bree at left5 with ease
    "Somewhat predictably, the sudden sound startled [bree.name], much like it had the last time I interrupted her focus when I saw her playing Alley Brawler for the first time."
    show bree stuned at vshake
    "And, much like that time, her jumping metaphorically out of her skin caused her hand to slip and almost drop the device it was holding."
    show bree surprised
    show fx exclamation at left5
    bree.say "Oh! Hi [hero.name]! I didn't like, see you there!"
    show bree normal
    "I quickly covered up my smirk as she turned to me, hiding my amusement at her plight."
    mike.say "Yeah, you seemed pretty absorbed in your phone. What're you reading?"
    show bree happy
    bree.say "Oh yeah! Details on the next Motor Racer just got leaked!"
    show bree normal
    mike.say "Woah, really? Anything interesting?"
    show bree smile
    bree.say "A whole buncha cool new stuff! Here, take a look!"
    show bree normal at center, zoomAt(1.5, (640, 1040)), vshake
    "Quickly rushing to my side, taking a seat next to me, [bree.name] eagerly shoved her device in my face."
    "I take it with much less enthusiasm, although I am curious, it would just be impossible to match [bree.name]'s seeming enthusiasm with every little thing she sees."
    "There's a lot to take in, so I just briefly skim the list, and pick out a few of the more noteworthy parts."
    mike.say "New drift system...?"
    show bree talkative
    bree.say "Yeah! The leak was really vague so everyone online is theorising what it might mean!"
    show bree normal
    mike.say "Sounds like it could end badly, the games feel pretty intuitive as is."
    show bree talkative
    bree.say "Maybe, but at least they're trying something different!"
    show bree normal
    mike.say "I guess so, just hope it doesn't ruin the whole thing."
    show bree happy
    bree.say "Oh come on, it'll be like, really fun anyway!"
    show bree normal
    mike.say "Hey, if you say so."
    hide bree
    show bree normal
    "With a giggle, [bree.name] takes her phone back off me, shoving it back into her pocket as she lept back off the couch and began towards the refrigerator."
    show bree talkative
    bree.say "I was just grabbing a drink, want one?"
    show bree normal
    mike.say "Sure, grab me a cola?"
    hide bree with easeoutright
    "All the talk of Motor Racer has yet again reminded me of the deal I made with [bree.name]."
    "Feeling an itch to play it once again, and seeing no reason not to hazard asking, once [bree.name] returns with our drinks I bring it up."
    show bree at center, zoomAt(1.5, (640, 1040)) with easeinright
    mike.say "You free for a while?"
    show bree talkative
    bree.say "Always! What's up?"
    show bree normal
    mike.say "Wanna play something?"
    show bree smile
    "I catch her usual wide grin spread just a little further on her cheeks."
    "I was satisfied as a result, that her answer would be a yes, even before she began eagerly nodding towards me."
    show bree talkative
    bree.say "Yeah! That'd be great! Come on! Let's get my copy of Motor Racer and we can play on the Zwitch!"
    hide bree with easeoutright
    "Once again, I find myself rushing after [bree.name] to keep up, thankful that my can is still closed for the time being or I'd be spilling my drink everywhere."
    scene bg secondfloor with fade
    "I make a note to keep it closed for a few moments after arriving in her room, out of fear of having the contents explode all over me."
    "It was when I reached her door and stepped inside that I realised just how little I'd gotten used to the idea of living with [bree.name] and Sasha."
    "I was getting along with them well enough, sure, but the sight of [bree.name]'s room instead of Samantha's room?"
    "It not only gave me pause, but outright shocked me."
    scene bg bedroom2 with fade
    "It was silly, I knew that, of course [bree.name] wouldn't just be sleeping on the floor amidst a few weights and a couple of exercise machines."
    "In a few ways, [bree.name] and Samantha were quite similar I suppose, so maybe it wouldn't have been as bad if I was used to it still being a bedroom."
    "And Samantha ended up abandoning her room for his not long after they started dating anyway..."
    "It was just odd is all. Having the change sprung on me so suddenly meant I hadn't properly processed it, I suppose."
    "It was like being thrust into the reality of the situation in an instant."
    "I must have been wearing my shock visibly however, as [bree.name] quickly caught it."
    show bree surprised at center, zoomAt(1.5, (640, 1040)) with dissolve
    bree.say "What's wrong, [hero.name]? I know it's a little dirty, I'm sorry!"
    show bree sad
    bree.say "I kept meaning to clean it but then I got distracted by the leak and-"
    show bree stuned
    mike.say "Don't worry about it, [bree.name]. Mine's way worse."
    show bree normal
    "I manage a chuckle, and pushed away the thoughts about my old crush as I took a couple of steps inside, swinging the door closed behind me."
    "[bree.name]'s room itself isn't all that surprising, if anything it was almost bland."
    "The walls were the same colors they'd always been of course, and what furniture she did have I'd already seen when I helped her bring in her things."
    "Well, aside from the larger items, which she had delivered soon after of course."
    "If [bree.name] had tried to make me drag her entire bed to her room for her I don't think I'd have given in as easily as I had."
    "I was reluctant enough with the boxes I did transport."
    "It gave me a chance to be a little nosey however, invasive perhaps."
    "The contents of each box were written on the outside in big black marker, so it wasn't like I was taking a peek inside the boxes."
    "Besides, there wasn't anything that juicy anyway, most of the boxes were just clothes or games."
    "While she had plenty for me to help with, that seemed to be all she had, everything she owned she'd brought then and there."
    "In a way, that could be seen as quite sad, at the same time it made me realise how much she needed this place."
    "I didn't have answers yet, who knew if I'd ever get them?"
    hide bree with easeoutright
    "At the moment, the more pressing matter was preparing myself, as [bree.name] had already found the box she was looking for and was rushing to get back down to the livingroom."
    scene bg livingroom
    show bree at center, zoomAt(1.5, (640, 1040))
    with fade
    "She grabbed her Zwitch, hand over mine, took Motor Racer 4 out of its box, and rammed it into the gaming system."
    "The graphics looked a little odd on such a small screen, but I didn't let that distract me as I took the device I was handed, and chose the same car I'd played as last time."
    hide bree
    show bree switch
    with fade
    "A quick glance confirmed my suspicions, with [bree.name] focusing intensely on the screen already like she tended to do when playing, it seemed."
    "I could sense she wasn't going to make it easy, and already knew first hand how good she was at this game."
    "At least this time it was free."
    "..."
    "Around an hour or so passed of race after race of back and forth."
    "I find myself more at home using a controller, I was more used to it than the layout they had back at the arcade after all."
    "Unfortunately for me, the same seemed to go for [bree.name], who'd obviously been playing this way regularly, making what little boost in my own skill meaningless."
    "As predicted, time flies and we barely exchange glances or converse as we play, what few comments we exchange being exclamations about how well the other has performed."
    "I'm not entirely sure if I can blame my enjoyment on the game anymore, it isn't exactly easy to grip me so hard so quickly."
    "In fact, I was beginning to suspect that [bree.name]'s participation alongside me is what made these sessions so engaging."
    "Whether or not she's going easy on me is irrelevant anymore, there's simply a constant back and forth between us that keeps it interesting."
    bree.say "That one was close!"
    "She wasn't wrong, I'd come out on top but only by a short length."
    "I'm not too proud to admit luck was a large factor in my victory."
    mike.say "Yeah, you almost had me."
    if hero.has_skill("video_games"):
        show bree switch breelose
        bree.say "I think you're starting to really get the edge on me!"
        mike.say "Nah, we're still pretty neck and neck."
        bree.say "No, really! You're so good!"
    else:
        show bree switch mikelose
        bree.say "You're definitely getting better!"
        mike.say "Heh, maybe soon you won't have to go so easy on me."
        bree.say "Definitely!"
    play sound cell_vibrate loop
    "I see [bree.name] open her mouth to say more, but before words come out she's interrupted by a low buzzing."
    "It took a moment for me to identify the source as a phone vibrating, and a quick check told me it wasn't mine."
    "I turned to mention it to [bree.name], but she's way ahead of me, already checking her phone curiously."
    stop sound
    hide bree
    show bree talkative at center, zoomAt(1.5, (640, 1040))
    bree.say "Ah! Sorry [hero.name]! I have to take this!"
    show bree normal
    mike.say "No problem, take your time."
    show bree wink
    bree.say "Thanks! I won't be long, promise!"
    show bree normal
    "With a grin and a wave, [bree.name] rushed for the exit."
    hide bree with easeoutright
    "I caught a brief glimpse of her holding the phone to her ear before her hand grasped the handle and my view was obstructed by the door."
    "The upbeat music of the game wafted through the room to save me from sitting in silence, although just doing nothing was still quickly growing incredibly awkward."
    "It didn't take a genius to realise that, at the end of the day, there was only one real option in this situation."
    "I quickly skimmed through the content of the box, looking at the various games in it."
    "Next to a few fighting games there was a few country CDs."
    "Unlike everything else I'd found, this one surprised me."
    "I picked a CD at random and took it out of the box."
    "The cover depicted a man in one of the most stereotypical country outfits I'd ever seen, complete with big leather boots and cowboy hat."
    "In fact, cowboy was quite accurate to describe what he seemed to be going for."
    "The man was even sitting on a large bail of hay with an acoustic guitar on his lap, smiling at the camera with a farm in the background."
    "It was as if someone designed the cover for the sole purpose of screaming 'Country' as loud as possible."
    show bree at center, zoomAt(1.5, (640, 1040)) with easeinright
    "Unfortunately for me, however, it was at this exact moment that the door opposite me swung open and [bree.name] reappeared in the room."
    show bree talkative
    bree.say "I'm really sorry that took so long, [hero.name]! I was just-"
    show fx exclamation
    show bree stuned
    "She cuts herself short as she spots me staring at her, CD in hand."
    "I feel like a deer in the headlights, although it wasn't like the item we paused over was hidden in anyway."
    show bree blush
    "Before I could react however, [bree.name]'s cheeks began to flush as she leapt at me, yanking the CD out of my hand."
    "For a moment, I thought she might be mad, but fortunately for me [bree.name] quickly proved that that wasn't the case."
    show bree surprised at startle
    bree.say "Ah! Don't look at that, I don't like country music!"
    show bree gloomy
    mike.say "Then uh, why do you have a bunch of country CDs?"
    show bree sadsmile
    "Another obvious question that seemed to catch [bree.name] entirely off guard, as she quickly began tripping over her own words and the blush on her cheeks simply grew thicker."
    show bree sad
    bree.say "Uh... OK, fine, I like country music..."
    show bree sadsmile
    menu:
        "Tease her":
            mike.say "Country music, really?"
            show bree talkative
            bree.say "Yeah..."
            show bree normal
            "[bree.name]'s cute normally, but when she's embarrassed that's doubly so."
            mike.say "Wow, and I thought you had good taste. Country music? That's like, bottom of the barrel stuff."
            show bree talkative
            bree.say "H-hey! It's not that bad..."
            show bree normal
            mike.say "Whatever you say now I know Motor Racer is a fluke though, I'll just have to make sure to avoid anything you recommend in the future."
            show bree annoyed
            "Although I'm clearly not serious, [bree.name] seemed to be growing uncomfortable, so I quickly dropped the act."
            mike.say "Hey, I'm kidding."
            "With a light flick of the wrist, I toss the CD towards [bree.name], who scrambles to catch it before it hits the floor."
            mike.say "I don't care what you listen to."
            show bree surprised
            bree.say "Oh wow, you really had me going then!"
            show bree normal
            "I may have pushed it a little far, but [bree.name] simply goes back to grinning, she doesn't seem to be all that bothered now."
            mike.say "Why do you care anyway? Who cares what your music tastes are?"
            show bree talkative
            bree.say "Well, it's a little weird is all."
            show bree normal
            mike.say "Weird, how so?"
            $ bree.sub += 5
        "Hey, I don't care.":
            mike.say "Why should I? So we have different taste in music, doesn't matter to me."
            show bree flirt blush
            show fx heart
            "Everyone has different tastes, and although the temptation to tease [bree.name] is there, only helped by how utterly adorable she looks when she's blushing, I don't want to really embarrass her."
            show bree happy
            bree.say "Hehe, thanks [hero.name]! It's just like, weird, you know?"
            show bree normal
            mike.say "Liking country music isn't weird."
            show bree talkative
            bree.say "No, I mean like... I don't actually like the music itself."
            show bree normal
            mike.say "Uh, what do you mean?"
            $ bree.love += 5
    show bree talkative -blush
    bree.say "I only listen to it because it reminds me of home."
    bree.say "I came from like, a little town in the middle of nowhere, the exact sort of place these songs are about, you know?"
    bree.say "I dunno, guess it feels like, nostalgic?"
    show bree normal
    mike.say "That makes sense I guess. You miss home?"
    "A short pause followed for [bree.name] to think."
    "I don't rush her, giving her the space she needed."
    "I do take the opportunity to take a seat back on the bed rather than have the conversation standing in the middle of the room however."
    "Fortunately for me, [bree.name] followed, and she finally spoke as I leaned over to grab my now room temperature drink."
    show bree talkative
    bree.say "No."
    show bree normal
    mike.say "Really?"
    show bree talkative
    bree.say "Yeah, I mean, I like, wouldn't go back there, you know?"
    show bree normal
    "It's odd to see her, not exactly unenthusiastic, just not quite as overly eager as she usually is."
    mike.say "Any reason why?"
    show bree talkative
    bree.say "Uh, it's like, a really long story, and I don't wanna bore you!"
    show bree happy
    bree.say "I'm happy here with you and Sasha anyway!"
    show bree normal
    "Well, that didn't last long. [bree.name] was already back to exclaiming everything she said needlessly enthusiastically, and the grin on her lips had already returned."
    "It didn't take a genius to see that wasn't the end of that story, but it didn't take a detective to realise she just didn't want to tell it."
    "Just having a bad childhood didn't make sense, not if she willingly reminded herself of it with music."
    "I couldn't deny being curious, but wasn't going to push it any further, so I quickly gave her an out."
    mike.say "So you've been getting along with Sasha?"
    show bree smile
    bree.say "Well enough! I mean, she's a little mean and we like, argue sometimes I guess, but we at least aren't enemies, and that's good enough for me!"
    show bree normal
    "That made enough sense to me, their personalities do clash somewhat but [bree.name] seems like the type of person who wouldn't have enemies of any kind."
    mike.say "Glad to hear you're getting along, it's one thing not to like someone, entirely another thing not to like your roommate."
    show bree happy
    bree.say "Hehe, I can only imagine! You guys are my first roommates, so I guess I'm like, really lucky~!"
    show bree talkative
    bree.say "Oh right! You like, took two roommates at once, right? Did you have people staying here before?"
    show bree normal
    mike.say "Yeah, remember how I mentioned my friend just graduated medical school? Him and his girlfriend."
    mike.say "Well, they weren't together when we first moved in."
    show bree talkative
    bree.say "Wow! So they like, moved in as roommates then fell in love~?"
    show bree smile
    bree.say "That's really romantic!"
    show bree normal
    mike.say "Yeah, sure it is."
    show bree stuned
    "The disdain in my voice must have been obvious."
    "I was still friends with Ryan, sure, but I also still harboured quite the crush on Samantha, and [bree.name] gushing over their relationship didn't help."
    show bree surprised
    show fx question
    bree.say "What's wrong, [hero.name]?"
    show bree stuned
    mike.say "Nothing, it's stupid."
    show bree talkative
    bree.say "Nuh uh! Listening to country music because it reminds you of home is stupid, and you were nice even then!"
    bree.say "I like, really don't believe it's that bad!"
    show bree normal
    mike.say "And I really think it is."
    show bree talkative
    bree.say "Come on! Just tell me~! I promise I won't laugh!"
    show bree normal
    "I opened my mouth ready to say no once again, but there's no point."
    "I already know that [bree.name] is going to drag it out of me eventually, and I can't be bothered with the back and forth anyway."
    mike.say "I used to have a crush on her when she first moved in."
    show bree stuned
    show fx exclamation
    "[bree.name]'s eyes immediately widened with shock, her jaw practically dropping in surprise."
    show bree surprised
    bree.say "Ah! I'm like, really sorry!"
    bree.say "I probably just made you feel worse, I didn't know, please forgive me!"
    show bree gloomy
    mike.say "Relax, it's fine."
    show bree sad
    bree.say "Really? You mean it?"
    show bree sadsmile
    mike.say "Yeah, she made her choice, nothing I can do about it now."
    show bree surprised
    bree.say "Wow [hero.name], that's like, a really mature way of looking at it!"
    show bree stuned
    mike.say "Really?"
    show bree smile
    bree.say "Yeah, really! I'm impressed!"
    show bree normal
    "Something about [bree.name]'s warm expression and gleeful exclamation surprisingly makes me feel better."
    "It wasn't as though she'd said anything monumental or particularly special, but she felt so genuine that I couldn't help but smile along with her."
    mike.say "Thanks [bree.name], that makes me feel a lot better."
    show bree happy at startle
    bree.say "Hehe, anytime!"
    show bree talkative
    bree.say "I'm just like, really sorry for bringing it up!"
    show bree normal
    mike.say "Hey, I already said it was fine."
    show bree talkative
    bree.say "I know but-"
    show bree normal
    mike.say "[bree.name], it's fine."
    show bree happy at startle
    bree.say "Hehe, alright~!"
    show bree normal
    mike.say "So uh, wanna play a few more rounds?"
    show bree smile
    bree.say "Always!"
    show bree normal
    "[bree.name] had made me feel better, sure, but I still wasn't entirely over Samantha, and more than anything else right now I just wanted to take my mind off it."
    "Either [bree.name] saw that, or she just wanted to play more, because before I had a chance to pick my controller back up she'd already selected her character and was waiting on me."
    "So, we played for another hour or so, the back and forth yet again keeping us engaged, and distracting each of us."
    "Me, from thinking about Ryan stealing Samantha, and for [bree.name], presumably memories of home."
    "Before long however, it was time to call an end to our game, the final score determining [bree.name] the winner by a narrow margin, narrow enough that she insisted we call it a draw."
    "We grabbed another drink and chatted about the leak a little more before we each went our separate ways."
    hide bree
    return

label bree_pool_throat:
    "Nothing like a relaxing swim by the pool, I say."
    "The sun is shining, there's no more work to do for awhile."
    "All is good."
    "While I'm getting in my few laps, the door opens up, and out steps [bree.name]."
    show bree swimsuit at left with easeinleft
    "She's dressed in a bikini that clings tightly to her body."
    show bree happy
    bree.say "Heeey, [hero.name]! Enjoying the weather, too, huh?"
    show bree normal
    mike.say "Hey, [bree.name]. You getting in?"
    show bree smile at center with move
    bree.say "Maybe! I just felt like I should step outside for once, you know, get some air."
    show bree normal
    mike.say "Sounds good to me, it's as nice a day as any. Besides, I can't picture a better view."
    show bree swimsuit happy blush
    bree.say "Hehe, thanks [hero.name]~."
    show bree smile
    bree.say "You're really nice sometimes, you know?"
    bree.say "I don't know though, like I've never liked being out in public dressed like this, you know?"
    show bree normal
    mike.say "Well it isn't like anyone can see you except me, we're too high up."
    mike.say "Besides, I've already seen everything before."
    show bree b flirt
    "I smirk as [bree.name] gasps playfully, feigning outrage for a few seconds, before giggling with a few shades of rose on her cheeks."
    show bree smile
    bree.say "See, this is what I mean, you're always so nice to me for some reason."
    bree.say "I'm not like, complaining or anything It's nice."
    show bree normal
    "I smile at her, and she smiles back, then sets up her towel by the side of the pool and lies down."
    show bree talkative
    bree.say "I am pretty tired though."
    bree.say "Maybe I won't swim, just lie here for a while and do nothing."
    show bree normal
    mike.say "Sounds productive."
    show bree talkative
    bree.say "Heh I'm uh, not very productive..."
    show bree sadsmile
    "I consider teasing her for a moment, but I detect a hint of sadness in her tone."
    "I'm not sure why, so I don't push it just in case."
    show bree happy
    "Instead I swim over to her, resting by the side of the pool and examining her while she can't see me doing so."
    scene bg pool at dark, blur(5)
    show bree b swimsuit happy at center, zoomAt(1.5, (640, 1040)), top_to_bottom
    "Really, I haven't seen her in a swimsuit so close before."
    "I've seen her with plenty less, of course, but still."
    show bree b swimsuit happy at center, zoomAt(1.5, (640, 1040)), bottom_to_top
    "There's just something about it that makes it titillating, even though it technically covers all the naughty bits."
    "I hope the water will hide my growing erection."
    scene bg pool
    show bree b swimsuit happy
    bree.say "Hey, [hero.name]?"
    show bree normal
    mike.say "Yeah?"
    show bree talkative
    bree.say "You went quiet, I was just making sure you were still there."
    show bree normal
    mike.say "Heh, yeah I'm right here, I wouldn't just abandon you."
    show bree talkative blush
    bree.say "...Thank you."
    show bree flirt -blush
    "She opens her eyes and cranes her head towards me, her grin not her usual but instead that cute little one she gives sometimes."
    "The smaller one, the one that's more genuine than cheerful. The one that makes my heart skip a beat."
    "I can't help but smile back. Leaning over, I plant a soft kiss on her forehead, before beginning to lightly stroke her hair."
    show bree happy
    "We stay like that for a little while in silence, before I speak."
    mike.say "Hey, [bree.name]?"
    show bree stuned
    show fx question
    bree.say "Hmm?"
    show bree flirt
    "She looks up to me, opening her eyes and raising an eyebrow, clearly wondering what I wanted."
    mike.say "I know I said it before, but seeing you in a swimsuit? Really something to behold."
    show bree b happy at startle
    "She giggles and begins playing with a strand of her hair, back to her usual trademark grin."
    mike.say "No, I mean it. I know I've seen you with less, but there's really something special about you like this."
    show bree normal
    "She doesn't giggle at this. Not because she doesn't like it, but because she's started to pick up on the underlining lust in my voice."
    show bree hesitating blush
    show fx heart
    bree.say "Really?"
    show bree flirt -blush
    mike.say "Yeah, really."
    show bree hesitating blush
    bree.say "Well You aren't that bad yourself."
    show bree flirt -blush
    "There's something else in her gaze now, something I've felt since she walked out of the house."
    hide bree
    show bree kiss swimsuit
    with fade
    $ bree.flags.kiss += 1
    "Slowly, I lean over and meet her lips with my own, and what starts as an innocent peck quickly turns into a deep embrace."
    "I stand at my full height, practically looming over her and not only pulling her in closer, but shifting her around as well."
    "She lets me position her at my will, content to let me lead as per usual."
    show bree rough oral at center, zoomAt(1.25, (500, 840)) with fade
    "Soon, her head is just by the pool while her body stretches towards the house, and now that it's out of the water, she very quickly notices my bulge."
    "I feel like I've done a good job getting across my intentions, so I don't pause to ask for permission as I pull back, breaking the kiss, and shove my shorts down in one movement."
    "Her eyes widen as she sees my rod, but I don't give her much chance to prepare herself."
    hide bree
    show bree rough oral
    with hpunch
    "Before she can react, I grab her by the shoulders, pushing myself forwards into her throat."
    "She squeals, her mouth now full of my chlorine cock."
    "Her heels dig into her towel as she rolls about, so I give her a brief respite, pulling back to give her a chance to breathe."
    "After a few seconds, I thrust again."
    "Her hair spreads out as it dips into the water, her face tilted all the way back with her forehead soaking in sweat and the liquid from the pool itself."
    show bree rough oral pain
    "This gives my dick a straight shot down her mouth and into her throat."
    "I slowly build up speed, letting her get more used to the intrusion, but my lust begins to get the better of me, and soon enough I'm going as fast as my hips can manage."
    "Her squeals drive me forward as I push myself deeper into that uncharted territory, my hands gripping onto her shoulders and her neck as the bulge in her throat is evidence that I'm filling her up."
    show bree rough oral throat pain
    "She grabs my sides, squeezing me tightly. Her body remains tense as I block her airway with my dick."
    mike.say "I'm close now!"
    "I tell her less as a warning, more as an assurance that she'll be back to breathing normally again soon."
    show bree rough oral throat fx
    "She lets out an affirmative squeal, scratching along my sides."

    "Her suit stains with the wetness that I'm giving her."
    "Through the struggle I can see on her face she's getting some sort of enjoyment out of this, that it isn't entirely one sided."
    with hpunch
    "Soon enough, I throw my head back, letting out a pleased groan as I shoot off into her."
    $ bree.sub += 5
    with hpunch
    pause 0.25
    show bree rough oral cum with hpunch
    "Unfortunately, some of my sperm spits out of her mouth, trailing down towards her nose and her eyes and dripping into the pool."
    hide bree
    show bree b swimsuit mouthful at center, zoomAt(1.5, (640, 1040))
    with fade
    "When I pull back, she coughs, more of the jizz staining the pool."
    "She rubs her throat, groaning as she sits herself up, coughing and spluttering as she tries to get her voice back."
    "But I wrap my arms around her and she gasps, looking over her shoulder in surprise."
    show bree talkative blush
    bree.say "Aaah, [hero.name]!?"
    bree.say "Aaah, [hero.name]!?"
    show bree sadsmile
    "Her voice is harsh and hoarse voice, but she's interrupted before she can say anything else, falling into the water with me."
    "She eventually comes back up, looking down over herself, soaked, yet washed of my spunk."
    show bree sad blush
    bree.say "...My throat hurts..."
    show bree sadsmile -blush
    "I grin at her and we make eye contact, which is enough for her to giggle and smile in return."
    mike.say "Yeah, guess I could have been more gentle, but where's the fun in that?"
    show bree happy blush
    "She blushes and giggles again, shrugging her shoulders in an exaggerated manner."
    show bree evil
    bree.say "Well, I didn't like, hate it..."
    show bree swimsuit flirt -blush
    mike.say "I, for one, thoroughly enjoyed it."
    "She smiles, leans in, and pecks me on the cheek. Then splashes me."
    "I'm caught off guard and left spluttering as [bree.name] attempts to escape without recompense, but I quickly grab her leg and drag her back as she squeals."
    "We spend the next ten minutes playing in the pool, before [bree.name] eventually says that she has to go clean up, and I decide to get out and clean up the mess we made in the pool too."
    $ bree.flags.bj += 1
    return

label bree_about_kiss:
    show bree
    "[bree.name] walks toward me."
    call bree_greet from _call_bree_greet_3
    show bree talkative blush
    bree.say "About that kiss..."
    show bree flirt -blush
    mike.say "Yes?"
    show bree talkative blush
    bree.say "Could you forget about it?"
    bree.say "I don't want it to be awkward between us..."
    show bree flirt -blush
    $ result = renpy.display_menu([("Yes", 1), ("No", 2)])
    if result == 1:
        mike.say "Sure, It's already forgotten."
        show bree smile
        bree.say "Thanks."
        $ bree.love += 1
    else:
        if hero.charm >= 20:
            mike.say "I don't want to, it's too sweet a memory..."
            show bree smile blush
            bree.say "Well, try anyway... Please."
            $ bree.love += 2
        else:
            mike.say "No can do, I am still rock hard thinking about it!"
            show bree annoyed
            bree.say "Jerk!"
            $ bree.love -= 3
    hide bree
    return

label bree_talk_breakup_male:
    call bree_greet from _call_bree_greet_4
    show bree talkative
    bree.say "I heard you had a bad breakup?"
    show bree sadsmile
    mike.say "Yeah, and then the girl I was in love with chose another man."
    show bree sad
    bree.say "Tough luck..."
    show bree gloomy
    mike.say "You don't say, I am afraid I'll never love again..."
    show bree happy
    bree.say "You know what Yoda would say?"
    show bree normal
    mike.say "No?"
    show bree talkative
    bree.say "Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering."
    bree.say "So stop being afraid..."
    bree.say "Be a Jeudi."
    show bree normal
    mike.say "You do know that a Jeudi is forbidden to love."
    show bree wink
    bree.say "Yeah, maybe not my best metaphor."
    $ bree.love += 2
    hide bree
    return

label bree_kiss_me:
    call bree_greet from _call_bree_greet_5
    show bree flirt blush
    if not bree.flags.kiss:
        "[bree.name] looks troubled while walking in my direction."
        "She seems to hesitate a little, then leans toward me, she obviously tries to kiss me."
        $ result = renpy.display_menu([("Kiss her", 1), ("Don't kiss her", 2)])
        if result == 1:
            hide bree
            show bree kiss
            with fade
            "[bree.name] kisses me softly but hungrily. The time stops for a few heartbeat."
            "After some time (I couldn't tell how long), we part."
            if bree.love >= 60 - hero.charm/2:
                hide bree
                show bree blush
                mike.say "What's the occasion?"
                show bree happy
                bree.say "I felt like giving myself a treat."
                show bree normal
                mike.say "Feel free to indulge yourself whenever you feel the need."
            else:
                hide bree
                show bree evil blush
                bree.say "I shouldn't have done that..."
            $ bree.flags.kiss += 1
            $ bree.love += 1
        elif result == 2:
            show bree gloomy
            "[bree.name] looks hurt when I push her away."
            $ bree.love -= 1
    else:
        "[bree.name] walks toward me..."
        show bree kiss with fade
        "...and kisses me deeply."
        hide bree kiss
        show bree blush
        with fade
        if bree.love >= 60 - hero.charm/2:
            mike.say "What's the occasion?"
            show bree happy
            bree.say "I felt like giving myself a treat."
            show bree normal
            mike.say "Feel free to indulge yourself whenever you feel the need."
        else:
            show bree evil blush
            bree.say "I shouldn't have done that..."
        $ bree.love += 1
        $ bree.flags.kiss += 1
    hide bree
    return

label bree_get_out_male:
    if game.from_room != "bathroom":
        show bree vangry
        if bree.activity["clothes"] == "underwear":
            bree.say "Please can you step out?"
        else:
            bree.say "I am naked. Please can you step out?"
        hide bree
    else:
        "I hear a voice through the door."
        if game.room == "bathroom":
            bree.say "[hero.name] I need the bathroom, can you step out?"
        else:
            bree.say "[hero.name], can you step out?"
        mike.say "Sure."
    return

label bree_not_get_out_male:
    if bree.get_clothes() == "naked":
        call bree_not_get_out_naked_male from _call_bree_not_get_out_naked_male
    else:
        call bree_not_get_out_clothed_male from _call_bree_not_get_out_clothed_male
    return

label bree_not_get_out_naked_male:
    if bree.love >= 170 and game.days_played % 5 == 0:
        show bree normal naked
        "I know that barging into the bathroom is a really bad habit."
        "And I really should train myself to knock before entering."
        "But the door's not locked and I'm thinking about something else."
        "That's why I just open the door and walk straight in there."
        show bree surprised at startle
        bree.say "Oh!"
        show bree happy
        bree.say "Hello there!"
        show bree normal
        "I stop in my tracks, staring dead ahead."
        "I guess I must look like a deer in the headlights right now."
        show bree naked b at center, zoomAt(1.25, (640, 900)), top_to_bottom
        "But there's no way I can tear my eyes away from what I'm seeing."
        mike.say "B...B...[bree.name]!"
        mike.say "B...B...Butt!"
        "[bree.name]'s standing there, totally naked!"
        show bree naked b normal at center, zoomAt(1.25, (640, 900)), bottom_to_top
        "And that view's enough to blow my mind!"
        show bree smile
        bree.say "Hey, [hero.name]!"
        bree.say "I guess you thought the bathroom was empty, huh?"
        show bree wink
        bree.say "Otherwise you'd be a dirty little pervert!"
        show bree normal
        "[bree.name] turns around as she's saying all of this."
        show bree at center, zoomAt(1.25, (640, 900)), hshake
        "And she does it with a little hop, just for good measure."
        "Which means that everything's in motion as she turns."
        mike.say "B...B...Breasts!"
        "I'm expecting [bree.name] to freak out and slap me or something."
        "At least to kick me out of the bathroom and tell me off."
        show bree happy
        "But instead she actually seems to be amused by my reaction."
        bree.say "Okay, [hero.name]..."
        show bree smile
        bree.say "Since you're here by accident, you can stay."
        bree.say "Just be a good boy while I get finished up, okay?"
        show bree normal at center, zoomAt(1.0, (840, 900)) with ease
        "I nod silently, my eyes still following her every move."
        "Of course I've seen [bree.name] around the house in some pretty skimpy stuff."
        "Hell, I've even seen her lounging around the pool in her swimsuit."
        "But this is totally different."
        show bree a
        "A chance to be within touching distance of her naked body!"
        "And yet still not being able to reach out and actually touch it."
        show bree at center, zoomAt(1.0, (540, 900)) with ease
        "[bree.name] seems to be getting off on this as much as me too."
        "She goes about finishing up her routine in the bathroom."
        show bree b
        "But I'm sure she doesn't usually do it with nothing at all on."
        "And I'm convinced it doesn't usually feature so much motion either."
        show bree at center, zoomAt(1.25, (540, 900)), startle
        "Every chance she gets, [bree.name] jumps and bounces on her heels."
        show bree at center, zoomAt(1.0, (640, 900)) with ease
        "She sways and sashays around the bathroom in front of me."
        "And before long, I'm hopelessly hard, aching from watching her."
        "Then suddenly it's all over."
        show bree a towel -naked
        "[bree.name] snatches up her towel and cover herself with it."
        hide bree
        show bree towel at center, zoomAt (1.65, (850, 1140))
        "Then she slips past me and out the door."
        show bree smile
        bree.say "All done!"
        show bree happy
        bree.say "Bathroom's yours!"
        show bree normal at center, zoomAt (1.0, (850, 1140)), startle
        "She's sure to squeeze my cock as she passes though."
        hide bree with easeoutright
        "Making me gasp and double over while the door slams shut."
        "And that's how she leaves me."
        "My mind reeling from what I just saw."
        "And my cock aching from what she just did to me."
        $ game.pass_time(1, True)
    else:
        show bree flirt blush
        "[bree.name] is naked..."
        mike.say "Sorry, [bree.name]. I didn't know you would be here."
        bree.say "You know... I don't mind if you come in..."
        hide bree
    return

label bree_not_get_out_clothed_male:
    show bree flirt
    if bree.get_clothes() == "underwear":
        "[bree.name] is in her undies..."
    mike.say "Sorry, [bree.name]. I didn't know you would be here."
    show bree smile
    bree.say "Stop it, we know each other well enough not to be bothered by that..."
    hide bree
    return

label bree_shower_BJ:
    "I usually take a shower in the morning so that I'm fresh for the day ahead, but tonight I was just so worn-out and tired that I felt I needed it."
    $ renpy.sound.play("sd/shower.ogg", loop=True)
    "So without any great fuss or ceremony, I just turn on the water, strip off and hop in on my way to crawling into bed at the end of the day."
    "The feeling of the water washing over me and the warmth seeping into my tired limbs is enough to tell me that I'd made the right decision."
    "Even after no more than a couple of minutes in there, I'm more than sure that I'll have no trouble falling into a deep and pleasant sleep as soon as my head hits the pillow."
    "In fact, I'm in so much of a state of relaxation that I hardly notice the sound of the bathroom door opening and someone slipping inside."
    "Normally I'd be pretty attentive to the fact that I've been joined in the middle of a shower like that."
    "But I feel so sleepy and relaxed by now that I just assume it's either Sasha or [bree.name] nipping into the bathroom for some unknown reason and hoping not to be caught in the act."
    "Whoever it is and whatever they're after, I simply decide that, so long as they don't make the fatal error of flushing the toilet, they can do as they please."
    "This means that when I hear the sound of tapping at the glass of the door to the shower cubicle, I yelp and almost jump out of my skin."
    with vpunch
    "That kind of a reaction would be embarrassing in and of itself in any other circumstances."
    "But as I'm standing inside a shower that's raining water down on me, I instantly find myself slipping and sliding around on the floor, trying to brace myself against equally slippery walls."
    "I don't know if my unexpected visitor was always intent upon making his presence known to me and then letting himself into the shower, or if my apparent state of disorientation prompting him to come to my rescue."
    show bree a towel with dissolve
    "Either way, almost the same moment that I manage to stop myself slipping and suffering an unpleasant fall, [bree.name]'s head appears around the shower door."
    "At the sight of her, I begin to open my mouth, intending to say something that probably won't adequately explain why I just freaked out."
    show bree b towel
    "But [bree.name] instantly puts a finger to her lips, telling me to keep quiet and waves me back with her other hand."
    "While our shower's not exactly huge, there's still enough room for me to flatten my back against the wall and allow her to step inside comfortably."
    "Only [bree.name] pauses before she does this, letting me see her shoulder her way out of the robe she's wearing and let it fall to the floor."
    show bree naked
    "Underneath she's completely naked, the crack of an opening in the shower door enough for me to know that my eyes aren't deceiving me."
    "The effect of that sight is enough to ensure that my heart is racing even as she slides the door open just wide enough to step fully into the shower."
    "Even now that she's inside of the shower with me, still [bree.name] doesn't as much as say a single word."
    scene bg bathroom at dark, blur(5)
    show bree b naked at center, zoomAt(1.5, (640, 1040)), top_to_bottom
    "Instead she just stands there, letting the water run down her body and soak her hair so that it settles into heavy, honey-coloured locks."
    "I think that I'm beginning to understand a little of what this is all about, as I can't keep from staring at this stunning view of her naked body."
    "[bree.name]'s not saying a word because she wants to keep this little encounter between us based on nothing more than the sight of each other and the feelings this stirs inside of us."
    show bree b naked at center, zoomAt(1.5, (640, 1040)), bottom_to_top
    "And it's no great surprise that it's working - well, at least it is from where I'm standing."
    "[bree.name]'s doing nothing more suggestive than standing mere inches away from me whilst completely naked, and already I'm starting to stir."
    show bree flirt
    "As she watches my cock stiffen and begin to stand to attention with what looks like growing delight, I watch her expression just as closely."
    "This means that the more [bree.name] looks at my cock with what can only be mounting anticipation, the more turned on I become in turn."
    "And in this way we seem to be feeding off of each other, becoming ever more aroused so long as neither of us breaks the cycle."
    "But all the same, when [bree.name] finally does so, I can hardly say that it comes as any kind of disappointment."
    show bree blush
    "Still keeping her silence, she bites her lip in anticipation and reaches out with one hand to take hold of my cock."
    "She holds it for a moment, and then begins to rub up and down the length of my shaft with a gentle, caressing touch."
    "The water that's constantly cascading over the both of us means that there's no need for any kind of lube."
    "And this also means that [bree.name] can steadily increase the speed and the amount of pressure that she's applying too."
    show shower bj breesasha bree with fade
    "Up until the very moment that she begins to sink down onto her knees, I had been thinking that I was getting a hand-job and would have been very glad of it."
    "But now I can see [bree.name]'s eyes focussing on the head of my cock, and the tip of her tongue sticking out from between her lips in anticipation."
    "And it seems as though I'm about to get far more than I could ever have expected."
    "Especially when all I wanted to begin with was a quick shower before bed!"
    show shower bj breesasha breemouth
    "I feel a shudder of pure pleasure pass through me as the sensation of [bree.name]'s lips and tongue first caress the very tip of my cock."
    "She could spend as long as she wants doing just that, and I'd be perfectly satisfied."
    "But she apparently has other things in mind, as she takes a full third of my length into her mouth mere moments afterwards."
    "From there, she begins to bob her head back and forth, taking me by surprise with the vigour of her pace."
    "Her eyes are closed and her face shows nothing save for a devotion to the task at hand, cheeks puckering as she sucks as hard as she's able."
    "It's all that I can do to keep from closing my eyes too, from just letting go to letting the sensations that [bree.name]'s creating inside of me."
    "Instead I reach out and run my hands through her hair, gently holding the sides of her head as she moves."
    "I have no way of knowing if this tactile gesture has any effect whatsoever upon [bree.name]."
    "But for me it's a means of grounding myself and adding another physical element to the experience."
    "All the same, she's taking me so deep now with every rhythmic motion of her head that it can't be long before I cum."
    "That I've lasted so long at all is baffling to me, as I was so weary to begin with that just standing up in the shower felt like a challenge."
    "[bree.name] may have somehow managed to coax a hidden reserve of energy and stamina out of me with her attentions, but that can't last forever."
    hide shower bj breesasha
    show shower bj breesasha bree
    "She must feel the onset of my orgasm almost as clearly as I do myself, as she pulls back her head and frees my cock just in time."
    show shower bj breesasha bree shoot with hpunch
    pause 0.25
    with hpunch
    "Making no effort to get out of the way, she takes the entirety of my ejaculation full on and in the face."
    show shower bj breesasha bree facial with hpunch
    "But all the same, there's only literal seconds to see the cum streaked across her face, as the water washes it away almost as quickly as it lands."
    "[bree.name] remains kneeling in the shower, waiting patiently until the very last drop of evidence is carried down the drain, and she's as clean as she was the moment she stepped into the shower to begin with."
    "And once she's spotless, she gets to her feet and lets herself out of the shower, still without uttering a single word."
    "Once [bree.name] has left the bathroom, I can't help but think that it was probably for the best that she did remain silent throughout what she just did to me."
    "As it's a rare thing for a girl to leave a guy lost for words and not get mad when he actually is."
    stop sound
    $ bree.flags.bj += 1
    return

label bree_birthday_date_male:
    $ DONE["bree_birthday_date_male"] = game.days_played
    $ game.active_date.clothes = "date"
    $ game.room = "date_restaurant"
    scene bg restaurant with fade
    "At first I was worried that dinner and a movie might not be special enough for [bree.name] on her birthday."
    show bree date at center, zoomAt(1.5, (640, 1040)) with easeinright
    "But as the waiter shows us to our table, she's so enthusiastic that I soon forget all of my concerns."
    "I guess it's easy to get tangled up in the notion that you have to make everything unique and memorable."
    show bree date happy at center, zoomAt(1.5, (640, 1140)) with ease
    "And the danger is that you can forget to just sit back and enjoy the simpler things in life."
    "Like right now, I'm really enjoying how happy [bree.name] seems to be."
    show restaurant meal bree date nomeals
    show restaurant_meal_waiter_pose03 as man zorder 1 at center
    with fade
    pause 0.3
    hide restaurant_meal_waiter_pose03 as man zorder 1 at center with easeoutright
    "She's positively beaming across the table at me as the waiter hands us each a menu."
    bree.say "Mmm..."
    show restaurant meal bree happy
    bree.say "I'm so hungry I could eat a horse!"
    show restaurant meal bree -happy
    mike.say "Hmm..."
    mike.say "I don't see horsemeat anywhere on the menu."
    mike.say "You want me to ask the waiter?"
    show restaurant meal bree blush
    "[bree.name] blushes in the most attractive way possible."
    "She waves a hand at me in alarm."
    show fx exclamation at right5
    bree.say "NO!"
    bree.say "[hero.name], I didn't mean..."
    "She stops in mid flow as she sees me raise my eyebrows and grin."
    show restaurant meal bree bored -blush
    show fx anger at right5
    bree.say "Ooh, you jerk!"
    mike.say "I'm sorry, [bree.name]."
    mike.say "It was just a joke!"
    show restaurant meal bree -bored
    "[bree.name] shakes her head."
    show restaurant meal bree happy
    "But she gives me a grudging smile all the same."
    bree.say "You've gotten me all discombobulated now."
    bree.say "I don't know what on earth I want to eat!"
    bree.say "So you can help me to choose, okay?"
    show restaurant meal bree normal
    menu:
        "Don't help her":
            $ game.active_date.score -= 10
            "Choosing food for someone else is just the worst."
            "Because they always seem to know what they really want to eat."
            "And they're just waiting for you to say that too."
            "That is after you've suggested everything else on the menu first!"
            "So that's why I roll my eyes at [bree.name]'s request."
            mike.say "Geez, [bree.name] - it's no big deal!"
            mike.say "Just order a burger or a steak or something."
            mike.say "What about a salad?"
            show restaurant meal bree bored
            "[bree.name] looks a little disappointed at my response."
            "I think that she can sense frustration in the tone of my voice too."
            bree.say "Okay, okay..."
            bree.say "I guess I'll just have a cheeseburger..."
        "Help her":
            $ game.active_date.score += 15
            "I don't normally like to help someone choose their food."
            "They usually know what they actually want anyway."
            "But it's [bree.name]'s birthday."
            "So I smile and indulge her."
            mike.say "You know me, [bree.name] - I'm no gourmand!"
            mike.say "But I was going to have a cheeseburger."
            mike.say "Because it's really hard to screw that up!"
            show restaurant meal bree happy
            "[bree.name] puts her hand in front of her mouth to stifle a giggle."
            "She shakes her head at me, clearly amused."
            show restaurant meal bree -happy
            bree.say "Oh, [hero.name] - what are you even like?"
            bree.say "We come out to such a nice place."
            bree.say "And you want to eat a cheeseburger?!?"
            show restaurant meal bree happy
            bree.say "Oh, what the hell - I'll have one too!"
    show restaurant meal bree eat -nomeals -happy
    show restaurant_meal_waiter_pose03 as man zorder 1 at center
    with fade
    pause 0.3
    hide restaurant_meal_waiter_pose03 as man zorder 1 at center with easeoutright
    "Once the food arrives, [bree.name] tucks into what's on her plate with gusto."
    "I mean, it's not like she's messy or anything like that."
    show restaurant meal bree happy
    "But you can clearly see that she's enjoying her food."
    "And she isn't afraid to show it either!"
    "Not that I'm complaining - it's really quite impressive."
    "The enthusiasm she's showing is almost sexy somehow!"
    show restaurant meal bree -happy blush
    "But after a little while, I get the impression that [bree.name]'s waiting for something."
    "She keeps smiling at me a little too much and fluttering her lashes too."
    mike.say "Ah, [bree.name]..."
    mike.say "Is there something up?"
    bree.say "Oh, no...not really."
    bree.say "It's just that this feels like one of those moments, you know?"
    mike.say "I'm not sure that I do!"
    bree.say "Sure you do, [hero.name]!"
    bree.say "Like if we were in a film, you'd whip out a ring and ask me to marry you."
    mike.say "You want me to propose?!?"
    "[bree.name] starts waving her hands at me and shaking her head."
    bree.say "No, silly!"
    bree.say "I just mean it feels like one of those moments, that's all!"
    show restaurant meal bree -blush
    if not hero.has_gifts:
        "I rub the back of my head, smiling like a dope."
        mike.say "Oh...well..."
        mike.say "That's okay then!"
        mike.say "Whew...I really did think you wanted me to propose just now!"
        bree.say "Yeah - that would have been crazy, huh?"
        "[bree.name]'s nodding and smiling."
        show restaurant meal bree bored
        "But I can't help get the feeling that I've somehow missed her point."
        "It's too late to backtrack now though."
        "So all I can do is keep on laughing like a goon."
        $ game.active_date.score -= 20
        $ bree.love -= 10
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_5
        if _return != "done":
            if _return not in ["None", "exit"]:
                "Of course - the birthday present!"
                "Now would be the perfect moment to surprise her with it."
                mike.say "Happy Birthday, [bree.name]!"
                show restaurant meal bree happy
                "I see her face light up as I hand over the gift."
                bree.say "Oh, [hero.name]."
                bree.say "You were just kidding around!"
                play sound [paper_ripping_2, paper_ripping_1]
                "I watch as she opens it, waiting to see her reaction."
                if _return:
                    $ game.active_date.score += 15
                    show restaurant meal bree -happy blush
                    "And then I see her face increase in brightness by what looks like a factor of ten."
                    bree.say "Oh...how did you know?!?"
                    bree.say "I've always wanted one of these!"
                    mike.say "Well...I kinda saw you didn't have one."
                    mike.say "Is it the right type?"
                    mike.say "The woman in the shop told me that..."
                    show restaurant meal bree happy -blush
                    bree.say "No, no...it's perfect!"
                    "Whew - chalk one up for me in the win column!"
                else:
                    $ game.active_date.score -= 10
                    show restaurant meal bree bored
                    "And then I see her face drop a little."
                    bree.say "Oh...it's..."
                    show fx drop at right5
                    bree.say "It's very nice...very thoughtful..."
                    mike.say "What's wrong, [bree.name]?"
                    mike.say "I thought everyone wanted one of those?"
                    bree.say "They do...they do!"
                    bree.say "I just already got one, that's all."
                    "Well, this is nice and awkward..."
            else:
                $ game.active_date.score -= 20
                "I rub the back of my head, smiling like a dope."
                mike.say "Oh...well..."
                mike.say "That's okay then!"
                mike.say "Whew...I really did think you wanted me to propose just now!"
                bree.say "Yeah - that would have been crazy, huh?"
                "[bree.name]'s nodding and smiling."
                show restaurant meal bree bored
                "But I can't help get the feeling that I've somehow missed her point."
                "It's too late to backtrack now though."
                "So all I can do is keep on laughing like a goon."
    hide bree
    show restaurant meal bree -eat order nomeals -blush -bored -happy with fade
    pause 0.3
    show restaurant_meal_waiter_pose03 as man zorder 1 at center with easeinright
    "With the main course done and dusted, the next obstacle presents itself."
    "The waiter hands us the dessert menus, and the intricate dance begins in earnest..."
    bree.say "Hmm..."
    bree.say "I'm feeling pretty stuffed!"
    bree.say "Were you going to have a dessert?"
    bree.say "Because I WILL have one if you are..."
    menu:
        "No":
            $ game.active_date.score -= 10
            mike.say "I can take it or leave it, [bree.name]."
            mike.say "If you'd have wanted one, I'd have said yes."
            mike.say "But if you're full, then I'll pass."
            show restaurant meal bree bored
            "[bree.name] looks disappointed the moment I say this."
            "But she's kind of backed herself into a corner here."
            "She can't come out and say she actually wants a dessert."
            "That way she'll look like a bit of a pig."
            "Even more so thanks to the fact she'd be eating on her own too!"
            $ ordered_desert = False
        "Yes":
            $ game.active_date.score += 15
            show restaurant meal bree happy
            mike.say "It's your birthday, [bree.name]!"
            mike.say "Who cares - have a dessert if you want one."
            show restaurant meal bree -happy blush
            bree.say "Well, I don't know..."
            mike.say "Look, I'll order one too."
            mike.say "Would that help?"
            show restaurant meal bree happy -blush
            "[bree.name] nods happily."
            "And with that we order a couple of desserts."
            $ ordered_desert = True
    show restaurant meal bree -happy -bored
    "I smile at [bree.name] as I check my wallet, mentally adding up the cost of the bill and a tip."
    if hero.money >= 300:
        $ game.active_date.score += 15
        $ hero.money -= 300
        "Luckily for me I have more than enough to cover it."
        "And I make a point of leaving a generous tip too."
        "No harm in making myself look generous in front of [bree.name]!"
    else:
        $ game.active_date.score -= 10
        "I feel my heart sink as I realise that I don't have enough to even cover the bill."
        show restaurant meal bree bored
        mike.say "Ah, [bree.name]..."
        mike.say "Could I borrow a couple of bucks?"
        "[bree.name] rolls her eyes as she reaches for her purse."
        bree.say "Oh, [hero.name] - this was supposed to be a treat for me"
    $ game.pass_time(2)
    scene bg door restaurant with fade
    pause 0.3
    show bree date normal at center, zoomAt(1.5, (640, 1040)) with easeinleft
    mike.say "So, [bree.name] - how about catching that late movie, huh?"
    "[bree.name] looks up and her gaze meets mine."
    if not game.active_date.score >= 50:
        show bree dazed
        if ordered_desert:
            bree.say "You know what, I don't think that dessert agreed with me!"
            mike.say "Oh...really?"
            bree.say "Yeah, [hero.name]."
        bree.say "I'm sorry, but I'm actually starting to feel a bit sick!"
        mike.say "That's okay, [bree.name]."
        mike.say "Let's get you home as quick as we can."
        scene bg taxi with fade
        pause 0.5
        show bg taxi car with dissolve
        "With that, I hail a taxi to drive us back to the house."
        "Sure, it's a disappointment."
        "But I can't make [bree.name] stay out if she's not well."
        return
    show bree happy
    bree.say "Oh yeah - you try and stop me!"
    show bree normal
    mike.say "Great, [bree.name]."
    mike.say "Let's grab a taxi."
    scene bg taxi with fade
    pause 0.5
    show bg taxi car
    "With that, I hail a taxi to take us to the multiplex."
    "I can't wait to get there, as [bree.name]'s enthusiasm is infectious!"
    scene bg cinema
    show bree date normal at center, zoomAt(1.5, (640, 1040))
    with fade
    "When we make it to the lobby of the local multiplex, the place is still pretty busy despite the late hour."
    "[bree.name] and I hold hands as we weave through the throng of bodies, constantly in danger of being separated."
    "We're staring with interest at the colourful posters advertising what's currently showing."
    "And each one represents a different world of possibilities to escape into for the next couple of hours."
    "We deliberately chose not to decide upon what we were going to see beforehand."
    "Supposedly because we wanted to keep the whole thing spontaneous."
    "But the truth of the matter is that we just couldn't agree on a film we both wanted to see!"
    "And it seems like we still can't..."
    show bree evil
    bree.say "I really want to see that one, [hero.name]!"
    "[bree.name] points at the poster for a sappy-looking romcom."
    "I try not to groan and roll my eyes as I survey it for myself."
    show bree normal
    mike.say "I don't know, [bree.name]."
    mike.say "That guy with the teeth is in it."
    mike.say "And he makes me want to go postal!"
    show bree talkative
    bree.say "Aw, come on, [hero.name]."
    show bree smile
    bree.say "You laughed at him in that movie we watched the other night."
    bree.say "You remember - the one where they had to impersonate sumo wrestlers to escape the Yakuza?"
    show bree normal
    mike.say "Yeah, well...I must have been drunk or high or something!"
    mike.say "I want to see this one here."
    show bree annoyed
    "I gesture towards the poster for an action movie."
    "It's mostly explosions and cars flying through the air."
    show bree sad
    bree.say "Aw, not another macho action movie!"
    bree.say "They're so dumb they make me want to cry."
    show bree gloomy
    mike.say "This one's different, [bree.name]."
    mike.say "The director just came off doing that musical version of Jaws."
    show bree talkative
    bree.say "Yeah, and I cried at that too!"
    show bree sadsmile
    mike.say "Only because you felt sorry for the shark!"
    show bree talkative
    bree.say "Oh, I don't know - you choose one."
    show bree normal
    menu:
        "Action movie":
            $ game.active_date.score -= 10
            mike.say "Okay, [bree.name]."
            mike.say "The action movie it is."
            show bree sad
            bree.say "Aww, [hero.name]."
            bree.say "It IS my birthday!"
            show bree dazed
            "I smile at the pouting face [bree.name]'s pulling."
            mike.say "You let me choose, [bree.name]."
            mike.say "That means you can't sulk over my choice!"
        "Romcom":
            $ game.active_date.score += 15
            mike.say "I suppose it IS your birthday, [bree.name]."
            mike.say "So it wouldn't be fair to make you sit through my choice."
            show bree surprised
            bree.say "You mean we're doing the romcom?!?"
            show bree normal
            mike.say "Yes, [bree.name] - we're doing the romcom."
            show bree happy
            bree.say "Yay!"
            "The smile on [bree.name]'s face almost makes it worth the sacrifice."
            "But then I remember it'll be dark in the theatre."
            "So I won't be able to see it while I'm forced to watch the movie!"
    scene bg black
    show buy_popcorn_bg_04 as bg zorder 1 at center
    show buy_popcorn_vendor_04 as vendor zorder 2 at center
    show buy_popcorn_fg_04 as fg zorder 3 at center
    with fade
    pause 0.3
    show bree date normal zorder 4 at center, zoomAt(1.5, (340, 1040)) with easeinleft
    "As soon as we've bought our tickets, [bree.name] drags me over to the concession stand."
    "I baulk at the ludicrous prices, but then I remind myself of the occasion."
    "It can't hurt to let them rape my wallet on [bree.name]'s birthday - can it?"
    "She's already pointing at one of the largest tubs of popcorn they sell."
    "Oh god...this is going to hurt!"
    show bree talkative
    bree.say "We have to get some popcorn, [hero.name]."
    bree.say "And it has to be sweet too!"
    show bree normal
    menu:
        "Salty":
            $ game.active_date.score -= 10
            mike.say "I'll buy the snacks, [bree.name]."
            mike.say "But only on the condition that we have salted."
            show bree surprised
            bree.say "Salted?!?"
            show bree sad
            bree.say "Eww - barf city!"
            show bree gloomy
            mike.say "That's my offer, [bree.name]."
            mike.say "Take it or leave it."
            show bree vangry
            bree.say "Whatever, [hero.name]."
            bree.say "But I bet you're only doing this because you don't want to share!"
        "Sweet":
            $ game.active_date.score += 15
            mike.say "I normally prefer salted, [bree.name]."
            mike.say "But we're sharing - and if you don't like salted..."
            show bree vangry
            bree.say "Bleugh!"
            bree.say "I HATE it, [hero.name]!"
            show bree annoyed
            "I let out a resigned sigh."
            mike.say "Okay, I guess we should get sweet then."
            show bree happy
            bree.say "Thanks, [hero.name]."
            bree.say "And I promise I won't hog the tub too!"
    scene bg cinemaroom
    show bree date normal at center, zoomAt(1.5, (640, 1040))
    with fade
    "We find the theatre that our movie is showing in and locate our seats."
    show bree date normal at center, zoomAt(1.5, (640, 1140)) with ease
    "And once we've awkwardly shuffled along the row, we bed down and get ready to watch."
    scene bg cinemaroom at dark, blur(5)
    show bree date normal at center, zoomAt(1.5, (640, 1140))
    with dissolve
    "It's not long before the lights go down and the trailers begin to roll."
    "And then I hear a whisper in my ear."
    show bree talkative
    bree.say "Hey, [hero.name]!"
    show bree normal
    mike.say "What's up, [bree.name]?"
    show bree talkative
    bree.say "These trailers are SO old."
    bree.say "I already watched this one on my laptop, like yesterday!"
    show bree normal
    "Normally the trailers are one of my favourite parts of going to the movies."
    "But it seems like [bree.name]'s determined to blabber through them without stopping for breath!"
    menu:
        "Tell her to shut up":
            $ game.active_date.score -= 10
            mike.say "[bree.name] - will you shut up for a minute?!?"
            show bree lose
            show fx exclamation
            $ bree.sub += 5
            bree.say "Huh!"
            mike.say "I really want to see the trailer for the new Star Soldiers movie."
            show bree surprised
            bree.say "Oh...okay, [hero.name]."
            bree.say "I was just enjoying talking to you, that's all..."
            show bree sadsmile
            mike.say "Well we can talk after the movie."
            show bree talkative
            bree.say "Okay, I get the message."
        "Let her keep talking":
            $ game.active_date.score += 15
            show bree smile
            "I could tell [bree.name] to shut the hell up."
            "But it's her birthday, and I'm enjoying talking to her too."
            "So I let her prattle on."
            "Sure, it means missing the Star Soldiers trailer I was so desperate to see."
            "But she's more important to me than that."
            "And so it's a sacrifice I'm willing to make."
    show bree normal with fade
    "The movie starts a couple of minutes later, and we settle down into our seats."
    "I glance over briefly at [bree.name], wanting to see if she's okay."
    if game.active_date.score >= 80 and bree.sexperience >= 1:
        "But I see that she's not looking at the screen."
        "Instead her eyes are focused on me."
        "And she's already reaching across to put her hand on my crotch!"
        call bree_birthday_sex from _call_bree_birthday_sex
    else:
        "[bree.name]'s eyes are firmly focused on the screen."
        "And so I just take it that she's tuned into the movie quicker than I have."
        "But soon I'm lost in the experience too."
        "The next thing I know, the credits are rolling and we're headed for the lobby."
        scene bg street with fade
        "I hail a taxi to drive us home."
        "And then I make small talk with [bree.name] the whole of the journey."
    return

label bree_birthday_sex:
    $ game.room = "date_cinemaroom"
    scene bg cinemaroom at dark, blur(5) with fade
    "I look down at [bree.name]'s hand, no longer caring what's happening on the screen in front of me."
    show bree date flirt at center, zoomAt(1.5, (640, 1140)) with fade
    "But then I see that she's looking me straight in the eye, mischief written all over her face."
    "I try to keep my voice to a whisper as I speak, aware of all the other people in the theatre."
    mike.say "[bree.name]..."
    mike.say "What are you doing?!?"
    "[bree.name] doesn't bother to answer me at first."
    show bree happy
    "Instead she giggles quietly and begins to undo my zipper."
    mike.say "[bree.name]!"
    show bree flirt blush
    "My voice is a hoarse whisper by now."
    "And only partly from fear of someone else noticing what [bree.name]'s doing."
    "The rest is on account of me getting ever more turned on with each second that passes!"
    show bree smile
    bree.say "It's the popcorn, [hero.name]."
    show bree flirt at center, zoomAt(1.5, (640, 1240)) with ease
    "[bree.name] whispers to me as she lowers her head into my lap."
    show bree smile
    bree.say "It stand being more salty..."
    show bree flirt
    "I could tell her what an ordinary person would do in this situation."
    "That they just go back to the lobby and buy some salted popcorn instead!"
    "But where would the fun be in that?"
    "[bree.name] chuckles and looks up at me one last time as my cock comes free."
    "She doesn't do anything so obvious as wink."
    "But the intention is clear and can be read in her eyes all the same."
    "[bree.name] starts slowly, just holding my already stiff cock in her hand."
    "She strokes the base gently, barely licking the tip with her tongue."
    hide bree
    show bree cinema bj bree
    with fade
    "Her lips only come into play when she starts to travel downwards."
    "And she runs then down the sides in a smooth motion."
    "[bree.name] lets the saliva run out of her mouth, moistening the shaft."
    "So by the time she gets to the bottom, I can see it glistening in the near darkness."
    "Her hand takes a firmer hold now, fingers circling the shaft."
    "[bree.name] begins to work it, using the saliva to smooth the motion."
    "At the same time she sucks on one of my balls and then the other."
    "The feeling is so intense that it's all I can do to keep quiet."
    "I bite down on my lip, tasting the coppery tang of blood as I do so."
    "My hands feel like talons as they dig into the arms of my seat."
    "I know that I could cum like this."
    "With [bree.name] stroking my cock and sucking my balls."
    "But it seems like she has something else in mind."
    "And right now, I'm powerless to stop her!"
    "[bree.name] gives my cock one last squeeze with her hand."
    "Then her lips are on the way back up again."
    "This time it doesn't take her long to reach the top."
    "And I realise that this is because she wants it in her mouth."
    show sexinserts head bree zorder 1 at center, zoomAt(1, (720, 810))
    "[bree.name] swallows more of my cock in less time than I ever thought she could manage."
    "Her head is soon going up and down in my lap, bobbing like crazy."
    "I have absolutely no idea what's happening on the screen."
    "Instead my eyes are glued to the top of [bree.name]'s head."
    "She's going so fast and it feels so good right now."
    "I just know that I'm mere moments away from cumming."
    "And it seems like [bree.name] knows it too."
    "When the time comes, it doesn't surprise her in the slightest."
    show sexinserts head bree cum zorder 1 at center, zoomAt(1, (720, 810))
    show bree cinema bj cum
    with vpunch
    "She manages to keep from making all but the smallest gagging sounds."
    with vpunch
    "Which is impressive, as even I can't keep from expressing the sensation."
    with vpunch
    "And I do so in the most natural way possible."
    mike.say "Oh shit!"
    "Guy" "Shut up, man!"
    "Girl" "Yeah, I'm watching the movie here!"
    "I try to lower myself further down into my seat."
    "Thankful the whole time that no one figured out what actually caused my outburst."
    hide sexinserts
    hide bree
    show bree b date flirt blush at center, zoomAt(1.5, (640, 1140))
    with fade
    "By now, [bree.name]'s wrapping everything up."
    "She slips my wilting cock back into my pants and zips me up again."
    "And then she makes a show of spitting the contents of her mouth onto the popcorn."
    "I'm staring at her, eyes wide with amazement as she offers me some."
    "But when I shake my head, she just shrugs and settles down to watch the film."
    "I try to do the same."
    "But somehow I just can't seem to think of anything apart from what just happened."
    "And afterwards, I couldn't have told you what happened in the film to save my life."
    return

label bree_pregnant_request:
    "I know it's one of those guy things, yeah."
    "When you realise your girlfriend is beating around the bush."
    "But you just can't figure out what the hell it could be about."
    show bree at center, zoomAt(1.25, (640, 880))
    "[bree.name]'s got me in that position right now, and I'm stumped."
    show bree talkative
    bree.say "Ah, [hero.name]..."
    show bree normal
    mike.say "Yeah, [bree.name]?"
    show bree talkative
    bree.say "Are you happy with us?"
    show bree normal
    "That's one of those vague questions that turns a guy's guts to water."
    "What does she mean by that?"
    "As far as I knew, everything was going great between us."
    "There's no arguments and we're getting along fine with one another."
    "In fact, I was pretty sure that our relationship was solid as a rock."
    mike.say "Well..."
    mike.say "I don't know exactly what you mean, [bree.name]."
    mike.say "I've never been happier than I am right now."
    mike.say "And I thought you were too..."
    show bree sadsmile
    "[bree.name] shakes her head at this, as if alarmed by my reply."
    show bree talkative
    bree.say "Oh no...not like that!"
    bree.say "I am happy, [hero.name]."
    bree.say "It's just that..."
    bree.say "I'm happy NOW, you know?"
    show bree sadsmile
    mike.say "But you might not be in the future?"
    "[bree.name] shakes her head again."
    show bree happy at startle
    "But this time she laughs and a smile appears on her face."
    show bree smile
    bree.say "I'm not very good at this, am I?"
    show bree normal
    mike.say "Ah, I don't really know what this is, [bree.name]!"
    show bree smile
    bree.say "What I'm trying to say is that I've been thinking about the future."
    bree.say "Our future together, and what we want it to look like."
    show bree normal
    "Ah, now we're getting down to it."
    "This is all about commitment."
    mike.say "I want it to look like it does now, [bree.name]."
    mike.say "You and me together."
    show bree talkative
    bree.say "Is there room for anyone else in there too?"
    show bree normal
    mike.say "Well, I was kind of thinking that we'd be exclusive!"
    show bree flirt
    "[bree.name] gives me a gentle shove."
    show bree smile blush
    bree.say "No, you moron!"
    bree.say "I mean kids."
    bree.say "I think we should try to get pregnant!"
    show bree normal
    "My mouth drops open at the mention of kids."
    "But she's serious, I can see that in her eyes."
    "[bree.name]'s actually asking me to get her pregnant!"
    menu:
        "Agree":
            "I'm not prepared for this in the slightest."
            "But then what other good things was I not prepared for in my life?"
            "I didn't plan to have [bree.name] move in here and hit it off with her."
            "Likewise, I didn't plan to start dating her."
            "Or for us to fall in love."
            "This could be another one of those chances..."
            mike.say "Now you mention it, [bree.name]..."
            mike.say "That makes a lot of sense."
            show bree stuned blush
            "I see surprise and then delight appear on [bree.name]'s face."
            show bree surprised
            bree.say "Y...you do?!?"
            show bree happy -blush
            bree.say "I mean...that's great, [hero.name]!"
            show bree talkative
            bree.say "Oh, I was so worried you'd say no."
            bree.say "That you'd want to wait and plan it all out..."
            show bree normal
            "I shake my head, dismissing [bree.name]'s concerns."
            mike.say "Ah, don't worry about any of that stuff."
            mike.say "It's all just details that we can sort out later."
            mike.say "All that really matters is that we love each other."
            mike.say "And we'll love our kid just as much."
            show bree flirt at center, traveling(2.5, 0.3, (640, 1640))
            "[bree.name] throws her arms around me and hugs me tightly."
            "I return the gesture, already warming to the idea of being a dad."
            "I feel [bree.name] rest her head on my shoulder."
            "Her breath warm against my neck."
            show bree smile
            bree.say "So, next question."
            show bree happy
            bree.say "When do we start trying to get pregnant?"
            $ bree.love += 2
            $ bree.flags.pregrequest = True
        "Refuse":
            "I'm not prepared for this in the slightest."
            "It's far too big of a decision to have dropped on me like this."
            "Starting a family requires planning and preparation."
            "Just throwing caution to the wind wouldn't be fair."
            "Not on [bree.name] or myself, let alone our children!"
            mike.say "Don't get me wrong, [bree.name]."
            mike.say "I see kids in our future for sure."
            show bree gloomy
            "I can already see the disappointment on [bree.name]'s face."
            show bree sad
            bree.say "But not here and now?"
            bree.say "I...I just thought that things were going well..."
            show bree sadsmile
            mike.say "Like I said, [bree.name] - I want a family."
            mike.say "But I think we need to make a home first."
            mike.say "Once we're married with a place of our own..."
            show bree normal
            "[bree.name] nods, and I can see that she's trying to put a brave face on it."
            show bree sadsmile
            "But she can't fully hide the fact that I've put paid to her dream."
            show bree talkative
            bree.say "I...I guess that makes sense, [hero.name]."
            bree.say "I'll just have to wait a little longer."
            show bree sadsmile
            "I nod and smile, putting a brave face on too."
            "I just have to hope that [bree.name] can wait long enough."
            $ bree.love -= 2
    return

label bree_event_office_01:
    "My head's been totally into my work from the moment I sat down at my desk this morning."
    "I swear that I haven't looked up from my computer screen even once."
    "So when I hear someone calling me, I just assume it's one of the girls that works under me."
    bree.say "Hey there!"
    if Person.is_not_hidden("lavish"):
        mike.say "If that's Lavish, it'll be fine - well done."
    elif Person.is_not_hidden("audrey"):
        mike.say "If that's Audrey, it won't be fine - do it again!"
    elif Person.is_not_hidden("shiori"):
        mike.say "If that's Shiori, it doesn't matter - I'll do it myself!"
    "I hear a giggle in response to my reeling off my stock answers."
    "And that's something I'd never get from Lavish, Audrey or Shiori."
    "So I have no choice but to look up and see who's actually there."
    show bree casual happy at top_mostleft with dissolve
    bree.say "Hi, [hero.name]!"
    show bree normal
    "I stare at the sight of [bree.name] standing in the door of my office."
    "This just doesn't make sense - what's she doing here?"
    "It's like getting to class back in high-school and finding your mom teaching the class!"
    mike.say "[bree.name]?"
    mike.say "What are you doing here?"
    show bree happy at left with ease
    "[bree.name] giggles again and walks further into my office."
    "I can see that she's checking the place out as she does so."
    show bree talkative at left5 with ease
    bree.say "Oh, nothing..."
    bree.say "I was just passing by when I remembered this is where you work."
    bree.say "So I thought I'd drop in and say hi!"
    show bree normal at left4 with ease
    mike.say "You just walked straight in here?"
    mike.say "I thought we had security downstairs!"
    show bree talkative
    bree.say "You do, but I just told them I was here to see you."
    show bree smile
    bree.say "They were super nice and said I could come straight up."
    show bree normal at center with ease
    "[bree.name] stops in her tracks and I see her expression change."
    show bree annoyed
    "She frowns and cocks her head on one side as she regards me."
    show bree vangry
    bree.say "Hey...wait a minute..."
    bree.say "You don't sound like you're pleased to see me!"
    bree.say "Are you embarrassed by me being here?"
    show bree annoyed
    "I shake my head, trying to convince [bree.name] that she's wrong."
    "But maybe she's actually more than a little right."
    "[bree.name]'s not exactly the professional type, you know?"
    "And I do try to keep my home life separate from my work life."
    mike.say "No, [bree.name]!"
    mike.say "It's just that you..."
    mike.say "You kind of threw me by turning up unannounced, that's all."
    mike.say "If I'd have known, I'd have...organised a tour, or something."
    "[bree.name]'s still frowning as I finish up my hasty explanation."
    show bree normal
    "But she nods all the same, seeming to accept it for now."
    show bree talkative
    bree.say "Yeah...I guess so."
    bree.say "After all, you play videogames with me in your underwear at home."
    bree.say "So it'd be pretty weird if you couldn't cope with me being here!"
    show bree normal
    "I nod eagerly, happy to finally have a way out."
    "Maybe if I can distract [bree.name] for a little longer."
    "Then she'll likely get bored and want to leave."
    "That way I can actually get some damn work done!"
    dwayne.say "Did I miss a company-wide memo?"
    dwayne.say "Because I don't remember today being a dress casual day!"
    show dwayne annoyed at top_mostleft with easeinleft
    show bree surprised at vshake
    "At the sound of Dwayne's booming voice, [bree.name] and I both jump a little."
    show dwayne at left
    show bree at right4
    with ease
    "Neither of us saw him walk into my office."
    "Which for a guy of Dwayne's size is saying something!"
    mike.say "H...hi, Dwayne!"
    show bree normal
    mike.say "It's okay, she doesn't work here."
    show dwayne therock
    "Dwayne does that thing where he kind of frowns and raises one eyebrow."
    "And in that one gesture he lets me know that he's not happy with my explanation."
    "But at the same time he somehow manages to cause me to scramble to make amends."
    mike.say "Sure, sure..."
    mike.say "I should introduce you!"
    mike.say "Dwayne, this is [bree.name] - one of my housemates."
    mike.say "[bree.name], this is Dwayne - my boss."
    show bree angry
    "[bree.name] looks at me with an odd expression on her face."
    "One that wasn't there before I described her simply as my housemate."
    "I guess she thought I was going to say she was more than that to me."
    "But there's no time for her to question me."
    show dwayne at left5 with ease
    "As Dwayne takes the introduction as his cue to launch a full-on charm offensive."
    show dwayne shout
    dwayne.say "[hero.name]'s being humble on my behalf, [bree.name]."
    show dwayne smile
    dwayne.say "I'm not just his boss, I'm CEO of the WHOLE company!"
    dwayne.say "Everybody here works for me!"
    dwayne.say "I hope [hero.name] gave you the grand tour?"
    show bree evil
    bree.say "Oh no, he didn't!"
    bree.say "I think he said was too busy."
    show dwayne upset
    "Dwayne looks at me accusingly and shakes his head."
    show dwayne vangry
    dwayne.say "We're going to have to have words about hospitality, [hero.name]!"
    dwayne.say "A true gentleman always makes time for a beautiful lady, [bree.name]!"
    show dwayne normal
    "It takes a moment for the compliment to sink in."
    show bree happy blush
    "But then [bree.name] blushes and can't help giggling for a third time."
    show dwayne shout
    dwayne.say "Anyway..."
    show dwayne smile at left5 with move
    dwayne.say "I'd love to stay and chat, really I would."
    dwayne.say "But I have an appointment to keep."
    dwayne.say "Call my office, [bree.name]."
    dwayne.say "I'm sure I can find time to give you a personalised tour!"
    hide dwayne with easeoutleft
    "With that, Dwayne strides confidently out of my office."
    "The whole place seems oddly smaller once he's gone."
    "But I'm relieved to be free of his oppressive machismo all the same."
    show bree talkative -blush at center with ease
    bree.say "Ooh..."
    bree.say "He seems nice!"
    show bree normal
    mike.say "Yeah, [bree.name]..."
    mike.say "That's exactly the word I'd use to describe him...nice!"
    "I'm about to say more, to warn [bree.name] about Dwayne's habits."
    "But her phone makes a pinging sound, and she instantly picks it up."
    show bree surprised
    bree.say "Oops!"
    bree.say "I need to be somewhere else fast!"
    show bree smile at left4 with ease
    bree.say "See you back home later, okay?"
    show bree normal
    mike.say "Okay, [bree.name]..."
    mike.say "Take care, yeah?"
    show bree happy at top_mostleft with ease
    "[bree.name] smiles and nods, waving as she hurries out of my office."
    hide bree with easeoutleft
    "But I get the feeling she barely heard what I actually just said."
    "If she's not careful, she could end up another notch on Dwayne's headboard."
    "And by my reckoning, that thing's already more notches than board!"
    $ game.flags.breeoffice_delay = TemporaryFlag(True, 2)
    $ hero.replace_activity()
    return

label bree_event_office_02:
    "I'm sitting at my desk, working hard as always."
    "Well...maybe I'm working hard at pretending to look like I'm working hard!"
    "Either way, I'm killing it to anyone that happens to look in on me right now."
    play sound door_knock
    "But then I hear a loud knock at the door, and I look up from my work."
    mike.say "Erm, hey..."
    mike.say "Come on in!"
    "The moment the words are spoken, the door swings open."
    show dwayne happy at center, zoomAt(1.25, (240, 920)) with easeinleft
    "And Dwayne strides confidently into my office."
    show dwayne shout at center, zoomAt(1.25, (440, 920)) with ease
    dwayne.say "Good morning, [hero.name]!"
    dwayne.say "And how does the day find you?"
    show dwayne normal
    "I should be used to Dwayne barging in here like a force of nature by now."
    "But somehow he still manages to thrown me off balance when he does this to me."
    show dwayne at center, zoomAt(1.25, (640, 920)) with ease
    "I don't know if it's his alpha male persona or just the fact he's my boss."
    "All I do know is that it's something I hate!"
    mike.say "Ah..."
    mike.say "I guess it finds me well, Dwayne."
    mike.say "I mean it's not the best of days..."
    mike.say "But it's not the worst either!"
    show dwayne happy
    show dwayne at center, zoomAt (1.0, (640, 920)), startle(0.14,-20)
    pause 0.2
    show dwayne at center, zoomAt (1.0, (640, 920)), startle(0.14,-20)
    pause 0.2
    show dwayne at center, zoomAt (1.0, (640, 920)), startle(0.14,-20)
    "Dwayne lets out one of his hearty, rumbling laughs."
    show dwayne annoyed
    "Then he shakes his head and points a meaty finger at me."
    show dwayne shout
    dwayne.say "You talk so much without actually saying a damn thing, [hero.name]!"
    dwayne.say "I don't know how you do that!"
    show dwayne annoyed
    "Not knowing quite how to take that comment, I just smile."
    "Which seems to be more than enough of a response for Dwayne."
    show dwayne shout
    dwayne.say "Anyway, enough with the banter..."
    show dwayne normal
    mike.say "Was..."
    mike.say "Was that banter?"
    show dwayne shout
    dwayne.say "I said forget about it!"
    dwayne.say "What I wanted to talk to you about was your little visitor from the other day."
    show dwayne normal
    "I frown for a moment, not able to recall who Dwayne's talking about."
    "The past few days have been pretty busy on all fronts for me."
    "So it's not that easy to just call what he's asking about to memory."
    mike.say "Who do you mean, Dwayne?"
    show dwayne shout
    dwayne.say "I mean that sweet little housemate of yours, of course!"
    dwayne.say "Brie, wasn't she called?"
    show dwayne normal
    mike.say "Oh..."
    mike.say "You mean BREE!"
    show dwayne shout
    dwayne.say "Isn't that what I said?"
    dwayne.say "Anyway, never mind..."
    show dwayne smile
    dwayne.say "I think it's time we invited her back for that grand tour."
    dwayne.say "If you know what I mean..."
    show dwayne normal
    "Dwayne leans forward and winks at me as he says this."
    "I nod and smile in return."
    mike.say "You mean show her around the place, right?"
    mike.say "All the highlights of the office and more!"
    show dwayne annoyed
    "Dwayne rolls his eyes at me in sheer exasperation."
    show dwayne shout
    dwayne.say "No, you dummy!"
    dwayne.say "I mean I want to have some fun with her in my office!"
    dwayne.say "And I don't mean play boardgames either!"
    show dwayne normal
    mike.say "You mean you want to have SEX with [bree.name]?!?"
    show dwayne smile
    dwayne.say "Well done, [hero.name]."
    show dwayne shout
    dwayne.say "You got there in the end!"
    dwayne.say "Hell, you can even join in if you like."
    dwayne.say "How generous of an offer is that?"
    show dwayne normal
    menu:
        "I'll ask [bree.name] about the tour.":
            "Sure, I'm shocked that Dwayne would suggest such a thing to me."
            "But the more I think about it, the less weird it starts to sound."
            "All he's really asking me to do is put out feelers towards [bree.name]."
            "There's no pressure on anyone involved, no blackmail or anything like that."
            "Surely the worst that could happen is [bree.name] saying no."
            mike.say "Okay, Dwayne..."
            mike.say "I'll ask [bree.name] the first chance I get."
            show dwayne smile
            "Dwayne's face breaks into a wide smile."
            "And he shows off his large, rather disturbingly white teeth."
            show dwayne happy
            dwayne.say "That's my boy!"
            dwayne.say "I knew I could count on you!"
            show dwayne smile
            "Dwayne clicks his fingers and points at me as he leaves."
            hide dwayne with easeoutleft
            "And once he's gone, I swear I can still feel his presence in the room."
            "It's like it lingers in his wake for a few minutes after he passes through."
            $ game.flags.officebree = True
        "Sorry, but no.":
            "I'm shocked that Dwayne would even suggest such a thing to me."
            "I know that he has a reputation around the office for being a flirt."
            "But I'm not going to offer [bree.name] up to him on a silver platter!"
            "Still, I need to handle this as delicately as I can."
            "Dwayne's my boss, so I can't just let him have it."
            mike.say "I think I misheard you just now, Dwayne."
            mike.say "So I'll let you tell me again what you wanted me to do."
            mike.say "Because I might get confused and assume you asked me to do something...unprofessional?"
            show dwayne therock
            "Dwayne does that thing where he raises his eyebrow again."
            "And I know from the fact that he's not talking that he's calculating the odds."
            show dwayne smile
            "Then, without warning, his face breaks into a wide smile."
            "And he shows off his large, rather disturbingly white teeth."
            show dwayne happy
            dwayne.say "You know what, [hero.name]..."
            dwayne.say "You're not the only one that got confused just now."
            dwayne.say "I can't even remember what I was asking you to do!"
            show dwayne shout
            dwayne.say "So let's just forget about it, okay?"
            show dwayne annoyed
            "Dwayne clicks his fingers and points at me as he leaves."
            hide dwayne with easeoutleft
            "And once he's gone, I swear I can still feel his presence in the room."
            "It's like it lingers in his wake for a few minutes after he passes through."
            $ game.flags.worksatisfaction = 0
        "No fucking way!!!":
            "I'm shocked that Dwayne would even suggest such a thing to me."
            "I know that he has a reputation around the office for being a flirt."
            "But I'm not going to offer [bree.name] up to him on a silver platter!"
            "Somebody needs to stand up to this guy."
            "And I guess it's going to have to be me!"
            mike.say "Like hell I will, Dwayne!"
            mike.say "I'm not going to let you get your hand on [bree.name]."
            mike.say "You just want to use her and then throw her aside - like you always do with women!"
            show dwayne upset
            "Dwayne slowly crosses his arms over his wide chest."
            "And he regards me with a stony frown on his face."
            show dwayne shout
            dwayne.say "Is that so, [hero.name]?"
            show dwayne vangry
            dwayne.say "Well, I have to say that I'm disappointed in you."
            dwayne.say "I thought that you understood how things work around here."
            show dwayne upset
            "I do the best I can not to let Dwayne intimidate me."
            "Which is easier said than done when you're this close to him!"
            mike.say "Say what you like, Dwayne."
            mike.say "I still won't do it."
            show dwayne therock
            "Dwayne does that thing where he raises his eyebrow again."
            "And I know from the fact that he's not talking that he's calculating the odds."
            show dwayne smile
            "Then, without warning, his face breaks into a wide smile."
            "And he shows off his large, rather disturbingly white teeth."
            show dwayne happy
            dwayne.say "Okay, [hero.name], okay."
            dwayne.say "That's the way you want to play it, then fine."
            show dwayne shout
            dwayne.say "But I won't forget this, you can be sure of that."
            show dwayne upset
            "Dwayne clicks his fingers and points at me as he leaves."
            hide dwayne with easeoutleft
            "And once he's gone, I swear I can still feel his presence in the room."
            "It's like it lingers in his wake for a few minutes after he passes through."
            $ game.flags.worksatisfaction = 0
            if game.flags.promoted > 4:
                $ game.flags.promoted = 4
            else:
                $ game.flags.promoted = 0
            $ bree.sub += 3
    $ hero.replace_activity()
    return

label bree_event_office_03:
    "It's only when I get back home after speaking to Dwayne that I realise I have no idea how to do this."
    "Am I supposed to just walk up to [bree.name] and ask her if she wants to come to my office and fuck the guy?"
    "Or should I try to drop it into casual conversation if the chance comes along?"
    "Yeah, like that's going to happen!"
    "[bree.name]'s going to be reeling off a list of random guys she wants to fuck."
    "And I just happen to overhear her and mention that Dwayne's well up for it!"
    "I don't think so!"
    "But maybe there's a third option."
    "Maybe I can bring Dwayne up and then steer the conversation in that direction?"
    "It's the only solid plan that I have, so I decide to give it a chance."
    show bree at center, zoomAt(1.25, (640, 880)) with dissolve
    "So, here goes nothing..."
    mike.say "Ah, [bree.name]..."
    show bree surprised
    bree.say "Yeah, [hero.name]?"
    show bree stuned
    mike.say "You enjoyed your little visit to my office the other day, right?"
    "[bree.name] looks more than a little puzzled at this."
    show bree normal
    "But she smiles and nods all the same."
    show bree talkative
    bree.say "I guess so, [hero.name]."
    bree.say "But it really was a little visit."
    bree.say "I only got to see the inside of your office!"
    show bree normal
    "I shake my head at this."
    mike.say "That's not exactly true, [bree.name]."
    mike.say "You got to meet Dwayne."
    mike.say "And he's the guy in charge of the whole place!"
    show bree annoyed
    "[bree.name] lets out a grunt at the mere mention of that name."
    show bree talkative
    bree.say "Oh yeah..."
    bree.say "THAT guy!"
    bree.say "He's the boss alright."
    bree.say "And doesn't he love everyone to know it!"
    show bree normal
    mike.say "Yeah, well..."
    mike.say "Dwayne was asking me about you today."
    show bree stuned
    "[bree.name]'s eyebrows shoot up at the mention of this."
    "Suddenly she seems more interested in what I have to say."
    show bree surprised
    bree.say "He did?"
    bree.say "What did he say about me?"
    show bree stuned
    "I can't believe the sudden change in [bree.name]'s attitude."
    "A moment ago she was acting like she hated Dwayne's guts."
    "And yet now she's desperate to know what he said about her!"
    mike.say "Do you really care that much, [bree.name]?"
    mike.say "I got the impression you thought he was a jerk?"
    show bree sadsmile
    "[bree.name] seems to realise the dilemma she's put herself in."
    show bree evil
    "She bites her lip and looks everywhere but at me."
    "Then she lets out a gasp of frustration."
    show bree hesitating
    bree.say "Urgh..."
    bree.say "Okay, okay...your boss is hot!"
    bree.say "There, I said it!"
    bree.say "But he's not the kind of guy you can let know you think he's hot!"
    show bree sadsmile
    "[bree.name] must see the look of confusion on my face."
    "Because she shakes her head at me before she goes on."
    show bree talkative
    bree.say "Never mind, [hero.name]."
    bree.say "Just tell me what Dwayne said, yeah?"
    show bree normal
    mike.say "Erm..."
    mike.say "He wanted to invite you back to the office for that tour he mentioned."
    show bree annoyed
    bree.say "Hmm..."
    show bree talkative
    bree.say "Well that sounds pretty innocent."
    show bree normal
    mike.say "Yeah, but in Dwayne's terms, that means something else."
    mike.say "It kind of means that he wants to get it on with you, in his office!"
    show bree stuned
    "[bree.name]'s eyes pop wide open in shock at this revelation."
    "And I wait with baited breath for her reaction..."
    show bree surprised
    if bree.sub >= 75:
        bree.say "You're fucking serious?"
        bree.say "He asked you to ask me to have sex with him?"
        show bree stuned
        mike.say "Well, he kind of included me in the deal too!"
        "[bree.name] blinks and shakes her head."
        show bree talkative
        bree.say "I...I guess I should be flattered!"
        bree.say "It's not every day I get propositioned by a guy like that!"
        show bree flirt
        "I'm still waiting for [bree.name] to actually say yes."
        "For some reason I can't consider the deal done until she has."
        mike.say "And that's a good thing, right?"
        mike.say "Which means you're saying...what, exactly?"
        show bree smile
        bree.say "I'm saying what the hell, [hero.name]."
        bree.say "How boring would I be if I turned down an offer like this?!?"
        show bree normal
        mike.say "That's great, [bree.name]!"
        mike.say "Leave all the details to me..."
        "And just like that, it's all arranged."
        $ hero.calendar.add(game.calendar.get_next_day_of_week("wednesday"), LabelAppointment(14, "bree", "Office Tour", "bree_event_office_04", "missed_bree_event_office_04"))
    elif bree.sub >= 25:
        bree.say "You're fucking serious?"
        bree.say "He asked you to ask me to have sex with him?"
        show bree annoyed
        mike.say "Well, he kind of included me in the deal too!"
        show bree angry
        "[bree.name] raises one eyebrow at this."
        "She's looking at me like I have steaming turds hanging out of my mouth."
        show bree vangry
        bree.say "Yeah, I should have asked what was in it for you!"
        bree.say "Now listen to me, [hero.name]."
        bree.say "You can tell Dwayne to drop dead."
        bree.say "I wouldn't sleep with him if you paid me!"
        hide bree with easeoutright
        "With that, [bree.name] turns and walks away."
        "Which leaves me with my answer."
        "Though I'm pretty sure Dwayne's not going to like it!"
        $ bree.love -= 20
        $ game.flags.officebree = False
    else:
        show bree vangry at vshake
        bree.say "HE WANTS TO DO WHAT?!?"
        show bree angry
        "[bree.name] bellows straight in my face."
        show bree vangry
        bree.say "You go right back there and tell him to go to hell!"
        bree.say "And you can go there with him too for even asking me!"
        hide bree with easeoutright
        "With that, [bree.name] turns and walks away."
        "Which leaves me with my answer."
        "Though I'm pretty sure Dwayne's not going to like it!"
        $ game.flags.officebree = False
        $ bree.love -= 50
        $ bree.sub -= 25
    return

label missed_bree_event_office_04:
    if game.flags.dwaynedead:
        return
    "Shit I missed the office tour planned by Dwayne."
    $ bree.love -= 5
    $ game.flags.worksatisfaction -= 20
    $ hero.calendar.add(game.calendar.get_next_day_of_week("wednesday"), LabelAppointment(14, "bree", "Office Tour", "bree_event_office_04", "missed_bree_event_office_04"))
    return

label bree_event_office_04(appointment=None):
    if game.flags.dwaynedead:
        return
    scene bg office
    "I have to confess that I'm pretty nervous as [bree.name] and I ride the elevator up to Dwayne's office."
    "Part of me still can't believe that she actually said yes when I asked her to do this."
    "Hell, that same part of me still can't believe I even asked her in the first place!"
    "But we're here now, and I guess that we're doing this thing, for better or worse."
    "I got a good few stares from female colleagues on the way up here too."
    "People like Aletta, who know all too well what kind of things Dwayne gets up to."
    "They're the ones I'm going to have a hard time explaining this to."
    "But as we reach the doors of Dwayne's office, I try to push all of that aside."
    "This is supposed to be fun for everyone involved, right?"
    "I make to get the door for [bree.name], but it swings open in front of me."
    scene bg ceo
    show dwayne at right4
    with fade
    "And there's Dwayne behind it, large as life and twice as unctuous."
    show dwayne happy
    show bree b casual evil blush at top_mostright with easeinright
    dwayne.say "[bree.name], [hero.name]..."
    dwayne.say "Hello!"
    dwayne.say "It's so good to see you again - especially you, [bree.name]!"
    show dwayne smile
    show bree happy
    "[bree.name] can't help but smile and giggle at this."
    "And I have to hand it to Dwayne."
    "He might be a womaniser that's got all the loyalty of a sewer rat."
    "But he does know how to put the charm on when the need arises."
    bree.say "He, he..."
    show bree smile
    bree.say "Hello to you too, Dwayne!"
    show bree normal at left with ease
    "Without asking to be invited in, [bree.name] hurries past Dwayne and into the office."
    "But he seems pleased with her enthusiasm, turning to follow her as she does so."
    "This leaves me to squeeze through the door before it closes and strands me outside."
    show bree surprised
    bree.say "Ooh..."
    bree.say "Is ALL of this your office, Dwayne?"
    show bree happy
    bree.say "It's like bigger than an entire apartment!"
    show bree flirt
    show dwayne smile
    "Dwayne has his hands planted on his hips and a huge grin on his face."
    "I can see how much he's getting off on [bree.name] being impressed by his office."
    "So much so I'm surprised he doesn't have organised tours through here all the time!"
    show dwayne happy
    dwayne.say "Yeah, [bree.name]."
    dwayne.say "All of this is me!"
    dwayne.say "I need room to stretch out."
    dwayne.say "And I don't like to share either!"
    show bree happy
    "As [bree.name] descends into another round of giggles, I decide it's time for me to speak up."
    "After all, I am supposed to be getting involved in the action here too!"
    "At this rate, Dwayne and [bree.name] are going to forget I'm even in the same room as them."
    mike.say "Ahem..."
    "Dwayne and [bree.name] both stop what they're doing and look in my direction."
    show dwayne annoyed
    show bree normal
    "And suddenly I find that being the centre of attention is more daunting than I expected."
    mike.say "Are we here so you can give [bree.name] a tour of your office, Dwayne?"
    mike.say "Because I thought you had something a bit more physical in mind."
    "For a moment I think Dwayne's going to react badly to my intervention."
    "Like maybe he's going to use his alpha male powers to put me in my place."
    "But luckily for me, it seems like he's still playing Mr Niceguy for [bree.name]'s sake."
    show dwayne shout
    dwayne.say "Of course, of course..."
    show dwayne happy
    dwayne.say "You see that's why I like having you around, [hero.name]."
    dwayne.say "You keep me grounded, focused on the task at hand."
    show dwayne normal
    "He turns to [bree.name] and then slaps the top of his desk with one hand."
    show dwayne happy
    dwayne.say "I think we all know why you're here, [bree.name]."
    dwayne.say "So why don't you pull down those little panties of yours."
    dwayne.say "And then climb up on this desk to provide some...corporate relief?"
    show dwayne smile
    show bree happy
    "[bree.name] nods happily as she walks over to the desk."
    "And she's already starting to take off her clothes as she does so."
    show bree smile blush
    bree.say "Okay, guys."
    bree.say "But how about we start out with a little strip-tease?"
    show bree flirt
    "Dwayne nods eagerly, then shoots me a sideways glance."
    "He winks at me, before turning his attention back to [bree.name]."
    "Though I can't tell if he's thanking me for making this happen."
    "Or else he's gloatingly reminding me that he told me so."
    "I keep my mouth shut and wait for him to turn his attention back to [bree.name]."
    "Only then do I shake my head and roll my eyes."
    "[bree.name] makes a good show of stripping off her clothes."
    "She drags it out and teases each piece coming off."
    show bree underwear with dissolve
    "Then she tosses them aside as she gets down to her underwear."
    show bree topless with dissolve
    "Next to go is her bra, then she pulls down her panties."
    show bree naked with dissolve
    "Finally naked, she jumps onto the desk."
    scene bg black
    show bree threesome dwaynemike
    with fade
    "Then she stands there, on her hands and knees."
    bree.say "Well?"
    bree.say "What are you waiting for?"
    bree.say "Come and get me!"
    "Dwayne lets out one of his best, rumbling laughs as he pulls at his tie."
    "He takes a step forwards and then seems to remember his manner for once."
    "He's standing behind [bree.name], so I guess he's claimed that end for himself."
    show bree threesome dwaynemike dwayne
    "So it looks like that just leaves me with the other end to play with."
    "Not that I can't have some fun with [bree.name]'s mouth!"
    show bree threesome dwaynemike mike
    "I take another look at Dwayne before we get started."
    "And I see that he's sliding a hand up and down his rather impressive cock."
    "As he does so, Dwayne gives me a knowing smile."
    "Then he grabs [bree.name] by the haunches and pulls her backwards."
    bree.say "Oh...hello!"
    "A moment later, Dwayne finds the mark with his cock."
    show bree threesome dwaynemike vaginal pleasure
    bree.say "Oooh...helllooo!"
    "I can hear something melting in [bree.name]'s voice as she says those words."
    "And I can only imagine that something similar is happening to her pussy at the same time too!"
    "Dwayne doesn't hold back for a moment, he pushed himself straight into [bree.name]."
    "She quivers and moans as he makes sure to get all the way inside of her."
    "And then he holds himself there for a moment, savouring the feeling."
    dwayne.say "How does it feel, [bree.name]?"
    show bree threesome dwaynemike normal
    dwayne.say "How does it feel to have something that big inside of you?"
    dwayne.say "Pretty fucking amazing, huh?"
    "[bree.name] nods desperately, gasping with each breath she takes."
    bree.say "Y...yes..."
    bree.say "It feels..."
    bree.say "So good...so good!"
    "Dwayne lets out another peal of rumbling laughter."
    "Then he begins to move inside of [bree.name]."
    "He goes slowly at first, but soon starts to pick up speed."
    "And soon enough, he's literally hammering away at her."
    "All the time, [bree.name]'s looking up at me, holding my eye."
    "To me it looks like she was telling the truth, that she's loving it."
    "But there's something else in her gaze, something imploring me to take action."
    "Still only half stripped-off, naked below the waist, I step closer to her."
    show bree threesome dwaynemike close
    "The moment [bree.name] spots my cock, jutting from below my shirt, she makes her move."
    "She takes it in her hand and leans her head forwards."
    "Before I can say a word, she's licking away at the tip."
    "Not that I was ever going to try and stop her, you understand?"
    "If that's what [bree.name] wants right now, then that's what she's going to get!"
    "It's a sacrifice I'm willing to make for her sake."
    "I move forwards until I'm almost standing against the side of the desk."
    "And [bree.name]'s quick to take full advantage of this."
    show bree threesome dwaynemike suck
    "In a matter of seconds, she has my cock fully in her mouth."
    "Then she's working away as if her life depended on it."
    "All the time, [bree.name]'s looking up at me, holding my eye."
    "I can feel the way her body's moving as Dwayne fucks her."
    "And I can see the pleasure she's feeling from his cock being inside her."
    "All of this seems to make [bree.name] all the more eager to pleasure me in turn."
    "Maybe this isn't so bad after all?"
    "Maybe what I really need to do is focus on the end result?"
    "Sure, Dwayne's getting off on fucking [bree.name] right now."
    "But all of that energy she's channelling into sucking my cock, not his."
    show bree threesome dwaynemike pleasure
    "So in a crazy, roundabout kind of way, I'm the one getting the best end of the deal."
    "I mean, think about it for a moment."
    "Dwayne and [bree.name] are sweating away like crazy."
    "And here I am, just standing still and reaping all the benefits!"
    "For the first time since all of this got started, I can feel myself starting to smile."
    "It's a wry grin, but I can't help it."
    "I just hope that nobody calls me on it!"
    dwayne.say "Hey..."
    dwayne.say "Is that a smile I see on your face, [hero.name]?"
    dwayne.say "I told you this thing was going to be worth it!"
    dwayne.say "Stick with me, and you'll reap the rewards, kid!"
    "What can I do but nod and keep on smiling in response to that?"
    "I resolve to let Dwayne think he's the one pulling all the strings here."
    "That way I can keep on letting him believe I'm just following his orders."
    "Sooner or later, a guy like that's going to slip up, big time."
    "And when he does, it'll pay to have the dirt on him..."
    dwayne.say "Whoa..."
    show bree threesome dwaynemike normal
    dwayne.say "Settle down there, [bree.name]!"
    dwayne.say "I think our little filly's about to lose it!"
    "I look down to see that [bree.name] has my cock almost all the way into her mouth."
    "Any deeper and she's going to need help to keep breathing!"
    "But her eyes are losing focus at the same time."
    "I think Dwayne might be right - [bree.name]'s about to cum!"
    dwayne.say "Right on time, baby!"
    dwayne.say "Here I come too!"
    "I try as best I can to keep my eyes on [bree.name] during what follows."
    show bree threesome dwaynemike creampie ahegao with hpunch
    $ bree.sub += 2
    "Dwayne shoots his load into her, grunting and groaning the whole time."
    with hpunch
    "It goes on so long and he makes such a show of it that I think it'll never end."
    with hpunch
    "But one thing it does manage to do is push [bree.name] over the edge too."
    "She still has my cock in her mouth as it happens."
    "And the helpless expression on her face is just too much."
    "I feel it triggering my orgasm too!"
    menu:
        "Cum in her mouth":
            "I don't want to snap [bree.name] out of the rhythm she's established."
            "And I'm guessing she must be ready for what happens next."
            with hpunch
            "So I keep my cock firmly in her mouth as I feel myself start to cum."
            show bree threesome dwaynemike cum inmouth normal with hpunch
            "[bree.name]'s eyes pop open a moment later, and she struggles for a moment."
            "This makes me think I misjudged the situation."
            "But a moment later I see her recover and regain her composure."
            show bree threesome dwaynemike -close -cum pleasure
            "Then she swallows everything that I have without error."
        "Pull out":
            "I feel like I need to put my stamp on what's happening here."
            "Dwayne just got to shoot his load into [bree.name]."
            "So I need to do something that's almost as impressive myself."
            "That's why I make a point to pull my cock out of [bree.name]'s mouth before it's too late."
            "[bree.name]'s eyes pop open in surprise and she gags as I yank it free."
            show bree threesome dwaynemike -close cumshot_mike normal cum onface with hpunch
            "But there's no time for an explanation, as I cum a moment later."
            with hpunch
            "[bree.name]'s face is spattered from forehead to chin with semen."
            show bree threesome dwaynemike cum onface -cumshot_mike pleasure with hpunch
            "And she gets a good portion in her mouth too."
    "Afterwards, as we all get cleaned up, Dwayne seems to be walking on air."
    "He's all smiles and compliments as we put our clothes back on and prepare to leave."
    scene bg ceo
    show dwayne happy at left
    show bree casual blush at right
    with fade
    dwayne.say "That was a hell of a way to pass the time, you guys!"
    dwayne.say "Way better than a damn game of golf!"
    dwayne.say "We should do it again sometime - and soon!"
    show dwayne smile
    mike.say "Ah..."
    mike.say "Yeah, Dwayne - sure thing."
    show bree happy
    bree.say "We should all compare diaries!"
    scene bg firstfloorbathroom at center, zoomAt(3.5, (900, 2000))
    show bree casual at center, zoomAt(1.5, (640, 1040))
    with fade
    "As [bree.name] and I ride the elevator down from Dwayne's office, we remain silent."
    "Maybe what we did was so big that we really don't need to chat about it."
    "Or maybe I'm fooling myself, and I just dragged [bree.name] into something weird."
    "Something that's going to make things between us super-awkward from now on."
    "If that's the case, then I suppose that I should be grateful I got a bj out of it."
    "Even if [bree.name] never wants to talk to me again!"
    return

label bree_morningwood:
    "I don't know why I wake up with her on my mind, but the first thing I think of is [bree.name]."
    "Guess I must have been dreaming about her, or at least thinking of her as I fell asleep last night."
    "And when I say that I'm thinking about [bree.name], I don't mean I'm contemplating her winning personality."
    "Let me put it this way - I have an almost painful case of morning wood, and she's to blame!"
    menu:
        "Try to ignore the inconvenience":
            $ hero.fun -= 5
            $ hero.cancel_event()
            return
        "Let [bree.name] know what she's responsible for":
            pass
    "So when I thrown back the covers and swing my legs out of bed, I'm practically on a mission."
    "I hurry to my bedroom door and slip out into the corridor."
    scene bg secondfloor with fade
    "Luckily for me, there's nobody else up and about yet."
    "That means I can sneak over to [bree.name]'s bedroom door without being seen."
    "With one hand on the handle, I take a last look around."
    "Then I open it and slide through it at the narrowest angle I can manage."
    scene bg bedroom2 with fade
    "Once I'm inside and I have the door closed behind me, I lean against it."
    "And then I start to scan [bree.name]'s room, contemplating my next move."
    "Of course I can see her bed from here."
    show sleep bree with fade
    "And the shape under the covers tells me that she's still in it."
    "In the quiet of [bree.name]'s bedroom I can also hear the sound of her breathing."
    "It's slow and steady, not quite a snore, but enough to suggest she's asleep."
    "In fact, I can just about make out [bree.name]'s head on the pillows."
    "But she has the covers pulled up all the way to her chin."
    "Which means all I can see is her blonde hair peeking out at the top!"
    "No matter, because what I have in mind doesn't use that end of the bed anyway."
    "I hastily pull off the clothes I was sleeping in and toss them aside."
    "Then I get down on all fours and crawl towards [bree.name]'s bed."
    "When I reach the foot of the bed, I lift the covers over my head."
    "Slowly and carefully I climb up and onto the bed."
    "I try as hard as I can to keep from waking [bree.name] as I do so."
    "But more than once I find myself freezing in place as stirs in her sleep."
    "This means that I spend the next few minutes inching up and onto the bed."
    "And then I begin to climb over [bree.name] too, making for the head of the bed."
    "This is hard not only because I have to be sure not to wake her."
    "It's also made worse by the fact that I'm literally touching [bree.name] the whole time."
    "That perfect body is spread out before me, just begging to be touched."
    "But I have to steel myself and ignore it if I want to pull this off."
    "At least [bree.name] makes things easier for me by being laid on her back."
    "This means that I can position myself on top of her with relative ease."
    "Looking down on her, I'm struck by just how beautiful she is."
    "She looks so peaceful and serene too, like a fairy-tale princess."
    "I don't know how it happens, but [bree.name] chooses right now to begin stirring."
    "Maybe I made too much noise or I didn't keep still enough."
    "But whatever the cause, she slowly opens her eyes."
    bree.say "Ooooh..."
    scene bg black
    show bree spoon bedroom2 mouth_pleasure eyes_pleasure
    with fade
    bree.say "Oh...morning, [hero.name]!"
    bree.say "What are you doing here?"
    bree.say "I don't remember falling asleep with you here."
    "I'm relieved to hear no trace of annoyance in [bree.name]'s voice."
    "Sure, she sounds sleepy and confused as she's waking up."
    "But there's more interest and amusement in there than anything else."
    mike.say "I...I guess I wanted to surprise you, [bree.name]."
    mike.say "I woke up and I couldn't get you out of my mind."
    "Suddenly I feel something brush against my cock."
    "Then I gasp as [bree.name]'s hand takes a firm hold of it."
    bree.say "Ha, ha!"
    bree.say "I see what you mean!"
    bree.say "Hmm...is all of that for me?"
    "I nod desperately, enjoying being handled by [bree.name]."
    "And I'm getting more excited by the moment."
    "Specifically because I can feel her other hand under the covers too."
    "It's hastily pulling down her panties!"
    bree.say "Then I guess I should put it to good use!"
    bree.say "Don't you think so?"
    "I nod eagerly as [bree.name] giggles."
    "And the look on her face is priceless too."
    "She's trying to direct traffic down there."
    "But she can't see what she's doing under the covers."
    "The result is that my cock slides here and there, out of control."
    bree.say "Ooh..."
    show bree spoon eyes_surprised vaginal
    bree.say "Mmm..."
    bree.say "Damn it!"
    "Suddenly I feel like I'm in just the right spot."
    "And I decide to take matters into my own hands while I'm there."
    "I position myself, and then I push forwards and down..."
    scene bree missionary
    show bree missionary bedroom2 vaginal
    bree.say "Oh shit..."
    mike.say "Oh holy shit!"
    "[bree.name]'s the one nodding now, eyes wide as I sink into her."
    "I can feel her pussy surrendering to me at the same time."
    "And I don't stop until I'm all the way in there too."
    "I could start pounding [bree.name] right now, go as fast and hard as I can."
    "But instead I choose to go slow and deep, savouring every moment."
    "The sensation of being inside her is incredible."
    show bree missionary pleasure
    "And there's no way any dream of [bree.name] could be this good."
    "Her head is laid back on the pillow, her eyes closing."
    "But I know that [bree.name]'s in no danger of falling back asleep."
    "That's because I can feel her moving under me, pushing herself upwards."
    "And I can hear the sound of her moaning with pure, unashamed pleasure."
    "[bree.name] lies back, giving herself over to me and to the experience."
    "She reclines on the bed, offering no resistance whatsoever."
    "For me, this means that I'm laid more on her than the bed beneath us."
    "[bree.name]'s thighs feel like cushions beneath me."
    "Her belly is soft and warm against mine."
    "And her breasts are like a couple of sweet pillows!"
    "Everything is moving beneath me, rising and falling."
    "In fact, [bree.name]'s entire body is quivering with every slow thrust I make."
    "She's still moaning, letting out little gasps of pleasure."
    "And a fine sheen of perspiration is appearing on her skin."
    show bree missionary normal
    "Suddenly I see that her eyes are open once more."
    "And it looks like she's trying to attract my attention."
    "I lean in closer to hear what [bree.name] has to say."
    bree.say "Uhh..."
    bree.say "[hero.name]..."
    bree.say "You're going to make me cum!"
    "[bree.name] grabs hold of me as she says this, her orgasm already beginning."
    "At the same time as her arms and legs do this, her pussy squeezes me too."
    show bree missionary pleasure
    "The sensation is so sudden and intense that I can't help being swept along with her."
    with hpunch
    "I lean forwards, pushing my weight down onto [bree.name]."
    with hpunch
    "This means that when I lose it, I'm all the way inside her."
    show bree missionary cum ahegao with hpunch
    "Together we ride it out, each making it that much more intense for the other."
    "Even afterwards, [bree.name] clings to me, keeping my cock inside her as long as she can."
    "Not that I'm complaining, as I'd stay here all day long if I could."
    $ bree.sexperience += 1
    $ game.room = "secondfloor"
    $ hero.flags.morningwood = TemporaryFlag(True, "day")
    return


label bree_stripclub_intro:
    show bree
    with fade
    "The date that [bree.name] and I have just been on couldn't have gone better from my point of view."
    show bree happy
    "[bree.name] was laughing at my jokes and hanging onto every word of the stories that I told her."
    "And it'd not like I was the only one on form either, because she's been a delight all night."
    show bree normal
    "It's times like this when I'm so glad that we decided to give this relationship a real go."
    "That we took a chance on becoming more than just housemates and platonic friends."
    show bree smile
    bree.say "So..."
    bree.say "What do you want to do now?"
    show bree normal
    "[bree.name] shrugs as she asks me the question."
    show bree talkative
    bree.say "You want to go home?"
    bree.say "Or head somewhere else?"
    show bree normal
    "I don't even need to think about my answer."
    "The words just come straight out of my mouth."
    mike.say "I don't want to go home, [bree.name]!"
    mike.say "I'm having a great time."
    "I think about where we could go next, but nothing springs to mind."
    "And it doesn't look like [bree.name] has any ideas of her own either."
    "It's just then that I get what feels like a flash of inspiration."
    mike.say "This is going to sound a little crazy, [bree.name]..."
    mike.say "But hear me out, okay?"
    "[bree.name] nods, waiting patiently to hear what I have to say."
    mike.say "Let's go to the first place we see around the corner, yeah?"
    mike.say "No matter what it is, we do it!"
    show bree hesitating
    bree.say "Are you serious?"
    show bree normal
    mike.say "Totally, serious!"
    mike.say "Restaurant, cinema, theatre or rodeo - we just do it!"
    show bree happy
    bree.say "Okay, you're on!"
    show bree normal at center, zoomAt(1.5, (640, 1040)) with fade
    "[bree.name] grabs hold of my hand and we hurry around the corner."
    "I can feel the excitement building up inside of me."
    show bg alley
    show bree normal at center, zoomAt(1.5, (640, 1040))
    with fade
    "That is until I see what awaits us."
    show bree surprised
    bree.say "Oh..."
    bree.say "Oh my!"
    show bree stuned
    mike.say "Yeah..."
    mike.say "Maybe around the next corner instead?"
    show bree wink
    bree.say "No way - we made a pact!"
    show bree normal
    "I look at [bree.name] in amazement."
    mike.say "But, [bree.name]..."
    mike.say "That's a strip-club!"
    mike.say "And it's open pole night!"
    show bree happy
    bree.say "Like I said, [hero.name]…"
    bree.say "We made a pact!"
    scene bg stripclub with fade
    $ game.room = "stripclub"
    pause 0.3
    show bree at center, zoomAt(1.5, (640, 1040)) with easeinleft
    "With that, [bree.name] pulls me inside the club."
    "And once we're in there, she directs me to a private booth."
    hide bree with easeoutright
    "Then she disappears from sight, apparently arranging her performance with the management!"
    call get_bree_lapdance from _call_get_bree_lapdance
    scene bg stripclub
    show bree happy
    with fade
    bree.say "You know [hero.name], this was fun."
    show bree talkative
    bree.say "I saw a flyer, they're hiring."
    bree.say "I'm thinking about applying."
    show bree normal
    menu:
        "You should try":
            mike.say "That's a great idea. You were perfect back then."
            $ bree.flags.work_stripclub = True
        "That's a bad idea":
            mike.say "I'm not sure this job is made for you."
            $ bree.flags.work_stripclub = False
    $ bree.love += 2
    $ game.active_date.score = 100
    $ game.room = "street"
    scene bg street
    show bree
    with fade
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
