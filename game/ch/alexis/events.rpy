


















init python:
    Event(**{
    "name": "alexis_start",
    "label": "alexis_start",
    "conditions": [
        IsDone("alexis_event_01"),
        HeroTarget(IsFlag("alexisstart")),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "alexis_event_02",
    "label": "alexis_event_02",
    "conditions": [
        IsDone("alexis_start"),
        IsDayOfWeek(5, 6, 7),
        IsHour(14, 15),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            MinStat("money", 500),
            IsActivity("None")
            ),
        PersonTarget(alexis,
            Not(IsPresent()),
            Not(IsHidden()),
            MinStat("love", 20),
            ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "alexis_event_03",
    "label": "alexis_event_03",
    "conditions": [
        IsDone("alexis_event_02"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_mall1"),
            ),
        PersonTarget(alexis,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 40),
            ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "alexis_event_04",
    "label": "alexis_event_04",
    "conditions": [
        IsDone("alexis_event_03"),
        HeroTarget(
            IsGender("male"),
            IsActivity("date_watch_a_movie"),
            IsRoom("date_cinemaroom"),
            ),
        PersonTarget(alexis,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 60),
            ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "alexis_event_05",
    "label": "alexis_event_05",
    "conditions": [
        IsDone("alexis_event_04"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_beach", "date_nudistbeach")),
        PersonTarget(alexis,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 80),
            ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "alexis_event_06",
    "label": "alexis_event_06",
    "conditions": [
        IsDone("alexis_event_05", "alexis_ntr_conversation"),
        HeroTarget(IsGender("male")),
        PersonTarget(alexis,
            IsActive(),
            MinStat("love", 100),
            ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "alexis_event_07a",
    "label": "alexis_event_07a",
    "conditions": [
        IsDone("alexis_event_06"),
        IsHour(8, 20),
        HeroTarget(
            Not(OnDate()),
            ),
        PersonTarget(alexis,
            Not(IsHidden()),
            IsFlag("hired_PI"),
            IsFlag("PIDelay", False),
            ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    "do_once": True,
    })

    Activity(**{
    "name": "alexis_event_07b",
    "display_name": "Report the rape",
    "label": "alexis_event_07b",
    "duration": 2,
    "rooms": "policestation",
    "conditions": [
        IsHour(9, 19),
        PersonTarget(alexis,
            Not(IsHidden()),
            IsFlag("policestation"),
            ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    "do_once": True,
    "icon": "alexis",
    })

    Activity(**{
    "name": "alexis_event_08a",
    "display_name": "Go talk to the coach",
    "label": "alexis_event_08a",
    "icon": "alexis",
    "duration": 1,
    "conditions": [
        IsDone("alexis_event_07a"),
        IsHour(8, 18),
        HasVehicle(),
        HeroTarget(
            Or(
                IsRoom("house"),
                HasRoomTag("street"),
            ),
            Not(OnDate()),
            IsActivity("None"),
            ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "alexis_event_08b",
    "label": "alexis_event_08b",
    "conditions": [
        IsDone("alexis_event_07b"),
        HeroTarget(IsRoom("date_livingroom")),
        PersonTarget(alexis,
            OnDate(),
            ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "alexis_event_09a",
    "display_name": "Tell her about the coach",
    "label": "alexis_event_09a",
    "duration": 0,
    "icon": "button_alexis",
    "conditions": [
        IsDone("alexis_event_08a"),
        HeroTarget(
            Or(
                IsRoom("date_pub"),
                HasRoomTag("pub"),
                ),
            ),
        PersonTarget(alexis,
                IsActive(),
                ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "alexis_event_10",
    "label": "alexis_event_10",
    "priority": 500,
    "duration": 1,
    "conditions": [
        Or(
           IsDone("alexis_event_08b"),
           IsDone("alexis_event_09a"),
           ),
        IsNotDone("alexis_event_11"),
        IsDayOfWeek("123457"),
        PersonTarget(alexis,
            IsActive(),
            MinStat("love", 160),
            ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    })

    Event(**{
    "name": "alexis_event_12",
    "label": "alexis_event_12",
    "conditions": [
        IsDone("alexis_event_11"),
        PersonTarget(alexis,
            IsActive(),
            MinStat("love", 180),
            ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "alexis_event_ntr_01",
    "label": "alexis_event_ntr_01",
    "conditions": [
        IsDone("alexis_event_05"),
        IsDayOfWeek(6, 7),
        IsHour(14, 18),
        HeroTarget(IsRoom("date_livingroom")),
        PersonTarget(alexis,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("story", 1, 3),
            MinStat("love", 100),
            ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "alexis_event_ntr_02",
    "label": "alexis_event_ntr_02",
    "duration": 1,
    "conditions": [
        IsDone("alexis_event_ntr_01"),
        HeroTarget(IsRoom("sexshop")),
        PersonTarget(alexis,
            Not(IsHidden()),
            IsFlag("story", 1, 3),
            MinStat("love", 130),
            MinStat("sexperience", 5),
            ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    "do_once": True,
    })

    Activity(**{
    "name": "ceo_office_spy_camera",
    "display_name": "Place spy camera in Dwayne's office",
    "rooms": "mcoffice",
    "conditions": [
        IsDone("alexis_event_ntr_02"),
        HeroTarget(
            HasRoomTag("mcoffice"),
            Not(IsFlag("dwaynedead"),),
            ),
        InInventory("spy_camera"),
        ],
    "label": "ceo_office_spy_camera",
    "icon": "spycamera",
    "do_once": True,
    })

    Event(**{
    "name": "alexis_event_ntr_03",
    "label": "alexis_event_ntr_03",
    "duration": 1,
    "conditions": [
        IsDone("ceo_office_spy_camera"),
        HeroTarget(HasRoomTag("mcoffice"),
                   IsFlag("ceoofficecameraplaced"),
                   Not(IsFlag("dwaynedead")),
                   ),
        PersonTarget(alexis,
            Not(IsHidden()),
            IsFlag("story", 1, 3),
            MinStat("love", 150),
            ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "alexis_event_ntr_04",
    "label": "alexis_event_ntr_04",
    "duration": 1,
    "conditions": [
        IsDone("alexis_event_ntr_03"),
        HeroTarget(IsGender("male"),
                   IsRoom("date_restaurant"),
                   Not(IsFlag("alexis_dwayne_encounter")),
                   ),
        PersonTarget(alexis,
            OnDate(),
            MinStat("love", 170),
            IsFlag("story", 1, 3),
            Or(
                IsFlag("sexydate"),
                IsFlag("sluttydate"),
                ),
            ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "alexis_event_ntr_05_intro",
    "label": "alexis_event_ntr_05_intro",
    "duration": 1,
    "conditions": [
        IsDone("alexis_event_ntr_04"),
        HeroTarget(IsGender("male"),
                   ),
        PersonTarget(alexis,
            IsActive(),
            IsFlag("ntr_delay", False),
            MinStat("love", 180),
            ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "alexis_event_ntr_05_restaurant",
    "label": "alexis_event_ntr_05_restaurant",
    "duration": 1,
    "conditions": [
        IsDone("alexis_event_ntr_05_intro"),
        HeroTarget(IsGender("male"),
                   IsRoom("date_restaurant"),
                   ),
        PersonTarget(alexis,
            OnDate(),
            IsFlag("story", 1, 3),
            Or(
                IsFlag("sexydate"),
                IsFlag("sluttydate"),
                ),
            IsFlag("ntr_05", "restaurant"),
            ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "alexis_event_ntr_05_home",
    "label": "alexis_event_ntr_05_home",
    "duration": 1,
    "conditions": [
        IsDone("alexis_event_ntr_05_intro"),
        IsTimeOfDay("afternoon", "evening"),
        "not Room.find('livingroom').get_present_girls_by_tag()",
        HeroTarget(IsGender("male"),
                   HasRoomTag("home"),
                   ),
        PersonTarget(alexis,
            Not(IsHidden()),
            IsFlag("ntr_05", "home"),
            ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    "do_once": True,
    })


    SpecificTalkSubject(**{
    "name": "alexis_ntr_conversation",
    "display_name": "About her behavior",
    "label": "alexis_ntr_conversation",
    "duration": 0,
    "icon": "button_alexis",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(alexis,
            IsActive(),
            IsFlag("conversation_event", "restaurant", "beach", "cinema"),
            ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "alexis_kiss_me",
    "label": "alexis_kiss_me",
    "max_girls": 1,
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(alexis,
            IsPresent(),
            Not(IsHidden()),
            MinFlag("kiss", 1),
            MinStat("love", 150),
            ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    "chances": 20,
    "once_day": True,
    "do_once": False,
    "quit": False,
    })

    Event(**{
    "name": "alexis_preg_talk",
    "label": "alexis_preg_talk",
    "do_once": False,
    "conditions": [
        HeroTarget(
            IsActivity("None"),
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(alexis,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("pregstory", 0),
            MinCounter("pregnant", 6),
            ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    })

    Event(**{
    "name": "alexis_blackmail_dwayne",
    "label": "alexis_blackmail_dwayne",
    "duration": 1,
    "conditions": [
        IsDone("alexis_event_ntr_03"),
        HeroTarget(HasRoomTag("work"),
                   Not(IsFlag("dwaynedead")),
                   IsFlag("alexisfootage", "blackmail"),
                   Not(IsFlag("alexis_dwayne_encounter")),
                   ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "alexis_rape_talk",
    "label": "alexis_rape_talk",
    "conditions": [
        IsDone("kylie_investigation_3"),
        PersonTarget(alexis,
            IsActive(),
            ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    "do_once": True,
    })

label alexis_start:
    $ alexis.unhide()
    return

label alexis_event_02:






    $ renpy.play("sd/cell_vibrate.ogg", "sound")
    $ result = renpy.call_screen("smartphone_choice")
    if not result:
        $ hero.cancel_event()
        return
    if alexis.love.max < 40:
        $ alexis.love.max = 40
    "I'm pretty much on autopilot when my phone rings, trying to manage two different tasks while remembering a couple of others that I have to take care of as soon as I've got these ones done."
    "So when I pull out my phone and see that the call is from an unknown number, I instantly make to reject it and get back to what I'm already struggling to get done."
    "But then, for some reason, I pause and decide to accept the call anyway."
    "I really can't explain what makes me do it, just one of those quirky feelings you get every so often to do something you'd normally pass over."
    mike.say "Hello?"
    "There's silence for a couple of seconds, and all that keeps me from hanging up is the sound of someone breathing on the other end."
    alexis.say "Hey, [hero.name], it's me - Alexis!"
    mike.say "Alexis...wow...erm, I was not expecting to get a call from you today!"
    "I can hear her make a little sound that could be laughter, or equally be a sly note of satisfaction."
    alexis.say "Well, surprise!"
    alexis.say "And I hope it was a good one?"
    "I'm genuinely too wrong-footed to be able to come up with anything clever to say."
    alexis.say "So, are you ready for our night out?"
    "I see my last chance to say no and get as far away as possible fading into the distance."
    mike.say "Okay, Alexis - I guess that'd be...nice."
    alexis.say "Let's meet tonight, at the restaurant."
    alexis.say "Okay - that's a date!"
    alexis.say "I'll text you the address and see you there, [hero.name]!"
    "And just like that she's back in my life and back taking control of it!"
    "And yes, I know that I just agreed to meet up with her for dinner, like a complete pussy!"
    "But it's not a date, I keep telling myself."
    "It's just two former acquaintances meeting up to compare notes and talk about old times."
    "And maybe if I keep on telling myself that for long enough, I might actually believe it too!"
    scene bg black with timelaps
    $ game.pass_time(6)
    scene bg restaurant with fade
    "If I was nervous to be walking into the restaurant expecting to see Alexis waiting for me, then imagine how much it made me panic to find that she was nowhere to be seen."
    "I check my watch and glance around in the hope of spotting her, but it's no good, she's not hiding behind any of the potted plants or pillars dotted around the place."
    "At a loss for what else to do, I wander over to where the maitre d' is standing, trying not to look too awkward and out of my element."
    "I mean, shit - this place is serious enough to have a damn maitre d' for god's sake!"
    "After exchanging a few clipped words with the maitre d' and being made to feel suitably moronic thanks to his superior attitude, things begin to make more sense."
    "Apparently the young lady in who's name the table has been booked called ahead to let them know that she was running late."
    "She left instructions that the gentleman she's dining with should be shown to the table to await her arrival."
    "It occurs to me, as I'm ushered into my seat, that it would have been pretty easy for Alexis to let me know she was going to be late too."
    "Already she's managed to wrong-foot me, even before I've laid eyes on her."
    "I want to believe that it's just an honest mistake, really I do."
    "But this smacks so much of the Alexis that I used to know..."
    "First the phone-call out of the blue, and now this!"
    "I resolve that when she finally does grace me with her presence, I should say something to get back on level ground with her."
    "I'm not talking about starting a blazing row or anything quite so dramatic."
    "Just being firm and laying down some basic rules, as I don't want this reunion to go the same way as our former relationship."
    show alexis date at center, zoomAt(1.0, (1040, 720)) with easeinright
    "But the moment that I look up and see her breezing casually into the restaurant, looking around for me, everything else seems to disappear from my mind."
    "I might have mentioned, in passing, the fact that Alexis was pretty cute back in the day."
    "Well, it looks like I remembered that wrongly."
    "Alexis was stunning...and she still is."
    "If she was a hot teenager when we were together, she's grown into an even hotter woman."
    "I can remember the tawny blonde hair, the huge eyes and the full lips."
    "But where she used to have the body of a girl yet to bloom, the red dress she's wearing now hugs the curves of an amazing feminine figure."
    "For a moment, she clutches her expensive-looking black purse to her chest as she glances around the room."
    show alexis date happy at center, zoomAt(1.0, (840, 720)) with ease
    "Then she spots me, and waves."
    "Before I can stop myself, I'm standing up and waving back, smiling like a fool."
    show alexis smile at center, traveling(1.5, 0.3, (640, 1040))
    "She walks over to the table, and I can hear the clacking of her high heels on the tiled floor."
    "I try to keep a sensible head on my shoulders, but she looks like something out of a damn movie right now."
    show alexis talkative
    alexis.say "Hello, [hero.name], so good to see you again."
    show alexis smile
    mike.say "Y-yeah...great to see you too, Alexis."
    "I go to sit down, but Alexis gives a slight cough and nods towards her chair."
    "For a moment I'm puzzled by the gesture, until I realise that she's expecting me to pull her chair out for her."
    menu:
        "Pull out Alexis' chair":
            "I know it's a bit old-fashioned, but we are in a pretty up-market kind of place."
            show alexis at center, zoomAt(1.5, (640, 1140)) with ease
            "Nodding that I understand her, I hurry round to pull out Alexis' chair and make sure she's seated comfortably."
            "She smiles in approval, clearly gratified to have me treat her in such a gentlemanly manner."
            $ alexis.sub -= 5
            $ alexis.love += 1
        "Don't":
            "Jesus wept - I'm meeting an old girlfriend for a meal in the twenty-first century."
            "Not courting a prospective bride on the maiden voyage of the Titanic!"
            "I pretend not to have understood what Alexis was expecting of me and just sit straight back down."
            show alexis annoyed
            "I can tell from the expression on her face that she's momentarily put out."
            show alexis at center, zoomAt(1.5, (640, 1140)) with ease
            "But she'd have to call me out on it and look like a bit of a bitch in doing so, and instead she chooses to ignore the whole matter and just sit down herself."
    hide alexis
    show restaurant meal alexis date nomeals with fade
    "As the menus arrive and I realise that this place is so much style over substance that I haven't been able to even guess what the cuisine they're serving is, we try to make small-talk."
    mike.say "I'm guessing there was a bit of a mix-up with the times tonight?"
    show restaurant meal alexis date nomeals happy
    "Alexis smiles at me over the top of her menu and lightly waves the comment away."
    alexis.say "Oh, [hero.name], that's fine - there's no need to apologise!"
    "What - did she actually just let me off the hook for something that she did?!?"
    "I open my mouth to object, but find myself interrupted by the arrival of the waiter to take our orders."
    "Unable to give Alexis a piece of my mind in front of someone else, I simply have to simmer down and pretend not to be annoyed at what she just did."
    "I'm feeling pretty wound up and distracted by now, and I just pick something almost at random from the menu before handing it back to the hovering waiter."
    alexis.say "It's so nice of you to agree to this, [hero.name]."
    alexis.say "I know we didn't part on the best of terms..."
    "Now there's quite the understatement."
    show restaurant meal alexis date nomeals -happy
    alexis.say "There were things we both did wrong..."
    "Both of us - really?"
    "I'd like to see the list of grievances against my name from back then!"
    alexis.say "But that was so long ago now."
    "I can feel teeth almost grinding together as I grit them and reply in a diplomatic manner."
    mike.say "That's all in the past now, Alexis."
    mike.say "I'd like to think that we've grown into different people since then."
    "That answer seems to be the one that Alexis was looking for, and the mood begins to lighten from that point on."
    show restaurant meal alexis date eat -nomeals with fade
    "We eat a couple of courses of way too expensive food and drink a bottle of wine that I suppose must be a decent one (it's expensive enough!)."
    "The talk turns to memories of being at school, with both of us being careful to avoid any sensitive topics."
    "I've almost forgotten all of the things that Alexis has done to irritate me tonight."
    "That is until I hear a deep, impossibly masculine voice intruding on the moment."
    "Shady guy" "Damn, girl - you're something else!"
    show restaurant meal alexis date -eat with fade
    show restaurant_meal_waiter_pose01 as man zorder 1 at left with easeinleft
    "I look up to see a guy towering over me that instantly makes me almost jump in my seat."
    "He's well over six feet tall, built like a professional athlete and shows off rugged good looks as he smiles down at Alexis."
    "She's already returning his smile, soaking up the adoration of this ebony demi-god that's decided to crash our private dinner."
    show restaurant meal alexis date blush
    alexis.say "Aww...that's so kind of you to say!"
    show restaurant meal alexis date -blush
    alexis.say "Tell me, do you work out?"
    alexis.say "I mean, you look like you must play ball or something, right?"
    "I can't believe that she's actually flirting with this guy, right in front of me!"
    "I know we kind of, sort of said this wasn't really a date."
    "But we both know that it kind of, sort of actually is!"
    menu:
        "Say something" if hero.fitness >= 25 and hero.charm >= 25:
            show restaurant meal alexis date bored
            mike.say "Hey, do you two mind doing your flirting on your own damn time!"
            "My angry words shatter the convivial mood that was fast building between Alexis and the other guy."
            "She looks at me with barely concealed annoyance in her eyes."
            "But to give him his credit, the guy seems to notice me for the first time."
            "Shady guy" "Hey, chill, bro - it's cool."
            "Shady guy" "I didn't know I was cramping your style...no need to get mad."
            hide restaurant_meal_waiter_pose01 as man with easeoutleft
            "He holds up a hand to acknowledge that he's backing off and that, as far as he's concerned, the matter's over and done with."
            "Alexis keeps her mouth shut as the guy walks away, but the rest of the night is irrevocably tainted by the incident."
            show restaurant meal alexis date eat bored
            "We eat the rest of our meal in a cold near silence and then go our separate ways."
            $ alexis.flags.restaurant_outcome = "stop_flirt"
            $ alexis.flags.conversation_event = "restaurant"
            $ alexis.flags.ntr_conversation = "flirt"
            $ game.pass_time(2)

            return
        "Say nothing":
            "I could speak up, but then this is supposed to be something that's not quite a date."
            "I don't really have any right to stop Alexis from talking to whoever she chooses."
            "Shady guy" "That's right, I play quarterback - you're a very perceptive young lady, you know that?"
            alexis.say "Let's just say that I have a lot of experience when it comes to spotting a pedigree athlete!"
            "The stranger beams at the compliment, but then seems to notice me for the first time."
            "Shady guy" "Oh, my apologies - I didn't see your man there."
            alexis.say "Who, [hero.name]?"
            alexis.say "Oh, he's okay - we're old friends catching up on old times."
            "Shady guy" "That's cool...but don't forget to keep some space aside for NEW friends?"
            "Shady guy" "You know what I'm saying?"
            hide restaurant_meal_waiter_pose01 as man with easeoutleft
            "With that he walks off and leaves us alone again."
    "We continue eating, but the tone of conversation is more muted now."
    "I could make an effort to inject new life into it, but the sight of Alexis flirting so openly in front of me makes me wonder what the point would be."
    "She's practically made it clear to me with that one act that this isn't some desperate attempt on her part to make things right between us."
    "Maybe the best I can hope for is to come out of this in one piece and with her as a kind of platonic friend, one that I can easily make excuses not to see ever again?"
    show restaurant meal nonpc with fade
    "Just before we order dessert, Alexis excuses herself to go to the bathroom."
    show restaurant meal nonpc order waiter with fade
    "I don't notice how long she's been gone until the waiter comes back a second time to ask if we're ready to order yet."
    "Telling him to come back in five minutes, I begin to wonder what's keeping Alexis."
    show restaurant meal nonpc -order -waiter with fade
    menu:
        "Go check on her":

            $ alexis.flags.caughtCheating = True
            $ alexis.flags.conversation_event = "restaurant"
            scene bg restaurant with fade
            "I get up as discreetly as I can and hurry over to the toilets."
            "It's only then that I realise I have absolutely no idea of how to check on Alexis in the women's bathroom."
            "I can't start hammering on the door or shouting her name, and walking straight in just isn't an option either."
            "In the end I settle for going into the men's bathroom instead, hoping that the wall between the two will be thin enough for me to hear what's happening on the other side."
            "But as soon as I walk in through the door, I disturb one of the waiters, who jumps at the sight of me and quickly scuttles out."
            "For a moment I can't make sense of it, thinking that restaurants usually have toilets in the back for staff."
            "It's only when I hear the sounds coming from the last cubicle that I begin to understand what he was actually doing in here."
            "The groans and moans emanating from behind the locked door can mean only one thing."
            "And I think that I'd honestly made up my mind what I was going to see, even before I walked into the second-to-last cubicle and stood on the toilet seat to peer over."
            show alexis reverse ntr publicbathroom vaginal with fade
            "There's the stranger that stopped at our table not twenty minutes ago."
            show alexis reverse ntr publicbathroom vaginal at startle(0.05,-10)
            "And there's Alexis, riding him like her life depended on it."
            menu:
                "Leave":
                    "I could have lived with her chatting another guy up, even in my company."
                    "But shit like this is just too much for me to put up with."
                    "It's proof positive that Alexis hasn't changed one bit since we were together all those years ago."
                    "I jump down from the toilet seat and storm out of the men's bathroom, not caring if either of them hears me as I go."
                    hide alexis with fade
                    "The waiter sees me grabbing my coat, and hurries over to make sure someone pays the bill."
                    "I sneer at his fake courtesy and tell him rather bluntly that the lady will be settling the cheque for tonight's meal."
                    "Alexis, I think, has already made me pay in more ways than one."
                    $ alexis.flags.restaurant_outcome = "found_leave"
                    $ alexis.flags.ntr_conversation = "leave"
                    $ game.pass_time(1)
                    return
                "Watch":
                    "I should walk away from this, or at least have the balls to interrupt them."
                    show alexis reverse at startle(0.05,-10)
                    "But instead I find myself compelled to remain silent and watch as they fuck in the next stall."
                    "I don't get to see everything, as I've evidently walked in on them while they're in the middle of it all."
                    show alexis reverse at startle(0.05,-10)
                    "Both of them are stripped naked, the stranger sitting astride the toilet and Alexis straddling his considerable lap."
                    "Neither of them speaks, and they're trying to keep as quiet as possible, though not really succeeding."
                    "I suppose it won't surprise you to learn that the guy's cock is simply massive."
                    "It stands erect and proud, perhaps an inch below Alexis' pussy as he literally holds her above it."
                    show alexis reverse at startle(0.05,-10)
                    "Though I can see her naked body without any kind of impediment, I keep finding myself drawn back to the expression on Alexis' face as she's lowered slowly onto the waiting cock."
                    "It's not one that I can ever recall seeing her show before, desperate, needy and almost, well...almost shameful."
                    show alexis reverse eyes_closed mouth_hurt at startle(0.05,-10)
                    "I watch as she bites her lip, almost expecting to see blood flow, in an effort to keep quiet as she slides down onto the huge cock beneath her."
                    "This isn't a long, drawn out instance of making love."
                    show alexis reverse mouth_pleasure at startle(0.05,-10)
                    "It's just two strangers fucking for the thrill of it in a toilet."
                    "The stranger holds the underside of Alexis' thighs so that he can more easily lift her up and down on his manhood."
                    "And with every thrust, she gasps more loudly, while her face becomes ever more flushed, her eyes more distant and cold."
                    show alexis reverse eyes_pleasure mouth_scream cum at startle(0.05,-15)
                    "It's not long before the guy cums inside of her, filling Alexis to the point where it begins to leak out even before he pulls out of her stretched pussy."
                    show alexis reverse eyes_surprised mouth_hurt -cum anal at startle(0.05,-15)
                    "But he's not done yet, I realise, as he lifts Alexis again so that he can thrust his cock straight up her ass."
                    "By this time, she's almost reeling from the way she's been used."
                    show alexis reverse eyes_pleasure mouth_ahegao at startle(0.05,-15)
                    "Her head lolls like that of a puppet with severed strings, and her tongue lolls out of her open mouth."
                    hide alexis with fade
                    "Sensing that the end is fast approaching, I hop down from my perch as quietly as I can manage and hurry back to our table."
                    "When Alexis returns a few minutes later, I try not to notice the signs of dishevelment that she's not been able to hide."
                    "The conversation is muted from then on, but I decide to play along with her excuse of being tired."
                    "We see out the end of the meal with this pretence of ignorance still going on."
                    "But all the time, my mind is racing thanks to what I've seen and the things that it could imply."
                    $ hero.money -= 500
                    $ alexis.flags.restaurant_outcome = "found_watch"
                    $ alexis.flags.ntr_conversation = "cheat"
                    $ game.pass_time(1)
                    return
        "Wait":

            "It seems to take forever for Alexis to wrap things up in the bathroom and make it back to the table."
            show restaurant meal alexis -nonpc with fade
            "She looks a little worse for wear when she sits down, but assures me that she's just feeling a little tired and that there's nothing more to worry about."
            "I try to forget about it and focus on ordering dessert, but a knowing grin on the waiter's face still bugs me all the same."
            $ alexis.flags.restaurant_outcome = "wait"
    "The rest of the meal passes fairly pleasantly and without incident."
    show restaurant meal alexis waiter alexishappy with fade
    "Only when the bill arrives and Alexis smiles at the waiter do I feel like the old annoyances are creeping back in once more."
    alexis.say "My date will be handling the cheque."
    "My eyes almost pop out of my head, as I've been keeping a rough estimate of the evening's cost in the back of my mind."
    "Luckily Alexis is still looking at the waiter when this happens, and I manage to pull my face back into something resembling a blithe grin when she does turn back to me."
    alexis.say "It's so kind of you to agree to treat me like this!"
    "She flutters her eyelids as I allow the waiter to rob me blind."
    "I just hope this is a simple case of miscommunication, and that Alexis isn't a gold-digger that's eyeing me up as her latest claim."
    $ hero.money -= 500
    $ game.pass_time(2)
    return

label alexis_event_03:
    if alexis.love.max < 60:
        $ alexis.love.max = 60
    show alexis casual
    "This is turning out to be one of those days where everything seems to be going my way."
    "I'm out on a date with Alexis, taking a casual stroll around the mall."
    "I'm feeling good, and more importantly, my date is looking incredible at my side."
    show alexis happy
    "Alexis hangs on every word I say, laughs at all my jokes and makes me feel like a million dollars."
    "Plus I can see the way other people are looking at her as we pass them."
    "Most of the guys, and even some of the girls that go by are shooting her admiring glances."
    "And sure, I might catch Alexis checking out the occasional one of them in return."
    show alexis normal
    "But while ninety nine percent of her attention is on me, it's all good!"
    mike.say "Hey, Alexis..."
    mike.say "What do you think of these pants?"
    mike.say "I kind of like them - but I'm not sure."
    mike.say "You think I can pull them off?"
    "Alexis doesn't even seem to be looking into the same shop window as me."
    show alexis at center, zoomAt(1.5, (640, 1040)) with hpunch
    "A fact which is confirmed when she grabs hold of my arm and pulls me away."
    mike.say "Wha..."
    mike.say "What are you doing?"
    show alexis at center, zoomAt(1.5, (540, 1040)) with ease
    alexis.say "Will you come over here, [hero.name]?"
    show alexis wink
    alexis.say "There's something I want to show you!"
    "Knowing that it's for the best, I give in."
    hide alexis with easeoutleft
    "I let Alexis drag me over to the window in question."
    scene bg jewelrystore
    show alexis casual happy
    with fade
    alexis.say "Now this is what I'm talking about!"
    alexis.say "What do you think, [hero.name]?"
    show alexis normal
    alexis.say "Aren't they pretty?"
    "I was expecting to be greeted with designer clothes on the other side of the glass."
    "Maybe even hoping that I'd see some adventurous underwear that Alexis was eyeing up."
    "But instead my eyes go wide for another reason entirely."
    "Spread out before me is a bewildering array of rings, chains and watches."
    "It's the window of a pretty high-end jewellers shop!"
    mike.say "Yeah, Alexis..."
    mike.say "They're pretty alright - pretty expensive!"
    show alexis confused
    "Alexis frowns at this, crossing her arms over her chest."
    "I can see that she's already starting to pout at my reaction."
    show alexis angry
    alexis.say "I should have known that's what you'd say!"
    alexis.say "All I did was show them to you, for god's sake!"
    "I eye Alexis with suspicion, narrowing my eyes."
    mike.say "If that's the case, Alexis..."
    mike.say "Then why are you getting defensive all of a sudden?"
    mike.say "Is this the point where I was supposed to offer to buy you something?"
    mike.say "Then you'd say that they were too expensive."
    mike.say "I'd insist you were worth it, that I could afford it."
    mike.say "Then we'd go back and forth, but I'd end up buying you it in the end, right?"
    show alexis annoyed blush
    "I can see Alexis's cheeks beginning to flush as I lay out the scenario."
    "And by the time I'm done, she's visibly red in the face."
    show alexis sad
    alexis.say "You don't have to make it sound so...so cynical!"
    alexis.say "Guys buy their girlfriends jewellery all the time!"
    alexis.say "Some even think that their girlfriends deserve nice things..."
    "I can see that Alexis is tipping over into feeling sorry for herself."
    "And that's the last thing that I want to happen, because it'll ruin our date."
    "So I let out a sigh of resignation and nod my head."
    mike.say "I'm sorry, Alexis."
    mike.say "I didn't mean to be...well...mean!"
    mike.say "Why don't you show me what caught your eye?"
    "Just then a thought occurs to me."
    mike.say "Wait..."
    mike.say "You weren't looking at the wedding rings?"
    mike.say "Were you?"
    show alexis surprised
    alexis.say "What?"
    alexis.say "No, [hero.name]!"
    show alexis normal -blush
    alexis.say "I was looking at this necklace."
    alexis.say "Oh, and the matching earrings too!"
    "My fears assuaged, I lean in to study the jewellery she's pointing out."
    "But then I feel a renewed surge of emotion as I read the price tag."
    mike.say "Whoa!"
    mike.say "Did you check out the price of those, Alexis?"
    mike.say "It's like two thousand dollars for the set!"
    show alexis blush
    "Alexis blushes a little more and refuses to meet my eye."
    alexis.say "Yeah..."
    show alexis -blush
    alexis.say "But you're a big-shot at work, right?"
    alexis.say "You must have a load of cash stashed in the bank!"
    alexis.say "I bet you could afford to splash out a little..."
    menu:
        "Agree (-2000$)" if hero.money >= 2000:
            "You know what, Alexis is one hundred percent right!"
            "I work my ass off, day in and day out."
            "And what do I have to show for it?"
            "Sure, my bank balance looks healthy most of the time."
            "But nobody else apart from me ever sees that."
            "Now jewellery, on the other hand..."
            "Everybody sees that, especially on a girl like Alexis!"
            mike.say "You're right, Alexis!"
            show alexis surprised
            alexis.say "I am?"
            mike.say "Yes you are!"
            mike.say "I shouldn't be so stingy."
            show alexis normal blush
            alexis.say "Does that mean..."
            mike.say "Oh yes it does!"
            mike.say "Let's get in there before somebody beats us to it!"
            $ alexis.love += 10
            show alexis happy
            "Alexis claps her hands together in sheer delight."
            "Then she takes hold of my hand, leaning in to plant a kiss on my cheek."
            "Alexis pulls me into the jewellers, and up to the counter."
            "All it takes is a few moments for me to point out what we want."
            "Then the assistant pulls them out of the window."
            $ hero.money -= 2000
            "I watch as they're boxed up and then pay with my card."
            "And I hardly feel the usual punch in the gut when the transaction goes through."
            scene bg mall2
            show alexis happy
            with fade
            "As we leave the jewellers, Alexis is beaming."
            "She clings to my arm. leaning against me."
            "And I hope that this show of affection is the real thing."
            "Because I can't afford to drop two thousand dollars every other day."
            "But surely Alexis's love can't be that expensive to keep - can it?"
            $ game.active_date.score = 100
        "Refuse":
            "You know what, Alexis might be right about my financial status."
            "But that still doesn't mean that I have to indulge her every whim!"
            mike.say "Forget about it, Alexis."
            mike.say "I might break the bank for you occasionally."
            mike.say "Like if it was your birthday."
            mike.say "Or a Christmas when you'd been a really good girl!"
            mike.say "But I'm not just going to drop two grand on a whim!"
            show alexis angry
            "Alexis frowns at me and then turns away from the window."
            alexis.say "Keep it up, [hero.name]."
            alexis.say "This way I know exactly how you feel about me!"
            hide alexis
            "With that she strides off at a brisk pace."
            "Which leaves me to hurry after her."
            mike.say "Alexis!"
            mike.say "Don't be like that!"
            mike.say "And don't walk away - at least wait for me to catch up!"
            "Weaving through the crowd of shoppers, I wave frantically at Alexis."
            "But she just keeps on walking, meaning that I have to chase after her."
            "Well, looks like that's the end of everything going my way!"
            $ game.active_date.score -= 75
    return

label alexis_event_04:











    if alexis.love.max < 80:
        $ alexis.love.max = 80
    show alexis
    mike.say "Alexis, remind me what you wanted?"
    "There's no immediate reply, and so I give her a gentle tap on the shoulder."
    alexis.say "Huh...what?"
    mike.say "What do you want to take into the film with you?"
    mike.say "Want to share a popcorn and soft-drink with me?"
    show alexis annoyed
    alexis.say "Oh, right...whatever's fine with me, [hero.name]."
    "I nod slowly and order the snacks, while trying to see where Alexis' attention was a moment beforehand."
    "Seems she could have been checking out the posters for the upcoming attractions."
    "Or else maybe she was checking out a bunch of guys on the other side of the lobby..."
    scene bg cinemaroom
    show alexis
    with fade
    "But as we make our way into the theatre and sit down, waiting for the film to start, I chide myself for being petty."
    "Of course guys are going to check Alexis out, she's gorgeous."
    "And if she chooses to glance back, then she's only human too."
    show alexis blush
    "I have to get over the fact that she cheated on me, as that happened so far into the past."
    "Sure, if she were getting up to stuff in the here and now, I'd be crazily pissed off."
    "But she's not, and that's the most important thing to remember."
    "Hell, it's not like I stopped eyeing up other women since we started seeing each other again, is it?"
    show alexis normal at center, zoomAt(1.5, (640, 1040))
    pause 0.5
    show alexis normal at center, zoomAt(1.5, (640, 1140)) with ease
    "Finding our seats, I can't help noting that the place is almost full."
    "I guess we weren't the only people who chose to see this movie and maybe thought it'd be a quiet time to do so."

    if alexis.flags.story == 2:
        show alexis happy at center, zoomAt(1.5, (640, 1140)), startle
        "Just as the house lights are going down, I hear Alexis chuckling to herself."
        "Intrigued by this, I lean in and whisper close to her ear."
        mike.say "What's so funny all of a sudden?"
        show alexis at center, zoomAt(1.5, (640, 1140)), startle
        "Alexis chuckles again, and then whispers back her answer."
        show alexis normal
        alexis.say "See that guy in the front row, the one with the badass haircut?"
        mike.say "Erm...yeah, I think so."
        mike.say "What about him?"
        alexis.say "He's been checking me out since we walked in."
        alexis.say "But his girlfriend just caught him doing it a couple of minutes ago."
        "I can now see the guy that Alexis must be talking about, sitting in the front row and looking decidedly uncomfortable."
        "She seems to be right, as the girl in the seat next to him is hissing something and jabbing a finger at him."
        "As the opening credits of the film roll, she gets up, empties a large drink into his lap and storms out."
        "He makes an alarmed sound and hurries after her, to the accompaniment of laughter from half the crowd and shushing from the other."
        "I look at Alexis, noting that she's one of those laughing."
        "And as I do so, it occurs to me that she must have been watching that guy at least as much as he was her."
        "How else could she have known what was going on?"
        "But then I shake my head, realising what a paranoid jerk I sound like."
        "We're sitting facing forwards, so of course she could see all of what just happened."
        "That letching moron just put on an impromptu pre-film show for the rest of us, that's all."
        "I shake my head at the thought of the hapless buffoon, and settle down to watch the film."
        scene bg cinemaroom at dark with dissolve
        "The next couple of hours pass in the pleasant alternate reality of the silver screen, and I forget all of my problems for almost the whole while."
        "All that manages to snap me out of it for a couple of seconds is the feeling of someone touching me in the darkness."
        "But then I realise it's just Alexis, taking my hand in hers and leaning her head on my shoulder."
        "After this, it doesn't take me long to lose myself in the film once more."
        scene bg cinemaroom
        show alexis blush at center, zoomAt(1.5, (640, 1040))
        with dissolve
        "On the way out of the room, Alexis is still hanging off of my arm, leaning into me with a smile on her face."
        alexis.say "This was fun, [hero.name]."
        alexis.say "I can't remember when I last went to see a film on a date."
        alexis.say "Well...maybe when I did and had such a great time!"
        mike.say "Me too, Alexis."
        mike.say "We shouldn't wait too long before we do this again."
        "I feel her squeeze my arm in response, and it gives me a feeling like something fluttering in my chest."
        "So what does it matter how many guys she looks at?"
        "So long as she's walking home on my arm at the end of the night."
        $ alexis.flags.cinema_outcome = "no_ntr"
    else:

        scene bg cinemaroom at dark with dissolve
        "By the time we're sitting in our seats, watching the trailers, I can already feel my eyes starting to close."
        "The dark theatre, plush seats and the way a film takes you out of reality all conspire to send me off to sleep."
        if alexis.flags.story == 0 and (hero.energy >= 5 or alexis.sub >= 50):
            "But that doesn't mean I have to just sit back and let it happen."
            "I've had a tough week, with no chance to relax or unwind the whole time."
            "There's going to be plenty of time to sleep once I'm home and in bed."
            "And I'm not going to miss out on the chance to spend some quality time with Alexis either!"
            "I find my head drooping onto my shoulder, manage to jerk myself awake with a slight grunt of confusion."
            mike.say "Huh...wha..."
            show alexis surprised at center, zoomAt(1.5, (640, 1140)), vshake
            "The noise seems to make Alexis jump, as if she wasn't expecting it."
            show alexis confused
            "She whispers urgently to me a moment later."
            alexis.say "God's sake, [hero.name]!"
            alexis.say "You almost scared the life out of me."
            show alexis normal
            "I can't help getting the odd feeling that she was in the act of doing something or other."
            "Though as I'm still a little groggy from almost nodding off, I just write it off as my being confused."
            "In the end, I manage to keep from actually falling fully asleep before the end credits roll."
            "Hell, I even get to see the little scene they put in afterwards too, which is a bonus."
            "I still need to have Alexis fill me in on some of the major plot details."
            "But for some reason she's quite vague, as though she was distracted too."
            "Who knows - maybe she's just as tired as me, just better at hiding it?"
            $ alexis.flags.cinema_outcome = "wait"
        else:
            $ alexis.flags.caughtCheating = True
            $ alexis.flags.conversation_event = "cinema"
            "All too soon I feel myself sinking into that weird place between sleep and waking."
            "That place where nothing seems to make sense and thoughts stretch into strange shapes without any effort whatsoever."
            "I don't know how long I'm actually asleep, but I don't get an elbow in the ribs, and so must not have been snoring."
            scene bg cinemaroom at dark with wipeup
            "And so when I finally wake up, I have literally no idea where I am for a good few minutes."
            "But slowly it starts to come back to me that I'm sitting in the cinema, with Alexis by my side."
            "Suddenly realising that I probably need to make an urgent apology to my date, I turn to look in her direction."
            "At first I think that she must have got up and slipped out to the bathroom or to refill her drink."
            "As when I gaze over, I can't see her in the seat at all."
            "But then I see something moving in the seat, and realise that she is one row further down the room."
            "The reason that I couldn't see her at first was because she's hunched over for some unknown reason."
            "There's an odd sound coming from down there too."
            "And at first I think she must be in the act of retching or actually throwing up, head between her knees."
            "Concerned for her well-being, I lean over a little to see what's going on."
            show alexis movie bj with fade
            "It's then that I see the guy sitting on the other side of her has his flies undone."
            "And worse, Alexis' head isn't between her knees at all."
            "It's actually buried in the lap of a complete stranger."
            "I can't believe what I'm seeing - she's giving him a blowjob while sitting right beside me!"

            if alexis.flags.story == 0:
                menu:
                    "Leave":
                        "I know that I should stop her, or at least say something."
                        "But the truth is that the shock I'm feeling seems to put me into a kind of autopilot."
                        "Without uttering a single word, I get up from my seat and walk out of the theatre."
                        "I don't know if Alexis even notices that I'm gone."
                        "As she waited for me to fall asleep before making a move on some other guy, I doubt it."
                        "And whether or not she'll be surprised to find me gone, I have no idea."
                        "The truth is that I thought Alexis had changed since we were last together."
                        "But it seems that I was one hundred percent wrong."
                        "And she's still just waiting to make a fool out of me at the first available opportunity."
                        scene bg cinema with fade
                        "As I leave the cinema, all I'm thinking about is how I'm going to get home."
                        "What I'll say to Alexis if she bothers to call me is something that I just can't seem to process."
                        "Maybe I'll see if she confesses or not."
                        "Maybe I'll confront her with the fact that I know and judge her by how she reacts."
                        "Or maybe I won't answer her call when it comes."
                        "All I know right now is that I want to be far away from here before Alexis realises I'm gone."
                        $ alexis.love -= 5
                        $ alexis.flags.cinema_outcome = "found_leave"
                        $ alexis.flags.ntr_conversation = "leave"
                        $ game.active_date.stay = False
                        $ hero.cancel_activity()
                    "Watch":
                        "All it'd take is for me to say something that one or both of them could hear."
                        "Or a simple tap on the shoulder would break the spell for good."
                        "Though I have no idea what would happen in the seconds that followed..."
                        "But for some reason, I do neither and simply continue to watch."
                        "After the way in which Alexis betrayed me when we were dating as kids, I should be outraged."
                        "And yet I keep on staring at the undeniable evidence that she hasn't changed one bit."
                        "Maybe it's because, before this moment, I'd never seen the evidence with my own eyes?"
                        show alexis movie bj up
                        "But whatever the reason, I can't stop watching in rapt disgust as her head bobs up and down in the guy's lap."
                        "I make sure not to turn my head in their direction, trying to keep from being seen."
                        "Still I can make out the fact that the stranger has his head leaned back, clearly enjoying the treatment."
                        "Why am I watching this?!?"
                        "She's making a fool out of me in public, and I can't tear my eyes away from the very act that's doing it!"
                        show alexis movie bj down
                        "I can feel my breathing becoming heavier as the blowjob becomes more intense."
                        "My heart's pounding in my chest and the blood's pounding in my ears."
                        "Oh god - am I actually getting off on this?"
                        "Is the real reason that I was so destroyed by Alexis' cheating the first time around not because of the infidelity?"
                        "Was it really because of the fact that I couldn't watch as she did so?"
                        "By now, the guy on the other side of Alexis is starting to make a desperately suppressed sound."
                        "At the same time, his hands are clutching at the arms of his seat."
                        show alexis movie bj cum
                        "No doubt he's moments away from cumming, and doing it right inside of her mouth too!"
                        "Before I have time to form another thought, he stiffens and Alexis makes a muffled gagging sound of her own."
                        "I watch out of the corner of my eye and with rapt fascination as she swallows every last drop of his cum."
                        "And then, without a single word passing between them, it's all over."
                        hide alexis
                        show alexis at center, zoomAt(1.5, (640, 1140)) with fade
                        "Alexis sits up and come back to her seat while the guy begins to fasten up his flies."
                        "I hastily put my head back on my shoulder and close my eyes, feigning sleep."
                        alexis.say "Hey, sleepy-head!"
                        mike.say "Huh...what the hell..."
                        show alexis happy at center, zoomAt(1.0, (640, 1140)), startle
                        "Alexis laughs out loud, apparently buying my efforts to appear asleep."
                        alexis.say "I can't believe it - you slept through the whole film!"
                        mike.say "Wow...I must have been more tired than I thought!"
                        hide alexis
                        show alexis kiss
                        with fade
                        $ alexis.flags.kiss += 1
                        "Still distracted by my own thoughts, I'm taken by surprise when Alexis kisses me without warning."
                        "I return the gesture, almost completely as a reflex action and with no hesitation, despite what I've seen her do."
                        "But then she goes further, sliding her tongue into my mouth and stepping into the kiss with more passion."
                        "At first I barely notice the hints of it still on her tongue even now."
                        "It only becomes apparent to me just what that odd, elusive taste is a couple of moments later."
                        "His cum...that's what it is."
                        "I can taste the last remnants of it on Alexis' tongue as she kisses me!"
                        hide alexis
                        show alexis happy at center, zoomAt(1.5, (640, 1040)) with fade
                        "Alexis jokes about my nodding off as we get up and leave the theatre."
                        "But she never once mentions what she was doing while I was supposedly asleep."
                        "I see her exchange a furtive glance with the guy himself as we pass in the lobby."
                        "But she seems happy to think that she's gotten clean away with it."
                        "And if I'm honest, that's not even what's troubling me the most right now."
                        "I'm more concerned by the fact that I just sat there and watched!"
                        $ alexis.flags.cinema_outcome = "found_watch"
                        $ alexis.flags.ntr_conversation = "cheat"
                        $ game.active_date.score = 100
                    "Confront her":
                        scene bg cinemaroom at dark with fade
                        mike.say "Alexis - what the fuck are you doing?!?"
                        "I honestly have no idea how loud my voice is when I stand up and shout this out."
                        "But I know that I'm shouting, and that it comes at a particularly quiet point in the film too."
                        "This means that everyone in the place sees my silhouette appear on the screen and hears what I said with perfect clarity."
                        "I only know this because of the numerous voices I can hear, raised in either surprise or objection."
                        "My own eyes are not looking around though, as they're solely focused on Alexis and the object of her most intimate attentions."
                        "The guy is already making a clumsy effort to force her head out of his lap, as if this will make a difference of some kind."
                        "Who knows, maybe he's hoping that he can convince me he just looked down and realised what was going on for the first time?"
                        "His haste to shove her off of his exposed cock means that Alexis is sent sprawling onto the floor between the rows of seats."
                        show alexis surprised at center, zoomAt(1.5, (640, 1140)), vshake
                        "She lands in an undignified heap, coughing and choking from having his dick unceremoniously yanked out of her mouth."
                        "The guy starts to mutter something that might either be an apology or a half-arsed attempt at an explanation of some kind."
                        "But I ignore him, only interested in what Alexis has to say for herself."
                        mike.say "Jesus, Alexis - are you that hungry for cock?"
                        mike.say "I guess I should be grateful that you at least waited until you thought I was asleep!"
                        show alexis sad
                        alexis.say "[hero.name]...I...I can..."
                        "By now the house lights have come up and other patrons are yelling in annoyance at the disturbance we've caused between us."
                        "Still others are openly laughing and pointing, amused at Alexis and the other guy being caught in the act."
                        "Out of the corner of my eye, I can see cinema employees starting to come down the aisle."
                        "Looks like this might be a good time to think about leaving."
                        mike.say "Ah, shut up, Alexis."
                        mike.say "Whatever bullshit you've got to say, I don't want to hear it."
                        mike.say "You were always better at using you mouth to suck cock anyway..."
                        scene bg cinema with fade
                        "And with that, I turn my back on her and storm out of the theatre."
                        "I don't stop until I'm out of the cinema and standing on the street."
                        "Without a thought for Alexis, I hail a cab and jump in."
                        "Maybe she can convince the guy who's dick she was just sucking to give her a ride home."
                        "Whatever he asks for in way of payment, I'm sure she'll willingly oblige."
                        $ alexis.flags.cinema_outcome = "found_confront"
                        $ alexis.set_gone_forever()
            else:

                "All it'd take is for me to say something that one or both of them could hear."
                "Or a simple tap on the shoulder would break the spell for good."
                "Though I have no idea what would happen in the seconds that followed..."
                "But for some reason, I do neither and simply continue to watch."
                "After the way in which Alexis betrayed me when we were dating as kids, I should be outraged."
                "And yet I keep on staring at the undeniable evidence that she hasn't changed one bit."




                show alexis movie bj up
                "But whatever the reason, I can't stop watching in rapt excitement as her head bobs up and down in the guy's lap."
                "I make sure not to turn my head in their direction, trying to keep from being seen."
                "Still I can make out the fact that the stranger has his head leaned back, clearly enjoying the treatment."

                "I can understand that Alexis needs this. But why am I so compliant?"
                "Why am I watching this?!?"
                "She's making a fool out of me in public, and I can't tear my eyes away from the very act that's doing it!"
                show alexis movie bj down
                "I can feel my breathing becoming heavier as the blowjob becomes more intense."
                "My heart's pounding in my chest and the blood's pounding in my ears."
                "Oh god - am I actually getting off on this?"
                "Is the real reason that I was so destroyed by Alexis' cheating the first time around not because of the infidelity?"
                "Was it really because of the fact that I couldn't watch as she did so?"
                "By now, the guy on the other side of Alexis is starting to make a desperately suppressed sound."
                "At the same time, his hands are clutching at the arms of his seat."
                show alexis movie bj cum
                "No doubt he's moments away from cumming, and doing it right inside of her mouth too!"
                "Before I have time to form another thought, he stiffens and Alexis makes a muffled gagging sound of her own."
                "I watch out of the corner of my eye and with rapt fascination as she swallows every last drop of his cum."
                "And then, without a single word passing between them, it's all over."
                scene bg cinemaroom
                show alexis blush at center, zoomAt(1.5, (640, 1140))
                with fade
                "Alexis sits up and come back to her seat while the guy begins to fasten up his flies."
                "I hastily put my head back on my shoulder and close my eyes, feigning sleep."
                alexis.say "Hey, sleepy-head!"
                mike.say "Huh...what the hell..."
                show alexis happy at center, zoomAt(1.0, (640, 1140)), startle
                "Alexis laughs out loud, apparently buying my efforts to appear asleep."
                alexis.say "I can't believe it - you slept through the whole film!"
                mike.say "Wow...I must have been more tired than I thought!"
                hide alexis
                show alexis kiss with fade
                $ alexis.flags.kiss += 1
                "Still distracted by my own thoughts, I'm taken by surprise when Alexis kisses me without warning."
                "I return the gesture, almost completely as a reflex action and with no hesitation, despite what I've seen her do."
                "But then she goes further, sliding her tongue into my mouth and stepping into the kiss with more passion."
                "At first I barely notice the hints of it still on her tongue even now."
                "It only becomes apparent to me just what that odd, elusive taste is a couple of moments later."
                "His cum...that's what it is."
                "I can taste the last remnants of it on Alexis' tongue as she kisses me!"
                hide alexis
                show alexis happy
                with fade
                "Alexis jokes about my nodding off as we get up and leave the theatre."
                "But she never once mentions what she was doing while I was supposedly asleep."
                "I see her exchange a furtive glance with the guy himself as we pass in the lobby."
                "But she seems happy to think that she's gotten clean away with it."
                "And if I'm honest, that's not even what's troubling me the most right now."
                "I'm more concerned by the fact that I just sat there and watched!"
                $ alexis.flags.cinema_outcome = "agree_ntr"
                $ game.active_date.score = 100
    return

label alexis_event_05:










    if "sports_car" in hero.inventory:
        call alexis_nice_car from _call_alexis_nice_car
    else:
        call alexis_crap_car from _call_alexis_crap_car
        $ hero.cancel_event()
        return
    if alexis.love.max < 100:
        $ alexis.love.max = 100
    "It seemed like a good idea at the time, when I remembered just how often Alexis and I used to hang-out at the beach back in high-school."
    "So much so, in fact, that going back there now seemed to be a complete no-brainer."

    if alexis.flags.story == 2:
        show alexis happy swimsuit at center with ease
        "But as we walk across the sand, looking for a spot to claim, it doesn't take long for me to see the essential flaw in my plan."
        "I've been wandering in Alexis' wake since we got out of the car, totally distracted by the sight of her in a swimsuit."
        "And it's only when we actually stop and I glance around that I begin to see I'm not the only guy that she's having that effect on."
        "Even though there's an entire beach that's almost full of scantily-clad women to ogle, all eyes seem to be on Alexis right now."
        "I'm not sure whether or not she's actually noticed the attention that she's getting from everyone else on the sand."
        "And for a moment, I wonder if I should say something to her, just in case she realises and it gets awkward."
        "But then I see her bend down to spread her towel out on the ground, visibly shaking her ass as she does so."
        "My suspicions are all but confirmed a moment later, when she reclines upon the towel and pulls out her sun-cream."
        "Alexis is one hundred percent aware of the attention that she's getting."
        "What's more, she's revelling in it too!"
        "I sit down beside her, trying to decide who's bothering me more."
        "Is it the dozens of guys that are currently checking out my date?"
        "Or Alexis herself, who seems to be loving every moment of it?"
        show alexis talkative
        alexis.say "[hero.name], would you be a darling?"
        show alexis normal
        mike.say "Huh...what was that?"
        "If Alexis is aware of just what's making me so distracted and edgy, she chooses to ignore it completely."
        "Instead, she extends the hand holding the sun-cream, giving me a cheeky smile as she does so."
        show alexis talkative
        alexis.say "Would you mind doing the honours?"
        show alexis normal
        mike.say "Oh...yeah, sure thing, Alexis!"
        "Of course I feel like a chump for just jumping to attention and following her every whim."
        "But seriously, what am I going to do about it?"
        "I can't make a scene in front of all these people and show her just how paranoid and insecure she makes me feel."
        "And what kind of message would that send to all of the other guys checking her out too?"
        hide alexis
        show beach cream alexis swimsuit with fade
        "So I obligingly squeeze the cream onto my hands and start to work it into Alexis' shoulders and back."
        "She lies flat on her belly while I do this, making appreciative noises as I progress down her spine and toward her waist."
        "I'd thought that my mind would be churning over the way Alexis flaunts herself, ruminating on the way she's silently showing me up."
        "But I soon find that I'm enjoying myself far more than I would have thought possible."
        "Alexis has such a fantastic body that being able to feel and caress it in such a manner is a real turn-on."
        "My worries melt away as I trace the shape of her lines and curves, making sure to cover every inch of her exposed flesh as I do so."
        "The sounds that she's now making are almost as arousing as the feel of her slick skin too."
        "Every sigh and moan that she lets slip makes me lick my lips and stiffen below the waist."
        "By now, I can't help shaking my head at just how paranoid I was letting myself become."
        "Sure, there might be anything up to a hundred guys, all of them staring at Alexis and thinking about what they'd like to do to her."
        "But I'm the only one that's actually getting to put his hands on her in and enjoy the experience."
        "I'd bet that every one of them is pretty jealous of me right now!"
        "How have I let myself forget that fact?"
        "Of course people are going to stare at Alexis - how could they not?"
        "But she's here with me, and looking isn't touching, is it?"
        show beach cream alexis nomc
        "I keep that in mind for the rest of the time that we spend at the beach."
        "And it means that I hardly notice the attention that she receives as we walk along the beach or play in the crashing waves."
        hide beach cream
        show alexis flirt swimsuit
        with fade
        "All the time, while it's clear that Alexis is still enjoying the feeling of having so many eyes upon her, she never once leaves my side."
        "I guess that's one of the things that I have to come to terms with myself, if I want to keep a hold of her this time around."
        "I need to stop thinking about other people noticing her, and make sure that enough of Alexis' attention is focused on me instead."

        $ alexis.flags.beach_outcome = "no_ntr"
        $ game.active_date.score = 100
    else:

        show alexis happy swimsuit at center with ease
        "But I'm already starting to wonder if coming down here today was such a good idea after all."
        "The sun is just scorching, meaning that the sand is likewise almost too hot to walk on."
        "All around us, I can see people either trying to get out of the sun or else frying themselves under its relentless heat."
        mike.say "Erm, Alexis...you don't think it's too hot to be out here, do you?"
        "Alexis responds to this by raising her eyebrows and shaking her head in disbelief."
        show alexis talkative
        alexis.say "Really, [hero.name]?!?"
        alexis.say "Isn't that what sun-screen is for?"
        show alexis annoyed
        mike.say "I know, but..."
        show alexis whining
        alexis.say "Oh, don't be such a stick-in-the-mud about it."
        show alexis talkative
        alexis.say "If you burst into flames, just go jump in the sea!"
        show alexis normal
        "And with that, she puts on her sunglasses and lies down to take advantage of the sun's rays."
        hide alexis
        show beach cream alexis swimsuit nomc with fade
        "I mutter something rather passive aggressive under my breath and start to plaster myself in sun-cream."
        "Alexis makes no sign that she's heard me, and for all I can tell she could already be asleep at my side."
        "I lie down too, only meaning to close my eyes for a couple of moments."
        "But the next thing that I know, I'm roused by something brushing against my side."
        mike.say "Huh...what's..."
        alexis.say "Don't wake up on my account."
        mike.say "Oh, Alexis..."
        mike.say "What are you getting up for?"
        mike.say "You only just laid down!"
        "Alexis chuckles at this and shakes her head once again."
        alexis.say "It's been more than an hour, [hero.name]!"
        alexis.say "You must have fallen asleep almost as soon as you shut your eyes."
        "I grab my phone, checking the time and finding that she's not pulling my leg."
        hide beach cream
        show alexis swimsuit talkative
        with fade
        alexis.say "Anyway, I'm thirsty."
        alexis.say "So I'm going to grab some water from the kiosk over by the dunes."
        alexis.say "You want anything?"
        show alexis normal
        mike.say "Sure, grab me one too."
        hide alexis with easeoutright
        "I watch Alexis walk a little way off, and then lay back down again."
        "The kiosk that she mentioned isn't too far, so she should be back in a couple of minutes at the most."
        "And so by the time she's been gone a good fifteen minutes, I'm beginning to get worried."

        if alexis.flags.story == 0:
            menu:
                "Wait for her":
                    "But then I realise that I'm being paranoid again, and that there's a hundred reasons why Alexis could be taking so long."
                    "The queue might have been longer than she expected, or the kiosk might have been sold out and she needed to walk to the next one."
                    "I have to learn to be more patient when it comes to her doing stuff like this, not to jump to any crazy conclusions."
                    "So I just close my eyes and resign myself to waiting until she comes back in her own good time."
                    show alexis swimsuit blush with easeinright
                    "When she finally does so, I deliberately ignore the fact she's been gone almost an hour."
                    mike.say "I was starting to worry there a little, Alexis."
                    mike.say "Any longer and I'd have filed a missing person's report!"
                    "Alexis looks this way and that, as if she's suddenly worried about something."
                    show alexis annoyed
                    "Which is odd behaviour for someone that just went to buy water."
                    "But I've already promised myself that I won't read too much into her actions, so I ignore it."
                    mike.say "I guess there was a queue?"
                    mike.say "Weather like this, everyone'll be wanting some, right?"
                    show alexis blush
                    "For some reason, Alexis reddens at this and begins to shake her head."
                    mike.say "Just joking - it's okay!"
                    "Alexis nods and sinks down onto the towel beside me."
                    "She's oddly quiet the rest of the time we're at the beach."
                    "But I choose to put that down to the heat getting to her, despite her earlier dismissing of it's effects."
                    $ game.active_date.score = 100
                    $ alexis.flags.beach_outcome = "wait"

                    $ DONE["alexis_ntr_conversation"] = game.days_played
                    $ alexis.flags.story = 3
                "Look for her":
                    $ alexis.flags.caughtCheating = True
                    $ alexis.flags.conversation_event = "beach"
                    "There's no way that it should be taking her this long to grab a bottle of water and get back here."
                    "Call me paranoid, but I can't help thinking that something bad might have happened to Alexis."
                    "I stand up, glancing around in the vain hope that she'll appear the moment I do so."
                    "But there's still no sign of her, and so I set off in the direction of the kiosk, hoping to bump into her on the way."
                    "It doesn't take me long to arrive at my destination, or to see that Alexis isn't here either."
                    "By now I'm beginning to get worried, and I wonder if she's walked on to another kiosk to get water instead."
                    "The quickest way I know to reach the next one is the path that runs along the back of the beach-huts and in front of the dunes."
                    "So I make straight for it, my head already filling with worst case scenarios as to what I might find along the way."
                    "I've not gone far when I hear the sound of voices a little way off of the path."
                    "Thinking that it might be Alexis, or at least someone that's seen her pass this way, I head in their general direction."
                    "But as I get closer, my pace slows and I start to move as quietly as I can."
                    "One reason for this is that I soon pick out two of the voices as male and pretty surly in tone."
                    "The other is that I recognise the second as female, and more importantly as belonging to Alexis herself."
                    "Fearing that she might be about to get mugged, or worse, I creep closer and strain to see what's happening."
                    "What I do see makes me feel a surge of anger and prepare myself to come to Alexis' aid."
                    show alexis beach threesome mike lick out with fade
                    "She's bent over in between the two guys I could hear just now, swimsuit around her ankles and breasts exposed."
                    "The guys, who look like a couple of typical gang-bangers, both have their cocks out and are clearly rather excited."
                    "I'm horrified by what I see, convinced that I've stumbled upon Alexis the moment before they were about rape her."
                    "But then I see her face for the first time, and notice that she's actually wearing a sultry smile."
                    "Alexis licks her lips in anticipation as one cock looms towards her mouth and the other her ass."
                    "Whatever the hell's going on here, it's certainly not being done against her will!"
                    menu:
                        "Leave":
                            "I turn my head away the moment before the real action begins, and try to blot out the sounds that follow a moment later."
                            hide alexis beach threesome
                            show bg beach with fade
                            "Taking advantage of the fact that I'd been able to sneak up on the unpleasant scene unnoticed, I slip away in the same fashion."
                            "I don't think the full implications of what I've just seen becomes apparent until I'm back on the sand and gathering up my things."
                            "Alexis just wandered off for a bottle of water and what?"
                            "Just happened to come across a couple of dodgy-looking guys that she couldn't resist having a threesome with?"
                            "Did she plan this from the start, or was it a spur-of-the-moment kind of thing?"
                            "As I stuff my bag and start to make for the car-park, I honestly can't think which of the two would be worse!"
                            "Call me harsh for climbing into the car and driving away, for leaving Alexis alone at the beach."
                            "But with the mood I'm in right now, I don't think my sharing the ride home with her would be pleasant for anyone concerned."
                            $ alexis.flags.beach_outcome = "found_leave"
                            $ alexis.flags.ntr_conversation = "leave"
                            $ alexis.love -= 10
                        "Say something":
                            with vpunch
                            mike.say "Alexis - what in the hell do you think you're doing?!?"
                            hide alexis
                            show alexis b naked at center, zoomAt(1.1, (640, 1000))
                            "At the very same moment, all three of them freeze and look in my direction."
                            "The expressions of surprise on the faces of the two guys are quite something to behold."
                            show alexis b surprised
                            "But they pale in comparison to the look of horror I see plastered on Alexis' features."
                            "I swear that the one cock is no more than an inch into her mouth."
                            "And as for the other...well, I'd rather not know just how far that one's made it before stopping."
                            mike.say "I mean...I know WHAT you're doing."
                            mike.say "That's pretty obvious..."
                            mike.say "I suppose what I mean is WHY are you doing it?"
                            show alexis confused naked at center, zoomAt(1.25, (640, 940))
                            "For some reason, Alexis chooses this as the moment to flinch away from the proffered cocks."
                            "The sudden movement makes it look as though she's only just realised what they actually are."
                            "She covers her naked breasts with one hand as well, fumbling to pull up her swimsuit with the other."
                            show alexis whining
                            alexis.say "Shit...shit...shit!"
                            alexis.say "You weren't supposed to see any of this..."
                            show alexis sad
                            "Rather than being disappointed to have been denied their prize, the gang-bangers instead appear amused by the awkward situation."
                            "They say nothing as they slip their dicks back into their shorts."
                            "Indeed they appear to enjoy the way in which Alexis is being humiliated right in front of them."
                            mike.say "Funny, Alexis - that's just the kind of impression I got myself!"
                            hide alexis with dissolve
                            "I turn and start to stalk back to the beach, leaving her to hurry after me as she tries to make herself at least appear decent."
                            alexis.say "[hero.name]...wait!"
                            alexis.say "Don't you think we should at least talk about what just happened?!?"
                            "Even the sound of her voice makes me picture those lips, pursing as the cock comes towards them..."
                            mike.say "No, Alexis, I don't."
                            mike.say "I think we should grab our stuff and you should call a taxi to take you home."
                            mike.say "Can you manage to do that without fucking the driver, huh?"
                            "And with that, I walk off to collect my things."
                            $ alexis.flags.beach_outcome = "found_confront"
                            $ alexis.set_gone_forever()
                        "Watch":
                            "I know that I should say something, break this up before it goes too much further."
                            "But for all the horror that the sight of it inspires in me, there's an equal amount of fascination too."
                            "Maybe it's because of all the time that my mind's spent dwelling on the thought of Alexis betraying me."
                            show alexis beach threesome mike suck normal anal
                            "Or maybe I'm just a far bigger pervert than I ever imagined possible."
                            "Either way, once I pause long enough to be sure that she has a cock in her mouth and her ass, I can't keep from watching."
                            "One thing I know for certain is that it can't be lack of experience that makes me stay still and silent."
                            "I've been in the same position as each of those guys in the past, and I know just how good it feels."
                            show alexis beach threesome mike lick
                            "But somehow the sight of them basically turning Alexis into a human spit-roast between is something I can't tear my eyes away from."
                            show alexis beach threesome suck at stepback(speed=0.1, h=-10, v=-20)
                            "Neither of them is gentle, the one with his cock in her mouth thrusting suddenly and the other pushing mercilessly into her ass."
                            "And yet none of this rough treatment at both ends of her body does anything to lessen Alexis' pleasure."
                            "Indeed, she seems to positively revel in the way she's being manhandled."
                            show alexis beach threesome at stepback(speed=0.1, h=-10, v=-20)
                            "The more the one cock is forced into her mouth and the other between her buttocks, the more she seems to like it."
                            "When she isn't gagging, Alexis makes low, muffled moaning sounds around the cock she's sucking."
                            show alexis beach threesome at stepback(speed=0.1, h=-10, v=-20)
                            "Likewise, her body trembles and quivers each time the other man rams his hips against her buttocks."
                            "I can feel my mouth going dry at the same time as my cock is getting ever harder."
                            show alexis beach threesome at stepback(speed=0.1, h=-10, v=-20)
                            "I slip a hand into my shorts and begin to stroke myself as Alexis takes ever more from each man."
                            "The heat of the day and the way she's being used means that she's almost dripping with sweat by now."
                            show alexis beach threesome at stepback(speed=0.1, h=-10, v=-20)
                            "Every motion of her head and slapping of her ass sends her pendulous breasts swaying in time."
                            "And in that moment, I see beads of sweat running down them and collecting to drip from her painfully erect nipples."
                            show alexis beach threesome mike surprised cum with hpunch
                            "Then, without warning, they both cum within mere seconds of one another."
                            "Neither spares as much as a second thought for Alexis herself, simply using her as a vessel for what follows after."
                            show alexis beach threesome ahegao
                            "She chokes on the cum being spurted down her throat in one second."
                            "And then her body jerks as the muscles of her ass convulse from the same being done to it."
                            show alexis beach threesome out
                            "I see Alexis' legs buckle and then collapse beneath her as they pull out a moment later."
                            "Having got their use out of her, neither of the men as much as pauses to say a word to Alexis."
                            show alexis beach threesome -cum
                            "Instead, they seem to be amused by the sight of her as she lays there before them."
                            "Slipping their cocks back into their shorts, they wander off, laughing to each other as they go."
                            "Used, abused and then abandoned, Alexis is left in a helpless, writhing mess."
                            "Slick with a mixture of sweat and cum, she coughs and hacks until she spits out the last of what she was made to swallow."
                            "In all my life, I don't think I've ever seen a woman so utterly degraded as she is right now."
                            "And it's only when I feel myself cumming too that I realise I've been gratifying myself to the same sight the whole time."
                            hide alexis with fade
                            "Unable to make sense of the conflicting emotions that this inspires in me, I turn and hurry back to the sand."
                            "All the way I feel sure that all it'll take is one look at me for everyone to know what just took place back there."
                            "But of course, no one suspects a thing."
                            "I lay myself back down on the towel and try to regain control, waiting for Alexis to show herself again."
                            show alexis blush swimsuit with easeinright
                            "When she finally does come back, she's done a remarkable job of cleaning herself up."
                            "And from the expression on her face, I could almost believe nothing out of the ordinary took place while she was gone."
                            "If, that is, I hadn't seen it with my own eyes..."
                            show alexis talkative
                            alexis.say "You wouldn't believe the time I've had!"
                            show alexis normal
                            mike.say "Oh, really?"
                            "I glance nonchalantly at my phone and then adopt an expression of feigned surprise."
                            mike.say "Wow, Alexis - you've been gone for ages!"
                            show alexis whining
                            alexis.say "Like I don't know that!"
                            alexis.say "The place was out of water, and so I had to walk all the way to the next kiosk."
                            alexis.say "Which took all this time..."
                            show alexis annoyed
                            mike.say "You do look pretty sweaty, Alexis!"
                            mike.say "And were they out of water too?"
                            "At the reference to the suspiciously absent bottle of water she supposedly set out for, Alexis looks more than a little furtive."
                            show alexis whining
                            alexis.say "I...ah...had to drink it on the way back...sorry!"
                            show alexis sad
                            mike.say "It's okay, Alexis - you look like you needed it more than I did!"
                            "And with that, I let the matter drop."
                            "But the mere thought of Alexis, slick and crawling around in humiliation, is enough to get me hard for days afterwards."
                            $ alexis.flags.beach_outcome = "found_watch"
                            $ alexis.flags.ntr_conversation = "cheat"
        else:

            "There's no way that it should be taking her this long to grab a bottle of water and get back here."
            "Call me paranoid, but I can't help thinking that something bad might have happened to Alexis."
            "I stand up, glancing around in the vain hope that she'll appear the moment I do so."
            "But there's still no sign of her, and so I set off in the direction of the kiosk, hoping to bump into her on the way."
            "It doesn't take me long to arrive at my destination, or to see that Alexis isn't here either."
            "By now I'm beginning to get worried, and I wonder if she's walked on to another kiosk to get water instead."
            "The quickest way I know to reach the next one is the path that runs along the back of the beach-huts and in front of the dunes."
            "So I make straight for it, my head already filling with worst case scenarios as to what I might find along the way."
            "I've not gone far when I hear the sound of voices a little way off of the path."
            "Thinking that it might be Alexis, or at least someone that's seen her pass this way, I head in their general direction."
            "But as I get closer, my pace slows and I start to move as quietly as I can."
            "One reason for this is that I soon pick out two of the voices as male and pretty surly in tone."
            "The other is that I recognise the second as female, and more importantly as belonging to Alexis herself."
            "Fearing that she might be about to get mugged, or worse, I creep closer and strain to see what's happening."
            "What I do see makes me feel a surge of anger and prepare myself to come to Alexis' aid."
            show alexis beach threesome mike lick out with fade
            "She's bent over in between the two guys I could hear just now, swimsuit around her ankles and breasts exposed."
            "The guys, who look like a couple of typical gang-bangers, both have their cocks out and are clearly rather excited."
            "I'm horrified by what I see, convinced that I've stumbled upon Alexis the moment before they were about rape her."
            "But then I see her face for the first time, and notice that she's actually wearing a sultry smile."
            "Alexis licks her lips in anticipation as one cock looms towards her mouth and the other her ass."
            "Whatever the hell's going on here, it's certainly not being done against her will!"
            "I know that I should say something, break this up before it goes too much further."
            "But for all the horror that the sight of it inspires in me, there's an equal amount of fascination too."
            "Maybe it's because of all the time that my mind's spent dwelling on the thought of Alexis betraying me."
            show alexis beach threesome mike suck normal anal
            "Or maybe I'm just a far bigger pervert than I ever imagined possible."
            "Either way, once I pause long enough to be sure that she has a cock in her mouth and her ass, I can't keep from watching."
            "One thing I know for certain is that it can't be lack of experience that makes me stay still and silent."
            "I've been in the same position as each of those guys in the past, and I know just how good it feels."
            show alexis beach threesome mike lick
            "But somehow the sight of them basically turning Alexis into a human spit-roast between is something I can't tear my eyes away from."
            show alexis beach threesome suck at stepback(speed=0.1, h=-10, v=-20)
            "Neither of them is gentle, the one with his cock in her mouth thrusting suddenly and the other pushing mercilessly into her ass."
            "And yet none of this rough treatment at both ends of her body does anything to lessen Alexis' pleasure."
            "Indeed, she seems to positively revel in the way she's being manhandled."
            show alexis beach threesome at stepback(speed=0.1, h=-10, v=-20)
            "The more the one cock is forced into her mouth and the other between her buttocks, the more she seems to like it."
            "When she isn't gagging, Alexis makes low, muffled moaning sounds around the cock she's sucking."
            show alexis beach threesome at stepback(speed=0.1, h=-10, v=-20)
            "Likewise, her body trembles and quivers each time the other man rams his hips against her buttocks."
            "I can feel my mouth going dry at the same time as my cock is getting ever harder."
            show alexis beach threesome at stepback(speed=0.1, h=-10, v=-20)
            "I slip a hand into my shorts and begin to stroke myself as Alexis takes ever more from each man."
            "The heat of the day and the way she's being used means that she's almost dripping with sweat by now."
            show alexis beach threesome at stepback(speed=0.1, h=-10, v=-20)
            "Every motion of her head and slapping of her ass sends her pendulous breasts swaying in time."
            "And in that moment, I see beads of sweat running down them and collecting to drip from her painfully erect nipples."
            show alexis beach threesome mike surprised cum with hpunch
            "Then, without warning, they both cum within mere seconds of one another."
            "Neither spares as much as a second thought for Alexis herself, simply using her as a vessel for what follows after."
            show alexis beach threesome ahegao
            "She chokes on the cum being spurted down her throat in one second."
            "And then her body jerks as the muscles of her ass convulse from the same being done to it."
            show alexis beach threesome out
            "I see Alexis' legs buckle and then collapse beneath her as they pull out a moment later."
            "Having got their use out of her, neither of the men as much as pauses to say a word to Alexis."
            show alexis beach threesome -cum
            "Instead, they seem to be amused by the sight of her as she lays there before them."
            "Slipping their cocks back into their shorts, they wander off, laughing to each other as they go."
            "Used, abused and then abandoned, Alexis is left in a helpless, writhing mess."
            "Slick with a mixture of sweat and cum, she coughs and hacks until she spits out the last of what she was made to swallow."
            "In all my life, I don't think I've ever seen a woman so utterly degraded as she is right now."
            "And it's only when I feel myself cumming too that I realise I've been gratifying myself to the same sight the whole time."
            hide alexis with fade
            "Unable to make sense of the conflicting emotions that this inspires in me, I turn and hurry back to the sand."
            "All the way I feel sure that all it'll take is one look at me for everyone to know what just took place back there."
            "But of course, no one suspects a thing."
            "I lay myself back down on the towel and try to regain control, waiting for Alexis to show herself again."
            show alexis blush swimsuit with easeinright
            "When she finally does come back, she's done a remarkable job of cleaning herself up."
            "And from the expression on her face, I could almost believe nothing out of the ordinary took place while she was gone."
            "If, that is, I hadn't seen it with my own eyes..."
            show alexis talkative
            alexis.say "You wouldn't believe the time I've had!"
            show alexis normal
            mike.say "Oh, really?"
            "I glance nonchalantly at my phone and then adopt an expression of feigned surprise."
            mike.say "Wow, Alexis - you've been gone for ages!"
            show alexis whining
            alexis.say "Like I don't know that!"
            alexis.say "The place was out of water, and so I had to walk all the way to the next kiosk."
            alexis.say "Which took all this time..."
            show alexis annoyed
            mike.say "You do look pretty sweaty, Alexis!"
            mike.say "And were they out of water too?"
            "At the reference to the suspiciously absent bottle of water she supposedly set out for, Alexis looks more than a little furtive."
            show alexis whining
            alexis.say "I...ah...had to drink it on the way back...sorry!"
            show alexis sad
            mike.say "It's okay, Alexis - you look like you needed it more than I did!"
            "And with that, I let the matter drop."
            "But the mere thought of Alexis, slick and crawling around in humiliation, is enough to get me hard for days afterwards."
            $ alexis.flags.beach_outcome = "agree_ntr"
            $ game.active_date.score = 100
    $ game.room = "map"
    $ game.active_date.stay = False
    return

label alexis_nice_car:
    if alexis.love.max < 100:
        $ alexis.love.max = 100
    play sound car_door
    scene bg street at center, zoomAt(1.25, (640, 530)), dark
    show car_inside_sit at center, zoomAt(1.5, (940, 1080))
    show alexis a casual happy at flip, center, zoomAt(2.0, (640, 1340))
    with fade
    "Right from the moment I pull up and Alexis hops into the passenger seat of the car, I'm getting good vibes off of her."
    "We're driving to the beach so that we can make the most of the decent weather before it turns crappy."
    "And we already agreed that it'd be best for me to drive there and back, but whatever the reason soon slips my mind."
    "That's mainly because I keep catching the way that Alexis is stealing glances in my direction."
    "I mean, it's not like she never does that to me."
    "But right now she's positively beaming at me whenever I catch her in the act."
    "And it's actually starting to distract me from the task of driving the car."
    mike.say "Alexis..."
    mike.say "Are you feeling okay?"
    show alexis a normal
    "Alexis seems to snap out of it a little when she hears the question."
    "Like she didn't realise she was doing anything and now she's trying to cover her tracks."
    show alexis a talkative
    alexis.say "Huh?"
    alexis.say "What do you mean, [hero.name]?"
    alexis.say "I'm okay..."
    show alexis a happy
    alexis.say "I'm fine...everything's fine!"
    show alexis a smile
    "I turn my gaze back to the road, trying to take the answer at face value."
    "But it just sounds so hasty and forced that I can't help questioning it."
    mike.say "Are you sure, Alexis?"
    mike.say "Because you seem a little distracted?"
    show alexis a talkative
    show fx question
    alexis.say "I do?"
    alexis.say "Oh...well..."
    hide fx
    show alexis a happy
    alexis.say "That must be because I'm looking forward to the beach!"
    alexis.say "I can't wait to hit that golden sand and soak up some rays!"
    show alexis a smile
    "I raise my eyebrows and give Alexis a nod."
    "That certainly sounds like it makes sense."
    "Maybe I'm just reading too much into things today."
    "I do the best I can to put it out of my mind and just drive."
    "But Alexis keeps doing subtle little things that make that impossible."
    "She seems to be checking her reflection in the window a lot."
    "That and smiling at anyone and everyone who happens to be passing on the sidewalk."
    "And when we pull up at the lights, she's practically beaming at the car next to us."
    mike.say "Alexis!"
    mike.say "Are you trying to flirt with everyone out there or what?"
    show alexis a stuned
    "Alexis almost jumps in her seat at the sound of my voice."
    "Her head shoots around and then she starts to shake it in denial."
    show alexis a surprised
    alexis.say "No way, [hero.name]!"
    show alexis a happy
    alexis.say "Anyway..."
    alexis.say "I don't think it's me they're looking at!"
    show alexis a smile
    "I frown at this, not understanding what Alexis means."
    mike.say "Well I'm pretty sure it's not me they're looking at, Alexis!"
    mike.say "Most guys don't try so hard to check me out!"
    "Alexis falls silent at this, and I take it that I've called her out."
    "Satisfied that she's thinking about what she's done, I let the matter drop."
    "But oddly that doesn't seem to stop Alexis from shooting me those same looks."
    "Maybe she's trying to win her way back into my good books."
    "And I guess she knows exactly how to go about it too."
    "Because as we pull into the car park at the beach, I'm feeling good again."
    scene bg beach
    show alexis casual happy at right
    with fade
    "I find a convenient space and hop out of the car."
    "Slinging my bag over my shoulder, I turn to see Alexis still lingering by the car."
    "Then I see that she's actually running a hand over the bodywork."
    "It hits me on that moment what's been going on."
    "And I feel dumb as a post for not noticing it before now."
    mike.say "Alexis..."
    mike.say "Do you have the hots for my car?!?"
    show alexis normal blush
    "Alexis looks up and pulls her hand away like the bodywork is red hot."
    "She shakes her head instinctively at first, but then begins to nod."
    show alexis talkative
    alexis.say "Okay, okay...you got me!"
    alexis.say "I know that girls aren't supposed to like cars."
    alexis.say "We're supposed to be above all that materialistic crap."
    show alexis -blush
    alexis.say "But this is one fine-looking vehicle you've got here!"
    show alexis smile
    "I nod and smile as it all starts to make sense."
    "Alexis wasn't trying to flirt with everyone on the way here."
    "She was getting off on the amount of attention my car was getting."
    "With a shake of the head I motion in the direction of the beach."
    mike.say "Don't worry, Alexis."
    mike.say "The security system is pretty sweet too."
    mike.say "So it'll still be here when we're done with the beach!"
    "Alexis shoots me a withering look."
    show alexis at center with ease
    "But then she shrugs and starts walking towards the beach."
    hide alexis with dissolve
    "I follow, but take the time to steal one last glance back at the car."
    "I guess it was worth the money that it cost me after all."
    "Because if it can impress a girl like Alexis, the it can impress anyone!"
    $ game.active_date.score += 30
    return

label alexis_crap_car:
    scene bg street
    show alexis casual annoyed
    "Right from the moment I pull in to pick Alexis up I can tell that there's something wrong."
    "We're supposed to be going to the beach to make the most of the decent weather while it lasts."
    "And before she hopped into the passenger seat, I was feeling pretty upbeat and positive."
    play sound car_door
    queue sound car_ignition
    scene bg street at center, zoomAt(1.25, (640, 530)), dark
    show car_inside_sit at center, zoomAt(1.5, (940, 1080))
    show alexis a casual annoyed at flip, center, zoomAt(2.0, (640, 1340))
    with fade
    "But as soon as we're on our way, I'm picking up negative vibes coming from Alexis."
    "I steal a quick glance in her direction, trying to see what's the matter."
    mike.say "Alexis..."
    mike.say "Is there something wrong?"
    show alexis a confused
    "She shoots me a glance that almost feels like a slap in the face."
    "And I can see from her expression that she's far from happy right now."
    show alexis a whining
    alexis.say "What?"
    show alexis a talkative
    alexis.say "No...there's nothing wrong."
    alexis.say "I...I just feel like I forgot something, that's all."
    show alexis a annoyed
    "Alexis looks down, beginning to rummage through her bag."
    "And I take this as a good excuse to turn my attention back to the road."
    "But after a couple more minutes, Alexis seems to have forgotten all about it."
    "She starts looking out of the window at the people passing on the sidewalk."
    "Then I notice that she's sinking down in her seat whenever we stop at a light."
    "It's almost like she's afraid of being seen in the car with me!"
    mike.say "Well..."
    mike.say "Did you find it?"
    show alexis a whining
    alexis.say "Did I find what?"
    alexis.say "What are you even talking about?"
    show alexis a annoyed
    "I frown at the way Alexis just sniped at me from the passenger seat."
    "Sure, she might be annoyed at discovering that she had forgotten whatever it was."
    "But that's no reason to take it out on me!"
    mike.say "The thing you were looking for in your bag, Alexis!"
    mike.say "You just told me five minutes ago that you thought you forgot something."
    mike.say "You stopped looking, so I assumed you did forget it."
    "Alexis looks at me for a moment longer."
    show alexis a annoyed
    "Then she nods her head a little too hastily."
    show alexis a whining
    alexis.say "Yeah, yeah..."
    alexis.say "Sun cream - I did forget it!"
    show alexis a annoyed
    mike.say "No problem, Alexis."
    mike.say "You can use some of mine."
    show alexis a whining
    alexis.say "Yeah..."
    alexis.say "And I bet it's the store brand too."
    alexis.say "The cheap stuff!"
    show alexis a annoyed
    mike.say "Huh?"
    mike.say "What's that supposed to mean?!?"
    show alexis a whining
    alexis.say "Oh...nothing!"
    alexis.say "Don't listen to me."
    alexis.say "I'm just pissed with myself, that's all!"
    show alexis a annoyed
    "Alexis's explanation sounds less than convincing to my ears."
    "But I know better than to poke the bear in a situation like this."
    "So I just nod and turn my attention back to driving again."
    "It doesn't seem to help though, as the tension in the car steadily rises."
    "And by the time we pull into the car park at the beach, it reaches a head."
    scene bg beach
    show alexis casual sad
    with fade
    "The moment I stop, Alexis opens the door and hops out."
    "I'm out a second later, fists clenched and jaw set."
    "We both look ready for a fight."
    mike.say "Cut the passive aggressive crap, Alexis!"
    mike.say "What in the hell is wrong with you?!?"
    "Alexis balls her hands into fists and plants them on her hips."
    "She leans forwards to deliver her response."
    show alexis angry
    alexis.say "What's wrong with me?"
    alexis.say "Hah!"
    alexis.say "What's wrong with you - driving around in that piece of crap?!?"
    show alexis upset
    mike.say "You...you mean my CAR?!?"
    show alexis angry
    alexis.say "Yeah I mean your car, [hero.name]!"
    alexis.say "It's a pile of crap that belongs in the junkyard!"
    alexis.say "And I don't want to be seen in it again!"
    show alexis upset
    mike.say "You mean you'd rather walk home than ride in it?"
    show alexis confused
    "The reality of the situation seems to suddenly dawn on Alexis."
    "For a moment I think that she's going to relent."
    "But then I see the muscles of her jaw twitch and tighten."
    show alexis angry
    alexis.say "Yeah - I just might do that!"
    show alexis upset
    mike.say "Fine by me, Alexis!"
    mike.say "Happy to let you!"
    hide alexis with dissolve
    "With that, Alexis turns her back on me and stalks off towards the beach."
    "I wait a few seconds for effect, then hurry after her."
    "Who knows, maybe she'll get over it if I leave her to sulk a little?"
    "If not, this is going to be one awkward day at the beach!"
    $ hero.cancel_activity()
    $ game.active_date.stay = False
    return

label alexis_event_06:
    if alexis.love.max < 120:
        $ alexis.love.max = 120
    "One thing that's changed since the last time that Alexis and I were together is the amount of time that we spend just talking."
    "I guess it's a symptom of us being older now, that we'd probably have been doing something physical instead in our younger days."
    "Not that we don't do that kind of thing any more, you understand?"
    "It's that the more life experience you accumulate, the more you have to talk about."
    "But for all of that, there are still some things that have remained a kind of unspoken taboo between us."
    "The most obvious of these is, of course, the unpleasant subject of how our relationship came to an end the first time round."
    "Though we don't mention it, it's always there, hanging over us - the elephant in the room."
    "That's why it catches me completely off guard when Alexis simply comes out and mentions it as we're chatting about something else entirely..."
    show alexis sad
    alexis.say "[hero.name], I know you're not going to want to hear this."
    alexis.say "But I think that, if we're seriously going to make this work between us a second time - we need to talk about it..."
    "I don't reply straight away, instead nodding slowly in order to buy myself just a little more time."
    "She doesn't need to come right out and name what she's talking about, of course."
    "But I think we've both been putting this off for as long as possible, each waiting for the other to broach the subject."
    mike.say "Okay, Alexis - if you think it's time?"
    "There's doubt in her expression, but still she shakes her head and presses on."
    alexis.say "I...I don't know about that."
    alexis.say "I don't know if there is a good time."
    alexis.say "Just that if we don't, it'll always be holding us back!"
    "Okay, here goes nothing!"
    "I take a deep breath and begin talking, if only for the sake of getting things started."
    mike.say "I don't know where we begin with this one, Alexis."
    mike.say "But I guess for me it was the pain of what happened, the betrayal."
    mike.say "That was the heart of it."
    "I look at her with a painful smile on my face, seeing her nod at my words."
    "Despite all the memories and the old feelings, it does help to know that she acknowledges my pain."
    mike.say "But it's not like I want an apology, or an explanation, Alexis."
    mike.say "It was so long ago that none of that stuff matters to me anymore."
    "Shrugging my shoulders, I let out a long sigh."
    mike.say "If you're over it, then I suppose I am too."
    menu:
        "Tell her you forgive her":
            mike.say "I forgive you, Alexis."
            mike.say "All I want now is to just be with you."
            show alexis cry
            "I'm honestly expecting that to be the end of it, me telling her that I forgive her cheating on me."
            "But almost as soon as I've finished speaking, I see that she's not in the least bit relieved by what I've said."
            mike.say "Alexis, what is it?"
            mike.say "Please, you can tell me anything...anything at all!"
            mike.say "We've all made mistakes in the past, but you can't beat yourself up forever..."
            "It's only now that I can see the tears beginning to well in the corner of her eyes."
            "She lets out a desperate sob, wiping at the tears with the back of her hand."
            alexis.say "You forgive me, huh?"
            alexis.say "Wow...that makes it all better then!"
            "The bitterness in her voice is unexpected, catching me off guard."
            mike.say "Huh..."
            alexis.say "I...I didn't cheat on you, [hero.name]!"
            mike.say "What are you saying, Alexis?"
            mike.say "That you DIDN'T have sex with Mr Blank?"
            $ alexis.love -= 20
            alexis.say "Jesus - can't you figure it out?"
            alexis.say "He RAPED me, you stupid bastard!"
            alexis.say "I had no choice...because he raped me!"
        "Let her talk" if hero.charm >= 50:
            "I hold my peace, sensing that Alexis needs to unburden herself."
            alexis.say "No, [hero.name], I'm not over it."
            alexis.say "And I don't know if I ever will be, either."
            "I make to say something, but the words won't come to me."
            "The puzzlement must be plain to see on my face, as Alexis shakes her head at me."
            alexis.say "Maybe you were wrong, [hero.name] - maybe you do need it explained to you."
            "She smiles, despite the tears already welling in the corner of her eyes."
            alexis.say "I couldn't tell you at the time, because it was too raw."
            alexis.say "But I should have done so, and much sooner than this."
            "I want to say something, ask any number of questions."
            "But I remain silent, sensing just how much this is costing her to say out loud."
            alexis.say "I never cheated on you, [hero.name] back then, not once."
            alexis.say "And I never would have, if I'd been given a choice..."
            "Alexis leaves the last statement hanging, and my mind racing towards an awful truth."
            "I look at her in unbelieving amazement, trying to comprehend the implications of what she means."
            show alexis cry
            alexis.say "Yeah, you just got it, didn't you?"
            alexis.say "Technically, I did have sex with another man."
            alexis.say "But not out of choice."
            alexis.say "He raped me, [hero.name] - the bastard raped me!"
    show alexis sad
    "My head is spinning with the revelation of what Alexis just told me, a fact that potentially changes everything."
    "All these years I was convinced that she'd thrown our relationship away for the sake of some tawdry pleasure."
    "And now it turns out that she was actually the victim of a disgusting piece of shit in a position of trust."
    "If what she says is true, then I've been deluding myself for more than a decade!"
    menu:
        "Don't believe her" if alexis.flags.caughtCheating:
            mike.say "Nice try, Alexis, nice try."
            "Alexis shakes her head as she hears the ironic amusement in my voice."
            alexis.say "What...what are you talking about?"
            mike.say "I honestly thought that you'd changed, Alexis."
            mike.say "And you have - but only in as much as you've gotten to be a better liar."
            alexis.say "No, [hero.name], it's the truth!"
            mike.say "Oh come on, Alexis, just stop it."
            mike.say "You nearly had me there, but stop it before you look pathetic."
            alexis.say "[hero.name], please - why are you doing this?"
            mike.say "Because I'm tired of you manipulating me with your lies, Alexis!"
            mike.say "You ruined what we had the last time by cheating on me."
            mike.say "And now, when I say that I forgive you, what happens?"
            show alexis cry
            "Alexis shakes her head again."
            "But whether it's in answer to the question or to disagree altogether, I can't tell."
            mike.say "What happens is that you invent a story about it being a rape, that's what!"
            mike.say "You turn the time when you betrayed me into a way to make me feel guilty."
            mike.say "And by magic, something you should be grovelling for becomes something to make me do it instead!"
            alexis.say "No...you've got it all wrong!"
            mike.say "If I have, then I'm really happy to be wrong, Alexis!"
            "And with that, I turn my back on her and walk away."
            $ alexis.love -= 50
        "Believe her":
            mike.say "God, Alexis..."
            mike.say "I feel like such a fool."
            mike.say "I should be the one apologising to you!"
            "Alexis shakes her head, but I can see that she appreciates the sentiment of my words."
            mike.say "All those years you had to carry that secret inside of you..."
            mike.say "Can you forgive me?"
            "Alexis is crying freely now, barely able to wipe away the tears."
            alexis.say "I don't need to forgive you, [hero.name]."
            alexis.say "Just to know that you believe me."
            "I nod at this, wrapping my arms gently around her."
            mike.say "You don't have to carry it around any longer, Alexis."
            mike.say "I think I understand everything a whole lot better now."
            mike.say "I just wish I'd been the kind of guy that you could let in on this back then."
            "Alexis lets out a tiny chuckle as she lays her head against my shoulder."
            alexis.say "Just be that kind of guy now."
            alexis.say "That's all I ask!"
            $ alexis.flags.rapeConfession = True
            $ game.flags.hirePI += 1
    return

label alexis_event_07a:
    play sound cell_vibrate
    "I feel my phone buzzing in my pocket."
    "A quick glance tells me it's the investigator."
    $ result = renpy.call_screen("smartphone_choice", "Investigator")
    if not result:
        $ hero.cancel_event()
        return
    "I answer it quickly, as this could be important."
    "Investigator" "Good to talk to you again, Mister [hero.family_name]."
    "Investigator" "It didn't take much digging for me to find your Mr Blank."
    "Investigator" "But then he's not exactly been in hiding since he retired."
    "Investigator" "You might have found him yourself with a little time spent on the internet!"
    mike.say "No way - I have a respectable job and an image to maintain as an upstanding member of the community."
    mike.say "That's why I hired you!"
    "Investigator" "Okay, putting that all aside for a moment..."
    "Investigator" "He moved just out of town when he retired, to one of those gated communities up in the hills."
    "Investigator" "His routine's pretty much set in stone, and I made a note of it in my report."
    "A picture appear on my phone's screen..."
    "Investigator" "Is this the man you're looking for?"
    "Investigator" "Do you recognise him?"
    mike.say "That's him."
    mike.say "I'm sure of it."
    "Investigator" "Okay - that my work here is technically done..."
    "Investigator" "But, I would like to say, in an unofficial capacity, that I think you should consider getting the authorities involved."
    "Investigator" "And I certainly suggest that you don't go taking matters into your own hands."
    "I hang up, very much decided to not follow that advice."
    mike.say "Long time coming that someone took you off of the team, Coach Blank."
    mike.say "Took you off of the team and retired you for good!"
    return

label alexis_event_07b:
    if alexis.love.max < 140:
        $ alexis.love.max = 140
    $ alexis.flags.policestation = False
    show bg policestation
    show alexis sad
    "While I've watched enough cop dramas and movies in my time, I still have no idea of just how this is going to go."
    "I'm also painfully aware of how much persuasion and cajoling that it took to get Alexis to agree to this."
    "And so I'm trying to be on my best behaviour as we walk into the police station together, the perfect supportive partner."
    "But all the same, no matter how much I keep nodding, smiling and offering reassurance, she still seems on edge."
    "Luckily for us, when we walk in, the front desk is pretty much deserted apart from the officer on duty."
    "As there's nobody in front of us and no other distractions in sight, we shuffled awkwardly towards the desk."
    "The officer looks up as we approach, nodding in that odd way that only the police are able to manage."
    "It's neither friendly nor hostile, but at the same time also somehow demands to know what the matter is, and quickly."
    "Policeman" "Good morning."
    "Policeman" "Can I help you with anything?"
    alexis.say "I...I wanted to..."
    "The officer's eyebrows begin to rise as Alexis loses her nerve."
    mike.say "My girlfriend...I mean, my partner...wanted to report a crime."
    "The officer looks at me and then at Alexis, as if asking whether or not she can speak for herself."
    alexis.say "He's right...he's right."
    alexis.say "I want to report a crime."
    "I see the officer begin to reach for a pile of forms behind the desk and a pen."
    mike.say "It's serious...the crime."
    mike.say "It's very serious and sensitive in nature."
    "Alexis nods at this, suddenly seeming to understand my objection."
    alexis.say "Yes, it is."
    alexis.say "Could we speak to someone?"
    alexis.say "Maybe somewhere in private?"
    "The officer is obviously no bumbling clod, as this almost instantly receives a curt nod."
    "Policeman" "Of course, I understand completely."
    "Policeman" "Take a seat and someone will be down to see you shortly."
    "Alexis and I do as we are told, waiting in an uncomfortable silence for what feels like an age."
    show alexis at left
    show inspector at right
    "Inspector" "Erm...you two would be the folks wanting to talk in...ah, private?"
    "I honestly don't know what I'd been expecting, in terms of just who we'd be talking to."
    "But the sight that greets me is not one that instantly fills me with confidence."
    "Standing before us is a short, slightly dishevelled-looking man in his middle years."
    "He wears a raincoat over a shabby suit and looks like his hair hasn't seen a comb in a long time."
    "Inspector" "Ah, let me introduce myself."
    "Inspector" "I'm Detective Michaels."
    "He smiles as he pats the pockets of his coat and rummages through those inside of his jacket."
    "And then her shrugs, as if admitting defeat."
    "Michaels" "I'd show you my ID...but I seem to have temporarily mislaid it!"
    "Alexis and I can't help staring at each other, both wondering if this guy is for real."
    "Michaels" "You must be Alexis and [hero.name]?"
    "He points at each of us in turn, receiving nods as he goes."
    "Michaels" "Great - follow me."
    "And before we can say a word, he turns and walks off down the corridor, expecting us to follow."
    "Alexis and I hop up and hurry after him, unable to think of anything else to do."
    "Michaels leads us to an interview room, well away from the front of the station."
    "Michaels" "Please, take a seat."
    "We do as we're told, still not fully able to take this shambling figure seriously."
    "Michaels" "Now I take it that you have something, erm...serious, to report?"
    "Alexis looks at the detective and then at me, receiving a nod to begin her story each time."
    alexis.say "Yes...yes, I do..."
    "Michaels" "But let me guess now - you're afraid to tell me?"
    alexis.say "It's...it's been a long time since it actually happened..."
    "Michaels" "And you think that because it was a long time ago, someone like me's not going to believe you, correct?"
    "Alexis nods, still looking nervous, but relieved all the same."
    alexis.say "Well...yes."
    "At this the detective smiles, broadly and with visible sympathy."
    "His formerly unimpressive features become warm and extremely reassuring."
    "Maybe I was too harsh in my initial assessment of this guy after all."
    "Michaels" "Miss, my wife said to me the other day that if you can't forget a thing, then there's a reason for it."
    "Michaels" "But maybe the best thing would be for you to just tell me what brought you here, and then we can decide."
    "Michaels" "What do you think of that?"
    "Alexis nods, unable to keep from smiling at the detective's odd mannerisms."
    alexis.say "Okay...okay, give me a second to get my head straight."
    "She takes a deep breath, lets it out in one slow motion, and then she begins."
    alexis.say "It...happened when I was in high-school, the thing."
    alexis.say "The gym teacher...the coach, he..."
    "Michaels says nothing, merely nodding and making affirmative noises as he writes in his careworn notebook."
    show alexis cry
    alexis.say "Raped me..."
    alexis.say "He raped me."
    "The first time she actually says the words, she sounds shaky and terrified."
    "But on the second, a new-found confidence seems to have crept into Alexis' voice."
    "Michaels" "I see now why you were so nervous, Miss."
    "Michaels" "But if you feel that you're able, would you mind telling me more?"
    "Alexis nods, and returns to her story."
    alexis.say "His name was Blank, and he used to turn up when there was no one else around."
    alexis.say "I don't know if I was the only one he hurt, but I wouldn't be surprised if I wasn't."
    "Michaels nods again, looking up from his notes."
    "Michaels" "Okay, that all seems to be in order."
    "Michaels" "Oh, there was one more thing I wanted to ask - were you two a couple back then, as well as now?"
    "Alexis and I exchange surprised looks, as neither of us mentioned our relationship even once."
    mike.say "Erm..yeah, we were together when it happened."
    alexis.say "But we broke up afterwards, and we only just got back together."
    "Michaels shakes his head, looking sympathetic and rueful at the same time."
    "Michaels" "And you only got around to telling this young man recently, didn't you, Miss?"
    "Alexis nods, looking even more surprised than before."
    hide inspector
    show inspector close
    "Michaels" "When you've been in this job as long as I have, you kind of learn how to read people."
    "With that, he stands up and motions towards the door."
    "Michaels" "That's all for now, but I'll be in touch if I need anything more from you."
    "Michaels" "In the meantime, here's my card."
    "Michaels" "Don't hesitate to call me if you remember anything else, anything at all."
    "Michaels hands a dog-eared card to Alexis as he ushers us out of the interview room."
    "Alexis is quiet on the way home, but then she has a hell of a lot to think about."
    "For my part, I choose to respect her silence."
    "Not least because my own mind is spinning too."
    "And although it was all my idea, I'm not totally sure it was the right thing to do after all..."
    return

label alexis_event_08a:
    show bg alley
    "Furnished with all of the information that the private investigator was able to provide me, finding Mr Blank was never going to be a problem."
    "Rather what causes me an issue as I drive to the place where I know he'll be, is the actual act of physically confronting him."
    "Up until now, I've not put much coherent thought into what I want to come out of this confrontation with my former gym teacher."
    "All that's been fuelling me is my anger at learning the truth behind Alexis' supposed cheating and his role in the same."
    "Why am I actually so determined to look this guy in the face and accuse him of raping her after all these years?"
    "It's not that I doubt Alexis is telling the truth."
    "And it's not as if forcing him to admit as much will change anything."
    "So the only explanation I can come up with is the most simple and least sensible one of all."
    "I suppose that I want to hurt the guy as much as I possibly can."
    "That and make myself feel better in the act..."
    "All of this is still turning over in my mind when I see Blank across the street."
    show blank
    "Without thinking, I pull over and jump out of the car, crossing the road to catch up to him."
    mike.say "Hey, you...hey, Blank!"
    "At the sound of his voice, Blank turn slowly to regard me."
    "The look on his face is one of mild puzzlement, with no sign whatsoever of anger or irritation."
    "Mr Blank" "Yeah, that's me alright."
    "Mr Blank" "And who might you be?"
    "Jesus Christ - up close and in person he's even uglier than the pictures that the private investigator showed me."
    "But then maybe my impression of him is being twisted by what I'm about to accuse him of having done to Alexis."
    mike.say "You won't remember me, but I remember you."
    mike.say "You took gym at my high-school."
    "A look of recognition dawns on his coarse features, and he actually half cracks a smile."
    "But then why wouldn't he?"
    "For all he knows, I'm just some random ex-pupil that's recognised him, totally out of the blue."
    "Mr Blank" "Huh...if you say so, son."
    "Mr Blank" "I've been retired so long now that I don't remember much from back then."
    mike.say "Is that so?"
    mike.say "Maybe you remember some of the other kids in my year?"
    mike.say "How about...Alexis...do you remember her?"
    "Blank blows out his cheeks at the mention of the name, his thick lips rasping unpleasantly as he does so."
    "Mr Blank" "Can't say that I do!"
    mike.say "No, really...try harder with that particular name."
    "At my sudden insistence, his expression turns a shade darker."
    "He frowns, as if he senses that something's suddenly changed in the tone of our conversation."
    "Mr Blank" "And what, pray tell, would make me remember her in particular?"
    "My voice drops to an angry hiss as I spit my answer in his direction."
    mike.say "Because you raped her, you sick sack of shit!"
    "Blank stares at me for what feels like the longest time, silent and his face unchanging."
    "I'd expected him to swing for me, or at the very least deny the accusation as soon as it was made."
    "But this silence is unnerving, and I get the distinct impression that he's sizing things up, coldly and without emotion."
    "Mr Blank" "Now those are the faces I DO remember, even after all these years."
    "Mr Blank" "But not that one - I think of the name and there's nothing at all."
    "Mr Blank" "Must mean that she wasn't anything that stuck in there."
    "He taps the side of his bald skull with one meaty finger."
    "Mr Blank" "Must mean that she was nothing special..."
    "I don't know which of the admissions that he just made is the one that makes me throw the first punch."
    "Maybe it's the casual way he just revealed that Alexis wasn't his only victim."
    "But more likely it's the fact that he dismissed her in the next breath."
    "Something that's caused her a lifetime of trauma and turned her into a shadow of the person she could have been."
    "And to him, it's nothing more than another notch on his belt."
    mike.say "You BASTARD!!!"
    menu:
        "Use a baseball bat" if "baseball_bat" in hero.inventory:
            "Sure, I might have lashed out in anger and without thinking it through."
            "But I've been in enough fights and picked up enough skills to be able to back it up."
            hide blank
            show coach fight baseball
            "Though my first blow is only enough to graze Blank's jaw and send him staggering backwards, the second hits him right in the face."
            "I don't give him the space to react, and that rewards me with the sound of something breaking as I hammer the bat into his nose."
            "I can see that he wants to put a hand to the wound, to inspect the damage."
            "But he hesitates, aware of the danger in letting down his guard long enough to do so."
            "Unfortunately for Blank, this pause lets ram the tip of the bat into his gut."
            "And while he's thick around the middle, it seems that most of it's blubber."
            "He groans and doubles over from the blow, looking and sounding like he's having a seizure of some kind."
            "The fat old piece of shit staggers forwards, still bent at the waist and gasping for breath."
            mike.say "What's up, Blank?"
            mike.say "You lost your tongue, or swallowed it?"
            "Another blow to the side of his head is enough to make Blank sink to his knees."
            mike.say "I'd ask how it feels to be the one on your knees for a change."
            mike.say "But the idea of you in that situation makes me want to puke."
            mike.say "How about you?"
            "I follow this with a nasty kick to his gut, and then another."
            mike.say "How about now, Blank?"
            mike.say "You going to puke yet, huh?"
            "Blank says nothing, but collapses onto his side, clutching his belly and moaning in pain."
            "I'm about to swing the bat at him again, this time to the side of his melon head."
            "But then I stop myself, seeing the genuine fear in his eyes as he begins to cower away from me."
            "Don't hear that and assume that I'm feeling mercy or sympathy for him."
            "And I'm not, even for a moment, worried about becoming just like him either."
            "That's the kind of bullshit they put in movies and soap operas!"
            "No, all that stops me is the thought that I might actually kill him."
            "Which would mean that he was not living with the pain off the beating I just gave him."
            "Or secure in the knowledge of why he was on the receiving end of it."
            hide coach
            "With the bat slung over my shoulder, I'm all ready to leave Blank writhing on his belly in the street."
            "But then the thought occurs to me that I should really take a trophy, something to prove my victory."
            "Don't worry - I'm not talking about taking his head or scalp, nothing crazy like that!"
            "In the end I just pull out my phone and snap a couple of pictures showing the mess I made of him."
            "That should be enough for a memento and proof of the deed having been done."
            mike.say "If I ever see your face again, or hear that Alexis has too..."
            "I leave the threat hanging over him, spit in his face, and then walk away."
            $ alexis.flags.coachVictory = True
            $ alexis.flags.coachBatte = True
        "Fight bare handed":
            if hero.fitness <= 25:
                "It doesn't take me long to realise that attacking in anger and without a plan is a bad idea."
                "The first punch lands, as Blank's unprepared and taken by surprise."
                "But it just grazes his jaw, sending him staggering backwards so that he now has space to react."
                "He might well be old and far past his prime, but that doesn't mean Blank's got one foot in the grave just yet."
                "Instinctively he comes out swinging, adopting a habitual boxing stance and advancing on me now."
                hide blank
                show coach fight lose
                "One heavy fist after another hits home, and it feels like there's nothing I can do to stop them."
                "Where I'm angry and not thinking straight, he's cold and has not a thing to prove to himself."
                "He catches me once on the jaw, and I feel my knees almost buckle from the effects of the blow."
                "Blank must have seen it too, as he doesn't hesitate to hammer another home on the other side of my skull a moment later."
                "The I really do go down, collapsing to the ground as the world begins to spin around me."
                "Blank follows up with one vicious kick to my stomach, enough to make sure I have no hope of getting up."
                "He's saying something as he stands over me, but my senses are too scrambled to have a hope of understanding."
                hide coach
                "I barely realise that he's turned his back on me and walked away a moment later."
                "And it's quite some time before I can pick myself up and stagger back to my car to lick my wounds."
            else:
                "Sure, I might have lashed out in anger and without thinking it through."
                "But I've been in enough fights and picked up enough skills to be able to back it up."
                hide blank
                show coach fight win
                "Though my first punch is only enough to graze Blank's jaw and send him staggering backwards, the second is right behind it."
                "I don't give him the space to react, and that rewards me with the sound of something breaking as I hammer him square in the nose."
                "I can see that he wants to put a hand to the wound, to inspect the damage."
                "But he hesitates, aware of the danger in letting down his guard long enough to do so."
                "Unfortunately for Blank, this pause lets me punch him in the gut."
                "And while he's thick around the middle, it seems that most of it's blubber."
                "He groans and doubles over from the blow, looking and sounding like he's having a seizure of some kind."
                "The fat old piece of shit staggers forwards, still bent at the waist and gasping for breath."
                mike.say "What's up, Blank?"
                mike.say "You lost your tongue, or swallowed it?"
                "Another punch to the side of his head is enough to make Blank sink to his knees."
                mike.say "I'd ask how it feels to be the one on your knees for a change."
                mike.say "But the idea of you in that situation makes me want to puke."
                mike.say "How about you?"
                "I follow this with a nasty kick to his gut, and then another."
                mike.say "How about now, Blank?"
                mike.say "You going to puke yet, huh?"
                "Blank says nothing, but collapses onto his side, clutching his belly and moaning in pain."
                "I'm about to lay another kick into him, this time to the side of his melon head."
                hide coach
                "But then I stop myself, seeing the genuine fear in his eyes as he begins to cower away from me."
                "Don't hear that and assume that I'm feeling mercy or sympathy for him."
                "And I'm not, even for a moment, worried about becoming just like him either."
                "That's the kind of bullshit they put in movies and soap operas!"
                "No, all that stops me is the thought that I might actually kill him."
                "Which would mean that he was not living with the pain of the beating I just gave him."
                "Or secure in the knowledge of why he was on the receiving end of it."
                "I'm all ready to leave Blank writhing on his belly in the street."
                "But then the thought occurs to me that I should really take a trophy, something to prove my victory."
                "Don't worry - I'm not talking about taking his head or scalp, nothing crazy like that!"
                "In the end I just pull out my phone and snap a couple of pictures showing the mess I made of him."
                "That should be enough for a memento and proof of the deed having been done."
                mike.say "If I ever see your face again, or hear that Alexis has too..."
                "I leave the threat hanging over him, spit in his face, and then walk away."
                $ alexis.flags.coachVictory = True
    return

label alexis_event_08b:
    if alexis.love.max < 160:
        $ alexis.love.max = 160
    "A couple of days have passed since I managed to convince Alexis to come with me to the police station."
    "She was reluctant at first, but once she agreed to report what Coach Blank had done to her, that set the wheels in motion."
    "But since then, neither of us has as much as brought the subject up in casual conversation."
    "And the interview left us both feeling like the last thing we wanted was to discuss it at length and in great detail."
    "So the matter hasn't come up since we left it in the capable hands of detective Michaels."
    "He also gave his contact details to Alexis, rather than me."
    "Which means that if he did call her or she chose to contact him, I have absolutely no way of knowing, save for asking outright."
    "And I just don't feel like that would be the right thing to do, what with the weight of the situation right now."
    "The first thing I know about how the case against Blank is progressing hits me right between the eyes."
    show bg alley
    show blank
    show tv overlay
    "As Alexis and I are watching the local news one evening, I see footage of Blank flash up on the screen in front of me."
    "He's being roughly handled by a pair of uniform police officers, and apparently none too pleased with the fact."
    "While the footage keeps on running, showing Blank being tackled to the ground, the anchor reels off the story."
    "News anchor" "And in other news, a former high-school gym teacher, who cannot be named for legal reasons, was arrested today."
    "News anchor" "Police were unable to release any specific details, but did comment that this arrest is the result of a long-running investigation."
    show blank at left
    show inspector close behind tv
    "The image on the screen changes to a close-up of Detective Michaels."
    "He smiles awkwardly as microphones are thrust in his face and blinks at the flashing of cameras."
    "Inspector" "Ah, all I can say is that we've been after this creep for some considerable time."
    "Inspector" "But we recently had a breakthrough when a new accuser came forward and gave us just what we needed to nail him."
    "Inspector" "Now we're looking at a considerable number of other possible victims as a result of this..."
    scene bg livingroom
    show alexis sad
    "I look around, surprised to see that his words have been cut off by Alexis turning of the TV."
    mike.say "Don't you want to hear what he has to say?"
    mike.say "I mean, this is good...right?"
    show alexis normal
    "Alexis sighs, shaking her head as if she honestly doesn't know what to think."
    alexis.say "Yeah, of course it's good."
    alexis.say "But it's not like some kind of magic cure, you know?"
    "At first I feel a little shocked to hear her say that, and a bit frustrated after all the effort and emotion involved."
    "But then I remember that this was never supposed to be about me and my anger towards Blank."
    "It's all about Alexis, doing what I can to help her heal and move on from what that bastard did to her."
    mike.say "I guess this is bigger for you than just getting the guy banged up?"
    mike.say "So it'll take more than that to help you heal?"
    "Alexis lets out a rueful little chuckle and shakes her head."
    alexis.say "You'd think that, yeah."
    alexis.say "But I think I was already on the way to healing before you convinced me to go to the cops."
    alexis.say "This is just kind of like the icing on the cake."
    mike.say "You mean..."
    alexis.say "I mean you'd already helped me to start healing, [hero.name]."
    alexis.say "If not, I'd never have let you talk me into any of that."
    show alexis kiss casual
    $ alexis.flags.kiss += 1
    "She gestures at the TV, and then presses herself against me, nestling into my embrace."
    "I can't help smiling as I put my arms around Alexis and pull her more closely towards me."
    "It's been a long and very winding road to get here from the two dumb kids we used to be in high-school."
    "But I'm finally starting to think that we're actually exorcising the demons of the past."
    "And our future together could be the best thing to happen to us yet."
    return

label alexis_event_09a:
    if alexis.love.max < 160:
        $ alexis.love.max = 160
    alexis.say "[hero.name]...[hero.name]!"
    mike.say "Over here, Alexis!"
    "As she hurries over to me, the local news is playing on the TV."
    "At the mention of a few familiar place names, we both glance up and see what the story's about."
    if alexis.flags.coachVictory == True:
        "News anchor" "A man named locally as Oswald Blank, a retired high-school gym teacher was reportedly attacked in the street yesterday afternoon."
        "An image flashes up on the screen, showing the extent of the injuries that I must have inflicted on Blank in the fight."
        if alexis.flags.coachBatte == True:
            "News anchor" "Witnesses claim that Mr Blank was set upon and battered repeatedly with a baseball bat during the attack, the assailant then fleeing the scene of the crime."
        else:
            "News anchor" "Witnesses claim that Mr Blank was set upon and beaten up during the attack, the assailant then fleeing the scene of the crime."
        "News anchor" "Police are appealing for any witnesses to come forward with information on the incident."
    else:
        "News anchor" "A man named locally as Oswald Blank, a retired high-school gym teacher was reportedly attacked in the street yesterday afternoon."
        "An shot of Blank that must be twenty years out of date flashes up on the screen, beside what I guess must be an artists impression of me!"
        "News anchor" "Despite the fact that his assailant was allegedly armed with a baseball bat, Mr Blank managed to valiantly defend himself against the attack."
        "News anchor" "Police are appealing for any witnesses to come forward with information on the incident."
    alexis.say "Oh god, what have you done?"
    mike.say "Hey, Alexis..."
    mike.say "I'm gonna be okay, I think..."
    mike.say "But you should see the state Blank is in!"
    "Alexis is far from amused by my poor attempt at humour, and plants her hands firmly on her hips."
    alexis.say "I can't believe you'd actually do something like this!"
    alexis.say "I let you into my confidence about what happened to me, and what do you do?"
    alexis.say "You run off to confront him like...like some kind of crazy vigilante!"
    "Alexis' face is a portrait of righteous anger that's pointing in my direction."
    "But there's also pain in her expression, and not a little fear too."
    if alexis.flags.coachVictory == True:
        "Now that it's all said and done, I can finally see what I chose to do from her perspective."
        "What did I think I was going to achieve by tracking down the man that assaulted her and beating him senseless?"
        "It hasn't undone what happened to her, and it doesn't seem to have eased her pain at all either."
        if alexis.sub.max < 100:
            $ alexis.sub.max = 100
    else:
        "Now the fight is over, I can finally begin to see what happened to Alexis from her perspective."
        "I haven't managed to make anything right, in fact I've let Blank hurt another person that she cares about."
    mike.say "I'm sorry, Alexis."
    mike.say "It wasn't my right to do that in your name."
    mike.say "I just...just wanted to make him pay, that's all."
    "Alexis narrows her eyes, studying me intently."
    alexis.say "Make him pay for what, exactly?"
    "I get the distinct feeling that the next words out of my mouth are going to be scrutinised in immense detail."
    "The obvious temptation would be to say that I did it to make Blank pay for raping Alexis."
    "But she's never as much as hinted at the fact that she wanted that kind of revenge for herself."
    "And so, for better or worse, I resolve to be as honest and open as I can be."
    mike.say "To pay for making me hate you, Alexis."
    mike.say "For making me hate you when he was the one that deserved to be hated."
    mike.say "It was because of him and my own stupidity that I lost you once."
    mike.say "And now I'm afraid that he's going to make me lose you a second time!"
    "Alexis looks at me with genuine surprise in her eyes, as though she was not expecting to hear me say as much."
    alexis.say "No, [hero.name] - there's no way he's going to do that!"
    alexis.say "That bastard doesn't hold any power over me now, not anymore."
    alexis.say "The only way this ends is if one of us chooses to end it, okay?"
    "I nod in agreement, not wanting to poke the dragon any more than I already have done."
    alexis.say "But all of that doesn't mean that I'm not mad at you."
    alexis.say "Because I am, okay?"
    "I nod again, sensing that there's a relief hiding just under the surface of Alexis' apparent annoyance at me."
    alexis.say "Just do me a favour, and don't go doing something like this again!"
    "I nod for a third time, genuinely relieved at this last demand."
    "As it's not like I was planning on adopting the life of a vigilante anyway!"
    return

label alexis_event_10:
    show alexis happy
    "I have no idea why she's doing it, but Alexis just won't shut the hell up about high school."
    "She keeps on bringing it up in conversation, no matter how far removed it is from what we're talking about."
    "Retelling old stories and asking me if I remember some random person that was in our year group."
    show alexis normal
    "It's starting to bug me, because I didn't have the best time in high school, you know?"
    "Plus Alexis and I had our own set of personal issues back then too."
    "So it's not a period of my life that I like to spend time dwelling on."
    show alexis happy
    "Eventually I just feel like I have to come out and say something, before I go crazy."
    mike.say "Alexis..."
    mike.say "Do me a favour, yeah?"
    show alexis normal
    show fx question
    alexis.say "Ah...sure, [hero.name]."
    alexis.say "What is it?"
    hide fx
    mike.say "Shut the hell up about high school!"
    show alexis annoyed
    alexis.say "Huh?"
    alexis.say "Was I talking about it that much?"
    "I roll my eyes and let out a groan at this."
    "It's pretty obvious that Alexis is trying deny it."
    "She knows full well what she was doing until I called her on it."
    mike.say "Alexis, please!"
    show alexis confused
    mike.say "You haven't shut up about it all day."
    mike.say "So tell me - what's it all about?"
    "For a moment I think that Alexis is going to deny it all over again."
    show alexis annoyed
    "But then she sighs and shakes her head, admitting defeat."
    alexis.say "Okay, [hero.name], you got me!"
    alexis.say "I was trying to put an idea in your head, okay?"
    alexis.say "It's our high school reunion next Saturday."
    alexis.say "And I REALLY want to go!"
    alexis.say "But I was sure that if I just straight up asked, then you'd say no."
    "High school reunion?"
    "Has it really been that long since we graduated?"
    "Man, that makes me feel so old!"
    "Alexis seems to take my silence for me thinking it over."
    "She keeps quiet for a little while."
    show alexis normal
    "But soon she can't keep from pressing me for an answer."
    alexis.say "So?"
    alexis.say "What do you think?"
    alexis.say "Don't you want to see how everyone is?"
    alexis.say "Show them what you've made of yourself too?"
    menu:
        "Accept":
            "At first I reject the idea out of hand."
            "I hated high school, it was hell for me."
            "But then I start to think about what she's saying."
            "I think I turned out pretty well, even after all that shit."
            "Maybe it is time that I faced some of those demons from my past?"
            "And I'll have Alexis on my arm too, which can only be a good thing!"
            mike.say "Okay, Alexis."
            mike.say "Let's go to the reunion."
            mike.say "Let's show everyone that we've made a success of our lives!"
            show alexis happy
            "Alexis claps her hands together in approval."
            "And the smile on her face makes me sure I'm doing the right thing."
            alexis.say "That's the spirit, [hero.name]!"
            alexis.say "Show everyone you're not the loser they always thought you were!"
            mike.say "Wait...what?!?"
            mike.say "People thought I was a loser back then?!?"
            show alexis normal
            show fx drop
            alexis.say "Erm..."
            alexis.say "No, no, no..."
            alexis.say "I meant they might have thought you were a loser if you didn't turn up!"
            hide fx
            mike.say "Ah...okay, Alexis."
            mike.say "If you say so..."
            $ hero.calendar.add(game.calendar.get_next_day_of_week("saturday"), LabelAppointment(16, "alexis", "High School Reunion (Alexis)", "alexis_event_11", "missed_alexis_event_11"))
        "Refuse":
            "Of course I don't!"
            "I fucking hated high school."
            "It was the single worst time of my life so far!"
            mike.say "No way, Alexis!"
            mike.say "I'd rather drink fucking poison!"
            show alexis confused
            "Alexis frowns at this."
            "She's clearly not happy with my answer."
            alexis.say "Aw, come on, [hero.name]!"
            alexis.say "You're not still butt-hurt about what happened back then, are you?"
            alexis.say "So you got your head flushed down the toilet a couple of times, so what?"
            alexis.say "Isn't it time we all moved on?"
            mike.say "Hey!"
            mike.say "For the record, I did not get my head flushed down the toilet!"
            mike.say "But people did make my life a misery."
            mike.say "And I don't want or need to be reminded of that!"
            show alexis angry
            "Alexis is already beginning to sulk at my rejection of her idea."
            alexis.say "Fine, please yourself!"
            alexis.say "I might just go alone, if that's your attitude."
            mike.say "Be my guest, Alexis."
            mike.say "I'm sure you'll have a great time with all those assholes from back in the day!"
    hide alexis
    return

label alexis_event_11(appointment=None):
    if alexis.love.max < 180:
        $ alexis.love.max = 180
    scene bg classroom with fade
    "Alexis was the one that talked me into the idea of attending our high school reunion."
    "And as soon as we get there, she shows a level of enthusiasm that I just can't match."
    "She's off mingling and greeting people that I barely recognise by name."
    "I'm still kind of reeling from being back at the school and in one of the old classrooms."
    "As I look around, everything I see seems to jog my memory and cause me to remember something from the past."
    "And almost none of those memories are the kind that I wanted to dredge up."
    "Let's just say that high school wasn't the happiest time of my life, okay?"
    jack.say "Hey, [hero.name]!"
    jack.say "How weird does all of this feel, huh?"
    show jack casual happy at left with move
    "I turn to see Jack hurrying over."
    show jack casual happy at left4 with ease
    "And the sight of a familiar face is an instant comfort."
    mike.say "Hey, Jack..."
    mike.say "Yeah, I guess it is pretty weird!"
    show jack casual normal at center with ease
    "Jack shakes his head as he glances around the class room."
    jack.say "I can't believe how small this place looks now."
    jack.say "I always remembered it being huge!"
    mike.say "I'm feeling a bit more freaked out by the people, Jack!"
    mike.say "Half of them look like complete strangers to me."
    mike.say "Did we actually go to school with them?"
    mike.say "Or are they just here for the buffet and the booze?"
    show jack casual happy
    "Jack snorts out a laugh at this."
    "Then he shakes his head."
    show jack casual normal
    jack.say "Are you kidding, man?!?"
    jack.say "That's Andre Alphonse right there."
    jack.say "Looks like he had a hair transplant or something!"
    mike.say "Whoa..."
    mike.say "It looks like fucking road-kill!"
    show jack casual happy at startle
    "Jack sniggers at this, just like he used to back in the day."
    show jack casual normal
    jack.say "You think that's bad?"
    jack.say "Look over there - that's Kelly Clerkenwell."
    "I follow Jack's gaze until I see the person in question."
    mike.say "No way!"
    mike.say "That girl looks like she ATE Kelly Clerkenwell!"
    jack.say "Nah, man - I'm pretty sure that's her."
    show fx drop
    jack.say "Shit...some people really let themselves go, huh?"
    "I can't help looking down at Jack's waistline as he says this."
    "I know he's my buddy - but seriously?"
    hide fx
    "He's got to be one of the pudgiest people in the room!"
    menu:
        "Ignore him":
            "I could call Jack out and tell him to lose some damn weight."
            "But the truth is that I need all the support I can get right now!"
            "Pissing him off means that I'd probably lose him as back-up."
            "So I just nod and go along with his critique of Kelly's weight."
        "You should buy a mirror":
            mike.say "You know what they say about people who live in glass houses, Jack!"
            "I give him a sharp prod in the belly to underline my point."
            "Jack's cheeks flush red and her tries to suck his gut in."
            "It doesn't make any difference, but it does make me chuckle."
            show fx anger
            jack.say "Hey, man - that is not cool!"
            jack.say "We're supposed to be buddies."
            hide fx
            jack.say "We should have each other's backs - like we did back in school!"
    show jack at left4
    show alexis casual at right
    with moveinright
    "Before we can get into it any deeper, Alexis interrupts the conversation."
    if alexis.flags.story == 1:
        alexis.say "Wow - it's a genuine nerd's reunion over here!"
        alexis.say "I'd better watch out for you two guys."
        show alexis happy
        alexis.say "Or a spontaneous game of Demons and Demigods might break out!"
        mike.say "Ha, ha..."
        mike.say "Very funny, Alexis!"
        mike.say "I could really do without you leaving me hanging like that again!"
        show alexis normal
        "Alexis waves away my complaints with one hand, as if they're nothing."
        "And I can see that she's paying more attention to Jack than me right now."
        "Which probably has something to do with the fact his tongue is practically hanging out!"
        show jack at left5
        show alexis flirt at right5
        with ease
        alexis.say "Well, hello, Jack!"
        alexis.say "I didn't get a good look at you from across the room."
        alexis.say "Haven't you changed since I saw you last!"
        alexis.say "You've grown, kind of bloomed even!"
        show jack casual perv
        "Jack nods eagerly, soaking up the compliments like a sponge."
        "I never knew if he had a thing for Alexis back in the day."
        "But then he's never been able to resist a pretty girl flirting with him either."
        jack.say "Ah..."
        jack.say "Y...yeah, Alexis!"
        jack.say "I'm growing right now too!"
        "Wait a minute..."
        "Did I just hear that right?"
        "Is Jack actually flirting back, right in front of me?!?"
        mike.say "Ahem..."
        mike.say "I was just gonna say..."
        show alexis annoyed
        alexis.say "Yeah, yeah, [hero.name]..."
        alexis.say "Save it for later."
        show alexis flirt
        alexis.say "Go grab me a drink while I catch up with Jack here."
        "I feel more than a little stunned by the way Alexis is treating me right now."
        "And I almost open my mouth to protest, to tell her exactly what I think of it."
        "But then I stop myself, because the last thing that I want is to cause a scene."
        hide jack
        hide alexis
        with dissolve
        "Instead I stalk off to get that drink as ordered."
        "Maybe I can use the time to cool down and get my temper under control."
        show jack casual perv at left
        show alexis casual happy
        with dissolve
        "The only problem is that when I get back, things seem to have escalated in my absence!"
        "Alexis is leaning in close, almost draping herself over Jack."
        "And she has one hand placed boldly on the front of his pants too."
        "For his part, Jack looks pretty nervous, even a little embarrassed."
        "But I note that he's not trying to push Alexis away at all either."
        mike.say "Erm..."
        mike.say "Guys?"
        mike.say "What's going on?"
        show alexis casual flirt
        "Alexis gives me a sly wink."
        alexis.say "I'm just going to give Jack here a little treat."
        alexis.say "He grew up so big and strong I think he deserves it!"
        "Jack looks at me with a mixture of awkwardness and amazement in his eyes."
        "And the only explanation he can give me is a shrug of the shoulders too."
        "Clearly he knows that Alexis is showing me up in front of him by doing this."
        "But he's not got the strength of will to resist her either!"
        "So my choice comes down to either calling her out in front of everyone here."
        "Or else I can do as she says and cover up what she's about to do to Jack."
        "Alexis doesn't give me the time I'd need to decide."
        show alexis ntr bj school reunion mike with fade
        "Instead she gets down on her knees and goes to work."
        "I have to hurry to stand over her as she starts to unzip Jack's flies."
        "In a mere matter of seconds, she has his cock out of his pants."
        "Needless to say, Jack's already good and hard."
        "The thrill of being seduced by Alexis is one thing."
        "But mix that with the danger of being blown in a public place..."
        "Well, you have a recipe to make a guy stand to attention right there!"
        "I keep stealing glances back over my shoulder."
        "That means I see Alexis's progress in glimpses."
        "She seems to be moving quickly, as if aware of the danger of being caught."
        "This means that she works her way speedily up Jack's shaft with her tongue."
        "Alexis licks her way to the top, and only then does she start to use her lips."
        "The tip gets a few gentle kisses and caresses, but then it's swallowed whole."
        "Jack gasps and lets out a weird groaning sound as Alexis goes down on him."
        "For a moment I think he's going to blow it, to shout out loud."
        "But somehow he manages to keep it under control, biting his lips hard."
        "This means that the general hubbub of conversation covers the sounds."
        "Not that Alexis seems to be in the least bit concerned."
        "Her head is moving back and forth at an alarming rate."
        "And part of me is starting to think that she doesn't care about the danger."
        "That she might actually want to get caught in the act for the sake of the drama!"
        "She's taking Jack's cock as deep into her mouth as she possibly can."
        "At the same time she's working his shaft with one hand."
        "And she's squeezing his balls with the other too!"
        "It's a rough blowjob, hurried and almost desperate in nature."
        "But it's having the desired effect on Jack."
        "Pretty soon he's gasping even more, starting to quiver too."
        $ alexis.love += 3
        $ alexis.sub -= 3
        "So I'm not surprised when he thrusts his cock forwards a moment later."
        "Jack must be shooting his load into Alexis's mouth right now!"
        "And I watch in terrible fascination as she swallows it like a pro."
        "Not one drop escapes her lips and she doesn't choke once."
        "Before either Jack or I can say a word, she's already covering her tracks."
        "Alexis deftly slides Jack's cock back into his pants and zips him up."
        hide alexis
        show jack casual zorder 1 at right
        show alexis normal casual zorder 2 at right4
        with fade
        "Then she stands up as casually and quickly."
        "Anyone watching would think she'd just stooped to pick up something she dropped a moment before."
        alexis.say "There now..."
        alexis.say "Doesn't that feel better, Jack?"
        show jack casual at right, startle
        "Jack nods eagerly, still too flushed for actual words."
        "I fix Alexis with a stare that's supposed tell her she's on thin ice."
        show alexis flirt at startle
        "But all I get in return is a peal of laughter and a confident wink."
        "And just like that she seems to think that the matter's over and done with."
        "Alexis doesn't mention it again the rest of the time we're there."
        "But it's constantly at the front of my mind."
        "The images just refuse to budge no matter what I do."
        "And I can see that the same is true of Jack as well."
        "He looks thrilled at what just happened, for sure."
        "But at the same time he's awkward with me, refusing to meet my eye."
        "It seems like the only one who got all she wanted out of this was Alexis!"
    else:
        show alexis angry
        alexis.say "Get your coat, [hero.name]."
        alexis.say "I want to leave - right now!"
        "The force with which Alexis says this is almost enough to stagger me."
        "It comes out of the blue, taking me completely by surprise."
        "I shoot a look in Jack's direction, looking for some help."
        "But he seems every bit as stunned as I am myself."
        mike.say "Alexis..."
        mike.say "You really want to leave?"
        mike.say "We only just got here!"
        mike.say "And coming here was your idea in the first place, remember?"
        show alexis confused
        "Alexis frowns at this, like I'm throwing it back in her face."
        "But then she shakes her head, like she's snapped out of something."
        show alexis sad
        alexis.say "Urgh..."
        alexis.say "Sorry, [hero.name]..."
        "It's only now that Alexis seems to notice Jack standing close by."
        "She shakes her head again, clearly embarrassed at her outburst."
        alexis.say "I guess a sorry's in order for you too, Jack."
        show alexis normal
        alexis.say "I was so tied up in myself just now that I didn't see you there!"
        show jack casual happy
        "Jack smiles awkwardly and waves away Alexis's apology."
        jack.say "Hey, Alexis..."
        jack.say "Don't worry about it, seriously."
        jack.say "It's not like you're the first girl not to notice my existence!"
        mike.say "Seriously, though, Alexis..."
        mike.say "What's the matter?"
        show jack casual normal
        show alexis sad
        "Alexis turns to regard the rest of the room."
        "She crosses her arms over her chest, a look of irritation on her face."
        show alexis annoyed
        alexis.say "I know that I can trust you two."
        alexis.say "So I'm just going to come out and say it."
        show alexis sad
        alexis.say "All anyone seems to want to talk about is...what happened to me here..."
        alexis.say "It's like that's all they see when they look at me!"
        "There's no need for Alexis to be more specific than that."
        "Both Jack and I know full well what she's talking about."
        "And that's the time she was sexually assaulted by a member of the teaching staff."
        "I can't believe that anyone would be crass and insensitive enough to bring it up here."
        "And from the look in his eyes, Jack feel the exact same way too."
        mike.say "Jesus, Alexis!"
        mike.say "I'm shocked...and mad too!"
        jack.say "Who was it, Alexis?"
        jack.say "You want us to have a word with them?"
        "I can see that Jack and I rallying to Alexis's aid has an instant effect."
        show alexis normal
        "She seems reassured by the support and genuinely grateful to be backed up."
        "But all the same she shakes her head, dismissing our offers to leap to her defence."
        show alexis annoyed
        alexis.say "No, no..."
        alexis.say "It's sweet of you to offer, guys..."
        alexis.say "But you'd be having words with half the people here!"
        alexis.say "Plus it'd just make the whole thing that much worse."
        show alexis sad
        "Jack and I exchange a worried glance."
        "But then we nod in agreement."
        "Alexis is right - we'd only be fuelling the fire if we did that."
        mike.say "Geez, Alexis..."
        mike.say "I thought I'd be the one pissed off at people dragging up the past!"
        mike.say "But If I'd known this would happen to you..."
        mike.say "Well, I'd have argued twice as hard for us not to come at all!"
        show alexis happy
        "Alexis chuckles and nods, ruefully agreeing with me for once."
        "But the look on Jack's face is more thoughtful."
        "It's like he's turning the whole thing over in his mind."
        jack.say "You know what..."
        show alexis normal
        jack.say "This might sound crazy, but hear me out..."
        jack.say "Maybe all of this is actually a good thing - did you ever think of that?"
        show alexis annoyed
        mike.say "What are you talking about, Jack?"
        mike.say "How could it possibly be good?"
        show alexis normal
        "Alexis puts a gentle hand on my arm."
        "At the same time she nods to Jack."
        alexis.say "Let him talk, [hero.name]."
        alexis.say "Jack sounds like he might be onto something here."
        show jack casual happy
        "Jack smiles and blushes a little."
        "Clearly he's not used to having the attention of a hot girl the likes of Alexis!"
        show jack casual normal
        jack.say "Ahem..."
        jack.say "Well...it's no fun being reminded of bad stuff from the past."
        jack.say "But how come all of these people are wanting to talk about it and you're not?"
        jack.say "Sure, you don't want to be reminded about it."
        jack.say "But doesn't it also mean you've moved on and they haven't?"
        jack.say "You came here wanting to show how far you've come."
        jack.say "And yet all they want to do is gossip about stuff from back in the day!"
        "What Jack's saying makes perfect sense to me."
        mike.say "He's right, Alexis."
        mike.say "All of the people in this room are stuck in the past."
        mike.say "They're making you mad because you're beyond that now."
        mike.say "You just need to see that and then leave them behind again."
        "It's now that Alexis starts to nod too."
        "And I can see the tension leaving her body."
        $ alexis.love += 5
        show alexis happy
        alexis.say "Thanks, guys."
        show alexis normal
        alexis.say "I see what you mean now."
        alexis.say "Maybe that's why I wanted to come here in the first place."
        alexis.say "To confront my past and prove to myself that I'm over it."
        alexis.say "I certainly won't miss seeing any of these losers again!"
        alexis.say "Present company excepted, of course."
        alexis.say "I kind of want to keep you two losers around!"
        mike.say "Ah..."
        mike.say "Thanks, Alexis - I think!"
        show jack casual happy
        show alexis happy
        "For the rest of the reunion, Alexis sticks by Jack and me."
        "We form a tight little knot, mostly ignoring everyone else."
        "And by the time it's all over, I'm ready to leave this place behind."
        "The past is a nice place to visit once in a while."
        "But I wouldn't want to live there."
    return

label missed_alexis_event_11:
    "Shit, I missed the high school reunion. Alexis is going to be mad."
    $ alexis.love -= 10
    $ alexis.sub -= 10
    $ DONE.pop("alexis_event_10", None)
    return

label alexis_event_12:
    if alexis.love.max < 200:
        $ alexis.love.max = 200
    if alexis.flags.story == 2:
        show alexis casual sad
        "Alexis is puzzling me today, making me feel more than a little uncomfortable for some reason."
        "It's not anything that she's said or done that's starting to put me on edge."
        "More like it's what she's not saying and doing that are worrying me."
        "Alexis keeps shooting me these glances, like she's trying to gauge my mood."
        "And more than once I think she's going to open her mouth and speak to me."
        "But every time she seems to bite her tongue and let the moment slip by."
        "Before too long it's becoming too much for me to handle - I swear I'm going crazy!"
        mike.say "Alexis..."
        mike.say "What on earth is wrong with you?"
        show alexis surprised
        "Alexis almost jumps at the sudden question."
        "A guilty response if I ever saw one!"
        alexis.say "Huh?"
        alexis.say "What do you mean, [hero.name]?"
        show fx drop
        alexis.say "I have no idea what you're even talking about!"
        "Ah, I think I'm starting to see what's going on here."
        hide fx
        "I recognise the reaction that my question elicited from Alexis."
        "And that's because it's one that I've been guilty of myself."
        "So if Alexis were a guy, what would she be trying to hide?"
        "Aha - that's it!"
        mike.say "Look, Alexis..."
        mike.say "Whatever it is you have to tell me, it's okay."
        mike.say "You can just come right out and say it."
        "Alexis looks at me like I just pulled off a Jeudi Mind Trick."
        show alexis normal
        "She shakes her head in amazement, like she can't believe it."
        alexis.say "B...but..."
        alexis.say "How did you know?"
        alexis.say "I haven't said a word all this time!"
        "I can only shrug and smile at this."
        "I'm not about to go sharing all my secrets with Alexis."
        "Plus I'm enjoying her amazement way too much right now!"
        mike.say "I'm just a natural when it comes to that kind of thing, Alexis!"
        mike.say "Admit it - you're lucky to be with a guy like me, right?"
        "As soon as I mention her being lucky to have me, something changes in Alexis."
        "Her cheeks flush and suddenly she won't look me in the eye anymore."
        "My instant reaction is to assume that I said the wrong thing."
        "I'm about to open my mouth and start apologising."
        "But Alexis beats me to it."
        alexis.say "Th...that's kind of it, [hero.name]..."
        alexis.say "That's what I wanted to talk to you about!"
        mike.say "Y...you're not breaking up with me, are you?"
        mike.say "Oh shit...please don't dump me, Alexis - not again!"
        show alexis surprised
        alexis.say "No, no, no!"
        alexis.say "I'm not dumping you, [hero.name]!"
        show alexis normal blush
        alexis.say "In fact it's...kind of the opposite..."
        alexis.say "I...I wanted to say that I never want to be without you!"
        "I stare at Alexis for a moment, not sure what to say."
        "Of all the things I could have imagined her wanting to tell me..."
        "That came pretty much out of the blue!"
        mike.say "I...I feel the same way about you, Alexis!"
        mike.say "But after what happened when we were together the first time..."
        mike.say "I never knew if I was going to be enough for you!"
        mike.say "You were...well, pretty wild back then!"
        show alexis -blush
        "Alexis shakes her head at this."
        alexis.say "That was then, [hero.name], it was a long time ago."
        alexis.say "We're both different people now."
        alexis.say "I like to think that I've changed for the better."
        alexis.say "And you...you're a better version of the guy you were back then!"
        "I can't help smiling as I look Alexis in the eye."
        show alexis blush
        "And it seems to be having an effect on her too."
        alexis.say "Why are you looking at me like that?"
        alexis.say "You're making me feel nervous!"
        mike.say "I can't help it, Alexis."
        mike.say "You're just so perfect!"
        show alexis happy
        alexis.say "Oh...stop talking like that!"
        show alexis normal
        alexis.say "Just tell me that I'm right and we can be together forever, okay!"
        mike.say "Okay, Alexis..."
        mike.say "We can be together forever."
        mike.say "Or longer, if you like!"
    else:
        show alexis casual annoyed
        "I didn't think that Alexis and I were going to be doing much more than chilling today."
        "And that's fine by me, as I like any chance I can get to just spend time with her."
        "But I can tell from the way that Alexis is looking at me that's not going to happen."
        "She has that serious expression on her face, the one that means business."
        "So the only choice that I really have is to look her square in the eye and listen."
        "And sure enough, it doesn't take long for her to broach the subject."
        alexis.say "[hero.name]..."
        alexis.say "I think it's time we had a talk about us."
        alexis.say "About where this relationship is going."
        "I can't help swallowing nervously as I hear all of this."
        "No guy really wants to be forced to sit down and discuss his relationship with a girl."
        "But when she comes out with it in such plain language, there's really no way to avoid it."
        mike.say "If you say so, Alexis."
        mike.say "I think it's going pretty well, all things considered."
        mike.say "Don't you?"
        show alexis normal
        "Alexis nods and smiles at this."
        "Which is an instant relief for me."
        alexis.say "Me too, [hero.name], me too."
        alexis.say "We're doing so much better than we did the first time around."
        alexis.say "And do you know why I think that is?"
        "I frown and shrug, not sure how to answer that."
        "My guess is that there's an answer Alexis wants to hear."
        "But as I have no idea what that is, I'll just have to guess."
        mike.say "Erm..."
        mike.say "Because we're all grown-up now?"
        mike.say "A couple of mature adults?"
        show alexis confused
        "Alexis looks thoughtful for a moment."
        "Like the answer's a good enough try."
        "But not the exact thing she was hoping for."
        alexis.say "That's part of it, [hero.name]."
        show alexis normal
        alexis.say "But I think it's because we're being honest with each other."
        alexis.say "We could never do that back in high-school."
        alexis.say "And it didn't end well because of that, did it?"
        "I'm tempted to say that it didn't end well because Alexis cheated on me!"
        "But that's not going to get me anywhere, now is it?"
        "So I nod and keep my mouth shut."
        alexis.say "So I'm going to keep on being honest, [hero.name]."
        alexis.say "And I'm going to tell you that I want to be with you."
        alexis.say "But only if you can handle me sleeping with other guys too."
        alexis.say "That's the deal, [hero.name]."
        show alexis flirt
        alexis.say "I get to fuck who I want, when I want."
        alexis.say "And you get to watch."
        show alexis normal
        alexis.say "Do you think you can handle that?"
        "Just the thought of watching Alexis being fucked is making me hard."
        "I have no idea where this is coming from, or why I feel it."
        "But maybe I've grown to love the idea since I first learned Alexis was a cheater?"
        "All I know is that I want to see more of it, and soon!"
        mike.say "Of course I can, Alexis!"
        mike.say "Seeing you with other guys is pretty hot."
        mike.say "And it just makes me want to fuck you all the more."
        mike.say "You know, to remind you that you're mine!"
        show alexis happy
        "Alexis smiles, an expression full of equal parts amusement and lust."
        alexis.say "Mmm..."
        alexis.say "I LOVE the sound of that, [hero.name]!"
        show alexis flirt
        alexis.say "Feeling one cock inside of me."
        alexis.say "But knowing it makes you want me all the more!"
        alexis.say "Oh fuck..."
        alexis.say "I'm getting wet just thinking about it!"
        "I nod eagerly at this, encouraging Alexis as much as I can."
        "And that's because I'm getting hard as the same time."
        mike.say "Just promise me one thing, Alexis."
        mike.say "That we do it soon and often!"
        show alexis normal
        "Alexis's eyes are alight with desire as she nods too."
        alexis.say "Oh, you bet we will!"
        show alexis flirt
        alexis.say "I can feel those cocks inside of me right now!"
        alexis.say "And I can feel your jealous eyes on me too..."
    return

label alexis_event_ntr_01:
    scene bg livingroom
    show alexis casual
    "I had meant to make this a relaxing weekend afternoon, just some time to do nothing."
    "But I guess if that's what I wanted, then I shouldn't have invited Alexis over."
    "The moment that she got here she was all smiles and winks, flirty as hell."
    "And now she's stripping off her clothes right in front of me!"
    show alexis topless with dissolve
    "It's just lucky my housemates aren't in to see all of this."
    mike.say "Ah..."
    mike.say "I WAS trying to chill out, Alexis!"
    "By now, Alexis is down to her panties."
    "And all she does is look back over her shoulders at me."
    show alexis naked happy with dissolve
    alexis.say "Aw, come on, [hero.name]!"
    alexis.say "They say a change is as good as a rest."
    show alexis normal
    alexis.say "Anyway, I have a surprise for you."
    "That's the first I've heard about any surprise."
    "And I can't help being intrigued at the idea."
    mike.say "A surprise, Alexis?"
    mike.say "What kind of surprise?"
    show alexis flirt
    alexis.say "If I tell you that, it won't be a surprise - will it!"
    "I open my mouth, meaning to question Alexis further."
    play sound door_knock
    "But it's then I hear a knock at the front door."
    show alexis normal
    "Alexis looks in the same direction, as if she expects me to answer it."
    mike.say "They can go to hell, Alexis!"
    mike.say "I want to see what this surprise is."
    show alexis confused
    alexis.say "Erm..."
    alexis.say "You might want to answer it, [hero.name]."
    show alexis normal
    alexis.say "If they keep knocking, it'll put me off when I show you..."
    "I shrug and stand up, beginning to make for the door."
    "I don't want to bother with all of this."
    "But if it means Alexis and I won't be disturbed, then what the hell."
    scene bg black with dissolve
    pause 0.1
    scene bg house
    show danny as marlon zorder 1 at left4, blacker
    show dwayne as ray zorder 2 at right5, blacker
    show dwayne as tyreese zorder 3 at flip, mostright5, blacker
    with wiperight
    "Opening the door, I expect to see the postman or a salesman of some kind."
    "But instead I'm greeted by the sight of three guys standing there."
    "Three BIG black guys, all of them leaning against the doorframe."
    "At the sight of me, the nearest of the guys looks up nonchalantly."
    show dwayne as ray at right5, blacker, startle
    "Ray" "Yo, dawg."
    "Ray" "I'm Ray, this here is Marlon."
    show danny as marlon at left4, blacker, startle
    "Marlon" "S'up."
    show dwayne as ray at right5, blacker, startle
    "Ray" "And that right there is Tyreese."
    show dwayne as tyreese at flip, mostright5, blacker, startle
    "Tyreese" "Hey."
    "Utterly stunned at introduction, I have no idea what to say."
    "And so I can only respond in kind."
    mike.say "Erm...hi..."
    mike.say "I'm [hero.name]..."
    "At the mention of my name, Ray nods."
    show dwayne as ray at right5, blacker, startle
    "Ray" "Yup, this is it."
    "Ray" "Alexis inside?"
    mike.say "I...I guess so..."
    "Ray nods and walks calmly past me before I can object."
    "Marlon and Tyreese follow close on his heels, leaving me alone on the doorstep."
    "Quickly shutting the door behind them, I hurry back into the sitting room."
    scene bg livingroom
    show alexis naked
    with fade
    "By the time I get there, all three of them are stripping off too!"
    alexis.say "I take it you already met the guys?"
    show alexis happy
    alexis.say "When I asked, they were more than up for a foursome."
    mike.say "A...a foursome?!?"
    show alexis normal
    alexis.say "Yeah, that's right."
    show alexis flirt
    alexis.say "And best of all - you get to watch the whole thing!"
    menu:
        "Accept":
            "I can't help grinning at the thought of what Alexis has in mind."
            "Maybe it sounds crazy, but I find myself actually wanting to watch."
            "All that time I spent brooding over how she cheated on me back in high-school."
            "Now I can see her try to handle three guys at once."
            "Rather than making me feel jealous, it's a chance to see Alexis humiliated."
            "If she wants to act like a slut, then why shouldn't I let her?"
            mike.say "Okay, Alexis - what are you waiting for?"
            show alexis normal
            "I sit down on one of the sofas, ready to watch the show."
            "Ray" "Okay, Alexis."
            "Ray" "Let's get this thing started..."
            hide alexis
            show alexis ntr handjob with fade
            "All four of them are naked by now."
            "Alexis perches on the opposite sofa and Ray sits beside her."
            "He lies back casually, letting his now stiff cock stand proud."
            "Marlon and Tyreese stand to the other side of Alexis."
            "Their own cocks bobbing mere inches from her face."
            "Without needing to be told what to do, Alexis leaps into action."
            "Her hands never seem to be still for a moment."
            "Instead they move from one cock to the next, never leaving one alone for too long."
            "She strokes, squeezes, rubs and caresses every inch that the guys possess between them."
            "Balls, shaft and head, all get worked in turn as she moves from one to the next."
            "It's kind of like watching someone spinning plates and keeping them all in motion."
            "And I can see from the faces of all three guys that she's doing a good job too."
            "Ray" "Ah yeah..."
            "Ray" "Now that's the stuff!"
            "Marlon" "Sweet!"
            "Tyreese" "Mmm..."
            "I can't help getting hard just from watching."
            "And before I know it, I have my own cock out too."
            "My hand pretty much copying Alexis's efforts."
            "But then I see Ray nod to the other guys, and they nod in turn."
            hide alexis
            show alexis ntr gangbang
            with fade
            "Without speaking a word, Marlon slides onto the sofa beside Alexis."
            "And then he guides her onto him, until she's straddling his lap."
            "Alexis moans as his cock pushes against her lips, resisting for a moment."
            show alexis ntr gangbang vaginal
            "But then she begins to sink down and onto it, gasping as she surrenders."
            "Before Marlon is all the way into her, Ray takes a firm hold of Alexis's waist."
            "He parts her buttocks and aims his cock straight between them."
            "Ray" "One cock ain't gonna be enough for you, girl!"
            "I see Alexis look back over her shoulder, nodding eagerly."
            "And that's all the permission Ray needs."
            show alexis ntr gangbang anal pleasure
            "He plunges his cock into Alexis's ass, pushing with all his strength."
            alexis.say "Oh..."
            alexis.say "Oh god..."
            alexis.say "I'm so full..."
            alexis.say "Full of cock!"
            "At this, I hear Ray chuckle."
            "He shakes his head and motions to Tyreese."
            "Ray" "Not yet you ain't."
            "Ray" "Tyreese, put that mouth of hers to better use!"
            "Tyreese nods as he steps forwards, holding his cock in one hand."
            show alexis ntr gangbang normal
            "Alexis's eyes go wide as he uses the other hand to cup her chin."
            show alexis ntr gangbang blow
            "A moment later his cock is in her mouth, and Alexis can't say another word."
            "But that doesn't mean that she's thrown at all."
            show alexis ntr gangbang pleasure
            "Within seconds, her head is moving back and forth as she services the cock."
            "And from the look on Tyreese's face, she's doing a good job too!"
            "In fact, I can see that she's doing far better than these guys expected."
            "Sure, all three of them are getting exactly what they wanted right now."
            "But I swear I can see a change come over them as time goes on."
            "There's a subtle hint in their expressions."
            "One that makes me think they expected to be too much for Alexis."
            "Oddly that makes me squeeze my own cock that much harder."
            "Like I'm turned on by the idea that Alexis is too much for them."
            "Ray even shakes his head as he keeps on pounding away at her ass."
            "Ray" "Goddamnit, woman..."
            "Ray" "How much cock do you need?!?"
            "Ray" "I'm gonna blow my load real soon!"
            "Marlon" "You and me both!"
            "Tyreese" "Not if I do it first!"
            show alexis ntr gangbang -blow
            "At the mere mention of them cumming, Alexis pulls the cock out of her mouth."
            "She's panting with exhaustion, but still manages to get her words out."
            alexis.say "All...of...it..."
            alexis.say "In the...in the face..."
            show alexis ntr gangbang -vaginal -anal
            "The guys hastily pull out of Alexis, freeing her for the first time."
            hide alexis
            show alexis ntr bukake with fade
            "And she almost tumbles onto the floor in the middle of the room."
            "They gather around her as she kneels there, cocks bobbing close to her face."
            show alexis ntr bukake lookright
            "Alexis begins to work all three of them in earnest."
            "And it doesn't take long for her efforts to be rewarded."
            show alexis ntr bukake closeeyes cumshot left middle right with hpunch
            "Within seconds of each other, the three of them shoot their loads."
            with hpunch
            "And Alexis is in the perfect position to catch almost every drop."
            show alexis ntr bukake -cumshot dickcum cum onbody onmouth with hpunch
            $ alexis.love += 4
            "Ray, Marlon and Tyreese gasp at the release, and Alexis gasps too."
            "But in her case, it's from the desire to not miss the smallest amount."
            "Still, most of the cum seems to hit her face all the same."
            "It stripes her forehead, cheeks and chin, dripping downwards."
            "Some actually lands in her open mouth to be swallowed greedily."
            "And some drips onto her lips too, which she laps up with her tongue."
            show alexis ntr bukake swallow -onmouth
            "Even afterwards, Alexis licks what she can find off of her fingers too."
            "That's when I feel something warm running over my own fingers."
            "And I realise that I just shot my own load too."
            show alexis ntr bukake closeeyes
            "Ray sees this and shakes his head, chuckling deeply."
            "Ray" "I guess that's like a standing ovation, huh?!?"
            "Ray" "Looks like you enjoyed this as much as we did, brother!"
            hide alexis
            show alexis naked
            with fade
            "There's more friendly banter as everyone gets dressed."
            "And then Ray, Marlon and Tyreese make their excuses to leave."
            "Ray" "This was fun, guys."
            "Ray" "We should do it again some time."
            "Ray" "And your man here could get involved too!"
            mike.say "Ah..."
            mike.say "I don't know about that!"
            "Ray" "Whatever - stay frosty."
            "And with that, they're gone."
            show alexis happy
            alexis.say "So..."
            show alexis normal
            alexis.say "Was that fun for you?"
            mike.say "Sure, Alexis - I had a good time watching."
            mike.say "You really ate those guys alive!"
            "That was supposed to be a compliment, but I see Alexis blush."
            show alexis blush
            alexis.say "What can I say, [hero.name]?"
            alexis.say "I have needs!"
            $ alexis.sub -= 5
            $ game.active_date.score = 100
            $ game.pass_time(2)
        "Refuse":
            "What the hell is she even thinking?!?"
            "Bringing three other guys into my home."
            "Fucking them in front of me!"
            mike.say "You've got to be joking, Alexis!"
            show alexis confused
            alexis.say "Huh?"
            alexis.say "B...but I thought..."
            mike.say "No, Alexis - you didn't think."
            mike.say "If you had then you'd have asked me first."
            mike.say "And I'd have told you this was a terrible idea."
            show alexis sad blush
            "Alexis looks away as I tell her off."
            "Her cheeks flush a deep shade of red."
            "The other guys couldn't help overhearing our exchange."
            "And I see Ray striding over from the other side of the room."
            "I wince as he reaches me, expecting trouble."
            "Ray" "Hey, Alexis."
            "Ray" "Is he tellin' the truth?"
            show alexis -blush
            alexis.say "Ah..."
            alexis.say "Yes, Ray."
            alexis.say "I didn't tell him."
            "Ray shakes his head."
            "Ray" "That's not cool, Alexis."
            "Marlon" "Uh-uh."
            "Tyreese" "No it ain't."
            "Ray" "You showed this guy up, and us too!"
            alexis.say "I'm sorry, you guys."
            alexis.say "I won't do it again."
            "Ray shakes his head and waves to his companions."
            "And together they pull on their clothes as they head for the door."
            "Once they're gone, there's an awkward atmosphere in the room."
            "Both Alexis and I are quiet, but I think she learned her lesson."
            $ alexis.love -= 20
            $ hero.cancel_activity()
            $ game.active_date.stay = False
            $ alexis.flags.story = 2
    return

label alexis_event_ntr_02:
    scene bg sexshop with fade
    "It's been a hard thing to wrap my head around, the fact that Alexis seems to need so much to satisfy her."
    "But now that I know it's the reason she's been behaving the way she has, I'm determined to deal with it."
    "I've decided that I need to show Alexis I understand her condition and I'm willing to make allowances for it."
    "After all, I lost her once, and I don't want to have that happen to me a second time."
    show alexis casual at right with dissolve
    "That's why I suggest that we take a trip to the local sex shop."
    "Where better to find a solution the to problem than that?"
    "So as we walk into the place, I do my best to play it casual."
    show alexis annoyed at center with ease
    alexis.say "It still feels a little weird coming here with you, [hero.name]!"
    mike.say "Huh?!?"
    mike.say "Why'd you say that, Alexis?"
    mike.say "I'm a pretty modern guy, aren't I?"
    mike.say "And I like getting it on as much as the next guy too!"
    show alexis happy at startle
    "Alexis chuckles and shakes her head."
    "Which is something I like to see, as it makes her look innocent and sweet."
    alexis.say "I didn't mean it like that!"
    show alexis normal
    alexis.say "More like it's new to me."
    alexis.say "We never did stuff like this when we were kids, you know?"
    "I nod, realising Alexis is right."
    "A lot has changed since we were together in high-school."
    "And for the better too, I hope."
    mike.say "Well..."
    mike.say "When you put it like that..."
    alexis.say "Okay, okay..."
    alexis.say "You're a man of the world now, [hero.name]."
    show alexis wink
    alexis.say "A voyager on the erotic seas of sexiness!"
    show alexis annoyed
    show fx question
    alexis.say "So, what are we here for, huh?"
    "Here we go."
    "I guess this is the point where I have to confess."
    "I just hope Alexis understands what I'm trying to do here!"
    mike.say "Okay, Alexis..."
    mike.say "Cards on the table..."
    mike.say "I've noticed it takes a lot to satisfy you."
    show alexis surprised
    "Alexis's eyes go wide at this."
    "And she looks this way and that like she's afraid of someone hearing."
    "How can she be so self-conscious?"
    "Especially after some of the stuff I've caught her doing in the past!"
    alexis.say "Whoa..."
    show alexis angry
    alexis.say "Now wait a minute there, mister!"
    alexis.say "I know I have a healthy appetite for that kind of thing."
    alexis.say "But you make it sound like I'm a nymphomaniac or something!"
    "I hold up a hand, waving away Alexis's protests."
    "I understand her reaction."
    "But I'm still determined to make my point."
    show alexis confused
    mike.say "It's okay, Alexis - there's no need to deny it."
    mike.say "I just want to make sure that you get what you need."
    mike.say "I feel like it's my duty as a good boyfriend, you know?"
    mike.say "To help out whenever and wherever I can."
    "Alexis seems less than convinced by my explanation."
    "But a look of resignation settles over her features a moment later."
    "She crosses her arms over her chest and shakes her head."
    show alexis annoyed
    alexis.say "Alright, [hero.name], you win."
    alexis.say "I'm willing to admit that I have...an appetite."
    alexis.say "So what's your genius solution?"
    menu:
        "Suggest more dildos":
            mike.say "Well, I figured that you need more than one cock, right?"
            mike.say "And rather than having you fuck other guys, how about this..."
            mike.say "We buy you a whole bunch of dildos, yeah?"
            mike.say "That way you'll always have one on hand when the mood takes you."
            show alexis confused
            "Alexis looks less than convinced."
            alexis.say "I..."
            alexis.say "I don't think..."
            "But I'm already committed to explaining my idea."
            "And I'm not about to stop now that I've actually said it."
            mike.say "Wait a minute, Alexis."
            mike.say "Just hear me out, okay?"
            mike.say "We can get all different shapes and sizes."
            mike.say "Some that vibrate too."
            mike.say "And we can make sure they're right there when you need them!"
            show alexis angry
            alexis.say "Will you shut the hell up for a second?!?"
            "I stop talking, surprised by Alexis's sudden out burst."
            show alexis normal
            "She takes a deep breath, holds it for a moment, then lets it out as a sigh."
            alexis.say "Look, [hero.name]..."
            alexis.say "It's not that simple, okay?"
            alexis.say "This isn't about getting as much cock inside me as possible."
            alexis.say "There's more to it than that."
            alexis.say "It's about the way that a guy looks at me, you know?"
            alexis.say "The way that I just know he's lusting after me!"
            "All I can do is look down at my feet as Alexis explains herself."
            "I thought I'd cracked it, that I was getting a handle on her."
            "But it seems I got it completely wrong."
            mike.say "Erm..."
            mike.say "Okay, Alexis..."
            mike.say "Maybe we should just leave?"
            show alexis sad
            alexis.say "Yeah..."
            alexis.say "Maybe we should!"
            hide alexis with moveoutright
            "And with that, we hurry out of the place before anyone sees us."
            $ alexis.love -= 5
            $ alexis.sub -= 5
            $ game.room = "alley"
        "Suggest the glory-hole room":
            mike.say "Well, I figured that you need more than one cock, right?"
            mike.say "And I'm also thinking that dildos aren't going to cut it either."
            mike.say "So we need a way you can get a whole lot of cock all at once."
            show alexis surprised
            "As I'm speaking, I see a look of genuine surprise appear on Alexis's face."
            "It's like I'm saying things that she never thought she'd hear from my lips."
            show alexis blush
            "Alexis is nodding too, eagerly hanging on my every word."
            show alexis normal
            alexis.say "That's amazing, [hero.name]!"
            alexis.say "No guy's ever seen it like that before."
            alexis.say "None of them have ever seen it from my point of view!"
            alexis.say "But I still don't know what you're going to do about it."
            mike.say "Ah..."
            mike.say "That's where this place come in, Alexis."
            mike.say "They've got one of those booths in the back."
            mike.say "The kind with glory-holes in the walls, yeah?"
            mike.say "I figure you spend some time in there."
            mike.say "That way you can have all the cock you want!"
            show alexis happy
            "Alexis is now looking at me in sheer amazement."
            "She's shaking her head like she can't believe what she's hearing."
            alexis.say "Y...you're serious?"
            show alexis normal
            alexis.say "You'd let me go in there?"
            alexis.say "Go in there and play with other guys' dicks?!?"
            mike.say "Of course, Alexis."
            mike.say "If it'll make you happy, that's all that matters."
            show alexis happy at center, zoomAt(1.5, (640, 1040))
            "Alexis nods eagerly as she grabs hold of my hand."
            "And before I know it, she's dragging me towards the back of the sex shop."
            hide alexis
            show alexis ntr glory hole with fade
            "Luckily for us, the booth is empty when we get there."
            alexis.say "Here goes nothing, [hero.name]!"
            alexis.say "Are you coming in there with me?"
            menu:
                "Enter the booth with Alexis":
                    "I think about it for a moment, weighing up the possibilities."
                    "And I'm almost convinced that I should say no, that it's a bad idea."
                    "But somehow I hear myself saying the words before even I realise it."
                    mike.say "Yeah, Alexis!"
                    mike.say "That sounds wild!"
                    "All of my nerves seem to vanish with the smile Alexis gives me."
                    "And she doesn't hesitate to pull me into the booth after her."
                    show alexis ntr glory hole alexis peace mike with dissolve
                    "Once we're inside, I just stand there, looking around me."
                    "I have no idea how this is supposed to work."
                    "But luckily for me, Alexis doesn't hesitate to take the lead."
                    show alexis ntr glory hole dickleft
                    "There are already anonymous cocks appearing through the holes."
                    show alexis ntr glory hole dickright
                    "They're of all colours, shapes and sizes imaginable."
                    "And Alexis turns on the spot, taking them all in."
                    show alexis ntr glory hole leftman
                    "Without warning, one of them seems to catch her eye."
                    show alexis ntr glory hole -peace wantleftcum
                    "Alexis pounces on it like a cat seizing its prey."
                    "And what follows is a staggering display of sexual appetite."
                    show alexis ntr glory hole leftblowjob closed -wantleftcum
                    "Lips, tongue and fingers all come into play as Alexis gets to work."
                    "Some cocks she uses her hands to pleasure."
                    "Rubbing the shafts and tormenting the heads."
                    "Others she takes into her mouth as well."
                    "And of these, some are given little more than a playful suck."
                    show alexis ntr glory hole opened cumdickleft
                    "But the lucky ones are almost swallowed hole."
                    "These she goes at as if her life depends on it."
                    "Part of me was worried that I just wouldn't be able to handle all of this."
                    "That I'd be overcome with jealousy the moment I saw Alexis touch another guy's cock."
                    show alexis ntr glory hole stand
                    "And yet it's the sheer look of delight on her face that truly grabs my attention."
                    "I don't think I've ever seen Alexis look so alive as she does right now!"
                    "Maybe I'm starting to understand what it is that she gets out of this."
                    "Maybe it's not about the dangerous thrill of cheating on someone after all."
                    show alexis ntr glory hole wantrightcum
                    "Because whenever she catches my eye, Alexis looks at me the same way too!"
                    "It's also about now that I realise I'm on show too!"
                    "All those eyes looking into the booth through the slots."
                    show alexis ntr glory hole wantleftcum
                    "They can see me as easily as they can Alexis."
                    "Perhaps that's why she chooses to leave me until last?"
                    show alexis ntr glory hole cumshot
                    "One by one the cocks poking through the holes are spent."
                    "They either spurt cum onto Alexis's hands."
                    show alexis ntr glory hole ahegao alexisrightcum -wantleftcum floorcum -cumshot
                    "Or else they spray the same into her face."
                    "The whole time this is happening, I can hear the guys attached to those cocks."
                    "Their moans of pleasure can he heard through the thin walls of the booth."
                    show alexis ntr glory hole peace -cumshot handcum
                    "Hell, I can even hear some of them slamming their hands against the walls too!"
                    "At least I think they're hitting the walls..."
                    show alexis ntr glory hole -leftman
                    "Some of them might be scraping their nails down the other side!"
                    "I have to admit that I never knew Alexis was this good."
                    "I'm one hell of a lucky guy to be able to get back with her!"
                    show alexis ntr glory hole futa
                    "She pleases all of those guys, one after another."
                    "And she never slows down for a moment, taking it all in the face."
                    show alexis ntr glory hole -peace -handcum
                    "So by the time she crawls over to me, Alexis is a sticky mess."
                    "Despite all the cocks she's already had, Alexis still wants mine!"
                    show alexis ntr glory hole wantrightcum
                    "And when she has it in her hands, she gets straight to work."
                    "Everything that I've watched her do to the other cocks was just practice."
                    "It was all just a rehearsal for what she's doing to me right now."
                    "Alexis caresses my cock, first with her hands and then with her tongue."
                    show alexis ntr glory hole rightblowjob -wantrightcum
                    "She works from bottom to top, building up the intensity as she goes."
                    "Now I can begin to feel some of the thrill that Alexis must get from this."
                    "She's involving me in the show, giving everyone something to watch."
                    "And far from killing my vibe, it's making me feel hotter than ever!"
                    show alexis ntr glory hole closed cumdickright
                    "As I watch Alexis's head bobbing up and down, I know I'm not alone."
                    "And when I feel myself letting go, we're being watched too."
                    show alexis ntr glory hole cumshot wallcum facecum with hpunch
                    "I gasp helplessly as I cum with my cock in Alexis's mouth."
                    with hpunch
                    "But she handles it like a pro, swallowing all I have to give."
                    show alexis ntr glory hole alexisleftcum with hpunch
                "Watch from outside the booth":
                    "I think about it for a moment, weighing up the possibilities."
                    "But then I shake my head, turning down the offer."
                    mike.say "Nah, I'm good, Alexis."
                    mike.say "I wouldn't want to cramp your style."
                    "For a moment I think Alexis is going to protest."
                    "But then she shrugs and gives me a little wave."
                    show alexis ntr glory hole alexis peace
                    "The next moment she slips through the door into the booth."
                    "I don't waste any time in finding one of the unoccupied slots."
                    show alexis ntr glory hole watch
                    "And then I settle down, intending to watch the proceedings in secret."
                    "Alexis stands in the middle of the booth, looking around her."
                    show alexis ntr glory hole dickright
                    "There are already anonymous cocks appearing through the holes."
                    show alexis ntr glory hole futa
                    "They're of all colours, shapes and sizes imaginable."
                    "And Alexis turns on the spot, taking them all in."
                    show alexis ntr glory hole dickleft
                    "I wasn't going to add mine to the mix."
                    "But I see Alexis pause and stare at the empty hole under my viewing slot."
                    "There's no way she can know who's behind the hole."
                    "And yet her eyes seem to be looking straight at me."
                    "It's like she's willing me to put it through the hole!"
                    show alexis ntr glory hole mike
                    "So in the end I relent, undoing my flies and getting my cock out."
                    show alexis ntr glory hole -peace
                    "Only when I slide it through the hole does Alexis move on."
                    "Without warning, one of the other cocks seems to catch her eye."
                    "Alexis pounces on it like a cat seizing its prey."
                    "And what follows is a staggering display of sexual appetite."
                    show alexis ntr glory hole wantleftcum
                    "Lips, tongue and fingers all come into play as Alexis gets to work."
                    "Some cocks she uses her hands to pleasure."
                    "Rubbing the shafts and tormenting the heads."
                    show alexis ntr glory hole leftblowjob -wantleftcum
                    "Others she takes into her mouth as well."
                    "And of these, some are given little more than a playful suck."
                    show alexis ntr glory hole cumdickright
                    "But the lucky ones are almost swallowed hole."
                    "These she goes at as if her life depends on it."
                    show alexis ntr glory hole cumshot closed
                    "Part of me was worried that I just wouldn't be able to handle all of this."
                    "That I'd be overcome with jealousy the moment I saw Alexis touch another guy's cock."
                    show alexis ntr glory hole ahegao stand -cumshot alexisrightcum
                    "And yet it's the sheer look of delight on her face that truly grabs my attention."
                    "I don't think I've ever seen Alexis look so alive as she does right now!"
                    show alexis ntr glory hole peace -futa handcum
                    "Maybe I'm starting to understand what it is that she gets out of this."
                    "Maybe it's not about the dangerous thrill of cheating on someone after all."
                    "Perhaps that's why she chooses to leave me until last?"
                    show alexis ntr glory hole leftman
                    "One by one the cocks poking through the holes are spent."
                    "They either spurt cum onto Alexis's hands."
                    show alexis ntr glory hole -peace -handcum
                    "Or else they spray the same into her face."
                    "The whole time this is happening, I can hear the guys attached to those cocks."
                    show alexis ntr glory hole leftblowjob
                    "Their moans of pleasure can he heard through the thin walls of the booth."
                    "Hell, I can even hear some of them slamming their hands against the walls too!"
                    show alexis ntr glory hole cumdickleft
                    "At least I think they're hitting the walls..."
                    "Some of them might be scraping their nails down the other side!"
                    show alexis ntr glory hole cumshot opened
                    "I have to admit that I never knew Alexis was this good."
                    "I'm one hell of a lucky guy to be able to get back with her!"
                    show alexis ntr glory hole stand wantleftcum
                    "She pleases all of those guys, one after another."
                    "And she never slows down for a moment, taking it all in the face."
                    show alexis ntr glory hole -cumshot -wantleftcum floorcum
                    "So by the time she crawls over to me, Alexis is a sticky mess."
                    "Did she leave me until last by a simple accident?"
                    "Or did she somehow guess that I was the last to join the party?"
                    show alexis ntr glory hole wantrightcum
                    "Despite all the cocks she's already had, Alexis still wants mine!"
                    "And when she has it in her hands, she gets straight to work."
                    "Everything that I've watched her do to the other cocks was just practice."
                    "It was all just a rehearsal for what she's doing to me right now."
                    "Alexis caresses my cock, first with her hands and then with her tongue."
                    show alexis ntr glory hole rightblowjob -wantrightcum
                    "She works from bottom to top, building up the intensity as she goes."
                    "Now I can begin to feel some of the thrill that Alexis must get from this."
                    "She's involving me in the show, giving everyone something to watch."
                    show alexis ntr glory hole closed
                    "And far from killing my vibe, it's making me feel hotter than ever!"
                    "As I watch Alexis's head bobbing up and down, I know I'm not alone."
                    "And when I feel myself letting go, we're being watched too."
                    show alexis ntr glory hole cumshot wallcum facecum with hpunch
                    "I gasp helplessly as I cum with my cock in Alexis's mouth."
                    with hpunch
                    "But she handles it like a pro, swallowing all I have to give."
                    show alexis ntr glory hole alexisleftcum with hpunch
            show alexis ntr glory hole stand peace handcum -cumshot -wantleftcum -wantrightcum -dickleft -dickright
            "Afterwards, the cocks disappear back into their holes one by one."
            "And Alexis lets herself out of the booth, still panting from her efforts."
            show alexis ntr glory hole pleasure -leftman -futa -rightman -mike -watch
            "She makes an effort to clean herself up and look presentable."
            "But I can see there's still an almost manic glint in her eyes."
            hide alexis
            show alexis casual blush
            with fade
            mike.say "Erm, Alexis..."
            mike.say "Are you feeling okay?"
            show alexis happy
            alexis.say "Oh, I feel better than okay, [hero.name]!"
            alexis.say "In fact, I haven't felt this alive in forever!"
            show alexis normal
            alexis.say "Seriously, thanks for letting me do this."
            alexis.say "And thanks for being so understanding too."
            show alexis -blush
            "I smile and nod, allowing Alexis to shower me with praise."
            "But it's not like I didn't get something out of this myself."
            "And I'm already wondering if she'll be up for doing it again sometime in the future..."
            $ alexis.love += 10
    return

label ceo_office_spy_camera:
    show chibi spy
    "It takes a little while, but I managed to sneak in Dwayne's office and find a good spot for the camera."
    $ game.flags.ceoofficecameraplaced = True
    $ hero.lose_item("spy_camera")
    return


label alexis_event_ntr_03:
    scene expression f"bg {game.room}"
    with fade
    "So okay, I'm kind of coming to terms with the fact that Alexis has certain quirks."
    "Certain unusual aspects to her personality and appetites that make things interesting."
    "I never knew about them back when we were in high-school - and maybe she didn't either."
    "But it's not like I just have to sit back and accept them in a passive sense, is it?"
    "I mean, I can...make use of them for my own gratification, can't I?"
    "Because Alexis is lucky that I'm willing to put up with that kind of thing."
    "So the least I can ask in return is to get something out of it for myself."
    "That's why I've invited Alexis into work with me today."
    "Sure, I passed it off as nothing more than a chance to see where I work."
    "But I know that Dwayne's going to be in the office today."
    "And I know that Alexis is his type too."
    "All I have to do is let him see her, then stand back and watch!"
    show alexis casual with dissolve
    alexis.say "Hmm..."
    alexis.say "I've got to admit it, [hero.name]..."
    alexis.say "You've done okay for yourself!"
    mike.say "Thanks, Alexis."
    mike.say "I guess all that studying in high-school paid off!"
    "I barely hear the sound of someone walking into the room."
    "In fact, I'm more aware of the way everyone is suddenly trying to look busy."
    "And I can almost smell the most expensive cologne imaginable on the air."
    "All of which tells me that Dwayne just made his entrance."
    "I hardly need to turn in the direction of the scent before he makes himself known to me."
    show dwayne at left with dissolve
    dwayne.say "Well, well, well..."
    dwayne.say "Now what do we have here?"
    mike.say "Oh, hey, Dwayne."
    mike.say "How are you doing?"
    "Dwayne doesn't even make eye-contact with me."
    "Instead he focuses all of his attention on Alexis."
    dwayne.say "Where are your manners, [hero.name]?"
    dwayne.say "Aren't you going to introduce me to your charming guest here?"
    "I do my best to look genuinely embarrassed."
    "But I can already see the effect that Dwayne's having on Alexis."
    "How can she resist a guy that exudes such alpha-male hormones?"
    mike.say "Oh...uh...yeah!"
    mike.say "Alexis, this is Dwayne."
    mike.say "He's my boss."
    "At this, Dwayne lets out a booming laugh and shakes his head."
    dwayne.say "What [hero.name] here is trying to say is that I'm the CEO."
    dwayne.say "I'm the big cheese, the head honcho."
    dwayne.say "Basically, the buck stops here!"
    "Dwayne points at his own jutting chin, just to add emphasis to the statement."
    show alexis wink
    "Alexis giggles and does that weird thing she does with her eyes."
    "And it's then I know she's caught, hook, line and sinker!"
    mike.say "Dwayne, this is Alexis."
    mike.say "She was my girlfriend back in high-school."
    show fx question at left
    dwayne.say "WAS your girlfriend?"
    dwayne.say "Does that mean she's a free-agent?"
    mike.say "Erm...no, Dwayne."
    mike.say "We're kind of back together - right, Alexis?"
    show alexis normal
    alexis.say "Yeah, yeah...whatever!"
    alexis.say "It's kind of a casual arrangement, you know?"
    dwayne.say "Sounds good to me, Alexis!"
    dwayne.say "How about I give you the grand tour of the place?"
    dwayne.say "The one with executive level access!"
    mike.say "But I was..."
    dwayne.say "I'm sure you have some work to be getting on with."
    show dwayne annoyed
    dwayne.say "Right, [hero.name]?"
    mike.say "But, Alexis..."
    alexis.say "Don't worry, [hero.name]."
    show alexis happy
    alexis.say "You just go do what you've got to do."
    alexis.say "I'm sure Dwayne can handle me on his own!"
    show dwayne normal
    "With that they walk off together, laughing and joking."
    hide alexis
    hide dwayne
    with moveoutleft
    "Well, more like with Dwayne doing the joking and Alexis the laughing."
    "Quick as a flash, I duck into my office and close the door behind me."
    "I think about pulling up the feed from the camera I have hidden in Dwayne's office."
    "But then I shake off the instinct and do a little actual work instead."
    "Better to leave them to get down to it and check the recording later."
    "I'm convinced I won't be able to get my head down and work."
    "But somehow I manage it, and soon I'm engrossed."
    play sound door_knock
    "I only look up a while later when I hear someone knocking at my office door."
    mike.say "Who's there?"
    show alexis casual normal at left with easeinleft
    alexis.say "It's only me, [hero.name]."
    alexis.say "Dwayne just got done showing me around."
    alexis.say "So I'm going to head off, okay?"
    mike.say "Sure, Alexis, sure..."
    mike.say "I have a couple of things I need to take care of around here."
    mike.say "But I'll call you later, okay?"
    show alexis flirt
    "Alexis nods and blows me a kiss before she disappears."
    hide alexis with moveoutleft
    "I force myself to wait a good couple of minutes after she's gone."
    "Then I log onto my computer and pull up the recent footage."
    "This is it, the point of no return."
    "Do I go through with this thing or not?"
    menu:
        "Watch the footage":
            "I'm one hundred percent certain that Dwayne will have gone out of his way to fuck Alexis."
            "And I know her well enough to be sure that she won't have been able to resist his advances too."
            "I'm also sure that it'll have happened in his palatial office, as the climax of the tour."
            "If you'll pardon the unfortunate pun..."
            scene bg ceo
            show layer master at glitch
            pause .1
            show layer master at glitch
            pause .1
            show layer master at glitch
            pause .1
            show layer master at glitch
            pause .1
            show layer master at animated_glitch
            "So I hit play and search the footage for Alexis and Dwayne."
            "Soon enough I see the doors of his office swing open."
            show dwayne at center
            show alexis casual at left
            with moveinleft
            "And Dwayne leads a suitably impressed Alexis inside."
            scene bg ceo
            show dwayne at center
            show alexis casual at left
            dwayne.say "Here we are, Alexis."
            show dwayne at right5 with ease
            dwayne.say "This is the nerve-centre of my empire!"
            alexis.say "Wow, Dwayne!"
            show alexis surprised at left5 with ease
            alexis.say "This is some office!"
            alexis.say "It's like something you'd see in a movie!"
            dwayne.say "You bet it is - that's exactly what I want people to think!"
            dwayne.say "Big doors, big windows, big desk - everything larger than life!"
            show alexis normal at left4 with ease
            "I watch as Alexis sidles over to the desk and leans on the edge."
            alexis.say "What's the point of a desk this big though?"
            alexis.say "It's like the size of a fucking pool table!"
            show dwayne at right5, startle
            "Dwayne lets out one of his patented booming laughs."
            show layer master at animated_glitch
            "And I can see that he's already loosening his tie!"
            dwayne.say "I could say it's to put people in their place."
            dwayne.say "To put a barrier between them and me."
            scene bg ceo
            show dwayne at right5
            show alexis casual at left4
            dwayne.say "But the truth is that I like to fuck on it!"
            show alexis wink at left4, startle
            "Alexis giggles at this, biting her lip in anticipation."
            "She turns to face Dwayne, sitting on the edge of the desk."
            show alexis normal blush
            alexis.say "So that's what happens at the end of the tour, huh?"
            "Dwayne gives this a nonchalant shrug as he takes off his jacket."
            dwayne.say "That's how I see this thing going down, Alexis."
            dwayne.say "And you're not exactly running for the door!"
            alexis.say "You know [hero.name] and I are a thing, right?"
            alexis.say "You know that and you still want to do this?"
            show layer master at animated_glitch
            show alexis naked blush with dissolve
            "Both of them are stripping off now."
            "Alexis leaning further back on the desk and Dwayne getting ever closer."
            scene alexis ntr office
            show alexis ntr office noguy
            show layer master at glitch
            pause .1
            show layer master at glitch
            pause .1
            show layer master at glitch
            pause .1
            show layer master at glitch
            pause .1
            show layer master at animated_glitch
            dwayne.say "I'm just his boss, Alexis."
            dwayne.say "You're the one in a relationship with the guy."
            if not cassidy.is_gone_forever and cassidy.sexperience >= 1:
                dwayne.say "Anyway, he fucks my daughter, I fuck his high-school sweetheart."
            else:
                dwayne.say "Turnaround's fair play!"
            scene alexis ntr office -noguy
            "Before Alexis can offer an answer, Dwayne is on top of her."
            "She lets out a wail of surprise as he parts her legs and pushes her backwards."
            "But it soon turns into a moan of pleasure as she gets a look at his cock."
            "Look, I'm not going to try and downplay that thing."
            "Dwayne's really packing down there!"
            "And he's more than eager to introduce Alexis to it as well!"
            show alexis ntr office vaginal
            "But he's also got that swagger and arrogance that comes from knowing he's an alpha male too."
            "Dwayne doesn't ask for permission or try to sense what Alexis might want from this encounter."
            "And that's because all he's thinking about is what he's going to get out of it."
            "She's just another notch on his belt, another trophy for his cabinet."
            "Alexis is flat on her back as Dwayne pushes his cock into her."
            "She gasps as it inches into her pussy, and he grunts at the same time."
            "Dwayne all but pins Alexis to the desk."
            "He uses his superior size and weight to bend her to his will."
            "Alexis's head is rolling from side to side on the desk."
            "Her mouth hangs open as she's pounded to within an inch of her life."
            "Dwayne has his hands on her naked breasts, pawing them at his leisure."
            "But he's not gentle in the way he touches them."
            "His broad fingers squeeze and pinch, making Alexis writhe and wriggle."
            "The sight makes me reach down and begin to stroke my own cock."
            "When did I undo my flies and get it out?"
            "I don't remember starting to masturbate to this!"
            "But now that I'm into it, I can't stop myself!"
            "Soon enough, I'm gasping and panting too."
            "Every time Dwayne thrusts himself into Alexis, I swear I feel it."
            "I know what it feels like to be inside of that pussy."
            "I know how it feels to shoot my load so deep inside of Alexis!"
            "So when Dwayne lets out a massive grunt and all but climbs on top of her, I know what's happening."
            show alexis ntr office ahegao creampie
            "Alexis whimpers as Dwayne cums inside of her, and I gasp too."
            "I can't see what's happening between Alexis's legs on the footage."
            "But I can feel the warm cum running over my own hand."
            show layer master at glitch
            pause .1
            show layer master at glitch
            pause .1
            show layer master at glitch
            pause .1
            show layer master at glitch
            pause .1
            show layer master at animated_glitch
            pause 2.0
            scene expression f"bg {game.room}" with fade
            "Desperate to clean myself up, I turn off the video and search for a tissue."
            "At the same time, my mind is racing."
            "What am I going to do with the footage?"
            menu:
                "Blackmail Dwayne":
                    "Well, that's obvious, isn't it?"
                    "I'm going to use it to screw Dwayne as hard as he just screwed Alexis!"
                    "All I have to do is figure out how to use the footage."
                    "That and work out what I actually want out of the deal for myself."
                    "And when I do, Dwayne won't know what hit him!"
                    $ game.flags.alexisfootage = "blackmail"
                "Keep the footage as leverage":
                    "Hmm..."
                    "You know, I never actually thought what I was going to do with it."
                    "Oh, I was always going to use the footage to blackmail Dwayne."
                    "But I never sat down and worked out just how I'd do it."
                    "Maybe I don't need to be so specific?"
                    "Having something like this up my sleeve is always good."
                    "Perhaps I should just bide my time, save it for when I really need it?"
                    $ game.flags.alexisfootage = "leverage"
                "Wipe the footage out of regret":
                    "I can already feel the guilt beginning to churn in my guts."
                    "What in the hell am I actually thinking?!?"
                    "I've basically just handed Alexis over to Dwayne."
                    "I've let him have his way with her, and for what?"
                    "So that I can blackmail him if I ever feel the need?!?"
                    "Am I not supposed to be better than this?"
                    "I feel like I'm becoming the bad guy in my own story!"
                    "Taking a deep breath, I select the footage from the folder."
                    "And then I delete it, making sure to empty the recycle bin too."
                    "Then I sit back in my chair, shaking my head."
                    "Okay, so...damage limitation."
                    "On the one hand, I basically set Alexis up to get fucked by Dwayne."
                    "But on the other, I didn't actually watch them have sex in his office."
                    "So at least I have plausible deniability."
                    "I just have to smarten myself up in future."
                    "I have to keep from getting myself in a mess like this again."
                    $ game.flags.alexisfootage = "watched"
        "Don't watch the footage":
            "I'm about to play the footage when a thought occurs to me."
            "What in the hell am I actually thinking?!?"
            "I've basically just handed Alexis over to Dwayne."
            "I've let him have his way with her, and for what?"
            "So that I can blackmail him if I ever feel the need?!?"
            "Am I not supposed to be better than this?"
            "I feel like I'm becoming the bad guy in my own story!"
            "Taking a deep breath, I select the footage from the folder."
            "And then I delete it, making sure to empty the recycle bin too."
            "Then I sit back in my chair, shaking my head."
            "Okay, so...damage limitation."
            "On the one hand, I basically set Alexis up to get fucked by Dwayne."
            "But on the other, I didn't actually watch them have sex in his office."
            "So at least I have plausible deniability."
            "I just have to smarten myself up in future."
            "I have to keep from getting myself in a mess like this again."
            $ game.flags.alexisfootage = "delete"
    $ hero.flags.alexis_dwayne_encounter = TemporaryFlag(True, 3)
    return

label alexis_blackmail_dwayne:
    scene expression f"bg {game.room}"
    "I feel like I have all the ammunition I need to confront Dwayne and make my demands."
    "The footage of him banging Alexis in his office is safely stored away and backed-up."
    "So there's no way that he can deny what happened or destroy the evidence I have."
    "If the news gets out that he's been fucking on company time, it won't be good."
    show dwayne annoyed with dissolve
    "Dwayne might be the CEO of the company, but he still has an image to maintain."
    "Plus he'll have to explain himself to his wife and daughter if I let them see the footage."
    "But rather than go charging in, I try to approach the whole thing casually at first."
    mike.say "Oh, hey, Dwayne..."
    mike.say "Alexis asked me to thank you for giving her a tour of the office."
    mike.say "She really enjoyed herself!"
    show dwayne normal at center, zoomAt (1.2, (640, 850))
    "Dwayne greets this with his characteristic grin."
    "And I can see that the mere mention of Alexis's name peaks his interest."
    "I guess that's the pleasant memories of what they got up to coming back to the surface."
    dwayne.say "No sweat, [hero.name]."
    dwayne.say "It was my pleasure."
    dwayne.say "She's a real fun girl to be around!"
    mike.say "Yeah, I know."
    mike.say "You looked like you were having a ball."
    mike.say "Especially when you were fucking her in your office!"
    "For a moment the reality of what I just said doesn't seem to register on Dwayne's face."
    show dwayne annoyed
    "But then I see his smile vanish and the look in his eyes harden as it dawns on him."
    dwayne.say "Oh, I see."
    dwayne.say "She told you about that, did she?"
    mike.say "No, Dwayne, she didn't."
    mike.say "But I had a little spy tape the whole thing for me."
    mike.say "The footage is stored away somewhere nice and safe."
    mike.say "And that's where it'll stay."
    mike.say "So long as you give me what I want."
    "Dwayne crosses his arms over his chest, regarding me with interest."
    "I can see that he's turning it over in his mind, weighing up his options."
    "All I can do is hold his eye, trying to keep a poker face as I do so."
    if hero.charm > 95:
        "Dwayne lets out a huffing sigh."
        "Then he gives me one quick nod of the head."
        show dwayne normal
        dwayne.say "Okay, [hero.name], okay."
        dwayne.say "This isn't my first dance."
        dwayne.say "What do you need to make this all go away?"
        "I feel a rush of adrenaline at the realisation that my efforts worked."
        "But I do all I can to keep a handle on things as I reel off my demands."
        $ renpy.dynamic("reward")
        menu:
            "Ask for money":
                mike.say "Don't worry, Dwayne."
                mike.say "I don't want to be king of the world."
                mike.say "All I want is a generous donation to my bank balance!"
                $ reward = "money"
            "Ask for a promotion" if not game.flags.capped_promotion:
                mike.say "I think my talents are wasted at my current pay-grade."
                mike.say "I could be of much better use a couple of rungs up the ladder."
                mike.say "If you know what I mean?"
                $ reward = "promotion"
        "Dwayne nods again, more slowly this time."
        show dwayne annoyed
        dwayne.say "That's something I can make happen."
        dwayne.say "Just give me a little time to get it done."
        dwayne.say "We're going to need to make it look legit."
        "Now that the deal's done, Dwayne seems to relax a little."
        "His smile returns and he looks me up and down with what could be respect."
        show dwayne normal
        dwayne.say "You know something, [hero.name]..."
        dwayne.say "You've got some balls on you - and I like that!"
        dwayne.say "But that Alexis...phew!"
        dwayne.say "She was well worth what this is going to cost me!"
        "I force a smile onto my face and try to look like I'm amused."
        "After all, I should be smiling and joking along with Dwayne right now."
        "I got what I wanted."
        "And maybe even earned a little more respect from Dwayne."
        "So it's got to have been worth it, right?"
        if reward == "promotion":
            $ game.flags.promoted += 1
        else:
            $ hero.money += 5000
    else:
        "Dwayne shakes his head and lets out a booming laugh."
        show dwayne normal
        dwayne.say "Nice try, [hero.name]!"
        dwayne.say "But you're going to have to do better than that!"
        mike.say "Wh...what are you talking about, Dwayne?"
        mike.say "I've got the footage of you and Alexis!"
        mike.say "Don't you realise what that means?"
        show dwayne at startle
        "Dwayne rolls his eyes and laughs again."
        dwayne.say "So what if you do?"
        show dwayne annoyed
        dwayne.say "It's not like I did anything wrong."
        dwayne.say "You fed that tasty little morsel to me yourself."
        dwayne.say "And believe me, she wanted everything she got!"
        mike.say "But if people around here find out..."
        show dwayne angry
        dwayne.say "Please, spare me the moral bullshit!"
        dwayne.say "The women working here already think I'm a player."
        dwayne.say "Half of them hate me for it."
        dwayne.say "And the other half are hot for me for the same reason!"
        dwayne.say "All it does with the guys is impress them!"
        mike.say "What about your wife?!?"
        mike.say "What about your daughter?!?"
        show dwayne annoyed
        dwayne.say "What about them?"
        dwayne.say "Without me they're out on their asses!"
        dwayne.say "So I get to have my fun - no guilt and no consequences!"
        "I open my mouth to protest."
        "But then I realise that I've run out of options."
        "Dwayne leans in and slaps me on the back."
        show dwayne normal
        dwayne.say "Aw, don't feel too bad, [hero.name]."
        dwayne.say "I'm guessing this was your first time trying to blackmail someone?"
        dwayne.say "Look, I'll do you a favour - I'll let it go this time."
        dwayne.say "I'll forget that you set me up, breached my privacy and pimped out your own girl!"
        show dwayne at startle
        "With that, Dwayne lets out another booming laugh."
        hide dwayne with easeoutleft
        "Then he turns and walks away, leaving me alone and defeated."
    scene bg black with dissolve
    return

label alexis_event_ntr_04:
    scene bg restaurant with fade
    "It's been a few days since I invited Alexis to my office so that she could see where I work."
    "Or if I'm more honest, so that I could tempt Dwayne into having sex with her in his office."
    "Yeah, yeah, yeah - spare me the moral outrage!"
    "It's a dog-eat-dog environment in that office, you know?"
    "And I needed to think outside of the box to get an advantage!"
    "Anyway, the problem is that Alexis won't stop talking about it."
    show alexis normal with dissolve
    "Of course she doesn't just come right out and say how great it was fucking Dwayne on his desk."
    "Instead she keeps on mentioning how cool and confident the guy was."
    "How he dresses like a real alpha male and has the huge office all to himself."
    scene bg bedroom1
    show alexis normal with fade
    "In the end, I feel like I have to at least try to stand up for myself."
    "Plus we're hanging out in my bedroom right now."
    "So I'd rather talk about how great I am instead!"
    mike.say "Yeah, yeah, yeah..."
    mike.say "Dwayne talks a good fight, Alexis."
    mike.say "But he's not as smart as he thinks he is!"
    show alexis confused
    "Alexis smirks and looks at me sideways."
    "All in all, she seems less than convinced."
    alexis.say "Aw, come on, [hero.name]!"
    show alexis normal
    alexis.say "At least try not to sound so jealous of the guy!"
    show alexis annoyed
    alexis.say "It's kind of pathetic, you know?"
    "Alexis's tone is so condescending."
    "Before I know what I'm doing, I'm firing back."
    mike.say "Oh yeah?!?"
    mike.say "Well if he's so perfect, answer me this..."
    mike.say "How come I managed to plant a spy camera in his office?!?"
    show alexis surprised at startle
    "I hear the gasp Alexis before I realise what I've said."
    "She shakes her head in sheer amazement at what she's hearing."
    show alexis at center, zoomAt (1.2, (640, 840))
    alexis.say "Are you serious?!?"
    show alexis normal
    alexis.say "You can see whatever happens in his office?"
    alexis.say "So you could have..."
    "I can literally see the pieces falling into place in Alexis's mind."
    "And at the same time I'm feeling a strange mixture of emotions."
    "Sure, there's shame and even a little bit of fear at how she'll react."
    "But there's also a good amount of defiant pride inside of me too."
    "Because I just proved she's not the only one with secrets."
    mike.say "Yeah, Alexis, you got it."
    mike.say "That camera was recording the whole time."
    mike.say "So I know what you and Dwayne got up to the other day too."
    alexis.say "That was your idea?"
    show alexis annoyed
    alexis.say "Did you and he..."
    mike.say "What?!?"
    mike.say "No way - Dwayne wasn't in on it."
    mike.say "I just know that he can't keep his hands off hot girls."
    mike.say "I was going to use the footage as leverage against him."
    mike.say "You know, if I ever had to resort to blackmail or whatever?"
    "I look away from Alexis, waiting to hear her freak out."
    "Waiting to feel the sting of her slapping me across the face too!"
    "But instead, when she speaks up, she sounds oddly calm."
    show alexis blush normal
    alexis.say "That's...really turning me on!"
    mike.say "HUH?!?"
    mike.say "You...you mean you're not mad with me?"
    show alexis annoyed
    alexis.say "It's a little freaky, sure."
    show alexis normal
    alexis.say "But I kind of like guys taking control like that..."
    alexis.say "And now I find you were controlling Dwayne and me the whole time!"
    alexis.say "Can you show me the footage?"
    alexis.say "I really want to see it from your point of view!"
    if game.flags.alexisfootage == "delete":
        mike.say "Sorry, Alexis..."
        mike.say "My conscience got the better of me."
        mike.say "I deleted the video after the first time I watched it!"
        show alexis annoyed -blush
        alexis.say "Y...you did?"
        alexis.say "Aw, hell!"
        "She sighs and shakes her head."
        alexis.say "Well, I guess I should be thankful you did that."
        show alexis normal
        alexis.say "I suppose it means that you're a good guy after all."
        alexis.say "A boring guy too - but a good one."
        mike.say "Erm..."
        mike.say "Thanks, Alexis."
        mike.say "I think..."
        "Alexis clams up after that, and I do the same."
        "I'm more than willing to let the matter drop."
        $ alexis.love += 2
    else:
        mike.say "Y...you do?!?"
        mike.say "Okay, okay..."
        mike.say "I can get to it on my phone..."
        show alexis at center, zoomAt (1.5, (640, 1040)) with dissolve
        "Alexis snuggles closer to me as I hunt for the footage."
        "And it feels like we're settling down to watch the latest binge-worthy series on download."
        scene bg ceo
        show alexis casual at left5
        show dwayne at right5
        show layer master at glitch
        pause .1
        show layer master at glitch
        pause .1
        show layer master at glitch
        pause .1
        show layer master at glitch
        pause .1
        show layer master at animated_glitch
        "The familiar scene begins to play out on the screen of my phone."
        "And at the same time, I feel Alexis's hand on my groin."
        scene bg bedroom1
        show alexis casual normal at center, zoomAt (2.0, (640, 1300))
        with fade
        alexis.say "Did you watch all of it?"
        alexis.say "From start to finish?"
        mike.say "Ah..."
        mike.say "Yeah, Alexis..."
        mike.say "I watched the whole thing!"
        "Slowly and without asking permission, she unzips my flies."
        "I'm already as hard as I can get, stiff as a fucking board."
        "And that seems to meet with Alexis's approval, as I hear her chuckle."
        show alexis blush
        alexis.say "Did you get this hard when you were watching?"
        mike.say "Oh yeah!"
        alexis.say "That's good, [hero.name]."
        show alexis wink
        alexis.say "I like that I can make you that hard when were not even in the same room!"
        scene alexis ntr office
        show layer master at glitch
        pause .1
        show layer master at glitch
        pause .1
        show layer master at glitch
        pause .1
        show layer master at glitch
        pause .1
        show layer master at animated_glitch
        "The footage is at the point where both Alexis and Dwayne are naked."
        "I watch as he pushes her backwards onto the desk, almost holding my breath."
        alexis.say "Mmm..."
        alexis.say "I like that..."
        alexis.say "Him taking charge like that."
        scene alexis ntr office
        alexis.say "And seeing his cock too."
        alexis.say "Just knowing what he's going to do with it!"
        "As if to make her point, Alexis squeezes my own cock inside my pants."
        alexis.say "The only thing better is actually feeling it going in!"
        alexis.say "Something that big, your muscles strain and stretch."
        alexis.say "For a moment you're sure it just won't fit."
        alexis.say "And then something gives, and it's filling you up!"
        mike.say "Y...you like them best when..."
        mike.say "When they're big?"
        alexis.say "Oh yeah, of course."
        alexis.say "But I like it better when they're big AND clever!"
        scene bg bedroom1
        show alexis casual normal blush at center, zoomAt (2.0, (640, 1300))
        with fade
        "I look down just in time to see Alexis pull my cock out of my pants."
        "She rubs it with one hand and bats the phone away with the other."
        "I get the message, tossing it onto the bed."
        "And instead I focus all of my attention on her."
        show alexis normal
        alexis.say "I wasn't thinking about Dwayne when he was fucking me, [hero.name]."
        mike.say "You weren't?"
        with vpunch
        "Pushing me down on the bed, she starts to pull down my pants."
        alexis.say "No way."
        show alexis flirt naked with dissolve
        "Instants later, she's naked, letting me wondering how she managed to made her clothes disappear."
        alexis.say "I'm never thinking about the other guys when they fuck me."
        scene alexis bj
        show alexis bj chub
        with fade
        "Alexis's head is hovering over my groin by now."
        "Her lips are mere inches from the head of my cock."
        alexis.say "I'm always thinking about what you'd do if you could see me fucking them!"
        show alexis bj hard
        "Before I can summon the will to answer, Alexis pounces."
        "Her lips close around the head of my cock."
        "And then she's working away at me, tongue, lips and all."
        show alexis bj blowjob
        "I brace myself on the bed, trying to let her have her way."
        "At the same time I can hear what's going on with the footage."
        "I can hear Dwayne talking on the video."
        dwayne.say "I'm just his boss!"
        dwayne.say "You're the one in the relationship with the guy!"
        "The first time I heard them, his words really hit home."
        "But now I know what was going through Alexis's mind that whole time."
        "I watch her head going up and down as she pleasures me."
        "She was thinking about me all the time she was fucking Dwayne."
        "Yeah, she might have been making a cuc out of me."
        show alexis bj close
        "But the guy was just a means to an end."
        "Maybe I can live with that?"
        "I lean back on the bed, enjoying the sensations of Alexis's lips and tongue."
        show alexis bj speed
        show sexinserts head alexis zorder 1 at center, zoomAt(1, (-140, 870))
        "She's going at me like her life depends on it, really exerting herself."
        "There was none of that when she was with Dwayne, just effort on his part."
        "Seems like Alexis is really flogging herself to get me off!"
        "And it's the mere thought of that which pushes me over a few moments later."
        show sexinserts head alexis cum zorder 1 at center, zoomAt(1, (-140, 870))
        show alexis bj -speed cum inmouth
        with vpunch
        "I shoot my load into Alexis's mouth, but she's ready for me."
        with vpunch
        "Without choking or gagging, she swallows it down in a couple of gulps."
        hide sexinserts
        show alexis bj -cum -inmouth hard open
        "And then she smiles up at me, her eyes beaming with satisfaction."
        $ alexis.love += 3
    $ hero.replace_activity()
    $ alexis.flags.ntr_delay = TemporaryFlag(True, 3)
    return

label alexis_event_ntr_05_intro:
    scene expression f"bg {game.room}" with fade
    "I know that Alexis and I have been through more than a little drama since we got back together."
    "Drama that's mainly been caused on account of her...what shall we call it - her problem?"
    "And maybe I should have been able to wrap my head around it by now, come to terms with it."
    "I mean, we're older and supposedly wiser now than we were back in high-school."
    "And she's not exactly trying to hide that side of her personality from me either."
    "But the problem is that this whole thing feels like a scab I just can't stop picking at."
    "No matter how I try to rationalise it, no matter how much I love being back with Alexis."
    "I'm still trying to be okay with her basically cheating on me whenever the whim takes her!"
    "And maybe that's the real problem."
    "I'm trying to make sense of this in my own head."
    "Maybe Alexis can explain this to me more easily?"
    "Oh shit...this is going to be tough!"
    "But I have to ask her the question..."
    show alexis normal with dissolve
    mike.say "Alexis..."
    mike.say "I need to talk to you...seriously!"
    show alexis sad
    "Instantly I see the expression on Alexis's face become concerned."
    "I guess she has to know what this is going to be about."
    show alexis annoyed
    alexis.say "S...sure, [hero.name]."
    alexis.say "What did you want to say to me?"
    mike.say "Well...this thing that you like to do..."
    mike.say "With other guys..."
    mike.say "Is it because I'm not enough for you?"
    mike.say "I mean, is it because I could be doing more to please you?"
    mike.say "Because if it is, just tell me what to do, and I'll do it!"
    "Alexis shakes her head, looking genuinely upset by what I just said."
    show alexis at center, zoomAt(1.5, (640, 1040))
    "She grabs hold of my hand, squeezing it so tight I almost wince."
    show alexis angry
    alexis.say "Oh god, [hero.name]!"
    alexis.say "Please don't ever think that!"
    alexis.say "I couldn't wish for a better lover than you."
    show alexis normal
    alexis.say "And more than that - I'm IN love with you too!"
    "I nod, trying as best I can to understand."
    mike.say "But..."
    mike.say "You still need more?"
    alexis.say "You have to understand, [hero.name]."
    alexis.say "What we have is different - special."
    alexis.say "You could even say it's unique."
    mike.say "So you're saying those other guys..."
    mike.say "They don't mean as much to you?"
    mike.say "They're like...playthings that you use and then throw away?"
    show alexis confused
    "Alexis frowns a little, like she doesn't fully agree with me."
    "But I can see that she doesn't totally disagree either."
    alexis.say "That might be a bit strong."
    alexis.say "I don't see them as objects I can use and toss aside."
    alexis.say "I need to know that they want me, that they desire me."
    alexis.say "But it's not like I care about them once it's over."
    alexis.say "So long as they get that, everyone's usually happy."
    "Alexis pauses and takes a deep breath."
    "She holds it in for a moment, then lets it out as a sigh."
    show alexis normal
    alexis.say "Everyone but you, [hero.name]!"
    alexis.say "And I really wish I could change that..."
    if alexis.flags.story == 1:
        "I'm weighing up everything that Alexis has said, all of her reasons."
        "And somehow they seem to make more sense now that she's been open with me."
        "Maybe that was all I needed, for her to tell it to me in simple terms."
        mike.say "That makes sense, Alexis."
        mike.say "I mean, it's kind of crazy in a kinky way."
        mike.say "But it all ties up when you put it like that."
        show alexis surprised at startle
        "Alexis stares at me, her eyes wide."
        "She blinks a couple of times."
        "It's almost like she can't actually believe it."
        alexis.say "You...you mean that?"
        mike.say "Yeah, Alexis, I mean it."
        mike.say "There's no way I'd want to be a cuc."
        mike.say "But a guy's got to be in the dark for that to happen, right?"
        mike.say "If I know what's happening and I'm okay with it, then there's no problem."
        mike.say "In fact, it shows were a mature, modern couple."
        show alexis happy
        "Alexis lets out what can only be described as a sigh of relief."
        alexis.say "Oh, wow..."
        alexis.say "You have NO idea what a relief it is to hear you say that!"
        alexis.say "And...you're okay with me doing other guys in front of you, right?"
        alexis.say "Because I could really do with blowing off some steam right about now!"
        "It's only now that I see Alexis has her phone in her hand."
        "I'm a little taken aback that she's already wanting to take advantage of my approval."
        "But I can't say all of that and then get pissy the very moment she takes me up on it."
        "So I shrug and nod."
        mike.say "Sure, Alexis, why not."
        alexis.say "That's great!"
        alexis.say "I'll just call Marlon, Ray and Tyreese up."
        alexis.say "They're going to be so thrilled you're cool with this!"
        $ alexis.flags.ntr_05 = "home"
    else:
        "I can kind of see what Alexis is trying to say."
        "I mean, it makes sense when she explains it."
        "But then it would, because all of this is happening inside of her head!"
        mike.say "Maybe you can, Alexis."
        mike.say "I mean, maybe you can change my mind."
        "I see hope in Alexis's eyes, and it looks totally genuine."
        "It's like she's eager for the chance to convince me."
        "And that has to be a good sign, right?"
        show alexis normal
        alexis.say "Sure thing, [hero.name]!"
        alexis.say "What can I do to prove it to you?"
        mike.say "Hmm..."
        mike.say "Maybe if we back up a couple of steps?"
        mike.say "Like go back to that great restaurant we had a date at."
        mike.say "We could see if things are different now I know all about your...needs?"
        show alexis happy
        alexis.say "That's a great idea!"
        alexis.say "Let's book a table as soon as we can!"
        "It might not be the perfect solution, but it's a start."
        "Maybe now we both have our cards on the table, things will go down differently?"
        $ alexis.flags.ntr_05 = "restaurant"
    return

label alexis_event_ntr_05_home:
    scene bg livingroom with fade
    "I've made sure that everyone else is out of the house before Alexis arrives."
    "After all, I may be trying to expand my horizons when it comes to her needs."
    "But that doesn't mean I'm ready to share those same quirks with my housemates!"
    "Not that Alexis seems to notice any of the trouble I've gone to on her behalf."
    scene bg black with dissolve
    pause 0.1
    scene bg house
    show alexis casual normal
    with wiperight
    "She just lets herself in, eager to get down to business."
    alexis.say "You ready for this, [hero.name]?"
    alexis.say "Because Ray, Marlon and Tyreese are!"
    alexis.say "And they're on their way over here right now!"
    menu:
        "We should report":
            mike.say "You know what Alexis, I'm not sure about this."
            mike.say "We should report this."
            show alexis annoyed
            alexis.say "Oh, I understand. I'll call them to cancel."
            "And with that, she leaves."
            hide alexis
            $ hero.cancel_event()
            $ alexis.love -= 5
            return
        "I'm ready":
            pass
    scene bg livingroom
    show alexis casual normal
    with fade
    "I close the door behind Alexis, trying to hide my nerves."
    "And I'm not sure the nonchalant shrug I give her is all that convincing."
    mike.say "Sure, Alexis."
    mike.say "I'm more then ready!"
    "Alexis nods, though I'm not sure she's buying it."
    alexis.say "Just relax and go with it, okay?"
    alexis.say "These guys are cool, people I know I can trust."
    play sound door_knock
    "Alexis is about to say more when there's a knock at the door."
    "But instead we both take a deep breath."
    "We exchange nods."
    "And then we go to answer the door together."
    scene bg black with dissolve
    pause 0.1
    scene bg house
    show danny as marlon zorder 1 at left4, blacker
    show dwayne as ray zorder 2 at right5, blacker
    show dwayne as tyreese zorder 3 at flip, mostright5, blacker
    with wiperight
    "Once we open the door, we're presented with the sight of our guests."
    "Ray, Marlon and Tyreese are leaning against the doorframe."
    "And they look as casual and laid-back as ever."
    "Oh, and big - I think I'd forgotten how large the three of them were!"
    show dwayne as ray at right5, blacker, startle
    "Ray" "Yo, dawg."
    "Ray" "You remember me - I'm Ray."
    "Ray" "You recognise Marlon."
    show danny as marlon at left4, blacker, startle
    "Marlon" "S'up."
    show dwayne as ray at right5, blacker, startle
    "Ray" "And how could you forget Tyreese."
    show dwayne as tyreese at flip, mostright5, blacker, startle
    "Tyreese" "Hey."
    show alexis casual happy zorder 4 at left with easeinleft
    alexis.say "Hey, guys!"
    alexis.say "Thanks for coming over at such short notice."
    show dwayne as ray at right5, blacker, startle
    "Ray" "No worries - we aim to please!"
    "Ray" "And you're jumping in on this one too, huh?"
    "It takes me a moment to realise that Ray's talking to me."
    "But when I do, I nod my head to show willing."
    mike.say "Oh yeah!"
    mike.say "I wouldn't want to miss out on something like this!"
    show dwayne as ray at right5, blacker, startle
    "Ray nods at this, and then waves to his companions."
    "And as one they walk into the house ahead of Alexis and me."
    "Ray and his companions seem to remember the way to the living room."
    scene bg livingroom
    show alexis casual happy
    with fade
    "So Alexis and I end up following them in there too."
    "And once they reach their destination, they all begin to strip-off."
    "Ray" "Okay, Alexis."
    "Ray" "Let's get this thing started..."
    show alexis topless with dissolve
    "Alexis nods, pulling off her own clothes."
    show alexis naked with dissolve
    "And I'm already unzipping my flies - like I'm okay with all of this!"
    hide alexis
    show alexis ntr gangbang with fade
    "Alexis perches on the opposite sofa and Ray sits beside her."
    "He lies back casually, letting his now stiff cock stand proud."
    "Marlon and Tyreese stand to the other side of Alexis."
    "Their own cocks bobbing mere inches from her face."
    "Without needing to be told what to do, Alexis leaps into action."
    "Her hands never seem to be still for a moment."
    "Instead they move from one cock to the next, never leaving one alone for too long."
    "She strokes, squeezes, rubs and caresses every inch that the guys possess between them."
    "Balls, shaft and head, all get worked in turn as she moves from one to the next."
    "It's kind of like watching someone spinning plates and keeping them all in motion."
    "And I can see from the faces of all three guys that she's doing a good job too."
    "Ray" "Ah yeah..."
    "Ray" "Now that's the stuff!"
    "Marlon" "Sweet!"
    "Tyreese" "Mmm..."
    "I can't help getting hard just from watching."
    "My cock is already out and clutched in my hand."
    "Which is pretty much copying Alexis's efforts."
    "But then I see Ray nod to the other guys, and they nod in turn."
    "Without speaking a word, Marlon slides onto the sofa beside Alexis."
    "And then he guides her onto him, until she's straddling his lap."
    "Alexis moans as his cock pushes against her lips, resisting for a moment."
    show alexis ntr gangbang vaginal
    "But then she begins to sink down and onto it, gasping as she surrenders."
    "Before Marlon is all the way into her, Ray takes a firm hold of Alexis's waist."
    "He parts her buttocks and aims his cock straight between them."
    "Ray" "One cock ain't gonna be enough for you, girl!"
    "I see Alexis look back over her shoulder, nodding eagerly."
    "And that's all the permission Ray needs."
    "He plunges his cock into Alexis's ass, pushing with all his strength."
    show alexis ntr gangbang anal pleasure
    alexis.say "Oh..."
    alexis.say "Oh god..."
    alexis.say "I'm so full..."
    alexis.say "Full of cock!"
    "At this, I hear Ray chuckle."
    "He shakes his head and motions to Tyreese."
    "Ray" "Not yet you ain't."
    "Ray" "Tyreese, put that mouth of hers to better use!"
    "Tyreese nods as he steps forwards, holding his cock in one hand."
    show alexis ntr gangbang normal
    "Alexis's eyes go wide as he uses the other hand to cup her chin."
    show alexis ntr gangbang blow
    "A moment later his cock is in her mouth, and Alexis can't say another word."
    "But that doesn't mean that she's thrown at all."
    show alexis ntr gangbang pleasure
    "Within seconds, her head is moving back and forth as she services the cock."
    "And from the look on Tyreese's face, she's doing a good job too!"
    "In fact, I can see that she's doing far better than these guys expected."
    "Sure, all three of them are getting exactly what they wanted right now."
    "But I swear I can see a change come over them as time goes on."
    "There's a subtle hint in their expressions."
    "One that makes me think they expected to be too much for Alexis."
    "Oddly that makes me squeeze my own cock that much harder."
    "Like I'm turned on by the idea that Alexis is too much for them."
    "Ray even shakes his head as he keeps on pounding away at her ass."
    "Ray" "Goddamnit, woman..."
    "Ray" "How much cock do you need?!?"
    "Ray" "I'm gonna blow my load real soon!"
    "Marlon" "You and me both!"
    "Tyreese" "Not if I do it first!"
    show alexis ntr gangbang -blow
    "At the mere mention of them cumming, Alexis pulls the cock out of her mouth."
    "She's panting with exhaustion, but still manages to get her words out."
    alexis.say "All...of...it..."
    alexis.say "In the...in the face..."
    show alexis ntr gangbang -vaginal -anal
    "The guys hastily pull out of Alexis, freeing her for the first time."
    hide alexis
    show alexis ntr bukake
    with fade
    "And she almost tumbles onto the floor in the middle of the room."
    "They gather around her as she kneels there, cocks bobbing close to her face."
    show alexis ntr bukake lookright
    "Alexis begins to work all three of them in earnest."
    "And it doesn't take long for her efforts to be rewarded."
    show alexis ntr bukake closeeyes cumshot left middle right with hpunch
    "Within seconds of each other, the three of them shoot their loads."
    with hpunch
    "And Alexis is in the perfect position to catch almost every drop."
    show alexis ntr bukake -cumshot dickcum cum onbody onmouth with hpunch
    $ alexis.love += 4
    "Ray, Marlon and Tyreese gasp at the release, and Alexis gasps too."
    "But in her case, it's from the desire to not miss the smallest amount."
    "Still, most of the cum seems to hit her face all the same."
    "It stripes her forehead, cheeks and chin, dripping downwards."
    "Some actually lands in her open mouth to be swallowed greedily."
    "And some drips onto her lips too, which she laps up with her tongue."
    show alexis ntr bukake swallow -onmouth
    "Even afterwards, Alexis licks what she can find off of her fingers too."
    "That's when I feel something warm running over my own fingers."
    "And I realise that I just shot my own load too."
    show alexis ntr bukake closeeyes
    "Ray sees this and shakes his head, chuckling deeply."
    "Ray" "I guess that's like a standing ovation, huh?!?"
    "Ray" "Looks like you enjoyed this as much as we did, brother!"
    hide alexis
    show alexis naked with fade
    "There's more friendly banter as everyone gets dressed."
    "And then Ray, Marlon and Tyreese make their excuses to leave."
    "Ray" "This was fun, guys."
    "Ray" "We should do it again real soon."
    "Ray" "And maybe your man here could get involved too!"
    mike.say "Y...yeah!"
    mike.say "I think I'd like that, Ray!"
    "Ray" "Whatever - stay frosty."
    "And with that, they're gone."
    show alexis happy
    alexis.say "So..."
    show alexis normal
    alexis.say "Was that fun for you?"
    mike.say "Sure, Alexis - I had a good time watching."
    mike.say "You really ate those guys alive!"
    "That was supposed to be a compliment, but I see Alexis blush."
    show alexis blush
    alexis.say "What can I say, [hero.name]?"
    alexis.say "I have needs!"
    mike.say "I know, Alexis."
    mike.say "And I feel like I understand those needs better then ever now."
    "Alexis nods, still blushing, despite the fact that everything went to plan."
    alexis.say "But you know what..."
    show alexis wink
    alexis.say "I think I could handle those three guys AND you at the same time!"
    "All I can do is shake my head and smile at Alexis."
    "Because she always seems to know how to surprise me."
    "That and keep me on my toes too!"
    return

label alexis_event_ntr_05_restaurant:
    scene bg restaurant with fade
    "I'm feeling pretty nervous as Alexis and I walk into the restaurant and sit down at a table."
    "After all, this is the first time I've been out in public with her since we discussed her...needs."
    "I'm trying as hard as I can to act normal, not to stare at every other guy in the place."
    "But what else am I supposed to do, especially when I know that Alexis is going to do it with one of them?"
    show alexis talkative at center, zoomAt (1.5, (640, 1140)) with dissolve
    alexis.say "How are you doing, [hero.name]?"
    alexis.say "Are you still up for this?"
    alexis.say "If not we can always..."
    show alexis normal
    mike.say "NO..."
    mike.say "No, Alexis...I'm fine."
    "I cut Alexis off before she can finish what she's trying to say."
    "And my voice jumps in volume, anxiety making me lose control of it for a moment."
    mike.say "Really, I'm fine."
    mike.say "Let's do this thing, okay?"
    "For a moment Alexis looks like she's going to argue with me."
    show alexis smile
    "But then she puts on a firm smile and nods her head."
    alexis.say "Okay, [hero.name]."
    show alexis happy
    alexis.say "Just try to have fun with it, yeah?"
    alexis.say "Look at the way they're trying to check me out!"
    show alexis wink
    alexis.say "But none of them want to be caught doing it, you see?"
    "What Alexis is saying makes a lot of sense."
    show alexis normal
    "And so I do my best to follow her advice."
    "Looking up from my menu, I scan the restaurant."
    "Almost instantly I can see what she means."
    "It's true, guys are looking her way all the time."
    "But then their eyes dart away the moment they think they've been spotted."
    "They want to let their gazes linger on Alexis, really check her out."
    show alexis happy at startle
    "I hear Alexis giggle, and it snaps me back to reality."
    mike.say "Fucking hell, Alexis!"
    mike.say "They can't take their eyes off of you!"
    show alexis talkative
    alexis.say "I know, I know!"
    alexis.say "It's such a rush - knowing that they all want me!"
    show alexis wink
    alexis.say "But I think the one that'll bite is that guy over there..."
    show alexis smile
    "Alexis makes a discreet gesture, tilting her head and glancing towards the man in question."
    show alexis normal
    "I do my best to follow her example and not make it too obvious that I'm checking him out."
    "And as soon as I do, I have to admit that Alexis has got taste."
    mike.say "Whoa!"
    mike.say "He's not a bad-looking dude!"
    "But then I see the other guy's date."
    "And I'm amazed all over again!"
    mike.say "Alexis..."
    mike.say "Have you seen the girl he's with?!?"
    mike.say "She's like a goddess or something!"
    mike.say "I...I mean she's not a patch on you, obviously!"
    show alexis confused
    "Alexis rolls her eyes at my attempts to explain myself."
    show alexis annoyed
    alexis.say "You don't have to bullshit me, [hero.name]!"
    alexis.say "I can see how pretty his date is from here."
    show alexis wink
    alexis.say "But that's not going to stop him from taking the bait!"
    show alexis normal
    "Part of me doesn't want to believe that Alexis is telling the truth."
    "But it's the same old-fashioned part of me that's not okay with all of this."
    "And that's the part of me that we're supposed to be dealing with here."
    "So I push aside any doubts that I have and try to keep an open mind."
    mike.say "So..."
    mike.say "What happens now?"
    show alexis normal
    alexis.say "We order food and then we wait."
    alexis.say "Right now he's interested."
    show alexis flirt
    alexis.say "But we need to let him simmer in his own juices for a while!"
    hide alexis
    show restaurant meal alexis
    with fade
    "As we wait, I can feel what Alexis has said beginning to make sense."
    "Now that I've gotten beyond my own jealousy and paranoia, I see she was right."
    "Knowing that so many guys are watching her - and wanting her!"
    "I feel a sense of superiority and pride swelling inside of me."
    "They might all want Alexis, but I'm the one that's got her!"
    show restaurant meal alexis bored
    "And that's got to mean something, right?"
    "I'm only half paying attention to what I'm eating."
    "Chewing and swallowing without really tasting anything."
    "So when Alexis coughs to get my attention, I look up instantly."
    alexis.say "Okay..."
    show restaurant meal alexis happy
    alexis.say "Now it's time!"
    mike.say "What do we do?"
    "She starts to get out of her chair, and I make to follow."
    "But Alexis waves me back into my seat."
    alexis.say "You don't do anything yet!"
    alexis.say "I'll get him to follow me into the bathroom."
    alexis.say "Once he's in there with me, wait a minute or two."
    alexis.say "Then you come join us."
    alexis.say "And for god's sake make it look casual!"
    "I nod eagerly, and do the best I can to obey."
    show restaurant meal alexis nonpc
    "I sit silently, watching as Alexis walks across the restaurant."
    "She doesn't even pause as she passes the guy's table then slips into the bathroom."
    "For a moment I wonder if she's misread the situation, as her target doesn't move an inch."
    "But then he makes to get up, showing me that he was waiting to make it look less suspicious."
    "Once he's slipped into the bathroom too, I do the best I can to wait like Alexis told me to."
    show restaurant meal alexis nonpc bored
    "I cast a glance over to the guy's unsuspecting date, who's sitting alone at just like me."
    "I wonder briefly what would happen if I were to go over there and strike up a conversation."
    "Would I be able to do to a girl the same thing Alexis can to a guy?"
    "I dismiss the idea as crazy, and then get up from my seat."
    "Hurrying across the restaurant, I make it to the bathroom."
    "If I was going too fast, maybe people will assume I was desperate to go!"
    "With my heart hammering in my chest, I slip into the bathroom."
    "As soon as I'm in there, I can hear the sound of Alexis getting it on."
    "I lock the door and scan the room, locating her in one of the stalls."
    "Now all I have to figure out is where I'm going to watch the action..."
    menu:
        "Hide and watch":
            "Already afraid that people saw us coming in here, I want to be cautious."
            "So I decide that it'd be best for me to watch Alexis and the other guy in secret."
            "Slipping into the next stall, I step up onto the toilet and peer over."
            "I'm not surprised to see the guy sitting down, pants around his ankles."
            "Nor am I surprised to see Alexis sitting on his lap."
            show alexis reverse ntr publicbathroom out mouth_pleasure with fade
            "But what does surprise me is the fact she's looking right up at me."
            "Alexis smiles, holding one finger to her lips."
            show alexis reverse vaginal at startle(0.05,-10)
            "And then I see she's using the other to guide the guy's cock home!"
            show alexis reverse eyes_surprised mouth_hurt at startle(0.05,-10)
            "Alexis's eyes go wide as she holds my gaze."
            "She's panting and biting her lip as she sinks down onto it."
            show alexis reverse eyes_normal
            "I can see everything that she's feeling."
            "It's like the sensations are written all over her face!"
            "Guy" "Oh yeah!"
            "Guy" "Now that's what I'm taking about!"
            show alexis reverse eyes_closed
            alexis.say "Mmm..."
            show alexis reverse eyes_normal mouth_scream
            alexis.say "Oh god..."
            alexis.say "Your cock..."
            alexis.say "It feels SO good inside of me!"
            show alexis reverse eyes_closed mouth_pleasure
            menu:
                "Masturbate":
                    "I can't help myself, I'm getting so turned on by this!"
                    "Before I know it, I'm unzipping my flies and pulling out my cock."
                    "It's painfully hard and I start working it without hesitation."
                    show alexis reverse eyes_normal at startle(0.05,-10)
                    "Somehow, Alexis seems to notice a change in my breathing."
                    "She nods, encouraging me in what I'm doing."
                    show alexis reverse at startle(0.05,-10)
                    "And at the same time she redoubles her own efforts too."
                    "My strokes keep up with Alexis as she bounces on the other guy's cock."
                    show alexis reverse at startle(0.05,-10)
                    "Suddenly it's almost like he's not there at all."
                    "It's like the guy's nothing more than a piece of meat."
                    show alexis reverse at startle(0.05,-10)
                    "One that Alexis is using for her own gratification."
                    "I feel flushed as I realise the power that she holds over him."
                    with hpunch
                    "And it thrills me so much that I shoot my load as I think about it."
                    "The warm cum runs down my cock and over my hand."
                    "But I'm not paying attention to anything but Alexis."
                "Just watch":
                    "I watch in rapt fascination as Alexis rides the guy's cock."
                    "Reading the pleasure that she's experiencing in her every movement."
                    "It's then I realise that I finally get what she's been trying to tell me."
                    "The guy's nothing more than a piece of meat that she's using."
                    show alexis reverse mouth_pleasure eyes_closed
                    "A more than willing cock that's getting her off when she wants it."
                    "His brain might as well not be there at all!"
            show alexis reverse at startle(0.05,-10)
            "All of a sudden, the guy starts to grunt and twitch."
            "He's coming already?!?"
            "It feels like I only just started watching them!"
            show alexis reverse cum mouth_ahegao at startle(0.05,-10)
            "Alexis is still looking me in the eye as he loses it inside of her."
            show alexis reverse mouth_scream at startle(0.05,-10)
            "She mouths the words 'I love you'."
            show alexis reverse at startle(0.05,-10)
            "Then I see her cheeks flush and I know that she's cumming too."
            "So I slip out of the stall and hurry back to our table."
        "Step in":
            "I could just slip into one of the stalls and watch from there."
            "It'd be the safest option and keep the other guy from seeing me."
            "But I've come this far and I'm not about to chicken out now."
            "So I take a deep breath and open the door to the stall they're in."
            "Guy" "H...hey!"
            "Guy" "Who the hell are you?"
            "Guy" "Is...it that the guy from your table?!?"
            "I'm not surprised to see the guy sitting down, pants around his ankles."
            "Nor am I surprised to see Alexis sitting on his lap."
            "But he seems pretty surprised to see me!"
            show alexis reverse ntr publicbathroom out with fade
            "Alexis is already sitting on his lap."
            "She has his cock in one hand, and gives him a sharp tug."
            show alexis reverse mouth_scream
            alexis.say "He's with me, okay?"
            alexis.say "You want to get freaky with me, right?"
            alexis.say "Then he gets to stay and watch!"
            show alexis reverse mouth_hurt
            "Guy" "O...okay, okay!"
            "Guy" "Whatever you say!"
            "Guy" "So long as you sit on my cock!"
            "Alexis smiles, holding one finger to her lips."
            show alexis reverse vaginal at startle(0.05,-10)
            "And then I see she's using the other to guide the guy's cock home!"
            show alexis reverse eyes_surprised
            "Alexis's eyes go wide as she holds my gaze."
            "She's panting and biting her lip as she sinks down onto it."
            show alexis reverse ntr publicbathroom vaginal
            "I can see everything that she's feeling."
            "It's like the sensations are written all over her face!"
            "Guy" "Oh yeah!"
            "Guy" "Now that's what I'm taking about!"
            show alexis reverse eyes_closed
            alexis.say "Mmm..."
            show alexis reverse eyes_normal mouth_scream
            alexis.say "Oh god..."
            alexis.say "Your cock..."
            alexis.say "It feels SO good inside of me!"
            show alexis reverse eyes_closed mouth_pleasure
            menu:
                "Masturbate":
                    "I can't help myself, I'm getting so turned on by this!"
                    "Before I know it, I'm unzipping my flies and pulling out my cock."
                    "It's painfully hard and I start working it without hesitation."
                    show alexis reverse eyes_normal at startle(0.05,-10)
                    "Somehow, Alexis seems to notice a change in my breathing."
                    "She nods, encouraging me in what I'm doing."
                    show alexis reverse at startle(0.05,-10)
                    "And at the same time she redoubles her own efforts too."
                    "My strokes keep up with Alexis as she bounces on the other guy's cock."
                    show alexis reverse at startle(0.05,-10)
                    "Suddenly it's almost like he's not there at all."
                    "It's like the guy's nothing more than a piece of meat."
                    show alexis reverse at startle(0.05,-10)
                    "One that Alexis is using for her own gratification."
                    "I feel flushed as I realise the power that she holds over him."
                    with hpunch
                    "And it thrills me so much that I shoot my load as I think about it."
                    "The warm cum runs down my cock and over my hand."
                    "But I'm not paying attention to anything but Alexis."
                "Call her dirty":
                    "I'm just loving the chance to watch Alexis make use of this guy."
                    "And I can't believe that I didn't see what she meant before."
                    "She's just using him like a piece of meat, getting off on him."
                    "All the time that his cock is inside her, Alexis is looking at me!"
                    show alexis reverse eyes_normal
                    "And the look in her eyes tells me that it's not him that's doing it for her."
                    show alexis reverse at startle(0.05,-10)
                    "It's the fact that I'm watching the whole thing!"
                    mike.say "Wow..."
                    mike.say "Alexis..."
                    mike.say "You...you dirty little bitch!"
                    show alexis reverse eyes_surprised mouth_pleasure
                    "Alexis's eyes go wide at the insult and she gasps."
                    show alexis reverse at startle(0.05,-10)
                    "But at the same time she nods desperately."
                    "She nods like she's encouraging me to do more!"
                    show alexis reverse at startle(0.05,-10)
                    mike.say "Just look at you, Alexis!"
                    mike.say "You're like a dog on heat."
                    mike.say "You're a slut!"
                    show alexis reverse at startle(0.05,-10)
                    "I lean forwards and yank at Alexis's top."
                    "It doesn't take much to expose her breasts."
                    show alexis reverse at startle(0.05,-10)
                    "And once they're on show, I take full advantage."
                    show alexis reverse eyes_closed mouth_scream
                    "I pinch Alexis's stiff nipples as hard as I can."
                    "And I squeeze her breasts while she's helpless to resist."
                    show alexis reverse at startle(0.05,-10)
                    "All the time I'm doing this, Alexis writhes and squeals."
                    "The humiliation seems to push her ever closer to the edge."
                "Just watch":
                    "I watch in rapt fascination as Alexis rides the guy's cock."
                    show alexis reverse eyes_closed mouth_pleasure at startle(0.05,-10)
                    "Reading the pleasure that she's experiencing in her every movement."
                    "It's then I realise that I finally get what she's been trying to tell me."
                    show alexis reverse at startle(0.05,-10)
                    "The guy's nothing more than a piece of meat that she's using."
                    "A more than willing cock that's getting her off when she wants it."
                    show alexis reverse at startle(0.05,-10)
                    "His brain might as well not be there at all!"
                    "It's like the guy's nothing more than a piece of meat."
                    show alexis reverse at startle(0.05,-10)
                    "One that Alexis is using for her own gratification."
                    "I feel flushed as I realise the power that she holds over him."
            "Guy" "I can't hold it in..."
            show alexis reverse eyes_surprised mouth_scream at startle(0.05,-10)
            alexis.say "Oh shit..."
            alexis.say "Oh fuck yes..."
            alexis.say "I'm gonna cum too!"
            with vpunch
            "I watch as Alexis takes everything the guy has to give."
            show alexis reverse out cum eyes_normal mouth_ahegao with vpunch
            "Her entire body twitches and twists as she cums."
            with vpunch
            "But still she keeps on holding my eye the entire time."
            "I stay there, watching until Alexis's orgasm begins to fade."
            "And then I take it's end as my cue to slip out of the bathroom."
            "I make it back to our table and try to act natural."
    hide alexis
    show restaurant meal alexis nonpc with fade
    "Alexis emerges from the bathroom a few minutes later."
    "She walks over to the table as if nothing were amiss."
    "I guess the other guy must have waited for a while before he slipped out too."
    "But I'm not at all interested in where he is or what he's doing."
    "Instead I focus all of my attention on Alexis."
    show restaurant meal alexis -bored -nonpc with dissolve
    "She sits down and resumes eating her meal."
    "I do the same, but I can't keep myself from gazing at her."
    show restaurant meal alexis happy
    "Alexis notices this and gives me a knowing smile."
    alexis.say "Now you get it."
    alexis.say "Right, [hero.name]?"
    mike.say "Yeah, Alexis."
    mike.say "I get it!"
    return

label alexis_ntr_conversation:
    if alexis.flags.ntr_conversation == "flirt":
        call alexis_conv_flirt from _call_alexis_conv_flirt
    elif alexis.flags.ntr_conversation == "leave":
        call alexis_conv_leave from _call_alexis_conv_leave
    elif alexis.flags.ntr_conversation == "cheat":
        call alexis_conv_cheat from _call_alexis_conv_cheat

    return

label alexis_conv_flirt:
    show alexis
    mike.say "Look, I just wanted to have it out about what happened at the restaurant the other night."
    "Alexis pauses, the silence becoming almost instantly pregnant."
    alexis.say "Okay...I'm listening."
    menu:
        "I know you cheat on me and that's okay":
            mike.say "I know that you're a cheater, Alexis."
            mike.say "In fact, I've always known that you weren't faithful to me."
            show alexis annoyed
            alexis.say "W...wait, I..."
            "I can hear a certain tone in Alexis's voice."
            "One that lets me know she's trying to explain herself."
            show alexis sad
            "But I cut her off before she can get started."
            mike.say "No, Alexis..."
            mike.say "You need to let me finish, okay?"
            "I take the silence on the other end of the line as Alexis doing as I asked."
            "So I take a deep breath and push on."
            mike.say "Look, Alexis..."
            mike.say "I've always known that you cheat on me with other guys."
            mike.say "But what I never told you was that...I'm kind of okay with it!"
            show alexis surprised
            alexis.say "You...you are?!?"
            mike.say "I know it sounds weird, Alexis."
            mike.say "But you seem to get off on fucking guys behind my back, right?"
            show alexis confused
            alexis.say "Well...yeah, I guess."
            mike.say "You get off on it and that's your kink."
            mike.say "And knowing that you do it is mine."
            mike.say "Alexis...I can't really explain it!"
            show alexis annoyed
            alexis.say "It's okay, [hero.name]."
            alexis.say "I think I get what you're saying."
            alexis.say "So..."
            show alexis confused
            alexis.say "You're cool with me doing stuff like that?"
            alexis.say "You WANT me to cuck you?"
            mike.say "Yeah, Alexis."
            mike.say "But don't make it too obvious, okay?"
            show alexis sad
            "Alexis goes quiet for a moment."
            show alexis normal at startle
            "But then I hear her let out a sigh."
            alexis.say "Okay, okay..."
            alexis.say "This is going to take some getting my head around!"
            alexis.say "I never had a guy say he wanted me to cheat on him before!"
            mike.say "Don't worry, Alexis."
            mike.say "I'm sure you're up to the challenge!"
            "I end the conversation with Alexis, already wondering if I've done the right thing."
            "But then I remind myself that this is a far more honest way to handle it."
            "I'm being honest about what Alexis really is and how that makes me feel."
            "If our relationship can't work when everything is out in the open, then what hope is there for us?"
            $ alexis.flags.story = 1
            $ alexis.flags.cheatokay = True
        "Don't cheat on me again":
            mike.say "I won't agree to see you again if you keep on behaving like that in front of me, Alexis."
            mike.say "I'm sorry if that makes me sound like a jealous prick of a throwback to a less enlightened time."
            mike.say "But we're not in high school anymore, and I won't put up with someone flirting in front of me like that."
            mike.say "I always tolerated it when we were kids because I didn't know any better."
            mike.say "But I won't take it any more."
            "Alexis is silent for a while, probably taken aback by the strength of my ultimatum."
            show alexis confused
            alexis.say "Okay, [hero.name]...I...I guess I didn't realise how strongly you felt about that kind of thing..."
            "I let out a frustrated sigh, afraid of sounding like a jealous ogre over what she probably regards as something completely harmless."
            mike.say "Look, I think we made a mistake by going into this whole idea of us getting to know each other again a bit naively."
            mike.say "We can't hide the fact that we both have a lot of emotional baggage that we're still carrying from the past."
            show alexis annoyed
            alexis.say "I guess so..."
            mike.say "What I'm saying is that I think we need to establish a few small ground-rules - and that no flirting while we're together is one of them."
            mike.say "By that I mean no flirting with other people...not each other."
            mike.say "Not that I'm saying you HAVE to flirt with me - unless you want to, that is!"
            show alexis happy at startle
            "Alexis laughs, genuinely for the first time during our conversation."
            show alexis wink
            alexis.say "Don't worry, I think I get what you mean!"
            $ alexis.flags.story = 2
        "Apologize and ignore the flirting":
            "I feel like I should confront Alexis about her behaviour."
            "Like I should call her out for openly flirting with another guy in front of me."
            "But then I remember what ended our relationship the last time."
            "And the fear of losing her for a second time makes me forget all about that option."
            mike.say "I just wanted to say sorry for getting upset when you were talking to that guy."
            mike.say "It was way out of order - I have no right to tell you who you can and can't talk to."
            alexis.say "It's okay, really...don't worry about it."
            mike.say "No, it's not - I got too possessive and jealous, even when we weren't supposed to be officially on a date."
            show alexis happy at startle
            "Alexis chuckles to herself, and she shakes her head at me."
            show alexis normal
            alexis.say "Like I already said, it's no big deal, [hero.name]."
            show alexis wink
            alexis.say "In fact, it was kind of flattering, the way you wanted me all to yourself!"
            mike.say "Well...I guess I'd just forgotten how much I liked spending time in your company, that's all."
            show alexis normal
            alexis.say "What do you say we just put it behind us and move on?"
            alexis.say "I think I'd like to hear more about just how much time you want to spend on me..."
            $ alexis.flags.story = 3
        "I know you cheat and I don't want to see you again":
            mike.say "Look, Alexis - I thought that it'd be great to see you again, that we'd likely both changed."
            mike.say "But I guess what I saw last night proved that I was only half right."
            mike.say "I might have changed, but you're still up to the same old shit you were back in the day."
            show alexis sad
            alexis.say "[hero.name], please..."
            alexis.say "I can explain!"
            mike.say "What are you going to tell me, Alexis?"
            mike.say "How can you spin the fact that I caught you flirting with another guy into a positive thing?"
            mike.say "What's next? Taking advantage of the darkness of the cinema or hiding behind the rocks at the beach?"
            "There's no immediate response to that."
            "But then I was hardly expecting one."
            mike.say "Alexis, I think I'd prefer it if we didn't see each other again...period."
            "It hurts to end the call like that, but I can't honestly see that I have another choice."
            $ alexis.set_gone_forever()
    "Hopefully I've nipped this thing in the bub, kept it from getting out of hand."
    "But I guess that only time will tell if I made the right decision or not."
    return

label alexis_conv_leave:
    "I'm still feeling humiliated and more than a little stupid for thinking that she might have turned over a new leaf."
    "The last thing that I want right now is to have to talk to her or even look her in the eye."
    "But then I wonder if I shouldn't hear what she has to say."
    "Who knows, maybe she's spent all night stewing in it too."
    if "alexis_event_05" in DONE:
        "Maybe she's actually come to the conclusion that screwing guys behind a rock while on a date with another is just a little bit rude."
    elif "alexis_event_04" in DONE:
        "Maybe she's actually come to the conclusion that sucking one guy while on a date with another is just a little bit rude."
    else:
        "Maybe she's actually come to the conclusion that screwing one guy in the bathroom while on a date with another is just a little bit rude."
    "That's why I decide to have an open conversation about last time."
    mike.say "Good morning, Alexis."
    "My tone is as flat and emotionless as I can make it, under the circumstances."
    show alexis angry at center, vshake
    alexis.say "YOU FUCKING PRICK!"
    "Well, I guess that answers the question about whether or not she's calling to apologise."
    alexis.say "Where in the HELL do you think you can get away with skipping out on me like that?!?"
    if "alexis_event_05" in DONE:
        alexis.say "I come back from the shack, and you've walked out..."
        alexis.say "Worse than that, you left me to take a cab home!"
    elif "alexis_event_04" in DONE:
        alexis.say "I come back from the bathroom, and you've walked out..."
    else:
        alexis.say "I come back from the bathroom, and you've walked out..."
        alexis.say "Worse than that, you left me to pick up the bill!"
    "I keep quiet, letting her rant away and list her perceived grievances, hoping that she'll eventually run out of steam."
    show alexis at startle
    alexis.say "I have NEVER been so humiliated..."
    "But at the use of that word, I just can't keep from jumping in."
    show alexis surprised at startle
    mike.say "Oh, for the love of god, Alexis - shut up for a second and actually listen to yourself."
    mike.say "Sure, I walked out on you, I admit it."
    if "alexis_event_05" in DONE:
        mike.say "But it was only after I walked in on you while you were having fun behind those rocks."
    elif "alexis_event_04" in DONE:
        mike.say "But it was only after I woke up while you were sucking that dude."
    else:
        mike.say "But it was only after I walked in on you while you were in the men's bathroom."
    show alexis mindless
    "Alexis stares at me in a stunned silence."
    "The kind that usually signifies that the goalposts in the argument are in the process of moving."
    mike.say "Are you still there, Alexis?"
    show alexis surprised at startle
    pause 1.0
    show alexis annoyed
    alexis.say "Yes...I can...listen, I can explain..."
    "This should be good."
    alexis.say "You...you weren't supposed to see that, [hero.name]..."
    mike.say "Yeah, Alexis - I kinda figured that one out for myself!"
    show alexis sad
    alexis.say "No...that's not what I meant...it's more complicated..."
    "Complicated, really?"
    "It looks like I'm going to have to lay down the law on this one."
    menu:
        "I know you cheat on me and that's okay":
            mike.say "I know that you're a cheater, Alexis."
            mike.say "In fact, I've always known that you weren't faithful to me."
            show alexis annoyed
            alexis.say "W...wait, I..."
            "I can hear a certain tone in Alexis's voice."
            "One that lets me know she's trying to explain herself."
            show alexis sad
            "But I cut her off before she can get started."
            mike.say "No, Alexis..."
            mike.say "You need to let me finish, okay?"
            "I take the silence on the other end of the line as Alexis doing as I asked."
            "So I take a deep breath and push on."
            mike.say "Look, Alexis..."
            mike.say "I've always known that you cheat on me with other guys."
            mike.say "But what I never told you was that...I'm kind of okay with it!"
            show alexis surprised
            alexis.say "You...you are?!?"
            mike.say "I know it sounds weird, Alexis."
            mike.say "But you seem to get off on fucking guys behind my back, right?"
            show alexis confused
            alexis.say "Well...yeah, I guess."
            mike.say "You get off on it and that's your kink."
            mike.say "And knowing that you do it is mine."
            mike.say "Alexis...I can't really explain it!"
            show alexis annoyed
            alexis.say "It's okay, [hero.name]."
            alexis.say "I think I get what you're saying."
            alexis.say "So..."
            show alexis confused
            alexis.say "You're cool with me doing stuff like that?"
            alexis.say "You WANT me to cuck you?"
            mike.say "Yeah, Alexis."
            mike.say "But don't make it too obvious, okay?"
            show alexis sad
            "Alexis goes quiet for a moment."
            show alexis normal at startle
            "But then I hear her let out a sigh."
            alexis.say "Okay, okay..."
            alexis.say "This is going to take some getting my head around!"
            alexis.say "I never had a guy say he wanted me to cheat on him before!"
            mike.say "Don't worry, Alexis."
            mike.say "I'm sure you're up to the challenge!"
            "I end the conversation Alexis, already wondering if I've done the right thing."
            "But then I remind myself that this is a far more honest way to handle it."
            "I'm being honest about what Alexis really is and how that makes me feel."
            "If our relationship can't work when everything is out in the open, then what hope is there for us?"
            $ alexis.flags.story = 1
            $ alexis.flags.cheatokay = True
        "Don't cheat on me again":
            mike.say "That was a serious screw-up on your part, Alexis."
            if "alexis_event_05" in DONE or "alexis_event_04" in DONE:
                mike.say "But...I guess we can chalk it up to a mistake and try again."
            else:
                mike.say "But...I guess that as we weren't officially on an actual date, we can chalk it up to a mistake and try again."
            alexis.say "You'd be okay with that?"
            "Alexis sounds as though she was expecting me to go off the deep end and dump her or something."
            "Which would have been hard, as we're not actually dating yet!"
            mike.say "I just think that we need to establish some ground rules, Alexis, that's all."
            mike.say "Maybe the first of which would be that we lay off excusing ourselves to fuck other people while we're together?"
            show alexis happy at startle
            "She had to laugh at the frank nature of my last statement."
            show alexis wink
            alexis.say "But what if they're like REALLY hot?"
            "The sarcasm and amusement in her voice suddenly reminds me of the Alexis that I always wanted to reconnect with."
            mike.say "I think we need to tackle that on a hottie by hottie basis, Alexis!"
            $ alexis.flags.story = 2
        "Apologize and ignore the cheating":
            "I feel like I should confront Alexis about her behaviour."
            "Like I should call her out for cheating on me like that."
            "But then I remember what ended our relationship the last time."
            "And the fear of losing her for a second time makes me forget all about that option."
            mike.say "I just wanted to say sorry for getting upset when you were talking to that guy."
            mike.say "It was way out of order - I have no right to tell you who you can and can't talk to."
            alexis.say "It's okay, really...don't worry about it."
            mike.say "No, it's not - I got too possessive and jealous, even when we weren't supposed to be officially on a date."
            show alexis happy at startle
            "Alexis chuckles to herself, and she shakes her head at me."
            show alexis normal
            alexis.say "Like I already said, it's no big deal, [hero.name]."
            show alexis wink
            alexis.say "In fact, it was kind of flattering, the way you wanted me all to yourself!"
            mike.say "Well...I guess I'd just forgotten how much I liked spending time in your company, that's all."
            show alexis normal
            alexis.say "What do you say we just put it behind us and move on?"
            alexis.say "I think I'd like to hear more about just how much time you want to spend on me..."
            $ alexis.flags.story = 3
        "I know you cheat and I don't want to see you again":
            mike.say "Look, Alexis - I thought that it'd be great to see you again, that we'd likely both changed."
            mike.say "But I guess what I saw last night proved that I was only half right."
            mike.say "I might have changed, but you're still up to the same old shit you were back in the day."
            show alexis sad
            alexis.say "[hero.name], please..."
            mike.say "What are you going to tell me, Alexis?"
            mike.say "How can you spin the fact that I caught you fucking another guy into a positive thing?"
            "There's no immediate response to that."
            "But then I was hardly expecting one."
            mike.say "Alexis, I think I'd prefer it if we didn't see each other again...period."
            "It hurts to end things, but I can't honestly see that I have another choice."
            $ alexis.set_gone_forever()
    "I end the conversation still feeling somewhat emotionally hungover from the night before and its fallout."
    "But there's a kernel of hope that I can sense, deep down in my gut."
    "I think that I might have just made the right decision for the both of us."
    return

label alexis_conv_cheat:
    show alexis
    if "alexis_event_05" in DONE:
        "I don't think that I let on what I saw Alexis and those strangers doing at the beach the other night, or gave her a clue I suspected something was up."
    elif "alexis_event_04" in DONE:
        "I don't think that I let on what I saw Alexis and the stranger doing in the cinema the other night, or gave her a clue I suspected something was up."
    else:
        "I don't think that I let on what I saw Alexis and the stranger doing in the men's bathroom the other night, or gave her a clue I suspected something was up."
    "But that means that I'm now left trying to bury that mental image, while all the time pretending that everything's okay and I'm convinced that Alexis is a changed woman."
    "I'm supposed to just get up and go about my day as though nothing untoward happened and nothing's bugging me."
    "In the end, I decide that it's better to talk to her and have it out than to just sit here stewing."
    mike.say "Well, Alexis - I had a pretty great time the other day."
    mike.say "But..."
    menu:
        "I know you cheat on me and that's okay":
            mike.say "I know that you're a cheater, Alexis."
            mike.say "In fact, I've always known that you weren't faithful to me."
            show alexis annoyed
            alexis.say "W...wait, I..."
            "I can hear a certain tone in Alexis's voice."
            "One that lets me know she's trying to explain herself."
            show alexis sad
            "But I cut her off before she can get started."
            mike.say "No, Alexis..."
            mike.say "You need to let me finish, okay?"
            "I take the silence on the other end of the line as Alexis doing as I asked."
            "So I take a deep breath and push on."
            mike.say "Look, Alexis..."
            mike.say "I've always known that you cheat on me with other guys."
            mike.say "But what I never told you was that...I'm kind of okay with it!"
            show alexis surprised
            alexis.say "You...you are?!?"
            mike.say "I know it sounds weird, Alexis."
            mike.say "But you seem to get off on fucking guys behind my back, right?"
            show alexis confused
            alexis.say "Well...yeah, I guess."
            mike.say "You get off on it and that's your kink."
            mike.say "And knowing that you do it is mine."
            mike.say "Alexis...I can't really explain it!"
            show alexis annoyed
            alexis.say "It's okay, [hero.name]."
            alexis.say "I think I get what you're saying."
            alexis.say "So..."
            show alexis confused
            alexis.say "You're cool with me doing stuff like that?"
            alexis.say "You WANT me to cuck you?"
            mike.say "Yeah, Alexis."
            mike.say "But don't make it too obvious, okay?"
            show alexis sad
            "Alexis goes quiet for a moment."
            show alexis normal at startle
            "But then I hear her let out a sigh."
            alexis.say "Okay, okay..."
            alexis.say "This is going to take some getting my head around!"
            alexis.say "I never had a guy say he wanted me to cheat on him before!"
            mike.say "Don't worry, Alexis."
            mike.say "I'm sure you're up to the challenge!"
            "I end the conversation with Alexis, already wondering if I've done the right thing."
            "But then I remind myself that this is a far more honest way to handle it."
            "I'm being honest about what Alexis really is and how that makes me feel."
            "If our relationship can't work when everything is out in the open, then what hope is there for us?"
            $ alexis.flags.story = 1
            $ alexis.flags.cheatokay = True
        "Don't cheat on me again":
            mike.say "I won't agree to see you again if you keep on behaving like that in front of me, Alexis."
            mike.say "I'm sorry if that makes me sound like a jealous prick of a throwback to a less enlightened time."
            mike.say "But we're not in high school anymore, and I won't put up with someone flirting in front of me like that."
            mike.say "I always tolerated it when we were kids because I didn't know any better."
            mike.say "But I won't take it any more."
            "Alexis is silent for a while, probably taken aback by the strength of my ultimatum."
            show alexis confused
            alexis.say "Okay, [hero.name]...I...I guess I didn't realise how strongly you felt about that kind of thing..."
            "I let out a frustrated sigh, afraid of sounding like a jealous ogre over what she probably regards as something completely harmless."
            mike.say "Look, I think we made a mistake by going into this whole idea of us getting to know each other again a bit naively."
            mike.say "We can't hide the fact that we both have a lot of emotional baggage that we're still carrying from the past."
            show alexis annoyed
            alexis.say "I guess so..."
            mike.say "What I'm saying is that I think we need to establish a few small ground-rules - and that no flirting while we're together is one of them."
            mike.say "By that I mean no flirting with other people...not each other."
            mike.say "Not that I'm saying you HAVE to flirt with me - unless you want to, that is!"
            show alexis happy at startle
            "Alexis laughs, genuinely for the first time during our conversation."
            show alexis wink
            alexis.say "Don't worry, I think I get what you mean!"
            $ alexis.flags.story = 2
        "Apologize and ignore the cheating":
            mike.say "...I guess I can't wait to know when I'm gonna get to see you again!"
            show alexis blush
            "Alexis chuckles sweetly at this, clearly flattered by my neediness."
            alexis.say "You need to be just a little more patient, [hero.name]!"
            show alexis normal
            alexis.say "But I promise that you can see more of me real soon..."
            "From there the conversation turns to the subject of when and where we're going to see each other next."
            "All the time I feel kind of bad for not confronting Alexis about the fact I caught her cheating on me."
            if "alexis_event_05" in DONE:
                "But the more I think about it, the more I realise just how much I got off on watching her being fucked by those guys."
            elif "alexis_event_04" in DONE:
                "But the more I think about it, the more I realise just how much I got off on watching her sucking another guy."
            else:
                "But the more I think about it, the more I realise just how much I got off on watching her being fucked by another guy."
            "I don't know if it was just the voyeurism involved, or that I actually got to watch what she tried to hide from me when we were an item in the past."
            "Either way, it made me feel as though I was a part of what she was doing somehow."
            "The fact that I was a secretive watcher turned the act from one of simple cheating into something I could enjoy in a twisted manner."
            "Unlike when she went behind my back in the past, this time I was already aware of her predilection to cheat."
            if "alexis_event_05" in DONE:
                "That put the suspicion in my mind and made me go looking when she lingered behind those rocks."
            elif "alexis_event_04" in DONE:
                "That put the suspicion in my mind and made me keep looking."
            else:
                "That put the suspicion in my mind and made me go looking when she lingered in the bathroom."
            "Perhaps that's the crux of it all - now that I'm aware of what she's doing, I feel more like I have a share of the power?"
            "I could confront Alexis at any time and place, but that's all in my hands."
            "Or I can choose to keep her in the dark and continue to watch as she fucks whoever she pleases, thinking that she's doing so without the slightest suspicion on my part."
            $ alexis.flags.story = 3
        "I know you cheat and I don't want to see you again":
            if "alexis_event_05" in DONE:
                mike.say "...I got worried when you were taking so long to get that water at the beach."
                mike.say "So I went to check on you...and I saw you with those other guys."
            elif "alexis_event_04" in DONE:
                mike.say "...I woke up in the middle of the movie during our date at the cinema."
                mike.say "...and I saw you with that other guy."
            else:
                mike.say "...I got worried when you were taking so long in the bathroom the other night."
                mike.say "So I went to check on you...and I saw you with that other guy."
            "There's a long, drawn-out silence as the significance of my words sinks in for Alexis."
            show alexis confused
            alexis.say "[hero.name]...that wasn't what it looked like...I..."
            "Seriously, that's the best excuse she can come up with?"
            mike.say "What was it supposed to look like, Alexis?"
            if "alexis_event_05" in DONE:
                mike.say "Because to me, it looked like you'd snuck off to have a threesome in the middle of our date."
            elif "alexis_event_04" in DONE:
                mike.say "Because to me, it looked like you'd snuck off to suck another guy in the middle of our date."
            else:
                mike.say "Because to me, it looked like you'd snuck off to fuck another guy in the middle of our date."
            mike.say "Or was it the angle that I was watching you from?"
            if "alexis_event_05" in DONE:
                mike.say "Should I have been looking under the water rather than over the top of the rocks?"
            elif "alexis_event_04" in DONE:
                mike.say "Should I have been looking under the seats rather than over them?"
            else:
                mike.say "Should I have been looking under the door rather than over the top of the stalls?"
            show alexis sad
            alexis.say "[hero.name], you're not letting me explain..."
            mike.say "What's there to explain, Alexis?"
            mike.say "Apart from that I thought you might have changed and you proved me wrong?"
            show alexis cry
            alexis.say "If you'd just..."
            mike.say "No, Alexis - no more excuses and lies."
            mike.say "We're done!"
            "And with that, I cut her off before she can say another word."
            $ alexis.set_gone_forever()
            return
    return

label alexis_kiss_me:
    hide alexis
    show alexis kiss
    with fade
    $ alexis.flags.kiss += 1
    if randint(1, 2) == 1:
        "I don't know what I've said or done to make Alexis feel the way that she must be feeling right now."
        "All I know is that the moment I turn my head towards her, I'm met by the sensation of her lips pressing against mine."
        "They're softer than I remember them ever being in the past."
        "And they move gently against my own in a way that tells me she wants this kiss badly."
        "I go slowly at first, letting her show me what she desires and not even trying to assert myself."
        "Looking at the way her eyes are so delicately closed suddenly makes me aware that I've kept mine open just to look at her."
        "I close them and try to focus only on the experience of Alexis feeling me out in such an enjoyable manner."
        "Alexis doesn't rush to slip her tongue between my lips, and instead I feel it tentatively reaching out, a little more each time."
        "Soon she musters the courage to explore further, and I hear her breathing become that much more intense as she does so."
        "All this time, neither of us touches the other with any other part of our bodies."
        "More than once I feel my hands begin to reach out for Alexis, but somehow the tenderness and intensity of the kiss always defeats me in this."
        "It's almost as if I fear that touching her will somehow break the spell, and that no subsequent kiss will be as special as this one is right now."
    else:
        "Alexis lures me in, making eyes and seeming to promise something in the way of a reward if I do as I'm bid."
        "Once she has me right where she wants me, I feel the sensation of her lips as they press against mine."
        "I honestly can't recall which of us was the first to kiss the other back in the day."
        "And I suppose that it doesn't matter which one of us it is now."
        "All that does is the fact that we're doing things over again."
        "And if the way this kiss from Alexis is making me feel is anything to go by, then we're getting off to a very good start indeed..."
    hide alexis kiss with fade
    $ cheated_girls = game.get_cheated_girls(alexis)
    if cheated_girls:
        call expression randchoice(cheated_girls).id + "_cheated" pass ("kissing") from _call_expression_127
    return

label alexis_preg_talk:
    "It'd be fair to say that I walk into what I thought was supposed to be nothing more than a chance to meet Alexis with my guard well and truly down."
    show alexis
    "But almost the same moment that I see her face for the first time, I can tell that I'm actually walking into something pretty damn heavy."
    "She greets me with an expression that's equal parts pained and a visible effort to put on a brave face."
    mike.say "Hey, Alexis...what's up?"
    mike.say "You look like you've got the weight of the world on your shoulders."
    "She gives me another pained look, and takes a deep breath, as if steeling herself for what she's about to say."
    alexis.say "You could say that, [hero.name]..."
    alexis.say "I don't know how best to get this out, so I'm just going to say it."
    "Oh shit - here we go!"
    alexis.say "You know how we've been getting on so well these past few weeks?"
    "I nod quickly."
    alexis.say "How we've been having a lot of fun - like multiple amounts of fun, sometimes on the same occasion?"
    "My nodding is getting more frantic now, as I begin to get the gist of what she's trying to tell me."
    alexis.say "Well, let's just say that a little something I picked up at the chemist's told me that we might have had too much fun!"
    alexis.say "Specifically, unprotected fun..."
    "Ah, I see what she means now."
    mike.say "You mean you're..."
    alexis.say "Yes, [hero.name] - I'm pregnant."
    "The weight of what she's just told me begins to sink in, almost making me want to sit down in sympathy."
    mike.say "And, well...what do you want to do about it?"
    "Alexis shakes her head, partly from genuine confusion and, I sense, at least a little from frustration at my passive response to such momentous news."
    alexis.say "I don't really know, [hero.name]."
    alexis.say "But I thought that I should tell you the truth, and maybe we could work that out together."
    "It occurs to me that Alexis must have known about this for at least a little amount of time before she told me."
    "And I wonder if she's really wanting to ask me for my input, or she's actually made her mind up already."
    mike.say "Wow...this has kind of dropped on me, Alexis."
    mike.say "Maybe if you tell me what you think, just off the cuff, I could use that to get my own thoughts straight too?"
    if alexis.love >= 150:
        "Alexis sighs and takes a hold of my hand, squeezing it tightly as she looks me straight in the eyes."
        alexis.say "I love you, [hero.name], and that's the truth."
        alexis.say "What I want is to have the baby and for us to raise it together, as a family."
        alexis.say "Look, I know we had issues in the past...that I did things that hurt you deeply."
        alexis.say "But we've looked the past in the face now and moved on together, haven't we?"
        show alexis flirt
        "She pauses for a moment, the emotion of what she's telling me clearly playing on her face as she does so."
        alexis.say "I don't think those hurtful things make us weak, I think that overcoming them made us stronger than before."
        alexis.say "In fact, I think that'd make a pretty sound base on which we could even build a marriage..."
    else:
        "Alexis smiles at me in an oddly amorous way, given the subject that we've just been discussing."
        "She leans in closer, placing her hand atop mine and beginning to stroke it with her fingers."
        show alexis happy
        alexis.say "Well, as you were man enough to get me in the family way, how about you go all the way with it?"
        alexis.say "I'm tired of being on my own and having no one to devote myself to in life."
        alexis.say "What I really want is the chance to settle down and become a happy little wife for you."
        show alexis blush
        "Her smile becomes wider still, and she now has a wicked glint in her eyes."
        alexis.say "And let's just say that I don't want to be one of these 'modern wives' either."
        alexis.say "When I promise to love, honour and obey you, then I really mean it."
        alexis.say "No matter what you might want - I'll always obey..."
    "And I thought just being hit with the news of the pregnancy was enough to make me confused and conflicted!"
    "What Alexis just added to that is equal parts dream come true and terrifying nightmare, depending simply on whether I choose to trust her or not."
    "I mull over what she's said for a moment, wondering if I should ask her for more time to consider my answer."
    "But one look into her eyes tells me that she's expecting one here and now."
    menu:
        "You should have a termination":
            "I puff my cheeks out in preparation for saying something that I know isn't going to go down well."
            "But I feel that I wouldn't be playing it fair if I chose to say something else for the sake of being liked."
            mike.say "Alexis, I hate to say this, but I think you should seriously think about having a termination."
            hide alexis
            show alexis angry
            "She stares at me for a moment, dumbfounded."
            "And then her face becomes angry, almost outraged."
            alexis.say "[hero.name]...how in the hell can you even think of such a thing?"
            alexis.say "This is a human being we're talking about - your own kid!"
            "I prepare myself again, as here comes the low blow that I'm not proud of, but I think needs to be delivered all the same."
            mike.say "You say it's mine, Alexis - but we both know that's not a certain thing."
            show alexis sad
            "Her anger abates for a moment, replaced with shock and genuine pain."
            "I know instantly that what I just said has hurt Alexis deeply, and I wish I could take it back."
            "But I won't."
            mike.say "You were a cheater back then, Alexis, and you're still a cheater now."
            mike.say "I don't want to turn down raising a family with you because of that, though."
            mike.say "I just won't raise kids with someone that I can't trust, as it wouldn't be fair on them."
            show alexis cry
            "Alexis has no answer to that."
            "Instead she just shakes her head as she backs away, then turns and runs from me."
            "The worst part is that I can tell she's trying to keep me from seeing the tears running down her face as she does so."
            $ alexis.flags.nodate = True
            $ alexis.flags.nokiss = True
            $ alexis.love -= 50
            $ alexis.flags.pregstory = 2
        "I want to raise the child with you":
            "I take a deep breath in preparation for what I'm going to say next, knowing that it will change my life forever."
            mike.say "You know what, Alexis - I think you're one hundred percent right."
            "Alexis looks at me with a hopeful expression, almost unable to believe what I just told her."
            alexis.say "You mean..."
            mike.say "I mean that we should totally make a go of raising the kid together."
            "Before I can say another word, Alexis wraps her arms around me and pulls me into a ferocious hug."
            "My face us buried in her hair, and all I can feel is the pleasant sensation of her body pressing itself against mine."
            "It takes me a while to realise that I can hear something, a sound that Alexis is making, even as she's still hugging me."
            "I pull back a little, and notice that she's crying in my arms."
            mike.say "Alexis, what's the matter...why are you crying?"
            "She sobs and sniffles a little as she tries to explain herself."
            alexis.say "I'm happy, really I am..."
            alexis.say "It's just that...you showed me that you really do forgive me for what I did to you before..."
            mike.say "Alexis, of course I do...we were kids, and you're a different person now!"
            alexis.say "I know, I know...but I never really believed it myself before now."
            alexis.say "I always thought I'd be tainted by it somehow..."
            alexis.say "But I can put it behind me now, start over again."
            alexis.say "Oh, [hero.name]...I promise I'll make you so happy!"
            mike.say "You already did, Alexis."
            $ alexis.love += 10
            $ alexis.flags.pregstory = 1
    "Two lives changed forever thanks to just one little conversation."
    "But a conversation with consequences that were far from little in their implications."
    return

label alexis_rape_talk:
    show alexis sad
    if alexis.love >= 100:
        alexis.say "[hero.name]."
        mike.say "Alexis."
        mike.say "I...I wanted to call you talk to you before now, Alexis."
        mike.say "But I was worried that..."
        alexis.say "What, [hero.name]?"
        alexis.say "What were you worried about?"
        mike.say "I didn't know if you'd want to hear from me, Alexis."
        mike.say "Not after I was the one that went to the police about what Kylie did..."
        "Alexis stares at me for the longest time, in total silence and yet with her mouth hanging open."
        "And when she does finally speak, the disbelief in her voice as clear as can be."
        alexis.say "How...how could you think that, [hero.name]?!?"
        alexis.say "Sure, Kylie's my sister."
        alexis.say "But I can't forgive what she did to you!"
        if kylie.flags.rape and not kylie.flags.killed:
            alexis.say "She raped you, [hero.name]."
            alexis.say "It'd be no different if you were a girl and she were a guy."
            alexis.say "As far as I'm concerned, Kylie's right where she needs to be."
            alexis.say "And maybe she should have been there a lot sooner too!"
        elif kylie.flags.rape and kylie.flags.killed:
            alexis.say "She raped you, [hero.name]."
            alexis.say "And I don't think I'll ever be able to forgive the fact that she killed someone either!"
            alexis.say "She's dangerous, too dangerous to be out on the streets where she could hurt someone else."
            alexis.say "God help me for saying this, but I hope they never let her out!"
        "I feel a sudden and unexpected surge of emotion as Alexis says all of this."
        "And I realise that I've been bottling up my feelings since it all happened."
        "Somehow, just knowing that Alexis is on my side is enough to lift the weight off of my shoulders."
        alexis.say "[hero.name]..."
        alexis.say "Are you...crying?"
        "Without asking my permission, Alexis cups my cheek with her hand and wipes my eye."
        "I see that her finger comes away wet, telling me that she's right."
        mike.say "I...I guess I am!"
        mike.say "It's just so good to know that you get it, Alexis - that you understand."
        alexis.say "Let's just say that I've been where you are now, [hero.name]."
        alexis.say "And you helped me to get back on my feet too."
        "For a moment I seriously think about asking Alexis just what she means by that."
        "But then I shake it off, deciding that now isn't the best time to pry."
        alexis.say "I lost you once, [hero.name]."
        alexis.say "But I won't let that happen again!"
        "I feel Alexis take hold of my hands."
        "Gripping them tightly as if afraid she'll lose me if she doesn't."
        "I don't need to be told to wrap my own fingers between hers either."
        "After that, there's no more need for words as she leans her forehead against mine."
        hide alexis
        show alexis kiss with fade
        $ alexis.flags.kiss += 1
        "And the sensation of kissing her lips is like sealing the deal."
        "As soon as I do so, I somehow feel like everything's going to be okay after all."
    else:
        alexis.say "Hey, [hero.name]."
        mike.say "Hey, Alexis."
        mike.say "I can't imagine it's fun for your family right now."
        alexis.say "Don't worry yourself about that, [hero.name]."
        alexis.say "As far as I'm concerned, you're the only victim here!"
        if kylie.flags.rape and not kylie.flags.killed:
            mike.say "Thanks for saying that, Alexis - you're a good friend."
            mike.say "But there's still a part of me that feels a little sorry for her, you know?"
            alexis.say "Huh...really?!?"
            mike.say "I know, I know...it sounds crazy."
            mike.say "But she was sick in the head, after all."
            "Alexis shakes her head, her mouth set in a grim line."
            alexis.say "It's amazing you can be that kind, [hero.name]."
            alexis.say "I couldn't be, and she's my kid sister!"
            "All I can do is shrug and offer Alexis a weak smile."
            mike.say "Maybe you'll be able to forgive her in time, Alexis."
            alexis.say "Maybe...maybe not."
            alexis.say "But I didn't come here to talk about Kylie."
        elif kylie.flags.rape and kylie.flags.killed:
            "Almost the same moment that she says it, Alexis realises the mistake she's made."
            "She starts waving her hands in front of herself, as if trying to distance herself from it."
            alexis.say "Oh shit, [hero.name] - I'm so sorry!"
            alexis.say "My first thought was for you."
            alexis.say "I guess I forgot about your poor housemate..."
            "I hold up my own hand, stopping Alexis before she can say anything more."
            mike.say "It's okay, Alexis - I understand."
            mike.say "You didn't know her like I did."
            mike.say "And you were just trying to be a good friend."
            "Alexis nods, but I can see in her eyes that she's not totally convinced by my words."
            mike.say "It's weird her not being around the place anymore."
            mike.say "And right now, I don't know what's going to happen next."
            mike.say "Maybe we'll get a new housemate, or maybe I'll move out."
            alexis.say "Well, you can always crash on the couch at my place."
            mike.say "Thanks, Alexis - you're a good friend."
            alexis.say "I didn't come here to talk about me, [hero.name]."
        alexis.say "I came here to talk about you."
        "I smile, trying to wave away her concern for me."
        mike.say "I'll be fine, Alexis."
        mike.say "I just need time to get over it, that's all."
        "Alexis looks me straight in the eye, shaking her head as she does so."
        "It's then that I feel the weight of her hand on mine."
        alexis.say "You don't need to act like it's nothing with me, [hero.name]."
        alexis.say "We go way back, far enough for me to know when you're putting on a front."
        mike.say "Uh...yeah, Alexis."
        mike.say "I guess you are one of my oldest friends."
        "Alexis squeezes my hand at this, a pained, but genuine smile on her face."
        alexis.say "I...I feel like I could have been a better friend, [hero.name]."
        alexis.say "Maybe if I had..."
        alexis.say "Maybe things would have been different..."
        mike.say "You couldn't have stopped Kylie, Alexis."
        mike.say "She was hellbent on doing what she did."
        mike.say "But I could use all the friends I can get right now."
        mike.say "So maybe you can help me get over what's been done?"
        "Alexis' smile slowly loses its pain and becomes more genuine as I say this."
        "She nods, and I can feel a smile spreading across my face too."
        "I guess this one of those times when old friends don't really need words to know what each other is thinking."
    $ alexis.love += 20
    return

label alexis_male_ending:
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding

    if renpy.has_label("alexis_achievement_3") and not game.flags.cheat:
        call alexis_achievement_3 from _call_alexis_achievement_3
    if alexis.flags.story == 1:
        "Before Alexis came back into my life, I would never have believed that I'd even have been able to be a friend to her."
        "The notion of starting to date her again or it becoming serious would have seemed almost unbelievable too."
        "But here we are, with me standing at the altar, waiting for her to come walking down the aisle!"
        "It's been a bit of a roller-coaster ride to get here though, with the past being dragged out into the light."
        "I think we're good...in fact I'm sure we've dealt with all of the stuff that Alexis did back then."
        "Or...to be more honest...I've come to accept them and look the other way!"
        "I know deep down that I shouldn't let Alexis get away with her...indiscretions."
        "But she just seems to have a power over me - one that makes me forgive her anything!"
        "I guess that it's more important to me to have her than to know she's always faithful."
        "And if that makes me a cuck, then that's just what I'll have to be!"
        "The sound of music beginning to play snaps me out of it and makes me look over my shoulder."
        show alexis wedding at center, zoomAt( 0.9, (640, 740)) with dissolve
        "I recognise it instantly as Alexis's choice, what she wanted to come down the aisle to."
        "And then she's there, doing just that."
        "I try to ignore the ripple of subdued conversation that passes through the assembled family and friends."
        "And I tell myself that they're not commenting on Alexis's past actions behind their raised hands."
        show alexis smile wedding at center, traveling(1.5, 5.0, (640, 1040))
        "Instead I focus all of my attention on watching my bride-to-be as she approaches."
        "It's no secret that Alexis has always had a hold on me, that I'm a sucker for her looks."
        "But the dress she's wearing somehow manages to make her appear more beautiful than ever."
        show alexis happy
        "She's also smiling, beaming in fact, which only adds to how stunning she looks."
        show alexis smile
        "At first I think Alexis is looking straight at me."
        "But then, and with more than a little confusion, I realise she's not."
        "She's actually looking past me - looking at the priest instead."
        "It's only now that I see the priest clearly too, noting how suave and handsome he looks."
        "Is she..."
        "Would Alexis really..."
        "On our wedding day..."
        "No...no, she's not flirting with the priest!"
        "I'm just being paranoid, that's all - it must be the nerves...just the nerves!"
        "I return Alexis's smile as she reaches my side, trying not to look pained as I do so."
        "But it feels like I have to struggle to divert her attention from the priest."
        mike.say "Ah..."
        mike.say "Hey, Alexis!"
        show alexis normal blush
        alexis.say "Oh...right!"
        alexis.say "Hey, [hero.name]!"
        show wedding alexis priest with fade
        "Priest" "Dearly beloved..."
        "Priest" "We are gathered here today..."
        "Priest" "To witness the joining of these two people in the bonds of holy matrimony."
        "You don't need me to tell you what happens next."
        "You've seen a million weddings play out, right?"
        "On TV, in movies and even in person - so you know how it goes."
        "Let's just say that I'm watching Alexis and the priest the whole time."
        "And she seems to be spending more time gazing lovingly at him than me!"
        "Priest" "If anyone knows of any lawful reason these two may not be married..."
        "Priest" "Let them speak now, or forever hold their peace!"
        "The priest pauses a moment for the traditional murmurs and laughter to pass."
        "But then he chuckles and adds an extra line all of his own."
        "Priest" "I mean...I could think of a couple, sure."
        "Priest" "But they might end up getting me kicked out of my job!"
        "The guests laugh, whether out of embarrassment or genuine amusement."
        "And Alexis chuckles too, her cheeks flushing red at the comment."
        "Suddenly I feel like I'm the only one that's not amused, the only one not in on the joke."
        "Priest" "Anyway..."
        "Priest" "Do you, [hero.name], take this FINE and beautiful woman to be your wife?"
        mike.say "I...I do!"
        "Priest" "Hmm...I thought so."
        "Priest" "And to you, Alexis, actually take this...this man to be your husband?"
        alexis.say "I...I guess I do!"
        "Priest" "Then I guess I have to pronounce you husband and wife."
        "Priest" "You can kiss the guy - if you like."
        scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
        show alexis kiss wedding
        with fade
        $ alexis.flags.kiss += 1
        "Before I can speak up or protest, Alexis kisses me quickly on the lips."
        "But then she turns her attention back to the priest."
        hide alexis
        show alexis wedding at center, zoomAt(1.5, (640, 1040))
        with fade
        alexis.say "Erm...excuse me?"
        "Priest" "Yes, Alexis?"
        show alexis flirt
        alexis.say "That was...such a beautiful ceremony!"
        "Priest" "Why, thank you, my dear!"
        alexis.say "So beautiful that I think you deserve a special thank you!"
        "Most of the guests have begun to file out of the chapel by now."
        "So mercifully they don't see what Alexis does next."
        "Without asking permission from the priest or me - her new husband!"
        scene bg black
        show alexis ntr wedding happy with fade
        "Alexis gets down on her knees and starts to unzip the priest's pants!"
        "I'm too shocked to move a muscle, and so is he."
        "This means that nobody stops her as she pulls out his cock."
        "I can instantly see that at least one of my suspicions was correct."
        "The priest has a massive, raging hard-on."
        "And it can only be from his proximity to my wife!"
        "Even more depressing is that fact that he also has a rather large manhood too."
        show alexis ntr wedding blowjob
        "Alexis takes full advantage of the confusion she's causing to get down to it."
        "She has the priest's cock in her mouth within the blink of an eye."
        show alexis ntr wedding closed
        "And then she's away, giving him head like her life depends on it!"
        "My eyes are as wide as saucers as I watch Alexis go at it."
        "I can feel my lips moving, but no words come out of my mouth."
        "It all feels like a dream, or a nightmare, coming true."
        "Is my bride of only a few short minutes actually blowing a guy in front of me?"
        "And not only that, but the very same priest that just married us?!?"
        "What brings home the reality of the thing is the look on the priest's face."
        "At first, when he locks eyes with me, I can see the same shock as I feel."
        "But then something changes in his expression, like he realises something."
        "He was probably expecting me to object, to cause a scene as I demanded Alexis stop."
        "I can almost see realisation dawn on him that it's not going to happen."
        show alexis ntr wedding blush
        "That's when a smile slowly spreads across his face and he give me a knowing nod."
        "This guy knows that I'm a cuck, that I'm not going to stop Alexis."
        "So he can just relax and enjoy the sensations of her sucking his cock."
        "Even worse, he can revel in the fact that it's happening right in front of me too!"
        "Alexis isn't holding back either, as she works his cock."
        "She's taking it as deep into her throat as she possibly can."
        "I can hear her panting between the sounds of licking and sucking."
        "And I know how good it must feel from all the times she's blown me in the past."
        "I can't keep track of time while all this is happening."
        "It might have been over in less than a minute or taken far longer."
        "But things change when the priest gives me a non-too-subtle wink."
        "At the same time he puts his hands on the side of Alexis's head."
        show alexis ntr wedding out opened tongueout
        "Then he pulls his cock out of her mouth in one smooth motion."
        "Alexis scarcely has time to catch a breath before it happens."
        show alexis ntr wedding cumshot closed
        "Without warning, the priest shoots his load straight into her face."
        "She gasps as his cum hits her nose and spreads across her cheeks."
        show alexis ntr wedding pleasure opened mouthcum dickcum -cumshot
        "And then it runs downwards, taking her make-up with it and soaking into her dress."
        "Before she can recover, the priest put his cock away and straightens his collar."
        scene bg church wedding
        show alexis blush wedding at center, zoomAt(1.5, (640, 1140)) with fade
        "He walks away, not bothering to spare a glance for either of us."
        "Which leaves me looking at my new wife."
        "Who looks back up at me, on her knees and smeared with another man's cum."
    else:
        "I have to confess that I never thought this day would come, not when Alexis first came back into my life."
        "There was so much emotional baggage from the last time that we were together, so many old wounds to reopen."
        "But I guess that I was wrong, that, in our case at least, time really was the healer they say it can be."
        "I don't know if it was because only one of us changed, or if we both grew into different people since high-school."
        "Or maybe we just realised that the best place to leave the past was...well, in the past!"
        "Either way, we just seemed to click like never before, and one thing lead to another."
        "Now here we are, with me standing at the altar, waiting for Alexis to walk down the aisle!"
        "The chapel is packed to the brim with our family and friends, all waiting for the same thing."
        "And just as I steal another glance over my shoulder, I hear the sound of music beginning to play."
        show alexis wedding at center, zoomAt( 0.9, (640, 740)) with dissolve
        "Instantly I recognise the song that Alexis chose to walk down the aisle too."
        "So I don't turn back to face the altar and the patiently waiting priest."
        "Instead I keep watching as Alexis finally comes into view at the other end of the chapel."
        "I hardly hear the whispered comments and gasps of approval from the guests."
        "And that's because I'm too wrapped up in gazing at my bride-to-be."
        "Sure, it's no secret that I've always been kind of a slave to Alexis's looks."
        "She's just the hottest girl I've ever seen - hands down!"
        "But somehow she's never looked as lovely as she does right now."
        "Her dress is the perfect choice, enhancing her natural beauty."
        "And she walks towards the altar with a confidence I've never seen in her before."
        "Alexis really does look like a princess, or even a queen!"
        "She's totally in control of her own destiny, commanding the room."
        "My feelings must be written across my face, plain to see."
        show alexis smile wedding at center, traveling(1.5, 5.0, (640, 1040))
        "Because when she reaches my side, Alexis doesn't feel the need to say a thing."
        "She just gives me a little shake of the head and a smile."
        "But somehow this is more than enough to let me know that she understands."
        "I'm about to open my mouth to whisper a few words to her..."
        "Priest" "Ahem..."
        show wedding alexis priest with fade
        "At the sound of the priest clearing his throat, we both look in his direction."
        "Priest" "If you're ready?"
        "Suitably chastened, Alexis and I nod in agreement."
        "Priest" "Then we can begin..."
        "Priest" "Ladies and gentlemen, we gathered here today..."
        "Priest" "To witness the joining of these two people in the bonds of holy matrimony..."
        "You know how the rest goes, right?"
        "No need for a blow-by-blow account."
        "So let's just skip ahead to the good bits..."
        "Priest" "If anyone present knows of any reason that these two may not be joined wed..."
        "Priest" "Let them speak now, or forever hold their peace!"
        "Alexis locks eyes with me, looking more than a little nervous."
        "We'd talked about this point in the ceremony before now."
        "And we'd both been sure that there was no chance of someone barging into the chapel on the day."
        "But still, we both hold our breath in case our old coach from high-school."
        "Priest" "Nobody?"
        "Priest" "Good..."
        "Alexis and I let out a sigh of relief in the very same moment."
        "And I can't help but see the amused smile on the priest's face."
        "Priest" "Do you, [hero.name], take Alexis to be your lawful, wedded wife?"
        mike.say "I do."
        "Priest" "And do you, Alexis, take [hero.name], to be your lawful, wedded husband?"
        alexis.say "I do."
        "Priest" "Then it gives me great pleasure to pronounce you husband and wife."
        "Priest" "You may kiss the bride!"
        scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
        show alexis kiss wedding
        with fade
        $ alexis.flags.kiss += 1
        "I don't hesitate to take him up on the offer."
        "And Alexis doesn't hold back either."
        "I must have kissed her a hundred times before now."
        "But somehow this feels like the first time all over again."
        "Maybe it's the promise of spending the rest of our lives together than makes it feel so special."
        "Or maybe Alexis learned some new trick that she's trying out on me for the very first time."
        "But it hardly seems to matter, as the kiss goes on and on as everyone watches me and my new wife!"
    scene alexis ending
    with fade
    if alexis.flags.story == 1:
        alexis.say "It's funny how you look back on the past and begin to realise that you were so wrong about stuff."
        alexis.say "I mean, take [hero.name] and me, when we were back in high-school."
        alexis.say "All the stuff that happened between us back then, it felt like the end of the world."
        alexis.say "When we broke up, it seemed like there was no way back for us, like we were over for good."
        alexis.say "But as time passes, you start to see that it's only that bad when it's still raw."
        alexis.say "After a couple of years have passed, you've moved on to other things, and it doesn't matter anymore."
        alexis.say "I guess it's all part of growing up, of becoming more mature."
        alexis.say "When [hero.name] came back into my life, I was worried that the past would come back to haunt me too."
        alexis.say "I was worried that the memory of what happened with our high-school coach would come between us."
        alexis.say "Because I changed in the time since we were last together, but not in my habits."
        alexis.say "What changed in me was that I realised this is just who I am."
        alexis.say "I'm not the kind of girl that one man can satisfy, that's a fact."
        alexis.say "If I need more than that, I have to get it from somewhere else."
        alexis.say "At first I tried to keep it from [hero.name], going behind his back."
        alexis.say "But it's often hard to think straight when you're desperate to let off steam like that."
        alexis.say "And so it didn't take long for him to figure out what was going on."
        alexis.say "I was sure that would be the end of it, that he'd dump me all over again."
        alexis.say "He'd accuse me of being the same little slut that cheated on him in high-school."
        alexis.say "And that would be the end of that - me and him over for the second time."
        alexis.say "But it was then that he really took me by surprise."
        alexis.say "He told me that he wasn't mad at my going behind his back."
        alexis.say "In fact, he said that it was pretty hot, something that got him excited!"
        alexis.say "So I wasn't the only one that had changed, that had grown up since we were last together."
        alexis.say "Naturally, I was pretty fucking relieved to hear that!"
        alexis.say "I'd gotten back the one that I thought had got away."
        alexis.say "And as a bonus, he was into the idea of me cheating on him too!"
        alexis.say "Also, the knowledge that he was being cucked REALLY made him perform in bed!"
        alexis.say "He was so into it that he almost managed to satisfy me on his own...almost."
        alexis.say "That was really the key to it all, what made the pieces fall into place."
        alexis.say "Once we'd been honest about our needs and desires, we could finally trust each other."
        alexis.say "Before we'd both been lying to ourselves, trying to be people that we just weren't."
        alexis.say "It's funny how being honest about something others see as dishonest can be a good thing!"
        alexis.say "[hero.name] even asked me to marry him!"
        alexis.say "And now we're getting to live a life of domestic bliss."
        alexis.say "He's happier and more productive at work, and I get to be a trophy wife!"
        alexis.say "I'm free to do what I like with whoever I like."
        alexis.say "So long as I let my loving husband know when and how he's being cucked!"
        if alexis.flags.mikeBabies >= 1:
            alexis.say "We've even been able to start a family all of our own."
            alexis.say "And by some miracle [hero.name] was the father."
            alexis.say "I think he might have been thrilled if he wasn't."
            alexis.say "But little Marco looks so much like his daddy."
            alexis.say "So he's not adding to [hero.name]'s humiliation in that way!"
        elif alexis.is_visibly_pregnant:
            alexis.say "We've even been blessed with the patter of tiny feet."
            alexis.say "I mean sure, [hero.name]'s not really the father, and he knows it too."
            alexis.say "But he's kind of thrilled to be raising another man's kid."
            alexis.say "It sort of adds to the fact that he's being humiliated on a daily basis!"
        else:
            alexis.say "I keep broaching the subject of us starting a family."
            alexis.say "And it's not like [hero.name] is against the idea."
            alexis.say "And one day we'll probably go through with it too."
            alexis.say "But part of me thinks that [hero.name] is hoping someone else will get me pregnant."
            alexis.say "You know, so that he can be humiliated in that way too?"
        alexis.say "So that's how our story turned out, at least so far."
        alexis.say "And I think we've got a better chance now than we ever had in the past."
        alexis.say "I suppose it proves that honesty is the foundation of any successful relationship."
        alexis.say "Especially when your relationship includes doing it with other guys!"
        alexis.say "In that case, you don't need to change your own habits, girls."
        alexis.say "Just find a sweet guy that's into the idea of being a cuck!"
    elif alexis.flags.story == 2:
        alexis.say "Wow...it's so weird to be in a place like this, looking back on where [hero.name] and I came from."
        alexis.say "Back then I always daydreamed about what it'd be like if we got married and settled down together."
        alexis.say "But then the thing that broke us up happened, and it seemed like that was going to stay a daydream."
        alexis.say "Even when [hero.name] came back into my life all those years later, I was still sure it'd come between us."
        alexis.say "Sure, we were thrilled to catch up and reconnect, even having fun going on a couple of silly dates."
        alexis.say "But sooner or later, I was sure that it'd come up."
        alexis.say "Or that I'd do something stupid...like I always seem to do."
        alexis.say "I'd get that crazy urge to go behind his back again."
        alexis.say "Half of it was because I enjoyed the danger of cheating on [hero.name]."
        alexis.say "But the other half was because I'd convinced myself that I had to do it."
        alexis.say "I could have acknowledged that I had a problem and tried to fix it."
        alexis.say "Instead I kept telling myself that it was natural, that I needed more than he could give me."
        alexis.say "I wasn't cheating on him, not really, because I couldn't help it."
        alexis.say "And telling him that he wasn't able to satisfy me would only have hurt him too."
        alexis.say "So that's how I started out when we got a second chance."
        alexis.say "I was doing the same stupid things that broke us up the first time."
        alexis.say "Maybe I was fooling myself into believing he'd never catch me out."
        alexis.say "Or maybe I always thought that he would in the end, and I was waiting for it to happen."
        alexis.say "Whatever the hell I was doing, [hero.name]'s not stupid."
        alexis.say "He figured it out in the end, and he confronted me too."
        alexis.say "I was ready for him to dump me a second time, for it to be over for good this time."
        alexis.say "But to my surprise, he didn't dump me."
        alexis.say "Instead he asked me why I was doing it."
        alexis.say "And once we started to talk - I mean REALLY talk, things got better."
        alexis.say "We'd never really done that, you see."
        alexis.say "Back when we were kids, it was all hormones and impossible promises."
        alexis.say "There was no chance to delve into what lay at the bottom of our problems."
        alexis.say "But now we were adults, we owed it to each other to finally start talking, to start sharing."
        alexis.say "Together we began to confront the ghosts of the past."
        alexis.say "It wasn't easy, and there were a lot of twists and turns along the way."
        alexis.say "Tempers often got frayed and tense words were exchanged."
        alexis.say "Yet at the end of it all, we were still standing and still together."
        alexis.say "I guess the core of what we share was enough to let us endure all of that."
        alexis.say "It was enough to let us start again, and do better this time round."
        alexis.say "And boy, did we ever do better on the second try!"
        alexis.say "It seems like once we were getting over the past, the future just got brighter."
        alexis.say "I'd never seen [hero.name] so happy, and I felt the same way too."
        alexis.say "But it still came as a massive surprise when he asked me to marry him."
        alexis.say "Of course I said yes, how could I not?"
        alexis.say "Yet it all seemed unreal, right up to the point he put the ring on my finger."
        alexis.say "And now I'm his wife, or his trophy wife - as he likes to call me!"
        alexis.say "[hero.name] goes out to work in the morning and I do whatever a wife is supposed to do."
        alexis.say "I mean, I do get bored sometimes...really bored."
        alexis.say "But don't worry - that doesn't mean I'm going to fall back into old habits!"
        if alexis.flags.mikeBabies >= 1 or alexis.is_visibly_pregnant:
            alexis.say "Running around after little Marco keeps me too busy for any of that."
            alexis.say "And yes, [hero.name] was relieved when his son ended up looking like him."
            alexis.say "But he needn't have worried himself, as I was over all of that well beforehand."
        else:
            alexis.say "And we keep talking about starting a family too."
            alexis.say "Which I guess will be more than enough to keep me busy."
            alexis.say "It also proves that [hero.name] trusts me."
            alexis.say "And that he's not expecting his kid to look like some other guy!"
        alexis.say "So that's where you find us, leaving the past behind and looking towards the future."
        alexis.say "It sure was a crazy journey to get here, but it was worth it."
        alexis.say "And I can't wait to see what life has in store for us around the corner."
    else:
        alexis.say "Yeah, yeah, yeah...I know what everyone's going to say!"
        alexis.say "That I'm a whore, and a cheater and a slut...all that stuff."
        alexis.say "But did anyone ever think that I might be the victim in all of this, huh?"
        alexis.say "Did it ever cross your minds that I cheat on [hero.name] because I have to?"
        alexis.say "No, it's not a crazy thing to say - it's me being honest, that's all!"
        alexis.say "I didn't ask to be born this way, to need more affection than one man can give."
        alexis.say "And no matter what anyone else thinks, it's perfectly natural."
        alexis.say "So why shouldn't I have the right to go elsewhere to get satisfied?"
        alexis.say "The problem between [hero.name] and me was never that I was seeing other guys."
        alexis.say "The REAL problem was that I got sloppy and let him find out about it."
        alexis.say "If I'd been more careful back in high-school, he'd never have known."
        alexis.say "And if he'd never known about the coach, then who knows?"
        alexis.say "Maybe we'd never have broken up back then and we'd still have been together?"
        alexis.say "I...I DO love him, you know?"
        alexis.say "I mean really love him - all the romantic side of it."
        alexis.say "I...I just need more than he can give me when it comes to the physical side of things."
        alexis.say "I thought things might have changed when our paths crossed and we got a second chance."
        alexis.say "But it didn't take me long to realise that [hero.name] wouldn't be enough for me."
        alexis.say "He is the man that I want to be with, that I want to spend my life with."
        alexis.say "So for that to happen, I have to keep him in the dark about certain things."
        alexis.say "And it's not like I'm hurting him either...not really."
        alexis.say "He's got his high-school sweet-heart back again."
        alexis.say "He's getting to make up for the mistakes we made back then too."
        alexis.say "Isn't that better than him knowing the truth?"
        alexis.say "This way we can both be happy and get what we want."
        alexis.say "I've always thought that the truth was over-rated anyway."
        alexis.say "And it never seemed to do anything for [hero.name] except make him miserable too!"
        alexis.say "That's where I'm doing something different, you see?"
        alexis.say "Something better even."
        alexis.say "I'm making [hero.name] happy, for as long as I can."
        alexis.say "And so far, it seems to be working out pretty well."
        alexis.say "[hero.name]'s happy at home and at work."
        if alexis.flags.mikeBabies >= 1:
            alexis.say "We've even been able to start a family all of our own."
            alexis.say "I was relieved to find out that [hero.name] was the father."
            alexis.say "It's something I take almost as divine proof that I'm in the right!"
            alexis.say "And little Marco looks so much like his daddy too."
            alexis.say "So that helps to keep suspicion off of me as well!"
        elif alexis.is_visibly_pregnant:
            alexis.say "We've even been blessed with the patter of tiny feet."
            alexis.say "I mean sure, [hero.name]'s not really the father."
            alexis.say "But he believes me when I say that Marco looks just like my grandfather."
            alexis.say "And he's over the moon at the chance to be a father anyway."
            alexis.say "So that helps to keep suspicion off of me too!"
        else:
            alexis.say "I keep broaching the subject of us starting a family."
            alexis.say "Especially when [hero.name] starts to get suspicious."
            alexis.say "And one day we'll probably go through with it too."
            alexis.say "I'll just have to remember to be extra careful when that time comes."
            alexis.say "As the last thing I need is awkward questions about our kid not looking like his daddy!"
        alexis.say "So we have all the important things in life taken care of."
        alexis.say "All I need to do is keep [hero.name] in the dark about certain things."
        alexis.say "As long as I can do that, I think we can make a go of it."
        alexis.say "Ignorance is bliss, or so they say."
        alexis.say "And I intend to make his life as blissful as it can possibly be."

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not alexis.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_1
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_1
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label alexis_birthday_date_male:
    $ DONE["alexis_birthday_date_male"] = game.days_played
    $ game.active_date.clothes = "date"
    scene bg street with fade
    "It took me a while to think of something that would make Alexis's birthday special."
    "But in the end I think that I managed to settle on something that fits the bill."
    "Now all I have to do is get Alexis to move her ass and actually get there!"
    "Right now I'm almost having to drag her through the main street."
    show alexis date annoyed at center, zoomAt(1.5, (940, 1040)) with easeinright
    alexis.say "But why won't you tell me where we're going?"
    alexis.say "We're not kids anymore, [hero.name]."
    alexis.say "Aren't we a bit old for surprises?"
    mike.say "You're never too old for a birthday surprise, Alexis!"
    mike.say "Come on, you're going to love this - I promise."
    "I'm hoping that'll be enough to get through to Alexis."
    show alexis surprised
    "But a moment later something else seems to catch her attention."
    show alexis at center, zoomAt(1.5, (340, 1040)) with ease
    "And she pulls me over to a nearby shop window."
    show alexis at startle
    alexis.say "Ooh!"
    show alexis normal
    alexis.say "Just a minute, [hero.name]..."
    alexis.say "I need to see the new stock they have in this place."
    alexis.say "It's just so shiny!"
    menu:
        "Let her check":
            "I feel myself getting frustrated."
            "But then I glance at the time."
            "If she's quick, then we can probably still make it."
            mike.say "Okay, Alexis..."
            mike.say "But you'd better be fast about it."
            "Alexis nods as she leads me over to the window."
            alexis.say "Oh man!"
            show alexis happy
            alexis.say "Will you take a look at that?"
            alexis.say "I was right."
            alexis.say "This stuff is so much better than what they had last season!"
            "I make what I hope are the appropriate sounds of agreement."
            "But I'm actually not looking into the window at all."
            "Instead I'm hastily planning the quickest route to our destination."
            "And as soon as Alexis is done gazing into the window, we're off again."
            $ game.active_date.score += 15
        "Push her, we have an appointment":
            "I feel a rush of annoyance at Alexis's dawdling."
            "And I remember the time I've booked us in for her surprise."
            mike.say "Come on, Alexis..."
            mike.say "We don't have time for this."
            mike.say "We're going to be late!"
            "I take hold of Alexis's hand."
            "And I make to pull her away from the window."
            show alexis angry
            alexis.say "Are you serious?"
            alexis.say "I only wanted to take a quick peek!"
            mike.say "Of course I'm serious!"
            mike.say "We have to go - now!"
            show alexis annoyed
            "Alexis lets out a huff of frustration."
            "But she also stops resisting me."
            "So I'm able to hurry her along through the street."
            "All the time hoping that we are going to be on time."
            $ game.active_date.score -= 10
    show alexis normal at center, zoomAt(1.25, (640, 900)) with fade
    "A little bit of hurrying finally sees us reach our destination."
    "So I turn to Alexis and gesture towards the door."
    mike.say "Here we are!"
    show alexis surprised
    alexis.say "The photo studio?"
    show alexis normal
    alexis.say "You want to get a picture of us?"
    show alexis annoyed
    alexis.say "Why not just get a selfie on your phone?"
    if hero.has_skill("high_libido"):
        "I thought that Alexis might react like this."
        "So I'm going to have to confess my motives."
        "I just hope that she's on the same page as me!"
        if hero.knowledge >= 75 or alexis.love >= 180:
            "I don't see any point in trying to hide my true intentions from Alexis."
            "After all, she's going to find out what they are the moment we walk in there."
            "So it seems to me like honesty is the best policy."
            mike.say "Okay, Alexis..."
            mike.say "Cards on the table."
            mike.say "I want to get some nice shots of you."
            show alexis normal
            "Alexis cocks her head on one side."
            "And I can see that she's intrigued."
            "But of course, she's not going to make it that easy for me."
            alexis.say "Oh really?"
            show alexis confused
            alexis.say "Just some nice shots, huh?"
            "I hold my hands up, making a gesture of surrender."
            mike.say "Alright..."
            mike.say "The pictures I want are a little more..."
            mike.say "Well, artistic in nature."
            show alexis normal
            alexis.say "You mean you want some sexy shots of me?"
            show alexis wink blush
            alexis.say "[hero.name]..."
            alexis.say "That's so hot!"
            alexis.say "And it's so liberated too - almost European!"
            show alexis happy
            alexis.say "So we should definitely do this!"
            "Alexis leads the way into the studio."
            "And I follow close on her heels."
            $ game.active_date.score += 15
        else:
            mike.say "Well..."
            mike.say "I just want some nice pictures of you, Alexis!"
            mike.say "Not some crap selfie taken on a phone!"
            "Alexis seems less than impressed with my explanation."
            "But she rolls her eyes and then nods her head all the same."
            show alexis annoyed
            alexis.say "Urgh..."
            alexis.say "That's like the lamest reason ever!"
            alexis.say "And it makes you sound like my mom too!"
            "I can feel my cheeks flushing with embarrassment."
            "And I'm regretting not being more honest with Alexis."
            "Maybe if I'd just admitted that I wanted some hot photos of her..."
            "Maybe then she'd have been a little bit more sympathetic."
            alexis.say "Come on then..."
            show alexis normal
            alexis.say "Let's get on with it!"
            "Alexis shakes her head as she stalks into the studio."
            "And I scuttle along after her."
            $ game.active_date.score -= 10
    elif hero.charm >= 50:
        "I thought that Alexis might react like this."
        "So I've already lined up my arguments."
        "And that means I'm prepared for this moment."
        if hero.charm >= 75:
            mike.say "Not that kind of photo, Alexis."
            mike.say "I've got a very different type in mind!"
            "Alexis raises her eyebrows."
            "And she looks at me in surprise."
            show alexis confused
            alexis.say "Huh?"
            alexis.say "What kind of photos are you talking about?"
            "I shrug and let out a sigh."
            mike.say "Well, Alexis..."
            mike.say "The thing is that I already have pictures of you."
            show alexis annoyed
            alexis.say "So why do you need more?"
            mike.say "Because those are all from back in high-school."
            mike.say "I don't have any that are of you as you are now."
            mike.say "And that doesn't feel right somehow."
            "Alexis blinks as my words sink in."
            "And I can see that she's genuinely moved."
            show alexis normal
            alexis.say "Wow..."
            alexis.say "That's actually pretty deep."
            show alexis blush
            alexis.say "Kind of romantic too!"
            show alexis wink
            alexis.say "So we should definitely do this!"
            "Alexis leads the way into the studio."
            "And I follow close on her heels."
            $ game.active_date.score += 15
        else:
            mike.say "Not that kind of photo, Alexis."
            mike.say "I've got a very different type in mind!"
            "Alexis raises her eyebrows."
            "And she looks at me in surprise."
            show alexis confused
            alexis.say "Huh?"
            alexis.say "What kind of photos are you talking about?"
            "I shrug and let out a little chuckle."
            "Already aware that I'm beginning to sweat."
            mike.say "The more...artistic kind, Alexis."
            mike.say "You know...the kind you want to keep private?"
            "Alexis's eyes go wide as she realises what I mean."
            show alexis surprised
            alexis.say "You mean nude shots, yeah?"
            alexis.say "Shots in my birthday suit?"
            mike.say "No, way, Alexis!"
            mike.say "Artistic doesn't mean nude!"
            mike.say "Well...unless you WANT to pose nude?"
            alexis.say "I don't know what's worse, [hero.name]."
            show alexis annoyed
            alexis.say "You wanting me to pose naked..."
            alexis.say "Or the fact you couldn't just come out and ask me straight!"
            "Alexis shakes her head as she stalks into the studio."
            "And I scuttle along after her."
            $ game.active_date.score -= 10
    else:
        mike.say "Ah, come on, Alexis!"
        mike.say "Don't tell me you're not into this."
        "Alexis looks at me, her mouth hanging open."
        show alexis confused
        alexis.say "What are you even talking about, [hero.name]?"
        alexis.say "I'm not a model or anything like that!"
        alexis.say "I don't want to pose for a photo shoot."
        mike.say "Don't try to kid me, Alexis."
        mike.say "I know you too well for that."
        "Alexis looks like she's going to argue with me."
        show alexis normal
        "But then she lets out a sigh and nods her head."
        alexis.say "Okay, okay..."
        alexis.say "I have always been curious."
        alexis.say "So maybe I should give it a try..."
        "Alexis leads the way into the studio."
        "And I follow close on her heels."
        $ game.active_date.score += 10
    scene bg photostudio
    show alexis date normal
    with fade
    "As soon as we get into the studio, I feel the mood lighten."
    "The place is modern and very professional in appearance."
    "Which seems to help dispelling any doubts Alexis has."
    "I can already see that she's admiring the shots hung on the walls."
    "And there's no wonder, as they all look pretty amazing."
    "Photographer" "Hey there!"
    "Photographer" "You must be [hero.name] and Alexis."
    alexis.say "That's right."
    mike.say "Erm..."
    mike.say "Yeah, that's us."
    "Photographer" "Great!"
    "Photographer" "If you want to come with me..."
    "Photographer" "We can get started."
    "Alexis makes to follow the photographer."
    "But I hesitate for a moment, which makes her pause too."
    alexis.say "What's the matter, [hero.name]?"
    alexis.say "Wait a minute..."
    show alexis annoyed
    alexis.say "You're not worried that the photographer's a guy..."
    alexis.say "Are you?"

    menu:
        "No problem here":
            mike.say "It just threw me for a moment."
            mike.say "I didn't book with this guy, Alexis."
            mike.say "The photographer I spoke to was a girl."
            "Alexis looks at me in amazement."
            show alexis normal
            alexis.say "Don't you think that's a bit sexist, [hero.name]?"
            alexis.say "This guy's going to be taking pictures of me, sure."
            alexis.say "But that's his job - he's a professional!"
            "Photographer" "Ah..."
            "Photographer" "Is there a problem?"
            mike.say "Oh no, no problem at all."
            mike.say "I was just saying that when I called to book, I spoke to a woman."
            "Photographer" "Did you speak to Karen when you booked the shoot?"
            mike.say "Yeah, that name sounds familiar."
            mike.say "I'm sorry, I must have assumed she'd be the one taking the photos."
            "The photographer smiles and shakes his head."
            "Photographer" "We work as professional partners."
            "Photographer" "So you can end up with either one of us doing the shoot."
            mike.say "It's fine."
            mike.say "So...shall we get on with it?"
            "The photographer nods and leads the way deeper into the studio."
            show alexis happy
            "I also note that Alexis seems to have accepted my explanation too."
            "Which is a massive relief."
            $ game.active_date.score += 15
        "In fact, yes":
            "I was the one that paid for this photo-shoot."
            "And when I did that, I was sure of what I was buying."
            "But this guy was never part of that deal!"
            mike.say "I..."
            mike.say "I didn't book with this guy, Alexis!"
            mike.say "The photographer I spoke to was a girl!"
            "Alexis looks at me in amazement."
            show alexis normal
            alexis.say "Don't you think that's a bit sexist, [hero.name]?"
            alexis.say "This guy's going to be taking pictures of me, sure."
            alexis.say "But that's his job - he's a professional!"
            "Photographer" "Ah..."
            "Photographer" "Is there a problem?"
            alexis.say "You could say that..."
            show alexis annoyed
            alexis.say "Someone was expecting the photographer to be a woman."
            "Photographer" "Did you speak to Karen when you booked the shoot?"
            mike.say "Yeah, that name sounds familiar."
            mike.say "I thought she'd be the one taking the photos."
            "The photographer smiles and shakes his head."
            "Photographer" "We work as professional partners."
            "Photographer" "So you can end up with either one of us doing the shoot."
            "I shrug my shoulders and let out an irritated sigh."
            mike.say "Urgh..."
            mike.say "Okay, okay..."
            mike.say "Just make sure everything stays professional."
            "Unlike me, the photographer does just that."
            "But I note that Alexis shoots me a frown as we get on with it."
            "And I take that as a warning to behave myself."
            $ game.active_date.score -= 10
    "The photographer ushers Alexis into position."
    show alexis normal with screenshot
    play sound cameraclick
    "And then he starts snapping away with his camera."
    with screenshot
    play sound cameraclick
    pause 0.2
    with screenshot
    play sound cameraclick
    "I stand back and watch as the photo-shoot proceeds."
    "And it all seems to be playing out as I'd expected."
    "The photographer asks Alexis to try out various poses."
    with screenshot
    play sound cameraclick
    "All the time he's offering her positive encouragement."
    "Photographer" "That's great..."
    "Photographer" "Just keep it natural..."
    "Photographer" "Yeah, just like that..."
    "Photographer" "Just like you're making love to the camera!"
    mike.say "Wait a minute..."
    mike.say "What did you just say?"
    "The photographer doesn't seem to hear my question."
    "It looks like he's too wrapped up in the moment."
    show alexis flirt
    "Alexis is just as focused too."
    "Almost like she's forgotten that I'm even here."
    "But then the photographer pauses for a moment."
    "And he seems to be thinking about something."
    menu:
        "[hero.name] should be in the photo too" if hero.fitness >= 50:
            "Photographer" "Hmm..."
            "Photographer" "You're doing well, Alexis."
            "Photographer" "But I still feel like we're missing something..."
            show alexis surprised
            alexis.say "We are?"
            alexis.say "What is it that we're missing?"
            "It's about now that I realise what the photographer is looking at."
            "And it's a little uncomfortable to notice that it's me!"
            "Photographer" "You're the perfect representation of the feminine, Alexis."
            "Photographer" "But we need to balance that out with the masculine element."
            "Now Alexis is looking at me too."
            show alexis confused
            alexis.say "You mean..."
            "Photographer" "I do..."
            "Photographer" "I think we need your friend here to pose with you!"
            show alexis normal
            alexis.say "What do you say, [hero.name]?"
            alexis.say "Will you do it?"
            "I can feel a pang of fear in my stomach."
            "But I force myself to ignore it as I nod my head."
            mike.say "If that's what it takes, Alexis."
            mike.say "Then you can count me in!"
            $ game.active_date.score += 10
            if hero.fitness >= 75:
                "I walk over and stand close by Alexis."
                with screenshot
                play sound cameraclick
                "And then the photographer gets back to work."
                "I make sure to listen to his directions."
                "And I honestly do the best I can to follow them."
                "Somehow everything seems to just fall into place."
                with screenshot
                play sound cameraclick
                pause 0.2
                with screenshot
                play sound cameraclick
                "And from there, the shoot really kicks into a higher gear."
                with screenshot
                play sound cameraclick
                "Photographer" "That's it!"
                "Photographer" "Just like that!"
                show alexis happy
                alexis.say "Looking good, [hero.name]."
                with screenshot
                play sound cameraclick
                "Photographer" "Ooh...I'm feeling it."
                with screenshot
                play sound cameraclick
                "Photographer" "I'm getting shivers over here!"
                show alexis annoyed
                alexis.say "Erm..."
                alexis.say "Aren't you supposed to be shooting me too?"
                "Photographer" "I can't help it."
                "Photographer" "The camera loves this guy!"
                $ game.active_date.score += 15
            else:
                "I walk over and stand close by Alexis."
                with screenshot
                play sound cameraclick
                "And then the photographer gets back to work."
                "I make sure to listen to his directions."
                "And I honestly do the best I can to follow them."
                "But somehow I always seem to be in the way."
                "Or else I'm just not getting what he wants me to do."
                "Photographer" "No, not like that!"
                show alexis annoyed
                alexis.say "[hero.name], you're in my way!"
                "Photographer" "Can't you emote more loudly?"
                alexis.say "Ouch!"
                show alexis angry
                alexis.say "Now you're stepping on my foot!"
                "Photographer" "Oh dear..."
                "Photographer" "This isn't working out at all!"
                "In the end I shuffle away from the shoot."
                "And I return to the place where I was standing before."
                show alexis normal
                with screenshot
                play sound cameraclick
                "Meanwhile Alexis and the photographer get back to it."
                "Doing the best they can to recover something of value."
                $ game.active_date.score -= 5
        "Alexis should wear less clothes":
            "Photographer" "Hmm..."
            "Photographer" "You're doing well, Alexis."
            "Photographer" "But I still don't feel like I'm capturing the real you."
            show alexis surprised
            alexis.say "You don't?"
            alexis.say "What can we do about it?"
            "Photographer" "Well..."
            "Photographer" "This is going to sound crazy, but hear me out."
            "Photographer" "What if you were to try taking off some of your clothes?"
            "At the mere mention of stripping off, my ears perk up."
            mike.say "Wait a minute..."
            mike.say "You want her to get naked?"
            "Photographer" "Trust me, it's just for the sake of artistic integrity."
            show alexis normal
            alexis.say "What do you think, [hero.name]?"
            alexis.say "I'm up for it if you are!"
            if alexis.love >= 180:
                "I think about it for a moment."
                "And then I nod my head."
                mike.say "If you think it'll make the shots better..."
                mike.say "Then sure, why the hell not."
                show alexis happy
                mike.say "Never let it be said that I'm a prude!"
                "The photographer nods and offers me a smile."
                "Photographer" "Great!"
                "Photographer" "I just knew you were the enlightened type."
                "Alexis nods happily too as she strips off."
                show alexis naked happy
                "As soon as she's naked, the shoot resumes."
                with screenshot
                play sound cameraclick
                "Which leaves me to watch, all the time trying to look natural."
                "But inside I can't believe my luck."
                "Alexis would never have agreed to this if I'd suggested it."
                with screenshot
                play sound cameraclick
                "And my guess is that the photographer would have called me a sleaze too."
                "Now they're both doing all the work for me!"
                "And I can't wait to see the end result."
                $ game.active_date.score += 15
            else:
                "I shake my head."
                "And I cross my arms over my chest for added effect."
                mike.say "Hell no!"
                mike.say "What is this supposed to be?"
                show alexis annoyed
                mike.say "Some kind of porn-shoot?"
                "The photographer holds up his hands and backs off."
                "Photographer" "No worries."
                "Photographer" "It was just a suggestion, that's all."
                "He does the best he can to get back into the shoot."
                with screenshot
                play sound cameraclick
                "But I can tell that he's bummed out by my refusal."
                "Alexis, on the other hand, is more vocal."
                alexis.say "Why did you have to go and be such a prude, [hero.name]?"
                show alexis angry
                alexis.say "This was all your idea in the first place."
                alexis.say "And the guy already told you it was artistic, not dirty!"
                "All I can do is frown and look at the floor until Alexis's eyes are off me."
                "And then I keep quiet, still sulking at being called a prude."
                $ game.active_date.score -= 10
    show alexis date normal with fade
    "Once the actual shoot is over, the photographer shows us the shots."
    "Sure, we're only seeing them on the screen of his digital camera."
    "But they look really impressive all the same, well worth the money."
    mike.say "Wow!"
    mike.say "I can't wait to get my hands on those!"
    alexis.say "Me too."
    show alexis happy
    alexis.say "I look amazing in those photographs!"
    mike.say "Huh?"
    mike.say "What do you mean, Alexis?"
    "Alexis furrows her brows at my question."
    show alexis confused
    alexis.say "Well..."
    alexis.say "I'm getting a set too, right?"
    alexis.say "After all, this is supposed to be a birthday gift for me."
    show alexis normal
    alexis.say "Isn't it?"
    "As she says all of this, the photographer chimes in too."
    "Photographer" "Actually, I wanted to ask you something too."
    "Photographer" "These turned out so well I'd like to use them in my portfolio."
    "Photographer" "You know, put them on my website and social media?"
    "Photographer" "Even hang some on the wall in the reception."
    if alexis.love >= 180:
        "I could get possessive of the photos, keep them to myself."
        "But they're right, these really are too good not to share."
        mike.say "Of course you should have a set, Alexis."
        mike.say "After all, you are in the photos."
        show alexis happy
        "This seems to please Alexis no end."
        "And she beams with happiness."
        "But then the photographer coughs."
        "Photographer" "Ahem..."
        "Photographer" "And what about my humble request?"
        "I turn to Alexis."
        mike.say "It's fine with me."
        mike.say "But you should have a say too, Alexis."
        mike.say "You're the one that's actually posing in them."
        alexis.say "Of course I want him to use them, [hero.name]."
        alexis.say "It's not every day I get to be in a portfolio!"
        "I shrug and nod, feeling like I've managed to make them both happy."
        $ game.active_date.score += 15
    else:
        "I can feel myself getting more possessive by the moment."
        "I hate the thought of anyone else getting to see the photos."
        mike.say "No way!"
        mike.say "I paid for these photos myself."
        mike.say "They're mine, and I'm not sharing them!"
        "The photographer looks disappointed."
        "But he nods all the same, remaining professional."
        "Photographer" "I understand."
        "Photographer" "You have the right to refuse."
        "But Alexis is under no such obligation."
        "And she doesn't hesitate to tell me off."
        show alexis annoyed
        alexis.say "[hero.name]!"
        alexis.say "Why are you being like this?"
        alexis.say "I thought you just wanted nice photos of me?"
        alexis.say "But now you're acting all creepy!"
        mike.say "That's not how it is, Alexis."
        mike.say "I just want to get what I paid for."
        mike.say "And that's all there is to it."
        $ game.active_date.score -= 10
    show alexis normal
    "I take care of the last few details for the photo-shoot."
    "And then I walk over to where Alexis is waiting for me."
    "She looks pretty happy with the way that it's all worked out."
    "But I can see that there's something else in her eyes."
    "Like there's a question on her mind that she's afraid to ask."
    mike.say "Come on, Alexis..."
    mike.say "Out with it!"
    show alexis annoyed
    alexis.say "Huh?"
    alexis.say "What are you talking about?"
    mike.say "I know you too well to be fooled, Alexis."
    mike.say "So ask me the question!"
    "Alexis looks like she's going to continue denying it for a moment."
    "But then she surrenders and nods her head."
    show alexis normal
    alexis.say "Okay, you got me."
    alexis.say "And I know that this is going to sound bad."
    alexis.say "But is the shoot the only present you got me?"
    if not hero.has_gifts:
        "Ah shit..."
        "Maybe I should have remembered to get her a little something."
        "Even just a token gift so she had something while we're waiting on the photos."
        "But I didn't, and so I'm going to have to talk my way out of this one."
        "Luckily Alexis just gave me the best option that I have."
        mike.say "Yeah, Alexis..."
        mike.say "The shoot was kind of the present!"
        show alexis annoyed
        alexis.say "Oh..."
        alexis.say "Okay, [hero.name]."
        show alexis normal
        alexis.say "It was a great one too."
        $ game.active_date.score -= 20
        $ alexis.love -= 10
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_1
        if _return != "done":
            if _return not in ["None", "exit"]:
                "I nod and pull out the gift that I bought for Alexis."
                mike.say "I did get you a little something, Alexis."
                mike.say "Just kind of a token gift, you know?"
                mike.say "So you'd have something while we wait for the photos."
                play sound [paper_ripping_1, paper_ripping_2]
                "Alexis takes the gift and eagerly begins to unwrap it."
                show alexis happy
                alexis.say "Aw!"
                alexis.say "Thanks, [hero.name]."
                show alexis flirt
                alexis.say "You're the best!"
                if _return:
                    "But the moment she sees what's inside, her face lights up."
                    show alexis happy
                    alexis.say "Oh my god!"
                    mike.say "What's the problem, Alexis?"
                    mike.say "Is there something wrong with it?"
                    show alexis normal
                    alexis.say "You said this was like, a token gift!"
                    alexis.say "But it's amazing!"
                    show alexis happy
                    alexis.say "Thank you so much!"
                    $ game.active_date.score += 20
                else:
                    "But the moment she sees what's inside, her face falls."
                    show alexis confused
                    mike.say "What's the problem, Alexis?"
                    mike.say "Is there something wrong with it?"
                    alexis.say "Oh..."
                    show alexis normal
                    alexis.say "Oh no..."
                    alexis.say "But then you did say that it was a token gift."
                    $ game.active_date.score -= 10
            else:
                "Ah shit..."
                "Maybe I should have remembered to get her a little something."
                "Even just a token gift so she had something while we're waiting on the photos."
                "But I didn't, and so I'm going to have to talk my way out of this one."
                "Luckily Alexis just gave me the best option that I have."
                mike.say "Yeah, Alexis..."
                mike.say "The shoot was kind of the present!"
                show alexis annoyed
                alexis.say "Oh..."
                alexis.say "Okay, [hero.name]."
                show alexis normal
                alexis.say "It was a great one too."
                $ game.active_date.score -= 20
                $ alexis.love -= 10
    "Once we're done wrapping up the shoot, it's time to leave."
    scene bg street
    show alexis date normal at center, zoomAt(1.25, (640, 900))
    with fade
    "Alexis and I walk out into the street, back to reality."
    "And there's that long, pregnant moment between us."
    mike.say "So..."
    mike.say "I think that's all the stuff I had planned for our date."
    mike.say "What do you want to do now, Alexis?"
    mike.say "I mean, I understand if you're tired and all..."
    if game.active_date.score >= 80 and alexis.sexperience >= 1:
        "Alexis looks at me in amazement."
        "And then she shakes her head."
        show alexis happy
        alexis.say "Are you kidding?"
        alexis.say "I'm having a great time."
        alexis.say "And I'm not ready for it to end yet."
        show alexis flirt
        "I feel a surge of delight at Alexis's enthusiasm."
        "But I do the best I can to sound nonchalant."
        mike.say "Well okay, Alexis..."
        mike.say "I guess that we can find something else to do."
        mike.say "Let's see if we can grab a taxi."
        mike.say "Maybe go somewhere a little more private..."
        call alexis_birthday_sex from _call_alexis_birthday_sex
    else:
        "Alexis nods and covers her mouth as she yawns."
        "But part of me can't help suspecting that she's putting it on."
        alexis.say "Oh..."
        show alexis annoyed
        alexis.say "Pardon me!"
        alexis.say "But yeah, I am feeling a little tired."
        show alexis normal
        alexis.say "You mind if we call it a day?"
        mike.say "Sure, Alexis, sure."
        mike.say "Let's see if we can get you a taxi or something."
        "It's not like I want the date to end yet."
        "But there's no point in arguing with Alexis."
        "Better to let it end here and now."
        scene bg street with fade
        "That way I can put more effort into our next date."
        "Provided there is one..."
    return

label alexis_birthday_sex:
    scene bg street with fade
    "I can almost feel the buzz that the photo-shoot seem to have given Alexis."
    "All the way back to my place in the taxi she keeps shooting me glances."
    "And when I look back, she quickly turns her head away, looking out of the window."
    "But at the same time I can feel her squeezing my hand."
    "With more intensity as we get ever closer to my place."
    "As soon as the taxi pulls up and the fare is paid, she yanks me out and up the path."
    scene bg house
    show alexis date normal
    with fade
    "I'm already fumbling for my keys as we make it onto the front porch."
    "But I still don't seem to be going fast enough for Alexis!"
    alexis.say "Come on, [hero.name]..."
    alexis.say "What's with the hold-up?"
    mike.say "Settle down, Alexis!"
    mike.say "I need to get the damn keys out of my pocket..."
    alexis.say "Well hurry up!"
    mike.say "Okay, okay..."
    mike.say "There we go!"
    scene bg livingroom
    show alexis date flirt at center, zoomAt (2.0, (640, 1300))
    with fade
    "The very moment I have the door open, Alexis leaps into action."
    "She pushes me inside with a strength that totally catches me off-guard."
    "And before I know it, she's hustling me through the house."
    "It's only familiarity with the place that lets me know where we're headed."
    "But it's a genuine relief to know that it seems to be my bedroom!"
    scene bg bedroom1
    show alexis date flirt blush at center, zoomAt (2.0, (640, 1300))
    with fade
    "Alexis opens the door and pushes me inside, then turns to close it."
    "I'm still a little dizzy from being dragged through the house."
    "So I take the opportunity to sit down on the nearest piece of furniture."
    "And sure, that does happen to be my bed."
    "But I figure that I already know which way this is going!"
    "Alexis still has her back turned to me as she closes the door."
    "Yet she begins to speak even before she turns around to face me."
    alexis.say "You know why we're here, [hero.name]."
    alexis.say "I don't need to explain it to you."
    show alexis normal
    alexis.say "Do you know why?"
    mike.say "Erm..."
    mike.say "I could guess..."
    alexis.say "Don't play dumb."
    alexis.say "You know as well as I do."
    alexis.say "It's because I can feel the way you're looking at me right now."
    mike.say "You can?"
    show alexis flirt
    alexis.say "Oh yes I can."
    alexis.say "And I could feel it all the way through the shoot as well."
    alexis.say "I could feel you looking at me with barely suppressed desire!"
    alexis.say "And the thought of it's been driving me crazy!"
    show alexis topless with dissolve
    "Alexis turns as she begins to strip off her clothes."
    "She does it slowly, letting me see every movement."
    "And I'm reminded of how I was watching her back in the studio."
    "I've got to admit that she's right - I was turned on the whole time."
    "Now I know that she was fully aware of that fact."
    show alexis naked with dissolve
    "And that it was having the same effect on her too."
    "I seem to begin taking off my own clothes without a conscious thought."
    "I'm so wrapped up in watching Alexis that I don't even know I'm doing it."
    "So by the time she makes it to the bed, we're both naked."
    "As Alexis climbs slowly onto the bed, I'm stirring too."
    "The closer she comes to me, the harder my cock gets."
    "And by the time she's crawling over my legs, it's stood up straight."
    "Alexis giggles at the sight of it."
    "Clearly she's delighted with the effect that she's having on me."
    "She reaches out with one hand, grabbing it as she straddles my thighs."
    scene alexis cowgirl with fade
    alexis.say "I was thinking about this the whole time."
    alexis.say "Thinking about how hard the sight of me was making you."
    alexis.say "And how good it would feel to have it inside of me."
    "Alexis has her fingers wrapped around the shaft of my cock as she says all of this."
    "And she's working it up and down too, adding to the arousal that I'm feeling."
    "All I can do is lie still and let her do whatever the hell she wants to me."
    "In fact the most that I can manage is to nod frantically."
    "That's a fact that only seems to make Alexis more confident."
    "So she doesn't even ask permission a moment later."
    "She simply presses the head of my cock hard against her pussy."
    "And then she pushes herself downwards."
    show alexis cowgirl vaginal
    "I gasp as I feel the natural resistance of her muscles."
    "Then I moan as that same resistance begins to melt away."
    "Little by little, Alexis lowers herself onto me."
    "And the fact she's taking it slow makes it all the more intense."
    "Suddenly I seem to remember that I'm not restrained in any way."
    "That I have a perfectly good pair of arms not doing anything right now."
    "In that instant, my hands reach out and take hold of Alexis's waist."
    "She jumps a little, surprised at the my sudden movements."
    "But that's all the time she gets to react."
    "Because a moment later, I begin to move in earnest."
    "Now that I have a hold of Alexis, I start to take charge."
    "My cock's deep inside of her, and I push it further still."
    "She tosses her head back, reeling from the sensation."
    "And I waste no time in beginning to move."
    "My lower half moving up and down lets me thrust into her."
    "I don't hold back on the speed either, moving ever faster."
    "Now it's Alexis's turn to reach out and hold onto me."
    "She plants her hands on my shoulders, fingers digging into my skin."
    "Alexis tries to use her weight to keep herself in place."
    "But it's not enough, and she's tossed around as I hammer away at her."
    "Where before Alexis was the one teasing me, she's now all but helpless."
    "Her eyes are squeezed shut, and her head is tossed this way and that."
    "Swaying to and fro, her breasts dance in front of my eyes."
    "I want desperately to reach out and hold them."
    "But I don't dare to let go of her before this thing is over."
    alexis.say "Ah..."
    alexis.say "Oh god..."
    alexis.say "I'm going to..."
    alexis.say "Mmm..."
    show alexis cowgirl ahegao
    "Alexis starts to cum even before she can say the actual words."
    "And as I'm holding onto her, I feel every twinge as it happens."
    "Her body goes into a kind of sensual meltdown while I'm still inside of her."
    "And with all that happening, I don't have a hope of holding on."
    show alexis cowgirl creampie with vpunch
    "I grunt and grimace as I shoot my load into Alexis."
    with vpunch
    "An action which only serves to make her own orgasm more intense."
    with vpunch
    "Eventually her arms tremble and then give way."
    "Which means that she falls on top of me, still quivering and quaking."
    show alexis cowgirl -vaginal limp -creampie drip
    show pussy_insert alexis cum zorder 1 at zoomAt(0.75, (40, 200))
    "Gently I roll Alexis onto her side and feel her slide off of me."
    "Neither of us speaks as we lie there."
    "We just enjoy the moment in silence."
    "Letting the sensations speak for themselves."
    hide pussy_insert
    $ alexis.sexperience += 1
    call sleep ("alexis") from _call_sleep_65
    $ game.room = "bedroom1"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
