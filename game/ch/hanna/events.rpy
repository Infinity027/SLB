init python:
    Event(**{
    "name": "hanna_masturbate",
    "label": "hanna_masturbate",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("hanna_event_01"),
        IsHour(10, 17),
        HeroTarget(
            IsGender("male"),
            IsActivity("take_a_shower_gym"),
            IsRoom("gymlockers"),
            MinStat("fitness", 30),
            ),
        ],
    "gallery": {'character':'hanna', 'label':'hanna_masturbate', 'id':'Masturbate', 'icon': 'hanna mast', 'scene': 'gym'},
    "music": "music/roa_music/purple.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "hanna_event_02",
    "label": "hanna_event_02",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("hanna_masturbate"),
        HeroTarget(
            IsGender("male"),
            IsActivity("buymembership"),
            IsRoom("gymreception"),
            MinStat("fitness", 30),
            ),
        ],
    "music": "music/roa_music/purple.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "hanna_event_03",
    "label": "hanna_event_03",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("hanna_event_02"),
        HeroTarget(
            IsGender("male"),
            IsActivity("take_a_shower_gym"),
            IsRoom("gymlockers"),
            MinStat("fitness", 40),
            ),
        PersonTarget(hanna,
            HasRoomTag("gym"),
            Not(IsHidden()),
            MinStat("love", 40),
            ),
        ],
    "gallery": {'character':'hanna', 'label':'hanna_event_03', 'id':'Shower BJ', 'icon': 'hanna bj outfit', 'scene': 'gym'},
    "music": "music/roa_music/purple.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "hanna_event_04",
    "label": "hanna_event_04",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("hanna_event_03"),
        IsHour(6, 10),
        HeroTarget(
            IsGender("male"),
            IsActivity("run_park"),
            HasRoomTag("park"),
            MinStat("fitness", 50),
            ),
        PersonTarget(hanna,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 60),
            ),
        ],
    "music": "music/roa_music/purple.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "hanna_event_05",
    "label": "hanna_event_05",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("hanna_event_04"),
        HeroTarget(
            IsGender("male"),
            IsRoom("gym", "gymmachine"),
            MinStat("fitness", 70),
            ),
        Or(
            HeroTarget(IsActivity("train_hard", "train")),
            And(
                HeroTarget(IsActivity("train_with")),
                PersonTarget(hanna,
                    IsActive(),
                    ),
                ),
            ),
        PersonTarget(hanna,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 80),
            ),
        ],
    "music": "music/roa_music/purple.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "hanna_event_06",
    "label": "hanna_event_06",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("hanna_event_05"),
        HeroTarget(
            IsGender("male"),
            MinStat("fitness", 80)
            ),
        PersonTarget(hanna,
            IsActive(),
            MinStat("love", 100),
            ),
        ],
    "music": "music/roa_music/purple.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "hanna_event_07a",
    "label": "hanna_event_07a",
    "duration": 1,
    "priority": 500,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasRoomTag("gym")),
        PersonTarget(hanna,
            IsActive(),
            IsFlag("gymSolution", "lend"),
            MinStat("love", 120),
            ),
        ],
    "music": "music/roa_music/purple.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "hanna_event_07b",
    "label": "hanna_event_07b",
    "duration": 1,
    "priority": 500,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasRoomTag("gym")),
        PersonTarget(hanna,
            IsActive(),
            IsFlag("gymSolution", "lewd"),
            MinStat("love", 120),
            ),
        ],
    "music": "music/roa_music/purple.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "hanna_event_07c",
    "label": "hanna_event_07c",
    "duration": 1,
    "priority": 500,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasRoomTag("gym")),
        PersonTarget(hanna,
            IsActive(),
            IsFlag("gymSolution", "sell"),
            MinStat("love", 120),
            ),
        ],
    "music": "music/roa_music/purple.ogg",
    "do_once": True,
    })

    AfterDateEvent(**{
    "name": "hanna_event_08",
    "label": "hanna_event_08",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("hanna_event_07b"),
        HeroTarget(
            IsGender("male"),
            ),
        MinDateScore(50),
        PersonTarget(hanna,
            OnDate(),
            MinStat("love", 140),
            ),
        ],
    "music": "music/roa_music/purple.ogg",
    "clothes": "date",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "hanna_event_08a",
    "label": "hanna_event_08a",
    "priority": 1000,
    "duration": 1,
    "conditions": [
        IsDone("hanna_event_07a"),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(hanna,
            IsActive(),
            MinFlag("repay", 3),
            MinStat("love", 160),
            IsFlag("event_delay", False)
            ),
        ],
    "music": "music/roa_music/purple.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "hanna_event_09",
    "label": "hanna_event_09",
    "priority": 1000,
    "duration": 1,
    "conditions": [
        IsDone("hanna_event_08"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_stripclub")),
        PersonTarget(hanna,
            OnDate(),
            Or(
                IsFlag("sexydate"),
                IsFlag("sluttydate"),
                ),
            MinStat("love", 160),
            ),
        ],
    "music": "music/roa_music/purple.ogg",
    "clothes": "sexydate",
    "do_once": True,
    })

    Event(**{
    "name": "hanna_event_10",
    "label": "hanna_event_10",
    "priority": 1000,
    "duration": 1,
    "conditions": [
        IsDone("hanna_event_09"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("gym")),
        PersonTarget(hanna,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 170),
            ),
        ],
    "music": "music/roa_music/purple.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "hanna_event_11",
    "label": "hanna_event_11",
    "priority": 1000,
    "duration": 1,
    "conditions": [
        IsHour(10, 16),
        IsDone("hanna_event_10"),
        HeroTarget(
            IsGender("male"),
            IsRoom("house")),
        PersonTarget(hanna,
            Not(IsHidden()),
            MinStat("love", 180),
            ),
        ],
    "music": "music/roa_music/purple.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "hanna_event_10a",
    "label": "hanna_event_10a",
    "priority": 1000,
    "duration": 1,
    "conditions": [
        IsDone("hanna_event_09a"),
        MinDateScore(50),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(hanna,
            IsPresent(),
            OnDate(),
            Not(IsHidden()),
            MinStat("love", 200),
            IsFlag("engagedmike", False),
            ),
        ],
    "music": "music/roa_music/purple.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "hanna_gym_profits_pay",
    "label": "hanna_gym_profits_pay",
    "conditions": [
        IsDone("hanna_gym_profits"),
        PersonTarget(hanna,
            IsActive(),
            MaxFlag("repay", 3),
            IsFlag("repay_delay", False),
            ),
        ],
    "music": "music/roa_music/purple.ogg",
    "do_once": False,
    })

    Event(**{
    "name": "hanna_gym_profits",
    "label": "hanna_gym_profits",
    "conditions": [
        IsDone("hanna_event_07a"),
        IsNotDone("hanna_gym_profits_alternate"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate())
            ),
        PersonTarget(hanna,
            IsPresent(),
            Not(IsHidden()),
            HasRoomTag("gym"),
            MinStat("love", 140)
            ),
        ],
    "music": "music/roa_music/purple.ogg",
    })

    Event(**{
    "name": "hanna_gym_profits_alternate",
    "label": "hanna_gym_profits_alternate",
    "do_once": True,
    "conditions": [
        IsDone("hanna_event_07b"),
        IsNotDone("hanna_gym_profits"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate())
            ),
        PersonTarget(hanna,
            IsPresent(),
            Not(IsHidden()),
            HasRoomTag("gym"),
            MinStat("love", 180),
            MinStat("sub", 75)
            ),
        ],
    "music": "music/roa_music/purple.ogg",
    })

    Event(**{
    "name": "hanna_gym_bj",
    "label": "hanna_gym_bj",
    "once_week": True,
    "max_girls": 1,
    "conditions": [
        IsDone("hanna_event_07b"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("train_with"),
            ),
        PersonTarget(hanna,
            IsPresent(),
            Not(IsHidden()),
            IsRoom("gym", "gymmachine"),
            MinStat("love", 150),
            MinStat("sub", 50)
            ),
        ],
    "music": "music/roa_music/purple.ogg",
    })

    Event(**{
    "name": "hanna_preg_talk",
    "label": "hanna_preg_talk",
    "do_once": False,
    "music": "music/roa_music/purple.ogg",
    "conditions": [
        IsHour(6, 15),
        HeroTarget(
            IsGender("male"),
            Or(
                HasRoomTag("street"),
                HasRoomTag("park"),
            ),
            Not(OnDate())),
        PersonTarget(hanna,
            IsPresent(),
            IsFlag("toldpreg", False),
            MinCounter("pregnant", 6),
            Not(IsHidden()),
            ),
        ],
    "music": "music/roa_music/purple.ogg",
    })

    Event(**{
    "name": "hanna_sub_event_01",
    "label": "hanna_sub_event_01",
    "do_once": True,
    "conditions": [
        IsDone("hanna_event_07b"),
        HeroTarget(HasRoomTag("gym")),
        PersonTarget(hanna,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "music": "music/roa_music/purple.ogg",
    })

    Event(**{
    "name": "hanna_sub_event_02",
    "label": "hanna_sub_event_02",
    "do_once": True,
    "conditions": [
        IsDone("hanna_sub_event_01"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_livingroom")),
        IsTimeOfDay("evening"),
        MinDateScore(90),
        PersonTarget(hanna,
            OnDate(),
            MinStat("sub", 90),
            IsFlag("collared"),
            ),
        ],
    "music": "music/roa_music/purple.ogg",
    })

label hanna_preg_talk:
    scene expression f"bg {game.room}"
    show hanna a blush sweat sport
    with fade
    hanna.say "Hey...hey, [hero.name]...hey there!"
    "My head snaps around in time to see Hanna, obviously out jogging and coming straight towards me."
    "I was never a fan of Baywatch back in the day, but she seems to run slow-motion as she approaches all the same."
    "Her shorts show off her shapely legs, her chest sways with the motion of her body, and her hair bounces around her face like a blonde halo."
    "Do I sound like I'm reeling off the virtues of a goddess at all?"
    "If so, then what do I care?"
    "She looks stunning, full stop."
    show hanna wink a at center, zoomAt(1.5, (640, 1040)), startle
    mike.say "Oh, hi, Hanna."
    "She stops just before me, bending over to rest her hands on her thighs and catch her breath for a moment."
    show hanna normal a
    "Having to watch her spandex shorts stretch as she does so is such a chore to endure!"
    show hanna normal b
    "She stands up and stretches a little more, so close that I can feel the heat, smell the perspiration coming off of her body."
    "It's weird how normally another person's sweat normally freaks me out."
    "But with her, it's somehow sexy - like she's giving off a pheromone, or something."
    show hanna normal a
    hanna.say "I must have jogged past here every day for months now."
    hanna.say "How come I've never seen you before?"
    hanna.say "You work around here, right?"
    hanna.say "I remember you saying so."
    mike.say "Yeah, in that building, right there."
    mike.say "Normally I've got so much on that I eat lunch at my desk."
    show hanna surprised at center, zoomAt(1.5, (640, 1040)), startle
    "Hanna shakes her head in disbelief, the idea that no sane person would allow themselves to be chained to a desk all day implicit in her eyes."
    show hanna normal
    hanna.say "But today, you managed to escape?"
    mike.say "Yeah, I guess you could say that."
    mike.say "And ran into you - so I guess you could call it fate!"
    show hanna annoyed
    "I can see from the way her expression changes that the joke fell far short of the mark."
    "But I can't tell for the life of me why."
    hanna.say "Well...maybe you might want to think about whether or not you believe that later."
    mike.say "What...why, Hanna?"
    hanna.say "There's something that I've been meaning to tell you for a while now."
    "Oh shit, here we go."
    hanna.say "I'd been trying to think of the right moment and spot, but nothing came to mind."
    hanna.say "So I guess, as fate made us meet at random, here and now is as good of a place and time as any."
    mike.say "Hanna, you're scaring me a little - are you trying to tell me that you want to break up or something?"
    show hanna normal
    hanna.say "[hero.name], no...god no...not that!"
    hanna.say "But it's almost as serious, I guess."
    mike.say "Aww, hell...just tell me, please?"
    "Hanna pauses to look around for a moment, as if steeling her nerves before she speaks again."
    hanna.say "Well, [hero.name]...here goes - I'm pregnant."
    "I feel like someone just snuck up and hit me in the gut with a sledgehammer."
    mike.say "You...you're sure?"
    hanna.say "As I can be - I took the test a couple of days ago, and it was positive."
    hanna.say "That's why I've been off the radar recently."
    hanna.say "I had to get my head round it before I told you."
    hanna.say "So - what are we going to do?"
    "Part of me feels mad that Hanna took so long to get her own head straight, but then dumped this on me in the street with no prior warning."
    "But then this is as serious as she says it is, and getting petulant and mad isn't going to make it any easier in the long run."
    menu:
        "You should have a termination":
            $ hanna.love -= 10
            mike.say "Jesus, Hanna - I'm not ready for this!"
            hanna.say "Look, I know I kinda just dropped this whole thing on you, and it's big."
            hanna.say "If you want time to think, maybe we could meet up tonight?"
            mike.say "No, Hanna, you don't understand."
            mike.say "What I mean to say, is that I'm not ready to be a parent - not at all!"
            hanna.say "But..."
            mike.say "And I don't think you are, either."
            show hanna sad
            "Hanna looks instantly devastated, as though she's desperately trying to think up a counter to my argument."
            mike.say "I don't just mean emotionally either."
            mike.say "My job has me wound up so tight that I might snap, and I still live in a house that I have to rent rooms in to make ends meet."
            mike.say "Your dad might own the gym, but neither of us wants to sponge off of him, do we?"
            hanna.say "So you think that we...that we should..."
            "She can't even bring herself to say the word, so I have to do it for her."
            mike.say "A termination, Hanna - yes, I think we have to get a termination."
            "Hanna's huge blue eyes begin to shed genuine, heartfelt tears."
            hide hanna
            show hanna sad blush sweat sport at center, zoomAt(2.0, (640, 1340))
            with fade
            "I embrace her, right there in the street."
            "Having to say that out loud was tough, but I genuinely think, under the circumstances, it was the best thing for the both of us."
            $ hanna.unpreg()
        "We should keep it":
            $ hanna.love += 10
            mike.say "Hanna, you should have told me the moment that you knew!"
            hanna.say "Oh geez, [hero.name] - you're not mad at me, are you?"
            mike.say "What?"
            mike.say "No, Hanna...I'm...I'm...the other thing...you know?"
            hanna.say "Happy?"
            mike.say "Yes, Hanna - I'm really, really happy!"
            show hanna happy
            "Hanna looks more startled than happy herself."
            hanna.say "Oh god, I really thought you were going to get mad...or tell me to get rid of it!"
            mike.say "No...why would I do that?"
            hanna.say "Well, that's why I took so long to tell you."
            hanna.say "First I was worried you wouldn't want it, or that you wouldn't want me anymore."
            hanna.say "Then I thought about how stressed you always are with your job, and how mine's no better..."
            mike.say "Fuck the jobs, Hanna - I don't mind scrubbing toilets if it means I can be with you...and our baby!"
            mike.say "All that's just minor details, and we'll work something out, just like people have been doing since the dawn of fucking time!"
            hide hanna
            show hanna happy blush sweat sport at center, zoomAt(2.0, (640, 1340))
            with hpunch
            "Hanna throws her arms around me, almost crushing the air out of my lungs."
            "She's crying, but I'm sure that they're tears of relief and, I hope, happiness."
            $ hanna.flags.toldpreg = True
    hide hanna
    show hanna sport blush sweat
    with fade
    "Eventually, I have to call time on our embrace and get back to the office."
    "Hanna looks a bit of a mess, with tears still staining her cheeks."
    "But she assures me that she's fine, and we agree to meet up later that evening to discuss things further."
    "As hard as work was to deal with this morning, I think it's going to be that much worse this afternoon, with those revelations kicking around inside of my head."
    return

label missed_hanna_event_09a(from_cancel=False):
    if not from_cancel:
        "I missed my date with Hanna."
        $ hanna.love -= 10
    $ DONE.pop("hanna_event_09a", None)
    $ hero.calendar.add(game.days_played + 1, DateAppointment(20, "hanna", "Date at restaurant (Hanna)", "hanna_event_09a", "missed_hanna_event_09a"))
    $ storytracker.refresh()
    return

label hanna_event_08a:
    if hanna.love.max < 180:
        $ hanna.love.max = 180
    show hanna
    with fade
    "It's been a while since Hanna told me all about the problems that the gym was facing."
    "And I still feel gratified that she let me put up the money for a loan to help her out."
    show hanna at center, zoomAt(1.5, (640, 1040)) with fade
    "So when she brings the subject up, I'm pretty interested in hearing what she has to say."
    hanna.say "Oh, yeah..."
    show hanna happy
    hanna.say "I meant to tell you I have good news!"
    mike.say "You do?"
    hanna.say "Mm-hmm..."
    hanna.say "The gym's back on track now."
    hanna.say "In fact it's doing better than ever."
    "I nod and smile, genuinely happy to hear of the change in Hanna's fortunes."
    "And I deliberately don't make mention of the loan as she tells me her news."
    "Because that would pretty much make me look like a total bread-head!"
    mike.say "That really is good news, Hanna!"
    mike.say "I thought you seemed happier than you have in a while."
    mike.say "This proves you're a pretty good businesswoman."
    show hanna blush
    "Hanna shakes her head and gives me a knowing glance."
    "It's a rare thing for her to look so coy."
    "And I'm reminded of just how cute she actually is."
    show hanna wink
    hanna.say "Oh come on, [hero.name]..."
    hanna.say "Stop trying to flatter me."
    hanna.say "And stop being so modest too."
    hanna.say "Actually, just stop being modest - you can flatter me all you like!"
    show hanna normal -blush
    "Hanna makes a visible effort to be more serious."
    "And she takes hold of my hand as she does so."
    hanna.say "Now, [hero.name]..."
    hanna.say "We both know that it was all down to your loan."
    hanna.say "Sure, I might have had some ideas that worked."
    hanna.say "But without your money, I couldn't have kept the doors open."
    "I wave a hand in the air, still trying to play it down."
    mike.say "In was just helping out a friend, Hanna."
    mike.say "You'd have done the same thing in my place."
    "I feel Hanna's grip on my hand tighten."
    "And she looks me straight in the eye."
    show hanna flirt
    hanna.say "Oh, I think we're more than friends, [hero.name]."
    hanna.say "And I want to take you out to say thanks."
    hanna.say "How about dinner at a nice restaurant?"
    hanna.say "My treat!"
    menu:
        "This is a date!":
            mike.say "There's no need to thank me, Hanna."
            mike.say "But if you want to buy me dinner, then that's fine by me!"
            show hanna happy
            "Hanna smiles and nods her head."
            "Happy to be getting her own way."
            $ hanna.love += 2
            hanna.say "Awesome!"
            hanna.say "I know the perfect place."
            hanna.say "Trust me, you're going to love it!"
            mike.say "I'm sure I will."
            $ hero.calendar.add(game.days_played + 3, DateAppointment(20, "hanna", "Date at restaurant (Hanna)", "hanna_event_09a", "missed_hanna_event_09a"))
        "It's fine Hanna, you don't need to":
            mike.say "I'm up for us going to eat somewhere nice, Hanna."
            mike.say "But I don't want you to have to pay for it on your own."
            show hanna sad
            "Hanna frowns at this."
            hanna.say "But why not?"
            hanna.say "I can afford it now the gym is doing better."
            hanna.say "And I want to thank you."
            mike.say "It's just this thing I have about being rewarded for good deeds, Hanna."
            mike.say "Like if I accept, it makes me feel as if I'm cashing in on doing the right thing."
            "Hanna looks more than a little confused and put out by my answer."
            "But nonetheless, she nods in agreement."
            hanna.say "Okay..."
            hanna.say "We'll go out somewhere."
            show hanna normal
            hanna.say "But we'll split the bill, okay?"
            mike.say "It's a deal."
            show hanna happy
            "Hanna cheers up a little now the matter is settled."
            "But I'm still worried that she doesn't really understand my reasons."
            $ hanna.flags.event_delay = TemporaryFlag(True, 7)
            $ hero.cancel_event()
            $ hanna.love -= 4
    return

label hanna_gym_profits_pay:
    show hanna
    hanna.say "I got something for you [hero.name]."
    mike.say "Oh?"
    show hanna happy
    hanna.say "Here's some of the money I owe you."
    $ hero.money += 1000
    $ hanna.flags.repay += 1
    $ hanna.flags.repay_delay = TemporaryFlag(True, 30)
    mike.say "Thanks Hanna."
    return

label hanna_gym_profits:
    if hanna.love.max < 160:
        $ hanna.love.max = 160
    scene bg gym
    show hanna
    with fade
    "I can see from the look on Hanna's face that she has something to tell me."
    "And her smile also hints that it's going to be something that I want to hear."
    "So I can't help smiling in return as she walks up right up to me."
    "Hanna cocks her head on one side and raises her eyebrows."
    show hanna happy
    hanna.say "Hey, [hero.name]!"
    hanna.say "I've been looking for you."
    mike.say "Really, Hanna?"
    mike.say "It's not like I'm hard to find, is it?"
    mike.say "I mean, you could have just called me!"
    show hanna normal
    "Hanna lets out a snort of breath and shakes her head."
    "And I can see that I'm in serious danger of spoiling her mood."
    "Clearly she wants me to play along, so I do just that."
    mike.say "Okay, Hanna, okay..."
    mike.say "I'm intrigued - why were you looking for me?"
    "Hanna's smile is perhaps a little less enthusiastic that it was a moment before."
    "But she seems sufficiently mollified to keep up the act she's already begun."
    hanna.say "Because I have something for you, [hero.name]."
    show hanna flirt
    hanna.say "Something that I wanted to give you in person."
    hanna.say "So it'd be a nice surprise."
    "Well now I am intrigued!"
    "And I guess it must be pretty obvious too."
    "Because Hanna giggles and her smile becomes wider again."
    hanna.say "I know exactly what you're thinking, [hero.name]."
    hanna.say "And you're a naughty boy for jumping to conclusions like that!"
    show hanna normal
    hanna.say "What I have for you is a little more innocent than that."
    hanna.say "And I can give it to you right here and now!"
    "It's only now that I notice Hanna has her hands behind her back."
    "She follows my gaze, but ducks back so I can't see what she's hiding."
    show hanna flirt
    mike.say "Ah, come on, Hanna!"
    mike.say "Quit stringing me along."
    mike.say "You want me to say I'm intrigued?"
    mike.say "Fine, I'm intrigued!"
    "Hanna keeps twisting and turning, keeping me from seeing."
    "All the time she's giggling, almost snorting in amusement."
    "But finally she seems to have tortured me enough."
    show hanna normal
    hanna.say "Alright, [hero.name]..."
    hanna.say "Here you go."
    "I wait with baited breath as Hanna lets me see what she's hiding."
    "But when I find a plain brown envelope being waved under my nose, I can't hide my confusion."
    mike.say "Huh?"
    mike.say "What the hell is that?"
    "Hanna shakes her head and stuffs the envelope into my hand."
    show hanna flirt
    hanna.say "Take a look inside, dummy!"
    "I do as I'm told, opening the flap to peer at the contents."
    "And my eyes go wide as I pull out a thick wad of used bills."
    mike.say "Whoa!"
    mike.say "There must be like..."
    hanna.say "A thousand bucks, maybe?"
    hanna.say "Because that's exactly how much there is."
    mike.say "What's all this about, Hanna?"
    mike.say "Did you rob a bank or something?!?"
    show hanna sad
    "Hanna takes a step back and looks at me in amazement."
    show fx question
    hanna.say "Erm...are you REALLY that dim?"
    hanna.say "You invested money in the gym, remember?"
    hide fx
    show hanna normal
    hanna.say "This is your first share of the profits!"
    mike.say "Oh yeah, of course!"
    "Almost the same moment I remember the investment, a thought occurs to me."
    mike.say "But why are you giving it to me in used notes, Hanna?"
    mike.say "I mean, couldn't you have transferred it into my bank account?"
    "Hanna instantly looks a little awkward."
    "She leans forward, pushing the money against me."
    show fx drop
    hanna.say "I'd rather keep this off the record, yeah?"
    hanna.say "Just to make things easier for the accountant."
    hide fx
    hanna.say "You understand?"
    "I shrug and nod."
    "Whatever reason Hanna has for being discreet, it's fine by me."
    show hanna flirt
    hanna.say "Plus this way we get to meet in secret."
    hanna.say "And we can exchange a valuable package."
    show hanna normal
    hanna.say "It's kinda like we're in a spy movie, right?"
    mike.say "If you say so, Hanna."
    mike.say "I guess it is pretty exciting!"
    show hanna happy
    "Hanna smiles at my enthusiasm."
    "But I note that she also makes me pocket the envelope so that it's out of sight."
    "I'm sure she's just worried about me flashing a huge wad of cash around in public."
    "So I put all other concerns out of my mind and instead concentrate on my profits."
    "Who knows - maybe I'll spend some of them on Hanna herself?"
    $ hero.money += 1000
    $ hanna.flags.repay += 1
    $ hanna.flags.repay_delay = TemporaryFlag(True, 30)
    return

label hanna_gym_profits_alternate:
    scene bg gym
    show hanna blush
    with fade
    "Hanna's got that look on her face today, I spotted it the moment we met up."
    "It's a more interesting look than the usually flirty expression she has."
    "And it normally means that she's got something on her mind."
    "Which in Hanna's case is more likely than not something dirty."
    "And I do mean the fun kind of dirty!"
    mike.say "What is it, Hanna?"
    show hanna annoyed
    hanna.say "Huh?"
    hanna.say "What do you mean?"
    "I shake my head, refusing to buy her protestations of innocence."
    mike.say "Oh come on, Hanna."
    mike.say "I know you well enough to know that look!"
    mike.say "You've got something on your mind, haven't you?"
    show hanna normal
    "For a moment, Hanna looks like she's going to keep on trying to bluff me."
    "But then she shrugs, realising that there's no way I'm falling for it."
    show hanna -blush flirt
    hanna.say "Okay, [hero.name], you got me!"
    hanna.say "There was something that I wanted to ask you."
    show hanna normal blush
    hanna.say "I was just waiting for the right moment, that's all."
    mike.say "No time like the present, Hanna."
    mike.say "Hit me with it, yeah?"
    hanna.say "Well..."
    hanna.say "I was wondering about your suggestions in the gym."
    "I can't help raising my eyebrows at the mention of my suggestions."
    "I was thinking that Hanna was about to suggest that we get up to something kinky."
    "The last thing I expected to hear was anything about financial matters."
    mike.say "My suggestions?"
    mike.say "What's the problem?"
    mike.say "Didn't it help out with your problems at the gym?"
    mike.say "Because if you're looking for more, I don't know if I can find the money!"
    show hanna sad at startle
    "Hanna shakes her head, like she's eager to dismiss the notion."
    hanna.say "No, no, no..."
    hanna.say "That's not it at all, [hero.name]!"
    show hanna normal
    hanna.say "The gym's doing fine."
    hanna.say "Actually, it's doing better than ever."
    "Now I am starting to get confused."
    mike.say "Then why would you need to talk about my suggestions?"
    mike.say "If everything's fine, then aren't we all happy?"
    hanna.say "We are, [hero.name], we are."
    show hanna sad
    hanna.say "It's just that I'm not comfortable with the current arrangement."
    hanna.say "Specifically the way I've been handing over your profits."
    mike.say "Really?"
    mike.say "I don't recall there being any problems, Hanna."
    show hanna normal
    hanna.say "Isn't there some other way I could compensate you?"
    show hanna -blush flirt at center, zoomAt(1.5, (640, 1040))
    hanna.say "Some way that doesn't involve money?"
    "It's only now that I realise how close Hanna's body is to mine."
    show hanna at center, zoomAt(2.0, (640, 1340))
    "And she's deliberately leaning in closer still."
    "But more importantly, I can feel her hand stroking me."
    "Stroking me somewhere very intimate, if you know what I mean!"
    menu:
        "Accept":
            "I don't even have to think about it."
            "As soon as the words come out of Hanna's mouth, I know what my answer will be."
            "And that's because I'm not fool enough to turn down an offer like that!"
            "What other kind of investment is going to offer returns of that kind?"
            mike.say "Sure thing, Hanna."
            mike.say "That sounds like a pretty sweet deal!"
            show hanna happy blush
            "Hanna nods and smiles, clearly pleased with my answer."
            hanna.say "Of course it is, [hero.name]!"
            hanna.say "You get to know that your investment is helping us grow."
            show hanna -blush flirt
            hanna.say "And I can make you grow by showing you just how grateful I am."
            "To underline the point, Hanna presses herself against me."
            "I can hear her breath as it brushes past my ear."
            "And her hand is really squeezing my cock through my pants now!"
            hanna.say "And you'd better believe that I am grateful, [hero.name]."
            hanna.say "I don't think I've ever been so grateful in my entire life..."
            "All I can do is nod and smile as Hanna drapes herself all over me."
            "And it's not like I could even summon the brain-power to speak if I wanted to."
            "Because my thoughts are already racing, conjuring images of what I could ask Hanna to do for me..."
            $ hanna.flags.payInNature = True
        "Refuse":
            "I open my mouth, about to say what a great idea that is."
            "But then I stop as a thought occurs to me."
            "Why would I want to take sexual favours over money?"
            "I could just take the cash and hire a prostitute if that was what I wanted."
            "And wouldn't that arrangement kind of make Hanna into a prostitute too?"
            show hanna surprised at startle
            mike.say "I think I'll pass, Hanna."
            mike.say "Maybe we can find a way around the cash-filled envelopes."
            mike.say "But I do think we should keep business and pleasure separate."
            show hanna annoyed at center, zoomAt(1.5, (640, 1040))
            "Hanna takes a step back from me, crossing her arms over her chest."
            "And it doesn't take an expert in body-language to tell she's not happy."
            hanna.say "What's the problem, [hero.name]?"
            hanna.say "Am I not good enough for you, huh?"
            hanna.say "Or...wait a minute..."
            show hanna angry
            hanna.say "Are you trying to make me offer you one of the other girls that works at the gym?!?"
            mike.say "Trust me, Hanna - neither of those things is true!"
            mike.say "I'm not after your female employees."
            mike.say "And you're one of the hottest girls I know!"
            mike.say "It's just that I like to get it on when there's not money at stake, okay?"
            show hanna annoyed
            "Hanna looks at least a little mollified by my explanation."
            "Her mouth is set in a pretty stubborn frown."
            "But all the same she nods and makes a little huffing sound."
            hanna.say "Okay, okay..."
            hanna.say "I get the message, [hero.name]."
            show hanna normal
            hanna.say "We'll stick to the current arrangement for now."
    return

label hanna_gym_bj:
    scene bg gym
    "It's time for a quick work-out at the gym, nothing out of the ordinary there."
    "And plus it's super quiet at the moment, so I'm looking forward to really pushing myself."
    "The only problem is that I keep getting these weird looks from Hanna the whole time."
    "Like, I'll be on a machine, and then she appears right next to me, without fail."
    "And she's doing the most bizarre work-out too, all this bending over and stretching."
    "All I can do is keep moving on and pretending not to notice her."
    "But that doesn't seem to help, as she confronts me when I go to hit the showers."
    show hanna close sad blush with easeinright
    hanna.say "What's the problem, [hero.name]?"
    hanna.say "You want to tell me that, huh?"
    "Hanna steps in front of me, blocking the way with her arm."
    mike.say "Wha..."
    mike.say "What's this about, Hanna?"
    mike.say "I was just working out, that's all!"
    show hanna close angry
    "Hanna snorts and shakes her head."
    hanna.say "Bullshit!"
    hanna.say "You were ignoring me, weren't you?"
    hanna.say "Trying to play hard to get!"
    show hanna close normal
    hanna.say "You worked out on everything in the gym."
    show hanna close -blush flirt
    hanna.say "Everything except me!"
    "Oh man!"
    "Now I get what the problem is!"
    "Hanna's got that hungry look in her eye right now."
    "The one that means she needs attention."
    "And she needs it quick!"
    mike.say "Chill out, Hanna!"
    mike.say "I just didn't pick up on the signals you were giving out."
    mike.say "That's all."
    show hanna at center, zoomAt(1, (640, 1540)) with move
    "Hanna grunts and reaches out, grabbing hold of my shorts."
    "Then without pause or hesitation, she pulls them roughly down." with vpunch
    mike.say "Hanna!"
    mike.say "What are you doing?!?"
    hanna.say "What does it look like?"
    hanna.say "I'm taking matters into my own hands!"
    hide hanna
    show hanna bj closed
    with fade
    "Hanna's on her knees in front of me mere moments later."
    "And she already has a firm hold of my cock too!"
    "I might not have been hard when she confronted me."
    "But that's not the case anymore, as the surprise and thrill start to affect me."
    "Hanna spurs my natural reaction on, stroking the shaft and kissing the tip."
    show hanna bj open suck
    show mouth_insert hanna zorder 1 at zoomAt(1, (860, 140))
    "And then she takes the matter out of my hands by talking it between her lips."
    "She looks up at me with determination in her eyes as she starts to work on it."
    "But she must read some of the effect that her efforts are having on me."
    "Because as I begin to feel waves of pleasure flowing through me, Hanna's expression changes."
    show hanna bj closed
    "As if she's feeling the same thing too, her eyes slowly close."
    "And a shudder of release flows from her head to her toes."
    "I guess that Hanna's now getting exactly what she wanted."
    "One hundred percent of my attention is on her right now."
    "And the feeling is pretty intense!"
    "I don't know what I would have done if Hanna had just come right out and asked me."
    "Like walked up to me in the middle of the gym and asked to suck my cock."
    "But somehow this feels like it's better."
    "Like maybe the frustration she's feeling is what's fuelling it."
    "One thing I can say is that I'm grateful this place is a ghost-town right now!"
    show hanna bj wet
    "Hanna's head moves back and forth with a regular rhythm."
    "And her tongue is working wonders on the inside at the same time."
    "All too soon I can feel myself wanting to let go."
    "My body is aching for release and there's nothing I can do to stop it."
    mike.say "Hanna..."
    mike.say "I can't..."
    mike.say "Can't hold on..."
    "I don't know if Hanna hears me or not."
    "But it's going to happen whichever's the case!"
    menu:
        "Cum on her face":
            "Hanna answers the question the moment before I cum."
            "In one smooth motion she pulls back her head."
            hide mouth_insert
            "Which means that my cock slides neatly out of her mouth."
            show hanna bj open normal cumshot with vpunch
            "Then she smiles as I shoot my load over her face."
        "Cum in her mouth":
            "I was expecting Hanna to be taken by surprise when I cum in her mouth."
            "In fact I was prepared to have to help her out as she gagged on it."
            show hanna bj cumshot
            show mouth_insert hanna cum
            with vpunch
            "But she surprises me by expertly swallowing as I shoot my load."
            with vpunch
            "Hanna gulps down everything that I have to give."
            show mouth_insert hanna -cum
            with vpunch
            "And she doesn't falter even once."
            hide mouth_insert
    hide hanna
    show hanna close topless blush
    with fade
    "Hanna almost collapses onto her backside when it's all over."
    "And I see she's panting for breath as she laps up the last few drops."
    hanna.say "I..."
    $ hanna.love += 3
    $ hanna.sub += 1
    show hanna normal
    hanna.say "I really needed that!"
    mike.say "No kidding, Hanna!"
    mike.say "But now I think we both need to get cleaned up!"
    show hanna blush
    "Hanna nods as she gets to her feet."
    "But I can see the way she's still looking at my cock."
    "And she can't keep from licking her lips at the same time."
    hanna.say "You know..."
    hanna.say "I wonder if we could sneak into the showers together?"
    hanna.say "What with this place being deserted..."
    return

label hanna_masturbate:
    scene samantha_showersex_bg at zoomAt(1.2, (-220, 0)), blur(16), dark with dissolve
    "There's nothing like a nice shower after a good, sweaty workout."
    "The whole body gets reinvigorated, and I come out clean and ready to tackle the rest of the day."
    "I let the water run for an extra long shower, enjoying not having to pay the water bill to feel the hot spray over my body."
    "Luckily, the gym is pretty dead this time of day, so I get the whole locker room all to myself with no one questioning me."
    "As I continue to appreciate my 'me' time, something makes me listen."
    "There's a locker slam, and a shuffling of clothes. Heh, no problem."
    "Just a couple dudes in a locker room after exercising."
    "Nothing wrong with that."
    "Girl" "A... ahh..."
    "W... what!?"
    "That sound—that's no dude!"
    "There's... a woman in here?"
    "I wrap the towel around my waist and poke my head out past the curtain."
    show hanna mast with dissolve
    "I almost gasp when I see her—the woman from the treadmill!"
    "I'd recognize that tanned body and golden hair anywhere!"
    "But... she's not wearing her gym outfit."
    "Is she... naked?"
    "Does she not know this is the men's locker room?"
    "Shit... does she see me?"
    "What's she doing?"
    "Girl" "Aah... [hero.name]."
    "She lifts up a piece of fabric, taking in a deep whiff and then shudders, letting out a long, sighing moan."
    "Oh fuck... that's... that's my underwear!"
    "She's sniffing my boxers and... and that's not all."
    "She lowers her one hand down along her body."
    "It still glistens with the sweat of her intense workout."
    "I can see everything, from her amazing abs and her well-toned arms, down to her legs, spread apart, her sex quivering in desire."
    "She pinches at her erect nipple, letting out a little gasp."
    "She holds my trousers in her other hand, and shuffles the fabric around until she gets right where my dick would be."
    show hanna mast b
    "Girl" "Mmm fuck, that... that's some good smell."
    "She whispers to herself, but the echo-filled room allows me to hear all."
    "Girl" "But it doesn't cover up your musk, [hero.name]."
    "A dreamy face fills her as she rolls her eyes back."
    "Girl" "Oh... yes..."
    "I take a few tentative steps out of the shower, tiptoeing my way to the bench, but hiding behind a series of lockers."
    "She lays on her belly, draping the underwear over her face as a blush passes over her flushed face."
    "It's a whole palette of interesting colors on those cheeks of hers, but she's not done yet."
    "Her finger trails down lower on her body when she keeps talking."
    "Girl" "Y... yeah... I didn't know how to tell you..."
    "Her fingers start rubbing over her lips."
    "Girl" "I'm a real fitness freak. I love everything... Everything about it!"
    "She gasps as two fingers dip inside."
    show hanna mast b wet
    "Girl" "Ah, you like... you like that?"
    "She gives me no chance to answer."
    "Does she even know I noticed her?"
    "No, obviously, she still thinks I'm in the shower."
    "Is she... is she waiting for me to get out?"
    "Girl" "Oooh... fuck me, [hero.name]."
    "Her fingers push deeper inside of her."
    "She rubs her clit with her palm and takes another long hit of my smell."
    "Girl" "Th... that's right! I love it. Your smell, your taste, aaanh!"
    "She lifts her ass upward, lifting up onto her toes as she cries out."
    "Girl" "Yeah, come on...let's do it! It's the best exercise. Rougher, rougher!"
    "Girl" "Burn those calories, build that muscle so you can pound me longer next time!"
    "She squirms, biting her lip. I can't help myself but to keep watching."
    "Obviously, she thinks I'm some kind of fitness god."
    "With the rate she fingers herself, I start to get a little jealous with myself."
    "She throws my trousers to the side and gropes around the ground blindly as she handfucks herself."
    "I kneel down and grab my sweaty boxer shorts and toss them back closer to her."
    "Her groping fingers grip at the fabric and she brings it up to her face."
    "Girl" "Oh, fuck yes..."
    "She hisses, and then just shoves the crotch right into her face."
    "Girl" "Ooooh, fuck! That musk!"
    "She laughs a little."
    "Girl" "It's the greatest smell. Come on, [hero.name], fuck me like the animals we are."
    "Girl" "This... this is what our bodies are for!"
    show hanna mast wet squirt
    "She rocks her hips wildly in a rhythm with those fingers, her gasps getting louder and louder."
    hide hanna with fade
    "I tiptoe my way back, keeping her thrusting movements in my eyesight, and soon, I get back to the shower stall."
    "With a loud slam, I turn off the water, leaving a few dripping droplets of water to fill the now quiet room."
    "From her location, she bites her finger, stifling back a few small whimpers."
    "She then sits up quickly, shuffling into her clothes, wait... was she not wearing underwear before!?"
    "Before I could register that idea, she already closed the door, leaving me alone with the slam."
    "When I return to my bench, I whistle—the whole area doesn't look like anyone had been there."
    "All my clothes were back in my locker where I left them."
    "The only thing different is the stain at the bench."
    "Here I thought this girl was out of my league."
    "Now, it seems like I'm the one SHE looks up to."
    "..."
    "..."
    "But what the hell is her name? And how the hell do I introduce myself NOW!?"
    return

label hanna_event_11:
    if hanna.love.max < 200:
        $ hanna.love.max = 200
    scene expression f"bg {game.room}"
    "For one thing, it's a really nice day, and I've been stuck inside for what feels like ages."
    "And I'm also waiting for Hanna to show up, so out here I should see her as soon as she does."
    "Oh, and maybe there's another reason in the fact that Hanna sounded pretty excited on the phone earlier."
    "Look, I know what you're thinking."
    "And I'm not just some desperately horny pervert!"
    "Hanna's just one of those girls, you know?"
    "She's not shy about liking to show off."
    "And you can hear it in her voice when she's...well, when she's in the mood!"
    "All the same, my plan, vague as it is, was just to wait out here until Hanna showed up."
    "Then I was going to invite her into the house and see where things went."
    show hanna casual with dissolve
    "But the moment she actually shows up, I forget all about my plans."
    "And that's because Hanna's just looking so good."
    "Way too good for me to think about anything else."
    "She comes walking up the path to the house, waving to me on the porch."
    "But it's hard for me to take my eyes off her legs as she gets closer."
    hanna.say "Hi, [hero.name]..."
    hanna.say "You came out to meet me!"
    show hanna flirt
    hanna.say "How sweet of you."
    "I nod and grin as Hanna climbs the stairs to the porch."
    "And I do try to tear my eyes away from her body and look her in the face."
    mike.say "Hey, Hanna..."
    mike.say "Yeah, I was just that desperate to see you!"
    show hanna happy at startle
    "Hanna laughs and does a little turn on the porch in front of me."
    hanna.say "So what do you think?"
    hanna.say "Do I live up to your expectations?"
    "I can't help nodding and laughing in turn."
    "It'd be pretty hard to hide the fact that Hanna's hot enough to make me crazy."
    "And why would I want to deny it anyway?"
    "Especially when I know that she likes to have all eyes on her."
    mike.say "Oh no, Hanna..."
    mike.say "You blew them out of the water!"
    "Hanna nods eagerly, lapping up the praise."
    show hanna close normal
    "Then she closes the distance between us, wrapping her arms around my waist."
    "I return the embrace, enjoying the feeling of her body pressed against mine."
    hide hanna
    call hanna_porch_sex from _hanna_event_11_porch_sex_call
    return

label hanna_event_10:
    if hanna.love.max < 180:
        $ hanna.love.max = 180
    scene bg gym
    "It's been one of those days when everything just seems to go right for me."
    "Not like I've won the lottery, but small stuff, you know?"
    "No queue at the coffee shop, lights turning green when I need them to."
    "And now I feel like I've really hit my stride in the gym too."
    "It's only my regular work-out, but as I finish up, I'm buzzing."
    "The effects must be physical as well as mental too."
    show hanna work with dissolve
    "Because I look up to see Hanna watching me from a short distance away."
    "I can't help smiling back at her, because I'm in such a good mood."
    "And plus, she always looks good in the skin-tight lycra she wears at work."
    show hanna happy
    "Hanna returns the smile and then glances around, as if she's looking for something."
    "Puzzled, I watch with growing interest as she starts fumbling with the door."
    show hanna normal
    "I open my mouth to ask Hanna what she's doing."
    "But by then she's already hurrying over to where I'm standing."
    mike.say "Hey, Hanna..."
    mike.say "What's up?"
    hanna.say "Oh, nothing..."
    hanna.say "I just wanted to check if you finished your work-out yet?"
    "I shrug casually and then nod."
    mike.say "Just wrapped it up a second ago."
    mike.say "Why'd you ask?"
    "It's only now that I note Hanna's looking a little shifty."
    "She's not the kind of girl that's an expert when it comes to lying."
    "And she's giving off most of the tell-tale signs right now."
    hanna.say "No reason..."
    show hanna happy
    hanna.say "I just wanted to talk to you about adding something to it, that's all."
    mike.say "You think I should be doing more?"
    hanna.say "I think there's one more thing you should be doing right now."
    mike.say "Oh yeah?"
    mike.say "And what would that be?"
    show hanna flirt
    hanna.say "Me!"
    "To underline the point, Hanna leans in close."
    hide hanna
    show hanna kiss work
    with dissolve
    $ hanna.flags.kiss += 1
    "She kisses me full on the mouth."
    "And her tongue snakes between my lips."
    "I rise to the kiss, unable to resist her even for a moment."
    "My hands grab hold of Hanna's ass, squeezing it through the lycra."
    "And I can feel her firm yet feminine body pressing against mine."
    "I have the urge to slide my hand under that tight, stretchy material."
    "Either above her waist and get myself a handful of her breasts."
    "Or else below it and feel how wet she's getting between her legs."
    "Hanna must be getting the same idea as me too."
    "As I can feel her stroking my cock as it gets ever harder."
    "But then I remember where we are."
    "Sure, Hanna might be a senior member of staff at the gym."
    "But that doesn't mean she can let herself get caught in a situation like this!"
    "They'd practically have to fire her in order to make the scandal go away."
    "And that's why I choose to break the kiss a moment later."
    hide hanna
    show hanna work blush
    with dissolve
    hanna.say "Mmm..."
    show hanna annoyed
    hanna.say "Huh?!?"
    hanna.say "What's the matter?"
    hanna.say "I was ready to go all the way!"
    mike.say "Me too, Hanna."
    mike.say "But I don't want you to get caught!"
    "Hanna shakes her head and giggles at this."
    show hanna happy
    hanna.say "Don't sweat it, [hero.name]."
    hanna.say "I locked the door on my way in here."
    hanna.say "And I'll erase the footage from the security cameras later too."
    "So that's what she was doing when she first came in here!"
    mike.say "Oh..."
    mike.say "Okay, Hanna..."
    mike.say "I feel kind of silly now!"
    hanna.say "It's okay, [hero.name]."
    show hanna flirt -blush
    hanna.say "Now...where were we?"
    "Hanna's already starting to strip off as she says this."
    show hanna topless with dissolve
    "I watch with unashamed delight as she pulls off her top."
    "And then, as her breasts sway with the motion, she pulls down her leggings."
    "Hanna must have pulled her panties down with them too."
    show hanna naked with dissolve
    "Because she's now standing there, naked in front of me!"
    "She slowly lowers herself to the floor, getting down on all fours."
    "Then she raises her ass in the air and looks back over her shoulder."
    scene bg black
    show hanna doggy gym with fade
    hanna.say "What are you waiting for, [hero.name]?"
    hanna.say "Ride me already!"
    "I nod hastily, tearing off my own clothes."
    "And then I'm down behind Hanna, grabbing hold of her with both hands."
    show hanna doggy mike
    "She gasps and then giggles, playfully waggling her ass at me."
    "Now all I have to do is decide where I'm going to put it!"
    menu:
        "Fuck her ass":
            "This whole thing feels pretty hurried and dirty."
            "It's like there's the very real danger of us being caught!"
            "But my reaction to that isn't to play it safe."
            "Instead I feel the sudden urge to up the stakes as much as possible."
            "That's why I part Hanna's buttocks and aim my cock between them."
            "She seems to catch on to what I'm doing pretty quickly."
            "Hanna giggles and shoves her ass backwards."
            "All of which lets me know that she's up for this."
            hanna.say "You want my ass, huh?"
            hanna.say "Well that's fine by me!"
            hanna.say "Just make sure you give it your all, [hero.name]!"
            "She's looking back over her shoulder as she says all of this."
            "And I give her a nod to show I understand."
            "Hanna's head turns the other way as I begin to push forwards."
            "Her ass is amazingly tight, toned like every part of her body."
            "But that doesn't mean it's going to be able to defeat me."
            "And that's because I've been whipped into shape by Hanna too."
            "It's kind of ironic that she's turned me into such a prize specimen of humanity."
            "As it's that same strength and stamina that I'm using to push into her right now!"
            show hanna doggy anal
            "Hanna begins to moan as the head of my cock enters her ass."
            "My progress is slow but steady, inching my way into her."
            "But all that really means is that the experience is drawn out."
            "For me the sensation of sinking in there is exquisite and feels unending."
            "I can only imagine what it must feel like on Hanna's end."
            "Though from the sounds that she's making, I can guess!"
            mike.say "You..."
            mike.say "You like that..."
            mike.say "Huh?"
            show hanna doggy happy
            "Hanna makes a mewling sound at first."
            "She nods her head as though unable to speak."
            "But then she gasps and seems to regain her senses."
            hanna.say "Mmm..."
            hanna.say "Oh yeah..."
            hanna.say "God yeah!"
            "By the time Hanna's saying all of this, I'm deep into her."
            "In fact, I'm almost as deep as I can possibly go."
            "With some girls I'd be getting worried right about now."
            "I'd need to be thinking about going slow and steady."
            show hanna doggy blush
            "Making sure that I didn't do anything that was too much for them to handle."
            "But I don't think I've ever been with a girl as fit and robust as Hanna."
            "And I just know that she can take whatever I can dish out."
            "That's why I get up to speed as quickly as I can."
            "I use every ounce of strength I possess to move inside of her."
            "The muscles of Hanna's ass are still squeezing me tightly."
            "But they've surrendered enough to let me thrust quite easily."
            "I take full advantage, going almost as fast as I would fucking her pussy."
            "And it doesn't take long for Hanna to prove me right as to her stamina either."
            "Almost any other girl would be crying out for mercy, begging me to slow down."
            "Instead, Hanna's head nods up and down the whole time."
            "She grunting sounds that she makes seem to urge me on."
            show hanna doggy ahegao sweat
            "Her body takes all that I have to give and still wants more!"
            "I know that I can't keep on going forever, even if Hanna could."
            "And I can already feel myself teetering on the edge."
            "A moment later I can't hold back any longer."
            mike.say "Oh shit..."
            mike.say "Here it comes!"
            call cum_reaction (hanna, 'anal', 1) from _call_cum_reaction_78
            if _return == 'anal_inside':
                "Hanna's almost got her head on the floor right now."
                "And her ass is stuck up in the air, legs braced firmly in place."
                "With me pushing downwards, the logical thing seems to keep on going."
                show hanna doggy creampie with hpunch
                "So that's just what I do, giving one last thrust as I shoot my load."
                with hpunch
                "Hanna lets out a deep, satisfied moan as I fill her ass."
                show hanna doggy squirt with hpunch
                "And I don't stop until the cum is seeping out from around my cock."
                $ hanna.love += 1
                $ hanna.sub += 1
            elif _return == 'anal_outside':
                "Hanna's almost got her head on the floor right now."
                "And her ass is stuck up in the air, legs braced firmly in place."
                "That means I can pretty much do whatever the hell I want."
                show hanna doggy -anal
                "And I use that freedom to pull my cock out of her ass before I cum."
                show hanna doggy cumshot with hpunch
                "Hanna moans at the sensation, and the same feeling pushes me over the edge too."
                show hanna doggy dickcum cum onbody -cumshot with hpunch
                "I shoot my load over Hanna's naked buttocks, striping them with hot, sticky cum."
                with hpunch
                "Then I stand back, panting as I watch it begin to run down her thighs."
                $ hanna.sub += 2
        "Fuck her pussy":
            "I can feel the thrill of what we're doing, the sense of danger."
            "The fear of someone walking in on us, catching us in the act."
            "It makes me hurry to get on with things, eagerly grabbing hold of Hanna's haunches."
            "The sense of danger is also making me pretty hard right now."
            "And I can already see that it's having a similar effect on Hanna too!"
            call check_condom_usage (hanna) from _call_check_condom_usage_42
            if _return == False:
                $ hero.cancel_event()
                return
            show hanna doggy
            if CONDOM:
                show hanna doggy condom
            hanna.say "Come on, [hero.name]."
            hanna.say "What are you waiting for?"
            hanna.say "Stick it in me already!"
            "Hanna's looking back over her shoulder as she says all of this."
            "And I give her a nod to show I understand."
            "A moment later I feel the head of my cock slide along her lips."
            "They're soft and warm, slippery in the most amazing way imaginable."
            "The rest of Hanna's body might be firm and solid."
            "But the same can't be said for her pussy right now."
            show hanna doggy vaginal
            "Almost the same moment I begin to push, it starts to give way."
            "Hanna yields to me in a slow and steady way."
            "This means that I enter her a little at a time to begin with."
            "But then I seem to reach some kind of tipping point."
            "And all of a sudden I feel myself sink deeper into her."
            "I gasp at the sensation, almost like she's dragging me in."
            "Hanna moans too, which only serves to add to the effect."
            hanna.say "Mmm..."
            show hanna doggy happy
            hanna.say "Oh my god..."
            hanna.say "Did...did you cock get bigger?"
            hanna.say "I swear you didn't fill me like this the last time we fucked!"
            show hanna doggy blush
            "I begin to move inside of Hanna, pushing as far into her as I can."
            "The way she's loving the feeling of my cock inside her..."
            "It's more than enough to make me work my hardest to please her."
            hanna.say "Whoa..."
            hanna.say "Oh yeah..."
            hanna.say "You can do that to me all day long!"
            "I can't help smiling at Hanna's praise."
            "She's not the only one that would like to do this all day long!"
            "I set as energetic of a pace as I can, working my body hard."
            "And as I do so, I'm silently glad of the fact I spend so much time at the gym."
            "My stamina would never have been up to the task without my work-out regimen."
            "Plus I know that I'd never have been able to satisfy a girl as fit as Hanna either."
            "I'm going as fast as I can right now, pushing myself to the limit."
            "But she's taking all that I have to give and demanding more!"
            "As hard as I'm pounding Hanna, my heart's pounding harder in my chest."
            "Her head is almost touching the floor by now."
            "And her ass is thrust as high in the air as possible."
            "I'm pushing down for all I'm worth, sweating and breathing hard."
            "Any other girl would have been exhausted by now."
            "They'd have cum and collapsed into a heap."
            "But not Hanna, she's still conscious and begging for more!"
            "No matter how much good working out at the gym has done for me, I'm only human."
            "I know that I can't keep on going forever, even if Hanna could."
            "And I can already feel myself teetering on the edge."
            "A moment later I can't hold back any longer."
            mike.say "Oh shit..."
            mike.say "Here it comes!"
            call cum_reaction (hanna, 'vaginal', 1) from _call_cum_reaction_79
            if _return == "vaginal_outside":
                "Hanna's still almost kissing the floor as I lose it."
                "And her ass is stuck up in the air, legs braced firmly in place."
                "That means I can pretty much do whatever the hell I want."
                show hanna doggy -vaginal
                "And I use that freedom to pull my cock out of her pussy before I cum."
                show hanna doggy cumshot with hpunch
                "Hanna moans at the sensation, and the same feeling pushes me over the edge too."
                show hanna doggy cum onbody dickcum -cumshot with hpunch
                "I shoot my load over Hanna's naked buttocks, striping them with hot, sticky cum."
                "Then I stand back, panting as I watch it begin to run down her thighs."
                $ hanna.sub += 1
            elif _return == "vaginal_condom":
                "Hanna's still almost kissing the floor as I lose it."
                "And her ass is stuck up in the air, legs braced firmly in place."
                "With me pushing downwards, the logical thing seems to keep on going."
                "We remembered to use protection, meaning that it's safe."
                "So that's just what I do, giving one last thrust as I shoot my load."
                "Hanna lets out a deep, satisfied moan as I fill her pussy."
                "And I don't stop until I'm spent, panting and gasping for breath."
            elif _return == "vaginal_inside_pill":
                hanna.say "Don't stop..."
                hanna.say "I'm on the pill..."
                hanna.say "You remember?!?"
                "Hanna's still almost kissing the floor as I lose it."
                "And her ass is stuck up in the air, legs braced firmly in place."
                "With me pushing downwards, the logical thing seems to keep on going."
                "And her desperate words remind me there's no danger in that."
                show hanna doggy creampie with hpunch
                "So that's just what I do, giving one last thrust as I shoot my load."
                with hpunch
                "Hanna lets out a deep, satisfied moan as I fill her pussy."
                show hanna doggy ahegao squirt with hpunch
                "And I don't stop until I'm spent, panting and gasping for breath."
                $ hanna.love += 1
            elif _return == "vaginal_inside_pregnant":
                hanna.say "Don't stop..."
                hanna.say "You already..."
                hanna.say "Knocked me up!"
                "Hanna's still almost kissing the floor as I lose it."
                "And her ass is stuck up in the air, legs braced firmly in place."
                "With me pushing downwards, the logical thing seems to keep on going."
                "And her desperate words remind me there's no danger in that."
                show hanna doggy creampie with hpunch
                "So that's just what I do, giving one last thrust as I shoot my load."
                with hpunch
                "Hanna lets out a deep, satisfied moan as I fill her pussy."
                show hanna doggy ahegao squirt with hpunch
                "And I don't stop until I'm spent, panting and gasping for breath."
                $ hanna.love += 1
            elif _return == "vaginal_inside_mad":
                hanna.say "No, no, no!"
                hanna.say "You have to stop now!"
                hanna.say "Don't cum in me - please!"
                "Hanna's words take me by surprise, making me forget what I was doing."
                "But my body keeps right on going, so giving one last thrust as I shoot my load."
                show hanna doggy creampie with hpunch
                "Hanna lets out a deep, ominous groan as I fill her pussy."
                with hpunch
                "And I don't stop until I'm spent, panting and gasping for breath."
                with hpunch
                "But my mind is already racing with the thought of what just happened."
                # $ hanna.impregnate()
                $ hanna.love -= 10
                $ hanna.sub += 5
            elif _return == "vaginal_inside_happy":
                "I suddenly remember that we didn't use any protection."
                "Which means I need to pull out before it's too late!"
                "But the moment I make my move, Hanna shakes her head."
                hanna.say "No, no, no!"
                hanna.say "Keep going!"
                hanna.say "Cum in me - please!"
                "Hanna's words take me by surprise, making me forget what I was doing."
                "But my body keeps right on going, so giving one last thrust as I shoot my load."
                show hanna doggy creampie with hpunch
                "Hanna lets out a deep, satisfied moan as I fill her pussy."
                with hpunch
                "And I don't stop until I'm spent, panting and gasping for breath."
                # $ hanna.impregnate()
                show hanna doggy ahegao squirt with hpunch
                "But my mind is already racing with the thought of what just happened."
                $ hanna.love += 5
    scene bg gym
    show hanna naked sweat
    with fade
    "We don't have much time to bask in the afterglow once we're done."
    "Instead we hastily find our clothes and start to get dressed."
    show hanna work -naked -sweat with dissolve
    "There's no need to exchange any words as we do so."
    "The flushed smiles we share are more than enough for us."
    show hanna happy at left with move
    "Hanna blows me a kiss as she unlocks the door and slips out."
    hide hanna with moveoutleft
    "Which leaves me exhausted and unable to even contemplate finishing my work-out."
    "But I guess what we just did more than makes up for it."
    return

label hanna_event_10a:
    show hanna
    with fade
    "Normally when I'm with Hanna, I can always tell that she's watching me closely."
    "And that's because she likes to know that all of my attention is on her alone."
    show hanna annoyed
    "But today something is different, because whenever I look at her, she looks away."
    "And the Hanna that I know isn't bashful in her eternal quest for attention."
    "So there's got to be something else bothering her right now."
    "Then I see a couple of pretty buff, good-looking guys walk past."
    "And every one of them is obviously checking Hanna out."
    "They're not even trying to hide the fact either."
    "But what surprises me is that Hanna totally fails to notice!"
    "Now I know for sure that there's definitely something wrong."
    "And I have to know what it is, for the sake of my own sanity."
    show hanna annoyed at center, zoomAt(1.5, (640, 1040)) with fade
    mike.say "Hanna..."
    mike.say "What is it with you today?"
    show hanna confused
    "Hanna looks round, meeting my eye for the first time."
    "And she still looks as confused and evasive as before."
    show hanna surprised
    hanna.say "Huh?"
    hanna.say "What do you mean, [hero.name]?"
    show hanna confused
    mike.say "You have to know what I mean, Hanna!"
    mike.say "You've been distracted as hell since we met up."
    mike.say "I'm starting to worry there's something seriously wrong with you!"
    "Hanna looks at me in total silence for a moment."
    "And I'm worried that she's just going to try to change the subject."
    "But then she seems to cave in, letting out a weary sigh."
    show hanna sad
    hanna.say "Urgh..."
    hanna.say "I've been wrestling with this for days now, [hero.name]."
    show hanna annoyed
    hanna.say "Going over and over it in my head."
    show hanna sad
    hanna.say "Trying to figure out how to tell you..."
    "I can feel a rising sense of panic in my gut as Hanna says all of this."
    "My brain naturally assumes that she must have the worst thing possible to tell me."
    "Like, she's got a terminal disease, or worse - she's going to dump me!"
    mike.say "It's okay, Hanna..."
    mike.say "I promise that whatever it is you have to say..."
    mike.say "You can tell me."
    show hanna confused
    "Hanna nods, obviously taking solace from my words."
    hanna.say "Alright..."
    hanna.say "Here goes..."
    show hanna blush
    hanna.say "[hero.name], I think...I think I love you!"
    "I've braced myself for the worst scenario."
    "So when Hanna comes out with a line like that, it kind of leaves me stunned."
    "I shake my head in confusion, not able to understand why that was so hard."
    mike.say "But that's good...isn't it?"
    mike.say "I mean, I like you too, Hanna."
    "Hanna shakes her head at this."
    show hanna normal
    hanna.say "Sure it is, [hero.name]."
    hanna.say "I realise that now."
    show hanna sad
    hanna.say "But at first I thought I was ill or something!"
    show hanna normal
    mike.say "Wait..."
    mike.say "You mistook falling in love with me for being ill?"
    "Much to my dismay, Hanna nods eagerly at this."
    show hanna annoyed -blush at startle
    hanna.say "Oh yeah!"
    hanna.say "I stopped trying to catch looks off other guys."
    hanna.say "And when they shot me a look, I felt...kind of dirty."
    hanna.say "It was like I wanted them to stop."
    hanna.say "At first I thought I was going off men altogether."
    hanna.say "Which wouldn't have been the end of the world..."
    mike.say "But?"
    show hanna normal blush
    hanna.say "But then I caught you looking at me, [hero.name]."
    hanna.say "And all the pleasant feelings came flooding right back!"
    hanna.say "Then I figured out that must mean I love you."
    "I blink at all Hanna's just off-loaded onto me."
    "It's kind of confusing, trying to process it all."
    "But the basic low-down seems to be good, because it's that she loves me!"
    mike.say "I..."
    mike.say "I think that's great, Hanna."
    mike.say "That it could be the start of something beautiful."
    show hanna b normal -blush
    "Hanna holds up a hand, stopping me in my tracks."
    hanna.say "Wait a second, [hero.name]..."
    hanna.say "There's more!"
    mike.say "More?"
    hanna.say "Oh yeah!"
    hanna.say "You're the only man that I want looking at me, [hero.name]."
    hanna.say "So that means I have to be with you always."
    hanna.say "I don't ever want you to leave my side."
    mike.say "What are you saying, Hanna?"
    mike.say "That you're going to tie me up in your basement or something?"
    show hanna annoyed blush
    "This suggestion seems to give Hanna pause for thought."
    hanna.say "Hmm..."
    show hanna normal -blush
    hanna.say "Now there's an interesting idea!"
    hanna.say "I was just going to ask you to marry me."
    hanna.say "You know, keep things traditional?"
    menu:
        "Let's get married!":
            "I'm still reeling from Hanna's confession of love."
            "But then her proposal of marriage hits me from nowhere."
            "My brain doesn't even seem to process the information."
            "I just open my mouth and out it comes."
            mike.say "Marry you?"
            mike.say "Of course I'll marry you, Hanna!"
            show hanna sad
            hanna.say "It's okay if you want to think about it."
            mike.say "I want to marry you!"
            hanna.say "Seriously, I don't want you to feel pressured."
            with vpunch
            mike.say "HANNA!"
            show hanna surprised at startle
            hanna.say "Wh...what?!?"
            mike.say "I'd love to marry you!"
            "Hanna seems not to hear me at first."
            "Then I see my words start to sink in."
            show hanna blush at startle
            hanna.say "You will?"
            mike.say "Of course I will, Hanna."
            show hanna happy
            mike.say "I want to be with you too."
            "Hanna doesn't say another word."
            hide hanna
            show hanna kiss
            with hpunch
            $ hanna.flags.kiss += 1
            "Instead she throws her arms around me."
            "And I find myself caught in a bear-hug."
            "Which is pretty formidable, thanks to her working as a fitness instructor!"
            "The kiss that follows is less intense, but much more passionate."
            "And I make sure that it lasts a good, long time too."
            $ hanna.set_fiance()
            $ hanna.love += 5
        "I need time to think about it.":
            "I'm still reeling from Hanna's confession of love."
            "But then her proposal of marriage hits me from nowhere."
            "And it's more than my poor, battered brain can take."
            mike.say "Whoa!"
            mike.say "Slow down there, Hanna!"
            show hanna confused
            hanna.say "What do you mean?"
            hanna.say "It's a simple enough question."
            hanna.say "All you have to do is say yes!"
            "I hold up a hand to stop Hanna in her tracks."
            mike.say "Well I'm saying no!"
            show hanna surprised at startle
            hanna.say "No?!?"
            mike.say "For now at least, Hanna."
            mike.say "You only just told me that you love me."
            mike.say "I kind of need some time to process that."
            "Hanna opens her mouth as though she's going to argue."
            "But then she seems to think better of it."
            "And instead she sighs with frustration."
            show hanna sad
            hanna.say "Okay, okay..."
            hanna.say "Maybe I did get a tiny bit carried away."
            show hanna normal
            hanna.say "But the offer still stands, [hero.name]."
            hanna.say "I love you and I want to marry you."
            hanna.say "But you can take a little time to make up your mind."
            "Now it's my turn to let out a sigh."
            "But mine is one of sheer relief."
            "Looks like I bought myself some breathing time!"
            $ hanna.love -= 10
    hide hanna with fade
    return

label hanna_event_09_intro:
    scene bg street
    show hanna date
    with fade
    "Look, let's get this out of the way first - I know that Hanna likes to have all eyes on her, that she's an exhibitionist."
    "It's just something that I've just had to come to terms with in the time that we've been seeing each other."
    "And yes, the idea to invite her along to a strip-club was kind of a way to turn the tables on her a little."
    "But when I finally pluck up the courage to pop the question, Hanna's answer takes me by surprise."
    mike.say "Hey, Hanna."
    mike.say "I just had a great idea for our date tonight."
    hanna.say "You did?"
    show hanna happy
    hanna.say "Well come on then - spit it out!"
    mike.say "We should take in a strip-club!"
    mike.say "It'd be fun, in a kind of ironic, postmodern way, you know?"
    show hanna normal
    "Hanna looks at me sideways for a couple of seconds, clearly weighing up the idea in her head."
    "And in that short space of time, I'm almost totally convinced that she's going to say no."
    "Which is fine by me, as I was only trying to have some innocent fun at her expense anyway."
    hanna.say "Yeah, I do know, [hero.name]."
    show hanna normal
    hanna.say "I see how it could be a laugh."
    hanna.say "So what are we waiting for?"
    hanna.say "Let's go already!"
    mike.say "Uh...I..."
    mike.say "Yeah, Hanna, of course - let's get going..."
    "It doesn't take us long to make our way to the strip-club that I had in mind."
    "Not that I have a massive number that I can call to mind, of course..."
    "I guess I just kind of nod and smile most of the way there, like I'm on autopilot."
    "The truth is that I'm still more than a little stunned at Hanna actually wanting to do this!"
    return

label hanna_event_09:
    $ game.room = "stripclub"
    if hanna.love.max < 170:
        $ hanna.love.max = 170
    if hanna.sub.max < 100:
        $ hanna.sub.max = 100
    scene poledance with fade
    "But as we walk in and choose a table right in front of the stage, I notice something unusual."
    "There are signs up around the place that catch my attention."
    show hanna normal date with dissolve
    mike.say "Hey, what's this?"
    hanna.say "It says 'Open Pole Night'."
    hanna.say "Does that mean what I think it means?"
    "I can only nod at first, the implications of those words already dawning on me."
    "As soon as I recover the power of speech, I agree with Hanna's implied guess."
    mike.say "I suppose it's like an open mike night, Hanna."
    mike.say "Only with no microphone."
    mike.say "And more scantily-clad dancing too!"
    show hanna surprised blush
    "I see Hanna's eyes light up almost the same instant that I mention those last couple of words."
    "She doesn't even have to hint at what she's thinking for it to be pretty plain to me."
    show hanna normal
    "Hanna fixes me with what I recognise as one of her cutest expressions."
    "The one that never fails to make me hot under the collar at the thought of what she wants."
    "She nods her head towards the empty stage, smiling sweetly."
    hanna.say "[hero.name]..."
    show hanna blush
    hanna.say " You think that..."
    mike.say "Y...you want to dance?"
    mike.say "On the stage?!?"
    show hanna annoyed
    "Hanna sighs and rolls her eyes in frustration."
    hanna.say "Urgh..."
    hanna.say "No, [hero.name], I want you to do it!"
    hanna.say "Of course I want to dance on the stage!"
    show hanna normal
    "At this, she fixes me with one of those stares that girls are so good at pulling off."
    "The kind that says I need to agree with her, and quickly."
    "Or else I'd better have a damn good reason to explain myself if I don't!"
    menu:
        "Discourage Hanna from dancing":
            "I'm already regretting the fact that I brought Hanna here in the first place."
            "But as if that wasn't enough, now I find myself on trial."
            "And for what?"
            "Over letting her make an exhibition of herself in public!"
            "Another guy might have just laughed it all off and told her to go right ahead."
            "But I can already feel the jealousy bubbling up inside of me."
            "I find that I hate the very idea of all eyes in the room being on Hanna."
            "Maybe it's time that I started being honest with her about that kind of thing?"
            mike.say "Hanna..."
            mike.say "Please don't do it."
            "Hanna raises her eyebrows as she regards me, waiting for me to say more."
            show hanna annoyed
            "Clearly it's going to take more than simply asking her not to go through with it."
            mike.say "Look, I know coming here was my idea."
            mike.say "And yeah, I thought it'd be a pretty wild and crazy place for a date."
            mike.say "But...I..."
            mike.say "I just don't like the thought of everyone looking at you."
            "Hanna frowns at this, cocking her head on one side as she considers my words."
            hanna.say "Huh, is that so?"
            show hanna normal
            hanna.say "But you'd come here and stare at other girls doing the same thing?"
            "I can already feel myself flushing with embarrassment at what Hanna just said."
            "She's really managed to nail me to the wall with that one."
            mike.say "I guess that kind of makes me a hypocrite, Hanna."
            mike.say "Because I want to keep you to myself..."
            "I'm expecting Hanna to blister me again, pretty sure that I deserve it too."
            "But then I see her face break and her expression soften."
            hanna.say "You...you like me that much, huh?"
            hanna.say "Well, I suppose that is kinda flattering, [hero.name]."
            hanna.say "But yeah, you are a hypocrite too!"
            hanna.say "Don't worry though."
            hanna.say "I won't dance if that's what you want."
            show hanna flirt -blush
            hanna.say "Who knows - I may treat you to a private show later tonight..."
            "And with that, we settle down to watch the girls who signed up for a spot on the stage."
            "I can't say that I enjoy the show as much as I might under any other circumstances."
            "But Hanna holds my hand under the table the whole time."
            "Which gives me more pleasure than any amateur stripping ever could."
            $ hanna.sub += 1
            $ game.active_date.score -= 10
        "Encourage Hanna to dance" if hanna.sub >= 60:
            "I can't say I like the idea of all eyes being on Hanna as she flaunts herself on stage."
            "But I'm not about to pussy out when it was my idea to come here in the first place either."
            "I take a quick look at the typically skimpy and revealing outfit that Hanna has on."
            show hanna normal
            "And then I check out some of the other girls that are either awaiting their turn or signing up for a spot."
            "Hanna's easily more of a knockout than any of them, and she's already dressed for the occasion too."
            "Plus I don't recognise anyone in here, what with the subdued lighting."
            mike.say "What the hell."
            mike.say "You should definitely go for it."
            show hanna happy
            hanna.say "You really mean it, [hero.name]?"
            mike.say "Sure thing I mean it!"
            mike.say "I bet you're a natural, Hanna."
            "I see a smile full of eager gratification spread across Hanna's face."
            "And a moment later, she's up and hurrying over to the bar to add her name to the list."
            "After that, time seems to speed up significantly as we wait for Hanna to be called to the stage."
            "I try to make idle conversation while watching the amateurs that are on before her."
            "But I can hardly concentrate for more than a second or two at a time."
            "Instead, all I can think of is what I'll see when her spot comes around."
            "Sure, I've spent a hell of a lot of time staring at Hanna's body in the time I've known her."
            "And can you blame me?"
            "I also know that she's not exactly shy of showing off either."
            "But this is technically the first time that she's done so openly and without pretence."
            "Somehow that seems to make the prospect all the more exciting."
            "Almost as if before we were merely flirting and this is the real thing."
            "And so when the time comes for Hanna to take to the stage, I'm caught completely off guard."
            scene poledance
            show poledance hanna
            with fade
            "Before I can even wish her luck, she's out of her seat and up there."
            "As Hanna steps under the lights, I see her hesitate for a moment, taking a deep breath."
            "But the very same second that the music begins to thump, any sign of nerves seems to vanish."
            "Hanna's head snaps up, and she grabs the pole with one hand, legs moving as she walks around it."
            "What follows is pretty much a revelation, as she puts on a show I won't soon forget."
            "Hanna moves like she wants to show each and every person in the room all that she's got."
            "And that trim, toned body moves in a way that makes looking away for a mere second impossible."
            "One moment she's on her feet, and the next she's hanging upside down from the pole."
            "But every movement is fluid and filled with an attitude that just oozes confidence."
            "Was this what Hanna had inside of her head?"
            "Is this what she was imagining whenever she led a class at the gym or enjoyed turning head in the street?"
            "If so, then I can finally understand the smile on her face when she did so."
            "That and the compulsion she must feel to show off!"
            "Hanna's performance has me mesmerised."
            "So much so that I hardly notice the claps and whistles she's getting from the audience around the room."
            "But maybe that's because she's taking great pains to make sure that her eyes are always on me."
            "This means that despite the fact she has an enthusiastic audience, I feel like Hanna's dancing for me alone."
            "All too soon the slot that she was given comes to an end."
            scene poledance with fade
            "And Hanna is forced to leave the stage, much to the disappointment of all present."
            "I'm still in somewhat of a daze when she sits back down at my side."
            "But then I feel her reach under the table and squeeze my cock through my pants."
            show hanna date happy with dissolve
            hanna.say "Mmm..."
            hanna.say "Looks like you were seriously impressed, [hero.name]!"
            mike.say "Ah...I...I guess so, Hanna!"
            hanna.say "Just so you know, what's in my hand now was on my mind."
            hanna.say "It was all I thought about the whole time I was up there!"
            "All I can do is swallow audibly, grabbing my drink to ease my suddenly dry throat."
            "Hanna laughs at my obvious state of aroused disarray until the music signals the start of the next act."
            "And then we sit and watch the rest of the amateurs take their turn in a pleasant silence."
            "The entire time, from then until the moment that we leave, she never moves her hand even once..."
            $ hanna.love += 2
            $ game.active_date.score = 100
    $ game.pass_time(2)
    return

label hanna_event_09a(appointment=None):
    $ DONE["hanna_event_09a"] = game.days_played
    if hanna.love.max < 200:
        $ hanna.love.max = 200
    scene bg door restaurant with fade
    "I have to admit that when it comes to a choice of restaurant, Hanna has pretty good taste."
    "And it looks like she was organised enough to call ahead and reserve a table too."
    scene bg restaurant with fade
    pause 0.3
    show ryan at left, blacker with dissolve
    show hanna date at right5 with easeinright
    "Because as soon as we walk in the door, she confidently strides over to the first waiter she sees."
    show hanna date at right4 with ease
    hanna.say "Excuse me..."
    "Waiter" "Yes, madam?"
    hanna.say "We have a reservation for two."
    hanna.say "The booking was made under the name 'hanna'?"
    "The waiter walks over to the little podium by the entrance and proceeds to check the list."
    "Then he looks up with an unctuous smile on his face."
    "Waiter" "Ah, yes..."
    "Waiter" "Here we are."
    "Waiter" "If you'd like to follow me..."
    "Hanna and I follow close on the waiter's heels as he leads us to our table."
    "And just like I was with the choice of restaurant, I'm impressed with this too."
    show restaurant meal nomeals hanna date with fade
    "Hanna seems to notice the fact, and she practically beams at me across the table."
    hanna.say "I take it you approve, [hero.name]?"
    hanna.say "You like this place?"
    mike.say "It looks great, Hanna!"
    mike.say "But..."
    mike.say "It also looks kind of expensive too!"
    "Hanna makes a point of shaking her head as she waves a hand in the air."
    show restaurant meal hannahappy
    hanna.say "Oh, don't worry about that."
    hanna.say "With the gym back on track, I can easily afford it."
    hanna.say "Plus tonight is supposed to be my treat."
    hanna.say "My way of saying thank you for coming to the rescue, remember?"
    "I feel a nervous smile spreading over my face as Hanna reminds me of the loan I gave her."
    "And I can't help rubbing the back of my head with my hand, trying to shake off my embarrassment."
    mike.say "Ah..."
    mike.say "You don't need to keep mentioning it, Hanna!"
    mike.say "Like I already said - any true friend would have done the same."
    "Hanna rolls her eyes as she chuckles at this."
    show restaurant meal -hannahappy
    hanna.say "You know you really have to stop doing that, [hero.name]."
    hanna.say "Just because you repeat it over and over again..."
    hanna.say "That still doesn't make it true!"
    show restaurant meal hannablush
    "Hanna reaches out with one hand, taking hold of mine across the table."
    "Then she gives it a tight squeeze, her smile becoming wider still."
    hanna.say "You gave me that loan because you're a very special kind of friend."
    hanna.say "The kind that's one in a million - once in a lifetime, even."
    hanna.say "I'm never going to forget that."
    hanna.say "And here's the first step on my path to repaying you..."
    show restaurant meal -hannablush
    "Without warning, Hanna pulls her other hand out from under the table."
    "And then she thumps it down in front of me, clutching a thick wad of bills."
    "For a moment, all I can do is blink at it in surprise."
    "But then I realise what it must be."
    mike.say "Hanna..."
    mike.say "Is that..."
    hanna.say "Every penny you loaned me, [hero.name]."
    hanna.say "And you can count it if you like."
    hanna.say "I won't be offended!"
    "I stare down at the wad of bills and then back up at Hanna."
    "And for a moment I'm totally lost for words."
    "Because this was the last thing I was expecting her to do!"
    menu:
        "I accept the money from Hanna":
            "I take a quick glance around the restaurant, hoping that nobody's seen the wad."
            "And then I reach out and take it from Hanna, figuring that's the best thing to do."
            "Hastily shoving it into one of the back pockets on my pants, I put an awkward smile on my face."
            $ hero.money += 1000
            mike.say "Ah..."
            mike.say "Thanks, Hanna..."
            mike.say "But I'm sure it's all there!"
            "Even though the money is now out of sight, I can still feel it."
            "Because the pocket I chose to put it in is now full to bursting."
            mike.say "You know..."
            mike.say "You could have just wired me the money."
            mike.say "Or even written me a cheque."
            show restaurant meal hannahappy
            "Hanna shrugs and smiles."
            "Clearly not picking up on my discomfort."
            hanna.say "Nah..."
            hanna.say "This way you'll always remember it!"
            "I spend the rest of the meal with the sensation of the wad against my ass."
            "And I'm already wondering what the hell I'm going to do with it."
            "Should I take it to the bank and try to deposit the whole lot?"
            "Or should I take it home and stuff it in my mattress in case of a future emergency?"
        "I do not accept the money from Hanna":
            "I take a quick glance around the restaurant, hoping that nobody's seen the wad."
            "And then I reach out and push it back towards Hanna, making sure I do so firmly."
            "This means she has no choice but to put the money back where it came from."
            "But I can see that she's more than a little puzzled by my actions."
            hanna.say "What's the matter, [hero.name]?"
            hanna.say "It's your money."
            hanna.say "Don't you want it back?"
            "I shake my head as I try to explain myself to Hanna."
            mike.say "Look, Hanna..."
            mike.say "I'm not trying to boast here."
            mike.say "But I really don't need the money back."
            mike.say "I'd like you to keep it - as a gift."
            show restaurant meal hannabored
            "Hanna looks totally stunned by this."
            "She blinks a few times."
            "Then she finally manages to reply."
            hanna.say "Okay, [hero.name]..."
            hanna.say "If that's what you really want."
            hanna.say "So should I put it back into the gym?"
            "I shrug my shoulders at this."
            mike.say "If that's what you think is best, Hanna."
            mike.say "But I'm cool with you doing whatever you want with the money."
            mike.say "It'll make me happy just knowing that I helped you out."
            show restaurant meal -hannabored
            "Hanna spends the rest of the meal in a slightly stunned state."
            "But I also note that she's staring at me more intensely than ever."
            "In fact she doesn't seem to be able to take her eyes off of me."
        "I insist Hanna reinvest the money in the gym":
            "I take a quick glance around the restaurant, hoping that nobody's seen the wad."
            "And then I reach out and push it back towards Hanna, making sure I do so firmly."
            "This means she has no choice but to put the money back where it came from."
            "But I can see that she's more than a little puzzled by my actions."
            hanna.say "What's the matter, [hero.name]?"
            hanna.say "It's your money."
            hanna.say "Don't you want it back?"
            "I shake my head as I try to explain myself to Hanna."
            mike.say "You said this investment helped the gym to get back up and running, right?"
            "Hanna nods at this."
            hanna.say "Yeah, [hero.name]..."
            hanna.say "We paid off all the debts and upgraded stuff that needed it badly."
            hanna.say "But we've more than made it back now."
            hanna.say "So you can have it back."
            mike.say "What if we reinvest the money in the gym?"
            mike.say "And you let me own a little piece of it with you?"
            show restaurant meal hannabored
            "Hanna looks totally stunned by this."
            "She blinks a few times."
            "Then she finally manages to reply."
            hanna.say "Okay, [hero.name]..."
            hanna.say "If that's what you really want."
            show restaurant meal -hannabored
            hanna.say "You'd be going into business with me!"
            "I nod and smile at the notion."
            mike.say "I like the idea of that, Hanna."
            mike.say "We get on well together, don't we?"
            mike.say "And I think we'd make good business partners too."
            "Hanna spends the rest of the meal in a slightly stunned state."
            "But I also note that she's staring at me more intensely than ever."
            "In fact she doesn't seem to be able to take her eyes off of me."
    return

label hanna_event_08:
    if hanna.love.max < 160:
        $ hanna.love.max = 160
    scene bg street
    show hanna date
    with fade
    "It's been one of those nights where everything just seems to go perfectly."
    "And so I hardly notice that time's passing, like it's flying by!"
    "Hanna's having a great time, laughing at my jokes and hanging on my every word."
    "Even while we're walking out of the restaurant and down the street outside."
    "In fact, she's so into what I'm saying it comes as a surprise when something else grabs her attention."
    mike.say "Erm..."
    mike.say "Hanna?"
    mike.say "Earth calling Hanna!"
    show hanna surprised at startle
    "Hanna seems as surprised as I was just a couple of moments ago."
    show hanna normal
    "But she soon shakes her head and smiles, returning to reality."
    hanna.say "Sorry, sorry..."
    show hanna annoyed blush
    hanna.say "I was just thinking about places like this..."
    "She nods towards the frontage of the building we're standing in front of."
    "And it's only now that I see it's a strip-joint."
    "Or to be more precise, the strip-joint I've been to a couple of times!"
    "I mean, I'm not like a regular or anything."
    "But someone working in there could have a good memory for faces!"
    mike.say "Oh...you mean the strip-joint?!?"
    mike.say "What about it, Hanna?"
    mike.say "I mean...what does it make you think about?"
    show hanna normal
    "Hanna nods and looks thoughtful."
    hanna.say "I just wonder what it's like to do something like that, you know?"
    hanna.say "Being on show in front of that many people the whole time!"
    mike.say "What do you mean, Hanna?"
    mike.say "You take classes at the gym every day."
    mike.say "Everyone taking part is looking at you the whole time."
    show hanna annoyed
    hanna.say "It's hardly the same thing, silly!"
    show hanna flirt -blush
    hanna.say "Those people are looking at me to copy what I'm doing."
    hanna.say "All that's on their minds is getting fitter!"
    show hanna normal blush
    "I can't help smirking a little at that statement."
    "I'm hardly thinking about getting fit when I watch Hanna in spandex."
    "And I don't know if she actually believes it herself."
    "That or if she's just trying to play the innocent."
    "So I decide to see what happens when I call her bluff."
    mike.say "Sounds like you're curious to see the inside of the place, Hanna."
    mike.say "So why don't we go in and you can see for yourself?"
    hanna.say "I...I suppose it wouldn't hurt."
    show hanna happy
    hanna.say "Okay...let's do it!"
    "I let out a burst of laughter at Hanna's response."
    "And that's because I was expecting to have to convince her just a little!"
    "All it needed was the slightest nudge."
    "And just like that, she's up for it!"
    show hanna normal at center, zoomAt(1.5, (640, 1040))
    "Hanna grabs hold of my hand and gives it a squeeze."
    "Then we walk straight up to the door and step inside."
    show bg stripclub
    $ game.room = "stripclub"
    scene poledance
    show hanna date normal at center, zoomAt(1.5, (640, 1040))
    with fade
    "I'm all ready to pretend like I'm not a regular at places like this."
    "But the look of excitement on Hanna's face means I don't need to bother."
    show hanna surprised blush
    "She's looking this way and that, her eyes wide with interest and amazement."
    "As always, there are girls in the skimpiest of outfits everywhere."
    "And then there's the usual crowd of patrons staring for all they're worth."
    mike.say "Are you okay, Hanna?"
    mike.say "I mean...most girls don't like this kind of place!"
    mike.say "We don't have to stay if it makes you feel uncomfortable."
    show hanna normal -blush at startle
    "Hanna shakes her head as she pulls me deeper into the strip-club."
    hanna.say "Don't be silly, [hero.name]!"
    show hanna happy
    hanna.say "This place is great!"
    hanna.say "No one can take their eyes off of those girls."
    hanna.say "It's like they're worshipping them or something!"
    show hanna normal at startle
    "All of a sudden, something seems to catch Hanna's eye."
    "She struggles to see what's happening on the stage."
    hanna.say "Why is there nobody using that pole?"
    hanna.say "The one up on the stage - why's nobody dancing around it?"
    "I shrug and then glance around, trying to find an answer."
    "And it doesn't take me long to spot a sign that explains the situation."
    mike.say "Looks like it's 'Open Pole Night', Hanna."
    show fx question
    hanna.say "Huh?!?"
    hanna.say "What does that mean?"
    mike.say "I guess it's like an open mike night, but with a pole!"
    mike.say "They want people to go up there and try their hand at dancing!"
    show hanna surprised blush
    "Hanna stares at me in amazement."
    "I don't think I've ever seen her eyes so wide and full of wonder."
    hanna.say "Do..."
    hanna.say "Do you think..."
    hanna.say "Should I go up there?"
    hanna.say "Should I try it myself?!?"
    menu:
        "Encourage Hanna to dance" if hanna.sub >= 60:
            "First she wants me to take her to a strip-club."
            "Now she wants my permission to get up there and dance around a pole!"
            "Is Hanna the greatest girl in the world or what?!?"
            mike.say "Of course you should, Hanna!"
            mike.say "You're drop-dead gorgeous - and you're in the best shape ever!"
            mike.say "And...wait a minute..."
            mike.say "Didn't you do pole-dancing classes at the gym too?"
            "Hanna's already beaming at the praise I'm heaping upon her."
            "But when she hears me mention the pole-dancing classes, she almost purrs like a cat!"
            show hanna happy
            hanna.say "I should have known you'd remember those!"
            hanna.say "And it sounds like you want an encore too!"
            hanna.say "Here..."
            hanna.say "Hold my drink..."
            show hanna normal
            hanna.say "Oh, and my clothes too!"
            "Before I can say another word, Hanna shoves her drink into my hand."
            "This is quickly followed by her clothes as she yanks them off."
            show hanna naked
            "And then she's sprinting towards the stage fully naked."
            "At first the rest of the patrons are as surprised as I am."
            scene poledance
            show poledance hanna naked
            with fade
            "But it doesn't take long for them to begin cheering."
            "And who wouldn't?"
            "An athletic blonde with a dynamite body literally just ran onstage."
            "No matter how good she is on the pole, that's worth seeing for its own sake!"
            "I push as close to the stage as I can get, fighting for a place."
            "And my efforts see me burst onto the very front row of the crowd."
            "I clap as best I can, the drinks and Hanna's clothes getting in the way."
            "She spots me instantly, making me think she was looking for me the whole time."
            "And now that she sees me, Hanna seems to take that as her cue to begin."
            "Right from the beginning she shows that she means business."
            "Hanna strides around the stage, wrapping herself around the pole."
            "I've watched that tight, sensual body moving at the gym so many time."
            "But seeing it here, under the strip-club lights, is somehow different."
            "Back at the gym I was sneaking glances."
            "I knew full well that staring openly was frowned upon."
            "Yet here Hanna's body is on show, being paraded in front of me."
            "And she's doing all she can to make sure that I'm not looking at anything else!"
            "Hanna twists and turns around the pole like a snake."
            "She uses her arms and legs to climb it, twirling the whole time."
            "One moment she's upside down, the next hanging off it sideways."
            "Her feet never seem to touch the ground!"
            "And all the time her muscles are flexing like steel fibres."
            "But somehow that does nothing to detract from her feminine allure."
            "If anything, the strength that Hanna's showing makes me harder than ever!"
            "That combined with the shape of her legs, her firm breasts and firmer ass..."
            "All I can think of is what she could do to me right now!"
            "In fact, I think everyone in the room is jealous of that damn pole!"
            "When Hanna finally rounds off her dance, it's to the sound of rapturous applause."
            scene poledance
            show hanna naked sweat normal
            with fade
            "She hurries off the stage and back over to where I'm waiting for her."
            "Hanna's panting and her skin is glistening with a patina of transpiration."
            show hanna normal at center, zoomAt(1.5, (640, 1040))
            "But she's still buzzing, loving the fact that all eyes are on her right now."
            "She takes her clothes from me one by one, dressing quickly."
            show hanna date -naked -sweat
            "And then she downs the rest of her drink in one, panting with exhaustion."
            mike.say "That..."
            mike.say "That was amazing, Hanna!"
            hanna.say "Yeah...I know!"
            show hanna happy
            hanna.say "It felt pretty amazing doing it too!"
            hanna.say "We HAVE to do this again - and soon!"
            "I nod eagerly, still unable to stop staring at Hanna with undisguised desire."
            "I want to tell her how hard my cock is right now and how much I want to fuck her!"
            "But maybe I'd better wait a little while to do that."
            "At least until she's got her breath back!"
            $ hanna.love += 2
            $ game.active_date.score = 100
        "Discourage Hanna from dancing":
            "People are always checking Hanna out - even when we're walking down the street."
            "So the last thing I want is to see her on stage in a damn strip-club!"
            mike.say "I don't know, Hanna..."
            mike.say "You're pretty athletic and all."
            mike.say "But pole-dancing is harder than it looks."
            show hanna sad
            "Hanna looks instantly disappointed at my lack of enthusiasm."
            "She frowns, beginning to pout at being denied the chance to show off."
            hanna.say "Hey!"
            show hanna angry
            hanna.say "We actually had pole-dancing classes at the gym, you know!"
            mike.say "Yeah, but this is different, Hanna."
            mike.say "You do those fitness classes with boxing moves too."
            mike.say "But that doesn't mean you can go twelve rounds with a heavyweight champ!"
            "Hanna lets out a snort of frustration at this."
            "But I can see that my words are sinking in."
            show hanna normal
            hanna.say "Okay, okay...you win!"
            hanna.say "I'll just stand here and watch."
            "What follows is pretty awkward."
            "Hanna and I watch as amateurs try their hand on the stage."
            "Some are pretty good and some are truly awful."
            "But most fall somewhere between the two extremes."
            "After a while, Hanna seems to decide that she's had enough."
            hanna.say "I'm feeling pretty tired, [hero.name]."
            hanna.say "How about you take me home?"
            mike.say "Erm...okay, Hanna."
            mike.say "If that's what you want..."
            "Well, that could have gone better."
            "As we leave, I weigh up the positives and negatives."
            "On the downside, I know I pissed Hanna off by not encouraging her to dance."
            "But on the other hand, I managed to talk her out of it and avert potential disaster."
            "So while she's giving me the quiet treatment right now, I think things could have been worse."
            "Which had to be a good thing, right?"
            $ hanna.sub += 1
            $ hero.cancel_activity()
            $ game.active_date.stay = False
    $ game.pass_time(2)
    return

label hanna_event_07a:
    if hanna.love.max < 140:
        $ hanna.love.max = 140
    "When I next see Hanna I'm still trying to get used to the five thousand dollar-shaped hole that she's put in my savings account."
    show hanna happy with dissolve
    "But as soon as I see how much better she looks since I let her have the loan, my misgivings about how sensible it was seem to somehow just fade away."
    show hanna at center, zoomAt (1.65, (650, 1140))
    "Hanna's positively beaming as she rushes up, a huge smile on her face and arms outstretched to throw them around me."
    "Although she takes me by complete surprise as her embrace pulls me close, I can't say that I'd have tried to stop her if forewarned."
    "Held so close against Hanna's body, I could swear that I can actually feel the renewed energy that's inside of her right now."
    "She holds me there for a minute or so, adding some very welcome squeezes to the hug, and then releases me with a light kiss to the cheek."
    hide hanna
    show hanna happy
    "Maybe I'd have liked more, but it's certainly a start..."
    mike.say "Okay, I'm going to take it from that that things are looking up for you!"
    hanna.say "They sure are, [hero.name]."
    show hanna wink
    hanna.say "And it's all thanks to you!"
    "I feel so gratified to be firmly in Hanna's affections right now that I almost forget the reason why."
    "But then I manage to shake off just enough of the effect that she's having on me to remember some of the finer details."
    mike.say "So you used the money to keep the wolves from the door?"
    "It takes Hanna a few moments to focus as well, and I see just a little of the elation disappear from her face as she does so."
    "No need to start panicking yet though, as it's probably nothing more than the effect of concentration that's doing it."
    show hanna normal
    hanna.say "Yeah, I did that - made sure I handled it myself."
    hanna.say "Dad didn't get anywhere near your money."
    "An instant sense of relief floods me, which I try to keep hidden for fear of making Hanna think I ever doubted her."
    mike.say "And what's next after that?"
    mike.say "What's step two of your plan?"
    "At this, Hanna looks a little awkward and sheepish, almost as though I've caught her out with the question."
    hanna.say "Erm...I guess that I have to start running things at the gym myself."
    hanna.say "I can't trust Dad to be anywhere near that side of the business anymore!"
    "Not bad, but it could have been a lot better."
    "I was kind of expecting her to have some kind of business plan thought out and know where she was going with this from here."
    "A part of me is starting to worry that I might have unknowingly bought myself part of a doomed venture."
    "Hanna might need some more help on my part, or else that five grand could be as good as gone."
    "But then, spending more time with her to give advice and having her even more in my debt could have its advantages..."
    mike.say "You should draw up a business plan to get out of this mess, Hanna."
    mike.say "Meet up with your accountant and have them bring you up to speed on everything too."
    "She nods at this, looking for all the world like it's a totally new concept for her."
    hanna.say "If you think that's what I should do, [hero.name]?"
    mike.say "It is, Hanna."
    mike.say "And what about your dad?"
    hide hanna
    show hanna surprised
    show fx question
    hanna.say "Huh...what about him?"
    "Jesus Christ - I think I'm starting to understand how Hanna and her father got into this position in the first place!"
    mike.say "Well, have you got him any professional help?"
    mike.say "He sounds like he's got a gambling addiction, and a serious one too."
    show hanna normal
    "Hanna nods, as if she's starting to understand where I'm going with this."
    hanna.say "Oh, yeah - he promised me he'd go to one of those gamblers anonymous groups."
    hanna.say "So that he could talk about it with other...other addicts..."
    mike.say "That's a start, but you have to make sure he keep his word, Hanna."
    show hanna sad
    "She nods, looking nothing short of daunted at the prospect of the task that lies ahead of her."
    mike.say "Don't worry, I'll be here to help you whenever you need me, okay?"
    show hanna normal
    "This seems to have the desired effect, and she's soon smiling again at the thought of having my shoulder to lean on."
    hanna.say "I'm so sorry to keep on dumping all of my problems on you, [hero.name]."
    hanna.say "But I really don't know what I'd have done without all of your help."
    mike.say "That's okay, Hanna."
    mike.say "What are friends for?"
    show hanna close
    "She wraps her arms around one of mine and leans in close to me."
    hanna.say "We are friends, aren't we, [hero.name]?"
    hanna.say "Really close friends..."
    "I swallow nervously, but can't help feeling a thrill at this show of affection towards me."
    "Maybe the payoff from all of this won't simply be the return of my savings after all."
    return

label hanna_event_07b:
    $ hanna.flags.sexywork = True
    if hanna.love.max < 140:
        $ hanna.love.max = 140
    "It's not like I really need an excuse to head down to the gym and see if Hanna's taken my advice about making some changes for the better."
    "I mean, I'm a member anyway, so I was already going to come along at least one day this week for my regular work-out."
    "Actually, if this thing comes off and the place sees a surge in business thanks to my advice, I may have to talk to Hanna about that."
    "If she gets enough new members signing up, surely they can afford to give me a freebie on my own membership fees?"
    "From the street, nothing much seems to have changed, but when I get inside, the first noticeable change comes as a slap in the face."
    "The member of staff behind the reception desk is one of the male instructors, and he's wearing what barely qualifies as a vest of tight, almost transparent material."
    "Okay, maybe not to my specific tastes, but sure to appeal to anyone partial to a fit guy in skin-tight clothing."
    "Looks like Hanna's taken my advice to heart and is really running with it!"
    "As I walk towards the changing rooms, I see some more subtle changes to the decor as well."
    "All of the posters for the more gruelling classes and straight-up subjects, like nutrition and fitness, seem to be gone."
    "In their place I see adverts for classes featuring glamorous models in skimpy work-out gear and even expensive brands of leggings and sports bras."
    "Funny - I never suggested any of that to Hanna..."
    "Once I'm changed and ready to go, I walk out into the gym itself and instantly see where most of the changes have been made."
    "Literally every single one of the trainers and instructors that I can see is dressed in the same fashion as the guy at reception."
    "Whether leading a class or giving individual advice to a patron, all of them have form-flattering lycra covering a very small portion of their firm, fit bodies."
    "The only material covering legs, arms and midriffs (if at all) is almost transparent and almost as alluring as the naked flesh on show."
    "But that's not the only thing that's different from how I remember the place being before."
    "The lighting feels like it's been subdued, and there are significantly more mirrors lining the walls too."
    "Thumping music fills the air, making the gym feel almost like the inside of a nightclub as people work out around me."
    "And a subtle change has been made in the machines I can see, as well as where they're stood."
    "Gone are all of the ones that were sure to make you look a fool when you used them and a sweaty mess afterwards."
    "In their place I see only machines that show off the human body as it bends and stretches in rather agreeable ways."
    "As people climb on and off what's left, it soon becomes clear that the machines are also positioned just so."
    "This means that a person using one can always see the most pleasing aspect of whoever's on the next, while also being checked out themselves at the same time."
    "All of this is pretty hard to take in at once."
    "So I find myself standing in a bit of a daze, not knowing where to start."
    hanna.say "Well, what do you think?!?"
    show hanna with moveinleft
    "In my state of confusion, I'd not noticed Hanna walk to me, let alone heard her start talking."
    hanna.say "[hero.name], hello - I'm standing right here!"
    mike.say "Yeah, Hanna, I see you now."
    show hanna happy at startle
    "She holds her hands up and gestures to the space around us, a smile on her face as she does a little turn."
    hanna.say "Ta-da...do you like what you see?"
    hanna.say "All of this was your idea, after all!"
    show hanna normal
    "What I can see right now is a pretty damn amazing view of Hanna as she turns around before me."
    "She's clearly included herself in the makeover that the gym's received."
    "Hanna's dressed in the exact same manner as the rest of the staff, and the sight is rather nice, to say the least!"
    "I swallow audibly, licking my lips as I try to think of something to say."
    "Specifically something that hasn't just sprung into my mind thanks to her flaunting herself in front of me."
    "Something that won't make me sound like a salivating degenerate..."
    mike.say "It's...it's...a lot to take in all at once!"
    mike.say "You've really taken my advice to heart."
    show hanna happy
    "Hanna practically beams at me, likely mistaking my dazed state for being overwhelmed with the state of the gym."
    "Rather than my being overwhelmed at the sight of her tight body in that incredible outfit!"
    hanna.say "I know - isn't it just!"
    show hanna sad
    hanna.say "Sure, some of the staff weren't on board to begin with."
    show hanna normal
    hanna.say "But most of them understood that we needed to make a change if we wanted to keep the place alive."
    "Finally managing to tear my eyes away from Hanna herself, I take a quick glance around the gym."
    mike.say "It's certainly buzzing in here."
    mike.say "I can't remember the last time it was this busy."
    mike.say "Or this loud..."
    "Hanna either doesn't pick up on the little jibe about the noise, or else chooses to simply ignore it."
    hanna.say "Yeah, we've seen things pick up in the past few days."
    hanna.say "You know - word of mouth, social media and all that."
    "I nod, unable to argue with what she's saying."
    "But, in the end, a small part of me still has to ask the inevitable question."
    mike.say "Hanna, you don't feel you're in danger of straying a little too far from the basic concept of an actual gym, do you?"
    mike.say "I mean, you could mistake this place for a nightclub if you weren't told what it was about."
    show hanna happy at startle
    "Hanna shakes her head, quickly dismissing my concerns."
    hanna.say "No way, [hero.name]!"
    show hanna normal
    hanna.say "We still do everything we did before, just with some extra attitude and swagger, that's all."
    show hanna wink
    hanna.say "It's like us showing off our bodies - we're only doing it to give our clients something to strive for!"
    mike.say "Okay, Hanna, if you say so..."
    show hanna normal
    "I keep trying to remember that this was basically my idea in the first place."
    "If Hanna's sure of what she's doing and where she's headed with this thing, then what is there to worry about?"
    "Maybe I should just go with it?"
    hanna.say "Okay, I gotta run - I have a class to take!"
    hanna.say "I'll talk to you later."
    show hanna happy
    hanna.say "Enjoy your work-out!"
    hide hanna with moveoutleft
    "I nod and wave a little nervously, then try to get on with doing just that."
    "Only it's surprisingly hard to remember a routine when there are just so many distractions surrounding you..."
    return

label hanna_event_07c:
    "When I finally get to meet up with Hanna again after she asked me for my advice regarding the gym, I'm expecting an update on her father and their financial woes."
    "But as soon as I set eyes on her, I can see that there's something else on her mind and another reason for wanting to see me."
    show hanna sad with dissolve
    "The look on Hanna's face is an odd mixture of tiredness and what looks like relief, as if she were freed of at least a portion of her former burdens."
    mike.say "Hanna, it's really great to see you."
    mike.say "I hope you've got some good news to share."
    "Hanna smiles, but there's a pain in the expression that just doesn't bode well for what she has to say."
    hanna.say "Yeah, [hero.name], I do."
    hanna.say "That and some not so good news..."
    "Seems that my suspicions were correct."
    mike.say "Okay - what's the good news?"
    "She sighs and then takes a deep breath, preparing herself to tell all."
    show hanna annoyed
    hanna.say "Well, I took your advice and sold the gym."
    hanna.say "I don't know if that's really good or bad."
    show hanna normal
    hanna.say "But it solved a lot of problems at a stroke - so let's call it good."
    "I nod, trying to look sympathetic while I prepare myself for what's to follow."
    hanna.say "As for my Dad, he's agreed to see a counsellor about his gambling problem."
    hanna.say "And he'll be going to one of those gamblers anonymous meetings every week from now on too."
    "She pauses, and I find myself wondering where the supposed bad news was amongst those things."
    "To me at least, they sound like a positive start for all concerned."
    show hanna sad
    "It's then that I realise Hanna's not done sharing her news with me."
    mike.say "So, Hanna - what's the bad news?"
    hanna.say "That's a little harder to swallow, [hero.name]."
    hanna.say "Obviously, with the gym sold on, I'm out of a job too."
    hanna.say "The new owners are letting me stay on for a while as a favour."
    hanna.say "But they can only employ me as an instructor, and not for the wage I was on as the boss's daughter!"
    "That makes sense, and I can understand why Hanna can't cope with having her income reduced so drastically."
    "Though it sounds a little less dramatic than she seems to be making it out to be."
    mike.say "So, what...you're looking for something better?"
    mike.say "There must be dozens of gyms that could use a manager with your experience?"
    hanna.say "Sure, there are lots of them."
    hanna.say "But the problem is that none of them are in town or within commuting distance of here either."
    "Ah, now I'm starting to see just what the bad news is here..."
    mike.say "I don't know what to say, Hanna."
    mike.say "I kind of feel like all of this is my fault."
    mike.say "After all, I was the one that suggested you sell the gym in the first place."
    show hanna at startle
    "Still looking sad, Hanna shakes her head and gives me a melancholy smile."
    hanna.say "You shouldn't, really you shouldn't."
    hanna.say "I think it was being stuck in the rut of that place that let my Dad's addiction get the better of him."
    hanna.say "We were both so comfortable and used to the routine, we never saw it coming - not until it was almost too late."
    "I feel conflicted now, sad for the losses that Hanna's suffered and guilty because I don't want to see her leave like this."
    "Honestly, I'd rather she wasn't leaving at all."
    mike.say "But, surely this isn't goodbye forever, is it?"
    mike.say "Wherever you find a new job, it can't be that far away."
    hanna.say "The gym where I've taken a position's in a town that's about a day's drive from here."
    "I nod again as that sounds promising, though I sense there's a but coming."
    hanna.say "But I'll need to devote myself to convincing them they can't do without me."
    hanna.say "So I can't say how long it'll be before I have the free time to even think about coming back to visit."
    mike.say "You won't know anyone there, Hanna."
    mike.say "Your whole life is right here!"
    hanna.say "Maybe that's for the best, as it'll mean I can make a new start, weed out the bad habits I've gotten into."
    mike.say "Sounds like your mind's made up."
    hanna.say "Yeah, I guess it pretty much is."
    "That's the end of it then, all of the possible arguments neatly cut off and done away with."
    "Hanna's really leaving, and she's doing so thanks to the consequences of my advice."
    "But do I actually have a right to be bitter about any of that?"
    "I gave the advice that I thought was best, and without a thought for what I wanted her to do myself."
    "And it seems to have addressed most of her problems too."
    "I guess that I need to grow up and realise that not everything is about me."
    show hanna normal
    hanna.say "I just thought that you deserved to be one of the first to know what I'd decided."
    hanna.say "And I wanted to say thanks, for being such a good friend and helping me save my Dad from himself."
    mike.say "That's okay, Hanna - what else are friends for?"
    show hanna at center, zoomAt(2.0, (640, 1340)) with dissolve
    "She leans in close and kisses me on the cheek, making me wish one last time that she was not leaving."
    hide hanna with dissolve
    $ hanna.set_gone_forever()
    return

label hanna_event_06:
    if hanna.love.max < 120:
        $ hanna.love.max = 120
    show hanna sad
    mike.say "Hanna...what's with you?"
    mike.say "You look like you've the weight of the world on your shoulders."
    show hanna at center, zoomAt(1.5, (640, 1040))
    "Hanna sniffles a little as she looks up at me, trying to force a smile with obvious effort."
    hanna.say "Oh, [hero.name]..."
    hanna.say "I'm sorry - I must look like such a mess!"
    "I shake my head and return her smile, dismissing her apology."
    mike.say "No...no, you just look a little tired, that's all."
    "It's a lie, of course."
    "Hanna looks bloody awful, but being blunt with the truth won't help her one bit."
    show hanna at startle
    "Hanna suddenly shakes her head, visibly pulling herself together through a sheer feat of will."
    hanna.say "It's okay - really."
    hanna.say "It has to do with what's got me into this state anyway."
    "Still wearing the same forced smile on her face, Hanna hastily wipes the corner of her eyes with the back of her hand."
    hanna.say "Right, here goes!"
    "I nod, almost holding my breath as I brace myself to hear some really bad news."
    hanna.say "It's about the gym."
    "Wait...what - did she just say the gym?"
    "What on earth does she need to tell me that badly about the gym?"
    "And the thought suddenly occurs to me..."
    mike.say "Hanna, is this about my gym fees?"
    mike.say "Because if it is, I honestly thought I was paid up to date!"
    mike.say "Normally they'd send me an email, or a text or something."
    mike.say "No one ever asked me for the money in person before!"
    "Hanna looks at me in disbelief, and then shakes her head."
    hanna.say "No, [hero.name], I don't want to talk about your gym fees!"
    "A mixture of relief and embarrassment floods through me as I realise how completely I've misread the situation."
    mike.say "Ah...right...sorry, Hanna."
    hanna.say "What I need to talk to you about is the gym itself."
    hanna.say "But it's hard for me, as the problem's, well...personal."
    mike.say "I'm listening, Hanna - whatever you have to tell me, I won't pass it on to another soul, I promise."
    "She nods, still not looking much happier about the situation, but determined to continue."
    hanna.say "It's my Dad, you see, he's always had a weakness for gambling."
    hanna.say "In the past it was never a big deal, never a lot of money, so I kind of ignored it."
    hanna.say "Likewise, he always hid the exact sums from me too."
    hanna.say "It was the elephant in the room, you know."
    "Oh dear - I think I can see where this is going, and it's not going to be good."
    hanna.say "But recently he's been getting worse, making bigger wagers with crazier odds."
    hanna.say "And he's been stealing money from the business to pay for it all."
    mike.say "Jesus, Hanna - how bad is it?"
    hanna.say "Bad - the gym needs around five grand, and that's just to keep the doors open."
    "All I can do is raise my eyebrows and blow out my breath in sheer amazement."
    mike.say "That's a lot of money, Hanna!"
    show hanna at startle
    hanna.say "You don't have to tell me!"
    hanna.say "So, what in the hell should I do?!?"
    menu:
        "You should sell it":
            mike.say "It sounds to me like anything you do to keep the business going is just a temporary solution."
            mike.say "You're not going to like this, Hanna - but I think you should cut your losses now."
            show hanna surprised at vshake
            "A shocked look appears on Hanna's face as the reality of what I'm saying sinks in."
            hanna.say "[hero.name], you can't mean..."
            mike.say "Yes, I do - I think that you should sell the gym to settle the debts."
            mike.say "That and make sure that your father can't get access to the money anymore."
            show hanna sad
            "Hanna shakes her head, the tears that were only a suggested before threatening to make an imminent return."
            hanna.say "But, [hero.name] - my Dad built that place up from nothing, it's all I have!"
            mike.say "I understand that, Hanna, I do."
            mike.say "But if you carry on like this, you'll end up watching your father destroy everything he built."
            mike.say "Make a clean brake of it now, and get him the help he needs, before it's too late."
            "She nods sadly, finally beginning to see the sense in my words."
            hanna.say "Maybe you're right, [hero.name]."
            hanna.say "It hurts real bad, but if I change things around him, perhaps it'll help to break the old habits?"
            "I give her a nod and a reassuring smile, placing my hand atop her own."
            "But I don't press my advice on her with any more force, knowing that I've given her a lot to think about already."
            $ hanna.flags.gymSolution = "sell"
        "I can lend you that money" if hero.money >= 5000:
            mike.say "You said that with 5 grand you could keep the place going, right?"
            show hanna normal
            "Hanna looks at me with the light of hope suddenly shining in her eyes."
            hanna.say "Yes...yes, that's right."
            hanna.say "That much could pay the bills and give me the breathing space I think I need."
            mike.say "Hmm...I could probably afford to lend you that much from my savings."
            mike.say "And I'd be more understanding than any bank when it came to being paid back."
            show hanna surprised blush
            hanna.say "Really?"
            hanna.say "You'd do that, for me?!?"
            "I have to be careful here, as she's vulnerable and desperate right now."
            "It'd be far too easy to get swept up in her rather manic gratitude and promise the Earth."
            mike.say "Sure, Hanna - what are friends for?"
            "I shrug, trying to make the whole thing sound like it's no real hassle, like I do this kind of thing all the time."
            "But in reality, it's a pretty big gamble on my part, and there's no guarantee I'll ever see the money again."
            "I have to wonder, would I even be making an offer like this if it were a male friend in the same kind of mess."
            show hanna happy at startle
            hanna.say "Oh, thank you, thank you, thank you!"
            hanna.say "You won't regret this - I promise!"
            "For all that I'm smiling right now, I can't say I share her optimism."
            $ hanna.flags.gymSolution = "lend"
            $ hero.money -= 5000
            $ hanna.love += 10
        "You could make it more attractive" if hanna.sub >= 25:
            mike.say "Well, there is one idea that springs to mind."
            mike.say "It'd probably give the business a shot in the arm."
            mike.say "But...ah, I'm not sure it's your kind of thing..."
            "I can see the look of desperation in Hanna's eyes, as clear as the fact that they're blue."
            "She's so desperate for any solution to her problems that she'll grab at whatever straws float past."
            "I just need to be careful here, make sure she takes the bait and I reel her in gently."
            show hanna normal
            hanna.say "No, really - what is it?"
            hanna.say "A fresh idea might be just what the place needs!"
            mike.say "Okay, okay."
            mike.say "Well, you're a gym."
            mike.say "And gyms basically sell the chance to have a fit body, right?"
            "Hanna nods at this, almost too readily."
            mike.say "So when you go to, say...a showroom to buy a car, they have the goods on display."
            "Hanna nods again, but begins to look a little less sure of what I'm saying."
            mike.say "You need to do that too - have the great body that people can get working out there on show."
            hanna.say "You mean we should..."
            mike.say "Have the fitness instructors wear stuff that shows off their perfect physiques."
            show hanna annoyed blush
            hanna.say "But, [hero.name], we already wear lycra at work."
            hanna.say "And that doesn't leave much to the imagination, believe me!"
            mike.say "Sure, Hanna, I get that."
            mike.say "What I'm talking about is getting rid of all those needless sleeves, legs and bits covering up the abs."
            show hanna surprised
            hanna.say "You mean we should wear more revealing stuff?"
            "I nod emphatically at this."
            show hanna annoyed
            hanna.say "But...wouldn't that be unprofessional, maybe even...I don't know, sleazy?"
            mike.say "Of course not!"
            mike.say "This is the twenty-first century, Hanna - we're living in an open-minded age."
            mike.say "The gym just needs to reflect that, to capitalise on it, that's all!"
            show hanna normal
            "Hanna nods, and I can see her weighing up all that I've said."
            "With any luck, I've managed to talk her round to my way of thinking."
            "All I need to do then is be supportive and understanding in order to watch the changes take place down at the gym."
            $ hanna.flags.gymSolution = "lewd"
            if hanna.sub.max < 50:
                $ hanna.sub.max = 50
    return

label hanna_event_05:
    if hanna.love.max < 100:
        $ hanna.love.max = 100
    "When I work out, I tend to like to do so alone, save for the music that I'm listening to at the time."
    "Modern life's so hectic and stressful that you need that head-space to just chill out for a stretch."
    "I know a work-out's not exactly relaxing, but sometimes you can only rest from one intense activity by doing another."
    "And that's why it seems odd that I find Hanna waiting for me when I walk out of the locker-room at the gym today."
    show hanna with dissolve
    mike.say "Ah...hey, Hanna."
    mike.say "You waiting for someone?"
    mike.say "New client wanting some one-on-one coaching?"
    "Hanna shakes her head, completely dismissing my guesses."
    hanna.say "Nope, not today."
    hanna.say "I was just gonna do a quick round of the machines."
    hanna.say "And I wondered if you wanted to join me?"
    "I shrug, trying to look nonchalant while actually feeling more than a little suspicious."
    mike.say "Sure, Hanna."
    mike.say "I could use the company."
    show hanna happy
    "If Hanna notices my surprise at her offer, then she manages to conceal it pretty well."
    "You might think that I sound paranoid, but this is out of the ordinary for her."
    "I know full well that Hanna never normally works out at the gym during business hours."
    "She's always too busy taking a class or dealing with some other aspect of her job there."
    "So the notion that she'd just happen to catch me like this is hard to credit."
    show hanna normal at left5 with move
    "As we walk over to the first of the machines, I try to sound casual and relaxed."
    mike.say "I have my routine pretty much worked out for today."
    mike.say "But I can change it up a bit, if you had something specific in mind?"
    hanna.say "No, no, it's fine."
    hanna.say "You just go right ahead."
    hanna.say "I'll follow your lead, okay?"
    "Curiouser and curiouser..."
    "I nod and do as I'm told, starting my routine as normal."
    "But I can't help finding it odd that Hanna's happy to follow me around the gym."
    "I know for a fact that she's far more of a fitness fanatic than I am."
    "My routine should be way beneath even her most casual of work-outs."
    "More like a warm-up in comparison!"
    "I start more slowly than usual, looking over my shoulder at Hanna as I do so."
    show hanna happy at startle
    "She smiles back as she mounts the machine next to me."
    show hanna normal
    "But I can already see that she's deliberately hanging back."
    "Short of stopping completely and demanding to know what's up, I have no other option but to go on."
    "And so I shake my head and try to lose myself in the familiar routine of my work-out."
    show hanna blush
    "This works for a short while, but then I happen to look round and notice what Hanna's up to."
    "Okay...okay, I'll be honest."
    "What actually happens is that I look round to check her out as she's using the same machine as me."
    "I know just what it does to the human body, and I want to see it do the same to Hanna."
    show fx heart at left5
    "It's then that I realise she's doing the exact same thing to me!"
    show hanna annoyed
    "Sure, she looks away as soon as I turn my head in her direction."
    hide fx
    "But the way she tries to bury herself in the work-out at the same time is a dead giveaway."
    show hanna normal
    "At first I don't know how I should feel about the whole thing."
    "Sure, I've been guilty of checking out girls at the gym quite often."
    "And I've always wondered if anyone returned the favour."
    "But now that I actually know someone's doing it to me right now, I feel kind of thrown!"
    "One thing I do know is that I'm not about to stop what I'm doing and complain to Hanna."
    "That'd make me feel like a hypocrite and look like a prude!"
    "I guess that I should really be flattered by the attention."
    "After all, it's not like I don't feel the same way about Hanna's body too."
    "She's hardly some random stranger that's taken to ogling me out of the blue."
    "This is the twenty-first century, so why shouldn't a girl feel that she can check out a guy?"
    show hanna sweat at right5 with fade
    "With this in mind, I power through the rest of my work-out, trying not to think about it too much."
    "I resist the temptation to give Hanna more of a show than she's already getting."
    "I mean, I'm not a dancer wanting her to shove bills into my shorts."
    "And trying too hard in that department might clue her in to me being aware of what she's doing."
    show hanna at center with fade
    "Afterwards, I make an effort to sound casual and unaware."
    mike.say "How did you find it, Hanna?"
    mike.say "See anything that you liked in my routine?"
    show hanna happy at startle
    "She nods, seemingly taking what I say at face value."
    hanna.say "Oh sure, [hero.name]."
    hanna.say "There were even a couple of things I want to see more of too."
    show hanna flirt -blush
    hanna.say "Maybe you could show them to me in a private session?"
    hide hanna with moveoutleft
    "And with that, she walks away, leaving me to wonder at the exact nature of her meaning..."
    return

label hanna_event_04:
    if hanna.love.max < 80:
        $ hanna.love.max = 80
    "So yeah, I've been running for a couple of months now and getting steadily more serious about it the whole time."
    "Just to be clear, I'm not ashamed of it and I only choose to run in the early morning because it's quieter then."
    "Well...maybe I am a little embarrassed about it - but only a little!"
    "You see, I'd always been one of those guys that sneered at self-righteous jerks running around in spandex."
    "But I'm not getting any younger, and it's a cheap, easy way to get some exercise without going all the way to the gym."
    "I just didn't want anyone else to know about it until I was fully at ease with it myself, that's all."
    "Maybe I just don't know many fellow joggers, or maybe they live too far away to run in the same park as me."
    "Either way, it was working out pretty well too, as no one bumped into me on my runs."
    "That was until one morning, when I was only a couple of hundred metres into my usual route."
    hanna.say "[hero.name]...hey...[hero.name]!"
    "I have my earbuds in, listening to some podcast or another."
    "This means I don't notice Hanna until she literally jumps out in front of me."
    show hanna sport at center, zoomAt(1.65, (660, 1140)) with moveinright
    with hpunch
    mike.say "Arrgh...fuck!"
    hanna.say "Whoa, don't shit yourself, [hero.name]!"
    "I pull my earbuds out, trying to pretend that my heart's only pounding from the effects of my run so far."
    mike.say "Jesus, Hanna!"
    mike.say "Don't do that to me..."
    "Hanna chuckles in response, as if she's unable to take anything I'm saying seriously."
    "Sometimes I forget she has that annoying habit so common to sporty types."
    "The terminal inability to see annoyance in others as anything other than amusing banter."
    "But then I become suspicious, narrowing my eyes at her."
    mike.say "Wait a minute - what are you doing here?"
    hanna.say "What does it look like to you?"
    "At this, Hanna makes a point of trotting around me in a tight circle."
    "I follow her, turning around slowly as she goes."
    "It takes me a few moments to realise that she's actually dressed for a run too."
    "But then I'm so used to seeing her in sportswear."
    "It can be genuinely hard to tell exactly what she's up to at any given time."
    mike.say "I didn't know that you ran here, Hanna."
    mike.say "I've never seen you before."
    show hanna happy at startle
    "Hanna shrugs at this, shaking her head and smiling."
    if not hanna.flags.knows_mike_runs:
        hanna.say "I didn't know that you ran at all."
        hanna.say "So I guess that makes it even!"
    with hpunch
    "She gives me a little punch on the arm, just to underline what she's said."
    "But I try to ignore the gesture, and the fact that it hurts more than I expected it to."
    mike.say "Seriously though - you haven't moved to my neighbourhood, have you?"
    show hanna annoyed
    hanna.say "No, I just got bored of all the routes near my place."
    show hanna normal
    hanna.say "So I hopped in the car to check out some new ones."
    show hanna happy
    hanna.say "It's just a bonus that I bumped into you."
    mike.say "Erm...a bonus?"
    hanna.say "Sure it's a bonus, [hero.name]."
    hanna.say "It means you can be my running partner!"
    mike.say "I...I guess so..."
    show hanna wink
    hanna.say "But I won't go easy on you just because we're friends!"
    hide hanna
    show hanna happy sport with dissolve
    pause 1.0
    hide hanna with moveoutleft
    "And with that, she's off, laughing back over her shoulder at me."
    scene expression f"bg {game.room}" at center, blur(10)
    "Without thinking, I take off after her, pushing myself to catch up."
    "I know it's a pretty dumb thing to do, letting her get under my skin like that."
    "But there's just something about Hanna, that need of hers to be the centre of attention and best at everything."
    "It makes me shake my head in despair at the best of times."
    "It can be cute, even endearing when she's just after attention and validation."
    "But this is where I come for some alone time on a morning, before I face the stresses of the day."
    "Who does she think she is, barging in on me like that?"
    show hanna sport at left with dissolve
    "As I catch up to Hanna, I try to keep two things in mind."
    "One is that she's a terrible show-off, and she'll be trying her best to keep my eyes on her the whole time."
    "The other is that, fit as she undoubtedly is, I know this park far better than she does..."
    "I begin slowly, letting Hanna think that she's got the measure of me."
    "My eyes are seldom off her body, watching her bounce and jiggle beneath her spandex."
    "But the difference is that I know the course we're running by heart."
    show hanna at center with ease
    "This means that I can pace myself for what's up ahead without the need to look away."
    "Hanna, on the other hand, is much too busy smiling at my ogling her to note anything of the kind."
    "And don't get me wrong - I am ogling her!"
    "It's just that I also have an ulterior motive for doing so right now."
    show hanna surprised at right with ease
    "Hanna only seems to notice that there's something wrong when she actually starts to drop behind."
    show hanna angry blush at right4 with ease
    "She makes an impressive attempt to rally, but by then it's too late."
    scene expression f"bg {game.room}" with fade
    "I finish the course a full thirty seconds before Hanna comes puffing up the hill where I'm waiting."
    show hanna blush sweat sport surprised at right with moveinright
    "Hands on her thighs and bent over double, she sucks in great lungfuls of air as she tries to recover."
    show hanna at center, zoomAt(1.65, (660, 1140))
    hanna.say "That was...pretty...amazing...[hero.name]..."
    hanna.say "Where've you...been hiding...all that stamina?!?"
    "I shrug casually, trying not to come over like too much of a smug arsehole."
    mike.say "Oh, it's nothing like that, Hanna."
    mike.say "I probably just know this place that well."
    mike.say "I do run here most mornings, after all..."
    show hanna normal
    "By now, Hanna's managed to stand up and almost catch her breath."
    hanna.say "Sure...thing, [hero.name]."
    show hanna flirt
    hanna.say "Makes me wonder what else you have that much stamina for..."
    return

label hanna_event_03:
    if hanna.love.max < 60:
        $ hanna.love.max = 60
    show hanna with dissolve
    "After a long work out, I can't help but notice just how much Hanna looks at me as I wipe my brow."
    hanna.say "[hero.name], do you want to get cleaned off?"
    mike.say "Heh, and here I thought you liked being dirty."
    show hanna wink at left with ease
    "She smirks at that and turns around heading towards the women's locker room."
    hanna.say "Alright, then, see you next time!"
    hide hanna with moveoutleft
    "I shrug and make my way back to the locker room."
    scene expression f"bg {game.room}" at center, blur(10)
    play sound shower loop
    "There, I undress and get into the shower."
    "Nothing quite like washing off after a great workout, that's for sure!"
    "As the water washes over me, the curtain opens quickly, and standing there just on the other side is Hanna, biting her lip and dressed in her white gym gear still."
    show hanna blush sport bottomless with easeinleft
    hanna.say "Hey there, [hero.name], mind if I join?"
    menu:
        "I mind":
            mike.say "H... Hanna!? I'm just taking a shower! What are you doing?"
            show hanna surprised at startle
            hanna.say "W... what? Oh, I'm sorry, shit! Fuck!"
            show hanna blush sad
            pause 1.0
            hide hanna with moveoutleft
            "She throws the shower closed and runs out of the room, her face beet red."
            "I think I might have fucked up."
            $ hanna.love -= 5
        "I don't mind":
            "I step back and usher Hanna inside."
            show hanna at center, zoomAt(2, (640, 1380)) with dissolve
            "She slowly steps on in, pressing her body up against mine, water puddling up on her chest as she sighs out."
            show hanna flirt -blush
            hanna.say "I've been wanting to do this since our first rep."
            hide hanna
            show hanna bj a outfit
            with fade
            "Soon, she slides down along my body, painting my chest with her tanktop."
            "The water spills out between and over her breasts, the white outfit getting heavy and transparent as it sticks to her body."
            "It's almost as if she isn't wearing anything, but much, much hotter!"
            "Her breasts run down over my cock."
            show hanna bj b
            "It springs free from between her breasts, quite ready for the attention now."
            "As the water rolls down her face, she looks up to me with half-lidded, lustful eyes."
            "She leans in, breathing with heated breaths over my skin."
            show hanna bj suck
            "The hunger in her eyes is real as she takes in my member."
            "She hums, groaning louder than the spray of water as she puts her hands off of my thighs and over her tits."
            "Her lips wraps around the head of my cock as she starts to bob up and down along my length, always looking up at me as she does it, seeking my approval, craving my satisfaction."
            "The wet fabric wraps around my flesh. Honestly, I can't say I've ever felt something quite like it before."
            show hanna bj a open
            "The softness of her breasts mix with the rough stickiness of her top."
            "I wince as it catches my skin a moment, but she laughs, pulling away from my length."
            hanna.say "Haha... yeah, a stupid idea."
            show hanna bj -outfit wet
            "Blushing, she peels her shirt upward and above her head."
            show hanna bj b
            "As any red-blooded man would do, I take the opportunity and slide my dick on in between her tits until it pops out from her cleavage."
            show hanna bj suck
            show mouth_insert hanna zorder 1 at zoomAt(1, (860, 140))
            "Now basically wearing my cock, she wraps her lips around it again, never breaking her eye contact through that entire exchange."
            "How long she goes without blinking, even in the shower, is crazy."
            "Now that her nice big tits wrap around my dick, with no sticky shirt to mess with me, I get more bold, and thrust forward."
            "She groans at the sudden increase in force, but takes it like a champ, bobbing her head over and over in the repetitive motions that only a fitness nut could truly appreciate."
            "Like I'm some kind of weights, she keeps up her tit reps."
            "She does give her body quite the workout as her tongue lashes under the head and up along the sides."
            "But even if a great athlete paces, it becomes impossible to hold out forever, and just like the runner who used too much of his speed at the beginning of the race, I can't keep it up myself."
            hide mouth_insert
            show hanna bj b cumshot with vpunch
            pause 1.0
            with vpunch
            "Instead, I yank her back, shooting my load all over her face."
            show hanna bj bodycum closed with vpunch
            "Hanna groans in a loud and lewd cry as my cum mixes with the water already raining down on her face."
            show hanna bj a -cumshot open
            "Soon enough, it will all wash away, but not before she runs her hands up over her cheeks and shudders."
            hanna.say "Aaah, nothing like the signs of a good workout."
            hanna.say "The body perspires... the muscles ache, the eyes grow heavy, and the cock shoots its load."
            hanna.say "It's wonderful, isn't it? What the body can do?"
            "I chuckle at that and sigh, leaning back against the shower."
            mike.say "Yeah, it is. But come here. Looks like you need a shower now, yourself."
            hide hanna
            show hanna blush sport sweat at center, zoomAt(2, (640, 1380)) with dissolve
            "Hanna hops up, wrapping her arms around me and pressing her chest against my body."
            "She nuzzles against me a bit, letting the water hit over our flesh for a bit longer before finally pulling away."
            hanna.say "Alright, well, could you get my back, [hero.name]?"
            "I grab the soap, delighted to do so."
    stop sound fadeout 1.0
    return

label hanna_event_02:
    if hanna.love.max < 40:
        $ hanna.love.max = 40
    $ hanna.unhide()
    "Well, here I am. Better get that membership renewed."
    "Can't let my gains go to waste..."
    show hanna normal at center, zoomAt(1.25, (640, 1040)) with dissolve
    mike.say "No way."
    "Sitting at the desk is the girl from the locker room, the one who flicked her bean while I was taking a shower."
    "What the hell would she be doing here?"
    show hanna surprised at startle
    "She looks up a moment, her eyes widening when she sees me."
    "Oh, great, now we're both caught in the headlights."
    mike.say "Uh... H-hi!"
    "I blurt out, pulling out my card."
    mike.say "I, uh, need to renew!"
    show hanna normal
    "She sighs and runs a hand through her blond hair, ushering me forward."
    "Girl" "Ah, a-alright. Welcome to The Gym. I'm Hanna. So, let's see, [hero.name], right?"
    "She talks while clacking away at the keyboard."
    menu:
        "Yes":
            mike.say "That's right."
            "I slide the membership card over towards her, real professional-like."
            "She doesn't even look at it as she puts in information into the system."
            "Trying to figure her out is going to be difficult."
            "It's not everyone who tries to pleasure themselves to you and you don't even know their name."
            mike.say "So, not often I see one of the members working at the desk. What's up with that?"
        "No":
            mike.say "Actually, no, that's not my name."
            show hanna surprised
            hanna.say "W... what?"
            show hanna blush
            "She turns bright red, glancing over towards my card, and then shooting me a glare."
            hanna.say "He-hey, what are you trying to do here? Are you messing with me?"
            "I chuckle..."
            mike.say "Just seeing if you were paying attention."
            show hanna annoyed
            "She rolls her eyes, and then types in the system."
            show hanna normal
            mike.say "I'm not the only one being deceptive, you know. Here, I thought you were a member, not a worker."
            $ hanna.love += 5
        "How do you know?":
            mike.say "How do you know my name? I don't' remember giving it to you."
            show hanna blush
            "She blushes at that, but types furiously into the system."
            "Obviously, I struck some kind of nerve. What is her game?"
            $ hanna.sub += 5
    show hanna normal -blush
    hanna.say "Ah, well, that. That's easy."
    hanna.say "My dad owns the gym."
    hanna.say "I work here from time to time, you know, when I'm not working out."
    mike.say "Ah, that makes sense."
    "Her tanktop is loose and I can nearly see all the way down to her nipples."
    hanna.say "The payment method the same?"
    mike.say "Uh, yeah!"
    mike.say "Everything the same."
    mike.say "Nothing I'd want to change around here, payment, machines, and staff."
    show hanna happy
    "She smiles at that and nods."
    show hanna normal
    hanna.say "You're all updated. The card should still work! Hope you have a great day!"
    menu:
        "See ya":
            mike.say "Alright, cool."
            mike.say "Gonna go to the locker room now."
            mike.say "Gotta get my workout on."
            mike.say "Is there anyone in there right now?"
            "She pauses a moment, her face a blank mask a moment before she smirks."
            hanna.say "No. You'd be all alone in there."
            "And with that, I give her a nod and walk away."
            hide hanna with dissolve
            "Even if I wanted to pursue something with her, perhaps while she's working and has my access to the gym in her hands isn't the best time?"
            "I may be pressing it by teasing that I know her secret."
        "About treadmill":
            mike.say "You know..."
            mike.say "I couldn't help but notice that you were checking me out the other day..."
            show hanna annoyed blush
            "Her eyes get really shifty at that."
            hanna.say "Aah, what? What are you talking about?"
            mike.say "Oh, you know... when you were on the treadmill."
            show hanna surprised
            "Hanna's fingers curl and she blows out a huge breath."
            hanna.say "I... did what?"
            mike.say "Yeah, you were stealing some glances, weren't you?"
            show hanna annoyed
            "She looks off to the side a moment, scratching her cheek."
            hanna.say "I'm... not supposed to ogle the customers."
            "But you did... and I liked it."
            "For a moment, she says nothing, but she takes her hands off of the computer and places them upon her knees."
            $ hanna.love += 5
            hanna.say "I... I really need to get some work done."
        "About locker room":
            "Perhaps now that we're finally confronting each other for the first time, I can actually get some answers out of her."
            mike.say "You know..."
            mike.say "I have been meaning to talk to you for a little while now."
            show hanna surprised
            hanna.say "O... oh, why is that?"
            show hanna annoyed
            "She asks, though the way she bites her lip lets me know she is anticipating the exact question I am about to give her."
            mike.say "Well, I wasn't sure what you were doing at first. I thought maybe you were lost and went to the wrong locker room."
            show hanna at startle
            "She squirms in her chair, her hands moving to her knees, gripping them tightly."
            mike.say "But then, I heard you calling out my name... that was pretty weird, too."
            mike.say "But now that I know that you actually WORK here, things are starting to come together."
            show hanna surprised blush
            "Her face turns beet red as she stares up at me, though her lips part."
            hanna.say "Aah.... Ha...."
            mike.say "But there you were, lying on a bench, sniffing my stuff, and fingering yourself."
            show hanna at center, zoomAt(1.5, (640, 1140))
            "I lean closer into the table."
            mike.say "I just couldn't help myself but watch you."
            "I continue, chuckling when she pushes herself back a bit."
            show hanna annoyed
            hanna.say "I... I'm sorry."
            mike.say "Don't be."
            mike.say "I'm going to exercise now. Enjoy your work. I'll see you later."
            hide hanna with fade
            "I turn to leave."
            hanna.say "Wait!"
            show hanna surprised blush at center, zoomAt(1.25, (640, 1040)) with fade
            "I stop and turn around. She has clasped her hands together, surprised at how loud she actually was."
            hanna.say "Let's..."
            show hanna normal
            hanna.say "Let's talk about this, when I'm off work. Here..."
            "She scribbles something down and hands me the sticky note."
            hanna.say "My number."
            show hanna wink
            hanna.say "Call me when you want us to talk."
            "I smile and give her a wave. Perhaps I'll let my exercise wait for the day?"
            $ hanna.sub += 5
            $ hero.smartphone_contacts.append("hanna")
    return

label hanna_sub_event_01:
    if hanna.sub.max < 75:
        $ hanna.sub.max = 75
    "I haven't really hit the gym for a serious workout since Hanna came to me and confessed about the mess that it was in."
    "At the time, she was pretty keen to take me up on my advice that spicing up the atmosphere might lead to an upturn in business."
    "And while I got a good look at the changes that she made in light of this, I never actually used the facilities when I did so."
    "I guess that I was a little nervous to show my face, afraid that the place might have ended up like a morgue."
    "But eventually, I gather my courage and grab my workout gear, heading out of the door and down to the gym."
    "And when I do, I'm more than pleasantly surprised to find the place busy and humming with patrons."
    "A quick glance around shows me that Hanna's nowhere to be seen right now."
    "So with a shrug, I make for the male locker-room and change into my gym clothes."
    "Almost as soon as I walk out onto the floor of the gym and head for the first machine in my routine, I can feel it."
    "The new vibe that's running through the entire place, giving it an energy and excitement that it never had before."
    "I don't know if it's the mirrors on the walls, the subdued lighting or the subtle music that's pumping out of the speakers."
    "Or maybe it's the fact that the trainers are walking about in hardly enough spandex to protect a gnat's modesty."
    "But whatever the reason for it, I can see that Hanna's one hundred percent committed to making this thing work!"
    "I'm on the machine that I need and already halfway through my reps when it happens."
    "Looking up from the business of working up a sweat, I catch sight of Hanna across the gym floor."
    "And as she walks amongst the frenetic activity going on around her, I feel myself slow down and then stop in my tracks."
    "Okay, I'll hold up my hands and admit that I had a good long look at the female trainers working today."
    "What do you expect - I'm only human, after all!"
    "But the sight of Hanna dressed in the same manner hits me like a slap to the face."
    show hanna a close at top_to_bottom with dissolve
    "I know full well how much she likes to have admiring eyes on her."
    "So she must be loving every single moment of this!"
    "She looks amazing..."
    show hanna a close at bottom_to_top
    "No, that's not going to cut it."
    "She looks fucking AMAZING!"
    "Even as far away as she is right now, I can already feel myself getting hard at the sight of her."
    hide hanna
    show hanna at right with dissolve
    "Hanna seems to be surveying the gym floor as she walks across it, looking here and there."
    show hanna annoyed at right5 with ease
    "Which makes sense, as she's the boss around here, and needs to keep her finger on the pulse."
    show hanna normal at right4 with ease
    "But I guess I must be pretty obvious, staring at her like I am."
    show hanna happy at center with ease
    "As she pauses and meets my eye on her way past, smiling and offering me a quick wave in way of greeting."
    "I feel myself swallowing at this, more than a little guilty at checking her out so shamelessly."
    "All the same, I still manage to return the gesture before Hanna gets distracted."
    show hanna annoyed at left with ease
    "I see a male patron catch her attention, and she tears herself away from me to see what he needs."
    "Taking this as an excuse to get back to my workout, I hit the machine with redoubled fervour."
    hide hanna with dissolve
    "Maybe if I try hard enough, I can exercise the image of Hanna and her spandex-clad body from my mind?"
    "But no more than a minute or so after I get back into it, I can't help glancing her way again."
    show hanna at left
    "I can see that she's showing the guy that distracted her how to program a step-machine."
    "He's nodding away like he should, but even I can see his attention is more focused on Hanna than the machine."
    "And when she steps onto it to show him how it moves, his eyes are literally fixated on her ass and thighs."
    "Then I see him point to her flexing muscles, as if he's asking her what it works on."
    show hanna surprised at vshake
    "She seems to answer him, but then I see her jump, as if shocked."
    "And I notice that the guy's got his hands on her buttocks, squeezing away like he's choosing a ripe peach!"
    menu:
        "Don't intervene":
            "Sure, my first instinct is to clamber off the machine I'm on and rush over there."
            "But then I shake my head and try to get back to my work-out before I lose the benefit altogether."
            "After all, I'm not some knight in shining armour."
            "And this place is supposed to be more touchy-feely than it was before."
            "Who knows, the guy might be perfectly innocent and unaware of what he just did."
            "But even if he's not, this is the kind of thing that Hanna's going to have to get used to for this thing to work."
            "And so I resign myself to watching the situation unfold as I press on with my workout."
            show hanna annoyed
            "Hanna looks pretty flustered in the immediate aftermath of the guy coping a feel."
            show hanna happy
            "But I see her shake it off, maintaining her professionalism and getting on with the job admirably."
            hide hanna with dissolve
            "Once I'm done with my workout, I head over to the water-cooler to rehydrate."
            show hanna happy at center, zoomAt(1.5, (640, 1040)) with hpunch
            "And it's there that I run into Hanna, still smiling despite the nature of the encounter she's just had."
            hanna.say "Oh..."
            hanna.say "Hey, [hero.name]."
            mike.say "Hey, Hanna."
            mike.say "I saw what just went down by the step-machines."
            show hanna annoyed
            hanna.say "Ugh...I know, right?"
            hanna.say "Can you believe that guy?"
            mike.say "Yeah, yeah - wandering hands are not fun."
            mike.say "But kudos to you for biting down on it and being professional."
            show hanna surprised
            "Hanna pauses, her mouth hanging half open."
            "It's clear that she's surprised by the sentiment I just expressed."
            "Maybe she was expecting me to be more critical of Mister Cop-a-Feel."
            show hanna normal
            "But then she shakes her head, as if reminding herself that she agreed to all of this."
            hanna.say "Ah...yeah..."
            hanna.say "Yeah, of course I was professional!"
            hanna.say "And you know what - he just renewed his membership for the year."
            hanna.say "Left a pretty big tip too!"
            "I give her a wink and a smile, keen to emphasize the positives and downplay the negatives."
            mike.say "What did I tell you, Hanna?"
            mike.say "There's money in the register, customers in the gym, and everyone's happy!"
            "Hanna nods a little too slowly to be in total agreement with the sentiment of my words."
            "But I'm not about to start indulging her misgivings now, not when she's already committed herself."
            show hanna happy
            hanna.say "I guess you're right, [hero.name]."
            hanna.say "That is why I agreed to make the changes in the first place!"
            mike.say "That's the spirit, Hanna."
            mike.say "This place'll be turned around before you know it!"
            $ hanna.love += 2
        "Stop the patron touching Hanna":
            "I don't even pause to turn off the machine that I've been using."
            "Instead, just clambering off of it while it's still going."
            "And then I'm hurrying across the gym floor towards the guy with the wandering hands."
            "Don't get me wrong, I was all for this change to the gym and I still am."
            "But that doesn't mean I'm going to stand back and let anyone get away with that."
            "This is a gym, not a strip-club."
            "And I don't want to see it turn into a brothel either!"
            show scottie casual as gymguy at flip, center, zoomAt(1.5, (340, 1020)), blacker
            show hanna at center, zoomAt(1.5, (940, 1040))
            with fade
            "As soon as I'm within reach, I put my hand on the guy's shoulder and spin him around."
            mike.say "Hey, man - keep your hands to yourself!"
            show scottie as gymguy at center, zoomAt(1.0, (340, 1020)), blacker, startle
            "The guy looks more surprised than anything, his eyes going wide at the sight of me."
            "Gym Guy" "Whoa..."
            "Gym Guy" "Calm down, dude!"
            mike.say "Not until you take your feelers off of her."
            mike.say "You hear me?!?"
            "Gym Guy" "Okay, okay..."
            "Gym Guy" "Geez, I'm sorry."
            "Gym Guy" "I just thought that..."
            "I'm not in the mood to let the guy finish explaining himself."
            "And so I cut him off before he's done."
            mike.say "Well you thought wrong, didn't you."
            hide scottie as gymguy with moveoutleft
            "With that, he turns and hurries away, aware that all eyes are now on him."
            show hanna annoyed at center, zoomAt(1.5, (640, 1040)) with ease
            hanna.say "Erm...thanks, I guess..."
            hanna.say "I'd have told him off myself."
            hanna.say "But he kind of took me by surprise, you know?"
            "I nod silently, not wanting to vent my anger in front of Hanna, let alone the other patrons in the gym."
            "The way I figure it, they've already had a free floor show out of this as a perk of their memberships."
            show hanna sad
            hanna.say "Ah, [hero.name]..."
            hanna.say "I'm not defending that sleaze or anything."
            hanna.say "But isn't that kind of thing going to happen now?"
            hanna.say "Now that I've made the changes you told me I should?"
            mike.say "I said you should sex this place up a little, Hanna."
            mike.say "I never said you should turn it into a place where people can pay to put their hands on you!"
            show hanna annoyed
            hanna.say "I know, I know - but..."
            mike.say "No buts, Hanna."
            show hanna normal
            mike.say "The scolding this guy just got will remind people that this is a gym."
            mike.say "Trust me, it'll be for the best."
            $ hanna.sub += 1
    return

label hanna_sub_event_02:
    "Tonight was supposed to be just a chance for us to kick back and chill on the sofa, nothing more than that."
    "But even so, there's always that sexual tension in the air when it comes to a girl the likes of Hanna."
    "And so I've spent most of the time wondering if she's going to try to make something happen."
    "I'm more than up for it if she does, but I don't want to be the one to make the first move."
    "Sounds dumb, I know."
    "It's just that I'm worried about coming off like one of those guys that thinks with his dick."
    "So by the time it's getting late, going dark outside and the streetlights coming on, nothing's happened."
    "Sure, it's a little disappointing, what with being so close to someone as hot as Hanna the whole time."
    "But I guess that I only have myself to blame for not doing something about it - so lesson learned there!"
    "Hanna sits up, stretching and letting out a yawn."
    show hanna casual surprised with dissolve
    hanna.say "Wow - I didn't realise it had gotten that late!"
    hanna.say "[hero.name], do you mind if I just go use the bathroom?"
    show hanna wink
    hanna.say "You know, freshen up a little?"
    "I shrug and shake my head in response, still thinking that this is going to be a pretty tame night."
    mike.say "Sure, Hanna..."
    mike.say "Whatever you want."
    show hanna at center, zoomAt(1.5, (640, 1040))
    "Hanna hauls herself up from where we've been slumped on the sofa, using me as a means to do so."
    hanna.say "I'll be right back, [hero.name]."
    hanna.say "Please don't go anywhere while I'm gone!"
    hide hanna with moveoutright
    "I make some kind of non-committal sound, as I'm hardly planning on getting off my ass anytime soon."
    "Hanna can't have been gone for more that a couple of minutes when I hear an odd sound coming from the front door."
    "Frowning in confusion, I haul myself up off of the sofa and begin to trundle towards the hallway."
    "[bree.name] and Sasha are both out for the night, probably not due back until the early hours, if at all."
    "And on top of that, it's not like they don't have keys to let themselves in."
    "I'm not expecting anyone calling around either, so I have no idea what the noise could be."
    "So when I turn around the corner and walk into the hall, my eyes go wide at what I see there."
    scene bg house
    show hanna naked
    with fade
    "The source of the noise is Hanna, on her hands and knees as she scratches at the front door."
    "Trust me, this would have been weird enough in its own right."
    "But the fact that she's also naked and holding a dog's leash in her hand pushed the scene over the top!"
    "Upon seeing me, Hanna turns around and regards me with an eager smile on her face."
    "She starts to speak, but her words are muffled by the leash clamped between her teeth."
    hanna.say "[hero.name]!"
    hanna.say "At last, you're here!"
    show hanna annoyed
    hanna.say "Walkies...please?"
    hanna.say "Like I said, I need the bathroom!"
    "For a moment I'm stunned into silence, unable to do anything but stare at her."
    "But then I see the look of anticipation in Hanna's eyes."
    "That and the way she keeps shaking her butt, doing her best to look like she's wagging her tail."
    "And I think, why the hell not?"
    "After all, I was the one that bought her the collar in the first place."
    "Reaching down, I take the leash out of Hanna's mouth and clip it to her collar."
    "She practically beams as I do this, ass shaking even faster than before."
    "With the leash held firmly in my hand, I unlock the front door and take a cautious look outside."
    "All of a sudden, Hanna makes a dash for the open door, just like a dog seeing the chance of escape."
    "Instinctively and without realising the consequences of my actions, I tug back on the leash."
    scene petplay
    show petplay hanna leash
    with fade
    "This means that Hanna is instantly jerked backwards, letting out a yelp of alarm."
    "I feel a surge of guilt at treating her so roughly, vowing to be more gentle in future."
    "But for all that I'm chiding myself, Hanna seems to feel like she's the one that should be punished."
    "She gazes at the floor, refusing to meet my eye, almost whining in what can only be described as shame."
    hanna.say "I'm sorry, [hero.name]."
    hanna.say "Please don't punish me!"
    mike.say "Ah...it...it's okay, Hanna."
    mike.say "Just be sure to heel in future, okay?"
    hanna.say "Yes, [hero.name], of course."
    hanna.say "I'll be a good dog, you'll see - I'll be the best dog ever!"
    "I nod, still more than a little shaken from what just happened."
    "Trying to keep my mind on other things, I return to the task of checking that the coast is clear."
    "And as soon as I'm satisfied that there's no one around, I step out of the door, leading Hanna behind me."
    "A part of me fully expects one of my neighbours to appear out of nowhere the second that we're out on the street."
    "Either that or a cop car to turn the corner and catch us full on in the beams of its headlights."
    "But I start to set a quick pace that Hanna matches, despite being on her bare hands and knees."
    "And pretty soon it becomes obvious that it's too late and too quiet for anything like that to happen."
    "At last I can feel myself begin to relax and actually enjoy the experience for the first time."
    "Hanna is as good as her word, playing the part of an obedient dog to the absolute letter."
    "It's only when I realise that we've been walking for a good ten minutes or more that something dawns on me."
    "And that's the fact that I have no idea where we're actually going!"
    "I've been too wrapped up in watching Hanna's naked body as she hurries along at my side."
    "It's a tough thing to do, but I finally manage to tear my gaze from her swaying breasts and buttocks for a moment."
    "Luckily for me, the entrance to the park is just up ahead, and so I make straight for it."
    "If the streets were quiet, then the park is absolutely deserted."
    show petplay stand hanna leash hannapee
    play sound peeing
    "We make a quick circuit of a route I know pretty well, stopping for Hanna to answer the call of nature against a tree."
    show petplay walk hanna leash -hannapee
    stop sound fadeout 0.5
    "And then I turn to make for home, not wanting to push my luck any further than I have to."
    "But for the first time on the walk, Hanna resists when I pull on the leash."
    mike.say "Hanna..."
    mike.say "Don't make me spank you!"
    "Hanna whines in the most adorable manner and sits up on her haunches before me."
    show petplay hanna hannahappy
    "Her eyes are so huge and pleading that I almost give in and ask her what she wants on the spot."
    "But she beats me to the punch, allowing me to keep my air of authority intact."
    hanna.say "Please, [hero.name] - I want to play!"
    hanna.say "Won't you let me play with your stick?"
    show petplay stand hannatongueout
    "As if she needs to underline the point, Hanna begins to paw at my zipper..."
    menu:
        "Stop her":
            "I glance around nervously, scanning the surrounding area for any signs of life."
            "There's nothing immediately obvious, but I feel like I'm tempting fate if I say yes."
            mike.say "No, bad dog!"
            show petplay stand hannatongueout hannacloseeyes
            mike.say "Now you do as you're told."
            mike.say "Or else I'll make you sleep out in the back yard tonight!"
            "Hanna whines some more, but then lowers her head and nods meekly."
            "I give a tug on the leash, and she obediently walks to heel once more."
            show petplay walk leash
            "We make it back to my place quicker than we did to the park."
            "And as soon as the door is closed behind us, I can breathe a sigh of relief."
            $ hanna.sub += 1
        "Let her continue":
            "I glance around nervously, scanning the surrounding area for any signs of life."
            "There's nothing immediately obvious, and so I think to hell with it."
            "Unzipping my flies, I give Hanna permission to do her worst."
            mike.say "Okay, there you go."
            mike.say "You've been a good dog tonight."
            mike.say "So you deserve a reward!"
            show petplay stand hannabj outside hold
            "Hanna claps her hands together in glee at this, practically bouncing up and down on the spot."
            "And then she reaches into my open flies with one hand, gently pulling out my cock."
            "It's never been less than halfway stiff the whole time that we've been on this strange, late night walk."
            "So it only takes a little bit of her handling it to go the whole way and get really hard."
            "Perhaps sensing this, or maybe that we're out in a public place, Hanna doesn't take her time."
            show petplay stand hannabj inside hold
            show mouth_insert hanna zorder 1 at zoomAt(1, (860, 140))
            "Instead she takes my cock straight into her mouth, dispensing with the foreplay and getting down to business."
            "This means that the job she does is rough and without her usual flair."
            "But under the rather unique circumstances, it works out just fine."
            "Hanna swallows me as far as she can, sloppily working it in and out as she does so."
            "The sound is something quite atrocious, but the sensation is out of this world."
            show petplay stand hannacloseeyes
            "Pretty soon her head is bobbing back and forth at quite some speed."
            "And I can already feel the urge to cum building up inside of me."
            "All the time I keep on looking this way and that, searching the darkness around us."
            "Suddenly I hear something that I'm certain must be another human being approaching."
            show petplay stand hannabj inside cumshot
            show mouth_insert hanna cum
            with hpunch
            "Which is all I need to lose myself inside of Hanna's mouth!"
            show petplay stand hannabj inside hannaopeneyes with hpunch
            "Unprepared for the premature ejaculation, she coughs and gags at it hits the back of her throat."
            with hpunch
            "Whereas I'm too preoccupied with pulling my cock out of her mouth and stuffing it back into my pants to help her."
            hide mouth_insert
            show petplay stand hannabj outside hannaswallow
            "But almost as soon as the panic begins it's over again."
            "And I realise that what I heard must have been an animal or merely the wind in trees above."
            "As soon as she's done choking, Hanna looks up at me and lets out a questioning whine."
            "I smile and give her a pat on the head, which seems to do the trick, as she smiles happily."
            show petplay walk leash -hannabj
            "With a quick a tug on the leash, and she obediently walks to heel once more."
            "We make it back to my place faster than we did to the park."
            "And as soon as the door is closed behind us, I can breathe a sigh of relief."
            $ hanna.love += 2
    $ hanna.flags.walk_outside = True
    return

label hanna_birthday_date_male:
    $ DONE["hanna_birthday_date_male"] = game.days_played
    $ game.active_date.clothes = "date"
    scene bg gym
    "I'm pretty sure that I'm on time as I walk into the lobby of the gym and glance around."
    "A quick glance at my watch tells me that I'm right - this is the exact time we agreed."
    "So where the hell is Hanna?"
    "And why is she keeping me waiting on her own birthday?"
    "I'm still looking here and there for her, checking my phone for messages too."
    "But there's no sign of her and not a single message to explain what's holding her up."
    "Sighing with frustration, I wander a little further into the gym."
    "And that's when I hear what sounds like Hanna's voice."
    "So I hurry towards it, hoping to find her."
    show hanna sport sweat with dissolve
    hanna.say "One, two, three..."
    hanna.say "Just like that."
    hanna.say "Come on, guys and gals - I know you can do it!"
    "There she is."
    "And she's not ready for our date at all."
    "Instead she's in the middle of leading an aerobics class!"
    menu:
        "Be patient":
            "Just then, Hanna looks over and makes eye-contact with me."
            show hanna happy
            "But when I see her flash me a smile, I start to forget why I was angry in the first place."
            show hanna normal
            "Instead I find that I can't take my eyes off her."
            "I mean, who cares about a reservation at a restaurant?"
            "Especially when you can watch your date working up a sweat in spandex!"
            "I must be grinning like a buffoon, because Hanna's beaming at me right now."
            "When it's finally over, she walks over to where I'm standing."
            show hanna sad at center, zoomAt(1.5, (640, 1040))
            hanna.say "Okay, okay..."
            hanna.say "I know I should have been ready to meet you, [hero.name]."
            hanna.say "But someone called in sick and I had to cover the class."
            hanna.say "I'd have called ahead."
            hanna.say "But it was short notice."
            mike.say "Don't worry about it, Hanna."
            mike.say "I'll just call the restaurant and see what I can do."
            mike.say "They might be able to put the reservations back."
            mike.say "And if not...well, we'll just go some place else instead."
            show hanna normal
            $ game.active_date.score += 15
            "Hanna smiles and nods."
            hanna.say "Okay, I'll just go get changed."
            show hanna wink
            hanna.say "I'll be as quick as I can."
            hide hanna with moveoutleft
            "With that, she hurries off and I get out my phone."
            "Sure, things aren't going exactly to plan."
            "But I'm sure we can get them back on track again."
        "Gesticulates to hurry her up":
            "Just then, Hanna looks over and makes eye-contact with me."
            show hanna happy
            "But when I see her flash me a smile, it's like a red rag to a bull."
            "I give her the best frown that I can manage from across the room."
            "And I point at my wrist to show her that her timing's the issue."
            show hanna sad
            "Hanna seems to pick up on my irritation, beginning to look awkward."
            "But that doesn't mean she stops the class for my sake."
            show hanna normal
            "Instead she looks away and keeps right on going."
            show hanna at center, zoomAt(1.5, (640, 1040))
            "When it's finally over, she walks over to where I'm standing."
            show hanna sad
            hanna.say "What's wrong, [hero.name]?"
            hanna.say "You look seriously pissed!"
            mike.say "Of course I'm pissed, Hanna."
            mike.say "We're already late for our reservation!"
            show hanna annoyed
            hanna.say "Urgh..."
            hanna.say "Look, I'm sorry, okay?"
            hanna.say "Someone called in sick and I had to cover the class."
            show hanna sad
            hanna.say "I know I should have called ahead."
            hanna.say "But it was short notice."
            mike.say "Whatever, Hanna - just go get changed."
            mike.say "Maybe I can move them back or something..."
            show hanna annoyed
            $ game.active_date.score -= 10
            "Hanna doesn't look pleased, but she does as I ask anyway."
            hide hanna with moveoutleft
            "But all the same, this date just got off to a real crappy start."
    scene bg gym
    show hanna date
    with fade
    "With Hanna showered, changed and looking ready for our date, it's time to leave the gym."
    scene bg street
    show hanna date at center, zoomAt(1.5, (640, 1040))
    with fade
    "And luckily for us it isn't far from there to the nightclub where I've made the reservations."
    "But one thing I wasn't expecting was for there to be such a big queue so early."
    "Hanna takes one look at it and let's out an irritated huff."
    show hanna annoyed
    hanna.say "Urgh..."
    hanna.say "I hurried up to leave work just to stand in line?"
    hanna.say "I gotta say, [hero.name]..."
    hanna.say "This isn't how I imagined spending my birthday!"
    "I try not to let Hanna's negativity get under my skin."
    "And instead make a point of smiling and shaking my head."
    mike.say "We're not going to be joining the queue, Hanna."
    mike.say "I made reservations, remember?"
    show hanna normal
    "I take hold of Hanna's hand and begin to make my way to the front of the queue."
    "This earns me a good few hard stares and muttered comments from the people we pass."
    "But I do the best I can to ignore them as I get the attention of the bouncers on the door."
    if hero.equipment["clothes"] and hero.equipment["clothes"].name == "fancy_clothes":
        "Bouncer" "Can I help you, sir?"
        mike.say "Yeah..."
        mike.say "We have reservations."
        mike.say "And that means we can skip the queue."
        mike.say "They'll be under the name [hero.family_name]."
        "The bouncer takes a moment to look at the guest list."
        "But then, much to my dismay, he shakes his head."
        "Bouncer" "Nah..."
        "Bouncer" "I'm not seeing it down here."
        show hanna sad
        "Hanna gives me a pleading look."
        "Like she wants me to handle the problem quickly."
        "So I take a deep breath and put on what I hope is my most charming smile."
        if hero.charm >= 70:
            mike.say "Oh really?"
            mike.say "That sucks for us, man!"
            mike.say "It's my girlfriend's birthday, you know?"
            mike.say "And I was treating her, doing something special."
            "The bouncer glances over to Hanna for a moment."
            show hanna happy
            "And she doesn't miss a beat, giving him a big smile."
            "I can see him checking her out, but that might help us out here."
            mike.say "Ah well, Hanna..."
            mike.say "Looks like we're going to the back of the queue!"
            "I turn to leave, but the bouncer raises a hand to stop me."
            show hanna normal
            "Bouncer" "Wait a minute, buddy."
            "Bouncer" "There's no need to ruin the lady's special night."
            "Bouncer" "Someone must have screwed up the list."
            "Bouncer" "So I'm gonna let you go straight in."
            "And just like that, we're walking into the club."
            show hanna blush
            $ game.active_date.score += 15
            hanna.say "Wow, [hero.name]..."
            hanna.say "That was pretty smooth!"
        else:
            mike.say "Look, man..."
            mike.say "I know I made the reservations."
            mike.say "So maybe you want to go get your boss or something?"
            mike.say "Or someone else that can actually make a real decision?"
            "As soon as the words are out of my mouth, the bouncer's whole demeanour changes."
            "Where before he was disinterested, now he looks seriously pissed."
            "Bouncer" "Okay, buddy..."
            "Bouncer" "I was trying to be nice."
            "Bouncer" "But that's it."
            "Bouncer" "Your name's not on the list."
            "Bouncer" "So you wait in line with everyone else."
            "Hanna and I are treated to the ignominy of walking back to the end of the line."
            "With the eyes of everyone we pushed past on us as we do so too."
            show hanna angry
            $ game.active_date.score -= 10
            hanna.say "Nice work, [hero.name]."
            hanna.say "You really showed that guy."
    else:
        "Bouncer" "Can I help you?"
        mike.say "I hope so, man..."
        mike.say "I made a reservation for the two of us."
        mike.say "So that should mean we get to skip the queue, right?"
        "Bouncer" "That's the way it works, sir."
        "Bouncer" "What name would it be under?"
        mike.say "It'd be [hero.family_name]."
        "The bouncer nods and begins to check the list for us."
        "But after a couple of uncomfortable seconds, he shakes his head."
        "Bouncer" "Hate to tell you this..."
        "Bouncer" "But that name's not on my list."
        show hanna sad
        "Hanna gives me a pleading look, obviously wanting me to sort things out."
        "But one look at the bouncer tells me he's not suddenly going to find my name on that list."
        "So I'm going to have to come up with a solution myself, and quickly too!"
        menu:
            "Bribe the bouncer" if hero.money >= 50:
                "Trying to keep it from being seen, I pull a bill out of my pocket."
                "And then I place it in the bouncer's hand without looking him in the eye."
                "I give it another couple of seconds, and then I take another look."
                "And I'm pleased to see that the bill has managed to disappear."
                mike.say "Ah..."
                mike.say "How's that list looking now?"
                mike.say "You know, sometimes I find things the second time I check!"
                "The bouncer makes a point of looking down at the list again."
                "But at the same time I can see the corner of his mouth curling into a grin."
                "And then he nods, letting out a little chuckle."
                "Bouncer" "You know what, sir..."
                "Bouncer" "Looks like you're right."
                $ hero.money -= 50
                show hanna normal
                "Bouncer" "Your name was here all along."
                "Bouncer" "I must have missed it the first time."
                "Bouncer" "So you can go straight in."
                "And just like that, we're walking into the club."
                show hanna blush
                $ game.active_date.score += 15
                hanna.say "Wow, [hero.name]..."
                hanna.say "That was pretty smooth!"
            "Argue with the bouncer":
                "I do the best I can to look serious, maybe even a little intimidating."
                "And then I speak up in a different tone of voice, trying to sound like I mean business."
                mike.say "Okay..."
                mike.say "Now you listen to me, and you listen good."
                mike.say "I know for a fact that I made those reservations."
                mike.say "So you'd better let us in, right now."
                mike.say "Or else go get your boss and let me tell him how useless you really are!"
                "Personally, I thought I did a pretty good job right there."
                "But my words don't have the desired effect on the bouncer."
                "Instead his expression changes, like a shutter going down and locking in place."
                "Bouncer" "Oh, yeah?"
                "Bouncer" "Well I think this conversation is over."
                "Bouncer" "And you can go wait in the queue, like everyone else."
                "Hanna and I are treated to the ignominy of walking back to the end of the line."
                "With the eyes of everyone we pushed past on us as we do so too."
                show hanna angry
                $ game.active_date.score -= 10
                hanna.say "Nice work, [hero.name]."
                hanna.say "You really showed that guy."
    scene bg nightclub
    show hanna date at center, zoomAt(1.5, (640, 1040))
    with fade
    "Once we're inside the club, Hanna's mood seems to pick up almost instantly."
    "She's smiling and looking around as she checks the place out."
    hanna.say "Good call, [hero.name]!"
    hanna.say "This place has a great feel about it."
    mike.say "If you like this, Hanna..."
    mike.say "Just wait until you see the VIP booth we've got for the night!"
    "Hanna looks more than a little intrigued as I lead her over towards the VIP area."
    "And her face practically lights up when she actually sees it for the first time."
    scene bg vip
    show hanna date surprised blush at center, zoomAt(1.5, (640, 1040))
    with fade
    hanna.say "WOW!"
    show hanna happy -blush
    hanna.say "We can see the whole club from up here!"
    hanna.say "And everyone can see me too!"
    show hanna normal
    hanna.say "US...I mean everyone can see us..."
    "I nod and smile as I sit down beside Hanna."
    "But I'm taken by surprise a moment later when a waitress pops up out of nowhere."
    "Waitress" "Hello, sir..."
    "Waitress" "Hello, madam..."
    "Waitress" "Can I get you something to drink?"
    "Hanna looks more than a little impressed at this."
    hanna.say "Wait..."
    show hanna happy
    hanna.say "We get table service too?!?"
    mike.say "Yeah, Hanna - only the best for you."
    mike.say "What shall we have?"
    "We order a couple of drinks and get down to chatting."
    "But before I know it, Hanna seems to have polished hers off."
    show hanna sad
    hanna.say "Hey..."
    hanna.say "Where'd the waitress go?"
    show hanna normal
    hanna.say "I need another one of these!"
    menu:
        "Order another round":
            "I take a look at my own drink."
            "And then I shrug my shoulders."
            mike.say "Why the hell not?"
            mike.say "Hey, waitress!"
            mike.say "Can we get two more of the same over here?"
            show hanna happy
            $ game.active_date.score += 15
            "Hanna smiles as the waitress brings over our order for the second time."
            hanna.say "You know, I thought you were going to tell me off just now."
            show hanna normal
            hanna.say "I mean, you haven't even finished off your first drink!"
            "I shrug again, the drain the last of that first drink in one go."
            mike.say "Aah!"
            mike.say "That really hits the spot."
            mike.say "Nah, no time to be a prude about it, Hanna."
            mike.say "We're celebrating."
            mike.say "So let's live a little."
        "Slow down Hanna":
            mike.say "Whoa..."
            mike.say "Slow down a little, Hanna!"
            mike.say "We've got all night, you know?"
            show hanna annoyed
            "Hanna frowns and narrows her eyes at me."
            hanna.say "What are you talking about?"
            hanna.say "It's my birthday."
            show hanna sad
            hanna.say "Aren't we supposed to be celebrating?"
            mike.say "I know that."
            mike.say "But it's not a race to see who can get paralytic the quickest!"
            $ game.active_date.score -= 10
            show hanna annoyed
            "Hanna crosses her arms over her chest."
            "And then she flops back into her seat."
            hanna.say "Huh..."
            hanna.say "It's not to see who's the most boring either."
            show hanna angry
            hanna.say "Because we already know who that is!"
    scene bg vip
    show hanna date at center, zoomAt(1.5, (640, 1040))
    with fade
    "I'm really starting to relax and settle into the atmosphere of the club."
    "The drink is probably helping me out, and being able to stare at Hanna too!"
    "She looks so damn sexy tonight."
    "Part of me can't believe that she's actually my date!"
    show hanna flirt
    hanna.say "Hey, [hero.name]..."
    hanna.say "Enough sitting on your ass already!"
    show hanna normal
    hanna.say "Let's go dance..."
    "Before I can even think of protesting, Hanna pulls me to my feet."
    "And then she leads me onto the dance-floor without pausing for a second."
    scene bg nightclub
    show dance hanna date
    with fade
    if randint(0, 1) == 0:
        "As soon as we hit the dance-floor, Hanna goes for it."
        "She's dancing like her life depends on it."
        "And I can see all of the classes she takes at the gym paying off."
        "Seriously, you haven't seen anything until you see one of her dance classes!"
        "And she's bringing all of those moves out on the dance-floor tonight."
        "I've been to a couple of those classes myself."
        "So I figure that the best thing to do would be to go in that direction too."
        "Now, if I can only remember the moves she taught me..."
        if hero.has_skill("dance"):
            "All of those lessons come flooding back to me as I start to dance."
            "And the natural instinct to move with style and grace helps me along too."
            "Before she knows what's happening, Hanna's almost being left behind!"
            "I can see from the surprise on her face that she had no idea I had moves like these."
            "But now all that she can do is keep right on dancing."
            "Well, that and try in vain to keep up with me!"
            $ game.active_date.score += 15
            "Soon Hanna starts to copy my moves, rather than pulling off her own."
            "Then I notice that other people are doing the same thing too!"
            "This is crazy - the dance-floor looks like a scene from a dance show!"
        else:
            "I must not have been paying attention during those particular classes."
            "Either that or I just naturally have two left feet."
            "Because no matter what I do, it seems to end in utter disaster."
            "More than once I blunder into Hanna on the dance-floor."
            "Or else I end up stepping on her feet and making her cry out in pain."
            $ game.active_date.score -= 10
            "In the end she makes me back up a safe distance from her."
            "And from that point on she makes sure that I keep to it too."
    else:
        "Hanna's really pushing herself on the dance-floor tonight."
        "I almost can't believe that she put in a full day's work at the gym before this."
        "And there doesn't seem to be any sign of her slowing down at all."
        "Where all this energy is coming from I have no idea!"
        "The only thing that I can do is try my best to keep up."
        "I mean, I'm no physical wreck."
        "But then again, I'm only human."
        "Hanna looks like a total machine right now!"
        if hero.fitness >= 80:
            "But it's not like I've been going to the gym just to use the sauna!"
            "Thanks to my time spent at Hanna's place of work, I'm fit as a fiddle."
            "And I'm more than ready for the challenge that she's set for me."
            "That means I can pretty much match Hanna move for move."
            "A fact that seems to take her a little by surprise."
            "I guess she's used to being the one setting the pace in her classes."
            "But this isn't the gym and she isn't taking a class."
            "So I don't feel bad about keeping up with her."
            "And maybe even pushing her to new heights too!"
            "In the end, it's Hanna that seems to start flagging first."
            "Because she's the one that pulls me off the dance-floor."
            hide dance
            show hanna date normal blush at center, zoomAt(1.5, (640, 1040))
            with fade
            mike.say "What's the matter, Hanna?"
            mike.say "I thought we were just getting warmed up?"
            show hanna surprised
            hanna.say "What?!?"
            hanna.say "You have got to be kidding!"
            show hanna wink
            $ game.active_date.score += 15
            hanna.say "If we keep this up, you're going to kill me!"
        else:
            "I do the best I can to breathe and keep my heart pumping."
            "But there's no way that I can keep up the pace Hanna's setting."
            "Soon enough I begin to flag and fall behind her."
            "The next thing I know I'm panting for breath."
            "Even worse, I swear I'm seeing spots in front of my eyes too!"
            hide dance with fade
            "Eventually I have to wave in surrender and stagger off the dance-floor."
            "It takes a while, but finally Hanna comes back to the booth to check on me."
            show hanna date sad at center, zoomAt(1.5, (640, 1040))
            hanna.say "You okay, [hero.name]?"
            hanna.say "I was worried about you back there!"
            mike.say "I'll be fine, Hanna."
            mike.say "Just needed to take a little break, that's all."
            show hanna normal
            hanna.say "That's okay."
            $ game.active_date.score -= 10
            hanna.say "I had lots of guys out there looking after me."
            mike.say "Oh...great."
            mike.say "I guess..."
    scene bg nightclub
    show hanna date at center, zoomAt(1.5, (640, 1040))
    with fade
    "Hanna finally seems to be ready to leave the dance-floor after totally owning it."
    "So she strides back to our booth like a queen surveying her realm before sitting down."
    scene bg vip
    show hanna date at center, zoomAt(1.5, (640, 1040))
    with fade
    "But as soon as we get there, I notice a drink waiting for us on the table."
    mike.say "Huh..."
    mike.say "I don't remember ordering that!"
    mike.say "How about you, Hanna?"
    show hanna surprised
    hanna.say "Uh-uh."
    show hanna normal
    hanna.say "Looks pretty impressive though!"
    "I've got to admit that Hanna's right."
    "It does look pretty impressive."
    "And it looks expensive too!"
    "As the waitress passes, I call her over."
    mike.say "Excuse me..."
    mike.say "But we didn't order this drink."
    "She smiles and shakes her head."
    "Waitress" "Oh no, sir..."
    "Waitress" "The gentlemen in the booth over there did."
    "Waitress" "They sent it over for your companion here."
    show hanna surprised
    "Hanna's eyebrows shoot up at this news."
    "And she strains to see who the waitress is pointing at."
    "Which is exactly what I'm doing too."
    "And I'm less than pleased to see that it's a bunch of guys."
    "As soon as they see we're looking in their direction, they're all smiles."
    "Waving and winking in Hanna's direction."
    "That's not good."
    "And it looks like I'm going to have to do something about it."
    menu:
        "Let Hanna keep the drink":
            show hanna normal
            "I take hold of the drink and hand it to Hanna."
            "And then I make sure to get the attention of the guy in the other booth."
            "I'm all smiles and pleasant waves, which only seems to amuse them more."
            "But then I make a point of wrapping my arms around Hanna."
            hide hanna
            show hanna kiss date
            $ hanna.flags.kiss += 1
            "And I kiss her full on the lips."
            "She's a little surprised at first."
            "But then she leans into the kiss too."
            "It's long and intense, with both of us enjoying every moment."
            hide hanna
            show hanna date at center, zoomAt(1.5, (640, 1040))
            "And once it's over, I shoot the guys in the other booth another smile."
            "But this time it's one of knowing triumph."
            "And true to form, they hunch down over their glasses."
            "All of a sudden not seeming to be so amused."
            mike.say "How's the drink, Hanna?"
            hanna.say "Erm..."
            hanna.say "Pretty good, [hero.name]."
            show hanna sad
            hanna.say "Are..."
            hanna.say "Are you really okay with them doing that?"
            show hanna normal
            mike.say "Of course, Hanna."
            mike.say "You can't blame them for having good taste!"
            show hanna surprised blush
            $ game.active_date.score += 15
            "Hanna's eyes go wide, and then she blushes at the compliment."
        "Tell the waitress to take the drink back":
            "I shove the drink towards the waitress."
            mike.say "Do me a favour and get rid of this."
            mike.say "And don't bring any more drinks over either."
            "The waitress looks a little uncomfortable."
            "But she nods and does as she's told all the same."
            "And I turn to face Hanna, deliberately showing my back to the other booth."
            show hanna angry
            $ game.active_date.score -= 10
            hanna.say "Why did you have to go and do a thing like that?"
            hanna.say "It was just one drink, [hero.name]."
            hanna.say "Those guys were just trying to be nice!"
            mike.say "They were trying to flirt with you, Hanna."
            mike.say "Right under my damn nose!"
            mike.say "Right in the middle of our date!"
            show hanna annoyed
            "Hanna looks away, like she's ready to let the matter drop."
            "Sure, it's not the most pleasant way to handle the problem."
            "But at least it lets Hanna know how I feel in no uncertain terms."
    show hanna normal
    hanna.say "[hero.name]..."
    mike.say "Yes, Hanna?"
    hanna.say "Today is my birthday, right?"
    mike.say "That was my understanding."
    show hanna wink
    hanna.say "So what happens on someone's birthday?"
    if not hero.has_gifts:
        "Ah shit!"
        "Hanna's fishing for a birthday present."
        "And I didn't bother to get her one!"
        "Maybe I can wriggle out of this one somehow..."
        show hanna normal
        mike.say "Well, Hanna..."
        mike.say "If they're lucky, someone takes them out on a really nice date!"
        "Hanna looks at me in silence for a moment."
        $ game.active_date.score -= 20
        show hanna sad
        "And then I see her face fall as she realises she's not getting a gift."
        hanna.say "Ah...yeah..."
        hanna.say "I guess I'm one lucky girl!"
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_8
        if _return != "done":
            if _return not in ["None", "exit"]:
                "I've been waiting for the right moment to whip this thing out."
                "But it looks like Hanna just created it for me."
                mike.say "Okay, Hanna - I get the hint."
                mike.say "Happy birthday!"
                show hanna happy
                "Hanna's face lights up as I hand over the gift."
                play sound [paper_ripping_2, paper_ripping_1]
                "And she doesn't hesitate to tear it open."
                if _return:
                    show hanna surprised blush
                    hanna.say "Oh..."
                    hanna.say "Oh wow..."
                    "Hanna holds up her gift, staring at it in amazement."
                    mike.say "What's the matter, Hanna?"
                    mike.say "Is it okay?"
                    show hanna happy
                    hanna.say "It's better than okay."
                    $ game.active_date.score += 20
                    hanna.say "This is awesome!"
                    show hanna normal
                    hanna.say "Thank you so much!"
                    "I nod and smile, feeling glad to have made the right choice."
                    "And seeing how happy Hanna looks right now makes it worth the effort."
                else:
                    show hanna sad
                    hanna.say "Oh..."
                    $ game.active_date.score -= 10
                    hanna.say "Thanks, I guess..."
                    "Hanna's looking at her gift with what can only be described as disappointment."
                    mike.say "Is there something wrong, Hanna?"
                    hanna.say "What?"
                    show hanna normal
                    hanna.say "Oh no, nothing's wrong."
                    "We exchange awkward smiles as Hanna puts the gift away."
                    "And I make a mental note to try harder next time."
            else:
                "Ah shit!"
                "Hanna's fishing for a birthday present."
                "And I didn't bother to get her one!"
                "Maybe I can wriggle out of this one somehow..."
                show hanna normal
                mike.say "Well, Hanna..."
                mike.say "If they're lucky, someone takes them out on a really nice date!"
                "Hanna looks at me in silence for a moment."
                $ game.active_date.score -= 20
                show hanna sad
                "And then I see her face fall as she realises she's not getting a gift."
                hanna.say "Ah...yeah..."
                hanna.say "I guess I'm one lucky girl!"
    show hanna normal
    "I take a look at the time, and I'm about to say that it's getting late."
    "But then I remember we're in a nightclub, and it's starting to get early!"
    mike.say "Have you seen the time, Hanna?"
    mike.say "They're going to be kicking us out of this place soon!"
    show hanna surprised
    hanna.say "Oh wow!"
    hanna.say "I totally lost track of it!"
    show hanna normal
    mike.say "Erm..."
    mike.say "So...you want to go home?"
    mike.say "Or do you still have some energy left?"
    if game.active_date.score >= 80 and hanna.sexperience >= 1:
        "Hanna nods her head eagerly."
        show hanna wink
        hanna.say "I've still got a little left."
        hanna.say "How about you?"
        mike.say "I could stretch it out a little longer."
        mike.say "But where are we going to go at this hour of the night?"
        show hanna normal
        "Hanna thinks for a moment."
        "And then she nods with a smile."
        hanna.say "Don't worry, [hero.name]..."
        show hanna flirt
        hanna.say "I know somewhere we can go."
        hanna.say "Come with me and I'll show you."
        call hanna_birthday_sex from _call_hanna_birthday_sex
    else:
        "Hanna answers this question with a pretty impressive yawn."
        "Though part of me is tempted to think that it's put on."
        show hanna sad
        hanna.say "Nah..."
        hanna.say "I'm totally tired out!"
        hanna.say "If I don't get some sleep, I'll be like a zombie at work tomorrow!"
        show hanna normal
        mike.say "Okay, Hanna..."
        mike.say "Let's see if we can get a taxi."
        "I could probably have stretched it out a little longer."
        "But I guess it's better to cut my losses and call it a night."
    return

label hanna_birthday_sex:
    scene bg gym
    show hanna date
    with fade
    "I'm more than a little surprised when Hanna drags me all the way back to the gym."
    "So much so that I don't manage to speak up until she's unlocked the door and pulled me inside."
    "As she locks the doors behind us, I finally put my confusion into words."
    mike.say "You're serious, Hanna?"
    mike.say "You want to fool around here?"
    mike.say "Where you work?!?"
    show hanna close flirt
    "Hanna turns to face me, already nodding eagerly."
    hanna.say "Why the hell not, [hero.name]?"
    hanna.say "It's close and I have the keys."
    hanna.say "Plus there's nobody here until the morning."
    hanna.say "Sounds perfect to me."
    mike.say "But what about the cameras?"
    mike.say "I know you have CCTV here."
    show hanna normal
    hanna.say "Yeah, we do."
    hanna.say "But who do you think looks at the footage, huh?"
    show hanna blush
    hanna.say "Nobody but me."
    mike.say "And you'll erase it, right?"
    hanna.say "Don't worry about a thing, [hero.name]."
    hanna.say "I'll handle it."
    "I nod at this, assuming that means what I think it means."
    "And I try to reassure myself that I'm just being overly cautious."
    "Hanna probably chose to bring me here for convenience alone."
    "And she'll want to get down to it somewhere like her office."
    "Which might not even have a CCTV camera in it."
    hanna.say "Come on, [hero.name]..."
    hanna.say "What are we waiting for?"
    "Hanna grabs hold of my hand and pulls me after her again."
    "But I notice that she's making straight for the main part of the gym."
    "The very same part where all of the daily classes are held!"
    mike.say "H...Hanna..."
    mike.say "We can't do it here!"
    show hanna -close
    "Hanna just laughs and pulls me down onto one of the yoga mats on the floor."
    show hanna topless
    "And she pretty much underlines her intentions by pulling off her top a second later."
    "I have to admit that this stops me in my tracks, silencing my objections."
    "What can I say?"
    "I'm only human after all!"
    "In fact, I hardly notice that I've started getting undressed too."
    "Hanna seems to spot this before I do, and nods to encourage me."
    show hanna normal
    hanna.say "I'm in here every day, you know?"
    hanna.say "All the walls are covered in mirrors."
    hanna.say "So I can see every movement I make from every possible angle."
    show hanna flirt
    hanna.say "And I always wondered what watching myself have sex would be like!"
    "Hanna's straddling my thighs as she tells me all of this."
    show hanna naked -topless
    "And at the same time she's stripping off the last of her clothes."
    "Any resistance left in me drains away as I stare up at the sight."
    "All I can do is nod and let Hanna have her way."
    "Because the view from down here is pretty amazing."
    "Even without a three hundred and sixty degree reflection!"
    "Hanna seems to notice the effect she's having on me right now."
    "She looks down with a smile on her face."
    "And she shakes her breasts from side to side for good measure."
    hanna.say "Like what you see, huh?"
    hanna.say "Hmm..."
    hanna.say "That was kind of a trick question."
    hanna.say "Because I already know that you do."
    show hanna close
    "I gasp in surprise as Hanna suddenly grabs hold of my cock."
    hanna.say "Your little friend down here gave you away!"
    "I nod even more as I feel Hanna start to stroke the shaft."
    show hanna cowgirl gym with fade
    "At the same time she starts to lower herself onto me."
    "There's nothing that I need to do, other than lie back."
    "Hanna seems to have everything literally in hand."
    "I can feel the soft sensation of her pussy against my cock."
    "It's warm, and getting wetter by the second."
    "Hanna knows just how long to tease me with the feel of her lips."
    show hanna cowgirl wet
    "And at the precise moment the time is right, she pushes my cock against them."
    "They part slowly, only a little at a time."
    "This means that I sink into her at the same pace."
    "And each time I do, the feeling is an intense burst of physical pleasure."
    show hanna cowgirl pleasure down
    "As soon as I'm all the way inside of her, Hanna changes gear."
    "Her hands free, she places them on my shoulders."
    "And then she raises her eyes, looking straight ahead."
    "Without needing to be told, I reach up and put my hands on her."
    "I have a good hold of her waist, gripping her tight."
    "That done, I wait a moment to see what she does next."
    show hanna cowgirl smile up
    "Hanna gives a little nod, and then she starts moving."
    "The very next second, I begin to move too."
    show hanna cowgirl up speed
    pause .5
    show hanna cowgirl down at center, vshake
    pause .1
    show hanna cowgirl bounce
    pause .3
    show hanna cowgirl -bounce at center, startle(0.1,-10)
    "When she goes down, I go up and we meet in the middle."
    "Then we reverse the action, beginning to pick up speed."
    show hanna cowgirl up speed
    pause .5
    show hanna cowgirl down at center, vshake
    pause .1
    show hanna cowgirl bounce
    pause .3
    show hanna cowgirl -bounce at center, startle(0.1,-10)
    pause .25
    show hanna cowgirl up
    pause .5
    show hanna cowgirl down at center, vshake
    pause .1
    show hanna cowgirl bounce
    pause .3
    show hanna cowgirl -bounce at center, startle(0.1,-10)
    pause .25
    show hanna cowgirl up
    pause .5
    show hanna cowgirl down at center, vshake
    pause .1
    show hanna cowgirl bounce
    pause .3
    show hanna cowgirl -bounce at center, startle(0.1,-10)
    "To me it feels like we're moving in perfect harmony, following each other."
    "But I can't shake the feeling of familiarity about what we're doing too."
    "The way that it feels more than a little like one of Hanna's gym classes."
    "I've seen her body move like this many times before."
    "Only then it was covered with spandex."
    "And, of course, I wasn't inside of her all those times!"
    "Not that I find the sensation unpleasant."
    "I feel like all of those classes were preparing Hanna for this."
    "And now her body is moving like a well-conditioned machine."
    "The whole purpose of which is to give me intense and unforgettable pleasure."
    show hanna cowgirl up pleasure
    pause .5
    show hanna cowgirl down at center, vshake
    pause .1
    show hanna cowgirl bounce
    pause .3
    show hanna cowgirl -bounce at center, startle(0.1,-10)
    hanna.say "Uh..."
    hanna.say "Harder..."
    show hanna cowgirl up
    pause .5
    show hanna cowgirl down at center, vshake
    pause .1
    show hanna cowgirl bounce
    pause .3
    show hanna cowgirl -bounce at center, startle(0.1,-10)
    hanna.say "Faster..."
    show hanna cowgirl up
    pause .5
    show hanna cowgirl down at center, vshake
    pause .1
    show hanna cowgirl bounce
    pause .3
    show hanna cowgirl -bounce at center, startle(0.1,-10)
    hanna.say "Come on...give me...more!"
    "I guess Hanna's as demanding during sex as she is as an instructor at the gym!"
    "Luckily for me, the time I've spent here working out has made me equal to the task."
    "I step up to the challenge, moving faster and harder than ever."
    show hanna cowgirl up sweat
    pause .4
    show hanna cowgirl down at center, vshake
    pause .1
    show hanna cowgirl bounce
    pause .25
    show hanna cowgirl -bounce at center, startle(0.1,-10)
    pause .25
    show hanna cowgirl up
    pause .4
    show hanna cowgirl down at center, vshake
    pause .1
    show hanna cowgirl bounce
    pause .25
    show hanna cowgirl -bounce at center, startle(0.1,-10)
    pause .25
    show hanna cowgirl up
    pause .4
    show hanna cowgirl down at center, vshake
    pause .1
    show hanna cowgirl bounce
    pause .25
    show hanna cowgirl -bounce at center, startle(0.1,-10)
    "But no matter what I do, it seems like Hanna just eats it up."
    "I can feel sweat starting to bead on my forehead."
    "And I know that my muscles aren't going to hold up to much more of this."
    "But just as I think that Hanna's going to wear me out, something changes."
    "Her body twitches, then she twists atop me."
    "Finally the illusion of her being able to take it all begins to crack."
    hanna.say "Oh fuck..."
    show hanna cowgirl up
    pause .3
    show hanna cowgirl down at center, vshake
    pause .1
    show hanna cowgirl bounce
    pause .2
    show hanna cowgirl -bounce at center, startle(0.1,-10)
    hanna.say "I...I'm gonna cum!"
    "Hanna's words act like some kind of crazy release valve for me."
    "Almost before she's done speaking, I can feel myself starting to lose it."
    show hanna cowgirl up speed ahegao
    pause .3
    show hanna cowgirl down at center, vshake
    pause .1
    show hanna cowgirl bounce
    pause .2
    show hanna cowgirl -bounce at center, startle(0.1,-10)
    pause .25
    show hanna cowgirl up
    pause .3
    show hanna cowgirl down at center, vshake
    pause .1
    show hanna cowgirl bounce
    pause .2
    show hanna cowgirl -bounce at center, startle(0.1,-10)
    pause .25
    show hanna cowgirl up
    pause .3
    show hanna cowgirl down at center, vshake
    pause .1
    show hanna cowgirl bounce
    pause .2
    show hanna cowgirl cum -speed -bounce at center, startle(0.1,-10)
    $ hanna.sexperience += 1
    "And as soon as I shoot my load into her, she loses control as well."
    with vpunch
    "Hanna forces herself downwards, grinding against me as she cums."
    with vpunch
    "I'm holding onto her so tightly that I expect to see bruises when I let her go."
    "But neither of us is going to stop until the very end."
    show hanna cowgirl up smile
    "And when that comes, Hanna collapses atop me."
    "Her head lands on my chest as she pants for breath."
    "But all I can do is hold onto her until one of us recovers."
    "And that's something we can afford to take our time over."
    "The gym's deserted and it's hours until dawn."
    "So there's nothing at all to disturb us until then."
    $ hero.cancel_activity()
    return

label hanna_male_ending:

    if renpy.has_label("hanna_achievement_3") and not game.flags.cheat:
        call hanna_achievement_3 from _call_hanna_achievement_3
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding with fade
    "I guess that I should have known our big day would turn out like this back when I popped the question."
    "Don't take that to mean I'm not down with the whole way that Hanna and I are getting married."
    "It's just that I sat through all of the planning kind of in a daze and nodding my head to most of it."
    "I mean, can you blame me?"
    "Organising a wedding is a massive headache that feels like it takes literally forever."
    "Hanna was more than willing to handle it all down to the smallest detail."
    "And there was like a thousand of those too!"
    "So yeah, I took the easy way out and just watched my future wife deal with it all."
    "Partly because I'm a lazy asshole and partly to see her in action."
    "Because Hanna looks amazing when she's whipped up into a frenzy like that!"
    "I just can't help shaking my head at all the stuff she's managed to pull off."
    "The whole chapel is decked out according to her exacting plan."
    "The guests have been given strict instructions on the dress-code."
    "And I swear that there's even a scent in the air that Hanna's chosen."
    "I take a quick glance down at myself, realising something for the first time."
    "I've been totally styled by Hanna too."
    "Which means I'm a part of this whole scheme as well!"
    "I shake my head, grinning to myself at the thought of it all."
    "Don't get me wrong, I'm not in the least bit upset or annoyed."
    "In fact I actually love the fact that all of this is part of Hanna's plan."
    "And when the music begins to play, I can see it all coming together."
    "Look, I know that Hanna's a bit of an exhibitionist."
    "But it's one of the things that makes her unique and special."
    "So as she sweeps into the chapel and up the aisle, I'm still smiling."
    "All eyes are on Hanna, and that's exactly how it should be."
    show hanna wedding normal at center, zoomAt (1.0, (640, 730)) with dissolve
    "This is her wedding day, when the bride is the star of the show."
    "And I could stare at Hanna no matter what she was wearing!"
    "But I have to say that she's never looked better than she does right now."
    "Hanna's dress is just perfect."
    "And why wouldn't it be?"
    "After all, it was made for her."
    if hanna.is_visibly_pregnant:
        "Even though it's been made to accommodate her belly, it's still perfect."
        "And it's not like I even care that everyone here can see she's pregnant."
        "All that means is our family is starting to grow, literally inside of her."
        "What better proof could there be of how much we love each other?"
    else:
        "It's at times like this when Hanna's obsession with working out really pays off."
        "And that dress accentuates every muscle and exquisite curve of Hanna's body."
        "I honestly don't think she's ever looked better than this in lycra and spandex."
        "Maybe she's only ever looked better naked!"
    show hanna at center, traveling (1.5, 5.0, (640, 1040))
    "I can't take my eyes off of Hanna as she reaches the altar."
    "And I can see from the look on her face that she knows it too."
    "Hanna's beaming at being the centre of attention."
    "And I couldn't be happier that she is."
    "As Hanna comes to stand by my side, I lean in to whisper to her."
    mike.say "You look amazing!"
    hanna.say "Thanks..."
    show hanna happy
    hanna.say "I try my best!"
    "Priest" "Ahem..."
    show wedding hanna with fade
    "At the sound of the priest's voice, Hanna and I snap to attention."
    "This is greeted with an indulgent smile in return."
    show wedding hanna priest with fade
    "And then the wedding proper begins."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join these two people in the bonds of holy matrimony..."
    "I don't remember much of what follows, most of it blurring together."
    "All that stands out for me are the important parts."
    "You know, the ones that we've rehearsed so many times?"
    "Priest" "Do you, Hanna, take this man [hero.name]..."
    "Priest" "To be your lawful, wedded husband?"
    hanna.say "I do."
    "Priest" "Very good."
    "Priest" "And do you, [hero.name], take this woman Hanna..."
    "Priest" "To be your lawful, wedded wife?"
    mike.say "I do."
    "Priest" "Also good."
    "The priest takes a moment to nod to the pair of us."
    "And then he continues with the next part of the ceremony."
    "Priest" "I call upon all those here present..."
    "Priest" "That if they know of any lawful impediment to these two being married..."
    "Priest" "Speak now, or forever hold your peace!"
    "There's the customary pause as the priest scans the guests."
    "And the equally customary ripple of nervous giggles follows."
    "Priest" "Very well..."
    "Priest" "It gives me great pleasure to pronounce you man and wife."
    "Priest" "You may kiss the bride!"
    show wedding hanna -priest with dissolve
    "Hanna and I don't need to be given permission to do that!"
    "A moment later we're wrapped in each others arms."
    scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
    show hanna kiss wedding
    with fade
    $ hanna.flags.kiss += 1
    "The kiss that follows doesn't hold a thing back."
    "And it doesn't tone things down for the setting either!"
    "I think I've got as much attention on me as Hanna usually gets right now."
    "But none of that seems to matter."
    "Not so long as I know that I'm the centre of Hanna's attention."
    hide hanna


    scene hanna gym ending
    with fade
    hanna.say "Hello?"
    hanna.say "Yeah, I'm talking to you!"
    hanna.say "Just checking that I've got your undivided attention, yeah?"
    hanna.say "Good, because you'd better be listening to what I have to say!"
    hanna.say "After all, I think I deserve to be the centre of attention for once..."
    hanna.say "Anyway, what was I supposed to be talking about again?"
    hanna.say "Oh yeah, [hero.name] and me!"
    hanna.say "The first thing to say is that I never made a habit of it."
    hanna.say "Dating guys that were gym members, that is."
    hanna.say "Sure, you get a lot of hotties in there."
    hanna.say "And yeah, they're all working out in their tight gear!"
    hanna.say "But you kind of get used to just seeing them as part of the furniture."
    hanna.say "How else could I even think about doing my job every day of the week?"
    hanna.say "That means it kind of takes something more to catch my attention."
    hanna.say "Don't get me wrong, I'm not saying [hero.name] wasn't one of the hotties."
    hanna.say "More like he was a work in progress, you know?"
    hanna.say "But he was smart and funny too."
    hanna.say "Not just another muscle-brained guy that thought he was god's gift to women!"
    hanna.say "So we got started just chatting at the gym."
    hanna.say "The next thing I know he's becoming a friend."
    hanna.say "And then we're dating, like it's the most natural thing in the world!"
    hanna.say "That's when I start to get to know the real [hero.name]."
    hanna.say "And he starts to get to know me too."
    hanna.say "The more I see of him the more I seem to like."
    hanna.say "And he seems to get me too, you know?"
    hanna.say "Like he understands that I'm more than a gym-bunny."
    hanna.say "I'm like that green guy in the film with the talking donkey."
    hanna.say "What I mean by that is I have layers."
    hanna.say "Not many guys are interested in more than the first few of those."
    hanna.say "And yeah, by that I do mean getting my clothes off and seeing me naked!"
    hanna.say "Sure, I like to be admired - what girl doesn't?"
    hanna.say "But there's more to it than that."
    hanna.say "What's the point of having a whole room of guys giving you the eye."
    hanna.say "What does it really mean if you know that none of them actually love you?"
    hanna.say "That's why [hero.name] is different, why he's special."
    hanna.say "And I guess that's why I married him in the end!"



    hanna.say "[hero.name]'s been the best husband that I could have wised for too."
    hanna.say "He's given me all the support I needed to take over running the gym."
    hanna.say "And now the place feels like it's totally mine."
    hanna.say "Like it's as much of a success as our marriage!"






    hanna.say "I love the way that my life is turning out now that we're settled down together."
    hanna.say "And I just know that the future is only going to see things get better."
    if hanna.is_visibly_pregnant:
        hanna.say "And [hero.name] Junior is all the proof that I need to be sure of it."
        hanna.say "The way that [hero.name] stepped up and became a father."
        hanna.say "It told me more about him than I ever thought possible."
        hanna.say "And now we're a happy little family unit!"
    else:
        hanna.say "All of this means that we're in a good place right now."
        hanna.say "And we keep talking about the possibility of starting a family."
        hanna.say "The time might not be right just now."
        hanna.say "But I know that will change sooner or later."
    hanna.say "So all in all, I think I did a pretty good job with [hero.name]."
    hanna.say "I managed to straighten out most of the kinks he had when we met."
    hanna.say "And I actively encouraged some of the ones that I really liked!"
    hanna.say "Now I think he's close to being the perfect man for me."
    hanna.say "One that I'm looking forward to spending a long time with."
    hanna.say "And if he's lucky, I won't trade him in for a younger model along the way!"

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not hanna.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_9
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_9
    $ game.set_new_game_plus()
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
