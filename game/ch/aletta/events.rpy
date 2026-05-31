init python:
    Event(**{
    "name": "aletta_event_01",
    "label": "aletta_event_01",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("coffee_break"),
            MinStat("charm", 30),
            ),
        PersonTarget(aletta,
            HasRoomTag("work")
            ),
        ],
    "music": "music/johny_grimes/levity.ogg",
    "priority": 500,
    "clothes": "work",
    "do_once": True,
    })

    Event(**{
    "name": "aletta_event_02",
    "label": "aletta_event_02",
    "conditions": [
        IsDone("aletta_event_01"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal"),
            MinStat("charm", 40),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            HasRoomTag("work"),
            MinStat("love", 20),
            ),
        ],
    "priority": 500,
    "music": "music/johny_grimes/levity.ogg",
    "clothes": "work",
    "do_once": True,
    })

    Event(**{
    "name": "aletta_event_03",
    "label": "aletta_event_03",
    "conditions": [
        IsDone("aletta_event_02"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal"),
            MinStat("charm", 50),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            HasRoomTag("work"),
            MinStat("love", 40),
            ),
        ],
    "priority": 500,
    "music": "music/johny_grimes/levity.ogg",
    "clothes": "work",
    "do_once": True,
    })

    Event(**{
    "name": "aletta_event_03b",
    "label": "aletta_event_03b",
    "conditions": [
        IsDayOfWeek("67"),
        IsHour(8, 18),
        HeroTarget(
            IsGender("male"),
            IsRoom("map"),
            MinStat("charm", 55),
            ),
        PersonTarget(aletta,
            MinStat("love", 50)
            ),
        ],
    "priority": 500,
    "music": "music/johny_grimes/levity.ogg",
    "clothes": "suit",
    "do_once": True,
    })

    Event(**{
    "name": "aletta_event_04",
    "label": "aletta_event_04",
    "conditions": [
        IsDone("aletta_event_03"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal"),
            MinStat("charm", 60),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            HasRoomTag("work"),
            MinStat("love", 60),
            ),
        ],
    "priority": 500,
    "clothes": "work",
    "music": "music/johny_grimes/levity.ogg",
    "gallery": {"conditions": [IsDone("aletta_event_04")], 'character':'aletta', 'label':'aletta_event_04', 'id':'Oral', 'icon': 'aletta oral', 'scene': 'alettaoffice'},
    "do_once": True,
    })

    Event(**{
    "name": "aletta_event_04b",
    "label": "aletta_event_04b",
    "conditions": [
        IsDone("aletta_event_03b"),
        IsDayOfWeek("6", "7"),
        IsHour(9, 12),
        HeroTarget(
            IsGender("male"),
            MinStat("charm", 70),
            IsRoom("bedroom1"),
            ),
        PersonTarget(aletta,
            IsFlag("sidestory", 1),
            IsFlag("sidestoryDelay", False),
            MinStat("love", 70),
            ),
        ],
    "gallery": {"conditions": [IsDone("aletta_event_04b")], 'character':'aletta', 'label':'aletta_event_04b', 'id':'Ride', 'icon': 'aletta ride', 'scene': 'livingroom'},
    "priority": 500,
    "clothes": "suit",
    "music": "music/johny_grimes/levity.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "aletta_event_05",
    "label": "aletta_event_05",
    "conditions": [
        IsDone("aletta_event_04"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal"),
            MinStat("charm", 80),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            HasRoomTag("work"),
            MinStat("love", 80),
            ),
        ],
    "priority": 500,
    "clothes": "work",
    "music": "music/johny_grimes/levity.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "aletta_event_05b",
    "label": "aletta_event_05b",
    "conditions": [
        IsDone("aletta_event_04b"),
        IsDayOfWeek("6", "7"),
        IsHour(9, 12),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom"),
            MinStat("charm", 90),
            ),
        PersonTarget(aletta,
            IsFlag("sidestory", 2),
            IsFlag("sidestoryDelay", False),
            MinStat("love", 90),
            ),
        ],
    "gallery": {"conditions": [IsDone("aletta_event_05b")], 'character':'aletta', 'label':'aletta_event_05b', 'id':'Shooting', 'icon': 'aletta shooting', 'scene': 'livingroom'},
    "priority": 500,
    "clothes": "suit",
    "music": "music/johny_grimes/levity.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "aletta_event_06",
    "label": "aletta_event_06",
    "conditions": [
        Or(
            IsDone("office_event_01"),
            IsDone("cherie_event_02"),
            HeroTarget(
                IsFlag("cherie_ceooffer"),
                MaxTimer("cherie_ceooffer", 5),
                ),
            ),
        IsDone("aletta_event_05"),
        IsNotDone("aletta_event_06_alt"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal"),
            MinStat("charm", 100),
            IsFlag("dwaynedead"),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            HasRoomTag("work"),
            MinStat("love", 100),
            ),
        ],
    "priority": 500,
    "clothes": "work",
    "music": "music/johny_grimes/levity.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "aletta_event_07",
    "label": "aletta_event_07",
    "conditions": [
        Or(
            IsDone("aletta_event_06"),
            IsDone("aletta_event_06_alt"),
            ),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_restaurant")),
        PersonTarget(aletta,
            OnDate(),
            MinStat("love", 120),
            IsFlag("delay", False)
            ),
        ],
    "priority": 500,
    "clothes": "work",
    "music": "music/johny_grimes/levity.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "aletta_event_08",
    "label": "aletta_event_08",
    "conditions": [
        IsDone("aletta_event_07", "aletta_event_06"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal")),
        PersonTarget(aletta,
            Not(IsHidden()),
            MinStat("love", 140),
            IsFlag("delay", False)
            ),
        ],
    "priority": 500,
    "clothes": "work",
    "music": "music/johny_grimes/levity.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "aletta_event_09",
    "label": "aletta_event_09",
    "conditions": [
        Or(
            And(
                "'fafwm' in DLCS",
                IsDone("aletta_event_08", "cherie_event_09")
                ),
            And(
                "'fafwm' not in DLCS",
                IsDone("aletta_event_08")
                )
            ),
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal"),
            MinStat("charm", 100),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            HasRoomTag("work"),
            MinStat("love", 160),
            IsFlag("delay", False)
            ),
        ],
    "priority": 500,
    "clothes": "work",
    "music": "music/johny_grimes/levity.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "aletta_event_10",
    "label": "aletta_event_10",
    "conditions": [
        IsDone("aletta_event_09"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal"),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            HasRoomTag("work"),
            MinStat("love", 180),
            ),
        ],
    "priority": 500,
    "clothes": "work",
    "music": "music/johny_grimes/levity.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "aletta_event_06_alt",
    "label": "aletta_event_06_alt",
    "conditions": [
        IsDone("aletta_event_05"),
        IsNotDone("aletta_event_06"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal"),
            MinStat("charm", 100),
            Not(IsFlag("dwaynedead")),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            HasRoomTag("work"),
            MinStat("love", 100),
            ),
        PersonTarget(cassidy,
            IsGone(),
            ),
        ],
    "priority": 500,
    "clothes": "work",
    "music": "music/johny_grimes/levity.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "aletta_event_08_alt",
    "label": "aletta_event_08_alt",
    "conditions": [
        IsDone("aletta_event_07", "aletta_event_06_alt"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal")),
        PersonTarget(aletta,
            Not(IsHidden()),
            MinStat("love", 140),
            HasRoomTag("work"),
            IsFlag("delay", False)
            ),
        ],
    "priority": 500,
    "clothes": "work",
    "music": "music/johny_grimes/levity.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "aletta_event_09_alt",
    "label": "aletta_event_09_alt",
    "conditions": [
        IsDone("aletta_event_08_alt"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal"),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            HasRoomTag("work"),
            MinStat("love", 160),
            IsFlag("delay", False)
            ),
        ],
    "priority": 500,
    "clothes": "work",
    "music": "music/johny_grimes/levity.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "aletta_event_10_alt",
    "label": "aletta_event_10_alt",
    "conditions": [
        IsDone("aletta_event_09_alt"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal"),
            IsFlag("fired", False),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            HasRoomTag("work"),
            MinStat("love", 180),
            IsFlag("delay", False)
            ),
        ],
    "priority": 500,
    "clothes": "work",
    "music": "music/johny_grimes/levity.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "aletta_event_10_alt_fired",
    "label": "aletta_event_10_alt_fired",
    "conditions": [
        IsDone("aletta_event_09_alt"),
        HeroTarget(
            IsGender("male"),
            IsFlag("fired", True),
            ),
        PersonTarget(aletta,
            IsActive(),
            MinStat("love", 180),
            IsFlag("delay", False)
            ),
        ],
    "priority": 500,
    "music": "music/johny_grimes/levity.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "aletta_investigation_callback",
    "label": "aletta_investigation_callback",
    "conditions": [
        IsNotDone("cassidy_investigation_complete"),
        IsHour(9, 14),
        PersonTarget(aletta,
            Not(IsPresent()),
            Not(IsHidden()),
            MinCounter("investigationcallback", 2),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "aletta_kiss_me",
    "label": "aletta_kiss_me",
    "max_girls": 1,
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(aletta,
            IsPresent(),
            Not(IsHidden()),
            MinFlag("kiss", 1),
            MinStat("love", 150),
            ),
        ],
    "music": "music/johny_grimes/levity.ogg",
    "chances": 20,
    "once_day": True,
    "do_once": False,
    "quit": False,
    })

    Event(**{
    "name": "aletta_preg_talk",
    "label": "aletta_preg_talk",
    "do_once": False,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(aletta,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("toldpreg", False),
            MinCounter("pregnant", 6),
            ),
        ],
    "music": "music/johny_grimes/levity.ogg",
    })

    Event(**{
    "name": "aletta_chat_about_cherie",
    "label": "aletta_chat_about_cherie",
    "conditions": [
        IsDone("cherie_cold_call"),
        HeroTarget(IsRoom("alettaoffice")),
        PersonTarget(aletta,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "priority": 1000,
    "do_once": True,
    })

    Event(**{
    "name": "aletta_chat_about_cherie2",
    "label": "aletta_chat_about_cherie2",
    "conditions": [
        IsDone("cherie_first_call"),
        HeroTarget(IsRoom("alettaoffice")),
        PersonTarget(aletta,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "priority": 1000,
    "do_once": True,
    })

    Event(**{
    "name": "aletta_stress",
    "label": "aletta_stress",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasRoomTag("work")),
        PersonTarget(aletta,
            HasRoomTag("work"),
            MinStat("love", 30),
            MinStat("sub", 10),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "aletta_stress_2",
    "label": "aletta_stress_2",
    "conditions": [
        IsDone("aletta_stress"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("work")),
        PersonTarget(aletta,
            HasRoomTag("work"),
            MinStat("love", 40),
            MinStat("sub", 20),
            IsFlag("kinkdelay", False),
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        PersonTarget(lavish,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        PersonTarget(audrey,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "aletta_stress_2b",
    "label": "aletta_stress_2b",
    "conditions": [
        IsDone("aletta_stress_2"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("work")),
        PersonTarget(aletta,
            HasRoomTag("work"),
            MinStat("love", 60),
            MinStat("sub", 40),
            IsFlag("kinkdelay", False),
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    })

    InteractActivity(**{
    "name": "aletta_stress_2c",
    "label": "aletta_stress_2c",
    "duration": 0,
    "display_name": "Use the remote vibrator",
    "conditions": [
        HeroTarget(HasRoomTag("work")),
        PersonTarget(aletta,
            IsActive(),
            HasRoomTag("work"),
            IsFlag("vibrator", True)
            ),
        ],
    "icon": "vibrate",
    "once_hour": True,
    })

    Event(**{
    "name": "aletta_stress_3",
    "label": "aletta_stress_3",
    "conditions": [
        IsDone("aletta_stress_2"),
        HeroTarget(
            IsGender("male"),
            IsRoom("ceo"),
            IsFlag("isceo"),
            ),
        PersonTarget(aletta,
            HasRoomTag("work"),
            MinStat("love", 100),
            MinStat("sub", 25),
            IsFlag("kinkdelay", False),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "aletta_kink_03",
    "label": "aletta_kink_03",
    "conditions": [
        IsDone("aletta_stress_2"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("mcoffice")),
        PersonTarget(aletta,
            HasRoomTag("work"),
            IsFlag("kinkdelay", False),
            MinStat("love", 50),
            MinStat("sub", 40),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "aletta_kink_04",
    "label": "aletta_kink_04",
    "conditions": [
        IsDone("aletta_kink_03"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("mcoffice")),
        PersonTarget(aletta,
            HasRoomTag("work"),
            IsFlag("kinkdelay", False),
            MinStat("love", 60),
            MinStat("sub", 50),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "aletta_kink_05",
    "label": "aletta_kink_05",
    "conditions": [
        IsDone("aletta_kink_04"),
        HeroTarget(
            IsGender("male"),
            IsRoom("alettaoffice")),
        HasSkill("shibari"),
        InInventory("bondage_ropes"),
        PersonTarget(aletta,
            IsRoom("alettaoffice"),
            IsFlag("kinkdelay", False),
            MinStat("love", 70),
            MinStat("sub", 60),
            ),
        PersonTarget(audrey,
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "aletta_kink_06",
    "label": "aletta_kink_06",
    "conditions": [
        IsDone("aletta_kink_05"),
        IsDayOfWeek(6, 7),
        IsHour(9, 18),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("work")),
        PersonTarget(aletta,
            IsFlag("kinkdelay", False),
            MinStat("love", 80),
            MinStat("sub", 70),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "aletta_kink_07",
    "label": "aletta_kink_07",
    "conditions": [
        IsDone("aletta_kink_06"),
        IsHour(9, 18),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("work")),
        PersonTarget(aletta,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("kinkdelay", False),
            MinStat("love", 90),
            MinStat("sub", 80),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "aletta_kink_08",
    "label": "aletta_kink_08",
    "conditions": [
        IsDone("aletta_kink_07"),
        IsHour(9, 18),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("mcoffice"),
            IsActivity("work_personal", "workhard_personal")
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            HasRoomTag("work"),
            IsFlag("kinkdelay", False),
            MinStat("love", 100),
            MinStat("sub", 90),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "aletta_spanking_start",
    "label": "aletta_spanking_start",
    "priority": 200,
    "conditions": [
        IsDone("aletta_stress_2"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal"),
            IsRoom("office", "personal", "ceo"),
            ),
        PersonTarget(aletta,
            IsRoom("alettaoffice", "office"),
            MinStat("love", 60),
            MinStat("sub", 40),
            IsFlag("kinkdelay", False),
            ),
        PersonTarget(audrey,
            Not(IsHidden()),
            ),
        PersonTarget(lavish,
            Not(IsHidden()),
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    })

label aletta_stress_2c:
    play sound cell_vibrate
    show aletta surprised
    show fx exclamation
    "Almost as soon as I press the button, I see Aletta's eyes widen in surprise."
    "She seems to want to look in my direction, but she fights the urge as I watch her."
    hide fx
    show fx heart
    show aletta blush
    "And in a couple of seconds, the look in Aletta's eyes undergoes a drastic change."
    show aletta pleasure
    "First they lose focus, as the vibrator works away at her pussy below."
    $ aletta.sub += 1
    "And then they roll back into her head as the sensations overtake her completely."
    return

label aletta_stress:
    "Working around a career-minded and ruthlessly efficient woman like Aletta, you get used to her raising her voice."
    "And after a while, you kind of start to not notice it, like it fades into the background office noise."
    "Which is why it comes as some surprise when I hear a discreet and almost delicate cough from the doorway."
    "I look up, fully expecting to see one of the meeker and more mild-mannered girls standing there."
    show aletta pain
    "But instead I see Aletta, looking straight at me with a pained smile on her face."
    mike.say "Erm, Aletta..."
    mike.say "Sorry, I didn't hear you come in!"
    mike.say "What can I do for you?"
    "Aletta sighs and begins to rub the side of her head, like she's trying to release a trapped nerve."
    "But I'm still more concerned with the notion that she might blow up at any moment."
    "As with her, there can be a moment of almost eerie silence before the storm breaks."
    aletta.say "I...I just needed to let you know..."
    aletta.say "About those figures I wanted from you."
    "I begin to nod almost instantly, already searching for what Aletta wants."
    mike.say "Oh, sure thing, Aletta."
    mike.say "I've got them right here..."
    aletta.say "NO..."
    "The tone of Aletta's voice stops me dead."
    "I look up to see that she's holding up her hand to dismiss me too."
    "But the odd thing is that she also has a pained look on her face."
    "Almost like raising her voice was enough to cause her discomfort."
    aletta.say "No, [hero.name]."
    aletta.say "I meant to say you should hold onto them."
    aletta.say "I...I'm running late on the report I need them for..."
    aletta.say "So I'll let you know when I actually want them, okay?"
    "I nod slowly, unused to hearing Aletta make such a confession."
    "She's usually never behind with her work, a consummate over-achiever."
    "And now that I'm looking more closely, she looks tired - exhausted even."
    mike.say "Aletta, are you feeling okay?"
    mike.say "You seem a little out of it, that's all!"
    "Aletta shakes her head at this."
    "And for a moment I think that she's just going to flat out deny it."
    "But then she lets out a massive sigh and her whole body seems to sag."
    aletta.say "Uuurgh..."
    aletta.say "Is it that obvious?"
    mike.say "Ah, yeah, Aletta."
    mike.say "You're normally like an unstoppable machine around here!"
    mike.say "It's worrying to see you off your game."
    aletta.say "I...I don't know what it is, [hero.name]."
    aletta.say "But just recently, I feel like things have been getting to me."
    aletta.say "I'm so stressed that I'm cranky all the time."
    aletta.say "I have these godawful headaches and I'm not sleeping either!"
    "I nod my head, trying to show Aletta that I feel for her plight."
    "Sure, she's a ball-breaker in the workplace and no mistake."
    "But that doesn't mean I'd wish all of that stuff on her."
    "Aletta can be a whole lot of fun when she wants to be too."
    "So much so that I feel the need to help her out of this predicament she's in."
    mike.say "Have you thought about taking some time off, Aletta?"
    mike.say "Maybe getting some counselling?"
    "I thought the suggestions I just made were pretty sensible."
    "Nothing drastic or in the least bit scary, at least in my mind."
    show aletta annoyed
    "And yet Aletta seems to recoil like a vampire at the sight of garlic!"
    aletta.say "Of course not, [hero.name]!"
    aletta.say "Do you have any idea what that would do to my standing around here?"
    aletta.say "I'm a woman working in a male-dominated corporate environment."
    aletta.say "If I show the slightest hint of weakness, my career could be ruined!"
    "The volume of Aletta's voice had been rising all the time she's speaking."
    show aletta pain
    "But when she's finished, I see her put her hand to her head again."
    mike.say "Whoa, calm down Aletta."
    mike.say "Now you're stressing out over being stressed out!"
    "Aletta takes a sharp breath into her lungs."
    show aletta normal
    "She holds it for a moment and then lets it out in one smooth motion."
    aletta.say "I'm okay, [hero.name]."
    aletta.say "I am a strong, independent woman."
    aletta.say "And I will find a way to handle this!"
    hide aletta
    "And with that, she turns smartly on her heel and walks out."
    "I'm left to watch her go in silence."
    "But I wonder if she was saying all of that to convince me or her!"
    if aletta.sub.max < 20:
        $ aletta.sub.max = 20
    $ aletta.flags.kinkdelay = TemporaryFlag(True, 1)
    return

label aletta_stress_2:
    show bg alettaoffice
    "I'm not the kind of guy that spends a whole lot of time complaining about his job."
    "For the most part it's pretty much what I wanted in terms of an actual career."
    "And I'm happy spending weekdays between nine and five in the office."
    "But meetings are an exception, because meetings suck on every possible level."
    "The only thing worse is a meeting where I'm supposed to be giving a presentation."
    "And that's exactly the kind of meeting I have now."
    call aletta_stress_meeting from _call_aletta_stress_meeting_1
    "As they get up and file out, my mind begins to dwell on what just happened."
    "What was that second remote actually for?"
    "And why did it seem to get Aletta so worked up?"
    "I shake my head, resolving to ask her about it the first chance I get."
    if aletta.sub.max < 40:
        $ aletta.sub.max = 40
    $ aletta.flags.kinkdelay = TemporaryFlag(True, 3)
    return

label aletta_stress_2b:
    "I wouldn't exactly say that Aletta and I have been trying to avoid each other since the incident with the vibrator."
    "That'd mean it was the only thing that was on both of our minds, like we were obsessing and couldn't think of anything else."
    "And that's not the case at all - honestly it's not!"
    "It's just that I find myself passing off jobs that would need me to go see her, even just to exchange a couple of words."
    "I either give them to Shiori or else convince myself that I'll handle it some other time and do something else instead."
    "It becomes obvious to me that Aletta's doing the same thing too."
    "She always hurries past the door to my office, and I end up dealing with her underlings the whole time as well."
    "Normally she'd think nothing of striding straight in and demanding whatever she wanted of me."
    "But as it is, I've gone whole days without being in the same room as her."
    play sound door_knock
    show aletta at top_mostleft
    "That is before I hear a knock at the door and look up to see her standing there."
    "Instantly my brain goes into auto-pilot and I wait for Aletta to speak first."
    "Like I already said, she's usually the one barging in on me and barking orders."
    show aletta dreamy
    "So it comes as some surprise when all Aletta does is stand there with an unfamiliar look on her face."
    "Her eyes are darting this way and that, like she's paranoid of being watched."
    "More than once she opens her mouth to speak, but stops as soon as someone walks close by."
    "Is she...is she actually nervous?"
    mike.say "Ah..."
    mike.say "Good morning, Aletta."
    mike.say "Would you like to come in?"
    "At the sound of my voice, she seems to snap out of it just a little."
    show aletta annoyed at left with move
    "A small measure of the old Aletta emerges as she nods and steps through the doorway."
    aletta.say "Ahem..."
    aletta.say "Yes, [hero.name], I would."
    aletta.say "And I'd appreciate not being left to stand around like that in future!"
    "But the moment that she's finished speaking, Aletta returns to her previous state of agitation."
    "She hurries into my office, shutting the door behind her."
    "Aletta pauses for a moment, as if listening for anyone eavesdropping on the other side."
    show aletta dreamy at center with move
    "After a moment, she nods and then scuttles over to my desk."
    "Once there, she pulls out the chair on the other side and flops down into it."
    mike.say "Aletta..."
    mike.say "Are you okay?"
    mike.say "Is the stress getting to you again?"
    "At the mere mention of the problems she described to me before, Aletta jumps in her seat."
    "Her eyes dart up to meet mine, looking wide, like those of a deer in the headlights."
    show aletta embarrassed
    "And then, just as quickly, she looks away again, deliberately not meeting my eye."
    aletta.say "No, [hero.name]."
    aletta.say "That's not it."
    aletta.say "Quite the opposite, actually..."
    mike.say "You mean you're not feeling stressed anymore?"
    mike.say "That's great news, Aletta!"
    mike.say "Why aren't you celebrating?"
    aletta.say "Well..."
    aletta.say "It's because I think I know what did it, [hero.name]."
    aletta.say "It's been since that meeting we had the other day."
    aletta.say "You know the one I mean?"
    mike.say "Yeah, Aletta - how could I forget it!"
    show aletta normal
    "Only now does Aletta turn her gaze back to me."
    "And the look in her eyes fills in all the blanks in an instant."
    mike.say "Whoa..."
    mike.say "Wait a minute, Aletta!"
    mike.say "You can't mean..."
    "Aletta cuts me off before I can finish."
    hide aletta
    show aletta close
    "She leans forward, planting the palms of her hands on the desktop."
    "I can't ever recall seeing her this passionate before now - this desperate even!"
    aletta.say "I DO mean it, [hero.name]!"
    aletta.say "I don't want to admit it, but I have to!"
    aletta.say "Since you used that thing on me, since you humiliated me in front of my peers..."
    aletta.say "The headaches are gone, I'm not stressed anymore and I'm sleeping like a baby!"
    aletta.say "You cured me, [hero.name]!"
    aletta.say "But now I need your help to stay well."
    aletta.say "What do you say - will you keep on giving me my medication?"
    menu:
        "Agree":
            "It takes a couple of seconds for me to actually understand what Aletta's asking of me."
            "I was expecting her to come in here and at the very least tell me off for what happened."
            "At the worst she might have threatened to get HR involved, maybe even tell me she already had."
            "But the last thing I could have imagined was her walking in here and asking me to do it again!"
            mike.say "You...you mean that, Aletta?"
            mike.say "The first time was just an accident."
            mike.say "You really want me to do it to you a second time?"
            show aletta blush
            "Aletta's cheeks flush a deep shade of red as I say this."
            "But she seems set on this course, and she nods all the same."
            aletta.say "It's not something that I could have imagined working, [hero.name]."
            aletta.say "And maybe that's why it did the trick."
            aletta.say "But, yes - I want you to do it again."
            "As if to underline the point, Aletta reaches into her pocket."
            "I watch as she pulls out the remote control for the vibrator."
            "She places it on the desk and then pushes it towards me."
            aletta.say "I want you to keep this, [hero.name]."
            aletta.say "It'll only work if I don't know when it's coming."
            "Slowly and with deliberate caution, I reach out and take it from her."
            "I nod gravely, turning the remote control over in my hand."
            mike.say "Okay, Aletta."
            mike.say "If you're totally sure this is what you want?"
            $ aletta.sub += 5
            "Aletta nods eagerly, keen to have my agreement."
            aletta.say "As sure as I've ever been about anything."
            aletta.say "I promise to keep the vibrator inside of me while I'm at work."
            aletta.say "I'll make sure the batteries are fresh too."
            aletta.say "All you have to promise me is that you won't warn me before you use it."
            aletta.say "Are we agreed, [hero.name]?"
            mike.say "Sure thing, Aletta."
            mike.say "We're agreed."
            hide aletta
            show aletta blush
            "I try to keep my voice even and serious as Aletta nods and rises to leave."
            hide aletta with moveoutleft
            "It's only when she's gone and I'm alone again that I allow myself to smile."
            "And when I do, it's a grin that spreads from one side of my face to the other."
            "How in the hell did I manage to get so damn lucky?!?"
            "Aletta just handed me what amounts to a remote control for her pussy!"
            "And she practically begged me to use it on her when and where I please."
            "This is going to be a serious amount of fun!"
            $ aletta.flags.vibrator = True
            $ aletta.flags.kinkdelay = TemporaryFlag(True, 1)
        "Refuse":
            "For a moment I can't actually believe what Aletta's asking me to do."
            "Picking up the remote control to her vibrator was a complete mistake."
            "And what happened afterwards still makes me feel incredibly guilty."
            "The very idea of inflicting something like that on her for a second time..."
            "I can't even bring myself to think of it!"
            mike.say "Aletta, what happened in that meeting was a complete accident."
            mike.say "I'm really sorry to put you through it."
            mike.say "I...I couldn't do it to you again!"
            show aletta annoyed
            "Aletta shakes her head at this."
            "She's clearly not going to be dissuaded so easily."
            aletta.say "None of that matters, [hero.name]."
            aletta.say "I know it was an accident, of course I do!"
            aletta.say "But all that does matters is the end result."
            aletta.say "You cured my stress!"
            mike.say "Yeah, but does it matter that it was me, Aletta?"
            mike.say "Look, if you want to keep on using that thing in meetings, that's fine."
            mike.say "I promise that your secret's safe with me, okay?"
            $ aletta.sub -= 25
            mike.say "I'm just not cool with having that kind of power over you."
            "Aletta leans back in her chair."
            "She looks frustrated and more than a little disappointed with my answer."
            show aletta angry
            "But I keep on staring straight at her, making it obvious that I mean it."
            $ aletta.love -= 20
            aletta.say "Urgh..."
            aletta.say "Okay, okay!"
            aletta.say "I can't force you to do it, [hero.name]."
            hide aletta
            show aletta
            aletta.say "I guess I'll just have to find another way of handling it."
            hide aletta with moveoutleft
            "With that, Aletta gets up from her seat and lets herself out of my office."
            "I'm not sure if I've made the right decision for her."
            "But if feels like the right one for me."
            "Even if I have just added to Aletta's level of stress."
            "Which doubtless means more stress for everyone else in the office too!"
    return

label aletta_stress_meeting:
    "I'm just finishing up getting the projector working as everyone starts to file in."
    "Shiori, Lavish and Audrey are too busy gossiping to pay me any attention."
    show aletta pain
    "But Aletta's still looking stressed and tired when she arrives."
    "And what's worse, she's trying to play it off as if nothing's wrong."
    mike.say "Hi, Aletta."
    mike.say "How are you feeling today?"
    "I only intended the question as idle chit-chat."
    show fx anger
    show aletta angry
    "But Aletta shoots me an almost venomous glare."
    aletta.say "What the hell's that supposed to mean, [hero.name]?"
    aletta.say "Why are you asking me that?!?"
    aletta.say "I'm fine, of course I am!"
    "Shocked at having my head almost bitten off, I look around the room."
    "Shiori, Lavish and Audrey have all fallen silent at Aletta's outburst."
    "And every one of them is staring at her in surprise."
    show aletta annoyed blush
    "Aletta seems to realise this a moment later, her cheeks flushing red."
    mike.say "Are you sure you're okay, Aletta?"
    mike.say "We can always reschedule, you know?"
    mike.say "Do this another time if you have something else on your mind..."
    show aletta pain
    aletta.say "No..."
    "Aletta snaps the word at me."
    show aletta normal
    "But then she makes a visible effort to restrain herself."
    aletta.say "No, [hero.name], there's no need for that."
    aletta.say "I'll be okay - let's just get on with the meeting, okay?"
    "I hold up my arms in a gesture of surrender."
    "And I try not to make eye-contact with the others as well."
    "Maybe I can just keep my head down and get through this quickly."
    "At least keep from making Aletta explode again before we get out of here."
    mike.say "Sure, Aletta - you're the boss!"
    hide aletta
    "Everyone hurries to their seats as I start the presentation."
    "And I'm already thinking how I can make things go faster."
    "Perhaps there are some things that I can skip over."
    "Some points that could be put in an email instead..."
    "At first, everything seems to go to plan."
    "I skip briskly from one point to the next, going as fast as I can."
    "I either don't stop for questions or else ignore them whenever a hand goes up."
    show shiori work
    "But I stumble when Shiori asks a question out loud and I can't ignore it."
    shiori.say "I...I'm sorry, [hero.name]."
    shiori.say "But I don't understand!"
    show lavish work at left
    lavish.say "Yeah, I don't either!"
    show audrey work at right
    audrey.say "You're going too fast!"
    "I stop to answer the question."
    "But then I hear Aletta getting pissed."
    hide audrey
    hide shiori
    hide lavish
    show fx anger
    show aletta angry
    aletta.say "Urgh..."
    aletta.say "What are you guys?"
    aletta.say "A set of damn morons?!?"
    mike.say "Right...right..."
    mike.say "I'll see you guys after the presentation's over."
    mike.say "Let's just push on to the end, okay?"
    "Still reeling from Aletta's latest outburst, I reach for the remote that works the projector."
    "My hand finds it after a couple of seconds groping around on the table."
    show aletta surprised blush
    "I think that I hear Aletta make a sound that might be a protest."
    show aletta embarrassed
    "But my mind is focused on getting through the presentation."
    "And I'm also doing this for her benefit, so I choose to ignore her."
    mike.say "So, on this next diagram..."
    show aletta vibrator on
    "I press the button that should make the slide I want pop up."
    "But nothing happens, save for Aletta shifting suddenly in her seat."
    mike.say "Hmm..."
    mike.say "That's weird!"
    show aletta vibrator surprised
    "I press the button again, and still nothing happens."
    aletta.say "Mmmm..."
    "What follows is a bizarre situation where nothing seems to make sense."
    show aletta vibrator pleasure
    "The more I hammer the buttons on the remote, the more irate Aletta seems to become."
    "The whole time nothing is happening on the projector screen."
    "And so I keep right on pressing the same button with ever more urgency."
    aletta.say "Ah..."
    aletta.say "Oh...oh god!"
    show aletta vibrator shiori_surprised
    "By now I'm no longer looking at the screen as I press the button."
    "Like everyone else in the room, I'm staring at Aletta instead."
    "She's practically writhing in her seat with what I can only imagine is suppressed rage."
    "Eyes wide and teeth clenched tightly together, she plunges her hands under the table."
    "I can picture her clenched fists under there, nails digging into her palms!"
    aletta.say "Oh no...oh no..."
    aletta.say "Not here...not now!"
    aletta.say "Oh...oh FUCK!"
    "My eyes almost pop out of their sockets as I listen to Aletta."
    "And the table rocks as her knees hit the underside."
    show aletta vibrator fall squirt ahegao open blurry
    "Finally she throws her head back and lets out a wail of some kind."
    show aletta vibrator shiori_embarrassed
    "Which is the moment that everyone looks away out of sheer embarrassment!"
    "I look down at my hands, noticing something for the first time."
    "The remote I'm holding doesn't look familiar at all."
    "And I can see the one I should be using right there on the table!"
    "I pick up the other remote, staring at the pair in confusion."
    hide aletta
    show aletta embarrassed blush
    "But then Aletta snatches the mysterious one out of my hand."
    hide aletta with moveoutleft
    "She grabs the rest of her things before hurrying out of the meeting room."
    "All I can do is shrug and turn to the others."
    mike.say "Well, I guess that wraps it up for today!"
    return

label aletta_stress_3:
    show bg ceo
    play sound door_knock
    "I almost don't look up from my desk when I hear a brisk knock at the door."
    "And that's because I know that Aletta's going to come sweeping in a moment later."
    show aletta work at left with moveinleft
    "True to form, she doesn't wait to be invited in, just opens the door and enters."
    mike.say "Something I can do for you, Aletta?"
    mike.say "Maybe organise a seminar on office etiquette?"
    mike.say "You know, basic stuff like waiting to be invited in?"
    show aletta happy
    "Aletta greets this with one of her characteristic and superior smirks."
    "Though I do have to admit, it makes her look particularly hot when she does that!"
    show aletta normal
    aletta.say "No thank you, [hero.name]."
    aletta.say "I find being forward works far better for me."
    show aletta flirt
    aletta.say "In business and life in general."
    show aletta at center with move
    "Aletta pauses as she walks the rest of the distance to my desk."
    mike.say "Like I already said, Aletta..."
    mike.say "Is there anything I can do for you?"
    mike.say "Or did you just come in here to stretch your legs?"
    aletta.say "Well, [hero.name]..."
    aletta.say "It was more to see if I could do something for you..."
    hide aletta
    show aletta close flirt
    "Aletta raises an eyebrow as she leans over my desk."
    "And she makes certain that I see down her top as she does so."
    mike.say "I...I am..."
    mike.say "I am feeling a little stressed today!"
    call aletta_fuck_office_titjob from _call_aletta_fuck_office_titjob
    $ aletta.flags.kinkdelay = TemporaryFlag(True, 1)
    return

label aletta_kink_03:
    "It's been a couple of days since I helped Aletta out with that little problem she had."
    "You know what I mean - the stress that had been giving her headaches and the sleepless nights?"
    "The same stress that had to be cured by means of a certain battery-operated device?"
    "Anyway, it seemed to have done the trick - Aletta's been brighter and more upbeat ever since."
    "And it must have rubbed off on me too, because I feel almost as good as she looks."
    "Or maybe that has more to do with knowing what curing Aletta's stress involved..."
    "Which is why it comes as a surprise to hear the commotion going on outside of my office."
    "I can hear raised voices out there - well, one raised voice at least."
    "And it's unmistakably Aletta's voice that I can hear too."
    "Sticking my head around the door, I'm in time to see the fallout of the shouting."
    scene bg office
    if not (shiori.hidden and lavish.hidden and audrey.hidden):
        show audrey at mostleft5
        show lavish at left5
        show shiori
        "Audrey, Lavish and Shiori are all dashing off in different directions."
        "But I can see that they've all fled from one central point."
    elif shiori.hidden and not (lavish.hidden and audrey.hidden):
        show audrey at mostleft5
        show lavish at left5
        "Audrey and Lavish are all dashing off in different directions."
        "But I can see that they've all fled from one central point."
    elif lavish.hidden and not (shiori.hidden and audrey.hidden):
        show audrey at mostleft5
        show shiori at left5
        "Audrey and Shiori are all dashing off in different directions."
        "But I can see that they've all fled from one central point."
    elif audrey.hidden and not (shiori.hidden and lavish.hidden):
        show shiori at mostleft5
        show lavish at left5
        "Lavish and Shiori are all dashing off in different directions."
        "But I can see that they've all fled from one central point."
    elif shiori.hidden and lavish.hidden and not audrey.hidden:
        show audrey at mostleft5
        "Audrey is dashing off in the corner of the office."
        "But I can see that she's fled from one central point."
    elif shiori.hidden and audrey.hidden and not lavish.hidden:
        show lavish at mostleft5
        "Lavish is dashing off in the corner of the office."
        "But I can see that she's fled from one central point."
    elif audrey.hidden and lavish.hidden and not shiori.hidden:
        show shiori at mostleft5
        "Shiori is dashing off in the corner of the office."
        "But I can see that she's fled from one central point."
    else:
        "Employees are all dashing off in different directions."
        "But I can see that they've all fled from one central point."
    show aletta angry at right
    "A point which is currently occupied by an angry, seething Aletta."
    mike.say "Aletta..."
    mike.say "What happened out here?"
    mike.say "Are you okay?"
    "At the sound of my voice, Aletta rounds on me."
    "I can see the anger still burning in her eyes."
    "And for a moment, I think I'm in for the same treatment as the others!"
    "But then the fire fades from Aletta's gaze, and she shakes her head."
    show aletta annoyed
    aletta.say "I...I'm sorry, [hero.name]."
    aletta.say "I don't know what came over me!"
    "I'm more worried by the fact that Aletta's apologising than her actual outburst."
    scene expression f"bg {game.room}"
    show aletta embarrassed
    "And so I waste no time ushering her into my office and making her sit down."
    "Once there, she seems to regain a measure of composure."
    aletta.say "This is so embarrassing."
    aletta.say "I can't believe I lost my temper like that."
    mike.say "I don't get it, Aletta."
    mike.say "You seemed so much more relaxed after..."
    mike.say "Well, after I helped you out!"
    show aletta normal blush
    "Aletta's cheeks flush just a little at the mention of what happened in the meeting."
    "She gives me a weak smile and tries to brush it off before answering my question."
    aletta.say "I know, I know..."
    show aletta normal -blush
    aletta.say "But the headaches..."
    aletta.say "They've come back!"
    "Now Aletta's looking at me in a very different way."
    "It takes me a while to figure it out."
    "But then it dawns on me - she's looking at me hopefully, almost pleading!"
    mike.say "You...you want me to use the thing on you again?"
    show aletta dreamy
    aletta.say "Ah, no..."
    aletta.say "I don't think it would work if I knew it was going to happen."
    aletta.say "I thought you might...well, use your imagination?"
    show aletta flirt blush
    aletta.say "You know - think up a little surprise for me?"
    menu:
        "Agree":
            "I can't keep myself from licking my lips as I listen to what Aletta's suggesting."
            "Is this really happening to me?"
            "Is an insanely hot woman really asking me to make her my plaything?"
            mike.say "S...sure thing, Aletta!"
            mike.say "I'm certain that I can come up with something."
            mike.say "What kind of a friend would I be if I didn't help out?"
            "Even as I'm saying the words, I'm wondering if pervert fits better than friend."
            "But what would you do in my situation?"
            "Tell her to take a hike?!?"
            show aletta happy
            "Aletta smiles broadly, clearly delighted with my answer."
            "She seems to regain a large measure of her confidence too."
            show aletta normal
            aletta.say "I knew that I could rely on you, [hero.name]."
            aletta.say "And of course, this doesn't just have to be fun for me..."
            "Aletta's smile becomes broader still as she raises her eyebrows."
            show aletta normal blush
            "She leans forwards, making sure that I can see everything as she does so."
            "My eyes bulge at the sight of her plump lips."
            "My heart pounds at the sight of her crossed legs."
            "And something else definitely bulges at the sight of her cleavage!"
            mike.say "A...anything I can do to help out, Aletta!"
            show aletta at left with move
            "Still smiling, Aletta gets up and turns to walk out of my office."
            hide aletta with moveoutleft
            "My minds already racing, even before she's gone."
            "And ideas are popping into my head too."
            "Sure, I have a moral obligation to help Aletta out."
            "But she said herself that I can have fun at the same time!"
            if aletta.sub.max < 50:
                $ aletta.sub.max = 50
        "Refuse":
            mike.say "Urgh!"
            mike.say "Aletta, really?"
            mike.say "This is an office, not a fucking sex-dungeon!"
            show aletta sad -blush
            "Aletta leans forward in her chair."
            "I can see that she's desperate."
            aletta.say "But, but..."
            aletta.say "You helped me before!"
            "I shake my head firmly."
            "This has to stop before it gets out of hand."
            mike.say "That was an accident, Aletta."
            mike.say "I'd never have pushed those buttons is I'd know..."
            mike.say "Well...if I'd known what it was doing to you!"
            mike.say "You need to see a shrink or a therapist or something."
            "Aletta makes to say something more, probably to protest."
            "But then she stops herself and gives me a forced nod."
            aletta.say "O...okay, [hero.name]."
            aletta.say "I understand."
            "With that, she gets up and walks out of my office."
            hide aletta with moveoutleft
            "Sure, I feel bad that I couldn't do more to help."
            "But I wanted to cure Aletta of her issues."
            "Not help her to indulge a new fetish on company time!"
            $ aletta.love -= 2
            $ hero.cancel_activity()
            $ game.pass_time(1)
            $ do_event.flags.canceled = TemporaryFlag(True, 3)
            return
    $ hero.cancel_activity()
    $ game.pass_time(1)
    $ aletta.flags.kinkdelay = TemporaryFlag(True, 1)
    return

label aletta_kink_04:
    if aletta.sub.max < 60:
        $ aletta.sub.max = 60
    "I'm feeling pretty confident as I sit waiting for Aletta to turn up for our appointment."
    "She left me with a poser when she asked me to help come up with a new solution to her stress."
    "But I put my mind to it and really tried to find something that would work for both of us."
    "And in the end, I came to the conclusion that the simplest answer is probably the best."
    show aletta annoyed
    "So perhaps that's why Aletta looks a little disappointed when she walks in a moment later."
    "After all, the last time I got involved she was using a remote-controlled vibrator!"
    "And there's nothing to be seen this time around, just me at my desk."
    mike.say "Hey, Aletta."
    mike.say "Come on in."
    mike.say "And don't forget to close the door behind you."
    aletta.say "Erm..."
    show fx question
    aletta.say "Did I miss something, [hero.name]?"
    aletta.say "Was the meeting about you helping with my stress another time?"
    "I shake my head, trying to look positive the whole time."
    mike.say "Not at all, Aletta."
    mike.say "Your problem's been on my mind ever since you asked for my help."
    mike.say "I just thought that it might be best to go back to basics, that's all!"
    show aletta normal
    "Aletta raises an eyebrow as she walks towards my desk."
    "I can see that she's intrigued to find out more."
    "Of course she wants to know what I have in mind for her."
    "But I'm not about to ruin the surprise by letting on just yet."
    "And so all I do is beckon Aletta closer with a single crooked finger."
    "She reaches the desk and leans her palms against the edge."
    "This time, Aletta raises both eyebrows, clearly expecting me to open up."
    "But I shake my head and nod for her to join me on my side instead."
    "For a moment I think that Aletta's going to call my bluff."
    "And if she does, I'll have no choice to but to tell her."
    "But it seems that my luck is in."
    "Aletta rolls her eyes, and yet she still pulls herself up and does as I ask."
    mike.say "Right here, Aletta."
    mike.say "I want you bending on my knees..."
    show aletta surprised
    "Aletta opens her mouth to ask me the inevitable question."
    "What in the hell is going on?"
    "And why in the hell does it need her standing there?"
    "But I'm determined not to let this chance pass me by."
    "While Aletta has no idea what's about to happen, the more effect it'll have."
    "And so without asking for permission, I bend Aletta over my knees."
    hide aletta
    show spank aletta
    aletta.say "Whoa..."
    aletta.say "What the hell..."
    "Aletta barely has time to cry out before I make my next move."
    "I take a firm hold of her skirt and hike it up to reveal her backside."
    show spank aletta spank
    play sound spank
    with hpunch
    "And then I lay the palm of my hand across it."
    "The sound it makes is like the crack of a whip."
    show spank aletta surprised
    "And Aletta cries out, more in surprise than pain."
    aletta.say "Ah..."
    aletta.say "M...my ass..."
    aletta.say "You...you spanked me!"
    show spank aletta up
    pause 0.3
    show spank aletta spank
    play sound spank
    with hpunch
    "By way of an answer, I reverse the motion, catching Aletta on the backhand."
    "She cries out for a second time, looking back over her shoulder in surprise."
    mike.say "Noticed that, did you?"
    mike.say "Yeah, Aletta, I'm spanking you."
    mike.say "And I'm not going to stop anytime soon either."
    show spank aletta up
    pause 0.3
    show spank aletta spank
    play sound spank
    with hpunch
    "The third slap is almost as loud as the first."
    "It makes Aletta yelps in alarm."
    mike.say "The door's not locked, you know."
    mike.say "So anyone could walk in on us, Aletta."
    mike.say "And shouting out loud, well..."
    mike.say "That's just going to make it more likely someone will!"
    "Aletta regards me with an almost pleading look in her eyes."
    show spank aletta ready pleasure
    "But then she bites her lip and turns her head to look forwards."
    show spank aletta up
    "I take this as permission to continue, aiming another slap at Aletta's ass..."
    show spank aletta spank
    play sound spank
    with hpunch
    if hero.sexperience >= 20:
        "Aletta whimpers as she takes the blow, her whole body quivering."
        "And I can feel the same shakes and thrills running through me too!"
        show spank aletta up
        pause 0.3
        show spank aletta spank
        play sound spank
        with hpunch
        "Every time she moves or makes a sound, it turns me on just as much."
        "And it's not just the enjoyment I take from getting physical with Aletta."
        "I can honestly feel the constant fear of being discovered too."
        "What if someone walks in on us while I'm spanking Aletta?"
        show spank aletta up
        pause 0.3
        show spank aletta spank
        play sound spank
        with hpunch
        "The mere thought of it spurs me on to spank harder and faster."
        "By now, Aletta is almost squealing with each contact I make."
        "The noises beginning to sound more like cries of pleasure all the time!"
        "Pretty soon there's no way to tell them apart."
        show spank aletta up
        pause 0.3
        show spank aletta spank marks
        play sound spank
        with hpunch
        "And I'm certain that Aletta can't tell the difference either."
        "Her buttocks have already turned a deep shade of red."
        "The shape of my hand actually becoming visible on her ass!"
        show spank aletta up
        pause 0.3
        show spank aletta spank
        play sound spank
        with hpunch
        "Finally, Aletta can stand no more and she collapses on my knees."
        "I hurry to help her, worried that I might have gone too far."
        mike.say "Aletta..."
        mike.say "Are you okay?!?"
        scene expression f"bg {game.room}"
        "Aletta gasps, but still manages to nod her head."
        "And a few moments later, she's actually able to speak."
        show aletta pleasure blush
        aletta.say "I...I..."
        aletta.say "I feel...amazing!"
        show aletta happy
        show fx exclamation
        aletta.say "It worked, [hero.name] - it actually worked!"
        mike.say "Whew..."
        mike.say "I'm glad to hear that, Aletta."
        mike.say "I was worried I might be the only one enjoying it!"
        show aletta dreamy blush
        "Aletta looks away from me as she pulls down her skirt."
        "But I can see that the cheeks on her face are as red as the ones beneath it!"
        aletta.say "N...no worries there, [hero.name]!"
        aletta.say "Would you like to..."
        show aletta flirt blush
        aletta.say "I don't know, maybe...do this again sometime?"
        "For a moment I can't believe what I'm hearing."
        "Not only did it work, but Aletta actually wants me to do it again!"
        mike.say "Sure thing, Aletta!"
        mike.say "Whatever you want!"
        "Aletta can only glance back over her shoulder at me for a brief second as she nods."
        "As it seems she's still reluctant to let me see just how much she's blushing!"
        $ aletta.flags.weeklyspank = game.days_played
    else:
        "Aletta whimpers as she takes the blow, her whole body quivering."
        "But now I'm beginning to wonder what happens if someone does walk in here."
        "Surely nobody's going to believe that this is a mutual thing, are they?"
        show spank aletta up
        pause 0.3
        show spank aletta spank
        play sound spank
        with hpunch
        "I mean, Aletta did ask me to think something up to deal with her stress."
        "But it's not like I talked this thing through with her beforehand, is it!"
        "With all of this running around inside of my head, it's hard to concentrate on the moment."
        show spank aletta up
        pause 0.3
        show spank aletta spank
        play sound spank
        with hpunch
        "And the finer points of what my efforts are achieving are pretty much lost on me."
        "This means that when the end of comes, I hardly notice it at all!"
        show spank aletta up
        pause 0.3
        show spank aletta spank
        play sound spank
        with hpunch
        "Aletta just seems to collapse on my knees, panting and gasping."
        "I hurry to help her, worried that I might have gone too far."
        scene expression f"bg {game.room}"
        mike.say "Aletta..."
        mike.say "Are you okay?!?"
        "Aletta gasps, but still manages to nod her head."
        "And a few moments later, she's actually able to speak."
        show aletta pleasure blush
        aletta.say "I...I..."
        aletta.say "I feel...pretty good!"
        show aletta happy
        show fx exclamation
        aletta.say "I think it worked!"
        mike.say "Oh, thank god you're okay!"
        mike.say "But I don't think I can do this again, Aletta."
        mike.say "I mean...we can find something else...if you want."
        mike.say "But I can't do THIS again!"
        show aletta normal
        "Aletta nods, looking oddly disappointed at my declaration."
        "But right now, it seems that she's in no condition to argue."
    $ hero.cancel_activity()
    $ game.pass_time(1)
    $ aletta.flags.kinkdelay = TemporaryFlag(True, 1)
    return

label aletta_kink_05:
    if aletta.sub.max < 70:
        $ aletta.sub.max = 70
    scene bg alettaoffice
    "I don't waste any time letting myself into Aletta's office."
    "I just open the door and burst right in without bothering to knock."
    "Of course, this means that Aletta is taken completely by surprise."
    show aletta annoyed
    "She looks up at me from where she's sitting at her desk, face a picture of irritation."
    "The receiver of the phone that sits on the desktop is still in her hand."
    "Well, it would be after I just called her on my mobile to check she was alone!"
    "But the moment she recognises me as the intruder, Aletta's expression changes."
    "It transforms from irritated and annoyed to intrigued and almost guilty!"
    show aletta dreamy
    aletta.say "[hero.name]..."
    show fx question
    aletta.say "What are you doing here?"
    if aletta.flags.weeklyspank:
        aletta.say "We aren't scheduled for another spanking until..."
        aletta.say "Let me see..."
        "Aletta glances down at the organiser on her desk."
        show aletta normal
        aletta.say "At least another week, it says here!"
        show fx question
        aletta.say "And wasn't I supposed to come to you?"
    "At first I don't offer anything in the way of an answer."
    "I just smile and close the door behind me."
    show aletta normal
    "And then I walk over to Aletta's desk and place the bag I'm holding in front of her."
    mike.say "Yeah, yeah, yeah."
    mike.say "I know all of that, Aletta."
    mike.say "But I think we need to keep things from getting stale."
    mike.say "You know - predictable?"
    "Aletta watches as I begin to unzip the bag and pull out its contents."
    show aletta surprised
    "And I see her eyes go wide as they're revealed to be lengths of rope."
    "Aletta swallows in trepidation."
    "She's probably guessed already that rock-climbing isn't what I have in mind!"
    show aletta embarrassed
    aletta.say "Are...are you sure about this, [hero.name]?"
    aletta.say "I mean, you do know what you're doing - right?"
    "I roll my eyes at the question, dismissing Aletta's concerns."
    show aletta normal
    mike.say "Sure I do, Aletta."
    mike.say "You're not the first person I ever tied up!"
    "Of course I don't tell her that she's actually the second."
    "Or that the first person I tried it on was myself."
    "And I'm certainly not going to mention how I needed my housemates to get me out of that one..."
    show aletta haircut
    aletta.say "Okay, [hero.name]."
    aletta.say "I'm going to trust you on this one."
    "I notice that Aletta's pretty caught up in the whole idea by now."
    scene aletta ropeplay
    "So much so that she doesn't ask the most obvious question."
    "Which is just what I plan to do with her once she's tied up."
    "So I guess that's going to be another surprise for her!"
    show aletta ropeplay b
    "Aletta obligingly lets me get to work."
    "And to my credit, I remember the knots and where they all go quite well."
    "All of which means that things go smoothly and I soon have Aletta all tied up."
    "Well...maybe not completely smoothly."
    show aletta ropeplay ropes
    "There are a couple of times that Aletta ends up wailing in pain."
    "And more than once a knot ends up in a compromising spot and I have to try again."
    "But those are just minor setbacks, and soon I have Aletta well and truly lashed to her chair."
    show aletta ropeplay gag
    "She even has a neat little gag securing her mouth too!"
    "Aletta stares at me helplessly from her seat."
    "And I stand back to admire my handiwork."
    "I can see from the look in her eyes that Aletta's getting a thrill out of this already."
    "Her cheeks are flushing with embarrassment and she's wriggling weakly against her bonds."
    "And the last touch is a blindfold over her eyes."
    show aletta ropeplay blindfold
    "I'm just about to ask her how she feels, ready to hear her muffled moans."
    play sound door_knock
    "But then I hear an unmistakable knock at the door!"
    "Aletta's head turns towards the sound, and then she looks back at me pleadingly."
    show aletta ropeplay pleasure
    aletta.say "Mmm..."
    aletta.say "Mmm...mmm...MMM!"
    mike.say "What are you trying to tell me, Aletta?"
    mike.say "I can't understand a word you're saying!"
    "Aletta shakes her head at me in sheer amazement, like I'm biggest moron in existence."
    "And it's then that I realise she may well be right."
    "Because I was the one that gagged her in the first place!"
    "It should have been obvious to me what she was trying to say."
    "That I need to deal with the situation - and fast!"
    audrey.say "Aletta?"
    audrey.say "Are you in there?"
    "Audrey!"
    "She's the last person in the world that I want seeing this."
    "If she has that kind of dirt on me and Aletta, we'll never hear the end of it!"
    "Without asking for permission, I grab Aletta under the arms."
    "She protests as I tip over her chair and shove them both under the desk."
    "But what in the hell does she want me to do - give her a presentation on my plan first?!?"
    audrey.say "Hey, I can hear you in there, Aletta!"
    audrey.say "Screw it, I'm just gonna drop the file you wanted on your desk."
    audrey.say "You're not the only one that's busy around here!"
    scene bg alettaoffice
    "I try to look natural, leaning over Aletta's desk as Audrey bursts in."
    "More muffled protests emerge from beneath the desk as my knees press against Aletta."
    show audrey frown at top_mostleft with moveinleft
    "But luckily the sound of Audrey entering the office is enough to cover them up."
    show audrey frown at left with move
    audrey.say "[hero.name]?!?"
    show fx question at left
    audrey.say "What the fuck are you doing here?"
    show audrey normal
    audrey.say "Where's that uppity bitch Aletta?"
    "Upon hearing the way that Audrey's talking about her, Aletta begins to protest again."
    "But I manage to shove a hand under the desk and clamp it over her mouth."
    if audrey.flags.nickname == "toy":
        mike.say "Oh, she's tied up somewhere else, Little toy."
    else:
        mike.say "Oh, she's tied up somewhere else, Audrey."
    mike.say "And she let me use her office while mine is..."
    mike.say "Erm...being fumigated..."
    mike.say "That's it - my office is being fumigated!"
    "Audrey nods slowly."
    "But she still looks less than convinced by my explanation."
    "Which makes me doubly glad of the fact that she's also the most shiftless person in the office."
    audrey.say "Huh...really..."
    audrey.say "Whatever."
    audrey.say "They don't pay me enough to give a shit."
    "Audrey tosses the file she's holding onto the desk."
    "It's contents spill out as she does so."
    "And it upsets some of the scrupulously neat paperwork already on the desk too."
    show audrey flirt
    audrey.say "Oops - did I make a mess of her nice little system there?"
    audrey.say "Well, Aletta can kiss my ass for all I care!"
    show audrey normal
    "At this last insult, I feel Aletta begin to writhe and wriggle under the desk."
    "Despite the fact that she's bound hand and foot, she still manages to move down there."
    "And the result is an alarming amount of noise, which can't escape Audrey's notice."
    show fx question
    audrey.say "What was that, [hero.name]?"
    if audrey.flags.nickname == "toy":
        mike.say "What was what, little Toy?"
    else:
        mike.say "What was what, Audrey?"
    mike.say "I didn't hear anything!"
    show audrey frown
    audrey.say "Bullshit - I heard a noise from under the desk!"
    mike.say "Oh, that was just me..."
    mike.say "I...banged my knee against the desk, that's all."
    "Audrey still looks less than convinced."
    "And for a moment I think she's actually going to look under the desk."
    "Which would be awkward."
    "As I have Aletta pressed so tightly down there that she can't move a muscle!"
    show audrey normal
    audrey.say "Like I said before - whatever."
    audrey.say "I have better things to do with my time!"
    hide audrey with moveoutleft
    "And with that, Audrey turns on her heel and walks out of the office."
    scene aletta ropeplay
    show aletta ropeplay b ropes blindfold gag
    "Taking a deep breath of relief, I get up and reach under the desk."
    "Aletta squirms and makes more sounds of muffled protest."
    "But none of that stops me from pulling her and the chair upright again."
    "I pull the blindfold off of her eyes, but leave the gag intact."
    show aletta ropeplay -blindfold
    if hero.sexperience >= 20:
        mike.say "Wow, Aletta..."
        mike.say "I don't know about you..."
        mike.say "But I got a real kick out of that!"
        mike.say "It's something we really have to do again!"
        $ aletta.sub += 2
    else:
        mike.say "Oh god, Aletta..."
        mike.say "That was awful..."
        mike.say "We can never do this again!"
        mike.say "You hear me - never!"
        $ aletta.sub -= 2
    "It's just as I finish speaking that I realise what the look in Aletta's eyes means."
    "She's regarding me with a mixture of frustration and sheer amazement right now."
    "And that's obviously because I've left her trussed up like a festive turkey!"
    "Taking a deep breath, I steel myself and begin to untie Aletta."
    "I have no idea what she'll do to me once she's free."
    "But I guess that I probably deserve whatever it is..."
    $ hero.cancel_activity()
    $ game.pass_time(1)
    $ aletta.flags.kinkdelay = TemporaryFlag(True, 1)
    return

label aletta_kink_spy_camera:
    show chibi spy
    "It takes a little while, but I find a good spot for the camera that can see the entire room, and is nearly impossible to see if you're not looking for it."
    $ hero.lose_item("spy_camera")
    $ game.flags.alettakinkspy = True
    return

label aletta_kink_06:
    if aletta.sub.max < 80:
        $ aletta.sub.max = 80
    scene expression f"bg {game.room}"
    "It feels like Aletta and I have gone down a veritable rabbit-hole together recently."
    "Ever since she came to me and asked for help relieving her stress, things have gotten more and more crazy."
    "Especially thanks to the fact that we soon found the best thing to destress her was indulging in kinky shit!"
    "It all started when I accidentally turned on her remote-controlled vibrator in the middle of a presentation."
    "From there, it's grown to the point where there's been spankings and even bondage sessions between us."
    "And all of it happening during the course of the working day with the added danger of discovery that brings."
    "But this time it's different, as I have something more risky in mind."
    "Which Aletta must realise as soon as I ask her to meet me at the office on a weekend."
    "Though she keep her curiosity to herself until the appointed day."
    show aletta work
    "And when she walks through the door of my office, what I have planned is still a mystery to her."
    "Aletta finds me sitting behind my desk, awaiting her arrival with a smile on my face."
    "She crosses her arms over her chest as she regards me, trying to look confident."
    "But I can already tell that she's desperate to know what's in store for her."
    aletta.say "Well, [hero.name] - here I am."
    aletta.say "What's so outrageous that we have to do it now?"
    show aletta embarrassed
    aletta.say "Why not when there's the chance we might get caught in the act?"
    "I nod at this, fully understanding where Aletta's coming from."
    "Of course she loves the idea of someone walking in on us."
    "Her outward image is one of superiority and self-control."
    "So the mere thought of her colleagues seeing her humiliated is crazily powerful."
    mike.say "Oh, I think you'll change your mind, Aletta."
    mike.say "So let's not waste anymore time, shall we?"
    mike.say "I want you to strip, Aletta."
    "I make the command as plain and simple as I can."
    "I don't want to leave any room for misunderstanding."
    "But all the same, Aletta still looks at me aghast."
    show aletta surprised
    aletta.say "You..."
    aletta.say "You can't be serious?"
    aletta.say "What about the security cameras?!?"
    if game.flags.alettakinkspy:
        "I shake my head, keen to dismiss Aletta's fears."
        show aletta dreamy
        mike.say "We don't have cameras in our offices, Aletta."
        mike.say "You know that as well as I do!"
        mike.say "And you won't have to put a foot outside of this room either."
        "Aletta doesn't know a thing about the hidden camera I installed in my office."
        "And hopefully she'll never have to find out either."
        "Which will leave me with a nice little souvenir of today's fun!"
    else:
        "I shake my head, dismissing Aletta's fears."
        show aletta dreamy
        mike.say "You know as well as I do there aren't any camera's in my office, Aletta."
        mike.say "And you won't have to take a step outside of the room while you're naked."
        mike.say "Nobody but me will see you - I promise."
    "Aletta nods slowly, seeing that I'm right."
    "And without as much as another word, she begins to undress."
    show aletta topless with dissolve
    "I watch in complete silence, but I can't keep from smiling the whole time."
    "Sure, I've seen Aletta in compromising positions before."
    "But never with the kind of shame that's showing on her face right now!"
    show aletta underwear blush with dissolve
    "Every piece of clothing that Aletta peels off is like a layer of armour she's shedding."
    "It leaves her that little bit more vulnerable, that little bit more exposed."
    show aletta naked with dissolve
    "Once she's finally naked, Aletta instinctively makes to cover herself."
    "But then the futility of the gesture seems to become apparent."
    "And instead, she slowly lowers her hands, letting her arms fall to her sides."
    "She's looking at me now, just waiting for my next instruction."
    "I've already rehearsed this moment in my head a hundred times."
    "And I simply nod in the direction of the table in the corner of the room."
    mike.say "You know how I like my coffee, Aletta."
    mike.say "So be a good girl, and fix me a cup - now!"
    "A small part of me is honestly expecting Aletta to tell me where I can shove it."
    "So it's both a relief and a thrill to see her almost jump to obey my command."
    "And even more delightful is the sight of her actually doing it."
    "Aletta's full figure bobs and sways as she hurries over to the coffee machine."
    "She pours me a cup with exaggerated care, making sure not to burn herself."
    "I watch with interest as she adds just the right amount of cream and sugar."
    "And then Aletta totters back over to where I'm sitting."
    "She stops a couple of feet from my chair and holds out the coffee."
    "I scrutinise it for a couple of seconds, and then accept it."
    mike.say "That's very good, Aletta."
    mike.say "Now kneel down there while I drink it."
    mike.say "I want you close by if I need anything else."
    "Aletta nods meekly as she settles down on her haunches."
    show aletta naked close
    "She holds my eye the whole time, looking up at me from the floor."
    "I feel like pinching myself, unable to believe that this is actually happening."
    "There was a time when I would have run away and hidden at the sight of Aletta coming my way."
    "And now here she is, sitting at my feet and awaiting my next command!"
    "I could literally ask her to do anything at all."
    "But then I am only human, so I settle upon the most obvious choice..."
    mike.say "This is good, Aletta."
    mike.say "But there's one thing that can make anything better."
    mike.say "I want you to take out my cock and suck it - right now!"
    show aletta surprised
    "Aletta's eyes go wide at this new command."
    "But I see that it's not from offence or outrage."
    show aletta flirt
    "Instead it seems to actually be an eagerness to please!"
    "Aletta hurries to do as she's told, getting onto her knees and leaning in close."
    "She has my flies open in a matter of seconds and my cock out as quickly."
    scene aletta blowjob
    show aletta blowjob ceo naked
    with fade
    "I'm already getting hard from the sight of Aletta kneeling before me."
    "And the moment that her fingers are wrapped around the shaft, it's a done deal."
    "In any other circumstances, Aletta might have been more subtle."
    "And if not, I might have told her to take her time about it."
    "But she's acting on instinct, and I'm caught up in the moment too."
    show mouth_insert aletta zorder 1 at zoomAt(1, (840, 160))
    "This means that Aletta all but shoves my cock into her mouth."
    "She wastes no time in swallowing in as deep as she possibly can."
    show aletta blowjob pleasure
    "And then she begins to work away at it, head bobbing up and down."
    "I try my best to remain aloof, sipping my coffee the whole time."
    "But Aletta's putting so much sheer effort into it that I can't keep it up."
    "I drop the cup of coffee onto the floor and collapse backwards in my chair."
    "Gasping for breath, I hold onto the arms for dear life."
    "It feels like I can't hold on for a moment longer."
    "I'm going to cum!"










    "I just lie back and let Aletta finish the job all on her own."
    "And it doesn't take long for her to do it either."
    show mouth_insert aletta cum zorder 1
    show aletta blowjob cum
    with vpunch
    "I shoot my load when my cock is as deep as it'll go."
    with vpunch
    "But for all her eagerness, Aletta's not ready for it."
    show aletta blowjob ahegao with vpunch
    "She coughs and gags as the cum hits the back of her throat."
    "Yet somehow she still manages to keep from spitting anything out."
    show mouth_insert aletta -cum zorder 1
    "And I watch as Aletta dutifully swallows every last drop."
    hide mouth_insert aletta
    $ aletta.flags.kinkdelay = TemporaryFlag(True, 1)
    return

label aletta_kink_07:
    if aletta.sub.max < 90:
        $ aletta.sub.max = 90
    scene expression f"bg {game.room}"
    show aletta dreamy
    "I can tell that something's up with Aletta almost the moment that we're alone together."
    "Maybe it's the fact that she's normally so good at projecting the aura of being confident and superior."
    "Maybe, in contrast, she's really bad at covering up the fact that she's feeling exposed and vulnerable."
    "Whatever the reason, Aletta stumbles over her words and beats around the bush for a while."
    "And in the end, I have to stop her and try to get to the root of the issue on my own..."
    mike.say "Aletta..."
    mike.say "Is there something bothering you?"
    mike.say "You know - something you want to say, but can't?"
    show aletta embarrassed blush
    "At the mere mention of the idea, Aletta's cheeks flush red with embarrassment."
    "Which in her case is almost as good as an open admission of guilt."
    aletta.say "I...I..."
    aletta.say "I don't know what you mean, [hero.name]!"
    show fx question
    aletta.say "Why would you say that?"
    show fx question
    aletta.say "Why would you even think that?"
    "I honestly can't think of a way to answer Aletta's questions."
    "At least one that wouldn't involve me pointing out the obvious."
    "And so I just give her my best sympathetic smile and raise my eyebrows."
    "Luckily for me, Aletta takes a moment to actually think about what she just said."
    "And then she shakes her head, a look of understanding on her face."
    show aletta sad
    aletta.say "I...I'm sorry, [hero.name]."
    aletta.say "I must sound like a madwoman!"
    mike.say "Well..."
    mike.say "Maybe you wouldn't if you told me what was up, Aletta?"
    mike.say "I mean if you were really honest with me?"
    "Aletta wrings her hands together tightly, almost unable to look me in the eye."
    "I can see that whatever's on her mind, it's seriously affecting her on every level."
    show aletta normal blush
    aletta.say "I have a...a confession to make."
    aletta.say "And it's not been easy for me to handle, [hero.name]."
    "My ears prick up at Aletta's choice of words."
    "Labelling what she has to say as a confession is pretty dramatic."
    "And it's not like Aletta to be dramatic when there's no good reason."
    mike.say "I'm listening, Aletta."
    mike.say "Whatever it is - you can tell me."
    show aletta dreamy
    "Aletta nods and gives me a weak little smile."
    "Which again is unlike her, as it makes her seem instantly vulnerable."
    show aletta normal -blush
    aletta.say "Okay, [hero.name], okay..."
    aletta.say "It's about what we've been doing, you and me."
    aletta.say "How you've been helping to deal with my stress..."
    "Aletta trails off, not feeling the need to go into any more detail."
    "The mere mention of what we've gotten up to recently is enough on it's own."
    "Enough to flood my mind with the images of Aletta's humiliation and submission."
    mike.say "What are you saying, Aletta?"
    mike.say "Has it done the trick?"
    mike.say "Are you trying to tell me that you're cured?"
    mike.say "That you don't need my help anymore?"
    "At the mere mention of what we've been doing coming to an end, Aletta's mood changes."
    "Where before she was embarrassed and shy, she suddenly becomes pleading, almost desperate."
    "Aletta's hand shoots out and grabs hold of my wrist, gripping it tightly."
    "She's squeezing hard, beginning to hurt me!"
    show aletta surprised with hpunch
    aletta.say "NO!"
    show aletta normal
    aletta.say "I...I mean...no!"
    aletta.say "That's not what I mean, [hero.name] - not at all!"
    "I shake my head, unable to see where this is going."
    mike.say "Then what, Aletta?"
    mike.say "What is it that you have to tell me?"
    show aletta blush
    aletta.say "I love it..."
    aletta.say "What you've been doing to me - I love it!"
    show fx exclamation
    aletta.say "In fact, I need it, [hero.name] - I NEED it!"
    "Aletta's eyes are wide as she looks into my own."
    "I don't need to be told that all of her usual defences are down."
    "She's laying herself open to me like never before!"
    if hero.sexperience >= 20:
        "I try to swallow, but find that my throat has suddenly gone dry."
        "Is this really happening to me?"
        "When I met Aletta, she was a ball-breaking bitch."
        "But here she is, a quivering mass of perverted urges!"
        mike.say "Y...you really mean it, Aletta?"
        mike.say "You like what we've been doing?"
        "At this, Aletta all but throws herself at my feet."
        "She clings to me, as if fearing that I might push her away."
        show aletta flirt close
        aletta.say "Oh, [hero.name]!"
        aletta.say "How can you need to ask me that?"
        aletta.say "You're the one!"
        aletta.say "The one that put me in touch with the real me!"
        "I open my mouth to say something - anything."
        "But Aletta's still on a roll and she cuts me off."
        aletta.say "The me you used to know was just a sham."
        aletta.say "You showed me that I'm happiest being submissive."
        aletta.say "You showed me that's what I'm supposed to be!"
        "It's about now that Aletta begins to see the look in my eyes."
        "Not only that, she guesses what it means as well."
        aletta.say "You know what I'm saying, don't you, [hero.name]?"
        show fx question
        aletta.say "And you...feel the same way - don't you?"
        "I can't keep on bottling it up."
        "Not when Aletta's laying herself open like this."
        mike.say "Aletta - I fucking love it!"
        "Aletta nods eagerly, encouraged by the passion of my words."
        "She's clinging to me now, wrapping her arms around me."
        show aletta happy -close
        aletta.say "Oh, [hero.name]..."
        aletta.say "It makes me so happy to hear you say that!"
        aletta.say "So happy I can't wait for you to put me in my place again!"
    else:
        "What have I done to this poor girl?"
        "When I met her, Aletta was an unapologetic, ball-breaking bitch."
        "And now I've reduced her to a quivering mass of perversion!"
        mike.say "Oh god, Aletta!"
        mike.say "I never meant for this to happen!"
        "At the sound of my apology, Aletta goes into overdrive."
        "She shakes her head vigorously, clutching at my hands."
        show aletta surprised
        aletta.say "No, [hero.name]!"
        aletta.say "No, no, no..."
        show aletta normal
        aletta.say "Don't you see?"
        show fx exclamation
        aletta.say "You put me in touch with the REAL me!"
        "I open my mouth to protest."
        "But Aletta's still on a roll and she cuts me off."
        aletta.say "The me you used to know was just a sham."
        aletta.say "You showed me that I'm happiest being submissive."
        aletta.say "You showed me that's what I'm supposed to be!"
        "It's about now that Aletta sees the look in my eyes."
        "And she reads from it that I'm not just disagreeing with her."
        "She can also tell that I'm becoming ever more disturbed with it too."
        aletta.say "I..."
        aletta.say "Well..."
        aletta.say "Maybe we should talk about this another time?"
        "Before I can offer an answer, Aletta turns on her heel and walks away."
        "I know that I should follow her, but I just can't make myself do it."
    $ aletta.flags.kinkdelay = TemporaryFlag(True, 1)
    return

label aletta_kink_08:
    scene expression f"bg {game.room}"
    "I'm pretty much engrossed in what I'm doing when I hear the sound for the first time."
    "At first I think it's somebody coughing or trying to clear their throat, and I ignore it."
    "But each time I hear it again, the sound is getting louder and harder to ignore."
    "In the end I look up to see what the hell is going on."
    "And that's when I find myself looking Aletta straight in the eye."
    show aletta normal
    aletta.say "Ahem..."
    "So it was her making the sound all along."
    "And it looks like she was trying to get my attention too."
    "I can't help narrowing my eyes a little as I stare at Aletta."
    "Because knowing her like I do, this is all very suspicious."
    "Aletta's the kind to normally stride into a room and demand whatever she wants."
    "But now she seems to be waiting, almost politely, for me to notice her."
    "Sure, she looks a little tetchy and impatient as she's waiting."
    "But by Aletta's standards, that's practically submissive!"
    mike.say "Erm..."
    mike.say "Can I help you, Aletta?"
    show aletta blush
    "The moment that I ask the question, I see Aletta's cheeks flush."
    "She seems embarrassed just by the invitation to speak to me."
    show aletta embarrassed
    aletta.say "I..."
    aletta.say "Well I..."
    "I nod and smile, trying to look supportive."
    "I'm just not used to having to coax Aletta like this."
    "Normally I'm the one stumbling over my words, much to her chagrin!"
    mike.say "It's okay, Aletta."
    mike.say "Whatever you have to say, just say it!"
    show aletta normal
    "Aletta nods and tries as best she can to match my own smile."
    "But her effort looks nervous and forced all the same."
    aletta.say "I..."
    aletta.say "I just wanted to say..."
    show aletta dreamy
    aletta.say "All of the...the things we've been doing..."
    aletta.say "The things we've been doing together...for my stress..."
    show aletta normal
    "The moment the words finally leave Aletta's mouth, I understand."
    "I know exactly what this is all about and why she's so nervous."
    "Recently I've been helping Aletta to burn off some of the stress she's built up."
    "And that help has taken the form of some rather intimate physical activities!"
    mike.say "I understand, Aletta."
    mike.say "You feel like you're over it all now, right?"
    mike.say "You want to stop doing what we've been doing together?"
    "Sure, it's not like I want to stop it all myself."
    "Aletta's normally forceful and dominant all the time."
    "So inverting that role and making her subservient was fun."
    "But it was never going to last, not with a girl like Aletta!"
    show fx exclamation
    aletta.say "Oh no!"
    show aletta annoyed
    aletta.say "No, no, no!"
    show aletta sad
    aletta.say "That's not what I meant at all!"
    "Aletta looks almost like she's panicked as she says this."
    "She shakes her head and waves her arms at me in desperation."
    show aletta embarrassed
    aletta.say "I don't want it to stop, [hero.name]!"
    aletta.say "In fact, I want more!"
    show aletta flirt
    aletta.say "I want to be your slave!"
    aletta.say "I want to be your slave on a permanent basis!"
    show aletta normal
    "I blink and stare at Aletta, stunned into silence."
    "At first I can't actually make sense of what she just said."
    "But then the reality of her words begins to sink in."
    "Yet I'm still as amazed even when I can comprehend her request!"
    menu:
        "We can do that":
            if aletta.sub.max < 100:
                $ aletta.sub.max = 100
            "I can't believe what I'm hearing."
            "Aletta's actually begging me to let her be my own, personal slave!"
            "I don't hesitate to nod my head in agreement."
            mike.say "Of course, Aletta!"
            mike.say "If that's what you want."
            "Aletta nods too, clearly delighted with my decision."
            show aletta happy
            "It looks like what we've been up to had more than the desired effect."
            "Because it seems to have changed Aletta's personality for the better."
            "Before she wasn't just stressed, she was bossy and demanding too."
            "I think I prefer this new and improved version of her in every way possible!"
            aletta.say "Oh, thank you!"
            aletta.say "Thank you, [hero.name]!"
            aletta.say "I can't wait to see what you have in store for me next!"
            "My mind is already racing with the possibilities of just what that might be."
            "And I'll be sure to make it something that delights me as much as it does Aletta too!"
            $ aletta.sub += 2
        "I'm not sure":
            "I almost say yes the very next second."
            "I mean, who wouldn't if they'd actually laid eyes on Aletta?"
            "She's everything a guy could want and more besides."
            "But something makes me stop myself."
            "And I think that I know what it is."
            "I'm afraid that what we've been doing is changing Aletta into someone else."
            "Someone different from who she was when I first met her."
            mike.say "Are you still feeling stressed, Aletta?"
            mike.say "I mean, that is why we started doing this in the first place, isn't it?"
            show aletta sad
            "Aletta shakes her head, beginning to look uncertain."
            aletta.say "Well..."
            show aletta embarrassed
            aletta.say "No, [hero.name]..."
            aletta.say "I've been feeling much better recently."
            mike.say "So there's really no need for us to keep doing it, is there?"
            aletta.say "I suppose not..."
            mike.say "Okay, Aletta."
            mike.say "Here's the deal..."
            mike.say "The very moment you feel stressed again, you don't hesitate."
            mike.say "You just stride right in here and demand that I do it all to you again, okay?"
            show aletta happy
            $ aletta.love += 2
            "Aletta nods, slowly at first, but then faster and with more confidence."
            "Then she turns on her heel and strides out, looking more confident with each step."
            hide aletta with moveoutleft
            "She's already starting to look like her old self."
            "Which has to be a good thing, right?"
    return


label aletta_spanking_start:
    "I've been working with Aletta for some time now, long enough that I can normally predict the nature of her visits to my office."
    "And I mean actually predict what's up before she has the chance to open her mouth and say a word."
    "Sometimes I can even manage it before I even look up from my work and acknowledge that she's standing there at all."
    "But of course, I'd never make the mistake of jumping in there and telling her that."
    "Certainly not before giving her the chance to speak."
    "Because after all, I do like the idea of keeping my head firmly attached to my shoulders!"
    "As the alternative would probably be having it torn off and slammed into the bin in the corner of my office."
    show aletta work
    "But today, for some reason, I get the surprise of my life when I look up at the sound of my door opening and see her standing right there."
    "You see I'd been expecting Shiori to bring me in some letter or other at any moment."
    "And the quiet, almost furtive sound of their entrance makes me assume that it's her."
    "There were none of the sounds of pounding footsteps and slamming of doors that usually accompanied Aletta's arrival."
    "And she looks somehow different too, but in a way that I can't immediately put my finger on."
    "With what I hope is an encouraging smile on my face, I wait for her to speak."
    "But Aletta manages to surprise me again, twice in such a small amount of time, by not saying a single word."
    mike.say "Aletta...are you feeling okay?"
    "I'm starting to get worried by now, thinking that she might have terrible news to impart or else collapse in a heap on the floor at any moment."
    "When she finally does manage to respond, it's with a brief nod and then a shake of the head."
    "What the hell is that even supposed to mean?"
    mike.say "Help me out here, Aletta - is that a yes or a no?"
    "She looks at me for a couple of seconds, and then seems to visibly make an effort to pull herself together."
    show aletta surprised
    aletta.say "What..."
    aletta.say "Sorry...sorry, I'm just..."
    show aletta normal
    aletta.say "I'm okay, really I am."
    "I could easily keep on pressing her, but these are the first coherent words she's managed since walking through the door."
    "Under the circumstances, perhaps it'd be better just to take Aletta at her word and see where this is going?"
    mike.say "Okay, Aletta - if you say so."
    mike.say "Now, was there something I can do for you?"
    "Maybe it's the air of formality and professionalism that I manage to keep in my voice that does it."
    "But whatever the reason, Aletta snaps out of the weird funk that she's in and actually answers me almost straight away."
    "I'm also encouraged by the fact that she almost sounds like her usual self too."
    aletta.say "Yes, [hero.name]...yes, of course."
    aletta.say "I wanted to let you know this in person."
    show aletta annoyed
    aletta.say "There's been an error on the project that we've been collaborating on these past few weeks."
    "Even though I'm trying to be calm and collected for Aletta's sake, I can't help throwing my arms up in annoyance at this news."
    mike.say "For fuck's sake, Aletta!"
    "I fully expect Aletta to give me back as good as she gets."
    "But she throws me by almost flinching at the harshness of my language."
    "What in the hell is the matter with her?"
    show aletta sad
    aletta.say "You...you're right to be mad, [hero.name]."
    aletta.say "My best guess is that this is going to cost us at least a week's worth of work, maybe more..."
    "I scrub my hands over my face and then plant my palms firmly on the top of my desk."
    "Taking in a deep, hopefully cleansing breath, I nod in weary resignation."
    mike.say "Okay, Aletta - what exactly did Audrey do this time?"
    show aletta dreamy
    "At this, Aletta shakes her head."
    mike.say "Huh, I'd have assumed it was her without a shred of proof!"
    mike.say "So I guess it was Lavish?"
    mike.say "She's still pretty new and prone to fucking up."
    show aletta blush
    "Again, Aletta shakes her head again - but this time her cheeks visibly redden."
    mike.say "Well, then it has to be Shiori, doesn't it?"
    mike.say "I haven't got any more of my people working on this thing."
    mike.say "And you wouldn't have bothered to come in person if the screw-up was on your side of things - would you?"
    show aletta embarrassed
    "Now Aletta won't even meet my eye, and her cheeks are positively scarlet."
    "All that she manages to do is shake her head for a third time."
    mike.say "So...what?"
    mike.say "It was down to one of your people?"
    mike.say "Look, I appreciate you taking the time to let me know in person, Aletta."
    mike.say "But wouldn't an email have been enough?"
    aletta.say "It...it wasn't one of my people."
    "Aletta seems to be struggling with each and every word that emerges from her mouth."
    show aletta sad
    aletta.say "It was...me."
    "It takes me more than a couple of moments to actually wrap my head around what Aletta's just said."
    "And even then I'm still not sure why she would even admit to such a thing."
    "I mean sure, she's as human as the next person."
    "But she'd usually rather die than admit as much - especially to me!"
    mike.say "Okay, Aletta - it was you that screwed up, and this mess is your fault."
    mike.say "But I still don't see why you had to tell me yourself."
    mike.say "I mean, what makes me so deserving of this special treatment?"
    show aletta dreamy
    "At the mere mention of her favouring me like this, Aletta avoids my eye once more."
    "Wait a minute - is that it?"
    "Does she feel like letting me down is different somehow?"
    show aletta embarrassed
    aletta.say "I don't know..."
    aletta.say "It just made me feel weird somehow."
    aletta.say "It made me feel like I'd let you down."
    show aletta normal
    aletta.say "And I thought that saying sorry might make it stop."
    mike.say "And...has it?"
    "Aletta shakes her head, a confused expression on her face."
    aletta.say "I think I need more than that."
    aletta.say "It's like...like I need to feel that I've been told off for what I've done."
    show aletta flirt
    aletta.say "You know...like I've been...punished."
    "Aletta steals a glance at me, the shame clear to see in the cast of her eyes."
    "Is she...is she actually asking me to...discipline her?"
    menu:
        "Do nothing":
            "What on earth is she even thinking?!?"
            "I can't start spanking another girl around here."
            "The place already feels more like an S&M club than an office most of the time!"
            mike.say "I think you've got your wires crossed on this one, Aletta."
            mike.say "Any disciplinary measures you might be subject to aren't part of my job."
            mike.say "After all, that's what disciplinary panels are for, isn't it?"
            show aletta normal
            "Aletta looks at me in stunned silence for a few seconds, and then seems to shake off her former mood."
            aletta.say "Well, I suppose that you're right, [hero.name]."
            aletta.say "Maybe I'd better take it up with Dwayne instead."
            "And with that, she pushes her glasses up and turns to stride out of my office."
        "Discipline her":
            if aletta.sub.max < 50:
                $ aletta.sub.max = 60
            "Truth be told, I've never seen Aletta in a mood of this kind before."
            "She's awkward, shy and almost desperate for my approval."
            "It's so different from her usual demeanour - and it's also damn hot too!"
            mike.say "You know what, Aletta - I like to think we work in a pretty modern, enlightened kind of environment."
            mike.say "One where we can come to each other and feel free to unburden ourselves of guilt without fear of ridicule or recrimination."
            mike.say "But I also think that, when we do have to resort to discipline, we can be...creative!"
            "At this, Aletta moves closer to my desk, nodding with a sudden interest in my words."
            mike.say "There's no need to get anyone from higher management or HR involved in this, really there isn't."
            mike.say "I think we could sort it out ourselves, with a token gesture."
            mike.say "A physical demonstration of just how sorry you are..."
            hide aletta
            show spank aletta
            "She leans forward, putting both hands on one side of me, and her knees on the other side."
            "I can hear her breath starting to quicken as I come ever closer."
            "But she makes no attempt to move, only watching with wide, expectant eyes."
            "I come to stay still, unable to keep from enjoying the sight of her in that exposed position."
            mike.say "Say if I were to raise your skirt right now..."
            "I say this as I reach out and do the same, taking the hem of Aletta's skirt in one hand and raising."
            "But all the same, a few moments later, the inviting curve of Aletta's buttocks are revealed."
            mike.say "And if I were to draw back my hand, like this..."
            show spank aletta up
            "I slowly raise a hand above Aletta's exposed backside."
            mike.say "Then swing it down like this..."
            show spank aletta spank surprised
            play sound spank
            with hpunch
            "The sound of my palm connecting with Aletta's ass is surprisingly loud."
            "For a moment I fear that someone on the other side of my office door must have heard it."
            "But then Aletta lets out a yelp of pain that makes me totally forget about the blow to her buttocks."
            "It's more of a low gasp than an actual scream, and it seems to be loaded with the confused tension she's filled with right now."
            show spank aletta ready
            mike.say "How did that feel?"
            mike.say "Was it good?"
            show spank aletta normal
            "Aletta nods furiously, glancing back at me over her shoulder."
            mike.say "You want more?"
            "She nods again, biting her lip in anticipation as she looks away."
            show spank aletta pleasure
            show spank aletta up
            pause 0.3
            show spank aletta spank marks
            play sound spank
            with hpunch
            "It's hard to remember just how many times I actually spank her after that."
            show spank aletta up
            pause 0.3
            show spank aletta spank
            play sound spank
            with hpunch
            "But by the time that I'm done, Aletta's cheeks back there are redder than the ones on her face have ever been."
            show spank aletta up
            pause 0.3
            show spank aletta spank
            play sound spank
            with hpunch
            "Aletta hurries to tug her skirt back down and pull herself back together."
            hide spank
            scene expression f"bg {game.room}"
            show aletta blush
            aletta.say "Th...thank you, [hero.name]..."
            "I smile warmly, as I sit down."
            mike.say "You're welcome, Aletta."
            mike.say "Come back any time you feel the need to...apologise to me again!"
            "As she hurries to leave, I wonder if Aletta spotted for a moment just how hard my cock is right now..."
            $ aletta.flags.kinkdelay = TemporaryFlag(True, 1)
    $ hero.replace_activity()
    $ game.pass_time(1)
    return

label aletta_preg_talk:
    $ aletta.flags.toldpreg = True
    show aletta
    aletta.say "[hero.name], are you okay?"
    aletta.say "Seriously, you look terrible!"
    "Great start - aren't I supposed to be the solid rock of a guy, supporting Aletta through whatever's troubling her?"
    "I need to snap out of it and stop being such a pathetic mess!"
    mike.say "It's okay, Aletta...I'm...I'm just worried about you, that's all."
    mike.say "Worried about why you wanted to meet me at such short notice, you know?"
    "Aletta looks at me sideways, as though she's not quite convinced by my explanation."
    "But she nods nevertheless, hinting that what she wants to discuss is more important than her doubts about my sincerity."
    aletta.say "Well, yes...what I have to tell you is quite important - and it does have to do with you specifically."
    "She pauses, and I nod emphatically, not even able to allow her a momentary pause in her delivery."
    mike.say "And that would be...what, exactly?"
    aletta.say "I'm pregnant, [hero.name]."
    "There it is, a bald and frank statement of the basic facts."
    "Trust Aletta not to beat around the bush or waste time gilding the lily."
    mike.say "You're...pregnant?"
    "Aletta raises her eyebrows at the question and my incredulous tone."
    aletta.say "Yes, is that not what I just said?"
    mike.say "Yeah...yeah, I heard you, Aletta."
    mike.say "It's just a bit of a shock, you know...a lot to take in all at once?"
    "Aletta shrugs dismissively at my confusion."
    aletta.say "I really don't see how it's that much of a surprise."
    aletta.say "We did it without protection more than once, and the chances are we were going to get caught out eventually."
    aletta.say "The question you should be asking yourself isn't if you can get your head around it, as you really don't have a choice in the matter."
    aletta.say "I'm pregnant, and that's all there is to it."
    aletta.say "What we need to be thinking about is what we're going to do about it."
    "Typical Aletta, straight to the point and with no time for sentimentality."
    if aletta.status == "fiance":
        show aletta dreamy
        aletta.say "In any other circumstances, I would have been one hundred percent in favour of having a termination."
        aletta.say "But you've already asked me to marry you, [hero.name] - and that changes everything."
        show aletta normal
        aletta.say "It means that we have a real chance to start a family together, build something meaningful - something bigger than the pair of us."
        "I've never heard Aletta talk like this before, as though all of her blunt force was being transformed into a genuine passion for making a future together."
        "I have to admit, it's more than a little scary!"
        menu:
            "Agree":
                "But when I actually start to think about the implications of what Aletta's suggesting, I find a lot of that fear oddly begins to fall away."
                "What am I really afraid of, commitment and spending my life with her and our child?"
                "I've been spending most of my time with her as things are, and I rushed here for fear of something being wrong."
                mike.say "You're right, Aletta - we should grab hold of this and make all that we can out of it."
                mike.say "Plus, I think we'd make pretty great parents, don't you?"
                show aletta happy
                "Aletta raises a quizzical eyebrow at this last statement, but she's already wearing a genuine smile that she just cant suppress."
                aletta.say "Well, that has yet to be seen..."
                aletta.say "But I have to admit, it'll be fun to find out!"
            "Disagree":
                $ aletta.love -= 20
                mike.say "Wow, that's one hell of a big step, Aletta..."
                mike.say "In fact, it's more of a leap than a step, one that you don't know where you're going to land!"
                "I let out a breath of frustration as I try to find the words to express myself without coming across as an irresponsible jerk."
                "And from the look growing on Aletta's face, I can tell that I'm not succeeding."
                show aletta annoyed
                aletta.say "Hmm...I'm beginning to think that I've misjudged you, [hero.name]."
                aletta.say "I thought that you were growing into a more mature and responsible character."
                aletta.say "One upon which I could firmly rely to provide the stability I would need to begin a new chapter in my life."
                show aletta angry
                show fx exclamation
                aletta.say "I can see now that I was wrong!"
                aletta.say "In fact, I need to think again about our entire relationship."
    else:
        aletta.say "I'll be honest with you, [hero.name] - my preferred solution is to have a termination before that's not an option."
        "I feel as though I've been hit with a right hand blow and then caught with the left on the way back."
        "Just when I thought that I was getting used to Aletta's forthright way of dealing with matters too."
        "Somehow it's so much harder to deal with when she's talking about a thing that's so personal to me."
        "Do I want to keep the baby or not?"
        "I suppose that I honestly don't know..."
        menu:
            "Tell her not to do it":
                mike.say "But I'm the father, so I get a say in this, right?"
                "Aletta nods, but not with the kind of expression on her face that says she's looking forward to hearing my input."
                aletta.say "Yes, [hero.name], of course you do."
                aletta.say "Why else would I have told you all this, and not just had the termination if you didn't?"
                mike.say "Well...maybe I think that the best thing would be for us to keep the baby."
                mike.say "What do you say to that?"
                "Aletta looks at me sideways, as if weighing up the whole situation."
                show aletta embarrassed
                aletta.say "Hmm...I'm not totally convinced that you're up to the task, [hero.name]."
                mike.say "I know, I know - but don't worry, I'm one hundred percent committed to proving it to you!"
                show aletta normal
                aletta.say "Well, let's not be hasty - we have a small window of opportunity before a decision has to be made."
                aletta.say "But I have to say that you're going to have to do a lot to convince me!"
            "Agree":
                mike.say "I think you're probably right, Aletta."
                mike.say "I'm not ready to be a parent, and it doesn't sound like you are either."
                "I can't say that Aletta looks happy at this statement, or even relieved to have me agree with her."
                show aletta sad
                "At the best I can only say that she seems oddly sad and yet resigned to they way things have turned out."
                aletta.say "Well, if that's all that you've got to say..."
                aletta.say "I'll call the clinic in the next day or so and make the arrangements."
                mike.say "Aletta...I'll stump up for my share of the bill."
                "Aletta smiles a little sadly at that, nodding so slightly that it's almost impossible to notice."
                aletta.say "Okay...that's decided then..."
                $ aletta.unpreg()
    "With that, we both go our separate ways, and I'm sure Aletta's thoughts are racing as much as mine."
    "But I think that, under the circumstances, we've made the best decision for everyone involved."
    return

label aletta_kiss_me:
    call aletta_greet from _call_aletta_greet_5
    show aletta
    "Being around Aletta for any significant amount of time, you tend to get used to her imperious, no-nonsense attitude to most situations and subjects."
    "I'm sorry, but maybe I worded that in a way that makes you think there's an element of choice involved for anyone interacting with her."
    "Just to clarify, there isn't - you either toughen up and deal with it, or else she grinds you mercilessly beneath her high, pointed heel."
    "This is the exact reason why it takes me completely by surprise when she begins to lean in towards me, closing her eyes and opening her mouth."
    "Is she going to shout in my face, even head-butt me out of some unsaid grudge?"
    hide aletta
    show aletta kiss with fade
    "And then she kisses me - out of nowhere."
    "And it's just impossible to describe...but I'll try all the same."
    "Aletta kisses like she handles most human social interactions, with force and passion."
    "All of that unyielding bossiness and dominating behaviour suddenly begins to make sense to me."
    "As I feel the emotion and almost desperate need for release in the way she pushes her tongue between my lips, I realise that what Aletta desires is perfection."
    "She strives to be the best in whatever she does, and she asks the same of those around her too."
    "Now that our hands are all over each other, I finally understand how much of a challenge it is to earn her trust and be worthy of her affection."
    hide aletta kiss
    show aletta blush at center, zoomAt(1.5, (640, 1040))
    with fade
    "Aletta isn't cold or distant, she just places a high price on her emotions."
    "If you can pay that price, the rewards are every bit its equal in value."
    hide aletta
    $ aletta.flags.kiss += 1
    return

label aletta_birthday_date_male:
    $ DONE["aletta_birthday_date_male"] = game.days_played
    $ game.active_date.clothes = "work"
    scene bg office with fade
    "The office is a pretty weird place when everyone's gone home at the end of the day."
    "It being so quiet makes everything normal suddenly seem strange and even a little creepy."
    "But I know where there's going to be at least one other human being in the place."
    scene bg door office private at center, zoomAt(1, (640, 720)) with fade
    "And that's where I'm making for right now - Aletta's office."
    show bg door office private at center, traveling(1.5, 0.3, (640, 1040))
    pause 0.3
    play sound door_knock
    "I knock once on the door and then let myself straight in."
    scene bg black with dissolve
    pause 0.5
    scene bg alettaoffice
    show aletta work angry
    with wipeleft
    aletta.say "Who's there?"
    aletta.say "Don't just walk in here!"
    aletta.say "I'm busy with..."
    show aletta surprised at startle
    "Aletta's irritable rant trails away as she sees me standing in the open doorway."
    aletta.say "Oh, it's you!"
    show aletta normal
    mike.say "Erm, yeah, Aletta - it's me!"
    mike.say "You forgot, didn't you?"
    show aletta annoyed
    "Aletta becomes instantly defensive at the question."
    "She frowns and shakes her head."
    "And she looks offended at the suggestion."
    aletta.say "Forgot what, exactly?"
    mike.say "Only that today's your birthday, Aletta!"
    mike.say "And we had reservations at the restaurant?"
    show aletta pain
    "Suddenly Aletta's whole demeanour changes."
    "She leans back in her chair and rubs her forehead with one hand."
    aletta.say "For god's sake!"
    aletta.say "I can't believe I forgot..."
    if not game.flags.dwaynedead:
        aletta.say "Dwayne's really been riding me on this project!"
        "I try to push aside the uncomfortable mental image that inspires."
        "And instead I walk into the office and pull something out from behind my back."
    mike.say "Don't worry about it, Aletta."
    mike.say "I called the place, and it turns out they deliver!"
    show aletta normal
    show fx exclamation
    "Aletta's face lights up as I pull the bag of food out and place it on her desk."
    aletta.say "This is food from the place we were going to eat?"
    hide fx
    show aletta happy
    aletta.say "That's really thoughtful of, [hero.name]!"
    show aletta normal
    aletta.say "Did you remember to order my favourite?"
    if hero.knowledge >= 75 or aletta.love >= 180:
        mike.say "Of course I did, Aletta!"
        mike.say "This is me treating you for your birthday."
        mike.say "So I wanted to make sure it was as perfect as possible!"
        "I hand Aletta the container with her meal inside of it."
        "And she takes it eagerly, opening the lid without hesitation."
        "As soon as she sees the contents and smells the aroma, her face lights up."
        show aletta happy
        aletta.say "Mmm..."
        $ game.active_date.score += 15
        aletta.say "I'm really going to enjoy this!"
        show aletta normal
        aletta.say "Thank you, [hero.name]."
    elif aletta.sub >= 50:
        aletta.say "Oh..."
        aletta.say "I'm sorry, [hero.name]..."
        $ game.active_date.score += 15
        aletta.say "I'm sure whatever you have for me will be wonderful!"
        "I nod and smile, pleased with the recovery."
        "And then I hand over Aletta's meal."
        "Which she takes with a nod of gratitude."
    elif aletta.sub <= -50:
        mike.say "Yes, Mistress..."
        mike.say "Of course I did!"
        "I hurry to take out Aletta's meal and place it on the desk before her."
        "Then I open the lids and place some of the plastic cutlery within reach."
        "She watches me with an indulgent smile on her face the whole time."
        "Then she nods with approval once I'm done."
        $ game.active_date.score += 15
        aletta.say "Very good, [hero.name]."
        aletta.say "Your Mistress is pleased."
    else:
        mike.say "Oops..."
        mike.say "Now I wish I had!"
        mike.say "I just ordered stuff that I like."
        mike.say "Is that going to be okay?"
        show aletta flirt
        "I can see that Aletta looks more than a little disappointed."
        "But she does the best she can to hide it from me."
        $ game.active_date.score -= 10
        aletta.say "Sure, [hero.name], sure..."
        aletta.say "I'll make do."
    show aletta normal at center, zoomAt(1.65, (660, 1140)) with fade
    "Pretty soon we're tucking into the meal and chatting between mouthfuls."
    "Sure, this isn't the date I'd planned for us to be having on Aletta's birthday."
    "But the oddness of the situation kind of makes it different, even a little special."
    "It's like we've stripped away all the usual crap that goes along with a date."
    "And instead we're just enjoying the chance to spend some quality time together."
    "Eventually there's a natural pause in the eating and talking."
    "And something piques my interest."
    "Something I hadn't noticed before now."
    if hero.has_skill("work"):
        "I find myself glancing down at the files strewn across Aletta's desk."
        "And I think I can start to see where her frustration's coming from."
        mike.say "Hey, I worked on this project a little too!"
        mike.say "I could probably help you get a handle on it."
        show aletta embarrassed
        aletta.say "I don't know, [hero.name]..."
        aletta.say "It's a pretty complicated one!"
        menu:
            "Help her":
                play sound paper_page
                "I start looking through the papers, ignoring Aletta's warnings."
                "And it doesn't take me long to find what I'm looking for."
                mike.say "You see this chart here, Aletta?"
                mike.say "Once I understood this, it all fell into place."
                "Aletta stares at the place where I'm pointing."
                show aletta surprised
                "And slowly it seems to dawn on her."
                aletta.say "No way!"
                show aletta embarrassed
                aletta.say "I mean...I would have found it in the end."
                $ game.active_date.score += 15
                show aletta happy
                aletta.say "But thanks for the shortcut!"
            "Help her!":
                play sound paper_page
                "I start looking through the papers, ignoring Aletta's warnings."
                "But in my eagerness to help, I pull out a file at the bottom of the pile."
                show aletta surprised
                play sound paper_page
                play sound body_fall
                with vpunch
                "And that brings the whole lot tumbling down, spilling papers onto the floor."
                $ game.active_date.score -= 10
                show aletta angry
                aletta.say "For the love of god, stop it!"
                aletta.say "It took me hours to get those in the right order!"
                "I hold up my hands and back away from the files."
                mike.say "Sorry!"
                mike.say "I was just trying to help."
                aletta.say "Well don't, okay?"
    elif hero.has_skill("cooking"):
        "I turn some of my food over in my mouth, savouring the taste."
        "There's something about it that seems a little different."
        "Aletta seems to notice what I'm doing."
        show fx question
        aletta.say "Is there something wrong with your food?"
        aletta.say "Because mine seems just fine."
        hide fx
        menu:
            "Be sophisticated":
                "I raise an eyebrow at this and chuckle to myself."
                mike.say "Oh please, Aletta!"
                mike.say "It's nothing of the sort."
                mike.say "I was just appreciating the finer qualities of this dish."
                "Aletta looks down at my food with interest."
                aletta.say "Hmm..."
                aletta.say "You want to let me taste it for myself?"
                "I shake my head and put my food out of her reach."
                $ game.active_date.score -= 10
                show aletta sad
                mike.say "I don't think so!"
                mike.say "A culinary experience like this cannot be shared!"
            "Be transparent":
                "I shake my head with a smile."
                mike.say "Oh no, Aletta..."
                mike.say "It's just that I know this recipe very well."
                mike.say "And I think they added something new, like a spice or herb."
                mike.say "You want to see for yourself?"
                show aletta at center, traveling (2.0, 1.0, (660, 1360))
                "I hold out a forkful of my food, and Aletta leans forwards."
                "She lets me place it in her mouth, and holds my eye as she chews it."
                aletta.say "Mmm..."
                $ game.active_date.score += 15
                show aletta happy at center, zoomAt(1.65, (660, 1140))
                aletta.say "That's really good!"
    else:
        "Aletta looks up at me from her food and smiles."
        "I can see that she's tired from all the extra work she's been putting in."
        "But I can also tell that she's really making an effort to show her gratitude."
        aletta.say "You know I must have eaten take-out in this office a hundred times."
        aletta.say "But it was never like this!"
        aletta.say "Maybe it's the company that makes the difference?"
        if hero.charm >= 75:
            "I nod and give Aletta what I hope is a charming smile."
            mike.say "I know what you mean, Aletta."
            mike.say "I think you can make a moment special almost anywhere."
            mike.say "So long as you're with the right person."
            $ game.active_date.score += 15
            show aletta happy
            "Aletta returns my smile and the nod for good measure."
            "In fact, she seems to be finding it hard to look me in the eye right now."
            show aletta blush
            "She even looks like she's blushing a little!"
        else:
            "I snort with laughter and a mouthful of food."
            "Which results in me spraying some onto Aletta's desk."
            mike.say "HAH!"
            mike.say "I think it's more about the food, Aletta."
            mike.say "You were probably eating crap back then."
            mike.say "Not decent shit like this!"
            $ game.active_date.score -= 10
            show aletta annoyed
            "Aletta looks at me sideways, like she's not impressed."
            aletta.say "Yeah..."
            aletta.say "Maybe it's not the company after all!"
    show aletta normal -blush
    "The food seems to be going down pretty well with Aletta."
    "But I have the strangest feeling that something is missing."
    "I keep racking my brain to remember what it is."
    "And then I see Aletta reaching for a bottle of water on her desk."
    show aletta surprised at startle
    mike.say "Drink!"
    "Aletta looks up at me, surprised by my sudden exclamation."
    aletta.say "I beg your pardon?"
    mike.say "I brought something to drink as well!"
    show aletta normal
    "I see interest in Aletta's eyes at the mention of a drink."
    "She nods, encouraging me to pull it out and pour her one."
    if hero.charm >= 75:
        mike.say "A red's the kind of thing we need."
        mike.say "A pretty robust one too."
        mike.say "So it can stand up to the spiciness of the food!"
        "Now the look in Aletta's eyes is really approving."
        "Even more so when I produce two real glasses."
        "Uncorking the wine, I pour her a generous measure."
        "And she doesn't hesitate to try it."
        $ game.active_date.score += 15
        show aletta happy
        aletta.say "Mmm..."
        aletta.say "That's exquisite, [hero.name]!"
    elif aletta.sub >= 50:
        mike.say "A red's the kind of thing we need."
        mike.say "A pretty robust one too..."
        "Before I can finish, Aletta plucks the bottle out of my hand."
        "Then she finds the glasses I brought along too."
        aletta.say "Let me serve you, [hero.name]"
        "I watch as she uncorks the bottle and pours me a generous measure."
        $ game.active_date.score += 15
        show aletta happy
        "Then she smiles as I take a long drink from my glass."
    elif aletta.sub <= -50:
        mike.say "Red wine..."
        mike.say "Only the best for you, Mistress!"
        "Aletta nods in approval as I produce a bottle of wine and two glasses."
        "I hurry to uncork it and pour her a generous measure."
        "And she doesn't hesitate to try it."
        aletta.say "Mmm..."
        $ game.active_date.score += 15
        show aletta happy
        aletta.say "That's exquisite, [hero.name]!"
        show aletta flirt
        aletta.say "Your Mistress is pleased!"
    else:
        mike.say "You're still technically working."
        mike.say "So no alcohol for you, Aletta!"
        "I wag a finger at Aletta as I pull out the bottle."
        show aletta sad
        "And when she sees that it's sparkling water, the sparkle in her eyes disappears."
        "I do the best I can to smile as I pour her a glass."
        $ game.active_date.score -= 10
        "But I get the impression Aletta was hoping for something a little stronger."
    show aletta normal
    "Aletta finishes off the last mouthful of her food."
    "And then she puts down her fork, a smile spreading over her face."
    aletta.say "Phew..."
    aletta.say "That was great, [hero.name]!"
    aletta.say "Are we done eating now?"
    if hero.knowledge >= 75 and hero.charm >= 75 and hero.has_item("pastry"):
        "I can't help responding to the leading question with a grin."
        "Or to be more specific, a knowing grin."
        "Because I'm sure that Aletta's fishing for something."
        mike.say "Oh no, Aletta..."
        mike.say "We're not done quite yet!"
        $ hero.lose_item("pastry")
        "With a flourish, I bring out the dessert."
        $ game.active_date.score += 15
        show aletta happy at startle
        "And it's all that Aletta can do to keep from clapping with delight."
        aletta.say "Oh, [hero.name]!"
        aletta.say "That's just perfect!"
    elif aletta.sub >= 50:
        "I look down at the empty containers and then back up at Aletta."
        "Then I nod my head, holding up the empty bag that I brought it in."
        mike.say "Yup!"
        mike.say "All done!"
        $ game.active_date.score += 15
        show aletta happy
        "Aletta nods, suddenly overcome with gratitude."
        aletta.say "That was such a lovely meal, [hero.name]"
        aletta.say "And I'm so full, I couldn't eat another morsel!"
    elif aletta.sub <= -50 and hero.has_item("pastry"):
        "I shake my head and I fumble for the bag."
        mike.say "Oh no, Mistress..."
        mike.say "We're not done quite yet!"
        $ hero.lose_item("pastry")
        "With a flourish, I bring out the dessert."
        $ game.active_date.score += 15
        show aletta happy at startle
        "And it's all that Aletta can do to keep from clapping with delight."
        aletta.say "Oh, [hero.name]!"
        aletta.say "That's just perfect!"
        aletta.say "You know just how to make your Mistress happy!"
    else:
        "I look down at the empty containers and then back up at Aletta."
        "Then I nod my head, holding up the empty bag that I brought it in."
        mike.say "Yup!"
        mike.say "All done!"
        $ game.active_date.score -= 10
        show aletta sad
        "Aletta nods, but I can see she looks a little disappointed."
        "And then it hits me - I didn't bring dessert!"
        "She's not calling me out on it, so I guess I'll have to play along."
        "But I could kick myself for forgetting something like that!"
    show aletta happy at center, zoomAt(1.5, (660, 1040))
    "Aletta leans back in her chair and takes a long sip of her drink."
    "She looks happy and relaxed right now, so I follow her example."
    show aletta normal
    "But then she looks at me, swirling the contents of her glass."
    aletta.say "Don't you think it's strange..."
    aletta.say "How when you're a kid, you always know what you want for your birthday."
    aletta.say "But as soon as you grown up, you can never think of anything!"
    "I nod and chuckle a little."
    mike.say "I know exactly what you mean, Aletta!"
    "Aletta nods as I agree with her."
    aletta.say "I guess when you're an adult, it's more about the surprise."
    aletta.say "You know what I mean?"
    "Aletta raises her eyebrows, and I realise she's hinting at something."
    "But what could it be?"
    if not hero.has_gifts:
        "I really don't know what she's talking about."
        "So all I can do is shrug and look helplessly at her."
        mike.say "I think I do, Aletta."
        mike.say "Surprises are great."
        mike.say "I like surprises!"
        "Aletta holds her expression for a few moments more."
        "But all I do is keep on staring straight at her in silence."
        $ game.active_date.score -= 20
        show aletta annoyed
        "Eventually she lets out a sigh and shakes her head."
        aletta.say "Yeah, [hero.name]..."
        aletta.say "Surprises really are great."
        $ aletta.love -= 10
        aletta.say "Being oblivious, not so much..."
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift
        if _return != "done":
            if _return not in ["None", "exit"]:
                "Of course - I'm such a dumbass!"
                "She's hinting that it's gift time."
                mike.say "I think I do, Aletta..."
                mike.say "You mean a surprise like this?"
                "I whip out the gift and hand it over to her."
                "And Aletta does her best to look totally surprised."
                show aletta dreamy
                aletta.say "Oh, [hero.name]..."
                aletta.say "You shouldn't have!"
                if _return:
                    play sound [paper_ripping_2, paper_ripping_1]
                    pause 1.0
                    show aletta surprised at startle
                    "As soon as she tears off the paper, Aletta looks stunned."
                    "She turns the gift over in her hands, like she's lost for words."
                    mike.say "Erm..."
                    mike.say "Is it okay?"
                    show aletta normal
                    "Aletta looks up and instantly starts to nod."
                    $ game.active_date.score += 20
                    show aletta happy
                    aletta.say "It's perfect, [hero.name]!"
                    aletta.say "How on earth did you know?"
                    mike.say "Oh..."
                    mike.say "Let's just say I heard you dropping a few subtle hints!"
                else:
                    play sound [paper_ripping_2, paper_ripping_1]
                    pause 1.0
                    show aletta sad
                    "As soon as she tears off the paper, Aletta's face drops."
                    "She puts the gift down and pushes it away from her."
                    mike.say "Erm..."
                    mike.say "Is it okay?"
                    "Aletta looks up with a disinterested expression on her face."
                    $ game.active_date.score -= 10
                    show aletta annoyed
                    aletta.say "It's fine, [hero.name], just fine."
                    aletta.say "Thank you."
                    "I nod and force a smile onto my face."
                    "But it doesn't sound like it's fine."
                    "In fact, I don't think she likes it at all!"
            else:
                "I really don't know what she's talking about."
                "So all I can do is shrug and look helplessly at her."
                mike.say "I think I do, Aletta."
                mike.say "Surprises are great."
                mike.say "I like surprises!"
                "Aletta holds her expression for a few moments more."
                "But all I do is keep on staring straight at her in silence."
                $ game.active_date.score -= 20
                show aletta annoyed
                "Eventually she lets out a sigh and shakes her head."
                aletta.say "Yeah, [hero.name]..."
                aletta.say "Surprises really are great."
                $ aletta.love -= 10
                aletta.say "Being oblivious, not so much..."
    scene bg alettaoffice
    show aletta work
    with fade
    "I start collecting up the remains of our meal, tidying as I go."
    scene bg alettaoffice at center, zoomAt (1.65, (1000, 1000)) with fade
    pause 1.0
    scene bg map night with fade
    "But then I find myself looking out of the window at the city below."
    "It's well into the night by now, and the lights seem to go on forever."
    scene bg alettaoffice at center, zoomAt (1.65, (1000, 1000)) with fade
    pause 1.0
    show aletta work dreamy at center, zoomAt(1.5, (760, 1040)) with easeinright
    "Aletta notices that I'm staring out of the window, and she comes to join me."
    aletta.say "You know something, [hero.name]..."
    aletta.say "I never stop to do that."
    aletta.say "I'm in here at all hours of the day and night."
    aletta.say "But I never took the time to just appreciate the view!"
    "As Aletta says all of this, I feel her take hold of my hands."
    show aletta normal
    "I turn to face her, and I see she's looking deep into my eyes."
    menu:
        "Kiss Aletta":
            hide aletta
            show aletta kiss work with fade
            "I don't hesitate to step forwards and kiss Aletta."
            $ game.active_date.score += 15
            "And it seems that this was just what she wanted."
            "Because she returns the kiss with obvious enthusiasm."
            "It lasts for a long time and even when it's over we don't part."
            hide aletta
            show aletta work dreamy at center, zoomAt(1.5, (760, 1040))
            with fade
            "We remain wrapped in each others arms, just looking at the city spread out before us."
            $ aletta.flags.kiss += 1
        "Take a step back":
            scene bg alettaoffice
            show aletta work
            with fade
            "I take a step back, shaking my head."
            if not (Harem.find_by_name("office") and Harem.find_by_name("office").is_active(aletta)):
                mike.say "We shouldn't get too comfortable, Aletta."
                mike.say "Someone might walk in on us."
                mike.say "You know, find out we're fooling around on company time?"
            $ game.active_date.score -= 10
            show aletta embarrassed
            "Aletta looks more than a little put out by this."
            "But she keeps her response to a curt nod."
            "And then she turns her back on me, walking away from the window."
    show aletta surprised
    aletta.say "Oh my..."
    aletta.say "Is that the time?"
    show aletta normal
    "I follow Aletta's example, checking the time for myself."
    "And when I see it, I'm as surprised as she is."
    mike.say "Wow!"
    mike.say "It really is late!"
    if game.active_date.score >= 80 and aletta.sexperience >= 1:
        show aletta flirt
        aletta.say "We should go to bed, right now!"
        mike.say "Okay, Aletta..."
        mike.say "If that's what you want!"
        "I turn to walk away."
        with hpunch
        "But I find that Aletta's still holding onto my hand."
        "I look up at her with confusion written all over my face."
        mike.say "What are you..."
        show aletta wink
        aletta.say "I mean together, you dope!"
        "I nod and then begin to smile as realisation dawns on me."
        scene bg street with fade
        "Quickly we get ready to leave, and then slip out of the building."
        "Then we head back to my place, not stopping until we're at the front door!"
        call aletta_birthday_sex from _call_aletta_birthday_sex
    else:
        show aletta angry
        aletta.say "And I have to be back here early tomorrow too!"
        show aletta normal
        aletta.say "So I'd better head home and get some sleep."
        "I nod and begin to gather up my things."
        "It's not the answer I wanted, for sure."
        "But if Aletta's tired, then I should let her get some rest."
        scene bg street with fade
        "So once I'm ready to leave, I slip out of the building."
        "And then I head home alone."
    return

label aletta_birthday_sex:
    scene bg house
    show aletta work at center, zoomAt(1.5, (660, 1040))
    with fade
    "The journey home from the office passes in what feels like the blink of an eye."
    "All I can seem to remember is the sensation of Aletta's hands all over me."
    "That and the feeling of her lips pressed against mine, her tongue in my mouth too!"
    "It could be that she's got the need to shake off the shackles of the office."
    "But I'd rather believe that she's been worked into such a passion by my own efforts."
    "Because it was me that managed to save the date she'd forgotten all about."
    "And on her own birthday too!"
    "I'm still wondering about that as Aletta grabs my hand and pulls me inside the house."
    play sound door_slam
    scene bg bedroom1
    show aletta close work flirt
    with hpunch
    "Then I find myself hustled into my bedroom and the door slammed firmly shut behind us."
    "For a moment I actually think that Aletta's going to go even further."
    "Like she's going to jam a chair under the door handle to make sure we're not disturbed!"
    "But instead she pushes me towards the bed, and I have no choice but to go along with it."
    "Hell, it's not like I'm going to resist, is it?"
    show aletta -close with vpunch
    "And it comes as no surprise to me that as soon as I reach the bed, she shoves me onto it."
    "I tumble backwards, landing on the mattress and staring up at Aletta."
    "Which means that I have a spectacular view of her."
    "And it's one that gets even better a moment later."
    show aletta underwear with dissolve
    "Because that's when she starts to slowly strip off her clothes!"
    aletta.say "I had a really great time tonight, [hero.name]."
    aletta.say "I was so caught up in my work."
    aletta.say "I was in another world!"
    "I nod as I watch Aletta stripping down to her bra and panties."
    "For all I know right now, she could be speaking a foreign language!"
    aletta.say "But you reminded me that work isn't everything."
    aletta.say "You reminded me that I need to find time to have fun too."
    aletta.say "And I think I figured out a pretty good way to do that."
    aletta.say "One that'll let me reward you at the same time too..."
    show aletta topless with dissolve
    "Aletta unhooks her bra and drops it onto the floor."
    show aletta naked -topless with dissolve
    "Then she pulls down her panties and steps out of them."
    show aletta close
    "Finally naked, Aletta climbs onto the bed and lies next to me."
    "Without waiting for permission, she begins to take off my clothes too."
    "I do the best I can to help her."
    "But in my excitement, I'm all fingers and thumbs."
    "After much fumbling, the job is finally done."
    "And then Aletta pushes herself up on the bed and straddles my thighs."
    "She's not messing around either, as she instantly grabs my cock."
    "Working it with one hand, Aletta gazes down at me."
    "She has that knowing look on her face."
    "The one only a truly confident woman can pull off."
    "And the one that's guaranteed to make me hard in no time at all!"
    aletta.say "Hmm..."
    aletta.say "You like that, yeah?"
    mike.say "Y...yeah, Aletta..."
    mike.say "It feels great!"
    "She nods, smiling slowly as my cock gets harder in the palm of her hand."
    show aletta cowgirl vaginal with fade
    "As soon as it's ready, she begins to rub it against her belly."
    "A little at a time, Aletta pushes it downwards."
    "This means that it inches it's way towards her pussy."
    "And by the time it finally gets there, I'm almost panting with anticipation."
    "Aletta's fully aware of the state she's got me in."
    "She chuckles and shakes her head."
    show aletta cowgirl pleasure vaginal down
    "But then she takes me by surprise, pushing downwards all of a sudden."
    "There's a moment of resistance, and then it happens."
    "The lips of her pussy part, and my cock slides into her."
    "Aletta slips down onto it, faster than either of us anticipated."
    "And now it's not just me that's panting and gasping."
    "Aletta looks me straight in the eye."
    "And in that moment, it's almost like I can read her thoughts."
    "I know that she needs me to take charge."
    "My hands reach up and take a firm hold of Aletta's waist."
    show aletta cowgirl raised
    pause 0.35
    show aletta cowgirl down
    pause 0.35
    show aletta cowgirl raised
    pause 0.35
    show aletta cowgirl down
    "And then I begin to move inside of her, slowly at first."
    "As soon as that happens, she bites her lip and nods."
    "But the speed of her nodding picks up almost instantly."
    "Without pause, I begin to go faster too."
    show aletta cowgirl raised
    pause 0.2
    show aletta cowgirl down
    pause 0.2
    show aletta cowgirl raised
    pause 0.2
    show aletta cowgirl down
    pause 0.2
    show aletta cowgirl raised
    pause 0.2
    show aletta cowgirl down
    pause 0.2
    show aletta cowgirl raised
    pause 0.2
    show aletta cowgirl down
    "And it looks like I guessed right, as Aletta moans at my efforts."
    aletta.say "Uhh..."
    aletta.say "Oh yes..."
    aletta.say "Just like that!"
    show aletta cowgirl down
    pause 0.2
    show aletta cowgirl raised
    pause 0.1
    show aletta cowgirl down
    "By now I'm going as fast as I can, thrusting up and down."
    "I'm holding onto Aletta so tightly that I'm afraid of leaving bruises."
    "But all the same I don't dare to loosen my grip for a second."
    show aletta cowgirl raised
    pause 0.2
    show aletta cowgirl down with vpunch
    "Aletta's pushing down with all of her weight too."
    "And yet she still looks like she's riding a bull in a rodeo."
    "She sways back and forth, her breasts bouncing the whole time."
    "Finally something seems to snap inside of Aletta."
    show aletta cowgirl raised
    pause 0.2
    show aletta cowgirl down ahegao with vpunch
    "She casts her head back and almost screams."
    if aletta.flags.submissive_interact:
        aletta.say "Use me as your target practice!"
        with hpunch
    "And her hands are all over her body in that moment."
    show aletta cowgirl raised
    pause 0.2
    show aletta cowgirl down with vpunch
    "I realise that she's cumming, her orgasm taking over."
    "That's more than enough to set me off too."
    show aletta cowgirl raised
    pause 0.2
    show aletta cowgirl down creampie with vpunch
    "With one last thrust upwards, I let go and shoot my load."
    "This seems to push Aletta even further, making her twist and writhe."
    show cuddle aletta
    show pussy_insert aletta cum zorder 1 at zoomAt(0.75, (40, 200))
    with fade
    "Then she collapses atop me, utterly spent."
    "I don't move, enjoying the sensation of Aletta's body against mine."
    "And it comes as no surprise when I hear the sound of gentle snoring a moment later."
    "After all the work she's put in on her birthday, I think Aletta's earned the right to sleep."
    hide pussy_insert
    $ aletta.sexperience += 1
    call sleep ("aletta") from _call_sleep_64
    $ game.room = "bedroom1"
    return

label aletta_event_01:
    scene bg office
    if aletta.love.max < 20:
        $ aletta.love.max = 20
    $ aletta.unhide()
    $ Room.find("alettaoffice").unhide()
    "I am ready to bang my head against my desk staring at the code on my computer."
    "This morning has been rather stressful so far at work."
    "I need to tell Aletta she needs to take this assignment over if it is this impossible."
    "I let out a sigh of relief when I see it is finally time for my break."
    "Without a second thought I get up and go to the break room."
    "I keep my eyes straight ahead not wanting to deal with anyone just yet."
    scene bg breakroom with fade
    "Pushing open the door to the break room I almost don't notice the cool breeze or the faint hint of cigarette smoke."
    show aletta_window_bg
    show aletta work dreamy at center, zoomAt(1.25, (720, 880))
    with fade
    "Distracted from my bad mood I look around the room and to my surprise find Aletta at the corner window smoking."
    "She doesn't seem to notice me."
    menu:
        "Tell her it's forbidden":
            show aletta_window_bg at center, traveling(1.35, 0.5, (720, 880))
            show aletta at center, traveling(1.5, 0.5, (740, 1040))
            "I walk over to her.."
            mike.say "Smoking is forbidden inside the building."
            show aletta normal
            "She turns and raises an eyebrow at me. Apparently, she did know I was in there."
            show aletta angry
            aletta.say "You think I don't know that?"
            show aletta annoyed
            "She blows smoke out of the side of her mouth out the window and I notice how her lipstick hasn't smudged a bit."
            "How does she do that?"
            show aletta angry
            aletta.say "I've been working here long enough that they won't fire me for sneaking a cigarette."
            show aletta upset
            "She flips ashes out the window."
            show aletta angry
            aletta.say "I've also been here long enough to not give a damn about the rules or if they fire me."
            show aletta talkative
            aletta.say "Besides, I got friends in cooperate. They'd help me get back on or a new job if I wanted."
            $ aletta.love -= 1
        "Tell her it's unhealthy":
            "Feeling like I should say something, but not brave enough to mention the rules..."
            mike.say "Do you know how unhealthy smoking is for you?"
            show aletta sadsmile
            "Aletta turns a tired look on me, like she had heard this line more than she likes."
            show aletta talkative
            aletta.say "I don't do it for my health, I do it to relax."
            show aletta normal
            "She takes a puff and then blows the smoke out the window."
            show aletta talkative
            aletta.say "Stress can kill you just as fast as cigarettes. And working here?"
            show aletta happy
            aletta.say "Maybe faster."
            show aletta normal
            "She flips her ashes out the window."
            show aletta talkative
            aletta.say "So don't lecture me about what's good for me. I'll be the judge of that."
            show aletta normal
            "I did see a way to argue that so I just shrug."
            $ aletta.love += 1
        "Ask if she has an extra":
            "I felt like trying my luck. If the boss is smoking in the break room, how could she seriously tell me I couldn't?"
            mike.say "Do you have an extra smoke?"
            show aletta stuned
            "She looks at me first in surprise and then with a smirk."
            show aletta normal
            "Placing her cigarette in her mouth she shakes another loose for me and holds it out."
            show aletta talkative
            aletta.say "Need a light?"
            show aletta normal
            "I nod and she hands me her lighter as well."
            "After taking a puff I hand it back and pull up a chair so I can sit by the window as well."
            "It seems odd to be smoking with my boss, but somehow calming as well."
            $ aletta.sub += 1
        "Say nothing":
            "I decide it is best to say nothing, but Aletta sees me before I can make my way to the fridge and leave."
            show aletta normal
            "Blowing out smoke in annoyance she turns toward me."
            show aletta talkative
            aletta.say "I suppose this is awkward."
            show aletta normal
            "I shrug, still not believing I am seeing my tight knit boss breaking one of the company rules."
            show aletta talkative
            aletta.say "Relax, rules get broken every day and the world still spins."
            show aletta normal
            "She did have a point."
    "I realize there's really no reason to rush."
    "I mean after all I was in no hurry to go back to my desk and Aletta didn't seem bothered by me being there."
    show aletta_window_bg at center, traveling(1.35, 0.5, (740, 880))
    show aletta at center, traveling(1.5, 0.5, (720, 1040))
    "Getting my lunch and an extra coke out of the fridge for Aletta I walk back over to her window."
    "Seeing me set the coke down in front of her she gives a small smile."
    show aletta happy
    aletta.say "Thanks [hero.name]."
    show aletta normal
    mike.say "No problem."
    show aletta dreamy
    "I watch her manicured nails open the tab as her red lips hold her cigarette all the while she looks out the window at nothing in particular."
    "She then takes the cigarette out of her mouth, and takes a sip of her coke."
    "The break room is quiet except for the faint sound of traffic."
    "It's the first calm I have felt all morning since coming to work."
    "As I eat I look to Aletta and see how tired she looks with her guard down."
    "I don't think I have ever seen her with her guard down."
    mike.say "Rough morning?"
    show aletta happy at startle
    "She gives a laugh but it doesn't sound like any humor is in it."
    show aletta talkative
    aletta.say "You don't know the half of it."
    show aletta whining
    aletta.say "Three people late, two sick, deadlines that are now impossible to make and corporate is riding my ass like it's somehow my fault?"
    show aletta annoyed
    "She shakes her head after making another puff."
    "She blows the smoke out of her very feminine lips."
    show aletta angry
    aletta.say "Let me hire decent people and maybe it wouldn't happen..."
    show aletta stuned
    "Suddenly she flashes a look..."
    show aletta whining
    aletta.say "That wasn't directed at you- you're a good worker [hero.name]."
    show aletta sadsmile
    mike.say "Don't worry, no offence taken."
    show aletta dreamy
    "She seems to relax again, going back to her cigarette."
    "I think this is the most human I have seen Aletta in the entire time I have known her."
    "I feel bad as I realize I never once thought about how much stress she must be under being the boss."
    "And only minutes ago I was annoyed at my desk job when I was only responsible for my own work, and could ask for help whenever I got stuck."
    "Aletta was responsible for dozens of us, and had no help."
    mike.say "You know, maybe if a few people got fired for 'not calling in' you could get a few new employees in."
    show aletta sadsmile
    "Aletta seems confused but then what I am saying seems to dawn on her."
    show aletta talkative
    aletta.say "Very true, [hero.name] I'll have to go check the call logs after my break. Thanks for the reminder."
    show aletta normal
    mike.say "Anytime Boss."
    "Standing up I gather my things to go back to work."
    "I decide I can figure out the code on my own if I try a little harder."
    hide aletta
    $ hero.fun += 1
    $ hero.energy += 1
    $ DONE["coffee_break"] = game.days_played
    $ hero.cancel_activity()
    return

label aletta_event_02:
    scene bg office
    if aletta.love.max < 40:
        $ aletta.love.max = 40
    "I lean back in my desk chair and stretch my arms over my head as I smile having just wrapped up a difficult assignment."
    "I feel rather accomplished for the day and it is not even noon yet."
    "I don't get to enjoy my moment of relaxation long when suddenly I hear a commotion out in the hallway."
    "Curious, I get up to go see what is going on."
    show aletta normal at center, zoomAt(1.0, (840, 720))
    show victor casual at center, zoomAt(1.25, (440, 890)), blacker
    with fade
    "I come up to a scene of another worker screaming in Aletta's face while she calmly stands there with her hands on her hips and everyone just watches."
    show fx anger at center, zoomAt(1.0, (840, 720))
    "I see how pissed off she is behind her composure."
    "I hear someone snicker before turning to see a female coworker whispering in another one's ear, and I get the feeling they are not on Aletta's side."
    "I remember the day Aletta was smoking in the break room and how stressed she was. This isn't right."
    show victor casual at center, zoomAt(1.0, (440, 890)), blacker, startle
    "Coworker" "You ask too much from us!"
    "Coworker" "You are just a lazy bitch who pushes all of your own work onto the rest of us and then complain when we can't get it and our own work done on time!"
    "Coworker" "I'm sick of being your lackey!"
    "Why wasn't anyone saying anything?"
    "Whether they liked Aletta our not, this was wrong."
    menu:
        "Stand up for Aletta":
            show victor casual at center, zoomAt(1.25, (400, 890)), blacker with ease
            mike.say "I think you need to back off buddy."
            "I take a step forward and become aware that all eyes are now on me."
            "Coworker" "Who are you?"
            "The guy sneers at me."
            mike.say "I'm [hero.name], and that just so happens to be our boss that you are disrespecting."
            mike.say "Don't you have any manners? You sound like a spoiled child."
            "Now there are snickers at the man who seems embarrassed."
            mike.say "If you knew half of the work Aletta does, you wouldn't have a leg to stand on."
            "There are more murmurs around the workers as those who had just been siding with this guy were now unsure of themselves."
            "Coworker" "Pff whatever. You're just an ass kisser."
            hide victor with easeoutleft
            "He turns and makes his exit as if he has won but I can tell he is eager to get out of here."
            "I just shake my head."
            "He didn't even give me a chance to respond."
            "Everyone starts to go back to work and I see Aletta looking at me with thankful eyes."
            show aletta talkative at center, traveling(1.25, 0.3, (640, 880))
            aletta.say "That was nice of you to step in."
            show aletta normal
            "I shrug."
            mike.say "It was nothing. I was just trying to do the right thing."
            show aletta happy at startle
            "She gives a bitter laugh."
            show aletta talkative
            aletta.say "No one else was going to. You'd think as much as they all come to me with their problems they would be a little more grateful."
            $ aletta.sub += 1
            $ aletta.love += 1
        "Keep watching.":
            "The guy keeps yelling at Aletta. She can barely get a word in, and when she does she is almost drowned out by him."
            "But that is only because she is trying to stay professional."
            "Security finally comes."
            "Officer" "What's going on here?"
            "Coworker" "Nothing. We are just having a conversation."
            mike.say "You think screaming at your boss is a conversation?"
            "He sneers at me."
            "Coworker" "Who are you?"
            mike.say "Doesn't matter."
            "Officer" "Okay well if everyone can just go back to work there will be no need for further action."
            hide victor with easeoutleft
            "The guy glares at Aletta, and then me, but finally agrees and goes back to work."
            "Security also leaves and with the show ever everyone goes back to their desks."
            "Except me."
            show aletta sad at center, traveling(1.25, 0.3, (640, 880))
            "Aletta looks tired and I find myself walking over to her."
            mike.say "Are you okay?"
            show aletta stuned
            "She looks to me slightly surprised."
            show aletta talkative
            aletta.say "All in a days work."
    aletta.say "I need a smoke now after all of that. Care to join me?"
    scene bg breakroom with fade
    "I am surprised that my boss was inviting me on a smoke break, but I follow her to the break room anyway."
    show aletta_window_bg
    show aletta work dreamy at center, zoomAt(1.25, (720, 880))
    with fade
    "She offers me one but I'm not brave enough to push my luck today. It's not even my break yet."
    "She lets out a sigh after lighting her cigarette."
    show aletta b pain
    "She rubs her neck as if it hurts."
    menu:
        "Offer to give her a massage":
            mike.say "Does your neck hurt?"
            "Looking at me out of the corner of her eye she blows smoke out the window."
            aletta.say "When doesn't it? It's just tight like my shoulders."
            mike.say "Here, let me help."
            hide aletta
            scene bg breakroom
            show slap_npc_aletta at center, zoomAt(1.4, (640, 1080))
            show slap_outfit_aletta_work at center, zoomAt(1.4, (640, 1080))
            show slap_exp_happy_aletta at center, zoomAt(1.4, (640, 1080))
            with fade
            "I stand behind her and start rubbing her shoulders and neck gently."
            "At first she stiffens and then eases into it."
            "I hear her let out a sigh of relief. And she leans her elbow on the window sill."
            aletta.say "You're really good at that [hero.name]."
            mike.say "Thanks. Maybe I can do it more often if you would like?"
            aletta.say "Maybe I'll let you. I'll keep it in mind."
            "I keep massaging until she tells me it feels better than it has in a long time."
            $ aletta.love += 1
        "Tell her she should go get a massage":
            mike.say "Does your neck hurt?"
            "She glances at me as she takes a puff."
            aletta.say "Yeah, but when doesn't it?"
            aletta.say "Part of the job description."
            mike.say "Maybe you should treat yourself to a massage at a spa?"
            show aletta sadsmile
            "She looks to me and I think I catch a hint of disappointment in her eye before it is gone."
            show aletta talkative
            aletta.say "Oh."
            show aletta a normal
            "She drops her hand."
            show aletta talkative
            aletta.say "Maybe. I'll look into that."
            show aletta dreamy
            "She goes back to looking out the window and smoking her cigarette."
    show aletta_window_bg
    show aletta work dreamy at center, zoomAt(1.25, (720, 880))
    with fade
    "I don't know what it is about Aletta that changed, but I feel myself getting closer to her when she is like this."
    "I feel the need to say something when suddenly the door to the break room opens and Aletta's almost finished cigarette goes out the window."
    show aletta talkative
    aletta.say "That's correct [hero.name], so if you continue at the pace you are going you should have no trouble finishing your work by the deadlines this week."
    aletta.say "Good job on getting that assignment for yesterday finished, I understand it was a difficult one."
    show aletta normal
    "I am confused as to what she is talking about for a moment but then realize she is acting."
    mike.say "Um... thank you. I just wanted to make sure."
    "Make sure of what I didn't know. I glance to the other worker that came in as they get a drink out of the fridge and leave not having noticed Aletta was smoking."
    show aletta happy
    "After the door shuts Aletta smiles to me."
    show aletta talkative
    aletta.say "Guess our break times over."
    aletta.say "Better get back to work before someone more observant comes in."
    show aletta normal
    "She shuts the window and I can't help but watch a little disappointed as she leaves."
    scene bg black with dissolve
    return

label aletta_event_03:
    scene bg alettaoffice
    if aletta.love.max < 60:
        $ aletta.love.max = 60
    $ aletta.flags.nodate = False
    $ aletta.flags.nokiss = False
    "The deadlines at work this week are ridiculous."
    "So much so they are pretty much impossible to get done on time without working over. But did anyone volunteer?"
    "No, of course not."
    "So that is why Aletta came to me and 'suggested' I stay after when I first got to work this morning."
    "At first I was dreading it, but throughout the day as I imagined being alone with her I started to look forward to it until it was what was getting me through my regular shift."
    show aletta close work dreamy
    "Now that she is sitting next to me I felt like the temperature in the room has gone up ten degrees."
    "What am I thinking?"
    "She is my boss."
    "But I find myself sitting closer throughout the night and she doesn't stop me."
    "Seeing her breasts peeking out of her shirt starts to make my heart beat a little bit faster."
    show aletta normal
    "Exactly what do I expect to happen tonight? That's right. Nothing. Because she is my boss. I need to get a grip of myself."
    "A grip... hmm maybe that isn't such a bad idea."
    "Maybe that's just my problem, I need to get off."
    "I could go to the bathroom real quick and jerk off and she would never know."
    show aletta talkative
    aletta.say "[hero.name]..."
    aletta.say "[hero.name] are you listening to me?"
    show aletta normal
    "I shake myself out of my thoughts."
    mike.say "Uh, what? Sorry. I kind of zoned out."
    show aletta annoyed
    "I try to laugh it off but she doesn't look happy with me."
    show aletta talkative
    aletta.say "I'll go over it again, but pay attention this time."
    show aletta normal
    "In no time I am zoned out again just watching her lips move and barely catching what she is saying."
    menu:
        "Brush against her arm":
            "I lean slightly closer as if to see the report she is showing me better and brush my arm against hers."
            "To my surprise she doesn't flinch away."
            "So I decide to keep my arm there and she doesn't move away."
            "Trying to hide my smirk I feel a surge of confidence."
            "But also blood rushing south."
            "Oops."
            $ aletta.love += 1
        "Keep some space between each other":
            "I lean on my right arm to keep from moving any closer to her."
            "At first she keeps talking but then glances my direction and there is a flicker of disappointment before she continues with what she is telling me."
            "Is it just my imagination?"
    show aletta talkative
    aletta.say "So do you understand what I am saying?"
    show aletta normal
    mike.say "Uh, yeah. I-I mean, yes, Aletta. I should be able to get it done no problem."
    show aletta b -glasses
    "She seems to relax into her chair for the first time, taking off her glasses and putting one ear piece to her lips."
    show aletta happy
    aletta.say "That's a relief. I was really worried about how to get this assignment done. I really don't need corporate on my ass again."
    show aletta b pain
    "She sighs and reaches back to rub her tense shoulders."
    show aletta dreamy
    "I want so badly to rub them for her but don't trust myself to be able to stop there."
    "The thought of having her bent over the desk out in the open with her skirt pushed up."
    "Wait what? Since when am I someone who falls for their boss?"
    "Am I falling for her? Or am I just horny?"
    "It has to be just horny. And she is an attractive woman. It is understandable."
    "That's it, I need to go take care of this."
    show aletta normal
    mike.say "Don't worry about it Aletta, I'll have it done before I leave here. I'm just going to go to the bathroom real quick."
    show aletta talkative
    aletta.say "No problem, [hero.name], it really is a great help."
    show aletta normal
    "She suddenly drops some of her papers as she turns in her chair to get up."
    show aletta surprised
    aletta.say "Oh-."
    show aletta sadsmile
    mike.say "Don't worry I got them!"
    "I quickly drop to the floor before she can get out of her seat and gather them up. Some slide under the desk and I have to crawl under."
    hide aletta
    show aletta ropeplay work
    with fade
    "When I come back up I turn my head and my heart jumps when I realize I can see up her skirt and can't tear my eyes away."
    "At first I think I am imagining that her legs are opening wider to show her panties and I can't believe my luck until she talks."
    show aletta ropeplay b pleasure
    aletta.say "You know, it is quite rude to stare."
    show aletta ropeplay normal
    play sound "<from 0 to 0.6>sd/SFX/doors/door_banging.ogg"
    pause 0.5
    with vpunch
    "I look up so fast I bang my head on the bottom of the desk and swear."
    hide aletta
    show aletta close work blush embarrassed
    menu:
        "Apologize":
            mike.say "I'm so sorry Aletta. I... It just caught me off guard."
            $ aletta.sub -= 1
        "Play dumb":
            mike.say "I-I... don't know what you mean."
    show aletta normal
    "Not being able to look her in the eyes I quickly hand the papers to her, which she takes with a smirk."
    show aletta talkative
    aletta.say "Let me know if you need anything, [hero.name]."
    show aletta normal
    "Now I definitely need to go to the bathroom, I think as I watch her walk away."
    scene bg publicbathroom with fade
    "Once in the stall I don't waste any time pulling my cock out of my pants."
    "I set a timer and tell myself I am going to make sure I cum in two minutes."
    "This has to be a quicky because I am not going to get caught with my pants down at work."
    "I wrap my hand around my cock and moan."
    "Jerking it to a steady tempo I can feel the pleasure flooding my senses and I am glad it is after hours or I know I would get caught."
    "I can't think about anything else right now."
    menu:
        "Think about Aletta's breasts":
            "I start to image her breasts free of her shirt and me cupping them in my hands before taking one of her nipples into my mouth."
            "I imagine the moans that would pour out of her and start jerking off faster."
            "If only I was actually holding them instead of my dick."
            "I keep thinking of Aletta's breasts in the most lewd ways possible and in no time I am cumming all over my hand and panting heavily."
            "I wash my hands and go back to work thinking about how I couldn't wait for a chance to spray her breasts with my cum."
        "Think about Aletta's pussy":
            "I start to image spreading Aletta's legs wide open and taking those lace panties off."
            "I think about plunging my fingers into her and making her scream."
            "I keep jerking off with my eyes closed pretending my hand is really Aletta's pussy and cum hard all over my hand."
            "After I clean up I go back to work with a satisfied smile, hoping I can get a chance at the real thing soon."
        "Think about an office intern":
            "I find myself thinking about an intern in the office instead of Aletta and before I know it my hard on is gone and I'm left disappointed."
            "I sigh and go wash my hands before going back to work."
    "At least my problem was gone."
    return

label aletta_event_03b:
    scene bg street
    "There I am, just strolling along, maybe gazing into a couple of shop windows on the way."
    $ renpy.sound.set_pan(1, 0, channel='sound')
    $ renpy.sound.set_pan(0.5, 6.0, channel='sound')
    play sound "<from 2 to 8>sd/SFX/vehicles/motorcycle_arrive.ogg" fadein 1.0
    $ renpy.sound.set_pan(0.5, 0, channel='sound')
    queue sound "<from 4 to 8>sd/SFX/vehicles/motorcycle_arrive.ogg" loop
    "When I suddenly hear the distinctive sound of a high-powered motorbike approaching at some speed."
    scene bg taxi at center, zoomAt(1.0, (640, 720)) with fade
    "I look up and around, not because I'm particularly impressed by that kind of thing, but more because it's the natural human reaction."
    "The bike is one of those Japanese types, the ones that look like they should be being ridden on some big racetrack in front of a load of cheering fans."
    show bg taxi at center, traveling(1.25, 0.5, (640, 880))
    "It's black and has streamlined bodywork that makes me wonder if even a radar could pick the thing up when it's speeding along."
    $ renpy.sound.set_pan(0.5, 0, channel='sound')
    $ renpy.sound.set_pan(0, 6.0, channel='sound')
    play sound "<from 4 to 10>sd/SFX/vehicles/motorcycle_arrive.ogg" fadein 0.2
    show aletta ride nobg noglasses at center, zoomAt(1.0, (840, 720)) with easeinright
    "But then I see the rider for the first time, and she looks like she could have been made to fit the bike, rather than the other way round."
    "Her black helmet and matching black leathers render her completely anonymous."
    "And yet the bodysuit is so fitted and tight that it leaves little to the imagination when it comes to her statuesque figure."
    "The female rider is tall, curvy and sits on the bike like some kind of warrior queen riding her steed into battle."
    "It's then that I realise I've been able to see so much only because she was in the act of slowing down and coming to a stop at the kerbside a couple of metres away."
    "I realise as well that I must have literally stopped in my tracks the very moment that I first laid eyes on her too."
    "As the rider uses her booted foot to put down the kickstand and turns the bike off, I try to look casual and turn away slowly, hoping that she hasn't seen me openly ogling her in the street."
    aletta.say "Hey, [hero.name]...where are you going in such a hurry?"
    "I recognise Aletta's voice instantly and turn back around, assuming that she must have walked up behind me in the street."
    "This could be awkward."
    "I'm not about to openly blank Aletta, but I don't want the biking amazon to see me either."
    scene bg taxi at center, zoomAt(1.0, (640, 720))
    show aletta_ride_bike at center, zoomAt(1.15, (740, 1000))
    show aletta suit helmet at center, zoomAt(1.25, (720, 900))
    show aletta_ride_bike_front at center, zoomAt(1.25, (840, 1000))
    with fade
    "Though when I do turn around, I'm amazed to see that they're actually one and the same person."
    "Oh yes, the leather goddess on the bike is none other than Aletta!"
    "The moment that I turn round to see this, the sun just so happens to be behind her."
    show aletta suit -helmet haircut noglasses at center, zoomAt(1.25, (720, 900)) with fade
    "And she just so happens to be in the act of taking off her helmet and shaking out her thick, brown hair."
    "Framed by the light of the sun, I swear that I see the whole thing in slow motion..."
    "...maybe even with classical music playing in the background too."
    mike.say "I..."
    show aletta talkative
    aletta.say "I said, where are you going, [hero.name]!"
    show aletta normal
    "I shake my head and try to pull myself back together."
    "It was bad enough just having to work with that body."
    "Now I have to deal with the memory of it in tight, form-fitting black leather too!"
    mike.say "Uh...sorry, Aletta - I guess I was just in a world of my own."
    show aletta happy
    "She smiles and shakes her head at my state of distraction."
    show aletta talkative
    aletta.say "Well, work has been pretty crazy this last week or so."
    aletta.say "It's at times like this that I always feel the need to bust this baby out and go for a long ride."
    aletta.say "Really helps to clear the cobwebs, I can tell you."
    show aletta normal
    mike.say "Huh...I didn't recognise you until you took your helmet off just now."
    "She gives me an odd, sideways look."
    "As if she's almost disappointed that I didn't recognise her simply from the shape of her body."
    "But if that is the case, she soon hides it."
    mike.say "I had no idea you were into motorbikes."
    mike.say "At least I've never seen you on one before...and you never talked about them at work either."
    show aletta happy
    "Aletta smiles at me, clearly pleased to have been able to surprise me and maintain an air of mystery at the same time."
    aletta.say "Oh yeah, [hero.name], I love to ride."
    show aletta talkative
    aletta.say "I just love the feeling of the bike, throbbing away beneath me..."
    aletta.say "Eating up the open road..."
    show aletta normal
    "Aletta grips the handlebars of the bike while she's telling me all of this, simulating the posture that she no doubt adopts when riding."
    "But all the time she does so, I'm wondering if she realises how she's straddling the bike in a REALLY suggestive manner."
    "She's almost throwing her head about as she acts out turning the thing, and I can't help thinking that she's actually imagining something else altogether being ridden rather passionately..."
    show aletta talkative
    aletta.say "Anyway...I can't sit around here all day chatting."
    aletta.say "I need to get away before I get a ticket."
    show aletta dreamy
    "She pauses in a thoughtful manner, so well rehearsed that I suspect it was far from spontaneous."
    aletta.say "Say...would you like a ride home?"

    show aletta talkative
    aletta.say "You'd be on your doorstep before you knew it."
    aletta.say "Especially with the way I ride!"
    show aletta normal
    "Right now, I can believe her!"
    menu:
        "No thanks":
            $ aletta.love -= 5
            mike.say "Ah...thanks for the offer, Aletta."
            mike.say "But I kinda walk home sometimes for the same reason you just said you ride that bike!"
            "I'm rubbing the back of my neck even as I say this, aware of just how lame it sounds."
            show aletta stuned
            "Aletta looks genuinely surprised at my refusing her offer."
            "And with the way she looks on that bike and in those leathers - who can blame her?"
            show aletta normal
            "But then she nods and shrugs her shoulders, seeming to accept my explanation."
            show aletta talkative
            aletta.say "Huh...I guess that makes sense, [hero.name]."
            aletta.say "We've all got our own ways of handling the daily grind."
            aletta.say "Far be it from me to screw up yours with mine!"
            show aletta sadsmile
            "I smile weakly, relieved to have been let off the hook."
            "But I can see a look of disappointment in Aletta's eyes, no matter how hard she tries to hide it."
            "And now I feel guilty for turning her down when she was clearly looking forward to showing off her bike and giving me a ride."
            $ renpy.sound.set_pan(0, 0, channel='sound')
            $ renpy.sound.set_pan(-1, 15.0, channel='sound')
            play sound motorcycle_leave
            scene bg taxi at center, zoomAt(1.25, (640, 880))
            show aletta ride nobg noglasses at center, zoomAt(1.0, (840, 720))
            with fade
            "We exchange a few more awkward pleasantries before she puts her helmet back on and gives me one final wave."
            hide aletta ride with easeoutleft
            "As she speeds off into the distance, I can't help wondering if I made the right decision."
            $ aletta.flags.cancel_sidestory = True
        "Sure":
            $ aletta.flags.sidestory = 1
            mike.say "Sure, Aletta - I'd love to hitch a ride home with you!"
            "My almost too eager response elicits a sly, knowing smile from Aletta."
            "I'm sure she's fully aware of just how much she's managed to reel me in with all of this biker chick stuff."

            "There might be a very real sexual undertone to what's going on here."
            "But Aletta offered me the chance to ride her bike - not to ride her."
            aletta.say "Just keep your feet up and make sure you hold onto me...tight."
            mike.say "Okay, okay...please don't go so fast that I fall off!"
            aletta.say "No promises, [hero.name] - so like I said, hold onto me real tight!"
            hide aletta
            show aletta ride mike noglasses
            with fade
            play sound motorcycle_ride loop
            "Aletta says all of this even as she's revving the bike and pulling away from the kerb."
            "I'm sure she's doing this on purpose, filling my head with the need to cling onto her and then adding acceleration as a motivator."
            "I've seen people doubled up on bikes many times in the past, and I try to copy their example."
            "But I still have to deal with the fact that I'm basically clinging onto Aletta for what feels like dear life."
            "Don't get me wrong - it's not that I don't WANT to cling onto Aletta under the right circumstances."
            "Though I fear that I'm going to end up paralysed and hanging off of her back like a priapic Yoda, still stuck in place even after the ride is over and done with."
            "I have my hands somewhere at the top of Aletta's thighs, trying to hold on well enough not to fall into traffic and yet not tight enough to make her think I'm already taking liberties."
            "She begins to speed up as soon as the first opportunity presents itself, weaving in and out of traffic with, what seems to me at least, increasing abandon."

            "So I have no choice other than to accept that my life is literally in her hands."
            "I try to distract myself by focussing on the sensations of being this close to Aletta."
            "I know I was going on about keeping this platonic and not getting sexual before now."
            "But I really need the distraction, and so let myself off the hook on this occasion."
            "What can I say about it that you've not already imagined?"
            "Aletta's body is pretty damn impressive through the clothes she wears to work."
            "But through supple leather, it's simply divine."
            "Her back and buttocks are quite possibly the most comfortable thing I've ever felt against my body."
            "Not to mention lower down..."
            show aletta ride mike lboob
            "Before I realise what I'm doing, my hands are no longer just holding onto Aletta's thighs for fear of falling off."
            "I can't help moving them up and down, almost massaging her through the leathers as I do so."
            "The need to keep up my grip means that I'm not being in the least bit gentle, but rather kneading handfuls of her beneath the leggings of her bodysuit."
            "Aletta must be well aware of what I'm doing, but she makes no attempt to slap away my hands or pull the bike over."
            "Instead, I swear she actually begins to rev the bike's engine almost in time to my squeezing of her breasts."
            "She also starts to go faster and ride with more abandon than before."
            "Though now, where before this would have intimidated me, I can't help finding that the arousing element of the ride turns the speed into something I actually enjoy."
            "The thought that Aletta is piling on the speed in direct response to my massaging her breasts is an incredible turn-on."
            "It feels almost as though she and the bike are linked, as though they're one entity."
            show aletta ride mike lboob pussy
            "The more I stir Aletta, the more the bike revs its engine and builds its speed."
            "My head is suddenly full of crazy thoughts, like making love to her while we're in motion, or mounting her as if she were a bike herself."
            "Suddenly I wonder if she can feel my dick through those leathers?"
            show aletta ride mike lboob pussy happy
            "I can't exactly help having a raging erection right now, can I?"
            "I'm genuinely worried about cumming in my pants if this keeps up as well!"
            "But then I can feel the speed of the bike lessening."
            "I shake off the almost trance-like state into which I'd fallen on the back of the bike and look around me."
            scene bg house at center, zoomAt(2.0, (650, 1250)), blur with fade
            show aletta ride mike noglasses nobg with easeinright
            "We're pulling up at the end of my street, just a couple of metres from my front door."
            stop sound
            scene bg house at center, zoomAt(2.0, (650, 1250)), blur
            show aletta_ride_bike at center, zoomAt(1.15, (740, 1000))
            show aletta suit helmet at center, zoomAt(1.25, (720, 900))
            show aletta_ride_bike_front at center, zoomAt(1.25, (840, 1000))
            with fade
            "I step off of the bike, almost shaking from the adrenaline still coursing through my veins."
            stop sound
            show aletta suit -helmet haircut noglasses at center, zoomAt(1.25, (720, 900)) with fade
            "Aletta removes her helmet."

            mike.say "Th..Thanks...Thanks for the lift...Aletta."
            show aletta happy
            "She smiles, and it's then that I know she can't have been ignorant of what even such a short ride with her has done to me."
            show aletta talkative
            aletta.say "No problem, [hero.name] - it was my pleasure."
            show aletta normal
            if game.week_day == 6:
                mike.say "Well, I guess I'll see you at work on Monday, yeah?"
            else:
                mike.say "Well, I guess I'll see you at work tomorrow, yeah?"
            "Aletta nods and gives me a little wave."
            show aletta talkative
            aletta.say "This was fun...we'll have to do it again some time, maybe?"
            "I nod, trying not to look either nervous or too turned on at the prospect."
            show aletta talkative
            aletta.say "Yeah, I'd really love to let you ride with me sometime soon..."
            hide aletta
            show aletta ride noglasses
            with fade
            "It's only when she's driven away from the kerb and I actually think about what she actually said, that I realise she never as much as mentioned the bike in relation to the proposed 'ride'."
            $ aletta.flags.sidestoryDelay = TemporaryFlag(True, 1)
            $ game.room = "house"
    $ game.pass_time(1)
    return

label aletta_event_04:
    scene bg alettaoffice
    if aletta.love.max < 80:
        $ aletta.love.max = 80
    show aletta annoyed
    with fade
    "I hear Aletta huff in aggravation and reach down to take her heels off all of a sudden."
    "We were working overtime again and she had seemed in a cranky mood the whole time."
    show aletta angry
    aletta.say "I hate that I have to wear these stupid high heels everyday."
    show aletta sadsmile
    mike.say "Why don't you just wear flats then?"
    show aletta angry
    aletta.say "Can't, part of the dress code for us bosses. Makes us look more professional or some bullshit like that. All it does is give me sore feet!"
    show aletta embarrassed
    "She starts rubbing her foot with the cutest pout I have ever seen her have."
    "I give her a smirk."
    mike.say "Here, let me help you with that."
    hide aletta
    show audrey_desk_bg_personal at flip
    show aletta vibrator nobg noshiori at center, zoomAt(1.5, (340, 1040))
    with fade
    "I reach down and lift her legs up and put her feet in my lap."
    show aletta vibrator surprised
    "She raises her eyebrow at me and moves so I can't see her underwear to my disappointment."
    aletta.say "What are you doing, [hero.name]?"
    show aletta vibrator embarrassed
    mike.say "Helping."
    "With that I start massaging her right foot and she makes a sound of pleasure."
    aletta.say "I might have to make you do this more often."
    "She leans into the back of the couch and puts her other foot in my lap close to my crotch, teasingly close."
    "I start to notice that every time I find a good spot while massaging her foot she gets a little bit closer to my crotch with her other one."
    "When I switch to her other foot she presses the first one completely against my groin and I have to hold back a moan."
    scene bg alettaoffice
    show aletta close normal
    with fade
    "She keeps pressing harder and rubbing with her foot as I massage all the while making complete eye contact with me."
    "For some reason I find this so hot."
    menu:
        "Talk dirty to her":
            mike.say "Well, well, aren't you a naughty girl?"
            show aletta blush
            "She gives me a smirk."
            show aletta flirt
            aletta.say "Me? The naughty one? You are the one getting hard by your boss rubbing you off. Looks like you are the bad one."
            show aletta normal
            mike.say "Me? You started it."
            show aletta flirt
            aletta.say "No, I believe you did when you tried to look up my skirt."
            show aletta normal
            "I can't really deny this."
            show aletta wink
            "She gives me a wink."
            $ aletta.sub += 1
        "Pretend not to notice what she is doing":
            "I try my hardest for as long as I can to pretend like I can't feel what she is doing."
            "But it just feels so good, even if it is just through my pants."
            "Finally a moan escapes me despite myself."

label aletta_event_04_sex:
    if 'aletta_event_04' in DONE:
        "Standing over Aletta as she flips through documents on the couch in her office, I have a clear view down her top. I immediately feel my cock begin to stiffen and I can almost taste her on my tongue again."
        mike.say "Aletta, you're looking a little burnt out, like you've been burning the candle at both ends. Maybe I can do something for you... or to you... to give you a break?"
        show aletta flirt
        aletta.say "Now, now, [hero.name], are you asking me to do naughty things in the office again?"
        show aletta normal
        "Her eyes trace down my body and rest on the noticeable outline of my dick through the fabric of my pants. A smirk crosses my face, as if daring her."
    hide aletta
    show aletta happy
    "Aletta laughs and gets up off the couch."
    show aletta normal blush
    "She gives me a sexy look as she lifts up her skirt just enough to hook her thumbs into her panties and pull them down her legs while making eye contact."
    "I can feel my heart pounding and my cock throbbing as she does so."
    "I can't take my eyes off of her."
    show aletta oral noman with fade
    "With a laugh she tosses them onto the floor and then places her hands on the table next to the couch."
    "Her pussy is just barely covered by the bottom of her skirt and she looks back at me with a lustful look as if temping me."
    "She spreads her legs more as if in invitation."
    menu:
        "Push her skirt up gently":
            "Getting up slowly I rub her bottom before taking the hem of her skirt in my hands and pushing it above her ass."
            "I look at what was before me and it is such a beautiful sight."
            "Her lips are already wet for me."
            if 'aletta_event_04' in DONE:
                $ aletta.sub -= 1
            else:
                $ aletta.sub -= 2
        "Be rough with her":
            "I yank her skirt up over her ass and give the right side a hard slap making her gasp."
            "She looks back at me in shock but pushes back against me as if she wants more."
            "So I give her another real quick slap before moving on to more fun."
            $ aletta.sub += 2
    show aletta oral manb
    "I take my fingers and run them along her lips slowly and teasingly until I suddenly thrust them into her center and she lets out a moan, pushing back to further fill herself with them."
    "Only a few minutes of this and her juices are already all over my fingers and threaten to run down her legs."
    "Needing more leverage, she drops down to her knees on the table."
    "It is the sexiest sight I have ever seen."
    "I follow suit, going down to my knees on the floor so my face is level with her pussy."
    "I love the smell of her and have a feeling I am going to enjoy the taste of her as well."
    show aletta oral mana tongue
    "I plunge my tongue inside and she lets out a startled but pleasured yell."
    aletta.say "Oh [hero.name]..."
    "Her moan is so sexy I decide to reward her by rubbing her clit in slow circles and continuing to lick her out at the same time."
    "I hear her start to pant heavily."
    aletta.say "[hero.name]... [hero.name]... I'm... I'm going to..."
    mike.say "It's okay Aletta, just let go and enjoy yourself."
    "I quickly replace my tongue with my fingers to help her along and she lets out a long drawn out moan as she squirts on my face."
    menu:
        "Try to catch it in your mouth":
            hide aletta
            show aletta oral mana cum
            "Knowing she was about to do so I had opened my mouth trying to catch as much as I could, licking my lips when she was done."
            mike.say "Mmm, Aletta you taste so good."
            if 'aletta_event_04' in DONE:
                $ aletta.sub -= 1
            else:
                $ aletta.sub -= 2
        "Quickly shut your mouth":
            hide aletta
            show aletta oral manb cum
            "Knowing she was about to do that, I quickly try to shut my mouth but didn't turn my head quick enough."
            "I make a face but try not to let her see it."
    hide aletta
    show aletta oral mana arm
    "I start to suck on her clit while still thrusting my fingers back and forth in her and she moves to give me more access as more needed, breathy, moans come out of her mouth."
    show aletta oral mana arm tongue
    "I lick her from her clit to her taint and back again as she tries to push back on my face."
    "She squirts again and seems to be losing control of herself."
    "I massage the walls of her vagina and nurse her clit at the same time and don't let up as I hear her beside herself in pleasure."
    "She tries to say my name but can hardly speak."
    show aletta oral mana arm tongue orgasm
    aletta.say "[hero.name]!"
    "I suddenly feel a shudder go through her and she lays her head down on her arms as she rides out the rest of her orgasm."
    "Standing up I use a tissue to wipe off my face before stealing her panties and pocketing them."
    "I didn't think she was going to miss them."
    if 'aletta_event_04' in DONE:
        $ aletta.sub -= 1
    hide aletta
    return

label aletta_event_04b:
    "After a week full of work and household politics, my weekends are usually when I officially turn off my brain and try to recuperate."
    "If I'm lucky, I can sometimes even manage to get away with not setting foot out of bed until some time in the afternoon."
    "To this end, I always leave my phone set to vibrate and on top of something soft, just to make sure I'm not disturbed."
    "The only possibility is opening my eyes for a moment and actually seeing that there's someone calling I can't resist talking to."
    $ renpy.sound.set_pan(0.75, 0, channel='sound')
    play sound cell_vibrate loop
    "Which is what's happening right now."
    "I glance blearily at the phone, trying to make out who's calling at this time."
    stop sound
    "'Aletta' - almost as soon as I read the name, I'm already scrambling for the phone."
    $ renpy.sound.set_pan(0, 0, channel='sound')
    play sound body_fall
    pause 0.3
    with vpunch
    "I fall out of the bed grabbing for it, and accept the call whilst laid on the floor in a heap of bedclothes."
    "Call me desperate, if you like."
    "But I'm not swimming in offers to the point where I can ignore a call from a girl the likes of Aletta."
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Aletta")
    if not result:
        $ hero.cancel_event()
        $ aletta.love -= 5
        return
    mike.say "Hey there...Aletta - what's up?"
    aletta.say "Hey, [hero.name] - I thought you weren't going to pick up for a minute there!"
    mike.say "I was struggling to get to my phone."
    mike.say "You know how it is on a weekend, right?"
    aletta.say "Oh, tell me about it!"
    aletta.say "I've been up since before six so that I could get to the gym and then hit the classes that I take on morning."
    aletta.say "The weekend is supposed to be time to relax, but I always seem to end up doing more than I would have at work!"
    "Oh great - the girl can even make me feel inadequate over the phone, and without try very hard too!"
    aletta.say "That's what I was calling about, actually."
    mike.say "What - you want me to work this weekend?"
    mike.say "It's kinda short notice..."
    aletta.say "No, no - nothing like that!"
    aletta.say "I meant that I managed to get some free time this afternoon."
    aletta.say "And I wondered if you wanted to come do something with me?"
    aletta.say "Something fun?"
    "Already my mind is conjuring all manner of 'fun' things that could be done with Aletta's help..."
    mike.say "What did you have in mind?"
    aletta.say "Well, I like to get some practice in down at the firing range every few weeks."
    aletta.say "I thought it'd be a laugh if we went along and squeezed off a few rounds together."
    aletta.say "What do you think?"
    menu:
        "Refuse":
            "The firing range?"
            "What does she think I am - some kind of gun-toting loon?"
            "Come to think of it, who invites someone on a date to go shoot off a shit-load of guns?"
            "Is she a gun-toting loon herself?"
            mike.say "Ahh...that sounds like a great idea, Aletta."
            mike.say "But I'm gonna have to take a rain-check...sorry."
            aletta.say "Oh...okay, I guess."
            aletta.say "Do you mind if I ask why?"
            "Here we go - better think up a good excuse, and fast."
            mike.say "Well...you know how we were talking about how much work we had on this week in the office?"
            aletta.say "Yeah...sort of..."
            mike.say "I brought a pile home with me to get through before Monday morning, and I just remembered about it."
            "There's a pause before she replies."
            aletta.say "You brought that much work home and still managed to forget about it all?"
            mike.say "Weird, I know!"
            mike.say "But I think it must have been the thought of getting to sack it all off and spend the rest of the day with you."
            mike.say "That probably would have been enough to make me forget about almost anything else!"
            "I wait for a moment, hoping that she buys it."
            "There's a muffled gasp and then a pretty genuine sounding giggle from the other end of the line."
            aletta.say "Well, if I have to be stood up, then at least it's nice to get a compliment like that at the same time."
            aletta.say "I'll call you some other time - don't work too hard now!"
            mike.say "Looking forward to it already!"
            "I think I might actually have pulled it off!"
            $ aletta.flags.cancel_sidestory = True
            return
        "Accept":
            $ aletta.flags.sidestory = 2
            mike.say "The firing range...sure, why not."
            aletta.say "Great - I'll swing by on the bike and pick you up in about an hour, okay?"
            mike.say "I'll be ready."
            "I put down the phone and hurry to get showered and ready for Aletta's arrival."
            scene bg bathroom at blur(8) with timelaps
            pause 2.0
            scene bg black with dissolve
            pause 1.0
            $ game.pass_time(1)
            scene bg house with wiperight
            pause 1.0
            $ renpy.sound.set_pan(1, 0, channel='sound')
            $ renpy.sound.set_pan(0, 3.0, channel='sound')
            play sound "<from 2 to 10>sd/SFX/vehicles/motorcycle_arrive.ogg"
            scene bg house at center, zoomAt(2.0, (650, 1250)), blur with fade
            show aletta ride noglasses nobg with easeinright
            "By the time she roars to a halt outside the house, I'm already standing by the kerb, waiting for her."
            "No one could know that I was slobbing in bed until so recently."
            scene bg house at center, zoomAt(2.15, (650, 1300)), blur
            show aletta_ride_bike at center, zoomAt(1.15, (740, 1000))
            show aletta suit helmet at center, zoomAt(1.25, (720, 900))
            show aletta_ride_bike_front at center, zoomAt(1.25, (840, 1000))
            with fade
            "Aletta flips up the visor of her helmet and tosses me the spare."
            stop sound fadeout 1.0
            aletta.say "Jump on - you know the drill, right?"
            $ renpy.sound.set_pan(0, 0, channel='sound')
            play sound motorcycle_ride
            "I nod and do as I'm told, trying not to make it so obvious that I'm eager as hell to press myself tightly against Aletta on the bike."
            hide aletta
            show aletta ride mike
            "The ride there is swift, thrilling and over way too soon."
            "We dismount and Aletta leads the way inside."
            stop sound fadeout 1.0
            scene bg shootingrange
            show aletta suit at center, zoomAt(1.25, (640, 880))
            with fade
            "The staff on duty seem to be pretty familiar with her, offering greetings and even a few little jokes."
            "But I don't even have time to get jealous, as she ushers me into the range and we prepare to shoot."
            "The place is pretty much like what you see on any cop show paper targets on the opposite wall in a long room, with booths for the shooters to stand in."
            "Ear and eye protectors are provided, and I hear Aletta say something about the handguns we're going to be shooting that gets lost in the constant din of the place."
            hide aletta
            show aletta shooting
            with fade
            "She goes first, and even before she's let off a single shot, I can tell from her stance that she's pretty damn serious about this thing."
            show aletta shooting fire
            play sound gun
            pause 0.2
            show aletta shooting -fire
            "I watch as Aletta puts one bullet after another into her target."
            show aletta shooting fire
            play sound gun
            pause 0.2
            show aletta shooting -fire
            "Sure, not all of them are kill-shots, but she's accurate enough to make the prospect of her shooting at you a pretty scary one."
            "Still wearing the ear protectors, she waves for me to take my shots."
            show aletta shooting mike
            "First I take a deep breath, and then step up to shoot."
            if hero.has_skill("shooting"):
                "I don't know if my stance is as good as Aletta's, but it's always served me well enough."
                show aletta shooting mike fire
                play sound gun
                pause 0.2
                show aletta shooting -fire
                "I shoot until the magazine is empty."
                "Not a crazy flurry of shots or a torturous series of quivering ones."
                "All of them are, more or less, on target."
                "Looking at it again, I think I even did a little better than Aletta herself."
                $ aletta.love += 5
                $ aletta.sub += 5
                scene bg shootingrange
                show aletta suit flirt at center, zoomAt(1.25, (640, 880))
                with fade
                "She certainly looks impressed enough with my performance."
                "What can I say?"
                "Just because I don't own a mountain of guns or want to start a militia in the backyard, that doesn't mean I can't be a good shot."
                "Not all people who can shoot are fanatics or spend the whole time bragging about it either."
                scene bg street
                show aletta suit at center, zoomAt(1.25, (640, 880))
                with fade
                "Outside of the range, I try to look surprised at Aletta's evidently growing admiration for my marksmanship."
                show aletta talkative
                aletta.say "Someone's certainly a dark horse!"
                show aletta normal
                mike.say "I'd prefer to call it not blowing my own trumpet."
                show aletta talkative
                aletta.say "It's nice to know that you actually have a trumpet!"
                show aletta normal
                mike.say "Ah, well...what kind of a jerk would I have been if I bragged about it the moment you said you wanted to go shooting with me?"
                show aletta dreamy
                "Aletta goes quiet for a moment, just nodding in silence, as if she were lost in thought."
                "From the reaction my being humble stirred in her, I begin to wonder if she's mentally comparing me with Dwayne."
                "Now there is a guy that never had a single problem shouting his talents from the rooftops."
                mike.say "Are you okay, Aletta?"
                show aletta talkative
                aletta.say "Oh, yeah...I'm fine."
                aletta.say "I was just thinking that it might be fun to find out what else you've been hiding from me!"
                show aletta normal
                "I laugh at the comment, like I'm supposed to."
                "But I'm already thinking that it might be fun to let her."
            else:
                "It's all I can do to keep the pistol from visibly shaking in my hand as I try to aim it at the target."
                show aletta shooting mike fire
                play sound gun
                pause 0.2
                show aletta shooting -fire
                "All of the advice Aletta tried to give me before we started went straight over my head."
                show aletta shooting mike fire
                play sound gun
                pause 0.2
                show aletta shooting -fire
                "Just like most of my shots do to the human shape described on the target I'm supposed to be aiming for."
                show aletta shooting mike fire
                play sound gun
                pause 0.2
                show aletta shooting -fire
                "I lose all track of the number of bullets that there should be left in the magazine as I reel of one lousy shot after another."
                "Soon the bullets run out, and I realise that I'm just pulling the trigger to no effect."
                scene bg shootingrange
                show aletta suit normal at center, zoomAt(1.25, (640, 880))
                with fade
                "Sheepishly, I put the gun down and turn to face Aletta."
                "No one else is shooting now, so it's safe for us both to remove our ear protectors."
                $ aletta.sub -= 20
                mike.say "Sorry...I guess...I guess I just embarrassed you pretty badly, huh?"
                show aletta talkative
                aletta.say "Don't be silly - there's no shame in being a bad shot, just in not wanting to get better."
                aletta.say "[hero.name], why didn't you just say if you weren't into this kind of thing?"
                show aletta normal
                mike.say "It's that obvious?"
                show aletta talkative
                aletta.say "Well, let's just say that if the aim were to keep from hitting the target at all - you'd be a natural."
                show aletta normal
                mike.say "Like I already said...I'm sorry."
                mike.say "I just thought that if I said I wasn't into guns, then you'd think less of me."
                mike.say "It was a chance to spend some more time with you, too..."
                show aletta happy
                "Aletta smiles at the admission, and I begin to see that I was wrong to imagine her looking down on me for those reasons."
                "I think she's genuinely touched at the idea of me wanting to see her that much."
                "And maybe also finding my honesty more than a little endearing too."
                show aletta talkative
                aletta.say "I could always teach you...if you'd like?"
                show aletta normal
                "It doesn't take much for me to agree, and while she gives me some more verbal pointers, she can't talk me through the actual shooting."
                "Of course, this means that she has to get in real close to ensure the lessons sink in when I try to shoot again."
                "Some guys might feel a little emasculated to have a woman bracing them and showing them how to fire a gun like this."
                "But I'm very happy to feel Aletta pressed against me, arms almost wrapped around me and the warmth of her breath against my cheek."
                "It gets even better when I actually squeeze the trigger and the force of the shot travels through my body and into hers."
                "By the time we've polished off an entire clip, she's practically wrapped herself around me."
                "I choose to read a lot into the fact that Aletta is not quick to release that hold she has on me."
                "And the way she lingers close afterwards is very pleasant as well."
                "As we leave, I can't help thinking how weird it is that I seem to have made such an impression on Aletta by kind of being weak where she's strong."
            $ aletta.flags.sidestoryDelay = TemporaryFlag(True, 1)
    $ game.pass_time(6)
    return

label aletta_event_05:
    if hero.flags.isceo:
        scene bg ceo
    else:
        scene bg personal
    if aletta.love.max < 100:
        $ aletta.love.max = 100
    play sound door_knock
    "I'm halfway to falling asleep in the middle of my current project when there's a knock at my office door."
    "I make sure I'm upright and look awake and focused before I call out."
    mike.say "Yeah? Come in."
    show aletta work at center, zoomAt(1.0, (540, 720)) with easeinleft
    "The door swings open and Aletta steps inside."
    "She doesn't immediately say anything, like 'hey, I was just looking for the stapler,' so my first thought is that I'm in some kind of trouble."
    show aletta work at center, zoomAt(1.0, (840, 720))
    show dwayne at center, zoomAt(1.1, (340, 780))
    with easeinleft
    "But she steps aside, and another someone steps into the doorway after her."
    "He's big and surprisingly burly in his office formal wear, his muscles visible beneath the fabric of his shirt."
    "What is this, Aletta's newest hire?"
    "He looks like an ex-underwear-model thinly veiled as an employee."
    "I bet she's gonna keep him under her desk."
    show aletta talkative
    aletta.say "I wanted to introduce you, since I don't think you've ever met."
    show aletta normal
    "Aletta holds a hand up to the guy, who seems to be waiting for something."
    show dwayne at center, traveling(1.25, 0.3, (340, 880))
    "I realize immediately that he's expecting me to get to my feet and shake his hand."
    menu:
        "Get up":
            $ game.set_flag("worksatisfaction", 10, mod="+")
            if hero.has_skill("work"):
                $ game.set_flag("worksatisfaction", 10, mod="+")
            "I guess I'll give the guy some dignity, even if he might be a nobody."
            "I'm not stupid enough to potentially piss off someone important, anyway."
            "I roll back my seat from my desk and get to my feet, turning to offer my hand to the dude."
            "His hand seems to be twice the size of mine when he reaches out and gives it a firm shake."
            show aletta talkative
            aletta.say "This is Mr. --"
            show aletta normal
            show dwayne shout
            dwayne.say "Please."
            show dwayne normal
            "He interrupts her, giving me a formal but pleasant smile as he looks down at me with my hand still clasped in his."
            show dwayne happy
            dwayne.say "Dwayne's fine."
            show dwayne smile
            "Ah. He's the kind of 'I'm a cool coworker' guy."
            "I don't mind."
            "They're definitely better than the uptight stiffs who expect you to address them like royalty."
            mike.say "Nice to meet you."
            show aletta talkative
            aletta.say "Dwayne, he's been working with us for a while now. He's..."
            show aletta normal
            "She stops to think for a second, staring at me, like she's evaluating what she wants to say."
            if game.flags.worksatisfaction > 50 or game.flags.promoted >= 10:
                $ aletta.love += 10
                show aletta talkative
                aletta.say "... efficient, and talented. I'm happy to have him as an employee."
                show aletta normal
                "Aw, Aletta, you shouldn't have. I could almost blush."
                show dwayne happy
                dwayne.say "A driving force in the company's success, huh?"
                show dwayne smile at center, traveling(1.1, 0.3, (340, 780))
                "Dwayne gives my hand one last firm shake before letting it go and stepping back."
                show dwayne happy
                dwayne.say "Very nice to meet you."
                show dwayne smile
                mike.say "Likewise."
            else:
                show aletta talkative
                aletta.say "...he's been getting the job done."
                show aletta normal
                show dwayne smile at center, traveling(1.1, 0.3, (340, 780))
                "Dwayne chuckled, giving my hand one last small shake before letting it go and stepping back."
                show dwayne happy
                dwayne.say "A workhorse, huh? Always good to have them on board."
                show dwayne normal
                mike.say "Good to be here."
                "Having a job is kind of a necessity, anyway."
            "I get the feeling this isn't her new hire."
            show aletta talkative
            aletta.say "You might not recognize him by first name. Dwayne is the CEO of the company."
            show aletta normal
            "Recognition floods me all at once, and suddenly I'm looking at this mammoth of a man with new eyes."
            "That's right, his name was Dwayne, wasn't it?"
            "It's hard to remember, since the guy's never really around in the office."
            show aletta talkative
            aletta.say "Well, we've got more stops to make, so."
            show aletta normal
            mike.say "Ah, yeah. I'll get back to work."
            show dwayne happy
            dwayne.say "Have a good one."
            show dwayne normal
            mike.say "You, too."
            hide dwayne
            hide aletta
            with easeoutleft
            "It's a little jarring, still, after the two of them leave."
            "I wish she would have warned me he was coming around today, so I could have dressed a little nicer or something."
            "Oh well. I think I made a good enough impression."
        "Stay seated":
            $ aletta.sub += 10
            "I lean myself back a little bit in my seat, making myself comfortable."
            "I was almost dozing off a second ago; I'm not gonna expend any precious energy standing up for formalities."
            "I'm sure he doesn't actually care."
            show aletta upset
            "Aletta seems like she's shooting me daggers from my peripheral, but I don't bother to look over to catch them."
            "I keep my eyes on the new guy."
            "She seems a little flustered by my choice."
            "I never really thought of first impressions as being as important as people make them out to be."
            "I need time to grow on people. Formality is fake, anyway."
            show aletta embarrassed
            aletta.say "Well..."
            "She gestures towards me, and the guy nods his head."
            aletta.say "He's..."
            "She pauses, maybe trying to think of some way to talk me up, even if she thinks I'm being a bit rude."
            if game.flags.worksatisfaction > 50 or game.flags.promoted >= 10:
                $ aletta.love += 10
                show aletta talkative
                aletta.say "...surprisingly competent."
                show aletta normal
                "She continued though it seemed to pain her a little bit."
                show aletta talkative
                aletta.say "Usually not like this."
                show aletta sadsmile
                "Aw, Aletta, you shouldn't have. I could almost blush."
                show dwayne happy
                "Shady guy" "A driving force in the company's success, huh?"
                show dwayne smile
                "He seems less bothered by my snub than Aletta is."
            else:
                show aletta talkative
                aletta.say "...he's been getting the job done."
                show aletta sadsmile
                "I guess that's all she can manage, right now."
                show dwayne happy
                "Shady guy" "A workhorse, huh? Always good to have them on board."
                show dwayne normal
            "I'm starting to get the impression that this guy's not just her new hire."
            show aletta normal
            "Aletta clears her throat and glances back to me."
            show aletta talkative
            aletta.say "This is Mr.--"
            show aletta normal
            "She still sounds a bit strained while she addresses me."
            show dwayne shout
            dwayne.say "Please."
            show dwayne normal
            "He interrupts her, giving me a tight and formal smile as he looks down at me."
            show dwayne happy
            dwayne.say "Dwayne's fine."
            show dwayne normal
            show aletta talkative
            aletta.say "...He's the CEO of our company."
            show aletta normal
            "Oh, shit."
            "Well, it's too late to jump to my feet and try to grovel."
            "I hope that it exudes confidence and some kind of alpha-demeanor for me to remain seated, but at this point I don't get the impression that Dwayne's the kind of man to be impressed by feigned dominance."
            "He could ruin my life in a second. I gulp hard, but try to keep my appearance under control."
            show dwayne happy
            dwayne.say "Well, it's been nice to meet you."
            show dwayne normal
            show aletta upset
            "Aletta shoots me a glance that says she doesn't feel the same."
            mike.say "Uh, yeah. Likewise."
            hide dwayne
            hide aletta
            with easeoutleft
            "I feel a little off even after they leave, internally cringing, just a little bit."
            "She could have at least warned me, or something."
            "You can't just barge in with higher-ups and expect me and my office to be spotless and perfectly deferential behavior off the bat."
            "Oh well. Hopefully I gave a good enough impression to not lose my job."
    return

label aletta_event_05b:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Aletta")
    if not result:
        $ hero.cancel_event()
        $ aletta.love -= 5
        return
    if aletta.love.max < 100:
        $ aletta.love.max = 100
    "I was a little curious when Aletta called me up, pretty much out of the blue and said she wanted to come over and see me."
    "But we'd had what I thought was a pretty successful date (if you could call it that) at the shooting range."
    "And after that, I was keen to see more of her as soon as the chance arose - so I instantly said yes."
    "It was only a few seconds before she hung up that she dropped into the conversation the fact that she also wanted to 'talk to me' about something."
    "Now to a girl, those are nothing more than words making up a casual statement."
    "But to a guy, they're almost always enough to send chills up your spine."
    "What in the hell could she possibly want to talk about?"
    "We're not at the stage in our relationship that we need to be talking about things yet, surely?"
    "We've only been out on sort-of dates a couple of times - so is it even properly a relationship yet?"
    "The only logical conclusion is that she's got cold feet and wants to call it all off."
    "And she's coming round to tell me how 'it's not you, it's me'!"
    "But then I actually manage to sit down and tell myself I'm being stupid, jumping to wild conclusions."
    "Best to just wait for her to turn up and hear what she has to say."
    play sound door_bell
    "When the doorbell rings, I try not to leap up and run to answer it."
    "Instead I walk as calmly as I can manage into the hallway and open it with what I hope is a smile on my face."
    scene bg house
    show aletta suit haircut talkative at center, zoomAt(1.0, (640, 720))
    with wiperight
    aletta.say "Hello, [hero.name], I came over as soon as I could."
    show aletta normal
    mike.say "Hey, Aletta..."
    "No sign of anything on her face to say she's not telling the truth."
    show aletta talkative
    aletta.say "Well..."
    show aletta normal
    mike.say "Well what?"
    show aletta talkative
    aletta.say "I was presuming that you were actually going to invite me in?"
    show aletta normal
    mike.say "Oh, yeah...of course...come on in!"
    show aletta at center, traveling(1.25, 0.3, (540, 880))
    "I step aside to let her into the hallway, only noticing at that moment that she's carrying what looks like an overnight bag in one hand."
    show bg livingroom
    "What's that about - is she planning on asking to stay over?"
    show aletta at center, traveling(1.5, 0.3, (640, 1040))
    "I close the door, but before I can ask about the bag, Aletta steps forward and wraps her arms around me tightly."
    hide aletta
    show aletta kiss suit haircut
    with fade
    $ aletta.flags.kiss += 1
    "She kisses me without asking, passionately and quickly adding her tongue as soon as I return the gesture."
    "Well, that certainly took my mind off of the idea of her coming over just to dump me!"
    hide aletta
    show aletta suit haircut happy at center, zoomAt(1.25, (640, 880))
    with fade
    "When the kiss is over, she smiles slyly at me."
    show aletta talkative
    aletta.say "You remember when we went to the shooting range?"
    show aletta normal
    "I nod slowly, wondering where this is going."
    if hero.has_skill("shooting"):
        show aletta talkative
        aletta.say "And how you kept it a secret that you're actually a pretty good shot?"
        show aletta normal
        "'Pretty good shot' - I seem to remember beating Aletta's score that day!"
    else:
        show aletta talkative
        aletta.say "And maybe needing more practice."
        show aletta normal
    "I nod again."
    show aletta talkative
    aletta.say "Well - I wondered if you fancied a rematch?"
    show aletta normal
    mike.say "You mean you want to go back to the shooting range again?"
    "Aletta shakes her head and holds up the bag she's brought with her."
    show aletta talkative
    aletta.say "No, [hero.name] - I brought my gun with me."
    aletta.say "You have woods out back, right?"
    aletta.say "I thought we could go out there and maybe shoot some cans."
    aletta.say "Loser buys dinner - what do you think?"
    show aletta normal
    "It's not what I was expecting, but it's a far better prospect than what I'd imagined."
    mike.say "Sure - why not?"
    scene bg pool with fade
    "We walk out of the back door, past the pool (which I note Aletta seems surprised by), and out of the back gate."
    scene bg forest with fade
    "The woods start a couple of feet from the property line."
    "And I figure that if we go far enough into them, the combination of distance and a major road on the other side should be enough to keep the sounds from alarming the neighbours."
    "We chat as we walk, not really talking about much that would interest anyone else."
    "The only stops we make are to collect maybe half-a-dozen empty cans along the way."
    "We stop when we come across a wall we can use, made out of brick and a little over waist height."
    show aletta suit with dissolve
    "I have no idea what it once was or what it was supposed to mark out, but it's just about perfect."
    mike.say "Seeing as how this was your idea, how about you set up the cans how you'd like them?"
    show aletta happy
    "Aletta nods and smiles, accepting the cans."
    show aletta normal
    "She arranges them in two groups of three, each group three feet apart and each individual can maybe one foot from the next."
    "That done, she walks over to her bag and unzips it."
    "Aletta reaches inside and pulls out a handgun, matte black and impressive enough to appear in a slick action movie."
    show aletta happy
    "She smiles at the look on my face, clearly thinking that I'm impressed."
    "But right now, intimidated would probably be closer to the actual truth."
    show aletta normal
    "She proceeds to drop out and catch the ammo magazine, slide the chamber back and basically do all that neat stuff people do in films to show they're a wizard with a gun."
    show aletta talkative
    aletta.say "This is a Gnock 18 semi-automatic pistol and it fires a nine millimetre parabellum round."
    aletta.say "So I don't need to tell you to treat it with respect, right?"
    show aletta normal
    "Everything she just said basically boiled down to 'this is a big, scary gun that fires bullets that'll kill you, stone dead'."
    "But I nod all the same, still well aware of the dangers posed by a gun."
    show aletta talkative
    aletta.say "You ready?"
    show aletta normal
    mike.say "As I'll ever be, I guess!"
    "Aletta turns the gun around in her hand so that she's holding it by the barrel and I'm taking it by the grip."
    "Shit, this girl really takes her firearms safety seriously!"
    hide aletta
    show aletta shooting mike forest
    with fade
    "Once I have the gun in my hands, the weight of it somehow makes this whole thing seem suddenly real."
    "We're not joking around and talking about this any more - we're actually doing it!"
    "Was I right about the distance and the sound of the road covering the shots?"
    "What if someone comes walking through the woods and gets shot by a stray bullet?"
    "Fuck - what if I shoot myself in the goddamn foot?"
    "Breathe, just breathe and keep calm!"
    "I've shot a gun before, and this is no different to those times."
    aletta.say "You okay?"
    mike.say "Sure, sure...I'm fine."
    mike.say "It's just...new gun, you know?"
    aletta.say "Okay...but there was just one more thing."
    aletta.say "I'd thought of it as a forfeit, to make it a little harder for you to shoot straight."
    aletta.say "But if you're nervous, then maybe it'll actually help to calm you..."
    "With that enigmatic last line, she kneels down slowly in front of me."
    "And then she starts to unzip my pants, while she smiles up at me slyly."
    "Bloody hell - she's really going to give me a blowjob while I'm supposed to be shooting this thing!"

label aletta_event_05b_sex:
    if "aletta_event_05b" in DONE:
        show aletta sport
        aletta.say "Wasn't expecting company out here... but since you're here and I happen to have my gear with me, let's have another rematch. Same... 'rules' as last time?"
        show aletta naked
        "I blush slightly as Aletta strips out of her hiking clothes, never breaking eye contact with me."
        aletta.say "Oh, I didn't think you'd mind if I slipped into something a bit more appropriate for shooting..."
        show aletta suit
        if not hero.has_skill("shooting") or not hero.fitness >= 50:
            aletta.say "If I remember correctly, you need a bit of practice under duress..."
        else:
            aletta.say "Go on, [hero.name], you know what to do..."
        "She licks her lips while she hands me her gun before kneeling in front of me."
        "The sound of my zipper deafening against the silence of the forest."
    if not hero.has_skill("shooting") or not hero.fitness >= 50:
        "Aletta doesn't find me very aroused when she first pulls my dick out."
        "But under the circumstances, can you blame me?!?"
        "Not that it discourages her to any great degree though."
        show aletta shooting mike forest bj lick
        "I try to tear my eyes away as she begins to stroke the shaft of my dick with her fingers, occasionally bringing it to her lips and kissing the tip."
        "I look down the barrel of the gun, amazed to see just how much it's shaking."
        "The one thing that I know for sure is that I'm not exactly shrinking from the situation - if you understand what I mean?"
        "Maybe it's the danger of doing something this risque and dangerous out in the open like this."
        "Maybe I'm having a perverse burst of excitement from handling a powerful gun in such a reckless manner."
        "Or just maybe Aletta's that damn good with her fingers and lips that I can't help stirring at her attentions."
        "She certainly looks good as I risk a glance down at her."
        "I'm semi-erect by now, and well on my way to being fully standing to attention."
        show aletta shooting mike forest bj suck
        "Aletta looks up at me as she slips her lips around my cock."
        "Her big, blue eyes are full of mischief and her lipstick glistens in the afternoon sunlight."
        with screenshot
        show aletta shooting mike forest bj suck fire
        play sound gun
        pause 0.2
        show aletta shooting -fire
        "Without thinking, I squeeze the trigger, sending a shot flying crazily wide of the mark."
        "While I jerk at the deafening sound, somehow Aletta manages to remain still."
        hide aletta
        show aletta shooting mike forest bj suck
        "Even the exaggerated motion of my dick she takes completely in her stride, widening her eyes in mock surprise as I push deeper into her open mouth."
        "From there, it's almost impossible for me to pay more attention to shooting straight than to what Aletta's doing to me."
        "Call me a pussy for not being able to concentrate on the gun if you like."
        "But I'm not ashamed to say that I was far more interested in the sensational things that I discovered Aletta could pull off with her tongue that afternoon."
        "I can't recall just how many bullets there were in the magazine."
        with screenshot
        show aletta shooting mike forest bj suck fire
        play sound gun
        pause 0.2
        show aletta shooting -fire
        "Only that I shot most of them randomly into the woods, completely missing the targets."
        "I might have grazed one of Aletta's cans, and I know I fired at least one shot almost straight up into the air."
        "Part of me expected that one to hit a passing bird, just to add to the insanity of what was happening to me right there and then."
        hide aletta
        show aletta shooting mike forest bj suck mouth
        "About the only thing that I did manage to shoot on target, was when I finally came into Aletta's mouth."
        "She smiled as she released me and swallowed without pause of hesitation, knowing full well what she had managed to make me do."
    else:
        "It's weird, but there's just something empowering about the thought of Aletta giving me oral while I'm shooting a big, macho handgun."
        "Maybe it's tapping into the primitive parts of my brain, but I suddenly feel incredibly aroused by what's going on."
        "The biggest side effect of this is that, by the time Aletta gets my dick out of my pants, I'm already almost fully erect."
        "She smiles at the sight of it, chuckling to herself."
        show aletta shooting mike forest bj lick
        "It doesn't take long for Aletta to have me standing fully to attention, as she strokes and caresses the shaft."
        "I take aim for the first can almost the same moment that she begins to lick tentatively at the tip of my dick."
        show aletta shooting mike forest bj suck
        "Her lips close around the head as I squeeze the trigger."
        show aletta shooting mike forest bj suck fire
        play sound gun
        pause 0.2
        show aletta shooting -fire
        "In the confusion of the resulting crack of gunfire, Aletta takes me deeper into her mouth."
        "Bullseye - the first can is nowhere to be seen, blown clean off of the wall."
        hide aletta
        show aletta shooting mike forest bj suck
        "Aletta's pace quickens now, and I can feel the sensation of her full lips travelling up and down, her tongue working away at me."
        show aletta shooting mike forest bj suck fire
        play sound gun
        pause 0.2
        show aletta shooting -fire
        "The second shot comes as if carried on this feeling, as easy as me simply walking up and pushing it over with a finger."
        hide aletta
        show aletta shooting mike forest bj suck
        "Two cans down, one to go."
        "Aletta's working on me like a machine by now, her head bobbing back and forth."
        "I look down at her for a moment, and I almost forget about taking my last shot."
        "She has her eyes closed and an almost peaceful look in them."
        "The sunlight is coming down, dappled by the leaves and branches overhead."
        "She looks amazing, mottled in the shadows and shade."
        "I feel like I could lose myself, right here and now, just looking at her."
        "But I resolve to take a shot at my last can before she makes me cum."
        "I have the shot all lined up just as I realise how close she's actually brought me."
        "Trying to breathe evenly, I begin to squeeze the trigger for one last shot."
        hide aletta
        with screenshot
        show aletta shooting mike forest bj lick fire
        play sound gun
        pause 0.2
        show aletta shooting -fire
        "And almost at the same moment that the gun fires, Aletta sends me over the edge."
        show aletta shooting mike forest bj lick fire facial
        "As I cum, the gun is thrown around in my hand, and it's all I can do to keep from firing off the remaining bullets in the clip."
        "Aletta makes sure that she finishes the job neatly, licking me clean afterwards."
        "When she's done, I risk a glance at the wall."
        "Three shots and three hits."
        "I wonder if that's more to do with my skills or Aletta's."
        $ aletta.sub += 5
    hide aletta
    show aletta suit
    "Aletta looks over my shoulder at the wall, smiling like a cat at the evidence of my performance."
    "She seems inordinately pleased with the effect her attentions seemed to have upon me."
    aletta.say "My turn!"
    "She takes the gun from me and replaces the clip, ensuring that she has a full load."
    show aletta shooting forest
    "And then she takes up a firing stance, looking at me with raised eyebrows."
    "It's then that I realise she's waiting for something."
    "Specifically, she's waiting to see if I'll reciprocate while she's shooting!"
    menu:
        "Don't":
            "What does she think this is, an exhibitionist's stroll in the woods?"
            "Sure, I'm bowled over that Aletta would give me a blowjob out here."
            "But it's not like I asked her to do it!"
            "Plus, it's not like she needs the help to clear her mind or anything."
            "Aletta's already a great shot!"
            mike.say "What are you waiting for?"
            mike.say "Fire away!"
            if not "aletta_event_05b" in DONE:
                $ aletta.love -= 5
            else:
                $ aletta.love -= 1
            "Aletta looks puzzled for a moment, and then she realises that I'm not about to give her oral any time soon."
            "Irritation and annoyance cross her face."
            "But then she buries those emotions under the veil of pretending not to give a shit."
            "A part of me thinks that it's high time I took some control back in this relationship."
            "What with guns, leathers and motorbikes, I sometimes feel like Aletta's the one constantly in the driving seat."
            with screenshot
            show aletta shooting forest fire
            play sound gun
            pause 0.2
            show aletta shooting -fire
            "With a cold efficiency that I suppose has to come mainly from my own actions, she reels off three shots in short order."
            "One after another, all three of her cans spin off into the trees as she hits them each in turn."
            hide aletta
            show aletta shooting forest
            "I clap and smile as she turns to regard me, more than a little haughtily."
            "While I might have refused to give her oral just now, my praise genuine."
            if not "aletta_event_05b" in DONE:
                $ aletta.sub += 5
            else:
                $ aletta.sub += 2
            "And I think Aletta can sense that, as she raises one eyebrow and returns a sliver of a smile."
            "If I'm right, and I sincerely hope that I am, I might actually have succeeded in making her respect me."
            "Maybe just a little."
        "Do it" if hero.fitness >= 50:
            "Well, fair's fair, I suppose!"
            "And really, is it that much of a chore to play with a girl the likes of Aletta?"
            "There are guys that'd kill for the chance to do just that!"
            "I nod eagerly, walking round behind her and open her fly."
            show aletta shooting forest finger open
            "In a moment, I have her suit open and pull it halfway down her thighs."


            "For all of her outward confidence, I can already feel her pussy almost quivering at my touch."
            with screenshot
            show aletta shooting forest finger open fire
            play sound gun
            pause 0.2
            show aletta shooting -fire
            "I probe the length of her pussy with one finger, and then hear the crack of the gun firing."
            hide aletta
            show aletta shooting forest finger open
            "A glance over her shoulder reveals that Aletta never even turned her head as she pulled the trigger, sending the shot way off target."
            "Realising what she's done, she shakes her head and tries to concentrate on the task at hand."
            "And now I see that I have a challenge too!"
            hide aletta
            show aletta shooting forest finger open juice
            "Using my fingers to stroke lower between Aletta's lips, I slip my free hand under her top and begin to massage her breasts."
            with screenshot
            show aletta shooting forest finger open fire
            play sound gun
            pause 0.2
            show aletta shooting -fire
            "She actually moans a little at that, but then steels herself and fires off a shot that I hear connect."
            hide aletta
            show aletta shooting forest finger open
            "My only answer is to take hold of one of her nipples and pinch it, beginning to push my fingers deeper still into her pussy."
            with screenshot
            show aletta shooting forest finger open juice fire
            play sound gun
            pause 0.2
            show aletta shooting -fire
            "Aletta tries to get off another shot before the effects take hold."
            hide aletta
            show aletta shooting forest finger open juice cum
            "But all too soon she's almost crying at what I'm doing to her pussy and breasts."
            "The fingers playing with her breasts are slick from her sweat, and those in her clit are already wrinkling from how wet she's become."
            with screenshot
            show aletta shooting forest finger open juice cum fire
            play sound gun
            pause 0.2
            show aletta shooting -fire
            "I almost forget the sound of the shots that she's firing, not really caring any longer who wins the shooting contest."
            show aletta shooting forest finger open juice cum
            "In the end, I vaguely hear the sound of Aletta dropping the gun onto the ground, before clasping her hands around my neck."
            show aletta shooting forest finger open juice cumhard
            "I still have my fingers deep in her pussy when she finally cums, and I feel every twitch and flex of her muscles as she does so."
            "Afterwards, I see one can missing, one on its side and another completely untouched."
            "A result of which I feel I can be quite proud."
            if not "aletta_event_05b" in DONE:
                $ aletta.love += 5
                $ aletta.sub -= 5
            else:
                $ aletta.love += 1
                $ aletta.sub -= 2
    hide aletta
    show aletta suit
    "Aletta packs the gun away in her bag, and links my arm as we walk back to the house together."
    "I'm not sure that I'll ever be fully comfortable combining guns and girls like this."
    "But for her, it was well worth the effort."
    if not "aletta_event_05b" in DONE:
        $ game.pass_time(2)
    return

label aletta_event_06:
    if aletta.love.max < 120:
        $ aletta.love.max = 120
    "I've been forced to keep secrets in the past and deal with all the guilt that comes along with that."
    "But I never thought that one day I'd end up trying to keep an actual murder under wraps!"
    "I mean sure, Dwayne wasn't the nicest of guys to be around and he was a pain to work for."
    "And on top of that, from what she told me before doing the deed, he made Aletta's life hell."
    "All of that should be enough for me to justify what she did to him, right?"
    "But there's still a part of me that can't get over the fact that Aletta shot him!"
    "It's the part of me that recoils at the idea of killing another human being."
    "No matter what a piece of shit they might have been!"
    "I keep telling myself that this isn't about my own guilt."
    "It's about protecting Aletta from the consequences of her actions."
    "That and making sure nobody has the chance to do what Dwayne did to her again."
    show aletta annoyed at center, zoomAt(1.0, (640, 720))
    "That's why I look up with a smile on my face when Aletta comes hurrying in to see me."
    show aletta at center, traveling(1.25, 0.3, (640, 880))
    mike.say "Hey, Aletta."
    mike.say "What can I do for you?"
    "Despite my best efforts to put a brave face on things, one look at her face has me worried."
    "Aletta seems nervous and haunted, glancing this way and that like she's afraid of being watched."
    mike.say "Aletta, did you hear me?"
    mike.say "What's the matter with you?!?"
    "Aletta seems to notice me for the first time as I say this."
    show aletta at center, zoomAt(1.25, (640, 880))
    show aletta stuned at startle
    "And she jumps a little, putting her hand to her chest as she does so."
    show aletta surprised
    aletta.say "Oh, [hero.name]!"
    aletta.say "You scared me out of my skin!"
    show aletta annoyed
    "I can't help frowning at Aletta."
    "How could I have surprised her like that?"
    "Didn't she come in here looking for me?"
    "And then it dawns on me."
    "The confusion, the paranoid stare and the fact she's on another planet right now."
    "The pressure must be getting to her!"
    mike.say "Aletta!"
    mike.say "Hey, Aletta!"
    mike.say "Look at me, Aletta - what's got you so riled-up?"
    show aletta whining
    aletta.say "I thought I could handle it, [hero.name]."
    aletta.say "I thought I'd just be so glad he was dead that it wouldn't matter."
    show aletta sadsmile
    mike.say "You...you mean Dwayne, right?"
    "At the mention of that name, Aletta seems to become instantly focused again."
    "She grabs hold of me by the wrists, clinging so hard that she's actually hurting me!"
    show aletta whining
    aletta.say "I can't get him out of my mind, [hero.name]!"
    aletta.say "Every time I close my eyes...he's there!"
    aletta.say "Every loud noise sounds like the gunshot!"
    aletta.say "I can't handle it!"
    show aletta sad
    "This is bad."
    "This is very bad."
    "If Aletta cracks like that in front of anyone else..."
    "Well, the consequences aren't worth dwelling on - save that it'd be bad!"
    "I have to do something."
    "I have to talk her round..."
    menu:
        "Reassure her":
            "Maybe this is partly my fault?"
            "Aletta's under so much strain right now."
            "No wonder she's on the verge of cracking up!"
            mike.say "Hey, Aletta..."
            mike.say "It's okay - I'm here for you."
            "I start to open my arms to make the point."
            "But Aletta surprises me by throwing hers around me the moment that I do."
            show aletta at center, traveling (1.5, 0.2, (640, 1040))
            pause 0.2
            with hpunch
            "She all but throws herself into my embrace, hugging me as close as she can."
            show aletta whining
            aletta.say "Oh, [hero.name]..."
            aletta.say "I'm so scared!"
            aletta.say "I don't know what I'd do without you!"
            show aletta sad
            "All I can do is hold Aletta close and try to reassure her."
            mike.say "Whoa, Aletta!"
            mike.say "It's going to be okay, I'll make sure of it."
            mike.say "I won't let anything happen to you - I promise."
            "My mouth might be writing cheques that my ass can't cash."
            "But I really do mean what I'm saying to Aletta right now."
            "If I can just offer her the support that she needs."
            "If I can just make sure that she can hold it together."
            "In fact, I know that I can do it!"
            "All Aletta needs is to know that she's not alone."
            "She needs me to be there for her, to be her rock."
            show aletta normal
            mike.say "Don't you worry about a thing, Aletta."
            mike.say "I'll keep you safe."
            $ aletta.love += 2
        "Snap out of it!":
            "Aletta need to toughen up."
            "And she needs to do it now!"
            mike.say "Aletta - snap the fuck out of it!"
            "The tone of my voice and choice of words has an immediate effect."
            show aletta stuned
            "Aletta blinks like she's been slapped across the face and falls silent."
            show aletta upset
            "And then she looks at me, square in the eye, like she's waiting for me to speak."
            "I guess Aletta's just not used to people talking to her like that."
            "So maybe it was enough to get through to her."
            mike.say "Don't come in here telling me that you can't handle it."
            mike.say "Because you HAVE to handle it, Aletta."
            mike.say "Otherwise you go to prison, and you don't get out."
            show aletta whining
            aletta.say "B...but..."
            aletta.say "I...I..."
            show aletta annoyed
            mike.say "Look at me, Aletta - I'm holding it together."
            mike.say "I'm doing it for the both of us, yeah?"
            mike.say "Because I was there and I kept my mouth shut for your sake!"
            mike.say "And I don't want to go to prison either!"
            show aletta sad
            "I can see that Aletta's almost shaking by now."
            "And I feel terrible to be laying into her like this."
            "But everything that I said is true."
            "If she confesses what she did, it's not only her neck on the line."
            "And I don't want to get passed around in prison like a chew-toy!"
            "So I keep on staring straight at Aletta, not daring to blink."
            "It comes as a relief a moment later when she looks away and nods."
            show aletta talkative
            aletta.say "O...okay, [hero.name]."
            aletta.say "I'll try my best."
            show aletta sadsmile
            "I smile the moment that the words are out of Aletta's mouth."
            "Nodding to reassure her, I try to seal the deal."
            mike.say "That's great, Aletta, really great."
            mike.say "All we need to do is keep quiet a little longer, yeah?"
            mike.say "Just until all of this blows over."
            show aletta normal
            "Aletta nods too, and returns the smile."
            "And I just hope that she means it too..."
            $ aletta.sub += 2
    $ hero.cancel_activity()
    $ game.pass_time(1)
    $ aletta.flags.delay = TemporaryFlag(True, 1)
    return

label aletta_event_07:
    if aletta.love.max < 140:
        $ aletta.love.max = 140
    "I've been itching to get the chance to eat at this restaurant for ages, ever since I saw the menu online."
    show aletta normal date at right with easeinright
    "But the moment that I lay eyes on Aletta as she walks in door, all thought of what I want to eat just vanishes."
    show aletta normal date at center with ease
    "The only thing that I can do is stare at my date as she strides confidently over to the table at which I'm sitting."
    "I'm seriously not exaggerating when I say that I can't remember Aletta ever looking as hot as she does right now!"
    "I don't even need to tear my eyes away from her to know that she's the centre of attention in the restaurant."
    "It's like I can feel the gaze of everyone else in the place following her progress."
    show aletta at center, zoomAt(1.5, (640, 1040)) with fade
    pause 0.5
    show aletta at center, zoomAt(1.5, (640, 1140)) with ease
    "That and the unspoken feelings of jealousy that are being aimed my way as she sits down across the table from me too!"
    show aletta embarrassed
    "Aletta looks calm and collected as she gets comfortable in her seat, not meeting my eye at first."
    "But I can tell from the self-satisfied smile on her face that she's more than a little pleased with her entrance."
    mike.say "Ah..."
    mike.say "Hey, Aletta!"
    mike.say "You're looking nice tonight..."
    hide aletta
    show restaurant meal aletta date nomeals with fade
    "At the sound of my faltering words, Aletta finally looks me straight in the eye."
    "She doesn't say anything at first, just makes a quiet chuckling sound."
    "But it's more than enough to let me know that she's purring like a happy cat on the inside right now!"
    aletta.say "Oh, what?"
    aletta.say "This old thing, really?"
    show restaurant meal aletta nomeals alettablush
    aletta.say "You're embarrassing me, [hero.name]!"
    aletta.say "All I did was throw on the first thing that came to hand."
    "I know that she's lying."
    "And Aletta knows that I know she's lying too."
    "So I just grin at her like an idiot and wave the waiter over."
    show restaurant meal aletta nomeals -alettablush waiter with fade
    "We order our food while I try to ignore the fact that the waiter's undressing Aletta with his eyes."
    show restaurant meal aletta -nomeals -waiter with fade
    "And it doesn't take long for what we chose to arrive, small-talk filling in all of the gaps as we wait."
    "But the whole time it feels like there's a tension in the air."
    "Like the sexual frustration that Aletta's charms are causing is hanging over us."
    "Eventually it seems to reach a peak."
    "And someone is compelled to speak up when it does..."
    if aletta.sub <= 30:
        show restaurant meal aletta alettabored
        "Aletta puts down her knife and fork, clearing her throat as she does so."
        mike.say "What's the matter, Aletta?"
        mike.say "Is there something up with your meal?"
        "Aletta shakes her head, dismissing my questions."
        "Then she leans her elbows on the table and cradles her chin on the palms of her hands."
        aletta.say "It's not that, [hero.name]."
        aletta.say "More like I haven't got much of an appetite tonight."
        show restaurant meal aletta -alettabored
        aletta.say "But I was thinking that you could help me out with that."
        "I have no idea where this is going."
        "But I'm still under the spell of Aletta's stunning outfit."
        "So I find myself nodding eagerly, almost without thinking."
        mike.say "Sure, Aletta."
        mike.say "Whatever you want!"
        show restaurant meal aletta alettahappy
        "Aletta smiles at my efforts to please her."
        "And then she leans closer, almost whispering into my ear."
        aletta.say "I want you to get under the table and eat me out, [hero.name]."
        show restaurant meal aletta alettablush
        aletta.say "Eat me out while we're eating out - that should give me an appetite!"
        "I look around the restaurant, noting all of the other people around us."
        "A part of me wants to say no on principal."
        "But that's not the part of me that seems to be in charge at the moment."
        "And the one that is in charge is thrilled at the danger of what Aletta's asking me to do!"
        mike.say "Okay, Aletta..."
        mike.say "I'm on it..."
        "Trying to look as natural as I can, I toss my napkin onto the floor."
        "And when I bend down to pick it up, I slip under the table."
        "I have no idea what Aletta's doing above me, and I try to push it out of my mind."
        "Instead I make straight for her legs, which part almost magically as I get close to them."
        "I'm about to reach for Aletta's panties when I see that there are none to be found."
        "She's been going commando all this time!"
        "I can imagine the smile spreading slowly across her face as she reveals it to me."
        "And knowing that she always had something like this in mind is already getting me hard."
        "Putting one hand on each of Aletta's thighs, I lower my head between them."
        scene aletta cunnilingus
        show aletta cunnilingus restaurant date noglasses
        with fade
        "Normally I'd start out slow and gentle, but this is different."
        "I can't stay down here forever, and there's a sense of urgency about things."
        "All of this means that I plunge my tongue straight between Aletta's lips."
        "At the same time, I press my own against them, just as if I were kissing her on the mouth."
        "She's already more than a little excited, and this shows as I get a taste of her."
        "And knowing that she's turned on makes her taste almost moreish!"
        "Wasting no time, I push my tongue as deep into her pussy as I can manage."
        show aletta cunnilingus pleasure
        "I feel Aletta's thighs tremble at my efforts, threatening to squeeze my head."
        "And I can only imagine what's going on above me too as she feels the effects."
        "The thought of her trying to suppress the sensations is a massive turn-on."
        "It's more than enough to make me work my hardest as I probe her pussy for all I'm worth."
        "Soon I can feel Aletta's clit as it rubs against the side of my tongue."
        "She's almost jumping out of her chair by now."
        "Fighting with all her strength to keep from crying out too!"
        show aletta cunnilingus ahegao
        "A second later I feel her hand in my hair, shoving my face into her crotch."
        "Aletta cums with my head trapped between her thighs, almost smothering me."
        "But then, just as suddenly, she releases me again."
        "I tumble backwards, scrambling back to my side of the table."
        scene bg restaurant
        show restaurant meal aletta date alettablush with fade
        "And when I haul myself up and into my seat, I'm treated to a rewarding sight."
        "Aletta looks shaken and stirred by what I've done to her."
        "Hair out of place and glasses askew, she's panting as she feels the aftershocks."
        "Her eyes are glassy and have a far-away look in them."
        "And so I just get back to eating my meal and leave her to recover."
        "If anyone asks, I'll just tell them that the food blew her mind..."
    else:
        "I put down my knife and fork, wiping my mouth on a napkin as I do so."
        "Aletta looks up at me, clearly wondering why I've stopped eating."
        "The interest on her face reminds me of the way things have been going between us recently."
        "Specifically the fact that I've been taking a more dominant role, helping relieve Aletta's stress."
        show restaurant meal aletta alettabored
        show fx question at left
        aletta.say "What's the matter, [hero.name]?"
        aletta.say "Is there something wrong with your meal?"
        "I cough to clear my throat."
        "And then I shake my head."
        mike.say "That's funny, Aletta."
        mike.say "Because I was just about to ask you the same thing!"
        mike.say "That and tell you I have something under the table."
        mike.say "Something that you might like the taste of better..."
        "I nod downwards in what I hope is a suggestive manner."
        show restaurant meal aletta alettablush
        "And I see a look of surprise and almost embarrassment appear on Aletta's face."
        "For a moment I think that I might have gone too far, that she'll say no."
        show restaurant meal aletta alettahappy
        "But then she gives me the briefest of nods and tosses her own napkin onto the floor."
        hide restaurant meal aletta
        show aletta date flirt at center, zoomAt(1.5, (640, 1140))
        with fade
        pause 0.5
        hide aletta with easeoutbottom
        "In the blink of an eye, Aletta's out of her seat and under the table."
        "I can hear her crawling over towards me."
        "And then I feel her parting my thighs and reaching for my flies."
        "I do the best I can to look casual, like nothing untoward is happening."
        "If anyone asks, my date just went to the bathroom, that's all."
        "Aletta wastes no time in reaching into my pants and pulling my cock out."
        scene bg black
        show aletta blowjob restaurant date with fade
        "The fact that the idea was already in my head to do this means it's already getting hard."
        "And the mere knowledge that she's making my fantasy a reality does the rest."
        "Let alone the actual feeling of Aletta playing with me under the table!"
        "Aletta begins to work the shaft, squeezing hard as she does so."
        "Normally I might have protested, told her to be more gentle."
        "But here and now it somehow adds to the sense of danger and urgency."
        "A moment later, she begins to lick and suck her way up from my balls."
        "And it feels like Aletta's aware of the fact we need to make this quick too."
        "Because she doesn't take it slow either, reaching the head of my cock swiftly."
        show mouth_insert aletta zorder 1 at zoomAt(1, (880, 200))
        "From there, she swallows it eagerly and as deep as she can manage."
        show aletta blowjob pleasure
        "Aletta shows me just how much of an appetite she has, not holding back."
        "More than once I find myself grabbing handfuls of the tablecloth as she works on me."
        "It's a battle to keep my face from showing it too."
        "When I take a sip of my drink or a mouthful of food, I'm fighting to do so."
        "And that's because Aletta's making me want to cry out thanks to what she's doing down there!"
        "But all of that changes the moment that I shoot my load."
        "It comes faster than it would if we were anywhere else while doing this."
        show mouth_insert aletta cum
        show aletta blowjob cum
        with vpunch
        "And there's no way that I can warn Aletta that it's about to happen."
        with vpunch
        "So as I let go, deep inside of her mouth, she has no time to prepare."
        show aletta blowjob ahegao with vpunch
        "I hear her gag, and then the table jerks as her head hits the underside."
        "My instinct is to check that she's okay."
        "But I push it down, knowing that to do so will blow our cover."
        hide mouth_insert aletta
        scene bg restaurant
        with fade
        "And so I just have to sit there and wait while she pulls herself together."
        "Eventually I feel her zipping me back up again."
        show aletta date flirt at center, zoomAt(1.5, (640, 1140)) with easeinbottom
        "A second later Aletta reappears and sits down in her chair like nothing happened."
        "She looks more than a little dishevelled, and she's wiping something off of her lip."
        "But her breathing is relaxed and she has a lazy smile on her face."
        mike.say "How was it, Aletta?"
        mike.say "Did it fill you up?"
        show aletta blush
        "Aletta lets out an exhausted little laugh."
        "Her cheeks are flushing just a tad."
        "And it makes her look even hotter than when she first walked in here."
        aletta.say "It filled me right up - no room to spare."
        aletta.say "In fact, I don't think I could eat another thing!"
    $ game.active_date.score = 85
    $ game.room = "map"
    $ aletta.flags.delay = TemporaryFlag(True, 1)
    return

label aletta_event_08:
    if aletta.love.max < 160:
        $ aletta.love.max = 160
    "I'm just sitting there in my office, pretending to work."
    "Telling myself that I'm not thinking about what happened to Dwayne."
    "I figure that if I just have to keep it up for long enough."
    "Long enough for me to start believing that we've gotten away with it."
    "Then maybe the feelings of guilt that have been gnawing at me will go away."
    play sound door_knock
    "In fact, I'm so engrossed in the act of telling myself that I don't hear a knock at the door."
    play sound door_knock
    "It only registers as a background noise, like the rest of the chatter in the office."
    "And it takes the person knocking to step into my field of vision for me to finally notice them."
    "Of course, this means that I also jump out of my skin at the same time..."
    show inspector at left with vpunch
    mike.say "Aargh!"
    mike.say "Oh god..."
    mike.say "You scared me to death!"
    "The man that I can now see standing in the doorway looks more than a little surprised."
    "But then why wouldn't he be, after I just jumped at the mere sight of him?"
    "He's an older guy, shabby-looking in shabby clothes that are as creased as his face."
    "His eyebrows are raised in apparent amusement though, rather than shock or offence."
    if "cherie_police_interview_male" in DONE:
        mike.say "Oh..."
        mike.say "Detective Michaels..."
        mike.say "Am I in trouble?"
        "Michaels" "You tell me!"
        "Michaels" "But today, we'd just like to talk to you about Mister Jackson."
    else:
        show inspector at left5 with ease
        "Detective" "Well, not actually to death."
        "Detective" "More like almost to death."
        "Detective" "You know, on account of you still being alive?"
        "It seems like a weird thing to say."
        "But I'm not in the mood to pull him up on it."
        "Still feeling paranoid, I try to ask what on earth he wants."
        mike.say "Ah...was..."
        mike.say "Was there something I can do for you?"
        mike.say "Are you lost or looking for someone?"
        "At this question, a change seems to come over the strange visitor."
        "It's like a light suddenly flickers on inside of his head."
        "He seems to remember just what he's doing here."
        show inspector at left4 with ease
        "Detective" "Strange you'd say that, young man."
        "Detective" "Because that's exactly why I'm here."
        "Detective" "I'm looking for someone called Dwayne - a colleague of yours, right?"
        "I feel like someone just pulled the ground out from under me."
        "And that I'm staring into a bottomless abyss threatening to swallow me whole!"
        "The man either fails to notice the look of horror on my face."
        "That or else he deliberately chooses to ignore it."
        "Detective" "I'm Detective Michaels, by the way."
        "Michaels" "Looking into this Dwayne guy's going missing."
    show inspector at center with ease
    "Michaels reaches into his coat and waves what must be his ID in my general direction."
    "It could be a cheese sandwich for all the attention that I can give it right now."
    mike.say "D...D...Dwayne?!?"
    "Michaels" "Yeah, you know him much?"
    "My mouth keeps on moving, but no sound is coming out."
    show inspector at center, zoomAt(1.25, (640, 880))
    "The detective takes another step towards me, a look of concern on his face."
    "Michaels" "What's the matter, son?"
    "Michaels" "You got something bothering you?"
    "Michaels" "Something you need to get off of your chest?"
    if aletta.love >= 140 or "cherie_police_interview_male" in DONE:
        "Suddenly the realisation hits me like a slap to the face."
        "This is just like one of those old cop shows you see on late-night television."
        "The detective catches the jittery suspect off-guard by being friendly."
        "Then he tricks the guy into spilling his guts and incriminating himself!"
        "There can't be any real evidence against Aletta or myself."
        "If there was, he'd have just walked in here and arrested us both!"
        mike.say "Oh..."
        if not "dwayne_corpse_discovery" in DONE:
            mike.say "It's just I'm worried, you know?"
            mike.say "Worried about Dwayne - since he went missing."
        mike.say "He was a good boss, and a such a great guy too!"
        "Michaels pauses for a moment, looking at me sideways."
        "It's like he wasn't expecting me to react that way at all."
        "Michaels" "Really?"
        "Michaels" "Because that's not how most folks around here describe him..."
        "All I can do is shrug and shake my head."
        "That and keep right on lying to a badge-carrying officer of the law."
        "I just tell myself that it's for Aletta and me, so it's a necessary evil."
        mike.say "You know how it is, detective."
        mike.say "Dwayne was a big-shot, a real high-flyer."
        mike.say "People either loved him or they were jealous of his success."
        "Michaels" "And it sounds like you were one of the former?"
        "Michaels" "You loved him?"
        "Michaels" "And you'd know, wouldn't you?"
        "Michaels" "Because you socialised with Dwayne and, what was her name..."
        mike.say "Aletta?!?"
        "Michaels" "That's the one!"
        "Michaels" "Real powerful aura off of that one."
        "Michaels" "The kind of woman a man'd do anything for - don't you think?"
        "I can see where he's going with this, where he's trying to steer me."
        "But I just shrug and shake my head all over again, refusing to be lead."
        mike.say "I wouldn't know about that, detective."
        mike.say "Aletta and I are colleagues and friends."
        mike.say "Nothing more than that."
        "Michaels shoots me one last glance."
        "And I can see in his eyes that he doesn't believe me."
        "But without proof to the contrary, he's facing a dead-end."
        "Michaels" "Okay, thanks for your help - it's been very useful."
        "Michaels" "If you do think of anything in the meantime..."
        "Michaels hands me a crumpled card with his contact details on it."
        "I take it, nodding and smiling the whole time."
        hide inspector with easeoutleft
        "And it's not until he's gone that I let go and sink down into my chair."
        "I'm drenched in sweat and my heart is pounding in my chest."
        "But all the same, I think I managed to fool him..."
        $ aletta.love += 5
        $ hero.cancel_activity()
        $ game.pass_time(1)
        $ aletta.flags.delay = TemporaryFlag(True, 1)
    else:
        "My eyes must be bulging out of their sockets by now."
        "If this guy really is a cop, then he'll know guilt when he sees it!"
        "Shit, he can probably even smell it on a person too!"
        "Maybe all of this stumbling and bumbling he's doing is just an act."
        "He's just playing with me, toying with my tortured conscience!"
        mike.say "Okay, okay..."
        mike.say "I'll confess, okay?"
        mike.say "Just stop it with the Jeudi mind-tricks already!"
        "Michaels expression becomes surprised again, this time genuinely so."
        "He backs off a little way, holding his hands up in a gesture of surrender."
        "Michaels" "Whoa...whoa..."
        "Michaels" "Settle down there, son."
        "Michaels" "Did you just say confess?"
        "I nod my head furiously, unable to stop myself."
        mike.say "Yes...yes I did!"
        mike.say "I can't take it anymore."
        mike.say "The guilt is eating away at me!"
        "Michaels" "Slow down for a minute."
        "Michaels" "You might want to hire a lawyer before you say more."
        "He's talking sense, of course, letting me know that I have rights."
        "But it's like the floodgates have opened now, and I can't stop myself."
        mike.say "No, I need to confess!"
        mike.say "It was Aletta - she shot him!"
        mike.say "She shot Dwayne and made me help her cover it up!"
        "Michaels remains quiet for a moment as he jots all of this down in his notebook."
        "And then he stuffs it back into his pocket, nodding grimly."
        "Michaels" "These are some serious allegations."
        "Michaels" "I'm going to need you to accompany me back to the station."
        scene bg office
        show inspector at center, zoomAt(1.25, (640, 880))
        with fade
        "I nod as I stand up and let Michaels lead me out of my office."
        "I have no idea of where this is going or what's in store for me."
        "But it feels so good to have unburdened myself."
        show aletta surprised at top_mostleft, dark with dissolve
        "So good that I almost don't notice Aletta, staring at me in horror as I walk out there..."
        $ aletta.set_gone_forever()
        $ hero.cancel_activity()
        $ game.pass_time(4)
    return


label aletta_event_09:
    if aletta.love.max < 180:
        $ aletta.love.max = 180
    "In the days after the incident with Dwayne, there's been little else on my mind."
    "Every waking moment seems to have been spent replaying the events of that day."
    "And whenever I manage to get a break for torturing myself, I'm always looking over my shoulder."
    "Of course the fact that the police came sniffing around the office only made things worse."
    "I can hardly concentrate on my work, and I expect every conversation to be bad news."
    show aletta at center, zoomAt(1.0, (340, 720)) with easeinleft
    "Which is why I find my heart hammering in my chest when Aletta comes striding up to me."
    "Sure, on the outside she looks suitably subdued and solemn."
    "Just the kind of mood you'd expect with the shadow of Dwayne's supposed disappearance hanging over her."
    "But I know her better than most people in the office ever could."
    "And I can read the emotions that are hidden under that carefully maintained demeanour."
    "That's why I try as best I can to keep my own expression neutral as she stops in front of me."
    show aletta at center, traveling(1.25, 1.0, (640, 880))
    mike.say "Hey, Aletta."
    mike.say "Was there something you needed?"
    show aletta embarrassed
    "Aletta doesn't answer me straight away."
    "Instead she looks around, making sure she can't be overheard."
    "Only when she's satisfied that we're alone does she start to speak."
    show aletta talkative
    aletta.say "Drop the act, [hero.name]."
    aletta.say "There's no need for it anymore."
    show aletta normal
    "At first I'm not sure what Aletta actually means."
    "I wonder if she's saying that I'm not convincing her."
    show aletta happy
    "But then I realise that she's beginning to smile at me."
    mike.say "I...I don't understand."
    mike.say "What are you saying, Aletta?"
    show aletta normal at center, traveling(2.5, 1.0, (640, 1640))
    "Aletta leans in closer still, as if it'll make a difference."
    "It's only now that I can see she's really trying to keep a handle on her emotions."
    "What I thought was just an upbeat mood seems more like mania this close up."
    "It scares me a little, as I'm so used to Aletta keeping her feelings under control."
    show aletta talkative
    aletta.say "It's over, [hero.name]."
    aletta.say "All of this horrible business with Dwayne."
    aletta.say "It's all finished with!"
    show aletta normal
    "I know that this should have cleared up all of my confusion at a stroke."
    "But it's such an unexpected development that it only makes things worse."
    "I saw Aletta empty a goddamn gun into Dwayne."
    "I saw the bullets enter his body."
    "And I'm pretty sure I saw the poor bastard check out too!"
    "I just don't understand how all of that can disappear so suddenly."
    mike.say "I don't get it, Aletta."
    mike.say "How can it be?"
    mike.say "For god's sake - the police were here just the other day!"
    "Aletta shakes her head at my objections, as if they're meaningless."
    show aletta talkative at center, traveling(1.5, 0.5, (640, 1040))
    aletta.say "The police just made an announcement, [hero.name]."
    aletta.say "They're ending their investigation into Dwayne."
    if "dwayne_corpse_discovery" in DONE:
        aletta.say "They discovered fraudulent transactions to offshore bank accounts which they linked to dangerous criminals."
        aletta.say "The official verdict is therefore that he was executed by a hitman hired by one of his acquaintances in the criminal underworld."
    else:
        aletta.say "The official verdict is that he skipped the country to avoid taxes!"
    show aletta normal
    "My head is still reeling from all of this."
    "I know that it means we're off the hook."
    "But it's like something inside of me still won't let go of the guilt and anxiety!"
    menu:
        "Celebrate":
            mike.say "Wow...I mean...just wow!"
            mike.say "That's fantastic news, Aletta!"
            mike.say "Why are we skulking about like this?"
            mike.say "Shouldn't we be celebrating?"
            mike.say "After all, it's not every day you get away with literal murder!"
            "Aletta winces a little at my admittedly poor choice of words."
            "But it's nothing more than a minor blip that she soon gets over."
            "And that's because my mood is now reflecting her own."
            show aletta talkative
            aletta.say "Maybe we should call it manslaughter in self-defence?"
            aletta.say "But you're right, [hero.name]."
            aletta.say "We should be celebrating the fact that he's dead!"
            show aletta normal
            "Again I see Aletta glance around."
            "It's as if she's worried someone might have sneaked up on us without being noticed."
            show aletta talkative
            aletta.say "But not here, okay?"
            aletta.say "Here we still need to be professional."
            show aletta normal
            "I nod eagerly, trying to let Aletta know I'm with her."
            "And my immediate rewards is feeling her hand below my waist."
            "I gasp as Aletta strokes my cock through my pants."
            show aletta talkative
            aletta.say "Don't judge me, [hero.name]."
            aletta.say "But getting away with murder..."
            show aletta flirt
            aletta.say "Well...it's kind of a thrill!"
            show aletta normal
            "I'm almost panting by now, imagining what Aletta has in mind."
            "But all she does is smile and then release me from her grip."
            show aletta at center, traveling(1.25, 0.3, (640, 880))
            pause 0.3
            hide aletta with easeoutleft
            "And with that, she turns and walks away."
            "Which leaves me alone with so many conflicting thoughts running through my head."
            "That and an embarrassingly stiff cock!"
            $ aletta.love += 2
        "Warn her":
            mike.say "Sure, it looks like we're going to get away with it."
            mike.say "But I still don't think we should be celebrating, Aletta."
            show aletta stuned
            "Aletta's expression turns to one of surprise and shock."
            "She doesn't seem to be able to process why I'm not elated too."
            show aletta surprised
            aletta.say "What's wrong, [hero.name]?"
            aletta.say "Aren't you happy for me?"
            show aletta stuned
            "Shit, this is going to be hard to articulate."
            "I have to separate my feelings for Aletta from my morals."
            mike.say "I couldn't be happier that you're not going to jail, Aletta."
            mike.say "But I can't forget the fact that we killed a man either."
            show aletta normal at center, traveling(1.25, 0.5, (640, 880))
            "Aletta pulls back from me, shaking her head."
            "I can see now that this scenario never occurred to her before now."
            show aletta whining
            aletta.say "But...but he was a monster, [hero.name]."
            show aletta angry
            aletta.say "You saw how he treated me."
            aletta.say "The things he made me do..."
            show aletta sad
            mike.say "I know all of that, Aletta."
            mike.say "And I hated Dwayne for it, you know that I did."
            mike.say "But he should have been the one going to jail - for what he did to you."
            show aletta at center, traveling(1.0, 0.5, (640, 720))
            "Aletta frowns as she backs away some more."
            "I can see that my words have hurt her, taken the edge off of her mood."
            "But I know her well enough to be sure that she's not going to just ignore them."
            "All I can do is wait and hope that she comes to see sense and understand."
            hide aletta with easeoutleft
            "Though for now, I have to settle for watching her walk away, shaking her head as she goes."
            $ aletta.sub += 5
    $ hero.cancel_activity()
    $ game.pass_time(1)
    $ aletta.flags.delay = TemporaryFlag(True, 1)
    return

label aletta_event_10:
    if aletta.love.max < 200:
        $ aletta.love.max = 200
    "Now that the whole business with Dwayne is over, I feel like a great weight has been lifted off of my shoulders."
    "Sure, it makes me a little guilty to think of it in that way, as it was Aletta that actually pulled the trigger."
    "But I was standing right there in the room when she did it, so I feel like I shared at least some of the trauma."
    "Though if anything, the fact that the police investigation is over seems to have cured her paranoia to a greater degree."
    "It's like she doesn't just want to draw a line under it all, but actually celebrate the fact that we got away with it."
    "And I guess that's why she's invited me up to Dwayne's office, the literal scene of the crime."
    scene bg ceo with fade
    "As soon as I walk in there, I'm transported back to the moment it happened."
    "The office has been professionally cleaned, and there's not a trace of evidence the thing happened at all."
    "But still, I can almost hear the gunshot and see what happened in the moments afterwards."
    aletta.say "Hey, [hero.name]."
    aletta.say "How different is this place now?"
    aletta.say "Like a throne room after the king's been beheaded!"
    show aletta happy at center, zoomAt(1.0, (640, 720)) with fade
    "I look over to where Aletta's standing, a triumphant smile on her face."
    "It takes an effort of will to push all thought of Dwayne out of my head in that moment."
    "And as I do so, I force what I hope is a convincing smile onto my own face too."
    show aletta normal
    mike.say "It's...weird, Aletta."
    mike.say "Being in here without Dwayne..."
    mike.say "Knowing that he's not coming back."
    show aletta talkative
    aletta.say "You can say it, [hero.name]."
    aletta.say "You can actually come out and say that he's dead."
    aletta.say "There's only the two of us here to hear it."
    show aletta normal
    "There's an awkward pause that drags on for a couple of seconds."
    "And it takes that time for me to realise that Aletta wasn't just reassuring me."
    "She seems to actually want me to come out and say the words!"
    show aletta whining
    aletta.say "What's the matter, [hero.name]?"
    aletta.say "Why won't you say it?"
    show aletta sadsmile
    mike.say "What difference does it make, Aletta?"
    mike.say "We both know what happened to Dwayne."
    mike.say "Why do you need to hear me say it?"
    show aletta talkative
    aletta.say "Because I don't think it's real to you."
    aletta.say "I don't think it will be until you actually say it."
    show aletta normal
    "I swallow and look away from Aletta for a moment, staring at the spot where it happened."
    "And then I look back at her, feeling my heart pounding in my chest."
    mike.say "He...he's dead, Aletta."
    mike.say "Dwayne's dead and you killed him!"
    show aletta happy
    "Aletta's smile is slow and languid as it spreads across her face."
    "She doesn't seem in the least bit troubled by hearing it said out loud."
    "In fact, if anything, it seems to make her confidence grow as I look at her!"
    show aletta talkative
    aletta.say "That's right, [hero.name]."
    show aletta angry
    aletta.say "I killed Dwayne in revenge for what he put me through."
    aletta.say "For all the things that he forced me to do for him."
    aletta.say "And to him..."
    show aletta upset
    "At the mention of the treatment she received from Dwayne, she pauses."
    "I can see that none of the wounds he inflicted on her have been healed by his death."
    "And in that moment, I stop feeling afraid and paranoid for myself."
    "Instead I feel an almost overwhelming sense of sympathy for Aletta instead."
    mike.say "He deserved to be punished for what he did to you, Aletta."
    show aletta normal
    "Aletta nods, struggling with the emotions that she must be feeling."
    show aletta talkative
    aletta.say "And you did the opposite of that, [hero.name]."
    aletta.say "You were always there for me when I needed you."
    aletta.say "So you deserve the opposite of what Dwayne got."
    aletta.say "You deserve a reward..."
    show aletta normal at center, traveling(1.25, 0.3, (640, 880))
    "With that, Aletta takes hold of my hand and leads me across the office."
    "Half intrigued and half stunned, I offer no resistance as we walk around Dwayne's desk."
    "Aletta pulls out the suitably large chair that goes with the palatial desk."
    scene office_cumshare_audrey_shiori_bg
    show aletta flirt at center, zoomAt(1.25, (640, 880))
    with vpunch
    "And then she pushes me down into it."
    "All I can do is watch in silence as she begins to strip off her clothes."
    show aletta topless with dissolve
    "Aletta goes slowly, clearly enjoying the way that I'm watching her."
    show aletta happy
    "And her smile gets wider with each and every item of clothing she drops on the floor."
    show aletta naked with dissolve
    "Once she's naked, Aletta turns her attention to me."
    show aletta normal at center, traveling(1.5, 1.0, (640, 1040))
    "She leans in close as she undresses me, talking the whole time."
    show aletta talkative
    aletta.say "I want you to feel what it was like to be him, [hero.name]."
    aletta.say "Sitting up here in his ivory tower, thinking he was king of the world."
    aletta.say "Because I know that you'll appreciate it like he never did."
    aletta.say "And because you deserve to feel like that too..."
    show aletta normal
    "Aletta's been massaging my cock as she says this."
    "And it's no surprise that I'm hard as a rock right now!"
    hide aletta
    show slap_npc_aletta at center, zoomAt(1.25, (640, 880))
    show slap_exp_happy_aletta at center, zoomAt(1.25, (640, 880))
    with fade
    "She turns her back on me, lowering herself down and onto me."
    "I gasp as I feel my cock rubbing against the lips of her pussy."
    "She's already slick, anticipating what we're about to do."
    "And she doesn't waste any time teasing me with it either."
    "Aletta sits down on me, letting my cock slide all the way in."
    "All I have to do is lean back and leave it all to her."
    scene office_cumshare_audrey_shiori_bg
    show slap_npc_aletta at center, zoomAt(1.25, (640, 880)), ride(0.3, -20)
    show slap_exp_happy_aletta at center, zoomAt(1.25, (640, 880)), ride(0.3, -20)
    "She works me from the start, bouncing up and down in my lap."
    "I always thought that where I was when we did it wouldn't make a difference."
    "Being inside of Aletta is already such an incredible feeling, so how could it?"
    "But somehow, doing it right here and now, feels so much more intense."
    "Maybe it's knowing that we conspired to kill Dwayne and got away with it."
    "Or perhaps there really is something about being surrounded by such opulence."
    "But I think that what might be going on is just what Aletta talked about."
    "She's so stunning, so effortlessly passionate and beautiful."
    "Being with her here makes me feel like the luckiest guy in the world."
    "And Dwayne had all of this, but it somehow wasn't enough for him."
    "Suddenly I don't feel intimidated or impressed by the memory of him."
    "I just feel sorry for the guy, that he was such an idiot."
    "I won't make the mistake of failing to appreciate Aletta!"
    "Inspired by that thought, I take a firm hold of Aletta."
    scene bg ceo
    show aletta naked at center, zoomAt(1.5, (640, 1040))
    with vpunch
    "And then I stand up, turning Aletta around and pushing her backwards onto the desk."
    show aletta haircut surprised with dissolve
    "She cries out in surprise, but then realises what I'm doing."
    scene bg black
    show aletta ceofuck vaginal
    with vpunch
    "Aletta braces her hands on the desktop, nodding eagerly."
    "And then I'm pounding her like my life depends on it."
    "Aletta keeps on nodding the whole time, urging me on."
    aletta.say "Oh yes..."
    aletta.say "Please, [hero.name]..."
    aletta.say "Just like that..."
    aletta.say "Don't stop until you make me cum!"
    if aletta.flags.submissive_interact:
        aletta.say "Use me as your target practice!"
    show aletta ceofuck pleasure
    "Aletta's words are a turn-on for sure."
    "But it's not like I need the encouragement!"
    "It's like I can feel all the guilt draining out of me as I fuck her."
    "Every thrust and the moans it elicits from Aletta purge me of it."
    "She's right - Dwayne was an asshole that deserved everything he got."
    "And I deserve to be screwing Aletta in his office right now!"
    "All of my energy goes into one last thrust as I start to cum."
    show aletta ceofuck creampie with hpunch
    "Aletta moans as I shoot my load into her, wriggling her ass as she takes it."
    with hpunch
    "I keep my cock inside of her as she cums too, feeling every moment as she does so."
    with hpunch
    aletta.say "I...I love you, [hero.name]!"
    aletta.say "I love you so much!"
    menu:
        "I love you too":
            "For a moment I'm overcome and I can't find the words to reply."
            "And then it all comes rushing out of me in a mad babble."
            mike.say "You do?!?"
            mike.say "Oh my god!"
            mike.say "I...I love you too, Aletta!"
            mike.say "I love you like crazy!"
            "Aletta positively beams at me as she turns over onto her back."
            "My cock slides out of her as she does so, but neither of us seems to notice."
            "All I can do is stare at the look of complete satisfaction on her face."
            "I don't think I've ever seen Aletta look that way before now."
            "There's no mask of professionalism or superiority."
            "She just looks...well, happy!"
            "Aletta strokes my cheek with her hand."
            scene bg ceo
            show aletta kiss naked haircut
            with fade
            "And then she leans up to kiss me."
            "It's long and slow, every moment feeling good."
            "And once it's over, we gather up our clothes and begin to get dressed."
            "Neither of us speaks as we do so, but there's no awkwardness in the silence."
            "It's more like both of us have said all that we need to say for now."
            "And we can just be together without speaking a word."
            "Aletta all but confirms this when she takes a hold of my hand as we leave the office."
            "She doesn't look me in the eye, but she squeezes my palm as we walk out of there."
            "Sure, it's a little thing - but it means the world to me."
            $ aletta.love += 10
            $ aletta.flags.kiss += 1
        "I don't":
            "I can almost feel my cock shrivelling up as Aletta utters those words."
            "Hastily pulling out and beginning to grab my clothes, I turn my back to her."
            scene bg ceo
            show aletta naked whining haircut at center, zoomAt(1.5, (640, 1040))
            with fade
            aletta.say "[hero.name]?"
            aletta.say "What's wrong?!?"
            show aletta sadsmile
            "I shake my head, still reeling from the emotions that I'm feeling."
            mike.say "I...I wasn't expecting that, Aletta."
            mike.say "You kinda took me by surprise!"
            show aletta embarrassed blush
            "Aletta's covering herself with her hands now."
            "Which is not a good sign after we just fucked like rabbits."
            show aletta whining
            aletta.say "I'm sorry, [hero.name]."
            aletta.say "I just thought that we were being honest."
            aletta.say "And...I mean it - I do love you!"
            show aletta normal
            "I'm almost dressed by now, pulling on my shirt."
            "I nod hastily, more to acknowledge what Aletta said than agree with it."
            mike.say "That's great, Aletta."
            mike.say "But I can't wrap my head around that shit right now."
            mike.say "Maybe hold that thought for now, yeah?"
            mike.say "And we can talk about it later?"
            show aletta sad
            "Aletta nods slowly, already looking sad and wounded."
            "I know that this is a jerk move on my part."
            "But I only just dealt with being an accessory to murder!"
            "I just have to hope that I can make it up to her later."
            "All of this is going through my head as I hurry out of the office."
            "And I make a point of not looking back to see Aletta as she gathers up her own clothes."
            $ aletta.love -= 10
    $ hero.cancel_activity()
    $ game.pass_time(1)
    return

label aletta_event_06_alt:
    if aletta.love.max < 120:
        $ aletta.love.max = 120
    scene expression f"bg {game.room}" with fade
    "I'm used to hearing the sound of Aletta's voice in the office."
    "And more often than not it's raised and telling someone else off."
    "Which is why my ears perk up at the sound of her being defensive."
    "It's just something so rare I can't help listening in out of sheer curiosity."
    aletta.say "Please!"
    aletta.say "I already asked you to stop..."
    aletta.say "This isn't the time or the place!"
    "I'm already thinking about going to see what the problem could be."
    "But then I hear the response that Aletta's pleading earns her."
    "And I know exactly what's going on!"
    dwayne.say "And I already said that's not going to happen, Aletta!"
    dwayne.say "I paid for everything in this building, including your salary."
    dwayne.say "That means I also paid for every last scrap of clothing you have on too."
    dwayne.say "It means that I own YOU, Aletta!"
    dwayne.say "Now do as I say - take off your top!"
    "I could have missed the meaning of every word he said and still known it was Dwayne."
    "Nobody else in the entire company would be so forward, inappropriate and entitled!"
    "I'm out of the door and headed in their direction in the blink of an eye."
    "And when I get there, the scene is just as I imagined it."
    scene bg alettaoffice
    show aletta pain at left5
    show dwayne angry
    with fade
    "Dwayne's leaning over Aletta."
    "Using his height and build to intimidate her."
    "Aletta must have heard me approaching."
    "As I can see the relief on her face."
    show aletta normal at left with ease
    aletta.say "Th...there you are, [hero.name]!"
    aletta.say "Just the person I wanted to talk to!"

    "Dwayne turns to look in my direction."
    "And I can see from the expression on his face that he's not pleased to be interrupted."
    dwayne.say "Nothing to see here, [hero.name]."
    dwayne.say "Aletta and I were just discussing a business matter."
    dwayne.say "One that's way above your pay-grade too."
    dwayne.say "So you can run along now, yeah?"
    "I can feel Dwayne's gaze burning into me."
    "And part of me wants to do as he says - just get the hell out of there."
    "But what kind of a friend would that make me when Aletta needs my help?"
    mike.say "Must be really sensitive if you need to get that close, Dwayne."
    mike.say "Come to think of it, I've never seen you get that close to your own wife!"
    show aletta normal at mostleft5 with ease
    aletta.say "Oh yeah, Dwayne - how is Cherie these days?"
    "At the mere mention of his wife's name, Dwayne shoots a mean look at Aletta."
    "But then he turns his attention back to me."
    "Like he senses that I'm the real potential danger here."
    dwayne.say "[hero.name]..."
    dwayne.say "Did you hear what I just said to you?"
    dwayne.say "Or are you suffering from a loss of hearing?"
    dwayne.say "Because if it's neither of those two things..."
    dwayne.say "Then you're getting pretty damn close to me firing your ass!"
    "I can feel the animosity in what Dwayne's saying to me."
    "And part of me is sure that he actually means it too."
    "But it's too late for me to think about backing down now."
    mike.say "Oh yeah?"
    mike.say "And exactly what would you be firing me for, Dwayne?"
    mike.say "Pretty hard to do that without a damn good reason these days, isn't it?"
    show dwayne annoyed
    "Dwayne narrows his eyes, obviously thinking about my retort."
    "I guess he's used to that threat being enough on it's own."
    aletta.say "He's right, Dwayne."
    show aletta annoyed
    aletta.say "It'd go straight to a tribunal."
    aletta.say "And who knows what would come out there..."
    "Dwayne lets out a growl of frustration."
    "But he stands back from Aletta at the same time, holding up his hands."
    dwayne.say "Well-played, well-played..."
    dwayne.say "But you'd better come up with a new game-plan."
    dwayne.say "Because this isn't over yet - not by a long way!"
    "With that, he turns on his heel and walks briskly away."
    hide dwayne
    "Aletta waits for him to be well and truly gone."
    "Then she lets out a sigh of relief and turns to face me."
    aletta.say "Thanks for the help, [hero.name]."
    show aletta embarrassed at center with ease
    aletta.say "Usually I can handle Dwayne's advances."
    aletta.say "But today it he was as though he wouldn't take no for an answer!"
    "I do the best I can to look concerned."
    "But it's hard, as I love having Aletta so grateful to me."
    mike.say "No worries, Aletta."
    mike.say "I just wish I could have got here sooner."
    mike.say "Are you sure you'll be okay?"
    mike.say "I can stay if you think he'll come back?"
    "Aletta shakes her head."
    aletta.say "That's kind of you to offer."
    show aletta normal
    aletta.say "But he won't be back any time soon."
    aletta.say "Dwayne's going to need time for his ego to heal."
    aletta.say "Time for his delusional mind to paint this as a victory for him too!"
    "Reluctantly I nod and turn to go."
    mike.say "Okay, Aletta."
    mike.say "But I'll be listening out all the same."
    aletta.say "Thanks, [hero.name]."
    show aletta happy
    aletta.say "That's good to know."
    "As I walk away, I'm sure that Aletta means what she's saying."
    "And that knowledge makes me feel like I'm needed around here."
    $ aletta.love += 2
    $ aletta.flags.delay = TemporaryFlag(True, 1)
    $ hero.cancel_activity()
    $ game.pass_time(1)
    return

label aletta_event_08_alt:
    if aletta.love.max < 160:
        $ aletta.love.max = 160
    scene expression f"bg {game.room}" with fade
    "I can barely see over the top of the files that are piled atop my desk."
    "And I'm so lost in the task I'm trying to complete that I've lost track of time."
    "Both of those are reasons that I don't look up when someone knocks on my door."
    "I just keep on doing what I've been doing for days on end."
    show aletta normal
    aletta.say "Hello, [hero.name]..."
    aletta.say "Have you had some lunch yet?"
    mike.say "Huh..."
    mike.say "What?"
    mike.say "Just put it on the pile, okay?"
    hide aletta
    show aletta close a with fade
    "The next thing I know, there's a hand waving in front of my face."
    "Instinctively I jump backwards in surprise and alarm."
    mike.say "What the..."
    mike.say "Oh...hey, Aletta!"
    mike.say "Sorry, but I was miles away."
    hide aletta close
    show aletta normal
    with fade
    "Aletta lets out a sigh as she surveys the organised chaos of my office."
    aletta.say "It certainly looks like it, [hero.name]."
    aletta.say "What did you do to deserve all of this?"
    "I lean back in my chair, rubbing the bridge of my nose."
    "And I let out a sigh of my own before I explain things to Aletta."
    mike.say "Don't take this the wrong way, Aletta."
    mike.say "But I think it was trying to help you out the other day!"
    "Aletta looks puzzled for a moment."
    "But then realisation dawns, and she frowns."
    aletta.say "You have to be joking, [hero.name]?"
    show aletta embarrassed
    aletta.say "Is he really that petty?"
    "All I can do is shrug and gesture to all of the files and papers."
    mike.say "You tell me, Aletta."
    mike.say "The very next day it's audit this, recalculate that!"
    mike.say "And all of it's coming straight down from the top too."
    "Aletta frowns and lets out a frustrated sigh."
    "Then she shakes her head with a strained smile."
    aletta.say "I guess you're starting to regret standing up for me!"
    show aletta normal
    aletta.say "Sorry you had to get dragged into this, [hero.name]."
    "As soon as the words are out of her mouth, I'm shaking my head too."
    mike.say "No way, Aletta!"
    mike.say "I don't regret that for a second!"
    "I see the reaction this instantly stirs in Aletta."
    "She looks relieved, like a weight's been lifted off her shoulders."
    "Aletta nods as she takes a few more steps into my office."
    show aletta happy
    aletta.say "That's a relief!"
    aletta.say "Because it'd have made this pretty awkward for me."
    mike.say "Made what awkward, Aletta?"
    mike.say "Just coming over to say hi to me?"
    show aletta normal
    aletta.say "Oh no, [hero.name]."
    aletta.say "I was talking about me asking if you wanted to have lunch with me."
    aletta.say "Because there's this great new place opened up a few blocks away."
    aletta.say "And the sandwiches they do there are to die for!"
    "On pure instinct alone, I start to get up and push my chair back."
    "But then reality bites, and I sit back down with a groan."
    mike.say "I'd love to, Aletta."
    mike.say "But I really have to keep on working."
    mike.say "If I leave the office, I'm worried I'll never get through all of this!"
    "Aletta nods at this."
    "But I notice that she doesn't look at all disappointed."
    "In fact she's actually smiling and nodding."
    aletta.say "I thought that would be the case."
    show aletta wink
    aletta.say "So I called ahead and had them deliver!"
    "Aletta pulls a bag from behind her back."
    "And whatever's in there smells delicious!"
    show aletta happy
    "Aletta's smile becomes wider as she sees my reaction to the food."
    "She sashays the last few feet to my desk and then perches on the edge."
    "Finally she opens the back and removes the contents, spreading them out before me."
    show aletta normal
    aletta.say "I know it's not much, [hero.name]."
    aletta.say "But think of this as my way of saying thanks."
    aletta.say "Because it means a lot knowing I have you around to back me up."
    mike.say "Any time, Aletta."
    mike.say "Just call and I'll be there!"
    aletta.say "Like my own personal bodyguard!"
    mike.say "Ah..."
    mike.say "I like to think of myself more like a superhero."
    show aletta happy
    "Aletta laughs and shakes her head."
    "But she's still smiling, which I take as a good sign."
    "What follows is a well-earned break for me."
    show aletta normal
    "And more importantly, it's some quality time spent with Aletta."
    "But all too soon the food is gone and it's time to get back to work."
    mike.say "We should do this again, Aletta."
    aletta.say "You're right, we should."
    "Aletta and I exchange a little wave as she walks out of my office."
    "But I can't help thinking that it means far more than that to both of us."
    $ aletta.love += 2
    $ aletta.flags.delay = TemporaryFlag(True, 1)
    $ hero.cancel_activity()
    $ game.pass_time(1)
    return

label aletta_event_09_alt:
    if aletta.love.max < 180:
        $ aletta.love.max = 180
    scene expression f"bg {game.room}"
    "I've managed to get through most of the bullshit work that Dwayne's lumbered me with."
    "But that doesn't mean that I'm having an easier time of things now."
    "Because I'm behind on my regular work as a result of all the extra stuff I had to do."
    "So now I'm having to work twice as hard just to get back up to speed!"
    "All the same, I still drop everything the moment I get a message from Aletta."
    "At first I fear the worst, that Dwayne's been up to his old tricks again."
    "But when I pick up my phone and read the message, I breathe a sigh of relief."
    "It's just Aletta asking me to come help her out with something in her office."
    "So I drop what I'm doing and hurry out the door."
    mike.say "Aletta..."
    mike.say "It's me!"
    "I rap on the door, just to be sure she hears me."
    "And the answer comes almost straight away."
    aletta.say "You're here already?"
    aletta.say "That's great, [hero.name]."
    aletta.say "Come right in!"
    scene bg alettaoffice
    show aletta
    with fade
    "I don't hesitate to open the door and hurry inside."
    "I turn to close it behind me, but then jump in surprise."
    "Aletta isn't sitting at her desk like I'd expected her to be."
    "She's standing right there in front of me."
    "I open my mouth to ask her what's going on."
    "But she pounces on me a moment later."
    "And I do mean she pounces on me."
    "There's no other way to describe it!"
    "Aletta wraps her arms around me and pulls me close."
    show aletta kiss with fade
    $ aletta.flags.kiss += 1
    "She plants her lips against mine and kisses me with a passion."
    "Taken completely by surprise, I'm helpless to resist."
    "And I find myself being dragged towards her desk."
    "Gasping and panting, Aletta breaks off the kiss."
    hide aletta kiss
    show aletta happy with fade
    aletta.say "Ah..."
    aletta.say "Oh god..."
    aletta.say "I needed that!"
    "By now I'm pinned to Aletta's desk, with her straddling me."
    "And while I'm still more than a little shocked, I'm not resisting in the slightest."
    mike.say "H...happy to..."
    mike.say "Happy to be of help, Aletta!"
    "Aletta smiles and licks her lips."
    "A sight which turns me on almost as much as the kiss did."
    aletta.say "You know how it is, [hero.name]."
    aletta.say "Me and you..."
    show aletta flirt
    aletta.say "We work so HARD around here!"
    "As she says this, Aletta chooses that moment to grab my cock."
    "And then she squeezes it, like her point needs underlining."
    aletta.say "What we need is to let off steam."
    aletta.say "Have a better work-life balance."
    mike.say "Y...yeah, Aletta..."
    mike.say "How would..."
    mike.say "How would that work?!?"
    aletta.say "Well..."
    show aletta happy
    aletta.say "It'd start with you putting your cock inside me!"
    "I nod furiously as Aletta undoes my flies."
    show aletta topless with dissolve
    "And then I watch as she strip off her clothes."
    show aletta naked with dissolve
    "She wastes no time in rubbing it between her legs."
    "I can feel that she's already pretty slick down there."
    "And the thought of her waiting for me with a wet pussy is almost too much."
    scene bg black
    show aletta cowgirl naked office
    with fade
    mike.say "Aletta..."
    mike.say "Oh fuck..."
    "Aletta smiles down at me as she pushes the head of my cock home."
    "But she can't keep it up as her own body begins to surrender too."
    "Pretty soon her face melts into an expression of sensual delight."
    show aletta cowgirl vaginal
    "And at the same time I can feel her sinking down onto me."
    aletta.say "Oh, [hero.name]..."
    aletta.say "Forget the kiss..."
    aletta.say "This is what I really need!"
    show aletta cowgirl pleasure
    "All I can do is lie back and let Aletta have her way with me."
    "She forces me down onto the desk, riding me for all she's worth."
    "Before too long, Aletta has me pinned down and totally helpless."
    "All I should have to do is enjoy the experience of her having her way with me!"
    dwayne.say "Hey, Aletta..."
    dwayne.say "I just wanted to..."
    dwayne.say "WHAT THE HELL?!?" with vpunch
    "Aletta and I freeze on the spot."
    show aletta cowgirl normal
    "Then as one we look towards the door."
    "Luckily for us, it closed behind the person that walked in on us."
    show dwayne angry at mostright5
    "But that's a small mercy, as we're now both staring at Dwayne."
    "And let's just say that he doesn't look happy."
    "His eyes are bulging and I can see veins standing out on his bald head!"
    hide aletta cowgirl
    scene bg alettaoffice
    show dwayne angry at mostright5
    show aletta naked angry
    with fade
    aletta.say "What do you think you're doing!"
    aletta.say "You can't just barge in here like this!"
    "Aletta's scrambling off of me as she says this."
    "And I'm trying as best I can to shove my cock back into my pants."
    "Luckily for me, being told off seems to distract Dwayne for a moment."
    "Which allows me to get myself straightened up."
    dwayne.say "What am I doing?"
    dwayne.say "I'm the goddamn boss - I go where I like!"
    dwayne.say "You two are the one's fucking on company time!"
    show dwayne angry at right with ease
    "Dwayne's advancing into the office as he says all of this."
    "And for the moment, it seems like his attention is focused on Aletta."
    "Which means that I have the chance to choose how I try to handle this."
    "So what am I going to do here?"
    menu:
        "Confront Dwayne":
            "I have to stand up to Dwayne, just like I did before."
            "Last time I proved that he's not as tough as he makes out."
            "So it should be a piece of cake to make him back down."
            mike.say "Oh, come on, Dwayne..."
            mike.say "You already tried to pull the big man act on me once before."
            mike.say "It didn't work then and it won't work now."
            show aletta surprised
            "Aletta's eyes go wide as she hears what I say."
            "But I try to ignore the look on her face and press on."
            "It's Dwayne I have to convince, not her."
            dwayne.say "Whoa..."
            dwayne.say "Did you just..."
            show dwayne annoyed
            dwayne.say "Did you just say what I think I heard you say?"
            mike.say "You heard me alright, Dwayne."
            mike.say "And you know that I'm right."
            dwayne.say "Is that so?"
            mike.say "You know it is, Dwayne."
            mike.say "You know what Aletta and I do together is none of your business."
            mike.say "So if you just walk away, we can pretend none of this ever happened."
            "For a moment, Dwayne doesn't move or say a word."
            "And I'm beginning to think that he's coming round to my offer."
            show dwayne angry
            "But then I see something break inside of him."
            "A slight twitch of the eye, a tightening of the jaw."
            hide aletta
            hide dwayne
            show dwayne fight neck at hshake
            "Then he just launches himself at me!"
            "I don't have time to react before his hands are around my throat."
            "They're huge and feel like they're made of something harder than flesh and bone."
            "Instinct alone makes me lash out, trying to hit him somewhere that hurts."
            scene bg alettaoffice at blur(8)
            show dwayne fight neck at blur(8)
            with dissolve
            "But it's no use, and he just keep on squeezing ever harder."
            scene bg alettaoffice at blur(8), dark
            show dwayne fight neck at blur(8), dark
            with dissolve
            "My vision starts to go blurry, and I know I'm passing out."
            scene bg alettaoffice at blur(16), dark
            show dwayne fight neck at blur(16), dark
            with dissolve
            "All I can hear is the sound of Aletta screaming in the background."
            scene bg alettaoffice at blur(16), dark, dark with dissolve
            "And then I black out."
            "But I have no idea if I'm unconscious or even still alive."
            "That is until the hands around my throat finally let go."
            "Then reality comes rushing back as I fall into heap on the floor."
            "I hear a sound that must be Dwayne storming out of the room."
            scene bg alettaoffice with dissolve
            "But I'm in no fit state to do anything but lie still, gasping for breath."
            call injured from _call_injured_3
        "Ease the tension":
            "I have to be the bigger man here, try to make peace."
            "After all, we're all adults here, and we have to work together."
            mike.say "Okay, Dwayne, okay..."
            mike.say "I'm going to need you to take a step back."
            mike.say "Step back and take a deep breath while you do that."
            "At the sound of my voice, Dwayne rounds on me."
            "It's almost like he half forgot I was even here."
            show dwayne annoyed
            dwayne.say "Take a deep breath?"
            dwayne.say "What in the hell are you talking about?!?"
            "Even though he's looming over me, I press on."
            "I have to show Dwayne that he can't intimidate me."
            "That way we can establish a dialogue and move on."
            mike.say "Look, Dwayne..."
            mike.say "I know you're into the whole alpha male thing."
            mike.say "And Aletta being with me is a challenge to that."
            "Dwayne narrows his eyes and fixes me with a hard stare."
            "He's honestly looking at me like I have steaming turds hanging out of my mouth right now!"
            show dwayne angry
            dwayne.say "You think the problem here is ME?!?" with vpunch
            dwayne.say "Let's get something straight here."
            dwayne.say "I pay you two to work for me."
            dwayne.say "Not to fuck each other on company time!"
            show aletta annoyed
            aletta.say "But it's fine for you to do that, Dwayne?"
            aletta.say "It's a different rule for the boss?"
            "Dwayne shoots a venomous glare at Aletta."
            "And he nods his head."
            dwayne.say "You bet it is, bitch."
            dwayne.say "I'm the boss, and I get to do all kinds of things you guys don't."
            dwayne.say "Like firing people that I find fucking when they should be working!"
            dwayne.say "Get your shit together, [hero.name]."
            dwayne.say "Because you're out of here!"
            "With that, Dwayne turns on his heel and strides out of Aletta's office."
            hide dwayne with easeoutleft
            "Which leaves the two of us staring at each other in amazement."
            "Did that just happen?"
            "Did he just fire me for real?"
            $ game.flags.fired = True
            $ game.flags.job_day = False
    $ aletta.love += 5
    $ aletta.sexperience += 1
    $ aletta.flags.delay = TemporaryFlag(True, 1)
    $ hero.cancel_activity()
    $ game.pass_time(1)
    return

label aletta_event_10_alt:
    if aletta.love.max < 200:
        $ aletta.love.max = 200
    scene expression f"bg {game.room}" with fade
    "I hate to admit it, but I'm still more than a little jumpy after what happened with Dwayne."
    "All it takes is the slightest unexpected noise or someone to sneak up on me unawares."
    "And the result is that I literally jump out of my seat, thinking I'm being attacked again."
    "It doesn't help that I have bruises all over me and it's painful to move my neck."
    "So I end up wincing from the pain as I jump as well."
    show aletta normal with fade
    aletta.say "Hey, [hero.name]!"
    mike.say "Wha..."
    mike.say "Arrgh!"
    mike.say "Fucking hell!"
    "Holding the crick in my neck, I look up to see Aletta standing in front of me."
    "She did have a pretty happy look on her face a few moments ago."
    "But now it's fast turning into one of embarrassment and genuine concern."
    show aletta sad
    aletta.say "Oh my!"
    aletta.say "Are you okay?"
    aletta.say "I didn't mean to..."
    "I wave away Aletta's concern with one hand."
    "Still using the other to massage the tortured muscles of my neck."
    mike.say "It's okay, Aletta..."
    mike.say "It really is getting better."
    mike.say "I'll be fine in no time, I promise."
    show aletta normal
    "Aletta nods as she walks over to me."
    "But all the same, I can see a look of genuine concern in her eyes."
    aletta.say "Erm..."
    aletta.say "Okay, [hero.name]."
    aletta.say "If you say so..."
    "There's an awkward pause as I keep on nursing my neck"
    "And at the same time, Aletta seems to have lost track of what she wanted to say."
    "I smile and do the best I can to encourage her."
    "Finally resorting to a vocal prodding."
    mike.say "You were saying?"
    "Aletta starts and nods."
    "And that lets me know that this must be serious."
    "Because Aletta's not usually tongue-tied or scatter-brained."
    "Not in any way, shape or form."
    aletta.say "Yes..."
    aletta.say "Of course..."
    aletta.say "I just wanted to say that you finally did it."
    show aletta dreamy
    aletta.say "You finally managed to get Dwayne off my back!"
    "At the mere mention of the guy's name I flinch."
    "Which sends another jolt of pain through my tortured muscles."
    mike.say "Ouch!"
    mike.say "Are you sure about that, Aletta?"
    mike.say "Because I thought I handled it the time before that."
    mike.say "Then the next thing I know, Dwayne's got his hands around my neck!"
    mike.say "Part of me is worried that he'll have me shot the next time!"
    show aletta normal
    "Aletta shakes her head at this."
    "And I can see that she's totally serious."
    "Which kind of makes me feel bad for cracking jokes in bad taste."
    aletta.say "I mean it, [hero.name]!"
    aletta.say "Dwayne really crossed the line this time."
    aletta.say "People actually saw what he did to you."
    aletta.say "They know what he's capable of now."
    mike.say "Good to know I'm not the only one!"
    aletta.say "Seriously, [hero.name]!"
    aletta.say "If he so much as raises his voice he could get sued!"
    aletta.say "And if that happens, then he's finished."
    aletta.say "Nobody will want to have anything to do with him."
    "The confidence in Aletta's voice is more than enough to convince me."
    "And I know that she wouldn't lie about something like this."
    "Slowly, and for the first time I start to believe what she's saying."
    "Maybe Dwayne really has gone too far this time."
    "And if that means he's going to leave Aletta alone..."
    "Well, then it was worth the pain I had to go through to make it happen."
    mike.say "That's great news, Aletta."
    mike.say "What's important is that he's not harassing you anymore."
    mike.say "And thanks for coming to tell me the good news."
    "At this, Aletta's expression changes."
    "Suddenly she looks less sure of herself."
    "Maybe even a little embarrassed."
    aletta.say "That's not really why I'm here, [hero.name]."
    show aletta flirt
    aletta.say "I mean, yes - I did come to tell you that."
    aletta.say "But what I really wanted to say was, thank you."
    mike.say "For what?"
    mike.say "Letting Dwayne throttle me?"
    aletta.say "No..."
    show aletta flirt blush
    aletta.say "For making me realise that I love you!"
    "It takes a moment for what Aletta just said to really sink in."
    "I have to stare at her and shake my head to understand the words."
    mike.say "Y...you're serious, Aletta?"
    mike.say "I mean...that's great!"
    mike.say "It's amazing - because I love you too!"
    mike.say "I guess that's why I did what I did..."
    "Aletta nods at this."
    show aletta happy
    aletta.say "I'm an independent woman, [hero.name]."
    aletta.say "I'd never ask a man to fight my battles for me."
    aletta.say "But you did what you did without a second thought."
    aletta.say "You weren't trying to impress me or make yourself look tough either."
    mike.say "Good job too - because it got me my ass kicked!"
    "Aletta chuckles and shakes her head."
    show aletta normal
    aletta.say "Maybe you couldn't beat Dwayne up."
    aletta.say "But he was the one that lost in the end."
    hide aletta
    show aletta kiss with fade
    $ aletta.flags.kiss += 1
    "Aletta underlines all of this by leaning in and kissing me on the lips."
    "I expect to feel the same pain as before, tensing for the moment it hits."
    "But the weird thing is that it never comes."
    "In fact, I can actually feel my muscles relaxing as Aletta kisses me."
    hide aletta kiss
    show aletta happy
    with fade
    "I guess that's something I should be thankful for!"
    "One of many things, in fact."
    $ aletta.love += 5
    $ hero.cancel_activity()
    $ game.pass_time(1)
    return

label aletta_event_10_alt_fired:
    if aletta.love.max < 200:
        $ aletta.love.max = 200
    scene expression f"bg {game.room}"
    "It's been a while since Dwayne walked in on Aletta and me in her office."
    "And the sting of being fired by the jerk hasn't faded yet."
    "But I'm doing the best I can to forget about it."
    "And I guess the task of finding a new job is helping with that too."
    "Taking a break from all that, I make an effort to catch up with Aletta."
    "Only realising when I do so that I don't actually know what happened to her at work."
    show aletta normal
    mike.say "I'm sorry I didn't ask this before, Aletta..."
    mike.say "But what happened to you at the office?"
    mike.say "Did Dwayne back off finally?"
    "Aletta seems to come alive as I ask my questions."
    "But I also note that she's shaking her head too."
    show aletta embarrassed
    aletta.say "Oh no, [hero.name]."
    aletta.say "After you stood up to him, he was a bigger asshole than ever!"
    "I can't help frowning at this news."
    "And I start shaking my head at Aletta."
    mike.say "Why didn't you tell me this before, Aletta?"
    mike.say "You should have reported him to HR."
    mike.say "Maybe even threatened to get the police involved."
    mike.say "Or at the very least, threaten to quit!"
    "Now Aletta's the one shaking her head."
    show aletta normal
    aletta.say "I did better than that."
    aletta.say "I really did quit."
    aletta.say "I told Dwayne where he could stick his lousy job!"
    "Suddenly I find myself backtracking on all I just said."
    "Like I'm worried that Aletta's put herself in a precarious position."
    mike.say "Whoa!"
    mike.say "Don't you think that's a little hasty?"
    mike.say "I mean, you had a pretty good thing going there, Aletta!"
    mike.say "Well...aside from the sexual harassment..."
    "Aletta holds up her hand and smiles at me."
    show aletta happy
    aletta.say "It's okay, [hero.name]."
    aletta.say "You don't think I got that job out of pity, did you?"
    show aletta normal
    aletta.say "And I certainly didn't get it by handing out favours to Dwayne either!"
    mike.say "Erm..."
    mike.say "What are you saying, Aletta?"
    mike.say "That you're happy to be unemployed?"
    show aletta happy
    "Aletta bursts into laughter and shakes her head again."
    "Like what I just said was the funniest thing she's ever heard."
    "Or maybe the most ridiculous..."
    aletta.say "Of course not!"
    show aletta normal
    aletta.say "What I mean is that I have a killer CV, [hero.name]!"
    aletta.say "Any company worth their salt would snap me up in an instant."
    aletta.say "But working for Dwayne had gotten me do beaten down I forgot that fact."
    mike.say "So you got a new job?"
    aletta.say "Damn right I did!"
    show aletta wink
    aletta.say "And a better one that I had before too."
    mike.say "So that's a...good thing?"
    aletta.say "It's a great thing."
    show aletta normal
    aletta.say "And it'd never have happened without you, [hero.name]."
    aletta.say "Now I have a great new job."
    aletta.say "I don't have to worry about Dwayne anymore."
    aletta.say "And I have space to think about what's important in my life."
    mike.say "That is great news, Aletta."
    show aletta flirt
    aletta.say "It's you, [hero.name]."
    mike.say "Huh?"
    mike.say "What's me?"
    aletta.say "You're what's important, you big dope!"
    hide aletta
    show aletta kiss with fade
    $ aletta.flags.kiss += 1
    "Aletta leans in and kisses me on the lips."
    "And actions really do speak louder than words."
    "Because I instantly know what she feels for me."
    "Thanks to the fact that I feel it in my body too."
    hide aletta kiss
    show aletta happy
    with fade
    "Once the kiss is over, Aletta looks me in the eye."
    aletta.say "Thank you..."
    aletta.say "For making me realise that I love you!"
    "It takes a moment for what Aletta just said to really sink in."
    "I have to stare at her and shake my head to understand the words."
    mike.say "Y...you're serious, Aletta?"
    mike.say "I mean...that's great!"
    mike.say "It's amazing - because I love you too!"
    $ aletta.love += 5
    $ game.pass_time(1)
    return

label aletta_chat_about_cherie:
    show aletta
    aletta.say "Hey, [hero.name], thanks for stopping in."
    mike.say "Sure, no problem."
    aletta.say "How'd your meeting with Cassidy's mom go?"
    mike.say "Step-mom."
    show aletta annoyed
    aletta.say "Whatever, don't care. How'd it go?"
    mike.say "It went okay, I guess?"
    show aletta normal
    aletta.say "That's it?"
    mike.say "Well, I didn't get anything from her, if that's what you mean."
    show aletta sad
    aletta.say "Oh. So it's a bust?"
    mike.say "No no, it's not a bust. She said she'll call me. I hope she meant it."
    aletta.say "And if she doesn't?"
    mike.say "Well, then it's a bust. But I think she'll call."
    aletta.say "Yeah, and I need to make other plans if she doesn't."
    mike.say "What do you mean?"
    aletta.say "None of your business."
    menu:
        "Insist":
            mike.say "Aletta, that sounds ominous."
            if aletta.love >= 100:
                "Aletta sighs."
                aletta.say "Look, [hero.name], I've been under Dwayne's...thumb for so long, I'd almost gotten used to it, and then this happened I got my hopes up, and now I can't bear this much longer."
                show aletta angry
                aletta.say "So if this doesn't work..."
                mike.say "Oh, I don't like the sound of that. Please don't do anything stupid."
                show aletta sad
                "Aletta shrugs."
                aletta.say "Then make this plan work, because it's all I have."
                mike.say "Okay."
            else:
                $ aletta.love += 5
                aletta.say "Don't worry about it, [hero.name]."
                mike.say "No, seriously."
                aletta.say "It's not your concern. I'll make sure whatever happens, you're protected."
                mike.say "Okay, I guess."
        "Let it go":
            pass
    show aletta normal
    aletta.say "Anyway, thanks for the update. Let me know if she calls?"
    mike.say "Sure."
    aletta.say "Thanks."
    return

label aletta_chat_about_cherie2:
    show aletta
    mike.say "Hey, Aletta. I just wanted to let you know that Cherie called back. I think we're a go."
    "Aletta visibly relaxes."
    mike.say "You okay?"
    aletta.say "Yeah. I just...I'm tired of feeling like a whore, you know? I've had about all I can handle."
    aletta.say "No, more than I can handle."
    mike.say "Yeah. This will be over soon, I promise."
    if aletta.love >= 140 and aletta.sexperience >= 1:
        aletta.say "[hero.name]?"
        mike.say "Yes?"
        aletta.say "Are you going to fuck her?"
        mike.say "Who? Cherie?"
        mike.say "I...I don't know. I might?"
        aletta.say "Do you want to?"
        menu:
            "Yes":
                mike.say "Yes. She's sexy, and...there's an appeal to taking something away from him."
                aletta.say "Is that what you're doing with me?"
                mike.say "No! I had no idea."
                aletta.say "Are you just collecting women?"
                mike.say "No!"
                aletta.say "Because me, Cassidy, obviously. Cherie too?"
                $ renpy.dynamic("count")
                $ count = 2
                if Person.is_not_hidden("shiori") and "shiori_office_bj" in DONE or shiori.sexperience > 1:
                    $ count += 1
                    aletta.say "And I know what you're doing with Shiori."
                if Person.is_not_hidden("audrey") and audrey.sexperience >= 2:
                    $ count += 1
                    aletta.say "And {b}everyone{/b} knows what you're doing with Audrey."
                if any(sasha.get_harems()):
                    $ count += 2
                    aletta.say "And I've heard rumors about the wild orgies you've had with that goth chick you hang out with."
                aletta.say "Seriously, [hero.name], how many women are there?"
                if count > 4:
                    mike.say "Uh. I guess...quite a lot."
                elif count > 2:
                    mike.say "It's...a few?"
                else:
                    mike.say "Only Cassidy."
                    aletta.say "And Cherie, who you admitted you want."
                aletta.say "[hero.name], I don't want to just be one of your trophies. Like Cherie or Cassidy."
                mike.say "I see."
                aletta.say "Will you dump them all for me, when I'm free of Dwayne?"
                mike.say "What?"
                aletta.say "Look, I'll give you a free pass for anything you've done while I've been stuck as his bitch."
                aletta.say "But when I'm free, do we have something?"
                mike.say "Of course we have something."
                aletta.say "Enough for you to dump the rest of your little harem?"
                if count == 2:
                    mike.say "It's just Cassidy, really."
                    aletta.say "Fine. Will you dump her?"
                else:
                    mike.say "That's an awful lot of women to hurt."
                    aletta.say "So that's a no, then?"
                menu:
                    "I will leave them for you":
                        mike.say "Yes, Aletta. I want you. I will leave them for you."
                        $ aletta.flags.saidwoulddump = True
                        aletta.say "Really? You'd better not be lying to me."
                        mike.say "Cross my heart!"
                    "I can't do that to them":
                        mike.say "I can't do that to them, Aletta. I'm sorry."
                        aletta.say "Fine. So that's it for us then?"
                        menu:
                            "I guess so":
                                mike.say "I guess it is. Look, I never meant to hurt you. Or anyone."
                                $ aletta.breakup()
                                aletta.say "I understand. I just. I think I need to be alone now."
                                mike.say "Yeah, I--"
                                show aletta angry
                                aletta.say "Get out."
                                $ game.room = "office"
                                return
                            "No":

                                mike.say "No, I don't see why it has to be it."
                                $ aletta.love -= 20
                                aletta.say "Well, I already said I won't share, and you said you won't leave them. What else is there?"
                                mike.say "Aletta, you're not thinking clearly right now. You're under a lot of stress with Dwayne. I get it."
                                mike.say "But listen to me. Let's talk about all of this again when this is all over, okay?"
                                aletta.say "I don't know."
                                mike.say "Just be patient. Please?"
                                aletta.say "I'll try."
            "No":
                $ aletta.flags.saidnocherie = True
                $ aletta.love += 5
                mike.say "No, I don't really want to."
                aletta.say "I guess that's something."
                mike.say "But...we're all doing things we don't really want to right now, aren't we?"
                aletta.say "Yeah, but are we enjoying them?"
                mike.say "Oh come on, it has to be a little bit pleasant? Or at least, it was?"
                aletta.say "Well. He does have the biggest...I mean."
                show aletta blush
                aletta.say "Fine."
                show aletta normal
                aletta.say "But that was a long time ago. Now not having my freedom sucks."
                mike.say "We'll fix it. I promise."
                aletta.say "Promises, promises. What are the promises of a man worth?"
                mike.say "I think that's my cue to leave..."
    return

label aletta_male_ending:
    $ game.hour = 16




    if renpy.has_label("aletta_achievement_3") and not game.flags.cheat:
        call aletta_achievement_3 from _call_aletta_achievement_3
    $ game.room = "church"
    scene bg church wedding
    with fade
    "So, here I am, standing around waiting for Aletta to arrive, feeling nervous and on show."
    "The irony is that this isn't the first time that she's had me in a position like this."
    "Most of the times that I was going into a meeting with her or we had a one-to-one."
    "On those occasions I almost always felt like this too."
    "But back then we were just colleagues - and now we're about to tie the knot!"
    "I guess I'm never going to totally get over it, no matter how much I love her."
    "Aletta's just one of those girls that has an aura about her."
    "She doesn't suffer fools gladly, and I hope that she's not marrying one today!"
    "Which is another reason why I need to get a handle on my nerves."
    "If I keep looking back over my shoulder the whole time, I'm going to look like a crazy man!"
    "I'm actually beginning to think that Aletta's deliberately keeping me waiting."
    "But then I hear the first swellings of the music she chose to come down the aisle to."
    "I can't help letting out a sigh of relief that's much louder than I intended."
    "In fact, it's so loud that it causes the priest to cough and attract my attention."
    "Tearing my eyes away from the doors of the chapel, I look in his direction."
    "He doesn't say a word, just gives me a reassuring smile."
    "And oddly it seems to help, making me nod in thanks."
    "Then it's his turn to glance over my shoulder, and I follow his gaze."
    "There she is, walking down the aisle towards me."
    show aletta wedding normal noglasses at center, zoomAt( 0.9, (640, 740))
    "Of course Aletta looks stunning - how could she not?"
    "The dress is perfect, but it's only accentuating what's already there."
    "And Aletta sweeps down the aisle with all the dignity of a queen!"
    "All eyes are on her, and she looks like she know it too."
    "In fact, she looks like she'd resent anyone failing to look at her right now!"
    if aletta.is_visibly_pregnant:
        "The cut of the dress accommodates Aletta's swelling belly."
        "And somehow it just serves to make her look that much more impressive."
        "Her hands are clutched before it, holding her bouquet."
        show aletta at center, traveling (1.5, 3.0, (640, 1060))
        "But as she comes closer, I can see that they're shaking a little."
    else:
        "She clutches the bouquet in her hands like a queens orb and sceptre."
        show aletta at center, traveling (1.5, 3.0, (640, 1060))
        "But as she comes closer, I can see that her hands are shaking a little."
    "I lean in to whisper to Aletta as she comes to a halt at my side."
    mike.say "Hey, Aletta."
    mike.say "I don't need to point this out."
    mike.say "But you look amazing."
    show aletta blush
    "Her confident demeanour slips for a moment, and I can see what's going on underneath."
    "Aletta's every bit as nervous as I am, it's just that she's far better at covering it up."
    "But the smile on her face is genuine as she nods to acknowledge my compliment."
    show aletta happy
    aletta.say "Not looking too shabby yourself, [hero.name]."
    aletta.say "I think you'll do for me!"
    show wedding aletta with fade
    "I can't help grinning like a fool as I see Aletta's mood improve."
    "It means so much to me that I can see beneath the front she projects for everyone else."
    "And it means even more to know that I can touch the real Aletta that lies beneath it too."
    show wedding aletta priest with dissolve
    "Priest" "Ahem..."
    "Priest" "Shall we begin?"
    "Aletta and I turn to face the priest, nodding at the same time."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today to witness the union of these two souls..."
    "I must have gone through the ceremony a hundred times in my mind - more even."
    "But still it all seems to rush past me in a flurry of successive moments."
    "I'm sure that if I see a video of the whole thing later, I won't remember a thing!"
    "Priest" "Do you, [hero.name], take Aletta to be your lawful, wedded wife?"
    "It's this one question that snaps me back to reality."
    "I realise that all attention is now on me."
    mike.say "I...I do!"
    "Priest" "And do you, Aletta, take [hero.name] to be your lawful, wedded husband?"
    aletta.say "I do."
    "Priest" "Then I call upon those present..."
    "Priest" "If they know of any reason these two may not be joined in wedlock..."
    "Priest" "To speak now, or forever hold their peace!"
    "Aletta and I share a fleeting glance."
    "And then we both look back at the chapel doors."
    "For a moment I honestly expect to see Dwayne burst in, somehow back from the dead."
    "Or more likely, Detective Michaels brandishing a warrant for Aletta's arrest."
    "But as the seconds stretch by, it becomes apparent that nothing of the kind is going to happen."
    "Priest" "Very well - it gives me great pleasure to declare you husband and wife."
    "Priest" "You may kiss the bride!"
    show wedding aletta -priest with dissolve
    "Neither of us needs to be told to do that."
    scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
    show aletta kiss wedding
    with fade
    $ aletta.flags.kiss += 1
    "Aletta places her lips against mine, and the kiss that follows is glorious."
    "I can feel in it the release of all the passion that exists between us."
    "That and the relief that we managed to get here, overcoming all the obstacles in our way."
    "It'll have to come to an end soon enough."
    "But until then, I can't think of nothing else at all..."
    if aletta.is_visibly_pregnant and (aletta.sub >= 25 or aletta.sub <= -25):
        scene bg black
        if aletta.sub >= 25:
            show aletta ending aletta
        else:
            show aletta ending mike
        with fade
        aletta.say "Hmm...I'm not exactly pleased that it's taken this long for me to be able to speak for myself!"
        aletta.say "I'm a modern woman that's got a lot to say, and I don't need someone like [hero.name] to say it for me!"
        aletta.say "But...I have to admit that I DO love him - even if he can be a typical man at times!"
        aletta.say "He's like that though, he gets under your skin before you even know it's happening."
        aletta.say "And by then it's already too late - you're starting to fall for his charms without knowing it."
        aletta.say "But his goofy sense of humour...now there's something I'll never get used to!"
        aletta.say "It was bad enough when we were just working together and he was cracking jokes."
        aletta.say "So think how bad it is now that we're married and raising a family together!"
        aletta.say "Wow...sorry...it just sounds so strange to be saying all of that!"
        aletta.say "I was so career-minded when I first met [hero.name], that's all."
        aletta.say "The last thing I was thinking of was starting a serious relationship."
        aletta.say "Never mind getting pregnant and marrying someone!"
        aletta.say "But that's another thing that he's pretty good at doing, you know?"
        aletta.say "[hero.name] seems to be able to change where I thought I was going."
        aletta.say "And the craziest thing is that, now it's happened, I like the way my life's turning out."
        aletta.say "Maybe the problem in the past was that I always tried to be in total control of everything."
        aletta.say "And when he made things a bit more crazy, [hero.name] taught me to enjoy the chaos."
        aletta.say "Whatever the reason, I'm happier now than I can ever remember being before he came along."
        if aletta.sub >= 25:
            aletta.say "Sure, I was angry at first."
            aletta.say "There was no way I wanted to give up my career to become a housewife."
            aletta.say "But I think I was also hiding the fact that I was scared of being a mother."
            aletta.say "I mean...how was I supposed to know what to do with a baby?!?"
            aletta.say "They don't do as they're told and there's no contract between you and them!"
            aletta.say "It was the first time in my life that I felt like I wouldn't be able to cope."
            aletta.say "But that was where [hero.name] came in."
            aletta.say "He was always there to support me as Britney came into our lives."
            aletta.say "Sometimes that meant taking time off work to be there physically."
            aletta.say "But almost as often it was no more than being on the end of the phone."
            aletta.say "I found that a few words from him were more than enough to get me through."
            aletta.say "Just knowing that he believed in me and would be back home as soon as he was able."
            aletta.say "And I think I turned out to be a pretty good mother too."
            aletta.say "I mean, Britney seems to feel that way."
            aletta.say "And [hero.name] does too!"
            aletta.say "So maybe motherhood is a career that suits me!"
        else:
            aletta.say "Sure, I didn't think he could pull it off at first."
            aletta.say "But he talked me around into letting him stay at home while I went back to the office."
            aletta.say "Of course I was grateful to be able to keep my career and still be a mother."
            aletta.say "Yet part of me was sure that [hero.name] would come to resent me for it."
            aletta.say "That or the fact he was bonding with Britney while I was away would make her forget about me."
            aletta.say "But he soon proved me wrong on both counts."
            aletta.say "[hero.name] really seems to love being the one to stay home with our daughter."
            aletta.say "And he makes sure that they video-call me at least once a day at the office."
            aletta.say "Somehow he always manages to make me getting home like a special occasion."
            aletta.say "Both of them greeting me as soon as I walk in through the door."
            aletta.say "And [hero.name] seems proud of the fact his wife is climbing the corporate ladder."
            aletta.say "And so long as I know that I have the both of them backing me up..."
            aletta.say "Well, I feel like there's nothing life can throw at me I can't handle!"
        aletta.say "Don't hear all of that and think that my life is one hundred percent perfect though."
        aletta.say "[hero.name]'s still the same old goofball that he was when we just worked together."
        aletta.say "And I don't think that's something that will ever change."
        aletta.say "Or at least it's something that's going to take longer to iron out."
        aletta.say "Not that it worries me, because I feel we've got a lifetime together."
        aletta.say "And that means plenty of time to sort him out!"
    else:
        scene office ending
        show office ending aletta work
        with fade
        aletta.say "I suppose it makes sense for me to be the one that sits down and sums up the story so far."
        aletta.say "[hero.name]'s sweet, and he means well - but he can be unreliable, even at the best of times."
        aletta.say "I mean, the whole of this thing might have been more accurate and efficient with me doing the talking."
        aletta.say "And you could have skipped over all of the boring parts where I wasn't involved as well!"
        aletta.say "What?"
        aletta.say "Oh, I see - you want me to get to the point."
        aletta.say "Sorry, I have a tendency to get distracted these days."
        aletta.say "I honestly think that it's [hero.name] starting to rub off on me..."
        aletta.say "No, I never thought of him as potential marriage material, not when we first met."
        aletta.say "And to be honest, I was more interested in my career and climbing the corporate ladder."
        aletta.say "I honestly thought that a relationship would be a burden and hold me back."
        aletta.say "Plus there was the fact that [hero.name] didn't come across as alpha-male material!"
        aletta.say "Oh..."
        aletta.say "You know all about the affair that I was having with Dwayne at the time we met?"
        aletta.say "Okay, okay - I take back some of the things I said about having a relationship."
        aletta.say "But the thing between Dwayne and myself..."
        aletta.say "It was more of an arrangement than a real relationship."
        aletta.say "I had something that he wanted, and he could offer me advancement."
        aletta.say "And I told myself that the way he treated me didn't matter - so long as it got me promoted."
        aletta.say "I...I suppose that's where [hero.name] was different."
        aletta.say "He couldn't promote me or head-hunt me for a new position."
        aletta.say "He just seemed to be interested in me for my own sake."
        aletta.say "I'm not proud of this, okay?"
        aletta.say "But that's why I gave him such a hard time to begin with."
        aletta.say "I thought that he was a dumb asshole with no drive or ambition."
        aletta.say "I couldn't see him for anything but his usefulness to my career."
        aletta.say "It was only when I started to compare the way he treated me to the way Dwayne did..."
        aletta.say "Well, it didn't take me long to know that I'd made a mistake."
        aletta.say "[hero.name] showed me what it felt like to be loved for who I am."
        aletta.say "And he helped me to realise that I'd been letting Dwayne abuse me."
        aletta.say "If it weren't for him, I'd never have had the courage to put an end to it."
        aletta.say "I'd never have had the motivation to pull the trigger on Dwayne."
        aletta.say "And that's because I knew that there was something waiting for me after he was gone."
        aletta.say "We've never looked back since that unpleasant business either."
        aletta.say "And it seems like I was wrong - [hero.name] was good for my career after all!"
        aletta.say "With me in his life, he found a focus and with that his true potential."
        aletta.say "He's unstoppable in the boardroom and the bedroom."
        aletta.say "Believe me - I know from first-hand experience!"
        aletta.say "And with him at my side, I found that I could do almost anything."
        aletta.say "Knowing that he's there for me, that he's got my back..."
        aletta.say "It's the best motivation that I've ever had!"
        aletta.say "We just moved into a penthouse apartment."
        aletta.say "We have a stock portfolio to die for."
        aletta.say "And we're even talking about ditching our old jobs and starting a company all of our own."
        aletta.say "I have no idea what that company will be, but that's not something that worries me."
        aletta.say "Together, [hero.name] and I can do anything!"

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not aletta.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3
    scene bg black with dissolve
    pause 1.0
    $ game.set_new_game_plus()
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
