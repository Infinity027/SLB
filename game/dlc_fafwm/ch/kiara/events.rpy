init python:
    Event(**{
    "name": "kiara_unhide",
    "label": "kiara_unhide",
    "conditions": [
        IsDone("bree_event_09b"),
        HeroTarget(
            IsGender("male"),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kiara_event_02",
    "label": "kiara_event_02",
    "duration": 1,
    "conditions": [
        IsDone("bree_event_09b"),
        IsHour(17, 19),
        HeroTarget(
            IsGender("male"),
            IsRoom("maidcafe"),
            MinStat("charm", 50),
            IsActivity("None"),
            ),
        PersonTarget(kiara,
            MinStat("love", 20),
            IsFlag("kiaradelay", False),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/focus.ogg",
    })

    Event(**{
    "name": "kiara_event_03",
    "label": "kiara_event_03",
    "conditions": [
        IsDone("kiara_event_02"),
        HeroTarget(
            IsGender("male"),
            IsRoom("stripclub"),
            IsActivity("None"),
            ),
        PersonTarget(kiara,
            MinStat("love", 40),
            IsFlag("kiaradelay", False),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/focus.ogg",
    })

    Event(**{
    "name": "kiara_event_04",
    "label": "kiara_event_04",
    "duration": 1,
    "conditions": [
        IsDone("kiara_event_03"),
        IsHour(21, 2),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(kiara,
            Not(IsPresent()),
            MinStat("love", 60),
            IsFlag("kiaradelay", False),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/focus.ogg",
    })

    Event(**{
    "name": "kiara_event_05",
    "label": "kiara_event_05",
    "duration": 1,
    "conditions": [
        IsDone("kiara_event_04"),
        IsHour(21, 2),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(kiara,
            MinStat("love", 80),
            IsFlag("kiaradelay", False),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/focus.ogg",
    })

    Event(**{
    "name": "kiara_event_06",
    "label": "kiara_event_06",
    "duration": 1,
    "conditions": [
        IsDone("kiara_event_05"),
        IsHour(21, 22),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(kiara,
            MinStat("love", 100),
            IsFlag("kiaradelay", False),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/focus.ogg",
    })

    Event(**{
    "name": "kiara_event_07",
    "label": "kiara_event_07",
    "duration": 1,
    "conditions": [
        IsDone("kiara_event_06"),
        IsNotDone("kiara_event_07b"),
        IsHour(12, 18),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_mall1"),
            ),
        PersonTarget(kiara,
            MinStat("love", 120),
            MaxStat("sub", -1),
            OnDate(),
            IsFlag("kiaradelay", False),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/focus.ogg",
    })

    Event(**{
    "name": "kiara_event_08",
    "label": "kiara_event_08",
    "duration": 1,
    "conditions": [
        IsDone("kiara_event_07"),
        IsHour(22, 4),
        HeroTarget(
            IsGender("male"),
            IsRoom("nightclub"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(kiara,
            MinStat("love", 140),
            IsFlag("kiaradelay", False),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/focus.ogg",
    })

    Event(**{
    "name": "kiara_event_09",
    "label": "kiara_event_09",
    "duration": 1,
    "conditions": [
        IsDone("kiara_event_08"),
        IsHour(22, 4),
        HeroTarget(
            IsGender("male"),
            IsRoom("nightclub"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(kiara,
            MinStat("love", 160),
            IsFlag("kiaradelay", False),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/focus.ogg",
    })

    Event(**{
    "name": "kiara_event_07b",
    "label": "kiara_event_07b",
    "duration": 1,
    "conditions": [
        IsDone("kiara_event_06"),
        IsNotDone("kiara_event_07"),
        IsHour(12, 18),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_mall1"),
            ),
        PersonTarget(kiara,
            MinStat("love", 120),
            MinStat("sub", 0),
            OnDate(),
            IsFlag("kiaradelay", False),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/focus.ogg",
    })

    Event(**{
    "name": "kiara_event_08b",
    "label": "kiara_event_08b",
    "duration": 1,
    "conditions": [
        IsDone("kiara_event_07b"),
        IsHour(10, 18),
        IsSeason(0, 1, 2),
        HeroTarget(
            IsGender("male"),
            IsRoom("park"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(kiara,
            MinStat("love", 140),
            IsFlag("kiaradelay", False),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/focus.ogg",
    })

    Event(**{
    "name": "kiara_event_09b",
    "label": "kiara_event_09b",
    "duration": 1,
    "conditions": [
        IsDone("kiara_event_08b"),
        IsHour(22, 2),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            Not(IsRoom("housemap")),
            Not(IsRoom("house")),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(kiara,
            MinStat("love", 160),
            IsFlag("kiaradelay", False),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/focus.ogg",
    })

    Event(**{
    "name": "kiara_preg_talk",
    "label": "kiara_preg_talk",
    "do_once": False,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(kiara,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("toldpreg", False),
            MinCounter("pregnant", 6),
            ),
        ],
    "music": "music/roa_music/focus.ogg",
    })

    Event(**{
    "name": "kiara_sub_event_01",
    "label": "kiara_sub_event_01",
    "duration": 1,
    "conditions": [
        IsDone("kiara_event_06"),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget("kiara",
            IsPresent(),
            Not(IsHidden()),
            MinStat("sub", 25),
            MinStat("sexperience", 1),
            IsFlag("kiaradelay", False),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/focus.ogg",
    })

    Event(**{
    "name": "kiara_sub_event_02",
    "label": "kiara_sub_event_02",
    "duration": 1,
    "conditions": [
        IsDone("kiara_sub_event_01"),
        HeroTarget(
            IsGender("male"),
            Or(
                HasRoomTag("home"),
                HasRoomTag("club"),
                IsRoom("maidcafe"),
                ),
            ),
        PersonTarget("kiara",
            MinStat("sub", 50),
            IsFlag("kiaradelay", False),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/focus.ogg",
    })

    Event(**{
    "name": "kiara_sub_event_03",
    "label": "kiara_sub_event_03",
    "duration": 1,
    "conditions": [
        IsDone("kiara_sub_event_02"),
        HeroTarget(
            IsGender("male"),
            Or(
                HasRoomTag("club"),
                IsRoom("maidcafe", "stripclub"),
                ),
            ),
        PersonTarget("kiara",
            MinStat("sub", 75),
            IsPresent(),
            IsFlag("kiaradelay", False),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/focus.ogg",
    })

label kiara_unhide:
    $ kiara.unhide()
    return

label kiara_event_02:
    if kiara.love.max < 40:
        $ kiara.love.max = 40
    $ game.room = "maidcafe"
    scene bg maidcafe with fade
    "It's getting to the time when the café usually closes for the day, and the last customers are drifting out of the place."
    "Which is a relief for me, as I'm more than ready to head home and devote myself to the important task of totally relaxing."
    "But just as I'm about to grab my things and head for the door too, I hear the sound of tapping on the counter."
    "It's way too loud and close by to be a sound that's being made unconsciously, and so it causes me to look up."
    show kiara work a dreaming at center, zoomAt(1.0, (1040, 760)) with dissolve
    "And that's when I see Kiara, drumming her long, exquisitely manicured nails on the surface of the counter."
    show kiara normal
    "As soon as our eyes meet, one corner of her mouth twists into a grin, and raises an eyebrow too."
    "And with the other hand, she crooks her index-finger, beckoning for me to follow."
    show kiara talkative a
    kiara.say "[hero.name]…"
    kiara.say "I want to talk to you about Bree."
    kiara.say "But I want to do so in private."
    show kiara normal
    pause 0.3
    hide kiara with easeoutright
    "With that, Kiara slips silently into the back of the place, obviously expecting me to be right behind her."
    "I only have time for a quick glance around the café before I get up and do as I'm told."
    "And that tells me the place is more than empty enough to mean we can both duck out of sight for a moment."
    scene bg maidcafeback
    show kiara work normal at center, zoomAt(1.25, (640, 880))
    with fade
    "So I hurry after Kiara into the space at the back of the café, already wondering what this is all about."
    "Like, what could she possibly want to ask me about Bree?"
    "I was sure that she really fit in well here, that she was slaying it as a waitress."
    mike.say "Erm..."
    mike.say "So, Kiara..."
    mike.say "What's up with you and Bree?"
    "Kiara has her back to me as I begin stumbling over my questions."
    "And she seems happy to let me get all of them out before she even turns around."
    show kiara mischievous
    "But when she does so, I almost feel like taking a step backwards."
    "Because somehow her whole demeanour seems to change as she does so."
    "Gone is the happy-go-lucky lady that I'm used to seeing running the café."
    "And in her place is what I can only describe as a woman that asserts her dominance with a mere glance."
    show kiara talkative
    kiara.say "Oh, there's no issue with Bree, [hero.name], none at all."
    kiara.say "That was just a ruse, a little play to get you alone."
    show kiara normal
    "As if such a bald admission of subterfuge wasn't unsettling enough, Kiara doesn't stand still as she makes it."
    show kiara at slide(150, 10.0)
    "Instead she begins to walk slowly around me, looking me up and down as she does so."
    "Blinking and shaking my head, I do the best I can to follow her progress and hold her eye."
    "Not that it seems to dissuade her in the slightest or stop her studying me intently."
    mike.say "What..."
    mike.say "What's this all about, Kiara?"
    mike.say "Did I do something to piss you off?"
    mike.say "Because if that's it, I had no idea!"
    show kiara mischievous
    "Kiara narrows her eyes as I begin to talk, in danger of it turning into helpless babbling."
    "She inclines her head, like she's considering what I'm saying with genuine interest."
    "But I note that she neither shakes nor nods her head, keeping me in the dark."
    show kiara talkative
    kiara.say "This isn't about anything like that, [hero.name]."
    kiara.say "No, it's about my own curiosity."
    kiara.say "My insatiable curiosity to know you better."
    kiara.say "To understand who you are and what makes you tick!"
    show kiara mischievous
    "By now, and even in my confused state of mind, I'm starting to get where this is going."
    "The way that Kiara's isolated me and deliberately caught me off-guard."
    "And now the admission that she's insanely curious about little old me."
    "This is all some kind of psychological game that she's getting off on playing."
    "Obviously it's predicated on the fact that she's stunningly beautiful and beguilingly exotic too."
    "But what I have to work out is how I want to play the game myself."
    "What cards I might have in my hand and whether I want to play to win, or fold completely."
    menu:
        "Try to keep things respectful":
            "Okay, let's get one thing straight here - I am totally intrigued by all of this."
            "Suddenly Kiara's gone from the hot woman that runs the café to someone with a genuine interest in me."
            "And so I am very interested in where this thing could be headed right now."
            "But the flip-side of that is me wanting to stay in control at the same time."
            "So whatever kind of emotional games and mind-tricks she's playing on me, I have to fight back a little."
            mike.say "That's cool, Kiara..."
            mike.say "And for the record, I feel the same way about you."
            "I can tell that Kiara's doing all she can to maintain her cool, calculating demeanour."
            show kiara normal
            "But even she can't prevent her eyebrows from rising as I make my subtle little riposte."
            show kiara talkative
            kiara.say "Oh, is that so?"
            kiara.say "Or are you just admitting that you've been checking me out?"
            kiara.say "Because that's something that almost every guy who comes in here does."
            kiara.say "And it's nothing at all like the kind of curiosity I possess for you."
            show kiara normal
            "Okay, so now we're really getting into it."
            "Kiara's fired the opening barrage, and I've returned fire."
            "Now she's taking things to the next level."
            mike.say "Oh no, Kiara..."
            mike.say "You've already got lots of cutesy little girls working for you here."
            mike.say "And they're all dressed up in such pretty outfits too."
            mike.say "If all I wanted to do was eye-up bimbos, they'd be more than enough for me."
            mike.say "No, I'm more intrigued by the woman that's pulling their strings."
            mike.say "Interested in getting to know her better as a friend."
            show kiara mischievous at zoomAt(1.25, (640, 880)) with ease
            "This seems to do the trick, as Kiara finally stops circling me."
            "And now she's looking me straight in the eye."
            "Almost like she's in the presence of an equal."
            kiara.say "Hmm..."
            show kiara talkative
            kiara.say "You almost took the words out of my mouth, [hero.name]."
            kiara.say "Because I think that's what I would like too."
            show kiara normal
            $ kiara.love += 4
        "Challenge Kiara's dominance":
            "Oh man, I am really loving this side of Kiara."
            "It's way more interesting than the face she puts on while running the café."
            "But that doesn't mean I'm into the idea of her totally dominating me like this."
            "In fact, there's a big part of me that's starting to see her as a challenge."
            "That makes me want to see if I can't conquer that confidence of hers."
            mike.say "Interesting that you had to call me back here to admit all of that, Kiara."
            mike.say "If you're so sure of yourself, why didn't you just say it out there?"
            mike.say "Or are you only really this confident when things are one-on-one?"
            show kiara fantasize at zoomAt(1.25, (640, 880)) with ease
            "Kiara seems to be waiting for the chance to come out with her next line."
            "No doubt a preprepared one, as I'm starting to think she's done this before."
            "Hell, she's probably stunned a long line of guys into submission with this act."
            "But my throwing it back in her face seems to have screwed-up her equilibrium."
            show kiara talkative
            kiara.say "I..."
            kiara.say "I don't know what you mean by that!"
            kiara.say "This is a private matter - between you and me, [hero.name]."
            kiara.say "Not a matter for everyone in the café to see and hear."
            show kiara sadsmile
            "I can feel the knowing smile spreading across my face as Kiara says all of this."
            "And it's more on account of the change in her tone than her actual choice of words."
            "For the first time I can hear doubt in Kiara's voice, that she's unsure of being in control."
            "Sure, that doesn't mean that I'm now in total control of the situation."
            "But it does mean that there's everything to play for."
            mike.say "Oh, I think you do know what I mean, Kiara."
            mike.say "You know that I'm as intrigued by you as you are by me."
            mike.say "And now that we've both admitted as much..."
            mike.say "Well, we're going to be going on a journey of mutual discovery, aren't we?"
            "Kiara's still looking me in the eye as I say all of this."
            "And it comes as a relief when she finally nods."
            show kiara talkative
            kiara.say "Yes, [hero.name]…"
            kiara.say "I believe that is what's happening here."
            show kiara normal
            $ kiara.sub += 4
        "Submit to Kiara's challenge":
            "It's times like these when I feel like there's nothing I can do to escape my fate."
            "Like, one moment I feel totally in control of where my life is headed."
            "And the next, something just reaches out and grabs me, pulling me in a totally different direction."
            "Just for the record, this is the latter - and Kiara's what's grabbed hold of me!"
            "A few minutes ago, she was simply the hot woman that runs the café."
            "But now she's a beautiful, beguiling creature casting a spell of intrigue."
            "And one that's inexplicably interested in me!"
            mike.say "Y...you really mean that, Kiara?"
            mike.say "Why would you be interested in a guy like me?"
            "It's all that I can do to keep my voice from shaking as I ask the question."
            "But my distinct lack of confidence doesn't seem to bother Kiara in the slightest."
            show kiara mischievous at zoomAt(1.25, (640, 880)) with ease
            "In fact, I feel my heart almost leap as she smiles at my stumbling tone."
            show kiara talkative
            kiara.say "Aww..."
            kiara.say "You are so sweetly innocent, [hero.name]!"
            kiara.say "I see how you look at me when we are out there."
            kiara.say "And I see also how you turn your gaze away when you think I notice."
            kiara.say "Your desire is plainly written upon your face, right there for me to see."
            kiara.say "And yet you cannot believe I might be looking at you in the same way?"
            show kiara mischievous at traveling(1.0, 0.5, (640, 720))
            "I can feel myself beginning to blink and get flustered at all Kiara's saying."
            show kiara normal
            "And she must be picking up on it too, because she instantly begins to back off."
            "She takes a step backwards and changes her tone, becoming more friendly than flirty."
            show kiara talkative
            kiara.say "But I am getting ahead of myself, as I sometimes do."
            kiara.say "What I mean to say is that I want to get to know you, [hero.name]."
            kiara.say "That I want us to become friends - good friends."
            kiara.say "Would you like that?"
            show kiara normal
            "I somehow manage to nod my head and blurt out a couple of coherent words."
            mike.say "Y...yes!"
            mike.say "I'd like that..."
            mike.say "I'd like it a lot!"
            $ kiara.sub -= 4
    show kiara mischievous at traveling(1.0, 0.5, (940, 720))
    "Kiara nods as she strides to one side of the room and picks up a bottle."
    show kiara mischievous at traveling(1.5, 0.5, (640, 1040))
    "Then she pours a measure into two glasses and offers one to me."
    "I take it as she lifts her own glass, as if proposing a toast."
    "And not knowing what else to do, I mirror the gesture."
    show kiara talkative
    kiara.say "So be it, [hero.name]…"
    kiara.say "From this moment on, we are more than mere acquaintances."
    kiara.say "Now we are friends, and our voyage of mutual discovery begins."
    kiara.say "But be warned - people who wander into my world rarely leave unchanged!"
    show kiara normal
    "Okay, that's probably the single most weird and cryptic thing I ever heard."
    "And I have no possible way of knowing what Kiara really means by it."
    "So instead of asking, I just take a sip from my glass and give her a smile."
    "Because there's no doubt in my mind that I'll find out further down the line."
    $ kiara.unhide()
    $ kiara.flags.kiaradelay = TemporaryFlag(True, 2)
    scene bg black with dissolve
    $ game.room = "street"
    return

label kiara_event_03:
    if kiara.love.max < 60:
        $ kiara.love.max = 60
    $ game.room = "stripclub"
    scene bg alley with fade
    "Normally when I'm feeling stressed out or tired, I'd just spend the evening playing videogames."
    "Or maybe nip down to The Winchester for a couple of pints if that wasn't quite enough to sort it."
    "But sometimes I'm just feeling so wound up and worn out that it takes something a little more potent."
    "And no, I'm not talking about anything addictive or flagrantly illegal here."
    "Though at times it might come close to that..."
    "No, what I needed tonight was a quick trip to my friendly local strip-club."
    "That handy place where a weary guy can go to recharge his batteries by staring at the female form."
    "And before you go calling me some kind of sexist or pervert, remember that this is purely therapeutic."
    "No different to me popping along to the nearest spa and hopping into the sauna or plunge-pool!"
    scene bg stripclub with fade
    "Anyway, once I'm past the cunningly-shaved gorillas working the door, I can finally relax."
    "And as I walk into the strip-club and head for the bar, I swear I can already feel the good it's doing me."
    "That is until I almost bump into a woman already standing at the bar and with her back turned."
    "I don't actually make contact with her, more pull back before that can happen."
    "But the both of us end up almost leaping back a few feet at the same time."
    mike.say "Whoops..." with hpunch
    mike.say "Sorry about that, lady..."
    mike.say "I was just trying to..."
    "It's just as I'm trying to explain myself that I get my first look at the woman's face."
    "And when I do, I feel like I've been slapped across the cheeks, I'm so surprised."
    show bg stripclub at center, zoomAt(1.4, (400, 820))
    show kiara work at center, zoomAt(1.8, (740, 1120))
    mike.say "Kiara?" with hpunch
    mike.say "What are you doing here?!?"
    "It doesn't take long for my surprise to become mingled with embarrassment too."
    "Because I find myself looking a the owner of the Maid Cafe where my housemate works."
    "And so there's a very real possibility of Bree discovering that I come here on a regular basis!"
    show kiara talkative
    kiara.say "Oh, hello, [hero.name]..."
    kiara.say "I was not expecting to see you here!"
    show kiara normal
    "Part of me is instantly thrown off by just how calm and collected Kiara seems to be right now."
    "I was kind of hoping that she's be every bit as embarrassed as I am to be spotted here."
    "But instead she seems to be totally nonchalant and unconcerned about the whole thing."
    "And now that I come to think about it, her elegant yet sensual style does kind of fit in here."
    mike.say "Erm..."
    mike.say "The feeling's kind of mutual, Kiara!"
    mike.say "I...I sometimes come here when my local is a little too busy."
    mike.say "Like it was tonight - so here I am!"
    "Kiara holds my eye as I rabbit on trying to explain myself without also incriminating myself."
    "And all the time she keeps a warms smile on her face as she nods silently."
    "Only once I'm done talking does she offer a response."
    show kiara talkative
    kiara.say "Well we can't have you not getting your desired refreshment, now can we?"
    show kiara normal
    "Without turning her head in the direction of the bar-tender, Kiara snaps her fingers."
    "The moment she does so, I can't help the fact that my jaw drops at the gesture."
    "I mean seriously, when was the last time you saw someone do something so disrespectful?"
    "I'm fully expecting the person behind the bar to tell her where to get off."
    "And so it staggers me even more when I see them hurry over and attend to Kiara in an instant."
    "Bartender" "Yes, Madam..."
    "Bartender" "What can I get for you?"
    "Without missing a beat, Kiara gestures to me."
    show kiara talkative
    kiara.say "Whatever my friend here would like to drink."
    kiara.say "And don't worry, [hero.name] - it's on the house."
    show kiara normal
    mike.say "It...it is?"
    mike.say "Erm...can I get a beer?"
    show kiara stuned with dissolve
    "Kiara looks more than a little surprised that I'd order something as pedestrian as simple beer."
    "But my head is still kind of spinning from the way she bent the bartender to her will just now."
    "And so I don't want to do anything that might break the spell."
    show kiara normal
    mike.say "So..."
    mike.say "Do you have, like, a tab here or something?"
    show kiara smile at startle(0.1, -5)
    pause 0.2
    show kiara bothered
    "Kiara seems oddly amused by the question, as she lets out a peal of laughter."
    show kiara talkative
    kiara.say "HA!"
    kiara.say "I suppose you could say that, [hero.name]."
    kiara.say "But it would be more honest to just say that I own the club."
    show kiara mischievous
    "Kiara throws the admission out like it's nothing at all."
    "But as soon as I hear it, I almost choke on a mouthful of beer."
    mike.say "Urgh..."
    mike.say "You..."
    mike.say "You own this place?!?"
    mike.say "I thought you just ran the Maid Cafe near the mall?"
    "Kiara shrugs."
    show kiara talkative
    kiara.say "The truth is that I own a diverse range of legitimate businesses."
    kiara.say "But I see no need to inform everyone I meet about each an every one of them."
    show kiara normal
    "I'm nodding the whole time that Kiara's telling me all of this."
    "And my hope is that I look like I'm taking it all in too."
    "But the truth is that my mind's racing at these revelations."
    "Suddenly Kiara's gone from a woman that runs a cafe to a bona fide captain of industry!"
    mike.say "I..."
    mike.say "I guess it makes sense to diversify your portfolio!"
    show kiara smile
    "That's it, the most sensible and intelligent thing I can think to say."
    "But luckily for me, it seems to both satisfy and amuse Kiara."
    "Because she greets it with a nod and a smile."
    show kiara talkative
    kiara.say "I should have known that you would understand, [hero.name]."
    kiara.say "A truly modern man like you isn't intimidated by a woman with legitimate business interests."
    kiara.say "Older, less evolved men can never seem to cope with the idea of such a thing."
    show kiara normal
    "I'm still nodding at all Kiara has to say."
    "But there's something that keeps nagging at me."
    "And that's the fact she seems to never say the 'business' without tagging on the word 'legitimate' afterwards."
    "Now I feel certain that I've heard that being done somewhere else and by a very specific group of people."
    "Though right now, the exact details escape me..."
    mike.say "Oh no, Kiara - I can totally handle a woman owning her own bar!"
    mike.say "And not only that, but a strip-club too?"
    mike.say "That's crazily progressive of you."
    show kiara mischievous
    "Kiara cocks her head on one side as she listens to me flatter her."
    show kiara flirt
    kiara.say "Hmm..."
    show kiara talkative
    kiara.say "It sounds to me like you'd be comfortable working under a woman like me."
    kiara.say "Wouldn't you, [hero.name]?"
    show kiara evil
    mike.say "Under...beside...on top of...or anywhere else you want me, Kiara!"
    show kiara talkative
    kiara.say "Is that so?"
    kiara.say "Well, how about I give you a little job to do for me?"
    kiara.say "A simple task to prove that you can take orders from a woman?"
    show kiara mischievous
    "Okay, tonight is definitely not going the way I thought that it would."
    "But I already managed to score a free beer from Kiara."
    "And I can't help feeling like I'm really getting somewhere with her right now."
    "So what the hell have I got to lose?"
    mike.say "Okay, Kiara..."
    mike.say "Hit me with it."
    show kiara smile
    "Kiara's smile becomes a little more knowing as I agree to her task."
    show kiara work normal at center, traveling(2.0, 0.5, (740, 1220))
    "But as soon as she leans in closer to explain it to me, I lose all interest in why that might be."
    show kiara talkative
    kiara.say "Okay, [hero.name]..."
    kiara.say "You see that man?"
    show danny at blacker, center, zoomAt(1, (-180, 720))
    kiara.say "The one sitting in the booth over there?"
    show bg stripclub at center, traveling(1.4, 1, (850, 820))
    show kiara normal at center, traveling(1.8, 1, (1220, 1120))
    show danny at blacker, center, traveling(1, 1, (300, 720))
    pause 1
    show bg stripclub at center, zoomAt(1.4, (850, 820))
    show kiara at center, zoomAt(1.8, (1220, 1120))
    show danny at blacker, center, zoomAt(1, (300, 720))
    "I turn my gaze in the direction that Kiara's pointing, and I can hardly miss the guy."
    mike.say "You mean the really mean-looking guy with the tattoos?"
    mike.say "It's kind of hard to miss him!"
    show kiara talkative
    kiara.say "Yes, that's the one I'm talking about - the man is called Donnie."
    kiara.say "Would it surprise you to know that he's in my debt?"
    kiara.say "That he owes me money and is supposed to be here to hand it over?"
    show kiara mischievous
    "I'm still staring at Donnie while Kiara's explaining the situation to me."
    "But as soon as she mentions the debt, I turn my head around to look at her again."
    "Because I can already see where this is going."
    show bg stripclub at center, traveling(1.4, 0.5, (400, 820))
    show kiara normal at center, traveling(1.8, 0.5, (740, 1120))
    show danny at blacker, center, traveling(1, 0.5, (-180, 720))
    mike.say "Let me guess, Kiara..."
    mike.say "You want me to go over there and persuade him to cough up, yeah?"
    show kiara mischievous
    "Kiara's smile is slow and subtle, creeping over her face as she regards me."
    show kiara talkative
    kiara.say "I see that you catch on fast, [hero.name]."
    kiara.say "That is a very desirable quality in a man."
    kiara.say "So, will you do this little thing for me?"
    show kiara mischievous
    menu:
        "Agree to get the money from Donnie":
            show bg stripclub at center, traveling(1.4, 1, (850, 820))
            show kiara normal at center, traveling(1.8, 1, (1220, 1120))
            show danny at blacker, center, traveling(1, 1, (300, 720))
            pause 1
            show bg stripclub at center, zoomAt(1.4, (850, 820))
            show kiara at center, zoomAt(1.8, (1220, 1120))
            show danny at blacker, center, zoomAt(1, (300, 720))
            "I take another look at Donnie, trying to really size him up this time."
            "Then I notice how intently Kiara is studying me right now."
            "It's like she's noting even the smallest aspect of my reaction to her request."
            "And that's when I realise that I'm being put through a subtle test here."
            menu:
                "Handle the matter in a professional and discreet manner" if hero.charm >= 75 and hero.knowledge >=25:
                    mike.say "I guess I could handle that, Kiara..."
                    mike.say "I mean, he's here to pay the debt, right?"
                    mike.say "So it's not like he doesn't know he's going to be asked for the money."
                    "Kiara nods as I try to justify the idea to myself."
                    show kiara talkative
                    kiara.say "Exactly so, [hero.name]..."
                    kiara.say "This is no different from me asking any of my employees to complete the task."
                    kiara.say "So it should be a simple matter of reminding Donnie of his obligation to me."
                    show kiara mischievous
                    "I nod as I put down my drink and turn in the direction of Donnie's booth."
                    show bg stripclub at center, traveling(1.6, 4, (1020, 920))
                    show kiara normal at center, traveling(3.2, 1, (1820, 1820))
                    show danny at blacker, center, traveling(1.6, 4, (440, 970))
                    pause 4
                    show bg stripclub at center, zoomAt(1.6, (1020, 920))
                    show kiara at center, zoomAt(3.2, (1820, 1820))
                    show danny at blacker, center, zoomAt(1.6, (440, 970))
                    "And I don't stop walking until I'm standing right next to the guy."
                    show bg stripclub at center, traveling(1.6, 1, (1020, 1120))
                    show kiara normal at center, traveling(2.2, 1, (1820, 1420))
                    show danny at blacker, center, traveling(1.6, 1, (440, 1070))
                    pause 1
                    show bg stripclub at center, zoomAt(1.6, (1020, 1120))
                    show kiara at center, zoomAt(2.2, (1820, 1420))
                    show danny at blacker, center, zoomAt(1.6, (440, 1070))
                    "At first he seems to be ignoring me out of sheer disdain."
                    "But then he stops and slowly turns his head towards me."
                    show danny at blacker, center, zoomAt(1, (440, 1070)), startle(0.1, 5)
                    "Donnie" "And what the fuck, might I ask, do you want?"
                    "Remembering everything that Kiara told me, I take a deep breath."
                    "And then I launch into it, consequences be damned."
                    mike.say "Kiara sent me over here."
                    mike.say "She says that she wants her money."
                    mike.say "So if you'd kindly hand it over?"
                    "Donnie seems less than impressed with my demand."
                    "And for a moment it seems like he's going to tell me to get lost."
                    "But then I see a twitch in his eye, like he's looking behind me."
                    "His direct line of sight leading to where Kiara is standing by the bar."
                    "And whatever he sees over there, it apparently helps to change his mind."
                    show danny at blacker, center, zoomAt(1, (440, 1070)), startle(0.1, 5)
                    "Donnie" "Ah, what the hell..."
                    "Donnie" "Take the damn money and tell her we're even."
                    "Donnie" "It's not worth my time anyway!"
                    "Donnie stands up and pulls a wad of used notes out of his pocket."
                    "Then he shoves it into my hand and shoulders his way out of the club."
                    "I take the chance to head straight back to Kiara, handing her the wad."
                    scene bg stripclub at center, zoomAt(1.4, (400, 820))
                    show kiara work at center, zoomAt(1.8, (740, 1120))
                    with dissolve
                    mike.say "All sorted, Kiara."
                    mike.say "He didn't..."
                    hide kiara
                    show kiara kiss date
                    with hpunch
                    mike.say "Mmm!"
                    hide kiara
                    show kiara kiss date
                    with dissolve
                    "Kiara cuts me off by placing her lips against mine, kissing me deeply."
                    "The kiss doesn't last for long, but it's intense and she holds nothing back."
                    hide kiara
                    show kiara work normal at center, zoomAt(1.8, (740, 1120))
                    with fade
                    "And when it's over, Kiara regards me with what I think is a newfound respect."
                    hide kiara kiss
                    show kiara work talkative at center, zoomAt(1.8, (740, 1120))
                    with dissolve
                    kiara.say "That was well handled, [hero.name]..."
                    kiara.say "You have my thanks for that."
                    kiara.say "And for the rest of the night, your drinks are on me."
                    show kiara normal
                    pause 0.5
                    scene bg stripclub with fade
                    "With that, Kiara gets up and sweeps away through the crowd."
                    "Leaving me shaking my head in her wake."
                    "And convinced that things between us are getting more complicated every time we meet."
                    $ kiara.love += 5
                "Handle the matter in an assertive and fearless manner" if hero.fitness >= 50:
                    mike.say "No problem whatsoever, Kiara..."
                    mike.say "That guy looks like just another cheap punk to me."
                    mike.say "The type you just need to stand up to for them to choke."
                    "Kiara nods as I try to justify the idea to myself."
                    show kiara talkative
                    kiara.say "I admire your confidence, [hero.name]..."
                    kiara.say "But do not make the mistake of underestimating Donnie."
                    kiara.say "Yes, he is scum - but scum that can be unpredictable."
                    show kiara mischievous
                    "I nod as I put down my drink and turn in the direction of Donnie's booth."
                    show bg stripclub at center, traveling(1.6, 4, (1020, 920))
                    show kiara normal at center, traveling(3.2, 1, (1820, 1820))
                    show danny at blacker, center, traveling(1.6, 4, (440, 970))
                    pause 4
                    show bg stripclub at center, zoomAt(1.6, (1020, 920))
                    show kiara at center, zoomAt(3.2, (1820, 1820))
                    show danny at blacker, center, zoomAt(1.6, (440, 970))
                    "And I don't stop walking until I'm standing right next to the guy."
                    show bg stripclub at center, traveling(1.6, 1, (1020, 1120))
                    show kiara normal at center, traveling(2.2, 1, (1820, 1420))
                    show danny at blacker, center, traveling(1.6, 1, (440, 1070))
                    pause 1
                    show bg stripclub at center, zoomAt(1.6, (1020, 1120))
                    show kiara at center, zoomAt(2.2, (1820, 1420))
                    show danny at blacker, center, zoomAt(1.6, (440, 1070))
                    "At first he seems to be ignoring me out of sheer disdain."
                    "But then he stops and slowly turns his head towards me."
                    show danny at blacker, center, zoomAt(1, (440, 1070)), startle(0.1, 5)
                    "Donnie" "And what the fuck, might I ask, do you want?"
                    "Remembering everything that Kiara told me, I take a deep breath."
                    "And then I launch into it, consequences be damned."
                    mike.say "The fucking money, pecker-neck..."
                    mike.say "I'm here for the money that you owe the lady over there."
                    mike.say "So hand it over and then you can be on your way."
                    "Donnie seems less than impressed with my demand."
                    "And for a moment it seems like he's going to tell me to get lost."
                    "But then I see a twitch in his eye, like he's looking behind me."
                    "His direct line of sight leading to where Kiara is standing by the bar."
                    "And whatever he sees over there, it apparently helps to change his mind."
                    show danny at blacker, center, zoomAt(1, (440, 1070)), startle(0.1, 5)
                    "Donnie" "Ah, what the hell..."
                    "Donnie" "Take the damn money and tell her we're even."
                    "Donnie" "It's not worth my time anyway!"
                    "Donnie stands up and pulls a wad of used notes out of his pocket."
                    "Then he shoves it into my hand and shoulders his way out of the club."
                    "I take the chance to head straight back to Kiara, handing her the wad."
                    scene bg stripclub at center, zoomAt(1.4, (400, 820))
                    show kiara work at center, zoomAt(1.8, (740, 1120))
                    with dissolve
                    mike.say "All sorted, Kiara."
                    mike.say "He didn't..."
                    mike.say "What the..."
                    "Kiara cuts me off by placing a hand on my cheek and caressing it tenderly."
                    "Then I watch as she runs it down my neck and over my chest."
                    "All the time looking like the very feel of my body is thrilling her."
                    show kiara talkative
                    kiara.say "Oh, [hero.name]...that was so...forceful!"
                    kiara.say "You have my thanks for that."
                    kiara.say "And for the rest of the night, your drinks are on me."
                    show kiara normal
                    pause 0.5
                    scene bg stripclub with fade
                    "With that, Kiara gets up and sweeps away through the crowd."
                    "Leaving me shaking my head in her wake."
                    "And convinced that things between us are getting more complicated every time we meet."
                    $ kiara.love += 2
                    $ kiara.sub += 5
                "Handle the matter in an obedient and fascinated manner":
                    mike.say "I... I think I could manage that, Kiara..."
                    mike.say "If you think so too?"
                    mike.say "And you trust me to get the money for you?"
                    "Kiara nods as I try to justify the idea to myself."
                    show kiara talkative
                    kiara.say "I believe in you, [hero.name]..."
                    kiara.say "This is just a little test, remember?"
                    kiara.say "The smallest of tasks to prove that you will do as I ask."
                    show kiara mischievous
                    "I nod as I put down my drink and turn in the direction of Donnie's booth."
                    show bg stripclub at center, traveling(1.6, 4, (1020, 920))
                    show kiara normal at center, traveling(3.2, 1, (1820, 1820))
                    show danny at blacker, center, traveling(1.6, 4, (440, 970))
                    pause 4
                    show bg stripclub at center, zoomAt(1.6, (1020, 920))
                    show kiara at center, zoomAt(3.2, (1820, 1820))
                    show danny at blacker, center, zoomAt(1.6, (440, 970))
                    "And I don't stop walking until I'm standing right next to the guy."
                    show bg stripclub at center, traveling(1.6, 1, (1020, 1120))
                    show kiara normal at center, traveling(2.2, 1, (1820, 1420))
                    show danny at blacker, center, traveling(1.6, 1, (440, 1070))
                    pause 1
                    show bg stripclub at center, zoomAt(1.6, (1020, 1120))
                    show kiara at center, zoomAt(2.2, (1820, 1420))
                    show danny at blacker, center, zoomAt(1.6, (440, 1070))
                    "At first he seems to be ignoring me out of sheer disdain."
                    "But then he stops and slowly turns his head towards me."
                    show danny at blacker, center, zoomAt(1, (440, 1070)), startle(0.1, 5)
                    "Donnie" "And what the fuck, might I ask, do you want?"
                    "Remembering everything that Kiara told me, I take a deep breath."
                    "And then I launch into it, consequences be damned."
                    mike.say "Erm...okay...excuse me, but..."
                    mike.say "The lady over by the bar...you know the one that I'm talking about?"
                    mike.say "Well, she'd like to know if she could have her money back?"
                    mike.say "You know...if it wouldn't be too much of an inconvenience?"
                    "Donnie seems less than impressed with my request."
                    "And for a moment it seems like he's going to tell me to get lost."
                    "As well as most likely getting up and punching me in the face too!"
                    "But then I see a twitch in his eye, like he's looking behind me."
                    "His direct line of sight leading to where Kiara is standing by the bar."
                    "And whatever he sees over there, it apparently helps to change his mind."
                    show danny at blacker, center, zoomAt(1, (440, 1070)), startle(0.1, 5)
                    "Donnie" "Ah, what the hell..."
                    "Donnie" "Take the damn money and tell her we're even."
                    "Donnie" "It's not worth my time anyway!"
                    "Donnie stands up and pulls a wad of used notes out of his pocket."
                    "Then he shoves it into my hand and shoulders his way out of the club."
                    "I take the chance to head straight back to Kiara, handing her the wad."
                    scene bg stripclub at center, zoomAt(1.4, (400, 820))
                    show kiara work at center, zoomAt(1.8, (740, 1120))
                    with dissolve
                    mike.say "All sorted, Kiara."
                    mike.say "He didn't..."
                    mike.say "Oh my!"
                    "Kiara cuts me off by grabbing my chin and cupping it in her hand."
                    "Then she looks deep into my eyes, as if studying me with great interest."
                    "And all I can do is just stand there, as still as a statue."
                    show kiara talkative
                    kiara.say "That was well handled, [hero.name]..."
                    kiara.say "You have my thanks for that."
                    kiara.say "And for the rest of the night, your drinks are on me."
                    show kiara normal
                    pause 0.5
                    scene bg stripclub with fade
                    "With that, Kiara gets up and sweeps away through the crowd."
                    "Leaving me shaking my head in her wake."
                    "And convinced that things between us are getting more complicated every time we meet."
                    $ kiara.love += 2
                    $ kiara.sub -= 4
        "Refuse to get the money from Donnie":
            "I make a point of looking back at Donnie and shaking my head."
            "Then I meet Kiara's eye as I deliver my answer."
            mike.say "Kiara, you have got to be kidding me."
            mike.say "I came here for a drink and to look at the girls on the stage."
            mike.say "I definitely did not come here to get my ass handed to me!"
            "Kiara surprises me by simply listening quietly while I say my piece."
            "She doesn't object or try to convince me to see things her way."
            show kiara serious at startle(0.2, 10)
            pause 0.4
            show kiara blank with dissolve
            "And when I'm done talking, she just nods."
            show kiara talkative
            kiara.say "I understand, [hero.name]..."
            kiara.say "And I am making a request, not issuing an order."
            kiara.say "There are plenty of other's in my employ that can handle the task."
            show kiara blank
            "I nod at this, expecting Kiara to change the subject."
            "But instead she takes me by surprise when she gets up from her stool."
            show kiara at startle(0.2, 10)
            "And then she gives me a little bow and a nod of the head."
            show kiara talkative
            kiara.say "Very well..."
            kiara.say "I have business that must be attended to."
            show kiara guilty with dissolve
            kiara.say "And you have a need to relax and entertain yourself."
            show kiara talkative
            kiara.say "So I will bid you farewell, my friend."
            show kiara normal
            "I'm about to say something in response, to protest at Kiara leaving me alone."
            "But she doesn't seem to be in the mood for conversation anymore."
            scene bg stripclub with fade
            "As she just turns her back on me and sweeps away into the crowd."
            "I stand there for a few moments, still kind of stunned."
            "But it looks like Kiara was serious about that being the end of it."
            "Because that's the last I see of her for the rest of the night."
            $ kiara.love -= 10
    $ kiara.flags.nokiss = False
    $ kiara.flags.nodate = False
    scene bg black with dissolve
    $ kiara.flags.kiaradelay = TemporaryFlag(True, 1)
    return

label kiara_event_04:
    play sound cell_vibrate loop
    if kiara.love.max < 80:
        $ kiara.love.max = 80
    "Normally I'd just take a quick glance at my phone when it vibrates."
    "Just note the name attached to the message or call that's coming in."
    "And based on that I'd decide if it interested me enough to distract from what I'm doing."
    "Or else I'd just slip the phone back into my pocket and deal with it later."
    scene expression f"bg {game.room}" at blur(5), dark
    $ renpy.show_screen("smartphone_choice", "Kiara", show_mc=False, accept_only=True)
    with dissolve
    "But as soon as I see Kiara's name on the screen, I drop everything and take the call."
    stop sound
    mike.say "Hey, Kiara..."
    mike.say "What's up?"
    "Even before Kiara says a word, I can tell that there really is something up."
    "In the background I can hear a commotion going, threatening to drown her out."
    "There are raised voices and the sounds of things clattering around in a chaotic mess."
    kiara.say "[hero.name]..."
    kiara.say "I..."
    kiara.say "I need your help."
    "I'm not used to hearing such obvious desperation in Kiara's voice."
    "Normally she's confident and assured, commanding in a quiet manner."
    "But now she sounds extremely stressed, maybe even on the verge of breaking."
    mike.say "What's happened?"
    mike.say "Are you okay?"
    kiara.say "I'm...I'm fine, honestly..."
    kiara.say "It's just that there's...an emergency at one of my clubs."
    kiara.say "And I would be very grateful for your help, if you can spare me the time?"
    "Kiara seems to be torn between two extremes as she explains herself to me."
    "On the one hand, it sounds like she's genuinely relieved to hear my concern for her."
    "But on the other I can sense that she wants to dispense with such niceties."
    "Which I guess is understandable in the face of whatever crises she's in the middle of."
    menu:
        "Agree to come to Kiara's aid":
            "No matter though, because she has a white knight right here."
            "And he's more than ready to come riding to her aid!"
            mike.say "Don't worry about anything, Kiara..."
            mike.say "I'll be there as soon as I can!"
            kiara.say "Oh, thank you!"
            kiara.say "I'll send the address of the club as soon you hang-up."
            $ game.room = "street"
            $ renpy.hide_screen("smartphone_choice")
            scene bg street with fade
            "Keeping my word, I head out as soon as Kiara sends me the address."
            "And I spend the short journey over there wondering what I'm going to find."
            "But it's safe to say that I wasn't prepared for the scene that greets me."
            scene bg nightclub
            show beach_cream_npc_alexis at blacker, center, zoomAt(0.4, (340, 720))
            show watch_tv_minami at blacker, center, zoomAt(0.65, (1140, 720))
            show watch_tv_minami_haircut at blacker, center, zoomAt(0.65, (1140, 720))
            show watch_tv_samantha at blacker, center, zoomAt(0.25, (880, 580))
            with fade
            "The place looks like one of those slick, fashionable nightclubs."
            "The kind where I'd be afraid of the door staff telling me to get lost."
            "Or at least that's how it must have looked a couple of hours ago."
            "Because now it's a total mess of broken glass, busted furniture and red paint spattered everywhere."
            "Oh no...scratch the bit about red paint, as a closer look shows me that it's actually blood!"
            "And I can see that there are people wandering about with visible wounds too."
            "Hell, some of them are just slumped on the floor, trying to staunch the bleeding."
            menu:
                "Do your best to help":
                    "I kind of feel a little overwhelmed with the situation that I've walked into."
                    "And normally my instinct would be to stand back and let the professionals handle it."
                    "But on the other hand I want to do all that I can to help Kiara in her time of need."
                    "Though I'm not a paramedic or the kind of guy that can take charge at a time like this."
                    "So instead I decide to do whatever I can to help, no matter how small."
                    "Turning to the first wounded person I find, I get straight to work."
                    mike.say "Hey there..."
                    mike.say "Let me help you, okay?"
                    mike.say "Maybe start by telling me where it hurts?"
                    "And that's how I do my best to help, going here and there, doing what I can."
                    show kiara work at center, zoomAt (1.0, (1040, 720)) with easeinright
                    "It's while I'm into the task that I get my first glimpse of Kiara amidst the chaos."
                    show kiara work at center, zoomAt (1.0, (740, 720)) with ease
                    "She seems to be everywhere at once, issuing orders and checking on her people."
                    show kiara work at center, zoomAt (1.0, (340, 720)) with ease
                    "And it's impossible for me not to see her in action and be totally impressed."
                    "Because I can see how much she cares for them, like they're not just employees."
                    scene bg nightclub
                    show kiara work at center, zoomAt (1.25, (640, 880))
                    with fade
                    show kiara at center, traveling(1.5, 1.0, (640, 1060))
                    "It's a long time before Kiara has the chance to come over and speak to me."
                    "But when she does, it's with a look of genuine interest in her eyes."
                    show kiara talkative
                    kiara.say "Ah..."
                    kiara.say "Finally we can speak!"
                    show kiara normal
                    mike.say "Phew..."
                    mike.say "I know what you mean, Kiara - this is insane!"
                    "Kiara nods."
                    show kiara talkative
                    kiara.say "Indeed it is, but I think we are starting to get things under control."
                    kiara.say "And I keep hearing from my people about how much you have helped them too."
                    show kiara normal
                    mike.say "Oh, I don't know about that..."
                    mike.say "I just kind of turned up and got stuck in, that's all."
                    show kiara talkative
                    kiara.say "Exactly, [hero.name] - you helped without needing to be told what to do."
                    kiara.say "And that is a quality that I admire."
                    show kiara normal
                    $ kiara.love += 4
                "Take charge of the situation":
                    "I've never been one of those guys that feels like an alpha male or a natural leader."
                    "And it's not like I've pursued a career that would equip me to assume that kind of a role."
                    "But as I stand there, surrounded by the chaos, something inside of me just seems to click."
                    "I don't know what it is, but maybe my feelings for Kiara and need to please her are a part of it."
                    "Whatever the reason, I instantly meet the gaze of the nearest person that looks in good condition."
                    mike.say "Hey, you..."
                    mike.say "Help me move this thing right here..."
                    mike.say "I think there's someone trapped under it!"
                    "It could be that I manage to put an authoritative tone into my voice as I say that."
                    "Or maybe it's just that people have been waiting for someone to take charge."
                    "Either way, the guy instantly does as he's told."
                    "And from that point on, I seem to be taking control of the situation."
                    "Before too long, Kiara's people are coming to me to ask what to do next."
                    scene bg nightclub
                    show kiara work at center, zoomAt (1.0, (640, 720))
                    with fade
                    show kiara at center, traveling(1.5, 0.5, (640, 1060))
                    "And when she finally finds me herself, I have to hold up a hand and ask her to hold on."
                    mike.say "Just a second, Kiara..."
                    mike.say "Move it over there, you see?"
                    mike.say "Then go help those guys with the wounded, okay?"
                    mike.say "Sorry, Kiara, I didn't mean to be rude just now."
                    mike.say "But I was kind of busy!"
                    "Much to my relief, Kiara doesn't seem in the least bit annoyed with me."
                    show kiara mischievous
                    "Instead she's actually looking at me with what might be respect in her eyes."
                    show kiara talkative
                    kiara.say "No need to apologise, [hero.name]."
                    kiara.say "After all, that's what I called you here to do - to take charge."
                    kiara.say "You seem to be doing that, and with great effectiveness too."
                    $ kiara.love += 1
                    $ kiara.sub += 3
                "Keep your distance with what you see":
                    "I had no idea what I was going to walk into when I agreed to help Kiara out."
                    "But there was nothing that could have prepared me for what I'm seeing right now."
                    "This isn't just a crisis at one of her clubs, this is a scene of actual violence!"
                    show kiara work at center, zoomAt (1.0, (1040, 720)) with easeinright
                    "I stand there helplessly looking around until I spot Kiara in the chaos."
                    "And yet even when I see her, I still find myself frozen to the spot."
                    "So in the end, she's the one that reacts to my arrival."
                    show kiara scream at center, traveling(1.25, 0.5, (640, 880))
                    kiara.say "[hero.name]…"
                    kiara.say "Don't just stand there."
                    kiara.say "Do something to help, god damn it!"
                    show kiara unhappy
                    "There's just something so commanding and powerful about the way Kiara speaks to me."
                    "My brain can't help processing it as an order, rather than a request."
                    show kiara sadsmile
                    "And so I find myself leaping into action as soon as she's spoken the words."
                    "In fact it's all I can do to keep from snapping off a little salute as well!"
                    hide kiara with fade
                    "I turn and look to the first person that I come across, doing what I can to help."
                    "And the mere act of involving myself seems to be what I needed to snap out of it."
                    "Because from that point on I feel like I'm a part of Kiara's crew, rather than a mere observer, or worse - a spare part."
                    "Helping people up, patching their wounds and then beginning to pick up the debris."
                    "All of it merges into one as we hurry around, turning the chaos back into a semblance of order."
                    show kiara work at center, zoomAt (1.25, (640, 880)) with easeinleft
                    "And through it all, Kiara is the centre of everything."
                    "She's not only issuing orders, but I also see her comforting her people."
                    "And I also see how much strength they seem to derive from knowing that she's there for them too."
                    $ kiara.love -= 1
                    $ kiara.sub -= 3
            with fade
            "By now the club seems to be settling into a rhythm of Kiara's people cleaning up."
            "Those in need of medical aid seem to have been taken off in search of it."
            show kiara childish
            "And so she takes the chance to pause for a moment, perching on a stool."
            show kiara at center, traveling(1.5, 0.5, (640, 1060))
            "Seeing just how exhausted she looks, I hurry over to be at her side."
            show kiara annoyed
            "Of course there's no way that I can do it quietly or without being seen."
            "And at first I'm worried that I've done something wrong."
            "That Kiara will be upset with me for, I don't know, maybe showing her up in front of her people?"
            show kiara normal
            "But almost as soon as she sees me, Kiara's face breaks into a smile."
            "I mean she still looks really weary, just also happy to see me."
            mike.say "Hey, Kiara..."
            mike.say "How are you holding up?"
            "I'm pretty close to her by now, leaning in to be heard over the noise going on around us."
            hide kiara
            show kiara kiss date
            with fade
            "And Kiara takes advantage of that closeness by putting her lips against mine and kissing me."
            "It's not a long kiss by any means, and it certainly doesn't lead to any heavy tongue action."
            "But I can feel the emotion that she's putting into it, as the same feeling stir in me too."
            hide kiara
            show kiara date smile at center, zoomAt(2.5, (640, 1660))
            with fade
            "And once it's over, Kiara leans her forehead against mine, as if we're holding each other up."
            show kiara talkative
            kiara.say "Much better, [hero.name]…"
            kiara.say "Much better for you being here with me!"
        "Refuse to come to Kiara's aid":
            "But all the same, I have no idea what she expects me to be able to do about it."
            "And on top of that, I'm already feeling pretty scared of the noises on the other end of the line!"
            mike.say "Erm..."
            mike.say "I don't think I can make it over there right now, Kiara."
            mike.say "But maybe I could call the emergency services for you?"
            "I hear Kiara take a sharp breath on her end."
            "And I can almost imagine her shaking her head in disbelief."
            kiara.say "No, [hero.name], that will not be necessary."
            kiara.say "And now that I think about it, perhaps you should stay away."
            kiara.say "This would be too dangerous of a thing for you to handle."
            $ renpy.hide_screen("smartphone_choice")
            scene expression f"bg {game.room}"
            with dissolve
            "With that, Kiara just hangs up on me."
            "And I'm left with the awful suspicion that I just dropped the ball."
            $ kiara.love -=10
    $ kiara.flags.kiaradelay = TemporaryFlag(True, 2)
    scene bg black with dissolve
    $ game.room = "street"
    return

label kiara_event_05:
    if kiara.love.max < 100:
        $ kiara.love.max = 100
    scene bg rpgthrone
    play sound crowd_theater loop
    show dwayne at center, blacker, zoomAt(0.7, (40, 720))
    show scottie at center, blacker, zoomAt(0.7, (140, 720))
    show palla at center, blacker, zoomAt(0.7, (940, 720))
    show aletta at center, blacker, zoomAt(0.7, (740, 720))
    with fade
    "I can't shake off the feeling of being out of place as I step into the rarefied air of Kiara's exclusive lounge."
    "I mean, I might have occasionally made it into the VIP area at night-club in the past and felt like I was someone."
    "But the moment that they let me into this place, I feel like I'm totally out of my depth."
    "For one thing, it's plush and fancy beyond my capacity to be able to make sense of the décor."
    "I honestly can't tell if it's too tasteful me to appreciate or else so vulgar and over the top I wouldn't know it."
    "And then there's the other guests that are flitting about the place and filling it with the subtle murmur of small-talk."
    "They're like the human equivalent of the baffling décor that I already mentioned."
    "Dressed up to the nines and sporting enough bling to sparkle under the lights, I have no idea who or what they are."
    "Seriously, these people could be big-noises in business or something to do with the entertainment industry."
    "Or they could just as easily be a bunch of scary gangsters with pistols hidden under their jackets!"
    "That's why I do my best to keep a low profile without looking too much like I don't belong."
    "And all the time I'm gazing around, trying to spot the one reason that I'm here in the first place."
    kiara.say "[hero.name]…"
    kiara.say "There you are!"
    "Somehow the sound of Kiara's voice cuts through everything, inside and outside of my head."
    "Suddenly I find myself forgetting about all of the things that were making me feel so uncomfortable."
    "Because as I turn in the direction of her voice, all of my thoughts are turning at the same time."
    "And the one thing that they're able to focus on is Kiara herself."
    show kiara d sluttydate at center, zoomAt(0.7, (640, 720)) with easeinleft
    mike.say "Kiara..."
    mike.say "You look..."
    mike.say "You look SO amazing!"
    "Seriously, what else am I supposed to say?"
    "Kiara's standing there, commanding the room."
    "And she's wearing a dress that makes her look like a total goddess."
    "I'd be babbling and stumbling over my words if I even tried to hide the effect she's having on me right now."
    show kiara a talkative
    kiara.say "Well, thank you, [hero.name]…"
    kiara.say "I have been given perhaps more sophisticated compliments tonight."
    kiara.say "But none of them have been anywhere near as genuine in nature."
    show kiara d normal
    "I choose to take that as a good sign, that Kiara approves of what I said."
    "And I hurry over to where she's standing before anyone else can get too close."
    "Finding as I do so that being in her orbit helps to make me feel more confident."
    "I can feel the eyes of her other guests on me as we converse together."
    "But somehow Kiara is able to shield me from them as she pulls me towards herself."
    mike.say "I...I should thank you for inviting me here, Kiara."
    mike.say "I'm not used to places as fancy as this."
    mike.say "And I was...well, I was afraid of embarrassing you!"
    show kiara smile at center, traveling(1.8, 3, (640, 1270))
    pause 3
    show kiara smile at center, zoomAt(1.8, (640, 1270))
    "Kiara smiles and extends her hand towards me, twining her fingers in mine."
    "And then she begins to lead me away from the main crowd in the lounge."
    show kiara b talkative
    kiara.say "Oh, [hero.name]..."
    kiara.say "You have nothing at all to be ashamed of, I assure you."
    kiara.say "None of the people you see here tonight would be here without my express invitation."
    kiara.say "But none of them are here in the same capacity as you are - none of them are my friends!"
    scene bg rpgthrone at center, zoomAt(2, (440, 1020))
    show kiara sluttydate a mischievous at center, zoomAt(1.8, (640, 1270))
    with fade
    $ renpy.music.set_audio_filter("sound", af.Lowpass(440))
    play sound crowd_theater loop volume 0.5
    "I'm nodding the whole time as Kiara leads me over to a more private part of the lounge."
    show kiara dreaming with dissolve
    "It's not like there's an even more exclusive area inside of this already pretty exclusive area."
    "But at the same time it's clear that this is her territory alone."
    "And it's not to be entered without her express permission or company."
    "This means that for the first time since I arrived, for all intents and purposes, we're alone together."
    show kiara mischievous at center, traveling(2.2, 1, (640, 1500))
    pause 1
    show kiara mischievous at center, zoomAt(2.2, (640, 1500))
    "Sure, there are other guests no more than a few metres away, but they can't easily see or hear us over here."
    menu:
        "Try to make a genuine connection with Kiara":
            show kiara flirt with dissolve
            "Almost as soon as it's apparent we have some privacy, Kiara's whole demeanour changes."
            "Before now she was playing the part of the beguiling criminal queenpin."
            "Holding court in front of all the people that she needs to impress."
            "But now that it's just the two of us, she almost sags under the weight of it all."
            "Don't get me wrong, she still looks stunningly beautiful."
            "It's just that now Kiara's choosing to show her true self to me."
            show kiara bothered
            kiara.say "Am so glad that you chose to come here tonight, [hero.name]."
            show kiara cringe
            kiara.say "I cannot be myself around any of these people, not for a second."
            kiara.say "So simply having you here refreshes me, gives me newfound energy!"
            show kiara sadsmile
            mike.say "Kiara..."
            mike.say "Are you...lonely?"
            "It seems like such an obvious thing for the average person to admit to."
            "But then I remember that Kiara's far from average, in every possible way."
            show kiara cringe
            kiara.say "In my line of work, there is so little time for a personal life."
            kiara.say "Let alone the space to even think about matters of the heart."
            "Kiara's looking me straight in the eye as she says all of this."
            show kiara sadsmile at center, traveling(2.4, 1, (640, 1620))
            "And it's about then that I realise she's still holding my hand."
            "Only now she's also squeezing it tightly, adding emphasis to her words."
            show kiara at center, traveling(2.6, 1, (640, 1740))
            "We're no more than a couple of inches apart, the distance closing by the second."
            "And what happens next feels like the most natural thing in the world."
            "I incline my head to one side, Kiara hers to the other."
            hide kiara
            show kiara kiss sluttydate
            with fade
            "Then our lips meet, and the kiss that follows is impossible to describe."
            "So I won't even try to put it into words, as that's be a waste of time."
            "Suffice to say that it lasts a long while, and when it's over, I feel things have changed between us."
            "Like we've admitted that the two of us are no longer friends or aquaintences."
            "The bond between us is way too strong for it to be described like that any longer."
            $ kiara.love += 5
        "Keep control of the situation":
            show kiara evil with dissolve
            "I was hoping that once we had some time alone, I might see Kiara's mask slip."
            "But from the way that she's looking at me, it seems she's still playing her part."
            "That she's almost being the same mysterious and unknowable woman she is for the sake of her guests."
            show kiara talkative
            kiara.say "You know that you're very lucky to get this chance to be alone with me, [hero.name]?"
            kiara.say "I have so many important people here tonight, my time is at a premium!"
            kiara.say "So if there's anything you need to say to me..."
            show kiara normal
            "I can't help twisting my mouth into an awkward frown and furrowing my brow at this."
            mike.say "Yeah, Kiara..."
            mike.say "There is something that I wanted to ask you."
            mike.say "And it's why in the hell are you putting on an act in front of me?"
            show kiara disappointed
            mike.say "You and I both know that we're way past that by now."
            "For a moment Kiara looks like she's going to rise to my challenge."
            "She looks almost offended as she pulls herself up to her full height."
            show kiara annoyed
            "But then the fight seems to drain out of her, and she visibly sags in front of me."
            show kiara cringe
            kiara.say "I do not know how you are able to do that..."
            kiara.say "To see through me so completely."
            kiara.say "I cannot do anything but he honest with you, [hero.name]..."
            show kiara sadsmile
            "Kiara's looking me straight in the eye as she says all of this."
            "And it's about then that I realise she's still holding my hand."
            "Only now she's also squeezing it tightly, adding emphasis to her words."
            show kiara cringe
            kiara.say "I need to be with you, to have you in my life."
            kiara.say "And if that means yielding to you in order to get what I want..."
            kiara.say "Then that's what I will do!"
            show kiara at center, traveling(2.2, 1, (640, 1600))
            pause 0.2
            show bg rpgthrone at center, traveling(2, 1, (440, 720))
            pause 1
            show kiara at center, zoomAt(2.2, (640, 1600))
            show bg rpgthrone at center, zoomAt(2, (440, 720))
            show kiara serious with dissolve
            "By now Kiara's almost kneeling in front of me."
            "And I find myself holding her up for fear of her guests seeing."
            "Because the last thing she needs is for them to think she's showing weakness."
            mike.say "Stand up, Kiara..."
            show kiara sadsmile
            mike.say "You have to keep up the show until we're truly alone."
            show kiara at center, traveling(2.2, 1, (640, 1500))
            pause 0.2
            show bg rpgthrone at center, traveling(2, 0.5, (440, 1020))
            pause 0.5
            show kiara at center, zoomAt(2.2, (640, 1500))
            show bg rpgthrone at center, zoomAt(2, (440, 1020))
            "The speed with which Kiara hurries to do as I tell her comes as a genuine surprise."
            "And it tells me that she wasn't saying all of that for the sake of being dramatic."
            "It feels like there's been a genuine shift in the balance of power between us."
            "That now I'm the one to whom she's looking for strength and guidance."
            $ kiara.love += 2
            $ kiara.sub += 3
        "Let it go":
            show kiara evil with dissolve
            "I was hoping that once we had some time alone, I might see Kiara's mask slip."
            "But from the way that she's looking at me, it seems she's still playing her part."
            "That she's almost being the same mysterious and unknowable woman she is for the sake of her guests."
            show kiara talkative
            kiara.say "You know that you're very lucky to get this chance to be alone with me, [hero.name]?"
            kiara.say "I have so many important people here tonight, my time is at a premium!"
            kiara.say "So if there's anything you need to say to me..."
            show kiara normal
            "I stand there listening to Kiara as she explains the situation to me."
            "Nodding my head as I take in each point and totally agree with it."
            "Because she's one hundred percent correct, and there's no denying it."
            show kiara at center, traveling(2.2, 1, (640, 1400))
            show bg rpgthrone at center, traveling(2, 1, (440, 1320))
            pause 1
            show bg rpgthrone at center, zoomAt(2, (440, 1320))
            show kiara at center, zoomAt(2.2, (640, 1400))
            "Which is why I don't hesitate to drop down onto one knee once she's done talking."
            mike.say "I..."
            mike.say "I just wanted to say that I'm always here for you, Kiara..."
            mike.say "Whatever you want or need, just say the word and I'll do it!"
            "I'm still holding onto Kiara's hand as I say all of this."
            "Only now it's a lot more like I'm squeezing it out of devotion."
            "And I'm looking up at her with a genuine intensity in my eyes."
            "So much so that it seems she can't help but be impressed with my passion."
            show kiara talkative
            kiara.say "Oh, [hero.name]..."
            kiara.say "There's no need to literally bend the knee!"
            kiara.say "So get up now, as you've shown your devotion to me."
            show kiara at center, traveling(2.2, 1, (640, 1500))
            pause 0.2
            show bg rpgthrone at center, traveling(2, 1, (440, 1020))
            pause 1
            show kiara at center, zoomAt(2.2, (640, 1500))
            show bg rpgthrone at center, zoomAt(2, (440, 1020))
            "I have to stop myself leaping to my feet the moment that Kiara gives the order."
            "Because now that I've devoted myself to her, I feel a swelling of true purpose in my breast."
            "I can see that Kiara was always supposed to be the centre of my world, my everything."
            "And part of me can't wait for her to command me to do something again."
            "Just so that I can push myself even harder to demonstrate my obedience to her."
            $ kiara.love += 2
            $ kiara.sub -= 2
    $ kiara.flags.kiaradelay = TemporaryFlag(True, 2)
    scene bg black with dissolve
    $ game.room = "street"
    return

label kiara_event_06:
    if kiara.love.max < 120:
        $ kiara.love.max = 120
    scene bg street with fade
    "Now that I feel like I've been officially accepted into Kiara's secret inner circle, it's kind of thrilling."
    "I'm in on the fact that she's actually running an underworld operation out of her clubs and other businesses"
    "So heading down to the club at her invitation is more like being summoned by the Godfather than just meeting my girlfriend."
    "I have no idea what new and potentially dangerous situation might be awaiting for me once I get myself down there."
    "And maybe the excitement is affecting my judgement more than a little, as that thought doesn't frighten me all that much."
    "Or maybe I'm just secure in the knowledge that Kiara's a big deal in the world she lives in."
    "Big enough to be able to command respect and protect those close to her - including me!"
    $ game.room = "nightclub"
    scene bg nightclub with fade
    "All of this is running through my head as I walk into the club and start looking around."
    "The sound of my coming in makes a couple of the staff look up from what they're doing."
    "And I exchange a slightly awkward wave with the friendlier ones before they go back to their tasks."
    "But the main reason that I don't go over and really start talking to anyone is that I'm waiting for Kiara."
    "I mean, she asked me to come down here today, so I was kind of expecting her to be here to meet me."
    "The problem is that she's nowhere to be seen, and nobody's stepping forward to explain why."
    scene expression f"bg {game.room}" at blur(5), dark
    $ renpy.show_screen("smartphone_choice", "Kiara", show_mc=False, accept_only=True)
    with dissolve
    "Frowning a little, I pull out my phone and dial her number."
    play sound "<from 0 to 4>sd/SFX/phone/phone_calling.ogg"
    "The phone rings a couple of times before she picks up."
    "And I can tell from the tone of her voice that she's in the middle of something."
    stop sound
    kiara.say "Ah..."
    kiara.say "Hello, [hero.name]…"
    kiara.say "I take it that you've made it to the club?"
    mike.say "Yeah, Kiara..."
    mike.say "I just walked in here."
    mike.say "But I'm guessing you're somewhere else right now?"
    "Kiara makes as slightly awkward sound, like she's struggling with something."
    "And for a moment I'm concerned that she might be in a tight spot."
    "But when she starts talking again, she shows no sign of discomfort."
    kiara.say "Ahem..."
    kiara.say "Yes, my apologies for not keeping my word."
    kiara.say "I will be there as soon as I am able."
    kiara.say "But in the meantime, I need to ask a favour of you."
    "I can't help frowning, as I was hoping Kiara might already be on her way."
    "But I suppose that offering to help her out will make that happen sooner, rather than later."
    mike.say "Sure thing, Kiara..."
    mike.say "What can I do to help?"
    kiara.say "Oh, it is nothing too taxing."
    kiara.say "I would just like you to look after the club until I get there."
    "I'm kind of glad that Kiara's not here to see the look on my face right now."
    "Because to me it feels like my eyes just popped out of their sockets and my jaw dropped onto the floor."
    mike.say "You want me to look after the club?"
    mike.say "Your club?"
    mike.say "All of it?"
    "Kiara doesn't seem to notice the panic creeping into my voice."
    "As she just carries on explaining what she wants to me."
    kiara.say "As I have said, it will not be for long."
    kiara.say "And you have already seen me doing it, no?"
    kiara.say "So I will do what I have to do here and see you soon."
    "It looks like Kiara thinks the matter is settled, as she ends the call there."
    "Which leaves me staring at the phone in my hand, totally stunned."
    "But I get the uncanny feeling that someone is looking at me."
    $ renpy.hide_screen("smartphone_choice")
    scene bg nightclub
    show dwayne at blacker, center, zoomAt(0.9, (240, 720))
    show emma at blacker, center, zoomAt(0.9, (640, 720))
    show cassidy at blacker, center, zoomAt(0.9, (1140, 720))
    show scottie at blacker, center, zoomAt(0.9, (880, 720))
    with dissolve
    "So I glance up, and that's when I see all of the staff standing before me."
    "And every one of them is looking at me with expectation written across their faces."
    "Looks like they're aware of what Kiara's asked me to do."
    "Or else they've just picked up on the vibes I was giving off during the phone-call just now."
    "Either way, I'm going to have to say something to them."
    menu:
        "Do your best to imitate Kiara's management style" if hero.knowledge >= 50:
            "I have to figure out how to run a place like this, at least for a short while."
            "And I'm wondering how in the hell I'm supposed to do it."
            "But then something occurs to me - I've already seen it done."
            "I've been around here while Kiara was in charge and watched her do it."
            "So maybe all I have to do is copy what I can remember her doing?"
            mike.say "Okay, guys and girls..."
            mike.say "Kiara's running late, and she's left me in charge."
            mike.say "But I want you to carry on as though she was here already."
            mike.say "Just come and see me if you need anything, and I'm sure we'll be fine."
            "I keep my tone positive and make it clear that I have every faith in the staff."
            "Because that's how Kiara seems to do it, believing in them and yet offering leadership."
            hide dwayne casual at blacker
            hide cassidy at blacker
            with easeoutright
            hide emma at blacker
            hide scottie at blacker
            with easeoutleft
            "And it seems to work too, as they all nod and hurry off to do whatever they have to do."
            "Which leaves me to watch over things, doing the best I can to anticipate any problems."
            "And a few of those do occur before Kiara makes it to the club."
            "But because of the space I've given myself, we can handle them before they escalate."
            play music "music/darren_curtis/feel_it_in_your_feet.ogg" loop
            scene bg black
            show bg nightclub
            show layer master at lparty
            with timelaps
            show kiara with easeinright
            "So when Kiara finally walks in, the place is just like it always seems."
            "Calm, relaxed and with everyone doing what they should be doing."
            show kiara talkative
            kiara.say "Ah, [hero.name]…"
            kiara.say "I knew that I could trust you."
            kiara.say "The place looks just the same as when I left it."
            $ kiara.love += 4
        "Do your best to run the club in an efficient manner" if hero.charm >= 50:
            "Looking around the club, I start to realise that this isn't really a problem."
            "No, this is actually a cleverly disguised opportunity for me."
            "Because it means that I can actually run this place how I think it should be run."
            "More than once I've seen how Kiara does things around here and thought there could be improvements made."
            "So I resolve to put those changes in place and prove that I'm right."
            mike.say "Okay, listen up, people..."
            mike.say "Kiara's running late, and she's left me in charge."
            mike.say "And that means we're going to be making a few changes around here."
            mike.say "So listen up, and listen good!"
            "I spend the next fifteen minutes drilling what I want from them into the staff."
            "And I don't let a single one of them out of my sight until I'm sure they get it."
            hide dwayne casual at blacker with easeoutright
            hide emma at blacker with easeoutleft
            hide cassidy at blacker with easeoutright
            hide scottie at blacker with easeoutleft
            "Then I dispatch them all to their new positions, and I watch them like a hawk."
            "Sure, there are a few small hiccups at first, as people adjust to the new way of doing things."
            "But soon enough things begin to run more smoothly and the whole place is buzzing with a new energy."
            play music "music/darren_curtis/feel_it_in_your_feet.ogg" loop
            scene bg black
            show bg nightclub
            show layer master at lparty
            with timelaps
            show kiara with easeinright
            "So much so that, when she finally walks in, Kiara seems to pick up on it herself."
            show kiara talkative
            kiara.say "Ah, [hero.name]…"
            kiara.say "I knew that I could trust you."
            kiara.say "And this place seems to be working better than ever!"
            $ kiara.love += 2
            $ kiara.sub -= 2
        "Do your best to muddle through without committing":
            "Looking around the club, I start to think there might be a way out of this."
            "Because this place was running perfectly well before I walked through the door, wasn't it?"
            "And in all the time I've been on the phone to Kiara, that hasn't changed either."
            "So what if I just...well...leave it that way?"
            "I suppose there's only one way to find out."
            mike.say "Erm..."
            mike.say "Okay, everyone..."
            mike.say "Kiara's running late, and she's left me in charge."
            mike.say "But you don't really need me looking over your shoulders, do you?"
            mike.say "So I'm just going to sit down over here, and leave you to it, okay?"
            "I can see that the staff are all looking at each other in confusion."
            "As if my admitting that there's nobody in charge somehow made them aware of it."
            "And as I sit down in the spot that I'd indicated, they all start milling about."
            "I don't really understand what happens next, but it just seems to get worse."
            show dwayne at blacker, center, traveling(1.0, 0.5, (260, 720))
            show emma at blacker, traveling(1.0, 0.5, (640, 720))
            show cassidy at blacker, traveling(1.0, 0.5, (1100, 720))
            show scottie at blacker, traveling(1.0, 0.5, (820, 720))
            "Instead of going off and doing what they were doing before, they all start asking questions."
            "And before too long the whole place is a mass of chaos and confusion."
            play music "music/darren_curtis/feel_it_in_your_feet.ogg" loop
            scene bg black
            show bg nightclub
            with timelaps
            show kiara stuned with easeinright
            "Which is what Kiara walks into when she finally arrives at the club."
            show kiara talkative
            kiara.say "Ah, [hero.name]…"
            kiara.say "I see things are getting a little hectic in here."
            kiara.say "And I'm guessing that I have you to thank for it?"
            $ kiara.love += 2
            $ kiara.sub += 3
    show kiara normal
    "All I can do is shrug and shake my head."
    mike.say "I just did my best, that's all."
    show kiara evil
    kiara.say "Yes, I can see that."
    kiara.say "Very interesting."
    show kiara smile
    "There's something strange about the tone of Kiara's voice."
    show kiara dreaming
    "Not to mention the way she's looking around at the state of the club."
    "All of which is starting to make me more than a little suspicious."
    mike.say "Kiara..."
    mike.say "This wasn't some kind of test, was it?"
    show kiara evil
    "Kiara smiles and raises one eyebrow in a quizzical manner."
    show kiara talkative
    kiara.say "It might have been."
    kiara.say "But then again, it might not."
    kiara.say "What is important is that it has taught me a lot about you!"
    show kiara normal
    pause 0.5
    scene bg black with dissolve
    $ game.room = "street"
    return

label kiara_event_07:
    if kiara.love.max < 140:
        $ kiara.love.max = 140
    scene bg street2
    show kiara
    with fade
    "I'm used to being at Kiara's side as she runs one of her cafes and exclusive clubs."
    "And evermore these days as she draws me deeper into the web of her underworld activities too."
    scene bg mall1
    show kiara at center, zoomAt(1.0, (640, 740))
    with fade
    "Which is why it feels weird to be walking around the mall with her today instead."
    "Kiara cuts an oddly elegant figure as she strides through the crowds of everyday shoppers."
    "But she insisted that this was where she wanted to spend some time with me today."
    "And there's no way that I can even think of turning down the chance to be at her side."
    mike.say "So..."
    mike.say "When are you going to clue me in, Kiara?"
    "I'm struggling to keep up with Kiara as I ask the question, ducking and weaving through the human throng."
    "But even when she turns her head to look in my direction, Kiara doesn't seem to be having any such problems."
    "In fact it's almost as if the crowds are instinctively parting in order to let her pass with ease."
    show kiara talkative
    kiara.say "Clue you in?"
    kiara.say "But, [hero.name], whatever can you mean?"
    show kiara normal
    mike.say "Oh come on!"
    mike.say "I just want to know why we're here, that's all."
    show kiara talkative
    kiara.say "We are at the mall, are we not?"
    kiara.say "What else would we be here for but to shop?"
    show kiara normal
    "I'm about to ask the obvious question and press Kiara for details."
    "To try to find out exactly what it is that we're supposed to be shopping for."
    "But before I can so that, she stops and grabs me by the shoulders."
    "Turning me so that I'm looking straight at the shop in front of me."
    show kiara talkative
    kiara.say "Aha!"
    kiara.say "Here we are, [hero.name]…"
    kiara.say "The place where all of your questions will be answered!"
    show kiara normal
    "I look the frontage of the shop up and down, recognising it instantly."
    "It's probably the swankiest and most expensive clothes store in the entire mall."
    mike.say "Whoa!"
    mike.say "Wait a second, Kiara..."
    mike.say "I can't go shopping for clothes in a place like that."
    mike.say "The people that work in there will take one look at me..."
    mike.say "And they'll be able to work out that I don't have enough money in my bank account!"
    "Kiara raises an eyebrows and cocks her head to one side."
    "Regarding me with a mixture of interest and amusement."
    show kiara talkative
    kiara.say "Maybe it was like that before..."
    kiara.say "But today, you are here with me."
    kiara.say "And I buy almost all of my clothes here."
    kiara.say "So I promise you, there will be no problems."
    show kiara normal
    "Before I can say another word, Kiara takes my arm."
    "And then she marches straight into the store."
    scene bg clothesshop with fade
    pause 0.3
    show kiara at center, zoomAt(1.0, (340, 740)) with easeinleft
    "As soon as we're inside, it feels like we've stepped into another world."
    "The noise and crowds of the mall vanish in an instant."
    "And they're replaced by a calm environment with the vague hints of classical music in the background."
    show ryan at blacker, center, zoomAt(1.0, (940, 740)) with dissolve
    "Within a couple of seconds of us entering the place, a guy who I take to be one of the salesmen appears."
    "And when I say he appears, I mean it - it's like he just materialises out of nowhere!"
    show ryan at blacker, center, zoomAt(1.0, (940, 740)), startle
    "Salesman" "Greeting, madam...and to the gentleman too."
    show kiara talkative
    kiara.say "Yes, yes..."
    kiara.say "I'm here to check on the items you're preparing for me."
    kiara.say "And for my companion here - to see about upgrading his wardrobe."
    show kiara normal
    "Kiara gestures to me with one hand, and the salesman turns to look in my direction."
    "And before I can say a word, he whips out a tape-measure and starts to use it on me."
    show ryan at blacker, center, zoomAt(1.0, (940, 740)), startle
    "Salesman" "Ooh, yes, sir..."
    "Salesman" "A new wardrobe, sir?"
    "Salesman" "Suit you, sir, suit you!"
    mike.say "What?"
    mike.say "Wait a minute..."
    mike.say "You didn't mention anything about me getting new clothes!"
    show kiara talkative
    kiara.say "But of course, [hero.name]."
    kiara.say "If you are going to be a part of my operation, you will need to look the part."
    kiara.say "So just let the man do his job, and I will take care of the rest."
    kiara.say "The accountants will make sure it is...a tax write-off."
    show kiara normal
    "I think about protesting and flatly refusing to cooperate."
    "More out of principle than anything else."
    "But Kiara doesn't seem to be in the mood to take no for an answer."
    "And I don't want to make a scene in a place like this either."
    "So it looks like I'm just going to have to grin and bear it."
    menu:
        "Make sure your voice is heard":
            "But that doesn't mean I have to just lie back and keep my mouth shut."
            mike.say "Okay, Kiara..."
            mike.say "But I get a veto on anything that I don't like."
            mike.say "I might not have the cash to flash in a place like this..."
            mike.say "But nobody's been dressing me as long as I have!"
            show kiara evil
            "Kiara doesn't say anything in response to my proclamation."
            "But I see that her eyebrows rise and the corner of her mouth curls."
            "As if she appreciates me standing up for myself."
            "And with the slightest nod of her head, she sets everything in motion."
            with fade
            "What follows is one of the strangest experiences of my life thus far."
            "The salesman ushers me in front of a mirror and keeps on taking measurements."
            "I'm used to just knowing my vague size for clothes and picking them off a rack."
            "So having him flit around me, poking and prodding at random, feels weird."
            mike.say "Hey..."
            mike.say "Where are you putting that thing?"
            mike.say "I don't think you need to measure that!"
            "Kiara stands a little way off as all of this is going on."
            "Chuckling softly at my apparent discomfort."
            show kiara talkative
            kiara.say "You must stand still, [hero.name]…"
            kiara.say "We would not want the cut of your pants to be too tight."
            kiara.say "The flow of blood to the extremities is so important!"
            show kiara normal
            "I throw a withering look Kiara's way, showing that I'm not amused."
            "Yet all that seems to do is make her own amusement increase."
            $ kiara.sub += 3
        "Let Kiara take the lead":
            "And things will probably go a lot quicker if I just keep my mouth shut too."
            mike.say "Okay, Kiara..."
            mike.say "But please, you know the kind of stuff I like to wear."
            mike.say "Don't go dressing me up in stuff that makes me look silly."
            mike.say "Remember - you've got to be seen with me too!"
            show kiara evil
            "Kiara doesn't say anything in response to my proclamation."
            "But I see that her eyebrows rise and the corner of her mouth curls."
            "As if she's amused by my pleading for her to be merciful."
            "And with the slightest nod of her head, she sets everything in motion."
            with fade
            "What follows is one of the strangest experiences of my life thus far."
            "The salesman ushers me in front of a mirror and keeps on taking measurements."
            "I'm used to just knowing my vague size for clothes and picking them off a rack."
            "So having him flit around me, poking and prodding at random, feels weird."
            mike.say "Hey..."
            mike.say "Where are you putting that thing?"
            mike.say "I don't think you need to measure that!"
            "Kiara stands a little way off as all of this is going on."
            "Chuckling softly at my apparent discomfort."
            show kiara talkative
            kiara.say "You must stand still, [hero.name]…"
            kiara.say "We would not want the cut of your pants to be too tight."
            kiara.say "The flow of blood to the extremities is so important!"
            show kiara normal
            "I throw a pleading look Kiara's way, which only seems to make things worse."
            "Because she now looks like she's more amused than ever."
            $ kiara.sub -= 3
    "And by the time the salesman returns with stuff for me to try on, she's laughing out loud."
    mike.say "Okay, I have to go into the fitting cubicle to try these on."
    mike.say "I guess you'll still be laughing when I come out, huh?"
    show kiara talkative
    kiara.say "Oh, no, no, no!"
    kiara.say "You cannot do that alone."
    kiara.say "I must be there to help you."
    kiara.say "To make sure that everything fits and looks just right."
    show kiara normal
    "Kiara plucks most of the clothes out of my hands and turns on her heel."
    "Giving me little choice but to follow her as she strides into the fitting cubicle."
    "Once inside, I slide the curtain across the entrance and turn around."
    if kiara.sub >= 0:
        "Just in time to see Kiara deposit the clothes and then kneel down in front of me."
        "And without another word, she proceeds to unzip my flies too!"
        mike.say "Kiara..."
        mike.say "What are you doing?!?"
        show kiara normal
        kiara.say "Shhh!"
        show kiara normal
        "I press my lips together as Kiara slides her hand into my pants."
        "And it gets harder still to stay silent as she proceeds to pull out my cock a moment later."
        "She doesn't pause or even offer an explanation of what she's doing, not that she needs to."
        "And for my part, the thrill of her giving me a blow-job right here is enough to make me complicit."
        "As well as to ensure that I'm already getting hard by the time Kiara manages to pull it all the way out."
        "The way that she's stroking and caressing the shaft soon means that it's fully erect and standing proud."
        "But as we're sneaking the chance to do this thing in a precarious position, Kiara's not wasting any time."
        scene bg black
        show kiara bj happy booth
        with fade
        "Still working the shaft with her hand, she leans forwards and opens her mouth, taking the head inside."
        "As she begins to lick and caress me with her tongue, I feel the sensations of pleasure spreading outwards."
        "And before too long they're getting intense, so much so that I have to brace myself against the cubicle walls."
        "I don't know if Kiara's aware of the effect that she's having on me, or just concentrating on the task at hand."
        "All I do know is that her head is now bobbing back and forth, gaining speed with each passing second."
        play sexsfx1 bj_openmouth
        show kiara bj closed blowjob at stepback(0.09, 10, 0)
        "I can feel my cock getting ever deeper into her mouth, even beginning to push down into her throat too."
        "Kiara has her eyes closed, concentrating on her task, and I can feel the effects of that."
        "The muscles in my legs are already starting to quiver and quake, making me struggle to stay upright."
        "At the same time my heart is pounding in my chest, my breath coming in ragged gasps."
        "I don't know how much longer I'm going to be able to hold on before the inevitable happens."
        play sexsfx1 bj_sucking loop
        show kiara bj at stepback(0.07, 10, 0)
        pause 0.2
        show kiara bj at stepback(0.07, 10, 0)
        "But a moment later, Kiara takes matters into her own hands - or to be more precise, her one free hand."
        "She closes her fingers around my balls and gives them a sudden, sharp squeeze."
        show kiara bj at stepback(0.07, 10, 0)
        pause 0.2
        show kiara bj at stepback(0.07, 10, 0)
        "And the shock of the sensation is more than enough to send a jolt through my entire body."
        "More importantly, it also sets things in motion, making me instantly begin to cum."
        show kiara bj pleasure at stepback(0.07, 10, 0)
        pause 0.2
        show kiara bj at stepback(0.07, 10, 0)
        "Normally there might have been a decision to make as to how this thing would end."
        "But as we're doing it inside of the fitting cubicle, Kiara keeps my cock firmly in her mouth."
        show kiara bj cum blowjob with hpunch
        pause 0.5
        play sexsfx1 bj_gulp
        show kiara bj with hpunch
        "This means that I shoot my load almost straight down her throat, and she swallows it smoothly."
        show kiara bj closed -cum with hpunch
        "And once I'm done, she lets it slide out of her mouth, daintily wiping her lips and beginning to smile."
    else:
        "Only to see that Kiara's already dropped the clothes and is looking straight at me."
        "She points to a spot on the floor in front of her with one hand."
        "The other adjusting the waistband of her skirt."
        show kiara talkative
        kiara.say "Now, [hero.name]..."
        kiara.say "Get down on your knees, right here."
        show kiara normal
        "I'm already moving to do as I'm told, lowering myself down before Kiara."
        "But that doesn't mean I'm not going to ask what she has in mind."
        mike.say "But the clothes?"
        mike.say "How can I try them on down here?"
        show kiara talkative
        kiara.say "Trust me, [hero.name]…"
        kiara.say "They will fit you just fine."
        kiara.say "What I want you to do now is pay me for them!"
        show kiara normal
        "Kiara unfastens her skirt and pulls it aside with a flourish."
        "Which reveals her exquisite legs and the panties at the top of them."
        "The sight should be more than enough to stun me completely."
        "But the truth is that I'm already totally devoted to obeying Kiara's every word."
        scene bg black
        show kiara oral booth
        with fade
        "So she doesn't even need to tell me that she wants me to lick her pussy, right here and now."
        "My brain just kicks in and I start moving without as much as a conscious thought."
        "Reaching out with both hands, I gingerly take hold of Kiara's panties."
        "And then I pull them downwards, slowly revealing the sight of her pussy."
        "As always, it's so pretty that I almost hold my breath as I look it over."
        "Neat and inviting, I can already catch the scent of it on the air."
        "The musky smell telling me that this isn't a spur of the moment thing."
        "Oh no, Kiara must have been getting excited the whole time we've been in the store."
        "And now it's my duty to make sure that she's satisfied before we leave it!"
        "With that in mind, I lean in closer, tilting my head and parting my lips."
        "Knowing that we don't have too much time, I dispense with the foreplay."
        "Deciding to use my lips and tongue, rather than caressing her with my fingers first."
        show kiara oral closed
        "Kissing at the lips of her pussy almost like I was kissing her mouth to mouth."
        "By now I have my eyes closed, relying on touch and feel to guide my actions."
        "The sensation of the soft folds is an exciting mix of smooth textures and sour tastes."
        "And the way that I can feel Kiara moving, hear her moaning softly pushes me onwards."
        "Like I already said, I don't have time to waste, so I push deeper as soon as I can."
        "Probing into the depths of her pussy without pausing, trying to get all the way in there."
        "This seems to be exactly what Kiara was wanting of me, as I feel her brace herself against the walls of the cubicle."
        "And at the same time her whole body is beginning to quiver and quake from my attentions too."
        show kiara oral pleasure hurt
        "My tongue is moving relentlessly, licking and lapping, it's motions like those of a snake."
        "But I can already feel the fatigue building up inside of it by now."
        "And the muscles along its length are threatening to seize up too."
        "Which makes what happens next very lucky indeed."
        "Kiara puts her hands on both sides of my head, holding me in place."
        show kiara oral pleasure ahegao with vpunch
        "And then I feel her pussy clench, its walls squeezing together as she cums."
        with vpunch
        "Her back leant against the rear wall of the cubicle, to keep from collapsing atop me."
    "It only takes a couple of moments for me to gather up the clothes from the cubicle floor."
    "And in the same time, Kiara makes herself decent again, hiding any hint of what we've just done."
    scene bg clothesshop with fade
    "So that once I pull back the curtain and we return to the main part of the store, no one is the wiser."
    "The salesman certainly doesn't seem to know what went down, as he happily bags our purchases and waves goodbye."
    "But all the while, Kiara and I are exchanging glances and secretive smiles."
    "And, as we walk out into the mall, I feel like something really significant has happened between us."
    "Something that's moved our relationship forwards in a subtle, but very important way."
    if not "fancy_clothes" in hero.inventory:
        $ hero.gain_item("fancy_clothes")
return

label kiara_event_08:
    if kiara.love.max < 160:
        $ kiara.love.max = 160
    scene bg street with fade
    "Now that I've got one of the suits on that Kiara and I bought from the fancy clothes store, I have to admit that it feels pretty good."
    "It's not as restrictive or itchy as the suits that I bought off the rack and as cheap as possible in the past."
    "So maybe there really is something in the idea of spending a bit more and feeling the benefits of it?"
    "But the best part of it is definitely the way that the new suits seem to draw extremely approving looks from Kiara herself."
    "Because I keep catching her looking me up and down when she thinks I'm not going to notice, which is very flattering."
    $ game.room = "nightclub"
    play music "music/darren_curtis/feel_it_in_your_feet.ogg" loop
    scene bg nightclub
    show kiara
    show layer master at lparty
    with fade
    "And when I walk into the club tonight, all suited and booted with her at my side, I really feel like I belong."
    "None of the guests as much as blink when they see me, and the staff seem to regard me as only one step removed from Kiara herself."
    hide kiara with easeoutright
    "All in all, I'm looking forward to an evening of seeing just where this new-found air of authority is going to take me."
    show bg door black secure at center, zoomAt(1.5, (640, 1080))
    show kiara at center, zoomAt(1.5, (640, 1080))
    with dissolve
    "But as I make to follow Kiara into the inner sanctum of her office, she puts a gentle hand on my chest to stop me."
    show kiara talkative
    kiara.say "I have some private business that I need to take care of, okay?"
    kiara.say "So I want you to stay out here and give me some privacy."
    show kiara normal
    "I can't help raising my eyebrows in surprise."
    "But it's not like I'm going to deny Kiara her privacy."
    "So I nod and glance around the club."
    mike.say "Sure thing, Kiara."
    mike.say "So..."
    mike.say "You want me to what...hang around out here until you're done?"
    show kiara evil
    "Kiara smiles and lets out a peal of laughter that, to me at least, sounds like the tinkling of exquisite little bells."
    kiara.say "Ha, ha..."
    show kiara talkative
    kiara.say "Oh, [hero.name], you can be so funny sometimes!"
    kiara.say "Of course you will be in charge while I am otherwise engaged."
    show kiara normal
    "I nod for a moment, but then the reality of what Kiara just said hits me."
    mike.say "You..."
    mike.say "You want to leave me in charge of the club - again?!?"
    show kiara talkative
    kiara.say "Well the first time I did so went well, did it not?"
    kiara.say "The place is still standing and we are all alive and well."
    kiara.say "So yes, I think you will do well being in charge for a second time."
    show kiara normal at center, traveling(1.25, 1.0, (640, 900))
    "I open my mouth to argue with Kiara, but she's already turned on her heel."
    play sound door_slam
    hide kiara
    show bg door black secure at center, zoomAt(1.5, (640, 1080))
    with hpunch
    "And the next second the door of her office slams closed, effectively ending the conversation."
    scene bg nightclub
    show layer master at lparty
    with fade
    "Which leaves me to slowly turn around and scan the interior of the club."
    "And the first thing that I realise is the fact that every single member of staff is looking straight at me!"
    "I mean they obviously try as hard as they can to hide it, looking away the second I glance in their general direction."
    "But it's painfully clear that hey heard every word that Kiara just said and saw my reaction too."
    "Okay, okay...when life gives you lemons - learn to suck on the yellow bastards and like it."
    "Taking it as read that everyone knows I'm now in charge, I walk casually over towards the door."
    "Assuming the position that the maitre'd usually occupies to greet guests as they enter the club."
    "Much to my relief, none of the staff seem to react to what I'm doing."
    "My guess is that they reckon it's best to just go along with it, unless something goes drastically wrong."
    "And so I'm kind of relying on the assumption that they'll come running to my aid if that happens."
    "Rather than just sitting back and watching me flounder."
    victor.say "Ah..."
    victor.say "This is Kiara's joint, right?"
    "I can't help jumping a little as I hear the sound of a voice right next to me."
    "One that belongs to someone who was able to almost appear out of thin air."
    show victor normal at center, zoomAt(1.5, (340, 1080)) with vpunch
    mike.say "HUH?!?"
    "I spin around in time to see a rugged-looking guy standing just inside the doorway."
    "He has a pale complexion and black hair, as well as a black suit and shirt to match."
    "He's definitely handsome pulls off his outfit in that annoyingly effortless way some guys can do it."
    "But right now he's kind of reacted to my surprise by tensing and reaching into his jacket."
    "He might just be pulling out his wallet, but then again he might be going for a gun!"
    menu:
        "React to Victor's presence as calmly as you can":
            "Shit - I need to handle this guy quickly."
            "But I can't make it look like I think he's going to shoot the place up."
            mike.say "Would you mind keeping your hands where I can see them, buddy?"
            "I do the best I can to keep my voice even and unthreatening."
            "Holding up my own hands as a sign of what I want him to do."
            show victor surprised
            victor.say "Huh?"
            show victor shout
            victor.say "Oh...oh no..."
            victor.say "I was just going to show you this photo."
            victor.say "And ask if you'd seen the guy in it?"
            show victor normal
            "I raise an eyebrow as the guy produces a photo."
            "And I instantly recognise the person in the centre of it."
            mike.say "You're looking for 'Francois the Frenchman'?"
            mike.say "Well, you're in luck..."
            mike.say "Because he's here tonight."
            "As soon as the words are out of my mouth, the guy makes to walk past me."
            show victor surprised at center, traveling(1.5, 0.2, (640, 1080))
            pause 0.2
            with hpunch
            "But I can already see where this is going, and so I move to block his path."
            show victor surprised
            victor.say "Ah..."
            victor.say "What are you doing?"
            show victor normal
            mike.say "Pardon me, but I can see the bulge under your jacket."
            mike.say "And I know that Francois is a man with a lot of enemies."
            mike.say "But I can't let you...handle him in the club."
            show victor upset
            "The guy narrows his eyes as he looks at me."
            "As if he's trying to size me up as a threat."
            show victor angry
            victor.say "Well what if I don't agree to that?"
            show victor upset
            mike.say "Then things are going to get messy, aren't they?"
            mike.say "Look, how about this..."
            mike.say "I have you escorted to the VIP section and give you a drink on the house."
            mike.say "And then, when Francois leaves, I have someone come and inform you."
            mike.say "Then you can slip out into the alleyway round the back..."
            mike.say "Where it's nice and dark, and there are no security cameras?"
            "For a moment I think the guy's going to pull his gun on me."
            show victor normal
            "But then he sets his mouth in a frown and nods."
            "I click my fingers and summon someone over to take care of him."
            scene bg vip
            show layer master at lparty
            with fade
            "And it's not until he's safely in the VIP area that I start to hyperventilate."
            show kiara talkative at center, zoomAt(1.0, (990, 760))
            kiara.say "My, my..."
            kiara.say "You realise that was a hitman?"
            show kiara normal at center, traveling(1.5, 0.5, (640, 1080))
            "Kiara's walked up behind me, just like everyone seems to be doing tonight."
            "But by now, I'm too exhausted to jump or be freaked out."
            mike.say "Yeah...I guessed he might be."
            show kiara talkative
            kiara.say "I'm impressed, you handled that well."
            kiara.say "Maybe you were always meant to do something like this?"
            show kiara normal
            $ kiara.sub += 3
        "Try to make Victor wait until Kiara's free to deal with him":
            "Oh man - where's Kiara when I really need her!"
            mike.say "N...n...no guns!"
            "There's no way I can keep myself calm."
            "Or hide the panic that's creeping into my voice."
            show victor surprised
            victor.say "Huh?"
            show victor shout
            victor.say "Oh...oh no..."
            victor.say "I was just going to show you this photo."
            victor.say "And ask if you'd seen the guy in it?"
            show victor normal
            "I shake my head as the guy produces a photo."
            "Too racked with anxiety to even be able to focus on it."
            show kiara talkative at center, zoomAt(1.25, (900, 900)) with easeinright
            kiara.say "You're looking for 'Francois the Frenchman'?"
            kiara.say "Well, you're in luck..."
            kiara.say "Because he's here tonight."
            show kiara normal
            "I feel a surge of relief as Kiara steps between me and the guy."
            "Blocking his path as he tries to walk straight past me and into the club."
            show victor shout
            victor.say "Ah..."
            victor.say "What are you doing?"
            show victor normal
            show kiara talkative
            kiara.say "Pardon me, but I can see the bulge under your jacket."
            kiara.say "And I know that Francois is a man with a lot of enemies."
            kiara.say "But I can't let you...handle him in the club."
            show kiara normal
            show victor upset
            "The guy narrows his eyes as he looks at Kiara."
            "As if he's trying to size her up as a threat."
            show victor angry
            victor.say "Well what if I don't agree to that?"
            show victor upset
            show kiara talkative
            kiara.say "Then things are going to get messy, aren't they?"
            kiara.say "Look, how about this..."
            kiara.say "I have you escorted to the VIP section and give you a drink on the house."
            kiara.say "And then, when Francois leaves, I have someone come and inform you."
            kiara.say "Then you can slip out into the alleyway round the back..."
            kiara.say "Where it's nice and dark, and there are no security cameras?"
            show kiara normal
            "For a moment I think the guy's going to pull his gun on Kiara."
            show victor normal
            "But then he sets his mouth in a frown and nods."
            play sound "<from 1.4 to 2.6>sd/SFX/humans/finger_snap.ogg"
            "She clicks her fingers and summons someone over to take care of him."
            hide victor
            show kiara talkative at center, zoomAt(1.25, (640, 900))
            with fade
            "And it's not until he's safely in the VIP area that I start to hyperventilate."
            mike.say "You...you..."
            mike.say "You realise that was a hitman?!?"
            show kiara talkative
            kiara.say "Yeah...I guessed he might be."
            kiara.say "Did you happen to take note of how I handled him?"
            kiara.say "Because it seems like you need lessons on that kind of thing."
            show kiara normal
            $ kiara.sub -= 3
        "Try to keep Victor from entering the club":
            "All of a sudden I can see it all play out inside of my head."
            "Me ducking for cover and this guy spraying the whole place with bullets."
            "The staff going down as they're hit before they even know what's happening."
            "Then Kiara emerging from her office and being struck down too."
            "No, I can't let that happen - I have to do something, and now!"
            mike.say "HE'S GOT A GUN!"
            show victor surprised
            victor.say "Huh?"
            victor.say "Who's got a..."
            show victor upset fly at center, zoomAt(1.5, (640, 1080)) with hpunch
            "Before the guy in black can finish what he's saying, I'm on him."
            "Throwing myself atop him and trying to grab for the weapon he's pulling."
            "For a moment it looks like I was wrong, because there's no gun there."
            "But the guy seems to move faster than I could ever hope to."
            show victor gun
            "And in the blink of an eye, there really is a gun in his hand."
            with hpunch
            "We end up grappling with each other, limbs everywhere."
            play sound gun
            pause 0.2
            with screenshot
            "But as I feel us tumble to the ground, there's a loud bang."
            "I don't seem to feel anything as the gun goes off and the bullet pierces my chest."
            "At least not any kind of pain."
            "Just a sudden rush of cold and the sensation that all feeling is ebbing away."
            "I lose consciousness even before I hit the ground."
            scene bg black with dissolve
            "And then there's darkness."
            "Then nothing."
            pause 1.0
            $ renpy.full_restart()
    return

label kiara_event_09:
    if kiara.love.max < 200:
        $ kiara.love.max = 200
    $ game.room = "nightclub"
    play music "music/darren_curtis/feel_it_in_your_feet.ogg" loop
    scene bg nightclub
    show layer master at lparty
    with fade
    "I'm finally starting to feel comfortable with the idea of being a part of Kiara's...legitimate business empire."
    "Standing by her side and helping to make sure everything runs smoothly, tackling issues before they become problems."
    "Hell, even the people that she has working for her are beginning to see me as a figure of authority too."
    "I mean, obviously not as much as they do Kiara herself, but maybe to the point where they see me as her right-hand man."
    "But all of these new responsibilities come with a lot of new stuff to learn and a great deal of running about too."
    scene bg vip
    show kiara
    with fade
    "So it comes as a genuine but welcome surprise to walk into the VIP area of the club and find it empty, save for Kiara."
    "She's standing by one of the tables that seems to have been set out with places for two diners."
    "And as she turns around to face me, I see that she also has a bottle of wine in her hands."
    mike.say "Oh..."
    mike.say "Hey, Kiara..."
    mike.say "Are we expecting special guests tonight?"
    mike.say "Because I didn't see anything on the schedule."
    "Kiara raises an eyebrow at the question, setting the bottle down on the table as she does so."
    show kiara talkative
    kiara.say "Oh yes, [hero.name]…"
    kiara.say "This table will be hosting the most special guests of all."
    kiara.say "Tonight you and I will be enjoying a meal while sitting at it."
    show kiara normal
    "I can't help blinking in genuine surprise at the news."
    "We've been so busy recently that it feels like we haven't stopped."
    "And the thought of doing anything so indulgent has been a million miles away from my mind."
    mike.say "Really?"
    mike.say "That sounds like a great idea!"
    mike.say "But what's the occasion?"
    if kiara.sub <= 50:
        "Kiara looks me straight in the eye and gestures around her."
        show kiara talkative
        kiara.say "I thought that it was time we celebrated."
        kiara.say "Marked the occasion of you becoming a part of my...business empire."
        kiara.say "An intimate meal, to symbolise how intimately we are now entwined."
        show kiara normal
        "I can't help beginning to feel a little nervous as Kiara talks about her business."
        "Because even now that I'm a part of it, I still find it equal parts thrilling and terrifying."
        "And there's no way that I'm going to object to a plan the likes of that."
        mike.say "That's a great idea, Kiara!"
        mike.say "You're right that you've been working hard."
        mike.say "And you deserve something nice - like you're rewarding yourself."
    else:
        "Kiara shrugs and shakes her head, trying to look as casual as she possibly can."
        "Which, knowing her as well as I do, instantly makes me think she's anything but."
        show kiara talkative
        kiara.say "No particular reason..."
        kiara.say "Does there need to be a reason?"
        kiara.say "Apart from how hard we've both been working recently?"
        show kiara normal
        mike.say "Actually, we should be celebrating how far we've come, you know?"
        mike.say "Since you first let me into your secret world."
        mike.say "And because now I feel like I'm really a part of it."
        show kiara smile
        "Kiara smiles and nods, eager to agree with me."
        "And I sense that's what she wanted to hear the whole time."
        show kiara talkative
        kiara.say "Exactly that!"
        show kiara normal
    "It's only now that I realise I can catch the scent of something pretty amazing on the air."
    "And as I inhale, the smell already beginning to make me feel hungry, Kiara puts her hand on the back of a chair."
    show kiara talkative
    kiara.say "I hope you are hungry, [hero.name]…"
    kiara.say "Because I have gone to the trouble of putting together the menu myself."
    kiara.say "And everything is traditional, recipes from the old country."
    show kiara normal
    "Realising that my sudden hunger is making me forget my manners, I leap into action."
    "Hurrying to pull out the chair Kiara's hand is resting on, as I try to be a gentleman."
    mike.say "Here, let me help you with that."
    "Kiara nods happily, allowing me to help her."
    "And then I scoot back around to the other side of the table and sit down myself."
    mike.say "It certainly smells amazing."
    mike.say "And I've got to say that I'm excited to try it out too."
    mike.say "I feel like there's so much for me to learn about your culture."
    "Kiara nods and then waves a hand in the air, clicking her fingers."
    "The sound is so loud that I can't help jumping a little."
    "And almost the second after it fades, the club staff start appearing with the food."
    "Hell, one of them even pops up to uncork and pour the wine!"
    show kiara talkative
    kiara.say "It is important to me that you become steeped in my people's ways."
    kiara.say "That you become one of the family, bound to me by blood."
    show kiara normal
    "I have a glass of the wine in my hand, swigging away as Kiara talks."
    "And it's so damn good that I can't help knocking almost half of it back in record time."
    "The only problem is that it must be bloody strong too, as I can already feel the effects."
    mike.say "Whoo!"
    mike.say "Y...yeah, Kiara..."
    mike.say "I am totally up for all of that stuff."
    mike.say "You can think of me as...as one of the family."
    "The food's arrived in front of us, and Kiara motions for me to tuck in."
    "And, as soon as I do, I find that it's every bit as good as the wine."
    "Hearty, satisfying and extremely filling - I feel like I could get used to this!"
    "Kiara leans in closer as we eat, telling me tales about her homeland."
    "And reeling off stories about the many, many relatives she seems to have back there."
    "Somehow I didn't notice it before, but there's mood music playing subtly in the background too."
    "Strings that remind me of some movie that I can't quite recall the name of."
    "And then it hit's me, like a bolt from the blue."
    "So I lean forwards, forgetting that I have a mouthful of food."
    mike.say "Hey..."
    mike.say "Isn't this from that movie?"
    mike.say "The one set in Sicily?"
    mike.say "Where the guy says something about...an offer you can't refuse?"
    "The food in my mouth means that I mumble and mutter the words."
    "But rather than being offended, Kiara looks at me in genuine surprise."
    show kiara surprised
    kiara.say "[hero.name]…"
    kiara.say "You sound just like my old godfather!"
    show kiara normal
    "Oddly, the sound of me speaking with my mouth full seems to have affected Kiara on an emotional level."
    "Because she now looks like she's come to a decision on some important matter, setting her jaw and nodding her head."
    show kiara talkative
    kiara.say "Yes..."
    kiara.say "I believe this is a sign."
    kiara.say "A sign that you are destined to be joined to my family in blood!"
    show kiara normal
    "I get the distinct impression that Kiara's expecting me to do something in response to that statement."
    "That she wants me to make some kind of dramatic gesture that shows my commitment to her."
    "But just what would an appropriate act look like?"
    "I mean, does she want me to shed blood?"
    "Or whack one of her enemies with a machine-gun?"
    if kiara.sub <= 50:
        "I'm still pondering the problem when Kiara reaches over the table."
        "And then she takes a firm hold of my hands, looking me straight in the eye."
        show kiara talkative
        kiara.say "I have taken the time to nurture you, [hero.name]…"
        kiara.say "I have tended and watered you, like a flower."
        kiara.say "And now, you must bloom!"
        show kiara normal
        mike.say "Erm..."
        mike.say "I'm not very good with horticultural references, Kiara."
        mike.say "Would you mind putting that in simpler terms?"
        show kiara talkative
        kiara.say "[hero.name], you must agree to marry me!"
        show kiara normal
        "The words finally seem to start making sense to me."
        "But the problem is that, as soon as they do, they set my head reeling all over again."
        "Because I think that Kiara just asked me to marry her."
        "Though it sounded more like an order than a request."
        menu:
            "Agree to marry Kiara":
                "But it's not like I need time to really consider my answer."
                "Almost as soon as the words are spoken, I know what it's going to be."
                mike.say "Of course I will, Kiara!"
                mike.say "That'd make me the happiest man in the world."
                hide kiara
                show kiara kiss
                with fade
                "I make to stand up, and Kiara follows my example, throwing her arms around me at the same time."
                "And the kiss that follows seems to seal the deal as much as her actually saying yes."
                $ lexi.set_fiance()
                $ kiara.love +=5
                $ kiara.sub -=5
            "Refuse to marry Kiara":
                "And so there's no way that I can even hope to give her an honest answer."
                "No, what I need is more time to really be able to think about it."
                mike.say "Erm..."
                mike.say "Do you really need an answer now?"
                mike.say "Or can I have some time to think about it?"
                show kiara stuned
                "Kiara looks at me with a mixture of surprise and disappointment in her eyes."
                hide kiara with easeoutright
                "I make to stand up, but Kiara's already on her feet and walking away."
                "Leaving me still kneeling on the floor, and the meal apparently over."
                $ kiara.sub +=5
                $ kiara.love -=20
    else:
        "But then it hits me."
        "The answer is so bloody obvious!"
        "Pushing back my chair, I slide off it to kneel on the floor."
        "And then I look up at Kiara, taking hold of her hand."
        mike.say "Okay, this is going to sound crazy..."
        mike.say "And I know that I don't have a ring or anything..."
        mike.say "But, Kiara..."
        mike.say "Will you marry me?"
        if kiara.sub <= 25 or kiara.sub >= 50:

            "Kiara's eyes blaze with intense emotion as soon as she hears my words."
            "And her head is soon nodding, letting me know that we're on the same wavelength."
            show kiara talkative
            kiara.say "Oh, [hero.name]…"
            kiara.say "It is like you have read my mind!"
            kiara.say "Yes, of course I will marry you - then you really will be part of the family!"
            hide kiara
            show kiara kiss
            with fade
            "I make to stand up, and Kiara follows my example, throwing her arms around me at the same time."
            "And the kiss that follows seems to seal the deal as much as her actually saying yes."
            $ lexi.set_fiance()
            $ kiara.love +=5
        else:

            "Kiara frowns as she listens to my proposal, brows furrowing more with each passing second."
            "And her head is soon shaking, letting me know that we're miles apart on this one."
            show kiara talkative
            kiara.say "No, [hero.name]…"
            kiara.say "I will not marry you."
            kiara.say "And I think that I have also lost my appetite."
            hide kiara with easeoutright
            "I make to stand up, but Kiara's already on her feet and walking away."
            "Leaving me still kneeling on the floor, and the meal apparently over."
            $ kiara.love -=20
    return

label kiara_male_ending:

    if renpy.has_label("kiara_achievement_3") and not game.flags.cheat:
        call kiara_achievement_3 from _call_kiara_achievement_3
    $ game.hour = 16
    $ game.room = "church"
    show bg church wedding with fade
    if "kiara_event_09" in DONE:
        "Guys are just like girls in that they always imagine what their wedding day is going to be like."
        "Any guy that says he doesn't or hasn't is a damn liar, and you can quote me on that, okay?"
        "But the one thing that I never imagined there would be on my wedding day was so many dudes in dark suits."
        "And as I take the time to look around the chapel, I don't just mean the men that are populating the pews."
        "Everywhere I look, I can see a burly-looking guy in a suit and sunglasses, watching the proceedings."
        "And every one of them has a worrying bulge under their jackets too, right where a pistol holster would be!"
        "Oh, and that's all before you notice the scars, tattoos and general surliness of the guys in the pews too."
        "There's not one of them that I'd want to meet in a dark alleyway, or, come to think of it, a well-lit one either."
        "In fact I could swear that I've seen some of those scary faces on the news, or in wanted posters around town..."
        "Before I can truly start focussing in on the most familiar faces, there's the sudden sound of music."
        "And I recognise the tune that Kiara chose for making her grand entrance today."
        "As one the assembled guests turn their heads to gaze at the doors of the chapel."
        "Which proceed to swing open at the perfect moment, as if this were a scene in a movie."
        show kiara wedding at center, zoomAt(1.0, (640, 720)) with dissolve
        "And when Kiara sweeps into sight, walking down the aisle, there's an audible gasp."
        "But then why wouldn't there be?"
        "She looks more fantastic than I can ever remember her looking, like a damn goddess even."
        "The dress that she's chosen is more like something that I'd say belongs in her own wardrobe."
        "You know, rather than the kind of thing a bride of a more traditional bent might wear?"
        "And it works too, as I can't take my eyes off of her!"
        if kiara.is_visibly_pregnant:
            "Hell, I Love every detail of it - even where it's been let out to accommodate her belly."
            "The growing curve of it reminding me of the fact that Kiara's well into her term by now."
            "Not to mention all the fun that we had trying to get her into that state in the first place!"
        else:
            "She was the most glamorous woman I'd ever seen the first time I walked into her café."
            "And there's no way that I can imagine meeting another with more mystique than she has."
            "Or a bride that's able to move like the femme fatale in a black and white movie."
        show kiara at center, traveling (1.5, 5.0, (640, 1040))
        "All of those heads turn to follow Kiara as she makes it to the end of the aisle."
        "Even the guys with the bulges in their jackets watching as she reaches the altar."
        "And I notice that she has a knowing smile on her face as she comes to stand beside me."
        show kiara talkative at center, zoomAt(1.5, (640, 1040))
        kiara.say "Oh, [hero.name]…"
        kiara.say "If only my father could see us now."
        kiara.say "He would be all like 'you come to me on my daughter's wedding day'!"
        show kiara normal
        show wedding kiara with fade
        "I'm about to make another joke based on a certain genre of movies."
        "But then the other person standing at the altar chooses that moment to butt in."
        "Priest" "Ey…"
        show wedding kiara priest with dissolve
        "Priest" "What are we waitin' for here?"
        "Priest" "Let's get things moving, capiche?"
        "To be perfectly honest, Kiara was the one that arranged for the priest to officiate."
        "And he kind of reminds me of the sort of guys that come to drink in her club's VIP area."
        "Which means that he also frightens me and I'm not about to ignore his wishes either."
        mike.say "Oh..."
        mike.say "Oh yeah..."
        mike.say "Fine my me!"
        "Priest" "Alright then..."
        "Priest" "Ladies and Made Men..."
        "Priest" "We're gathered here today..."
        "Priest" "To marry this lovely lady..."
        "The priest points to Kiara."
        "Priest" "To dis here meatball of a guy."
        "And then he jerks his thumb in my general direction."
        "From there the service goes pretty much as you'd expect it to."
        "Well, apart from the rather unusual vocabulary of the priest delivering it."
        "Something that becomes even more apparent when we finally make it to the vows."
        "Priest" "Okay..."
        "Priest" "Do you, Kiara..."
        "Priest" "Take this guy to be your wedded husband?"
        "Priest" "And do you, like, promise not to have him whacked?"
        "Priest" "I mean, like, unless he really has it coming?"
        "My eyes are almost popping out of their sockets as Kiara answers."
        kiara.say "I do."
        "Priest" "Beautiful!"
        "Priest" "And do you, [hero.name]…"
        "Priest" "Take this dame, to be your wedded wife?"
        "I'm fully expecting the priest to tac on a line about whacking Kiara."
        "And when he doesn't, I'm left floundering and looking like I've frozen up."
        "Priest" "Hey..."
        "Priest" "Did you hear me, pally?"
        mike.say "Ah..."
        mike.say "Y...yeah..."
        mike.say "I sure do!"
        "Priest" "I suppose that'll do it."
        "Priest" "So if any of youse that's sittin' there..."
        "Priest" "If you got any beef about these two being wed..."
        "Priest" "Speak up now, or shut ya damn yap!"
        "Almost as soon as the priest has made the proclamation, a murmur spreads through the entire chapel."
        "And it's not the usual bit of humour that accompanies this little moment of tradition in the ceremony."
        "Because Kiara already warned me that this is where one of her rivals might try to crash the party."
        "The guys in their sunglasses are all sticking a hand into their jackets, poised to be ready."
        "And I can see more than a few people in the pews that look as though they're sweating too."
        "Priest" "Okay, okay..."
        "Priest" "Looks like we aint got any takers dis time."
        "Priest" "So by the power vested in me..."
        "Priest" "I declare you husband and wife - now get outta here!"
        show wedding kiara -priest with dissolve
        "The sense of relief that floods through me is both genuine and palpable."
        "Making my legs a little wobbly as I turn to face Kiara."
        scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
        show kiara kiss wedding
        with fade
        "But the moment that she throws her arms around my shoulders, I know it's going to be okay."
        "And the kiss that we share in the following seconds seems to erase all of my worries too."
        "We did it, we actually managed to tie the knot."
        "We're husband and wife - I'm married to the mob!"
        scene bg black with dissolve
        pause 0.5
        show kiara ending
        with fade
        kiara.say "So what you're saying is that you want me to be brutally honest?"
        kiara.say "To talk about how [hero.name] and I first met and how we got to where we are today?"
        kiara.say "Well, if that's what you really want, you'd better be prepared for what it gets you."
        kiara.say "I'll be frank with you - when I first met [hero.name], I was not instantly impressed."
        kiara.say "You must understand that he was just another one of the boys that turned up at the café."
        kiara.say "One of so many that followed on the heels of the girls that worked for me there, you know?"
        kiara.say "But it was Bree's heels on which he followed, one of the more interesting and intelligent girls."
        kiara.say "And if she tolerated him, then I at least knew that there must be some redeeming quality in there."
        kiara.say "At first I only spoke to him in passing, being polite and yet keeping slightly aloof."
        kiara.say "Of course he was drawn to me, like most young men would have been in his position."
        kiara.say "That may sound arrogant of me to say, but I know that I have been blessed with beauty."
        kiara.say "And even more so, I have learnt to use that beauty to my advantage with others."
        kiara.say "So I did what any woman with a mind of her own would have done in my position."
        kiara.say "I made small-talk and asked [hero.name] the occasional question, carefully noting his answers."
        kiara.say "And much to my surprise, I found that they were charismatic and interesting."
        kiara.say "Soon enough I began to enjoy his company when he would come to the café, trailing after Bree."
        kiara.say "And when he did not, I would feel a small pang of disappointment, but hide it from view."
        kiara.say "I flatter myself in this, but I believe that it did not take long for [hero.name]'s allegiance to change."
        kiara.say "Before too long it was apparent that he was no longer coming to the café to see Bree."
        kiara.say "Instead he was there in the hope of seeing me, which I found oddly thrilling."
        kiara.say "Because as you no doubt understand, I am a woman that has a standing in the underworld."
        kiara.say "So it is hardly like I need the attention of a younger man to add excitement to my life."
        kiara.say "Perhaps I thought that it was a passing thing, a fling for the both of us that would soon fade."
        kiara.say "But when the relationship between us only became more intense, I made a fateful decision."
        kiara.say "I vowed that I would test [hero.name] by bringing him into my own hidden world."
        kiara.say "At first he was shocked, that was plain to see."
        kiara.say "But I believe it was his growing affection for me that made his persevere."
        kiara.say "Little by little I introduced him to my businesses and showed him how things were done."
        kiara.say "And while there was some stumbling along the way, he adapted and evolved until he became useful to me."
        kiara.say "All the while that was happening, our love was becoming more intense."
        kiara.say "The fact that I was growing to need him getting all the more obvious."
        kiara.say "[hero.name] was not born to work in an office, oh no!"
        kiara.say "He was born to stand at my side, as we wield a pair of matching machine-guns."
        kiara.say "Making the gutters run red with the blood of our enemies!"
        kiara.say "Naturally he quit his day-job, and now he's my right-hand man."
        if kiara.is_visibly_pregnant or kiara.flags.mikeBabies >= 1:
            kiara.say "Oh, and I should mention that he is also a devoted family man."
            kiara.say "Already making sure that our little boy Michael is trained in the family business."
            kiara.say "All in anticipation of the day when he takes the reigns himself."
        else:
            kiara.say "Oh, and I do not think it will be long before [hero.name] gives me an heir."
            kiara.say "A child with all the combined ruthlessness of their parents."
            kiara.say "The perfect apprentice to be trained to take the reigns in turn."
        kiara.say "I mean, there is the small matter of how the police keep on hounding us."
        kiara.say "Threatening to prosecute us for something as petty and stupid as tax-avoidance!"
        kiara.say "But they are no real concern for us, because there is always a way out."
        kiara.say "[hero.name] and I have already spoken about retiring to the old country."
        kiara.say "If they come after us, then that is where we will go."
        kiara.say "And once there, we will rule our new domain with an iron fist."
        kiara.say "We will ride through the streets like the robber-barons of old."
        kiara.say "And it will be glorious!"
    else:
        call kiara_male_ending_b from _call_kiara_male_ending_b

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not kiara.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_26
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_26
    scene bg black with dissolve
    pause 1.0
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label kiara_event_07b:
    if kiara.love.max < 140:
        $ kiara.love.max = 140
    scene bg street2 at center, zoomAt(1.0, (640, 720)) with fade
    "I'm still not one hundred percent sure that I understand what Kiara's motivation is in asking me to take her to the mall."
    "Because it's not exactly the kind of place that springs to mind when I think of someone as stylish and sophisticated as her."
    "But it's also not like I'm going to turn down the chance to spend some quality time with a woman as hot as she is either."
    "And so I make sure that I'm standing at the entrance to the mall at the exact time that we agreed to meet."
    show kiara casual dreaming at center, zoomAt(0.9, (940, 720)) with easeinright
    "Though I'm reminded of my confusion when Kiara strides up, dressed to kill and getting admiring glances all round."
    "Oh man, she looks like she should be on a red carpet in Hollywood, not hanging around the local mall!"
    mike.say "Hey..."
    mike.say "Kiara..."
    mike.say "Over here!"
    "As soon as she hears the sound of my voice, Kiara looks around, searching for me."
    show kiara normal
    "And the moment that she sets eyes on me, her face seems to genuinely light up."
    show kiara talkative at center, traveling(1.25, 0.5, (640, 900))
    kiara.say "Oh..."
    kiara.say "Hi there, [hero.name]…"
    kiara.say "Hope I'm not running late or spoiling your vibe?"
    show bg street2 at center, traveling(1.25, 1.0, (640, 880))
    show kiara normal at center, traveling(1.5, 1.0, (640, 1080))
    "I can't help frowning as I walk the short distance over to where Kiara's standing."
    show kiara talkative
    kiara.say "What's up, friend?"
    kiara.say "Why are you shooting me that look?"
    show kiara normal
    mike.say "Erm..."
    mike.say "Because you don't normally talk like that, Kiara..."
    mike.say "And it's weird hearing you trying to sound like a teenager!"
    show kiara annoyed
    "Now it's Kiara's turn to frown, and she lets out a sigh of frustration."
    show kiara whining
    kiara.say "Oh bother!"
    kiara.say "Is it really that obvious?"
    show kiara sadsmile
    mike.say "Yeah, it kind of is."
    show kiara pout
    kiara.say "Hmm..."
    show kiara irritated
    kiara.say "Well that's annoying."
    show kiara talkative
    kiara.say "I wanted to be able to fit in with all of the other people at the shopping mall."
    kiara.say "So you're going to have to teach me how to do it."
    show kiara normal
    "My brain's starting to tie itself in knots by now."
    mike.say "Wait a minute..."
    mike.say "You want me to teach you to fit in at the mall?"
    show kiara talkative
    kiara.say "Not just at the mall, [hero.name]…"
    kiara.say "I want you to help me become average and normal - just like you!"
    show kiara normal
    "I stare at Kiara for a moment, trying to process what she just told me."
    "Is she actually asking me to teach her how to behave like an average joe?"
    "Like that film where the guy shows the common girl how to be sophisticated, but in reverse?"
    mike.say "But why, Kiara?"
    mike.say "You're classy and...well, mysterious..."
    "I make a point of not mentioning the fact she also seems to be some kind of underworld kingpin."
    mike.say "Why would you want to be more like an average schlub?"
    scene bg mall1
    show kiara normal casual at center, zoomAt(1.5, (640, 1080))
    with fade
    "Kiara wraps her arm in mine, and then she proceeds to begin walking me into the mall."
    show kiara talkative
    kiara.say "You might think that my life is all fun and excitement, [hero.name]."
    show kiara whining
    kiara.say "But the truth is that, beneath a thin veneer of style, it is empty."
    kiara.say "There is nothing real, nothing that will last - and no love!"
    show kiara talkative
    kiara.say "I so desperately want what you have, a life that is real."
    show kiara sadsmile
    "I have to admit that Kiara's kind of blowing my mind right now."
    "There's no way I'd have thought someone like her was jealous of my lifestyle."
    "Or that she'd plead with me to show her how to achieve it for herself."
    "But here we are, and I guess that I should really be flattered."
    "Kiara's asking me to introduce her to my world, so the least I can do is try."
    show kiara normal
    mike.say "Okay, Kiara..."
    mike.say "I'll do my best."
    mike.say "So, first things first - why do we come to the mall?"
    show kiara talkative
    kiara.say "Because we desire to purchase something."
    kiara.say "And one of the stores here sells the thing."
    show kiara stuned
    mike.say "Wrong!"
    mike.say "We come to the mall to hang out and socialise."
    show kiara surprised
    kiara.say "You come to a temple of consumerism in order to relax?"
    kiara.say "To a place that is crowded and noisy, with advertisements thrust into your face?!?"
    show kiara stuned
    "I think about what Kiara's saying, and it kind of makes sense."
    "But I need to make her understand the kind of socialising I mean."
    show kiara normal
    mike.say "Maybe relaxing isn't the right way to put it."
    mike.say "Perhaps exciting would be better?"
    "By now we're standing outside the amusement arcade."
    "And I can feel an idea forming inside of my head."
    mike.say "Like this place, Kiara..."
    mike.say "I love coming in here to play games."
    scene bg arcade with fade
    pause 0.5
    show kiara casual stare at center, zoomAt(1.5, (640, 1080)) with easeinright
    "Kiara looks around as I lead her inside the arcade."
    "Her eyes wide as she takes in all the flashing lights."
    show kiara talkative
    kiara.say "I understand games like poker and roulette."
    show kiara whining
    kiara.say "But surely these are games for children?"
    show kiara sadsmile
    mike.say "For children?"
    mike.say "Are you kidding?!?"
    mike.say "There games are genuine classics, Kiara."
    mike.say "Hell, there are even people that play them on a professional level!"
    show kiara dreaming
    "Kiara doesn't seem convinced, so I decide to show her that I'm right."
    "Looking around for the perfect arcade cabinet to prove my point."
    menu:
        "Choose a light-gun game":
            "And that's when I spot the 'Virtual Cop' cabinet."
            "One of the classic light-gun games from back in the day."
            show kiara sadsmile
            mike.say "Come on, Kiara..."
            mike.say "Let's try this one out."
            "Kiara reluctantly follows me over to the cabinet and waits as I pump in the coins."
            "Then takes the brightly-coloured plastic pistol that I hand her."
            mike.say "Okay, you have to shoot all the gangsters that come onto the screen."
            mike.say "And when you run out of bullets, shoot away from the screen to reload."
            show kiara pout
            "I see Kiara's brows furrow as I mention shooting gangsters."
            "But the game begins before I can worry too much about it."
            mike.say "Here we go!"
            show game arcade kiara at center, zoomAt(1.25, (780, 880)) with fade
            "An alarm-bell rings and blocky, polygonated figures run around on the screen."
            "A cheesy depiction of a bank robbery playing out before us."
            "I must have played this game a thousand times in the past."
            "So I'm instantly poised to take my first shot..."
            "But then I see each and every robber before me felled in short order."
            "Soon enough the second wave pops up, and the same thing happens again."
            "I haven't gotten off a single shot, and Kiara's cleaning house!"
            mike.say "What the hell?!?"
            "I turn my head to see Kiara standing with the pistol held in a double-handed stance."
            "And without as much as a blink, she nails another wave of villains."
            kiara.say "Hmm..."
            kiara.say "I can see how this would be a fun distraction."
            kiara.say "It's almost like the real thing."
            $ kiara.love += 2
        "Choose a platform game":
            "And that's when I spot the 'Mega Plumber Siblings' cabinet."
            "One of the classic platform games from back in the day."
            mike.say "Come on, Kiara..."
            mike.say "Let's try this one out."
            "Kiara reluctantly follows me over to the cabinet and waits as I pump in the coins."
            "Then I point her towards one of the joysticks on the front of the cabinet."
            mike.say "Okay, you have to jump on all of the enemies that come on the screen."
            mike.say "And you need to collect as many of the coins as possible too."
            "I see Kiara's brows furrow as I mention the mechanics of the game."
            "But the game begins before I can worry too much about it."
            mike.say "Here we go!"
            show game arcade kiara at center, zoomAt(1.25, (780, 880)) with fade
            "The cheery music begins to play, and the screen shows a two-dimensional, cartoonish environment."
            "With two short, moustachioed sprites for Kiara and me to control waiting to get things moving."
            "I must have played this game a thousand times in the past."
            "So I'm more than ready to start jumping, squashing and smashing."
            "But the first thing that Kiara's sprite does is run backwards."
            mike.say "What the hell?!?"
            mike.say "Where are you going?"
            kiara.say "How would I even know?"
            kiara.say "I have a joystick and two buttons..."
            kiara.say "What do they even have to do with making the little man move?"
            "I watch as one of the enemy sprites closes in on Kiara's guy."
            "And then I wince as the familiar sound of him dying fills the air."
            kiara.say "What happened?"
            mike.say "Erm..."
            mike.say "You just died."
            mike.say "So maybe we should try something else?"
            $ kiara.love -= 2
    scene bg arcade
    show kiara casual at center, zoomAt(1.5, (640, 1080))
    with fade
    "Part of me would like to stay and play some more games with Kiara."
    "But I want to show her more of the wonders to be found in the mall."
    scene bg mall1
    show kiara casual at center, zoomAt(1.5, (640, 1080))
    with fade
    "And so we head out of the arcade and back into the thronging crowds."
    show kiara talkative
    kiara.say "So you don't actually come here to buy anything?"
    kiara.say "Just to play frivolous games?"
    show kiara normal
    "As Kiara asks the question, we just so happen to be passing a particular store."
    "And an idea hits me as we do so, inspiring my answer and the direction in which I now steer her."
    mike.say "Oh no, Kiara..."
    mike.say "There's a very real social aspect to it as well."
    mike.say "Because if one of your buddies works at the mall..."
    mike.say "Then you can always pop in and catch up with them."
    scene bg electronic with fade
    pause 0.5
    show kiara casual stare at center, zoomAt(1.5, (640, 1080)) with easeinleft
    "I say all of this as Kiara and I are walking into the electronics store."
    "And I can already see Shawn standing behind the counter, looking as harassed as ever."
    show kiara pout
    kiara.say "Hmm..."
    show kiara talkative
    kiara.say "But isn't your friend supposed to be working?"
    kiara.say "You would be getting him in trouble with his boss, would you not?"
    show kiara normal
    mike.say "Not if he IS the boss..."
    mike.say "Hey, Shawn!"
    show kiara casual stare at center, traveling(1.25, 0.3, (340, 900))
    show shawn work smile at center, zoomAt(1.25, (940, 900)) with easeinright
    "Shawn looks up as soon as he hears my voice, his face breaking into a smile."
    show shawn stuned
    "But then he sees Kiara at my side, and I swear that his jaw literally drops."
    show shawn surprised
    shawn.say "[hero.name]…"
    shawn.say "Who..."
    shawn.say "Who's...your friend?"
    show shawn stuned
    "I can't help grinning as Shawn openly gapes at Kiara."
    "Loving the fact that he's bowled over by her beauty."
    mike.say "Shawn, this is Kiara..."
    mike.say "Kiara, this is Shawn."
    show kiara talkative
    kiara.say "Charmed to meet you, Shawn."
    show kiara normal
    show shawn talkative
    shawn.say "Y...yeah..."
    shawn.say "Likewise!"
    shawn.say "Is there, like...anything I can do for you guys?"
    show shawn normal
    "Trying to play it cool, I lean nonchalantly on the counter."
    mike.say "Nah, not really..."
    mike.say "Kiara and I are just on a date, you know?"
    mike.say "Checking out the mall and hanging out in general?"
    show shawn stuned
    "By now it looks to me like Shawn's eyes are going to pop out of their sockets."
    "And I honestly believe that I'm going to remember this feeling for the rest of my life."
    "But that doesn't mean Shawn's going to be cowed into submission quite so easily."
    show shawn sadsmile
    "Because I can already see him doing all that he can to recover his composure."
    show shawn talkative
    shawn.say "Well in that case, it makes perfect sense to come in here."
    shawn.say "We sell only the very finest in modern, electrical consumer goods."
    shawn.say "Everything you see before you is top of the line and very exclusive."
    show shawn normal
    "Shawn gestures around him, encouraging us to look around."
    "And I've got to admit, the place does look very shiny and impressive."
    show kiara pout
    "But I see that Kiara's frowning a little, like she doesn't agree."
    show kiara talkative
    kiara.say "No, I think that you are mistaken."
    show kiara sadsmile
    show shawn embarrassed
    shawn.say "I...I don't know what you mean."
    show shawn sadsmile
    show kiara talkative
    kiara.say "Many of the products on your shelves are not genuine."
    kiara.say "They are imitations, made cheaply and passed off as the real thing."
    show kiara normal
    show shawn embarrassed
    shawn.say "What are you even talking about?"
    show shawn sadsmile
    show kiara talkative
    kiara.say "Fakes, packed into shipping containers and smuggled past customs."
    kiara.say "I would recognise them anywhere."
    show kiara normal
    show shawn sad
    "I can see that Shawn's starting to sweat as Kiara keeps on talking."
    "Looking around as though he's afraid of the other customers in the store overhearing her."
    menu:
        "Step in to help Shawn":
            "Okay, I know that it's fun to watch Shawn squirm."
            "But we are supposed to be here to teach Kiara how to behave like a normal person."
            "And dropping hints about smuggling rings and fake consumer goods is definitely not normal."
            mike.say "Lighten up, Shawn..."
            mike.say "Don't you know a joke when you hear one?"
            show shawn stuned
            show kiara pout
            "Shawn blinks in surprise."
            "But then looks instantly happier as his brain seizes the way out I'm offering him."
            show shawn embarrassed
            shawn.say "Oh..."
            show shawn happy
            shawn.say "Oh yeah, good one, Kiara..."
            shawn.say "You almost had me there!"
            show shawn normal
            "Before Kiara can protest, I nod to Shawn."
            scene bg mall2
            show kiara casual at center, zoomAt(1.5, (640, 1080))
            with fade
            "And then I steer her away from the counter and out of the store."
            show kiara irritated
            kiara.say "What did you do that for?"
            kiara.say "I was not making a funny joke!"
            show kiara pout
            mike.say "Erm..."
            mike.say "Maybe drop the underworld info-dumps in future, yeah?"
            mike.say "It's not really the vibe we're going for here."
            $ kiara.love -= 2
            $ kiara.sub += 2
        "Back up Kiara and torment Shawn":
            "Okay, I know that I really should be stepping in to stop Kiara here."
            "But it's just too much fun watching Shawn squirm."
            mike.say "Oh-oh..."
            mike.say "Sounds like someone's in trouble!"
            mike.say "What happened, Shawn - did it all fall off the back of a lorry?"
            show shawn stuned
            "By now Shawn's eyes are wide with panic."
            "And he's waving his hands for us to be quiet."
            show shawn angry
            shawn.say "Shhh!"
            show shawn vangry
            shawn.say "Shut up, shut up, shut up..."
            shawn.say "Stop talking, or I'll have no choice but to ban you from the store!"
            show shawn upset
            "I can't help laughing to myself as I lead Kiara out of the store."
            scene bg mall2
            show kiara casual at center, zoomAt(1.5, (640, 1080))
            with fade
            "Leaving Shawn having kittens behind us and staring at his precious stock."
            show kiara pout
            kiara.say "Hmm..."
            show kiara talkative
            kiara.say "So I am thinking that was not such a good idea?"
            kiara.say "And that I should not be talking about such things in future?"
            show kiara normal
            mike.say "Oh, man..."
            mike.say "Seeing Shawn piss his pants like that was priceless."
            mike.say "But you're probably right, Kiara."
            $ kiara.love += 2
            $ kiara.sub -= 2
    show bg mall2
    show kiara normal
    with dissolve
    "Kiara and I wander further into the mall, talking about everything and nothing."
    "But occasionally I notice that some of the people we pass nod, or wave in her direction."
    "At first I just put it down to the fact that Kiara's one stunning sight to behold."
    "Then I notice that she's actually responding in a similar manner as well."
    mike.say "Kiara..."
    mike.say "Do you, like, know those people?"
    mike.say "I thought you said the mall wasn't the kind of place you normally come to?"
    show kiara dreaming
    "Kiara looks like she's going to deny it for a second."
    show kiara normal
    "But then she nods her head."
    show kiara talkative
    kiara.say "Not everyone that's a part of the underworld hides themselves away."
    kiara.say "Many of them are all around us, going about their daily lives."
    show kiara guilty
    kiara.say "For example, that man over there is currently wanted in at least three countries."
    kiara.say "Because he did away with his boss and then ground up the body in a mincing machine."
    kiara.say "They say that he flushed what was left down the..."
    "I make a point of deliberately looking in the opposite direction to one Kiara's pointing in."
    "Desperate not to see the supposed crazed murderer that she's trying to show me."
    show kiara stuned
    mike.say "OKAY!"
    mike.say "Okay...I get the picture."
    mike.say "There are scary people everywhere."
    show kiara normal
    "Kiara shrugs, as if it's no big deal that I don't want to know."
    "And as we walk deeper into the mall, I start to think that she's right."
    "The further the two of us can get from the world she's tyring to leave behind, the better."
    scene bg black with dissolve
    pause 0.5
    return

label kiara_event_08b:
    if kiara.love.max < 160:
        $ kiara.love.max = 160
    scene bg park with fade
    "After our trip to the mall, I feel like my quest to acclimatise Kiara to the non-criminal world is going well."
    "But I feel like my efforts were hampered by the sheer number of other people who we were around on that particular day."
    "So for the next stage of the process, I've arranged for Kiara to meet me at the entrance to the park."
    "Though I've also made a point of not telling her what exactly it is that we're going to be doing there."
    show kiara at center, zoomAt(0.9, (340, 720)) with easeinleft
    "This means that when I see her walking towards me, she has a look of intrigue on her face and a twinkle in her eye."
    show kiara at center, traveling(1.25, 1.0, (640, 900))
    "And when I wave to let her know that I've seen her, Kiara waves back and quickens her pace, making it to me in the blink of an eye."
    show kiara talkative
    kiara.say "[hero.name]…"
    kiara.say "I hope that I am not late?"
    show kiara normal
    mike.say "Oh no, you're right on time."
    "I don't even need to pull out my phone before I shake my head, dismissing Kiara's fears."
    "Because the truth is that I really don't care if Kiara's on time or running pretty late."
    "She looks so good and I'm so excited to be spending some time with her today, that nothing else seems to matter."
    show kiara talkative
    kiara.say "I must say that I am intrigued to know what we are here for."
    kiara.say "The mystery has kept me guessing ever since you invited me along."
    show kiara normal
    "By way of an answer, I hold up the picnic hamper that I've been hiding behind my back."
    mike.say "Well guess no longer, Kiara..."
    mike.say "We're going to be having a picnic!"
    "Kiara's face lights up at the sight of the hamper, and she claps her hands together too."
    "All of which serves to make me feel pretty smug, like I've made the perfect choice."
    show kiara talkative
    kiara.say "Oh, [hero.name]…"
    kiara.say "I have always seen such things, in movies and on the television."
    kiara.say "But I have never been invited to go along on one before now."
    show kiara normal
    "Holding the hamper in one hand, I offer the other to Kiara."
    "Making sure to offer her a smile to match her own at the same time."
    mike.say "Then I'm happy to be the first person to do so!"
    mike.say "Come on, Kiara, let's go find the perfect spot."
    "Kiara doesn't hesitate to take hold of my hand, squeezing it tightly."
    show bg pond with dissolve
    "And then I lead the way into the park, still basking in her enthusiasm for my plan."
    "Most of the time and effort involved in preparing for today went into the picnic itself."
    "It's not like I took the time to come down to the park and scout out the best possible spot."
    "But luckily for me the park isn't too busy, despite the fact that it's a pretty nice day."
    "Kiara and I stroll down the paths and then onto the grass, considering various spots."
    scene bg black
    show harmony_picnic_bg
    if game.season == 0:
        show harmony_picnic_bg_spring
    elif game.season == 1:
        show harmony_picnic_bg_summer
    else:
        show harmony_picnic_bg_fall
    with fade
    "And in the end we settle on one that's just at the edge of the wooded part of the park."
    "The shade of the leaves above us offering some relief from the heat of the sun."
    "But the pleasant blue of the sky still hanging over us at the same time."
    "I pull out the rug I brought along for the occasion, spreading it on the grass."
    show kiara casual at center, zoomAt(1.35, (540, 720)) with easeinleft
    pause 0.3
    show kiara at center, traveling(1.5, 1.0, (640, 1100))
    "Then we both sit down on it, and I begin taking out the food I've packed."
    "Okay, I'll level with you now - I'm not the most talented chef in the world."
    "So a lot of the stuff I'm producing is fairly basic and uncomplicated in nature."
    "But much to my relief, that doesn't seem to bother Kiara in the slightest."
    "I guess the novelty of what we're doing is more than enough to make up for it."
    "Kiara watches patiently as I fuss about, setting everything up."
    show kiara mischievous
    "And when I'm done, she looks at me with expectation in her eyes."
    "Though it takes me a moment to realise why she's not actually doing anything yet."
    "She already told me that she's never been on a picnic before."
    "So how would she know what the correct etiquette for one is?"
    menu:
        "Tell Kiara to just dig in and help herself":
            "I chuckle and gesture to the food spread out in front of us."
            mike.say "There's no need to be shy, Kiara..."
            mike.say "Feel free to try anything that takes your fancy."
            show kiara delicious
            "Kiara nods and does as I say, trying a little here and a little there."
            "And soon enough we're eating and chatting away happily."
            "Looking for all the world like any other couple having a picnic."
            $ kiara.sub -= 2
        "Offer to feed Kiara titbits from the picnic":
            "I pluck a few choice titbits onto a plate."
            "And then I make a point of shuffling closer to Kiara."
            mike.say "You might want to try a little sample first."
            mike.say "So maybe let me help you choose?"
            "Kiara seems to be very taken with the idea."
            show kiara delicious at center, traveling(1.75, 1.0, (640, 1200))
            "As she leans in close and lets me feed her from the plate."
            "Making pleasant sounds as she samples the food I've prepared for her."
            "And more than once managing to lick and nibble at my fingers too."
            "Something that certainly doesn't bother me in the slightest!"
            $ kiara.sub += 2
    scene bg pond at center, zoomAt(1.2, (640, 720)) with fade
    "It still seems to be pretty quiet in the park as the picnic goes on."
    "Only the occasional dog-walkers and strollers passing by our spot on the grass."
    "And the truth is that I'm way too interested in Kiara to be paying attention to anyone else."
    show victor at center, zoomAt(0.65, (340, 720)) with easeinleft
    "So when a guy in a dark suit appears a little way off, I do the best I can to ignore him."
    "Sure, he looks out of place in the middle of the park and he must be hot in all that black."
    "But the way I see it, that's his problem and not mine."
    scene bg black
    show harmony_picnic_bg
    if game.season == 0:
        show harmony_picnic_bg_spring
    elif game.season == 1:
        show harmony_picnic_bg_summer
    else:
        show harmony_picnic_bg_fall
    show kiara smile at center, zoomAt(1.5, (640, 1100))
    with fade
    "And that's when I remember that I brought a bottle of something special along."
    "So I reach into the hamper and pull it out, already tearing the foil from around the cork."
    show kiara talkative
    kiara.say "Oh my..."
    kiara.say "What is this?"
    kiara.say "Champagne?"
    show kiara normal
    mike.say "Well..."
    mike.say "It's not from that part of France..."
    mike.say "So technically you can't call it that!"
    play sound champagne volume 1.2
    show kiara stuned
    "Suddenly there's a loud popping sound, and the cork is no longer in the neck of the bottle."
    "Of course this means that the contents start spurting out like a fountain."
    "And I scramble to pour it into the nearby glasses before it's all spilled."
    show kiara surprised
    kiara.say "But however did you do that?"
    kiara.say "You were not even touching the cork!"
    show kiara stuned
    mike.say "I don't know..."
    mike.say "I guess it must have been the change in pressure or something like that?"
    play sound glass_broken volume 1.2
    "A second later there's yet another sound, but this time it's a crystalline shattering."
    show kiara c at center, traveling(1.75, 0.2, (940, 1440))
    "And the pair of us duck instinctively as the neck of the bottle literally explodes."
    with vpunch
    mike.say "AAARGH!"
    show kiara angry c
    kiara.say "Get down!"
    show kiara upset c
    victor.say "Ah, shit!"
    "It's as I dive for cover that I remember there's only the two of us on the picnic."
    "So where in the hell did that third voice come from?"
    show victor gun upset at center, zoomAt(1.0, (340, 720)) with easeinleft
    "Looking up, I get my answer, as I see the odd guy in the dark suit."
    "He's standing a little way off from out blanket, but looking straight at us."
    "But even more incriminating is the fact there's a silenced pistol in his hand."
    "And he seems to be struggling to reload it in hope of firing again!"
    "I'm about to suggest something along the lines of running for our lives."
    show kiara a
    "But Kiara beats me to it, looking the would-be assassin straight in the eyes."
    show kiara surprised at center, traveling(1.5, 0.3, (940, 1100))
    kiara.say "Victor!"
    show kiara guilty
    kiara.say "What are you doing?!?"
    kiara.say "And since when were you such a terrible shot?"
    show kiara uninterest
    mike.say "You..."
    mike.say "You know this guy?!?"
    show kiara guilty
    kiara.say "Only in a professional sense."
    kiara.say "He is one of the better hitmen for hire around these parts."
    kiara.say "And in the past, I was the one hiring him, not his target."
    show kiara uninterest
    "In the time that's passed while we were speaking, Victor hasn't remained idle."
    "He's managed to reload his pistol and close the distance between us."
    "But for some reason he hasn't even tried to take another shot yet."
    "Almost like he's distracted by something and unable to concentrate."
    show victor shout
    victor.say "Ah..."
    show victor sadsmile
    victor.say "It's nothing personal, Kiara..."
    victor.say "Just business, you know that, right?"
    show victor normal
    "Victor holds up a hand to Kiara, like he's asking her for a momentary pause."
    "And then he turns his attention to me instead."
    show victor shy
    victor.say "Erm..."
    show victor shout
    victor.say "Quick question - is that rice pudding?"
    victor.say "Like, in the little pots?"
    show victor normal
    "The sheer strangeness of the question almost floors me."
    "But I can't see any other logical thing to do than answer it."
    "As he is the one that's holding the loaded gun right now."
    mike.say "Erm..."
    mike.say "Yeah, it sure is, buddy."
    show victor happy
    victor.say "Oh, man - I thought so!"
    show victor sadsmile
    victor.say "I was sure they didn't make it anymore."
    victor.say "And I used to love that stuff when I was a kid."
    victor.say "That's why I missed the shot - I was so surprised!"
    show victor normal
    "I'm nodding and trying to tell Victor all that he wants to know."
    "Because all of this has got my brain turning over pretty fast."
    "And I think that I can fathom a way out of this situation."
    menu:
        "Try to use the rice pudding to bribe Victor":
            "I bend down slowly and pick up one of the pots of rice pudding."
            "And then I hold it out to Victor, nodding for him to come closer."
            mike.say "You want one?"
            mike.say "We've got enough to spare."
            show victor gun upset at center, traveling(1.25, 1.0, (440, 720))
            "He edges forwards cautiously, until he's close enough to take it."
            "At which point he has to holster his pistol to be able to do so."
            "Then Kiara and I watch in silence as he peels off the lid and eats a little."
            victor.say "Mmm…"
            show victor shout
            victor.say "Oh yeah, that takes me back!"
            show victor normal
            "Victor proceeds to take another mouthful."
            "And then he doesn't seem to be able to stop."
            "As he eats the entire contents of the pot."
            show victor shout
            victor.say "Aw, man..."
            victor.say "That's put me in such a good mood."
            victor.say "There's no way I can kill anyone now!"
            hide victor with easeoutleft
            "With that, Victor turns on his heel and walks away."
            show kiara bothered
            "Leaving Kiara and I to let out a gasp of relief and thanks for being spared."
        "Leave it to Kiara to talk Victor down":
            "I was going to try and use Victor's apparent love of rice pudding to save our asses."
            "But suddenly I realise how downright stupid that sounds even inside of my head."
            "So I pause, hoping to be able to come up with something else if I rack my brains."
            "And it's in that same moment that I hear Kiara speak up."
            show kiara guilty
            kiara.say "You know what all of this is about, don't you, Victor?"
            kiara.say "You realise why they hired you to take me out?"
            show kiara uninterest
            show victor shout
            victor.say "Ah..."
            victor.say "Rumour is that you've lost it, Kiara..."
            victor.say "That you're a liability."
            show victor normal
            show kiara guilty
            kiara.say "I'm trying to go straight, Victor - to leave that life behind."
            kiara.say "Isn't that what you tried to do, before they dragged you back in?"
            show kiara uninterest
            show victor upset
            "Victor visibly stiffens as Kiara asks him the question."
            "And I can see that she's getting under his skin more with each passing second."
            show victor shout
            victor.say "Maybe you're right..."
            victor.say "But that doesn't change anything."
            show victor normal
            show kiara guilty
            kiara.say "Well how about if I give you something, Victor?"
            kiara.say "Something that you can use to make it out again?"
            show kiara dreaming
            "Kiara holds up key that she's produced from somewhere."
            "A key that looks pretty mundane, like it'd open a locker at a train station somewhere."
            show kiara guilty
            kiara.say "Find the locker, and use the information inside of it."
            show kiara dreaming
            "For a moment I think that Victor's going to ignore the offer."
            "That he's actually going to pull the trigger on us."
            "But then he nods and holds out his empty hand."
            "Kiara tosses the key, and he catches it neatly."
            hide victor with easeoutleft
            "With that, Victor turns on his heel and walks away."
            show kiara bothered
            "Leaving Kiara and I to let out a gasp of relief and thanks for being spared."
        "Use the rice pudding to throw at Victor":
            "I bend down slowly and pick up one of the pots of rice pudding."
            "All the time making out that I'm going to hand it over to Victor."
            "But at the last moment I instead hurl the thing straight at his head."
            show kiara stuned
            show victor surprised at startle
            "He instinctively goes to shield himself with his hands."
            "And in doing so, he must have inadvertently pulled the trigger."
            play sound silencer
            "Because I hear the sound of the gun going off again."
            "Only this time there's no shattering or popping sound."
            "Just a stab of pain in my chest, and then I begin to feel cold."
            "I hardly notice myself collapsing onto the ground."
            scene bg black with dissolve
            "Because my vision is growing dim, fading away to nothing."
            "And in a few more moments there's nothing at all left."
            pause 0.5
            $ renpy.full_restart()
    scene bg black with dissolve
    return

label kiara_event_09b:
    if kiara.love.max < 200:
        $ kiara.love.max = 200
    play sound cell_vibrate
    "I feel my phone vibrating in my pocket, just the once to indicate that I've received a message."
    "And so I pull it out, not really devoting all of my brain to the task as I do so."
    $ nvl_mode = "phone"
    nvl clear
    "But the moment that I see Kiara's name on the screen, I hurry to open the message."
    "Because I'm always more than eager to see what she has to say to me."
    kiara_nvl "[hero.name], meet me at the club..."
    kiara_nvl "Come as quickly as you can..."
    kiara_nvl "I will explain when you get here."
    "My eyes dart from side to side as I read and then reread the short lines that Kiara's sent to me."
    "And, of course, my mind instantly starts to race on account of the vagueness of what I find there."
    "What on earth could have happened to her that's so serious?"
    "And why would she choose to go back to the club after leaving it behind?"
    "I think about sending a message back and asking all of these questions."
    $ nvl_mode = None
    "But in the end I decide that the best thing would be to do as Kiara asked."
    scene bg house with fade
    "And so I drop everything and rush to the location of Kiara's club."
    "All the while the craziest scenarios imaginable are playing out inside of my head."
    scene bg street with fade
    "So much so that by the time I'm a few streets away, I'm jogging along."
    "But then I see the first tell-tale signs of smoke ahead of me."
    "And the unmistakable scent of it hits my nostrils a second later."
    "That's when I break into a run, unable to keep myself from beginning to panic."
    scene bg alley
    show fx fog
    show layer master at police_lights
    with dissolve
    "Turning the corner, I see my fears confirmed - the club is no longer standing."
    "In its place is a blackened mass of burnt timbers and warper girders."
    "There's no sign of the fire that must have consumed the place."
    "But fire crews and police are still milling around beyond temporary barriers."
    "Looking this way and that, I begin desperately searching for Kiara."
    with hpunch
    mike.say "KIARA?"
    mike.say "WHERE ARE YOU?"
    kiara.say "Here, [hero.name]…"
    kiara.say "I am here."
    "It's impossible to describe the sense of relief that washes over me when I hear her voice."
    show kiara date sad at center, zoomAt(0.9, (940, 720))
    show kiara at center, traveling(1.75, 0.5, (640, 1140))
    "And when I turn to see Kiara hurrying towards me, I throw my arms wide and fly to her too."
    "A moment later she's wrapped in my arms, and I can't help but hold her in a crushing embrace."
    "Almost like I'm afraid that she's going to be snatched away from me without warning."
    mike.say "Kiara..."
    mike.say "I was so worried!"
    mike.say "I thought that..."
    show kiara talkative
    kiara.say "No, [hero.name]…"
    kiara.say "I am safe, as you can see."
    show kiara dreaming at center, traveling(1.5, 0.5, (640, 1040))
    "Kiara pulls back from my embrace a little as she says this."
    "Just enough for her to be able to look up at the scene before us."
    show kiara guilty
    kiara.say "Which is more than can be said for those who were inside the club."
    show kiara uninterested
    "It's only now that I see there are ambulances at the scene, as well as fire engines and police cars."
    "Their crews engaged in the grim task of carrying out stretchers covered with sheets."
    mike.say "What happened here, Kiara?"
    mike.say "Was there some kind of accident?"
    mike.say "You know, like a gas leak or something?"
    show kiara pout
    "Kiara lets out a grim chuckle and shakes her head."
    show kiara talkative
    kiara.say "Ha!"
    kiara.say "Most likely that's what it will have been made to look like."
    kiara.say "And so that is what the official cause will be recorded as."
    show kiara sadsmile
    mike.say "You..."
    mike.say "You mean this was done on purpose?"
    mike.say "Like, it was Arson?!?"
    show kiara normal
    "Kiara nods."
    show kiara whining
    kiara.say "The world that I chose to leave behind is a cruel and brutal one."
    kiara.say "And the moment that I did so, my former rivals would have begun plotting."
    kiara.say "Either they wanted to claim this place for themselves, or deny it to others."
    kiara.say "Whichever it was, you can see why I made my decision to get out when I did."
    kiara.say "I just regret that my choice has been so costly for others."
    show kiara unhappy
    "On the one hand I'm relieved that Kiara managed to escape the fire herself."
    "But on the other, I can feel how deeply this is affecting her."
    menu:
        "Assure Kiara that this is not her fault":
            mike.say "You can't blame yourself for this, Kiara."
            mike.say "Sure, you were once a part of this world."
            mike.say "But you weren't the one that started it all."
            mike.say "Something like this would have happened no matter what you chose to do."
            show kiara sadsmile
            "Kiara nods again, as if she's accepting the logic of what I'm saying."
            "But it doesn't seem to be helping to improve her mood any."
            show kiara whining
            kiara.say "You are right to say such things."
            kiara.say "Though they do not absolve me of my guilt."
            kiara.say "That, I believe, will take time to come."
            $ kiara.sub -= 4
        "Tell Kiara this proves she should have gotten out sooner":
            mike.say "This just proves how right you were to get out, Kiara."
            mike.say "If anything, you maybe should have done it sooner."
            mike.say "I'm just glad that you did decide to do it."
            mike.say "And that you weren't in there when this happened."
            show kiara sadsmile
            "Kiara nods her head, as if she's accepting the logic of what I'm saying."
            "Even though it's maybe not as sympathetic as I could have made it."
            show kiara talkative
            kiara.say "You are right to say these things."
            kiara.say "And the guilt that I feel is a heavy weight to bear."
            kiara.say "But it is still preferable to dying in that fire!"
            $ kiara.sub += 4
    kiara.say "Which is why there is something I have to ask of you."
    show kiara sadsmile
    "I note the sudden change in Kiara's tone, as if she's becoming more serious."
    show kiara serious
    "Channelling the last reserves of her energy to be able to do so as well."
    mike.say "Huh?"
    mike.say "What's that, Kiara?"
    show kiara talkative
    kiara.say "I cannot interpret this as anything but a sign that my old life is truly over."
    kiara.say "And so now I am totally committed to the new one that we have been making together."
    kiara.say "Which means that I must ask - [hero.name], will you make me your wife?"
    show kiara blank
    "For a moment I don't really seem to hear what Kiara just said to me."
    "The words are all familiar, but I've never heard them in that combination before."
    "But then it hits me, and not for the first time today, my mind reels at the implications."
    menu:
        "Agree to marry Kiara":
            "I know that Kiara's just gone though a pretty traumatic experience."
            "And maybe the more sensible thing to do would be to wait a while."
            "At least until she's had the chance to get her head back together."
            "But that's not the part of me which is making the decisions right now."
            "And so the answer I give comes from the more emotional part of me."
            "The one that's keen to do all it can to comfort and support Kiara."
            mike.say "Of course I will, Kiara!"
            show kiara normal
            mike.say "I know that we don't have a ring or anything like that."
            mike.say "So I can't make a traditional proposal..."
            mike.say "But we'll get one as soon as we can."
            show kiara talkative
            kiara.say "Oh, [hero.name]…"
            kiara.say "None of that matters."
            kiara.say "All that really matters is that you said yes!"
            hide kiara
            show kiara kiss date
            with fade
            "Kiara pulls me closer, putting her lips softly against mine."
            "And the kiss that follows serves to seal the pact we just made."
            $ kiara.set_fiance()
            hide kiara
        "Ask Kiara for more time to think about it":
            "I can see why Kiara would be asking me that at a time like this."
            "She's just suffered a pretty big dose of trauma."
            "She's seen former friends hurt or even killed."
            "But maybe that's why making such a big decision right now is a bad idea."
            mike.say "I don't think now is the time for that, Kiara."
            mike.say "You're still reeling from the fire right now."
            mike.say "Let's give you some time to recover, okay?"
            mike.say "Then we can make the decision with clearer heads."
            "Kiara looks disappointed with my answer, which is understandable."
            "But she seems to get the logic of what I'm saying, as she nods."
            show kiara talkative
            kiara.say "Ah..."
            kiara.say "You see things more clearly than I."
            kiara.say "And perhaps you are right."
            kiara.say "So we shall wait, as you say, for the dust to settle."
            $ kiara.love -= 10
            $ kiara.sub -= 10
    show kiara date uninterest at center, zoomAt(1.5, (640, 1040))
    with fade
    "Kiara and I stand there, locked in each other's embrace."
    "Watching in solemn silence as the emergency services go about their grim tasks."
    "And I can't help thinking that we're also watching a definitive end to Kiara's former life."
    "Whilst standing on the brink of a totally new one that's only just beginning."
    return

label kiara_male_ending_b:
    "I can't help being nervous as I stand at the altar, waiting for the moment when my bride walks in."
    "The suit that I'm wearing felt perfectly comfortable when I tired it on before, but now it seems tight."
    "Likewise I remember the chapel feeling light and spacious, whereas now the walls seem to be closing in on me."
    "I keep telling myself that it's all down to nerves, trying to regulate my breathing and think positively."
    "But every time I look around, I see the faces of all the guests that we've invited looking back at me."
    "And it feels like every one of them is silently asking me why the hell Kiara isn't here yet."
    "Like they're thinking that she's not going to show up and the whole wedding day is going to turn into a farce!"
    "And oh god - what if they're right?"
    "What if..."
    "Suddenly the sound of music fills the air, the track that Kiara chose reaching my ears."
    "And all of my fears vanish in an instant as the doors to the chapel swing open."
    show kiara a wedding at center, zoomAt(1.0, (640, 720)) with dissolve
    "In that same moment, every head in the room turns at the same time, gazing backwards."
    show kiara a at center, traveling (1.5, 20.0, (640, 1040))
    "Just in time to see Kiara come sweeping down the aisle and begin walking towards he altar."
    "And believe me, she looks more fantastic than I can ever remember seeing her look before."
    "Kiara wanted everything about the wedding to be as traditional as possible."
    "So this is the first time that I've seen the dress, let alone her in it."
    "The thing is a vision of pure white, flattering Kiara's striking beauty."
    "And all of the majestic presence she used to give off as an underworld kingpin is still there."
    "Only now she's somehow managed to channel it into a very different vibe indeed."
    "Now Kiara looks like the perfect bride, demure and understated in her demeanour."
    if kiara.is_visibly_pregnant:
        "Even the fact that she's getting close to full-term is taken into account."
        "The cut of her dress subtle accommodating the curve of her belly."
        "Serving as a reminder of the fact we'll soon be a family."
    else:
        "I've watched over the past few months as Kiara slowly shed her former identity."
        "And been there with her every step of the way as she crafted a new one."
        "So seeing her like this feels like we've come to the end of a long journey together."
    "All in all, the effect of finally seeing Kiara in her wedding dress is stunning."
    "So stunning, in fact, that I'm left staring and speechless when she gets to the altar."
    show kiara at center, zoomAt(1.5, (640, 1040))
    "My mouth opening and closing, but with no words or coherent sounds coming out of it."
    "And before Kiara can say anything herself, the priest speaks up."
    "Priest" "Ahem..."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today, to join these two people..."
    "Priest" "In the bonds of holy matrimony."
    "You know how it goes from there, right?"
    "The priest goes on at length about the beauty of commitment."
    "Using flowery language to paint a picture of the wedded bliss that awaits us."
    "And neither of us actually needs to say another word until her gets to the vows."
    "Priest" "Do you, Kiara..."
    "Priest" "Take this man..."
    "Priest" "To be your lawful, wedded husband?"
    "Kiara answers without missing a beat."
    show kiara talkative
    kiara.say "I do."
    show kiara normal
    "Priest" "And do you, [hero.name]…"
    "Priest" "Take this woman..."
    "Priest" "To be your lawful, wedded wife?"
    "Luckily for me, my answer is almost as effortless."
    mike.say "I do."
    "The priest nods."
    "Priest" "Then I call upon all those here present..."
    "Priest" "That if you know of any lawful reason that these two many not be married..."
    "Priest" "Speak now, or forever hold your peace!"
    "Of course there's the usual pause and ripple of nervous laughter from the guests."
    "But I'm genuinely worried as I wait for the moment to pass and the service to go on."
    "Because this would be the perfect point for Kiara's former life to crash the proceedings."
    "For armed hitmen to kick open the doors and spray the inside of the chapel with bullets!"
    "So when the priest starts talking again, I can't hide my genuine relief."
    "Priest" "Very good."
    "Priest" "By the powers vested in me, I pronounce you husband and wife."
    "Priest" "You may kiss the bride."
    "I don't hesitate to do as the priest says pulling Kiara into a tight embrace."
    hide kiara
    show kiara kiss wedding
    with fade
    "And the kiss that follows is equal definitely tinged with the relief I'm feeling."
    "But the largest part of it is the love that exists between us."
    "The same love that we've just celebrated by the joining of our lives."
    "And the promise of the future that awaits us."
    scene bg black with dissolve
    pause 0.5
    show kiara ending
    with fade
    kiara.say "So what you're saying is that you want me to be brutally honest?"
    kiara.say "To talk about how [hero.name] and I first met and how we got to where we are today?"
    kiara.say "Well, if that's what you really want, you'd better be prepared for what it gets you."
    kiara.say "I'll be frank with you - when I first met [hero.name], I was not instantly impressed."
    kiara.say "You must understand that he was just another one of the boys that turned up at the café."
    kiara.say "One of so many that followed on the heels of the girls that worked for me there, you know?"
    kiara.say "But it was Bree's heels on which he followed, one of the more interesting and intelligent girls."
    kiara.say "And if she tolerated him, then I at least knew that there must be some redeeming quality in there."
    kiara.say "At first I only spoke to him in passing, being polite and yet keeping slightly aloof."
    kiara.say "Of course he was drawn to me, like most young men would have been in his position."
    kiara.say "That may sound arrogant of me to say, but I know that I have been blessed with beauty."
    kiara.say "And even more so, I have learnt to use that beauty to my advantage with others."
    kiara.say "So I did what any woman with a mind of her own would have done in my position."
    kiara.say "I made small-talk and asked [hero.name] the occasional question, carefully noting his answers."
    kiara.say "And much to my surprise, I found that they were charismatic and interesting."
    kiara.say "Soon enough I began to enjoy his company when he would come to the café, trailing after Bree."
    kiara.say "And when he did not, I would feel a small pang of disappointment, but hide it from view."
    kiara.say "I flatter myself in this, but I believe that it did not take long for [hero.name]'s allegiance to change."
    kiara.say "Before too long it was apparent that he was no longer coming to the café to see Bree."
    kiara.say "Instead he was there in the hope of seeing me, which I found oddly thrilling."
    kiara.say "Because as you no doubt understand, I am a woman that had a standing in the underworld."
    kiara.say "So it was hardly like I needed the attention of a younger man to add excitement to my life."
    kiara.say "Perhaps I thought that it was a passing thing, a fling for the both of us that would soon fade."
    kiara.say "But when the relationship between us only became more intense, I made a fateful decision."
    kiara.say "I vowed that I would leave behind the life I had lead and join him in his own world."
    kiara.say "It was not an easy decision for me to make, and one that came at great cost."
    kiara.say "Because it is no simple thing to disentangle oneself from the connections of the underworld."
    kiara.say "And those same connections will often try as best they can to pull you back in again."
    kiara.say "But I persevered, and with his help, I was finally able to make a new life for myself."
    kiara.say "One that I soon found was far more rewarding and satisfying than my previous existence."
    kiara.say "Do I miss the life of an underworld kingpin?"
    kiara.say "No, I do not think that I do."
    kiara.say "And I have to say that the life of a home-maker is no less demanding."
    kiara.say "[hero.name] goes out to work every day, and expects me to keep things neat and tidy."
    kiara.say "To have a warm meal on the table for him when he comes home in the evenings."
    if kiara.is_visibly_pregnant or kiara.flags.mikeBabies >= 1:
        kiara.say "As well as to look after little Michael and see to his education."
        kiara.say "Investing in the future of our little family unit."
        kiara.say "To which I suspect there may soon be more additions."
    else:
        kiara.say "Though I suspect that there might soon be more for me to do."
        kiara.say "As [hero.name] will no doubt wish to start a family before too long."
        kiara.say "Something that I am more than ready to make happen for him."
    kiara.say "But that is not all that there is to life, oh no."
    kiara.say "I have kept myself busy, getting involved in the local Women's Institute."
    kiara.say "An organisation that, in many way, reminds me of the underworld I left behind."
    kiara.say "And one that my unique skills have allowed me to rise to the very top of too."
    kiara.say "In fact, it is surprising how much that I learned in that part of my life is useful in my new one."
    kiara.say "So maybe you can take the woman out of the underworld..."
    kiara.say "But you cannot take the underworld out of the woman."
    return


label kiara_preg_talk:
    $ kiara.flags.toldpreg = True
    show kiara normal at center, zoomAt(1.0, (640, 720))
    "I have the usual smile on my face as I see Kiara walking towards me."
    "Because who wouldn't be smiling when the beautiful woman they're dating turns up?"
    show kiara annoyed at center, traveling(1.5, 0.5, (640, 1040))
    "But that soon changes when I see that she has a serious expression on her face."
    "And when a woman like Kiara looks like that, you just know that she means business!"
    mike.say "Erm..."
    mike.say "Hi, Kiara..."
    mike.say "Is everything okay?"
    "As I say this I'm hoping that Kiara's going to suddenly snap out of it and change her mood."
    "Because it wouldn't be the first time she's shown up with her mind on other things."
    "Things that were capable of making her frown like that, and which I might help counter."
    "But my hopes are dashed when she plants her balled fists on her hips and shakes her head."
    show kiara irritated
    kiara.say "No, [hero.name]…"
    kiara.say "Everything is not okay."
    kiara.say "We have to talk about something - a very serious something!"
    show kiara annoyed
    "Almost as soon as the words are out of Kiara's mouth, I can feel my guts begin to churn."
    "Because that's something that no guy ever wants to hear coming from his other half."
    "The vague declaration that there's something so serious it requires 'a talk'."
    mike.say "Oh..."
    mike.say "Okay..."
    mike.say "Well, what exactly was it you wanted to talk about?"
    "Kiara's mouth becomes a straight, hard line."
    "And I watch as she takes in a deep breath through her nose."
    "All in all, I get the feeling that she's preparing herself for what lies ahead."
    show kiara irritated
    kiara.say "You remember when we were...having fun recently?"
    kiara.say "Specifically when we were having fun together?"
    show kiara annoyed
    "It takes me a moment to figure out what Kiara means by that."
    "But then realisation dawns on me, and I nod my head."
    mike.say "Oh yeah..."
    mike.say "How could I forget?"
    mike.say "That really was a lot of fun!"
    kiara.say "Hmm..."
    show kiara irritated
    kiara.say "Maybe we should have had a little less fun, and taken a little more care."
    show kiara annoyed
    "Again I find myself staring at Kiara as I try to decipher the meaning of her words."
    "But this time the delay on my part is more due to the gravity of what I think she's implying."
    mike.say "You mean..."
    mike.say "You mean you're..."
    show kiara whining
    kiara.say "Yes, [hero.name]…"
    kiara.say "It would appear that I am pregnant."
    kiara.say "Which would also mean that you are the baby's father."
    show kiara sadsmile
    "The force of it all seems to hit me almost the same moment that Kiara spells it out."
    "Like it couldn't have been real until someone actually said the words in front of me."
    "But now the weight of the revelation feels like it's pressing down, threatening to squash me."
    mike.say "I..."
    mike.say "I'm going to be a father?"
    show kiara whining
    kiara.say "No, [hero.name]…"
    show kiara sad
    mike.say "But you just said you were pregnant, right?"
    show kiara whining
    kiara.say "That's not what I mean..."
    show kiara sad
    mike.say "But that's what you said, just now!"
    show kiara whining
    kiara.say "NO!"
    show kiara sad
    "Kiara raises her voice and holds up her hands in an effort to silence me."
    "And it works, as I can suddenly see the strain that's contorting her face."
    show kiara whining
    kiara.say "No, [hero.name]…"
    kiara.say "I did not come to tell you that you are going to be a father."
    kiara.say "I came to tell you because I believe you have a right to know."
    kiara.say "That you should be told before I arrange to get rid of it."
    show kiara sad
    "I was silent before on account of Kiara cutting me off."
    "But I'm speechless now from genuine shock and confusion."
    mike.say "You..."
    mike.say "You can't be serious?!?"
    "I can see from the look in Kiara's eyes that she's not trying to be cruel."
    "And I think there's part of her that wants to open up to me right now."
    "But she also seems to be more than determined to make her point."
    show kiara whining
    kiara.say "But of course I am serious, [hero.name]!"
    kiara.say "I am a businesswoman with many responsibilities."
    kiara.say "Not some young girl in the first flush of youth."
    kiara.say "There is no way that I can become a mother, not now."
    show kiara sad
    "I want to be able to go away and digest all of the things that I've been told."
    "But there doesn't seem to be any time for that, as Kiara's mind is made up."
    "So I feel like I'm reeling here, doing the best I can to keep up with what's happening to me."
    mike.say "You want a termination?"
    mike.say "You want me to agree to getting rid of it?"
    show kiara whining
    kiara.say "No, [hero.name], my mind is already made up."
    kiara.say "I just wanted to tell you before it happens."
    show kiara sad
    menu:
        "If you don't want to keep it then I'm not gonna force you...":
            "I feel like I've run at full speed into a brick wall."
            "Kiara's just told me that she's pregnant with my child."
            "But then, just as bluntly, she's told me she wants to get rid of it too!"
            "Part of me wants to scream and shout like madman."
            "Part of me wants to grab her by the shoulders and plead with her."
            "But another part of me, maybe a more selfish part, doesn't want to lose her."
            "And in the end, that's the part of me that seems to win."
            mike.say "Okay, Kiara..."
            mike.say "If that's what you want, then I'll respect your wishes."
            "Kiara nods as I agree to let her have her way."
            "And as she does so, I see a relief in her eyes."
            "Like she's finally able to let her guard down."
            show kiara whining
            kiara.say "Thank you, [hero.name]."
            kiara.say "I know that I said I would have my way regardless..."
            kiara.say "But having your approval is still important to me."
            show kiara sadsmile
            "I nod, silently letting Kiara know that I understand."
            "And all the time I'm telling myself that this is just how things have played out now."
            "Who knows what the future has in store for the two of us."
            "And there's always the chance that we could try again."
            "That circumstances might change to make raising a family possible."
            $ kiara.love += 10
            $ kiara.unpreg()
        "You can't give up on this child!":
            "I feel like my head is spinning right now, like the whole world's gone crazy."
            "But in the middle of it all, I keep thinking about how much I want to be with Kiara."
            "And the idea of us having a baby together, of starting a family..."
            "Well, that just feels like the perfect way to cement our relationship for good."
            "And so before I fully know what I'm doing, the words are coming out of my mouth."
            "I'm trying to change her mind and to make her forget about getting a termination."
            mike.say "That's the craziest thing I ever heard, Kiara!"
            mike.say "You're the strongest woman I ever met, you know that?"
            mike.say "You're totally crushing being a businesswoman."
            mike.say "And I bet you'd be a brilliant mom too!"
            "Kiara shakes her head, trying to dismiss everything I just said."
            show kiara whining
            kiara.say "[hero.name]…"
            kiara.say "I know what you are trying to do..."
            kiara.say "But..."
            show kiara sad
            "The only problem is that I'm not in the mood to let her stop me now."
            "Not when I'm on a roll like this one."
            mike.say "Hear me out, please..."
            mike.say "Because it's not like you'd be on your own either, is it?"
            mike.say "You'd have me to pick up the slack, and I'm not scared of being a stay-at-home dad!"
            if kiara.love >= 150:
                show kiara stuned
                "I can see something starting to change in Kiara's demeanour."
                "Before now she had all of her defences up and was fighting me."
                "But now I think they're starting to come down as she listens to me."
                show kiara surprised
                kiara.say "I..."
                kiara.say "I wanted to think that it might be possible..."
                kiara.say "But I have always had to sacrifice in life."
                kiara.say "Always had to give up on my dreams to achieve success."
                show kiara stuned
                "I take this as my cue to step forwards and take Kiara's hands in my own."
                mike.say "That was before you had me, Kiara..."
                mike.say "Before you had someone that was there to share the burden."
                mike.say "I'm here to share your sacrifice and to make your dreams a reality."
                "Kiara stares into my eyes as I say all of this."
                "Almost like she can't believe what she's hearing."
                "But then she nods her head."
                show kiara talkative
                kiara.say "I believe that you are telling the truth, [hero.name]."
                kiara.say "And I believe that, together, we can do it!"
                show kiara smile
                "With that, Kiara leans her head against my chest."
                "And I pull her into an embrace, holding her tightly."
                $ kiara.love += 5
                $ kiara.sub += 7
            else:
                show kiara whining
                kiara.say "Please stop it!"
                kiara.say "I already told you, my mind is made up."
                show kiara sad
                "This time there's a finality in Kiara's voice that stops me dead."
                "One that tells me there's no point in arguing anymore."
                mike.say "Okay, Kiara..."
                mike.say "If that's what you want, then I'll respect your wishes."
                "Kiara nods as I agree to let her have her way."
                "And as she does so, I see a relief in her eyes."
                "Like she's finally able to let her guard down."
                show kiara talkative
                kiara.say "Thank you, [hero.name]."
                kiara.say "I know that I said I would have my way regardless..."
                kiara.say "But having your approval is still important to me."
                show kiara sad
                "I nod, silently letting Kiara know that I understand."
                "And all the time I'm telling myself that this is just how things have played out now."
                "Who knows what the future has in store for the two of us."
                "And there's always the chance that we could try again."
                "That circumstances might change to make raising a family possible."
                $ kiara.sub -= 10
                $ kiara.unpreg()
    return

label kiara_sub_event_01:
    if kiara.sub.max < 50:
        $ kiara.sub.max = 50
    "I've been around Kiara long enough by now to know when there's something bugging her."
    "And I'd also like to think that the bond between us is strong enough for me to ask her about it too."
    show kiara dreaming at center, zoomAt(1.25, (640,900)) with dissolve
    "So when I see that she's more than a little distracted, I make a point of bringing it up."
    mike.say "Kiara..."
    mike.say "Penny for your thoughts?"
    "Kiara looks distracted as she turns to face me, her expression vague."
    show kiara annoyed
    "But then as she thinks about what I just said, she begins to frown."
    show kiara angry
    kiara.say "What are you trying to say, [hero.name]?"
    kiara.say "That you value my thoughts so little?"
    kiara.say "You think they are worth no more than that?"
    show kiara annoyed
    "I shake my head, realising that Kiara's totally misunderstood me."
    mike.say "No, Kiara..."
    mike.say "Sorry, that's not what I mean at all!"
    mike.say "It's an old saying, you know, a turn of phrase?"
    mike.say "It means I'd pay to know what's on your mind."
    show kiara stuned
    "Kiara's irritation is soon replaced by confusion."
    "But at least she doesn't seem to be annoyed with me anymore."
    show kiara surprised
    kiara.say "That is such a strange way of putting it!"
    show kiara talkative
    kiara.say "Maybe next time you should just ask to know what I am thinking?"
    show kiara normal
    "I can't help nodding, as that would make things simpler for everyone involved."
    "But right now I'm still more interested in hearing what's bothering Kiara."
    mike.say "Maybe I will, Kiara."
    mike.say "But I still want to know what's on your mind."
    show kiara serious
    "Now I see Kiara hesitate, as though she's reluctant to speak up."
    show kiara annoyed
    mike.say "You know another saying is 'a problem shared is a problem halved', right?"
    "For a moment I don't think that Kiara's going to take me up on the offer."
    show kiara normal
    "But then she lets out a sigh and begins to talk."
    if "kiara_event_07b" in DONE:

        show kiara whining
        kiara.say "Oh, [hero.name]…"
        kiara.say "You have no idea how I am haunted by my former life as a gangster..."
        kiara.say "I...I mean a legitimate business-person."
        kiara.say "Even though I have put that behind me and begun anew..."
        kiara.say "The memories of it haunt me until I fall asleep at night."
        kiara.say "And they return as soon as I awake every morning."
        kiara.say "There is no way for me to escape them!"
    else:

        show kiara whining
        kiara.say "Oh, [hero.name]…"
        kiara.say "You have no idea what it's like to be a woman and a gangster..."
        kiara.say "I...I mean legitimate business-person."
        kiara.say "The pressures on me are immense and they never cease."
        kiara.say "They haunt me until I fall asleep at night."
        kiara.say "And they return the very moment I awake every morning."
        kiara.say "There is no way I can escape them!"
    show kiara sad
    "I can hear the weight of Kiara's problems in her voice as she tells me all about them."
    "And I know without the need to ask any more of her that she's being totally honest and truthful."
    "But the problem is that I need to be able to do something that will help her."
    "Something that goes beyond simply listening and nodding my head."
    mike.say "You know, Kiara..."
    mike.say "This kind of fells like a confession."
    show kiara sadsmile
    "I've never raised the subject of spiritual beliefs with Kiara before now."
    "Not for any particular reason, it was just something that didn't come up in conversation."
    show kiara normal
    "But I can see that the comparison strikes a chord with her, as she nods eagerly."
    show kiara talkative
    kiara.say "Yes, very much so."
    kiara.say "But you are not a priest, [hero.name]."
    show kiara normal
    mike.say "Does that really matter?"
    show kiara talkative
    kiara.say "What do you mean?"
    show kiara normal
    mike.say "Maybe you should still confess to me, Kiara..."
    mike.say "Get down on your knees and unburden yourself to me."
    mike.say "Let me be the one to take on the responsibility, while you put yourself in my hands."
    show kiara normal
    "The recognition in Kiara's eyes is slowly turning into something else entirely."
    "Building in intensity until it reminds me of a flame burning within her."
    show kiara talkative
    kiara.say "You would do that for me?"
    kiara.say "You would let me put myself in your hands?"
    show kiara sadsmile
    "I nod, expecting to have to explain myself to Kiara in more detail."
    show kiara confident at center, traveling( 1.25, 0.7, (640, 1080))
    "But then she surprises me by bowing her head and kneeling down."
    "And yeah, I really mean that - she gets down on her knees in front of me!"
    show kiara talkative
    kiara.say "I am ready to confess, [hero.name]…"
    kiara.say "So may we begin?"
    show kiara normal
    "I'm still a little thrown by how quickly Kiara went with the idea."
    "And so it takes me a couple of seconds to get my brain in gear."
    mike.say "Uh..."
    mike.say "Yeah, sure..."
    mike.say "So confess to me, Kiara - put yourself in my hands."
    show kiara confident at startle(0.3, 15)
    "Kiara lowers her head, nodding at the same time."
    show kiara talkative
    kiara.say "I confess that I have always needed to appear strong and resilient."
    kiara.say "That the path I have walked required me to seem like I had a heart of stone."
    kiara.say "But the truth is that I have withered and died inside because of this."
    kiara.say "In my heart of hearts, I do not desire to lead or to command."
    kiara.say "No, this life has left me weary and drained, an empty shell of a woman."
    kiara.say "What I desire most is to be relieved of my burdens."
    show kiara normal
    "Kiara raises her hands, fingers intertwined, almost like she's praying."
    mike.say "If that's what you really want, Kiara..."
    mike.say "All you have to do is say the words."
    show kiara talkative
    kiara.say "It is, [hero.name], it is!"
    show kiara normal
    mike.say "Then say it!"
    show kiara talkative
    kiara.say "Ah..."
    kiara.say "The strain is too much for me - I must do as you command..."
    kiara.say "I...I put all of my burdens in your hands!"
    show kiara normal with hpunch
    "Kiara finally breaks, throwing her arms around my legs and clingning onto me."
    "And I can almost feel the intensity of the emotions flooding through her right now."
    scene bg black with dissolve
    return

label kiara_sub_event_02:
    if kiara.sub.max < 75:
        $ kiara.sub.max = 75
    show kiara normal at center, zoomAt(1.25, (640,900)) with dissolve
    "The memory of Kiara getting down on her knees and confessing to me is still fresh in my mind."
    "And it's made all the more prominent by the fact that she seems to have really benefited from it."
    "Her moods have been much better since it happened, and she appears to be more upbeat in general."
    show kiara confident at center, traveling( 1.25, 0.7, (640, 1080))
    "Which is why it comes as a surprise to me that, as soon as we're alone, she gets down on her knees again."
    show kiara normal
    "I watch what Kiara's doing, my eyes going wide as she clasps her hands together and looks me in the eye."
    mike.say "What's the matter, Kiara?"
    mike.say "Are you feeling overwhelmed again?"
    mike.say "Because it isn't that long since your last...confession."
    "Kiara stares up at me, her eyes already letting me know that she's on the verge of pleading."
    "That there's something desperate inside of her that's already straining to get out."
    show kiara talkative
    kiara.say "I...I know that, [hero.name]…"
    kiara.say "It's just that confessing to you..."
    kiara.say "Well, it made me feel so liberated, so freed from my burdens."
    show kiara normal
    mike.say "Yeah, Kiara..."
    mike.say "Talking openly about your problems will do that."
    "As soon as I start referring to what we did like it was a therapy session, Kiara's mood changes."
    "She shakes her head and reaches out with both hands, grabbing hold of mine and refusing to let go."
    show kiara talkative
    kiara.say "No, no, no..."
    kiara.say "It was not like that, [hero.name]…"
    kiara.say "What I felt was deeper, more powerful - almost spiritual!"
    show kiara normal
    "Okay, so Kiara's really into this whole confessional thing."
    "Which means that I should probably start giving it more respect too."
    "Because I have to confess that it's kind of a turn-on to have her on her knees like this!"
    mike.say "That's great, Kiara."
    mike.say "So what are you telling me?"
    mike.say "That you want to confess to me whenever things get too heavy for you?"
    "Kiara shakes her head, now yanking on my hands as she starts to plead with me."
    show kiara talkative
    kiara.say "No, [hero.name]…"
    kiara.say "I only wish that it were enough to satisfy me!"
    kiara.say "I know that it's wicked and wanton of me to even be asking this..."
    kiara.say "But I want more!"
    kiara.say "Will you give it to me?"
    show kiara normal
    "Kiara's passion is really starting to impress me, to make me believe she's sincere."
    "But it feels like there's something underneath all of this that I haven't tapped into yet."
    "So I nod and do the best I can to look authoritative and like I know what I'm doing."
    mike.say "Of course I will, Kiara."
    mike.say "But there has to be a price, you understand?"
    mike.say "The greater the indulgence on my part, the greater the submission on yours."
    "Kiara's eyes are wide by now, looking at me with a desperate need to be saved."
    "And she doesn't hesitate to nod her head, agreeing to my terms."
    show kiara talkative
    kiara.say "Yes, of course..."
    kiara.say "I will do whatever you ask of me."
    kiara.say "I...have only confessed the least of my burdens to you so far."
    kiara.say "That I had always doubted my fitness for the roles that I found myself in."
    kiara.say "But the truth is that the root of all my insecurities is my lack of belief in myself."
    kiara.say "I believe that I could accept my role in the underworld not because I am strong..."
    kiara.say "But because I believe that I am worthless as a person, and so being a criminal did not matter!"
    show kiara normal
    "Kiara's head drops as she makes her confession, as if it presses heavily on her."
    "And the act of voicing it is physically exhausting, leaving her drained."
    mike.say "Believe that I can help you, Kiara."
    mike.say "But I will need two things from you in return."
    show kiara talkative
    kiara.say "Just name them, [hero.name]…"
    kiara.say "Tell me what they are and I will do them!"
    show kiara normal
    mike.say "The first is total obedience."
    mike.say "To do exactly as I say, without question."
    mike.say "The second is to strip away the layers of deception you have built up around yourself."
    mike.say "And we do that in a symbolic fashion, by stripping away what you're wearing."
    "I can see that Kiara's listening intently to what I'm saying."
    show kiara confident at startle(0.3, 15)
    "Nodding her head to show that she understands and too."
    "And without hesitation, she begins to do as she's told."
    "Unfastening the buttons of what she's wearing and peeling it off."
    show kiara underwear with dissolve
    "Little by little her body is revealed as she removes her clothes."
    "Soon the outer layer is gone and Kiara's kneeling before me in her underwear."
    show kiara naked with dissolve
    "But still she keeps going, unhooking her bra and shouldering out of it."
    "Then pulling down her panties and tossing them aside to that she's totally naked."
    show kiara normal
    "Kiara looks up at me again, her eyes silently asking what she must do next."
    "And it's a damn hard thing to keep my mind focussed on the task at hand."
    "Because all I really want to do is get my hands on that damn fantastic body of hers!"
    mike.say "Go sit in the chair, Kiara."
    mike.say "And take hold of the arms."
    show kiara at center, traveling(1.25, 0.4, (640,900))
    "Kiara nods and hurries to obey, rising only to dart to the nearest chair."
    "And while she sits down, I busy myself looking for what I'm going to need next."
    if "kiara_event_07b" in DONE:

        "My eyes settle on Kiara's purse, and I see something that might work."
        "A flourish of colour leading me to two fine silk scarves."
        "Which I quickly pluck out of the purse and tie around her wrists."
        "Then I tie the other end to the arms of the chair."
    else:

        "My eyes settle on Kiara's purse, and I see something that might work."
        "The glint of metal leading me to two pairs of handcuffs."
        "Which I quickly pluck out of the purse and fasten around her wrists."
        "Then I attach the other end to the arms of the chair."
    "This means that Kiara's bound in place, unable to get up from her seat."
    "But she doesn't seem to be in the mood to struggle or protest."
    show kiara normal
    "Instead she looks up at me just like before, still awaiting my next instruction."
    "Though now we have come to the point where I don't have to hold back as much as before."
    "When I can finally indulge myself and relieve some of the pressure I'm feeling."
    "My hands reach out and cradle Kiara's head, touching either side of her jawline."
    show kiara flirt
    "And the moment that I make contact with her, she lets out a pretty dramatic sigh."
    "Letting me know that I'm not the only one feeling the tension exists between us."
    kiara.say "Ah..."
    show kiara confident
    kiara.say "Mmm…"
    show kiara normal
    "I slide my hands gently downwards, caressing Kiara's neck."
    "And at the same time I begin to issue commands as well."
    mike.say "Unburden yourself, Kiara..."
    mike.say "Dig down deep into your soul..."
    mike.say "And release what's been trapped down there all these years."
    show kiara talkative
    kiara.say "Y...yes..."
    kiara.say "I will...obey!"
    show kiara normal
    "I move my hands over Kiara's shoulders, tracing their lines to her arms."
    "Then describe the curve below them, sweeping around to the front of her chest."
    show kiara talkative
    kiara.say "I have never done anything with the best of intentions."
    kiara.say "Always choosing the path that I thought looked like the best..."
    kiara.say "But secretly suspected would result in failure!"
    kiara.say "Oh..."
    show kiara normal
    show sexinserts chest kiara zorder 1 at center, zoomAt(1, (670, 740))
    with dissolve
    "I reward Kiara's confession by cupping her breasts in my hands."
    "Using my fingers and thumbs to pinch and squeeze her nipples."
    "Which respond by instantly stiffening at my attentions."
    show kiara talkative
    kiara.say "I...I chose my henchmen in the same way..."
    kiara.say "Favouring the headstrong and overconfident."
    kiara.say "Always hoping they would prove to be unworthy!"
    show kiara flirt
    hide sexinserts
    show sexinserts belly kiara zorder 2 at center, zoomAt(1, (640, 600))
    with dissolve
    "I let go of Kiara's breasts and stroke the palms of my hands over her stomach."
    "Inching ever closer to her waist and what lies below, totally exposed."
    "She tries to pull her legs together, thighs pressing against each other."
    "But it's too late to keep one of my hands from wedging itself between them."
    hide sexinserts
    show sexinserts bottom kiara zorder 2 at center, zoomAt(0.75, (0, 920))
    with dissolve
    "And in the next instant, my fingers begin to caress the lips of her pussy."
    show kiara tasty
    kiara.say "Ungh…"
    show kiara talkative
    kiara.say "I...I made sure my operations were seen by the police."
    kiara.say "That eventually they would see through any and all cover."
    kiara.say "Because I...I wanted to be caught!"
    show kiara flirt
    "The tips of my fingers are sinking into Kiara as she makes this last confession."
    "Her pussy already softened enough to allow them to slide all the way into her."
    show kiara confident
    "She moans helplessly as I rub, stroke and caress her from the inside."
    "Seeing the pleasure and the revelations coming out of her as equal parts of what we're doing here."
    "That last one was the biggest yet, maybe even the confessional equivalent of a climax."
    show kiara shout with vpunch
    "And so it doesn't surprise me when I feel Kiara's entire body tense a moment later."
    "Shudders spreading out form her centre as she loses it and succumbs."
    show kiara confident
    hide sexinserts
    with dissolve
    "Releasing Kiara from the bonds that hold her in place I watch as she slither out of the chair."
    show kiara flirt
    "Ending up a helpless heap of limbs at my feet, still gasping from the effects of her orgasm."
    show kiara talkative
    kiara.say "Th...thank you..."
    kiara.say "Thank you so much!"
    scene bg black with dissolve
    return

label kiara_sub_event_03:
    if kiara.sub.max < 100:
        $ kiara.sub.max = 100
    kiara.say "[hero.name]!"
    kiara.say "Please, wait..."
    kiara.say "I...I need you!"
    "I recognise Kiara's voice the very same moment that I hear it behind me."
    "But what I don't recognise and what worries me is the tone of it."
    "In the past I've been used to hearing Kiara speak with a cool air of authority."
    "Yet now the sound that reaches my ears is one of helplessness and desperation."
    mike.say "Kiara?"
    mike.say "What's the matter?!?"
    if game.room == 'maidcafe':
        show kiara work sad at center, zoomAt(1.25, (640,900)) with easeinright
    else:
        show kiara date sad at center, zoomAt(1.25, (640,900)) with easeinright
    "I turn just in time to see Kiara come staggering towards me."
    show kiara at center, traveling( 1.25, 0.3, (640, 1080)) with ease
    "And then, before I can reach her, she half kneels, half collapses in front of me."
    "Clasping her hands together like she's offering up a desperate prayer for salvation."
    show kiara serious at center, traveling( 1.5, 0.5, (640, 1180))
    "Then bowing down so that her forehead is touching the ground an inch from my feet."
    show kiara shout
    kiara.say "I can't do it anymore, [hero.name]…"
    kiara.say "I can't go on without you telling me what to do!"
    show kiara serious
    "Okay normally I'm more than down with the idea of a woman doing what I tell them."
    "Because obedience has always been a real turn-on as far as I'm concerned."
    "But this is a whole different level to the kind of submission that I'm used to."
    mike.say "Okay, Kiara..."
    mike.say "I'm guessing this is about the little confession sessions that we've been having, yeah?"
    mike.say "You feel like you need to unburden yourself of some more repressed thoughts and emotions?"
    show kiara tantrum
    kiara.say "NO..."
    show kiara whining
    kiara.say "Not this time!"
    show kiara sad
    "Kiara raises her head just enough to be able to make eye-contact with me."
    "And I can see that there's an almost feverish intensity in her stare."
    show kiara whining
    kiara.say "I need more than that, please!"
    kiara.say "Your commands are the only thing that works for me now."
    kiara.say "They're the only thing that can stop the doubts..."
    kiara.say "The only thing that silences the voices that come in the darkness!"
    show kiara sad
    "I do the best that I can to hide the impact Kiara's pleas are having on me."
    "Because the truth is that I'm amazed at what my efforts seem to have done to her."
    "We've gone from me trying to make her unburden herself to what looks like total dependence."
    "And I'm beginning to wonder just how much Kiara's come to need my influence to function."
    mike.say "So..."
    mike.say "You're saying that you need me to..."
    show kiara whining
    kiara.say "Tell me what to do, [hero.name]!"
    kiara.say "Command me and I will obey."
    kiara.say "I need you to be my...to be my master!"
    show kiara sadsmile
    "Something weird seems to happen to me the moment that Kiara uses that word."
    "As soon as she asks me to be her master, all of my misgivings seem to vanish."
    "Where before I was worried about where this was leading us, now I'm calm and even confident."
    "Maybe all I needed to hear was Kiara asking me to assume control, giving me her permission."
    "But whatever the reason, everything just seems to fall into place for me now."
    mike.say "Then that's exactly what I'll be."
    mike.say "From now on you'll call me that, Kiara..."
    mike.say "You'll call me 'Master' and obey my every command."
    show kiara normal
    "Kiara nods eagerly at this."
    show kiara talkative
    kiara.say "Yes..."
    kiara.say "Yes, Master!"
    show kiara normal
    mike.say "And my first command is to take off all those clothes."
    mike.say "How am I supposed to know what's mine if I can't see it?"
    show kiara at center, traveling( 1.25, 0.7, (640, 1080))
    "Again Kiara nods, beginning to rise from where she's been kneeling."
    "But I raise a hand before she can even get off of her knees."
    mike.say "No, don't get up..."
    mike.say "Stay down there until I tell you otherwise."
    mike.say "Stay there and present yourself to me for inspection."
    show kiara flirt
    "Kiara hurries to obey my commands, her cheeks flushing a deep shade of red as she does so."
    "But at the same time I can see that she's more than eager to follow my orders."
    show kiara naked normal with dissolve
    "She hastily tears at the buttons and zippers of the clothes that she's wearing."
    "Pulling off every piece of clothing without regard for stretching or tearing them."
    "And then casting them aside until she's stripped naked in front of me."
    scene bg black
    show expression f"kiara doggy {'maidcafe' if game.room == 'maidcafe' else 'stripclub'} closed nomc"
    with fade
    "That done, Kiara rolls over and positions herself on all fours."
    show kiara doggy normal
    kiara.say "I am ready, Master..."
    kiara.say "Ready to be inspected."
    show kiara doggy closed
    "I walk slowly around Kiara as she rests on her hands and knees."
    "Making a full circuit of her and taking in every inch of her body."
    "Sure, it's a thrill to see her naked and exposed like this."
    "But what makes it even better is the look on her face right now."
    "The effort that she's putting into suppressing her embarrassment and keeping still."
    "To me it almost feels like an electrical charge, building up in the air between us."
    show kiara doggy normal
    kiara.say "M...Master..."
    kiara.say "May I say something?"
    show kiara doggy closed
    mike.say "What is it, Kiara?"
    show kiara doggy normal
    kiara.say "There is something in my purse."
    kiara.say "Something that you might want to use."
    show kiara doggy closed
    "I raise a quizzical eyebrow as Kiara tips me off towards the mysterious item in her purse."
    "Keen to see just what she could think would be appropriate to bring into play at a time like this."
    "But when I pluck it up and open it, I can't help smiling as I see the thing in question."
    "Or to be more precise, the two things - a leather collar and matching leash!"
    mike.say "I see what you mean, Kiara!"
    mike.say "And yes, I do think we should use it."
    show kiara doggy at center, zoomAt(1.75, (1100, 1200))
    "I can see that Kiara's battle to keep herself under control has intensified."
    show kiara doggy closed collar
    "That she's almost shaking as I undo the collar and loop it around her neck."
    show kiara doggy closed leash mikemc -nomc
    "And once I've tightened it, I clip the leash to the metal ring hanging from it."
    "Kiara offers no resistance as I pull her backwards and against me."
    "Meaning that I can loosen my grip on her leash for a moment."
    "Just long enough to reach down and unzip my flies, then reach inside."
    mike.say "There, Kiara..."
    mike.say "Now you really do look the part."
    show kiara doggy normal
    kiara.say "Th...thank you, Master..."
    kiara.say "I am most humbly grateful to be yours!"
    show kiara doggy closed
    mike.say "Oh, you're not mine yet - not quite."
    show kiara doggy normal
    kiara.say "B...but, Master..."
    kiara.say "What can you mean?!?"
    show kiara doggy closed
    mike.say "You're not completely mine until I claim you, Kiara!"
    show kiara doggy closed leash at center, traveling(1.0, 0.5, (640, 720))
    "I underline my point by wrapping Kiara's leash tightly in one hand."
    "And then using the other to latch onto her waist."
    show kiara doggy pleasure
    kiara.say "Wha…"
    kiara.say "Oh..."
    kiara.say "Oh, Master!"
    show kiara doggy closed
    "Needless to say that I've gotten good and hard while all of this was going on."
    "And now the only thing on my mind is the need to make good use of that fact."
    "Not that Kiara seems to need any encouragement now that she's figured out my intentions."
    "Because she lowers herself even more and spreads her thighs wider still."
    "Meaning that it's no challenge for me to thrust my cock straight between them."
    play sexsfx1 slide_in
    show kiara doggy vaginal pleasure
    "The head fits right between the lines of her lips, sliding along their length."
    "And the sensation makes Kiara bear down further still, stretching her muscles."
    "As she does so, her pussy surrenders too, letting the head spring backwards."
    "From there it pops straight into her, half the shaft following it before I know what's happened."
    mike.say "Ah..."
    mike.say "Fuck..."
    show kiara doggy pleasure
    kiara.say "Ooh..."
    kiara.say "Please, Master..."
    kiara.say "Please take me?!?"
    show kiara doggy closed
    "Kiara's words are desperate, filled with a genuine need for me to do as she asks."
    "But it's not like I really need to be encouraged to do anything else right now."
    play sexsfx1 fuck_moderate loop
    show kiara doggy speed at stepback(0.07, -10, 0)
    pause 0.2
    show kiara doggy at stepback(0.07, -10, 0)
    "And I'm already beginning to thrust in and out of her as she begs me to do so."
    "This means that Kiara's words soon fade away into pure, animal moaning."
    show kiara doggy at stepback(0.07, -10, 0)
    pause 0.2
    show kiara doggy at stepback(0.07, -10, 0)
    "Her cries mixing with my own incoherent gasps as I pound away at her."
    "I have the leash in one hand and the other holding onto whatever gives me purchase."
    show kiara doggy at stepback(0.07, -10, 0)
    pause 0.2
    show kiara doggy at stepback(0.07, -10, 0)
    "The sound of our thighs slapping together almost as loud as the cries by now."
    "Don't be under any illusion that this is some poetic kind of love-making."
    show kiara doggy at stepback(0.07, -10, 0)
    pause 0.2
    show kiara doggy at stepback(0.07, -10, 0)
    "Oh no, this is just raw, animal passion being expressed without restraint."
    "Two desperate people fucking like beasts because they can't control themselves."
    show kiara doggy at stepback(0.07, -10, 0)
    pause 0.2
    show kiara doggy at stepback(0.07, -10, 0)
    "And man, does it feel good!"
    "From where I'm kneeling, I can see Kiara's buttocks jiggling."
    show kiara doggy bounce at stepback(0.07, -10, 0)
    pause 0.2
    show kiara doggy at stepback(0.07, -10, 0)
    "Her breasts swaying beneath her as she's rocked back and forth."
    show kiara doggy closed
    "And her eyes closed as she's overwhelmed by the pleasure she's feeling."
    show kiara doggy at stepback(0.07, -10, 0)
    pause 0.2
    show kiara doggy at stepback(0.07, -10, 0)
    "But when I sense the muscles of her pussy starting to tighten, I snap back to reality."
    mike.say "No, Kiara..."
    mike.say "You don't...don't cum..."
    mike.say "Not until...I tell you!"
    show kiara doggy ahegao blush
    kiara.say "Uh..."
    kiara.say "Y..yes...yes, Master!"
    "I can literally feel the effect that my words have on Kiara."
    show kiara doggy at stepback(0.07, -10, 0)
    pause 0.2
    show kiara doggy at stepback(0.07, -10, 0)
    "The effort that she's putting into keeping herself from cuming."
    "And the power that signifies suddenly hits me like a rush of adrenaline."
    play sexsfx1 final_thrust
    show kiara doggy cum shake with hpunch
    "A moment later I feel myself lose it, shooting my load into Kiara."
    with hpunch
    mike.say "Argh..."
    mike.say "N...now, Kiara..."
    mike.say "Now you can cum!"
    show kiara doggy orgasm -speed -bounce -shake with hpunch
    "Almost the moment that I'm done giving her permission, Kiara climaxes too."
    "Arching her back and pushing herself against me so that she's rearing up."
    show kiara doggy closed
    "And then she shudders, slowly collapsing into a heap in front of me."
    play sexsfx1 slide_out
    show kiara doggy out -cum
    "My cock sliding out of her as she curls herself into a ball at my feet."
    show kiara doggy cum_puddle nomc with fade
    "I take some time to clean myself up and get my head back together."
    "And I wait as Kiara takes a significantly longer time to do the same."
    call stop_all_sfx from _call_stop_all_sfx_73
    scene expression f"bg {game.room}"
    if game.room == 'maidcafe':
        show kiara work collar at center, zoomAt( 1.5, (640, 1080))
    else:
        show kiara date collar at center, zoomAt( 1.5, (640, 1080))
    with fade
    "Silently collecting her clothes and dressing herself, then walking to my side."
    "Once there, she silently hands me her leash, acknowledging what's changed between us."
    "The level of connection meaning that not a single word passes our lips."
    "And then together, we walk out, her a step behind me."

    if "kiara_event_07b" in DONE:
        scene bg park
        show kiara date collar smile at center, zoomAt( 1.5, (640, 1080))
        with fade
        "I make a point of walking down to the park, holding onto Kiara's leash."
        "Doing nothing to hide it and the collar from everyone that we see on the way."
        "I can feel that all of their eyes are on us right now."
        "And I can't imagine what must be going through their minds."
        "But I know that this needs to be seen and acknowledged."
        "That the shift in power must be made official for it to work."
        "Everything's changed, and it's time for the world to know it."
    else:

        scene bg nightclub
        show kiara date collar smile at center, zoomAt( 1.5, (640, 1080))
        with fade
        "I make a point of walking into the club, holding onto Kiara's leash."
        "Doing nothing to hide it and the collar from everyone in there."
        "I can feel that all of their eyes are on us right now."
        "And I can't imagine what must be going through their minds."
        "But I know that this needs to be seen and acknowledged."
        "That the shift in power must be made official for it to work."
        "Everything's changed, and it's time for the world to know it."
    $ kiara.set_sex_slave()
    $ kiara.flags["giftslave_collar"] = True
    scene bg black with dissolve
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
