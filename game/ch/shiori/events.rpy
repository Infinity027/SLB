
init python:
    Event(**{
    "name": "shiori_start",
    "label": "shiori_start",
    "priority": 500,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsFlag("hiringshiori")
            ),
        ],
    "music": "music/roa_music/miss_summer.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "shiori_event_01",
    "label": "shiori_event_01",
    "priority": 100,
    "conditions": [
        IsDone("shiori_start"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work_personal", "workhard_personal")
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            HasRoomTag("work"),
            MinStat("love", 20),
            ),
        ],
    "music": "music/roa_music/miss_summer.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "shiori_event_02",
    "label": "shiori_event_02",
    "priority": 100,
    "conditions": [
        IsDone("shiori_event_01"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work_personal", "workhard_personal")
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            HasRoomTag("work"),
            MinStat("love", 30),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            ),
        ],
    "music": "music/roa_music/miss_summer.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "shiori_event_03",
    "label": "shiori_event_03",
    "priority": 100,
    "conditions": [
        IsDone("shiori_event_02"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work_personal", "workhard_personal")
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            HasRoomTag("work"),
            MinStat("love", 40),
            ),
        ],
    "music": "music/roa_music/miss_summer.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "shiori_event_04",
    "label": "shiori_event_04",
    "priority": 100,
    "conditions": [
        IsDone("shiori_event_03"),
        IsNotDone("shiori_event_05"),
        HeroTarget(IsGender("male")),
        PersonTarget(shiori,
            IsActive(),
            HasRoomTag("work"),
            IsFlag("babysitting", False),
            MinStat("love", 75),
            ),
        ],
    "music": "music/roa_music/miss_summer.ogg",
    "do_once": False,
    })

    Event(**{
    "name": "shiori_event_05",
    "label": "shiori_event_05",
    "priority": 500,
    "duration": 4,
    "conditions": [
        IsHour(19, 22),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            HasRoomTag("home"),
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            IsFlag("babysitting"),
            ),
        ],
    "music": "music/roa_music/miss_summer.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "shiori_event_06",
    "label": "shiori_event_06",
    "priority": 100,
    "conditions": [
        IsDone("shiori_event_05"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work_personal", "workhard_personal")
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            HasRoomTag("work"),
            MinStat("love", 100),
            ),
        ],
    "music": "music/roa_music/miss_summer.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "shiori_has_had_sex",
    "label": "shiori_has_had_sex",
    "priority": 1000,
    "conditions": [
        IsDone("shiori_event_06"),
        PersonTarget(shiori,
            MinStat("love", 110),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "shiori_stripclub",
    "label": "shiori_stripclub",
    "priority": 100,
    "conditions": [
        IsDone("shiori_has_had_sex"),
        HeroTarget(
            IsGender("male"),
            IsRoom("stripclub")
            ),
        PersonTarget(shiori,
            Not(IsPresent()),
            Not(IsHidden()),
            MinStat("love", 120),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/miss_summer.ogg",
    })

    Event(**{
    "name": "shiori_stripclub_confession",
    "label": "shiori_stripclub_confession",
    "priority": 100,
    "conditions": [
        IsDone("shiori_stripclub"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("mcoffice")
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            HasRoomTag("work"),
            MinStat("love", 120),
            ),
        ],
    "music": "music/roa_music/miss_summer.ogg",
    "do_once": True,
    })



    Event(**{
    "name": "shiori_scold_2",
    "label": "shiori_scold_2",
    "priority": 100,
    "conditions": [
        IsDone("shiori_event_01"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("mcoffice"),
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            HasRoomTag("work"),
            MinStat("sub", 40),
            ),
        ],
    "music": "music/roa_music/miss_summer.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "shiori_scold_3",
    "label": "shiori_scold_3",
    "priority": 100,
    "conditions": [
        IsDone("shiori_scold_2"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("mcoffice"),
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            HasRoomTag("work"),
            MinStat("love", 60),
            MinStat("sub", 50),
            ),
        ],
    "music": "music/roa_music/miss_summer.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "shiori_scold_4",
    "label": "shiori_scold_4",
    "priority": 100,
    "conditions": [
        IsDone("shiori_scold_3"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work_personal", "workhard_personal")
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            HasRoomTag("work"),
            MinFlag("spank_counter", 1),
            MinStat("love", 80),
            MinStat("sub", 60),
            ),
        ],
    "music": "music/roa_music/miss_summer.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "shiori_scold_5",
    "label": "shiori_scold_5",
    "priority": 100,
    "conditions": [
        IsDone("shiori_scold_4"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work_personal", "workhard_personal")
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            HasRoomTag("work"),
            MinFlag("spank_counter", 2),
            MinStat("love", 100),
            MinStat("sub", 70),
            ),
        ],
    "music": "music/roa_music/miss_summer.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "shiori_coffee_2",
    "label": "shiori_coffee_2",
    "priority": 100,
    "conditions": [
        IsDone("shiori_event_02"),
        HeroTarget(
            IsGender("male"),
            IsRoom("office", "personal", "ceo"),
            IsActivity("work_personal", "workhard_personal"),
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            HasRoomTag("work"),
            IsFlag("coffee"),
            MinStat("love", 110),
            MinStat("sub", 50),
            ),
        ],
    "music": "music/roa_music/miss_summer.ogg",
    "do_once": False,
    "once_week": True,
    "chances": 20,
    })

    Event(**{
    "name": "shiori_sleep_office",
    "label": "shiori_sleep_office",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("work_personal", "workhard_personal"),
            IsRoom("personal", "ceo"),
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            HasRoomTag("work"),
            MinStat("love", 40),
            Not(IsFlag("stop_sleep_office")),
            ),
        ],
    "music": "music/roa_music/miss_summer.ogg",
    "do_once": False,
    "once_week": True,
    "chances": 20,
    })

    Event(**{
    "name": "shiori_show_off_3",
    "label": "shiori_show_off_3",
    "priority": 100,
    "conditions": [
        IsDone("shiori_event_06"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work_personal", "workhard_personal")
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            HasRoomTag("work"),
            IsFlag("buttplug"),
            MinStat("love", 120),
            ),
        ],
    "music": "music/roa_music/miss_summer.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "shiori_office_bj",
    "label": "shiori_office_bj",
    "priority": 100,
    "conditions": [
        IsDone("shiori_scold_5"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("work"),
            ),
        PersonTarget(shiori,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 120),
            MinStat("sub", 80),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            ),
        ],
    "music": "music/roa_music/miss_summer.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "shiori_kiss_me",
    "label": "shiori_kiss_me",
    "max_girls": 1,
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(shiori,
            IsPresent(),
            Not(IsHidden()),
            MinFlag("kiss", 1),
            MinStat("love", 150),
            ),
        ],
    "chances": 25,
    "music": "music/roa_music/miss_summer.ogg",
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "shiori_preg_talk",
    "label": "shiori_preg_talk",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate())
            ),
        PersonTarget(shiori,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("toldpreg", False),
            MinCounter("pregnant", 6),
            ),
        ],
    "music": "music/roa_music/miss_summer.ogg",
    "quit": False,
    })

    Event(**{
    "name": "shiori_meeting",
    "label": "shiori_meeting",
    "priority": 0,
    "conditions": [
        IsDone("shiori_event_05"),
        IsHour(0, 9),
        HeroTarget(IsActivity("work_personal", "workhard_personal")),
        PersonTarget(aletta,
            Not(IsHidden()),
            MinStat("love", 50),
            ),
        PersonTarget(audrey,
            Not(IsHidden()),
            MinStat("love", 50),
            ),
        PersonTarget(shiori,
            Not(IsHidden())
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "shiori_payoff_conversation",
    "label": "shiori_payoff_conversation",
    "display_name": "Tell her you paid off her debt",
    "icon": "button_shiori",
    "conditions": [
        IsDone("shiori_strip_club_payoff"),
        HeroTarget(IsGender("male")),
        PersonTarget(shiori,
            IsActive(),
            MinStat("love", 180),
            ),
        ],
    "do_once": True,
    })

    Activity(**{
    "name": "shiori_strip_club_payoff",
    "label": "shiori_strip_club_payoff",
    "display_name": "Pay off the manager",
    "rooms": ["stripclub"],
    "conditions": [
        IsDone("shiori_strip_club_manager"),
        HeroTarget(
            IsGender("male"),
            MinStat("money", 10000)
            ),
        ],
    "do_once": True,
    "icon": "shiori",
    })

    Event(**{
    "name": "shiori_strip_club_manager",
    "label": "shiori_strip_club_manager",
    "priority": 100,
    "conditions": [
        IsDone("shiori_bruises"),
        IsHour(0, 21),
        HeroTarget(
            IsGender("male"),
            IsRoom("stripclub")
            ),
        PersonTarget(shiori,
            MinStat("love", 160)
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            ),
        PersonTarget(audrey,
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/miss_summer.ogg",
    })

    Event(**{
    "name": "shiori_bruises",
    "label": "shiori_bruises",
    "priority": 100,
    "conditions": [
        IsDone("shiori_work_no_show"),
        IsHour(0, 11),
        HeroTarget(
            IsGender("male"),
            IsActivity("work_personal", "workhard_personal")
            ),
        PersonTarget(shiori,
            IsFlag("BruisesDelay", False)
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/miss_summer.ogg",
    })

    Event(**{
    "name": "shiori_work_no_show",
    "label": "shiori_work_no_show",
    "priority": 100,
    "conditions": [
        IsDone("shiori_blackmail_confession"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work_personal", "workhard_personal")
            ),
        PersonTarget(shiori,
            MinStat("love", 150)
            ),
        PersonTarget(audrey,
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/miss_summer.ogg",
    })

    InteractEvent(**{
    "name": "shiori_blackmail_confession",
    "label": "shiori_blackmail_confession",
    "priority": 100,
    "conditions": [
        IsDone("shiori_stripclub_lapdance_1"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("mcoffice")
            ),
        PersonTarget(shiori,
            IsActive(),
            MinStat("love", 140),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/miss_summer.ogg",
    })

    Event(**{
    "name": "shiori_stripclub_lapdance_1",
    "label": "shiori_stripclub_lapdance_1",
    "priority": 100,
    "conditions": [
        IsDone("shiori_stripclub_confession"),
        HeroTarget(
            IsGender("male"),
            IsActivity("get_a_lapdance")
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            IsRoom("stripclub"),
            MinStat("love", 130),
            ),
        ],
    "music": "music/roa_music/miss_summer.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "shiori_stripclub_lapdance_2",
    "label": "shiori_lapdance_2",
    "priority": 100,
    "conditions": [
        IsDone("shiori_stripclub_lapdance_1"),
        HeroTarget(
            IsGender("male"),
            IsActivity("get_a_lapdance"),
            HasStamina(),
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            IsRoom("stripclub"),
            MinStat("love", 140),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/miss_summer.ogg",
    })



    Event(**{
    "name": "shiori_investigation_callback",
    "label": "shiori_investigation_callback",
    "conditions": [
        IsNotDone("cassidy_investigation_complete"),
        IsHour(9, 22),
        PersonTarget(shiori,
            Not(IsPresent()),
            MinCounter("investigationcallback", 2),
            ),
        ],
    "music": "music/roa_music/miss_summer.ogg",
    "do_once": True,
    })


label shiori_start:
    $ shiori.unhide()
    return

label shiori_event_01:
    if shiori.love.max < 30:
        $ shiori.love.max = 30
    "Getting chewed up by my superior for missing the call of an important client is not exactly the way I thought my day was going to go."
    "I'm not supposed to take calls, anymore. That's my secretary's job. I guess it's time to go find out what's up."
    show shiori
    "I find Shiori at her desk, talking on the phone and filing her nails."
    mike.say "Shiori, do you have a minute?"
    shiori.say "Hold on, [hero.name]. Yes... uh-huh? I'll let him know right away."
    show shiori happy
    "She hangs up the phone, looking up to me with a smile on her face."
    shiori.say "That was the order you called in for yesterday."
    shiori.say "They'll be making their way in by tomorrow..."
    shiori.say "And..."
    show shiori surprised
    "She gasps, covering her mouth."
    shiori.say "Oh my gosh! [hero.name]! "
    show fx drop
    show shiori embarrassed
    shiori.say "The Parkerson appointment! I totally forgot."
    shiori.say "I'm so sorry!"
    "I shake my head."
    mike.say "Sorry isn't going to cut it. You're in deep trouble, do you understand?"
    mike.say "Now, I'm going to have to stay overtime just to find a replacement! I have plans. I can't just go around fixing your messes."
    show shiori sad
    shiori.say "I... I guess you're going to write me up, aren't you...?"
    "She lowers her head a bit, slumping her shoulders forward as she sighs, defeated."
    mike.say "You need to shape up, or there's going to be some serious consequences, that's for sure."
    shiori.say "Serious, huh...?"
    "From under her breath, she mutters something."
    mike.say "What's that?"
    "She gasps again."
    shiori.say "Oh, I'm sorry boss, did you hear that?"
    mike.say "What did you say to me just now?"
    "There's a silence as she glances back and forth. Everyone else is out to lunch, leaving her and myself alone for the time being."
    show shiori embarrassed blush
    shiori.say "Oh, nothing. I just said 'what are you going to do, spank me?"
    mike.say "I... what?"
    "She shrugs."
    shiori.say "Well, you aren't going to write me up, right?"
    shiori.say "Guess you could punish me some other way."
    shiori.say "I mean that WOULD get the message across not to mess with you anymore."
    "The smile on her face, the redness on her cheeks..."
    mike.say "Wait a minute... are you...?"
    shiori.say "Hm...?"
    "I shake my head."
    mike.say "No, nevermind. Just see if you can't get them to reschedule, or else you really are going to get it."
    shiori.say "Oooh, yes, [hero.name]!"
    "She says, saluting me and then grabbing the phone."
    show shiori normal blush
    "As I walk away from her, I give her one last parting look, curious at what her game is. But as I see her, her eye catches mine, and a slight smirk spread across her face."
    mike.say "Just make sure if you make another mistake..."
    "I begin to speak to her, taking the time to steel myself for what I was about to imply."
    mike.say "...you'd better make sure its not something so important. I don't want to get REALLY angry with you and make a..."
    "I cough and straighten my tie."
    mike.say "I don't want to make a DRASTIC decision."
    show shiori flirt blush
    "She bites her lip and leans over her computer, typing away furiously as I finally turn and head back to my desk."
    "Let's see how morale goes after THAT."
    hide shiori
    $ shiori.love += 5
    return

label shiori_event_02:
    if shiori.love.max < 40:
        $ shiori.love.max = 40
    show shiori at left with easeinleft
    "I watch Shiori absently as she scurries here and there, nodding and shaking her head at the answers that she gets from each successive colleague."
    "Strictly speaking, the company's quite progressive on things like making drinks and fetching stuff for superiors."
    show shiori at center with ease
    "There's no specific requirement for someone of her grade to actually do things like that."
    "And even if Aletta or I asked her to, Shiori could still say no and be well within her rights to do so."
    "But she seems eager to take on any and all roles that she can of that nature, as though she wants to mother the entire office and make herself indispensable."
    show shiori at right with ease
    "I keep on trying to tear my attention away from Shiori and get back to work, as she's only taking down orders for drinks after all."
    "And yet I find that, for some reason, I can't take my eyes off of her for more than a couple of seconds before I feel compelled to look her way again."
    show shiori at right4 with ease
    "Full disclosure up front, if you'll pardon the pun - I know that she has unfeasibly large breasts."
    "They're distracting enough, even when she's trying to hide them under her otherwise demure and sensible work-clothes."
    show shiori at top_right with ease
    "But it's not just that, you have to believe me!"
    "There's just something about how deferential and eager to please Shiori seems to be."
    "Something I can't quite put my finger on, and yet it makes me wonder what lies behind her being so damn needy and quick to seek praise like that..."
    show shiori happy at center with ease
    shiori.say "Good morning, [hero.name]."
    "I jerk to attention at my desk, as Shiori bustles in on me and bursts the bubble of my thoughts with her cheery presence."
    mike.say "Erm...hi, Shiori - what can I do for you this morning?"
    "She smiles at this, almost blushing at the same time, clasping her hands together and cocking her head on the side as she looks at me."
    show shiori normal
    shiori.say "Don't be silly, [hero.name] - I'm the one that's supposed to do things for you!"
    shiori.say "You can ask me to do anything you want, any time you feel the need..."
    "Is it me, or did it just get hotter in here?"
    "I fiddle with my collar nervously, while I momentarily lose the power of speech."
    mike.say "COFFEE!"
    show shiori surprised with vpunch
    "Shiori jumps slightly at the volume with which the word comes out of me."
    "I can't help but notice the impressive way that her breasts jump in sympathy too."
    mike.say "Coffee, Shiori - I guessed that you were going round asking people how they took theirs just now!"
    show shiori happy
    shiori.say "Oh, yes, of course...that's what I came in here to ask."
    show shiori normal blush
    shiori.say "I'm such a scatter-brain, [hero.name] - whatever are you going to do with me?"
    "There's a suggestive weight to that last question that I try to ignore as best I can."
    mike.say "Well, Shiori - getting back to the subject of the coffee..."
    menu:
        "Black":
            mike.say "I like my coffee the same way I like my women."
            mike.say "Sweet, black and hot as hell!"
            show shiori sad
            "I laugh the instant after I say this, trying to show Shiori that I'm joking."
            "But she looks more shocked and embarrassed than anything else."
            "Also a little hurt too, as though I've said something to deliberately hurt her alone."
            mike.say "Ah look, I'm sorry, Shiori...that was just a poor attempt at a joke."
            mike.say "For the record - I take my coffee black with one sugar."
            mike.say "And I'd be very grateful if you could make me one."
            show shiori normal
            "Shiori smiles weakly at this, nodding before she turns to go."
            hide shiori with easeoutleft
            "She leaves me hoping that I've not just landed myself an appointment with human resources."
            "I really hope not, as I can't take the prospect of sitting through the orientation video on sexual harassment again!"
        "Milky":
            $ shiori.flags.coffee = True
            mike.say "I always take mine white - I can't stand the taste of the stuff without milk, you know?"
            show shiori happy
            "For some reason, Shiori seems to be oddly pleased with this statement, almost like I gave her the exact answer she was looking for."
            shiori.say "Great, [hero.name] - I'll be sure to make it nice and milky for you!"
            "I try not to be too weirded out by her enthusiasm at discovering I like my coffee with plenty of milk."
            mike.say "Erm...okay, Shiori...was there anything else that you wanted to ask me right now?"
            show shiori normal
            shiori.say "No, I don't think so..."
            shiori.say "But, of course, that's not to say that there isn't!"
            show shiori joke
            shiori.say "I'm such a scatter-brain, after all!"
            "And with that, she turns around and bustles out of my office."
            hide shiori with easeoutleft
            "If it had been anyone else, then I'd have fully expected to be looking up to find a white coffee on my desk sometime in the next ten minutes."
            "But as it's Shiori I'm dealing with, it could well be tomorrow before one appears."
            if renpy.has_label("shiori_achievement_5") and not game.flags.cheat:
                call shiori_achievement_5 from _call_shiori_achievement_5
    "So there I am - left feeling odd and edgy by the supposedly simple act of having Shiori come in and ask me how I take my coffee."
    "I shake my head, and then try to get my mind back on my work once more."
    "But I still can't keep myself from taking the occasional glance out into the office and shaking my head at Shiori's quirkiness."
    return

label shiori_event_03:
    if shiori.love.max < 75:
        $ shiori.love.max = 75
    "I hear the sound of someone coming into my office and saying something to get my attention."
    "But it's only when I finally look up that I realise I can't actually see them for the piles of paperwork on my desk."
    "I bob this way and that as the person on the other side is doing the same thing, until I see just who's there."
    show shiori
    mike.say "Oh, hey there, Shiori."
    mike.say "Didn't see you there for all of this paperwork!"
    show shiori happy
    "Shiori smiles weakly, staring at the stacks that were keeping her concealed."
    shiori.say "Hello, [hero.name]."
    show shiori normal
    shiori.say "That's actually what I wanted to talk to you about."
    shiori.say "Would you like me to archive some of this in the basement?"
    "Now that she's mentioned it, I can see that Shiori's right."
    "How on earth did I let things get this bad without noticing it?"
    mike.say "That'd be great, Shiori."
    mike.say "But it looks like a hell of a lot of work."
    if Person.is_not_hidden("lavish"):
        mike.say "Maybe ask Audrey and Lavish to lend a hand too?"
    else:
        mike.say "Maybe ask Audrey to lend a hand too?"
    show shiori happy
    shiori.say "Don't worry, [hero.name], I can handle it!"
    "I watch as Shiori gamely begins to scoop up the first armful of papers from one of the piles."
    show shiori annoyed
    "She struggles, but looks determined to succeed, even as the pile wobbles precariously."
    "And then it happens."
    hide shiori with moveoutbottom
    play sound body_fall
    pause 0.3
    with vpunch
    "I don't know which comes first - if the pile collapses or she trips over her own feet."
    "Either way, the papers cascade to the floor and Shiori follows then down."
    show shiori fall closed papers
    "She lands on her hands and knees, already scrabbling to collect the papers scattered on the floor."
    "But as she falls, her skirt rides up her back, exposing her from the waist down."
    "Every motion she makes is visible as her buttocks wiggle under her panties."
    "Every inch of her curvy legs are on show, thighs calves and all."
    "The effort that she's putting into it means that her body is in almost constant motion."
    "And with a shape like that, there's a lot of her to get animated."
    show shiori fall open
    "Suddenly, Shiori stops moving and looks back over her shoulder at me."
    "Her face is bright red, eyes wide with embarrassment."
    "She grabs for the papers before her while desperately tugging her skirt back down."
    hide shiori
    show shiori close blush
    shiori.say "Oh, [hero.name], I'm so sorry!"
    shiori.say "Whatever must you think of me?"
    "And then scuttles off with as many of the papers as she can carry."
    hide shiori with easeoutleft
    "I try as best I can to sit down, struggling the whole time with the effect Shiori's had on the contents of my pants..."
    return

label shiori_event_04:
    show shiori
    "It's no great surprise to learn that Shiori's terrible when it comes to keeping her true intentions hidden."
    "She's a hopeless liar, and the more she tries to deny something, the more obvious it becomes as a result."
    "Right now she's been talking about nothing in particular for quite some time."
    "But she keeps on seeming to be building up to saying something, and then backing off at the last minute."
    "I'm getting tired of nodding and muttering yes and no at regular intervals."
    "And so, for better or worse, I decide to call her out."
    mike.say "Shiori, what's the matter, huh?"
    mike.say "What's bothering you?"
    show shiori surprised
    shiori.say "I...I don't know what you mean, [hero.name]!"
    show shiori happy
    shiori.say "Whatever gave you that impression?"
    "Shiori's smile is a little too forced, and she's clearly starting to blush."
    "All signs that I've hit the nail on the head."
    show shiori normal
    mike.say "Oh, come on, Shiori!"
    mike.say "You're babbling on and on about nothing."
    mike.say "And you're doing it at a hundred miles an hour too!"
    "By now, Shiori's cheeks have turned a bright shade of red."
    show shiori embarrassed blush
    shiori.say "Oh dear..."
    shiori.say "I'm not very good at this kind of thing!"
    "As if she needed to come right out and say as much!"
    "But there's that cute, vulnerable side of her coming out again."
    "The one that makes me want to rush in and save her from the big, bad world..."
    mike.say "It's okay, Shiori."
    mike.say "You don't need to worry about asking me something."
    "At this, Shiori's smile becomes more genuine, and she fixes me with those huge eyes of hers."
    "Clasping her hands together over her ample chest, she sighs, making everything rise and fall beneath her top."
    "God, she's so innocent and yet so damn sexy."
    "Sometimes I just want to eat her up!"
    "But then I remember that she's got something serious on her mind."
    "And so I try to banish such thoughts from my own, at least for the time being."
    "I return her smile, hoping that it'll be enough to encourage her to go on."
    shiori.say "You're right - of course you are."
    shiori.say "I do want to ask you for something...for a favour."
    shiori.say "But I'm worried that you'll say no...well, freak out and then say no!"
    "Well, that pretty much answers the question as to why she wouldn't just come right out and say it."
    "But I'm still in the dark as to just what the it in question actually is."
    "I'm not being cynical here, and I do genuinely want to help Shiori out if I can."
    mike.say "You won't know that until you ask the question, Shiori."
    mike.say "We're friends, aren't we?"
    show shiori happy
    "She nods at this."
    mike.say "Then go ahead and ask me."
    mike.say "Who knows - I might even say yes!"
    "Shiori shakes her head, still smiling and seemingly reassured by my efforts."
    show shiori normal
    shiori.say "Okay, [hero.name], okay...here goes nothing!"
    shiori.say "I...I was wondering...if you'd watch Kanta for me?"
    mike.say "Kanta's your son, right?"
    mike.say "You want me to watch your kid?!?"
    "I realise that I must have sounded far more shocked than I thought."
    show shiori surprised
    "As Shiori's smile fades and her eyes become instantly wide with worry."
    shiori.say "Oh no..."
    shiori.say "I knew you'd freak out!"
    menu:
        "Refuse":
            "Even after all the effort I went to reassuring her, Shiori was right about my reaction."
            "The very thought of being left in charge of someone else's kid sends shivers of terror down my spine."
            "But all the same, I can see that I still need to sugar-coat my answer."
            "Even if it's only for the sake of trying to keep myself on speaking terms with Shiori..."
            mike.say "No...no, Shiori - I'm not freaking out, I promise."
            "The moment that I say this, I can see that I've made a mistake."
            "Hope seems to blossom anew in Shiori's eyes."
            mike.say "But I'm sorry - the answer's still no."
            show shiori sad
            shiori.say "Please, [hero.name], won't you at least think about it?"
            shiori.say "I'm only asking because I'm desperate!"
            mike.say "I don't know the first thing about looking after a child, Shiori."
            mike.say "I'm sure he's a great kid and all..."
            mike.say "I just can't, okay?"
            $ shiori.love -= 10
            "Shiori sighs again, but this time it's in resigned disappointment."
            shiori.say "Okay...okay, [hero.name]."
            shiori.say "I guess I'll just have to figure something else out..."
            "The relief that I feel at being let off the hook from babysitting Shiori's kid doesn't last too long."
            "All too soon it's washed away by a deeper and more shameful sensation of guilt."
            show shiori normal
            "I can almost see the weight of the world pressing down on Shiori's shoulders as she tries to smile through it."
            "But I've made my decision, and that's that."
            "I can't let myself get guilted into becoming a child-minding service for Shiori's convenience."
            "She made the decisions that are blighting her life."
            "I can't let them do the same to mine too..."
            $ hero.cancel_event()
        "Accept":
            $ shiori.flags.babysitting = TemporaryFlag(True, "day")
            "I won't lie - the very idea of being left in charge of someone else's kid terrifies me."
            "But then it hits me that this isn't just anyone's kid - it's Shiori's kid!"
            "She's a friend that's asking me for help in her time of need."
            "Plus it'll also mean that she'll be grateful for me coming to the rescue..."
            "Not that I'm thinking of doing this out of anything other than the ties of friendship, you understand!"
            "And just like that I'm talking about the idea like I've already said yes."
            mike.say "No...no, Shiori - I'm not freaking out, I promise."
            mike.say "You just caught me off guard, that's all!"
            "The moment that I say this, hope seems to blossom anew in Shiori's eyes."
            shiori.say "You mean..."
            "It's almost as though she can't come right out and say it for fear of breaking the spell of the moment."
            show shiori happy
            mike.say "Yes, Shiori, I mean it."
            mike.say "I'll babysit Kanta for you, just this once."
            "Upon hearing this, Shiori instantly throws her arms around me and pulls me into a tight embrace."
            "I find myself torn between the shock of just how strong she is and the amazing sensation of her breasts squashed up against me."
            show shiori close happy
            shiori.say "Oh...thank you, thank you, thank you, [hero.name]!"
            shiori.say "You're the best, the absolute best!"
            shiori.say "I'll do anything to repay you...absolutely anything at all!"
            "I try as best I can to ignore the rather uncharitable way that last statement could be interpreted."
            mike.say "Okay...okay, Shiori!"
            mike.say "You're grateful...I get it!"
            mike.say "I can't watch Kanta for you if you break my ribs!"
            hide shiori
            show shiori blush
            "This makes Shiori release me from her death-grip, blushing once again."
            shiori.say "Oops...sorry, [hero.name]."
            shiori.say "You're just such a great guy for doing this."
            shiori.say "I guess I got a little carried away, huh?"
            "I nod and smile, still gasping for breath."
            shiori.say "Okay, right - I'll text you the day and the time."
            shiori.say "Then I'll drop Kanta round at your place on the actual night."
            "Then she gives me one of those smiles that makes me want to sweep her right off of her feet."
            shiori.say "Aww, the two guys in my life finally getting to spend some time together!"
            shiori.say "I don't know why, but I'm sure you're going to get on like a house on fire!"
    return

label shiori_event_05:
    if shiori.love.max < 100:
        $ shiori.love.max = 100
    show bg livingroom
    "By the time the actual night comes around for me to babysit Shiori's kid, it's all that's been on my mind for the whole day."
    "More than once I think about calling her up and pulling out, and a couple of times I even have the phone in my hand, about to press dial."
    "And then the memory of her ecstatic face and that intense hug she gave me always chooses that exact moment to resurface."
    "Sure, it's less than noble to admit that a large part of my motivation here is the thought that there might be more where that came from."
    "But Shiori still needs the favour, and it's not like she seems to dislike spending time with me, is it?"
    "For all I know, she could be using this as an opportunity to feel me out, see how well I handle spending time with her son."
    "Maybe if I make a good impression on the kid, he'll put in an equally good word for me with his mom?"
    play sound door_bell
    "It's then that I hear the sound of the doorbell ringing and glance at my phone."
    "Shit - how did it get to be that time already?!?"
    "I don't feel like I'm in the slightest bit ready for this!"
    "Hurrying to the front door, I take a deep breath and open it wide, smiling as I do so."
    scene bg house
    show shiori casual happy at right
    with wiperight
    shiori.say "Hey, [hero.name], I have someone here that wants to meet you!"
    "Still smiling, I follow Shiori's nodding head to one side of her and look down."
    "Fully expecting to be greeted with the sight of a child standing there, I frown when I see nothing at all."
    "I look back up at Shiori, who's still nodding away happily."
    "For a moment I begin to wonder if she's actually crazy and has made the kid up."
    "But then she seems to note my puzzled expression and looks down to her side as well."
    show shiori surprised
    shiori.say "Oh, sorry, [hero.name]."
    show shiori normal
    shiori.say "I should have said that he's a little shy around strangers!"
    "With that, she reaches behind her legs and takes hold of something, pulling it into view for the first time."
    "Suddenly I'm greeted with the sight of a rather small, skinny kid with a mop of black hair."
    "He looks up at me sullenly, still clinging to his mother's leg as if afraid she'll abandon him at any moment."
    shiori.say "[hero.name], this is Kanta."
    shiori.say "Kanta, this is [hero.name]."
    shiori.say "He's the man I was telling you about, remember?"
    shiori.say "The one that's going to look after you so mommy can go to her other work?"
    "Kanta nods dutifully, looking like he's had this information drilled into him already."
    mike.say "Hey, Kanta - your mom's told me so much about you."
    mike.say "It's great to finally meet the man himself!"
    "At the mere sound of my voice, the kid practically wraps himself around Shiori's legs."
    "She spends the next few minutes awkwardly trying to prise him loose and hand him over to me."
    "The whole time she keeps assuring me that everything will be fine and thanking me over and over again."
    shiori.say "I'll be back for him at the time we agreed."
    mike.say "Okay."
    shiori.say "Everything he needs is in the bag."
    mike.say "Got it."
    shiori.say "I put a couple of notes in there, about what he likes..."
    shiori.say "What he can and can't eat..."
    shiori.say "All of his allergies..."
    "For heaven's sake - is this a kid or the last specimen of an endangered species?"
    mike.say "Shiori...Shiori, it's just a couple of hours."
    mike.say "I'm sure we'll be fine."
    mike.say "Won't we, Kanta?"
    mike.say "Mommy doesn't need to worry about us, does she?"
    "For all of my efforts, all I get in way of reward from Kanta is more sullen silence."
    show shiori embarrassed
    shiori.say "Well, I have to run, or I'll be late for my...shift...yeah, that's it, my shift."
    shiori.say "I'll see my two favourite guys later!"
    hide shiori with dissolve
    "And with that, she's gone, leaving me standing on the porch with the kid."
    "Unsure of what to do next, I take hold of his hand and lead him indoors for want of a better plan."
    show bg livingroom with fade
    "He doesn't resist or try to run after Shiori, but I still get the feeling he could burst into tears at any given moment."
    "Closing the front door behind us means that I have to turn my back on the little guy for a moment."
    mike.say "So, Kanta - what fun stuff do you want to do until your mom gets back?"
    "The fact that I get no answer doesn't come as a big surprise."
    "I'm already beginning to wonder if the kid can speak at all."
    if not bree.hidden:
        bree.say "Well, well, well - who do we have here?"
        show bree sleep with dissolve
        "I turn around at the sound of [bree.name]'s voice to see her halfway down the stair, an indulgent smile plastered across her face."
        "She's wearing her pyjamas and looks like she's settling in for a night of slobbing in front of the TV."
        "As used to seeing my housemate dressed like this as I am, it's still a surprise to see that Kanta's gazing at her, as if spellbound."
        "And it's not the same sullen silence I've been getting either, as the kid's genuinely wide-eyed right now."
        mike.say "This is Kanta, my colleague's little boy."
        mike.say "Remember me telling you I agreed to watch him tonight?"
        "[bree.name] nods, still smiling as she comes the rest of the way down the stairs and into the hallway."
        bree.say "Sure I do."
        bree.say "It'll be nice to have another big, strong man about the house for a couple of hours!"
        "Kanta" "Hey, lady...are you a princess?"
        "I'm so taken aback by the fact that Kanta's finally spoken, that I almost miss what he actually said."
        show bree flirt blush
        "[bree.name], immediately flattered, laughs out loud."
        "She puts one hand on her chest and the other over her mouth, clearly charmed."
        bree.say "Aww...you think I'm a princess?"
        bree.say "That's so sweet!"
        "Kanta" "Are you one?"
        "Kanta" "Because princesses have hair that's blonde, like you do."
        "[bree.name] leans down to beam over the kid, nodding the whole time."
        "Kanta" "But princesses wear more clothes than you."
        "Kanta" "And my mommy says there's a word for ladies that don't wear enough clothes."
        "Kanta" "She calls them sl..."
        "Before [bree.name]'s expression can change from adoring to surprised and then to annoyed, I bundle Kanta into another room."
        hide bree
    if not sasha.hidden:
        show bg kitchen
        show sasha sleep
        with fade
        "My random choice of direction means that we end up in the kitchen, bursting in on Sasha as she eats her dinner at the table."
        "Unlike [bree.name], who at least started out doting on the kid, the sight of him almost seems to make Sasha's skin crawl."
        "As I walk him towards her a little way, I swear that she moves back steadily the whole time."
        mike.say "Sasha, meet Kanta."
        mike.say "He's going to be staying with us until his mom gets back from her evening shift."
        sasha.say "Eww...okay...whatever."
        show sasha annoyed
        sasha.say "Just keep him and his creepy little fingers out of my room!"
        "Kanta seems to have fallen back into silence since we came into the kitchen."
        "But I notice now that he's staring at Sasha with almost the same intensity as he did at [bree.name] a moment ago."
        sasha.say "Erm...[hero.name]..."
        sasha.say "Why is it staring at me like that?"
        "Unbidden by anything save for his own natural curiosity, Kanta cocks his head on one side, still studying Sasha."
        "Kanta" "Why are you that colour?"
        sasha.say "What...what does it mean?"
        "Kanta" "Why are you all white, like milk from mommy's pink pillows?"
        "Kanta" "Are you a vampire?"
        show sasha wtf
        sasha.say "Am I a what?!?"
        mike.say "Well, you are pale Sasha."
        mike.say "And you do sleep in the daytime, then come out mainly at night..."
        "Seeing that this meeting is quickly going the same way as the one with [bree.name], I scoop up the kid and hurry off once more."
        hide sasha
    show bg livingroom
    with fade
    if bree.love >= 150 and not bree.hidden and sasha.love >= 150 and not sasha.hidden:
        "Once we're alone in the living room, I empty the toys out of Kanta's bag and try to please him as best I can."
        "I recall every scene I can remember from movies and TV where someone has to babysit a kid."
        "But none of that seems to work, so instead I just watch the kid quietly."
        bree.say "Hey there!"
        sasha.say "You need some help?"
        show bree sleep at left
        show sasha sleep at right
        with dissolve
        "I look up to see [bree.name] and Sasha standing in the doorway, all smiles and waves for Kanta."
        mike.say "Like you wouldn't believe!"
        "[bree.name] and Sasha pad into the room, joining me so that there's now three people smiling down at Kanta."
        "He squints back up at us through narrowed eyes for a while, and then hands one of his toy cars to me."
        "One each follows for [bree.name] and Sasha, who take them without protest."
        "Grabbing one for himself, he starts to push it around on the carpet, making a revving sound the whole time."
        "Slowly and with infinite caution, I follow his lead, trailing his car with my own."
        "It takes perhaps another minute for [bree.name] and Sasha to join in too."
        "But soon enough we're having races around the floor, swerving wildly to avoid the rest of his junk as we do so."
        "I'd like to say that I let him win, but the truth is that Kanta beats all three of us more often than not."
        "Perhaps I can blame that on him being smaller and closer to the ground?"
        "We keep on playing the same game until Kanta starts to look tired, rubbing his eyes with the back of his hand."
        mike.say "Want to play on my console?"
        "I point to the TV."
        "Kanta half shrugs, and then shakes his head."
        "But all the same, I see he's still staring at the TV."
        show bree happy
        bree.say "Maybe you want to watch some kid's TV?"
        sasha.say "That's if you think you can handle something as high-brow as kid's TV, [hero.name]?"
        "Kanta actually nods at this, and then even gives a little smile."
        "I turn the TV on and flick onto the kid's channels that I don't think have ever been watched in the house before now."
        "And when I look back, Kanta's clambered onto the sofa and made himself comfortable."
        "He's already eyeballing the bright colours churning on the screen for his amusement."
        "But all the same he still pats the sofa to either side of him, which I choose to take as an invitation to sit."
        "The three of us occupy the space around Kanta, still a little scared to be sitting so close to him."
        "The kid's so quiet that it takes me a long time to realise that he's actually dozed off, leaning his head on my arm."
        show bree flirt blush
        bree.say "Aww, [hero.name], you're a natural!"
        show sasha happy
        sasha.say "Yeah, at this rate he'll be calling you 'Daddy' before you know it!"
        play sound door_bell
        "Just then I hear the sound of the doorbell, saving me from further mocking at the hands of my housemates."
        hide bree
        hide sasha
        show bg house
        show shiori casual
        with wiperight
        "Shiori looks dog-tired as she walks into the living room."
        "But her face lights up as soon as she sees us together on the sofa."
        shiori.say "How did you get him to sleep?!?"
        shiori.say "He never sleeps for anyone else...never!"
        mike.say "I don't know - we just played until he tired himself out, I guess."
        "As Shiori scoops him up from the sofa, Kanta stirs a little and smiles at her."
        "Kanta" "Hey mom..."
        "Kanta" "[hero.name] and I had fun..."
        "And with that, he falls back asleep, his head resting on her shoulder."
        "Shiori pauses on the doorstep, practically beaming despite the lateness of the hour."
        shiori.say "Thanks again, [hero.name]."
        shiori.say "You don't know just how important this was for me!"
        mike.say "Don't worry about it, Shiori."
        mike.say "I was happy to help."
        "She pauses, her mouth open."
        "And for a moment I think she's going to say something more."
        "But then she just smiles and kisses me briefly on the cheek."
        "And with that, she's gone."
        $ bree.love += 5
        $ sasha.love += 5
    elif bree.love >= 150 and not bree.hidden:
        "Once we're alone in the living room, I empty the toys out of Kanta's bag and try to please him as best I can."
        "I recall every scene I can remember from movies and TV where someone has to babysit a kid."
        "But none of that seems to work, so instead I just watch the kid quietly."
        bree.say "Hey, need some help?"
        show bree sleep with dissolve
        "I look up to see [bree.name] standing in the doorway."
        mike.say "Sure thing, [bree.name]."
        "[bree.name] pads into the room and joins me in smiling down at Kanta."
        "He squints at us through narrowed eyes for a while, and then hands one of his toy cars to me and a second to [bree.name]."
        "Grabbing one for himself, he starts to push it around on the carpet, making a revving sound the whole time."
        "Slowly and with infinite caution, we follow his lead, trailing his car with our own."
        "Soon enough we're having races around the floor, swerving wildly to avoid the rest of his junk as we do so."
        "I'd like to say that I let him win, but the truth is that Kanta beats [bree.name] and myself more often than not."
        "Perhaps I can blame that on him being smaller and closer to the ground than us?"
        "We keep on playing the same game until Kanta starts to look tired, rubbing his eyes with the back of his hand."
        mike.say "Want to play on my console?"
        "I point to the TV."
        "Kanta half shrugs, and then shakes his head."
        "But all the same, I see he's still staring at the TV."
        show bree happy
        bree.say "Maybe you want to watch some kid's TV?"
        "Kanta actually nods at this, and then even gives a little smile."
        "I turn the TV on and flick onto the kid's channels that I don't think have ever been watched in the house before now."
        "And when I look back, Kanta's clambered onto the sofa and made himself comfortable."
        "He's already eyeballing the bright colours churning on the screen for his amusement."
        "But all the same he still pats the sofa to either side of him."
        "I look at [bree.name] and she shrugs in response as we sit down by Kanta."
        "The kid's so quiet that it takes me a long time to realise that he's actually dozed off, leaning his head on my arm."
        sasha.say "Huh, the little bastard burned himself out!"
        show bree at right
        show sasha sleep at left
        with dissolve
        "[bree.name] and I glance up to see Sasha leaning around the doorway."
        "She glances at the TV, still showing an endless loop of kid's shows."
        sasha.say "I'm surprised you're not out of it too, [hero.name]."
        sasha.say "These cartoons are way more highbrow than the stuff you're normally into watching!"
        play sound door_bell
        "Just then I hear the sound of the doorbell, saving me from further mocking at the hands of my housemates."
        hide bree
        hide sasha
        show bg house
        show shiori casual
        with wiperight
        "Shiori looks dog-tired as she walks into the living room."
        "But her face lights up as soon as she sees us together on the sofa."
        shiori.say "How did you get him to sleep?!?"
        shiori.say "He never sleeps for anyone else...never!"
        mike.say "I don't know - we just played until he tired himself out, I guess."
        "As Shiori scoops him up from the sofa, Kanta stirs a little and smiles at her."
        "Kanta" "Hey mom..."
        "Kanta" "[hero.name] and I had fun..."
        "And with that, he falls back asleep, his head resting on her shoulder."
        "Shiori pauses on the doorstep, practically beaming despite the lateness of the hour."
        shiori.say "Thanks again, [hero.name]."
        shiori.say "You don't know just how important this was for me!"
        mike.say "Don't worry about it, Shiori."
        mike.say "I was happy to help."
        "She pauses, her mouth open."
        "And for a moment I think she's going to say something more."
        "But then she just smiles and kisses me briefly on the cheek."
        "And with that, she's gone."
        $ bree.love += 5
    elif sasha.love >= 150 and not sasha.hidden:
        "Once we're alone in the living room, I empty the toys out of Kanta's bag and try to please him as best I can."
        "I recall every scene I can remember from movies and TV where someone has to babysit a kid."
        "But none of that seems to work, so instead I just watch the kid quietly."
        sasha.say "Hey, need some help?"
        show sasha sleep with dissolve
        "I look up to see Sasha standing in the doorway."
        mike.say "Sure thing, Sasha."
        mike.say "I...I just didn't think this was your kind of thing?"
        "Sasha pads into the room and joins me in smiling down at Kanta."
        sasha.say "Nah, he just kind of took me by surprise before."
        sasha.say "Kind of a cute little bastard, isn't he?"
        "Kanta squints at us through narrowed eyes for a while, and then hands one of his toy cars to me and another to Sasha."
        "Grabbing one for himself, he starts to push it around on the carpet, making a revving sound the whole time."
        "Slowly and with infinite caution, we follow his lead, trailing his car with our own."
        "Soon enough we're having races around the floor, swerving wildly to avoid the rest of his junk as we do so."
        "I'd like to say that I let him win, but the truth is that Kanta beats Sasha and me more often than not."
        "Perhaps I can blame that on him being smaller and closer to the ground than us?"
        "We keep on playing the same game until Kanta starts to look tired, rubbing his eyes with the back of his hand."
        mike.say "Want to play on my console?"
        "I point to the TV."
        "Kanta half shrugs, and then shakes his head."
        "But all the same, I see he's still staring at the TV."
        show sasha happy
        sasha.say "Maybe you want to watch some kid's TV?"
        "Kanta actually nods at this, and then even gives a little smile."
        "I turn the TV on and flick onto the kid's channels that I don't think have ever been watched in the house before now."
        "And when I look back, Kanta's clambered onto the sofa and made himself comfortable."
        "He's already eyeballing the bright colours churning on the screen for his amusement."
        "But all the same he still pats the sofa to either side of him."
        "I look at Sasha and she shrugs in response as we sit down by Kanta."
        "The kid's so quiet that it takes me a long time to realise that he's actually dozed off, leaning his head on my arm."
        bree.say "Aww!"
        show sasha at left
        show bree at right
        with dissolve
        "I look up to see [bree.name] standing in the doorway, hands clasped under her chin and eyes wide like something out of a cutesy anime."
        bree.say "The little angel burned himself out!"
        "She glances at the TV, still showing an endless loop of kid's shows."
        bree.say "I'm surprised you're not out of it too, [hero.name]."
        bree.say "These cartoons are way more highbrow than the stuff you're normally into watching!"
        play sound door_bell
        "Just then I hear the sound of the doorbell, saving me from further mocking at the hands of my housemates."
        hide bree
        hide sasha
        show bg house
        show shiori casual
        with wiperight
        "Shiori looks dog-tired as she walks into the living room."
        "But her face lights up as soon as she sees us together on the sofa."
        show shiori surprised
        shiori.say "How did you get him to sleep?!?"
        shiori.say "He never sleeps for anyone else...never!"
        mike.say "I don't know - we just played until he tired himself out, I guess."
        show shiori normal
        "As Shiori scoops him up from the sofa, Kanta stirs a little and smiles at her."
        "Kanta" "Hey mom..."
        "Kanta" "[hero.name] and I had fun..."
        "And with that, he falls back asleep, his head resting on her shoulder."
        "Shiori pauses on the doorstep, practically beaming despite the lateness of the hour."
        show shiori happy
        shiori.say "Thanks again, [hero.name]."
        shiori.say "You don't know just how important this was for me!"
        mike.say "Don't worry about it, Shiori."
        mike.say "I was happy to help."
        show shiori normal
        "She pauses, her mouth open."
        "And for a moment I think she's going to say something more."
        "But then she just smiles and kisses me briefly on the cheek."
        "And with that, she's gone."
        $ sasha.love += 5
    elif hero.energy < 5:
        "Once we're alone in the living room, I empty the toys out of Kanta's bag and try to please him as best I can."
        "I recall every scene I can remember from movies and TV where someone has to babysit a kid."
        "But no matter what I try, nothing seems to be able to get through to the kid."
        "It's not like he breaks down and cries for his mother the whole time."
        "But he stays silent and in a huff, just letting me exhaust myself for no reward."
        "Soon enough I relent and just sit him in front of a kid's channel on the TV."
        "That seems to placate him somewhat, letting me slump down on the sofa where I can still see him."
        "I'm tired out, but determined not to fall asleep while he's in my care."
        "I tell myself that I'll just close my eyes and keep on listening for any sound of change..."
        show bg black with dissolve
        "That sound turns out to be screaming, making me sit bolt upright, looking left and right in utter confusion."
        show bg livingroom
        if not bree.hidden and not sasha.hidden:
            show bree sleep at left
            show sasha sleep at right
        with dissolve
        if not bree.hidden and not sasha.hidden:
            "I'm surprised to see [bree.name] and Sasha, the former nursing Kanta as he wails and the latter glaring at me in disbelief."
        mike.say "Wha...what happened?"
        if not bree.hidden and not sasha.hidden:
            sasha.say "You fell asleep, [hero.name]!"
            bree.say "The poor little man must have fallen and banged his head on the TV!"
        mike.say "Oh shit, of shit, oh shit!"
        mike.say "I just closed my eyes for a couple of seconds, that's all!"
        play sound door_bell
        "Right on cue, I hear the sound of the doorbell ringing."
        if not bree.hidden and not sasha.hidden:
            hide bree
            hide sasha
        show bg house
        show shiori casual
        with wiperight
        "The very second that she's in the house, Shiori hears Kanta's wailing and flies to him."
        if not bree.hidden and not sasha.hidden:
            "She almost sends [bree.name] flying as she snatches her son from the other girl's arms."
        mike.say "I...I don't know what happened, Shiori!"
        mike.say "My eyes were only off of him for a second..."
        if not bree.hidden and not sasha.hidden:
            "I catch [bree.name] and Sasha glaring at me in disbelief as I tell the lie."
            "But they stay quiet all the same, rolling their eyes and shaking their heads in disapproval."
        show shiori angry
        shiori.say "That's the thing about kid's, [hero.name] - you CAN'T take your eyes off them, even for a second!"
        "Almost as soon as the harsh words are out of her mouth, Shiori shakes her head as if she regrets them."
        "She examines Kanta's head and lets out an extremely heavy sigh, like she's weary to the very bone."
        show shiori normal
        shiori.say "It's okay - he'll have a lump in the morning, but no damage done."
        show shiori sad
        shiori.say "This is my fault really."
        shiori.say "After all, I was the one that left him with someone who has no experience with kids."
        shiori.say "Some mother I am..."
        mike.say "Shiori...I..."
        show shiori normal
        "Shiori holds a hand up to stop me from saying anything more."
        shiori.say "It's getting real late, [hero.name], and I'm tired."
        shiori.say "I don't really know what I'm saying any more..."
        mike.say "Ah...okay, Shiori."
        mike.say "I guess I'll see you at work tomorrow?"
        "She nods and smiles back at me over her shoulder as she carries Kanta out of the house."
        "And I don't think I've ever seen a person look so tired as she does in that moment."
        $ shiori.love -= 10
    else:
        "Once we're alone in the living room, I empty the toys out of Kanta's bag and try to please him as best I can."
        "I recall every scene I can remember from movies and TV where someone has to babysit a kid."
        "But none of that seems to work, so instead I just watch the kid quietly."
        "He squints at me through narrowed eyes for a while, and then hands one of his toy cars to me."
        "Grabbing one for himself, he starts to push it around on the carpet, making a revving sound the whole time."
        "Slowly and with infinite caution, I follow his lead, trailing his car with my own."
        "Soon enough we're having races around the floor, swerving wildly to avoid the rest of his junk as we do so."
        "I'd like to say that I let him win, but the truth is that Kanta beats me more often than not."
        "Perhaps I can blame that on him being smaller and closer to the ground than me?"
        "We keep on playing the same game until Kanta starts to look tired, rubbing his eyes with the back of his hand."
        mike.say "Want to play on my console?"
        "I point to the TV."
        "Kanta half shrugs, and then shakes his head."
        "But all the same, I see he's still staring at the TV."
        mike.say "Maybe you want to watch some kid's TV?"
        "Kanta actually nods at this, and then even gives a little smile."
        "I turn the TV on and flick onto the kid's channels that I don't think have ever been watched in the house before now."
        "And when I look back, Kanta's clambered onto the sofa and made himself comfortable."
        "He's already eyeballing the bright colours churning on the screen for his amusement."
        "But all the same he still pats the sofa beside him, which I choose to take as an invitation to sit."
        "The kid's so quiet that it takes me a long time to realise that he's actually dozed off, leaning his head on my arm."
        if not bree.hidden and not sasha.hidden:
            bree.say "Aww!"
            bree.say "Sasha, you have to come see this!"
            show bree sleep blush at left with dissolve
            "I look up to see [bree.name] standing in the doorway, hands clasped under her chin and eyes wide like something out of a cutesy anime."
            "Sasha joins her a moment later, snorting with laughter as she sees what's gotten her housemate so worked up."
            show sasha sleep happy at right with dissolve
            sasha.say "Huh, the little bastard burned himself out!"
            "She glances at the TV, still showing an endless loop of kid's shows."
            sasha.say "I'm surprised you're not out of it too, [hero.name]."
            sasha.say "These cartoons are way more highbrow than the stuff you're normally into watching!"
        play sound door_bell
        "Just then I hear the sound of the doorbell, saving me from further mocking at the hands of my housemates."
        if not bree.hidden and not sasha.hidden:
            hide bree
            hide sasha
        show bg house
        show shiori casual
        with wiperight
        "Shiori looks dog-tired as she walks into the living room."
        "But her face lights up as soon as she sees us together on the sofa."
        show shiori surprised
        shiori.say "How did you get him to sleep?!?"
        shiori.say "He never sleeps for anyone else...never!"
        mike.say "I don't know - we just played until he tired himself out, I guess."
        show shiori normal
        "As Shiori scoops him up from the sofa, Kanta stirs a little and smiles at her."
        "Kanta" "Hey mom..."
        "Kanta" "[hero.name] and I had fun..."
        "And with that, he falls back asleep, his head resting on her shoulder."
        "Shiori pauses on the doorstep, practically beaming despite the lateness of the hour."
        show shiori happy
        shiori.say "Thanks again, [hero.name]."
        shiori.say "You don't know just how important this was for me!"
        mike.say "Don't worry about it, Shiori."
        mike.say "I was happy to help."
        show shiori normal
        "She pauses, her mouth open."
        "And for a moment I think she's going to say something more."
        "But then she just smiles and kisses me briefly on the cheek."
        "And with that, she's gone."
        $ shiori.love += 5
    return

label shiori_event_06:
    if shiori.love.max < 110:
        $ shiori.love.max = 110
    "Working in an office, you get into a routine pretty quickly and most often without noticing it."
    "With me, it usually revolves around my daily schedule of coffee, essential for keeping me awake and alert."
    "I'd get off my arse and make my own, but Shiori's kind of claimed the role of coffee maker recently."
    "All it usually involves is her putting the cup on my desk and cheerily letting me know it's there."
    "If I look up at all, it's just to make some vague sound that passes as a thanks and reach for the cup."
    "But today I hear a distinctly different sound approaching at coffee time, and so I look up with interest."
    show shiori at top_left with easeinleft
    "The sight that greets me is Shiori, tottering into my office while carrying a tray before her."
    show shiori at left4 with ease
    "Balanced precariously on said tray is a cafetiere of coffee, small jug of milk, sugar cubes along with a cup and saucer."
    mike.say "Erm, Shiori...what's all this in aid of?"
    show shiori at center with ease
    "Shiori beams at me over the tray, almost dropping it with the effort."
    shiori.say "I noticed that you're always drinking that instant coffee, [hero.name]."
    show shiori happy
    shiori.say "So I thought you might like a treat - some REAL COFFEE!"
    mike.say "Oh, I see."
    mike.say "That's very thoughtful, Shiori."
    mike.say "But you shouldn't have..."
    show shiori normal
    "I don't get to finish what I was saying, as Shiori shakes her head to dismiss it."
    "But this also means that she closes her eyes for a moment and stops looking where she's going."
    hide shiori with easeoutbottom
    play sound body_fall
    pause 0.3
    with vpunch
    "A moment later, she seems to trip over something unseen, going face-first onto the floor."


    with hpunch
    "The contents of the tray are flung against the wall, most of the breakable items shattering on impact."
    mike.say "Shiori - are you okay?!?"
    show shiori fall nopanties closed coffee with vpunch
    "I'm up and around my desk in a matter of seconds, worried that she might have hurt herself in the fall."
    "But when I get to her, Shiori's unhurt and already scrabbling to clean up the mess she's made."
    mike.say "Shiori..."
    "I stop dead, seeing that her skirt has ridden up as she fell, exposing her from the waist down."
    "Shiori doesn't seem to have noticed at all, as she crawls around on all fours in front of me."
    "Though what's really stopped me in my tracks is the fact that I can clearly see she's not wearing a scrap of underwear."
    show shiori fall open
    shiori.say "Oh god, I'm so clumsy!"
    shiori.say "I can't do anything right!"
    shiori.say "You must be so angry with me..."
    "To be honest, I hardly hear a single word that Shiori's saying."
    "Instead I'm hypnotised by the sight of her naked backside as she shuffles around on her hands and knees."
    "It's only when she finally looks over her shoulder at me and then gasps in surprise that she notices she's exposed."
    hide shiori with fade
    "Shiori makes a yelping noise, and then yanks down her skirt as she flees from my sight."
    "But soon afterwards I begin to wonder about the whole incident."
    "What are the chances of her deciding to change my morning coffee routine?"
    "As well as doing it on the same day she either forgot to wear panties or go commando?"
    "And on top of that - why would she choose to go commando at all?"
    return

label shiori_has_had_sex:
    if shiori.love.max < 120:
        $ shiori.love.max = 120
    return



label shiori_scold_2:
    "I decide to return to my office to get some work done."
    mike.say "Dammit! What the hell is this!"
    "I stomp out of my office and scan over the room."
    mike.say "Shiori!"
    show shiori with moveinleft
    "Shiori comes running in, panting and bending over, her hands on her knees."
    shiori.say "I'm sorry... [hero.name]. What's the matter?"
    "I hold up the package of pens, 20 count, all of them black."
    show fx question
    shiori.say "I... I don't understand. I told inventory about your pen shortage?"
    shiori.say "Is something the matter?"
    "I take a deep breath, trying to calm down."
    mike.say "Alright, first of all, the contracts we deal with have to be done in blue ink, Shiori."
    "I shove the package to her."
    "She fumbles a moment and holds it between her hands, pressing the packet up against her breasts."
    shiori.say "Oh, but, [hero.name], that's okay. Because the memo I sent you said we were allowing black pens now, and..."
    "She trails off as I stare death threats into her eyes. I didn't need to say it."
    "I really didn't WANT to say it, but here I am, anyway."
    mike.say "Shiori... what memo...?"
    show shiori embarrassed
    "She buries her face in the pens, trembling at the thought."
    shiori.say "O... oh, did I... did I forget to send it to you?"
    mike.say "Yes, yes you did."
    "She sighs, lowering the pens. For a split second, I can see a little grin on her face."
    "Oh, no, is this what she was planning? I sigh and I take the pens from her."
    mike.say "And another thing... I said I needed 10 pens, not 10 CRATES of pens! Just look at this. It's covering my desk!"
    shiori.say "Oh, my, sir, that's a lot... a lot of pens! I guess I don't listen very well, do I?"
    "I lean in, narrowing my gaze at her."
    "She stares up at me with a dumb little smile as she leans back, stumbling a moment until she hits a desk behind her with a squeak."
    mike.say "No, apparently you don't listen very well."
    show shiori blush
    shiori.say "Are you going to spank me now, sir?"
    "I slowly move my hand up towards her, hovering by her thigh a moment."
    mike.say "Hm... well, you do deserve a punishment."
    "She squeaks, shaking as I lean in closer to her, a smile spreading upon my lips."
    shiori.say "I've... I've been such a bad girl, boss..."
    mike.say "Yes, yes you have..."
    "I say, chuckling softly to her."
    shiori.say "I really should be punished... and there's no one here to stop you."
    mike.say "No, there isn't..."
    "I agree."
    shiori.say "S... so, how are you going to do it?"
    "She asks, her eyes watering, getting wide."
    "She bites her lip as she looks to me with expectant glee."
    "I grab the pens and yank them from her."
    mike.say "First of all, I'm going to have to put these back in their box. Then, I'm going to have to ask you to take these to the post office."
    shiori.say "W... what?"
    mike.say "And then after that... you can get me a coffee. You're really pushing your luck."
    mike.say "Next time, your punishment WILL be severe."
    "She grumbles, but I catch a quick flick of her tongue as she licks her lips."
    hide shiori with easeoutleft
    "Oh yes, this could be quite fun to keep up."
    $ shiori.love += 5
    return

label shiori_scold_3:
    "As I arrive at my office, there sits a large coffee cup from an expensive store with my name spelled wrong upon it."
    "I give it a quick sip, only to spit it back out immediately."
    mike.say "What the hell? Shiori!?"
    show shiori at top_left with moveinleft
    "Shiori peeks into my office, hiding her face behind the door."
    shiori.say "Y... yes, [hero.name]?"
    "I clap my hands together and breathe deeply through my nose."
    "Closing my eyes, I refocus myself a moment before I push my hands downward."
    "Once I open my eyes again, I see her, and I just ask her a simple question."
    mike.say "Why... does my coffee... have salt?"
    shiori.say "Oh, that?"
    show shiori at center with ease
    "Shiori taps her cheek, looking up and away, putting on an almost ditzy face."
    shiori.say "I have no idea how that could have happened."
    shiori.say "I mean, I forgot to get you sugar at the store, and I know you asked for sugar last night, so... I just went to the break room and poured some in and-"
    "She gasps, slapping her cheeks."
    show shiori embarrassed
    shiori.say "Oh no, [hero.name], you don't suppose I put salt in there by mistake?"
    shiori.say "Oh, I'm so terribly sorry! I can't believe I did that. Please, oh please, oh please don't reprimand me!"
    menu:
        "Spank her":
            $ shiori.flags.start_spanking = True
            $ shiori.flags.spank_counter += 1
            "I take the coffee cup and slam it on a cabinet, leaving my desk clear. I then point to it, and nod."
            "She gasps, but frowns, shaking her head."
            shiori.say "Oh, no, sir! Please, don't do this! I'll do better, I promise!"
            "I just point."
            show shiori spanking
            "She gulps, trembling as she bends herself over the desk, pressing her ample breasts up against the desktop."
            shiori.say "Oh, this is so embarrassing. I can't believe I'm being so degraded!"
            mike.say "You should have known that sugar and salt are in two different containers in the break room."
            shiori.say "I know, I know! I was just so worried!"
            mike.say "Well, now, you have to pay the price."
            show shiori spanking hand
            "I lift my hand upwards."
            "She closes her eyes, burrowing her head down against the desk."
            "I wiggle my fingers a moment, holding my arm in the air."
            "She whimpers in preparation."
            show shiori spanking blur
            play sound spank
            with hpunch
            "I then throw my arm down, smacking her right on her skirt-covered rump."
            show shiori spanking done
            "She gasps, tilting her head back."
            shiori.say "Oooh, I'm sorry, sir! Please, don't do it again!"
            hide shiori
            show shiori blush
            "I grab my coffee and then I walk out towards the hallway."
            mike.say "No, I think you've learned your lesson. I need to get myself a coffee."
            mike.say "You go and keep up your work, and don't fail me again."
            hide shiori
            $ shiori.love += 5
            "I toss the cup in the trash and continue on my way out, leaving her to grumble as I leave her wanting for more."
            "This game we're playing... it's actually getting to be kinda fun."
            "Except... maybe for the salty drinks. Gah!"
        "Let it go":
            mike.say "You really, really have to learn how to do the basic job. If you can't get the simplest things right, I'll just have to find a new secretary."
            shiori.say "Oh no sir, please don't say that! I'll do better, I promise!"
            mike.say "Prove it."
            show shiori sad
            "Shiori looks at me, with tears in her eyes."
            shiori.say "You can punish me, do anything, but please don't fire me!"
            mike.say "Fine, but do better next time! Or else!"
            "I toss my cup in the trash and head to the break room. Because after this, I need a cup of coffee in a bad way."
    return

label shiori_scold_4:
    "I grumble at my desk and turn off my computer."
    "Tapping one of my bulk-ordered black pens on my desk, I can't help but feel a bit anxious."
    "I haven't gotten a call I wanted in a few hours, and they said they'd call today."
    "I can't get anything done without them, and there's nothing else to do around here until they do."
    "I scoot out of my desk and peer out towards Shiori's desk."
    "She's on her phone... it seems like a pretty slow day, too."
    "Sighing, I lean up against the door and I call out to her."
    mike.say "Shiori, get in my office."
    show shiori
    "Surprised, she immediately hops up, following me inside."
    shiori.say "W... what did I do this time, [hero.name]."
    mike.say "It's more like what you didn't do... Shiori, did you remember to call Miss Jefferson back this morning?"
    "She blinks a moment, and she tilts her head."
    shiori.say "Miss... Miss Jefferson...?"
    mike.say "Oh, come on, Shiori! You're usually so good, but when you screw up, you really screw up. How could you forget Miss Jefferson!"
    shiori.say "I honestly have no idea who you're talking about!"
    "She whines."
    menu:
        "Spank her" if shiori.flags.start_spanking:
            $ shiori.flags.spank_counter += 1
            mike.say "Well, if you're so forgetful, I think I'll have to give you something that'll be hard to forget. Bend over."
            "She stares at me for a moment, only to then shake her head as she walks on over to the desk."
            show shiori spanking
            shiori.say "Oh, [hero.name], you're so mean! I can't believe I take this abuse from you."
            mike.say "Yeah, well, if you don't learn, you're going to have to keep taking it... and I'm going to have to make it more memorable this time."
            show shiori spanking botup
            "I flip up her skirt and she grips my desk, gasping at the rush of air."
            "I lean in, giving the cheek a bit of a squeeze."
            mike.say "Right. Now, that this is out of the way, I can actually get to that skin underneath."
            "Maybe I should..."
            "I tease at the hem of her panties, and she groans, but I pull away."
            show shiori spanking botup hand
            mike.say "Hey, who said you could enjoy your punishment, hm? You want to like this shit?"
            show shiori spanking botup blur
            play sound spank
            with hpunch
            "I smack her on one cheek, leaving a red mark on her rump."
            show shiori spanking botup done pain
            "She gasps, shaking underneath. She holds her mouth shut so she doesn't scream too loud that others could hear."
            show shiori spanking botup hand normal
            mike.say "Good girl, you're learning not to be too loud."
            mike.say "You'll need it."
            show shiori spanking botup blur
            play sound spank
            with hpunch
            "Without warning, I smack her other cheek, and she screams louder into her hands, huffing after I'm done."
            show shiori spanking botup -blur pain
            "I stand up and I grab my coat."
            show shiori spanking botup normal
            mike.say "I'm going to go out for a walk a bit. Hold my calls until I get back, and try to remember Miss Jackson."
            "As I step out of the room, she gasps and says."
            shiori.say "Hey wait, you said it was 'Jefferson' earlier. Boss, are you... did you... YOU HAD ME WORRIED!"
            "I snicker as I walk out the door."
            "Two can play at her game, indeed."
            $ shiori.love += 5
        "Tell her to do her job":
            mike.say "Oh for fuck's sake, Shiori. Go, get on the phone, do your damn job."
            "Shiori nearly shrieks."
            show shiori sad
            shiori.say "Please don't fire me, [hero.name]!"
            mike.say "I won't if you go and do your job. {b}Right{/b}! {b}Now{/b}!"
            hide shiori with easeoutleft
            "Shiori practically runs to her desk and picks up the phone to do her job."
            "I don't know how much longer I can take this."
    return

label shiori_scold_5:
    show shiori angry with easeinleft
    "Shiori barges into my office, the smuggest of smug looks upon her face as she stands there, hands folded over her chest."
    "I stare up at her, confused as to what she's doing."
    mike.say "Can I... help you, Shiori...?"
    shiori.say "I'm onto you, you know."
    "She says, sass starting to drip from every syllable."
    mike.say "Oh, really...? And just what am I up to?"
    show shiori annoyed
    shiori.say "I remember when you made up Miss Jackson and Miss Jefferson, trying to make me think I was forgetting someone important."
    shiori.say "Well, guess what? I figured out you actually hired some girl to pretend to be one of them and call with an 'urgent request'."
    "I lower my coffee cup."
    mike.say "W... what?"
    shiori.say "Oh yeah, she said she needed to speak with you right away."
    shiori.say "Well, you know what I did? I told her she could talk to Miss Lincoln if she wanted to make a complaint."
    "Rubbing my eyes, I put my coffee aside and ask."
    mike.say "Shiori... was that... Jenna Jefferson...?"
    show shiori normal
    "She nods."
    shiori.say "Yup! That's the one. That's the plant you put in there to punk me."
    shiori.say "Well, you know what? No more teasing from you, [hero.name]. I got you this time, hehe!"
    "I push up from the desk and point to it."
    mike.say "No, you just hung up on an actual client. It's come to my attention that you're just wanting to be spanked."
    mike.say "Maybe now, I can cure you of that disease by giving it to you, very, very hard."
    show shiori embarrassed
    "She gulps, shuddering."
    shiori.say "Oh, I... is that... so? Look, I'm really sorry and..."
    $ shiori.flags.spank_counter += 1
    hide shiori
    show shiori spanking
    "I point to my desk, and she sighs, sliding over it."
    show shiori spanking botpantiesdown
    "I grab her skirt, hiking it up and showing off her panties."
    "I then trace my fingers down along the white fabric before I gripped at them and tugged them down, exposing her before me."
    show shiori spanking botpantiesdown hand
    mike.say "A bare butt... that's the only way to cure you."
    show shiori spanking botpantiesdown done mark pain foot
    play sound spank
    with hpunch
    "I slap her square in the center, lower than normal, getting close to her exposed pussy."
    hide shiori
    show shiori spanking botpantiesdown hand normal
    "She yelps, her tongue rolling out from that hit."
    show shiori spanking botpantiesdown done mark pain
    play sound spank
    with hpunch
    shiori.say "Aaaagh! Boss, I'll do better, I promise!"
    hide shiori
    show shiori spanking botpantiesdown hand normal
    mike.say "No more games from now on!"
    show shiori spanking botpantiesdown blur
    play sound spank
    with hpunch
    "I said, slapping her on one cheek, and then the other."
    show shiori spanking botpantiesdown done mark pain
    "She grips the desk, shuddering violently as she groans out from my slaps."
    hide shiori
    show shiori spanking botpantiesdown hand normal
    shiori.say "B... Boooosss!"
    show shiori spanking botpantiesdown blur
    play sound spank
    with hpunch
    mike.say "From now on, if you want to be punished, you do a GOOD job. That's because you want this so much."
    show shiori spanking botpantiesdown done mark pain foot
    shiori.say "Aaah, r-right boss!"
    hide shiori
    show shiori spanking botpantiesdown hand normal
    mike.say "Screw up in your job for real again, and I'll really get upset, and that's a promise."
    show shiori spanking botpantiesdown blur
    play sound spank
    with hpunch
    play sound spank
    with hpunch
    play sound spank
    with hpunch
    "I give her a triple slap."
    show shiori spanking botpantiesdown done mark pain foot
    "One cheek, the other, and then in between."
    hide shiori
    show shiori spanking botpantiesdown e pain
    "She pants, leaning over the desk, groaning as her butt shines red with my hand prints."
    show shiori spanking botpantiesdown e normal
    mike.say "Now, then... I need to call Miss Jefferson back and apologize for the incompetence of my staff. We'll talk about this later. Got it?"
    shiori.say "Uh... huh..."
    "She sighs, closing her eyes and smiling."
    mike.say "Dang, it's a message."
    mike.say "Shiori, you can take care of this, but... leave your panties here when you go back to your desk."
    hide shiori
    show shiori blush
    "She squeaks and pushes herself up, pulling down her skirt and running off towards the room."
    hide shiori with easeoutleft
    "Yes, I believe its game over... now the real fun begins."
    $ shiori.love += 5
    return

label shiori_coffee_2:
    show shiori
    "When you're messing around with someone in the workplace, things can often get a little complicated."
    "For example, you tend to start speaking in code for the sake of keeping what you get up to from being overheard."
    "The problem comes when you realise that almost every term and phrase that you could use in the course of the working day now also means something else entirely."
    "So when your secret paramour comes into your office and asks you to help them find a lost file in the basement archives."
    "How are you supposed to know if you're being invited for a quick fuck out of the sight of your colleagues."
    "Or if you actually are being drafted in to dig out a particularly elusive client file?"
    "Trust me, if you're not careful, that kind of confusion can lead to serious trouble!"
    "I get reminded of this conundrum when I hear the sound of someone bustling into my office without bothering to knock."
    "Not that the person in question failing to knock bothers me at all, it just means I can narrow down who it might be without needing to look up."
    if Person.is_not_hidden("lavish"):
        "It can't be Lavish, as she's young and paranoid about making a bad impression, so she always knocks."
    if Person.is_not_hidden("aletta"):
        "It can't be Aletta, because in the very few seconds after the person came in, they didn't start making demands of me."
    if Person.is_not_hidden("audrey"):
        "And it can't be Audrey, as they're not leaning over my desk or making a show of themselves in any way."
    "Which means it can only really be one other person."
    show shiori
    mike.say "Good morning, Shiori."
    "I don't bother to look up as I greet her, enjoying the little squeak of surprise she lets out."
    shiori.say "Good...good morning, [hero.name]!"
    "I make a point of never explaining how I can work out that it's her, no matter how many times I'm able to do so."
    "It keeps Shiori just that little bit in awe of me and off her guard."
    mike.say "Was there something I can do for you, Shiori?"
    mike.say "Or is this just a social visit?"
    "When there's no answer save for some nervous muttering, I finally decide to look up from my work."
    show shiori embarrassed
    "I see Shiori, looking as embarrassed and awkward as usual, a tray of hot drinks clutched in her hands."
    "I raise my eyebrows, giving her a clear signal that I want her to explain herself."
    "Even though it's already pretty obvious what she's here for."
    shiori.say "Erm...I...I wondered if you'd like your coffee, [hero.name]?"
    "I raise one eyebrow now, making my expression quizzical."
    mike.say "Of course I would, Shiori."
    mike.say "You know that I like a coffee around this time in the morning and you also know just how I take it."
    mike.say "So would you mind explaining to me why today you feel the need to come in here and ask?"
    show shiori blush
    "Shiori gives me what I think is supposed to be a nonchalant shrug and a smile, which ends up looking more than a little panicked and paranoid."
    call shiori_coffee_choice from _call_shiori_coffee_choice
    "Left alone, I pick up my coffee and blow the steam off of the top before taking a long and much-needed mouthful."
    "I don't get back to work immediately, as Shiori and her strange habits are still uppermost in my mind."
    "All of this over my choice of milk!"
    "I'm not sure if I should feel flattered or terrified!"
    return

label shiori_coffee_choice:
    shiori.say "Well...I was thinking...I know that you have milk in your coffee."
    "I nod as she gingerly puts the tray down on the desk in front of me."
    show shiori normal
    shiori.say "But I wondered if...for a change...you might want to choose the kind of milk I put into it today?"
    "Now I see that there are two small jugs on the tray, as well as the cups of steaming, black coffee."
    mike.say "I am going to want milk, Shiori - so what have you got there?"
    show shiori happy
    "Shiori's mood recovers a little at my interest, and she smiles as she points to each jug in turn."
    shiori.say "Ah...okay...you normally have fat-free, but I also have half-fat, and..."
    "I can hear her pause and take in a deep breath before she continues."
    show shiori blush
    shiori.say "You could have...full-fat...if that's what you'd like?"
    "Her hands rise up and out of view, and my eyes instinctively follow them."
    "Shiori clasps one hand on either side of her breasts and slowly pushes them together so that they bulge outwards, almost popping out of her blouse."
    "Wait a minute - does she actually mean..."
    "Shiori keeps on leaning further forwards until her heavy chest is almost hanging over the coffee cups on the tray."
    if shiori.flags.topless:
        "She looks at me, clearly waiting for an answer."
    else:
        "She looks at me, clearly waiting for an answer, her breasts in increasing danger of falling out of her top."
    menu:
        "No":
            $ shiori.love -= 5
            "I can feel my stomach begin to churn at the very thought of what Shiori's suggesting."
            "An unconscious urge makes me cough, and I can taste the hint of bile at the back of my throat."
            show shiori sad
            mike.say "You know what, Shiori - I think I'll stick with the good, old fat-free, okay?"
            "Shiori's eyes widen and her cheeks colour as my answer sinks in and she realises that she's still pushing her breasts together almost in my face."
            "Her arms shoot to her sides and she stands bolt upright, making her chest bounce in sympathy."
            shiori.say "Oh...okay...that's...that's great, [hero.name]..."
            "She pours the milk into one of the cups of black coffee as an awkward silence fills the space between us."
            "Once she's stirred the coffee and placed it on the desk, she gives me a fragile smile and hurries out of my office."
            hide shiori with moveoutleft
            "I blow out my cheeks and shake my head, still not quite able to get my head around what Shiori actually just did."
        "Yes":
            $ shiori.love += 5
            $ shiori.sub += 10
            "I look Shiori in the eye and then glance down at her breasts, licking my lips as I try to make a decision."
            "The look in her eyes tells me that she's totally serious, and I can't deny that I'm instantly curious too."
            "I don't know whether it's a kink in me, or just a natural instinct given the size of her breasts."
            "But can anyone honestly say that they haven't at least wondered what breast milk tastes like?"
            show shiori happy
            mike.say "Erm...okay, Shiori...that sounds...nice."
            "Her face instantly lights up at my accepting her offer."
            shiori.say "Sure thing, [hero.name]!"
            shiori.say "I'm so happy to serve you - to let you use every single part of me."
            shiori.say "It makes me feel so happy...so useful!"
            "I loosen my collar with a finger as Shiori describes how she wants to be used by me."
            "But then I find myself tugging in my tie as though it's a garrote as soon as she begins to unbutton her blouse."
            "Shiori bares her left breast, pulling down her bra so that it falls, full and heavy to sway over my desk."
            "She's actually going to do it!"
            hide shiori
            show shiori milk
            with fade
            "Cupping the breast with her right hand and placing her left hand atop it, she dangles the breast over one of the cups of black coffee."
            "Shiori then begins to push her left hand down the breast, pressing and massaging as she goes."
            "No milk flows to begin with, but I can see from her expression that she's becoming somewhat aroused already."
            "As Shiori sighs and moans from the sensations of trying to milk herself, eyes closed and biting her lip, I can feel my cock stiffening in sympathy."
            "Soon the first of the milk begins to dribble from her large, swollen nipples and into the steaming coffee below."
            "And then it starts to come in more regular squirts, most hitting the cup, but some spilling onto the desk around it."
            "The milk is thick and it must be full of fat, as I can see it covering the surface of the coffee with an oily sheen."
            "Thick bubbles of fat are also coagulating and floating as more breast milk is pumped into the cup."
            "By now, the contents are starting to spill over the lip of the cup, and Shiori's eyes are beginning to glaze over."
            "My erection is becoming painful for the want of being stuck into her, and I can only guess that her pussy must be in a similar state."
            hide shiori milk
            show shiori
            with vpunch
            mike.say "SHIORI!"
            "She snaps out of it suddenly at the sound of my raised voice."
            mike.say "Shiori...that's enough - the cup's full, see?"
            "She looks at me with a distant expression, and then down at the cup."
            shiori.say "Oh, I see...silly me!"
            "She grins whilst still looking more than a little spaced out, and turns to leave."
            mike.say "Ahem...Shiori - your collar's a little twisted..."
            "Shiori glances down and takes a full five seconds to realise that her left breast is still hanging out."
            "She giggles in embarrassment, makes herself decent and then slips out of my office."
            hide shiori with easeoutleft
    return

label shiori_sleep_office:
    "At first it's not something that I even noticed, just a mild annoyance in the corner of my mind."
    "It's like, I emailed Shiori about something that wasn't too important about an hour ago."
    "And since then I haven't heard anything back from her on the subject."
    "The more time that passes, the more that matter goes from unimportant to pretty urgent."
    "And then there's that weird noise that I keep hearing too."
    "It's weird, like someone sawing wood in another room."
    "But there's nobody doing maintenance on this floor of the building."
    "So what in the hell can it be?"
    "Finally I can't stand it any longer."
    "I pick up the phone and dial Shiori's extension."
    play sound phone_calling
    "It rings and rings, then goes straight to voicemail."
    "And that's the last straw."
    stop sound
    "I stand up, sending my chair skidding across the floor behind me."
    "Then I stalk around my desk and out of the door."
    scene bg office with fade
    mike.say "Shiori?"
    mike.say "Shiori?"
    mike.say "Where are you?!?"
    "I spot that there's someone sitting at her desk."
    "But it looks like they're leaning forwards, so I can't see if it's her."
    "And as I get closer, the ruttling, sawing sound is starting to get ever louder."
    mike.say "Shiori?"
    mike.say "Are you okay?"
    "Walking around to the front of her desk, I can't quite believe what I'm seeing."
    show shiori sleep office with fade
    "Shiori's sitting at her desk, but her head's sagging forwards."
    "Her head's not actually on the desktop either, it's resting on her chest!"
    "Shiori's boobs are literally so big they're acting like pillows!"
    "She makes the noise again, and I realise that she's snoring."
    "Shiori's actually fallen asleep at her desk!"
    "So that explains why she's been unreachable for the past hour."
    "But what am I going to do about it?"
    menu:
        "Wake her up with kiss" if shiori.love >= 80:
            "The first thing that pops into my head is the tale of Sleeping Beauty."
            "Although I don't think she was as well-endowed as Shiori is."
            "At least in the chest department!"
            "That gives me an idea, one that might get me in trouble with HR."
            "But once I have it in my head, I can't seem to shake it off."
            "So I lean in close to Shiori."
            "And then I place my lips against hers."
            "At first nothing happens."
            "But then slowly she begins to stir."
            "Shiori's lips twitch against mine."
            hide shiori
            show shiori kiss
            with dissolve
            $ shiori.flags.kiss += 1
            "And then she parts them, her tongue sliding between my own."
            "Before I know it, what was supposed to be a gentle kiss becomes pretty intense."
            "It's only when Shiori finally opens her eyes that it comes to an end."
            hide shiori
            show shiori close surprised blush
            shiori.say "Oh..."
            shiori.say "Oh my goodness!"
            shiori.say "It wasn't a dream?"
            show shiori embarrassed -close
            "I pull back a little and offer Shiori a shrug."
            mike.say "I'm sorry, Shiori."
            mike.say "That was pretty inappropriate of me."
            mike.say "But you just looked so sweet while you were sleeping."
            "At first, Shiori's cheeks flush red as she accepts the compliment."
            "But then the reality of what I just said seems to dawn on her."
            show shiori sad
            shiori.say "Please don't tell anyone I was sleeping?"
            shiori.say "It won't happen again, I promise!"
            "I nod and smile, pleased to be let off the hook for kissing her without permission."
            "And I'm happy not to press the issue with her."
            mike.say "It's okay, Shiori."
            mike.say "So long as you don't make a habit of it, okay?"
            show shiori normal
            $ shiori.love += 4
            "Shiori nods and makes a show of getting back to work."
            "But I note the way she keeps stealing glances in my direction when she thinks I'm not looking."
        "Wake her up gently":
            "Well, I know what I'm not going to do."
            "And that's wake her up harshly."
            "Shiori works so hard around here."
            "And her personal life is no picnic either."
            "So she deserves to be treated with kindness and care."
            "I lean in close and put a hand on Shiori's shoulder."
            "And then I shake her gently."
            mike.say "Shiori?"
            shiori.say "Mmm..."
            shiori.say "Wha..."
            mike.say "Shiori, you need to wake up!"
            "Shiori's eyes open slowly, and the seems to recognise me."
            "But as she wakes up, her expression becomes ever more confused."
            hide shiori
            show shiori surprised
            shiori.say "[hero.name]?"
            shiori.say "How can you be here and in my dream?"
            shiori.say "And now you have your clothes back on too!"
            mike.say "Shiori..."
            mike.say "What are you talking about?"
            "By now Shiori seems to be fully awake."
            "And she appears to know that she's said too much as well!"
            show shiori blush
            shiori.say "Oh...oh my!"
            shiori.say "I was just groggy, that's all!"
            show shiori embarrassed
            shiori.say "Please don't tell anyone I was sleeping?"
            shiori.say "It won't happen again, I promise!"
            "I nod and smile, still intrigued by Shiori's dreams."
            "But I decide not to press the issue with her."
            mike.say "It's okay, Shiori."
            mike.say "So long as you don't make a habit of it, okay?"
            show shiori normal -blush
            $ shiori.love += 1
            "Shiori nods and makes a show of getting back to work."
            "And I decide to leave it a little while before asking her for anything."
            "Because it looks like she'll need the time to recover."
        "Scold her":
            "I shake my head and lean in close to Shiori's ear."
            "And then I shout into it."
            mike.say "Wakey, Wakey!" with vpunch
            mike.say "No sleeping on company time!"
            hide shiori
            show shiori surprised at center, vshake
            "Shiori instantly leaps up and lets out a wail of alarm."
            shiori.say "WHA..."
            shiori.say "What?!?"
            shiori.say "I wasn't asleep, I swear it!"
            shiori.say "I was just resting my eyes!"
            "I shake my head at Shiori's excuses."
            mike.say "Don't give me that, Shiori."
            mike.say "If you need extra sleep, get it while you're at home, okay?"
            show shiori sad
            "Shiori looks down at her feet and nods her head."
            $ shiori.sub += 1
            shiori.say "Yes, [hero.name]."
            shiori.say "Of course I will."
            hide shiori
            "I nod and begin to walk back to my office."
            "Sure, I feel a little bad at treating Shiori like that."
            "And I know she doesn't have the easiest life."
            "But I can't let that undermine my career as well as hers!"
        "Scold her harshly (this will never happen again)":
            "I shake my head and lean in close to Shiori's ear."
            "And then I bellow into it."
            mike.say "WAKE UP!" with vpunch
            mike.say "Wake up, you lazy cow!"
            hide shiori
            show shiori surprised at center, vshake
            "Shiori instantly leaps up and lets out a wail of alarm."
            shiori.say "WHA..."
            shiori.say "What?!?"
            shiori.say "I wasn't asleep, I swear it!"
            shiori.say "I was just resting my eyes!"
            "I shake my head at Shiori's excuses."
            mike.say "Don't give me that, Shiori."
            mike.say "If I catch you sleeping on the job again, you're done here."
            mike.say "Do I make myself clear?"
            show shiori sad
            "Shiori looks down at her feet and nods her head."
            $ shiori.love -= 2
            shiori.say "Yes, [hero.name]."
            shiori.say "Of course I will."
            hide shiori
            "I nod and begin to walk back to my office."
            "It's not my fault that girl's life is a dumpster fire."
            "And it's not my fault she's let herself become a human doormat either."
            "She needs to sort herself out, or else I need to get rid of her."
            $ shiori.flags.stop_sleep_office = True
        "Let her sleep":
            "I shake my head and smile at the sight."
            "I know that I should wake her up."
            "Maybe even tell her off for sleeping on the job."
            "But I know just how hard Shiori's life is outside of work."
            "And none of those misfortunes are her fault either."
            "She works so hard to provide for her son too."
            "So if it's down to me to do something about it, then so be it."
            "Because what I'm choosing to do about it is nothing at all."
            hide shiori with fade
            "I turn around and walk back to my office as quietly as I can."
            "And once I'm there, I divert Shiori's calls to my own phone too."
            "Maybe she'll find out about it or maybe she won't."
            "Either way it doesn't matter."
            "Because I'm not doing it for thanks."
            "I'm doing it because I think it's right."
    hide shiori
    return

label shiori_show_off_3:
    show shiori at left with moveinleft
    "I'm not surprised when Shiori appears in my office clutching an armful of brushes and cleaning products."
    "After all, she was the one that spilled coffee all over the carpet the other day."
    "And the stain's still there, right where she left it when she scurried away, pulling down her skirt."
    show shiori happy at center with move
    shiori.say "Good morning, [hero.name]."
    show shiori normal
    shiori.say "I hope you're not still mad about yesterday?"
    shiori.say "I came to clean up the mess I made - you see?"
    "Shiori holds out what she's carrying, as if I need to have its purpose spelled out to me."
    mike.say "Of course I'm not mad at you, Shiori."
    mike.say "What happened the other day was an accident, that's all."
    mike.say "But it's good of you to offer to clean up."
    "Shiori beams at me, clearly over the moon to have earned my praise."
    "But as she gets down to work, I have my suspicions that all is not as it seems."
    "It's still odd coincidence that Shiori just so happened to trip over and expose herself when going commando."
    "And there's no need for her to be scrubbing at the stain she left, as the cleaners will just take care of it anyway."
    show shiori at onknees with ease
    "Sure enough, my concerns are proven valid when Shiori gets down on her hands and knees in front of my desk."
    hide shiori with easeoutbottom
    "She puts a lot of effort into grinding away at the stain with a scrubbing brush, grunting the whole time."
    "But there seems to be more wiggling of her backside than any notable lessening of the stain itself."
    show shiori at center, onknees with easeinbottom
    shiori.say "Oh bother."
    shiori.say "This isn't going to do it."
    shiori.say "What I need is a bigger brush!"
    show shiori at center with ease
    "I watch with morbid fascination as Shiori hauls herself up and makes for the clutter of brushes she brought with her."
    "It doesn't take her long to become hopelessly entangled in them, swaying dangerously back and forth."
    shiori.say "Silly things - why won't they do as they're told!"
    hide shiori with easeoutbottom
    play sound body_fall
    pause 0.3
    with vpunch
    "And then she pitches forwards, sending everything clattering to the floor, followed by herself."
    "I stand up to see where she fell, not feeling the need to come rushing to her aid this time."
    "Something just tells me that Shiori's not going to have landed too badly from a fall like that..."
    show shiori fall nopanties plug bucket with fade
    "And sure enough, upon rounding the side of the desk, I see her sprawled on her hands and knees."
    "Just like before, Shiori's skirt has ridden up and exposed the fact that she's not wearing any panties."
    "But then I stop, dead in my tracks, amazed at what I can see."
    "There, emerging from between her pale, rounded buttocks, is the unmistakable shape of a butt-plug."
    "And not any butt-plug either, as I instantly recognise the size, colour and shape of the one I bought Shiori myself!"
    "The end of the plug moves and bobs in her ass as she scrambles around on the floor."
    "I'm fascinated, not only by the sight of it, but also by the urge to reach down and pull it out."
    "Right now Shiori's moaning and complaining about the stubborn nature of the coffee stain."
    "But I can't imagine what noises would come out of her were I to yank the plug free!"
    shiori.say "Oops!"
    shiori.say "Did my naughty skirt ride up again, [hero.name]?"
    shiori.say "Whatever must you think of me?"
    hide shiori
    show shiori close blush
    with fade
    "Though Shiori makes a show of pulling down her skirt and blushing, she has to know just what she's doing."
    "And doing it with the butt-plug that I bought her pretty much makes anything else an impossibility."
    return

label shiori_office_bj:
    scene bg office
    show shiori
    menu:
        "Talk to Shiori about your idea.":
            pass
        "Deal with her later":
            $ hero.cancel_event()
            return
    mike.say "Shiori, I have an idea, if you're interested."
    "Shiori looks up from her desk, eyes wide."
    shiori.say "Did I do something wrong, [hero.name]?"
    "I shake my head."
    mike.say "No, nothing like that, but I was thinking maybe you deserve yourself a little reward. Of course... it'd be pretty dangerous if we get caught."
    hide shiori
    if hero.flags.isceo:
        scene bg ceo
    else:
        scene bg personal
    "I walk past her, letting her wonder what it is we were doing."
    "Sitting at my desk, I resolve to get some work done before she comes in."
    show shiori
    "Soon, however, there's a knock on my door. Shiori stands there, looking shy as she meekly speaks up."
    shiori.say "W... what did you want from me, Boss...?"
    "I scoot back from my desk, my legs spread a bit as I motion down underneath."
    mike.say "Come on over here..."
    show shiori close
    "She gasps, but does as she's told."
    hide shiori with easeoutbottom
    "Soon, she's sitting in the little area under my desk, peering up at me with big, excited eyes."
    shiori.say "Oh, boss... if I'm in here, no one's going to be out there to greet people. What if someone comes in?"
    show shiori bj office outfit smile with fade
    "I unzip my pants, letting my dick spill out."
    mike.say "That's where the fun comes in."
    shiori.say "O... oh my!"
    "She stares at my length."
    shiori.say "Boss, I don't think... is this even... ethical?"
    mike.say "Since when were you about following the rules?"
    shiori.say "H... hey. I don't break them... on purpose."
    mike.say "Well, then, go ahead."
    "She wraps her fingers around the base as she scoots herself in, closing one eye as she licks up from base to the tip."
    show shiori bj suck
    "She sighs, her body shuddering as she holds onto my thigh with one hand and lowers her lips around my cock, holding me still with the other."
    "She slips up and down along the pole, the quiet office filled with the slurping slick sounds of her mouth and tongue over my length. I groan as I pet her hair, and she glances up at me, sucking upon my length with a happy squeak."
    hide shiori with vpunch
    "The door opens up, and I scoot in, reflexively pushing her head closer to my thighs, and holding her in place."
    show aletta with easeinleft
    "After a quick muffled grunt, she is trapped in between my thighs as I sit there, hands folded as Aletta enters the room."
    aletta.say "Ah, there you are [hero.name]. I've been looking for you."
    mike.say "Ah, yeah? You have?"
    show aletta sad
    aletta.say "Yes, I wanted to discus some of the reports here. It seems your office has missed a few things."
    mike.say "Ah, that must be my Shiori. She's a nice girl, but lacks proper discipline."
    show aletta annoyed
    aletta.say "This company can't permit slackers, Mister [hero.family_name]."
    mike.say "Oh, don't you worry about that. I'll be sure to whip her into shape."
    hide aletta
    show shiori bj office outfit suck
    "As I speak, Shiori's mouth around my cock only sucks harder."
    "I wince slightly, but keep my cool."
    mike.say "In... in fact, I think I'll personally see to her training, if you don't mind. I have a... a good feeling about this one, as long as she's... whipped into shape."
    hide shiori
    show aletta
    "Aletta nods."
    aletta.say "Well, as long as you have things handled, I guess I'll just head on out."
    aletta.say "I want a report on her workmanship in the morning."
    hide aletta with easeoutleft
    play sound door_slam
    "Aletta leaves, slamming the door behind her."
    "A moment later, I fall forward on the desk and shove my hips forward, practically forcing my cock down Shiori's throat."
    show shiori bj office outfit suck cumshot with hpunch
    "Under the desk, Shiori gulps and gasps as cum shoots down her."
    with hpunch
    "Soon, she backs out, with only a small trail of pearly whiteness left dribbling down her chin."
    hide shiori
    show shiori blush
    with fade
    "I scoot back, smiling down at her as she wipes her chin off, panting heavily."
    mike.say "Well, I'm sure you heard all of that, but you know what...?"
    mike.say "Looking at you, I think you have a stellar performance review."
    "She smiles up at me, sighing with dreamy happiness."
    shiori.say "Pleasure as always, [hero.name]."
    mike.say "Glad your morale is up."
    "I zip up my pants and stand up."
    mike.say "Because you're going to have to stay late tonight to organize that mess."
    "Shiori whimpers slightly, though her smile never leaves her face."
    shiori.say "I'll... I'll do my best, sir."
    mike.say "That's the morale we need at this company. Good job!"
    hide shiori
    return

label shiori_kiss_me:
    call shiori_greet from _call_shiori_greet_5
    show shiori
    "I don't think that in all the time she's been working under me, I've ever seen Shiori do something that could honestly be described as assertive in any way."
    "And that's exactly what makes me stop and watch, almost in fascination, as she seems to be trying to summon the will to do just that."
    "At first I just assume that she's pissed about something and is trying to summon up the courage to mention it to me."
    "But no matter how long of a pregnant pause I allow to build up between us, she still doesn't as much as open her mouth to let out a squeak."
    "I really don't want to be an asshole to Shiori, as she's genuinely as shy and bumbling as she's being right now."
    "And yet I also don't want to have to sit around all day, just for the sake of hearing her meekly explaining some minor grievance that I don't even care about."
    "I let out an exasperated breath, meaning to utter a couple of words with the intention of prodding Shiori into action."
    "But the moment that I have my mouth open, she seems to come instantly to life."
    "Before I have time to guess what she's doing, I feel her mouth clamping over mine like a leech!"
    show shiori kiss with fade
    $ shiori.flags.kiss += 1
    "Shit, what's going on?"
    "Is Shiori actually planting a kiss on me?!?"
    "I haven't fully managed to answer that question before I find myself leaning into the unexpected kiss without any conscious choice on my part."
    "Her lips are so full and soft, and the sounds that she's making are such a turn-on that I can't help but go along with it too."
    hide shiori kiss
    return

label shiori_preg_talk:
    show shiori
    if "shiori_blackmail_confession" not in DONE:
        mike.say "Hey, Shiori - what's up?"
        "I can tell the very moment that I look into her eyes this close up that I've badly misjudged the situation."
        "Shiori's own eyes are almost as wide as saucers, glazed over as if seeing only wondrous things."
        "All tell-tale signs that, whatever the matter is, it's taking over every thought that's passing through her head."
        show shiori close
        "At the sight of me, Shiori practically throws herself in my direction, almost collapsing into my unsuspecting arms."
        "It's all that I can do to keep from either dropping her or being knocked over myself."
        shiori.say "Oh, [hero.name], I'm so happy to see you!"
        shiori.say "I have the most wonderful news!"
        "Wonderful news?"
        "Now that's not something I expected to hear from her today."
        mike.say "Erm...okay, Shiori."
        mike.say "I guess you should probably tell me just what it is..."
        "Her own enthusiasm means that she totally misses my own confusion and sudden anxiety as to just where all of this will ultimately lead."
        show shiori happy
        "Shiori simply smiles so broadly that her eyes are almost forced closed by the degree to which her cheeks rise in sympathy."
        "She pulls back from my embrace just enough to grab one of my hands and hold it over her belly."
        "Her grip is far stronger than anything I ever imagined her being capable of, and it even scares me a little."
        shiori.say "Can you feel it?"
        "She's looking at me with such intensity that I can hardly tear my eyes away from her gaze to look down at her stomach."
        shiori.say "Can you feel the first stirrings of the miracle that we created?"
        shiori.say "The new life that you planted inside of me?"
        "Suddenly, realisation dawns on me."
        mike.say "Oh god, you don't mean..."
        "Shiori nods furiously, her smile becoming almost manic as she does so."
        shiori.say "Yes, [hero.name], I do - I'm pregnant!"
        shiori.say "Isn't it wonderful news?!?"
        show shiori normal
        menu:
            "You should abort":
                "I feel like a gaping black hole just opened up under my feet and is trying to pull me down into oblivion."
                "It's not that I hate the idea of either having a kid or being with Shiori for a long while to come."
                "But having both dropped on me from a great height is simply a terrifying prospect."
                mike.say "But...Shiori...we can't..."
                "Even someone as oblivious and innocent as Shiori can't fail to pick up on the fact I'm not exactly elated with her news."
                "Her eyes become wide and her smile shrinks away to almost nothing."
                show shiori surprised
                shiori.say "[hero.name]...what's the matter?"
                shiori.say "Aren't you happy that you're going to be a father?"
                "Something about her expression makes the floodgates finally open for my emotions."
                mike.say "I can't have a kid, Shiori...we can't..."
                show shiori sad
                "Shiori suddenly cries out in horror."
                shiori.say "Oh, [hero.name]...you don't mean..."
                mike.say "It's okay, Shiori - I'll pay for the operation."
                mike.say "You won't have to worry about a thing, I promise!"
                hide shiori
                show shiori sad
                "Shiori backs away from me slowly, shaking her head as if she no longer knows who she's looking at."
                shiori.say "No...I won't...I won't let you kill our baby!"
                "She turns her back on me with more drama than I thought she was capable of."
                "And then she runs away from me, her sobs carrying backwards on the air."
                $ shiori.set_gone_forever()
            "That's wonderful":
                "It takes a good few moments of staring into space and not saying a word."
                "But I soon realise that most, if not all, of my negative emotions are just the shock of being told that I'm going to be a father."
                "When I actually look down and see Shiori looking back up at me, hanging on my response to her news, I feel positively elated."
                show shiori happy
                $ shiori.love += 10
                mike.say "Shiori...that's amazing news!"
                mike.say "I'm going to be a dad!"
                "I don't think I've ever seen a smile like the one on Shiori's face right now."
                "Her eyes almost seem to glaze over with happiness."
                mike.say "Wait...you do want me to be involved, to raise the kid - don't you?"
                "Shiori doesn't seem to be able to believe the words that keep coming out of my mouth."
                shiori.say "YES...I mean, yes...of course I do, [hero.name]!"
                shiori.say "Actually, I was worried that you...might not want to be..."
                "I shake my head in disbelief at the very idea that she might think I would reject her and the baby."
                mike.say "Shiori, I never really thought about it much before."
                mike.say "But the way I see it, this is the perfect chance for us to build a life together."
                mike.say "I mean, this pretty much makes us a family, doesn't it?"
                "Suddenly I feel my middle being squeezed tightly enough to make me gasp for breath."
                "I look down in surprise to see Shiori wrapped around me like a constricting snake."
                shiori.say "Oh, [hero.name], you've made me so happy!"
                $ shiori.flags.toldpreg = True
        hide shiori with moveoutleft
        "Once Shiori pulls herself together enough to be on her way, I'm left alone to contemplate all that she's told me."
        "I'm still feeling more than a little disoriented myself, and it still hasn't really sunk in."
        "All that has is the overwhelming news that I'm going to be a father!"
    else:
        "It can be pretty tough to tell when there's something up with Shiori, as she's kind of meek and has a worried look about her most of the time anyway."
        "So the first that I tend to know about such things is when she actually manages to pluck up the courage to just come out and tell me about it."
        "I suppose if I'm honest, the matter's not helped by the fact that I'm usually distracted by staring at her breasts."
        "That and imagining what I want to do to her the next time that an opportunity presents itself..."
        shiori.say "Erm...hey, [hero.name]..."
        shiori.say "Did you hear what I said?"
        shiori.say "It is kind of important..."
        shiori.say "But I suppose I could come back later, if you're too busy right now..."
        "See what I mean?"
        "With some effort, I finally manage to tear by eyes away from the enticing sight of Shiori's cleavage and look her straight in the eye."
        mike.say "Sorry, Shiori - I was miles away!"
        mike.say "What were you trying to tell me?"
        show shiori sad
        "Shiori manages a weak smile at my belated attention, but it's clearly not enough to change the rather sad look in her eyes."
        shiori.say "Well...you know how we've been...getting to know each other?"
        shiori.say "Getting to know each other...outside of work?"
        "I nod slowly, my head filling instantly with a series of rather lewd images."
        "I'm guessing by that she means that we've been fucking like rabbits whenever the chance comes up."
        shiori.say "And you remember that we weren't always that careful when it came to...using protection?"
        "Suddenly I understand the reason for her unusually downcast mood and why she's beating about the bush."
        mike.say "Shiori - what are you trying to say?"
        "She smiles helplessly, her hands unconsciously hugging her belly in a protective manner."
        show shiori normal
        shiori.say "[hero.name], I'm pregnant!"
        shiori.say "I'm having your baby!"
        "My mouth works silently for a moment as I try to wrap my head around what Shiori just told me."
        "And then, when I finally find the words, it all comes out in a desperate flurry of verbiage."
        mike.say "What?"
        mike.say "Are you sure?"
        mike.say "Could you have made a mistake?"
        mike.say "What in the hell are we going to do?!?"
        show shiori sad
        "With the same pained smile on her face, Shiori takes a deep breath."
        "I suppose she's already had some time to think about this whole mess."
        "But I have no idea what conclusions she might have come to..."
        if not shiori.flags.donestripping:
            shiori.say "I...I always thought that I'd be happy if you made me pregnant, [hero.name]."
            shiori.say "Really, I did!"
            shiori.say "The thought of it even made me touch myself...when I was alone at night..."
            show shiori blush
            "Shiori's cheeks suddenly redden at this confession."
            mike.say "I'm sensing there's a 'but' about to be inserted right about now?"
            "Shiori lets out a sigh of regret so genuine that it almost feels like a stab to the heart."
            shiori.say "Oh, [hero.name] - I'm already a single mother!"
            shiori.say "I struggle to make ends meet as it is."
            shiori.say "The way things are, I can't possibly keep our baby."
            mike.say "So...what are you saying, Shiori?"
            show shiori normal
            shiori.say "I'm...I'm going to have a termination!"
            menu:
                "Agree with Shiori":
                    "It takes me a moment to gather myself and reply to this second bombshell from Shiori in almost as many minutes."
                    "I can see something in her eyes that I take to be a glimmer of desperate hope."
                    "Maybe the hope that I'll convince her to change her mind."
                    "But I can't see any way out of this mess for us either."
                    mike.say "If that's what you want, Shiori, then I'll support you one hundred percent."
                    mike.say "I'll foot my share of the bill too, of course."
                    mike.say "And if there's anything else I can do..."
                    show shiori sad
                    "Shiori nods sadly, as if my words have confirmed the course she was already settled on."
                    "She doesn't say another word to me then, just turns and walks quietly away."
                    "I suppose she needs to be alone with her thoughts right now."
                    hide shiori
                    $ shiori.love -= 30
                    $ shiori.unpreg()
                "Plead to keep the baby":
                    "I don't even have to hesitate before I blurt out my response."
                    mike.say "No, Shiori!"
                    mike.say "You can't mean that, surely?!?"
                    show shiori happy
                    "She looks surprised, and more than a little hopeful at my outburst."
                    show shiori sad
                    "But then her face becomes sad once more, and she shakes her head."
                    shiori.say "But, I just couldn't raise another child - not alone!"
                    mike.say "You won't be!"
                    mike.say "Alone, that is!"
                    shiori.say "You mean..."
                    mike.say "Yes, Shiori - I want to raise this baby with you!"
                    mike.say "I want us to be a family!"
                    "She shakes her head, seemingly not convinced."
                    shiori.say "I just don't know if that would work."
                    shiori.say "So for now...my decision stands."
                    "She doesn't say another word to me then, just turns and walks quietly away."
                    "I suppose she needs to be alone with her thoughts right now."
                    hide shiori
                    $ shiori.love -= 20
                    $ shiori.sub -= 10
                    $ shiori.unpreg()
        else:
            shiori.say "I don't know, [hero.name], I really don't."
            shiori.say "That's why I wanted to tell you as soon as I could."
            shiori.say "I needed to know what you would want to do."
            shiori.say "I HOPED you would know what would be for the best..."
            "Oh god - I thought just being told I'd gotten Shiori pregnant would be the scariest thing I could imagine right now."
            "But she's pretty much asking me to tell her whether she should keep it or not!"
            "I mean, I like her a hell of a lot and she drives me crazy on a purely physical level."
            "But can I actually commit to raising a child with her?"
            "And maybe even more than that, like devoting a large part of my life to them both?"
            "In the end, I guess it comes down to the question of whether I love Shiori or whether I see her as just another conquest."
            menu:
                "Tell her to have an abortion":
                    mike.say "You're already struggling to raise one child alone, Shiori."
                    mike.say "Add a second and you'll never be able to hold down your job - not a chance."
                    mike.say "I'd offer to support you, but my salary just wouldn't cover it."
                    mike.say "I simply can't afford to pay twice for rent, food and all of the rest."
                    "After I've laid out the reasons that we can't afford a child based on our current circumstances, Shiori looks like she's about to say something."
                    "For a moment, I actually think that she's going to suggest I could make some changes, make a sacrifice if I really wanted to."
                    show shiori sad
                    "But then she just lets out a sad, resigned sigh and nods her head slowly."
                    shiori.say "Yes, [hero.name], I suppose that you're right."
                    shiori.say "Would you...would you at least..."
                    mike.say "Don't worry, Shiori - I'll make all the arrangements."
                    shiori.say "Thank you, [hero.name]."
                    "She doesn't say another word to me then, just turns and walks quietly away."
                    "I suppose she needs to be alone with her thoughts right now."
                    hide shiori
                    $ shiori.love -= 20
                    $ shiori.sub += 10
                    $ shiori.unpreg()
                "Tell her to keep the baby" if shiori.love >= 150:
                    "And that's a question that I instantly know the answer to."
                    mike.say "Shiori, I want you to keep the baby."
                    show shiori happy
                    "At this, Shiori's eyes grow suddenly wide with disbelief and then joy."
                    shiori.say "Oh, [hero.name] - do you really mean that?!?"
                    shiori.say "But...but what about the cost and the hard work?"
                    shiori.say "And you'd need to be involved, as I can't raise two children on my own..."
                    "Shiori trails off as she realizes the implications of what she's just said."
                    show shiori blush
                    "She looks afraid all of a sudden, as though she's over-stepped the mark and is now in serious trouble."
                    shiori.say "I'm so sorry, [hero.name]!"
                    shiori.say "I would never try to force you to..."
                    mike.say "It's okay, Shiori, you're not forcing anything on me."
                    mike.say "I want to raise this child with you."
                    mike.say "Whatever it costs, whatever it takes, we'll handle it - together."
                    show shiori happy
                    "Shiori practically bursts into tears of joy as she rushes to throw her arms around me."
                    "I hug her back, enjoying the feeling of her petite and yet curvaceous body pressed against me."
                    "Looking down at her as she buries her head into my chest, I know I've made the right decision."
                    hide shiori
                    $ shiori.love += 20
                    $ shiori.sub += 10
                    $ shiori.flags.toldpreg = True
    return

label shiori_male_ending:
    $ game.hour = 16




    if renpy.has_label("shiori_achievement_3") and not game.flags.cheat:
        call shiori_achievement_3 from _call_shiori_achievement_3
    $ game.room = "church"
    scene bg church wedding with fade
    "Why is it that, no matter how hard you try, there's always a couple of cliches on your wedding day?"
    "Shiori and I really did make every effort that we could to ensure that things would go smoothly today."
    "But all the same, here I am, standing in front of the altar and feeling the jitters creeping up my spine!"
    "The chapel is already filling up with friends and relatives on both sides, all behaving themselves."
    "And there's been nothing go awry yet either, the whole ceremony so far going according to plan."
    "So why am I so worried?"
    "I guess part of it is that it's been such a long journey for us to get here."
    "From Shiori and I starting out as colleagues in the office and our relationship growing from there."
    "Then there's the matter of the baggage that she was still carrying from the way her last marriage ended too."
    "Wow - I guess when you look at it like that, we really have been through a lot!"
    "But it's been worth it - Shiori's worth it."
    "Maybe I'm just paranoid that we're almost there and this is the last obstacle in our way."
    "It's just as I'm about to dive down another mental rabbit-hole that the music begins to play."
    "Instantly I snap out of it, recognising the track that Shiori chose to come down the aisle to."
    "I look back over my shoulder, willing her to be there..."
    "And much to my relief, there she is - right on cue!"
    show shiori cosplay happy with dissolve
    "Shiori told me that she was going to wear a kimono for the ceremony."
    "But being a stickler for tradition, she refused to let me see it before now."
    "And it was worth the wait."
    "She looks perfect, petite and achingly beautiful as she walks towards me."
    "I can't help grinning from ear to ear at the sight of her."
    "Shiori doesn't take long to notice my reaction, and she blushes deeply."
    "Which of course only serves to make her look all the more demure and desirable."
    if shiori.is_visibly_pregnant:
        "Shiori's hands cradle her swollen belly in an unconscious gesture."
        "It's hard to tell that she's pregnant thanks to the kimono."
        "But the thought of my child growing inside of her is always on my mind."
        "And it simply makes the fact we're about to become a family that much more special."
    else:
        "Shiori clutches the flowers in her bouquet tightly."
        "And I can hear her breathing as she walks the last few feet to the altar."
        "It sounds like she's doing some kind of breath exercises."
        "Seems that she's ever bit as nervous as I am!"
    show shiori at center, zoomAt(1.5, (640, 1040))
    "As soon as she's standing beside me, I turn my head to look at Shiori."
    "And it's no surprise to find she's doing the same thing as well."
    "I don't know if I'm allowed to say anything to her right now."
    "I try to think of something that I could mouth to her instead."
    "But nothing springs to mind that's short and snappy enough."
    "So instead we end up simply staring at each other in dumb silence!"
    "Priest" "Ahem..."
    "In the end, the sound of the priest clearing his throat is what comes to our rescue."
    show shiori normal at startle
    "Shiori and I almost jump to attention, thankful for his taking control of the situation."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "And just like that, we're into it."
    "We're one step closer to tying the knot!"
    "The ceremony passes in a blur of words and phrases."
    "That is until we come to the vows."
    "Priest" "Do you, [hero.name], take Shiori to be your lawful, wedded wife?"
    mike.say "I do."
    "Priest" "And do you, Shiori, take [hero.name] to be your lawful, wedded husband?"
    show shiori happy at startle
    shiori.say "I...I do!"
    "Priest" "Then I call upon all those present..."
    "Priest" "That if they know of any reason these two may not be joined in holy matrimony..."
    "Priest" "To speak now, or forever hold their peace..."
    "Shiori and I look at each other and then at the doors of the chapel."
    "Both of us have been dreading this moment in the ceremony."
    "Shiori's former husband."
    "If he was ever going to show up and throw a spanner in the works - this is the moment!"
    "Everyone seems to hold their breath for the longest time as we wait..."
    "Priest" "I'll take that as a no!"
    "Priest" "Then it is my great pleasure to pronounce you husband and wife."
    "Priest" "You may kiss the bride!"
    "I don't need to be told twice."
    scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
    show shiori kiss cosplay mwedding
    $ shiori.flags.kiss += 1
    "Gathering Shiori into my arms, I kiss her passionately."
    "We did it - we're married!"
    hide shiori
    show shiori happy cosplay close
    "I can feel Shiori's arms around me."
    "And I don't ever want to let her go!"
    scene shiori ending
    if shiori.flags.cowkini:
        show shiori ending cowkini
    else:
        show shiori ending swimsuit
    with fade
    shiori.say "Are...are you REALLY sure that it's okay for me to be doing this?"
    shiori.say "I mean, aren't they expecting [hero.name]?"
    shiori.say "Oh...okay, I guess."
    shiori.say "I'm not sure they're interested in my side of the story, you know?"
    shiori.say "But if you say so - here goes..."
    shiori.say "I think I liked [hero.name] from the first moment that I saw him."
    shiori.say "Well, at least I thought he was really cute and that I'd be working for a handsome boss!"
    shiori.say "But, I never thought that he'd look at me that way - not when I started working under him."
    shiori.say "I suppose that I didn't think I was good enough for him, that I didn't deserve him."
    shiori.say "Sure, he could be demanding at times."
    shiori.say "He was my boss, and that's just how it has to be."
    shiori.say "But he could be sweet and kind too."
    shiori.say "When he found out about the mess my personal life was in, he could have been mean about it."
    shiori.say "More than once it got in the way of my work, and I was scared that he might fire me."
    shiori.say "But [hero.name] surprised me by understanding and doing all he could to help out."
    shiori.say "That's when I knew he was a good man at heart."
    shiori.say "And...well...I suppose..."
    shiori.say "That was about the time I started to have feelings for him!"
    shiori.say "But it was when he met Kanta, my son, that I knew he was special."
    shiori.say "[hero.name] didn't owe Kanta anything at all."
    shiori.say "Yet he was as kind to my boy as he'd been to me!"
    shiori.say "And yes...I...I did wonder after that..."
    shiori.say "Wonder if he could be a father to Kanta."
    shiori.say "A better one than his real father had ever been too."
    shiori.say "I still wasn't expecting it when he asked me to marry him though!"
    shiori.say "I'd have been a fool to say no, after he'd been so good to me."
    shiori.say "And more than that...I knew by then that I was in love with him!"
    shiori.say "Since we got married, we've never looked back, not for a moment."
    shiori.say "[hero.name] and I have a place all of our own."
    shiori.say "[bree.name] and Sasha are sweet girls, of course."
    shiori.say "But we're a family now, and we need the space!"
    if shiori.flags.mikeBabies >= 1 or shiori.is_visibly_pregnant:
        shiori.say "Kanta's getting so tall these days."
        shiori.say "And since little Tetsuo arrived, it's already feeling cramped!"
    else:
        shiori.say "Kanta needs the room to stretch his legs."
        shiori.say "And who knows when he'll have a little brother or sister to play with too!"
    shiori.say "I would have kept on working, if [hero.name] thought that was for the best."
    shiori.say "But I think he already knew that what I really wanted was to make a home for us."
    shiori.say "It's not like I miss the hustle and bustle of the office anyway."
    shiori.say "My time's better spent making sure that [hero.name] comes home to a happy house."
    shiori.say "And I'm not just saying that either - I know it's the truth."
    shiori.say "Because that's another thing [hero.name] gave me."
    shiori.say "He gave me the ability to see my own worth, to know that I'm loved."
    shiori.say "And that means that I'm not afraid of the future anymore."
    shiori.say "Not while the present is this good!"

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not shiori.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_20
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_20
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label shiori_meeting:
    show shiori_stretch_bg
    "It's bad enough having to pretend that you care about something for the sake of looking like you give a shit at work."
    "But the agony of that is magnified by a factor of ten when you're trapped in a room with other people doing the exact same thing."
    "And that's exactly how the meeting that I find myself sitting through this morning feels."
    "It's way too early to be getting into stuff this intense and tedious, and that's plainly obvious to see."
    "In fact, it's written on the faces of Shiori, Audrey and myself as we stifle yawns and try to keep our eyes from closing."
    "That said, I do have to give Aletta all the praise she deserves for putting on a show of defiance and professionalism."
    "For all that the three of us are battling to stay awake and even vaguely alert, the same can't be said for her."
    show aletta
    aletta.say "And I think that if you look at the charts on page six of the report..."
    "At first, no one picks up on the fact that Aletta's left the words hanging in the air."
    "But then she coughs and raps her knuckles on the table, making everyone start in surprise."
    show aletta annoyed
    aletta.say "Ahem!"
    aletta.say "As I was saying - the charts on page six!"
    "I shake my head and hold a hand up, almost pleading with Aletta to show mercy."
    show aletta normal
    mike.say "Okay, okay!"
    mike.say "We get it, Aletta."
    mike.say "This is important stuff, and we're half-asleep."
    show aletta annoyed
    aletta.say "I really don't see how that's MY problem, [hero.name]!"
    mike.say "It's not, Aletta."
    show aletta normal
    mike.say "But do you think we could get some coffee or something?"
    mike.say "That way we can wake up a little, you know?"
    show audrey at right with easeinright
    audrey.say "Yeah, then you can yell at us while we're on a caffeine rush!"
    show shiori at left with easeinleft
    shiori.say "I...I would like some coffee, [hero.name]."
    shiori.say "Kanta was up most of the night with a temperature."
    shiori.say "So I didn't get much sleep..."
    "I know that I should be more professional, but my heart instantly goes out to Shiori."
    "She has such a hard life as a single mother trying to hold down a full-time job at the same time."
    "I don't think that I'd stand a chance at coping with what she has on her shoulders every day."
    hide audrey
    hide shiori
    show aletta annoyed
    "Aletta makes a harrumphing noise, clearly annoyed at the weakness of us lesser mortals."
    "But all the same she nods, seeming to realize that she's facing an uphill task."
    show aletta normal
    "And then she nods towards the coffee pot that's steaming away in the corner of the room."
    aletta.say "I suppose I could do with a coffee too."
    aletta.say "Let's break for five minutes and then get back into it."
    aletta.say "But after that, I'm not stopping or slowing down for any of you."
    aletta.say "Is that understood?"
    hide aletta
    "Aletta gets a round of weary nods and vague sounds of agreement for her trouble."
    "I scan the faces around the table, seeing that Shiori really does look wiped out."
    "Her eyes are heavy and she seems to be fighting just to hold up her head."
    show audrey
    mike.say "Audrey, would you mind fixing the coffee?"
    show audrey frown
    audrey.say "Huh - what did your last slave die of?!?"
    mike.say "I strangled them for refusing to bring me caffeine!"
    hide audrey with easeoutright
    "Audrey rolls her eyes and gets up to do as I've asked her, which leaves me free to check up on Shiori."
    "Maybe it makes me sound a little sexist and behind the times, but I feel the need to be protective of her."
    "I know some of the details of her private life, and the girl's got it pretty hard."
    "The last thing she needs is to have her proverbial balls busted by Aletta on top of all that."
    mike.say "How was Kanta when you left him this morning, Shiori?"
    show shiori embarrassed
    "At the sound of my voice, it seems to take Shiori a moment to realize I'm talking to her alone."
    show shiori normal
    "She regards me with those huge, tired eyes and a weary smile on her face."
    "All of which serves to pull at my heartstrings, making me want to protect her all the more."
    shiori.say "Oh, it'd all but gone by the time he went off to day-care."
    shiori.say "Thanks so much for asking, [hero.name]."
    shiori.say "I know it's silly of me to worry like that."
    shiori.say "But since his father left us, Kanta's all I have!"
    mike.say "I know, Shiori."
    mike.say "It must be tough for you, coping on your own."
    "Shiori cocks her head on one side, clearly enjoying having my shoulder to lean on."
    "She looks so innocent and sweet in that moment, that it baffles me how anyone could hurt her so."
    audrey.say "Coffee's up!"
    "The sound of Audrey's voice and the mugs of steaming coffee that she plants in front of us break the spell of the moment."
    "Shiori and I both snap back into the reality of the meeting room, sitting up as if coming to attention."
    mike.say "Well..."
    mike.say "I'm sure Kanta will be okay."
    hide shiori
    show shiori stretch with fade
    "Shiori nods in agreement, but doesn't speak for the sake of a yawn I can see building up inside of her."
    "She stretches her back and pulls her arms back at the same time, as if trying to shake off her fatigue in one motion."
    "And I have to confess that I can't help staring at the effect all of this has on her considerable cleavage."
    "Maybe I should say something, but the sight of the buttons on Shiori's blouse straining under the pressure is quite remarkable!"
    "So much so that I find myself licking my lips unconsciously the whole time."
    "But then there's the sudden sound of something snapping or twanging."
    show shiori stretch pop
    play sound woosh_punch
    with hpunch
    "And something else shooting across the room like a bullet!"
    audrey.say "AARGH!"
    audrey.say "Shit..."
    audrey.say "My fucking eye!"
    aletta.say "HEY!"
    aletta.say "What's this in my damn coffee!"
    "I glance over my shoulder to see what's happened to Aletta and Audrey, and then back at Shiori."
    "But any confusion that I might have had as to what just happened evaporates as soon as I look at the latter of the three."
    "Shiori is still sitting there, frozen in the same pose as before."
    "Her hands are crossed behind her head and her chest is thrust out."
    "The only difference is that I can now see most of her bra and a good portion of her heaving breasts too!"
    "It sounds crazy, like something out of a cheesy comedy skit."
    "But she actually did just pop the buttons down the front of her blouse!"
    "Shiori's face turns bright red as she slowly lowers her arms and pulls her blouse together."
    shiori.say "Oops..."
    shiori.say "That never happened before!"
    "Aletta sniffs in disapproval."
    aletta.say "Well, that's put me off my coffee!"
    "Audrey is still nursing the eye one of the buttons managed to hit."
    audrey.say "Seriously, Shiori..."
    audrey.say "You should need a fucking permit for those things - they're lethal weapons!"
    shiori.say "I...I'm sorry..."
    "As if the look of sheer embarrassment on Shiori's face weren't enough."
    "I can almost feel the words of the other two girls cutting into her like knives."
    mike.say "Okay, that's enough."
    mike.say "It was clearly an accident, and Shiori already apologized."
    aletta.say "That's easy for you to say, [hero.name]."
    aletta.say "She didn't contaminate your coffee!"
    audrey.say "Your coffee?!?"
    audrey.say "What about my eye?"
    audrey.say "That ditzy bitch could have blinded me!"
    mike.say "I said enough already!"
    mike.say "That's no way to talk to a colleague that's clearly under pressure."
    mike.say "I'm pulling the plug on this meeting until we've all had time to calm down."
    "There are mutters and mumbling from Aletta and Audrey at this."
    "But they collect their things and shuffle out of the meeting room all the same."
    hide shiori stretch
    show shiori close
    "When they're gone and I'm alone with Shiori, she looks up at me, a shy but grateful look on her face."
    shiori.say "Thanks, [hero.name]."
    shiori.say "You're a really great boss, you know?"
    mike.say "Ah, it's okay, Shiori."
    mike.say "Now, let's see if we can find some pins or binder clips in the stationary cupboard."
    mike.say "You know - so we can make you decent again!"
    $ shiori.love += 5
    return

label shiori_payoff_conversation:
    if shiori.love.max < 200:
        $ shiori.love.max = 200
    show shiori
    "Even as I sidle up to her, I can already see the mixed emotions that my presence is causing inside of Shiori."
    "On the one hand, she looks embarrassed to see me, no doubt thanks to the fact I know all about her dirty, shameful little secret."
    "But on the other, it's not like Shiori's ever been any good at hiding her true feelings for me either."
    "And so she can't help smoothing her hair back behind her ear as a meek smile begins to curl her lips."
    show shiori blush
    shiori.say "H...hello, [hero.name]."
    shiori.say "What can I do for you today?"
    shiori.say "Was there something I was supposed to be getting on with?"
    "All the time that she's saying this, Shiori still can't quite bring herself to look me in the eye."
    mike.say "No, Shiori, I don't need anything from you just now."
    mike.say "Actually, I wanted to talk about something that I can do for you."
    "I'm beating about the bush, trying my best to not come right out and say it."
    "But still Shiori seems to know exactly what I'm talking about."
    "I know this because she instantly jumps a little and turns away from me."
    shiori.say "Oh, [hero.name], I thought we talked about that?"
    shiori.say "I'm working to pay off the debt, and I'm sure it'll be all over soon."
    shiori.say "I won't let it affect my work for you, I promise!"
    shiori.say "And I couldn't bear to think of you getting mixed up with those awful, awful men..."
    "I put a gentle hand on Shiori's shoulder, trying to turn her around to face me again."
    "She resists at first, but then I see her sag a little, as if surrendering to the inevitable."
    "And she allows me to twist her so that we're looking each other in the eye."
    mike.say "Now you listen to me, Shiori."
    mike.say "I don't want to hear you talking like that again, you hear me?"
    mike.say "And this isn't about your work, either - it never was."
    mike.say "This is about you having someone to stand up for you."
    mike.say "Having a friend to help out when you need it."
    show shiori surprised
    "Shiori clasps her hands together underneath her chin, gazing up at me in disbelief."
    "Her eyes are simply huge, wide open and so completely without guile that I could just fall into them."
    "And then there's the way that her chest is heaving, going up and down with each breath she takes."
    "Jesus Christ - how could her ex have ever done what he did to this woman?!?"
    "She makes me sweat just looking at her!"
    shiori.say "[hero.name]..."
    shiori.say "You can't mean..."
    "I nod, swallowing to make sure that I can actually speak the words without my voice cracking."
    mike.say "Yes, Shiori, I mean exactly that."
    mike.say "You don't have to worry about your husband's debt anymore."
    mike.say "And you'll never have to dance in that club again, either."
    mike.say "I've taken care of it all."
    "Shiori looks at me in stunned silence."
    show shiori normal
    "Her lips are moving without a sound emerging from between them."
    "And when she finally manages to speak, her voice is small and meek."
    show shiori happy
    shiori.say "Thank you, [hero.name]."
    shiori.say "I don't know how I can ever repay your kindness."
    shiori.say "Really, I don't - or why you'd do that for me..."
    "Though my mind is flooded with imaginative and original means of recompense."
    "I remind myself that I'm supposed to be doing this to help Shiori, not exploit her."
    mike.say "Shiori, there's no need to think like that."
    mike.say "I didn't get you off the hook with them just to make you indebted to me."
    show shiori close
    "Shiori takes me by surprise then, leaping forwards and wrapping her arms around my waist."
    "She's pressing herself as close to me as she possibly can, as if clinging to me for dear life."
    "The sensation of her body against mine is indescribable, and it takes my breath away for a moment."
    "And I swear that I can feel her heart, pounding away inside of her chest."
    shiori.say "Oh, [hero.name]."
    shiori.say "You're like a white knight, or...or a prince from a fairy-tale!"
    shiori.say "You're my hero!"
    "Slowly and with more than a little trepidation, I return Shiori's embrace."
    "As she feels my arms wrap around her, she lets out a satisfied sigh."
    "And then she presses herself closer to me still, placing her head against my chest."
    "The whole time I can feel my cock stiffening for her, my body aching for her too."
    "I have no idea if Shiori even realises the effect that she's having on me."
    "But I know how easy it would be to become addicted to having her treat me like this..."
    return

label shiori_strip_club_payoff:
    show bg stripclub
    "I felt nervous when I was walking into the club as just another patron in search of a lap-dance."
    "And so much more so when I was doing the same with the aim of confronting the manager about Shiori."
    "So you can imagine how I feel now that I have a bag stuffed with ten grand clutched in my hand."
    "I try to walk back into the club with all the confidence I can muster."
    "But there's nothing that I can do to keep my heart from pounding and my eyes from darting this way and that."
    "Why is it only now that I'm actually doing this thing that I realize just how stupid it sounds?"
    "Every shadowy corner looks like a place that some thug could be lying in wait for me."
    "And I can't pass even the most innocent-looking member of staff without thinking they're going to jump me."
    "All of this means that by the time I make it to the manager's office, I'm a bag of nerves."
    "The shabby little man looks up at me as I lean my back against the door to close it behind me."
    "Manager" "Well, well, well."
    "Manager" "What do we have here?"
    "The look of amusement and sleazy anticipation on his face is plain to see."
    "But by now, the trauma of getting here without incident has started to subside."
    "And I can start to feel irate and angry at the mere sight of the man."
    mike.say "Don't get cute with me."
    mike.say "You know full well what I'm here for."
    "The manager nods, holding up his hands in a gesture of conciliation."
    "But all the same, the self-satisfied smirk remains plastered on his face the whole time."
    "Manager" "Okay, okay...don't piss yourself!"
    "Manager" "I never expected you to actually show up with the cash."
    "Manager" "So you're gonna have to excuse me for being a little tickled by all of this."
    $ hero.money -= 10000
    "I shake my head and toss the bag onto the desk before him."
    mike.say "Whatever you say."
    mike.say "I don't really care what you're feeling right now."
    mike.say "Just take the money and tell me this thing is settled."
    mike.say "Then we can each go our separate ways and never see each other again!"
    "The manager laughs, shaking his head at my rough talk."
    "Manager" "Okay, tough guy."
    "Manager" "Just leave the bag and walk out the door."
    "Manager" "As soon as you do that, you can go tell Shiori the good news."
    "He laughs again, clearly enjoying the chance to draw out my torture by even a small length of time."
    "Manager" "Maybe you can ride up on a white horse."
    "Manager" "Disappear off into the sunset together, or something!"
    "I narrow my eyes, instantly suspicious at being dismissed so quickly."
    mike.say "That's it?"
    mike.say "You're not even going to count it?"
    mike.say "Make sure all ten grand is there?"
    "The manager shakes his head again, dismissing my concerns."
    "Manager" "Nah, kid - there's no need."
    "Manager" "You don't strike me as the devious kind."
    "Manager" "And I can always find out where you live..."
    "The manager sits back in his chair, letting the implied threat sink in."
    "I half open my mouth, thinking to fire back some kind of retort."
    "But then the futility of doing so strikes me."
    "And all I want is to get out of there as quickly as I can."
    "This whole business is starting to make me feel utterly sordid and filthy."
    "The sooner I can wash my hands of it all, the better!"
    "I give the manager a nod, but curl my mouth into a half-sneer as I do so."
    "And with that I turn on my heel and walk straight out of the office."
    "I don't stop or even make eye-contact with another human being until I'm out of the club."
    "And even then I keep on walking until I'm well away from the place."
    "All the time my mind is racing as I try to rationalize what I've just done."
    "I've handed ten grand in used notes to a sleazy guy that's up to his eyeballs in vice and depravity."
    "And all on the understanding that he'll be good enough to use it to clear Shiori's debt."
    "I don't know if I'm incredibly brave or unbelievably naive!"
    "And on top of all that, I still have to explain all of this to Shiori herself!"
    "I guess that whatever happens, I'm going to be living in interesting times!"
    if shiori.love.max < 180:
        $ shiori.love.max = 180
    $ shiori.flags.schedule = "default"
    $ shiori.flags.donestripping = True
    return

label shiori_strip_club_manager:
    if shiori.love.max < 170:
        $ shiori.love.max = 170
    show bg stripclub
    "Normally I have a very strict policy of not getting involved in other people's problems."
    "And I definitely have a policy of not getting involved with the criminal element either."
    "As both of those things can be a pain, as well as seriously shortening your lifespan."
    "So it's hard for me to explain just why I feel compelled to make an exception in Shiori's case."
    "I arrive at the strip-club where she's been working early, before the place opens up for the night."
    "There's not many of the staff around, and so no one raises an eyebrow when I slip inside."
    "The place isn't all that large, so finding my way to what passes for the manager's office is pretty easy."
    "I knock once, and then open the door before anyone inside can raise an objection."
    "I'm greeted by a surprised-looking man on the opposite side of an untidy desk."
    "Manager" "Huh?"
    "Manager" "Who in the hell are you?"
    mike.say "I'm here to talk to you - on the subject of the dancers."
    "Manager" "We already auditioned all of the male strippers we need, buddy!"
    "I shake my head hastily."
    mike.say "No, I mean I want to talk to you ABOUT one of the dancers."
    mike.say "Shiori, to be precise."
    mike.say "I want to talk to you about Shiori."
    "The manager raises his eyebrows at this and leans back in his chair."
    "Manager" "Really...is that so?"
    "Manager" "Well, I guess you'd best take a seat then."
    "I nod, sitting down in the uncomfortable chair on my side of the desk."
    "The manager makes no attempt to begin the conversation, just stares at me the whole time."
    "I start to speak and then stop more than once, part of me wondering what on earth I'm doing here."
    mike.say "Actually, it's not just about Shiori."
    mike.say "It's about the debt that she owes."
    mike.say "The debt that her husband left her with..."
    "The manager shakes his head at this, and purses his lips."
    "Manager" "She told you all about that, did she?"
    "Manager" "Bad thing her old man did, running out on her like that, real bad thing."
    "Manager" "Sweet little number like Shiori - no way she should be working in a place like this."
    "I nod again, hoping that the manager's sympathy for her plight might count in my favor."
    mike.say "You're right - she shouldn't be working in a dump like this!"
    "At this, the manager widens his eyes and cocks his head on one side."
    mike.say "Ah...sorry."
    mike.say "I meant dump in a generic sense, you know what I mean?"
    mike.say "No offense intended..."
    "The manager shrugs the insult off as though it were nothing."
    "Manager" "None taken."
    "Manager" "Like I already said, Shiori's too good for this place."
    "Manager" "But I just run the joint, and I can't forgive her debt."
    "Manager" "My job's to see that it's paid back, every last penny and with interest."
    "Sensing my chance, I jump on this last point."
    mike.say "So it doesn't matter how the debt's repaid, just that it is?"
    "Manager" "Come again?"
    mike.say "Just now, you said this was all about repaying the debt, right?"
    "Manager" "Sure, but..."
    mike.say "So if I were to step in and repay the debt on Shiori's behalf?"
    "The manager leans back in his chair, studying me in silence for what feels like an age."
    "But then he narrows his eyes and leans forwards over the desk."
    "Manager" "Now I remember where I've seen you before."
    "Manager" "You've been in here the past couple of nights."
    "Manager" "You're the mysterious guy that's been tipping Shiori so well!"
    "I try not to let this fluster me, thinking that I'm making progress towards my goal here."
    "But I can already feel the paranoia rising in my gut."
    "The fear of being drawn into the same web as Shiori herself."
    "In the end, I hold up my hands and nod."
    mike.say "Sure, yeah - that's me."
    "The manager shakes his head and laughs at me."
    "But then the laughter becomes a racking cough that makes him fight for breath."
    "He holds up a hand to plead for a moment to recover, and then begins to talk again."
    "Manager" "Hey, hey - I'm not judging you, son."
    "Manager" "If you want to be Shiori's white knight, so be it!"
    "Manager" "Take her away from all this and be a better husband than the last guy."
    "I swallow, trying to subdue my nerves as I prepare to ask the question I'm dreading."
    mike.say "So..."
    mike.say "How much does she owe?"
    "Manager" "Ah, now we get down to it!"
    "Manager" "Right now, your little crush owes my employers around five thousand."
    "Manager" "Give or take."
    "I nod, feeling relieved at the size of the figure."
    "Sure, it's not an inconsiderable sum."
    "But if that's all it takes to get Shiori out of this mess, then it's a bargain."
    mike.say "That sounds fair..."
    "Before I can finish, the manager waves a finger at me."
    "Manager" "Uh-uh...not so fast."
    "Manager" "This is a business, son."
    "Manager" "My employers agreed to let Shiori pay off her debt, sure."
    "Manager" "But only because it was on the understanding that would be with interest."
    "Already I can feel my stomach tying itself in knots at his words."
    "I sense a deep and perhaps bottomless hole opening up beneath me."
    mike.say "Alright - how much are we talking here?"
    "The manager smiles, sensing that he's got me just where he wants me."
    "Manager" "As it stands?"
    "Manager" "Hmmm..."
    "Manager" "Ten thousand would put her in the clear."
    "Ten thousand?!?"
    "Oh god - where am I going to find that much money?"
    "I battle to keep my face straight, reminding myself that this is for Shiori's sake, not mine."
    "Soon I feel together enough to nod and open my mouth to speak a coherent string of words..."
    menu:
        "I'll think about it":
            mike.say "Five thousand I could have laid my hands on today."
            mike.say "But ten is going to mean I have to examine my options."
            "The manager puckers his lip again and shrugs."
            "Manager" "You do what you got to do, son."
            "Manager" "I'll still be here when you've made up your mind."
            "Manager" "And so will Shiori - dancing for money off of guys the likes of me..."
            "The manager lets the implied threat hang in the air as I get up and let myself out."
            "All the while the enormity of what I'm getting involved in becomes ever more apparent."
            "What am I thinking, getting myself mixed up with gangsters?"
            "And all for the sake of a girl too!"
        "I'll be back with the money":
            mike.say "Five thousand would have been easier."
            mike.say "But ten will take me longer to lay my hands on."
            "The manager puckers his lip again and shrugs."
            "Manager" "You do what you got to do, son."
            "Manager" "I'll still be here when you've made up your mind."
            "Manager" "And so will Shiori - dancing for money off of guys the likes of me..."
            "The manager lets the implied threat hang in the air as I get up and let myself out."
            "On my way out it's all that I can do to keep from swearing and lashing out in frustration."
            "The mere thought of people like that putting their hands all over Shiori makes me seethe with anger."
    return

label shiori_bruises:
    $ shiori.unhide()
    if shiori.love.max < 160:
        $ shiori.love.max = 160
    show bg office
    "When I make it into the office, I'm pretty much half asleep and not really aware of what's going on around me."
    "I didn't get much sleep the night before, my mind still racing with thoughts of what might have befallen Shiori."
    "This means that I walk in there in a kind of daze, barely acknowledging my co-workers as they wish me a good morning."
    show aletta with moveinleft
    aletta.say "Good morning, [hero.name]."
    mike.say "Huh...hey, Aletta."
    hide aletta with moveoutright
    show audrey with moveinleft
    audrey.say "Rise and shine, boss!"
    if audrey.flags.nickname == "toy":
        mike.say "Yeah, yeah...whatever, Toy."
    else:
        mike.say "Yeah, yeah...whatever, Audrey."
    hide audrey with moveoutright
    show shiori bruised with moveinleft
    shiori.say "Good morning, [hero.name]!"
    mike.say "Oh, hi Shiori..."
    show shiori at right with move
    show shiori at center with hpunch
    mike.say "Wait...what...Shiori!"
    "I almost spin on my heel, totally forgetting the fact that nobody else knows what I do about Shiori's private life."
    "To them she was probably just off sick yesterday and forgot to call in, what with having to juggle her kid as well."
    "So it's no wonder that my over the top reaction earns me a room full of curious stares."
    "Most of all I see Shiori herself staring up at me with a worried look spreading across her face."
    shiori.say "I...ah...I'm sorry, [hero.name]."
    shiori.say "All I said was good morning..."
    "I realize that this is quickly turning into a scene, and that I need to restore some sanity to the situation."
    mike.say "Well...you weren't here yesterday, Shiori."
    mike.say "And...and I wasn't expecting to see you today either..."
    mike.say "You surprised me, that's all!"
    shiori.say "Oh, yes...of course."
    "It's then that inspiration strikes, and I'm quick to leap on the idea before it escapes me."
    mike.say "Also, you didn't call in to let anyone know you weren't coming in, Shiori."
    mike.say "So I'll need to see you about that in my office."
    mike.say "Come and see me when you're ready, okay?"
    shiori.say "Oh...okay."
    hide shiori with moveoutright
    "I don't know if Shiori picks up on the real reason that I want to see her in private."
    "But regardless of whether or not she's slow on the uptake, this seems to have the desired effect on the rest of the office."
    "With the show over, everyone else returns to what they were doing beforehand."
    "All of them sure that I'm just eager to chew Shiori out in private over some petty, bureaucratic bullshit."
    if hero.flags.isceo:
        show bg ceo with fade
    else:
        show bg personal with fade
    "It's not long before I hear the sound of Shiori's knock at the door."
    show shiori bruised with moveinright
    "As she lets herself in, I motion for her to take a seat on the other side of my desk."
    mike.say "Sorry I had to make it seem like I was mad at you just now, Shiori."
    shiori.say "You...you mean you're not?"
    "I look at her with an open mouth, amazed that she could even think I was angry with her."
    mike.say "Of course not, Shiori."
    mike.say "I don't care if you need to take a day off, and to hell with you calling in too."
    mike.say "After what you told me the other day, I was scared stiff something terrible had happened to you!"
    "Now it's Shiori's turn to stare at me open-mouthed."
    shiori.say "You were worried about me - really?"
    "I find myself shaking my head in disbelief at the question."
    "How can she be so surprised to find that I was worried about her well-being?"
    "Does she really think that little of herself that she just assumes nobody cares about her welfare?"
    mike.say "Yes, Shiori."
    mike.say "I've been worried out of my mind."
    "For heaven's sake - it's almost like she expects me to be mad at her for the things she can't help!"
    mike.say "Where were you, Shiori?"
    mike.say "I can't make you tell me if you don't want to."
    mike.say "But knowing what I know, I'm going to be concerned like this whenever something happens to you."
    mike.say "It'd be good for my stress levels if you'd tell me when it really isn't anything serious!"
    "Shiori nods, forcing a pained smile onto her face."
    "I suspect that she's beginning to realize just what taking me into her confidence actually means."
    shiori.say "Okay...okay, [hero.name]."
    shiori.say "The truth is...I...had an accident at my second job."
    "That line would have sounded so innocent and come as such a relief had I not known exactly what Shiori's other job was."
    mike.say "WHAT?!?"
    mike.say "Shiori - what have the bastards done to you?"
    "Shiori looks down at the floor, as if she can't meet my eye for shame as she tells her story."
    shiori.say "They...they said that I was behind with my payments."
    shiori.say "I don't understand how it works, but they insisted that I was."
    shiori.say "Then they said that it was okay, that I could make it up another way..."
    "From the placement of that dramatic pause, I just know what's coming next can't be good."
    shiori.say "They said that if I...slept...with men..."
    shiori.say "They said that would be enough to make it right."
    shiori.say "I said no..."
    "I see that all the time she's telling me this, Shiori's been fingering her arms."
    "She has a thick blouse on, covering almost everything but her neck and hands."
    mike.say "Show me, Shiori."
    mike.say "Take off your top and show me."
    "There's nothing erotic or seductive about what I'm asking her to do."
    "And maybe that's why she obeys without as much as a pause."
    "Or maybe it's because she's already drawn me in too deep to say that it's too much."
    "Either way, I watch as Shiori obliges me, hissing in sympathy at what I see revealed."
    show shiori topless with dissolve
    "The pale skin of Shiori's arms, belly and back are a map of yellow, purple and black bruises."
    "I have no idea how many blows must have fallen or how hard they were when they did."
    "But none of that matters in the slightest, just that she's been assaulted in such a monstrous way."
    mike.say "Put...put your top back on, Shiori."
    mike.say "I've seen enough."
    show shiori -topless with dissolve
    "Shiori does as she's told for the second time, silently and still without meeting my eye."
    "Only when she's fully dressed does she look up and speak."
    shiori.say "What are you going to do now?"
    "I have no idea if she means to simply ask if I'll report this, or if she's actually asking for my help."
    "And the honest truth is that I really don't know myself."
    "I don't relish the thought of getting involved with animals of this kind."
    "But I kind of am involved already, whether I like it or not - Shiori saw to that when she told me all about the ugly mess."
    mike.say "I don't know, Shiori."
    mike.say "But if you'll let me, I'll do what I can to help."
    "Shiori nods and smiles at this, seeming to understand that I don't have any instant answers to her plight."
    "She stands and walks to the door of my office, still clutching at her bruised arms."
    hide shiori with easeoutright
    "Once she's let herself out and I'm alone with my thoughts, I shake my head in a hopeless manner."
    "What in the actual hell am I supposed to do here without getting innocent people hurt...or worse?"
    return

label shiori_work_no_show:
    show bg office
    "I don't normally notice someone not being at their desk when I walk into the office on a morning."
    "I'm not the kind of guy that's a tyrant for punctuality in the workplace kind of thing."
    "And I only tend to get pissed when someone else shirking affects my ability to work too."
    "But what with Shiori's dramatic revelation to me the other day, I guess I'm more sensitive than usual."
    "That's why I note her desk being empty as I walk past it on the way to my office."
    if hero.flags.isceo:
        show bg ceo
    else:
        show bg personal
    "I tell myself that I'm just being paranoid, letting what she told me color what I'm seeing."
    "Even though almost everyone else is at their desks already, she's most likely just running a little late."
    "I sit down at my own desk and try to lose myself in my work, hoping to hear her arrive at any moment."
    "But as the morning wears on with what feels like agonizing slowness, there's still no sign of Shiori."
    "Every time I glance up from my work and through the open door of my office, her desk is deserted."
    "Every time I hear a voice in conversation or answering a phone, it's not her either."
    "Getting ever more concerned, I get up and walk to the door, sticking my head out and looking around."
    show bg office
    show audrey
    if audrey.flags.nickname == "toy":
        mike.say "Toy, have you seen Shiori at all today?"
    else:
        mike.say "Audrey, have you seen Shiori at all today?"
    "Audrey looks up from painting her nails, as if being asked the question is a terrible affront to her dignity."
    show audrey annoyed
    audrey.say "No, I haven't."
    mike.say "Well, did she call in sick or anything?"
    audrey.say "No, she didn't."
    mike.say "Hmm..."
    mike.say "Let me know if she does, okay?"
    audrey.say "Whatever you say, boss!"
    audrey.say "Geez, don't thank me or anything..."
    "I deliberately ignore Audrey's muttered comments, too absorbed in my mounting concern for Shiori."
    hide audrey
    if hero.flags.isceo:
        show bg ceo
    else:
        show bg personal
    "It's getting so bad by now that I can't sit down, and so I start pacing from one side of my office to the other."
    "In the end, I decide that I can't wait any longer, and I need to do something proactive before I freak out."
    "Making sure that my office door is firmly closed, I pull out my phone and dial Shiori's number."
    "I figure that this isn't breaking any of the promises that I made to her about keeping it all secret."
    "No one else can listen in on the phone-call, and if she's fine I can just play the concerned boss."
    play sound phone_calling
    "But, of course, the phone rings until it goes to voicemail."
    shiori.say "Hey, Shiori here!"
    shiori.say "I can't answer the phone right now."
    shiori.say "But leave me a message, and I'll call you right back, I promise!"
    "As soon as the tone passes for me to leave my message, I stammer into the phone."
    "I know I should have tried to sound calm, in case anyone else hears the message."
    "But everything comes pouring out all at once."
    mike.say "HEY...hey...Shiori."
    mike.say "This is [hero.name]...[hero.name] from work."
    mike.say "Just calling to see if you're safe...I mean okay."
    mike.say "Ahh...I don't know what I mean!"
    mike.say "Just...just call me if you get this, okay?"
    "I end the call before I say something even more stupid and clumsy, cursing myself for rushing in and making a mess of it."
    "After that, I leave my phone out on the desk, staring at it every few minutes in the hope of seeing a message from Shiori."
    "But each and every time I do, there's nothing there and my mind just keeps on racing, thinking of all the horrible fates that could have befallen her."
    $ shiori.flags.BruisesDelay = TemporaryFlag(True, 1)
    $ shiori.hide()
    return

label shiori_lapdance_2:
    "I honestly have no idea what to expect as I find myself back in the strip-club where I had Shiori dance for me."
    "But for all I know, Shiori could have begged to change shifts after what happened."
    "Or else she could already have glimpsed me from behind the stage curtain and even now be refusing to go on stage."
    "Of all the possibilities, I think this last one is the most unlikely of all."
    "As what do the disreputable types that own and run a place like this care about Shiori's feelings?"
    "To them, she's nothing more than a piece of meat to make the customers salivate like dogs and spend their money."
    "But then I guess that begs the question - what is she to me?"
    "I don't really know the answer to that, at least not yet."
    "Though I do know that she's far more than a mere piece of meat!"
    "And yet here I am, waiting to treat her in just that same manner..."
    "I try not to think about the implications of that, to push it out of my head."
    "It's no easy task, but it becomes steadily easier as the music begins to play and I wait for Shiori to emerge onto the stage."
    "When she finally does emerge, I can feel my heartbeat quicken at the mere sight of her."
    "Shiori has on the same neon-yellow fishnet outfit as she did the last time."
    "And her face betrays the fact that she's very embarrassed at discovering my presence."
    "But just as before, the eyes of her employers are on her as well as those of the club patrons."
    "Shiori puts on what looks like a brave smile and begins to move in time to the music."
    "Her dancing could not be described as skilled or spellbinding in nature."
    "And yet the awkwardness of her presence on stage begins to make me get hard."
    "Even though she knows that she's expected to come over and dance for me, Shiori takes her time about it."
    "She tries to make a slow, seductive dance out of the whole thing."
    "But in reality, she only really succeeds in making herself look even more nervous and reluctant."
    show shiori lapdance
    "By the time she finally comes close enough to begin dancing for me alone, I've already made a crazy decision."
    "As Shiori takes the notes out of my hand and stuffs then in her thong, I begin to fumble with my flies."
    "There's no way for her to see what I'm doing, as she has her back to me as she dances."
    "Thanks to the sheer size of Shiori's ass, I doubt someone standing right by my seat could either."
    "Shiori starts to shake her buttocks and drop them suggestively towards my lap."
    "But the whole time, she has no idea that my cock is out of my pants."
    "The dance continues, with Shiori teasing as she comes ever closer to me."
    "Several times I have to resist the temptation to reach out and grab her before the time is right."
    "And then, as her buttocks finally pass over the head of my cock, I make my move."
    "Feeling the head of my cock on her ass, Shiori glances over her shoulder in surprise."
    show shiori lapdance worried
    shiori.say "Wha...what's that!"
    "It's at this exact moment that I take a firm hold of her thighs."
    "And then I pull her down and onto me."
    show shiori lapdance fuck
    shiori.say "I...ah...oh..."
    shiori.say "Oh, [hero.name]!"
    "But now it's my turn to be surprised, as my plan becomes reality."
    "I'd been expecting to meet resistance from Shiori, to have to defeat her natural resistance."
    "Instead she's as wet and willing as can be, and my cock slips straight into her pussy."
    shiori.say "Ah...[hero.name]..."
    shiori.say "You're inside of me!"
    shiori.say "You can't be inside of me..."
    shiori.say "Not here..."
    shiori.say "Not where everyone can see!"
    "I'm pretty sure that no one can see what we're doing right now."
    "And Shiori could easily try to pull away from me."
    "Likewise she could raise her voice and call out for help."
    "But instead she keeps her volume down and continues to pretend to dance for me."
    "In fact, if I didn't know better, I'd swear that she was getting ever more turned on by what I'm doing to her."
    shiori.say "Oh, [hero.name]..."
    shiori.say "What are you doing to me?"
    shiori.say "If they find out that I let you do me..."
    shiori.say "I'll be in so much trouble!"
    "If I wasn't listening to her, then at least I could have pleaded ignorance."
    "But the truth is that I can hear each and every word that comes out of her mouth."
    "And it's such a turn-on that I couldn't stop now, even if I wanted to."
    "The feeling of being balls-deep inside of Shiori, in the middle of the club."
    "Having her dancing on my cock while she frets and pleads, fearing the consequences of being caught in the act."
    "Perhaps the only small mercy I can offer is the fact that I'm excited enough for it to be over quickly."
    show shiori lapdance ahegao
    shiori.say "Oh, [hero.name]..."
    shiori.say "Oh my god!"
    "And with that, I lose myself inside of her."
    "Luckily for the both of us, my orgasm is easily mistaken for the climax of Shiori's dance."
    $ shiori.sub += 5
    "I throw my head back, as if exhausted from the thrill of the personal attention she's given me."
    "And at the same time she quakes and shivers, looking for all the world like she's wrapping up the dance."
    show shiori lapdance worried -fuck
    "As my cock slithers out of Shiori, she makes a valiant effort to look like she's still performing."
    "But I can tell from the way that she's clenching her buttocks and thighs that she's preoccupied."
    "She's battling to keep the cum still inside of her from seeping out and running down the inside of her legs."
    "And the thought of her doing that for the rest of the night is almost as hot as the memory of fucking her in public."
    hide shiori
    "I can't keep a wicked smile from spreading across my face as she hurries behind the stage curtain."
    "Whoever else she dances for tonight, Shiori will already have my cum inside of her..."
    if hero.sexperience <= 15:
        $ hero.flags.sexperience += 1
    $ shiori.sexperience += 1
    $ hero.replace_activity()
    return

label get_shiori_lapdance:
    if game.week_day % 2 == 0 and 'shiori_stripclub_lapdance_2' in DONE:
        call shiori_lapdance_2 from _call_shiori_lapdance_repeat_2
    else:
        call shiori_stripclub_lapdance_1 from _call_shiori_lapdance_repeat_1
    return

label shiori_blackmail_confession:
    show shiori blush
    if shiori.love.max < 150:
        $ shiori.love.max = 150
    "Shiori looks at me with a serious expression."
    shiori.say "You know that it's just Kanta and me."
    shiori.say "But you don't know how we ended up like that."
    show shiori normal
    "I shake my head, agreeing that I know almost nothing of the grim little details of the situation."
    "If I'd thought about it at all, I guess my assumption was pretty much based on the obvious."
    "I just took it for granted that the kid's father knocked her up and never took responsibility."
    "Or straight up walked out and left her holding the baby, in the literal sense."
    shiori.say "Kanta's father, he was a very...controlling man."
    shiori.say "He was the one that took care of the money, the bills, everything."
    shiori.say "I was happy with that, didn't care about those things, so long as we were happy."
    show shiori sad
    shiori.say "But one day, Kanta's father just..."
    shiori.say "He just didn't come home, and I guessed soon after that he was never going to come home again."
    "As I listen to Shiori tell her story, I notice that she refuses to call the guy her husband, or even her partner."
    "Is she only referring to him as the father of her son because she's still in so much pain over his abandoning them?"
    shiori.say "I had to start looking after everything, and it was scary."
    shiori.say "Kanta was always asking when Daddy would be coming home."
    shiori.say "And I had no idea what to tell him..."
    "At the mention of her son, Shiori looks like she's going to break down again."
    show shiori annoyed
    "But then she makes a visible effort to steal herself and continues on with her story."
    shiori.say "Then, one day, men in suits came to the door."
    shiori.say "They told me that they were friends of Kanta's father, that they had played cards and gambled together."
    shiori.say "They told me that he had disappeared while owing them money, and that I had to pay them back somehow."
    shiori.say "I told them that I was sorry, but I had no money."
    shiori.say "And they said that it was okay, that I could work for them to pay off the debt."
    show shiori angry
    "Shiori looks up and straight into my eyes, fear and shame clear to be seen on her face."
    shiori.say "I'm not stupid, [hero.name]."
    shiori.say "I know that they're gangsters, or something of that kind."
    shiori.say "And I have no idea what they think I owe them, or if they'll ever let me pay it off."
    shiori.say "If it weren't for Kanta, I wouldn't care what they did to me."
    show shiori sad
    shiori.say "But if I don't do as they say, I'm scared that they'll hurt my son."
    mike.say "I see, Shiori."
    mike.say "That's...that's quite a bind to be in!"
    "Yeah, I know that statement sounds pretty stupid after all that Shiori's just told me."
    "But how can I hope to process the fact my co-worker's being blackmailed by mobsters in a matter of mere minutes?"
    mike.say "Like I already said, Shiori - I won't breathe a word of this to anyone."
    mike.say "Nothing you've told me since will change that, I promise."
    mike.say "Just be sure to let me know if I can help."
    mike.say "And go to the police if these people threaten you or your son, please!"
    show shiori happy
    "Getting up and turning to go, Shiori nods at me and smiles."
    shiori.say "Thank you [hero.name], I'll think about it."
    hide shiori with moveoutleft
    "I return the smile as Shiori closes the door behind her."
    "But the moment I'm alone, the enormity of what she's told me truly starts to sink in."
    "What in the hell has she gotten herself tangled up in?"
    return

label shiori_stripclub_lapdance_1:
    if shiori.love.max < 140:
        $ shiori.love.max = 140
    "After the first time I went along to the strip-club and saw Shiori there, I told myself I'd never go back."
    "But here I am, sitting in the front row and feeling the sensation of my heart, pounding away in my chest."
    "To tell the truth, I don't honestly know why I came back here at all."
    "There was just some masochistic urge that seemed to make me want to do it."
    "I know that I should be better than this, that I should want to do all I can to get Shiori away from this place."
    "But there was just something about the way she looked at me the first time I was here."
    "That and the utterly helpless way she came to me afterwards and told me everything in confidence."
    "I don't know, maybe I just can't get enough of her when she's vulnerable and humiliated?"
    "And I also don't know what that says about me, either!"
    "As I sit right in front of the stage, bills clutched in my sweaty palm, I try not to think about all of that."
    "But as soon as the lights change and the music starts up for Shiori's dance, I forget everything else in an instant."
    "Now all I can see is Shiori, as she walks slowly onto the stage."
    "She has on the same outfit of neon blue fishnets as she did the last time I saw her here."
    "And on her face is the same look of discomfort I remember so well."
    "I can already feel myself getting hard at the mere sight of her."
    "But what really gets me going is what happens when she recognises me a moment later."
    "Shiori quails visibly, almost beginning to shake with apprehension."
    "I make a point of waving the bills in my hand for all to see, and then gesturing at my lap."
    "Shiori glances over her shoulder, shaking her head at someone that I can't see."
    "The exchange must be both swift and silent, as the shake soon turns into an embarrassed nod."
    show shiori blush
    "She makes her way over to where I'm sitting, trying and failing to turn the short walk into part of her dance."
    "I hold out the bills, and Shiori takes them as she's supposed to, stuffing them into the waistband of her thong."
    show shiori lapdance
    "She shyly smiles at me as she runs her hands through my hair."
    "And yet everything that she's doing is turning me on all the more."
    "Shiori whips off her top, letting her huge breasts bounce free."
    "And then she pushes them into my face, almost smothering me in the act."
    "With my head practically buried in her cleavage, I only feel the sensation of Shiori sitting astride my thighs."
    "Despite the awkward situation I've deliberately chosen to put her in, she doesn't hold back."
    "I feel her pushing herself against me, rubbing her entire body against mine."
    "My hands grab hold of her ample thighs as she grinds her groin into me."
    "I can only guess that Shiori's using her chest to keep me from looking her straight in the face."
    "But how can I complain when the feeling of having my features buried in her cleavage feels so good?"
    "A moment later, I feel one of her nipples brush against my lips."
    "Unable to resist the temptation, wrap my lips around it and begin to suck."
    "I hear Shiori let out a genuine moan of surprise and arousal."
    "She tries to pull free, making me bite down gently on her nipple."
    "At this, she lets out a cry of pain, and I take this as a signal to release her."
    "As soon as she stands up, I expect nothing more than for her to bolt backstage."
    "But I must not have had my money's worth yet, as she turns her back on me and bends over."
    "Shiori pushes her backside into my face, jiggling her round buttocks as she does so."
    "And then she lowers them onto my lap once again, grinding into me from behind."
    "Her movements are faster and more frantic now, as if she's trying to get through this as soon as possible."
    "But the effect is the same, and the weight of her buttocks on my already swollen cock is entirely predictable."
    "I cum in my shorts as Shiori slows down and comes to a stop."
    hide shiori
    "She must know what she's done to me as she hurries back onto the stage."
    "And yet she makes no effort to as much as glance over her shoulder as she flees the scene."
    "Instead she leaves me alone, sitting in the mess that I've made of myself."
    "I have no idea whether I should be pleased or ashamed over what I've just done."
    "And I certainly have no idea what I'll say to Shiori when I next see her in the office either..."
    return

label shiori_stripclub_confession:
    $ shiori.flags.schedule = "stripclub"
    if shiori.love.max < 130:
        $ shiori.love.max = 130
    "The truth is that I don't think I could actually get my head down and work."
    "At least not until I've had the chance to speak to the specific colleague that I'm looking out for."
    "Obviously it's Shiori, on account of where I saw her last time and just what she was doing there."
    "I have no doubt whatsoever that she'll make a beeline for me as soon as she gets into work."
    "No matter the embarrassment she must be feeling right now, she'll be convinced that she has to confront me about it."
    "Otherwise she runs the risk of me telling someone else in the company, maybe even someone in HR..."
    "And so I sit there, sipping my coffee and waiting."
    "All the time the images of what I saw last night are on my mind."
    "I'm worried that I'll never be able to imagine Shiori any other way than naked from now on..."
    play sound door_knock
    "Just then, I hear a timid knock at the door to my office."
    show shiori sad at top_mostleft with dissolve
    "Looking up, I'm not at all surprised to see Shiori standing there, eyes downcast and wringing her hands before her."
    "She looks awful, her skin not its natural shade of pale, but white and washed out."
    "Her eyes are red and puffy, as though she's been crying the whole night through instead of sleeping."
    shiori.say "H...hello...[hero.name]."
    shiori.say "I...wondered if you could..."
    shiori.say "If I could..."
    "I don't think I've ever seen Shiori in a state like this before."
    "Sure, I've seen her worked up and fretting over something dumb or petty."
    "But here and now she looks like she's right on the brink of doing something desperate!"
    mike.say "Of course I have time to see you, Shiori."
    mike.say "You come right on in and close the door behind you."
    mike.say "That way we can be sure of some privacy, okay?"
    "It's not like what I say is enough to make Shiori brighten up and become a regular little sunbeam."
    "But all the same, she seems to pick up on the warmth in my voice and my sympathy for her."
    show shiori normal
    "She manages a weak smile and a quick nod, hastily closing the door behind her."
    show shiori at center, zoomAt(1.5, (640, 1040)) with fade
    pause 0.5
    show shiori at center, zoomAt(1.5, (640, 1140)) with ease
    "Shiori sits down on the other side of the desk, accepting the coffee I pour for her without a word."
    "That alone is enough to tell me she's out of sorts, the lack of her usual humble nature and good manners."
    "We endure a couple of minutes of awkward silence, punctuated only by the sound of her slurping coffee."
    "And then Shiori finally tries to speak."
    shiori.say "I...I think I need to explain..."
    shiori.say "Make a couple of things clear..."
    mike.say "It's okay, Shiori."
    mike.say "Trust me, I won't tell a soul."
    shiori.say "That's very kind of you, [hero.name]."
    shiori.say "But I..."
    mike.say "No, Shiori - no buts."
    mike.say "This is the twenty-first century, for god's sake."
    mike.say "A lot of people have a second job these days."
    mike.say "Granted, it's not usually doing...well...what you do."
    mike.say "But it's not like this company can tell you how to live your life."
    mike.say "That's your choice..."
    "Shiori takes me by surprise then, shaking her head and beginning to wail."
    show shiori sad
    shiori.say "But, [hero.name] - it's not my choice, none of it is!"
    mike.say "Shiori, what are you talking about?"
    mike.say "I...I don't understand!"
    shiori.say "Of course you don't."
    shiori.say "I tried to explain, but you wouldn't let me!"
    "As Shiori continues to wail, I realise that she's right."
    "I've been trying so hard to play the caring, woke boss that I haven't let her get a word in edgeways."
    mike.say "Okay, Shiori, go ahead - tell me what you feel I should know."
    mike.say "I won't interrupt, I promise."
    "Shiori nods, her wails subsiding into sniffling and the occasional sob."
    shiori.say "I'm not dancing in that...place...because I want to."
    shiori.say "You have to understand that, [hero.name], I'm not that type of girl!"
    shiori.say "I do it because I have to, because I need the money so very badly..."
    "I nod with what I hope is visible sympathy."
    "I have the urge to add that I'm not the kind of guy that normally goes to that kind of place."
    "But I've promised to let Shiori have her say, and so I keep that to myself."
    shiori.say "I know this is my own problem, [hero.name]."
    shiori.say "And I promise that it won't interfere with my work here."
    "Instinctively, I reach over the desk and place my hand over Shiori's in what I hope is a reassuring gesture."
    "I'm far more gratified than I expected to be when she doesn't flinch or try to pull her hand away."
    show shiori normal
    mike.say "Like I already said, Shiori - I won't breathe a word of this to anyone."
    mike.say "Nothing you've told me since will change that, I promise."
    mike.say "Just be sure to let me know if I can help."
    show shiori happy at center, zoomAt(1.5, (640, 1040)) with ease
    pause 0.5
    show shiori happy at center, zoomAt(1.5, (440, 1040)) with ease
    "Getting up and turning to go, Shiori nods at me and smiles."
    shiori.say "You're a good boss, [hero.name], thank you."
    hide shiori with easeoutleft
    "I return the smile as Shiori closes the door behind her."
    "But the moment I'm alone, the enormity of what she's told me truly starts to sink in."
    "What in the hell has she gotten herself tangled up in?"
    return

label shiori_stripclub:
    "Mostly I don't pick up on what the guys around me are saying, as it's all the usual stuff."
    "Comments on the relative charms of the girls that are up and dancing."
    "What they'd like to do with them or to them given the chance."
    "You know the kind of lines guys come out with in that kind of place, right?"
    "Things that they'd never dream of saying anywhere else, even when wasted."
    "All of it washes over me, that is until I hear a couple of words here and there that pique my curiosity."
    "Shady guy" "Whoa - look at the tits on this one!"
    "Shady guy" "Yeah...in case of an emergency, she doubles as a flotation device!"
    "I shake my head in amusement at the predictable nature of the comments."
    "But all the same, I still turn around to see for myself the anatomy that could have inspired them."
    "And when I do, my jaw drops open and my eyes go wide with disbelief at what I'm seeing."
    show poledance shiori with fade
    "Tottering out onto the stage before me is an undoubtedly pretty girl, with a figure that is almost too good to be true."
    "All she's wearing is a top, thong and leg-warmers of matching, cyan fishnet material with a pair of high heels of the same colour."
    "This means that every inch of her pale skin is visible, right down to the deep red of her cheeks as she blushes before the crowd."
    "It's Shiori - I can't believe what I'm seeing, but it's definitely her!"
    "I watch, almost spellbound, as she reaches the pole on the stage and slowly begins to dance."
    "It's slow at first, as if playing on the natural vulnerability that shows in almost every aspect of her being."
    "But as she eases into the routine, I see Shiori start to lose herself in the sound of the music and movement."
    "Though all the while she's up there, I never once see her look completely at ease."
    "It's almost as if a part of her cannot let go of the awkwardness and shame she feels at what she's doing."
    "Not that the rest of the crowd in which I'm standing seems to be sensitive to that fact."
    "Or maybe they are, their cheers and shouts of encouragement fuelled by enjoyment of her discomfort."
    "And what about me?"
    "I'm just as fixated on Shiori right now as anyone else in the place."
    "But unlike the rest of the baying patrons around me, I'm feeling torn right down the middle."
    "I watch as Shiori pulls her top off over her head."
    "The motion makes her large, heavy breasts rise and fall."
    "Even before they've bounced for the first time, I can already feel myself getting hard at the sight."
    "And as she starts to move, wrapping herself around the pole, all I want is to reach out and touch her."
    "I'd like to be able to say that it's to scoop Shiori up and carry her away from this place, to save her."
    "But the truth is that I want her as much as anyone else in the place right now!"
    "I've never seen Shiori's body move like this before."
    "She tosses her head, making her thick, black hair fly."
    "Her breasts bounce and sway in time to her movements, nipples erect and hard the whole time."
    "And as she pauses, bending over to shake her backside at the crowd, she also inches down her thong."
    "Now stripped almost completely naked in front of a room packed with baying strangers, Shiori starts to bring her dance to a close."
    "Hands clapping onto her buttocks, she thrusts her breasts out towards the crowd, as if inviting them to be touched."
    "Then she takes them in her palms, massaging and squeezing them like handfuls of fleshy dough."
    "Shiori stands there, naked on the stage and demeaning herself for the gratification of her audience."
    "Part of me knows that I should be feeling sympathy for her as a colleague, and maybe even a friend."
    "But I'm ashamed to say that all I have on my mind at that moment in time is my own desire to fuck her."
    "It's just then, as Shiori bows forwards and shoves her exposed breasts towards the crowd for one last time, that it happens."
    "The lights are bright on the stage and dull out here in the audience, so it must be tough for her to see any of the faces in the crowd."
    "But some random trick of the light and where I just happen to be standing means that we both look up at exactly the right moment."
    "Our eyes meet, and I see Shiori gasp as she recognises me."
    "She freezes for a moment as she does this, and time seems to stop for me too."
    "Luckily the rest of the crowd simply assumes that she's letting them get their money's worth as they stare at her."
    "And then, just like that, we both snap back to reality."
    "I watch as Shiori snatches up the few items of clothing she stripped off, trying to cover herself for the first time."
    hide shiori with fade
    "Then she turns and flees the stage, tottering dangerously atop her high heels as she goes."
    "No one in watching seems to care about the speed and haste with which she leaves."
    "But then why would they?"
    "They've seen all that they wanted to see already."
    "And if her turn on the stage is over, then all the better to get the next girl up there and dancing."
    "I spend the rest of the time that we're in the strip club almost in a state of shock at what I've just seen."
    "Luckily for me, people are used to seeing guys in such a place with a bewildered look on their face."
    "So no one as much as bats an eyelid as I try to reconcile the sweet, slightly bumbling girl from my office with the act I just saw on stage."
    "I knew that Shiori had a second job, and that she probably needs it to make ends meet."
    "Life's tough for a single parent these days, no question about that."
    "Though I never dreamed that she could be doing something like this on the side!"
    "I don't know what the fallout of my discovering Shiori's secret double life as a stripper might ultimately be."
    "But I am sure that the office is going to be very interesting indeed..."
    return

label shiori_birthday_date_male:
    $ DONE["shiori_birthday_date_male"] = game.days_played
    $ game.active_date.clothes = "casual"
    scene bg cinema
    show shiori casual normal
    with fade
    "Normally going to the movies is a relaxing experience for me."
    "It's a time to lose myself in a film and forget about the real world."
    "But being here with Shiori seems to be having the opposite effect."
    "We're supposed to be here to celebrate her birthday."
    show shiori sad
    "Yet she hasn't stopped worrying and looking at her phone since we left her place."
    "And now that we're in the lobby, she's doesn't show any sign of stopping."
    shiori.say "Ooh..."
    shiori.say "Maybe I should just give them a call?"
    shiori.say "Just to be sure Kanta's okay?"
    shiori.say "I have the babysitter's number right here."
    shiori.say "And she did say it was fine to call her..."
    "I turn around from the poster I'm studying to look at Shiori."
    "And I see that she's already pulling out her phone."
    show shiori embarrassed at startle
    "She only just stops before beginning to dial the number."
    "A guilty smile on her face at being caught in the act."
    menu:
        "Let Shiori call the babysitter":
            "Sure, it's pretty annoying that Shiori's so paranoid about Kanta."
            "But the kid's all she's got in the world, and he was on the scene before I was."
            "So what right do I have to get on her case about it?"
            "Better for me to support her as best I can."
            mike.say "I'm sure Kanta's fine, Shiori."
            show shiori normal
            mike.say "The sitter would have called us if he wasn't."
            mike.say "But call her if it'll make you feel better."
            mike.say "We can spare the time."
            show shiori smile
            pause 0.5
            show shiori normal at top_mostright with ease
            "Shiori nods and turns away to make the call."
            show shiori with fade
            "It takes her about a minute or two to wrap it up."
            show shiori happy at center with ease
            "And then she turns back to me, a look of relief on her face."
            shiori.say "He's fine!"
            $ game.active_date.score += 15
            show shiori normal
            shiori.say "But thanks for letting me call."
            shiori.say "At least I can relax now!"
        "Do not let Shiori call the babysitter":
            if shiori.is_collared:
                "I shoot Shiori a disapproving look."
                "And that seems to do the trick."
                "She hastily put her phone away."
                "And then she stares down at her feet."
                shiori.say "I..."
                $ game.active_date.score += 5
                shiori.say "I'm sorry, master."
            else:
                "I can't believe she's actually doing this to me!"
                "And she's smothering her kid at the same time."
                "He's never going to be able to stand on his own two feet at this rate."
                "I roll my eyes at Shiori."
                show shiori sad
                "And then I fix her with a hard stare."
                mike.say "Put your phone away, Shiori."
                mike.say "You and I both know that he's fine."
                mike.say "If he wasn't, the babysitter would have called us by now."
                show shiori embarrassed
                "Shiori opens her mouth, as if she's going to argue."
                show shiori sad
                "But I harden my stare, and it seems to do the trick."
                $ game.active_date.score -= 10
                "She nods demurely and puts her phone away."
    "That matter taken care of, Shiori joins me to look at the posters in the lobby."
    "I decided not to choose a film before we got here, so Shiori could have some input."
    "But I can see that she's in danger of being overwhelmed by the sheer amount of choice!"
    "And I can't really blame her, because all of the posters are as loud as they can be."
    "Every one of them screaming that we should choose them over all the others."
    mike.say "Anything leap out at you, Shiori?"
    mike.say "Fancy a rom-com, or a thriller?"
    show shiori normal
    "Shiori's still glancing from one poster to another."
    "But then I see her eyes settle on one in particular."
    show shiori surprised
    shiori.say "Ooh..."
    shiori.say "Sirens and Serenity!"
    show shiori happy
    shiori.say "I'd like to see that one."
    shiori.say "I read the book - it's a historical romance, with mermaids too!"
    show shiori smile
    "That doesn't sell itself to me, I have to say!"
    show shiori normal
    mike.say "What about the new Space Wars film, Shiori?"
    mike.say "It's set before the original trilogy."
    mike.say "And it tells you what went on before them too!"
    show shiori sad
    "It doesn't look like I've sold my ideal choice to Shiori either."
    shiori.say "Oh I don't know, [hero.name]."
    show shiori normal
    shiori.say "Maybe you should choose?"
    "I shrug and then nod."
    "If that's what she wants."
    menu:
        "Choose Sirens and Serenity":
            "I could just say, fuck it, and choose Space Wars."
            "And I'm pretty sure that Shiori would go along with it."
            "But we are supposed to be here for her birthday."
            "So I'd be a jerk to just indulge myself."
            show shiori surprised
            mike.say "Let's see Sirens and Serenity, Shiori."
            mike.say "It's not my kind of thing."
            mike.say "But if you like it, then I'm sure it'll be great."
            $ game.active_date.score += 15
            show shiori happy
            "Shiori's smile is instant and genuine."
            "And it makes me feel pretty good too."
            "So everyone wins."
        "Choose Space Wars":
            if shiori.is_collared:
                show shiori embarrassed
                shiori.say "What am I thinking!"
                show shiori smile
                shiori.say "Of course you should choose, master!"
                "I nod and treat Shiori to an approving smile."
                "Which instantly makes her entire face light up."
                mike.say "We'll see the Space Wars film, Shiori."
                $ game.active_date.score += 5
                mike.say "And well done for knowing your place."
            else:
                "Ah, screw it - everyone loves Space Wars!"
                mike.say "Space Wars it is, Shiori!"
                mike.say "Let's go buy our tickets."
                show shiori sadsmile
                "Shiori nods and smiles at this."
                $ game.active_date.score -= 10
                "But I can see that she's less than pleased."
                "Not that she's about to say anything about it."
                "Well, maybe she'll speak up for herself in future."
    show shiori casual normal at center, zoomAt(1.5, (640, 1040)) with fade
    "With the film decided on and the tickets bought, you know what's next."
    "And that's buying snacks before the film starts."
    show shiori sad
    "But Shiori doesn't seem that keen as we walk over to the counter."
    mike.say "What's up, Shiori?"
    mike.say "Don't you want a snack to take into the film?"
    show shiori annoyed
    "Shiori shakes her head and looks concerned."
    shiori.say "I'd like to, [hero.name]."
    shiori.say "But the prices here are crazy!"
    "I look at the prices next to the drinks and snacks."
    "And I have to admit, Shiori's not kidding."
    "But that doesn't mean I don't want to buy something."
    menu:
        "Suggest that you and Shiori share":
            mike.say "How about we compromise, Shiori?"
            mike.say "I get a drink and something to eat."
            mike.say "And then we share it?"
            show shiori normal
            "Shiori nods, apparently happy with the idea."
            $ game.active_date.score += 15
            shiori.say "That sounds like a better idea, [hero.name]."
            shiori.say "Then I don't have to feel guilty."
            show shiori happy
            shiori.say "Because I don't have to finish it all by myself."
            show buy popcorn shiori with fade
            "That decided, we step up to the counter and place our order."
            "It doesn't take long for our purchases to turn up."
            "And then we're all set to go."
        "Buy yourself something and not Shiori":
            if shiori.is_collared:
                show shiori smile
                shiori.say "Of course you should buy whatever you want, master."
                shiori.say "I would never presume to tell you how to spend your money."
                show buy popcorn shiori with fade
                "I nod and step up to the counter, ordering what I want."
                "And as soon as I have it, I hand the lot over to Shiori."
                mike.say "Carry these for me, Shiori."
                mike.say "But don't eat or drink anything."
                mike.say "Not until I give you permission to."
                $ game.active_date.score += 5
                "Shiori takes the refreshments and nods meekly."
            else:
                mike.say "Whatever, Shiori."
                mike.say "If you think it's too much, then that's fine."
                mike.say "But it's not going to stop me from buying something."
                $ game.active_date.score -= 10
                show buy popcorn shiori nogirl with fade
                "I walk over to the counter and place my order."
                "Which leaves Shiori to stand and watch."
                "Then I return with my purchases in my hands."
                hide buy popcorn with fade
                mike.say "Okay..."
                mike.say "Let's go!"
                "Sure, it looks a little awkward."
                "But I gave Shiori a straight choice."
    scene bg cinemaroom
    show shiori casual at center, zoomAt(1.5, (640, 1040))
    with fade
    "Shiori and I make our way to the screen that's showing our film."
    "And it looks like we've made it in good time too, as it's not started yet."
    "All we need to do now is find our seats."
    "Then we can get settled down and wait for the film to start."
    $ randevent = randint(1, 3)
    if randevent == 1:
        mike.say "Row C..."
        mike.say "Seats nine and ten..."
        mike.say "You see them, Shiori?"
        shiori.say "I think so, [hero.name]!"
        show shiori surprised at startle
        shiori.say "Oh!"
        "I walk up behind Shiori, trying to see what's made her stop."
        show shiori zorder 3 at center, zoomAt(1.5, (440, 1040)) with ease
        show victor as first_guy zorder 1 at center, zoomAt (1.0, (780, 940)), blacker
        show ryan tux smile as second_guy zorder 2 at center, zoomAt (1.0, (1080, 940)), blacker
        with dissolve
        "And looking over her shoulder, I can see two guys sitting in our seats."
        mike.say "Erm..."
        mike.say "I think you're in our seats, guys!"
        "They look up at me slowly."
        "And I can see a total lack of concern on their faces."
        "First Guy" "So what?"
        "Second Guy" "I don't see your names on them!"
        show shiori sad
        "Shiori gives me a pleading look."
        "Evidently she expects me to sort this thing out."
        if hero.charm >= 50:
            mike.say "Don't worry about it, Shiori."
            mike.say "These seat suck anyway."
            mike.say "The ones over there are much better..."
            "I turn and point to the seats I mean."
            show shiori normal
            "And Shiori makes to start in their direction."
            show victor as first_guy at center, zoomAt (1.0, (780, 780)), blacker
            show ryan tux smile as second_guy at center, zoomAt (1.0, (1080, 780)), blacker
            with ease
            "First Guy" "Whoa, whoa, whoa..."
            "First Guy" "Hold on a second!"
            "Second Guy" "Yeah, you guys are supposed to be sitting here!"
            "Second Guy" "If those seats are better, then we're taking them!"
            hide victor as first_guy at center, zoomAt (1.0, (780, 780)), blacker
            hide ryan tux smile as second_guy at center, zoomAt (1.0, (1080, 780)), blacker
            with moveoutright
            "I shrug and move aside as the two guys hurry to grab the other seats."
            show shiori at center, zoomAt(1.5, (640, 1040)) with ease
            "Then Shiori and I sit down in our seats."
            show shiori sad
            shiori.say "I'm sorry, [hero.name]..."
            shiori.say "Now we have to put up with the worse view!"
            mike.say "No we don't, Shiori."
            mike.say "I lied - these seats are the better ones."
            mike.say "But by the time those guys find out, it'll be too late to argue!"
            show shiori surprised
            "Shiori looks at me in amazement."
            show shiori happy
            $ game.active_date.score += 15
            "But then she giggles and leans her head on my shoulder."
            shiori.say "Oh, [hero.name]!"
            show shiori joke
            shiori.say "You're so wicked!"
            hide shiori
            show watch movie happy shiori
            with fade
            pause 1.0
        else:
            mike.say "My name might not be on it."
            mike.say "But I've got a ticket with that number, dipshit!"
            show shiori surprised at startle
            "Shiori gasps as I give the guys as good as I'm getting."
            "But the problem is that they don't seem to be biting."
            "Instead they just share a knowing glance and shake their heads."
            "First Guy" "Go pick a fight somewhere else, buddy."
            "First Guy" "I want to watch the film."
            "Second Guy" "You heard the man."
            "Second Guy" "Only a jerk starts a fight over a cinema seat!"
            "I'm about to fire back."
            show shiori sad at startle
            "But then I feel Shiori grabbing my arm."
            shiori.say "They're right, [hero.name]."
            shiori.say "It's not worth it!"
            shiori.say "Come on - there are two seat over there!"
            show shiori at center, zoomAt(1.5, (640, 1040))
            hide victor as first_guy
            hide ryan tux smile as second_guy
            with fade
            "I let Shiori drag me away, feeling frustrated at having to let it drop."
            $ game.active_date.score -= 10
            "But also feeling like a loser for getting aggressive in the first place too."
            hide shiori
            show watch movie happy shiori
            with fade
            pause 1.0
    elif randevent == 2:
        show watch movie happy shiori with fade
        "We're about halfway through the film, and I'm really into it."
        "And whenever I steal a glance at Shiori, she's just as absorbed."
        "In fact the entire audience seems to have their eyes glued to the screen."
        "Which makes it all the more jarring when Shiori suddenly leans over."
        "Then she hisses into my ear suddenly and without warning."
        hide watch movie
        show shiori angry blush
        with hpunch
        shiori.say "Arrgh..."
        shiori.say "Ouch, ouch, ouch!"
        "After jumping out of my skin, I whisper back."
        mike.say "Shiori!"
        mike.say "What the hell's the matter?!?"
        show shiori sad
        shiori.say "It's my foot..."
        shiori.say "It's gone to sleep!"
        shiori.say "I have...pins and needles!"
        mike.say "Okay, okay..."
        mike.say "Sit still and I'll see what I can do."
        if hero.has_skill("massage"):
            "I slide out of my chair and onto the floor."
            "And as soon as I'm down there, I pull off Shiori's shoe."
            "I don't leap straight into it, instead I take a moment."
            "And I use that time to figure out exactly where the problem is."
            "That means I know where to start and where I'm going."
            show shiori normal
            "The result is that it doesn't take long for Shiori to feel relief."
            "I know that's the case too, as her foot relaxes in my hands."
            "And I can hear her letting out quiet sighs of relief too."
            "Before long, she's moving her foot like there's no problem."
            "So I just add a little more rubbing for good measure."
            "Then I put her shoe back on and climb into my chair."
            "As soon as I'm back on eye-level with Shiori, I lean in close."
            "And I whisper to her."
            mike.say "Is that better?"
            mike.say "Are you okay now?"
            show shiori smile
            "Shiori nods and gives me a smile."
            shiori.say "Yes."
            shiori.say "Much better now."
            show shiori normal
            $ game.active_date.score += 15
            shiori.say "Thank you!"
        else:
            "I slide out of my chair and onto the floor."
            "And as soon as I'm down there, I pull off Shiori's shoe."
            "That done, I set to work rubbing away at it."
            "I give it all I've got, really trying to work the muscles."
            show shiori sadsmile
            "At first, Shiori seems to react in a positive way."
            "She starts to wriggle her foot and then her toes."
            "So I redouble my efforts, convinced I'm doing well."
            show shiori angry at startle
            "But then I feel her leg stiffen and her gasp in pain."
            "When she tries to pull it away from me, I hold on."
            "Because I'm still sure that I can do some good."
            with vpunch
            "But all this gets me is a kick in the stomach a moment later."
            "Winded and gasping for breath, I haul myself off the floor."
            "And I flop back into my chair, looking at Shiori in amazement."
            shiori.say "Nice going..."
            "She whispers through gritted teeth."
            show shiori annoyed
            $ game.active_date.score -= 20
            shiori.say "Now I have a cramp too!"
    elif randevent == 3:
        show watch movie happy shiori with fade
        "We're well into the film, and I'm enjoying it immensely."
        "But when I glance over at Shiori, she seems to be frowning."
        "This puzzles me, and it makes me wonder if she's having a good time."
        "Which is important to me, as I'm treating her on her birthday."
        "So I lean over and whisper in her ear."
        hide watch movie
        show shiori sad
        with fade
        mike.say "What's the matter, Shiori?"
        mike.say "You don't like the film?"
        "Shiori shakes her head."
        show shiori embarrassed
        shiori.say "Oh dear..."
        shiori.say "It's not that, [hero.name]."
        shiori.say "I like it - but I'm confused!"
        shiori.say "Who is that man in the hat again?"
        shiori.say "And what is he doing?"
        if hero.has_skill("bookworm"):
            "I take a quick glance at the screen, to see who Shiori's talking about."
            "And the moment I do so, I can see where the confusion must have come from."
            mike.say "Oh yeah..."
            mike.say "Don't worry about it, Shiori."
            mike.say "They explained it better in the book."
            mike.say "He's a traitor that sold them all down the river in the past."
            show shiori normal
            $ game.active_date.score += 15
            "Shiori nods as the light of understanding grows in her eyes."
            "She turns her attention back to the screen."
            "And I do the same, thankful that all of my reading finally turned out to be of use."
        else:
            "I stare at the screen for a moment."
            "And then I realise that I haven't got a clue either."
            "So all I can do is shrug and confess as much to Shiori."
            mike.say "Erm..."
            mike.say "I dunno, Shiori!"
            mike.say "Maybe if I'd read the book before I saw the film?"
            $ game.active_date.score -= 10
            "Shiori looks at me with a helpless expression on her face."
            "And then she turns her attention back to the screen."
            "Part of me hopes it's because she's trying to figure it out for herself."
            "But if I'm honest, it's more likely she's trying to spare me any further embarrassment."
    scene bg cinemaroom with fade
    "About halfway through the film, the screen fades to black."
    "And then the lights in the theatre come back on."
    show shiori casual surprised at center, zoomAt(1.5, (640, 1040)) with dissolve
    "Shiori blinks and looks around in surprise."
    shiori.say "Huh?"
    shiori.say "What's happening?"
    shiori.say "Is there something wrong with the film?"
    "I glance around and see an usher holding a tray of refreshments come through the door."
    mike.say "No, Shiori..."
    mike.say "It looks like they're just having an interval, that's all."
    mike.say "I guess it's a chance to sell more popcorn!"
    show shiori normal
    "Shiori nods, but then a thought seems to occur to her."
    shiori.say "You know what, [hero.name]..."
    show shiori smile
    shiori.say "This would be a perfect time to surprise someone."
    shiori.say "Don't you think?"
    "For a moment I wonder what Shiori's talking about."
    "But then it hits me - we're out celebrating her birthday."
    "So she must be fishing to see if I bought her a gift."
    if not hero.has_gifts:
        if shiori.is_collared:
            mike.say "I don't think I like your tone, Shiori."
            mike.say "Sounds to me like you're demanding something from me."
            mike.say "That wouldn't be the case, would it?"
            show shiori sad
            "Shiori's face drops as she realises the mistake she's made."
            "And the next moment she starts to grovel in the hope of making it up to me."
            shiori.say "No, master..."
            shiori.say "Of course not!"
            shiori.say "Please, forget I said anything at all!"
        else:
            "Ah hell..."
            "I knew there was something that I meant to do."
            "It was pick up a birthday present for Shiori!"
            "Now I'm going to have to talk my way out of this mess."
            mike.say "I guess so, Shiori."
            mike.say "Intervals are almost unheard of these days."
            mike.say "I wonder if anyone's going to take advantage of the opportunity?"
            "I glance around, trying to distract attention from my own screw-up."
            "Shiori keeps on looking at me, with hope in her eyes."
            show shiori sadsmile
            "But little by little, I see if fade into nothing."
            show shiori annoyed
            $ game.active_date.score -= 20
            "Until she lets out a little sigh and shakes her head."
            "Looks like she's going to let the matter drop."
            "But I still feel like a jerk all the same."
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_18
        if _return != "done":
            if _return not in ["None", "exit"]:
                mike.say "Oh yeah, Shiori..."
                mike.say "Like, it'd be the perfect time to give someone a present, yeah?"
                "I produce Shiori's gift as I say this."
                "And I'm delighted to see her face light up."
                show shiori happy
                shiori.say "Oh, [hero.name]!"
                shiori.say "Thank you so much!"
                play sound [paper_ripping_2, paper_ripping_1]
                "Shiori takes the gift from be and begins to unwrap it."
                if _return:
                    "But as soon as she sees what's inside, her expression changes."
                    "Shiori can't hide the amazement she's feeling."
                    "Instead she shakes her head and gasps at her gift."
                    $ game.active_date.score += 20
                    shiori.say "Oh, [hero.name]!"
                    shiori.say "This is too much."
                    shiori.say "I don't deserve something like that!"
                    "I shake my head and smile."
                    mike.say "You're wrong, Shiori."
                    mike.say "That's exactly why you do deserve it!"
                else:
                    show shiori sadsmile
                    "But as soon as she sees what's inside, her expression changes."
                    "Shiori can't hide the disappointment she's feeling."
                    "All the same, she tries her best to sound grateful."
                    $ game.active_date.score -= 10
                    shiori.say "Oh..."
                    shiori.say "Thank you, [hero.name]."
                    show shiori normal
                    shiori.say "That's...that's very nice."
                    "All I can do is nod and try to change the subject."
                    "Anything to escape the feeling of embarrassment that's coming over me right now."
            else:
                if shiori.is_collared:
                    mike.say "I don't think I like your tone, Shiori."
                    mike.say "Sounds to me like you're demanding something from me."
                    mike.say "That wouldn't be the case, would it?"
                    show shiori sad
                    "Shiori's face drops as she realises the mistake she's made."
                    "And the next moment she starts to grovel in the hope of making it up to me."
                    shiori.say "No, master..."
                    shiori.say "Of course not!"
                    shiori.say "Please, forget I said anything at all!"
                else:
                    "Ah hell..."
                    "I knew there was something that I meant to do."
                    "It was pick up a birthday present for Shiori!"
                    "Now I'm going to have to talk my way out of this mess."
                    mike.say "I guess so, Shiori."
                    mike.say "Intervals are almost unheard of these days."
                    mike.say "I wonder if anyone's going to take advantage of the opportunity?"
                    "I glance around, trying to distract attention from my own screw-up."
                    "Shiori keeps on looking at me, with hope in her eyes."
                    show shiori sadsmile
                    "But little by little, I see if fade into nothing."
                    show shiori annoyed
                    $ game.active_date.score -= 20
                    "Until she lets out a little sigh and shakes her head."
                    "Looks like she's going to let the matter drop."
                    "But I still feel like a jerk all the same."
    show watch movie happy shiori with fade
    "Soon enough the film resumes and we're engrossed in it once more."
    "Shiori and I become lost in the narrative, swept away by the story."
    "And before we know it, the last scene plays out and the credits roll."
    hide watch movie
    show shiori casual normal
    with fade
    "As soon as that happens, Shiori starts to gather her things."
    mike.say "What are you doing, Shiori?"
    show shiori surprised
    shiori.say "Huh?"
    shiori.say "I'm getting ready to go."
    shiori.say "Isn't it over?"
    mike.say "What about the post-credit scene?"
    shiori.say "Is there one?"
    mike.say "I don't know."
    mike.say "But I won't unless we sit through the credits!"
    show shiori sad
    "Shiori doesn't look convinced by this argument."
    "In fact, I can see that she wants to get moving."
    menu:
        "Forget about the post-credit scene":
            "I take one last, longing look at the screen."
            "And then I nod my head and start to get up."
            mike.say "Okay, Shiori..."
            mike.say "Let's go."
            show shiori surprised
            "Shiori looks a little surprised at my decision."
            "I think she was expecting me to dig my heels in on this one."
            shiori.say "Are you sure, [hero.name]?"
            mike.say "Yeah, I'm sure."
            mike.say "I can probably see it online anyway."
            show shiori normal
            $ game.active_date.score += 15
            "Shiori nods happily, and we make our way out of the theatre."
        "Make Shiori stay for the post-credit scene":
            if shiori.is_collared:
                mike.say "Sit down and be quiet, Shiori."
                mike.say "We'll leave when I say so."
                mike.say "And not a second before!"
                "The harshness of my tone seems to do the trick."
                "Shiori practically jumps in her chair."
                $ shiori.sub += 2
                "But she nods and looks down at her feet."
                "And I don't hear another word from her until after the scene is done."
            else:
                "I shake my head and cross my arms over my chest."
                "Then I make a point of settling back into my seat."
                mike.say "You leave if you want, Shiori."
                mike.say "But I'm staying put!"
                show shiori annoyed
                $ game.active_date.score -= 10
                "Shiori rolls her eyes in disgust."
                "But then she flops back into her own seat."
                "And it seems like she's resigned to letting me have my way."
                "Once the scene is done, I have to admit it wasn't all I'd hoped for."
                "But I feel like I have to big it up in order to save face."
                "Then we finally get up and leave the theatre together."
    scene bg cinema
    show shiori casual normal
    with fade
    "Once we're back in the lobby, I feel that odd detachment that comes after sitting through a film."
    "The strange realisation that you've been immersed in a fantasy and that this is actual reality."
    "What snaps me back to myself is the sight of Shiori once again checking her phone for messages."
    show shiori happy
    shiori.say "Phew!"
    shiori.say "It's okay - no emergencies!"
    mike.say "No news is good news!"
    show shiori normal
    mike.say "So..."
    mike.say "What happens now, Shiori?"
    mike.say "It's not that late, you know?"
    if game.active_date.score >= 80 and shiori.sexperience >= 1:
        "Shiori seems to think about it for a moment."
        "She even looks down at her phone."
        "Which makes me think she's going to want to go home."
        "But then an unusual look comes over her face."
        "And it takes me a moment to realise that it's one of rebellion!"
        show shiori joke
        shiori.say "You're right, [hero.name]."
        shiori.say "And since Kanta's fine, we should stay out a little longer."
        show shiori flirt at center, zoomAt(1.5, (640, 1040))
        shiori.say "Come on - let's go have some real fun!"
        "I can't describe the joy I feel as Shiori grabs my hand."
        "And I don't hesitate to follow her as she leads me away."
        "I don't know where we're headed."
        "But her giggles tell me I'm going to like it when we get there."
        call shiori_birthday_sex from _call_shiori_birthday_sex
    else:
        show shiori sadsmile
        "Shiori gives me a helpless smile."
        "But she also shakes her head."
        shiori.say "I know Kanta's okay."
        show shiori normal
        shiori.say "But I really should be getting back to him all the same."
        "I nod, knowing that I shouldn't argue the point."
        "Pushing back when it comes to Shiori's kid wouldn't be a good idea."
        mike.say "Okay, Shiori..."
        mike.say "Let's see about getting you a taxi..."
        "Sure, it's not the way I'd have liked for the date to end."
        "But sometimes you've just got to cut your losses."
        "And make sure you try harder next time around."
        scene bg black with dissolve
    return

label shiori_birthday_sex:
    "By now I've come to think that I know Shiori pretty well."
    "We worked together before we even started to think about dating."
    "And in that time I came to think of her as a sweet and innocent girl."
    "The kind that you'd have to coax to even admit that she liked sex."
    "And that you'd probably have to get drunk for it to actually happen."
    "That means I'm expecting Shiori to want to come back to my place after our date."
    "Or at least for me to take her somewhere that's nice and private for it to happen."
    "Which is why it comes as such a shock when she drags me down a deserted corridor at the cinema."
    show bg publicbathroom with hpunch
    "And then pushes me through the door of a small bathroom that's hidden back there too!"
    "The first time that I get to stop and collect myself is when Shiori lets go of my hand."
    "And she only does that in order to lock the door behind us."
    mike.say "Whoa..."
    mike.say "Slow down, Shiori!"
    mike.say "What's gotten into you?"
    mike.say "You're not usually as forward as this!"
    show shiori at center, zoomAt(1.65, (640, 1140))
    "Shiori answers me with a hand placed in the middle of my chest."
    "Then she uses it so shove me backwards with a surprising show of strength."
    show bg publicbathroom at center, dark
    show shiori at center, zoomAt(1.25, (640, 940))
    with hpunch
    "Caught off-balance, I stagger back and into the cubicle surrounding the toilet."
    show shiori at center, zoomAt(1.5, (640, 1040))
    "And Shiori follows me in there, not letting up for a second."
    show shiori normal blush
    shiori.say "I don't know, [hero.name]."
    shiori.say "I don't know what's gotten into me."
    show shiori flirt -blush
    shiori.say "All I do know is what I want to get in me."
    show shiori blush
    shiori.say "And that's you!"
    "I can tell you that I'm just not ready for this."
    "In my mind Shiori's still the shy girl that need to be taken by the hand."
    "And now here she is, practically pouncing on me in a public bathroom!"
    "A moment later, she's literally that, leaping at me without warning."
    hide shiori
    show shiori kiss casual
    with fade
    $ shiori.flags.kiss += 1
    "Shiori wraps her arms around my neck and her legs around my waist."
    "Her weight sends me crashing into the wall of the cubicle."
    "And I have to use all of my strength to keep from toppling over."
    "Not that any of that seems to stop Shiori, not even for a second."
    "Instead she claps her lips over mine and pushes her tongue into my mouth."
    "Now let me get one thing straight here."
    "I might be talking about being surprised and staggered."
    "But there's no way I'm complaining about it."
    "And I'm not asking Shiori to stop - quite the opposite!"
    "I return that kiss with almost as much passion as Shiori gives it with."
    "And I'm not just struggling to hold her up, I'm embracing her for all I'm worth."
    "At the same time I can feel Shiori's hands going to work."
    hide shiori
    show shiori at center, zoomAt(1.65, (640, 1140))
    with fade
    "First they tug desperately at her own panties, pulling them down."
    "That done, their attention turns to unzipping my flies."
    "I have no idea how Shiori manages this."
    "Especially when she can't see what the hell she's doing."
    show shiori naked with dissolve
    "But somehow she succeeds, and I feel her fingers around my cock."
    "Shiori pretty much yanks it out of my pants in one move."
    "And she's not wasting any time once she has it in her grasp either."
    "Shiori pushes the head hard against the lips of her pussy."
    hide shiori
    show shiori lapdance publicbathroom naked
    with fade
    "The kiss breaks as we both gasp at the sensation."
    "But it only becomes more intense as gravity comes into play."
    "I'm hard by now, and Shiori's getting more excited by the second."
    "When hard meets soft, we begin to melt into each other."
    "And then Shiori's weight does the rest of the work for us."
    "I'm deep inside of her before I know it, almost overwhelmed by the sensation."
    "For her own part, Shiori tightens her grip on me, clinging on for dear life."
    "But the moment that I can go no deeper, sheer instinct takes over."
    "From that point on, I don't have to ask what Shiori wants."
    "Because it's the exact same thing that I want too."
    "Pushing her against the wall, I begin to thrust with my groin."
    show shiori lapdance fuck
    "And as there's nowhere for her to go, she takes everything I have to give."
    shiori.say "Mmm..."
    shiori.say "Y..yes..."
    shiori.say "Please..."
    shiori.say "Just like that!"
    "It's at times like these when I'm glad to be a regular at the gym."
    "Not to mention that Shiori's, shall we say, well-built too."
    "Because it means that I have the strength not only to hold her up."
    "But also the stamina to keep on pounding her as I do so."
    "And the fact that she's sturdily built means that Shiori can take it too."
    "In fact, anyone that didn't know her as well as I do wouldn't see anything else."
    "They'd just see Shiori passively taking all that I can give her."
    "But I know for sure that's not the case."
    "Shiori's not just taking all that she's given."
    "She's swallowing it down and demanding more with each second that passes!"
    "The more I thrust into her, the more she pushes her weight down onto me."
    "The more I try to move inside her, the tighter she holds me."
    "Sure, on the outside, Shiori's sweet and demure, almost timid."
    "But there's a deep and powerful need inside of her."
    "One that she needs to satisfy by any means possible."
    "Shiori's riding me every bit as much as I'm fucking her right now."
    "And I'm sure that if I were to stop, she'd go right on regardless."
    "I can feel my heart pounding in my chest, my breath coming in gasps."
    "Yet I can't even think about slowing down, never mind stopping."
    "For all the talk of what Shiori needs, there's also my desire to give it to her."
    "Somehow pleasing her is almost more important to me than my own needs."
    "I know that I won't be able to let go until I'm sure she's fulfilled."
    "That's why I keep right on going, making love to Shiori with all my might."
    "And I don't stop until she starts to wriggle and wail in my arms."
    show shiori lapdance ahegao
    shiori.say "Ah..."
    shiori.say "Oh god..."
    shiori.say "So good..."
    shiori.say "You're going to make me..."
    "Shiori doesn't have to finish what she was trying to say."
    $ shiori.sexperience += 1
    "Because I can already feel her starting to cum."
    with vpunch
    "And as her pussy squeezes my cock, she takes me with her."
    with vpunch
    "I push against the wall with all of my remaining strength."
    with vpunch
    "Holding Shiori there as we both ride out our orgasms."
    "Her head flops and then falls onto my shoulder."
    "And I feel Shiori go as limp as a rag doll in my arms."
    "As gently as I can, I relax my arms and sit down on the toilet."
    "Then I sit there with her on my lap, waiting for us both to recover."
    "I just hope nobody heard what we were just doing in here."
    "And that no one needs the bathroom before we're ready to leave."
    $ hero.cancel_activity()
    $ game.pass_time(2)
    scene bg black with dissolve
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
