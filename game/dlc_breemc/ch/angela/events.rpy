init python:
    
    Event(**{
        "name": "angela_female_event_01",
        "label": "angela_female_event_01",
        "priority": 500,
        "duration": 1,
        "conditions": [
            IsDayOfWeek(6, 7),
            IsHour(14, 16),
            HeroTarget(
                IsGender("female"),
                IsRoom("livingroom")),
            PersonTarget(mike,
                MinStat("love", 100)
                ),
            ],
        "do_once": True,
        "quit": False,
        })
    
    Event(**{
        "name": "angela_female_event_02",
        "label": "angela_female_event_02",
        "priority": 500,
        "duration": 1,
        "conditions": [
            IsDone("angela_female_event_01"),
            IsTimeOfDay("afternoon"),
            HeroTarget(
                IsGender("female"),
                IsRoom("mall1")),
            PersonTarget(angela,
                IsFlag("angeladelay", False),
                MinStat("love", 20)
                ),
            ],
        "do_once": True,
        "quit": False,
        })
    
    Event(**{
        "name": "angela_female_event_03",
        "label": "angela_female_event_03",
        "priority": 500,
        "duration": 1,
        "conditions": [
            IsDone("angela_female_event_02"),
            HeroTarget(
                IsGender("female"),
                IsActivity("run_park")),
            PersonTarget(angela,
                IsFlag("angeladelay", False),
                MinStat("love", 40)
                ),
            ],
        "do_once": True,
        "quit": False,
        })
    
    Event(**{
        "name": "angela_female_event_04",
        "label": "angela_female_event_04",
        "priority": 500,
        "duration": 1,
        "conditions": [
            IsDone("angela_female_event_03"),
            IsTimeOfDay("morning", "afternoon"),
            HeroTarget(IsGender("female"),
                Not(IsActivity())
                ),
            PersonTarget(angela,
                IsFlag("angeladelay", False),
                MinStat("love", 60)
                ),
            ],
        "do_once": True,
        "quit": False,
        })
    
    Event(**{
        "name": "angela_female_event_05",
        "label": "angela_female_event_05",
        "priority": 500,
        "duration": 1,
        "conditions": [
            IsDone("angela_female_event_04"),
            HeroTarget(IsGender("female"),
                Or(
                    IsRoom("map"),
                    HasRoomTag("street"),
                    HasRoomTag("park"),
                ),
                Not(IsActivity()),
                ),
            PersonTarget(angela,
                HasRoomTag("street"),
                Not(IsHidden()),
                IsFlag("angeladelay", False),
                MinStat("love", 80)
                ),
            ],
        "do_once": True,
        "quit": False,
        })
    
    Event(**{
        "name": "angela_female_event_06",
        "label": "angela_female_event_06",
        "priority": 500,
        "duration": 0,
        "conditions": [
            IsDone("angela_female_event_05"),
            HeroTarget(IsGender("female"),
                HasRoomTag("pub"),
                Not(IsActivity()),
                ),
            PersonTarget(angela,
                IsPresent(),
                Not(IsHidden()),
                MinStat("love", 100),
                IsFlag("angeladelay", False),
                ),
            ],
        "do_once": True,
        "quit": False,
        })
    
    Event(**{
        "name": "angela_female_event_07",
        "label": "angela_female_event_07",
        "priority": 500,
        "duration": 0,
        "conditions": [
            IsDone("angela_female_event_06"),
            IsTimeOfDay("morning", "afternoon"),
            HeroTarget(IsGender("female"),
                Or(
                    HasRoomTag("street"),
                    HasRoomTag("park"),
                ),
                Not(IsActivity()),
                ),
            PersonTarget(angela,
                Not(IsHidden()),
                MinStat("love", 110),
                IsFlag("angeladelay", False),
                ),
            ],
        "do_once": True,
        "quit": False,
        })
    
    
    Event(**{
        "name": "angela_female_event_08",
        "label": "angela_female_event_08",
        "priority": 500,
        "duration": 1,
        "conditions": [
            IsDone("angela_female_event_07"),
            HeroTarget(IsGender("female"),
                IsRoom("hospital"),
                Not(IsActivity()),
                Not(IsFlag("angela_test_results")),
                ),
            PersonTarget(angela,
                Not(IsHidden()),
                MinStat("love", 120),
                IsFlag("angeladelay", False),
                ),
            ],
        "do_once": False,
        "once_day": True,
        })
    
    
    Event(**{
        "name": "angela_female_event_09",
        "label": "angela_female_event_09",
        "priority": 500,
        "duration": 1,
        "conditions": [
            IsDone("angela_female_event_08"),
            IsTimeOfDay("afternoon", "evening"),
            HeroTarget(IsGender("female"),
                IsRoom("livingroom", "kitchen", "bathroom", "bedroom2"),
                IsFlag("angela_test_results"),
                Not(IsActivity()),
                ),
            PersonTarget(angela,
                Not(IsHidden()),
                MinStat("love", 140),
                IsFlag("angeladelay", False),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "angela_female_event_10",
        "label": "angela_female_event_10",
        "priority": 500,
        "duration": 1,
        "conditions": [
            IsDone("angela_female_event_09"),
            IsTimeOfDay("afternoon", "evening"),
            HeroTarget(IsGender("female"),
                HasRoomTag("home"),
                Not(IsActivity()),
                ),
            PersonTarget(angela,
                Not(IsHidden()),
                MinStat("love", 160),
                IsFlag("angeladelay", False),
                ),
            ],
        "do_once": True,
        })
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    Event(**{
        "name": "angela_asking_for_help_fail",
        "label": "angela_asking_for_help_fail",
        "priority": 500,
        "duration": 1,
        "conditions": [
            IsDone("angela_female_event_10"),
            HeroTarget(IsGender("female"),
                Not(IsActivity()),
                ),
            PersonTarget(angela,
                Not(IsHidden()),
                MinStat("love", 160),
                IsFlag("angeladelay", False),
                IsFlag("angela_choice", "outside_help"),
                Not(IsFlag("outside_help")),
                ),
            And(
                Or(
                    Or(
                        IsDone("angela_female_event_12b"),
                        IsDone("angela_female_event_13d"),
                    ),
                    PersonTarget(mike,
                        Or(
                            IsHidden(),
                            IsGone(),
                            ),
                        ),
                    ),

                Or(
                    IsDone("angela_female_event_12c"),
                    PersonTarget(dwayne,
                        Or(
                            IsHidden(),
                            IsGone(),
                            ),
                        ),
                    ),
                Or(
                    IsDone("angela_female_event_12d"),
                    PersonTarget(victor,
                        Or(
                            IsHidden(),
                            IsGone(),
                            ),
                        ),
                    ),
                Or(
                    IsDone("angela_female_event_12e"),
                    PersonTarget(danny,
                        Or(
                            IsHidden(),
                            IsGone(),
                            ),
                    ),
               ),
            ),
            ],
        "do_once": True,
    })
    
    
    
    
    Event(**{
        "name": "angela_female_event_11",
        "label": "angela_female_event_11",
        "priority": 500,
        "duration": 1,
        "conditions": [
            IsDone("angela_female_event_10"),
            IsTimeOfDay("morning", "afternoon"),
            HeroTarget(IsGender("female"),
                IsRoom("policestation"),
                Not(IsActivity()),
                ),
            PersonTarget(angela,
                Not(IsHidden()),
                MinStat("love", 180),
                IsFlag("angeladelay", False),
                IsFlag("angela_choice", "police"),
                ),
            ],
        "do_once": True,
        })
    
    Activity(**{
        "name": "angela_female_event_12a",
        "display_name": "Break in Angela's house",
        "max_girls": 0,
        "rooms": ("street", "street2"),
        "conditions": [
            IsTimeOfDay("night"),
            IsNotDone("angela_female_event_12a"),
            HeroTarget(IsGender("female"),
                HasRoomTag("street"),
                Not(IsActivity()),
                ),
            PersonTarget(angela,
                Not(IsHidden()),
                MinStat("love", 180),
                IsFlag("angeladelay", False),
                ),
            Or(
                And(
                    IsDone("angela_female_event_10"),
                    PersonTarget(angela,
                        IsFlag("angela_choice", "evidence"),
                        ),
                    ),
                And(
                    IsDone("angela_female_event_11"),
                    PersonTarget(angela,
                        IsFlag("angela_choice", "police"),
                        ),
                    ),
                )
            ],
        "label": "angela_female_event_12a",
        "icon": "investigate",
        "once_day": True,
        })
    
    Event(**{
        "name": "angela_female_event_14a",
        "label": "angela_female_event_14a",
        "priority": 500,
        "duration": 1,
        "conditions": [
            IsDone("angela_female_event_13a"),
            IsTimeOfDay("afternoon", "evening"),
            HeroTarget(IsGender("female"),
                IsRoom("policestation"),
                Not(IsActivity()),
                ),
            PersonTarget(angela,
                Not(IsHidden()),
                IsFlag("angeladelay", False),
                ),
            ],
        "do_once": True,
        })
    
    
    SpecificTalkSubject(**{
        "name": "angela_female_event_12b",
        "label": "angela_female_event_12b",
        "display_name": "About your mother",
        "icon": "button_angela",
        "conditions": [
            IsDone("angela_female_event_10"),
            HeroTarget(IsGender("female"),
                ),
            PersonTarget(angela,
                Not(IsHidden()),
                MinStat("love", 180),
                IsFlag("angeladelay", False),
                IsFlag("angela_choice", "outside_help"),
                IsFlag("outside_help", None),
                ),
            PersonTarget(mike,
                IsActive(),
                MinStat("sexperience", 1),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "angela_female_event_13d",
        "label": "angela_female_event_13d",
        "conditions": [
            IsDone("angela_female_event_12b"),
            IsNotDone("angela_female_event_13e"),
            HeroTarget(IsGender("female"),
                IsActivity("None"),
                ),
            PersonTarget(angela,
                Not(IsHidden()),
                IsFlag("angeladelay", False),
                IsFlag("outside_help", "mike"),
                ),
            PersonTarget(mike,
                IsPresent(),
                MinStat("love", 150),
                Not(IsHidden()),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "angela_female_event_13e",
        "label": "angela_female_event_13e",
        "conditions": [
            IsDone("angela_female_event_12b"),
            IsNotDone("angela_female_event_13d"),
            IsTimeOfDay("morning", "evening", "afternoon"),
            HeroTarget(IsGender("female"),
                IsActivity("None"),
                ),
            PersonTarget(angela,
                Not(IsHidden()),
                IsFlag("angeladelay", False),
                IsFlag("outside_help", "mike"),
                ),
            PersonTarget(mike,
                IsPresent(),
                MaxStat("love", 149),
                Not(IsHidden()),
                ),
            ],
        "do_once": True,
        })
    
    
    SpecificTalkSubject(**{
        "name": "angela_female_event_12c",
        "label": "angela_female_event_12c",
        "display_name": "About Angela",
        "icon": "button_angela",
        "conditions": [
            IsDone("angela_female_event_10"),
            HeroTarget(IsGender("female"),
                IsRoom("ceo"),
                ),
            PersonTarget(angela,
                Not(IsHidden()),
                MinStat("love", 180),
                IsFlag("angeladelay", False),
                IsFlag("angela_choice", "outside_help"),
                IsFlag("outside_help", None),
                ),
            PersonTarget(dwayne,
                IsActive(),
                Not(IsHidden()),
                MinStat("sexperience", 1),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "angela_female_event_13f",
        "label": "angela_female_event_13f",
        "conditions": [
            IsDone("angela_female_event_12c"),
            IsTimeOfDay("morning", "evening", "afternoon"),
            HeroTarget(IsGender("female"),
                HasRoomTag("home")
                ),
            PersonTarget(angela,
                Not(IsHidden()),
                IsFlag("angeladelay", False),
                IsFlag("outside_help", "dwayne"),
                ),
            PersonTarget(dwayne,
                Not(IsHidden()),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "angela_female_event_14b",
        "label": "angela_female_event_14b",
        "conditions": [
            IsDone("angela_female_event_13f"),
            IsTimeOfDay("morning", "afternoon"),
            HeroTarget(IsGender("female"),
                HasRoomTag("mcoffice")
                ),
            PersonTarget(angela,
                Not(IsHidden()),
                IsFlag("angeladelay", False),
                ),
            PersonTarget(dwayne,
                Not(IsHidden()),
                ),
            ],
        "do_once": True,
        })
    
    
    SpecificTalkSubject(**{
        "name": "angela_female_event_12d",
        "label": "angela_female_event_12d",
        "display_name": "About Angela",
        "icon": "button_angela",
        "conditions": [
            IsDone("angela_female_event_10"),
            HeroTarget(IsGender("female"),
                ),
            PersonTarget(angela,
                Not(IsHidden()),
                MinStat("love", 180),
                IsFlag("angeladelay", False),
                IsFlag("angela_choice", "outside_help"),
                IsFlag("outside_help", None),
                ),
            PersonTarget(victor,
                IsActive(),
                Not(IsHidden()),
                MinStat("sexperience", 1),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "angela_female_event_13g",
        "label": "angela_female_event_13g",
        "conditions": [
            IsDone("angela_female_event_12d"),
            IsTimeOfDay("morning", "evening", "afternoon"),
            HeroTarget(IsGender("female"),
                HasRoomTag("home")
                ),
            PersonTarget(angela,
                Not(IsHidden()),
                IsFlag("angeladelay", False),
                IsFlag("outside_help", "victor"),
                ),
            PersonTarget(victor,
                Not(IsHidden()),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "angela_female_event_14c",
        "label": "angela_female_event_14c",
        "conditions": [
            IsDone("angela_female_event_13f"),
            IsTimeOfDay("evening", "night"),
            HeroTarget(IsGender("female"),
                HasRoomTag("street")
                ),
            PersonTarget(angela,
                Not(IsHidden()),
                   IsFlag("angeladelay", False),
                ),
            PersonTarget(victor,
                Not(IsHidden()),
                ),
            ],
        "do_once": True,
        })
    
    
    SpecificTalkSubject(**{
        "name": "angela_female_event_12e",
        "label": "angela_female_event_12e",
        "display_name": "About Angela",
        "icon": "button_angela",
        "conditions": [
            IsDone("angela_female_event_10"),
            HeroTarget(IsGender("female"),
                ),
            PersonTarget(angela,
                Not(IsHidden()),
                MinStat("love", 180),
                IsFlag("angeladelay", False),
                IsFlag("angela_choice", "outside_help"),
                IsFlag("outside_help", None),
                ),
            PersonTarget(danny,
                IsActive(),
                Not(IsHidden()),
                MinStat("sexperience", 1),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "angela_female_event_13h",
        "label": "angela_female_event_13h",
        "conditions": [
            IsDone("angela_female_event_12e"),
            IsTimeOfDay("morning", "evening", "afternoon"),
            HeroTarget(IsGender("female"),
                HasRoomTag("home")
                ),
            PersonTarget(angela,
                Not(IsHidden()),
                IsFlag("angeladelay", False),
                IsFlag("outside_help", "danny"),
                ),
            PersonTarget(danny,
                Not(IsHidden()),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "angela_female_event_14d",
        "label": "angela_female_event_14d",
        "conditions": [
            IsDone("angela_female_event_13h"),
            IsTimeOfDay("evening", "night"),
            HeroTarget(IsGender("female"),
                IsRoom("alley")
                ),
            PersonTarget(angela,
                Not(IsHidden()),
                IsFlag("angeladelay", False),
                ),
            PersonTarget(danny,
                Not(IsHidden()),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "angela_female_event_15",
        "label": "angela_female_event_15",
        "display_name": "Finally Free",
        "conditions": [
            IsTimeOfDay("evening"),
            HeroTarget(IsGender("female"),
                HasRoomTag("pub"),
                ),
            PersonTarget(angela,
                Not(IsHidden()),
                IsFlag("angeladelay", False),
                ),
            Or(
                IsDone("angela_female_event_14a"),
                IsDone("angela_female_event_13c"),
                IsDone("angela_female_event_13f"),
                IsDone("angela_female_event_13g"),
                IsDone("angela_female_event_13h"),
                ),
            ],
        "do_once": True,
        })
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    Event(**{
        "name": "angela_female_dom_01",
        "label": "angela_female_dom_01",
        "duration": 1,
        "conditions": [
            IsDone("angela_female_event_09"),
            
            IsTimeOfDay("morning", "afternoon"),
            HeroTarget(
                IsGender("female"),
                IsFlag("collared", False),
                HasRoomTag("home"),
                Not(IsActivity()),
                ),
            PersonTarget(angela,
                Not(IsHidden()),
                MinStat("love", 110),
                IsFlag("angeladelay", False),
                ),
            ],
        "do_once": True,
        })

label angela_female_event_01:
    $ angela.flags.schedule = "default_female"
    $ angela.unhide()
    scene bg livingroom
    play sound door_knock
    "There's a knock at the door, but at first I just ignore it."
    "Yeah, I know it's lazy of me - but I'm not expecting anyone."
    "Also, I know that I'm not the only person in the house either."
    "I haven't seen Sasha in a while, but I known [mike.name]'s mooching about somewhere."
    play sound [door_knock, "<silence .5>", door_knock]
    "But then I hear the knocking for a second time, and a third."
    "So I roll my eyes as I get up and slope towards the door."
    bree.say "Don't worry about it guys."
    bree.say "I'll just drop everything and get the door, yeah?"
    "I wait for a moment, just to see if anyone heard me."
    "But all I hear is silence, so I open the door, muttering to myself the whole time."
    scene bg black with dissolve
    pause 0.1
    show bg house
    show angela normal at center, zoomAt(1.0, (640, 720))
    with wiperight
    bree.say "Ah..."
    bree.say "Hey, can I help you?"
    show angela smile at center, traveling(1.25, 0.5, (640, 880))
    "The woman standing on the doorstep gives me a broad smile."
    "And I do the same as we look each other up and down."
    "She's one of those older women that you just want to hate straight off."
    "You know the kind I mean, right?"
    "Tall and with a dark complexion that means she has no wrinkles."
    "Full figure without there being any way you could call her fat."
    "She's just standing there, brimming with self-assured confidence."
    show angela talkative at startle(0.1, 5)
    angela.say "Oh, you must be [hero.name]."
    angela.say "Am I right?"
    show angela smile
    bree.say "Erm...yeah, that's me!"
    show angela happy
    angela.say "Of course it is, dear."
    angela.say "[mike.name]'s told me all about you!"
    show angela smile
    "That's all it takes for my mind to put the pieces together."
    "This must be [mike.name]'s mom!"
    "But what's she doing here?"
    mike.say "Mom?!?"
    mike.say "Is that you?"
    scene bg livingroom
    show mike smile at center, zoomAt(1.25, (640, 900))
    with fade
    "I turn around just in time to see [mike.name] appear in the hallway."
    "He looks genuinely happy to see Angela, but surprised all the same."
    show mike happy at startle(0.1, 5)
    mike.say "What are you doing here?"
    mike.say "You never said you were going to be in town!"
    show mike smile at center, zoomAt(1.25, (440, 900))
    show angela smile at center, zoomAt(1.1, (840, 830))
    with easeinright
    "Without asking for permission, Angela steps into the hallway."
    "This means that she also brushes past in at the same time."
    "I only just manage to step out of her way without being shoved aside!"
    show angela annoyed at startle(0.1, 5)
    angela.say "Since when do I need permission to visit my son?"
    show angela normal
    bree.say "Ah..."
    bree.say "Maybe since he started living with other people?"
    bree.say "People that have a right to privacy?"
    show angela happy at startle
    "Angela laughs and shakes her head at this."
    "And I can't help feeling like she's dismissing everything I just said."
    angela.say "Oh, [hero.name] - you're so funny!"
    show angela a talkative pinch
    angela.say "Now, [mike.name]..."
    angela.say "Come here and give your mother a hug!"
    show angela flirt zorder 1 at center, zoomAt(1.1, (740, 830))
    show mike surprised zorder 2 at center, zoomAt(1.0, (640, 900)), hshake
    show fx exclamation
    with ease
    "Angela proceeds to grab [mike.name] in what I can only describe as a bear-hug."
    "She wraps her arms around him, cramming his head into her chest."
    "And for a moment I'm actually worried she'll smother him with those things!"
    show mike shy blush at center, zoomAt(1.25, (440, 900)) with ease
    "But then [mike.name] breaks away, blushing like a little kid."
    show mike surprised at startle(0.1, 5)
    mike.say "Aw, Mom!"
    mike.say "Not in front of [hero.name]!"
    show mike annoyed
    "All I can do is smile awkwardly."
    "That and try to make things less awkward."
    bree.say "Say, Angela..."
    bree.say "You must be pretty beat after driving all the way over here."
    bree.say "How about we all sit down and have a coffee?"
    show angela happy at startle(0.1, 5)
    angela.say "That sounds wonderful, [hero.name]."
    angela.say "Lead the way!"
    show angela smile
    "I do as I'm told, showing Angela into the kitchen."
    scene bg kitchen
    show angela smile at center, zoomAt(1.1, (840, 830))
    show mike normal at center, zoomAt(1.25, (440, 900))
    with fade
    "Once we're there, [mike.name] and his mom sit down while I make the coffee."
    "They seem to be chatting amongst themselves the whole time."
    "And I can't help listening in to what they're saying."
    "Most of it is innocent stuff."
    "Though it does kind of tip me off to the fact Angela's a possessive mother."
    "Part of me's amazed that she even let [mike.name] move to the big city on his own!"
    "Putting the cups of coffee on a tray, I walk over to join them."
    show angela happy at startle(0.1, 5)
    angela.say "Thank you, [hero.name]."
    angela.say "[mike.name] and I were just talking about his love life."
    show mike surprised blush at startle
    mike.say "MOM!"
    mike.say "Not in front of [hero.name]!"
    show mike shy
    show angela happy at startle
    "Angela laughs and dismisses [mike.name]'s alarm."
    show angela smile
    "And she does it in the exact same way she did with me a few minutes ago."
    "She really doesn't seem to be concerned with embarrassing him at all."
    show angela talkative at startle(0.1, 5)
    angela.say "Don't be silly, [mike.name]."
    angela.say "[hero.name] has to live under the same roof as you."
    show mike happy
    angela.say "So she probably knows more about it than you'd think!"
    show angela talkative
    angela.say "You know, [hero.name] - his father and I are really hoping he meets a nice girl."
    show mike blush
    show mike happy
    angela.say "Specifically the kind of girl that would make a good wife."
    show angela normal
    if hero.morality >= 25:
        "My eyes go wide at this, and I must look shocked."
        show angela smile
        "Because Angela smiles at me, chuckling again."
        show mike happy at startle(0.1, 5)
        angela.say "Why, [hero.name] - you look so demure when you blush."
        angela.say "And to think that I could embarrass you so easily too!"
        show angela smile
        "Angela turns to [mike.name], who looks every bit as embarrassed as me right now."
        "And she nods her head back in my direction as she speaks to him."
        show angela talkative at startle(0.1, 5)
        angela.say "Now that's the kind of girl that I could approve of, [mike.name]."
        angela.say "Polite, well-spoken and even a little innocent too!"
        show angela normal
        show mike surprised at startle
        mike.say "MOM!"
        mike.say "You're showing me up!"
        show mike shy
        show angela talkative at startle(0.1, 5)
        angela.say "Nonsense, [mike.name]."
        angela.say "I'm doing no such thing - am I, [hero.name]?"
        show angela smile
        "I shake my head at this."
        "It's because I'm being put on the spot and don't have an answer."
        "But Angela seems quite happy to assume that I'm agreeing with her."
        show angela happy at startle(0.1, 5)
        angela.say "There, you see?"
        show angela talkative
        angela.say "Now drink up your coffee."
        angela.say "And tell me all about the girls you're seeing!"
    elif hero.morality <= -25:
        "I narrow my eyes at this, and a smile spreads across my face."
        "Angela instantly notices this change in expression."
        show mike normal
        show fx question at right
        show angela worried at startle(0.1, 5)
        angela.say "Did I say something funny, [hero.name]?"
        angela.say "Do you find the idea amusing?"
        show angela annoyed
        "I shake my head, unable to keep from chuckling."
        bree.say "Oh no, no - not at all."
        bree.say "I was just wondering how you'd judge it, you know?"
        bree.say "What a girl has to do to be wife material for [mike.name]?"
        show angela annoyed
        "Angela raises an eyebrow at this."
        "And then she lets out a little snort of derision."
        show angela talkative at startle(0.1, 5)
        angela.say "The traditional stuff, of course."
        angela.say "Caring for my son, making him happy."
        show angela annoyed
        "My smiles gets even wider at this."
        "And by now it must look positively wolfish."
        bree.say "Let's cut to the chase, Angela."
        bree.say "We all know what that really means."
        show angela talkative at startle(0.1, 5)
        angela.say "Oh, do we now?"
        angela.say "And what would that be, [hero.name]?"
        show mike surprised blush at startle
        mike.say "MOM!"
        mike.say "You're showing me up!"
        show mike annoyed
        show angela talkative at startle(0.1, 5)
        angela.say "Nonsense, [mike.name] - be quiet!"
        show angela normal
        bree.say "It means performing in the bedroom, between the sheets."
        bree.say "And I can assure you I know how to do that."
        bree.say "I could even give you and [mike.name] a demonstration - if you'd like?"
        show angela disgusted
        show fx exclamation at right
        "Angela leans back, as if she's disgusted with me."
        "And [mike.name] looks like he's about to have a heart attack!"
        bree.say "Honestly, I can do either one of you - or both!"
        show angela angry
        show mike down
        "Angela stands up and turns towards the door."
        angela.say "[mike.name], I think I'd like to leave now!"
        hide angela with easeoutright
        "She strides out of the kitchen."
        hide mike with moveoutright
        "[mike.name] follows close on her heels."
        "And when they're both gone, I can't help smiling."
        "Because I think that went quite well, all things considered!"
        scene bg livingroom with fade
        return
    else:
        "I narrow my eyes a little at this and shake my head."
        "And I see the gesture instantly register in Angela's own eyes."
        show mike normal
        show fx question at right
        show angela worried at startle(0.1, 5)
        angela.say "What's the matter, [hero.name]?"
        angela.say "Was it something I said?"
        show angela normal
        bree.say "Huh..."
        bree.say "I guess I just think that's a bit old-fashioned, you know?"
        bree.say "The whole looking for the perfect bride kind of thing."
        bree.say "Not really my style."
        show angela annoyed
        "Angela raises an eyebrow at this."
        "And then she lets out a little snort of derision."
        show angela normal at startle(0.1, 5)
        angela.say "Well, I wouldn't worry too much, [hero.name]."
        angela.say "You're not the sort of girl we had in mind anyway."
        show mike surprised blush at startle
        mike.say "MOM!"
        mike.say "You're showing me up!"
        show mike annoyed
        show angela talkative at startle(0.1, 5)
        angela.say "Nonsense, [mike.name]."
        angela.say "I'm just being honest, that's all."
        angela.say "You'd be far more suited to a girl like your sister Minami."
        show angela normal
        "His SISTER?!?"
        "Yeah, because that's not creepy at all!"
        show angela happy at startle(0.1, 5)
        angela.say "Now drink up your coffee."
        angela.say "And tell me all about the girls you're seeing!"
    show angela normal
    "[mike.name] and Angela seem to get into it after that."
    "Their conversation becomes intimate and I feel left out."
    "So I make my excuses and leave them to it."
    scene bg livingroom with fade
    "In fact, it's a relief to get away from the pair of them."
    "My own mother's hard enough to deal with - never mind someone else's!"
    $ angela.flags.angeladelay = TemporaryFlag(True, 6)
    return
label angela_female_event_02:
    if angela.love.max < 40:
        $ angela.love.max = 40
    scene bg mall1
    "Normally I walk around the mall like I'm only there in body, not in spirit."
    "I mean, I know the place so well that my brain tends to wander off on its own!"
    "And that leaves me free to browse my favourite stores on the one hand."
    "While my thoughts are floating freely at the same time too."
    "But today something's different, and it snaps me back to reality."
    "I see a familiar face that I've never encountered here before."
    show angela annoyed at center, zoomAt (1.0, (1040, 720)) with easeinright
    "It's Angela, [mike.name]'s mom, and she looks like she's on a mission."
    show angela at center, traveling(1.1, 0.5, (840, 830))
    "But there's no way for me to avoid an encounter with her."
    show angela at center, traveling(1.5, 0.5, (640, 1040))
    "As Angela's literally walking straight towards me!"
    if hero.morality <= -25:
        show angela disgusted
        angela.say "Oh...it's YOU again!"
        show angela annoyed
        "I give Angela a knowing smile."
        "It's great to know I've been living, rent free, inside of her head!"
        bree.say "Yeah, it's me!"
        bree.say "Hello to you too, Angela!"
    else:
        show angela happy
        angela.say "Oh...hello there."
        angela.say "It's...[hero.name], isn't it?"
        show angela smile
        "I nod, trying to look polite."
        "Maybe I should be grateful she even managed to remember my name!"
        bree.say "That's me..."
        bree.say "And hello to you too, Angela!"
    show angela normal
    bree.say "I didn't expect to see you at the mall."
    bree.say "Don't you and [mike.name]'s dad live out of town?"
    show fx drop
    "Angela looks a little furtive at this."
    "Her eyes dart this way and that."
    "But I can't decide what I said that set her off."
    show angela annoyed
    angela.say "Well...it's a little embarrassing."
    show angela talkative blush
    angela.say "But, woman to woman - I'm shopping for lingerie!"
    angela.say "Specifically something special, for [mike.name]'s dad."
    show angela normal
    "It's an obvious opening, but I can't resist it."
    bree.say "Oh..."
    bree.say "Do your local stores not carry his size?"
    "Angela rolls her eyes at my attempted humour."
    "And then she shakes her head."
    show angela annoyed
    angela.say "I'm serious, [hero.name]!"
    angela.say "I need to liven things up in the bedroom."
    angela.say "But we live in a small town and I don't want word to get around."
    bree.say "Okay, okay...I'm sorry."
    bree.say "But what's the problem?"
    bree.say "The mall has plenty of places that sell super sexy underwear."
    show angela talkative
    angela.say "I...I don't know where they are."
    show angela sad
    angela.say "That's the problem, [hero.name]!"
    "Angela seems pretty desperate, right now."
    "And I guess she could use some help too."
    bree.say "I could show you some places, if you'd like?"
    bree.say "And you can be sure I'll keep it to myself too."
    show angela happy -blush
    "Angela seems instantly touched by the gesture."
    show angela at center, zoomAt (1.65, (650, 1140))
    "She leans in and puts a hand on my shoulder."
    show angela worried
    angela.say "You'd do that for me?"
    angela.say "Oh, [hero.name] - aren't you the sweetest little thing!"
    show angela shy
    "Okay, that was a little condescending."
    "But I can live with it."
    show angela normal
    if hero.morality <= -25:
        scene bg sexshop
        show angela
        with fade
        "I march Angela straight to the most risque store in the mall."
        "Because there's no sense in beating about the bush."
        "Not if she wants [mike.name]'s dad to be beating her bush!"
        "She looks reluctant at first, but she follows me in there."
        "And I make straight for the most outrageous thing I can find."
        bree.say "You should SO get these panties, Angela."
        bree.say "They look really hot."
        bree.say "And they're crotchless too - guys love that!"
    else:
        scene bg clothesshop
        show angela
        with fade
        "I start off by taking Angela to a few of the more vanilla stores in the mall."
        "That seems to help break the ice and lets me get a handle on what she's into."
        "I mean, one girl's risque can be another girl's laundry day pants, you know?"
        "But pretty soon I start to notice something a little bit weird about Angela's tastes."
        bree.say "Ooh, Angela..."
        bree.say "How about this bra and panties?"
        bree.say "They'd go great with the colour of your eyes!"
    show angela disgusted
    "Angela frowns, almost like she's pained looking at my choice."
    "But I see a light in her eyes that tells me she's fighting her instincts."
    "Then she holds up something that's far more plain instead."
    show angela talkative
    angela.say "Oh no, [hero.name]."
    angela.say "I was thinking something more like this, you know?"
    angela.say "This really is more the kind of thing [mike.name]'s dad likes."
    show angela normal
    bree.say "Okay, Angela, whatever you say."
    bree.say "You know the guy better than I do!"
    show bg mall1
    show angela at center, zoomAt (1.5, (640, 1040))
    with fade
    "We walk out of the store with Angela's choice of underwear."
    "But I swear I see her looking longingly back at the stuff I suggested."
    "It's weird, but she seems to be torn over the choice she's made."
    "Maybe it's just me reading too much into the situation."
    "So with that in mind, I make an effort to change the subject."
    bree.say "Soooo..."
    bree.say "You must have like a thousand stories about [mike.name]."
    bree.say "Right, Angela?"
    show angela smile
    "There's no mistaking the smile that spreads across Angela's face."
    "She knows full well that I'm digging for the inside scoop on [mike.name]."
    "And who can blame her for smiling like that?"
    "She's a proud mom, and [mike.name]'s a pretty cool guy."
    "I mean, he can be a jerk at times too."
    "But generally he's cool - and cute..."
    show angela happy
    angela.say "Of course I do, [hero.name]!"
    show angela talkative
    angela.say "Why, I remember this one time."
    angela.say "He must have been all of five years old..."
    show angela normal
    "I keep on nodding while Angela reels off her story."
    "At first I think she's just pausing for effect."
    show angela mindless
    "But then she just keeps quiet, not saying another word."
    "After what feels like forever, I wave a hand in front of her face."
    bree.say "Hey, Angela!"
    bree.say "Are you okay?"
    show angela surprised at startle
    show fx exclamation
    "Suddenly, Angela jerks back to reality."
    "And I jump in surprise too!"
    angela.say "Wha..."
    angela.say "What was that, [hero.name]?"
    bree.say "You...you just kind of tuned out there for a minute."
    bree.say "You were in the middle of telling me a story about [mike.name]."
    bree.say "Then you just went dead silent!"
    show angela sad
    angela.say "Oh..."
    angela.say "Sorry, [hero.name] - I just have a lot on my mind, that's all."
    show angela surprised
    angela.say "Is that the time?"
    show angela annoyed
    angela.say "I have to get back before [mike.name]'s dad gets home."
    show angela normal
    "I look at Angela sideways, trying to size her up."
    "I'm worried that she might not be as okay as she claims."
    "But it's not like I can force her to stay if she wants to leave."
    bree.say "Okay, Angela."
    bree.say "Have a safe journey home."
    bree.say "Oh, and good luck with your purchases!"
    show angela happy
    "Angela smiles and gives me a wave as she turns to walk away."
    hide angela with easeoutleft
    "And all I can do is shrug and watch her go."
    "Part of me wonders if I should tell [mike.name] about my concerns."
    "But then how do I also tell him I went shopping for lingerie with his mom?"
    $ angela.flags.angeladelay = TemporaryFlag(True, 1)
    return

label angela_female_event_03:
    if angela.love.max < 60:
        $ angela.love.max = 60
    scene bg park
    "I didn't come to the park for any specific reason that I could explain."
    "It's just one of those days when I really don't have much I need to do."
    "Sitting on my ass playing videogames was the only other option I had."
    "So instead I decided to venture outside and take a walk around the park."
    "Because fresh air and exercise are always a good thing, right?"
    "At least that's what I keep telling myself as I trudge along the path."
    "Oh yeah, I forgot - nature's boring as hell!"
    "I mean, once you've seen one tree, you've seen them all, right?"
    "With this in mind, I force myself to complete one whole circuit of the park."
    "That way I figure that I can justify heading for home after I'm done."
    "And I finish my walk as quickly as I can, because I hear the Zbox calling me!"
    "Before I reach the exit to the park, I spot someone up ahead."
    show angela annoyed at dark, left5 with dissolve
    "I'm about to steer my way around them and continue on."
    hide angela
    show angela annoyed at left5
    with dissolve
    "But then I recognise them as someone I've met before."
    "Isn't that [mike.name]'s mom?"
    "Agnes?"
    "Angie?"
    "Angela - that's her name!"
    show angela at center, zoomAt (1.25, (460, 870))
    "As I get closer, I'm intending to say hi to her."
    "Maybe even to stop and have a quick chat about whatever."
    show angela at center, zoomAt (1.4, (560, 980))
    "But as I reach her, the look on Angela's face fills me with concern."
    "She looks confused, almost like she's lost!"
    show angela at center, zoomAt (1.5, (640, 1040))
    "I quicken my pace, hurrying over to her."
    bree.say "Angela?"
    bree.say "Is everything okay?"
    "At the sound of my voice, Angela turns to face me."
    show angela surprised
    "She looks surprised to see me walking towards her."
    show angela happy
    "But then I see the light of recognition in her eyes."
    angela.say "[hero.name]!"
    angela.say "It is you, isn't it?"
    show angela smile
    bree.say "Of course it's me, Angela!"
    bree.say "Did you not recognise me from over there?"
    "I point back in the direction from which I came."
    "Maybe that's it - maybe Angela just didn't see me coming."
    "She could be short-sighted and trying to keep it quiet."
    "A lot of people are embarrassed by that kind of thing."
    show angela talkative
    angela.say "I...I don't like to say, [hero.name]."
    angela.say "You're probably not interested in my problems!"
    show angela normal
    bree.say "Don't be silly, Angela."
    bree.say "If there's something wrong, I'd like to help."
    bree.say "That is...if I can help."
    "For a moment I don't think Angela's going to open up to me."
    "But then she treats me to a weary smile and nods her head."
    show angela worried
    angela.say "The truth is, [hero.name]..."
    show angela frustrated
    angela.say "I don't know what I'm doing here!"
    bree.say "Oh, that's SO weird, Angela!"
    bree.say "Me too!"
    show angela surprised
    angela.say "Really?"
    bree.say "Yeah, I just came here on a whim."
    bree.say "Then I ended up wandering around, just getting bored!"
    show angela annoyed
    angela.say "Erm...no, [hero.name]."
    angela.say "That's not what I meant."
    show angela frustrated
    angela.say "I REALLY don't know why I came here!"
    angela.say "One minute I was sitting at home."
    angela.say "And the next I was walking in the park."
    show angela disappointed
    angela.say "Everything in between is just...gone!"
    angela.say "And it keeps happening to me."
    "Without thinking, I take hold of Angela's hand."
    bree.say "That's awful, Angela!"
    bree.say "Have you told anyone about it?"
    bree.say "Are you seeing a doctor?"
    show angela talkative
    angela.say "I'm thinking about making an appointment at the hospital."
    angela.say "But I haven't told [mike.name] or my husband yet."
    angela.say "They both have so much stress in their lives already."
    angela.say "And I don't want to worry them until I know if there's something wrong with me!"
    show angela normal
    "I squeeze Angela's hand, trying to offer her reassurance."
    bree.say "Well you can tell me anything you want to, Angela."
    bree.say "I'd like to think that I'm your friend, okay?"
    bree.say "Is there anything I can do to help?"
    "Angela looks down at her hand clasped in mine."
    "Then she turns her gaze upwards and looks me straight in the eye."
    "Is it just me, or is there suddenly some kind of tension in the air?"
    if hero.morality >= 25:
        "I free my hand as gently as I can, smiling at Angela the whole time."
        bree.say "Of course I mean how can I help out, yeah?"
        bree.say "Like can I give you a lift someplace?"
        bree.say "Maybe be a shoulder to cry on?"
        bree.say "You get my meaning?"
        "Angela stares at me for a moment longer."
        "It's almost as if she's expecting me to say something else entirely."
        show angela happy
        "But then the moment passes, and she simply nods and smiles."
        angela.say "Of course, [hero.name], I understand."
        angela.say "And it's so kind of you to offer."
        angela.say "I'll let you know if I need anything."
        show angela normal
        angela.say "And please, keep this between us, okay?"
        angela.say "I'll let [mike.name] know when the time is right."
        "I nod and we exchange phone numbers."
        hide angela with easeoutright
        "Then we part ways, each walking off in the opposite direction."
    elif hero.morality <= -25:
        "I don't try to pull my hand away from Angela."
        "In fact I reach out and pull her into a tight embrace."
        "I feel her stiffen for a moment, but then she relaxes."
        "The sensation of Angela's body against mine feels so good!"
        bree.say "Don't be too proud to accept a helping hand, Angela."
        bree.say "And don't think I only mean ask stuff like a lift here and there too."
        bree.say "If you need support of a more...intimate kind too."
        bree.say "All you have to do is ask."
        show angela at center, zoomAt (1.75, (650, 1150))
        "I feel Angela's arms tighten around me a moment later."
        show angela flirt
        "And she surprises me by kissing me on the cheek!"
        "But when she ends the embrace, I see she's back in control again."
        show angela happy at center, zoomAt (1.5, (650, 1040))
        angela.say "Of course, [hero.name], I understand."
        angela.say "And it's so kind of you to offer."
        angela.say "I'll let you know if I need anything."
        show angela normal
        angela.say "And please, keep this between us, okay?"
        angela.say "I'll let [mike.name] know when the time is right."
        "I nod and we exchange phone numbers."
        hide angela with easeoutright
        "Then we part ways, each walking off in the opposite direction."
        $ angela.lesbian += 1
    else:
        "I don't try to pull my hand away from Angela."
        "In fact I reach out and take hold of her other hand too."
        bree.say "Don't be too proud to accept a helping hand, Angela."
        bree.say "And don't think I only mean ask stuff like a lift here and there too."
        bree.say "If you need to talk, I can drop everything and pick up the phone."
        "Angela stares at me for a few long seconds."
        "It's like she's weighing something up inside of her head."
        "Then she squeezes my hands in return."
        show angela flirt at center, zoomAt (1.75, (650, 1150))
        "And she surprises me by leaning in to kiss me on the cheek!"
        show angela happy at center, zoomAt (1.5, (650, 1040))
        angela.say "Of course, [hero.name], I understand."
        angela.say "And it's so kind of you to offer."
        angela.say "I'll let you know if I need anything."
        show angela normal
        angela.say "And please, keep this between us, okay?"
        angela.say "I'll let [mike.name] know when the time is right."
        "I nod and we exchange phone numbers."
        hide angela with easeoutright
        "Then we part ways, each walking off in the opposite direction."
    $ angela.love += 1
    $ hero.smartphone_contacts.append("angela")
    $ angela.flags.angeladelay = TemporaryFlag(True, 1)
    $ hero.cancel_activity()
    return

label angela_female_event_04:
    if angela.love.max < 80:
        $ angela.love.max = 80
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Angela")
    if not result:
        $ hero.cancel_event()
        $ angela.love -= 5
        return
    "My phone starts to ring, and I pull it out to check who's calling."
    "But when I see that the call ID says 'Angela', I take it on the spot."
    "If Angela's calling me, then it's probably something pretty important!"
    "Okay, okay...there might some other kind of motivation for me to answer."
    "Maybe something to do with the call being from [mike.name]'s incredibly hot mom!"
    "But I'm already telling myself that's just a coincidence."
    if hero.morality <= -15:
        bree.say "Hey there, Angela..."
        bree.say "Good to hear from you."
        bree.say "And I mean REALLY good!"
    else:
        bree.say "Angela?"
        bree.say "I wasn't expecting a call from you."
        bree.say "Is everything okay?"
    angela.say "Erm..."
    angela.say "I...I really don't know, [hero.name]!"
    "The moment the first word is out of Angela's mouth, I know something is wrong."
    "Her voice is shaky and she's struggling to finish what she's trying to say."
    "And I know instantly that I need to step up and do all I can to help."
    bree.say "Angela..."
    bree.say "You sound like there's something seriously wrong!"
    bree.say "Look, where are you right now?"
    bree.say "Because I can come and find you if you need me to?"
    angela.say "I'm at the hospital, [hero.name]."
    angela.say "Or at least that's where I think I am..."
    menu:
        "I'm on my way!":
            "That's all I need to hear."
            "I'm up and headed for the door before I even reply to Angela."
            bree.say "Stay right where you are, Angela."
            bree.say "I'm on my way."
            angela.say "Oh, thank you, [hero.name]!"
            $ angela.love += 2
            angela.say "I'll be right here waiting for you, I promise."
            "I do the best I can to get to the hospital quickly."
            scene bg hospital with fade
            "And before too long I'm hunting around the place for Angela."
            show angela casual sad with dissolve
            "When I spot her, I feel a flood of relief and hurry over."
            if hero.morality <= -15:
                bree.say "Oh, Angela..."
                bree.say "Your guardian angel is here!"
            else:
                bree.say "ANGELA!"
                bree.say "It's okay - I'm here!"
            show angela normal
            "Angela looks up at the sound of my voice."
            show angela happy
            "And the relief on her face is plain to see."
            angela.say "Thank god you're here, [hero.name]!"
            show angela normal
            angela.say "I didn't want to say it over the phone..."
            show angela sad
            angela.say "But I'm really scared!"
            if hero.morality <= -15:
                bree.say "There's nothing to be scared of, Angela."
                bree.say "Not while I'm here with you."
                bree.say "I'll keep you safe and sound."
            else:
                bree.say "What is it, Angela?"
                bree.say "What are you scared of?"
            show angela disappointed
            "Angela manages a weak smile at this."
            show angela normal at center, zoomAt (1.5, (650, 1040))
            "Which makes me aware of how much she needs my support."
            angela.say "Well..."
            angela.say "It's been happening for a while now - headaches and getting dizzy."
            angela.say "I always wrote it off as stress or women's troubles, you know?"
            angela.say "But the past couple of weeks I've been kind of blacking out."
            angela.say "I'm just going about, doing whatever one moment."
            angela.say "And the next thing I know I'm waking up and it's minutes, even hours later!"
            angela.say "I'm not crazy enough to think I've been abducted by aliens!"
            show angela sad
            angela.say "But I don't know what's behind it."
            "I nod as I listen to everything Angela has to tell me."
            bree.say "And so you're waiting to see the doctor now?"
            bree.say "Or did you already get seen?"
            "Angela shakes her head at this."
            angela.say "Oh no, [hero.name]!"
            show angela normal
            angela.say "I haven't spoken to anyone here yet."
            angela.say "I wanted to talk to you first."
            bree.say "But why, Angela?"
            bree.say "I'm not a doctor!"
            "Angela looks around, a nervous expression on her face."
            "And she makes a gesture with her hand for me to keep it down."
            angela.say "[mike.name]'s father doesn't exactly...trust, doctors."
            show angela annoyed
            angela.say "In fact he'd be angry if he found out I was even here."
            angela.say "He thinks that they're always interfering, trying to control people!"
            show angela normal
            angela.say "I...I guess that sounds a little weird?"
            "It sounds one hundred percent crazy to me."
            "But I try to play it down for Angela's sake."
            bree.say "I guess some people are just eccentric about that stuff, Angela."
            bree.say "But if you're afraid of what he thinks, why did you come to the hospital at all?"
            angela.say "I always listened to him before now, [hero.name]."
            angela.say "But that was before things got this bad."
            angela.say "Now I'm scared there's something really wrong with me."
            show angela annoyed
            angela.say "I...I want to see a doctor, but I'm afraid of what'll happen next!"
            "Angela goes quiet and looks me straight in the eye."
            "Which is as good as her saying she wants my advice."
            menu:
                "You have to see a doctor":
                    "I can see that Angela's genuinely frightened to go against her husband's wishes."
                    "And part of me thinks that this is something I shouldn't be getting myself involved in."
                    "But the fact Angela called me and not, well...anyone else, must mean something."
                    "Like she values my opinion or sees me as one of her most trusted friends."
                    "Or hell, maybe it's the opposite and I'm the only one far-enough removed to see past the bullshit!"
                    "So all I can really do is go with my instinct."
                    bree.say "Cards on the table, Angela..."
                    bree.say "Screw what your husband thinks."
                    bree.say "This is your life we're talking about."
                    bree.say "And that's more important than his weird hang-ups!"
                    "My words don't make Angela's mood improve significantly."
                    show angela normal
                    "But she nods and manages a weak smile all the same."
                    angela.say "Thanks, [hero.name]..."
                    angela.say "You're right - I know you are."
                    angela.say "But I think I just needed to hear it from someone else."
                    $ angela.love += 2
                    "I smile too, and I take Angela by the hand."
                    "Then I lead her over to the reception desk."
                    "Together we arrange for her to see a doctor."
                    hide angela with fade
                    "And then I wait patiently for her appointment to be done."
                    show angela normal at center, zoomAt (1.5, (650, 1040)) with dissolve
                    "When she reappears, Angela actually looks a little more positive."
                    bree.say "How did it go?"
                    angela.say "Well..."
                    angela.say "They ran a lot of tests and told me a lot of what-ifs."
                    angela.say "But I won't know anything for certain until the results come back."
                    $ angela.flags.saw_doctor = True
                "You just need to release your stress":
                    "My instinct is of course to tell Angela that she should see a doctor."
                    "That and to hell with whatever weird hang-ups [mike.name]'s dad might have."
                    "But I can see that Angela's genuinely scared of him finding out."
                    "I have no idea what kind of a guy [mike.name]'s dad is either."
                    "Seeing as how [mike.name] and his mom are cool, I kind of assumed he would be too."
                    "But if he's some kind of secret psycho, the I could be landing Angela in trouble."
                    bree.say "Maybe you should give it a miss this time, Angela."
                    bree.say "Just to keep yourself in his good books."
                    angela.say "But, [hero.name]..."
                    show angela sad
                    angela.say "What if it keeps happening?"
                    angela.say "Or if it gets worse?"
                    $ angela.sub += 1
                    "I let out a frustrated sigh."
                    bree.say "Look, Angela..."
                    bree.say "You're obviously scared of upsetting him."
                    bree.say "If not you'd have just seen the doctor already."
                    bree.say "But it's different now that you've confided in me."
                    bree.say "And if something else happens, you call me first."
                    bree.say "I promise I'll get you back here and in front of a doctor, okay?"
                    "Angela still looks worried."
                    show angela normal
                    "But she nods her head all the same."
                    angela.say "Okay, [hero.name]..."
                    angela.say "I'll do that."
            scene bg taxi with fade
            pause 0.5
            show bg taxi car with dissolve
            "We walk out of the hospital together and I see Angela into a taxi."
            "I'm still not sure that was the right thing to do."
            "But then I'm not sure there's a right and a wrong answer here."
            "And all the possible choices seem to lead to an equally messy end."
            $ hero.flags.went_to_hospital = True
        "I'm calling [mike.name]!":
            "Suddenly I can feel the weight of someone else's problems pressing down on me."
            "I know that Angela's in a bind right now, but I already have so many problems of my own."
            "And this really does sound like it could be something serious."
            "Something that her actual family should be involved with, not someone she hardly knows."
            bree.say "Okay, Angela..."
            bree.say "Just stay where you are."
            bree.say "I'll make sure [mike.name]'s there as soon as possible."
            "There's a moment of silence on the other end of the line."
            "And then Angela finally breaks it."
            angela.say "Do...do you think that's the best thing, [hero.name]?"
            angela.say "I know that [mike.name]'s so busy these days."
            angela.say "I was wondering if you could maybe..."
            bree.say "Oh no, Angela..."
            bree.say "I couldn't possibly make it to the hospital right now!"
            "I feel bad cutting Angela off like that."
            "Even worse that I'm pretty much palming her off onto [mike.name]."
            "But he is her son, so this kind of thing is his responsibility."
            angela.say "Yes, [hero.name]..."
            angela.say "I understand..."
            angela.say "Thank you for your help."
            "I can feel the pangs of guilt stabbing me in the stomach as I end the call."
            "So I do the best I can to assuage them by calling [mike.name] up straight away."
            "I don't know what the significance of Angela calling me before him might be."
            "But I do know that I don't have room for anymore drama in my life right now!"
            $ angela.love -= 2
            $ hero.flags.went_to_hospital = False
    $ angela.flags.angeladelay = TemporaryFlag(True, 3)
    scene bg black with dissolve
    return

label angela_female_event_05:
    if angela.love.max < 100:
        $ angela.love.max = 100
    scene expression f"bg {game.room}"
    "I wasn't expecting to see Angela today, so spotting her comes as a surprise."
    show angela casual disappointed at right with easeinright
    "She doesn't seem to see me at first, and so I make a point of waving to her."
    show angela smile at center with ease
    "Once Angela sees me doing this, her face lights up with recognition."
    if hero.flags.went_to_hospital:
        "But as she hurries over, I remember something that makes me feel terrible."
        if angela.flags.saw_doctor:
            "She was supposed to be letting me know the results of her tests from the hospital."
        else:
            "She was supposed to be letting me know if her blackouts were getting worse."
        "I never heard anything from her, and so it must have slipped my mind."
        "And now I feel like a bad friend for not remembering to call her."
        "Whether things are getting better or worse, I'm expecting Angela to be a little down."
        "So it comes as a surprise when she walks up to me with a cheerful smile on her face."
    show angela happy at center, zoomAt (1.2, (640, 840))
    angela.say "Why, hello, [hero.name]!"
    angela.say "I wasn't expecting us to bump into each other today."
    show angela smile
    if hero.morality <= -20:
        bree.say "I'm always hoping to bump into you, Angela."
        bree.say "Repeatedly, if possible!"
    else:
        bree.say "Me neither, Angela..."
        bree.say "But it's a lucky thing we did, right?"
    bree.say "So..."
    bree.say "Is there any news?"
    "Angela's smile doesn't move an inch as I'm talking."
    "And once I'm done, she keeps on going in a blithe and happy tone."
    show angela happy
    angela.say "That's kind of you to ask, [hero.name]."
    angela.say "But it's nothing out of the ordinary."
    show angela talkative
    angela.say "[mike.name] doesn't call as much as I'd like."
    angela.say "And I worry that he's losing weight."
    angela.say "Aside from that, it's just the same old stuff."
    show angela normal
    angela.say "But then you know that my life's not as exciting as yours!"
    show angela smile
    "I can't help frowning in confusion."
    "It's like Angela doesn't seem to remember the trip to the hospital."
    "Or else she's deliberately choosing not to mention it for some reason."
    menu:
        "Ask about the hospital":
            "I could take it that Angela's got a good reason not to mention it."
            "But that would mean forgetting about how scared she was back in the hospital."
            "And I feel like she really opened up to me that time as well."
            "Like we were making a meaningful connection."
            "So it'd be wrong to just let her get away with it."
            if angela.love >= 90:
                bree.say "Oh, Angela!"
                bree.say "I thought we were much better friends than that."
                bree.say "You really opened your heart to me at the hospital!"
            else:
                bree.say "Come on, Angela!"
                bree.say "Is this some kind of game?"
                bree.say "You can't tell me you forgot about the hospital?"
            show angela mindless
            "Angela blinks and shakes her head."
            show angela surprised
            "For a moment there looks to be spark of recognition in her eyes."
            show angela normal
            "But then she blinks for a second time, and it's gone."
            show angela mindless
            angela.say "Oh don't be silly, [hero.name]!"
            angela.say "My husband and I don't trust doctors at all."
            angela.say "They're always interfering, trying to control people!"
            "Angela stares at me with glassy eyes as she says this."
            "Almost like she's not really hearing what I have to say."
            "It's so weird that I'm starting to feel a little freaked out."
            menu:
                "You don't remember calling me?":
                    "The more Angela denies it, the more I feel the need to insist."
                    "I just can't let it go when one of my friends could be in danger."
                    "I have to keep on pressing, even if it costs me that friendship."
                    bree.say "Angela, please!"
                    bree.say "I don't know why you're doing this."
                    bree.say "But you really need to talk to a doctor!"
                    "I bite my tongue before I say what pops into my head next."
                    "But then I just decide to come out with it."
                    "And to hell with the consequences for me."
                    bree.say "Tell me, Angela..."
                    bree.say "Did your husband find out about the hospital?"
                    bree.say "Did...did he put his hands on you?"
                    show angela protest
                    "Angela's jaw drops open at the accusation."
                    hide angela
                    show angela casual protest
                    "She takes a step backwards, shaking her head."
                    angela.say "[hero.name!u]!"
                    show angela mindless
                    angela.say "How could you even think such a thing?"
                    angela.say "My husband is a perfect gentleman."
                    $ angela.love -= 2
                    angela.say "And we are completely happy together."
                    "As she says all of this, I see that glassy look in her eyes again."
                    "Like she's not really saying the words with the passion I'd expect."
                    bree.say "Angela, please..."
                    "Angela cuts me off by raising a hand."
                    show angela at left with ease
                    "Then she turns her back on me and walks away."
                    hide angela with easeoutleft
                    "And with that, she's gone."
                    "Leaving me even more confused than I was before."
                "If you say so":
                    "I have no idea why Angela's doing this."
                    "But she's not budging, despite my efforts."
                    "So maybe the best thing is to just play along for now."
                    "Then I can dig a little deeper when the chance presents itself."
                    if hero.morality < 0:
                        bree.say "Whatever you say, Angela."
                        bree.say "I get in such a flutter around you sometimes!"
                    else:
                        bree.say "If you say so, Angela."
                        bree.say "I must be mixing you up with someone else."
                    "Angela chuckles politely and waves my words away."
                    angela.say "I'm sure that's it, [hero.name]."
                    show angela happy
                    $ angela.love += 1
                    angela.say "Anyway, I have to be going."
                    angela.say "I'll see you around."
                    show angela normal
                    angela.say "And tell [mike.name] it wouldn't kill him to call his mother!"
                    hide angela with easeoutleft
                    "And with that, she's gone."
                    "Leaving me even more confused than I was before."
        "Don't mention her last phone call":
            "I don't know why Angela wouldn't want to talk about it."
            "Especially after she went to the trouble of calling me."
            "That and the fact that I came all the way to the hospital too!"
            "But then I begin to remember how conflicted she was when I got there."
            "And how she told me about [mike.name]'s dad having a weird thing against doctors."
            "Maybe he found out she was at the hospital somehow."
            "Could his reaction have been so bad she wants to forget it ever happened?"
            "If so, then what choice to I have but to play along?"
            if hero.morality <= -15:
                bree.say "Oh come on, Angela!"
                bree.say "I bet you could teach me a thing or two!"
            else:
                bree.say "Oh, I don't know about that, Angela!"
                bree.say "I'm not exactly setting the world on fire right now either."
            show angela happy at startle
            "Angela chuckles politely and waves my words away."
            angela.say "Oh, [hero.name] - you're too kind!"
            $ angela.love += 1
            show angela normal
            angela.say "Anyway, I have to be going."
            angela.say "I'll see you around."
            angela.say "And tell [mike.name] it wouldn't kill him to call his mother!"
            hide angela with easeoutleft
            "And with that, she's gone."
            "Leaving me even more confused than I was before."
    $ angela.flags.angeladelay = TemporaryFlag(True, 3)
    scene bg black with dissolve
    return

label angela_female_event_06:
    if angela.love.max < 120:
        $ angela.love.max = 120
    "It's been a few days since I last bumped into Angela."
    "And I have to confess that in that time I've kind of forgotten about her issues."
    "Well, I don't mean forgotten about it totally."
    "Not like she seems to have done with the visit to the hospital."
    "I've just kind of had issues in my own life to deal with instead."
    "So when she drops me a text and asks to meet up at the pub, it comes as a surprise."
    "I text back to say that I'm up for it, and then I head down there as soon as I can."
    "Partly because I'm still concerned about Angela and I want to see how she's doing."
    "But also because I was worried she'd decided that our friendship was over."
    "Once I'm down there, I scan the taproom, looking for any sign of Angela."
    "And it doesn't take me long to spot her at a table in the far corner."
    "Upon seeing me, she stands up and waves me over."
    "So I pick my way through the crowd to where she's sitting."
    "Angela smiles sweetly at me and pats the seat next to her."
    show angela casual normal at center, zoomAt(1.5, (640, 1140)) with dissolve
    "An invitation that I'm more than happy to accept."
    angela.say "Hello, [hero.name]..."
    show angela casual normal
    angela.say "Thanks for coming at such short notice."
    if hero.morality <= -10:
        bree.say "I practically ran here, Angela..."
        bree.say "You know that I'd do anything for you!"
    else:
        bree.say "Hey, Angela..."
        bree.say "It's no trouble at all."
        bree.say "I'm always up for spending quality time with you."
    "It seems as though Angela wasn't expecting the compliment."
    show angela blush
    "Because her cheeks flush with colour."
    "Not much, but just enough to be noticeable."
    angela.say "I feel the same way, [hero.name]."
    angela.say "I know we haven't known each other long."
    angela.say "But I feel like in that short time...we've gotten very close."
    show angela -blush
    "Angela pauses and looks down at the table."
    show angela sad
    "As though what she has to say next is going to be difficult for her."
    angela.say "Which, if I'm honest, is why I asked you here."
    angela.say "I wanted to apologise for what happened the last time we met."
    "As soon as she's said this, Angela looks up."
    show angela normal
    "And she looks me in the eye too."
    "God...it's so hard to think when she does that!"
    menu:
        "That's okay.":
            "I don't think this is the time or place to open up old wounds."
            "So I vow not to even mention the trip to the hospital."
            "Because the last thing I want is for Angela to clam up on me again."
            if hero.morality <= -20:
                bree.say "You don't have to apologise to me, Angela."
                bree.say "Not even if you'd done far worse things to me!"
            else:
                bree.say "There's no need, Angela."
                bree.say "It was all just a misunderstanding."
            show angela at startle
            "Angela surprised me by putting her hand atop mine on the table."
            "Then she gives it a squeeze for good measure."
            show angela happy
            angela.say "You have no idea how much that means to me, [hero.name]."
            angela.say "It means that you understand the position I'm in."
            $ angela.love += 2
        "What happened at the hospital?":
            "This feels like the perfect opportunity to bring it up again."
            "Angela must have had a chance to think things over since last time."
            "Or else why would she be trying to build bridges with me now?"
            "She must know I can't just act like it never even happened."
            bree.say "Does that mean you're ready to talk about the hospital now, Angela?"
            bree.say "Because I'm still worried about those blackouts you're having!"
            "From the look on Angela's face, I can see that I just made a mistake."
            show angela annoyed at center, zoomAt(1.5, (640, 1040)) with ease
            "She frowns and shakes her head, making to stand up."
            angela.say "Really, [hero.name]?"
            show angela angry
            angela.say "I thought we were done with this!"
            angela.say "But I obviously thought wrong..."
            "The thought of Angela leaving sends me into a panic."
            with hpunch
            "And without thinking I reach out to grab her by the wrist."
            bree.say "NO!"
            show angela surprised
            "At the sound of me raising my voice, every head in the room turns in our direction."
            "Angela doesn't say a word, she just glances down at where I'm gripping her arm."
            "Quick as a flash, I let go, and this seems to be enough to mollify her."
            show angela annoyed at center, zoomAt(1.5, (640, 1140)) with ease
            "She sits down again slowly, looking me in the eye as she does so."
            bree.say "I..."
            bree.say "I'm sorry, Angela..."
            bree.say "I won't bring it up again - I promise!"
            show angela normal
            "Angela nods, seemingly accepting my apology."
            $ angela.love -= 2
    show angela normal
    "I'm expecting Angela to say more."
    "But instead I see her gaze drawn elsewhere."
    "And when I look up, I could swear she's staring at a girl that just walked in."
    "I can see why anyone would stare at the girl, she's drop-dead gorgeous."
    "But I'm sure Angela's staring at her for the same reason every guy in here is."
    "Alright, alright - and for the same reason I am too."
    "She's staring because she's checking the girl out!"
    if hero.morality <= -25:
        bree.say "Wow..."
        bree.say "Check out the hottie!"
        bree.say "I bet everyone in here wants a piece of that action!"
    else:
        bree.say "She's beautiful, isn't she?"
        bree.say "It's okay, Angela..."
        bree.say "You can be honest with me."
    show angela shock at startle
    "Angela looks at me with shock written all over her face."
    "Like she thinks that I'm going to be outraged or something."
    show angela normal
    "But when she sees that's not the case, her expression softens."
    angela.say "Well, [hero.name]..."
    show angela happy
    angela.say "Since I'm telling you all about myself..."
    angela.say "That's just the kind of girl I used to go for back in pre-med!"
    "My jaw drops open at the audacity of Angela's confession."
    "I look at the gorgeous girl and then back at her."
    if hero.morality <= -25:
        bree.say "Angela, you dirty bitch!"
        bree.say "I've got to admire your taste!"
    else:
        bree.say "You know what, Angela..."
        bree.say "Now you mention it, I can believe that!"
    angela.say "You mean..."
    show angela surprised
    angela.say "You're not shocked?"
    angela.say "Oh dear - things have changed so much since I was young."
    angela.say "People used to freak out when I told them I was into guys AND girls!"
    show angela normal
    menu:
        "I like girls too":
            if hero.morality <= -25:
                bree.say "Oh come on, Angela..."
                bree.say "Who isn't into both?"
                bree.say "I mean, why limit your options?"
            else:
                bree.say "You don't have to hide who you really are with me, Angela."
                bree.say "And if it helps, you should know that I'm bisexual too."
                bree.say "So there's another thing we have in common!"
            show angela surprised
            "Angela looks surprised by my admission at first."
            "But then I see her begin to warm to the idea."
            show angela normal
            angela.say "I...I normally feel quite intimidated."
            angela.say "You know, by women who are open about that kind of thing?"
            angela.say "But it's different with you, [hero.name]."
            show angela blush
            angela.say "And I wonder why that should be..."
            $ angela.love += 2
        "It's more common than you think":
            if hero.morality <= -25:
                bree.say "You shouldn't be ashamed of being bisexual, Angela!"
                bree.say "It's fine to be who you're supposed to be."
                bree.say "I mean, why limit your options?"
            else:
                bree.say "I don't mean to be condescending, Angela..."
                bree.say "But times have changed since then."
                bree.say "Being bisexual is a lot more acceptable now."
            "Angela thinks about it for a moment."
            "And then she nods."
            angela.say "You know what, [hero.name]..."
            angela.say "You're absolutely right."
            show angela blush
            angela.say "I shouldn't keep on hiding that part of me."
            $ angela.sub += 1
    "Angela looks thoughtful for a moment."
    "Like she's pondering something that just occurred to her."
    show angela normal -blush
    angela.say "You know it's weird..."
    angela.say "I used to be really into girls like that."
    angela.say "Back when I was in pre-med..."
    "My ear perk up at this."
    bree.say "Pre-med?"
    bree.say "You mean you're a doctor?"
    bree.say "Wow, Angela - you must be super smart!"
    "Angela waves away my praise."
    show angela happy at startle
    "And she chuckles, shaking her head."
    angela.say "Oh no, [hero.name] - I never completed my studies."
    angela.say "I was all set to be one though."
    show angela normal
    angela.say "In fact it was my ambition since I was a little girl."
    "I can't help frowning at this."
    bree.say "But you gave it all up?"
    bree.say "Why would you do that?"
    angela.say "Because I met [mike.name]'s dad, of course!"
    angela.say "Once he came into my life, my priorities changed."
    angela.say "I couldn't be a doctor as well as a wife and mother!"
    bree.say "Erm..."
    bree.say "Yeah you could."
    bree.say "Women balance their careers with their home-life all the time."
    show angela happy
    angela.say "Oh, [hero.name]..."
    angela.say "That's true today."
    show angela normal
    angela.say "But those were different times."
    bree.say "I don't understand, Angela..."
    bree.say "[mike.name]'s about the same age as me."
    bree.say "And my mom worked a job when I was a kid - she still does."
    show angela happy
    "Angela smiles and shakes her head."
    "Like she's going to dismiss everything I just said."
    show angela normal
    "But then it's her turn to frown."
    angela.say "Wait a minute, [hero.name]..."
    angela.say "That...that makes sense."
    angela.say "I was about to say it didn't...but it does!"
    "Angela's starting to look more and more confused."
    show angela annoyed
    "And I'm beginning to worry this might have something to do with her black-outs."
    "But all I can think to do is trying to change the subject."
    bree.say "So being bisexual AND your career in medicine..."
    bree.say "You gave them both up to be with [mike.name]'s dad?"
    bree.say "Wow...he must be one amazing guy!"
    "Almost as soon as I start talking about her husband, Angela's demeanour changes."
    "Her frown turns into a smile, but I see that same glazed look in her eyes as before."
    angela.say "Oh yes..."
    show angela mindless
    angela.say "My husband is the perfect partner for me!"
    angela.say "And he's made me so happy - I could never think of leaving him!"
    bree.say "Okay..."
    bree.say "This is getting weirder by the second!"
    bree.say "I never even mentioned you leaving the man, Angela!"
    show angela surprised at startle
    "By the time I'm done speaking, Angela seems to have snapped out of it."
    angela.say "Huh?"
    angela.say "What was that, [hero.name]?"
    "From that point on, Angela seems to forget all about the subject."
    show angela normal
    "No matter what I do, she simply avoids it and starts to talk about something else."
    "So in the end I give up and just keep the conversation to neutral topics."
    "This means the rest of the time we're together passes peacefully."
    "And maybe a little tamely too."
    "But once we've said our goodbyes, I'm left wondering."
    "What the hell is going on with Angela in her private life?"
    "I feel like I won't be able to let it go until I have an answer."
    $ angela.flags.angeladelay = TemporaryFlag(True, 1)
    scene bg black with dissolve
    return


label angela_female_event_07:
    scene expression f"bg {game.room}"
    "The first time I notice the poster, it doesn't even register in my mind."
    "It's just another ad for something or other that's been plastered to a wall."
    "But as I keep seeing it throughout the day, something starts to bug me."
    "I mean, it's not the kind of thing that really interests me normally."
    "It's an ad for a magic show happening at a local theatre."
    "There's a typical shot of the magician in his tuxedo and top hat."
    "And it's only when I stop and look at the guy I realise why it's bugging me."
    bree.say "Huh..."
    scene expression f"bg {game.room}" at dark with dissolve
    show dylan staff at opacity(0.5), center, zoomAt (1.5, (640, 1040)) with dissolve
    bree.say "That guy's a dead ringer for [mike.name]!"
    "I take a closer look, thinking that will clear it up for me."
    "After all, it's probably just going to be a coincidence."
    show mike_apparition at opacity(0.5), center, zoomAt (1.30, (640, 870)) with dissolve
    "But the more I scrutinize the poster, the more convinced I become."
    bree.say "Geez!"
    hide dylan with dissolve
    bree.say "Put some grey in his hair and [mike.name] could be this guy!"
    scene expression f"bg {game.room}" with dissolve
    "I start to read some more of the details at the bottom of the poster."
    bree.say "'The amazing Dylan Devant...'"
    bree.say "'And his beautiful assistant Angela...'"
    "Now I see that there's a smaller picture to one side."
    "It's a woman in a revealing outfit and lots of make-up."
    scene expression f"bg {game.room}" at dark with dissolve
    show angela_apparition at opacity(0.5), center, zoomAt (0.60, (640, 840)) with dissolve
    "But there's no mistaking her for [mike.name]'s mom!"
    "Wait a minute..."
    "That would explain the resemblance..."
    "The Amazing Dylan Devant must be [mike.name]'s dad!"
    scene expression f"bg {game.room}" with dissolve
    "I hurry to read the rest of the poster."
    bree.say "'See sleight of hand, escapology and hypnosis...'"
    bree.say "'All live on stage...'"
    "Oh my god!"
    "I can't actually believe [mike.name] never told me his dad was a magician!"
    "And that Angela was his assistant too!"
    "Suddenly I remember all of the strange things Angela's done recently."
    "Calling me to the hospital because she was blacking out."
    "But then behaving like none of it ever happened."
    "Confiding in me that her husband hates doctors."
    "That she gave up her career and more to be with him."
    "But then telling me that she's blissfully happy a moment later."
    "Urgh..."
    "If only this had thrown some light on it all."
    "Instead I have just one more weird thing to add to the growing list."
    $ angela.flags.angeladelay = TemporaryFlag(True, 1)
    return

label angela_investigation_points(points):
    $ game.flags.angelainvestigation += points
    $ NOTIFICATIONS.append(["{image=gui/icons/icon_investigation.png} +" + str(points), 2])
    return

label angela_female_event_08:
    if not hero.flags.done_first_visit:
        "I've tried pretty hard to put what happened with Angela out of my head."
        "I've tried to tell myself that it's between Angela and her husband."
        "That what happens in their marriage is none of my business."
        "But it's no good - I just can't stop thinking about it."
        "Nothing seems to make sense to me."
        "One moment Angela's worried enough to go to the hospital."
        "The next she's denying that she even went there."
        "First she tells me that her husband has all these weird hang-ups."
        "But then she claims that he's the greatest and their marriage is perfect."
        "And on top of all that, there's the fact they're a magician and his assistant."
        "Who the hell knows what that has to do with all of this?!?"
        "In the end I feel like I'm going to go mad if I don't do something."
        "If I don't try to get some answers for the questions bugging me."
        "So that's why I find myself going back to the hospital."
        "I know for certain that I was there with Angela."
        "And I know that she was seen by a doctor there too."
        "If I can just find out the results of those tests."
        "I'm sure it'd help me to get my head around what's going on."
        "Once I'm at the hospital, I make straight for the reception desk."
        "I don't think the receptionist on duty is the same one as before."
        "So she probably won't recognise me from when I was here with Angela."
        show aletta a work at flip, center, zoomAt (1.25, (650, 950)), blacker with dissolve
        "Receptionist" "Hello..."
        "Receptionist" "How can I help you?"
    else:
        "I just don't feel like I got all the answers I was looking for the last time."
        "So I gather up my courage and head back to the hospital again."
        "And I'm hoping that this will be the last time I have to do it."
        "I don't waste any time in walking straight up to the reception desk."
        "The girl sitting behind it looks familiar, probably the same one as last time."
        show aletta a work at flip, center, zoomAt (1.25, (650, 950)), blacker with dissolve
        "Receptionist" "Hello..."
        "Receptionist" "How can I help you?"
        "I breathe a sigh of relief."
        "Because she doesn't seem to recognise me."
    menu:
        "I'm here to take tests reports for a friend":
            bree.say "I was here with a friend the other day."
            bree.say "Her name's Angela..."
            bree.say "And I was wondering if I could see her test results?"
            "As soon as the words are out of my mouth, the receptionist frowns."
            "And I realise I just made a big mistake."
            show aletta a work at center, zoomAt (1.0, (650, 950)), blacker, startle(0.05,-10)
            "Receptionist" "Certainly not!"
            "Receptionist" "Patient confidentiality is of the upmost importance to us."
            "Receptionist" "So there's no way I would ever disclose that information."
            "Receptionist" "And that means this conversation is over!"
            hide aletta with dissolve
            "I turn and walk away from the desk."
            "But then I remember something else from the last time I was here."
            "I swear that I could spot the doctor Angela saw."
            "Maybe I can ask him instead."
        "I need to talk to my friend's doctor":
            "These places aren't known for giving out patient's details on a whim."
            "Especially not to random people that just walk up and ask for them."
            "So I'm going to need to come at this from a different angle."
            "But then I remember something else from the last time I was here."
            "I swear that I could spot the doctor Angela saw."
            "Maybe I should just ask to see him?"
            "Luckily for me, I see him walk by a second later."
            bree.say "Erm..."
            bree.say "I was just here a few days ago."
            bree.say "And I saw that doctor over there."
            "The receptionist look in the direction I'm pointing."
            show aletta a work at center, zoomAt (1.0, (650, 950)), blacker, startle(0.05,-10)
            "Receptionist" "You mean Doctor Pickman?"
            bree.say "Yeah..."
            bree.say "That's the one!"
            show aletta a work at center, zoomAt (1.0, (650, 950)), blacker, startle(0.05,-10)
            "Receptionist" "Well, he's right there."
            "Receptionist" "You can probably catch him now."
            hide aletta with dissolve
            "I nod and hurry over to where the doctor is standing."
            "I can't tell this guy I'm Angela, because he was the one examining her!"
            "So I'm going to have to come up with another plan."
        "Hi, I'm Angela, I'm here for my test results":
            "I put on my best helpless smile."
            "And I get ready to lie like my life depends on it."
            bree.say "Ah..."
            bree.say "My name's Angela..."
            bree.say "I was in here a couple of days ago for some tests."
            bree.say "And I just wanted to know if my results are ready?"
            "The receptionist nods and begins to check her computer."
            show aletta a work at center, zoomAt (1.0, (650, 950)), blacker, startle(0.05,-10)
            "Receptionist" "Hmm..."
            "Receptionist" "You should have got a text message to tell you they were ready."
            "Receptionist" "But sometimes the system gets screwed-up, you know how technology is!"
            "Receptionist" "Just let me check your records..."
            "Receptionist" "What was the surname?"
            "I feel sudden twinge of fear at the realisation I have no idea!"
            "In all the time I've known Angela, and [mike.name] too, they never told me."
            "Sure, I've seen it on [mike.name]'s mail, but it doesn't seem to have sunk in!"
            if hero.has_skill("sneaky"):
                call angela_investigation_points (10) from _call_angela_investigation_points
                "For a moment I rack my brain, trying to think of a solution."
                "And then I see that there's a window behind the receptionist."
                "On it I can clearly see a reflection of her computer screen!"
                "All I have to do then is read down the list of names."
                "And sure enough, I see an Angela on the date we were last here."
                bree.say "It's [mike.family_name]."
                show aletta a work at center, zoomAt (1.0, (650, 950)), blacker, startle(0.05,-10)
                "Receptionist" "Here we are..."
                "Receptionist" "Oh...okay..."
                "Receptionist" "Your notes say that Doctor Pickman has the results."
                "Receptionist" "So you'll have to talk to him."
                "Receptionist" "I believe you'll find him over there."
                "I smile even as I'm cursing inwardly."
                hide aletta with dissolve
                "And I make to walk in the direction she points."
                "I was hoping she's just tell me what I want to know."
                "But it looks like I'm going to have to go higher up the food-chain."
                "And I can't tell this guy I'm Angela, because he was the one examining her!"
            elif hero.knowledge >= 50:
                call angela_investigation_points (10) from _call_angela_investigation_points_1
                "I clear my mind and try to concentrate."
                "Recalling all the times I remember seeing [mike.name]'s name written down."
                "For a few seconds I keep on drawing a blank."
                "But then I have a bolt of almost divine inspiration."
                bree.say "It's [mike.family_name]."
                show aletta a work at center, zoomAt (1.0, (650, 950)), blacker, startle(0.05,-10)
                "Receptionist" "Here we are..."
                "Receptionist" "Oh...okay..."
                "Receptionist" "Your notes say that Doctor Pickman has the results."
                "Receptionist" "So you'll have to talk to him."
                "Receptionist" "I believe you'll find him over there."
                "I smile even as I'm cursing inwardly."
                hide aletta with dissolve
                "And I make to walk in the direction she points."
                "I was hoping she's just tell me what I want to know."
                "But it looks like I'm going to have to go higher up the food-chain."
                "And I can't tell this guy I'm Angela, because he was the one examining her!"
            else:
                "It's no good."
                "I have absolutely no idea."
                bree.say "Erm..."
                bree.say "[mike.name]'s mom?"
                "The receptionist looks up at me."
                "And her expression says it all."
                show aletta a work at center, zoomAt (1.0, (650, 950)), blacker, startle(0.05,-10)
                "Receptionist" "Excuse me..."
                "Receptionist" "But would you mind not wasting my time?"
                "Receptionist" "Because I do not appreciate it!"
                hide aletta with dissolve
                "My head sinks as I slink away from the reception desk."
                "But then I remember something else from the last time I was here."
                "I swear that I could spot the doctor Angela saw."
                "Maybe I can ask him instead."

    if not hero.flags.done_first_visit:
        "I hurry over to where the doctor is standing."
        "He seems to be checking his notes or something like that."
        show victor at flip, center, zoomAt (1.5, (640, 1110)), blacker with dissolve
        "But he looks up as he hears me approaching."
        "And that's when I remember something else about him."
        "He's one of those doctors you think only exists in soap operas."
        "He's young, but not young enough to look like he isn't experienced."
        "And he's handsome too, but not so handsome that he seems out of reach."
        show victor at center, zoomAt (1.0, (640, 1110)), blacker, startle(0.05,-10)
        "Doctor" "Oh..."
        "Doctor" "Hello there..."
        "Doctor" "Is there something I can help you with?"
        if hero.morality >= 0:
            bree.say "Are..."
            bree.say "Are you Doctor Pickman?"
        else:
            bree.say "I can think of a dozen things straight off!"
            bree.say "But first, I need to know -are you Doctor Pickman?"
        "The doctor glances down at the ID card hanging around his neck."
        "And then he looks back up at me with a winning smile."
        show victor at center, zoomAt (1.0, (640, 1110)), blacker, startle(0.05,-10)
        "Doctor" "That's what it says here!"
        "Doctor" "So I guess I must be."
        if hero.morality >= 0:
            "I can't help giggling like a fool."
            "And feeling thankful this guy isn't my gynaecologist!"
        else:
            "I can't help laughing at this."
            "And wishing this guy was my gynaecologist!"
        bree.say "Okay, Doctor..."
        bree.say "The thing is, I came in here with a friend the other day."
        bree.say "Her name is Angela."
        bree.say "She was worried because she'd been having black-outs."
        "The doctor nods as he listens to me."
        "And he seems to be genuinely concerned."
        "Which, of course, makes him instantly that much hotter!"
        show victor at center, zoomAt (1.0, (640, 1110)), blacker, startle(0.05,-10)
        "Doctor" "I see..."
        "Doctor" "She was right to come and get that checked out!"
        bree.say "I think so too!"
        bree.say "And you told her to come back and collect her results later."
        "The doctor nods again."
        "But this time he frowns a little too."
        show victor at center, zoomAt (1.0, (640, 1110)), blacker, startle(0.05,-10)
        "Doctor" "Yes, that's pretty standard around here."
        "Doctor" "I'm sorry, I don't see where this is going!"
        "I can feel myself starting to get a little flustered."
        "Because the doctor's right, I'm not making myself clear."
        bree.say "She's denying it ever happened!"
        bree.say "That's the problem!"
        bree.say "And I don't know why she's doing it either."
        "I can see a look of concern creeping over the doctor's face."
        "But when he actually comes to speak, he shakes his head."
        show victor at center, zoomAt (1.0, (640, 1110)), blacker, startle(0.05,-10)
        "Doctor" "I'm sorry to hear that."
        "Doctor" "It sounds very strange."
        "Doctor" "But I don't see what it has to do with us here at the hospital."
        "Doctor" "I mean, memory loss could be a symptom of a cranial issue."
        "Doctor" "But then again, your friend could be suffering from psychological issues too."
        "Doctor" "Or she could even just be choosing to pretend she never came here at all."
        "The worst thing about all of this is that he's one hundred percent right."
        "Which means that I'm going to have to ask him to go above and beyond for me."
        bree.say "I think it's something to do with what the tests showed up."
        bree.say "And if could just get a chance to maybe look at them?"
        bree.say "I...I know that's against the rules..."
        "I'm expecting the doctor to shut me straight down."
        "But instead he looks around for a moment."
        "Almost like he's checking there's nobody within earshot."
        show victor at center, zoomAt (1.0, (640, 1110)), blacker, startle(0.05,-10)
        "Doctor" "It's absolutely one hundred percent against the rules!"
        "Doctor" "But, unlike some of my colleagues, I sometimes bend those rules."
        bree.say "What are you saying?"
        show victor at center, zoomAt (1.0, (640, 1110)), blacker, startle(0.05,-10)
        "Doctor" "Well..."
        "Doctor" "Being a doctor brings with it some perks."
        "Doctor" "But there are others that aren't, shall we say, standard?"
        if hero.morality >= 0:
            bree.say "You..."
            bree.say "You want a bribe?"
        else:
            bree.say "Oh, I see where this is going!"
            bree.say "You want me to offer you an incentive?"
        show victor at center, zoomAt (1.0, (640, 1110)), blacker, startle(0.05,-10)
        "Doctor" "You could put it that way."
        "Doctor" "I'd prefer to think of it as a show of gratitude!"
        "Doctor" "After all, you are asking me to take a risk."
    else:
        "I hurry over to where the doctor is standing."
        "He seems to be checking his notes or something like that."
        show victor at center, zoomAt (1.5, (640, 1110)), blacker with dissolve
        "But he looks up as he hears me approaching."
        "And I see recognition in his eyes."
        show victor at center, zoomAt (1.0, (640, 1110)), blacker, startle(0.05,-10)
        "Doctor" "Hello again."
        "Doctor" "Back for more, are we?"
        "I can already feel myself blushing."
        "But I do the best I can to control myself."
        bree.say "That's right."
        bree.say "And this time I'm not leaving until I get what I want!"
        show victor at center, zoomAt (1.0, (640, 1110)), blacker, startle(0.05,-10)
        "Doctor" "Oh really?"
        "Doctor" "So what are you offering me this time?"
    menu:
        "A kiss might help":
            if hero.morality >= 0:
                "It feels wrong to be doing things this way."
                "Somehow I thought a doctor would be more above wanting a bribe."
            else:
                "I should have known I'd have to bribe this guy!"
                "And just offered him something sweet straight off the bat!"
            "But if I have to offer him an incentive, just something small..."
            "I reach up and put my arms around the doctor's neck."
            scene bg hospital
            show doctor kiss
            with fade
            "Then I pull him towards me and place my lips against his."
            "He doesn't resist, letting me push my tongue into his mouth."
            "I clear my mind and focus in nothing but the kiss."
            "That way I can make sure that it's hot and lingering."
            "But most of all that it's memorable and leaves him wanting more."
            "For his part, he seems to enjoy it."
            "He leans in and returns the kiss with serious enthusiasm."
            "And I know I must be doing something right."
            "Because I can feel his cock hardening against my thigh."
            "When it's over, he straightens up and lets out a sigh."
            hide doctor kiss
            show victor at flip, center, zoomAt (1.5, (640, 1110)), blacker
            with fade
            "Then he nods."
            show victor at flip, center, zoomAt (1.0, (640, 1110)), blacker, startle(0.05,-10)
            "Doctor" "Okay..."
            "Doctor" "For that much I'll tell you this..."
            "Doctor" "Your friend really did come in here."
            "Doctor" "And she did take a series of tests."
            "I wait silently, expecting him to say more."
            "But instead he just looks me in the face and smiles."
            bree.say "Yeah, and..."
            bree.say "What about the results?"
            call angela_investigation_points (15) from _call_angela_investigation_points_2
            if hero.morality > -15:
                $ hero.morality -= 1
        "Money always helps" if hero.money >= 50:
            if hero.morality >= 0:
                "It feels wrong to be doing things this way."
                "Somehow I thought a doctor would be more above wanting a bribe."
            else:
                "I should have known I'd have to bribe this guy!"
                "And just offered him something sweet straight off the bat!"
            "But if I have to offer him an incentive, maybe money will be enough."
            "At least that way I can keep my dignity and self-respect!"
            bree.say "Here..."
            "I start to pull out my purse and rummage through it."
            "Then I collect up all the notes I have on me."
            bree.say "This is all I have to give you."
            bree.say "Please tell me it's enough!"
            "Luckily for me I'm carrying a little more money than I normally would."
            "But I'm still worried that it won't be enough to persuade him."
            "I wait as the doctor glances down at the wad of notes in my hand."
            "For a moment I'm sure that he's going to refuse to take it."
            "But then he lets out what sounds like a disappointed sigh."
            "And he brushes up against me."
            "At first I don't realise what he's doing."
            "Then I feel him grab the money out of my hand."
            $ hero.money -= 50
            "And I realise he's trying to take it without being seen."
            show victor at flip, center, zoomAt (1.0, (640, 1110)), blacker, startle(0.05,-10)
            "Doctor" "Okay..."
            "Doctor" "For that much I'll tell you this..."
            call angela_investigation_points (25) from _call_angela_investigation_points_3
            if hero.morality > -15:
                $ hero.morality -= 1
        "A quick blowjob won't hurt" if hero.morality <= -25:
            if hero.morality >= -30:
                "It feels wrong to be doing things this way."
                "Somehow I thought a doctor would be more above wanting a bribe."
            else:
                "I should have known I'd have to bribe this guy!"
                "And just offered him something sweet straight off the bat!"
            "But if I have to offer him a good enough incentive..."
            "So I reach out and take hold of his hand."
            bree.say "Okay, doctor..."
            bree.say "Where can we go for a consultation?"
            bree.say "Somewhere a little more...private?"
            "I don't have to make my meaning any more plain."
            "The doctor nods and quickly leads me a little way down the corridor."
            scene doctor_fuck_bg
            show victor at flip, center, zoomAt (1.5, (640, 1110)), blacker
            with fade
            "And then he guides me into what looks like an examination room."
            "It has a medical bed, a few chairs, and most importantly a lock on the door."
            "I watch as the doctor turns the tab and it clicks, giving us some privacy."
            show victor at center, zoomAt (1.0, (640, 1110)), blacker, startle(0.05,-10)
            "Doctor" "So..."
            "Doctor" "About this incentive..."
            "I answer him by getting straight down on my knees."
            "And then reaching out to undo his flies."
            "The doctor's question dies in his mouth."
            "And he seems more than happy to let me get down to business."
            "My urge is to get this over with as soon as possible."
            "But if I do that, I risk him being pissed off with the result."
            "And that could make him less likely to tell me what I want to know."
            "So instead I settle on making this a no-frills affair."
            "I reach into his pants and pull out his cock without hesitation."
            scene bg black
            show bree cinema bj mike doctor hospital
            with fade
            "Not stopping to indulge in any real foreplay or teasing."
            "Luckily for me it seems the doctor is already more than a little excited."
            "The fact that his cock is almost all the way there tells me he likes this kind of thing."
            "And for a moment I wonder how many times he's done this in the past."
            "With women in my position, with nurses, maybe even with his patients."
            "That last possibility has serious implications."
            "So I do the best I can to push it aside."
            "Instead I put all of my attention into massaging his shaft."
            "He's not a small guy, and pretty soon it's as big as it's going to get."
            "Which means it's time for me to take a deep breath and begin."
            "Licking my lips, I part them and start to kiss the tip."
            "From there I move on to taking it into my mouth."
            "All the time I'm nuzzling with my teeth and licking with my tongue."
            "I can soon tell that I was right in thinking I won't have to work hard."
            "The smallest effort on my part seems to make the doctor quiver with delight."
            "So I guess I was also right in thinking that he gets off on this kind of thing."
            "Knowing that, I'm sure to make plenty of nods to his preferences."
            show bree cinema bj mike doctor hospital at startle(0.1, 15)
            "I take him deeper and deeper into my mouth."
            "And as I do so, I make almost desperate panting sounds."
            "In short I do everything I can to make him think he's the one with the power."
            show bree cinema bj mike doctor hospital at startle(0.1, 15)
            "Pretty soon my head is going back and forth as fast as I can make it move."
            "I'm doing the best I can to get his cock so deep it can't go any further."
            "Doctor" "Mmm..."
            "Doctor" "Yes...yes..."
            "Doctor" "Just like that!"
            show bree cinema bj mike doctor hospital at startle(0.1, 15)
            "At the sound of his voice, I redouble my efforts."
            "Doing the best I can to make it seem like I'm obeying him."
            show bree cinema bj mike doctor hospital at startle(0.1, 15)
            "And it seems like that's just what he needs to push him to the next level."
            "I can already feel his body tensing, his muscles starting to twitch."
            show bree cinema bj mike doctor hospital at startle(0.1, 15)
            "Which means I need to decide how I'm going to end this."
            menu:
                "Swallow":
                    "I feel like I've done this guy enough favours already."
                    "And so when the time comes, I just keep right on going."
                    with vpunch
                    "As the doctor shoots his load, I swallow it down."
                    show bree cinema bj cum with vpunch
                    "Luckily for me, I'm able to handle it pretty easily."
                    "So the whole thing ends without a hitch."
                "Pull out":
                    "I figure that as I'm trying to bribe this guy, I need to sweeten the deal."
                    "So before the end comes, I gently guide his cock out of my mouth."
                    "The doctor looks puzzled and a little disappointed at this."
                    "But his mood seems to pick up a moment later when he loses it."
                    with vpunch
                    "Because when that happens, he shoots his load straight into my face."
                    with vpunch
                    "I gasp, mouth and eyes wide open as it hits me."
                    "Doing the best I can to look shocked and taken by surprise."
            call angela_investigation_points (50) from _call_angela_investigation_points_4
            scene doctor_fuck_bg
            show victor at flip, center, zoomAt (1.5, (640, 1110)), blacker
            with fade
            "Once it's all over and done, I clean myself up."
            "At the same time, the doctor is making himself presentable too."
            if hero.morality > -40:
                $ hero.morality -= 2
            else:
                $ hero.morality -= 1
        "Offer a private consultation" if hero.morality <= -50:
            if hero.morality >= -55:
                "It feels wrong to be doing things this way."
                "Somehow I thought a doctor would be more above wanting a bribe."
            else:
                "I should have known I'd have to bribe this guy!"
                "And just offered him something sweet straight off the bat!"
            "But if I have to offer him a good enough incentive..."
            "So I reach out and take hold of his hand."
            bree.say "Okay, doctor..."
            bree.say "Where can we go for a consultation?"
            bree.say "Somewhere a little more...private?"
            "I don't have to make my meaning any more plain."
            "The doctor nods and quickly leads me a little way down the corridor."
            scene doctor_fuck_bg
            show victor at flip, center, zoomAt (1.5, (640, 1110)), blacker
            with fade
            "And then he guides me into what looks like an examination room."
            "It has a medical bed, a few chairs, and most importantly a lock on the door."
            "I watch as the doctor turns the tab and it clicks, giving us some privacy."
            show victor at center, zoomAt (1.0, (640, 1110)), blacker, startle(0.05,-10)
            "Doctor" "So..."
            "Doctor" "About this incentive..."
            "By way of an answer, I turn my back on him."
            "And then I walk over to the examination bed."
            "For a moment I think about climbing up onto it."
            "But then I take a look back over my shoulder."
            "And I can see that's not going to be necessary."
            "He looks more than excited right now."
            "Almost like he's fighting to keep himself under control."
            "And for a moment I wonder how many times he's done this in the past."
            "With women in my position, with nurses, maybe even with his patients."
            "That last possibility has serious implications."
            "So I do the best I can to push it aside."
            "Then I lean over the bed and reach back with both hands."
            "I use them to pull down my panties, giving him a clear view up my skirt."
            "The first thing I know about him being there is the sensation of him grabbing my haunches."
            "And then I feel the sensation of him thrusting himself up against me."
            "I can't help letting out a yelp of surprise."
            "Because it's then I realise he already has his cock out."
            "It's bigger than I expected it to be, and so hard it's ready to go."
            "So I guess this is going to be a no-frills affair!"
            "All the better from my point of view."
            "It seems like the doctor enjoys being the one in control."
            "As I feel him reach down between my legs."
            scene bg black
            show doctor fuck
            with fade
            "And then he begins to tickle and tease the lips of my pussy."
            "The moan that I let out then is only partly for show."
            "Because it feels like he's putting his anatomical knowledge to good use!"
            "I was worried that I'd have to fake it to pull this off."
            "But instead the doctor's fingers ensure that won't be necessary."
            "I can already feel myself getting warm and slick."
            "And the pleasure from the sliding of his fingers is becoming ever more intense."
            "Just when I think it can't get hotter or heavier, he takes it to the next level."
            "The doctor suddenly thrusts forwards with his cock, pushing his way into me."
            "As wet and willing as he's managed to get me, it still doesn't happen easily."
            "Every fraction of an inch meets with resistance, and it's crazily intense."
            "All I can do is hold onto the edge of the bed for dear life!"
            "Because I can tell that this guy isn't going to stop until he's spent."
            show doctor fuck at stepback(0.07, -10, 0)
            "Almost as soon as he's as deep inside as he can go, the doctor kicks it up a gear."
            "He doesn't wait to savour the sensation, or let me enjoy it either."
            show doctor fuck at stepback(0.07, -10, 0)
            pause 0.2
            show doctor fuck at stepback(0.07, -10, 0)
            "Instead he starts thrusting in and out of me as if his life depends on it."
            "Every time I'm pushed hard against the desk, gasping at the feeling."
            "But he's always in motion, preparing to do it again before my senses catch up."
            show doctor fuck at stepback(0.07, -10, 0)
            pause 0.2
            show doctor fuck at stepback(0.07, -10, 0)
            "I can't remember the last time someone fucked me this hard or this fast."
            "And to think, just a few minutes before he was as calm as he could ever be!"
            show doctor fuck at stepback(0.07, -10, 0)
            pause 0.2
            show doctor fuck at stepback(0.07, -10, 0)
            "My fingers are holding so hard the edge of the desk."
            "I can hear the wood creaking under the pressure."
            show doctor fuck at stepback(0.07, -10, 0)
            pause 0.2
            show doctor fuck at stepback(0.07, -10, 0)
            "Doctor" "Mmm..."
            "Doctor" "Yes...yes..."
            "Doctor" "Just like that!"
            "From the sound of his voice, I can tell he's almost there."
            with vpunch
            "And a moment later I feel his muscles clench."
            with vpunch
            "Then he shoots his load into me."
            with vpunch
            "There's no time to even think about it."
            "It just happens, and his climax pushes me to mine too."
            scene doctor_fuck_bg
            show victor at flip, center, zoomAt (1.5, (640, 1110)), blacker
            with fade
            "Once it's all over and done, I clean myself up."
            "At the same time, the doctor is making himself presentable too."
            $ hero.morality -= 5
            call angela_investigation_points (100) from _call_angela_investigation_points_5
        "Just leave":
            "I desperately want to see those test results."
            if hero.morality >= 25:
                "But the thought of having to perform certain acts to get them..."
                "Well, it just feels like too much, like one step too far."
            if hero.morality <= -25:
                "But I'm not turning tricks for them."
                "This guy doesn't deserve what I have to offer!"
            "So I take a deep breath and then shake my head."
            bree.say "You know that helping me out would be the right thing to do."
            bree.say "But I guess you're not a good enough person to do what's right for its own sake."
            bree.say "And I'm not going to sacrifice my own morals for your gratification."
            "The doctor nods and smiles as I say all of this."
            show victor at center, zoomAt (1.0, (640, 1110)), blacker, startle(0.05,-10)
            "Doctor" "Very righteous, very admirable."
            "Doctor" "It leaves you right back where you started."
            "Doctor" "But at least you have your sense of moral superiority for comfort!"
            "Doctor" "Anyway...if you change your mind, you know where to find me."
            hide victor with easeoutright
            "With that, he turns on his heel and walks away."
            "Which leaves me with no other choice but to leave."
            scene bg street with fade
            "So I slink out of the hospital and make my way home."
            $ game.room = "street"
            scene bg black with dissolve
            return
    if game.flags.angelainvestigation >= 100:
        bree.say "So..."
        bree.say "Now it's time for you to keep your side of the deal!"
        show victor at center, zoomAt (1.0, (640, 1110)), blacker, startle(0.05,-10)
        "Doctor" "Sure, sure..."
        "Doctor" "The long and short of it is that your friend's fine."
        bree.say "You actually mean that?"
        bree.say "There's nothing wrong with Angela?"
        "The doctor nods."
        show victor at center, zoomAt (1.0, (640, 1110)), blacker, startle(0.05,-10)
        "Doctor" "Nothing showed up on the tests."
        "Doctor" "Nothing that would explain blackouts."
        bree.say "Wait a second..."
        bree.say "You mean the blackouts are not real?"
        show victor at center, zoomAt (1.0, (640, 1110)), blacker, startle(0.05,-10)
        "Doctor" "Oh yes, they're real."
        "Doctor" "But whatever's causing them isn't physiological."
        "Doctor" "I'd have liked to run more tests, maybe refer her to a psychologist."
        bree.say "So why didn't you do that?"
        bree.say "Did she turn you down?"
        bree.say "Like she told me none of this ever happened?"
        "The doctor shrugs."
        show victor at center, zoomAt (1.0, (640, 1110)), blacker, startle(0.05,-10)
        "Doctor" "The truth is that your friend never actually came back here at all."
        "Doctor" "It was her husband that turned up to collect the test results."
        "Doctor" "And when I brought up the matter of a psychologist, he said it wasn't necessary."
        "Now I really am starting to get confused."
        bree.say "But why?"
        bree.say "Angela told me her husband's pretty much perfect!"
        bree.say "Why wouldn't he want to take your advice?"
        show victor at center, zoomAt (1.0, (640, 1110)), blacker, startle(0.05,-10)
        "Doctor" "He said that he already knew what was wrong with her."
        "Doctor" "He told me she'd been diagnosed with a psychological condition."
        "Doctor" "What's more, he insisted that if she turned up here again, we should call him."
        "Doctor" "Anyway..."
        "Doctor" "I have to get back to work before I'm missed."
        "Doctor" "I hope that helps you - because you definitely helped me!"
        hide victor with easeoutright
        "With that, he turns on his heel and walks to the door."
        "Then he unlocks it and leaves without a backwards glance."
        scene bg hospital with fade
        "I hurry to leave too, walking out of the hospital."
        scene bg street with fade
        "On the way home my mind is racing with this new information."
        "Is what Angela's husband said true?"
        "Does she really have a psychological condition?"
        "If so, that would explain the strange ways she's been behaving."
        "But something just doesn't feel right about all of this."
        "My mixed-up feelings for Angela probably aren't helping."
        "And maybe they're making me biased against her husband."
        "But I just can't see what he's doing as the actions of a caring spouse."
        "Instead they come across as suspicious and controlling."
        "I wish I could just talk to Angela, without her denying what actually happened."
        "Until that happens, I don't think I'm going to be able to let this thing go."
        $ game.room = "street"
        if angela.love.max < 140:
            $ angela.love.max = 140
        $ game.flags.angela_test_results = True
        scene bg black with dissolve
        return
    elif game.flags.angelainvestigation >= 50:
        bree.say "So..."
        bree.say "Now it's time for you to keep your side of the deal!"
        show victor at center, zoomAt (1.0, (640, 1110)), blacker, startle(0.05,-10)
        "Doctor" "Sure, sure..."
        "Doctor" "The long and short of it is that your friend's fine."
        bree.say "You actually mean that?"
        bree.say "There's nothing wrong with Angela?"
        "The doctor nods."
        show victor at center, zoomAt (1.0, (640, 1110)), blacker, startle(0.05,-10)
        "Doctor" "Nothing showed up on the tests."
        "Doctor" "Nothing that would explain blackouts."
        bree.say "Wait a second..."
        bree.say "You mean the blackouts are real?"
        "The doctor shrugs as he walks to the door."
        "Doctor" "You only asked me about the tests."
    elif game.flags.angelainvestigation >= 25:
        show victor at center, zoomAt (1.0, (640, 1110)), blacker, startle(0.05,-10)
        "Doctor" "Your friend really did come in here."
        "Doctor" "And she did take a series of tests."
        "I wait silently, expecting him to say more."
        "But instead he just looks me in the face and smiles."
        bree.say "Yeah, and..."
        bree.say "What about the results?"
    "The doctor keeps on smiling as he shakes his head."
    show victor at center, zoomAt (1.0, (640, 1110)), blacker, startle(0.05,-10)
    "Doctor" "I'm afraid that's all you get."
    "Doctor" "Unless you want to offer me something more valuable?"
    "Doctor" "Anyway...if you change your mind, you know where to find me."
    hide victor with easeoutright
    "With that, he turns on his heel and walks away."
    "Which leaves me with no other choice but to leave."
    scene bg street with fade
    "So I slink out of the hospital and make my way home."
    scene bg black with dissolve
    $ game.room = "street"
    $ hero.flags.done_first_visit = True
    $ angela.flags.angeladelay = TemporaryFlag(True, 1)
    return


label angela_female_event_09:
    play sound cell_vibrate
    "I feel my phone vibrating, so I pull it out and casually check the caller ID."
    "The truth is that I've been more than a little distracted recently, pretty out of it."
    "After what happened between Angela and me at the hospital the other day..."
    "Well, let's just say that I'm still trying to figure that one out!"
    "But all of that confusion disappears the moment I see exactly who's calling."
    "It's Angela!"
    $ result = renpy.call_screen("smartphone_choice", "Angela")
    if not result:
        $ do_event.flags.canceled = True
        $ angela.love -= 5
        return
    if angela.love.max <= 160:
        $ angela.love.max = 160
    "Without hesitation, I take the call."
    "And I swear I can already feel my heart starting to beat faster!"
    "Even so, I do the best I can to keep my emotions under control."
    bree.say "Angela?"
    bree.say "I wasn't expecting..."
    angela.say "[hero.name]?!?"
    angela.say "Are you on your own?"
    angela.say "[mike.name]'s not there with you, is he?"
    "I'm instantly thrown by Angela's tone of voice on the other end of the line."
    "She sounds anxious, even panicked, which is not like her at all."
    bree.say "What's the matter, Angela?"
    bree.say "Is everything okay?"
    angela.say "I need you to answer the question, [hero.name]!"
    angela.say "Are you on your own?!?"
    bree.say "Y...yeah, Angela..."
    bree.say "I'm on my own - there's nobody else here right now."
    "I hear Angela let out a sigh of relief."
    "I could start to question her again, hoping for a better result this time."
    "But I decide to keep quiet and see what she says next."
    angela.say "Good...that's good..."
    angela.say "Look, [hero.name]..."
    angela.say "I need you to do something for me, okay?"
    bree.say "Like I already said, Angela..."
    bree.say "Whatever you need, I'll do it!"
    angela.say "Okay, okay..."
    angela.say "I'm going to send you a text with a hotel and a room number."
    angela.say "Meet me there as soon as you can."
    angela.say "I'll explain everything when you get here."
    bree.say "Angela..."
    bree.say "Wait..."
    scene expression f"bg {game.room}"
    "My words go unanswered as Angela ends the call and leaves me hanging."
    "A moment later the text message she mentioned arrives."
    "I open it without stopping to pause for breath."
    "And sure enough, all that it contains is the name of a hotel and a room number."
    "I shake my head as I put my phone away and think about my next move."
    "I guess this is where I find out whether or not all those things I said were true."
    "Because Angela just told me where she is and made it clear there's something wrong."
    "I could easily get hold of [mike.name] or call the police and tell them my concerns."
    scene bg house with fade
    "But I'm already headed out the door and planning my route to the hotel."
    "So I that's the answer to the question - I did mean what I said!"
    scene bg door black secure at center, zoomAt(1, (640, 720)) with fade
    "Getting to the hotel and finding the room proves to be the easy part."
    "What's hard comes when I finally get there."
    "And it's summoning the courage to knock on the door."
    "I don't know what I'm more afraid of as I do so."
    "The chance of finding Angela after she's done something desperate."
    "Or just walking in there and finding her unharmed."
    "Because in the case of the latter, I still have to talk this out with her!"
    show bg door black secure at center, traveling(1.5, 0.3, (640, 1040))
    pause 0.3
    play sound door_knock
    "I take a deep breath, lean in close, and then rap my knuckles on the door."
    bree.say "Angela?"
    bree.say "Are you in there?"
    bree.say "It's [hero.name]!"
    scene bg black with dissolve
    pause 0.5
    scene bg hotelroom at center, zoomAt(1.5, (640, 1040)), dark
    show angela frustrated at center, zoomAt(1.5, (640, 1040))
    with hpunch
    "I almost tumble into the room as Angela opens the door."
    "Was she waiting behind it this whole time, looking through the peephole?"
    "I don't have time to ask the question, as she bundles me inside."
    scene bg hotelroom
    show angela frustrated at center, zoomAt(1.25, (840, 880))
    with hpunch
    "The same momentum that almost saw me fall over carries me a good few feet into the room."
    "And I just have time to turn around and see Angela locking the door behind me."
    bree.say "Whoa..."
    angela.say "You came straight here, right?"
    angela.say "You didn't tell anyone, like I asked?"
    angela.say "You made sure you weren't followed?!?"
    bree.say "Whoa, Angela!"
    bree.say "Slow down!"
    bree.say "I'm here like you asked, okay!"
    "My words seem to have an effect on Angela."
    show angela normal
    "She stops talking and tries to breathe more slowly."
    show angela at center, zoomAt(1.25, (540, 880)) with ease
    pause 0.5
    show angela at center, zoomAt(1.25, (540, 980)) with ease
    "Then she walks past me and sits down on the bed."
    show angela sad
    angela.say "I'm sorry, [hero.name]..."
    angela.say "I've been on my own in this room for too long."
    show angela frustrated
    angela.say "I'd have called you sooner."
    angela.say "But I had to let the trail go cold first!"
    "I can't help frowning, as none of that sounds good."
    bree.say "Let the trail go cold?"
    bree.say "Angela, you're starting to scare me!"
    bree.say "What are you talking about?"
    with hpunch
    "Rather than answering my question, Angela grabs me by the wrist."
    show angela frustrated at center, zoomAt(1.5, (640, 1140)) with vpunch
    "Then she pulls me down to sit beside her on the bed."
    show angela angry
    angela.say "I figured it out, [hero.name]!"
    angela.say "I figured out what's been happening to me!"
    angela.say "Or at least I figured out WHO's been doing it to me..."
    show angela annoyed
    "Angela pauses and glances around the room."
    "It's as if she's still scared of someone overhearing us."
    bree.say "You...you mean the problems with your memory?"
    show angela frustrated
    angela.say "It's my husband, [hero.name]!"
    show angela angry
    angela.say "My own husband's been doing this to me!"
    show angela frustrated
    "I shake my head, unable to believe what I'm hearing."
    bree.say "You mean [mike.name]'s dad?!?"
    show angela angry
    angela.say "Yes, [hero.name] - that's who it is!"
    angela.say "I told him all about it."
    angela.say "The memory loss, the hospital, how scared it was making me."
    angela.say "And he just dismissed it, [hero.name] - he said I was imagining things!"
    show angela frustrated
    "I'm struggling with what Angela's telling me."
    "I know that all of this looks insane, like she's gone crazy."
    "But why wouldn't her husband be as concerned as I am for her?"
    "Still, I do the best I can to play devil's advocate."
    bree.say "Sounds like he's an uncaring prick, Angela."
    bree.say "But that's not proof he's the one behind it, surely?"
    show angela protest
    angela.say "It got worse AFTER I told him, [hero.name]!"
    angela.say "Don't you see?"
    show angela normal
    angela.say "He kept making me cups of tea and other things."
    angela.say "At first I thought he was trying to make it up to me."
    angela.say "But then I kept forgetting where they'd come from!"
    angela.say "He's drugging me, or something like that."
    show angela pleased
    angela.say "I ran away as soon as I could, and I haven't had an episode since."
    angela.say "In fact, I'm starting to feel a lot better!"
    show angela flirt
    angela.say "Especially since you got here..."
    "As she says this, I feel Angela put her hand atop mine!"
    "I look down at it and then back up at her."
    "She's staring at me intently, a hunger in her eyes!"
    if hero.morality >= 25:
        "Oh god..."
        "I don't think I've ever been this scared to be alone with another woman!"
        "But I can't deny the way that I'm feeling, being here with Angela..."
        "I know that it's what I want!"
        bree.say "I...I'm a little afraid right now, Angela!"
        bree.say "But I think you are too, right?"
        "Angela nods hastily."
        show angela sad
        angela.say "I'm terrified, [hero.name]!"
        show angela flirt
        angela.say "And you're the only person that makes me feel safe!"
        "She's looking right into my soul with those huge eyes of hers."
        "And in that moment, I know that there's no way to resist!"
    elif hero.morality <= -25:
        "Oh god...it's finally happening!"
        "Angela's coming onto me!"
        "Yeah, yeah - I know she's opening up to me too."
        "I came here because I wanted to help Angela."
        "But I also came because I want to be with her."
        "And I mean alone with her!"
        bree.say "I had to come, Angela."
        bree.say "Because I have to be with you!"
        "Angela nods hastily."
        show angela sad
        angela.say "I'm terrified, [hero.name]!"
        show angela flirt
        angela.say "And you're the only person that makes me feel safe!"
        angela.say "I'll do whatever you want, so long as you stay with me..."
        "She's looking right into my soul with those huge eyes of hers."
        "And in that moment, I know that there's no way to resist!"
    else:
        "And I know that it's hunger, because I'm feeling it too!"
        "There's a desire coming from deep down inside of me."
        "Sure, I came here because I wanted to help Angela."
        "But I also came because I want to be with her."
        "And I mean alone with her!"
        bree.say "I'll do whatever I can, Angela."
        bree.say "I'll hold you and never let anyone hurt you!"
        "Angela nods hastily."
        show angela sad
        angela.say "I'm terrified, [hero.name]!"
        show angela flirt
        angela.say "And you're the only person that makes me feel safe!"
        "She's looking right into my soul with those huge eyes of hers."
        "And in that moment, I know that there's no way to resist!"
    "Before I know what's happening, Angela and I are leaning ever closer."
    hide angela
    show angela kiss
    with fade
    $ angela.flags.kiss += 1
    "And it feels like a painful eternity until our lips actually touch."
    "But when they finally do, I feel a new sensation welling up inside of me."
    "It's similar to the first time that we kissed, but subtly different too."
    "The sense of strangeness and the pang of fear are gone."
    "And in their place is a growing sense of familiar passion."
    "Even a sense of hunger!"
    "Angela and I are kissing passionately now, kissing like lovers."
    "This time she doesn't feel the need to grab me in a hug."
    "Instead I feel her hands touching me gently, exploring my body."
    "A moment later I'm doing the same thing, enjoying the sensation of holding her."
    "In this way we draw closer and closer, twining our limbs together."
    "I've lost all sense of this woman as the mother of someone I know."
    "She's suddenly so much more to me than that."
    "And all I know is that I want her more than anything I can imagine."
    "Our hands are pulling at each others clothes now."
    show angela kiss underwear with dissolve
    $ angela.flags.kiss += 1
    "But undressing is a clumsy affair, as neither of us will take a step backwards."
    "Instead we keep on kissing and caressing as we struggle to get the job done."
    "Angela battles with my clothes and I fight against hers."
    "And little by little, garments are tossed aside and onto the floor."
    "Somehow Angela manages to get me down to my panties and bra first."
    "Then she goes further, leaving me naked before her for the first time."
    "She still has on her underwear, and I instinctively pull back."
    hide angela kiss
    show angela underwear at center, zoomAt(1.5, (640, 1040))
    with fade
    "I can't help covering up my chest and beginning to blush."
    "Even trapped in her bra, Angela's breasts are so big."
    "They're balanced out by her broad thighs too."
    "Her figure is so feminine, like a mother goddess!"
    "She's starting to make me feel a little inadequate..."
    "As if she senses the problem, Angela leans back on the bed, giving me some space."
    "But at the same time she reaches back to unhook her bra."
    "The other arm she uses to hold her breasts up as she does so."
    show angela naked with dissolve
    "Then she releases them, letting the heavy orbs fall naturally free."
    "And she uses both hands to slowly slide down her panties."
    scene bg black
    show bree cunnilingus angela nomc hotel
    with fade
    "Now that she's naked too, Angela doesn't make any effort to move."
    "She simply lies back on the bed, propped up on her elbows."
    "But she holds my eye the whole time, smiling warmly."
    "It's as if she knows how I'm feeling, as if she understands."
    "And she's just waiting for me to pluck up the courage to make the next move."
    "Slowly and still holding Angela's eye, I crawl onto the bed."
    "As I get closer, I feel my eyes being drawn downwards."
    "I just can't keep myself from staring at Angela's breasts!"
    show bree cunnilingus angela -nomc kiss normalside with fade
    angela.say "Oh, [hero.name]..."
    angela.say "You're as bad as a guy!"
    "Angela shakes her head and reaches out to take hold of my hands."
    "Then she gently guides them forwards until they come to rest on the source of my fascination."
    "I can't keep from gasping as I feel them in my hands for the first time."
    angela.say "What are you waiting for, [hero.name]?"
    angela.say "Come on - I want you to play with me!"
    "I nod, telling myself that there's nothing stopping me from doing as she says."
    show bree cunnilingus angela kiss pleasurebree
    "But before I can take another step, I feel something that makes me yelp with surprise."
    bree.say "Oh..."
    bree.say "Oh shit..."
    "Angela smiles as the realisation of what she's doing dawns on me."
    show bree cunnilingus angela side normalangela
    "She must have used my distraction to make her move, to slide her hand under me."
    "And now she's stroking the lips of my pussy!"
    angela.say "Oh my, [hero.name]!"
    angela.say "You're practically wet through!"
    angela.say "Was it me did that to you?"
    show bree cunnilingus angela tongue pleasureangela normalkiss with fade
    "All I can do is nod desperately as Angela keeps on playing with me."
    show bree cunnilingus angela pleasurekiss
    "My mouth is hanging open, and I'm gasping at the sensations coming from down there."
    show bree cunnilingus angela suck blush front normalside normalbree -tongue with fade
    "Angela draws me down until I'm laid on top of her, but she doesn't stop."
    show bree cunnilingus angela normalsuck
    "My head comes to rest on her breasts, using them like pillows."
    show bree cunnilingus angela pleasuresuck
    angela.say "Mmm..."
    show bree cunnilingus angela pleasureside
    angela.say "Which one of us gets to taste the other, [hero.name]?"
    angela.say "Your call - your pussy or mine?"
    menu:
        "Yours":
            bree.say "Me..."
            bree.say "Please...Angela..."
            bree.say "Let me...do you!"
            "Angela chuckles and nods."
            show bree cunnilingus angela suck blush front
            pause 1.0
            show bree cunnilingus angela suck blush normalsuck
            "Then she lies back, arms at her sides."
            show bree cunnilingus angela suck blush pleasuresuck
            "Which means that she's totally at my mercy!"
            "As desperate as I am to do this thing, I still have to pause for a moment."
            "And that's because part of me just can't believe this is actually happening!"
            "This gorgeous older woman, my housemates mother - she's here with me!"
            angela.say "What's the matter, [hero.name]?"
            angela.say "Is something wrong?"
            bree.say "Oh no, Angela - no way!"
            show bree cunnilingus angela normaldown lick with fade
            "Feeling the need to back up my words, I lower myself down between Angela's thighs."
            "I keep looking her in the eye as I do so, right until the very last moment."
            "Then I close them and part my lips."
            "It's not like I need to look hard to find what I'm looking for."
            "I can feel the heat already radiating from Angela's pussy."
            "And the scent of her is almost too much for me to take!"
            "I feel like I've never wanted to taste anything as badly."
            "But still I can't force myself to go any faster."
            "Now the tip of my tongue is leading the way, searching for Angela."
            "And when it finds what I'm looking for, the effect is electric!"
            angela.say "Mmm..."
            show bree cunnilingus angela pleasuredown lick
            angela.say "Oh god..."
            angela.say "[hero.name]..."
            show bree cunnilingus angela normaldown
            "I don't know if it's the sensation of Angela on my tongue that does it."
            "Or if the sound of her reaction is what's really spurring me on."
            "But from that moment on, I can't think of anything else."
            "My tongue begins to dart deeper into the folds of Angela's pussy."
            "It snakes and slithers like it has a mind of its own."
            "Every twist seems to see it slide further inside of her."
            "How can I even begin to describe the taste?"
            "It's not like anything you could find to eat or drink."
            "In fact it's almost overwhelming, almost too much to take in."
            "But I know that I can't stop myself, that I'm starting to crave it."
            "I want to go deeper still, to push my tongue all the way into Angela."
            "This must be the taste that defines her, the essence of her womanhood."
            "I know that I've done stuff like this before, had it done to me too."
            "Yet somehow with Angela it all feels suddenly new."
            "I feel like I'm discovering the joy of it all over again."
            "I lick every fold like it needs individual attention."
            "And every fraction of an inch I make it inside becomes an obsession."
            "Meanwhile I can sense the effect my efforts are having on Angela."
            "Her broad, soft thighs are squeezing me on both sides."
            show bree cunnilingus angela at startle(0.05,-10)
            "And she's trying to lift her pelvis as high as she can."
            show bree cunnilingus angela pleasuredown
            angela.say "[hero.name]..."
            angela.say "What are you..."
            angela.say "What are you doing to me?"
            angela.say "Please...don't stop now!"
            "Angela's words are music to my ears."
            "Just knowing that I'm giving her pleasure spurs me on."
            "My tongue is starting to feel numb."
            "And my jaw is beginning to ache as well."
            "But that doesn't stop me putting in one final effort."
            "I push my tongue deeper still, pressing my face between Angela's thighs."
            "I can hardly breathe as I do this, the musky scent of her pussy filling my senses."
            show bree cunnilingus angela tongue at startle(0.05,-10)
            "But the reward for my efforts isn't long in coming, and I feel Angela begin to quake."
            show bree cunnilingus angela pleasureangela at startle(0.05,-10)
            "She gasps and moans as I force her to a climax, muscles twitching more and more."
            with vpunch
            "I'm still buried in her pussy as she cums, riding it out to the very end."
        "Show me!":
            show bree cunnilingus angela kiss front normalside normalbree with fade
            "I scuttle backwards onto the bed, laying back as I do so."
            "Propped up on my elbows, I make sure that my thighs are parted."
            "I feel more than a little ashamed for showing myself off in such an obvious way."
            "But Angela just has that kind of an effect on me!"
            bree.say "Please, Angela..."
            bree.say "I...I want this so badly!"
            show bree cunnilingus angela pleasurebree
            bree.say "Please do me!"
            "Angela lets out a laugh that takes me completely by surprise."
            "It's deep, confident and almost predatory in nature."
            "And it sends a shiver through my entire body."
            "Not the least of which I feel between my legs!"
            "Oh fuck...she's already making me wet down there!"
            show bree cunnilingus angela pleasureside
            angela.say "Oh, little [hero.name]!"
            angela.say "You're so sweet."
            angela.say "But you're not so innocent, are you?"
            "I shake my head, desperate to agree as Angela crawls onto the bed."
            scene bg black
            show angela cunnilingus bree onangela hotel with fade
            "She's on all fours now, almost stalking across the short distance between us."
            "Angela still has that smile on her face as she comes towards me."
            "And now it's putting me in mind a female big-cat stalking it's prey!"
            show angela cunnilingus bree chest suck with fade
            "I nod, trying as best I can not to tremble with anticipation."
            "Angela begins to crawl over me, her hands touching my legs."
            "Part of me wants her to keep on going, to lie wholly atop me."
            show angela cunnilingus bree down normal neck lick with fade
            "But as she sinks down between my thighs, I remember what she has in mind."
            "My eyes are locked on Angela's as her head goes down."
            "And even when she sinks too low for me to see, I still stare intently."
            "That is until the moment I feel Angela begin to work her magic on me."
            "It's a sensation that comes like a bolt out of the blue."
            "Like I've been struck by lightning and shocked to the core."
            show angela cunnilingus bree up pleasure
            "My eyes close and my head drops backwards."
            "Luckily the bed is there to catch me, cushioning my fall."
            "I wanted to watch Angela as she went down on me."
            "I wanted to see her tongue at work between my legs."
            "But all I can do is lie there, prostrate and helpless."
            "Trust me, I'm not stranger to this kind of thing."
            "I've taken it and given just as good back in return."
            "But this is something else entirely."
            "I don't know if Angela is drawing on experience right now."
            "Or maybe she's just that good at using her tongue."
            "Hell, maybe it's the thrill of being with her that's doing this to me."
            "Whatever the reason, every move she makes sends a jolt through my body."
            "I honestly thought I'd be able to sense exactly what Angela was doing to me."
            "But instead I find that I'm overwhelmed and unable to guess what's going on."
            "To me it feels like her tongue is able to change shape at will."
            "It seems to grow, shrink, contract and expand inside of me."
            "And all the time it sends twirling, coruscating sensations through me."
            show angela cunnilingus bree down pleasure outside
            bree.say "Oh..."
            bree.say "Oh, Angela..."
            bree.say "You're making me..."
            bree.say "I'm gonna..."
            show angela cunnilingus bree normal inside
            "There's no way I can finish saying what I wanted to say."
            "Because all at once I lose the power of speech."
            "I lose the ability to think coherent thoughts too."
            show angela cunnilingus bree chest
            "The pleasure I'm feeling is just too much."
            "It overloads everything else, pushing it aside."
            "That's because I'm about to cum."
            "And I know that it's going to be intense."
            "But there's no way that I could have prepared myself for this."
            show angela cunnilingus bree pleasure at startle(0.05,-10)
            "I feel like I'm teetering on the edge of a precipice, about to go over the edge."
            show angela cunnilingus bree at startle(0.05,-10)
            "Then it happens, the sensation builds to the point where I can't hold on for a moment longer."
            show angela cunnilingus bree up ahegao with hpunch
            "I'm swept away, feeling pleasure overtake my senses."
            "Angela doesn't stop for a moment, just keeps on going the whole time."
            "She only relents when my body finally goes slack and limp."
    scene bg black
    show bree cunnilingus angela kiss side pleasureangela pleasurebree hotel with fade
    "Neither of us speaks after that, not a single word."
    "Exhaustion takes hold and we simply slump on the bed."
    "I know that Angela is lying beside me, limbs tangled in mine."
    "But I have no idea what happens next or where we go from here."
    "Once we stir and come back to our senses, we have to face Angela's issues."
    "But for now, all we can do is lie here and sink into a deep, blissful sleep."
    scene bg black with dissolve
    $ angela.flags.angeladelay = TemporaryFlag(True, 1)
    return

label angela_female_event_10:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Angela")
    if not result:
        $ do_event.flags.canceled = True
        $ angela.love -= 5
        return
    if angela.love.max <= 180:
        $ angela.love.max = 180
    "It's been a few days since Angela called me to the hotel room."
    "And the truth is that I've been worrying about her the whole time."
    "So when she calls me up, I answer the phone right away."
    bree.say "Hey, Angela..."
    bree.say "Are you okay?"
    angela.say "Y...yeah, [hero.name]..."
    angela.say "I just wondered if I could see you?"
    angela.say "It's kind of lonely here, all on my own!"
    bree.say "Sure, Angela, sure..."
    bree.say "I'll be over as soon as I can."
    "I might have made it sound like I was going to fit Angela in when I had a spare moment."
    scene bg street with fade
    "But the truth is that I head straight over to the hotel as soon as the call is over."
    show bg door black secure at center, zoomAt(1.5, (640, 1040))
    pause 0.3
    play sound door_knock
    "And all it takes is one knock at the door for Angela to open it."
    scene bg black with dissolve
    pause 0.5
    scene bg hotelroom at center, zoomAt(1.5, (640, 1040)), dark
    show dick reactions angela smile nodick nobreemc
    with hpunch
    "She peeks through the gap in the door, and I can see that she's dressed only in a sheet from the bed."
    scene bg hotelroom
    show angela naked at center, zoomAt (2.5, (640, 1740))
    with fade
    show angela at center, traveling (2.4, 1.0, (340, 1640))
    "The door opens just enough for me to let myself in, while Angela scurries back to the bed."
    "All of this feels weird, almost surreal to me."
    "But the only other thing that comes close to being as crazy is the stuff that's been happening to Angela at home."
    "And I know that if I want to have a chance of keeping this fragile thing we have alive, I need to get find a solution."
    "So before I say a word, I begin to search the room, starting to look for Angela's clothes."
    "The motion seems to stir Angela into herself up, where before she was almost half-asleep."
    "She props herself up on one elbow, reaching out for me with her other hand."
    show angela b annoyed
    angela.say "[hero.name]..."
    angela.say "What are you doing?!?"
    show angela afraid
    "There's such a desperation in Angela's voice that I can't help feeling guilty."
    "Like she's convinced that I'm about to do something that will put her in danger."
    "That makes me stop and turn to face her."
    bree.say "It's okay, Angela..."
    bree.say "I'm not going to do anything desperate, I promise."
    bree.say "I just want you to get your clothes on while I start to get my head together too."
    show angela fragile
    "Angela doesn't seem to like the sound of the last part."
    show angela normal
    "But I can see that she's making an effort to be strong."
    "She sits up in bed, pulling the sheets up to her chest."
    "It's a gesture that seems a little odd."
    "But then I remember just how much more than me she's been through recently."
    "So I let it go and instead try to focus on the bigger issues at hand."
    bree.say "We need to think up a plan, Angela."
    bree.say "Decide what we're going to do next."
    show angela worried
    angela.say "But what can we do, [hero.name]?"
    angela.say "All we know is that Dylan's been doing something to me."
    angela.say "And we think it involves drugs - but it could be anything!"
    show angela normal
    "I've been waiting for this to come up, for the right time to show my cards."
    "Because my urge to find a solution seems to have super-charged my brain."
    "I put it all together, weighing up everything that's happened, and I think I've found an answer."
    bree.say "What if it's not drugs, Angela?"
    bree.say "Remember that the tests didn't find anything in your system."
    bree.say "What if this guy's been hypnotising you this whole time?"
    "The question seems to hit Angela like a hard slap in the face."
    show angela surprised at startle
    "Her eyes bulge in their sockets and her mouth drops open."
    "Angela shakes her head, like the possibility never even occurred to her before now."
    angela.say "He..."
    angela.say "He hypnotised me?"
    angela.say "Why, it's obvious!"
    show angela frustrated
    angela.say "Why didn't I think of that before now?"
    show angela sad
    "I shrug and shake my head at the question."
    bree.say "I don't know much about hypnosis, Angela."
    bree.say "But most people I see get hypnotised don't seem to know they're hypnotised."
    bree.say "And if he's been doing this to you for as long as I think he has..."
    show angela fragile
    "Now Angela's nodding her head, rather than shaking it."
    show angela protest
    angela.say "Of course, [hero.name]..."
    angela.say "It's all starting to make sense now."
    angela.say "Dylan practiced his act on me so many times over the years."
    angela.say "He could have planted any number of suggestions in my mind."
    show angela disgusted
    angela.say "Primed me with cues that would let him control me whenever he liked!"
    show angela angry
    "I'm nodding too, taking in all that Angela's saying."
    "All of this would certainly explain the strange way she's been behaving."
    "The sudden changes in her behaviour and the denial of things I saw happen with my own eyes."
    show angela worried
    angela.say "Oh god..."
    angela.say "How far back does this thing go?"
    angela.say "Did he change what I wanted in college?"
    angela.say "And our marriage - is that even real?"
    show angela disgusted
    "I watch as Angela seems to be reevaluating her life in the light of this terrible revelation."
    show angela surprised
    "But then she looks me straight in the eye, suddenly seized by a notion that leaves her pale-faced."
    angela.say "What..."
    show angela shock
    angela.say "What about [mike.name]?"
    angela.say "And Minami?"
    angela.say "Am I even who my children think I am?!?"
    "I throw my arms around Angela as she collapses onto my shoulder."
    "And I stroke her hair as she begins to sob, her body shaking the whole time."
    bree.say "That's not what' important, Angela."
    bree.say "No matter what comes out in the end..."
    bree.say "They'll always remember that your love for them was real."
    bree.say "You have to hold onto that, okay?"
    "Angela barely manages to nod, and I feel the sensation on my shoulder."
    show angela annoyed
    angela.say "But what are we going to do, [hero.name]?"
    angela.say "How are we going to stop him?"
    "Okay, it's time for me to put on my big-girl pants!"
    menu:
        "We can go to the police":
            bree.say "We've been doing this on our own too long, Angela."
            bree.say "It's time we got the authorities involved."
            angela.say "You..."
            show angela surprised
            angela.say "You mean the police?"
            "I nod, doing the best I can to look firm in my decision."
            bree.say "Your husband's been getting away with this for too long."
            bree.say "Now we're going to bring the weight of the law down on his head!"
            "I watch as Angela listens to what I have to say."
            show angela normal
            "And then she begins to nod too."
            "Which I hope means that she's on board."
            angela.say "Okay, [hero.name]..."
            angela.say "Let's go talk to the police."
            "When she reaches out to take my hand, I hold hers tightly."
            "All the time hoping that I'm making the right decision."
            $ angela.flags.angela_choice = "police"
        "We can ask for help" if not all([mike.hidden, dwayne.hidden, danny.hidden, victor.hidden]):
            bree.say "We've been doing this on our own too long, Angela."
            bree.say "It's time we got help from someone else."
            angela.say "You..."
            show angela surprised
            angela.say "You mean the police?"
            "I shake my head, making it clear that I don't."
            bree.say "This whole thing is so crazy, Angela..."
            bree.say "If we tell the police about it, they're going to think we're crazy!"
            show angela protest
            angela.say "But we have to do something, [hero.name]!"
            angela.say "I can't let that man trap me again..."
            angela.say "Not now that I know who he really is!"
            show angela annoyed
            "I nod, trying to reassure Angela."
            bree.say "I know, I know..."
            bree.say "That's why we're going to get help from someone else."
            bree.say "Someone that's used to solving problems in unusual ways."
            show angela normal
            "Angela nods, which I hope means that she's on board."
            "And when she reaches out to take my hand, I hold hers tightly."
            "All the time hoping that I'm making the right decision."
            $ angela.flags.angela_choice = "outside_help"
            $ angela.flags.outside_help = None
        "We need to gather more evidence":
            bree.say "This whole thing is so crazy, Angela..."
            bree.say "Anyone we tell about it is going to think we're crazy too!"
            show angela protest
            angela.say "But we have to do something, [hero.name]!"
            angela.say "I can't let that man trap me again..."
            angela.say "Not now that I know who he really is!"
            show angela annoyed
            "I nod, trying to reassure Angela."
            bree.say "I know, I know..."
            bree.say "That's why we're going to handle this ourselves."
            bree.say "We're going to find the proof we need to bust his ass."
            bree.say "And then he'll never be able to bother you again."
            show angela normal
            "Angela nods, which I hope means that she's on board."
            "And when she reaches out to take my hand, I hold hers tightly."
            "All the time hoping that I'm making the right decision."
            $ angela.flags.angela_choice = "evidence"
    $ angela.flags.angeladelay = TemporaryFlag(True, 1)
    scene bg black with dissolve
    return


label angela_asking_for_help_fail:

    "It seems that I have to find another solution to stop Dylan."
    menu:
        "I'll convince Angela to go to the police":
            $ angela.flags.angela_choice = "police"
        "I'll gather more evidence":
            $ angela.flags.angela_choice = "evidence"
    return


label angela_female_event_11:
    scene bg street
    show angela fragile at center, zoomAt (1.5, (640, 1060))
    with fade
    "I have to admit that I don't like having to visit the police station at the best of times."
    "But right now it feels like Angela and I are hurrying there whilst looking over our shoulders."
    "I know it sounds crazy, but part of me is expecting her husband to leap out of an alleyway or something."
    "Then I imagine he'll click his fingers in front of Angela's face, instantly placing her under his control."
    "And what about me?"
    "Will he put me under his spell too?"
    "Make me forget that Angela ever existed, or who I am myself?!?"
    "No, no...I have to stop thinking like that!"
    "If I'm distracted I could miss something important."
    "Maybe let the guy sneak up on us while worrying about that very same thing happening."
    "Shaking the feeling off, I pretty much throw the doors to the police station open."
    "Then I push Angela inside, hurrying in on her heels."
    scene bg policestation with fade
    show angela worried at center, zoomAt (1.25, (940, 880)) with easeinright
    angela.say "Whoa..."
    angela.say "Careful, [hero.name]!"
    show angela fragile
    bree.say "Sure, Angela, sure..."
    bree.say "We're here now, so I can finally relax."
    show angela normal
    "Angela nods at this and gives me a smile."
    "But I can see the tension in her eyes and how she's clenching her jaw."
    "She's so wired that she could lose it any second now."
    show angela fragile
    "Which I guess makes two of us!"
    "I glance around, looking for someone in uniform."
    "And that's when my eyes settle on what looks like a reception desk."
    "The officer sitting behind it seems to sense my attention and looks up."
    show camila work at center, zoomAt (1.25, (340, 980)), dark, dark with dissolve
    "Officer" "Can I help you, madam?"
    "I walk the short distance to the desk, putting a smile on my face."
    "And I make sure to pull Angela along with me as I do so."
    show angela normal at center, zoomAt (1.25, (840, 880)) with ease
    bree.say "Ah..."
    bree.say "Yeah..."
    bree.say "My friend here is having serious problems with her husband."
    bree.say "And we'd like to talk to someone about getting him arrested?"
    show camila weird
    "Officer" "Right..."
    "Officer" "There's a few formalities to go through."
    "Officer" "You know, before we get to the stage of arresting someone?"
    show camila normal
    bree.say "Oh..."
    bree.say "Sure, sure..."
    bree.say "We're here to do whatever we need to do to get the ball rolling."
    "The officer nods slowly and starts to take down some details."
    "Angela answers some simple questions, and the officer gestures to a bench."
    show camila weird
    "Officer" "Take a seat."
    "Officer" "A detective will be along to see you soon."
    hide camila
    show angela fragile at center, zoomAt (1.5, (640, 1060))
    with fade
    "Angela and I do as we're told, sitting down and preparing to wait."
    "There's a couple of old magazines on a table and some posters on the walls."
    "But apart from that, we only have our phones to entertain ourselves."
    "And for some reason, neither of us seems to feel like talking much."
    "On my part that's because I'm dreading trying to explain all of this to an actual police officer."
    "I guess the same thing must be true for Angela as well."
    "After what feels like forever, there's the sound of an awkward cough."
    show angela normal at center, zoomAt (1.15, (940, 840)) with fade
    show inspector at center, zoomAt (1.25, (340, 880)) with easeinleft
    "And we both look up to see a short, kind of dishevelled-looking man before us."
    "He's dressed in a raincoat and everything about him seems oddly creased somehow."
    "Inspector" "Erm..."
    "Inspector" "Are you the ladies here about one of your partners?"
    show angela worried
    angela.say "Y...yes..."
    angela.say "That's us."
    show angela afraid
    "Inspector" "Alright then..."
    "Inspector" "Let's go somewhere a little more private."
    show angela normal
    "The detective leads us to a room with a table and chairs, motioning for us to sit down."
    "Then he closes the door behind us and sits down on the other side of the table."
    "Inspector" "Okay..."
    "Inspector" "Which one of you is making the complaint?"
    "Angela taps her chest."
    show angela protest
    angela.say "That would be me."
    show angela normal
    "The detective nods."
    "But then he looks me in the eye."
    "Inspector" "And that would make you...who, exactly?"
    "Inspector" "Sorry if that's an awkward question."
    "Inspector" "But I need to know how everyone fits into this little picture."
    bree.say "Sure, sure..."
    bree.say "My name's [hero.name]..."
    bree.say "And I'm Angela's...friend."
    "I'm expecting the detective to ask exactly what that means."
    "But instead he surprises me by nodding, as if satisfied."
    "Inspector" "Okay, Angela..."
    "Inspector" "You want to tell me what this is all about?"
    "Angela nods and takes a deep breath."
    show angela worried
    angela.say "I want to report that my husband has been hypnotising me."
    "Angela says the words in a frank and forthright manner."
    "But the detective instantly does a double-take."
    "Inspector" "Excuse me..."
    "Inspector" "But did you just say hypnotising you?!?"
    show angela protest
    angela.say "Yes I did."
    angela.say "My husband is a stage magician and a hypnotist."
    angela.say "Quite a famous one, actually."
    angela.say "And I believe that he's been using his powers on me without my permission."
    show angela fragile
    "I can see that the detective is listening very intently."
    "But I also notice that he's not writing anything down on his crumpled notepad."
    bree.say "Angela's been having blackouts, really bad ones."
    bree.say "She keeps waking up in places she can't remember going."
    bree.say "And she forgets other places she's been too."
    "Again the detective seems to listen to the story."
    "And only speaks up once I've finished adding to it."
    "Inspector" "That sounds serious - you should see a doctor!"
    bree.say "She did!"
    bree.say "And they said it was all mental, not physical."
    bree.say "But then her husband turned up and took her away."
    bree.say "And the next time I saw Angela, she'd forgotten all about it!"
    "The detective shakes his head at this."
    "Inspector" "These are some very serious accusations!"
    "I feel a surge of hope, as he's not dismissing our story."
    bree.say "So you believe us?"
    bree.say "You'll bust this guy's ass?!?"
    "The detective holds up a hand to stop me."
    "Inspector" "Wait a second, madam..."
    "Inspector" "It's got nothing at all to do with whether I believe you or not."
    "Inspector" "But it does have a whole lot to do with what we can prove."
    "Inspector" "And right now, I have nothing that'd let me get a warrant of any kind."
    show angela sad
    "Angela visibly sags in her seat, shoulders falling."
    show angela worried
    angela.say "So we're stuck?"
    angela.say "There's noting we can do?"
    show angela afraid
    bree.say "No, Angela..."
    bree.say "We just need to find the evidence he needs."
    "I turn to face the detective."
    bree.say "Right?"
    bree.say "If we bring you proof, you'll do something about it?"
    "The detective holds up his hands in a gesture of openness."
    "Inspector" "Look, ladies..."
    "Inspector" "Stage magicians hypnotising their wives sounds unbelievable on paper."
    "Inspector" "But I've seen some really weird stuff in my time on the force."
    show angela fragile
    "Inspector" "Bring me real evidence, and I'll bust this evil Houdini of yours like any other guy."
    "That seems to bring the interview to an end."
    hide angela with easeoutright
    "The detective shows us out and we leave the police station, walking back onto the street."
    scene bg street
    show angela fragile at center, zoomAt (1.5, (640, 1040))
    with fade
    "I'm feeling pretty positive right now, like I have a clear plan of action in my head."
    "But Angela looks downcast as we start to walk back to her hotel."
    show angela worried
    angela.say "I don't know why you look so happy, [hero.name]..."
    angela.say "We still don't have any way of getting the proof he wants!"
    show angela fragile
    bree.say "Don't worry about it, Angela."
    bree.say "I know just how we're going to get it."
    bree.say "You leave it to me, okay?"
    show angela normal
    "Angela nods, seemingly happy not to hear the actual details."
    "Which suits me fine, as I'm sure she wouldn't like the plan I've cooked up."
    "Specifically to break into her home and find the evidence myself."
    $ angela.flags.angeladelay = TemporaryFlag(True, 1)
    $ game.room = "street"
    scene bg black with dissolve
    return

label angela_female_event_12a:
    "It's becoming pretty obvious that nobody else is going to step up and help Angela out."
    "So if I want to see her free of her problems, then I'm going to have to do it myself."
    "All of which is easy to proclaim beforehand, when it's all just talk."
    "But now that it's time to take some action, it feels very different indeed."
    "Because how exactly am I going to find evidence of what Angela's husband has been doing to her?"
    "Only by being able to rummage through his most private stashes of stuff, right?"
    "And he's not just going to let me in the house if I walk up and knock on the door."
    "So what choice do I have but to try breaking into the place?"
    play music "music/darren_curtis/come_out_and_play.ogg" loop fadeout 0.5
    show bg park night at center, zoomAt (1.25, (640, 900)), dark, flip with vpunch
    play sound hitting_bushes
    "So that's how I come to be all dressed in black and squatting down in the bushes."
    "I can see the house from where I'm hiding, and I have to admit it looks pretty nice."
    "I'd much rather have been visiting this place for the first time as [mike.name]'s friend."
    "Or even better as Angela's significant other."
    "But I guess those are the breaks in life."
    "All I get is to be trying to break in while dressed up like a bargain basement ninja!"
    "It's already dark, and I can see that there's only one light on in the house."
    "I think that's the bedroom, so maybe that Dylan creep is watching TV or something."
    "Would it be too much to ask for him to have fallen asleep in his bed?"
    "The thought is very appealing, making me dread the alternative."
    "But then I shake it off, worried that it's distracting me."
    "At this rate I'm never going to make it any closer to the house than this."
    "So I summon all of the willpower I can muster, and make my first move."
    play sound hitting_bushes
    with vpunch
    "Crouching down, I run awkwardly across the lawn and up to the side of the house."
    "All the time I'm praying that this guy doesn't have security cameras all over the place."
    play sound woosh_punch
    with vpunch
    "And once I make it, I collapse against the wall of the house."
    "I can feel my heart starting to race already, and I'm not even inside yet."
    "Glancing around for a possible way in, I stop and stare in sheer amazement."
    "Am I really seeing what I think I'm seeing?"
    "Because if so, there's a window just above me."
    "One that's been left slightly open!"
    "With aching slowness, I stand up and reach for the window."
    "It slides open even further as I tug at it, presenting me with the perfect way inside."
    "Okay, this is it - this is the point of no return."
    "Taking a deep breath, I remind myself of why I came here in the first place."
    "And then I reach up and begin to haul myself in through the open window."
    "Climbing in feels like it takes forever, every second seeming like a lifetime."
    "But eventually I manage to pull my legs up after me."
    "I hold onto the window itself, using it as an anchor."
    "Then it's just a matter of lowering them down and into the house."
    scene bg angelalivingroom lightsoff at dark with fade
    "It's pretty dark inside, making it hard for me to tell where I am."
    scene bg angelalivingroom lightsoff with dissolve
    "But I soon begin to make sense of my surroundings as my eyes adjust."
    "And it seems that I've ended up in the livingroom."
    "Looking this way and that, I start to move deeper into the room."
    "That's when I feel my sleeve snag against something behind me."
    "I realise too late that it's caught on the edge of the window."
    "And even in turning to see as much, I've made the situation that much worse."


    with vpunch
    "Because the motion pulls on the window, slamming it against the frame."
    "The noise wouldn't normally have been anything out of the ordinary."
    "But in a dark house during the night, it sounds loud enough to wake the dead."
    "And certainly loud enough for anyone else in the place to hear."
    play sound bed_jump
    "Sure enough, there's the sound of someone stirring in another room."
    "Dylan" "What the hell..."
    "Dylan" "Is there..."
    "Dylan" "Is there someone there?!?"
    "In that moment my brain seem to be screaming at me to move."
    "To clamber back out of the window or look for somewhere to hide."
    "But for some reason I find myself frozen, rooted to the spot."
    "And that's just how he finds me."
    scene bg angelalivingroom
    show dylan at center, zoomAt (1.25, (940, 900)), blacker with easeinright
    "He bursts out of what must be the hallway door, flipping on the lights."
    hide dylan
    show dylan stuned at center, zoomAt (1.25, (940, 900))
    with dissolve
    "Then I'm face-to-face with Angela's husband for the first time."
    "I recognise him instantly from the posters I've seen."
    "Sure, he's a little older."
    "And he's dressed in casual clothes, rather than a top hat and tails."
    "Plus the look on his face wasn't one of shock and surprise either."
    "But I guess the look on my face must be pretty similar right now!"
    show dylan surprised at center, traveling (1.5, 0.3, (640, 1080))
    "Dylan" "Who in the hell are you?"
    "Dylan" "And what are you doing in my house?!?"
    show dylan stuned
    "Well, it looks like I've managed to fuck this up good and proper."
    "The only question is, what am I going to do about it?"
    scene bg black with dissolve
    pause 0.5
    if hero.morality <= -25 or hero.has_skill("martial_arts") or "master_training_female_event_05" in DONE:
        menu:
            "Lie" if hero.morality <= -25:
                call angela_female_event_13a from _call_angela_female_event_13a
            "Flee":
                call angela_female_event_13b from _call_angela_female_event_13b
            "Fight" if hero.has_skill("martial_arts") or "master_training_female_event_05" in DONE:
                call angela_female_event_13c from _call_angela_female_event_13c
    else:
        call angela_female_event_13b from _call_angela_female_event_13b_1
    return

label angela_female_event_13a:
    scene bg angelalivingroom
    show dylan at center, zoomAt (1.5, (640, 1080))
    with fade
    "I find myself glancing around as Dylan stands in front of me."
    "And for a moment I think that there's no possible way out of this."
    show dylan shout
    "Dylan" "I asked you a question!"
    "Dylan" "What are you doing in my house?!?"
    show dylan normal
    "Suddenly something seems to dawn on Dylan."
    "And he points an accusing finger in my direction."
    show dylan shout
    "Dylan" "You're a burglar, aren't you?"
    "Dylan" "You broke in here to steal my memorabilia, didn't you?"
    show dylan normal
    "As soon as he says this, I feel something dawn on me too."
    "The walls are covered in old posters of his act with Angela."
    "And he's clearly still obsessed with that part of his life."
    "So maybe I can use that to my advantage."
    bree.say "No!"
    bree.say "I'm not a burglar..."
    bree.say "I'm...I'm a fan!"
    "Dylan seems not to understand me at first, squinting in confusion."
    "But then the words seem to begin making some kind of sense to him."
    show dylan surprised at center, zoomAt (1.0, (640, 1080)), stepback
    "Dylan" "You're..."
    "Dylan" "You're a fan?"
    "Dylan" "Are you serious?!?"
    show dylan stuned
    "I'm nodding the whole time Dylan's asking his questions."
    "Trying to do all that I can to convince him it's the truth."
    bree.say "Actually..."
    bree.say "I'm your biggest fan."
    bree.say "And...I know breaking in here was a stupid thing to do."
    bree.say "But I thought that if I got to speak to you alone..."
    show dylan normal
    "I put on the best act that I can as I pretend to explain myself."
    "Staring at the ground and refusing to meet Dylan's eye."
    "And it seems to work, because when I look up, his demeanour's changed."
    "Where before he was hostile and suspicious, he now looks positively intrigued."
    "Which leads me to believe that I've managed to hook him with the ruse."
    show dylan shout at center, zoomAt (1.0, (640, 1080)), stepback
    "Dylan" "Well..."
    "Dylan" "Maybe you should have tried knocking at the door first!"
    show dylan happy
    "Dylan" "But...we're here now, and we're talking, aren't we?"
    show dylan smile
    "Dylan's face cracks into a smile as he says this."
    "And I have to admit that I can guess what Angela probably used to see in the guy."
    "He's kind of charming in a stiff, maybe even arrogant kind of way."
    "But I have to keep pushing that out of my mind."
    "Because I'm supposed to be playing the part of a fanatical fan."
    "And I'm only doing that to get a chance to search for the evidence that I need."
    "I can't let any kind of genuine rapport build up between us."
    "So all the time I keep on reminding myself of what this guy did to Angela."
    bree.say "I..."
    bree.say "I guess we are!"
    bree.say "Oh wow...this is so weird."
    bree.say "I'm actually talking to THE Dylan Devant!"
    show dylan evil at center, zoomAt (1.0, (640, 1080)), stepback
    "He waves a hand at this and shakes his head."
    show dylan talkative
    "Dylan" "Oh please, no one calls me that at home."
    show dylan happy at center, zoomAt (1.5, (740, 1080)) with ease
    "Dylan" "Dylan will do just fine."
    "Dylan" "But what am I supposed to call you?"
    show dylan smile
    "I think for a moment, worried that telling him my real name would give the game away."
    "So I settle on the first name that comes into my head, regardless of the consequences."
    bree.say "Sasha..."
    bree.say "My name's Sasha."
    show dylan talkative at center, zoomAt (1.0, (740, 1080)), stepback
    "Dylan" "Okay, Sasha..."
    show dylan happy at center, zoomAt (1.5, (540, 1080)) with ease
    "Dylan" "I think we already established you're not here to rob me."
    "Dylan" "So what else is there that Dylan Devant can do for his biggest fan?"
    show dylan smile
    "Okay, this is it."
    "I think I figured out a way to handle this guy and get what I want."
    "Let's just hope that I have the skills to pull it off!"
    "Doing the best I can to look nervous and yet desirable, I walk towards him."
    show dylan at center, zoomAt (1.5, (640, 1080)) with ease
    "And only now do I make the effort to look up and meet his gaze."
    bree.say "Well..."
    bree.say "Dylan..."
    bree.say "There was one thing..."
    "Dylan doesn't move an inch as I make it to where he's standing."
    "Instead he remains perfectly still, letting me lean myself against him."
    bree.say "You see I used to watch you on stage all the time."
    bree.say "Especially when you were doing stuff with that glamorous assistant of yours."
    bree.say "I was always so jealous when you sawed her in half or made her disappear."
    bree.say "And I wondered if you'd want to use your magic wand on me?"
    "I think it's working."
    "I think I've managed to disarm his suspicions."
    "That and totally get the organ in his pants to do all the thinking instead of his brain."
    "I feel Dylan take hold of my hand."
    "And then he presses it against the front of his pants."
    show dylan happy at center, zoomAt (1.0, (640, 1080)), stepback
    "Dylan" "I think my magic wand just answered your question, Sasha..."
    "Dylan" "It's all ready to work a spell on you!"
    show dylan evil
    "I hate myself for doing it, but I have to keep up the act."
    "So I let out the best giggle that I can manage."
    "And it seems to work, making him think that I'm being pulled in."
    bree.say "Oh, Dylan..."
    bree.say "I always wondered about it..."
    bree.say "But I never let myself hope it'd be this big!"
    show dylan happy at center, zoomAt (1.0, (640, 1080)), stepback
    "Dylan" "Wait until you see it in the flesh, Sasha!"
    show dylan evil
    "Dylan takes hold of my hand as he says this."
    "And then I let him lead me slowly up the stairs."
    "From there he opens the door of a bedroom and pulls me in after him."
    "Inside I see that there's a double bed, and I do the best I can not to register too much else."
    "Because I just know this has to be the very room where Angela and he are supposed to share."
    "Doing the best I can to keep those thoughts out of my head, I remain passive, letting him take the lead."
    "Dylan seems to know exactly what he wants too, wasting no time in stripping off my clothes."
    "He pushes me down onto the bed before beginning to remove his own, and I wait for him there."
    "I'm still doing the best I can to keep the act up, cooing and gasping when it feels appropriate."
    "But my guess is that he's by now too far into this thing to really notice my efforts."
    "By the time Dylan is naked and climbs onto the bed, all he's interested in is my body."
    "I feel like I could simply lie back and let him get the business done without moving once."
    "Though for the sake of appearances, I make the occasional show of it."
    "Looking up at him with that same amazement in my eyes and gasping at the size of his cock seems to do the trick."
    show dylan happy at center, zoomAt (1.0, (640, 1080)), stepback
    "Dylan" "You know, Sasha..."
    "Dylan" "I had a reputation when I was younger."
    "Dylan" "They said I was a magician on the stage, and between the sheets too!"
    show dylan smile
    bree.say "Oh, Dylan..."
    bree.say "You're so funny..."
    bree.say "And such a stud too!"
    "I can hardly believe the words that are coming out of my mouth right now."
    "But a moment later I have something that's more than enough to distract me."
    "Because I feel the sensation of his cock rubbing against the lips of my pussy."
    "Desperate to find some way to make this bearable, I try to picture someone in his place."
    scene bg angelalivingroom at dark
    show mike casual happy
    with fade
    "[mike.name]?"
    "No, too close to home!"
    hide mike
    show sasha casual happy
    with fade
    "Sasha?"
    "No, that could get confusing!"
    hide sasha
    show angela casual flirt
    with fade
    "Angela?"
    "As soon as the thought pops into my head, there's no turning back."
    "I tune myself out of what's going on in the room and imagine Angela atop me instead."
    "And I do the best I can to pretend that his cock is a strap-on she's wearing too."
    "This means that when I feel the inevitable happen, I'm already miles away."
    scene angela missionary bree with fade
    "As Dylan enters me, it's Angela that I'm picturing."
    "In fact the image that I conjure of her is so strong that I forget where I am altogether."
    "Instead I'm imagining being made love to by the woman that I'm doing all of this for."
    "I can't hear the pathetic sound of Dylan as he grunts and heaves."
    "All that I hear is the pleasant sound of Angela, giggling as she pleasures me."
    "I can only guess that my reactions are pretty impressive."
    "Because Dylan seems to be taking all of this as me enjoying his efforts."
    "Encouraged by my desire for his own estranged wife, he puts everything he has into it."
    "But for me, this only results in the images of Angela becoming that much more vivid and intense."
    show angela missionary bree pain
    "I'm longing for her touch, even as he's thrusting in and out of me."
    "And the truth is that it feels like my mind is becoming seperated from my body."
    "While Dylan desperately exhausts himself on top of me, I'm drifting away."
    show angela missionary bree pleasure
    "Reaching a higher plain where Angela waits for me!"
    "But all of a sudden I feel a sharp force, pulling me back to the material world."
    "As my senses begin to clear and sharpen, I realise what must have happened."
    scene bg angelalivingroom with dissolve
    "Because Dylan's already rolling off of me and collapsing into a heap at my side."
    "Wow...that didn't take very long at all!"
    "I hope he was able to go longer when it came to his stage shows."
    "He follows up that unimpressive performance by starting to snore soon afterwards."
    "Unable to believe my luck, I give him an experimental poke in the ribs."
    "And when he just grumbles and rolls over, I know my chance has finally come."
    "As quickly as I dare, I jump off the bed and grab my clothes."
    "I'm still pulling them on as I begin to search the house."
    "But it doesn't take me long to find what looks like Dylan's study."
    "And right there, in the middle of the desk, is what looks like a paper journal."
    "Even as I open it, I'm thinking that he can't be that brazen, can he?"
    "To write down, on paper, all of the stuff he's been doing to Angela?"
    "Yet there it is, written in plain English - a diary of every time he's hypnotised her."
    "Not only that, there's a record of his reasons for doing it and his thoughts too!"
    "For a moment I wonder how he kept this from Angela."
    "But then I realise that all he had to do was hypnotise her not to notice the journal."
    "I stand up, shaking my head to stop myself from contemplating it any longer."
    "None of that matters right now, because I have what I came for."
    "Clutching the journal to my chest, I hurry downstairs."
    "And once I reach the window I used to get in, I clamber out of it again."
    "Then I flee into the night, as fast as I dare."
    "All the time trying to control my emotions."
    "Because I could hold in my hands the answer to all of Angela's problems."
    "As well as the key to securing our future together."
    $ angela.flags.angeladelay = TemporaryFlag(True, 1)
    $ DONE["angela_female_event_13a"] = game.days_played
    return

label angela_female_event_14a:
    scene bg policestation with fade
    "Clutching the diary that I managed to swipe from Dylan's study to my chest, I hurry through the police station doors."
    "Angela is only a step behind me, still more than a little puzzled as to just what is going on right now."
    show angela worried at center, zoomAt (1.25, (940, 880)) with easeinright
    angela.say "[hero.name]..."
    angela.say "Slow down a little!"
    angela.say "What are we even doing here?!?"
    show angela fragile
    "In my desperation to get to see the detective that we spoke to the last time, I don't really listen to what Angela's saying."
    "Instead I wave a hand in the air, trying to put her off until I've dealt with matters that seem more important right now."
    bree.say "I already told you, Angela..."
    bree.say "We have the proof that we need."
    bree.say "Now the police can charge your husband."
    show angela worried
    angela.say "We do?"
    angela.say "Then where is it?"
    angela.say "All you have there is a notebook from Dylan's desk!"
    show camila work at center, zoomAt (1.25, (340, 980)), dark, dark with dissolve
    "I'm already at the desk and trying to talk to the officer on duty as Angela says this."
    "So my attention is divided unequally between her and he matter of getting to see the detective."
    "Officer" "How can I help you, madam?"
    bree.say "I showed you it already, Angela..."
    bree.say "It's right here!"
    "Before Angela can say another word, I turn back to the officer on the reception desk."
    bree.say "Sorry...yeah..."
    bree.say "We need to see the detective?"
    bree.say "I don't recall his name - but he looks kind of scruffy?"
    bree.say "Wears a raincoat and has a cigar in his hand?"
    "The officer nods at this."
    "Officer" "Oh, you mean the lieutenant?"
    "Officer" "You can go right in and see him."
    "Officer" "That door right over there."
    "I nod my thanks to the officer and begin to hustle Angela into the room."
    hide camila
    show angela fragile at center, zoomAt (1.5, (640, 1060))
    with fade
    "She's still looking more than a little confused as we bustle in through the door."
    "But as soon as we're in there, my attention switches to the lieutenant."
    "He's sitting behind the desk, looking as dishevelled as ever."
    show angela normal zorder 2 at center, zoomAt (1.15, (940, 840)) with fade
    show inspector zorder 3 at center, zoomAt (1.25, (340, 880)) with easeinleft
    "Inspector" "Oh..."
    "Inspector" "Hello again, ladies."
    "Inspector" "I presume you've got something more concrete for me than the last time?"
    "I nod as I step forwards and slam the journal down on the desk."
    bree.say "You bet we do."
    bree.say "It's all in there, everything you need."
    bree.say "The arrogant bastard kept a diary of everything he did to Angela here."
    "The lieutenant's eyebrows rise as he picks up the journal and begins to flip through it."
    "As he does so, I notice that he can't help looking up at Angela every so often."
    "Inspector" "I'm sorry, madam..."
    "Inspector" "But I'm gonna have to ask you to verify some of the information in here."
    "I notice that he points to certain lines on the pages as he does so."
    "But Angela's response is not the one that I was expecting."
    show angela surprised
    "Instead of looking worried at the prospect of reliving her trauma, she looks confused."
    "Almost as if she has no idea what the guy's talking about."
    show angela protest
    angela.say "I...I don't understand..."
    angela.say "Verify what, exactly?"
    show angela frustrated
    "I'm totally baffled by what's happening right now."
    "But I can see that the lieutenant is more intrigued."
    "It's like I can see the gears turning inside of his head."
    "Then he takes us both by surprise as he slams the journal shut."
    "Inspector" "Don't worry about that right now, madam."
    show angela normal
    "Inspector" "As luck would have it, your husband is here at the station right now."
    "Inspector" "Seems he was burgled last night, which is a pretty strange coincidence."
    "The lieutenant shoots me a knowing glance, then adds a wink."
    "Which I take to mean that he's pretty much figured out where I got the journal."
    "Inspector" "But obviously, this case would take precedence over that one."
    "He's still looking at me as he adds that."
    "And I choose to take it as an assurance that I'm safe."
    show angela worried
    angela.say "Dylan's here?!?"
    show angela sad
    "Inspector" "Don't worry, madam..."
    "Inspector" "His brand of magic doesn't work on cops."
    "Inspector" "But I am going to have him brought in here."
    "Inspector" "Because I have some questions I want him to answer."
    "Inspector" "And I'd like you to help me ask them, okay?"
    show angela fragile
    "Angela looks at me for assurance, and part of me wants to let her off the hook."
    "But I steel myself for what lies ahead, because I know we have to do this thing."
    bree.say "Don't worry, Angela..."
    bree.say "The Lieutenant and I will be right here with you."
    show angela normal
    bree.say "And we have the chance to put him away for good too."
    "Angela nods, but I can see the strain on her face as she does so."
    "The lieutenant nods in turn, then picks up the phone on his desk."
    "Inspector" "Yeah..."
    "Inspector" "Well forget about that for now."
    "Inspector" "Just bring Mister Devant up here to me."
    "Inspector" "No, he can find out what for once he's here."
    "I can feel the tension rising in the room as we wait."
    "And once I even have to remind myself not to hold my breath."
    "But eventually the door opens, and all heads turn in that direction."
    "It's actually hard to say who looks more surprised in that moment."
    "Angela and I staring at Dylan in the doorway, or him staring back at us."
    show angela frustrated
    show dylan zorder 1 at center, zoomAt (1.15, (640, 840)) with easeinright
    "Luckily the lieutenant doesn't seem in the slightest bit affected."
    "I guess he's more than used to this kind of thing in his line of work."
    "Inspector" "Hey there, Mister Devant..."
    "Inspector" "You mind if I call you Dylan?"
    show dylan surprised
    "Dylan" "What?!?"
    "Dylan" "Why am I even here?"
    "Dylan" "And what is my wife doing here too?"
    show dylan stuned
    "I have no idea if Dylan recognises me from the previous night or not."
    "He might even be deliberately ignoring me for the sake of playing the innocent."
    "Either way, this seems to be the Lieutenant's show."
    "So I don't speak up on that account."
    "Inspector" "Just a quick question, Dylan..."
    "Inspector" "Do you recognise this book?"
    "He holds up the journal for all to see."
    "And I'm expecting Dylan to deny all knowledge of it."
    "But then he surprises me by nodding his head."
    show dylan surprised
    "Dylan" "That's my notebook, from my study."
    "Dylan" "It must have been stolen in the burglary last night."
    show dylan stuned
    "Inspector" "The same one you claim to have slept through?"
    "Inspector" "Hmm..."
    "Inspector" "There's a lot of interesting stuff in here, you know?"
    "Inspector" "It reads like a magician's diary, one that's hypnotising his wife!"
    "I blink in sheer amazement at what the Lieutenant is saying."
    "It's like he's laying it all out for Dylan's sake."
    "Giving him the chance to get his story straight and deny it all!"
    show angela normal
    bree.say "Wait a minute..."
    show inspector at center, zoomAt (1.0, (340, 880)), startle
    "Inspector" "Ah, ah, ah..."
    "Inspector" "Please don't interrupt me, madam."
    "Inspector" "So, Dylan - is this your diary?"
    show dylan at center, zoomAt (1.0, (640, 840)), startle
    "Dylan shakes his head and lets out a derisive laugh."
    show dylan happy
    "Dylan" "Of course not!"
    "Dylan" "Those are just notes for a book I've been working on."
    "Dylan" "A thriller in which a magician hypnotises his wife."
    show dylan smile
    bree.say "Oh, come on!"
    bree.say "You expect us to believe that?!?"
    "The lieutenant holds up a hand to silence me."
    "And for the first time, Dylan looks in my direction."
    "In that moment I realise that he totally recognises me."
    "And that he's one hundred percent sure he's the one in control of this situation."
    show dylan shout
    "Dylan" "It's a subject I have plenty of experience in."
    "Dylan" "But it's not autobiographical, I assure you."
    show dylan normal
    "Inspector" "I gotta admit, that does sound like a pretty good read!"
    "Inspector" "I was just dipping into it before you walked in here."
    "Inspector" "But I'm having a little trouble with your handwriting, Dylan..."
    "As he says this, the lieutenant places the journal on the desk."
    "Then he turns it so that Angela can see the pages clearly."
    "Inspector" "Madam, you obviously know your husband's handwriting better than I do."
    show angela annoyed
    "Inspector" "Would you mind reading me that line?"
    "Inspector" "The one right there?"
    show dylan stuned
    "Even before Angela looks down at the page, Dylan's expression changes."
    "He makes a move to grab the journal, but then seems to think better of it."
    show angela surprised
    angela.say "What are you talking about?"
    show angela worried
    angela.say "There's nothing written on that page, or any of the others."
    angela.say "It's totally blank, and I don't understand why none of you can see that!"
    show angela fragile
    "I'm looking at the same page as Angela right now."
    "And I can clearly see the lines of tight, neat handwriting filling it."
    "But then realisation hits me like a freight train."
    bree.say "She can't see the words!"
    bree.say "He hypnotised her so she can't see them!"
    "Dylan's already backing towards the door, shaking his head."
    show dylan shout
    "Dylan" "It's...it's a private journal..."
    "Dylan" "Of course I didn't want her to read it!"
    show dylan normal
    "Inspector" "So before it was notes for a novel."
    "Inspector" "Now it's a private journal."
    "Inspector" "Either way, it seems you've been keeping a lot from your wife."
    show dylan shout
    "Dylan" "So I have my secrets, so what?"
    show dylan normal
    "Inspector" "You sure do, Mister Devant."
    "Inspector" "And I suspect this is just the tip of the iceberg!"
    "Inspector" "Officers, take him away!"
    show camila work zorder 1 at center, zoomAt (1.15, (1160, 780)), dark, dark with easeinright
    show angela normal
    show dylan surprised
    "As if on cue, the door opens and two uniformed police officers pounce on Dylan."
    "I get the impression that he wants to say something, like a villain in a TV show."
    "But they manhandle him out of the room before he can get out a single word."
    hide dylan
    hide camila
    with easeoutleft
    show angela happy
    angela.say "Oh, lieutenant..."
    angela.say "How can I ever thank you?!?"
    show angela normal
    "The lieutenant chuckles and shakes his head."
    "Inspector" "There's no need to thank me, Madam - I'm only doing my job."
    "Inspector" "The one you want to thank is your companion right there."
    "Inspector" "She's the one that brought in the evidence we needed."
    "I can already feel my cheeks flushing as he says all of this."
    show angela happy zorder 4 at center, traveling (2.5, 0.3, (640, 1640))
    "But then Angela practically throws herself at me."
    hide angela
    hide inspector
    show angela kiss
    with fade
    $ angela.flags.kiss += 1
    "And I find her lips pressed tightly against mine a second later."
    "As soon as I regain my senses, I return the kiss with equal passion."
    "Because I'm finally beginning to let myself believe that our problems are over."
    "Dylan's under lock and key, and there may be a way to go yet."
    "But it looks like he's going to be going away for a long time."
    "Which means that Angela and I can actually start planning a future together."
    $ angela.flags.angeladelay = TemporaryFlag(True, 1)
    return

label angela_female_event_13b:
    scene bg angelalivingroom
    show dylan evil at center, zoomAt (1.5, (640, 1080))
    with fade
    "I know that I should do something, and fast!"
    "Run, throw something at Dylan, even just let out a scream."
    "But for some reason my muscles are frozen, and I can't move an inch."
    "I'll never shout at people in horror movies for doing that again."
    "Because right now, I know exactly how they're supposed to feel!"
    show dylan shout
    "Dylan" "I asked you a question!"
    "Dylan" "What are you doing in my house?!?"
    show dylan evil
    "Suddenly something seems to dawn on Dylan."
    "And he points an accusing finger in my direction."
    show dylan shout at center, zoomAt (1.0, (640, 1080)), stepback
    "Dylan" "You're a burglar, aren't you?"
    "Dylan" "You broke in here to steal my memorabilia, didn't you?"
    show dylan evil
    "As soon as he says this, I feel something dawn on me too."
    "The walls are covered in old posters of his act with Angela."
    "And he's clearly still obsessed with that part of his life."
    "So maybe I can use that to my advantage."
    bree.say "No!"
    bree.say "I'm not a burglar..."
    bree.say "I'm...I'm a..."
    "The words die in my throat as he raises a hand, looking me straight in the eye."
    "For a moment I have no idea what just happened, why I'm unable to finish speaking."
    "But then, to my horror, I realise that it's not just my lips and tongue that are paralysed."
    "Where before I was frozen by fear, now there's something else holding me in place."
    "I can't even move my eyes to tear them away from Dylan's own."
    "And it's only then that it dawns on me what must have happened."
    "Dylan's face becomes a picture of cruel amusement as he watches me realise what he already knows."
    show dylan shout at center, zoomAt (1.0, (640, 1080)), stepback
    "Dylan" "What's that, little thief?"
    "Dylan" "Cat got your tongue?"
    show dylan talkative
    "Dylan" "I suppose you've never been hypnotised before?"
    "Dylan" "And maybe you're one of those folks that thinks it's all phoney?"
    "Dylan" "The type that goes around claiming it only works on the weak-minded?"
    show dylan happy at startle
    "Dylan lets out a mocking laugh as he comes closer."
    "Dylan" "I'll let you into a little secret."
    "Dylan" "Those were always the ones that I enjoyed hypnotising the most!"
    "Dylan" "The doubters and the sceptics, I always made a point of humiliating them on stage."
    show dylan smile at center, zoomAt (1.5, (540, 1080)) with ease
    "He's walking around me now, looking me up and down."
    "But my eyes can only follow him when he's within my range of vision."
    "Whenever he steps out of it, I have no idea where he is or what he's doing."
    show dylan talkative at center, zoomAt (1.5, (740, 1080)) with ease
    "Dylan" "You know something..."
    "Dylan" "My wife was one of those people when we first met."
    "Dylan" "She was into science and logic, only believing things when she had so-called proof."
    "Dylan" "Even when I opened up to her about my passion for magic and my wish to become a stage magician..."
    show dylan shout at center, zoomAt (1.5, (640, 1080)) with ease
    "Dylan" "She laughed in my face!" with vpunch
    "Dylan" "But all of that changed when I convinced her to let me put her under."
    "Dylan" "Of course, she was sure that she'd be unaffected, that she'd shake it off."
    show dylan happy at center, zoomAt (1.5, (940, 1080)) with ease
    "Dylan" "What little she knew!"
    show dylan smile
    "I can feel myself starting to sweat now, as Dylan begins to rant."
    "He's opening up and confessing everything to me, which should be a good thing."
    "But I've seen enough films and TV shows to know what all of this means."
    show dylan at center, zoomAt (1.5, (540, 1080)) with ease
    "He's only telling me all of this stuff because he's sure I won't get to pass it on."
    "And that means he doesn't intend to let me go!"
    show dylan talkative
    "Dylan" "But maybe I should have done a better job on her."
    show dylan at center, zoomAt (1.5, (640, 1080)) with ease
    "Dylan" "As she did manage to run off with some little slut!"
    "Dylan" "But I won't make the same mistake again, not with you."
    "Dylan" "It's getting lonely around here, just by myself."
    show dylan happy
    "Dylan" "And I like the look of you, so I'll make you my new pet."
    show dylan smile
    "The fear that I was feeling before is now turning into sheer terror."
    "Because instead of saving Angela, I'm going to replace her!"
    "But no matter what I do, nothing seems to loosen his hold on me."
    show dylan talkative zorder 1 at center, zoomAt (1.5, (640, 1080)) with ease
    "Dylan" "Come to think of it, you might be the perfect candidate for something new."
    "Dylan" "I've been working on a way to make a subject totally obedient and loyal."
    "Dylan" "But at the same time keep their conscious mind aware of all that's happening to them."
    "Dylan" "To make them like a coma victim, trapped helplessly in their own body."
    "Dylan" "Able to see and feel everything, yet not have a single iota of control."
    "Dylan" "Hmm..."
    "Dylan" "It's going to take a lot of work."
    "Dylan" "So we'd best get started, hadn't we?"
    play music "<from 2 to 20>music/darren_curtis/into_oblivion.ogg" loop fadein 0.5 fadeout 5.0
    show dylan_fx_light as fx1 zorder 2 at center, zoomAt (1.5, (640, 1080))
    show fx spirale as fxleft zorder 3 at center, zoomAt (0.5, (563, 495))
    show fx spirale as fxright zorder 4 at center, zoomAt (0.5, (615, 495))
    with dissolve
    pause 0.1
    show dylan surprised at center, traveling(2.5, 5.0, (640, 1740))
    show dylan_fx_light as fx1 zorder 2 at center, traveling(2.5, 5.0, (640, 1740))
    show fx spirale as fxleft zorder 3 at center, traveling(0.8, 5.0, (513, 745))
    show fx spirale as fxright zorder 4 at center, traveling(0.8, 5.0,  (601, 745))
    "Dylan" "Follow me, girl..."
    "Dylan" "We have a busy night ahead of us!"
    show dylan smile
    "Without a conscious thought, my legs begin to move and I walk after him."
    "But even if I had the power to move my own body, I doubt I could have do so."
    show dylan at dark with dissolve
    "Because the effect of his words has been to send my mind into a hopeless spiral of panic."
    "I'm being made to walk towards a fate that sounds even worse than death."
    scene angela_dylan_ending_bg as bg
    show angela dylan ending zorder 4
    with fade
    "A waking nightmare in which I'll be forced to watch everything this monster does to me."
    show angela_dylan_ending_fx_swirl as swirl zorder 2 at clock(5), center, zoomAt(2.0, (640, 1800))
    show angela_dylan_ending_hands as hands zorder 3 at dark, center, zoomAt(1.0, (640, 820))
    pause 0.1
    show angela_dylan_ending_hands as hands zorder 3 at center, zoomAt(1.0, (640, 820))
    show angela_dylan_ending_hands as hands zorder 3 at center, traveling(1.0, 5.0, (640, 680))
    with dissolve
    show angela_dylan_ending_fx_sparks as sparks zorder 1 at flicker(1)
    show angela_dylan_ending_fx_stars as starts zorder 1 at flicker(2)
    show angela dylan ending mchypno angelahypno zorder 4
    with dissolve
    "And there's absolutely nothing I can do to stop it, no hope of escaping."
    "The idea to be enslaved alongside Angela is little comfort."
    hide angela_dylan_ending_fx_sparks as sparks zorder 1
    hide angela_dylan_ending_fx_stars as starts zorder 1
    show angela_dylan_ending_hands as hands at dark
    show angela dylan ending naked zorder 4
    with dissolve
    "The only thing I can pray for is that the silent screams inside of my head shatter my sanity."
    "That I descend into the oblivion of sheer madness and lose all sense of myself."
    $ DONE["angela_female_event_13b"] = game.days_played
    scene bg black with dissolve
    pause 1.0

    $ renpy.full_restart()

label angela_female_event_13c:
    scene bg angelalivingroom
    show dylan at center, zoomAt (1.5, (640, 1080))
    with fade
    "I feel myself unconsciously adopting one of the stances I was taught in martial arts class."
    "And at the same time I'm also tensing my muscles and preparing for Dylan to make a sudden move."
    "Hell, I can even see the counters and moves that I could use if he comes at me in certain ways."
    "But none of that seems to be obvious to Dylan, as he keeps right on pressing me for an answer."
    show dylan shout at center, zoomAt (1.0, (640, 1080)), stepback
    "Dylan" "I asked you a question!"
    "Dylan" "What are you doing in my house?!?"
    show dylan normal
    "Suddenly something seems to dawn on Dylan."
    "And he points an accusing finger in my direction."
    show dylan shout at center, zoomAt (1.0, (640, 1080)), stepback
    "Dylan" "You're a burglar, aren't you?"
    "Dylan" "You broke in here to steal my memorabilia, didn't you?"
    show dylan normal
    "As soon as he says this, I feel something dawn on me too."
    "The walls are covered in old posters of his act with Angela."
    "And he's clearly still obsessed with that part of his life."
    "Which means he's a mark for himself, and so pretty pathetic."
    bree.say "No!"
    bree.say "I'm not a burglar..."
    bree.say "I'm a martial artist."
    bree.say "And if you don't back off, I'm gonna kick your ass!"
    "I add a quick and pretty impressive flurry of moves after that."
    "Which is usually more than enough to scare the shit out of someone."
    "Or at the very least make them back off, realising what they're messing with."
    "But instead, Dylan seems to be amused by the move."
    show dylan shout at center, zoomAt (1.5, (540, 1080)) with ease
    "Dylan" "Oh you are, are you?"
    "Dylan" "And that's supposed to scare me?"
    show dylan evil
    "All I can do is shrug in response to that."
    bree.say "Well, yeah..."
    bree.say "I mean, you're a fucking magician, for god's sake."
    bree.say "Not some kind of super-macho, underground fighting champion!"
    show dylan happy at center, zoomAt (1.0, (640, 1080)), startle
    "Dylan let's out a deep, booming laugh at this."
    "And I mean one that's really up there in movie-villain territory."
    "Dylan" "Oh, you poor fool!"
    "Dylan" "Do you really think that stage magic is simply all smoke and mirrors?"
    "Dylan" "The first thing we learn in magic school is the art of sorcerous self-defence!"
    show dylan smile staff at center, zoomAt (1.5, (640, 1080)) with ease
    "As he says this, Dylan thrusts out one hand, stretching out his fingers."
    "And right before my eyes, one of the wands mounted on the wall begins to quiver."
    "Then it pops from it's fixtures, flying across the intervening space."
    "The next thing I know, it's in Dylan's hand, and he's swinging it at me!"
    play sound woosh_punch
    "I leap backwards the tip of the wand missing my head by mere inches."
    play sound woosh_punch
    "But Dylan follows up with a furious series of swings."
    play sound woosh_punch
    "Each of them feels like I dodge it by a fraction of an inch less"
    play sound woosh_punch
    "With the last swing, he makes an attempt to catch me."
    "This means that he overreaches himself, just enough for me to capitalise on the mistake."
    "I'm quick to counter, landing a blow that sends him staggering backwards." with hpunch
    show dylan at center, zoomAt (1.5, (740, 1080)) with ease
    "Quick as a flash, I regain my composure and leap towards Dylan."
    "Aiming a vicious flying-kick at his head."
    "And I'm sure that would have ended the fight if it'd have connected."
    play sound woosh_punch
    "But somehow Dylan manages to dodge it and pull a pack of cards out of his sleeve."
    show dylan happy at center, zoomAt (1.5, (640, 1080)) with ease
    "Dylan" "Pick a card..."
    "Dylan" "Any card..."
    "Dylan" "Because they all foretell your doom!"
    show dylan smile
    play sound woosh_punch
    "Dylan squeezes the pack and somehow launches then all into the air at once."

    play sound woosh_punch
    queue sound woosh_punch
    queue sound woosh_punch
    "The cards fly at me, and I feel them slicing through my clothes as well as my skin."
    "Shit - those their edges are sharp as razor-blades!"
    "Covering up, I manage too push through the deadly storm of cards."
    "But once I'm on the other side, I see that Dylan hasn't been idle."
    "Instead he's waiting for me, clutching a top-hat in his hands."
    bree.say "Ha..."
    bree.say "What are you gonna do with that?"
    bree.say "Pull out a rabbit to bite my butt?"
    show dylan shout at center, zoomAt (1.0, (640, 1080)), stepback
    "Dylan" "Oh, you wish..."
    "Dylan" "I swore that I'd never use this move."
    "Dylan" "But you leave me with no choice..."
    show dylan evil
    "Dylan points the underside of the hat towards me."
    "Then he pulls it back under his arm."
    scene bg black
    show magicshow_house as bg zorder 1 at center, zoomAt(1.0, (640, 720))
    show magicshow_dylan as mdylan zorder 4 at center, zoomAt(1.0, (540, 720))
    show magicshow_breemc_dodge as mbree zorder 2 at center, zoomAt(1.0, (640, 720))
    with hpunch
    "Dylan" "HATOKEN!"
    show magicshow_dylan as mdylan zorder 4 at center, traveling(1.0, 0.1, (600, 720))
    "I watch in amazement as he thrusts it forwards again."
    with screenshot
    play sound doves
    show magicshow_doves as mdoves zorder 3 at center, zoomAt(1.0, (580, 720))
    "And a ball of wriggling doves shoots out of it."
    "I mean that literally, it's live doves."
    play sound doves
    show magicshow_doves as mdoves zorder 3 at center, traveling(1.0, 0.3, (640, 720))
    "Which is flying straight towards me!"
    "At the last possible moment, my finely-honed instincts kick in."
    show magicshow_breemc_dodge as mbree zorder 2 at center, traveling(1.0, 0.2, (740, 720))
    play sound woosh_punch
    "I leap to the side, the ball of birds missing me and shooting past."
    show magicshow_doves as mdoves zorder 3 at center, traveling(1.0, 0.2, (1020, 220))


    "Then I hear it colliding with the shelves and cabinets behind me." with vpunch
    scene bg angelalivingroom
    show dylan surprised at center, zoomAt (1.25, (640, 900))
    "Dylan" "No..."
    "Dylan" "Dear gods, no!"
    "Dylan" "Not my precious memorabilia!"
    show dylan stuned
    "He seems to have forgotten all about me as he rushes to assess the damage."
    play sound punch_hard
    pause 0.2
    show dylan surprised with hpunch
    "Which leaves me free to land a blow that sends him spinning through the air."
    play sound punch_hard
    pause 0.2
    with hpunch
    pause 0.1
    hide dylan with easeoutbottom
    play sound body_fall
    "And another that knocks the air out of him and I'm sure cracks a rib as he hits the floor."
    "Dylan" "Aargh..."
    "Dylan" "No more, please..."
    "Dylan" "Mercy, I beg you - have mercy!"
    "I make a point of pushing my heel down and into Dylan's chest."
    "And I really grind it in there, making sure I feel bone scraping against bone."
    "Dylan" "AAARGH!" with vpunch
    bree.say "Stop wailing, you worthless piece of shit!"
    bree.say "Now you listen to me, and you listen good."
    bree.say "Angela's no longer a part of your life, and she never will be again."
    bree.say "You got that?!?"
    "Another burst of pressure on Dylan's ribs underlines my point."
    "Dylan" "YES!"
    "Dylan" "Yes, I get it!"
    bree.say "You're not welcome in this city either."
    bree.say "So you're going to get the fuck out and never come back too"
    "This time I only threaten another stomping."
    "But the effect is still pretty impressive."
    "Dylan flinches from the expected pain."
    "And even when it's not forthcoming, he still cowers in fear."
    "But I also see that he's nodding his head as he curls himself into a foetal position on the floor."
    "I shake my head feeling more pity than anger as I watch him crawl in total defeat."
    "Sure that he won't be getting up anytime soon, I turn my back on him and walk away."
    "I also make a point of letting myself out of the front-door, rather than using the window."
    "And I leave it open, letting the cold night air flood into the house behind me."
    $ angela.flags.angeladelay = TemporaryFlag(True, 1)
    $ DONE["angela_female_event_13c"] = game.days_played
    return


label angela_female_event_12b:
    "If I'm going to get anyone else involved in this affair, it needs to be someone I can trust."
    "And it wouldn't hurt for them also to be someone that has a dog in the fight too."
    "[mike.name]'s a person that ticks both of those boxes, so going to him seems a no-brainer."
    "But I just have to be careful about how I pitch the idea to him."
    "Better he sees this as a chance to help out his mom in her time of need."
    "Rather than his housemate turned mom's lover asking him to spy on his dad!"
    "So the first chance I get to talk to [mike.name] alone, I steel myself for the task ahead..."
    show mike normal at center, zoomAt (1.25, (640, 900)) with fade
    bree.say "Ah..."
    bree.say "[mike.name]..."
    "At the sound of my voice, [mike.name] glances around."
    "And I can instantly see that he seems to have a lot on his mind."
    "Which is understandable, given the circumstances."
    show mike surprised
    show fx question
    mike.say "Uh..."
    mike.say "Hey, [hero.name]..."
    mike.say "What's the problem?"
    show mike annoyed
    "Almost the moment he blurts out the question, [mike.name] looks annoyed with himself."
    "He shakes his head, as if trying to throw off the funk that he's in."
    "And then he scrubs his face with both hands, leaving himself looking bleary-eyed."
    hide fx
    show mike shout
    mike.say "Urgh..."
    mike.say "Sorry, [hero.name]..."
    mike.say "I've just been dealing with some pretty heavy family stuff recently."
    mike.say "You know that my mom went missing?"
    mike.say "And my dad keeps calling me all the time too!"
    mike.say "Like he thinks I know where she could be or something..."
    show mike sad
    "I get the sense that [mike.name]'s beginning to pour his heart out to me."
    "But the fact is that I know more about the whole thing than he does."
    "And if I want him to help me out, then I guess I'll have to come clean."
    "So I hold up a hand to stop him."
    bree.say "Okay, [mike.name]..."
    bree.say "I'm going to tell you something now."
    bree.say "But you're probably not going to like it."
    show mike normal
    "[mike.name] looks at me with a mixture of hope and confusion on his face."
    "And for a moment I think he might actually tell me he doesn't want to hear it."
    "That information that comes with caveats like that is too much for him to handle."
    show fx question
    show mike surprised
    mike.say "Is it something about my mom?"
    mike.say "Do you know where she is?!?"
    show mike angry
    mike.say "[hero.name], if it is, then you have to tell me!"
    show mike upset
    "I hold up my hands in an effort to have [mike.name] slow down."
    bree.say "First things first, [mike.name]..."
    bree.say "You need to know that your mom and I have become...close."
    bree.say "Like, really close!"
    "I'm expecting [mike.name] to freak out at this, or at least to be mad at me."
    "But instead he kind of just lets out a sigh and nods his head."
    show mike shout
    mike.say "Phew..."
    mike.say "I kind of had my suspicions, [hero.name]!"
    mike.say "You seemed to be getting pretty close recently."
    mike.say "And she was talking about you all the time too."
    show mike sad
    bree.say "You're not mad with me are you, [mike.name]?"
    show mike shout
    mike.say "Not really, [hero.name]..."
    mike.say "I thought mom and dad were going through a rough patch."
    mike.say "So knowing she has someone to care for her is kind of a relief!"
    show mike normal
    "I know that [mike.name] means by that."
    "Because I can feel the relief flooding through my veins too!"
    show mike surprised
    mike.say "Plus it means that you know where my mom is, right [hero.name]?"
    mike.say "Because if you did, you'd tell me, wouldn't you?"
    show mike normal
    "And there it is, the emotional punch to the gut!"
    bree.say "Okay, [mike.name]..."
    bree.say "I do know where she is."
    bree.say "But I can't tell you where, just that she's safe."
    show mike upset
    "[mike.name] shakes his head at this."
    "Like he's unable to believe what he's hearing."
    show mike angry
    mike.say "[hero.name]!"
    mike.say "Are you being serious right now?!?"
    show mike upset
    bree.say "Just hear me out, [mike.name]."
    bree.say "Because when you hear what I have to say, you'll understand my reasons."
    "[mike.name]'s looking at me with a serious amount of suspicion in his eyes."
    "And based on what he knows about all of this, I can't say that I blame him."
    "So I'd better make my explanation a damn good one."
    bree.say "You know that your mom's been having blackouts, right?"
    show mike shout
    mike.say "Of course I do, [hero.name]!"
    mike.say "But she told me they're nothing serious."
    mike.say "She went to the hospital and got checked out."
    mike.say "She's on medication and everything."
    show mike normal
    "I shake my head, unable to believe what I'm hearing."
    bree.say "That's not how it is at all!"
    bree.say "And the hospital didn't give her medication."
    bree.say "I went there with her - they said there was nothing medically wrong with her!"
    show mike surprised
    mike.say "What are you talking about, [hero.name]?"
    mike.say "Why would my mom lie to me?"
    show mike upset
    bree.say "Because she doesn't know she's lying, [mike.name]..."
    bree.say "Because your dad's hypnotising her!"
    show mike surprised
    "[mike.name] stares at me in silence for a moment."
    show mike happy at startle
    "Then he bursts out laughing."
    mike.say "Oh wow, [hero.name]..."
    mike.say "That's a good one!"
    mike.say "What are you going to tell me next?"
    mike.say "That he's used his magic tricks to make her disappear?"
    bree.say "Think about it, [mike.name]!"
    bree.say "She's hysterical one time you see her."
    bree.say "But the next time she can't even remember it!"
    show mike down
    "This last point does seem to get through to [mike.name]."
    "He pauses like he's turning it over in his head."
    show mike shout
    mike.say "You know..."
    mike.say "I always thought that was her just burying stuff."
    mike.say "Not dealing with it..."
    show mike down
    bree.say "You see, [mike.name]?"
    bree.say "Your mom's in real danger."
    bree.say "And the danger is your dad!"
    bree.say "Will you help me do what I need to do to save her?"
    if mike.love >= 100:
        show mike normal
        "[mike.name] nods at this."
        show mike upset
        "And I see the look on his face become resolute."
        show mike shout
        mike.say "You bet I will, [hero.name]!"
        mike.say "Everything you've told me would sound crazy on it's own."
        show mike angry
        mike.say "But when you put it all together, it kind of starts to make sense."
        show mike upset
        "I'm nodding like crazy by now."
        "Trying to encourage [mike.name] as much as I can."
        bree.say "I know, I know..."
        bree.say "We're through the looking glass here, [mike.name]."
        bree.say "But I've already spoken to the police."
        bree.say "They say they can help, but we need evidence."
        show mike surprised
        mike.say "What kind of evidence, [hero.name]?"
        show mike normal
        bree.say "The kind that your dad might have, [mike.name]."
        bree.say "The kind you could find if you went to his place."
        "Now it's [mike.name]'s turn to nod."
        show mike shout
        mike.say "I hear you, [hero.name]."
        mike.say "I'll cook up an excuse to go see him."
        mike.say "Then I can sneak into his study and find something incriminating."
        show mike normal
        "I feel a sudden sense of hope begin to grow in my chest."
        "And for the first time in as long as I can remember, I don't feel like Angela and I are alone in this."
        "With [mike.name] helping us out, I just know we can bring this guy to justice."
        $ angela.flags.outside_help = "mike"
        $ angela.flags.angeladelay = TemporaryFlag(True, 1)
    else:
        show mike upset
        "[mike.name] shakes his head."
        "And the expression on his face is firm."
        show mike shout
        mike.say "No I won't, [hero.name]."
        mike.say "First you won't tell me where my mom is."
        mike.say "Then you tell me my dad's hypnotising her!"
        show mike angry
        mike.say "And the worst thing is that you expect me to buy it all..."
        mike.say "Then sign up for some crazy plan that you've cooked up!"
        show mike upset
        bree.say "But, [mike.name]..."
        bree.say "It's the truth!"
        hide mike with easeoutleft
        "[mike.name] doesn't even respond to my final plea."
        "Instead he turns on his heel and walks away."
        "Leaving me pretty much back where I started."
        "That and in need of a new plan."
        $ angela.flags.outside_help = None
    $ game.room = "street"
    $ hero.replace_activity(end_event=True)
    scene bg black with dissolve
    return

label angela_female_event_13d:
    scene expression f"bg {game.room}"
    with fade
    "I've been on tenterhooks waiting to hear back from [mike.name] ever since he agreed to my crazy scheme."
    "And by now there's been more than enough time for him to have been to his parent's house and back."
    "Of course it's not as simple as him just nipping home on the pretence of seeing his dad."
    "There's also the small matter of his needing to search his parent's house for the proof I need."
    "Which is another issue on top of the last, because I don't know what form that evidence would even take."
    "But despite all that, I keep on looking up at the merest sound of another person approaching."
    show mike b smile at center, zoomAt(1.25, (940, 920)) with easeinright
    "And when I finally see that the person approaching is [mike.name], I feel my heart leap into my mouth."
    show mike b at center, zoomAt(1.25, (640, 920)) with ease
    bree.say "[mike.name!u]!"
    bree.say "You made it back?"
    bree.say "Does that mean you pulled it off?"
    bree.say "Did you find what we're looking for?!?"
    "I know full well that I'm coming on strong."
    "Not even giving [mike.name] a chance to say hi before pressing him for information."
    "But that's just where my head is right now, and I need to know if he found the proof."
    "Yet there's something odd about the way he reacts to my stream of questions."
    show mike b annoyed
    "At first [mike.name] looks a little overwhelmed by the verbal barrage."
    "But then, as I start to ask how the whole thing went, he starts to look more confused."
    show mike b surprised
    mike.say "[hero.name]..."
    mike.say "[hero.name], slow down, for god's sake!"
    mike.say "You're going so fast that I can't tell what you even mean."
    show mike b normal
    "I'm more than a little frustrated by [mike.name]'s reaction."
    "But that last plea at least gives me hope."
    "Because I take it to mean that I'm going too fast to be clear."
    "So all I should need to do in order to remedy it is slow down. "
    bree.say "Okay, [mike.name]..."
    bree.say "Sorry..."
    bree.say "I just got a little carried away there."
    show mike a smile
    "[mike.name] nods, letting me know that he understands and there's no hard feelings."
    show mike a happy
    mike.say "No worries, [hero.name]."
    show mike a shout
    mike.say "Now what was all that about?"
    show mike smile
    "I'm a little put off by the way [mike.name]'s making me go around the houses right now."
    "Even if I wasn't being exactly clear before, I still sent him off on a pretty important mission."
    "I'd have thought reporting back to me on what he's found would have been a high priority."
    bree.say "What do you think it was about, [mike.name]?"
    bree.say "You just got back from you folk's place, right?"
    bree.say "So what did you find?"
    show mike surprised
    "[mike.name] surprises me again by frowning."
    "And then he stares at me with a quizzical look on his face."
    mike.say "Erm..."
    show mike shout
    mike.say "I found my dad there, [hero.name]."
    mike.say "Rambling around the place all on his own."
    show mike sad
    "I can't actually believe what I'm hearing."
    "And so it's impossible to keep the surprise off my face and out of my voice."
    bree.say "What in the hell are you talking about?!?"
    "[mike.name] just doesn't seem to read the emotions I'm radiating right now."
    "Instead he seems to interpret my words as reflecting his own sentiments."
    show mike shout
    mike.say "Tell me about it, [hero.name]!"
    mike.say "But it's always the same when mom goes away like this."
    mike.say "She visits a friend or a relative for a few weeks at a time."
    mike.say "And dad says he'll be fine, he always does."
    mike.say "The truth is that he really can't cope on his own - he's hopeless!"
    show mike sad
    "For a moment I just stare at [mike.name], my mouth hanging open."
    "It's like he's making an inappropriate joke out of all this."
    "And I'm just hanging on, waiting for him to realise it's in bad taste."
    "But the only problem is that doesn't happen."
    "Instead he keeps on staring at me, then adds a helpless shrug."
    show mike shout
    mike.say "I give up, [hero.name]..."
    mike.say "What is it?"
    mike.say "Why are you looking at me like that?"
    show mike sad
    bree.say "[mike.name], don't you remember what we talked about before you went to your parent's house?"
    bree.say "You were going to look for proof of what your dad's been doing to Angela?"
    show mike upset
    "It's only now that [mike.name]'s expression changes."
    "I watch as it becomes darker and more concerned."
    show mike angry
    mike.say "What are you talking about, [hero.name]?"
    mike.say "Are you...are you accusing my dad of something?!?"
    mike.say "Because I really don't appreciate that!"
    show mike upset
    "I feel like this conversation is heading into dangerous territory."
    "But I also feel like I owe it to Angela to press [mike.name] for more information."
    bree.say "[mike.name], I'm being serious now..."
    bree.say "You were supposed to look for proof, remember?"
    bree.say "Proof that your dad's been hypnotising your mom?"
    show mike smile
    "Suddenly [mike.name]'s mood changes again, just as quickly as before."
    "Only now he's smiling and shaking his head."
    "Like there's nothing at all amiss about the accusation."
    show mike happy
    mike.say "Of course he's hypnotised her, [hero.name]."
    mike.say "He must have done it a hundred times in their act."
    mike.say "And he explained all about it to me when I asked him."
    mike.say "Hell, he even showed me some of his techniques - and they were pretty impressive too!"
    show mike smile
    "I'm shaking my head as [mike.name] tells me all of this."
    "But he doesn't seem to notice."
    "In fact he starts nodding his head, as if something now makes sense to him."
    show mike happy
    mike.say "That must be what you're getting confused about, [hero.name]."
    mike.say "You ask me to quiz my dad about his act when I saw him next."
    mike.say "I remember now!"
    show mike smile
    "The look on [mike.name]'s face and his sudden happiness is starting to freak me out."
    "It's like he's slipped into some kind of prerecorded script without knowing it."
    "And it reminds me of the way Angela was behaving when she denied stuff happened."
    "That's when it begins to make sense to me, and I realise that he's been hypnotised too!"
    "Dylan must have sensed what was going on and used his powers on [mike.name]!"
    bree.say "Ah..."
    bree.say "Yeah, [mike.name]..."
    bree.say "You must be right!"
    hide mike with easeoutleft
    "[mike.name] nods happily at this and wanders off on his way."
    "Which leaves me all the more determined to dig deeper."
    "Because if Dylan did hypnotise him, that means there really is something worth hiding in that house."
    "But it looks like I'm going to have to find another way of getting in there and finding it for myself."
    $ angela.flags.outside_help = None
    return

label angela_female_event_13e:
    scene expression f"bg {game.room}"
    with fade
    "I've been on tenterhooks waiting to hear back from [mike.name] ever since he agreed to my crazy scheme."
    "And by now there's been more than enough time for him to have been to his parent's house and back."
    "Of course it's not as simple as him just nipping home on the pretence of seeing his dad."
    "There's also the small matter of his needing to search his parent's house for the proof I need."
    "Which is another issue on top of the last, because I don't know what form that evidence would even take."
    "But despite all that, I keep on looking up at the merest sound of another person approaching."
    show mike b smile at center, zoomAt(1.25, (940, 920)) with easeinright
    "And when I finally see that the person approaching is [mike.name], I feel my heart leap into my mouth."
    show mike b at center, zoomAt(1.25, (640, 920)) with ease
    bree.say "[mike.name!u]!"
    bree.say "You made it back?"
    bree.say "Does that mean you pulled it off?"
    bree.say "Did you find what we're looking for?!?"
    "I know full well that I'm coming on strong."
    "Not even giving [mike.name] a chance to say hi before pressing him for information."
    "But that's just where my head is right now, and I need to know if he found the proof."
    "Yet there's something odd about the way he reacts to my stream of questions."
    show mike b annoyed
    "At first [mike.name] looks a little overwhelmed by the verbal barrage."
    "But then, as I start to ask how the whole thing went, he holds up a hand to stop me."
    show mike b surprised
    mike.say "[hero.name]..."
    mike.say "[hero.name], slow down, for god's sake!"
    mike.say "You're going so fast, you're not making any sense."
    show mike b normal
    "I'm more than a little frustrated by [mike.name]'s reaction."
    "But that last plea at least gives me hope."
    "Because I take it to mean that I'm going too fast to be clear."
    "So all I should need to do in order to remedy it is slow down. "
    bree.say "Okay, [mike.name]..."
    bree.say "Sorry..."
    bree.say "I just got a little carried away there."
    show mike a smile
    "[mike.name] nods, letting me know that he understands and there's no hard feelings."
    show mike a happy
    mike.say "No worries, [hero.name]."
    show mike a shout
    mike.say "Now what was all that about?"
    show mike smile
    "I'm a little put off by the way [mike.name]'s making me go around the houses right now."
    "Even if I wasn't being exactly clear before, I still sent him off on a pretty important mission."
    "I'd have thought reporting back to me on what he's found would have been a high priority."
    bree.say "What do you think it was about, [mike.name]?"
    bree.say "You just got back from you folk's place, right?"
    bree.say "So what did you find?"
    show mike normal
    "Even as I'm saying all of this, I see [mike.name]'s expression change."
    "He nods, finally acknowledging what I'm talking about for the first time."
    show mike shout
    mike.say "Oh yeah, [hero.name]..."
    mike.say "I did what you asked."
    mike.say "I looked into what my dad's been up to."
    show mike normal
    bree.say "And what did you find?"
    bree.say "Did you get the proof I need?!?"
    "[mike.name] nods again, and I feel a surge of relief."
    show mike shout
    mike.say "Yeah, [hero.name]..."
    mike.say "And what's more, I confronted my dad."
    mike.say "I told him all of what you told me."
    mike.say "And he confessed to it, every last word."
    show mike normal
    "I'm feeling a strange mix of emotions as [mike.name] tells me all of this."
    "Because on the one hand, that's great news."
    "But on the other, it's not what I asked [mike.name] to do."
    "And I have no idea what it's going to mean now his dad knows I'm onto him."
    bree.say "So he told you how he did it?"
    bree.say "He told you how he hypnotised Angela?"
    show mike happy at center, traveling(1.5, 0.5, (640, 1080))
    mike.say "Oh, he did much better than that, [hero.name]..."
    mike.say "He showed me exactly how he did it!"
    show mike smile
    bree.say "[mike.name]..."
    bree.say "What do you..."
    play music "<from 2 to 20>music/darren_curtis/into_oblivion.ogg" loop fadein 0.5 fadeout 5.0
    show mike b smile zorder 1 at center, zoomAt (1.5, (640, 1080))
    show dylan_fx_light as fx1 zorder 2 at center, zoomAt (1.56, (642, 1127))
    show fx spirale as fxleft zorder 3 at center, zoomAt (0.5, (563, 505))
    show fx spirale as fxright zorder 4 at center, zoomAt (0.5, (616, 505))
    "The words die in my throat as he raises a hand, looking me straight in the eye."
    "For a moment I have no idea what just happened, why I'm unable to finish speaking."
    "But then, to my horror, I realise that it's not just my lips and tongue that are paralysed."
    "Where before I was frozen by fear, now there's something else holding me in place."
    "I can't even move my eyes to tear them away from [mike.name]'s own."
    "And it's only then that it dawns on me what must have happened."
    "[mike.name]'s face becomes a picture of cruel amusement as he watches me realise what he already knows."
    show mike happy
    mike.say "That's right, [hero.name]..."
    mike.say "My dad thought it was time he passed his skills onto his only son."
    mike.say "And I can't believe what I've been missing out on all these years!"
    mike.say "All those times that girls rejected me, that I was passed up for a promotion."
    mike.say "He's given me the power to make sure that those things never happen to me again."
    mike.say "He's given me the power to control my own destiny!"
    show mike smile
    "I always wondered what it would be like to be hypnotised."
    "Even came to fear it once I realised what was happening to Angela."
    "But there's no way I could have been prepared for the reality of it."
    "I feel like a creeping horror is spreading over me as realisation dawns."
    "I'm completely helpless, just like Angela was before me!"
    show mike angry
    mike.say "Of course there was a price for all of this knowledge and power."
    mike.say "My dad made me promise to stay out of his relationship with mom."
    show mike shout
    mike.say "But now I know what he's been doing to her, I'm not concerned anymore."
    mike.say "He made me see that she's better off this way, happier, you know?"
    show mike happy
    mike.say "Oh, and the other thing he made me promise was to take care of you."
    show mike smile at dark with dissolve
    "[mike.name]'s smile has never looked this way to me before."
    "It's sinister and full of hinted malevolence towards me."
    show mike happy
    mike.say "But the way I see it, this is more of a reward."
    mike.say "You get to stop fretting about my mom and her affairs."
    mike.say "And I get to work my new powers on you."
    mike.say "I think we'll start by making you obedient and grateful."
    mike.say "That always worked with my mom."
    show mike a smile zorder 1 at center, traveling(2.5, 10.0, (640, 1740))
    show dylan_fx_light as fx1 zorder 2 at center, traveling(2.6, 10.0, (642, 1816))
    show fx spirale as fxleft zorder 3 at center, traveling(0.95, 10.0, (500, 855))
    show fx spirale as fxright zorder 4 at center, traveling(0.95, 10.0,  (588, 855))
    "I want to resist, to scream out in defiance of all that [mike.name]'s saying."
    "There's no way that I can tell if this change in him is real."
    "Or if his dad managed to hypnotise him too and reprogram his brain."
    "But in the end it doesn't really matter which is the truth."
    "[mike.name]'s powers of hypnosis are all too real, and I can't resist them."
    "So the only thing that I can do is stand there and listen to his words."
    "And slowly feel my will ebbing away as he makes good on his promise."
    "I know that soon I won't be able to remember any of this at all."
    "The only thoughts in my head will be the ones that he's put in there."
    "And that's more terrifying than anything else."
    "The knowledge that I could spend years, even the rest of my life as a prisoner in my own head!"
    show mike shout
    mike.say "So..."
    mike.say "We have a lot of work ahead of us, [hero.name]."
    mike.say "Shall we get started?"
    show mike normal
    bree.say "Y...yes, [mike.name[0]]...[mike.name]..."
    show mike angry
    mike.say "No, no, no..."
    show mike happy
    mike.say "Try that again."
    show mike smile
    bree.say "Yes...Master..."
    "Without a conscious thought, my legs begin to move and I walk after him."
    "But even if I had the power to move my own body, I doubt I could have do so."
    "Because the effect of his words has been to send my mind into a hopeless spiral of panic."
    "I'm being made to walk towards a fate that sounds even worse than death."
    scene angela mike ending zorder 1
    with fade
    "A waking nightmare in which I'll be forced to watch everything this monster does to me."
    show angela_dylan_ending_fx_swirl as swirl zorder 3 at clock(5), center, zoomAt(2.0, (640, 1800))
    with dissolve
    show angela_dylan_ending_fx_sparks as sparks zorder 2 at flicker(1)
    show angela_dylan_ending_fx_stars as starts zorder 2 at flicker(2)
    with dissolve
    "And there's absolutely nothing I can do to stop it, no hope of escaping."
    hide angela_dylan_ending_fx_sparks as sparks
    hide angela_dylan_ending_fx_stars as starts
    with dissolve
    "The only thing I can pray for is that the silent screams inside of my head shatter my sanity."
    "That I descend into the oblivion of sheer madness and lose all sense of myself."
    scene bg black with dissolve
    pause 1.0

    $ renpy.full_restart()



label angela_female_event_12c:
    "If I'm going to do this thing and free Angela from her abusive husband, then I have to get serious."
    "That means bringing in the big guns, which in this case means getting the help of someone who gets results."
    "And there's only one person I know that always does that, who embodies all the qualities of a real winner."
    "Which is why I find myself standing outside the doors of Dwayne's palatial office, getting my head in order."
    "Only when I feel like I'm ready do I push the doors open and walk inside."
    "But the moment I do so, I can feel my heart start racing inside of my chest."
    "Normally I'd be able to resist Dwayne's brand of alpha-male bullshit."
    "And his Giga-Chad aura would be just slide off of me like water off a duck's back."
    "The problem right now is that I'm not meeting Dwayne on an equal playing field."
    "I'm coming to him in order to ask a favour, and he knows that."
    show dwayne happy at center, zoomAt(1.25, (640, 920)) with fade
    dwayne.say "Well, well, well..."
    dwayne.say "[hero.name], what a pleasure it is to see you."
    dwayne.say "And when I say that, I mean a pleasure for the eyes."
    dwayne.say "Because you are looking divine!"
    show dwayne normal
    "Dwayne's sitting back in his huge chair as he says all of this."
    "Which, of course, is behind his equally huge desk"
    "And in the middle of his ludicrously huge office."
    "All in all, he looks more like a king on his throne than the bigtime boss of a modern company."
    bree.say "Erm..."
    bree.say "Hello, Dwayne."
    bree.say "You look...prosperous, I guess."
    show dwayne smile
    "Dwayne's mouth twists into a shape that seems to express his amusement."
    "But somehow I can't quite bring myself to describe it as a smile."
    show dwayne happy
    dwayne.say "I'm going to assume you mean that in terms of my surroundings..."
    dwayne.say "Rather than my gut!"
    show dwayne shout
    dwayne.say "But enough with the pleasantries, [hero.name]."
    dwayne.say "Come take a seat."
    show dwayne normal
    "Dwayne gestures to the somewhat smaller chair on my side of the desk."
    "So I scuttle over and perch on the edge of it, leaning forwards."
    bree.say "Thanks for seeing me at such short notice, Dwayne."
    bree.say "I know that you're a busy man and all that."
    "Dwayne waves a hand in the air."
    "As if dismissing my concerns."
    show dwayne shout
    dwayne.say "Not at all, [hero.name]."
    dwayne.say "I've always got time for a beautiful woman like yourself."
    dwayne.say "And when I heard you wanted to see me, but wouldn't say why..."
    show dwayne happy
    dwayne.say "Well, I was intrigued, to say the least!"
    show dwayne smile
    "Dwayne puts his elbows down on the desk and leans forwards as he says this."
    "And for the first time I sense a genuine change in his demeanour."
    "Before he was all gushing charm and showing-off his clout."
    "But now I sense a more keen, even predatory side to him coming out."
    "And I wonder if this is how he is with his competition in business."
    show dwayne shout
    dwayne.say "So, [hero.name]..."
    dwayne.say "Just what could be so important?"
    dwayne.say "What could you want from me that you need to keep secret?"
    show dwayne normal
    "I'm starting to feel more than a little intimidated by now."
    "Aware of the fact that Dwayne and I are alone in his office."
    "But I do the best I can to gather my confidence and see it through."
    bree.say "Basically, I have a problem..."
    bree.say "A problem of a deeply personal nature."
    bree.say "And I want to ask for your help in solving it."
    "Dwayne leans back in his chair again."
    "And he holds up his hands, gesturing to the office in which we're sitting."
    show dwayne shout
    dwayne.say "You may have noticed that I'm pretty good at what I do, [hero.name]."
    dwayne.say "But you may not be aware that my business isn't solving people's problems."
    show dwayne normal
    bree.say "I know that, Dwayne..."
    bree.say "But I already went to the police."
    bree.say "And they can't help me!"
    show dwayne therock
    "At the mention of the police, I see Dwayne's eyebrows rise."
    "And I feel a pang of hope that I've piqued his interest."
    show dwayne shout
    dwayne.say "So the police can't help..."
    dwayne.say "But you think I can?"
    show dwayne normal
    bree.say "You're a very persuasive man, Dwayne."
    bree.say "You know people, right?"
    bree.say "You know ways to get what you want?"
    bree.say "To get things done?"
    show dwayne therock
    "Dwayne tilts his head on one side and then back again."
    "Like the way he twisted his mouth into something that wasn't quite a smile, it's not quite a nod."
    "But all the same, I take it as an indication of interest."
    show dwayne shout
    dwayne.say "You'd better tell me all about this problem of yours, [hero.name]."
    dwayne.say "Then I can tell you what I think would be for the best."
    show dwayne normal
    "I nod eagerly, already beginning to explain myself."
    bree.say "Okay..."
    bree.say "I'm in a relationship with a woman..."
    bree.say "An older woman called Angela."
    show dwayne therock
    "Again I see a slight upturn in Dwayne's interest."
    "Like he's intrigued to hear more about my private life."
    "But I can't let that get to me now, as I have to make my case."
    bree.say "She's still married to her husband, but we're very much in love."
    bree.say "Recently she started having these weird blackouts."
    bree.say "And she was coming round in places she had no memory of going to."
    bree.say "She'd tell me about it, but the next time I saw her she'd deny it ever happened."
    bree.say "I even took her to the hospital to get checked out, but the results were negative."
    "Dwayne lets out a grunt at this."
    show dwayne shout
    dwayne.say "Huh..."
    dwayne.say "Tall stories with no evidence whatsoever."
    dwayne.say "Sounds to me like this Angela of yours is doing it for attention."
    show dwayne normal
    "I shake my head at this, instantly protesting."
    "But at the same time, part of me is amazed to hear the anger in my own voice."
    bree.say "That's not how it is!"
    bree.say "Her husband keeps covering things up, keeping her away from doctors too."
    bree.say "And we figured out that it could only be because he's controlling Angela."
    bree.say "Because he's hypnotizing her!"
    show dwayne happy
    show dwayne at center, zoomAt (1.0, (640, 920)), startle(0.14,-20)
    pause 0.2
    show dwayne at center, zoomAt (1.0, (640, 920)), startle(0.14,-20)
    pause 0.2
    show dwayne at center, zoomAt (1.0, (640, 920)), startle(0.14,-20)
    "This time Dwayne actually laughs out loud."
    show dwayne happy at startle
    dwayne.say "Hah!"
    dwayne.say "What is this guy, a goddamn magician?!?"
    show dwayne smile
    "Without stopping to blink, I nod my head."
    bree.say "How did you guess?"
    bree.say "He was called Dylan Devant!"
    show dwayne happy
    dwayne.say "You're serious?"
    show dwayne shout
    dwayne.say "Wait..."
    dwayne.say "I think I heard of that guy."
    show dwayne annoyed
    bree.say "You might have..."
    bree.say "Or [mike.name] could have told you about him too."
    bree.say "After all, he is the guy's dad!"
    show dwayne therock
    "The moment the words are out of my mouth, I know that I screwed-up."
    show dwayne shout
    dwayne.say "The same [mike.name] that works for me?"
    dwayne.say "And if this Devant guy is your Angela's husband..."
    show dwayne happy
    dwayne.say "Then that means she's [mike.name]'s mom!"
    show dwayne at center, zoomAt (1.0, (640, 920)), startle(0.14,-20)
    pause 0.2
    show dwayne at center, zoomAt (1.0, (640, 920)), startle(0.14,-20)
    pause 0.2
    show dwayne at center, zoomAt (1.0, (640, 920)), startle(0.14,-20)
    "Dwayne can't contain his amusement, laughing out loud."
    dwayne.say "Oh, [hero.name]..."
    show dwayne shout
    dwayne.say "So let me get this straight in my head..."
    dwayne.say "You're sleeping with [mike.name]'s mom."
    dwayne.say "And you think his dad is hypnotising her too!"
    dwayne.say "On top of that, you want me to find the proof?"
    show dwayne normal
    bree.say "Erm..."
    bree.say "Yeah..."
    bree.say "That's about the size of it!"
    show dwayne happy at startle
    "Dwayne shakes his head, still chuckling to himself."
    if dwayne.love >= 100:
        show dwayne shout
        dwayne.say "You were right to come to me with this, [hero.name]."
        dwayne.say "I'm used to handling problems like this myself."
        show dwayne therock
        dwayne.say "And I know people that can make them just...disappear."
        show dwayne normal
        "That all sounds pretty intimidating."
        "But I do the best I can to look keen."
        bree.say "What we need is evidence, Dwayne."
        bree.say "Something that we can use to prove it all."
        "Dwayne nods again."
        show dwayne shout
        dwayne.say "Okay, [hero.name]..."
        dwayne.say "All we need to settle on is my fee."
        show dwayne normal
        "That stops me dead in my tracks."
        "And I end up staring at Dwayne in amazement."
        bree.say "You..."
        bree.say "You want money?"
        show dwayne shout
        dwayne.say "No, [hero.name]..."
        dwayne.say "I already have money."
        show dwayne happy
        dwayne.say "What I want is you!"
        show dwayne normal
        "I know that I should have seen this coming."
        "That Dwayne would only agree to help for such a price."
        "But I need this to happen, and if that's what it costs..."
        bree.say "Okay, Dwayne..."
        bree.say "Whatever you want."
        show dwayne smile
        "This time the smile that spreads across Dwayne's face is real."
        show dwayne happy
        dwayne.say "Consider it done."
        show dwayne smile
        "There doesn't seem to be anything more to say after that."
        scene bg breakroom with fade
        "And it's only when I leave Dwayne's office that reality starts to hit me."
        "I just agreed to give myself to him in return for help!"
        "Ah well, at least I have that over him."
        "If he doesn't deliver on his side of the bargain, then he gets nothing."
        "I just hope that, in the end, it's worth what I promised him."
        $ angela.flags.outside_help = "dwayne"
        $ angela.flags.angeladelay = TemporaryFlag(True, 3)
    else:
        show dwayne happy
        dwayne.say "Well, I've got to thank you, [hero.name]..."
        dwayne.say "That's the most amusing thing I've heard in a very long time."
        show dwayne normal
        "I sit there in silence, a nervous smile on my face."
        "Because I'm waiting for Dwayne to say more."
        show dwayne shout
        dwayne.say "What's the matter?"
        dwayne.say "Do you need it spelling out, [hero.name]?"
        show dwayne therock
        bree.say "Do I need what spelling out?"
        show dwayne shout
        dwayne.say "The meeting's over, [hero.name]."
        dwayne.say "It's time for you to leave."
        show dwayne annoyed
        "Almost without thinking, I stand up."
        "There's just something so commanding about Dwayne's tone."
        "But I manage to stop myself before I walk out of there at his behest."
        bree.say "But..."
        bree.say "But I came here for your help!"
        show dwayne shout
        dwayne.say "I can't help you, [hero.name]."
        dwayne.say "What you need is the police."
        show dwayne happy
        dwayne.say "Or maybe some kind of wizard-slaying hitman!"
        show dwayne annoyed
        "I open my mouth to protest."
        "But Dwayne's already turned his chair around to stare out of the window."
        "Which I take as a sign that the conversation is over."
        scene bg breakroom with fade
        "So it looks like I won't be getting any help from around here."
        $ angela.flags.outside_help = None
    $ game.room = "breakroom"
    $ hero.replace_activity(end_event=True)
    scene bg black with dissolve
    return

label angela_female_event_13f:
    "It's been a good few days since I went to see Dwayne and explained all of my problems to him."
    "And even though I figure that the help he offered me would take some time, I'm already getting twitchy."
    "I keep pulling out my phone and staring at it, sometimes even pulling up his number, a finger hovering over the screen."
    "But somehow I manage to fight the urge and keep on waiting, hoping that he'll be the one calling me instead."
    "I also find myself doing whatever I can to pass the time and keep my mind off the subject too."
    show play console sasha mcalone
    "I play on the Z-Box until I'm sick of every game that we have in the house."
    "I try reading, but everything I pick up doesn't seem to grip me enough."
    hide play console sasha mcalone
    show mike at left4
    show sasha at right4
    with fade
    "I even try spending time with [mike.name] and Sasha, hoping their problems will distract me from my own."
    "But in the end they both tell me, in the nicest way possible, to get the hell out of their hair."
    hide mike
    hide sasha
    show chibi tv as dylan_news
    with fade
    "So the only thing left for me to do is sit down in front of the TV and see if that can distract me."
    "It's weird, but these days I'm more likely to watch stuff on my phone or laptop."
    "So the act of watching the TV is kind of weird and old-fashioned!"
    "I flick through the channels, looking for something interesting to settle on."
    "At first I'm thinking that a movie or even a soap-opera might be what I need."
    "But then I happen upon one of the twenty-four hour news channels."
    "I'm about to move on when I see something that catches my eye."
    "It's a news report with a picture in the background that looks familiar."
    "So I lean forwards and listen to see what the hell it's all about."
    "Newsreader" "And in other news..."
    "Newsreader" "Many people might recall seeing the famous stage magician, Dylan Devant..."
    "Newsreader" "But the former star of stage and screen caused controversy yesterday."
    "It's only now that I recognise the picture as a poster of Angela's husband."
    "And as soon as I do, all of my attention is focussed on the screen."
    "Newsreader" "When it was revealed that he was bankrupt..."
    "Newsreader" "And later that he had actually fled the country!"
    "Newsreader" "Efforts are being made to obtain an extradition order..."
    "Newsreader" "But official sources are sceptical as to the likelihood of that being possible."
    "The newsreader says a few more words, but then moves on to the next story."
    hide chibi tv with dissolve
    "Which leaves me to collapse backwards onto the sofa, my mind blown."
    "If that's the truth of the matter, then Angela's finally safe from that man."
    "And that in turn means that we're also free to be together!"
    "I'm about to begin celebrating when something else occurs to me."
    "The newsreader said Dylan was bankrupt and fled the country."
    "And that's just how I'd have expected Dwayne to go after him."
    "Which means that I owe him big time!"
    "That and I'm going to have to visit him a second time."
    "So that we can discuss what kind of payment he expects for his help!"
    return

label angela_female_event_14b:
    "I thought that coming back to Dwayne's office for the second time would be easier than the first."
    "But if anything, it feels more of a challenge to be walking through those doors now than before."
    "My mood's been on what felt like a permanent high since Dylan upped and fled the country."
    "Because now I have so much to look forward to with Angela and nothing to get in the way of that."
    "Well, nothing save for the knowledge that I need to repay the debt that I owe to Dwayne."
    "But I keep on telling myself that it's only fair that I do this thing."
    "After all, he is the one that made sure I have a future with Angela."
    "So I can't go back on my word now, can I?"
    "I'm sure to put a smile on my face as I push the double doors open and walk into Dwayne's office."
    scene bg ceo with fade
    "But the effort is wasted on account of the fact that his chair is turned away from me."
    "He seems to be gazing out of the window at the impressive view of the city."
    "But I know him well enough to suspect that he's doing it more for show."
    bree.say "Hi, Dwayne..."
    bree.say "Thanks for finding the time to see me again."
    show dwayne at center, zoomAt(1.25, (640, 920)) with dissolve
    "My suspicions are all but confirmed as Dwayne spins around in his chair."
    "Then he leans forwards, resting his elbows on the desk."
    show dwayne happy
    dwayne.say "Hello, [hero.name]..."
    dwayne.say "And you should know by now, I'll always find time for you."
    dwayne.say "Because you come to me with such interesting problems."
    show dwayne normal
    "I nod my head, trying not to appear nervous."
    "And I take the chance to scurry across the floor to Dwayne's desk."
    "Normally I'd wait for him to offer me a seat, but today I'm far too on edge."
    "So I just sit myself down in the chair on my side of the desk instead."
    show dwayne at center, zoomAt(1.5, (640, 1080)) with fade
    "Luckily for me, this seems to be exactly what Dwayne wanted."
    "As he leans even closer to me, resting his chin on his steepled hands."
    show dwayne shout
    dwayne.say "I presume you've been watching the news?"
    dwayne.say "Keeping up to speed on the affairs of a certain person?"
    show dwayne normal
    "It's only in situations like this that I'm reminded of how large Dwayne actually is."
    "He's almost towering over me right now, even though we're both sitting down!"
    "And it feels like everything in his office is designed to enhance that impression too."
    bree.say "Y...yeah, I have."
    bree.say "I saw that he fled the country?"
    bree.say "Something about his financial affairs?"
    show dwayne smile
    "The smile that spreads across Dwayne's face betrays a whole host of different emotions at once."
    "There's the obvious pride he's feeling at being the one to solve my problems."
    "But also the desire to make it appear like what he did was really nothing so important to him."
    "And under all that, I can sense the anticipation he must be feeling at calling in the debt."
    show dwayne happy
    dwayne.say "It's such a shame that these celebrity types aren't more savvy in that area."
    dwayne.say "He might have been a magician on the stage, maybe one of the best."
    dwayne.say "But he certainly wasn't a wizard when it came to his accounts!"
    dwayne.say "All it took was a little poke here and a prod there..."
    dwayne.say "And it all came tumbling down around his ears."
    show dwayne smile
    "I'm nodding eagerly the whole time Dwayne's telling me this."
    "There might not be any specific details in there."
    "But maybe that's for the best, as the more I know the more I get drawn into the affair."
    bree.say "So that's all done and dusted then?"
    bree.say "There's no way he's going to be able to come back?"
    show dwayne normal
    "Dwayne disappoints me for a moment by shrugging."
    show dwayne shout
    dwayne.say "There's no guarantee he won't, [hero.name]."
    dwayne.say "But if he does, then he'll be in prison before he can take a breath."
    dwayne.say "If he's smart, and I believe that he is, then he'll never come back."
    show dwayne normal
    "Okay, so that's not the answer that I ideally wanted to hear."
    "But it's probably as close as I'm ever going to get to it."
    "Which leaves only the question of Dwayne's payment."
    bree.say "So..."
    bree.say "What do you want in return, Dwayne?"
    bree.say "What's your price?"
    show dwayne therock
    "Dwayne cocks his head one side as he studies me across the desk."
    "As if it's now his turn to be the one feeling a little disappointment."
    show dwayne shout
    dwayne.say "Now, [hero.name]..."
    dwayne.say "This isn't about services rendered and payments due!"
    dwayne.say "This is about friends doing favours for friends."
    dwayne.say "I dealt with Dylan Devant because of my enduring friendship with you."
    dwayne.say "And now you're doing something pleasant for me in the same manner."
    dwayne.say "So I think you know what kind of a gesture would be appropriate, don't you?"
    show dwayne normal
    "Urgh...I should have known Dwayne would pull something like this!"
    "He's not going to come out and ask me to have sex with him."
    "What he wants is for me to offer myself up to him on a platter."
    "That way it looks like he never even had to hint at it."
    "And the worst thing is that I don't have any choice but to play along."
    with fade
    "So I nod as I stand up and push back my chair."
    show bg ceo at center, traveling(2.0, 3.0, (0, 980))
    show dwayne zorder 1 at center, traveling(2.0, 3.0, (640, 1380))
    "Then I do my best to saunter around the side of the desk in a seductive manner."
    "Dwayne seems to be into it the moment that I start too."
    "Because he pushes his own chair backwards, though he remains seated."
    "And he turns to face me as I approach him around the desk."
    "I can see that there's now enough space for me to come between him and the desk."
    show bree b annoyed blush casual zorder 2 at flip, center, zoomAt(2.25, (440, 1140)) with easeinleft
    "So I walk into it, and then I turn my back to him."
    "This means that as I bend over, my ass is pushed into his face."
    "I spread my legs wide as I lower myself down, leaning on the desk."
    hide bree with dissolve
    "And then I make a point of hiking up my skirt so that my panties are visible."
    "I'm wondering how far Dwayne is going to let me go before he gets involved."
    "Because it would be just like him to keep me in suspense on a point like that."
    "To keep on sitting back and see just how far I'd go to entice him."
    "But a moment later I'm surprised as I hear his chair creak."
    show dwayne at center, traveling(2.0, 1.0, (940, 1080))
    "And then I feel his hands taking hold of me around the waist."
    "Which answers the question as to how long Dwayne's prepared to wait before claiming his prize!"
    "He doesn't say a word or wait for permission of any kind."
    "Not that I'd expect him to, as this isn't that sort of deal."
    "Instead I feel Dwayne slide his fingers into my panties and against my buttocks."
    "Then he pulls them down in one smooth motion, all the way to my knees."
    show sexinserts bottom bree zorder 1 at vflip, center, zoomAt(0.75, (0, 640)) with dissolve
    "I gasp as those hands don't retreat once my panties are down."
    "Instead they begin to explore the space between my legs."
    "Dwayne expertly teases me down there, stroking and caressing where it's softest."
    "There's no way that I can keep my mind on anything else, and I soon start to succumb."
    "But maybe that's the best way to do this thing, to surrender to my basest instincts?"
    "That way I can forget everything else and give myself over to Dwayne until it's over."
    "With that in mind, I reach down and hastily tug off my panties."
    "Then I kick them away and spread my legs wider still."
    "Dwayne seems to appreciate the gesture, and I hear the sound of his flies being unzipped."
    "I hastily get rid of my own clothes."
    hide sexinserts
    hide dwayne
    show bree threesome dwaynemike office at center, zoomAt(1.25, (640, 740))
    with fade
    "The mere thought of what's coming next makes me bite my lip in anticipation."
    show bree threesome dwaynemike dwayne with fade
    "Because I know that with Dwayne, bigger is better."
    "And down there it's no exception!"
    bree.say "Oh..."
    bree.say "Mmm..."
    bree.say "Oh fuck!"
    "I know it sounds like I'm playing the part that Dwayne expects of me."
    "Gasping and moaning as I feel the sensation of his cock between my thighs."
    "But believe me when I say that's not what's happening here."
    "Dwayne doesn't waste any time with foreplay or tease me before the event."
    "It feels like he knows exactly what he wants and how to go about getting it."
    "Plus the fact that his cock is hard and ram-rod straight."
    "So he doesn't need to spare a hand to guide it home either."
    show bree threesome dwaynemike at stepback(speed=0.1, h=-10, v=-20)
    "Instead he tightens his grip on my haunches and pulls me suddenly backwards."
    "At the same time he thrusts his own body forwards, pressing his cock hard against my pussy."
    "As ready as Dwayne seems to be for all of this, the same can't be said for me."
    "The head of his cock rubs up and down the length of my lips over and over again."
    "But to begin with, it stubbornly refuses to open to him."
    "It's not like I'm failing to feel pleasure at what he's doing either."
    "Already I can feel it pulsing through the rest of my body like an electric current."
    "Somehow my pussy is the last part of me to get with the program, refusing to the last."
    "But when the first chink in the armour appears, Dwayne leaps on it."
    show bree threesome dwaynemike dwayne vaginal
    "All of a sudden, I feel him sink into me by perhaps an inch."
    show bree threesome dwaynemike dwayne vaginal pleasure
    "And as soon as that happens, I lose all sense of myself in the moment."
    "The only thing I can think about is the sensation of him going ever deeper."
    "As he begins to fill me, I find myself nodding, almost begging him for more."
    "But then it's not like Dwayne needs any encouragement from me to do so."
    "Finally I feel him go as deep as he possibly can, and I'm totally filled."
    "Dwayne pauses, probably enjoying the sensation for himself."
    "As he does so, all I can do is pant and mouth silent words of helplessness."
    "I can't remember the last time a guy felt so big inside of me."
    "And I can't imagine feeling anything more sensational than this."
    show bree threesome dwaynemike at stepback(speed=0.1, h=-10, v=-20)
    pause 0.3
    show bree threesome dwaynemike at stepback(speed=0.1, h=-10, v=-20)
    "Well, that is until Dwayne starts to move inside me."
    "Then I feel those same sensations explode into so much more."
    "It doesn't take long for me to slumped over the desk, totally helpless."
    show bree threesome dwaynemike at stepback(speed=0.1, h=-10, v=-20)
    pause 0.3
    show bree threesome dwaynemike at stepback(speed=0.1, h=-10, v=-20)
    "I swear that Dwayne and his cock are all that's holding me up."
    "Because the feeling of him thrusting in and out of me turns my legs to rubber."
    hide bree threesome dwaynemike
    show dwayne grab cheeks at center, zoomAt(1.1, (640, 740))
    with hpunch
    dwayne.say "You like that...huh?"
    dwayne.say "You like being fucked like that?"
    show dwayne grab cheeks at stepback
    pause 0.3
    show dwayne grab cheeks at stepback
    bree.say "Uh...Uh..."
    show dwayne grab cheeks at stepback
    pause 0.3
    show dwayne grab cheeks at stepback
    bree.say "Y...yeah..."
    show dwayne grab cheeks at stepback
    pause 0.3
    show dwayne grab cheeks at stepback
    bree.say "I like it..."
    dwayne.say "That's right, [hero.name]..."
    show dwayne grab cheeks at stepback
    pause 0.3
    show dwayne grab cheeks at stepback
    dwayne.say "You get your...happy ending...with Angela..."
    show dwayne grab cheeks at stepback
    pause 0.3
    show dwayne grab cheeks at stepback
    dwayne.say "But you...walk off into the sunset...with the memory of my cock inside of you!"
    show dwayne grab cheeks at stepback
    pause 0.2
    show dwayne grab cheeks at stepback
    "I know what Dwayne's doing here, the way he's trying to fuck with my head."
    "But there's no way that I can muster even the smallest hint of rebellion."
    show dwayne grab cheeks at stepback
    pause 0.2
    show dwayne grab cheeks at stepback
    "It's like he's stripped me down to the most base, animalistic of my desires."
    "So all I can do is nod desperately, throwing my head up and down."
    show dwayne grab cheeks at stepback
    pause 0.2
    show dwayne grab cheeks at stepback
    "Not in the hope that doing so will make him stop."
    "But in the shameful hope that it will make him keep on going."
    show dwayne grab cheeks at stepback
    pause 0.2
    show dwayne grab cheeks at stepback
    bree.say "Yes..."
    bree.say "That's what I want..."
    show dwayne grab cheeks at stepback
    pause 0.2
    show dwayne grab cheeks at stepback
    bree.say "I want to feel you inside of me!"
    show dwayne grab cheeks at stepback
    pause 0.2
    show dwayne grab cheeks at stepback
    "That seems to be more than what Dwayne was hoping to hear out of me."
    "Because almost as soon as the words are out of my mouth, I feel a change in him."
    hide dwayne grab cheeks
    show bree threesome dwaynemike office dwayne vaginal pleasure at center, zoomAt(1.25, (640, 740))
    with hpunch
    "His grip tightens and he thrusts harder than ever before."
    "Then a moment later he lets go, shooting everything he has into me."
    show bree threesome dwaynemike office creampie with hpunch
    "There's no way that I can hope to resist, not after he's taken me so thoroughly."
    show bree threesome dwaynemike office vaginal ahegao with hpunch
    "I cum withing seconds, wailing and clawing at the desk, without any hope of escape."
    show bree threesome dwaynemike office outside with hpunch
    "Now that he's had his way with me, Dwayne pulls out with a grunt of satisfaction."
    scene bg ceo
    show dwayne at center, zoomAt(1.5, (640, 1080))
    with fade
    "I hear him zip up his flies and sit down in his chair."
    "But he makes no effort to help me out of my current predicament."
    "So I'm forced to simply lie there, totally exposed and helpless."
    "Eventually I find the strength to haul myself up and look for my discarded panties."
    "And every time I look in his direction, I see Dwayne watching me intently."
    show dwayne smile
    "He seems to be enjoying this almost as much as he did actually fucking me."
    "The fact that my cheeks are burning with shame probably only adds to his delight too."
    show dwayne at center, traveling(1.25, 0.3, (640, 920))
    "Once I feel like I'm halfway decent, I begin to walk towards the door."
    show dwayne happy
    dwayne.say "Good luck to you and Angela, [hero.name]..."
    dwayne.say "But if it doesn't work out, I'm always here for you."
    dwayne.say "Or hell, if you just find that you want some real cock..."
    dwayne.say "Just call me up and I'm sure that I can fit into you..."
    dwayne.say "Oops - I mean fit you in, obviously!"
    show dwayne smile
    "I nod as I let myself out of Dwayne's office, trying not to hang my head."
    scene bg breakroom with fade
    "But it's hard not to, as I can still feel the sensation of him inside me."
    "I keep telling myself that it'll fade, that this was all for Angela's sake."
    "And I'm sure that I'll come to believe that in time."
    "I just hope it happens sooner, rather than later."
    $ game.room = "breakroom"
    scene bg black with dissolve
    return


label angela_female_event_12d:
    "I kind of feel awkward asking Victor to meet me like this, as I have to be all mysterious over the phone."
    "I don't want to get into the details of the favour I have to ask him for fear of it freaking him out."
    "But of all the guys I know, he feels like the one that's best suited to handling this kind of thing."
    show victor normal at center, zoomAt(1.25, (540, 920)) with fade
    "And when we meet up, Victor doesn't help make the situation any less tense and weird."
    show victor paranoid at center, zoomAt(1.25, (520, 920)) with MoveTransition(0.1)
    "Because he's doing that strange thing he does where he's constantly looking over his shoulder."
    "Almost like he thinks someone is watching his every move."
    bree.say "Victor..."
    bree.say "Hey, Victor..."
    bree.say "I'm over here!"
    show victor surprised at center, zoomAt(1.25, (540, 920)) with MoveTransition(0.1)
    "Victor almost flinches as I raise my voice and wave to him."
    show victor upset at center, traveling(1.5, 0.2, (640, 1080))
    "And he hurries over to where I'm standing as quickly as he can."
    show victor shout
    victor.say "Ah..."
    victor.say "Okay, [hero.name], okay..."
    victor.say "No need for all the shouting and yelling!"
    show victor sadsmile
    bree.say "Oops!"
    bree.say "Sorry, Victor..."
    bree.say "It's just such a relief to see you."
    show victor paranoid
    "Victor nods, still glancing around as if looking for someone watching him."
    "Then he takes hold of my arm and urges me to move as he begins to stride off."
    show victor shout
    victor.say "Ah..."
    show victor joke
    victor.say "Let's talk as we walk, [hero.name]."
    victor.say "It's safer that way."
    show victor normal
    "Of course I'm a little weirded out by the idea."
    "But I'm desperate to get Victor's help in dealing with Angela's husband."
    "So I guess I'm just going to have to indulge his little eccentricities."
    "Though as soon as I fall in at his side and we're moving, I try to get straight to the point."
    bree.say "Victor..."
    bree.say "I'm sorry for being vague over the phone."
    bree.say "But this problem that I have..."
    bree.say "It's kind of...unusual!"
    show victor paranoid
    "Victor nods as I say all of this, still looking around in a paranoid manner."
    "But I can tell from the expression on his face that he's listening to every word."
    "It's like he's constantly multi-tasking inside of his head."
    "Which is pretty impressive for a guy!"
    show victor shout
    victor.say "Ah..."
    show victor joke
    victor.say "Yeah, [hero.name]..."
    victor.say "I'm kind of used to hearing that!"
    show victor shout
    victor.say "So, you want to tell me what the problem actually is?"
    show victor normal
    bree.say "Sure, Victor..."
    bree.say "It's my friend Angela, you see."
    bree.say "We started seeing each other behind her husband's back."
    bree.say "And everything seemed to be going well."
    bree.say "I was getting to know her, finding out about her past, all that stuff."
    bree.say "Then she just started forgetting things we'd done and that she'd told me."
    bree.say "That was bad enough, but then she began having these blackouts."
    bree.say "Waking up in places she couldn't remember going to."
    "Normally when I start telling this story to people, I know what the reaction will be."
    "They begin scoffing at the details, unable to believe I'm telling the truth."
    "But for some reason, Victor just seems to take it all at face value."
    "He nods all the time I'm describing the memory loss and blackouts."
    show victor shout
    victor.say "Ah..."
    show victor angry
    victor.say "Sounds like she's being drugged, [hero.name]."
    victor.say "That and maybe kidnapped too."
    show victor upset
    "I'm still kind of a little thrown by Victor's taking me at my word."
    "So I have to pause for a moment while I get my head back in order."
    bree.say "Not drugged, Victor..."
    bree.say "Hypnotised!"
    show victor surprised at startle
    "For the first time since we started discussing the matter, Victor looks surprised."
    "And for a second I'm worried that I've finally reached the limits of his credulity."
    "But then he frowns, like he's really considering the idea."
    victor.say "Ah..."
    victor.say "Hypnotised, huh?"
    show victor sadsmile
    victor.say "It's been a while since I dealt with something like that!"
    show victor upset
    "I could spend some more time explaining the finer details to Victor."
    "But the simple fact that he seems to believe me spurs me on."
    bree.say "It's her husband, Victor."
    bree.say "He's a famous stage magician."
    bree.say "Or at least he used to be."
    bree.say "I'm sure he's using his hypnotic powers to keep Angela prisoner."
    bree.say "And I need someone to find the evidence to prove it."
    show victor shout
    victor.say "Ah..."
    victor.say "And that's where I come in?"
    show victor normal
    bree.say "Yes, Victor..."
    bree.say "Will you help me take care of this?"
    bree.say "Will you help me to set Angela free?"

    if victor.love >= 20:
        "Victor nods his head, a grim look on his face."
        show victor shout
        victor.say "Ah..."
        show victor joke
        victor.say "I can take care of this guy, [hero.name]..."
        show victor happy
        victor.say "No problem with that."
        show victor normal
        "I feel a smile spreading across my face as Victor gives me his answer."
        "In fact it's all that I can do to keep from clapping my hands with glee."
        bree.say "That's great, Victor!"
        bree.say "So you'll do it?"
        bree.say "You'll help me?"
        show victor shout
        victor.say "Ah..."
        victor.say "Are you sure about this, [hero.name]?"
        victor.say "Because once I do this thing, there's no taking it back!"
        show victor upset
        "I have to admit that I'm a little puzzled by Victor's question."
        "I thought that I already made it clear I was one hundred percent for him doing this."
        "So I kind of do the best I can to push the seriousness of what he's saying aside."
        "Because I'm not going to be put off now that I'm so close to achieving my goal."
        bree.say "I know all of that, Victor."
        bree.say "And I already told you I'm fine with it."
        bree.say "So please, help Angela and me out?!?"
        bree.say "Don't make me beg you!"
        "Victor still has that same grim look on his face."
        "He gives me a single nod, quick and silent."
        show victor shout
        victor.say "Ah..."
        victor.say "Leave it with me, [hero.name]..."
        victor.say "You'll know when it's done."
        hide victor paranoid with easeoutleft
        "With that, Victor turns on his heel and strides away."
        "He looks like he's all ready to get down to business."
        "So I guess all I can do is wait for the results."
        $ angela.flags.outside_help = "victor"
        $ angela.flags.angeladelay = TemporaryFlag(True, 3)
    else:
        "Much to my surprise, Victor shakes his head."
        show victor shout
        victor.say "Ah..."
        show victor sadsmile
        victor.say "This doesn't sound like my kind of thing, [hero.name]."
        show victor sad
        "I'm already shaking my head."
        "I had so much hope pinned on getting Victor's help."
        "And I won't give it up without a fight."
        bree.say "But you're so good at solving problems, Victor!"
        bree.say "This is just one guy..."
        bree.say "Surely you can handle a retired magician?"
        show victor shout
        victor.say "Ah..."
        victor.say "You've got to understand, [hero.name]..."
        victor.say "This job doesn't fit my skill-set."
        show victor sadsmile
        victor.say "You should maybe call the cops?"
        show victor sad
        bree.say "I already tried that, Victor!"
        show victor shout
        victor.say "Then I dunno, [hero.name]..."
        victor.say "Maybe call some other cops?"
        show victor annoyed
        "I want to keep on arguing my case with Victor."
        "But I get the feeling that he's done discussing it."
        "So I let the matter drop for now, leaving it well alone."
        hide victor with fade
        "Maybe I'll get the chance to bring it up again at a more opportune time."
        "Or maybe I can think of someone else that could offer me the help I need."
        scene bg street with fade
        $ angela.flags.outside_help = None
    $ game.room = "street"
    $ hero.replace_activity(end_event=True)
    scene bg black with dissolve
    return

label angela_female_event_13g:
    "It's been a good few days since I met up with Victor and explained all of my problems to him."
    "And even though I figure that the help he offered me would take some time, I'm already getting twitchy."
    "I keep pulling out my phone and staring at it, sometimes even pulling up his number, a finger hovering over the screen."
    "But somehow I manage to fight the urge and keep on waiting, hoping that he'll be the one calling me instead."
    "I also find myself doing whatever I can to pass the time and keep my mind off the subject too."
    show play console sasha mcalone
    "I play on the Z-Box until I'm sick of every game that we have in the house."
    "I try reading, but everything I pick up doesn't seem to grip me enough."
    hide play console sasha mcalone
    show mike at left4
    show sasha at right4
    with fade
    "I even try spending time with [mike.name] and Sasha, hoping their problems will distract me from my own."
    "But in the end they both tell me, in the nicest way possible, to get the hell out of their hair."
    hide mike
    hide sasha
    show chibi tv as dylan_news
    with fade
    "So the only thing left for me to do is sit down in front of the TV and see if that can distract me."
    "It's weird, but these days I'm more likely to watch stuff on my phone or laptop."
    "So the act of watching the TV is kind of weird and old-fashioned!"
    "I flick through the channels, looking for something interesting to settle on."
    "At first I'm thinking that a movie or even a soap-opera might be what I need."
    "But then I happen upon one of the twenty-four hour news channels."
    "I'm about to move on when I see something that catches my eye."
    "It's a news report with a picture in the background that looks familiar."
    "So I lean forwards and listen to see what the hell it's all about."
    "Newsreader" "And in other news..."
    "Newsreader" "Many people might recall seeing the famous stage magician, Dylan Devant..."
    "Newsreader" "But the former star of stage and screen was found dead yesterday."
    "It's only now that I recognise the picture as a poster of Angela's husband."
    "And as soon as I do, all of my attention is focussed on the screen."
    "Did I actually hear that right?"
    "They found him dead?!?"
    "Newsreader" "Devant's body was discovered in his home..."
    "Newsreader" "And a police spokesperson confirmed that he died of a gunshot wound."
    "Newsreader" "But the same spokesperson refused to confirm rumours that it was a suicide."
    "Newsreader" "Though unofficial sources have speculated that Devant shot himself in the back..."
    "The newsreader says a few more words, but then moves on to the next story."
    hide chibi tv with dissolve
    "Which leaves me to collapse backwards onto the sofa, my mind blown."
    "If that's the truth of the matter, then Angela's finally safe from that man."
    "And that in turn means that we're also free to be together!"
    "I'm about to begin celebrating when something else occurs to me."
    "The newsreader said Dylan was supposed to have shot himself in the back?!?"
    "How in the hell is he supposed to have managed that?"
    "Ah well, I guess there must have been an accident or something."
    "And I'm sure that Vincent will explain everything to me when I see him next."
    "Which I guess will be sooner, rather than later."
    "Because I really want to thank him in person."
    return

label angela_female_event_14c:
    scene expression f"bg {game.room}" with fade
    "I'm filled with conflicting emotions as I hurry to meet Victor."
    "On the one hand, I'm delighted that Angela's problems have been solved."
    "That and the fact we should now be able to live our lives together in peace."
    "But on the other, I'm aware of just how much Victor's done for me."
    "I have no idea just what his taking care of Dylan might have involved."
    "Though it must have been pretty dangerous, because the guy ended up dead!"
    scene bg alley with fade
    "So I'm feeling an intense sense of guilt as I arrive at the alleyway."
    "Yeah, yeah...I know."
    "It's a weird place to meet, and a pretty sketchy one too."
    "But I'm guessing that Victor needs to keep a low profile right now."
    "Anyway, it seems like I'm the first one here, as there's no sign of him."
    "So I step a little way back into the shadows so as not to be seen."
    "And I prepare myself to wait for Victor's arrival."
    victor.say "Ah..."
    victor.say "Hey, [hero.name]..."
    "Even though the voice that's suddenly in my ear is familiar, that doesn't help."
    "I still let out a shriek of alarm and jump back out of the shadows and into the light."
    with vpunch
    bree.say "AAARGH!"
    bree.say "What the fuck?!?"
    "My heart is still hammering in my chest as the figure follows me out of the shadows."
    show victor paranoid at center, zoomAt(1.5, (640, 1080)) with easeinright
    "But to my immense relief, I see that it was actually Victor in there with me."
    show victor sadsmile
    victor.say "Oops..."
    victor.say "Sorry, [hero.name]..."
    victor.say "Sneaking up on people like that is kind of a habit!"
    show victor normal
    "Like I already said, I'm relieved that it's Victor."
    "But that doesn't mean I'm okay with what he just did."
    bree.say "Well it's a bad one, Victor..."
    bree.say "The kind of habit you should really break!"
    "Almost as soon as the words are out of my mouth, I find myself regretting them."
    "Because after all, I'm supposed to be here to thank Victor for all he's done."
    "So maybe him making me jump like that wasn't as big of a deal as I made it out to be."
    bree.say "Okay..."
    bree.say "I'm sorry, Victor."
    bree.say "I've just been through a lot recently."
    bree.say "But that was no reason to bite your head off."
    "Victor does that kind of nodding and shrugging thing of his."
    "When he seems to be both agreeing with you and letting you off the hook at the same time."
    show victor shout
    victor.say "Ah..."
    show victor joke
    victor.say "No hard feelings, [hero.name]..."
    show victor sadsmile
    victor.say "I know what that's like, trust me!"
    show victor normal
    "Now I'm the one nodding, as I put a smile on my face."
    bree.say "Sure, Victor, sure..."
    bree.say "I just wanted to say thank you, obviously."
    bree.say "I saw what happened to Dylan on the news."
    bree.say "Of course, him shooting himself couldn't have had anything to do with you."
    bree.say "That must have been something he did after you talked to him, right?"
    "I notice that Victor looks around as I say all of this."
    "And if I didn't know better, I'd swear he looks a little guilty."
    show victor shout
    victor.say "Ah..."
    victor.say "Yeah, [hero.name]..."
    victor.say "Pretty weird how he managed to shoot himself in the back like that!"
    victor.say "But let's not talk about dead guys, shall we?"
    victor.say "Does this mean you an Angela are safe now?"
    show victor normal
    "I feel a strange mix of emotions as Victor brings up Angela's name."
    "There's the familiar surge of affection that she always inspires in me."
    "But at the same time I'm feeling a deep sense of gratitude to Victor."
    "That and something else...something deeper."
    bree.say "Yeah, Victor..."
    bree.say "I think that just about wraps things up."
    bree.say "Apart from things between me and you."
    bree.say "I mean, we haven't even talked about how I'm going to repay you!"
    "Victor waves a hand in the air, dismissing the idea just like that."
    show victor shout
    victor.say "Ah..."
    show victor joke
    victor.say "I'd never ask for money from you, [hero.name]."
    victor.say "I see you as a friend, not a client."
    show victor happy
    "Victor has a wan smile on his face as he says all of this."
    "And I can feel my heart beginning to ache a little for him."
    "After all, this guy just went all out for me."
    "He may even have gotten involved in something pretty heavy."
    "There has to be some kind of way that I can show him how much that means to me."
    show victor at center, traveling(2.0, 1.0, (640, 1380))
    "Almost without thinking, I reach out and take hold of Victor's hand."
    show victor surprised
    "He looks at me in surprise, but doesn't pull away."
    show victor at dark with dissolve
    "And he doesn't resist as I pull him back into the shadows of the alleyway either."
    show victor shout
    victor.say "Ah..."
    victor.say "[hero.name]..."
    victor.say "What are you doing?"
    show victor normal
    "This time I put a single finger to Victor's lips."
    "And when I take it away, I place my own lips in it's place."
    hide victor
    show victor kiss at center, dark
    with fade
    $ victor.flags.kiss += 1
    "Victor's surprise melts away as we share a kiss."
    "At first it's pretty tame, but the mood soon changes."
    "And as the kiss becomes more intense, I feel Victor wrapping his arms around me."
    "Pretty soon he gets the message about what's happening here, and he can't hold back."
    "I almost break the kiss as I feel Victor lift me off my feet."
    show camila_stand_bg_alley as bg zorder 1 at flip
    show victor kiss zorder 2 at flip, center, zoomAt(1.1, (640, 740)), dark with hpunch
    "Then he turns around and presses me against the wall."
    "This means that I have to wrap my legs around him and cling on with my arms too."
    "Which is pretty awkward right now, as I'm also trying to reach his flies!"
    "Somehow we manage to grope and grasp until things begin to work."
    "I have Victor's manhood out of his pants and he's pulling down my underwear."
    show victor kiss naked with fade
    "What follows isn't exactly a picture of romantic fulfilment."
    "Instead it's kind of a desperate act between two confused and conflicted individuals."
    "All I know is that I can feel the hunger building inside of me for him."
    "And in the moment, this seems to be the perfect way in which to pay Victor back."
    scene bg black
    show victor standing alley
    with fade
    "I cling on even tighter as I begin to feel the head of his cock down below."
    "Victor's strength seems to be more than up to the task of supporting me."
    "So I'm able to savour the sensation of sinking down and onto him."
    "My own body seems to want this as much as his."
    "And there's only the smallest amount of resistance before it happens."
    show victor standing vaginal at stepback(speed=0.1, h=-10, v=-20)
    "My lips part, allowing him a little way inside."
    "Which is all that Victor needs to make his next move."
    show victor standing pleasure at stepback(speed=0.1, h=-10, v=-20)
    "I gasp in sheer amazement as he pulls me down even harder."
    show victor standing at stepback(speed=0.1, h=-10, v=-20)
    "At the same time, Victor thrusts upwards, driving himself almost the whole way inside."
    "All the time I'm nodding and murmuring things that aren't quite words."
    "Because the feelings that are flooding my senses are just too intense."
    show victor standing up at stepback(speed=0.1, h=-10, v=-20)
    "The only choice I have is to hold on tight and enjoy the ride."
    "From that point on, I feel like Victor is the one in total control."
    show victor standing at stepback(speed=0.1, h=-10, v=-20)
    "He isn't making love to me."
    show victor standing down at stepback(speed=0.1, h=-10, v=-20)
    "He's fucking me with an almost desperate passion."
    show victor standing at stepback(speed=0.1, h=-10, v=-20)
    "His movements come in explosive bursts of energy."
    "And this means that I'm sure he's going to peak any second."
    show victor standing at stepback(speed=0.1, h=-10, v=-20)
    "Yet somehow he doesn't, his stamina keeping things going."
    "By the time I sense the first hints of him reaching his climax, I'm totally helpless."
    show victor standing at stepback(speed=0.1, h=-10, v=-20)
    "Victor makes one last thrust, flattening me against the wall."
    with vpunch
    "And then I feel him explode inside of me, and I cum at the same moment."
    show victor standing alley creampie up ahegao
    with vpunch
    "How could I not?"
    with vpunch
    "He's already totally overwhelmed me."
    "So I'm swept along with him."
    "Utterly spent, Victor still manages to lower me gently to the ground."
    scene bg alley
    show victor at center, zoomAt(2.0, (640, 1380))
    with fade
    "And we both seem to be standing on shaky legs as we make ourselves decent."
    show victor shout
    victor.say "Ah..."
    show victor joke
    victor.say "I don't know what to say!"
    show victor normal
    bree.say "Then don't say anything, Victor."
    bree.say "Let's just keep this between us, okay?"
    "Victor nods in agreement, then turns on his heel."
    show victor at center, traveling(1.5, 1.0, (640, 1080))
    "He gives me a brief wave as he walks away."
    hide victor with easeoutleft
    "And I return it, watching him disappear into the shadows."
    "I can't help shaking my head, wondering where he could be going."
    "But then I guess that's just the kind of guy he is."
    "Mysterious and moving in the shadows, like a phantom in the night."
    "I'm just lucky I could call on him in my time of need."
    $ victor.sexperience += 1
    return


label angela_female_event_12e:
    "The last thing that I generally want to do when it comes to a problem is involve someone like Danny."
    "Especially when it's a problem as personal and sensitive as the one that Angela and I are facing right now."
    "But there simply doesn't seem to be an alternative, as I don't know of anyone else that can help me."
    "So before asking for help, I steel myself for what lies ahead."
    show danny normal at center, zoomAt(1.25, (640, 920)) with fade
    "And as soon as I lay eyes on him, I can see that Danny's weighed the situation up."
    "From the knowing look on his face, he's more than sure that I'm coming to him in my time of need."
    "And there's no way that Danny's going to miss the opportunity to wallow in it."
    show danny shout at center, traveling(1.5, 0.3, (640, 1080))
    danny.say "Hey there, [hero.name]..."
    danny.say "Long time no see, yeah?"
    show danny normal
    bree.say "Urgh..."
    bree.say "Yeah, Danny..."
    bree.say "Not long enough, if you ask me!"
    show danny annoyed
    danny.say "Huh?"
    danny.say "What was that?"
    show danny annoyed
    bree.say "I said, some people are worth waiting to see."
    show danny shout
    danny.say "Oh..."
    danny.say "Okay..."
    show danny normal
    "Danny seems to recover from his momentary confusion pretty quickly."
    show danny smile
    "And the lascivious grin soon spreads over his face once again."
    show danny sneaky
    danny.say "So..."
    danny.say "I'm guessing you've got a problem, [hero.name]?"
    danny.say "One that you want Danny here to solve?"
    show danny smile
    "I do the best I can to put a smile on my face too."
    "As well as ignoring the slimy overtones Danny puts into every word."
    bree.say "That's very insightful of you, Danny."
    bree.say "I do indeed have a problem."
    bree.say "And I'm also hoping you can provide me with a solution."
    "Danny nods happily, still loving being in the driving seat."
    show danny sneaky
    danny.say "So what are you waiting for?"
    danny.say "Spill the beans!"
    show danny smile
    bree.say "Okay, Danny..."
    bree.say "Here goes..."
    bree.say "I've been seeing a woman called Angela."
    show danny joke
    "At the mere mention of Angela's name, Danny's grin becomes wider still."
    show danny sneaky
    danny.say "So this is a girl-on-girl thing?"
    danny.say "Alright!"
    show danny smile
    bree.say "Yeah, Danny..."
    bree.say "My sentiments exactly..."
    bree.say "Anyway, Angela's still technically married to her husband."
    bree.say "And she was well on her way to leaving him too."
    bree.say "But then she started having these blackouts and losing her memory."
    show danny normal
    "Danny actually seems to be listening now, taking it all in."
    "He strokes his chin and nods."
    show danny shout
    danny.say "Huh..."
    danny.say "Sounds like he's drugging this chick."
    danny.say "Her old man, I mean."
    show danny annoyed
    "I shake my head, dismissing the idea."
    bree.say "Uh-uh..."
    bree.say "She had tests done at the hospital."
    bree.say "And the results were negative - no drugs in her system."
    show danny angry
    danny.say "Then how in the hell did he do it?"
    show danny upset
    bree.say "Hypnotism!"
    show danny surprised
    "Danny stares at me with an incredulous look in his eyes."
    show danny scared
    danny.say "What?!?"
    danny.say "You mean like putting people in trances?"
    danny.say "Making them think they're chickens and all that shit?!?"
    show danny surprised
    bree.say "Exactly that, Danny!"
    bree.say "Her husband used to be Dylan Devant, a stage magician."
    bree.say "And hypnosis was part of his act!"
    show danny psycho
    "Danny's nodding slowly by now."
    "Like he's accepting all the crazier parts of the story."
    show danny shout
    danny.say "So, [hero.name]..."
    danny.say "Whaddya want me to do to this magician prick?"
    show danny sneaky fist
    danny.say "Break his wand as well as both his legs?"
    show danny psycho
    bree.say "I need proof, Danny - proof that he's been doing those things to Angela."
    "Danny's still nodding his head when I finish what I have to say."
    "And so I wait with baited breath to see what his answer will be."

    if danny.love >= 60:
        show danny shout
        danny.say "Sure thing, [hero.name]..."
        danny.say "I reckon I can handle this magician fuck."
        show danny psycho -fist
        "I feel a sudden and almost overwhelming surge of relief."
        "And in my gratitude, I can't help throwing myself at Danny."
        bree.say "Oh, thank you!"
        bree.say "I'll make sure you don't regret this, Danny."
        show danny shout
        danny.say "You'll do better than that, [hero.name]."
        show danny sneaky
        danny.say "You'll help me out with a little problem of my own first."
        show danny psycho
        "I take an unconscious step backwards."
        "Already wondering what Danny can be talking about."
        bree.say "A problem?"
        show danny shout
        danny.say "Yeah, [hero.name]..."
        danny.say "I got this deal going down in a couple of minutes."
        danny.say "And the customer's a real pain in the ass."
        danny.say "I got his shit, but I just know he's gonna need something more."
        show danny sneaky
        danny.say "A little something to sweeten the deal, if you know what I mean?"
        show danny psycho
        "To be honest, I can guess what Danny means."
        "But I want to hear it from his own lips."
        "Just in case we're not on the same page."
        bree.say "No, Danny, I don't."
        bree.say "You care to enlighten me?"
        show danny shout
        danny.say "Nothing big or heavy, [hero.name]."
        danny.say "Just suck him off to seal the deal."
        danny.say "If you think you can handle that?"
        show danny psycho
        menu:
            "I'll do it" if hero.morality <= -25:
                "I don't hesitate to nod my head."
                "Sure, it sounds degrading."
                "And it's probably going to be dangerous too."
                "But what real choice to I have?"
                "I need Danny's help to get this problem sorted."
                "So I'll do anything I have to in order to make that happen."
                bree.say "Okay, Danny, you've got a deal."
                bree.say "Lead the way."
                show danny sneaky
                danny.say "Good girl, [hero.name]..."
                danny.say "I knew you'd understand how these things work."
                show danny psycho at center, zoomAt(1.5, (540, 1080)) with ease
                "Danny gestures for me to follow him."
                show danny at center, zoomAt(1.5, (340, 1080)) with ease
                "Then he turns and leads the way into a dark alley."
                scene bg alley with fade
                "Because of course the deal can't take place anywhere nice or even in plain daylight!"
                "But I already agreed to do this thing, so I keep my thoughts to myself."
                "When we reach a part of the alley that looks just like any other to me, Danny holds up a hand."
                "He doesn't need to explain to me that this means I should stay back, as I can already see someone up ahead."
                "The figure is standing in a gloomy doorway so I can't make out his face, only really the lower half of his body."
                show ryan casual angry at center, zoomAt(1.25, (340, 920)), blacker
                show danny at center, zoomAt(1.25, (640, 920))
                with dissolve
                "Danny walks over to him, and they begin to speak in hushed tones, so I can't hear a word."
                "But I can see them gesturing, first the guy at me, and then Danny to the other guy's crotch."
                "After this I can almost feel the guy staring at me, and I swear I see his body move as he nods."
                "Danny turns to face me, waving with his hand to beckon me over."
                "So I steel myself and do as he asks."
                "Once I make it over there, the guy doesn't make a move to come out of the shadows."
                "That suits me fine, as I just kneel down and reach out for his flies."
                show breemc bj mugger with fade
                "What follows is one of the least enjoyable blow-jobs I've ever had the misfortune to give."
                show breemc bj tip
                pause .25
                show breemc bj base
                pause .25
                show breemc bj tip
                pause .25
                show breemc bj base
                pause .25
                show breemc bj tip
                pause .25
                show breemc bj base
                "The guy is pretty much average in every possible measure, and it doesn't take me long to get him hard."
                show breemc bj blowjob
                "But I only do the barest minimum required of me to make the thing happen."
                show breemc bj medium
                pause .25
                show breemc bj small
                pause .25
                show breemc bj medium
                pause .25
                show breemc bj small
                pause .25
                show breemc bj medium
                pause .25
                show breemc bj small
                "The guy must have been pretty excited at the prospect of it too."
                "Because I feel like he's only been in my mouth for a few minutes when it happens."
                show breemc bj medium
                pause .25
                show breemc bj small
                pause .25
                show breemc bj medium
                pause .25
                show breemc bj small
                pause .25
                show breemc bj medium
                pause .25
                show breemc bj small
                "He lets out a grunt, and then I feel him shiver from head to toe."
                show breemc bj handjob base
                "That gives me enough warning to pull back my head, sliding his cock out of my mouth."
                show breemc bj handjob cum with hpunch
                "And then I let him shoot his load into my face."
                show breemc bj handjob -cum facecum with hpunch
                "As soon as it's done, I get to my feet and walk to the end of the alley."
                scene bg alley with fade
                show ryan casual angry at center, zoomAt(1.25, (440, 920)), blacker
                show danny at center, zoomAt(1.25, (840, 920))
                "And I wait there until Danny wraps up his business with the guy."
                hide ryan
                show danny sneaky at center, zoomAt(1.25, (640, 920))
                with easeoutleft
                danny.say "Thanks, [hero.name]..."
                danny.say "You just made me one very happy customer!"
                show danny smile
                bree.say "So that's my side of the bargain done, right?"
                bree.say "Now you'll take care of yours?"
                show danny sneaky
                danny.say "Sure thing, [hero.name]..."
                danny.say "Consider it done!"
                $ hero.morality -= 1
                $ angela.flags.outside_help = "danny"
                $ angela.flags.angeladelay = TemporaryFlag(True, 3)
            "No way !":
                "I don't hesitate to shake my head."
                "Sure, I need Danny's help."
                "But I don't need it bad enough to get mixed up in his dealing drugs!"
                bree.say "No way, Danny."
                bree.say "I'm not turning tricks for you!"
                show danny annoyed
                "Danny shrugs and shakes his head."
                "But I can see that the disappointment on his face is feigned."
                "He's clearly enjoying the chance to turn me down for not meeting his terms."
                show danny shout
                danny.say "That's a damn shame, [hero.name]."
                danny.say "Because that means the deal's off."
                show danny annoyed at center, zoomAt(1.5, (540, 1080)) with ease
                "He turns on his heel and starts to walk away."
                show danny at center, zoomAt(1.5, (340, 1080)) with ease
                "Though he keeps his pace slow enough for me to be able to catch up, should I change my mind."
                hide danny with easeoutleft
                "But I'm determined to stick to my answer, not to cave into the pressure he's putting me under."
                "If Danny won't help me without the chance to exploit me, then I'll find someone else who will."
                $ angela.flags.outside_help = None
    else:
        show danny shout -fist
        danny.say "Nah, [hero.name]..."
        danny.say "I don't think I'm the guy you want on this one."
        show danny annoyed
        "I shake my head, unable to believe what I'm hearing."
        bree.say "You can't be serious, Danny?"
        bree.say "I thought you weren't afraid of anything?"
        show danny shout
        danny.say "Not being afraid of anything is dumb, [hero.name]."
        danny.say "But one thing I am is smart."
        show danny angry -fist
        danny.say "Smart enough to know this all sounds bad."
        danny.say "I aint messing with no magician, retired or otherwise!"
        show danny annoyed -fist at center, zoomAt(1.5, (540, 1080)) with ease
        "Danny turns to start walking away."
        "But I follow him, beginning to get desperate."
        bree.say "What do you want, Danny?"
        bree.say "Money?"
        bree.say "Drugs?"
        bree.say "Sex?!?"
        show danny smile at center, zoomAt(1.5, (340, 1080)) with ease
        "Danny chuckles and keeps right on walking away."
        show danny sneaky
        danny.say "I can get all of those things whenever I want."
        danny.say "And I don't got to mess with anyone magical to get them either."
        danny.say "Go call the cops, [hero.name] - aren't they supposed to handle this kind of stuff?"
        hide danny with easeoutleft
        "With that, Danny walks away, leaving me to ponder my next move."
        $ angela.flags.outside_help = None
    $ game.room = "street"
    $ hero.replace_activity(end_event=True)
    scene bg black with dissolve
    return

label angela_female_event_13h:
    "It's been a good few days since I met up with Danny and begged him to help me with all of my problems."
    "And even though I figure that the help he offered me would take some time, I'm already getting twitchy."
    "I keep pulling out my phone and staring at it, sometimes even pulling up his number, a finger hovering over the screen."
    "But somehow I manage to fight the urge and keep on waiting, hoping that he'll be the one calling me instead."
    "I also find myself doing whatever I can to pass the time and keep my mind off the subject too."
    show play console sasha mcalone
    "I play on the Z-Box until I'm sick of every game that we have in the house."
    "I try reading, but everything I pick up doesn't seem to grip me enough."
    hide play console sasha mcalone
    show mike at left
    show sasha at right
    "I even try spending time with [mike.name] and Sasha, hoping their problems will distract me from my own."
    "But in the end they both tell me, in the nicest way possible, to get the hell out of their hair."
    hide mike
    hide sasha
    show chibi tv as dylan_news
    with fade
    "So the only thing left for me to do is sit down in front of the TV and see if that can distract me."
    "It's weird, but these days I'm more likely to watch stuff on my phone or laptop."
    "So the act of watching the TV is kind of weird and old-fashioned!"
    "I flick through the channels, looking for something interesting to settle on."
    "At first I'm thinking that a movie or even a soap-opera might be what I need."
    "But then I happen upon one of the twenty-four hour news channels."
    "I'm about to move on when I see something that catches my eye."
    "It's a news report with a picture in the background that looks familiar."
    "So I lean forwards and listen to see what the hell it's all about."
    "Newsreader" "And in other news..."
    "Newsreader" "Many people might recall seeing the famous stage magician, Dylan Devant..."
    "Newsreader" "But the former star of stage and screen was found dead yesterday."
    "It's only now that I recognise the picture as a poster of Angela's husband."
    "And as soon as I do, all of my attention is focussed on the screen."
    "Did I actually hear that right?"
    "They found him dead?!?"
    "Newsreader" "Devant's body was discovered in his home..."
    "Newsreader" "And a police spokesperson confirmed that drug paraphernalia was found at the scene."
    "Newsreader" "But the same spokesperson refused to confirm rumours that it was a case of an accidental overdose."
    "Newsreader" "Though unofficial sources have speculated that Devant was known to have had a cocaine habit..."
    "The newsreader says a few more words, but then moves on to the next story."
    hide chibi tv with dissolve
    "Which leaves me to collapse backwards onto the sofa, my mind blown."
    "If that's the truth of the matter, then Angela's finally safe from that man."
    "And that in turn means that we're also free to be together!"
    "I'm about to begin celebrating when something else occurs to me."
    "The newsreader said Dylan was supposed to have taken an overdose?!?"
    "Wow...I had no idea he was into stuff like that!"
    "Ah well, I guess there must have been an accident or something."
    "And I'm sure that Danny will explain everything to me when I see him next."
    "Which I guess will be sooner, rather than later."
    "Because I really want to thank him in person."
    "And then there's going to be the matter of what he'll ask for in payment."
    "Which I guess won't be something small or insignificant."
    return

label angela_female_event_14d:
    "I feel like I've been on a kind of high since I heard the news of Dylan's death."
    "Because now that he's gone, there's nothing to keep Angela and me from living our lives."
    "Well, apart from the small matter of me thanking Danny for the hand he had in all of that."
    "And of course, the issue of exactly what he's going to ask for in return for his help."
    "So it's with that in mind I make my way to the alleyway where he wanted to meet me."
    "And I do the best that I can to ensure that I look confident as I wait for him to turn up."
    danny.say "Hey, there, sweet-cheeks…"
    danny.say "How's it hanging?"
    play sound spank
    with hpunch
    "Danny punctuates this greeting by slapping me hard on the ass."
    "The shock of which makes me cry out and jump up into the air."
    with hpunch
    bree.say "Argh!"
    show danny smile at center, zoomAt(1.25, (640, 920)) with easeinleft
    bree.say "Ooh..."
    bree.say "Dammit, Danny!"
    "All my alarm and cursing gets me from Danny is a particularly filthy laugh."
    "But then what else should I have expected from a guy with his reputation?"
    show danny sneaky
    danny.say "Ah, lighten up, [hero.name]..."
    danny.say "After all, you're in the clear now, right?"
    danny.say "Your guardian angel here swooped in and made all your problems disappear."
    "Danny's grinning at me the whole time he's saying this."
    "One of those hungry, knowing grins that he gets at times like this."
    "Specifically times when he knows that he's owed something juicy."
    "And he has the opportunity to collect on the debt at his leisure."
    bree.say "Yeah, Danny..."
    bree.say "About that..."
    bree.say "I guess Dylan must have overdosed or something?"
    bree.say "You know, after you gave him all of those drugs?"
    show danny psycho
    "Now the subject's changed to Dylan, Danny's watching me more intensely than before."
    "And I can see that the look in his eyes is becoming that much more predatory in nature."
    "I guess that's understandable, as this is the most dangerous part of our business today."
    "Ideally I don't want to know the gruesome details of what went down when confronted Dylan."
    "Only that he did and the matter's closed."
    "But I also know that's part of what's going to cost me so dearly here and now."
    "I've asked Danny to take a massive risk for my sake, and now I have to pay the price."
    show danny sneaky
    danny.say "Yeah, [hero.name]..."
    danny.say "Something like that."
    danny.say "These celebrity types are pretty flaky at the best of times."
    danny.say "None of them really know their limits, what they can handle."
    show danny psycho
    "I nod, trying to normalise what Danny's saying."
    "Because I guess this kind of thing is an everyday occurrence to him."
    bree.say "Still..."
    bree.say "It's a shame that he died, I guess."
    show danny shout
    danny.say "Nah, [hero.name]..."
    show danny angry
    danny.say "Fuck that guy."
    danny.say "He was a piece of shit."
    show danny sneaky
    danny.say "And trust me, I know shit when I see it!"
    show danny psycho
    "I nod for a second time, willing to accept Danny's take on the matter."
    bree.say "So..."
    bree.say "That just leaves the matter of payment, right?"
    bree.say "What do you want in return for your help, Danny?"
    show danny normal
    "To my surprise, Danny shrugs and shakes his head."
    show danny shout
    danny.say "Take it as a freebie, [hero.name]."
    danny.say "A favour between friends."
    show danny annoyed
    "I can't help blinking in sheer amazement at this."
    "And I'm stammering as I try to get my words out."
    bree.say "Y...you're serious?"
    bree.say "Really, Danny?!?"
    show danny smile
    "Danny chuckles and shakes his head again."
    show danny sneaky
    danny.say "Nah, [hero.name]..."
    danny.say "I'm just fucking with you!"
    danny.say "I'll take a fuck in the alleyway over there."
    danny.say "Then we're all square."
    show danny smile
    "Now it's my turn to let out a sudden burst of laughter."
    "Because I'm simply amazed at how brazen Danny's being."
    bree.say "Hah..."
    bree.say "You don't beat around the bush, do you?"
    show danny sneaky
    danny.say "I dunno, [hero.name]..."
    danny.say "I'm planning on doing some serious beating around yours!"
    show danny smile
    "I shake my head at this."
    "But not because I'm about to tell Danny to get lost."
    "More because I'm pretty much resigned to this thing happening."
    bree.say "Okay, Danny..."
    bree.say "If that's really what you want?"
    show danny sneaky
    danny.say "You know it is, [hero.name]!"
    show danny smile
    "Now that it looks like the terms have been agreed, I turn towards the alleyway."
    show danny at center, traveling(1.1, 2.0, (740, 820))
    "Danny gives me a leering smile and takes the lead, walking me into the gloom."
    "He doesn't seem to be interested in going too far, just enough to be hidden from the street."
    "Then he gestures to a spot between a dumpster and the door to god knows what."
    show danny sneaky
    danny.say "After you, [hero.name]."
    show danny smile
    "I guess I'm going to have to make the most of this."
    "So I go where I'm directed, then brace myself against the side of the dumpster."
    "I hastily get rif of my clothes."
    hide danny
    show danny stand alley alone
    with fade
    "And I make sure that Danny sees me spreading my legs as I look back over my shoulder."
    bree.say "There you go, Danny..."
    bree.say "Do your worst, or your best."
    bree.say "Because I doubt I'll be able to tell the difference!"
    "Far from being offended, Danny barks out a laugh at this."
    "As if he genuinely enjoys the streak of defiance I'm showing."
    "But I also note he doesn't bother to respond with words."
    "Instead I feel one of his hands grip me on the shoulder."
    "Then the other one makes it's presence felt below my waist."
    show danny stand alley -alone fingering eyes_dazed with fade


    "The weird thing is that I was all set to tune myself out of reality at this point."
    "To think of something else while I left Danny to have his fun."
    "But there's a strange sense of acceptance that I feel settling over me."
    "Not like this is how I wanted things to go down in an ideal world."
    "Far more like a feeling that this is a kind of cosmic rebalancing."
    "Danny did something extreme and dangerous for me."
    show danny stand alley eyes_closed mouth_pleasure
    "So I need to do something just as extreme in order to pay it back."
    "Somehow that helps to absolve me of any guilt that I might have been feeling."
    "And as my mind comes to terms with it, my body seems to fall in line too."

    "I find myself pushing my ass backwards and towards him."
    "Even giving it a little shake from side to side to sweeten the deal."
    "Danny instantly rises to the challenge, grabbing my waist again."
    show danny stand alley fuck out eyes_scared mouth_hurt with fade
    "Then he surprises me by thrusting forwards without warning."
    "The sensation is almost like being impaled, with no hope of escape."
    "Still it takes him more than a couple of tries like that to get anywhere."
    "Each time my pussy stubbornly refuses to give in, keeping him out."
    "But that only seems to make Danny all the more determined."
    "Every time he tries, I can feel the resistance weaken."
    show danny stand alley fuck vaginal eyes_dazed mouth_pleasure at stepback(speed=0.1, h=-10, v=-20)
    "Until finally he gets what he wants, and begins to push inside."
    "I hear him gasp in triumph as I moan with the sensation."
    "Yet Danny's not content to take it slow and savour the moment."
    "Instead he redoubles his efforts, trying to get as deep as he can."
    show danny stand alley eyes_closed at stepback(speed=0.1, h=-10, v=-20)
    pause 0.3
    show danny stand alley at stepback(speed=0.1, h=-10, v=-20)
    "This means one hard thrust after another, inching his way in there."
    "And when he can't get any deeper, that's the when he really starts to move."
    show danny stand alley at stepback(speed=0.1, h=-10, v=-20)
    pause 0.3
    show danny stand alley at stepback(speed=0.1, h=-10, v=-20)
    "Danny's hand moves from my shoulder to the back of my head."
    "He grabs a handful of hair and pulls backwards."
    "I have no choice but to literally bend to his will."
    show danny stand alley at stepback(speed=0.1, h=-10, v=-20)
    pause 0.3
    show danny stand alley at stepback(speed=0.1, h=-10, v=-20)
    "At the same time he's pounding away at me below the waist."
    "Each movement forwards threatening to flatten me against the side of the dumpster."
    show danny stand alley eyes_scared at stepback(speed=0.1, h=-10, v=-20)
    pause 0.3
    show danny stand alley at stepback(speed=0.1, h=-10, v=-20)
    "I fight back with all of the strength I can muster."
    "Which mainly involves bracing my arms and keeping them straight."
    "My muscles are already beginning to strain and ache from the effort."
    "And at the same time, I can feel my legs becoming weak too."
    show danny stand alley at stepback(speed=0.1, h=-10, v=-20)
    pause 0.3
    show danny stand alley at stepback(speed=0.1, h=-10, v=-20)
    "Danny might not be gentle or subtle in any way."
    "But what he lacks in grace he more than makes up for in sheer force."
    show danny stand alley at stepback(speed=0.1, h=-10, v=-20)
    pause 0.3
    show danny stand alley at stepback(speed=0.1, h=-10, v=-20)
    "I feel like my whole body is being pounded flat, tenderised by his attentions."
    "And the worst thing of all is that part of me is actually enjoying it."
    show danny stand alley eyes_closed mouth_dazed at stepback(speed=0.1, h=-10, v=-20)
    pause 0.3
    show danny stand alley at stepback(speed=0.1, h=-10, v=-20)
    "The base, hungry part of my sexual being is delighted at my treatment."
    "I can almost feel it inside of me, baying like a she-wolf."
    "Loving the fact that I'm being fucked like an animal."
    show danny stand alley at stepback(speed=0.1, h=-10, v=-20)
    pause 0.3
    show danny stand alley at stepback(speed=0.1, h=-10, v=-20)
    "But for all of the effort that he's putting in, Danny's only human."
    "And soon enough I feel him starting to twitch and shudder."
    show danny stand alley fuck vaginal cum eyes_ahegao mouth_pleasure with hpunch
    "Then he tenses and thrusts himself deep into me one last time."
    with hpunch
    "He cums a second later, and the intensity means I lose it too."
    show danny stand alley fuck out eyes_closed with hpunch
    "Danny pulls out once he's spent, without a care for what happens to me."
    hide danny stand alley with fade
    "So I find myself collapsing against the dumpster, my head spinning."
    "And it's all I can do to reach down and pull up my panties."
    show danny sneaky at center, zoomAt(1.25, (640, 920)) with fade
    danny.say "Urgh..."
    danny.say "Pleasure doing business with you, [hero.name]."
    danny.say "Look me up the next time you're in need of help."
    danny.say "Because I could sure go for another one of those!"
    hide danny smile with easeoutright
    "I don't even look Danny in the face as he turns and walks away."
    "I just wave a hand vaguely in his direction."
    "Then I turn and begin to stagger towards home."
    "All the time hoping that I don't have to take Danny up on his offer."
    return

label angela_birthday_date_female:
    $ DONE["angela_birthday_date_female"] = game.days_played
    $ game.active_date.clothes = "casual"
    scene bg university
    show angela surprised
    with fade
    "I arranged to meet Angela right in the middle of the university campus."
    "Angela told me she wasn't always so mature and sophisticated."
    "In fact, she confessed to me that she was a pretty wild girl back when she was at college."
    "I figure that being in a place like this should help her remember her own student days."
    angela.say "So this is the place you meant."
    angela.say "I have to admit..."
    show angela normal
    angela.say "I was a little surprised when you said you wanted to meet me here."
    bree.say "Don't worry, Angela..."
    bree.say "It's all part of my plan."
    angela.say "So..."
    show fx question
    angela.say "Did you just get out of class, or something like that?"
    "I shake my head as I prepare to brief Angela on my brilliant plan."
    hide fx
    bree.say "Nope."
    bree.say "I wanted to help you remember your past, Angela."
    bree.say "I thought it'd be a fun birthday if we could help you reconnect with your former self."
    bree.say "Because you told me you were crazy fun back then, remember?"
    show angela surprised
    "I watch as Angela's eyes go wide with surprise."
    angela.say "Oh..."
    angela.say "Oh, I see..."
    show angela disappointed
    angela.say "You know, [hero.name]...that really was a long time ago."
    angela.say "And a lot of crazy things have happened to me since then."
    show angela shy
    angela.say "I don't know if I'm ready to go back there yet."
    menu:
        "Don't worry":
            "I nod and take hold of Angela's hand."
            "And then I give it a squeeze."
            "Which I hope is enough to reassure her."
            bree.say "Don't worry, Angela..."
            bree.say "We're not going to be dropping acid or going to an illegal rave."
            bree.say "And I won't ask you to do anything you're not comfortable with either."
            bree.say "I promise."
            "Angela still doesn't look totally convinced."
            "But she does listen to what I've said."
            "And I can see that she's making a serious effort to conquer her fears."
            show angela normal
            $ angela.love += 2
            $ game.active_date.score += 15
            angela.say "Okay, [hero.name]..."
            angela.say "If you're sure it'll be okay."
            angela.say "Just promise to be gentle with me?"
            bree.say "I will, Angela."
            bree.say "Don't worry about it."
        "Don't be silly":
            "I shake my head and wave a dismissive hand in the air."
            "At the same time I make scoffing noise too."
            bree.say "Pfft..."
            bree.say "Don't be silly, Angela..."
            bree.say "This is going to be great!"
            bree.say "It's like we're going on an adventure, yeah?"
            bree.say "Travelling back into the past!"
            "Angela doesn't look totally convinced."
            "But all the same, she still puts on a brave face."
            show angela normal
            $ angela.love += 2
            $ game.active_date.score += 15
            angela.say "Okay, [hero.name]..."
            angela.say "If you're sure it'll be okay."
            angela.say "Just promise to be gentle with me?"
            bree.say "Trust me, Angela - you have nothing to worry about!"
    "I don't really have a plan that's set in stone for how this is going to happen."
    "Instead I decide to start out this pretty odd date just with a stroll around the campus."
    "I figure that seeing familiar sights will help to stir pleasant memories for Angela."
    "So we do just that, strolling along together as student life goes on all around us."
    "Angela spends most of the time nodding and chuckling to herself."
    "Which must mean that she's being transported back to her own student days."
    "And she proves me right when she starts pointing things out to me."
    angela.say "I guess that building there must be the library."
    angela.say "Geez...that brings back some memories!"
    bree.say "Pulling all-nighters before an exam, yeah?"
    bree.say "And still managing to scrape a pass, I bet!"
    "Angela shakes her head, laughing at my assumption."
    show angela happy
    angela.say "More like finding a quiet corner to sleep off a hangover!"
    angela.say "I could put my head down on the table and just drift off."
    angela.say "Anyone that found me would just assume I'd fallen asleep while studying!"
    "I nod and smile, doing all that I can to encourage Angela."
    "This is the exact kind of stuff that I hoped she'd remember."
    show angela normal
    "But then Angela frowns as she looks at one building in particular."
    angela.say "Huh..."
    angela.say "What's that?"
    angela.say "I don't remember there being a building like that on my campus!"
    bree.say "Oh..."
    bree.say "The Digital Archive?"
    show fx question
    "Angela seems to hear what I say."
    "But she still stares at me blankly."
    hide fx
    menu:
        "You mean... You really don't know what it is?":
            bree.say "Wow, Angela..."
            bree.say "You really are out of touch!"
            bree.say "That's like the place where you can access digital information."
            bree.say "Like stuff that's stored in databases and the University's servers."
            show angela annoyed
            $ angela.love -= 2
            $ game.active_date.score -= 10
            "Angela looks more than a little embarrassed by her lack of knowledge."
            "And I can see that she's not keen to stay in the vicinity of the building."
            angela.say "Okay, [hero.name], okay..."
            angela.say "You already know that I'm a little rusty."
            angela.say "But there's no need to rub it in!"
            hide angela
            "Angela starts walking away, and I hurry to follow her."
            "I can't believe that she's being so sensitive about this."
            "But their is an alternative explanation."
            "Which is that I was being insensitive myself."
        "Let me explain what it is":
            bree.say "That's like the place where you can access digital information."
            bree.say "Like stuff that's stored in databases and the University's servers."
            bree.say "It's really just a library without all the books."
            show angela disappointed blush
            "Angela looks a little embarrassed at her lack of knowledge."
            "But all the same, she also looks happy with my explanation."
            "Maybe even relieved that I kept it so simple and straightforward."
            angela.say "I get it now, [hero.name]."
            show angela normal -blush
            $ game.active_date.score += 15
            angela.say "Thanks for putting it in a way that makes sense."
            angela.say "These days everyone assumes that you're totally up on that kind of thing."
            angela.say "But some of us really didn't grown up with the internet and all that."
            angela.say "So it's not a no-brainer like it is for your generation."
            "I nod, beginning to see how this must seem to Angela."
            "I guess I do kind of take that stuff for granted."
    show angela surprised
    angela.say "Oh yes..."
    angela.say "One thing I do remember is the Student's Union."
    show angela happy
    angela.say "Actually, if I'm honest, the bar at the Student's Union!"
    "Now that sounds more like what I had in mind."
    bree.say "Hmm..."
    bree.say "You have to be a member to get in there."
    bree.say "But I do know a great pub pretty close to the campus."
    bree.say "Come on, I'll take you there."
    "Angela nods eagerly."
    "And she doesn't hesitate to follow on my heels."
    scene bg door pub with fade
    "So after a short walk, we arrive at The Winchester."
    scene bg pub
    show angela
    with fade
    "I don't hesitate to open the door and usher Angela inside."
    "I'd been expecting the place to be pretty quiet."
    "But as soon as we walk in, we're confronted by a large crowd."
    "It seems to be made up of guys and girls, all shouting and singing."
    "And every single one of them looks like they're huge too!"
    "Without hesitation, Angela turns to me and nods."
    show angela happy
    angela.say "Oh yes..."
    angela.say "I remember the university rugby society as well!"
    angela.say "At least somethings never change."
    "I do the best I can to elbow my way through the crowd."
    "And all the time I'm looking for somewhere to sit."
    show angela surprised
    show gwen teaser at flip, mostright5, dark, dark, dark, dark with moveinright
    "But that also means I'm not paying much attention to my surroundings."
    show angela grudge at mostleft4
    show gwen teaser at right, dark, dark, dark, dark
    with hpunch
    "And that's how I manage to collide with a massive girl a moment later."
    "She must have been coming back from the bar."
    "Because she proceeds to fumble and drop a tray of drinks on the floor."
    "Then she looks up at me with fury in her eyes."
    "Girl" "You clumsy little cow!"
    "Girl" "Why don't you look where you're going?!?"
    if randint(0, 1) == 0:
        "I do the best I can to smile and shrug it off."
        "But it doesn't look like the girl's going to let the matter drop."
        "She fronts up to me, jutting her chin out in a belligerent way."
        show angela at left
        show gwen teaser at right4, dark, dark, dark, dark
        with hpunch
        "And she even gives me a shove on the shoulder into the bargain!"
        menu:
            "Stand your ground":
                show angela surprised at left5 with ease
                bree.say "Did you just threaten me?"
                "I don't think the girl was expecting me to stand up to her at all."
                "So as soon as I fire back with a question, it seems to throw her."
                "Girl" "Well...yeah..."
                "Girl" "Didn't you hear me?"
                "Girl" "Of course it was a threat!"
                "I raise any eyebrow in response to this."
                bree.say "There it is, an admission from your own lips."
                bree.say "You just threatened me with physical violence."
                "Girl" "So?"
                "Girl" "What are you going to do about it?!?"
                bree.say "You mean physically?"
                bree.say "Nothing at all."
                bree.say "But I am going to walk over to the bar and report you."
                bree.say "Because this pub has a policy of barring anyone that does that."
                bree.say "And not just you, but all of your little rugby friends here too."
                bree.say "What do you think they're going to say when they find out, huh?"
                bree.say "That you got them all barred from one of their favourite pubs?"
                "The girl looks nervously around for a moment."
                "And then her whole demeanour changes."
                "Suddenly it's like she's the one begging for mercy."
                "Girl" "Okay, okay..."
                "Girl" "I'm sorry, yeah?"
                "Girl" "Let's just forget this ever happened."
                "The girl scuttles off back to her friends."
                "Angela looks at me in amazement, genuinely impressed."
                bree.say "Oh, don't look so surprised."
                bree.say "I've worked behind the bar in places like this."
                bree.say "And you learn to deal with jerks like that pretty quickly."
                show angela happy
                $ angela.sub += 1
                $ game.active_date.score += 15
            "Ease the thing out":
                bree.say "There's no need to talk to me like that."
                bree.say "After all, it was just a couple of drinks."
                bree.say "How about..."
                bree.say "How about I buy you some more?"
                "The girl shakes her head and gives me another shove."
                "Girl" "I don't think so."
                "Girl" "Because you don't even sound sorry."
                "Girl" "But maybe you will after I give you a good slapping!"
                show angela protest at left4
                show gwen teaser at right5
                with ease
                angela.say "Whoa, whoa, whoa..."
                "Suddenly Angela steps between me and the girl."
                angela.say "Did you just threaten to assault my friend?"
                angela.say "Because that's the kind of thing that can get you banned from a bar."
                angela.say "And not just you, but all of your little rugby friends here too."
                angela.say "What do you think they're going to say when they find out, huh?"
                angela.say "That you got them all barred from one of their favourite pubs?"
                "The girl looks nervously around for a moment."
                "And then her whole demeanour changes."
                "Suddenly it's like she's the one begging for mercy."
                "Girl" "Okay, okay..."
                "Girl" "I'm sorry, yeah?"
                "Girl" "Let's just forget this ever happened."
                show angela annoyed
                hide gwen teaser with easeoutleft
                "The girl scuttles off back to her friends."
                "And I look at Angela in amazement, genuinely impressed."
                show angela happy
                angela.say "Oh, don't look at me like that."
                angela.say "You learn to be tough when you raise two kids!"
    else:
        bree.say "Ah, what are you complaining about?"
        bree.say "I just did you a favour, sister!"
        "The girl shakes her head in angry confusion."
        "Girl" "What are you even talking about?"
        bree.say "I don't think you could have handled that booze."
        bree.say "I saved you from looking like a light-weight in front of your buddies!"
        "Girl" "What would you know about drinking, pip-squeak?"
        bree.say "More than you, fat-ass!"
        "Girl" "Okay, let's see you prove it!"
        "Before I know what's happening, I'm pushed down into a seat."
        "And the big girl plants herself in one on the opposite side of the table."
        "Her friends are really getting into it now, jeering and lining up drinks."
        "Girl" "The rules are simple."
        "Girl" "We drink until one of us can't!"
        show angela shy
        angela.say "Erm..."
        angela.say "[hero.name]..."
        angela.say "Are you sure this is a good idea?"
        bree.say "Trust me, Angela..."
        bree.say "I can take her!"
        "I really believe what I'm saying to Angela."
        "Because I've drunk people under the table before."
        if hero.has_skill("iron_stomach") or hero.hunger >= 5 and hero.fitness >= 50:
            "And that requires two things."
            "The ability to pace yourself."
            "And knowing when to throw a curve ball."
            "Which is why I grab my first drink before the other girl even looks ready."
            "And I toss it straight back, swallowing it all in one go."
            "The drink hits my stomach pretty hard, but I know I can take it."
            "Even better, the other girl is staring at me in amazement."
            "I take advantage of this, grabbing the second drink and getting stuck in."
            "And all the while she's groping for her first, trying to make up for lost time."
            "After that there's no real chance of her catching me up."
            "She does the best she can, but it's not going to be enough."
            "The girl just seems to get more drunk and slower the whole time."
            hide gwen teaser
            "In the end, she sways for a moment, then fall of her chair and onto the floor."
            "Her friends hurry to check that she's okay."
            "And Angela helps me to my feet too."
            show angela happy at center
            $ game.active_date.score += 15
            angela.say "That was amazing, [hero.name]!"
            angela.say "How ever did you do it?"
            bree.say "Buuuurrrp!"
            show angela normal
            angela.say "Come on, [hero.name]..."
            angela.say "What you need now is some strong coffee..."
        else:
            "But as I reach out for the first drink, I can't believe what I'm seeing."
            "The other girl has already grabbed her first drink."
            "And she's knocked it back in one go!"
            "While I stare at her in amazement, she takes full advantage."
            "And she does that by picking up the second drink and starting on that."
            "I hurry to chug down my own first drink."
            "But in my haste, I forget to pace myself properly."
            "Which in turn means that I choke on the liquid."
            "And when I finally manage to swallow, it hits my stomach like a clenched fist to the gut."
            "After that, there's no chance of me catching up."
            "I keep on trying, but all that happens is I get steadily more drunk."
            "In the end I feel so dizzy that I fall off my seat."
            "And Angela has to pick me up, as the other girl's friends pat her on the back."
            show angela disappointed
            angela.say "Come on, [hero.name]..."
            angela.say "You did your best."
            show angela shy
            angela.say "What you need now is some strong coffee..."
    scene bg black with dissolve
    pause 1.5
    scene bg pub
    show drink pub angela
    with dissolve
    "Now that all the fuss with the rugby society seems to be over, Angela and I can finally settle down."
    "We find a table all to ourselves, grab some drinks, and soon enough we're chatting away pleasantly."
    "At first the topics of conversation are all pretty tame and we keep the jokes clean too."
    "But one drink leads to another, and soon enough I'm starting to feel a little wicked."
    "I can't help stealing looks at Angela's astonishing body, and it's making me feel all hot."
    "Oh god...is being drunk how it feels to be a guy?"
    "Totally dumb and only able to think about sex?!?"
    "I can feel my cheeks beginning to burn as Angela finally catches me staring at her breasts."
    "So I tear my eyes away and desperately try to look for something to serve as a distraction."
    "Then I see it."
    "There's a table full of hot guys just over there."
    "Oh...but there's also one full of hot girls just next to it!"
    "My plan was to distract Angela by pointing out the hotties."
    "Then we could chat about which ones are our favourites."
    "Maybe even send them an anonymous drink over and see what happens!"
    "But the only problem is that I don't know which table to choose."
    "The table of hot guys?"
    "Or the table of hot girls?"
    menu:
        "Point out the hot girls":
            hide drink
            show angela
            bree.say "Whoa..."
            bree.say "Angela..."
            bree.say "Check out those hotties over there!"
            show angela sadistic
            angela.say "[hero.name]!"
            angela.say "You're so naughty!"
            "Angela might be trying her best to sound shocked."
            "But I can already see she's trying to spot them herself."
            show angela happy
            angela.say "Which table are you talking about?"
            angela.say "Just out of curiosity..."
            bree.say "The one with the girls."
            bree.say "That one over there."
            "Angela spots the table I mean."
            "And I see her eyes go a little wider as she checks them out."
            show angela flirt
            angela.say "Mmm..."
            angela.say "They really are hot!"
            angela.say "I like the look of the blonde right there."
            show angela happy
            angela.say "You know, she's just the type I used to go for."
            angela.say "At least before I met [mike.name]'s dad!"
            bree.say "You...you mean you really like blonde girls?"
            bree.say "Girls like me?"
            show angela normal blush
            "Angela's head spins around as she hears what I just said."
            "And her cheeks flush red as she realises what it implies."
            angela.say "W...well, yes, [hero.name]..."
            angela.say "I guess you're right!"
            angela.say "If we'd met back then..."
            angela.say "And if you were my age, of course!"
            show angela flirt
            angela.say "I'd have been really into you."
            bree.say "And what about now?"
            "Angela doesn't say anything."
            $ game.active_date.score += 15
            $ angela.love += 2
            "Instead she leans in and kisses me gently on the lips."
            "Which is probably the best answer I could have hoped for!"
        "Point out the hot guys":
            bree.say "Whoa..."
            bree.say "Angela..."
            bree.say "Check out those hotties over there!"
            show angela sadistic
            angela.say "[hero.name]!"
            angela.say "You're so naughty!"
            "Angela might be trying her best to sound shocked."
            "But I can already see she's trying to spot them herself."
            show angela happy
            angela.say "Which table are you talking about?"
            angela.say "Just out of curiosity..."
            bree.say "The one with the guys."
            bree.say "That one over there."
            "Angela spots the table I mean."
            "And I see her eyes go a little wider as she checks them out."
            show angela flirt
            angela.say "Mmm..."
            angela.say "They really are hot!"
            show angela normal
            angela.say "The blonde one reminds me of [mike.name]'s dad."
            angela.say "You know, when he was younger?"
            "I nod and smile, trying to look like I'm interested."
            "But the truth is that I'm starting to think I made a mistake."
            "I was trying to get Angela in the mood to talk about kinky shit."
            "But instead I seem to have stirred up fond memories of her husband."
            "And hell, I want all of that attention on me, not him!"
    show angela normal -blush
    "I can see that getting Angela to spend a little time eyeing people up was a good idea."
    "It seems to have relaxed her, kind of easing her into being more honest and open."
    "And best of all it's also made her more keen to talk about matters of the heart."
    angela.say "I'm having a good time right now, [hero.name]."
    angela.say "I have to admit that I wasn't sure about all of this."
    angela.say "Because normally I don't like to be reminded of the past."
    show angela disappointed
    angela.say "And...well...the fact that I'm not as young as I once was!"
    if randint(0, 1) == 0:
        "I shake my head as Angela says all of this."
        "Because I want to assure her that age isn't an issue."
        "That it's not something that will put me off being with her."
        if hero.charm >= 85:
            "I smile and shake my head."
            "Then I reach out and put my hand atop Angela's."
            bree.say "You're a mature woman, Angela."
            bree.say "And a really beautiful one too!"
            bree.say "You know who you are and what you want."
            bree.say "Put all of that together, and you get one hell of a package!"
            show angela surprised
            "Angela's expression changes to one of surprise."
            "And then just as quickly to one of delight."
            angela.say "Do you really mean that, [hero.name]?"
            bree.say "Of course I do, Angela!"
            show angela happy
            $ angela.love += 2
            $ game.active_date.score += 25
            angela.say "It feels so strange to hear someone talking about me like that."
            angela.say "I guess I've gotten used to people not seeing me that way."
            angela.say "To them just seeing me as a wife or a mother."
            angela.say "But it's exciting as well as scary!"
            "Angela puts her other hand on top of mine too."
            "And she squeezes it tightly."
            "Which makes my heart beat a little faster."
        else:
            "I laugh and shake my head."
            "Waving away Angela's concerns with a flick of my hand."
            bree.say "Ha!"
            bree.say "Come on, Angela..."
            bree.say "You're not THAT old!"
            bree.say "I mean...you're younger than my mom is, yeah?"
            show angela shock
            "Angela's expression changes to one of surprise."
            "And then just as quickly to one of annoyance."
            angela.say "Is that really how you see me, [hero.name]?"
            show angela grudge
            $ angela.love -= 5
            $ game.active_date.score -= 35
            angela.say "You measure me against your own mother?"
            "I shake my head, realising that I've screwed-up."
            bree.say "No!"
            bree.say "That's not it at all!"
            "Angela nods and seems to be willing to let the matter drop."
            "But I make a mental note to steer clear of the subject in future."
    else:
        "I can't help letting out a yawn as I shake my head."
        "Because it's far later than I realised."
        show layer master at blur(4)
        "In fact, I can feel my eyes getting heavier by the second!"
        if hero.has_skill("no_sleep") or hero.energy >= 8:
            show layer master at default
            "I shake away what I know is the urge to drop off to sleep."
            "And I somehow find a hidden reserve of energy to keep myself awake."
            bree.say "Ooh..."
            bree.say "Sorry, Angela..."
            bree.say "Here you are talking about age."
            bree.say "And I'm the one that's falling asleep!"
            show angela normal
            "Angela smiles and lets out a chuckle of amusement."
            angela.say "I guess you're right, [hero.name]."
            $ game.active_date.score += 15
            angela.say "You really are only as old as the one you feel!"
            show angela flirt
            "Angela underlines her point by reaching under the table."
            "And then I feel her stroking my thigh with her hand!"
            "Suddenly any notion of falling asleep is gone."
            "And all I want to do is see where this is going."
        else:
            show layer master at dark, dark
            "Everything seems to go black for a moment."
            scene bg black with dissolve
            "And I kind of drift away from reality."
            "But then I feel myself being gently shaken."
            "And suddenly I'm back in the room."
            scene bg pub
            show angela annoyed
            bree.say "Urgh..."
            bree.say "Wha..."
            bree.say "What happened?"
            angela.say "Erm..."
            angela.say "You kind of dropped off for a second there, [hero.name]."
            show angela grudge
            $ game.active_date.score -= 20
            angela.say "I didn't think I was that boring!"
            "I can feel my cheeks burning as Angela explains the situation."
            "And my embarrassment only gets worse a moment later."
            "When I realise that I was starting to drool in my sleep too!"
            bree.say "Oh no!"
            bree.say "Angela, I'm so sorry!"
            show angela annoyed
            $ angela.love -= 3
            angela.say "And here I was thinking that I was the old, boring one!"
    "Angela smooths back her hair with a hand."
    "And that lets me see the earrings she's wearing for the first time."
    bree.say "Ooh..."
    bree.say "Those are nice, Angela!"
    show angela normal
    angela.say "The earrings?"
    angela.say "They are, aren't they?"
    angela.say "[mike.name] bought them for me as a birthday present."
    if not hero.has_gifts:
        "I feel like kicking myself as I realise that I didn't get Angela a gift myself."
        "Somehow I managed to forget all about it."
        bree.say "Damn it!"
        bree.say "I'm sorry, Angela..."
        bree.say "I forgot to get you anything."
        bree.say "I can be so forgetful!"
        $ game.active_date.score -= 10
        $ angela.love -= 2
        "Angela shakes her head at this."
        angela.say "Don't be so hard on yourself, [hero.name]."
        angela.say "It's not the end of the world."
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_32
        if _return != "done":
            if _return not in ["None", "exit"]:
                "The mention of birthday presents reminds me of something important."
                "And so I pull out the gift that I bought for Angela."
                bree.say "Speaking of which..."
                bree.say "Happy birthday!"
                show angela happy
                angela.say "Oh, [hero.name]!"
                angela.say "How thoughtful of you to remember."
                "Angela takes the gift from me."
                "And then she carefully unwraps it while I watch."
                if _return:
                    "But as soon as she sees what's inside, Angela seems to come alive."
                    "Her eyes widen and she holds up the gift to get a closer look."
                    "And for a moment it's almost like she forgets I'm even there."
                    bree.say "Angela?"
                    bree.say "Are you okay?"
                    angela.say "Oh..."
                    angela.say "Oh yes, [hero.name], I'm fine."
                    angela.say "I'm just amazed you managed to find one of these!"
                else:
                    show angela normal
                    $ game.active_date.score -= 10
                    "But as soon as she sees what's inside, Angela seems to lose interest."
                    "Sure, she goes through the motions of smiling and nodding."
                    "Yet it's clear that she's not really that impressed."
                    angela.say "It's very nice, [hero.name]."
                    angela.say "Thank you very much."
                    bree.say "Okay..."
                    bree.say "I guess..."
            else:
                "I feel like kicking myself as I realise that I didn't get Angela a gift myself."
                "Somehow I managed to forget all about it."
                bree.say "Damn it!"
                bree.say "I'm sorry, Angela..."
                bree.say "I forgot to get you anything."
                bree.say "I can be so forgetful!"
                $ game.active_date.score -= 10
                $ angela.love -= 2
                "Angela shakes her head at this."
                angela.say "Don't be so hard on yourself, [hero.name]."
                angela.say "It's not the end of the world."
    "I happen to check the time, and I'm amazed to see how late it is."
    "Angela notes my surprise and leans in to see the time too."
    show angela surprised
    angela.say "Oh my!"
    angela.say "Is it really that late already?"
    bree.say "Well, you know what they say."
    bree.say "I guess time really does fly when you're having fun!"
    show angela normal
    bree.say "So..."
    bree.say "You want to call it quits?"
    bree.say "Or should we maybe do something else fun?"
    if game.active_date.score >= 100:
        "Angela looks more than a little tired."
        "But she nods at the mere mention of keeping the date going."
        angela.say "If that's okay with you, [hero.name]?"
        angela.say "I'm having a really great time."
        angela.say "And I don't want it to end yet!"
        bree.say "Me too, Angela..."
        bree.say "But I think that we should maybe go somewhere else."
        "Angela nods in agreement."
        "Then she reaches across the table and takes hold of my hand."
        show angela flirt
        angela.say "Come on, [hero.name]..."
        angela.say "Let's go find that somewhere else."
        "I get to my feet at the same time as Angela."
        hide angela with easeoutright
        "And still holding hands, we head for the door."
        "I'm not exactly sure where we're going."
        "And I don't know what will happen once we get there."
        "But one thing I do know is that it'll be fun finding out!"
        call angela_birthday_sex_female from _call_angela_birthday_sex_female
    else:
        "Angela stretches and lets out a little yawn."
        "Though I can't help the feeling that it's a tad put on."
        angela.say "Oooh..."
        angela.say "Listen to me, [hero.name]."
        angela.say "I'm practically falling asleep on my feet!"
        angela.say "I had a great time tonight."
        angela.say "But I think it's time to go to bed."
        "I nod in agreement."
        "Not because I feel the same way."
        "But more because I don't want to seem needy."
        bree.say "Oh, sure thing, Angela..."
        bree.say "I could do with getting some sleep too."
        bree.say "But we're going to do this again, right?"
        bree.say "And soon, yeah?"
        angela.say "Sure, [hero.name]."
        angela.say "I'll call you, okay?"
        hide angela with easeoutright
        "I nod and wave as Angela gets up and walks to the door."
        "That meant what I thought it meant, right?"
        "That she's going to call me soon?"
        "No matter how much I tell myself that it did, I still have some nagging doubts."
    return

label angela_birthday_sex_female:
    scene bg street
    show angela casual
    "It doesn't take long for Angela and me to flag down a taxi."
    "And as soon as we pile into the back, there's decision to be made."
    "Where are we going to go?"
    "At first, neither of us says a thing, we just stare at each other."
    "But then I surprise myself by being the one to speak up."
    bree.say "My place..."
    bree.say "We're going to my place..."
    bree.say "Right?"
    "Angela nods and I feel her take hold of my hand."
    "Then she squeezes it tightly."
    angela.say "You bet, [hero.name]."
    angela.say "But you might want to give the driver your actual address!"
    "I nod and do as she says, so we can begin our journey."
    show bg house with fade
    "And from there, the drive seems to pass by in the blink of an eye."
    "When the taxi pulls up, I pay the driver and we start to walk up to the house."
    "But I can already sense that there's an unspoken question hanging in the air."
    "One that neither of is wants to be the one to bring up."
    "Yet it's the reason that we're slowing down as we get ever closer to the front-door."
    "In the end, just like in the taxi, I figure I should be the one to break the silence."
    bree.say "I know what you're thinking, Angela..."
    bree.say "But for all we know, [mike.name] could not be home."
    "Angela nods, and I feel her squeeze my hand all over again."
    angela.say "It doesn't matter if he's home or not, [hero.name]."
    angela.say "[mike.name]'s all grown up now."
    angela.say "He's not a little boy anymore - he's a man."
    angela.say "And I have a life of my own to lead."
    "We're mounting the steps to the porch as Angela says all of this."
    "And I'm nodding, agreeing with the sentiment one hundred percent."
    "But I still feel like I want to sneak into the house unseen."
    bree.say "Totally, Angela, totally..."
    bree.say "But I'd be sneaking you into the house if you were anyone else."
    bree.say "I'm just not in the habit of announcing to my housemates that I'm getting it on!"
    "Angela nods, letting me know that she's on the same page."
    "So it's agreed - we're not hiding from [mike.name]."
    "But we're not going to sit him down and tell him what we're doing either."
    show bg livingroom with dissolve
    show angela at left with ease
    "To that end I open the door as quickly and quietly as I'm able."
    "And then we hurry up the stairs to my bedroom."
    "I must have walked that short route thousands of time already."
    show bg secondfloor with dissolve
    show angela at right5 with ease
    "But today it feels like the longest walk of my life."
    "I'm looking this way and that, expecting [mike.name] or Sasha to appear at any moment."
    "By the time we make it to my room, my heart is pounding in my chest."
    show bg bedroom4 with dissolve
    show angela at left5 with ease
    "And I all but drag Angela inside as I slam the door shut behind us."
    "Leaning against it, I try to get my breathing under control."
    "And I can see that Angela's in pretty much the same state too."
    bree.say "I..."
    bree.say "I think...we made it!"
    show angela at center, zoomAt (1, (640, 720)) with ease
    show angela at center, traveling (1.25, 1.0, (640, 940))
    "Before I can say another word, Angela walks over to me."
    hide angela
    show angela kiss at right4, startle(0.05,-10)
    $ angela.flags.kiss += 1
    "And she presses her lips against mine, kissing me with a passion!"
    "It seems like she's not trying to calm herself down."
    "Instead she's decided to give in and go with the adrenaline rush!"
    "But it's not like I've managed to calm myself down."
    "Not in the space of those few short seconds."
    "And now I can feel my pulse starting to speed up all over again."
    "What other choice do I have but to give in?"
    "Before I know it, I'm giving as good as I'm getting."
    "And I'm no longer leaning against the door either."
    "Instead I'm pushing Angela backwards as I kiss her."
    show angela kiss at center with ease
    "Each step takes us closer to the bed."
    show angela kiss underwear with dissolve
    "And our hands are tugging at each other's clothes."
    show angela kiss at left4 with ease
    "Once a garment it taken off, it gets tossed aside."
    show angela kiss naked with dissolve
    "Then we start on the next one with even greater determination."
    show bree cunnilingus angela
    "By the time I feel us bump into the bed, both Angela and I are naked."
    "Neither of us stops long enough to lower ourselves onto the mattress."
    "Instead we tumble down onto it in a tangle of limbs."
    with vpunch
    "We roll on the bed, Angela coming up on top."
    scene angela cunnilingus bree with vpunch
    "And she wastes no time in taking advantage of that fact."
    "Angela places her hands on my shoulders, pinning me down."
    "I could struggle to free myself, try to take control."
    "But I'm far too intrigued to see where this is going."
    "I want to discover what she has in mind for me."
    "And so I just lie back and let Angela have her way."
    "She lowers herself down, holding my eye as she does so."
    "Angela doesn't stop until her head is level with my breasts."
    show angela cunnilingus bree suck with fade
    "Then she casts her eyes down and falls on them without mercy."
    "I feel my nipples stiffen and become hard as her lips find them."
    "I was pretty turned on by what Angela's mouth did to mine."
    "But I'm totally blown away by what it's now doing to my chest."
    "Angela licks, nuzzles and bites in ways I didn't think were possible."
    "Rather and I swear that she's tweaking her technique all the time too."
    show angela cunnilingus bree down
    "This isn't just having someone put my nipples in her mouth."
    "It's like she's playing them, like they're a delicate musical instrument."
    bree.say "Aah..."
    bree.say "Angela..."
    bree.say "What are you..."
    show angela cunnilingus bree down pleasure
    bree.say "Oh...oh god!"
    "The tone and volume of my voice change as Angela surprises me again."
    "I was so tied up in what she's doing to me I didn't notice her hands move."
    show angela cunnilingus bree up pleasure
    "And they've now wandered all the way down to my belly, then below."
    "Angela's playing with my pussy too, just as skilfully as she is my breasts!"
    "The tips of her fingers trace the lines, slowly and deeply."
    show angela cunnilingus bree outside down normal
    "And they move ever closer to the centre with each pass."
    "This means that when Angela reaches the middle, she meets no resistance."
    show angela cunnilingus bree inside
    "Her fingers are able to slide straight into me, pushing me to another level."
    show angela cunnilingus bree pleasure
    "I have to close my eyes in order to keep from being overwhelmed."
    "But the moment that I do, Angela makes her next move."
    "I hardly notice as she abandons my breasts."
    "As the sensations from my pussy are drowning everything else out."
    show angela cunnilingus bree lick -inside with fade
    "Realisation only dawns when I feel those lips and that tongue down there."
    "And it's not like Angela chooses to slow down or go easy on me either."
    "Instead she takes full advantage of the groundwork her fingers have already laid down."
    "Angela all but dives in head-first, tongue pushing into me."
    "And as a woman, she knows just what to do down there too."
    "With a guy I'd be having to make the right sounds to guide him."
    "To let him know just how good it felt and when I wanted more of the same thing."
    show angela cunnilingus bree lick up
    "But Angela knows from her own experience where to go and what to do."
    "She cuts right to the point, pushing me further with each passing second."
    "Angela gives me exactly what I want, even before I know that I want it myself."
    show angela cunnilingus bree lick up outside
    "And if I could, I'd lie here and just soak it up forever."
    "But there's only so much that my body can take."
    "I'm already fast approaching that point, beginning to teeter on the edge."
    show angela cunnilingus bree lick up inside
    "And then it happens, I feel myself swept away and rendered helpless."
    "All I can do is lie there, letting my orgasm pass over me."
    "I don't know if Angela's aware that its happening."
    show angela cunnilingus bree lick ahegao
    "And I can hardly feel what she's doing to me now."
    "My senses are flooded, my mind overwhelmed."
    "So I just surrender, and wait for my mind to come back to me."
    $ angela.love += 2
    $ angela.sexperience += 1
    $ game.pass_time(2)
    return


label angela_female_event_15:
    if angela.love.max < 200:
        $ angela.love.max = 200
    "I've been bursting at the seams ever since Dylan got what he deserved."
    "Bursting with the desire to see Angela now that she's finally free of him."
    "But I guess there's always some kind of red-tape in these kinds of situation."
    "Because it's a couple of days before she can actually find the time to see me."
    "And while I wait for Angela to turn up, I can feel my guts kind of starting to churn."
    "I mean, she's meeting me to say that everything is cool now, right?"
    "Now we can relax and really start living our best lives together."
    "Even begin to think about planning for the future."
    "But there's still that little bit of me that's paranoid and expecting bad news."
    "Like maybe the stress of all this will somehow make Angela want to cool things off."
    "Or worse, she could realise she only loved me as a refuge from what Dylan was doing to her."
    "And now that he's out of the picture, her real feelings are becoming clear!"
    "No, no, no..."
    "That's just crazy."
    "What Angela and I have been building together is more stable than that."
    "At least, I hope it is!"
    angela.say "[hero.name]..."
    angela.say "Hey, [hero.name]!"
    "All of those doubts seem to vanish at the sound of Angela's voice."
    "I find myself instantly turning in the direction from which it's coming."
    show angela happy at center, zoomAt (1.5, (640, 1040)) with easeinright
    "And when I see her hurrying towards me, I feel sure of her feelings for me."
    "Angela has the biggest smile on her face right now."
    "In fact, I don't think I can remember seeing her so happy before now."
    show angela normal
    bree.say "Angela..."
    bree.say "It's so good to see you."
    bree.say "It feels like it's been ages!"
    show angela happy
    angela.say "Oh, don't be silly, [hero.name]..."
    angela.say "It can't have been more than a day or two."
    angela.say "But I will say, a lot's happened in that time."
    show angela normal
    "I'm nodding as Angela begins to explain herself, perhaps a little too eagerly."
    "The truth is that I want to leap straight into questioning her about everything."
    "But I'm doing the best I can to keep from overwhelming her."
    bree.say "But most of it's good, right?"
    bree.say "It's all turned out the way we hoped?"
    if "angela_female_event_14a" in DONE or "angela_female_event_13c" or "angela_female_event_13f" in DONE:
        show angela annoyed
        "Angela nods."
        "And as soon as she does so, I feel a surge of relief."
        show angela happy
        angela.say "That's pretty much it, [hero.name]."
        angela.say "I've been speaking with my lawyers about all of this."
        angela.say "And they say that I'm entitled to the house and Dylan's assets."
        angela.say "At least the ones he couldn't take with him."
        show angela normal
        bree.say "That sounds like good news, Angela."
        "Angela nods again."
        show angela angry
        angela.say "Plus the lawyers said he won't be able to stop me from divorcing him too!"
    elif "angela_female_event_13g" in DONE or "angela_female_event_13h" in DONE:
        show angela annoyed
        "Angela looks a little uncomfortable as I ask the question."
        show angela happy
        angela.say "I'm not sure I'd call Dylan being dead a good thing, [hero.name]..."
        angela.say "Even knowing what he did to me, the man is still [mike.name] and Minami's father."
        show angela annoyed
        "I feel a sudden pang of embarrassment and regret."
        "Because Angela's right in what she's saying."
        "And it was pretty crass of me to say something like that."
        bree.say "Ah hell, Angela..."
        bree.say "I'm sorry, really I am!"
        bree.say "I've just gotten so used to seeing the guy as the villain of the piece."
        bree.say "I should have remembered that he was also a husband and a father."
        "Angela's mood visibly softens as I make my apology."
        "And she nods, letting me know that it's been accepted."
        show angela happy
        angela.say "That's okay, [hero.name]."
        angela.say "It's the only way that you knew him."
        show angela disappointed
        angela.say "But now I have to accept the fact that I've been left a widow."
    show angela normal
    "I feel the weight of that last statement hit me like a slap in the face."
    "Because it means that Angela just dropped her legal status into the mix."
    "Before now we've basically been lovers, engaged in an affair behind her husband's back."
    "But now that he's out of the picture, there's the chance for us to become far more."
    "And I'm waiting to find out what Angela has to say on the subject."
    show angela worried
    angela.say "Why are you looking at me like that, [hero.name]?"
    show angela shy
    "I blink and shake my head in surprise at Angela's question."
    "Because I might have been waiting with baited breath to hear what she said next."
    "But that was not what I was expecting to hear at all!"
    bree.say "What..."
    bree.say "I..."
    bree.say "Well, Angela..."
    bree.say "I was kind of wondering what that meant for us?"
    bree.say "You know, we went through all of this stuff together."
    bree.say "I'm just hoping that there's a future for us now it's over, that's all!"
    show angela surprised
    "Angela looks at me in confusion for a moment."
    "Like she's not really sure where all of this is coming from."
    angela.say "Oh, [hero.name]..."
    show angela happy
    angela.say "You silly goose, you!"
    angela.say "Of course there's a future for us."
    angela.say "That is if you want to spend your time with an old maid like me?"
    show angela normal
    "I don't bother to answer that question with words."
    "And I don't know that I could have done if I'd tried."
    "Because the emotions inside of me are just too intense."
    show angela shy blush at center, traveling(2.0, 0.5, (640, 1340))
    "Instead I throw my arms around Angela, pulling her close to me."
    "Angela seems overwhelmed for a moment, but then she returns the hug."
    show angela disappointed
    "And neither of us seems to feel the need to speak after that."
    "The embrace that we share is enough to express how we feel."
    "That we want to be together and won't let anything pull us apart."
    scene bg black with dissolve
    return

label angela_female_ending:
    $ game.hour = 16
    $ game.room = "church"
    $ game.season = 1
    scene bg church wedding at center, zoomAt (1.0, (640, 720)) with fade
    "I might be into my videogames and other nerdy stuff, and I certainly don't come across as a normal girl."
    "But there are still some of those essentially girly things that I've done throughout my life so far."
    "And one of those is to imagine how my wedding would go down in the ideal world of my own imagination."
    "Sure it's changed over the years, based on where my head was at that point and what I was into at the time."
    "But one thing's for sure - I never imagined it would turn out like this!"
    "After the roller-coaster of a ride Angela and I had to get here, the wedding itself was almost an afterthought."
    "Amnesia, hospital trips, hypnosis, calling in the police and confronting her stage magician husband..."
    "All of that meant for a while we were just relieved to be done with it and in the clear."
    "So when we began to plan the ceremony, we realised that neither of us had a clue what we wanted."
    "I mean who was going to be where and when?"
    "Do we both start the ceremony at the altar?"
    "Do we both walk down the aisle?"
    "And would that be together or apart?"
    "Do we go with one of us at the altar and the other walking down the aisle?"
    "And even then who goes where?"
    "In the end we decided that Angela had done the walking down the aisle thing the last time."
    "And anything that made this wedding different to her last one could only be a good thing."
    "So she's the one standing at the altar, and I'm going to be walking down the aisle."
    "But of course those are just the physical details of the ceremony."
    "Having them all figured out doesn't do a thing to help with my nerves."
    "I keep on trying to psyche myself up for this."
    "Yet I'm still feeling nervous right up to the moment when the music starts to play."
    "And when that happens, I know that I don't have any more time to work on it."
    "I just have to take a deep breath and walk into the chapel."
    "Then whatever happens is down to fate."
    "So that's just what I do, pushing through it and walking straight in there."
    "As soon as I do so, I feel my nerves become even worse than before."
    "Because now I'm confronted by every single guest we invited turning to stare at me!"
    "I can see Sasha, [mike.name] and Minami on one row."
    "I can see my mom and dad on another."
    "A lot of the other faces I don't seem to recognise."
    "But that's probably another consequence of the nerves."
    show angela wedding zorder 4 at center, zoomAt (1.0, (640, 740)) with dissolve
    "It's only when I see Angela, waiting for me at the altar, that things change."
    "Suddenly all that matters is closing the distance between me and her."
    show bg church wedding at center, traveling (1.3, 5.0, (640, 940))
    show angela wedding at center, traveling (1.5, 5.0, (640, 1040))
    "I almost forget where I am and what we're doing as I begin to hurry down the aisle."
    "And more than once I actually have to force myself to slow down to a more dignified pace."
    if hero.pregnant:
        "I'm so eager to get to Angela that I almost forget to support my belly."
        "But then the cut of my dress has been made to take that into account."
        "It subtly works the shape of the curve into its design, but doesn't seek to hide it."
        "Meaning that I can show off the fact I'm pregnant without it looking awkward."
    else:
        "I'm so eager to get to Angela that I almost manage to trip over my own feet!"
        "But I guess that's what you get for wearing flats more than heels."
        "And not for the first time, I wish I'd worn sneakers under my dress."
        "Because who in the hell was ever going to see them?"
    hide angela
    show wedding angela with fade
    "Angela greets me with the warmest smile imaginable as I finally reach her."
    "And I'm about to say something to her, probably something silly too."
    "But she stops me by nodding towards the waiting priest."
    show wedding angela priest with dissolve
    "Priest" "Ahem..."
    "Priest" "Shall we get started?"
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join these two people in the bonds of holy matrimony."
    "For all that our relationship has been wild so far, the rest of the ceremony is pretty standard fare."
    "The priest recites all of the stuff that he has to about morality and being a good person."
    "Which means that everyone is on autopilot until the interactive part of the show."
    "Priest" "Angela..."
    "Priest" "Do you take [hero.name]..."
    "Priest" "To be your lawful, wedded partner?"
    angela.say "I do."
    "Priest" "And do you, [hero.name]..."
    "Priest" "Take Angela..."
    "Priest" "To be your lawful, wedded partner?"
    bree.say "You bet I do!"
    "The priest nods, and I can see him trying not to smile."
    "Priest" "Very well..."
    "Priest" "I call upon all those here present..."
    "Priest" "That if you know of any lawful reason these two may not be wed..."
    "Priest" "Speak now, or forever hold your peace!"
    "This is supposed to be the point where the priest pauses for effect."
    "And where the guests share a knowing chuckle as they wait for the moment to pass."
    "But for Angela and I, it's been something that we've dreaded."
    "Because there's always that irrational fear in the back of our minds."
    "The fear that somehow Dylan could come back and ruin our big day."
    "That the tendrils of his magical powers could reach out and snatch away our happiness."
    "But luckily for us, the moment passes without incident."
    "And the sigh of relief that I let out is a genuine one."
    "Priest" "Very good..."
    "Priest" "By the powers vested in me..."
    "Priest" "I pronounce you married."
    "Priest" "You may celebrate in an appropriate manner."
    show wedding angela -priest with dissolve
    "To Angela and me that means only one thing."
    scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
    show angela wedding kiss
    with fade
    $ angela.flags.kiss += 1
    "We wrap our arms around each other and lean into a kiss."
    "It's pretty long and intense, more so than most altar kisses."
    "But I think that after all we've been though to get here, we kind of deserve it."
    "And it's a show of defiance too, against all the forces that stood in our way."
    "We beat them all and endured, now we're here and the deal is done."
    "And we have the rest of our lives to enjoy the victory together."
    show angela ending with fade
    angela.say "Are you sure that this is the best way to do things?"
    angela.say "I mean, [hero.name]'s been the one to tell the story up to here."
    angela.say "Why would you want to switch things around at the very end?"
    angela.say "Okay, okay...I suppose that makes sense."
    angela.say "So here goes..."
    angela.say "When you've been through something like I have, it's hard to tell what's real from what's not."
    angela.say "My memories from before I met Dylan are something I think I can be sure of, that he didn't tamper with."
    angela.say "But from the moment that man came into my life, nothing at all is certain to me."
    angela.say "I always thought that I'd changed from the person I was in college because of my experiences in life."
    angela.say "Meeting Dylan and falling in love with him, becoming part of his act and then settling down to raise a family."
    angela.say "I told myself it was all so different from the dreams I had before him on account of growing into an adult."
    angela.say "Every new person that I met was just a footnote in the ongoing story of our lives together."
    angela.say "That was until I met [hero.name]."
    angela.say "To begin with she was nothing more than one of [mike.name]'s housemates, a female friend of my son."
    angela.say "But right from the start I found myself hitting it off with her, as she reminded me of myself."
    angela.say "Not the wife and mother that I was at the time, the girl I'd been back in college and even before that."
    angela.say "Maybe that's why the control Dylan had over me began to loosen around that time?"
    angela.say "Getting to know [hero.name] reminded me of who I was before he started to mould me into what he wanted."
    angela.say "And that weakened the hypnotic suggestions he'd put inside of my head."
    angela.say "Well, that's my theory anyway."
    angela.say "I wasn't consciously aware of it at the time, but I started spending more time around [hero.name]."
    angela.say "Whenever I was in town to see [mike.name] or Minami, I'd make an excuse to come to the house."
    angela.say "And if [hero.name] wasn't there, I would have to do my best to hide my disappointment."
    angela.say "Pretty soon I was popping up there for the flimsiest of reasons."
    angela.say "Probably making it look like I was a typical fretting mother, vetting anyone around [mike.name]."
    angela.say "I think [hero.name] must have sensed something in my attitude towards her."
    angela.say "Because she didn't mind me being around, and even shared meals with me."
    angela.say "From there it was a natural step to meeting up for the occasional coffee."
    angela.say "Even happening to bump into her by accident at the mall."
    angela.say "Or at least that's how I made it look..."
    angela.say "[hero.name] and I were almost becoming friends in our own right."
    angela.say "Maybe she saw me more as an older sister at that point though."
    angela.say "But for me she was a breath of fresh air, finally someone that I could talk to."
    angela.say "I would never have been able to admit it openly, but I was feeling smothered in my daily life."
    angela.say "So when [hero.name] began pumping me for information about my past, I was more than happy to oblige."
    angela.say "But that was when the black-outs started to happen, me waking up in places I couldn't remember going to."
    angela.say "Now it seems obvious that Dylan was using his hypnotism to stamp out the effects [hero.name] was having on me."
    angela.say "Every time she's awaken even a sliver of my former self, he must have stamped it out viciously."
    angela.say "And I feel like it was almost a battle, the desperation of his efforts being what affected me so badly."
    angela.say "The problem was that he'd spent so long conditioning me to be the perfect wife and mother."
    angela.say "There was no way I'd damage that image by turning to him or my children for help."
    angela.say "So he ended up driving me into [hero.name]'s arms, even as he tried to strengthen his hold on me."
    angela.say "It was only once we were together like that and facing my problems that our relationship truly blossomed."
    angela.say "In the chaos of it all, [hero.name] and I just kept on getting ever closer as my true self began to return."
    angela.say "And then there was the craziness of finding the evidence to prove what Dylan had been doing."
    angela.say "After that, [hero.name] and I were bonded in a way that could never be denied."
    angela.say "So now we have the life what we wanted together."
    angela.say "But I'm still struggling to make sense of just who I am."
    angela.say "Sometimes it feels like I'm still the girl I was in college."
    angela.say "Like I just woke up in the body of a mature woman."
    angela.say "Other times I worry that I don't have any personality at all."
    scene bg black with dissolve
    pause 1.0
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label angela_female_dom_01:
    "All it seems to take at the moment is for Angela to call or drop me a simple text message."
    "The slightest hint that she's got time to spare and wants to spend it with me."
    "And I just can't help myself, I drop everything and come running to meet her."
    "I don't know what it is exactly, there's just something about being around Angela."
    "The thrill of spending time with a mature, confident and beautiful women like her."
    "It's like nothing I've ever experienced with younger girls, or even older guys."
    scene bg coffeeshop with fade
    "And it's why I hurry to meet Angela as soon as she tells me she's free today."
    "Even though I make sure to get to the meeting place as quickly as I can, it's no good."
    show angela casual at center, zoomAt(1.25, (640, 880)) with fade
    "Angela still manages to beat me there and be waiting when I arrive."
    show bg coffeeshop at center, traveling (1.15, 0.5, (640, 800))
    show angela smile at center, traveling (1.5, 0.5, (640, 1040))
    "And she gives me a knowing smile as I walk up to greet her."
    show angela happy
    angela.say "Hello, [hero.name]..."
    angela.say "I'm so glad that you could come and meet me today."
    angela.say "It feels like so long since we were last together."
    show angela smile
    "I can't help putting on an ironic smile as Angela says this."
    "Because I know for a fact that it can't have been that long."
    bree.say "Hi, Angela..."
    bree.say "And you can stop trying to charm me like that, okay?"
    bree.say "You know as well as I do that we saw each other a couple of days ago!"
    show angela normal
    "Rather than admitting to her little deception, Angela instead looks thoughtful."
    show angela talkative
    angela.say "Is it really that short of a time?"
    angela.say "Ah, I guess it just feels that way to me."
    angela.say "Any time spent apart from you is starting to feel like an eternity, [hero.name]!"
    show angela normal
    "I instantly let out a giggle at Angela's gushing compliment."
    "Shaking my head as I can't believe what I'm hearing."
    bree.say "Okay, Angela..."
    bree.say "I like to be praised as much as the next girl."
    bree.say "But don't you think that's a little too much?"
    "Angela cocks her head on one side, neither nodding or shaking it."
    show angela smile
    "Which seems to tell me that she appreciates me seeing through her flattery."
    "But possibly doesn't totally agree with me claiming that it's all for show."
    show angela sadistic
    angela.say "Ah, young people today..."
    angela.say "You're all so smart and cynical!"
    show angela talkative
    angela.say "Anyway..."
    angela.say "That's not why I wanted to see you today."
    show angela smile
    "I suspected as much."
    "So I give Angela a nod."
    "And then I wait to hear what she has to say."
    show angela talkative
    angela.say "We've been getting along so well lately, [hero.name]..."
    angela.say "Really connecting and growing together."
    angela.say "Wouldn't you agree?"
    show angela normal
    "There's nothing in that statement that I'd disagree with."
    "So I give Angela another nod."
    bree.say "Of course, Angela..."
    bree.say "Every time we meet up I feel like I've had more fun than the last time."
    show angela smile
    "Angela gives me one of those slow, achingly beautiful smiles of hers."
    "At once letting me know that I've given her the exact answer she wanted."
    "But also cluing me in on how much she's enjoying the memories it's stirred for her."
    show angela happy
    angela.say "I feel the same way too, [hero.name]..."
    angela.say "So I wanted to give you a little something."
    angela.say "Just a small token of appreciation."
    angela.say "But something that makes our relationship official."
    show angela smile
    "Now my mind is really racing as I try to figure out what it could be."
    "Surely we're nowhere near the point in our relationship where Angela would be proposing to me?"
    "But then again, she is an older woman, and one that's already been married and raised kids."
    "Maybe she's not about to wait and see how things turn out in the long run?"
    "Perhaps Angela's wanting to grab onto the happiness she's found already?"
    "All of this is running through my head as she produces a gift-wrapped box."
    play sound [paper_ripping_2, paper_ripping_1]
    "I take it as Angela offers it to me, gingerly tearing off the paper."
    "Then I open it and pull out what's inside."
    bree.say "Oh my..."
    bree.say "It's a..."
    bree.say "A collar?!?"
    "Angela nods, still smiling."
    show angela happy
    angela.say "You've seemed so happy since I started taking charge of things, [hero.name]."
    angela.say "And it's felt very natural for me to start being the one to make the decisions."
    angela.say "I think we make a lot of sense in dominant and submissive roles."
    angela.say "Wouldn't you agree?"
    show angela normal
    menu:
        "Accept the collar":
            "I'm finding it hard to really listen to what Angela's saying right now."
            "Partly because I'm staring at the collar wit rewed interest."
            "And partly because everything is starting to fall into place."
            bree.say "Yeah, yeah, yeah..."
            bree.say "I get all of that, Angela..."
            bree.say "Can you just help me get this thing on?"
            show angela surprised
            "Angela seems surprised by my eagerness to wear the collar."
            "Which I guess means that she was expecting to have to explain herself in greater detail."
            show angela normal
            "But she hurries to help me with it all the same."
            show angela happy
            angela.say "Of course, [hero.name]..."
            angela.say "Just let me..."
            angela.say "Maybe if I come at it from this angle..."
            show angela smile
            "There are hands everywhere as we struggle to get the collar around my neck."
            "And most of the confusion comes from us both trying not to get in the other's way."
            "But eventually we manage to get the thing on me and fastened in place."
            bree.say "Oh, Angela..."
            bree.say "This is perfect."
            bree.say "You know, it just feels right."
            "Angela looks more relieved than surprised by now."
            "Because I guess giving me the collar was a real gamble."
            "If I hadn't been into it, then she'd most likely have been in deep trouble!"
            show angela happy
            angela.say "You see..."
            show angela talkative
            angela.say "I was always the one that was submissive in my marriage."
            show angela normal
            "I shake my head, cutting Angela off before she can apologise."
            bree.say "It's okay, Angela.."
            bree.say "You don't need to explain."
            bree.say "I never knew I wanted this before you gave me the collar."
            bree.say "But it all seems to make an odd kind of sense to me."
            bree.say "Like it was the missing piece of the puzzle."
            "Something occurs to me as I'm saying all of this."
            "And I can't help cocking my head on one side."
            bree.say "So..."
            bree.say "Does this mean I have to start calling you 'Mistress'?"
            show angela blush shy
            "Angela blushes visibly, finding it hard to meet my eye."
            show angela worried
            angela.say "Well, I..."
            angela.say "You don't have to at first..."
            angela.say "But maybe you could..."
            angela.say "I mean, if you really wanted to?"
            show angela normal
            bree.say "Oh, Angela..."
            bree.say "You're going to have to toughen up if you want to be my mistress!"
            "Angela answers this by staying silent and turning a darker shade of red."
            "And I can't help beginning to laugh at her awkward attempts to assert herself."
            $ hero.flags.collared = True
            $ angela.love += 5
        "Refuse the collar":
            "I'm already shaking my head as I thrust the collar back into Angela's hands."
            "And the action seems to take her completely by surprised, her eyes going wide."
            show angela surprised
            angela.say "[hero.name]..."
            angela.say "What..."
            angela.say "What are you doing?"
            show angela normal
            bree.say "What does it look like, Angela?"
            bree.say "I'm turning your gift down!"
            show angela sad
            "Angela looks down at the collar in her hands."
            "Then she looks back up at me, shaking her head in confusion."
            show angela worried
            angela.say "But, [hero.name]..."
            angela.say "I don't understand..."
            angela.say "I thought you liked me being the one in charge?"
            show angela sad
            "Oh my god..."
            "How could she read my signals and get them so wrong?"
            bree.say "Angela, I like the way you're more mature than me, more confident."
            bree.say "It makes me feel safe around you."
            bree.say "Like I can trust you to take charge when I need you too."
            bree.say "But that doesn't mean I want you to take over my entire life!"
            show angela fragile
            "Angela looks like she's trying to think up a counter-argument."
            "Her hands clutching at the collar as she listens to what I have to say."
            "But when she does speak up for herself, she's not as authoritative as before."
            show angela worried
            angela.say "I..."
            angela.say "I'm sorry, [hero.name]..."
            angela.say "I was always the one that was submissive in my marriage."
            angela.say "Perhaps I let being the older partner in out relationship go to my head?"
            show angela fragile
            "She sighs and turns on her heel."
            show angela worried
            angela.say "I think I need to take some time to think this over."
            angela.say "Because I don't like misreading you this badly."
            show angela fragile
            "The best I can do is offer Angela a weak smile."
            $ angela.love -= 5
            hide angela with easeoutright
            "That and to watch her as she walks away in silence."
            "All the while hoping that this isn't an insurmountable obstacle to our relationship."
    scene bg black with dissolve
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
