init python:
    Event(**{
    "name": "kylie_event_02",
    "label": "kylie_event_02",
    "duration": 1,
    "conditions": [
        IsDone("kylie_event_01"),
        IsDayOfWeek(2, 5),
        HeroTarget(
            IsGender("male"),
            IsRoom("university"),
            MinStat("charm", 30),
            Not(IsFlag("kylie_event_02_delay"))
            ),
        ],
    "music": "music/roa_music/dreamy.ogg",
    "do_once": True,
    "once_day": True,
    })

    Event(**{
    "name": "kylie_start",
    "label": "kylie_start",
    "conditions": [
        IsDone("kylie_event_02"),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Activity(**{
    "name": "call_kylie",
    "display_name": "Call Kylie",
    "label": "kylie_event_03",
    "conditions": [
        IsDone("kylie_event_02"),
        IsHour(19, 0),
        PersonTarget(kylie,
            Not(IsPresent()),
            Not(IsFlag("schedule", "jail")),
            MinStat("love", 40),
            ),
        ],
    "music": "music/roa_music/dreamy.ogg",
    "do_once": True,
    "icon": "kylie",
    })

    Event(**{
    "name": "kylie_event_04",
    "duration": 1,
    "conditions": [
        IsDone("call_kylie"),
        HeroTarget(
            IsGender("male"),
            IsActivity("talk", "sweet_talk")),
        PersonTarget(kylie,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActive()),
            Not(IsFlag("schedule", "jail")),
            MinStat("love", 50),
            ),
        PersonTarget(minami,
            Not(IsActive())
            ),
        ActiveTarget(
            MinStat("love", 50)
            ),
        ],
    "label": "kylie_event_04",
    "music": "music/roa_music/dreamy.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "kylie_event_05",
    "duration": 1,
    "conditions": [
        IsDone("kylie_event_04", "alexis_event_01"),
        PersonTarget(kylie,
            IsPresent(),
            Not(IsHidden()),
            HasRoomTag("uni"),
            IsFlag("nextevent", False),
            IsFlag("jealouspath", False),
            Not(IsFlag("schedule", "jail")),
            ),
        ],
    "label": "kylie_event_05",
    "music": "music/roa_music/dreamy.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "kylie_event_06",
    "duration": 1,
    "conditions": [
        IsDone("kylie_event_04"),
        IsHour(22, 4),
        HeroTarget(IsRoom("bedroom1")),
        PersonTarget(kylie,
            Not(IsPresent()),
            IsFlag("nextevent", False),
            IsFlag("jealouspath"),
            Not(IsFlag("schedule", "jail")),
            ),
        ],
    "label": "kylie_event_06",
    "music": "music/darren_curtis/come_out_and_play.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "kylie_event_07a",
    "label": "kylie_event_07a",
    "duration": 1,
    "conditions": [
        Or(
            IsDone("kylie_event_05"),
            IsDone("kylie_event_06"),
           ),
        PersonTarget(kylie,
                     IsActive(),
                     MinStat("love", 80),
                     MaxStat("yandere", 24),
                     Not(
                         And(
                             IsFlag("schedule", "jail"),
                             IsFlag("cantgetbetter", False),
                            )
                        )
                    ),
        ],
    "music": "music/roa_music/dreamy.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "kylie_event_07b",
    "label": "kylie_event_07b",
    "duration": 1,
    "conditions": [
        Or(
            IsDone("kylie_event_05"),
            IsDone("kylie_event_06")
            ),
        PersonTarget(kylie,
            IsActive(),
            MinStat("love", 80),
            MinStat("yandere", 25),
            Not(IsFlag("schedule", "jail"))
            ),
        ],
    "music": "music/darren_curtis/come_out_and_play.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "kylie_event_08a",
    "label": "kylie_event_08a",
    "duration": 1,
    "conditions": [
        IsDone("kylie_event_07a"),
        HeroTarget(IsRoom("coffeeshop")),
        PersonTarget(kylie,
            Not(IsHidden()),
            IsRoom("coffeeshop"),
            MinStat("love", 100),
            MaxStat("yandere", 24),
            Not(IsFlag("schedule", "jail")),
            IsFlag("cantgetbetter", False),
            IsFlag("nextevent", False)
            ),
        ],
    "music": "music/roa_music/dreamy.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "kylie_event_08b",
    "label": "kylie_event_08b",
    "duration": 1,
    "conditions": [
        Or(
            IsDone("kylie_event_07a"),
            IsDone("kylie_event_07b")
            ),
        IsHour(14, 18),
        HeroTarget(IsRoom("bedroom1")),
        PersonTarget(kylie,
            Not(IsHidden()),
            MinStat("love", 100),
            MinStat("yandere", 25),
            IsFlag("nextevent", False),
            Not(IsFlag("schedule", "jail")),
            ),
        ],
    "music": "music/darren_curtis/come_out_and_play.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "kylie_event_09a",
    "label": "kylie_event_09a",
    "duration": 1,
    "conditions": [
        IsDone("kylie_event_08a"),
        PersonTarget(kylie,
            IsActive(),
            MinStat("love", 120),
            MaxStat("yandere", 24),
            IsFlag("nextevent", False),
            IsFlag("cantgetbetter", False),
            Not(IsFlag("schedule", "jail")),
            ),
        ],
    "music": "music/roa_music/dreamy.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "kylie_event_09b",
    "label": "kylie_event_09b",
    "duration": 1,
    "conditions": [
        IsDone("kylie_event_08b"),
        IsHour(23, 4),
        HeroTarget(IsRoom("bedroom1")),
        PersonTarget(kylie,
            Not(IsHidden()),
            MinStat("love", 120),
            MinStat("yandere", 35),
            IsFlag("nextevent", False),
            Not(IsFlag("schedule", "jail")),
            ),
        ],
    "music": "music/darren_curtis/come_out_and_play.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "kylie_event_10a",
    "label": "kylie_event_10a",
    "duration": 1,
    "conditions": [
        IsDone("kylie_event_09a"),
        PersonTarget(kylie,
            IsActive(),
            MinStat("love", 150),
            MaxStat("yandere", 24),
            IsFlag("nextevent", False),
            IsFlag("cantgetbetter", False),
            Not(IsFlag("schedule", "jail")),
            ),
        ],
    "music": "music/roa_music/dreamy.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "kylie_event_10b",
    "label": "kylie_event_10b",
    "duration": 1,
    "conditions": [
        IsDone("kylie_event_09b"),
        IsHour(20, 23),
        HeroTarget(IsRoom("bedroom1")),
        PersonTarget(kylie,
            Not(IsHidden()),
            MinStat("yandere", 60),
            IsFlag("nextevent", False),
            Not(IsFlag("schedule", "jail")),
            ),
        Not(
            And(
                PersonTarget(bree,
                    Or(
                        IsHidden(),
                        IsGone()
                        ),
                    ),
                PersonTarget(sasha,
                    Or(
                        IsHidden(),
                        IsGone()
                        ),
                    ),
                ),
            ),
        ],
    "music": "music/darren_curtis/come_out_and_play.ogg",
    "do_once": True,
    })

    Activity(**{
    "name": "kylie_event_11b",
    "display_name": "Find and confront Kylie",
    "label": "kylie_event_11b",
    "conditions": [
        IsDone("kylie_event_10b"),
        IsHour(14, 22),
        PersonTarget(kylie,
            Not(IsHidden()),
            Not(IsPresent()),
            MinStat("yandere", 75),
            IsFlag("nextevent", False),
            Not(IsFlag("schedule", "jail")),
            ),
        ],
    "music": "music/darren_curtis/come_out_and_play.ogg",
    "icon": "kylie",
    "do_once": True,
    "quit": True
    })

    Event(**{
    "name": "kylie_classroom_bj",
    "label": "kylie_classroom_bj",
    "once_week": True,
    "max_girls": 1,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("study_with"),
            ),
        PersonTarget(kylie,
            IsPresent(),
            Not(IsHidden()),
            IsRoom("classroom"),
            MinStat("love", 140),
            MinStat("sub", 35)
            ),
        ],
    "music": "music/roa_music/dreamy.ogg",
    })


    Event(**{
    "name": "kylie_yandere",
    "conditions": [
        HeroTarget(IsActivity(
            "kiss",
            "slap_ass",
            "talk",
            "sweet_talk",
            "offer_a_drink",
            "ask_birthday",
            "ask_number",
            "cinema_with",
            "dance_with",
            "gift",
            "pet",
            )),
        PersonTarget(kylie,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActive()),
            MinStat("love", 25),
            ),
        ],
    "label": "kylie_yandere",
    "do_once": False,
    "cancel_activity": False,
    "quit": False,
    })

    Event(**{
    "name": "kylie_preg_talk",
    "label": "kylie_preg_talk",
    "do_once": False,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(kylie,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("toldpreg", False),
            MinCounter("pregnant", 6),
            ),
        ],
    "music": "music/roa_music/dreamy.ogg",
    })

    Event(**{
    "name": "kylie_attack",
    "duration": 2,
    "priority": 1000,
    "conditions": [
        IsHour(0, 6),
        HeroTarget(IsRoom("house")),
        PersonTarget(kylie,
            IsPresent(),
            Not(IsHidden()),
            Not(IsFlag("schedule", "jail")),
            MinFlag("hasRun", 1),
            MaxCounter("pregnant", 0),
            MinStat("love", 100),
            MinStat("yandere", 50),
            ),
        ],
    "label": "kylie_attack",
    "music": "music/darren_curtis/come_out_and_play.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "kylie_run",
    "do_once": False,
    "priority": 900,
    "conditions": [
        IsHour(0, 6),
        HeroTarget(IsRoom("house")),
        PersonTarget(kylie,
            IsPresent(),
            Not(IsHidden()),
            Not(IsFlag("schedule", "jail")),
            ),
        ],
    "label": "kylie_run",
    })

    Event(**{
    "name": "kylie_unRun",
    "do_once": False,
    "conditions": [
        IsHour(7, 0),
        PersonTarget(kylie,
            IsFlag("run"),
            Not(IsFlag("runDelay")),
            ),
        ],
    "label": "kylie_unRun",
    "quit": False,
    })

    Event(**{
    "name": "kylie_stop_pill",
    "do_once": False,
    "conditions": [
        PersonTarget(kylie,
            IsFlag("pill"),
            MinStat("love", 180),
            MaxStat("sub", 89),
            MinStat("yandere", 50),
            ),
        ],
    "label": "kylie_stop_pill",
    "once_week": True,
    "quit": False,
    })

    Event(**{
    "name": "kylie_rattle",
    "label": "kylie_rattle",
    "conditions": [
        IsNotDone("kylie_attack"),
        HeroTarget(HasRoomTag("home")),
        PersonTarget(kylie,
            Not(IsHidden()),
            IsRoom("house"),
            IsFlag("nostalking", False),
            Not(IsFlag("schedule", "jail")),
            MinStat("yandere", 25),
            ),
        ],
    "music": "music/darren_curtis/come_out_and_play.ogg",
    "do_once": False,
    "once_day": True,
    })

    Activity(**{
    "name": "kylie_investigation_2",
    "display_name": "Report Kylie",
    "label": "kylie_investigation_2",
    "duration": 2,
    "rooms": "policestation",
    "conditions": [
        IsHour(9, 19),
        PersonTarget(kylie,
            Not(IsHidden()),
            IsFlag("policestation"),
            ),
        ],
    "do_once": True,
    "icon": "kylie",
    })

    Event(**{
    "name": "kylie_investigation_3",
    "label": "kylie_investigation_3",
    "conditions": [
        IsDone("kylie_investigation_2"),
        IsHour(11, 14),
        HeroTarget(IsFlag("kylieinvestigationdelay", False)),
        PersonTarget(kylie,
            Not(IsHidden()),
            IsFlag("arrest"),
            ),
        ],
    "priority": 500,
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "kylie_voyeur_confront",
    "display_name": "Confront Kylie",
    "label": "kylie_voyeur_confront",
    "conditions": [
        IsDone("kylie_voyeur"),
        HeroTarget(IsGender("male")),
        PersonTarget(kylie,
            IsActive(),
            ),
        ],
    "do_once": True,
    "icon": "button_alexis",
    })

    Event(**{
    "name": "kylie_camera",
    "label": "kylie_camera",
    "duration": 1,
    "priority": 500,
    "do_once": True,
    "conditions": [
        IsHour(10, 18),
        HeroTarget(
            IsRoom("livingroom"),
            IsFlag("kyliecameraplaced"),
            IsFlag("kyliecameradelay", False),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            HasRoomTag("home")
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            HasRoomTag("home")
            ),
        ],
    })

    Event(**{
    "name": "kylie_bree_confrontation",
    "priority": 500,
    "conditions": [
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            ),
        PersonTarget(kylie,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("target", "bree"),
            Not(IsFlag("schedule", "jail")),
            MinStat("love", 50),
            MinStat("yandere", 50),
            ),
        ],
    "label": "kylie_bree_confrontation",
    "music": "music/darren_curtis/come_out_and_play.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "kylie_breakup_1",
    "label": "kylie_breakup_1",
    "priority": 500,
    "conditions": [
        PersonTarget(kylie,
            IsPresent(),
            Not(IsHidden()),
            HasRoomTag("mall_southside"),
            Or(IsFlag("friendzone"), IsFlag("breakup")),
            Not(IsFlag("breakupDelay"))
            ),
        ],
    "music": "music/darren_curtis/come_out_and_play.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "kylie_breakup_2",
    "label": "kylie_breakup_2",
    "priority": 500,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            ),
        IsTimeOfDay("afternoon"),
        IsDone("kylie_breakup_1"),
        PersonTarget(kylie,
            Not(IsFlag("breakupDelay"))
            ),
        PersonTarget(alexis,
            Not(IsPresent()),
            Not(IsHidden()),
            ),
        ],
    "music": "music/darren_curtis/come_out_and_play.ogg",
    "do_once": True,
    "once_month": True,
    })

    Event(**{
    "name": "kylie_hypnosis_crazy",
    "label": "kylie_hypnosis_crazy",
    "priority": 500,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(kylie,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("on_hypnosis_craze", False),
            MinFlag("yandere_hypnosis_adjustments", 3),
            ),
        ],
    "music": "music/darren_curtis/come_out_and_play.ogg",
    "do_once": False,
    })

    Event(**{
    "name": "kylie_yandere_hypnosis_backlash",
    "label": "kylie_yandere_hypnosis_backlash",
    "priority": 500,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(kylie,
            IsFlag("yandere_hypnosis_backlash"),
            ),
        ],
    "music": "music/darren_curtis/come_out_and_play.ogg",
    "once_day": True,
    })

    InteractEvent(**{
    "name": "kylie_prison_visit_1",
    "priority": 500,
    "label": "kylie_prison_visit_1",
    "conditions": [
        IsDone("camila_prison_visit_1"),
        HeroTarget(
            IsGender("male"),
            IsRoom("jail"),
            ),
        PersonTarget(kylie,
            IsActive(),
            IsFlag("schedule", "jail"),
            MinStat("love", 100),
            ),
        ],
    "music": "music/roa_music/hero.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "kylie_trial_1",
    "priority": 1500,
    "label": "kylie_trial_1",
    "conditions": [
        "'kylie_investigation_3' in DONE and game.days_played >= DONE['kylie_investigation_3'] + 20",
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom"),
            ),
        PersonTarget(kylie,
            Not(IsHidden()),
            IsFlag("schedule", "jail"),
            Not(IsFlag("killed", False)),
            ),
        ],
    "music": "music/darren_curtis/come_out_and_play.ogg",
    "do_once": True,
    })


label kylie_yandere_hypnosis_backlash:
    "Thinking back on Kylie's outburst still gives me chills..."
    $ kylie.yandere += 20
    $ kylie.flags.yandere_hypnosis_backlash -= 1
    if kylie.flags.yandere_hypnosis_backlash == 0:
        $ kylie.flags.yandere_hypnosis_adjustments = 0
        $ kylie.flags.on_hypnosis_craze = False
    return

label kylie_hypnosis_crazy:
    $ kylie.flags.on_hypnosis_craze = True
    "I should have known it was too good to be true."
    show kylie yandere
    "Kylie turns to me with a crazed look in her eye"
    kylie.say "You thought you could control me like that [hero.name]??"
    kylie.say "I guess I need to show you even harder how much I love you, and how much you {i}WILL{/i} come to love me..."
    $ kylie.yandere += 20
    $ kylie.flags.yandere_hypnosis_backlash = 2
    return

label kylie_breakup_2:
    play sound cell_vibrate loop
    "The sensation of my phone vibrating in my pocket distracts me from what I'm doing."
    "I absently pluck it out and look at the caller ID, wondering who it could be."
    "But when I notice that it's Alexis, my interest is suddenly aroused."
    stop sound
    $ result = renpy.call_screen("smartphone_choice", "Alexis")
    if not result:
        $ hero.cancel_event()
        $ alexis.love -= 5
        return
    mike.say "Hey, Alexis..."
    mike.say "I haven't heard from you in a while!"
    mike.say "What can I do for you?"
    "My tone's upbeat and positive, betraying my interest in Alexis."
    "But as soon as I hear her reply, I know that she's not in the same place, not at all."
    "Instead, Alexis sounds quiet and more than a little emotional on the other end of the line."
    alexis.say "H...hey, [hero.name]..."
    alexis.say "Sorry to call you out of the blue like this..."
    alexis.say "But there's something I think you should know."
    "I take a deep breath and shake off my previously positive mood."
    "This sounds super heavy, like I should be sitting down or something."
    mike.say "Okay, Alexis..."
    mike.say "I'm listening."
    alexis.say "No..."
    alexis.say "This isn't something I can say over the phone..."
    "Alexis pauses for a moment, obviously pondering the situation."
    "I choose to keep quiet while she does so, giving her the space she needs."
    alexis.say "I know..."
    alexis.say "Can you come meet me somewhere?"
    alexis.say "Maybe we can talk better over a coffee?"
    mike.say "Sure thing, Alexis..."
    mike.say "I'll be right there."
    "We agree on a nearby coffee shop and then Alexis ends the call."
    "Which leaves me hurrying to meet her."
    "That and wondering what the hell she has to tell me!"
    show bg coffeeshop with fade
    "I get to the coffee shop as soon as I can."
    show alexis b sad at center, zoomAt(1, (340, 840)) with dissolve
    "But somehow Alexis still beats me there."
    "I'm wondering if she was here all the time."
    "Then I forget everything on my mind as I see that she's red-eyed."
    "Has Alexis actually been crying?"
    "I hurry over to her table and sit down."
    show bg coffeeshop at center, zoomAt(1.5, (340, 940))
    show alexis a sad at center, zoomAt(1.5, (640, 1140))
    "As I do so, Alexis looks up at me."
    "And I can see that I was right."
    "She has been crying - and by the looks of it, a lot!"
    mike.say "Alexis, I came as soon as I could..."
    mike.say "What's the matter?"
    mike.say "Why have you been crying?"
    "Rather than getting me the answer I wanted, this seems to set Alexis off again."
    show alexis b cry
    "She's blubbering uncontrollably, and I can see instantly that it's not put-on."
    "Whatever's upsetting her is one hundred percent genuine in nature."
    "I hastily grab a handful of paper napkins and offer them to Alexis."
    "Yeah, I know it's a lame thing to do."
    "But Alexis takes them all the same."
    "She dabs her eyes and then blows her nose."
    "The sound of which is quite impressive."
    show alexis b sad
    alexis.say "Oh..."
    alexis.say "Oh dear..."
    alexis.say "Thanks for coming, [hero.name]."
    alexis.say "And sorry I'm such a mess!"
    mike.say "No need to apologise, Alexis."
    mike.say "Just tell me what's happened, okay?"
    mike.say "What's gotten you into this state?"
    "Alexis nods and proceeds to blow her nose again."
    "I try to force a smile onto my face and ignore the liquid, bubbling sound she makes."
    alexis.say "It's..."
    alexis.say "It's Kylie..."
    mike.say "Oh god, Alexis!"
    mike.say "What's she done now?"
    mike.say "And who's she done it to?"
    "The words are out of my mouth before I realise what I'm saying."
    "I'm just so used to expecting to find that Kylie's done something crazy."
    "I don't for a moment think that it could be anything else."
    "Alexis shakes her head at me, looking even more distraught."
    "But thankfully, she's currently in a state of emotional turmoil."
    "So she doesn't seem to catch onto the full implications of what I just said."
    show alexis cry
    alexis.say "No, [hero.name]!"
    alexis.say "It's not what Kylie's done to someone else."
    alexis.say "It's what she's done to herself!"
    show alexis sad
    "Instantly images of extreme self-harm flood my mind."
    "I've learned the hard way that Kylie's prone to such things."
    "That she can act out on the troubled thoughts in her mind."
    "So I'm already preparing myself for what I think is the worst."
    "But then Alexis tops anything that I could have imagined myself."
    show alexis cry
    alexis.say "[hero.name]..."
    alexis.say "Kylie..."
    alexis.say "She...she killed herself!"
    show alexis sad
    "For a moment the words mean nothing to me."
    "They're just a collection of random sounds."
    "Then it hits me like a punch in the gut."
    mike.say "Alexis..."
    mike.say "What are you saying?"
    mike.say "That Kylie's...that she's dead?!?"
    "Of course it's a totally dumb question."
    "But I'm stunned by the news and struggling to process it."
    "Luckily for me, Alexis is in a similar place too."
    "Which means that she takes the question at face value."
    show alexis cry
    alexis.say "Yeah, [hero.name]..."
    alexis.say "My little sister's gone!"
    alexis.say "Slashed her wrists with that DAMN box-cutter of hers!"
    show alexis sad
    "I slump back in my chair, shaking my head in disbelief."
    "All I can think of is how recently I saw Kylie at the mall."
    "But then I recall how awful she looked, how she was like a zombie."
    "Already I can feel the guilt churning up my stomach."
    "I could have said something to her then."
    "Or I could have called Alexis and warned her."
    "Why didn't I do any of that?"
    "I was just relieved to get away from Kylie at the time."
    "I didn't want to have to handle anymore of her bullshit."
    "Well I don't have to worry about that anymore - nobody does."
    "Now I just have to live with the guilt that I stood back and did nothing!"
    mike.say "I...I don't know what to say!"
    mike.say "Couldn't they do anything to save her?"
    "Alexis shakes her head at this."
    show alexis cry
    alexis.say "She was gone when we found her."
    alexis.say "I...I think she planned it that way."
    alexis.say "She must have known nobody would find her in time..."
    "Alexis stops and shakes her head."
    alexis.say "Sorry, [hero.name]..."
    alexis.say "You don't need to know all the gory details."
    alexis.say "I only called you to tell you all of this because you were close."
    show alexis sad
    "There it is - another punch to the gut!"
    mike.say "Y...yeah, Alexis..."
    mike.say "Kylie and I...we were friends!"
    show alexis normal
    "Alexis gives me a wan smile."
    "And there's a knowing look in her eye too."
    alexis.say "Oh, stop it, [hero.name]!"
    alexis.say "I know we have history, you and me."
    alexis.say "But you don't have to protect my feelings."
    alexis.say "I know exactly how Kylie felt about you."
    alexis.say "How could I not - she was my sister!"
    alexis.say "And she was so happy when the two of you started getting closer, you know?"
    "I nod in agreement."
    "But I already feel like the worst man alive."
    alexis.say "She really seemed to be turning a corner after that."
    alexis.say "And sure, I was a little jealous at first."
    alexis.say "But then I got over it, and I was just happy for the both of you."
    show alexis sad
    alexis.say "Though I guess her issues were just too big for it to make a difference!"
    "Oh fuck..."
    "Alexis is talking like Kylie and I never broke things off!"
    "Did Kylie never tell Alexis and her family what happened between us?"
    "That we ended it on a very bad note and she was devastated?"
    mike.say "She..."
    mike.say "She affected me in a big way..."
    mike.say "I never met a girl quite like Kylie before!"
    "Alexis nods and reaches out to put her hand atop mine."
    "She wears a sad smile as she does so."
    "A fact which only serves to make me feel that much worse."
    alexis.say "It's okay, [hero.name], I understand."
    alexis.say "And I'm here for you - you know that, right?"
    alexis.say "Any time you need to talk about your feelings, just call me."
    alexis.say "Even if you just need someone to be with you, I'm always here."
    alexis.say "I think we could both use a friend right now!"
    mike.say "Th...thanks, Alexis!"
    mike.say "I just might do that."
    "Alexis smiles again."
    "But then her phone makes a sound and she frowns a little."
    alexis.say "I have to get that, [hero.name] - sorry!"
    mike.say "No worries, Alexis."
    mike.say "I should get going too."
    mike.say "You must have like a million things to handle!"
    scene bg coffeeshop with dissolve
    "I stand up and give Alexis a wave as I turn to leave."
    "She returns the gesture and then begins to fiddle with her phone."
    "And I take that as the perfect opportunity to hurry out of the coffee shop."
    scene bg street with fade
    "I'm still reeling from the news as I walk back home."
    "Of all the crazy things Kylie was capable of..."
    "I never thought she'd do something like that!"
    return

label kylie_breakup_1:
    "It's weird when you're just walking along and, out of nowhere, something catches your eye."
    "No matter what it is, you're caught off-guard, thrown until you can make some sense of it."
    "That very thing just happened to me a moment ago, and now I'm totally off-balance."
    "I was just minding my own business, strolling around the mall like all the other shoppers."
    "But now I'm standing still as I survey the crowd, looking for what caught my eye."
    "I'm sure it was a familiar face, someone that I should know on sight."
    "So why in the hell am I so confused right now?"
    "Why didn't I recognise them when I saw them?"
    "I start moving in the direction that I thought they were going in."
    "At the same time I'm scanning the faces around me, looking for a match."
    "I don't think there's any chance of me identifying the person in question."
    "But then I see one particular girl walking along on the very edge of the crowd."
    show kylie b hoodie annoyed hoodup at right, dark with dissolve
    "She's wearing a shabby hoody and shapeless sweat-pants."
    "And she's hunched over too, like she doesn't want to be seen."
    "Yet there's just something so familiar about the way she walks."
    "And I hate to admit this - but her ass looks pretty familiar too!"
    "Part of me wants to just leave it."
    "After all, chances are it's nobody I actually know."
    "But I'm not hurrying to be anywhere right now."
    "So I guess checking it out wouldn't be a total waste of my time."
    hide kylie
    show kylie b hoodie annoyed hoodup
    "I hurry over and get in front of the girl in the hoodie."
    "Even this close it's hard to get a look at her face."
    "She has the hood pulled down and she's gazing almost straight at the ground!"
    mike.say "Erm..."
    mike.say "Hey there!"
    "I'm trying to keep pace with the girl as she walks on."
    "But my greeting doesn't even seem to register with her."
    "Instead she keeps right on walking."
    "I don't know if she's got earbuds in or something."
    "Maybe she's just deliberately ignoring me."
    "Either way this makes me feel a little annoyed."
    "So I step into her path and try again."
    mike.say "Hey!"
    mike.say "I said hello!"
    show kylie hoodie at center, zoomAt(2, (640, 1380)) with hpunch
    "A moment later, the girl literally walks into me."
    show kylie hoodie at center, zoomAt(1.5, (640, 1040)) with hpunch
    "She's not going too fast, so all that happens is that we both stagger back a little."
    "But at least she stops in her tracks and looks up at me for the first time."
    hide kylie
    show kylie hoodie y hoodup annoyed at center, zoomAt(1.25, (640, 880))
    "And when she does, I have to take another step back in sheer surprise."
    show kylie annoyed hoodie hooddown
    mike.say "Kylie?!?"
    mike.say "Is that really you?"
    show kylie b
    "You might think I'm just being a bit dramatic here."
    "That Kylie just couldn't be bothered to do herself up today."
    "That she just slobbed down to the mall in her sweat-pants and hoodie - so what?"
    "But this is nothing of the sort, I assure you!"
    "Whenever I saw Kylie in the past, she took a genuine pride in her appearance."
    "Hair, make-up and clothes - all of them were immaculate, wherever she was."
    "Now she's staring at me blankly, her face devoid of make-up."
    "There are red rims around her eyes, bags under them too."
    "I swear I can see the remnants of food around her mouth."
    "And her hair is hanging in lank tangles."
    "Like it's not been washed or brushed in ages."
    show kylie whining
    kylie.say "Wha..."
    kylie.say "Huh?"
    show kylie annoyed
    "Kylie's eyes are glazed over, like she can't actually see me."
    "And her expression is vacant, as if she's sedated or on something."
    mike.say "Holy shit!"
    mike.say "Kylie - what the hell happened to you?!?"
    "I wave a hand in front of Kylie's face."
    "I even snap my fingers in an effort to get a response."
    show kylie sad
    "Slowly, Kylie seems to come out of her trance."
    "Her eyes focus on my hand and then on my face."
    "But all the same, she still looks very confused."
    show kylie sadhappy
    kylie.say "Eurgh..."
    kylie.say "[hero.name]?"
    kylie.say "Is that really you?"
    show kylie whining
    kylie.say "Oh shit - don't tell me I'm seeing things again!"
    kylie.say "I shouldn't have stopped taking my meds!"
    show kylie sad
    "Every word that comes out of Kylie's mouth fills me with dread."
    "What could have happened to make her into such a mess?"
    "And the mere mention of drugs makes me think the worst."
    "Has she actually turned into a junkie since I last saw her?"
    mike.say "Yeah, it's me, Kylie!"
    mike.say "You're not hallucinating, I promise."
    mike.say "Well...unless you're seeing other shit aside from me."
    mike.say "Like pink elephants and all that stuff - I can't account for that!"
    show kylie normal
    "As I'm speaking I can see change coming over Kylie."
    "It's like her expression is going from confusion to vague recognition."
    "She nods as the fog seems to clear a little."
    show kylie shout
    kylie.say "Oh...that has to be you for real."
    kylie.say "I'd know that babbling anywhere!"
    show kylie normal
    "Choosing to ignore the implied insult, I press Kylie again."
    mike.say "What's with all this, Kylie?"
    "I gesture at her clothes and hair."
    mike.say "You look like you've been sleeping rough!"
    show kylie annoyed
    "Kylie looks down at herself, like she's seeing it for the first time."
    show kylie happy at startle
    "But rather than being shocked, she just chuckles and shakes her head."
    show kylie sadhappy
    kylie.say "Whoa!"
    kylie.say "I didn't realise it'd gotten this bad!"
    kylie.say "I guess my nose just got used to the smell too!"
    show kylie annoyed
    "I look at her in sheer amazement."
    mike.say "You're not bothered about how you look?"
    mike.say "You're a mess, Kylie!"
    mike.say "Why are you doing this to yourself?"
    show kylie sadhappy at startle
    "Kylie just sighs, shrugs and then lets out a chuckle of laughter."
    show kylie whining
    kylie.say "Ah..."
    kylie.say "Things have been a little tough recently, [hero.name]."
    kylie.say "You see there was this guy I was really into."
    kylie.say "I pinned everything on him...but he broke my heart!"
    show kylie sad
    "I open my mouth, meaning to call the guy a scumbag."
    "But then I realise who Kylie's actually talking about."
    mike.say "Oh..."
    mike.say "I see..."
    mike.say "For what it's worth, Kylie - I'm sorry!"
    show kylie annoyed
    "Kylie shakes her head and waves away my apology."
    "Much to my surprise, she doesn't seem mad at all."
    "Instead it's like she's too drained to do be anything but apathetic towards me."
    show kylie whining
    kylie.say "Nah...no...no way."
    show kylie sadhappy
    kylie.say "I should be the one thanking you!"
    kylie.say "It was you that gave me the kick in the ass I needed."
    kylie.say "You telling me to get lost was the wake-up call that saved me."
    show kylie normal
    "I can't help staring at Kylie as she says all of this."
    "It's hard to imagine that this is what recovery looks like!"
    mike.say "If you say so, Kylie..."
    mike.say "Is there anything I can do to help?"
    show kylie whining
    kylie.say "Oh no...no way!"
    kylie.say "You've already done more than enough."
    kylie.say "Sure, I'm not doing too well emotionally...or mentally either!"
    kylie.say "And I've been pretty depressed too!"
    kylie.say "But you have to hit rock bottom before you can start to climb again."
    show kylie sadhappy
    kylie.say "Am I right?"
    show kylie normal
    "I nod slowly, too worried by what I'm hearing to do anything else."
    mike.say "Well..."
    mike.say "I should really get going!"
    mike.say "I have to do something...or be somewhere!"
    show kylie happy
    kylie.say "Okay, [hero.name]..."
    show kylie talkative
    kylie.say "It was nice to see you."
    kylie.say "To see that you're doing so well..."
    hide kylie with dissolve
    "I'm already turning and starting to walk away from Kylie as I say all of this."
    "The truth is that I want to get as far away from her as I can right now."
    "The mess that she's in and the way that she's talking is scaring me."
    "Plus I can't help feeling more than a little guilty too."
    "I mean, I was definitely the one in the right when I told her to get lost."
    "But I can't deny that what I did definitely played a big part in all of this."
    "Luckily for me, Kylie just stands there and watches me run away."
    "All the time her face is as blank as it was when I first saw her."
    "And even when she's out of sight, I can still feel her staring after me."
    "It's like her eyes are boring two holes in the back of my head!"
    $ kylie.flags.breakupDelay = TemporaryFlag(True, 3)
    $ kylie.set_gone_forever()
    return

label kylie_bree_confrontation:
    "I don't normally hang around if I hear the sound of raised voices that can only mean two people are having an argument nearby."
    "And I certainly don't make a habit of stopping to see if there's a chance to overhear whatever the cause of the disagreement might be."
    "But both of those things are usually predicated on the assumption that those arguing are strangers and the subject can't have anything at all to do with me."
    "I swear that's the only reason that I find myself stopping in my tracks as I hurry from one lecture to another at college this morning."
    "I recognise both of the angry voices almost instantly, though it takes me sneaking closer to be able to see just who exactly they belong to."
    show kylie angry at left5
    show bree a annoyed at right4
    with dissolve
    "And as I do this, I see that the argument I've stumbled upon is between [bree.name] and Kylie, of all people!"
    "Well, I say that it's an argument for want of a better word."
    "Because right now, it seems a lot more like Kylie yelling at a very surprised and rather frightened [bree.name]."
    "I'm already in two minds as to whether I should step out of hiding and intervene, or else walk away and leave them to it."
    "Understand that I'm not afraid to break it up, but as far as I know, this is just a weird coincidence and it's none of my business."
    "Sure, a gentleman would step in and make sure nobody got hurt."
    "But a modern man knows that sometimes it's best to let girls fight their own battles - especially when it's with another girl!"
    show kylie vangry at left4 with ease
    kylie.say "I tried to smarten you up the gentle way."
    kylie.say "But you're obviously too dumb to get the message."
    show kylie angry
    show bree b angry at right4, hshake
    "I watch as Kylie grabs a handful of [bree.name]'s hair and twists it mercilessly, making me wince in sympathy."
    show bree b vangry
    bree.say "Ahh...shit..."
    bree.say "What are you even talking about, you mad bitch?!?"
    show bree b angry
    show kylie vangry at left4, vshake
    kylie.say "Don't play the innocent with me, you nasty old sow!"
    kylie.say "You'd better keep away from [hero.name] from now on, or else you'll get what's coming to you."
    show kylie angry
    "Did I just hear that right?"
    "Is this whole thing over me?"
    "Part of me feels instantly flattered and more than a little turned on at the idea."
    "But then another round of screams from [bree.name] reminds me that this might not be the proper time and place to be gloating..."
    menu:
        "Help [bree.name]":
            mike.say "Kylie, what do you think you're doing to my housemate?"
            $ kylie.yandere += 10
            $ bree.love += 10
            $ kylie.sub += 5
            "I step out of my hiding place as both of the girls glance in the direction of my voice."
            show bree normal
            "[bree.name] looks instantly relieved to see me, though she might have had a similar reaction to any potential saviour right about now."
            show kylie surprised at left5 with ease
            "In contrast, Kylie looks momentarily confused, as though I've caught her breaking character and she doesn't know what to do about it."
            kylie.say "[hero.name]...this...this isn't what it looks like!"
            "I hold her eye as I come closer, trying to look confident but at the same time not threatening or judgemental."
            mike.say "Okay, Kylie - you tell me what it's supposed to look like, okay?"
            mike.say "Because it kind of looks like you're getting ready to beat the shit out of poor [bree.name] there."
            mike.say "But you're going to put me right on that one, yes?"
            "As I at least try to be diplomatic and remember all of the hostage negotiation scenes that I've seen in movies, there's a spluttering sound as [bree.name] finally loses her patience."
            show bree vangry
            bree.say "Jesus wept - it looks like she's going to beat the shit out of me because before you turned up, that's exactly what the mad bitch was going to do!"
            show kylie angry at left4 with ease
            show bree b sad at right4, hshake
            "At this, Kylie gives [bree.name]'s hair another sharp tug, resulting in a fresh round of screams."
            mike.say "Kylie, for god's sake, let her go...please!"
            show kylie sad at left5 with ease
            "Frowning and clearly reluctant to do so, Kylie nevertheless does as she's told."
            show kylie whining
            kylie.say "You shouldn't listen to a word she says, [hero.name]."
            kylie.say "She'll cry and pout, play the innocent in front of you - but I know the truth about her!"
            show kylie sad
            show bree vangry
            bree.say "And what, pray tell, is that?"
            show bree angry
            show kylie crazysad
            kylie.say "That you're a liar and a manipulator and you want to make sure [hero.name] and I can never be together..."
            kylie.say "And we ARE supposed to be together!"
            show bree surprised at right with ease
            "[bree.name] backs away from where Kylie's standing, shaking her head and pointing at the other girl in disbelief."
            show bree vangry
            bree.say "I'm leaving now, and you're lucky I don't call the damn cops."
            bree.say "Which I will do if this mouth-breathing psycho comes within spitting distance of me again anytime soon!"
            hide bree with easeoutright
            "[bree.name] turns her back on Kylie and I, walking away as quickly as she can without being seen to break into a run."
            show kylie vangry
            kylie.say "Well, do you see what I mean now?!?"
            show kylie angry at center with ease
            "I turn to face Kylie, utterly thrown by what she just said to me."
            show kylie vangry
            kylie.say "Don't you see what she's trying to do?"
            kylie.say "She's out to break us up - she's crazy!"
            show kylie angry
            mike.say "SHE'S crazy?!?"
            "All I can do is throw my hands up in the air as I too find myself backing away from Kylie."
            show kylie vangry
            kylie.say "[hero.name], where are you going?"
            kylie.say "Don't you want to sit down and talk this through?"
            show kylie angry
            mike.say "Right now, Kylie, all I want to do is be somewhere you're not!"
            hide kylie with dissolve
            "And with that, I turn and walk away without looking back."
            "But even as I do so, I can still hear Kylie calling after me."
            kylie.say "It's okay, [hero.name], I understand what I need to do now."
            kylie.say "You'll see, don't worry about it, I'll take care of everything..."
            "I know that I should try to find out just what she means by that, but instead I try to pretend that I haven't heard a single thing she's saying."
        "Hide and watch":
            "Though the knowledge that all of this is on account of them fighting over me is pretty intriguing."
            "And so while I know that I should probably be stepping in right about now, either to be [bree.name]'s knight in shining armour or just to break it up, I choose not to."
            "It's the wrong decision, and I know that more with each second that passes."
            "But watching the confrontation unfold has all of the inappropriate fascination of driving past a traffic collision and straining to see something gruesome."
            show bree vangry
            bree.say "How can I keep away from him?!?"
            bree.say "He's my housemate - we live under the same damn roof!"
            show bree annoyed
            "Kylie seems to take this statement of fact as some kind of smart-mouthed comment from [bree.name], leaning in to sneer at her words."
            show kylie vangry
            kylie.say "Oh, how convenient for you!"
            kylie.say "You might be able to fool [hero.name] by acting the innocent, taking advantage of his being such a pure soul."
            show kylie sadhappy
            kylie.say "But that won't work with me - I can see you for what you really are, and I know what you want!"
            show kylie angry
            "As she spits out ever more accusations at [bree.name], Kylie's voice becomes louder and more manic in tone."
            "At the same time she begins to exert more force on the handful of hair that she's still clutching."
            show bree sad at right4, hshake
            "This in turn makes [bree.name] yelp in pain once more, struggling to keep from having the hair simply torn from her scalp."
            show bree vangry
            bree.say "Ahh...shit..."
            bree.say "You...you actually think that I'm trying to steal [hero.name] away from you?!?"
            show bree sad
            "Almost visibly seething with anger by now, Kylie nods her head vigorously at [bree.name]'s question."
            show kylie crazysad
            kylie.say "Don't try to play your games with me, you little whore!"
            kylie.say "I don't think you're trying - I KNOW that you are!"
            kylie.say "You're just like all the other girls in his life, all the ones that came before."
            kylie.say "You all pretend to love him, lie to him and make him think that he loves you too."
            kylie.say "But you all hurt him, cheat on him and betray him in the end!"
            show kylie sad
            show bree surprised
            bree.say "What...is that what you think?"
            bree.say "You need to..."
            show kylie angry
            show bree cry at right4, hshake
            "[bree.name]'s words are turned into another scream as Kylie pulls her to within an inch of her own face."
            $ bree.love -= 10
            show kylie vangry
            kylie.say "Don't tell me what to do - no one tells me what to do!"
            kylie.say "I won't stand here and listen to your lies anymore."
            kylie.say "You know that [hero.name] and I are supposed to be together, anyone could see it if they'd just take the time to really look."
            kylie.say "And you want to keep that from happening, even if it's just for the sake of spite!"
            show kylie angry
            show bree at right4, vshake
            "I watch in stunned silence as Kylie actually uses the handful of [bree.name]'s hair to hold her still while she plants a foot in her backside."


            pause 0.2
            show bree at right, hshake with move
            "The force of the blow sends the shorter girl staggering forwards as her tormentor finally releases her grip on the hair."
            show kylie vangry
            kylie.say "You've been warned, I don't expect to have to tell you again - and I won't!"
            kylie.say "Run along now, and do as you're told, like a good little girl should."
            kylie.say "And if you don't...well, I won't be held responsible for what happens."
            kylie.say "It'll be on your own head..."
            show kylie angry
            "[bree.name] mutters something in return, most likely a parting threat."
            "But her words are lost in the sound of her sobbing and turning to run away as fast as she's able."
            hide bree with moveoutright
            "Kylie stands and watches her go, arms crossed over her chest and a look of pure, righteous triumph on her face."
            "I'm so shocked by the exchange between them and the implications for myself, that I don't even think of confronting her, not even for a second."
            "Instead I remain hidden, waiting for Kylie to leave before I emerge and hurry off to my next lecture."
            hide kylie with dissolve
            "But no matter how I try, once I'm sat in the lecture theatre, I can't think of anything but the confrontation that I just witnessed."
    return

label kylie_camera:
    show bg livingroom
    "I don't honestly recall if I got the idea to buy a camera and install it out on the front porch because of Kylie."
    "Or if I'd always been toying with the idea of getting one anyway, and the business with her just spurred me into action."
    "But either way, I got my hands on one and spent a frustrating couple of hours trying to put it somewhere discreet out on the front porch."
    "Yeah, I know it's not the most challenging of tasks on paper - but I'm a tech guy, not the hands-on type - okay?"
    "And after that was done, it took only a couple of minutes to set up the feed from the camera to my laptop and mobile."
    "I guess that I was finished, just having done it kind of made me feel that much more secure."
    "I say this because I didn't even bother to check the footage for a good week or so afterwards."
    "But then I spent a couple of nights being woken up in the small hours of the morning by the security lights."
    "It always seems to happen around 3:00am, and no matter how many times I look out there, I can't see a damn thing."
    "So I just chalk it up to a fox or something similar, maybe crossing the lawn or rooting around the trash."
    show bree casual normal at left5
    show sasha casual normal at right5
    with dissolve
    "It's only when I hear [bree.name] and Sasha mention the lights coming on that I even begin to wonder about it."
    show bree talkative
    bree.say "Sasha, were you out late last night?"
    show bree normal
    show sasha whining
    sasha.say "Erm, no, [bree.name] - I turned in early for a change."
    sasha.say "I wondered if you were, actually."
    show sasha sadsmile
    show bree talkative
    bree.say "Ah, so the lights woke you up too?"
    show bree hesitating
    "My sleep-addled mind never managed to put it all together."
    "But being reminded in the middle of the day seems to do the trick."
    "There's no need to speculate as to what could be tripping the lights."
    hide bree
    hide sasha
    with dissolve
    "All I have to do is go back and check the feed from the security camera around that same time."
    if Person.is_not_hidden("kylie") and kylie.yandere >= 25:
        $ kylie.flags.policestation = True
        call kylie_investigation_1 from _call_kylie_investigation_1_1
    else:
        "As soon as I get a spare moment to myself, I pull up the footage for the previous night."
        "Sifting through it, there's nothing to explain the mystery at first."
        "The only sign of life that I see is actually someone walking their dog in the middle of the night."
        "Weird, but I guess that's not exactly illegal or anti-social behaviour."
        "The footage ends, and I now fully understand the meaning of boring."
        $ game.pass_time(2, needs=True)
    return

label kylie_voyeur_confront:
    "Ever since I caught sight of Kylie, watching from the corridor outside my room as her sister and I had sex, I've thought of little else."
    "Whenever I have a spare moment, or my mind wanders from what I'm doing, I see the image of her again, standing there half in shadow."
    "And then I recall her hand, reaching between her legs as she watched in silence, aware of my eyes upon her the whole time."
    "One moment I'm convinced that I should have called out the second that I saw her."
    "That I should have put a stop to it, right there and then, and not worried about the fallout."
    "But in the next I'm even more sure that I was right to keep my mouth shut and not tell a soul."
    "That I was far wiser to bottle it all up and wait until I could confront Kylie myself."
    "And of course, this being Kylie, I don't have to wait very long before I get the chance."
    show kylie a happy
    "As soon as I spot her, walking towards me as if she doesn't have a care in the world, I can already feel my blood beginning to boil."
    "I bite down on my rising anger until she's close enough to exchange words, and then I grab her firmly by the arm."
    show kylie b smile at center, zoomAt(1.5, (640, 1040)) with hpunch
    "Kylie offers no resistance whatsoever as I drag her around a corner and out of sight of anyone else that might be passing."
    show kylie at center, zoomAt(1.5, (1040, 1040)) with ease
    with hpunch
    "Even when I push her up against the wall in what's not the gentlest of ways, the smile still stays fixed on her face."
    mike.say "What in the hell are you doing, walking up to me all smiles?"
    mike.say "How many different kinds of crazy are you, Kylie?!?"
    show kylie happy
    kylie.say "It's okay, [hero.name], it's okay."
    kylie.say "You don't have to pretend to be mad with me!"
    show kylie normal
    mike.say "Wha...what did you just say?"
    show kylie shout
    kylie.say "I said you don't have to pretend to be mad with me."
    show kylie normal
    mike.say "What the fuck are you talking about, Kylie?"
    mike.say "Of course I'm mad at you!"
    mike.say "You broke into my damn house and watched me in bed - with your SISTER!"
    show kylie smile
    "Kylie chuckles at this, shaking her head as if we're playing some kind of game that she finds amusing."
    show kylie shout
    kylie.say "That's not how it looked from where I was standing the other night!"
    kylie.say "I seem to remember you having every chance in the world to tell Alexis I was there."
    kylie.say "To me, it looked like you were letting me watch, like you were liking having an audience."
    hide kylie
    show kylie b normal at right
    "I back away from Kylie, shaking my head at her twisted interpretation of events."
    "Twisted yes, but perfectly believable all the same."
    mike.say "No...no, that's not what happened."
    mike.say "I didn't want to scare Alexis, to freak her out, that's all."
    show kylie talkative at center with ease
    kylie.say "Oh, I see..."
    kylie.say "So you told her as soon as you woke up the next morning, right?"
    kylie.say "Because I have to say, she's not said a word about it to me!"
    show kylie sad
    mike.say "Okay, Kylie, I admit it - I didn't tell Alexis what you did."
    show kylie smile
    "Kylie shakes her head with another smile."
    show kylie shout
    kylie.say "Oh no, you mean what WE did, [hero.name]."
    kylie.say "You fucked my sister while I watched, rubbing my pussy til I came."
    kylie.say "We did that together, you and me!"
    show kylie normal
    "Kylie must recognize the look that spreads across my face as revulsion then, maybe even as self-loathing."
    show kylie talkative
    kylie.say "You shouldn't beat yourself up over it, [hero.name]."
    kylie.say "People watch other people fucking all the time - they call it pornography."
    show kylie shout
    kylie.say "In fact, I was surprised how much it turned me on when I expected the opposite."
    show kylie normal
    mike.say "Huh...what do you mean?"
    show kylie shout
    kylie.say "Well, I just know that you and I are destined to be together, [hero.name]."
    kylie.say "I've always known that."
    kylie.say "But I NEVER thought the sight of you with another girl would get me so...hot!"
    kylie.say "In fact, it got me so turned on that I think I'd like to see it again..."
    show kylie normal
    menu:
        "That's gross!":
            "What in the hell is wrong with this girl?"
            "She's like peeling an onion that's made of pure perversion."
            "Just when you think you've gotten under her skin, you find another layer that's more depraved than the last."
            mike.say "How can you even stand there and say that?"
            mike.say "Get the fuck away from me, you sick, crazy bitch!"
            "I'm already backing away from Kylie by now, getting ready to run if I have to."
            show kylie smile
            "But all the same, that sick smile is still there, and she simply shakes her head slowly."
            show kylie crazyhappy
            kylie.say "Like I said, [hero.name], it's okay."
            kylie.say "You pretend to be mad at me for as long as you need to."
            kylie.say "I promise I'll still be here when you're ready to admit that you love me."
            kylie.say "Until then, I'll just keep on watching, protecting you from the shadows."
            show kylie normal
            "Now it's my turn to shake my head, a motion that becomes ever more frantic as I turn and run away."
            "I just know that she's standing there, watching me flee, that same smile on her face."
            "But I don't look back once, and I just keep on running."
            $ kylie.yandere += 10
            return
        "That's hot!":
            "I stare at Kylie for a moment, licking my lips as I think about what she just admitted."
            "My first instinct was to tell her to go to hell, but then a thought struck me."
            "What if she is right, and what happened the other night really was no worse than watching porn?"
            "Sure, Alexis would probably be devastated if she knew what went down and that I kept it to myself."
            "But by doing so, I've spared her that trauma and all of the pain that would come along with it."
            "And what about Kylie herself - doesn't she have needs too?"
            "There's definitely something weird going on with this girl, but who am I to judge her so harshly?"
            "What if this is the only way that she knows how to express that side of herself?"
            "I have no reason to doubt that she means it when she says that she loves me too."
            "Would it really be so bad to give her what she wants and let her watch me have sex with other women?"
            "Plus, knowing that she's only getting off on it because it's me she's watching is insanely hot!"
            mike.say "M...maybe I was too harsh."
            show kylie talkative
            kylie.say "Huh - what was that, [hero.name]?"
            show kylie normal
            mike.say "I said maybe I was too harsh on you, Kylie."
            mike.say "Okay, so I did like that you were watching me fuck Alexis."
            show kylie crazyhappy
            "Kylie's eyes become even wider than normal, her smile ear-to-ear."
            kylie.say "I KNEW IT!"
            kylie.say "I knew that you really loved me, [hero.name]!"
            kylie.say "So...you'll let me watch?"
            show kylie normal
            "I think about saying something to her, about putting conditions in place."
            "But then I realize just how crazy it would be to agree to something like this while trying to argue about the fine-print."
            mike.say "Okay, Kylie, okay."
            mike.say "If that's what you want."
            hide kylie
            show kylie kiss
            with fade
            $ kylie.flags.kiss += 1
            "In way of answer, Kylie leans in and kisses me, full on the lips."
            "I feel her tongue dart into my mouth, like a seeking eel."
            "The kiss lingers for a long time, until she chooses to release me."
            hide kylie
            show kylie b blush
            with fade
            kylie.say "You won't regret this, [hero.name], I promise."
            kylie.say "And every time you see me, you can be sure that I'll be wet at the mere sight of you..."
            show kylie normal
            "And with that, she turns and walks away, leaving me alone with my conscience screaming in alarm."
            "I have no idea what I just agreed to, or where it will lead!"
            $ kylie.love += 10
            $ kylie.flags.canwatch = True
            return

label kylie_voyeur:
    $ DONE["kylie_voyeur"] = game.days_played
    show alexis missionary hard with fade
    "As Alexis lays there, spread out below me on the bed, I can honestly say that she's one of the most beautiful sights I've ever seen in my life."
    "And what makes the experience all the more incredible is the fact that she's a love I thought that'd lost forever."
    "So it amazes me that I could have forgotten for even a moment just how incredible she looks right now."
    "By rights, as I feel my cock sliding along the lips of her pussy, Alexis should be the only thing on my mind."
    "Yet all the same, I have the strangest feeling in the back of my mind, one that I just can't seem to shake off."
    show alexis missionary vaginal pleasure
    "No matter how much I try to push it aside and concentrate on making love to Alexis, it still nags at the corner of my awareness."
    "Perhaps it's something to do with the way that Alexis and I broke it off all those years ago?"
    "Maybe there's still a lingering sense of fear and doubt that she might betray me for a second time?"
    "Something like that would take a long time to truly get over."
    "Even more so if it was something lurking in the depths of my unconscious mind..."
    alexis.say "Ahh..."
    alexis.say "[hero.name]...that feels amazing."
    show alexis missionary normal
    alexis.say "You can do that to me all night long!"
    "At the sound of Alexis's voice, I try even harder to snap out of it."
    "I manage to smile down at her and begin to do my best to oblige."
    show alexis missionary pleasure
    "The effect is almost instant, as she rolls her head back into the pillows."
    alexis.say "Oh yeah..."
    alexis.say "Don't you dare stop."
    alexis.say "Not until I cum!"
    "But almost as soon as Alexis closes her eyes and loses herself to the moment, I feel that same sensation again."
    show alexis missionary normal
    "The only difference is that now something springs to mind that helps me define it better."
    if kylie.flags.canwatch:
        "The sensation reminds me of the first time I felt this feeling of being watched."
        "Without stopping my thrusting in and out of Alexis, I smile and turn my head towards the doorway."
        "I know what I am expecting to find there, which makes it all the more exciting."
        "When I look over at the door, my adrenaline starts to pump."
        "By the light that's coming into the room, I can also see a shadowed shape that fills me with lust."
        "Trust me, I've lived here and had this room as my own long enough to know the shadows that light casts."
        "And the only thing that could make one like that is someone standing outside and peering in!"
        "All the time I have my eyes fixed on the shadow in the doorway, completely ignoring Alexis."
        "As if sensing my having noticed its presence, the shadow takes a single step forward."
        "This brings half of its face into view, the other half still hidden in the shadows."
    else:
        "The sensation reminds me of that age old and uncanny feeling of being watched."
        "Without stopping my thrusting in and out of Alexis, I cast my head this way and that."
        "Surely I must be wrong, or mistaking the sensation for something similar yet different."
        "I'm more than sure that none of my housemates would spy on me in a situation like this."
        "Which means that if someone is watching, it can't be [bree.name] or Sasha..."
        "Now I can feel myself beginning to panic, wondering if there's an unseen intruder in the house."
        "A quick glance confirms that the windows are closed and secure."
        "But when I look over at the door, my heart almost skips a beat."
        "It's open to the corridor outside, even though I'm sure I closed it before we got down to business."
        "By the light that's coming into the room, I can also see a shadowed shape that fills me with dread."
        "Trust me, I've lived here and had this room as my own long enough to know the shadows that light casts."
        "And the only thing that could make one like that is someone standing outside and peering in!"
        "My mind begins to race, desperately recalling all the items to hand that could be used as a weapon and where they are in relation to me."
        "All the time I have my eyes fixed on the shadow in the doorway, expecting someone to burst in any second."
        "As if sensing my having noticed its presence, the shadow takes a single step forward."
        "This brings half of its face into view, the other half still hidden in the shadows."
    hide alexis missionary
    show kylie memory
    with fade
    "I gasp at the sight, instantly recognizing it as Kylie."
    "And then I gasp again as I glance down and see that she's completely naked."
    "Alexis remains none the wiser as she moans in pleasure beneath me, unaware that her younger sister is watching our every move."
    if kylie.flags.canwatch:
        "What can I do apart from smile and keep right on going?"
        "After I confronted Kylie, I knew this was likely to happen again."
        "How she knew that Alexis and I had a date planned tonight is beyond me."
        "As Kylie stares straight at me, I begin to thrust harder into her sister."
        "From the look on her face, she's getting a massive kick out of the situation."
        "Well, that and knowing that I'm aware of what she's doing too."
        "For a moment, I actually think that she's going to walk into my bedroom and make her presence known."
        "That she'll ask to join into what's happening between Alexis and me, consequences be damned."
        "But then I see that Kylie's arm is moving with a slow, steady rhythm."
        "My eye darts down, curious to see the evidence of what I know she's doing."
        "I see that her fingers are working away furiously at the lips and folds of her pussy."
        "There's no doubt about it, my eyes aren't deceiving me - she's masturbating over what we're doing!"
        "As I turn gaze back up and lock eyes with Kylie, I expect to see her smile or wink at me."
        "But her face remains passive as she pleasures herself in complete silence."
        "The only thing that makes me sure she's enjoying this as much as I am is how her lips turn up at the corners."
        "In any other circumstances, I'd read that as nothing more sinister than a smile."
        "Yet here and now, in these strangest of circumstances, it's exhilarating in the extreme."
    else:
        "What can I do apart from keep right on going?!?"
        "If I stop, Alexis will know that there's a problem and demand to know what it is."
        "If I call Kylie out, then all hell's going to break loose, and who knows where it'll end?"
        "And then there's the part of me that's morbidly curious to see just what that crazy bitch has in mind..."
        "Kylie stares straight at me, holding my eye."
        "From the look on her face, she's getting a massive kick out of the situation."
        "Well, that and knowing that I'm aware of what she's doing too."
        "For a moment, I actually think that she's going to walk into my bedroom and make her presence known."
        "That she'll force her way into what's happening between Alexis and me, consequences be damned."
        "But then I see that Kylie's arm is moving with a slow, steady rhythm."
        "My eye darts down, curious to see just what it could be that she's doing."
        "And then I see that her fingers are working away furiously at the lips and folds of her pussy."
        "There's no doubt about it, my eyes aren't deceiving me - she's masturbating over what we're doing!"
        "My gaze shoots back up and I lock eyes with Kylie, expecting to see her leer or sneer at me."
        "But her face remains passive as she pleasures herself in complete silence."
        "The only thing that makes me sure she's even awake and not in some kind of trance is how her lips turn up at the corners."
        "In any other circumstances, I'd read that as nothing more sinister than a smile."
        "Yet here and now, in these strangest of circumstances, it's disturbing in the extreme."
    hide kylie memory
    show alexis missionary vaginal pleasure
    with fade
    alexis.say "Oh, shit..."
    alexis.say "Shit..."
    "I almost jump at the sound of Alexis's voice, and I almost slip out of her pussy too."
    "My head snaps back around as I redouble my efforts, instinctively sensing that she's about to cum."
    alexis.say "Yeah, [hero.name]..."
    alexis.say "That's the shit!"
    show alexis missionary ahegao
    alexis.say "Make me cum...please!"
    show alexis missionary creampie
    "I lose myself inside of Alexis a moment later, which is enough to make it happen for her too."
    "Even as she rides me to the very last, I can't resist taking one last look back, over my shoulder."
    "But all I see there is the empty doorway, and the familiar shadows cast by the lights in the corridor."
    if kylie.flags.canwatch:
        "However Kylie got in, she's already fled the scene, leaving me feeling satisfied and Alexis none the wiser."
        "I know that I should say something to Alexis about it."
        "Not only did someone spy on her while we were making love, but worse, it was her own younger sister."
        "Yet I hold my tongue and tell her nothing, knowing how much both Kylie and myself love the voyeurism."
        $ kylie.love += 5
    else:
        "However Kylie got in, she's already fled the scene, leaving me feeling seriously creeped out and guilty."
        "I know that I should say something to Alexis about it."
        "Not only did someone spy on her while we were making love, but worse, it was her own younger sister."
        "Yet I hold my tongue and tell her nothing, hoping to confront Kylie at the first available opportunity."
        "Somehow I feel that if I challenge her myself, the crazy bitch might be more willing to talk."
        "Either that, or I could keep her from doing something drastic to her sister..."
    hide alexis missionary
    call alexis_sleep_date_fuck from _call_alexis_sleep_date_fuck_1
    return


label kylie_investigation_1:
    $ DONE["kylie_investigation_1"] = game.days_played
    "As soon as I get a spare moment to myself, I pull up the footage for the previous night."
    "Sifting through it, there's nothing to explain the mystery at first."
    "The only sign of life that I see is actually someone walking their dog in the middle of the night."
    "Weird, but I guess that's not exactly illegal or anti-social behavior."
    "But then, just as the time-stamp on the footage approaches 3:00am, I see it."
    "A figure walks down the street and pauses in front of the house."
    "It's impossible to make out much detail at that distance, but I instantly expect it to be a clown."
    "You know, because I've watched all of those videos?"
    "The ones where someone dresses up as a clown and wanders around residential neighborhoods in the dark?"
    "But as the figure turns and starts to walk up the path to the front porch, they trip the lights."
    "And then I can see quite clearly that, while the figure isn't a clown, it's just as terrifying of a sight."
    "It's Kylie, as large as life and twice as creepy."
    "She has a smile plastered on her face and a crazed look in her eyes."
    "I watch, holding my breath as she steps up, onto the porch."
    "And then she just stands there, motionless and silent."
    "This goes on for so long that I forget I held my breath."
    "I breathe out, almost gasping for air and the sensation jolts me back to reality."
    "My instinct is to pretend this isn't happening, or that Kylie's just playing a prank."
    "But as I fast-forward through the footage, I become ever more convinced that this is deadly serious."
    "She's there for literally hours, hardly moving or changing her expression."
    "I can't help getting the impression that she's waiting for someone to open the door."
    "And I don't even want to imagine what would happen if one of us actually did..."
    "Finally, just before first light, Kylie simply turns around and retraces her steps."
    "As she walks away from the house, I realize that she must now look quite innocent in nature."
    "Sure, she's a girl walking home alone in the early morning."
    "But that's just a potentially unwise choice, not the behavior of a dangerous lunatic."
    "I don't want to do it, but I forced myself to check the footage from nights before that one."
    "And I feel my heart sink into my stomach as I see the same sequence of events, replayed over and over again."
    "Jesus Christ - she's a stalker!"
    "Worse than that - she's a madwoman!"
    "What in the hell am I going to do?!?"
    return

label kylie_investigation_2:
    $ game.flags.kylieinvestigationdelay = TemporaryFlag(True, 7)
    show bg policestation
    "It seems pretty crazy to me now that I wasn't at all worried when I realised that Kylie wasn't just extra keen on me."
    "Even when it dawned on me that what she was doing pretty much amounted to stalking, I still didn't instantly get worried."
    "I guess I was actually more than a little thrilled at the attention, turned-on in that dumb way only a guy can be."
    "But when she brought it to my doorstep, started hanging around my house at all hours of the night."
    "That was when I finally woke up to the seriousness of what was going on with her."
    "Suddenly, this obsession of hers was putting not just me in danger, but [bree.name] and Sasha too!"
    "Perhaps I could have tried confronting Kylie, demand that she leave me and my housemates alone."
    "But past experience told me that she'd just ignore me, brush it off in her usual crazy manner."
    "Or worse, telling her to get lost in no uncertain terms might be enough to push her into an act of violence."
    "So that's why I went to the trouble of hiding a camera on the front porch of the house."
    "If I couldn't force Kylie to stop, then I'd need evidence to get the help of someone that could."
    "I had the camera linked to my computer, and within a couple of days, I also had plenty of incriminating footage."
    "Keeping the whole matter to myself, I burned what I thought would be the strongest evidence onto a disc."
    "And with that in my pocket, I went straight to the nearest police station."
    "Policeman" "Good morning, Sir."
    "Policeman" "How can I help you?"
    mike.say "I'd like to talk to someone about..."
    if kylie.flags.killed:
        mike.say "Well, about a murder, you know?"
    elif kylie.flags.rape:
        mike.say "Well, about a rape, you know?"
    else:
        mike.say "Well, about stalking, you know?"
    "The officer behind the reception desk nods at this."
    "I see them reach for some forms and a pen."
    "Policeman" "Do you have a criminal record, Sir?"
    "Policeman" "Or are you here to confess to your first offence?"
    mike.say "Wait...what?!?"
    if kylie.flags.killed:
        mike.say "I'm here because someone killed my friend!"
    elif kylie.flags.rape:
        mike.say "I'm here because someone raped ME!"
        mike.say "Not the other way around!"
    else:
        mike.say "I'm here because someone's stalking ME!"
        mike.say "Not the other way around!"
    "The officer hastily returns the forms to the pile and picks up a phone."
    "Policeman" "Ah, sorry, Sir."
    "Policeman" "You just struck me as the type, you know?"
    "I open my mouth to protest, to complain about what just happened."
    "But the officer holds up a hand to silence me while speaking into the receiver."
    "A quick conversation follows, of which I can hear almost nothing at all."
    "Then just as swiftly, the officer returns the receiver to its cradle and points down the corridor."
    "Policeman" "Interview room nine, Sir."
    "Policeman" "Detective Foglio will be with you shortly."
    "Still prickled by the assumption that I was the criminal and not the victim, I do as I'm told."
    with fade
    "And once I'm in the designated interview room and sat at the table, I don't have to wait long until I'm seen."
    "The door opens noisily, slamming against the wall, and I catch the butt end of an argument as it does so."
    "Inspector" "Oh yeah?!?"
    "Inspector" "Well you tell that prick, Callaghan that he can shove it!"
    "Inspector" "I hear he's into that kind of shit!"
    "The voice is strong, stern and sounds like it doesn't take crap from anyone."
    "And on top of that, it's without a doubt female as well!"
    show camila work normal at center, zoomAt(1, (640, 720)) with easeinleft
    "The first I see of the person it belongs to is a glimpse out of the corner of my eye as she pushes past me."
    show camila at center, zoomAt(1, (640, 720)) with ease
    "A second later, she drags the chair on the other side of the table noisily back across the floor."
    show camila at center, traveling(1.5, 0.3, (640, 1040))
    pause 0.3
    show camila at center, traveling(1.5, 0.3, (640, 1140))
    if "camila_event_01_alt" in DONE:
        "Which is when I realise that I've seen that face before!"
        show camila talkative
        camila.say "Hey, [hero.name]..."
        camila.say "I thought that a familiar face might make this go more smoothly."
        show camila normal
        mike.say "H...hey, Camila..."
        "Oh man, I knew this was going to be a tough one for me to pull off."
        "But Camila just made it that much harder for me to get my words out."
        "And the worst thing is that she thinks she's doing me a favour!"
        "Okay, okay...I have to get a hold of myself and do this thing."
        "Preferably without ruining my relationship with Camila into the bargain."
        mike.say "Thanks for thinking about me and stepping in."
        mike.say "I'm just a little nervous...in case you hadn't noticed!"
        mike.say "And police stations kinda make me even more nervous, yeah?"
        "Camila puts on a hard but understanding smile as I struggle to explain myself."
        "But I note that she doesn't make any attempt to reach across the table and touch me."
        "Not even to offer a pat on the back of my hand, which I guess is her trying to keep things professional."
        camila.say "No need to explain it to me."
        camila.say "And don't worry - I've got more than enough experience of this place for the both of us."
        "I watch as Camila takes out her notepad and pulls out a pen."
        "And there's a slight change in her as she does so."
        "Almost as if she's shifting gear from friendly to formal."
        show camila talkative
        camila.say "Okay, good enough..."
        camila.say "So, the officer on the front desk tells me you want to report..."
        show camila surprised
        if kylie.flags.killed:
            camila.say "What was it...a murder?"
        elif kylie.flags.rape:
            camila.say "What was it...a rape?"
        else:
            camila.say "What was it...stalking?"
        show camila sad
        "I nod with enthusiasm at this, keen to get this over with as soon as possible."
        "But also, I realise, because I feel on odd compulsion to obey Camila almost without question."
        mike.say "Yes...I mean yeah, that's right, Camila."
        "She notices me trying to make my voice deliberately deeper."
        "And her frown is more than enough to make me stop."
        mike.say "There's this girl I went to high school with, you see."
        mike.say "Her name's Alexis...."
        show camila annoyed
        "Camila starts scribbling notes into her pocket book as quickly as I can speak the words."
        "And I can't help notice that her handwriting is atrocious as she furiously hacks away at the pages."
        if not kylie.flags.rape and not kylie.flags.killed and not "kylie_attack" in DONE:
            show camila talkative
            camila.say "And this is the girl that you're accusing of stalking you?"
            show camila normal
            mike.say "Oh no, that's her younger sister, Kylie."
            show camila annoyed
            "Camila furrows her brows at this."
            show camila surprised
            camila.say "Then what does this Alexis character have to do with anything?"
            show camila annoyed
            mike.say "We were in a relationship back then, and it ended...badly."
            show camila angry
            camila.say "And this Kylie bitch is what, mad at you for breaking her sister's heart?"
            show camila annoyed
            mike.say "No, no, no - that's ancient history by now."
            mike.say "No, I ran into Kylie at college."
            mike.say "And then she started following me everywhere, telling me that she's always been obsessed with me!"
            show camila normal
            "The Camila raises a quizzical eyebrow at this, clearly amused at the notion."
            show camila talkative
            camila.say "Let me guess - because you're just that irresistible, right?"
            show camila normal
            mike.say "Yes...no...I don't know!"
            mike.say "Kylie's insane, okay?"
            mike.say "I'm scared that she's going to do something to one of my housemates...or me."
        elif kylie.flags.rape and not kylie.flags.killed:
            show camila surprised
            camila.say "And this is the girl that you're accusing of raping you?"
            show camila normal
            mike.say "No, aren't you listening to me?"
            mike.say "Kylie's the one that raped me!"
            show camila annoyed
            "The Camila furrows her brows at this."
            show camila surprised
            camila.say "Then what does this Alexis character have to do with shit?"
            show camila normal
            mike.say "We were in a relationship back then, and it ended...badly."
            show camila angry
            camila.say "And this Kylie bitch is what, mad at you for breaking her sister's heart?"
            show camila annoyed
            mike.say "No, no, no - that's ancient history by now."
            mike.say "No, I ran into Kylie at college."
            mike.say "And then she started following me everywhere, telling me that she's always been obsessed with me!"
            show camila normal
            "The Camila raises a quizzical eyebrow at this, clearly amused at the notion."
            show camila talkative
            camila.say "Let me guess - because you're just that irresistible, right?"
            show camila normal
            mike.say "Yes...no...I don't know!"
            mike.say "Kylie's insane, okay?"
        elif kylie.flags.killed:
            show camila surprised
            camila.say "And this is the girl that got murdered?"
            show camila normal
            mike.say "No, aren't you listening to me?"
            mike.say "My housemate's the one that got killed!"
            mike.say "And Kylie is the murderer!"
            show camila annoyed
            "Camila furrows her brows at this."
            show camila surprised
            camila.say "Then what does this Alexis character have to do with shit?"
            show camila normal
            mike.say "We were in a relationship back then, and it ended...badly."
            show camila angry
            camila.say "And this Kylie bitch is what, mad at you for breaking her sister's heart?"
            show camila annoyed
            mike.say "No, no, no - that's ancient history by now."
            mike.say "No, I ran into Kylie at college."
            mike.say "And then she started following me everywhere, telling me that she's always been obsessed with me!"
            show camila normal
            "Camila raises a quizzical eyebrow at this, clearly amused at the notion."
            show camila talkative
            camila.say "Let me guess - because you're just that irresistible, right?"
            show camila normal
            mike.say "Yes...no...I don't know!"
            mike.say "Kylie's insane, okay?"
        else:
            show camila surprised
            camila.say "And this is the girl that you're accusing of trying to raping you?"
            show camila normal
            mike.say "No, aren't you listening to me?"
            mike.say "Kylie's the one that tried to rape me!"
            show camila annoyed
            "Camila furrows her brows at this."
            show camila surprised
            camila.say "Then what does this Alexis character have to do with shit?"
            show camila normal
            mike.say "We were in a relationship back then, and it ended...badly."
            show camila angry
            camila.say "And this Kylie bitch is what, mad at you for breaking her sister's heart?"
            show camila annoyed
            mike.say "No, no, no - that's ancient history by now."
            mike.say "No, I ran into Kylie at college."
            mike.say "And then she started following me everywhere, telling me that she's always been obsessed with me!"
            show camila normal
            "Camila raises a quizzical eyebrow at this, clearly amused at the notion."
            show camila talkative
            camila.say "Let me guess - because you're just that irresistible, right?"
            show camila normal
            mike.say "Yes...no...I don't know!"
            mike.say "Kylie's insane, okay?"
        if "kylie_attack" not in DONE and kylie.flags.policestation:
            mike.say "Look, I'm not making this stuff up!"
            "I pull the disc out of my pocket and slam it down on the table."
            mike.say "She's been hanging around outside my house in the middle of the night."
            mike.say "If you don't believe me, take a look at the footage on that disc!"
            "The officer reacts to my mounting agitation by gesturing downwards with her open hands."
            show camila surprised
            camila.say "Hey, hey - calm down, [hero.name]..."
            camila.say "I'm just trying to establish the facts here, okay?"
            show camila normal
            "She reaches across the table and takes the disc, turning it over in her hands."
            show camila angry
            camila.say "Tell me, has this bitch actually made any threats or turned this thing physical?"
            show camila annoyed
            mike.say "Well...no, not really."
            mike.say "But you have the evidence right there."
            mike.say "Isn't that all you need to bust her ass?"
            show camila surprised
            "Camila surprises me then by bursting into laughter."
            "It's loud and as raucous as I would have expected, but it's also infectious."
            "And she looks pretty amazing when she smiles like that too..."
            show camila surprised
            camila.say "'Bust her ass'?"
            camila.say "Where did you hear that shit?!?"
            show camila surprised
            mike.say "I...I guess it was on TV."
            mike.say "Sorry...I'm not very good at this."
            mike.say "TV shows and movies are all I have to go on."
            show camila wink
            "Camila puts a hand in front of her mouth, trying to force herself to stop laughing."
            show camila talkative
            camila.say "Ah Jesus, I'm sorry, [hero.name]..."
            camila.say "I shouldn't have done that - this is a serious matter."
            show camila sadsmile
            "I smile weakly, struggling to accept that Camila broke her big tough cop act to apoligise to me."
            mike.say "Camila...this is all feeling pretty weird, you know?"
            show camila talkative
            camila.say "Okay, okay...I gotta admit, I'm feeling the same way too."
            camila.say "Maybe we can meet up for a drink and a chat when this is over?"
            camila.say "You know, try to reset things between us?"
            show camila normal
            mike.say "Yeah, Camila - that sounds like a great idea."
            show camila talkative
            camila.say "It sure does."
            camila.say "Actually, I'm kind of relieved to have run into you today."
            camila.say "It makes a change to be talking to a guy honest enough to admit he's no tough cookie."
            camila.say "Especially when you spend as much time as I do around meatball cops as sensitive as a brick."
            camila.say "And most of them about half as smart too!"
            show camila normal
            "I manage to laugh at this, and not sound too much like I'm in danger of choking."
            show camila talkative
            camila.say "Okay, [hero.name] - here's the bad news."
            camila.say "As things stand, unless your Little Miss Fruitloop kicks thing up a notch..."
            show camila normal
            "She spreads her hands out in front of her for emphasis."
            show camila whining
            camila.say "I'm afraid my hands are tied!"
            show camila sad
            mike.say "But...but..."
            show camila surprised
            camila.say "Whoa there, tough guy - I didn't say you were on your own, did I?"
            show camila normal
            "She pulls a business card out of her jacket pocket and hands it over to me."
            show camila talkative
            camila.say "I know you've got my cell number already..."
            camila.say "But this is my work number - like my own personal bat-signal."
            camila.say "If shit gets real, then you call me on this one, okay?"
            show camila normal
            mike.say "And if...well, if shit hits the fan...what then?"
            show camila talkative
            camila.say "Then you dial nine-one-one, and pray they get to you quick enough!"
            show camila normal
            $ kylie.flags.arrest = False
            $ hero.cancel_activity()
        elif "kylie_attack" in DONE and kylie.flags.killed:
            mike.say "Officer, she killed my housemate - right in front of me!"
            "Suddenly the memory of that moment returns with a vengeance."
            "I see the scene playing out in slow-motion."
            "The expression on her face."
            "The blood..."
            show camila whining
            camila.say "I know, [hero.name], I know."
            camila.say "Listen - there's nothing I can say or do to change what happened."
            camila.say "And I'll move heaven and earth to catch that cold-hearted monster!"
            camila.say "But right now, you're the one I'm more worried about..."
            show camila normal
            "At the mention of my own well being, I stop and look at her in complete silence."
            "And then it feels like a black hole is opening up beneath me, threatening to pull me down into its depths."
            mike.say "She...she tied me up."
            mike.say "She forced herself on me."
            mike.say "I...I don't even know if that counts as rape!"
            "Detective Foglio shakes her head, vigorously this time."
            show camila whining
            camila.say "Don't even think that, [hero.name]."
            camila.say "Don't you dare go down that dumb, macho rabbit hole!"
            camila.say "Man or woman, it doesn't change what that psycho did to you."
            show camila normal
            "I nod, unable to put into words how much her reassurance means to me."
            "Her strength means that I can accept what happened without feeling like I'm falling apart."
            "And I'm not afraid to say that, in that moment, I feel tears welling in the corner of my eyes."
            "But then Camila chooses that moment to finally reach out and put a hand on my shoulder."
            show camila talkative
            camila.say "Hey, you're not dealing with this shit on your own."
            camila.say "I'm gonna be here for you, every step of the way - whether you like it or not!"
            show camila normal
            mike.say "Hey, Camila - that really means a lot."
            show camila talkative
            camila.say "I mean it - but don't you go getting all mushy on me now."
            camila.say "But it does make a change to be talking to a guy honest enough to admit he's no tough cookie."
            camila.say "Especially when you spend as much time as I do around meatball cops as sensitive as a brick."
            camila.say "And most of them about half as smart too!"
            show camila normal
            "I manage to laugh at this, and not sound too much like I'm in danger of choking."
            mike.say "Thank you, Camila."
            mike.say "You don't know how much I needed to hear you say that!"
            $ kylie.flags.arrest = True
        elif "kylie_attack" in DONE and kylie.flags.rape:
            mike.say "She...she tied me up."
            mike.say "She forced herself on me."
            mike.say "I...I don't even know if that counts as rape!"
            "Detective Foglio shakes her head, vigorously this time."
            show camila whining
            camila.say "Don't even think that, [hero.name]."
            camila.say "Don't you dare go down that dumb, macho rabbit hole!"
            camila.say "Man or woman, it doesn't change what that psycho did to you."
            show camila normal
            "I nod, unable to put into words how much her reassurance means to me."
            "Her strength means that I can accept what happened without feeling like I'm falling apart."
            "And I'm not afraid to say that, in that moment, I feel tears welling in the corner of my eyes."
            "But then Camila chooses that moment to finally reach out and put a hand on my shoulder."
            show camila talkative
            camila.say "Hey, you're not dealing with this shit on your own."
            camila.say "I'm gonna be here for you, every step of the way - whether you like it or not!"
            show camila normal
            mike.say "Hey, Camila - that really means a lot."
            show camila talkative
            camila.say "I mean it - but don't you go getting all mushy on me now."
            camila.say "But it does make a change to be talking to a guy honest enough to admit he's no tough cookie."
            camila.say "Especially when you spend as much time as I do around meatball cops as sensitive as a brick."
            camila.say "And most of them about half as smart too!"
            show camila normal
            "I manage to laugh at this, and not sound too much like I'm in danger of choking."
            mike.say "Thank you, Camila."
            $ kylie.flags.arrest = True
        elif "kylie_attack" in DONE and kylie.flags.assault_video:
            mike.say "Look, I'm not making this stuff up!"
            "I pull the disc out of my pocket and slam it down on the table."
            mike.say "She's been hanging around outside my house in the middle of the night."
            mike.say "If you don't believe me, take a look at the footage on that disc!"
            "Camila reacts to my mounting agitation by gesturing downwards with her open hands."
            show camila talkative
            camila.say "Hey, hey - calm down, [hero.name]..."
            camila.say "I'm just trying to establish the facts here, okay?"
            camila.say "Tell me, has this bitch actually made any threats or turned this thing physical?"
            show camila normal
            "At this point, I almost feel like I'm going to explode with frustration."
            mike.say "Watch the goddamn footage!"
            mike.say "She's right there - shocking me with a taser on my own front porch!"
            "She reaches across the table and takes the disc, turning it over in her hands."
            show camila talkative
            camila.say "If this video shows what you say it does..."
            camila.say "Well, let's just say that it changes the complexion of this whole thing."
            show camila normal
            "I can feel the tension starting to drain out of me as she seems to be taking me more seriously."
            "And I instantly begin to regret the irate tone that I took with her just now."
            mike.say "So you can do something about it, right?"
            mike.say "Isn't that all you need to bust her ass?"
            show camila happy at startle
            "Camila surprises me then by bursting into laughter."
            "It's loud and as raucous as I would have expected, but it's also infectious."
            "And she looks pretty amazing when she smiles like that too..."
            show camila talkative
            camila.say "'Bust her ass'?"
            camila.say "Where did you hear that shit?!?"
            show camila normal
            mike.say "I...I guess it was on TV."
            mike.say "Sorry...I'm not very good at this."
            mike.say "TV shows and movies are all I have to go on."
            show camila wink
            "Camila puts a hand in front of her mouth, trying to force herself to stop laughing."
            show camila talkative
            camila.say "Ah Jesus, I'm sorry, [hero.name]..."
            camila.say "I shouldn't have done that - this is a serious matter."
            show camila normal
            "I smile weakly, struggling to accept that Camila just broke her big tough cop act for me."
            mike.say "Camila...this is all feeling pretty weird, you know?"
            show camila talkative
            camila.say "Okay, okay...I gotta admit, I'm feeling the same way too."
            camila.say "Maybe we can meet up for a drink and a chat when this is over?"
            camila.say "You know, try to reset things between us?"
            show camila normal
            mike.say "Yeah, Camila - that sounds like a great idea."
            show camila talkative
            camila.say "It sure does."
            camila.say "Actually, I'm kind of relieved to have run into you today."
            camila.say "It makes a change to be talking to a guy honest enough to admit he's no tough cookie."
            camila.say "Especially when you spend as much time as I do around meatball cops as sensitive as a brick."
            camila.say "And most of them about half as smart too!"
            show camila normal
            "I manage to laugh at this, and not sound too much like I'm in danger of choking."
            show camila talkative
            camila.say "Okay, [hero.name] - here's the good news."
            camila.say "Once I review this footage, we should have enough to charge Little Miss Fruitloop."
            camila.say "After that, it's only a matter of time until we bring her in."
            show camila normal
            mike.say "But what if she gets to me before that?!?"
            mike.say "Can't I get some kind of police protection?"
            show camila talkative
            camila.say "Whoa there, tough guy - I didn't say you were on your own, did I?"
            show camila normal
            "She pulls a business card out of her jacket pocket and hands it over to me."
            show camila talkative
            camila.say "I know you've got my cell number already..."
            camila.say "But this is my work number - like my own personal bat-signal."
            camila.say "If shit gets real, then you call me on this one, okay?"
            show camila normal
            mike.say "And if...well, if shit hits the fan...what then?"
            show camila talkative
            camila.say "Then you dial nine-one-one, and pray they get to you quick enough!"
            show camila normal
            $ kylie.flags.arrest = False
            $ hero.cancel_activity()
        else:
            "Camila lets out a sigh of frustration and pushes herself back from the table."
            "She holds her hands up in the air, shaking her head in a gesture of helplessness."
            show camila whining
            camila.say "I'm sorry, [hero.name], you gotta believe I am."
            camila.say "But without any kind of actual proof, there's zero chance of me doing anything about it."
            camila.say "And my hands stay tied as long as that's the case."
            show camila normal
            $ kylie.flags.arrest = False
            $ hero.cancel_activity()
    else:
        "And then she flops down into the seat, letting out a grunt of frustration as she tosses her badge and a gun on the table before her."
        show camila talkative
        "Det. Foglio" "I'm Sergeant Camila Foglio, pleased to meet you Mr..."
        show camila normal
        mike.say "Ah...[heroname]...[heroname] [hero.family_name]..."
        "Yeah, I admit it - I almost managed to forget my own name after setting eyes on her."
        "She looks every inch a cop, and a really tough one at that!"
        "But she's also got cascading curls of black hair, the most beguiling eyes, and..."
        "And a scar on her forehead, cutting her right eyebrow clean in two!"
        show camila angry
        "Det. Foglio" "Hey, hey, hey!"
        show camila annoyed
        "She snaps her fingers a mere inch from my face."
        show camila angry
        "Det. Foglio" "What the hell's the matter?"
        "Det. Foglio" "Stop starin' at me like I got two heads already!"
        show camila annoyed
        "That same straightforward intensity is now focused solely on me."
        "And it makes me snap out of it in a mere matter of seconds."
        mike.say "Uh...yeah...sorry!"
        show camila talkative
        "Det. Foglio" "Okay, good enough..."
        "Det. Foglio" "So, the officer on the front desk tells me you want to report..."
        show camila surprised
        if kylie.flags.killed:
            "Det. Foglio" "What was it...a murder?"
        elif kylie.flags.rape:
            "Det. Foglio" "What was it...a rape?"
        else:
            "Det. Foglio" "What was it...stalking?"
        show camila sad
        "I nod with enthusiasm at this, keen to move on from my initial faux pas."
        "But also, I realise, because I feel on odd compulsion to obey the cop almost without question."
        mike.say "Yes...I mean yeah, that's right, officer."
        "She notices me trying to make my voice deliberately deeper."
        "And her frown is more than enough to make me stop."
        mike.say "There's this girl I went to high school with, you see."
        mike.say "Her name's Alexis...."
        show camila annoyed
        "The officer starts scribbling notes into her pocket book as quickly as I can speak the words."
        "And I can't help notice that her handwriting is atrocious as she furiously hacks away at the pages."
        if not kylie.flags.rape and not kylie.flags.killed and not "kylie_attack" in DONE:
            show camila talkative
            "Det. Foglio" "And this is the girl that you're accusing of stalking you?"
            show camila normal
            mike.say "Oh no, that's her younger sister, Kylie."
            show camila annoyed
            "The officer furrows her brows at this."
            show camila surprised
            "Det. Foglio" "Then what does this Alexis character have to do with shit?"
            show camila annoyed
            mike.say "We were in a relationship back then, and it ended...badly."
            show camila angry
            "Det. Foglio" "And this Kylie bitch is what, mad at you for breaking her sister's heart?"
            show camila annoyed
            mike.say "No, no, no - that's ancient history by now."
            mike.say "No, I ran into Kylie at college."
            mike.say "And then she started following me everywhere, telling me that she's always been obsessed with me!"
            show camila normal
            "The officer raises a quizzical eyebrow at this, clearly amused at the notion."
            show camila talkative
            "Det. Foglio" "Let me guess - because you're just that irresistible, right?"
            show camila normal
            mike.say "Yes...no...I don't know!"
            mike.say "Kylie's insane, okay?"
            mike.say "I'm scared that she's going to do something to one of my housemates...or me."
        elif kylie.flags.rape and not kylie.flags.killed:
            show camila surprised
            "Det. Foglio" "And this is the girl that you're accusing of raping you?"
            show camila normal
            mike.say "No, aren't you listening to me?"
            mike.say "Kylie's the one that raped me!"
            show camila annoyed
            "The officer furrows her brows at this."
            show camila surprised
            "Det. Foglio" "Then what does this Alexis character have to do with shit?"
            show camila normal
            mike.say "We were in a relationship back then, and it ended...badly."
            show camila angry
            "Det. Foglio" "And this Kylie bitch is what, mad at you for breaking her sister's heart?"
            show camila annoyed
            mike.say "No, no, no - that's ancient history by now."
            mike.say "No, I ran into Kylie at college."
            mike.say "And then she started following me everywhere, telling me that she's always been obsessed with me!"
            show camila normal
            "The officer raises a quizzical eyebrow at this, clearly amused at the notion."
            show camila talkative
            "Det. Foglio" "Let me guess - because you're just that irresistible, right?"
            show camila normal
            mike.say "Yes...no...I don't know!"
            mike.say "Kylie's insane, okay?"
        elif kylie.flags.killed:
            show camila surprised
            "Det. Foglio" "And this is the girl that got murdered?"
            show camila normal
            mike.say "No, aren't you listening to me?"
            mike.say "My housemate's the one that got killed!"
            mike.say "And Kylie is the murderer!"
            show camila annoyed
            "The officer furrows her brows at this."
            show camila surprised
            "Det. Foglio" "Then what does this Alexis character have to do with shit?"
            show camila normal
            mike.say "We were in a relationship back then, and it ended...badly."
            show camila angry
            "Det. Foglio" "And this Kylie bitch is what, mad at you for breaking her sister's heart?"
            show camila annoyed
            mike.say "No, no, no - that's ancient history by now."
            mike.say "No, I ran into Kylie at college."
            mike.say "And then she started following me everywhere, telling me that she's always been obsessed with me!"
            show camila normal
            "The officer raises a quizzical eyebrow at this, clearly amused at the notion."
            show camila talkative
            "Det. Foglio" "Let me guess - because you're just that irresistible, right?"
            show camila normal
            mike.say "Yes...no...I don't know!"
            mike.say "Kylie's insane, okay?"
        else:
            show camila surprised
            "Det. Foglio" "And this is the girl that you're accusing of trying to raping you?"
            show camila normal
            mike.say "No, aren't you listening to me?"
            mike.say "Kylie's the one that tried to rape me!"
            show camila annoyed
            "The officer furrows her brows at this."
            show camila surprised
            "Det. Foglio" "Then what does this Alexis character have to do with shit?"
            show camila normal
            mike.say "We were in a relationship back then, and it ended...badly."
            show camila angry
            "Det. Foglio" "And this Kylie bitch is what, mad at you for breaking her sister's heart?"
            show camila annoyed
            mike.say "No, no, no - that's ancient history by now."
            mike.say "No, I ran into Kylie at college."
            mike.say "And then she started following me everywhere, telling me that she's always been obsessed with me!"
            show camila normal
            "The officer raises a quizzical eyebrow at this, clearly amused at the notion."
            show camila talkative
            "Det. Foglio" "Let me guess - because you're just that irresistible, right?"
            show camila normal
            mike.say "Yes...no...I don't know!"
            mike.say "Kylie's insane, okay?"
        if "kylie_attack" not in DONE and kylie.flags.policestation:
            mike.say "Look, I'm not making this stuff up!"
            "I pull the disc out of my pocket and slam it down on the table."
            mike.say "She's been hanging around outside my house in the middle of the night."
            mike.say "If you don't believe me, take a look at the footage on that disc!"
            "The officer reacts to my mounting agitation by gesturing downwards with her open hands."
            show camila surprised
            "Det. Foglio" "Hey, hey - calm down, Mister [hero.family_name]."
            "Det. Foglio" "I'm just trying to establish the facts here, okay?"
            show camila normal
            "She reaches across the table and takes the disc, turning it over in her hands."
            show camila angry
            "Det. Foglio" "Tell me, has this bitch actually made any threats or turned this thing physical?"
            show camila annoyed
            mike.say "Well...no, not really."
            mike.say "But you have the evidence right there."
            mike.say "Isn't that all you need to bust her ass?"
            show camila surprised
            "The officer surprises me then by bursting into laughter."
            "It's loud and as raucous as I would have expected, but it's also infectious."
            "And she looks pretty amazing when she smiles like that too..."
            show camila surprised
            "Det. Foglio" "'Bust her ass'?"
            "Det. Foglio" "Where did you hear that shit?!?"
            show camila surprised
            mike.say "I...I guess it was on TV."
            mike.say "Sorry...I'm not very good at this."
            mike.say "TV shows and movies are all I have to go on."
            show camila wink
            "The officer puts a hand in front of her mouth, trying to force herself to stop laughing."
            show camila talkative
            "Det. Foglio" "Ah Jesus, I'm sorry, Mister [hero.family_name]."
            "Det. Foglio" "I shouldn't have done that - this is a serious matter."
            show camila sadsmile
            "I smile weakly, struggling to accept that this tough cop just apologised to me."
            mike.say "Mister [hero.family_name] makes me feel like I'm the one in the wrong here."
            show camila talkative
            "Det. Foglio" "Okay, [hero.name], you got it."
            "Det. Foglio" "I'm Camila, by the way!"
            show camila normal
            mike.say "Hey, Camila - nice to meet you."
            show camila talkative
            camila.say "You too, man, you too."
            camila.say "It makes a change to be talking to a guy honest enough to admit he's no tough cookie."
            camila.say "Especially when you spend as much time as I do around meatball cops as sensitive as a brick."
            camila.say "And most of them about half as smart too!"
            show camila normal
            "I manage to laugh at this, and not sound too much like I'm in danger of choking."
            show camila talkative
            camila.say "Okay, [hero.name] - here's the bad news."
            camila.say "As things stand, unless your Little Miss Fruitloop kicks thing up a notch..."
            show camila normal
            "She spreads her hands out in front of her for emphasis."
            show camila whining
            camila.say "I'm afraid my hands are tied!"
            show camila sad
            mike.say "But...but..."
            show camila surprised
            camila.say "Whoa there, tough guy - I didn't say you were on your own, did I?"
            show camila normal
            "She pulls a business card out of her jacket pocket and hands it over to me."
            show camila talkative
            camila.say "If shit gets real, then you call me, okay?"
            show camila normal
            mike.say "And if...well, if shit hits the fan...what then?"
            show camila talkative
            camila.say "Then you dial nine-one-one, and pray they get to you quick enough!"
            show camila normal
            $ kylie.flags.arrest = False
            $ hero.cancel_activity()
        elif "kylie_attack" in DONE and kylie.flags.killed:
            mike.say "Officer, she killed my housemate - right in front of me!"
            "Suddenly the memory of that moment returns with a vengeance."
            "I see the scene playing out in slow-motion."
            "The expression on her face."
            "The blood..."
            show camila whining
            "Det. Foglio" "I know, [hero.name], I know."
            "Det. Foglio" "Listen - there's nothing I can say or do to change what happened."
            "Det. Foglio" "And I'll move heaven and earth to catch that cold-hearted monster!"
            "Det. Foglio" "But right now, you're the one I'm more worried about..."
            show camila normal
            "At the mention of my own well being, I stop and look at her in complete silence."
            "And then it feels like a black hole is opening up beneath me, threatening to pull me down into its depths."
            mike.say "She...she tied me up."
            mike.say "She forced herself on me."
            mike.say "I...I don't even know if that counts as rape!"
            "Detective Foglio shakes her head, vigorously this time."
            show camila whining
            "Det. Foglio" "Don't even think that, [hero.name]."
            "Det. Foglio" "Don't you dare go down that dumb, macho rabbit hole!"
            "Det. Foglio" "Man or woman, it doesn't change what that psycho did to you."
            show camila normal
            "I nod, unable to put into words how much her reassurance means to me."
            "Her strength means that I can accept what happened without feeling like I'm falling apart."
            "And I'm not afraid to say that, in that moment, I feel tears welling in the corner of my eyes."
            show camila talkative
            "Det. Foglio" "I'm Camila, by the way!"
            show camila normal
            mike.say "Hey, Camila - nice to meet you."
            show camila talkative
            camila.say "You too, man, you too."
            camila.say "It makes a change to be talking to a guy honest enough to admit he's no tough cookie."
            camila.say "Especially when you spend as much time as I do around meatball cops as sensitive as a brick."
            camila.say "And most of them about half as smart too!"
            show camila normal
            "I manage to laugh at this, and not sound too much like I'm in danger of choking."
            mike.say "Thank you, Camila."
            mike.say "You don't know how much I needed to hear you say that!"
            $ kylie.flags.arrest = True
        elif "kylie_attack" in DONE and kylie.flags.rape:
            mike.say "She...she tied me up."
            mike.say "She forced herself on me."
            mike.say "I...I don't even know if that counts as rape!"
            "Detective Foglio shakes her head, vigorously this time."
            show camila whining
            "Det. Foglio" "Don't even think that, [hero.name]."
            "Det. Foglio" "Don't you dare go down that dumb, macho rabbit hole!"
            "Det. Foglio" "Man or woman, it doesn't change what that psycho did to you."
            show camila normal
            "I nod, unable to put into words how much her reassurance means to me."
            "Her strength means that I can accept what happened without feeling like I'm falling apart."
            "And I'm not afraid to say that, in that moment, I feel tears welling in the corner of my eyes."
            show camila talkative
            "Det. Foglio" "I'm Camila, by the way!"
            show camila normal
            mike.say "Hey, Camila - nice to meet you."
            show camila talkative
            camila.say "You too, man, you too."
            camila.say "It makes a change to be talking to a guy honest enough to admit he's no tough cookie."
            camila.say "Especially when you spend as much time as I do around meatball cops as sensitive as a brick."
            camila.say "And most of them about half as smart too!"
            show camila normal
            "I manage to laugh at this, and not sound too much like I'm in danger of choking."
            mike.say "Thank you, Camila."
            $ kylie.flags.arrest = True
        elif "kylie_attack" in DONE and kylie.flags.assault_video:
            mike.say "Look, I'm not making this stuff up!"
            "I pull the disc out of my pocket and slam it down on the table."
            mike.say "She's been hanging around outside my house in the middle of the night."
            mike.say "If you don't believe me, take a look at the footage on that disc!"
            "The officer reacts to my mounting agitation by gesturing downwards with her open hands."
            show camila talkative
            "Det. Foglio" "Hey, hey - calm down, Mister [hero.family_name]."
            "Det. Foglio" "I'm just trying to establish the facts here, okay?"
            "Det. Foglio" "Tell me, has this bitch actually made any threats or turned this thing physical?"
            show camila normal
            "At this point, I almost feel like I'm going to explode with frustration."
            mike.say "Watch the goddamn footage!"
            mike.say "She's right there - shocking me with a taser on my own front porch!"
            "She reaches across the table and takes the disc, turning it over in her hands."
            show camila talkative
            "Det. Foglio" "If this video shows what you say it does..."
            "Det. Foglio" "Well, let's just say that it changes the complexion of this whole thing."
            show camila normal
            "I can feel the tension starting to drain out of me as she seems to be taking me more seriously."
            "And I instantly begin to regret the irate tone that I took with her just now."
            mike.say "So you can do something about it, right?"
            mike.say "Isn't that all you need to bust her ass?"
            show camila happy at startle
            "The officer surprises me then by bursting into laughter."
            "It's loud and as raucous as I would have expected, but it's also infectious."
            "And she looks pretty amazing when she smiles like that too..."
            show camila talkative
            "Det. Foglio" "'Bust her ass'?"
            "Det. Foglio" "Where did you hear that shit?!?"
            show camila normal
            mike.say "I...I guess it was on TV."
            mike.say "Sorry...I'm not very good at this."
            mike.say "TV shows and movies are all I have to go on."
            show camila wink
            "The officer puts a hand in front of her mouth, trying to force herself to stop laughing."
            show camila talkative
            "Det. Foglio" "Ah Jesus, I'm sorry, Mister [hero.family_name]."
            "Det. Foglio" "I shouldn't have done that - this is a serious matter."
            show camila normal
            "I smile weakly, struggling to accept that this tough cop just apologised to me."
            mike.say "Mister [hero.family_name] makes me feel like I'm the one in the wrong here."
            show camila talkative
            "Det. Foglio" "Okay, [hero.name], you got it."
            "Det. Foglio" "I'm Camila, by the way!"
            show camila normal
            mike.say "Hey, Camila - nice to meet you."
            show camila talkative
            camila.say "You too, man, you too."
            camila.say "It makes a change to be talking to a guy honest enough to admit he's no tough cookie."
            camila.say "Especially when you spend as much time as I do around meatball cops as sensitive as a brick."
            camila.say "And most of them about half as smart too!"
            show camila normal
            "I manage to laugh at this, and not sound too much like I'm in danger of choking."
            show camila talkative
            camila.say "Okay, [hero.name] - here's the good news."
            camila.say "Once I review this footage, we should have enough to charge Little Miss Fruitloop."
            camila.say "After that, it's only a matter of time until we bring her in."
            show camila normal
            mike.say "But what if she gets to me before that?!?"
            mike.say "Can't I get some kind of police protection?"
            show camila talkative
            camila.say "Whoa there, tough guy - I didn't say you were on your own, did I?"
            show camila normal
            "She pulls a business card out of her jacket pocket and hands it over to me."
            show camila talkative
            camila.say "If shit gets real, then you call me, okay?"
            show camila normal
            mike.say "And if...well, if shit hits the fan...what then?"
            show camila talkative
            camila.say "Then you dial nine-one-one, and pray they get to you quick enough!"
            show camila normal
            $ kylie.flags.arrest = False
            $ hero.cancel_activity()
        else:
            "The detective lets out a sigh of frustration and pushes herself back from the table."
            "She holds her hands up in the air, shaking her head in a gesture of helplessness."
            show camila whining
            "Det. Foglio" "I'm sorry, [hero.name], you gotta believe I am."
            "Det. Foglio" "But without any kind of actual proof, there's zero chance of me doing anything about it."
            "Det. Foglio" "And my hands stay tied as long as that's the case."
            show camila normal
            $ kylie.flags.arrest = False
            $ hero.cancel_activity()
    $ kylie.flags.policestation = False
    return

label kylie_investigation_3:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Camila")
    if not result:
        $ hero.cancel_event()
        return
    "Enough time had passed since what Kylie did to me that fateful night for the details to start fading a little."
    "Sure, I was still getting the occasional flashback, but it wasn't as raw as it once was, or as scary to recall either."
    "But then I hear the sound of my phone ringing, and glance down to see that the call is from Camila, the cop working the case."
    "I can't ignore it - the whole thing is way too important for that."
    "So reluctantly, I pick up the phone and answer the call..."
    mike.say "Hey, Camila."
    mike.say "Good to hear from you."
    camila.say "Really, [hero.name]?"
    camila.say "That's not usually what I hear on a call like this."
    "I shrug, even though the gesture goes unseen by Camila."
    mike.say "Well, I'm not going to shoot the messenger, Camila!"
    "I hear her chuckle on the other end of the line."
    "And the sound cheers me up more than I expect it to."
    camila.say "Yeah, save that for after you hear my news, [hero.name]!"
    camila.say "You free to come down the station some time today?"
    mike.say "Sure, Camila."
    mike.say "I'll be there as soon as I can."
    show bg policestation with fade
    "As soon as I wrap up the call, I drop what I was doing and head straight over to the police station."
    "Once there, I don't have to spend long sitting in the interview room before the door opens behind me."
    "This comes as a relief, stopping my mind from wandering back to the previous times I was in there."
    show camila talkative with easeinright
    camila.say "Hello again, [hero.name]."
    show camila normal
    mike.say "Detective Foglio."
    "Camila gives me a frown of mock disapproval as she sits down across the table."
    "She puts the file she was carrying down and looks me in the eye."
    show camila talkative
    camila.say "I told you, call me Camila - or I'll have you arrested!"
    show camila normal
    mike.say "Ah, on what charge, Dete...Camila?"
    show camila talkative
    camila.say "Oh, I'm sure I can make something up."
    camila.say "You know how we cops are..."
    camila.say "But seriously, I didn't ask you here to shoot the shit."
    show camila normal
    mike.say "No, I guess not."
    "Camila opens the file and takes a couple of moments to read something I can't see for myself."
    show camila talkative
    camila.say "Long story short, [hero.name] - Little Miss Fruitloop's going down."
    show camila normal
    "It takes a moment for the truth of what she's saying to fully sink in."
    "The news is obviously something I'd been waiting to hear."
    "But it still doesn't seem quite real."
    show camila talkative
    camila.say "Did you hear what I said, [hero.name]?"
    camila.say "Kylie's going to spend a hell of a long time behind bars!"
    show camila normal
    "I nod silently, more out of instinct than actual comprehension."
    show camila talkative
    camila.say "Geez, [hero.name]."
    camila.say "After all the bitch put you through."
    camila.say "I'd have though you'd be over the fucking moon!"
    show camila normal
    mike.say "No..."
    mike.say "Sorry, I am...really."
    mike.say "It's just...I thought the news would make me happy."
    mike.say "But I kind of can't help feeling a little bit sorry for her."
    mike.say "Crazy, huh?"
    show camila surprised
    "Camila looks at me like I've gone insane, shaking her head in bafflement."
    show camila talkative
    camila.say "I'd say so, [hero.name]."
    camila.say "If it were me, I'd be happy to see her rot."
    show camila normal
    "But then she stops and studies me intently for a moment."
    "And it's as if trying to weigh up something that's bothering her."
    "I can't help sweating a little as I become the full focus of her scrutiny."
    show camila talkative
    camila.say "But you're not me, are you, [hero.name]."
    camila.say "And maybe that's a good thing..."
    show camila normal
    "Camila lets the thought float on the air for a moment, looking thoughtful."
    "But then she seems to shake it off and become her normal, brusque self once more."
    show camila talkative
    camila.say "Sorry...that's about it as far as you need to be concerned."
    camila.say "We'll be in touch if we need anything more from you."
    camila.say "And if you need something from me..."
    camila.say "Well, you got my number, okay?"
    show camila normal
    mike.say "Okay, Camila - and thanks."
    show camila talkative
    camila.say "Just doing my job, [hero.name], just doing my job."
    camila.say "See you around..."
    show camila normal
    "I nod and smile as Camila leads me out of the room and towards the exit."
    "And though I hope I never have to see the inside of a police station again, I can't say the same about her..."
    $ kylie.flags.schedule = "jail"
    $ kylie.flags.nodate = True
    $ kylie.flags.noproposedate = True
    $ Harem.leave_by_name("taming", "kylie")
    $ hero.calendar.find_and_remove(girl="kylie")
    return

label kylie_prison_visit_1:
    scene bg jail
    show kylie talkative jail
    with fade
    kylie.say "Oh, [hero.name]..."
    show kylie happy
    kylie.say "I knew that you'd come again!"
    show kylie shout
    kylie.say "I just knew that you would never abandon me!"
    kylie.say "I knew that you'd leave that bitch and come back to me!"
    show kylie normal
    "Part of me simply can't believe what Kylie said the last time."
    "That she think what she did was just misunderstanding."
    "I know that I should stand up to Kylie, put her in her place."
    "But another part of me can't help feeling sorry for her."
    "Because maybe she is crazy enough to wind up in a place this."
    "And if that's the case, doesn't she need help to get better?"
    menu:
        "Sympathise with Kylie":
            "I don't know what it is about Kylie that makes me act this way."
            "I know that she's crazy and I know that she's out of touch with reality."
            "But still I find myself smiling and nodding at what she's saying."
            mike.say "It's okay, Kylie."
            mike.say "You're in a safe place now."
            mike.say "Somewhere you can get all the help you need."
            show kylie normal
            "Kylie shakes her head at this."
            "And she presses herself closer to the bars."
            show kylie vangry
            kylie.say "No, no, no!"
            kylie.say "I don't need any of this, [hero.name]."
            show kylie sadhappy
            kylie.say "All I need is you!"
            show kylie sad
            "I can't help feeling flattered at this."
            "Sure, I know that Kylie's not playing with a full deck."
            "But she's pretty much throwing herself at my feet right now!"
            mike.say "Don't worry, Kylie."
            mike.say "I'm here for you."
            mike.say "I'll always be here for you."
            show kylie smile
            "Kylie nods eagerly, giving my ego another boost."
            show kylie shy
            "And then she looks to one side, biting her lip."
            show kylie blush
            kylie.say "Actually, [hero.name]..."
            kylie.say "About the conjugal visit..."
            show kylie shy
            "I swallow at the implications of the word."
            "The mere idea of having sex with Kylie in a place like this is scary."
            "But it's that good kind of scary that can't help but turn you on."
            menu:
                "Agree to a conjugal visit":
                    "My head's nodding before I even know it."
                    "And my mouth struggles to keep up."
                    mike.say "Y...yeah, Kylie."
                    mike.say "That sounds like a great idea!"
                    show kylie smile
                    "Kylie's smile is so wide it almost makes her look unhinged."
                    show kylie normal
                    "And her eyes somehow seem to become larger still."
                    show kylie shout
                    kylie.say "I knew you'd understand, [hero.name]."
                    kylie.say "I'm a woman with needs, genuine physical needs!"
                    hide kylie
                    show kylie close blush jail
                    kylie.say "And the thing I need most is you!"
                    "Kylie's practically squashing herself against the bars by now."
                    "Her breath is steaming on the surface before her face."
                    "And her breasts are squashed together, almost bursting out of her jumpsuit."
                    "In fact, I'm afraid she's going to start playing with herself any moment!"
                    mike.say "Wow, Kylie!"
                    mike.say "How did it get to be that hour?"
                    mike.say "I think our time's about up for today."
                    mike.say "But I'll ask about that conjugal visit on the way out."
                    hide kylie
                    show kylie jail shout
                    kylie.say "Okay, [hero.name]."
                    kylie.say "You're all that I'll think about until next time."
                    show kylie normal
                    "I wave goodbye to Kylie as I turn to leave."
                    hide kylie with dissolve
                    "My mind already racing as I try to make sense of my feelings for her."
                    $ kylie.flags.agreed_conjugal_visit = True
                "Put Kylie off":
                    "All the same, I'm still more than a little scared of Kylie."
                    "So maybe sex with a psycho will have to wait."
                    mike.say "Ah..."
                    mike.say "Lets put that one down as a maybe, yeah?"
                    mike.say "At least until you're well on the mend?"
                    show kylie sad
                    "Kylie looks instantly disappointed."
                    "And for a moment, I think she's going to flip out."
                    show kylie annoyed
                    "But then she pauses and the expression on her face changes subtly."
                    "It reminds me of an animal that's been caught out once before."
                    "And now it's changing its tactics to avoid the same fate."
                    show kylie whining
                    kylie.say "Maybe you're right, [hero.name]."
                    show kylie sadhappy
                    kylie.say "We shouldn't rush things."
                    show kylie normal
                    "I nod, happy to have managed to dodge that particular bullet."
                    mike.say "We can talk about that the next time I come to visit."
                    mike.say "But I think our time's about up for today."
                    show kylie happy
                    kylie.say "Okay, [hero.name]."
                    kylie.say "You're all that I'll think about until next time."
                    show kylie normal
                    "I wave goodbye to Kylie as I turn to leave."
                    hide kylie with dissolve
                    "My mind already racing as I try to make sense of my feelings for her."
        "Put Kylie in her place":
            "I shake my head, pushing all of my sympathy for Kylie aside."
            "It's people indulging her and ignoring her craziness that's the problem here."
            "If someone had put their foot down earlier, maybe none of this would have happened."
            mike.say "That's not why I'm here, Kylie."
            mike.say "I didn't come to visit you so we could pick up where we left off."
            mike.say "You're way too far gone for that to ever happen."
            show kylie sad
            "Now it's Kylie's turn to shake her head."
            "She presses her hands against the bars."
            "And she looks as desperate as I've ever seen her."
            show kylie whining
            kylie.say "You don't really mean that, [hero.name]."
            show kylie talkative
            kylie.say "I know you don't!"
            kylie.say "You're angry with me, I get that."
            show kylie shout
            kylie.say "But we can work it out together - because we love each other!"
            show kylie normal
            "I take a step backwards from the bars."
            show kylie stuned
            "And Kylie seems to understand what this means."
            "Her eyes are wide, like a frightened animal."
            mike.say "No, Kylie, we can't."
            mike.say "I thought I loved you, I really did."
            mike.say "But we can't be together while you're like this."
            mike.say "You're sick and you need to get better."
            mike.say "And I don't want to see you again until that happens."
            hide kylie with dissolve
            "With that, I turn and walk out before Kylie can respond."
            "I can hear her behind me, pleading and begging."
            "But I don't pay any attention to her."
            "Because I'm afraid of what I'll do if I make out any of her words."
    return

label kylie_trial_1:
    "Normally I just slope into the hallway when I hear the mail hit the doormat and look it over."
    "That's because I can tell from a glance if there's anything worth my attention in there."
    "But most of it is usually circulars, advertising and those scam promotions claiming you've won a prize."
    "So usually I take one glance and then walk away to do something more productive with my time."
    "But today there's something on the doormat that catches my eye."
    "It's a pretty official-looking letter in a fancy envelope with a printed address."
    "And it has my name printed on there too, so I guess it's for me."
    "Stooping to pick it up, I also see the words {b}'Private & Confidential'{/b} on there too!"
    "I have to admit, the sends a shiver down my spine."
    "Hell, it's even enough to make my ass tighten up!"
    "This thing has bad news written all over it."
    "I already feel like it's going to be a demand for money or something similarly unwelcome."
    "But there's no sense in trying to avoid the inevitable."
    play sound paper_ripping_1
    "So I tear open the envelope as soon as I stand up."
    play sound paper_page
    "Then I unfold and start to read the contents right there in the hallway."
    "My stomach lurches as soon as I see an official logo on the letter too."
    with vpunch
    "Shit - it's from the courthouse!"
    "Something about me needing to attend a trial there."
    "And it's for...what exactly?"
    "Oh man - it's a fucking murder trial!"
    "And here I was thinking that I'd probably avoid jury duty."
    "I'm already scanning the letter, looking for the exemptions when I realise my mistake."
    "It's not asking me to be part of the jury at all."
    "In fact, it's far worse than that."
    "This is about Kylie's trial."
    "And I'm being called as a witness!"
    "I lean back against the wall, the letter crumpled in my hand."
    "And when I say lean, I kind of mean collapse and the wall holds me up."
    "Man...I thought that this was almost over."
    "Kylie's behind bars, and there's more than enough evidence to send her down."
    "I was expecting to be able to forget all about what happened until she was in jail."
    "But I suppose that was more than a little naive of me."
    scene bg livingroom at blur(8), dark
    show kylie yandere knife at center, zoomAt (1.2, (640, 800))
    show kylie at center, traveling (1.75, 1.0, (640, 1200))
    pause 1.0
    scene bg livingroom with dissolve
    "I mean, I was pretty much to only witness to what Kylie did that night."
    "And it's not like she's going to hold up her hands and admit to being guilty."
    "Taking a deep breath, I force myself to stand up."
    "Then I straighten out the letter in my hand."
    "I need to read this thing properly, to find out what's expected of me."
    "After all, I have to do everything I can to see that justice is done."
    if kylie.flags.killed == 'bree':
        show bree casual a normal at center, opacity(0.65) with dissolve
        "I owe [bree.name] that much, don't I?"
        hide bree with dissolve
    elif kylie.flags.killed == 'sasha':
        show sasha casual a normal at center, opacity(0.65) with dissolve
        "I owe Sasha that much, don't I?"
        hide sasha with dissolve
    "And what about me too?"
    "If Kylie gets away with this, then she's going to be coming for me."
    "Either to kill me as well, or...I don't know, catch me and torture me!"
    "For all I know, she could still be convinced that she loves me."
    "That we're supposed to be together!"
    "Doing the best I can to look confident as I start to read the letter again."
    "But I can still feel the fear twisting in my gut the whole time."
    "Did Kylie really get to me that much?"
    "Am I really that afraid of her?"
    "I guess I'm going to find out when I'm in the witness stand!"
    $ hero.calendar.add(game.days_played + 10, LabelAppointment((10, 22), "kylie", "Attend Kylie's trial", "kylie_trial_2", "kylie_trial_2_missed"))
    scene bg black with dissolve
    return

label kylie_trial_2_missed:
    $ DONE['kylie_trial_2_missed'] = game.days_played
    "..."
    "....."
    "{b}DAMN IT!{/b}" with hpunch
    "I jut remember I had to attend Kylie's trial today!"
    "I will surely have information on how it happened."
    if kylie.pregnant:
        $ kylie.flags.trial_verdict = "crazy"
    else:
        $ kylie.flags.trial_verdict = "tried_but_guilty"
        $ kylie.flags.engagedmike = False
        $ kylie.flags.nopropose = True
        $ kylie.flags.nopreg = True
        $ hero.calendar.add(game.days_played + 30, LabelAppointment((18, 22), "kylie", "Attend Kylie's execution", "kylie_trial_3", "kylie_trial_3_missed"))
    return

label kylie_trial_2(appointment=None):
    $ DONE['kylie_trial_2'] = game.days_played

    "I'm all dressed up in what I hope is a respectable-looking suit."
    "I've been over what I have to say in my head more than a hundred times."
    "And I keep telling myself that all I have to do is tell the truth."
    "But still I'm sweating like crazy and feeling like a bag of nerves."
    "So when they finally call me to the stand, I almost jump out of my skin!"
    show kylie trial witness at center, zoomAt(1.5, (940, 1075)) with fade
    "I walk to the witness stand, trying to keep my gaze ahead of me."
    "Most of the time I've been in the courtroom, I was staring at the floor."
    "And a good deal of what's been said just went right over my head."
    "But now I find myself looking up for the first time."
    show kylie trial witness at center, traveling(1.85, 2.0, (240, 1275))
    "And when I do so, it's straight into Kylie's eyes."
    "The sight of her sitting there hits me like a punch on the jaw."
    "Instantly I'm back in the room on the night of the murder."
    "Part of me is expecting her to jump out of her seat and run at me."
    if kylie.flags.killed == 'bree':
        "For her to attack me with that damn box-cutter, just like she did poor [bree.name]!"
    if kylie.flags.killed == 'sasha':
        "For her to attack me with that damn box-cutter, just like she did poor Sasha!"
    "But instead she just sits there, staring at me with an oddly calm look on her face."
    "It's only as I climb into the witness stand and sit down that it begins to make sense to me."
    "Of course Kylie's insane, as crazy as a box of fucking frogs."
    "But she's not sitting in your own shit crazy."
    "More like cold and calculating crazy."
    "She's obviously doing the best she can to make herself look calm and sane."
    "For a moment I'm sure that it can't work."
    "But then I realise that it almost worked on me just now."
    "If I didn't know what she'd done, I'd have been none the wiser."
    "I'd have just walked into the court and wondered why the hell she was sitting in the dock!"
    "Kylie smiles as soon as our eyes meet."
    "Like we're old friends bumping into each other in the street."
    "But all I can see is the same look she had on her face that night."
    "Judge Clooney" "Ahem..."
    hide kylie
    show kylie trial witness
    with hpunch
    "It's only when I hear the judge cough that I snap out of it."
    "And I realise that Kylie's frozen me to the spot with her stare."
    "I force myself to look away and hurry into the witness stand."
    "Someone offers me a copy of the bible."
    "And I put my hand on it like I'm on autopilot."
    "Judge Clooney" "Do you swear to tell the truth..."
    "Judge Clooney" "The whole truth..."
    "Judge Clooney" "And nothing but the truth?"
    mike.say "I..."
    mike.say "I do."
    "The judge nods, and the questioning begins in earnest."
    "Once we're into it, things go pretty much as you'd expect."
    "The lawyer defending Kylie tries to make me admit that she's disturbed."
    "But that she really didn't know what she was doing that night."
    "And the lawyer for the prosecution wants me to say that she's a cold-blooded killer."
    "That she's using the notion of being crazy to hide the fact she knew what she was doing."
    "The truth is that the pair of them are driving ME crazy!"
    "They both want me to say exactly what'll make their case."
    "But the one thing that they manage to do is make me actually think for myself."
    "And for the first time, I know that I'm weighing it all up in my head."
    "So as soon as I get the chance, I decide to speak up for myself."
    menu:
        "Protest Kylie's innocence":
            "I don't know if it was that last look from Kylie that did it."
            "Or of I knew that I felt this way about her the whole time."
            "But either way, I just know that she's the victim in all of this."
            mike.say "Your honour..."
            mike.say "What Kylie did was a terrible thing."
            mike.say "But I truly believe that she couldn't help herself."
            mike.say "And that she didn't know it was wrong."
            "I can hear gasps from the people watching in the public gallery."
            "And I know that some of the victim's relatives must be sitting out there."
            "But I try to ignore that thought and press on."
            mike.say "Kylie's spent her entire life not being listened to."
            mike.say "Her entire life not being helped."
            mike.say "I think it's time that changed."
            mike.say "She's as much a victim here as the person that was killed!"
            if (not kylie.pregnant and hero.charm >= 120 and hero.knowledge >= 80) or (kylie.pregnant and hero.charm >= 110 and hero.knowledge >= 80):
                $ kylie.flags.trial_verdict = "innocent"
            else:
                $ kylie.flags.trial_verdict = "tried_but_guilty"
        "Plead Kylie's insanity":
            "I don't know if it was that last look from Kylie that did it."
            "Or of I knew that I felt this way about her the whole time."
            "But either way, I just know that Kylie needs to be somewhere safe and secure."
            "Somewhere she can't hurt anyone else, or herself."
            mike.say "Your honour..."
            mike.say "What Kylie did was a terrible thing."
            mike.say "But I truly believe that she can change."
            "I can hear gasps from the people watching in the public gallery."
            "And I know that some of the victim's relatives must be sitting out there."
            "But I try to ignore that thought and press on."
            mike.say "With the right help, I think she'll come to understand her crimes."
            mike.say "Sure, you're going to want to lock her away for the rest of her life."
            mike.say "But if she's executed, then the life of the person she killed means nothing."
            if (not kylie.pregnant and hero.charm >= 80 and hero.knowledge >= 110) or (kylie.pregnant and hero.charm >= 70 and hero.knowledge >= 110):
                $ kylie.flags.trial_verdict = "crazy"
            else:
                $ kylie.flags.trial_verdict = "tried_but_guilty"
        "Describe Kylie as a cold-blooded killer":
            "I don't know if it was that last look from Kylie that did it."
            "Or of I knew that I felt this way about her the whole time."
            "But either way, I just know that she's a monster."
            "And that she needs to be punished for what she did."
            mike.say "Your honour..."
            mike.say "What Kylie did was a terrible thing."
            mike.say "And I truly believe that she knew what she was doing that night."
            "I can hear gasps from the people watching in the public gallery."
            "And I know that some of the Kylie's relatives must be sitting out there."
            "Maybe Alexis is amongst them too."
            "But I try to ignore that thought and press on."
            mike.say "There's only one way that things can be put right."
            mike.say "There has to be a balance."
            mike.say "A life for a life."
            mike.say "I'm pleading with you..."
            show kylie trial witness cry with hpunch
            mike.say "SEND THAT PSYCHO BITCH TO THE CHAIR!"
            $ kylie.flags.trial_verdict = "guilty"
    "The next thing I know, there's someone ushering me out of the witness stand."
    "Which I guess means that the judge has heard all they want to from me."
    "So now all I can do is go back to my seat and wait to see what happens."
    "There's some more legal wrangling from both sides."
    "But I find it hard to follow any of it as I'm lost in my own thoughts."


    "What does catch my attention though, is when the judge hammers down his gavel."
    hide kylie
    show kylie trial witness at center, zoomAt(1.9, (680, 1360))
    with fade
    "Judge Clooney" "I've heard the arguments from both sides."
    "Judge Clooney" "And now it's time for me to render my verdict..."
    "Everyone in the courtroom falls silent at this."
    "And it feels like everyone holds their breath too."
    "All waiting to hear what the judge says next."
    if kylie.flags.trial_verdict == "innocent":
        "Judge Clooney" "It is my passionate belief that this woman is mentally ill."
        "Judge Clooney" "And that she could therefore not have been responsible for her crimes."
        "Upon hearing this, the public gallery erupts."
        "I can hear people hurling abuse and calling for justice."
        "But the judge just ignores them and carries on with his verdict."
        "Judge Clooney" "I am requiring the defendant to undergo psychological assessment."
        "Judge Clooney" "And she will be required to submit to strenuous supervision."
        "Judge Clooney" "But there will be no custodial sentence."
        "Judge Clooney" "And she will be free to leave custody once the trial is over."


        "The judge hammers down his gavel again, making it official."
        "There's still the sound of protests in the background."
        "But all I feel is an immense sense of relief."
        "Feeling like I'm being watched, I look up."
        hide kylie
        show kylie trial witness
        with fade
        "And it's then that I see Kylie staring at me across the courtroom."
        "She smiles and then holds up her hands in the shape of a heart."
        "And despite everything that's happened, I feel mine start to beat faster!"
        $ kylie.flags.schedule = "default"
        $ kylie.flags.nodate = False
        $ kylie.flags.noproposedate = False
    elif kylie.flags.trial_verdict == "crazy":
        "Judge Clooney" "It is my passionate belief that this woman is mentally ill."
        "Judge Clooney" "And that she could therefore not have been responsible for her crimes."
        "Upon hearing this, the public gallery erupts."
        "I can hear people hurling abuse and calling for justice."
        "But the judge just ignores them and carries on with his verdict."
        "Judge Clooney" "I am requiring the defendant to undergo psychological assessment."
        "Judge Clooney" "But based on the danger that she poses, she will not be released from custody."
        "Judge Clooney" "Instead she will be sentenced to a minimum of ten years."
        "Judge Clooney" "Which will be served in a high-security mental facility."


        "The judge hammers down his gavel again, making it official."
        "And most of the sounds of protest are replaced by cheers of approval."
        "But all I feel is an immense sense of relief."
        "Feeling like I'm being watched, I look up."
        hide kylie
        show kylie trial witness
        with fade
        "And it's then that I see Kylie staring at me across the courtroom."
        "Her face is unreadable, almost bereft of emotion."
        "And she keeps on staring at me like that as she's lead away."
    elif kylie.flags.trial_verdict == "guilty" or kylie.flags.trial_verdict == "tried_but_guilty":
        "Judge Clooney" "It is my passionate belief that this woman is mentally ill."
        "Judge Clooney" "But also that this did not prevent her knowing what she was doing."
        "Judge Clooney" "I am convinced that she was fully aware of her crimes when committing them."
        "Upon hearing this, the public gallery erupts."
        "I can hear people hurling abuse and calling for justice."
        "But the judge just ignores them and carries on with his verdict."
        "Judge Clooney" "Under such circumstances, there can be only one verdict."
        "Judge Clooney" "Much as it pains me to invoke this punishment..."
        "Judge Clooney" "I rule that the defendant be taken from here to a place of execution."
        "Judge Clooney" "That she be put to death using the electric chair."





        "The judge hammers down his gavel again, making it official."
        "And most of the sounds of protest are replaced by cheers of approval."
        "But all I feel is an immense sense of relief."
        hide kylie
        show kylie trial witness
        with fade
        "Feeling like I'm being watched, I look up."
        "And it's then that I see Kylie staring at me across the courtroom."
        "Her face is unreadable, almost bereft of emotion."
        "And she keeps on staring at me like that as she's lead away."
        if kylie.flags.trial_verdict == "tried_but_guilty":
            "Maybe I could have done more to help her during the trial..."
            "I should have prepare a speech, study law, and for what it's worth, wear better clothes..."
        $ kylie.flags.engagedmike = False
        $ kylie.flags.nopropose = True
        $ kylie.flags.nopreg = True
        $ hero.calendar.add(game.days_played + 30, LabelAppointment((18, 22), "kylie", "Attend Kylie's execution", "kylie_trial_3", "kylie_trial_3_missed"))
    scene bg black with dissolve
    return

label kylie_trial_3_missed:
    $ DONE['kylie_trial_3_missed'] = game.days_played
    $ kylie.unpreg()
    "..."
    "....."
    "{b}FIRETRUCK!{/b}" with hpunch
    "I jut remember I had to attend Kylie's execution today!"
    "I wonder what happened since I was not there to see it..."
    if kylie.flags.trial_verdict == "tried_but_guilty":
        $ kylie.set_gone_forever()
    else:
        $ kylie.flags.revenge_attack_delay = TemporaryFlag(True, randint(75, 105))
        $ kylie.hide()
    return

label kylie_trial_3(appointment=None):
    $ DONE['kylie_trial_3'] = game.days_played
    $ kylie.unpreg()



    show kylie trial execution at center, zoomAt(1.5, (940, 1075)) with fade
    "And here I was thinking that being a witness at a murder trial was the craziest thing possible."
    "But never in my wildest dreams did I ever think I'd find myself attending an actual execution!"
    "I've only ever seen this kind of thing in movies and TV shows before now."
    "And part of me was actually surprised to discover we still had the death penalty in this country."
    "But here I am, shuffling into the room where they apparently do this kind of thing all the time."
    "I've kind of taken all of my cues for today from what I know about attending funerals."
    "You know, what with death being the common theme there?"
    "So I'm dressed in what I hope is a smart yet sombre outfit that suits the occasion."
    "And I'm being very quiet, trying to seem respectful and serious about the proceedings."
    "I had been hoping to sneak in and sit at the back somewhere, keeping myself out of sight."
    "But paranoia about being late means that I'm one of the first people to turn up."
    "So when the doors open, I find myself being ushered inside and down to the first row."
    "This means that I'm sitting front and centre, staring straight at the damn chair!"
    "I look around, but it's no good."
    "The place is already almost full."
    "If I try to move now, I'll just cause a scene."
    "So instead I try to hunker down in my seat, hoping no one will recognise me."
    "I mean, it's not my fault that it came to this."
    "Sure, I made a passionate plea for it at Kylie's trial."
    "But she did kind of play her part in actually murdering one of my housemates!"
    "Things only get worse when they actually bring Kylie into the room."
    hide kylie
    show kylie trial execution
    with fade
    "I try not to look at her, but I just can't help it."
    "Come on, cut me some slack - I'm actually going to see someone I thought I loved fry!"
    "And the very moment that I look in her direction, Kylie spots me too."
    "It's like she zeroes in on me with unwavering precision."
    "Like she was one hundred percent sure I'd be here."
    "Her eyes are fixed on me as she's lead across the stage and to the chair."
    "And they stay on me as she's made to sit in it and strapped down too."
    "I feel like her gaze is drawing attention to me from the crowd as well."
    "Somehow, even though they're here to see her execution, everyone is looking at me!"
    "I keep telling myself that this will all be over soon."
    "The guards aren't wasting any time getting things ready."
    "I'm sure they want this done as quickly as possible."
    "Then one of them steps forwards with something black in his hand."
    show kylie trial execution helmet
    "It takes me a moment to realise this must be the hood they put over the head of the condemned."
    "I feel my guts churn and then turn to water."
    if kylie.flags.trial_verdict == "guilty":
        "This is it..."
        "It's actually going to happen."
    "Guard" "Does the condemned have any last words?"
    if kylie.flags.trial_verdict == "guilty":
        show kylie trial execution scaredmike
        "I have to stop myself from jumping up and objecting."
        "Last words?!?"
        "I thought that was just something that Hollywood came up with!"
        "Oh god..."
    show kylie trial execution helmet at center, zoomAt(1.75, (300, 1040))
    kylie.say "Yes..."
    kylie.say "Yes, I do!"
    "I can feel Kylie's gaze on me now."
    "And there's nothing I can do to keep from looking her in the eye."
    kylie.say "[hero.name]..."
    show kylie trial execution crazy
    kylie.say "I'm so happy you came along today."
    kylie.say "Because it proves to me that the love we have is real."
    "I can hear people muttering and gasping all around me."
    if kylie.flags.trial_verdict == "guilty":
        "This is a nightmare, an utter living nightmare."
        "Even when she's being executed, Kylie's still playing games."
        "Somehow she's managing to make this whole thing about me!"
    kylie.say "I want you to know that I forgive you, [hero.name]."
    kylie.say "I want you to know that I love you."
    kylie.say "And that even death isn't a barrier to that love."
    kylie.say "What happens here today won't stop me coming back to be with you!"
    hide kylie
    show kylie trial execution crazy helmet
    with fade
    "With that, Kylie nods to the guard holding the hood."
    "He pulls it over her head, then nods in turn to the guard by the switch."
    "Part of me wants to scream at them to stop, to let me talk to Kylie."
    if kylie.flags.trial_verdict == "guilty":
        "What in the hell did she mean by that last line?"
        "How can death not stop that crazy bitch getting to me?!?"


    show kylie trial execution scaredmike pain fx with hpunch
    "But it's too late, as electricity crackles through the chair."
    "The lights in the room dim as Kylie's body jerks against the restraints."
    "Mercifully I can't hear the sounds of her screaming in pain."
    "But soon the air is filled with the sickening smell of charred flesh."
    "And the worst thing is that it's true."
    "It really does smell like barbecued pork!"
    stop sound fadeout 0.5
    show kylie trial execution dying -fx with dissolve

    if renpy.has_label("kylie_achievement_7") and not game.flags.cheat:
        call kylie_achievement_7 from _call_kylie_achievement_7
    "Once it's all over, everyone around me starts to get up and leave."
    "But I just find myself sitting there until I'm the last one left."
    "Part of me can't actually believe that Kylie's dead."
    "I keep expecting her to leap up like the killer in a horror movie."
    show kylie trial execution -scaredmike
    "But in the end someone comes over and asks me to leave in a polite, yet firm tone."
    "So I shuffle back out of the place, still trying to believe what I just saw."
    "I know that I'm being stupid, reading too much into Kylie's last words."
    "But part of me still wants to keep looking back over my shoulder."
    $ kylie.set_gone_forever()
    scene bg black with dissolve
    return

label kylie_rattle:
    "It seems that the lights around the front of the house are on."
    "Something keeps triggering the sensors and lighting up the front yard."
    "This means that the windows are lit up every time it happens."
    "Usually it's just a random cat or fox roaming around the neighbourhood in the dark."
    "But tonight it's happening far too often to be something as natural and innocent as that."
    return

label kylie_attack:
    if renpy.has_label("kylie_achievement_3") and not game.flags.cheat:
        call kylie_achievement_3 from _call_kylie_achievement_3
    show bg house
    if game.flags.kyliecameraplaced:
        $ kylie.flags.assault_video = True
    $ kylie.flags.policestation = True
    "Peeking outside, I can get a pretty good view of the front of the house."
    "I can see all almost all of the front yard and a good portion of the porch around the front door too."
    "At first I can't make out anything amiss down there, but then I am looking for some kind of animal, maybe scuffling around the bins."
    "This means that I don't notice there's someone lurking around the porch until I take a second look."
    "But there they are - an unmistakably human figure standing close to the front door."
    "I try not to panic as I watch the potential intruder, struggling to see just what they're doing."
    "The lock on the front door is pretty sturdy, and I'm fairly sure all of the ground floor windows are locked too."
    "As the figure moves around a little more, I manage to catch a glimpse of long, blonde hair."
    "Could it be [bree.name], trying to get in after losing her keys?"
    "No, that can't be it."
    "The person at the door looks taller, her hair longer and paler than [bree.name]'s."
    "Who do I know who fits that description and might be lurking in my street in the middle of the night?"
    "And then it hits me - who else but Kylie?"
    "At that point, I don't know what comes over me, but I feel so angry all of a sudden."
    "How dare she do this to me, hanging around outside my house like some kind of crazed stalker?!?"
    show kylie a normal with dissolve
    "I yank the door open and find Kylie standing before me."
    "Now I admit I was expecting her to at least look surprised at being caught in the act."
    "But instead she greets me with a smile and a little wave."
    "For all the world, she looks as innocent as if she's appeared in the middle of the afternoon and bringing freshly-baked cookies."
    show kylie a shout
    kylie.say "Hey, [hero.name] - I hope I didn't wake you."
    show kylie a normal
    mike.say "No you didn't but... What the hell, Kylie - it's the middle of the night!"
    show kylie a shout
    kylie.say "Well, duh - I know what time it is, silly!"
    kylie.say "That's why I was knocking so quietly!"
    show kylie a normal
    mike.say "But...that wouldn't have woken me up at all."
    show kylie a happy
    kylie.say "It must have, because here you are - and pretty grumpy too, I might add!"
    show kylie a normal
    "I hold a hand up to halt the conversation and shake my head in the hope of waking myself up."
    "My intention was to chase Kylie off, not get drawn into a ridiculous discussion with her on the doorstep."
    mike.say "Never mind all that crap, Kylie."
    mike.say "What in the hell do you want?"
    "If she's at all aware of the irritation and annoyance in my tone, Kylie chooses to ignore it completely."
    show kylie b blush
    kylie.say "Oh, yeah - I came over to have sex with you, [hero.name]."
    kylie.say "I guess you could say it's a booty call!"
    mike.say "You what?!?"
    kylie.say "We're going to have sex - what's so hard to understand about that?"
    kylie.say "It's the twenty-first century, [hero.name]."
    kylie.say "We girls are empowered to go out there and get what we want."
    kylie.say "And I want you to have sex with me and give me a baby."
    show kylie smile
    "She's so open and blunt about it that I find myself almost lost for words."
    mike.say "Are you actually crazy, Kylie?"
    mike.say "You think I'm actually in the mood to have sex with you right now?!?"
    show kylie crazyhappy
    "Kylie giggles and shakes her head at this, as if finding the idea as ludicrous as I do myself."
    show kylie shout
    kylie.say "Of course not - you just got woken up in the middle of the night."
    kylie.say "That's why I'm going to give you all the encouragement you need to get it up for me!"
    show kylie normal
    mike.say "No, Kylie, you're not."
    mike.say "You're going to get out of here before I call the police!"
    "Kylie shakes her head again, still seeming to think I'm not being serious."
    "It's then that I hear a weird crackling sound, kind of like an electrical device shorting out."
    show kylie taser
    "I only catch the briefest glimpse of the Taser in Kylie's hand before she thrusts it into my back."
    show kylie taser shivers lightning
    play sound taser
    pause 0.2
    with hpunch
    "The pain is instant and like being kicked in the gut by a mule."
    show kylie taser -shivers -lightning
    "There's no staggering around or trying to fight off the effects, and I black out a second later."
    play sound body_fall
    pause 0.3
    scene bg house at blur(16), dark, dark with dissolve
    "The pain is still there when I come round, making me groggy and disoriented."
    "That makes it seem like only a moment has passed since I was knocked out."
    "Maybe I could make more sense of where I am and why, if it wasn't for the fact I'm woken up choking and gasping for air."
    "I cough violently, spitting water everywhere."
    "But instantly I feel a hand clamping my jaw shut, forcing me to breathe through my nose."
    "At the same time another seems to be massaging my throat with more force than skill."
    "All I can do is swallow what little water remains inside of my mouth in a couple of gagging gulps."
    "And as I do this, I can feel something else travelling down my throat along with it."
    scene bg bedroom1 at blur(16), dark
    show kylie happy at center, zoomAt(1.5, (640, 1040)), dark
    with dissolve
    kylie.say "There you go - you took your medicine, like a good boy!"
    show kylie normal
    mike.say "Uurgh...what the...fuck!"
    show kylie shout
    kylie.say "Whoa, slow down there, [hero.name]."
    kylie.say "We'll get to that part soon enough, you naughty thing!"
    show kylie normal
    "I respond to this in the most logical way possible, by trying to sit up and push Kylie away from me."
    with vpunch
    "But it's about that same time that I feel the painful sensation of something cutting into my wrists and ankles."
    scene bg bedroom1
    show kylie normal at center, zoomAt(1.5, (640, 1040))
    with dissolve
    call blue_pill from _call_blue_pill
    "Turning my head this way and that, my worst fears are confirmed - I'm tied down on my own bed!"
    "My arms are lashed to either side of the headboard, and my legs bound together at the foot of the bed."
    "And where I was only wearing a T-shirt and shorts beforehand, now I'm completely naked."
    mike.say "Fuck...fuck...fuck..."
    mike.say "You've zapped me with a Taser, tied me up and now you're drugging me!"
    mike.say "Kylie, you are one screwed-up bitch!"
    show kylie sadhappy
    "Kylie chuckles and wags a finger in my face, as if scolding me for my insolence."
    kylie.say "Now, now - is that any way to talk to the soon-to-be mother of your child?"
    "Now it's my turn to laugh, a desperate sound that's astonished at what she's just suggested."
    mike.say "What...you...you still think I'm going to have sex with you?"
    mike.say "I'm so scared right now, my cock's about to shrink back inside me."
    mike.say "And never come out again, not as long as I live!"
    "At this, Kylie's gaze travels slowly down towards my groin, and I feel my eyes compelled to follow."
    "She nods her head towards my cock, which is already starting to twitch into life, and raises her eyebrows in mock surprise."
    show kylie blush
    kylie.say "Well, what do we have here?"
    kylie.say "Looks like your manhood disagrees with you, [hero.name]!"
    "My eyes widen as I see that she's right, my cock is stiffening more with each second."
    mike.say "Shit!"
    mike.say "What did you shove down my throat, you mad cow?"
    show kylie happy
    kylie.say "Just a magic little blue pill, that's all!"
    show kylie blush
    kylie.say "Now, shall we get started?"
    "This is rape."
    "She's actually going to rape me!"
    call injured from _call_injured_7
    menu:
        "Scream for help" if (bree.love >= 150 and not bree.hidden) and (sasha.love >= 150 and not sasha.hidden):
            "It's about now that I realise I've been trying to talk to Kylie, to reason with her for too long."
            "Forget any kind of macho crap about dealing with this myself - I need help, and fast!"
            mike.say "HELP...HELP ME...FOR THE LOVE OF GOD, HELP ME!"
            mike.say "HELP Mmmmmh..."
            show kylie angry
            "Kylie suddenly clamps both of her hands down over my mouth, silencing my cries for help."
            show kylie vangry
            kylie.say "[hero.name], what are you even thinking?!?"
            kylie.say "This is a beautiful moment, just for the two of us."
            kylie.say "We're going to make a new life together, and then be a family!"
            kylie.say "We're going to live happily ever after, just like I always dreamed it'd be..."
            show kylie angry
            "At first, Kylie's words sound like the ravings of a madwoman."
            "But as she holds my mouth shut, she's also covering my nose, and I can feel myself begin to suffocate."
            "And this makes her words begin to lose all meaning as well."
            "Just when I think it's all over and I'm about to pass out for the final time, Kylie releases me without warning."
            "As I cough and gasp for breath, I hardly notice the sound that's distracted her and in the same moment saved me too."
        "Scream for help" if not (bree.love >= 150 and sasha.love >= 150) and sasha.love < bree.love and not bree.hidden:
            hide kylie
            show bree sleep surprised
            bree.say "Whoa - what in the fuck have I walked in on?!?"
            "There's [bree.name], standing in the doorway of my bedroom."
            "Dressed in her pink pyjamas and brandishing a pillow, she doesn't look all that threatening."
            "But in my current predicament, she's a welcome sight all the same."
            "For a moment, I feel hope rising in my gut, as Kylie looks stunned at being disturbed in the act."
            "And yet as I wait for [bree.name] to come rushing to my aid, she looks almost rooted to the spot in horror."
            mike.say "[bree.name], what are you waiting for?!?"
            mike.say "Help me!"
            "While [bree.name] struggles to recover from her state of shock, Kylie shows no such problems herself."
            "Almost before [bree.name] can manage to move an inch, the crazy bitch is off the bed and on her."
            hide bree
            show kylie murder bree
            play sound knife
            pause 0.2
            with vpunch
            "I see something flash in her hand, and then hear a shocked scream from [bree.name]."
            "The sound takes only a couple of seconds to turn into a terrible, choking gurgle."
            "And then I see [bree.name] collapse to the floor, her throat opened in a gaping red gash."
            play sound body_fall
            hide kylie
            show kylie a knife bloodyknife bloodyface yandere at right5
            with fade
            "Kylie turns around slowly, wiping away [bree.name]'s blood from where it's spurted across her face."
            kylie.say "Sorry you had to see that, [hero.name]."
            kylie.say "But I'm afraid that's what's going to happen from now on."
            kylie.say "That's what's in store for anyone that tries to come between us!"
            "She smiles at me, but her eyes are filled with a madness, the sight of which terrifies me."
            "I gape at her, unable to wrap my head around the terrible deed she's just committed in front of me."
            kylie.say "That's right, [hero.name]."
            kylie.say "You just lie back and let me do all the work..."
            hide kylie
            show kylie cowgirl bloodbath vaginal
            "With that, she walks back over to the bed and begins to lower herself down and onto me."
            "A quick glance at her hand shows me that Kylie's still holding the bloody knife."
            show kylie cowgirl orgasm
            "But when I look up and see the expression on her face, it almost holds me spellbound."
            "Kylie has her eyes closed and her lips slightly parted as she starts to guide my cock inside of her."
            "Sure, I've seen girls looking like they're enjoying themselves during sex before now."
            "But somehow this looks like so much more than that."
            show kylie cowgirl pleasure
            "Kylie actually looks as though she's realising a cherished aspiration or dream - and right on top of me!"
            "She sinks slowly downwards, until she can go no further."
            "And then she simply remains still, as if she wants to preserve the moment for as long as possible."
            "When she finally does start to move again, she begins slowly, riding me gently."
            show kylie cowgirl orgasm
            "But her pace soon quickens, and I can feel my own heartbeat quickening to keep pace."
            "Before too long, I feel as though Kylie is pushing me to go as fast as I can."
            "Gone is the almost saintly look that surrounded her at the beginning."
            show kylie cowgirl ahegao
            "And in its place is an ever more lustful and demanding succubus, trying to drain my very soul to satisfy her desires."
            "Kylie tosses her head from side to side, starting to sigh and moan as her passion builds to a climax."
            "Her hair whips this way and that, alternatively brushing and then lashing at my face."
            "I can feel her nails as she drags them down my chest, and smell the coppery tang of my own blood."
            mike.say "Oh shit..."
            mike.say "Kylie...I'm going to..."
            kylie.say "Oh, [hero.name]!"
            kylie.say "Do it...fill me up inside!"
            kylie.say "DO IT!"
            show kylie cowgirl creampie
            $ kylie.impregnate(True)
            $ kylie.flags.rape = True
            $ kylie.sexperience += 1
            "I let myself go, doing exactly what she wants."
            "As soon as she's satisfied that I'm done, Kylie climbs off of me and wipes the bloody blade of the knife on the pillow by my head."
            "I don't know if I should curse or scream for mercy."
            hide kylie
            "But Kylie's already walking towards the open door, leaving me still tied to the bed."
            "She steps over [bree.name], blowing me a kiss and giving me a wave as she does so."
            "And then I'm left alone, helpless and mere feet away from the dead body of my murdered girlfriend."
            $ kylie.flags.killed = "bree"
            $ bree.set_gone_forever()
            $ Room.find("bedroom2").hide()
            return
        "Scream for help" if not (bree.love >= 150 and sasha.love >= 150) and sasha.love >= bree.love and not sasha.hidden:
            hide kylie
            show sasha bass attack
            sasha.say "Get away from him, you crazy bitch!"
            "My head snaps up to see Sasha, standing in the doorway of my bedroom."
            "She might be wearing nothing more than her pyjamas right now."
            "But she's also wielding her guitar in two hands and looks like she's come to fight!"
            "Kylie stares at the new arrival, surprise and shock freezing her in place."
            mike.say "Be careful, Sasha!"
            mike.say "She's totally fucking insane!"
            sasha.say "Yeah, well - I'm pretty mad myself right now!"
            "Sasha steps forward, taking a swing at Kylie."
            "But while she was frozen a moment before, the sudden attack seems to shake her out of it."
            "The guitar blow comes within mere inches of connecting with the side of Kylie's head."
            hide sasha
            show kylie murder sasha
            play sound knife
            pause 0.2
            with vpunch
            "And yet before she can recover and try for a second swing, I see Sasha stagger, her hand going to her throat."
            "It's only then that I notice the blade in Kylie's hand, stained red and dripping with blood."
            mike.say "SASHA!"
            mike.say "NO!"
            "Clutching at her throat in a futile attempt to stem the bleeding, Sasha drops her guitar and then collapses to the floor."
            play sound body_fall
            hide kylie
            show kylie a knife bloodyknife bloodyface yandere at right5
            with fade
            "Kylie turns around slowly, wiping away Sasha's blood from where it's spurted across her face."
            kylie.say "Sorry you had to see that, [hero.name]."
            kylie.say "But I'm afraid that's what's going to happen from now on."
            kylie.say "That's what's in store for anyone that tries to come between us!"
            "She smiles at me, but her eyes are filled with a madness, the sight of which terrifies me."
            "I gape at her, unable to wrap my head around the terrible deed she's just committed in front of me."
            kylie.say "That's right, [hero.name]."
            kylie.say "You just lie back and let me do all the work..."
            hide kylie
            show kylie cowgirl bloodbath vaginal
            "With that, she walks back over to the bed and begins to lower herself down and onto me."
            "A quick glance at her hand shows me that Kylie's still holding the bloody knife."
            show kylie cowgirl orgasm
            "But when I look up and see the expression on her face, it almost holds me spellbound."
            "Kylie has her eyes closed and her lips slightly parted as she starts to guide my cock inside of her."
            "Sure, I've seen girls looking like they're enjoying themselves during sex before now."
            "But somehow this looks like so much more than that."
            show kylie cowgirl pleasure
            "Kylie actually looks as though she's realising a cherished aspiration or dream - and right on top of me!"
            "She sinks slowly downwards, until she can go no further."
            "And then she simply remains still, as if she wants to preserve the moment for as long as possible."
            "When she finally does start to move again, she begins slowly, riding me gently."
            show kylie cowgirl orgasm
            "But her pace soon quickens, and I can feel my own heartbeat quickening to keep pace."
            "Before too long, I feel as though Kylie is pushing me to go as fast as I can."
            "Gone is the almost saintly look that surrounded her at the beginning."
            "And in its place is an ever more lustful and demanding succubus, trying to drain my very soul to satisfy her desires."
            show kylie cowgirl ahegao
            "Kylie tosses her head from side to side, starting to sigh and moan as her passion builds to a climax."
            "Her hair whips this way and that, alternatively brushing and then lashing at my face."
            "I can feel her nails as she drags them down my chest, and smell the coppery tang of my own blood."
            mike.say "Oh shit..."
            mike.say "Kylie...I'm going to..."
            kylie.say "Oh, [hero.name]!"
            kylie.say "Do it...fill me up inside!"
            kylie.say "DO IT!"
            show kylie cowgirl creampie
            $ kylie.impregnate(True)
            $ kylie.flags.rape = True
            $ kylie.sexperience += 1
            "I let myself go, doing exactly what she wants."
            "As soon as she's satisfied that I'm done, Kylie climbs."
            hide kylie
            "But Kylie's already walking towards the open door, leaving me still tied to the bed."
            "She steps over Sasha, blowing me a kiss and giving me a wave as she does so."
            "And then I'm left alone, helpless and mere feet away from the dead body of my murdered girlfriend."
            $ kylie.flags.killed = "sasha"
            $ sasha.set_gone_forever()
            $ Room.find("bedroom3").hide()
            return
        "Stay silent":
            "Call me crazy if you like - but is what's happening here REALLY such a bad thing?"
            "Sure, it's all a bit extreme and there's kind of been no real consent on my part."
            "But then isn't that kind of the vibe that Kylie gives out?"
            "She's more than a little crazy, and she does things that are crazy and spontaneous too."
            "Maybe this is just her idea of a serious bondage session?"
            "And if that's so, then there's nothing wrong with just sitting back and enjoying it, right?"
            kylie.say "That's right, [hero.name]."
            kylie.say "You just lie back and let me do all the work..."
            hide kylie
            show kylie cowgirl vaginal
            "With that, she begins to lower herself down and onto me."
            "Her skirt soon conceals my painfully erect cock, but I can feel every movement she makes."
            show kylie cowgirl orgasm
            "And when I look up and see the expression on her face, it almost holds me spellbound."
            "Kylie has her eyes closed and her lips slightly parted as she starts to guide my cock inside of her."
            "Sure, I've seen girls looking like they're enjoying themselves during sex before now."
            "But somehow this looks like so much more than that."
            show kylie cowgirl pleasure
            "Kylie actually looks as though she's realising a cherished aspiration or dream - and right on top of me!"
            "She sinks slowly downwards, until she can go no further."
            "And then she simply remains still, as if she wants to preserve the moment for as long as possible."
            "When she finally does start to move again, she begins slowly, riding me gently."
            show kylie cowgirl orgasm
            "But her pace soon quickens, and I can feel my own heartbeat quickening to keep pace."
            "Before too long, I feel as though Kylie is pushing me to go as fast as I can."
            "Gone is the almost saintly look that surrounded her at the beginning."
            show kylie cowgirl ahegao
            "And in its place is an ever more lustful and demanding succubus, trying to drain my very soul to satisfy her desires."
            "Kylie tosses her head from side to side, starting to sigh and moan as her passion builds to a climax."
            "Her hair whips this way and that, alternatively brushing and then lashing at my face."
            "I can feel her nails as she drags them down my chest, and smell the coppery tang of my own blood."
            mike.say "Oh shit..."
            mike.say "Kylie...I'm going to..."
            kylie.say "Oh, [hero.name]!"
            kylie.say "Do it...fill me up inside!"
            kylie.say "DO IT!"
            show kylie cowgirl creampie
            $ kylie.impregnate(True)
            $ kylie.flags.rape = True
            $ kylie.sexperience += 1
            "I let myself go, doing exactly what she wants."
            "Panting for breath, I hardly notice the sound that makes Kylie turn her head towards the door, her face a picture of alarm."
    hide kylie
    show sasha bass attack
    show bree pillow attack at left
    sasha.say "Get away from him, you bitch!"
    bree.say "Yeah - what she said!"
    "Desperately twisting my body and turning my head towards the door, I see my salvation in the form of [bree.name] and Sasha."
    "They stand there, grim-faced and determined, like a pair of avenging Valkyries."
    "Well, maybe actual Valkyries wouldn't share their particular taste in pyjamas."
    "But I'm glad to see them all the same."
    "Sasha brandishes her guitar in a two-handed grip, ready to swing at a moment's notice."
    "Whereas [bree.name] stands prepared to swing with a pillow."
    "But she more than makes up for the lack of substance in choice of weapon thanks to the look of utter determination on her face."
    hide bree
    hide sasha
    if kylie.flags.rape:
        show kylie naked yandere at right5, hshake
    else:
        show kylie casual yandere at right5, hshake
    with hpunch
    "Kylie clambers off of me and down from the bed, almost hissing like an animal being held at bay."
    "She backs away, allowing [bree.name] and Sasha to step between her and the bed."
    hide kylie with moveoutright
    "But this move on their part leaves the door unguarded, and seeing her opportunity, Kylie darts through it and away."
    $ sasha.love += 10
    $ bree.love += 10
    $ sasha.sub -= 25
    $ bree.sub -= 25
    show bree sleep angry at right5
    show sasha sleep angry at left5
    "Neither of the girls even thinks of giving chase, both of them instead falling upon me, trying to free me from my bonds."
    show bree sad
    show sasha sad
    "As they set me loose and then fuss over me to check that there's no permanent damage done, I almost manage to forget what just happened."
    "Under any other circumstances, having [bree.name] and Sasha to nurse me would be a dream come true."
    "But the trauma of what I've just endured means that I can hardly appreciate what they're doing for me in that manner."
    show bree normal at center, zoomAt(1.5, (940, 1040))
    show sasha normal at center, zoomAt(1.5, (340, 1040))
    "Instead I feel shaken to the core, and deeply grateful to have two such brave and caring housemates."
    "No, not housemates - friends."
    $ game.room = "bedroom1"
    return

label kylie_stop_pill:
    $ kylie.flags.pill = False
    $ kylie.flags.unpilled = True
    return

label kylie_unRun:
    $ kylie.flags.run = False
    $ kylie.unhide()
    return

label kylie_run:
    mike.say "I could swear I saw someone here..."
    mike.say "I must be imagining things."
    $ kylie.flags.run = True
    $ kylie.flags.runDelay = TemporaryFlag(True, randint(1, 7))
    $ kylie.flags.hasRun += 1
    $ kylie.hide()
    return

label kylie_classroom_bj:
    scene bg classroom
    "The classroom's pretty quiet today, thanks to us all being given some pretty intense work to get through."
    "Almost everyone has their heads down, racking their brains as they try to come up with the right answers."
    "And that's just what I'm doing to, that is until I feel the sensation of a hand sliding into my lap."
    "It can only belong to the person sitting right next to me."
    show kylie close smile
    "So I turn my head and whisper the inevitable question."
    mike.say "Ah, Kylie..."
    mike.say "Why's your hand on my groin?"
    mike.say "Did you drop a pen or something?"
    "But the moment I look Kylie in the face, I feel myself swallowing and gasping."
    "There's not a hint of shame on her face right now, in fact there's something else there."
    "And my best guess is that it's a barely controlled feeling of lust!"
    show kylie close shout
    kylie.say "Oh no, [hero.name]."
    kylie.say "I've got my pen right here."
    show kylie close a normal
    "Kylie waves the pen at me with her free hand."
    show kylie close happy
    kylie.say "I just wanted to feel your cock in my hand, that's all!"
    show kylie close normal
    "My eyes open wide at the sheer audacity of what Kylie just said."
    "Which prompts her to give my cock a good, hard squeeze."
    "As far as I can tell just for the sake of backing up her words."
    mike.say "Mmm..."
    mike.say "Kylie..."
    mike.say "Were in the middle of class!"
    show kylie close happy
    "Kylie chuckles and shakes her head, dismissing my concerns."
    show kylie close shout
    kylie.say "Don't worry."
    kylie.say "I know all about moving silently."
    kylie.say "And everyone's all wrapped up in their work anyway."
    show kylie close normal
    mike.say "Yeah, they are."
    mike.say "Because this stuff is like super hard!"
    "Kylie's expression becomes one of mock concern at this."
    show kylie close blush
    kylie.say "Aww..."
    kylie.say "You sound stressed!"
    show kylie close happy
    kylie.say "What you need is something to calm you down..."
    show kylie close smile at center, zoomAt(1, (640, 1540)) with move
    "Kylie's still smiling as she begins to sink down in her seat."
    show kylie at center, zoomAt(1, (640, 2040)) with move
    hide kylie
    "I'm not sure how she manages to do it, but she slithers under the table."
    "And all the time she keeps on holding my eye too."
    "She only looks away when she starts to unzip my flies."
    "I can feel my heart start beating like a drum as I watch her."
    "And I know that I could say something to stop her."
    "Or else reach down and try to intervene."
    "But somehow I'm frozen in place, just watching her."
    "Ah, who am I trying to kid!"
    "I know just what Kylie's up to."
    "And the truth is I want to see if she can pull it off!"
    "After all, my cock's already hard from her squeezing it just now."
    "I might as well let her put it to good use."
    show kylie bj classroom with fade
    "I try to keep from holding my breath as Kylie opens my flies."
    "And I almost gasp aloud when she reaches inside and takes hold of my cock."
    "Normally I'd expect Kylie to tease me or engage in some kind of foreplay."
    "But as soon as she sees that I'm already getting hard, she sets to work."
    show kylie bj tongue
    show mouth_insert kylie zorder 1 at zoomAt(1, (860, 140))
    "Leaning in closer still, her lips close around the head."
    "And for a moment, it just feels like she's kissing my cock."
    "But then a look of very real hunger seems to come over her face."
    show kylie bj blow -tongue
    "At the same time I feel Kylie begin to make use of her teeth too!"
    "I wince instinctively, thinking that she's going to bite down."
    "But then I realise that she's just using it to add some spice to the experience."
    "And that allows me to sit back in my chair and just enjoy what follows."
    "Kylie's settling into a really pleasing rhythm under the table."
    "So much so that it's all I can do to keep from sighing with pleasure."
    "The way she's using her lips, tongue and teeth really is something."
    "I'm just letting a smile creep over my face."
    "And I'm leaning back happily in my chair when it hits me."
    "People are starting to look up from their work."
    "They're starting to look straight at me too!"
    "Of course they are."
    "We're supposed to be in the middle of a challenging task."
    "And I'm reclining in my seat like the king of the world!"
    "I hastily lean forwards, trying to look like I'm working too."
    "Which is a damn good thing."
    show kylie bj pleasure
    "Because that's the exact moment Kylie chooses to kick things up a gear."
    "I can feel that she's taking me deeper than ever before."
    "Really working the shaft of my cock for all she's worth."
    "At this rate, I won't be able to hold on for much longer!"
    menu:
        "Cum on her face":
            show kylie bj normal
            "I pull back in my seat as far as I dare."
            "And Kylie seems to get the message straight away."
            show kylie bj out
            hide mouth_insert
            "She lets my cock slide out of her mouth."
            show kylie bj tongue
            "Then she sits there patiently, just waiting for it to happen."
            show kylie bj cumshot dickcum cum onface with vpunch
            "A moment later I lose it, spattering Kylie's face with cum."
            show kylie bj -cumshot
        "Cum in her mouth":
            show kylie bj normal
            "I leave my cock right where it is until the last moment."
            "Kylie seems to get the message, and I feel her preparing herself."
            show kylie bj pleasure cumshot
            show mouth_insert kylie cum
            "So when I shoot my load into her mouth, she handles it like a pro."
            with vpunch
            "Kylie swallows every last drop, not pausing once."
            show kylie bj out normal tongue dickcum -cumshot
            "Even sucking like a desperate fish once it's over."
            hide mouth_insert
    "I keep right on pretending to work while Kylie tidies up under the table."
    "I can feel her licking around my cock, lapping up every last drop of cum."
    hide kylie
    show kylie close at center, zoomAt(1, (640, 1540))
    with fade
    "Only then does she push my cock back into my pants and zip up my flies."
    show kylie smile at center, zoomAt(1, (640, 1355)) with ease
    "Then she emerges from under the desk and climbs into her seat as quietly as she left it."
    "After that, we keep quiet and make sure our heads are down until the end of the period."
    return

label kylie_preg_talk:
    $ kylie.flags.toldpreg = True
    if not kylie.flags.rape:
        show kylie a happy at center, zoomAt(2, (640, 1380))
        kylie.say "[hero.name], hi!"
        show kylie a smile
        "At the sound of her voice behind me and close enough to almost whisper in my ear, I can't help jumping almost out of my skin."
        with vpunch
        mike.say "SHIT!"
        show kylie a normal at center, zoomAt(1.5, (640, 1040)) with vpunch
        mike.say "Kylie - why do you have to sneak up on me like that?!?"
        mike.say "Are you trying to give me a heart attack or what?"
        show kylie impressed
        "But from the wide-eyed expression on her face and the sheer width of her smile, I can instantly tell that Kylie's in one of those moods where she's off with the fairies."
        "I know that I shouldn't think things like this about the girl that I'm currently dating, but it always feels like there's a little bit of the crazy about her at times like this."
        "Of course, I mean the cute, kooky kind of crazy."
        "Not the straight-jackets and padded rooms kind of crazy..."
        "Anyway, I soon remember that it was Kylie that wanted this meeting and that she had an announcement to make."
        mike.say "Erm...you said that you wanted to see me, Kylie?"
        mike.say "That you had something you needed to tell me to my face?"
        show kylie smile
        "I didn't think that it was possible, but all the same I see Kylie's smile become even wider than before."
        show kylie happy
        kylie.say "Of course, [hero.name]."
        show kylie shout
        kylie.say "And trust me, you're gonna be so glad that I did!"
        show kylie normal
        "I nod at Kylie, trying to encourage her to hurry up and spit it out - whatever IT is."
        show kylie shout
        kylie.say "Oh, [hero.name] - I'm pregnant!"
        show kylie normal
        "I might have had no clue as to just what Kylie was about to say, but I still didn't expect it to be that!"
        mike.say "You're what?!?"
        show kylie shout
        kylie.say "I'm pregnant..."
        show kylie impressed
        "She cocks her head on one side and begins to look at me in a puzzled manner, as if this was not the reaction she had been expecting."
        show kylie talkative
        kylie.say "What's the matter, [hero.name]?"
        kylie.say "Aren't you happy to hear that you're going to be a father?"
        kylie.say "Doesn't it make you go all gooey inside just thinking about how this means we can raise them together?"
        kylie.say "How we can get married and settle down, be a proper family?"
        show kylie shout
        kylie.say "Don't you see?"
        show kylie happy at center, zoomAt(2, (640, 1380))
        kylie.say "It's like fate intervened and gave us a reason that we HAVE to stay together...forever!"
        show kylie smile
        "The whole time that she's been telling me this, Kylie's also been leaning ever closer."
        "So by the time she says the word 'forever', she's practically close enough for the tips of our noses to touch."
        show kylie impressed
        "While her eyes just seemed to be wide with enthusiasm before, they now look like there's an intense fire in them."
        "It's almost...well...if I'm honest, it's almost enough to scare me."
        menu:
            "I'll take responsibility":
                "But then I finally manage to give myself a metaphorical shake, realising just how stupid and paranoid I'm being right now."
                "It's pretty obvious that I've been letting my natural fear of commitment colour everything Kylie's said to me."
                "Of course she's going to be crazy - crazily elated at the prospect of having a baby with the man that she loves."
                "And the last thing that she needs at a time like this is to have that same guy acting like a childish, irresponsible jerk!"
                mike.say "I'm sorry, Kylie - you're right...of course you're right."
                mike.say "I am happy, but the news just stunned me for a second, that's all."
                hide kylie
                show kylie kiss casual
                with fade
                $ kylie.flags.kiss += 1
                "At this, Kylie shows her delight by leaning in and kissing me, full on the lips."
                "She even goes as far as to slip her tongue in and press her voluptuous body against me as she does so."
                "And I have to admit, at this point I just melt, feeling all of my former misgivings draining away."
                "All I can think about is the image of Kylie with her belly swelling as our child grows inside of her."
                "I can't believe that I've let myself become so paranoid as to be able mistake her genuine love for something more sinister!"
                "And that's certainly a mistake that I won't be making again."
                hide kylie
                show kylie smile at center, zoomAt(1.5, (640, 1040))
                "When she finally breaks away from the kiss, I see that Kylie has the most gorgeous smile on her face."
                "I honestly don't think that I've ever seen her looking more beautiful and radiant than she does right now."
                show kylie happy
                $ kylie.love += 10
                kylie.say "Oh, [hero.name] - I always knew that this would happen to me one day."
                show kylie shout
                kylie.say "I always knew that if I waited long enough, I'd have you and we could settle down together."
                kylie.say "And now that my dreams have all come true, I'm NEVER going to let you go again!"
            "I don't want anything to do with it":
                "Fuck sake - I can't be a father, not at this stage in my life, and certainly not without some kind of warning either!"
                "Don't get me wrong, for all of her quirks and odd habits, I adore Kylie."
                "She's fun to be around, and she turns me on like crazy."
                "But as much as I'm not ready to have a kid, I've never thought of her as the family type either."
                mike.say "You...you sound like you've already decided to keep the baby, Kylie."
                show kylie y surprised
                "Suddenly she looks at me with horror evident in her eyes, clutching at her belly with both hands."
                kylie.say "Oh, [hero.name]...I could never, ever even imagine murdering our child!"
                kylie.say "Please don't tell me you think I'd be capable of that!"
                kylie.say "This baby is a symbol of the fact that we were always meant to be together..."
                show kylie y sad
                mike.say "No, Kylie...you don't understand."
                mike.say "I was trying to say that I can't be a parent right now."
                mike.say "I respect your decision to keep the baby."
                mike.say "But, I'm sorry - I can't be a part of the kid's life, not like you'd want me to..."
                $ kylie.love -= 20
                $ kylie.yandere += 25
                "Kylie goes quiet for a moment, simply staring at me."
                "I get the impression that she's processing my words, sifting them for meaning."
                "Her eyes seem to glaze over for a couple of seconds, like she's zoned out while thinking about what to do next."
                show kylie b happy
                kylie.say "Don't worry, [hero.name] - I understand completely."
                show kylie b normal
                "Surprised to hear her speak so quickly, it takes me a few seconds to realise what Kylie actually just said."
                mike.say "Wait...what...you do?!?"
                show kylie b smile
                "She smiles at me, sweetly and with infinite indulgence."
                show kylie b shout
                kylie.say "Sure I do - I've gone and sprung all of this on you, and you just need some time to make sense of it all."
                kylie.say "So you do that, and the baby and I will be waiting for you as soon as you're ready."
                show kylie b normal
                mike.say "No, Kylie...that's not it - you're twisting my words..."
                show kylie a normal
                "Before I can say any more, Kylie puts a finger to my lips and stops me in my tracks."
                show kylie a shout
                kylie.say "Shhh...it's okay."
                kylie.say "There's no need to say another word!"
                show kylie a normal
                "And with that, she turns and walks away from me, still holding up her finger to keep me silent."
                "Which isn't really that much of a problem, as I'm pretty much lost for words anyway."
            "You should get an abortion":
                "For a moment, I'm genuinely stunned by the both the revelation of Kylie being pregnant and her almost psychotic glee at the situation."
                "Sure, messing around with her was fun, kind of like riding a roller-coaster that terrified and elated me in equal measures."
                "And it's not like I've been using her as a fuck-buddy either - I have a very real affection for Kylie, honestly I do."
                "But I've already pretty much made up my mind that she's not long-term relationship material, let alone a potential wife and mother to my children."
                "I know that I'm not ready to have kids, and that I'd want to be able to plan that kind of thing out once I'm sure that I am."
                "And then there's the obvious matter of Kylie's mental health, which I think it's pretty clear just isn't up to the challenge of raising a child."
                "I can't put this off any longer, not when there's the potential of a new and innocent life being harmed as well."
                mike.say "Kylie, I think we both know that keeping the baby would be the wrong decision to make."
                "The elation and manic happiness drains from Kylie's face in mere seconds as she listens to my words."
                show kylie y surprised
                "In its place, I can see a look of confusion that's quickly turning into a dark and even worrying expression of anger."
                kylie.say "What did you just say to me, [hero.name]?"
                kylie.say "Please, tell me that I just misheard you - tell me that you didn't say what I thought you just said!"
                show kylie angry
                "I can hear myself swallowing and coughing in actual fear, my Adam's apple bobbing up and down like a ballcock."
                "But I try as best I can to hold my nerve and press on, confident that Kylie will back down if I just stand up to her."
                mike.say "You heard me well enough, Kylie."
                mike.say "Neither of us is capable of raising a child right now, we're both of us too young and selfish."
                mike.say "I think that the only answer is for you to have a termination, before it's too late..."
                show kylie sad
                "The anger in Kylie's eyes is momentarily replaced with disbelief, as though she truly can't understand why I'm saying these things to her."
                "But all too soon the same anger returns and she looks at me as though she actually wants to kill me."
                show kylie vangry
                $ kylie.love -= 20
                $ kylie.yandere += 50
                kylie.say "How can you say that, [hero.name]?"
                kylie.say "How can you even think it?!?"
                kylie.say "We were always destined to be together, to love each other - and our baby's supposed to be living proof of that!"
                kylie.say "Why, [hero.name] - why don't you want our baby?"
                kylie.say "Why don't you love me like you're supposed to?!?"
                show kylie angry
                mike.say "Kylie, please - you're upset and emotional, maybe from the hormones."
                mike.say "I do love you, really I do..."
                "I don't want to say it, and I wish I could keep from doing so with every fibre of my being."
                "But I can't...I just can't."
                mike.say "You don't need a baby, Kylie - you need help."
                mike.say "From me, from a doctor, from..."
                "Before I can finish the sentence, I see the barest hint of something catching the light in Kylie's clenched fist."
                "And then she slashes it in an upwards arc, before I even have a chance to react."
                show kylie a casual yandere knife
                play sound knife
                pause 0.2
                with vpunch
                if renpy.has_label("kylie_achievement_8") and not game.flags.cheat and game.week_day == 5 and game.day == 13:
                    call kylie_achievement_8 from _call_kylie_achievement_8
                "The blade of the box-cutter is razor-sharp, slicing my throat open before I can feel it doing so."
                "I don't have any sensation of the blood that's now gushing from the gaping wound she's made."
                "All I can hear is the sound of my own ragged breath, as the air in my lungs escapes through the wound instead of my mouth."
                hide kylie
                show kylie a casual yandere knife
                play sound body_fall
                pause 0.3
                with vpunch
                scene expression "bg {}".format(game.room) at blood
                show kylie a casual yandere knife at center, blood
                with dissolve
                "Kylie keeps on talking as I fall onto my knees and then onto all fours at her feet."
                "I can't make sense of it all, but there's something about me being a monster and a murderer."
                "Something else about how she'll always have the baby, and it'll be someone that loves her and appreciates her like she deserves to be."
                scene expression "bg {}".format(game.room) at blur(8), blood
                show kylie a casual yandere knife at center, blur(8), blood
                with dissolve
                "The last thing I can make out is now she'll never let the kid go and how they'll stay with her forever."
                "But by now the sound of her voice has faded into an indistinct sound that has no meaning to me."
                "And as I finally bleed out and pass into the darkness, I have no idea whether I'm alone or not at the very last."
                scene bg black with dissolve
                pause 1.0
                $ renpy.full_restart()
    else:
        "What happened to me in my own bedroom - what Kylie did to me that night..."
        "It's been a couple of days since it actually happened."
        "But whenever I close my eyes, it feels like it's still going on."
        "I see flashes of what she inflicted on me, the things she did."
        "And every time I could be right back there, tied to the bed and completely helpless."
        "I had hoped that, with time, it might get better - that the memories might fade."
        "But so far it only seems to be getting worse, the flashbacks more intense."
        "Sometimes it's the only thing that I can think about at all!"
        "I find myself looking over my shoulder the whole time."
        "And I won't walk into a room without first switching on the light."
        "Even then I feel the need to check the shadows and any potential hiding places."
        "But it doesn't seem to do me any good."
        show kylie a happy at center, zoomAt(1.5, (640, 1040)) with hpunch
        kylie.say "HEY!"
        show kylie a smile
        "Kylie seems to appear out of thin air."
        "One moment she's nowhere to be seen."
        "And the next she's right there, in my face and leaning ever closer."
        hide kylie
        show kylie a smile
        "I can't help leaping backwards and cowering in genuine terror."
        mike.say "Oh shit, oh shit, oh shit..."
        mike.say "Please don't hurt me again!"
        show kylie stuned
        "Kylie looks really puzzled for a moment, as if she's baffled by my fear."
        "And for a few seconds, I genuinely think I can see reality dawning on her."
        show kylie smile
        "But the she shakes her head and the same manic expression appears on Kylie's face."
        show kylie sadhappy
        kylie.say "Oh, [hero.name]."
        kylie.say "You're so funny!"
        kylie.say "I could never hurt the man I love."
        kylie.say "Everything I do for you, I do it BECAUSE I love you!"
        show kylie smile
        "Kylie smiles at me as she says this."
        "And her eyes betray no hint of insincerity the whole time."
        "She genuinely seems to believe what she's saying is the truth."
        "Which means that she's completely and utterly insane!"
        mike.say "Wha...what do you want, Kylie?"
        show kylie stuned
        "Again, Kylie greets my question with a puzzled expression."
        show kylie sadhappy
        kylie.say "Well, I could have called you or sent a text."
        kylie.say "But this kind of good news should be given in person!"
        show kylie normal
        "What on earth is she talking about?"
        "Is it too much to hope that she's come to her senses and realised she's crazy?"
        "That she's going to hand herself in to the police and confess everything?"
        mike.say "Good news?"
        show kylie happy
        kylie.say "Yes, silly."
        kylie.say "The good news is that you're a real stud!"
        show kylie normal
        mike.say "Oh god..."
        mike.say "You don't mean..."
        "Kylie nods happily, anticipating what I'm thinking."
        "She has her hands clasped behind her back and she's rocking back and forth on her heels."
        "She looks for all the world like any perfectly sane girl delivering wonderful news to her boyfriend."
        show kylie shout
        kylie.say "Yes I do."
        kylie.say "Our union was blessed."
        show fx heart
        show kylie happy
        kylie.say "I'm pregnant!"
        show kylie smile
        if not kylie.flags.killed:
            "I feel like my eyes are going to pop out of my head."
            "My brain just can't seem to process what Kylie just told me."
            "But I know that I have to say something."
            "Even if it's just for the sake of keeping her from getting violent!"
            menu:
                "Say that you are happy for her":
                    "What choice do I really have but to put a smile on my face?"
                    "I know full well what Kylie's capable of when pushed to the limit."
                    "And it's not just me that she could hurt now."
                    "Whether I like it or not, there's another life involved."
                    mike.say "R...really, Kylie?"
                    mike.say "Th...that is good news!"
                    "As I suspected, Kylie seems not to notice the nerves in my voice."
                    "Either that or she just chooses to ignore it as she's getting what she wants."
                    show kylie crazyhappy
                    "Her smile grows broader still as she sees her twisted vision of the future within her grasp."
                    $ kylie.love += 10
                    $ kylie.yandere -= 10
                    show kylie shout
                    kylie.say "Of course it is, [hero.name]!"
                    kylie.say "It's like I told you before - this is the way it's meant to be."
                    kylie.say "You, me and the baby, a perfect little family!"
                    show kylie normal
                    "The thought of it sends chills down my spine."
                    "But maybe this is the only way?"
                    "Kindness might win through with Kylie where honesty has failed in the past."
                    "So I just keep on smiling as she grabs my hand and presses it against her belly."
                    "I mean, there will have to be doctors and other people like that involved along the way."
                    "And one of them is bound to see the true nature of Kylie's issues, right?"
                    "Perhaps this way she can get the help she so desperately needs."
                    "And get that help without anyone being hurt along the way..."
                "Say she disgusts you":
                    "I'm still scared of Kylie, to the point of pissing my pants."
                    "But I can't go on like this for the rest of my life."
                    "And it's that much more serious now, if what she says is true."
                    "There's another life, an innocent involved in this awful mess."
                    mike.say "Kylie, please - I'm begging you now."
                    mike.say "This has got to stop!"
                    show kylie smile
                    "The smile is still fixed upon Kylie's face as she ignores me again."
                    "I can already see the same routine of denial beginning as she shakes her head."
                    mike.say "I mean it, Kylie!"
                    mike.say "You're sick - sick in the head."
                    mike.say "And you need help before you really hurt someone."
                    show kylie normal
                    "Finally I can see a change in Kylie's expression, her smile beginning to fade."
                    "I almost breathe a sigh of relief, as I know that I'm reaching her for real."
                    show kylie whining
                    $ kylie.love -= 25
                    $ kylie.yandere += 25
                    kylie.say "Y...you don't mean that, [hero.name]."
                    kylie.say "You're reeling from my good news - that's all!"
                    show kylie sad
                    mike.say "Stop it, Kylie!"
                    mike.say "Face reality for once."
                    mike.say "You broke into my house and assaulted me."
                    mike.say "You raped me, damn it!"
                    mike.say "And if you won't admit to it..."
                    mike.say "Well, then maybe it's time I did something about it myself!"
                    hide kylie with dissolve
                    "With that, I turn and storm away from Kylie."
                    "And all the time I'm hoping that she takes my shaking for sheer rage."
                    "Rather that than the genuine fear that it really is."
        else:
            "For a moment, I almost forget the fact that Kylie's a killer."
            "The revelation that she's pregnant hits me like a slap in the face."
            "I know that I have to say something, answer her in some way."
            "But this whole situation just got that much more complicated and scary!"
            menu:
                "Say you are happy for her":
                    "Do I really have a choice other than to force a smile onto my face?"
                    "I'm standing in front of a genuine rapist and murderer."
                    "And she's now not only a threat to me and everyone I know."
                    "She has another potential victim already growing inside of her!"
                    mike.say "Y...you really mean that, Kylie?"
                    mike.say "You're right - this changes everything!"
                    "If she hears the shaking in my voice, then Kylie chooses to ignore it."
                    "Or maybe she's just blinded by my say what she wants so desperately to hear."
                    "Whatever the reason, she grins even wider than before."
                    $ kylie.love += 10
                    $ kylie.yandere -= 10
                    show kylie shout
                    kylie.say "Of course it does, [hero.name]!"
                    kylie.say "This was all meant to be, remember?"
                    kylie.say "I love you and you love me - forever!"
                    show kylie normal
                    "The finality of what Kylie says is chilling."
                    "But is there any other way?"
                    "I know she's capable of the most heinous acts if it gets her what she wants."
                    "So I smile as I let her take my hand and put it on her belly."
                    "If she's going to have the baby, then she'll need to see doctors and nurses."
                    "We'll be in and out of hospitals and clinics the whole time."
                    "Maybe if I drop a subtle hint here and there..."
                    "Then Kylie might end up getting the help she really needs."
                "Say she disgust you":
                    "I can feel myself literally shaking as I stand there in front of Kylie."
                    "But I just can't let this thing go on for much longer."
                    "She's already killed one person in front of me."
                    "And there's no way a psycho like that can be trusted with a kid!"
                    mike.say "Okay, Kylie - that's it."
                    mike.say "It's time to admit that you have a problem!"
                    "My words seem to have little or no effect."
                    "The smile remains fixed on Kylie's face as she shakes her head."
                    mike.say "For fuck's sake, Kylie - I mean it!"
                    mike.say "You're not normal, you're some kind of murdering freak!"
                    mike.say "You killed someone - murdered them in front of me!"
                    show kylie normal
                    "I watch as Kylie's smile finally begins to fade."
                    "I'd be relieved, if it weren't for the darkness in her eyes."
                    show kylie vangry
                    $ kylie.love -= 25
                    $ kylie.yandere += 25
                    kylie.say "I HAD to do that, [hero.name]."
                    kylie.say "I told you - she was trying to come between us."
                    show kylie angry
                    mike.say "No, Kylie, she wasn't."
                    mike.say "She was trying to save me - save me from you!"
                    mike.say "You broke in and raped me, damn it!"
                    mike.say "Raped me and killed my housemate!"
                    mike.say "And I won't let you get away with it."
                    mike.say "I think it's time I told the authorities about you."
                    hide kylie
                    "I turn on my heel and storm away from Kylie before she can respond."
                    "I hope too that she takes my shaking for sheer rage."
                    "Because it's actually from the genuine fear I'm feeling right now!"
    return

label kylie_cookies:
    if kylie.room == game.room:
        $ kylie.love += 2
        $ kylie.sub += 2
        if kylie.yandere >= 5:
            $ kylie.yandere -= 5
        $ kylie.flags.atecookies = True
    return

label kylie_start:
    if kylie.love.max < 40:
        $ kylie.love.max = 40
    $ kylie.love += 30
    $ hero.smartphone_contacts.append("kylie")
    $ kylie.unhide()
    return

label kylie_event_11b:
    "I don't know what I'm going to say to Kylie when I finally find her."
    "And I don't know what she might try to do to me when we're face-to-face."
    "But I do know that this has gone too far - WAY too far!"
    "I thought about calling the police after what she did in front of the house."
    "And maybe [bree.name] and Sasha have already done that in spite of me."
    "But I just can't shake off the notion that I have to confront Kylie myself."
    "That if I can just talk to her one last time, maybe I can get through to her."
    "So I start hitting her favourite spots around town."
    scene bg university with fade
    pause 1
    scene bg gym with fade
    "I'm looking for her, or at least any sign that she's been there recently."
    scene bg coffeeshop with fade
    pause 1
    scene bg park with fade
    "But I must be pretty distracted while I'm looking."
    "Because it's Kylie that manages to find me first!"
    show kylie close casual happy
    kylie.say "Hello, [hero.name]!"
    show kylie close casual normal
    mike.say "Kylie?!?"
    mike.say "What the hell..."
    "Before I can finish speaking, Kylie leaps into action."
    "I hardly have a chance to see the taser that she has in her hand."
    "But I sure as hell feel it when she jabs it into my stomach."
    hide kylie
    show kylie taser
    play sound taser
    pause 0.2
    with hpunch
    "A second later it goes off, sending it's charge shooting into me."
    "My muscles tense and my entire body goes rigid as I fall to the ground."
    "And the last thing I see before I pass out is Kylie standing over me."
    "She's talking, but I can't hear a word she's saying."
    scene bg park at blur(16), dark, dark with dissolve
    "Her smile is the last thing I see before everything goes black..."
    "...and then I wake up into a new and totally baffling reality."
    scene bg church at dark, dark
    show layer master at blur(12)
    with fade
    "My head is spinning, my body aching."
    "I feel like I've been beaten up under water!"
    scene bg church at dark
    show layer master at blur(6)
    with dissolve
    "In fact, I feel like I should be laid out on my back right now."
    "But somehow I'm standing up - and I can't move!"
    mike.say "Wha..."
    show layer master at blur(0)
    with dissolve
    mike.say "What happened?"
    mike.say "Where am I?!?"
    "I cast my gaze around, despite how much it hurts me to do so."
    "My body feels stiff and bruised, like it's been through a lot of punishment."
    "Plus my head's groggy and my vision swims as I try to see where I am."
    kylie.say "Oh, you're finally awake!"
    kylie.say "You do like to keep a girl waiting, don't you!"
    "At the sound of Kylie's voice, I feel a flush of panic sweep over me."
    "It's not conscious fear, rather the result of the last thing I remember."
    "Her leaping on me, using the taser and everything going black."
    mike.say "Argh!"
    mike.say "Get the fuck away from me!"
    "Instinctively trying to back off, I find that I can't move a muscle."
    "I look down and see that I'm tied up and somehow propped up too!"
    "And what's stranger is that I'm dressed in a pretty fancy suit too!"
    "The sound of Kylie's manic laughter makes me look up again."
    show kylie wedding smile at center, dark with dissolve
    "And now I see her for the first time, gasping in amazement."
    "She's dressed as a bride, in a wedding dress and clutching a bouquet."
    scene bg church at dark
    show kylie wedding normal
    with dissolve
    "Only now do I see that we're in some kind of chapel."
    "At first I think there's a whole crowd of people in the pews."
    "But then I see that they're actually mannequins."
    "The kind of dummies that you see in shop windows!"
    "Shit - there's even one standing close by me."
    "It's dressed as a priest too!"
    mike.say "Fuck, fuck, fuck..."
    mike.say "Kylie..."
    mike.say "What have you done?"
    mike.say "What is all of this?!?"
    show kylie smile
    "Kylie answers this with another peal of manic laughter."
    "Then she shakes her head as she walks over to me."
    show kylie crazyhappy
    kylie.say "What does it look like, [hero.name]?"
    kylie.say "This is it, our big day!"
    show kylie happy
    kylie.say "We're getting married, silly!"
    show kylie normal
    mike.say "Jesus Christ, Kylie!"
    mike.say "What are you even talking about?!?"
    show kylie shout
    kylie.say "Don't worry, [hero.name]."
    kylie.say "I realised that you're not getting it yet."
    kylie.say "That you don't understand how we're supposed to be together forever."
    kylie.say "So I've taken matters into my own hands, relieved you of that responsibility."
    show kylie normal
    "I shake my head desperately."
    "There has to be a way out of this."
    mike.say "No, Kylie..."
    mike.say "You attacked me, kidnapped me!"
    mike.say "You're sick, can't you see that?"
    mike.say "You need help, and it's not too late to get it."
    mike.say "Just untie me, then I can get you the help you need - please!"
    show kylie crazyhappy
    "Kylie just laughs, dismissing my words."
    kylie.say "No, [hero.name]..."
    kylie.say "You're the one that needs help - my help."
    show kylie shout
    kylie.say "But don't worry."
    kylie.say "Once we're married, I promise to devote myself to you."
    kylie.say "Then you'll come to see the truth!"
    show kylie normal
    "Kylie throws her bouquet aside and pulls out what looks like a small remote control."
    "But I note that the taser has also appeared in her other hand too!"
    "She presses a button and then I hear music begin to play."
    "It's a wedding march, coming from a small tape-player."
    "I see the thing pinned to the chest of the mannequin dressed as a priest."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join these two people in the bonds of holy matrimony."
    "I have no idea where Kylie got the recording from or how."
    "But I'm forced to stand there, helpless as this farce plays out."
    "The voice of the priest drones on through the ceremony."
    "And all the time Kylie is there, holding the dreaded taser."
    "Priest" "Do you, Kylie..."
    "Priest" "Take this man, [hero.name]..."
    "Priest" "To be your lawful, wedded husband?"
    "I note that when the priest speaks our names, the voice changes."
    "Jarringly it becomes Kylie's own voice, showing that she's doctored the tape."
    show kylie happy
    kylie.say "I DO!"
    show kylie normal
    "Priest" "And do you, [hero.name]..."
    "Priest" "Take this woman, Kylie..."
    "Priest" "To be your lawful, wedded wife?"
    mike.say "I most certainly fucking do not!"
    show kylie crazyhappy
    "Without warning, Kylie rams the taser into my gut."
    "The initial blow is almost enough to make me puke on its own."
    show layer master at blur(12)
    play sound taser
    pause 0.2
    with hpunch
    "But then she hits the trigger, and I convulse as it shocks me."
    "I hear kylie rewinding the tape a moment later."
    "Priest" "And do you, [hero.name]..."
    show layer master at blur(6)
    "Priest" "Take this woman, Kylie..."
    "Priest" "To be your lawful, wedded wife?"
    show layer master at blur(3)
    mike.say "Urgh..."
    mike.say "Fuck..."
    show layer master at blur(20)
    play sound taser
    pause 0.2
    with hpunch
    play sound taser
    pause 0.2
    with hpunch
    "Kylie shocks me again, for longer this time."
    "And I really do puke the second time around."
    "But I can still hear the tape being rewound again."
    "Priest" "And do you, [hero.name]..."
    "Priest" "Take this woman, Kylie..."
    "Priest" "To be your lawful, wedded wife?"
    show layer master at blur(10)
    mike.say "Y...yeah..."
    mike.say "I do...I do!"
    "Priest" "Very good."
    "Priest" "Then it is my great pleasure to pronounce you man and wife!"
    show layer master at blur(5)
    "Even while I'm still gasping for breath I notice what Kylie left out."
    "When was the bit where somebody's supposed to be able to object?"
    "I guess she edited that bit out, like she changed everything else around too!"
    "Priest" "You may kiss the bride!"
    show kylie happy
    "Kylie giggles happily as she tosses the remote control aside."
    "Then she pulls out a handkerchief and cleans the puke off my face."
    show layer master at blur(2)
    show kylie close shout
    kylie.say "Look at the mess you've made of yourself!"
    show kylie happy
    kylie.say "What would you do without me to clean you up?"
    kylie.say "But don't worry about that anymore."
    show layer master at blur(0)
    show kylie shout
    kylie.say "Now you've got me to look after you - forever!"
    show kylie -close kiss
    "Kylie leans in and forces her lips against mine."
    "Her tongue pushes itself into my mouth like a writhing eel."
    "There's nothing I can do to resist her anymore."
    "I'm beaten, broken and I can feel despair taking hold of my thoughts."
    "But I have to try to hold on, to rely on my strength of Will."
    "Maybe she'll slip up and I can make a break for it?"
    scene bg church at blur(16), dark, dark with dissolve
    "I mean, this can't be the end - can it?"
    scene bg black with dissolve
    pause 5
    "I shouldn't be afraid..."
    "I shouldn't let her see my fear..."
    "I have to make a show of defiance...I have to!"
    "All of these thoughts pass through my head while I'm alone in the darkness."
    "Again and again I turn them over in my mind, trying to make myself believe them."
    "It's been so long that I've lost count of the days, and they've become a litany."
    "Without them to cling to, I really think that I'd have gone mad before now."
    "But then maybe I'm already mad."
    "And the repetition of those thoughts is the form that my madness takes."
    "If you think you're mad, doesn't that mean you can't be mad?"
    "I'm sure I remember reading that somewhere..."
    "But then the door at the top of the stairs opens."
    "The light starts to come down them, along with the footsteps."
    "And any thought of defiance vanishes in an instant."
    "Instead I scurry backwards into a corner, dragging my chains after me."
    "I don't stop until I'm pressed against the wall."
    "And even then I keep on trying to push myself into it."
    "The light hurts my eyes, but that's not why I'm cowering."
    "I'm cowering because I don't want to have to see her!"
    "But what choice to I have?"
    "None - I don't have any choices left to me!"
    "I can hear her footsteps on the cold stone floor."
    "Hear her shoes splashing through the puddles of fetid water."
    "She's talking to me, and as always, I try not to listen to what she's saying."
    "But there's no way that I can keep her voice out of my head."
    "Not when she's already in there, dominating my thoughts!"
    kylie.say "Oh, [hero.name]!"
    kylie.say "Where are you, my darling?"
    kylie.say "Won't you come out and see me?"
    scene kylie bad ending mike with dissolve
    pause 2
    "I try to keep my face pressed against the wall."
    "I try with all the willpower that I have left."
    "But already I can feel my body betraying me."
    "It's like the subconscious part of my mind, the animal part of me responds."
    "She's already broken me, mind, body and spirit, bent me to her will."
    "And I'm responding to her commands without even being aware of it."
    "On my hands and knees I crawl out of the corner and towards her."
    "I don't try to get up, I don't think I have the strength to."
    "And it's been so long since I stood on my own two feet."
    "I doubt that I could remember how to actually do it."
    kylie.say "There you are, dear!"
    kylie.say "How are you feeling today, huh?"
    kylie.say "I brought you your breakfast, like always!"
    show kylie bad ending kylie
    "She puts the bowl of watery gruel on the floor beside me."
    "It's enough to live on, but just barely so."
    "She feeds me enough to keep me alive and aware, after a fashion."
    "But never enough for me to regain my strength or focus my mind."
    kylie.say "Don't worry, dear - you don't have to say you're grateful."
    kylie.say "That's the wonderful thing about being married to you."
    kylie.say "It means I know you're eternally grateful for everything I do!"
    "She smiles and turns her back on me, walking towards the stairs."
    "I try to say something, to speak actual words of a kind."
    "But it's been so long that nothing comes out but a gasp."
    "It's quiet and so low that she doesn't even hear it."
    "Her footsteps recede across the floor and then up the stairs."
    "The door closes and takes the light with it."
    "And just like that, I'm alone in the darkness again."
    "I don't know how long it's been."
    "I don't know where I am."
    "I haven't seen my face in a mirror for so long."
    "I only remember my own name because she uses it around me."
    "Is this what she meant when she said that we were supposed to be together forever?"
    "All I know is that death would be a welcome relief."
    "And if hell comes after that, then so be it."
    "It couldn't be worse than this."
    scene bg black with dissolve
    pause 1
    $ renpy.full_restart()

label kylie_event_10b:
    if kylie.love.max < 200:
        $ kylie.love.max = 200
    $ kylie_assault_10b = 1 if (kylie.flags.killed == "sasha" or sasha.hidden) else 2 if (kylie.flags.killed == "bree" or bree.hidden) else randint(1, 2)
    "It's been a pretty quiet day for me, just the usual routine of work and studying."
    "Which, to be honest, is a relief after the stress that I've been through recently."
    "Since Kylie really started to ramp up the craziness, it's been hell for me."
    "I've been constantly looking over my shoulder, expecting her to pop up from nowhere."
    "And every time my phone rings, I've braced myself for a call telling me she's done something insane."
    "But now I'm actually starting to think that this might be the end of it."
    "Maybe Kylie was just suffering from a temporary flare-up of the crazies?"
    "Maybe she'd forgotten to take her meds or something as innocent as that?"
    "Whatever the reason, I really hope that she's on the mend now."
    "It just feels good to finally have a day when I can worry about normal stuff."
    "Nothing happening to me that's not normal and completely mundane in nature."
    "Even when I hear the sound of someone screaming, it doesn't phase me."
    "I just assume it's [bree.name] playing on the Zbox with the sound up too loud."
    "Shaking my head, I walk towards the living room, meaning to tell her off."
    scene bg livingroom
    "But when I get to the hallway, I see that the front door is wide open."
    "The screaming is coming from out there, not the living room."
    if kylie_assault_10b == 1:
        bree.say "You...you psycho!"
        bree.say "Get the hell away from me!"
    elif kylie_assault_10b == 2:
        sasha.say "Don't touch me!"
        sasha.say "You crazy fucking bitch!"
    kylie.say "Who are you calling crazy?!?"
    kylie.say "I'll make you pay!"
    kylie.say "You won't take him away from me!"
    "I break into a run as I recognise the voices coming from outside."
    scene bg house
    show kylie a casual yandere knife at mostleft4
    if kylie_assault_10b == 1:
        show bree casual angry at right
    elif kylie_assault_10b == 2:
        show sasha casual angry at right
    "And as soon as I get out of the door, my worst suspicions are confirmed."
    "Kylie's standing on the porch in front of the house."
    "She has a box-cutter in her hand, and a murderous look in her eyes."
    show kylie casual yandere knife at center with move
    if kylie_assault_10b == 1:
        show bree surprised at vshake
        "And she's advancing on [bree.name], who looks like she's been in a fight!"
    elif kylie_assault_10b == 2:
        show sasha surprised at vshake
        "And she's advancing on Sasha, who looks like she's ready for a fight!"
    mike.say "Kylie!"
    mike.say "What the actual fuck?!?"
    "At the sound of my voice, Kylie stops and glances in my direction."
    if kylie_assault_10b == 1:
        "[bree.name] senses the chance to escape from her would-be attacker."
        hide bree with moveoutright
    elif kylie_assault_10b == 2:
        "Sasha senses the chance to escape from her would-be attacker."
        hide sasha with moveoutright
    "And she darts behind me, shooting into the house."
    "For a moment I feel relieved that she's managed to get out of the way."
    "But then it dawns on me that I'm now alone out here."
    "Alone with a potentially murderous Kylie and her weapon of choice!"
    mike.say "N...now calm down, Kylie!"
    mike.say "We don't want anyone getting hurt, do we?"
    "Kylie lets out a cackle of almost demonic laughter."
    "She shakes her head, eyes wide and full of malice."
    show kylie talkative
    kylie.say "Oh, [hero.name]..."
    kylie.say "Are you really that dumb?"
    kylie.say "I'm standing here with a blade in my hand."
    kylie.say "And you just saw me trying to slice up your slut of a housemate!"
    $ kylie.yandere += 20
    show kylie vangry
    kylie.say "OF COURSE I WANT SOMEONE TO GET HURT!"
    show kylie crazyhappy
    "Kylie laughs like true madwoman for a second time."
    hide kylie with dissolve
    "Then she turns and flees from the porch and into the night."
    "I think about running after her, trying to tackle her to the ground."
    "Would she actually turn that box-cutter on me?"
    "But then I hear the sound of a commotion coming from inside the house."
    "And I dismiss the idea in favour of attending to problems closer to home."
    "I rush back into the house, only pausing to lock the door behind me."
    "Because who knows, Kylie might double back and try to come inside!"
    scene bg livingroom
    if kylie_assault_10b == 1:
        show bree sad zorder 2 at center
        "I find [bree.name] in the hallway."
        if sasha.hidden:
            mike.say "[bree.name]..."
            mike.say "Are you okay?"
        else:
            show sasha sad zorder 1 at left5
            "I find [bree.name] in the hallway, being comforted by Sasha."
            mike.say "[bree.name]..."
            mike.say "Are you okay?"
            show sasha angry
            sasha.say "Of course she's not okay, [hero.name]!"
            sasha.say "She just got attacked on her own doorstep!"
            "[bree.name] looks up at me as Sasha finishes her rant."
        "Her face is pale and her eyes wide."
        bree.say "I...I'm okay..."
        bree.say "She didn't cut me with the blade..."
        bree.say "Do...do you know that girl?"
    elif kylie_assault_10b == 2:
        show sasha sad zorder 2 at center
        "I find Sasha in the hallway."
        if bree.hidden:
            mike.say "Sasha..."
            mike.say "Are you okay?"
        else:
            show bree sad zorder 1 at left5
            "I find Sasha in the hallway, being comforted by [bree.name]."
            mike.say "Sasha..."
            mike.say "Are you okay?"
            bree.say "She's shaken up, [hero.name]."
            bree.say "But other than that, she seems okay!"
            "Sasha glares up at me when [bree.name]'s done talking."
        "She sure does look shaken by what just happened."
        "But I can see that she's pretty pissed too!"
        show sasha angry
        sasha.say "Do you know that mad bitch, [hero.name]?"
        sasha.say "Because she seemed to think she knew you!"
        show sasha upset
    "I sigh and nod my head, not looking forward to what I have to say next."
    mike.say "Yeah, I know her."
    mike.say "Her name's Kylie."
    mike.say "She's kind of got it into her head that we're supposed to be together."
    mike.say "Before all of this, she just seemed to be a little intense, you know?"
    mike.say "But now I'm worried that she's gone totally insane!"
    if kylie.flags.killed not in ['bree', 'sasha']:
        "Now both [bree.name] and Sasha are looking at me incredulously."
        show sasha angry
        sasha.say "You're worried that she's flipped out?!?"
        show sasha upset
        show bree talkative
        bree.say "Oh, [hero.name]..."
        bree.say "I think that ship's already sailed!"
        show bree sad
        "I nod my head grimly, because the girls are right."
    elif kylie.flags.killed == 'bree':
        "Now Sasha is looking at me incredulously."
        show sasha angry
        sasha.say "You're worried that she's flipped out?!?"
        sasha.say "I think that ship's already sailed!"
        show sasha
        "I nod my head grimly, because she is right."
    elif kylie.flags.killed == 'sasha':
        "Now [bree.name] is looking at me incredulously."
        show bree talkative
        bree.say "You're worried that she's flipped out?!?"
        bree.say "I think that ship's already sailed!"
        show bree sad
        "I nod my head grimly, because she is right."
    "It's way beyond time that I faced the truth."
    "Kylie's gone totally insane - she's stark, staring mad!"
    "And she's dangerous too, intent on doing serious harm."
    "I have to stop her before it's too late."
    mike.say "Don't worry, I'll handle this."
    mike.say "Kylie's not going to pull this kind of shit again!"
    $ game.room = "livingroom"
    $ kylie.flags.cantgetbetter = True
    $ kylie.flags.nextevent = TemporaryFlag(True, 3)
    return

label kylie_event_10a:
    if kylie.love.max < 200:
        $ kylie.love.max = 200
    $ kylie.yandere.max = 50
    show kylie
    "I know that I'm not exactly the most modern and switched-on guy in the world when it comes to expressing my feelings."
    "But I do acknowledge that I have them."
    "And I try the best I can to show them when it seems to be the right time too."
    "This is one of those times, right here and right now."
    "I just know that I have to make the effort to let someone know how I feel about them."
    "It's Kylie - who else could it possibly be?"
    "I seem to be thinking about her every second that we're apart."
    "And the time that we're together seems to pass by too quickly."
    "Then I can't wait for the next time I'm going to see her."
    "That's why I've resolved to tell her all of this the next time we meet."
    "She's come so far since we first met, changed so much."
    "I mean, she was practically a basket case back then!"
    "Not that I intend to put it quite like that when I tell her..."
    mike.say "Kylie..."
    mike.say "Can I be serious for a minute?"
    show kylie smile
    "Kylie gives me an ironic smile as I say this."
    "And she raises her eyebrows, showing a keen interest."
    show kylie talkative
    kylie.say "Oh no..."
    kylie.say "Here we go!"
    show kylie happy
    kylie.say "A guy that wants to get serious!"
    show kylie normal
    mike.say "Oh, come on, Kylie!"
    mike.say "You do know this is why most guys don't ever open up, right?"
    mike.say "Girls say they want them to all the time - then they shoot them down!"
    show kylie smile
    "Kylie sniggers at this, clearly amused by my pouting."
    "But then she forces herself to stop and looks me straight in the eye."
    show kylie shout
    kylie.say "Okay, [hero.name], point taken."
    kylie.say "Sorry for making fun of you."
    kylie.say "Go ahead and say your piece - I'm all ears!"
    show kylie normal
    "I still feel more than a little humiliated."
    "But I do the best I can to soldier on regardless."
    mike.say "What I wanted to say was this..."
    mike.say "You've come on such an incredible journey, Kylie."
    mike.say "From being the person you were when I first met you..."
    mike.say "To the person you are today!"
    show kylie smile
    "I see the expression on Kylie's face change as I speak."
    show kylie normal
    "Where before she was amused, she now looks surprised."
    show kylie blush
    "And then she begins to blush, embarrassed by my words."
    "But I keep going, determined to finish what I have to say."
    mike.say "You faced your own demons and defeated them."
    mike.say "And you've become such an amazing person since then."
    mike.say "I'm proud of you, and proud to be with you too!"
    mike.say "And I don't think I could love you more."
    show kylie smile
    "I can see that Kylie's getting emotional."
    "There are tears welling in the corner of her eyes."
    "So I need to get through this before she loses it!"
    mike.say "You really are the best thing in my life, Kylie."
    mike.say "And I know this was something you used to say before you got help."
    mike.say "But I truly believe that you were right when you said we were meant to be together."
    mike.say "At least I hope that's how it's going to be for us!"
    show kylie close smile
    "Kylie leans into me, her head on my shoulder."
    "I hear and feel her let out a sigh of contentment."
    show kylie close shout
    kylie.say "Oh, [hero.name]..."
    kylie.say "I always dreamed that we'd be together."
    kylie.say "But I never thought it could be like this!"
    kylie.say "What we have right now - it's so much better."
    $ kylie.yandere -= 5
    show kylie close happy
    kylie.say "I could never have dreamed up something as perfect as this!"
    return

label kylie_event_09b:
    if kylie.love.max < 150:
        $ kylie.love.max = 150
    "Part of me still can't believe what I actually saw in my own bedroom the other night."
    "Kylie, breaking into my home and sabotaging the condoms that I keep on the bedside table!"
    "I had to sit down and look at the things once she'd fled the scene, really study them."
    "Because I needed to see the actual holes that she'd made with the needle."
    "Otherwise I don't think I'd have been able to believe it was real."
    "I might have become convinced that I dreamed it all, or that I was hallucinating a the time!"
    "But picking one up, my worst fears were confirmed."
    "It was all real, every last bit of it."
    "After that I can't stop thinking about it, wondering what in the hell she was trying to achieve."
    "It doesn't make any sense to think that she was expecting me to use the condoms with another girl."
    "Because what good would it do Kylie to engineer a situation where I got somebody else pregnant?"
    "No, she must have been hoping that I'd use one of them when we were sleeping together."
    "That way she could make it look like she wanted to take precautions."
    "But the chances would be pretty good that she'd end up pregnant herself."
    "That had to be it!"
    "Kylie's convinced that we're supposed to be together forever."
    "That our relationship is some kind of divine prophecy, or something crazy like that!"
    "She must have decided that she needs to get pregnant to make sure I stay with her!"
    "Well she can forget about that!"
    "I'm not letting my cock anywhere near that psycho!"
    "Not until she can prove to me that she's anything but crazy."
    "And I don't have to wait too long for the chance to confront her either."
    play sound cell_vibrate
    "Soon enough I get a message on my phone from Kylie, begging me to meet up with her."
    stop sound
    "I keep my response short, agreeing to be there, but not calling her out."
    "I don't want to spook her and lose this opportunity."
    scene bg street
    show kylie a casual smile at center, zoomAt(1.0, (640, 720))
    with fade
    "As soon as I turn up, I see that Kylie's made it here before me."
    "I was expecting her to look serious, even threatening."
    "But I'm surprised to see that she seems pretty upbeat and happy."
    show kylie happy at center, traveling(1.25, 0.5, (640, 880))
    kylie.say "Hi, [hero.name]!"
    show kylie shout
    kylie.say "So glad you agreed to come meet me!"
    show kylie normal
    "I narrow my eyes at Kylie, suspecting some kind of trick."
    mike.say "Of course I came, Kylie."
    mike.say "I came because I want an explanation."
    mike.say "I want to know why you broke into my house, into my room!"
    mike.say "I think you should explain to me why you did what you did!"
    show kylie happy at startle
    "Kylie laughs out loud at this."
    "Not the crazy kind of laugh that I might have been expecting."
    show kylie smile
    "But instead a light and carefree laugh, one that tries to play down my concerns."
    "Not that it's enough to fool me, because it sounds practiced, rather than spontaneous."
    show kylie shout
    kylie.say "I don't know what you're talking about, [hero.name]!"
    show kylie talkative
    kylie.say "I wanted to meet up so that I could say sorry."
    kylie.say "Sorry for being so hard to get hold of recently."
    show kylie b shout
    kylie.say "That and to give you a surprise to make up for it..."
    show kylie normal at center, traveling(1.5, 0.5, (640, 1040))
    "Without asking permission, Kylie reaches out with a hand."
    "I feel her cupping my groin, then squeezing my cock through my pants."
    show kylie b blush
    kylie.say "How about we take a stroll up that alley over there?"
    kylie.say "This surprise is one I have to give you in private!"
    show kylie normal
    menu:
        "Let's do it":
            "Maybe I have got all of this wrong, like Kylie says?"
            "I did kind of put my own spin on what I saw the other day."
            "And should really have asked for her side of the story first."
            "Instead I shouted at her and got all aggressive."
            "But here she is, still trying to be nice to me."
            "And the feeling of her hand down there is pretty hard to ignore!"
            "Ah, what the hell - Kylie deserves another chance."
            mike.say "Okay..."
            mike.say "Okay, Kylie..."
            show kylie smile
            "She smiles even more widely as I agree to what she wants."
            "Kylie grabs my hand and pulls me towards the alley."
            "I follow without a hint of resistance."
            scene bg alley
            show kylie blush at center, zoomAt(1.25, (640, 880))
            with fade
            "And a few seconds later we're at the far end of the alley."
            "It's shaded and secluded down here, hidden from the street."
            "Only now does it occur to me how well hidden we actually are."
            "I mean, you could slit someone's throat right here."
            "And the chances are that nobody on the street would see or hear a thing!"
            "But all those thoughts are banished a moment later."
            scene bg black
            show kylie bj alley casual
            with fade
            "And that's because I feel Kylie tugging at my flies!"
            "She's already down on her knees in front of me."
            "Her hand is slipping inside my pants!"
            "It only takes her a second or two to pull my cock out."
            "Her lips are around it in an instant."
            "It's not even totally hard when she starts kissing and licking."
            "But her attentions soon see to that!"
            show kylie bj blow pleasure
            show mouth_insert kylie zorder 1 at zoomAt(1, (860, 140))
            "I have to brace myself against the wall as Kylie goes to work on me."
            "She's moving with an almost manic energy, like she's got something to prove."
            "And I get the feeling that this is going to be a hot and heavy affair!"
            "In fact, Kylie's head is going back and forth like a jackhammer right now."
            "I can feel my thoughts starting to get confused and hazy."
            "It's like I can't focus on what I came here to confront her about."
            "And when I do recall any of it, the whole thing just seems so silly."
            "What in the hell was I so concerned about?"
            "Kylie was motivated enough to do all of that."
            "So it must mean that she loves me, right?"
            "And now she's trying to make amends."
            "I find myself nodding as Kylie wraps her tongue around my cock."
            mike.say "Oh yeah..."
            show kylie bj normal
            mike.say "Kylie..."
            mike.say "That's so good..."
            mike.say "I love you so fucking much!"
            "The more I praise Kylie, the harder she seems to work."
            show kylie bj pleasure
            "Soon enough she's giving me everything she has."
            "And I'm gasping helplessly as she pushes me towards the end."
            "Kylie senses that I'm getting there, but she doesn't stop."
            $ kylie.love += 10
            $ kylie.yandere -= 2
            show kylie bj cumshot
            show mouth_insert kylie cum
            with hpunch
            "Instead she braces herself and takes it on."
            with hpunch
            "She swallows with determination, not stopping once."
            show kylie bj out -cumshot dickcum normal
            show mouth_insert kylie -cum
            with hpunch
            "And only when I'm done does she release my cock from her mouth."
            hide mouth_insert
            "Kylie's gasping for breath as she looks up at me."
            "But her eyes are so full of love and devotion it's almost heart-breaking."
            "How could I ever have doubted her, even for a moment?"
            "I'm sure we can work through whatever her problems are."
            "Then we can just get on with our lives together."
            $ game.room = "alley"
            $ kylie.flags.cantgetbetter = False
        "No way":
            show kylie surprised at center, traveling(1.25, 0.2, (640, 880))
            "I slap Kylie's hand away from me."
            "And at the same time I take a step backwards."
            mike.say "Get the hell away from me!"
            mike.say "Jesus Christ..."
            mike.say "You really are a fucking psycho!"
            mike.say "Do you even remember what I caught you doing, Kylie?!?"
            "Kylie stumbles back a few feet."
            show kylie normal
            "But then she regains her balance and I see that she's still smiling."
            "She shakes her head at me, like I'm being scolded for some minor indiscretion."
            $ kylie.yandere += 10
            show kylie happy
            kylie.say "Oh, [hero.name]!"
            show kylie talkative
            kylie.say "When will you ever learn?"
            kylie.say "Whatever either of us has done, it's in the past now."
            kylie.say "It doesn't matter, only the future matters for you and me!"
            $ kylie.love += 20
            show kylie crazyhappy
            kylie.say "We're destined to be together, it's written in the stars!"
            show kylie normal at center, traveling(1.0, 0.2, (640, 720))
            "I shake my head and take another step back."
            mike.say "Keep away from me, Kylie!"
            mike.say "So you hear me?!?"
            show kylie sad
            "Kylie just sighs and shakes her head."
            show kylie crazysad
            kylie.say "You're upset, [hero.name], that's all."
            kylie.say "You need some time to get your head in order."
            show kylie crazyhappy
            kylie.say "So I'll be going now."
            kylie.say "But you'll be hearing from me real soon!"
            hide kylie with dissolve
            "With that, she turns and strolls away, waving over her shoulder."
            "I watch her go, trying to suppress a shudder of revulsion."
            "How can she act so calm and collected?"
            "Does she actually think she's done nothing wrong?"
            "I need to think of something to stop this."
            "And I need to do it before she pops up again!"
            $ game.room = "street"
            $ kylie.flags.cantgetbetter = True
    $ kylie.flags.nextevent = TemporaryFlag(True, 3)
    return

label kylie_event_09a:
    if kylie.love.max < 150:
        $ kylie.love.max = 150
    $ kylie.yandere.max = 75
    show kylie at center, zoomAt(1.0, (640, 720))
    "Seeing the changes that have come over Kylie since she started getting help has been amazing."
    "Back when I first met her, she was a girl teetering on the brink of becoming a genuine psycho."
    show kylie shy
    "I was almost convinced that she was beyond help and that I needed to get her out of my life."
    "But now that she's having regular sessions with a therapist, everything's changed for the better."
    show kylie annoyed
    "Kylie's actually facing her demons, owning up to the way that she's behaved in the past."
    "And it's working, she seems to improve every time that I see her now!"
    show kylie smile
    "We can spend quality time together without me worrying about setting her off."
    "In the past it could have been something as small as me saying the wrong thing."
    "Or her catching me being nice to another girl while she was around."
    "Anything like that would have made her jealous."
    "Sometimes it would even send her into a fit of rage!"
    show kylie normal
    "Now she's able to laugh it off and get on with living her life."
    "And she's opening up too, being more honest about the way she feels."
    "Which sometimes catches me off-guard!"
    show kylie shout at center, traveling(1.25, 0.2, (640, 880))
    kylie.say "[hero.name]..."
    kylie.say "I have a confession to make!"
    show kylie normal
    "At the mere mention of the word 'confession', my ears prick up."
    "It's so loaded with connotations of dread that I can't help it."
    "Suddenly Kylie had one hundred percent of my attention."
    mike.say "A confession, Kylie?"
    mike.say "What about?"
    show kylie impressed
    "Kylie fixes me with those huge eyes of hers."
    "They seem to be able to gaze right into my soul!"
    "She takes a deep breath, then lets it out as a heavy sigh."
    show kylie talkative
    kylie.say "Remember when I said that I loved you?"
    show kylie shy
    mike.say "Yeah, Kylie!"
    mike.say "How could I forget something like that?!?"
    show kylie whining
    kylie.say "Well, I was lying!"
    show kylie annoyed
    "I blink and shake my head in surprise."
    "Did Kylie actually just say that she doesn't love me?"
    "Is this what her therapy sessions have made her realise?"
    "Oh no...did I encourage her to pick away at her feelings for me?"
    mike.say "Y...you mean..."
    mike.say "You don't really love me?!?"
    show kylie stuned
    "Kylie seems surprised by my reaction."
    "Now it's her turn to shake her head."
    show kylie surprised
    kylie.say "No, no, no!"
    kylie.say "That's not what I meant at all!"
    show kylie whining
    kylie.say "I was talking about before, [hero.name]!"
    kylie.say "Back when I was in denial about my problems!"
    show kylie shy
    "I feel a sudden rush of relief as Kylie explains herself."
    "And also not a small amount of embarrassment at jumping to the wrong conclusion too."
    mike.say "So you DO love me?"
    mike.say "Is that what you're saying?"
    show kylie talkative
    kylie.say "What I'm trying to say, [hero.name]..."
    kylie.say "Is that I didn't know what I was feeling back then."
    kylie.say "But now I've looked back and made sense of my feelings."
    kylie.say "I've realised that what I felt for you was obsession, not love."
    show kylie annoyed
    "Kylie looks away for a moment."
    "It's like she can't bear to look me in the eye."
    show kylie shy
    "But then she seems to gather her strength."
    show kylie normal
    "And she turns to regard me again."
    show kylie talkative
    kylie.say "I needed to do that, you see?"
    kylie.say "To understand that I didn't really love you before."
    show kylie shout
    kylie.say "Because only by doing that can I truly love you now."
    kylie.say "And I do, [hero.name] - I really do love you!"
    show kylie normal
    "I feel a second wave of relief pass over me as Kylie says this."
    "And I almost need to sit down as the emotions flood through me."
    "I had no idea that she could cause me to have such a dramatic physical reaction!"
    "I guess I also had no idea how much knowing she loved me mattered as well!"
    mike.say "Oh god..."
    mike.say "Kylie, you have no idea..."
    mike.say "I'm SO glad you said that!"
    $ kylie.yandere -= 2
    show kylie happy at startle, center, traveling(1.25, 0.2, (640, 880))
    "Kylie laughs and takes hold of my hands."
    show kylie shout
    kylie.say "Of course I love you, [hero.name]!"
    kylie.say "That's why I'm doing all of this, remember?"
    hide kylie
    show kylie kiss
    with fade
    $ kylie.flags.kiss += 1
    "Kylie pulls me closer to her, wrapping her arms around my waist."
    "She feels so good pressed up close, so soft, warm and welcoming."
    "And the kiss she plants on me a moment later seals the deal."
    "It says so much more than words ever could!"
    $ kylie.flags.nextevent = TemporaryFlag(True, 3)
    return

label kylie_event_08b:
    "It's been a couple of days since I heard from Kylie and I'm starting to get a little worried."
    "Not like I think she's been kidnapped or fled the country, nothing crazy like that."
    "It's just that she was pretty worked up the last time that we met, emotional as well."
    "And it's not like her to disappear on me without at least a text or a phone call."
    "None of the messages that I've left for her seem to have been answered either."
    scene bg livingroom with fade
    "Part of me is even starting to think that I should call the police!"
    "But then I remember that I know Kylie's sister almost as well as I know her."
    "Maybe Alexis knows what's happened to her and where she is right now?"
    "Putting my hand into my pocket for my cell phone, I realise it's not there."
    "And then I remember that I left it charging on my bedside table."
    "No problem, it's not like my room is more than a couple of metres away."
    "I take the stairs two at a time, arriving at my room seconds later."
    "I'm not even consciously thinking as I open the door."
    "My brain's just on autopilot as I hunt for my phone."
    scene bg bedroom1
    show kylie casual y surprised
    with hpunch
    $ game.room = "bedroom1"
    mike.say "Oh..."
    mike.say "Hi, Kylie!"
    "I've waved and nodded to Kylie before I even realise she's there."
    "The sheer strangeness of walking into my room and finding her there is too much."
    "It's like my mind just accepts it and carries on for fear of freaking out!"
    "I walk maybe a couple of steps past Kylie, and then I snap back to reality."
    "Luckily for me, Kylie seems to be as surprised to see me as I am to see her."
    "She stands there, frozen to the spot in the middle of what she's doing."
    "Which gives me the chance to see the condoms from my bedside table spread out before her."
    "Kylie has one in her hand and what looks like a needle in the other."
    "And she's pushing the latter through the former!"
    "Kylie shakes her head and begins to speak."
    show kylie a sadhappy
    kylie.say "[hero.name]!"
    kylie.say "This isn't what it looks like!"
    show kylie annoyed
    "Look at what she's doing and then over to the open window."
    "That must have been how she got in here."
    "But I swear that I locked the damn window - I always do!"
    "And what else could she be doing that what it looks like?!?"
    "What's going on here?"
    "Why is Kylie breaking into my room to sabotage my condoms?"
    "The only things that make sense are also just plain crazy!"
    show kylie normal
    mike.say "Kylie..."
    mike.say "I...I've been worried about you."
    mike.say "Where have you been all this time?"
    mike.say "And what are you doing?"
    "For a moment, Kylie stands still and holds my eye."
    show kylie talkative
    "She opens her mouth and I think that she's going to explain herself."
    show kylie angry at left with ease
    "But then she moves, quicker than I can hope to react."
    "Kylie bolts for the open window."
    hide kylie with easeoutleft
    "I do the best that I can to reach it, to reach her."
    "But she's just too fast for me, like she's charged with manic energy."
    "My hand just barely grazes her heel as she leaps through the window."
    "I half climb out, intending to run after her."
    "Maybe even to tackle her on the lawn out front of the house."
    "But then the thought occurs to me that might not be a good idea."
    "For one thing, I don't like the thought of being seen doing that."
    "Wrestling a fleeing woman in the street isn't a good look for a guy."
    "And if Kylie really is as crazy as she seems, she might be armed with more than needles."
    "I don't want to end today by getting stabbed on my own lawn!"
    "So instead I just sit down on the edge of the window and watch her go."
    "Because I have no clue as to what I should do next."
    "All of this is starting to seriously scare me."
    $ kylie.flags.cantgetbetter = True
    $ hero.gain_item("pierced_condom", hero.has_item("condom"))
    $ hero.gain_item("box_of_pierced_condoms", hero.has_item("box_of_condoms"))
    $ hero.lose_item("condom", hero.has_item("condom"))
    $ hero.lose_item("box_of_condoms", hero.has_item("box_of_condoms"))
    $ kylie.flags.nextevent = TemporaryFlag(True, 3)
    return

label kylie_event_08a:
    "I'm kind of nervous about meeting up with Kylie today, worried about how she's going to be with me."
    "It's not been long since she opened up to me about the obsessive way that she's been acting."
    "That she confessed to me she realised there was something wrong and that she wanted to change."
    "But the agreement was that I'd agree to formalise our relationship if she began getting help."
    "Yeah, I know how that sounds - trust me, I do!"
    "But you have to remember that I was already kind of falling for Kylie before all of this came out."
    "I did have feelings for her, but her almost turning into a crazy stalker was putting me off."
    "So I took a gamble on her being sincere, gave what she proposed a chance to work out."
    "And if that sounds cynical to you, then sue me!"
    "Today's the day that I'm supposed to be getting kind of an update from Kylie."
    "We've agreed to meet up and talk about how her first few sessions with the therapist have gone."
    "And the truth is that I have no idea what to expect."
    "Of course, I want to hear that she's doing well."
    "But on the other hand I know that Kylie has form with this kind of thing."
    "What if she's clever enough to lie about this and convince me she's changing?"
    "I guess the only thing I can do is meet up with her and see what she has to say."
    kylie.say "Hey, [hero.name]!"
    show kylie a casual shout zorder 2 at center, zoomAt(1.0, (940, 720)) with dissolve
    kylie.say "Over here!"
    show kylie a normal at center, traveling (1.25, 1.0, (640, 880))
    "Kylie's almost jumping up and down on the spot when she sees me approaching."
    "She waves a hand in the air, beaming from ear to ear as I walk over to her."
    mike.say "Ah..."
    mike.say "Hey, Kylie..."
    mike.say "You look a lot happier since the last time I saw you."
    show kylie normal at center, traveling (1.5, 1.0, (640, 1040))
    "Kylie's nodding eagerly even before I've finished speaking."
    "She takes hold of my hands and squeezes them, still nodding."
    show kylie shout
    kylie.say "You noticed that?"
    kylie.say "I do, I do!"
    show kylie happy
    kylie.say "I feel SO much better!"
    show kylie normal
    "I force a smile onto my face at this and nod in return."
    "But the truth is that I'm more than a little scared right now."
    "Kylie seems to have exchanged manic jealousy for manic happiness!"
    "And I'm afraid this is going to be the new face of her craziness."
    mike.say "So..."
    mike.say "It went well with the therapist?"
    "At the mention of the help she's been getting, I see a change come over Kylie."
    "She visibly calms down and becomes less animated, even controlling her breathing."
    show kylie talkative
    kylie.say "Ooh..."
    kylie.say "Sorry, [hero.name]..."
    show kylie sadhappy
    kylie.say "I think I got a little carried away there!"
    kylie.say "My doctor says that I have to keep an eye on that."
    show kylie shout
    kylie.say "He taught me all kinds of things to stay calm and focus."
    kylie.say "I...I was just so glad to see you, that's all!"
    show kylie normal
    "All of that sounds good, and Kylie really does seem calmer now."
    "I find myself starting to smile as I feel reassured of her sincerity."
    mike.say "That's great, Kylie."
    mike.say "You really do seem to be more in control now."
    show kylie shout
    kylie.say "Oh yeah - so much more in control!"
    kylie.say "My doctor's helped me to realise that I was wrong."
    show kylie talkative
    kylie.say "Loving someone and controlling them aren't the same thing."
    kylie.say "And I don't need to know where you are all the time either."
    kylie.say "Because love depends on trust!"
    show kylie normal
    mike.say "Wow..."
    mike.say "Sounds like you've really been facing your demons, Kylie!"
    show kylie talkative
    kylie.say "I have, I have..."
    kylie.say "But the thing that's teaching me the most is being with you, [hero.name]!"
    kylie.say "I'm learning how to be happy without the need to be the one in control."
    kylie.say "That feeling a little jealousy is natural now and again."
    show kylie normal
    show shiori zorder 1 at left, blacker with easeinleft
    "Just at that moment a girl happens to walk past us."
    show shiori zorder 1 at left4, blacker with ease
    "I know that I should be concentrating on what Kylie's saying."
    show kylie shy
    show shiori zorder 1 at right, blacker with ease
    "But this girl has literally the biggest chest that I've ever seen!"
    "I can't help staring at her."
    show kylie normal
    hide shiori zorder 1 at blacker with easeoutright
    "But then I realise that Kylie's seen me gazing in her direction."
    "And I look back at her, afraid of what she'll do next."
    show kylie happy
    kylie.say "Ha, ha!"
    show kylie shout
    kylie.say "I bet you thought I was going to go all psycho on you, huh?"
    kylie.say "Well don't worry, [hero.name], I'm not."
    kylie.say "Not after all the progress I've made with my issues."
    kylie.say "I know now that just because you look at another girl, it doesn't mean you love me any less!"
    kylie.say "Being jealous of you for that kind of thing is wrong, I understand that now."
    show kylie normal
    "I find myself smiling at this, almost beaming actually!"
    "Is it just me, or did Kylie get prettier since she started getting better?"
    "I certainly find that I'm drawn to her more now that she's dealing with her demons."
    "And I hope that she keeps on improving, because I'm liking the new Kylie more and more!"
    $ kylie.flags.nextevent = TemporaryFlag(True, 3)
    return

label kylie_event_07b:
    if kylie.love.max < 120:
        $ kylie.love.max = 120
    $ kylie.flags.cantgetbetter = True
    "Today just seemed like any ordinary day in my life, nothing happened to make it seem exceptional at all."
    "In fact, pretty much all of it was forgettable, and I doubt that I could recall it from memory if I tried."
    "Of course that was before I met up with Kylie, because after that, things really started to pick up."
    "I mean, how could they not when you're getting to spend some serious quality time with a girl like her?"
    show kylie casual at center, zoomAt(1.0, (940, 720)) with dissolve
    "It sounds crazy, but her turning up is almost like the sun coming out on an otherwise dark and cloudy day!"
    show kylie casual at center, traveling(1.5, 1.0, (640, 1040))
    "The moment I see Kylie approaching, I hurry over to greet her."
    mike.say "Hey, Kylie!"
    mike.say "I'm so glad you're finally here!"
    "Another girl might have backed off at this, told me that I was being creepy or smothering."
    show kylie smile
    "But not Kylie, who seems instantly delighted with all the attention that I'm giving her."
    show kylie shout
    kylie.say "Aw..."
    kylie.say "That's so sweet of you to say, [hero.name]!"
    show kylie talkative
    kylie.say "I hurried over as fast as I could."
    kylie.say "I just couldn't stand to be away from you for a second longer!"
    show kylie normal
    "Kylie underlines her point by taking hold of my hands and squeezing them tightly."
    hide kylie
    show kylie kiss casual
    with dissolve
    $ kylie.flags.kiss += 1
    "Then she leans in and kisses me, full on the lips and with a great deal of passion."
    "I return the kiss with what I hope is just as much enthusiasm."
    "It's already making my heart race and something else stiffen down below!"
    "Neither of us seems to want to bring the kiss to an end."
    "But eventually we need to breathe, and so to my disappointment it does."
    hide kylie
    show kylie casual normal at center, zoomAt(1.5, (640, 1040))
    with dissolve
    kylie.say "Mmm..."
    show kylie shout
    kylie.say "You don't know how much it means to me, [hero.name]."
    kylie.say "Hearing you talking about me like that - about us like that."
    show kylie happy
    kylie.say "It makes me so sure that we're perfect for each other."
    kylie.say "Sure that we're destined to spend the rest of our lives together too!"
    show kylie normal
    "The statement sounds so odd coming out of the blue like that."
    "And Kylie says it with such firm conviction too."
    "I can't help letting out a little chuckle and shaking my head."
    mike.say "Ah..."
    mike.say "What are you talking about, Kylie?"
    mike.say "I was just happy to see you, yeah?"
    mike.say "What you said sounds like a contract signed in blood or something!"
    show kylie happy at startle
    "Now it's Kylie's turn to laugh and roll her eyes."
    show kylie normal
    "She reacts as though I'm making a joke or something."
    show kylie shout
    kylie.say "Oh, [hero.name] - you're so funny!"
    show kylie talkative
    kylie.say "But don't be silly now, not when we're talking about something so serious!"
    kylie.say "You have to have felt it too, that almost supernatural force drawing us together?"
    show kylie normal
    mike.say "Kylie..."
    mike.say "What are you talking about?"
    mike.say "Seriously, you're starting to scare me a little here!"
    show kylie crazyhappy at startle
    "Kylie just laughs again, but this time it's a very different sound."
    "It's deeper and even a little menacing to my ears."
    show kylie sadhappy
    kylie.say "You know that we're destined to be together, [hero.name]."
    kylie.say "I know that you can feel it in your heart."
    show kylie talkative
    kylie.say "That's why I need us to be totally exclusive from now on."
    show kylie vangry
    kylie.say "You can't be with any other girl but me, understand?"
    kylie.say "You can't be with them, flirt with them or even think about them!"
    show kylie talkative
    kylie.say "Promise me, [hero.name] - promise me that you'll be mine alone!"
    show kylie angry
    menu:
        "Accept":
            $ kylie.set_girlfriend()
            "I don't even have to think of an answer to that question."
            "Because I know what it will be without a conscious thought."
            mike.say "Of course I will, Kylie!"
            mike.say "I can't imagine being with anyone else but you!"
            $ kylie.yandere -= 10
            show kylie normal
            "Kylie's face lights up at this, so much that she's practically beaming."
            show kylie smile
            "She's nodding eagerly, almost tripping over herself as she tries to speak."
            show kylie shout
            kylie.say "Oh..."
            kylie.say "Oh, [hero.name]..."
            kylie.say "I knew it!"
            kylie.say "I just knew it!"
            show kylie smile at center, zoomAt(1.75, (640, 1140))
            with hpunch
            "She leaps forwards and throws her arms around me."
            "And then I find myself in an embrace like that of a constricting snake!"
            show kylie happy
            kylie.say "We were meant to be together - forever!"
            show kylie smile
            "I put my arms around Kylie and return the hug."
            "I can't make much sense of what she's babbling about."
            "But my best guess is that she's just gotten swept up in the emotion of the moment."
            "I'm sure she doesn't mean half of the things she said."
            "Or at least not with the intensity that she said them!"
        "Refuse":
            "Before I can even think of how to answer that, I burst out laughing."
            with vpunch
            "I'm shaking my head at what Kylie just asked me, convinced she must be joking."
            mike.say "You're kidding, right?"
            mike.say "I mean, you have to be kidding!"
            mike.say "That's like the kind of stuff a crazy says in the movies!"
            $ kylie.love -= 2
            $ kylie.yandere += 5
            show kylie angry
            "I can see that this isn't what Kylie wanted to hear."
            "Her face darkens instantly from a smile to a frown."
            "And she's even balling up her fists too!"
            show kylie vangry
            kylie.say "[hero.name]..."
            kylie.say "You know just how much I love you."
            kylie.say "I've tried to make that plain to you."
            show kylie crazyhappy
            kylie.say "So that's why I'm going to ignore what you just said."
            kylie.say "That and give you another chance to answer me correctly!"
            show kylie angry
            "I laugh again and double down on what I already said."
            mike.say "Stop it, Kylie."
            mike.say "You're starting to sound like a psycho!"
            show kylie stuned
            "That word seems to spark something inside of Kylie."
            "Like it makes her far more angry than it has any right to."
            show kylie crazysad
            kylie.say "What did you call me?"
            show kylie angry
            mike.say "I didn't call you anything, Kylie."
            mike.say "I just observed that you SOUND like a psycho!"
            $ kylie.yandere += 5
            show kylie a crazyhappy
            "Kylie waves a finger under my nose at this."
            show kylie vangry
            kylie.say "I can see that you're going to need to be taught a lesson, [hero.name]."
            kylie.say "One that'll make you see things the way they really are!"
            show kylie yandere
            kylie.say "And one that you won't see coming until it's too late!"
            hide kylie with dissolve
            "With that, Kylie turns on her heel and storms away."
            "Which leaves me alone and wondering what the hell just happened between us!"
    $ kylie.flags.nextevent = TemporaryFlag(True, 3)
    return

label kylie_event_07a:
    if kylie.love.max < 120:
        $ kylie.love.max = 120
    "I've just about had enough of the way Kylie's been behaving around me recently."
    "Until now I've been happy to kind of just let it slide, to look the other way, you know?"
    "And I admit that a lot of that was because she's just so damn hot and into me."
    "Plus there was the thrill of her being Alexis's cute little sister too."
    "I mean, it's pretty hot knowing that she had a thing for me so far back!"
    "But this time she's really done it, gone too far!"
    "I'm going to give her a piece of my mind."
    "I don't think she'll like it, but she needs to hear what I have to say."
    show kylie casual sad with dissolve
    "As soon as I lay eyes on Kylie, I open my mouth to speak."
    "But then I see the look on her face."
    "It's downcast, almost dejected."
    "If it were anybody else, I'd say they were ashamed of themselves."
    "But, in my experience at least, that's just not Kylie's style!"
    "I can feel all the anger and irritation draining out of me."
    "Suddenly it seems churlish to shout at Kylie when she's in such a state."
    mike.say "Ah, Kylie..."
    mike.say "What's wrong?"
    mike.say "You look like you just got some bad news!"
    show kylie annoyed
    "Kylie looks away from me almost as soon as I speak."
    "And it takes a little while for her to turn her head back in my direction."
    show kylie sadhappy
    "But when she does I can see that she's forced a grim smile onto her face."
    kylie.say "I..."
    kylie.say "I have something to say to you, [hero.name]."
    show kylie whining
    kylie.say "I...I'm sorry!"
    show kylie sad
    "I can't help looking more than a little stunned."
    "Of all the unexpected things that Kylie's done, that's probably the most surprising."
    "I never actually thought that I'd hear her apologising for anything!"
    mike.say "Erm..."
    mike.say "For what, Kylie?"
    mike.say "What exactly are you sorry for?"
    "Kylie wrings her hands together and lets out a huge sigh."
    "I can see that this is really hard for her, that she's struggling."
    "So I resist the urge to tear into her like I was planning to."
    show kylie whining
    kylie.say "Oh, you know what for, [hero.name]!"
    kylie.say "For everything!"
    kylie.say "I just...I don't seem to be able to stop myself sometimes!"
    kylie.say "I want something SO much that I can't see anything else!"
    show kylie annoyed
    "Kylie frowns and stares down at her feet."
    show kylie whining
    kylie.say "So I'm sorry, okay?"
    kylie.say "But I wanted to tell you that I'm trying to change."
    kylie.say "Really, I am!"
    kylie.say "But I think I'm going to need your help..."
    show kylie sad
    "Oh, here we go!"
    "I knew that there had to be a catch!"
    mike.say "It's great that you can admit you have a problem, Kylie."
    mike.say "Don't they say that's the first step on the road to recovery?"
    mike.say "But what can I do to help?"
    "Kylie looks up at me, already beginning to blush."
    "But she presses on with what she has to say all the same."
    show kylie talkative
    kylie.say "You know how I feel about you, [hero.name]."
    kylie.say "And that could be the motivation I need to change."
    kylie.say "If...if you let me be your girlfriend..."
    kylie.say "Then I'll start seeing a therapist, I promise!"
    show kylie sad
    "Kylie looks at me with those huge, gorgeous eyes of hers."
    "And I just know that she's pinning all of her hopes on my answer."
    menu:
        "Accept":
            $ kylie.set_girlfriend()
            $ kylie.yandere.max = 90
            "Geez...I came here to lay it on the line for Kylie."
            "Now I find myself listening as she pleads for my help instead."
            "Part of me thinks that, for this to work, she should be doing it for herself."
            "But then she's gotten this far without anyone helping her out."
            "What good has that done - the girl's turning into a basket case!"
            "And it's that thought that makes my mind up for me."
            mike.say "If you really mean it, Kylie..."
            mike.say "Then yeah, we can give it a go."
            mike.say "But only if you keep seeing someone, right?"
            mike.say "And I have to see you improving too!"
            "Yeah, I know, I know."
            "It's not the most inspiring of speeches."
            "And it's definitely not an auspicious way to start a relationship."
            "But these are the cards I've been dealt."
            "And this is how I'm going to play them."
            show kylie smile
            "Not that Kylie seems to react that way."
            "From her reaction, you'd think I just got down on one knee and proposed!"
            $ kylie.love += 2
            hide kylie
            show kylie close casual smile
            with hpunch
            "She leaps forwards, throwing her arms around me."
            show kylie shout
            kylie.say "Oh, thank you, [hero.name]!"
            kylie.say "You don't know what this means to me!"
            kylie.say "So long as I have you, I just know this will work out!"
            kylie.say "If I have you, then I can do anything!"
            show kylie normal
            "I return the embrace, slowly relaxing and beginning to enjoy it."
            "Maybe this is the best thing for the both of us?"
            "Kylie certainly likes me, and I can't deny I want her."
            "This way we can grow together in an honest, open way."
            "If she's as good as her word, this could actually work out."
            "And, if we're lucky, it might be the beginning of something really special too."
        "Refuse":
            $ kylie.flags.cantgetbetter = True
            "But then I remember why I wanted to confront Kylie in the first place."
            "She was being crazy because she wanted to be in a relationship with me."
            "So how is giving her what she wants going to help her change anything?"
            mike.say "Geez, Kylie..."
            mike.say "You had me there for a moment."
            mike.say "Right up until the 'be my girlfriend' line!"
            show kylie annoyed
            "Kylie shakes her head at this."
            "But I'm not finished saying my piece."
            mike.say "It's great that you admit you have a problem."
            mike.say "But you've got to make that change for yourself, don't you see that?"
            mike.say "You need to sort out you before there can be an us!"
            show kylie sad
            kylie.say "But, [hero.name]..."
            kylie.say "I need you, really I do!"
            kylie.say "I don't know if I can do it on my own!"
            mike.say "Then you should find out, Kylie."
            mike.say "Go do it and then come tell me what happened."
            mike.say "But I can't help you until you help yourself!"
            $ kylie.love -= 5
            hide kylie with dissolve
            "With that, I turn and walk away."
            "And much to my surprise, Kylie lets me go."
            "She doesn't argue or run after me either."
            "So maybe I did manage to get through to her this time?"
            "I guess only time will tell."
    $ kylie.flags.nextevent = TemporaryFlag(True, 3)
    return

label kylie_event_06:
    $ target = Person.find(kylie.flags.target)
    "You know that weird feeling of being watched, the one that's something to do with the unconscious parts of your brain?"
    "It's not like you know that's what it is at first, more like it's an uneasy tingling as the hairs on the back of your neck stand up."
    "Only when you finally stop what you're doing and look around do you start to feel like there's someone snooping on you."
    "I look up from my desk after realising that the last sentence I wrote is nonsensical garbage."
    "It's getting stupidly late, and I should have turned in a good few hours ago to keep from feeling like a zombie in the morning."
    "But still, somehow I know that it's not the fact that I've been up, burning the midnight oil, that's distracting me."
    "For some reason, my eyes are drawn to the window, even though the curtains have been drawn all evening."
    "I try to shake off the feeling, telling myself that I'm probably just stressed and tired from all the work I've been doing of late."
    "And yet I keep looking back at the window, as if there's something on the other side of the glass that I won't be able to rest until I've seen."
    "More to prove to myself that this whole thing is just a stupid distraction than anything else, I push back my chair and get up."
    "As I walk the short distance to the window, I have no choice but to stretch out my aching back and listen to the noises that my protesting body makes."
    "That can't be good - surely someone of my age shouldn't creak and crack like that?"
    "I don't do anything so dramatic as throwing the curtains aside, just opening them wide enough to stick my head through the gap."
    "Outside there's nothing remarkable to be seen at first glance, just a typically dark, unremarkable night."
    "This alone should have be enough to convince me that I'm jumping at shadows."
    "But I linger a little longer, enjoying the chance to take a break from my work and stare out of the window instead."
    show bg house at center, zoomAt(1.75, (640, 1240))
    show kylie b annoyed at center, zoomAt(0.75, (640, 840)), dark
    with fade
    "And that's when I see the figure, standing beneath one of the street-lights that line the pavement outside my house."
    "A chill runs down my spine, and I jump back away from the window, surprised to have seen anyone out there so late at night."
    "But then I take a second glance down at the figure, and that's when I realize that I recognise the person."
    mike.say "Kylie..."
    show kylie normal
    "As if she hears me murmur her name, Kylie chooses that exact moment to look directly at my window."
    show kylie a crazyhappy
    "Her face is a veritable picture of delight as she smiles and waves at me eagerly."
    "Though in the harsh glare of the street-light, Kylie does rather take on the aspect of a leering ghoul thanks to her wide grin and large eyes."
    "Baffled as to just what I should do in this situation, I resort to opening the window and calling out to her."
    mike.say "Kylie - what in the hell are you doing out there?!?"
    show kylie sadhappy
    "Kylie's brows wrinkle in apparent puzzlement."
    kylie.say "I've come to see you, [hero.name] - isn't it obvious?"
    mike.say "But why - do you even know what time it is?"
    show kylie sad
    kylie.say "I need your help - that's why."
    kylie.say "Well, are you going to let me in or not?"
    "It seems like she's not going to volunteer anything more than that."
    "And as though my question about the lateness of the hour is just going to be ignored too."
    "I'm reluctant to open the door to anyone that turns up at random and this late at night, no matter what they want from me."
    "But I'm already more than a little concerned about Kylie's stability, so just turning her away seems a pretty harsh thing to do."
    "Plus, I don't want her to cause a scene in the street, maybe even make one of my neighbours call the police..."
    menu:
        "Let her in":
            "How long have I been saying that I wanted to be a friend to Kylie, that I wanted to help her out?"
            "Well, I guess this is the point where I have to put my money where my mouth is..."
            mike.say "Okay - just come to the door and I'll be right up."
            scene bg livingroom
            with fade
            "Hoping that I haven't just made a massive mistake, I hurry upstairs and open the front door for Kylie."
            scene bg house
            show kylie happy
            with wiperight
            "Kylie stands in front of me, positively beaming with happiness at being let in."
            kylie.say "Thanks again for inviting me in, [hero.name]!"
            mike.say "Well...what kind of a friend would I be if I left you out there, alone and in the cold?"
            show kylie normal
            kylie.say "Oh, [hero.name] - I'm so lucky to have a friend like you!"
            mike.say "Erm...so...here we are then..."
            "Kylie remains silent, but she looks at me in a suggestive manner, nodding eagerly."
            mike.say "Just wait here a second - I need to take care of a few things in my room."
            show kylie crazyhappy
            "At the mention of my bedroom, Kylie's smile seems to widen even more."
            scene bg bedroom1
            with fade
            "While Kylie takes off her shoes in the hallway, I race back downstairs and into my room."
            "My tidying basically consists of cramming things into drawers and shoving what's strewn across the floor under my bed."
            "When I've done all I can, the place still looks pretty messy."
            "But hopefully, if I keep the lighting to a couple of lamps, it won't be all that obvious."
            scene bg livingroom
            show kylie normal
            with fade
            "I go back out and onto the main floor, finding Kylie staring right at me from the entrance hallway."
            "She has that open, innocent look on her face that just seems to be designed to make me melt."
            "When she does that, I almost instantly forget any worries that I might have had about her."
            mike.say "All clear - come on down."
            "Nodding as she begins to run down the stairs, Kylie comes as soon as she's called."
            scene bg bedroom1
            show kylie
            with fade
            "It's not like Kylie's the first girl that I've had inside my room."
            show kylie at center, zoomAt(1.5, (640, 1140)), vshake
            "But for some reason, it feels different as she walks in and sits down on the bed beside me."
            mike.say "So...are you going to tell me why you turned up on my doorstep like this?"
            mike.say "Because I have to tell you, it's got me pretty worried for you right now."
            "Though I'm trying to voice my concern for her, Kylie's reaction is more like I'd have expected if I'd told her I was madly in love with her."
            show kylie b blush
            kylie.say "Oh, [hero.name] - you really think that much about me?"
            kylie.say "I just knew you were the right person to turn to!"
            show kylie smile
            mike.say "Erm...yeah...right..."
            mike.say "Oh, I'm being a bad host."
            mike.say "Can I get you anything?"
            mike.say "It's cold out there tonight - would you like a hot drink?"
            mike.say "Not coffee this late at night, but tea?"
            show kylie happy
            kylie.say "That'd be lovely!"
            show kylie normal
            mike.say "Okay, I'll be right back."
            "Kylie watches me until I leave the room, smiling sweetly the whole time."
            scene bg livingroom with dissolve
            "I pause on the landing, pulling out my mobile and logging onto the site from which I can watch the camera that I have set up in my room."
            "Normally I'd only check the feed if I suspected that I'd had a break-in or something like that."
            "But I really do want to see what Kylie gets up to in my absence."
            "Sure, she might spot the camera, but she won't know if it's turned on or not."
            scene bg kitchen with dissolve
            "Watching the screen, I make my way to the kitchen and begin making her tea."
            "It's not long before I see something that makes me stop what I'm doing and stare at the image before me."
            "Almost as soon as I'm on the stairs, Kylie darts for my laundry pile, rummaging through it like a determined terrier."
            "She surfaces a moment later, a pair of my briefs clutched in her hand."
            "I watch as she lies back on the bed and pulls the dirty underwear over her face, putting the crotch right under her nose."
            "Her breathing is muffled, but I can hear her taking in long, deep breaths all the same."
            kylie.say "Mmm...[hero.name]...ahh..."
            "Kylie lies there like that for about thirty seconds, and then pulls the briefs off of her face."
            "She balls them up and crams them down between her considerable breasts, evidently wanting to keep them as some kind of trophy."
            kylie.say "What else are you hiding, [hero.name]?"
            kylie.say "Let's take a quick peek, shall we?"
            "Kylie slides neatly off the bed and begins to rifle through the contents of my bedside drawers."
            "I have no idea what she's hoping to find in there, as I'm not the kind of guy to keep a secret diary or treasured keepsakes in there."
            "She seems to be getting more than a little frustrated, that is until she happens upon a bundle of old photos in the bottom of one drawer."
            "I know instantly what those are - shots that I took on a disposable camera of myself with an old girlfriend."
            "Back then, most mobile phones only had shitty cameras, and you could still buy that kind of camera and get the shots developed easily."
            "I only keep them for the sake of the pleasant memories they stir in me."
            "But they seem to have quite the opposite effect on Kylie, as she bears her teeth, grinding them in what looks like anger."
            "She roots around in the same drawer until she finds a black marker pen, and begins to scribble all over the girl in the picture."
            "With her free hand, she fishes the soiled briefs out of her bra and shoves them under her skirt."
            "I don't need any help to know what she does with them next, as I can see her hand going up and down under the fabric."
            "And I can clearly see the look of almost manic excitement on her face as she rubs the crotch of the briefs against the lips of her pussy."
            "Kylie combines the act of defacing the image of my former girlfriend with that of frantically pleasuring herself with something that's been against my cock."
            "The message is quite a simple one to figure out..."
            "Once the girl's image has been completely obliterated, Kylie seems satisfied enough to stuff the briefs back into their hiding place once more."
            "She shuffles the photo back into the pile and tosses them back inside the drawer where she found them."
            "By this time, the kettle has boiled and the tea is brewed, so I decide to hurry back downstairs before Kylie can get up to anything else."
            scene bg bedroom1
            show kylie b normal at center, zoomAt(1.5, (640, 1140))
            with fade
            "I open the door to find her sitting on the bed in almost the precise spot that I left her, face a picture of innocence."
            show kylie shout
            kylie.say "Oh, thank goodness you're back - I was starting to get worried!"
            show kylie normal
            "I frown a little as I hand over the steaming cup of tea."
            mike.say "Erm...I was only gone like five minutes at the most!"
            show kylie shout
            kylie.say "Well, it felt like a real long time to me..."
            show kylie normal
            "Oh god, I can feel her locking onto me with those huge eyes and just pulling me in again."
            "I should be confronting her with what I just saw on the camera, telling her off for stealing my clothes and defacing my photos."
            "But she's just so beguiling somehow - I can't stay mad at her!"
            "And it's not just because she's unbelievably hot - honestly, it's not."
            "The more I get to know about her, admittedly numerous, flaws; the more I want to be the one to save her."
            "She's like some kind of beautiful, broken doll...and I can't help wanting to be the guy that repairs her, that makes her whole again."
            "Kylie leans in closer to me, and I can smell that unique scent that I noticed the last time she was this near."
            "We're alone, in my room, on my bed..."
            mike.say "Kylie..."
            show kylie shout
            kylie.say "Yes, [hero.name]..."
            show kylie normal
            mike.say "You still haven't told me why you came here."
            show kylie sadhappy
            kylie.say "Isn't it obvious?"
            kylie.say "I came because I missed you [hero.name]..."
            kylie.say "And because..."
            "Kylie entwines her fingertips, staring sheepishly down at them in her lap."
            kylie.say "And...I wanted to say sorry...for how I was when I saw you with that girl the other day..."
            show kylie sad
            "I have to be honest with her, otherwise I won't be able to look her in the face."
            mike.say "Kylie - what I said to you then, about [target.name]..."
            mike.say "It wasn't the absolute truth."
            mike.say "What I'm trying to say is...I don't think I feel as strongly about her as I might have made it sound..."
            "Without missing a beat, Kylie leaps on the opportunity that I've just given her."
            show kylie blush
            kylie.say "So you're basically saying that you might have stronger feelings for me?!?"
            show kylie shy
            mike.say "Yes...maybe...I don't really know!"
            show kylie shout
            kylie.say "Don't worry, [hero.name] - that's good enough for me!"
            show kylie talkative
            kylie.say "All that really matters is that I like you and you like me too."
            kylie.say "We can fill in all the little details along the way!"
            show kylie normal at center, zoomAt(1.5, (640, 1040)) with ease
            "And with that, she's getting to her feet as though she intends to leave."
            mike.say "You're...you're leaving?"
            show kylie shout
            kylie.say "I sure am - you'll get nothing more from me tonight, you naughty boy, you!"
            "Still more than a little bewildered, I show her to the door and say goodnight."
            hide kylie with easeoutright
            pause 0.5
            scene bg bedroom1 with fade
            "When I get back to my room, I have the urge to watch back the footage of her in my room."
            "But the password to my phone escapes me, and I can't find the scrap of paper on my desk where I'd scribbled it down for just such an occasion."
            "Dismissing it as unimportant, I climb into bed and finally managed to fall sound asleep."
        "Don't let her come in.":
            "Okay, when did my life become like something out of a horror movie?"
            "Seriously, this girl should have her own sinister theme music, just to warn people when she's around."
            "As hot as she undoubtedly is, Kylie's obviously fallen out of the crazy tree and hit every branch on the way down."
            "If I needed serious motivation to focus my attentions on [target.name], then she just gave it to me in spades."
            scene bg house at center, zoomAt(1.75, (640, 1240)), blur(16), dark with dissolve
            "Yanking the curtains closed, I turn off all the lights in the room before crawling into bed."
            "Almost as soon as I'm under the covers, I can feel myself drifting off."
            "Even the memory of Kylie, staring up at me from the street below, seem to fade away..."
            scene bg bedroom1 with fade
            $ game.pass_time(1, True)
            "When I wake up, I'm surprised not to have heard my alarm go off."
            "I roll over and look at the clock on the bedside table, convinced that it must be dawn already."
            "But, much to my surprise, I see that it's not much more than twenty minutes since I got into bed."
            "A moment later I take a breath and cough, feeling just how dry and scratchy my throat feels."
            "No mystery as to what woke me up then."
            "Time for a quick trip to the kitchen for a glass of water..."
            "Dragging myself out of bed, I wander up the stairs in the general direction of the kitchen."
            scene bg kitchen with fade
            "Padding barefoot across the tiled kitchen floor, I grab a glass and fill it from the tap."
            "As I drink the water, I begin to wake up a little more."
            "The memory of Kylie, standing there in the street comes back to me."
            "I laugh a little and shake my head, still not sure what she was hoping to achieve by turning up at such a late hour."
            "Surely she must have gotten too cold and uncomfortable to still be out there, right?"
            "It's at that very moment that I swear I see something, pale and oval in shape, looking in through the window."
            with hpunch
            "The glass falls from my hand, shattering on the floor and I leap back to avoid the shower of shards."
            "When I look back at the window, the shape, whatever it was, is gone."
            "Damn it - I could have sworn that was a face!"
            "Still shaking, I force myself to sweep up the glass and then begin to make my way back to bed."
            "I walk into the hallway, making for the stairs, telling myself the whole time that I was just seeing things that weren't there."
            play sound door_knock
            "But as I reach the top of the stairs, I hear a slow, heavy knocking at the front door."
            "I freeze in place, only my head turning to stare at the frosted glass panes in the door."
            "By the street-lights, I can just make out a figure standing there, its head framed in a mass of blonde hair."
            "It's Kylie - it has to be!"
            "I try to take comfort from the fact that the door is locked and securely bolted as I turn my head away."
            "Taking the stairs one at a time and making as little sound as possible, I sneak down to my room."
            "Feeling like I could hear the sound of breaking glass and splintering wood at any given second, I finally make it to the sanctuary of my bedroom."
            scene bg bedroom1 with fade
            "Once inside, I hastily jam a chair under the door-handle and make sure that my phone is in reach on the bedside table."
            "That done, I crawl back into bed and pull the covers up almost to the level of my nose."
            "Part of me can't believe that I'm this afraid of a girl."
            "But another part of me is hoping and praying that she's gone long before morning comes around."
    return

label kylie_event_05:
    $ target = Person.find(kylie.flags.target)
    "After the last encounter that I had with Kylie and her catching me talking to [target.name], I was worried about how she'd react the next time I saw her."
    "I might not have got my feelings for [target.name] one hundred percent straight yet, but I don't see why that should stop Kylie and I still being friends."
    "She's a hell of a lot of fun to be around, at least when she's in a good mood..."
    "And you can't avoid the fact that she's pretty hot to boot!"
    show kylie normal with easeinright
    "So when I bump into her at uni, I'm relieved to see that she's all smiles at the sight of me."
    show kylie smile
    "It's almost as though the last encounter we had never happened at all."
    "Weird how she seems to be able to turn things on and off like that..."
    show kylie sadhappy
    kylie.say "Oh [hero.name] - will you just look at all of this!"
    mike.say "Look at what, Kylie?"
    show kylie sad
    "Kylie makes a helpless face as she holds up an armful of textbooks, notebooks and other assorted papers."
    "Coursework - that's something anyone taking a class can appreciate!"
    mike.say "Ouch - sorry to see such a mountain of work!"
    mike.say "I know just how you must feel."
    show kylie whining
    kylie.say "Urgh...it's just so BORING!"
    kylie.say "I feel like I just want to toss them all in the river - or set fire to them, and watch it all burn..."
    kylie.say "Coursework really sucks."
    show kylie sad
    mike.say "I know, Kylie - we've all been there, wanting to just throw it all away."
    mike.say "But the alternative's failing, which is much worse."
    show kylie shout
    kylie.say "It's just so overwhelming though!"
    kylie.say "Maybe if I had a little help though, a study partner, or even a mentor of a kind..."
    show kylie normal
    "Suddenly, Kylie puts the papers down and clasps her hands together in front of me."
    show kylie sadhappy
    "She's making serious puppy-dog eyes at me now, and she's disturbingly good at it too."
    mike.say "Ah...Kylie - are you seriously asking for my help with your studies?"
    show kylie shout
    kylie.say "Oh, [hero.name] - that's so sweet of you!"
    kylie.say "I accept!"
    show kylie b smile at center, zoomAt(1.5, (640, 1040))
    "Kylie makes sure to cross her arms under her bosom as she leans forward, plumping up her already impressive chest."
    "If her intention was to distract and confuse me, then she's been very successful indeed."
    mike.say "Ah...I...erm..."
    show kylie shout
    kylie.say "You have NO idea how grateful I am that you'd help me..."
    kylie.say "That you'd indulge me like this."
    show kylie normal
    "Indulge her?"
    "Oh yeah - I'd indulge that, all day long!"
    "No, wait a minute - what was the question again?!?"
    menu:
        "Agree":
            "I can't keep on saying that I want to be Kylie's friend with a straight face if I won't help her out when she needs it."
            "Plus, this is going to involve ploughing through all of that coursework she just showed me, and that's pretty dry stuff."
            "Not much chance of things getting out of hand while we're preoccupied with that little lot either."
            mike.say "Okay, I'll help you out as much as I can."
            mike.say "But we're going to need some place quiet."
            "I think through the options that occur to me, and then make a suggestion of venue."
            mike.say "Both of my housemates should be out right now, so how about we go to my place to study?"
            show kylie happy
            kylie.say "That sounds perfect - let's get going!"
            show kylie smile
            "Kylie seems very enthusiastic, but then she's just got the help she wanted with her studies."
            "So she's bound to be excited at the prospect - isn't she?"
            scene bg black with timelaps
            pause 0.5
            scene bg house
            show kylie shout
            with timelaps
            kylie.say "Ooh...nice pad, [hero.name]!"
            kylie.say "I should study with you more often..."
            scene bg livingroom
            show kylie
            with fade
            "Once we're in the house and I'm sure [bree.name] and Sasha are out, I show Kylie into the living room."
            "We could use the dining room table, but I want a more relaxed atmosphere, and so I sit down on the sofa in front of the coffee-table."
            show kylie at center, zoomAt(1.5, (640, 1140)) with fade
            "Kylie settles herself down on the sofa beside me, hands neatly folded in her lap."
            "I almost find myself laughing at how refined she looks, almost regal in her aspect."
            "The effect is somewhat spoiled by the size of her chest though!"
            "Not that I don't find them very impressive, especially this close up."
            "Taking such a long glance at her hands in her lap, I can't help but notice the thick, black stockings that Kylie's wearing."
            "Pulled up almost to the hemline of her skirt, I think I finally understand why they figure so prominently in all those porn videos..."
            "They're just stockings, made out of mundane materials, but somehow they're insanely distracting."
            "But then the complete package is more than a little distracting too."
            "It's weird to find myself doing something so everyday and routine with a girl this hot."
            "Almost like I'm living a dream and just waiting for the moment when I wake up."
            "I wonder what we look like, Kylie and I."
            "Do we make a cute couple, or would people just not believe that I even had a chance with a girl this stunning?"
            "But anyway, back to reality..."
            mike.say "Right then - let's have a look at the first of these equations and you can tell me what's got you stumped..."
            "Instinctively, I lean over the first page of the textbook open on the coffee table."
            "And, of course, Kylie almost immediately does the same."
            "It's weird, but you never really take in someone's scent until you're this close to them."
            "Kylie's scent puzzles me a little, in as much as I can't decide if it's a perfume or natural."
            "Either way it's intriguing, in a way I never thought a smell could be."
            "But as usual, there's soon a physical sensation that outdoes it."
            "Something large and very soft is pressing against my arm as Kylie leans in."
            "I think you can guess what it is..."
            mike.say "Do you know what this sign here calls for, what you need to do?"
            show kylie talkative
            kylie.say "No [hero.name], I don't!"
            kylie.say "I think you need to show me..."
            show kylie annoyed
            "Kylie's pouting like no student of mathematics ever pouted to be shown the answer before."
            "Time to show her what a real mathematician can do!"
            mike.say "This symbol here indicates that the total can be changed - but in this case, it's not just a case of simple division..."
            "I can see how the problem might baffle a beginner, but this is basic stuff for someone of my level."
            show kylie talkative
            kylie.say "Hmm...I think I get it, [hero.name] - but it's so fucking dull!"
            show kylie annoyed
            "Kylie frowns and lets out a cute, pouting sigh as she leans her head in closer still."
            "Her long, blonde hair falls over my shoulder, locks brushing against my cheek."
            mike.say "I...I guess that's...that's true!"
            show kylie whining
            kylie.say "Hmmm...I'm bored, [hero.name]..."
            show kylie sad
            "Kylie sits up, just a little straighter, her hand brushing aside my hair by my ear."
            "Her voice is breathy, almost a whisper in my ear as she speaks."
            show kylie talkative
            kylie.say "How about we go do something...else?"
            show kylie normal
            mike.say "No, I don't think we should...I don't think we should give up quite so quickly!"
            show kylie sad
            "Kylie pulls back a little way, but not so far that I can't see the look in her eyes."
            show kylie whining
            kylie.say "So...you don't want to..."
            show kylie sad
            "She strokes the back of her hand down my cheek, and then slips her fingers around the back of my neck."
            mike.say "After...we can go somewhere - after we get finished with this, okay?"
            mike.say "After we finish here though, okay?"
            show kylie normal
            "At my words, any trace of disappointment disappears from Kylie's face, and she practically beams at me."
            show kylie shout
            kylie.say "Oh, yes - that sounds really good!"
            show kylie normal
            "With that cleared up, we get back to the matter at hand."
            "But all too soon, I begin to agree with Kylie - this is pretty boring."
            "Maybe calling an end to it early and doing something else would reinvigorate us?"
            "Our minds - obviously I meant, reinvigorate our minds!"
        "Refuse":
            "I may know my stuff in the areas that I'm studying, but I'm no tutor the likes of which it sounds as though Kylie needs."
            "Plus there's the issue of her clearly wanting to manoeuvre me into a situation where we're all alone with no witnesses."
            mike.say "I would, Kylie, honestly I would."
            mike.say "But those equations are making my eyes spin just to look at them."
            mike.say "On top of that, I have a ton of my own coursework to get done too."
            show kylie angry
            "Kylie's eyes were doe-like and soft before now, but they suddenly become hard and almost hateful."
            $ kylie.yandere += 5
            "I was expecting Kylie to be disappointed, maybe even take it badly enough to throw a tantrum in anger."
            "But she almost jumps back from me as if in shock, her jaw hanging open with obvious outrage."
            show kylie vangry
            kylie.say "Well, I never expected to get that kind of response from you!"
            kylie.say "I really thought you were my friend, [hero.name] - I thought that you cared about me!"
            show kylie angry
            mike.say "Ah, look, Kylie...I'm sorry you're disappointed, but..."
            show kylie talkative
            kylie.say "NO...no...it's fine...fine."
            show kylie annoyed
            "Kylie looks down and away from me, half her face falling into shadow and looking surprisingly dramatic as a result."
            show kylie talkative
            kylie.say "I suppose that you only study with much smarter girls than me, right?"
            show kylie annoyed
            "It's now I notice that Kylie is toying with the bracelet around one of her wrists."
            "She pulls and tugs at it constantly, wrapping it around her fingers as if trying to use the motion to bleed off the tension she's feeling."
            "Suddenly, the band snaps, and the beads that were strung on it go flying in every direction imaginable."
            mike.say "Jesus, Kylie!"
            show kylie vangry
            kylie.say "Urgh...I can't believe this is happening to me!"
            show kylie sad
            "Kylie looks up again, and I'm taken by surprise by the tears welling in the corner of her eyes."
            show kylie whining
            kylie.say "Would it have been so bad to just spend a little time studying with me?"
            kylie.say "Is the thought of spending time with me really that awful?"
            show kylie sad
            mike.say "No, Kylie - that's not what I meant at all!"
            show kylie angry at center, zoomAt(1.5, (640, 1040))
            with hpunch
            "She takes me by surprise then, stepping in close and grabbing me by the collar with an unexpected show of strength."
            show kylie vangry
            kylie.say "Well fuck it - like it or not, you're coming with me anyway!"
            show kylie angry
            mike.say "What the hell..."
            with hpunch
            "Kylie begins pulling me off by the collar, hauling me away against my will."
            mike.say "Kylie...Kylie, stop!"
            mike.say "This is crazy - you can't just force me to do what you want!"
            show kylie vangry
            kylie.say "Oh, can't I now?!?"
            show kylie angry at center, zoomAt(2, (640, 1440))
            with hpunch
            "Kylie spins around and puts her face within inches of mine, almost nose-to-nose."
            "I can see from the look in her narrowed eyes that she's definitely not joking around with me."
            "The sudden burst of strength, the physical force to get what she wants, the almost manic look in her eyes."
            "A large part of me is pretty scared of her right now."
            "But there's a part of me that's oddly excited too..."
            show kylie whining
            kylie.say "..."
            show kylie sad
            "Suddenly the fire seems to go out of Kylie's eyes, and I feel the strength of her grip on my collar weaken to almost nothing."
            show kylie sad at center, zoomAt(1.5, (640, 1040))
            "She sighs, so deeply and with such emotion that if feels like the weight of the entire world is settling onto her shoulders."
            show kylie whining
            kylie.say "No...you're right - I can't force you to come with me."
            kylie.say "I'm sorry, [hero.name]...sometimes I just get...emotional, I guess."
            hide kylie
            show kylie casual sad
            with hpunch
            "I rub my neck nervously, not really knowing what's the best thing to say or do right now."
            "I want to help Kylie if at all I can, but the truth is that she's staring to scare me a little."
            mike.say "Ah...well...we all get carried away once in a while..."
            show kylie whining
            kylie.say "No...it's not like that."
            kylie.say "It's...different - but I don't know how to describe just how!"
            show kylie sad
            "It's hard to get a handle on just what Kylie's talking about."
            "But it sounds like she's keeping some kind of dark secret from the world at large."
            mike.say "We can always study together some other time, Kylie."
            mike.say "Or we can talk about your feelings, if you'd like..."
            show kylie surprised
            kylie.say "Huh?"
            show kylie sadhappy
            kylie.say "Oh...okay...whatever."
            hide kylie with moveoutleft
            "As I watch Kylie turn and walk away from me, I'm distracted by the myriad of thoughts and feelings she's inspired in me."
            "So much so that I'm genuinely not looking where I'm going."
            "Before I know it, I've gone and walked into someone coming the other way."
            show alexis stuned with hpunch
            "Of all the people in the world - it's Alexis!"
            show alexis surprised
            alexis.say "Oh...[hero.name], long time no see!"
            alexis.say "You feeling okay?"
            show alexis talkative
            alexis.say "As I couldn't help seeing you get into that little tussle with my kid-sister..."
            show alexis normal
            mike.say "What...that?"
            mike.say "Oh, don't worry about me - I'll be fine, eventually."
            show alexis talkative
            alexis.say "Well, if you say you're okay..."
            "The atmosphere between us is typically frosty, not helped by the fact she crosses her arms over her chest in a disapproving manner."
            show alexis talkative
            alexis.say "I mean...you know that Kylie's always been a bit...volatile, right?"
            show alexis sadsmile
            "I nod in agreement, recalling my recent encounters with the girl in question."
            show alexis talkative
            alexis.say "She's usually pretty harmless, unless she lets herself get fixated on something."
            alexis.say "Or someone..."
            alexis.say "Anyway, no one knows what makes her tick better than I do."
            alexis.say "So if she causes you any trouble, or you're just worried about her, tell me, yeah?"
            show alexis normal
            mike.say "Thanks for the advice, Alexis - I'll be sure to keep it in mind."
            show alexis talkative
            alexis.say "Yeah, sure...sure."
            show alexis happy
            alexis.say "Good to see you again, by the way..."
            show alexis normal
            mike.say "Good to see you too, Alexis."
            "Only it isn't good to see her, is it?"
            "Alexis looks better than I remember her, with cute, choppy blonde hair and a full, mature figure."
            "All of which I have to force myself to balance against the way that she broke my heart when she betrayed me back in the day."
            "Falling for Alexis all over again is that last thing that I need to happen to me right now."
            "Especially when things are already getting so complicated between me and her younger sister."
            "But, of course, there's always that perennially stupid part of my brain that keeps on marvelling that I was ever with a girl like Alexis at all."
            "And it starts to make me wonder things like if she's changed over the years, and if she's genuinely sorry for what she did to me."
            "Like I already said, it's a stupid part of me."
            "But the worst thing is that I just don't know how to make it shut the hell up..."
            hide alexis
    return

label kylie_event_04:
    $ kylie.flags.target = active_girl.id
    $ kylie.flags.nextevent = TemporaryFlag(True, 3)
    "Try as I might, there's nothing that I can do to get the telephone conversation I had with Kylie out of my head."
    "Every time my mind wanders or I try to relax and think of nothing, there it is again."
    "The sound of Kylie's voice as she touched herself as vivid as it was in my ear that night."
    "It was a real shock, but I can't lie to myself and say that it wasn't a massive turn-on at the same time."
    "It took all of my will-power not to start touching myself too..."
    "But there was just something that held me back, made me hesitate."
    "I'm damned if I know what to call it, but under all the girlish charm, there's something slightly scary about Kylie."
    "I don't know if you could actually call her dangerous, and yet she did have me in the palm her hand right there..."
    "Ah, maybe I'm just being a little paranoid, reading too much into the whole thing."
    "It's just that I've only had Kylie back in my life for a couple of days, and already it's been a pretty intense experience."
    "I almost feel like she has this grand plan for me in mind, and she wants to rush me into it."
    "In all the confusion she's caused me, I'd almost forgotten about [active_girl.name]."
    $ renpy.show(active_girl.id)
    with dissolve
    "And how could I have forgotten about a girl that makes me feel the way she does?!?"
    "In the end, I'm so wound up in thoughts of both girls that I almost wind up walking straight into one of them."
    "[active_girl.name]..."
    "She spots me first, waving enthusiastically to get my attention before hurrying over to begin chatting away."
    "At first, it's a very welcome relief to have someone to talk to, even if it's just to take my mind off of my anxieties."
    "But the feeling doesn't last, and soon I can feel an odd sensation, nagging at the corners of my attention."
    "It makes me feel twitchy, distracted - almost like I'm being watched..."
    "My gaze keeps wandering as we talk, searching for any sign of the unseen watcher."
    "A couple of times the need to keep looking means that I lose track of the conversation."
    "So I have to make awkward apologies for not listening closely enough."
    "This is probably the reason that the conversation wraps up well before I'd have liked it to."
    "And so, as I say goodbye to the girl that I really wanted to talk to, I'm already scanning the surrounding area for the one that I suspect is spying on me."
    $ renpy.hide(active_girl.id)
    $ kylie.yandere += 5
    show kylie angry casual hoodie hoodup at top_mostright, dark
    with dissolve
    "I was right - there she is, watching me from afar, her expression none too pleasant as she does so."
    "Even from here, I can see that her large eyes are fixated on me as I chat to [active_girl.name]."
    "From the expression on her face, you'd think we were breaking some kind of social taboo."
    "And yet all we're doing is having a slightly flirty chat, out in the open and without any attempt to hide it."
    "I'm astonished to see that she's raking her nails down the trunk of a tree, gouging lines of bark as she does so."
    "In fact, her eyes are so wide that I can actually see her pupils, shrinking down to the size of pinpricks."
    "She doesn't move the whole time, I swear that she doesn't as much as blink."
    "I'm pretty sure there's no way she can hear what we're actually saying."
    "Which means that, unless she can lip-read, she's just fixating on us and thinking whatever thoughts are turning over and over in her mind."
    show kylie vangry
    kylie.say "..."
    kylie.say "Why HER?"
    kylie.say "What's so great about HER?!?"
    show kylie angry
    "Kylie shows her teeth, visibly grinding them together."
    "And then she turns to lean against the far side of the tree, breathing heavily as if overcome with emotion."
    hide kylie
    $ renpy.show(active_girl.id)
    with dissolve
    mike.say "Ah...so...I'll see you around - yeah?"
    "[active_girl.name] nods enthusiastically, apparently not noticing my state of unease."
    "I get what would normally be a very pleasant hug and a squeeze before she walks off, blissfully unaware of Kylie's lurking presence."
    $ renpy.hide(active_girl.id)
    with moveoutleft
    "While I'm glad to have had the chance to talk to her, I'm also pretty pissed off at the moment being ruined."
    show kylie angry hoodie hoodup at top_mostright, dark with dissolve
    kylie.say "..."
    "But then my thoughts are interrupted by the sight of Kylie, walking out of the trees and slowly towards me."
    hide kylie
    show kylie angry hoodie hoodup at top_mostright
    with dissolve
    show kylie at right with move
    "At first, I try not to pay her any attention, but she's sidling ever closer and so I have no choice but to acknowledge her presence."
    show kylie y at right4 with move
    "There's only a vague hint of the annoyance that was in her eyes remaining, and as she reaches the spot where I'm standing, it vanishes completely."
    show kylie normal hooddown at center with move
    "By the time she's standing in front of me, her face is the very image of sweet innocence."
    show kylie a happy
    kylie.say "Hey, [hero.name]!"
    show kylie a shout
    kylie.say "And how are YOU doing today?"
    show kylie normal
    mike.say "Erm...hey, Kylie..."
    show kylie at center, zoomAt(1.5, (640, 1040))
    "I almost flinch as she comes even closer, remembering how she's been watching me and the weirdness of the phone call the other night."
    "It's odd, but there's still a part of me that wonders what would have happened if I'd just given in and gone along with it."
    "Infuriating as it is, Kylie just seems to have that effect on me, making me wonder what it would be like to give in to her insanity for a moment..."
    mike.say "I'm okay...I guess, all things considered."
    mike.say "And you?"
    show kylie happy
    kylie.say "Excellent, couldn't be better!"
    show kylie annoyed
    "But as soon as she's spoken those words, her expression becomes strained and she cocks her head on one side."
    show kylie talkative
    kylie.say "But...there is something that's been kinda bugging me a teeny, tiny little bit."
    kylie.say "Don't know if I should mention it though..."
    show kylie annoyed
    "This is one of those moments that you seem to get with Kylie, where she catches you totally off-guard."
    "I want to know what's up, but I'm instantly afraid that it'll open a whole new bag of worms."
    mike.say "What's the matter, Kylie?"
    mike.say "You can tell me, can't you?"
    show kylie talkative
    kylie.say "Oh, [hero.name] - I know that I can tell you anything!"
    show kylie whining
    kylie.say "But...I'm just afraid of what you'll think of me if I tell you this..."
    show kylie annoyed
    "She clasps her hands behind her back, beginning to shift from one foot to the other."
    show kylie talkative
    kylie.say "Oh, dear...I don't know if I should tell..."
    show kylie annoyed
    mike.say "No, no...Kylie, it's okay - you can tell me."
    show kylie talkative
    kylie.say "You want me to be honest, [hero.name]?"
    kylie.say "Is that really what you want?"
    show kylie annoyed
    "I have that unsettling feeling again, the one in the pit of my stomach."
    "This should be a perfectly safe and normal conversation between two sane individuals."
    "Yet with Kylie, it always feels like stepping off a precipice into the unknown."
    show kylie talkative
    kylie.say "I...I saw you talking with [active_girl.name] just before I came over to say hello."
    kylie.say "And, well...I guess it just got me wondering."
    kylie.say "What do you think of her, [hero.name]?"
    show kylie annoyed
    "What do I think of [active_girl.name]?"
    "How do I even begin to answer that - especially when it's Kylie asking the question?"
    menu:
        "She's just a friend":
            "Does what I actually feel for [active_girl.name] even matter as far as the answer to that question is concerned?"
            "Sure, I could be brutally honest and tell Kylie that I have feelings for [active_girl.name]."
            "But it's not like we're engaged or anything, and I have the urge not to hurt Kylie's feelings for no good reason."
            mike.say "She's a friend, you know?"
            mike.say "I like chatting to her now and then."
            show kylie talkative
            kylie.say "So you're saying that you look forward to it?"
            show kylie annoyed
            mike.say "Yeah...I guess so."
            "I had hoped that would settle the matter, but instead she keeps on staring at me with those huge, intense eyes."
            show kylie talkative
            kylie.say "I see."
            kylie.say "Do you like talking to her more than to me?"
            kylie.say "Would you like her to call you like I did the other night?"
            kylie.say "Would you like her to touch herself..."
            show kylie angry
            mike.say "NO...no, it's not like that!"
            "She's doing it again - going from zero to crazy in five seconds flat!"
            mike.say "I...I really liked what you did for me on the phone the other night."
            mike.say "It was just so incredible, and I was so tired..."
            show kylie whining
            kylie.say "Oh...so, I kind of wore you out, huh?"
            kylie.say "I was worried that you hated me for it."
            kylie.say "I thought you were talking to other girls to punish me!"
            show kylie sad
            mike.say "No, Kylie, that's not it at all!"
            "I hate that she makes me do things like this - reassuring her by validating her full-on behaviour towards me."
            "But she seems so desperate and needy at times like this, the last thing that I want to do is be guilty of hurting her."
            "And a large part of me isn't lying - that phone-call was enough to leave me breathless."
            show kylie happy
            kylie.say "Oh, well - that's okay then!"
            show kylie shout
            kylie.say "I'll be seeing you soon, I hope?"
            show kylie normal
            mike.say "Sure...I think we have some classes together."
            show kylie sadhappy
            kylie.say "Hmm...maybe I'll see you sooner."
            kylie.say "Be careful, [hero.name]."
        "I kinda like her":
            $ kylie.yandere += 10
            $ kylie.flags.jealouspath = True
            "I can't possibly string someone as obviously fragile and needy as Kylie along."
            "She deserves to know the truth, no matter how much it might hurt."
            mike.say "Kylie - can I be honest with you?"
            show kylie sadhappy
            kylie.say "Oh, [hero.name] - of course, you can always be brutally honest with me!"
            show kylie sad
            "Even as I wince at her choice of words, I'm already committed to saying what I have to say."
            mike.say "I...I think that I like her."
            mike.say "Actually, I like her quite a lot..."
            show kylie whining
            kylie.say "I...I see..."
            show kylie sad
            "Suddenly, her entire body starts to shake and quiver."
            "She doesn't make a sound, but it's uncomfortable to watch all the same."
            mike.say "Kylie, are...are you okay?"
            show kylie sadhappy
            kylie.say "Oh I'm fine [hero.name] - I'm just fine and dandy!"
            show kylie sad
            mike.say "Erm...I don't think that you are..."
            show kylie sadhappy
            kylie.say "Oh, really - what makes you say that?"
            show kylie sad
            mike.say "Well...you look really upset right now - upset that I find another girl attractive."
            show kylie sadhappy
            kylie.say "Hah...that's ridiculous - why would I even care about a thing like that?"
            kylie.say "No...it doesn't bother me in the slightest - not one little bit..."
            show kylie sad
            "I don't need a sixth sense to know so blatant of a lie when I see one."
            show kylie sadhappy
            kylie.say "I mean really, you guys - how could you think such a thing [hero.name]..."
            show kylie y hoodup annoyed at center, zoomAt(1.5, (340, 1040)) with move
            "Kylie turns her back on me, like she's about to run away."
            "But instead, she just stands there, her shoulders tensing and relaxing."
            "It's as though she's fighting to keep something, under control, to keep it from breaking out."
            "Is it sadness, or rage that she's feeling right now?"
            mike.say "..."
            mike.say "Kylie...hey, talk to me - please?"
            show kylie a talkative
            kylie.say "It's...it's fine...really..."
            show kylie annoyed
            "That's when I happen to look down and notice that she's digging her nails into the flesh of her palms."
            "I've never noticed before now, but her nails are almost ragged, as if she's been using them to scratch at something."
            "Small points of red are beginning to appear where the nails are digging in..."
            mike.say "Kylie, for god's sake - talk to me!"
            show kylie hooddown at center, zoomAt(1.5, (440, 1040)) with hpunch
            "Unable to think of anything else to do, I take her by the elbow and make her turn to face me."
            "I'm afraid that touching her, let alone manhandling her, will set her off."
            "But otherwise, I'm all out of ideas."
            mike.say "I...I'm sorry if I gave you the wrong signals."
            mike.say "I know that I let you give me your number, and then I called you the other night..."
            "I trail off, not wanting to dwell on what happened during that call."
            "All the time, I can't help thinking that I'm just digging the hole I'm already in deeper still."
            show kylie sadhappy
            kylie.say "Who said you gave out any signals?"
            show kylie angry at center, zoomAt(1.5, (640, 1040)) with move
            "Kylie finally lets me turn her around, meeting my eye as soon as I do so."
            show kylie talkative
            kylie.say "I think it's great that you like her."
            kylie.say "I'm happy for the both of you!"
            kylie.say "So, I hope we get to stay friends, huh?"
            kylie.say "That would be so nice..."
            show kylie angry
            "The words are coming out of her mouth, but her face is telling me an entirely different story."
            "Her eyes have a dark cast to them, and her brows are getting pretty intense too."
            "Even a typically clueless guy like me can tell that, underneath it all, she's majorly upset."
            "Her pupils look odd, as if they're really narrow - it's weird, but I can't explain it."
            "She's on the brink of freaking me out for real now!"
            show kylie talkative
            kylie.say "So!"
            kylie.say "You run along and have fun with [active_girl.name]!"
            kylie.say "I'll just go back to..."
            show kylie angry
            mike.say "Kylie, wait - please?"
            "Without as much as another word, she sharply jerks her hand away from mine."
            "Free of my grasp, she hurries away, leaving me alone and staring after her."
    hide kylie with moveoutright
    return

label kylie_event_03:
    if kylie.love.max < 100:
        $ kylie.love.max = 100
    "The note's been burning a hole my pocket since the moment that Kylie pulled it out and handed it to me in the Library the other day."
    "It's just a string of numbers, written in a cutesy manner, but nothing at all out of the ordinary."
    "I've been given a telephone number by a girl in the past - hell, sometimes, when I called them, they even turned out to be genuine."
    "But for some reason, this time it feels different somehow...weird maybe too strong of a word, though it's edging that way for sure."
    "What happened between her older sister and me is water under the bridge, as it was so long ago."
    "I mean, Kylie was nothing but a little kid back then, and she had nothing at all to do with how much Alexis hurt me."
    "Ah, but then she couldn't have been that much of a kid, not based on the confession that she made to me before handing over the note."
    "That was a pretty intense story that she told, of her sneaking to watch Alexis and me having sex one stormy night."
    "If she'd been older at the time, or a guy, it'd be easy to think of her as a voyeur and a pervert."
    "But as far as I know, it was just the one time and she stumbled upon us completely by accident, so that'd be a harsh judgement to make."
    "In fact, what does the story she told me and her kind of intense manner mean, other than that she's a quirky individual?"
    "Why should everyone have to be perfectly normal and appear sane the whole time?"
    "How boring of a world would that be to live in?"
    "No, I think the root of my worry is more likely to be the fact that she's the little sister of my ex, and nothing more than that."
    "It's like Kylie said herself, she's tired of everyone thinking of her as the kid and treating her like a child."
    "I've fallen into the trap of thinking about her that way too."
    "Chances are that, if she weren't Alexis's sister, I'd just see her as eccentric and write that off as nothing to worry about."
    "So while the nagging doubts about Kylie are still there in the back of my mind, I resolve to call her."
    "That way I can show myself that I'm just being paranoid for no good reason."
    "Pulling out the note, I dial the number into my mobile."
    "The whole time I'm thinking that it'll probably just go to voicemail anyway."
    play sound "<from 0 to 2>sd/SFX/phone/phone_calling.ogg"
    "But instead she answers almost as soon as the call goes through and the ringtone has begun."
    kylie.say "Oh, [hero.name]...I'm so glad you finally called me!"
    kylie.say "I've been worrying myself sick that you thought I was some kind of weirdo..."
    "Kylie's voice is instantly excited and eager, but with an odd undertone of barely suppressed tension beneath the surface."
    "What on earth is she talking about?"
    "It's only been a couple of days at the most since we last met up."
    mike.say "What...why would you think that?"
    mike.say "Wait - does this have something to do with the story about you watching Alexis and me?"
    kylie.say "Uh-huh...when you didn't call me that night, I was sure you thought I was some kind of sick pervert!"
    mike.say "Oh...I'm sorry if you got that impression, Kylie."
    if hero.flags.likebeingwatched:
        mike.say "Didn't you remember that I kind of said I thought the whole thing was hot - quite a turn on?"
        "The nervous energy that I could hear in Kylie's voice suddenly dissipates, and she now sounds a lot more sedate, almost sulky in tone."
    kylie.say "But you didn't call and tell me that - did you?"
    kylie.say "I was going round in circles over what I'd said and done."
    kylie.say "I...I was convinced that you hated me..."
    "I can't understand where any of this is coming from, or how I've managed to upset her so badly."
    "Is she really that sensitive, that crazily hung-up on me?"
    mike.say "No, Kylie, it's nothing like that at all, believe me."
    mike.say "I just wanted to leave it a day or two before I called."
    mike.say "Because...because I didn't want you to think that I was too pathetic and needy."
    "What the hell - maybe she'll respond well to flattery?"
    mike.say "You must have so many guys beating down your door."
    mike.say "And all of them must be younger and better looking than me..."
    kylie.say "NO...I mean...no, I really don't!"
    kylie.say "You're the only guy I'm interested in, [hero.name]."
    kylie.say "And that's the truth!"
    mike.say "Okay, okay, Kylie - I do believe you."
    "She goes silent for a moment, and all I can hear is her breathing on the other end of the line."
    mike.say "Kylie, are you still there?"
    mike.say "Are you okay?"
    "She chuckles in a playful manner, instantly reminding me of just how cute and sexy she is in the flesh."
    "Somehow none of the misgivings that I had before seem to matter in the least right now."
    kylie.say "You know, you really should have called me sooner."
    kylie.say "Even if we can't see each other, we can still be intimate over the phone..."
    "Wait a minute - is she telling me that she wants to talk dirty, right here and now?"
    kylie.say "Where are you right now?"
    mike.say "Ah...I guess I was just thinking about getting ready for bed."
    kylie.say "Well, I beat you too it - I'm already under my sheets!"
    kylie.say "And I'm not wearing anything but my little pink panties..."
    "Oh god - her voice is so teasing, so sexy."
    "I get a picture of what she's describing in my mind so vivid that it almost hurts."
    "My breathing must have become heavier too, as Kylie laughs again and begins to tell me more."
    kylie.say "You can picture it, can't you [hero.name]?"
    kylie.say "Don't be ashamed, it's okay...I don't mind that one little bit!"
    kylie.say "In fact, I want you to lie there and fantasise about me - it lets me know just how much you want me..."
    "She begins to sigh in a way so sensuous that I'm almost convinced that she's already touching herself on the other end of the line."
    kylie.say "Do you remember when I told you how I touched myself, while I was watching you fuck my sister?"
    mike.say "Y...y...yes!"
    kylie.say "Well, now I want you to fantasise that I'm touching myself again."
    kylie.say "Only this time, I'm touching myself at the thought of you fucking me instead."
    "What is she doing to me?!?"
    "She's got my cock so hard I could cut glass with the tip, and all she's doing is talking to me!"
    kylie.say "I'm sliding my fingers under the elastic of my panties."
    kylie.say "They're cold, and they feel so good against my pussy."
    kylie.say "You've made it all wet, [hero.name], just the thought of you did that."
    "I don't know if I should tell her to stop or else urge her on."
    "Maybe it's the fact that this feels so wrong that makes me want her to keep going so badly?"
    kylie.say "Ah...I'm slipping them inside of my pussy now, [hero.name]."
    kylie.say "They feel so good."
    kylie.say "But I'm imagining they're your cock, and that makes them so much better..."
    "My hand keeps straying below my waist as her words have the desired effect."
    "I can see everything she described in my mind's eye, every sound suggesting another image of her in a state of desperate arousal."
    "Only when she's actually cumming and the words on the other end of the line are replaced by sensual moans, can I bring myself to hang up."
    "She sounded to be in no condition to continue the conversation, and it would only have been mere moments until there were two of us at it as well."
    "Shaking my head in disbelief, I continue on my way to bed, knowing that whatever happens from here, Kylie has now wormed her way right into my head."
    "And the worst thing is that I really don't think that I want to root her out of there any time soon, either."
    return

label kylie_event_02:
    scene bg university
    "I walk into the university library, looking around as though I've never even seen the inside of the place before now."
    "I have, of course - but I'm not looking for directions, rather I'm looking for someone in particular."
    kylie.say "Hey, [hero.name] - over here!"
    show kylie casual with dissolve
    "My head's not the only one to turn around at the loud call, even though that many people in the room can't be called [hero.name] too."
    "Not that Kylie seems to be at all concerned with the etiquette of keeping the noise down in a library."
    "She practically slams her book down on the table in front of her as I walk over, trying to ignore the harsh stares she's attracting."
    show kylie shout
    kylie.say "I didn't think that you'd come to see me here."
    show kylie happy
    kylie.say "I'm so happy that you did."
    show kylie shout
    kylie.say "I have something that I need to tell you!"
    show kylie normal
    menu:
        "That's what friends are for":
            mike.say "Ah, don't mention it - it's just great to get the chance to catch up with you again."
            mike.say "Plus I thought you might need some help getting to grips with this place."
            mike.say "This place can be pretty intimidating for a new kid."
            show kylie smile
            "Kylie smiles awkwardly and looks down, tracing the spine of the book she was just reading."
            show kylie talkative
            kylie.say "[hero.name]...would you mind not treating me like I'm still a little girl?"
            kylie.say "I'm all grown up now - legally an adult...know what I mean?"
            show kylie shy
            "The fact that she looks up and almost catches me eyeing her cleavage makes her point for me."
            "Far more forcefully than her words ever could have."
        "I could never say no to a pretty face":
            $ kylie.love += 1
            mike.say "To be honest, Kylie - I've been itching to see you again since we met the other day."
            mike.say "I know it sounds lame, but I just can't get over what a beautiful woman you've become."
            "That's a pretty bold compliment, I know."
            show kylie sadhappy
            "And almost instantly I see Kylie's pale cheeks flush red."
            kylie.say "Thank you, [hero.name] - you have no idea how much that means to me."
            kylie.say "I've always wanted to hear someone say that to me."
            kylie.say "Someone just like you..."
            show kylie shy
            "She's staring at me so intently now that it's getting a little uncomfortable."
    mike.say "So, you wanted to talk to me about something?"
    "My attempt to change the subject is so sudden that Kylie almost seems to jump at it."
    show kylie normal at center, zoomAt(1.5, (640, 1040)), vshake
    "Putting her hands flat on the table, she stands up and leans forwards."
    "Kylie narrows her eyes, the thoughtful look on her face making me think that she's weighing up what she's about to say."







    show kylie talkative
    kylie.say "I've been carrying this inside of me for so long..."
    show kylie shy
    "This sounds like it's going to be heavy going - I can already see Kylie's lips quivering as she speaks."
    show kylie talkative
    kylie.say "But, I really want to share it with you."
    kylie.say "Share something that I've been holding onto for years now."
    show kylie normal
    mike.say "Okay, Kylie...what is it that you want to tell me?"
    "Kylie takes in a deep breath and then lets it out in the form of a dramatic sigh, as if preparing herself for what lies ahead."
    show kylie sadhappy
    kylie.say "I like you, [hero.name]."
    show kylie shy
    mike.say "Ah...I like you too, Kylie."
    show kylie talkative
    kylie.say "No...I mean I REALLY like you."
    kylie.say "I've liked you ever since the first moment that I saw you."
    show kylie normal
    mike.say "Erm...is that so?"
    show kylie shout
    kylie.say "Yes...yes it is!"
    kylie.say "In fact, let me share a story with you, one that'll explain everything!"
    show kylie shy
    kylie.say "Once I watched you fuck Alexis while touching myself..."
    show kylie normal
    "Once Kylie's finished her sentence, I find that I'm seriously confused about how it should make me feel."
    "On the one hand, it's pretty creepy to imagine her skulking around in the shadows, watching me having sex."
    "But on the other, I can't deny that it's flattering to know that a girl could see me in that kind of light and hold a torch for all these years afterwards."
    show kylie impressed
    "Either way, after baring her soul like that, Kylie's looking at me with wide-eyed expectation."
    "I'm going to have to tell her something."
    "But the question is what, exactly?"
    mike.say "Okay, Kylie..."
    menu:
        "It's wrong":
            "I don't want to hurt her feelings, but what Kylie just confessed to me is just plain wrong."
            "If she's been going around doing stuff like that for most of her life, then she could be in serious danger."
            "At the very least she could use some kind of therapy."
            mike.say "You have to realise that you can't watch people like that."
            mike.say "It's a violation of their privacy, and it's wrong."
            mike.say "And...it makes me feel uncomfortable knowing you did that to me."
            show kylie angry
            "Instantly there's a dramatic change in Kylie, the expression on her face becoming twisted and hate-filled."
            show kylie vangry
            kylie.say "How fucking DARE you!"
            kylie.say "I tell you that I love you, that I've worshipped you my whole life - and you turn around and reject me!"
            show kylie crazysad
            kylie.say "What kind of a monster are you?!?"
            $ g = Girl.sort(key=lambda x: x.love, reverse=True)[0].name
            kylie.say "What...is it [g] that you're into, huh?"
            kylie.say "What in the hell does that nasty old hag have that I don't?!?"
            show kylie angry
            mike.say "Kylie, please..."
            show kylie vangry
            kylie.say "Don't you 'please Kylie' me!"
            hide kylie
            show kylie casual y angry
            "Kylie scrapes her chair out from under the table and stands up, her hair flicking around as she does so."
            "Hands planted firmly on her hips, she looks down at me with disdain in her eyes."
            show kylie vangry
            kylie.say "I really believed that you were like the guy in that story."
            kylie.say "But maybe I just need to figure this out in my head - so see you later, [hero.name]!"
            hide kylie with moveoutleft
            "With that, Kylie storms out of the library, seemingly intent on making as much noise and creating as big of a scene as possible."
            "I'm starting to wonder if I might have been too harsh on her, failed to see things from any perspective other than my own."
            "She was so young back then, and like most guys, I get super twitchy about the idea of someone that age being in any way sexual."
            "But for now, I really think I need to get out of the library and grab some fresh air."
            return
        "I liked it":
            "A part of me knows that what she's just confessed to me was more than a little wrong and in more than a few ways."
            "But I still can't help getting all hot under the collar at the image of Kylie doing all of that while nobody knew she was even there."
            mike.say "The thought of you being there, doing that to yourself - it's pretty hot."
            show kylie smile
            "Kylie smiles broadly and giggles, fluttering her eyelids in a way that makes me feel even hotter."
            show kylie sadhappy
            kylie.say "You think so?"
            kylie.say "And here I was, afraid that you'd think it was weird and creepy!"
            kylie.say "I mean, wasn't I the little sister?"
            show kylie shy
            "I swallow nervously at this question, wondering why she wants to labour that point."
            "Is she enjoying watching me squirm?"
            mike.say "You're not so little anymore!"
            mike.say "Urgh...I'm sorry, Kylie - you've gotten me in a bit of a mess."
            show kylie happy
            kylie.say "Don't worry about it, [hero.name] - it's kinda flattering that you're all mixed up over me!"
            show kylie shout
            kylie.say "And if you say that you'll take me on a date, then we can work on getting you straightened up nicely."
            show kylie shy
            mike.say "You...you want to go on a date with me?"
            show kylie surprised
            kylie.say "Ooooh, [hero.name] - I thought you'd never ask!"
            show kylie happy
            kylie.say "I accept!"
            $ hero.flags.likebeingwatched = True
    hide kylie
    show kylie casual surprised at center, vshake
    kylie.say "Wait a minute - is that the time?!?"
    kylie.say "I have to get going!"
    show kylie annoyed
    mike.say "What, already?"
    mike.say "I feel like we only just started talking..."
    "Kylie seems to ignore me, standing up and pulling a folded piece of paper out of the pocket of her shirt."
    show kylie smile
    "She pauses just long enough to push it across the table to me and smile."
    show kylie shout
    kylie.say "Be sure to pick somewhere nice for our first date!"
    show kylie smile
    "And with that, she's gone."
    hide kylie with moveoutleft
    "Left alone, I unfold the piece of paper, finding on it a phone number next to a heart with a smiley face inside."
    "Oh shit - I think I just agreed to call my ex-girlfriends little sister up and take her out on a date!"
    return

label kylie_birthday_date_male:
    $ DONE["kylie_birthday_date_male"] = game.days_played
    $ game.active_date.clothes = "casual"
    scene bg livingroom
    "Luckily for me, I remembered that Kylie's birthday was coming up in time to be able to make plans."
    "But rather than try to spring a surprise on her, I decided that the best thing would be to get her in on it too."
    "So I just came right out and asked Kylie if she wanted to celebrate her birthday with me and how."
    "Obviously I was delighted when she jumped at the chance to spend the time with me."
    "But I was more than a little surprised when she told me that she wanted to hang out at my place."
    "I suggested any number of other places that would be more fun, but she was insistent."
    "And so that left me to arrange a night on which my housemates would be out."
    "I wanted to make damn sure that Kylie and I would have the house all to ourselves."
    "Because...well, I think you know the reason!"
    "Now everything's ready for our date night in together."
    "The house is spotless."
    "I have food in the refrigerator."
    "And most importantly of all, my housemates are out of my hair."
    "I'm just making sure everything's perfect for perhaps the hundredth time."
    play sound door_knock
    "And that's when I hear the sound of someone knocking at the door."
    "I take one last glance in the mirror, then I hurry to answer it."
    mike.say "Hi, Kylie..."
    scene bg house
    if not (kylie.flags.killed == 'sasha' or sasha.hidden):
        show sasha casual
        with wiperight
        sasha.say "Sorry, [hero.name]..."
        show sasha joke
        sasha.say "Wrong girl!"
        "I gape at the sight of Sasha where I'd been expecting to see Kylie."
        mike.say "What the hell?!?"
        mike.say "What are you doing back here?"
        mike.say "And where's my date?"
        show sasha annoyed
        "Sasha shrugs and shakes her head."
        sasha.say "I just nipped back because I forgot my keys."
        sasha.say "As soon as I grab them, I'm outta here."
        sasha.say "And as for your date..."
        sasha.say "She's a hefty blonde, right?"
        sasha.say "Kinda dead, staring eyes?"
        "I can't help prickling at Sasha's unflattering description of Kylie."
        mike.say "She has a fuller than average figure, yeah."
        mike.say "But her eyes are intense, that's all!"
        mike.say "Anyway, what's that got to do with anything?"
        sasha.say "I saw a girl like that climbing over the garden fence, just now."
        show sasha normal
        sasha.say "So I thought someone that crazy might be kooky enough to date you!"
        scene bg livingroom
        "I shoot Sasha a hard stare, but then I turn and hurry away."
        "Surely she's just trying to wind me up?"
        "Why would someone climb over the fence, rather than come to the front door?"
        scene bg pool
    show kylie smile casual
    with fade
    if not (kylie.flags.killed == 'sasha' or sasha.hidden):
        "But as soon as I walk out of the house and into the yard, there she is."
    kylie.say "Hi, [hero.name]!"
    kylie.say "I hope I'm not late."
    if not (kylie.flags.killed == 'sasha' or sasha.hidden):
        "Kylie grins at me from where she's sitting on the patio furniture."
        "And from the look on her face, you'd think this was all perfectly normal."
        menu:
            "Tell Kylie off for climbing over the fence":
                mike.say "Don't you use the front door, Kylie?"
                mike.say "You know, like a normal person would?"
                show kylie sad
                "My words seem to catch Kylie off-guard."
                "It's almost like they hurt her feelings."
                "Like she finds the question pretty strange."
                $ game.active_date.score -= 10
                show kylie annoyed
                kylie.say "Why are you talking to me like that, [hero.name]?"
                kylie.say "You were the one that said I could come over here, remember?"
                show kylie angry
                kylie.say "And you never said that I had to use the front door!"
                "I shake my head in disbelief at what I'm hearing."
                "Is she trying to say that it's my fault?"
                "Well, this date's getting off to a strange start!"
                "I just hope it doesn't get any stranger from here."
            "Ignore it":
                mike.say "Oh..."
                mike.say "There you are, Kylie!"
                mike.say "I was expecting you at the front door."
                show kylie sad
                "Kylie looks a little puzzled by this."
                kylie.say "Was I not supposed to climb over the fence?"
                kylie.say "People never tell me these things."
                kylie.say "Then they get mad when don't know things they didn't tell me!"
                "I nod and smile, reminding myself that Kylie's more than a little quirky."
                "I guess she does kind of have a point."
                "And I don't want the date to get off to a bad start."
                "So what's the point in starting an argument over it?"
                mike.say "You know what, Kylie..."
                mike.say "I never thought of it that way!"
                show kylie smile
                $ game.active_date.score += 15
                "Kylie nods and smiles."
                "Like she's happy to have been able to expand my mind."
    "I gesture for Kylie to get up and follow me into the house."
    show kylie normal
    "And much to my relief, she seems happy to do just that."
    scene bg livingroom
    show kylie casual
    with fade
    "Once we're inside, she pauses to look around."
    "And I can see that she's taking in every detail around her."
    mike.say "Erm..."
    mike.say "I take it you like what you see, huh?"
    show kylie smile
    "Kylie hits me with the full effect of her smile in answer to this."
    show kylie normal
    "That combined with the act of looking straight into my eyes."
    "Wow - those things are huge, and SO beautiful!"
    if not (kylie.flags.killed == 'sasha' or sasha.hidden):
        "How could Sasha say such awful things about them?!?"
    show kylie happy
    kylie.say "Oh yeah!"
    kylie.say "Your place looks amazing from the inside, [hero.name]."
    show kylie normal
    kylie.say "Well, aren't you going to give me the grand tour?"
    "I stare at Kylie in silence for a moment."
    "Because I don't think anyone's ever asked me to do that before."
    mike.say "Are you sure, Kylie?"
    mike.say "It's just a normal rental place - nothing special!"
    show kylie smile
    kylie.say "Oh yes - I want to see every inch of it!"
    menu:
        "Agree to give Kylie a tour":
            if hero.charm >= 65:
                "I shrug and nod my head."
                mike.say "Why not, Kylie."
                mike.say "It's not like we're on a strict schedule for tonight."
                mike.say "Come one then..."
                show kylie happy at startle
                $ game.active_date.score += 15
                "Kylie's face lights up as she gets her way."
                show kylie happy at startle
                "She even claps her hands together and jumps up and down on the spot."
                "All of which only serves to make her look hotter than ever!"
                show bg bedroom1
                show kylie normal
                with fade
                "I do try to make the impromptu tour that follows as quick as possible."
                show bg livingroom with fade
                "But wherever we go, Kylie's bizarrely interested in everything she sees."
                show bg kitchen with fade
                "She even keeps asking me about stuff like the kind of locks we have on the doors and windows."
                show bg secondfloor with fade
                "That and how good the burglar alarm is, as well as if we have security cameras too!"
                show bg bathroom with fade
                "I guess she must be really concerned for my safety."
                show bg livingroom with fade
                "Because what other explanation could there be?"
            else:
                show bg bedroom1
                show kylie normal
                with fade
                pause 1.0
                show bg kitchen with fade
                "Kylie does seem to be more than a little interested in the house."
                show bg secondfloor with fade
                pause 1.0
                show bg bathroom with fade
                "Every so often she asks me the oddest questions about it."
                show bg livingroom with fade
                "And in the end, I feel like I have to call her out on it."
                mike.say "Why all the interest in the place, Kylie?"
                mike.say "Is it like your ideal home or something?"
                show kylie annoyed
                "Kylie looks a little surprised by the question."
                "So much so that she shakes her head and laughs."
                show kylie sadhappy at startle
                kylie.say "Oh no, [hero.name] - of course not."
                kylie.say "This isn't my kind of place at all."
                kylie.say "It's way too small and generic."
                kylie.say "And the walls are practically paper-thin too."
                show kylie happy
                kylie.say "No chance of keeping people from hearing what's going on inside."
                menu:
                    "Laugh off Kylie's comments":
                        "Sure, Kylie's comments are more than a little rude."
                        "But that's no reason for me to let it ruin the rest of the night."
                        "So I decide to just laugh it off."
                        mike.say "I know what you mean, Kylie."
                        mike.say "It's not the most aspirational of places, is it?"
                        mike.say "But luckily for me, I'm just renting it for the time being."
                        "Kylie looks surprised to hear my dumping on the place too."
                        "And it seems to make her aware of how insensitive her comments were."
                        show kylie sad
                        kylie.say "No, no, no..."
                        kylie.say "I didn't mean for you to take all of that personally."
                        show kylie normal
                        kylie.say "I just meant it in a practical sense, you know?"
                        mike.say "Whatever you say, Kylie."
                        mike.say "Let's just talk about something else, okay?"
                    "Get offended at Kylie's comments":
                        "I can feel my heckles rising at Kylie's comments."
                        "How dare she take a dump on my home like that?"
                        "It's not my fault this is all I can afford on my salary!"
                        mike.say "Well I'm sorry, Kylie..."
                        mike.say "Maybe you're used to better than this."
                        mike.say "But some of us just have to live within our means!"
                        show kylie sad
                        kylie.say "Oh no!"
                        kylie.say "I didn't mean it like that."
                        mike.say "Too late to take it back now."
                        mike.say "Urgh..."
                        mike.say "Let's change the subject before we really fall out!"
                        $ game.active_date.score -= 10
        "Make up an excuse not to give Kylie a tour":
            "I smile and shake my head."
            mike.say "Sorry, Kylie..."
            mike.say "I haven't allowed for that in tonight's itinerary."
            mike.say "Maybe I'll have time to take you on a quick tour later."
            mike.say "How does that sound?"
            show kylie sad
            $ game.active_date.score -= 10
            "Kylie frowns and makes a huffing sound."
            "Then she begins to pout, which only makes her look hotter than ever!"
            kylie.say "But why not?"
            kylie.say "Isn't it my birthday?"
            kylie.say "And shouldn't you do whatever I want?"
            "I just wave her concerns away."
            mike.say "Like I already said, Kylie..."
            mike.say "Maybe later."
    show kylie normal
    "Even though we're just staying in at my place, I've gone to quite an effort for Kylie."
    "Because, after all, it is her birthday that we're celebrating."
    "And I want it to be as memorable as possible."
    "To that end, I've gone to the trouble of preparing us a meal."
    "And a quick glance at the time lets me know it's almost ready."
    "But the moment I think about going into the kitchen, my bladder makes itself known to me."
    "I know that I'm going to have to go to the bathroom."
    mike.say "Kylie..."
    mike.say "Dinner's almost ready."
    show kylie happy
    kylie.say "Mmm..."
    show kylie smile
    kylie.say "I thought I could smell something nice!"
    mike.say "Yeah..."
    mike.say "But the thing is, I need to go to the bathroom."
    mike.say "So could you nip into the kitchen and turn off the stove?"
    show kylie normal
    "Kylie nods in agreement."
    scene bg bathroom with fade
    "And I take the chance to hurry off to the bathroom."
    "As soon as I'm done and my hands are washed, I head back to the kitchen."
    scene bg kitchen with fade
    "I'm expecting to be greeted by Kylie and the smell of a home-cooked meal."
    "But instead I find the kitchen empty and the smell of burning in the air!"
    "Hurrying over to the stove, I see everything going black and bubbling over."
    "So I do the best I can to save the meal, though I'm already sure it's too late."
    "That done, I go looking for Kylie."
    scene bg livingroom
    show kylie crazyhappy casual
    with fade
    "And I'm more than a little surprised to find her in the hallway."
    "Where she appears to be fiddling with the lock on the front door!"
    show kylie surprised
    mike.say "Kylie!"
    mike.say "What the hell?!?"
    mike.say "Dinner's ruined!"
    mike.say "Where were you?"
    "Kylie spins around at the sound of my voice."
    show kylie sad
    kylie.say "Sorry!"
    show kylie annoyed
    kylie.say "I got distracted looking at the lock on your door."
    "I blink in sheer bewilderment."
    "She actually abandoned dinner to poke around with my front door?"
    menu:
        "Smooth things over with Kylie":
            if randint(0, 1) == 0:
                "I'm about to complain about the meal having being ruined again."
                "But then I remember all of the leftovers that are just sitting in the fridge."
                "I bet I could use those to knock up something just as good as I'd planned."
                mike.say "It's okay, Kylie."
                mike.say "Actually, I'm a bit of a wizard in the kitchen."
                mike.say "So I'll make us something from whatever's in there."
                mike.say "You just wait and see."
                "Kylie follows close on my heels as I walk back into the kitchen."
                "And it seems she's keen to see my culinary skills in action!"
                scene bg kitchen
                show kylie sad casual
                with fade
                if hero.has_skill("cooking"):
                    "As soon as I open the refrigerator, I know exactly what I'm going to make."
                    show kylie normal
                    "And Kylie watches on in apparent fascination as I set to work."
                    "Her amazement only increases as the meal takes shape."
                    "And when I serve up two plates of the stuff, she looks delighted."
                    show kylie smile
                    $ game.active_date.score += 15
                    kylie.say "Mmm!"
                    kylie.say "That looks incredible."
                    kylie.say "And it smells divine too!"
                    mike.say "Ah..."
                    mike.say "It's nothing, Kylie."
                    mike.say "I could do this in my sleep!"
                else:
                    "As soon as I open the refrigerator, I know this isn't going to work."
                    "But I've already sold Kylie on the idea, so I still have to make a show of it."
                    "Pulling out the more promising leftovers, I get right to it."
                    show kylie normal
                    "Kylie looks pretty impressed as I throw everything together."
                    "But once it's done, there's no way to hide how badly I've screwed it up!"
                    mike.say "Erm..."
                    mike.say "Voila!"
                    show kylie angry
                    $ game.active_date.score -= 10
                    kylie.say "Eww!"
                    kylie.say "That looks horrible!"
                    mike.say "Ah..."
                    mike.say "Forget it, Kylie."
                    mike.say "I'll go order us a pizza or something."
            else:
                "I take a deep breath, hold it for a second, and then let it out."
                "The idea was to make tonight special for Kylie."
                "So raging at her isn't going to help, only make things worse."
                mike.say "It's okay, Kylie."
                mike.say "It's not the end of the world."
                mike.say "I'll just order us a pizza or something."
                show kylie sad
                kylie.say "Are you sure, [hero.name]?"
                kylie.say "It sounds like you went to a lot of trouble!"
                mike.say "It was just an accident, Kylie."
                mike.say "I'm sure I'll get the chance to cook for you again soon enough."
                show kylie normal
                $ game.active_date.score += 15
                "This seems to reassure Kylie that I'm not mad with her."
                "And more importantly, it means we can get on with our date."
        "Tell Kylie that you are mad at her":
            mike.say "Do you have any idea how long I spent preparing that meal, Kylie?"
            mike.say "The ingredients weren't cheap either!"
            mike.say "And I did it all because I wanted to make tonight special."
            "Kylie looks away, reluctant to meet my eye while I'm so mad."
            $ game.active_date.score -= 10
            kylie.say "I already said I was sorry."
            show kylie sad
            kylie.say "What more do you want from me?"
            "I'm about to say something else fuelled by my irritation."
            "But then I realise that it won't help, only make things worse."
            "So I bite my tongue."
            mike.say "Ah..."
            mike.say "Forget it, Kylie."
            mike.say "I'll go order us a pizza or something."
    scene bg black with dissolve
    pause 1.5
    scene bg livingroom
    show kylie casual
    with dissolve
    "Kylie seems genuinely satisfied once we've finished eating."
    "She pushes her plate away and gives me a smile."
    show kylie smile
    kylie.say "Oh..."
    kylie.say "I'm so full!"
    kylie.say "I couldn't possibly eat another bite."
    show kylie normal
    kylie.say "So..."
    kylie.say "What next?"
    mike.say "Well, I was thinking we could watch a movie?"
    show fx question
    kylie.say "And what movie are we going to watch, [hero.name]?"
    "I've already put some serious thought into this."
    "And it comes down to a choice between two movies."
    "One's a rom-com, and the other's a psychological thriller."
    hide fx
    menu:
        "Psychological thriller":
            mike.say "How about this one, Kylie?"
            mike.say "'Deadly Magnetism'!"
            "Kylie looks at the image on the cover of the DVD."
            show kylie happy
            "And suddenly her expression becomes one of intense interest."
            kylie.say "Oh..."
            $ game.active_date.score += 15
            kylie.say "That looks interesting!"
            kylie.say "Very romantic, you know?"
            mike.say "Erm, okay..."
            mike.say "If you say so."
            show watch date tv kylie with fade
            "I dim the lights and we sit back to watch the movie."
            "Kylie stays quiet almost the entire way through it."
            "So I keep my mouth shut until the end too."
            mike.say "Well, Kylie..."
            mike.say "What did you think?"
            mike.say "Pretty intense and scary, right?"
            kylie.say "No way, [hero.name]!"
            kylie.say "That was so tragic, the way she loved that guy!"
            mike.say "Did we just watch the same movie?"
            mike.say "She put his kid's Guinea Pigs in the blender!"
            kylie.say "Only because she was forced into it."
            "I shake my head and decide to let the matter drop."
        "Rom-com":
            mike.say "How about this one, Kylie?"
            mike.say "'When Barry Met Annie'!"
            "Kylie looks at the image on the cover of the DVD."
            show kylie sadhappy
            "And her smile suddenly becomes forced."
            kylie.say "Erm..."
            $ game.active_date.score -= 10
            kylie.say "Okay, if you say so..."
            mike.say "Aw come on, Kylie..."
            mike.say "You'll love this one - it's a classic!"
            show watch date tv kylie with fade
            "I dim the lights and we sit back to watch the movie."
            "Kylie stays quiet almost the entire way through it."
            "So I keep my mouth shut until the end too."
            mike.say "Well, Kylie..."
            mike.say "What did you think?"
            mike.say "Pretty great, huh?"
            kylie.say "No way!"
            kylie.say "That was horrible."
            kylie.say "Why did the guy end up with that awful, boring girl?"
            kylie.say "And not the interesting one that was really into him!"
            mike.say "Because that girl was a psycho, Kylie!"
            mike.say "She was like stalking him and stuff!"
            "Kylie frowns and turns away, clearly not convinced."
            "So I decide to cut my losses and change the subject."
    hide watch date tv
    show kylie casual smile at center, zoomAt(1.5, (640, 1040))
    with fade
    "Kylie leans back on the sofa and cocks her head on one side."
    "And it seems that she's giving me a seriously meaningful look too."
    "I can't help returning the gesture from my side of the sofa."
    mike.say "What's the matter, Kylie?"
    mike.say "You look like you want to ask me something."
    mike.say "But you don't know how to actually do it!"
    show kylie normal
    "Kylie looks away for a moment, blushing a little."
    "But then she seems to regain her confidence."
    "Because she looks me in the eye and comes straight out with it."
    kylie.say "Well, what do you think it is, [hero.name]?"
    kylie.say "You asked me here to celebrate my birthday."
    show kylie smile
    kylie.say "So I'm wondering if you got me something nice as a gift?"
    if not hero.has_gifts:
        "Damn it - I knew there was something else I had to remember!"
        "Wait a minute...maybe I can talk my way out of this."
        "There has to be some way I can get myself off the hook."
        mike.say "I already gave you your gift, Kylie."
        mike.say "Our date tonight - that's the gift."
        mike.say "That and all the memories you'll be able to treasure for years to come!"
        show kylie sadhappy
        "Kylie looks more than a little disappointed."
        "But luckily for me, it doesn't look like she's going to argue with me."
        $ game.active_date.score -= 20
        kylie.say "Oh..."
        kylie.say "Of course..."
        show kylie annoyed
        $ kylie.love -= 5
        $ kylie.yandere += 5
        kylie.say "That's so thoughtful of you, [hero.name]!"
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_11
        if _return != "done":
            if _return not in ["None", "exit"]:
                "Luckily for me, I didn't forget to get Kylie a birthday present."
                "And this seems like the perfect moment to whip it out."
                mike.say "Of course I did, Kylie!"
                mike.say "You really think I'd invite you over here if I hadn't?"
                "Kylie looks delighted as I hand over the gift."
                play sound [paper_ripping_1, paper_ripping_2]
                "And she doesn't waste any time in tearing off the wrapping paper."
                if _return:
                    show kylie surprised
                    "But the moment she sees what's inside, she lets out a gasp of amazement."
                    mike.say "What's the matter, Kylie?"
                    mike.say "Is there a problem with the gift?"
                    kylie.say "What?"
                    kylie.say "Oh no, not at all."
                    show kylie happy
                    $ game.active_date.score += 20
                    kylie.say "This is just...amazing!"
                    kylie.say "How did you know?"
                    "I shrug like it's nothing and shake my head."
                    mike.say "Oh, I don't know, Kylie..."
                    mike.say "I guess I just remembered all those hints you've been dropping!"
                    "The truth is that I'm pretty pleased with myself."
                    "And I'm expecting to have scored some serious points with that gift."
                else:
                    show kylie sad
                    "But the moment she sees what's inside, her face falls."
                    mike.say "What's the matter, Kylie?"
                    mike.say "Is there a problem with the gift?"
                    kylie.say "Ah..."
                    show kylie sadhappy
                    $ game.active_date.score -= 10
                    kylie.say "No...no problem."
                    kylie.say "I'm just kind of blown away, that's all!"
                    "It doesn't take a genius to know that Kylie's not telling the truth."
                    "But then I guess she's only trying to spare my feelings for getting her a lame gift."
                    "So I just nod and smile, waiting for this awkward moment to be over."
            else:
                "Damn it - I knew there was something else I had to remember!"
                "Wait a minute...maybe I can talk my way out of this."
                "There has to be some way I can get myself off the hook."
                mike.say "I already gave you your gift, Kylie."
                mike.say "Our date tonight - that's the gift."
                mike.say "That and all the memories you'll be able to treasure for years to come!"
                show kylie sadhappy
                "Kylie looks more than a little disappointed."
                "But luckily for me, it doesn't look like she's going to argue with me."
                $ game.active_date.score -= 20
                kylie.say "Oh..."
                kylie.say "Of course..."
                show kylie annoyed
                $ kylie.love -= 5
                $ kylie.yandere += 5
                kylie.say "That's so thoughtful of you, [hero.name]!"
    "By now it's starting to get pretty late."
    "It's dark outside and we need to have the lights on inside the house."
    "I can't help yawning a little, which seems to amuse Kylie a whole lot."
    show kylie normal
    show fx question
    kylie.say "What's the matter?"
    kylie.say "Am I putting you to sleep?"
    hide fx
    show kylie blush
    kylie.say "Or am I too much for you to keep up with?"
    mike.say "Oooh..."
    mike.say "Sorry, Kylie!"
    mike.say "It's been kind of a long day!"
    "Kylie might be trying to make a joke out of me yawning just now."
    "But the truth of the matter is that I am pretty tired."
    "In fact, I feel like I'm fighting to keep my eyes open!"
    if hero.fitness >= 50 and hero.energy >= 5:
        "It's at times like this I'm glad to be in such good shape."
        "Because it means I can call on an extra reserve of energy."
        "And that's just what I do, pretty much forcing myself to stay awake."
        mike.say "Sorry about that, Kylie."
        mike.say "Now, what were you saying?"
        show kylie smile
        $ game.active_date.score += 15
        "Kylie looks pleased that I'm making an effort to engage her."
        "But all the same she's starting to look a little weary herself."
        show kylie normal
        "She puts a hand to her mouth, trying to stifle a yawn of her own."
        kylie.say "Oh no..."
        kylie.say "Now you've got me started too!"
        mike.say "Hmm..."
        mike.say "Maybe you could do with a coffee?"
        mike.say "I'll just go and put on a fresh pot."
    else:
        "Pretty soon the battle seems to be one I'm losing."
        show layer master at dark
        with dissolve
        "My eyes are closing, and there's nothing I can do about it."
        scene bg livingroom at blur(16), dark, dark with Dissolve(2)
        "But a moment later, I feel myself jolted awake."
        pause 1
        mike.say "Urgh..."
        mike.say "Huh?"
        scene bg livingroom at dark with dissolve
        mike.say "Wha..."
        scene bg livingroom
        show kylie angry casual
        with dissolve
        kylie.say "Wake up!"
        kylie.say "And stay awake this time!"
        kylie.say "You were snoring just now!"
        "I get up, feeling more than a little groggy."
        "And I do the best I can to shake off the feeling."
        mike.say "Maybe it's time for some coffee."
        mike.say "I'm just going to make a fresh pot, okay?"
        $ game.active_date.score -= 10
        kylie.say "Yeah, I think you'd better!"
    hide kylie
    show kylie normal
    with fade
    "I'm getting that instinctive feeling that the date is coming to an end."
    "It's not like there's been some decisive moment or mistake on my part."
    "Just that things have run their natural course."
    "And now would be a good time to wrap it up."
    mike.say "It's getting pretty late, Kylie."
    mike.say "You should be thinking about getting a taxi."
    mike.say "You know, if you want to make it home anytime soon?"
    if kylie.sexperience >= 1:
        "Kylie shakes her head at this."
        kylie.say "What are you talking about, [hero.name]?"
        kylie.say "Tonight isn't over yet."
        show kylie blush
        kylie.say "There's one more thing we have to do before then..."
        "I'm about to ask Kylie what she means."
        show kylie smile at center, zoomAt(1.5, (640, 1040))
        "But then she stands up and takes hold of my hand."
        "She doesn't say a word."
        "But then she doesn't have to."
        "Somehow I know that she's asking me to follow her to my bedroom."
        "And I don't hesitate as she leads me out of the room."
        call kylie_birthday_sex from _call_kylie_birthday_sex
    else:
        "Kylie nods her head as she checks the time for herself."
        show fx exclamation
        kylie.say "Wow, you're right!"
        kylie.say "I'd better be going."
        hide fx
        "She gets up and begins to gather her things."
        "I follow her to the door."
        "All the time waiting to hear her say something positive."
        scene bg house
        show kylie casual
        with fade
        mike.say "So..."
        mike.say "You had a good time tonight?"
        kylie.say "What?"
        show kylie smile
        kylie.say "Oh...oh yeah, it was the best."
        show kylie normal
        kylie.say "Look, I'll call you, okay?"
        "I nod as I let Kylie out of the door."
        scene bg livingroom with fade
        "And once it's closed I wonder why I'm feeling just a little deflated."
        "I mean, she said tonight went great, right?"
        "So what in the hell am I worrying about?"
    return

label kylie_birthday_sex:
    show kylie smile at center, zoomAt(1.5, (640, 1040)) with fade
    pause 1
    show kylie smile at center, zoomAt(1.5, (740, 1040)) with ease
    "It's not like Kylie has to try very hard to get me to follow her."
    show kylie normal
    "She keeps looking back over her shoulder at me, with that smile."
    show kylie at center, zoomAt(1.5, (940, 1040)) with ease
    "The one that always seems to turn me into a helpless mess."
    show kylie happy at startle
    "Then she adds a mischievous giggle too, which is enough to seal the deal."
    hide kylie smile with easeoutright
    "Even though this is my house, I just let Kylie lead me wherever she pleases."
    "The fact is that I'm assuming she's taking me straight to my bedroom."
    scene bg livingroom at blur(16), dark with dissolve
    "And so I don't take my eyes off of her until the door closes behind me."
    "It's only then that I notice there's none of my stuff around me."
    scene bg bedroom2
    show kylie smile casual
    with fade
    "In fact, what I can see looks a hell of a lot like [bree.name]'s stuff instead!"
    "All it takes is a brief glance around to confirm my worst fears."
    mike.say "Kylie..."
    mike.say "What's going on?!?"
    mike.say "This is [bree.name]'s bedroom - not mine!"
    "If I was expecting Kylie to act surprised, I'm instantly disappointed."
    "Because all she does is roll her eyes and walk towards the bed."
    show kylie blush
    kylie.say "Well, duh!"
    kylie.say "Of course it is, silly."
    "As if she just explained everything, Kylie turns her back on me."
    show kylie underwear smile with dissolve
    "Then she starts to take off her clothes."
    "And with some serious speed too!"
    mike.say "But we can't..."
    mike.say "We can't be in here!"
    "Kylie doesn't seem to hear what I'm saying to her."
    show kylie topless with dissolve
    "She just keeps right on going, taking off even more of her clothes."
    mike.say "KYLIE!"
    mike.say "Are you even hearing me right now?!?"
    "I hurry over to where she's pulling off her panties."
    show kylie naked -topless with dissolve
    "And I make it just as she kicks them off and climbs onto [bree.name]'s bed."
    show kylie normal
    kylie.say "Of course I can hear you, [hero.name]!"
    show kylie blush
    kylie.say "I'm just ignoring you, that's all."
    mike.say "You're ignoring me?"
    mike.say "But why?"
    show kylie close normal
    "Kylie chuckles as she kneels on the bed and reaches out for me."
    "And she shakes her head as she begins to undress me too."
    kylie.say "Because that's what you really want, silly!"
    kylie.say "But you're too much of a good guy to admit it."
    mike.say "What are you talking about?"
    show kylie smile
    "Kylie keeps on laughing as she strips me to the waist."
    "And for some reason I just stand there and let her do it."
    "Maybe because I'm so interested in hearing her explanation."
    kylie.say "Oh come on, [hero.name]."
    show kylie normal
    kylie.say "You invited me over here."
    kylie.say "And you made sure your housemates were gone too."
    if kylie.flags.killed == 'bree':
        kylie.say "We both know [bree.name] won't be back."
    else:
        kylie.say "We both know [bree.name] won't be back before we're done."
    kylie.say "You want to fuck me on her bed, [hero.name]."
    show kylie blush
    kylie.say "But you need me to make it happen!"
    "I think about what she's saying."
    "And I'm turning it over in my head."
    "Seriously thinking about it as Kylie starts to take off my pants."
    mike.say "I guess that does make sense, Kylie."
    kylie.say "Of course it does, [hero.name]!"
    show kylie normal
    kylie.say "Because you do, don't you?"
    kylie.say "Want me, that is..."
    kylie.say "You do want me, don't you?"
    show kylie missionary bedroom4 with fade
    "Kylie makes it clear what she means by crawling backwards on the bed."
    "Lowering herself onto the mattress at the same time."
    "Making sure that I can see her body spread out before me."
    "Do I want her?"
    "Right now I can't imagine wanting anything more than I want Kylie!"
    "All thought of this being [bree.name]'s room seems to vanish in a moment."
    "And without another conscious thought, I throw myself onto the bed."
    "How can I describe the sensation of landing atop Kylie?"
    "Look, I'm not comparing it to landing on a mattress or a waterbed."
    "It's far better and more memorable than that."
    "Because none of those things respond by wrapping themselves around you."
    "Kylie gasps in delight as I instantly do the same."
    "Then, with my arms holding her tightly, I roll over."
    show kylie cowgirl lift pleasure bedroom4 with hpunch
    "Caught off-guard, Kylie rolls with me, turning as she tumbles."
    "Now I'm the one lying on my back, and Kylie's perched atop me."
    kylie.say "Oh..."
    kylie.say "Oh my..."
    show kylie cowgirl normal
    kylie.say "Looks like someone changed their mind!"
    "Kylie plants one hand on my shoulder to support herself."
    "And with the other she reaches down between my legs."
    "I gasp as I feel her take hold of my cock with a firm grip."
    "She holds my eye as she begins to stroke up and down the shaft."
    "And I swear that I can actually see the desire rising in her eyes."
    kylie.say "Mmm..."
    kylie.say "I like the feel of this thing."
    kylie.say "I think I'm going to like the feel of it inside me even more!"
    "I'm nodding eagerly by now."
    "More than happy to let Kylie take the lead."
    "All I do is reach up and put both hands on her haunches."
    "As soon as I do that, I feel the urge to hold on as tightly as I can."
    "Kylie feels so solid, so good to have a grip of."
    "It's almost as much of a turn on as her beautiful curves and smiling face."
    "I have no idea if Kylie's aware I'm being turned on my how thicc she is."
    "But she's smiling down at me anyway, holding my eye the whole time."
    "And then I realise what she's actually been doing."
    "That's distracting me, while she angles my cock in just such a way..."
    mike.say "Oooh..."
    mike.say "Whoa..."
    mike.say "Oh god, Kylie!"
    "Kylie lets out a wicked laugh as I feel her pussy rubbing against my cock."
    "But that doesn't mean that she lets up for a second."
    "In fact she seems to double down the moment I react like that."
    "I can feel all of her weight pressing down on me."
    "And at the same time the resistance that's keeping me out is ebbing away."
    show kylie cowgirl vaginal orgasm
    "Then with one final push, Kylie opens like a flower."
    "I take this as my cue to thrust up as she pushes down."
    "And what follows is a moment of sheer, indescribable pleasure."
    "Kylie inches her way down and onto me, her face expressing what she's feeling."
    "I can only think that she's seeing the same thing on my face too."
    "Because it's almost too much for me to take."
    "I can feel my body freezing with the sensations."
    "But luckily for me, Kylie seems to have fared better."
    "I know this because she keeps on going even though I've stopped."
    show kylie cowgirl pleasure
    "Not waiting to ask for an explanation, Kylie begins to ride me hard."
    "Before she was only pushing down, but now she's going up too."
    "It's like she knows just what's happened to me."
    "And now she's going to set about keeping this thing going."
    "All I can do is lie back and watch as Kylie bounces up and down."
    "I can feel her buttocks slapping down on my thighs."
    "And I can see her breasts as they swing above my face."
    "It's overwhelming, almost too much."
    "But then I remember something that I'd forgotten."
    "Something that slipped my mind in the hurry to couple with Kylie."
    "We're not doing this in my bedroom."
    "We're doing it in [bree.name]'s - and on her bed too!"
    "The realisation seems to snap me out of it in mere seconds."
    "I can feel my senses clearing and my body starting to move again."
    "There's no way that I'm going to cut this thing short."
    "But that doesn't mean I can't use all my energy to make it more intense."
    "To make sure the both of us burn out quicker than if I just lay back."
    show kylie cowgirl orgasm
    "Almost as soon as I start to move inside of Kylie again she starts to nod."
    "Luckily for me, she doesn't seem to be aware of my motivation in doing so."
    "Instead she's just understandably delighted at the sensations it produces."
    "It doesn't take too long for the roles to be reversed."
    "Now I'm the one making the headway, while Kylie becomes ever more still."
    "In fact, she's becoming so still that I'm worried she's holding her breath!"
    show kylie cowgirl ahegao
    "But the Kylie lets out a sudden gasp of release that makes me jump."
    "And then I know what's really happening."
    "I can feel the muscles of her pussy squeezing my dick."
    "Her eyes are rolling back into her head."
    "All of which means that she's starting to cum."
    "I feel a sudden rush of relief and a sense of serious achievement."
    "Which seems to be more than enough to push me in the same direction."
    show kylie cowgirl creampie with vpunch
    "I shoot my load into Kylie just a few seconds after her orgasm hits."
    with vpunch
    "Then I strengthen my grip on her as she appears to go limp in my arms."
    show kylie cowgirl orgasm with vpunch
    "Kylie all but collapses onto me, panting with exhaustion."
    "And for the first time tonight I have no trouble taking charge."
    scene bg bedroom2 with fade
    "I gather up our clothes and lead her out of [bree.name]'s bedroom."
    "Stopping to make sure there's no trace of us having been in there, I close the door."
    scene bg bedroom1
    show kylie underwear smile
    with fade
    "And then I usher Kylie back to my own room, relieved to be able to hide her in there."
    "Now that we're safe, we can take all the time we need to recover."
    "And hopefully nobody else will ever know what we just did."
    $ kylie.sexperience += 1
    call sleep ("kylie") from _call_sleep_72
    return

label kylie_propose_male:
    if kylie.flags.schedule == "jail":
        "It's weird that visiting time at the prison's become such a part of my daily routine."
        "When Kylie was convicted and sent down, part of me thought that would be the end of it."
        "But oddly it seems to have had the opposite effect, making the bond between us stronger."
        "Somehow all of the madness and insanity coming out means I've seen Kylie for who she really is."
        "And I've actually found that I'm totally in love with the girl in the middle of it all."
        "Also, it's not like Kylie's turned into a ravening monster now she's behind bars."
        "She actually seems sorry for what she's done, willing to make amends too."
        "And I can't help thinking about what I could have done differently."
        "Like, maybe if I'd been a better boyfriend, if I'd listened to her more."
        "Then maybe I could have spotted the signs and saved her from doing what she did."
        "That's why I'm resolved to do whatever I can for her now."
        "I want to make sure Kylie and I have a future together."
        "I want to prove to her that I'll always be there at her side."
        "So I wait for what feels like the right moment."
        "And then I pull out the ring I've been clutching in my pocket."
        "Then I get down on one knee in front of Kylie's cell door."
        kylie.say "Wh...what's happening?"
        show kylie jail surprised
        kylie.say "[hero.name]..."
        kylie.say "What are you doing?"
        mike.say "I've wanted to do this for a long time, Kylie."
        mike.say "I want tell you that I love you."
        mike.say "That I'll always be there for you."
        mike.say "So...will you marry me?"
        "Kylie looks shocked, like she can't believe what's happening."
        "And that means I genuinely can't read the expression on her face."
        "But luckily for me, it doesn't take long for her to recover."
        if kylie.love < 195:
            "Kylie shakes her head and begins to back away from me."
            "And she doesn't stop until she's literally backed up to the far wall."
            show kylie sad
            "This leaves me clinging to the bars of the cell door, shaking my head too."
            mike.say "Kylie!"
            mike.say "What's wrong?"
            mike.say "Am I going too fast for you?"
            mike.say "Because you don't have to say yes or no right now."
            mike.say "If you want to take your time, I can wait for an answer."
            kylie.say "No, no, no!"
            kylie.say "You can't ask me to do that, [hero.name]!"
            show kylie angry
            kylie.say "I have to be punished - don't you understand?!?"
            mike.say "What are you talking about, Kylie?"
            mike.say "You're in jail for what happened."
            mike.say "Isn't that your punishment?"
            mike.say "I want us to start planning our life together!"
            show kylie sad
            kylie.say "No, that can't happen!"
            kylie.say "I tried to make it work, [hero.name]."
            kylie.say "But it all ended in disaster."
            kylie.say "We can't save something that's been ruined."
            "I open my mouth to argue, to plead with Kylie."
            "But she cuts me off, shouting and looking past me."
            kylie.say "GUARD...GUARD!"
            show kylie normal
            kylie.say "I want to be alone now!"
            kylie.say "I want him to leave!"
            "I stand up and put the ring away as the guards come in."
            "And I don't protest when they kindly but firmly ask me to leave."
            scene bg policestation with fade
            "My head's spinning from what just happened."
            "What I need is time to get my thoughts straight."
            "And the inside of a prison isn't the place to do that."
            $ kylie.love -= 25
            $ kylie.sub -= 25
        else:
            "Kylie nods her head eagerly, holding out her hand."
            "And I don't hesitate to take the chance."
            "I slide the ring onto her finger without hesitation."
            kylie.say "Oh, [hero.name]!"
            show kylie happy
            kylie.say "I thought you'd never ask me to marry you."
            kylie.say "Not after everything that I've done."
            show kylie smile
            "As Kylie's nodding her head, I'm shaking mine."
            mike.say "God no, Kylie!"
            mike.say "All that stuff..."
            mike.say "It just made me realise how much I love you."
            mike.say "It made me want to try all the harder to be with you."
            mike.say "I want to build a life for the both of us."
            "I'm not prepared for what happens next."
            "Kylie reaches through the bars and grabs me with both hands."
            with hpunch
            "She pulls me bodily against the cell door, almost knocking the wind out of me."
            hide kylie
            show kylie kiss jail
            with fade
            $ kylie.flags.kiss += 1
            "But I hardly have time to grunt in pain before she clamps her lips onto mine."
            "I'm pretty sure that we shouldn't be doing this right now."
            "But I can't bring myself to pull away from her."
            "Instead I return the kiss with what I hope is a similar level of passion."
            "A moment later I hear the door opening behind me."
            "I know that it's one of the guards, coming in to break it up."
            "So I pull back and break off the kiss."
            hide kylie kiss
            show kylie jail happy
            with fade
            "There's just enough time to say goodbye to Kylie."
            "And then I'm ushered out of the door and away."
            "My head's spinning from what just happened."
            "What I need is time to get my thoughts straight."
            "But visiting time will come round again soon enough."
            "And then Kylie and I can really start planning where we go from here."
            $ kylie.set_fiance()
    else:
        show kylie
        "I've been thinking about this for a long time, weighing up the pros and cons of popping the question to Kylie."
        "On the one hand, she's probably the hottest girl that I've ever dated, hands down."
        "And she's super into me too, almost crazily infatuated - which is never a bad thing, right?"
        "But there is the fact that means she can be super intense too, the other side of that same coin."
        "I mean, Kylie's pretty much jealous of every other girl in my life, whether they're into me or not!"
        "But let's cut to the chase here and admit the truth - those cons don't really matter, do they?"
        "Kylie can be jealous all she wants, because I'm not interested in any other girls."
        "And once she's got a ring on her finger, that should make her calm down on that front too."
        "Surely this is what Kylie wants, for me to make a commitment to her?"
        "So I arrange to get my hands on a ring, and then I wait for the right moment."
        "I'm sure I'm doing the right thing."
        "So what could possibly go wrong?"
        show kylie happy
        "Kylie seems totally unaware of what I'm planning."
        "She's happily talking about something that I'm not paying attention to."
        "Because the only thing on my mind right now is getting down on one knee to pop the question."
        "Kylie walks a step and a half ahead of me before she realises I'm not at her side anymore."
        show kylie annoyed
        "Then she turns around, a confused look on her face as she searches for where I've gone."
        kylie.say "[hero.name]..."
        kylie.say "Where did you go?"
        "It doesn't take more than a few seconds for Kylie to spot me."
        show kylie surprised
        "And when she does, her eyes go wide with genuine surprise."
        kylie.say "Wh...what are you doing?"
        kylie.say "Why are you down there?"
        "I put a smile on my face that I hope reflects my genuine feelings."
        "And then I hold up the ring so that Kylie can't fail to see it."
        mike.say "Kylie..."
        mike.say "Will you marry me?"
        show kylie normal
        "As I watch her reaction, Kylie takes in a deep breath."
        "In fact, she seems to be taking it in for a very long time."
        "I'm actually worried that she might be about to explode!"
        if kylie.love < 195:
            "I'm almost convinced that Kylie's about to say yes."
            "That she's going to let it all out in one huge burst."
            show kylie sad
            "But then I see the look on her face change."
            "And she lets the huge breath out in a long sigh."
            "Kylie seems to deflate as she does this too."
            "She shakes her head slowly, showing sadness and disappointment."
            kylie.say "Oh, [hero.name]..."
            kylie.say "I want to say yes, really I do!"
            kylie.say "But you're just not ready for that kind of commitment!"
            "I frown as I try to digest Kylie's words."
            "At first I thought she said that she wasn't ready to commit."
            "But then it dawns on me that she actually said I wasn't ready for that!"
            mike.say "Erm..."
            mike.say "Kylie..."
            mike.say "What do you mean that I'm not ready?"
            mike.say "I'm kind of the one going down on one knee here!"
            show kylie smile
            "Kylie shakes her head and laughs in a dismissive manner."
            "All of which makes it seem like I'm an idiot for not understanding her."
            show kylie normal
            kylie.say "Don't worry about it, [hero.name]."
            kylie.say "It's not your fault."
            kylie.say "There are just some thing about your life."
            kylie.say "Somethings that I need to...take care of first."
            "I frown, still not rally getting what Kylie means."
            "But the look on her face reassures me it'll be okay."
            "After all, didn't she just say she'll be ready to commit soon?"
            "All I have to do is sit back and wait for that time to come."
            "So I nod happily, slipping the ring away as I get to my feet."
            "And part of me is wondering what Kylie has in store for me too!"
            $ kylie.love -= 25
            $ kylie.sub -= 25
        else:
            show kylie happy
            "Kylie lets it all out in one huge burst."
            "All at once she's quaking with emotion."
            show kylie normal
            "Her eyes are filling up with tears."
            "And she's nodding her head like crazy."
            kylie.say "Yes, yes, yes!"
            kylie.say "Of course I will, [hero.name]!"
            kylie.say "This is just how I saw it happening!"
            show kylie smile
            kylie.say "I just knew it would turn out this way!"
            "I'm too thrilled at the fact Kylie said yes to think of anything else."
            "Sure, some of what she's saying sounds a little weird."
            "But I just put it down to the emotions she's feeling."
            "They're probably making her babble on without thinking."
            "I don't waste any time in pushing the ring onto Kylie's finger."
            "And then I climb to my feet as she studies it intently."
            kylie.say "Oh, this is just perfect."
            kylie.say "Everything's falling into place."
            kylie.say "Now all I need to do is tie up some loose ends..."
            mike.say "Huh?!?"
            mike.say "What do you mean by that?"
            show kylie normal
            "Kylie looks surprised at the question."
            "But it only takes a moment for her to recover."
            "Then she smiles as she explains herself to me."
            show kylie happy
            kylie.say "Oh, nothing you need to worry about!"
            kylie.say "Just some little matters to deal with before the big day, that's all."
            kylie.say "I need everything to be perfect if we're going to spend the rest of our lives together!"
            "That sounds good to me, so I don't press the matter further."
            "I just nod and smile, letting Kylie know it's settled."
            "She plants a kiss on my lips and all seems well."
            $ kylie.set_fiance()
        hide kylie
    return

label kylie_male_ending:







    if renpy.has_label("kylie_achievement_5") and not game.flags.cheat:
        call kylie_achievement_5 from _call_kylie_achievement_5
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding with fade
    "There were so many times when I thought this day would never come."
    "And now that I'm finally standing at the altar, it feels surreal."
    "Yeah, I know that everyone has insane nerves on their wedding day."
    "But after all that Kylie and I have been through together..."
    "Well, I feel like we've endured far more than most couples."
    "I know that the chapel is pretty much full right now."
    "Yet I haven't looked at a single face amongst the guests."
    "Even the priest standing in front of me doesn't seem real."
    "All of that is because I'm only looking out for one person."
    "And the moment that I hear the sound of music begin to play, I see her!"
    show kylie wedding with dissolve
    "Kylie sweeps into the chapel, and I only have eyes for her."
    "She insisted on not letting me see her in the dress before the wedding."
    "And I'm glad that she did - because she's nothing short of a vision in blue!"
    "As she walks down the aisle towards me, Kylie takes my breath away."
    "Somehow her dress manages to make her look every inch the perfect bride."
    "But I can see the way it shows off her magnificent figure too."
    "And her face...well...what can I say about that?"
    "She looks like an angel, the most beautiful girl in the world!"
    "I mean, she was always pretty, sure."
    "But since she really came to grips with her demons, something changed."
    "Back then there was always a manic glimmer in her eye, a twitch of the jaw."
    "Now all of that energy is channelled elsewhere."
    "And Kylie's true beauty just shines out of her like a beacon!"
    "Ah shit...I'm sorry."
    "I'm starting to babble - but I'm just so happy!"
    show wedding kylie with fade
    "Kylie reaches the altar and takes her place at my side."
    "She looks at me with those eyes, smiling sweetly."
    "Once she had a scary possessiveness in them, almost a madness."
    "But now that's been transmuted into a look of love."
    "A love that I share."
    "Priest" "Ahem..."
    show wedding kylie priest with dissolve
    "Almost as one, the entire chapel comes to attention."
    "And when that happens, the priest smiles happily."
    "Priest" "Friends, we are gathered here today."
    "Priest" "To witness the union of these two people in holy matrimony."
    "You don't need me to tell you the rest, right?"
    "You've seen a wedding before now."
    "So I'll just jump ahead to the good bits."
    "Priest" "If anyone here knows of any lawful reason these two may not be joined..."
    "Priest" "Let them speak now, or forever hold their peace!"
    "There's the usual moment of silence and quiet chuckles."
    "Then Kylie speaks up herself."
    kylie.say "Don't worry about it."
    kylie.say "I already killed them all off!"
    "At first everyone seems startled, like they don't know how to react."
    "But then I begin to laugh, and slowly, the rest of the guests follow."
    "I know Kylie made the joke mostly for my benefit."
    "Making fun of herself and the jealousy that she used to struggle with."
    "And knowing that just makes me love her all the more."
    "Priest" "So, do you, [hero.name], take Kylie to be your lawful, wedded wife?"
    mike.say "I do."
    "Priest" "And do you, Kylie, take [hero.name] to be your lawful, wedded husband?"
    kylie.say "Oh, yes I do!"
    "Priest" "Very good."
    "Priest" "Therefore it is with great pleasure that I pronounce you husband and wife."
    "Priest" "You may kiss, if you like?"
    show wedding kylie -priest with dissolve
    "It's not like we need to be told!"
    scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
    show kylie kiss wedding
    $ kylie.flags.kiss += 1
    "Kylie almost throws herself into my arms, and I clutch her tightly."
    "The kiss is wonderful, but what's better is the sensation of holding her in my arms."
    "That and the knowledge that I get to do it for the rest of my life too!"
    scene kylie ending
    with fade
    kylie.say "Oh...this is going to be hard!"
    kylie.say "I wish [hero.name] was here to help me through it!"
    kylie.say "Now, come on, Kylie - you can do it, you know you can!"
    kylie.say "I'm sorry, you guys - I guess I'm just scared what you all think of me."
    kylie.say "I'm 'Kylie the Psycho'...the crazy girl that wanted [hero.name] all to herself!"
    kylie.say "But that's not me anymore, you see?"
    kylie.say "I admit that I had a problem...a really BAD problem."
    kylie.say "And if it weren't for [hero.name], I don't know what I'd have done."
    kylie.say "But you have to understand that I didn't know I was doing anything wrong."
    kylie.say "I didn't know that I even had a problem until he showed me that I did!"
    kylie.say "You see I was always in love with [hero.name], right from the start."
    kylie.say "I fell in love with him the very moment that I saw him with Alexis."
    kylie.say "And...well...that was where the problems started."
    kylie.say "I wanted him so much, knew that he was supposed to be with me."
    kylie.say "All I could think was that my sister was getting in the way."
    kylie.say "Our parents had always told us that we should share things."
    kylie.say "That we should make sure that the other had what we needed."
    kylie.say "And I knew that what I needed was [hero.name]!"
    kylie.say "I...I suppose I was too young to understand."
    kylie.say "Too young to know how complicated human feelings really were."
    kylie.say "All I knew was that Alexis had something I wanted so badly."
    kylie.say "And she didn't seem to want to share it with me!"
    kylie.say "So I promised myself that not only would he be mine one day."
    kylie.say "But also that I'd never share him with anyone else either!"
    kylie.say "It wasn't too hard to get his attention when I met him again."
    kylie.say "So much time had passed that he'd all but forgotten awkward little Kylie."
    kylie.say "I wasn't his girlfriend's annoying, bratty younger sister anymore."
    kylie.say "I did pretty well when it comes to looks and all that."
    kylie.say "And I knew what guys wanted in a girl too."
    kylie.say "So getting him to notice me was the easiest part."
    kylie.say "Looking back now it just seems so stupid, all the games I was playing."
    kylie.say "I wanted [hero.name] so desperately, I wanted him all to myself."
    kylie.say "It never occurred to me that I could have kept him just by being myself."
    kylie.say "There were always so many other girls around, and I saw them all as rivals."
    kylie.say "I wanted him that badly, so I figured that they must have wanted him too!"
    kylie.say "That seems crazy now - I mean, he's a catch, sure."
    kylie.say "But I'm pretty sure he's not the most desirable man on the planet!"
    kylie.say "Oops...is...is he going to hear this?"
    kylie.say "If he is...tell him that I'm sorry and I didn't mean it, yeah?"
    kylie.say "Tell him he really is the sexiest man who ever lived!"
    kylie.say "Anyway...where was I..."
    kylie.say "Oh yeah...I came close to going over the edge, to doing something crazy."
    kylie.say "But [hero.name] didn't reject me, didn't call me a crazy bitch."
    kylie.say "He was worried about me, wanted to make sure I was okay."
    kylie.say "And that's when I started to realise what true love actually is."
    kylie.say "It's caring for another person more than you care about yourself."
    kylie.say "[hero.name] loved me before I did something that insane."
    kylie.say "So how could doing it make him love me more?"
    kylie.say "It was that realisation that changed things, that showed me it was all pointless."
    kylie.say "I needed to stop trying to ensure he loved me, and just let him love me!"
    kylie.say "When you compare it to that, all of the rest seems to be easy!"
    kylie.say "We got married and we moved in together."
    kylie.say "All the things that you're supposed to do when you love someone."
    if kylie.flags.mikeBabies > 0 or kylie.is_visibly_pregnant:
        kylie.say "We even started a family of our own!"
        kylie.say "Our daughter's strong and beautiful."
        kylie.say "I decided to call her Alexis, as a gesture to my sister."
    else:
        kylie.say "Who knows, we may even start a family together."
        kylie.say "And if we have a girl, I want to call her Alexis."
        kylie.say "As a gesture of peace to my sister."
    kylie.say "And that's because Alexis didn't take things working out for us that well."
    kylie.say "In fact, she kind of went off the rails when she heard the news we were married."
    kylie.say "She spent some time in and out of psychiatric institutions."
    kylie.say "But the prognosis isn't good, and we're worried about her."
    kylie.say "Maybe it's not too late for her though."
    kylie.say "Maybe she'll find someone to save her, like [hero.name] saved me?"
    kylie.say "But anyway, enough with the depressing stuff already."
    kylie.say "What really matters is that [hero.name] and I are together."
    kylie.say "And we couldn't be happier than we are right now."
    kylie.say "It turned out almost like a fairy tale in the end."
    kylie.say "Well...there were a few twists and turns along the way."
    kylie.say "But we got there in the end!"

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not kylie.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_12
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_12
    $ game.set_new_game_plus()
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
