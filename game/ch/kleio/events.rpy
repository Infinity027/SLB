init python:
    Event(**{
    "name": "kleio_start",
    "label": "kleio_start",
    "priority": 500,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            MinFlag("performance", 2)),
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "kleio_start2",
    "label": "kleio_start",
    "priority": 500,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsFlag("band", 2)),
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "kleio_event_01",
    "label": "kleio_event_01",
    "priority": 500,
    "duration": 4,
    "conditions": [
        Or(
            IsDone("kleio_start"),
            IsDone("kleio_start2"),
            ),
        IsHour(14, 15),
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(kleio,
            Not(IsPresent()),
            Not(IsHidden()),
            MinStat("love", 20),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "kleio_event_02",
    "label": "kleio_event_02",
    "priority": 500,
    "duration": 4,
    "conditions": [
        IsDone("kleio_event_01"),
        IsHour(17, 18),
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(kleio,
            Not(IsPresent()),
            Not(IsHidden()),
            MinStat("love", 40),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "do_once": True,
    })

    WakeUpEvent(**{
    "name": "kleio_event_03",
    "label": "kleio_event_03",
    "priority": 500,
    "conditions": [
        IsDone("kleio_event_02"),
        IsHour(5, 8),
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(kleio,
            Not(IsPresent()),
            Not(IsHidden()),
            MinStat("love", 60),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "kleio_event_04",
    "priority": 500,
    "label": "kleio_event_04",
    "duration": 2,
    "conditions": [
        IsDone("kleio_event_03"),
        IsDayOfWeek("24"),
        IsHour(9, 18),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsRoom("map"),
            ),
        GameTarget(
            Or(
                IsFlag("band", 1),
                IsFlag("band", 2)
            )
        ),
        HasVehicle(motor=True),
        PersonTarget(kleio,
            Not(IsPresent()),
            Not(IsHidden()),
            MinStat("love", 80),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "kleio_event_05",
    "priority": 500,
    "label": "kleio_event_05",
    "conditions": [
        IsDone("kleio_event_04"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsRoom("studio"),
            HasStamina(),
            ),
        PersonTarget(kleio,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 100),
            MaxStat("lesbian", 15),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "kleio_event_05b",
    "priority": 500,
    "label": "kleio_event_05b",
    "duration": 2,
    "conditions": [
        IsDone("kleio_event_05"),
        IsNotDone("kleio_event_05c"),
        IsDayOfWeek("135"),
        IsHour(20, 23),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(kleio,
            Not(IsPresent()),
            Not(IsHidden()),
            IsFlag("niceCar"),
            MinStat("love", 110),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "kleio_event_05c",
    "priority": 500,
    "label": "kleio_event_05c",
    "duration": 2,
    "conditions": [
        IsDone("kleio_event_05"),
        IsNotDone("kleio_event_05b"),
        IsDayOfWeek("135"),
        IsHour(14, 18),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            HasRoomTag("home"),
            ),
        PersonTarget(kleio,
            Not(IsPresent()),
            Not(IsHidden()),
            IsFlag("niceCar", False),
            MinStat("love", 110),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "kleio_event_06",
    "priority": 500,
    "label": "kleio_event_06",
    "conditions": [
        Or(
            IsDone("kleio_event_05b"),
            IsDone("kleio_event_05c"),
            ),
        Not(IsDone("kleio_event_06b")),
        IsHour(12, 18),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            ),
        PersonTarget(kleio,
            Not(IsPresent()),
            Not(IsHidden()),
            MinStat("love", 120),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "kleio_event_06b",
    "priority": 500,
    "label": "kleio_event_06b",
    "conditions": [
        Or(
            IsDone("kleio_event_05b"),
            IsDone("kleio_event_05c"),
            ),
        Not(IsDone("kleio_event_06")),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(kleio,
            IsActive(),
            MinStat("love", 120),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "do_once": True,
    })

    AfterDateEvent(**{
    "name": "kleio_getting_serious_01",
    "label": "kleio_getting_serious_01",
    "priority": 500,
    "conditions": [
        Or(IsDone("kleio_event_06"),IsDone("kleio_event_06b")),
        HeroTarget(IsGender("male")),
        MinDateScore(90),
        PersonTarget(kleio,
            OnDate(),
            MinStat("love", 140),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "kleio_event_07",
    "priority": 500,
    "label": "kleio_event_07",
    "conditions": [
        Or(
            IsDone("kleio_event_06"),
            IsDone("kleio_event_06b"),
            ),
        IsDone("kleio_getting_serious_01"),
        HeroTarget(IsGender("male")),
        PersonTarget(kleio,
            IsActive(),
            MinStat("love", 150),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "do_once": True,
    })

    AfterDateEvent(**{
    "name": "kleio_getting_serious_02",
    "label": "kleio_getting_serious_02",
    "priority": 500,
    "conditions": [
        IsDone("kleio_getting_serious_01"),
        HeroTarget(IsGender("male")),
        MinDateScore(90),
        PersonTarget(kleio,
            OnDate(),
            MinStat("love", 160),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "kleio_event_07_1",
    "priority": 500,
    "label": "kleio_event_07_1",
    "conditions": [
        IsDone("kleio_event_07", "kleio_getting_serious_02"),
        HeroTarget(
            IsGender("male"),
            Or(
                IsRoom("date_park"),
                HasRoomTag("park"),
                ),
            ),
        PersonTarget(kleio,
            IsActive(),
            MinStat("love", 170),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "kleio_event_08",
    "priority": 500,
    "label": "kleio_event_08",
    "conditions": [
        IsDone("kleio_event_07_1"),
        IsHour(19, 22),
        HeroTarget(
            IsGender("male"),
            Or(
                IsRoom("date_pub"),
                HasRoomTag("pub"),
                ),
            ),
        PersonTarget(kleio,
            IsActive(),
            MinStat("love", 180),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "kleio_event_09",
    "priority": 500,
    "label": "kleio_event_09",
    "conditions": [
        IsDone("kleio_event_08"),
        IsHour(10, 22),
        HeroTarget(
            IsGender("male"),
            IsFlag("kleiocall", False)),
        PersonTarget(kleio,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 190),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "kleio_event_10",
    "priority": 500,
    "label": "kleio_event_10",
    "conditions": [
        IsDone("kleio_event_09"),
        IsHour(9, 19),
        HeroTarget(
            IsGender("male"),
            IsFlag("kleiocall", False)),
        PersonTarget(kleio,
            Not(IsPresent()),
            Not(IsHidden()),
            IsFlag("engagedmike", False),
            MinStat("love", 200),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "kleio_event_11",
    "priority": 500,
    "label": "kleio_event_11",
    "conditions": [
        IsDone("kleio_event_10"),
        IsHour(18, 20),
        HeroTarget(
            Not(OnDate()),
            IsRoom("rooftop"),
            ),
        PersonTarget(kleio,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 200),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "kleio_practice_01",
    "priority": 500,
    "label": "kleio_practice_01",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("practice_band"),
            MinFlag("bandpractice", 25),
            ),
        PersonTarget(kleio,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 50),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kleio_say_preg",
    "label": "kleio_say_preg",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsRoom("map"),
            ),
        PersonTarget(kleio,
            IsFlag("toldpreg", False),
            MinCounter("pregnant", 6),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "once_day": True,
    "do_once": False,
    "quit": False,
    })

    Event(**{
    "name": "kleio_kiss_me",
    "label": "kleio_kiss_me",
    "max_girls": 1,
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(kleio,
            IsPresent(),
            Not(IsHidden()),
            MinFlag("kiss", 1),
            MinStat("love", 150),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "chances": 20,
    "once_day": True,
    "do_once": False,
    "quit": False,
    })

    Event(**{
    "name": "kleio_preg_talk",
    "label": "kleio_preg_talk",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(kleio,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("toldpreg", False),
            MinCounter("pregnant", 6),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "once_day": True,
    "do_once": False,
    "quit": False,
    })

    InteractEvent(**{
    "name": "kleio_event_talk_murder",
    "label": "kleio_event_talk_murder",
    "priority": 500,
    "conditions": [
        PersonTarget(kleio,
            IsActive(),
            ),
        PersonTarget(kylie,
            IsFlag("killed", "sasha"),
            ),
        ],
    "clothes": "casual",
    "music": "music/roa_music/horizon.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "kleio_meet_bree",
    "priority": 500,
    "label": "kleio_meet_bree",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasRoomTag("pub"),
            ),
        Or(
            PersonTarget(kleio,
                IsPresent(),
                ),
            PersonTarget(bree,
                IsPresent(),
                ),
        ),
        PersonTarget(kleio,
            HasRoomTag("pub"),
            Not(IsHidden()),
            MinStat("love", 100),
            ),
        PersonTarget(bree,
            HasRoomTag("pub"),
            Not(IsHidden()),
            MinStat("love", 100),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "kleio_twintails_01",
    "priority": 500,
    "label": "kleio_twintails_01",
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            ),
        PersonTarget(kleio,
            IsActive(),
            IsFlag("chosenbree"),
            MinStat("love", 120),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "kleio_twintails_02",
    "priority": 1000,
    "label": "kleio_twintails_02",
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            ),
        PersonTarget(kleio,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("haircut"),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "kleio_call_me_master",
    "priority": 500,
    "label": "kleio_call_me_master",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            ),
        PersonTarget(kleio,
            IsActive(),
            IsFlag("girlfriend"),
            Not(IsFlag("mikeNickname", "master")),
            MinStat("sub", 50),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "kleio_sub_event_1",
    "label": "kleio_sub_event_1",
    "priority": 500,
    "conditions": [
        IsHour(20, 6),
        HeroTarget(
            IsGender("male")),
        PersonTarget(kleio,
            IsActive(),
            Not(HasCheated()),
            MinStat("love", 125),
            MinStat("sub", 75),
            ),
        Or(
            InInventory("car"),
            InInventory("sports_car")),
        ],
    "music": "music/roa_music/horizon.ogg",
    "do_once": True,
    })

label kleio_start:
    if kleio.love.max < 20:
        $ kleio.love.max = 20
    $ kleio.unhide()
    return

label kleio_event_01:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice")
    if not result:
        $ hero.cancel_event()
        return
    if kleio.love.max < 40:
        $ kleio.love.max = 40
    mike.say "Hello?"
    kleio.say "Hey. It's Kleio."
    $ hero.smartphone_contacts.append("kleio")
    if hero.charm >= 25:
        mike.say "Oh, hey Kleio. What's up?"
        kleio.say "Nothing, really. I just figured I'd call you and see if you wanted to come to the mall."
        mike.say "With you?"
        kleio.say "No, with my dog. Of course with me."
        if game.flags.band:
            kleio.say "You had better taste in music than I expected when you played for us, and I want someone to go to the record store with me."
            kleio.say "Are you in or out?"
        else:
            kleio.say "You seem to have better taste in music than your looks imply, and I want someone to go to the record store with me."
            kleio.say "Are you in or out?"
        mike.say "Oh! Uh, in. Definitely in. Should I meet you somewhere, or—"
        $ kleio.love += 1
    else:
        mike.say "Kleio? How did you get my number?"
        kleio.say "Does it really matter that much? Sheesh, why are you so defensive?"
        "She's one to talk."
        mike.say "Nevermind. Sorry. What do you need?"
        kleio.say "I'm bored, Sasha's at work and Anna is busy. Do you want to come shopping with me or not?"
        "I hesitate. Shopping isn't my thing by any means, but any chance to break down Kleio's icy exterior is probably one I should take."
        mike.say "Um. Sure, I guess. What are we shopping for?"
        kleio.say "Music."
        mike.say "Oh. Uh, ok then."
    kleio.say "Meet me at the mall."
    mike.say "I'll be there."
    kleio.say "See you in a minute."
    "Before I even realize it, Kleio hangs up the phone on me."
    scene bg mall1
    show kleio date
    with fade
    "When I arrive, Kleio is waiting for me at the entrance of the mall."
    kleio.say "Come on, let's go. The music store closes at eight and I want to be there before it's empty."
    "Shrugging, I follow along, deciding against mentioning whatever had made her upset—for now."
    show bg mall2 with fade
    "We walk in relative silence, with only a few short words between us, Kleio occasionally tapping away at her phone as we walk."
    "Feeling confident, I decide to ask her about it."
    if hero.charm < 25:
        mike.say "Who are you talking to on there?"
        show kleio date annoyed
        "Kleio glares at me, eyes flaring, and I immediately get the notion that asking this was a bad idea."
        show kleio angry
        kleio.say "None of your business, asshole. I invited you out to go shopping, not to interrogate my personal life."
        "Before I get another glance, she slides her phone back into her pocket."
        $ kleio.love -= 1
    elif hero.has_skill("video_games"):
        mike.say "Playing a game?"
        "Kleio scoffs, slipping her her phone in her pocket, stifling a laugh."
        kleio.say "What, am I twelve now? No, I'm just texting."
        mike.say "Who? Is it someone I know?"
        show kleio date annoyed
        kleio.say "Ugh. No. Mind your own business, okay?"
        mike.say "Ah. Well, I definitely recommending downloading this one game. It's called—"
        kleio.say "No offense, but I don't really care."
        show kleio date normal
        "Despite her harsh words, I can see her hiding a smirk."
        $ kleio.love -= 1
    else:
        mike.say "Whatcha doing?"
        "Kleio looks up at me, annoyed."
        show kleio date annoyed
        kleio.say "Nothing. What does it matter?"
        mike.say "I was just curious. It's not a big deal. It's just, by the way you were typing, it looked important."
        kleio.say "Well, it's not, okay? Quit being so nosy."
        "Before I get another glance, she slides her phone back into her pocket."
    show kleio date normal
    "Although it worries me for her, I decide against asking at all, knowing it would just upset her."
    "She leads me through the mall, dead set on her musical mission, as we weave through the patrons and departments."
    show bg bookstore with fade
    "I find myself nearly getting lost a few times, only stumbling up beside her just as we reach the entrance."
    kleio.say "Hurry up, slow-poke. We're here."
    "Swallowing, I follow her, hoping to God this goes well."
    "We're barely ten seconds into the store before she starts bombarding me with questions."
    kleio.say "Okay, [hero.name], which do you think? This record or this one?"
    "She holds up two records, and I gulp. This is my chance to prove myself, and I have no idea if I'm gonna get this right."
    $ A = 0
    menu:
        "Michael Johnson":
            mike.say "I definitely think you should go with the Michael Johnson album. I mean, who can go wrong with the King of Pop?"
            "Kleio looks unsure."
            kleio.say "I mean, I guess. He was cool and all, don't get me wrong, but I mean, I'm more of a guitar person myself."
            "I wince. Of course. I should've known that. I'm picking albums for Kleio, not myself. Damnit."
            mike.say "You're right. Maybe you should go with the other one."
            kleio.say "Yeah, maybe. I'll take your word for it for now."
            "Hesitantly, she shoves the album up under her arm."
        "Metallikea":
            mike.say "Metallikea all the way. Come on now, is that even a question?"
            "Kleio grins, shoving the album up under her arm without a second thought."
            show kleio happy
            kleio.say "Hell yeah, my dude. This one even has my favorite song on it: Master of Muppets."
            mike.say "Oh, yeah. That's an awesome song. The guitar in that is unreal."
            kleio.say "Right??"
            show kleio normal
            $ kleio.love += 1
            $ A += 1
    kleio.say "Come on, let's keep looking."
    "We wade through the store, Kleio working silently, picking up albums and examining them almost like a collector would."
    "Despite her almost permanent scowl on her face, I can't help but notice how beautiful she looks as she picks over this records."
    "Her physique is entertaining enough that I don't even really mind being here."
    "However, she eventually breaks my reverie, asking for my opinion once again."
    kleio.say "What about these two? Which do you prefer?"
    menu:
        "Pelvis Resley":
            mike.say "Uh, probably Elvis. He's really great."
            "Kleio frowns, looking at the albums again."
            kleio.say "You're right, but I'm not sure if he's really my style."
            mike.say "I mean, he makes rock music! We wouldn't have rock music without him."
            kleio.say "Yeah. You're right."
            "She shoves the album underneath her arm, but she doesn't look too happy about it."
        "Disrupted":
            mike.say "Disrupted are a seriously kickass band, in my opinion, at least."
            "Kleio grins, flipping the album over to read it."
            show kleio happy
            kleio.say "You have better taste in music than I thought, boy. I may just have to get this."
            "I can't hold back my smile."
            mike.say "I think you should. You'd love it."
            "With a huge smile, she shoves the record up under her arm before moving on."
            show kleio normal
            $ kleio.love += 1
            $ A += 1
    "It isn't long before her arms are full of albums, juggling them beneath her."
    "She's trying to hide the fact that she's struggling, but she's not very good at it."
    "Finally, I decide to step in."
    mike.say "Let me help you. At least until we get to the counter."
    if A == 2:
        show kleio blush
        "Kleio tries to look defiant, but the blush permeating her cheeks stops it quickly. I open my arms, and she deposits them cheerfully."
        kleio.say "Thanks. I appreciate that. You've been very helpful today."
        mike.say "Anytime, Kleio. I've liked helping out."
        $ kleio.love += 1
    elif A == 1:
        "Kleio looked up at me, almost startled by my offer."
        kleio.say "Oh. Uh, sure. Here, you can take half, and I'll carry the other."
        "Shrugging, I accept the offer, knowing her pride was probably in the way for letting me take them all."
        "She deposits half of them carefully into my arms."
    else:
        show kleio date annoyed
        "Kleio rolled her eyes, turning away from me."
        kleio.say "Oh, so now you decide to be helpful?"
        "I'm a little baffled by her response, but I do my best to try again."
        mike.say "I was only trying to be nice, Kleio."
        kleio.say "Yeah, well. I've got it."
        $ kleio.love -= 1
    hide kleio
    show kleio date normal
    "Kleio turns to me."
    kleio.say "I'm ready to check out. Come on, the register is this way."
    "Nodding, I follow her, watching her silently check out the records, the clerk filling two plastic bags full before she turns to me."
    kleio.say "Ready to go?"
    "Nodding, I agree with her."
    mike.say "Yeah, sure. Let's get going."
    show bg mall1 with fade
    "We walk in silence again, weaving through the nearly empty mall, exiting through the same door we came before Kleio decides to speak again."
    if A >= 1:
        kleio.say "Sorry for being so distant today. I've been...dealing with some stuff, and I needed a distraction."
        "I'm a little shocked by her admission, but I try not to show it."
        mike.say "I understand. It's no worries at all—do you want to talk about it? Maybe I can help."
        "Kleio sighs, making her way back towards my place, walking in silence for a moment before she decides to speak."
        show kleio sad
        kleio.say "My girlfriend and I broke up today."
        if hero.charm < 25:
            mike.say "Oh, so you're gay?"
            show kleio date annoyed
            "Kleio rolls her eyes, huffing in annoyance."
            kleio.say "Seriously? Is that really all you care about? For your information, no, I'm not. Well, not exactly. I'm bi. But it doesn't really matter."
            "I falter, realizing my reaction had obviously offended her."
            mike.say "I'm sorry, Kleio. I didn't mean to upset you. I just didn't know."
            show kleio date normal
            kleio.say "Yeah, well, now you do. Not like it matters now, anyway. She's out of my life, and I'm better off for it."
            mike.say "I hope so."
            show bg street with fade
            "We walk in silence, before reaching the door to her apartment complex. We stand awkwardly for a moment, before she finally breaks the tension."
            kleio.say "Well, have a good night, [hero.name]. Thanks for coming."
            mike.say "You're welcome, and you too, Kleio. I'm sorry about your girlfriend. If you need me, I'm a phone call away, okay?"
            "She nods, smiling slightly before turning away, disappearing into the evening, leaving me to walk myself upstairs alone."
            hide kleio with easeoutright
        else:
            mike.say "Oh, my gosh, I'm sorry to hear that. Are you doing okay?"
            "She shrugs, looking a bit resigned as she answers."
            show kleio annoyed
            kleio.say "Yeah. I mean, as fine as I can be after a breakup."
            kleio.say "I saw it coming for a while, if that counts for anything. It was like ripping off a band-aid though—it hurts, but it had to happen."
            mike.say "I totally understand that."
            show kleio sad
            kleio.say "It just sucks, I guess, you know? I mean, any breakup sucks, but the way she did it—it was like I didn't matter to her at all."
            mike.say "What do you mean?"
            show kleio annoyed
            kleio.say "She texted me. That's why I was on my phone so much on the way to the mall."
            kleio.say "I was trying to do damage control, to try and fix things between us again—I just didn't realize that for once, things weren't fixable."
            mike.say "Sometimes, things aren't meant to be fixed. Maybe you're better off without her."
            show kleio normal
            kleio.say "You think?"
            mike.say "I mean, you seem okay. Anyone who makes you sad and treats you like that doesn't really deserve to be in your life, you know?"
            kleio.say "I know. You're right. It just... hurts. Sorry to drag you into this."
            kleio.say "I just needed someone today."
            mike.say "Don't worry about it. I'm glad I could help a little bit though."
            "Though she's sad, she smiles slightly, and I feel my chest swell when I realized I made her smile."
            kleio.say "Yeah. Me too."
            show bg street with fade
            "We walk in silence for a moment, and, almost unconsciously, I slip my hand into hers."
            "For the moment, it feels right, and she doesn't object."
            "Eventually, we reach the door to her apartment complex, and she breaks her hand from mine."
            "For a moment, we stand awkwardly, neither of us knowing quite what to do."
            kleio.say "Well, goodnight [hero.name]. Thank you for coming tonight. It really means a lot to me."
            "I smile, pushing a strand of hair behind her ear, stepping closer to her."
            "I feel her heart pounding against mine, our chests pressed up against one another."
            mike.say "Anytime, seriously."
            $ kleio.love += 1
            if kleio.lesbian > 10:
                $ kleio.lesbian -= 1
            "She smiles, gazing up at me, and, before I have a chance to second guess myself, I lean down and kiss her."
            "For a moment, she seems startled, but then she leans into the kiss, wrapping her arms around my neck, leaning comfortably into my body."
            "Her lips are soft and warm against mine, and, when she finally pulls away, I feel it's far too soon."
            "I want nothing more than to kiss her again, feel her body, her breasts pressed against me. It takes everything I have in me not to pull her into me again."
            "She blushes, and, by the way she's looking at me, it's clear she's feeling the same."
            "But, before her hormones get the best of her, she steps away, with a smile still plastered on her face."
            if game.hour > 20:
                kleio.say "Goodnight, [hero.name]."
            else:
                kleio.say "Goodbye, [hero.name]."
            "I just smile, watching her go, gazing at her until I can no longer catch sight of her figure in the masses."
            hide kleio
            "Unable to wipe the smile from my face or the memory of her kiss from my mind, I turn to my complex, ready to tuck in, knowing who would be plaguing my dreams for the rest of the evening."
    else:
        kleio.say "Are you okay to walk yourself home? I have somewhere I need to be."
        "Somewhat startled and hurt by her question, I try my best not to show it."
        mike.say "Oh, uh, sure. It's no problem. Are you sure you don't want me to walk you home? It's really no bother."
        kleio.say "I can handle myself. Thanks, though."
        "Kleio nods, and I realize she's already leaning away from me. At this point, I have to let her go."
        mike.say "Okay. You're welcome. Have a good night, Kleio. Thanks for hanging out with me."
        kleio.say "Yeah. I'll see you at practice, [hero.name]."
        hide kleio with easeoutright
        "I watch her go, walking quickly and brusquely, and I find myself feeling almost sad as she leaves."
        show bg street with fade
        "Hoping I can redeem myself later, I turn, prepping myself for the long walk home that I hadn't anticipated taking alone."
        "Turning my gaze from the sunset and Kleio to the quickly rising night, I begin my lonely journey home."
    $ kleio.flags.nokiss = False
    $ game.room = "street"
    return

label kleio_event_02:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Kleio")
    if not result:
        $ hero.cancel_event()
        $ kleio.love -= 5
        return
    if kleio.love.max < 60:
        $ kleio.love.max = 60
    $ renpy.dynamic("satisfaction", "tattoo", "selection")
    $ satisfaction = 0
    mike.say "Hey Kleio, what's going on?"
    kleio.say "Nothing much."
    kleio.say "Anyways—are you doing anything right now?"
    mike.say "No, not really. Why?"
    kleio.say "How do you feel about tattoos?"
    "For a moment, I can feel my heart plummet into my stomach."
    "I know that Kleio and I are getting close, but, if she's suggesting matching tattoos, that's a one-way train to crazy town that I really don't want to be on."
    mike.say "Uh, Kleio, I'm glad we're friends, but..."
    kleio.say "Bitch, do you think I'm suggesting we're getting matching tattoos? Oh my God..."
    mike.say "Oops. Well, can you really blame me, Kleio?"
    kleio.say "Quit being a dumbass. Do you want to come with me while I get my tattoo or not?"
    mike.say "Uh, sure, I guess."
    kleio.say "Great. I'm outside. Hurry up—my appointment is in 10 minutes."
    mike.say "What? Kleio—"
    "Before I can finish my statement, she abruptly hangs up on me."
    "She has a bad habit of doing that, and of randomly showing up at my house, but, considering her, I had better get used to it."
    scene bg house
    show kleio casual
    with wiperight
    "I get dressed quickly before making my way down the stairs to her car. She is lounging outside, finishing up a cigarette, before she sees me."
    hide kleio
    "She doesn't waste time in waving; instead, she jumps into the car, gesturing I follow, before speeding off towards the parlor."
    scene black
    play sound car_door
    pause 0.4
    play sound car_door
    queue sound car_ignition
    scene bg street with fade
    with vpunch
    "She speeds and swerves through traffic, her music blaring so loud that I have to scream to talk to her. However, she doesn't seem phased."
    mike.say "What are you getting?"
    kleio.say "You mean, what tattoo?"
    mike.say "Yeah."
    kleio.say "I'm not sure. I haven't quite decided. I'm torn between two—a wolf walking across my collarbone, or a pair of angel wings on my back. Which do you think?"
    menu:
        "Wolf":
            mike.say "A wolf. Duh! That's so badass."
            kleio.say "You think? I was worried it came off a little too 'alpha bitch'."
            mike.say "No, totally not. I love it, and you should totally get it. I mean, if it's want you want, anyways."
            if kleio.sub > 25:
                kleio.say "You know what? Let's fucking do it [hero.name]!"
                $ tattoo = "wolf"
            else:
                kleio.say "Sorry, I think I'll go with the wings [hero.name]."
                $ tattoo = "angel"
        "Angel wings":
            mike.say "Get the angel wings! Holy shit, those would be cool as fuck."
            kleio.say "Right? It's an idea I've had since I was a kid. I've just never really had the opportunity to get it done before now."
            mike.say "Well then seize the motherfucking day then, Kleio. Get your angel wings."
            kleio.say "You know what? I absolutely should. Thanks, [hero.name]."
            $ tattoo = "angel"
            $ satisfaction += 1
        "None":
            mike.say "I'm not sure, I'm not really a big fan of tattoos."
            "Kleio rolls her eyes at me, clearly annoyed."
            kleio.say "Prude."
            mike.say "Hey!"
            kleio.say "Whatever. I'll just figure it out myself."
            $ tattoo = "None"
            $ satisfaction -= 1
    show kleio casual
    scene bg mall1
    with fade
    "Before I even realize it, we've arrived at the tattoo parlor."
    "The neon sign is blinding, and the artistry, although clearly talented, is gaudy as hell. I feel a chill as she drags me into what is clearly her element."
    scene bg tattooshop
    show kleio a casual
    with fade
    "She is not an unknown patron in this shop, sharing a smile with nearly everyone she passes."
    "I feel very uncomfortable, watching the stares rake up and down my unfamiliar body as she makes her way to her appointment room."
    "Her artist, clearly expecting her, is prepped and ready for her arrival. They exchange pleasantries, with me almost entirely ignored, waiting on the sidelines."
    "Finally, without a word to me, the tattoo artist gestures to a small folding chair in the corner, designed for guests of the one getting the tattoo."
    "Feeling regret about this whole endeavor, wondering if I even should have come, I slip into the chair, hoping that at least some part of this will keep me interested."
    "Luckily, I don't have to wait very long for something interesting to happen."
    "As though it was normal, as though it didn't matter at all, Kleio crossed her arms at her waist and casually pulls off her shirt."
    hide kleio
    show kleio a topless casual
    with dissolve
    "Although I could feel her eyes on me, I couldn't help but take in the view—she had gorgeous breasts, and I couldn't stop thinking about how it would feel to have my hands on them..."
    "My reverie is interrupted by Kleio's harsh laughter."
    kleio.say "Enjoy the view, Loverboy, because it's all you're gonna get for a while."
    hide kleio
    scene bg black
    show tattooparlor kleio topless
    with fade
    "As soon as she said it, she slid into the chair, breasts down, back up, hiding herself from my view in preparation for the needle."
    "Feeling slightly dazed, I struggled to get my thoughts straight again as the whir of the needle began to fill the room."
    "We sit in silence for a while, and I feel the awkwardness fill the room."
    "It's hard to hear over the tattooist's needle, and he needs to concentrate, so yelling isn't very conducive in the room either."
    "For a while, it is just Kleio and I, eyes awkwardly locking every few minutes as the needle dives and surfaces from her flesh."
    $ kleio.flags.tattoo = tattoo
    hide tattooparlor kleio
    show tattooparlor kleio kleio_casual topless
    with dissolve
    "Finally, though, after about an hour of waiting, the artist stepped out to take a quick water break."
    "Kleio sighs, clearly relieved to have a break from the pain, before turning to me."
    kleio.say "Have you ever considered getting a tattoo or piercing before?"
    menu:
        "No way":
            mike.say "No way."
            "Kleio rolls her eyes before continuing the conversation."
            kleio.say "Why not? Too chicken?"
            menu:
                "Yeah":
                    mike.say "Yeah...I just have a low pain tolerance, I guess."
                    kleio.say "Oh my God, don't be such a fucking baby. It's really not that bad, honestly, especially after you get used to it."
                    mike.say "I don't know, Kleio. I'm just not feeling it."
                    "She scoffs, annoyed, as the artist reenters the room, looking rejuvenated."
                    kleio.say "Whatever."
                    scene bg tattooshop
                    $ satisfaction -= 1
                "No":
                    mike.say "No."
                    kleio.say "Then what is it?"
                    "I shuffle uncomfortably, knowing this is going to be an unpopular opinion, especially in a tattoo shop."
                    mike.say "It's nothing against you, or anyone in this place, but I just personally think that the unblemished human body is the most beautiful thing in the world, and adding anything else too it just detracts from the whole thing."
                    mike.say "Like a bumper sticker on a Ferrari."
                    "Kleio looks annoyed, but, surprisingly, keeps her cool, sounding almost dry as the artist comes back into the room."
                    kleio.say "How very Biblical of you."
                    "I roll my eyes, watching, almost bored, as the artist finished the last of the work, shooing us out of the store before I really have another chance to blink."
                    scene bg tattooshop
        "Yes":
            mike.say "Hell yeah!"
            "Kleio's eyes glint with excitement at my words."
            kleio.say "Then why not get something done? You don't have any yet, right?"
            mike.say "I don't know, I've just never really had the time or the money, you know?"
            kleio.say "You have the time now, and the money, too, right? Go wild, my dude."
            menu:
                "Not right now":
                    mike.say "Eh, maybe another time. I want to think about it more, you know?"
                    kleio.say "Suit yourself, Loverboy. It'd make you like ten times hotter."
                    "My mind starts racing, wondering what it means if Kleio thinks I'm hot, as the artist reenters the room to continue."
                    "I watch, almost bored, as the artist finished the last of the work, shooing us out of the store before I really have another chance to blink."
                    scene bg tattooshop
                "Sure":
                    $ satisfaction += 1
                    mike.say "You know what, maybe I will."
                    "Right as I speak, the artist reenters the room, overhearing the tailend of our conversation, dollar signs flashing in his eyes as he hears my passing remark."
                    "Artist" "What do you want done? I have a buddy who could come fit you in."
                    if hero.money < 200:
                        mike.say "Ah, I was just dreaming. I don't really have the money for much of anything at the moment."
                        "Artist" "Whatever. Suit yourself, my dude. Hopefully we'll see you back soon. In the meantime, let me finish up on your lady friend here."
                        "I sigh, leaning back into my chair, waiting as the artist finished the last touches on Kleio's piece."
                        scene bg tattooshop
                    else:
                        menu:
                            "Tattoo":
                                $ selection = 0
                                mike.say "A tattoo."
                                "Artist" "Fantastic. My buddy in the back can help you out after I finish up with Kleio here."
                                "Artist" "She shouldn't have much more to go."
                                "Artist" "Feel free to flip through the catalogue."
                            "Piercing":
                                $ selection = 1
                                mike.say "A piercing."
                                "Artist" "Sounds good to me. It shouldn't take too long, either. Let me finish up with Kleio here, and we can all go back."
                        "The Artist smiles, finishing up Kleio's piece for the next few minutes as I anxiously await my fate."
                        "Sooner than I thought possible, he was done, tidying up his things and breezily going over aftercare with Kleio."
                        scene bg tattooshop
                        show kleio casual
                        "She approached me with a grin, linking arms with me before dragging me back to the back office."
                        if selection == 0:
                            "Artist" "Alright, did you make a decision?"
                            "At Kleio's encouragement, I point to the design I chose—nothing too extravagant for my first time."
                            "The artist nods his approval, and, almost like I was in a dream, I found myself in the seat, listening to the buzz of the needle."
                            show kleio at center, zoomAt(1.5, (640, 1040))
                            "Kleio holds my hand as we go, her breasts hanging so close to my face, grinning at me like a child at a candy store, sending my heart and my mind into a fluttering, dirty mess."
                            kleio.say "It looks great."
                            "We remain like that for a while, the dull aching pain easily forgotten when replaced with Kleio by my side."
                            "Before I know it, the tattoo is done, the artist leaning back from my body and grinning as he admired his work."
                            "He delivers his aftercare advice with ease, my mind struggling to pay attention as Kleio's warm body pressed closer and closer into mine."
                            "Hoping I had done everything right, we leave the shop, almost giddy, admiring our new art together."
                        else:
                            "Artist" "Nice choice. Just hold still—this shouldn't take long."
                            show kleio at center, zoomAt(1.5, (640, 1040))
                            "Kleio slips her hand into mine, squeezing it nicely as the artist prepped the area for the needle."
                            "I held my breath noticing her beauty, her warm skin, her breasts pressed so nicely against me, that I barely even noticed the needle jam itself into my skin."
                            "Before I even know it, it's all over, and we leave the shop, smiles on our faces, clutching aftercare in our hands as we leave the store, almost giddy."
    if satisfaction >= 0:
        show kleio casual happy
        kleio.say "I had a lot of fun today, [hero.name]. And it looks like you did, too. Thank you for coming."
        mike.say "Anytime. Anything for you, Kleio."
        "She grins at me, before reaching up, and placing a breathy kiss on my cheek."
        "My mind is spinning, grin plastered permanently on my face, unable to even breathe the whole ride home."
        $ kleio.love += 5
        if kleio.lesbian > 10:
            $ kleio.lesbian -= 1
    else:
        show kleio casual annoyed
        kleio.say "Well, thanks for coming."
        "I'm not stupid—I can tell things are awkward between us. Whatever it may be, I don't want stick around to find out what's causing it."
        mike.say "Yeah. Anytime, I guess."
        show kleio normal
        "She smiles weakly, before gesturing to her car, at least having the decency to take me home."
        "My mind reels the whole ride home, confused and wondering what Kleio and I even are."
    hide kleio
    $ kleio.flags.nodate = False
    $ game.room = "house"
    return

label kleio_event_03:
    scene bg bedroom1
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Kleio")
    if not result:
        $ hero.cancel_event()
        return
    if kleio.love.max < 80:
        $ kleio.love.max = 80
    mike.say "Hello?"
    "Her voice sounds disjointed and far away through the phone, but I'd recognize it just about anywhere."
    "I could barely hear the noise of a car driving in the background."
    kleio.say "Are you awake?"
    "I blink, surprised by her frantic tone and the time of her call."
    mike.say "I am now. What's up? Are you okay?"
    kleio.say "Sorry. Are you doing anything right now?"
    mike.say "Well, I was sleeping. Why?"
    kleio.say "I want to show you something. I'll be at your house in 10."
    mike.say "Wait, Kleio! Hold on, I—"
    "Before I can get a word in edgewise, I realize that she's hung up on me."
    "Groaning, fully awake now, I decide that I may as well get ready for her arrival."
    scene bg livingroom with fade
    "Knowing Kleio, she won't stop until she gets what she wants, whatever that may be."
    play sound door_knock
    "Purposely avoiding looking at the clock, knowing it's way earlier than I'd ever wake up otherwise, I finish getting dressed just as I hear a quiet knock at my door."
    scene bg house
    show kleio date
    with wiperight
    "I open it slowly, facing a small Kleio, who is staring up at me expectedly."
    mike.say "Kleio, what—"
    show kleio at center, zoomAt(1.5, (640, 1040))
    with vpunch
    "Once again she interrupts me, placing a finger against my lips, shushing me."
    kleio.say "Shh. Don't ask questions."
    $ BAD = False
    menu:
        "Insist":
            mike.say "Uh, no, Kleio, I am definitely going to ask questions. What the hell is going on?"
            show kleio annoyed
            "She rolls her eyes, annoyed, but decides to give me an answer."
            kleio.say "I told you, I want to show you something."
            mike.say "Show me what?"
            show kleio angry
            kleio.say "It's a surprise, dumbass. Are you in or what?"
            "Grumbling, knowing there was no chance I'd ever be able to fall back asleep after this, I agree, allowing her to lead me down the stairs to her car."
            $ kleio.love -= 1
            $ BAD = True
        "Go along":
            "Against my better judgement, and slightly excited, I stay quiet, allowing her to lead me out of my house and down the stairs to her car."
    hide kleio
    show kleio c date punk
    "Kleio has a wild glint in her eyes as she quickly loads us into her car and takes off towards the edge of town."
    scene black
    play sound car_door
    pause 0.4
    play sound car_door
    queue sound car_ignition
    scene bg street with fade
    with vpunch
    "She speeds through the empty streets, street lights shining into our car like police headlights."
    menu:
        "Tell her to slow down":
            mike.say "Kleio, what the hell? Slow down!"
            "Kleio rolls her eyes, ignoring my requests as I scramble to find my seatbelt and a handhold, praying there is no one else out on the road with us."
            $ kleio.love -= 1
            $ BAD = True
        "Enjoy the ride":
            "I can't hold in a hoot of excitement as we tear down the streets, the night still dark and empty as we drive further and further from the city center."
            "Any thoughts of where we might be going were left behind me, my heart racing faster and faster as I realize how beautiful the girl I'm sitting beside really is."
    "Finally, we slow down, reaching an abandoned storage building that rests on the very far edge of town."
    "She curses as she realizes that the night was getting lighter, the deep navy slowly shifting into a paler blue."
    play sound car_door
    pause 0.4
    play sound car_door
    show kleio c date with moveinright
    kleio.say "Damn it, we have to hurry, [hero.name]. Come on."
    if not BAD:
        "Almost unconsciously, she slips her hand into mine, dragging me across the dirt parking lot and towards the entrance of the crumbling building, kicking up dirt and grime as we run."
    else:
        "She takes off without a glance back at me, leaving me to chase after her as fast as I could, our feet kicking up clouds of dirt as we approached the entrance to the building."
    scene bg alley
    show kleio c date
    with fade
    "Finally, we arrive at the base of the large, almost crumbling building, staring up at the decrepit brick, the night light just barely raising before us."
    show kleio a date seductive
    "Kleio stares up at me, a mischievous glint in her eye."
    kleio.say "Ready?"
    menu:
        "Sure":
            mike.say "Hell yeah, I'm ready."
            show kleio
            "With a huge smile now plastered on her face, she grabs the large concrete door and yanks it open, dragging me across the floor to a rickety metal ladder on the opposite side of the wall."
        "No":
            mike.say "No! No, Kleio, stop. Just stop. I'm all for being impulsive, but not like this. Are you high or something?"
            show kleio surprised
            kleio.say "What? No! Jesus, [hero.name]. I'm not."
            mike.say "Well, regardless, I'm not going in a creepy ass building with you alone without some idea of what's going on."
            show kleio normal
            "My words, although harsh, seem to finally get to Kleio. She sighs, turning to me, her face entirely unreadable."
            kleio.say "There's a view. A really, really good view. And, I don't know, it's probably stupid—but I just wanted to share it with someone. Okay?"
            "I couldn't hide my shock. This whole trip was just for the sake of a sunrise?"
            "I'm tempted to back out, go back home and curl into my bed, forgetting this whole ass thing, but I catch a glimpse of her face, and I can't."
            "I can tell that, as much as Kleio doesn't want to admit it, wants to stay tough and untouchable to the outside world, there is something underneath there that she can't hide forever. She has pain I can't understand, but she's trying to let me in."
            "And the only way there is climbing up to the top of this damn roof."
            "Sighing, I lean over, and help her push the heavy door open."
    hide kleio with moveoutleft
    scene bg alley at dark with dissolve
    "We get to the ladder quickly, quicker than I thought possible considering the decrepit nature of the building, her body moving at an almost frantic pace to get to the top of the building."
    "The clangs of the metal are jarring, and, although I'm trying to swallow my fear, I can't help but think that this whole thing is going to collapse out from underneath me."
    "That this stupid ladder is how I go, and I'm going to have to explain to God what the hell I was trying to do, and, truly, having no idea at all."
    "Kleio notices my fear, and smirks, making a point to climb to the top even faster."
    scene bg blank with dissolve
    scene bg rooftop with dissolve
    "Despite my anxiety, we make it to the roof fine, nearly unscathed, climbing onto the large concrete surface just in time to catch the bright, scathing sun in our eyes."
    "I forget about Kleio for a moment, walking slowly towards the sunrise, soaking in the view."
    "I stare forward, the yellow beautiful and ethereal in the fresh sky."
    show kleio b date at flip, zoomAt(1.1, (320, 440)) with dissolve
    "Barely able to break my face away, I see Kleio, looking like a goddess in the light, almost unconsciously slide to the ground, sitting cross legged to watch the sunrise."
    hide kleio
    show kleio a date at flip, zoomAt(1.65, (340, 540))
    with dissolve
    "Without thinking about it, I join her by her side to watch."
    "We watch in silence, unthinking of the time or of the other person sitting beside me, simply taking in the view before us, only the sounds of the settling building, the distant highway, and the other's breath keeping us company."
    "Finally, Kleio breaks the silence with just one simple word."
    kleio.say "See?"
    "I nod, too overcome by the view to say anymore."
    if not BAD:
        show kleio happy blush
        "I see her smile at me, ducking her head to hide her barely visible blush."
        "It is this ethereal view, the sight of her rosy smile against the sunrise, that finally sends me spiraling back down to reality."
        mike.say "Why did you show me this, Kleio?"
        show kleio normal
        "She looks startled, but not angered, by the intrusive question."
        "She breathes in, holding it for just a moment before she let it go, her sigh heavy and laden with something I can't entirely understand."
        kleio.say "I don't know, [hero.name]. I know we don't know one another all that well—we only met recently, if I'm being honest with myself."
        kleio.say "Though, I can't help but feel that, on some level, we understand one another more than we realize, you know?"
        "Her words catch me off guard. They're vulnerable, and, for once, completely untinged by sarcasm."
        "This was a rare moment for her, and I wasn't ready to let her go just yet."
        mike.say "I agree, Kleio. I do."
        show kleio happy
        "She smiles, and, for a moment, I think that her beauty rivals the sunrise, or, even, if I'm daring, is more beautiful than it."
        show kleio normal
        kleio.say "I know it seems really silly—it's just a sunrise, we get hundreds of them, and we can look at pictures of them, and really, they aren't that special at all—but, then again, this is special, in a kind of stupid way, to me, at least."
        "This is my space, my home, my little corner of the universe. I've never really taken anyone else up here, but I got sick and tired of being lonely every single day. I wanted to share it with someone else. So, for whatever stupid, silly reason—I brought you."
        mike.say "It's not stupid, Kleio. I'm really glad you did."
        "I slide my hand across, grabbing hers in mine, not wanting to shatter the moment with anything more."
        kleio.say "Really?"
        mike.say "Really. I couldn't think of anyone better to share this moment with."
    else:
        "We sit in a comfortable silence, her easily a foot away from me, lost in thought."
        "Her face is clouded with something I can't understand, and, although I'm distracted by the sunrise, her face distracts me more."
        "Finally, I break the silence."
        mike.say "Kleio, why did you bring me here?"
        kleio.say "I don't know. Isn't it enough that I wanted someone to share the sunrise with?"
        "Her answer, although it's valid, stings. I can tell she's holding back from me."
        mike.say "Is that really all?"
        kleio.say "I don't know, [hero.name]."
        show kleio annoyed
        kleio.say "Does there have to be a deep, fucking metaphorical answer to every single thing that I do?"
        kleio.say "Can't we just want to enjoy the sunrise?"
        mike.say "Chill, Kleio. Yes, I think that we can enjoy the sunrise."
        mike.say "In a planned event. But calling me randomly, speeding down the road—wouldn't that come across as very deliberate to you, if I did it to you?"
        show kleio normal
        "Kleio ignores me, and I can tell her walls are up, once again."
        kleio.say "Nope. Sometimes people just want to enjoy a fucking sunrise, [hero.name]."
        "I sigh, finally looking away from her, the sky shifting almost as rapidly as her moods."
        mike.say "I guess so, Kleio. I guess so."
        "We sit in silence, the light filling the spaces between us as they get wider and wider."
    scene bg rooftop
    show kleio date
    with fade
    "Finally, as the sun gets to be too high, the sky too blue to justify watching the sunrise anymore, Kleio gets to her feet."
    kleio.say "Are you ready to go? There isn't much more to watch."
    mike.say "I guess you're right. Let's go."
    "We make our way down in silence, taking in the view in our own brains."
    if not BAD:
        kleio.say "So...do you want to go get coffee, or something? Talk about what we saw, or something?"
        mike.say "Really?"
        kleio.say "Yeah. I mean, only if you want to. You seem pretty tired, but that's why I suggested coffee."
        mike.say "Yeah. Yeah! I'd like that a lot, Kleio. I'd like that a lot."
        show kleio happy
        kleio.say "Fantastic. Let's go, then. Let's go."
        "I smile at her, and slip my hand across the console, taking her hand into mine before we drive off towards the morning sun."
        if kleio.lesbian > 10:
            $ kleio.lesbian -= 1
    else:
        kleio.say "Well...that's all, I guess. I can take you home now."
        mike.say "That was really all you wanted to show me?"
        kleio.say "Yeah, that was it, [hero.name]. That was all."
        "I can sense the discomfort in her voice, and, despite my intense curiosity, I let my tiredness get the better of me, and I decide to let it go."
        mike.say "Whatever, Kleio. Let's just head home."
        kleio.say "Sounds good. You can go get the sleep I interrupted you from."
        mike.say "Yeah...yeah. Sounds good."
        "Kleio nods, and proceeded to drive in silence towards the morning sun, with me left confused, bewildered, and unsure of where Kleio and I were."
    hide kleio
    $ game.pass_time(1)
    return

label kleio_event_04:
    $ kleio.flags.schedule = "work"
    "Normally I'd always be sure to either take my car back to the dealership, or at least an approved vehicle repair centre when it's on the fritz and I'm left clueless as to why."
    "It just saves time and hassle, as they take it away and fix the problem without me having to do anything more than sit with a coffee and a magazine until the car's ready."
    "The only real problem is that it comes at a price, and as I'd been feeling the pinch in my wallet a little more than usual this month, I made the mistake of listening to the advice I was offered."
    "I guess that I should have smelled a rat when Sasha chimed up at the mere mention of my car troubles, as she's not exactly an expert in that particular area herself."
    "But she kept insisting that she knew a mechanic that worked at a local garage, whom she made sound like some kind of mechanical miracle-worker."
    "In the end, I don't know if I agreed to look them up more because I was convinced, or just wanted Sasha to shut up gushing about this guy I was to ask for called 'Kay'."
    "Shrugging this mystery guy off as some Neanderthal petrol-head she must have dated at some time in the past, I looked the address up and resolved to drive down there as soon as the opportunity arose."
    show bg garage with fade
    "Pulling onto the concourse in front of the place, it looks like one of those garages where they make those reality TV shows."
    "You know the ones I mean - where a bunch of bearded apes restore heaps of crap they buy on the cheap and then sell them to idiots with more money than sense."
    "I can't see any specimens of the former kind around, so I risk hitting the horn in the hope of attracting someone's attention."
    "After about a minute, a guy in a trucker cap and a sleeveless lumberjack shirt appears, squinting at me as he emerges into the daylight."
    "He looks like the missing-link if grunge had been a thing back at the dawn of mankind, and I instantly assume this must be the mysterious 'Kay'."
    "I get out of the car and try my best to communicate with this modern-day primitive."
    mike.say "Hey, are you Kay?"
    "The man stares at me like I just said the most stupid thing imaginable and slowly shakes his head."
    mike.say "Erm...okay - is Kay in the back?"
    mike.say "It's just that a friend recommended I have him take a look at my car."
    "When the guy shakes his head a little and chuckles softly to himself, I begin to think that Sasha was bullshitting me or that I've come to the wrong place."
    "But then he kind of nods and gestures back over his shoulder, which I take to mean that I should look for Kay inside."
    "I nod my thanks and make my way inside, hoping that Kay will prove to be more talkative, even if more friendly might be too much to ask."
    "Inside, when my eyes adjust to the change in light, I'm presented with a typical small-time garage."
    "Tool-racks line the walls and elevators lift cars off of the ground so that they can be worked on from beneath."
    "Vintage signs hang on the walls and the smell of engine oil seems to permeate the very air itself."
    "At first I can see no evidence of life, but the sound of something crackling and the occasional burst of light draws me to the very back of the place."
    "Expecting to have to shout over the sound of what can only be a welding rig in full operation, I round the corner and stop dead in my tracks."
    "The flying sparks confirm that I was correct in at least one sense, but what they illuminate in dazzling flashes of light shows I was way off of the mark in another."
    "The welder has a mask on, so their face is completely hidden to me."
    "But their overalls are open to the waist, the arms tied around the midriff to keep them out of the way."
    "Aside from this and the heavy welding gloves, they're wearing only a tight little vest top."
    "A top which shows off an unmistakably pert and petite pair of breasts that are not restricted by a bra of any kind."
    "Below these is a tight, shapely and very feminine stomach, with a hint of tattoos and smears of grease and oil across the otherwise pale skin."
    "I don't think I've ever felt the elastic on my shorts begin to stretch so much at the sight of metal being welded to metal before now..."
    "Unaware of where I'm putting my feet, I kick something heavy and it makes a sound loud enough to alert the welder of my lingering presence."
    "She immediately kills the welding torch and turns to face me, pulling off the gloves and tossing them down as she does so."
    "Is it my imagination, or does she actually pause before lifting her mask?"
    "Whatever her intentions, that couple of seconds as she regards me from behind it allows me to truly appreciate all there is to see."
    "I can tell now that the oil and grease are smears from her own fingers as she must have wiped them across her belly."
    "And I can also see the fine coat of perspiration on her exposed skin, and how it's soaking the fabric of her vest so that it clings to her nipples too."
    "When she finally lifts the visor of the mask, I almost hold my breath in anticipation of what lies below."
    show kleio work with dissolve
    kleio.say "Hey there, Loverboy - you like what you see?"
    mike.say "Huh...Kleio...is that really you?!?"
    kleio.say "Nah, I just pretend to work here, you know?"
    kleio.say "Like in case some goof that I know comes in and I can make them gawp!"
    "As she treats me to the habitual round of insults I've come to expect from Kleio, my brain actually begins to function again."
    "Of course, I assumed Sasha meant 'Kay', when she must have meant 'K' as in an initial."
    "Also, I don't recall her ever specifically mentioning that the mechanic was a guy either."
    "It all begins to make a lot more sense to me now."
    kleio.say "Let me guess - Sasha sent you, right?"
    "I nod helplessly, much to Kleio's amusement."
    kleio.say "Ah, don't feel bad - she does it all the time, so you're not the first to fall for it."
    "Kleio pulls the welding mask off, revealing that she's got her hair tied up under a bandana that's wet with sweat."
    "She wipes her forehead with the back of her hand, and I get a whiff of oil and grease from her direction that makes me feel pretty weird."
    "I mean, she's filthy, covered in sweat and dressed in grimy overalls."
    "But all the same I can't keep my eyes off of her for as much as a second right now."
    "There's just something about the look and the scent of her that makes me want to roll around until I'm as dirty as she is."
    "So long as we're rolling around together when I do it..."
    kleio.say "So, have you got something that you want me to take a look at?"
    kleio.say "Maybe see if I can handle it for you?"
    "I don't know if the double entendres are deliberate or not, so I choose to ignore them and soldier on."
    mike.say "Yeah...yeah...I wondered if you'd take a look at my car?"
    mike.say "It's parked out front and I'm damned if I know what the problem with it is!"
    show kleio happy
    "Kleio gives me a smile that, while clearly patronising in nature, is actually quite endearing."
    kleio.say "Come on, [hero.name], show me what you've got!"
    show kleio normal
    "We walk out onto the forecourt, and I point out my car to Kleio as I walk over to where I left it parked."
    if "sports_car" in hero.inventory:
        $ hero.flags.vehicle_in_garage = "sports_car"
        $ kleio.love += 5
        $ kleio.flags.niceCar = True
        show kleio blush
        "I can't help feeling as though the balance has suddenly been redressed at least a little as Kleio lays eyes on my car for the first time."
        "It's not like her eyes pop out of her head or anything so dramatic, as she's not the kind to let on like that."
        "But all the same, she takes her time in looking the car over."
        "And when she finally does manage to pay me some attention again, she's wearing a grudging look of respect on her face."
        kleio.say "Okay, I admit it - I had no idea that you'd drive something this impressive!"
        "I'm tempted to gloat, as it's so hard to win anything resembling a compliment from a hard-ass the likes of Kleio."
        "But it's also such a pleasant change to see her being this positive, and so I try to keep the mood light."
        mike.say "Well, you never told me that you were a mechanic either."
        mike.say "So maybe we can call it even, yeah?"
        "Kleio responds to this with a little thump to my arm."
        "But then follows that up by wrapping her own arm around the very same one a moment later."
        show kleio seductive
        "She leans her weight against me, still looking at the car in an almost dreamy manner."
        kleio.say "I'm really gonna enjoy getting my hands dirty on this one."
        show kleio normal
        kleio.say "I'll call you just as soon as I'm ready, and you can come straight over and inspect my work, okay?"
        "I nod in agreement, not sure I should mention the fact that she's got me so turned on I'm hearing every word as an innuendo right now."
        "I leave the keys with her and call for a taxi to get me home."
        $ hero.lose_item("sports_car")
    else:
        $ hero.flags.vehicle_in_garage = "car"
        mike.say "Normally I'd just take it to the dealership and let them worry about it."
        mike.say "But seeing as how I know someone that's an expert when it comes to this kind of thing..."
        "Kleio smirks visibly as I present her with my choice of vehicle."
        "I've never been anything but conservative and sensible when it comes to my choice in cars."
        "So she's looking over a pretty average, safe Japanese model with a good fuel-efficiency and..."
        "Well, I have to admit it - lots of other features that she probably doesn't care two shits about either!"
        kleio.say "No worries - these kind are really easy to handle, very predictable, you know?"
        mike.say "Yeah...I guess so."
        "She looks at me sideways, clearly aware of the fact that I'm massively out of my depth here."
        "And that I get she's using my choice of car as a convenient means to insult me by proxy too."
        kleio.say "Don't worry your pretty little head, [hero.name] - I'll sort it out for you."
        "I thank her and order a taxi to get home, all the time feeling awkward and inadequate under Kleio's gaze."
        $ hero.lose_item("car")
    "Kleio gives me a brief wave from the forecourt as I pull away in the taxi."
    "She looks so improbable in her overalls and yet so undeniably sexy."
    "I can't help but wonder what other hidden talents she might have to be discovered."
    if kleio.love.max < 100:
        $ kleio.love.max = 100
    return

label kleio_event_05:
    scene bg studio
    "Every string I pluck on my guitar is nearly drowned out by the rain outside."
    "It's exhausting, trying to write music in these conditions, and I'm considering asking if we can just call it a night."
    show kleio at left with dissolve
    "Kleio, however, has me slightly distracted; her head is in my lap, leaning back as she hums a few muted tunes, while I absentmindedly stroke her hair. As exhausted as I am, I don't want this night to end."
    show sasha annoyed at right with dissolve
    "Right as I'm about to open my mouth to see what the plan is, Sasha, annoyed, throws down her sheet music, quickly getting to her feet."
    show sasha angry
    sasha.say "I can't do this anymore. I'm exhausted, and we aren't getting anything done."
    "Kleio sits up from my lap, confused."
    kleio.say "But Sasha, there's a massive rainstorm going on. Are you sure you want to leave?"
    show sasha annoyed
    "Sasha says nothing, just glares at Kleio through sleepy, angered eyes as she gathers up the rest of her things."
    menu:
        "Walk Sasha home":
            mike.say "Let me at least walk you home, Sasha."
            hide kleio
            "Although she's annoyed, she relents, and I gather her things and hold the door for her as we walk towards the front door of the small studio."
            "As soon as we're out of earshot, she spins around to face me, quickly grabbing her things from my arms."
            show sasha
            sasha.say "What are you doing with me?"
            "Baffled, I sputter out a reply."
            mike.say "What do you mean?"
            sasha.say "Kleio has been all over you for, like, the past two weeks, and instead of taking the opportunity I tried to give you, you're walking me out. You've gotta go back in there, I'm sure she's waiting on you."
            mike.say "What are you talking about?"
            mike.say "Kleio isn't into me. We're just—friends, I guess."
            "Sasha rolls her eyes."
            sasha.say "You've got to be kidding me. I knew you were an idiot, but I didn't know you were blind, too. Go back in there. Trust me for once, okay?"
            "Even though her words slightly embarrass me, I find myself nodding along anyway. I see the way Kleio looks at me, and I definitely do want more of it. Perhaps this annoying rainstorm has given me a chance."
            hide sasha
            "With a small smile to Sasha, I say goodbye, before returning back to the studio."
        "Let her leave":
            "I say nothing to Sasha, but do my best to be helpful despite her irritating attitude."
            "I quickly stack up her things, handing her a stack of sheet music, and push her backpack over to her."
            show sasha normal
            sasha.say "Thanks."
            "I smile at her."
            mike.say "It's nothing, Sasha. Goodnight."
            "Kleio follows suit."
            kleio.say "Goodnight!"
            hide sasha with moveoutright
            "All we get is a door slammed roughly on us, accompanied by a loud roll of thunder from outside."
        "Tell her to stay":
            mike.say "Sasha, I really don't think that's a good idea. It's not safe out there."
            "Sasha glares at me, sending daggers piercing through my skin as she roughly gathers her things."
            show sasha angry
            sasha.say "And who are you to try and stop me?"
            "I hesitate a bit, but the rainstorm doesn't seem to be letting up at all, and I really don't want Sasha to do something stupid just because she's tired and annoyed."
            "I get to my feet, walking towards her."
            mike.say "Sasha—"
            show sasha wtf
            sasha.say "Shut up, [hero.name]!"
            hide sasha with moveoutright
            play sound door_slam
            "Snarling, she turns her back on me and slams the studio door in my face."
            "Kleio sucks in her breath, and let out a low whistle behind me."
            kleio.say "Yikes."
    $ kleio.sexperience += 1
    show kleio at center with move
    "Hesitantly, I return to Kleio, who is now sitting cross-legged, elbows on her knees, leaning forward so far her shirt is gaping wide open. I can't help but take a look—she has gorgeous breasts."
    "She notices me looking, but, instead of shying away, she lets a slight smile play on her lips as she innocently leans forward just a tiny bit more, just enough to keep me interested."
    "My thoughts are scrambling as I stutter for a response."
    mike.say "So, uh, what are we gonna do for the rest of the night?"
    show kleio happy
    "Kleio smiles, shrugging her shoulders. Her breasts move with her."
    kleio.say "I'm not sure."
    show kleio normal
    "Thunder rolls in the distance, and she winces, slightly."
    kleio.say "Definitely not going out in that."
    "I pull my eyes away from her chest, and go sit down next to her again."
    mike.say "You know, you look really good tonight, Kleio."
    show kleio blush
    "She blushes, but doesn't shy away. Instead, she stares deeply into my eyes, looking almost seductive as I cross the room."
    "My heart is pounding as I slowly take my seat next to her."
    "I manage to get out a stutter, but nothing further, simply blushing before I cross the room."
    "Kleio notices my nervousness and grins, watching me closely as I take my seat beside her."
    "She quickly flops down onto my shoulder, staring slightly up at me, eyes blinking slowly."
    "I feel my skin growing hot, embarrassed and aroused by her gaze."
    "I shift my seating position slightly, trying to hide my growing boner."
    show kleio at center, zoomAt(1.5, (640, 1040))
    "It doesn't work. Kleio sits up again, clambering around to sit on front of me, propped up on her knees, ass resting on her feet."
    "She drags her eyes down my chest, her eyes settling on my growing bulge, her face mere inches from mine when she speaks."
    show kleio seductive
    kleio.say "Excited, are we?"
    "I match her energy as best I can, leaning forward, close enough that our noses are now touching."
    "I smirk slightly, gazing deep into her eyes, only breaking my gaze to get a quick glance at her lips."
    mike.say "Can you blame me?"
    "I'm barely able to contain myself as I watch her slowly move closer."
    "Unable to help it, I find myself blushing profusely, once again trying to shift so that my boner is hidden."
    mike.say "Um, I'm sorry."
    "As I move, she reaches out, grabbing my knee and stopping me from moving."
    kleio.say "No, don't move. I don't mind."
    hide kleio
    show kleio kiss
    with fade
    $ kleio.flags.kiss += 1
    "Barely seconds pass before her lips are on mine."
    "She kisses me fiercely, hands moving swiftly to knock my legs out of the way before she climbs into my lap, wrapping her long, beautiful legs around my waist."
    "I tangle my hands in her short hair as she wraps her arms around me, digging her nails sharply into my back."
    "I gasp as she claws at me, and I feel her smile against my opened mouth."
    "Clearly this was her intention; she slips her tongue inside my mouth to meet mine, kissing me hard as she begins to rock her hips against mine."
    "My dick is rock-hard now, and I no longer try and hide it."
    "I'm shameless as she grinds against me, moaning against her lips as she kisses me."
    "Unable to help it, I slide my lips off hers, kissing down her neck, tracing her tattoo with my lips, listening intently to every moan that she lets out."
    "I match her rocking hips, stride for stride, making sure she knows how much I want her in that moment."
    "Her hands wander down my back, occasionally latching in when I place a small bite."
    "Eventually, they make their way down to my waistband, and she gazes up at me, making perfect eye contact as she begins to unbutton them."






































    show kleio naked kiss with dissolve
    $ kleio.flags.kiss += 1
    "Quick in my move against her, I match her, pace for pace, my hands moving to her own waistband to undo it."
    "Kleio doesn't even hesitate; she tears off my jeans like a hungry animal, placing kisses on whatever piece of bare skin she can find."
    "I return the favor, tearing off her shirt and undoing her bra, quickly leaning down to kiss her breasts as she helps me kick the last of my jeans off."
    "Her skin is hot against mine as I slowly lower her to a nearby table, my body rocking against hers as I feel her moan."
    "She gasps for air, but I keep kissing her, unable to draw myself away from the beautiful curves of her body."
    hide kleio
    show kleio naked seductive blush at center, zoomAt(1.5, (640, 1040))
    with fade
    "Eventually, she pulls me away, bringing my face back up to meet hers."
    "We crash together, looking like a show of modern art as we hastily try and get as much of each other as we can."
    "Gasping and out of breath, she pulls away, just for a moment, and looks me deep into my eyes. I know what she wants, but I want to hear her say it."
    mike.say "What do you want, Kleio?"
    "She leans up, wrapping her legs around my waist and pulling my hips as close to my body as she can."
    kleio.say "Shut up and fuck me!"
    $ CONDOM = False
    if hero.has_condom():
        menu:
            "Use a condom":
                $ CONDOM = hero.use_condom()
            "Do it raw":
                pass
    hide kleio
    if CONDOM:
        show kleio rough condom
    show kleio rough vaginal
    with fade
    "I need no further instruction; I thrust forward, filling her quickly, making her gasp in pleasure."
    "For a moment, I remain, overwhelmed by the feeling, before I slowly begin to rock my hips back and forth, building up a rhythm."
    "She gasps and moans every time I thrust forward, my hips roughly hitting her ass."
    "Her hands wrap around her own ass, spreading it open to help me get deeper."
    "I press on, so deeply ingrained in the pleasure of her body that I am barely able to focus on anything else."
    "Eventually, though, I notice her getting restless beneath me."
    "Her body is alight and so is mine, desperate to get more of her, to get as much of her as I can, to take her as fast and as hard as I can."
    "I want Kleio, more than anything, and I am doing all I can to have her."
    show kleio rough pleasure
    "Her moans begin to get sharper and louder, her breathing irregular, and I know she is getting close."
    "I keep with my rhythm, desperate to get both her and myself there."
    "She is moaning and crying out, nearly screaming in pleasure, and I find my own moans mixing in with hers, mumbled echoes of her name intermixed with cries of extreme pleasure."
    "Her body was fire, and she had set me alight."
    "Pressure builds up in me, and I begin to fuck her as hard as I could, my body a gun with the trigger nearly pulled."
    with vpunch
    "Almost as though we had planned it, she shot her head back, trembling and moaning, the pulsation from her orgasm setting off my own."
    show kleio rough ahegao
    if not CONDOM:
        show kleio rough creampie
        $ kleio.impregnate()
    with vpunch
    "I cum quickly, moaning her name loudly as I feel the pressure that had built up finally release in a moment of pure pleasure."
    with vpunch
    "For a moment, it was simply sweet, sweet ecstasy, before I carefully slipped out of her, falling back onto the floor, her quickly following suit beside me."
    hide kleio
    show kleio naked blush at center, zoomAt(1.5, (640, 1040))
    with fade
    "We both are quiet, simply taking a second to catch our breaths before leaning into one another."
    "I wrap my arms around her warm body, pulling her close to me as she hides a slight grin."
    "I make no effort to contain my own: I'm grinning as wide as I can."
    "Finally, she breaks the silence, sitting up, ear cocked to the sky."
    kleio.say "You know, I think the rain stopped."
    "Then, with an unmistakable grin, she tumbles back into my arms, and I couldn't help but laugh."
    mike.say "You know what, Kleio, you're absolutely right."
    show kleio happy
    "She smiles at me, before glancing up from in between my arms."
    show kleio normal
    kleio.say "Do you want to stay here?"
    mike.say "Actually, why don't we go back to my place?"
    "Winking, I gently pushing her off and helping her gather her clothes."
    mike.say "I'm sure we can have some more, uh, fun there?"
    hide kleio
    show kleio naked
    pause 1
    hide kleio
    show kleio casual
    "She enthusiastically agrees, and we both quickly change, leaving the dark studio behind as we race out into the dark night, two lovers that are, for a moment, simply alight with one another."
    "I pull her as close as I can to me, savoring for a moment her fluttering heartbeat."
    mike.say "Kleio, I don't think I ever want to leave."
    if kleio.love.max < 110:
        $ kleio.love.max = 110
    hide kleio
    scene bg black with timelaps
    pause 0.1
    $ game.pass_time(6, True)
    return

label kleio_event_05b:
    "It hasn't been anywhere near long enough since I dropped my car off at Kleio's garage for me to have been able to get the image of her in that hot, grimy state off of my mind."
    "But by the same measure, I was pretty sure that it hadn't been nearly long enough for her to have found what the problem was, let alone fix it."
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Kleio")
    if not result:
        $ hero.cancel_event()
        $ kleio.love -= 5
        return
    "So you can understand my surprise when I hear my phone ringing and see Kleio's name pop up so soon after I left the car with her."
    if kleio.love.max < 120:
        $ kleio.love.max = 120
    if kleio.sub.max < 100:
        $ kleio.sub.max = 100
    mike.say "Hey, Kleio - I guess this is about the car, right?"
    kleio.say "Yeah, [hero.name], that's right..."
    "I can't avoid making a frustrated sound as she pauses, letting the words trail off into an awkward silence."
    mike.say "It's going to cost me to fix the thing, isn't it?"
    mike.say "Okay, okay...just tell me what the damage is, let's get it out of the way!"
    "I wait for the answer that I'm dreading, thinking of how I took the car to her in the first place in the hope of avoiding such a large bill."
    "However the strained silence on Kleio's end continues, making me worry all the more."
    mike.say "Come on, Kleio - is it really that bad?!?"
    kleio.say "No...no...I think you're getting the wrong message here."
    kleio.say "The car's fine, better than ever, in fact."
    "I can't quite believe what I'm hearing."
    mike.say "It's what, Kleio?"
    kleio.say "It's fixed - the problem was pretty simple once I started looking into it."
    "I glance at my watch, frowning in puzzlement now."
    mike.say "Well...couldn't it have waited until the morning?"
    mike.say "The place I used to take the car always called during the day when they wanted me to come pick it up."
    "There's another strained silence, and I find myself almost willing Kleio to just come out and say what she means."
    kleio.say "Well, sure it could...but I was just working on it after hours, as you're a friend."
    kleio.say "And I wondered if you wanted to come down to the garage to get it now, and maybe have me talk you through what was up with it?"
    "Okay, now I feel like the worst person in the world for being so terse with her."
    mike.say "Ah, okay..."
    mike.say "Look, I'm sorry, Kleio...that was pretty ungrateful of me."
    mike.say "Can we forget all of that and just start the whole conversation over?"
    "I hear her let out a little chuckle on the other end of the line."
    kleio.say "Okay, so long as you promise to stop being a jerk to me?"
    mike.say "Okay, Kleio, I promise."
    mike.say "I'd love to come over and see your handiwork for myself."
    mike.say "Let me grab a taxi and I'll be right over."
    show bg garage with fade
    "I arrive at the garage a short time later, stepping out of the taxi to see that the forecourt and frontage are in complete darkness."
    "There's a hint that the lights are on inside from the glow that's escaping from around the doors, but the place still looks deserted."
    kleio.say "Hey, [hero.name] - over here!"
    show kleio work with dissolve
    "I follow the sound of her voice to see Kleio, standing in the out-spill of light from an open side door."
    "She beckons me over more eagerly than I might have expected, and then closes the door behind me."
    "I don't think anything of it when she takes a moment to lock it as well, as this isn't the best neighbourhood in town either."
    "She's wearing pretty much the same overalls, vest and bandana that she was when I dropped the car off the other day."
    "But the smears of grease and oil on her belly, arms and even across her cheek are, of course, new."
    "I hardly hear a word Kleio is saying as she leads me to the back of the garage to where my car is waiting."
    "All I'm interested is the smell of sweat and motor oil that's coming off of her right now."
    "That and the way her ass moves under the weight of her overalls as they're stripped to her waist and folded around her."
    "I honestly try to listen to what she's saying as we stand by the car, but right now it might as well we white noise to me."
    "In the end, all I can do is keep on nodding until she motions for me to sit in the driver's seat."
    play sound car_ignition
    "Not knowing exactly what she expects me to do, I fall back on turning the key in the ignition and then revving the car a couple of times."
    play sound car_ignition
    "I can see Kleio almost jump every time I do so, with an odd kind of look on her face."
    mike.say "Sounds great!"
    kleio.say "Yeah, it sure does..."
    show kleio blush
    kleio.say "I'd love you to make me rev like that..."
    "I'm so distracted by the car being fixed and my desire for Kleio that I almost totally miss what she just said."
    mike.say "What..."
    show kleio work seductive blush
    "Kleio looks almost bashful as she repeats herself, which is almost as surprising as what she actually said in the first place."
    kleio.say "I said...that I'd love you to make me rev like that..."
    "I look up, only noticing as I do so that she's come to stand right by me, inside the open door to the car."
    "From where I'm sitting, I'm looking her straight in the naked belly, close enough to reach out and touch."
    "Now I realise what the strange look on her face was when I was revving the car."
    "I can scarcely believe it, but Kleio must have been turned on by the sound!"
    "She's actually jealous of the way I'm treating the car!"
    "Now things are beginning to make more sense, from the admiration she gave me after seeing the car to working on it after hours."
    "All the way to asking me here to supposedly check out the job that she's done on it so late at night."
    "Is Kleio such a petrol-head that discovering I'm one too has elevated me in her estimation that much!"
    kleio.say "Come on, [hero.name]...don't leave me hanging here!"
    show kleio work topless with dissolve
    "She pulls off her vest, tossing it aside and letting her breasts sit proud and naked upon her chest."
    "I hadn't noticed how chill the air in the garage was until that moment."
    "But I certainly do now, as her small nipples pucker and stand erect, either from the cold, her arousal, or else both."
    kleio.say "Please - I want you to treat me just like you do this car."
    kleio.say "I promise that I'll be as much fun to ride..."
    "It's not like I needed much encouragement, or as if the image of her in those grimy overalls has been out of my head for more than a minute in the past twenty four hours."
    "Without answering her, I reach up and take her nipples between the forefinger and thumb of each hand."
    "I have no intention of treating Kleio just like I would my car, but I still feel a little like I'm pressing the ignition button as I squeeze them."
    "Only when she almost sobs with release do I actually begin to realise how much she must want this."
    "The very thought of a girl as outwardly tough and surly as Kleio being so turned on and vulnerable make me instantly start to harden."
    "Stepping out of the car, I keep pinching at her nipples and caressing her breasts as I find her mouth."
    hide kleio
    show kleio kiss naked
    with fade
    $ kleio.flags.kiss += 1
    "I try to kiss her gently at first, but I feel her tongue almost instantly force its way into my mouth all the same."
    "We're so close now that I can smell nothing but the grease and sweat that's all over Kleio's tight, lithe body."
    "The scent of it is even more intoxicating now that we're wrapped in each other's arms, something I never thought would turn me on before I caught it emanating from her."
    "I already know that this isn't going to be anything deep and meaningful."
    "If romantic sex is like a long, relaxing drive in the countryside, this is going to be more a hair-raising tear down a drag-racing strip."
    "Pushing Kleio backwards with no resistance whatsoever, I glance around almost frantically for the nearest spot that will serve my purposes."
    "But the only one that I can see that won't be simply a seat of cold metal is the bonnet of the car, still warm from my revving the engine a moment ago."
    "Kleio feels herself being walked backwards into the front bumper, and begins to hastily untie the arms of her overalls so that she can then pull them down."
    hide kleio
    show kleio missionary
    with fade
    "They collect around her ankles, and she starts to pull down her panties too as she clambers up and onto the bonnet."
    "Her buttocks make the most adorable little squeaking sound as she shuffles backwards and spreads her legs in anticipation of what's to come next."
    show kleio missionary mike
    "I'm more then ready for her by the time that I have my cock out and start angling towards her."
    "Kleio is breathing heavily as she waits for me to reach her, and I can see her chest rising and falling as her heart beat ever more quickly."
    kleio.say "No need for the lube - I'm all oiled up and waiting for you..."
    show kleio missionary blush
    kleio.say "Ride me, please..."
    "I'm massively turned on by Kleio right now, but I have to admit that part of me is eager to actually fuck her before she starts making engine noises herself!"
    "But I have to admit that she wasn't kidding in the slightest when she said that she was ready for me."
    show kleio missionary vaginal pleasure -blush
    "There's almost nothing to push against as I find the lips of her pussy and feel the head of my cock sliding between them."
    "I come into Kleio in one smooth motion, hearing her moan in satisfaction as I do so."
    show kleio missionary flirt
    "She's never been this easy to please before, so ready to take me into her."
    "It's as though the combination of grease, oil and sweat has somehow proven an alchemical formula to melt her insides."
    show kleio missionary blush sweat
    "I always thought that I could see past Kleio's arrogant and spiky exterior before now, appreciate that she was different deep down at her core."
    "But if this is truly the real Kleio, the one that lies behind all the facades and defences, then she's so much more than even that!"
    show kleio missionary pleasure
    "I can't keep from pushing my head against her chest as I move in and out of her, kissing her nipples as the scent of her almost threatens to overwhelm me."
    "Before too long, I can feel my thrusts becoming more intense and desperate, and I know that I'm about to cum."
    "Whether Kleio will too, I don't know and I can't do anything to ensure, as I can already feel myself letting go."
    show kleio missionary creampie ahegao with vpunch
    "She falls back onto the bonnet as I climb up and over her, pushing as deeply into her as I can go while my climax lasts."
    with vpunch
    "We end like that, with her spread-eagled over the bonnet of the car and me laid atop her, as slick with sweat as she is herself."
    show kleio missionary flirt with vpunch
    "Kleio chuckles with delight as she holds onto me, the last ghosts of my orgasm making me twitch and push into her still."
    kleio.say "Motor maintenance one-oh-one...it's essential to keep an engine healthy by taking it for a regular run and pushing it to its limits!"
    "For my part, I can't summon the will to say anything at all."
    "But I'm now starting to think that there's something I might enjoy a ride in a little more than my car."
    $ game.room = "map"
    $ hero.gain_item(hero.flags.vehicle_in_garage)
    $ hero.flags.vehicle_in_garage = False
    $ kleio.sexperience += 1
    return

label kleio_event_05c:
    if kleio.love.max < 120:
        $ kleio.love.max = 120
    "I'm just minding my own business in the house, doing this and that without any real plan of action."
    "The truth is that I'm feeling pretty bored and frustrated without my car, effectively stuck at home until it's fixed."
    "Not that I have any reason to doubt that Kleio's up to the job of getting it done for me."
    "It's just that she promised to call me when the car was ready, but didn't tell me just when that would be."
    "Which I suppose is pretty much irrefutable proof that she's a genuine mechanic!"
    "I've already lost all track of time when I hear the loud blaring of a horn in the street outside."
    "It's more curiosity than annoyance that sends me scuttling to the window to see what's going on."
    "But it doesn't take long for me to recognise my own car in the driveway, with Kleio sitting behind the wheel."
    "Whether she sees me looking out at her or not, she still chooses to grind her palm into the horn another time."
    "Afraid of becoming public enemy number one in the eyes of the neighbours, I hurry out the front door."
    show bg house with wiperight
    "I'm sure Kleio understands what the constant waving of my hands means."
    "But all the same, she chooses to pound the horn one last time before I can make it to the car."
    "And this time she holds it down for even longer, dragging out the blaring sound for all it's worth."
    show kleio casual
    mike.say "Kleio, what the hell are you doing?!?"
    mike.say "Stop making that blasted noise!"
    "Kleio has the window wound down on the driver's side, and her arm hanging out of it."
    "As I finally reach the car, she sticks her head out too."
    kleio.say "Hey, Loverboy."
    kleio.say "I brought your shaggin' wagon back, just like I said I would!"
    kleio.say "All fixed up and better than ever."
    kleio.say "Well, as good as a bucket like this is ever gonna get..."
    "Without asking permission, I reach into the car and pull the keys out of the ignition."
    mike.say "I don't remember the horn being broken, Kleio."
    mike.say "Is there any particular reason you couldn't have just knocked at the door?"
    "Kleio gives me a withering smile as she opens the door and climbs out."
    kleio.say "You know, [hero.name], I was surprised when you showed up at the garage in this thing."
    kleio.say "But now I'm staring to see attraction it must have for you."
    "I roll my eyes at the comment, trying my best not to show how much it bothers me."
    mike.say "Ha, ha, Kleio - very funny."
    mike.say "Look, I'm really grateful that you fixed the problem."
    mike.say "What do I owe you for the work?"
    "Kleio kicks one of the tires and shakes her head dismissively."
    kleio.say "No charge, Loverboy."
    kleio.say "Working on one of these is almost too easy."
    kleio.say "Let's just call it a favour between friends, okay?"
    "I nod, more than a little taken aback at being given a freebie."
    mike.say "Sure, Kleio - if you say so."
    show kleio happy
    "Kleio smiles and then slaps me on the back pretty hard."
    kleio.say "Don't mention it, [hero.name]."
    show kleio normal
    kleio.say "I love the chance to help out a damsel in distress every now and then!"
    kleio.say "Now, I need to go drive something that's a little more manly than a hairdryer."
    kleio.say "Your car feels like it just oozes the word pussy!"
    hide kleio with fade
    "And with that, she's gone, leaving me standing in the driveway beside my painfully sensible car."
    "Part of me knows that I should be deeply insulted, desperate to redeem my manhood."
    "But another part of me is so turned on by Kleio's bad attitude right now, that I can't think of anything else..."
    $ hero.gain_item(hero.flags.vehicle_in_garage)
    $ hero.flags.vehicle_in_garage = False
    return

label kleio_event_06:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Kleio")
    if not result:
        $ hero.cancel_event()
        $ kleio.love -= 5
        return
    if kleio.love.max < 140:
        $ kleio.love.max = 140
    "It's impossible to spend even the smallest amount of time around Kleio without noticing how crazily opinionated she is."
    "No matter what the issues is, big or small alike, she's got a take on it and if you're not with her, then you're against her!"
    "Now I like to think of myself as a pretty progressive, modern kind of guy - you know?"
    "Woke might be too strong a word to describe me, but otherwise I'm generally for things that are good and against stuff that's bad."
    "But all the same, talking to Kleio about any given subject can often feel like stepping through a minefield."
    "So, I confess that most of the time, I tend to nod and smile whenever she voices an opinion on a subject."
    "More often than not, it seems to steer me clear of trouble and make for a relatively quiet life."
    "That is until today, when I get a call from Kleio that seems to come totally out of the blue."
    mike.say "Hey, Kleio - what's up?"
    kleio.say "Don't give me that shit, [hero.name]."
    kleio.say "Where in the HELL are you?!?"
    "For a moment, I can't quite wrap my head around the question."
    mike.say "Ah...not where I'm supposed to be, I'm guessing?"
    kleio.say "Yeah, well - you'd be damn right too!"
    kleio.say "The protest's been going for an hour already."
    kleio.say "And you're not here to support me!"
    mike.say "Protest...what protest?"
    "I hear Kleio make a frustrated sound on the other end of the line."
    "And I instantly know that I've said the worst possible thing."
    kleio.say "What do you mean 'what protest'?"
    kleio.say "The same damn protest you agreed to come to last week, [hero.name]!"
    "Oh shit, I must have said yes to something without even realising it!"
    "I guess this is the danger of nodding and smiling whenever Kleio asks me a question."
    mike.say "That's today?!?"
    mike.say "Oh, I'm sorry, Kleio - I thought it was next week!"
    "Kleio makes a kind of low growling noise, which doesn't sound at all good for me."
    kleio.say "Whatever, [hero.name]."
    kleio.say "Either get down here or don't."
    kleio.say "Just spare me your lame excuses, okay?"
    show bg street with fade
    "Even as Kleio ends the call, I'm already grabbing my jacket as I race to the door."
    "I have no trouble finding the protest when I get to the city centre."
    "All I have to do is follow the sound of chanting and jeering until I'm confronted by the sight of it."
    "Literally hundreds of people are milling around, holding banners and pumping their fists in the air."
    "I don't think I've ever seen so many tattoos, piercings and heads of dyed hair in one place before."
    "It's like being surrounded by an entire herd of Kleio's all at once!"
    "I cast my gaze around, searching for the one person that I'm here for the sake of pleasing."
    show kleio casual annoyed at center, dark with dissolve
    "And then I see her, standing on the edge of the crowd, obviously waiting for me."
    "Kleio had her arms crossed over her chest and taps her foot impatiently."
    hide kleio
    show kleio casual normal
    with dissolve
    "But when she sees how red-faced I am and hears me panting as I run up, her face softens a little."
    "Hands on knees and bent over double, I immediately start to apologise."
    mike.say "Sorry...Kleio..."
    mike.say "Totally...forgot..."
    kleio.say "Okay, okay!"
    kleio.say "Don't overdo it, [hero.name]."
    kleio.say "At least you're here now..."
    "And with that, she shoves a homemade sign into my hands."
    kleio.say "Come on, or this thing'll be over before we get in there!"
    "Before I can even read what's written on the sign, Kleio grabs my hand with an iron grip."
    with hpunch
    "She pulls me into the heaving crowd, showing little regard for those she elbows and jostles in the process."
    "Soon we're deep into the throng of protestors, and the noise beyond deafening."
    "I'd expected to feel hemmed in by the crowd of bodies, even scared of being crushed."
    "Instead I find it reminds me of the gigs that I've been to over the years."
    "Only it's crusty protestors all and their chants around me, rather than crusty rockers and heavy metal."
    "Kleio keeps looking back over her shoulder at me, her mouth working away."
    "But the incredible volume of the crowd means that it's impossible to hear or be heard."
    "Every time that I'm forced to resort to the old nod or shake of the head, I get a twinge of fear in my gut."
    "At first it seems to be paying off, but every time I feel the odds are being stacked more heavily against me."
    "Finally, I see Kleio talking in passionate tones to some of the protestors around us."
    "I have no idea if she actually knows them, or if they're just on the same wavelength as her."
    "Either way, she's getting an enthusiastic response from them."
    "But the only problem is that she seems to be getting nods and shakes of the head in equal measures."
    "So when she inevitably turns to me, eyes wide and appealing for an answer."
    "This is it, I can't go on fobbing her off any longer."
    "She's demanding an answer, one way or the other!"
    menu:
        "No!":
            "It's a fifty-fifty chance, right?"
            "So there's really no logic to which way I choose to leap."
            "I take a lungful of breath and bellow out my answer..."
            mike.say "FUCK NO!!!"
            $ kleio.love -= 25
            "It would have to be that same moment that the crowd chooses to go quiet."
            "And so not only does Kleio hear me clearly, so does everyone around us too."
            "The look on her face turns to shock, then outrage."
            "And I know in that instant that I made the wrong choice."
            show kleio angry
            kleio.say "What did you just say?!?"
            kleio.say "How the hell could you even think that, [hero.name]?!?"
            play sound punch_hard
            pause 0.2
            with vpunch
            "The moment that I begin trying to explain myself, Kleio punches me in the stomach."
            "Taken by complete surprise, I fold over and sink to my knees."
            show kleio angry at left with move
            "Through watering eyes, I see Kleio's back as she shoves her way through the crowd."
            hide kleio with moveoutleft
            "Most people seem to lose interest in my plight pretty quickly."
            "But there are still some disapproving comments that reach my ears as I slink away in shame."
            "All the way home I keep vowing to myself that I'll pay more attention in future..."
        "Yes!":
            "It's a fifty-fifty chance, right?"
            "So there's really no logic to which way I choose to leap."
            "I take a lungful of breath and bellow out my answer..."
            mike.say "FUCK YEAH!!!"
            "It would have to be that same moment that the crowd chooses to go quiet."
            "And so not only does Kleio hear me clearly, so does everyone around us too."
            "The look on her face changes to one of disbelief."
            "But then just as quickly to one of genuine joy."
            "And I know in that instant that I made the right choice."
            show kleio happy
            kleio.say "You got it, [hero.name] - FUCK YEAH!!!"
            "First one, then two, and pretty soon most of the protestors around us begin to join in too."
            "In fact, the new chant spreads so far and so fast that soon the whole crowd is following our lead."
            "Kleio and I find ourselves unceremoniously hauled onto the shoulders of a couple of burly guys."
            "They smell pretty bad, but I can't help being carried along with the spirit of the moment."
            show kleio at center, zoomAt(1.5, (640, 1040))
            with hpunch
            "Kleio leans in close and punches me on the shoulder."
            "Taken by complete surprise, I yelp in alarm and not a little pain."
            "But then I see the look of sheer happiness on her face, and I find myself smiling too."
            "Kleio takes firm hold of my hand, as if she's not going to let herself be parted from me."
            "And so with a huge, stupid grin plastered across my face, I gaze at her happily too."
    return

label kleio_event_06b:
    if kleio.love.max < 140:
        $ kleio.love.max = 140
    "It's one of those days when Kleio and I are just hanging out together, not doing anything in particular."
    "It's not quite a date, but at the same time it's definitely more than a couple of friends just being together."
    "Truth be told, these are some of the best times that I've had with Kleio since we officially became an item."
    "There's no pressure on either of us, and we have the space to be ourselves and let it all hang out."
    "But of course that doesn't mean Kleio stops being Kleio..."
    mike.say "Mmm..."
    mike.say "I'm gonna get a snack, Kleio."
    mike.say "You want me to grab you something too?"
    show kleio annoyed at center, vshake
    "Kleio scoffs at this and shakes her head."
    kleio.say "Jesus wept, Loverboy!"
    kleio.say "You just ate like a half hour ago."
    kleio.say "Have you got a damn tape-worm?"
    kleio.say "Or are you TRYING to get fat on me?"
    "Kleio's comment stops me dead in my tracks."
    "I hadn't spared a second thought about when I last ate something."
    "All I did was get the impulse to eat and decide to act on it."
    "But now Kleio's gone and made me feel like a compulsive eater!"
    "I blink at her for a moment, not sure of what to say in response."
    "It's only then that I remember who it is I'm talking to."
    "And I burst out laughing."
    mike.say "Yeah, Kleio..."
    mike.say "You're probably right!"
    mike.say "Forget about the snack."
    "I'm expecting Kleio to gloat at making me agree with her."
    "Or at least to throw another insult or two in my direction."
    show kleio normal
    "But instead she catches me off-guard by frowning."
    kleio.say "How do you DO that, [hero.name]?"
    mike.say "Do what, Kleio?"
    kleio.say "That thing where I attack you."
    kleio.say "And then you just shrug it off like nothing happened!"
    "I look at Kleio blankly for a moment, not knowing what to say."
    "I mean, the answer is so fundamental and obvious."
    "I have to make a conscious effort to put it into actual words."
    mike.say "Because that's the way you are, Kleio."
    mike.say "And I love every part of you - even the insults."
    mike.say "I know that they're just your way of communicating."
    mike.say "So they kind of don't bother me anymore."
    "Kleio makes kind of a huffing noise."
    "She shakes her head and sighs."
    kleio.say "It kind of takes the edge off of it, you know?"
    kleio.say "Urgh...and to think..."
    kleio.say "I was always scared of winding up with a guy like my old man!"
    "My ears prick up at this."
    show kleio annoyed
    "And that's because Kleio almost never talks about her parents."
    "Hell, she doesn't talk much about her past either."
    "Not before she met Sasha and they formed the band together."
    mike.say "So..."
    mike.say "I'm NOT like your dad."
    mike.say "And that's a...good thing?"
    kleio.say "You bet your fucking life it's a good thing, Loverboy!"
    show kleio angry
    kleio.say "My old man was the biggest fucking asshole on the planet!"
    kleio.say "He beat my mom black and blue."
    kleio.say "Then, when she left, he did the same to me..."
    show kleio annoyed
    "Kleio trails off as she realises what she's admitting to."
    "That her emotions have made her open up without realising it."
    show kleio sad
    kleio.say "Ah fuck..."
    kleio.say "I went and broke my number one rule!"
    kleio.say "I went and told you my pathetic sob story!"
    "I shake my head at this."
    "Part of me can't believe what Kleio is saying."
    mike.say "Don't say that, Kleio!"
    mike.say "Nobody has a right to abuse you like that."
    mike.say "And you don't have to hide it from me either."
    mike.say "I...I have no idea what that feels like."
    mike.say "And I'm not going to say that I understand, because I don't."
    mike.say "But I'll be here for you if you want to talk...or not, okay?"
    show kleio normal
    "Kleio lands a playful punch on my shoulder."
    show kleio at center, zoomAt(1.5, (640, 1040))
    "But it has no force to it, and she leans into me afterwards."
    kleio.say "Fuck me, Loverboy."
    kleio.say "I don't deserve you!"
    "I wrap my arms around Kleio, pulling her closer."
    mike.say "Yes you do, Kleio."
    mike.say "And anyway..."
    mike.say "I always thought your number one rule was to never go ten seconds without saying 'fuck'?"
    show kleio happy
    "Kleio sniggers into my shoulder at this."
    "And then she wraps her arms around me too."
    return

label kleio_getting_serious_01:
    show bg street
    show kleio c seductive
    "Almost as soon as we're out of the place and starting to walk down the street, Kleio looks back over her shoulder at me."
    "She's walking a couple of paces ahead, and the expression on her face seems to be one of pure, unbridled mischief."
    "I'm not troubled by this in the slightest, as the date went well - very well indeed."
    "And as Kleio's fondness for being outrageous and pushing my buttons just serves to make me that much more into her right now."
    mike.say "And just what the hell is that look supposed to mean, huh?"
    show kleio annoyed
    "Kleio raises her eyebrows and opens her mouth in mock outrage at my question."
    kleio.say "You really want to know, Loverboy?"
    mike.say "Yeah, Kleio - I really want to know!"
    kleio.say "Okay, if you insist..."
    show kleio happy
    kleio.say "I was just thinking that you're not half as lame as you look!"
    "Now it's my turn to put on a look of pretend outrage."
    "I've been around Kleio long enough to know when she's serious with her venom."
    "But I can also tell when she's putting it on for the sake of getting a reaction."
    "I guess it's kind of like her own special way of flirting, you know?"
    "And the worst thing that you can do in a situation like this is to back down for even a moment."
    mike.say "Yeah, well, Kleio."
    mike.say "That just shows how poor a judge of character you really are!"
    show kleio angry
    "Kleio's eyes go wide at my retort, but I see her smile twist in just such a way."
    "And the look that she gives me lets me know that she's enjoying this immensely."
    kleio.say "It's not my fault I've got such poor material to work with, Loverboy!"
    show kleio happy
    kleio.say "Anyway, this was fun."
    kleio.say "So I think you've just about earned the chance to do it again some time."
    "And with that, Kleio goes to turn her back on me and stroll off down the street."
    show kleio at left4 with move
    pause 1
    show kleio surprised at center, zoomAt(1.5, (640, 1040)), hshake
    "But she only makes it a few inches before she's stopped in her tracks."
    show kleio a surprised
    "Kleio looks back and down, seeing my hand holding her wrist, keeping her from leaving."
    show kleio normal
    "Her gaze travels upwards until she's looking me straight in the eye."
    "Then she cocks her head on one side, issuing what I know is a challenge."
    "She's letting me know that, whatever I do next, it had better be good."
    mike.say "Thing is, Kleio..."
    mike.say "I think I did better than you give me credit for."
    mike.say "I think things went well enough tonight for me to deserve more."
    show kleio seductive
    kleio.say "Oh, yeah?"
    kleio.say "That's what you think, is it, Loverboy?!?"
    mike.say "Yeah, Kleio, it is."
    mike.say "So you have two choices."
    mike.say "Either kiss me or slap me in the face."
    mike.say "Because I'm not letting go until you do one of them."
    show kleio at center, zoomAt(1.65, (640, 1540))
    with vpunch
    "I pull Kleio towards me, finding that there's little resistance to my doing so."
    "As the distance between us disappears, I half expect to feel her hand on my cheek any moment."
    "But by the time she's close enough for me to pull her into an embrace, I know that it's not coming."
    kleio.say "You've sure got some balls on you, Loverboy!"
    mike.say "No more than you, Kleio!"
    kleio.say "Ah, shut up and kiss me, you ass!"
    hide kleio
    show kleio kiss
    with fade
    $ kleio.flags.kiss += 1
    "And so that's just what I do, leaning down to place my lips against her own."
    "For all of her bravado, Kleio kisses me in a sensual and tender way."
    "Her tongue teasing me and the sound of her breath betraying just how much she's laying herself open in that moment."
    "What's happening right now?"
    "Are we becoming something more than a pair of sarcastic wankers that trade insults as much as we turn each other on?"
    "Whatever it is, all I know is that I like it."
    "And I think that Kleio does too..."
    hide kleio kiss
    if kleio.love.max < 150:
        $ kleio.love.max = 150
    return

label kleio_event_07:
    if kleio.love.max < 160:
        $ kleio.love.max = 160
    show kleio
    "I've only recently begun to notice it, but there's definitely something odd going on with Kleio right now."
    "Okay, I know she's not exactly the most normal of girls to begin with, being so spikey and all that."
    "But even so, I can see that there's something up that's been going on for a couple of days."
    "Normally, any amount of time that I spend with Kleio means weathering a certain amount of her characteristic insults."
    "To be honest though, that's something that I've pretty much gotten used to by now."
    "In fact, it's starting to become one of those little quirks that I really like about her."
    "So when she seems to stop being able to reel them off at me, that's the thing that starts to make me worry."
    "It's almost like Kleio sees the opportunity to stick one in there, but then shies away at the very last moment."
    "I have no idea what's behind it, and I'm getting more concerned for her every time it happens."
    "So much so, that I eventually feel that I have no choice but to bring it up with her."
    mike.say "Kleio..."
    kleio.say "Hmm?"
    mike.say "Is something bugging you?"
    kleio.say "You what, Loverboy?"
    mike.say "I mean it, Kleio - what's up with you?"
    show kleio annoyed
    kleio.say "I don't know, [hero.name]."
    show kleio angry
    kleio.say "Maybe I'm pissed off with being asked questions by a..."
    kleio.say "By a..."
    kleio.say "Urrgh!"
    show kleio annoyed
    "There she goes again - starting an insult and not being able to finish it."
    show kleio normal
    mike.say "This is what I mean, Kleio."
    mike.say "You keep getting tongue-tied around me."
    "I take a deep breath before I go ahead and say what's on my mind."
    mike.say "Is it me, Kleio?"
    mike.say "Have I done something to hack you off?"
    "Obviously I'm worried that the answer is going to be a resounding yes."
    "That and just what the fallout will be if I'm right."
    show kleio annoyed
    "Kleio looks away, as if refusing to meet my eye."
    "And that makes me think that I was right, that she's going to dump me or something."
    mike.say "If it's me, then just say so."
    mike.say "I can change, Kleio."
    mike.say "I promise you that!"
    show kleio surprised
    kleio.say "No, [hero.name] - don't ever do that!"
    show kleio annoyed blush
    "Kleio falls silent as soon as the words have left her lips."
    "She seems almost shocked into silence by her sudden outburst."
    mike.say "What...what do you mean, Kleio?"
    mike.say "Won't me changing help make it better?"
    show kleio normal
    "Kleio forces herself to turn her head and look at me."
    "And I can see the effort that it's taking for her to do so."
    kleio.say "No, no..."
    kleio.say "I mean...I don't want you to change, [hero.name]."
    kleio.say "I...I like you just as you are!"
    show kleio angry
    kleio.say "There, I said it, okay?!?"
    show kleio annoyed
    "For a moment, I'm just as stunned as Kleio seemed to be."
    "I'm so unused to her talking in this way, I don't know how to react."
    "But then I begin to realise how hard it must have been for her to make a confession like that."
    "Kleio's tough exterior is such a part of her, admitting to her feelings can't be easy."
    mike.say "I...I like you too, Kleio."
    mike.say "And I kind of like the way you blister me too..."
    show kleio surprised
    kleio.say "You...you do?!?"
    "I nod and smile, enjoying the novelty of having Kleio be so honest and open about her feelings."
    mike.say "Yeah, I do."
    mike.say "I always sort of figured that it meant you liked me!"
    show kleio normal
    kleio.say "That's why it's been hard to do it, [hero.name]."
    show kleio happy
    kleio.say "It's getting hard to think of things I hate about you anymore!"
    mike.say "Don't worry - I'm sure I can come up with something new to bug you with!"
    show kleio seductive
    "Kleio's expression turns to one of amused outrage, and she punches me gently on the arm."
    show kleio happy at center, zoomAt(1.5, (640, 1040))
    "But then she leans in closer, resting her head on the same shoulder."
    "I pull her into a hug, thinking all the while of how unique and special this girl is to me..."
    return

label kleio_getting_serious_02:
    show bg street
    show kleio
    "I can remember someone trying to give me advice about relationships, telling me it's only as good as your last date."
    "But if that really is the case, then I guess Kleio and I are doing pretty well on that count."
    "We just had one of those dates where everything seems to fall into place."
    "The kind where the two of you just click, and it feels like it was meant to be, you know?"
    "And yes, I know that this is Kleio I'm talking about, the queen of quirk."
    "But lately, we've been spending more time than ever in each other's company."
    "And things have been steadily getting more serious between us too."
    "Where Kleio's abrasive character and acid tongue once bugged me, I now feel like I've been let in on the joke."
    "All of the ways in which she used to rub me up the wrong way are fast becoming things I actually adore about her."
    "They're the kind of things that you want to change about someone when you first get involved with them."
    "But after time passes, they become the elements of their character that you wouldn't miss for the world."
    "And again, I know you're going to find that hard to believe - but it's the truth."
    "All of this is going around in my mind as we walk home from our date."
    "Kleio holding my hand as we go, but I can feel that she's trying to make me slow my pace."
    "I guess that she wants me to stop for some reason, and it's this that give me a sudden sense of Déjà vu."
    "Didn't this same thing happen before, only with me tugging Kleio back as we walked home after a date?"
    "I feel a twinge of wicked amusement at the fact the roles have been reversed."
    "Who would have thought that we'd get to the point where it was Kleio appealing for my attention?"
    "And wouldn't it be ironic to turn the tables on her?"
    "I keep on walking, pretending to ignore Kleio's efforts to make me stop."
    kleio.say "Hey...hey, Loverboy!"
    kleio.say "Slow down already!"
    mike.say "Oh, sorry, Kleio."
    mike.say "I guess I was too lame to hear you the first time, huh?"
    show kleio angry
    "I see Kleio's eyes widen and her mouth open in an expression of playful outrage."
    kleio.say "Bravo, [hero.name]."
    kleio.say "Way to throw my own words back at me!"
    show kleio annoyed
    "Now that I'm forced her to admit that she was pretty mean to me that last time, I can let her have her way."
    show kleio at center, zoomAt(1.5, (640, 1040))
    "I turn and allow Kleio to pull me into a tight embrace, enjoying the sensation of her body as it's pressed against me."
    mike.say "You're sarcastic most of the time, Kleio."
    mike.say "So how am I supposed to know when you're actually being serious?"
    show kleio normal
    kleio.say "I'm being serious right now, [hero.name]."
    kleio.say "Tonight was fun...really fun."
    show kleio blush
    kleio.say "I just wanna hug, to make that feeling last a little longer, you know?"
    "Are my ears deceiving me?"
    "Did I just hear Kleio getting sentimental on me?"
    "She sounds almost like she's going all soft and fluffy!"
    "I could come out with any number of smartass comments, try to score a couple of points over her."
    "But that just feels like it'd make me the biggest jerk on the face of the planet right now."
    mike.say "Me too, Kleio."
    mike.say "Me too."
    "So I do nothing more than hold her."
    "And the odd thing is, that while I do, I feel so happy it's unreal."
    "There's nothing to be said, no jokes to be made or points to be scored off of each other."
    "There's only Kleio and me, sharing a moment together."
    "Neither of us wanting it to end..."
    $ kleio.set_girlfriend()
    if kleio.love.max < 170:
        $ kleio.love.max = 170
    return

label kleio_event_07_1:
    if kleio.love.max < 180:
        $ kleio.love.max = 180
    "It's a pretty nice day out, clear skies and even a little bit of sunshine thrown in for good measure."
    "On a day like this I often take the chance to get out of the house and take a walk somewhere relaxing."
    "But one thing that I don't usually do is take Kleio along with me."
    "Let's just say that she's not the type that likes long, romantic walks in the countryside!"
    "But by some minor miracle, I've actually talked her into a quick stroll around the park."
    "Probably because I promised to take her straight to the pub when we're done!"
    "At least we can sit outside in the beer garden when we get there."
    "That way we'll still be making the most of the fine weather."
    "But it does mean that I have to put most of my effort into entertaining Kleio."
    "Because she's not the kind of girl that's happy to just take in the scenery!"
    show kleio casual annoyed
    kleio.say "Isn't this the park where they busted a bunch of smackheads?"
    show kleio normal
    kleio.say "You know, I swear it is."
    show kleio annoyed
    kleio.say "I remember seeing this place on the news!"
    show kleio normal
    mike.say "Ah..."
    mike.say "I wouldn't know anything about that, Kleio!"
    mike.say "I just come here to get some exercise, you know?"
    mike.say "Maybe to feed the ducks too?"
    "Kleio doesn't seem to pick up on my hints to drop it."
    "Nor the idea that we should be enjoying the chance to be surrounded by nature."
    "Instead she seems more interested in noting all the negative things about the park."
    kleio.say "And those things that look like bins..."
    kleio.say "Like that one over there - what are those for?"
    mike.say "Erm..."
    mike.say "Those are for putting your dog's...waste into."
    show kleio angry
    kleio.say "Urgh...like dog shit?!?"
    show kleio annoyed
    mike.say "Yeah, Kleio."
    mike.say "But you put it in a bag first!"
    kleio.say "What, like the ones hanging from that tree over there?"
    mike.say "Yeah, I suppose so..."
    mike.say "That's a Crab Apple tree, by the way."
    kleio.say "Huh...crap apple tree, more like!"
    show kleio normal
    "I can't help sniggering at Kleio's snide comment."
    "But that's one of the reasons I love her!"
    "We walk on, as I'm determined to make at least one loop around the park."
    "Kleio continues to find fault with everything that I show her."
    "And I'm kind of accepting that this is going to be the way it goes."
    "That is until I see a familiar figure coming from the opposite direction."
    mike.say "Oh shit!"
    show kleio surprised
    kleio.say "What's up, Loverboy?"
    show kleio happy
    kleio.say "Did you step in something?"
    show kleio normal
    mike.say "No, Kleio..."
    mike.say "You see that woman over there?"
    kleio.say "Huh?"
    kleio.say "You mean the frump with the huge rack?"
    kleio.say "Jesus Christ - don't tell me you've fucked that?!?"
    mike.say "No, Kleio!"
    mike.say "That's my mom!"
    show kleio close surprised
    "Kleio actually does a double-take at this."
    kleio.say "NO WAY, Loverboy!"
    kleio.say "You came out of that?!?"
    hide kleio
    show kleio surprised
    "But I'm already starting to walk the other way."
    kleio.say "Hey, wait a minute!"
    kleio.say "Where are you going?"
    mike.say "Where do you think, Kleio?"
    mike.say "Somewhere she won't see us!"
    show kleio seductive
    kleio.say "Nah, fuck that."
    kleio.say "I wanna meet her for myself."
    show kleio surprised
    kleio.say "HEY THERE!"
    kleio.say "HEY...[hero.name]'S MOM!"
    show kleio seductive
    "Before I can stop her, Kleio's yelling as she walks towards my mom."
    "Of course it doesn't take long for her to be heard and for my mom to zero in on us."
    "After all, Kleio has a hell of a big mouth on her!"
    show kleio at left with move
    show angela casual at right with moveinright
    angela.say "Oh..."
    angela.say "Hello there!"
    angela.say "Who might you be?"
    kleio.say "I might be Kleio."
    kleio.say "And I might be your son's fuck-buddy!"
    show angela surprised
    "I hear the words leave Kleio's mouth almost in slow-motion."
    "Like one of those scenes in a movie where they slow down a gun-shot."
    "Because the look on my mom's face is pretty much the same as someone taking a bullet."
    angela.say "Y...you mean his girlfriend...surely?"
    kleio.say "You could call me that, yeah."
    kleio.say "But we're buddies that fuck a lot too."
    kleio.say "So fuck-buddy definitely applies."
    mike.say "H...hey, mom!"
    mike.say "I see Kleio already introduced herself!"
    show angela protest
    angela.say "There you are, dear!"
    angela.say "Yes...she most certainly did!"
    "Kleio gives me a sickly grin."
    "She's clearly enjoying the chance to create some drama."
    show angela annoyed
    angela.say "She tells me she's your...partner?"
    mike.say "That's right, mom."
    mike.say "Kleio and I have been dating for a while now."
    show angela frustrated
    angela.say "Hmm..."
    angela.say "Strange that you never mentioned her before now!"
    "Oh shit - looks like my mom's up for a fight!"
    "And that's not a good thing, believe me."
    "I know Kleio's capable of being as big of a bitch as they come."
    "But my mom can go with the best of them."
    "And she's got years more experience too!"
    kleio.say "Yeah well..."
    kleio.say "I tend to keep his tongue pretty busy down here!"
    "Kleio points to her crotch with both hands."
    show kleio happy
    "Grinning at my mom as she does so."
    show angela sadistic at right5 with move
    angela.say "Oh my, those are some pretty pictures on your tummy, my dear."
    angela.say "Did you draw them on yourself with a marker pen?"
    show kleio angry at vshake
    kleio.say "WHAT?!?"
    kleio.say "At least I didn't have my chest blown up with a foot-pump!"
    show angela happy
    "Mom laughs and waves Kleio's words away like they're nothing."
    angela.say "You have to have something up top before that can happen."
    show angela sadistic
    angela.say "Tell me, Kleio - do you often get mistaken for a boy?"
    show kleio at vshake
    pause 1
    show kleio at left5 with move
    kleio.say "Wha...the...what did you say?!?"
    show kleio at vshake
    "I just about manage to get hold of Kleio before she launches herself at my mom."
    show kleio at left with move
    "And I have a manic smile on my face as I drag her away down the path."
    mike.say "Ah...okay, mom!"
    mike.say "It was great seeing you!"
    mike.say "Come on, Kleio - let's get you to the pub!"
    show angela annoyed
    "My mom chuckles at the sight of me having to restrain Kleio."
    angela.say "See you later, dear."
    show angela normal
    angela.say "And don't worry, Kleio - [hero.name] always went through phases as a boy."
    show angela sadistic
    angela.say "You're probably just another one of those!"
    "Kleio lets out a snarl of rage."
    show kleio d
    "And she thrusts a middle finger in my mom's direction."
    kleio.say "Screw you, you old hag!"
    kleio.say "I'll make you pay, you'll see!"
    kleio.say "How about I marry your precious son, huh?"
    kleio.say "Then we live happily ever after with a ton of brats?"
    kleio.say "You'll have to spend every holiday with me until the day you die!"
    return

label kleio_event_08:
    scene bg pub at dark
    if kleio.love.max < 190:
        $ kleio.love.max = 190
    "It doesn't matter how hard I try, I'm just so hyped tonight that I can't keep a stupid grin off of my face."
    "It's stuck there the whole time that we're standing in the queue and showing our tickets to get into the venue."
    show kleio annoyed at center, zoomAt(1.5, (640, 1040))
    "And every time Kleio looks sideways at me, she shakes her head and rolls her eyes, snorting in a derisive manner."
    show kleio normal
    "But even so, I can tell that she's more amused than annoyed."
    "That and the fact that she's pretty excited too."
    "She's just better at hiding it, that's all."
    show kleio happy
    kleio.say "Geez, Loverboy!"
    show kleio annoyed
    kleio.say "Are you gonna be grinning like a fool all night?"
    mike.say "Was I doing that, Kleio?"
    mike.say "Sorry, I must still be buzzing that I got us tickets for the gig."
    mike.say "But not just any gig - a Metallikea gig!"
    show kleio normal
    kleio.say "Okay, okay - I get it!"
    kleio.say "And I'm grateful, really I am."
    kleio.say "Just stop milking it, yeah?"
    "I nod hastily, not wanting to spoil the mood."
    "Also, it's probably better to let Kleio go on thinking that I was just lucky to score the tickets."
    "Rather than have her dig too deeply into what I had to do to get them."
    "I already have a massive phone bill from all the hours spent on hold with the ticket hotline."
    "And then there's the huge hole in my bank account from where the scalper I bought them from gutted me!"
    "But it's all worth it, just to know that Kleio's grateful and having a good time."
    "A moment later I'm shaken out of my reverie as she grabs me firmly by the wrist."
    mike.say "Whoa, Kleio!"
    mike.say "What's going on?!?"
    kleio.say "Come on, Loverboy."
    show kleio happy
    kleio.say "It's starting!"
    with hpunch
    show layer master at lparty
    play music "music/TeknoAXE/simple_metal.ogg" loop fadeout .5 fadein .5
    "And with that, I find myself being dragged bodily into the already thronging crowd."
    "But Kleio doesn't stop there."
    "Instead she pushes her way ever deeper into the press of bodies."
    with hpunch
    "Before I know it, I'm getting hit from every imaginable angle."
    "I take elbows to the gut and groin."
    with hpunch
    "I stumble and almost fall as my feet are stamped on."
    "More than once, someone actually manages to headbutt me too!"
    "But through all of this, I somehow keep a hold of Kleio's hand."
    "When she finally seems to be satisfied with where we are, she stops pulling along."
    "And when my vision returns to something like normal, all I can do is admit that I'm impressed."
    "She's fought her way to a spot where we have a pretty sweet view of the stage."
    "The fact that it's nowhere near the already violent mosh-pit is a relief too!"
    "What follows is a blur of screeching vocals, sawing chords and thumping tunes."
    "I can't recall individual moments, and the songs all merge into one."
    "But it's a gig that I'll never forget."
    "And that's thanks to the thrill it inspires in me."
    "That and the buzz it leaves me with afterwards."
    "When the final encore is over, Kleio grabs me by the wrist again."
    scene bg pub at dark
    show kleio happy
    show fx exclamation
    play music "music/roa_music/horizon.ogg" loop fadeout .5 fadein .5
    kleio.say "[hero.name]..."
    kleio.say "That was AMAZING!"
    mike.say "You don't have to tell me, Kleio."
    mike.say "I was there too!"
    show kleio normal
    kleio.say "I didn't think they could ever replace Clint Thompson."
    mike.say "I know what you mean."
    mike.say "But that new bassist, she's damn good."
    show kleio seductive
    kleio.say "And really hot, too!"
    menu:
        "Be cool":
            mike.say "Erm, yeah, Kleio - I do have eyes of my own!"
            mike.say "How could I miss a babe like that?!?"
            mike.say "Every guy and girl in the place must have been thinking the same thing too."
            show kleio normal
            "Kleio looks at me sideways, on odd expression on her face."
            show fx exclamation
            kleio.say "Really, [hero.name]?"
            show kleio blush
            kleio.say "And you...you don't have a problem with that?"
            "I screw my face up into a puzzled expression at this."
            mike.say "Why would I have a problem with that, Kleio?"
            mike.say "We're both adults - we can admit we find other people attractive, can't we?"
            kleio.say "I know, I know..."
            show kleio annoyed
            kleio.say "It's just that...well..."
            kleio.say "Some men really have a problem with me liking girls as well as guys, yeah?"
            "I shrug at this, not knowing what to say other than the truth."
            mike.say "Well, I'm not one of those guys, Kleio."
            show kleio normal
            mike.say "I know that you dated girls before we got together."
            mike.say "And I'm cool with that."
            mike.say "The only thing I don't want you to do is stop liking me!"
            "Kleio's silent for a prolonged moment, holding my eye the whole time."
            show kleio kiss
            $ kleio.flags.kiss += 1
            "And then, out of nowhere, she pulls me in and plants a kiss on my lips."
            "Once the surprise has passed, I return it with enthusiasm."
            show kleio seductive blush at center, zoomAt(1.5, (640, 1040))
            "Afterwards I shake my head at Kleio."
            mike.say "Ah, Kleio..."
            show kleio happy
            mike.say "What was that for?"
            kleio.say "It was for being you, [hero.name]."
            show kleio seductive
            kleio.say "Just for being you."
            "I shake my head again."
            "Not fully getting what she means, but happy that she's happy."
            if game.active_date and date_girl == kleio:
                $ game.active_date.score = 85
        "Be jealous":
            mike.say "Y...you really think so?"
            mike.say "I hadn't noticed..."
            "Kleio fixes me with a sideways, sceptical look."
            show kleio normal
            kleio.say "Oh, come on, [hero.name]!"
            kleio.say "Who are you trying to kid?"
            "I'm about to open my mouth and deny it for a second time."
            "But Kleio's expression undergoes a subtle change."
            "She nods, as if she's just figured something out."
            kleio.say "Are you jealous?"
            mike.say "What?!?"
            mike.say "No...don't be ridiculous."
            show kleio surprised
            kleio.say "Oh my god - you ARE jealous!"
            $ kleio.love -= 5
            show kleio happy
            kleio.say "Is it because she's a woman?"
            show kleio annoyed
            kleio.say "Or just because you're insecure, huh?"
            kleio.say "I mean, the first one is pretty lame."
            kleio.say "But the second one is not cool at all!"
            mike.say "It's neither - because I'm not jealous!"
            kleio.say "You're raising your voice like you're jealous."
            mike.say "Kleio, please."
            mike.say "If I'm raising my voice, it's because I'm being accused of something I'm not!"
            "Kleio narrows her eyes at me, clearly not convinced by my protestations of innocence."
            show kleio normal
            kleio.say "Whatever, [hero.name]."
            kleio.say "But once you cool down, we're going to have a serious chat about this."
            "I take this as my warning that the matter is closed and I should shut up."
            "But I can't help sulking for the rest of the night."
            "Which adds a sour tone to the whole evening that I just can't shake off."
    $ game.pass_time(4)
    $ game.flags.kleiocall = TemporaryFlag(True, 1)
    return

label kleio_event_09:
    $ renpy.play("sd/cell_vibrate.ogg", "sound")
    $ result = renpy.call_screen("smartphone_choice")
    if not result:
        $ hero.cancel_event()
        return
    if kleio.love.max < 200:
        $ kleio.love.max = 200
    "You ever have one of those moments in your life where everything is proceeding as normal, nothing's amiss."
    "And then you get blindsided by something that takes you completely by surprise?"
    "Yeah, well - that's me right now, as my phone begins to ring and I innocently pick it up to answer."
    "There's no caller ID and I don't recognise the number."
    "Though I do note it's a land line with a local dialling code."
    "That makes it a little unusual, and as a result, I almost ignore it completely."
    "I figure that whoever it is will either leave a message, or else they're not worth my time."
    "But then something makes me change my mind and answer the call anyway."
    "I can't explain it, other than a gut feeling that I should probably pick up."
    mike.say "Hello?"
    mike.say "Who is this?"
    kleio.say "[hero.name], am I ever glad to hear your voice!"
    kleio.say "Whatever you do, don't hang up!"
    "I don't know what's more of a shock."
    "Discovering that the call is from Kleio."
    "Or hearing the barely suppressed panic in her voice."
    mike.say "Jesus, Kleio - what's wrong?"
    mike.say "Are you okay?"
    "I can almost hear Kleio trying to pull herself together on the other end of the line."
    "It's as if just hearing my voice is enough to give her the strength to do so."
    kleio.say "I...I'm fine, [hero.name]."
    kleio.say "I just need some help, that's all."
    kleio.say "I'm in a...a bit of a mess, you know?"
    "I take a deep breath, preparing myself for what's coming next."
    mike.say "Where are you, Kleio?"
    kleio.say "Okay, just promise not to freak out, yeah?"
    mike.say "Oh shit, Kleio - where are you?!?"
    kleio.say "I'm at the police station, okay!"
    with vpunch
    mike.say "THE POLICE STATION?!?"
    mike.say "Kleio, did you get attacked or something?!?"
    kleio.say "No...No..."
    kleio.say "Nothing like that!"
    mike.say "Then what..."
    kleio.say "I got arrested..."
    kleio.say "At the protest..."
    "Now it all starts to make some kind of sense."
    "I remember Kleio mentioning that she was attending a demo of some kind today."
    "But she's always going to one or another protest, and so it didn't seem like a big deal."
    mike.say "How on earth did you manage that?"
    kleio.say "It was totally police brutality!"
    kleio.say "They started pushing and shoving us!"
    mike.say "Okay, Kleio - spare me the gruesome details."
    mike.say "I guess this is your one phone call?"
    kleio.say "Yeah, [hero.name] - I couldn't think of anyone else to turn to!"
    kleio.say "They're saying that I gotta make bail."
    kleio.say "If not, I have to spend the night in the cells!"
    "I can't believe what I'm hearing."
    "It's like being in some cliched movie!"
    menu:
        "Bail Kleio out":
            mike.say "Stay right there, Kleio."
            mike.say "I'm on my way!"
            "Without even letting Kleio reply, I'm headed out the door."
            scene bg black with dissolve
            scene bg policestation with dissolve
            "When I arrive at the police station, I rush inside."
            "My credit card is already in my hand before I say a word to the officer on the desk."
            show kleio normal casual at right with moveinright
            "As soon as Kleio is released, I rush over to her."
            show kleio at center with move
            kleio.say "Hey there, Loverboy!"
            kleio.say "How much do I owe you for bailing me out?"
            mike.say "Don't worry about that, Kleio - it's only money."
            mike.say "Tell me you're okay?"
            mike.say "Did any of them touch you?"
            mike.say "If they as much as laid a finger on you..."
            "Looking more than a little flustered at my tirade, Kleio puts her hands on my chest."
            "She shakes her head, trying to keep me from glaring at the cops that I see walking past us."
            kleio.say "Whoa, Loverboy, whoa there!"
            kleio.say "No one did anything, and I'm fine, okay?"
            "I nod, still not feeling completely convinced despite Kleio's protestations."
            mike.say "Okay, Kleio, if you say so."
            mike.say "But this is the last time you go to one of those protests alone!"
            "At this, Kleio pulls back a little way."
            "Her face twists into a puzzled expression."
            show kleio annoyed
            kleio.say "Are...are you banning me from going to protests?!?"
            "I shake my head vigorously."
            mike.say "Hell no, Kleio."
            mike.say "I'm coming with you from now on!"
            mike.say "When is there a protest against police brutality?!?"
            show kleio normal
            "Kleio cocks her head on one side, looking at me strangely."
            kleio.say "Seriously, [hero.name]."
            kleio.say "Thanks for coming to my rescue."
            kleio.say "It means a lot to know that you've got my back."
            mike.say "Any time, Kleio."
            show kleio blush at center, zoomAt(1.5, (640, 1040))
            "In an unusual show of emotion, Kleio wraps her arm in mine and leans her head against my shoulder."
            "And together we walk out of the Police Station without looking back."
            $ game.pass_time(1)
        "Don't bail Kleio out":
            mike.say "Just how much is this going to cost me, Kleio?"
            "There's a pause on the other end of the line."
            "As if Kleio's surprised to hear me ask such a question."
            mike.say "How much, Kleio?!?"
            kleio.say "Ah..."
            kleio.say "Well...a couple of hundred bucks..."
            mike.say "That's a lot of money, Kleio!"
            mike.say "What am I - a fucking ATM?"
            kleio.say "Of...of course not!"
            kleio.say "I just figured that..."
            "I cut Kleio off before she can say anything more."
            mike.say "You know what, Kleio."
            mike.say "Maybe you could use a night in the cells."
            mike.say "That way you can think about what landed you there!"
            kleio.say "What?!?"
            kleio.say "[hero.name] - why are you being like this?!?"
            mike.say "Because you're a big girl, Kleio."
            mike.say "And you need to start owning your own mistakes!"
            kleio.say "[hero.name], please..."
            "I hang up before she can make me think about changing my mind."
            "Sure, it's harsh, and she'll hate me for a little while."
            "But I really think Kleio needs to learn a lesson from this."
            $ kleio.love -= 30
    $ game.flags.kleiocall = TemporaryFlag(True, 7)
    return

label kleio_event_10:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Kleio")
    if not result:
        $ hero.cancel_event()
        $ kleio.love -= 5
        return
    "My phone rings and I answer it without even thinking, hardly noticing that the call's from Kleio."
    kleio.say "Hey, Loverboy - what are you doing right now?"
    mike.say "Ah, Kleio..."
    mike.say "Nothing, I guess!"
    kleio.say "Great, then you can come meet me some place special."
    mike.say "Where would that be?"
    kleio.say "The place we had our first date."
    kleio.say "You remember where that was, right?"
    mike.say "Of course I do, Kleio."
    mike.say "But why there?"
    kleio.say "Erm...no reason at all."
    kleio.say "Just be there as soon as you can, okay?"
    mike.say "Okay, okay..."
    "And that's where she ends the call."
    "Leaving me confused, but still rushing to do as she says!"
    return

label kleio_event_11:
    scene bg rooftop
    show kleio happy
    "I think that I've known Kleio long enough to be aware of her quirks, spent enough time with her to know her habits."
    "And that means that I can easily tell when there's something up with her, that something's not quite right in her mood."
    "This is one of those times, when she's trying the best she can to act normal, but she's just not being herself."
    "Sure, she's laughing at my jokes and agreeing with most of the stuff I'm saying to her."
    "But that's one of the things that's tipping me off to there being something wrong."
    "The Kleio I know is never this agreeable and eager to agree with my opinion on anything."
    "She'd normally have peppered the conversation with more than half a dozen cutting remarks by now too!"
    "If it were almost any other girl, I would just come right out and ask her what was up."
    "But this is Kleio, and she's more...complicated than that."
    "So I feel that I have to come at this from another angle."
    mike.say "You know what I think, Kleio?"
    show kleio normal
    kleio.say "What's that, [hero.name]?"
    mike.say "I think there was a lot of sense to how things were back in the day."
    mike.say "What with men being in charge and women staying at home to keep house."
    kleio.say "Yeah, yeah..."
    kleio.say "I hear that..."
    show kleio angry
    show fx anger
    kleio.say "Wait...WHAT?!?"
    "As soon as I know that I have Kleio's full attention, I hold up my hands in a gesture of surrender."
    mike.say "KIDDING!"
    mike.say "Kleio, I was just kidding, okay?"
    mike.say "You were miles away and I wanted to snap you out of it."
    "Kleio looks puzzled, then confused and finally she shakes her head."
    show kleio normal
    kleio.say "Yeah, I know..."
    kleio.say "Sorry, [hero.name]."
    kleio.say "I've had something on my mind for a while now."
    mike.say "I can see that!"
    "Kleio lets out a deep, emotional sigh."
    kleio.say "I need to do this now."
    kleio.say "Or else I'll lose my nerve..."
    "Now it's my turn to adopt a puzzled expression."
    "I have no idea what she could be talking about."
    "But then I see that Kleio's holding something between her fingers and thumb."
    "She must have pulled it out while I was looking her in the eye."
    show kleio blush
    kleio.say "I...I know this isn't how it's supposed to go."
    kleio.say "And I am NOT about to get down on one knee!"
    kleio.say "But, [hero.name]...will you marry me?"
    "It's only now that my eyes focus on the ring that Kleio's holding out to me."
    "I'm almost literally stunned, blinking and struggling to find my words."
    menu:
        "Say yes":
            "But when I finally snap out of it, the first thing I do is burst out laughing."
            show kleio annoyed
            "Instantly I see Kleio's face twist into an expression of annoyance."
            show kleio angry
            show fx anger
            kleio.say "Hey, you asshole!"
            show fx anger
            kleio.say "What's so funny?!?"
            kleio.say "I'm laying myself open here!"
            "I shake my head, managing to get my laughter under control."
            mike.say "No, Kleio, no..."
            mike.say "I'm not laughing at you."
            mike.say "I'm laughing because I love this so much!"
            show kleio surprised
            "Now Kleio's expression is one of bafflement."
            kleio.say "Y...you do?"
            show kleio normal
            mike.say "This is you, Kleio."
            mike.say "This is so perfectly you."
            mike.say "No one else could have done a thing like this."
            mike.say "That's why I love it - and you."
            show kleio blush
            "Kleio's cheek's flush as she looks this way and that, conscious of my being overheard."
            kleio.say "Shut up, [hero.name] - you're embarrassing me!"
            "It's a little too late for that now."
            "And if Kleio won't get down on one knee, then I will."
            "I kneel down in front of her, taking hold of the hand that's clutching the ring."
            mike.say "Yes, Kleio."
            mike.say "I will marry you."
            mike.say "Just so long as you never change who you are, okay?"
            show kleio at center, zoomAt(1.5, (640, 1040))
            "Kleio almost drags me to my feet, desperate to avoid a scene."
            "But in the struggle of limbs, I pull her into a tight embrace."
            "She returns the gesture, and I feel her push the ring onto my finger."
            kleio.say "You've done it now, Loverboy."
            kleio.say "Now you're stuck with me!"
            mike.say "Nowhere else I'd rather be..."
            hide kleio
            show kleio kiss
            $ kleio.flags.kiss += 1
            "The kiss that we share a moment later is deep, long and passionate."
            "I know we have the rest of our lives together."
            "But I still don't want it to end."
            $ kleio.set_fiance()
        "Say no":
            mike.say "Wow..."
            mike.say "Of all the things I ever imagined, Kleio!"
            mike.say "You proposing to me was not one of them."
            show kleio surprised
            "I see doubt instantly flash in Kleio's eyes."
            "She hastily pockets the ring and shakes her head."
            show kleio annoyed
            kleio.say "You don't sound like you're gonna say yes..."
            "I shake my head at this, smiling sadly."
            mike.say "It's very modern of you, Kleio."
            mike.say "But I'm just not in a place where I can do that right now."
            mike.say "Maybe some time in the future, but not now."
            show kleio sad
            kleio.say "Oh...okay...okay..."
            kleio.say "I guess it was a dumb idea anyway."
            "I think about saying more, about reassuring her."
            "But I can see that she's already pushing the whole thing aside in her mind."
            "Talking about it now would only cause an argument."
            "And so I leave the subject well alone."
            "I just hope that I haven't hurt Kleio too badly in the process."
            $ kleio.love -= 15
    $ game.room = "map"
    return

label kleio_male_ending:









    if renpy.has_label("kleio_achievement_3") and not game.flags.cheat:
        call kleio_achievement_3 from _call_kleio_achievement_3
    $ game.hour = 16
    scene bg alley
    "I don't know if I ever gave any serious thought to what the scene might look like on the day that I got married."
    "It's a pretty old and tired stereotype, I know - but as a guy, it never was something that occupied my mind."
    "But guess would be that, even if I had been tempted to do so, this is about a million miles away from what I'd have imagined."
    "Right now I'm standing on the tarmac in the middle of a vacant lot that's on the outskirts of the city."
    "I have no fucking clue if we're actually allowed to be here or not."
    "So we could be breaking the law for all I know."
    "But thankfully I'm not alone."
    "There are literally dozens of vehicles and more than a hundred people crowded around me."
    "The air is filled with exhaust fumes and the sound of engines being revved in anticipation."
    "And everyone present seems to be either a punk, biker, rockabilly or somewhere in-between."
    "It's a pretty unique occasion, that's for sure."
    "But then I am about to tie the knot with an equally unique girl."
    "That thought still fresh in my mind, I look to my side, where Kleio's standing."
    show kleio wedding blush with dissolve
    "And I find her doing the same thing, gazing up at me with that familiar, wry smile on her face."
    "There might have been a time when I found the impish impertinence she has about her annoying in the extreme."
    "But in the weeks and months that we've spent getting to know each other, that's become the last thing I feel for her."
    "Now all that smile means is that the girl I love is about to say something witty and smart, to make me laugh."
    "As hard as it might be to believe, I've actually come to find Kleio's sharp tongue to be something I adore."
    "Where before she was prickly and arrogant, now all I see is her passion and intelligence."
    "And it doesn't hurt that she looks as hot as hell right now too!"
    "Disdaining anything even slightly traditional, Kleio's wearing only a pair of shorts and a skimpy top."
    "But rather than her usual choice of black or similarly dark colours, today she's chosen white."
    if not kleio.is_visibly_pregnant:
        "Which helps to show off the tattoos and piercings all over Kleio's tight little body."
        "All of which I can recall kissing with my own lips on numerous occasions."
    else:
        "Which helps to show off the curve of her ever-growing belly for all to see."
        "Not that either of us is anything but proud of the fact we're soon going to be parents."
    "In fact the whole affair is pretty much a chance to stick the middle finger up to the haters in our lives."
    "All of this was her idea too, getting hitched in the middle of this automotive chaos."
    "We're surrounded by most of the friends and acquaintances she's made in the course of her career as a mechanic."
    "And they're making the whole affair feel a lot more like a raucous party than an actual wedding."
    "Personally, I couldn't give a damn how it looks to anyone else."
    show kleio wedding happy at center, zoomAt(1.5, (640, 1040))
    "Kleio's happy."
    "And if she's happy, then so am I."
    "Biker" "Dearly beloved..."
    "Biker" "I SAID DEARLY BELOVED!!!"
    "While the noise doesn't die down completely, it still quietens significantly."
    "All eyes are focused on the source of the bellowing that was responsible, waiting for what's to come next."
    "Kleio and I got the full effect, as the man who shouted them out is standing right in front of us."
    "A towering biker with a full beard and long hair, all in greys and silvers, eyes hidden behind his shades."
    "What marks him out from the crowd, apart from his commanding presence, is the bible clutched in one of his massive hands."
    "The guy's name escapes me, as I've been introduced to so many other bikers already today."
    show kleio wedding normal
    "But Kleio chose him on account of him once having been a priest."
    "At least that was before some unexplained incident saw him leave his church behind him."
    "I didn't have the courage to ask just what it was, as quite frankly, he terrifies me."
    "And the fact that he seems to have an almost paternal interest in Kleio's well being only adds to that feeling."
    "Biker" "Thank you..."
    "Biker" "Now, where was I..."
    "Biker" "We are gathered here today, to join my dear little Kleio here."
    "Biker" "And...let's see...[hero.name]..."
    "Biker" "To join them together in the bonds of holy matrimony."
    "All of the weddings that I've been to were fairly long affairs, with readings, poems and, of course, the exchange of vows."
    "That's why it takes me by complete surprise when he follows these few opening lines up with what comes next."
    "Biker" "So, Kleio - do you take [hero.name] to be your lawful, wedded husband?"
    "If she's as thrown as I am by the truncated ceremony, Kleio shows no sign of it."
    "Instead she nods happily and answers without pause or hesitation."
    show kleio wedding happy
    kleio.say "Hell yeah - I do!"
    "For a moment the biker looks at her, almost as if he was hoping for a different answer entirely."
    show kleio wedding normal
    "But then he seems to shake it off and remember the task at hand."
    "Biker" "And what about you, buddy?"
    "Biker" "Do you take Kleio here to be your lawful wedded wife?"
    "I open my mouth to say yes, but find myself cut off as he rumbles on."
    "Biker" "Do you promise to love, honour and obey her?"
    "Biker" "And, forsaking all others, to be faithful to her as long as your ass is alive?"
    "Wait a minute - all Kleio had to do was say yes."
    "And here I am feeling like I'm being interrogated by the Spanish Inquisition!"
    mike.say "I do..."
    mike.say "I will..."
    mike.say "Okay, are you happy now?!?"
    show kleio wedding happy
    "The biker nods at this, although his face still says he doesn't quite trust me."
    "Biker" "Then I now declare you wife and husband."
    "Biker" "You can kiss this fine specimen of a woman, I guess!"
    "Suddenly it feels like the cross-examination is over, and a sense of relief floods my entire body."
    "A feeling that's only made better when Kleio wraps her arms around my neck and pulls me down until we're looking each other in the eye."
    hide kleio
    show kleio kiss wedding
    with fade
    $ kleio.flags.kiss += 1
    "She doesn't stop to ask permission, and just plants her lips on mine."
    "I return the kiss with just as much passion, forgetting about every other person there."
    "And this isn't one of your traditionally chaste wedding kisses either."
    "It had tongues, audible sound-effects and lasts far longer than would normally be considered polite."
    "But all of that seems to meet with the approval of the crowd."
    "They cheer, rev their engines and pound their horns, creating enough noise to wake the dead."
    show kleio wedding happy at center, zoomAt(1.5, (640, 1040)) with fade
    "Kleio breaks the kiss then, wincing at the cacophonous sound, but smiling all the same."
    kleio.say "It's too late to run away now, Loverboy."
    show kleio wedding seductive
    kleio.say "You belong to me - and all these guys are my witnesses too."
    kleio.say "Better be nice to me, or they'll hunt you down!"
    show kleio wedding normal
    mike.say "Don't worry about that, Kleio."
    mike.say "None of these guys is even half as scary as you, even in his wildest dreams!"
    show kleio wedding blush
    show fx heart
    kleio.say "Aww, that's such a sweet thing to say!"
    kleio.say "I love you, Loverboy."
    mike.say "I love you too, Kleio."
    scene bg pool
    show kleio
    with fade
    kleio.say "So, anyway - enough of having that big schlub doing all the talking for me!"
    show kleio annoyed
    kleio.say "There was NO WAY I was gonna let him have the last word on our story."
    kleio.say "And I bet he made the whole thing sound pretty lame too!"
    kleio.say "I mean, it's hard for him to explain just how hot and edgy I really am."
    show kleio happy
    kleio.say "Bless Loverboy's little heart!"
    show fx heart
    kleio.say "I love him really."
    show kleio normal
    kleio.say "I guess this is the part where you're expecting me to say that I started out hating [hero.name], yeah?"
    kleio.say "But then he kind of grew on me, and I came to realise that I was actually in love with him, right?"
    show kleio annoyed
    kleio.say "Well forget that!"
    kleio.say "What do you guys think I am?"
    kleio.say "Some kind of predictable Tsundere in a manga you like to drool over?"
    show kleio normal
    kleio.say "I am SO much more than that!"
    kleio.say "But yeah, maybe I did think that [hero.name] was pretty lame at first."
    kleio.say "Can you blame me though?"
    kleio.say "He came over as just another dumb prick that Sasha foisted on the band."
    kleio.say "And they usually got the message that I'm not impressed with them super quick."
    kleio.say "But not Loverboy, oh no."
    kleio.say "The meaner I was with him, the more he seemed determined to stick around."
    show kleio annoyed
    kleio.say "To begin with, I just assumed he was a standard, run-of-the-mill guy."
    kleio.say "You know - a moron."
    show kleio normal
    kleio.say "But then he'd do or say something that was pretty smart."
    kleio.say "Well, not girl-smart, you know?"
    kleio.say "More like guy-smart like when a dog does a really neat trick, yeah?"
    kleio.say "Anyway, I guess he just kind of started to grow on me."
    kleio.say "Kinda like a dog too..."
    kleio.say "Seriously though, it's hard for me to talk about this kind of stuff."
    kleio.say "But that's one of the reasons [hero.name] really is great."
    kleio.say "He's never once chewed me out for being me, or asked me to change who I am."
    kleio.say "It's like...like everyone wants me to be something I'm not."
    kleio.say "Yet he's into me for who I actually am, you know?"
    kleio.say "Ah, I'm sounding all emotional and mushy - like Anna and Sasha!"
    kleio.say "But Loverboy just does that to me when I talk about him."
    show kleio blush
    show fx heart
    kleio.say "I guess I really do love him..."
    kleio.say "Anyway..."
    hide kleio
    $ game.room = "pool"
    show kleio ending
    with fade
    kleio.say "After we tied the knot, there wasn't time to think, or plan, or anything."
    kleio.say "We Deathless Harpies are currently in the middle of our first headlining tour."
    kleio.say "Sure, it's just playing clubs and shit, but it's ours and we own that fucker."
    kleio.say "And for now, it keeps our minds off of what happens when we're back to reality."
    if kleio.is_visibly_pregnant:
        kleio.say "It's getting harder to play my guitar every night."
        kleio.say "And we might end up coming home with a new member of the band."
        kleio.say "It's going to be a girl, and we've decided to call her 'Courtney'."
        kleio.say "Loverboy shits himself whenever the subject comes up."
        kleio.say "But we've agreed that we're moving in together once we're home again."
    else:
        kleio.say "Maybe he'll move in with me, or the other way around."
        kleio.say "But I have NO idea what Sasha would think about having me as a housemate!"
    kleio.say "So maybe we'll end up getting a place of our own."
    kleio.say "Fuck it, maybe we'll end up hitting the big time and move into a damn mansion!"
    kleio.say "Either way, all I know is that I want [hero.name] as close as possible..."
    kleio.say "WHAT?!?"
    kleio.say "No, I am not getting soft!"
    kleio.say "Geez..."
    kleio.say "You see, this is what happens when you try to open up and be honest about your feelings."
    kleio.say "Everyone and his fucking grandma tells you that you're just a big softie at heart!"
    kleio.say "Well it's not true..."
    kleio.say "Except...maybe in the case of Loverboy!"
    kleio.say "So, there you have it."
    kleio.say "I love him, he loves me and we're disgustingly happy right now."
    kleio.say "What more do you people want from me - blood?"
    kleio.say "At least I know what I want - and it's [hero.name]."
    kleio.say "I don't know what tomorrow might bring, or where we'll be in ten year's time."
    kleio.say "I say that you've got to grab life with both hands and hold on for the ride."
    kleio.say "And that's just what I intend to do."
    kleio.say "[hero.name]'s stuck with me now, whether he likes it or not!"
    kleio.say "Because I love his big, dumb ass - and that's all there is to it."
    kleio.say "So long, losers!"
    kleio.say "You might see us every day, or never again."
    kleio.say "But I don't think that you'll ever be able to forget us!"

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not kleio.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_11
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_11
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label kleio_event_talk_murder:
    show kleio sad at center, zoomAt(1.5, (640, 1040))
    "Kleio surprises me by throwing her arms around my neck and hugging me tightly."
    "It takes me a moment to snap out of it and hug her back in return."
    "And as I do I can feel the tension and trepidation lifting."
    "But not the guilt, that stubbornly remains."
    "Eventually, Kleio breaks the hug and looks up at me."
    "And I can see that she has tears in her eyes."
    kleio.say "Fuck me, man - this sucks worse than anything!"
    mike.say "I...I know, right?"
    mike.say "Look, Kleio..."
    mike.say "I understand if you're mad with me..."
    "Kleio looks at me as though she doesn't understand."
    "Then realisation dawns on her, and she shakes her head."
    kleio.say "Oh hell no!"
    kleio.say "Don't beat yourself up, man!"
    kleio.say "There's no way you could have known!"
    if kylie.flags.rape == True:
        kleio.say "And she assaulted you too."
        kleio.say "That's wrong, no matter that she's a woman and you're a man."
        kleio.say "You shouldn't feel guilty about it."
    else:
        kleio.say "Listen, we've all been there."
        kleio.say "We've all put our metaphorical dicks in crazy!"
        kleio.say "When you're into someone, you don't see the warning signs."
    "Of all the people that I know, I never thought I'd hear this from Kleio."
    "Sure, it's delivered in her usual, in your face style."
    "But I can hear the genuine emotion in her voice as she speaks to me."
    "And the look in her eyes is one hundred percent sincere."
    mike.say "I just keep thinking that I should have done something, Kleio!"
    mike.say "I should have been smarter or fought back harder."
    $ kleio.love += 10
    kleio.say "Nah, you couldn't."
    kleio.say "And it doesn't mean you're not a good guy."
    kleio.say "Sasha wouldn't have come running to help if you weren't."
    kleio.say "Because that girl could smell a cunt a mile off!"
    "I can't help laughing at Kleio's description of Sasha."
    show kleio happy
    "She joins in a moment later, so that we're both laughing."
    show kleio sad
    "But then Kleio suddenly bursts into tears, and I join her."
    show kleio at center, zoomAt(1.65, (640, 1140))
    "She leans against me and I wrap her in my arms."
    "It's comforting, but there's noting sexual about the moment."
    "We're just two friends, trying to prop each other up in a time of need."
    kleio.say "Come on, man - let's go grab a beer."
    kleio.say "We can get drunk and swap Sasha stories, yeah?"
    mike.say "Sounds good to me, Kleio."
    mike.say "Let's go!"
    "Still leaning against each other, we walk off towards Sasha's favourite pub."
    "And the rest of the night kind of disappears into a drunken blur."
    return

label kleio_birthday_date_male:
    $ DONE["kleio_birthday_date_male"] = game.days_played
    $ game.active_date.clothes = "casual"
    play music ["music/roa_music/horizon.ogg"] loop
    scene bg street
    show kleio b casual
    with fade
    "When I promised to take Kleio out on a date for her birthday, I didn't spare it a second thought."
    "But as soon as I had the chance to actually think about it, I realised that I was in serious trouble."
    "Because what in the hell kind of thing would someone like her want to do to celebrate her birthday?"
    "Can you seriously see Kleio eating a meal in a fancy restaurant?"
    "Or taking a romantic stroll on the beach at sunset?"
    "I can more imagine her drinking her own bodyweight in beer."
    "And then maybe challenging a biker-gang to an arm-wrestling contest!"
    "But then I had a revelation - Kleio's a mechanic, right?"
    "So I should take her to somewhere that'd come in useful."
    "Somewhere we can have some fun too."
    "Which is how we ended up here..."
    scene bg black with dissolve
    scene bg kart
    show kleio a surprised casual
    with dissolve
    mike.say "Ta da!"
    mike.say "Welcome to the Go-Kart track, Kleio!"
    mike.say "And happy birthday too!"
    "Kleio stares at the view before her for a moment, then back at me."
    show kleio a punk
    "And I see that she has one eyebrow raised, an amused expression on her face."
    kleio.say "Are you serious, Loverboy?"
    kleio.say "Aren't go-karts supposed to be for kids?"
    menu:
        "For kids, not for kids... Noodles, don't noodles...":
            mike.say "Oh come on, Kleio - lighten up, just for a little while."
            mike.say "It's your birthday, and you're supposed to be having fun."
            show kleio b annoyed
            "Kleio rolls her eyes at this."
            "But the I see that she gives me a little nod."
            kleio.say "Ah, what the hell..."
            $ game.active_date.score += 15
            kleio.say "I suppose it couldn't hurt."
            show kleio bbis normal
            kleio.say "You know most race-car drivers started out with go-karting?"
            mike.say "Really?"
            mike.say "No, Kleio, I did not know that!"
        "Say whaaat?!?":
            mike.say "Oh come on, Kleio - don't you think that's just a little ungrateful?"
            mike.say "After I went to all the trouble of booking this for your birthday too!"
            show kleio b annoyed
            "Kleio rolls her eyes and lets out a grumble."
            "Then she hits me with a pretty mean side-eye."
            show kleio a angry
            kleio.say "Okay, okay..."
            kleio.say "But I'm only doing this because you guilted me into it."
            show kleio a punk
            $ game.active_date.score -= 10
            kleio.say "Because you whined like a bitch and made me!"
            mike.say "Whatever, Kleio."
            mike.say "Let's just get this over with, okay?"
    "Once we're inside the place, I need to pick up our tickets."
    "I already made a reservation online, so Kleio and I join the queue."
    "The problem is that the track is busier than I was expecting."
    mike.say "Huh..."
    mike.say "The queue's pretty long today!"
    show kleio a annoyed
    kleio.say "Urgh..."
    kleio.say "Of course it is, dumbass!"
    kleio.say "We're in the middle of a school holiday."
    kleio.say "Places like this are crawling with little brats!"
    show emma blazer b at center, flip, zoomAt (1.0, (920, 380)), dark, dark, dark, dark
    show kleio at left5
    with dissolve
    "A woman standing in front of us in the queue seems to overhear our conversation."
    "And she turns around with a smile."
    show kleio a surprised
    "Woman" "Are you here with your kids too?"
    "Woman" "Ours love this place so much."
    "Woman" "Sometimes I feel like we spend the entire holiday here!"
    menu:
        "Warn the lady your \"Fury Road\" mode is on!":
            show kleio a normal
            mike.say "Oh, hell no!"
            mike.say "Kleio and I are here to race karts ourselves."
            "The woman looks at me in surprise."
            "Woman" "But..."
            "Woman" "Aren't you a little...well, old for this?"
            "I shrug and shake my head."
            mike.say "I don't see any age signs to say so, do you?"
            mike.say "So just tell your kids to keep out of my way, okay?"
            "The woman looks like she's about to say something in response."
            "In fact now that I look at her closely, she does look like a potential Karen!"
            "But then Kleio leans around me and chimes in too."
            show kleio d punk
            kleio.say "He's right, damn right!"
            kleio.say "We're gonna make those kids eat our dust!"
            hide emma with moveoutright
            "The woman frowns at me and turns her back."
            "Which I guess means that the conversation is over."
            show kleio bbis happy at center, zoomAt(1.5, (640, 1040))
            with hpunch
            "Then I feel Kleio elbow me in the ribs."
            mike.say "Ouch!"
            $ game.active_date.score += 15
            kleio.say "Way to go, Loverboy."
            kleio.say "That put her in her place."
            show kleio bbis punk
            kleio.say "And this is going to be some serious fun!"
        "Impress the lady by telling her you're here with your kids":
            mike.say "Erm..."
            show kleio a surprised
            mike.say "Yeah, we're here with our kids too."
            "The woman nods and smiles."
            "Then she points to a couple of kids."
            "Which happen to the most perfect, angelic looking youngsters imaginable."
            "Woman" "Those are my little darlings over there."
            "Woman" "Where are your's?"
            "Looking around in desperation, my eyes settle on some likely candidates."
            "And I point at the nearest group of kids."
            mike.say "Those are ours - the ones over there."
            "Woman" "You mean the kids trying to feed worms to the ones smaller than them?!?"
            show kleio a annoyed
            mike.say "Ah...yeah!"
            hide emma with moveoutright
            "The woman frowns at me and turns her back."
            "Which I guess means that the conversation is over."
            show kleio d angry at center, zoomAt(1.5, (640, 1040))
            with hpunch
            "Then I feel Kleio elbow me in the ribs."
            mike.say "Ouch!"
            $ game.active_date.score -= 10
            kleio.say "Way to go, Loverboy."
            kleio.say "Now they think we're raising a bunch of juvenile delinquents!"
    "Finally we get to the head of the queue and I confirm our booking."
    "And when the member of staff in the booth hands us our helmets, we're good to go."
    "Kleio and I stroll over to where the go-karts are parked."
    show kleio bbis annoyed
    "And I see that she's having a long, hard look at them."
    if hero.has_skill("video_games"):
        mike.say "You know what, Kleio..."
        mike.say "This reminds me of Plumber Kart!"
        "Kleio looks up from the kart she's studying."
        show kleio a
        "And she screws her face up in an expression of confusion."
        kleio.say "What are you even talking about?"
        kleio.say "You mean that dumb videogame?"
        mike.say "Erm...yeah, Kleio."
        show kleio angry
        kleio.say "You're clueless, Loverboy!"
        kleio.say "This isn't some dumb game."
        show kleio d
        kleio.say "This is the real thing!"
        menu:
            "Don't let her bother you. Pitch something":
                "I shake my head and chuckle."
                "All of which seems to fly straight up Kleio's ass."
                show kleio bbis annoyed
                kleio.say "What's so funny, huh?"
                mike.say "I might not be as much of a petrolhead as you, Kleio."
                mike.say "But I think I know a bit more about videogames."
                mike.say "You know they worked with real drivers and go-karts to make that game, right?"
                "Kleio looks more than a little confused."
                kleio.say "Ah..."
                show kleio b
                kleio.say "They did?"
                mike.say "Yeah, they did."
                mike.say "And they modelled all of the physics off the data they captured as well."
                kleio.say "Erm..."
                kleio.say "What does that mean?"
                mike.say "It means the game works just like the real thing!"
                show kleio bbis blush
                $ kleio.sub += 5
                "Kleio nods, beginning to look a little embarrassed."
                "But I feel empowered by having been able to school her on the subject."
            "Anyway... follow her lead to please her":
                "I find myself staring at the ground, feeling more than a little hurt."
                mike.say "Okay, Kleio, okay."
                mike.say "I know you're more knowledgeable than me when it comes to this kind of thing."
                mike.say "But there's no need to be so mean about it!"
                show kleio a happy at startle
                "Kleio laughs and shakes her head."
                kleio.say "Oh man..."
                show kleio a punk
                $ game.active_date.score -= 10
                kleio.say "You can be such a pussy!"
    else:
        if randint(1, 2) == 1:
            "I have a hunch that Kleio's going to be able to spot the best kart they have available."
            "And I figure that I need to turn that to my advantage somehow."
            "Hmm...I wonder if there's a way I can make her tell me what to look for."
            "And maybe I can do it without her even knowing too."
            "I take a quick glance around."
            "And then my eyes settle on the kart that looks in the worst condition."
            "Well, at least to my admittedly amateur eye."
            mike.say "Hey, Kleio..."
            mike.say "What about this Kart?"
            mike.say "It looks pretty nice."
            show kleio bbis annoyed
            "At the sound of my voice, Kleio walks over."
            if hero.has_skill("sneaky"):
                "As soon as she looks at the kart, Kleio shakes her head."
                kleio.say "Nah, this is trash!"
                show kleio a normal
                kleio.say "And here's why..."
                "What follows is a crash-course in go-kart mechanics."
                "I nod along the whole time, listening intently."
                "And when Kleio's done, I feel like I know enough."
                show kleio a happy
                $ game.active_date.score += 15
                kleio.say "Now I gotta go choose my kart, okay?"
                mike.say "Okay, Kleio..."
                mike.say "See you on the track."
                hide kleio with moveoutleft
                "Once I'm alone again, I use the info Kleio just gave me."
                "And I'm pretty confident it means I've chosen on of the best karts."
            else:
                "As soon as she looks at the kart, Kleio shakes her head."
                kleio.say "Nah, this is trash!"
                show kleio a angry
                kleio.say "Hey, wait a minute..."
                kleio.say "What are you trying to pull?"
                "I take a step back and raise my hands."
                mike.say "No tricks, Kleio - I swear!"
                show kleio bbis
                $ game.active_date.score -= 10
                kleio.say "Bullshit!"
                kleio.say "You know squat about this stuff."
                kleio.say "You were trying to get me to pick a kart out for you!"
                hide kleio with moveoutleft
                "Kleio shakes her head as she walks off to pick her own Kart."
                "Which I guess just leaves me to pick one at random and hope for the best."
        else:
            "I've got to admit that I have no idea what I'm looking for."
            "So all I can do is wander amongst the go-karts, choosing one at random."
            show kleio a happy
            "I notice that Kleio's watching me with a wry smile on her face."
            "And when she sees me looking in her direction, she comes over."
            show kleio a normal
            kleio.say "Don't know which one to choose, huh?"
            kleio.say "Well, you should get more clued-up, Loverboy!"
            kleio.say "And don't go asking me for any help."
            kleio.say "This was your idea - so I wanna see how well you pick 'em!"
            "I give Kleio a last pleading look."
            "But she nods her head towards the go-karts."
            "Which lets me know that I'm on my own."
            "So it looks like I'm just going to have to choose at random."
            "And hope that I get lucky too..."
            if hero.is_lucky:
                mike.say "Erm..."
                mike.say "What about these ones?"
                mike.say "They're a very nice colour."
                mike.say "Maybe that means they'll go faster?"
                "Kleio looks at me like she's going to laugh."
                show kleio a surprised at startle
                "But then something about the karts seems to catch her eye."
                "She leans in close to poke around the engines."
                "And then she stands up shaking her head."
                kleio.say "Well fuck me sideways..."
                show kleio a normal
                kleio.say "It might be sheer dumb luck."
                kleio.say "But these look like the best karts they have here!"
                show kleio a happy
                $ game.active_date.score += 15
                kleio.say "Next time I buy a car, I'm bringing you along to check it out!"
                hide kleio with moveoutleft
            else:
                mike.say "Erm..."
                mike.say "What about these ones?"
                mike.say "They're a very nice colour."
                mike.say "Maybe that means they'll go faster?"
                show kleio surprised
                "Kleio looks at me in sheer amazement."
                show kleio b happy at startle
                "And then she bursts into laughter."
                kleio.say "Go faster because they're a nice colour?"
                kleio.say "Are you a fucking moron or what?!?"
                kleio.say "No...don't answer that."
                show kleio bbis
                $ kleio.sub -= 5
                kleio.say "Just leave picking the cars to me."
                hide kleio with moveoutleft
    play music "music/TeknoAXE/simple_metal.ogg" loop fadein .5
    play sound car_ignition
    scene kleio kart kleio zorder 2 at center, zoomAt(1.0, (640, 720))
    show kleio_kart_bg as bg zorder 1 at center, zoomAt(1.25, (640, 880))
    show kleio_kart_mikemc as mike zorder 3 at center, zoomAt(0.9, (640, 660))
    with fade
    "Now that we've got ourselves a couple of go-karts, we're ready to hit the track."
    "So I hastily leap into my kart and then I strap myself in."
    "But even as I try to get the thing started, Kleio shoots past me in her own kart!"
    show kleio kart kleio at center, traveling(1.25, 2.0, (540, 880))
    kleio.say "Ha ha!"
    kleio.say "Eat my dust, loser boy!"
    "Normally I'm pretty calm behind the wheel of a car."
    "Yet somehow Kleio's mocking words are like a red rag to a bull."
    show kleio_kart_bg as bg zorder 1 at center, traveling(1.0, 2.0, (640, 720))
    show kleio_kart_mikemc as mike at center, traveling(1.0, 2.0, (640, 720))
    "And I screech after her, my ears filled with the sound of tortured rubber."
    "Once I'm on the track, I see her up ahead of me."
    "And then the race is well and truly on!"
    if hero.has_skill("racing"):
        "I might have deliberately forgotten to tell Kleio this."
        "But kart racing's been a passion of mine since I was a kid."
        "I literally can't count the hours that I've spent tearing up tracks like this."
        "And so sitting in the seat of a go-cart is like coming home."
        "It doesn't take me long to catch up to Kleio, closing the gap in record time."
        "My instincts are serving me really well too."
        "I see the perfect spot to overtake her kart coming up."
        "But then a thought occurs to me."
        "Do I really want to beat Kleio on her birthday?"
        menu:
            "Show her what it's like to be the best":
                "Screw being nice!"
                "Kleio's not going to respect me for that."
                "I pull out before a corner, almost going onto two wheels."
                show kleio_kart_mikemc as mike zorder 3 at center, traveling(1.1, 5.0, (640, 800))
                show kleio kart kleio at center, traveling(0.9, 5.0, (640, 660))
                "And then I scream past her and into the lead."
                "After that the roles are reversed."
                "Kleio's in my rear-view mirror for the rest of the race."
                "But there's no way she can catch me!"
                "I tear past the finish-line and screech to a halt."
                play music ["music/roa_music/horizon.ogg"] loop
                scene bg kart
                show kleio a surprised casual
                with fade
                "Then I see Kleio walking towards me."
                kleio.say "Where the fuck did you learn to drive like that?!?"
                mike.say "I don't know, Kleio - it just came naturally, I guess!"
                show kleio a normal
                "Kleio snorts and nods."
                $ game.active_date.score += 10
                $ kleio.sub += 2
                "But I note a look of newfound respect in her eyes."
            "Let her win, it's her birthday after all":
                "I decide that the best thing to do is to let Kleio have the win."
                "But that doesn't mean I have to make it look easy for her."
                show kleio_kart_bg as bg zorder 1 at center, traveling(1.0, 2.0, (640, 720))
                show kleio_kart_mikemc as mike at center, traveling(0.9, 2.0, (640, 660))
                show kleio kart kleio at center, traveling(1.1, 2.0, (540, 800))
                "I'm on Kleio's ass the whole time that we're racing round the track."
                "Every time I spot her make a mistake or a chance, I go for it."
                "But I'm always careful to pull back at the last moment."
                "That way I manage to make it look like Kleio's just keeping ahead of me."
                "And on the final lap, I make sure to be just about to catch her."
                "Right on her tail as she flies across the chequered line."
                "I come in second, stopping my kart in a safe spot."
                play music ["music/roa_music/horizon.ogg"] loop
                scene bg kart
                show kleio a surprised casual
                with fade
                "Then I see Kleio walking towards me."
                show kleio a
                kleio.say "You almost had me back there!"
                kleio.say "Where the fuck did you learn to drive like that?!?"
                mike.say "I don't know, Kleio - it just came naturally, I guess!"
                show kleio a normal
                "Kleio snorts and nods."
                $ game.active_date.score += 20
                "But I note a look of newfound respect in her eyes."
    else:
        if randint(1, 2) == 1 or hero.is_lucky:
            "I don't know what in the hell comes over me."
            "But not only am I keen to chase after Kleio, I'm on fire too."
            "Everything just seems to click as I follow her around the track."
            "And before she knows what's happening, I'm all over her ass!"
            "Sure, Kleio's a pretty mean driver behind the wheel."
            "But I feel like I'm on a higher plane."
            "Like I've become a savant or something!"
            "I pull out before a corner, almost going onto two wheels."
            show kleio_kart_mikemc as mike zorder 3 at center, traveling(1.1, 5.0, (640, 800))
            show kleio kart kleio at center, traveling(0.9, 5.0, (640, 660))
            "And then I scream past her and into the lead."
            "After that the roles are reversed."
            "Kleio's in my rear-view mirror for the rest of the race."
            "But there's no way she can catch me!"
            "I tear past the finish-line and screech to a halt."
            play music ["music/roa_music/horizon.ogg"] loop
            scene bg kart
            show kleio a surprised casual
            with fade
            "Then I see Kleio walking towards me."
            kleio.say "Where the fuck did you learn to drive like that?!?"
            mike.say "I don't know, Kleio - it just came naturally, I guess!"
            "Kleio snorts and nods."
            $ game.active_date.score += 15
            $ kleio.sub += 2
            "But I note a look of newfound respect in her eyes."
        else:
            "I chase after Kleio, fully intending to catch up to her."
            "But no matter how I hold my foot down on the accelerator, it does me no good."
            hide kleio with easeoutleft
            "She stays ahead of me the whole time, leaving me well behind."
            "In fact, I'm so fixated on catching Kleio that I ignore everything else."
            show kleio_kart_mikemc as mike at center, traveling(1.4, 0.5, (540, 940))
            "And that's why I end up losing control towards the end of the race."
            play sound car_screeching_tires
            hide kleio_kart_mikemc as mike with easeoutright
            "Misjudging a corner, I spin out."


            with vpunch
            with hpunch
            "And I collide with the tyres at the side of the track."
            show kleio a happy casual
            play music ["music/roa_music/horizon.ogg"] loop
            scene bg kart
            show kleio a surprised casual
            with fade
            "When my vision clears, I see Kleio walking towards me."
            kleio.say "Wow..."
            kleio.say "You really do suck at this!"
            mike.say "Thanks, Kleio..."
            mike.say "I take it you won?"
            show kleio a normal
            $ game.active_date.score += 5
            "Kleio nods and smiles."
            "So I try to console myself with the fact I at least managed to make her happy."
    show kleio bbis casual normal
    "Once we're done racing, Kleio and I find a quiet spot away from the track."
    "Neither of us says as much, but I guess we just need a few moments to chill out."
    "Though that doesn't mean Kleio's going to be letting up on me just yet."
    kleio.say "So..."
    show kleio a
    kleio.say "You brought me on a date?"
    mike.say "Yeah."
    kleio.say "And it's my birthday, right?"
    mike.say "It sure is, Kleio."
    show kleio b
    kleio.say "So is there anything else you got for me?"
    if not hero.has_gifts:
        "Oh shit!"
        "I thought I remembered everything."
        "But I went and forgot Kleio's birthday present!"
        "There's nothing else for it."
        "I'm just going to have to try and lie my way out of this one."
        mike.say "Well, I didn't get you a lame present, Kleio!"
        mike.say "Because that would have been so predictable, yeah?"
        mike.say "And I know you're not the kind of girl to be into that anyway!"
        show kleio a
        "Kleio looks at me like she's going to tell me off."
        "But then I see the look of recognition in her eye I was hoping for."
        "The look that lets me know I've pulled it off."
        $ game.active_date.score -= 10
        $ kleio.love -= 5
        show kleio a happy
        kleio.say "Well...yeah!"
        show kleio a normal
        kleio.say "You got me right there, Loverboy!"
        "I can see that she's really feeling let down."
        "But at least the lie got me off the hook for now."
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_28
        if _return != "done":
            if _return not in ["None", "exit"]:
                "I hold up one hand while I reach for something with the other."
                mike.say "Now don't get mad, Kleio."
                mike.say "Because I know you're not into the usual birthday traditions."
                mike.say "But I got you a gift anyway."
                "Kleio eagerly takes the gift from my hands."
                "All the time trying to look like she's doing so under sufferance."
                kleio.say "Ah, you really shouldn't have."
                kleio.say "But I'll let it slide this one time!"
                if _return:
                    show kleio bbis
                    play sound [paper_ripping_2, paper_ripping_1]
                    "Kleio tears off the paper and tosses it aside."
                    "But the moment she sees what's inside, her face lights up."
                    show kleio bbis surprised at startle
                    kleio.say "NO WAY!"
                    kleio.say "You have got to be fucking with me!"
                    mike.say "What's the matter, Kleio?"
                    mike.say "Is everything okay?"
                    "Kleio looks me in the eye."
                    $ game.active_date.score += 15
                    show kleio bbis happy
                    "And I can see the sheer amazement on her face."
                    kleio.say "Where the fuck did you find this?!?"
                    kleio.say "Do you even know how rare they are?"
                    kleio.say "I've been looking for one since forever!"
                    mike.say "Ah...yeah, Kleio."
                    mike.say "I remember you mentioned it a couple of times."
                    mike.say "And it wasn't easy to find - but I got lucky!"
                    hide kleio
                    show kleio kiss casual
                    with hpunch
                    $ kleio.flags.kiss += 1
                    "I'm taken by surprise a moment later, when Kleio kisses me passionately."
                    "And the fact she squeezes my cock pretty hard too only adds to the sensation!"
                    "So I'm going to guess that she likes her birthday present."
                else:
                    show kleio bbis
                    "Kleio tears off the paper and tosses it aside."
                    "But the moment she sees what's inside, her face falls."
                    show kleio a annoyed
                    kleio.say "Oh..."
                    mike.say "What's the matter, Kleio?"
                    mike.say "Is everything okay?"
                    $ game.active_date.score -= 10
                    "Kleio grunts and shrugs her shoulders."
                    kleio.say "Ah..."
                    show kleio b
                    kleio.say "It's not a total pile of shit."
                    kleio.say "But you could have done better!"
                    "I'm more than a little stunned by how blunt Kleio's being."
                    "So all I can do is nod slowly."
                    mike.say "Okay, Kleio..."
                    mike.say "I guess I'll try harder next time."
            else:
                "Oh shit!"
                "I thought I remembered everything."
                "But I went and forgot Kleio's birthday present!"
                "There's nothing else for it."
                "I'm just going to have to try and lie my way out of this one."
                mike.say "Well, I didn't get you a lame present, Kleio!"
                mike.say "Because that would have been so predictable, yeah?"
                mike.say "And I know you're not the kind of girl to be into that anyway!"
                show kleio a
                "Kleio looks at me like she's going to tell me off."
                "But then I see the look of recognition in her eye I was hoping for."
                "The look that lets me know I've pulled it off."
                $ game.active_date.score -= 10
                $ kleio.love -= 5
                show kleio a happy
                kleio.say "Well...yeah!"
                show kleio a normal
                kleio.say "You got me right there, Loverboy!"
                "I can see that she's really feeling let down."
                "But at least the lie got me off the hook for now."
    hide kleio
    show kleio bbis casual normal
    with fade
    "By now I feel like I'm all rested from the first race I had against Kleio."
    "And it seems that she's feeling the same way too, as she leaps to her feet."
    kleio.say "You know what, Loverboy?"
    kleio.say "I'm really getting into this shit now!"
    show kleio a
    kleio.say "You wanna hit the track a second time?"
    "I look over Kleio's shoulder at the go-kart track."
    "And I wonder if I have another race around it in me."
    "Sure, I could really push myself and do what Kleio wants right now."
    "It is her birthday, after all."
    "But on the other hand, I'm feeling seriously bushed."
    "Another race would probably finish me off!"
    menu:
        "Let's race again!":
            mike.say "Okay, Kleio - you're on."
            mike.say "Otherwise you'll end up racing against kids."
            mike.say "And it'd be embarrassing to see them beat your ass!"
            show kleio bbis surprised
            "Kleio's eyes go wide as I stand up."
            "But she laughs at my cockiness all the same."
            show kleio d punk
            $ game.active_date.score += 20
            kleio.say "Big talk, loser boy!"
            kleio.say "Let's see if you can back it up on the track!"
            "Together we hurry over to where the go-karts are parked."
            "And we're soon speeding around the track for a second time."
        "Another time maybe, I don't feel like it":
            mike.say "Nah, Kleio..."
            mike.say "I think I'll pass on this one."
            $ game.active_date.score -= 10
            show kleio a annoyed
            "Kleio frowns at this, clearly disappointed with my answer."
            "But she gets up and starts towards the track all the same."
            kleio.say "Well forget you then, you boring bastard!"
            kleio.say "I'd rather race against adults."
            kleio.say "But if you force me to do it against kids..."
            show kleio bbis punk
            kleio.say "Then I'm gonna bash their heads in and laugh while I do it!"
            "I can't help thinking that it might have been safer to just say yes."
            "But I've made my decision now, and I have to stand by it."
            "Because I don't think Kleio will respect me if I go changing my mind."
    show kleio bbis normal
    "It's getting to the time of day when I think we've had enough go-karting."
    "In fact I'm starting to feel like I've had enough go-karting to last me a lifetime!"
    "I take a quick glance over at Kleio, just to be sure."
    "And I can see that she's tired, even though she's trying to hide it under her usual bravado."
    mike.say "Think we should be moving on, Kleio?"
    mike.say "I know I'm feeling pretty beat!"
    show kleio a happy
    kleio.say "Ha!"
    kleio.say "What a wimp!"
    "I watch as Kleio does her best to stifle a yawn."
    show kleio b normal
    kleio.say "But yeah..."
    kleio.say "Maybe we should give someone else a chance."
    show kleio d punk
    kleio.say "I'm tired, sure - tired of kicking your ass!"
    show bg street
    show kleio b normal
    with fade
    "As we walk out of the go-karting track, Kleio pauses to take a look back."
    show kleio bbis normal
    kleio.say "You know what..."
    mike.say "What, Kleio?"
    kleio.say "We should try racing for real some time soon."
    mike.say "You mean...like, in real cars?"
    show kleio a
    kleio.say "Yeah, exactly like that!"
    kleio.say "Could be a lot of fun."
    menu:
        "It's a deal":
            "I think about it for a moment, trying to be serious."
            "I mean, the thought of Kleio in a full-sized racing car is pretty scary!"
            "But people race cars all the time."
            "And there has to be some kind of health and safety involved, right?"
            mike.say "Yeah, Kleio..."
            mike.say "That sounds like it could be fun."
            mike.say "So long as you're not talking about a demolition derby!"
            $ game.active_date.score += 15
            $ kleio.love += 2
            show kleio a happy
            "Kleio snorts and shakes her head."
            "But she looks more than a little pleased with my answer."
            kleio.say "Ha!"
            kleio.say "I was sure you were gonna say no."
            show kleio a punk
            kleio.say "Maybe you're not such a pussy after all, Loverboy!"
        "Nonsense":
            "The mere thought of getting into a full-sized racing car fills me with dread."
            "I mean, puttering around on a go-kart is one thing."
            "But doing it in a real car sounds crazily dangerous!"
            mike.say "Oh no!"
            mike.say "No way, Kleio!"
            mike.say "Are you actually thinking up ways to kill me?!?"
            $ game.active_date.score -= 10
            show kleio a annoyed
            "Kleio rolls her eyes and shakes her head."
            kleio.say "Urgh..."
            kleio.say "Forget I mentioned it, Loverboy."
            kleio.say "And try to keep your knickers on!"
    mike.say "Anyway..."
    mike.say "I think that's officially the end of our date, Kleio."
    mike.say "I had a great time today - how about you?"
    show kleio bbis normal
    "Kleio looks at me in silence for a moment."
    "And I get the feeling she's weighing things up in her head."
    if game.active_date.score >= 100:
        show kleio a
        kleio.say "You know what, Loverboy..."
        kleio.say "Today's been pretty fucking amazing!"
        kleio.say "You really pulled it off."
        "I can't help smiling at Kleio's reaction."
        "Because praise like this is rare on her part."
        mike.say "Erm..."
        mike.say "So..."
        mike.say "We'll do this again?"
        mike.say "Some time soon maybe?"
        "Kleio shakes her head at this."
        show kleio bbis seductive
        kleio.say "Oh no..."
        kleio.say "We're not done yet."
        kleio.say "Not by a long shot!"
        "The next thing I know, Kleio grabs hold of my wrist."
        "And then she's dragging me off somewhere without even asking for permission!"
        call kleio_birthday_sex from _call_kleio_birthday_sex
    else:
        kleio.say "Ah..."
        show kleio a
        kleio.say "I had an okay time, I guess."
        "It's not the answer I was hoping for."
        "But it looks like that's the best I'm going to get out of Kleio."
        mike.say "Erm..."
        mike.say "So..."
        mike.say "We'll do this again?"
        mike.say "Some time soon maybe?"
        "Kleio shrugs and begins to walk away."
        show kleio b normal
        kleio.say "Yeah, maybe..."
        kleio.say "I'll call you, okay?"
        hide kleio
        "With that she turns and continues off down the street."
        "Leaving me to start walking home in the opposite direction and alone."
    return

label kleio_birthday_sex:
    scene bg street
    show kleio bbis casual seductive
    with fade
    "It doesn't take me long to recognise the neighbourhood Kleio's dragging me through."
    "It's a little more rough and ready than the ones I'm used to frequenting on a daily basis."
    "This place is more lock-ups and scrapyards than anything else."
    "Which is why the garage that Kleio works at as a mechanic is around here too."
    "I don't think she's planning on showing me around the local junkyards either."
    "So I guess that's where we're headed right now."
    scene bg garage
    show kleio a casual seductive
    with fade
    "Sure enough, Kleio leads me right to the garage."
    "Then we slip down an alley-way, and she lets us in through a side-door."
    "I look around as Kleio flips on the lights."
    "And my senses fill with the smell of oil and other automotive fluids."
    mike.say "Are we here for you to catch up on some work, Kleio?"
    mike.say "Or did you have something else in mind?"
    show kleio c
    "Kleio grins at me like a feral cat."
    "And rather than answering, she stalks over to a car in the middle of the room."
    "Well, I'm guessing that it's a car."
    "Because while it's car-shaped, the whole thing is under a tarp at the moment."
    "And if it's not, then that's one crazy coincidence!"
    show kleio a
    kleio.say "Over here."
    "Kleio beckons for me to follow her."
    kleio.say "Come take a look at this!"
    "I do as I'm told, walking over to join Kleio."
    "And once I'm there, she whips back the tarp with a dramatic gesture."
    if hero.knowledge >= 60:
        "For a couple of seconds, I can't actually believe what I'm seeing."
        "I blink and rub my eyes, but when I open them, it's still there."
        mike.say "Kleio..."
        mike.say "Is that what I think it is?"
        mike.say "Is that a Buccaneer Banzai?!?"
        $ kleio.love += 5
        show kleio a happy
        "Kleio's face lights up the moment I name the car."
        "And she nods, practically oozing enthusiasm."
        kleio.say "I fucking know, right?"
        kleio.say "I never thought I'd even see one."
        kleio.say "But I'm actually working on this one!"
    else:
        "I stare at the car was under the tarp."
        "For sure it looks very pretty."
        "And very old too, which probably means it's valuable."
        "But I have no idea what the hell it is!"
        mike.say "Erm..."
        mike.say "That's a very nice car, Kleio."
        mike.say "What kind is it?"
        show kleio bbis happy
        "Kleio chuckles and shakes her head."
        kleio.say "I should have known you wouldn't know what it was, Loverboy!"
        show kleio a normal
        kleio.say "For your information, this is a Buccaneer Banzai."
        kleio.say "I never thought I'd even see one."
        show kleio a happy
        kleio.say "But I'm actually working on this one!"
    "I step forwards and put a hand on the bonnet of the car."
    "Up close I can start to see what's so special about it."
    "Kleio walks over to join me, putting her hand atop mine."
    show kleio bbis seductive
    kleio.say "Thing is, Loverboy..."
    kleio.say "The owner's never going to let me drive this car."
    kleio.say "So I want to do the next best thing while it's in here."
    mike.say "And that is...what, Kleio?"
    "Kleio hops onto the bonnet of the car, sitting down and spreading her legs."
    show kleio a punk
    kleio.say "I want to get fucked on the bonnet!"
    kleio.say "And I want you to be the one to do it to me!"
    mike.say "Sure, Kleio..."
    mike.say "I..."
    mike.say "Urgh..."
    show kleio close bbis seductive with vpunch
    "Kleio cuts me off before I can finish by grabbing my collar."
    "Then she yanks me closer, looking me straight in the eye."
    kleio.say "Sorry, Loverboy..."
    kleio.say "Didn't make myself clear just now."
    show kleio close a
    kleio.say "I wasn't asking, I was telling!"
    hide kleio
    show kleio kiss casual
    with hpunch
    $ kleio.flags.kiss += 1
    "With that, Kleio clamps her lips down on mine."
    "Her tongue snakes into my mouth, and she kisses me hungrily."
    "At the same time she pulls me down on top of her, legs wrapping around my waist."
    "And I can feel her hand squeezing my cock as well, fumbling with my flies."
    "But let's get one thing straight here, okay?"
    "Kleio might have just taken me by surprise."
    "But I'm totally up for what she wants right now."
    "The second I recover from the surprise, I leap into action too."
    "And my hands are all over her body."
    "They slide up her thighs and onto her flat belly."
    "The next second they're grasping her breasts through her shirt."
    "And I feel Kleio's nipples hardening from my touch."
    "The sensation speeds up my own cock getting hard too."
    "As does the sound of Kleio moaning with pleasure."
    kleio.say "Mmm..."
    kleio.say "Oh yeah..."
    kleio.say "Like that...just like that!"
    show kleio kiss topless with dissolve
    $ kleio.flags.kiss += 1
    "Spurred on by Kleio's words, I begin to pull off her top."
    "She doesn't resist for a second, but does all she can to help."
    "Which isn't much, as she's also trying to pull out my cock at the same time!"
    "Somehow this confused mass of limbs and sexual tension works out."
    show kleio kiss naked -topless with dissolve
    "One by one we strip off each other's clothes."
    "And I know that we're ready to go when I feel Kleio's skin against mine."
    show kleio missionary with fade
    kleio.say "Do it!"
    kleio.say "Stick it in my pussy..."
    kleio.say "Then fuck me hard!"
    show kleio missionary mike with dissolve
    "I nod eagerly as Kleio pushes the head of my cock against her pussy."
    "Pushing from my own side, I feel how slick she is down there."
    "The feel and the scent of it begin to overwhelm my senses."
    "And from that point on, I don't need any more encouragement."
    "Grabbing hold of Kleio's thighs, I feel my fingers sink into them."
    show kleio missionary vaginal pleasure
    "Then I thrust myself forwards, and I feel myself sinking into another part of her too."
    "Kleio's pussy is tight, and her muscles squeeze me almost like they're aggressive in their own right."
    "But the whole thing feels so fucking good as she clings onto me."
    "I can't help grunting like some kind of animal as I go as deep as possible."
    "All the while I can feel Kleio's head resting on my shoulder."
    "Her breath comes in gasps, in time with my own thrusts."
    "And for all her ferocious talk, she's being reduced to a state of helplessness."
    show kleio missionary flirt blush
    kleio.say "Y...yeah..."
    kleio.say "That's what I want..."
    kleio.say "Just like that..."
    "This is the side of Kleio that makes me crazy."
    "The side that nobody else gets to see."
    "Inside of the fierce alley-cat is a sex-kitten."
    "And I just love the sound of her purring away as she gets fucked!"
    "Leaning my head down, I begin to nuzzle at Kleio's breasts."
    show kleio missionary pleasure sweat
    "I tease and nibble at the nipples, making her squeal with pleasure."
    "The sound of her buttocks squeaking against the bonnet of the car speeds up."
    "And I can feel the muscles inside her pussy start to twitch and tense."
    kleio.say "Oh..."
    kleio.say "Oh fuck..."
    kleio.say "I'm...I'm gonna cum!"
    show kleio missionary ahegao creampie with vpunch
    "Kleio's not the only one, and I shoot my load just as she starts to cum."
    with vpunch
    "Her arms wrap around my neck and her legs cross at the base of my spine."
    with vpunch
    "This means she's clinging into me for dear life the whole time."
    "But when it's all over, she lets go and falls back onto the bonnet of the car."
    show kleio missionary -mike with dissolve
    "I stand back and shake my head."
    mike.say "Oh man..."
    mike.say "Phew..."
    mike.say "Wow, Kleio..."
    mike.say "I think we made a mess of the car!"
    show kleio missionary flirt
    "Kleio looks up at me while stroking her slick pussy with one hand."
    "She's flushed and panting, but looks totally satisfied."
    show kleio missionary pleasure
    kleio.say "Ah, fuck the car, Loverboy."
    kleio.say "That was worth it."
    kleio.say "And I can just buff it out on Monday morning!"
    $ kleio.sexperience += 1
    scene bg black with dissolve
    return

label kleio_kiss_me:
    call kleio_greet from _call_kleio_greet_5
    show kleio
    "From the ironic sneer that's on her lips, I can't help thinking that Kleio's about to spit an insult at me."
    "But when she grabs a handful of my collar and yanks my face close to hers, my mouth opens in surprise."
    hide kleio
    show kleio kiss
    with fade
    $ kleio.flags.kiss += 1
    "She takes full advantage of this, sticking her tongue between my lips without warning."
    "It actually takes me a couple of seconds to realise that Kleio's kissing me."
    "But I pretty much know that it's a very pleasant feeling from the moment she begins."
    "And from there, my only concern is when it's going to stop..."
    hide kleio kiss with fade
    return

label kleio_say_preg:
    scene bg street
    "Kleio picks me up on the street corner a little way down from my house block, screeching to a halt in her characteristic manner."
    "I'm already sensing that something's off with her, as she usually stops out front of my building, and now she seemingly doesn't want anyone else to see her."
    "As I open the door to get in, I notice that I'm not met by the usual blare of insanely loud punk or metal."
    play sound car_door
    pause 0.5
    play sound car_ignition
    with vpunch
    "Almost before I'm strapped in and certainly before I can speak a single word, Kleio slams the car into gear and tears away from the curb."
    mike.say "And good morning to you, too!"
    kleio.say "What...did you say something to me?"
    "She's obviously distracted, making her normally erratic driving that much worse as a result."
    mike.say "I just said good morning."
    kleio.say "Oh...okay...whatever."
    "Distracted, erratic and none of her usual acid-tongued sarcasm."
    "Even I can sense that there's something serious eating at her this morning."
    mike.say "Kleio, what the hell's up with you?"
    kleio.say "It's...I'm okay, I guess - we just need to talk, that's all."
    "Those four words that all sane men dread to hear - 'we need to talk'!"
    with hpunch
    "I say nothing until Kleio picks a suitably deserted back street and pulls in to park."
    show kleio casual at center, zoomAt(1.65, (640, 1140)) with dissolve
    "Taking a breath so deep I can hear it, Kleio turns in her seat to look me in the eye as she speaks."
    kleio.say "I don't know how to say this, so I'm just going to come out and say it - I'm pregnant."
    "For a second I can't seem to make sense of what she's said."
    "Then the enormity of it hits me, and I suddenly feel like I've been punched in the gut, all the air sucked out of my lungs."
    if kleio.love <= 175:
        show kleio casual sad
        kleio.say "Yeah, that's pretty much how I thought you'd take it."
        "I can see the sadness in her eyes turning into resentment as she speaks."
        kleio.say "Don't worry, I'm not gonna ask you to settle down and play happy families with me."
        kleio.say "I already called some place and made arrangements."
        menu:
            "Agree":
                mike.say "You are right, it's for the best."
                $ kleio.love -= 20
                $ kleio.sub += 5
            "Disagree" if hero.charm >= 50:
                mike.say "Don't pretend you know how I feel, I would have supported our child all the way."
                $ kleio.love -= 10
        kleio.say "Yeah, right..."
        $ kleio.unpreg()
        return
    else:
        show kleio casual sad
        kleio.say "Fuck it, I'm sorry to just throw all of this in your lap."
        "I can see the fear and a little bit of hope in her eyes as she lays herself open to me."
        kleio.say "I always told myself that I'd have an abortion if I got pregnant."
        show kleio normal
        kleio.say "But that was before I met you, and...well, the time we've had together kind of changed my mind."
        kleio.say "I want to keep it - but I want you to be involved as well."
    "My mouth works like a fish out of water, as I still feel breathless and stunned."
    "Kleio keeps on staring at me, as though she won't be happy until she hears something that'll satisfy her."
    menu:
        "No":
            mike.say "Jesus Christ, Kleio...you can't just throw something like this in my face and ask me to cope!"
            mike.say "I'm not even slightly ready to be a parent, and neither are you!"
            show kleio annoyed
            "Kleio grimaces at the sting of my words, clearly seeing her hopes dashed, but then her face hardens."
            show kleio angry
            kleio.say "What are you saying, [hero.name] - that I'd make a shitty mother, or that you're not man enough for the job?!?"
            mike.say "Yes...no...both of them...none of them...I don't know what I mean, damn it!"
            kleio.say "Yeah, maybe...but I do know that you don't care for me enough..."
            $ kleio.set_gone_forever()
        "Yes":
            mike.say "Yes...of course...if that's what you want...is that what you want?!?"
            show kleio casual happy
            "Kleio's face floods with what looks like a mix of relief and actual genuine joy."
            kleio.say "Of course it's what I want, you moron - would I have asked if it wasn't?"
            mike.say "Sorry...I just never thought of you as the 'mothering type' before, that's all."
            show kleio seductive
            "Kleio shoots me a sideways glance, grinning slyly at the implied insult in my words."
            mike.say "Sorry again...it's something I never thought about either, but with you, it just feels right somehow."
            $ kleio.love += 10
    play sound car_ignition
    with vpunch
    "The drive back to my house is spent in silence, as we both retreat into our own thoughts."
    "I get the feeling that a lot just happened in the space of a very short time, things that will bring big changes in the near future."
    $ kleio.flags.toldpreg = True
    return

label kleio_practice_01:
    "With the Battle of the bands getting so close, most of my free time had been eaten up at the practice room."
    "Save for working, eating and sleeping, playing music, or at least trying to and arguing over it was all I'd done."
    "Normally the prospect of being locked in a room with a trio of feisty women would have been a dream come true."
    "But tempers were getting frayed as we tried to get everything just right."
    "When I noticed their moods at all, Sasha seemed to be gloomier than ever, and Anna might actually have been sulking a little at her drums."
    "But my recent encounters with Kleio had perked my interest in her."
    "The singer's angriness now felt more like passion to me, her spikey demeanour making me ever more intrigued about her impetuous nature."
    show sasha angry at right
    sasha.say "Hey, [hero.name], what do you think?"
    show sasha annoyed
    "I stare at Sasha, not knowing what she means."
    "I was too busy watching how Kleio moves in front of the mic-stand to pay attention."
    mike.say "Huh?"
    show sasha angry
    sasha.say "Jesus, [hero.name], wake up! This is important!"
    show kleio angry at left
    kleio.say "Cut him some slack, Sasha - we're all fried from all this practicing."
    "I flash Kleio a brief smile as a way of saying thanks, and she returns it with an impish, knowing grin of her own."
    sasha.say "Okay, but listen to me this time, alright?"
    show sasha annoyed
    show kleio annoyed
    "I nod to signal that she should repeat her question."
    sasha.say "That last section, the one before the final chorus - I think we should go back to playing it how we used to."
    kleio.say "Yeah, right - that way always sucked, and I think we should change it, play it like I've been doing."
    sasha.say "You're the lead guitarist, [hero.name] - what do you think?"
    menu:
        "Side with Sasha":
            $ a = 1
            mike.say "If you always played it Sasha's way, maybe it's too late to go making changes?"
            show kleio angry
            kleio.say "Bullshit!"
            show sasha angry
            sasha.say "Two against one, Kleio - I win!"
            kleio.say "It was shit before and it's still shit now - we can't hope to win anything if we don't admit that and get better!"
            "Kleio tosses her guitar down, sending the stand toppling over and storms out onto the fire escape for a cigarette."
            $ kleio.love -= 5
        "Side with Kleio":
            $ a = 2
            mike.say "Kleio's way changes the whole feel of the song, makes it edgier - we need to stand out like that."
            show kleio happy
            kleio.say "YES!"
            show sasha angry
            sasha.say "We've always played it that way in the past...we don't have the time to learn a new section now."
            show kleio normal
            kleio.say "Majority rules, Sasha - I win!"
            "Kleio puts her guitar down and waltzes off to the fire escape for a victory smoke."
            $ kleio.love += 5
        "Ask Anna's opinion":
            $ a = 3
            mike.say "I liked both versions...but, Anna - what do you think?"
            show anna surprised at center with dissolve
            "Anna looks genuinely surprised to be asked, as if she's well used to being left out of discussions between Sasha and Kleio on such matters."
            show anna normal
            anna.say "I'm the same - I like both, so we could use some of one and some of the other, maybe?"
            "Kleio groans like she's being tortured and stomps off onto the fire escape for a cigarette."
            show sasha normal
            sasha.say "Okay, Anna...let's see if we can come to a compromise."
    hide anna
    hide kleio
    hide sasha
    "I follow Kleio out onto the fire escape, worried that she's mad, but also afraid of copping her wrath at the same time."
    show kleio
    "Hearing my footsteps, she turns round to regard me."
    "She leans against the railings, cigarette in one hand and blowing out a plume of smoke."
    if a == 1:
        mike.say "Sorry if I stamped on you in there, I just thought it was a better way to play the section."
        show kleio annoyed
        "Kleio's expression is typically surly and dismissive, but she sniffles slightly, making me wonder if I'd accidentally found a chink in her armour."
        kleio.say "Nah, don't apologise - I'm a big girl, I can take my lumps...I just thought that after..."
        "She lets the words fade into the air like the smoke from her cigarette, clearly hoping that I'd jump in."
        mike.say "After what, Kleio?"
        show kleio normal
        kleio.say "Nothing...nevermind...I was just being stupid there for a second."
    elif a == 2:
        kleio.say "Thanks for backing me up in there."
        kleio.say "Don't get me wrong - Sasha's a great bass player, but she's no guitar wizard, and that's a fact."
        mike.say "No problem - your way was clearly miles better."
        show kleio happy
        "Kleio laughs grittily thanks to the cigarette smoke in her mouth and closes the few feet between us."
        show kleio seductive
        "She wraps her arms around my neck and leans herself in closely."
        kleio.say "Seems I was wrong about you back when we first met - I'm really looking forward to collaborating with you more in the future...If you get me?"
        "For all of her radical posturing, I'm amazed to see how predictable Kleio can be when she gets what she wants and had her ego stroked in an agreeable way."
        if kleio.lesbian > 10:
            $ kleio.lesbian -= 1
    else:
        mike.say "Just wanted to check you're okay."
        show kleio annoyed
        "Kleio sniffles a little, and her eyes look a little red rimmed."
        "Has what just happened in the practice room really got to such a seemingly tough girl so much?"
        show kleio normal
        kleio.say "I'm fine...really."
        kleio.say "And it's fine too - Sasha and me having to compromise."
        mike.say "I'm sorry I dragged Anna into the argument, I just felt like it wasn't my right to make the casting vote."
        kleio.say "No, you're right...we're supposed to be a band, so everyone should have a say."
        kleio.say "I guess I'm just feeling a little stupid that you, of all people, had to remind me of that fact!"
        "Kleio surprises me by putting her arms around my waist and hugging me tightly, reminding me in turn of just how pleasant her body feels this close."
        if kleio.lesbian > 10:
            $ kleio.lesbian -= 1
    "We wait in silence as she finishes her cigarette, and then we go back inside."
    "All I can think as we walk through the door is how much Kleio keeps hidden and intrigue I feel for those depths of her personality."
    hide kleio
    return

label kleio_preg_talk:
    "It doesn't take me long to notice that Kleio's not her usual self."
    "With any other girl, it might show up as being sarcastic or prickly."
    "But Kleio can be both those things when she's in a good mood."
    "And so I notice it in her because she's being unusually quiet."
    "The last thing that I want is for her to be wrestling with something alone."
    "So I make an effort to broach the subject as soon as I feel the time is right."
    mike.say "Hey, Kleio..."
    mike.say "What's bugging you, huh?"
    show kleio normal
    kleio.say "Huh..."
    kleio.say "What are you talking about, Loverboy?"
    kleio.say "I'm fine, as always."
    "I give Kleio a slight frown."
    "And it's more than enough to let her know I'm not convinced."
    mike.say "Oh, Kleio."
    mike.say "You didn't even bother to drop a fuck in there!"
    mike.say "It's like you're not even trying to fool me."
    "Kleio opens her mouth to protest."
    "But then she seems to change her mind."
    "She sighs and shrugs."
    show kleio annoyed
    kleio.say "I guess you know me too well by now."
    kleio.say "Far too well to be taken in."
    kleio.say "Don't know if that's good or bad!"
    mike.say "Kleio..."
    mike.say "You're trying to change the subject!"
    "Kleio sighs for a second time."
    show kleio normal
    kleio.say "Okay, okay..."
    kleio.say "But this is going to be a real downer."
    kleio.say "I need to tell you something..."
    kleio.say "I need to tell you that I'm pregnant."
    "Kleio sounds so uncomfortable and forced as she says the words."
    "So much so that I don't think of doubting her for as much as a second."
    mike.say "Wow..."
    mike.say "I was not expecting that..."
    "Kleio makes a clucking noise with her tongue."
    "And then she nods, letting out a rueful laugh."
    show kleio annoyed
    kleio.say "So there."
    kleio.say "Now you know."
    kleio.say "Like I said - a real downer!"
    menu:
        "Let's keep the baby":
            "Kleio's wrong, dead wrong."
            "She just hasn't seen it yet, that's all."
            mike.say "It doesn't have to be, Kleio."
            mike.say "A downer, that is."
            show kleio surprised
            "Kleio looks at me in confusion."
            "She shakes her head as she does so."
            kleio.say "Wh...what are you saying?"
            kleio.say "That we should keep the baby?"
            mike.say "Why not, Kleio?"
            mike.say "I mean, I know all of the practical reasons not to."
            mike.say "But since when have you lived your life like that, huh?"
            show kleio annoyed
            kleio.say "Did you not hear what I said, Loverboy?"
            kleio.say "This isn't running off to play in a gig."
            kleio.say "It's a bit more serious than that!"
            mike.say "Of course I heard you, Kleio."
            mike.say "But I think this is something we can handle."
            mike.say "So long as we do it together - I think we can handle anything!"
            show kleio normal
            "Kleio doesn't seem to have a comeback for that."
            "Instead she just stares at me in silence for what feels like forever."
            "And when she does finally speak up, her voice is low and serious."
            kleio.say "Do you really mean that?"
            kleio.say "You...really want to have a kid...with ME?!?"
            "Now it's my turn to look confused and shake my head."
            mike.say "Kleio..."
            mike.say "What are you talking about?"
            mike.say "Of course I do."
            mike.say "I love you, for god's sake!"
            show kleio at center, zoomAt(1.65, (640, 1140))
            "Kleio nods and then leans her head on my shoulder."
            "I don't need to be told to wrap my arms around her."
            show kleio happy
            kleio.say "Oh, Loverboy..."
            kleio.say "I don't deserve a guy like you!"
            mike.say "Oh yes you do, Kleio."
            mike.say "Oh yes you do..."
            $ kleio.love += 10
            $ kleio.flags.toldpreg = True
        "Tell her to abort":
            "Kleio's right - this could put a downer on everything for us."
            "I mean, we couldn't organise using a damn condom."
            "So how on earth are we going to raise a child between us?"
            mike.say "Yeah, a real downer, Kleio."
            mike.say "We can't be parents."
            mike.say "We can hardly look after ourselves!"
            "Kleio nods at this."
            "But she still looks saddened by my response."
            show kleio sad
            kleio.say "You're right."
            kleio.say "That's just what I was thinking."
            kleio.say "I just..."
            kleio.say "I just wanted to hear you say it, that's all."
            "It sounds like Kleio wasn't as certain as she sounded at first."
            "But that doesn't change the fact that we can't start a family right now."
            mike.say "I think this is the right thing, Kleio."
            mike.say "Maybe we'll be ready to have kids in the future."
            mike.say "But here and now, we can't go through with it."
            show kleio at center, zoomAt(1.65, (640, 1140))
            "Kleio nods and then leans her head on my shoulder."
            "I don't need to be told to wrap my arms around her."
            "She needs all the support I can give her at a time like this."
            $ kleio.love -= 25
            $ kleio.unpreg()
    return

label kleio_meet_bree:
    "It's been one of those days, what with work and my studies all piling up."
    "What I need is to take a break, so I head straight to the pub and walk right in."
    "Almost as soon as I'm in there I can feel myself beginning to relax and unwind."
    "There's some decent music on the jukebox and the gentle hum of conversation in the air."
    "I grab a drink and then begin to scan the place for somewhere to sit my ass down."
    bree.say "Hey, [hero.name]!"
    bree.say "Come keep me company!"
    "I instantly recognise the sound of [bree.name]'s voice."
    show bree happy at top_mostleft with moveinleft
    "And then I see her walking towards me."
    hide bree with dissolve
    kleio.say "Oi, Loverboy!"
    kleio.say "What are you doing in here?"
    "A second later my head spins in the opposite direction."
    show kleio happy at top_mostright with moveinright
    "And I see Kleio elbowing her way over too."
    hide kleio with dissolve
    "I have no idea how I'm supposed to handle the situation."
    "I'm being approached from both sides by different girls."
    "And neither of them seems to have noticed the other's presence."
    bree.say "Why are you ignoring me?!?"
    kleio.say "Hey, dumb-ass, I'm talking to you!"
    "I take a step backwards."

    show bree at center, zoomAt(1, (-200, 730))
    show kleio a at center, zoomAt(1, (1420, 730))
    "Which lets them see each other for the first time."
    show bree surprised at flip, left
    show kleio surprised at right
    with ease
    bree.say "Oh!"
    kleio.say "Huh?!?"
    mike.say "[bree.name], meet Kleio."
    mike.say "Kleio, meet [bree.name]."
    "Both of the girls are understandably surprised."
    "But it doesn't take them long to figure the situation out."
    "Don't get me wrong, I'm not trying to flatter myself here."
    "But both of them were thinking that they'd have me to themselves."
    "Even if it was just for the sake of having a platonic drink with a friend."
    show bree annoyed
    show kleio annoyed
    "[bree.name] and Kleio seem to eye each other up like a couple of territorial cats."
    "Though it's [bree.name] that breaks the silence between them."
    show bree happy at flip, left5 with move
    bree.say "Kleio..."
    bree.say "You're one of the girls in Sasha's band, right?"
    "I see Kleio bristle at this."
    show kleio at right5 with move
    kleio.say "You mean we're in a band together."
    show bree normal
    show kleio angry
    kleio.say "It's not like it's Sasha's band!"
    show kleio normal
    kleio.say "So that makes you her housemate, yeah?"
    show bree annoyed
    bree.say "I...I guess so!"
    bree.say "I suppose Sasha's told you all about me!"
    kleio.say "Ah...she's dropped your name a couple of times."
    "[bree.name] blinks in surprise at Kleio's abrasive demeanour."
    "And I realise that she's not used to dealing with it like I am."
    "I need to step in here before Kleio says something we'll all regret!"
    show bree normal
    show kleio normal
    mike.say "Hey, I know..."
    mike.say "Let's grab a table together."
    mike.say "That way we can chat, yeah?"
    mike.say "All get to know each other better?"
    "I look from [bree.name] to Kleio, hoping for a positive response."
    show bree annoyed
    show kleio annoyed
    "But both of their faces looks distinctly unconvinced."
    show bree happy
    bree.say "Ah..."
    bree.say "I wondered if you wanted to play the arcade games with me?"
    bree.say "They have 'Bronze Chopper' over there!"
    "I look in the direction that [bree.name]'s pointing."
    "That does sound like a sweet deal!"
    show kleio angry
    kleio.say "Urgh..."
    show bree annoyed
    kleio.say "Boring!"
    show kleio normal
    kleio.say "I wanna shoot some pool, Loverboy!"
    "Kleio sticks a thumb over her shoulder, towards the vacant pool table."
    "And now I'm conflicted, as that sounds like fun too."
    "Especially the chance to see Kleio bending over the table!"
    show bree flirt at center, zoomAt(1.5, (340, 1040))
    show kleio a seductive at center, zoomAt(1.5, (940, 1040))
    bree.say "You want to play with me, right?"
    kleio.say "Nah, you wanna play with me - don't ya?"
    "Balls - looks like I'm going to have to choose one over the other!"
    menu:
        "Play with [bree.name]":
            "I really like the sound of playing pool with Kleio."
            "And sure, I can play games on the Zbox back home."
            "But it's just not the same as playing on a genuine, vintage arcade cabinet!"
            "Plus I get to play alongside bree too."
            mike.say "Maybe we can squeeze in a game of pool later, Kleio?"
            show bree happy
            mike.say "But first I need to pump some coins into that game!"
            show kleio annoyed
            "Kleio looks instantly annoyed by my choice."
            "She scowls and crossed her arms over her chest."
            $ kleio.love -= 20
            show kleio angry
            kleio.say "What?!?"
            kleio.say "Are you kidding me?"
            show bree flirt
            "[bree.name]'s reaction is a lot more dignified."
            "But I can still see the smugness in her smile."
            "She tosses her head, making her hair shimmer in the light."
            "And I swear that Kleio notes the way I stare at [bree.name]'s long, golden locks!"
            "Is she...is she actually jealous?"
            "No...no way."
            "This is Kleio we're talking about!"
            show bree happy
            bree.say "Come on, [hero.name]!"
            bree.say "I want to play until my wrists ache!"
            show kleio annoyed
            kleio.say "Whatever, whatever..."
            kleio.say "Forget you losers!"
            "I feel like I should say something to Kleio."
            hide kleio with moveoutright
            "But she's already walking off across the pub."
            "And when I turn around, [bree.name]'s already pumping coins into the machine."
            "So I hurry over to join her, soon forgetting all about Kleio."
            $ kleio.flags.chosenbree = True
        "Play with Kleio":
            "I really like the sound of playing some retro games with [bree.name]."
            "But I can play all the games I want on the Zbox back home."
            "And one thing we don't have back there is a pool table."
            "Or Kleio's ass!"
            mike.say "We can get some gaming in on the Zbox back home, [bree.name]."
            mike.say "Let's shoot some pool with Kleio while we're here, yeah?"
            "[bree.name] looks instantly disappointed with my choice."
            "But Kleio punches the air to celebrate."
            "She's never been gracious in victory or defeat!"
            show kleio happy
            show bree annoyed
            kleio.say "YES!"
            kleio.say "You know it makes sense!"
            kleio.say "Come on, I'll play the both of you!"
            $ bree.love -= 20
            show bree sad
            bree.say "Nah, I think I'll pass."
            bree.say "You guys have fun though."
            bree.say "And I'll see you back home later, [hero.name]."
            "I feel like I should say something to [bree.name]."
            hide bree with moveoutleft
            "But she's already walking off across the pub."
            "And when I turn around, Kleio's bent over as she racks up the balls."
            "So with an eyeful of that, I soon forget all about [bree.name]."
    return

label kleio_twintails_01:
    show kleio sad
    "I know Kleio pretty well by now, so all of her little quirks and habits are familiar to me."
    "But almost as soon as I see her today, I can tell that there's something up, something bothering her."
    "With most people they'll get snappy or evasive when their mind's on something else."
    "The problem is that Kleio's snarky and spikey the whole time anyway!"
    "So when she goes quiet and the constant flow of insults stops, it's a dead giveaway."
    mike.say "Ah, Kleio..."
    mike.say "Are you okay right now?"
    mike.say "You know, in general?"
    show kleio angry
    show fx anger
    kleio.say "WHAT?!?"
    kleio.say "What is that supposed to mean?"
    show kleio annoyed
    mike.say "I mean is there anything you want to talk about?"
    mike.say "Anything at all?"
    "Kleio snorts and shakes her head."
    show kleio angry
    kleio.say "Of course not!"
    kleio.say "What a dumb question!"
    "I hold my hands up and nod my head, letting the matter drop."
    show kleio sad
    "But I can see that Kleio's not doing the same thing herself."
    "She refuses to meet my eye, frowning as if she's about to say something."
    kleio.say "[hero.name]..."
    "Okay, here we go."
    "I know it's about to get serious when Kleio uses my real name!"
    mike.say "Yeah, Kleio..."
    kleio.say "I...I did want to talk about something."
    kleio.say "I wanted to ask you something."
    kleio.say "But it's gonna sound stupid, I just know it!"
    "Kleio opening up to me like this is super rare."
    "So I need to be careful and coax it out of her."
    mike.say "Okay, Kleio..."
    mike.say "I'll make a deal with you."
    mike.say "You ask your question."
    mike.say "And if it's stupid, we forget you ever asked it, okay?"
    mike.say "I promise you that I'll never mention it again."
    show kleio annoyed
    "Kleio looks at me sideways, still frowning a little."
    "But I can see that she's already softening to the idea."
    show kleio normal
    "And a moment later she nods in agreement."
    kleio.say "Okay, okay..."
    show kleio angry
    kleio.say "But don't say it's not stupid if it is, yeah?"
    kleio.say "Because I'll know you're lying!"
    mike.say "I'll be honest, Kleio."
    mike.say "Brutally honest, I promise!"
    show kleio normal
    "Kleio still doesn't look like she's one hundred percent convinced."
    "But all the same, she takes a deep breath and then asks her question."
    show kleio sad blush
    kleio.say "Do you..."
    kleio.say "Do you like long hair?"
    "Now it's my turn to frown, as that wasn't the question I expected."
    "I shake my head and shrug my shoulders as I search for a response."
    "And it has to be an honest one too, or else I'll be in trouble!"
    mike.say "I suppose so, Kleio."
    mike.say "I mean it looks kind of cool."
    mike.say "You think I should grow mine?"
    mike.say "Is that it?"
    show kleio angry
    kleio.say "No, you terminal moron!"
    kleio.say "I meant on girls!"
    kleio.say "Do you like long hair on girls?!?"
    show kleio normal
    "I look at Kleio, blinking in surprise."
    "And she stares back at me from beneath her short, choppy haircut."
    "It's hard to describe how strange her questions sounds to me."
    "But Kleio's so confident and sure of herself most of the time."
    "I'd never presume to tell her that she should change something about herself."
    show kleio angry
    kleio.say "Well?!?"
    kleio.say "Do you or don't you?!?"
    mike.say "Don't get me wrong, Kleio..."
    mike.say "Short hair looks great on a girl."
    mike.say "But long hair's kind of got that classic appeal, you know?"
    mike.say "Maybe it's a little more sophisticated?"
    show kleio normal -blush
    "I'm expecting Kleio to explode in a fit of temper."
    "But instead that, she looks thoughtful as she ponders my answer."
    kleio.say "Hmm..."
    kleio.say "Sophisticated, huh?"
    kleio.say "That's interesting...really interesting."
    "I keep on looking at Kleio as she says all of this."
    "And that's because I'm expecting another question."
    "Or at least that she's going to want me to expand on the point."
    "But instead, Kleio seems to be lost in her thoughts."
    "And so I do the best I can to forget about the matter."
    "Whatever's on Kleio's mind, she'll tell me when she's ready."
    "Or else she won't tell me at all."
    "Either way, I'm not going to poke the bear!"
    $ kleio.flags.haircutDelay = TemporaryFlag(True, 7, hook=[hook_set_flag, {"girl": kleio, "flag": "haircut", "value": True}])
    return

label kleio_twintails_02:
    scene expression f"bg {game.room}"
    "I know that girls are always getting pissed off with guys not noticing they've done something new with their hair."
    "But sometimes it's like a massive change in somebody's appearance can be so big that you don't see it at first."
    "It's like it's so massive that your brain just can't take it in, so instead it blots the change out for a while."
    show kleio happy
    "And that's why I totally fail to notice what's changed about Kleio the first time I lay eyes on her."
    "Sure, it's been a while since I saw her last."
    "And she's definitely trying to make me notice whatever's different - but of course she's pretending not to!"
    "But my brain just won't let me get to grips with it, no matter how hard I try."
    show kleio seductive
    kleio.say "Hey there, Loverboy!"
    kleio.say "Long time no see, huh?"
    "Kleio's smiling at me in the most suggestive manner possible."
    show kleio normal
    "And she raises her eyebrows as if she expects me to see it any second."
    mike.say "Hey, Kleio!"
    mike.say "It has been a little while, hasn't it?"
    mike.say "You're...ah...you're looking good!"
    "Kleio nods at this, still smiling."
    "But I can see in her eyes that she's urging me on to say more."
    "What in the hell can it be?"
    "What's changed since I saw her last?"
    "I try to look Kleio up and down without making it too obvious."
    "But everything seems to be how I remember it and in the same place too."
    show kleio annoyed at hshake
    "It's only when Kleio begins to get annoyed and shakes her head that I see it."
    "There's something moving up there that wasn't there before!"
    "Two high pigtails above her ears, which sway as she moves her head!"
    mike.say "Wow..."
    mike.say "Kleio..."
    mike.say "Your hair!"
    show kleio normal
    "A look of triumph flares in Kleio's eyes as I speak the words."
    "But again she does the best she can to hide her true emotions."
    "So when she speaks, it's with a practised tone of nonchalance."
    kleio.say "Oh, that?"
    kleio.say "You noticed, did you?"
    kleio.say "I wasn't gonna say anything, but now you know..."
    "Kleio makes a point of tossing her head around a little more."
    "This makes her hair swing around, catching the light in a golden cascade."
    "I can't hope to hide the fact that I'm impressed by what I'm seeing."
    "I mean, I thought Kleio was hot with short hair, sure."
    "But the change just makes me love the look of her even more!"
    mike.say "Wow, Kleio...just wow!"
    kleio.say "You like it, huh?"
    kleio.say "I dunno if I'm gonna keep it."
    kleio.say "Maybe I will and maybe I won't..."
    mike.say "You HAVE to keep it, Kleio!"
    show kleio happy
    "She smiles at my insistence, clearly liking how I'm acting."
    mike.say "But how did you do it, Kleio?"
    mike.say "It's not been that long since I saw you last!"
    mike.say "It's not a wig is it - or hair extensions?"
    show kleio angry
    show fx anger
    "Kleio looks instantly offended by the mere suggestion."
    "She frowns and shakes her head."
    kleio.say "The hell it is!"
    kleio.say "This is all me - one hundred percent natural!"
    mike.say "Your hair really grows that fast?!?"
    hide fx
    show kleio sad
    show fx drop
    "Now Kleio's starting to look a little unsure."
    kleio.say "W...well yeah!"
    kleio.say "Doesn't everybody's hair do that?"
    mike.say "No way, Kleio!"
    mike.say "It'd take mine months to grow that long!"
    mike.say "Whoa...you must have to get it cut like what, every week?"
    show kleio angry
    kleio.say "What if I do?!?"
    kleio.say "You make it sound like I'm some kind of freak!"
    "Sensing danger in the air, I decide to back off from the subject."
    "It's then that I remember how Kleio was looking at [bree.name]'s hair in the pub."
    "That and the odd way she asked me if I liked girls with long hair too."
    mike.say "Kleio..."
    mike.say "You didn't grow your hair to look more like [bree.name], did you?"
    show kleio surprised blush
    "Kleio curls her lip into a sneer and shakes her head."
    kleio.say "Huh?"
    kleio.say "[bree.name] who?"
    show kleio sad
    kleio.say "Oh...you mean little miss blondie bimbo?"
    kleio.say "Of course not - I'd forgotten she even existed!"
    mike.say "Okay, Kleio, if you say so."
    mike.say "I'm just saying it'd be okay if you did."
    show kleio annoyed -blush
    kleio.say "Well I didn't!"
    mike.say "That's okay too."
    show kleio normal
    kleio.say "You bet it's okay."
    "I'm trying not to laugh at Kleio's reaction."
    "She's really not as good at hiding her feelings as she thinks she is!"
    mike.say "Just for the record, Kleio."
    kleio.say "Yeah?"
    mike.say "Whatever the reason you chose to grow your hair."
    kleio.say "Uh-huh?"
    mike.say "I really like it."
    mike.say "It looks amazing."
    show kleio happy blush
    "There's no way Kleio can stop herself from blushing and smiling."
    "And as she does so, she looks more beautiful than ever."
    hide kleio
    hide expression f"bg {game.room}"
    return

label kleio_call_me_master:
    scene expression f"bg {game.room}"
    "When I first met Kleio, I could never had imagined that things would turn out this way."
    "I mean, she was such a fierce, feisty little bitch - more than a little scary to be around."
    "But that was before I got to know the real Kleio, the one that's underneath all the bravado."
    "And it was such a revelation to find out that she was really just covering up her true self."
    "Since we both came out about what we want from our relationship, she seems so much happier."
    "It's like she can finally stop pretending around me and be the person she really wants to be."
    "And I thought that we were already at the end of that particular journey."
    "That we'd reached a point where the both of us were more than happy."
    "This is until Kleio brings it up out of the blue..."
    show kleio normal at center, zoomAt(1.5, (640, 1040)) with dissolve
    kleio.say "[hero.name]..."
    kleio.say "I have something that I want to tell you."
    "I look up instantly the moment I hear this."
    "Well, wouldn't any sane guy do the same thing?"
    "It's like we're hard-wired to detect the slightest hint of dissatisfaction from a partner!"
    mike.say "What's that, Kleio?"
    mike.say "What did you want to say to me?"
    show kleio happy
    "Kleio smiles and shakes her head."
    "Clearly she notices the panic in my voice."
    show kleio normal
    kleio.say "Don't shit yourself, [hero.name]!"
    kleio.say "I'm not breaking up with your ass!"
    kleio.say "Not in a million fucking years is that gonna happen!"
    "I nod at this."
    "And I can already feel a flush of relief passing through my body."
    mike.say "Oh..."
    mike.say "Thank god, Kleio!"
    show kleio blush
    kleio.say "I'd never leave you, [hero.name]."
    kleio.say "That's what I wanted to tell you."
    kleio.say "That I've been so happy since I admitted that I wanted you to be my master."
    kleio.say "I feel like I don't have to worry about how people see me anymore."
    show kleio seductive
    kleio.say "None of that stuff matters, because all I have to worry about is pleasing you!"
    "Aw, geez..."
    "I always try to play the aloof and unflappable master at times like this."
    "But part of me wants to just let it all out and tell Kleio how much I love her too."
    "I mean, just look at her - she's practically perfect in every way."
    "And all she wants to do is devote herself to me!"
    mike.say "It makes me happy to hear you say that, Kleio."
    mike.say "And I'm more than proud to be your master."
    "Kleio nods at my words, eager to show her devotion."
    kleio.say "Oh yes...master!"
    kleio.say "I want to bow down to you alone."
    kleio.say "There's never going to be another master for me!"
    show kleio happy pat
    "I nod and smile, patting Kleio on the head."
    "She practically shivers at my touch, happier than ever."
    "In fact, I wouldn't be surprised to hear her purr like a satisfied cat."
    show kleio happy -pat
    "How rare is it that two people can be so perfectly happy together?"
    "Both of them finding in the other exactly what they need to make their lives complete?"
    "Now that has to be a real fairy tale romance, doesn't it?"
    $ kleio.flags.mikeNickname = "Master"
    $ kleio.sub += 2
    return

label kleio_sub_event_1:
    "Since Kleio started to really get into the idea of being submissive around me, things have really started to change."
    "For one thing, we don't have those same long debates that always turn into arguments about where to go and what to do."
    "These days, all I have to do is think of what I feel like doing when we're together and she simply goes along with it."
    "Which makes our time together SO much simpler and more enjoyable for me."
    "Like today, I want to get out of the house, but I can't be bothered to think up something to do."
    "Before I'd have suggested something and Kleio would have dug her heels in, finding any dumb reason to object."
    "But now it's quick, simple and pain-free!"
    mike.say "Kleio..."
    mike.say "Grab your shit!"
    mike.say "We're going for a drive, okay?"
    show kleio talkative
    kleio.say "Oh fuck..."
    kleio.say "Wait for me!"
    kleio.say "I'm coming, I'm coming - don't go without me!"
    show kleio normal
    "You see what I mean?"
    play sound car_door
    queue sound "<from 0 to 6.0>sd/SFX/vehicles/car_ignition.ogg"


    scene bg street night at center, zoomAt(1.25, (640, 530)), dark
    show car_inside_sit at center, zoomAt(1.5, (940, 1080))
    show kleio b casual shy at center, zoomAt(2.0, (640, 1340))
    with fade
    "No more than a couple of minutes after I speak the words, we're in the car."
    "Then we're off and driving down the road out of my neighbourhood."
    "I have no idea where we're going or for how long."
    "But the silence in the air is like music to my ears!"
    "And Kleio's sitting happily in the passenger seat, just watching the world go by."
    "I keep trying to look at the road ahead, to keep my attention on driving."
    "But every time I steal a look at Kleio, it gets harder to do."
    "It's not that she's trying to distract me - at least not at first."
    "She's just sitting there, looking so fucking hot!"
    "Pretty soon she begins to notice the trouble I'm having keeping my eyes off of her."
    show kleio a wink at center, zoomAt(1.0, (640, 1340)), stepback(0.5, 10.0, 10.0)
    "And like any good cock-tease, she starts to play up to my attentions."
    "Kleio begins to sigh and run her hands over her body."
    show kleio at center, zoomAt(1.0, (640, 1340)), stepback(0.5, 10.0, 10.0)
    "First her legs get this treatment, reminding me of their exquisite shape."
    "Then she moves upwards, stroking her flat belly with both hands."
    show kleio at center, zoomAt(1.0, (640, 1340)), stepback(0.5, 10.0, 10.0)
    "But when she pushes her breasts together and purses her lips, it's too much."
    play sound car_screeching_tires
    show kleio a surprised
    with hpunch
    "I almost lose control of the car, swerving across the road as I do so."
    with hpunch
    "Kleio gasps in shock and alarm as I battle to keep us from coming off the tarmac."
    show kleio a sadsmile
    "A moment later it's over, I have the car back under control and we're safe."
    "But my heart is still pounding in my chest."
    "And a quick sideways glance shows me that Kleio's still white as a sheet."
    "Neither of us seems to be enjoying the ride at the moment."
    "So I take the decision to pull over as soon as I can."
    "Seeing a secluded spot where I can park, I pull off the road."
    "I figure that we could both use a little time to calm down after our near-death experience."
    play sound "<from 2.0 to 10.0>sd/SFX/vehicles/car_ignition.ogg"
    "Turning off the engine, I turn to Kleio with a guilty look on my face."
    mike.say "Erm..."
    mike.say "Sorry about that, Kleio."
    mike.say "I guess I got a little distracted back there!"
    hide kleio
    show kleio a casual annoyed at flip, center, zoomAt(2.0, (640, 1340))
    "Kleio instantly begins to shake her head, dismissing my apology."
    kleio.say "Oh hell no!"
    kleio.say "That was totally my fault."
    kleio.say "How are you supposed to drive with me distracting you the whole time?"
    "I shrug, tyring to see it from the angle that Kleio's suggesting."
    "I mean, she was distracting me, that's for sure."
    "Maybe she's got a point?"
    mike.say "Ah..."
    mike.say "Okay, Kleio..."
    mike.say "Next time, don't act sexy enough to make me crash the car, okay?"
    show kleio a happy
    "Kleio giggles and flutters her eyelids at me."
    show kleio a shy
    kleio.say "You're not driving the car right now."
    kleio.say "So that must mean it's okay to be sexy, right?"
    "Kleio underlines the point by squeezing her breasts together again."
    "And as soon as she does so, I feel the panic and stress drain away."
    "In their place I can feel the same desire that almost saw us careen off the road."
    "But this time we're totally stationary, and there's nothing to distract me."
    mike.say "I guess not, Kleio."
    mike.say "And I can't think of a better way for you to apologise!"
    "I raise an eyebrow and pat my thighs."
    "And to make my intent clear, I nod towards my lap."
    show kleio a happy
    "Kleio giggles again, and then claps her hands together with glee."
    scene bg black
    show kleio carsex hurt at center, zoomAt(1.5, (450, 1080))
    with fade
    "She wastes no time in clambering out of her seat and over to me."
    show kleio carsex naked with hpunch
    "And as she sits down astride me, she hastily pulls off her top."
    "I gasp as those same breasts almost hit me in the face."
    "Sure, they looked good from the passenger seat."
    "But they look so much better an inch from the end of my nose!"
    "Without hesitation, I lean forwards."
    "And then I bury my face between them."
    "Some girls have way bigger tits than Kleio."
    "But as far as I'm concerned, you can keep them."
    "These are just the right size for me to be able to nuzzle at them."
    "I can go from one nipple to the other, with just a turn of my head."
    "Plus there's no danger of me being suffocated by them either!"
    show kleio carsex closed normal at startle (0.05, -10)
    "Kleio laughs with delight as I play with her chest."
    show kleio carsex hold
    "But at the same time I can feel what she's doing with her hands."
    show kleio carsex open
    "She's rubbing at my crotch, massaging my cock through my pants."
    "It feels really good, and I'm getting harder by the moment."
    "Looking up from between Kleio's breasts, I nod at her."
    mike.say "Okay, Kleio..."
    mike.say "Go ahead and help yourself."
    "Kleio nods eagerly, already doing as she's told."
    show kleio carsex at center, traveling(1.0, 0.5, (640, 720))
    "It doesn't take her long to pull my cock out of my pants."
    "As soon as it's free, Kleio gets straight to work."
    "She runs her hand up and down the shaft with one hand."
    "And she squeezes my balls with the other, just tight enough for it to feel good."
    mike.say "Oh yeah..."
    mike.say "That's amazing, Kleio!"
    kleio.say "Oh..."
    kleio.say "You deserve it...master!"
    kleio.say "But please...can I have it?"
    kleio.say "Will you put it inside of me?"
    "I can't help laughing at Kleio's desperate plea."
    "If feels good to know that she wants it so badly."
    "And it makes withholding it that much more enjoyable too!"
    mike.say "Show me how much you want it, Kleio."
    mike.say "Convince me it's the thing you want most in the world!"
    "Kleio gasps at the demand, pouting at not getting what she wants."
    "Then she bites her lip and begins to pant with desperation."
    show kleio carsex pleasure
    kleio.say "Oooh..."
    kleio.say "I want it SO much!"
    show kleio carsex normal
    kleio.say "It feels good in my hand."
    kleio.say "But it'd feel so much better inside of me!"
    kleio.say "I can almost feel it going in, feel it filling me up!"
    show kleio carsex hurt
    "Without warning I slide a hand into Kleio's shorts."
    "I use it to trace the line of her lips, feeling between the folds."
    "She gasps in surprise, wriggling in my lap."
    "Kleio's already hot and wet down there."
    "My fingers slip easily into her pussy a moment later."
    "I watch as she shuts her eyes and bites her lip."
    "And I just know that she's imagining me sinking into her!"
    mike.say "Okay, Kleio..."
    mike.say "You can have it!"
    kleio.say "Oh, thank you, master!"
    show kleio carsex hurt at center, traveling(1.0, 0.5, (640, 720))
    "With a dexterity that surprises me, Kleio strips off below the waist."
    "And then she's aiming my cock between her legs."
    "She whimpers as she lowers herself down onto it."
    "There's a moment when her body resists."
    show kleio carsex hurt closed fuck vaginal with fade
    "Then her lips part and she sinks slowly down onto me."
    show kleio carsex pleasure ahegao
    kleio.say "Oh god..."
    kleio.say "It's not like I imagined..."
    kleio.say "It's so much better!"
    show kleio carsex hurt closed
    "I hardly have to do a thing from that point on."
    show kleio carsex at startle (0.05, -10)
    "Kleio plants her hands on my shoulders and starts to ride my cock in earnest."
    show kleio carsex at startle (0.05, -10)
    "She works herself up and down, moaning with pleasure the whole time."
    show kleio carsex hand
    "This leaves my hands free to explore the rest of her body."
    "And I take full advantage, kissing, squeezing, licking and biting."
    "Kleio nods eagerly at my efforts, still riding me hard."
    show kleio carsex normal at startle (0.05, -10)
    kleio.say "Y...yeah..."
    kleio.say "Play with me, master..."
    kleio.say "I'm all yours...every bit of me!"
    show kleio carsex open hurt at startle (0.05, -10)
    "Then Kleio's eyes open wide and she stiffens against me."
    show kleio carsex normal at startle (0.05, -10)
    kleio.say "I'm gonna cum..."
    kleio.say "I can't take it..."
    show kleio carsex ahegao pleasure at startle (0.05, -10)
    kleio.say "Gonna cum..."
    show kleio carsex -vaginal with vpunch
    "At the last moment I tear my cock out of Kleio."
    with vpunch
    "She wails as the sensation makes her cum that much more quickly."

    show kleio carsex cumshot with vpunch
    "And then I cum too, shooting my load onto her body!"
    show kleio carsex -cumshot bodycum
    "Suddenly there's the sound of tires scraping on gravel."
    with vpunch
    mike.say "SHIT!"
    mike.say "Kleio, get dressed!"
    mike.say "There's someone pulling in behind us!"


    scene bg street night at center, zoomAt(1.25, (640, 530)), dark
    show car_inside_sit at center, zoomAt(1.5, (640, 1080))
    show layer master at police_lights
    with fade
    "I glance into the rear-view mirror and feel my heart sink."
    mike.say "Oh great, it's the fucking police!"
    "Kleio does as she's told, tumbling back onto the passenger seat."
    "Luckily for us she wasn't wearing much to begin with."
    "And all I need to do is stuff my cock back into my pants."
    "So by the time the officer is out of her car, we're just about presentable."
    play sound car_window_open
    scene bg taxi night zorder 1 at center, zoomAt(1.25, (640, 780))
    show car_inside_window zorder 3 at blacker
    show layer master at police_lights
    with fade
    show camila work zorder 2 at center, zoomAt(1.5, (640, 800)) with easeinleft
    "Officer" "Mind telling me what you're doing pulled over, sir?"
    mike.say "Erm..."
    mike.say "We were just checking the map, officer."
    mike.say "But we're fine now, ready to be on our way."
    "I see her gaze fall on Kleio and her jaw drop."
    scene bg street night at center, zoomAt(1.25, (640, 530)), dark
    show car_inside_sit at center, zoomAt(1.5, (940, 1080))
    show kleio a casual annoyed at flip, center, zoomAt(2.0, (640, 1340))
    show cassidy_facecum_b at flip, center, zoomAt(2.0, (630, 1340))
    show layer master at police_lights
    with fade
    "Looking over there too, I feel a rising sense of panic."
    "Officer" "Ah, madam..."
    "Officer" "You have a little something on your face!"
    show kleio a stuned
    "Kleio glances in the mirror, seeing the cum streaking her features."
    show kleio a annoyed blush
    "She looks back a the officer, blushing with embarrassment."
    "But she still manages to reply."
    show kleio a shy
    kleio.say "It's...just face cream, officer."
    kleio.say "I was putting it on while we checked the map."
    "The officer nods and starts to back away."
    play sound car_window_close
    "I have no idea if she believed Kleio or not."
    "But she doesn't look inclined to ask anymore questions."
    play sound car_ignition
    scene bg street night at center, zoomAt(1.25, (640, 530)), dark
    show car_inside_sit at center, zoomAt(1.5, (940, 1080))
    show kleio b casual happy blush at center, zoomAt(2.0, (640, 1340))
    with fade
    "As she pulls away, I start the engine and get ready to drive back home."
    "But not before I find a packet of paper tissues in the glove-box for Kleio."
    scene bg black with dissolve
    pause 0.3
    stop sound
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
