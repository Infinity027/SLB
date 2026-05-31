init python:
    Event(**{
    "name": "sasha_female_event_02_notify",
    "label": "sasha_female_event_02_notify",
    "priority": 500,
    "do_once": False,
    "quit": False,
    "conditions": [
        IsNotDone("sasha_female_event_02"),
        IsHour(9, 0),
        HeroTarget(
            IsGender("female"),
            IsRoom("livingroom", "kitchen", "bathroom", "bedroom1")),
        PersonTarget(sasha,
            Not(IsHidden()),
            IsRoom("bedroom3"),
            Not(IsActivity("sleep")),
            Not(HasCheated()),
            IsDone("female_intro"),
            MinStat("love", 30),
            ),
        ],
    })

    Event(**{
    "name": "sasha_female_event_02",
    "label": "sasha_female_event_02",
    "duration": 1,
    "priority": 500,
    "do_once": True,
    "music": "music/roa_music/smile_for_me.ogg",
    "conditions": [
        IsHour(9, 0),
        HeroTarget(
            IsGender("female"),
            IsRoom("secondfloor", "bedroom3")),
        PersonTarget(sasha,
            Not(IsHidden()),
            IsRoom("bedroom3"),
            Not(IsActivity("sleep")),
            Not(HasCheated()),
            IsDone("female_intro"),
            MinStat("love", 30),
            ),
        ],
    })

    InteractEvent(**{
    "name": "sasha_female_event_03",  
    "label": "sasha_female_event_03",
    "priority": 500,
    "music": "music/roa_music/smile_for_me.ogg",
    "duration": 0,
    "conditions": [
        IsDone("sasha_female_event_02"),
        HeroTarget(
            IsGender("female"),
            IsRoom("mall1"),
            IsFlag("sasha_delay_female", False),
            ),
        PersonTarget(sasha,
            HasRoomTag("mall_southside"),
            Not(IsHidden()),
            Not(HasCheated()),
            MinStat("love", 40),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "sasha_female_event_04",  
    "label": "sasha_female_event_04",
    "duration": 1,
    "priority": 500,
    "music": "music/roa_music/smile_for_me.ogg",
    "conditions": [
        IsDone("sasha_female_event_03"),
        HeroTarget(
            IsGender("female"),
            HasRoomTag("pub"),
            IsFlag("sasha_delay_female", False),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(HasCheated()),
            MinStat("love", 60),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "sasha_female_event_05",  
    "label": "sasha_female_event_05",
    "duration": 1,
    "priority": 500,
    "music": "music/roa_music/smile_for_me.ogg",
    "conditions": [
        IsDone("sasha_female_event_04"),
        Not(IsDone("sasha_female_event_05b")),
        IsSeason(0, 1),
        HeroTarget(
            IsGender("female"),
            IsRoom("kitchen"),
            IsFlag("sasha_delay_female", False),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(HasCheated()),
            MinStat("love", 100),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "sasha_female_event_05b", 
    "label": "sasha_female_event_05b",
    "duration": 1,
    "priority": 500,
    "music": "music/roa_music/smile_for_me.ogg",
    "conditions": [
        IsDone("sasha_female_event_04"),
        Not(IsDone("sasha_female_event_05")),
        IsSeason(2, 3),
        HeroTarget(
            IsGender("female"),
            IsRoom("date_mall1"),
            IsFlag("sasha_delay_female", False),
            ),
        PersonTarget(sasha,
            OnDate(),
            MinStat("love", 100),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "sasha_female_event_sex_talk_05",
    "label": "sasha_female_event_sex_talk_05",
    "duration": 1,
    "priority": 500,
    "music": "music/roa_music/smile_for_me.ogg",
    "conditions": [
        Or(
            IsDone("sasha_female_event_05"),
            IsDone("sasha_female_event_05b")
          ),
        Not(IsDone("sasha_female_event_06")),
        HeroTarget(
            IsGender("female"),
            Not(OnDate()),
            IsFlag("sasha_delay_female", False),
            ),
        PersonTarget(sasha,
            IsActive(),
            MinStat("love", 120),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "sasha_female_event_06",  
    "label": "sasha_female_event_06",
    "duration": 1,
    "priority": 500,
    "music": "music/roa_music/smile_for_me.ogg",
    "conditions": [
        IsDone("sasha_female_event_sex_talk_05"),
        IsHour(7, 10),
        HeroTarget(
            IsGender("female"),
            IsRoom("kitchen"),
            IsFlag("sasha_delay_female", False),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(HasCheated()),
            MinStat("love", 140),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "sasha_female_event_07",  
    "label": "sasha_female_event_07",
    "duration": 3,
    "priority": 500,
    "music": "music/roa_music/smile_for_me.ogg",
    "conditions": [
        IsDone("sasha_female_event_06"),
        IsHour(19, 0),
        HeroTarget(HasRoomTag("home"),
            IsFlag("sasha_delay_female", False),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            Not(HasCheated()),
            MinStat("love", 140),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "sasha_female_event_08",  
    "label": "sasha_female_event_08",
    "duration": 3,
    "priority": 500,
    "music": "music/roa_music/smile_for_me.ogg",
    "conditions": [
        IsDone("sasha_female_event_07"),
        HeroTarget(
            IsFlag("sasha_delay_female", False),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(HasCheated()),
            Not(IsActivity("sleep")),
            MinStat("love", 180),
            MinFlag("kiss", 1),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "sasha_female_beach_date_event_01",
    "label": "sasha_female_beach_date_event_01",
    "priority": 500,
    "music": "music/roa_music/smile_for_me.ogg",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsRoom("date_beach", "date_nudistbeach"),
            ),
        PersonTarget(sasha,
            OnDate(),
            ),
        ],
    "do_once": True,
    })

    Activity(**{
    "name": "sasha_clothesshop_coworker_01",
    "label": "sasha_clothesshop_coworker_01",
    "money_gain": {"attributes": ["charm"]},
    "duration": 4,
    "priority": 500,
    "rooms": "clothesshop",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_day", "clothesshop"),
            MinFlag("worked_clothesshop", 3),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    "do_once": True
    })

    Activity(**{
    "name": "sasha_clothesshop_coworker_02",
    "label": "sasha_clothesshop_coworker_02",
    "money_gain": {"attributes": ["charm"]},
    "duration": 4,
    "priority": 500,
    "rooms": "clothesshop",
    "conditions": [
        IsDone("sasha_clothesshop_coworker_01"),
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_day", "clothesshop"),
            MinFlag("worked_clothesshop", 6),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    "do_once": True
    })

    Activity(**{
    "name": "sasha_clothesshop_coworker_03",
    "label": "sasha_clothesshop_coworker_03",
    "money_gain": {"attributes": ["charm"]},
    "duration": 4,
    "priority": 500,
    "rooms": "clothesshop",
    "conditions": [
        IsDone("sasha_clothesshop_coworker_02"),
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_day", "clothesshop"),
            MinFlag("worked_clothesshop", 9),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    "do_once": True
    })

    Activity(**{
    "name": "sasha_clothesshop_friend_01",
    "label": "sasha_clothesshop_friend_01",
    "money_gain": {"attributes": ["charm"]},
    "duration": 4,
    "priority": 500,
    "rooms": "clothesshop",
    "conditions": [
        IsDone("sasha_clothesshop_coworker_03"),
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_day", "clothesshop"),
            MinFlag("worked_clothesshop", 12),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    "do_once": True
    })

    Activity(**{
    "name": "sasha_clothesshop_friend_02",
    "label": "sasha_clothesshop_friend_02",
    "money_gain": {"attributes": ["charm"]},
    "duration": 4,
    "priority": 500,
    "rooms": "clothesshop",
    "conditions": [
        IsDone("sasha_clothesshop_friend_01"),
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_day", "clothesshop"),
            MinFlag("worked_clothesshop", 15),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    "do_once": True
    })

    Activity(**{
    "name": "sasha_clothesshop_friend_03",
    "label": "sasha_clothesshop_friend_03",
    "money_gain": {"attributes": ["charm"]},
    "duration": 4,
    "priority": 500,
    "rooms": "clothesshop",
    "conditions": [
        IsDone("sasha_clothesshop_friend_02"),
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_day", "clothesshop"),
            MinFlag("worked_clothesshop", 18),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    "do_once": True
    })

    Activity(**{
    "name": "sasha_clothesshop_friend_04",
    "label": "sasha_clothesshop_friend_04",
    "money_gain": {"attributes": ["charm"]},
    "duration": 4,
    "priority": 500,
    "rooms": "clothesshop",
    "conditions": [
        IsDone("sasha_clothesshop_friend_03"),
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_day", "clothesshop"),
            MinFlag("worked_clothesshop", 21),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    "do_once": True
    })

    Activity(**{
    "name": "sasha_clothesshop_lover_01",
    "label": "sasha_clothesshop_lover_01",
    "money_gain": {"attributes": ["charm"]},
    "duration": 4,
    "priority": 500,
    "rooms": "clothesshop",
    "conditions": [
        IsDone("sasha_clothesshop_friend_04"),
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_day", "clothesshop"),
            MinFlag("worked_clothesshop", 24),
            ),
        PersonTarget(sasha,
            MinStat("love", 160),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    "do_once": True
    })

    Activity(**{
    "name": "sasha_clothesshop_lover_02",
    "label": "sasha_clothesshop_lover_02",
    "money_gain": {"attributes": ["charm"]},
    "duration": 4,
    "priority": 500,
    "rooms": "clothesshop",
    "conditions": [
        IsDone("sasha_clothesshop_lover_01"),
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_day", "clothesshop"),
            MinFlag("worked_clothesshop", 27),
            ),
        PersonTarget(sasha,
            MinStat("love", 160),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    "do_once": True
    })

    Activity(**{
    "name": "sasha_clothesshop_lover_03",
    "label": "sasha_clothesshop_lover_03",
    "money_gain": {"attributes": ["charm"]},
    "duration": 4,
    "priority": 500,
    "rooms": "clothesshop",
    "conditions": [
        IsDone("sasha_clothesshop_lover_02"),
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("job_day", "clothesshop"),
            MinFlag("worked_clothesshop", 30),
            ),
        PersonTarget(sasha,
            MinStat("love", 160),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    "do_once": True
    })

label sasha_female_event_02_notify:
    $ renpy.say("", randchoice(["I hear banging from the hallway. Maybe I should see what's going on?", "I hear a loud thump from the hallway.", "I can distantly hear the sound of swearing. I think it's coming from the hallway."]))
    return

label sasha_female_event_02:
    if sasha.love.max < 40:
        $ sasha.love.max = 40
    show bg secondfloor with fade
    "I hear Sasha cursing in her bedroom..."
    "I walk down the hallway and peer into her room; she's managed to muscle a dresser and a bookshelf into the room by herself, but the U-haul is still outside with her bed and a little more furniture in it."
    scene bg bedroom3
    show sasha annoyed
    with fade
    "Several boxes lay on the floor, a few with books and clothing tumbled out of them; they must have been stacked and fallen over."
    "Sasha looks frustrated enough to throw something."
    menu:
        "Tell her to keep it quiet":
            bree.say "Hey, I get that this is frustrating, but can you try to keep it down?"
            play sound door_slam
            pause 0.4
            scene bg door bedroom3 at center, zoomAt(1.25, (640, 880))
            with hpunch
            "She slams the door shut after glaring at me."
            $ sasha.love -= 5
            return
        "Offer to help":
            show sasha normal
            bree.say "Hey, looks like you've got a lot going on here; need some help with unpacking?"
            $ sasha.love += 2
            show sasha shout
            sasha.say "A second pair of arms would be perfect."
            show sasha normal
            menu:
                "Accept" if hero.energy > 2:
                    bree.say "Sure, let's get these boxes out of the way and we'll get started!"
                    $ sasha.love += 2
                "Refuse":
                    bree.say "Sorry, I don't have time right now."
                    $ sasha.love -= 2
                    return
    scene bg bedroom3
    show sasha shout
    sasha.say "You wanna help me get these boxes empty?"
    sasha.say "I'll be able to sort everything out and get stuff where it belongs way easier if I can just see everything."
    show sasha normal
    menu:
        "Refuse":
            bree.say "Sorry, I don't have time tonight."
            "I've got to get a good night of sleep."
            $ sasha.love -= 1
            return
        "Accept" if hero.energy > 5:
            bree.say "Sure, let me get the box cutter."
            $ sasha.love += 1
    "I help her get her bed and the furniture placed just where she wants them and then get started opening up the slew of boxes she's got scattered through the room."
    "Sasha has a lot of books!"
    "All sorts of topics, with a lot of fantasy and science fiction."
    "Plenty of music too; her CD tower is going to be full before they're all unpacked."
    "She's got a nice stereo set up on the big book shelf, and I prepare myself to deal with some loud music now and then."
    scene unpack sasha with fade
    "I sit on the edge of the bed and slit the flaps open on a smallish box, then open it up and blink in surprise."
    "It's full of toys, and not the kind kids play with!"
    show unpack sasha down surprised
    bree.say "Wow."
    "I murmur softly before I can stop myself."
    "Sasha turns and looks at me with a brow raised, then grins as she sees the box I've opened."
    "She shows no shame at all, no shyness or embarrassment; this woman is confident!"
    sasha.say "What, you've never seen sex toys before?"
    menu:
        "No":
            bree.say "Well... no."
            "I say a little defensively, suddenly feeling shy under her frank gaze."
            $ sasha.love += 1
            show unpack sasha up blush
            sasha.say "Aww."
            "Sasha coos with a little smile."
            sasha.say "Well, take a good look and get an education!"
            show unpack sasha smile normal
            menu:
                "Don't look at the toys":
                    bree.say "No, it seems sort of private to me. I'll leave it on your nightstand."
                    $ sasha.love -= 1
                    $ HIDE_UI = True
                    scene bg black with dissolve
                    pause 0.1
                    scene bg bedroom3
                    show sasha
                    with dissolve
                    $ HIDE_UI = False
                    "Job done, I tuck the box-cutter back in my pocket."
                    bree.say "That's the last of them!"
                    menu:
                        "Offer more help" if hero.energy > 7:
                            bree.say "Do you need any more help?"
                            "Sasha shakes her head."
                            show sasha shout
                            sasha.say "You already have been more help than most of my friends."
                            $ sasha.love += 1
                        "Stop helping":
                            bree.say "That's it for me. Good luck with your unpacking!"
                    show sasha shout
                    sasha.say "Thanks for the help. Catch you later."
                    show sasha normal
                    "She then moves to the next box of stuff."
                    return
                "Look at the toys":
                    pass
                "Joke" if hero.charm >= 10:
                    bree.say "Planning on a demonstration?"
                    "I ask with a snicker. Sasha laughs and wags her finger mock-scoldingly at me, then goes back to putting her books on the shelf."
                    $ sasha.love += 1
            show unpack sasha search
            "I start sorting through the box."
            "Which has several dildos of various sizes --including one that sort of astounds me--."
            show unpack sasha dildo shown
            "A few of which have control knobs for vibration."
            show unpack sasha vibrator shown
            "A box of ribbed condoms is in here as well, along with what looks like a leather thong!"
            show unpack sasha search
            "I pull the thong out and realize what it is by the circular opening at the front; a strap on!"
            show unpack sasha
            bree.say "So, you're into girls?"
            "Sasha smirks at me."
            show unpack sasha evil
            sasha.say "And boys. Never know what you'll like until you try it!"
            menu:
                "Be surprised" if hero.charm < 10:
                    show unpack sasha up surprised
                    bree.say "You use this on guys?"
                    sasha.say "You would not believe how many macho looking guys gets off being pegged by a sexy lady."
                "Be surprised" if hero.charm >= 15:
                    show unpack sasha up smile
                    bree.say "You use this on guys?"
                    "Sasha smiles a little and shrugs."
                    show unpack sasha normal
                    sasha.say "Sure. Some guys really love it. Especially the submissive ones. And I like being in control."
                    "She adds with a grin."
                    sasha.say "Go ahead and leave the box on the nightstand."
                    $ sasha.love += 1
                "Be interested":
                    show unpack sasha
                    bree.say "Wow.. that.. seems kinda hot."
                    "Sasha grins wickedly at me."
                    show unpack sasha evil
                    sasha.say "Oh, believe me, it's hot. Go ahead and leave the box on the nightstand."
                    $ sasha.love += 2
        "Yes":
            show unpack sasha up smile normal
            bree.say "Sure I've seen sex toys before, but not this many unless I was in a sex shop!"
            "I grin at her, making sure my tone is teasing so she won't get offended."
            show unpack sasha evil
            sasha.say "Spend much time in sex shops, do you?"
            show unpack sasha blush
            "She smirks at me."
            menu:
                "Yes":
                    bree.say "Hey, everybody needs a little spice in the bedroom, right?"
                    "Sasha grins."
                    show unpack sasha evil
                    sasha.say "Absolutely. The spicier, the better! Go ahead and put that on the nightstand; I'll unpack it later."
                    $ sasha.love += 2
                "No":
                    bree.say "No I was always too shy..."
                    "Sasha grins."
                    show unpack sasha evil
                    sasha.say "Don't know what you're missing. Go ahead and put that on the nightstand; I'll unpack it later."
    scene bg bedroom3 with fade
    "The Naughty Box set aside on the nightstand, I open up the rest of the boxes so she can see what stuff she's got where."
    "Job done, I tuck the box-cutter back in my pocket."
    show sasha with dissolve
    bree.say "That's the last of them!"
    menu:
        "Offer more help" if hero.energy > 7:
            bree.say "Do you need any more help?"
            "Sasha shakes her head."
            show sasha happy
            sasha.say "You already have been more help than most of my friends."
            $ sasha.love += 1
        "Stop helping":
            bree.say "That's it for me. Good luck with your unpacking!"
    show sasha happy
    sasha.say "Thanks for the help. Catch you later."
    show sasha normal
    "She then moves to the next box of stuff."
    return

label sasha_female_event_03:
    if sasha.love.max < 60:
        $ sasha.love.max = 60
    show sasha normal
    bree.say "Hey Sasha, what's up?"
    show sasha shout
    sasha.say "I'm craving something sweet. You wanna go check out this new ice cream place at the mall?"
    show sasha normal
    menu:
        "ICE CREAM!":
            scene bg black with timelaps
            scene bg mall1
            show sasha normal at center, zoomAt(1.5, (640, 1040))
            with timelaps
            bree.say "Yeah! Ice cream!!"
            bree.say "Oh, you got a cup? No cone?"
            show sasha shout
            sasha.say "Yeah I don't really like the cones so I always get a cup."
            show sasha normal
            bree.say "I guess that makes sense. I just love the crunch so much! So, what flavor did you get? I bet it's nothing as delicious as mine."
            show sasha shout
            sasha.say "Oh really? And what flavor is that?"
            show sasha normal
            "I giggle to myself triumphantly."
            bree.say "Mint chocolate chip, the absolute best flavor in the entire universe!"
            show sasha sadsmile
            "Sasha gives me a look of pity."
            bree.say "What?! What did YOU get that's so special?"
            show sasha joke
            "Sasha's mouth twists into a wry grin. I immediately feel insecure."
            show sasha happy
            sasha.say "Oh nothing, just a significantly more sophisticated flavor. You know, for adults. I got orange custard chocolate chip."
            show sasha normal
            bree.say "...What? You got what?"
            "Sasha repeats herself, with a chuckle."
            bree.say "What the actual fuck is that flavor? That sounds awful...what?!"
            "I wonder about Sasha's sanity."
            show sasha shout
            sasha.say "It's really good. Have you ever had one of those chocolate oranges that come in the foil and you break them apart?"
            show sasha normal
            "I nod, suddenly very excited about the concept of the flavors being described to me."
            bree.say "I love those things actually!"
            show sasha shout
            sasha.say "Yeah well it's like that but as ice cream."
            show sasha normal
            "As we begin walking around the mall, I fall silent to focus on eating my cone that's trying to drip all over me."
            show sasha happy
            "My eyes are darting all around at the busy shops and I steal glances here and there at Sasha's cup..."
            "She really looks like she's enjoying herself and it only makes me more curious."
            "..."
            "With my mouth still a bit full, I venture a brave question."
            bree.say "...Can I try it though?"
            show sasha shout
            sasha.say "What?"
            show sasha normal
            bree.say "Your ice cream. Can I have a bite?"
            show sasha shout
            sasha.say "Well I mean I have only one spoon."
            show sasha normal
            bree.say "Oh...I have only this cone...but I'm not a germophobe...unless you are."
            show sasha shout
            sasha.say "Not really."
            show sasha normal
            bree.say "So it sounds like you'll give me some, right?"
            show sasha happy at startle
            "Sasha laughs quietly to herself."
            show sasha joke
            sasha.say "Damn you're persistent."
            show sasha normal
            bree.say "I'm the kind of woman who knows what she wants and when she wants it."
            show sasha joke
            sasha.say "Oh? And what do you want again?"
            show sasha normal
            bree.say "Are you making me beg for ice cream, is that what you're doing right now?"
            "I pout and say in an exaggerated, cartoony voice--"
            bree.say "Feed me, Sasha!"
            show sasha shout
            sasha.say "Okay okay I get it. Open up."
            show sasha normal
            "Oh. Wow, I actually didn't expect her to FEED me. I was just being silly. But okay, I can dig it!"
            bree.say "Aaaahn~!"
            "The cold hits my tongue, and the cream melts in my mouth, spreading the beautiful taste of orange dreamsicle and leaving pieces of chocolate for me to enjoy as a well-planned afterword. It did indeed taste exactly like a chocolate orange."
            bree.say "That's delicious. I can see why it's your favorite. It might be mine now too!"
            show sasha happy
            sasha.say "What can I say, I have good taste...even if it's a little off the beaten path."
            show sasha normal
            bree.say "You're supposed to march to the beat of your own drum anyway."
            show sasha shout
            sasha.say "In my case, I groove to the beat of my own strum...since I'm not the drummer in the Deathless Harpies."
            show sasha normal
            "I laugh, a little louder than I meant to which draws the attention of passersby."
            show sasha shout
            sasha.say "Was that really funny for you?"
            show sasha normal
            bree.say "Yeah haha, I'm sorry I didn't mean to cause a scene. I've just never heard it before and it caught me off guard. But yeah. Beat of your own strum, we can use that."
            "I spot the arcade coming up. It's my time to shine!"
            bree.say "Hey! See the arcade? Wanna go? Please please pleaseeeee?"
            "I sound like a kid begging her mom for something instead of a grown woman who can make her own decisions...but I don't care."
            show sasha shout
            sasha.say "Hmm...okay sure but depending on the game I might just watch."
            scene bg arcade
            show sasha normal
            with fade
            bree.say "I'll pick something two player, how's that sound?"
            "Sasha nods in agreement and motions for me to lead the way."
            "I stand, scanning each cabinet's flashing lights and spot something I know for sure I'm good at and that Sasha would enjoy: Sitar Hero. I make my way over, checking over my shoulder to make sure I didn't lose her."
            show sasha surprised
            sasha.say "Sitar Hero? Really?"
            show sasha stuned
            bree.say "What's wrong with Sitar Hero?"
            show sasha joke
            sasha.say "Nothing...just get ready to get your ass kicked, is all."
            show sasha normal
            bree.say "Oh I see, you think you're good, huh?"
            show sasha shout
            sasha.say "I'll let my gaming do the talking here."
            show sasha normal
            "I give her a side-eye and pick my character, Muriel. I love that she's an old lady. Reminds me of my favorite cartoon when I was little."
            "Sasha picks a guy with a blond mullet and a black zippered trench coat. Very trendy. I let Sasha pick the song. I know them all anyway."
            "Time to choose the difficulty. I notice Sasha tab over to Expert mode."
            bree.say "Oh, you play on Expert too?"
            show sasha happy
            sasha.say "I'm a professional bassist, you dumb-bass."
            show sasha normal
            bree.say "Wooaaaaah wow them's fighting words, okay! Bring it."
            "The song begins and Sasha surprises me at how good she is at this game. I'm actually struggling to keep up."
            show sasha joke
            sasha.say "Having a little bit of trouble, gamer girl?"
            show sasha normal
            bree.say "No! I'll show you!"
            "As I spoke I glanced at Sasha, missing a crucial note."
            bree.say "AH! NO!! DAMMIT!"
            "The song ends as Sasha does a small victory dance."
            show sasha happy at vshake
            bree.say "Ughhh no fair…"
            sasha.say "What do you mean? The game is all about skill. Sounds like you need to practice some more."
            show sasha normal
            bree.say "Yeah, well...I went easy on you."
            show sasha joke
            sasha.say "Aww thank you."
            show sasha normal
            play sound cell_vibrate
            "I appreciate that Sasha's as sarcastic as I am. My phone buzzes. It's just a game app notification."
            "Before I lock the screen, I notice the time. We've been here for a while."
            bree.say "Well it was fun...I gotta go though, very busy with uh...gamer...stuff."
            show sasha happy
            "Sasha flashes me a genuine smile and waves."
            sasha.say "Okay. See you later. I had a lot of fun. Let's hang out more from now on, okay?"
            show sasha normal
            bree.say "Sure! I had a great time too. Catch you at home."
            $ game.pass_time(1)
            $ game.room = "map"
        "No thanks":
            bree.say "I'm good thanks though."
            show sasha shout
            sasha.say "OK. See you around."
            $ hero.cancel_event()
            $ sasha.love -= 2
    hide sasha
    $ game.flags.sasha_delay_female = TemporaryFlag(True, 1)
    return

label sasha_female_event_04:
    if sasha.love.max < 100:
        $ sasha.love.max = 100
    scene bg pub
    "Upon stepping foot inside, my eyes are immediately drawn to a familiar yet unexpected sight. Sasha is bent over a pool table, stretching her gorgeous body in order to make a far shot."
    show sasha play pool with fade
    "She seems like she's really focused. I don't want to startle her, so I approach carefully to make sure she catches sight of me. I dare not open my mouth until the shot is made."
    "CRACK!"
    "The balls make a satisfying sound against each other as the 6 ball flies into one of the pockets, sinking decisively."
    hide sasha
    show sasha at center, zoomAt(1.25, (640, 880))
    with fade
    bree.say "Good shot."
    show sasha happy
    sasha.say "Thanks. And thanks for not trying to scare me. What are you doing here?"
    show sasha normal
    bree.say "You're welcome. I hate it when assholes do that shit. I was bored at home and came by."
    "I notice the corners of Sasha's mouth pull into the smallest of appreciative grins."
    show sasha shout
    sasha.say "To say hi to me?"
    show sasha normal
    bree.say "No, I actually didn't know you were here. I figured you were home and just being quiet or something."
    show sasha shout
    sasha.say "Me? Quiet?"
    show sasha normal
    bree.say "Hmm...fair haha."
    show sasha annoyed
    "Sasha rolls her eyes ironically and cops a fake attitude."
    show sasha vangry
    sasha.say "Ohh, so now I'm LOUD?"
    show sasha normal
    "I scoff and fold my arms in return."
    bree.say "Oh yeah. SO loud. Sometimes I can't even sleep, it's just like constant."
    show sasha happy at startle
    "Sasha giggles and studies the pool table before her, no doubt planning her next shot."
    bree.say "So do you always come here alone then or...?"
    hide sasha
    show sasha play pool
    with fade
    "Sasha leans over again, aiming for the next striped ball she can sink. Looks like she'll have to bank it dangerously close to a solid. Tricky shot."
    sasha.say "Yeah. I like playing pool. Lets me do something while I just let my mind kind of wander. Plus I like to come and people-watch."
    bree.say "Wow…"
    hide sasha
    show sasha shout at center, zoomAt(1.25, (640, 880))
    with fade
    sasha.say "What?"
    show sasha normal
    bree.say "You're not gonna believe this haha."
    show sasha shout
    sasha.say "You gonna tell me or not?"
    show sasha normal
    bree.say "That's why I'm here. To people-watch."
    show sasha happy at startle
    "Sasha throws back her head in genuine laughter."
    sasha.say "Crazy! I guess great minds really do think alike."
    show sasha shout
    bree.say "Right?"
    show sasha shout
    sasha.say "Hey...how long do you plan on staying?"
    show sasha normal
    bree.say "I don't have anything to do now or tomorrow as far as I know, so...until last call?"
    show sasha shout
    sasha.say "Cool. How about I grab us a couple of shots and you be my player two?"
    show sasha normal
    bree.say "Isn't that phrase more for video games?"
    show sasha shout
    sasha.say "Same difference. You got it either way, nerd girl."
    show sasha normal
    bree.say "I'd be mad at you calling me that, but you're not wrong so I'll let it slide just this once."
    show sasha happy
    sasha.say "Thank you for sparing me from your wrath."
    hide sasha with easeoutright
    "Sasha turns, flipping her hair over her shoulder, and walks toward the bar."
    "...Wait...she didn't even ask me what I want...and am I supposed to rack these for a new game?"
    "I sigh but figure that's what she wanted. Maybe she'll appreciate it if I take the initiative."
    "I let my mind wander as I gather the balls and rack them. I place them perfectly on the table. Sasha's not back yet, so I decide to be extra anal and move all the numbers to the top."
    "...There we go. Instaframe-worthy. Actually, it's surprisingly satisfying to look at. Kind of like when you see freshly-organized stores that shoppers haven't destroyed yet."
    "A few more moments pass and I begin to muse to myself."
    bree.say "I wonder what kind of shot Sasha likes...? She strikes me as someone who doesn't like something too sweet."
    "A familiar voice pipes up behind me."
    show sasha shout at center, zoomAt(1.75, (640, 1190))
    sasha.say "Actually, that's exactly what I like."
    show sasha normal with vpunch
    "I jump, yelping a bit."
    bree.say "Don't sneak up on me like that!"
    show sasha joke at center, traveling(1.5, 0.3, (640, 1040))
    sasha.say "I wasn't sneaking. It's not my fault you zoned out like a space cadet."
    show sasha normal
    "...I guess she's right. I was pretty lost in my own head."
    "Sasha places my shot on the side of the pool table, and notices I racked for her."
    show sasha shout
    sasha.say "Hey...thanks for racking. I know I didn't explicitly tell you to, so it was nice that you did it unprompted."
    show sasha normal
    bree.say "You're welcome. Thanks for grabbing the shots. What'd you get?"
    show sasha shout
    sasha.say "Don't laugh...but I got us buttery nipples. 4 each."
    show sasha normal
    "The immature side of me laughs internally at 'nipples. 4 each'. Wait...4? That's…"
    bree.say "Haha! You planning to get fucked up tonight, huh?"
    show sasha happy
    sasha.say "Maybe...but trying to play pool while you're drunk as shit is fun. You game?"
    show sasha normal
    bree.say "Sure thing."
    show sasha shout
    sasha.say "You ever had this shot before?"
    show sasha normal
    "I shake my head, bringing the glass to my nose for a whiff. It smells fantastic. Like those yellow hard candies old ladies give you sometimes."
    show sasha shout
    sasha.say "It's butterscotch liqueur and Irish creme liqueur. Creamy, smooth, sweet."
    show sasha normal
    bree.say "When you describe it like that, it's almost sexy."
    show sasha joke
    sasha.say "I guess that's why it's called a buttery NIPPLE."
    hide sasha
    show pool sasha
    with fade
    "Sasha grabs her pole and chalks it. She places the cue ball where she wants it, draws back, and fires the ball cracking the group well. She's good. I think she'll win, especially if I'm about to get 4 shots in me."
    bree.say "Speaking of...thanks for footing the bill. You didn't have to."
    hide pool sasha
    show sasha shout at center, zoomAt(1.5, (640, 1040))
    with fade
    sasha.say "It's cool. Consider it a consolation for kicking your ass at Sitar Hero."
    show sasha normal
    bree.say "Thanks...I was really broken up about it. It drove me to drinking."
    show sasha happy at startle
    "I threw back another shot just to prove my point. Sasha scoffed and chuckled."
    sasha.say "You're a fucking goof, you know that?"
    show sasha normal
    bree.say "I know. Now, let's really start playing. It's my turn, right?"
    show pool sasha with fade
    "Sasha and I spent the rest of the night bantering back and forth, getting drunk together."
    "She told me about her annoying ex and how impulsive and meat-headed he was. Sounds like a real winner."
    scene bg street with fade
    "Eventually the bartender waved us over for last call, so Sasha paid the bill with a generous tip and we saw ourselves out. Walking home with Sasha feels natural."
    "The night air lingers on my skin once we get back in. It leaves me wishing I weren't returning to my room alone...but maybe I'm just a bit too drunk."
    scene bg bedroom2 with fade
    "I stumble to my room, hit the bed, and the nothingness of a deep sleep arrests me."
    $ game.flags.sasha_delay_female = TemporaryFlag(True, 1)
    $ sasha.love += 2
    $ game.room = "bedroom2"
    call sleep from _call_sleep_75
    return

label sasha_female_event_05:
    if sasha.love.max < 140:
        $ sasha.love.max = 140
    "It's rather warm inside and it's no better outside."
    "It just feels like there's no escaping the heat no matter how many layers of clothing I peel off."
    "I decide to throw on a tank top, some shorts and flip-flops. Can't go wrong with flip-flops."
    "I head downstairs to look for something to help myself out with this heat. I find Sasha standing in front of the freezer, door open."
    scene bg kitchen
    show sasha sport at right4
    with fade
    bree.say "Sasha? Sasha that's not how a refrigerator works, you're going to suck the cold out of it instead of the hot out of you."
    show sasha annoyed
    show fx drop at right4
    sasha.say "You know, I don't think you could suck the hot out of me even if you tried. You got any better ideas?"
    show sasha sadsmile
    "I smirk."
    bree.say "Not really."
    "I look around, thinking about ice cream, cold fruit, water…"
    bree.say "The pool! Of course!"
    "I try to seem cool. Clearly it was the obvious answer all along."
    "Really, truly, obscenely obvious."
    "Sasha thinks about my answer for a split second before her face lights up."
    show sasha happy
    sasha.say "Yes! Of course. I'll go grab a towel and swimsuit and…"
    hide sasha with easeoutright
    "She does not bother to finish her sentence. She just leaves."
    "She also does not bother to close the freezer. I close the door for her and reassure the freezer that it did a good job acting like an A/C."
    scene bg bedroom4 with fade
    "I run upstairs to put on a swimsuit under a coverup. I grab two towels, some sunscreen, and I take them all outside in a little tote."
    "Sasha also tosses some stuff out and comes back inside."
    scene bg kitchen
    show sasha swimsuit shout
    with fade
    sasha.say "We can't have a pool day with no snacks or anything else planned out. Plus, we need drinks. I'm going to get some beer. You figure out food."
    show sasha normal
    bree.say "Wait, bee--?"
    hide sasha with moveoutleft
    "Before I have a chance to answer, Sasha dashes off for alcohol."
    "Fuck. I hate that stuff. I'm a bit hesitant to try some, but we'll see."
    "I think about the fruit I thought of earlier and pull out a nice half-watermelon from the fridge. I scoop some out in small sphere-shapes with an ice cream scoop. I add in some kiwi, mango, pineapple…"
    show sasha swimsuit at left with moveinleft
    "I dump the balls back into the now empty half-watermelon. Looks like fruit confetti. Tasty."
    show sasha shout at center with ease
    sasha.say "I've been here for a bit watching, is that all you know how to do with fruit? Pass me a mango."
    show sasha normal at center, zoomAt(1.5, (640, 1040)) with dissolve
    "Sasha effortlessly peels the mango with her hands and starts to carve a \"V\" shape into two sides. They begin to resemble wings, maybe?"
    "She does another \"V\" slice at the front and picks up a piece and flips it over. It kind of looks like a beak."
    bree.say "You've made a bird!"
    show sasha happy
    sasha.say "Ca-CAW!"
    "I smile. She DOES have a goofy side."
    show sasha normal
    bree.say "Well, that's mine now. You can have some of my fruit confetti."
    show sasha shout
    sasha.say "It's for the pool, let's take it out with a small ice box to keep everything cool. Especially the beer."
    show sasha normal
    bree.say "Oh man. We're eating good today. Do you think some cheese and crackers would pair well?"
    show sasha shout
    sasha.say "Goes fine with beer. Bring some over!"
    $ game.room = "pool"
    scene bg pool
    show sasha swimsuit at center, zoomAt(1.25, (640, 880))
    with fade
    "I snag some port wine cheese and crackers and bring them outside with the cooler with Sasha's help."
    "We take off our coverups and I'm not sure if I'm the one that looks for a little too long or if it's her."
    show sasha shout
    sasha.say "Cover the fruit!"
    show sasha swimsuit at center, zoomAt(1.0, (640, 920))
    play sound water_splash
    with vpunch
    "I am confused, but I close the lid on the cooler. Water splashes over my back as soon as the lid shuts."
    show sasha happy
    "I think Sasha laughs so hard she swallows some water."
    bree.say "All right, I see how it is."
    play sound water_splash
    show playing water pool sasha noball
    with fade
    "I jump into the pool after Sasha and splash her."
    "She's still laughing."
    sasha.say "Hey, hey! I'm sorry! I thought it was hilarious! At least I told you to cover the fruit first!"
    "I pout. She has a point."
    sasha.say "There, there. It's not the end of the world. You just got a little wet. It won't be the last time!"
    bree.say "I-"
    play sound water_splash
    "And then I get splashed."
    bree.say "You gremlin!"
    sasha.say "No, no! Harpy. Harpy!"
    bree.say "Right, right, an awful water-harpy. When are you performing for me, anyways?"
    sasha.say "Hmm… We'll see about that. Let's enjoy the pool first since it's too hot for me to think."
    bree.say "I'll hold you to that!"
    hide playing water
    $ renpy.show("swimmingrace_bg_02", tag="bg")
    show sasha swimsuit happy at center, zoomAt(1.5, (640, 1040))
    with fade
    sasha.say "Let's get at the food, pass me a beer. You're having some. I grabbed a gentle one for you."
    show sasha normal
    "I take a sip. It tastes like… bread? Is that right? Bread?"
    bree.say "It tastes kind of like the way fresh bread smells."
    show sasha shout
    sasha.say "Yes, it's usually what beginners like. It's gentle and it's just bready. It's because of the yeast."
    show sasha normal
    bree.say "What do you mean? How does yeast make- oh, yeast makes bread. Duh."
    show sasha shout
    sasha.say "That's just a simplification. It's a lot more intricate than that, but I won't bore you."
    show sasha normal
    "I munch on the cheese and crackers and gesture for Sasha to have some. She does."
    bree.say "These are pretty good. I like the port wine flavor a lot."
    show sasha shout
    sasha.say "Yeah, no, these are really yummy with the beer."
    show sasha normal
    "We munch on the crackers."
    show sasha shout
    sasha.say "Want some fruit?"
    show sasha normal
    "Was she going to feed me again? I'm all for this."
    bree.say "Of course! Feed me, Sasha!"
    show sasha happy at center, zoomAt(2.5, (640, 1640)) with dissolve
    "And so she does. Cute."
    "I give her a bite of her carved mango. We spend some time eating the fruit until we finish it all up."
    sasha.say "Sweet and cool. Like me."
    show sasha normal
    bree.say "Very funny. We're talking about me, here."
    show sasha shout at center, zoomAt(1.5, (640, 1040)) with dissolve
    sasha.say "Yeah? How well can you swim? Wanna race and take a lap?"
    show sasha normal
    "Oh, oops. I'm not a very strong swimmer."
    bree.say "I, uh… no, I'm not a very good swimmer. I'm just here to escape the heat."
    show sasha sadsmile
    "Sasha looks like she feels a bit bad about what she said."
    show sasha shout
    sasha.say "Hmm… would you want to go over to the deep end with some help?"
    show sasha normal
    "I think I'm blushing."
    bree.say "How do you plan on doing that? You aren't supposed to be on someone's back when they swim."
    "I wave my finger at her."
    bree.say "It can lead to drowning, you know."
    show sasha happy
    sasha.say "Oh, don't be dramatic. Come on."
    show sasha normal
    "Sasha takes my hand and pulls. I follow along, doing my best doggy-paddle."
    show sasha surprised
    sasha.say "Are you trying to waddle? What are you doing?"
    show sasha stuned
    bree.say "I am trying to PADDLE. SASHA."
    show sasha surprised
    sasha.say "Oh, oops. Let me just…"
    show sasha normal at center, zoomAt(2.5, (640, 1640)) with dissolve
    "Sasha scoops me up in her arms instead. I feel like a damsel."
    bree.say "Oh no! I've been kidnapped! Help, help!"
    show sasha happy
    sasha.say "Should I drop you?"
    show sasha normal
    bree.say "Wait, no, please don't."
    show swimmingrace sasha swimsuit mc_swimsuit with fade
    "Sasha keeps wading towards the deep end of the pool. She reaches the edge and puts me at an angle where I can grab onto the ledge."
    sasha.say "Alright. Your feet won't touch the ground."
    bree.say "No, they do not touch the ground."
    "I notice the sun is setting and the golden hour illuminates Sasha's skin in a sensual way I've never seen before. I want to run my fingers through her wet hair. I want to touch her body and feel her beneath me."
    "I want to pull her close and touch my lips to hers. I want to ask permission to enter her mouth with my tongue. I…"
    bree.say "Can I get out now? I'm...definitely not SCARED but you know, I prefer to touch my feet to the ground."
    sasha.say "Of course...I'm so sorry if I made you feel uncomfortable."
    bree.say "No, I...you're here, so. I know I'm in good hands."
    hide swimmingrace swimsuit mc_swimsuit
    show sasha normal
    with fade
    "I stumble over my words...that's so unlike me. Normally I'm ready to bat with any manner of zingers."
    bree.say "A-Anyway um, I…"
    "Fuck. I'm kind of horny."
    bree.say "I'm...cold. I'm gonna dry off and head on in. Maybe take a nap."
    show sasha surprised
    pause 0.5
    show sasha normal
    "A look of surprise flashes across Sasha's face - if I'd blinked, I'd have missed it."
    show sasha shout
    sasha.say "Sure. Okay. I'll see you."
    show sasha normal
    "I don't stop my rush to look back at Sasha. I'm embarrassed and confused and so incredibly turned on. I feel awful about leaving her like that...but I can't be around her with these secret feelings."
    $ game.flags.sasha_delay_female = TemporaryFlag(True, 1)
    return

label sasha_female_event_05b:
    if sasha.love.max < 120:
        $ sasha.love.max = 120
    "Did I ever mention how much I love the mall?"
    "I mean, the crowds of people suck for sure."
    "But the place itself is always exciting."
    "And going there is like a mini adventure."
    if game.season == 2:
        "It's even better when Halloween is coming too."
        "All the stores are done up for the festive season."
        "And everyone's hurrying here and there, shopping for sweets."
        "It reminds me of how Halloween used to be, makes me feel like a kid again!"
    elif game.season == 3:
        "It's even better when Christmas is coming too."
        "All the stores are done up for the festive season."
        "And everyone's hurrying here and there, shopping for gifts."
        "It reminds me of how Christmas used to be, makes me feel like a kid again!"
    "And it seems to have the same effect on Sasha too."
    show sasha annoyed at center, zoomAt(1.25, (640, 880)) with dissolve
    "Only it turns her back into a surly, sulky little brat!"
    sasha.say "Urgh..."
    show sasha angry
    sasha.say "How many more shops do we have to do, [hero.name]?"
    sasha.say "All this false light is giving me a headache!"
    sasha.say "And the crowds are making me feel claustrophobic too!"
    show sasha annoyed at center, zoomAt(1.5, (640, 1040))
    "I force a smile onto my face as I turn to look at Sasha."
    "What I really want to do is tell her off for being such a killjoy."
    "I mean, why did she even agree to come to the mall with me in the first place?"
    if game.season == 2:
        "I could have done all the sweets shopping myself."
    elif game.season == 3:
        "I could have done all the gift shopping myself."
    "And twice as quickly without her to slow me down!"
    if game.season == 2:
        bree.say "Just feel the Halloween cheer in the air, Sasha!"
    elif game.season == 3:
        bree.say "Just feel the Christmas cheer in the air, Sasha!"
    bree.say "That always helps me to push on through at times like this."
    bree.say "And anyway, we only have one more thing to buy."
    show sasha shout
    sasha.say "That's a relief!"
    sasha.say "Who's the last name on the list?"
    show sasha normal
    "I bristle a little at this question."
    "I must have told Sasha that half-a-dozen times already!"
    bree.say "Just [mike.name]."
    bree.say "He's the last."
    show sasha happy at startle
    "Sasha can't help sniggering at the mention of our housemate's name."
    sasha.say "Let me guess..."
    show sasha joke
    sasha.say "Soap?"
    sasha.say "Deodorant?"
    show sasha happy
    sasha.say "It has to be personal hygiene products, right?"
    show sasha normal
    "As much as I want to tell Sasha off, I can't help giggling too."
    "[mike.name]'s a great guy, and I love living with him - most of the time."
    "But he can be a little stinky in that uniquely male way."
    "Sasha's joking about [mike.name] is just enough to cheer me up."
    "And so I make an effort to sell the task ahead to her."
    bree.say "It's no big deal, Sasha."
    bree.say "Let's hit one of the big department stores next."
    bree.say "That way we'll have more choice."
    bree.say "And we won't need to go to any more small stores."
    show sasha shout
    sasha.say "Sounds good to me, [hero.name]."
    show sasha happy
    sasha.say "Let's go!"
    scene bg mall2
    show sasha normal at center, zoomAt(1.25, (640, 880))
    with fade
    "I feel a new surge of energy as we enter the department store."
    "All we need to do is find one gift for [mike.name], then we're done."
    "How hard can that be?"
    "As soon as we're inside, I start looking around."
    "And it's then that I realise the problem with my plan."
    "Sure, there's a lot of choice in here."
    "But there's so much stuff - where are we supposed to even start?!?"
    "Sasha and I wander aimlessly for a while."
    show sasha annoyed
    "And I can feel her mood starting to turn sour again."
    "But then my eyes fall on what looks like the perfect gift for [mike.name]."
    show sasha normal at center, zoomAt(1.5, (640, 1040))
    "I pounce on it an instant later, holding it up for Sasha to see."
    bree.say "Aha!"
    bree.say "How about this?"
    if hero.morality >= 60:
        show sasha surprised at startle
        show fx question
        sasha.say "SOCKS?!?"
        show sasha shocked
        sasha.say "What are we, [hero.name]?"
        sasha.say "His adopted lesbian mommies?!?"
        show sasha annoyed
        hide fx
        "I can feel my cheeks flushing red as I wave the socks in the air."
        "But I don't put them down, even after Sasha makes fun of me."
        bree.say "Not all gifts have to be super-exciting, Sasha!"
        bree.say "And I've seen [mike.name] walking around with holes in his socks."
        bree.say "I think it'd be nice to get him some new ones."
        bree.say "It'd show him that we care!"
        "Sasha shakes her head and lets out an exasperated snort."
        show sasha normal
        "But she seems to relent and let the matter drop."
        show sasha shout
        sasha.say "Okay, [hero.name], okay."
        sasha.say "Socks it is."
        show sasha happy
        sasha.say "Just don't put my name on them, okay?"
        show sasha normal
        "I nod, happy to have the matter settled."
        "But then a thought occurs to me."
        bree.say "Oh...so you're going to get him a gift of your own?"
        bree.say "What's that going to be, Sasha?"
        show sasha shout
        sasha.say "Oh, don't you worry."
        show sasha joke
        sasha.say "I can think of something fun to give [mike.name]."
        sasha.say "And it definitely won't be socks!"
        show sasha normal
        "I get the feeling that Sasha's not going to tell me just what that might be."
        "So I just shrug and head towards the counter to pay for the socks."
        "At least the Christmas shopping is over for another year."
        "And now we can head for home."
        $ sasha.sub -= 2
        $ sasha.love += 1
    elif hero.morality >= 20:
        show sasha surprised
        show fx question
        sasha.say "Boxer shorts?!?"
        show sasha joke
        sasha.say "Isn't that a little boring, [hero.name]?"
        hide fx
        sasha.say "He's already got plenty of those!"
        show sasha normal
        "I can feel my cheeks flushing red as I wave the shorts in the air."
        "But I don't put them down, even after Sasha makes fun of me."
        bree.say "Not all gifts have to be super-exciting, Sasha!"
        bree.say "And I've seen [mike.name] walking around with holes in his underwear."
        bree.say "I think it'd be nice to get him some new pairs."
        bree.say "It'd show him that we care!"
        show sasha joke
        "I see a knowing smile spreading slowly across Sasha's face."
        "And she raises an eyebrow as she regards me."
        show sasha shout
        sasha.say "Oh...now I get it!"
        show sasha happy
        sasha.say "You've been staring at [mike.name]'s junk - haven't you?"
        show sasha normal
        with vpunch
        bree.say "WHAT?!?"
        bree.say "No...I...I don't know what you mean!"
        "I may have looked, sure."
        "But how can I help it?"
        "It's not like I make [mike.name] walk around in his underwear!"
        show sasha joke
        sasha.say "You just want to wrap the goods in nicer packaging!"
        sasha.say "Way to go, [hero.name]!"
        show sasha normal
        bree.say "It's not like that, Sasha!"
        bree.say "It's more like wanting to have nice cushions on the sofa."
        bree.say "Or pretty pictures hanging on the walls, you know?"
        show sasha happy
        sasha.say "You make [mike.name] sound like piece of furniture, [hero.name]!"
        show sasha normal
        "I get the feeling that Sasha's not going to let me explain myself."
        "So I just shrug and head towards the counter to pay for the shorts."
        "At least the Christmas shopping is over for another year."
        "And now we can head for home."
        $ sasha.sub -= 1
        $ sasha.love += 2
    elif hero.morality >= -20:
        show sasha surprised
        sasha.say "Whoa, [hero.name]!"
        sasha.say "Those are some REALLY tight pants!"
        sasha.say "They don't leave much to the imagination!"
        show sasha normal
        "I give Sasha a knowing smile, more than a little pleased to have shocked her."
        "But at the same time I shrug, dismissing her concerns as if they're irrelevant."
        bree.say "I don't know, Sasha."
        bree.say "I think he could stand to show himself off a little more."
        show sasha shout
        sasha.say "You mean you want to eye him up around the house?"
        show sasha flirt
        sasha.say "Isn't that, well...exploiting him?"
        show sasha normal
        "I let out a chuckle, amused by Sasha's concerns."
        bree.say "Oh come on, Sasha."
        bree.say "Don't give me that."
        bree.say "I'm not trying to turn [mike.name] into a sex-slave."
        bree.say "I just want to help him make the most of himself, that's all."
        bree.say "I think he'd be flattered to know I like the look of his body."
        "Sasha still doesn't look convinced."
        "She shakes her head and narrows her eyes."
        show sasha annoyed
        sasha.say "I dunno, [hero.name]..."
        sasha.say "Something about this just doesn't feel right."
        sasha.say "You go ahead and buy those pants if you like."
        sasha.say "But don't put my name on them, okay?"
        show sasha normal
        "I shrug again and make a little tutting sound."
        "I get the feeling that Sasha's not going to change her mind."
        "But that's not really a problem."
        "It just means that I'll get all the credit for the gift."
        "So I head towards the counter to pay for the pants."
        if game.season == 3:
            "At least the Christmas shopping is over for another year."
            "And now we can head for home."
        $ sasha.sub += 1
        $ sasha.love += 2
    elif hero.morality >= -60:
        sasha.say "Erm, [hero.name]..."
        show sasha shout
        sasha.say "That's a bikini!"
        sasha.say "And I don't think it's [mike.name]'s size either!"
        show sasha normal
        "I give Sasha a knowing smile and shake my head."
        "Then I hold the bikini up against my chest."
        bree.say "Yeah, like I'd want to see [mike.name] in something this cute!"
        bree.say "Of course not, Sasha - it's for me to wear!"
        show sasha annoyed
        "Sasha frowns and shakes her own head in turn."
        "Clearly she's not getting the point."
        show sasha shout
        sasha.say "I thought we were shopping for [mike.name]?"
        sasha.say "So what - you saw the bikini and just had to have it?"
        show sasha normal
        bree.say "No, Sasha!"
        bree.say "It's still a present for [mike.name]."
        bree.say "The gift he gets is the chance to see me in it!"
        show sasha surprised
        "The light of understanding finally appears in Sasha's eyes."
        "But then she looks more than a little shocked too."
        sasha.say "Wow..."
        show sasha shocked
        sasha.say "That's a little abstract for [mike.name], don't you think?"
        sasha.say "And maybe a little slutty on your part too!"
        show sasha normal
        "I snort and wave away her concerns with a flick of my wrist."
        bree.say "Oh, don't worry, Sasha."
        bree.say "I'll make sure [mike.name] gets it."
        bree.say "And anyway, it's not slutty."
        bree.say "It's actually empowering."
        bree.say "I'm not ashamed of being hot!"
        "Sasha looks less than convinced."
        "But that's not really my problem."
        "I was the one that came up with the idea for the gift."
        "So I head towards the counter to pay for the bikini."
        "At least the Christmas shopping is over for another year."
        "And now we can head for home."
    else:
        sasha.say "Erm, [hero.name]..."
        sasha.say "That's a vibrator!"
        show sasha happy
        sasha.say "And I don't want to think where [mike.name] could shove that thing!"
        show sasha normal
        "I chuckle and shake my head at Sasha's reaction."
        "How can she be so prudish about this kind of thing?"
        bree.say "Oh, I do, Sasha!"
        bree.say "I've always wanted to try this model of vibrator out."
        bree.say "And I was kind of hoping that [mike.name] would use it on me."
        bree.say "That way we can both enjoy his Christmas present!"
        show sasha happy at startle
        "Sasha bursts out laughing at this, but then she puts a hand to her mouth."
        show sasha normal
        "She seems to be amused and more than a little intrigued by the idea."
        "But there's still a part of her that's embarrassed by it too."
        show sasha shout
        sasha.say "I...I just don't know, [hero.name]."
        sasha.say "I mean, we all have to live together."
        sasha.say "Could you really look [mike.name] in the face?"
        sasha.say "You know - after he used that thing on you?"
        show sasha normal
        "I wave the vibrator in the air as I answer the question."
        "Not really caring if anyone sees me doing so."
        bree.say "Nah, Sasha, not really."
        bree.say "It'd only get awkward if he didn't use it properly."
        bree.say "If he didn't make me cum - then he'd never hear the end of it!"
        show sasha surprised
        sasha.say "Wow..."
        show sasha shout
        sasha.say "That's pretty bold of you, [hero.name]."
        show sasha joke
        sasha.say "And more than a little slutty!"
        show sasha normal
        "I snort and wave away her concerns with a flick of my wrist."
        bree.say "It's actually empowering."
        bree.say "I'm not ashamed of being hot!"
        "Sasha looks less than convinced."
        "But that's not really my problem."
        "I was the one that came up with the idea for the gift."
        "So I head towards the counter to pay for the vibrator."
        "At least the Christmas shopping is over for another year."
        "And now we can head for home."
    $ game.flags.sasha_delay_female = TemporaryFlag(True, 1)
    return

label sasha_female_event_sex_talk_05:
    if sasha.love.max < 140:
        $ sasha.love.max = 140
    "Sasha and I have been getting on really well recently, spending loads of time together and having fun."
    "So I guess we're in that stage of the relationship where you really start to get to know someone inside out."
    "You know what I mean - the period where you begin exploring what you have in common and where you maybe differ?"
    show sasha normal at center, zoomAt(1.25, (640, 880))
    "But today it seems like I'm getting a crash course in a certain side of Sasha, and it's a very interesting one indeed!"
    show sasha shout
    sasha.say "Okay, [hero.name]..."
    sasha.say "Cards on the table..."
    sasha.say "Do you use toys when you're on your own?"
    show sasha normal
    "Sasha just seems to drop the question into the middle of the conversation, casual as you like."
    "But to me it's more like she's tossed a hand-grenade into the it!"
    if hero.morality >= 25:
        "I can guess exactly what Sasha's talking about."
        "But I still feel the need to at least try deflecting the question."
        bree.say "You mean like dolls or something, Sasha?"
        bree.say "I mean [mike.name] gets mad when you call them that..."
        bree.say "He says they're 'action figures', whatever that means."
        bree.say "But everyone knows they're really dolls for men!"
        show sasha annoyed
        "Sasha rolls her eyes at everything I'm saying."
        "And once I'm done talking, she shakes her head."
        show sasha shout at startle
        sasha.say "Don't pretend to be naïve, [hero.name]..."
        sasha.say "You know full well that I'm talking about sex toys!"
        sasha.say "Dildos, vibrators, strap-ons, anal-beads and butt-plugs!"
        sasha.say "I want to know if you use them when you touch your pussy!"
        show sasha sadsmile
        "Now it's my turn to shake my head."
        "Totally freaked out by Sasha's sudden outburst."
        bree.say "No, Sasha..."
        bree.say "I don't even know what half of that stuff is, I swear!"
        bree.say "Please stop saying all those words?"
        bree.say "You're really starting to scare me!"
        show sasha stuned
        "Sasha looks pretty taken aback by my reaction."
        "But she does as I ask."
        show sasha surprised
        sasha.say "Okay, [hero.name], okay."
        sasha.say "Geez..."
        sasha.say "I had no idea you were such a prude!"
    elif hero.morality <= -25:
        "I frown and shake my head at Sasha's question."
        "Because it's just so obvious and boring!"
        bree.say "Like you even need to ask, Sasha?"
        bree.say "I never masturbate without using something that takes batteries!"
        bree.say "What's the point if it's not going to make you cum like a mother-fucker?"
        show sasha stuned
        "Sasha seems to be more than a little surprised by my answer."
        "My guess is that she thinks she's the really outrageous one around here."
        "That she always gets off on shocking people by saying stuff like that."
        "So it must be a surprise when she gets beaten at her own game."
        show sasha surprised
        sasha.say "Well..."
        sasha.say "I mean..."
        sasha.say "I always use a dildo at the very least!"
        show sasha stuned
        "I can't help sniggering at this."
        bree.say "Oh yeah, Sasha..."
        bree.say "I remember wanking like a fucking cavewoman!"
        bree.say "What do you do for seconds?"
        bree.say "Shove a pointed stick up your ass?!?"
        show sasha shocked
        "I'm still laughing as Sasha's eyes almost pop out of their sockets."
        sasha.say "Erm..."
        show sasha embarrassed
        sasha.say "Maybe we should change the subject, [hero.name]?"
    else:
        "I shake my head, already chuckling at Sasha's bold question."
        bree.say "Wow, Sasha..."
        bree.say "You really don't beat around the bush, do you?"
        "I might not be answering the question straight away."
        "But my tone and the look on my face make it plain that I'm intrigued."
        show sasha joke
        sasha.say "Aah..."
        sasha.say "You've got to be bold, [hero.name]..."
        sasha.say "Shake shit up if you want to get at the good stuff!"
        show sasha normal
        "I nod at this, preparing my answer."
        bree.say "Okay, Sasha..."
        bree.say "I don't always use toys when I masturbate."
        bree.say "Because I think there's something totally sensual about using fingers."
        show sasha shy
        "I can see that I've caught Sasha's interest."
        show sasha at center, traveling(1.5, 1.0, (640, 1040))
        "She's leaning in closer, nodding intently."
        "And she clearly likes where this is going."
        bree.say "But on occasion I do like to spice things up."
        bree.say "Like, I'll use a dildo to get myself off, you know?"
        bree.say "But a vibrator kind of feels like a bit much."
        bree.say "Almost like it'd be too much effort for a quick wank, yeah?"
        "Sasha's still nodding as I say all of this."
        "And I can tell that she's trying to look blasé and like she's not too impressed."
        "But I know the signs when I see them, and I'm sure she's getting turned-on."
        show sasha flirt
        sasha.say "Y...yeah, [hero.name]..."
        sasha.say "I totally know what you mean."
        sasha.say "Totally, get what you're saying..."
    show sasha embarrassed
    "Sasha pauses for a moment, clearly pondering where to take the conversation next."
    show sasha normal
    "But then I see her smile, and I can almost see the lightbulb come on above her head."
    show sasha shout
    sasha.say "Multiple partners, [hero.name]!"
    sasha.say "What's your stance on doing it with more than one person at once?"
    show sasha shy
    if hero.morality >= 25:
        "I can feel my cheeks flushing red almost as soon as Sasha raises the subject."
        "And there's nothing I can do to hide my reaction from her either."
        bree.say "Oh, Sasha!"
        bree.say "You mean being with more than one guy?"
        bree.say "I thought that kind of thing only happened in porn movies?!?"
        "Sasha doesn't seem in the least bit put off by my reaction."
        "In fact, it seems to make her all the more eager to go further still."
        show sasha shout
        sasha.say "Oh, it happens for real, [hero.name]..."
        sasha.say "And it doesn't have to be with another guy either."
        sasha.say "I've been with a guy and two girls in the past."
        show sasha wink
        sasha.say "Hell, I've been with more than two of each!"
        show sasha shy
        "Part of me can't believe the revelations that I'm hearing."
        "But another can't comprehend that they're coming from Sasha too!"
        "I feel like I'm seeing a whole different side of her."
        bree.say "Oh..."
        bree.say "That's...fascinating, Sasha..."
        bree.say "Totally fascinating!"
        show sasha shy
        "I can tell that Sasha wants to tell me more."
        show sasha sadsmile
        "But then she can also see the fear on my face right now."
        show sasha normal
        "So instead she chooses to leave it there."
        "Almost like she's accepting the prestige of shocking me to my core."
        "Rather than risking the conversation ending if she pushes me further still."
    elif hero.morality <= -25:
        "I almost laugh out loud as Sasha broaches the subject of threesomes."
        "Because I stopped calling my multiple partner encounters that a long time ago."
        "You know, since there's seldom only three of us involved in them anymore?"
        bree.say "The more bodies the better..."
        bree.say "Right, Sasha?"
        "I hold up both hands."
        "And I motion like I'm holding something in each that just might be a cock."
        "Then I act out sticking them both in my mouth, using the tip of my tongue to push out my cheeks."
        "I make sure to add a knowing wink as well, implying that Sasha's been in that position too."
        show sasha embarrassed
        sasha.say "Erm..."
        sasha.say "Yeah, [hero.name]..."
        sasha.say "Of course!"
        sasha.say "I mean, being in the band..."
        sasha.say "Offers like that are always coming my way."
        sasha.say "So you've got to be pretty picky about saying yes."
        with vpunch
        "Now I really do laugh out loud."
        "As I can see that Sasha's getting way out of her depth."
        with vpunch
        bree.say "Ha, ha!"
        bree.say "You've got to be joking, Sasha?!?"
        bree.say "You're in a fucking band and you're not fucking the band?"
        bree.say "I thought rock and roll was all about living like a hedonist?"
        bree.say "If it were me, I'd have a cock in every hole as soon as a gig was over."
        bree.say "Hell, I'd be trying to get two in most of them!"
        show sasha blush
        "Now I can see that Sasha's on the verge of breaking."
        "For the first time I can remember, she's the one turning red."
        show sasha embarrassed
        "And I can see that she's desperate to change the subject too!"
    else:
        "I know where this conversation is going."
        "Threesomes and multiple partners is one of those explicit subjects."
        "The kind of thing you throw out there on the one level to look experienced."
        "But on another to kind of feel out the person that you're talking to."
        "My guess is that Sasha's trying to get a measure of me with this one."
        "So I need to be equally measured in the responses that I give her."
        "Not because I'm trying to manipulate her."
        "More because I want to have a measure of control too."
        bree.say "I know what you're saying, Sasha..."
        bree.say "And I've had a few in my time."
        bree.say "Like, I'm not always on the lookout for them."
        bree.say "But if the right one comes along..."
        show sasha shy
        "Much to my relief and delight, Sasha starts nodding her head."
        "Perhaps a little more eagerly than she means to."
        show sasha flirt
        sasha.say "Oh, me too, [hero.name], me too."
        sasha.say "I mean, being in the band..."
        sasha.say "Offers like that are always coming my way."
        sasha.say "So you've got to be pretty picky about saying yes."
        show sasha normal
        "I return the nod, letting Sasha know that I agree with her."
        "But at the same time, I feel a sense of warmth inside."
        "Because I know that I managed to keep that all important level of control."
    show sasha shout
    sasha.say "Yeah..."
    sasha.say "Multiple partners can be fun and all that..."
    sasha.say "But you can still have fun with one guy, right?"
    show sasha normal
    "I feel a little more like we're getting back onto safe ground here."
    "Plus I think I catch the scent of gossip on the air."
    "All of which makes me want to encourage Sasha to say more."
    bree.say "Oh, you're not wrong there!"
    bree.say "But it has to be the right guy."
    "Sasha's nodding now, as she warms to the subject."
    show sasha shout
    sasha.say "Take my ex, Scottie for example..."
    sasha.say "Great-looking guy, and jacked as hell too!"
    show sasha annoyed
    sasha.say "But the moron didn't have two braincells to rub together!"
    show sasha normal
    "I'm nodding too by now."
    "Because I know exactly what Sasha's getting at."
    bree.say "Oh yeah..."
    bree.say "You have to be able to have a conversation at some point in the relationship!"
    show sasha wink
    sasha.say "Of course you do - it can't all be about sex!"
    if hero.morality >= 25:
        bree.say "Oh, Sasha..."
        bree.say "You're so naughty!"
    elif hero.morality <= -25:
        bree.say "Thing is you've got to use a guy like that, Sasha..."
        bree.say "Make sure he pleasures you and then kick him to the kerb!"
    else:
        bree.say "If it could, then he sounds like he'd be perfect!"
    show sasha normal
    "Now that we're talking about actual guys that we know, the inevitable happens."
    "The subject slowly turns to the closest one to both Sasha and myself."
    bree.say "So..."
    bree.say "What do you think of [mike.name]?"
    bree.say "He's not here to listen in or anything."
    bree.say "So we can be brutally honest!"
    show sasha normal
    "I was expecting to have to coax Sasha just a little more."
    "But instead she comes straight out with it."
    show sasha shout
    sasha.say "Ah..."
    sasha.say "Don't get me wrong, [hero.name]..."
    sasha.say "As a friend and housemate, [mike.name]'s great - aside from the typical guy bullshit!"
    sasha.say "He's pretty cute too."
    show sasha embarrassed
    sasha.say "But he just comes over as totally innocent, you know?"
    sasha.say "Like he's not had his heart broken yet!"
    show sasha sadsmile
    if hero.morality >= 25:
        bree.say "Oh, Sasha..."
        bree.say "Poor [mike.name] shouldn't have to be broken by anything!"
    elif hero.morality <= -25:
        bree.say "Well, if he needs someone to break him in..."
        bree.say "I know just how to turn a good boy bad!"
    else:
        bree.say "I get what you're saying, Sasha..."
        bree.say "He is kinda like a puppy-dog most of the time!"
    show sasha normal
    "Sasha nods as she listens to all that I have to say."
    "But I'm not sure if any of it really has time to sink in."
    "Because she seems pretty eager to change the subject a moment later."
    show sasha flirt
    sasha.say "Now [mike.name]'s little buddy..."
    sasha.say "There's a guy I could really sink my teeth into!"
    bree.say "Oh..."
    bree.say "You mean Jack?"
    show sasha happy
    sasha.say "That's the one!"
    show sasha normal
    "I have to admit to being more than a little puzzled by Sasha's interest in Jack."
    "From what I know of the guy, he's very sweet and I guess kind of cute too."
    "But he's also a total geek, even more so than [mike.name]."
    bree.say "I didn't think he was your type, Sasha?"
    bree.say "I thought you were into buff guys, like jocks?"
    bree.say "Jack's a bigger nerd than [mike.name]!"
    show sasha joke
    "The look on Sasha's face becomes sly and knowing as I say all of this."
    show sasha wink
    "She gives me a wink too, like she's about to impart some secret knowledge."
    show sasha shout
    sasha.say "Yeah, yeah, yeah..."
    sasha.say "But he's also got sub written all over him, [hero.name]!"
    sasha.say "All you gotta do is give a guy like that a little sugar..."
    show sasha happy
    sasha.say "Then you can walk all over him as much as you like!"
    show sasha shy
    if hero.morality >= 25:
        "I can't believe what I'm hearing."
        bree.say "Oh, Sasha..."
        bree.say "That's so mean!"
    elif hero.morality <= -25:
        "I nod eagerly, wanting to hear more."
        "But I can't be sure if it's the idea of dominating Jack that's turning me on."
        "Or else it's the fact that Sasha's into that kind of thing too!"
        bree.say "That sounds great, Sasha - tell me more!"
    else:
        "I'm kind of surprised to be hearing Sasha admit stuff like that."
        "As I had no idea she was into that kind of thing!"
        bree.say "I guess if that's what you're into..."
    show sasha normal
    "But then Sasha sighs and shakes her head."
    show sasha shout
    sasha.say "Problem is that he's [mike.name]'s buddy."
    sasha.say "So breaking him in would be awkward."
    sasha.say "You'd probably have to make him blubber a good couple of times."
    sasha.say "And that's a hard thing to explain to his mates!"
    show sasha normal with fade
    "After that we seem to drift onto other topics."
    "And none of them are as exciting as the previous ones."
    "But when the conversation comes to a natural end, I'm not disappointed."
    "Because I have so much new information about Sasha to process."
    "And I feel like she was really beginning to open up to me back there."
    "As though the connection between us is getting stronger all the time."
    $ game.flags.sasha_delay_female = TemporaryFlag(True, 1)
    return

label sasha_female_event_06:
    "Waking up is hard this morning."
    "I stumble to the kitchen...but there is no cup of ambition to pour."
    "Sooo... drowsyyyy..."
    show sasha sleep surprised with dissolve
    sasha.say "Oh, good lord. You look like death. Late night?"
    show sasha normal
    bree.say "I couldn't sleep."
    show sasha shout
    sasha.say "Coffee time?"
    show sasha normal
    "She says it gently, almost like I'll break if she raises her voice. Does she think I'm hungover?"
    "It sounds nice, anyways."
    bree.say "…Coffee time."
    show sasha happy
    sasha.say "Alright. I'm feeling pretty sleepy too. I know of a nice café near here. You'll love it."
    scene bg bedroom2 with fade
    "We both don some nice casual clothes and go to the café together."
    scene bg coffeeshop
    show sasha casual
    with fade
    "It's a small, very cute place. There's soft mood lighting, a cozy atmosphere, and the air is filled with the scent of homemade pies, fresh bread, and all other kinds of delicacies."
    show sasha at center, zoomAt(1.5, (640, 1040))
    pause 0.2
    show sasha at center, zoomAt(1.5, (640, 1140)) with ease
    "We're seated quickly and served water."
    bree.say "This is an adorable café, but I feel a little out of my element. I assume you have a favorite order?"
    show sasha shout
    sasha.say "Mm. You bet. I hope you enjoy it. The order will come with two cups, so we can share."
    show sasha normal
    "The waitress comes back, and Sasha makes her order. I just sit there and look cute."
    bree.say "Do I get to know anything about the coffee before I drink it?"
    show sasha happy
    sasha.say "Nope! It's made one specific way with specific beans. Sit tight and be patient. The fidgeting is pretty cute, though. I can tell you're excited."
    "Heck."
    show sasha normal
    "The waitress brings in two mugs and something that looks like an open hourglass. There's coffee in it and it's got a funny little jacket around the bit where the hourglass gets thin."
    "She also brings a small bowl of grapes."
    bree.say "What is this coffee hourglass?"
    show sasha joke
    sasha.say "It tells you when the coffee is ready."
    show sasha normal
    bree.say "Oh. Okay. How do I tell when it's done?"
    show sasha shout
    sasha.say "I'm kidding. Sorry, maybe I shouldn't tease you when you're uncaffeinated like this. It's a glass pour-over coffee maker."
    sasha.say "You put the coffee on this open bit and pour hot water into it. The glass is supposed to keep it all coffee-only with no extra flavors, and it lets the water hang out with the beans more so we get all the coffee flavor and the good stuff out of them."
    show sasha normal
    "Sasha pours me a cup."
    "I take a sip of the black coffee. It's nutty, smooth, and a little fruity. It's delicious."
    bree.say "Oh, this coffee is so good. It's so smooth. What kind is this? How is it so good?"
    show sasha happy
    sasha.say "Oooh, I love talking about coffee. I won't bore you with all the bean types, but this is a medium roast."
    show sasha normal
    bree.say "Please, bore me! This way I'll be able to see how well this coffee works. I know there are different types of roasts, but I don't know all that much about them."
    "I keep sipping at the coffee."
    "Sasha looks like she might be in love with her cup."
    "I may join her."
    show sasha shout
    sasha.say "Blonde roasts are really… they're really acidic? They're also called light roasts sometimes. They taste sour sometimes as well. They're really hit or miss for me, so I just avoid them."
    show sasha normal
    bree.say "With everything I learned about beer over the past few days, I am surprised you don't like sour-ish coffee."
    show sasha shout
    sasha.say "Sours are very different! You can't judge me!"
    show sasha normal
    bree.say "Alright, fine. What about this medium roast? I think the menu said something about it pairing well with fruit?"
    show sasha shout
    sasha.say "Right, yeah, a lot of medium roasts avoid tasting burned like some dark roasts. They keep the fruity notes of the coffee beans and they just pair really well."
    show sasha normal
    bree.say "I saw some stuff about flavored coffee too? Hazelnut?"
    show sasha shout
    sasha.say "You know essential oils?"
    show sasha normal
    bree.say "The ones that our neighbor sells?"
    show sasha shout
    sasha.say "No- well, sort of. Not really. You toss the beans in the oils. Because they're so dry, they just sponge it up."
    show sasha normal
    bree.say "Oh! That's really clever. I like that."
    "I take a handful of grapes and eat them. I sip at the coffee. It's so good!!"
    bree.say "Aaah! Delicious! These shouldn't be this good together!"
    show sasha joke
    sasha.say "It's criminal. Coffee is already addicting enough on its own. This should be illegal."
    show sasha normal
    "Some cafe-goers look daggers in Sasha's direction."
    show sasha shout
    sasha.say "Maybe I shouldn't curse coffee in such a way. Not here."
    show sasha normal
    bree.say "Definitely not here."
    bree.say "How much of a coffee snob are you, anyway?"
    show sasha shout
    sasha.say "Guess."
    show sasha normal
    bree.say "You started in… high school. Someone warned you not to and you did it anyways."
    show sasha shout
    sasha.say "Oddly close, but no."
    show sasha normal
    bree.say "Band members warned you not to during long practices."
    show sasha happy
    "Sasha smiles."
    bree.say "Ha!"
    show sasha shout
    sasha.say "Still no cigar. But you almost got me. Writing music takes a lot of work and late nights."
    sasha.say "When you really get into the groove, you just don't want to stop. You want to keep going and get it all out."
    show sasha normal
    "She sounds like she really likes her music and her hobby. It's no surprise, seeing she's in a band."
    show sasha shout
    sasha.say "You're not very into coffee, but I've seen you have some. Biology stuff?"
    show sasha normal
    bree.say "And here's where you got me. Definitely biology stuff. There's a lot of memorization early on in the major and then it's a jumbled mess."
    "I decide to match her words."
    bree.say "When you get into the groove, you really want to keep going and get it all in."
    show sasha happy
    sasha.say "We relate pretty hard here."
    show sasha normal
    "We really do. I feel my heart pound."
    bree.say "Yeah."
    "I fall silent. I wonder if Sasha can hear my heart, even though I know that's scientifically impossible from across the table."
    show sasha shout
    sasha.say "Don't worry, I can."
    show sasha normal
    with vpunch
    bree.say "Wh-WHAT?"
    "I panic. My heart races faster. Christ, slow down, it's not a marathon, I chide myself."
    show sasha shout
    sasha.say "Relate."
    show sasha normal
    bree.say "OH. Yeah. Yes. Mm. Mmhm. Yes. Relate."
    show sasha surprised
    "Sasha looks at me like she's questioning my sanity."
    sasha.say "Uh...you okay?"
    show sasha normal
    bree.say "Totally! I'm…"
    show sasha joke
    sasha.say "Nervous?"
    show sasha normal
    "How did she know?!"
    show sasha shout
    sasha.say "Me too. So, don't say anything. Let me just talk for a bit, okay?"
    show sasha normal
    "I nod, and I feel my face burn bright red. I wonder if I'm visibly blushing or not."
    show sasha shout
    sasha.say "You're funny. You're smart. You're...someone I want to spend more time around. So, why don't you?"
    show sasha normal
    "I can't believe what I'm hearing. Is Sasha asking me out?"
    show sasha shout
    sasha.say "I'm asking you out. Just in case you were overthinking it and wondering if I was or wasn't."
    show sasha normal
    "HOW CAN SHE READ MY MIND LIKE THIS?!?" with vpunch
    show sasha shout
    sasha.say "...Hello? You look like you're paying attention but you're not answering. Did I break you?"
    show sasha normal
    "The words finally manage to propel themselves out of my lumped throat."
    bree.say "Y-yeah, I can fine just you hear--I can hear you just fine!"
    show sasha shout
    sasha.say "Well then?"
    show sasha normal
    "I attempt to gather my composure and fail at looking as cool as I usually do."
    bree.say "I'd really like that."
    show sasha shout
    sasha.say "My band, The Deathless Harpies, has a concert coming up. It'd be cool if you could come have a listen. We're a power metal band."
    show sasha normal
    bree.say "Well, I like post-hardcore so power metal is an easy next step. I'd love to come."
    show sasha annoyed
    sasha.say "Post-hardcore? You emo."
    show sasha normal
    bree.say "Well, not anymore anyway."
    show sasha happy
    "I laugh nervously. Really? Me. Her. A date. The next time I see Sasha, we'll be on a date."
    show sasha shout
    sasha.say "You know us coming here was a way to get us alone, by the way, right?"
    show sasha normal
    bree.say "Wh...why?"
    show sasha shout
    sasha.say "Didn't want to have to risk getting interrupted. We have all the supplies to make perfectly good coffee at home. But I wanted to talk to you alone."
    show sasha normal
    bree.say "How long have you felt this way about me?"
    show sasha joke
    sasha.say "I dunno. You just kind of grew on me. But I like it. You're like mold. Gross but fuzzy."
    show sasha happy
    bree.say "Oh my god, fuck you."
    "I laugh at her absurdity but I'm grateful for the levity her joke brought to the heavy atmosphere."
    show sasha joke
    sasha.say "Not before the first date! Which, by the way, the concert is tonight"
    show sasha normal
    "...Fuck. That made me kinda horny again. FUCK. How does she do that? Wait. Tonight?"
    bree.say "Prude."
    "I tease her. But then my mind wanders. I have to get ready for the concert."
    show sasha shout
    sasha.say "Well, you seem like you've finally gotten out of your morning mood. Do you have plans today?"
    show sasha normal
    menu:
        "Yes":
            bree.say "Yeah, sorry. I gotta head out."
            bree.say "I'll see you around though. And tonight."
            show sasha shout
            sasha.say "I'm going to stick around here. See you."
            show sasha normal
            "She winks and I gather my things, wave, then head out."
            hide sasha
            scene bg street
            with fade
            $ game.flags.sasha_delay_female = TemporaryFlag(True, 1)
            $ game.room = "street"
        "No":
            $ sasha.love += 1
            bree.say "I can stay a little longer."
            show sasha happy with fade
            "Sasha and I chat for a few more minutes. I ask her about the boring coffee bean types and she reluctantly lets down her walls to nerd out for a bit."
            "After an hour, we notice the time and decide to part ways, promising to see each other at the concert later."
            scene bg black with dissolve
            $ game.flags.sasha_delay_female = TemporaryFlag(True, 1)
            $ game.pass_time(1)
            $ game.room = "street"
    return

label sasha_female_event_07:
    if sasha.love.max < 180:
        $ sasha.love.max = 180
    scene bg bedroom2 with fade
    "The day flew by fast. Too fast. It's already time to start getting ready."
    "I'll see Sasha and her band perform...and we might do something after. Who knows?"
    play sound door_knock
    pause 0.5
    show sasha normal date at right with easeinright
    "Sasha knocks on my door to visit me a few hours before call time."
    show sasha happy
    sasha.say "Are you excited for tonight? Do you know what you'll wear? Think you told me you were a lil' emo!"
    show sasha wink
    "She winks at me. Think I'm already unraveling."
    bree.say "You know, at least I'm not stuck in that phase still."
    show sasha joke
    sasha.say "Yeah? Why're you going out tonight with me then, huh?"
    show sasha normal
    bree.say "'C-Cause I never grew out of it…"
    show sasha sadsmile
    sasha.say "Mm-hmm."
    show sasha normal
    bree.say "How will this work out, then? I can't talk to you while you're on stage."
    show sasha shout
    sasha.say "You're right, but I've planned for that. We've got more groups playing after us to host a dance… type… thing."
    sasha.say "And before that, you can come backstage and we can have a quick drink before I, uh…"
    show sasha embarrassed
    "Sasha looks down a little."
    "She seems embarrassed."
    bree.say "Before you...?"
    show sasha blush
    sasha.say "Before I play for you, goofball."
    show sasha shy
    "And here is where she slays my cheeks. I'm all red."
    "I give her a bright smile."
    show sasha normal
    bree.say "I'm looking forward to it. Are you all readied up?"
    show sasha shout
    sasha.say "Yep! Let's go!"
    scene bg street with fade
    "And off we go. I know it's just call time and I'll be hanging out for like an hour or two before the show actually begins but hey it's cool. I'll get to spend more time with Sasha this way."
    "..."
    "We fall silent on our way, and I find myself lost in thought."
    "I know I'm beyond excited to see her in her element. Maybe I should ask her if she wants to keep me company during my biology study sessions."
    "Definitely not as cool as a rock concert though. Maybe not. Stupid idea."
    "...Unless?"
    scene bg door pub with fade
    "I'm pulled out of my embarrassing thoughts once we arrive."
    scene bg pub with fade
    "The venue hums with life and the chatter of the crowd makes it hard to hear any meaningful conversation."
    show concert pub anna kleio sasha mike date at center, zoomAt (1.6, (855, 980))
    "I take a drink once it all begins and pay close attention to Sasha once the band walks on stage. I hope I get to meet the other members too."
    scene bg black
    show concert solo sasha date
    sasha.say "Hello everyone! Thank you for coming tonight to see and support us!"
    scene bg black
    show concert pub anna kleio sasha mike date
    "The crowd claps and whoops. I give her a cheery whistle."
    scene bg black
    show concert solo kleio date
    kleio.say "Are you bitches ready to rock?!?"
    "The crowd cheers even louder."
    kleio.say "Hell yeah! Let's get it started!"
    scene bg black
    show concert pub anna kleio sasha mike date at center, zoomAt (1.6, (855, 980))
    play music "music/deathless_harpies/Deathless_Harpies.ogg" loop
    "The drum counts the band in and the jam starts. Kleio sings, and wow, she's amazing! I'm really digging this song."
    "The crowd roars! I can't believe the energy around me. It's so lively!"
    "I push my way towards the front, right at the stage's edge."
    "Maybe I'm hoping she looks at me here and there."
    scene bg black
    show concert solo sasha date
    "..."
    "Sasha turns towards me during a song and walks towards me."
    scene concert_solo_bg_pub_sasha at center, zoomAt(1.2, (640, 740)), dark, blur(5)
    show sasha kiss date
    with fade
    $ sasha.flags.kiss += 1
    "She sits on the edge of the stage and kisses me very briefly."
    "..."
    hide sasha kiss
    show concert pub anna kleio sasha mike date at center, zoomAt (1.6, (855, 980))
    with fade
    "The song blares up until the end and starts another barrage of screaming from the audience."
    kleio.say "You wanna keep it going?!"
    "The crowd is still going strong."
    kleio.say "GOOD! But before we start our next song, our bassist has a special message for someone in the audience. Sasha, get up here!"
    scene bg black
    show concert solo sasha date
    sasha.say "I've got a really cute date here tonight! I just kissed her during that last song, and this next one is dedicated to her!"
    play music "music/roa_music/smile_for_me.ogg" loop
    "Ahh, I'm a mess. Everything she does just gets to me. She's so cute and so hot… and she's dedicating a song to me!"
    scene bg pub with dissolve
    "The band finishes their set and I look for Sasha after the performance, once they're all available to mingle."
    show sasha happy date at center, zoomAt(1.5, (640, 1040))
    sasha.say "[hero.name]! I found you!"
    show sasha normal
    bree.say "Sasha! You were SO GREAT up there!"
    "Sasha smiles. I think my heart flutters a little."
    "She looks great in her performance outfit. Very striking."
    show sasha shout
    sasha.say "Thank you! I was happy to see you near the front."
    show sasha normal
    bree.say "Mm, yeah, I saw you look at me often while you were on stage."
    show sasha shout
    sasha.say "Oh, you noticed?"
    show sasha normal
    bree.say "Of course!"
    show sasha joke
    sasha.say "I'd be a little shocked if you didn't, considering I dedicated a song to you and kissed you in the middle of another."
    show sasha normal
    bree.say "Listen, sometimes crushes make you miss the obvious. You're lucky I caught these at all."
    show sasha shout
    sasha.say "There are other groups playing soon, do you dance at all?"
    show sasha normal
    bree.say "God, no, but for you? I'll give it my best."
    "Sasha takes my hand and leads me to the dance floor."
    hide sasha
    scene bg pub at center, zoomAt(1.2, (640, 740)), dark, blur(5)
    show dance sasha date at center, zoomAt(1.2, (640, 740))
    with fade
    "She's very fluid in all her movements, and she's got a firm grip on my wrist."
    "She pulls me in very close, turning me around so that she presses against my back."
    "People seem jealous that I'm with someone from the band."
    sasha.say "You're very cute, you know that? I saw you blushing from the stage."
    bree.say "I don't know what you're talking about."
    sasha.say "You're doing it now."
    bree.say "I plead the fifth."
    sasha.say "I kinda wanna see how red your cheeks can get."
    "I manage to find some courage."
    bree.say "What about you?"
    "I give her a quick peck on the cheek."
    "She cocks a brow at me and gives me a sexy, lopsided smile."
    "I really like that look on her."
    sasha.say "Yeah, alright, alright. You got me."
    "The band onstage keeps playing, but we've stopped dancing to their beat, miles away from reality right now."
    "Surreal."
    "Floating."
    "Ecstatic to be with her."
    "Once we come down, Sasha leans in close to my ear to make sure I can hear her over the noise."
    sasha.say "We've also got some merch, but you can have one that features me free of charge."
    sasha.say "If we're on a date together I want to make sure everyone knows! Actually, let me sign it super fast.."
    "Sasha scribbles on the back of my shirt with a marker she pulled out of thin air."
    sasha.say "There."
    bree.say "What does it say? Is it just your actual signature, or??"
    sasha.say "Wait until you get to a mirror instead."
    scene bg pub with dissolve
    "We mingle with the band and take in the environment, dancing here and there. The event comes to a close and Sasha helps the band pack up before we hop in the car back home."
    scene bg bedroom2 with dissolve
    "The first thing I do once I'm alone is turn away from my bedroom mirror and to have a look at what Sasha wrote on my back."
    "I see the words ‘Sasha's Gal' in metallic purple."
    "...I can't believe she really did me like that... and I can't believe what a sucker I am to like it this much."
    $ game.flags.sasha_delay_female = TemporaryFlag(True, 1)
    $ sasha.love += 4
    $ game.room = "bedroom2"
    scene bg black with dissolve
    return

label sasha_female_event_08:
    if sasha.love.max < 200:
        $ sasha.love.max = 200
    scene expression f"bg {game.room}"
    show sasha shout at center, zoomAt(1.0, (640, 720)) with fade
    sasha.say "Ah..."
    sasha.say "[hero.name]?"
    show sasha normal at center, traveling(1.5, 0.5, (640, 1040))
    "I look up as soon as I hear Sasha calling my name."
    "Mostly it's out of sheer instinct and nothing more."
    "But I can also tell that there's something more interesting in Sasha's tone."
    "Like the reason that she wants my attention is more than just to say hi."
    bree.say "Yeah, Sasha..."
    bree.say "What's up?"
    show sasha shout
    sasha.say "Oh..."
    sasha.say "Nothing really..."
    show sasha blush
    sasha.say "Nothing that important!"
    show sasha embarrassed
    "I'm nodding as Sasha says all of this."
    "But I don't believe her, not even for an instant."
    "Because I know that she's doing the best she can to hide her real intentions."
    bree.say "Okay, Sasha..."
    bree.say "Then I guess it's not all that important for me to hear it!"
    show sasha annoyed at center, zoomAt(1.5, (740, 1040)) with ease
    with hpunch
    "I manage to half turn away from Sasha before I feel her hand on my arm."
    show sasha normal at center, zoomAt(1.5, (640, 1040)) with ease
    "And I do the best to keep from laughing as I let her turn me back around."
    show sasha pain
    sasha.say "No, [hero.name]!"
    sasha.say "I...I mean it is pretty important..."
    show sasha sadsmile
    "I feel like I've spent long enough torturing Sasha."
    "So I make sure to have a sympathetic look on my face."
    bree.say "It's okay, Sasha..."
    bree.say "I'm only teasing you."
    bree.say "Go on and tell me what you wanted to say."
    show sasha normal
    "Not only have I reassured Sasha, I've totally given her permission to say her piece."
    "But the fact that she's still stumbling over what she has to say really strikes me."
    "Because it must mean that what she has to say is pretty important after all."
    show sasha shout
    sasha.say "Well..."
    sasha.say "I was just gonna say that..."
    show sasha embarrassed
    "Sasha now looks like she's doing all she can to get the words out."
    "Almost like it's a physical battle for her to speak them."
    show sasha blush
    sasha.say "That..."
    sasha.say "That I'm kind of in love with you!"
    show sasha embarrassed
    "As soon as Sasha finally manages to say it, the roles are reversed."
    "Now it's me that's stuttering and blinking in sheer surprise."
    bree.say "Y...you..."
    bree.say "You love...me..."
    bree.say "Sasha, you really mean that?!?"
    "Sasha's nodding her head like crazy now."
    "Doing all she can to confirm that I'm right."
    show sasha happy
    sasha.say "That's right, [hero.name]..."
    sasha.say "When we're together, I feel happier than I can ever remember feeling."
    sasha.say "And when we're apart, you're like, the only thing I can think about!"
    show sasha blush
    sasha.say "I...I know this is a heavy thing to drop on you."
    sasha.say "And you probably don't feel the same way about me..."
    show sasha embarrassed
    "Sasha pauses and takes in a deep breath."
    "Then she lets it out with a weary sigh."
    show sasha blush
    sasha.say "Urgh..."
    show sasha shout
    sasha.say "But I had to say it before I went crazy."
    sasha.say "And even if you don't love me back, I wondered if..."
    sasha.say "If you wanted to go steady with me or something?"
    sasha.say "You know, like, make things official between us?"
    show sasha normal
    menu:
        "I feel the same":
            "I'm still reeling from Sasha's confession when she asks the question."
            "But I can already feel myself nodding, even before I manage to speak."
            bree.say "Yeah, Sasha..."
            bree.say "I think I'd like that..."
            bree.say "I'd like it quite a lot!"
            "I'm expecting Sasha to say that she's pleased with my answer."
            "Or even to just manage a smile and a squeal of delight."
            hide sasha
            show sasha kiss
            with hpunch
            $ sasha.flags.kiss += 1
            "But instead she leaps forwards and plants her lips on mine."
            "The kiss takes me by complete surprise."
            "Meaning that I end up standing there like a fool at first."
            "But then I begin to loosen up and return the affection Sasha's showing me."
            "Though all the time my mind's racing, trying to come to terms with what just happened."
            "Sasha asked me to be her girlfriend, which is crazy."
            "But what's even crazier is that I said yes!"
            hide sasha kiss
            $ sasha.set_girlfriend()
            $ sasha.flags.nobreakup = False
        "I need some time":
            "I'm still reeling from Sasha's confession when she asks the question."
            "But I can already feel myself shaking my head, even before I manage to speak."
            bree.say "No, Sasha..."
            bree.say "I can't do that..."
            show sasha sad
            bree.say "At least not yet."
            $ sasha.love -= 10
            "Sasha looks understandably devastated at my answer."
            "And why wouldn't she?"
            "The girl just opened herself up to me completely."
            "She put her heart into my hands, and I just dropped it on the ground!"
            show sasha whining
            sasha.say "But why not, [hero.name]?"
            sasha.say "Don't you feel the same way about me?"
            show sasha sad
            bree.say "I like you a lot, Sasha..."
            bree.say "Like, to a crazy degree..."
            bree.say "But it just doesn't feel like real love, not yet!"
            bree.say "Could...could we just give it a little more time?"
            "Sasha nods, doing the best she can to hide her hurt feelings."
            "And that's how I have to accept that we're leaving things."
            "With her disappointed at being turned down."
            "And me feeling guilty that I'm not quite on the same page as her."
    $ game.flags.sasha_delay_female = TemporaryFlag(True, 1)
    return

label sasha_female_ending:
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding with fade
    "After all of the hours, days, weeks and even months of planning, it's finally happening."
    "The big day is here, the day on which Sasha and I are finally going to tie the knot."
    "The chapel is full to bursting with all of the guests that we've invited along."
    "The music that we picked out is beginning to play over the PA."
    "And the both of us are wearing the outfits we decided on for the ceremony."
    "But unlike most traditional weddings, neither of us is standing at the altar right now."
    "Instead we're waiting with baited breath for the chapel doors to open and let us in."
    "And that's because neither of us was going to be the one to stand alone at the altar."
    "Or the one walking alone down the aisle to join them either!"
    "No, Sasha and I talked it through."
    "And we came to the conclusion that we're equals in this relationship."
    "So we wanted the ceremony to reflect that fact."
    "But right now, I'm staring at those doors like I have laser-vision."
    "Like I want to burn straight through them as the nerves are starting to get to me."
    "And that's about the time I feel someone taking hold of my hand."
    show sasha wedding shy at center, zoomAt(1.5, (640, 1040)) with dissolve
    "Looking down, I see that it's Sasha."
    "But then of course it's her."
    "Who else is standing right beside me, going through everything that I am?"
    "My eyes shoot up to meet Sasha's, and I see that she's smiling."
    "It's one of those wry, knowing smiles that she's so good at pulling off."
    show sasha shout
    sasha.say "So what do you say, [hero.name]?"
    sasha.say "Are you ready to do this thing, or what?"
    show sasha normal
    "I feel myself nodding before I can even get out a single word."
    "And at the same time I find that I'm squeezing Sasha's hand in return."
    bree.say "Of course I do, Sasha!"
    bree.say "I'm kind of scared shitless right now..."
    bree.say "But I really want to do it!"
    show sasha happy
    "Sasha gives me a nod in return, then I see her move her leg."
    show sasha normal with hpunch
    "And without hesitation, she literally kicks open the chapel doors!"
    "I don't know if anyone sees her doing it, and I don't have time to react."
    "Because the moment the doors swing open, Sasha strides forwards."
    "She's still holding my hand as tightly as ever, so I don't have a choice."
    "It's either follow her in there, or else yank her backwards!"
    "So I choose the former, and we both stride into the chapel together."
    "I think that I recognise some of the face that pass by me."
    "But most of the trip down the aisle is a total blur."
    "And the world doesn't come back into focus until we're at the altar."
    if hero.is_visibly_pregnant:
        "In fact I'm so engrossed in what we're doing I almost forget to hold onto my belly."
        "But thankfully the way that my dress has been cut is sympathetic to the bulging shape."
        "So I feel supported the entire time we're walking down the aisle."
    else:
        "More than once I'm sure that I'm going to trip and fall."
        "But somehow I manage to stay on my feet the entire way down the aisle."
    show wedding sasha priest with fade
    "The priest is standing there, looking like he has all the patience in the world."
    "Though as soon as we come to a halt before him, the guy springs into action."
    "Priest" "Now that we're all here..."
    "Priest" "Shall we begin?"
    "At this, Sasha and I begin nodding and scurrying around."
    "Both trying to get into position without tripping over each other."
    "And once we're on our allotted spots, we're all set to go."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join these two people in the bonds of holy matrimony."
    "And just like that, we're off and into it."
    "The priest rattles off the familiar lines of the ceremony."
    "And everything goes just as smoothly as it did in all of the rehearsals."
    "The only difference is that this time it's for real!"
    "Before I know it, we get to the vows."
    "Priest" "Do you, Sasha..."
    "Priest" "Take bree..."
    "Priest" "To be your lawful, wedded partner?"
    "Sasha shoots me another one of those smiles."
    "Then she turns her attention back to the priest."
    sasha.say "Of course I do."
    "The priest nods with evident satisfaction."
    "And then he turns to address me."
    "Priest" "And to you, [hero.name]..."
    "Priest" "Take Sasha..."
    "Priest" "To be your lawful, wedded partner?"
    "I take a deep breath, thinking that this is going to be a tough thing to say."
    "But as soon as I open my mouth, I find that I don't even pause with my answer."
    bree.say "I do."
    "The priest nods again."
    "And he next turns to address the assembled guests."
    "Priest" "[hero.name] and Sasha have now exchanged their vows."
    "Priest" "So I call on all those here present..."
    "Priest" "That if you know of any lawful reason..."
    "Priest" "That these two many not be joined in matrimony..."
    "Priest" "Speak now, or forever hold your peace!"
    "Of course the guests all chuckle and laugh as we wait for the customary couple of moments."
    "And I know that I should be seeing this as a chance for a light-hearted laugh too."
    "But there's always that lingering worry that my dad's going to make an ass of himself."
    "Or that an ex-boyfriend is going to come storming into the chapel and make a scene."
    "Priest" "I'll take that as a no then!"
    "Finally I feel like I can breathe again."
    "Priest" "And therefore it gives me great pleasure to pronounce you married."
    "Priest" "You may celebrate in a way you feel is fitting."
    show wedding sasha -priest with dissolve
    "Sasha and I don't need any more encouragement than that."
    "Within a moment we're wrapped in each others arms."
    scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
    show sasha kiss wedding
    with fade
    "And then our lips are pressed together."
    "So that our tongues are wrapped around each other too."
    "Neither of us seems to feel the need to say a word."
    "We simply express ourselves in the moment."
    "Living for the now, secure in the knowledge we have tomorrow ahead of us."

    scene sasha female ending
    with fade
    sasha.say "So this is where I get to speak up for myself, huh?"
    sasha.say "Share my side of the story instead of [hero.name]?"
    sasha.say "Okay, so are you ready for some seriously juicy confessions and revelations?"
    sasha.say "Nah, only kidding!"
    sasha.say "Being with [hero.name]'s turning out to be a pretty sweet deal."
    sasha.say "And I don't have any major complaints beyond her snoring and hogging the duvet!"
    sasha.say "But I'm still kinda amazed that [hero.name] and I was even a thing that happened."
    sasha.say "Back when we first moved into the house with [mike.name], everything was so different."
    sasha.say "I didn't even know if I was going to be able to live alongside [hero.name]."
    sasha.say "Let alone have any kind of relationship with her."
    sasha.say "Yeah, I know that sounds totally crazy now."
    sasha.say "But hear me out, okay?"
    sasha.say "I'm a metal-chick, into playing my guitar so loud it'd make your ears bleed."
    sasha.say "And in walks this cutesy blonde girl, into her videogames and all that stuff."
    sasha.say "Not someone I'd expect to click with from the word go."
    sasha.say "But I decided that I was going to give her a chance, to get to know her."
    sasha.say "And it didn't take long for the three of us to become pretty good friends."
    sasha.say "At first that's all it was between [hero.name] and myself."
    sasha.say "I thought of her in the same way that I did [mike.name]."
    sasha.say "We all hung out around the house, and we went to the pub together too."
    sasha.say "But soon I found myself doing things with [hero.name] when [mike.name] wasn't there."
    sasha.say "In the end it felt like we were spending most of our free time together."
    sasha.say "And those trips to the pub or the movies slowly kind of mutated into dates."
    sasha.say "I don't know if there was ever a point where we made it totally official."
    sasha.say "If there was, then I don't remember it."
    sasha.say "Our relationship just grew like that, totally organically."
    sasha.say "So before he knew it, poor old [mike.name] was living with a couple!"
    sasha.say "I was awkward, but we all made the effort to get on like we did before."
    sasha.say "But when [hero.name] and I decided to go totally crazy and get married..."
    sasha.say "Well, that was when we knew that something had to change."
    sasha.say "So we moved out and into a place of our own."
    sasha.say "Leaving [mike.name] behind was hard, as we were all still good friends."
    sasha.say "Doubly so thanks to him now being left there on his own."
    sasha.say "But we still keep in contact and hang-out whenever we can."
    sasha.say "And I hear that he's got two new girls moved in with him now."
    sasha.say "So maybe this time round he'll be the one to get lucky?"
    if hero.is_visibly_pregnant:
        sasha.say "Not that we get much free time with little Johnny running us both ragged!"
        sasha.say "Even with two mommies to look after him, that kid's still a handful."
        sasha.say "But then I guess that [hero.name] must have been like that when she was a girl too."
        sasha.say "I'll have to remember to ask her dad all about that the next time he's over to visit..."
    else:
        sasha.say "Not that we get that much free time, what with us both working so hard."
        sasha.say "Though I always feel like [hero.name]'s dropping hints that we should think about kids."
        sasha.say "Giving me subtle signs that she's getting broody and wants a family."
        sasha.say "But I'm not quite sure how I feel about that yet."
    sasha.say "Needless to say that [hero.name] aced all of her exams."
    sasha.say "Then she went and bagged herself a sweet job as a biologist."
    sasha.say "I don't pretend to understand half of what she does at work."
    sasha.say "But it always sounds really impressive when she talks about it."
    sasha.say "And I owe her a hell of a lot for supporting me with the band."
    sasha.say "There was a time back there when she was paying all the bills."
    sasha.say "While me and the girls in The Deathless Harpies were giving it our best shot."
    sasha.say "But in the end I made the choice to leave the band, as we weren't getting anywhere."
    sasha.say "Anna and Kleio are still out there, performing gigs and trying to make it."
    sasha.say "They recruited a new guitarist and they send me their new stuff to listen to."
    sasha.say "But don't think that I hung up my own guitar when I left."
    sasha.say "I put all of that practise to good use, and now I'm a guitar coach."
    sasha.say "So I get to pass on my skills to a new generation of musicians."
    sasha.say "I think that about covers it all, you know?"
    sasha.say "Where [hero.name] and I started out to where we are right now."
    sasha.say "We might not have taken over the world or be rich and famous."
    sasha.say "But we're doing pretty damn well for ourselves."
    sasha.say "And when I think about what the future holds, I get really excited."
    sasha.say "Because I can only see things getting better for us from now on."
    scene bg black with dissolve
    pause 1.0
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label sasha_female_beach_date_event_01:
    $ renpy.dynamic(sashatopless=False)
    scene bg beach
    "It's the kind of day where it'd be criminal to stay cooped up inside."
    "So Sasha and I decide to take a drive out to the beach together."
    "We were overdue going on a date together, so this should do just fine."
    "And sure enough, when we arrive at the beach, the place is alive."
    "Everywhere I look, there are people sunbathing, swimming or just hanging out."
    show sasha surprised at right with easeinright
    sasha.say "Ooh..."
    show sasha annoyed
    sasha.say "It looks really busy down there!"
    show fx question
    sasha.say "Are you sure about this, [hero.name]?"
    "Sasha's question kind of catches me off guard."
    "I thought she was as up for this as I was."
    "I mean, she sounded like she was all the way here."
    "And the beach doesn't look full up to me, just busy."
    "Is there something else going on here?"
    "Is Sasha worried about being seen on the beach with me?"
    "That thought is all it takes to spur me into action."
    "If Sasha's lacking in confidence, then I'll show enough for the both of us!"
    show sasha surprised at center, zoomAt(1.5, (880, 1040))
    "I reach over and take hold of Sasha's hand."
    bree.say "Yes, Sasha."
    bree.say "I'm sure about this."
    bree.say "There's nobody I want to be here with more than you!"
    show sasha happy
    "Sasha smiles and nods, beginning to look a little more confident."
    "So I set off, striding towards the dunes and pulling her after me."
    show sasha normal at center, zoomAt(1.5, (640, 1040)) with ease
    "Soon enough I feel Sasha catch up to me and start keeping pace."
    "Her hand grips mine more tightly too, which makes me smile."
    "It's almost like I can feel the confidence growing in her the whole time."
    "We find a pretty decent spot, towards the less crowded end of the beach."
    "Throwing our towels down on the sand, we claim it as our own."
    "I look around for a moment, surveying the beach around us."
    bree.say "Wow..."
    bree.say "There sure are a lot of people looking in this direction all of a sudden!"
    bree.say "What do you think's got them so interested, Sasha?"
    show sasha surprised
    "Sasha looks at me with raised eyebrows."
    show sasha happy at startle
    "Then she chuckles and shakes her head."
    sasha.say "Like you don't know, [hero.name]!"
    show sasha joke
    sasha.say "They're looking at two really hot babes."
    sasha.say "A couple of girls that walked around holding hands."
    sasha.say "So it's pretty obvious they're an item!"
    show sasha normal
    "I glance around for a moment, trying to see who Sasha means."
    bree.say "Huh?"
    bree.say "Where?"
    "But then it hits me."
    bree.say "Oh..."
    bree.say "You mean us, don't you?"
    show sasha happy at startle
    "Sasha laughs and rolls her eyes."
    show sasha joke
    sasha.say "You were the one who insisted we walk down here hand-in-hand!"
    show sasha shout
    sasha.say "Times are changing fast, [hero.name], that's for sure."
    sasha.say "But a same-sex couple is still gonna get attention."
    sasha.say "Especially when they're hot girls!"
    show sasha flirt
    sasha.say "The question is, what are we gonna do about it, huh?"
    show sasha normal
    "From the way Sasha's looking at me right now, I know exactly what she means."
    "It was me that got us into this mess, so I'm going to have to get us out of it!"
    "But how?"
    if hero.morality >= 25:
        "I can already feel my cheeks flushing red with embarrassment."
        "What was I thinking being so brazen just now?"
        "I've got the entire beach staring at Sasha and me."
        "I've turned us into some kind of spectacle for them to gawp at!"
        show sasha surprised at center, zoomAt(1.5, (640, 1140)) with move
        pause 0.2
        with vpunch
        "I sit down as quickly as I can, pulling Sasha with me as I do so."
        sasha.say "Whoa..."
        sasha.say "Hey, [hero.name]..."
        sasha.say "Settle down!"
        show sasha normal
        "Despite Sasha's protests, I don't stop until she sits down too."
        "Only then do I try to explain myself to her."
        bree.say "I'm so sorry, Sasha!"
        bree.say "I had no idea!"
        show sasha shout
        sasha.say "It's okay, [hero.name] - let them stare."
        sasha.say "I don't care what any of them think."
        sasha.say "And neither should you."
        sasha.say "We're just here to have a great day at the beach, like everyone else!"
        show sasha normal
        "I find myself smiling, despite the embarrassment I'm still feeling."
        "Somehow, knowing that Sasha doesn't care gives me strength."
        $ sasha.love += 1
        $ hero.morality += 1
    elif 0 <= hero.morality < 25:
        "I look around in amazement, feeling my cheeks begin to flush red."
        "But then I shake my head, remembering that we live in the twenty-first century."
        "So what if all of those people want to look at Sasha and me."
        "That's no reason for me to be embarrassed to be seen with her."
        "Either they're checking us out, which is flattering."
        "Or else they've got a problem, which is...well, their problem!"
        bree.say "Why should we do anything about it, Sasha?"
        bree.say "All we did was come to the beach to hang out."
        bree.say "It's not our fault we're so gorgeous!"
        show sasha happy at startle
        pause 0.5
        show sasha normal at center, zoomAt(1.5, (640, 1140)) with ease
        "Sasha laughs out loud as she sits down on her towel."
        "I join her and get comfortable on my own."
        show sasha shout
        sasha.say "You're right, [hero.name] - let 'em look if they want to."
        sasha.say "Because that's all anybody else but you's gonna get to do!"
        show sasha normal
        "As if to underline her point, Sasha leans over towards me."
        hide sasha
        show sasha kiss
        with fade
        $ sasha.flags.kiss += 1
        "Then she kisses me, full on the mouth."
        "It's not a long kiss, nor is it a particularly sensual one."
        hide sasha kiss
        show sasha normal at center, zoomAt(1.5, (640, 1140))
        with fade
        "In fact, I doubt most people see it at all."
        "But maybe that's the point Sasha's making."
        "Who cares what anybody else sees or thinks?"
        "As long as we like it, that's all that matters."
        $ sasha.love += 1
    elif -25 <= hero.morality < 0:
        "I look around for a moment, seeing that Sasha's dead right."
        "There are more than a few people looking at us with curiosity."
        "But it's not like that kind of thing's going to bother me."
        "In fact, it's probably a compliment that they're doing it at all."
        bree.say "Let them stare if they want to, Sasha."
        bree.say "It's a free country!"
        show sasha surprised at center, zoomAt(1.5, (640, 1140)) with ease
        "I put a hand on her wrist and pull her down with me."
        "Sasha settles on her towel and I sit on mine."
        "But I make no effort to let go of her hand once we're sitting down."
        "Instead I put my other hand on the back of Sasha's neck."
        "And I draw her towards me."
        sasha.say "W...what are you doing?"
        bree.say "Giving them something to stare at of course!"
        hide sasha
        show sasha kiss
        with fade
        $ sasha.flags.kiss += 1
        "With that, I kiss Sasha, full on the mouth."
        "I make sure to use my tongue too, turning it into a passionate affair."
        "I have my eyes closed, so I've no idea how many people on the beach see us."
        "But I can feel the way Sasha melts into the kiss, unable to resist."
        hide sasha kiss
        show sasha flirt at center, zoomAt(1.5, (640, 1140))
        with fade
        "And that's what makes the whole thing worth it."
        $ sasha.sub += 1
    elif hero.morality < -25:
        "I look around for a moment, seeing that Sasha's dead right."
        "There are more than a few people looking at us with curiosity."
        "I can't help laughing at the sight of them, at how pathetic they are."
        "Every one of them is trying to stare at us while making it look like they're not!"
        bree.say "Geez..."
        bree.say "Can you believe these sad cases?"
        bree.say "Come here, Sasha..."
        "I take hold of Sasha's wrist again, pulling her towards me."
        show sasha surprised at center, zoomAt(2.0, (640, 1340))
        "She's jerked the short distance between us."
        "And then she finds herself pressed against me."
        sasha.say "W...what are you doing, [hero.name]?"
        bree.say "I'm giving them something to stare at!"
        hide sasha
        show sasha kiss
        with fade
        $ sasha.flags.kiss += 1
        "With that, I kiss Sasha, full on the mouth."
        "I make sure to use my tongue too, turning it into a passionate affair."
        "I have my eyes closed, but I know that almost everybody on the beach can see us."
        "And I can feel the way Sasha melts into the kiss, unable to resist."
        "Which is what makes the whole thing worth it."
        hide sasha kiss
        show sasha dazed at center, zoomAt(1.5, (640, 1140))
        with fade
        "After that, we sit down on our towels."
        "Sasha still looks more than a little flustered."
        "But I'm feeling fine, because I got to make my point."
        $ sasha.sub += 1
        $ hero.morality -= 1
    "Things seem to quiet down after that and people start to lose interest in us."
    "That means I can finally relax and let this turn into a real date at the beach."
    show sasha normal
    "Just Sasha and me, laying on the sand and soaking up the rays."
    "Well, not all of them, of course!"
    "We're a little in the shade and both of us are wearing sunscreen."
    "There's no point in paying for all of our fun with sunburn later on!"
    "In fact, it's so warm and pleasant on the beach right now."
    "The sound of the sea is so soothing, almost like a lullaby."
    scene bg beach at blur(16), dark, dark with wipedown
    "I actually think I might...fall...asleep..."
    sasha.say "Hey, [hero.name]!" with vpunch
    bree.say "Huh..."
    bree.say "Wha..."
    bree.say "What?!?"
    scene bg beach
    show sasha shout at center, zoomAt(1.5, (640, 1040))
    with wipeup
    sasha.say "Will you wake up already?"
    sasha.say "You were snoring like a pig!"
    show sasha normal
    bree.say "Hey - I do not snore!"
    show sasha happy at startle
    "Sasha sniggers at my flat denial and shakes her head."
    show sasha shout
    sasha.say "How'd you know you don't snore?"
    sasha.say "You're asleep when it happens, dummy!"
    sasha.say "Anyway, forget that..."
    show sasha joke
    sasha.say "Make yourself useful and run some sunscreen on me, yeah?"
    sasha.say "It's been ages since I put this lot on and it's wearing off!"
    show sasha normal
    "Sasha thrusts the sunscreen into my hands and rolls onto her belly."
    show beach cream sasha nomc at center, zoomAt (1.25, (740, 740)) with fade
    "Then she looks up at me and waves a hand at her back."
    sasha.say "Come on - what are you waiting for?"
    if hero.morality >= 25:
        "Instantly horrified at the very idea, I push the sunscreen away."
        "We've already had the entire beach staring at us once today."
        "So the sight of me rubbing that stuff into her skin would be the same thing all over again!"
        "Sasha frowns and tries to thrust the sunscreen at me again."
        sasha.say "Come on, [hero.name]!"
        sasha.say "I need a hand here!"
        bree.say "Well you didn't need a hand when you put the first lot on, Sasha."
        bree.say "You seemed to be pretty happy with the job you did that time."
        hide beach cream sasha
        show sasha stuned at center, zoomAt(1.5, (640, 1040))
        with fade
        "Sasha looks more than a little confused."
        show sasha surprised
        sasha.say "Yeah, I know that."
        sasha.say "But I thought you might like to..."
        show sasha stuned
        bree.say "No, Sasha - I really think you should do it yourself."
        bree.say "I...I might miss a bit, you know?"
        bree.say "And it's like how people parachuting always prepare their own parachutes, right?"
        show sasha whining
        sasha.say "Erm...no, [hero.name], I don't think so!"
        show sasha shout
        sasha.say "But if that's the way you feel, then fine - I'll do it myself."
        show sasha normal
        "I take a deep breath, relived to have avoided another potential crisis."
        "And then it occurs to me, I should probably reapply my own sunscreen too!"
        $ sasha.love += 2
    elif 0 <= hero.morality < 25:
        "I take the sunscreen from Sasha before I've really thought it through."
        "But then I remember everyone staring when we first got here."
        "I hope I'm not about to give them something else to stare at!"
        sasha.say "Come on, [hero.name]!"
        sasha.say "I need a hand here!"
        "But then I snap out of it and squeeze out the sunscreen."
        "After all, who's going to see Sasha when she's laid out flat on the sand?"
        "All they're going to see is someone rubbing sunscreen into someone else's back."

        bree.say "Get ready, Sasha."
        bree.say "This stuff's freezing!"
        "I spend the next few minutes rubbing the sunscreen into Sasha's skin."
        "And she really seems to be grateful, making appreciative noises the whole time."
        "Pretty soon I'm enjoying myself too, tracing the lines of her body with my hands."
        "Once it's over, I have to say that I'm disappointed, as I was having a good time."
        bree.say "There you go, Sasha - all done!"
        hide beach cream sasha
        show sasha happy
        with fade
        sasha.say "Thanks, [hero.name]."
        sasha.say "Now lie down and I'll do you, okay?"
        show sasha stuned
        "I do as I'm told, surrendering myself to Sasha's ministrations."
        show beach cream bree nomc with fade
        "And for the next ten minutes or so, I get the other side of the experience."
        "By the time Sasha's done returning the favour, I feel more relaxed than ever."
        hide beach cream bree
        show sasha happy
        with fade
        "I may never put my own sunscreen on again."
        $ sasha.love += 1
    elif -25 <= hero.morality < 0:
        "I take the sunscreen from Sasha, a smile already forming on my face as I do so."
        "Sure, anybody on the beach might see me doing this, but who cares?"
        "Sasha and I came here to have a good time together."
        "And I know how to make even this a part of that!"
        sasha.say "Come on, [hero.name]!"
        sasha.say "I need a hand here!"
        bree.say "Oh, don't worry, Sasha."
        bree.say "I'll give you more than one hand!"

        "I squeeze the sunscreen onto my hands and prepare myself."
        "And then I spend the next few minutes rubbing it into Sasha's skin."
        "Well, kind of - it's more like I turn it into a sensual massage!"
        "Sasha seems to catch onto what I'm doing pretty quickly."
        "But soon enough she's caught in my little trap, and can't escape."
        "Sasha moans and groans the whole time I'm rubbing it in."
        "I'm enjoying myself too, tracing the lines of her body with my hands."
        "By the time I'm done, Sasha seems pretty hot and bothered."
        "But I'm disappointed, as I was having a good time."
        hide beach cream sasha
        show sasha shy
        with fade
        bree.say "There you go, Sasha - all done!"
        show sasha flirt
        sasha.say "Th...thanks, [hero.name]."
        sasha.say "Now lie down and I'll do you, okay?"
        show sasha shy
        "I do as I'm told, surrendering myself to Sasha's ministrations."
        show beach cream bree nomc at center, zoomAt (1.25, (760, 720)) with fade
        "And for the next ten minutes or so, I get the other side of the experience."
        "By the time Sasha's done returning the favour, I feel more relaxed than ever."
        hide beach cream bree
        show sasha normal
        with fade
        "I may never put my own sunscreen on again."
        $ sasha.love += 2
    elif hero.morality < -25:
        "I take the sunscreen from Sasha, a smile already forming on my face as I do so."
        "Sure, anybody on the beach might see me doing this, but who cares?"
        "Sasha and I came here to have a good time together."
        "And I know how to make even this a part of that!"
        sasha.say "Come on, [hero.name]!"
        sasha.say "I need a hand here!"
        bree.say "Oh, don't worry, Sasha."
        bree.say "I'll give you more than one hand!"

        "I squeeze the sunscreen onto my hands and prepare myself."
        "And then I spend the next few minutes rubbing it into Sasha's skin."
        "Well, kind of - it's more like I turn it into a sensual massage!"
        "Sasha seems to catch onto what I'm doing pretty quickly."
        "But soon enough she's caught in my little trap, and can't escape."
        "Sasha moans and groans the whole time I'm rubbing it in."
        "I'm enjoying myself too, tracing the lines of her body with my hands."
        "By the time I'm done rubbing it into her back, Sasha seems pretty hot and bothered."
        "It's then that I deftly pull down the straps of her bikini top."

        sasha.say "...[hero.name]!"
        sasha.say "What are you doing?"
        bree.say "I did your back already."
        bree.say "Now I need to do your front too!"
        "For a moment, I think Sasha's actually going to say no."
        "I raise a single, quizzical eyebrow, as if daring her to do it."
        "Sasha nods and does as she's told, rolling onto her back."
        "She holds onto her top as she does so."
        "But I tug it off the moment she's laid face-up."
        "And I don't give her a chance to back down either."
        "Fresh suncream on my hands, I repeat the process on Sasha's front."
        "Working my way up from her feet, it's pretty much like her back was."
        "It's only when I reach her belly and start approaching her breasts that the mood changes."
        "I can hear Sasha almost panting in anticipation, until the moment I touch them."
        "The she begins to sigh as I gently massage the sunscreen into her breasts."
        "I make it slow and sensual, savouring every moment it takes."
        hide beach cream sasha
        show sasha shy topless
        "And when I'm done, Sasha doesn't even try to reach for her bikini top."
        "Instead she just lies there, letting the sun soak into her half-naked body."
        $ sasha.love += 1
        $ sasha.sub += 1
        $ sashatopless = True
    "Once we're all slathered in sunscreen, it's back to lazing on the sand."
    "And this time it's not just me that's baking like a lizard in the sun."
    "More then once I sit up and look over at Sasha, thinking we might do something fun."
    "Like, I don't know, get an ice-cream or go for a walk in the sea."
    "But every time I do, she has her eyes closed and looks like she's asleep."
    "At first I think she's just pretending, but then I hear her start snoring."
    "Never mind a pig - Sasha sounds like a warthog with a head-cold!"
    "And to think, she had the cheek to accuse me of snoring loudly!"
    "I seem to drift in and out of sleeping and waking."
    hide sasha
    show bg black with dissolve
    "Until I feel someone shaking me out of my slumber."
    sasha.say "[hero.name]..."
    sasha.say "Hey, [hero.name]!" with vpunch
    show bg beach with dissolve
    show sasha normal at center, zoomAt(1.5, (640, 1040))
    if sashatopless:
        show sasha normal topless
    bree.say "Wha...what is it?"
    bree.say "I wasn't snoring, I swear!"
    show sasha shout
    sasha.say "Forget about that, [hero.name]!"
    sasha.say "Take a look around."
    scene bg beach with fade
    "I sit up, a little groggily at first, trying to see what Sasha's talking about."
    "And then I see that there's nobody else around on the beach, just the two of us."
    bree.say "Huh?"
    bree.say "Where did everybody go?"
    bree.say "It can't be that late, can it?"
    show sasha normal at center, zoomAt(1.5, (640, 1040))
    if sashatopless:
        show sasha normal topless
    "Sasha holds up her phone to show me the actual time."
    show sasha shout
    sasha.say "I don't know, [hero.name] - it's pretty late in the day."
    sasha.say "Looks like most people already packed up and went home."
    show sasha normal
    bree.say "Hmm..."
    bree.say "Maybe that's what we should do too?"
    show sasha annoyed
    "Sasha looks at me sideways, shaking her head."
    sasha.say "Are you actually crazy?"
    show sasha shout
    if sashatopless:
        show sasha shout topless
    sasha.say "We have the entire beach to ourselves!"
    sasha.say "It's like we're the last two people left alive in the planet."
    sasha.say "And we can do whatever the hell we want!"
    show sasha normal
    bree.say "And just what is that, pray tell?"
    hide sasha
    show sasha
    "Sasha smiles as she hauls herself up and stretches."
    show sasha flirt
    if sashatopless:
        "Then she starts to take off her bikini bottom."
    else:
        show sasha topless
        "Then she starts to take off her bikini top."
    sasha.say "To get naked with my girlfriend on the beach - what else!"
    if hero.morality >= 25:
        "My hands shoot out before Sasha even has a chance to reach the fabric."
        show sasha at center, zoomAt(1.5, (640, 1040))
        "And she stops more out of surprise than me holding her arms still."
        show sasha stuned at startle
        bree.say "WHOA!"
        bree.say "Just...just wait a minute there, okay?"
        show sasha surprised
        sasha.say "What's the problem, [hero.name]?"
        show sasha whining
        sasha.say "There isn't another soul here!"
        show sasha annoyed
        "Sasha makes a good point, there isn't."
        "So I have to come up with a reason that doesn't involve anyone seeing us."
        "And I have to do it fast."
        "Which is why my mouth starts moving before my brain starts thinking."
        bree.say "Because..."
        bree.say "Because I want to save my energy..."
        bree.say "For when we...get home!"
        bree.say "That's it - I want to save my energy for when we get home!"
        show sasha normal
        "Sasha looks at me for a moment, like she's about to call me on my bullshit."
        show sasha flirt
        "But then she gives me a sly wink and nods, taking her hands off her straps."
        show sasha shout
        sasha.say "Is that so?"
        sasha.say "I bet you've been cooking up ideas all day, huh?"
        sasha.say "Well, come on then - what are we waiting for?"
        show sasha happy
        sasha.say "Let's get back there and make it all happen!"
        show sasha normal
        "I nod, trying not to look concerned as we gather up our things."
        "I have the time it takes to walk to the car and drive home."
        "Who knows, I might actually be able to come up with something before we make it back..."
        $ sasha.love += 1
        $ hero.morality += 1
    elif 0 <= hero.morality < 25:
        "I shrug my shoulders and then make to follow Sasha's example."
        show sasha naked
        "After all, why the hell not?"
        "There's nobody else here and it sounds like fun."
        "I've barely got my bikini off before Sasha pounces on me from behind."
        hide sasha
        show sasha female foreplay naked
        with fade
        "I yelp, but then let out a giggle of excitement as I feel her hands touching me."
        sasha.say "Mmm..."
        sasha.say "I wish every trip to the beach ended like this."
        "Sasha's fingers dance over my body as she says this."
        "I feel them stroking, brushing, caressing."
        bree.say "Me too, Sasha!"
        bree.say "Me too..."
        bree.say "Oh god..."
        "Just then I feel Sasha begin to caress my naked breasts."
        "She starts out gently, but then adds more force to her touch."
        bree.say "Oh yeah..."
        bree.say "That feels good!"
        "I turn my head back to look at Sasha."
        show sasha kiss naked with fade
        $ sasha.flags.kiss += 1
        "And she takes the chance to kiss me with a passion."
        "All I can think about while this is happening is that I want more."
        "At this rate, I'm going to be helpless to resist within mere moments."
        "The second the kiss breaks, I gasp for air."
        hide sasha kiss naked
        show sasha dazed at center, zoomAt(1.5, (640, 1040))
        with fade
        bree.say "S...Sasha..."
        bree.say "Let's go back..."
        bree.say "Finish this off there..."
        "Sasha's panting too, but she soon starts nodding in agreement."
        show sasha shout
        sasha.say "Come on - what are we waiting for?"
        sasha.say "Let's get back there and make it happen!"
        show sasha normal
        "I nod as we hurry to gather up our things."
        "I have no idea just what we're going to do when we get back."
        "But it's going to be fun finding out."
        $ sasha.love += 2
        $ sasha.sub += 1
    elif -25 <= hero.morality < 0:
        "I shrug my shoulders and then make to follow Sasha's example."
        show sasha naked
        "After all, why the hell not?"
        "There's nobody else here and it sounds like fun."
        "I've barely got my bikini off before Sasha pounces on me from behind."
        hide sasha
        show sasha female foreplay naked
        with fade
        "I yelp, but then let out a giggle of excitement as I feel her hands touching me."
        sasha.say "Mmm..."
        sasha.say "I wish every trip to the beach ended like this."
        "Sasha's fingers dance over my body as she says this."
        "I feel them stroking, brushing, caressing."
        bree.say "Me too, Sasha!"
        bree.say "Me too..."
        bree.say "Oh god..."
        "Just then I feel Sasha begin to caress my naked breasts."
        "She starts out gently, but then adds more force to her touch."
        bree.say "Oh yeah..."
        bree.say "That feels good!"
        "I turn my head back to look at Sasha."
        "And she takes the chance to kiss me with a passion."
        "All I can think about while this is happening is that I want more."
        "As if reading my mind, Sasha reaches down with one of her hands."
        "I feel it slide between my thighs, finding my pussy with ease."
        "And then she's massaging it with her fingers."
        "Sasha's touch is expert, hitting every spot where I need it."
        "All I can do is lie back in her arms, letting her have her way with me."
        "It doesn't take long for her to work me up to a peak."
        "The orgasm that follows spreading out to grip my entire body."
        "I'm helpless as I cum, quivering in her arms the whole time."
        "Sasha holds me until it's all over, making sure her work is done."
        $ sasha.sub += 1
        $ hero.morality -= 1
    elif hero.morality < -25:
        "I shrug my shoulders and then make to follow Sasha's example."
        show sasha naked
        "After all, why the hell not?"
        "There's nobody else here and it sounds like fun."
        "I've barely got my bikini off before Sasha pounces on me from behind."
        hide sasha
        show sasha female foreplay naked
        with fade
        "I yelp, but then let out a giggle of excitement as I feel her hands touching me."
        sasha.say "Mmm..."
        sasha.say "I wish every trip to the beach ended like this."
        "Sasha's fingers dance over my body as she says this."
        "I feel them stroking, brushing, caressing."
        bree.say "Me too, Sasha!"
        bree.say "Me too..."
        bree.say "Oh god..."
        "Just then I feel Sasha begin to caress my naked breasts."
        "She starts out gently, but then adds more force to her touch."
        bree.say "Oh yeah..."
        bree.say "That feels good!"
        "I turn my head back to look at Sasha."
        "And she takes the chance to kiss me with a passion."
        "All I can think about while this is happening is that I want more."
        "That's when I reach behind me with one hand."
        "I push it between Sasha's legs, finding her pussy."
        "And I begin to stroke it, going faster with each passing second."
        "Sasha whimpers and quivers, but she doesn't tell me to stop."
        "As if reading my mind, she reaches down with one of her own hands."
        "I feel it slide between my thighs and over my pussy with ease."
        "And then she's massaging it with her fingers."
        "Sasha's touch is expert, hitting every spot where I need it."
        "Together we each work the other to a peak."
        "And we cum at the exact same moment too."
        "I'm helpless as my climax, quivering in Sasha's arms the whole time."
        "Sasha clings to me until it's all over and our work is done."
        $ hero.morality -= 1
    $ sasha.lesbian += 2
    $ game.active_date.score += 50
    $ game.pass_time(4, True)
    $ hero.replace_activity()
    scene bg black with dissolve
    return

label sasha_clothesshop_coworker_01:
    scene bg clothesshop with fade
    "I've been restocking the racks for most of my shift at the clothes store."
    "So most of the time I haven't been paying much attention to anything else."
    "The only other member of staff on duty at the moment is Sasha."
    "But she's on the sales counter, so we don't have any reason to interact."
    "At least I thought we didn't, until I look up to see her hurrying over."
    show sasha whining with easeinleft
    sasha.say "[hero.name]..."
    sasha.say "Hey, [hero.name]!"
    show sasha sad
    "I put down what I'm doing and turn towards my co-worker."
    "And it's only when I do so that I see Sasha has something in her hand."
    bree.say "What's the matter, Sasha?"
    bree.say "You sound a little flustered!"
    "Sasha chooses that moment to thrust the thing in her hand towards me."
    "And now I see that it's a purse."
    "Or to be more accurate, it's a really nice purse."
    "One that looks designer and very expensive."
    "And not to knock Sasha, but also one that she wouldn't own herself."
    show sasha whining
    sasha.say "I just served a customer, [hero.name]..."
    sasha.say "And she was buying a load of stuff."
    sasha.say "But when she'd gone, I noticed she left her purse!"
    sasha.say "What should we do?"
    show sasha sad
    menu:
        "Go after the customer":
            bree.say "You're sure it's her purse?"
            show sasha normal
            "Sasha nods."
            show sasha shout
            sasha.say "Totally sure!"
            show sasha normal
            bree.say "Then hand it over and I'll chase after her."
            bree.say "I remember seeing the woman you're talking about."
            bree.say "It was only a couple of minutes ago she was in here."
            bree.say "She can't have gone that far."
            show sasha stuned
            "Sasha doesn't look convinced with my solution."
            show sasha surprised
            sasha.say "Why don't you let me go, [hero.name]?"
            sasha.say "After all, I was the one that served her."
            show sasha stuned
            "I shake my head, dismissing Sasha's suggestion."
            bree.say "No, Sasha..."
            bree.say "We're not really supposed to leave one person minding the store anyway."
            bree.say "And you're the one that's working the cash register as well."
            bree.say "I'm just restocking the rails."
            show sasha normal
            "Sasha nods and hands over the purse."
            show sasha shout
            sasha.say "Okay, [hero.name]..."
            sasha.say "There you go."
            scene bg mall1 with fade
            "I nod as I take the purse, then I hurry out of the store."
            if hero.fitness>= 30:
                "Just like I said, I catch the woman up quickly."
                "And she looks relieved as soon as she sees the purse in my hand."
                "I reunite her with it and then get back to the store as fast as I can."
                $ hero.money += 100
                $ hero.fun += 1
                $ hero.energy -= 1
                scene bg clothesshop with fade
                "With the whole thing sorted, I get on with restocking the rails once more."
            else:
                "Despite all my efforts, I can't catch up with the woman."
                scene bg clothesshop with fade
                "Finally, I return to the store hoping the woman will come back for her purse."
                $ hero.fun -= 1
                $ hero.energy -= 1
        "Tell Sasha to leave the purse under the counter":
            bree.say "The best thing would be to put it under the counter, Sasha."
            bree.say "Chances are she'll realise before too long and come back for it."
            show sasha sad
            "Sasha doesn't seem convinced with my solution."
            "She glances at the entrance to the store and then back at me."
            show sasha whining
            sasha.say "Are you sure, [hero.name]?"
            show sasha shout
            sasha.say "It was only like a couple of minutes ago."
            sasha.say "The woman can't have gotten far."
            sasha.say "So I could probably catch up to her."
            show sasha whining
            sasha.say "You know, if you'd watch the store?"
            show sasha sadsmile
            "I shake my head, dismissing the idea."
            bree.say "We're not supposed to leave the store with just one member of staff."
            bree.say "Plus are you really sure that was the woman's purse?"
            bree.say "If not, you could be handing it over to someone else."
            show sasha annoyed
            "Sasha still doesn't seem convinced."
            "But she shrugs and lets out a sigh."
            show sasha whining
            sasha.say "You really think that's the best idea?"
            show sasha sad
            bree.say "Yes, Sasha, I do."
            bree.say "Just stick it under the desk and wait."
            bree.say "It's for the best, trust me."
            "Reluctantly, Sasha does as I tell her."
            "And I go back to restocking the rails."
            "Happy to have dealt with the situation so quickly."
    $ sasha.love += 2
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    $ game.flags.worked_clothesshop += 1
    return

label sasha_clothesshop_coworker_02:
    scene bg clothesshop with fade
    "I'm just pottering around the store, doing all of the little jobs that need to be handled."
    "But then I hear the sound of raised voices on the other side of the store."
    "And one thing that you learn pretty quickly when working in retail is that that's a bad sound."
    "It's the kind of sound that usually means a customer is seriously pissed-off."
    "And that in turn can only mean bad things for the poor sods working in the store!"
    "Hurrying over to the source of the sound, I find it's coming from the sales desk."
    show sasha annoyed at right
    show violaine at flip, center, blacker
    with dissolve
    "Sasha's behind the desk, taking the brunt of a verbal assault."
    "And on the other side is a customer that's delivering it."
    "Approaching cautiously, I take a deep breath, preparing to interject."
    bree.say "Excuse me..."
    bree.say "I couldn't help overhearing..."
    bree.say "Is there a problem here?"
    show sasha sad
    "As soon as I'm finished speaking, both of them turn to face me."
    "The customer is frowning and waving a bill in front of me."
    "While Sasha looks harassed, but relieved that I've turned up."
    "But of course they both try to speak at the same time."
    "Customer" "Of course there's a problem!"
    "Customer" "This silly bitch just short-changed me!"
    show sasha vangry
    sasha.say "I did not!"
    sasha.say "[hero.name], she's trying to rob the store!"
    show sasha annoyed
    "I hold up my hands, appealing for calm as I step between them."
    "And I can feel my confidence beginning to rise as I do so."
    "Because this is a situation that I've dealt with before."
    bree.say "Okay, okay..."
    bree.say "I think we all need to calm down a little here!"
    bree.say "Mistakes are an easy thing to make when it comes to money."
    bree.say "But luckily we have a way of checking these things out."
    bree.say "Madam..."
    bree.say "You believe you were short-changed?"
    "The customer nods while shooting a mean glance in Sasha's direction."
    "Customer" "That's right!"
    "Customer" "I paid with a twenty."
    "Customer" "And she gave me change for a ten!"
    show sasha vangry
    "Sasha instantly opens her mouth to argue."
    show sasha upset
    "But I hold up my hand again."
    bree.say "And you dispute this, Sasha?"
    show sasha vangry
    sasha.say "You bet I do!"
    sasha.say "I know a twenty from a ten, [hero.name]."
    show sasha upset
    "I nod and then turn back to the customer."
    bree.say "You see that camera right there?"
    "I point to the camera above the desk."
    bree.say "That's there to record everything that goes in and out of the register."
    bree.say "So if you just wait a second, I'll call up the footage."
    bree.say "Then we'll see what denomination of note was exchanged."
    "Suddenly the customer starts to shake her head."
    show violaine at flip, center, blacker, startle
    "Customer" "Oh no..."
    "Customer" "There's no need for that!"
    "Customer" "Not over so small an amount of money!"
    hide violaine
    show violaine at center, blacker
    pause 0.3
    hide violaine with easeoutleft
    "With that, she turns on her heel and hurries out of the store."
    show sasha stuned at center with ease
    "Which leaves Sasha staring after her in amazement."
    show sasha shocked
    sasha.say "So she was lying!"
    sasha.say "Otherwise she'd have stayed to see the footage, right?"
    show sasha stuned
    menu:
        "Laugh it off with Sasha":
            "I nod and smile."
            bree.say "Of course, Sasha..."
            bree.say "People are always trying that kind of thing in here."
            bree.say "But you don't need to argue with them."
            bree.say "Not when you can just pull up the footage, yeah?"
            show sasha normal
            "Now it's Sasha's turn to nod and smile."
            show sasha happy
            sasha.say "I get it, [hero.name]."
            sasha.say "Thanks for the help back there."
            show sasha shout
            sasha.say "Sometimes my temper can get the better of me!"
            show sasha normal
            "It feels pretty good to have come to Sasha's rescue."
            "But hopefully I've also shown her how to deal with things like that in the future."
            "And working with her is going to be easier as a result."
            $ sasha.love += 4
        "Advise Sasha to learn her lesson":
            "I can't help frowning at Sasha and shaking my head."
            bree.say "Of course she was, Sasha."
            bree.say "People are always trying that kind of thing on."
            bree.say "Especially the ones that are loaded!"
            show sasha angry
            "Sasha nods, looking even more pissed."
            show sasha vangry
            sasha.say "So I was right to call her on it?"
            show sasha upset
            bree.say "No, you were not!"
            bree.say "We're not here to get into fights with the customers."
            bree.say "That's why we have cameras all over the store."
            bree.say "We don't argue the toss, Sasha - we just pull up the footage."
            show sasha annoyed
            "Sasha looks more sullen and sulky than ever as I lecture her."
            "But that's no concern of mine."
            "We're coworkers here, not friends."
            "And the sooner she learns how this place works the better!"
            $ sasha.love -= 2
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    $ game.flags.worked_clothesshop += 1
    return

label sasha_clothesshop_coworker_03:
    scene bg clothesshop with fade
    "I hate it when my shift at the clothes store runs through meal times."
    "Because I get really distracted when I'm hungry, and I can't concentrate."
    "This also means that I tend to get pretty hangry at work too."
    "And I end up stomping around the store in a bad mood until I can feed myself."
    "Usually I insist of taking the first break and eating something as soon as possible."
    "So when I feel my stomach rumbling, I know that it's time to leap into action."
    "But first things first - I have to tell Sasha that I'm going on my lunch-break."
    "I wave to get her attention, and then let her know what time it is."
    show sasha with easeinright
    bree.say "Hey, Sasha..."
    show sasha surprised
    sasha.say "Huh?"
    show sasha shout
    sasha.say "What's up, [hero.name]?"
    show sasha normal
    bree.say "Time for lunch!"
    bree.say "I'm just gonna..."
    "Before I can finish what I'm trying to say, Sasha leaps into action."
    show sasha shocked
    sasha.say "Already?"
    show sasha happy
    sasha.say "Okay, [hero.name] - thanks for the reminder."
    sasha.say "I'll be back as soon as I can!"
    hide sasha with easeoutleft
    bree.say "No, Sasha..."
    bree.say "Wait!"
    "My words seem to fall on deaf ears as Sasha rushes straight out of the store."
    "Not only does this leave me holding down the fort on my own, it also pisses me off."
    "So it's pretty much impossible to keep from sinking into a foul mood after that."
    "I spend the time Sasha's out getting lunch stalking about the store."
    "I avoid customers whenever I can manage it."
    "And when I can't, they tend to get pretty shoddy treatment from me."
    "I keep checking the time and working out how long Sasha's been."
    "For all of her promises to be quick, in the end she's gone a rather long time."
    show sasha normal with easeinleft
    "And when she finally does walk back into the store, I see she's carrying some bags."
    "Unfortunately, none of them seem have food inside!"
    show sasha whining
    sasha.say "Urgh..."
    sasha.say "Sorry to be gone so long, [hero.name]."
    sasha.say "I had a bunch of errands to run in my lunch-break."
    sasha.say "And wouldn't you know it, everywhere was crazily busy!"
    show sasha sadsmile
    menu:
        "Ask Sasha to be more considerate next time":
            "I'm almost over the edge in terms of getting hangry right now."
            "But somehow I manage to bite down on it and be nice to Sasha."
            bree.say "I get that you had stuff to do, Sasha."
            bree.say "But normally we discuss who's going to go to lunch first."
            bree.say "And it can be awkward for me, because I get hangry!"
            show sasha sad
            "Sasha seems to realise the error of her ways as I say all of this."
            "And the look on her face is one of genuine embarrassment."
            show sasha whining
            sasha.say "Ah..."
            sasha.say "Sorry, [hero.name]!"
            sasha.say "I'll be sure to ask next time."
            show sasha sad
            "Then she reaches into one of the bags."
            "And the smell of what she pulls out almost makes me weep."
            show sasha shout
            sasha.say "I did stop off at the sandwich shop though."
            sasha.say "And I bought us both some lunch!"
            show sasha normal
            "I could almost hug Sasha right now!"
            "And I have to stop myself simply grabbing the sandwich and devouring it in front of her."
            bree.say "Thanks, Sasha..."
            bree.say "But I'm going to go in the back now."
            bree.say "I need to be alone with my sandwich!"
            show sasha happy
            "Sasha nods and steps aside, letting me hurry off with my prize."
            $ hero.hunger += 3
            $ sasha.love += 4
        "Remind Sasha the right way":
            "By now I'm feeling so hungry and annoyed that there's no hope."
            "I don't think I could be nice to Sasha if my life depended on it."
            "So I can't hold back when it comes to my response."
            bree.say "That really wasn't cool, Sasha."
            bree.say "How you just walked out of here without stopping."
            bree.say "Normally we decide who goes to lunch first between us."
            show sasha whining
            sasha.say "Oh..."
            sasha.say "Sorry, [hero.name]."
            sasha.say "I guess I didn't think."
            show sasha sad
            bree.say "Well maybe you should try that next time?"
            bree.say "Because I'm not nice when I'm hangry!"
            "Sasha frowns and backs away from me as I say all of this."
            show sasha whining
            sasha.say "Yeah..."
            sasha.say "I can see that now!"
            sasha.say "So you might want to do something about that, right?"
            show sasha annoyed
            "I shoot Sasha an annoyed look as I hurry out of the store."
            "And then I'm off, hunting for food like a pissy velociraptor."
            "So woe betide anyone that happens to get between me and food!"
            $ sasha.love -= 2
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    $ game.flags.worked_clothesshop += 1
    return

label sasha_clothesshop_friend_01:
    scene bg clothesshop with fade
    "It's been one of those days at work, the kind where you can't wait for it to end."
    "And yeah, I know what you're thinking before you say it."
    "Working at a clothes store - how hard can that be?"
    "Well take it from me, it's not as easy as you might think."
    "For one thing, you're on your feet for literally hours."
    "And then there's the constant stream of customers to deal with."
    "Believe me, the customer definitely is not always right!"
    "So once the end of my shift is in sight, I start to feel a little hope."
    "All I have to do is hang on in there, just a tiny bit longer."
    "Then I can walk out of this place before I fall flat on my face!"
    "Even better, I know that it's Sasha coming in to take on the next shift."
    "And she's someone I can rely on more than a random co-worker."
    show sasha sad at center, zoomAt(1.0, (640, 720)) with easeinleft
    "So when I see her hurrying into the store, my heart leaps in my chest."
    "Because right now, Sasha represents my freedom!"
    bree.say "Sasha..."
    bree.say "Am I glad too see you!"
    "But the moment she gets close enough to talk, I see that something's wrong."
    "Sasha looks like she's in a state of harassed confusion right now."
    show sasha whining
    sasha.say "Oh..."
    sasha.say "Hey, [hero.name]..."
    sasha.say "I...I need to ask a favour, okay?"
    sasha.say "And it's a pretty big one too."
    show sasha sad
    "I can't help frowning as I listen to Sasha."
    "Because she really doesn't look like she's ready to start her shift."
    "In fact she looks a total mess!"
    bree.say "Erm..."
    bree.say "What is it, Sasha?"
    bree.say "I mean, my shift's just ending."
    bree.say "And yours is about to start."
    show sasha whining
    sasha.say "That's the thing, [hero.name]..."
    sasha.say "I just got a call from Kleio..."
    sasha.say "Like just as I was walking in here."
    sasha.say "You know her?"
    sasha.say "She's one of the girls in my band, yeah?"
    show sasha sadsmile
    "The name is familiar, though I can't recall which one of them it is."
    "There's the short one with the big rack and the thin one with the bad attitude."
    "But none of that seems important right now."
    "So I just no in order to get Sasha to explain herself."
    show sasha whining
    sasha.say "The ceiling at the practice room is leaking."
    sasha.say "And I need to get over there to save our gear!"
    show sasha shout
    sasha.say "[hero.name], is there any chance that..."
    sasha.say "Maybe you could cover my shift today?"
    sasha.say "Just this once?"
    show sasha sadsmile
    menu:
        "Agree to cover Sasha's shift":
            "As soon as Sasha asks the favour of me, I feel conflicted."
            "On the one hand I feel like I should help my friend out."
            "But on the other, the thought of staying here a second longer..."
            "Well, it's driving me crazy!"
            "But I know that Sasha would do the same for me."
            "So there's only one possible answer."
            bree.say "Urgh..."
            bree.say "This is going to kill me, Sasha!"
            bree.say "But okay, I'll cover your shift."
            show sasha happy
            "The look of relief on Sasha's face is instant."
            show sasha at center, traveling(1.5, 0.5, (640, 1040))
            "And she grabs hold of my hand, squeezing it hard."
            sasha.say "Oh, [hero.name]..."
            sasha.say "Thank you, thank you, thank you!"
            show sasha shout
            sasha.say "I'll sort this as soon as I can."
            sasha.say "And then I'll be right back!"
            hide sasha with easeoutleft
            "With that, Sasha turns on her heel and literally runs out of the store."
            "Which leaves me to take a deep breath and summon the last of my strength."
            "As I walk in the opposite direction and prepare to start another shift."
            $ sasha.love += 5
        "Refuse to cover Sasha's shift":
            "As soon as Sasha asks the favour of me, I feel conflicted."
            "On the one hand I feel like I should help my friend out."
            "But on the other, the thought of staying here a second longer..."
            "Well, it's driving me crazy!"
            "And that's what makes my mind up in the end."
            "So I steel myself to resist temptation, and I shake my head."
            bree.say "Any other time and I would, Sasha."
            bree.say "But I'm dead on my feet right now."
            bree.say "Doing another few hours here would kill me!"
            show sasha sad
            "Sasha looks like she can see that I'm not lying."
            "But that doesn't mean she's not going to give it a second try."
            show sasha whining
            sasha.say "I can see that, [hero.name]..."
            sasha.say "But maybe you could go on the register or something?"
            sasha.say "Please?"
            show sasha sadsmile
            "I keep on shaking my head, already heading for the door."
            bree.say "I really can't, Sasha."
            show sasha sad
            bree.say "Ask one of the other girls, okay?"
            bree.say "And remember that I owe you one."
            "With that, I turn my back on Sasha."
            "And I hurry out of the store, hoping she does find someone to help."
            $ sasha.love -= 5
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    $ game.flags.worked_clothesshop += 1
    return

label sasha_clothesshop_friend_02:
    scene bg clothesshop with fade
    "I'm just handling the never-ending task of tidying up the fitting-rooms at the back of the store."
    "Because no matter how hard we try to tell them, customers just leave the clothes in there."
    "It's like the second they lose interest, they just drop them all over the floor and walk out."
    "So it feels like there's always one of us going in there to scoop them up again."
    "But as I emerge with an armful of clothes, I hear the sound of raised voices in the store."
    "Dropping the clothes, I hurry over in the hope of being able to help."
    show sasha angry at right5
    show heart attack at flip, left5, blacker
    with dissolve
    "And I'm shocked to see Sasha holding onto the end of a pair of jeans."
    "A quick glance at the other end lets me know just what the problem is."
    "Because the other end of the garment is being held onto by a dodgy looking guy."
    "The pair of them seem to be engaged in a tug of war over the jeans."
    show sasha pain
    sasha.say "[hero.name]..."
    sasha.say "Help me!"
    show sasha whining
    sasha.say "He's a...shop-lifter!"
    show sasha upset
    "I have perhaps a couple of seconds to decide what I'm going to do here."
    "Should I back Sasha up and help her to pull on the pair of jeans?"
    "Help her pull until they tear down the middle?"
    "Or perhaps I could do something more direct to the thief?"
    "Whatever I decide, I know that I need to do it soon!"
    menu:
        "Tackle the thief with Sasha":
            bree.say "Sasha..."
            bree.say "Forget the jeans..."
            bree.say "Tackle the guy instead!"
            "Without waiting for Sasha to acknowledge me, I leap forwards."
            play sound punch_hard
            pause 0.2
            with hpunch
            "And a moment later I slam straight into the shop-lifter."
            "He's caught totally by surprise and off-balance too."
            play sound body_fall
            pause 0.3
            hide heart attack with easeoutbottom
            "Which means we land in an untidy heap of limbs on the floor."
            play sound woosh_punch
            show sasha at center, traveling(1.25, 0.2, (640, 900))
            "Luckily for me, that's the exact moment Sasha chooses to get involved."
            play sound body_fall
            pause 0.3
            hide sasha with easeoutbottom
            pause 0.2
            with vpunch
            "She lands on top of the guy, and together we have the weight to pin him down."
            "Sure, he still manages to put up a pretty good fight."
            "And he almost gets free at one point."
            play sound punch_hard
            pause 0.2
            with vpunch
            "That is until I accidentally land a blow in a certain part of his anatomy."
            "One that I know from my own experience is often a guy's weak point!"
            "As his face turns purple from the pain, I hear the sound of approaching feet."
            "Luckily for Sasha and me, it's a couple of security guards."
            "They proceed to pounce on the guy too, and it's all over."
            show sasha at center, zoomAt(1.25, (640, 900)) with easeinbottom
            "Sasha and I get up, panting and more than a little sore."
            "And we watch as the security guards drag the shop-lifter away."
            show sasha whining
            sasha.say "Phew..."
            sasha.say "That was...intense!"
            show sasha normal
            bree.say "Yeah..."
            bree.say "Normally it's store policy not to tackle shop-lifters."
            bree.say "But I couldn't let you tangle with him on your own."
            show sasha happy
            sasha.say "Thanks for the help, [hero.name]."
            sasha.say "But maybe we should leave it to the security guards next time?"
            $ sasha.love += 5
        "Tell Sasha to let it go":
            "I hurry over to where Sasha's struggling with one leg of the jeans."
            "And I put my hands on her arm, already trying to make her let go."
            bree.say "Let go of the jeans, Sasha!"
            bree.say "They're not worth it!"
            show sasha stuned
            "Sasha looks at me with confusion in her eyes."
            "And she shakes her head, refusing to let go."
            show sasha surprised
            sasha.say "What are you talking about, [hero.name]?"
            show sasha vangry
            sasha.say "We can totally handle this guy!"
            sasha.say "So long as we do it together, right?"
            show sasha upset
            "I'm shaking my head too."
            "But I'm also tugging at Sasha's hands too."
            "And eventually I manage to break her grip."
            play sound body_fall
            pause 0.3
            hide sasha with easeoutbottom
            pause 0.2
            with vpunch
            "This means that the two of us fall in a heap on the ground."
            hide heart attack with easeoutleft
            "But also that the thief is pretty much launched out of the door too."
            "He almost stumbles and falls on his face, but then manages to dash off."
            show sasha sad at center, zoomAt(1.25, (640, 900)) with easeinbottom
            "Sasha shoves me off her and starts to get up."
            show sasha upset
            "And she looks pretty pissed at me too."
            show sasha vangry
            sasha.say "What did you do that for, [hero.name]?!?"
            sasha.say "I totally had that under control!"
            show sasha annoyed
            "I pick myself up too, forcing a smile onto my face as I do so."
            bree.say "Erm..."
            bree.say "I believe you, Sasha."
            bree.say "But the policy in the store is not to challenge shop-lifters."
            bree.say "It's way too dangerous!"
            bree.say "And I don't want to see a friend get hurt."
            show sasha surprised
            "Sasha seems to think about this as I explain myself."
            show sasha stuned
            "And she slowly starts to nod her head."
            show sasha whining
            sasha.say "Ah yeah..."
            sasha.say "I kinda get it, [hero.name]."
            show sasha shout
            sasha.say "I'll leave it to the security guards next time."
            $ sasha.love += 5
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    $ game.flags.worked_clothesshop += 1
    return

label sasha_clothesshop_friend_03:
    scene bg clothesshop with fade
    play sound phone_ring loop
    "At the sound of the phone in the store ringing, I look up from what I'm doing."
    "And I'm about to go and answer it myself, but then I see Sasha picking up the receiver."
    stop sound
    "That's a relief, as it means I can get right back to what I'm doing."
    show sasha with easeinright
    "But when I next look up, I see Sasha walking towards me."
    "So I guess the call wasn't just someone asking when the store closes this time."
    show sasha whining
    sasha.say "Urgh..."
    sasha.say "You're not going to believe this, [hero.name]..."
    sasha.say "But that was the girl who's supposed to be taking the next shift."
    show sasha sad
    "At the mere mention of the person relieving us, I feel my heart sink in my chest."
    "Because whatever the phone call was about, Sasha's mood says that it can't be good."
    bree.say "Don't hold back, Sasha..."
    bree.say "Just go ahead and hit me with it."
    bree.say "No matter how bad it is."
    "Sasha takes a deep breath, and then leaps into her explanation."
    show sasha whining
    sasha.say "Okay..."
    sasha.say "Apparently there's been some kind of screw-up with her transportation."
    sasha.say "Like, her car blew up on her, and for some reason she can't take the bus!"
    show sasha sad
    bree.say "That sucks for her, Sasha."
    bree.say "But what does it mean for us?"
    show sasha pain
    "Now Sasha really is grimacing."
    "But somehow she still manages to get her words out."
    show sasha whining
    sasha.say "Basically she's going to be a little late."
    show sasha sad
    bree.say "Erm..."
    bree.say "Exactly how late?"
    show sasha whining
    sasha.say "Maybe half an hour?"
    sasha.say "Forty-five minutes at the most?"
    show sasha sad
    "I can't help letting out a groan and rolling my eyes."
    "Because I was all ready to start counting down to the end of my shift."
    "And now it looks like I'm going to be stuck here for a while longer."
    bree.say "You have to be kidding!"
    bree.say "I'm starving, Sasha."
    bree.say "We were supposed to be going to get something to eat!"
    show sasha shout
    sasha.say "I know, I know..."
    sasha.say "But it's not like we can leave the store unattended."
    sasha.say "And we can't lock up while we get food either."
    show sasha sadsmile
    "I nod in agreement."
    "But then a thought occurs to me."
    bree.say "One of us could go out to get something, right?"
    bree.say "And the other one can hold down the fort?"
    "Sasha nods in agreement."
    show sasha shout
    sasha.say "That sounds like a plan, [hero.name]."
    sasha.say "You okay to nip out?"
    show sasha normal
    bree.say "No problem, Sasha..."
    bree.say "I'll go first."
    scene bg mall1 with fade
    "With that I hurry our of the store, intent on finding food."
    menu:
        "Buy food for Sasha and yourself" if hero.money >= 50:
            "I try to be as quick as I can, going to the nearest place I can think of."
            scene bg bakery with fade
            "But there's still a queue to be served and I have to wait for our food to be prepared."
            $ hero.money -= 50
            "So by the time I grab my order and head back to the store, the time is almost up."
            scene bg clothesshop with fade
            "The next member of staff to come on shift should be arriving any moment."
            "But still I can't resist opening up my food and stuffing it into my mouth!"
            show sasha with dissolve
            "As soon as Sasha lays eyes on it, she all but starts drooling."
            show sasha shout
            sasha.say "Quick, [hero.name]..."
            sasha.say "Where's mine?"
            sasha.say "I'm gonna pass out from hunger!"
            show sasha normal
            "Without stopping, I toss Sasha's order to her."
            show sasha happy
            "And she doesn't hesitate to follow my lead."
            "Soon the pair of us are devouring our food like ravenous animals."
            "Luckily for us, nobody walks into the store while all of this is happening."
            "And by the time we're finished, our relief is almost due."
            "So we can clean ourselves up and look half decent when they arrive."
            $ sasha.love += 5
            $ hero.hunger += 5
        "Buy food for yourself":
            "I try to be as quick as I can, going to the nearest place I can think of."
            scene bg bakery with fade
            "But there's still a queue to be served and I have to wait for my food to be prepared."
            "So by the time I grab my order and head back to the store, the time is almost up."
            scene bg clothesshop with fade
            "The next member of staff to come on shift should be arriving any moment."
            "But still I can't resist opening up my food and stuffing it into my mouth!"
            show sasha with dissolve
            "As soon as Sasha lays eyes on it, she all but starts drooling."
            show sasha shout
            sasha.say "Quick, [hero.name]..."
            sasha.say "Where's mine?"
            sasha.say "I'm gonna pass out from hunger!"
            show sasha sadsmile
            "I stop chewing and stare at Sasha over my food."
            "Did she just say what I think she said?"
            "Was she expecting me to buy her something too?!?"
            bree.say "Oops..."
            bree.say "Sorry, Sasha..."
            bree.say "I didn't get you anything!"
            show sasha sad
            "It's bad enough that I have to admit as much."
            "But the matter is made that much worse thanks to my having a full mouth."
            "Which means it kind of looks like I'm spitting my food at Sasha too!"
            show sasha whining
            sasha.say "Ah..."
            show sasha shout
            sasha.say "It's okay, [hero.name]..."
            sasha.say "I think I can hold on a little longer."
            sasha.say "Just don't go on eating that in front of me, yeah?"
            show sasha sad
            "Feeling like the worst friend in the world, I give Sasha a weak nod."
            "And then I scuttle off to eat my food in a shameful silence."
            $ hero.hunger += 5
            $ sasha.love -= 5
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    $ game.flags.worked_clothesshop += 1
    return

label sasha_clothesshop_friend_04:
    scene bg clothesshop with fade
    sasha.say "Erm..."
    sasha.say "[hero.name]?"
    show sasha with dissolve
    "I look up from what I'm doing to see Sasha standing in front of me."
    "And before she says another word, I note that she's motioning over her shoulder."
    show sasha at left4 with ease
    show gwen teaser at right, blacker with easeinright
    "A quick glance in that direction also shows me that there's a woman standing behind her."
    "A very large and intimidating woman who looks like she's less than pleased with something."
    bree.say "Yeah, Sasha?"
    bree.say "Is there something you needed?"
    show sasha pain
    "Sasha nods, a pained look on her face."
    show sasha whining
    sasha.say "Kind of..."
    sasha.say "This customer has an issue she'd like to raise with the store!"
    show sasha sad
    show gwen teaser at right4, blacker with ease
    "Almost as soon as Sasha mentions the woman, she leaps into action."
    show gwen teaser at center, blacker with ease
    show gwen teaser at center, blacker, stepback(0.16, 5, 0)
    show sasha stuned at left with ease
    show sasha at hshake
    "I watch as Sasha's all but flung aside by the irate customer."
    show sasha upset
    show gwen teaser zorder 2 at center, traveling (1.25, 1.0,  (640, 900)), blacker
    "Woman" "What do you mean 'raise an issue'?"
    "Woman" "I want to make a complaint!"
    "Woman" "And I want to speak to a manager too!"
    "I find myself backing off as the woman advances on me."
    "But then I feel the sales desk against my back, and I can't retreat any further."
    "Instead I scurry around it, keen to put the piece of furniture between us."
    "Luckily for me, the woman stays on the other side."
    "But she still leans on the desk in an intimidating manner."
    "Woman" "Are you going to get me the manager or not?!?"
    bree.say "Erm..."
    bree.say "The manager isn't in the store right now."
    bree.say "But I'm the senior employee on duty."
    bree.say "So why don't you explain the situation to me?"
    "The woman nods as she slams down a pair of trousers in front of me."
    with vpunch
    "She does it with such violence too that I can't help jumping backwards."
    "Woman" "Your store has it's sizes all wrong!"
    "Woman" "I know what size I am, and I should be able to fit into these."
    "Woman" "But when I tried them on just now, they were too small for me!"
    "I look at the woman, trying to guess her size by eye."
    "And then I pick up the trousers and check the size on the label."
    "And what I read there makes me look at the woman a second time."
    "All the while I'm wondering what planet she's currently on too."
    "There's no way the size on the pants is wrong."
    "And there's no way she could fit into them."
    "Not without me carving strips off of her ass and thighs!"
    menu:
        "Deal with the situation in a diplomatic manner" if hero.charm >= 30:
            bree.say "Madam..."
            bree.say "I am sorry."
            bree.say "But our stock is aimed at a less mature clientele."
            show sasha stuned
            show gwen teaser at center, zoomAt (1.0,  (640, 900)), blacker, startle
            "The woman regards me with narrowed eyes."
            "Woman" "What are you trying to say?"
            "Woman" "That I'm old?"
            "Woman" "That I can't read a label?"
            "I keep a polite smile on my face."
            show sasha sadsmile
            "But I make a point of gesturing to the door."
            bree.say "Not at all."
            bree.say "But there are several stores down the way."
            bree.say "And they specialise in serving a more discerning type of lady."
            "The woman makes a harumphing sound as she heads for the door."
            show gwen teaser at center, traveling (1.0, 5.0,  (340, 900)), blacker
            "Woman" "Humph..."
            "Woman" "Then I'll try my luck there instead."
            hide gwen with easeoutleft
            show sasha happy
            $ sasha.love += 5
            "I know it's technically losing a client."
            "But to avoid confrontation, it's a sacrifice I'm willing to make."
        "Give the woman a frank appraisal of the situation":
            bree.say "Madam..."
            bree.say "Are you on some form of strong medication?"
            bree.say "Because you seem to be out of touch with reality!"
            show gwen teaser at center, zoomAt (1.0,  (640, 900)), blacker, startle
            show sasha stuned
            "The woman's eyes almost pop out of her head at this."
            show sasha happy
            $ sasha.love += 2
            "She splutters and gasps, like I just slapped her in the face."
            "Woman" "What the..."
            "Woman" "Well I..."
            "Woman" "Never been so insulted..."
            "She keeps on getting redder in the face as she rants."
            "But the whole time I keep smiling at her."
            bree.say "I can take a note of your complaint if you'd like."
            bree.say "But I'm afraid nothing will come of it."
            bree.say "Because we take no responsibility for the size of our customer's backsides."
            "That does it."
            "That last comment sends her over the edge."
            hide gwen with easeoutleft
            "The woman storms out of the store, vowing vengeance and retribution as she goes."
            "But as there's nothing to her complaint, I'm happy to watch her go."
    show sasha happy at center with ease
    sasha.say "Phew..."
    show sasha shout
    sasha.say "Thanks, [hero.name]..."
    sasha.say "I thought she'd never leave!"
    show sasha normal
    bree.say "No worries, Sasha."
    bree.say "When you work here long enough, you get used to problem customers."
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    $ game.flags.worked_clothesshop += 1
    return

label sasha_clothesshop_lover_01:
    scene bg clothesshop with fade
    "There's always a fuss at the clothes store when the rota for the next month is out."
    "Everyone rushes to see what shifts they've been given and what days off they get too."
    "And after that there's the additional matter of just who you'll be working with on those days."
    "Everyone wants to get lucky and end up on a shift with someone they like."
    "Or at the very least someone that they can tolerate without murderous thoughts!"
    "But the thing is that it's a little more complicated for me and Sasha."
    "As we're a lot more than friends these days, if you know what I mean!"
    "So ending up on a shift with each other should be the most desirable thing in the world."
    "But part of me is worried about what the result will be if it happens all the time."
    "You have to understand that I'm not suggesting I don't want to spend time with Sasha."
    "And we tend to get on really well when we're both on the same shift."
    "No, what I'm worried about is it meaning that we spend too much time together."
    "When we hang out together or go on a date that's one thing."
    "But working together is totally different, at least if you ask me."
    "There are times when you have to deal with awful customers."
    "And then there are the occasions on which the store is crazily busy."
    "I don't want to get stressed and take it out on Sasha."
    "And I certainly don't want her to do the same to me either!"
    "Yet I'm also scared to say that I don't want to be on the same shift too."
    "Because that could look like I want to put some distance between us."
    "So when Sasha comes hurrying over to show me the rota, I feel myself getting really anxious."
    show sasha happy with easeinleft
    sasha.say "Good news, [hero.name]..."
    sasha.say "Looks like we got a couple of shifts together next month."
    show sasha normal
    bree.say "Really?"
    bree.say "That's great news, Sasha."
    bree.say "How many exactly?"
    show sasha annoyed
    "Sasha frowns at this and shakes her head."
    show sasha shout
    sasha.say "Not as many as I'd like!"
    show sasha normal
    bree.say "It's not a big deal."
    bree.say "Maybe we'll get more next month?"
    bree.say "Especially if we show management how good of a team we are this month, yeah?"
    show sasha sadsmile
    "Sasha nods her head at this."
    show sasha annoyed
    "But the expression on her face seems to say that she's not totally convinced."
    sasha.say "Hmm..."
    show sasha shout
    sasha.say "I was gonna ask some of the other girls to swap shifts."
    sasha.say "That way we won't have to work so hard to get what we want, right?"
    show sasha sadsmile
    "Sasha looks at me, making it plain that she's waiting for my answer."
    "Looks as though she wants my permission to give it a try."
    menu:
        "Agree to try changing the shifts":
            "I decide that it's probably best to go along with Sasha's idea."
            "Because the last thing I want is for her to think I hate her company."
            bree.say "Do you think they would?"
            bree.say "Because it'd be great if we could make that happen."
            show sasha normal
            "Sasha nods, spurred on by my encouragement."
            show sasha happy
            sasha.say "Oh yeah, [hero.name]..."
            show sasha shout
            sasha.say "I already spotted a couple of shifts some of them hate working."
            sasha.say "And only one of us is on most of them."
            show sasha normal
            bree.say "Do you want me to speak to any of the other girls?"
            show sasha shout
            sasha.say "Nah..."
            sasha.say "I can handle it myself."
            sasha.say "Leave it to me!"
            hide sasha happy with easeoutright
            "With that, Sasha hurries off to put her plan into action."
            "And I watch her go, hoping that I've made the right decision."
        "Tell Sasha not to try changing the shifts":
            "I decide that it's probably best to limit the time we're working together."
            "So I shake my head at the idea, letting Sasha know that I disapprove."
            bree.say "I don't think there's any need to do that, Sasha."
            bree.say "I mean, it's not like we have to be on every shift together."
            show sasha stuned
            "Sasha looks more than a little taken aback by my answer."
            "But to my relief, she looks more surprised than upset."
            show sasha surprised
            sasha.say "Why not, [hero.name]?"
            sasha.say "I thought it'd be cool to work together?"
            show sasha sad
            "I shrug and force a smile onto my face."
            "Trying to explain myself to Sasha."
            bree.say "It's great that we get to work together sometimes, Sasha."
            bree.say "But I'd rather spend my time with you doing fun stuff."
            bree.say "And things sometimes get pretty stressful around here."
            bree.say "So I'd rather you not see me getting stressed out too!"
            show sasha normal
            "Sasha seems to take in my words and ponder them as I speak."
            "And when I'm done explaining, she actually nods."
            show sasha shout
            sasha.say "You know what, [hero.name]..."
            sasha.say "You've got a point."
            sasha.say "Maybe we would be better spending quality time together."
            sasha.say "So let's leave the rota as it is."
    $ sasha.love += 8
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    $ game.flags.worked_clothesshop += 1
    return

label sasha_clothesshop_lover_02:
    scene bg clothesshop with fade
    "I'm engaged in the never-ending task of folding up clothes and putting them on display."
    "It's one of those things that's always needing to be done in a clothes store."
    "And normally it's also one of the things that nobody wants to get lumbered with."
    "But the truth is that I tend to find it quite relaxing, almost meditative."
    "And so I take it on while whoever else is on shift with me does other stuff."
    "Today that's Sasha, and I get the sense that she's not very happy with my choice."
    "Which is weird, because it should be giving her the chance to do less boring stuff around the store."
    "Yet every time I look up, I see her stomping past on her way to do this or that."
    "And pretty soon I find myself wondering just what her problem is."
    "In fact it's bugging me so much that I find I've stopped folding and started staring."
    show sasha at left with easeinright
    "For the first time I watch Sasha as she walks past me and stops on the other side of the store."
    "I'm expecting her to say something or make a rude gesture in my direction."
    "So it comes as a genuine shock when she turns her back to be and bends over."
    "Then she actually pulls up her skirt and flashes her ass at me!"
    "I mean, sure, she has panties on under it."
    "But that's not the point!"
    "When Sasha stands up again, I can see that she's smiling at me."
    "It's like her whole mood's changed now that I've seen what she just did."
    "Wait a minute..."
    "Has she been doing that every time she walked past me?"
    "No wonder she looked so pissed off if this is the only time I saw her!"
    "Now that she knows she has my attention, Sasha seems determined to keep it."
    "She walks to another part of the store, this time one closer to the windows."
    "And she proceeds to do the same thing again."
    "From my point of view, I can see how close she is to being seen."
    "And by that I mean being seen by someone other than me!"
    menu:
        "Get a thrill out of what Sasha is doing":
            "Part of me feels like I should stop Sasha before she gets in trouble."
            "Or at least tell her about all the cameras she's flashing me in front of."
            "But the truth is that I'm enjoying the show too much to want to stop it."
            "So I decide to indulge Sasha, smiling and nodding as she repeats the flash."
            "She doesn't seem to be getting tired of performing for my amusement."
            "And it's certainly brightening up the shift for me too."
            show sasha normal at center, traveling(1.5, 2.0, (640, 1040))
            "When Sasha finally decided that the performance is over, she swaggers over to me."
            show sasha flirt
            sasha.say "So..."
            sasha.say "You like what you see, huh?"
            show sasha shy
            bree.say "Oh yeah, it was very brave of you."
            bree.say "Especially with all the cameras in here!"
            show sasha surprised
            sasha.say "Cameras?"
            sasha.say "What cameras?"
            show sasha stuned
            bree.say "You didn't think there were cameras in here?"
            show sasha whining
            sasha.say "Of course I did, [hero.name]..."
            sasha.say "But I thought they were only for filming shop-lifters and things like that!"
            show sasha sad
            "I blink at Sasha, baffled by what she just said."
            bree.say "How would they film shop-lifters and not everything else in the shop?!?"
            show sasha pain
            sasha.say "I don't know!"
            show sasha whining
            sasha.say "But I know we have to erase that tape!"
            show sasha sad
            bree.say "Don't worry, Sasha..."
            show sasha sadsmile
            bree.say "I'm just messing with you."
            bree.say "I know where the footage is logged on the store computer."
            bree.say "We'll wipe all trace of your ass at the end of the shift."
            $ hero.morality -= 1
            $ sasha.love += 8
        "Hurry over and tell Sasha to stop what she's doing":
            "And if that happens then we could both be in serious trouble."
            "We could even end up losing our jobs over it."
            "Before Sasha can repeat her performance again, I hurry over there."
            "At first she's smiling as I come closer."
            "But then her expression changes as she sees mine."
            show sasha normal at center, traveling(1.5, 2.0, (640, 1040))
            bree.say "Sasha!"
            bree.say "You have to stop doing that!"
            show sasha surprised
            sasha.say "Huh?"
            sasha.say "What are you talking about, [hero.name]?"
            sasha.say "Nobody saw a thing."
            show sasha sad
            bree.say "That's just because you were lucky."
            bree.say "You could get spotted any time."
            bree.say "And what about the security cameras in here?!?"
            show sasha stuned
            "At the mere mention of cameras, Sasha's face goes pale."
            show sasha surprised
            sasha.say "Cameras?"
            sasha.say "What cameras?"
            show sasha stuned
            bree.say "You didn't think there were cameras in here?"
            show sasha whining
            sasha.say "Of course I did, [hero.name]..."
            sasha.say "But I thought they were only for filming shop-lifters and things like that!"
            show sasha sadsmile
            "I blink at Sasha, baffled by what she just said."
            bree.say "How would they film shop-lifters and not everything else in the shop?!?"
            show sasha pain
            sasha.say "I don't know!"
            show sasha whining
            sasha.say "But I know we have to erase that tape!"
            sasha.say "Wait here, bree - I'll go find it."
            hide sasha with easeoutright
            "I don't have it in me to tell Sasha there's no tape to be found."
            "Plus her searching for it guarantees there won't be any more mooning the rest of my shift."
            $ sasha.love -= 5
            $ hero.morality += 1
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    $ game.flags.worked_clothesshop += 1
    return

label sasha_clothesshop_lover_03:
    scene bg clothesshop with fade
    "The store that I work in kind of markets itself as catering to men and women alike."
    "But the truth is like ninety percent of the stuff we sell is totally for women."
    "So it's unusual for us to get a guy wandering around the place on his own."
    "And when we do, it's usually one looking to buy something for his significant other."
    "Today I spot just that kind of guy too - wandering around and looking kind of lost."
    show scottie at flip, right5, blacker with dissolve
    "So I make a point of walking over there with a polite smile on my face."
    "I tend to find a friendly face and some help is what these guys really need."
    "But as soon as I make eye-contact with this one, I get a different vibe off of him."
    bree.say "Excuse me, sir..."
    bree.say "Is there anything I can do to help you?"
    "Even before the guy opens his mouth to speak, I can feel his eyes all over me."
    "And this is one of those times I just know that I'm being mentally undressed."
    "The smile that he shows me in return for mine isn't the same kind either."
    "His is the type a total jerk pulls off when he's trying to look superior."
    "Shady guy" "Maybe you can, maybe you can't..."
    "Shady guy" "You don't look like the kind of girl that I'm shopping for though."
    "I can't help raising my eyebrows in surprise."
    "Because most of the guys I approach in here are quite grateful for my help."
    "But this guy makes it sound like he's doing me a favour giving me the time of day!"
    bree.say "Is that so?"
    bree.say "Just what kind of girl are you shopping for?"
    bree.say "I'm sure we have the kind of styles that she'd like."
    "The guy looks at me for a moment."
    "Kind of like I'm something he just found smeared on the sole of his shoe."
    "And then he shrugs as he casts his gaze around the store."
    show sasha annoyed at left with dissolve
    "But then his eyes settle on Sasha."
    "She's stocking the racks on the other side of the store."
    "So there's no way she could know she's being watched or hear what we're saying."
    "Shady guy" "Now that's more like it - that girl over there."
    bree.say "Which girl do you mean?"
    "Shady guy" "The one with the dark hair."
    "Shady guy" "She looks like a proper rock slut!"
    "Shady guy" "Do you sell the kind of thing she'd wear?"
    hide sasha with dissolve
    "I feel my heckles go up the moment the guy starts talking about Sasha like that."
    "And in instant I know just the kind of man that he is."
    "The kind that likes to intimidate women by putting down others."
    "I bet he's banking on me being too shocked to do anything about it too!"
    "Well that's where he's dead wrong."
    "Because I know exactly how to deal with this kind of bullshit!"
    menu:
        "Insinuate the guy is shopping for himself":
            "I take a step backwards and look the guy up and down."
            "He takes note of what I'm doing, instantly becoming suspicious."
            "Shady guy" "Hey!"
            "Shady guy" "Why are you looking at me like that?"
            "I make sure I have a patronising smile on my face."
            "And I raise me eyebrows, nodding in a conspiratorial manner."
            bree.say "Oh, don't you worry about a thing, sir."
            bree.say "I can see from here that your measurements are the same as hers."
            bree.say "And there's no reason to be shy about it."
            "The guy's starting to look nervous."
            "Glancing this way and that."
            "Shady guy" "What are you talking about?"
            "Shady guy" "What's my size got to do with anything?!?"
            "I let out a chuckle and lean in closer."
            bree.say "That's good, keep it up."
            bree.say "I know that guys come in here for clothes all the time."
            bree.say "Guys that just want women's clothes to make them feel pretty!"
            bree.say "So don't worry, we'll sort you out, sir."
            "By now the guy's starting to sweat."
            "And he's actually backing away from me."
            "Shady guy" "That's not what I'm here for!"
            "Shady guy" "You stay the hell away from me!"
            hide scottie with easeoutleft
            "With that, he turns on his heel and runs out of the door."
            show sasha surprised with easeinright
            "As I watch him go, Sasha wanders over."
            sasha.say "Huh!"
            show sasha whining
            sasha.say "What's his problem?"
            show sasha annoyed
            bree.say "I think he wanted to buy some women's clothes for himself."
            bree.say "But the pressure was too much for the poor guy."
            show sasha joke
            sasha.say "What a shame."
            sasha.say "Looked like he could have pulled off a nice off-the-shoulder number too!"
        "Extoll Sasha's virtues as your lover":
            "I make sure that the guy can see me staring at Sasha too."
            "Then I shake my head and let out a laugh."
            "Of course he becomes instantly suspicious."
            "Looking at me sideways and frowning."
            "Shady guy" "Hey..."
            "Shady guy" "What's so funny about that?"
            "Shady guy" "You got a problem with what I just said?"
            bree.say "Oh no..."
            bree.say "She's definitely a handful, that one."
            bree.say "But she's also more than a little boy like you could handle!"
            "The guy obviously bristles at this, crossing his arm over his chest."
            "And it seems like he wants to get confrontational too."
            "Shady guy" "Oh yeah?"
            "Shady guy" "What would you know about it, little girl?!?"
            bree.say "Well, she does happen to be my partner."
            bree.say "And by that, I don't mean my business partner."
            bree.say "I mean my lover, the woman that I'm with and the one that shares my bed."
            bree.say "So yeah, I'd know a hell of a lot about it!"
            "The guy's getting flustered now, unsure of how to respond."
            "He doesn't seem to have a comeback for what I just told him."
            "And I can almost see his confidence draining away by the second."
            "Pretty soon he's reduced to apologising and grovelling."
            "Shady guy" "I...I'm sorry..."
            "Shady guy" "I...I didn't know..."
            "Shady guy" "That...that you were together!"
            hide scottie with easeoutleft
            show sasha surprised with easeinright
            "As I watch him go, Sasha wanders over."
            sasha.say "Huh!"
            show sasha whining
            sasha.say "What's his problem?"
            show sasha annoyed
            bree.say "He couldn't handle the sheer feminine power on display in here."
            show sasha joke
            sasha.say "What a shame."
            sasha.say "But he looked like a lame prick anyway."
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    $ game.flags.worked_clothesshop += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
