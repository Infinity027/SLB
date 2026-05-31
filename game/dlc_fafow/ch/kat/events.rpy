init python:
    Event(**{
    "name": "kat_event_01",
    "label": "kat_event_01",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "duration": 1,
    "conditions": [
        IsDone("bree_event_11"),
        HeroTarget(
            IsGender("male"),
            IsRoom("arcade"),
            ),
        PersonTarget(kat,
            MinStat("love", 20),
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kat_event_02",
    "label": "kat_event_02",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "duration": 1,
    "conditions": [
        IsDone("kat_event_01"),
        Or(
            And(
                IsHour(7, 18),
                HeroTarget(
                    IsRoom("mall1", "mall2"),
                    Not(OnDate()),
                    ),
                ),
            And(
                IsHour(20, 0),
                HeroTarget(
                    Or(
                        IsRoom("cinema"),
                        HasRoomTag("pub"),
                        ),
                    Not(OnDate()),
                    ),
                ),
            ),
        PersonTarget(kat,
            MinStat("love", 40),
            Not(IsPresent()),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kat_event_03",
    "label": "kat_event_03",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "duration": 0,
    "conditions": [
        IsDone("kat_event_02"),
        IsHour(14, 17),
        HeroTarget(IsRoom("date_amusement")),
        PersonTarget(kat,
            MinStat("love", 60),
            OnDate(),
            ),
        ],
    "do_once": True,
    })

    AfterDateEvent(**{
    "name": "kat_event_04",
    "label": "kat_event_04",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "conditions": [
        IsDone("kat_event_03"),
        MinDateScore(90),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(kat,
            MinStat("love", 80),
            OnDate(),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kat_event_05",
    "label": "kat_event_05",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "duration": 0,
    "conditions": [
        IsDone("kat_event_04"),
        IsHour(10, 16),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("street"),
            Not(OnDate()),
            ),
        PersonTarget(kat,
            MinStat("love", 100),
            ),
        ],
    "do_once": True,
    })

    AfterDateEvent(**{
    "name": "kat_event_06",
    "label": "kat_event_06",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "conditions": [
        IsDone("kat_event_05"),
        MinDateScore(80),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(kat,
            OnDate(),
            MinStat("love", 120),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kat_event_07",
    "label": "kat_event_07",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "duration": 1,
    "conditions": [
        IsDone("kat_event_06"),
        IsHour(14, 17),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("street"),
            Not(OnDate()),
            ),
        PersonTarget(kat,
            MinStat("love", 140),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kat_event_08",
    "label": "kat_event_08",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "duration": 1,
    "conditions": [
        IsDone("kat_event_07"),
        HeroTarget(
            IsGender("male"),
            OnDate(),
            ),
        PersonTarget(kat,
            MinStat("love", 150),
            OnDate(),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kat_event_08a",
    "label": "kat_event_08a",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "duration": 1,
    "conditions": [
        IsDone("kat_event_08"),
        HeroTarget(
            IsGender("male"),
            OnDate(),
            ),
        PersonTarget(kat,
            MinStat("love", 160),
            IsFlag("agree_sex_cam", True),
            OnDate(),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kat_event_08b",
    "label": "kat_event_08b",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "duration": 1,
    "conditions": [
        IsDone("kat_event_08"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(HasRoomTag("work")),
            Not(HasRoomTag("home")),
            ),
        PersonTarget(kat,
            MinStat("love", 160),
            IsFlag("agree_sex_cam", False),
            Not(OnDate()),
            Not(IsPresent()),
            ),
        ],
    "chances": 25,
    "do_once": True,
    })

    Event(**{
    "name": "kat_event_08c",
    "label": "kat_event_08c",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "duration": 1,
    "conditions": [
        IsDone("kat_event_08b"),
        HeroTarget(
            IsGender("male"),
            OnDate(),
            ),
        PersonTarget(kat,
            IsFlag("confront_sex_cam", True),
            OnDate(),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kat_event_09",
    "label": "kat_event_09",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "duration": 1,
    "conditions": [
        Or(
            IsDone("kat_event_08a"),
            IsDone("kat_event_08b"),
            ),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("street"),
            Not(OnDate()),
            ),
        PersonTarget(kat,
            MinStat("love", 180),
            IsFlag("confront_sex_cam", False),
            Not(IsPresent()),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kat_event_10",
    "label": "kat_event_10",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "duration": 1,
    "conditions": [
        IsDone("kat_event_09"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(HasRoomTag("work")),
            Not(HasRoomTag("home")),
            ),
        PersonTarget(kat,
            MinStat("love", 200),
            Not(IsPresent()),
            ),
        ],
    "chances": 50,
    "do_once": True,
    })

    Event(**{
    "name": "kat_kink_01",
    "label": "kat_kink_01",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "duration": 1,
    "conditions": [
        IsDone("kat_event_01"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_livingroom"),
            IsActivity("date_play_console"),
            ),
        PersonTarget(kat,
            MinStat("sub", 10),
            MinStat("love", 80),
            OnDate(),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kat_kink_02",
    "label": "kat_kink_02",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "duration": 1,
    "conditions": [
        IsDone("kat_kink_01"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_pub"),
            Or(
                IsActivity("buy_a_round"),
                IsActivity("offer_a_drink"),
                ),
            ),
        PersonTarget(kat,
            MinStat("sub", 20),
            MinStat("love", 100),
            OnDate(),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kat_kink_03",
    "label": "kat_kink_03",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "duration": 1,
    "conditions": [
        IsDone("kat_kink_02"),
        HeroTarget(
            IsGender("male"),
            IsActivity("kiss"),
            ),
        PersonTarget(kat,
            MinStat("sub", 40),
            MinStat("love", 120),
            MinFlag("kiss", 4),
            IsActive(),
            IsPresent(),
            ),
        ],
    "do_once": True,
    })

    InteractEvent(**{
    "name": "kat_kink_04",
    "label": "kat_kink_04",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "duration": 1,
    "conditions": [
        IsDone("kat_kink_03"),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(kat,
            MinStat("sub", 60),
            MinStat("love", 130),
            IsActive(),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kat_kink_05",
    "label": "kat_kink_05",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "duration": 1,
    "conditions": [
        IsDone("kat_kink_04"),
        MinDateScore(50),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(kat,
            MinStat("sub", 80),
            MinStat("love", 150),
            OnDate(),
            ),
        ],
    "do_once": True,
    })

    InteractEvent(**{
    "name": "kat_kink_06",
    "label": "kat_kink_06",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "duration": 1,
    "conditions": [
        IsDone("kat_kink_05"),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(kat,
            MinStat("sub", 100),
            IsActive(),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kat_jack_01",
    "label": "kat_jack_01",
    "duration": 2,
    "conditions": [
        IsDone("kat_event_02"),
        IsHour(10, 16),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("street"),
            ),
        PersonTarget(kat,
            MinStat("love", 60),
            Not(IsPresent()),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kat_jack_02",
    "label": "kat_jack_02",
    "duration": 2,
    "conditions": [
        IsDone("kat_jack_01"),
        IsHour(10, 16),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("street"),
            ),
        PersonTarget(kat,
            MinStat("love", 100),
            Not(IsPresent()),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kat_jack_03",
    "label": "kat_jack_03",
    "duration": 2,
    "conditions": [
        IsDone("kat_jack_02"),
        IsHour(10, 16),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("street"),
            ),
        PersonTarget(kat,
            MinStat("love", 120),
            MinStat("sub", 20),
            Not(IsHidden()),
            ),
        PersonTarget(jack,
            IsFlag("will_meet_kat", True),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kat_jack_04",
    "label": "kat_jack_04",
    "duration": 2,
    "conditions": [
        IsDone("kat_jack_03"),
        IsHour(8, 17),
        HeroTarget(
            IsGender("male"),
            IsRoom("coffeeshop"),
            ),
        PersonTarget(kat,
            MinStat("love", 135),
            MinStat("sub", 20),
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kat_jack_05",
    "label": "kat_jack_05",
    "duration": 2,
    "conditions": [
        IsDone("kat_jack_04"),
        IsHour(10, 16),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("street"),
            ),
        PersonTarget(kat,
            MinStat("love", 140),
            MinStat("sub", 50),
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "kat_jack_06",
    "label": "kat_jack_06",
    "display_name": "Jack's idea",
    "icon": "button_jack",
    "duration": 2,
    "conditions": [
        IsDone("kat_jack_05"),
        HeroTarget(
            IsGender("male"),
            IsRoom("arcade"),
            ),
        PersonTarget(kat,
            MinStat("love", 145),
            MinStat("sub", 50),
            IsActive(),
            ),
        PersonTarget(jack,
            IsFlag("ready_kat_jack_threesome", True),
            ),
        ],
    "do_once": True,
    })

    CallEvent(**{
    "name": "kat_jack_07",
    "label": "kat_jack_07",
    "duration": 3,
    "conditions": [
        IsDone("kat_jack_06"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            ),
        PersonTarget(kat,
            ContactKnown(),
            MinStat("love", 160),
            MinStat("sub", 75),
            Not(IsPresent()),
            IsActive(),
            Not(IsActivity("sleep")),
            IsFlag("agree_kat_jack_threesome", True),
            ),
        PersonTarget(bree,
            Or(
                Not(HasRoomTag("home")),
                IsHidden(),
                IsGone(),
                ),
            ),
        PersonTarget(sasha,
            Or(
                Not(HasRoomTag("home")),
                IsHidden(),
                IsGone(),
                ),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kat_jack_08",
    "label": "kat_jack_08",
    "duration": 0,
    "conditions": [
        IsDone("kat_jack_07"),
        HeroTarget(
            IsGender("male"),
            Or(
                HasRoomTag("street"),
                HasRoomTag("park"),
                HasRoomTag("mall_southside"),
                ),
            ),
        PersonTarget(kat,
            MinStat("love", 180),
            Not(IsHidden()),
            Not(IsPresent()),
            ),
        ],
    "do_once": True,
    })


    Event(**{
    "name": "jack_kat_special",
    "label": "jack_kat_special",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "conditions": [
        IsHour(10, 16),
        IsDone("kat_jack_07"),
        IsNotDone("jack_kat_special"),
        Or(
            IsNotDone("kat_jack_08"),
            And(
                IsDone("kat_jack_08"),
                PersonTarget(jack,
                    IsFlag("trouple_wedding", True),
                    ),
                ),
            ),
        PersonTarget(kat,
            ContactKnown(),
            MinStat("love", 160),
            MinStat("sub", 75),
            Not(IsPresent()),
            IsFlag("agree_kat_jack_threesome", True),
            ),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        ],
    "duration": 3,
    "do_once": False,
    "once_day": True,
    })


    Event(**{
    "name": "kat_preg_talk",
    "max_girls": 1,
    "label": "kat_preg_talk",
    "do_once": False,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(kat,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("toldpreg", False),
            MinCounter("pregnant", 6),
            ),
        ],
    "music": "music/roa_music/buddy.ogg",
    })

    InteractActivity(**{
    "name": "kat_vibrator_restaurant",
    "label": "kat_vibrator_restaurant",
    "duration": 1,
    "display_name": "Have fun with Kat",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            OnDate(),
            IsRoom("date_restaurant"),
        ),
        PersonTarget(kat,
            IsActive(),
            OnDate(),
            MinStat("sub", 60),
            MinStat("love", 130),
            ),
        ],
    "icon": "vibrate",
    "once_day": True,
    })

    Activity(**{
    "name": "challenge_kat",
    "label": "challenge_kat",
    "display_name": "Challenge Kat",
    "icon": "playarcade",
    "rooms": "date_mall1",
    "fun": 2,
    "money_cost": 25,
    "conditions":[
        PersonTarget(kat,
            OnDate(),
            "kat.sub.max < 10",
            ),
        ],
    "once_week": True,
    })

label challenge_kat:
    show kat surprised
    mike.say "You know what Kat?"
    mike.say "I think it's time for a d-d-d-duel!"
    show kat defiant
    kat.say "Oh yeah?"
    kat.say "You want your ass beat again?"
    mike.say "You won't beat me anymore!"
    mike.say "Prepare to lose!"
    scene bg arcade
    show kat defiant
    with fade
    if hero.knowledge >= 50 and hero.flags.video_games_played >= 15:
        "I am confident going into the match as I have learn new old-school tricks."
        show kat surprised
        "And as soon as we're into it, Kat gets a nasty surprise."
        "She'd be good, but everything that she tries, I have an answer for."
        show kat angry
        "Kat's really clued up on playing the game."
        "Yet she's got no idea about the oldest and most obscure tactics."
        "And so they catch her totally off-guard."
        "I can hear her gasping and groaning as I out-play her."
        "But nothing that she does seems to help."
        "Because I'm handing Kat her ass in spectacular fashion!"
        show kat shocked
        "The bout ends as the head of Kat's character head explodes in a shower of blood, bone and brain matter."
        mike.say "YES!"
        mike.say "Ultimate Brutality!"
        "I feel totally energised by the win."
        "But my wrists feel like I have arthiritis or something!"
        show kat angry
        "Kat looks pissed at having lost."
        "But she makes a visible effort to smile through it."
        kat.say "Erm..."
        kat.say "Well played, [hero.name]..."
        kat.say "Maybe you're not so bad after all."
        "Even though it's a half-hearted admission, it's enough for me."
        mike.say "You're not too shabby yourself, Kat."
        mike.say "Told you I won't let you win again!"
        if kat.sub.max < 10:
            $ kat.sub.max = 10
    else:
        "I am confident going into the match."
        "But as soon as we're into it, I get a nasty surprise."
        "Everything that I try, Kat seems to have an answer for."
        "Even the oldest and most obscure tactics I have don't work."
        "It's almost like she has me totally scouted."
        "Like she's been watching every match I've played."
        "Kat hands my ass to me in spectacular fashion."
        "The bout ends as my character's head explodes in a shower of blood, bone and brain matter."
        show kat crazy
        kat.say "YES!"
        kat.say "Ultimate Brutality!"
        "Once again I feel totally humiliated by the loss."
        "Plus my wrists feel like I have arthiritis or something!"
        "But all the same, I do my best to suck it up and put on a smile."
        show kat normal
        mike.say "Ah..."
        mike.say "Well done, Kat..."
        mike.say "You beat me one more..."
        show kat smile
        "Even though it's a half-hearted admission, it seems to do the trick."
        "Kat drops a little of her swagger as she gives me a smile."
        kat.say "Cheer up, [hero.name]..."
        kat.say "You're not so bad yourself."
        show kat defiant
        kat.say "But I doubt you'll ever be able to beat me!"
        $ game.active_date.score += 30
    $ hero.flags.video_games_played += 1
    return

label kat_event_01:
    if kat.love.max < 40:
        $ kat.love.max = 40
    scene bg arcade
    "Normally when I'm down at the local arcade, it's just for the sake of hanging out."
    "Well, that and the chance to play some seriously sweet retro games too."
    "But today's a little different, because the arcade's hosting a special event."
    "And that's a knockout tournament for the one and only Ultimate Gore Fighter!"
    "It was one of my absolute favourite arcade games as a kid, a real coin-guzzler."
    "And I think that remember enough to be able to have a damn good chance of winning the whole thing."
    "As soon as I walk into the place, I'm presented with a long row of the old-school UGF arcade cabinets."
    "And just the sight of them takes me right back to my childhood."
    "Seriously, I can almost feel my wrists aching from all the time I spent playing back in the day!"
    "I don't waste any time in signing up for the tournament."
    show jack as gamer1 zorder 1 at left4, blacker
    show ryan as gamer2 zorder 2 at right5, blacker
    show scottie as gamer5 zorder 3 at flip, left, blacker
    show sasha as gamer3 zorder 4 at flip, mostright5, blacker
    show alexis b as gamer4 zorder 5 at flip, mostleft5, blacker
    show kat zorder 6 at center, blacker
    with dissolve
    "But the whole time I'm also looking around, trying to scout my competition."
    "Sure, there are a couple of familiar faces here and there."
    "Though none of them are players that I really know that well."
    "And then I see her, already standing in front of an arcade cabinet."
    hide kat
    show kat zorder 6 at center, dark
    with dissolve
    "It's Kat, the gamer girl that seems to keep popping up everywhere!"
    "Part of me wants to act like I haven't seen her at all."
    "To just walk over to where my first opponent is waiting for me."
    "But that part of me loses out to the one that's intrigued to see Kat here."
    "The same part of me that keeps on reminding me of just how cute she is."
    "So I find myself wandering over while trying to look casual."
    "You know, like walking towards her and looking like I'm not."
    hide kat
    show kat zorder 6 at center, zoomAt(1.5, (640, 1040))
    kat.say "Hey, [hero.name]!"
    kat.say "You entering the tournament too?"
    with vpunch
    "I almost leap out of my skin as Kat says hello."
    "And that's because she does it without even turning around."
    mike.say "Huh?"
    mike.say "How did you..."
    show kat smile
    "Kat lets out a peal of laughter as she finally looks back over her shoulder at me."
    "And then she taps the screen of the arcade cabinet with the tip of her finger."
    kat.say "You're not a vampire, [hero.name]!"
    kat.say "I can totally see you in the glass!"
    "I can feel myself starting to blush with embarrassment."
    "And it looks like my encounter with Kat is off to a typically cringe-worthy start."
    mike.say "Ah...yeah..."
    mike.say "Of course!"
    mike.say "And I am, by the way..."
    mike.say "Entering the tournament, that is!"
    show kat normal
    "Kat nods and seems to be genuinely pleased to hear it."
    kat.say "That's great news."
    kat.say "At least there's one other player in the thing that's up to scratch."
    show kat annoyed
    kat.say "My first opponent was a total loser - no skills at all!"
    mike.say "Well that's not me, Kat."
    mike.say "I'm a UGF veteran!"
    show kat smile
    kat.say "Brilliant, [hero.name]."
    show kat defiant
    kat.say "That means when I beat you, it'll really mean something!"
    "I can't help frowning at what Kat just said."
    "I mean, how arrogant is she?"
    mike.say "What do you mean by that, Kat?"
    mike.say "You make it sound like you've already got me beaten!"
    show kat happy
    kat.say "Oh come on, [hero.name]..."
    kat.say "Like you even stand a chance against me!"
    kat.say "But don't worry about it."
    show kat defiant
    kat.say "I promise I'll do all I can to make you look good."
    kat.say "Before I destroy you, that is!"
    "I take a step backwards and shake my head."
    "I know that this is only a tournament at the local arcade."
    "But I do the best I can to sound like I'm totally serious."
    mike.say "Don't start celebrating just yet, Kat."
    mike.say "Because I just might have a surprise in store for you!"
    "Kat doesn't dignify that with an answer."
    "Instead she cocks her head to one side and raises one eyebrow."
    "Then she gives me a cocky wave as I head off to find my first opponent."
    hide kat with fade
    "I guess that Kat's arrogant assumption that she'll win must have lit a fire under me."
    "Because as soon as I start playing, I'm tearing my foes apart."
    "Almost every match I have ends with me scoring a brutality on my foes too."
    show kat surprised zorder 6 at center, zoomAt(1.5, (640, 1040))
    "But then I look up and see that my next opponent is Kat."
    "I guess it was just fated for things to go down this way."
    show kat defiant
    "The two best players in the game clashing."
    "And only the strongest will survive the encounter!"
    kat.say "Thanks for dealing with all those other losers for me, [hero.name]."
    kat.say "But now you've kind of outlived your usefulness."
    kat.say "So I'm going to have to put you out of your misery!"
    mike.say "Don't be so sure, Kat."
    mike.say "I like to save the easiest prey until last!"
    mike.say "Come on - let's do this!"
    if hero.knowledge >= 50 and hero.flags.video_games_played >= 15:
        "I'm not dumb enough to take Kat lightly."
        "Because I know she's a great gamer in her own right."
        "But I am confident going into the match."
        "As I have a whole load of old-school tricks up my sleeve."
        show kat surprised
        "And as soon as we're into it, Kat gets a nasty surprise."
        "I thought that she'd be good, and she really is."
        "But everything that she tries, I have an answer for."
        show kat angry
        "Kat's really clued up on playing the game."
        "Yet she's got no idea about the oldest and most obscure tactics."
        "And so they catch her totally off-guard."
        "I can hear her gasping and groaning as I out-play her."
        "But nothing that she does seems to help."
        "Because I'm handing Kat her ass in spectacular fashion!"
        show kat shocked
        "The bout ends as the head of Kat's character head explodes in a shower of blood, bone and brain matter."
        mike.say "YES!"
        mike.say "Ultimate Brutality!"
        "I feel totally energised by the win."
        "But my wrists feel like I have arthiritis or something!"
        show kat angry
        "Kat looks pissed at having lost."
        "But she makes a visible effort to smile through it."
        kat.say "Erm..."
        if kat.sub.max < 10:
            $ kat.sub.max = 10
        $ kat.sub += 2
        $ kat.love -= 2
        kat.say "Well played, [hero.name]..."
        kat.say "Maybe you're not so bad after all."
        "Even though it's a half-hearted admission, it's enough for me."
        mike.say "You're not too shabby yourself, Kat."
        mike.say "Even if you are the second best player here!"
    else:
        "I'm not dumb enough to take Kat lightly."
        "Because I know she's a great gamer in her own right."
        "But I am confident going into the match."
        "As I have a whole load of old-school tricks up my sleeve."
        "Yet as soon as we're into it, I get a nasty surprise."
        "Everything that I try, Kat seems to have an answer for."
        "Even the oldest and most obscure tactics I have don't work."
        "It's almost like she has me totally scouted."
        "Like she's been watching every match I've played."
        "But that can't be the case."
        "As I know she was playing her own matches at the time."
        "In the end it doesn't matter how she managed to do it."
        "Kat hands my ass to me in spectacular fashion."
        "The bout ends as my character's head explodes in a shower of blood, bone and brain matter."
        show kat crazy
        kat.say "YES!"
        kat.say "Ultimate Brutality!"
        "I feel totally humiliated by the loss."
        "Plus my wrists feel like I have arthiritis or something!"
        "But all the same, I do my best to suck it up and put on a smile."
        show kat normal
        mike.say "Ah..."
        mike.say "Well done, Kat..."
        mike.say "I guess you are pretty good after all."
        show kat smile
        "Even though it's a half-hearted admission, it seems to do the trick."
        "Kat drops a little of her swagger as she gives me a smile."
        kat.say "You know what, [hero.name]..."
        $ kat.love += 4
        kat.say "You're not so bad yourself."
        show kat defiant
        kat.say "Even if you are the second best player here!"
    $ hero.flags.video_games_played += 1
    return

label kat_event_02:
    if kat.love.max < 60:
        $ kat.love.max = 60
    show jack smile
    "As soon as I see Jack, I just know that he's got something he's desperate to show me."
    "And that's because he has the same kind of manic energy you usually only see in kids on a sugar-rush."
    "I know from long experience that he always gets like this when he's found something new."
    "Something that really excites him or gets his motor running."
    mike.say "Hey, Jack..."
    mike.say "What is it this time?"
    show jack happy
    jack.say "Hey, [hero.name]..."
    show jack surprised
    jack.say "I...wait..."
    jack.say "How did you know I wanted to show you something?"
    "I roll my eyes and wave away Jack's question."
    "Because he probably wouldn't believe me if I explained it to him."
    mike.say "Never mind that."
    mike.say "Just show me what you have to show me, okay?"
    show jack normal
    "Luckily for me, when Jack's like this he has a very short attention span too."
    "Well, at least he does when it comes to anything that isn't his current obsession."
    "So as soon as I mention it, he forgets all about my ability to read him like a book."
    show jack normal
    jack.say "Oh yeah!"
    jack.say "Wait until you see this..."
    jack.say "She's so amazing, I swear you're going to freak!"
    scene expression f"bg {game.room}" at dark
    show jack normal zorder 1 at dark, center, zoomAt(1.1, (340, 740))
    show streaming stream title smile zorder 2 at center, zoomAt(1.0, (640, 520))
    show streaming_phone zorder 3 at center, zoomAt(1.0, (640, 520))
    with fade
    "Jack pulls his phone out and proceeds to pull up a video on it."
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(animated_glitch, offset=3)
    "But even as he does so, I have a pretty good idea of where this is going."
    show streaming start normal
    "The fact that he mentioned it involves someone of a female persuasion explains it all."
    "Because Jack's also notorious for developing crushes on girls at the drop of a hat!"
    "So when I see that the video's of a girl, I know instantly that I was right."
    show jack happy
    jack.say "Check her out, [hero.name]..."
    jack.say "Isn't she awesome?!?"
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(animated_glitch, offset=3)
    "At first I'm not too blown away by what I'm seeing."
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming game normal at functools.partial(animated_glitch, offset=3)
    "The video's obviously a recording of a live-stream."
    show streaming happy
    "The girl that Jack's totally into is playing a game that looks familiar."
    "But as I watch a little longer and look a little closer, I realise something."
    show streaming normal
    "It's not just the game that's familiar, the girl is too!"
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(animated_glitch, offset=3)
    "As soon as I get a good look at her face, that confirms it."
    "The streamer that Jack's so interested in is Kat!"
    show jack normal
    jack.say "Well?"
    jack.say "What do you think?"
    hide expression f"bg {game.room}"
    show expression f"bg {game.room}"
    show jack normal zorder 1 at center, zoomAt(1.1, (340, 740))
    with dissolve
    hide streaming
    hide streaming_phone
    with easeoutbottom
    jack.say "Because I know what I think..."
    show jack perv at center, zoomAt(1.1, (640, 740)) with ease
    jack.say "I'm in love!"
    menu:
        "You know her too?":
            "I really should tell Jack that I've met Kat."
            "He looks so high on the mere sight of her."
            "And if he finds out that I kept that fact from him..."
            "Well, he could think I'm trying to keep him away from her!"
            mike.say "She's called Kat, right?"
            show jack surprised at startle
            "Jack's head snaps around at the mention of Kat's name."
            "And I see his eyes narrow as he studies me."
            show jack sad
            jack.say "Wait a minute..."
            jack.say "How did you know that?"
            "I shrug and shake my head."
            "Trying to make out that it's no big deal."
            mike.say "I've met her in person, at a gaming tournament."
            mike.say "[bree.name] and I played against her and some other guy."
            "Jack's still looking at me with suspicion in his eyes."
            "Then he shakes his head too."
            show jack angry
            jack.say "Bullshit, [hero.name]..."
            jack.say "I don't believe a word of it!"
            "I can't help laughing at what Jack just said."
            mike.say "What are you talking about, Jack?"
            mike.say "Why would I make up something like that?"
            "Jack frowns at me."
            "And I can see that his mind is racing."
            "Trying to come up with a valid reason."
            jack.say "I dunno..."
            jack.say "Maybe you just want to impress me!"
            jack.say "Like, you can't stand that I saw the hot gamer-girl first!"
            mike.say "Oh, come on, Jack!"
            mike.say "Don't you think you're being a little bit childish?"
            show jack sad at startle
            "Jack scoffs at my words."
            "And he shakes his head."
            jack.say "Whatever, [hero.name]!"
            show jack perv
            jack.say "She's absolutely frikin gorgeous!"
            jack.say "I've been watching everything she's recorded."
            jack.say "I just can't get enough of her!"
            "All I can do is nod and smile in response."
            "Jack keeps on showing me the video."
            "Pointing out things that he likes about Kat."
            "But all the time I'm still reeling from the fact he won't believe me."
            "Because it's going to be pretty awkward if he ever runs into the two of us together!"
            $ jack.flags.heard_about_kat = True
        "Yeah... She looks great...":
            "I suppose that I could tell Jack all about me having met Kat."
            "But he looks so high on the sight of her."
            "And that makes me wonder if it would be a good idea."
            "I mean, he might get the wrong end of the stick and become jealous."
            "No, better to pretend that I don't know her."
            "Because what are the chances of him actually meeting her anyway?"
            mike.say "Yeah, Jack..."
            mike.say "She's pretty cute."
            mike.say "Not really my kind of thing."
            mike.say "But each to his own, right?"
            show jack smile at startle
            "Jack scoffs at my words."
            "And he shakes his head."
            jack.say "Whatever, [hero.name]!"
            show jack perv
            jack.say "She's absolutely frikin gorgeous!"
            jack.say "I've been watching everything she's recorded."
            jack.say "I just can't get enough of her!"
            "All I can do is nod and smile in response."
            "Jack keeps on showing me the video."
            "Pointing out things that he likes about Kat."
            "But all the time I'm thinking about what I've decided to keep from him."
            "Wondering if there's any chance of him actually meeting her and blowing my cover!"
    return

label kat_event_03:
    if kat.love.max < 80:
        $ kat.love.max = 80
    scene bg amusement
    show kat yawn at center, zoomAt(1.5, (640, 1040))
    with fade
    kat.say "[hero.name]!"
    kat.say "How much longer do I have to keep this up?"
    mike.say "Don't open your eyes yet, Kat..."
    mike.say "Just a little longer, I promise!"
    kat.say "Ooh..."
    kat.say "I'm scared I'm going to trip and fall!"
    mike.say "Okay, Kat..."
    mike.say "You can open your eyes now."
    show kat sadsmile
    "Kat does as I tell her, blinking at the sudden return of the light."
    "She's squinting to begin with."
    show kat surprised
    "But as soon as she sees where we are, her eyes go wide."
    mike.say "Ta da!"
    mike.say "This is where we're going for our date."
    "Kat shakes her head, still staring in amazement."
    show fx exclamation
    kat.say "Whoa..."
    kat.say "The amusement park?"
    show kat happy
    kat.say "No way!"
    show kat smile
    "I'm seriously pleased that Kat's reacting in the way she is."
    "But I have to admit that she's perhaps a little more amazed than I expected."
    "Though maybe that's because she just opened her eyes to all of this."
    "All the sights and sounds of the park hitting her without warning."
    "Even I feel a little overwhelmed right now."
    "So maybe the best thing is for us to get in there already."
    mike.say "Come on, Kat..."
    mike.say "We're wasting precious time out here!"
    show kat normal
    "Kat nods, taking hold of my hand."
    "And then we head inside, mingling with the crowds."
    show kat shy with fade
    kat.say "Oh my..."
    kat.say "It's so loud in here."
    kat.say "And there are so many people!"
    "I can't help frowning a little."
    "As what Kat's saying sounds a bit odd to me."
    mike.say "What else would you expect, Kat?"
    mike.say "All of the people and the noise they make..."
    mike.say "That's part of the amusement park experience."
    show kat blush
    "Kat seems to blush at this, as if she's caught off-guard."
    kat.say "Oh yeah..."
    kat.say "Of course they are!"
    kat.say "So..."
    show kat normal -blush
    kat.say "What are we going to do first?"
    "The question distracts me from pressing Kat further."
    "And I find myself glancing around the park as I size up our options."
    $ amusement_done = []
    while game.hour < 18:
        if amusement_done:
            scene bg amusement
            show kat normal at center, zoomAt(1.5, (640, 1040))
            with fade
        menu:
            "Go on the Ferris Wheel" if not "ferris_wheel" in amusement_done:
                "I take one look at the Ferris Wheel, and my mind is made up."
                mike.say "Come on, Kat..."
                mike.say "We're going on the Ferris Wheel!"
                show kat sad
                kat.say "Are you sure that's a good idea?"
                show fx drop
                kat.say "It looks really high!"
                mike.say "That's kind of the idea!"
                show bg amusement at center, zoomAt(1.5, (940, 940))
                show kat sad at center, zoomAt(1.5, (740, 1040))
                with fade
                "I don't hesitate to begin leading Kat over to the Ferris Wheel."
                "And soon enough we're in the queue, fast approaching the front."
                show kat afraid
                "As we get shown into one of the gondolas, Kat's still clutching my hand."
                "Her grip on it gets ever tighter as we go higher."
                "But then I look around and see that she's got her eyes closed!"
                mike.say "Kat..."
                mike.say "You can't keep your eyes closed the entire time we're on here!"
                kat.say "You wanna bet?"
                mike.say "That's a shame."
                mike.say "Because you're really missing out."
                mike.say "The view from up here is amazing!"
                show kat sadclosed
                kat.say "Hmm..."
                kat.say "Oh, okay..."
                kat.say "Here goes nothing!"
                show bg amusement at dark
                scene bg black
                show ferris wheel kat with fade
                "I watch as Kat opens her eyes and takes a look around."
                "And I make sure to keep a tight hold of her hand too."
                "Just in case the sight makes her panic or do something stupid."
                kat.say "Oh..."
                $ game.active_date.score += 20
                kat.say "Oh wow!"
                kat.say "You were right."
                "For the rest of the time that we're on the Ferris Wheel, Kat keeps her eyes open."
                "And she actually seems to begin enjoying herself as well."
                "But once we're back on solid ground, she pulls me away from it."
                "And then she makes sure that we don't go near that particular ride again."
                $ amusement_done.append("ferris_wheel")
                $ game.pass_time(1)
            "Go on the Carousel" if not "carousel" in amusement_done:
                "I hear the old-fashioned organ music coming from the carousel."
                "And that draws me in the direction of the large merry-go-round."
                mike.say "Let's take a ride on the carousel, Kat!"
                mike.say "The big one right over there."
                show kat smile
                kat.say "The one with the wooden horses on it?"
                show kat smile
                kat.say "I always thought those things were for kids?"
                mike.say "Don't worry about it, Kat."
                mike.say "They let big kids on it too!"
                show bg amusement at center, zoomAt(1.5, (640, 840))
                show kat normal
                with fade
                "Kat and I hurry over to the carousel and join the queue."
                "Like I already said, the thing is pretty big."
                "So it can take a lot of riders at a time."
                "And this means we get to the front of the queue pretty quickly."
                "Kat makes to leap onto the horse next to mine."
                "But at the last minute, someone beats her to it."
                "I hastily pat the spot in front of me."
                "And Kat has no choice but to jump onto it."
                show bg amusement at dark
                scene bg black
                show merry go round kat with fade
                "Because a moment later, the carousel starts to move."
                "Pretty soon she's clinging onto the pole and I have my arms wrapped around her."
                "That's because, for all that it looks old-fashioned, the carousel is a bit of a dark horse."
                "Once up to speed, it moves seriously fast."
                "And the horses move up and down swiftly too."
                "I spend the entirety of the ride pressed right up against Kat."
                $ game.active_date.score += 10
                "And as a result, it's a pretty memorable experience to say the least!"
                "Although I don't know if it was as enjoyable for her."
                "As we climb off the horse and then step down from the carousel, Kat rubs her butt."
                kat.say "Ouch!"
                kat.say "I think that ride left me saddle sore!"
                $ amusement_done.append("carousel")
                $ game.pass_time(1)
            "Go to the Haunted House" if not "haunted_house" in amusement_done:
                "As soon as I set eyes on the haunted house, I know we have to go in there."
                "It's just such a cliche of the amusement park, the idea of being scared silly."
                "Even if most of the stuff inside would look totally goofy in broad daylight."
                mike.say "How about the haunted house, Kat?"
                mike.say "I always love those things!"
                show bg amusement at center, zoomAt(1.5, (340, 740))
                show kat annoyed at center, zoomAt(1.5, (440, 1040))
                with fade
                "Kat looks a little nervous as she stares at the attraction."
                kat.say "I don't know, [hero.name]..."
                show kat sadsmile
                kat.say "Dark places and jump-scares are okay in survival horror games."
                show kat sad
                kat.say "But in real life?"
                mike.say "Don't worry, Kat..."
                mike.say "I'll keep you safe, I promise."
                show kat annoyed
                "Kat doesn't look totally convinced."
                show kat sadsmile at startle
                "But she nods all the same."
                kat.say "Okay, okay..."
                kat.say "But you'd better!"
                show kat normal at center, zoomAt(1.5, (640, 1040)) with ease
                "We walk over to the entrance of the haunted house."
                show bg amusement at dark
                scene bg black
                show haunted house kat with fade
                "And then the employee on the door lets us into the gloomy interior."
                "What follows is almost a total blur of screams and running in the semi-darkness."
                "I know that what's in here with us is just cheap animatronics and people in costumes."
                $ game.active_date.score += 5
                "But somehow it still manages to make Kat and me jump out of our skins."
                "Eventually we burst out of the exit doors."
                "Both of us panting and our hearts racing."
                mike.say "Whoa..."
                mike.say "I...I think I might have used my shorts as an emergency toilet!"
                show kat afraid
                kat.say "N...never again, [hero.name]..."
                show kat angry
                kat.say "Never again!"
                $ amusement_done.append("haunted_house")
                $ game.pass_time(1)
            "Go for the Love Boat" if not "love_boat" in amusement_done:
                "The long, elegant necks of the swan-shaped love-boats catch my eye."
                "And it seems to me that I've hit on the perfect romantic choice of ride."
                mike.say "Let's take a ride on the love-boat, Kat."
                mike.say "Doesn't that sound just perfect?"
                show kat sadsmile
                kat.say "Meh..."
                kat.say "It sounds kinda boring to me!"
                show kat smile
                kat.say "But you're not going to let me talk you out of it..."
                kat.say "Are you?"
                "By way on an answer, I just shake my head."
                "And then I start leading Kat over to the ride in question."
                "It doesn't seem to be one of the more popular rides in the park."
                "So the queue is small and we're climbing into a boat in no time at all."
                show love boat kat
                "There aren't any seatbelts, and it doesn't seem like we'll need any."
                "As the boat sails into the dimly lit tunnel at an achingly slow pace."
                "I gaze around at the kind of samey tunnel walls as we creep along."
                "And I can't help letting out a sigh of disappointment."
                mike.say "Well..."
                mike.say "This is...sedate!"
                kat.say "Sedate?"
                kat.say "I feel like I'm falling into a coma!"
                mike.say "Hmm..."
                mike.say "I think the point of this ride was a chance to make out in private."
                kat.say "Huh!"
                kat.say "People must have been pretty desperate and horny in the past."
                $ game.active_date.score += 5
                kat.say "I tend to like a little more excitement to get me in the mood!"
                "After what feels like forever, we emerge from the end of the tunnel."
                "And I think both of us are wondering what the point of it all was."
                $ amusement_done.append("love_boat")
                $ game.pass_time(1)
            "Go in the Hedge Maze" if not "maze" in amusement_done:
                "That's about when I see the sign for the hedge maze."
                "It stands out to me as I know that not many parks have those."
                "And so the chances are that Kat's not going to be expecting it."
                mike.say "Come on, Kat..."
                mike.say "Let's go try the hedge maze."
                show kat surprised
                kat.say "Hedge maze?"
                kat.say "Like, a maze made out of bloody hedges?"
                mike.say "Yeah, pretty much."
                mike.say "It's not just a clever name!"
                show kat annoyed
                kat.say "They have something that lame-sounding here?"
                show kat happy
                kat.say "I've got to see this!"
                "Kat and I hurry over to the entrance of the hedge maze."
                show hedge maze kat
                "And once there, we find that you can just walk straight in."
                "At first, Kat holds onto my hand as we explore the twists and turns."
                "But pretty quickly I sense a dramatic change in her mood."
                "Rather than being bored, she seems to be enjoying it more by the second."
                "Soon enough she's running around the corners, dragging me along with her."
                mike.say "Whoa!"
                mike.say "Slow down!"
                kat.say "This is great..."
                kat.say "It reminds me of that retro game."
                kat.say "The one where you have to eat the pills and dodge the ghosts!"
                "I'm pretty sure I know the one that Kat's talking about."
                "But the name of it is something that I just can't recall."
                "So I leave it alone, as I don't want to get sued for getting it wrong..."
                "And instead I do the best I can to keep up with Kat as she tears around the maze."
                $ game.active_date.score += 20
                kat.say "Yeah!"
                kat.say "I feel like I'm inside the game!"
                "Once we finally find our way out, Kat's beaming from ear to ear."
                "But as for me, I feel ready to drop!"
                $ amusement_done.append("maze")
                $ game.pass_time(1)
            "Buy ice creams" if not "ice_cream" in amusement_done:
                "I keep seeing people walking past with ice creams in their hands."
                "And until now, I didn't think that I was hungry."
                "But with each new frozen delight that I set eyes on, I want one of my own all the more."
                mike.say "Hey, Kat..."
                mike.say "How about we go grab an ice cream?"
                "Kat follows my gaze to the latest ice cream to be carried by us."
                "And she shrugs."
                show kat smile
                kat.say "Sure, [hero.name]..."
                kat.say "Why not?"
                "That's all I needed to hear."
                "And a moment later, I grab hold of Kat's hand."
                show kat surprised with hpunch
                kat.say "Wha..."
                kat.say "Whoa!"
                with hpunch
                "Elbowing my way through the crowd, I make straight for the nearest ice cream stand."
                "And Kat has no choice but to come along as I drag her in my wake."
                "Finally we arrive and I see my goal in sight."
                mike.say "One of those please."
                mike.say "And make it a large one too!"
                mike.say "What about you, Kat?"
                show kat normal
                kat.say "Erm..."
                kat.say "I'll have one of those things there, I guess."
                show amusement icecream kat
                "Kat points to a seemingly random ice cream."
                "And I'm about to ask how she can be so nonchalant."
                "But at that same moment, I'm handed my ice cream."
                "And without pause or hesitation, I set about devouring it."
                "The whole thing only lasts a couple of minutes a the most."
                "And once it's gone, I let out a sigh of relief."
                mike.say "Urgh..."
                mike.say "I needed that!"
                kat.say "Geez..."
                $ game.active_date.score += 10
                kat.say "It sounds like you did too!"
                $ amusement_done.append("ice_cream")
                $ game.pass_time(1)
    scene bg amusement
    show kat at center, zoomAt(1.5, (640, 1040))
    with fade
    "Once we've exhausted ourselves having fun, Kat and I wander around the amusement park."
    "And the way she's looking at everything like it's new reminds me of something I meant to ask her before now."
    mike.say "You've not been to many places like this..."
    mike.say "Have you, Kat?"
    kat.say "No..."
    kat.say "Not really."
    mike.say "How come?"
    mike.say "Most people bugged their folks to bring them here whenever they could."
    mike.say "I know I certainly did!"
    show kat sad
    "Kat looks a little embarrassed."
    "Almost like she doesn't want to talk about it."
    kat.say "Well..."
    kat.say "My parents were kind of strict, you know?"
    kat.say "Way stricter than you'd think too."
    kat.say "And they didn't approve of places like this."
    mike.say "Ouch!"
    mike.say "That sounds tough."
    kat.say "It was, but..."
    show kat surprised
    "Kat trails off as she sees something that steal away her attention."
    "I follow her line of sight, trying to see what's caught her interest."
    mike.say "Isn't that..."
    show kat shocked at startle
    show fx exclamation
    kat.say "It's Princess Plum!"
    show kat surprised
    "Kat's totally correct."
    "But of course it's not the real Princess Plum."
    "It's one of the park employees dressed up as the character and posing for photos with guests."
    show kat shocked
    kat.say "Ooh..."
    show kat happy
    kat.say "I just love Princess Plum!"
    kat.say "She was my best friend when I was a little girl!"
    mike.say "Huh?"
    mike.say "How could she be your friend?"
    show kat smile
    kat.say "Oh...I mean she was my imaginary friend, you know?"
    kat.say "I didn't really have any friends back then."
    "Kat mentions the fact pretty casually, like it's just a matter of fact."
    "But on top of what she just told me about her folks, it really makes me think."
    "She's not painting a very pleasant picture of the life she had growing up."
    "And it's starting to make me wonder what else she's got to tell me about her past."
    kat.say "You like Princess Plum too, right?"
    "Kat's question snaps me back to reality."
    "And I feel like I have to do something to lighten the mood."
    mike.say "Oh yeah, Kat..."
    mike.say "Especially when she looks like that!"
    show kat angry
    kat.say "Oh, [hero.name]..."
    show kat blush
    kat.say "Is that all you guys think about?"
    mike.say "Lighten up, Kat..."
    mike.say "I think about you too!"
    mike.say "Actually..."
    mike.say "You don't happen to have a Princess Plum costume, do you?"
    show kat shy with hpunch
    "Kat slaps me hard on the chest."
    show kat smile
    $ game.active_date.score += 15
    "But I can see that she's smiling all the same."
    "So it looks like I achieved my objective."
    "At least for now."
    return

label kat_event_04:
    if kat.love.max < 100:
        $ kat.love.max = 100
    scene bg street
    show kat happy
    with fade
    "The date's been going pretty well, or at least that's the way I see it."
    "Kat and I have been getting on like a house on fire the whole time."
    "Making each other laugh and sharing stories that show how much we have in common."
    show kat normal
    "But all of a sudden I feel like someone flicks a switch that only affects Kat."
    "Because she goes quiet for a moment, the laughter stopping almost abruptly."
    "For a moment I think about asking her what's up."
    "Then I see that she's about to say something herself."
    show kat sad
    kat.say "[hero.name]..."
    mike.say "Yeah, Kat?"
    kat.say "I wanted to ask your opinion on something."
    show kat shy
    kat.say "Something that's kind of a little...taboo."
    "Now she's managed to pique my interest."
    show kat at center, zoomAt(1.5, (640, 1040))
    "And so I lean forwards, eager to hear what Kat has to say."
    mike.say "Sure, Kat..."
    mike.say "You can ask me anything."
    mike.say "So fire away!"
    show kat sadsmile at startle
    "Kat nods and smiles."
    "But I note that it looks a little forced."
    show kat normal
    kat.say "You know sites on the internet..."
    kat.say "The kind where people pay to see other people do things?"
    mike.say "You mean sites like ExclusiveFans?"
    mike.say "That kind of thing?"
    show kat at startle
    "Kat nods again."
    "But I note that this time, she's not smiling."
    kat.say "Exactly those kind of sites."
    show kat shy
    kat.say "What do you think of the girls that have accounts on them?"
    mike.say "Just to be clear, Kat..."
    mike.say "We're talking about the kind of girls that do sexual stuff, yeah?"
    mike.say "The ones that do it for the money their fans send them?"
    show kat at startle
    "Kat nods for a third time."
    "And this time she doesn't say a word."
    "Clearly waiting to hear what my answer will be."
    menu:
        "I have no problem with that":
            $ kat.flags.yes_for_camgirl = True
            "I find myself shrugging and shaking my head."
            mike.say "I guess I never really thought about it before."
            mike.say "But I can't say it bothers me that much!"
            show kat surprised
            "Kat's eyes seems to light up as she hears my answer."
            "So I suppose it was the one she'd hoped to hear."
            show kat shocked
            kat.say "Really?"
            kat.say "You don't think it's wrong?"
            kat.say "Or that the girls who do it are immoral?"
            show kat surprised
            "I can't help laughing at the way Kat puts her thoughts into words."
            "The ones she chooses almost make her sound like she's a refugee from the past!"
            mike.say "We're not living in the Dark Ages, Kat!"
            mike.say "There's always going to be people that hate porn and stuff like that."
            mike.say "But as far as I'm concerned, a woman's body is her own, and nobody else's."
            mike.say "If that's what she decides to do with it, then that's her business."
            "I pause and take a deep breath."
            "Because I know what I have to say next is pretty risky."
            mike.say "In fact..."
            mike.say "I think it's pretty hot!"
            show kat shocked blush
            kat.say "You do?"
            show kat surprised
            mike.say "Oh yeah!"
            mike.say "I love the idea of a girl being her own boss."
            $ kat.sub -= 2
            mike.say "Of her being in control of getting what she wants!"
        "I think that’s not right":
            $ kat.flags.yes_for_camgirl = False
            "I can't help the look of distaste that creeps onto my face."
            "But all the same, I do what I can to make sure my answer is fair."
            mike.say "Look, Kat..."
            mike.say "I try really hard not to judge other people."
            mike.say "Because god knows none of us are perfect."
            mike.say "And I don't know anyone that has one of those accounts."
            mike.say "Or the reason they do what they do."
            "I pause to take a deep breath."
            "And then I let it out as a resigned sigh."
            mike.say "But as for how I feel?"
            mike.say "I guess I must be a little old-fashioned."
            mike.say "Because I don't really like it."
            show kat sad
            "Kat nods slowly, listening to my every word."
            kat.say "So..."
            kat.say "You don't approve?"
            mike.say "I know I sound like an old man right now."
            mike.say "But I really don't!"
    mike.say "But why are you asking me about stuff like that?"
    mike.say "It seems like it came out of nowhere!"
    show kat shy
    kat.say "Oh..."
    kat.say "No reason..."
    show kat happy -blush
    kat.say "Just trying to get to know you a little better, that's all!"
    "I'm not convinced by Kat's explanation."
    "But I decide to leave it alone for now."
    "That way we can get on with our date instead."
    return

label kat_event_05:
    if kat.love.max < 120:
        $ kat.love.max = 120
    show jack happy
    jack.say "Hey..."
    jack.say "Hey, man..."
    jack.say "Come check this out!"
    show jack normal
    "I look up to see Jack waving his phone in the air as he hurries towards me."
    "But I'm not surprised in the least, as he's always insisting that I look at something."
    "It's usually a viral video that he thinks is cool, or a new roleplaying game he's into."
    "The best way to handle it is to simply nod and smile, letting him show it off."
    "Then I can either wait for him to see something shiny and new so that he forgets about it."
    "Or if it's actually something worth my attention, I can geek out with him to my heart's content."
    mike.say "What is it, Jack?"
    mike.say "You seem really wired!"
    "Jack nods eagerly, almost shoving his phone into my face."
    "I jerk my head back instinctively, and he seems to get the message."
    show jack blush
    "Jack pulls the phone back and makes a guilty face."
    jack.say "Oops!"
    jack.say "Sorry, man..."
    jack.say "I just really need you to see this video!"
    show jack normal
    mike.say "Okay, Jack..."
    mike.say "What is it?"
    mike.say "More stuff from Kat's livestream?"
    "I guess that this is what the video could be based on a recent conversation we had."
    "One in which Jack explained to me that he had a pretty intense crush on Kat."
    "But the question earns me a pretty strange response, as Jack shakes his head."
    show jack surprised
    jack.say "What?!?"
    jack.say "Oh no...no way!"
    jack.say "I already found someone else - and she's even better!"
    show jack smile
    "I can't help frowning at Jack's casual dismissal of Kat."
    "Sure, I know that he has a short attention span."
    "And his crushes don't usually last very long either."
    "But it's kind of different when the girl is someone I know."
    "It makes me feel like Jack's just tossing her aside without a second thought."
    "But there's nothing I can really do about the situation."
    scene expression f"bg {game.room}" at dark
    show jack normal zorder 1 at dark, center, zoomAt(1.1, (340, 740))
    show streaming cam smile interface_fg zorder 2 at center, zoomAt(1.0, (640, 520))
    show streaming_phone zorder 3 at center, zoomAt(1.0, (640, 520))
    with fade
    "So I resolve to just watch the video and get it over with."
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(animated_glitch, offset=3)
    "Jack hits play, and I instantly see it's another livestream."
    "But in this one the girl has next to nothing on."
    "And she's lying on a bed in a very suggestive position."
    mike.say "Oh..."
    mike.say "This one's a camgirl?"
    jack.say "Yeah..."
    jack.say "I found her on ExclusiveFans..."
    jack.say "But not just any camgirl."
    show jack perv
    jack.say "This one's the camgirl of my dreams!"
    "I roll my eyes at Jack's declaration of yet another crush."
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(animated_glitch, offset=3)
    "But I keep my thoughts to myself as the video keeps playing."
    "Then I notice something familiar about the camgirl."
    show streaming normal
    "Her blonde hair doesn't match the image I have in my mind."
    "But I swear that she looks just like Kat!"
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(animated_glitch, offset=3)
    "As I look a little closer, my suspicions are all but confirmed."
    show streaming smile
    "She might be wearing a wig, but that's definitely her."
    show jack normal
    mike.say "Erm..."
    mike.say "Is it just me..."
    mike.say "Or does she look a lot like Kat?"
    show jack wink
    jack.say "I know, I know..."
    jack.say "She's like Kat, but even better!"
    hide expression f"bg {game.room}"
    show expression f"bg {game.room}"
    show jack normal zorder 1 at center, zoomAt(1.1, (340, 740))
    with dissolve
    hide streaming
    hide streaming_phone
    with easeoutbottom
    pause 0.5
    show jack at center, zoomAt(1.1, (640, 740)) with ease
    menu:
        "Insist that the camgirl is actually Kat":
            show jack normal
            "I take a sideways glance at Jack as he watches the video."
            "And it's plain to see that he's totally entranced by what he sees."
            "He's a stubborn bastard at the best of times."
            "But I feel like I have to try to stop this."
            "Before it gets out of hand."
            mike.say "Jack..."
            mike.say "You're not that dumb, are you?"
            show jack surprised
            jack.say "Huh?"
            jack.say "What are you talking about?"
            mike.say "That girl doesn't just look like Kat."
            mike.say "She IS Kat!"
            "Jack shakes his head, refusing to believe me."
            show jack angry
            jack.say "No way!"
            jack.say "This girl's blonde!"
            mike.say "It's obviously a wig, you moron!"
            show jack sad
            "Jack shoves his phone into his pocket."
            "And then he rounds on me, arms crossed over his chest."
            show jack angry
            jack.say "Look, man..."
            jack.say "Just what is your problem with this girl?"
            jack.say "It's like you've got it in for her or something!"
            show jack sad
            mike.say "Jack..."
            mike.say "That's not it at all."
            mike.say "It's just that Kat's obviously got a lot going on in her life."
            mike.say "A lot of secrets that she's been keeping from people she knows."
            mike.say "I don't know why and I don't know what it all means."
            show jack smile
            "Jack lets out a snort of derision."
            show jack angry
            jack.say "Ha..."
            jack.say "You just said it yourself - you don't know shit!"
            jack.say "So why are you trying to lecture be about it?"
            jack.say "Maybe you should educate yourself first!"
            hide jack with moveoutright
            "With that, Jack turns on his heel and storms off."
            "That leaves me alone and feeling pretty awkward."
            "Because I know that I'm right."
            "The girl in that video was definitely Kat."
            "And now I know that she's a camgirl."
            "One that does stuff for money on ExclusiveFans too!"
            "If nothing else, that explains her asking me about the site the other day."
            "I guess she was feeling me out, trying to gauge what my reaction would be!"
        "Do not insist that the camgirl is Kat":
            show jack blush
            "I take a sideways glance at Jack as he watches the video."
            "And it's plain to see that he's totally entranced by what he sees."
            "When he gets like this, it's super hard to talk him out of something."
            "Or to convince him of something he doesn't want to be true."
            "So I decide to save myself a lot of unnecessary hassle."
            show jack normal
            mike.say "Yeah, Jack..."
            mike.say "That's pretty uncanny!"
            mike.say "I mean...they could be sisters."
            show jack smile
            jack.say "Tell me about it, man!"
            jack.say "What are the chances?"
            scene expression f"bg {game.room}" at dark
            show jack normal zorder 1 at dark, center, zoomAt(1.1, (340, 740))
            show streaming cam interface_fg zorder 2 at center, zoomAt(1.0, (640, 520))
            show streaming_phone zorder 3 at center, zoomAt(1.0, (640, 520))
            with fade
            "Jack makes me watch the rest of the video."
            show jack perv
            "All while he expounds on his feelings for the girl."
            show streaming smile
            "That and what he'd like to do with her if given the chance."
            show jack blush
            "And by the end of it all, I'm beginning to feel pretty awkward."
            show streaming at functools.partial(glitch, offset=3)
            pause .1
            show streaming at functools.partial(glitch, offset=3)
            pause .1
            show streaming at functools.partial(glitch, offset=3)
            pause .1
            show streaming at functools.partial(glitch, offset=3)
            pause .1
            show streaming at functools.partial(animated_glitch, offset=3)
            "Because the more I see of it, the more I know that I'm right."
            show jack normal
            "That's definitely Kat."
            "And now I know that she's a camgirl."
            "One that does stuff for money on ExclusiveFans too!"
            "If nothing else, that explains her asking me about the site the other day."
            "I guess she was feeling me out, trying to gauge what my reaction would be!"
    return

label kat_event_06:
    show kat confused with fade
    kat.say "Erm..."
    kat.say "[hero.name]..."
    kat.say "Can we, like...maybe talk about something?"
    "I can tell from the very first word that Kat's got something big to lay on me."
    "It's all in the tone, that level of seriousness that any guy worth his salt can identify."
    "The one that means you're about to spend the next few minutes squirming helplessly."
    "Or else going to learn something that changes everything in an instant."
    "But of course, I do the only logical thing."
    "Which is to pretend that I'm completely oblivious."
    mike.say "Oh..."
    mike.say "Sure thing, Kat..."
    mike.say "What was it that you wanted to talk about?"
    "I don't know if my ruse is good enough to fool Kat."
    show kat shy
    "But she seems to intent on saying her piece to let it show either way."
    kat.say "I kind of have a confession to make..."
    show kat annoyed
    kat.say "Well, maybe confession is too strong of a word..."
    show kat sad
    kat.say "Let's just say there's something I need to tell you."
    "Now this is getting interesting."
    "So I nod and lean in closer."
    "Basically doing all that I can to encourage Kat to speak up."
    show kat normal
    kat.say "You...you remember the other day?"
    kat.say "You know, when that I asked you about ExclusiveFans?"
    kat.say "And you told me what you thought of girls that stream on there?"
    "Of course I remember!"
    "How could I ever forget her bringing up something like that?"
    "But all the same, I make sure to keep my response neutral and sympathetic."
    mike.say "Yeah, Kat..."
    mike.say "I remember that."
    mike.say "What about it?"
    show kat shy
    "Kat looks down at her feet before she speaks again."
    "Letting me know that whatever she has to say, she thinks it's serious."
    show kat annoyed blush
    kat.say "Well..."
    kat.say "The reason I asked was because, I don't just stream videogames."
    show kat afraid
    kat.say "I also do more adult types of streams, for my most devoted fans!"
    "I knew it!"
    "I knew that I was right!"
    "So the girl in the video Jack showed me really was Kat."
    "And now she's confessing everything to me."
    show kat confused -blush
    kat.say "Well?"
    kat.say "Aren't you going to say anything?"
    show kat afraid
    kat.say "I'm kind of opening up to you here?"
    menu:
        "['As said before, ' if kat.flags.yes_for_camgirl else '']I have no problem with that":
            $ kat.flags.yes_for_camgirl = True
            if kat.love.max < 140:
                $ kat.love.max = 140
            "I can't keep a genuine grin from creeping across my face."
            show kat surprised
            show fx exclamation
            "And Kat looks at me in surprise as it's happening."
            kat.say "Hey!"
            kat.say "What's so funny?!?"
            hide fx
            mike.say "I kind of already knew about it, Kat."
            mike.say "A friend of mine showed me some of your streaming footage."
            mike.say "You like, had a wig on - but I knew it was you!"
            show kat angry blush
            "Kat frowns and plants her hands on her hips."
            kat.say "Hurmph..."
            kat.say "You might have said something already."
            kat.say "I got myself all worked up to confess!"
            show kat normal -blush
            kat.say "But wait..."
            kat.say "Are you okay with it or not?"
            kat.say "You didn't actually say so!"
            "I nod, doing the best I can to be serious and sincere."
            if kat.flags.yes_for_camgirl:
                mike.say "I thought I already told you..."
            mike.say "I'm totally okay with it."
            mike.say "I even think it's pretty hot!"
            show kat yawn
            "Kat let's out a sigh of relief."
            kat.say "Phew..."
            kat.say "That's a weight off my mind!"
            show kat offended at startle
            kat.say "Wait a minute..."
            show kat normal
            kat.say "You said a friend of yours showed you my footage?"
            mike.say "Yeah, Kat..."
            mike.say "He's called Jack, and he's a pretty big nerd!"
            show kat sadsmile
            kat.say "Does he use the handle 'Dong-Kong Sixty Nine'?"
            kat.say "Because I have a subscriber that does, and he's a massive nerd."
            mike.say "Hmm..."
            mike.say "It could be, I guess..."
            mike.say "Anyway, enough about him..."
            mike.say "When do I get to see you do a livestream for myself?"
            show kat smile
            kat.say "Oh, I don't know..."
            kat.say "Maybe we could arrange a private streaming session?"
            show kat blush
            $ kat.sub += 2
            $ game.active_date.score += 20
            kat.say "Just you and me..."
        "['I already told you t' if kat.flags.yes_for_camgirl is False else 'T']hat's not right":
            $ kat.flags.yes_for_camgirl = False
            "I can't keep a serious frown from spreading across my face."
            show kat sadclosed
            "And Kat seems to get nervous as she sees it happening."
            mike.say "I wish to god that you hadn't, Kat!"
            if not kat.flags.yes_for_camgirl:
                mike.say "Didn't I already make my feelings clear to you?"
            mike.say "I hate that kind of thing."
            mike.say "It's just prostitution dressed-up for the digital age!"
            "Kat shakes her head, trying to argue her case."
            show kat confused
            kat.say "That's not how it is at all."
            kat.say "Nobody gets to have actual sex with me!"
            kat.say "In fact, it's more like real art."
            kat.say "Just people admiring the beauty of the human body!"
            "I let out a snort of derisive laughter."
            "And I shake my head in sheer amazement."
            mike.say "Oh yeah, Kat..."
            mike.say "It's exactly like real art."
            mike.say "I can't count the number of times I went in an art gallery..."
            mike.say "And the place was full of guys wanking themselves off!"
            mike.say "Or there was the time I went to see the Mona Lisa in Paris."
            mike.say "And I ended up slipping on tissues soaked in jizz!"
            $ kat.love -= 20
            $ kat.sub -= 10
            show kat annoyed
            "Kat's back to gazing at her feet now."
            "And it doesn't look like she's going to fire back at me any time soon."
            mike.say "So no, Kat..."
            mike.say "I'm most definitely not cool with it."
            mike.say "And I don't think I can look at you right now either."
            hide kat with dissolve
            "With that, I turn and walk away."
            "I don't even bother to look back."
            "Content to huddle under the dark cloud of my own negative thoughts."
            $ hero.replace_activity()
            $ game.room = "street"
    return

label kat_event_07:
    if kat.love.max < 150:
        $ kat.love.max = 150
    scene expression f"bg {game.room}"
    "I like to think of myself as a modern kind of guy, you know?"
    "To believe that I'm more open-minded than the average too."
    "The type of person not freaked out by something out of the ordinary."
    "But I have to admit that what I'm about to do is kind of pushing that."
    "Finding out that Kat was a camgirl was a challenge of itself."
    "And now she's invited me along to watch her film an actual session!"
    "I mean, I had to say yes, right?"
    "I couldn't chicken out and look like it bothers me."
    "Because it doesn't...bother me, that is."
    "I'm totally cool with the whole idea."
    "Or at least that's what I keep telling myself as I walk into the room."
    scene bg kathome with fade
    "The set-up is pretty much what I expected, the kind of thing I've seen before."
    "There's somewhere for Kat to lie down and a camera set up to film it all."
    "Of course she has a lap-top from which she can run the whole show too."
    show kat sport haircut with dissolve
    "And there's Kat, right in the middle of it all."
    "She's fiddling with the equipment."
    "And she's doing so in the skimpiest outfit imaginable!"
    "But then of course she is."
    "Because she's not going to do something like this in a boilersuit, now is she?"
    mike.say "Ah..."
    mike.say "Hi, Kat!"
    show kat surprised
    "At the sound of my voice, Kat looks up from what she's doing."
    show kat happy
    "And she seems genuinely pleased to see me standing here."
    kat.say "Hey, [hero.name]..."
    show kat smile
    kat.say "Just checking everything's working perfectly."
    kat.say "I can't afford for one of these things to go wrong."
    show kat d afraid
    kat.say "My fans would freak out if that happened!"
    "I nod, still trying to look nonchalant."
    mike.say "I know what you mean, Kat!"
    mike.say "I've met some pretty intense fans in my time."
    "Kat nods too."
    "But she looks far more serious than me."
    show kat a annoyed
    kat.say "Oh, these guys and girls are the craziest of all."
    kat.say "Like, there's no way I'd ever let them know about you."
    mike.say "Huh?"
    mike.say "Why's that?"
    show kat a angry
    kat.say "Because they'd be out for your blood, that's why!"
    mike.say "You're joking?"
    mike.say "What did I ever do to them?!?"
    show kat b smile
    kat.say "You got involved with me, you dope!"
    "I'm about to ask Kat for more information on this potential new danger in my life."
    "Precisely what I have to be afraid of and how I can avoid being mobbed by her fans."
    "But the sound of the lap-top making a sound distracts Kat and she hurries over to it."
    show kat c normal
    kat.say "Look, [hero.name]..."
    kat.say "The session's about to start."
    show kat c smile
    kat.say "We can talk later, okay?"
    kat.say "You'll be totally safe and out of sight so long as you stay over there."
    show kat a happy
    kat.say "And keep quiet too!"
    "I nod, doing the best I can to stop thinking about Kat's fans."
    scene bg kathome at center, zoomAt(1.5, (640, 920)) with fade
    "Settling down in the spot she pointed out, I can't help feeling strange."
    "Almost like I'm sitting in one of those hides they use to watch wildlife."
    show kat a normal sport haircut at center, zoomAt(1.5, (740, 920)) with easeinleft
    pause 0.2
    show kat a underwear with dissolve
    pause 0.3
    show kat at center, zoomAt(1.5, (740, 1140)) with ease
    "Kat lies down in front of the camera, but not before she strips off some more."
    "Now she's dressed in almost nothing at all, and everything's on show."
    "Speaking of which, it seems like it's time for the show to begin."
    with fade
    show layer master at katstream
    "I've watched things like this in the past."
    "Because of course I have."
    "I'm only human, after all."
    "But when I watched those streams, I could see the chatroom attached to them."
    "Now the only thing I can see is Kat, as she responds to what her fans are typing."
    play sound ping
    "I can hear the sound of the lap-top pinging though, a steady stream of sound."
    play sound ping
    "And I know that everyone of them is someone interacting with her in real-time."
    play sound ping
    "Offering her a compliment, making a request or else sending her money."
    show kat b smile
    kat.say "Hey, you guys!"
    kat.say "I hope you've all missed me?"
    "I don't know if it's the question that Kat just asked."
    "Or else what she's doing with her hands as she asks it."
    show kat b surprised
    play sound ping
    "But whatever the cause, the lap-top pings away merrily."
    kat.say "Oh..."
    show kat a happy
    kat.say "That's so kind of you!"
    "Kat's smiling and giggling the whole time she says this."
    "Being all sweet and attentive to her audience."
    "And it's made all the more intriguing by the fact I just know she's acting."
    "The Kat I know is way more surly and edgy than that - she has teeth!"
    show kat defiant
    kat.say "You know what..."
    kat.say "I am feeling a little hot!"
    show kat b smile
    kat.say "So I really should take it off!"
    show kat b smile at center, zoomAt(1.5, (740, 940)) with ease
    "I watch as Kat peels off the last of her clothes."
    "She does it slowly and deliberately, making sure to take her time."
    play sound ping
    "And all the while she does so, I hear the lap-top ping more than ever!"
    play sound ping
    show kat b topless with dissolve
    "The peak comes when she takes off her bra, revealing her perfect, petite breasts."
    play sound ping
    "My ears fill with the sound of the fans showing their approval."
    "And I can't say that I blame them one bit."
    "Because I can feel myself getting hard at the sight too!"
    show kat c happy at center, zoomAt(1.5, (740, 1040)) with fade
    kat.say "Oh, I know that you like them."
    kat.say "And I like showing them off to you too!"
    show kat a smile blush
    "Kat leans back on one elbow as she looks down at her chest."
    "And this leaves her other hand free to play with them idly."
    kat.say "Mmm..."
    kat.say "It feels so good when I hold them."
    kat.say "Even better when I start to squeeze them!"
    "It's not just me that's getting hard right now."
    "Kat's nipples are becoming stiffer by the second."
    show kat a yawn
    kat.say "Hmm..."
    kat.say "I really wish you could all feel them too."
    play sound ping
    "Of course this sparks another flurry of pings."
    "But Kat doesn't seem to pay them as much attention as before."
    show kat c happy at center, zoomAt(1.75, (740, 1140))
    "Instead she leans in closer to the screen."
    "And it looks like she's trying to read one of the comments."
    show kat d sadsmile
    kat.say "That's so cheeky of you!"
    kat.say "Asking me how my pussy feels too."
    kat.say "You should be ashamed of yourself!"
    "Kat does her best to look shocked as she says all of this."
    show kat d defiant -blush
    "But then she glances away from the screen for a moment."
    "And I see her expression become wicked and conspiratorial."
    kat.say "Actually..."
    kat.say "I kind of want to know what it feels like too!"
    show kat c
    kat.say "Because it's getting all tingly down there."
    kat.say "And wet too..."
    "Kat must be really good at this, a total natural."
    "Because I find myself hanging on her every word."
    "I can't keep from leaning in closer too."
    "Desperate to see what she's talking about."
    show kat timid
    "I do this just in time to see Kat's hand slide down from her breasts."
    "It travels over her belly and down onto her thigh in one smooth movement."
    hide kat
    show kat mast haircut rub
    with fade
    "And from there it slips between her legs, fingers already beginning to move."
    show kat mast mouth_scream
    kat.say "Oooh..."
    show kat mast mouth_normal
    kat.say "I really like the way that feels!"
    show kat mast mouth_hurt eyes_pleasure
    kat.say "Mmm..."
    show kat mast mouth_normal
    kat.say "It's making me want to touch myself even more..."
    show kat mast eyes_close
    "I can only imagine the number of people that must be watching her right now."
    "All of those eyes staring at the sight of her fingers tracing the lines of her pussy."
    "Kat's giving her audience exactly what they want, but she's not being quick about it."
    "In fact she seems to know just how to strike the right balance to keep them enthralled."
    show kat mast haircut finger
    "Little by little she pushes her fingers deeper and presses harder."
    show kat mast mouth_scream eyes_open at startle(0.05, -10)
    kat.say "Oh dear..."
    kat.say "My fingers went inside of me!"
    kat.say "But I can't stop now..."
    kat.say "Not when it feels SO good!"
    show kat mast rub mouth_hurt eyes_close at startle(0.05, -10)
    "I can't help nodding as I watch Kat playing with herself."
    "It feels like she's talking directly to me right now."
    show kat mast finger at startle(0.05, -10)
    "Even though I know she has to play to her entire audience."
    "Kat begins to moan as her pace quickens, closing her eyes at the same time."
    show kat mast rub shake mouth_hurt eyes_pleasure at startle(0.05, -10)
    "She leans backwards, nodding at the pleasure she's feeling."
    show kat mast finger -shake mouth_scream eyes_pleasure at startle(0.05, -10)
    kat.say "Oh..."
    kat.say "Oh god..."
    show kat mast rub eyes_close mouth_hurt at startle(0.05, -10)
    kat.say "I...I can't stop!"
    show kat mast finger shake mouth_scream at startle(0.05, -10)
    kat.say "I'm going to...going to cum!"
    play sound ping
    show kat mast rub at startle(0.05, -10)
    "The lap-top seems to be going into meltdown as all of this is happening."
    play sound ping
    show kat mast finger eyes_pleasure at startle(0.05, -10)
    "It keeps pinging ever faster, almost like it's having an orgasm too."
    show kat mast squirt eyes_close mouth_scream with vpunch
    "It's all I can do to keep myself from shouting out my approval."
    with vpunch
    "And I have to bite down on my knuckles to keep quiet."
    show kat mast -shake rest mouth_normal
    "Once she's spent, Kat leans over and waves at the camera with one hand."
    scene bg kathome
    show kat naked a happy haircut at center, zoomAt(1.5, (640, 1040))
    with fade
    "And with the other she turns it off, signalling that the session is over."
    "Then she leaps up and shakes herself, as if trying to wake up."
    "But there's still part of me that can't help thinking it's to shake off what just happened."
    hide kat
    show kat a normal naked haircut
    with fade
    kat.say "Urgh..."
    kat.say "Are you okay for a few minutes, [hero.name]?"
    kat.say "I always like to jump in the shower after a session."
    kat.say "Helps me to reset my brain, you know?"
    mike.say "Yeah, Kat..."
    mike.say "I get it."
    mike.say "You go right ahead."
    show kat smile
    "Kat gives me a nod and a smile, then she heads off to take her shower."
    hide kat with easeoutleft
    "While she's gone, I can't stop thinking about everything I just saw and heard."
    "The truth is that I don't really know what to make of it all."
    "It was quite something to watch, really hot and sexy."
    "And it's kind of a thrill to know that Kat's so much in demand."
    "Plus she must be making some serious money."
    "Because her lap-top was pinging away like crazy."
    "But then I can't help feeling a little jealous of having to share Kat."
    "Especially with so many other people - guys and girls alike!"
    "I guess it's just going to take me a little longer to make sense of this."
    "And until then I'll just have to keep an open mind."
    return

label kat_event_08:
    if kat.love.max < 160:
        $ kat.love.max = 160
    show kat a shy
    "I've agreed to meet up with Kat today, just to spend some time hanging-out."
    "You know, chatting, maybe playing some games or grabbing a bite to eat."
    "Just the usual kind of random stuff that guys and girls do together."
    "And I'm doing the best I can to play it casual, to keep things normal."
    "But obviously I have the memory of watching Kat streaming on my mind."
    "The whole thing was so weirdly compelling that I just can't stop thinking about it."
    "But I try nonetheless, and at first I think Kat's on the same page as me."
    show kat a timid at center, zoomAt(1.5, (640, 1040)) with fade
    "Because all we chat about is normal stuff."
    "That is until I hear her take a deep breath."
    "Kat holds it in for a moment, letting me know this is something, rather than nothing."
    "And then she lets it out in one long sigh."
    show kat a shy
    kat.say "So..."
    show kat b
    kat.say "I guess there's kind of an elephant in the room."
    kat.say "Huh, [hero.name]?"
    mike.say "Yeah, Kat..."
    mike.say "You could say that."
    show kat a
    kat.say "And I guess it's shaped like you watching me stream."
    kat.say "Right?"
    "All I can do is shrug my shoulders and nod."
    mike.say "It was always going to be an eye-opener, Kat."
    show kat a sad
    kat.say "But you liked it, didn't you?"
    kat.say "I mean, you looked like you were having a good time."
    mike.say "Oh, don't get me wrong..."
    mike.say "It was kind of mind-blowing!"
    mike.say "I just don't think I've managed to fully process it yet, that's all."
    show kat smile
    "Kat nods at this, showing me that she understands."
    "Or at least that she's prepared to accept my non-commital answer for now."
    "But then she turns and shifts her head a little."
    "And when she speaks, there's a change in the tone of her voice."
    "Which is a pretty good sign that she's about to change the subject."
    show kat a normal
    kat.say "Anyway..."
    kat.say "I have another session coming up real soon."
    show kat shy
    kat.say "And I was wondering if..."
    "I jump in before Kat can finish what she has to say."
    "It has to be because of the subject we're discussing."
    "I just can't help myself."
    mike.say "You want me to watch the next one too?"
    mike.say "Well...I suppose I could."
    show kat a timid
    "Kat shakes her head at this."
    "Then she holds her hand up to stop me from saying more."
    kat.say "You mind letting me finish, [hero.name]?"
    kat.say "I wasn't asking you to just sit and watch this time."
    show kat b sadsmile
    kat.say "I wondered if you'd be up for actually getting involved?"
    "For a moment I find myself staring blankly at Kat."
    "I understand all of the words she just said."
    "As well as what they mean in that order."
    "But for some reason my brain just won't process them."
    mike.say "You..."
    mike.say "You want me..."
    mike.say "To be on camera with you..."
    mike.say "While you're doing sexy stuff?"
    show kat d afraid blush
    "Kat chuckles at the way I'm getting embarrassed and tongue-tied."
    kat.say "Of course that's what I mean!"
    show kat c shy
    kat.say "I've been getting a lot of requests for more intimate stuff."
    kat.say "And my fans would love to see me get fucked on a live stream."
    show kat c timid
    kat.say "So what do you say?"
    menu:
        "You know... I'm quite photogenic":
            "Before now I'd been wrestling with the whole issue of Kat streaming."
            "But the moment she mentions the idea of me getting involved, that changes."
            "Somehow it crystalises everything for me, letting me make up my mind."
            mike.say "You know what, Kat..."
            mike.say "I'm going to take you up on that offer."
            show kat a yawn -blush
            "Kat lets out a yelp of delight."
            "And she claps her hands together for added effect too."
            $ kat.love += 2
            $ game.active_date.score += 20
            show kat a happy
            kat.say "I was sure you'd be up for it."
            show kat b smile
            kat.say "The way you kept looking at me the last time..."
            kat.say "I just knew you wouldn't be able to say no."
            "There's a moment of silence that follows."
            "And in it we just stare at each other."
            "As if we're waiting for the other person to say something."
            "But in the end I feel compelled to speak up first."
            mike.say "So..."
            mike.say "What happens now?"
            mike.say "I mean, I've never done this kind of thing before."
            mike.say "So you're going to have to take the lead."
            show kat b surprised
            kat.say "Yes..."
            kat.say "Of course..."
            show kat a defiant
            kat.say "Just leave everything to me."
            kat.say "I'll sort out all of the details."
            "With that we do the best we can to change the subject."
            "And now I have something else to occupy my mind."
            "Something even more crazy than the last one."
            $ kat.flags.agree_sex_cam = True
        "Sorry but being exposed like that is not my thing":
            "Before now I'd been wrestling with the whole issue of Kat streaming."
            "But the moment she mentions the idea of me getting involved, that changes."
            "Somehow it crystalises everything for me, letting me make up my mind."
            show kat c surprised -blush
            mike.say "No, Kat..."
            mike.say "I have no problem with you doing what you do."
            mike.say "But I'm not going to get involved with it either."
            "Of course this isn't the answer that Kat was hoping for."
            "And she immediately does all she can to change my mind."
            show kat a sad
            kat.say "Are you serious, [hero.name]?"
            kat.say "If you're okay with it, why not get in on it too?"
            show kat a sadsmile
            kat.say "You've seen how much fun it is."
            kat.say "And how hot it is too!"
            kat.say "Plus you'd get a share of the donations too."
            "I shake my head, not at all convinced."
            mike.say "You don't need to pay me to fuck you, Kat!"
            kat.say "You know that's not what I meant!"
            show kat a sad
            kat.say "Come on, [hero.name], please?"
            kat.say "You'd be helping me take things to the next level."
            mike.say "Sorry, Kat..."
            mike.say "But you're going to have to get there on your own."
            mike.say "Because my answer is still no."
            $ kat.love -= 5
            $ game.active_date.score -= 10
            "Kat still looks like she wants to argue with me."
            "She opens her mouth, but then closes it again."
            "And it seems she's willing to let the matter drop."
            "At least for now."
            $ kat.flags.agree_sex_cam = False
    hide kat
    show kat a
    with fade
    return

label kat_event_08a:
    if kat.love.max < 180:
        $ kat.love.max = 180
    scene bg street
    "As soon as Kat lets me know that she's ready to start her latest stream, I head straight over."
    "I'd like to be able to say that I play it cool and arrive in my own time, staying in control."
    "But the truth is that I hurry to her apartment as quickly as possible, eager to get things started."
    "Because in the time I've been waiting to do this, I've been getter ever more excited."
    scene bg door hallway at center, zoomAt(1, (640, 720)) with fade
    "And once I reach Kat's door, I can't help hammering on it."
    show bg door private at center, traveling(1.5, 0.3, (640, 1040))
    pause 0.3
    play sound door_banging
    scene bg black
    pause 2.0
    stop sound
    scene bg kathome at center, zoomAt(1.25, (640, 940))
    show kat sport haircut at center, zoomAt(1.5, (640, 1040))
    with wiperight
    "Luckily she opens up before I can pound the thing off its hinges."
    kat.say "Settle down there, tiger!"
    kat.say "Save all that energy for the stream, okay?"
    show bg kathome at center, traveling(1.0, 1.0, (640, 720))
    show kat sport haircut at center, traveling(1.0, 1.0, (940, 720))
    "With that, Kat steps back and opens the door wide, letting me into her apartment."
    "It's only as I walk inside that I see behind the door, getting a good look at her for the first time."
    "My body might keep on moving, but my eyes are fixed on Kat the whole time."
    "Because she's already as scantily dressed as she was for the last session I watched her film!"
    "And it seems as though my interest is more than a little obvious."
    show kat defiant sport haircut at center, traveling(1.25, 2.0, (640, 820))
    kat.say "I take it you approve of my outfit?"
    kat.say "That you won't have a problem performing on camera?"
    "I shake my head at this."
    "Partly to let Kat know my answer to her second question."
    "And partly to shake off the effects the sight of her is having on me right now."
    mike.say "N...no, Kat..."
    mike.say "No problem at all!"
    show kat happy
    "Kat greets this with a nod and a smile."
    "Then she beckons for me to follow her as she walks into another room."
    show kat normal
    "Of course this is the same one she used for the last session, and the set-up is the same."
    "Only this time Kat doesn't motion for me to sit down behind the camera."
    show kat at center, traveling(1.25, 2.0, (640, 820))
    "Instead she leads me straight in front of it."
    "In effect, putting me centre-stage!"
    kat.say "Okay, [hero.name]..."
    kat.say "You want to start getting ready?"
    mike.say "You mean get naked?"
    kat.say "For starters, yeah..."
    kat.say "Just chuck your clothes over there, right?"
    kat.say "It doesn't matter where, so long as they're out of shot."
    show kat annoyed
    "I nod and begin to do as I'm told."
    "But Kat's too engrossed in making last-minute checks to even notice."
    "And it's not until I'm totally naked that she looks my way again."
    show kat smile
    kat.say "Looking good!"
    kat.say "Now put this on..."
    kat.say "And then we're ready to go."
    show kat b at startle
    pause 0.2
    show kat a
    "Kat tosses something to me as she says this."
    "And it's only when I catch the thing that I realise what it is."
    mike.say "A pig mask?"
    mike.say "What's this for?"
    show kat shy
    kat.say "To cover your face of course."
    kat.say "I don't want people to know who you are."
    mike.say "What are you trying to say?"
    mike.say "That I'm not good-looking enough for your fans to see me?"
    show kat confused
    "Kat rolls her eyes and shakes her head at this."
    kat.say "Of course not, [hero.name]!"
    kat.say "Look, you have a so-called proper job, don't you?"
    mike.say "Erm..."
    mike.say "Yeah, you could call it that."
    show kat defiant
    kat.say "Well, would you still have it if your boss saw you fucking me online?"
    "My eyes go wide as I realise that Kat's got a damn good point."
    "And I wonder how in the hell the same thing never occurred to me."
    mike.say "Point taken, Kat..."
    play sound woosh_punch
    scene bg black with wipedown
    "I say this as I put on the mask and make sure it's secure."
    scene bg kathome at center, zoomAt(2.0, (640, 1200))
    show kat_mask_fx as fx zorder 3
    with dissolve
    "Afterwards I find that it restricts my vision."
    "But then I'm going to be staying in front of the camera."
    "So that shouldn't really be an issue."
    show bg kathome at center, traveling(2.0, 2.0, (340, 1200))
    "What I'm more worried about is it getting in the way of my breathing."
    "Because I'm guessing Kat's going to want me to do her pretty hard."
    show bg kathome at center, traveling(2.0, 2.0, (940, 1200))
    "I'll just have to do all that I can to pace myself."
    "That and pray I don't pass out from lack of oxygen halfway through!"
    show bg kathome at center, zoomAt(2.0, (640, 1200))
    with vpunch
    "Suddenly I feel the sensation of something warm and soft against my groin."
    show bg kathome at center, traveling(2.0, 2.0, (640, 900))
    show minami_spank_body as katass at center, zoomAt(2.75, (800, 2000)), rotation(270)
    show minami_spank_body as katass at center, traveling(2.75, 2.0, (800, 2200)), rotation(270)
    with dissolve
    "And when I looks down, I see Kat's ass right there in front of me!"
    kat.say "Hey, guys..."
    kat.say "So good to see all of you again."
    "I must have been so distracted by the mask I lost track of what's going on."
    "Because it looks like the session's already started."
    kat.say "And the more observant amongst you might have noticed that I have a guest today."
    kat.say "This is my good friend 'Mister Pig'..."
    kat.say "Wave to the nice people, Mister Pig!"
    "Kat never mentioned anything calling me that."
    "Or about my having to interact with the audience."
    "But this isn't the time or place to complain about such things."
    "So I simply raise a hand awkwardly and vaguely wave it around."
    kat.say "Now then, guys..."
    kat.say "Mister Pig's going to help me do something you've been asking for."
    kat.say "Something that all of you want to see really badly."
    kat.say "Mister Pig's going to fuck me, right here and now."
    kat.say "In fact, he's going to fuck me hard enough to make me squeal."
    kat.say "Aren't you, Mister Pig?"
    "This time I decide to nod my head, the mask flopping around as I do so."
    "Sure, the mask and the name aren't very flattering to my ego."
    "But I bet my bod looks good in comparison to them."
    "And like Kat already said, nobody can see my face."
    "The realisation that I have nothing to worry about starts to take hold."
    "And the thrill of excitement soon follows on its heels too."
    "I can already feel my cock starting to get hard at the prospect of what lies ahead."
    "So much so that Kat feels it too!"
    kat.say "Oh..."
    kat.say "Hello!"
    kat.say "Seems like Mister Pig is ready!"
    kat.say "Aren't you, Mister Pig?"
    scene kat doggy naked mike haircut katroom with hpunch
    "Kat underlines the point by pushing her ass hard against me."
    "And in that moment, something clicks, deep inside of my head."
    "My hands shoot out and grab her by the haunches."
    "My fingers dig into the soft flesh of her thighs."
    "And I thrust myself forwards without warning."
    "Before now, Kat was teasing me and playing to the audience."
    "But now she lets out a genuine cry of surprise."
    "The head of my cock is pressed hard against the lips of her pussy."
    "And the fact that she's wriggling in my grasp only serves to help me out."
    "That's because it means the tip slithers and slides around."
    "It traces an erratic line amongst the folds down there."
    "And I can already feel Kat getting wetter by the second."
    "All of a sudden I find the opening I was looking for."
    show kat doggy eyes_close speed with hpunch
    "Without a conscious thought, I push harder than ever."
    "Now Kat's moaning as my cock sinks all the way into her."
    "Within moments it's filling the length of her pussy."
    "And that means she's also totally at my mercy."
    kat.say "M...Mister..."
    kat.say "Mister Pig..."
    kat.say "You're...SO...big!"
    "I don't pause to enjoy the sensation of being inside Kat."
    "Instead I start to thrust back and forth with everything I have."
    "By now I'm totally lost in the act of what she's asked me to do to her."
    "And the truth is that I'm playing out the things I think my character would do."
    "It's almost like the mask gives me the power to be someone else entirely."
    "Like it means that I don't have to behave like person I normally am."
    "And this new persona that Kat's thrust upon me is pretty animalistic."
    "All that it's concerned with is indulging its appetites."
    "And it won't stop until they've been sated!"
    kat.say "Y...yes..."
    kat.say "P...please..."
    kat.say "Fuck me...harder!"
    "I hear the words that Kat's saying, but I'm not sure they have any effect on me."
    "It kind of feels like someone urging a boulder to keep on rolling down a hill."
    "What's happening right here would still be happening if she'd kept perfectly quiet."
    show kat doggy eyes_close speed with hpunch
    "But that's not something Kat's able to do, as she's pounded ever harder."
    "Inside the mask, I can only catch glimpses of jiggling pink."
    "And all I hear is the sound of Kat moaning and my own laboured breathing."
    "Aside from that, all I focus on is the sensation of my cock inside her."
    "I don't even try to look at the lap-top screen once."
    "And the sounds that it's making are impossible to hear too."
    "Even Kat's words are drowned out as I feel myself about to cum."
    "My ears are filled with the sound of my heart pounding."
    with hpunch
    "As with one last thrust, I shoot my load into her."
    with hpunch
    "I have no way of knowing if the sound I make myself escapes the mask."
    show kat doggy eyes_close -speed with hpunch
    "But I feel Kat collapse in front of me sliding off my cock as she does so."
    "And my senses don't return to normal until I glimpse Kat shutting the lap-top."
    $ kat.sexperience += 1
    scene bg black with dissolve
    pause 0.2
    play sound woosh_punch
    scene bg kathome
    show kat c naked haircut happy blush at center, zoomAt(2.0, (640, 1340))
    with wipeup
    "I take that as my cue to tear off the mask and toss it aside."
    "My hair and face are soaked with sweat, my breathing ragged."
    "Though none of that seems to matter to me right now."
    "Because Kat's looking at me with a visible glint in her eye."
    "And her cheeks are flushed red from what I just did to her."
    $ kat.love += 5
    show kat smile c
    kat.say "That was great, [hero.name]!"
    kat.say "Just what I wanted."
    kat.say "The chatroom was going crazy for it."
    mike.say "Uh..."
    mike.say "You mean..."
    mike.say "They liked it?"
    show kat surprised c
    kat.say "They were freaking out!"
    kat.say "I haven't had this many donations in ages!"
    show kat happy c
    "I can't help smiling, as a sense of genuine achievement sweeps over me."
    "Who knows, maybe this kind of thing isn't so bad after all?"
    "And what's not to like about getting paid to fuck?"
    $ hero.cancel_activity()
    return

label kat_event_08b:
    "It's been a couple of days since Kat asked me to have sex with her on one of her streaming sessions."
    "At first I was worried that turning her down was going to have serious consequences for our relationship."
    "But since then she hasn't mentioned it even once, so I guess it wasn't such a big deal after all."
    "In fact I'm just starting to forget about the whole affair when I happen to bump into Jack."
    show jack surprised at center, zoomAt(1.25, (640, 940)) with hpunch
    "And I mean literally bump into him, because he's totally not looking where he's going!"
    mike.say "Whoa..."
    mike.say "Jack!"
    jack.say "Wha..."
    jack.say "[hero.name]!"
    mike.say "Are you okay, man?"
    show jack sad
    jack.say "I'm sorry, dude..."
    show jack normal
    jack.say "I was totally wrapped up in what I was watching!"
    "I see that Jack still has his phone in his hand, a video paused on the screen."
    mike.say "Huh..."
    mike.say "It must have been pretty absorbing."
    mike.say "What in the hell were you even watching?"
    "Jack looks a little furtive at me questioning his viewing material."
    "He glances around, like he's checking that nobody can overhear us."
    show jack surprised at center, traveling(1.5, 1.0, (640, 1040))
    "And then he leans in closer, holding up his phone for me to see."
    jack.say "You remember that camgirl I told you about?"
    jack.say "The one called Kat?"
    mike.say "Of course I do."
    jack.say "Well, she just kicked things up to the next level."
    mike.say "What does that mean, exactly?"
    show jack perv
    jack.say "Oh man..."
    jack.say "She just had sex with some guy on her stream!"
    "The moment I hear those words, I want to grab the phone from Jack."
    "But somehow I manage to summon up the willpower to stop myself."
    mike.say "What guy?"
    mike.say "Who is she having sex with?!?"
    show jack surprised
    "Even though I'm reigning it in, Jack still looks puzzled."
    jack.say "Huh?"
    jack.say "What do you care?"
    mike.say "Just answer the question, Jack!"
    show jack normal
    jack.say "Okay, okay..."
    jack.say "But there's no point in even asking me."
    jack.say "Because the guy's wearing this creepy pig mask the whole time!"
    mike.say "Pig mask?!?"
    jack.say "Look, man..."
    jack.say "Just watch the video for yourself."
    scene expression f"bg {game.room}" at dark
    show jack normal zorder 1 at dark, center, zoomAt(1.1, (340, 740))
    show streaming sex interface_fg zorder 2 at center, zoomAt(1.0, (640, 520))
    show streaming_phone zorder 3 at center, zoomAt(1.0, (640, 520))
    with hpunch
    "Jack thrusts his phone into my hand, looking flustered as he does so."
    "And then he stands back as I hit play, holding the thing mere inches from my face."
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(animated_glitch, offset=3)
    "I see Kat, down on all fours in the place she usually streams from."
    "Then I see the shape of a guy appear from behind her."
    "Just like Jack said, he's naked save for a pig mask."
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(animated_glitch, offset=3)
    "And from the looks of him, he's pretty well-built too."
    "Muscles and manhood alike!"
    "I watch in growing horror as he grabs hold of Kat's buttocks."
    hide expression f"bg {game.room}"
    show expression f"bg {game.room}"
    show jack normal zorder 1 at center, zoomAt(1.1, (340, 740))
    with dissolve
    hide streaming
    hide streaming_phone
    with easeoutbottom
    pause 0.5
    show jack perv at center, zoomAt(1.1, (640, 740)) with ease
    "And then I shove the phone against Jack's chest before I see anything more."
    jack.say "Now you see?"
    jack.say "It's just like I said."
    mike.say "Yeah, Jack, yeah..."
    mike.say "Look, I have to go."
    mike.say "I...I have to be somewhere."
    show jack normal
    jack.say "Sure, man."
    jack.say "Whatever..."
    hide jack with easeoutleft
    "Jack holds up his hands as he turns and walks away."
    "Which leaves me alone to try and make sense of what I just saw."
    "When Kat asked me to have sex with her on camera, I thought it was an exclusive offer."
    "You know, like she wanted to do it with me because we're an item."
    "I had no idea she was just asking me as the first choice for the part!"
    "Learning that Kat would actually have sex with another guy leaves me kind of shaken."
    "But I know that I have to decide what I'm going to do about it."
    menu:
        "Confront Kat":
            "I just can't believe that Kat would go behind my back like that."
            "Sure, I didn't want to have sex with her on camera when she asked."
            "But she should have made it clear to me she'd be looking for someone else instead!"
            "It's hard enough to cope with a girl I'm seeing doing what she does."
            "I can't handle her going behind my back too."
            "No, there's just no way that I can let this one slide."
            "I'm going to have to confront Kat the first chance that I get."
            "Maybe I can make her see the error of her ways."
            "Or maybe she'll just tell me to get lost and dump my ass."
            "But either way I'll know that I was the one in the right."
            $ kat.flags.confront_sex_cam = True
        "Do not confront Kat":
            if kat.love.max < 180:
                $ kat.love.max = 180
            "Of course I want to march right up to Kat and have it out with her."
            "To demand to know what the hell she thinks she's doing."
            "But then I remember that she's not done or said anything about it to me since."
            "Like, she's behaving as though this doesn't affect our relationship at all."
            "So the only thing I can think is that's the way she sees it."
            "To Kat, fucking this guy must have simply been a business thing."
            "Sure, I could tell her that I don't like it."
            "But then I'd be trying to control her career, wouldn't I?"
            "Maybe the best thing would be to just forget about it."
            "Because I want Kat more than I want to complain to her about all of this."
            "So that's what I'm going to have to do."
            "I just hope that I have the strength to pull it off."
            $ kat.flags.confront_sex_cam = False
    return

label kat_event_08c:
    "I haven't told Kat the real reason that I wanted to meet up with her today."
    show kat with dissolve
    "So when she shows up, she has no idea that I'm going to confront her."
    "As far as she's concerned, I guess the fact she fucked another guy isn't an issue."
    "But that's just another point in my favour, a way to catch her off-guard."
    show kat happy at center, traveling(1.5, 1.0, (640, 1040))
    kat.say "Hey, [hero.name]..."
    kat.say "You're looking good today!"
    show kat smile
    mike.say "You really think so, Kat?"
    mike.say "Like, you don't think I'd look better in a mask?"
    mike.say "Maybe a pig mask?"
    show kat confused
    "The moment the words are out of my mouth, everything changes."
    "Kat must know in that instant that the jig is up, that I know everything."
    "But to her credit, she stands her ground and doesn't freak out."
    show kat annoyed
    kat.say "So I guess you saw my last streaming session?"
    mike.say "I saw enough of it, Kat..."
    mike.say "Enough to know what you did."
    "I'm waiting to see how Kat's going to handle this."
    "How she's going to try to explain herself."
    "Hell, if she'll even try to justify it at all."
    show kat sad
    kat.say "So you're really going to do this?"
    mike.say "Looks that way, Kat!"
    show kat angry
    kat.say "Okay, [hero.name]..."
    kat.say "Number one, I gave you the chance to be that guy."
    kat.say "And you were the one that said no - so that's on you."
    kat.say "And number two, don't think you can lecture me about this stuff."
    kat.say "I'm the one making a career out of being a camgirl."
    kat.say "I'm the one taking all the risks too!"
    mike.say "You think that's what this is all about?"
    mike.say "That I'm jealous of that guy?!?"
    kat.say "What else could it be about?"
    "I shake my head at this, unable to believe what I'm hearing."
    mike.say "It's about trust, Kat!"
    mike.say "If you'd told me that's the way it was, I might have changed my mind."
    mike.say "I had no idea you were going to get fucked on camera even if I said no!"
    show kat annoyed
    "Kat doesn't hesitate to fire right back at me."
    "Throwing all of her anger and frustration in my direction."
    show kat angry
    kat.say "I don't have to explain myself to you."
    kat.say "What you're talking about is control, not trust."
    kat.say "If I have to clear everything I do with you, I'm not in control of my own life!"
    show kat sad
    mike.say "What are you even talking about?"
    mike.say "I don't want to control you."
    mike.say "I just want a say in things like sex!"
    show kat angry
    kat.say "No, [hero.name]..."
    kat.say "That's exactly what you're saying."
    kat.say "My body belongs to me, and only to me!"
    kat.say "You don't get a say in what I do with it."
    "I open my mouth to argue."
    "But Kat holds up a hand to silence me."
    with hpunch
    show kat annoyed at center, zoomAt(1.5, (340, 1040)) with ease
    "And then she uses it to push me aside so she can walk away."
    mike.say "Kat..."
    mike.say "Where are you going?"
    mike.say "This conversation isn't over!"
    show kat angry
    kat.say "Oh yes it is."
    kat.say "Just like you and me."
    kat.say "We're done!"
    hide kat with easeoutleft
    "From the look that Kat gives me as she strides away, I know not to follow."
    "And all I can assume is that she was totally sincere in what she just said."
    "As I watch her go, I feel a complex web of emotions churning in my gut."
    "On the one hand I feel vindicated that I stood my ground and made my feelings clear."
    "But of course I also feel crushed that she'd end our relationship on a note like this."
    "I guess Kat's career as a camgirl is more important to her than what he had together."
    "And that's something I'm just going to have to come to terms with."
    $ hero.cancel_activity()
    $ kat.set_gone_forever()
    return

label kat_event_09:
    if kat.love.max < 200:
        $ kat.love.max = 200
    "I'm just walking down the street, minding my own business."
    "It's not too crowded, but somehow I still manage to bump into someone."
    "Out of habit, I turn slightly as I pass them and wave a hand."
    show victor zorder 1 at center, zoomAt (1.5, (740, 1040)), blacker with hpunch
    mike.say "Ah..."
    mike.say "Sorry, man..."
    "fan1" "Urgh..."
    "fan1" "No worries, buddy..."
    show victor at center, zoomAt (1.0, (940, 1040))
    show danny zorder 2 at center, zoomAt (1.5, (340, 1040)), blacker
    with easeinleft
    "I'm about to keep on walking when another guy next to the first chimes up."
    show danny at center, zoomAt (1.0, (440, 1040)) with hpunch
    "And what's even more worrying is that he reaches out and grabs my arm as he does so."
    "fan2" "Hey..."
    "fan2" "Wait a second..."
    "My automatic reaction is to pull away, tearing myself out of his grasp."
    "I take a few steps backwards, trying to put distance between us."
    mike.say "Back off, man..."
    mike.say "Your friend already said it was okay!"
    show victor at center, zoomAt (1.5, (940, 1040)), startle
    "fan1" "Yeah, he's cool."
    show danny at center, zoomAt (1.5, (440, 1040)), startle
    "fan2" "Nah, man..."
    "fan2" "That's him - that's the guy!"
    "I look from one of them to the other, and back again."
    "Because I have no idea what they're talking about."
    mike.say "Look, guys..."
    mike.say "I don't know who you think I am."
    mike.say "But I never saw you before in my life!"
    "The first guy is looking at me more closely as I say this."
    "Screwing up his eyes like he's trying to place me."
    "And then he nods, which can't be a good sign."
    show victor at center, zoomAt (1.5, (940, 1040)), startle
    "fan1" "Fuck me..."
    "fan1" "I think you're right!"
    show danny at center, zoomAt (1.5, (440, 1040)), startle
    "fan2" "I told you - he's Mr Pig!"
    "fan2" "He's the one that's fucking Kat!"
    "All of a sudden, things are beginning to make sense."
    if kat.flags.agree_sex_cam:
        "They must have recognised me from the streaming session with Kat."
        "The one where I fucked her while wearing that damn pig mask."
        "I have no idea how they figured out it was me."
        "So much for her claiming that it'd keep my identity a secret!"
    else:
        "These guys must be fans of Kat's streaming sessions."
        "And one's that saw her fuck that guy in the pig mask too!"
        "I have no idea how they could think it was me."
        "But they seem to be convinced of it all the same."
    mike.say "Come on, guys..."
    mike.say "I know you like her and all that."
    mike.say "But you're not seriously going to fight me over it, are you?"
    "The guys exchange an amused look."
    "And for a moment I think that I might be out of danger."
    "But then they turn their attentions back to me."
    "And I don't like the look in their eyes."
    show victor at center, zoomAt (1.5, (940, 1040)), startle
    "fan1" "Oh, we're not going to beat you up."
    show danny at center, zoomAt (1.5, (440, 1040)), startle
    "fan2" "Nah, we're going to kill you!"
    if (hero.fitness + (10 * hero.has_skill("martial_arts")))>= 80:
        "The two of them try to jump me before I can react."
        "But luckily for me I've been in this kind of spot before."
        "And I've never really taken my eyes off them or let my guard down for a moment."
        show danny at center, zoomAt (1.5, (940, 1040)), startle
        pause 0.2
        play sound woosh_punch
        "The first guy lunges at me, and I easily sidestep the blow."
        show danny at center, zoomAt (1.5, (440, 1040)), startle
        pause 0.2
        play sound woosh_punch
        "And as I turn, I see the second one trying for a sucker-punch."
        "He misses, and I take advantage of his being thrown off-balance."
        play sound punch_hard
        pause 0.2
        with vpunch
        "It's not manly or impressive, but I choose to punt him in the balls."
        hide danny with easeoutbottom
        "Which sends him to the floor in a crumpled ball of pain."
        "By now he first guy has recovered his own balance."
        "He looks determined to do better this time."
        "And a quick glance down at his felled mate seems to enrage him further still."
        "But it's also a big mistake on his part, because it lets me get the first blow in."
        play sound punch_hard
        pause 0.2
        show victor at center, zoomAt (1.5, (940, 1040)), hshake
        "I'm not messing around either, which is why I land a right hand punch on the side of his head."
        play sound punch_hard
        show victor at center, zoomAt (1.5, (940, 1040)), hshake
        "It's more than enough to stagger him, letting me follow up with another punch."
        hide victor with easeoutbottom
        "This one's a left, straight to the jaw, and it sends him down to join his friend."
        "Adrenaline is still pumping through my veins, though my hands are already starting to throb."
        "So I make use of the former to turn on my heel and run away from the scene of the fight."
        "All I can think to do is put as much distance between myself and my attackers as possible."
        call injured from _call_injured_13
        return
    else:
        "The two of them are on me before I can even think."
        "And the fact that I'm not prepared makes things even worse."
        show victor at center, zoomAt (1.5, (940, 1040)), startle
        play sound punch_hard
        pause 0.2
        show danny at center, zoomAt (1.5, (440, 1040)), startle
        with vpunch
        "While I'm trying to fend off one guy, the other sucker-punches me."
        "The blow spins my head around, and I feel my legs buckling too."
        show expression f"bg {game.room}"
        show victor at center, zoomAt (1.5, (940, 1040)), startle
        play sound punch_hard
        pause 0.2
        show danny at center, zoomAt (1.5, (440, 1040)), startle
        show layer master at blur(5)
        with vpunch
        show expression f"bg {game.room}" at center, traveling(1.5, 0.5, (640, 720))
        show victor at center, traveling(1.5, 0.5, (940, 720))
        show danny at center, traveling(1.5, 0.5, (440, 720))
        "But the assault doesn't stop as I crumple to the ground."


        pause 0.2
        with vpunch
        "Now I can feel kicks aimed at my ribs and groin."
        with hpunch
        scene expression "bg {}".format(game.room) at center, zoomAt(1.6, (640, 720))
        show victor at center, zoomAt(2, (940, 720)), blacker
        show danny at center, zoomAt(2, (440, 720)), blacker
        show layer master at blood
        "Some are connecting with my head too, making it hard to focus."
        "All I can think is that they'll get tired soon and stop."
        "They already made their point, and they can't really mean to kill me."
        "Can they?"
        "That's the last thought to pass through my head."
        play sound punch_hard
        pause 0.2
        with vpunch
        scene expression "bg {}".format(game.room) at center, zoomAt(1.6, (640, 720))
        show victor at center, zoomAt(2, (940, 720)), blacker
        show danny at center, zoomAt(2, (440, 720)), blacker
        show layer master at blur(8), blood
        "As a moment later, a kick harder than the ones before connects with my head."
        "And this time it's enough to make me black out completely."
        "Enough to make sure that I never wake up again."
        scene bg black with dissolve
        pause 1.0
        $ renpy.full_restart()

label kat_event_10:
    jack.say "Hey, [hero.name]..."
    "At the familiar sound of Jack's voice, I look up with a smile on my face."
    show jack sad at center, zoomAt(1.0, (840, 720)) with dissolve
    "But that soon fades when I see that he's not smiling himself."
    "In fact he looks like he's pretty pissed about something."
    jack.say "Don't you try and ignore me, mister..."
    jack.say "I've got a bone to pick with you!"
    "I see that Jack's waving something that he's holding in his hand."
    show jack at center, traveling(1.5, 1.0, (640, 1040))
    "But the odd thing is that it looks too small for him to threaten me with it."
    "And it's not until he gets closer still that I realise it's his mobile."
    mike.say "Erm..."
    mike.say "What's the matter, Jack?"
    mike.say "What did I do now?"
    "Jack's still waving his phone in the air as he reaches me."
    with vpunch
    "And he uses the index finger of his other hand to poke me in the chest."
    show jack angry
    jack.say "You couldn't just leave it alone, could you?"
    jack.say "Don't you know that it's nice to share?!?"
    "I'm getting pretty tired of being harangued like this."
    "Especially when I have no idea what I'm supposed to have done."
    show jack at center, zoomAt(1.25, (840, 900)) with hpunch
    "So I give Jack a firm shove, just to get myself some space."
    "And then I hold out my own hand to stop him coming closer again."
    mike.say "Whoa..."
    mike.say "Back up there, big guy!"
    mike.say "You'd better explain yourself, and fast!"
    "By way of answer, Jack holds up his phone."
    scene expression f"bg {game.room}" at dark
    show jack normal zorder 1 at dark, center, zoomAt(1.1, (840, 740))
    show streaming cam interface_fg zorder 2 at center, zoomAt(1.0, (640, 520))
    show streaming_phone zorder 3 at center, zoomAt(1.0, (640, 520))
    with fade
    "And I can see a familiar scene in the video on the screen."
    "There's Kat, sitting in the spot where she usually hosts her livestreams."
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(animated_glitch, offset=3)
    "Though I do note that she seems to be wearing more clothing than usual."
    mike.say "And your point is, Jack?"
    mike.say "I think we already established you like to ogle Kat."
    mike.say "And I don't like to think what else you do in private at the same time!"
    jack.say "That's the whole problem, [hero.name]..."
    jack.say "Thanks to you, I can't do that anymore!"
    mike.say "Make sense, man..."
    mike.say "I never stopped you using your body like an amusement park before."
    mike.say "So what's changed?"
    jack.say "Oooh..."
    jack.say "Just watch the damn stream!"
    "Before I can object, Jack hits play on his phone."
    "And then he all but jams it into my face."
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(animated_glitch, offset=3)
    kat.say "You guys know that I love you all, right?"
    kat.say "And that we've had the best times together too?"
    kat.say "But I've got to tell you something that kind of sucks."
    show streaming sadclosed
    "I was about to tell Jack to go to hell."
    "As well as exactly where he could shove his phone too."
    "But the tone of Kat's voice and her body-language stop me dead."
    show streaming sad
    "She looks so sad and downcast as she's speaking."
    "Yet also like she's resolved to say what she has to say."
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(animated_glitch, offset=3)
    show streaming sadsmile
    kat.say "And that's that I won't be doing this anymore."
    kat.say "Yeah, you heard me right..."
    kat.say "This is officially my last streaming session."
    "Kat pauses in the video as her lap-top goes into meltdown."
    "That must be all of her fans freaking out at the news."
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(animated_glitch, offset=3)
    kat.say "I know, guys, I know..."
    kat.say "But this is the way it's got to be."
    show streaming timid
    kat.say "And why, I hear you all asking?"
    kat.say "Well, that's because while I love you guys..."
    show streaming smile
    kat.say "I'm actually only truly IN love with one guy."
    show streaming annoyed
    kat.say "No, Booblord69, I can't tell you who he is."
    show streaming smile
    kat.say "Uh-uh, Assman2000, I don't want you to hunt him down and kill him!"
    kat.say "You see what I mean, you guys?!?"
    show streaming sadsmile
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(glitch, offset=3)
    pause .1
    show streaming at functools.partial(animated_glitch, offset=3)
    kat.say "Just remember all the good times we had together."
    kat.say "And if you can find it in you, be happy for me and my man, okay?"
    show streaming smile
    kat.say "So keep safe and look after yourselves."
    kat.say "Because that's it - I'm officially retired!"
    hide expression f"bg {game.room}"
    show expression f"bg {game.room}"
    show jack normal zorder 1 at center, zoomAt(1.1, (340, 740))
    with dissolve
    hide streaming
    hide streaming_phone
    with easeoutbottom
    pause 0.5
    show jack at center, zoomAt(1.1, (640, 740)) with ease
    "With that, the video comes to an end."
    "I can't help shaking my head, a huge smile spreading across my face."
    "But Jack seems to think this is all at his expense."
    show jack angry
    jack.say "I hope you're proud of yourself!"
    jack.say "You've ruined the career of a true celebrity."
    jack.say "And you've left her fanbase in tatters!"
    "I finally feel myself snapping out of it and back to reality."
    "Which is something Jack could do with a large dose of too."
    mike.say "Oh shut up, Jack!"
    mike.say "Like any of this is my fault."
    jack.say "She just said she's quitting because of you!"
    mike.say "Well I didn't ask her to do that, you terminal wally!"
    mike.say "And don't act like you're suicidal over it either."
    mike.say "You'll be wanking yourself blind over someone else before the week's out!"
    show jack sad
    "Jack looks suitably chastened by my words."
    "He mutters something under his breath as he puts his phone away."
    "But whatever it is, I don't hear a word."
    "And that's because my head is filled with thoughts of Kat."
    "Is she actually serious?"
    "She's giving up streaming because of her feelings for me?"
    "I have to get a hold on myself as the implications sink in."
    "And I think I can already feel my head swelling too!"
    return

label kat_male_ending:
    $ game.hour = 16


    if jack.flags.engagedmc:
        jump jack_kat_male_ending






    if renpy.has_label("kat_achievement_3") and not game.flags.cheat:
        call kat_achievement_3 from _call_kat_achievement_3
    $ game.room = "church"
    scene bg church wedding with fade
    "I've seen so many movies and TV series with wedding scenes in them that this just feels like a cliche."
    "Standing at the altar in a chapel, wearing a rented suit and waiting impatiently for things to get going."
    "Even now that I'm doing it for real, the whole thing still doesn't seem to read as reality."
    "Ironically it could be some kind of videogame that I've been playing and totally lost myself in."
    "Which would be kind of appropriate, seeing how Kat and I met in the first place."
    "But as soon as I take a moment to reach into the pocket of my pants and pinch myself, I know it's for real."
    mike.say "Ouch!"
    "I thought that I managed to keep my yelp of pain quiet enough to go unheard."
    "But all the same, the priest standing in front of me looks up, with disapproval in his eyes."
    mike.say "Sorry, father...reverend...your grace..."
    mike.say "Just pinching myself, you know?"
    "The look on the priest's face suggests that he very much doesn't."
    "And he opens his mouth to say something, likely a command for me to take this more seriously."
    "But before he can speak a word, music swells and the chapel is suddenly alive with anticipation."
    "The music has a profound effect on me too, because I recognise it as the track Kat chose herself."
    "And I turn around just in time to see the chapel doors open to let her in."
    show kat wedding blush at center, zoomAt(1.0, (640, 720)) with dissolve
    "There must be dozens of faces between us, so many rows of seats all full of guests."
    show kat wedding timid at center, traveling(1.75, 10.0, (640, 1150))
    "Yet the only face that I can make out is Kat's as she walks down the aisle towards me."
    "She's always been something of a shy girl, awkward in some social situations."
    "And yet somehow the dress she's wearing is able to make her the centre of attention."
    "It compliments her demure looks, somehow making the most of them without changing who she appears to be."
    if kat.is_visibly_pregnant:
        "Even the delicate curve of Kat's belly is treated with dignity."
        "Making a subtle statement of the fact that she's pregnant."
        "Rather than shoving the fact into the face of anyone that sees her."
    else:
        "To me there's no sense of the dress turning Kat into a fairytale princess."
        "Because she's already the most beautiful girl in the world to my eyes."
        "Instead it confirms for me what I already knew - that I'm one hell of a lucky guy!"
    "The music fades as Kat reaches the altar and comes to a halt at my side."
    "Now that she's close enough for me to touch, I finally see the smile on her face."
    "It's small and hard to spot unless you know all the quirks of Kat's expressions."
    "And that makes me sure that it's solely intended for me."
    show kat happy
    kat.say "Wow..."
    show kat smile
    kat.say "We made it this far."
    kat.say "We're really doing it!"
    mike.say "I know, Kat..."
    mike.say "How crazy is this?!?"
    "Priest" "Ahem..."
    show kat surprised at startle
    "As one, Kat and I jump a little."
    "Then we turn our attention to the priest."
    "Priest" "I think it's time to get started."
    show kat timid
    "It's a statement, rather than a question."
    show wedding kat with fade
    "One that neither of us is about to query too."
    "The same hush that settles over Kat and me also settles over the assembled guests."
    "And that means that the service can get underway."
    show wedding kat priest with dissolve
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To witness the joining of these two people..."
    "Priest" "In the bonds of holy matrimony."
    "Just like that, we're into the actual meat of the ceremony."
    "But all the same, you don't want to hear every single word."
    "And you definitely don't want to see every minute move we make."
    "What you want is to cut to the chase and see all the good bits."
    "You know, like when the priest says this stuff..."
    "Priest" "Do you, Kat..."
    "Priest" "Take this man, [hero.name]..."
    "Priest" "To be your lawful, wedded husband?"
    kat.say "I do."
    "Priest" "Very good."
    "Priest" "And do you, [hero.name]..."
    "Priest" "Take this woman, Kat..."
    "Priest" "To be your lawful, wedded wife?"
    mike.say "I do."
    "Priest" "Now we're getting somewhere."
    "Now the priest looks over our shoulders and at the assembled guests."
    "Priest" "I call upon those here present..."
    "Priest" "That if you know of any reason these two may not be joined in wedlock..."
    "Priest" "Speak now, or forever hold your peace!"
    "This is the moment that I've been dreading."
    "Because I know that some of Kat's former cam-girl fans might have come along."
    "Let's just say that a lot of them were less than pleased when she quit that line of work."
    "And they found the perfect target for their anger when she added that it was so she could marry me!"
    "Luckily there are no screaming hordes of neck-beards to be seen."
    "Just the customary ripple of gentle laughter from the guests."
    "Priest" "Very well..."
    "Priest" "By the power vested in me..."
    "Priest" "I hereby pronounce you husband and wife."
    "Priest" "You may kiss the bride!"
    "Priest" "Well...it's not compulsory or anything."
    "Priest" "But most people seem keen on doing it..."
    show wedding kat -priest with dissolve
    "Neither of us is really listening to the priest anymore."
    "Because we only have eyes for each other."
    "Kat almost leaps at me, wrapping her arms around my neck."
    scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
    show kat kiss wedding
    with fade
    $ kat.flags.kiss += 1
    "And I catch her, sweeping her up into a passionate kiss."
    "We've done that so many times before, but this time it feels somehow different."
    "Maybe because it's the first time we've done it as a married couple."
    "And so it marks the beginning of a new chapter in our lives together."
    scene bg black
    show kat ending
    with fade
    kat.say "You know it's weird, I always thought that I'd meet someone and it'd be love at first sight."
    kat.say "Okay, maybe that makes me sound more than a little naive."
    kat.say "But I sure as hell thought that I'd at least get on with the person I ended up with from the start."
    kat.say "Of course that means I didn't like [hero.name] when we first met."
    kat.say "Actually, I'd go even further than that."
    kat.say "I'd say that I thought he was a total jerk!"
    kat.say "Erm...no, it wasn't anything that he said or did that made me think that."
    kat.say "It was because he partnered up with one of my rivals on the professional gaming scene."
    kat.say "And before you say it, I know that makes me sound like the jerk, and not him."
    kat.say "But what can I say - I was really into the whole gaming thing back then."
    kat.say "I was good at it, so much so that I was making money."
    kat.say "So I tended to dislike the competition as a matter of course."
    kat.say "Plus it didn't help that he was in a team with [bree.name], who's guts I totally hated."
    kat.say "And yeah, I found out later that she was actually okay too."
    kat.say "Look, it wasn't until after [hero.name] and [bree.name] beat me at my own game that things started to change."
    kat.say "That really shook things up for me."
    kat.say "Because before that I was sure that I was on my way to being the greatest of all time."
    kat.say "Sounds really dumb to admit that now, but I was just that arrogant and up my own ass."
    kat.say "When they beat me, it totally rocked my confidence and shook me to the core."
    kat.say "But it also made me want to find out more about the pair of them too."
    kat.say "I wanted to know what it was they had that meant they could beat me."
    kat.say "And luckily for me, they were able to see beyond our rivalry and accept me as a friend."
    kat.say "That's when I began to learn that their strength wasn't based on some secret strategy."
    kat.say "There was nothing special about the way they played when they were together."
    kat.say "It was more to do with the fact that they played together as equals and friends."
    kat.say "Whereas I just wanted to win at any cost, [hero.name] and [bree.name] had fun."
    kat.say "And I soon began to want to get in on that too."
    kat.say "Well...the truth was that I wanted to get in on it with [hero.name] in particular."
    kat.say "It was hard at first, opening up about my life to him."
    kat.say "I'd been very private up to that point, keeping different things separate."
    kat.say "I never let people from my gaming career into the streaming side of things, and vice versa."
    kat.say "But somehow I knew that I wasn't going to be able to keep any part of my life from [hero.name]."
    kat.say "I don't think that he was too into me being a cam-girl to begin with."
    kat.say "You know, having all those people paying to watch me do things online?"
    kat.say "But he went along with it because I asked him to."
    kat.say "And when the time came to put an end to it and move on, that was my decision too."
    kat.say "Domesticity kind of crept up on me slowly from there."
    kat.say "But the biggest surprise was how natural I found it."
    "[hero.name] and I got married, becoming a typically nauseating couple in love."
    if kat.is_visibly_pregnant:
        kat.say "And when we found out I was going to have a baby, it was perfect."
        kat.say "Mario came along nine months later, and we became a family."
        kat.say "[hero.name] might not be the most confident of fathers."
        kat.say "But his heart is in the right place, and that's what matters."
    else:
        kat.say "So much in love that we're already thinking about starting a family."
        kat.say "We haven't decided to make a go of it just yet."
        kat.say "And I know that [hero.name]'s hiding the fact he's scared of the responsibility."
        kat.say "But I'm sure that he'll muddle through and make a good father in the end."
    kat.say "It's kind of a cliche that [hero.name] got to keep his career."
    kat.say "And doubly so that I decided to stay at home myself."
    kat.say "But I'm not bored or frustrated, far from it."
    kat.say "I actually started streaming again, but just gaming this time."
    kat.say "My fanbase is growing at a slow, but respectable rate."
    kat.say "And no, I'm not as crazily competitive as I used to be back in the day."
    kat.say "But that doesn't mean I'm a pushover either."
    kat.say "Just challenge me to a game, and you'll soon find out that I've still got it!"

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not kat.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_22
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_22
    scene bg black with dissolve
    pause 1.0
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label kat_kink_01:
    if kat.sub.max < 20:
        $ kat.sub.max = 20
    show play console kat
    "Since [bree.name] and I started to build bridges with Kat, we've started to hang out more."
    "And our gaming sessions at my place have begun to be a semi-regular thing."
    "It doesn't have to be all three of us either."
    "More than once I've walked in on [bree.name] and Kat playing on the Zbox."
    "But today it's come down to myself and Kat, as [bree.name] wasn't around when she came over."
    "Normally I'd be playing a pretty intense session with [bree.name], like we're used to."
    "But I'm finding that playing with Kat instead has its own rewards."
    "I mean, I love playing with [bree.name]."
    "But we do kind of know each other pretty well by now."
    "And that means we've played most of the games that we own together many times over."
    "So sometimes it can feel like we're just doing the same thing over and over again."
    "With Kat there's a whole new world of possibilities to explore."
    "We're steadily working our way through my games collection."
    "Plus she's introduced me to a couple that I'd never even heard of before."
    "And some of those are genuine bangers too!"
    scene bg livingroom
    show kat annoyed
    with fade
    kat.say "I still can't believe you never played Undead Island before."
    kat.say "It's like a classic!"
    mike.say "Give me a break, Kat..."
    mike.say "That game was out before I was even born!"
    "Kat scoffs at this, shaking her head at me."
    show kat angry
    kat.say "Like, you think I'm older than you?"
    kat.say "Face it, [hero.name]..."
    show kat defiant
    kat.say "I'm just a more serious connoisseur of video-games than you are!"
    "All I can do in response to that is make a non-commital grunting sound."
    "And then I make a concerted effort to turn my attention back to the game we're playing."
    show play console kat with fade
    "It's a co-op shooter, Kat and I teaming up against some other players online."
    "So far we've been doing well, winning more matches than we've lost."
    "But the guys we're up against this time are surprisingly good."
    mike.say "Wait..."
    mike.say "I...I think I got this guy!"
    kat.say "Be careful..."
    kat.say "These assholes are sneaky as hell!"
    mike.say "Cover me, Kat..."
    mike.say "I'm going to push up on him!"
    kat.say "Go for it..."
    kat.say "I've got your six."
    "My guy on the screen breaks cover and makes a dash for it."
    "And I can feel my heart pounding in my chest as the gambit plays out."
    "The adrenaline is really pumping now, and I'm sure this is going to pay off."
    mike.say "Ha!"
    mike.say "Eat shit, mother-fucker!"
    mike.say "Wait...what?!?"
    mike.say "Where'd he go?!?"
    kat.say "What are you talking about?"
    kat.say "He was right there!"
    kat.say "You had a guaranteed kill!"
    "Suddenly a figure pops up out of nowhere on the screen."
    "I swear he doesn't even put his head around the frame of a nearby door."
    "And yet when he shoots, my guy's peppered with enough lead to down an elephant!"
    "I can't help what happens next, my emotions are too out of control."
    scene bg livingroom with vpunch
    "Leaping up, I throw my joypad down at the same time."


    "It bounces off the floor, probably broken by the impact."
    "But I hardly notice as I start to rant and rave like an impotent prick."
    mike.say "What the hell?!?"
    mike.say "That's total bullshit!"
    mike.say "I had him bang to rights!"
    mike.say "There's no way he saw that coming!"
    mike.say "I'm gonna respawn and fucking kill that guy!"
    show kat confused with dissolve
    "I don't even notice that Kat's got up too."
    "And that she's doing her best to calm me down."
    "It's only when she actually gets in my face that I see her at all."
    kat.say "I know, I know..."
    show kat angry
    kat.say "But you need to calm the fuck down!"
    kat.say "We'll get a mod involved, okay?"
    kat.say "They're probably cheating, using a hack to see through the walls."
    show kat confused
    kat.say "All this rage is going to do is give you a brain haemorrhage!"
    "I'm still flailing my arms around and shaking my head."
    show kat close angry
    "So Kat tries to put herself between me and the TV screen."
    "All the time she's looking up at me, hoping to catch my eye."
    "This means we both have our lips parted at the same time."
    show kat surprised
    "And I just happen to spit at that same moment."
    "I don't mean to do it, it just kind of happens."
    "You might say that I'm almost foaming with rage."
    "But it hits Kat square on, landing in her open mouth and on her lips."
    show kat blush -close
    "She jumps backwards in surprise, and that instantly snaps me out of it."
    mike.say "Oh shit..."
    mike.say "Kat, I'm so sorry..."
    mike.say "I didn't mean to..."
    show kat shy
    "Kat shakes her head, holding one hand up to silence me."
    "And the other she puts to her lips, obviously to wipe away my spit."
    "I can see that she's looking flustered, and I assume that's because she's embarrassed."
    "But as I watch her intently, Kat turns away from me, trying to hide what she's doing."
    "Despite her efforts, I still manage to see her catch the spit on her fingers."
    $ kat.sub += 2
    $ game.active_date.score += 40
    "And to my amazement, instead of wiping it away, she licks it off her fingertips!"
    "I look away as soon as I realise what she's doing."
    "And I just have to hope that she didn't catch me watching her."
    show kat -blush
    kat.say "Okay...okay..."
    kat.say "I'm fine..."
    show kat smile
    kat.say "And you've chilled the fuck out too - which is good!"
    kat.say "Now how about we play something else, yeah?"
    "I nod, eager to forget all about what just happened."
    "So Kat and I set about finding another game to play."
    "Hopefully one that'll be less stress-inducing."
    "But try as I might, I just can't get that image of her out of my head."
    "And I can't figure out why she's want to lick up spit either."
    if do_activity:
        $ do_activity.apply_changes()
    $ hero.cancel_activity()
    return

label kat_kink_02:
    if kat.sub.max < 40:
        $ kat.sub.max = 40
    scene drink_room_pub
    show kat c casual zorder 1 at center, zoomAt(1.75, (440, 1340)), rotation(-10)
    show drink_table_pub_kat_casual as table zorder 2
    show drink_room_fg_pub as fg zorder 3
    with fade
    "It feels like all Kat and I have been doing since we met is feverishly playing video-games."
    "So much so that I'm beginning to think that's all she does for a social life."
    "With that in mind, I make an effort to keep on inviting her along to other places."
    "At first she seems reluctant to come with me, and I start to worry she's a total lock-in."
    "But finally Kat relents and agrees to accompany me to The Winchester for what I promise will be a quiet drink."
    "And once we're actually in the place, I get a pleasant surprise."
    "Because Kat seems to warm up to the idea almost immediately."
    "And before too long she looks like she's really enjoying herself."
    mike.say "You're having a good time, yeah?"
    show kat shy
    kat.say "I...I suppose that I am."
    show kat happy
    kat.say "This is a pretty nice place."
    mike.say "It sure is, Kat..."
    mike.say "That's why I chose to make it my local."
    mike.say "I come in here with friends whenever I get the chance."
    "Kat nods and takes a sip of her drink."
    "Almost without thinking, I do the same."
    show kat normal
    "And I notice that Kat watches me the whole time I'm drinking."
    show kat sadsmile
    "Sure, that seems a little strange."
    "But I just chalk it down to her still feeling a little awkward."
    kat.say "Erm..."
    kat.say "What is that you're drinking, [hero.name]?"
    mike.say "Oh..."
    mike.say "It's just a regular beer, Kat."
    mike.say "I didn't order anything fancy like a craft beer this time."
    show kat normal
    "Kat's still nodding as she stares at my glass."
    "Evidently she's very interested in it."
    "But why that is I couldn't say."
    show kat smile
    kat.say "I have no idea when it comes to stuff like that."
    kat.say "Like, I only ever ordered something like that in a fantasy RPG!"
    kat.say "I don't know what the difference between beer and ale is at all."
    kat.say "Or even if there is a difference!"
    mike.say "Hmm..."
    mike.say "I'm not an expert myself, Kat."
    mike.say "But I think it's something to do with how they make it and what they make it with."
    mike.say "Also, beer tends to have bubbles in it, and ale not so much."
    "Kat points at my glass."
    show kat normal
    kat.say "Can I try it?"
    kat.say "I only tasted beer a couple of times."
    kat.say "So I don't really know if I even like it!"
    mike.say "Sure, Kat..."
    mike.say "Here you go..."
    "I hand the glass over to Kat, keen to indulge her."
    "She takes it and raises the glass to her lips."
    "But before she drinks, I notice that she turns the glass around."
    show kat b yawn
    "In doing so, she makes sure that she's drinking from the same spot as me."
    "It's a little odd, but I just assume it's because of the head."
    "It's a lot thicker where I haven't drunk from the glass."
    "So it makes sense that she'd choose to drink from the same place."
    mike.say "So..."
    mike.say "What do you think?"
    show kat sadsmile
    $ kat.sub += 1
    kat.say "Hmm..."
    kat.say "It's a bit too hoppy for me."
    "I can't help frowning at this."
    show kat b yawn
    "And I'm even more confused when Kat takes a second sip."
    show kat normal
    mike.say "I thought you said you didn't know much about beer, Kat?"
    mike.say "But it sounds like you know all about the way it should taste."
    mike.say "Even like you have a preference too!"
    show kat smile
    "Kat watches me over the rim of my own glass."
    show kat b yawn
    "And she does this as she takes yet another sip."
    mike.say "Plus you're swallowing a lot of a beer you say you don't like!"
    show kat annoyed
    "Kat hurries to put the glass down on the table."
    "And then she shoves it back over to me as she shakes her head."
    show kat confused
    kat.say "What?"
    kat.say "Oh...oh no!"
    show kat annoyed
    kat.say "That stuff about hops, that was just something I overheard once."
    show kat shy blush
    kat.say "Sorry, I was nervous, trying to make myself sound clever!"
    kat.say "And I only kept on drinking because I was listening to you."
    kat.say "I guess I just got distracted, that's all."
    show kat -blush
    "I decide to let it go, as I don't want to upset Kat."
    "We're having a good time together right now."
    "Even if she is acting a little weird."
    "But like she says herself, it'd probably down to nerves."
    mike.say "You know what..."
    mike.say "I'm feeling hungry."
    mike.say "And some food would really help to soak up the alcohol!"
    mike.say "So I'm going to order me up one of The Winchester's famous burgers."
    mike.say "How about you, Kat?"
    mike.say "You hungry too?"
    show kat normal
    "Kat's expression turns thoughtful for a moment."
    "And then she nods."
    show kat smile
    kat.say "Okay..."
    kat.say "But I'll just have some fries."
    kat.say "I'm not hungry enough for a whole burger!"
    scene bg pub with fade
    "I nip off to the bar to order the food."
    "And while I'm there I get us more drinks too."
    scene drink_room_pub
    show kat c casual happy zorder 1 at center, zoomAt(1.75, (440, 1340)), rotation(-10)
    show drink_table_pub_kat_casual as table zorder 2
    show drink_room_fg_pub as fg zorder 3
    with fade
    "When I get back, Kat and I chat about nothing in particular."
    "And either the food is done extra quick."
    "Or else we get lost in the conversation."
    "Because the next thing I know, my burger appears in front of me."
    show kat smile with fade
    mike.say "Right, Kat..."
    mike.say "No more time for talking."
    mike.say "Now I have to use my mouth for eating!"
    show kat happy
    "Kat chuckles and begins to eat some of her fries."
    show kat defiant
    "But I can see that she's watching me as I take my first bite."
    "It kind of feels a little strange to have someone watching me eat."
    "And understand that I don't mean Kat's just looking in my direction."
    "She's literally staring, an uneaten fry in her hand and her mouth hanging open."
    "After a couple of bites, I feel the need to call her out on it."
    mike.say "You keep staring at me, Kat..."
    mike.say "What's up?"
    mike.say "Are you wishing you ordered the burger too?"
    show kat surprised
    "My words seem to snap Kat out of it and back to reality."
    "She shakes her head, as if trying to clear away the cobwebs."
    kat.say "Huh?"
    show kat confused
    kat.say "Oh...oh yeah!"
    show kat shy
    kat.say "It just looks so good..."
    kat.say "But I still don't think I could eat one all to myself!"
    "I put the burger down on the plate and push it towards Kat."
    mike.say "It's no hassle, Kat..."
    mike.say "Here, have a bite or two."
    mike.say "I don't mind sharing it with you."
    show kat smile
    "Kat smiles as she reaches out to pick up the burger."
    "And I watch again as she turns it around before taking a bite."
    show kat b yawn
    "Like with the drink before, I was expecting her to bite the other side."
    "Instead she seems determined to take a bite right where I just did."
    show kat happy
    $ kat.sub += 1
    kat.say "Mmm!"
    "Kat speaks through a mouthful of burger."
    kat.say "That's one good burger!"
    show kat smile
    kat.say "I have to order one of these the next time we come here."
    "I'm still a little puzzled with the way Kat's choosing to eat."
    "But the fact she sounds keen on doing this again kind of distracts me."
    "Because what do a couple of strange habits matter?"
    "Especially when you balance that against the chance to have a good time with a hot girl!"
    "So I just put the images out of my head for now."
    "And instead I focus all of my efforts on chatting to Kat."
    "Because hopefully this is the beginning of something special between us."
    if do_activity:
        $ do_activity.apply_changes()
    $ hero.cancel_activity()
    return

label kat_kink_03:
    show kat smile
    "You know how it feels when you just know that the time is right."
    "Everything clicks and you almost unconsciously begin to make the first move."
    show kat at center, zoomAt(2.0, (640, 1340)) with fade
    "You're leaning in, looking the girl in the eye while connecting on a higher level."
    scene expression f"bg {game.room}" at blur(16), dark, dark
    show kat at center, zoomAt(2.0, (640, 1340)), blur(16), dark, dark
    with wipedown
    "Then you close your eyes, knowing that your lips will touch any moment."
    "Will she slip you a little tongue into the mix?"
    "Will you dare to do that yourself?"
    "Then she sticks a finger in the way, stopping you dead in your tracks."
    "Wait...what?!?"
    "That's not what's supposed to be happening here!"
    scene bg black
    $ renpy.show(f"bg {game.room}")
    show kat at center, zoomAt(2.0, (640, 1340))
    with wipeup
    "My eyes burst open and I try to speak."
    "But Kat's fingers are pressed against my lips."
    "So my words come out slurred and incoherent."
    mike.say "Kat..."
    mike.say "Wha..."
    mike.say "What are you..."
    "Kat responds by quickly pulling her hand away from my mouth."
    show kat shy
    "And she looks away as I stare at her in a state of total confusion."
    "Like she's too embarrassed to look me in the eye right now."
    kat.say "I..."
    kat.say "I'm sorry!"
    kat.say "I just..."
    kat.say "I just wasn't ready for you to kiss me yet!"
    "I narrow my eyes as I look at Kat."
    "Because that sounds like a pretty lame excuse."
    mike.say "Look, Kat..."
    mike.say "You can be honest with me."
    mike.say "If you don't like the thought of kissing me, just say so."
    mike.say "I can take it, you know?"
    show kat confused
    "Kat finally summons up the courage to look me in the eye."
    "And when she does so I can see that there's some serious feelings at play here."
    "She looks conflicted, like she's wrestling with something inside."
    kat.say "That's not it - not at all!"
    kat.say "I just..."
    show kat shy blush
    kat.say "I don't know how to ask you this..."
    mike.say "Well there are only two choices, as far as I see it."
    mike.say "Either you do or you don't!"
    kat.say "But if I do..."
    show kat afraid
    kat.say "You might not like what I have to say!"
    mike.say "And if you don't..."
    mike.say "Things are always going to be awkward between us."
    mike.say "So you need to decide which option is worse!"
    show kat shy -blush
    "Kat looks down at her feet again."
    "But then she nods her head."
    "And when she looks up again, I can see that she's made her decision."
    show kat sad
    kat.say "Okay, [hero.name]..."
    kat.say "I..."
    show kat afraid blush
    kat.say "I want you to spit in my mouth!"
    "I blink and remain silent for an extended moment."
    "Mainly because I can't seem to make sense of what Kat just said."
    mike.say "I'm sorry..."
    mike.say "You want me to spit?"
    show kat confused
    kat.say "Yes."
    mike.say "To spit in your mouth?!?"
    kat.say "That's right - I want you to spit in my mouth."
    show kat shy
    kat.say "I've...always wanted to know what it feels like."
    kat.say "And what it tastes like too."
    kat.say "But I never felt comfortable enough with anyone to ask."
    show kat sadsmile
    kat.say "That is, not until I met you!"
    "I'm still kind of reeling from Kat's request."
    "But as my mind starts to clear, things begin to fall into place."
    "I remember Kat licking it up when I accidentally spat in her mouth."
    "Then I recall her sharing my food and some of my beer."
    "How she always made sure to eat and drink from the same place as my mouth had been."
    "Oh man..."
    "I always thought the dream was a girl admitting that she wants to try something new."
    "Preferably something exciting that tends to happen in the confines of her bedroom."
    "Just my luck that I'd end up with the one that wants to be used as a human spittoon!"
    show kat smile
    kat.say "Well..."
    kat.say "Will you do it for me?"
    menu:
        "I'll give you what you want":
            if kat.sub.max < 60:
                $ kat.sub.max = 60
            "God knows that I've done a lot of things to impress women over the years."
            "So many that I've probably forgotten more than I can ever hope to remember."
            "And is this really that different?"
            "Plus, people don't exactly get to choose what turns them on."
            "So I should maybe cut Kat some slack here."
            mike.say "Okay, Kat..."
            mike.say "I won't lie - this does feel more than a little weird."
            mike.say "But if you're sure that's what you want..."
            show kat surprised -blush
            mike.say "Then I'll give it a go."
            "Kat looks like she almost doesn't believe me."
            "She blinks a couple of times before she speaks."
            kat.say "You're serious?"
            show kat sad
            kat.say "Because if not, don't screw around with me, okay?"
            kat.say "You don't know how much I need this!"
            mike.say "No, Kat..."
            mike.say "I'm totally serious."
            show kat normal
            "Kat nods."
            kat.say "Okay then..."
            show kat smile
            kat.say "No time like the present!"
            show kat yawn
            "With that, she opens her mouth wide."
            "And she leans her head back to make my job easier."
            "Okay, here goes nothing!"
            show kat at center, traveling(2.5, 1.0, (640, 1640))
            "I try to make sure what I have in my mouth when I spit is just plain saliva."
            "Because I have no idea where phlegm comes into this kind of thing, if at all."
            "And when I'm satisfied I have enough of it in my mouth, I spit it into Kat's."
            show kat blush
            "As soon as it hits her tongue, she reacts in a very physical and dramatic way."
            show kat sadclosed
            "Her tongue writhes and she quickly closed her mouth."
            "Part of me is honestly expecting her to spit it out and tell me off any moment."
            "But instead, Kat swallows in a very clearly sensual manner."
            "Like she's just swallowed the most delicious thing imaginable."
            "Her eyes are closed, her cheeks flushed with colour."
            "And I swear that she's almost quivering too!"
            "All I can do is stand there, watching in amazement."
            show kat happy
            $ kat.sub += 4
            "It looks like she was telling the truth all along."
            "This really is something that she gets off on!"
        "... disgusting...":
            "God knows that I've done a lot of things to impress women over the years."
            "So many that I've probably forgotten more than I can ever hope to remember."
            "But spitting in someone's mouth?"
            "That's where even I have to draw the line!"
            mike.say "Urgh..."
            show kat shocked -blush
            mike.say "That's the most disgusting thing I've ever heard, Kat!"
            mike.say "No, I am not going to spit in your mouth."
            "Kat's expression becomes pleading as she hears this."
            "And she does the best that she can to argue her case."
            show kat sad
            kat.say "[hero.name]..."
            kat.say "I'm kind of opening up to you here."
            kat.say "You know, sharing one of my deepest secrets?"
            show kat sadclosed
            kat.say "One of my most personal fetishes!"
            show kat sad
            mike.say "Maybe you should have kept it a secret, Kat."
            mike.say "I mean, you couldn't have maybe had a different fetish?"
            mike.say "A fun one like wanting to be tied up during sex?"
            mike.say "Even wanting to call me 'Daddy' would be less embarrassing!"
            kat.say "Well, I'm sorry..."
            kat.say "People don't get to choose their fetishes, do they!"
            show kat offended
            $ kat.sub -= 5
            $ kat.love -= 10
            mike.say "You're damn right - because nobody sane would choose that one!"
            show kat angry
            "For a moment I actually think that Kat's going to slap me."
            hide kat with easeoutright
            "But then she just balls her fists up and walks away."
            "Which is probably the most sensible choice right now."
            "Because I think I need some time and space to absorb that last revelation."
    if do_activity:
        $ do_activity.apply_changes()
    $ hero.cancel_activity()
    return

label kat_kink_04:
    if kat.sub.max < 80:
        $ kat.sub.max = 80
    show kat
    "It's been a couple of days since the subject of Kat's rather interesting predilections came out."
    "And while I was kind of surprised and a little freaked out to begin with, I feel like that's changed."
    "Now that I've had the time to really think it all over, the whole thing doesn't seem nearly as strange."
    "I mean, I've read stuff on the internet and seen some things that left me feeling downright queasy."
    "And what Kat explained to me the other day seems to pale in comparison to all of that."
    "So when I next see her, I get the urge to tell her as much almost with my first breath."
    "But I manage to stop myself at the last minute, thinking better of it."
    "Because even if we're both cool with it now, I doubt Kat wants to make it such a big deal."
    show kat at center, traveling (1.5, 1.0, (640, 1040))
    mike.say "Hey, Kat..."
    mike.say "You look great today!"
    show kat smile
    kat.say "Hey, [hero.name]..."
    kat.say "Thanks for the compliment!"
    show kat surprised
    kat.say "Oh, and I just wanted to say..."
    show kat happy
    kat.say "I'm still super grateful about how you handled the whole spitting and drooling thing."
    "I blink in genuine amazement, totally caught off-guard."
    "It looks like I was totally wrong."
    "Kat obviously does want to make a big thing out of it after all!"
    mike.say "Oh..."
    mike.say "Well, you know..."
    mike.say "Like I said at the time, it's no big deal."
    show kat confused
    mike.say "I mean, we all have our little quirks, don't we?"
    "I force what I hope is a casual smile onto my face as I say all of this."
    "And my hope is that it'll be enough to convince Kat that it's nothing to worry about."
    "Or at least that it's nothing we need to discuss every time we meet up."
    show kat angry
    "But all I manage to do is make the look on her face become more serious."
    "And she shakes her head, dismissing the sentiment of my words."
    show kat enthusiastic
    kat.say "Oh, no!"
    kat.say "Oh, hell not it isn't!"
    kat.say "Knowing that you accept me for who I really am is totally liberating."
    kat.say "You have no idea what it's like to be hiding a secret like that, [hero.name]."
    "All I can do in response to that is give Kat a firm nod of the head."
    "Because she's damn right on that score!"
    show kat sadsmile
    kat.say "I've been hiding it from people for as long as I can remember."
    kat.say "Always knowing that it was a part of who I really am."
    kat.say "But at the same time, also knowing how people would judge me if they knew."
    "Again I find myself nodding at all that Kat has to say on the matter."
    "I can easily imagine how most people would react to being told something like that."
    "And as I listen to her explain herself, I'm slowly beginning to appreciate her sentiment."
    mike.say "People can be really mean, Kat."
    mike.say "Like, totally closed-minded."
    mike.say "I mean, it's not like you're hurting anyone else, is it?"
    show kat smile
    "Now it's Kat's turn to nod as she becomes more confident in herself."
    "And it's kind of crazy to see how much my supporting her is helping."
    "She seems to be getting more firm in her conviction with every passing second."
    show kat happy
    kat.say "You're damn right, [hero.name]!"
    show kat smile
    kat.say "I'm not walking up to complete strangers and asking them to spit in my mouth!"
    kat.say "This is, like, a totally private thing between consenting adults."
    "Even when Kat came out and told me about all of this, I had no idea it was so important to her."
    "And that fact is already making me see the whole thing in a different light."
    "Apparently this is a big part of what gets Kat's motor running."
    "So I need to start embracing it along with all the other elements of her personality."
    mike.say "Well, just so you know..."
    mike.say "This adult is totally down with it."
    mike.say "Whatever you need, Kat..."
    mike.say "Just let me know, and I'll make it happen."
    show kat smileclosed at center, traveling (2.0, 1.0, (640, 1340))
    "Kat lets out a sigh and rests her head on my shoulder."
    kat.say "Oh, [hero.name]..."
    kat.say "I'm so lucky to have found a guy like you."
    mike.say "No, Kat..."
    mike.say "I think I'm the lucky one here!"
    return

label kat_kink_05:
    show kat shy at center, zoomAt(1.5, (640, 1040))
    "Things seem to be going really well with Kat and me."
    "Whenever we spend time together, I'm loving every moment of it."
    "And I'm pretty sure that she's having a good time too."
    "Plus there's nothing getting in the way of those good times either."
    "Well, nothing apart from the usual little hiccups you find in any relationship."
    show kat timid
    "So it kind of comes as a surprise when I find Kat looking at me in just such a way."
    show kat shy
    "The kind of way that all guys can spot on sheer, base instinct alone."
    "The way that means she has something she wants to say to me."
    mike.say "Ah, Kat..."
    mike.say "Was there something you wanted to ask me?"
    show kat busted
    "Kat blinks and shakes her head as soon as I say this."
    "Which lets me know that she's surprised in turn."
    show kat surprised
    kat.say "Wait a minute..."
    kat.say "How did you know that?"
    show kat timid
    kat.say "Guys are supposed to be clueless about that kind of thing!"
    "All I can do is shrug and offer up a helpless smile."
    mike.say "Even us guys get wise to it sooner or later, I guess!"
    mike.say "So..."
    mike.say "I am right?"
    mike.say "There is something you wanted to say to me?"
    show kat shy blush
    "By now Kat's beginning to look pretty awkward."
    "She's unable to look me straight in the eye."
    "And so she keeps glancing away and then back to me every couple of seconds."
    kat.say "Uhm..."
    show kat timid
    kat.say "Yeah..."
    show kat shy
    kat.say "I mean, I guess so."
    kat.say "It's kind of hard when you put me on the spot like this!"
    "I can't help finding that ironic."
    "Because my guess is that Kat was about to do the very same thing to me."
    "But I'm doing my best not to be an asshole about the whole situation."
    "I can see that she's struggling right now, so I put on an understanding face."
    mike.say "Look, Kat..."
    mike.say "Let's just forget about all of that stuff, okay?"
    mike.say "Instead, how about we pretend I never rumbled you?"
    mike.say "Just go ahead and ask your question."
    mike.say "And I promise you an honest answer."
    show kat timid -blush
    "Kat hesitates for a moment."
    "And part of me thinks that she's going to turn me down."
    show kat afraid
    "But then she seems to rally her spirits."
    show kat yawn
    "Kat nods and takes a deep breath, then she begins to speak."
    kat.say "Okay, here goes..."
    show kat confused
    kat.say "This kind of thing isn't exactly fashionable right now."
    kat.say "So it's something that I've never felt able to tell any of my previous partners."
    show kat smile
    kat.say "But with you, I feel different - like we have a deeper connection."
    kat.say "The kind of connection that means you'll understand it."
    "Oh boy!"
    "Just what I needed to hear today - a confession of some kind!"
    "All I can do is keep nodding as I listen to what Kat has to say."
    "To wait for her to explain herself and then give an honest reaction."
    "I just hope it's something I can handle, and that she's cool with my response."
    mike.say "It's okay, Kat..."
    mike.say "You can say what you need to say."
    mike.say "I'm here and I'm listening."
    show kat shy
    kat.say "Well, it's like this..."
    show kat blush
    kat.say "I've always wanted to devote myself to one guy, and one guy alone."
    "Kat pauses, apparently to let the implications of this sink in."
    "But I find myself blinking and beginning to frown."
    "Because I can't really see the significance of what she just said."
    mike.say "But..."
    mike.say "But aren't we doing that right now, Kat?"
    mike.say "You and me, we're in an exclusive relationship."
    mike.say "So you already pulled it off, right?"
    show kat afraid -blush
    "Kat shakes her head, frowning a little as she does so."
    kat.say "No, no, no..."
    kat.say "That's not what I mean!"
    show kat timid blush
    kat.say "I mean I want to give myself to that guy."
    kat.say "I want him to own me, body, mind and soul!"
    "By now my eyes are wide open, almost popping out of their sockets."
    "And I can feel my heart beginning to race in my chest too."
    mike.say "You..."
    mike.say "You mean..."
    show kat sadsmile
    kat.say "Yes, [hero.name]…"
    kat.say "I want you to be that guy!"
    kat.say "So what's your answer?"
    kat.say "Will you let me give myself to you, totally and utterly?"
    menu:
        "By Salt, Mercury and Sulfur you are now mine!":
            if kat.sub.max < 100:
                $ kat.sub.max = 100
            "The question kind of throws me, leaving my head spinning."
            "I never even thought of being in a relationship like that before now."
            "Because you have to admit, it's not exactly a modern way of behaving."
            "But the more I think about it, the more I find myself warming to the idea."
            "I'm starting to see the advantages of having Kat obey my every command."
            "And the best thing is that she seems to want it so badly."
            "So I wouldn't even have to feel guilty about it, would I?"
            mike.say "Well..."
            mike.say "I mean, I guess we could try it out."
            mike.say "If that's what you really want?"
            show kat happy
            "Kat's already nodding eagerly."
            "Then she reaches out and grabs hold of my hands."
            kat.say "Of course it is!"
            show kat smile
            kat.say "Oh, [hero.name]…"
            show kat smileclosed
            kat.say "This is going to be perfect!"
            kat.say "So long as you remember that you have to act like you own me, right?"
            show kat smile
            kat.say "You think you can do that for me?"
            mike.say "Oh, don't worry, Kat..."
            mike.say "I'm sure I can manage that!"
            $ game.active_date.score += 20
        "Sorry but I don't want you to turn as a pet":
            "I've been able to get my head around most of the stuff that Kat's asked of my so far."
            "But I think I just found my limit as far as she's concerned."
            "And that's because I'm a thoroughly modern kind of guy."
            "I want to be in a relationship with an equal, not lording it over her like a slave!"
            show kat surprised -blush
            mike.say "I'm sorry, Kat..."
            mike.say "But that's just not the kind of guy I am."
            mike.say "I want a partner, not a pet!"
            show kat confused
            "Kat begins to shake her head almost as soon as she hears my response."
            kat.say "Please think about it, [hero.name]…"
            kat.say "I'm sure we could make it work."
            kat.say "You know, figure out how to make it more modern?"
            mike.say "I'm sorry, Kat..."
            mike.say "But the answer is no."
            show kat sad
            "Kat opens her mouth, as if she's going to argue."
            "But then she looks down at her feet and nods."
            "Which I assume means that she's willing to let the matter drop."
            $ game.active_date.score -= 20
    return

label kat_kink_06:
    show kat
    "Things have been so great between Kat and me since I agreed to let her devote herself to me."
    "And yeah, I know that sounds pretty obvious and that it's a sweet deal from my point of view."
    "But I'm being serious when I say all of that, because it seems to have eliminated all of our problems too."
    "With Kat accepting me as the boss in every sense and situation, things are so much simpler for us."
    "There's no need for us to argue over anything, because the decision is always mine to make."
    "And before you say it, it's not like Kat's unable to think for herself either."
    "She's perfectly at liberty to come to me and ask for anything that she could want."
    "But she accepts that my word on that is final, just like it is for everything else."
    "The best thing of all is that all of this seems to be making Kat happier than ever too!"
    "I'm serious when I say that she always has a smile on her face these days."
    "And I think that having the need to make decisions for herself has kind of liberated her."
    "Not that I don't sometimes feel the need to check up on all of that..."
    mike.say "Kat..."
    show kat smile at center, traveling (1.5, 1.0, (640, 1040))
    "At the sound of my saying her name, Kat instantly looks up."
    "She doesn't hesitate to meet my gaze, smiling eagerly as she does so."
    "All in all, she looks like she's waiting with baited breath for whatever I have to say to her."
    kat.say "Yes, [hero.name]?"
    kat.say "Did you have something you wanted to ask me?"
    show kat smileclosed
    kat.say "Because if so, I'm all ears!"
    kat.say "So just go ahead and ask me anything!"
    show kat normal
    mike.say "Erm..."
    mike.say "Okay, Kat..."
    mike.say "I just wanted to ask if you were okay, that's all."
    show kat smile
    "If anything, Kat's smile becomes wider still as she hears my question."
    "And she begins to nod her head even before she utters a word in answer."
    show kat happy
    kat.say "Of course I am!"
    kat.say "How could I be anything but okay?"
    kat.say "I have the bestest boyfriend in the whole world!"
    show kat smile
    "I'm nodding too by this point."
    "Only mine are far slower and more careful than Kat's."
    mike.say "Yeah..."
    mike.say "That's...good, that's very good."
    mike.say "So long as you're fine, Kat."
    "Kat keeps right on smiling as the conversation seems to be coming to an end."
    "And she's trying so hard to keep it up that I almost miss the subtle twitch in the corner of her mouth."
    "But once I see it, I can't ignore it."
    mike.say "Kat..."
    show kat shy
    kat.say "Oh..."
    kat.say "Oh damn it!"
    mike.say "What's the matter, Kat?"
    mike.say "Whatever it is, you can tell me."
    show kat yawn
    "Kat finally lets her guard down, releasing a frustrated sigh."
    show kat annoyed
    kat.say "Okay, okay..."
    kat.say "But first I want to say that this has nothing to do with how I asked you to treat me."
    show kat normal
    kat.say "I'm loving being devoted to you like this, and I don't want that to change."
    kat.say "You got that?"
    "I nod, doing the best I can to show that I understand."
    show kat shy
    kat.say "Right..."
    kat.say "How do I say this the right way?"
    show kat defiant
    kat.say "Ah, fuck it..."
    kat.say "I'll just come out with it and then we can haggle over the finer points."
    "I have to bite my lip as I wait to hear what Kat has to say for herself."
    "Because I'm more than a little worried this could affect what I have going here."
    "But I'm also sure that trying to shut her down would make that patently obvious."
    "And a show of chauvinistic selfishness is not going to help my case one bit."
    kat.say "Okay..."
    kat.say "Like I already said, I love how you've been treating me, [hero.name]."
    kat.say "It's kind of like a dream come true for me."
    show kat shy
    kat.say "But..."
    "Urgh..."
    "Why does there always have to be a 'but'?"
    show kat annoyed
    kat.say "But it's not enough!"
    "I was so prepared to hear something else that Kat's meaning escapes me at first."
    "So much so that I find myself blinking in confusion."
    mike.say "What do you mean by that?"
    mike.say "What more do you want?"
    show kat confused
    "Kat instantly looks anxious, like she thinks she's pissed me off."
    kat.say "I know, I know..."
    kat.say "It sounds crazy, right?"
    kat.say "How could I ask anything more of you?"
    show kat blush
    kat.say "But I so dearly want to be able to call you my master!"
    show kat shy
    kat.say "That and to totally devote my life to you!"
    "Again I find myself almost lost for words."
    mike.say "You want to what?!?"
    show kat afraid
    kat.say "To serve you for the rest of my life!"
    show kat timid
    kat.say "Would you even consider letting me do that?"
    menu:
        "My word is final and my word is \"yes\"":
            "I kind of thought that we'd gone as far down this road as possible."
            "But the moment Kat floats the idea, I know that I want to go further still."
            "Because the idea of being Kat's master for life sounds like the ultimate win!"
            show kat surprised -blush
            mike.say "Of course I would!"
            mike.say "I...I mean..."
            mike.say "Yeah, if that's what you want?"
            "Kat nods, her eyes lighting up at my answer."
            kat.say "You mean it?"
            show kat enthusiastic
            kat.say "That's a yes?!?"
            "I'm nodding too, and that seems to be enough for Kat."
            show kat smileclosed
            $ kat.love += 5
            "She throws her arms around me, practically jumping into my embrace."
            $ kat.status = "sex slave"
            $ kat.flags.mikeNickname = "Master"
            kat.say "Oh, Master!"
            kat.say "Oooh..."
            kat.say "That sounds so good, so right!"
            mike.say "It sure does, Kat!"
        "That might be going a bit too far for me...":
            "I always wondered if there was a limit for me."
            "But it looks like there most certainly is."
            "And that I just found it too."
            mike.say "No way, Kat..."
            mike.say "I can do all the fetish stuff."
            mike.say "I can even handle you letting me own you."
            mike.say "But being like some lord and master is just too much."
            show kat sad
            kat.say "You can't be serious?!?"
            kat.say "This isn't that much different to what we have going on right now."
            show kat whinge
            kat.say "In fact, if you think about it, it's kind of a logical progression!"
            "I shake my head, reaffirming my answer."
            mike.say "Sorry, Kat..."
            mike.say "But it's a no."
            mike.say "I'll go this far and no further."
            "Kat looks like she's about to argue some more."
            show kat sad
            $ kat.love -= 5
            "But then she seems to think better of it."
            "Instead she simply nods and lets the matter drop."
    return

label kat_jack_01:
    scene expression f"bg {game.room}"
    show jack
    with fade
    jack.say "Hey dude, ready to go?"
    mike.say "Yep, lead the way."
    scene bg gamestore
    show sasha as gamer3 zorder 1 at flip, center, zoomAt (1.25, (1060, 840)), blacker
    show ryan as gamer2 zorder 2 at center, zoomAt (1.25, (860, 840)), blacker
    show alexis b as gamer4 zorder 3 at flip, center, zoomAt (1.25, (660, 840)), blacker
    show scottie as gamer5 zorder 4 at flip, center, zoomAt (1.25, (460, 840)), blacker
    with fade
    show jack zorder 5 at center, zoomAt (1.25, (260, 840)) with easeinleft
    "The room is far more noisy and full of people than I was expecting when I agreed to come here with Jack."
    "So I guess the streamers and online influencers that are appearing at this signing session are a pretty big deal."
    "Hell, I was so casual about coming along that I didn't even bother to check who was actually going to be here."
    "But even as I'm looking around at the lines leading up to the tables, I already recognise some of the names."
    "Of course every one of them has signs and banners with their name and likeness all over them."
    "Which is a good thing too, because it's impossible to see the actual people at the tables over the sea of heads."
    show jack happy
    jack.say "This is great!"
    jack.say "This is so great!"
    show jack smile
    jack.say "Isn't it, [hero.name]?"
    jack.say "Isn't it great?!?"
    "Jack's literally jumping up and down with glee as he says this."
    with hpunch
    "And he's yanking on my arm too, so hard I worry he'll dislocate my shoulder."
    "I nod as I make an effort to pull myself out of his grasp."
    "But more to placate him than out of a genuine sense of agreement."
    mike.say "Yeah, Jack..."
    mike.say "It's great."
    mike.say "So...do you see anyone in particular you want to do?"
    "Jack responds by jabbing me in the ribs with his elbow."
    jack.say "Hell yeah!"
    show jack perv
    jack.say "I can see more than a few actresses I'd love to 'do'!"
    jack.say "But I think we're just supposed to ask for photos and autographs!"
    mike.say "Very funny, Jack..."
    mike.say "But you know what I mean."
    mike.say "These lines are pretty long."
    mike.say "And it looks like it's only going to get worse."
    show jack normal
    jack.say "Don't worry, man..."
    jack.say "I have it all planned out!"
    "Jack opens his backpack and shows me what's inside."
    "Leaning in closer, I see that it's packed to bursting with stuff."
    "There are posters, glossy photos, books, CDs and DVDs too."
    mike.say "No way..."
    mike.say "No way are you going to get all that shit signed!"
    "Jack taps his nose with the tip of his finger."
    jack.say "Oh yeah?"
    jack.say "Just stand back and watch a professional at work, my friend!"
    "With that, Jack dives straight into the first line."
    "And just like that, we're into it."
    scene bg black with timelaps
    scene bg gamestore
    show kat happy zorder 1 at center, zoomAt (1.1, (820, 900)), blacker
    show ryan as gamer3 zorder 2 at flip, center, zoomAt (1.25, (1060, 840)), blacker
    show sasha as gamer2 zorder 3 at center, zoomAt (1.25, (860, 840)), blacker
    show scottie as gamer4 zorder 4 at flip, center, zoomAt (1.25, (660, 840)), blacker
    show alexis b as gamer5 zorder 5 at flip, center, zoomAt (1.25, (460, 840)), blacker
    show jack zorder 6 at center, zoomAt (1.25, (260, 840))
    with timelaps
    "In the hours that follow, I'm dragged in front of a myriad of faces."
    "Some are familiar and others leave me clueless as to who they actually are."
    "But there they all are, posing awkwardly with me and Jack."
    "All recorded for posterity in the photos on his cell phone."
    "One thing that I do notice is that there's a definite pattern to Jack's targets."
    "In fact I'd swear that not a single one of them was male."
    "Which makes me think that Jack really is a professional."
    "To be precise, a professional sleaze!"
    "So I just resign myself to following in Jack's wake."
    "Soon enough there's a routine to how it goes down."
    "We endure an agonising wait in the queue."
    show ryan as gamer3 at flip, center, zoomAt (1.25, (1360, 840)), blacker
    show sasha as gamer2 at center, zoomAt (1.25, (1160, 840)), blacker
    show scottie as gamer4 at flip, center, zoomAt (1.25, (160, 840)), blacker
    show alexis b as gamer5 at flip, center, zoomAt (1.25, (-160, 840)), blacker
    show jack at center, zoomAt (1.25, (540, 840))
    with ease
    "Then Jack gushes all over the next supposedly famous girl we meet."
    "I just stand to the side, offering an occasional smile and a laugh."
    "After that, Jack guilts them into signing the merch that he's brought with him."
    "All the while ignoring their pleas to buy something for them to sign instead."
    "And this keeps up until we come to the last person on Jack's list."
    show jack perv
    jack.say "Ooh yeah..."
    jack.say "This is that gamer-girl I told you about the other day."
    jack.say "The really cute one with the violet hair!"
    "Suddenly I remember that Jack did show me one of Kat's videos."
    "And looking up, I see that he's right."
    "The table in front of us is covered in pictures of Kat's face."
    hide kat
    show kat happy zorder 1 at center, zoomAt (1.1, (820, 900))
    with dissolve
    "And there she is, sitting behind it, smiling at her adoring fans!"
    jack.say "Oh man..."
    jack.say "This is going to be so great!"
    show kat surprised at center, zoomAt (1.0, (820, 900)), startle
    show jack surprised at center, zoomAt (1.0, (440, 840)), hshake
    "But as soon as we get to the front of the queue, Jack gets a shock."
    "Because Kat totally ignores him, instead looking straight at me."
    show kat smile at center, zoomAt (1.0, (820, 740)) with ease
    show kat zorder 3 at center, traveling (1.25, 1.0, (780, 840))
    kat.say "Hey, [hero.name]!"
    kat.say "What are you doing here?"
    "Jack literally gawps at this, looking from me to Kat and then back again."
    show jack at center, zoomAt (1.25, (340, 840)) with ease
    if jack.flags.heard_about_kat:
        jack.say "No way!"
        jack.say "No fucking way!"
        jack.say "You weren't screwing with me?"
        jack.say "You really know her?!?"
        "All I can do is shrug and shake my head."
        mike.say "I told you so, Jack."
        mike.say "It's not my fault you wouldn't believe me."
    else:
        jack.say "What the hell?"
        jack.say "What the actual hell, man?!?"
        jack.say "You never told me that you knew her!"
        "All I can do is shrug and shake my head."
        mike.say "Would you have believed me if I had?"
        mike.say "You were too busy gushing over her to even hear a word I said!"
    show kat normal
    kat.say "Ahem..."
    "At the sound of Kat clearing her throat, we both turn to face her."
    kat.say "It's great to see you, [hero.name]..."
    show kat sad
    kat.say "But I'm afraid that I don't have time to hang-out right now."
    kat.say "There's still a queue of people in line behind you!"
    "I nod and take the liberty of shoving Jack forwards."
    mike.say "Okay, Kat..."
    show kat normal at center, zoomAt (1.25, (840, 840))
    show jack normal at center, zoomAt (1.25, (420, 840))
    with ease
    mike.say "This is my friend Jack."
    mike.say "He's a really big fan of yours."
    kat.say "He is?"
    show kat happy
    $ kat.love += 2
    kat.say "That's amazing!"
    kat.say "What is it about my work you like, Jack?"
    show kat smile
    kat.say "Anything in particular?"
    "Kat and I both look at Jack."
    "Patiently waiting for an answer."
    show jack blush
    jack.say "I..."
    jack.say "Erm..."
    jack.say "Well..."
    jack.say "Duh..."
    show kat zorder 6 at center, traveling (1.5, 0.5, (740, 1000))
    "Kat pulls me a little distance away from Jack."
    "And then she leans in close to whisper to me."
    show kat sad
    kat.say "Don't take this the wrong way, [hero.name]..."
    kat.say "But is this one of those special grant a wish things?"
    show kat normal
    kat.say "Because if it is, that's totally fine."
    kat.say "It just helps if I know a fan has certain...unique needs in advance, yeah?"
    "I shake my head as I realise what Kat means."
    mike.say "No..."
    mike.say "Oh no, Kat..."
    mike.say "He's just star-struck, that's all."
    mike.say "Look, let's just take a photo and get him a signed photo."
    mike.say "Then I'll get him out of your hair, okay?"
    scene bg gamestore
    show kat smile at center, zoomAt (1.5, (860, 1040))
    show jack smile zorder 5 at center, zoomAt (1.5, (460, 1040))
    with fade
    "Kat nods and we get straight to work."
    with screenshot
    play sound cameraclick
    "I take a shot of the three of us on Jack's phone."
    "Then Kat shoves a polaroid into his hand."
    "And I lead the still stunned Jack out of the place."
    scene bg street
    show jack blush
    with fade
    "Once we're outside in the fresh air, he seems to come round a little."
    jack.say "Did..."
    jack.say "Did we see her?"
    mike.say "Yeah, Jack - we saw her."
    mike.say "We took a photo, she signed a publicity shot."
    mike.say "Hell, she even laughed at your jokes."
    jack.say "Oh..."
    jack.say "That's good news..."
    show jack happy
    jack.say "I knew she couldn't resist the Jack Attack!"
    mike.say "Indeed..."
    mike.say "Now I think we'd best get you home, and pronto!"
    "With one arm supporting Jack, I set off in the direction of his place."
    "And I have to try really hard not to laugh at the show he just made of himself too."
    return

label kat_jack_02:
    show jack at right with easeinright
    "When I see Jack approaching, part of me is still worried that he might he out of it."
    "Because when I saw him last, I was dropping him off at home while he babbled nonsense at me."
    "But another part of me is kind of dreading him coming back to his senses again."
    "And that's because the reason he was in such a state was from the revelation that I know Kat."
    "Yeah, yeah...I know how that sounds."
    show jack at center with ease
    "But Jack's one of those guys that can get super intense about the strangest of things."
    "Like he was so fixated on Kat, in the grips of such a strong crush, that he wouldn't believe me."
    "No matter what I said to him, there was no way he'd ever have been convinced of the truth."
    "It actually took Kat recognising me and saying hi right in front of him."
    "And even then he was literally stunned by the sight of it!"
    "But now he's apparently recovered and had time to process the information."
    "Which means that I'm going to have to deal with the fallout."
    mike.say "Erm..."
    mike.say "Hi, Jack..."
    mike.say "You're looking better than when I last saw you!"
    "I'm trying to make myself seem upbeat and nonchalant."
    show jack angry
    "But I can already see that Jack's face is set in a no-nonsense expression."
    "And he stalks up to me with balled fists, then points a finger into my face."
    show fx anger
    jack.say "That was a pretty shitty thing you did to me back there, mister!"
    jack.say "I thought you were supposed to be my friend?!?"
    hide fx
    "I take step backwards, not appreciating the way Jack's getting in my face."
    mike.say "Whoa, whoa, whoa!"
    mike.say "What are you talking about, man?"
    jack.say "You know very well what I'm talking about."
    jack.say "I'm talking about Kat..."
    jack.say "And how you should have told me you knew her!"
    if jack.flags.heard_about_kat:
        mike.say "Now you're just being crazy, Jack!"
        mike.say "I told you that I knew her, remember?"
        mike.say "You wouldn't believe me!"
        show jack surprised
        show fx drop
        jack.say "Well..."
        jack.say "You might have told me..."
        hide fx
        show jack angry
        jack.say "But you didn't convince me!"
    else:
        mike.say "Oh come off it, Jack!"
        mike.say "You know as well as I do that wouldn't have worked."
        mike.say "You'd have thought I was lying to you."
        mike.say "Or else you wouldn't have heard me at all."
        mike.say "There's no talking to you when you get like that over a girl!"
    "Jack waves a dismissive hand in the air."
    jack.say "Anyway, forget about all that."
    show jack normal
    jack.say "Because I figured out a way you can make it up to me."
    mike.say "Erm..."
    mike.say "I really don't think I have anything to make up for, Jack!"
    "Jack seems to totally ignore my objection."
    "And instead he pushes on with his explanation."
    jack.say "I'm willing to put all of your mistakes behind us."
    show jack perv
    jack.say "That is, if you're willing to introduce me to Kat."
    mike.say "But I already did that."
    mike.say "You even have photographic evidence of it happening!"
    show jack angry
    jack.say "Are you kidding?"
    jack.say "I was in some kind of trance the whole time!"
    show jack sad
    jack.say "Kat must think I'm some kind of blithering idiot."
    "I resist the temptation to point out that's exactly what happened."
    "And I do the best I can to seriously consider Jack's demands."
    menu:
        "Alright... I'll arrange something":
            "It doesn't seem like Jack's going to let this one drop any time soon."
            "So if I want to have any hope of putting an end to it, I don't have a choice."
            mike.say "Urgh..."
            mike.say "Okay, Jack..."
            mike.say "You win."
            show jack smile
            jack.say "You mean it?"
            jack.say "You'll introduce me to Kat?"
            mike.say "That's what I said, isn't it?"
            mike.say "But that's all I'm doing, okay?"
            mike.say "Once I've introduced you, you're on your own."
            mike.say "I'm not going to hang around and hold your hand."
            show jack happy
            "Jack makes a scoffing sound and shakes his head."
            jack.say "I think I can handle myself, [hero.name]!"
            jack.say "You just worry about arranging the meeting."
            show jack perv
            jack.say "I'll handle the rest."
            hide jack with easeoutright
            "I think about reminding Jack of what happened the last time."
            "But all that's going to do is start up another argument."
            "So instead I decide to leave it alone."
            "Jack seems satisfied with the way things have played out."
            "And I suppose that I just have to keep my part of the bargain."
            "Then it's up to Jack."
            "Whether he pulls it off or screws up for a second time."
            "But I already know how I think this is going to go down."
            $ jack.flags.will_meet_kat = True
        "Do not agree to introduce Jack to Kat":
            "For a moment I'm prepared to say yes."
            "But then a thought occurs to me."
            "Why am I even a part of this?"
            "Jack's the one with the crush on Kat."
            "I just happen to be a mutual friend of them both."
            mike.say "You know what, Jack..."
            mike.say "I'm washing my hands of this whole thing."
            show jack surprised at startle
            "Jack's eyes go wide with surprise."
            "And he starts to shake his head."
            jack.say "What?"
            jack.say "N...no!"
            jack.say "You're my friend!"
            jack.say "You have to help me!"
            show jack sad
            mike.say "No, Jack, I don't."
            mike.say "And I think I'm being a better friend this way too."
            mike.say "If you want to try hooking up with Kat, then go ahead."
            mike.say "At least this way you'll succeed or fail off of your own efforts."
            show jack angry
            "Jack keeps on pleading his case a little longer."
            "But I remain unmoved by his arguments."
            show jack sad
            "And eventually he has no choice but to let the matter drop."
            hide jack with easeoutright
            "Sure, I feel kind of guilty for not helping him out."
            "But I think this is the better choice in the long term."
            "Plus it gets me out of this mess for good."
            "Or at least I hope it does."
            $ jack.flags.will_meet_kat = False
    return

label kat_jack_03:
    scene expression f"bg {game.room}"
    show kat at center, zoomAt (1.1, (820, 900))
    with fade
    "I've always had kind of a problem with introducing my old friends to new ones."
    "It's like I'm so into the new person that I really don't want to share them."
    "And I know that sounds really childish and dumb, but it's just how I tend to be."
    "But right now I'm doing the best I can to push all of that aside."
    "Because I promised Jack that I'd talk to Kat on his behalf."
    "To let her know that he's a massive fan and would love to meet her."
    "I'm just hoping that I won't come to regret this!"
    show kat smile
    show kat at center, traveling (1.5, 1.0, (640, 1040))
    mike.say "Kat..."
    mike.say "You seem pretty cool with the whole, having fans thing."
    mike.say "Like you appreciate how much they're into what you do, right?"
    show kat enthusiastic
    "Kat looks up at this, and I see genuine interest in her eyes."
    "But still, she cocks her head on one side and studies me for a moment."
    show kat smile
    "As if she's already wondering what's hiding behind the question."
    show kat smileclosed
    kat.say "You could say that."
    show kat smile
    kat.say "I mean, sometimes it can feel like a bit much."
    kat.say "But they're generally more good than bad."
    show kat normal
    "I nod at this."
    "Trying to look like I just got the answer I wanted."
    "But maybe I'm trying a little too hard."
    "Because Kat starts trying to dig a little deeper."
    show kat shy
    kat.say "That's kind of a weird thing to ask me, [hero.name]…"
    kat.say "Just right out of the blue like that!"
    kat.say "Especially when we already talked about all of that stuff."
    "It was hard enough forcing myself to do this in the first place."
    "So I don't want to add another layer of complications to that."
    "Which means the best option is to just come clean about my motives."
    show kat normal
    mike.say "The thing is, Kat..."
    mike.say "I'm not really asking about that."
    mike.say "Hell, I'm not even asking for me!"
    "Kat listens to what I have to say intently."
    show kat smileclosed
    "And she nods her head for me to go on."
    show kat normal
    mike.say "You see I have this friend called Jack."
    show kat confused
    mike.say "And he's kind of a big fan of yours."
    "Realisation dawns on Kat's face as I say all of this."
    "And now she quickly tunes into the subject."
    show kat surprised at startle
    kat.say "Oh..."
    show fx exclamation
    kat.say "Now I see where this is going!"
    "Then she pauses as something seems to occur to her."
    show kat confused
    kat.say "Wait a second..."
    show kat enthusiastic
    kat.say "Is he a fan of Gamer Girl me?"
    kat.say "Or...is he a fan of Cam Girl me?"
    "Kat's beginning to smile as she asks me the questions."
    "That's because she's warming to the idea of it being the latter."
    "Enjoying the thrill of what she does on camera."
    "As well as the fact it's kind of putting me on the spot."
    mike.say "Which do you think?!?"
    mike.say "I wouldn't be getting this awkward if he just watched you play videogames!"
    show kat smileclosed at startle
    "Kat lets out a pretty sexy giggle and shakes her head."
    show kat smile
    "All of which makes me forget about Jack and his request for a moment."
    kat.say "So..."
    kat.say "What's horny little Jack like?"
    show kat normal
    kat.say "And what does he want from the object of his innermost desires?"
    kat.say "A signed photo?"
    show kat defiant
    kat.say "A shout-out on my next livestream?"
    kat.say "Or is he even more ambitious than that?"
    "I can't help liking it when Kat gets into her online persona like that."
    "I mean, she's pretty damn sexy when she's not playing the part."
    "But somehow the character that she's created for herself adds a new dimension."
    "Like she's consciously trying to concentrate all of her sexiness at once."
    "Urgh..."
    "I almost need to shake myself to focus on Jack."
    "Instead of just thinking about what I want right now!"
    mike.say "Jack?"
    mike.say "He's..."
    mike.say "Well, he's your standard nerd, I guess!"
    mike.say "Likes videogames, comic-books, playing wargames - all that stuff."
    show kat sadsmile
    kat.say "Ah, but he also likes sexy stuff too..."
    show kat confused
    show fx question
    kat.say "Am I right?"
    show kat enthusiastic at startle
    show fx exclamation at startle
    kat.say "Or at least he likes going solo on himself!"
    "I find myself holding up my hands."
    "Waving them in the hope of making Kat calm down."
    show kat smileclosed
    mike.say "Whoa..."
    show kat confused
    mike.say "We're getting a little ahead of ourselves here!"
    show kat normal
    mike.say "I was more thinking we just start with you meeting Jack in the flesh?"
    mike.say "How does that sound?"
    show kat smileclosed at startle
    "Kat lets out another of her super-sexy giggles."
    show kat smile
    "But I note that she also nods her head."
    "Which comes as something of a relief."
    show kat happy
    kat.say "Sure we can, [hero.name]."
    kat.say "You arrange the time and the place."
    kat.say "And I'll meet this Jack of yours."
    show kat smile
    kat.say "But I want you there as my chaperone."
    show kat sadsmile
    kat.say "Just in case he turns out to be a psycho cannibal or something!"
    mike.say "Erm..."
    mike.say "Yeah, Kat..."
    show kat smile
    mike.say "I think you're safe on that score at least."
    mike.say "I've never known Jack to miss a single meal."
    mike.say "But I'm pretty sure he never ate anyone!"
    show kat annoyed
    show fx question
    kat.say "Maybe he just eats people out?"
    show kat happy at startle
    "Kat chuckles at her own joke."
    "But I choose to take that as the matter being settled."
    "So for better or worse, it looks like Jack's going to get what he wants."
    "Though I'll just have to make sure he doesn't get anything that I want for myself!"
    return

label kat_jack_04:
    scene bg coffeeshop with fade
    "I figure that the best place for Kat and Jack to meet is probably the coffeeshop."
    "It's a neutral setting that everyone's familiar with, as we all crave caffeine."
    "And there's bound to be enough people around to keep Jack's behaviour in check."
    "Or else I can always throw a cup of water in his face."
    "Come to think of it, one of those sprays might be more effective."
    "The ones that you see them using to keep excitable dogs in line..."
    "I'm still thinking of the possibilities that would offer when Kat jabs me in the ribs."
    show kat angry zorder 1 at center, zoomAt(1.25, (840, 880)) with easeinright
    with hpunch
    mike.say "Ow!"
    show kat smile
    mike.say "What was that for?!?"
    kat.say "For not answering me the first three times I said your name!"
    show kat normal
    "Suddenly I realise that I must have been miles away, lost in my own thoughts."
    "So I do all that I can to focus my attention solely on what Kat's saying."
    show kat at center, zoomAt(1.25, (340, 880)) with ease
    show kat at center, traveling_easeinZoom(1.5, 0.5, (340, 1040))
    mike.say "Sorry, sorry..."
    mike.say "What's the problem?"
    show kat at stepback(0.1, 20, 0)
    "By way of an answer, Kat points to the door of the coffeeshop."
    show kat smile
    kat.say "I might be wrong, [hero.name]..."
    kat.say "But my gut tells me that's Jack."
    kat.say "That guy right over there."
    show kat normal
    show jack zorder 1 at mostright5 with easeinright
    "It doesn't take me long to see that Kat's right."
    "There's Jack alright, looking around with a big, dumb grin on his face."
    "He kind of reminds me of a kid that's been told he's going to adopt a puppy."
    "And now he's finally made it down to the animal shelter to meet it."
    show kat sadsmile
    kat.say "Shouldn't we wave him over or something?"
    show kat normal
    mike.say "No need, Kat."
    mike.say "Just watch this, okay?"
    "At first, Jack doesn't seem to see us as he wanders into the place."
    "His head turns this way and that, but he actually looks like he's out of it."
    show kat enthusiastic
    show fx question zorder 2 at left
    kat.say "Is he stoned or something?"
    mike.say "Oh no, that's not it."
    mike.say "He's kind of tuning into you right now."
    show kat confused
    kat.say "Tuning into me?"
    show fx question at left
    kat.say "What does that mean?"
    "I shrug and shake my head."
    mike.say "I dunno, Kat..."
    mike.say "I've never really been able to make sense of it myself."
    mike.say "But he can kind of find women without really trying."
    mike.say "Like in a cartoon, where someone smells food, you know?"
    mike.say "And then they kind of float towards it?"
    show kat annoyed
    "Kat gives me a look that says bullshit."
    show kat surprised
    "But then she watches in amazement as Jack almost hovers in our direction."
    show jack at right with ease
    pause 0.5
    show jack at mostright4 with ease
    pause 0.5
    show jack at right5 with ease
    "His eyes look unfocussed and I swear he never looks right at us."
    show jack at right with ease
    show jack at center, zoomAt(1.0, (960, 720)) with ease
    show jack at center, traveling_easeinZoom(1.5, 0.5, (960, 1140))
    "Yet still he manages to plonk himself down in an empty chair on the other side of the table."
    "And as soon as he does so, the trance-like state comes to an abrupt end."
    show kat surprised
    show jack surprised
    show fx exclamation at right
    jack.say "WHOA!"
    show jack happy
    mike.say "Wha..."
    show kat normal
    kat.say "Shit..."
    show jack smile
    jack.say "Hey, you guys!"
    show kat smile
    jack.say "No need to worry about not seeing me and calling me over just now."
    jack.say "I kind of have a knack for finding my way to the prettiest girl in the room!"
    show jack normal
    mike.say "Yeah, Jack..."
    mike.say "I think we just saw that skill in action!"
    mike.say "Anyway..."
    mike.say "Time for a formal introduction."
    mike.say "Jack, this is Kat."
    mike.say "Kat, this is Jack."
    show kat happy
    kat.say "Hi, Jack..."
    show kat smile
    kat.say "I'm so pleased to finally meet you in person."
    kat.say "[hero.name] tells me you're my number one fan!"
    show jack smile
    show kat smileclosed
    "Kat puts on one of her most impishly cute smiles."
    show jack sad blush
    "And then I watch her hit Jack with it."
    "The effect is almost like him being hit by a freight-train."
    "Instantly Jack goes from joking and confident to a quivering wreck."
    "I swear that I see his pupils dilate and sweat begin beading at his temples."
    jack.say "Ur..."
    show jack at backforth(1.0, 20, 0)
    jack.say "I..."
    show jack at backforth(1.0, -20, 0)
    jack.say "That is..."
    show kat at stepback(1.0, 100, 0)
    pause 1
    show jack wink blush at startle
    show kat normal
    "Before I can stop her, Kat reaches out across the table."
    "And she puts her hand atop Jack's, trying to reassure him."
    "As soon as she does so, his nerves seem to abate for a moment."
    "Jack stops stuttering and stumbling, looking her straight in the eye."
    show jack at backforth(1.0, 20, 0)
    jack.say "Oh wow, Kat..."
    show jack at backforth(1.0, -20, 0)
    jack.say "You're even prettier in person than you are on a screen!"
    "Sure, it's a corny line."
    "But Jack's too flustered to be able to fake it."
    "So maybe that's why he manages to almost make Kat blush."
    show jack normal
    show kat defiant
    kat.say "Oh, Jack..."
    kat.say "That's so sweet of you to say!"
    "Though Kat managed to keep control of herself, the same can't be said for Jack."
    "As he's soon blushing like crazy, going bright red and becoming bashful."
    show jack at backforth(1.0, 20, 0)
    jack.say "I..."
    show jack at backforth(1.0, -20, 0)
    jack.say "Oh man..."
    show jack happy
    show kat smile
    jack.say "I still can't believe this is actually happening."
    jack.say "I mean, pinch me, man - make sure I'm not dreaming!"
    "I have no idea if Jack's being serious or not."
    "But this seems like too much of an opportunity to indulge myself."
    "So I lean over the table and pinch Jack as hard as I can on the arm."
    show jack surprised -blush at startle
    show fx exclamation at right
    show kat happy
    jack.say "OUCH!"
    show jack angry
    jack.say "Hey..."
    jack.say "What the hell, man?!?"
    "I shrug as I sit back down."
    show jack sad
    mike.say "You were the one that asked to be pinched!"
    mike.say "And we're all still here, aren't we?"
    mike.say "Plus, don't be such a big baby!"
    "I catch Kat's eye as I sit back down, and I give her a slight roll of my own."
    show kat defiant
    "She nods, too subtly for anyone else to see it, letting me know she's on the same page."
    "That I want Jack to meet her."
    "But not to get in the way of what we have going on together."
    "Jack seems oblivious to all of this though."
    "He's still rubbing his arm and shooting me evil looks."
    "And when he starts talking again, he leans towards Kat."
    "Like he's subtly trying to ease the conversation away from me."
    show kat normal
    show jack normal
    jack.say "So, Kat..."
    jack.say "How did you and [hero.name] meet?"
    jack.say "It's not like he watches your livestreams."
    jack.say "So what's the story on you becoming friends?"
    show kat defiant
    "Kat shoots me another sideways glance."
    "And I can tell that she's asking me what her answer should be."
    menu:
        "I already told Jack!" if jack.flags.heard_about_kat:
            "I shrug my shoulders."
            "Because I already told Jack almost everything else about us."
            mike.say "Jack wants to be filled in on the backstory, Kat."
            mike.say "So you can skip all the gory details of us getting together!"
            "Kat seems more than a little relieved by this."
            show kat happy
            kat.say "Well, Jack..."
            kat.say "You know I'm a professional gamer too?"
            show kat normal
            show jack surprised
            "Jack looks amazed by this information."
            "His eyes popping open as he takes it in."
            show jack at startle
            show fx exclamation at right
            jack.say "You are?!?"
            jack.say "Oh boy, oh boy, oh boy..."
            show fx exclamation at right
            jack.say "You just get cooler all the time, Kat!"
            show jack smile
            show kat smile at startle
            "Kat chuckles at Jack's enthusiasm."
            "But she presses on with her story all the same."
            show kat happy
            kat.say "[hero.name] was one of my opponents in a tournament."
            show kat smile
            kat.say "And we became friends afterwards."
            kat.say "Then one thing lead to another, and here we are!"
            show kat normal
            "Jack looks more amazed than ever as he looks from Kat to me and back again."
            "He kind of slumps back in his seat, like he's blown away by the tale."
            show jack wink
            jack.say "Oh man..."
            jack.say "One thing never leads to another for me."
            show jack happy
            show fx exclamation at right
            jack.say "It usually leads straight to a slap across the face!"
        "Lets Kat tell Jack" if not jack.flags.heard_about_kat:
            "I shrug my shoulders, and give Kat a nod."
            "Because we have nothing to hide."
            "Plus I don't want Jack getting any ideas the idea that she's single."
            show kat timid
            "Kat seems to pick up on my meaning, as she let's go of Jack's hand."
            "Instead she clasps mine, squeezing it as she looks me in the eye."
            "And the gesture isn't lost on Jack either."
            show jack surprised at startle
            jack.say "Are you two..."
            jack.say "Oh boy, oh boy, oh boy..."
            show fx exclamation at right
            jack.say "This keeps getting crazier all the time, Kat!"
            show jack smile at startle
            "Kat chuckles at Jack's enthusiasm."
            show kat happy
            show fx question at left
            kat.say "You know I'm a professional gamer too?"
            kat.say "Well, [hero.name] was one of my opponents in a tournament."
            kat.say "And we became friends afterwards."
            kat.say "Then one thing lead to another, and here we are!"
            show kat smile
            "Jack looks more amazed than ever as he looks from Kat to me and back again."
            "He kind of slumps back in his seat, like he's blown away by the tale."
            show jack wink
            jack.say "Oh man..."
            jack.say "One thing never leads to another for me."
            show jack happy
            show fx exclamation at right
            jack.say "It usually leads straight to a slap across the face!"
        "Do not let Kat tell Jack" if not jack.flags.heard_about_kat:
            "I shake my head, letting Kat know my feelings on the matter."
            "It's not that I feel like we've got anything to hide."
            "More that I know how immature Jack can be when there are intense feelings involved."
            "If he finds out that we're an item like this, he could come to resent me for it."
            "He's told me that he's got the hots for Kat himself, so he could get bitter."
            "Maybe get it into his head that I deliberately wanted to rub his face in it."
            "Kat seems to pick up on my meaning, as she keeps her tone light and conversational."
            show kat smile
            kat.say "Well, Jack..."
            kat.say "You know I'm a professional gamer too?"
            show kat normal
            "Jack looks amazed by this information."
            "His eyes popping open as he takes it in."
            show jack surprised at startle
            show fx exclamation at right
            jack.say "You are?!?"
            jack.say "Oh boy, oh boy, oh boy..."
            jack.say "You just get cooler all the time, Kat!"
            show kat happy at startle
            "Kat chuckles at Jack's enthusiasm."
            "But she presses on with her story all the same."
            show kat smile
            kat.say "[hero.name] was one of my opponents in a tournament."
            kat.say "And we became friends afterwards."
            kat.say "That's just about all there is to it."
            show kat normal
            "Jack nods his head at this."
            "Perhaps a little too eagerly for my liking."
            "So I resolve to keep a closer eye on him from now on."
            "Just in case I pick up any hints that he's trying to make a move on Kat."
    show jack smile
    "After that the conversation goes to all of the places you'd expect it to."
    "Kat and Jack compare notes on their respective geekdoms."
    "And we drink far more expensive coffee than we probably should."
    "But much to my surprise, it's Jack that calls an end to the meet-up."
    show jack wink blush
    jack.say "Okay, guys..."
    jack.say "I've had so much coffee I can see through time!"
    mike.say "Okay, Jack..."
    mike.say "We can wrap it up there."
    show kat happy
    show jack smile
    kat.say "Yeah, Jack..."
    kat.say "It was really nice to meet you."
    show jack at center, traveling_easeoutZoom(1.0, 0.5, (960, 720))
    show kat normal
    "Jack's nodding at all of this as he gets up."
    show jack happy
    jack.say "Sure, sure..."
    jack.say "Maybe we can do it again?"
    jack.say "Some time soon?"
    hide jack with easeoutright
    "We all nod and wave as he hurries out of the coffeeshop."
    "And once he's gone, Kat turns to me, a puzzled expression on her face."
    show kat annoyed
    show fx question
    kat.say "I don't get it."
    kat.say "He's keen to meet me, and he seems to like me when he does."
    show kat sadsmile
    kat.say "But then he has to scuttle off without warning like that."
    show kat sad
    "I keep watching as Jack retreats into the distance."
    "And at first, I'm as flummoxed as Kat."
    "But then a thought occurs to me."
    mike.say "I think I know the reason."
    mike.say "But you might not like it!"
    show kat angry
    show fx exclamation at left
    kat.say "Don't be so presumptuous!"
    kat.say "Just tell me already."
    show kat normal
    mike.say "Well, it's pretty obvious that Jack has the hots for you."
    mike.say "But his memory's no better than any guy in the street."
    mike.say "So he'll need to get to somewhere private before he forgets your face!"
    show kat shocked
    "Kat's face goes from puzzled to horrified in a matter of seconds."
    show fx question at left
    kat.say "You mean he's going to?"
    mike.say "Yup."
    show kat surprised
    kat.say "With his cock out?"
    mike.say "Oh yeah."
    show kat shocked at startle
    show fx question at left
    show fx exclamation as fx2 zorder 2 at left
    kat.say "He could be doing it as we speak?!?"
    mike.say "I'd be amazed if his pants aren't around his ankles right now!"
    show kat happy at startle
    "Kat shakes her head and then begins to laugh."
    show kat smile
    show fx exclamation at left
    kat.say "What a dirty boy!"
    mike.say "Oh, you have no idea!"
    return

label kat_jack_05:
    scene expression f"bg {game.room}"
    with fade
    show jack at center, zoomAt (1.25, (640, 940)) with easeinright
    "Jack and I have met up on the premise that we haven't seen to much of each other lately."
    "You know, just that we're old buddies that really should find more time to just hang-out?"
    "But the problem is that I'm starting to think Jack has an ulterior motive here."
    "Because no matter what I try to talk about, he always tries to change the subject."
    "Which on it's own wouldn't be a total pain in the ass."
    "But he keeps on going back to the same thing every time."
    "And it's all starting to wear pretty thin!"
    mike.say "Did you see the latest Orks from Wargames Factory yet?"
    mike.say "They're so good I might consider getting back into Spacemallet!"
    show jack sad
    jack.say "Nah..."
    jack.say "I'll never forgive them for nerfing my Space Elves!"
    show jack normal
    jack.say "But you know what..."
    show fx question zorder 2
    jack.say "I wonder if Kat ever played Spacemallet?"
    "That's it."
    "That's the limit, right there!"
    "Without warning, I round on Jack."
    "And I poke a finger into his rather soft chest."
    mike.say "Will you stop?"
    mike.say "Will you?!?"
    show jack surprised at stepback
    "Jack leaps backwards, shock and surprise on his face."
    "And I can see that he's already clutching at his chest where I prodded him."
    show jack angry
    jack.say "Whoa..."
    show fx question at center
    show fx exclamation as fx2 zorder 2 at center
    jack.say "What the hell, man?!?"
    jack.say "What did I do to deserve that?"
    mike.say "Like you don't know!"
    show jack sad
    mike.say "Whatever I say, it's the same."
    mike.say "No matter what it is, you bring it back to Kat."
    mike.say "Whether you think she ate it, rode it or played it."
    mike.say "It doesn't matter what it is, it's always the same!"
    "Jack flinches for a second time when I hurl the accusations at him."
    "And I can see that's mainly because he now knows the game is up."
    show jack normal
    jack.say "Okay, okay..."
    jack.say "You got me, [hero.name]…"
    show fx question at center
    jack.say "Just don't hurt me anymore, okay?"
    "I let out a sigh, seriously considering giving Jack another vicious poke."
    "But then I relent, stepping back and holding up my hands in a gesture of surrender."
    mike.say "Agreed."
    show jack surprised
    mike.say "But only on the condition you spill your guts!"
    "Jack looks puzzled by this last demand."
    show jack angry
    jack.say "What are you talking about, man?"
    jack.say "I confessed that I'm obsessed with your girlfriend already."
    show jack sad
    jack.say "Isn't that enough?"
    mike.say "I know you better than that, Jack."
    mike.say "You're always getting obsessed with girls."
    mike.say "But you at least try to hide it when I'm the one dating them."
    mike.say "This is different though, because you won't shut up about her."
    "For a moment I think Jack's going to deny it."
    "That he's going to try to weasel his way out of it."
    show jack normal
    "But then he seems to sag, and he nods his head in defeat."
    jack.say "You got me, man, you got me."
    jack.say "I tried really hard."
    jack.say "But I just can't get Kat out of my head!"
    jack.say "No matter how hard I try, it's no good."
    show jack happy
    jack.say "Plus my right hand is starting to ache all the time."
    show fx exclamation at center
    jack.say "And I actually think my eyesight's getting worse!"
    show jack normal
    mike.say "Alright, that's enough sharing!"
    mike.say "I get the picture."
    "Jack looks like I punched him in the gut, rather than poked him in the chest."
    jack.say "Look, man..."
    jack.say "You gotta help me out here."
    jack.say "I'm an addict and you're dealing the drug I need!"
    mike.say "Jack..."
    mike.say "I'm dating Kat, not pimping her out!"
    show jack sad
    "Jack shakes his head, looking almost pained as he does so."
    jack.say "I know, I know..."
    jack.say "That's why I'm not asking you to let me sleep with her alone."
    mike.say "You're not?"
    show jack happy
    jack.say "No, I figured we could have a threesome, yeah?"
    jack.say "You, me and Kat."
    show jack normal
    menu:
        "Agree to the idea of a threesome":
            "I'm about to tell Jack that he can fuck right off."
            "But that's just my instinctive reaction to the idea."
            "And I manage to stop myself just in time."
            "Because a new thought just popped into my head."
            "Why the hell not?"
            "A threesome would kill two birds with one stone."
            "It'd take care of Jack's desperate lusts."
            "And it'd let me keep a close eye on him at the same time."
            mike.say "Okay, Jack..."
            mike.say "I'll talk to Kat, see what she says."
            show jack sad
            "Jack lets out a long sigh."
            "And then he shrugs his shoulders."
            jack.say "Okay, man..."
            jack.say "It was worth a try."
            jack.say "I guess you're just not as liberated as I thought!"
            mike.say "Erm..."
            mike.say "Jack..."
            mike.say "I just said yes!"
            show jack normal
            "Jack stares at me blankly for a moment."
            "Then he shakes his head, as if trying to restart his brain."
            show jack surprised blush at startle
            show fx question at center
            show fx exclamation as fx2 at center
            jack.say "You...you did?!?"
            show jack happy at startle
            jack.say "Well that's great!"
            show jack happy at startle
            jack.say "That's just great!"
            mike.say "Hold on, Jack..."
            mike.say "I said I'd talk to Kat, that's all."
            mike.say "She gets the casting vote."
            show jack smile
            jack.say "Okay, okay..."
            show jack -blush
            jack.say "Of course she does."
            jack.say "Just let me know as soon as she does, yeah?"
            show jack normal
            "I nod, now wanting to let the matter drop."
            "But I soon realise how awkward we've managed to make things."
            "And there's nothing to do but put on my big-boy pants and tough it out."
            $ jack.flags.ready_kat_jack_threesome = True
            return
        "Do not agree to the idea of a threesome":
            "It doesn't take more than a split-second for me to respond."
            "And once I do, I'm back to blistering Jack again."
            mike.say "Are you out of your tiny little mind?"
            mike.say "So you're obsessed with Kat, so what?"
            mike.say "I'm not going to let you fuck her for the sake of your mental health!"
            show jack sad
            "Jack's instantly back on the defensive."
            "Shaking his head and trying to deflect my anger."
            jack.say "I hear you, man..."
            show fx question at center
            jack.say "It...it just sounded so reasonable in my head, you know?"
            mike.say "No, Jack..."
            mike.say "I don't know."
            mike.say "And I don't want to."
            mike.say "In fact, I never want to hear you mention this again!"
            mike.say "You got that?"
            "Sure, I feel kind of bad blistering Jack like this."
            "But I know him too well to just leave it to chance."
            "He's too obsessive to be able to let it go."
            "So it's better to nip the thing in the bud, here and now."
            show jack wink
            jack.say "I've got it..."
            jack.say "No more sexy thoughts about Kat!"
            jack.say "No more!"
            show jack normal
            "I nod, now willing to let the matter drop."
            "But I soon realise how awkward I've managed to make things."
            "And there's nothing to do but put on my big-boy pants and tough it out."
            $ jack.flags.ready_kat_jack_threesome = False
            return

label kat_jack_06:
    scene bg arcade with fade
    show kat at center, zoomAt(1.0, (640, 720)) with dissolve
    "There's no way that I'm going to beat around the bush with Kat like Jack did to me."
    "No, I'm just going to walk right up to her and ask the question without any bullshit."
    "Then she can say yes or no, and that'll be the matter settled."
    mike.say "Kat..."
    mike.say "There's something I need to ask you."
    show kat enthusiastic at center, traveling(1.25, 0.5, (640, 880))
    "As soon as the words are out of my mouth, I see the first flaw in my supposedly fool-proof plan."
    "Of course Kat's eyes light up at the mere mention of me needing to ask her something."
    "It hardly matters whether the thing in question turns out to be good or bad in nature."
    "The fact that a guy feels the need to announce it at all means it has to be important."
    show kat smile
    kat.say "Oh do you now?"
    kat.say "Well this I have to hear!"
    show kat normal
    "I'm still doing the best I can to ignore all of the distractions as I begin to explain myself."
    "But I can already feel myself sinking down into the hole that I've gone and dug."
    mike.say "Well..."
    mike.say "You remember, Jack?"
    "Kat nods at this."
    show kat smile
    kat.say "Your friend from the coffeeshop?"
    show fx question at center
    kat.say "Pudgy and geeky in equal measures?"
    kat.say "Of course I remember him."
    show kat b normal
    "I'm about to speak when Kat holds up a finger to stop me."
    kat.say "What happened to him?"
    show kat defiant
    kat.say "No...let me guess..."
    show kat happy at startle
    kat.say "He finally lost his virginity?"
    mike.say "Very funny, Kat!"
    show kat smile
    "I shake my head and make a slight change to my tone."
    "All in an effort to restart the conversation in a more serious manner."
    mike.say "But no, I'm pretty sure that's already happened."
    mike.say "What I meant to say was that I saw him the other day."
    mike.say "And he asked me to ask you something."
    mike.say "To kind of pass on an idea he had."
    show kat enthusiastic
    "Kat raises an eyebrow at this."
    "And I can see that I've finally got her full attention."
    kat.say "Now whatever could that be?"
    kat.say "Let me think..."
    show kat defiant
    kat.say "He's a truly tremendous nerd."
    kat.say "And he has a slight weight issue too."
    kat.say "Not to forget that he's a fan of my livestreams."
    kat.say "Now this might sound like a shot in the dark..."
    kat.say "But I'm going to guess that it involves sex?"
    show kat happy
    kat.say "Or at the very least, a chance to sniff where I've been sitting?"
    "I want to keep things serious, but I'm not made of stone."
    "And I can't help cracking up as Kat sums Jack up so well."
    show kat smile
    mike.say "Very funny, Kat..."
    mike.say "And not far off the mark either."
    mike.say "Jack was wondering if we'd be interested in a sexual encounter."
    mike.say "Specifically one involving him."
    show kat normal at backforth(0.3, 5, 0)
    "Kat shakes her head at first, not exactly impressed."
    kat.say "Oh no..."
    kat.say "I may stream kinky shit..."
    show kat offended at startle
    kat.say "But that doesn't mean I fuck random fans!"
    show kat angry
    mike.say "Ah, but you seem to have missed one thing."
    mike.say "He said a sexual encounter with us."
    mike.say "Not just you."
    show kat normal
    "Kat sits up as soon as she hears this."
    "Like that one fact changes everything."
    if kat.sub >= 60:
        show kat smile
        kat.say "Wait..."
        kat.say "You mean like a threesome?"
        kat.say "You, me and him?"
        "I nod at this."
        mike.say "Well, that's how I understand a threesome works, Kat!"
        mike.say "You sound like that perked your interest, yeah?"
        "Kat doesn't go as far as giving me a nod."
        "But she kind of shrugs in a way that tells me I'm right."
        show kat sadsmile
        kat.say "Sure it does, [hero.name]."
        show kat smileclosed
        kat.say "Don't get me wrong, I think your friend Jack is kind of cute."
        kat.say "In a nerdy, desperate sort of way, you know?"
        show kat smile
        kat.say "But I still wouldn't want to do it with him."
        mike.say "Unless I'm in on it too?"
        show kat shy
        "Kat looks a little bashful as I ask the question."
        "But it doesn't stop her from answering me."
        show kat happy at startle
        kat.say "Of course it does!"
        show kat smile
        kat.say "It's like we're having fun with a friend."
        show kat shy
        show kat blush with dissolve
        kat.say "Only it's...sexy fun!"
        "I'm doing the best I can to keep from laughing."
        "Because Kat just looks so cute when she comes over all bashful like this."
        show kat smile
        show kat -blush with dissolve
        mike.say "So..."
        mike.say "I'll go back and tell Jack it's a yes."
        mike.say "Then I can get our diaries lined up."
        "Kat nods, and I take that as a cue to drop the subject."
        "Now all I have to do is actually organise the threesome."
        "That and make sure nothing goes drastically wrong."
        $ Harem.join_by_name("exclusive_fan", "jack", "kat")
        $ kat.flags.agree_kat_jack_threesome = True
        $ kat.love += 1
        $ kat.sub += 1
        return
    else:
        show kat smile
        kat.say "Okay, [hero.name]..."
        kat.say "I was joking around just then."
        show kat defiant
        kat.say "But now I'm being totally serious."
        "The tone of Kat's voice could have told me that much without her saying so."
        "In fact it's so serious and commanding that I find myself nodding obediently."
        show kat smile
        kat.say "You go back to your friend..."
        show kat offended
        kat.say "And you tell him that he can go fuck himself."
        kat.say "Because there's no way in hell that he's fucking me!"
        show kat angry
        "Maybe that's a bit stronger than what I'd been expecting."
        "But there's still no mistaking the answer for anything but a negative."
        mike.say "Okay, Kat..."
        mike.say "I hear you, loud and clear."
        mike.say "But I might kind of soften the language a little."
        mike.say "Because Jack's a sensitive guy, you know?"
        show kat annoyed
        "Kat curls her lip at this."
        "Like she disapproves of my intent."
        show kat angry
        kat.say "Well, you know him better than I do."
        kat.say "But just be sure that he gets the message, yeah?"
        show kat sadsmile
        kat.say "I've met a hundred guys like Jack before."
        kat.say "And if you want them to get the message, you've got to stick it in and break it off!"
        $ kat.flags.agree_kat_jack_threesome = False
        $ kat.love -= 1
        $ kat.sub -= 1
        return

label kat_jack_07:
    mike.say "Hey Kat, how are you?"
    kat.say "Fine [hero.name]. Why are you calling for?"
    mike.say "You remember the talk we had about Jack, me and you?"
    mike.say "Well, I'm free right now so if want to come by to make it happen..."
    kat.say "I was in the middle of something but I can free myself easily."
    kat.say "Jack is free too?"
    mike.say "I don't know, but I'm sure he'll come at light speed at the moment he know you are coming."
    kat.say "Alright, then I'll be there in an hour."
    $ game.hour += 1
    scene bg livingroom with fade
    "After all of the planning and negotiating, the big day is finally here."
    "The threesome with Jack and Kat's been arranged an agreed."
    "So now I'm just waiting for the moment when both of them arrive on my doorstep."
    "But yeah, I'm making it all sound way more simple and stress-free than it actually is!"
    "I've had to make sure that [bree.name] and Sasha are out of the house."
    "Not just that, but also that they won't be back in time to walk in on us."
    "Which obviously made the pair of them more than a little curious as to what I have planned."
    "So that meant I had to offer them some bribes and incentives to get them to leave."
    "Then there was the small matter of making sure the house was clean enough."
    "Because my housemates are filth wizards, friends to only the pig and the rat!"
    "And even now that I've got everything sorted, I'm pacing up and down as I wait."
    "I must have practiced what I'm going to say when they turn up a hundred times."
    "Trying to strike just the right balance when I open the door."
    "On the one hand I want to seem like I'm cool with all of this."
    "But at the same time I feel like I should be able to laugh about it too."
    play sound door_bell
    "Yet when the doorbell finally rings, all I feel like I do is panic."
    "That and run into the hallway in a state of total disarray."
    "I don't even pause long enough to get my head in order."
    scene bg black with dissolve
    pause 0.1
    scene bg house
    with wiperight
    "Instead I open the door, telling myself it'll just be one of them."
    "And whether it's Jack or Kat, I can recover while we wait for the other one."
    "So I stand there, putting a smile on my face."
    "Only to be greeted by the both of them standing on the porch."
    show jack casual smile at center, zoomAt(1.25, (340, 920))
    show kat casual normal at center, zoomAt(1.25, (940, 880))
    with dissolve
    jack.say "Hey, buddy!"
    show jack normal
    show kat happy
    kat.say "Hi there, [hero.name]!"
    show kat normal
    "I glance at the time and then back at Jack and Kat."
    mike.say "Wow..."
    mike.say "You're both right on time."
    mike.say "Who'd have thought that'd happen!"
    "Jack and Kat don't seem to pick up on my discomfort in the slightest."
    scene bg livingroom with fade
    show jack casual normal at center, zoomAt(1.25, (340, 920))
    show kat casual normal at center, zoomAt(1.25, (940, 880))
    with easeinright
    "Instead they're all shrugs and smiles as they push their way into the house."
    show jack smile
    jack.say "Weird, right?"
    jack.say "I'm normally running late."
    jack.say "But not today!"
    show jack normal
    show kat talkative
    kat.say "Me too."
    kat.say "And luckily we bumped into each other just down the street."
    kat.say "Because one of us turning up on our own would have been pretty awkward!"
    show kat normal
    "All I can do is nod in agreement, that and keep on smiling."
    "In an attempt to shake off my nerves, I lead them to the back of the house."
    scene bg pool with fade
    show jack casual normal at center, zoomAt(1.25, (340, 920))
    show kat casual normal at center, zoomAt(1.25, (940, 880))
    with easeinleft
    "And once we're out by the pool, I wave my hand about in a vague gesture."
    mike.say "Erm..."
    mike.say "You guys want to go it out here?"
    mike.say "I've got to admit that I'm a little rusty on threesomes!"
    mike.say "So I don't know if there's any etiquette to observe?"
    "As soon as I admit my ignorance, I see relief on Jack and Kat's faces."
    "Like they were trying to act cool until I came clean as well."
    show jack smile
    jack.say "Me neither!"
    jack.say "How about you, Kat?"
    show jack normal
    show kat talkative
    kat.say "I know a little bit, I guess?"
    kat.say "I mean, I've watched a couple of videos!"
    show kat normal
    "Jack and I are nodding eagerly as Kat makes the admission."
    "Almost like she's going to describe how to do this thing."
    "To break it down into simple, easy steps for us."
    "But then she shakes her head."
    show kat talkative
    kat.say "I suppose the first thing would be for us all to get naked?"
    show kat normal
    show jack smile
    jack.say "You only had to say the word!"
    show jack normal swimsuit at hshake
    "Jack underlines his enthusiasm by pulling off his shirt."
    "Then he tosses it aside, already starting to undo his pants."
    show kat stuned
    "Kat shoots me a surprised look, that I'm probably mirroring myself."
    show kat happy at startle
    "But then she bursts into spontaneous laughter."
    "And I can't help but join in."
    show kat underwear with dissolve
    "The next thing I know, she's stripping-off too."
    "So I have no choice but to join in for fear of being left behind!"
    show jack naked with fade
    "Somehow Jack and I manage to get naked before Kat."
    "She's still in her underwear when I come up on her right side."
    "Jack takes the left, already reaching up to unhook her bra."
    "But my hand goes in the opposite direction, sliding over her belly."
    "And I try to combine taking off her panties with exploring inside of them."
    "All the time I'm looking up at Kat, watching the expression on her face."
    "Though it looks like the sensations she's feeling are leaving it blank."
    "I can see that she's also nodding her head the whole time."
    "Which tells me that she's loving every moment of what we're doing."
    scene bg black
    show katjack foreplay pool open
    with fade
    "Soon enough the last of Kat's clothes are off, and she's totally naked."
    "Now I'm eager to see where this thing is going next."
    show katjack foreplay closed
    "And I get the feeling that Kat and Jack are both waiting for someone else to take the lead."
    "So with that in mind, I sit back and motion for Jack to do the same thing."
    show katjack foreplay open pleasure
    "This means that Kat's suddenly presented with the view of not one, but two cocks."
    "Needless to say that Jack and I are more than a little excited by now."
    "Which means that they're both standing to attention, right in front of Kat."
    "I watch as her eyes go wide at the sight, and then I see her give a little nod."
    "Without the need for anyone to say a word, Kat kneels down in front of us."
    show katjack bj pool with fade
    "And then she starts to lean in closer, already beginning to open her mouth."
    "Kat makes eye contact with me just before she starts."
    show katjack bj righthand_forth lefthand_forth
    pause 0.2
    show katjack bj righthand_back lefthand_back at stepback(speed=0.05, h=10, v=0)
    "Like she's asking me where she should focus her attentions."
    "I can see that Jack's not noticed either."
    "So I could tell her to go for one of us or the other."
    menu:
        "Make her suck you":
            $ kat.flags.mike_pleased += 1
            "It's selfish of me, I know."
            "But I don't hesitate to nod towards my own cock."
            "Kat doesn't need any more encouragement than that."
            "Because her head goes down a moment later."
            show katjack bj suckmike
            "And then I feel her lips wrapping around the head of my cock."
            "Kat uses every tool at her disposal as she goes to work on me."
            "Lips, tongue and teeth all come into play during the blow-job."
            "But I have no idea what Jack's doing the whole time it's going on."
            "And that's because I end up closing my eyes and surrendering to the experience."
            show katjack bj righthand_forth
            pause 0.2
            show katjack bj righthand_back at stepback(speed=0.05, h=10, v=0)
            "I'm vaguely aware of Kat's head bobbing up and down."
            "But beyond that, I'm lost in a world of pure sensation and pleasure."
            show katjack bj righthand_forth
            pause 0.2
            show katjack bj righthand_back at stepback(speed=0.05, h=10, v=0)
            "More than once I'm sure that she must have taken me deep into her throat."
            "And I keep on expecting myself to cum at any moment."
            show katjack bj righthand_forth
            pause 0.2
            show katjack bj righthand_back at stepback(speed=0.05, h=10, v=0)
            "That's why I'm surprised when I feel it coming so far ahead of time."
            "In fact I have all the time I need to decide how I want this to end."
            show katjack bj righthand_forth
            pause 0.2
            show katjack bj righthand_back at stepback(speed=0.05, h=10, v=0)
            "Even more so when I open my eyes and see that Kat's looking up at me."
            "Which can only mean she's on the same page as me right now."
            menu:
                "Indicate her to take it in her mouth":
                    "I quickly point downwards, hoping Kat gets my meaning."
                    "And luckily for me she seems to understand."
                    "Kat closes her eyes again and redoubles her efforts."
                    show katjack bj suckmike mikecum with hpunch
                    "The effect of which being that I soon feel myself losing it."
                    with hpunch
                    "Already prepared, Kat has no problem swallowing everything straight down."
                    with hpunch
                    "She rides it out to the very end, gulping the last drops without incident."
                "Indicate her to take it on her face":
                    "I quickly point upwards, hoping Kat gets my meaning."
                    "And luckily for me she seems to understand."
                    show katjack bj -suckmike mikecum
                    "Kat opens her mouth and leans backwards, releasing my cock."
                    "Then she waits patiently as it bobs in front of her face."
                    show katjack bj mikecum with hpunch
                    "Within moments I feel myself losing it, letting go."
                    show katjack bj -mikecum facecum with hpunch
                    "And Kat takes all of it, straight in the face."
                    "Smiling the whole time her face is spattered with cum."
        "Make her suck Jack":
            $ kat.flags.jack_pleased += 1
            "I could be a selfish jerk here, but I just don't have the heart."
            "So I make sure to nod towards Jack's cock instead of mine."
            "Kat doesn't need any more encouragement than that."
            "Because her head goes down a moment later."
            show katjack bj suckjack pool
            "And then I see her lips wrapping around the head of Jack's cock."
            "Kat uses every tool at her disposal as she goes to work on him."
            "Lips, tongue and teeth all come into play during the blow-job."
            "I have no idea what Jack's feeling, but it must be incredible."
            "And it looks so good that I can't tear my eyes away."
            show katjack bj lefthand_forth
            pause 0.2
            show katjack bj lefthand_back at stepback(speed=0.05, h=-10, v=0)
            "I'm vaguely aware of Kat's head bobbing up and down."
            "But beyond that, I'm lost in the act of watching her pleasure Jack."
            show katjack bj lefthand_forth
            pause 0.2
            show katjack bj lefthand_back at stepback(speed=0.05, h=-10, v=0)
            "More than once I'm sure that she must have taken him deep into her throat."
            "And I keep on expecting him to cum at any moment."
            show katjack bj lefthand_forth
            pause 0.2
            show katjack bj lefthand_back at stepback(speed=0.05, h=-10, v=0)
            "But then I'm surprised to see that Kat's looking up at me."
            "Which can only mean she's waiting for me to tell her something."
            "Like she wants me to say how this should end!"
            menu:
                "Indicate her to take it in her mouth":
                    "I quickly point downwards, hoping Kat gets my meaning."
                    "And luckily for me she seems to understand."
                    "Kat closes her eyes again and redoubles her efforts."
                    show katjack bj suckjack jackcum with hpunch
                    "The effect of which being that Jack starts losing it."
                    with hpunch
                    "Already prepared, Kat has no problem swallowing everything straight down."
                    with hpunch
                    "She rides it out to the very end, gulping the last drops without incident."
                "Indicate her to take it on her face":
                    "I quickly point upwards, hoping Kat gets my meaning."
                    "And luckily for me she seems to understand."
                    show katjack bj -suckjack jackcum
                    "Kat opens her mouth and leans backwards, releasing Jack's cock."
                    "Then she waits patiently as it bobs in front of her face."
                    show katjack bj jackcum with hpunch
                    "Within moments I see Jack losing it, letting go."
                    show katjack bj -jackcum facecum with hpunch
                    "And Kat takes all of it, straight in the face."
                    "Smiling the whole time her face is spattered with cum."
        "Let her decide which one to blow":
            $ kat.flags.mike_pleased += 0.5
            $ kat.flags.jack_pleased += 0.5
            "I make sure to nod at my own cock and then at Jack's, hoping Kat gets my drift."
            "And I'm rewarded with a nod in return as her head goes down a moment later."
            show katjack bj suckjack pool
            "And then I see her lips wrapping around the head of Jack's cock."
            "Kat uses every tool at her disposal as she goes to work on him."
            "Lips, tongue and teeth all come into play during the blow-job."
            show katjack bj lefthand_forth
            pause 0.2
            show katjack bj lefthand_back at stepback(speed=0.05, h=10, v=0)
            "I have no idea what Jack's feeling, but it must be incredible."
            "And it looks so good that I can't tear my eyes away."
            "I'm vaguely aware of Kat's head bobbing up and down."
            show katjack bj lefthand_forth
            pause 0.2
            show katjack bj lefthand_back at stepback(speed=0.05, h=10, v=0)
            "But beyond that, I'm lost in the act of watching her pleasure Jack."
            "More than once I'm sure that she must have taken him deep into her throat."
            show katjack bj lefthand_forth
            pause 0.2
            show katjack bj lefthand_back at stepback(speed=0.05, h=10, v=0)
            "And I keep on expecting him to cum at any moment."
            "But then I'm surprised to see that Kat's looking up at me."
            "A moment later she raises her head, letting Jack's cock slide out of her mouth."
            show katjack bj suckmike pool
            "And just like that she switches over, giving the same treatment to me."
            "I feel my eyes closing as all of the sensations I imagined become real."
            show katjack bj righthand_forth
            pause 0.2
            show katjack bj righthand_back at stepback(speed=0.05, h=-10, v=0)
            "Kat gives me every bit as much care and attention as she gave to Jack."
            "And I can only assume that he must be watching in the same way that I did."
            "I keep on expecting myself to cum at any moment."
            show katjack bj righthand_forth
            pause 0.2
            show katjack bj righthand_back at stepback(speed=0.05, h=-10, v=0)
            "That's why I'm surprised when I feel it coming so far ahead of time."
            "When my eyes open, I can see that Kat's in complete control."
            show katjack bj righthand_forth
            pause 0.2
            show katjack bj righthand_back at stepback(speed=0.05, h=-10, v=0)
            "Not only has she been working me with her mouth, but she kept Jack stiff with her hand too."
            "And now it looks like the both of us are about to blow!"
            show katjack bj normal
            "Kat opens her mouth and leans backwards, releasing my cock."
            "She does the same with Jack's too."
            "Then she waits patiently as they bob in front of her face."
            show katjack bj jackcum mikecum mikecum with hpunch
            "Within moments I feel myself losing it, letting go and so does Jack."
            show katjack bj -jackcum -mikecum facecum with hpunch
            "And Kat takes all of it, straight in the face."
            "Smiling the whole time her face is spattered with cum."
    menu:
        "Fuck Kat":
            $ kat.flags.mike_pleased += 1
            "Jack flops back onto one of the sun-loungers by the side of the pool."
            "He looks totally exhausted already, like he needs to take a moment to rest."
            "But it doesn't look like Kat's going to let him get away with it."
            scene bg black
            show katjack mikefuck pool
            with fade

            "She bends over the other end of the lounger."
            show katjack mikefuck surprised
            kat.say "What are you doing, Jack?"
            kat.say "You can't be worn out already?!?"
            show katjack mikefuck normal
            jack.say "I..."
            jack.say "I'm okay, really..."
            jack.say "I just need a second to catch my breath!"

            "Jack looks at me pleadingly while Kat continues to turn towards him."
            "And I know that I'm going to have to step in here and save his ass."
            "So I quickly go near the other end of the lounger too."

            "By now, Kat's pretty much within reach."
            "And she makes it that much easier for me by looking the other way."
            show katjack mikefuck mike out with hpunch
            "Which means I can just reach out and grab hold of her."
            show katjack mikefuck surprised
            kat.say "Huh?"
            kat.say "What the..."
            show katjack mikefuck normal
            mike.say "Get your ass over here, Kat..."
            mike.say "I've got something for you!"
            "Lifting Kat's right thigh, I spread her legs wide."
            "And art the same time I give myself easy access to what lies between."
            "It's about now that what I'm doing seems to dawn on Kat."
            "She stops wriggling and instead lets me have my way."
            "And I see her staring down at my cock too."
            "Obviously she's wondering what I'm going to do with it."
            "So I guess I'd better make up my own mind too!"
            menu:
                "Fuck her pussy":
                    "I can easily see that Jack and I aren't the only ones getting worked up here."
                    "Because the light is already making the lips of Kat's pussy glisten."
                    "And the sight of it is something that I just can't hope to resist."
                    "I'm not about to beat about the bush either, as I can see what I want."
                    "It's right there for the taking, and Kat's nodding now too."
                    kat.say "What are you waiting for?"
                    kat.say "Put that thing inside me already!"
                    show katjack mikefuck mike vaginal surprised with hpunch
                    "Spurred on by her words, I leap into action."
                    "The first thrust that I make doesn't get me inside of her."
                    "But then I never expected it to, only to rub along the length of her lips."
                    "The real aim was to make her quiver with anticipation."
                    "That and to make sure that she wants more the next time round."
                    show katjack mikefuck mike normal at stepback(speed=0.1, h=10, v=0)
                    "So that when I make my second thrust, I feel her beginning to melt."
                    "It's still not enough to get me inside, but it encourages me to try again."
                    show katjack mikefuck at stepback(speed=0.1, h=10, v=0)
                    "And this time I feel myself gasp as the head sinks into Kat."
                    "There's no thought of pulling back and trying again."
                    "Instead I push even harder than before, refusing to back down."
                    "My cock sinks further in, perhaps halfway his time."
                    show katjack mikefuck at stepback(speed=0.1, h=10, v=0)
                    "I feel like I'm pushing a massive boulder uphill."
                    "That I'm struggling with all my might to reach the very top."
                    "And when I do, gravity turns everything in my favour."
                    "All of that means I feel myself sink all the way into Kat."
                    show katjack mikefuck at stepback(speed=0.1, h=10, v=0)
                    "The entire length of my cock is swallowed by her pussy."
                    "But the momentum is too strong to resist, and I don't stop."
                    "The moment I fill her, I start to move back and forth."
                    show katjack mikefuck at stepback(speed=0.1, h=10, v=0)
                    "And before she has a chance to recover, I'm pounding her for all I'm worth."
                    "Kat throws her head back and moans, letting me know I'm hitting the spot."
                    "But at the back of my mind, I'm praying that Jack doesn't move an inch."
                    "Because I'm pretty sure if he does, the lounger will topple over!"
                    "As if reading my mind, Kat stretches backwards a moment later."
                    show katjack mikefuck mike jack lick with hpunch
                    "Soon Jack joins us, standing in front of Kat."
                    "And she reaches out for Jack's cock, putting it straight into her mouth."
                    "He's in no condition to argue, just groaning."
                    "All of which means I have the guaranteed counterweight I need."
                    "It only occurs to me then why Kat's chosen now to suck his cock again."
                    "I can feel her muscles clenching around my cock with growing strength."
                    "So she must have put it in there to keep herself quiet while she cums!"
                    "The mere thought of it thrills me so much that I realise I'm about to join her."
                    "I probably have no more than a few seconds to decide what to do next!"
                    menu:
                        "Cum inside":
                            "But why do anything else when what I'm doing right now feels so good?"
                            show katjack mikefuck xray with hpunch
                            "All it takes is a few more deep thrusts, and then I feel myself losing it."
                            show katjack mikefuck mikecum with hpunch
                            "With my cock all the way inside of Kat, I shoot my load, totally filling her."
                            show katjack mikefuck ahegao open with hpunch
                            "She cums at the same time too, almost rolling off the sun-lounger as it happens."
                        "Pull out":
                            "Feeling a little perverse after all the effort it took to get in there, I decide to pull out."
                            "I don't know where the urge comes from, just that I can't seem to resist it."
                            show katjack mikefuck out mikecum with hpunch
                            "And so I slide my cock out of Kat the moment before I lose it."
                            with hpunch
                            "Then I shoot my load over her belly as she cums too, almost rolling off the sun-lounger as it happens."
                "Fuck her ass":
                    "I can easily see that Jack and I aren't the only ones getting worked up here."
                    "Because the light is already making the curves of Kat's ass glisten."
                    "And the sight of it is something that I just can't hope to resist."
                    "I'm not about to beat about the bush either, as I can see what I want."
                    "It's right there for the taking, and Kat's nodding now too."
                    kat.say "What are you waiting for?"
                    kat.say "Put that thing inside me already!"
                    show katjack mikefuck mike anal surprised with hpunch
                    "Spurred on by her words, I leap into action."
                    "The first thrust that I make doesn't get me inside of her."
                    "But then I never expected it to, only to rub around the edge of her hole."
                    "The real aim was to make her quiver with anticipation."
                    "That and to make sure that she wants more the next time round."
                    show katjack mikefuck mike normal at stepback(speed=0.1, h=10, v=0)
                    "So that when I make my second thrust, I feel her beginning to melt."
                    "It's still not enough to get me inside, but it encourages me to try again."
                    show katjack mikefuck at stepback(speed=0.1, h=10, v=0)
                    "And this time I feel myself gasp as the head sinks into Kat."
                    "There's no thought of pulling back and trying again."
                    "Instead I push even harder than before, refusing to back down."
                    "My cock sinks further in, perhaps halfway his time."
                    show katjack mikefuck at stepback(speed=0.1, h=10, v=0)
                    "I feel like I'm pushing a massive boulder uphill."
                    "That I'm struggling with all my might to reach the very top."
                    "And when I do, gravity turns everything in my favour."
                    "All of that means I feel myself sink all the way into Kat."
                    "The entire length of my cock is swallowed by her ass."
                    "But the momentum is too strong to resist, and I don't stop."
                    show katjack mikefuck at stepback(speed=0.1, h=10, v=0)
                    "The moment I fill her, I start to move back and forth."
                    "And before she has a chance to recover, I'm pounding her for all I'm worth."
                    "Kat throws her head back and moans, letting me know I'm hitting the spot."
                    "But at the back of my mind, I'm praying that Jack doesn't move an inch."
                    "Because I'm pretty sure if he does, the lounger will topple over!"
                    "As if reading my mind, Kat stretches backwards a moment later."
                    show katjack mikefuck mike jack lick with hpunch
                    "Soon Jack joins us, standing in front of Kat."
                    "And she reaches out for Jack's cock, putting it straight into her mouth."
                    "He's in no condition to argue, just groaning."
                    "All of which means I have the guaranteed counterweight I need."
                    "It only occurs to me then why Kat's chosen now to suck his cock again."
                    "I can feel her muscles clenching around my cock with growing strength."
                    "So she must have put it in there to keep herself quiet while she cums!"
                    "The mere thought of it thrills me so much that I realise I'm about to join her."
                    "I probably have no more than a few seconds to decide what to do next!"
                    menu:
                        "Cum inside":
                            "But why do anything else when what I'm doing right now feels so good?"
                            show katjack mikefuck with hpunch
                            "All it takes is a few more deep thrusts, and then I feel myself losing it."
                            show katjack mikefuck with hpunch
                            "With my cock all the way inside of Kat, I shoot my load, totally filling her."
                            show katjack mikefuck ahegao open with hpunch
                            "She cums at the same time too, almost rolling off the sun-lounger as it happens."
                        "Pull out":
                            "Feeling a little perverse after all the effort it took to get in there, I decide to pull out."
                            "I don't know where the urge comes from, just that I can't seem to resist it."
                            show katjack mikefuck out mikecum with hpunch
                            "And so I slide my cock out of Kat the moment before I lose it."
                            with hpunch
                            "Then I shoot my load over her belly as she cums too, almost rolling off the sun-lounger as it happens."
        "Let Jack fuck Kat":
            $ kat.flags.jack_pleased += 1
            "Maybe I should be more of a selfish asshole at times like this."
            "But all I can think of is how much Jack wanted this to happen."
            "And so I just can't put myself first right now."
            "Which is why I put my hands on Kat's hips and begin to push her downwards."
            "Jack's already flopped onto one of the sun-loungers by the side of the pool."
            scene bg black
            show katjack jackfuck pool
            with fade
            "And it doesn't take much effort for me to push Kat down and onto him."
            "At first she looks at me with confusion in her eyes."
            "Probably wondering what guy in his right mind would push her away from him."
            "But then the glances back over her shoulder and sees Jack for the first time."
            "And when she looks back at me again, it's clear that Kat understands my intentions."
            kat.say "Hey, Jack..."
            kat.say "You want to make my day?"
            "Jack looked more than a little exhausted when he sat down on the lounger just now."
            "But when he hears Kat asking him the question, he seems to come alive again."
            jack.say "Wha..."
            jack.say "I..."
            jack.say "Whoa!"
            jack.say "Sure thing, Kat - I'd do anything for you!"
            "Kat smiles and lets out a particularly sexy giggle."
            "All of which makes me regret letting Jack take the lead here."
            "But I already made that decision, so I just smile too."
            "This is going to be Jack's show, and I'm just here to watch."
            "Jack reaches up and takes hold of Kat around the waist."
            "And she reciprocates by gently lowering herself onto him."
            "Yet even as she's getting closer to his cock, Jack's not looking at her."
            "I realise that he's actually looking at me instead!"
            mike.say "What is it?"
            "I hiss, trying to make it sound discreet."
            jack.say "Help me out, dude..."
            jack.say "Tell me where to put it!"
            "Fuck's sake!"
            "Can't this guy do anything for himself?"













































































            "I don't want Jack to blow this, for both our sakes."
            "But I want this to be memorable for Kat too."
            mike.say "Go for the back-door, Jack..."
            mike.say "Show the lady that you can mix it up a little!"
            "Jack nods eagerly."
            "And then he turns his attention to the task at hand."
            "Kat seems to have overheard the conversation."
            "But she chooses to keep her thoughts to herself."
            "All she gives me is a quick wink, which I take as Kat showing her approval."
            "Though for all of his apparent nerves, Jack seems to step up to the challenge."
            show katjack jackfuck jack at stepback(speed=0.1, h=-10, v=0)
            "Because I can see that he has a firm hold on Kat right now."
            "And from the look on her face, he's really asserting himself!"
            show katjack jackfuck jack closed jackinside at stepback(speed=0.05, h=-10, v=0)
            "I watch Kat's face as she begins to feel what he's doing down there."
            "Almost being able to feel the same things that she is as they happen."
            show katjack jackfuck jack open at stepback(speed=0.05, h=-10, v=0)
            "At first Kat holds my eye and seems to be intent on keeping it so."
            "But it doesn't take long for the look in her eyes to become far away."
            "It's like I'm watching Jack's attentions take hold and overcome her senses."
            "Kat's lips part, and her breathing starts to quicken too."
            show katjack jackfuck jack closed at stepback(speed=0.05, h=-10, v=0)
            "Before much longer she's kind of panting, rather than just breathing."
            "And I'm fully expecting her tongue to start lolling out of her mouth."
            "Hell, I wouldn't be surprised if she actually went cross-eyed!"
            "Impressed by the effect Jack's having on her, I take a step backwards."
            "This lets me sneak a look at what's going on down there."
            "And I have to say that I'm pretty impressed by what I see."
            show katjack jackfuck jack open at stepback(speed=0.05, h=-10, v=0)
            "Jack looks every bit as distracted from reality as Kat."
            "But in his case it's all on account of concentration."
            "Normally I wouldn't pay close attention to another guy making love."
            "Yet there's something oddly compelling about watching Jack go at it."
            show katjack jackfuck jack closed shake at stepback(speed=0.05, h=-10, v=0)
            "His cock is sliding in and out of Kat's hole like a pink piston."
            show katjack jackfuck jack open at stepback(speed=0.05, h=-10, v=0)
            "Going so fast that I can't believe this is my familiar, out of shape buddy."
            show katjack jackfuck jack closed at stepback(speed=0.05, h=-10, v=0)
            "Maybe that belly really is the fuel-tank for a love-machine?"
            "Suddenly I realise that I'm standing there, staring at Jack's cock."
            "And if it is doing things to Kat right now, then so can I!"
            show katjack jackfuck jack open at stepback(speed=0.05, h=-10, v=0)
            "Taking advantage of the fact that she's totally out of it, I lean in close."
            "I open my mouth and place my lips against Kat's."
            "The move was kind of experimental, but the result is instant."
            "I say that because I feel Kat's tongue dart into my mouth a second later."
            "Without pause or hesitation, we're kissing with a genuine passion."
            show katjack jackfuck jack closed at stepback(speed=0.05, h=-10, v=0)
            "I feel myself reach out and begin to touch her body too."
            "All of this comes as part of a natural flow, without a single conscious thought."
            "And now I feel like I'm involved for real, sensing what's passing between them."
            "Kat responds to my touch, her body beginning to move faster than before."
            show katjack jackfuck jack closed at stepback(speed=0.05, h=-10, v=0)
            "I can feel a change in Jack too, his thrusts becoming harder and more desperate."
            jack.say "Urgh..."
            jack.say "[hero.name]..."
            show katjack jackfuck jack closed at stepback(speed=0.05, h=-10, v=0)
            jack.say "I'm gonna cum..."
            jack.say "What do I do?!?"
            show katjack jackfuck jack closed at stepback(speed=0.05, h=-10, v=0)
            "Seriously?"
            "This again?"
            show katjack jackfuck jack closed at stepback(speed=0.05, h=-10, v=0)
            "Breaking off the kiss with Kat, I turn my attention back to Jack."
            menu:
                "Encourage him to cum inside":
                    mike.say "Just keep going, Jack..."
                    mike.say "Don't stop now!"
                    "Jack nods, hurrying to do as he's told."
                    show katjack jackfuck jack jackinside jackcum with hpunch
                    "Then I watch as he groans, letting go deep inside of Kat."
                    with hpunch
                    "But to be perfectly honest, I'm more interested in watching Kat."
                    show katjack jackfuck jack ahegao -shake with hpunch
                    "As she begins to cum a moment later, writhing and twitching as it happens."
                    "The fact that she's pressed against me at the time just adds to the experience too!"
                "Order him to pull out":
                    mike.say "Pull out, Jack..."
                    mike.say "Do it now!"
                    "Jack nods, hurrying to do as he's told."
                    show katjack jackfuck jack jackoutside jackcum -shake with hpunch
                    "Then I watch as he groans, dragging himself out of Kat."
                    show katjack jackfuck jack bodycum with hpunch
                    "But to be perfectly honest, I'm more interested in watching Kat."
                    show katjack jackfuck jack ahegao -jackcum with hpunch
                    "As she begins to cum a moment later, writhing and twitching as it happens."
                    "The fact that she's pressed against me at the time just adds to the experience too!"
        "Team up on her":
            $ kat.flags.mike_pleased += 0.5
            $ kat.flags.jack_pleased += 0.5
            "It seems crazy to me that I'm trying to decide who gets to fuck Kat."
            "I mean, aren't we supposed to be having a crazy threesome here?"
            "Why am I worrying about who gets to do who?"
            "Everyone should be getting their own piece of the action."
            "Especially when there are more than enough holes and cocks to fill them!"
            "I put my hands on Kat's hips and begin to push her downwards."
            mike.say "Jack..."
            mike.say "Wake the hell up!"
            "Jack's already flopped onto one of the sun-loungers by the side of the pool."
            scene bg black
            show katjack foreplay pool open
            with fade
            "And it doesn't take much effort for me to push Kat down and onto him."
            "At first she looks at me with confusion in her eyes."
            "Probably wondering what guy in his right mind would push her away from him."
            "But then the glances back over her shoulder and sees Jack for the first time."
            show katjack doublepen pool with fade
            "And when she looks back at me again, it's clear that Kat understands my intentions."
            "Or at least she thinks that she does!"
            kat.say "Hey, Jack..."
            kat.say "You want to make my day?"
            "Jack looked more than a little exhausted when he sat down on the lounger just now."
            "But when he hears Kat asking him the question, he seems to come alive again."
            jack.say "Wha..."
            jack.say "I..."
            jack.say "Whoa!"
            jack.say "Sure thing, Kat - I'd do anything for you!"
            "Kat smiles and lets out a particularly sexy giggle."
            "My guess is that she's expecting me to hand her over to Jack, then back off."
            "So I understand the look of confusion on her face when I follow her down as well."
            kat.say "Huh?"
            kat.say "What are you..."
            mike.say "Just leave this to me, Kat..."
            mike.say "All you need to do is sit back and relax."
            "As I say all of this, Jack sticks his head over Kat's shoulder."
            "I see he has a hand held in the air and a puzzled look on his face."
            jack.say "Erm..."
            jack.say "What exactly's going on here?"
            menu:
                "Go for her pussy":
                    mike.say "I'm taking the front, Jack..."
                    mike.say "That leaves you with the back-door, okay?"
                    "Jack blinks and stares at me for a moment, like he doesn't get it."
                    "But then I see understanding dawn on him, and he nods eagerly."
                    jack.say "We're both going to do her at the same time?!?"
                    jack.say "You got it, buddy!"
                    "Kat looks from Jack and then back to me."
                    kat.say "I'm guessing I don't get a say in this?"
                    mike.say "Well..."
                    mike.say "I..."
                    "Kat chuckles and shakes her head."
                    kat.say "Just make sure I get taken to heaven and back, okay?"
                    "Jack and I are both nodding by now."
                    show katjack doublepen jackback with fade
                    "Because we're desperately keen to show Kat what we can do together."
                    "Kat reaches out, putting her arms around my neck."
                    show katjack doublepen jackback mikefront with hpunch
                    "And then she pulls herself closer to me."
                    "My cock is already practically between her legs."
                    "Which means that I only have to make the slightest of movements."
                    show katjack doublepen pleasure closed blush
                    "And as soon as I do, Kat lets out a moan of pure delight."
                    "I can't help gasping too, as I feel the head of my cock brush her pussy."
                    "The lips are warm and already getting slick, like she's almost ready for me."
                    "I make sure to support Kat as I stroke the head up and down them too."
                    "Of course there's a measure of natural resistance in them."
                    "But with each pass I can feel it beginning to fade a little more."
                    "Until the point where it's strength can't match my will to get inside."
                    "When that happens, I feel myself sink in perhaps an inch or more."
                    show katjack doublepen mikevaginal
                    "Making to go further, I push forwards."
                    "At the same time, instinct alone makes Kat move backwards."
                    show katjack doublepen jackanal
                    "And when she does, Jack's right there, waiting for her."
                    show katjack doublepen scared open
                    kat.say "Oh..."
                    kat.say "Oh wow..."
                    kat.say "Oh fuck..."
                    show katjack doublepen pleasure
                    "I can't feel what's going on back there, or see it for that matter."
                    "But what I can feel is the way Kat's starting to quiver from head to toe!"
                    "Whatever Jack's doing, he seems to be meeting with no obstacles whatsoever."
                    show katjack doublepen closed at stepback(speed=0.05, h=10, v=10)
                    "And what little I can see of him appears to already be moving back and forth."
                    "Not wanting to be left out, I quicken my own pace, trying to catch up to Jack."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                    "Soon enough this means that Kat's being pounded from both directions at once."
                    "And neither of us is going to slow down for fear of being the weak link in the chain."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                    "Trapped between Jack and myself, all Kat can do is take all that she's being given."
                    "She tosses her head and rolls her eyes, gasping for breath the whole time."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                    "And when she grabs hold of me with her hands, I feel her nails raking my skin!"
                    "Part of me is wondering how long we're going to be able to keep this up."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                    jack.say "Urgh..."
                    jack.say "[hero.name]..."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                    jack.say "I'm gonna cum..."
                    jack.say "What do I do?!?"
                    show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                    "And it looks like Jack just gave me my answer."
                    "But I'm kind of thankful for it, as I was about to admit the same thing."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                    "This way at least it looks like Jack called time rather than me!"
                    menu:
                        "Tell him that you both need to cum inside":
                            mike.say "Just keep going, Jack..."
                            mike.say "Don't stop now!"
                            show katjack doublepen closed at stepback(speed=0.05, h=10, v=10)
                            "Jack nods, hurrying to do as he's told."
                            "Then I watch as he groans, letting go deep inside of Kat."
                            show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                            "All it takes is a few more deep thrusts, and then I feel myself losing it."
                            show katjack doublepen orgasm mikecum jackcum with vpunch
                            "With my cock all the way inside of Kat, I shoot my load, totally filling her."
                            with vpunch
                            "She cums at the same time too, almost rolling off the sun-lounger and taking us with her."
                        "Tell him to cover her body with semen":
                            mike.say "Pull out, Jack..."
                            mike.say "Do it now!"
                            show katjack doublepen jackout
                            "Jack nods, hurrying to do as he's told."
                            show katjack doublepen jackcum with vpunch
                            "Then I watch as he groans, dragging himself out of Kat, painting her back with sticky white stripes."
                            "Feeling a little perverse after all the effort it took to get in there, I decide to pull out too."
                            "I don't know where the urge comes from, just that I can't seem to resist it."
                            show katjack doublepen mikeout mikecum with hpunch
                            "And so I slide my cock out of Kat the moment before I lose it."
                            show katjack doublepen orgasm with hpunch
                            "Then I shoot my load over her belly as she cums too, almost rolling off the sun-lounger as it happens."
                "Go for her ass":
                    mike.say "I'm taking the back-door, Jack..."
                    mike.say "That leaves you with the front, okay?"
                    mike.say "But we need to switch places first!"
                    "Jack blinks and stares at me for a moment, like he doesn't get it."
                    "But then I see understanding dawn on him, and he nods eagerly."
                    jack.say "We're both going to do her at the same time?!?"
                    jack.say "You got it, buddy!"
                    "Kat looks from Jack and then back to me."
                    kat.say "I'm guessing I don't get a say in this?"
                    mike.say "Well..."
                    mike.say "I..."
                    "Kat chuckles and shakes her head."
                    kat.say "Just make sure I get taken to heaven and back, okay?"
                    "Jack and I are both nodding by now."
                    show katjack doublepen mikeback with fade
                    "Because we're desperately keen to show Kat what we can do together."
                    "As quickly as we can, Jack and I swap places."
                    "Then Kat reaches out, putting her arms around Jack's neck."
                    show katjack doublepen mikeback jackfront with hpunch
                    "And then she pulls herself closer to him."
                    "This leaves me sitting right behind her, not even able to see her face."
                    "But my cock is already practically between her legs."
                    "Which means that I only have to make the slightest of movements."
                    show katjack doublepen pleasure closed blush
                    "And as soon as I do, Kat lets out a moan of pure delight."
                    "I can't help gasping too, as I feel the head of my cock brush her hole."
                    "It feels warm and welcoming, like she's almost ready for me."
                    "I make sure to pull Kat towards me as I stroke the head up and down them too."
                    "Of course there's a measure of natural resistance in her muscles."
                    "But with each pass I can feel it beginning to fade a little more."
                    "Until the point where it's strength can't match my will to get inside."
                    "When that happens, I feel myself sink in perhaps an inch or more."
                    show katjack doublepen mikeanal
                    "Making to go further, I push forwards."
                    "At the same time, instinct alone makes Kat try to move forwards."
                    show katjack doublepen jackvaginal
                    "And when she does, Jack's right there, waiting for her."
                    show katjack doublepen scared open
                    kat.say "Oh..."
                    kat.say "Oh wow..."
                    kat.say "Oh fuck..."
                    show katjack doublepen pleasure
                    "I can't feel what's going on around the front, or see it for that matter."
                    "But what I can feel is the way Kat's starting to quiver from head to toe!"
                    "Whatever Jack's doing, he seems to be meeting with no obstacles whatsoever."
                    show katjack doublepen closed at stepback(speed=0.05, h=10, v=10)
                    "And what little I can see of him appears to already be moving back and forth."
                    "Not wanting to be left out, I quicken my own pace, trying to catch up to Jack."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                    "Soon enough this means that Kat's being pounded from both directions at once."
                    "And neither of us is going to slow down for fear of being the weak link in the chain."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                    "Trapped between Jack and myself, all Kat can do is take all that she's being given."
                    "She tosses her head and rolls her eyes, gasping for breath the whole time."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                    "And when she grabs hold of me with her hands, I feel her nails raking my skin!"
                    "Part of me is wondering how long we're going to be able to keep this up."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                    jack.say "Urgh..."
                    jack.say "[hero.name]..."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                    jack.say "I'm gonna cum..."
                    jack.say "What do I do?!?"
                    show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                    "And it looks like Jack just gave me my answer."
                    "But I'm kind of thankful for it, as I was about to admit the same thing."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                    "This way at least it looks like Jack called time rather than me!"
                    menu:
                        "Tell him that you both need to cum inside":
                            mike.say "Just keep going, Jack..."
                            mike.say "Don't stop now!"
                            show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                            "Jack nods, hurrying to do as he's told."
                            "Then I watch as he groans, letting go deep inside of Kat."
                            show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                            "All it takes is a few more deep thrusts, and then I feel myself losing it."
                            show katjack doublepen orgasm mikecum jackcum with vpunch
                            "With my cock all the way inside of Kat, I shoot my load, totally filling her."
                            with vpunch
                            "She cums at the same time too, almost rolling off the sun-lounger and taking us with her."
                        "Tell him to cover her body with semen":
                            mike.say "Pull out, Jack..."
                            mike.say "Do it now!"
                            show katjack doublepen jackout
                            "Jack nods, hurrying to do as he's told."
                            show katjack doublepen jackcum with hpunch
                            "Then I watch as he groans, dragging himself out of Kat, painting her belly with sticky white stripes."
                            "Feeling a little perverse after all the effort it took to get in there, I decide to pull out too."
                            "I don't know where the urge comes from, just that I can't seem to resist it."
                            show katjack doublepen mikeout mikecum with vpunch
                            "And so I slide my cock out of Kat the moment before I lose it."
                            show katjack doublepen orgasm with vpunch
                            "Then I shoot my load over her back as she cums too, almost rolling off the sun-lounger as it happens."
    scene bg pool with fade
    "Once it's all over, I just want to lie back on the lounger and pass out."
    "But as soon as I have a chance to think clearly again, I leap straight up."
    "And then I begin collecting up my clothes and pulling them on."
    "Jack and Kat seem to catch on without needing to be told."
    "And so soon we're all rushing around, trying to hide the evidence."
    scene bg livingroom with fade
    "Luckily for me, [bree.name] and Sasha don't make an appearance before we're done."
    "So nobody else gets let in on the secret of what we've been up to."
    "But I'm sure that it'll be a long time before any of us forget it."
    $ kat.sexperience += 1
    return

label kat_jack_08:
    "I've been expecting to hear from Jack ever since we had the threesome with Kat."
    "There really wasn't much time to talk about anything once it was all over."
    "And I get the impression he wouldn't have opened up in front of her anyway."
    show jack casual at center, zoomAt(1.25, (640, 920)) with easeinright
    "So when he comes bouncing up to me, I kind of know what I'm about to hear."
    show jack smile
    jack.say "Hey there, buddy..."
    jack.say "How's life treating you?"
    show jack normal
    "I do the best I can to put a smile on my face so as to match the one Jack's wearing."
    "But I doubt that it's anywhere near as wide and beaming in comparison."
    mike.say "Ah..."
    mike.say "Hi, Jack..."
    mike.say "I guess that..."
    show jack smile
    jack.say "Yeah, yeah..."
    jack.say "That's great, [hero.name]…"
    show jack annoyed
    "Jack cuts me off before I can say anything meaningful."
    "Letting me know straight away that he's not really interested in what I have to say."
    "Instead he ploughs straight on with his own agenda, forgetting all about the pleasantries."
    show jack smile
    jack.say "I haven't been able to think about anything but Kat, you know?"
    jack.say "Ever since we all met up and had such serious fun the other day?"
    jack.say "You remember?"
    show jack normal
    "I nod, doing the best I can to forget about my own irritation."
    "Because it seems that this is really important to Jack."
    "And as his friend, I feel like I kind of have to indulge him."
    mike.say "Sure, Jack..."
    mike.say "Of course I remember it."
    mike.say "You don't just forget about a threesome!"
    "Jack nods at this, at least letting me know that he's listening to me."
    "Though he still seems to be more interested in steering the conversation himself."
    "That agenda that I mentioned before pulling him in a certain direction."
    show jack smile
    jack.say "Oh, but it was so much more than that!"
    jack.say "I felt like it was kind of a revelation, [hero.name]."
    jack.say "One of those things that opens your eyes to the reality of the world."
    show jack happy
    jack.say "You know, like something that changes you?"
    show jack normal
    mike.say "We had a threesome, Jack..."
    mike.say "And yeah, it was a lot of fun."
    mike.say "But you're making it sound like some kind of spiritual awakening!"
    "The comment was supposed to bring Jack back down to earth."
    "But instead it seems to do the opposite, as he nods his head."
    show jack smile
    jack.say "That's exactly what it did!"
    jack.say "It made me realise something really important."
    jack.say "It made me realise that I'm in love with Kat!"
    show jack normal
    "Jack's admission kind of takes me by surprise."
    "And I have to stop for a moment to be able to process it."
    menu:
        "What a coincidence! I'm in love too!":
            "The only problem is that I feel the exact same way about Kat."
            "And my brain can't help itself when the subject comes up."
            "I just have to admit the nature of my feelings for her."
            mike.say "Oh my god..."
            show jack surprised
            mike.say "Me too!"
            mike.say "I'm totally head over heels in love with Kat!"
            "Now it's Jack's turn to look stunned."
            "He takes a step backwards."
            "And he looks from side to side."
            "All of which makes me start to feel nervous."
            "I mean, is he going to punch me in the face, or something like that?"
            show jack smile
            jack.say "DUDE..."
            show jack happy
            jack.say "That's great news!"
            show jack normal
            mike.say "It..."
            mike.say "It is?"
            "Jack nods his head furiously."
            show jack smile
            jack.say "Yeah, it is..."
            jack.say "It means we can all be together..."
            show jack happy
            jack.say "You, me and Kat - all three of us!"
            show jack normal
            "We seem to be going back and forth here."
            "One moment I'm stunned, then Jack is."
            "And now it's back to being my turn."
            "I was expecting Jack to be mad, to see me as a rival."
            "But instead he's loving the idea."
            "In fact he seems to be pondering something about it right now."
            show jack smile
            jack.say "Oh, oh, oh..."
            jack.say "We should propose to her, you and me..."
            show jack happy
            jack.say "We should both ask Kat to marry us!"
            show jack normal
            menu:
                "You're right! Let's both marry her!":
                    "I almost gape at Jack."
                    mike.say "You mean we ask her to marry us both?!?"
                    "Jack nods eagerly."
                    show jack smile
                    jack.say "Yeah, dude..."
                    jack.say "That'd be so dope..."
                    jack.say "Don't you think?"
                    show jack normal
                    "Marrying my best friend and the woman I love?"
                    "What could possibly go wrong?"
                    mike.say "You bet it would!"
                    mike.say "We should do it as soon as possible..."
                    mike.say "How quickly do you think we can get some rings?"
                    show jack happy
                    "And just like that, Jack and I are into it."
                    "We're discussing the details of the proposal."
                    "Chatting away as though Kat's already said yes."
                    "But I feel sure that she will."
                    "All we need to do now is pop the question."
                    "And then the three of us can spend the rest of our lives together!"
                    $ jack.flags.trouple_wedding = True
                "Thaaaat's way too weird for me to be in couple with you...":
                    "I frown at Jack."
                    mike.say "You mean ask her and see who she chooses?"
                    mike.say "Like, if she says yes to one of us and turns the other down?"
                    show jack surprised
                    "Jack looks kind of shocked by my questions."
                    "He shakes his head vigorously."
                    show jack worried
                    jack.say "No..."
                    jack.say "I mean ask her to marry both of us!"
                    show jack sadsmile
                    "I can't help laughing at the suggestion."
                    "And that doesn't seem to sit well with Jack."
                    show jack surprised
                    jack.say "Huh?"
                    jack.say "What's so funny?"
                    jack.say "Why are you laughing at me?!?"
                    show jack sadsmile
                    mike.say "Jack, you're asking me to marry you!"
                    mike.say "You're my friend, but I don't feel that way about our relationship."
                    show jack sad
                    "Jack's expression darkens as he hears what I have to say."
                    show jack angry
                    jack.say "Oh that's just perfect, [hero.name]."
                    jack.say "I open up to you about how I feel."
                    jack.say "I even try to include you in there too."
                    jack.say "And you just throw it all back in my face!"
                    show jack whining
                    jack.say "Well screw you..."
                    jack.say "Kat and I will be happy together without you!"
                    hide jack with easeoutright
                    "With that, Jack turns on his heel and storms off."
                    "I think about going after him."
                    "Trying to explain myself better and calm him down."
                    "But in the end I decide to leave it alone."
                    "You see, Jack's not the most experienced of guys."
                    "Especially when it comes to women!"
                    "So he tends to fall for them at the drop of a hat."
                    "Most likely he'll be infatuated with Kat for a few weeks."
                    "And then he'll see some other streamer or cosplayer that'll distract him."
                    "Once things are back to normal, he'll forget all about it."
                    "I just have to ride it out until then, that's all."
                    $ jack.flags.trouple_wedding = False
        "You should calm down a bit buddy...":
            "My first instinct is to tell Jack to back off."
            "To tell him that I was in love with Kat first."
            "But then I remember who it is that I'm talking to."
            "You see, Jack's not the most experienced of guys."
            "Especially when it comes to women!"
            "So he tends to fall for them at the drop of a hat."
            "Most likely he'll be infatuated with Kat for a few weeks."
            "And then he'll see some other streamer or cosplayer that'll distract him."
            "Which means the best thing would probably be to keep my feelings to myself."
            mike.say "Wow..."
            mike.say "You really mean that, Jack?"
            mike.say "You've actually got feelings for Kat?"
            "Jack nods eagerly, not suspecting a thing."
            show jack smile
            jack.say "Oh yeah..."
            jack.say "I'm totally in love with her, dude!"
            show jack happy
            jack.say "And this time it's the real thing, I just know it!"
            show jack normal
            "I nod and smile, doing the best I can to seem genuine."
            mike.say "Well, that's kind of what you always say."
            mike.say "So maybe just temper your expectations, yeah?"
            show jack blank
            "Jack looks at me like I started speaking in a foreign language."
            "He shakes his head, letting me know that he totally disagrees."
            show jack whining
            jack.say "What are you talking about, dude?"
            jack.say "This is it - this is true love!"
            jack.say "You should be rooting for me."
            show jack sadsmile
            "All I can do is shrug."
            "That and try to look sympathetic."
            mike.say "I just don't want you to get hurt, that's all."
            mike.say "You know how sensitive you are, Jack..."
            mike.say "You're not exactly hard-hearted!"
            "But not matter what I say, it doesn't seem to make a difference."
            show jack lying
            jack.say "Don't worry about me, dude..."
            jack.say "I just know this is going to work out!"
            show jack happy
            jack.say "Kat and I are meant to be together."
            show jack smile
            jack.say "And I'm sure she feels the same way too."
            show jack normal
            "I nod and smile, not wanting to say anything more."
            "Jack seems to be set on the course he's chosen."
            "But I'm going to have to be pretty canny on my own part."
            "I want to make sure this goes in my favour and not his."
            "Because while he's my friend, I won't give Kat up for Jack's sake."
            $ jack.flags.trouple_wedding = False
    return


label jack_kat_special:
    $ renpy.dynamic(jack_score=0, kat_score=0)
    scene bg street with fade
    "It's weird that I've known Jack for literally years and in that time we've hung-out countless times."
    "And once I got to know Kat too, we found it really easy to spend time together, just having fun."
    "So on the face of it, being in a relationship with both of them should be the easiest thing in the world."
    "But then you add the sexual dimension into the mix, and somehow everything changes."
    "I feel kind of awkward when we're trying to do things that are just totally normal."
    "And the worst thing is that Jack and Kat don't seem to be having the same issues I am."
    "Whenever we're all together, they just act perfectly normal."
    "Kat kind of teases Jack and he reacts like he hates it, when in reality he loves the attention."
    "And that's where I want to be too, a place where we can be friends as well as lovers."
    "So I figure that the best thing to do is spend time doing those normal things that friends do."
    "The first and foremost of them being a trip to the mall."
    "I've arranged to meet Jack and Kat just inside the main entrance."
    "But the problem is that I got held up on the way there."
    "So I'm already running late!"
    "And I do mean that I'm running in the literal sense of the word."
    "Gasping and panting as I finally manage to slow down in sight of the mall's doors."
    scene bg mall1
    show jack casual embarrassed at center, zoomAt(1.0, (440, 760))
    show kat casual smile at center, zoomAt(1.0, (840, 720))
    with fade
    "Much to my relief, I can see that Jack and Kat are already here."
    "So I begin waving to them as I stagger the last few feet to where they're standing."
    mike.say "Urgh..."
    mike.say "Phew..."
    mike.say "Hey, guys!"
    show jack surprised at center, traveling(1.25, 0.2, (440, 920))
    show kat stuned at center, traveling(1.25, 0.2, (840, 880))
    "Jack and Kat turn to see me approaching."
    "And I can see that they're more than a little surprised by the state I'm in."
    show kat surprised
    kat.say "Wow..."
    kat.say "I haven't seen you sweat this much since I last beat your ass on the Z-Box!"
    show kat smile
    jack.say "Yeah, [hero.name]…"
    jack.say "You look really wasted."
    jack.say "Have you been skimping on going to the gym?"
    show jack smile
    if randint(1, 2) == 2:

        "I can't believe they're ganging up on me like this."
        "Aren't we supposed to be having some quality time together?"
        menu:
            "Brush the comments aside":
                "I feel the urge to say something equally as cutting back to them."
                "But then I remember that we're supposed to be here on what I guess is a date."
                "And so the last thing I want to do is start things off on a negative."
                "So instead I wave a hand in the air, making it clear I'm not rising to the bait."
                mike.say "Ha, ha..."
                mike.say "Very funny, guys..."
                mike.say "Remind me to take the piss out of you the next time you're out of breath."
                "Finally feeling like I can breath again, I shake my head."
                mike.say "Let's just get inside the mall, okay?"
                $ kat_score += 1
                $ jack_score += 1
            "Put Kat in her place":
                "Jack's jibe totally got under my skin."
                "But for some reason it's Kat's that makes me retaliate."
                mike.say "Funny, Kat..."
                mike.say "I seem to remember that I beat your ass the last time we played against each other!"
                mike.say "And when we were done, I hadn't even broken a sweat."
                jack.say "Hah!"
                jack.say "Good comeback, buddy!"
                "Kat scowls at me, and then shoots another hard stare in Jack's direction."
                kat.say "Ah, shut up..."
                kat.say "Let's just get inside the mall."
                $ kat_score -= 1
                $ jack_score += 1
            "Put Jack in his place":
                "Kat's jibe totally gets under my skin."
                "But for some reason it's Jack's that makes me retaliate."
                "So I round on him and poke a finger into his belly."
                mike.say "Funny thing, Jack..."
                mike.say "I don't remember seeing you down the gym recently?"
                mike.say "Or ever, come to think of it."
                kat.say "Hah!"
                kat.say "Take that, tubby!"
                "Jack scowls at me, and then shoots another hard stare in Kat's direction."
                jack.say "Ah, shut up..."
                jack.say "Let's just get inside the mall."
                $ kat_score += 1
                $ jack_score -= 1
            "Put Jack and Kat in their places":
                "I wanted this thing to go well right from the start."
                "But not for me to be the butt of all the jokes."
                "And I feel like I need to stand up for myself here."
                "Otherwise they're going to keep on taking the piss all the time we're here."
                mike.say "Will you two lay off me?"
                mike.say "I tried to get here as quickly as I could, okay?"
                mike.say "It's not my fault that I got held up along the way!"
                "Jack and Kat exchange a knowing glance."
                "And then they start shaking their heads."
                jack.say "Ah, quit moaning, [hero.name]…"
                jack.say "We were just messing with you."
                kat.say "You really are way too sensitive, you know?"
                kat.say "It can be a bit of a downer!"
                "I look away from them, trying not to admit that they're probably right."
                mike.say "Ah, shut up..."
                mike.say "Let's just get inside the mall."
                $ kat_score -= 1
                $ jack_score -= 1
    else:

        "I feel like they're both ganging up on me."
        "But maybe I can use a little manipulation to turn things around?"
        "I just have to make them feel guilty."
        "And I think I know how to do it."

        if hero.charm >= 75:
            "I let out a sigh and shake my head."
            "And then I make it seem like I'm ignoring the comments."
            "But I'm sure to let Kat and Jack see that I'm doing so."
            mike.say "Whatever..."
            mike.say "Let's..."
            mike.say "Let's just get inside, okay?"
            "As I turn to walk into the mall, Kat grabs hold of my wrist."
            show kat surprised
            kat.say "Wait a minute, [hero.name]…"
            kat.say "Are you okay?"
            show kat sad
            show jack whining
            jack.say "Yeah, buddy..."
            jack.say "It was just a joke, right?"
            show jack sadsmile
            mike.say "Ah..."
            mike.say "I just put a lot into this, you know?"
            mike.say "I wanted everything to be perfect?"
            show jack embarrassed
            show kat shy
            "Much to my delight, Kat and Jack share a concerned glance."
            "Then they start doing all they can to make amends."
            show jack smile
            jack.say "Don't worry, man..."
            jack.say "It'll be great!"
            show jack normal
            show kat talkative
            kat.say "We'll make sure it is, okay?"
            show kat smile
            "I can't help treating myself to a smile as my plan works out."
            "But I make sure that Kat and Jack don't catch me doing so."
            $ kat_score += 1
            $ jack_score += 1
        else:

            "I do the best I can to make myself look hurt."
            "And then I let out a sigh to add to the effect."
            mike.say "Oh man..."
            mike.say "I can't believe you guys are being so mean to me!"
            "I can tell from the tone of my voice that something's going wrong."
            "And almost as soon as they hear what I have to say, Kat and Jack look unimpressed."
            show jack happy at startle
            show kat happy at startle
            "They share a knowing look and then start to laugh, shaking their heads the whole time."
            show kat smile
            show jack smile
            jack.say "Aww..."
            jack.say "Did we hurt your feelings?"
            show jack normal
            show kat talkative
            kat.say "That's too bad, [hero.name]…"
            kat.say "Because now we're gonna be even meaner!"
            show kat defiant
            "All I can do is try to ignore the teasing from Kat and Jack."
            "That and put it behind me so that we can get on with the date."
            mike.say "Ah..."
            mike.say "Let's just forget about it, okay?"
            mike.say "Forget about it and get on with the date."
    with fade
    "Almost as soon as we're inside the mall, I hear a really weird sound."
    "It's like a rumbling gurgle, and it reminds me of a blocked sink backing up."
    "The mall's not exactly quiet today, with lots of people all making noise."
    "Yet I can still hear the sound, like it's really close."
    mike.say "Kat..."
    mike.say "Can you hear that?"
    show kat whining
    kat.say "You mean the strange gurgling sound?"
    kat.say "Like they need to get the pipes fixed?"
    show kat normal
    mike.say "That's it exactly!"
    "Now that I know I'm not going mad, I turn to Jack."
    "Because I want to be sure that he can hear it too."
    mike.say "Jack..."
    mike.say "Can you..."
    show jack embarrassed
    "I stop as I see that Jack's looking really embarrassed."
    "And that he's also clutching his stomach with both hands."
    "As Kat turns to look at him too, I see it begin to vibrate."
    "At the same moment I hear the grumbling sound again."
    mike.say "Wow..."
    mike.say "Mystery solved!"
    show kat talkative
    kat.say "Is that really you, Jack?"
    show kat smile
    "Jack looks around, keen to make sure nobody else is listening."
    "Then he leans in closer to us, nodding as he does so."
    show jack whining
    jack.say "Okay, okay..."
    jack.say "It's me making the noises."
    jack.say "I skipped lunch to make it here on time."
    jack.say "And now my stomach's making a formal protest!"
    show jack sadsmile
    mike.say "So..."
    mike.say "We need to do what?"
    mike.say "Feed it?"
    show jack smile at startle
    "Jack nods eagerly at the suggestion."
    "But I can see that Kat's not keen on the idea."
    "She shakes her head and lets out a sigh."
    show kat whining
    kat.say "Oh, Jack..."
    kat.say "We just got here."
    kat.say "Can't you wait a little longer?"
    show kat annoyed
    menu:
        "Suggest Jack grab a snack from a food stall":
            "I shrug and point to a nearby stall selling fast food."
            mike.say "It's not a problem, guys..."
            mike.say "We're at the mall, not time-travelling in the middle ages."
            mike.say "Every modern convenience is to hand!"
            "Jack seems to cheer up as soon as I voice the suggestion."
            show jack happy
            jack.say "Yeah, Kat..."
            jack.say "I just need a quick snack."
            jack.say "Like a pit-stop, you know?"
            show jack normal
            show kat happy at startle
            "Kat giggles and pokes a finger into Jack's belly."
            show kat talkative
            kat.say "Okay, Jack..."
            kat.say "But you're going to have to catch us up, okay?"
            show kat sad
            hide jack with easeoutright
            "Jack nods and hurries off to the stall."
            "And in the meantime, I put an arm around Kat's shoulder."
            show jack casual at center, zoomAt(1.25, (440, 920)) with easeinright
            "We've only walked a short distance when Jack comes back."
            "He's already halfway through whatever he bought to eat."
            "So there's no real way of telling what it is any longer."
            "And I do the best I can to ignore the sounds of his devouring the rest of it too."
            $ jack_score += 1
        "Suggest that Jack can wait a little longer":
            "I put on a smile and place my arm around Kat's shoulder."
            mike.say "Come on, Jack..."
            mike.say "You can live on your body fat for a few weeks at least."
            mike.say "So you're not going to expire before we've looked around a little!"
            show kat happy at startle
            "Kat giggles and pokes a finger into Jack's belly."
            "But this only makes him pull back and look resentful."
            show jack whining
            jack.say "Hey!"
            jack.say "I'll have you know this is all muscle."
            show jack smile
            "But he doesn't get a response."
            "Because Kat and I have already started walking away."
            "This leaves Jack to hurry along after us."
            "And we do the best we can to ignore his complaining too."
            "So after a short while, it just fades into the background noise."
            $ jack_score -= 1
        "Suggest that they should get some food first":
            "I put on a smile and point at Jack's belly."
            mike.say "Trust me, Kat..."
            mike.say "I've known Jack a lot longer than you."
            mike.say "And it's always a bad call to ignore his belly!"
            show jack normal
            "Jack seems to cheer up the second I speak up in his favour."
            show jack smile
            jack.say "Yeah, Kat..."
            jack.say "I just need a quick snack."
            jack.say "Like a pit-stop, you know?"
            show jack normal
            "Kat crosses her arms over her chest and rolls her eyes."
            "But she also seems to surrender at the same time."
            show kat whining
            kat.say "Whatever..."
            kat.say "Let's go somewhere you can stuff your face already!"
            show kat angry
            "Jack happily leads the way to the first place we can get fast food."
            "And then he eagerly ploughs through his order."
            "All while Kat looks bored as hell."
            $ kat_score -= 1
            $ jack_score += 1
        "Leave Jack and Kat to sort themselves out":
            "I hold up my hands and take a step back from Jack and Kat."
            mike.say "Okay..."
            mike.say "One of you wants to eat now."
            mike.say "The other one doesn't."
            mike.say "But I couldn't care either way."
            mike.say "So you need to work this one out between you."
            "I walk a few feet away from Jack and Kat to show that I mean it."
            "And then I turn my back on them, leaving them to debate the matter."
            show kat whining
            kat.say "I don't want to eat now..."
            kat.say "I'm not hungry."
            show kat sad
            show jack sadsmile
            jack.say "Well I am and I do!"
            show jack sad
            show kat angry
            kat.say "Of course you do, Jack..."
            kat.say "You're always hungry!"
            show kat upset
            "The argument rolls on without my involvement."
            "Until in the end they come to a stalemate."
            "Jack doesn't get his food, so he's miserable."
            "But Kat's also pissed-off from the argument."
            "So we walk on in an awkward silence."
            "And I'm left wondering if I made the right decision by keeping out of it."
            $ kat_score -= 1
            $ jack_score -= 1
    "It doesn't take long wandering around the mall for something to pique our interest."
    scene bg arcade with fade
    show jack casual at center, zoomAt(1.25, (440, 920))
    show kat casual at center, zoomAt(1.25, (840, 880))
    with easeinright
    "And it's a no-brainer with Kat, Jack and myself that it'd be the videogame arcade."
    "After all, we're a trio of gamers, all of whom are into the retro titles they have in there."
    "This means that we don't even need to have a discussion about whether or not we go in."
    "Instead we just kind of drift into the place without as much as a word exchanged between us."
    "And once we're inside, we find ourselves surrounded by flashing lights and familiar sound effects."
    "But Kat's the first to announce what she wants to do next."
    show kat talkative
    kat.say "Okay, okay..."
    kat.say "I want to go play one of those classic shooters..."
    kat.say "Maybe 'S-Type', as I haven't played it in ages."
    show kat smile
    show jack blank
    "Jack shakes his head at this."
    show jack whining
    jack.say "Boring!"
    show jack smile
    jack.say "I want to check out the old-school fighting games."
    jack.say "'Avenues of Anger' is calling out to me!"
    show jack normal
    "I can't say that either of those choices appeals to me."
    mike.say "Are you guys sure?"
    mike.say "I was thinking of playing 'Run Out'..."
    mike.say "You know, the racing game?"
    show jack embarrassed
    show kat annoyed
    "As one, Kat and Jack shake their heads at me."
    show kat talkative
    kat.say "Forget that [hero.name]…"
    kat.say "Come play with me instead."
    show kat smile
    show jack smile
    jack.say "Or play with me..."
    jack.say "And avoid dying of boredom!"
    show jack normal
    menu:
        "Choose 'Run Out'":
            "I know that it's going to mean going off and doing my own thing for a while."
            "But I've been itching to play the game that I want in the arcade for ages."
            "And I know that if I don't stay true to my gamer's heart, I'll regret it."
            mike.say "No problem, guys..."
            mike.say "Let's all go play the game we want."
            mike.say "Then we can meet back here when we're done."
            mike.say "How does that sound?"
            "Jack and Kat both nod."
            show kat talkative
            kat.say "Okay, [hero.name]."
            show kat smile
            show jack smile
            jack.say "Sounds good to me too."
            show jack normal
            "With that, we go our separate ways and play the games we want."
            "By the time we're done and we meet up again, I feel like I have arthritic wrists."
            "Kat and Jack seem to be pleased at getting to play the games they wanted too."
            "But I do note that everyone's talking about their own private fun."
            "Rather than anything that we've done as a threesome."
        "Choose 'S-Type'":
            "I know that I'm definitely not in the mood for playing a fighting game."
            "But when I really think about a shooter, that doesn't sound too bad."
            mike.say "I'm not up for playing a beat-em-up, Jack."
            mike.say "But I could probably go for a shoot-em-up, Kat."
            "Jack can't help frowning as he hears what I have to say."
            "Though it's pretty predictable that Kat seems delighted."
            jack.say "You guys are nuts!"
            jack.say "But don't worry about me."
            jack.say "I'll go have fun on my own."
            "With that, he walks off to find the game he wants to play."
            "Which leaves Kat and me to go find her choice of game."
            kat.say "Come on, [hero.name]…"
            kat.say "You're gonna love this, I promise!"
            "By the time we're done and we meet up again, I feel like I have arthritic wrists."
            "Kat and Jack seem to be pleased at getting to play the games they wanted too."
            "But I do note that everyone's talking about their own private fun."
            "Rather than anything that we've done as a threesome."
            $ kat_score += 1
        "Choose 'Avenues of Anger'":
            "I know that I'm definitely not in the mood for playing a shooting game."
            "But when I really think about a fighter, that doesn't sound too bad."
            mike.say "I'm not up for playing a shoot-em-up, Kat."
            mike.say "But I could probably go for a beat-em-up, Jack."
            "Kat can't help frowning as he hears what I have to say."
            "Though it's pretty predictable that Jack seems delighted."
            kat.say "You guys are nuts!"
            kat.say "But don't worry about me."
            kat.say "I'll go have fun on my own."
            "With that, she walks off to find the game she wants to play."
            "Which leaves Jack and me to go find his choice of game."
            jack.say "Come on, dude…"
            jack.say "You're gonna love this, I promise!"
            "By the time we're done and we meet up again, I feel like I have arthritic wrists."
            "Kat and Jack seem to be pleased at getting to play the games they wanted too."
            "But I do note that everyone's talking about their own private fun."
            "Rather than anything that we've done as a threesome."
            $ jack_score += 1
        "Suggest 'Whack-A-Gopher'":
            "Everyone seems to be intent on getting their own way here."
            "And none of them seem to be willing to back down either."
            "But maybe there's another choice of game in the arcade?"
            "One that's totally different to our choices, but still fun."
            "I cast my eyes around the arcade, and then I see the perfect thing."
            mike.say "Hey, guys..."
            mike.say "When was the last time you played 'Whack-A-Gopher'?"
            "I point over at the game where the plastic gophers are popping up from their holes."
            "And I can see that the moment I do, Kat and Jack can't help staring in the same direction."
            show kat happy
            kat.say "Geez..."
            show kat talkative
            kat.say "I haven't played that since I was a kid!"
            show kat smile
            show jack smile
            jack.say "Me neither..."
            jack.say "And I used to be the absolute best at it too!"
            show jack normal
            "I can't help frowning as Jack recounts his former glories."
            mike.say "Since when?!?"
            mike.say "I played it with you when we were kids, Jack."
            mike.say "You were always the worst at it!"
            show jack surprised
            jack.say "Lies, all lies!"
            show jack normal
            show kat talkative
            kat.say "If that's so, then prove it..."
            kat.say "Put your money where your mouth is!"
            show kat defiant
            "Jack nods, looking determined to defend his honour."
            "And with that in mind, he strides over to the game."
            "Then he snatches up one of the padded mallets."
            "And just like that, we're on!"
            "Kat, Jack and I battle it out to the bitter end."
            "We hammer away at the gophers until we're exhausted."
            "But the off thing is that afterwards, nobody seems to remember who scored what."
            "Instead we're all too busy laughing and joking about the whole experience."
            $ jack_score += 1
            $ kat_score += 1
    with fade
    "Walking away from the game, I suddenly remember something."
    mike.say "Shit..."
    mike.say "The tickets!"
    "Before Kat and Jack can ask me what's going on, I'm already running back."
    "And once I make it to the machine, I snatch up the string of tickets hanging out of the front."
    "Then I walk back to where the others are waiting, feeling an immense sense of relief."
    show jack smile
    jack.say "Oh yeah..."
    jack.say "The tickets!"
    show jack normal
    "As soon as she sees them, Kat seems to understand their significance."
    show kat talkative
    kat.say "I get it now..."
    kat.say "We trade those in for prizes, right?"
    show kat smile
    "I nod as I tear up the tickets, dividing them three ways."
    "Then I hand an equal share to Kat and Jack, keeping one for myself."
    "At the same time feeling glad that we won enough to keep the shares even."
    mike.say "You got it, Kat..."
    mike.say "Let's go and see what we can get!"
    "Together we hurry to the counter where the tickets can be exchanged."
    "But it soon becomes apparent that anything worth having costs a lot of tickets."
    mike.say "Ouch!"
    mike.say "Looks like all I can afford is one of those erasers."
    mike.say "The one's shaped like a novelty turd."
    "Kat and Jack are both still scanning the shelves behind the counter."
    "Evidently they're giving it more thought than me."
    show jack smile
    jack.say "I'm liking that plushie there..."
    jack.say "The one that looks like it's a dugong?"
    show jack normal
    show kat talkative
    kat.say "I want a plushie too..."
    kat.say "But I like the octopus!"
    show kat smile
    "I chuckle and shake my head as I look at the price of the plushies."
    mike.say "Dream on, guys..."
    mike.say "Those are like, what..."
    mike.say "Twice the amount of tickets we have each?"
    "Even as I say this, I can see Kat and Jack both staring at me intently."
    "And then I see their eyes travel down to the tickets clutched in my hand."
    mike.say "Oh, no way!"
    mike.say "You can't be serious?!?"
    "What did I do to deserve this?"
    "Both of them want me to throw my tickets in to get the prize they're after."
    "But I only have enough to afford one plushie!"
    $ renpy.dynamic(rand_choice=randint(1, 3))
    if rand_choice == 3:

        "But I know that it's going to fall to me to sort this out."
        "Because that's the way these things always seem to go."
        menu:
            "Get the eraser":
                "I kind of feel pissed off that the two of them want my tickets."
                "And that makes me want to use them for myself just to make a point."
                "Even if it does mean getting something that's totally crap."
                "And in this case, I do mean crap!"
                mike.say "Nah..."
                mike.say "I really want one of those erasers."
                mike.say "Bree and Sasha will totally freak if I leave it out on the kitchen counter!"
                "I can see that Kat and Jack want to argue with me."
                "But there's really nothing they can say to change my mind."
                "Not without making it totally obvious that they have designs on my tickets."
                show kat whining
                kat.say "Ah, yeah..."
                kat.say "I might get one of those too."
                show kat sadsmile
                show jack whining
                jack.say "They sound like a total riot."
                show jack sadsmile
                "I step up and hand over my tickets, then take my eraser."
                "Jack and Kat follow my lead a moment later."
                "And we leave the arcade with three totally shitty prizes."
                "But I feel like I managed to make a point all the same."
                $ jack_score -= 1
                $ kat_score -= 1
            "Get the dugong":
                "I kind of feel pissed off that the two of them want my tickets."
                "And that makes me want to use them for myself just to make a point."
                "But that dugong does look totally sweet."
                "And who knows, if I give Jack my tickets, maybe he'll let me borrow it?"
                mike.say "You should have my tickets, Jack."
                mike.say "Because I know how much you love dugongs!"
                show jack blush
                "Jack blushes a little and waves away my comments."
                show jack smile
                jack.say "Ah, they're just so chubby and cute..."
                jack.say "I can't resist them!"
                show jack normal
                "I hand over the tickets and Jack hurries off to claim his plushie."
                "Which leaves Kat with the smaller share of the tickets for herself."
                show kat annoyed
                kat.say "Ah, yeah..."
                kat.say "I'll just get myself one of those novelty erasers then."
                show kat sad
                "We leave the arcade with Jack beaming happily."
                "But also with Kat looking annoyed at her shitty prize."
                "So I guess the moral of the story is that you can't please everyone."
                $ jack_score += 1
                $ kat_score -= 1
            "Get the octopus":
                "I kind of feel pissed off that the two of them want my tickets."
                "And that makes me want to use them for myself just to make a point."
                "But that octopus does look totally sweet."
                "And who knows, if I give Kat my tickets, maybe she'll let me borrow it?"
                mike.say "You should have my tickets, Kat."
                mike.say "Because I know how much you love octopi!"
                show kat blush
                "Kat blushes a little and waves away my comments."
                show kat talkative
                kat.say "Ah, they're just so slippery and slimy..."
                kat.say "I love to imagine them crushing people with their mighty tentacles!"
                show kat smile
                "I hand over the tickets and Kat hurries off to claim her plushie."
                show jack blank
                "Which leaves jack with the smaller share of the tickets for himself."
                show jack whining
                jack.say "Ah, yeah..."
                jack.say "I'll just get myself one of those novelty erasers then."
                show jack sad
                "We leave the arcade with Kat beaming happily."
                "But also with Jack looking annoyed at his shitty prize."
                "So I guess the moral of the story is that you can't please everyone."
                $ jack_score -= 1
                $ kat_score += 1
            "Suggest we pool our tickets and get something bigger":
                "I kind of feel pissed off that the two of them want my tickets."
                "And that makes me want to use them for myself just to make a point."
                "But then I see some of the larger plushies on the next shelf up."
                mike.say "Wait a minute..."
                mike.say "If we pool all of our tickets..."
                mike.say "I think we can afford one of those bigger plushies!"
                "Kat and Jack follow my pointing finger."
                "And it doesn't take long for them to see I'm right."
                show kat talkative
                kat.say "He's right..."
                kat.say "We could totally get that big, vicious dog!"
                show kat smile
                show jack smile
                jack.say "Oh man..."
                jack.say "It reminds me of one that bit me as a kid..."
                jack.say "I still have the scar!"
                show jack normal
                "With everyone on board, I walk up to the counter."
                "Then I exchange all of the tickets we have for the plushie they want."
                "And that done, we walk out of the arcade with everyone happy."
                "Kat and Jack because they have a plushie to share."
                "And me because we all managed to get onto the same page for once."
                $ jack_score += 1
                $ kat_score += 1
    elif rand_choice == 2:

        "I feel the sudden spark of inspiration as I think about the problem."
        "And I know that I have the perfect solution to the problem of the tickets."
        mike.say "Leave this to me, guys..."
        mike.say "I know how to get more tickets."
        mike.say "Just let me play a couple more games."
        mike.say "I'll win us all the tickets we need."
        show kat stuned
        show jack surprised
        "Kat and Jack look at me in surprise."
        show kat whining
        kat.say "Are you sure about this, [hero.name]?"
        kat.say "We all got pretty exhausted playing that last game."
        show kat sad
        show jack whining
        jack.say "I know I couldn't play another one."
        jack.say "I'm totally spent!"
        show jack sadsmile
        "By the time they've said their piece, we're back amongst the arcade machines."
        "And I'm headed straight for the 'Whack-A-Gopher' game."
        "I pick up the padded hammer and slide a coin into the slot."
        "And I'm sure to give the guys a cocky glance as I get myself ready."
        mike.say "Watch and learn, guys!"
        if hero.stamina:

            "I start out playing the game pretty well."
            "I'm hammering away merrily, getting a decent score."
            "But pretty soon I can feel fatigue begin to set in."
            "The hammer seems to get heavier by the second."
            "And that's when I feel the extra dose of stamina kick in."
            "With it I feel like I can push on through the wall of fatigue."
            "Battering the gophers with renewed speed a vigour."
            show kat smile
            show jack normal
            with fade
            "By the time I've spent my last quarter, I'm sweating profusely."
            "But it was well worth the effort, because I have the tickets we need."
            "I hold them up for everyone to see."
            "And then I motion for Kat and Jack to follow me."
            mike.say "Come on, guys..."
            mike.say "We've got a dugong and octopus to grab!"
            "Kat and Jack still seem a little amazed that I managed to pull it off."
            "So much so that they hang back while I go up to the counter alone."
            "It's almost like they think I'm going to keel over any moment."
            "But of course nothing of the kind happens."
            "Instead I return to them and hand over the plushies."
            $ jack_score += 1
            $ kat_score += 1
        else:

            "I start out playing the game pretty well."
            "I'm hammering away merrily, getting a decent score."
            "But pretty soon I can feel fatigue begin to set in."
            "The hammer seems to get heavier by the second."
            "Soon enough I'm missing more of the gophers than I'm hitting."
            "And by the time I've spent my last quarter, I'm sweating profusely."
            "But it's all in vain, because I haven't won nearly enough tickets."
            show kat sad
            show jack sad
            with fade
            "The walk back to the counter is pretty quiet."
            "And once we get there, I at least try to put on a brave face."
            mike.say "I suppose one of those erasers isn't so bad."
            mike.say "Bree and Sasha will totally freak if I leave it out on the kitchen counter!"
            "I can see that Kat and Jack want to argue with me."
            "But there's really no point, as we can't afford anything else."
            show kat whining
            kat.say "Ah, yeah..."
            kat.say "I might get one of those too."
            show kat sadsmile
            show jack lying
            jack.say "They sound like a total riot."
            show jack sadsmile
            "I step up and hand over my tickets, then take my eraser."
            "Jack and Kat follow my lead a moment later."
            "And we leave the arcade with three totally shitty prizes."
            $ jack_score -= 1
            $ kat_score -= 1
    else:

        "I feel the sudden spark of inspiration as I think about the problem."
        "And I know that I have the perfect solution to the problem of the tickets."
        mike.say "Leave this to me, guys..."
        mike.say "I know how to get more tickets."
        mike.say "And we won't have to pay for them either!"
        "Kat and Jack look at me with genuine interest."
        "And I give them a knowing smile in return."
        hide jack
        hide kat
        with fade
        "Then I creep back towards the arcade machines."
        "Trying to look nonchalant, I look for any that dispense tickets."
        "More specifically any where the people playing them have forgotten to collect theirs."
        if hero.has_skill("sneaky"):

            "I keep a close eye on the most likely targets."
            "But at the same time I make sure to act innocent."
            "And I also make sure that I keep just out of sight too."
            "Most of the time I find tickets that have just been forgotten."
            "But more than once I manage to lean in as someone's looking the other way."
            "I can almost hear Kat and Jack taking a deep breath and holding it."
            "Then as soon as I snatch the tickets, they let them out again."
            "The relief is written all over their faces as I return a moment later."
            "And a quick count proves that I've managed to acquire more than enough tickets."
            mike.say "Come on, guys..."
            mike.say "We've got a dugong and octopus to grab!"
            "Kat and Jack still seem a little nervous about the source of the tickets."
            "So much so that they hang back while I go up to the counter alone."
            "It's almost like they think someone will know that the tickets were stolen."
            "But of course nothing of the kind happens."
            "Instead I return to them and hand over the plushies."
            "And as we walk out of the arcade, their moods soon begin to improve."
            $ jack_score += 1
            $ kat_score += 1
        else:

            "I can see a few tickets hanging out of machines here and there."
            "But the real prize in this game is the ones where someone's still playing."
            "And soon enough I think that I see a likely target."
            "A guy playing one of the machines looks to be pretty distracted."
            "So I waste no time in sidling up to him, and then leaning in."
            "I reach out for the tickets, intending to snatch them quickly."
            "But to my horror, I feel my fingers close on his hand, rather than the tickets!"
            show shawn zorder 2 at center, zoomAt (2.5, (640, 1640)), blacker with hpunch
            "Quick as a flash, the guy clamps his hand on mine and turns to face me."
            "Random guy" "Hey!"
            "Random guy" "What the hell are you..."


            pause 0.3
            show kat casual confused zorder 1 at center, zoomAt(1.25, (740, 880)) with vpunch
            "Random guy" "Urgh..."
            "For a moment I can't tell what just happened."
            hide shawn with easeoutbottom
            "But then the guy starts to crumple in front of me."
            "And as he collapses to the floor, I see Kat standing behind him."
            "The position from which she must have been able to kick him in the balls!"
            show kat offended
            kat.say "What are you waiting for?"
            kat.say "Run!"
            hide kat with easeoutright
            "Kat, Jack and I all turn and dash for the exit."
            "And once out of the arcade, we keep on running into the mall."
            "No one stops or looks back until we're well away."
            "Then we do the best we can to slow down and act natural."
            $ jack_score -= 1
            $ kat_score -= 1
    scene bg mall1 with fade
    show jack casual at center, zoomAt(1.25, (440, 920))
    show kat casual smile at center, zoomAt(1.25, (840, 880))
    with easeinleft
    "Strolling around the mall I get the feeling that the date is coming to an end."
    "I can't put my finger on exactly what makes me think that, I can just sense it."
    "Everyone seems a little tired and ready to slow things down, a little subdued maybe."
    "So I decide that it's a good time to put the inevitable question to them."
    mike.say "So..."
    mike.say "Are you guys ready to call it a day?"
    mike.say "Or maybe you want to go do something else?"

    if all(score >= 2 for score in (jack_score, kat_score)):
        "Jack and Kat seem to response pretty quickly."
        "And what they say kind of catches me off-guard."
        show kat whining
        kat.say "Call it a day?"
        kat.say "No way, [hero.name]!"
        show kat smile
        show jack whining
        jack.say "I'm not ready to quit yet!"
        jack.say "Surely we can keep hanging-out a little longer?"
        show jack sadsmile
        mike.say "Oh yeah..."
        mike.say "That sounds great!"
        "Kat, Jack and I begin walking together."
        "We're not going in any particular direction."
        "Rather we're walking as we discuss what to do next."
        "And I guess this means that the date was a success."
        "Because neither of them seems to want it to end just yet."
        $ kat.love += 2
        call jack_kat_special_sex from _call_jack_kat_special_sex

    elif kat_score >= 2:
        "Jack and Kat seem to response pretty quickly."
        "But they both seem as amazed as I am to hear what the other has to say."
        show kat whining
        kat.say "Call it a day?"
        kat.say "No way, [hero.name]!"
        show kat smile
        show jack whining
        jack.say "I'm totally exhausted!"
        jack.say "And I seriously need to get some me time."
        show jack sad
        "I shrug as I walk over to Kat and put an arm around her shoulder."
        mike.say "If that's how you feel, Jack..."
        mike.say "Then I guess it's just Kat and me from this point on!"
        hide jack with easeoutright
        "With that, Jack walks off to get the rest he seems to need so badly."
        "Which leaves Kat and I to decide what we want to do next."
        "And I suppose that means the date was kind of a success."
        "At least fifty percent a success anyway."
        $ kat.love += 1

    elif jack_score >= 2:
        "Jack and Kat seem to response pretty quickly."
        "But they both seem as amazed as I am to hear what the other has to say."
        show kat whining
        kat.say "I don't know about you two..."
        kat.say "But I'm feeling pretty worn out."
        show kat sad
        show jack whining
        jack.say "I'm not ready to quit yet!"
        show jack smile
        jack.say "Surely we can keep hanging-out a little longer?"
        show jack sadsmile
        "I shrug as I walk over to Jack and give him a high-five."
        mike.say "If that's how you feel, Kat..."
        mike.say "Then I guess it's just Jack and me from this point on!"
        show jack smile
        jack.say "Yeah, just like old times!"
        show jack sadsmile
        hide kat with easeoutleft
        "With that, Kat walks off to get the rest she seems to need so badly."
        "Which leaves Jack and I to decide what we want to do next."
        "And I suppose that means the date was kind of a success."
        "At least fifty percent a success anyway."
        $ kat.love -= 1
    else:

        "Jack and Kat seem to response pretty quickly."
        "But I can tell from the looks on their faces it's not good news."
        show kat whining
        kat.say "I don't know about you two..."
        kat.say "But I'm feeling pretty worn out."
        show kat sad
        show jack whining
        jack.say "I'm totally exhausted!"
        jack.say "And I seriously need to get some me time."
        show jack sadsmile
        mike.say "Oh..."
        mike.say "Oh yeah..."
        mike.say "Me too."
        "With that we all say our goodbyes."
        hide kat with easeoutleft
        hide jack with easeoutright
        "And then we go our separate ways."
        "But I can't help wondering if I did enough to make the date a success."
        "Though I guess only time will tell whether I pulled it off or not."
        $ kat.love -= 2
    return

label jack_kat_special_sex:
    scene bg house
    show jack casual at center, zoomAt(1.25, (440, 920))
    show kat casual smile at center, zoomAt(1.25, (840, 880))
    with fade
    "It's still earlier than I would have hoped when Kat, Jack and I make it back to my place."
    "We decided to come here because it's a shorter hop from the mall than Kat's apartment."
    "And none of us want to brave Jack's place, as he still lives in his mom's basement!"
    "But the only problem is that this is kind of a spur of the moment thing."
    "Which means I haven't been able to ensure that the coast will be clear on our arrival."
    "As soon as we find ourselves on the porch, I turn to address Kat and Jack."
    mike.say "Okay, guys..."
    mike.say "Here's the drill..."
    mike.say "I open the door, and then we run straight to my bedroom, okay?"
    "This earns me a couple of wry stares from the others."
    show kat talkative
    kat.say "What's the rush, [hero.name]?"
    kat.say "Are you that desperate for some action?"
    show kat smile
    show jack happy at startle
    "Jack chuckles as he hears Kat's questions."
    "And then he weighs in with some of his own."
    show jack smile
    jack.say "She's right, dude..."
    jack.say "Are you worried Bree and Sasha are gonna see us?"
    show jack normal
    show kat talkative
    kat.say "You mean his housemates?"
    show kat smile
    show jack smile
    jack.say "Oh yeah, Kat..."
    jack.say "They're super hot!"
    show jack normal
    "Jack suddenly seems to remember who he's talking to."
    "And he starts to backpedal furiously."
    show jack whining
    jack.say "But..."
    jack.say "But obviously not as hot as you, Kat!"
    show jack normal
    "I cross my arms and give Jack a hard stare."
    mike.say "You really want to run into them, Jack?"
    mike.say "And end up getting the ninth degree, huh?"
    mike.say "They'll want to know exactly what we're up to."
    mike.say "Then every noise you make, you'll be sure they're listening to you!"
    "Jack's eyes go wide as I describe the scenario."
    "And then he starts nodding in agreement."
    show jack smile
    jack.say "Oh yeah..."
    jack.say "Maybe you're right!"
    show jack normal
    mike.say "You know I am!"
    hide kat
    hide jack
    with easeoutleft
    "Without wasting any more time, I unlock the door and usher them inside."
    scene bg livingroom with fade
    "Then I follow on their heels, quickly locking it behind us."
    "Moments later I'm leading them straight to my room."
    "And it's all I can do not to hold my breath until we get there."
    scene bg bedroom1 with fade
    "Glancing over my shoulder, I open the bedroom door."
    show jack casual at center, zoomAt(1.25, (840, 920))
    show kat casual smile at center, zoomAt(1.25, (440, 880))
    with easeinright
    "Kat and Jack dart inside, and I slip in after them."
    "But only when the door is closed do I allow myself to relax."
    mike.say "Phew..."
    mike.say "At least now we can relax!"
    "Even as I'm saying this, I feel Jack's hand on my shoulder."
    "He's shaking me, as if he wants me to look at something."
    show jack lying
    jack.say "Erm..."
    jack.say "I don't know about that, man!"
    show jack normal
    "Looking in the same direction as Jack, I see what he's talking about."
    "Kat hasn't waited for any further instruction from me."
    "Instead she's already over by the bed, making herself comfortable."
    show kat naked with dissolve
    "And by that I mean she's in the act of removing her clothes!"
    "For a moment Kat has her back to us as we watch her."
    "But then she seems to sense our eyes wandering all over her body."
    "Because she turns around, already waving for us to join her."
    show kat talkative
    kat.say "Hey..."
    kat.say "This isn't a one-woman strip show!"
    kat.say "Get over here and get naked, before I change my mind!"
    show kat smile
    "The threat of losing out on some action is more than enough to motivate us."
    show jack naked with dissolve
    "And it sends Jack and me hurrying across the room, already tugging at our clothes."
    "We're at best half-naked by the time we reach Kat, which she seems to find hilarious."
    scene bg black
    show katjack foreplay open
    with fade
    "She sits down on the bed, watching the show as we take off the last few items."
    "And once we're all finally naked, she's smiling in anticipation."
    show katjack foreplay closed
    "But one thing I notice is that Kat's looking at me, rather than Jack."
    show katjack foreplay open pleasure
    "I think she's waiting for me to give her the nod as to what happens next."
    menu:
        "Blow-job":
            "I take a step forwards and reach out to grab Kat's hands."
            "Then I pull her to her feet and turn around so that we swap places."
            "Beckoning for Jack to join me, I sit down on the edge of the bed."
            "He seems confused at first, not sure what's going on."
            scene bg black
            show katjack bj
            with fade
            "But when Kat gets down on her knees in front of me, he soon catches on!"
            jack.say "Oh..."
            jack.say "Oh right, I get it!"
            "Jack dashes to the side of the bed and sits down a beside me."
            "And it's all I can do to keep him from pushing me over sideways!"
            "He seems eager for things to get going."
            "Though I see Kat's still holding my eye."
            show katjack bj righthand_forth lefthand_forth
            pause 0.2
            show katjack bj righthand_back lefthand_back at stepback(speed=0.05, h=10, v=0)
            "Looks like she's waiting to see who gets her attentions."
            menu:
                "Gesture for Kat to suck you":
                    "I'm still kind of high on the idea that Kat's waiting for my directions."
                    "And I know that it's kind of a selfish thing of me to do knowing that."
                    "But I can't keep myself from nodding down in the direction of my own cock."
                    "Kat follows my gaze, soon seeing the fact that I'm already getting excited."
                    "I watch as she lowers her head towards it, feeling the sense of anticipation rise."
                    "Stealing a glance to my side, I try to see what Jack's doing right now."
                    "And much to my relief, I notice that he's staring down too."
                    "It seems that he's far too engrossed in the act of watching to object."
                    "Which at least helps to make me feel a little better about my decision."
                    "But when I look back down myself, I see that Kat's looking up at me."
                    "She raises her eyebrows, as if making sure my attention's one hundred percent on her."
                    "Only when she sees that's the case does she turn her eyes back down again."
                    "And the moment she does so, I feel instantly rewarded."
                    show katjack bj suckmike
                    "Because the sensation of those lips closing around my cock is impossible to describe."
                    "I'd keep on watching what Kat's doing down there, but it just feels too good."
                    "Instead I feel my eyes half closing as her head begins to bob up and down."
                    show katjack bj righthand_forth
                    pause 0.2
                    show katjack bj righthand_back at stepback(speed=0.05, h=10, v=0)
                    "In fact the effects are so intense that pretty soon I have to hold myself up."
                    "From that point on I have to fight to keep my eyes open so I can watch."
                    "Kat's using her mouth so well that I can almost feel myself drifting off."
                    show katjack bj righthand_forth
                    pause 0.2
                    show katjack bj righthand_back at stepback(speed=0.05, h=10, v=0)
                    "And by the time she takes me deeper into her throat, I'm totally in her power."
                    "Kat seems to have so much control over me that I suspect she could end it whenever she wants."
                    "Or else she'd be able to keep me hanging on until I had nothing at all left in the tank."
                    "Which is why I'm so surprised when I see Kat looking up at me again."
                    show katjack bj righthand_forth
                    pause 0.2
                    show katjack bj righthand_back at stepback(speed=0.05, h=10, v=0)
                    "Is she..."
                    "She really is!"
                    "Kat's giving me a chance to let her know how I want this to end!"
                    menu:
                        "Let her swallow":
                            "Quick as I can, I wave my hand downwards."
                            "Kat nods, and then I see her close her eyes."
                            "The moment that she picks up speed, I know she got my meaning."
                            with hpunch
                            "She's taking me ever deeper, pushing me harder."
                            show katjack bj suckmike mikecum with hpunch
                            "And when I finally shoot my load, she swallows it right down."
                            with hpunch
                            "Not even letting the twitching and jerking of my orgasm get in her way."
                        "Go to facial":
                            "Quick as I can, I wave my hand upwards."
                            "Kat nods, and then I see her close her eyes."
                            "The moment that she pulls her head back, I know she got my meaning."
                            show katjack bj -suckmike
                            "Kat lets my cock slide smoothly out of her mouth then bob before her face."
                            show katjack bj mikecum with hpunch
                            "And when I finally shoot my load, she doesn't move as much as an inch."
                            show katjack bj -mikecum facecum with hpunch
                            "Not even when it spatters across her cheeks and nose."
                "Gestures for Kat to suck Jack":
                    "I'm still kind of high on the idea that Kat's waiting for my directions."
                    "But it'd be selfish of me to use that in order to keep Jack out of things."
                    "So with a heavy heart, I nod my head towards Jack's cock instead of mine."
                    "Kat follows my gaze, soon seeing the fact that Jack's already getting excited."
                    "I watch as she lowers her head towards it, seeing his sense of anticipation rise."
                    "And a quick glance at Jack's face tells me that he's totally into what's happening too."
                    "Which at least helps to make me feel a little better about my decision."
                    "But when I look back down myself, I see that Kat's looking up at me."
                    "She raises her eyebrows, as if making sure my attention's one hundred percent on her."
                    "Only when she sees that's the case does she turn her eyes back down again."
                    "And the moment she does so, Jack starts to moan and gasp."
                    show katjack bj suckjack
                    "Because the sensation of those lips closing around his cock must be impossible to describe."
                    "I keep on watching what Kat's doing down there, because I can't tear my eyes away."
                    "And I feel my eyes bulge as her head begins to bob up and down."
                    show katjack bj lefthand_forth
                    pause 0.2
                    show katjack bj lefthand_back at stepback(speed=0.05, h=-10, v=0)
                    "In fact the effects are so intense that pretty soon Jack has to hold himself up."
                    "From that point on I couldn't tear my eyes away even if I wanted to."
                    "Kat's using her mouth so well that I can almost feel it myself."
                    show katjack bj lefthand_forth
                    pause 0.2
                    show katjack bj lefthand_back at stepback(speed=0.05, h=-10, v=0)
                    "And by the time she takes Jack deeper into her throat, I'm totally enthralled."
                    "Kat seems to have so much control over Jack that I suspect she could end it whenever she wants."
                    "Or else she'd be able to keep him hanging on until he had nothing at all left in the tank."
                    show katjack bj lefthand_forth
                    pause 0.2
                    show katjack bj lefthand_back at stepback(speed=0.05, h=-10, v=0)
                    "Which is why I'm so surprised when I see Kat looking up at me again."
                    "Is she..."
                    "She really is!"
                    show katjack bj lefthand_forth
                    pause 0.2
                    show katjack bj lefthand_back at stepback(speed=0.05, h=-10, v=0)
                    "Kat's giving me a chance to let her know how I want this to end!"
                    menu:
                        "Let her swallow":
                            "Quick as I can, I wave my hand downwards."
                            "Kat nods, and then I see her close her eyes."
                            "The moment that she picks up speed, I know she got my meaning."
                            with hpunch
                            "She's taking Jack ever deeper, pushing him harder."
                            show katjack bj suckjack jackcum with hpunch
                            "And when he finally shoots his load, she swallows it right down."
                            with hpunch
                            "Not even letting the twitching and jerking of his orgasm get in her way."
                        "Go to facial":
                            "Quick as I can, I wave my hand upwards."
                            "Kat nods, and then I see her close her eyes."
                            "The moment that she pulls her head back, I know she got my meaning."
                            show katjack bj -suckjack
                            "Kat lets Jack's cock slide smoothly out of her mouth then bob before her face."
                            show katjack bj jackcum with hpunch
                            "And when he finally shoots his load, she doesn't move as much as an inch."
                            show katjack bj -jackcum facecum with hpunch
                            "Not even when it spatters across her cheeks and nose."
                "Gesture for Kat to suck them both":
                    "I'm still kind of high on the idea that Kat's waiting for my directions."
                    "But it'd be selfish of me to use that in order to keep Jack out of things."
                    "So I nod my head first towards Jack, and Kat instantly begins to move towards him."
                    "Then I nod back towards myself a moment later, and thankfully she seems to understand."
                    "Turning my eyes over to where Jack's lying again, I make it clear she should start there."
                    "Kat follows my gaze, soon seeing the fact that Jack's already getting excited."
                    "I watch as she lowers her head towards it, seeing his sense of anticipation rise."
                    "And a quick glance at Jack's face tells me that he's totally into what's happening too."
                    "But when I look at her face again, I see that Kat's looking up at me."
                    "She raises her eyebrows, as if making sure my attention's one hundred percent on her."
                    "Only when she sees that's the case does she turn her eyes back down again."
                    show katjack bj suckjack
                    "And the moment she does so, Jack starts to moan and gasp."
                    "Because the sensation of those lips closing around his cock must be impossible to describe."
                    show katjack bj lefthand_forth
                    pause 0.2
                    show katjack bj lefthand_back at stepback(speed=0.05, h=10, v=0)
                    "I keep on watching what Kat's doing down there, because I can't tear my eyes away."
                    "And I feel my eyes bulge as her head begins to bob up and down."
                    show katjack bj lefthand_forth
                    pause 0.2
                    show katjack bj lefthand_back at stepback(speed=0.05, h=10, v=0)
                    "In fact the effects are so intense that pretty soon Jack has to hold himself up."
                    "From that point on I couldn't tear my eyes away even if I wanted to."
                    show katjack bj lefthand_forth
                    pause 0.2
                    show katjack bj lefthand_back at stepback(speed=0.05, h=10, v=0)
                    "Kat's using her mouth so well that I can almost feel it myself."
                    "And by the time she takes Jack deeper into her throat, I'm totally enthralled."
                    show katjack bj normal
                    "Which means I'm totally taken by surprise when Kat releases him a moment later."
                    "She all but pounces on me while I'm out of it too."
                    show katjack bj suckmike
                    "And just like that, I'm the one getting all of her oral ministrations."
                    "Now I know just what Jack was feeling as I watched him before."
                    show katjack bj lefthand_forth
                    pause 0.2
                    show katjack bj lefthand_back at stepback(speed=0.05, h=10, v=0)
                    "Because Kat's treating me to the same thorough going over."
                    "I can imagine that the roles must be reversed between us."
                    "That now Jack's the one sitting back and watching me be taken to a higher plane."
                    show katjack bj lefthand_forth
                    pause 0.2
                    show katjack bj lefthand_back at stepback(speed=0.05, h=10, v=0)
                    "But there's no way I can check to see if I'm right."
                    "Because my eyes are tight shut, cutting off the rest of my senses."
                    "The sensations of what Kat's doing to me are just too intense and overwhelming."
                    show katjack bj lefthand_forth
                    pause 0.2
                    show katjack bj lefthand_back at stepback(speed=0.05, h=10, v=0)
                    "All I can do is give myself over to the experience, letting it wash over me."
                    "The only problem is that Kat's so good at what she's doing."
                    "Which means I can't even hope to hold on much longer."
                    show katjack bj lefthand_forth
                    pause 0.2
                    show katjack bj lefthand_back at stepback(speed=0.05, h=10, v=0)
                    "My eyes pop open just in time to see Kat let me slide out of her mouth."
                    show katjack bj normal
                    "And it's only now that I notice Kat's been keeping Jack in the loop too."
                    "She's working him with one hand, even as she now releases me."
                    "Kat leans back, letting both cocks bob in front of her face."
                    show katjack bj jackcum mikecum mikecum with hpunch
                    "And somehow she manages to time things perfectly so we both cum at once."
                    show katjack bj -jackcum -mikecum facecum with hpunch
                    "She doesn't move an inch as she's hit from two different angles."
                    "Not even when it spatters over most of her face, covering it in sticky, white lines."
        "Fuck Kat":
            "If Kat's basically putting all of the power in my hands, then I'm going to take it."
            "And I'm also going to be sure to use it to reward myself for all of my hard work."
            "Because if it wasn't for me, we wouldn't be here in the first place, would we?"
            "So I waste no time in stepping up and leaning over the bed."
            "At the same time I reach out and put my hands on Kat's thighs."
            "Then I part her legs, lifting the right one higher than the left."
            scene bg black
            show katjack mikefuck
            with fade
            "This means that she has to lean backwards onto the mattress."
            show katjack mikefuck mike
            "But it also means that her legs are parted, allowing me to get between them."
            "And it's safe to say that I'm more than ready to get down to business."
            "I can see that Kat's nodding eagerly as she looks up at me."
            "Letting me know that she's totally on-board with what I'm doing."
            "She makes this even more plain a moment later when she reaches down."
            menu:
                "Fuck pussy":
                    "And I feel her take hold of my cock, guiding it home as she does so."
                    "Kat presses the head hard against the lips of her pussy."
                    show katjack mikefuck mike vaginal surprised with hpunch
                    "Almost like she hopes to be able to push me straight inside of her."
                    "But as much as she seems to want it, her body still puts up a token resistance."
                    show katjack mikefuck surprised
                    kat.say "Mmm..."
                    kat.say "Please..."
                    kat.say "I want it so bad!"
                    show katjack mikefuck normal
                    "There's really no need for Kat to explain herself to me right now."
                    "Because I'm on totally the same wavelength that she is."
                    "And I was determined to make it happen even before she spoke up."
                    "All her desperate pleas do is make me more determined to succeed."
                    show katjack mikefuck mike normal at stepback(speed=0.1, h=-10, v=0)
                    "With her holding me in place, I begin to move back and forth."
                    "This draws the head of my cock up and down the length of her pussy."
                    "And every pass that I make sees Kat gasp and moan all the more."
                    show katjack mikefuck at stepback(speed=0.1, h=-10, v=0)
                    "Each time I repeat the move, I feel her weaken just a little."
                    "And each time I almost hold my breath, hoping for a breakthrough."
                    "It happens again and again, making me go through the motions almost without thinking."
                    show katjack mikefuck at stepback(speed=0.1, h=-10, v=0)
                    "So when it actually does happen, I'm caught off-guard."
                    show katjack mikefuck mike surprised with hpunch
                    "All of a sudden I feel Kat's muscles surrender, and I sink into her."
                    "Both of us gasp, momentarily stunned by the unexpected sensation."
                    "But it only takes a second for us to recover."
                    show katjack mikefuck normal at stepback(speed=0.1, h=-10, v=0)
                    "And once we do, I start thrusting in and out of Kat in earnest."
                    "Likewise she comes back to life too, throwing back her head and holding on for dear life."
                    "Which is just as well, because I'm not holding anything back this time."
                    show katjack mikefuck at stepback(speed=0.1, h=-10, v=0)
                    "I throw all that I have into the effort of pounding away at Kat."
                    "And for a moment it looks like she won't be able to hold on at all."
                    "But then I see her eyes settle on something else."
                    show katjack mikefuck at stepback(speed=0.1, h=-10, v=0)
                    "Her hand darts out, grabbing hold of what I realise is Jack's cock!"
                    show katjack mikefuck mike jack lick with hpunch
                    "Then she pulls it towards herself, wrapping her lips around the head."
                    show katjack mikefuck at stepback(speed=0.1, h=-10, v=0)
                    "Of course Jack doesn't object at all, just going along with it."
                    "And that leaves me to tear my eyes away and focus on the task at hand."
                    show katjack mikefuck at stepback(speed=0.1, h=-10, v=0)
                    "Without any further distractions, I use the very last of my energy."
                    "It powers me on to the very end, until the moment I feel myself start to lose it."
                    show katjack mikefuck at stepback(speed=0.1, h=-10, v=0)
                    "And with Kat otherwise engaged, I can end things exactly how I choose too!"
                    menu:
                        "Cum inside pussy":
                            "Still feeling the need to indulge myself, I push on to the end."
                            show katjack mikefuck xray with hpunch
                            "And when I finally come, I do so as deep inside Kat as I possibly can."
                            show katjack mikefuck mikecum with hpunch
                            "Helpless and unable to escape, she takes everything that I have to give."
                            show katjack mikefuck ahegao open with hpunch
                            "Lying there until I'm totally spent, and her pussy is overflowing."
                        "Pull out of pussy":
                            "Wanting to make a point, even to mark my territory, I make to pull out."
                            "Helpless and unable to move, Kat can do nothing to stop me."
                            with hpunch
                            "She lies there, still writhing with pleasure as I slide free."
                            show katjack mikefuck out mikecum with hpunch
                            "And then I shoot my load over her belly and thighs."
                "Fuck ass":
                    "And I feel her take hold of my cock, guiding it home as she does so."
                    "Kat presses the head hard against the lips of her pussy."
                    "Almost like she hopes to be able to push me straight inside of her."
                    "But I have other ideas, and I lift her up a little more."
                    "At the same time I make a fresh effort to push forwards."
                    show katjack mikefuck mike anal surprised with hpunch
                    "And the result is that my cock slides between the cheeks of her ass instead."
                    show katjack mikefuck surprised
                    kat.say "Wha..."
                    kat.say "What are you..."
                    kat.say "Oh, you naughty boy!"
                    show katjack mikefuck normal
                    "I'm quietly relieved to realise Kat's open to the idea."
                    "That she's totally on the same wavelength as."
                    "I was determined to make it happen even before she spoke up."
                    "But her surprised reaction makes me more determined to succeed."
                    show katjack mikefuck mike normal at stepback(speed=0.1, h=-10, v=0)
                    "With her holding me in place, I begin to move back and forth."
                    "This draws the head of my cock up and down between her buttocks."
                    "And every pass that I make sees Kat gasp and moan all the more."
                    show katjack mikefuck at stepback(speed=0.1, h=-10, v=0)
                    "Each time I repeat the move, I feel her muscles relax just a little."
                    "And each time I almost hold my breath, hoping for a breakthrough."
                    "It happens again and again, making me go through the motions almost without thinking."
                    show katjack mikefuck at stepback(speed=0.1, h=-10, v=0)
                    "So when it actually does happen, I'm caught off-guard."
                    show katjack mikefuck mike surprised with hpunch
                    "All of a sudden I feel Kat's muscles surrender, and I sink into her."
                    "Both of us gasp, momentarily stunned by the unexpected sensation."
                    "But it only takes a second for us to recover."
                    show katjack mikefuck normal at stepback(speed=0.1, h=-10, v=0)
                    "And once we do, I start thrusting in and out of Kat in earnest."
                    "Likewise she comes back to life too, throwing back her head and holding on for dear life."
                    "Which is just as well, because I'm not holding anything back this time."
                    show katjack mikefuck at stepback(speed=0.1, h=-10, v=0)
                    "I throw all that I have into the effort of pounding away at Kat."
                    "And for a moment it looks like she won't be able to hold on at all."
                    "But then I see her eyes settle on something else."
                    show katjack mikefuck at stepback(speed=0.1, h=-10, v=0)
                    "Her hand darts out, grabbing hold of what I realise is Jack's cock!"
                    show katjack mikefuck mike jack lick with hpunch
                    "Then she pulls it towards herself, wrapping her lips around the head."
                    show katjack mikefuck at stepback(speed=0.1, h=-10, v=0)
                    "Of course Jack doesn't object at all, just going along with it."
                    "And that leaves me to tear my eyes away and focus on the task at hand."
                    show katjack mikefuck at stepback(speed=0.1, h=-10, v=0)
                    "Without any further distractions, I use the very last of my energy."
                    "It powers me on to the very end, until the moment I feel myself start to lose it."
                    show katjack mikefuck at stepback(speed=0.1, h=-10, v=0)
                    "And with Kat otherwise engaged, I can end things exactly how I choose too!"
                    menu:
                        "Cum inside ass":
                            "Still feeling the need to indulge myself, I push on to the end."
                            show katjack mikefuck with hpunch
                            "And when I finally come, I do so as deep inside Kat as I possibly can."
                            with hpunch
                            "Helpless and unable to escape, she takes everything that I have to give."
                            show katjack mikefuck ahegao open with hpunch
                            "Lying there until I'm totally spent, and her pussy is overflowing."
                        "Pull out of ass":
                            "Wanting to make a point, even to mark my territory, I make to pull out."
                            "Helpless and unable to move, Kat can do nothing to stop me."
                            with hpunch
                            "She lies there, still writhing with pleasure as I slide free."
                            show katjack mikefuck out mikecum with hpunch
                            "And then I shoot my load over her belly and thighs."
        "Jack fucks Kat":
            "Part of me wants to take full advantage of the fact Kat's deferring to me."
            "To be totally selfish and make sure that I'm the one getting all the attention."
            "But at the same time I'm painfully aware of the fact there are three people in this relationship."
            "And putting myself in front of Jack isn't going to help it to thrive."
            "So I push aside my instincts and decide to put Jack ahead of me."
            "I watch as Kat reaches back and grabs Jack's manhood."
            "But rather than seize the initiative, he looks up at me."
            jack.say "What do I do now?"
            jack.say "Seriously, dude..."
            jack.say "You gotta help me out here!"
            "Fuck sake, what is it with these two?"
            "Have I got to plan the whole thing out for them?!?"
            menu:
                "Lead Jack to fuck Kat's pussy":
                    scene bg black
                    show katjack doublepen mikeback
                    with hpunch
                    "The first step to doing so is to let myself onto the bed."
                    "And as I do so, I catch Kat to bring her down with me."
                    "Of course she's totally unprepared for this."
                    kat.say "Wha..."
                    kat.say "Whoa..."
                    kat.say "Why are you..."
                    mike.say "Hey, Jack!"
                    mike.say "Keep it simple, stupid!"
                    jack.say "Huh?"
                    mike.say "Use the front-door!"
                    show katjack doublepen jackfront
                    "As soon as I explain myself in the most simple terms possible, Jack seems to catch on."
                    "He nods eagerly, already beginning to move as he puts my advice into action."
                    "Luckily for him, it seems that Kat's a lot more on the ball."
                    "And perhaps even more luckily for Jack, she's also in a pretty good mood right now."
                    "She gives me a knowing wink as she reaches down between her legs."
                    "Then I hear Jack gasp as she grabs the shaft of his penis."
                    "Looks like he's going to have all the help he needs to do this thing right!"
                    "I watch as Kat begins to move up and down under Jack."
                    "All the time she's working the head of his cock against her pussy too."
                    "It's glistening in the light, letting me know that Kat's already pretty excited."
                    show katjack doublepen closed
                    "And it's not long before she closes her eyes, the sensations beginning to get to her."
                    show katjack doublepen pleasure blush jackvaginal
                    kat.say "Mmm..."
                    kat.say "Oh god..."
                    kat.say "The feels so good!"
                    show katjack doublepen at stepback(speed=0.05, h=10, v=0)
                    "I take a moment to look over Kat's shoulder as she says all of this."
                    "And I'm rewarded with the sight of Jack's beaming face behind her."
                    "He's way too engrossed in what's happening to have a hope of seeing me."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=0)
                    "So I get to watch as he tightens his grip on Kat, moving ever faster himself."
                    "What I'm getting to see here is very impressive, and it's getting me hard too."
                    "But I've kind of already resigned myself to the fact that I'm only going to be watching."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=0)
                    "That is until I turn my attention back to Kat, and I get an unexpected surprise."
                    "I feel her hands all over me, stroking and caressing my naked body."
                    "And that's all the motivation I need to start doing it in return too."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=0)
                    "This means that pretty soon I'm as involved in what's going on as Kat and Jack."
                    "I swear that I can feel everything that Kat's feeling too."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=0)
                    "Every move that Jack makes being translated into what she's doing to me."
                    "And I'm sure that this is the way I'm going to ride this thing out."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=0)
                    "But then I hear the sound of Jack calling my name again."
                    jack.say "[hero.name]…"
                    jack.say "Hey, hey!"
                    show katjack doublepen at stepback(speed=0.05, h=10, v=0)
                    "I open my eyes and pull away from Kat, unable to believe what I'm hearing."
                    mike.say "What is it now?!?"
                    jack.say "Erm..."
                    jack.say "I think I'm gonna cum..."
                    jack.say "What should I do about it?"
                    menu:
                        "Tell Jack to cum inside Kat's pussy":
                            mike.say "Just keep going, you moron!"
                            show katjack doublepen at stepback(speed=0.05, h=10, v=0)
                            "Jack nods eagerly, making Kat being to laugh out loud."
                            with hpunch
                            "But she can only keep it going until the moment he does as I say."
                            show katjack doublepen orgasm jackcum with hpunch
                            "Because then she stiffens, feeling the intensity of what he's doing."
                            with hpunch
                            "And I find myself having to hold her up until it's all over."
                        "Tell Jack to pull out of Kat's pussy":
                            mike.say "Pull out, you moron!"
                            show katjack doublepen at stepback(speed=0.05, h=10, v=0)
                            "Jack nods eagerly, making Kat being to laugh out loud."
                            "But she can only keep it going until the moment he does as I say."
                            show katjack doublepen jackout with hpunch
                            "Because then she stiffens, feeling the intensity of him pulling out of her."
                            show katjack doublepen orgasm jackcum with vpunch
                            "I can't see what's happening behind her back."
                            with vpunch
                            "But it must be pretty intense."
                            "Because I find myself having to hold her up until it's all over."
                "Lead Jack to fuck Kat's ass":
                    scene bg black
                    show katjack jackfuck
                    with hpunch
                    "The first step to doing so is to let myself onto the bed."
                    "And as I do so, I catch Kat to bring her down with me."
                    "Kat's so on the ball that she even manages to make it look like I'm catching her."
                    "As though she's the one that needed to be rescued from falling by me!"
                    kat.say "Urgh..."
                    kat.say "Thanks for catching me, [hero.name]!"
                    "I watch as Kat reaches back and grabs Jack's manhood."
                    "But rather than seize the initiative, he looks up at me."
                    jack.say "What do I do now?"
                    jack.say "Seriously, dude..."
                    jack.say "You gotta help me out here!"
                    mike.say "Make it memorable, doofus!"
                    jack.say "Huh?"
                    mike.say "Use the back-door, Jack!"
                    show katjack jackfuck jack
                    "As soon as I explain myself in the most simple terms possible, Jack seems to catch on."
                    "He nods eagerly, already beginning to move as he puts my advice into action."
                    "Luckily for him, it seems that Kat's a lot more on the ball."
                    "And perhaps even more luckily for Jack, she's also in a pretty good mood right now."
                    show katjack jackfuck jack closed
                    pause 0.1
                    show katjack jackfuck jack open
                    "She gives me a knowing wink as she reaches down between her legs."
                    "Then I hear Jack gasp as she grabs the shaft of his penis."
                    "Looks like he's going to have all the help he needs to do this thing right!"
                    "I watch as Kat begins to move up and down atop Jack."
                    "All the time she's working the head of his cock between her ass cheeks too."
                    "It doesn't seem to take long for the muscles to begin relaxing either."
                    show katjack jackfuck jack jackinside closed
                    "So it's not long before she closes her eyes, the sensations beginning to get to her."
                    kat.say "Mmm..."
                    kat.say "Oh god..."
                    kat.say "The feels so good!"
                    show katjack jackfuck jack jackinside open
                    "I take a moment to look over Kat's shoulder as she says all of this."
                    "And I'm rewarded with the sight of Jack's beaming face behind her."
                    "He's way too engrossed in what's happening to have a hope of seeing me."
                    show katjack jackfuck jack shake closed at stepback(speed=0.1, h=-10, v=0)
                    "So I get to watch as he tightens his grip on Kat, moving ever faster himself."
                    "What I'm getting to see here is very impressive, and it's getting me hard too."
                    "But I've kind of already resigned myself to the fact that I'm only going to be watching."
                    show katjack jackfuck jack at stepback(speed=0.1, h=-10, v=0)
                    "That is until I turn my attention back to Kat, and I get an unexpected surprise."
                    "Her eyes are now wide open, and she's looking straight at me!"
                    "Kat crooks a single finger at me, beckoning me forwards."
                    show katjack jackfuck jack at stepback(speed=0.1, h=-10, v=0)
                    "And I do as I'm told without a second thought, leaning in to get closer."
                    "Once I'm within reach, Kat leans forwards plants her lips against mine."
                    "Kat doesn't hold back either, or make the kiss chaste in any way, shape or form."
                    show katjack jackfuck jack open at stepback(speed=0.1, h=-10, v=0)
                    "Instead she pushes her tongue straight into my mouth, encouraging me to do the same."
                    "At the same time I feel her hands all over me, stroking and caressing my naked body."
                    "And that's all the motivation I need to start doing it in return too."
                    show katjack jackfuck jack closed at stepback(speed=0.1, h=-10, v=0)
                    "This means that pretty soon I'm as involved in what's going on as Kat and Jack."
                    "I swear that I can feel everything that Kat's feeling too."
                    show katjack jackfuck jack at stepback(speed=0.1, h=-10, v=0)
                    "Every move that Jack makes being translated into what she's doing to me."
                    "And I'm sure that this is the way I'm going to ride this thing out."
                    show katjack jackfuck jack at stepback(speed=0.1, h=-10, v=0)
                    "But then I hear the sound of Jack calling my name again."
                    jack.say "[hero.name]…"
                    jack.say "Hey, hey!"
                    show katjack jackfuck jack at stepback(speed=0.1, h=-10, v=0)
                    "I open my eyes and pull away from Kat, unable to believe what I'm hearing."
                    mike.say "What is it now?!?"
                    jack.say "Erm..."
                    show katjack jackfuck jack at stepback(speed=0.1, h=-10, v=0)
                    jack.say "I think I'm gonna cum..."
                    jack.say "What should I do about it?"
                    menu:
                        "Tell Jack to cum inside Kat's ass":
                            mike.say "Just keep going, you moron!"
                            show katjack jackfuck jack at stepback(speed=0.1, h=-10, v=0)
                            "Jack nods eagerly, making Kat being to laugh out loud."
                            show katjack jackfuck jack at stepback(speed=0.1, h=-10, v=0)
                            "But she can only keep it going until the moment he does as I say."
                            show katjack jackfuck jack ahegao jackinside jackcum with hpunch
                            "Because then she stiffens, feeling the intensity of what he's doing."
                            show katjack jackfuck jack -shake with hpunch
                            "And I find myself having to hold her up until it's all over."
                        "Tell Jack to pull out of Kat's ass":
                            mike.say "Pull out, you moron!"
                            "Jack nods eagerly, making Kat being to laugh out loud."
                            show katjack jackfuck jack at stepback(speed=0.1, h=-10, v=0)
                            "But she can only keep it going until the moment he does as I say."
                            show katjack jackfuck jack ahegao with hpunch
                            "Because then she stiffens, feeling the intensity of him pulling out of her."
                            show katjack jackfuck jack jackoutside jackcum -shake with hpunch
                            "I can't see what's happening behind her back."
                            show katjack jackfuck jack bodycum with hpunch
                            "But it must be pretty intense."
                            show katjack jackfuck jack jackoutside -jackcum
                            "Because I find myself having to hold her up until it's all over."
        "Fuck Kat with Jack":
            "I'm just beginning to think about which one of us should get lucky."
            "Whether it's Jack or me that gets to actually do it with Kat on this occasion."
            "But then it hits me right between the eyes - what am I even doing?!?"
            "We're supposed to be in a threesome together, not a time-share scheme."
            "And the last time I checked, it wasn't like Kat had only one hole either."
            mike.say "Hey, Jack..."
            mike.say "You're a guy with a healthy appetite."
            mike.say "So what would you say to a spit-roast?"
            "Jack looks surprised by the question, narrowing his eyes at me."
            jack.say "That sounds great, buddy..."
            jack.say "But maybe we should take care of business here first?"
            jack.say "Plus, that way we'll have built up a serious hunger too!"
            "I see kat doing the best she can to keep a straight face."
            "But it's no good, and she soon bursts out laughing."
            kat.say "Oh, Jack..."
            kat.say "You total moron!"
            kat.say "He's asking if you want to take a hole each, yeah?"
            "It seems like Kat doesn't want to leave things to Jack a second time."
            "Because she makes herself clear a moment later."
            "Pointing at her pussy with one hand and her ass with the other."
            "Jack's eyes go wide as realisation dawns on him."
            jack.say "Oh..."
            jack.say "Oh yeah..."
            jack.say "I totally knew what you meant really."
            jack.say "I was just making a joke out of it."
            "Maybe another time I'd have called Jack on his ridiculous bullshit."
            "But right now I'm more interested in getting things started."
            "So rather than saying any more, I make my first move."
            menu:
                "Fuck pussy and Jack fucks ass":
                    scene bg black
                    show katjack jackfuck open mikeoutside
                    with fade
                    "Which is to step right up and put myself in front of Kat, belly-to-belly."
                    "She smiles and reaches out to put her arms on my shoulders without question."
                    "Because she instinctively knows that I've chosen the hole round the front."
                    "But as I kind of expected, Jack keeps on staring at me blankly for a moment."
                    "That is until I nod my head toward Kat's ass."
                    show katjack jackfuck jack jackoutside
                    "Thankfully that's all he needs to catch on and get up behind her."
                    "And to be honest, I'm glad that he's back there right now."
                    "Because it means that I can rely on him to hold Kat up for me."
                    "Taking full advantage, I lean in close."
                    "That's when I feel Kat take hold of my cock."
                    "I can't help gasping in surprise at the sudden and unexpected sensation."
                    mike.say "Ah..."
                    kat.say "What's the matter?"
                    kat.say "Am I coming on too strong for you?"
                    mike.say "Oh no, no way..."
                    mike.say "Don't stop on my account!"
                    "Kat gives me a knowing smile as she presses the head of my cock against her pussy."
                    show katjack jackfuck closed mikeinside
                    "At the same time I'm pushing forwards myself, instinctually trying to get inside."
                    "But it's the natural resistance her body puts up that adds the spice to what we're doing."
                    "If Kat's feeling even a fraction of what I am right now, she must be almost helpless."
                    "We keep the same motions going for what feels like forever, with nothing changing."
                    "And then it happens, I feel the smooth sensation of Kat opening up like a flower."
                    "I sink into her in one smooth motion, not stopping until she's totally filled."
                    "But the her body doesn't seem to be done surrendering quite yet."
                    show katjack jackfuck jackinside
                    "Because within moments, I hear Jack gasping too."
                    show katjack jackfuck jack closed at stepback(speed=0.05, h=-10, v=0)
                    "And then Kat starts to sink down onto him at the same time."
                    "Not wanting to be left behind or pulled out by the motion, I follow the motion."
                    show katjack jackfuck jack closed at stepback(speed=0.05, h=-10, v=0)
                    "And pretty soon everyone is moving, up and down, this way and that."
                    "At first it kind of feels like Jack and I are in direct competition."
                    show katjack jackfuck jack closed at stepback(speed=0.05, h=-10, v=0)
                    "That we're both trying to be the one to fuck Kat hardest and fastest."
                    "But soon enough I discover that we can make movements that are sympathetic."
                    show katjack jackfuck shake at stepback(speed=0.05, h=-10, v=0)
                    "And we fall into that rhythm without the need to say a word."
                    show katjack jackfuck at stepback(speed=0.05, h=-10, v=0)
                    "One goes up when one goes down."
                    show katjack jackfuck at stepback(speed=0.05, h=-10, v=0)
                    "One goes in when one goes out."
                    show katjack jackfuck at stepback(speed=0.05, h=-10, v=0)
                    "This mean we're not in each other's way."
                    "But more importantly it means that Kat is getting the best of both worlds."
                    "Caught in the middle of what's going on, she's well and truly impaled."
                    show katjack jackfuck at stepback(speed=0.05, h=-10, v=0)
                    "Yet all it takes is a single glance to see that she's loving every moment."
                    "One second she's looking at me, the next at Jack and then at the ceiling."
                    show katjack jackfuck at stepback(speed=0.05, h=-10, v=0)
                    "And all the time she's nodding, like she never wants it to stop."
                    "The only problem is that I can't keep this up forever."
                    show katjack jackfuck at stepback(speed=0.05, h=-10, v=0)
                    "And a quick glance at Jack tells me the same is true of him."
                    "In fact the moment I meet his eye, he holds my glance."
                    jack.say "I..."
                    jack.say "I'm gonna lose it!"
                    jack.say "What should I do?!?"
                    "This time I'm not annoyed or irritated by Jack's question."
                    show katjack jackfuck at stepback(speed=0.05, h=-10, v=0)
                    "And that's because I'm in the exact same position as he is."
                    "So I take it upon myself to be the one to direct traffic."
                    menu:
                        "Tell Jack to cum inside Kat's ass":
                            show katjack jackfuck jack closed at stepback(speed=0.05, h=-10, v=0)
                            mike.say "Don't stop now..."
                            mike.say "Just..."
                            mike.say "Just keep going!"
                            show katjack jackfuck jack closed at stepback(speed=0.05, h=-10, v=0)
                            "Jack nods and does as he's told."
                            show katjack jackfuck jackcum mikecum with hpunch
                            "Which means that mere moments later, we both lose it inside of Kat."
                            show katjack jackfuck ahegao with hpunch
                            "I don't know which one hits first, just that she starts to jerk and wriggle."
                            show katjack jackfuck -shake with hpunch
                            "It's like watching someone tossed here and there, all the time cumming too."
                            "And I'm sure that if we weren't holding onto her, Kat would be in a heap on the floor right now!"
                        "Tell pull out of Kat's ass":
                            mike.say "Okay, Jack..."
                            mike.say "Pull out..."
                            mike.say "NOW!"
                            "Jack nods and does as he's told."
                            show katjack jackfuck jackoutside mikeoutside
                            "Which means that mere moments later, we both pull out of Kat."
                            "I don't know which one of us manages to make it out first."
                            "But the effect it has on her is pretty impressive."
                            show katjack jackfuck jackcum mikecum with hpunch
                            "It's like watching someone tossed here and there, all the time cumming too."
                            show katjack jackfuck bodycum with hpunch
                            "And I'm sure that if we weren't holding onto her, Kat would be in a heap on the floor right now!"
                            show katjack jackfuck ahegao -jackcum -mikecum -shake with hpunch
                            "In watching her I almost forget what I'm doing, not noticing that I shoot my load over her belly."
                            "Or that Jack does the same thing to her back."
                "Fuck ass and Jack fucks pussy":
                    show katjack doublepen mikeback with fade
                    "Which is to step right up and turn Kat around, so that we're standing belly to back."
                    "She smiles and leans herself backwards into me without question."
                    "Because she instinctively knows that I've chosen the hole back here."
                    "But as I kind of expected, Jack keeps on staring at me blankly for a moment."
                    "That is until I nod my head toward Kat's pussy."
                    "Thankfully that's all he needs to catch on and get in front of her."
                    "And to be honest, I'm glad that he's round there right now."
                    "Because it means that I can rely on him to hold Kat up for me."
                    "Taking full advantage, I lean in close."
                    "That's when I feel Kat take hold of my cock."
                    "I can't help gasping in surprise at the sudden and unexpected sensation."
                    mike.say "Ah..."
                    show katjack doublepen pleasure
                    kat.say "What's the matter?"
                    kat.say "Am I coming on too strong for you?"
                    show katjack doublepen smile
                    mike.say "Oh no, no way..."
                    mike.say "Don't stop on my account!"
                    "Kat gives me a knowing smile as she presses the head of my cock between the cheeks of her ass."
                    "At the same time I'm pushing forwards myself, instinctually trying to get inside."
                    "But it's the natural resistance her body puts up that adds the spice to what we're doing."
                    "If Kat's feeling even a fraction of what I am right now, she must be almost helpless."
                    "We keep the same motions going for what feels like forever, with nothing changing."
                    show katjack doublepen scared closed blush mikeanal
                    "And then it happens, I feel the smooth sensation of Kat opening up like a flower."
                    "I sink into her in one smooth motion, not stopping until she's totally filled."
                    "But the her body doesn't seem to be done surrendering quite yet."
                    show katjack doublepen jackvaginal
                    "Because within moments, I hear Jack gasping too."
                    "And then Kat starts to sink down onto him at the same time."
                    "Not wanting to be left behind or pulled out by the motion, I follow the motion."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                    "And pretty soon everyone is moving, up and down, this way and that."
                    "At first it kind of feels like Jack and I are in direct competition."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                    "That we're both trying to be the one to fuck Kat hardest and fastest."
                    "But soon enough I discover that we can make movements that are sympathetic."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                    "And we fall into that rhythm without the need to say a word."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                    "One goes up when one goes down."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                    "One goes in when one goes out."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                    "This mean we're not in each other's way."
                    "But more importantly it means that Kat is getting the best of both worlds."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                    "Caught in the middle of what's going on, she's well and truly impaled."
                    "Yet all it takes is a single glance to see that she's loving every moment."
                    show katjack doublepen open pleasure at stepback(speed=0.05, h=10, v=10)
                    "One second she's looking at me, the next at Jack and then at the ceiling."
                    "And all the time she's nodding, like she never wants it to stop."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                    "The only problem is that I can't keep this up forever."
                    "And a quick glance at Jack tells me the same is true of him."
                    "In fact the moment I meet his eye, he holds my glance."
                    show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                    jack.say "I..."
                    jack.say "I'm gonna lose it!"
                    jack.say "What should I do?!?"
                    show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                    "This time I'm not annoyed or irritated by Jack's question."
                    "And that's because I'm in the exact same position as he is."
                    "So I take it upon myself to be the one to direct traffic."
                    menu:
                        "Tell Jack to cum inside Kat's pussy":
                            mike.say "Don't stop now..."
                            mike.say "Just..."
                            mike.say "Just keep going!"
                            show katjack doublepen at stepback(speed=0.05, h=10, v=10)
                            "Jack nods and does as he's told."
                            show katjack doublepen orgasm mikecum jackcum with vpunch
                            "Which means that mere moments later, we both lose it inside of Kat."
                            with vpunch
                            "I don't know which one hits first, just that she starts to jerk and wriggle."
                            with vpunch
                            "It's like watching someone tossed here and there, all the time cumming too."
                            "And I'm sure that if we weren't holding onto her, Kat would be in a heap on the floor right now!"
                        "Tell Jack to pull out of Kat's pussy":
                            mike.say "Okay, Jack..."
                            mike.say "Pull out..."
                            mike.say "NOW!"
                            "Jack nods and does as he's told."
                            show katjack doublepen jackout mikeout
                            "Which means that mere moments later, we both pull out of Kat."
                            "I don't know which one of us manages to make it out first."
                            "But the effect it has on her is pretty impressive."
                            show katjack doublepen orgasm jackcum mikecum with vpunch
                            "It's like watching someone tossed here and there, all the time cumming too."
                            with vpunch
                            "And I'm sure that if we weren't holding onto her, Kat would be in a heap on the floor right now!"
                            with vpunch
                            "In watching her I almost forget what I'm doing, not noticing that I shoot my load over her belly."
                            "Or that Jack does the same thing to her back."
    scene bg black
    show katjack foreplay closed
    with fade
    "Afterwards, everyone seems utterly spent, collapsing into a pile on the bed."
    "All that any of us can do is lie there, smiling with satisfaction."
    "And maybe it's not because we're out of breath that nobody's talking."
    "Just maybe it's because what we're feeling can't be put into words."
    $ kat.sexperience += 1
    return

label jack_kat_male_ending:
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding
    show jack date zorder 2 at center, zoomAt(1.5, (300, 1080))
    with fade
    "I've known Jack for a good number of years now, and we've been through a lot together."
    "There's more than a few crazy stories I could tell you about what we've gotten up to."
    "But I don't think any of them compare to what we're doing today."
    "Because right now, Jack and I are standing in front of the altar in a chapel."
    "We're wearing matching suits and waiting for the bride to come walking down the aisle."
    "The only thing is, it's not the usual groom with his good buddy in the role of best man."
    "Oh no, we're technically both the groom today, at least I think that's how it works."
    "Because we're both marrying the same girl!"
    "If you remember, Jack got the idea that we should propose to Kat together."
    "I agreed, and when we finally mustered up the courage, she only went and said yes!"
    "So here we are, sweating and trying to settle our nerves as we wait."
    "I sneak a look over my shoulder at the assembled guests that are filling the pews."
    "Kat, Jack and I are all well-represented by family and friends out there."
    "But I have to admit that there are faces out there I don't recognise at all."
    "I suppose these are all the people I'll have to get to know once we're married."
    "Jack seems to be looking in the same direction as well."
    "And when I catch his eye, it seems as though he's about to say something."
    "But then the sound of music fills the air, and the whole chapel stands to attention."
    show jack embarrassed date at center, zoomAt(1.5, (240, 1080)) with ease
    "Every head in the place turns to look at the doors, just as they swing open."
    show kat wedding smile zorder 1 at center, zoomAt(1.0, (640, 720))
    hide jack
    with dissolve
    show kat wedding at center, traveling(1.5, 5.0, (640, 1040))
    "And then Kat walks into the chapel and down the aisle."
    "I can't take my eyes off of her, and I guess that Jack must be staring too."
    "Because I've never seen Kat dressed up like this before, not even once."
    "Normally she's one hundred percent casual, totally relaxed in her choice of clothes."
    "So seeing her in an elegant, flowing white dress is a complete surprise."
    "And believe me, she looks absolutely amazing!"
    if kat.is_visibly_pregnant:
        "I can hardly tell that she's got a swollen belly under the dress."
        "The cut of it manages to hide the fact pretty well."
        "Not that I'm at all embarrassed by the fact."
        "In fact I'm incredibly proud that Kat's carrying a baby."
        "Though I admit to not knowing which of us is the father."
    else:
        "I make mental note to ask Kat if she'll dress-up nice in the future."
        "Because I'd be really disappointed if this is the only time she does it."
        "She looks way too good to never see her looking this way again."
    show kat wedding at center, zoomAt(1.5, (900, 1040))
    show jack embarrassed date at center, zoomAt(1.5, (380, 1080))
    with easeinleft
    "Kat strides confidently up to the altar, Jack and I stepping aside to let her pass."
    "And then she looks to either side of her, giving each of us a nod."
    show kat talkative
    kat.say "Okay, guys..."
    kat.say "Are you ready to do this thing?"
    show kat smile
    mike.say "Ready as I'll ever be!"
    show jack lying
    jack.say "You bet I am, Kat!"
    show jack normal
    show kat happy
    kat.say "Then let's do it!"
    show kat smile
    "As one we turn to look at the priest, who nods pleasantly."
    "Priest" "Shall we begin?"
    "Priest" "Dearly beloved, we are gathered here today..."
    "Priest" "To join these three people, in the bonds of holy matrimony."
    "From that point on the ceremony is just like every other one you've seen."
    "So pardon me if we jump forward to where it gets more interesting."
    "Which would be the point where we all get to exchange our vows."
    "Priest" "Do you, Kat..."
    "Priest" "Take Jack and [hero.name]…"
    "Priest" "To be your lawful, wedded partners?"
    show kat happy at startle
    kat.say "I do."
    show kat smile
    "The priest nods and then turns to Jack."
    "Priest" "Do you, Jack..."
    "Priest" "Take Kat and [hero.name]…"
    "Priest" "To be your lawful, wedded partners?"
    show jack whining at startle
    jack.say "NO!"
    show jack sadsmile
    show kat stuned
    "The priest, Kat and I all turn to look at Jack in horror."
    "And at the same time every guest in the chapel gasps too."
    show jack happy at startle
    jack.say "KIDDING!"
    show jack smile
    show kat smile
    jack.say "Of course I do!"
    jack.say "Man, you guys have zero sense of humour!"
    show jack normal
    "The priest shoots a withering look at Jack."
    "Then he turns his attention to me."
    "Priest" "And do you, [hero.name]…"
    "Priest" "Take Kat and Jack..."
    "Priest" "To be your lawful, wedded partners?"
    "Priest" "Even after that so-called display of humour?"
    mike.say "I do."
    "The priest nods again."
    "Priest" "Rather you than me..."
    "Priest" "I call upon those here present..."
    "Priest" "That if you know of any lawful reason..."
    "Priest" "That these three may not be joined in holy matrimony..."
    "Priest" "Speak now, or forever hold your peace!"
    "There's the customary pause while the guests chuckle to each other."
    "And I'm sure to keep a close eye on Jack the whole time too."
    "Just in case he gets the urge to treat us to another amusing performance."
    "But thankfully nothing untoward happens before the priest speaks again."
    "Priest" "Very well..."
    show kat blush
    show jack blush
    "Priest" "It therefore gives me great pleasure to pronounce you married."
    "Priest" "You may celebrate in a way that you find appropriate."
    "The priest steps back to allow the three of us to come together."
    show jack happy zorder 1 at center, traveling(2.0, 0.3, (440, 1380))
    show kat happy zorder 2 at center, traveling(2.0, 0.3, (740, 1340))
    "Which allows Jack and I to lean in and kiss Kat from either side."
    "Then she tosses her bouquet back and over her shoulder."
    "But she doesn't seem to care where it lands."
    "Because all of her attention is focussed on her new husbands."
    "And the only thing we have eyes for is our new wife."

    scene bg black
    show katjack ending
    with fade
    jack.say "Oh boy, oh boy, oh boy..."
    jack.say "This is going to be so great!"
    jack.say "After all this time, I finally get to be the one telling the story!"
    kat.say "Hey!"
    kat.say "What do you think you're doing?"
    kat.say "We're supposed to be doing this together."
    kat.say "Telling them about how great life is now that we're all living happily ever after."
    jack.say "Oh..."
    jack.say "Oh yeah, of course!"
    jack.say "I was just getting warmed up, that's all."
    kat.say "Well, you should probably be the one to start."
    kat.say "You are the one that's know [hero.name] the longest."
    jack.say "That's for sure, Kat..."
    jack.say "[hero.name] and I have been buddies since we were kids."
    jack.say "We always played videogames together, and Deities and Demigods..."
    kat.say "So what you're saying is that you were pretty standard nerds?"
    jack.say "Nerds?"
    jack.say "We have never been nerds!"
    kat.say "Oh really?"
    kat.say "Well what if I were to say something like..."
    kat.say "The prequels are better than the original trilogy."
    jack.say "WHAT?!?"
    jack.say "What are you talking about?"
    jack.say "Are you totally and utterly insane?"
    kat.say "Ha, ha!"
    jack.say "Oh..."
    jack.say "Okay, okay..."
    jack.say "I see what you did there, and it was very clever."
    jack.say "But you played more videogames than any of us, Kat..."
    jack.say "Hell, you even did it for a living!"
    kat.say "That doesn't make me a nerd, it makes me a professional."
    kat.say "And you should be thankful that I did too."
    kat.say "Because if not, I'd never have met [hero.name] in the first place."
    kat.say "The first time I ever saw him, he was competing against me in a tournament."
    jack.say "Point taken."
    jack.say "But remind me of something, Kat..."
    jack.say "What happened in that tournament?"
    kat.say "Really?"
    kat.say "You're going to make me say it?"
    kat.say "After all this time?"
    jack.say "Of course I am!"
    jack.say "Come on, Kat..."
    jack.say "Out with it!"
    kat.say "He beat me, okay..."
    kat.say "Are you happy now?"
    kat.say "He beat me and then I kind of got intrigued to find out why."
    jack.say "You were streaming your games at the time too, right?"
    jack.say "Because that's how I first discovered you."
    kat.say "Oh yeah, more proof of your geekdom!"
    kat.say "How did I end up here?"
    kat.say "Married to a fanboy and a guy that beat me at videogames?"
    jack.say "Oh come on, Kat..."
    jack.say "You love us really."
    kat.say "I suppose so."
    if kat.flags.mikeBabies >= 1:
        kat.say "But I think little Jack Junior has a lot to do with that!"
        jack.say "Oh yeah..."
        jack.say "It was kinda nice of [hero.name] to let us call him that."
        kat.say "Well he does look like a miniature version of you!"
    else:
        kat.say "But I think little Peach has a lot to do with that!"
        jack.say "Oh yeah..."
        jack.say "She's so great!"
        jack.say "Erm..."
        jack.say "You ever wonder which one of us is the..."
        kat.say "Stop right there, Jack..."
        kat.say "We all agreed not to open that can of worms!"







    jack.say "And we have the best jobs possible too."
    jack.say "We run our own videogames store."
    jack.say "Which is the coolest thing ever!"
    kat.say "Only you two seem to think your job's just sitting around playing games."
    kat.say "While I'm the one that has to do all of the hard work!"
    jack.say "Who are you trying to kid, Kat?"
    jack.say "You always insist on being the first to play all of the new games!"
    kat.say "That's research!"
    kat.say "Plus I have to keep my skills sharp for the professional tournaments."
    jack.say "Whatever you say, Kat..."
    jack.say "But you've got to admit, life is pretty sweet right now."
    kat.say "I guess you're right, Jack..."
    kat.say "We've got a great business doing what we love."
    kat.say "And even better, we've got each other too."
    jack.say "Aww..."
    jack.say "See, Kat?"
    jack.say "I knew you were a big softie underneath."
    kat.say "Not as big and soft as your belly!"
    jack.say "Hey..."
    jack.say "No fat-shaming!"
    jack.say "And anyway, I'm just big-boned..."
    kat.say "Of course you are, Jack, of course you are."
    scene bg black with dissolve
    pause 0.3
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label kat_preg_talk:
    show kat a sad
    "Kat's got a pretty serious expression spread across it right now."
    "Plus the fact that her eyes seem to be red and more than a little puffy."
    show kat a sad at center, zoomAt(1.5, (640, 1040))
    "Almost like..."
    mike.say "Kat..."
    mike.say "Have you..."
    mike.say "Have you been crying?"
    show kat a annoyed
    "As soon as I ask the question, Kat seems to become defensive."
    "She sniffles and shakes her head, though the evidence is right there."
    kat.say "No..."
    show kat a sadclosed
    kat.say "Yes..."
    show kat a sadsmile
    kat.say "Ah...that's not important!"
    mike.say "Of course it is, Kat!"
    mike.say "If something bad's happened to you, then I want to know."
    mike.say "That's why you're here, right?"
    show kat d sadclosed
    "Kat nods, still sniffling and sighing."
    "She also keeps wiping the corner of her eyes with the back of her hand."
    "And each time she does so, they become redder and more angry."
    "Though I get the distinct impression mentioning that would be a mistake."
    show kat a sad
    kat.say "Okay, [hero.name]..."
    kat.say "This is serious, yeah?"
    kat.say "So I need you to not panic."
    mike.say "I'll do my best."
    kat.say "You'd better!"
    kat.say "Because I just took a pregnancy test."
    kat.say "And the result was positive."
    "For a moment the world around me seems to slow and come to a stop."
    "I know what those words all mean, and how they fit together to create a greater meaning."
    "But for some reason I can't fully connect all of that back to reality."
    show kat a confused
    kat.say "[hero.name]?"
    kat.say "Did you hear what I said?!?"
    mike.say "Y...yeah, Kat..."
    mike.say "I heard you."
    show kat d
    "By now Kat's waving her arms in the air."
    "Beginning to demand answers from me."
    show kat sad
    kat.say "So what are we going to do?"
    kat.say "Tell me that, [hero.name]!"
    show kat d afraid
    kat.say "What the fuck are we going to do?!?"
    menu:
        "We should keep the baby":
            "Oddly enough, I don't hesitate to come out with an answer."
            "One that I hope will show I'm taking charge of the situation."
            "As well as reassuring Kat that everything will be fine."
            mike.say "Don't worry about anything, Kat."
            mike.say "Sure, this is a shock and all."
            mike.say "But we're not the first people to end up here."
            show kat surprised
            "Kat looks up at me, her eyes wider than ever."
            "But for the first time, I think I can see hope in them."
            kat.say "You..."
            show kat confused
            kat.say "You really mean that?"
            kat.say "You're going to try to make this work?"
            "I shake my head."
            mike.say "No, Kat..."
            mike.say "I'm not going to try to make it work."
            mike.say "I am going to make it work."
            show kat a happy
            $ kat.love += 10
            "Something inside of Kat seems to break as she hears this."
            "It's like until that very moment, she's been holding back."
            "Doing the best she can to stay strong under the circumstances."
            "But now that she knows I'm on her side, the dam finally breaks."
            show kat at center, zoomAt(1.5, (640, 1040)) with hpunch
            "Kat throws her arms around me, hugging me with surprising strength."
            kat.say "We'll make it work, [hero.name]..."
            show kat a smile
            kat.say "You and me against the world."
            kat.say "Nothing's can beat us as long as we're together!"
            $ kat.flags.toldpreg = True
            hide kat
            show kat a smile at center, zoomAt(1.65, (640, 1140)), startle(0.05,-10)
            "I nod and wrap my arms around Kat."
            "Returning the gesture and trying to offer her reassurance."
            "But at the same time my mind is already filling."
            "Thoughts building up as to the enormity of the task ahead."
        "You should have a termination":
            "Oddly enough, I don't hesitate to come out with an answer."
            show kat at center, zoomAt(1.5, (640, 1040))
            "One that I hope will show I'm taking charge of the situation."
            "As well as reassuring Kat that everything will be fine."
            mike.say "Don't worry about anything, Kat."
            mike.say "I have some savings that I've been putting aside."
            mike.say "It was supposed to be for a deposit on a place of my own."
            mike.say "But this is more important than that."
            show kat confused
            "Kat seems a little confused by what I'm saying."
            "She frowns as she questions me further."
            kat.say "What's the money for, [hero.name]?"
            kat.say "Sure, we'll need it further down the line."
            kat.say "But I don't see what we need to pay for right now."
            mike.say "A termination isn't free, Kat!"
            mike.say "They don't hand those things out lightly either!"
            show kat shocked
            "Kat's eyes go wide at this."
            hide kat
            show kat shocked
            "And she actually takes a step backwards."
            "Putting some distance between the two of us."
            kat.say "A termination?"
            show kat offended
            $ kat.love -= 20
            kat.say "What are you talking about?"
            kat.say "I don't want to get rid of it!"
            mike.say "What am I talking about?"
            mike.say "What the hell are you talking about?!?"
            mike.say "I can't be a father and we can't start a family!"
            show kat annoyed
            kat.say "No, [hero.name]..."
            show kat angry
            $ kat.sub -= 10
            kat.say "I won't let you kill my baby!"
            kat.say "I'll do this on my own if I have to."
            kat.say "I don't need you, and the baby doesn't either!"
            show kat at right4 with ease
            "Before I can say another word, Kat turns on her heel."
            hide kat with easeoutright
            $ kat.set_gone_forever()
            "Then she runs away, as fast as her feet will carry her."
            "And something tells me that she won't be coming back."
    return

label kat_vibrator_restaurant:
    scene bg restaurant with fade
    show ryan as waitersprite at center, blacker
    pause 0.4
    show kat date at right with easeinright
    "Kat and I are just being shown to our table by the waiter."
    "We've been talking about this and that, everything and nothing."
    show ryan as waitersprite at blacker, left
    show kat date at right5
    with ease
    "Mainly because I couldn't get anything to eat at lunchtime today."
    "So I'm preoccupied with the way that my stomach keeps on growling."
    show kat date shy blush
    "That means I'm really not paying attention when Kat presses something into my hand."
    mike.say "Huh?"
    mike.say "What's..."
    "I'm about to ask what the hell Kat just handed me."
    "But then I see her shooting me a serious look."
    show kat date b defiant
    "And she's drawing her thumb and index finger over her lips as she does so."
    "Even in my confused state, I know that means she wants me to zip it!"
    show restaurant meal kat date nomeals
    show restaurant_meal_waiter_pose01 as waiter zorder 1
    with fade
    "So I let the matter drop and just sit down in the chair I'm guided to by the waiter."
    hide restaurant_meal_waiter_pose01 as waiter zorder 1 with easeoutleft
    "Once he's handed us a pair of menu's and taken our drinks order, he disappears."
    "Which means we're alone and I can finally ask Kat what's going on."
    mike.say "Kat..."
    mike.say "What is this thing?"
    "I make to hold it up."
    "But she waves her hand downwards."
    show restaurant meal kat date nomeals bored
    kat.say "Don't get it out and wave it around!"
    kat.say "Put it in your pocket and leave it there, okay?"
    "More puzzled than ever, I do as I'm told."
    mike.say "Yeah, Kat..."
    mike.say "This is getting weird!"
    show restaurant meal kat date nomeals blush -bored
    kat.say "It's a remote control, yeah?"
    kat.say "One that's for something I'm..."
    kat.say "Something I'm wearing, okay?"
    show restaurant meal kat date nomeals normal -blush
    "I can't help looking down at the pocket where I just stashed the remote."
    "But then I see Kat hold up her hand, as if she wants me to stop."
    kat.say "Wait!"
    kat.say "Don't touch it until I explain."
    "I nod and put both of my hands on the table where she can see them."
    "Because I figure that's the best way to show that I'm listening."
    "And maybe to finally get an explanation out of her."
    kat.say "I'll level with you, [hero.name]..."
    show restaurant meal kat date nomeals blush
    kat.say "That's the remote control for a vibrator."
    kat.say "A pretty powerful one too."
    kat.say "And right now that vibrator's located right about here."
    "My eyes go wide as Kat points down to her groin."
    mike.say "You..."
    mike.say "You can't be serious?!?"
    show restaurant meal kat date nomeals -blush -bored
    "Kat nods."
    kat.say "Oh, I'm serious alright."
    kat.say "All you have to do is press a button on that remote."
    kat.say "And I'll be helpless to resist what it does to me."
    "Suddenly I'm starting to feel like I'm in an action movie."
    "The kind where a bomb is going to blow up and kill everyone."
    "Unless the hero keeps driving a bus above thirty or something crazy like that!"
    mike.say "Erm..."
    mike.say "You mind if I ask why?"
    show restaurant meal kat date nomeals happy
    "Kat nods again, and I can see a sparkle in her eye as she does so."
    "Looks like she's been dying to explain it all to me."
    "Just like a villain in an action movie too!"
    kat.say "Look, I've always had this...thing about being controlled."
    kat.say "I guess you could call it a fetish, really."
    kat.say "Like, I play games all the time and I'm the one holding the controller."
    kat.say "But part of me wonders what it'd be like to be the sprite on the screen."
    kat.say "What it'd feel like to have someone controlling me!"
    show restaurant meal kat date nomeals -happy
    "I blink for a moment as realisation begins to set in."
    "And then suddenly, everything starts to make sense."
    mike.say "You..."
    mike.say "You mean you want me to..."
    mike.say "Control you?!?"
    show restaurant meal kat date nomeals happy
    "Kat nods for a third time."
    "More emphatically than ever before."
    kat.say "Yeah, [hero.name]..."
    kat.say "That's exactly what I mean."
    kat.say "I want you to control just how much sexual pleasure I experience!"
    "I take a quick glance around the restaurant as Kat says this."
    "Suddenly aware of just how many people are in here tonight."
    "Shit...where did they all come from?"
    "I'm sure half of them weren't there a moment before."
    mike.say "But, Kat..."
    mike.say "This place isn't exactly quiet, is it?"
    show restaurant meal kat date nomeals -happy bored
    kat.say "But don't you see?"
    show restaurant meal kat date nomeals -bored happy
    kat.say "That's part of the thrill!"
    show restaurant meal kat date nomeals -happy normal
    "The honest truth is that I do see."
    "And the more I think about it, the more the idea turns me on!"
    mike.say "Okay, Kat..."
    mike.say "You got it."
    mike.say "When should I turn it on?"
    "Kat shakes her head."
    kat.say "I don't want to know!"
    show restaurant meal kat date nomeals blush
    kat.say "That's part of the fun."
    kat.say "Just choose your moment and then turn it on, okay?"
    kat.say "Now this thing has three settings - low, medium and high."
    kat.say "I also want you to choose which one it's set to."
    show restaurant meal kat date nomeals -blush
    "With that, Kat stops talking about the vibrator."
    show restaurant_meal_waiter_pose01 as waiter zorder 1 at top_mostleft with easeinleft
    "And a moment later the waiter returns to take our orders."
    "I keep quiet about the whole thing too."
    "But I can feel the weight of the remote control in my pocket."
    hide restaurant_meal_waiter_pose01 as waiter zorder 1 with easeoutleft
    "And it's on my mind as I wait for the perfect moment to use it."
    show restaurant meal kat date happy
    kat.say "Mmm..."
    kat.say "This is SO good!"
    "I watch as Kat tastes her food, loving the flavour."
    "But the sounds she's making remind me of her moaning in a state of passion."
    "And that's when I know the moment has arrived."
    "So I reach into my pocket and turn on the vibrator."
    menu:
        "Low intensity":
            scene bg black
            show kat cunnilingus restaurant date eyes_close mouth_close vibrator remote turnon
            with fade
            "I decide that the best thing would be to set the vibrator to low."
            "Because I have no idea what the higher settings would do to Kat."
            "And the fact we're surrounded by other diners means I need to be cautious."
            show kat cunnilingus -remote
            "But even though I choose the lowest setting, the effect is pretty clear."
            "Kat's still making those moaning sounds over her food."
            "Yet even when she's swallowed a mouthful, they don't stop."
            "Instead she keeps on making those same low moaning sounds."
            "In fact the only thing that stops them is her putting more food into her mouth."
            "I watch in fascination as Kat seems to gush over every mouthful."
            "Her cheeks are flushing too, her eyes struggling to stay open."
            mike.say "It's good, huh?"
            kat.say "Mmm-hmm..."
            mike.say "What was that?"
            mike.say "I didn't hear what you said?"
            show kat cunnilingus eyes_open
            kat.say "Y...yeah..."
            kat.say "It's g...good!"
            "I nod as I look on in fascination at Kat's reaction."
            "I guess it's a mixture of genuine interest and very real arousal on my part."
            "And I just love the way that it's taking so much time for her to build up."
            show kat cunnilingus eyes_close mouth_hurt
            "Before she was just moaning as she ate, but now Kat's wriggling in her seat too!"
            "By the time we've finished our food, she's totally helpless."
            "Kat seems to be holding something in the whole time the waiter's at our table."
            "But as soon as he walks away, she gasps in an almost desperate manner."
            show kat cunnilingus eyes_up
            kat.say "Ah..."
            kat.say "Ah..."
            kat.say "Please, [hero.name]..."
            kat.say "Turn it off..."
            kat.say "I just came, and now I'm sitting in it!"
            $ kat.love += 10
        "Medium intensity":
            scene bg black
            show kat cunnilingus restaurant date eyes_close mouth_close vibrator
            with fade
            "I don't want to seem like some kind of pussy and choose the low setting."
            "But the thought of using the high one seems pretty crazy to me."
            show kat cunnilingus remote turnon
            "So I decide that the medium setting is the only sensible one to use."
            "And I feel pretty confident that I've made the right choice as I switch it on."
            show kat cunnilingus -remote
            "At first there doesn't seem to be any change in Kat."
            "She's still making that moaning sound as she eats her food."
            show kat cunnilingus mouth_open
            "But then I notice that the tone of it is changing subtly."
            "It's hard to hear as it begins, but clearer with every moment that passes."
            "The moans are getting longer and louder as time goes on."
            "Kat's putting less food into her mouth and chewing it more slowly."
            "Like she's moving in slow-motion or something!"
            "I can see that she's flushing too, her eyes kind of glazing over."
            mike.say "How's the food, Kat?"
            mike.say "You seem to be enjoying it?"
            show kat cunnilingus eyes_open mouth_hurt
            kat.say "Mmm..."
            kat.say "Uhn...yeah..."
            show kat cunnilingus eyes_up
            kat.say "Oh yeah!"
            kat.say "G...good...it's...good!"
            "I can feel myself getting hotter as I watch Kat work herself towards an orgasm."
            "She's still eating, like her body's on auto-pilot."
            "But she's also twitching in her seat."
            "Like she's being given electric shocks through the chair."
            show kat cunnilingus mouth_open
            "Finally she collapses backwards, almost tipping herself onto the floor."
            mike.say "Kat..."
            mike.say "Are you okay?"
            kat.say "T...turn it..."
            kat.say "Turn it...off..."
            kat.say "I just came, and now I'm sitting in it!"
            $ kat.love += 4
            $ kat.sub += 2
        "High intensity":
            scene bg black
            show kat cunnilingus restaurant date eyes_close mouth_close vibrator
            with fade
            "I figure that if I'm going to do this thing, then what the hell."
            "There's no point in holding back, and I might as well go all in."
            "So I forget all about the medium and low settings on the vibrator."
            "And instead I go straight for the high one."
            show kat cunnilingus remote turnon eyes_open mouth_hurt
            "The moment I hit the button, the effect is both visible and dramatic."
            "Before, Kat was just moaning quietly as she enjoyed her food."
            "But now her eyes widen in genuine surprise."
            "All I can say is that it's a good job she already swallowed her last mouthful."
            "Because now she seems to be totally in the thrall of the vibrator."
            show kat cunnilingus eyes_close mouth_open -remote
            "I watch in genuine fascination as Kat grabs the edge of the table."
            "Her fingers are turning white as they cling onto it too!"
            "Her mouth hangs open as she pants for breath."
            "And her cheeks have flushed as red as a fucking tomato!"
            mike.say "Erm..."
            mike.say "Is there something wrong with the food, Kat?"
            mike.say "Something in the sauce a little too piquant?"
            show kat cunnilingus eyes_up mouth_hurt
            kat.say "Ah..."
            kat.say "Urgh..."
            kat.say "Fnarr..."
            "The sounds that Kat's making are getting louder by the second."
            show kat cunnilingus eyes_close
            "She's starting to twitch and wriggle in her seat too."
            "All of which is getting us glances from the other diners."
            "I think about turning the vibrator off."
            "But then I remember that Kat made me promise not to."
            "My mind races as I try to think of some other solution."
            "And then one comes to me in a flash."
            "Sure, it's crazy - but what other point do I have?"
            show kat cunnilingus eyes_up mouth_open
            "I leap out of my chair and hurry to Kat's side of the table."
            "Then I pull her own chair aside and wrap my arms around her waist."
            "People start to gasp and stare in sheer amazement."
            "So I put the second part of my plan into action."
            mike.say "She's...choking..."
            mike.say "But...it's...okay..."
            mike.say "I know...the...Heimlich...Manoeuvre!"
            "As soon as they hear that, everyone backs off."
            "And some of them even cheer me on!"
            "All the while I can feel Kat grinding against me."
            "Until the moment she lets out one final, drawn out moan."
            show kat cunnilingus eyes_close
            kat.say "Ah..."
            kat.say "Ah..."
            kat.say "Please, [hero.name]..."
            kat.say "Turn it off..."
            kat.say "I just came, and now you're getting a wet crotch!"
            $ kat.sub += 5
    $ game.active_date.score += 15
    return

label kat_birthday_date_male:
    $ DONE["kat_birthday_date_male"] = game.days_played
    $ game.active_date.clothes = "casual"
    scene bg arena with fade
    "Agreeing to meet Kat at the gaming arena before our date was kind of a red herring."
    "I know that she likes to spend a lot of her time hanging out there and playing the latest games."
    "And I did drop some pretty heavy hints that what we're doing would involve videogames."
    "So my guess is that she's going to assume we're staying there to do more of the same."
    "Because after all, it is her birthday that we're celebrating."
    "But the truth is that I have a surprise in store for her."
    "One that I hope will make this an extra special birthday."
    "Or at least one that doesn't land me in the dog-house!"
    show kat with dissolve
    kat.say "Hey, [hero.name]..."
    kat.say "You're lucky you got here when you did."
    kat.say "I only just wrapped up a serious session on Residential Wicked!"
    mike.say "I guess so, Kat."
    mike.say "Anyway..."
    mike.say "Grab your stuff and follow me."
    mike.say "Also, prepare to have some serious birthday fun!"
    "Kat crosses her arms over her chest and adopts an awkward pose."
    "Urgh...I guess this is where the question start!"
    show kat surprised
    kat.say "Go where exactly?"
    kat.say "I thought we were going to play some games?"
    menu:
        "Sell Kat on the mystery":
            "I could let Kat's attitude get under my skin."
            "But by now I'm pretty used to the fact that she can be a bit of a brat."
            "So instead of telling her off, I decide to take the opposite approach."
            "Which is to dangle something shiny in front of her."
            mike.say "Oh, we're going to play games alright."
            mike.say "Just not the ones they have around here."
            mike.say "And I guarantee you haven't played these ones too!"
            "Kat frowns and narrows her eyes."
            "Probably because I just appealed to her vanity as a gamer."
            show kat offended
            kat.say "Bullshit!"
            kat.say "I've played every game that's out at the moment."
            show kat happy
            kat.say "And I know nothing's gone under my radar!"
            mike.say "Are you sure about that?"
            mike.say "It'd be a shame if you were to miss out..."
            show kat surprised
            kat.say "Oooh..."
            kat.say "You asshole!"
            show kat happy
            kat.say "Okay, okay...you got me!"
            kat.say "Let's go see what the hell you're even talking about!"
            $ game.active_date.score += 25
        "Tell off for being boring":
            "Kat's attitude instantly flies up my ass."
            "And in the space of a few seconds, I'm in a pretty combative mood."
            "So I strike a similar pose to the one she's pulling."
            mike.say "Why so hostile, Kat?"
            mike.say "I bet you've been here most of the day."
            mike.say "But when I suggest we go somewhere else, you complain!"
            show kat confused
            "Kat shakes her head at this."
            "And she narrows her eyes as she replies."
            kat.say "What's wrong with this place?"
            kat.say "I like it here."
            kat.say "I have a lot of fun here."
            kat.say "And most people don't hassle me here either!"
            mike.say "Look, Kat..."
            mike.say "Are you going to come see where I want to take you or not?"
            mike.say "Because I'm starting to think this was a bad idea!"
            "I can see that Kat knows she's pushing me dangerously close to my limits."
            "So she immediately begins to back down."
            "But of course, she has to dress this up as her doing me a favour."
            kat.say "Okay, okay..."
            kat.say "Geez, man - don't have a coronary!"
            kat.say "Let's go see what's so great about your plans anyway."
            $ game.active_date.score -= 20
    scene bg mall1
    show kat crazy
    with fade
    "When we arrive at the mall, Kat's mood doesn't suddenly improve."
    "Instead she seems to become even more sceptical than before."
    kat.say "The mall?"
    kat.say "What are we doing here?!?"
    kat.say "I thought you said we were going to play games?"
    mike.say "We are!"
    mike.say "Just follow me and we'll be there in no time, I promise."
    "Kat begins to do as I ask."
    "But then she sees a coffee shop up ahead."
    show kat timid
    kat.say "I could do with a shot of caffeine right now!"
    kat.say "Can we stop off and grab one?"
    menu:
        "Get a coffee":
            "I stop and think about it for a moment."
            "And it occurs to me that we're not on that tight of a schedule."
            "So taking a detour for a coffee wouldn't hurt."
            "Plus it'd earn me some points with Kat too."
            mike.say "Sure thing, Kat..."
            mike.say "We can take a few minutes out to sit down too."
            mike.say "If you're okay with that?"
            show kat happy
            "Kat's face breaks into a smile."
            "And she takes my hand, pulling me towards the coffee shop."
            scene bg coffeeshop with fade
            show kat at center, zoomAt(1.0, (640, 720)) with easeinright
            "We head inside and place our orders with the barista."
            show kat at center, traveling(1.5, 1.0, (640, 1040))
            pause 1.0
            show kat at center, zoomAt(1.5, (640, 1140)) with ease
            "Then we grab a table and take our time over drinking our coffee."
            "Which proves to be a good idea."
            "Because it allows Kat to decompress from her time at the gaming arena."
            "That and to fire off a hundred questions at me about where we're headed."
            show kat defiant
            kat.say "Is it the cinema?"
            mike.say "No."
            kat.say "Is it a fancy restaurant?"
            mike.say "No!"
            kat.say "Is it...a comic-book store?"
            mike.say "No, so just wait and see!"
            $ game.active_date.score += 25
        "Don't get a coffee":
            mike.say "Forget about getting your hit right now, Kat!"
            mike.say "There's going to be plenty of time for that later."
            show kat sad
            "Kat scowls and looks towards the coffee shop."
            show kat sadsmile
            kat.say "It's not a big deal, [hero.name]!"
            kat.say "We could be in and out of there in no time."
            kat.say "And it's not like I can't take a coffee in wherever we're going."
            "Now it's my turn to frown at Kat."
            "And I make sure to shake my head too."
            mike.say "I don't know about that..."
            mike.say "And I don't want to take the risk of us not getting in there."
            mike.say "One coffee could derail the whole thing!"
            "Kat grumbles and mutters under her breath."
            "But she seems to be resolved to doing things my way."
            "God's sake - are we ever going to get to where we're going?"
            $ game.active_date.score -= 15
    scene bg mall1 with fade
    show kat normal
    "Finally we arrive out front of the arcade at the mall."
    "And I throw my arms wide, letting Kat know that we're here."
    scene bg arcade
    show kat normal
    with fade
    mike.say "Ta da!"
    mike.say "Happy birthday, Kat!"
    show kat surprised
    kat.say "The arcade?"
    kat.say "Wow..."
    kat.say "I didn't know this place was still here!"
    mike.say "Well it is..."
    mike.say "And you won't find a better selection of retro games anywhere else in town."
    "At the mention of the word retro, Kat looks a little unsure."
    show kat annoyed
    kat.say "I dunno..."
    kat.say "I've always been into the cutting edge of gaming."
    kat.say "Retro stuff kinda puts me off."
    kat.say "But I guess I can give it a go..."
    "I'm going to have to go the extra mile if I want to sell this to Kat."
    "But luckily for me, I'm one charismatic and convincing guy!"
    if kat.love + hero.charm >= 200:
        mike.say "Don't see it as a challenge, Kat."
        mike.say "Instead, look at this as research."
        "Kat stares at me blankly."
        show kat normal
        kat.say "Huh?"
        kat.say "But I play modern videogames."
        kat.say "How is playing old ones going to help with that?"
        mike.say "Think about it, Kat..."
        mike.say "Modern games didn't just appear out of thin air."
        mike.say "There had to be games before them."
        mike.say "Games that they learned from, that they built on to improve."
        "I can see that I'm getting through to Kat."
        "She's nodding, like she's turning the idea over in her head."
        kat.say "You're saying I could get a feel for that, right?"
        kat.say "Like I could understand the games that programmers played as kids?"
        kat.say "Maybe even get a handle on what makes them tick?"
        mike.say "Precisely that, Kat!"
        kat.say "Well come on then - what are we waiting for?"
        $ game.active_date.score += 20
    else:
        mike.say "Don't worry about it, Kat..."
        mike.say "Old-fashioned games are so much simpler than modern stuff."
        mike.say "That means they're much easier to get the hang of playing."
        "Kat nods at this."
        "But she still doesn't look convinced."
        show kat sad
        kat.say "But that's part of the problem, [hero.name]!"
        kat.say "Those games from the past are like, so simple..."
        kat.say "It's almost like they're for babies now!"
        "I know that Kat's trying to be honest, to explain herself."
        "But I can't help reading an insult into her words."
        "One that's aimed at me too."
        mike.say "That's just because you've been spoiled by modern games."
        mike.say "There's a beautiful simplicity to retro games."
        mike.say "One that you have to really try hard to appreciate."
        kat.say "Huh..."
        kat.say "You make it sound like this is going to be really hard."
        kat.say "I thought we were supposed to be having fun?"
        mike.say "Oh, whatever..."
        mike.say "Let's just get the hell inside already!"
        $ game.active_date.score -= 10
    "Once we're in the arcade, I make straight for the vintage arcade cabinets."
    "I can see the way Kat's gazing longingly at the more modern offerings."
    show kat normal
    "Which fills me with the need to get her in front of the best they have to offer."
    "I'm sure that if she plays the right retro games she'll be instantly hooked."
    show kat at center, zoomAt(1.5, (640, 1040)) with fade
    mike.say "You like beat-em-ups, right?"
    kat.say "Erm..."
    kat.say "I like fighting games, sure."
    kat.say "But I'm kind of used to them being three-dimensional!"
    mike.say "I know, I know..."
    mike.say "But the two-dimensional graphics are part of the style!"
    kat.say "If you say so..."
    kat.say "So what's this one all about?"
    mike.say "That's 'Twin Tiamat', Kat!"
    if hero.has_skill("video_games") or kat.love + hero.knowledge >= 200:
        menu:
            "Show your skill at Kat" if hero.has_skill("video_games"):
                mike.say "This is a very old game, Kat."
                mike.say "But one of the things that keeps it popular is the mechanics."
                show kat surprised
                kat.say "You've got to be joking?"
                kat.say "This thing looks like it burns coal to work!"
                mike.say "Seriously, Kat..."
                mike.say "The controls are really sound."
                mike.say "Just wait and see..."
                "I could play this game with my eyes closed."
                "I've done it so many times that I know it inside out."
                "And straight away I give Kat something to aspire to."
                show game arcade kat with fade
                kat.say "Wha..."
                kat.say "Wait..."
                kat.say "How did you do that?!?"
                mike.say "Double tap on the joystick, Kat..."
                mike.say "Just as you press punch."
                kat.say "Okay..."
                kat.say "No...wait..."
                kat.say "I think...yeah, I got it!"
                "We play through the entire game before we're done."
                "Starting to work together as a pretty good team too."
                mike.say "Okay, Kat..."
                mike.say "That guy's the final boss."
                kat.say "The one with the machine gun?"
                kat.say "Wait, didn't he kidnap the girl at the start of the game?"
                kat.say "He's going down for promoting violence against women!"
                "It doesn't take us long to finish the boss off."
                "Which leaves Kat and me to celebrate our victory together."
                $ game.active_date.score += 20
            "Talk about the history of the game" if kat.love + hero.knowledge >= 200:
                mike.say "This one's actually got an interesting history, Kat."
                show kat surprised
                kat.say "Really?"
                mike.say "Oh sure!"
                kat.say "Well, aren't you going to tell me all about it?"
                mike.say "Well, you remember Delinquent Manga?"
                mike.say "About school-boys getting into fights and all that?"
                show kat happy
                kat.say "Oh yeah!"
                kat.say "Weren't those big over there in the last century?"
                mike.say "Yeah, but no need to put it like that, Kat."
                mike.say "Some of us were born back then!"
                mike.say "Anyway..."
                mike.say "They made a game based on that."
                mike.say "Then they changed it around for the Western market."
                mike.say "And 'Twin Tiamat was the result."
                "Kat takes a second look at the game."
                "And I can see she's doing so with a renewed interest."
                kat.say "I suppose it does look kinda cool."
                kat.say "Like one of those retro movies from the eighties."
                mike.say "That's the spirit, Kat."
                mike.say "It's like playing a little piece of history."
                $ game.active_date.score += 20
    else:
        kat.say "So what?"
        kat.say "You want to give it a try?"
        mike.say "Of course I do, Kat..."
        mike.say "I love this game!"
        show game arcade kat with fade
        "I stick a couple of quarters into the machine."
        menu:
            "Try hard vs Kat":
                kat.say "So what..."
                kat.say "We just beat these guys up?"
                mike.say "The clue's in the name, Kat..."
                mike.say "It's a beat-em-up!"
                "Kat nods and we get down to the task of kicking ass."
                "But she just doesn't seem to be able to get into it."
                "Like the controls and the flow of the game escape her."
                "Pretty soon she's losing lives and falling behind."
                kat.say "So what happens now that we killed all the bad guys?"
                mike.say "Now we have to fight each other."
                kat.say "Oh...okay."
                "Kat hesitates for a moment, and that's the only chance I need."
                "Before I can really think of the consequences, I'm beating her hands down."
                "And it doesn't take long for me to come out as the winner."
                mike.say "Erm..."
                mike.say "Looks like I beat you!"
                kat.say "Yeah...you sure kicked my ass!"
                kat.say "Way to make my birthday special..."
                $ game.active_date.score -= 20
            "Let Kat win":
                kat.say "So what..."
                kat.say "We just beat these guys up?"
                mike.say "The clue's in the name, Kat..."
                mike.say "It's a beat-em-up!"
                "Kat nods and we get down to the task of kicking ass."
                "But she soon proves to be far better at it than me."
                "Like something just clicks for her."
                "And before too long, she's pulling ahead."
                kat.say "So what happens now that we killed all the bad guys?"
                mike.say "Now we have to fight each other."
                kat.say "Oh...okay."
                "Without hesitation, Kat begins to do just that."
                "Her sprite lays into mine mercilessly."
                "And I get the exact same treatment as the bad guys."
                kat.say "Erm..."
                kat.say "Looks like I beat you!"
                mike.say "Yeah...you sure kicked my ass!"
                $ game.active_date.score += 10
    hide game arcade
    show kat at center, zoomAt(1.5, (640, 1040))
    with fade
    "Kat spots something that seems to interest her ."
    "And she hurries over to get a closer look."
    "I follow, already knowing what it is."
    show kat surprised
    kat.say "Geez..."
    kat.say "These things look like real guns!"
    "Kat's pointing at the replica machine guns attached to the cabinet."
    mike.say "Yeah, they're pretty hardcore!"
    mike.say "This one's called 'Operation Wolverine'."
    mike.say "And those are light-guns."
    kat.say "Now this one looks interesting."
    kat.say "Can we play it?"
    mike.say "Of course we can, Kat."
    mike.say "That's what we came here to do."
    show game arcade kat with fade
    menu:
        "Take the blue gun":
            "Kat and I each grab one of the light-guns."
            "And then I pump coins into the slot."
            "There's a brief introduction."
            "And then we're into the shooting."
            kat.say "Hey..."
            kat.say "This is pretty fun!"
            kat.say "I mean, it's really dumb - like an eighties action flick."
            kat.say "But still fun!"
            "I nod in agreement."
            "But Kat's good mood doesn't seem to last."
            "Because she's seriously fucking up at playing the game."
            "She can't seem to hit any of the cartoonish terrorists."
            "And every hostage that runs on screen somehow ends up in her line of fire."
            mike.say "Erm..."
            mike.say "You do realise that you're supposed to be saving those guys?"
            mike.say "Not shooting them all?"
            kat.say "Hey!"
            kat.say "Get off my back!"
            kat.say "I never even played this game before."
            $ game.active_date.score -= 10
        "Take the red gun":
            "Kat and I each grab one of the light-guns."
            "And then I pump coins into the slot."
            "There's a brief introduction."
            "And then we're into the shooting."
            kat.say "Hey..."
            kat.say "This is pretty fun!"
            kat.say "I mean, it's really dumb - like an eighties action flick."
            kat.say "But still fun!"
            "I nod in agreement."
            "But I'm finding it hard to actually say anything."
            "Because I'm seriously fucking up at playing the game."
            "I can't seem to hit any of the cartoonish terrorists."
            "And every hostage that runs on screen somehow ends up in my line of fire."
            kat.say "Erm..."
            kat.say "Aren't you supposed to be saving those guys?"
            kat.say "Not shooting them all?"
            mike.say "I know, I know..."
            mike.say "I'm just not on form today!"
            $ game.active_date.score += 20
    hide game arcade
    show kat at center, zoomAt(1.5, (640, 1040))
    with fade
    "Once Kat and I have played every game that catches our eye, it's time for a break."
    "So we head to a quiet part of the arcade where we can tune back into reality."
    "I'm still buzzing from the adrenaline of playing so many great games."
    "And I'm hoping that she feels the same way too."
    "But right now it seems like there's something she wants to ask me."
    mike.say "What is it, Kat?"
    mike.say "I know that look!"
    show kat shy
    kat.say "Oh..."
    kat.say "Well..."
    kat.say "It is my birthday, [hero.name]."
    kat.say "I wondered if you got anything for me?"
    if not hero.has_gifts:
        "Ah, shit..."
        "I knew there was something that I'd forgotten!"
        "I guess that all I can do now is try to cover up my mistake."
        mike.say "I already gave you your present, Kat."
        mike.say "All of the great memories that we've made today!"
        mike.say "Ones that you'll remember for years to come."
        show kat sad
        "Kat looks a little disappointed with this answer."
        "But she does the best she can to hide it from me."
        kat.say "Oh yeah..."
        kat.say "Of course..."
        kat.say "Thanks, [hero.name]."
        $ game.active_date.score -= 20
        $ kat.love -= 10
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_24
        if _return != "done":
            if _return not in ["None", "exit"]:
                mike.say "Don't worry, Kat..."
                mike.say "The trip to the arcade isn't your actual present."
                mike.say "I got you a little something to unwrap too."
                show kat happy
                "Kat's face lights up as I hand over the gift."
                play sound [paper_ripping_2, paper_ripping_1]
                "And she wastes no time in tearing off the paper."
                kat.say "Thanks, [hero.name]!"
                kat.say "That's so great of you!"
                if _return:
                    "As soon as she sees what's inside, Kat's face lights up."
                    kat.say "Oh wow!"
                    kat.say "Where did you find one of these?"
                    kat.say "I've always wanted one!"
                    "I can't keep a smile from spreading across my face."
                    "And basking in the glory of Kat's reaction."
                    mike.say "It was nothing, Kat."
                    mike.say "All worth it to see the look on your face."
                    $ game.active_date.score += 20
                else:
                    show kat sadsmile
                    "But as soon as she sees what's inside, Kat's face drops."
                    kat.say "Oh..."
                    kat.say "That's..."
                    kat.say "That's great..."
                    "It's pretty obvious that Kat hates what I bought her."
                    "And even though she tries to hide it, I know that I fucked up."
                    "So all I can do is force a smile onto my face and try to move on."
                    $ game.active_date.score -= 10
            else:
                "Ah, shit..."
                "I knew there was something that I'd forgotten!"
                "I guess that all I can do now is try to cover up my mistake."
                mike.say "I already gave you your present, Kat."
                mike.say "All of the great memories that we've made today!"
                mike.say "Ones that you'll remember for years to come."
                show kat sad
                "Kat looks a little disappointed with this answer."
                "But she does the best she can to hide it from me."
                kat.say "Oh yeah..."
                kat.say "Of course..."
                kat.say "Thanks, [hero.name]."
                $ game.active_date.score -= 20
                $ kat.love -= 10
    mike.say "So..."
    mike.say "I think we already played every game here, Kat."
    mike.say "Well...at least every decent one!"
    show kat normal
    "Kat nods and takes a deep breath."
    "Then she lets it out."
    "And the weariness in it is plain to hear."
    kat.say "Yeah, [hero.name]."
    kat.say "I think I'm all gamed out!"
    "I nod, more than ready to take a break from the arcade."
    mike.say "What do you want to do now?"
    mike.say "It's not too late to get something else in before we call it a day."
    mike.say "Are you up for that?"
    if game.active_date.score >= 80 and kat.sexperience >= 1:
        "Kat begins to nod her head eagerly."
        show kat happy
        kat.say "Sure, [hero.name]..."
        kat.say "I'm not ready to quit yet!"
        kat.say "In fact, I have an idea for what I want to do next."
        "Of course, that was just the answer that I wanted to hear."
        "And I'm practically beaming as Kat grabs my hand."
        "Then I let her lead me off wherever she's going."
        "Because it's a thrilling change to let her make the decisions."
        "Especially after I organised everything else today."
        "I just hope that whatever she has in mind, it's going to be fun."
        call kat_birthday_sex from _call_kat_birthday_sex
    else:
        "Kat kind of screws her face up."
        "And then she shakes her head."
        show kat sadsmile
        kat.say "Nah..."
        kat.say "I'm just about burnt out."
        kat.say "And I could do with getting some rest."
        "That's not exactly the answer I wanted."
        "But I don't let it show."
        "Instead I nod in agreement."
        mike.say "No worries, Kat."
        mike.say "Let's see about getting you home..."
        "I can understand her feeling tired after all we've done today."
        "But I hope that it's only because of that she's calling time on our date."
        "And that it's not something I did, or forgot to do which is to blame."
    return

label kat_birthday_sex:
    scene bg livingroom
    show kat happy
    with fade
    "I think I have a pretty good idea of what Kat's got in mind."
    "But as we pull up outside my place, I decide to play it cool."
    "No sense in pouncing on her the moment that we're inside."
    "And then finding out that she just wanted to see my anime collection!"
    "So as I close the front door, I'm still trying to act all casual."
    mike.say "So, Kat..."
    mike.say "Here we are..."
    mike.say "What are we going to do?"
    show kat defiant
    "By way of answer, Kat gives me a mischievous smile."
    "And she saunters off towards the sitting room."
    hide kat with easeoutleft
    "Then she disappears through the door, beckoning for me to follow."
    scene bg bedroom1
    with fade
    "Of course I don't hesitate to hurry after her."
    "Because I'm already feeling more than a little aroused by her teasing."
    show kat happy at center, zoomAt (1.0, (640, 820)) with fade
    "Once I round the door, I find Kat kneeling on the floor."
    "She seems to be checking out the consoles set up in the room."
    "And I feel my heart sink as the possibility of fooling around appears to fade."
    mike.say "Ah..."
    mike.say "You wanted to check out my Z-Box?"
    mike.say "I thought I already told you all about it, Kat?"
    "At the sound of my voice, Kat turns to look over her shoulder."
    "Then she slowly turns the rest of her body so that she's facing me."
    "She doesn't get up, but instead beckons me to come join her on the floor."
    kat.say "You did, [hero.name]."
    kat.say "But that's not the kind of game I want to play tonight."
    kat.say "We already spent the entire day on video-games."
    kat.say "Now I want to play games of a different kind..."
    "Kat doesn't leave anything to chance when it comes to her meaning."
    "Because the moment she's done saying her piece, she starts to strip off."
    "Right there, in the middle of the floor."
    "I watch as she pulls off her top and tosses it aside."
    "The movement makes her breasts bounce inside of her bra."
    show kat topless with dissolve
    "But a moment later she unhooks it and sets them free."
    "Kat turns her attention to undressing below the waist."
    "But that's the moment that I choose to make my own move."
    "It only takes me a couple of seconds to take off my own clothes."
    "And then I pretty much throw myself onto the floor by Kat."
    "She yelps in surprise as I lean forwards and begin to kiss her breasts."
    "The sound doesn't stop me, only makes me all the more determined."
    "Now I have one of her nipples between my lips."
    "And the other I'm pinching with my fingers."
    "I feel them stiffening as Kat's yelps become moans of pleasure."
    show kat naked with dissolve
    "Somehow she still manages to strip off the rest of her clothes."
    "But I only know this because she's naked when she clambers onto me."
    "I can feel the warmth of her smooth skin as she pushes me down."
    "And I'm happy to let her do so, releasing her nipple as I surrender."
    "I look up at Kat as she rears up above me."
    "Her cheeks are flushed red and her violet hair is in disarray."
    "But from the look in her eyes, I know that she's intent upon what she wants."
    "That notion is confirmed a moment later when she reaches out."
    "And without asking permission, clamps a hand on my cock."
    "Kat grabs it close to the base, holding it firmly."
    "It's not enough for the hold to be painful."
    "Yet it instantly sends a thrill of pleasure through my entire body."
    "And I can't keep myself from shuddering at the sensation."
    show kat defiant
    kat.say "Oh..."
    kat.say "You like that, huh?"
    kat.say "You like me playing with your joystick?"
    "Sure, it's a pretty obvious line."
    "Even a corny way to talk about sex."
    "But somehow, coming out of Kat's mouth, it just works."
    mike.say "Oh yeah, Kat!"
    mike.say "I really want you to play with me!"
    mike.say "To get a high-score too!"
    "Oh man..."
    "We have to get down to it soon."
    "Because this is getting to be a pretty cringe conversation!"
    "Luckily for me, Kat seems more than keen to get it on."
    "She starts rubbing her hand up and down the shaft of my cock."
    "At the same time she starts wiggling her ass."
    "And I can feel that she's gearing herself up for it."
    "A moment later, Kat gets up on her knees."
    "And she shuffles forwards so that she's right over my cock."
    hide kat
    show kat cowgirl
    with fade
    "She wastes no time in beginning to rub the head against her pussy."
    "The lips are already beginning to look slick, like she's getting wet."
    "And now there's no chance of me uttering any more cheesy lines."
    "Because all of my attention is focussed on Kat's pussy."
    "She seems fully aware of this, as I can hear her giggling."
    "Obviously she likes being the centre of my attention."
    "And she's getting off on teasing me too!"
    kat.say "Mmm..."
    kat.say "I'm ready, [hero.name]."
    kat.say "How about you?"
    kat.say "Are you ready for me?"
    kat.say "Do you want me?"
    "I swallow audibly and nod."
    "My eyes feel like they're popping out of my head."
    "My heart is hammering inside of my chest."
    "If I don't get what she's teasing me with soon..."
    "I'm sure a vein in my brain is going to pop!"
    "Thankfully, Kat seems to feel like she's teased me enough."
    show kat cowgirl eyes_close mouth_pleasure vaginal
    "So she begins to lower herself onto me."
    "If I thought that I was gasping and panting before, I was wrong."
    "Because now I'm really feeling my body come to life."
    "Even the resistance from Kat's muscles drives me crazy."
    "I hold my breath as her pussy tries to keep me out."
    "And when it finally gives way, my cock begins to inch its way inside."
    "That sensation makes me release the air in my lungs as a huge groan."
    show kat cowgirl eyes_open mouth_open
    "Kat smiles at the sound, but not the mischievous grin she wore before."
    "Now her smile is knowing and almost wicked in nature."
    "Now she knows that she has me in the palm of her hand."
    "And I can tell that she intends to make good use of that power too!"
    "Kat plants her hands on my chest, spread wide apart."
    "And she lowers herself down until I fill her completely."
    "She pauses for a moment, maybe to savour the feeling."
    "Or maybe to allow me to do the same, teasing again."
    show kat cowgirl eyes_up mouth_hurt
    "Then, without warning, she launches into it."
    "Suddenly, I find myself being ridden with a desperate passion."
    "And there's a strength in Kat's petite frame too."
    "One that catches me totally off-guard."
    "Rather than being weak, those little muscles are wiry."
    "They seems to possess a power that's completely unexpected too."
    show kat cowgirl eyes_close mouth_hurt
    "Kat slams herself down on me, then bounces back up again."
    show kat cowgirl eyes_close mouth_open
    "One motion seems to feed into the other, creating a loop."
    show kat cowgirl eyes_open mouth_open
    "And it's one that feeds on itself too, getting more intense with each repetition."
    show kat cowgirl eyes_close mouth_open at startle(0.05,-10)
    "Soon enough, Kat's pinning me down on the floor."
    "Her buttocks slapping against my naked thighs."
    show kat cowgirl eyes_open mouth_pleasure
    "I reach up with my hands, putting them all over her body."
    "But inevitably they gravitate towards her breasts."
    show kat cowgirl at startle(0.05,-10)
    "The speed at Kat's going at means they're jiggling like crazy."
    "And I find the mere sight of them hypnotic."
    show kat cowgirl at startle(0.05,-10)
    "Now that my hands are on them again, I can't help myself."
    "I caress, squeeze and pinch without mercy."
    "And it doesn't take long for this to have a visible effect."
    show kat cowgirl at startle(0.05,-10)
    "Where before Kat was simply riding me, she now begins to slow a little."
    show kat cowgirl eyes_open mouth_open
    "Not by much, she's still going up and down at an astonishing speed."
    "But the sensations of me playing with her breasts are affecting her too."
    "Now she seems to be nodding, moaning in response to my attentions."
    "And for the first time, I feel like I have a measure of control."
    "Apologies for returning to the gaming imagery."
    "But if Kat's treating my cock like a joystick..."
    show kat cowgirl eyes_up mouth_hurt
    "Then her nipples are my joypad!"
    show kat cowgirl at startle(0.05,-10)
    "I keep on tweaking and tapping."
    "And pretty soon I know that she's not going to be able to keep it up."
    "Already I can see Kat shaking her head and whimpering."
    show kat cowgirl at startle(0.05,-10)
    "She's doing all she can to hold on."
    "But she's going to cum any second."
    "The knowledge should be empowering me."
    "Yet instead it pushes me over the edge too."
    show kat cowgirl at startle(0.05,-10)
    "In that moment I know I'm going to cum too."
    "And there's nothing I can do to stop it either."
    show kat cowgirl eyes_up mouth_pleasure
    show kat cowgirl at startle(0.05,-10)
    "In the end, I don't know which one of us actually cums first."
    "But the moment they do, the other is dragged into it as well."
    "Kat's pussy clenches, her entire body shuddering."
    show kat cowgirl eyes_close mouth_open cum with vpunch
    "At the same time I stiffen, shooting my load."
    with vpunch
    "Those seconds seem to stretch into a far longer period of time."
    with vpunch
    "Then reality catches up to us, and we snap back into the moment."
    "Kat collapses atop me, wriggling and squirming in the afterglow."
    "But I realise that we need to act fast."
    "We need to get dressed again and hide the evidence."
    "Before one of my housemates walks in and catches us."
    "All the same, we separate and dress with smiles on our faces."
    "Our heads filled with memories of what we just did together."
    $ kat.sexperience += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
